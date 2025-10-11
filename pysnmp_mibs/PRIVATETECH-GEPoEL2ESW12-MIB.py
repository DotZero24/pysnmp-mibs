# SNMP MIB module (PRIVATETECH-GEPoEL2ESW12-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rubytech/PRIVATETECH-GEPoEL2ESW12-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:43 2025
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

privatetech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1)
)
_Gepoel2esw12ProductId_ObjectIdentity = ObjectIdentity
gepoel2esw12ProductId = _Gepoel2esw12ProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24)
)
_Gepoel2esw12System_ObjectIdentity = ObjectIdentity
gepoel2esw12System = _Gepoel2esw12System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1)
)
_Gepoel2esw12SystemInformation_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemInformation = _Gepoel2esw12SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1)
)
_Gepoel2esw12ModelName_Type = DisplayString
_Gepoel2esw12ModelName_Object = MibScalar
gepoel2esw12ModelName = _Gepoel2esw12ModelName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 1),
    _Gepoel2esw12ModelName_Type()
)
gepoel2esw12ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ModelName.setStatus("current")
_Gepoel2esw12BIOSVersion_Type = DisplayString
_Gepoel2esw12BIOSVersion_Object = MibScalar
gepoel2esw12BIOSVersion = _Gepoel2esw12BIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 2),
    _Gepoel2esw12BIOSVersion_Type()
)
gepoel2esw12BIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12BIOSVersion.setStatus("current")
_Gepoel2esw12FirmwareVersion_Type = DisplayString
_Gepoel2esw12FirmwareVersion_Object = MibScalar
gepoel2esw12FirmwareVersion = _Gepoel2esw12FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 3),
    _Gepoel2esw12FirmwareVersion_Type()
)
gepoel2esw12FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12FirmwareVersion.setStatus("current")
_Gepoel2esw12HardwareMechanicalVersion_Type = DisplayString
_Gepoel2esw12HardwareMechanicalVersion_Object = MibScalar
gepoel2esw12HardwareMechanicalVersion = _Gepoel2esw12HardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 4),
    _Gepoel2esw12HardwareMechanicalVersion_Type()
)
gepoel2esw12HardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HardwareMechanicalVersion.setStatus("current")
_Gepoel2esw12SeriesNumber_Type = DisplayString
_Gepoel2esw12SeriesNumber_Object = MibScalar
gepoel2esw12SeriesNumber = _Gepoel2esw12SeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 5),
    _Gepoel2esw12SeriesNumber_Type()
)
gepoel2esw12SeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SeriesNumber.setStatus("current")
_Gepoel2esw12HostMACAddress_Type = MacAddress
_Gepoel2esw12HostMACAddress_Object = MibScalar
gepoel2esw12HostMACAddress = _Gepoel2esw12HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 6),
    _Gepoel2esw12HostMACAddress_Type()
)
gepoel2esw12HostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HostMACAddress.setStatus("current")
_Gepoel2esw12ConsoleBaudrate_Type = DisplayString
_Gepoel2esw12ConsoleBaudrate_Object = MibScalar
gepoel2esw12ConsoleBaudrate = _Gepoel2esw12ConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 7),
    _Gepoel2esw12ConsoleBaudrate_Type()
)
gepoel2esw12ConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ConsoleBaudrate.setStatus("current")
_Gepoel2esw12RAMSize_Type = DisplayString
_Gepoel2esw12RAMSize_Object = MibScalar
gepoel2esw12RAMSize = _Gepoel2esw12RAMSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 8),
    _Gepoel2esw12RAMSize_Type()
)
gepoel2esw12RAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12RAMSize.setStatus("current")
_Gepoel2esw12FlashSize_Type = DisplayString
_Gepoel2esw12FlashSize_Object = MibScalar
gepoel2esw12FlashSize = _Gepoel2esw12FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 9),
    _Gepoel2esw12FlashSize_Type()
)
gepoel2esw12FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12FlashSize.setStatus("current")
_Gepoel2esw12BridgeFBDSize_Type = DisplayString
_Gepoel2esw12BridgeFBDSize_Object = MibScalar
gepoel2esw12BridgeFBDSize = _Gepoel2esw12BridgeFBDSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 10),
    _Gepoel2esw12BridgeFBDSize_Type()
)
gepoel2esw12BridgeFBDSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12BridgeFBDSize.setStatus("current")
_Gepoel2esw12TransmitQueue_Type = DisplayString
_Gepoel2esw12TransmitQueue_Object = MibScalar
gepoel2esw12TransmitQueue = _Gepoel2esw12TransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 11),
    _Gepoel2esw12TransmitQueue_Type()
)
gepoel2esw12TransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12TransmitQueue.setStatus("current")
_Gepoel2esw12MaximumFrameSize_Type = DisplayString
_Gepoel2esw12MaximumFrameSize_Object = MibScalar
gepoel2esw12MaximumFrameSize = _Gepoel2esw12MaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 12),
    _Gepoel2esw12MaximumFrameSize_Type()
)
gepoel2esw12MaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12MaximumFrameSize.setStatus("current")
_Gepoel2esw12CPULoad_Type = DisplayString
_Gepoel2esw12CPULoad_Object = MibScalar
gepoel2esw12CPULoad = _Gepoel2esw12CPULoad_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 1, 13),
    _Gepoel2esw12CPULoad_Type()
)
gepoel2esw12CPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12CPULoad.setStatus("current")
_Gepoel2esw12SystemTime_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemTime = _Gepoel2esw12SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2)
)
_Gepoel2esw12SystemTimeManual_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemTimeManual = _Gepoel2esw12SystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1)
)


class _Gepoel2esw12SystemTimeManualClockSource_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SystemTimeManualClockSource_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualClockSource_Object = MibScalar
gepoel2esw12SystemTimeManualClockSource = _Gepoel2esw12SystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 1),
    _Gepoel2esw12SystemTimeManualClockSource_Type()
)
gepoel2esw12SystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualClockSource.setStatus("current")
_Gepoel2esw12SystemTimeManualLocaltime_Type = DisplayString
_Gepoel2esw12SystemTimeManualLocaltime_Object = MibScalar
gepoel2esw12SystemTimeManualLocaltime = _Gepoel2esw12SystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 2),
    _Gepoel2esw12SystemTimeManualLocaltime_Type()
)
gepoel2esw12SystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualLocaltime.setStatus("current")


class _Gepoel2esw12SystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Gepoel2esw12SystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualTimeZoneOffset_Object = MibScalar
gepoel2esw12SystemTimeManualTimeZoneOffset = _Gepoel2esw12SystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 3),
    _Gepoel2esw12SystemTimeManualTimeZoneOffset_Type()
)
gepoel2esw12SystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualTimeZoneOffset.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavings_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavings = _Gepoel2esw12SystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 4),
    _Gepoel2esw12SystemTimeManualDaylightSavings_Type()
)
gepoel2esw12SystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavings.setStatus("current")


class _Gepoel2esw12SystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Gepoel2esw12SystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualTimeSetOffset_Object = MibScalar
gepoel2esw12SystemTimeManualTimeSetOffset = _Gepoel2esw12SystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 5),
    _Gepoel2esw12SystemTimeManualTimeSetOffset_Type()
)
gepoel2esw12SystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualTimeSetOffset.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsType_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsType = _Gepoel2esw12SystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 6),
    _Gepoel2esw12SystemTimeManualDaylightSavingsType_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsType.setStatus("current")
_Gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom = _Gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 7),
    _Gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo = _Gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 8),
    _Gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 9),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 10),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 11),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 12),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 13),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 14),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 15),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo = _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 1, 16),
    _Gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Gepoel2esw12SystemTimeNTP_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemTimeNTP = _Gepoel2esw12SystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2)
)
_Gepoel2esw12SystemTimeNTPTable_Object = MibTable
gepoel2esw12SystemTimeNTPTable = _Gepoel2esw12SystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeNTPTable.setStatus("current")
_Gepoel2esw12SystemTimeNTPEntry_Object = MibTableRow
gepoel2esw12SystemTimeNTPEntry = _Gepoel2esw12SystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2, 1, 1)
)
gepoel2esw12SystemTimeNTPEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12SystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeNTPEntry.setStatus("current")


class _Gepoel2esw12SystemTimeNTPIndex_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gepoel2esw12SystemTimeNTPIndex_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeNTPIndex_Object = MibTableColumn
gepoel2esw12SystemTimeNTPIndex = _Gepoel2esw12SystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2, 1, 1, 1),
    _Gepoel2esw12SystemTimeNTPIndex_Type()
)
gepoel2esw12SystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeNTPIndex.setStatus("current")


class _Gepoel2esw12SystemTimeNTPServerIPType_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeNTPServerIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeNTPServerIPType_Object = MibTableColumn
gepoel2esw12SystemTimeNTPServerIPType = _Gepoel2esw12SystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2, 1, 1, 2),
    _Gepoel2esw12SystemTimeNTPServerIPType_Type()
)
gepoel2esw12SystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeNTPServerIPType.setStatus("current")
_Gepoel2esw12SystemTimeNTPServer_Type = DisplayString
_Gepoel2esw12SystemTimeNTPServer_Object = MibTableColumn
gepoel2esw12SystemTimeNTPServer = _Gepoel2esw12SystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2, 1, 1, 3),
    _Gepoel2esw12SystemTimeNTPServer_Type()
)
gepoel2esw12SystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeNTPServer.setStatus("current")


class _Gepoel2esw12SystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type gepoel2esw12SystemTimeNTPCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gepoel2esw12SystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Gepoel2esw12SystemTimeNTPCurrentMode_Object = MibTableColumn
gepoel2esw12SystemTimeNTPCurrentMode = _Gepoel2esw12SystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 2, 2, 1, 1, 4),
    _Gepoel2esw12SystemTimeNTPCurrentMode_Type()
)
gepoel2esw12SystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemTimeNTPCurrentMode.setStatus("current")
_Gepoel2esw12SystemAccount_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemAccount = _Gepoel2esw12SystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3)
)
_Gepoel2esw12SystemAccountUsers_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemAccountUsers = _Gepoel2esw12SystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1)
)


class _Gepoel2esw12SystemAccountUserCreate_Type(Integer32):
    """Custom type gepoel2esw12SystemAccountUserCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SystemAccountUserCreate_Type.__name__ = "Integer32"
_Gepoel2esw12SystemAccountUserCreate_Object = MibScalar
gepoel2esw12SystemAccountUserCreate = _Gepoel2esw12SystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 1),
    _Gepoel2esw12SystemAccountUserCreate_Type()
)
gepoel2esw12SystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SystemAccountUserCreate.setStatus("current")
_Gepoel2esw12SystemAccountUsersTable_Object = MibTable
gepoel2esw12SystemAccountUsersTable = _Gepoel2esw12SystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12SystemAccountUsersTable.setStatus("current")
_Gepoel2esw12SystemAccountUsersEntry_Object = MibTableRow
gepoel2esw12SystemAccountUsersEntry = _Gepoel2esw12SystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2, 1)
)
gepoel2esw12SystemAccountUsersEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12UserIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12SystemAccountUsersEntry.setStatus("current")


class _Gepoel2esw12UserIndex_Type(Integer32):
    """Custom type gepoel2esw12UserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Gepoel2esw12UserIndex_Type.__name__ = "Integer32"
_Gepoel2esw12UserIndex_Object = MibTableColumn
gepoel2esw12UserIndex = _Gepoel2esw12UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2, 1, 1),
    _Gepoel2esw12UserIndex_Type()
)
gepoel2esw12UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12UserIndex.setStatus("current")


class _Gepoel2esw12UserName_Type(DisplayString):
    """Custom type gepoel2esw12UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gepoel2esw12UserName_Type.__name__ = "DisplayString"
_Gepoel2esw12UserName_Object = MibTableColumn
gepoel2esw12UserName = _Gepoel2esw12UserName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2, 1, 2),
    _Gepoel2esw12UserName_Type()
)
gepoel2esw12UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12UserName.setStatus("current")


class _Gepoel2esw12Password_Type(DisplayString):
    """Custom type gepoel2esw12Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gepoel2esw12Password_Type.__name__ = "DisplayString"
_Gepoel2esw12Password_Object = MibTableColumn
gepoel2esw12Password = _Gepoel2esw12Password_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2, 1, 3),
    _Gepoel2esw12Password_Type()
)
gepoel2esw12Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Password.setStatus("current")


class _Gepoel2esw12UserPrivilegeLevel_Type(Integer32):
    """Custom type gepoel2esw12UserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12UserPrivilegeLevel_Type.__name__ = "Integer32"
_Gepoel2esw12UserPrivilegeLevel_Object = MibTableColumn
gepoel2esw12UserPrivilegeLevel = _Gepoel2esw12UserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2, 1, 4),
    _Gepoel2esw12UserPrivilegeLevel_Type()
)
gepoel2esw12UserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12UserPrivilegeLevel.setStatus("current")


class _Gepoel2esw12AccountUserRowStatus_Type(Integer32):
    """Custom type gepoel2esw12AccountUserRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gepoel2esw12AccountUserRowStatus_Type.__name__ = "Integer32"
_Gepoel2esw12AccountUserRowStatus_Object = MibTableColumn
gepoel2esw12AccountUserRowStatus = _Gepoel2esw12AccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 1, 2, 1, 5),
    _Gepoel2esw12AccountUserRowStatus_Type()
)
gepoel2esw12AccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccountUserRowStatus.setStatus("current")
_Gepoel2esw12SystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
gepoel2esw12SystemAccountPrivilegeLevel = _Gepoel2esw12SystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2)
)


class _Gepoel2esw12PrivilegeLevelAccount_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelAccount_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelAccount_Object = MibScalar
gepoel2esw12PrivilegeLevelAccount = _Gepoel2esw12PrivilegeLevelAccount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 1),
    _Gepoel2esw12PrivilegeLevelAccount_Type()
)
gepoel2esw12PrivilegeLevelAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelAccount.setStatus("current")


class _Gepoel2esw12PrivilegeLevelDiagnostics_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelDiagnostics_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelDiagnostics_Object = MibScalar
gepoel2esw12PrivilegeLevelDiagnostics = _Gepoel2esw12PrivilegeLevelDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 2),
    _Gepoel2esw12PrivilegeLevelDiagnostics_Type()
)
gepoel2esw12PrivilegeLevelDiagnostics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelDiagnostics.setStatus("current")


class _Gepoel2esw12PrivilegeLevelIP_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelIP_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelIP_Object = MibScalar
gepoel2esw12PrivilegeLevelIP = _Gepoel2esw12PrivilegeLevelIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 3),
    _Gepoel2esw12PrivilegeLevelIP_Type()
)
gepoel2esw12PrivilegeLevelIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelIP.setStatus("current")


class _Gepoel2esw12PrivilegeLevelMaintenance_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelMaintenance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelMaintenance_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelMaintenance_Object = MibScalar
gepoel2esw12PrivilegeLevelMaintenance = _Gepoel2esw12PrivilegeLevelMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 4),
    _Gepoel2esw12PrivilegeLevelMaintenance_Type()
)
gepoel2esw12PrivilegeLevelMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelMaintenance.setStatus("current")


class _Gepoel2esw12PrivilegeLevelOLT_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelOLT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelOLT_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelOLT_Object = MibScalar
gepoel2esw12PrivilegeLevelOLT = _Gepoel2esw12PrivilegeLevelOLT_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 5),
    _Gepoel2esw12PrivilegeLevelOLT_Type()
)
gepoel2esw12PrivilegeLevelOLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelOLT.setStatus("current")


class _Gepoel2esw12PrivilegeLevelONU_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelONU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelONU_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelONU_Object = MibScalar
gepoel2esw12PrivilegeLevelONU = _Gepoel2esw12PrivilegeLevelONU_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 6),
    _Gepoel2esw12PrivilegeLevelONU_Type()
)
gepoel2esw12PrivilegeLevelONU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelONU.setStatus("current")


class _Gepoel2esw12PrivilegeLevelSMTP_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelSMTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelSMTP_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelSMTP_Object = MibScalar
gepoel2esw12PrivilegeLevelSMTP = _Gepoel2esw12PrivilegeLevelSMTP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 7),
    _Gepoel2esw12PrivilegeLevelSMTP_Type()
)
gepoel2esw12PrivilegeLevelSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelSMTP.setStatus("current")


class _Gepoel2esw12PrivilegeLevelSNMP_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelSNMP_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelSNMP_Object = MibScalar
gepoel2esw12PrivilegeLevelSNMP = _Gepoel2esw12PrivilegeLevelSNMP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 8),
    _Gepoel2esw12PrivilegeLevelSNMP_Type()
)
gepoel2esw12PrivilegeLevelSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelSNMP.setStatus("current")


class _Gepoel2esw12PrivilegeLevelSecurity_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelSecurity_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelSecurity_Object = MibScalar
gepoel2esw12PrivilegeLevelSecurity = _Gepoel2esw12PrivilegeLevelSecurity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 9),
    _Gepoel2esw12PrivilegeLevelSecurity_Type()
)
gepoel2esw12PrivilegeLevelSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelSecurity.setStatus("current")


class _Gepoel2esw12PrivilegeLevelSystem_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelSystem_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelSystem_Object = MibScalar
gepoel2esw12PrivilegeLevelSystem = _Gepoel2esw12PrivilegeLevelSystem_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 10),
    _Gepoel2esw12PrivilegeLevelSystem_Type()
)
gepoel2esw12PrivilegeLevelSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelSystem.setStatus("current")


class _Gepoel2esw12PrivilegeLevelTrapEvent_Type(Integer32):
    """Custom type gepoel2esw12PrivilegeLevelTrapEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gepoel2esw12PrivilegeLevelTrapEvent_Type.__name__ = "Integer32"
_Gepoel2esw12PrivilegeLevelTrapEvent_Object = MibScalar
gepoel2esw12PrivilegeLevelTrapEvent = _Gepoel2esw12PrivilegeLevelTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 3, 2, 11),
    _Gepoel2esw12PrivilegeLevelTrapEvent_Type()
)
gepoel2esw12PrivilegeLevelTrapEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PrivilegeLevelTrapEvent.setStatus("current")
_Gepoel2esw12IP_ObjectIdentity = ObjectIdentity
gepoel2esw12IP = _Gepoel2esw12IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4)
)
_Gepoel2esw12IPv4_ObjectIdentity = ObjectIdentity
gepoel2esw12IPv4 = _Gepoel2esw12IPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1)
)
_Gepoel2esw12IPv4Configured_ObjectIdentity = ObjectIdentity
gepoel2esw12IPv4Configured = _Gepoel2esw12IPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1)
)


class _Gepoel2esw12Ipv4DHCPClient_Type(Integer32):
    """Custom type gepoel2esw12Ipv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12Ipv4DHCPClient_Type.__name__ = "Integer32"
_Gepoel2esw12Ipv4DHCPClient_Object = MibScalar
gepoel2esw12Ipv4DHCPClient = _Gepoel2esw12Ipv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 1),
    _Gepoel2esw12Ipv4DHCPClient_Type()
)
gepoel2esw12Ipv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv4DHCPClient.setStatus("current")
_Gepoel2esw12IPv4Address_Type = IpAddress
_Gepoel2esw12IPv4Address_Object = MibScalar
gepoel2esw12IPv4Address = _Gepoel2esw12IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 2),
    _Gepoel2esw12IPv4Address_Type()
)
gepoel2esw12IPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4Address.setStatus("current")
_Gepoel2esw12IPv4Mask_Type = IpAddress
_Gepoel2esw12IPv4Mask_Object = MibScalar
gepoel2esw12IPv4Mask = _Gepoel2esw12IPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 3),
    _Gepoel2esw12IPv4Mask_Type()
)
gepoel2esw12IPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4Mask.setStatus("current")
_Gepoel2esw12IPv4Router_Type = IpAddress
_Gepoel2esw12IPv4Router_Object = MibScalar
gepoel2esw12IPv4Router = _Gepoel2esw12IPv4Router_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 4),
    _Gepoel2esw12IPv4Router_Type()
)
gepoel2esw12IPv4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4Router.setStatus("current")


class _Gepoel2esw12IPv4VLANId_Type(Integer32):
    """Custom type gepoel2esw12IPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gepoel2esw12IPv4VLANId_Type.__name__ = "Integer32"
_Gepoel2esw12IPv4VLANId_Object = MibScalar
gepoel2esw12IPv4VLANId = _Gepoel2esw12IPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 5),
    _Gepoel2esw12IPv4VLANId_Type()
)
gepoel2esw12IPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4VLANId.setStatus("current")
_Gepoel2esw12IPv4DNSServer_Type = IpAddress
_Gepoel2esw12IPv4DNSServer_Object = MibScalar
gepoel2esw12IPv4DNSServer = _Gepoel2esw12IPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 6),
    _Gepoel2esw12IPv4DNSServer_Type()
)
gepoel2esw12IPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4DNSServer.setStatus("current")


class _Gepoel2esw12IPv4DNSProxy_Type(Integer32):
    """Custom type gepoel2esw12IPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12IPv4DNSProxy_Type.__name__ = "Integer32"
_Gepoel2esw12IPv4DNSProxy_Object = MibScalar
gepoel2esw12IPv4DNSProxy = _Gepoel2esw12IPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 1, 7),
    _Gepoel2esw12IPv4DNSProxy_Type()
)
gepoel2esw12IPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4DNSProxy.setStatus("current")
_Gepoel2esw12IPv4Current_ObjectIdentity = ObjectIdentity
gepoel2esw12IPv4Current = _Gepoel2esw12IPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2)
)


class _Gepoel2esw12Ipv4CurrentDHCPClient_Type(Integer32):
    """Custom type gepoel2esw12Ipv4CurrentDHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12Ipv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Gepoel2esw12Ipv4CurrentDHCPClient_Object = MibScalar
gepoel2esw12Ipv4CurrentDHCPClient = _Gepoel2esw12Ipv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2, 1),
    _Gepoel2esw12Ipv4CurrentDHCPClient_Type()
)
gepoel2esw12Ipv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv4CurrentDHCPClient.setStatus("current")
_Gepoel2esw12IPv4CurrentAddress_Type = IpAddress
_Gepoel2esw12IPv4CurrentAddress_Object = MibScalar
gepoel2esw12IPv4CurrentAddress = _Gepoel2esw12IPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2, 2),
    _Gepoel2esw12IPv4CurrentAddress_Type()
)
gepoel2esw12IPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4CurrentAddress.setStatus("current")
_Gepoel2esw12IPv4CurrentMask_Type = IpAddress
_Gepoel2esw12IPv4CurrentMask_Object = MibScalar
gepoel2esw12IPv4CurrentMask = _Gepoel2esw12IPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2, 3),
    _Gepoel2esw12IPv4CurrentMask_Type()
)
gepoel2esw12IPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4CurrentMask.setStatus("current")
_Gepoel2esw12IPv4CurrentRouter_Type = IpAddress
_Gepoel2esw12IPv4CurrentRouter_Object = MibScalar
gepoel2esw12IPv4CurrentRouter = _Gepoel2esw12IPv4CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2, 4),
    _Gepoel2esw12IPv4CurrentRouter_Type()
)
gepoel2esw12IPv4CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4CurrentRouter.setStatus("current")


class _Gepoel2esw12IPv4CurrentVLANId_Type(Integer32):
    """Custom type gepoel2esw12IPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gepoel2esw12IPv4CurrentVLANId_Type.__name__ = "Integer32"
_Gepoel2esw12IPv4CurrentVLANId_Object = MibScalar
gepoel2esw12IPv4CurrentVLANId = _Gepoel2esw12IPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2, 5),
    _Gepoel2esw12IPv4CurrentVLANId_Type()
)
gepoel2esw12IPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4CurrentVLANId.setStatus("current")
_Gepoel2esw12IPv4CurrentDNSServer_Type = IpAddress
_Gepoel2esw12IPv4CurrentDNSServer_Object = MibScalar
gepoel2esw12IPv4CurrentDNSServer = _Gepoel2esw12IPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 1, 2, 6),
    _Gepoel2esw12IPv4CurrentDNSServer_Type()
)
gepoel2esw12IPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12IPv4CurrentDNSServer.setStatus("current")
_Gepoel2esw12IPv6_ObjectIdentity = ObjectIdentity
gepoel2esw12IPv6 = _Gepoel2esw12IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2)
)
_Gepoel2esw12IPv6Configured_ObjectIdentity = ObjectIdentity
gepoel2esw12IPv6Configured = _Gepoel2esw12IPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 1)
)


class _Gepoel2esw12Ipv6AutoConfiguration_Type(Integer32):
    """Custom type gepoel2esw12Ipv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12Ipv6AutoConfiguration_Type.__name__ = "Integer32"
_Gepoel2esw12Ipv6AutoConfiguration_Object = MibScalar
gepoel2esw12Ipv6AutoConfiguration = _Gepoel2esw12Ipv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 1, 1),
    _Gepoel2esw12Ipv6AutoConfiguration_Type()
)
gepoel2esw12Ipv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6AutoConfiguration.setStatus("current")


class _Gepoel2esw12Ipv6Address_Type(DisplayString):
    """Custom type gepoel2esw12Ipv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gepoel2esw12Ipv6Address_Type.__name__ = "DisplayString"
_Gepoel2esw12Ipv6Address_Object = MibScalar
gepoel2esw12Ipv6Address = _Gepoel2esw12Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 1, 2),
    _Gepoel2esw12Ipv6Address_Type()
)
gepoel2esw12Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6Address.setStatus("current")


class _Gepoel2esw12Ipv6Prefix_Type(Integer32):
    """Custom type gepoel2esw12Ipv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gepoel2esw12Ipv6Prefix_Type.__name__ = "Integer32"
_Gepoel2esw12Ipv6Prefix_Object = MibScalar
gepoel2esw12Ipv6Prefix = _Gepoel2esw12Ipv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 1, 3),
    _Gepoel2esw12Ipv6Prefix_Type()
)
gepoel2esw12Ipv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6Prefix.setStatus("current")


class _Gepoel2esw12Ipv6Router_Type(DisplayString):
    """Custom type gepoel2esw12Ipv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gepoel2esw12Ipv6Router_Type.__name__ = "DisplayString"
_Gepoel2esw12Ipv6Router_Object = MibScalar
gepoel2esw12Ipv6Router = _Gepoel2esw12Ipv6Router_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 1, 4),
    _Gepoel2esw12Ipv6Router_Type()
)
gepoel2esw12Ipv6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6Router.setStatus("current")
_Gepoel2esw12IPv6Current_ObjectIdentity = ObjectIdentity
gepoel2esw12IPv6Current = _Gepoel2esw12IPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 2)
)


class _Gepoel2esw12Ipv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type gepoel2esw12Ipv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12Ipv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Gepoel2esw12Ipv6CurrentAutoConfiguration_Object = MibScalar
gepoel2esw12Ipv6CurrentAutoConfiguration = _Gepoel2esw12Ipv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 2, 1),
    _Gepoel2esw12Ipv6CurrentAutoConfiguration_Type()
)
gepoel2esw12Ipv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6CurrentAutoConfiguration.setStatus("current")


class _Gepoel2esw12Ipv6CurrentAddress_Type(DisplayString):
    """Custom type gepoel2esw12Ipv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gepoel2esw12Ipv6CurrentAddress_Type.__name__ = "DisplayString"
_Gepoel2esw12Ipv6CurrentAddress_Object = MibScalar
gepoel2esw12Ipv6CurrentAddress = _Gepoel2esw12Ipv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 2, 2),
    _Gepoel2esw12Ipv6CurrentAddress_Type()
)
gepoel2esw12Ipv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6CurrentAddress.setStatus("current")


class _Gepoel2esw12Ipv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type gepoel2esw12Ipv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gepoel2esw12Ipv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Gepoel2esw12Ipv6CurrentLinkLocalAddress_Object = MibScalar
gepoel2esw12Ipv6CurrentLinkLocalAddress = _Gepoel2esw12Ipv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 2, 3),
    _Gepoel2esw12Ipv6CurrentLinkLocalAddress_Type()
)
gepoel2esw12Ipv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6CurrentLinkLocalAddress.setStatus("current")


class _Gepoel2esw12Ipv6CurrentPrefix_Type(Integer32):
    """Custom type gepoel2esw12Ipv6CurrentPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gepoel2esw12Ipv6CurrentPrefix_Type.__name__ = "Integer32"
_Gepoel2esw12Ipv6CurrentPrefix_Object = MibScalar
gepoel2esw12Ipv6CurrentPrefix = _Gepoel2esw12Ipv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 2, 4),
    _Gepoel2esw12Ipv6CurrentPrefix_Type()
)
gepoel2esw12Ipv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6CurrentPrefix.setStatus("current")


class _Gepoel2esw12Ipv6CurrentRouter_Type(DisplayString):
    """Custom type gepoel2esw12Ipv6CurrentRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gepoel2esw12Ipv6CurrentRouter_Type.__name__ = "DisplayString"
_Gepoel2esw12Ipv6CurrentRouter_Object = MibScalar
gepoel2esw12Ipv6CurrentRouter = _Gepoel2esw12Ipv6CurrentRouter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 4, 2, 2, 5),
    _Gepoel2esw12Ipv6CurrentRouter_Type()
)
gepoel2esw12Ipv6CurrentRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Ipv6CurrentRouter.setStatus("current")
_Gepoel2esw12Syslog_ObjectIdentity = ObjectIdentity
gepoel2esw12Syslog = _Gepoel2esw12Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5)
)
_Gepoel2esw12SyslogConf_ObjectIdentity = ObjectIdentity
gepoel2esw12SyslogConf = _Gepoel2esw12SyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 1)
)


class _Gepoel2esw12ServerMode_Type(Integer32):
    """Custom type gepoel2esw12ServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12ServerMode_Type.__name__ = "Integer32"
_Gepoel2esw12ServerMode_Object = MibScalar
gepoel2esw12ServerMode = _Gepoel2esw12ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 1, 1),
    _Gepoel2esw12ServerMode_Type()
)
gepoel2esw12ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12ServerMode.setStatus("current")
_Gepoel2esw12ServerAddress1_Type = IpAddress
_Gepoel2esw12ServerAddress1_Object = MibScalar
gepoel2esw12ServerAddress1 = _Gepoel2esw12ServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 1, 2),
    _Gepoel2esw12ServerAddress1_Type()
)
gepoel2esw12ServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12ServerAddress1.setStatus("current")


class _Gepoel2esw12SyslogLevel_Type(Integer32):
    """Custom type gepoel2esw12SyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12SyslogLevel_Type.__name__ = "Integer32"
_Gepoel2esw12SyslogLevel_Object = MibScalar
gepoel2esw12SyslogLevel = _Gepoel2esw12SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 1, 4),
    _Gepoel2esw12SyslogLevel_Type()
)
gepoel2esw12SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SyslogLevel.setStatus("current")
_Gepoel2esw12SyslogDetailedInfo_ObjectIdentity = ObjectIdentity
gepoel2esw12SyslogDetailedInfo = _Gepoel2esw12SyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2)
)


class _Gepoel2esw12SyslogDetailedInfoClear_Type(Integer32):
    """Custom type gepoel2esw12SyslogDetailedInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Gepoel2esw12SyslogDetailedInfoClear_Object = MibScalar
gepoel2esw12SyslogDetailedInfoClear = _Gepoel2esw12SyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 1),
    _Gepoel2esw12SyslogDetailedInfoClear_Type()
)
gepoel2esw12SyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoClear.setStatus("current")
_Gepoel2esw12SyslogDetailedInfoTable_Object = MibTable
gepoel2esw12SyslogDetailedInfoTable = _Gepoel2esw12SyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoTable.setStatus("current")
_Gepoel2esw12SyslogDetailedInfoEntry_Object = MibTableRow
gepoel2esw12SyslogDetailedInfoEntry = _Gepoel2esw12SyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 2, 1)
)
gepoel2esw12SyslogDetailedInfoEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12SyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoEntry.setStatus("current")


class _Gepoel2esw12SyslogDetailedInfoIndex_Type(Integer32):
    """Custom type gepoel2esw12SyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gepoel2esw12SyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Gepoel2esw12SyslogDetailedInfoIndex_Object = MibTableColumn
gepoel2esw12SyslogDetailedInfoIndex = _Gepoel2esw12SyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 2, 1, 1),
    _Gepoel2esw12SyslogDetailedInfoIndex_Type()
)
gepoel2esw12SyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoIndex.setStatus("current")
_Gepoel2esw12SyslogDetailedInfoLevel_Type = DisplayString
_Gepoel2esw12SyslogDetailedInfoLevel_Object = MibTableColumn
gepoel2esw12SyslogDetailedInfoLevel = _Gepoel2esw12SyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 2, 1, 2),
    _Gepoel2esw12SyslogDetailedInfoLevel_Type()
)
gepoel2esw12SyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoLevel.setStatus("current")


class _Gepoel2esw12SyslogDetailedInfoTime_Type(DisplayString):
    """Custom type gepoel2esw12SyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gepoel2esw12SyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Gepoel2esw12SyslogDetailedInfoTime_Object = MibTableColumn
gepoel2esw12SyslogDetailedInfoTime = _Gepoel2esw12SyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 2, 1, 3),
    _Gepoel2esw12SyslogDetailedInfoTime_Type()
)
gepoel2esw12SyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoTime.setStatus("current")
_Gepoel2esw12SyslogDetailedInfoMessage_Type = DisplayString
_Gepoel2esw12SyslogDetailedInfoMessage_Object = MibTableColumn
gepoel2esw12SyslogDetailedInfoMessage = _Gepoel2esw12SyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 5, 2, 2, 1, 4),
    _Gepoel2esw12SyslogDetailedInfoMessage_Type()
)
gepoel2esw12SyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SyslogDetailedInfoMessage.setStatus("current")
_Gepoel2esw12Snmp_ObjectIdentity = ObjectIdentity
gepoel2esw12Snmp = _Gepoel2esw12Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6)
)
_Gepoel2esw12SnmpConf_ObjectIdentity = ObjectIdentity
gepoel2esw12SnmpConf = _Gepoel2esw12SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1)
)
_Gepoel2esw12TrapHostConfTable_Object = MibTable
gepoel2esw12TrapHostConfTable = _Gepoel2esw12TrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfTable.setStatus("current")
_Gepoel2esw12TrapHostConfEntry_Object = MibTableRow
gepoel2esw12TrapHostConfEntry = _Gepoel2esw12TrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1)
)
gepoel2esw12TrapHostConfEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12TrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfEntry.setStatus("current")


class _Gepoel2esw12TrapHostConfIndex_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gepoel2esw12TrapHostConfIndex_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfIndex_Object = MibTableColumn
gepoel2esw12TrapHostConfIndex = _Gepoel2esw12TrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 1),
    _Gepoel2esw12TrapHostConfIndex_Type()
)
gepoel2esw12TrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfIndex.setStatus("current")


class _Gepoel2esw12TrapHostConfVersion_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3),
    )


_Gepoel2esw12TrapHostConfVersion_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfVersion_Object = MibTableColumn
gepoel2esw12TrapHostConfVersion = _Gepoel2esw12TrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 2),
    _Gepoel2esw12TrapHostConfVersion_Type()
)
gepoel2esw12TrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfVersion.setStatus("current")


class _Gepoel2esw12TrapHostConfIPType_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
    )


_Gepoel2esw12TrapHostConfIPType_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfIPType_Object = MibTableColumn
gepoel2esw12TrapHostConfIPType = _Gepoel2esw12TrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 3),
    _Gepoel2esw12TrapHostConfIPType_Type()
)
gepoel2esw12TrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfIPType.setStatus("current")
_Gepoel2esw12TrapHostConfIP_Type = DisplayString
_Gepoel2esw12TrapHostConfIP_Object = MibTableColumn
gepoel2esw12TrapHostConfIP = _Gepoel2esw12TrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 4),
    _Gepoel2esw12TrapHostConfIP_Type()
)
gepoel2esw12TrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfIP.setStatus("current")


class _Gepoel2esw12TrapHostConfPort_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gepoel2esw12TrapHostConfPort_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfPort_Object = MibTableColumn
gepoel2esw12TrapHostConfPort = _Gepoel2esw12TrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 5),
    _Gepoel2esw12TrapHostConfPort_Type()
)
gepoel2esw12TrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfPort.setStatus("current")


class _Gepoel2esw12TrapHostConfCommunity_Type(DisplayString):
    """Custom type gepoel2esw12TrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gepoel2esw12TrapHostConfCommunity_Type.__name__ = "DisplayString"
_Gepoel2esw12TrapHostConfCommunity_Object = MibTableColumn
gepoel2esw12TrapHostConfCommunity = _Gepoel2esw12TrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 6),
    _Gepoel2esw12TrapHostConfCommunity_Type()
)
gepoel2esw12TrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfCommunity.setStatus("current")


class _Gepoel2esw12TrapHostConfSeverityLevel_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfSeverityLevel_Object = MibTableColumn
gepoel2esw12TrapHostConfSeverityLevel = _Gepoel2esw12TrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 7),
    _Gepoel2esw12TrapHostConfSeverityLevel_Type()
)
gepoel2esw12TrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfSeverityLevel.setStatus("current")


class _Gepoel2esw12TrapHostConfSecurityLevel_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gepoel2esw12TrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfSecurityLevel_Object = MibTableColumn
gepoel2esw12TrapHostConfSecurityLevel = _Gepoel2esw12TrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 8),
    _Gepoel2esw12TrapHostConfSecurityLevel_Type()
)
gepoel2esw12TrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfSecurityLevel.setStatus("current")


class _Gepoel2esw12TrapHostConfAuthPtc_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfAuthPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12TrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfAuthPtc_Object = MibTableColumn
gepoel2esw12TrapHostConfAuthPtc = _Gepoel2esw12TrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 9),
    _Gepoel2esw12TrapHostConfAuthPtc_Type()
)
gepoel2esw12TrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfAuthPtc.setStatus("current")
_Gepoel2esw12TrapHostConfAuthPassword_Type = DisplayString
_Gepoel2esw12TrapHostConfAuthPassword_Object = MibTableColumn
gepoel2esw12TrapHostConfAuthPassword = _Gepoel2esw12TrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 10),
    _Gepoel2esw12TrapHostConfAuthPassword_Type()
)
gepoel2esw12TrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfAuthPassword.setStatus("current")


class _Gepoel2esw12TrapHostConfPrivPtc_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12TrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfPrivPtc_Object = MibTableColumn
gepoel2esw12TrapHostConfPrivPtc = _Gepoel2esw12TrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 11),
    _Gepoel2esw12TrapHostConfPrivPtc_Type()
)
gepoel2esw12TrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfPrivPtc.setStatus("current")
_Gepoel2esw12TrapHostConfPrivPassword_Type = DisplayString
_Gepoel2esw12TrapHostConfPrivPassword_Object = MibTableColumn
gepoel2esw12TrapHostConfPrivPassword = _Gepoel2esw12TrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 12),
    _Gepoel2esw12TrapHostConfPrivPassword_Type()
)
gepoel2esw12TrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfPrivPassword.setStatus("current")


class _Gepoel2esw12TrapHostConfCurrentMode_Type(Integer32):
    """Custom type gepoel2esw12TrapHostConfCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gepoel2esw12TrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Gepoel2esw12TrapHostConfCurrentMode_Object = MibTableColumn
gepoel2esw12TrapHostConfCurrentMode = _Gepoel2esw12TrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 1, 6, 1, 4, 1, 13),
    _Gepoel2esw12TrapHostConfCurrentMode_Type()
)
gepoel2esw12TrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapHostConfCurrentMode.setStatus("current")
_Gepoel2esw12OltManagement_ObjectIdentity = ObjectIdentity
gepoel2esw12OltManagement = _Gepoel2esw12OltManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2)
)
_Gepoel2esw12OltPortTable_Object = MibTable
gepoel2esw12OltPortTable = _Gepoel2esw12OltPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltPortTable.setStatus("current")
_Gepoel2esw12OltPortEntry_Object = MibTableRow
gepoel2esw12OltPortEntry = _Gepoel2esw12OltPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1)
)
gepoel2esw12OltPortEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltPortEntry.setStatus("current")


class _Gepoel2esw12OltPortStatusIndex_Type(Integer32):
    """Custom type gepoel2esw12OltPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gepoel2esw12OltPortStatusIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltPortStatusIndex_Object = MibTableColumn
gepoel2esw12OltPortStatusIndex = _Gepoel2esw12OltPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 1),
    _Gepoel2esw12OltPortStatusIndex_Type()
)
gepoel2esw12OltPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortStatusIndex.setStatus("current")
_Gepoel2esw12OltPortLinkStatus_Type = DisplayString
_Gepoel2esw12OltPortLinkStatus_Object = MibTableColumn
gepoel2esw12OltPortLinkStatus = _Gepoel2esw12OltPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 2),
    _Gepoel2esw12OltPortLinkStatus_Type()
)
gepoel2esw12OltPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortLinkStatus.setStatus("current")


class _Gepoel2esw12OltPortState_Type(Integer32):
    """Custom type gepoel2esw12OltPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltPortState_Type.__name__ = "Integer32"
_Gepoel2esw12OltPortState_Object = MibTableColumn
gepoel2esw12OltPortState = _Gepoel2esw12OltPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 3),
    _Gepoel2esw12OltPortState_Type()
)
gepoel2esw12OltPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortState.setStatus("current")


class _Gepoel2esw12OltPortSpdDpxConf_Type(Integer32):
    """Custom type gepoel2esw12OltPortSpdDpxConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(101, 101),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(1001, 1001),
    )


_Gepoel2esw12OltPortSpdDpxConf_Type.__name__ = "Integer32"
_Gepoel2esw12OltPortSpdDpxConf_Object = MibTableColumn
gepoel2esw12OltPortSpdDpxConf = _Gepoel2esw12OltPortSpdDpxConf_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 4),
    _Gepoel2esw12OltPortSpdDpxConf_Type()
)
gepoel2esw12OltPortSpdDpxConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortSpdDpxConf.setStatus("current")
_Gepoel2esw12OltPortSpdDpx_Type = DisplayString
_Gepoel2esw12OltPortSpdDpx_Object = MibTableColumn
gepoel2esw12OltPortSpdDpx = _Gepoel2esw12OltPortSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 5),
    _Gepoel2esw12OltPortSpdDpx_Type()
)
gepoel2esw12OltPortSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortSpdDpx.setStatus("current")


class _Gepoel2esw12OltPortFlwCtlConf_Type(Integer32):
    """Custom type gepoel2esw12OltPortFlwCtlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltPortFlwCtlConf_Type.__name__ = "Integer32"
_Gepoel2esw12OltPortFlwCtlConf_Object = MibTableColumn
gepoel2esw12OltPortFlwCtlConf = _Gepoel2esw12OltPortFlwCtlConf_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 6),
    _Gepoel2esw12OltPortFlwCtlConf_Type()
)
gepoel2esw12OltPortFlwCtlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortFlwCtlConf.setStatus("current")
_Gepoel2esw12OltPortFlwCtl_Type = DisplayString
_Gepoel2esw12OltPortFlwCtl_Object = MibTableColumn
gepoel2esw12OltPortFlwCtl = _Gepoel2esw12OltPortFlwCtl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 1, 1, 7),
    _Gepoel2esw12OltPortFlwCtl_Type()
)
gepoel2esw12OltPortFlwCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPortFlwCtl.setStatus("current")
_Gepoel2esw12OltStatisticsTable_Object = MibTable
gepoel2esw12OltStatisticsTable = _Gepoel2esw12OltStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsTable.setStatus("current")
_Gepoel2esw12OltStatisticsEntry_Object = MibTableRow
gepoel2esw12OltStatisticsEntry = _Gepoel2esw12OltStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1)
)
gepoel2esw12OltStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltStatisticsPortType"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltStatisticsQueryGroup"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsEntry.setStatus("current")


class _Gepoel2esw12OltStatisticsPortType_Type(Integer32):
    """Custom type gepoel2esw12OltStatisticsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gepoel2esw12OltStatisticsPortType_Type.__name__ = "Integer32"
_Gepoel2esw12OltStatisticsPortType_Object = MibTableColumn
gepoel2esw12OltStatisticsPortType = _Gepoel2esw12OltStatisticsPortType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 1),
    _Gepoel2esw12OltStatisticsPortType_Type()
)
gepoel2esw12OltStatisticsPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsPortType.setStatus("current")


class _Gepoel2esw12OltStatisticsQueryGroup_Type(Integer32):
    """Custom type gepoel2esw12OltStatisticsQueryGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gepoel2esw12OltStatisticsQueryGroup_Type.__name__ = "Integer32"
_Gepoel2esw12OltStatisticsQueryGroup_Object = MibTableColumn
gepoel2esw12OltStatisticsQueryGroup = _Gepoel2esw12OltStatisticsQueryGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 2),
    _Gepoel2esw12OltStatisticsQueryGroup_Type()
)
gepoel2esw12OltStatisticsQueryGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsQueryGroup.setStatus("current")
_Gepoel2esw12OltStatisticsOctet_Type = Counter64
_Gepoel2esw12OltStatisticsOctet_Object = MibTableColumn
gepoel2esw12OltStatisticsOctet = _Gepoel2esw12OltStatisticsOctet_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 3),
    _Gepoel2esw12OltStatisticsOctet_Type()
)
gepoel2esw12OltStatisticsOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsOctet.setStatus("current")
_Gepoel2esw12OltStatisticsCRC8Errors_Type = Counter64
_Gepoel2esw12OltStatisticsCRC8Errors_Object = MibTableColumn
gepoel2esw12OltStatisticsCRC8Errors = _Gepoel2esw12OltStatisticsCRC8Errors_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 4),
    _Gepoel2esw12OltStatisticsCRC8Errors_Type()
)
gepoel2esw12OltStatisticsCRC8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsCRC8Errors.setStatus("current")
_Gepoel2esw12OltStatisticsErrorFrameTransfer_Type = Counter64
_Gepoel2esw12OltStatisticsErrorFrameTransfer_Object = MibTableColumn
gepoel2esw12OltStatisticsErrorFrameTransfer = _Gepoel2esw12OltStatisticsErrorFrameTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 5),
    _Gepoel2esw12OltStatisticsErrorFrameTransfer_Type()
)
gepoel2esw12OltStatisticsErrorFrameTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsErrorFrameTransfer.setStatus("current")
_Gepoel2esw12OltStatisticsLineCodeError_Type = Counter64
_Gepoel2esw12OltStatisticsLineCodeError_Object = MibTableColumn
gepoel2esw12OltStatisticsLineCodeError = _Gepoel2esw12OltStatisticsLineCodeError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 6),
    _Gepoel2esw12OltStatisticsLineCodeError_Type()
)
gepoel2esw12OltStatisticsLineCodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLineCodeError.setStatus("current")
_Gepoel2esw12OltStatisticsCorrectableFECBlock_Type = Counter64
_Gepoel2esw12OltStatisticsCorrectableFECBlock_Object = MibTableColumn
gepoel2esw12OltStatisticsCorrectableFECBlock = _Gepoel2esw12OltStatisticsCorrectableFECBlock_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 7),
    _Gepoel2esw12OltStatisticsCorrectableFECBlock_Type()
)
gepoel2esw12OltStatisticsCorrectableFECBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsCorrectableFECBlock.setStatus("current")
_Gepoel2esw12OltStatisticsUncorrectableFECBlock_Type = Counter64
_Gepoel2esw12OltStatisticsUncorrectableFECBlock_Object = MibTableColumn
gepoel2esw12OltStatisticsUncorrectableFECBlock = _Gepoel2esw12OltStatisticsUncorrectableFECBlock_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 8),
    _Gepoel2esw12OltStatisticsUncorrectableFECBlock_Type()
)
gepoel2esw12OltStatisticsUncorrectableFECBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsUncorrectableFECBlock.setStatus("current")
_Gepoel2esw12OltStatisticsUndersizeFrame_Type = Counter64
_Gepoel2esw12OltStatisticsUndersizeFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsUndersizeFrame = _Gepoel2esw12OltStatisticsUndersizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 9),
    _Gepoel2esw12OltStatisticsUndersizeFrame_Type()
)
gepoel2esw12OltStatisticsUndersizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsUndersizeFrame.setStatus("current")
_Gepoel2esw12OltStatisticsCorrectableFECBytes_Type = Counter64
_Gepoel2esw12OltStatisticsCorrectableFECBytes_Object = MibTableColumn
gepoel2esw12OltStatisticsCorrectableFECBytes = _Gepoel2esw12OltStatisticsCorrectableFECBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 10),
    _Gepoel2esw12OltStatisticsCorrectableFECBytes_Type()
)
gepoel2esw12OltStatisticsCorrectableFECBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsCorrectableFECBytes.setStatus("current")
_Gepoel2esw12OltStatisticsPostFECGoodFrame_Type = Counter64
_Gepoel2esw12OltStatisticsPostFECGoodFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsPostFECGoodFrame = _Gepoel2esw12OltStatisticsPostFECGoodFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 11),
    _Gepoel2esw12OltStatisticsPostFECGoodFrame_Type()
)
gepoel2esw12OltStatisticsPostFECGoodFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsPostFECGoodFrame.setStatus("current")
_Gepoel2esw12OltStatisticsPostFECBadFrame_Type = Counter64
_Gepoel2esw12OltStatisticsPostFECBadFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsPostFECBadFrame = _Gepoel2esw12OltStatisticsPostFECBadFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 12),
    _Gepoel2esw12OltStatisticsPostFECBadFrame_Type()
)
gepoel2esw12OltStatisticsPostFECBadFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsPostFECBadFrame.setStatus("current")
_Gepoel2esw12OltStatisticsPreFECGoodFrame_Type = Counter64
_Gepoel2esw12OltStatisticsPreFECGoodFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsPreFECGoodFrame = _Gepoel2esw12OltStatisticsPreFECGoodFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 13),
    _Gepoel2esw12OltStatisticsPreFECGoodFrame_Type()
)
gepoel2esw12OltStatisticsPreFECGoodFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsPreFECGoodFrame.setStatus("current")
_Gepoel2esw12OltStatisticsPreFECBadFrame_Type = Counter64
_Gepoel2esw12OltStatisticsPreFECBadFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsPreFECBadFrame = _Gepoel2esw12OltStatisticsPreFECBadFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 14),
    _Gepoel2esw12OltStatisticsPreFECBadFrame_Type()
)
gepoel2esw12OltStatisticsPreFECBadFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsPreFECBadFrame.setStatus("current")
_Gepoel2esw12OltStatisticsLaserIdlePower_Type = Counter64
_Gepoel2esw12OltStatisticsLaserIdlePower_Object = MibTableColumn
gepoel2esw12OltStatisticsLaserIdlePower = _Gepoel2esw12OltStatisticsLaserIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 15),
    _Gepoel2esw12OltStatisticsLaserIdlePower_Type()
)
gepoel2esw12OltStatisticsLaserIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLaserIdlePower.setStatus("current")
_Gepoel2esw12OltStatisticsFECPacketTooLongEvent_Type = Counter64
_Gepoel2esw12OltStatisticsFECPacketTooLongEvent_Object = MibTableColumn
gepoel2esw12OltStatisticsFECPacketTooLongEvent = _Gepoel2esw12OltStatisticsFECPacketTooLongEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 16),
    _Gepoel2esw12OltStatisticsFECPacketTooLongEvent_Type()
)
gepoel2esw12OltStatisticsFECPacketTooLongEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsFECPacketTooLongEvent.setStatus("current")
_Gepoel2esw12OltStatisticsFECBlock_Type = Counter64
_Gepoel2esw12OltStatisticsFECBlock_Object = MibTableColumn
gepoel2esw12OltStatisticsFECBlock = _Gepoel2esw12OltStatisticsFECBlock_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 17),
    _Gepoel2esw12OltStatisticsFECBlock_Type()
)
gepoel2esw12OltStatisticsFECBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsFECBlock.setStatus("current")
_Gepoel2esw12OltStatisticsLaserPower_Type = Counter64
_Gepoel2esw12OltStatisticsLaserPower_Object = MibTableColumn
gepoel2esw12OltStatisticsLaserPower = _Gepoel2esw12OltStatisticsLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 18),
    _Gepoel2esw12OltStatisticsLaserPower_Type()
)
gepoel2esw12OltStatisticsLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLaserPower.setStatus("current")
_Gepoel2esw12OltStatisticsLaserVCC_Type = Counter64
_Gepoel2esw12OltStatisticsLaserVCC_Object = MibTableColumn
gepoel2esw12OltStatisticsLaserVCC = _Gepoel2esw12OltStatisticsLaserVCC_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 19),
    _Gepoel2esw12OltStatisticsLaserVCC_Type()
)
gepoel2esw12OltStatisticsLaserVCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLaserVCC.setStatus("current")
_Gepoel2esw12OltStatisticsLaserBias_Type = Counter64
_Gepoel2esw12OltStatisticsLaserBias_Object = MibTableColumn
gepoel2esw12OltStatisticsLaserBias = _Gepoel2esw12OltStatisticsLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 20),
    _Gepoel2esw12OltStatisticsLaserBias_Type()
)
gepoel2esw12OltStatisticsLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLaserBias.setStatus("current")
_Gepoel2esw12OltStatisticsLaserTemp_Type = Counter64
_Gepoel2esw12OltStatisticsLaserTemp_Object = MibTableColumn
gepoel2esw12OltStatisticsLaserTemp = _Gepoel2esw12OltStatisticsLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 21),
    _Gepoel2esw12OltStatisticsLaserTemp_Type()
)
gepoel2esw12OltStatisticsLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLaserTemp.setStatus("current")
_Gepoel2esw12OltStatisticsUnicastFrame_Type = Counter64
_Gepoel2esw12OltStatisticsUnicastFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsUnicastFrame = _Gepoel2esw12OltStatisticsUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 22),
    _Gepoel2esw12OltStatisticsUnicastFrame_Type()
)
gepoel2esw12OltStatisticsUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsUnicastFrame.setStatus("current")
_Gepoel2esw12OltStatisticsMulticastFrame_Type = Counter64
_Gepoel2esw12OltStatisticsMulticastFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsMulticastFrame = _Gepoel2esw12OltStatisticsMulticastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 23),
    _Gepoel2esw12OltStatisticsMulticastFrame_Type()
)
gepoel2esw12OltStatisticsMulticastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsMulticastFrame.setStatus("current")
_Gepoel2esw12OltStatisticsBroadcastFrame_Type = Counter64
_Gepoel2esw12OltStatisticsBroadcastFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsBroadcastFrame = _Gepoel2esw12OltStatisticsBroadcastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 24),
    _Gepoel2esw12OltStatisticsBroadcastFrame_Type()
)
gepoel2esw12OltStatisticsBroadcastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsBroadcastFrame.setStatus("current")
_Gepoel2esw12OltStatisticsOversizetFrame_Type = Counter64
_Gepoel2esw12OltStatisticsOversizetFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsOversizetFrame = _Gepoel2esw12OltStatisticsOversizetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 25),
    _Gepoel2esw12OltStatisticsOversizetFrame_Type()
)
gepoel2esw12OltStatisticsOversizetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsOversizetFrame.setStatus("current")
_Gepoel2esw12OltStatisticsCRC32Frame_Type = Counter64
_Gepoel2esw12OltStatisticsCRC32Frame_Object = MibTableColumn
gepoel2esw12OltStatisticsCRC32Frame = _Gepoel2esw12OltStatisticsCRC32Frame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 26),
    _Gepoel2esw12OltStatisticsCRC32Frame_Type()
)
gepoel2esw12OltStatisticsCRC32Frame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsCRC32Frame.setStatus("current")
_Gepoel2esw12OltStatisticsMPCPFrame_Type = Counter64
_Gepoel2esw12OltStatisticsMPCPFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsMPCPFrame = _Gepoel2esw12OltStatisticsMPCPFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 27),
    _Gepoel2esw12OltStatisticsMPCPFrame_Type()
)
gepoel2esw12OltStatisticsMPCPFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsMPCPFrame.setStatus("current")
_Gepoel2esw12OltStatisticsMPCPBytes_Type = Counter64
_Gepoel2esw12OltStatisticsMPCPBytes_Object = MibTableColumn
gepoel2esw12OltStatisticsMPCPBytes = _Gepoel2esw12OltStatisticsMPCPBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 28),
    _Gepoel2esw12OltStatisticsMPCPBytes_Type()
)
gepoel2esw12OltStatisticsMPCPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsMPCPBytes.setStatus("current")
_Gepoel2esw12OltStatisticsMPCPDiscoveryTimeout_Type = Counter64
_Gepoel2esw12OltStatisticsMPCPDiscoveryTimeout_Object = MibTableColumn
gepoel2esw12OltStatisticsMPCPDiscoveryTimeout = _Gepoel2esw12OltStatisticsMPCPDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 29),
    _Gepoel2esw12OltStatisticsMPCPDiscoveryTimeout_Type()
)
gepoel2esw12OltStatisticsMPCPDiscoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsMPCPDiscoveryTimeout.setStatus("current")
_Gepoel2esw12OltStatisticsMPCPDiscoveryWindow_Type = Counter64
_Gepoel2esw12OltStatisticsMPCPDiscoveryWindow_Object = MibTableColumn
gepoel2esw12OltStatisticsMPCPDiscoveryWindow = _Gepoel2esw12OltStatisticsMPCPDiscoveryWindow_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 30),
    _Gepoel2esw12OltStatisticsMPCPDiscoveryWindow_Type()
)
gepoel2esw12OltStatisticsMPCPDiscoveryWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsMPCPDiscoveryWindow.setStatus("current")
_Gepoel2esw12OltStatisticsReportFrame_Type = Counter64
_Gepoel2esw12OltStatisticsReportFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsReportFrame = _Gepoel2esw12OltStatisticsReportFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 31),
    _Gepoel2esw12OltStatisticsReportFrame_Type()
)
gepoel2esw12OltStatisticsReportFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsReportFrame.setStatus("current")
_Gepoel2esw12OltStatisticsReportFrameAbort_Type = Counter64
_Gepoel2esw12OltStatisticsReportFrameAbort_Object = MibTableColumn
gepoel2esw12OltStatisticsReportFrameAbort = _Gepoel2esw12OltStatisticsReportFrameAbort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 32),
    _Gepoel2esw12OltStatisticsReportFrameAbort_Type()
)
gepoel2esw12OltStatisticsReportFrameAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsReportFrameAbort.setStatus("current")
_Gepoel2esw12OltStatisticsOAMFrames_Type = Counter64
_Gepoel2esw12OltStatisticsOAMFrames_Object = MibTableColumn
gepoel2esw12OltStatisticsOAMFrames = _Gepoel2esw12OltStatisticsOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 33),
    _Gepoel2esw12OltStatisticsOAMFrames_Type()
)
gepoel2esw12OltStatisticsOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsOAMFrames.setStatus("current")
_Gepoel2esw12OltStatisticsOAMBytes_Type = Counter64
_Gepoel2esw12OltStatisticsOAMBytes_Object = MibTableColumn
gepoel2esw12OltStatisticsOAMBytes = _Gepoel2esw12OltStatisticsOAMBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 34),
    _Gepoel2esw12OltStatisticsOAMBytes_Type()
)
gepoel2esw12OltStatisticsOAMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsOAMBytes.setStatus("current")
_Gepoel2esw12OltStatisticsLlidMisMatch_Type = Counter64
_Gepoel2esw12OltStatisticsLlidMisMatch_Object = MibTableColumn
gepoel2esw12OltStatisticsLlidMisMatch = _Gepoel2esw12OltStatisticsLlidMisMatch_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 35),
    _Gepoel2esw12OltStatisticsLlidMisMatch_Type()
)
gepoel2esw12OltStatisticsLlidMisMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsLlidMisMatch.setStatus("current")
_Gepoel2esw12OltStatisticsUngrantedFrames_Type = Counter64
_Gepoel2esw12OltStatisticsUngrantedFrames_Object = MibTableColumn
gepoel2esw12OltStatisticsUngrantedFrames = _Gepoel2esw12OltStatisticsUngrantedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 36),
    _Gepoel2esw12OltStatisticsUngrantedFrames_Type()
)
gepoel2esw12OltStatisticsUngrantedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsUngrantedFrames.setStatus("current")
_Gepoel2esw12OltStatisticsRegisterRequests_Type = Counter64
_Gepoel2esw12OltStatisticsRegisterRequests_Object = MibTableColumn
gepoel2esw12OltStatisticsRegisterRequests = _Gepoel2esw12OltStatisticsRegisterRequests_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 37),
    _Gepoel2esw12OltStatisticsRegisterRequests_Type()
)
gepoel2esw12OltStatisticsRegisterRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsRegisterRequests.setStatus("current")
_Gepoel2esw12OltStatisticsRegisterAcks_Type = Counter64
_Gepoel2esw12OltStatisticsRegisterAcks_Object = MibTableColumn
gepoel2esw12OltStatisticsRegisterAcks = _Gepoel2esw12OltStatisticsRegisterAcks_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 38),
    _Gepoel2esw12OltStatisticsRegisterAcks_Type()
)
gepoel2esw12OltStatisticsRegisterAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsRegisterAcks.setStatus("current")
_Gepoel2esw12OltStatisticsGateFrame_Type = Counter64
_Gepoel2esw12OltStatisticsGateFrame_Object = MibTableColumn
gepoel2esw12OltStatisticsGateFrame = _Gepoel2esw12OltStatisticsGateFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 39),
    _Gepoel2esw12OltStatisticsGateFrame_Type()
)
gepoel2esw12OltStatisticsGateFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsGateFrame.setStatus("current")
_Gepoel2esw12OltStatisticsReport_Type = Counter64
_Gepoel2esw12OltStatisticsReport_Object = MibTableColumn
gepoel2esw12OltStatisticsReport = _Gepoel2esw12OltStatisticsReport_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 40),
    _Gepoel2esw12OltStatisticsReport_Type()
)
gepoel2esw12OltStatisticsReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsReport.setStatus("current")


class _Gepoel2esw12OltStatisticsClear_Type(Integer32):
    """Custom type gepoel2esw12OltStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltStatisticsClear_Type.__name__ = "Integer32"
_Gepoel2esw12OltStatisticsClear_Object = MibTableColumn
gepoel2esw12OltStatisticsClear = _Gepoel2esw12OltStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 2, 1, 41),
    _Gepoel2esw12OltStatisticsClear_Type()
)
gepoel2esw12OltStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltStatisticsClear.setStatus("current")
_Gepoel2esw12OltInformation_ObjectIdentity = ObjectIdentity
gepoel2esw12OltInformation = _Gepoel2esw12OltInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 3)
)
_Gepoel2esw12OltChipID_Type = DisplayString
_Gepoel2esw12OltChipID_Object = MibScalar
gepoel2esw12OltChipID = _Gepoel2esw12OltChipID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 3, 1),
    _Gepoel2esw12OltChipID_Type()
)
gepoel2esw12OltChipID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltChipID.setStatus("current")
_Gepoel2esw12OltFirmwareVersion_Type = DisplayString
_Gepoel2esw12OltFirmwareVersion_Object = MibScalar
gepoel2esw12OltFirmwareVersion = _Gepoel2esw12OltFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 3, 2),
    _Gepoel2esw12OltFirmwareVersion_Type()
)
gepoel2esw12OltFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltFirmwareVersion.setStatus("current")
_Gepoel2esw12OltPersonalityVersion_Type = DisplayString
_Gepoel2esw12OltPersonalityVersion_Object = MibScalar
gepoel2esw12OltPersonalityVersion = _Gepoel2esw12OltPersonalityVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 3, 3),
    _Gepoel2esw12OltPersonalityVersion_Type()
)
gepoel2esw12OltPersonalityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPersonalityVersion.setStatus("current")
_Gepoel2esw12OltOltApp0Version_Type = DisplayString
_Gepoel2esw12OltOltApp0Version_Object = MibScalar
gepoel2esw12OltOltApp0Version = _Gepoel2esw12OltOltApp0Version_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 3, 4),
    _Gepoel2esw12OltOltApp0Version_Type()
)
gepoel2esw12OltOltApp0Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltOltApp0Version.setStatus("current")
_Gepoel2esw12OltOltApp1Version_Type = DisplayString
_Gepoel2esw12OltOltApp1Version_Object = MibScalar
gepoel2esw12OltOltApp1Version = _Gepoel2esw12OltOltApp1Version_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 3, 5),
    _Gepoel2esw12OltOltApp1Version_Type()
)
gepoel2esw12OltOltApp1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltOltApp1Version.setStatus("current")
_Gepoel2esw12OltGreenPonConf_ObjectIdentity = ObjectIdentity
gepoel2esw12OltGreenPonConf = _Gepoel2esw12OltGreenPonConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4)
)
_Gepoel2esw12OltGreenPonTable_Object = MibTable
gepoel2esw12OltGreenPonTable = _Gepoel2esw12OltGreenPonTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonTable.setStatus("current")
_Gepoel2esw12OltGreenPonEntry_Object = MibTableRow
gepoel2esw12OltGreenPonEntry = _Gepoel2esw12OltGreenPonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1)
)
gepoel2esw12OltGreenPonEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltGreenPonIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonEntry.setStatus("current")


class _Gepoel2esw12OltGreenPonIndex_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OltGreenPonIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonIndex_Object = MibTableColumn
gepoel2esw12OltGreenPonIndex = _Gepoel2esw12OltGreenPonIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 1),
    _Gepoel2esw12OltGreenPonIndex_Type()
)
gepoel2esw12OltGreenPonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonIndex.setStatus("current")


class _Gepoel2esw12OltGreenPonstate_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltGreenPonstate_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonstate_Object = MibTableColumn
gepoel2esw12OltGreenPonstate = _Gepoel2esw12OltGreenPonstate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 2),
    _Gepoel2esw12OltGreenPonstate_Type()
)
gepoel2esw12OltGreenPonstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonstate.setStatus("current")


class _Gepoel2esw12OltGreenPonSleepAfterNoTraffic_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonSleepAfterNoTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonSleepAfterNoTraffic_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonSleepAfterNoTraffic_Object = MibTableColumn
gepoel2esw12OltGreenPonSleepAfterNoTraffic = _Gepoel2esw12OltGreenPonSleepAfterNoTraffic_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 3),
    _Gepoel2esw12OltGreenPonSleepAfterNoTraffic_Type()
)
gepoel2esw12OltGreenPonSleepAfterNoTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonSleepAfterNoTraffic.setStatus("current")


class _Gepoel2esw12OltGreenPonOffTime_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonOffTime_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonOffTime_Object = MibTableColumn
gepoel2esw12OltGreenPonOffTime = _Gepoel2esw12OltGreenPonOffTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 4),
    _Gepoel2esw12OltGreenPonOffTime_Type()
)
gepoel2esw12OltGreenPonOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonOffTime.setStatus("current")


class _Gepoel2esw12OltGreenPonMinOnTime_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonMinOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonMinOnTime_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonMinOnTime_Object = MibTableColumn
gepoel2esw12OltGreenPonMinOnTime = _Gepoel2esw12OltGreenPonMinOnTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 5),
    _Gepoel2esw12OltGreenPonMinOnTime_Type()
)
gepoel2esw12OltGreenPonMinOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonMinOnTime.setStatus("current")


class _Gepoel2esw12OltGreenPonMinOnuOffTime_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonMinOnuOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonMinOnuOffTime_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonMinOnuOffTime_Object = MibTableColumn
gepoel2esw12OltGreenPonMinOnuOffTime = _Gepoel2esw12OltGreenPonMinOnuOffTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 6),
    _Gepoel2esw12OltGreenPonMinOnuOffTime_Type()
)
gepoel2esw12OltGreenPonMinOnuOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonMinOnuOffTime.setStatus("current")


class _Gepoel2esw12OltGreenPonSleepCheckTime_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonSleepCheckTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonSleepCheckTime_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonSleepCheckTime_Object = MibTableColumn
gepoel2esw12OltGreenPonSleepCheckTime = _Gepoel2esw12OltGreenPonSleepCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 7),
    _Gepoel2esw12OltGreenPonSleepCheckTime_Type()
)
gepoel2esw12OltGreenPonSleepCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonSleepCheckTime.setStatus("current")


class _Gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep_Object = MibTableColumn
gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep = _Gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 8),
    _Gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep_Type()
)
gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep.setStatus("current")


class _Gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup_Object = MibTableColumn
gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup = _Gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 9),
    _Gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup_Type()
)
gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup.setStatus("current")


class _Gepoel2esw12OltGreenPonProvisionOnu_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonProvisionOnu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltGreenPonProvisionOnu_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonProvisionOnu_Object = MibTableColumn
gepoel2esw12OltGreenPonProvisionOnu = _Gepoel2esw12OltGreenPonProvisionOnu_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 10),
    _Gepoel2esw12OltGreenPonProvisionOnu_Type()
)
gepoel2esw12OltGreenPonProvisionOnu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonProvisionOnu.setStatus("current")


class _Gepoel2esw12OltGreenPonUnprovisionOnu_Type(Integer32):
    """Custom type gepoel2esw12OltGreenPonUnprovisionOnu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltGreenPonUnprovisionOnu_Type.__name__ = "Integer32"
_Gepoel2esw12OltGreenPonUnprovisionOnu_Object = MibTableColumn
gepoel2esw12OltGreenPonUnprovisionOnu = _Gepoel2esw12OltGreenPonUnprovisionOnu_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 1, 1, 11),
    _Gepoel2esw12OltGreenPonUnprovisionOnu_Type()
)
gepoel2esw12OltGreenPonUnprovisionOnu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGreenPonUnprovisionOnu.setStatus("current")
_Gepoel2esw12OltPowerSavingReportTable_Object = MibTable
gepoel2esw12OltPowerSavingReportTable = _Gepoel2esw12OltPowerSavingReportTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportTable.setStatus("current")
_Gepoel2esw12OltPowerSavingReportEntry_Object = MibTableRow
gepoel2esw12OltPowerSavingReportEntry = _Gepoel2esw12OltPowerSavingReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1)
)
gepoel2esw12OltPowerSavingReportEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltPowerSavingReportIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportEntry.setStatus("current")
_Gepoel2esw12OltPowerSavingReportIndex_Type = Integer32
_Gepoel2esw12OltPowerSavingReportIndex_Object = MibTableColumn
gepoel2esw12OltPowerSavingReportIndex = _Gepoel2esw12OltPowerSavingReportIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1, 1),
    _Gepoel2esw12OltPowerSavingReportIndex_Type()
)
gepoel2esw12OltPowerSavingReportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportIndex.setStatus("current")
_Gepoel2esw12OltPowerSavingReportOnuMac_Type = DisplayString
_Gepoel2esw12OltPowerSavingReportOnuMac_Object = MibTableColumn
gepoel2esw12OltPowerSavingReportOnuMac = _Gepoel2esw12OltPowerSavingReportOnuMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1, 2),
    _Gepoel2esw12OltPowerSavingReportOnuMac_Type()
)
gepoel2esw12OltPowerSavingReportOnuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportOnuMac.setStatus("current")


class _Gepoel2esw12OltPowerSavingReportCandidate_Type(Integer32):
    """Custom type gepoel2esw12OltPowerSavingReportCandidate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltPowerSavingReportCandidate_Type.__name__ = "Integer32"
_Gepoel2esw12OltPowerSavingReportCandidate_Object = MibTableColumn
gepoel2esw12OltPowerSavingReportCandidate = _Gepoel2esw12OltPowerSavingReportCandidate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1, 3),
    _Gepoel2esw12OltPowerSavingReportCandidate_Type()
)
gepoel2esw12OltPowerSavingReportCandidate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportCandidate.setStatus("current")


class _Gepoel2esw12OltPowerSavingReportAsleep_Type(Integer32):
    """Custom type gepoel2esw12OltPowerSavingReportAsleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltPowerSavingReportAsleep_Type.__name__ = "Integer32"
_Gepoel2esw12OltPowerSavingReportAsleep_Object = MibScalar
gepoel2esw12OltPowerSavingReportAsleep = _Gepoel2esw12OltPowerSavingReportAsleep_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1, 4),
    _Gepoel2esw12OltPowerSavingReportAsleep_Type()
)
gepoel2esw12OltPowerSavingReportAsleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportAsleep.setStatus("current")
_Gepoel2esw12OltPowerSavingReportTimeAsleep_Type = Counter32
_Gepoel2esw12OltPowerSavingReportTimeAsleep_Object = MibTableColumn
gepoel2esw12OltPowerSavingReportTimeAsleep = _Gepoel2esw12OltPowerSavingReportTimeAsleep_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1, 5),
    _Gepoel2esw12OltPowerSavingReportTimeAsleep_Type()
)
gepoel2esw12OltPowerSavingReportTimeAsleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportTimeAsleep.setStatus("current")
_Gepoel2esw12OltPowerSavingReportTimeActive_Type = Counter32
_Gepoel2esw12OltPowerSavingReportTimeActive_Object = MibTableColumn
gepoel2esw12OltPowerSavingReportTimeActive = _Gepoel2esw12OltPowerSavingReportTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 4, 2, 1, 6),
    _Gepoel2esw12OltPowerSavingReportTimeActive_Type()
)
gepoel2esw12OltPowerSavingReportTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPowerSavingReportTimeActive.setStatus("current")
_Gepoel2esw12OltBridgeConfig_ObjectIdentity = ObjectIdentity
gepoel2esw12OltBridgeConfig = _Gepoel2esw12OltBridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 5)
)
_Gepoel2esw12OltBridgingConfAgeLimit_Type = Integer32
_Gepoel2esw12OltBridgingConfAgeLimit_Object = MibScalar
gepoel2esw12OltBridgingConfAgeLimit = _Gepoel2esw12OltBridgingConfAgeLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 5, 1),
    _Gepoel2esw12OltBridgingConfAgeLimit_Type()
)
gepoel2esw12OltBridgingConfAgeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltBridgingConfAgeLimit.setStatus("current")
_Gepoel2esw12OltBridgingConfAllowVlanOnSimple_Type = Integer32
_Gepoel2esw12OltBridgingConfAllowVlanOnSimple_Object = MibScalar
gepoel2esw12OltBridgingConfAllowVlanOnSimple = _Gepoel2esw12OltBridgingConfAllowVlanOnSimple_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 5, 2),
    _Gepoel2esw12OltBridgingConfAllowVlanOnSimple_Type()
)
gepoel2esw12OltBridgingConfAllowVlanOnSimple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltBridgingConfAllowVlanOnSimple.setStatus("current")
_Gepoel2esw12OltDBA_ObjectIdentity = ObjectIdentity
gepoel2esw12OltDBA = _Gepoel2esw12OltDBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6)
)
_Gepoel2esw12OltAggregateShaperTable_Object = MibTable
gepoel2esw12OltAggregateShaperTable = _Gepoel2esw12OltAggregateShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltAggregateShaperTable.setStatus("current")
_Gepoel2esw12OltAggregateShaperEntry_Object = MibTableRow
gepoel2esw12OltAggregateShaperEntry = _Gepoel2esw12OltAggregateShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 1, 1)
)
gepoel2esw12OltAggregateShaperEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltAggregateShaperIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltAggregateShaperEntry.setStatus("current")


class _Gepoel2esw12OltAggregateShaperIndex_Type(Integer32):
    """Custom type gepoel2esw12OltAggregateShaperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gepoel2esw12OltAggregateShaperIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltAggregateShaperIndex_Object = MibTableColumn
gepoel2esw12OltAggregateShaperIndex = _Gepoel2esw12OltAggregateShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 1, 1, 1),
    _Gepoel2esw12OltAggregateShaperIndex_Type()
)
gepoel2esw12OltAggregateShaperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltAggregateShaperIndex.setStatus("current")


class _Gepoel2esw12OltAggregateShaperBwEnable_Type(Integer32):
    """Custom type gepoel2esw12OltAggregateShaperBwEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltAggregateShaperBwEnable_Type.__name__ = "Integer32"
_Gepoel2esw12OltAggregateShaperBwEnable_Object = MibTableColumn
gepoel2esw12OltAggregateShaperBwEnable = _Gepoel2esw12OltAggregateShaperBwEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 1, 1, 2),
    _Gepoel2esw12OltAggregateShaperBwEnable_Type()
)
gepoel2esw12OltAggregateShaperBwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltAggregateShaperBwEnable.setStatus("current")


class _Gepoel2esw12OltAggregateShaperMaxBw_Type(Integer32):
    """Custom type gepoel2esw12OltAggregateShaperMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12OltAggregateShaperMaxBw_Type.__name__ = "Integer32"
_Gepoel2esw12OltAggregateShaperMaxBw_Object = MibTableColumn
gepoel2esw12OltAggregateShaperMaxBw = _Gepoel2esw12OltAggregateShaperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 1, 1, 3),
    _Gepoel2esw12OltAggregateShaperMaxBw_Type()
)
gepoel2esw12OltAggregateShaperMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltAggregateShaperMaxBw.setStatus("current")


class _Gepoel2esw12OltAggregateShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12OltAggregateShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltAggregateShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12OltAggregateShaperMaxBurst_Object = MibTableColumn
gepoel2esw12OltAggregateShaperMaxBurst = _Gepoel2esw12OltAggregateShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 1, 1, 4),
    _Gepoel2esw12OltAggregateShaperMaxBurst_Type()
)
gepoel2esw12OltAggregateShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltAggregateShaperMaxBurst.setStatus("current")
_Gepoel2esw12OltDropDownWeightsTable_Object = MibTable
gepoel2esw12OltDropDownWeightsTable = _Gepoel2esw12OltDropDownWeightsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownWeightsTable.setStatus("current")
_Gepoel2esw12OltDropDownWeightsEntry_Object = MibTableRow
gepoel2esw12OltDropDownWeightsEntry = _Gepoel2esw12OltDropDownWeightsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1)
)
gepoel2esw12OltDropDownWeightsEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltDropDownWeightsIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownWeightsEntry.setStatus("current")


class _Gepoel2esw12OltDropDownWeightsIndex_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownWeightsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gepoel2esw12OltDropDownWeightsIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownWeightsIndex_Object = MibTableColumn
gepoel2esw12OltDropDownWeightsIndex = _Gepoel2esw12OltDropDownWeightsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 1),
    _Gepoel2esw12OltDropDownWeightsIndex_Type()
)
gepoel2esw12OltDropDownWeightsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownWeightsIndex.setStatus("current")


class _Gepoel2esw12OltDropDownLevel1_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel1_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel1_Object = MibTableColumn
gepoel2esw12OltDropDownLevel1 = _Gepoel2esw12OltDropDownLevel1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 2),
    _Gepoel2esw12OltDropDownLevel1_Type()
)
gepoel2esw12OltDropDownLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel1.setStatus("current")


class _Gepoel2esw12OltDropDownLevel2_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel2_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel2_Object = MibScalar
gepoel2esw12OltDropDownLevel2 = _Gepoel2esw12OltDropDownLevel2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 3),
    _Gepoel2esw12OltDropDownLevel2_Type()
)
gepoel2esw12OltDropDownLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel2.setStatus("current")


class _Gepoel2esw12OltDropDownLevel3_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel3_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel3_Object = MibScalar
gepoel2esw12OltDropDownLevel3 = _Gepoel2esw12OltDropDownLevel3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 4),
    _Gepoel2esw12OltDropDownLevel3_Type()
)
gepoel2esw12OltDropDownLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel3.setStatus("current")


class _Gepoel2esw12OltDropDownLevel4_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel4_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel4_Object = MibScalar
gepoel2esw12OltDropDownLevel4 = _Gepoel2esw12OltDropDownLevel4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 5),
    _Gepoel2esw12OltDropDownLevel4_Type()
)
gepoel2esw12OltDropDownLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel4.setStatus("current")


class _Gepoel2esw12OltDropDownLevel5_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel5_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel5_Object = MibScalar
gepoel2esw12OltDropDownLevel5 = _Gepoel2esw12OltDropDownLevel5_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 6),
    _Gepoel2esw12OltDropDownLevel5_Type()
)
gepoel2esw12OltDropDownLevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel5.setStatus("current")


class _Gepoel2esw12OltDropDownLevel6_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel6_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel6_Object = MibScalar
gepoel2esw12OltDropDownLevel6 = _Gepoel2esw12OltDropDownLevel6_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 7),
    _Gepoel2esw12OltDropDownLevel6_Type()
)
gepoel2esw12OltDropDownLevel6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel6.setStatus("current")


class _Gepoel2esw12OltDropDownLevel7_Type(Integer32):
    """Custom type gepoel2esw12OltDropDownLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltDropDownLevel7_Type.__name__ = "Integer32"
_Gepoel2esw12OltDropDownLevel7_Object = MibScalar
gepoel2esw12OltDropDownLevel7 = _Gepoel2esw12OltDropDownLevel7_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 2, 1, 8),
    _Gepoel2esw12OltDropDownLevel7_Type()
)
gepoel2esw12OltDropDownLevel7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDropDownLevel7.setStatus("current")
_Gepoel2esw12OltPollingRateTable_Object = MibTable
gepoel2esw12OltPollingRateTable = _Gepoel2esw12OltPollingRateTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateTable.setStatus("current")
_Gepoel2esw12OltPollingRateEntry_Object = MibTableRow
gepoel2esw12OltPollingRateEntry = _Gepoel2esw12OltPollingRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1)
)
gepoel2esw12OltPollingRateEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltPollingRateIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateEntry.setStatus("current")


class _Gepoel2esw12OltPollingRateIndex_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OltPollingRateIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateIndex_Object = MibTableColumn
gepoel2esw12OltPollingRateIndex = _Gepoel2esw12OltPollingRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 1),
    _Gepoel2esw12OltPollingRateIndex_Type()
)
gepoel2esw12OltPollingRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateIndex.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel0_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel0_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel0_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel0 = _Gepoel2esw12OltPollingRateLevel0_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 2),
    _Gepoel2esw12OltPollingRateLevel0_Type()
)
gepoel2esw12OltPollingRateLevel0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel0.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel1_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel1_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel1_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel1 = _Gepoel2esw12OltPollingRateLevel1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 3),
    _Gepoel2esw12OltPollingRateLevel1_Type()
)
gepoel2esw12OltPollingRateLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel1.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel2_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel2_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel2_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel2 = _Gepoel2esw12OltPollingRateLevel2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 4),
    _Gepoel2esw12OltPollingRateLevel2_Type()
)
gepoel2esw12OltPollingRateLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel2.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel3_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel3_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel3_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel3 = _Gepoel2esw12OltPollingRateLevel3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 5),
    _Gepoel2esw12OltPollingRateLevel3_Type()
)
gepoel2esw12OltPollingRateLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel3.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel4_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel4_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel4_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel4 = _Gepoel2esw12OltPollingRateLevel4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 6),
    _Gepoel2esw12OltPollingRateLevel4_Type()
)
gepoel2esw12OltPollingRateLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel4.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel5_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel5_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel5_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel5 = _Gepoel2esw12OltPollingRateLevel5_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 7),
    _Gepoel2esw12OltPollingRateLevel5_Type()
)
gepoel2esw12OltPollingRateLevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel5.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel6_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel6_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel6_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel6 = _Gepoel2esw12OltPollingRateLevel6_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 8),
    _Gepoel2esw12OltPollingRateLevel6_Type()
)
gepoel2esw12OltPollingRateLevel6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel6.setStatus("current")


class _Gepoel2esw12OltPollingRateLevel7_Type(Integer32):
    """Custom type gepoel2esw12OltPollingRateLevel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gepoel2esw12OltPollingRateLevel7_Type.__name__ = "Integer32"
_Gepoel2esw12OltPollingRateLevel7_Object = MibTableColumn
gepoel2esw12OltPollingRateLevel7 = _Gepoel2esw12OltPollingRateLevel7_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 6, 3, 1, 9),
    _Gepoel2esw12OltPollingRateLevel7_Type()
)
gepoel2esw12OltPollingRateLevel7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltPollingRateLevel7.setStatus("current")
_Gepoel2esw12OltIgmpProxy_ObjectIdentity = ObjectIdentity
gepoel2esw12OltIgmpProxy = _Gepoel2esw12OltIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 7)
)


class _Gepoel2esw12OltMaxIGMPGroup_Type(Integer32):
    """Custom type gepoel2esw12OltMaxIGMPGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Gepoel2esw12OltMaxIGMPGroup_Type.__name__ = "Integer32"
_Gepoel2esw12OltMaxIGMPGroup_Object = MibScalar
gepoel2esw12OltMaxIGMPGroup = _Gepoel2esw12OltMaxIGMPGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 7, 1),
    _Gepoel2esw12OltMaxIGMPGroup_Type()
)
gepoel2esw12OltMaxIGMPGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltMaxIGMPGroup.setStatus("current")


class _Gepoel2esw12OltGlobalBwPollSize_Type(Integer32):
    """Custom type gepoel2esw12OltGlobalBwPollSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_Gepoel2esw12OltGlobalBwPollSize_Type.__name__ = "Integer32"
_Gepoel2esw12OltGlobalBwPollSize_Object = MibScalar
gepoel2esw12OltGlobalBwPollSize = _Gepoel2esw12OltGlobalBwPollSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 7, 2),
    _Gepoel2esw12OltGlobalBwPollSize_Type()
)
gepoel2esw12OltGlobalBwPollSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltGlobalBwPollSize.setStatus("current")


class _Gepoel2esw12OltIgmpCaptureAllMode_Type(Integer32):
    """Custom type gepoel2esw12OltIgmpCaptureAllMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Gepoel2esw12OltIgmpCaptureAllMode_Type.__name__ = "Integer32"
_Gepoel2esw12OltIgmpCaptureAllMode_Object = MibScalar
gepoel2esw12OltIgmpCaptureAllMode = _Gepoel2esw12OltIgmpCaptureAllMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 7, 3),
    _Gepoel2esw12OltIgmpCaptureAllMode_Type()
)
gepoel2esw12OltIgmpCaptureAllMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltIgmpCaptureAllMode.setStatus("current")


class _Gepoel2esw12OltIgmpDAForwarding_Type(Integer32):
    """Custom type gepoel2esw12OltIgmpDAForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Gepoel2esw12OltIgmpDAForwarding_Type.__name__ = "Integer32"
_Gepoel2esw12OltIgmpDAForwarding_Object = MibScalar
gepoel2esw12OltIgmpDAForwarding = _Gepoel2esw12OltIgmpDAForwarding_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 7, 4),
    _Gepoel2esw12OltIgmpDAForwarding_Type()
)
gepoel2esw12OltIgmpDAForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltIgmpDAForwarding.setStatus("current")


class _Gepoel2esw12OltIgmpSAForwarding_Type(Integer32):
    """Custom type gepoel2esw12OltIgmpSAForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Gepoel2esw12OltIgmpSAForwarding_Type.__name__ = "Integer32"
_Gepoel2esw12OltIgmpSAForwarding_Object = MibScalar
gepoel2esw12OltIgmpSAForwarding = _Gepoel2esw12OltIgmpSAForwarding_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 7, 5),
    _Gepoel2esw12OltIgmpSAForwarding_Type()
)
gepoel2esw12OltIgmpSAForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltIgmpSAForwarding.setStatus("current")
_Gepoel2esw12OltNetworkParameters_ObjectIdentity = ObjectIdentity
gepoel2esw12OltNetworkParameters = _Gepoel2esw12OltNetworkParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8)
)
_Gepoel2esw12OltOamParameters_ObjectIdentity = ObjectIdentity
gepoel2esw12OltOamParameters = _Gepoel2esw12OltOamParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 1)
)


class _Gepoel2esw12OltMaxOamRate_Type(Integer32):
    """Custom type gepoel2esw12OltMaxOamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Gepoel2esw12OltMaxOamRate_Type.__name__ = "Integer32"
_Gepoel2esw12OltMaxOamRate_Object = MibScalar
gepoel2esw12OltMaxOamRate = _Gepoel2esw12OltMaxOamRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 1, 1),
    _Gepoel2esw12OltMaxOamRate_Type()
)
gepoel2esw12OltMaxOamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltMaxOamRate.setStatus("current")


class _Gepoel2esw12OltMinOamRate_Type(Integer32):
    """Custom type gepoel2esw12OltMinOamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Gepoel2esw12OltMinOamRate_Type.__name__ = "Integer32"
_Gepoel2esw12OltMinOamRate_Object = MibScalar
gepoel2esw12OltMinOamRate = _Gepoel2esw12OltMinOamRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 1, 2),
    _Gepoel2esw12OltMinOamRate_Type()
)
gepoel2esw12OltMinOamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltMinOamRate.setStatus("current")


class _Gepoel2esw12OltLoopbackTimeout_Type(Integer32):
    """Custom type gepoel2esw12OltLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 65535),
    )


_Gepoel2esw12OltLoopbackTimeout_Type.__name__ = "Integer32"
_Gepoel2esw12OltLoopbackTimeout_Object = MibScalar
gepoel2esw12OltLoopbackTimeout = _Gepoel2esw12OltLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 1, 3),
    _Gepoel2esw12OltLoopbackTimeout_Type()
)
gepoel2esw12OltLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltLoopbackTimeout.setStatus("current")
_Gepoel2esw12OltVlanParameters_ObjectIdentity = ObjectIdentity
gepoel2esw12OltVlanParameters = _Gepoel2esw12OltVlanParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 2)
)
_Gepoel2esw12OltVlanEtherType_Type = DisplayString
_Gepoel2esw12OltVlanEtherType_Object = MibScalar
gepoel2esw12OltVlanEtherType = _Gepoel2esw12OltVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 2, 1),
    _Gepoel2esw12OltVlanEtherType_Type()
)
gepoel2esw12OltVlanEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltVlanEtherType.setStatus("current")


class _Gepoel2esw12OltTagUp_Type(Integer32):
    """Custom type gepoel2esw12OltTagUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltTagUp_Type.__name__ = "Integer32"
_Gepoel2esw12OltTagUp_Object = MibScalar
gepoel2esw12OltTagUp = _Gepoel2esw12OltTagUp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 2, 2),
    _Gepoel2esw12OltTagUp_Type()
)
gepoel2esw12OltTagUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltTagUp.setStatus("current")


class _Gepoel2esw12OltTagDown_Type(Integer32):
    """Custom type gepoel2esw12OltTagDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltTagDown_Type.__name__ = "Integer32"
_Gepoel2esw12OltTagDown_Object = MibScalar
gepoel2esw12OltTagDown = _Gepoel2esw12OltTagDown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 2, 3),
    _Gepoel2esw12OltTagDown_Type()
)
gepoel2esw12OltTagDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltTagDown.setStatus("current")
_Gepoel2esw12OltMpcpParametersTable_Object = MibTable
gepoel2esw12OltMpcpParametersTable = _Gepoel2esw12OltMpcpParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 3)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltMpcpParametersTable.setStatus("current")
_Gepoel2esw12OltMpcpParametersEntry_Object = MibTableRow
gepoel2esw12OltMpcpParametersEntry = _Gepoel2esw12OltMpcpParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 3, 1)
)
gepoel2esw12OltMpcpParametersEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltMpcpParametersIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltMpcpParametersEntry.setStatus("current")


class _Gepoel2esw12OltMpcpParametersIndex_Type(Integer32):
    """Custom type gepoel2esw12OltMpcpParametersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OltMpcpParametersIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltMpcpParametersIndex_Object = MibTableColumn
gepoel2esw12OltMpcpParametersIndex = _Gepoel2esw12OltMpcpParametersIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 3, 1, 1),
    _Gepoel2esw12OltMpcpParametersIndex_Type()
)
gepoel2esw12OltMpcpParametersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltMpcpParametersIndex.setStatus("current")


class _Gepoel2esw12OltMpcpDiscoveryPeriod_Type(Integer32):
    """Custom type gepoel2esw12OltMpcpDiscoveryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gepoel2esw12OltMpcpDiscoveryPeriod_Type.__name__ = "Integer32"
_Gepoel2esw12OltMpcpDiscoveryPeriod_Object = MibTableColumn
gepoel2esw12OltMpcpDiscoveryPeriod = _Gepoel2esw12OltMpcpDiscoveryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 3, 1, 2),
    _Gepoel2esw12OltMpcpDiscoveryPeriod_Type()
)
gepoel2esw12OltMpcpDiscoveryPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltMpcpDiscoveryPeriod.setStatus("current")


class _Gepoel2esw12OltMpcpDiscoveryWindow_Type(Integer32):
    """Custom type gepoel2esw12OltMpcpDiscoveryWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(84, 131070),
    )


_Gepoel2esw12OltMpcpDiscoveryWindow_Type.__name__ = "Integer32"
_Gepoel2esw12OltMpcpDiscoveryWindow_Object = MibTableColumn
gepoel2esw12OltMpcpDiscoveryWindow = _Gepoel2esw12OltMpcpDiscoveryWindow_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 8, 3, 1, 3),
    _Gepoel2esw12OltMpcpDiscoveryWindow_Type()
)
gepoel2esw12OltMpcpDiscoveryWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltMpcpDiscoveryWindow.setStatus("current")
_Gepoel2esw12OltOperation_ObjectIdentity = ObjectIdentity
gepoel2esw12OltOperation = _Gepoel2esw12OltOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 9)
)


class _Gepoel2esw12OltEnable_Type(Integer32):
    """Custom type gepoel2esw12OltEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltEnable_Type.__name__ = "Integer32"
_Gepoel2esw12OltEnable_Object = MibScalar
gepoel2esw12OltEnable = _Gepoel2esw12OltEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 9, 1),
    _Gepoel2esw12OltEnable_Type()
)
gepoel2esw12OltEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltEnable.setStatus("current")


class _Gepoel2esw12OltDisable_Type(Integer32):
    """Custom type gepoel2esw12OltDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltDisable_Type.__name__ = "Integer32"
_Gepoel2esw12OltDisable_Object = MibScalar
gepoel2esw12OltDisable = _Gepoel2esw12OltDisable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 9, 2),
    _Gepoel2esw12OltDisable_Type()
)
gepoel2esw12OltDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltDisable.setStatus("current")
_Gepoel2esw12OltBlockLinkListTable_Object = MibTable
gepoel2esw12OltBlockLinkListTable = _Gepoel2esw12OltBlockLinkListTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 10)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltBlockLinkListTable.setStatus("current")
_Gepoel2esw12OltBlockLinkListEntry_Object = MibTableRow
gepoel2esw12OltBlockLinkListEntry = _Gepoel2esw12OltBlockLinkListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 10, 1)
)
gepoel2esw12OltBlockLinkListEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OltBlockLinkIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltBlockLinkListEntry.setStatus("current")


class _Gepoel2esw12OltBlockLinkIndex_Type(Integer32):
    """Custom type gepoel2esw12OltBlockLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_Gepoel2esw12OltBlockLinkIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OltBlockLinkIndex_Object = MibTableColumn
gepoel2esw12OltBlockLinkIndex = _Gepoel2esw12OltBlockLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 10, 1, 1),
    _Gepoel2esw12OltBlockLinkIndex_Type()
)
gepoel2esw12OltBlockLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OltBlockLinkIndex.setStatus("current")
_Gepoel2esw12OltBlockLinkLabel_Type = MacAddress
_Gepoel2esw12OltBlockLinkLabel_Object = MibTableColumn
gepoel2esw12OltBlockLinkLabel = _Gepoel2esw12OltBlockLinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 10, 1, 2),
    _Gepoel2esw12OltBlockLinkLabel_Type()
)
gepoel2esw12OltBlockLinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OltBlockLinkLabel.setStatus("current")


class _Gepoel2esw12OltBlockLinkUnblock_Type(Integer32):
    """Custom type gepoel2esw12OltBlockLinkUnblock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OltBlockLinkUnblock_Type.__name__ = "Integer32"
_Gepoel2esw12OltBlockLinkUnblock_Object = MibTableColumn
gepoel2esw12OltBlockLinkUnblock = _Gepoel2esw12OltBlockLinkUnblock_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 10, 1, 3),
    _Gepoel2esw12OltBlockLinkUnblock_Type()
)
gepoel2esw12OltBlockLinkUnblock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OltBlockLinkUnblock.setStatus("current")
_Gepoel2esw12OltAllKnownLinkProvision_ObjectIdentity = ObjectIdentity
gepoel2esw12OltAllKnownLinkProvision = _Gepoel2esw12OltAllKnownLinkProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11)
)
_Gepoel2esw12OltProvisionInOltTable_Object = MibTable
gepoel2esw12OltProvisionInOltTable = _Gepoel2esw12OltProvisionInOltTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltProvisionInOltTable.setStatus("current")
_Gepoel2esw12OltProvisionInOltEntry_Object = MibTableRow
gepoel2esw12OltProvisionInOltEntry = _Gepoel2esw12OltProvisionInOltEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1)
)
gepoel2esw12OltProvisionInOltEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12ProvInOltIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltProvisionInOltEntry.setStatus("current")


class _Gepoel2esw12ProvInOltIndex_Type(Integer32):
    """Custom type gepoel2esw12ProvInOltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_Gepoel2esw12ProvInOltIndex_Type.__name__ = "Integer32"
_Gepoel2esw12ProvInOltIndex_Object = MibTableColumn
gepoel2esw12ProvInOltIndex = _Gepoel2esw12ProvInOltIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 1),
    _Gepoel2esw12ProvInOltIndex_Type()
)
gepoel2esw12ProvInOltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInOltIndex.setStatus("current")
_Gepoel2esw12ProvInOltLinkLabel_Type = MacAddress
_Gepoel2esw12ProvInOltLinkLabel_Object = MibTableColumn
gepoel2esw12ProvInOltLinkLabel = _Gepoel2esw12ProvInOltLinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 2),
    _Gepoel2esw12ProvInOltLinkLabel_Type()
)
gepoel2esw12ProvInOltLinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInOltLinkLabel.setStatus("current")
_Gepoel2esw12ProvInOltBridge_Type = Integer32
_Gepoel2esw12ProvInOltBridge_Object = MibTableColumn
gepoel2esw12ProvInOltBridge = _Gepoel2esw12ProvInOltBridge_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 3),
    _Gepoel2esw12ProvInOltBridge_Type()
)
gepoel2esw12ProvInOltBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInOltBridge.setStatus("current")


class _Gepoel2esw12ProvInOltSourceEpon_Type(Integer32):
    """Custom type gepoel2esw12ProvInOltSourceEpon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_Gepoel2esw12ProvInOltSourceEpon_Type.__name__ = "Integer32"
_Gepoel2esw12ProvInOltSourceEpon_Object = MibTableColumn
gepoel2esw12ProvInOltSourceEpon = _Gepoel2esw12ProvInOltSourceEpon_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 4),
    _Gepoel2esw12ProvInOltSourceEpon_Type()
)
gepoel2esw12ProvInOltSourceEpon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInOltSourceEpon.setStatus("current")


class _Gepoel2esw12ProvInOltDestNNI_Type(Integer32):
    """Custom type gepoel2esw12ProvInOltDestNNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12ProvInOltDestNNI_Type.__name__ = "Integer32"
_Gepoel2esw12ProvInOltDestNNI_Object = MibTableColumn
gepoel2esw12ProvInOltDestNNI = _Gepoel2esw12ProvInOltDestNNI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 5),
    _Gepoel2esw12ProvInOltDestNNI_Type()
)
gepoel2esw12ProvInOltDestNNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInOltDestNNI.setStatus("current")
_Gepoel2esw12ProvInOltVlan_Type = DisplayString
_Gepoel2esw12ProvInOltVlan_Object = MibTableColumn
gepoel2esw12ProvInOltVlan = _Gepoel2esw12ProvInOltVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 6),
    _Gepoel2esw12ProvInOltVlan_Type()
)
gepoel2esw12ProvInOltVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInOltVlan.setStatus("current")


class _Gepoel2esw12DelProvInOlt_Type(Integer32):
    """Custom type gepoel2esw12DelProvInOlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DelProvInOlt_Type.__name__ = "Integer32"
_Gepoel2esw12DelProvInOlt_Object = MibTableColumn
gepoel2esw12DelProvInOlt = _Gepoel2esw12DelProvInOlt_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 1, 1, 7),
    _Gepoel2esw12DelProvInOlt_Type()
)
gepoel2esw12DelProvInOlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12DelProvInOlt.setStatus("current")
_Gepoel2esw12OltProvisionInHostTable_Object = MibTable
gepoel2esw12OltProvisionInHostTable = _Gepoel2esw12OltProvisionInHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OltProvisionInHostTable.setStatus("current")
_Gepoel2esw12OltProvisionInHostEntry_Object = MibTableRow
gepoel2esw12OltProvisionInHostEntry = _Gepoel2esw12OltProvisionInHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1)
)
gepoel2esw12OltProvisionInHostEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12ProvInHostEponPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12ProvInHostIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OltProvisionInHostEntry.setStatus("current")


class _Gepoel2esw12ProvInHostEponPort_Type(Integer32):
    """Custom type gepoel2esw12ProvInHostEponPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12ProvInHostEponPort_Type.__name__ = "Integer32"
_Gepoel2esw12ProvInHostEponPort_Object = MibTableColumn
gepoel2esw12ProvInHostEponPort = _Gepoel2esw12ProvInHostEponPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 1),
    _Gepoel2esw12ProvInHostEponPort_Type()
)
gepoel2esw12ProvInHostEponPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInHostEponPort.setStatus("current")
_Gepoel2esw12ProvInHostIndex_Type = Integer32
_Gepoel2esw12ProvInHostIndex_Object = MibTableColumn
gepoel2esw12ProvInHostIndex = _Gepoel2esw12ProvInHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 2),
    _Gepoel2esw12ProvInHostIndex_Type()
)
gepoel2esw12ProvInHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInHostIndex.setStatus("current")
_Gepoel2esw12ProvInHostLinkLabel_Type = MacAddress
_Gepoel2esw12ProvInHostLinkLabel_Object = MibTableColumn
gepoel2esw12ProvInHostLinkLabel = _Gepoel2esw12ProvInHostLinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 3),
    _Gepoel2esw12ProvInHostLinkLabel_Type()
)
gepoel2esw12ProvInHostLinkLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInHostLinkLabel.setStatus("current")


class _Gepoel2esw12ProvInHostBridge_Type(Integer32):
    """Custom type gepoel2esw12ProvInHostBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_Gepoel2esw12ProvInHostBridge_Type.__name__ = "Integer32"
_Gepoel2esw12ProvInHostBridge_Object = MibTableColumn
gepoel2esw12ProvInHostBridge = _Gepoel2esw12ProvInHostBridge_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 4),
    _Gepoel2esw12ProvInHostBridge_Type()
)
gepoel2esw12ProvInHostBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInHostBridge.setStatus("current")


class _Gepoel2esw12ProvInHostBridgeDestNNI_Type(Integer32):
    """Custom type gepoel2esw12ProvInHostBridgeDestNNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12ProvInHostBridgeDestNNI_Type.__name__ = "Integer32"
_Gepoel2esw12ProvInHostBridgeDestNNI_Object = MibTableColumn
gepoel2esw12ProvInHostBridgeDestNNI = _Gepoel2esw12ProvInHostBridgeDestNNI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 5),
    _Gepoel2esw12ProvInHostBridgeDestNNI_Type()
)
gepoel2esw12ProvInHostBridgeDestNNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInHostBridgeDestNNI.setStatus("current")
_Gepoel2esw12ProvInHostVlan_Type = DisplayString
_Gepoel2esw12ProvInHostVlan_Object = MibTableColumn
gepoel2esw12ProvInHostVlan = _Gepoel2esw12ProvInHostVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 6),
    _Gepoel2esw12ProvInHostVlan_Type()
)
gepoel2esw12ProvInHostVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12ProvInHostVlan.setStatus("current")


class _Gepoel2esw12DelProvInHost_Type(Integer32):
    """Custom type gepoel2esw12DelProvInHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DelProvInHost_Type.__name__ = "Integer32"
_Gepoel2esw12DelProvInHost_Object = MibTableColumn
gepoel2esw12DelProvInHost = _Gepoel2esw12DelProvInHost_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 2, 11, 2, 1, 7),
    _Gepoel2esw12DelProvInHost_Type()
)
gepoel2esw12DelProvInHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DelProvInHost.setStatus("current")
_Gepoel2esw12OnuManagement_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuManagement = _Gepoel2esw12OnuManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3)
)
_Gepoel2esw12OnuStatisticsTable_Object = MibTable
gepoel2esw12OnuStatisticsTable = _Gepoel2esw12OnuStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuStatisticsTable.setStatus("current")
_Gepoel2esw12OnuStatisticsEntry_Object = MibTableRow
gepoel2esw12OnuStatisticsEntry = _Gepoel2esw12OnuStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1)
)
gepoel2esw12OnuStatisticsEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuPortStatisticsMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuPortStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuStatisticsEntry.setStatus("current")
_Gepoel2esw12OnuPortStatisticsMacAddress_Type = MacAddress
_Gepoel2esw12OnuPortStatisticsMacAddress_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsMacAddress = _Gepoel2esw12OnuPortStatisticsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 1),
    _Gepoel2esw12OnuPortStatisticsMacAddress_Type()
)
gepoel2esw12OnuPortStatisticsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsMacAddress.setStatus("current")


class _Gepoel2esw12OnuPortStatisticsIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuPortStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gepoel2esw12OnuPortStatisticsIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortStatisticsIndex_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsIndex = _Gepoel2esw12OnuPortStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 2),
    _Gepoel2esw12OnuPortStatisticsIndex_Type()
)
gepoel2esw12OnuPortStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsIndex.setStatus("current")
_Gepoel2esw12OnuPortStatisticsOctetTransfer_Type = Counter64
_Gepoel2esw12OnuPortStatisticsOctetTransfer_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsOctetTransfer = _Gepoel2esw12OnuPortStatisticsOctetTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 3),
    _Gepoel2esw12OnuPortStatisticsOctetTransfer_Type()
)
gepoel2esw12OnuPortStatisticsOctetTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsOctetTransfer.setStatus("current")
_Gepoel2esw12OnuPortStatisticsTotalFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsTotalFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsTotalFrame = _Gepoel2esw12OnuPortStatisticsTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 4),
    _Gepoel2esw12OnuPortStatisticsTotalFrame_Type()
)
gepoel2esw12OnuPortStatisticsTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsTotalFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsUnicastFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsUnicastFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsUnicastFrame = _Gepoel2esw12OnuPortStatisticsUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 5),
    _Gepoel2esw12OnuPortStatisticsUnicastFrame_Type()
)
gepoel2esw12OnuPortStatisticsUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsUnicastFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsMulticastFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsMulticastFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsMulticastFrame = _Gepoel2esw12OnuPortStatisticsMulticastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 6),
    _Gepoel2esw12OnuPortStatisticsMulticastFrame_Type()
)
gepoel2esw12OnuPortStatisticsMulticastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsMulticastFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsBroadcastFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsBroadcastFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsBroadcastFrame = _Gepoel2esw12OnuPortStatisticsBroadcastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 7),
    _Gepoel2esw12OnuPortStatisticsBroadcastFrame_Type()
)
gepoel2esw12OnuPortStatisticsBroadcastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsBroadcastFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics64OctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics64OctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics64OctetFrame = _Gepoel2esw12OnuPortStatistics64OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 8),
    _Gepoel2esw12OnuPortStatistics64OctetFrame_Type()
)
gepoel2esw12OnuPortStatistics64OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics64OctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics65to127OctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics65to127OctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics65to127OctetFrame = _Gepoel2esw12OnuPortStatistics65to127OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 9),
    _Gepoel2esw12OnuPortStatistics65to127OctetFrame_Type()
)
gepoel2esw12OnuPortStatistics65to127OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics65to127OctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics128to255OctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics128to255OctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics128to255OctetFrame = _Gepoel2esw12OnuPortStatistics128to255OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 10),
    _Gepoel2esw12OnuPortStatistics128to255OctetFrame_Type()
)
gepoel2esw12OnuPortStatistics128to255OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics128to255OctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics256to511OctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics256to511OctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics256to511OctetFrame = _Gepoel2esw12OnuPortStatistics256to511OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 11),
    _Gepoel2esw12OnuPortStatistics256to511OctetFrame_Type()
)
gepoel2esw12OnuPortStatistics256to511OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics256to511OctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics512to1023OctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics512to1023OctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics512to1023OctetFrame = _Gepoel2esw12OnuPortStatistics512to1023OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 12),
    _Gepoel2esw12OnuPortStatistics512to1023OctetFrame_Type()
)
gepoel2esw12OnuPortStatistics512to1023OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics512to1023OctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics1024to1518OctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics1024to1518OctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics1024to1518OctetFrame = _Gepoel2esw12OnuPortStatistics1024to1518OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 13),
    _Gepoel2esw12OnuPortStatistics1024to1518OctetFrame_Type()
)
gepoel2esw12OnuPortStatistics1024to1518OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics1024to1518OctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatistics1519upOctetFrame_Type = Counter64
_Gepoel2esw12OnuPortStatistics1519upOctetFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatistics1519upOctetFrame = _Gepoel2esw12OnuPortStatistics1519upOctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 14),
    _Gepoel2esw12OnuPortStatistics1519upOctetFrame_Type()
)
gepoel2esw12OnuPortStatistics1519upOctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatistics1519upOctetFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsUndersizeFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsUndersizeFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsUndersizeFrame = _Gepoel2esw12OnuPortStatisticsUndersizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 15),
    _Gepoel2esw12OnuPortStatisticsUndersizeFrame_Type()
)
gepoel2esw12OnuPortStatisticsUndersizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsUndersizeFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsFCSError_Type = Counter64
_Gepoel2esw12OnuPortStatisticsFCSError_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsFCSError = _Gepoel2esw12OnuPortStatisticsFCSError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 16),
    _Gepoel2esw12OnuPortStatisticsFCSError_Type()
)
gepoel2esw12OnuPortStatisticsFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsFCSError.setStatus("current")
_Gepoel2esw12OnuPortStatisticsCRC8Error_Type = Counter64
_Gepoel2esw12OnuPortStatisticsCRC8Error_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsCRC8Error = _Gepoel2esw12OnuPortStatisticsCRC8Error_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 17),
    _Gepoel2esw12OnuPortStatisticsCRC8Error_Type()
)
gepoel2esw12OnuPortStatisticsCRC8Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsCRC8Error.setStatus("current")
_Gepoel2esw12OnuPortStatisticsLineCodeError_Type = Counter64
_Gepoel2esw12OnuPortStatisticsLineCodeError_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsLineCodeError = _Gepoel2esw12OnuPortStatisticsLineCodeError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 18),
    _Gepoel2esw12OnuPortStatisticsLineCodeError_Type()
)
gepoel2esw12OnuPortStatisticsLineCodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsLineCodeError.setStatus("current")
_Gepoel2esw12OnuPortStatisticsBytesDropped_Type = Counter64
_Gepoel2esw12OnuPortStatisticsBytesDropped_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsBytesDropped = _Gepoel2esw12OnuPortStatisticsBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 19),
    _Gepoel2esw12OnuPortStatisticsBytesDropped_Type()
)
gepoel2esw12OnuPortStatisticsBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsBytesDropped.setStatus("current")
_Gepoel2esw12OnuPortStatisticsFramesDropped_Type = Counter64
_Gepoel2esw12OnuPortStatisticsFramesDropped_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsFramesDropped = _Gepoel2esw12OnuPortStatisticsFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 20),
    _Gepoel2esw12OnuPortStatisticsFramesDropped_Type()
)
gepoel2esw12OnuPortStatisticsFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsFramesDropped.setStatus("current")
_Gepoel2esw12OnuPortStatisticsBytesDelayed_Type = Counter64
_Gepoel2esw12OnuPortStatisticsBytesDelayed_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsBytesDelayed = _Gepoel2esw12OnuPortStatisticsBytesDelayed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 21),
    _Gepoel2esw12OnuPortStatisticsBytesDelayed_Type()
)
gepoel2esw12OnuPortStatisticsBytesDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsBytesDelayed.setStatus("current")
_Gepoel2esw12OnuPortStatisticsMaxDelay_Type = Counter64
_Gepoel2esw12OnuPortStatisticsMaxDelay_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsMaxDelay = _Gepoel2esw12OnuPortStatisticsMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 22),
    _Gepoel2esw12OnuPortStatisticsMaxDelay_Type()
)
gepoel2esw12OnuPortStatisticsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsMaxDelay.setStatus("current")
_Gepoel2esw12OnuPortStatisticsDelayThreshold_Type = Counter64
_Gepoel2esw12OnuPortStatisticsDelayThreshold_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsDelayThreshold = _Gepoel2esw12OnuPortStatisticsDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 23),
    _Gepoel2esw12OnuPortStatisticsDelayThreshold_Type()
)
gepoel2esw12OnuPortStatisticsDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsDelayThreshold.setStatus("current")
_Gepoel2esw12OnuPortStatisticsErroredFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsErroredFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsErroredFrame = _Gepoel2esw12OnuPortStatisticsErroredFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 24),
    _Gepoel2esw12OnuPortStatisticsErroredFrame_Type()
)
gepoel2esw12OnuPortStatisticsErroredFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsErroredFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsUnusedBytes_Type = Counter64
_Gepoel2esw12OnuPortStatisticsUnusedBytes_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsUnusedBytes = _Gepoel2esw12OnuPortStatisticsUnusedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 25),
    _Gepoel2esw12OnuPortStatisticsUnusedBytes_Type()
)
gepoel2esw12OnuPortStatisticsUnusedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsUnusedBytes.setStatus("current")
_Gepoel2esw12OnuPortStatisticsOversizedFrame_Type = Counter64
_Gepoel2esw12OnuPortStatisticsOversizedFrame_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsOversizedFrame = _Gepoel2esw12OnuPortStatisticsOversizedFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 26),
    _Gepoel2esw12OnuPortStatisticsOversizedFrame_Type()
)
gepoel2esw12OnuPortStatisticsOversizedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsOversizedFrame.setStatus("current")
_Gepoel2esw12OnuPortStatisticsPauseFrames_Type = Counter64
_Gepoel2esw12OnuPortStatisticsPauseFrames_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsPauseFrames = _Gepoel2esw12OnuPortStatisticsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 27),
    _Gepoel2esw12OnuPortStatisticsPauseFrames_Type()
)
gepoel2esw12OnuPortStatisticsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsPauseFrames.setStatus("current")
_Gepoel2esw12OnuPortStatisticsLengthErrors_Type = Counter64
_Gepoel2esw12OnuPortStatisticsLengthErrors_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsLengthErrors = _Gepoel2esw12OnuPortStatisticsLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 28),
    _Gepoel2esw12OnuPortStatisticsLengthErrors_Type()
)
gepoel2esw12OnuPortStatisticsLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsLengthErrors.setStatus("current")
_Gepoel2esw12OnuPortStatisticsAligmentErrors_Type = Counter64
_Gepoel2esw12OnuPortStatisticsAligmentErrors_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsAligmentErrors = _Gepoel2esw12OnuPortStatisticsAligmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 29),
    _Gepoel2esw12OnuPortStatisticsAligmentErrors_Type()
)
gepoel2esw12OnuPortStatisticsAligmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsAligmentErrors.setStatus("current")
_Gepoel2esw12OnuPortStatisticsCRC32Error_Type = Counter64
_Gepoel2esw12OnuPortStatisticsCRC32Error_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsCRC32Error = _Gepoel2esw12OnuPortStatisticsCRC32Error_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 30),
    _Gepoel2esw12OnuPortStatisticsCRC32Error_Type()
)
gepoel2esw12OnuPortStatisticsCRC32Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsCRC32Error.setStatus("current")
_Gepoel2esw12OnuPortStatisticsSingleCollision_Type = Counter64
_Gepoel2esw12OnuPortStatisticsSingleCollision_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsSingleCollision = _Gepoel2esw12OnuPortStatisticsSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 31),
    _Gepoel2esw12OnuPortStatisticsSingleCollision_Type()
)
gepoel2esw12OnuPortStatisticsSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsSingleCollision.setStatus("current")
_Gepoel2esw12OnuPortStatisticsMultipleCollision_Type = Counter64
_Gepoel2esw12OnuPortStatisticsMultipleCollision_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsMultipleCollision = _Gepoel2esw12OnuPortStatisticsMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 32),
    _Gepoel2esw12OnuPortStatisticsMultipleCollision_Type()
)
gepoel2esw12OnuPortStatisticsMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsMultipleCollision.setStatus("current")
_Gepoel2esw12OnuPortStatisticsLateCollision_Type = Counter64
_Gepoel2esw12OnuPortStatisticsLateCollision_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsLateCollision = _Gepoel2esw12OnuPortStatisticsLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 33),
    _Gepoel2esw12OnuPortStatisticsLateCollision_Type()
)
gepoel2esw12OnuPortStatisticsLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsLateCollision.setStatus("current")
_Gepoel2esw12OnuPortStatisticsExcessiveCollision_Type = Counter64
_Gepoel2esw12OnuPortStatisticsExcessiveCollision_Object = MibTableColumn
gepoel2esw12OnuPortStatisticsExcessiveCollision = _Gepoel2esw12OnuPortStatisticsExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 34),
    _Gepoel2esw12OnuPortStatisticsExcessiveCollision_Type()
)
gepoel2esw12OnuPortStatisticsExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortStatisticsExcessiveCollision.setStatus("current")


class _Gepoel2esw12OnuStatisticsClear_Type(Integer32):
    """Custom type gepoel2esw12OnuStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuStatisticsClear_Type.__name__ = "Integer32"
_Gepoel2esw12OnuStatisticsClear_Object = MibTableColumn
gepoel2esw12OnuStatisticsClear = _Gepoel2esw12OnuStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 1, 1, 35),
    _Gepoel2esw12OnuStatisticsClear_Type()
)
gepoel2esw12OnuStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuStatisticsClear.setStatus("current")
_Gepoel2esw12OnuInformationTable_Object = MibTable
gepoel2esw12OnuInformationTable = _Gepoel2esw12OnuInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuInformationTable.setStatus("current")
_Gepoel2esw12OnuInformationEntry_Object = MibTableRow
gepoel2esw12OnuInformationEntry = _Gepoel2esw12OnuInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1)
)
gepoel2esw12OnuInformationEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuInfoOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuInfoMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuInformationEntry.setStatus("current")


class _Gepoel2esw12OnuInfoOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuInfoOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuInfoOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuInfoOltPort_Object = MibTableColumn
gepoel2esw12OnuInfoOltPort = _Gepoel2esw12OnuInfoOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 1),
    _Gepoel2esw12OnuInfoOltPort_Type()
)
gepoel2esw12OnuInfoOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuInfoOltPort.setStatus("current")
_Gepoel2esw12OnuInfoMacAddress_Type = MacAddress
_Gepoel2esw12OnuInfoMacAddress_Object = MibTableColumn
gepoel2esw12OnuInfoMacAddress = _Gepoel2esw12OnuInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 2),
    _Gepoel2esw12OnuInfoMacAddress_Type()
)
gepoel2esw12OnuInfoMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuInfoMacAddress.setStatus("current")
_Gepoel2esw12OnuModelName_Type = DisplayString
_Gepoel2esw12OnuModelName_Object = MibTableColumn
gepoel2esw12OnuModelName = _Gepoel2esw12OnuModelName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 3),
    _Gepoel2esw12OnuModelName_Type()
)
gepoel2esw12OnuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuModelName.setStatus("current")
_Gepoel2esw12OnuSerialNumber_Type = DisplayString
_Gepoel2esw12OnuSerialNumber_Object = MibTableColumn
gepoel2esw12OnuSerialNumber = _Gepoel2esw12OnuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 4),
    _Gepoel2esw12OnuSerialNumber_Type()
)
gepoel2esw12OnuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuSerialNumber.setStatus("current")
_Gepoel2esw12OnuOutputOpticalWavelength_Type = DisplayString
_Gepoel2esw12OnuOutputOpticalWavelength_Object = MibTableColumn
gepoel2esw12OnuOutputOpticalWavelength = _Gepoel2esw12OnuOutputOpticalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 5),
    _Gepoel2esw12OnuOutputOpticalWavelength_Type()
)
gepoel2esw12OnuOutputOpticalWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuOutputOpticalWavelength.setStatus("current")
_Gepoel2esw12OnuFirmwaveVersion_Type = DisplayString
_Gepoel2esw12OnuFirmwaveVersion_Object = MibTableColumn
gepoel2esw12OnuFirmwaveVersion = _Gepoel2esw12OnuFirmwaveVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 6),
    _Gepoel2esw12OnuFirmwaveVersion_Type()
)
gepoel2esw12OnuFirmwaveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFirmwaveVersion.setStatus("current")
_Gepoel2esw12OnuBootCodeVersion_Type = DisplayString
_Gepoel2esw12OnuBootCodeVersion_Object = MibTableColumn
gepoel2esw12OnuBootCodeVersion = _Gepoel2esw12OnuBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 7),
    _Gepoel2esw12OnuBootCodeVersion_Type()
)
gepoel2esw12OnuBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBootCodeVersion.setStatus("current")
_Gepoel2esw12OnuPersonalityVersion_Type = DisplayString
_Gepoel2esw12OnuPersonalityVersion_Object = MibTableColumn
gepoel2esw12OnuPersonalityVersion = _Gepoel2esw12OnuPersonalityVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 8),
    _Gepoel2esw12OnuPersonalityVersion_Type()
)
gepoel2esw12OnuPersonalityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPersonalityVersion.setStatus("current")
_Gepoel2esw12OnuApp0Version_Type = DisplayString
_Gepoel2esw12OnuApp0Version_Object = MibTableColumn
gepoel2esw12OnuApp0Version = _Gepoel2esw12OnuApp0Version_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 9),
    _Gepoel2esw12OnuApp0Version_Type()
)
gepoel2esw12OnuApp0Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuApp0Version.setStatus("current")
_Gepoel2esw12OnuApp1Version_Type = DisplayString
_Gepoel2esw12OnuApp1Version_Object = MibTableColumn
gepoel2esw12OnuApp1Version = _Gepoel2esw12OnuApp1Version_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 2, 1, 10),
    _Gepoel2esw12OnuApp1Version_Type()
)
gepoel2esw12OnuApp1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuApp1Version.setStatus("current")
_Gepoel2esw12OnuTrafficManagement_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuTrafficManagement = _Gepoel2esw12OnuTrafficManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3)
)
_Gepoel2esw12OnuQueueConfig_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuQueueConfig = _Gepoel2esw12OnuQueueConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1)
)
_Gepoel2esw12OnuUpstreamQueueConfigTable_Object = MibTable
gepoel2esw12OnuUpstreamQueueConfigTable = _Gepoel2esw12OnuUpstreamQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueConfigTable.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueConfigEntry_Object = MibTableRow
gepoel2esw12OnuUpstreamQueueConfigEntry = _Gepoel2esw12OnuUpstreamQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1, 1)
)
gepoel2esw12OnuUpstreamQueueConfigEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuUpstreamQueueOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuUpstreamMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuUpstreamConfigIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueConfigEntry.setStatus("current")


class _Gepoel2esw12OnuUpstreamQueueOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuUpstreamQueueOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuUpstreamQueueOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuUpstreamQueueOltPort_Object = MibTableColumn
gepoel2esw12OnuUpstreamQueueOltPort = _Gepoel2esw12OnuUpstreamQueueOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1, 1, 1),
    _Gepoel2esw12OnuUpstreamQueueOltPort_Type()
)
gepoel2esw12OnuUpstreamQueueOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueOltPort.setStatus("current")
_Gepoel2esw12OnuUpstreamMacAddress_Type = MacAddress
_Gepoel2esw12OnuUpstreamMacAddress_Object = MibTableColumn
gepoel2esw12OnuUpstreamMacAddress = _Gepoel2esw12OnuUpstreamMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1, 1, 2),
    _Gepoel2esw12OnuUpstreamMacAddress_Type()
)
gepoel2esw12OnuUpstreamMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamMacAddress.setStatus("current")


class _Gepoel2esw12OnuUpstreamConfigIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuUpstreamConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Gepoel2esw12OnuUpstreamConfigIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuUpstreamConfigIndex_Object = MibTableColumn
gepoel2esw12OnuUpstreamConfigIndex = _Gepoel2esw12OnuUpstreamConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1, 1, 3),
    _Gepoel2esw12OnuUpstreamConfigIndex_Type()
)
gepoel2esw12OnuUpstreamConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamConfigIndex.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueSize_Type = DisplayString
_Gepoel2esw12OnuUpstreamQueueSize_Object = MibTableColumn
gepoel2esw12OnuUpstreamQueueSize = _Gepoel2esw12OnuUpstreamQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1, 1, 4),
    _Gepoel2esw12OnuUpstreamQueueSize_Type()
)
gepoel2esw12OnuUpstreamQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueSize.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueSizeDoModify_Type = DisplayString
_Gepoel2esw12OnuUpstreamQueueSizeDoModify_Object = MibTableColumn
gepoel2esw12OnuUpstreamQueueSizeDoModify = _Gepoel2esw12OnuUpstreamQueueSizeDoModify_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 1, 1, 5),
    _Gepoel2esw12OnuUpstreamQueueSizeDoModify_Type()
)
gepoel2esw12OnuUpstreamQueueSizeDoModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueSizeDoModify.setStatus("current")
_Gepoel2esw12OnuDownstreamQueueConfigTable_Object = MibTable
gepoel2esw12OnuDownstreamQueueConfigTable = _Gepoel2esw12OnuDownstreamQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamQueueConfigTable.setStatus("current")
_Gepoel2esw12OnuDownstreamQueueConfigEntry_Object = MibTableRow
gepoel2esw12OnuDownstreamQueueConfigEntry = _Gepoel2esw12OnuDownstreamQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2, 1)
)
gepoel2esw12OnuDownstreamQueueConfigEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDownstreamQueueConfigOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDownstreamMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDownstreamPort"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamQueueConfigEntry.setStatus("current")


class _Gepoel2esw12OnuDownstreamQueueConfigOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuDownstreamQueueConfigOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuDownstreamQueueConfigOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuDownstreamQueueConfigOltPort_Object = MibTableColumn
gepoel2esw12OnuDownstreamQueueConfigOltPort = _Gepoel2esw12OnuDownstreamQueueConfigOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2, 1, 1),
    _Gepoel2esw12OnuDownstreamQueueConfigOltPort_Type()
)
gepoel2esw12OnuDownstreamQueueConfigOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamQueueConfigOltPort.setStatus("current")
_Gepoel2esw12OnuDownstreamMacAddress_Type = MacAddress
_Gepoel2esw12OnuDownstreamMacAddress_Object = MibTableColumn
gepoel2esw12OnuDownstreamMacAddress = _Gepoel2esw12OnuDownstreamMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2, 1, 2),
    _Gepoel2esw12OnuDownstreamMacAddress_Type()
)
gepoel2esw12OnuDownstreamMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamMacAddress.setStatus("current")


class _Gepoel2esw12OnuDownstreamPort_Type(Integer32):
    """Custom type gepoel2esw12OnuDownstreamPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuDownstreamPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuDownstreamPort_Object = MibTableColumn
gepoel2esw12OnuDownstreamPort = _Gepoel2esw12OnuDownstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2, 1, 3),
    _Gepoel2esw12OnuDownstreamPort_Type()
)
gepoel2esw12OnuDownstreamPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamPort.setStatus("current")
_Gepoel2esw12OnuDownstreamQueueSize_Type = DisplayString
_Gepoel2esw12OnuDownstreamQueueSize_Object = MibTableColumn
gepoel2esw12OnuDownstreamQueueSize = _Gepoel2esw12OnuDownstreamQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2, 1, 4),
    _Gepoel2esw12OnuDownstreamQueueSize_Type()
)
gepoel2esw12OnuDownstreamQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamQueueSize.setStatus("current")
_Gepoel2esw12OnuDownstreamQueueSizeDoModify_Type = DisplayString
_Gepoel2esw12OnuDownstreamQueueSizeDoModify_Object = MibTableColumn
gepoel2esw12OnuDownstreamQueueSizeDoModify = _Gepoel2esw12OnuDownstreamQueueSizeDoModify_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 2, 1, 5),
    _Gepoel2esw12OnuDownstreamQueueSizeDoModify_Type()
)
gepoel2esw12OnuDownstreamQueueSizeDoModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDownstreamQueueSizeDoModify.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueConfigAdd_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuUpstreamQueueConfigAdd = _Gepoel2esw12OnuUpstreamQueueConfigAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 3)
)


class _Gepoel2esw12OnuUpstreamQueueAddOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuUpstreamQueueAddOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuUpstreamQueueAddOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuUpstreamQueueAddOltPort_Object = MibScalar
gepoel2esw12OnuUpstreamQueueAddOltPort = _Gepoel2esw12OnuUpstreamQueueAddOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 3, 1),
    _Gepoel2esw12OnuUpstreamQueueAddOltPort_Type()
)
gepoel2esw12OnuUpstreamQueueAddOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueAddOltPort.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueAddMacAddress_Type = MacAddress
_Gepoel2esw12OnuUpstreamQueueAddMacAddress_Object = MibScalar
gepoel2esw12OnuUpstreamQueueAddMacAddress = _Gepoel2esw12OnuUpstreamQueueAddMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 3, 2),
    _Gepoel2esw12OnuUpstreamQueueAddMacAddress_Type()
)
gepoel2esw12OnuUpstreamQueueAddMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueAddMacAddress.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueAddSize_Type = DisplayString
_Gepoel2esw12OnuUpstreamQueueAddSize_Object = MibScalar
gepoel2esw12OnuUpstreamQueueAddSize = _Gepoel2esw12OnuUpstreamQueueAddSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 3, 3),
    _Gepoel2esw12OnuUpstreamQueueAddSize_Type()
)
gepoel2esw12OnuUpstreamQueueAddSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueAddSize.setStatus("current")


class _Gepoel2esw12OnuUpstreamQueueAdd_Type(Integer32):
    """Custom type gepoel2esw12OnuUpstreamQueueAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuUpstreamQueueAdd_Type.__name__ = "Integer32"
_Gepoel2esw12OnuUpstreamQueueAdd_Object = MibScalar
gepoel2esw12OnuUpstreamQueueAdd = _Gepoel2esw12OnuUpstreamQueueAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 3, 4),
    _Gepoel2esw12OnuUpstreamQueueAdd_Type()
)
gepoel2esw12OnuUpstreamQueueAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueAdd.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueConfigDel_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuUpstreamQueueConfigDel = _Gepoel2esw12OnuUpstreamQueueConfigDel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 4)
)


class _Gepoel2esw12OnuUpstreamQueueDelConfigOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuUpstreamQueueDelConfigOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuUpstreamQueueDelConfigOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuUpstreamQueueDelConfigOltPort_Object = MibScalar
gepoel2esw12OnuUpstreamQueueDelConfigOltPort = _Gepoel2esw12OnuUpstreamQueueDelConfigOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 4, 1),
    _Gepoel2esw12OnuUpstreamQueueDelConfigOltPort_Type()
)
gepoel2esw12OnuUpstreamQueueDelConfigOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueDelConfigOltPort.setStatus("current")
_Gepoel2esw12OnuUpstreamQueueDelMacAddress_Type = MacAddress
_Gepoel2esw12OnuUpstreamQueueDelMacAddress_Object = MibScalar
gepoel2esw12OnuUpstreamQueueDelMacAddress = _Gepoel2esw12OnuUpstreamQueueDelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 4, 2),
    _Gepoel2esw12OnuUpstreamQueueDelMacAddress_Type()
)
gepoel2esw12OnuUpstreamQueueDelMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueDelMacAddress.setStatus("current")


class _Gepoel2esw12OnuUpstreamQueueDel_Type(Integer32):
    """Custom type gepoel2esw12OnuUpstreamQueueDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuUpstreamQueueDel_Type.__name__ = "Integer32"
_Gepoel2esw12OnuUpstreamQueueDel_Object = MibScalar
gepoel2esw12OnuUpstreamQueueDel = _Gepoel2esw12OnuUpstreamQueueDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 1, 4, 3),
    _Gepoel2esw12OnuUpstreamQueueDel_Type()
)
gepoel2esw12OnuUpstreamQueueDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuUpstreamQueueDel.setStatus("current")
_Gepoel2esw12OnuFieldSelectTable_Object = MibTable
gepoel2esw12OnuFieldSelectTable = _Gepoel2esw12OnuFieldSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldSelectTable.setStatus("current")
_Gepoel2esw12OnuFieldSelectEntry_Object = MibTableRow
gepoel2esw12OnuFieldSelectEntry = _Gepoel2esw12OnuFieldSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1)
)
gepoel2esw12OnuFieldSelectEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuFieldSelectOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuFieldIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldSelectEntry.setStatus("current")


class _Gepoel2esw12OnuFieldSelectOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuFieldSelectOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuFieldSelectOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuFieldSelectOltPort_Object = MibTableColumn
gepoel2esw12OnuFieldSelectOltPort = _Gepoel2esw12OnuFieldSelectOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 1),
    _Gepoel2esw12OnuFieldSelectOltPort_Type()
)
gepoel2esw12OnuFieldSelectOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldSelectOltPort.setStatus("current")
_Gepoel2esw12OnuMacAddress_Type = MacAddress
_Gepoel2esw12OnuMacAddress_Object = MibTableColumn
gepoel2esw12OnuMacAddress = _Gepoel2esw12OnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 2),
    _Gepoel2esw12OnuMacAddress_Type()
)
gepoel2esw12OnuMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMacAddress.setStatus("current")


class _Gepoel2esw12OnuPort_Type(Integer32):
    """Custom type gepoel2esw12OnuPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gepoel2esw12OnuPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPort_Object = MibTableColumn
gepoel2esw12OnuPort = _Gepoel2esw12OnuPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 3),
    _Gepoel2esw12OnuPort_Type()
)
gepoel2esw12OnuPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPort.setStatus("current")


class _Gepoel2esw12OnuFieldIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuFieldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_Gepoel2esw12OnuFieldIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuFieldIndex_Object = MibTableColumn
gepoel2esw12OnuFieldIndex = _Gepoel2esw12OnuFieldIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 4),
    _Gepoel2esw12OnuFieldIndex_Type()
)
gepoel2esw12OnuFieldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldIndex.setStatus("current")
_Gepoel2esw12OnuFieldName_Type = DisplayString
_Gepoel2esw12OnuFieldName_Object = MibTableColumn
gepoel2esw12OnuFieldName = _Gepoel2esw12OnuFieldName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 5),
    _Gepoel2esw12OnuFieldName_Type()
)
gepoel2esw12OnuFieldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldName.setStatus("current")


class _Gepoel2esw12OnuRefCount_Type(Integer32):
    """Custom type gepoel2esw12OnuRefCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gepoel2esw12OnuRefCount_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRefCount_Object = MibTableColumn
gepoel2esw12OnuRefCount = _Gepoel2esw12OnuRefCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 6),
    _Gepoel2esw12OnuRefCount_Type()
)
gepoel2esw12OnuRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRefCount.setStatus("current")


class _Gepoel2esw12OnuLayerSel_Type(Integer32):
    """Custom type gepoel2esw12OnuLayerSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12OnuLayerSel_Type.__name__ = "Integer32"
_Gepoel2esw12OnuLayerSel_Object = MibTableColumn
gepoel2esw12OnuLayerSel = _Gepoel2esw12OnuLayerSel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 7),
    _Gepoel2esw12OnuLayerSel_Type()
)
gepoel2esw12OnuLayerSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuLayerSel.setStatus("current")


class _Gepoel2esw12OnuDWord_Type(Integer32):
    """Custom type gepoel2esw12OnuDWord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gepoel2esw12OnuDWord_Type.__name__ = "Integer32"
_Gepoel2esw12OnuDWord_Object = MibTableColumn
gepoel2esw12OnuDWord = _Gepoel2esw12OnuDWord_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 8),
    _Gepoel2esw12OnuDWord_Type()
)
gepoel2esw12OnuDWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDWord.setStatus("current")


class _Gepoel2esw12OnuBitOffset_Type(Integer32):
    """Custom type gepoel2esw12OnuBitOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Gepoel2esw12OnuBitOffset_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBitOffset_Object = MibTableColumn
gepoel2esw12OnuBitOffset = _Gepoel2esw12OnuBitOffset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 9),
    _Gepoel2esw12OnuBitOffset_Type()
)
gepoel2esw12OnuBitOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBitOffset.setStatus("current")


class _Gepoel2esw12OnuFieldWidth_Type(Integer32):
    """Custom type gepoel2esw12OnuFieldWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Gepoel2esw12OnuFieldWidth_Type.__name__ = "Integer32"
_Gepoel2esw12OnuFieldWidth_Object = MibTableColumn
gepoel2esw12OnuFieldWidth = _Gepoel2esw12OnuFieldWidth_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 10),
    _Gepoel2esw12OnuFieldWidth_Type()
)
gepoel2esw12OnuFieldWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldWidth.setStatus("current")


class _Gepoel2esw12OnuFieldModify_Type(Integer32):
    """Custom type gepoel2esw12OnuFieldModify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 37),
    )


_Gepoel2esw12OnuFieldModify_Type.__name__ = "Integer32"
_Gepoel2esw12OnuFieldModify_Object = MibTableColumn
gepoel2esw12OnuFieldModify = _Gepoel2esw12OnuFieldModify_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 11),
    _Gepoel2esw12OnuFieldModify_Type()
)
gepoel2esw12OnuFieldModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldModify.setStatus("current")


class _Gepoel2esw12OnuFieldClear_Type(Integer32):
    """Custom type gepoel2esw12OnuFieldClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuFieldClear_Type.__name__ = "Integer32"
_Gepoel2esw12OnuFieldClear_Object = MibScalar
gepoel2esw12OnuFieldClear = _Gepoel2esw12OnuFieldClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 2, 1, 12),
    _Gepoel2esw12OnuFieldClear_Type()
)
gepoel2esw12OnuFieldClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuFieldClear.setStatus("current")
_Gepoel2esw12OnuRule_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuRule = _Gepoel2esw12OnuRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3)
)
_Gepoel2esw12OnuRuleNumberTable_Object = MibTable
gepoel2esw12OnuRuleNumberTable = _Gepoel2esw12OnuRuleNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleNumberTable.setStatus("current")
_Gepoel2esw12OnuRuleNumberEntry_Object = MibTableRow
gepoel2esw12OnuRuleNumberEntry = _Gepoel2esw12OnuRuleNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 1, 1)
)
gepoel2esw12OnuRuleNumberEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleNumberOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleNumberMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleNumberPort"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleNumberEntry.setStatus("current")


class _Gepoel2esw12OnuRuleNumberOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleNumberOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuRuleNumberOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleNumberOltPort_Object = MibTableColumn
gepoel2esw12OnuRuleNumberOltPort = _Gepoel2esw12OnuRuleNumberOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 1, 1, 1),
    _Gepoel2esw12OnuRuleNumberOltPort_Type()
)
gepoel2esw12OnuRuleNumberOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleNumberOltPort.setStatus("current")
_Gepoel2esw12OnuRuleNumberMacAddress_Type = MacAddress
_Gepoel2esw12OnuRuleNumberMacAddress_Object = MibTableColumn
gepoel2esw12OnuRuleNumberMacAddress = _Gepoel2esw12OnuRuleNumberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 1, 1, 2),
    _Gepoel2esw12OnuRuleNumberMacAddress_Type()
)
gepoel2esw12OnuRuleNumberMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleNumberMacAddress.setStatus("current")


class _Gepoel2esw12OnuRuleNumberPort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleNumberPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gepoel2esw12OnuRuleNumberPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleNumberPort_Object = MibTableColumn
gepoel2esw12OnuRuleNumberPort = _Gepoel2esw12OnuRuleNumberPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 1, 1, 3),
    _Gepoel2esw12OnuRuleNumberPort_Type()
)
gepoel2esw12OnuRuleNumberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleNumberPort.setStatus("current")


class _Gepoel2esw12OnuRuleNumber_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_Gepoel2esw12OnuRuleNumber_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleNumber_Object = MibTableColumn
gepoel2esw12OnuRuleNumber = _Gepoel2esw12OnuRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 1, 1, 4),
    _Gepoel2esw12OnuRuleNumber_Type()
)
gepoel2esw12OnuRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleNumber.setStatus("current")
_Gepoel2esw12OnuRuleClauseNumberTable_Object = MibTable
gepoel2esw12OnuRuleClauseNumberTable = _Gepoel2esw12OnuRuleClauseNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClauseNumberTable.setStatus("current")
_Gepoel2esw12OnuRuleClauseNumberEntry_Object = MibTableRow
gepoel2esw12OnuRuleClauseNumberEntry = _Gepoel2esw12OnuRuleClauseNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2, 1)
)
gepoel2esw12OnuRuleClauseNumberEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleClauseNumberOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleClauseMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleClausePort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleClauseNumberIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClauseNumberEntry.setStatus("current")


class _Gepoel2esw12OnuRuleClauseNumberOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleClauseNumberOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuRuleClauseNumberOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleClauseNumberOltPort_Object = MibTableColumn
gepoel2esw12OnuRuleClauseNumberOltPort = _Gepoel2esw12OnuRuleClauseNumberOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2, 1, 1),
    _Gepoel2esw12OnuRuleClauseNumberOltPort_Type()
)
gepoel2esw12OnuRuleClauseNumberOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClauseNumberOltPort.setStatus("current")
_Gepoel2esw12OnuRuleClauseMacAddress_Type = MacAddress
_Gepoel2esw12OnuRuleClauseMacAddress_Object = MibTableColumn
gepoel2esw12OnuRuleClauseMacAddress = _Gepoel2esw12OnuRuleClauseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2, 1, 2),
    _Gepoel2esw12OnuRuleClauseMacAddress_Type()
)
gepoel2esw12OnuRuleClauseMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClauseMacAddress.setStatus("current")


class _Gepoel2esw12OnuRuleClausePort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleClausePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gepoel2esw12OnuRuleClausePort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleClausePort_Object = MibTableColumn
gepoel2esw12OnuRuleClausePort = _Gepoel2esw12OnuRuleClausePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2, 1, 3),
    _Gepoel2esw12OnuRuleClausePort_Type()
)
gepoel2esw12OnuRuleClausePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClausePort.setStatus("current")


class _Gepoel2esw12OnuRuleClauseNumberIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleClauseNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_Gepoel2esw12OnuRuleClauseNumberIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleClauseNumberIndex_Object = MibTableColumn
gepoel2esw12OnuRuleClauseNumberIndex = _Gepoel2esw12OnuRuleClauseNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2, 1, 4),
    _Gepoel2esw12OnuRuleClauseNumberIndex_Type()
)
gepoel2esw12OnuRuleClauseNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClauseNumberIndex.setStatus("current")


class _Gepoel2esw12OnuRuleClauseNumber_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleClauseNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Gepoel2esw12OnuRuleClauseNumber_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleClauseNumber_Object = MibTableColumn
gepoel2esw12OnuRuleClauseNumber = _Gepoel2esw12OnuRuleClauseNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 2, 1, 5),
    _Gepoel2esw12OnuRuleClauseNumber_Type()
)
gepoel2esw12OnuRuleClauseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleClauseNumber.setStatus("current")
_Gepoel2esw12OnuRuleTable_Object = MibTable
gepoel2esw12OnuRuleTable = _Gepoel2esw12OnuRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleTable.setStatus("current")
_Gepoel2esw12OnuRuleEntry_Object = MibTableRow
gepoel2esw12OnuRuleEntry = _Gepoel2esw12OnuRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1)
)
gepoel2esw12OnuRuleEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRuleMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuRulePort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuPortRuleIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleEntry.setStatus("current")


class _Gepoel2esw12OnuRuleOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuRuleOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleOltPort_Object = MibTableColumn
gepoel2esw12OnuRuleOltPort = _Gepoel2esw12OnuRuleOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 1),
    _Gepoel2esw12OnuRuleOltPort_Type()
)
gepoel2esw12OnuRuleOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleOltPort.setStatus("current")
_Gepoel2esw12OnuRuleMacAddress_Type = MacAddress
_Gepoel2esw12OnuRuleMacAddress_Object = MibTableColumn
gepoel2esw12OnuRuleMacAddress = _Gepoel2esw12OnuRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 2),
    _Gepoel2esw12OnuRuleMacAddress_Type()
)
gepoel2esw12OnuRuleMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleMacAddress.setStatus("current")


class _Gepoel2esw12OnuRulePort_Type(Integer32):
    """Custom type gepoel2esw12OnuRulePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gepoel2esw12OnuRulePort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRulePort_Object = MibTableColumn
gepoel2esw12OnuRulePort = _Gepoel2esw12OnuRulePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 3),
    _Gepoel2esw12OnuRulePort_Type()
)
gepoel2esw12OnuRulePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRulePort.setStatus("current")


class _Gepoel2esw12OnuPortRuleIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_Gepoel2esw12OnuPortRuleIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleIndex_Object = MibTableColumn
gepoel2esw12OnuPortRuleIndex = _Gepoel2esw12OnuPortRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 4),
    _Gepoel2esw12OnuPortRuleIndex_Type()
)
gepoel2esw12OnuPortRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleIndex.setStatus("current")


class _Gepoel2esw12OnuPortRuleDelete_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuPortRuleDelete_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleDelete_Object = MibTableColumn
gepoel2esw12OnuPortRuleDelete = _Gepoel2esw12OnuPortRuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 5),
    _Gepoel2esw12OnuPortRuleDelete_Type()
)
gepoel2esw12OnuPortRuleDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleDelete.setStatus("current")
_Gepoel2esw12OnuPortRuleAction_Type = DisplayString
_Gepoel2esw12OnuPortRuleAction_Object = MibTableColumn
gepoel2esw12OnuPortRuleAction = _Gepoel2esw12OnuPortRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 6),
    _Gepoel2esw12OnuPortRuleAction_Type()
)
gepoel2esw12OnuPortRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAction.setStatus("current")
_Gepoel2esw12OnuPortRuleClauses_Type = DisplayString
_Gepoel2esw12OnuPortRuleClauses_Object = MibTableColumn
gepoel2esw12OnuPortRuleClauses = _Gepoel2esw12OnuPortRuleClauses_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 7),
    _Gepoel2esw12OnuPortRuleClauses_Type()
)
gepoel2esw12OnuPortRuleClauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleClauses.setStatus("current")
_Gepoel2esw12OnuPortRuleNextClauses_Type = DisplayString
_Gepoel2esw12OnuPortRuleNextClauses_Object = MibTableColumn
gepoel2esw12OnuPortRuleNextClauses = _Gepoel2esw12OnuPortRuleNextClauses_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 3, 1, 8),
    _Gepoel2esw12OnuPortRuleNextClauses_Type()
)
gepoel2esw12OnuPortRuleNextClauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleNextClauses.setStatus("current")
_Gepoel2esw12OnuRuleAdd_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuRuleAdd = _Gepoel2esw12OnuRuleAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4)
)


class _Gepoel2esw12OnuRuleAddOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleAddOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuRuleAddOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleAddOltPort_Object = MibScalar
gepoel2esw12OnuRuleAddOltPort = _Gepoel2esw12OnuRuleAddOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 1),
    _Gepoel2esw12OnuRuleAddOltPort_Type()
)
gepoel2esw12OnuRuleAddOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleAddOltPort.setStatus("current")
_Gepoel2esw12OnuRuleAddMacAddress_Type = MacAddress
_Gepoel2esw12OnuRuleAddMacAddress_Object = MibScalar
gepoel2esw12OnuRuleAddMacAddress = _Gepoel2esw12OnuRuleAddMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 2),
    _Gepoel2esw12OnuRuleAddMacAddress_Type()
)
gepoel2esw12OnuRuleAddMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleAddMacAddress.setStatus("current")


class _Gepoel2esw12OnuRuleAddPort_Type(Integer32):
    """Custom type gepoel2esw12OnuRuleAddPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gepoel2esw12OnuRuleAddPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRuleAddPort_Object = MibScalar
gepoel2esw12OnuRuleAddPort = _Gepoel2esw12OnuRuleAddPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 3),
    _Gepoel2esw12OnuRuleAddPort_Type()
)
gepoel2esw12OnuRuleAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRuleAddPort.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddPriority_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 13),
    )


_Gepoel2esw12OnuPortRuleAddPriority_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddPriority_Object = MibScalar
gepoel2esw12OnuPortRuleAddPriority = _Gepoel2esw12OnuPortRuleAddPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 4),
    _Gepoel2esw12OnuPortRuleAddPriority_Type()
)
gepoel2esw12OnuPortRuleAddPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddPriority.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddAction_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_Gepoel2esw12OnuPortRuleAddAction_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddAction_Object = MibScalar
gepoel2esw12OnuPortRuleAddAction = _Gepoel2esw12OnuPortRuleAddAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 5),
    _Gepoel2esw12OnuPortRuleAddAction_Type()
)
gepoel2esw12OnuPortRuleAddAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddAction.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddActionPort_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddActionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gepoel2esw12OnuPortRuleAddActionPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddActionPort_Object = MibScalar
gepoel2esw12OnuPortRuleAddActionPort = _Gepoel2esw12OnuPortRuleAddActionPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 6),
    _Gepoel2esw12OnuPortRuleAddActionPort_Type()
)
gepoel2esw12OnuPortRuleAddActionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddActionPort.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddActionQueue_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddActionQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_Gepoel2esw12OnuPortRuleAddActionQueue_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddActionQueue_Object = MibScalar
gepoel2esw12OnuPortRuleAddActionQueue = _Gepoel2esw12OnuPortRuleAddActionQueue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 7),
    _Gepoel2esw12OnuPortRuleAddActionQueue_Type()
)
gepoel2esw12OnuPortRuleAddActionQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddActionQueue.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddClauseNum_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddClauseNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gepoel2esw12OnuPortRuleAddClauseNum_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddClauseNum_Object = MibScalar
gepoel2esw12OnuPortRuleAddClauseNum = _Gepoel2esw12OnuPortRuleAddClauseNum_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 8),
    _Gepoel2esw12OnuPortRuleAddClauseNum_Type()
)
gepoel2esw12OnuPortRuleAddClauseNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddClauseNum.setStatus("current")
_Gepoel2esw12OnuPortRuleAddClauseTable_Object = MibTable
gepoel2esw12OnuPortRuleAddClauseTable = _Gepoel2esw12OnuPortRuleAddClauseTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddClauseTable.setStatus("current")
_Gepoel2esw12OnuPortRuleAddClauseEntry_Object = MibTableRow
gepoel2esw12OnuPortRuleAddClauseEntry = _Gepoel2esw12OnuPortRuleAddClauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9, 1)
)
gepoel2esw12OnuPortRuleAddClauseEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuPortRuleAddClauseIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddClauseEntry.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddClauseIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddClauseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Gepoel2esw12OnuPortRuleAddClauseIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddClauseIndex_Object = MibTableColumn
gepoel2esw12OnuPortRuleAddClauseIndex = _Gepoel2esw12OnuPortRuleAddClauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9, 1, 1),
    _Gepoel2esw12OnuPortRuleAddClauseIndex_Type()
)
gepoel2esw12OnuPortRuleAddClauseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddClauseIndex.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddField_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Gepoel2esw12OnuPortRuleAddField_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddField_Object = MibTableColumn
gepoel2esw12OnuPortRuleAddField = _Gepoel2esw12OnuPortRuleAddField_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9, 1, 2),
    _Gepoel2esw12OnuPortRuleAddField_Type()
)
gepoel2esw12OnuPortRuleAddField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddField.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddOperation_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12OnuPortRuleAddOperation_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddOperation_Object = MibTableColumn
gepoel2esw12OnuPortRuleAddOperation = _Gepoel2esw12OnuPortRuleAddOperation_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9, 1, 3),
    _Gepoel2esw12OnuPortRuleAddOperation_Type()
)
gepoel2esw12OnuPortRuleAddOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddOperation.setStatus("current")


class _Gepoel2esw12OnuPortRuleAddValueType_Type(Integer32):
    """Custom type gepoel2esw12OnuPortRuleAddValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuPortRuleAddValueType_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPortRuleAddValueType_Object = MibTableColumn
gepoel2esw12OnuPortRuleAddValueType = _Gepoel2esw12OnuPortRuleAddValueType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9, 1, 4),
    _Gepoel2esw12OnuPortRuleAddValueType_Type()
)
gepoel2esw12OnuPortRuleAddValueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddValueType.setStatus("current")
_Gepoel2esw12OnuPortRuleAddValue_Type = DisplayString
_Gepoel2esw12OnuPortRuleAddValue_Object = MibTableColumn
gepoel2esw12OnuPortRuleAddValue = _Gepoel2esw12OnuPortRuleAddValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 9, 1, 5),
    _Gepoel2esw12OnuPortRuleAddValue_Type()
)
gepoel2esw12OnuPortRuleAddValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPortRuleAddValue.setStatus("current")


class _Gepoel2esw12DoOnuRulerAdd_Type(Integer32):
    """Custom type gepoel2esw12DoOnuRulerAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DoOnuRulerAdd_Type.__name__ = "Integer32"
_Gepoel2esw12DoOnuRulerAdd_Object = MibScalar
gepoel2esw12DoOnuRulerAdd = _Gepoel2esw12DoOnuRulerAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 3, 3, 4, 10),
    _Gepoel2esw12DoOnuRulerAdd_Type()
)
gepoel2esw12DoOnuRulerAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DoOnuRulerAdd.setStatus("current")
_Gepoel2esw12OnuIGMP_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuIGMP = _Gepoel2esw12OnuIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4)
)
_Gepoel2esw12OnuIGMPSnoopingTable_Object = MibTable
gepoel2esw12OnuIGMPSnoopingTable = _Gepoel2esw12OnuIGMPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPSnoopingTable.setStatus("current")
_Gepoel2esw12OnuIGMPSnoopingEntry_Object = MibTableRow
gepoel2esw12OnuIGMPSnoopingEntry = _Gepoel2esw12OnuIGMPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1)
)
gepoel2esw12OnuIGMPSnoopingEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPSnoopingOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPSnoopingMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPSnoopingEntry.setStatus("current")


class _Gepoel2esw12OnuIGMPSnoopingOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPSnoopingOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuIGMPSnoopingOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPSnoopingOltPort_Object = MibTableColumn
gepoel2esw12OnuIGMPSnoopingOltPort = _Gepoel2esw12OnuIGMPSnoopingOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 1),
    _Gepoel2esw12OnuIGMPSnoopingOltPort_Type()
)
gepoel2esw12OnuIGMPSnoopingOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPSnoopingOltPort.setStatus("current")
_Gepoel2esw12OnuIGMPSnoopingMacAddress_Type = MacAddress
_Gepoel2esw12OnuIGMPSnoopingMacAddress_Object = MibTableColumn
gepoel2esw12OnuIGMPSnoopingMacAddress = _Gepoel2esw12OnuIGMPSnoopingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 2),
    _Gepoel2esw12OnuIGMPSnoopingMacAddress_Type()
)
gepoel2esw12OnuIGMPSnoopingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPSnoopingMacAddress.setStatus("current")


class _Gepoel2esw12OnuRobustnessCount_Type(Integer32):
    """Custom type gepoel2esw12OnuRobustnessCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gepoel2esw12OnuRobustnessCount_Type.__name__ = "Integer32"
_Gepoel2esw12OnuRobustnessCount_Object = MibTableColumn
gepoel2esw12OnuRobustnessCount = _Gepoel2esw12OnuRobustnessCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 3),
    _Gepoel2esw12OnuRobustnessCount_Type()
)
gepoel2esw12OnuRobustnessCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuRobustnessCount.setStatus("current")


class _Gepoel2esw12OnuLastMemberQuery_Type(Integer32):
    """Custom type gepoel2esw12OnuLastMemberQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gepoel2esw12OnuLastMemberQuery_Type.__name__ = "Integer32"
_Gepoel2esw12OnuLastMemberQuery_Object = MibTableColumn
gepoel2esw12OnuLastMemberQuery = _Gepoel2esw12OnuLastMemberQuery_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 4),
    _Gepoel2esw12OnuLastMemberQuery_Type()
)
gepoel2esw12OnuLastMemberQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuLastMemberQuery.setStatus("current")


class _Gepoel2esw12OnuPort1IGMPGroupNumber_Type(Integer32):
    """Custom type gepoel2esw12OnuPort1IGMPGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_Gepoel2esw12OnuPort1IGMPGroupNumber_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPort1IGMPGroupNumber_Object = MibTableColumn
gepoel2esw12OnuPort1IGMPGroupNumber = _Gepoel2esw12OnuPort1IGMPGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 5),
    _Gepoel2esw12OnuPort1IGMPGroupNumber_Type()
)
gepoel2esw12OnuPort1IGMPGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPort1IGMPGroupNumber.setStatus("current")


class _Gepoel2esw12OnuPort1QueueForClassification_Type(Integer32):
    """Custom type gepoel2esw12OnuPort1QueueForClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Gepoel2esw12OnuPort1QueueForClassification_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPort1QueueForClassification_Object = MibTableColumn
gepoel2esw12OnuPort1QueueForClassification = _Gepoel2esw12OnuPort1QueueForClassification_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 6),
    _Gepoel2esw12OnuPort1QueueForClassification_Type()
)
gepoel2esw12OnuPort1QueueForClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPort1QueueForClassification.setStatus("current")


class _Gepoel2esw12OnuPort2IGMPGroupNumber_Type(Integer32):
    """Custom type gepoel2esw12OnuPort2IGMPGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_Gepoel2esw12OnuPort2IGMPGroupNumber_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPort2IGMPGroupNumber_Object = MibTableColumn
gepoel2esw12OnuPort2IGMPGroupNumber = _Gepoel2esw12OnuPort2IGMPGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 7),
    _Gepoel2esw12OnuPort2IGMPGroupNumber_Type()
)
gepoel2esw12OnuPort2IGMPGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPort2IGMPGroupNumber.setStatus("current")


class _Gepoel2esw12OnuPort2QueueForClassification_Type(Integer32):
    """Custom type gepoel2esw12OnuPort2QueueForClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Gepoel2esw12OnuPort2QueueForClassification_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPort2QueueForClassification_Object = MibTableColumn
gepoel2esw12OnuPort2QueueForClassification = _Gepoel2esw12OnuPort2QueueForClassification_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 8),
    _Gepoel2esw12OnuPort2QueueForClassification_Type()
)
gepoel2esw12OnuPort2QueueForClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPort2QueueForClassification.setStatus("current")


class _Gepoel2esw12OnuIGMPForwardGroupByL2DA_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPForwardGroupByL2DA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuIGMPForwardGroupByL2DA_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPForwardGroupByL2DA_Object = MibTableColumn
gepoel2esw12OnuIGMPForwardGroupByL2DA = _Gepoel2esw12OnuIGMPForwardGroupByL2DA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 9),
    _Gepoel2esw12OnuIGMPForwardGroupByL2DA_Type()
)
gepoel2esw12OnuIGMPForwardGroupByL2DA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPForwardGroupByL2DA.setStatus("current")


class _Gepoel2esw12OnuIGMPForwardGroupByVID_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPForwardGroupByVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuIGMPForwardGroupByVID_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPForwardGroupByVID_Object = MibTableColumn
gepoel2esw12OnuIGMPForwardGroupByVID = _Gepoel2esw12OnuIGMPForwardGroupByVID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 10),
    _Gepoel2esw12OnuIGMPForwardGroupByVID_Type()
)
gepoel2esw12OnuIGMPForwardGroupByVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPForwardGroupByVID.setStatus("current")


class _Gepoel2esw12OnuIGMPForwardGroupByIPDA_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPForwardGroupByIPDA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuIGMPForwardGroupByIPDA_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPForwardGroupByIPDA_Object = MibTableColumn
gepoel2esw12OnuIGMPForwardGroupByIPDA = _Gepoel2esw12OnuIGMPForwardGroupByIPDA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 1, 1, 11),
    _Gepoel2esw12OnuIGMPForwardGroupByIPDA_Type()
)
gepoel2esw12OnuIGMPForwardGroupByIPDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPForwardGroupByIPDA.setStatus("current")
_Gepoel2esw12OnuIGMPVlanProvision_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuIGMPVlanProvision = _Gepoel2esw12OnuIGMPVlanProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2)
)
_Gepoel2esw12OnuIGMPVlanProvisionTable_Object = MibTable
gepoel2esw12OnuIGMPVlanProvisionTable = _Gepoel2esw12OnuIGMPVlanProvisionTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanProvisionTable.setStatus("current")
_Gepoel2esw12OnuIGMPVlanProvisionEntry_Object = MibTableRow
gepoel2esw12OnuIGMPVlanProvisionEntry = _Gepoel2esw12OnuIGMPVlanProvisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 1, 1)
)
gepoel2esw12OnuIGMPVlanProvisionEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPVlanProvisionOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPVlanProvisionMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanProvisionEntry.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanProvisionOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanProvisionOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuIGMPVlanProvisionOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanProvisionOltPort_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanProvisionOltPort = _Gepoel2esw12OnuIGMPVlanProvisionOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 1, 1, 1),
    _Gepoel2esw12OnuIGMPVlanProvisionOltPort_Type()
)
gepoel2esw12OnuIGMPVlanProvisionOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanProvisionOltPort.setStatus("current")
_Gepoel2esw12OnuIGMPVlanProvisionMacAddress_Type = MacAddress
_Gepoel2esw12OnuIGMPVlanProvisionMacAddress_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanProvisionMacAddress = _Gepoel2esw12OnuIGMPVlanProvisionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 1, 1, 2),
    _Gepoel2esw12OnuIGMPVlanProvisionMacAddress_Type()
)
gepoel2esw12OnuIGMPVlanProvisionMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanProvisionMacAddress.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup = _Gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 1, 1, 3),
    _Gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup_Type()
)
gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan = _Gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 1, 1, 4),
    _Gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan_Type()
)
gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan.setStatus("current")
_Gepoel2esw12OnuIGMPVlanTable_Object = MibTable
gepoel2esw12OnuIGMPVlanTable = _Gepoel2esw12OnuIGMPVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanTable.setStatus("current")
_Gepoel2esw12OnuIGMPVlanEntry_Object = MibTableRow
gepoel2esw12OnuIGMPVlanEntry = _Gepoel2esw12OnuIGMPVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1)
)
gepoel2esw12OnuIGMPVlanEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPVlanOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPVlanMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPVlanIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanEntry.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuIGMPVlanOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanOltPort_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanOltPort = _Gepoel2esw12OnuIGMPVlanOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 1),
    _Gepoel2esw12OnuIGMPVlanOltPort_Type()
)
gepoel2esw12OnuIGMPVlanOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanOltPort.setStatus("current")
_Gepoel2esw12OnuIGMPVlanMacAddress_Type = MacAddress
_Gepoel2esw12OnuIGMPVlanMacAddress_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanMacAddress = _Gepoel2esw12OnuIGMPVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 2),
    _Gepoel2esw12OnuIGMPVlanMacAddress_Type()
)
gepoel2esw12OnuIGMPVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanMacAddress.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gepoel2esw12OnuIGMPVlanIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanIndex_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanIndex = _Gepoel2esw12OnuIGMPVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 3),
    _Gepoel2esw12OnuIGMPVlanIndex_Type()
)
gepoel2esw12OnuIGMPVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanIndex.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanEponVlanID_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanEponVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gepoel2esw12OnuIGMPVlanEponVlanID_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanEponVlanID_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanEponVlanID = _Gepoel2esw12OnuIGMPVlanEponVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 4),
    _Gepoel2esw12OnuIGMPVlanEponVlanID_Type()
)
gepoel2esw12OnuIGMPVlanEponVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanEponVlanID.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanUserVlanID_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanUserVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gepoel2esw12OnuIGMPVlanUserVlanID_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanUserVlanID_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanUserVlanID = _Gepoel2esw12OnuIGMPVlanUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 5),
    _Gepoel2esw12OnuIGMPVlanUserVlanID_Type()
)
gepoel2esw12OnuIGMPVlanUserVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanUserVlanID.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanMaxAllowedGroup_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanMaxAllowedGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gepoel2esw12OnuIGMPVlanMaxAllowedGroup_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanMaxAllowedGroup_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanMaxAllowedGroup = _Gepoel2esw12OnuIGMPVlanMaxAllowedGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 6),
    _Gepoel2esw12OnuIGMPVlanMaxAllowedGroup_Type()
)
gepoel2esw12OnuIGMPVlanMaxAllowedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanMaxAllowedGroup.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanDel_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuIGMPVlanDel_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanDel_Object = MibTableColumn
gepoel2esw12OnuIGMPVlanDel = _Gepoel2esw12OnuIGMPVlanDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 2, 1, 7),
    _Gepoel2esw12OnuIGMPVlanDel_Type()
)
gepoel2esw12OnuIGMPVlanDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanDel.setStatus("current")
_Gepoel2esw12OnuIGMPVlanAdd_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuIGMPVlanAdd = _Gepoel2esw12OnuIGMPVlanAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3)
)


class _Gepoel2esw12OnuIGMPVlanAddOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanAddOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuIGMPVlanAddOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanAddOltPort_Object = MibScalar
gepoel2esw12OnuIGMPVlanAddOltPort = _Gepoel2esw12OnuIGMPVlanAddOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3, 1),
    _Gepoel2esw12OnuIGMPVlanAddOltPort_Type()
)
gepoel2esw12OnuIGMPVlanAddOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanAddOltPort.setStatus("current")
_Gepoel2esw12OnuIGMPVlanAddMacAddress_Type = MacAddress
_Gepoel2esw12OnuIGMPVlanAddMacAddress_Object = MibScalar
gepoel2esw12OnuIGMPVlanAddMacAddress = _Gepoel2esw12OnuIGMPVlanAddMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3, 2),
    _Gepoel2esw12OnuIGMPVlanAddMacAddress_Type()
)
gepoel2esw12OnuIGMPVlanAddMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanAddMacAddress.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanAddEponVlanID_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanAddEponVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gepoel2esw12OnuIGMPVlanAddEponVlanID_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanAddEponVlanID_Object = MibScalar
gepoel2esw12OnuIGMPVlanAddEponVlanID = _Gepoel2esw12OnuIGMPVlanAddEponVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3, 3),
    _Gepoel2esw12OnuIGMPVlanAddEponVlanID_Type()
)
gepoel2esw12OnuIGMPVlanAddEponVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanAddEponVlanID.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanAddUserVlanID_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanAddUserVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gepoel2esw12OnuIGMPVlanAddUserVlanID_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanAddUserVlanID_Object = MibScalar
gepoel2esw12OnuIGMPVlanAddUserVlanID = _Gepoel2esw12OnuIGMPVlanAddUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3, 4),
    _Gepoel2esw12OnuIGMPVlanAddUserVlanID_Type()
)
gepoel2esw12OnuIGMPVlanAddUserVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanAddUserVlanID.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup_Object = MibScalar
gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup = _Gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3, 5),
    _Gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup_Type()
)
gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup.setStatus("current")


class _Gepoel2esw12OnuIGMPVlanAddDo_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPVlanAddDo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuIGMPVlanAddDo_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPVlanAddDo_Object = MibScalar
gepoel2esw12OnuIGMPVlanAddDo = _Gepoel2esw12OnuIGMPVlanAddDo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 2, 3, 6),
    _Gepoel2esw12OnuIGMPVlanAddDo_Type()
)
gepoel2esw12OnuIGMPVlanAddDo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPVlanAddDo.setStatus("current")
_Gepoel2esw12OnuIGMPGroup_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuIGMPGroup = _Gepoel2esw12OnuIGMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3)
)
_Gepoel2esw12OnuIGMPGroupTable_Object = MibTable
gepoel2esw12OnuIGMPGroupTable = _Gepoel2esw12OnuIGMPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupTable.setStatus("current")
_Gepoel2esw12OnuIGMPGroupEntry_Object = MibTableRow
gepoel2esw12OnuIGMPGroupEntry = _Gepoel2esw12OnuIGMPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1, 1)
)
gepoel2esw12OnuIGMPGroupEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPGroupOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPGroupMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuIGMPGroupJoinedIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupEntry.setStatus("current")


class _Gepoel2esw12OnuIGMPGroupOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPGroupOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuIGMPGroupOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPGroupOltPort_Object = MibTableColumn
gepoel2esw12OnuIGMPGroupOltPort = _Gepoel2esw12OnuIGMPGroupOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1, 1, 1),
    _Gepoel2esw12OnuIGMPGroupOltPort_Type()
)
gepoel2esw12OnuIGMPGroupOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupOltPort.setStatus("current")
_Gepoel2esw12OnuIGMPGroupMacAddress_Type = MacAddress
_Gepoel2esw12OnuIGMPGroupMacAddress_Object = MibTableColumn
gepoel2esw12OnuIGMPGroupMacAddress = _Gepoel2esw12OnuIGMPGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1, 1, 2),
    _Gepoel2esw12OnuIGMPGroupMacAddress_Type()
)
gepoel2esw12OnuIGMPGroupMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupMacAddress.setStatus("current")


class _Gepoel2esw12OnuIGMPGroupJoinedIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuIGMPGroupJoinedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_Gepoel2esw12OnuIGMPGroupJoinedIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuIGMPGroupJoinedIndex_Object = MibTableColumn
gepoel2esw12OnuIGMPGroupJoinedIndex = _Gepoel2esw12OnuIGMPGroupJoinedIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1, 1, 3),
    _Gepoel2esw12OnuIGMPGroupJoinedIndex_Type()
)
gepoel2esw12OnuIGMPGroupJoinedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupJoinedIndex.setStatus("current")
_Gepoel2esw12OnuIGMPGroupJoinedID_Type = IpAddress
_Gepoel2esw12OnuIGMPGroupJoinedID_Object = MibTableColumn
gepoel2esw12OnuIGMPGroupJoinedID = _Gepoel2esw12OnuIGMPGroupJoinedID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1, 1, 4),
    _Gepoel2esw12OnuIGMPGroupJoinedID_Type()
)
gepoel2esw12OnuIGMPGroupJoinedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupJoinedID.setStatus("current")
_Gepoel2esw12OnuIGMPGroupJoinedPort_Type = DisplayString
_Gepoel2esw12OnuIGMPGroupJoinedPort_Object = MibTableColumn
gepoel2esw12OnuIGMPGroupJoinedPort = _Gepoel2esw12OnuIGMPGroupJoinedPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 4, 3, 1, 1, 5),
    _Gepoel2esw12OnuIGMPGroupJoinedPort_Type()
)
gepoel2esw12OnuIGMPGroupJoinedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuIGMPGroupJoinedPort.setStatus("current")
_Gepoel2esw12OnuBridgeConfig_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuBridgeConfig = _Gepoel2esw12OnuBridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5)
)
_Gepoel2esw12OnuBridgeConfigTable_Object = MibTable
gepoel2esw12OnuBridgeConfigTable = _Gepoel2esw12OnuBridgeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigTable.setStatus("current")
_Gepoel2esw12OnuBridgeConfigEntry_Object = MibTableRow
gepoel2esw12OnuBridgeConfigEntry = _Gepoel2esw12OnuBridgeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1)
)
gepoel2esw12OnuBridgeConfigEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuBridgeConfigOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuBridgeConfigMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuBridgeConfigPort"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigEntry.setStatus("current")


class _Gepoel2esw12OnuBridgeConfigOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuBridgeConfigOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuBridgeConfigOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBridgeConfigOltPort_Object = MibTableColumn
gepoel2esw12OnuBridgeConfigOltPort = _Gepoel2esw12OnuBridgeConfigOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1, 1),
    _Gepoel2esw12OnuBridgeConfigOltPort_Type()
)
gepoel2esw12OnuBridgeConfigOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigOltPort.setStatus("current")
_Gepoel2esw12OnuBridgeConfigMacAddress_Type = MacAddress
_Gepoel2esw12OnuBridgeConfigMacAddress_Object = MibTableColumn
gepoel2esw12OnuBridgeConfigMacAddress = _Gepoel2esw12OnuBridgeConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1, 2),
    _Gepoel2esw12OnuBridgeConfigMacAddress_Type()
)
gepoel2esw12OnuBridgeConfigMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigMacAddress.setStatus("current")


class _Gepoel2esw12OnuBridgeConfigPort_Type(Integer32):
    """Custom type gepoel2esw12OnuBridgeConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuBridgeConfigPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBridgeConfigPort_Object = MibTableColumn
gepoel2esw12OnuBridgeConfigPort = _Gepoel2esw12OnuBridgeConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1, 3),
    _Gepoel2esw12OnuBridgeConfigPort_Type()
)
gepoel2esw12OnuBridgeConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigPort.setStatus("current")


class _Gepoel2esw12OnuBridgeConfigAgeLimit_Type(Integer32):
    """Custom type gepoel2esw12OnuBridgeConfigAgeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_Gepoel2esw12OnuBridgeConfigAgeLimit_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBridgeConfigAgeLimit_Object = MibTableColumn
gepoel2esw12OnuBridgeConfigAgeLimit = _Gepoel2esw12OnuBridgeConfigAgeLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1, 4),
    _Gepoel2esw12OnuBridgeConfigAgeLimit_Type()
)
gepoel2esw12OnuBridgeConfigAgeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigAgeLimit.setStatus("current")


class _Gepoel2esw12OnuBridgeConfigEntryLimit_Type(Integer32):
    """Custom type gepoel2esw12OnuBridgeConfigEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gepoel2esw12OnuBridgeConfigEntryLimit_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBridgeConfigEntryLimit_Object = MibTableColumn
gepoel2esw12OnuBridgeConfigEntryLimit = _Gepoel2esw12OnuBridgeConfigEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1, 5),
    _Gepoel2esw12OnuBridgeConfigEntryLimit_Type()
)
gepoel2esw12OnuBridgeConfigEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigEntryLimit.setStatus("current")


class _Gepoel2esw12OnuBridgeConfigLearningMode_Type(Integer32):
    """Custom type gepoel2esw12OnuBridgeConfigLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuBridgeConfigLearningMode_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBridgeConfigLearningMode_Object = MibTableColumn
gepoel2esw12OnuBridgeConfigLearningMode = _Gepoel2esw12OnuBridgeConfigLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 1, 1, 6),
    _Gepoel2esw12OnuBridgeConfigLearningMode_Type()
)
gepoel2esw12OnuBridgeConfigLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBridgeConfigLearningMode.setStatus("current")
_Gepoel2esw12OnuDynamicMac_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuDynamicMac = _Gepoel2esw12OnuDynamicMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2)
)
_Gepoel2esw12OnuDynamicMacTable_Object = MibTable
gepoel2esw12OnuDynamicMacTable = _Gepoel2esw12OnuDynamicMacTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicMacTable.setStatus("current")
_Gepoel2esw12OnuDynamicMacEntry_Object = MibTableRow
gepoel2esw12OnuDynamicMacEntry = _Gepoel2esw12OnuDynamicMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1, 1)
)
gepoel2esw12OnuDynamicMacEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDynamicOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDynamicLink"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDynamicPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuDynamicMacIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicMacEntry.setStatus("current")


class _Gepoel2esw12OnuDynamicOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuDynamicOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuDynamicOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuDynamicOltPort_Object = MibTableColumn
gepoel2esw12OnuDynamicOltPort = _Gepoel2esw12OnuDynamicOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1, 1, 1),
    _Gepoel2esw12OnuDynamicOltPort_Type()
)
gepoel2esw12OnuDynamicOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicOltPort.setStatus("current")
_Gepoel2esw12OnuDynamicLink_Type = MacAddress
_Gepoel2esw12OnuDynamicLink_Object = MibTableColumn
gepoel2esw12OnuDynamicLink = _Gepoel2esw12OnuDynamicLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1, 1, 2),
    _Gepoel2esw12OnuDynamicLink_Type()
)
gepoel2esw12OnuDynamicLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicLink.setStatus("current")


class _Gepoel2esw12OnuDynamicPort_Type(Integer32):
    """Custom type gepoel2esw12OnuDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuDynamicPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuDynamicPort_Object = MibTableColumn
gepoel2esw12OnuDynamicPort = _Gepoel2esw12OnuDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1, 1, 3),
    _Gepoel2esw12OnuDynamicPort_Type()
)
gepoel2esw12OnuDynamicPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicPort.setStatus("current")


class _Gepoel2esw12OnuDynamicMacIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuDynamicMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gepoel2esw12OnuDynamicMacIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuDynamicMacIndex_Object = MibTableColumn
gepoel2esw12OnuDynamicMacIndex = _Gepoel2esw12OnuDynamicMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1, 1, 4),
    _Gepoel2esw12OnuDynamicMacIndex_Type()
)
gepoel2esw12OnuDynamicMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicMacIndex.setStatus("current")
_Gepoel2esw12OnuDynamicMacLink_Type = MacAddress
_Gepoel2esw12OnuDynamicMacLink_Object = MibTableColumn
gepoel2esw12OnuDynamicMacLink = _Gepoel2esw12OnuDynamicMacLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 1, 1, 5),
    _Gepoel2esw12OnuDynamicMacLink_Type()
)
gepoel2esw12OnuDynamicMacLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuDynamicMacLink.setStatus("current")
_Gepoel2esw12OnuClearDynamicMacTable_Object = MibTable
gepoel2esw12OnuClearDynamicMacTable = _Gepoel2esw12OnuClearDynamicMacTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuClearDynamicMacTable.setStatus("current")
_Gepoel2esw12OnuClearDynamicMacEntry_Object = MibTableRow
gepoel2esw12OnuClearDynamicMacEntry = _Gepoel2esw12OnuClearDynamicMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 2, 1)
)
gepoel2esw12OnuClearDynamicMacEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuClearDynamicMacOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuClearDynamicMacLink"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuClearDynamicMacPort"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuClearDynamicMacEntry.setStatus("current")


class _Gepoel2esw12OnuClearDynamicMacOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuClearDynamicMacOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuClearDynamicMacOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuClearDynamicMacOltPort_Object = MibTableColumn
gepoel2esw12OnuClearDynamicMacOltPort = _Gepoel2esw12OnuClearDynamicMacOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 2, 1, 1),
    _Gepoel2esw12OnuClearDynamicMacOltPort_Type()
)
gepoel2esw12OnuClearDynamicMacOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuClearDynamicMacOltPort.setStatus("current")
_Gepoel2esw12OnuClearDynamicMacLink_Type = MacAddress
_Gepoel2esw12OnuClearDynamicMacLink_Object = MibTableColumn
gepoel2esw12OnuClearDynamicMacLink = _Gepoel2esw12OnuClearDynamicMacLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 2, 1, 2),
    _Gepoel2esw12OnuClearDynamicMacLink_Type()
)
gepoel2esw12OnuClearDynamicMacLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuClearDynamicMacLink.setStatus("current")


class _Gepoel2esw12OnuClearDynamicMacPort_Type(Integer32):
    """Custom type gepoel2esw12OnuClearDynamicMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12OnuClearDynamicMacPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuClearDynamicMacPort_Object = MibTableColumn
gepoel2esw12OnuClearDynamicMacPort = _Gepoel2esw12OnuClearDynamicMacPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 2, 1, 3),
    _Gepoel2esw12OnuClearDynamicMacPort_Type()
)
gepoel2esw12OnuClearDynamicMacPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuClearDynamicMacPort.setStatus("current")


class _Gepoel2esw12OnuClearDynamicMacClear_Type(Integer32):
    """Custom type gepoel2esw12OnuClearDynamicMacClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuClearDynamicMacClear_Type.__name__ = "Integer32"
_Gepoel2esw12OnuClearDynamicMacClear_Object = MibTableColumn
gepoel2esw12OnuClearDynamicMacClear = _Gepoel2esw12OnuClearDynamicMacClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 2, 2, 1, 4),
    _Gepoel2esw12OnuClearDynamicMacClear_Type()
)
gepoel2esw12OnuClearDynamicMacClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuClearDynamicMacClear.setStatus("current")
_Gepoel2esw12OnuVlanOption_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuVlanOption = _Gepoel2esw12OnuVlanOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3)
)
_Gepoel2esw12OnuVlanOptionTable_Object = MibTable
gepoel2esw12OnuVlanOptionTable = _Gepoel2esw12OnuVlanOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionTable.setStatus("current")
_Gepoel2esw12OnuVlanOptionEntry_Object = MibTableRow
gepoel2esw12OnuVlanOptionEntry = _Gepoel2esw12OnuVlanOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1, 1)
)
gepoel2esw12OnuVlanOptionEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuVlanOptionOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuVlanOptionMac"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionEntry.setStatus("current")


class _Gepoel2esw12OnuVlanOptionOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuVlanOptionOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuVlanOptionOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuVlanOptionOltPort_Object = MibTableColumn
gepoel2esw12OnuVlanOptionOltPort = _Gepoel2esw12OnuVlanOptionOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1, 1, 1),
    _Gepoel2esw12OnuVlanOptionOltPort_Type()
)
gepoel2esw12OnuVlanOptionOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionOltPort.setStatus("current")
_Gepoel2esw12OnuVlanOptionMac_Type = MacAddress
_Gepoel2esw12OnuVlanOptionMac_Object = MibTableColumn
gepoel2esw12OnuVlanOptionMac = _Gepoel2esw12OnuVlanOptionMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1, 1, 2),
    _Gepoel2esw12OnuVlanOptionMac_Type()
)
gepoel2esw12OnuVlanOptionMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionMac.setStatus("current")
_Gepoel2esw12OnuVlanOptionEtherType_Type = DisplayString
_Gepoel2esw12OnuVlanOptionEtherType_Object = MibTableColumn
gepoel2esw12OnuVlanOptionEtherType = _Gepoel2esw12OnuVlanOptionEtherType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1, 1, 3),
    _Gepoel2esw12OnuVlanOptionEtherType_Type()
)
gepoel2esw12OnuVlanOptionEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionEtherType.setStatus("current")


class _Gepoel2esw12OnuVlanOptionTagUp_Type(Integer32):
    """Custom type gepoel2esw12OnuVlanOptionTagUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuVlanOptionTagUp_Type.__name__ = "Integer32"
_Gepoel2esw12OnuVlanOptionTagUp_Object = MibTableColumn
gepoel2esw12OnuVlanOptionTagUp = _Gepoel2esw12OnuVlanOptionTagUp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1, 1, 4),
    _Gepoel2esw12OnuVlanOptionTagUp_Type()
)
gepoel2esw12OnuVlanOptionTagUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionTagUp.setStatus("current")


class _Gepoel2esw12OnuVlanOptionTagDown_Type(Integer32):
    """Custom type gepoel2esw12OnuVlanOptionTagDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuVlanOptionTagDown_Type.__name__ = "Integer32"
_Gepoel2esw12OnuVlanOptionTagDown_Object = MibTableColumn
gepoel2esw12OnuVlanOptionTagDown = _Gepoel2esw12OnuVlanOptionTagDown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 3, 1, 1, 5),
    _Gepoel2esw12OnuVlanOptionTagDown_Type()
)
gepoel2esw12OnuVlanOptionTagDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuVlanOptionTagDown.setStatus("current")
_Gepoel2esw12OnuBroadcastQueue_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuBroadcastQueue = _Gepoel2esw12OnuBroadcastQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4)
)
_Gepoel2esw12OnuBroadcastQueueTable_Object = MibTable
gepoel2esw12OnuBroadcastQueueTable = _Gepoel2esw12OnuBroadcastQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuBroadcastQueueTable.setStatus("current")
_Gepoel2esw12OnuBroadcastQueueEntry_Object = MibTableRow
gepoel2esw12OnuBroadcastQueueEntry = _Gepoel2esw12OnuBroadcastQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4, 1, 1)
)
gepoel2esw12OnuBroadcastQueueEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuBroadcastQueueOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuBroadcastQueueMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuBroadcastQueuePort"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuBroadcastQueueEntry.setStatus("current")


class _Gepoel2esw12OnuBroadcastQueueOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuBroadcastQueueOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuBroadcastQueueOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBroadcastQueueOltPort_Object = MibTableColumn
gepoel2esw12OnuBroadcastQueueOltPort = _Gepoel2esw12OnuBroadcastQueueOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4, 1, 1, 1),
    _Gepoel2esw12OnuBroadcastQueueOltPort_Type()
)
gepoel2esw12OnuBroadcastQueueOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBroadcastQueueOltPort.setStatus("current")
_Gepoel2esw12OnuBroadcastQueueMacAddress_Type = MacAddress
_Gepoel2esw12OnuBroadcastQueueMacAddress_Object = MibTableColumn
gepoel2esw12OnuBroadcastQueueMacAddress = _Gepoel2esw12OnuBroadcastQueueMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4, 1, 1, 2),
    _Gepoel2esw12OnuBroadcastQueueMacAddress_Type()
)
gepoel2esw12OnuBroadcastQueueMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBroadcastQueueMacAddress.setStatus("current")


class _Gepoel2esw12OnuBroadcastQueuePort_Type(Integer32):
    """Custom type gepoel2esw12OnuBroadcastQueuePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuBroadcastQueuePort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBroadcastQueuePort_Object = MibTableColumn
gepoel2esw12OnuBroadcastQueuePort = _Gepoel2esw12OnuBroadcastQueuePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4, 1, 1, 3),
    _Gepoel2esw12OnuBroadcastQueuePort_Type()
)
gepoel2esw12OnuBroadcastQueuePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBroadcastQueuePort.setStatus("current")


class _Gepoel2esw12OnuBroadcastQueueIndex_Type(Integer32):
    """Custom type gepoel2esw12OnuBroadcastQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gepoel2esw12OnuBroadcastQueueIndex_Type.__name__ = "Integer32"
_Gepoel2esw12OnuBroadcastQueueIndex_Object = MibTableColumn
gepoel2esw12OnuBroadcastQueueIndex = _Gepoel2esw12OnuBroadcastQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 5, 4, 1, 1, 4),
    _Gepoel2esw12OnuBroadcastQueueIndex_Type()
)
gepoel2esw12OnuBroadcastQueueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuBroadcastQueueIndex.setStatus("current")
_Gepoel2esw12OnuMiscOperationTable_Object = MibTable
gepoel2esw12OnuMiscOperationTable = _Gepoel2esw12OnuMiscOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationTable.setStatus("current")
_Gepoel2esw12OnuMiscOperationEntry_Object = MibTableRow
gepoel2esw12OnuMiscOperationEntry = _Gepoel2esw12OnuMiscOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1)
)
gepoel2esw12OnuMiscOperationEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuMiscOperationOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuMiscOperationMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationEntry.setStatus("current")


class _Gepoel2esw12OnuMiscOperationOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuMiscOperationOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationOltPort_Object = MibTableColumn
gepoel2esw12OnuMiscOperationOltPort = _Gepoel2esw12OnuMiscOperationOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 1),
    _Gepoel2esw12OnuMiscOperationOltPort_Type()
)
gepoel2esw12OnuMiscOperationOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationOltPort.setStatus("current")
_Gepoel2esw12OnuMiscOperationMacAddress_Type = MacAddress
_Gepoel2esw12OnuMiscOperationMacAddress_Object = MibTableColumn
gepoel2esw12OnuMiscOperationMacAddress = _Gepoel2esw12OnuMiscOperationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 2),
    _Gepoel2esw12OnuMiscOperationMacAddress_Type()
)
gepoel2esw12OnuMiscOperationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationMacAddress.setStatus("current")


class _Gepoel2esw12OnuMiscOperationEnable_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationEnable_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationEnable_Object = MibTableColumn
gepoel2esw12OnuMiscOperationEnable = _Gepoel2esw12OnuMiscOperationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 3),
    _Gepoel2esw12OnuMiscOperationEnable_Type()
)
gepoel2esw12OnuMiscOperationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationEnable.setStatus("current")


class _Gepoel2esw12OnuMiscOperationDisable_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationDisable_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationDisable_Object = MibTableColumn
gepoel2esw12OnuMiscOperationDisable = _Gepoel2esw12OnuMiscOperationDisable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 4),
    _Gepoel2esw12OnuMiscOperationDisable_Type()
)
gepoel2esw12OnuMiscOperationDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationDisable.setStatus("current")


class _Gepoel2esw12OnuMiscOperationReset_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationReset_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationReset_Object = MibTableColumn
gepoel2esw12OnuMiscOperationReset = _Gepoel2esw12OnuMiscOperationReset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 5),
    _Gepoel2esw12OnuMiscOperationReset_Type()
)
gepoel2esw12OnuMiscOperationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationReset.setStatus("current")


class _Gepoel2esw12OnuMiscOperationRestore_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationRestore_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationRestore_Object = MibTableColumn
gepoel2esw12OnuMiscOperationRestore = _Gepoel2esw12OnuMiscOperationRestore_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 6),
    _Gepoel2esw12OnuMiscOperationRestore_Type()
)
gepoel2esw12OnuMiscOperationRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationRestore.setStatus("current")
_Gepoel2esw12OnuMiscOperationExportFilePath_Type = DisplayString
_Gepoel2esw12OnuMiscOperationExportFilePath_Object = MibTableColumn
gepoel2esw12OnuMiscOperationExportFilePath = _Gepoel2esw12OnuMiscOperationExportFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 7),
    _Gepoel2esw12OnuMiscOperationExportFilePath_Type()
)
gepoel2esw12OnuMiscOperationExportFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationExportFilePath.setStatus("current")


class _Gepoel2esw12OnuMiscOperationDoExport_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationDoExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationDoExport_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationDoExport_Object = MibTableColumn
gepoel2esw12OnuMiscOperationDoExport = _Gepoel2esw12OnuMiscOperationDoExport_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 8),
    _Gepoel2esw12OnuMiscOperationDoExport_Type()
)
gepoel2esw12OnuMiscOperationDoExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationDoExport.setStatus("current")
_Gepoel2esw12OnuMiscOperationImportFilePath_Type = DisplayString
_Gepoel2esw12OnuMiscOperationImportFilePath_Object = MibTableColumn
gepoel2esw12OnuMiscOperationImportFilePath = _Gepoel2esw12OnuMiscOperationImportFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 9),
    _Gepoel2esw12OnuMiscOperationImportFilePath_Type()
)
gepoel2esw12OnuMiscOperationImportFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationImportFilePath.setStatus("current")


class _Gepoel2esw12OnuMiscOperationDoImport_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationDoImport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationDoImport_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationDoImport_Object = MibTableColumn
gepoel2esw12OnuMiscOperationDoImport = _Gepoel2esw12OnuMiscOperationDoImport_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 10),
    _Gepoel2esw12OnuMiscOperationDoImport_Type()
)
gepoel2esw12OnuMiscOperationDoImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationDoImport.setStatus("current")


class _Gepoel2esw12OnuMiscOperationRFModule_Type(Integer32):
    """Custom type gepoel2esw12OnuMiscOperationRFModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuMiscOperationRFModule_Type.__name__ = "Integer32"
_Gepoel2esw12OnuMiscOperationRFModule_Object = MibTableColumn
gepoel2esw12OnuMiscOperationRFModule = _Gepoel2esw12OnuMiscOperationRFModule_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 6, 1, 11),
    _Gepoel2esw12OnuMiscOperationRFModule_Type()
)
gepoel2esw12OnuMiscOperationRFModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuMiscOperationRFModule.setStatus("current")
_Gepoel2esw12OnuGreenPonTable_Object = MibTable
gepoel2esw12OnuGreenPonTable = _Gepoel2esw12OnuGreenPonTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonTable.setStatus("current")
_Gepoel2esw12OnuGreenPonEntry_Object = MibTableRow
gepoel2esw12OnuGreenPonEntry = _Gepoel2esw12OnuGreenPonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1)
)
gepoel2esw12OnuGreenPonEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuGreenPonOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuGreenPonMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonEntry.setStatus("current")


class _Gepoel2esw12OnuGreenPonOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuGreenPonOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuGreenPonOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuGreenPonOltPort_Object = MibTableColumn
gepoel2esw12OnuGreenPonOltPort = _Gepoel2esw12OnuGreenPonOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 1),
    _Gepoel2esw12OnuGreenPonOltPort_Type()
)
gepoel2esw12OnuGreenPonOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonOltPort.setStatus("current")
_Gepoel2esw12OnuGreenPonMacAddress_Type = MacAddress
_Gepoel2esw12OnuGreenPonMacAddress_Object = MibTableColumn
gepoel2esw12OnuGreenPonMacAddress = _Gepoel2esw12OnuGreenPonMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 2),
    _Gepoel2esw12OnuGreenPonMacAddress_Type()
)
gepoel2esw12OnuGreenPonMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonMacAddress.setStatus("current")


class _Gepoel2esw12OnuGreenPonEnable_Type(Integer32):
    """Custom type gepoel2esw12OnuGreenPonEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuGreenPonEnable_Type.__name__ = "Integer32"
_Gepoel2esw12OnuGreenPonEnable_Object = MibTableColumn
gepoel2esw12OnuGreenPonEnable = _Gepoel2esw12OnuGreenPonEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 3),
    _Gepoel2esw12OnuGreenPonEnable_Type()
)
gepoel2esw12OnuGreenPonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonEnable.setStatus("current")


class _Gepoel2esw12OnuPowerSaveEnable_Type(Integer32):
    """Custom type gepoel2esw12OnuPowerSaveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OnuPowerSaveEnable_Type.__name__ = "Integer32"
_Gepoel2esw12OnuPowerSaveEnable_Object = MibTableColumn
gepoel2esw12OnuPowerSaveEnable = _Gepoel2esw12OnuPowerSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 4),
    _Gepoel2esw12OnuPowerSaveEnable_Type()
)
gepoel2esw12OnuPowerSaveEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuPowerSaveEnable.setStatus("current")


class _Gepoel2esw12OnuGreenPonPDnLaserTransmit_Type(Integer32):
    """Custom type gepoel2esw12OnuGreenPonPDnLaserTransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OnuGreenPonPDnLaserTransmit_Type.__name__ = "Integer32"
_Gepoel2esw12OnuGreenPonPDnLaserTransmit_Object = MibTableColumn
gepoel2esw12OnuGreenPonPDnLaserTransmit = _Gepoel2esw12OnuGreenPonPDnLaserTransmit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 5),
    _Gepoel2esw12OnuGreenPonPDnLaserTransmit_Type()
)
gepoel2esw12OnuGreenPonPDnLaserTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonPDnLaserTransmit.setStatus("current")


class _Gepoel2esw12OnuGreenPonPDnLaserRecv_Type(Integer32):
    """Custom type gepoel2esw12OnuGreenPonPDnLaserRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OnuGreenPonPDnLaserRecv_Type.__name__ = "Integer32"
_Gepoel2esw12OnuGreenPonPDnLaserRecv_Object = MibTableColumn
gepoel2esw12OnuGreenPonPDnLaserRecv = _Gepoel2esw12OnuGreenPonPDnLaserRecv_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 6),
    _Gepoel2esw12OnuGreenPonPDnLaserRecv_Type()
)
gepoel2esw12OnuGreenPonPDnLaserRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonPDnLaserRecv.setStatus("current")


class _Gepoel2esw12OnuGreenPonPDnSerdes_Type(Integer32):
    """Custom type gepoel2esw12OnuGreenPonPDnSerdes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9999, 9999),
    )


_Gepoel2esw12OnuGreenPonPDnSerdes_Type.__name__ = "Integer32"
_Gepoel2esw12OnuGreenPonPDnSerdes_Object = MibTableColumn
gepoel2esw12OnuGreenPonPDnSerdes = _Gepoel2esw12OnuGreenPonPDnSerdes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 7, 1, 7),
    _Gepoel2esw12OnuGreenPonPDnSerdes_Type()
)
gepoel2esw12OnuGreenPonPDnSerdes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuGreenPonPDnSerdes.setStatus("current")
_Gepoel2esw12OnuAuthorization_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuAuthorization = _Gepoel2esw12OnuAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8)
)
_Gepoel2esw12OnuAuthorizationTable_Object = MibTable
gepoel2esw12OnuAuthorizationTable = _Gepoel2esw12OnuAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationTable.setStatus("current")
_Gepoel2esw12OnuAuthorizationEntry_Object = MibTableRow
gepoel2esw12OnuAuthorizationEntry = _Gepoel2esw12OnuAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1)
)
gepoel2esw12OnuAuthorizationEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuAuthorizationOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12OnuAuthorizationMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationEntry.setStatus("current")


class _Gepoel2esw12OnuAuthorizationOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuAuthorizationOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuAuthorizationOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuAuthorizationOltPort_Object = MibTableColumn
gepoel2esw12OnuAuthorizationOltPort = _Gepoel2esw12OnuAuthorizationOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1, 1),
    _Gepoel2esw12OnuAuthorizationOltPort_Type()
)
gepoel2esw12OnuAuthorizationOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationOltPort.setStatus("current")
_Gepoel2esw12OnuAuthorizationMacAddress_Type = MacAddress
_Gepoel2esw12OnuAuthorizationMacAddress_Object = MibTableColumn
gepoel2esw12OnuAuthorizationMacAddress = _Gepoel2esw12OnuAuthorizationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1, 2),
    _Gepoel2esw12OnuAuthorizationMacAddress_Type()
)
gepoel2esw12OnuAuthorizationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationMacAddress.setStatus("current")


class _Gepoel2esw12OnuAuthorizationAllLinks_Type(Integer32):
    """Custom type gepoel2esw12OnuAuthorizationAllLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Gepoel2esw12OnuAuthorizationAllLinks_Type.__name__ = "Integer32"
_Gepoel2esw12OnuAuthorizationAllLinks_Object = MibTableColumn
gepoel2esw12OnuAuthorizationAllLinks = _Gepoel2esw12OnuAuthorizationAllLinks_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1, 3),
    _Gepoel2esw12OnuAuthorizationAllLinks_Type()
)
gepoel2esw12OnuAuthorizationAllLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationAllLinks.setStatus("current")
_Gepoel2esw12OnuAuthorizationStatus_Type = DisplayString
_Gepoel2esw12OnuAuthorizationStatus_Object = MibTableColumn
gepoel2esw12OnuAuthorizationStatus = _Gepoel2esw12OnuAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1, 4),
    _Gepoel2esw12OnuAuthorizationStatus_Type()
)
gepoel2esw12OnuAuthorizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationStatus.setStatus("current")
_Gepoel2esw12OnuAuthorizations_Type = DisplayString
_Gepoel2esw12OnuAuthorizations_Object = MibTableColumn
gepoel2esw12OnuAuthorizations = _Gepoel2esw12OnuAuthorizations_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1, 5),
    _Gepoel2esw12OnuAuthorizations_Type()
)
gepoel2esw12OnuAuthorizations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizations.setStatus("current")


class _Gepoel2esw12OnuAuthorize_Type(Integer32):
    """Custom type gepoel2esw12OnuAuthorize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuAuthorize_Type.__name__ = "Integer32"
_Gepoel2esw12OnuAuthorize_Object = MibTableColumn
gepoel2esw12OnuAuthorize = _Gepoel2esw12OnuAuthorize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 1, 1, 6),
    _Gepoel2esw12OnuAuthorize_Type()
)
gepoel2esw12OnuAuthorize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorize.setStatus("current")
_Gepoel2esw12OnuAuthorizationAdd_ObjectIdentity = ObjectIdentity
gepoel2esw12OnuAuthorizationAdd = _Gepoel2esw12OnuAuthorizationAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 2)
)


class _Gepoel2esw12OnuAuthorizationAddOltPort_Type(Integer32):
    """Custom type gepoel2esw12OnuAuthorizationAddOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12OnuAuthorizationAddOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12OnuAuthorizationAddOltPort_Object = MibScalar
gepoel2esw12OnuAuthorizationAddOltPort = _Gepoel2esw12OnuAuthorizationAddOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 2, 1),
    _Gepoel2esw12OnuAuthorizationAddOltPort_Type()
)
gepoel2esw12OnuAuthorizationAddOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationAddOltPort.setStatus("current")
_Gepoel2esw12OnuAuthorizationAddOnuMac_Type = MacAddress
_Gepoel2esw12OnuAuthorizationAddOnuMac_Object = MibScalar
gepoel2esw12OnuAuthorizationAddOnuMac = _Gepoel2esw12OnuAuthorizationAddOnuMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 2, 2),
    _Gepoel2esw12OnuAuthorizationAddOnuMac_Type()
)
gepoel2esw12OnuAuthorizationAddOnuMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationAddOnuMac.setStatus("current")


class _Gepoel2esw12OnuAuthorizationAddLinkNumber_Type(Integer32):
    """Custom type gepoel2esw12OnuAuthorizationAddLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Gepoel2esw12OnuAuthorizationAddLinkNumber_Type.__name__ = "Integer32"
_Gepoel2esw12OnuAuthorizationAddLinkNumber_Object = MibScalar
gepoel2esw12OnuAuthorizationAddLinkNumber = _Gepoel2esw12OnuAuthorizationAddLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 2, 3),
    _Gepoel2esw12OnuAuthorizationAddLinkNumber_Type()
)
gepoel2esw12OnuAuthorizationAddLinkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationAddLinkNumber.setStatus("current")


class _Gepoel2esw12OnuAuthorizationAddDo_Type(Integer32):
    """Custom type gepoel2esw12OnuAuthorizationAddDo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12OnuAuthorizationAddDo_Type.__name__ = "Integer32"
_Gepoel2esw12OnuAuthorizationAddDo_Object = MibScalar
gepoel2esw12OnuAuthorizationAddDo = _Gepoel2esw12OnuAuthorizationAddDo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 3, 8, 2, 4),
    _Gepoel2esw12OnuAuthorizationAddDo_Type()
)
gepoel2esw12OnuAuthorizationAddDo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12OnuAuthorizationAddDo.setStatus("current")
_Gepoel2esw12LlidManagement_ObjectIdentity = ObjectIdentity
gepoel2esw12LlidManagement = _Gepoel2esw12LlidManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4)
)
_Gepoel2esw12LinkQue_ObjectIdentity = ObjectIdentity
gepoel2esw12LinkQue = _Gepoel2esw12LinkQue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1)
)
_Gepoel2esw12LinkSLATable_Object = MibTable
gepoel2esw12LinkSLATable = _Gepoel2esw12LinkSLATable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLATable.setStatus("current")
_Gepoel2esw12LinkSLAEntry_Object = MibTableRow
gepoel2esw12LinkSLAEntry = _Gepoel2esw12LinkSLAEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1)
)
gepoel2esw12LinkSLAEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAEntry.setStatus("current")


class _Gepoel2esw12LinkOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkOltPort_Object = MibTableColumn
gepoel2esw12LinkOltPort = _Gepoel2esw12LinkOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 1),
    _Gepoel2esw12LinkOltPort_Type()
)
gepoel2esw12LinkOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkOltPort.setStatus("current")
_Gepoel2esw12LinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkMacAddress_Object = MibTableColumn
gepoel2esw12LinkMacAddress = _Gepoel2esw12LinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 2),
    _Gepoel2esw12LinkMacAddress_Type()
)
gepoel2esw12LinkMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkSLAMinShaperEnable_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMinShaperEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkSLAMinShaperEnable_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMinShaperEnable_Object = MibTableColumn
gepoel2esw12LinkSLAMinShaperEnable = _Gepoel2esw12LinkSLAMinShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 3),
    _Gepoel2esw12LinkSLAMinShaperEnable_Type()
)
gepoel2esw12LinkSLAMinShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMinShaperEnable.setStatus("current")


class _Gepoel2esw12LinkSLAMaxShaperMaxBw_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMaxShaperMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkSLAMaxShaperMaxBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMaxShaperMaxBw_Object = MibTableColumn
gepoel2esw12LinkSLAMaxShaperMaxBw = _Gepoel2esw12LinkSLAMaxShaperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 4),
    _Gepoel2esw12LinkSLAMaxShaperMaxBw_Type()
)
gepoel2esw12LinkSLAMaxShaperMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMaxShaperMaxBw.setStatus("current")


class _Gepoel2esw12LinkSLAMaxShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMaxShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkSLAMaxShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMaxShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkSLAMaxShaperMaxBurst = _Gepoel2esw12LinkSLAMaxShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 5),
    _Gepoel2esw12LinkSLAMaxShaperMaxBurst_Type()
)
gepoel2esw12LinkSLAMaxShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMaxShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkSLAMaxShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMaxShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkSLAMaxShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMaxShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkSLAMaxShaperSchedulerLevel = _Gepoel2esw12LinkSLAMaxShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 6),
    _Gepoel2esw12LinkSLAMaxShaperSchedulerLevel_Type()
)
gepoel2esw12LinkSLAMaxShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMaxShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkSLAMaxShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMaxShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkSLAMaxShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMaxShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkSLAMaxShaperSchedulerWeight = _Gepoel2esw12LinkSLAMaxShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 7),
    _Gepoel2esw12LinkSLAMaxShaperSchedulerWeight_Type()
)
gepoel2esw12LinkSLAMaxShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMaxShaperSchedulerWeight.setStatus("current")


class _Gepoel2esw12LinkSLAMinShaperMinBw_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMinShaperMinBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkSLAMinShaperMinBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMinShaperMinBw_Object = MibTableColumn
gepoel2esw12LinkSLAMinShaperMinBw = _Gepoel2esw12LinkSLAMinShaperMinBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 8),
    _Gepoel2esw12LinkSLAMinShaperMinBw_Type()
)
gepoel2esw12LinkSLAMinShaperMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMinShaperMinBw.setStatus("current")


class _Gepoel2esw12LinkSLAMinShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMinShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkSLAMinShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMinShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkSLAMinShaperMaxBurst = _Gepoel2esw12LinkSLAMinShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 9),
    _Gepoel2esw12LinkSLAMinShaperMaxBurst_Type()
)
gepoel2esw12LinkSLAMinShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMinShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkSLAMinShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMinShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkSLAMinShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMinShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkSLAMinShaperSchedulerLevel = _Gepoel2esw12LinkSLAMinShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 10),
    _Gepoel2esw12LinkSLAMinShaperSchedulerLevel_Type()
)
gepoel2esw12LinkSLAMinShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMinShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkSLAMinShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkSLAMinShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkSLAMinShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkSLAMinShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkSLAMinShaperSchedulerWeight = _Gepoel2esw12LinkSLAMinShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 1, 1, 11),
    _Gepoel2esw12LinkSLAMinShaperSchedulerWeight_Type()
)
gepoel2esw12LinkSLAMinShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkSLAMinShaperSchedulerWeight.setStatus("current")
_Gepoel2esw12LinkUpQSLATable_Object = MibTable
gepoel2esw12LinkUpQSLATable = _Gepoel2esw12LinkUpQSLATable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLATable.setStatus("current")
_Gepoel2esw12LinkUpQSLAEntry_Object = MibTableRow
gepoel2esw12LinkUpQSLAEntry = _Gepoel2esw12LinkUpQSLAEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1)
)
gepoel2esw12LinkUpQSLAEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkUpQOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkUpQMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAEntry.setStatus("current")


class _Gepoel2esw12LinkUpQOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkUpQOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQOltPort_Object = MibTableColumn
gepoel2esw12LinkUpQOltPort = _Gepoel2esw12LinkUpQOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 1),
    _Gepoel2esw12LinkUpQOltPort_Type()
)
gepoel2esw12LinkUpQOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQOltPort.setStatus("current")
_Gepoel2esw12LinkUpQMacAddress_Type = MacAddress
_Gepoel2esw12LinkUpQMacAddress_Object = MibTableColumn
gepoel2esw12LinkUpQMacAddress = _Gepoel2esw12LinkUpQMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 2),
    _Gepoel2esw12LinkUpQMacAddress_Type()
)
gepoel2esw12LinkUpQMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQMacAddress.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMinShaperEnable_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMinShaperEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkUpQSLAMinShaperEnable_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMinShaperEnable_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMinShaperEnable = _Gepoel2esw12LinkUpQSLAMinShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 3),
    _Gepoel2esw12LinkUpQSLAMinShaperEnable_Type()
)
gepoel2esw12LinkUpQSLAMinShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMinShaperEnable.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMaxShaperMaxBw_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMaxShaperMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkUpQSLAMaxShaperMaxBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMaxShaperMaxBw_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMaxShaperMaxBw = _Gepoel2esw12LinkUpQSLAMaxShaperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 4),
    _Gepoel2esw12LinkUpQSLAMaxShaperMaxBw_Type()
)
gepoel2esw12LinkUpQSLAMaxShaperMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMaxShaperMaxBw.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMaxShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMaxShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkUpQSLAMaxShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMaxShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMaxShaperMaxBurst = _Gepoel2esw12LinkUpQSLAMaxShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 5),
    _Gepoel2esw12LinkUpQSLAMaxShaperMaxBurst_Type()
)
gepoel2esw12LinkUpQSLAMaxShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMaxShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel = _Gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 6),
    _Gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel_Type()
)
gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight = _Gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 7),
    _Gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight_Type()
)
gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMinShaperMinBw_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMinShaperMinBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkUpQSLAMinShaperMinBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMinShaperMinBw_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMinShaperMinBw = _Gepoel2esw12LinkUpQSLAMinShaperMinBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 8),
    _Gepoel2esw12LinkUpQSLAMinShaperMinBw_Type()
)
gepoel2esw12LinkUpQSLAMinShaperMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMinShaperMinBw.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMinShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMinShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkUpQSLAMinShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMinShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMinShaperMaxBurst = _Gepoel2esw12LinkUpQSLAMinShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 9),
    _Gepoel2esw12LinkUpQSLAMinShaperMaxBurst_Type()
)
gepoel2esw12LinkUpQSLAMinShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMinShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel = _Gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 10),
    _Gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel_Type()
)
gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight = _Gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 2, 1, 11),
    _Gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight_Type()
)
gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight.setStatus("current")
_Gepoel2esw12LinkDnQSLATable_Object = MibTable
gepoel2esw12LinkDnQSLATable = _Gepoel2esw12LinkDnQSLATable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLATable.setStatus("current")
_Gepoel2esw12LinkDnQSLAEntry_Object = MibTableRow
gepoel2esw12LinkDnQSLAEntry = _Gepoel2esw12LinkDnQSLAEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1)
)
gepoel2esw12LinkDnQSLAEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkDnQOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkDnQMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAEntry.setStatus("current")


class _Gepoel2esw12LinkDnQOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkDnQOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQOltPort_Object = MibTableColumn
gepoel2esw12LinkDnQOltPort = _Gepoel2esw12LinkDnQOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 1),
    _Gepoel2esw12LinkDnQOltPort_Type()
)
gepoel2esw12LinkDnQOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQOltPort.setStatus("current")
_Gepoel2esw12LinkDnQMacAddress_Type = MacAddress
_Gepoel2esw12LinkDnQMacAddress_Object = MibTableColumn
gepoel2esw12LinkDnQMacAddress = _Gepoel2esw12LinkDnQMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 2),
    _Gepoel2esw12LinkDnQMacAddress_Type()
)
gepoel2esw12LinkDnQMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQMacAddress.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMinShaperEnable_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMinShaperEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkDnQSLAMinShaperEnable_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMinShaperEnable_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMinShaperEnable = _Gepoel2esw12LinkDnQSLAMinShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 3),
    _Gepoel2esw12LinkDnQSLAMinShaperEnable_Type()
)
gepoel2esw12LinkDnQSLAMinShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMinShaperEnable.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMaxShaperMaxBw_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMaxShaperMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkDnQSLAMaxShaperMaxBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMaxShaperMaxBw_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMaxShaperMaxBw = _Gepoel2esw12LinkDnQSLAMaxShaperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 4),
    _Gepoel2esw12LinkDnQSLAMaxShaperMaxBw_Type()
)
gepoel2esw12LinkDnQSLAMaxShaperMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMaxShaperMaxBw.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMaxShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMaxShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkDnQSLAMaxShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMaxShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMaxShaperMaxBurst = _Gepoel2esw12LinkDnQSLAMaxShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 5),
    _Gepoel2esw12LinkDnQSLAMaxShaperMaxBurst_Type()
)
gepoel2esw12LinkDnQSLAMaxShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMaxShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel = _Gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 6),
    _Gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel_Type()
)
gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight = _Gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 7),
    _Gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight_Type()
)
gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMinShaperMinBw_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMinShaperMinBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkDnQSLAMinShaperMinBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMinShaperMinBw_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMinShaperMinBw = _Gepoel2esw12LinkDnQSLAMinShaperMinBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 8),
    _Gepoel2esw12LinkDnQSLAMinShaperMinBw_Type()
)
gepoel2esw12LinkDnQSLAMinShaperMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMinShaperMinBw.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMinShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMinShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkDnQSLAMinShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMinShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMinShaperMaxBurst = _Gepoel2esw12LinkDnQSLAMinShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 9),
    _Gepoel2esw12LinkDnQSLAMinShaperMaxBurst_Type()
)
gepoel2esw12LinkDnQSLAMinShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMinShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel = _Gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 10),
    _Gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel_Type()
)
gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight = _Gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 1, 3, 1, 11),
    _Gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight_Type()
)
gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight.setStatus("current")
_Gepoel2esw12LinkMulticastSLATable_Object = MibTable
gepoel2esw12LinkMulticastSLATable = _Gepoel2esw12LinkMulticastSLATable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLATable.setStatus("current")
_Gepoel2esw12LinkMulticastSLAEntry_Object = MibTableRow
gepoel2esw12LinkMulticastSLAEntry = _Gepoel2esw12LinkMulticastSLAEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1)
)
gepoel2esw12LinkMulticastSLAEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkMulticastOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkMulticastMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAEntry.setStatus("current")


class _Gepoel2esw12LinkMulticastOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkMulticastOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastOltPort_Object = MibTableColumn
gepoel2esw12LinkMulticastOltPort = _Gepoel2esw12LinkMulticastOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 1),
    _Gepoel2esw12LinkMulticastOltPort_Type()
)
gepoel2esw12LinkMulticastOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastOltPort.setStatus("current")
_Gepoel2esw12LinkMulticastMacAddress_Type = MacAddress
_Gepoel2esw12LinkMulticastMacAddress_Object = MibTableColumn
gepoel2esw12LinkMulticastMacAddress = _Gepoel2esw12LinkMulticastMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 2),
    _Gepoel2esw12LinkMulticastMacAddress_Type()
)
gepoel2esw12LinkMulticastMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastMacAddress.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMinShaperEnable_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMinShaperEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkMulticastSLAMinShaperEnable_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMinShaperEnable_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMinShaperEnable = _Gepoel2esw12LinkMulticastSLAMinShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 3),
    _Gepoel2esw12LinkMulticastSLAMinShaperEnable_Type()
)
gepoel2esw12LinkMulticastSLAMinShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMinShaperEnable.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMaxShaperMaxBw_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMaxShaperMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkMulticastSLAMaxShaperMaxBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMaxShaperMaxBw_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMaxShaperMaxBw = _Gepoel2esw12LinkMulticastSLAMaxShaperMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 4),
    _Gepoel2esw12LinkMulticastSLAMaxShaperMaxBw_Type()
)
gepoel2esw12LinkMulticastSLAMaxShaperMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMaxShaperMaxBw.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst = _Gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 5),
    _Gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst_Type()
)
gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel = _Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 6),
    _Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel_Type()
)
gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight = _Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 7),
    _Gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight_Type()
)
gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMinShaperMinBw_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMinShaperMinBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 1000000),
    )


_Gepoel2esw12LinkMulticastSLAMinShaperMinBw_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMinShaperMinBw_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMinShaperMinBw = _Gepoel2esw12LinkMulticastSLAMinShaperMinBw_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 8),
    _Gepoel2esw12LinkMulticastSLAMinShaperMinBw_Type()
)
gepoel2esw12LinkMulticastSLAMinShaperMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMinShaperMinBw.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMinShaperMaxBurst_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMinShaperMaxBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gepoel2esw12LinkMulticastSLAMinShaperMaxBurst_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMinShaperMaxBurst_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMinShaperMaxBurst = _Gepoel2esw12LinkMulticastSLAMinShaperMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 9),
    _Gepoel2esw12LinkMulticastSLAMinShaperMaxBurst_Type()
)
gepoel2esw12LinkMulticastSLAMinShaperMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMinShaperMaxBurst.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel = _Gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 10),
    _Gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel_Type()
)
gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel.setStatus("current")


class _Gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight_Type(Integer32):
    """Custom type gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_Gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight_Object = MibTableColumn
gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight = _Gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 2, 1, 11),
    _Gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight_Type()
)
gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight.setStatus("current")
_Gepoel2esw12LinkBridge_ObjectIdentity = ObjectIdentity
gepoel2esw12LinkBridge = _Gepoel2esw12LinkBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3)
)
_Gepoel2esw12LinkBridgeModeTable_Object = MibTable
gepoel2esw12LinkBridgeModeTable = _Gepoel2esw12LinkBridgeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkBridgeModeTable.setStatus("current")
_Gepoel2esw12LinkBridgeModeEntry_Object = MibTableRow
gepoel2esw12LinkBridgeModeEntry = _Gepoel2esw12LinkBridgeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1)
)
gepoel2esw12LinkBridgeModeEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkBridgeOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkBridgeLinkMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkBridgeModeEntry.setStatus("current")


class _Gepoel2esw12LinkBridgeOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkBridgeOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkBridgeOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkBridgeOltPort_Object = MibTableColumn
gepoel2esw12LinkBridgeOltPort = _Gepoel2esw12LinkBridgeOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 1),
    _Gepoel2esw12LinkBridgeOltPort_Type()
)
gepoel2esw12LinkBridgeOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkBridgeOltPort.setStatus("current")
_Gepoel2esw12LinkBridgeLinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkBridgeLinkMacAddress_Object = MibTableColumn
gepoel2esw12LinkBridgeLinkMacAddress = _Gepoel2esw12LinkBridgeLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 2),
    _Gepoel2esw12LinkBridgeLinkMacAddress_Type()
)
gepoel2esw12LinkBridgeLinkMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkBridgeLinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkBridgeMode_Type(Integer32):
    """Custom type gepoel2esw12LinkBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_Gepoel2esw12LinkBridgeMode_Type.__name__ = "Integer32"
_Gepoel2esw12LinkBridgeMode_Object = MibTableColumn
gepoel2esw12LinkBridgeMode = _Gepoel2esw12LinkBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 3),
    _Gepoel2esw12LinkBridgeMode_Type()
)
gepoel2esw12LinkBridgeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkBridgeMode.setStatus("current")


class _Gepoel2esw12LinkBridgeDestNNI_Type(Integer32):
    """Custom type gepoel2esw12LinkBridgeDestNNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkBridgeDestNNI_Type.__name__ = "Integer32"
_Gepoel2esw12LinkBridgeDestNNI_Object = MibTableColumn
gepoel2esw12LinkBridgeDestNNI = _Gepoel2esw12LinkBridgeDestNNI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 4),
    _Gepoel2esw12LinkBridgeDestNNI_Type()
)
gepoel2esw12LinkBridgeDestNNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkBridgeDestNNI.setStatus("current")


class _Gepoel2esw12LinkEntryLimit_Type(Integer32):
    """Custom type gepoel2esw12LinkEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Gepoel2esw12LinkEntryLimit_Type.__name__ = "Integer32"
_Gepoel2esw12LinkEntryLimit_Object = MibTableColumn
gepoel2esw12LinkEntryLimit = _Gepoel2esw12LinkEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 5),
    _Gepoel2esw12LinkEntryLimit_Type()
)
gepoel2esw12LinkEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkEntryLimit.setStatus("current")
_Gepoel2esw12LinkVlan_Type = DisplayString
_Gepoel2esw12LinkVlan_Object = MibTableColumn
gepoel2esw12LinkVlan = _Gepoel2esw12LinkVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 6),
    _Gepoel2esw12LinkVlan_Type()
)
gepoel2esw12LinkVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkVlan.setStatus("current")


class _Gepoel2esw12LinkUpstreamCoS_Type(Integer32):
    """Custom type gepoel2esw12LinkUpstreamCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkUpstreamCoS_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUpstreamCoS_Object = MibTableColumn
gepoel2esw12LinkUpstreamCoS = _Gepoel2esw12LinkUpstreamCoS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 7),
    _Gepoel2esw12LinkUpstreamCoS_Type()
)
gepoel2esw12LinkUpstreamCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUpstreamCoS.setStatus("current")


class _Gepoel2esw12LinkMaxToSCoS_Type(Integer32):
    """Custom type gepoel2esw12LinkMaxToSCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_Gepoel2esw12LinkMaxToSCoS_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMaxToSCoS_Object = MibTableColumn
gepoel2esw12LinkMaxToSCoS = _Gepoel2esw12LinkMaxToSCoS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 8),
    _Gepoel2esw12LinkMaxToSCoS_Type()
)
gepoel2esw12LinkMaxToSCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMaxToSCoS.setStatus("current")


class _Gepoel2esw12LinkMinToSCoS_Type(Integer32):
    """Custom type gepoel2esw12LinkMinToSCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_Gepoel2esw12LinkMinToSCoS_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMinToSCoS_Object = MibTableColumn
gepoel2esw12LinkMinToSCoS = _Gepoel2esw12LinkMinToSCoS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 9),
    _Gepoel2esw12LinkMinToSCoS_Type()
)
gepoel2esw12LinkMinToSCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMinToSCoS.setStatus("current")


class _Gepoel2esw12LinkUsingCosTos_Type(Integer32):
    """Custom type gepoel2esw12LinkUsingCosTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkUsingCosTos_Type.__name__ = "Integer32"
_Gepoel2esw12LinkUsingCosTos_Object = MibTableColumn
gepoel2esw12LinkUsingCosTos = _Gepoel2esw12LinkUsingCosTos_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 10),
    _Gepoel2esw12LinkUsingCosTos_Type()
)
gepoel2esw12LinkUsingCosTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkUsingCosTos.setStatus("current")


class _Gepoel2esw12LinkNonIP_Type(Integer32):
    """Custom type gepoel2esw12LinkNonIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkNonIP_Type.__name__ = "Integer32"
_Gepoel2esw12LinkNonIP_Object = MibTableColumn
gepoel2esw12LinkNonIP = _Gepoel2esw12LinkNonIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 1, 1, 11),
    _Gepoel2esw12LinkNonIP_Type()
)
gepoel2esw12LinkNonIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkNonIP.setStatus("current")
_Gepoel2esw12LinkBridgeModeDel_ObjectIdentity = ObjectIdentity
gepoel2esw12LinkBridgeModeDel = _Gepoel2esw12LinkBridgeModeDel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 2)
)


class _Gepoel2esw12LinkDelBridgeOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkDelBridgeOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkDelBridgeOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDelBridgeOltPort_Object = MibScalar
gepoel2esw12LinkDelBridgeOltPort = _Gepoel2esw12LinkDelBridgeOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 2, 1),
    _Gepoel2esw12LinkDelBridgeOltPort_Type()
)
gepoel2esw12LinkDelBridgeOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelBridgeOltPort.setStatus("current")
_Gepoel2esw12LinkDelBridgeLinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkDelBridgeLinkMacAddress_Object = MibScalar
gepoel2esw12LinkDelBridgeLinkMacAddress = _Gepoel2esw12LinkDelBridgeLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 2, 2),
    _Gepoel2esw12LinkDelBridgeLinkMacAddress_Type()
)
gepoel2esw12LinkDelBridgeLinkMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelBridgeLinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkDelBridgeMode_Type(Integer32):
    """Custom type gepoel2esw12LinkDelBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Gepoel2esw12LinkDelBridgeMode_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDelBridgeMode_Object = MibScalar
gepoel2esw12LinkDelBridgeMode = _Gepoel2esw12LinkDelBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 2, 3),
    _Gepoel2esw12LinkDelBridgeMode_Type()
)
gepoel2esw12LinkDelBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelBridgeMode.setStatus("current")


class _Gepoel2esw12D0DelLinkBridgeMode_Type(Integer32):
    """Custom type gepoel2esw12D0DelLinkBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12D0DelLinkBridgeMode_Type.__name__ = "Integer32"
_Gepoel2esw12D0DelLinkBridgeMode_Object = MibScalar
gepoel2esw12D0DelLinkBridgeMode = _Gepoel2esw12D0DelLinkBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 2, 4),
    _Gepoel2esw12D0DelLinkBridgeMode_Type()
)
gepoel2esw12D0DelLinkBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12D0DelLinkBridgeMode.setStatus("current")
_Gepoel2esw12LinkBridgeModeAdd_ObjectIdentity = ObjectIdentity
gepoel2esw12LinkBridgeModeAdd = _Gepoel2esw12LinkBridgeModeAdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3)
)


class _Gepoel2esw12LinkAddBridgeOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkAddBridgeOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkAddBridgeOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddBridgeOltPort_Object = MibScalar
gepoel2esw12LinkAddBridgeOltPort = _Gepoel2esw12LinkAddBridgeOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 1),
    _Gepoel2esw12LinkAddBridgeOltPort_Type()
)
gepoel2esw12LinkAddBridgeOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddBridgeOltPort.setStatus("current")
_Gepoel2esw12LinkAddBridgeLinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkAddBridgeLinkMacAddress_Object = MibScalar
gepoel2esw12LinkAddBridgeLinkMacAddress = _Gepoel2esw12LinkAddBridgeLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 2),
    _Gepoel2esw12LinkAddBridgeLinkMacAddress_Type()
)
gepoel2esw12LinkAddBridgeLinkMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddBridgeLinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkAddBridgeMode_Type(Integer32):
    """Custom type gepoel2esw12LinkAddBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Gepoel2esw12LinkAddBridgeMode_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddBridgeMode_Object = MibScalar
gepoel2esw12LinkAddBridgeMode = _Gepoel2esw12LinkAddBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 3),
    _Gepoel2esw12LinkAddBridgeMode_Type()
)
gepoel2esw12LinkAddBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddBridgeMode.setStatus("current")


class _Gepoel2esw12LinkAddBridgeDestNNI_Type(Integer32):
    """Custom type gepoel2esw12LinkAddBridgeDestNNI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkAddBridgeDestNNI_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddBridgeDestNNI_Object = MibScalar
gepoel2esw12LinkAddBridgeDestNNI = _Gepoel2esw12LinkAddBridgeDestNNI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 4),
    _Gepoel2esw12LinkAddBridgeDestNNI_Type()
)
gepoel2esw12LinkAddBridgeDestNNI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddBridgeDestNNI.setStatus("current")


class _Gepoel2esw12LinkAddEntryLimit_Type(Integer32):
    """Custom type gepoel2esw12LinkAddEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Gepoel2esw12LinkAddEntryLimit_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddEntryLimit_Object = MibScalar
gepoel2esw12LinkAddEntryLimit = _Gepoel2esw12LinkAddEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 5),
    _Gepoel2esw12LinkAddEntryLimit_Type()
)
gepoel2esw12LinkAddEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddEntryLimit.setStatus("current")


class _Gepoel2esw12LinkAddVlan_Type(Integer32):
    """Custom type gepoel2esw12LinkAddVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gepoel2esw12LinkAddVlan_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddVlan_Object = MibScalar
gepoel2esw12LinkAddVlan = _Gepoel2esw12LinkAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 6),
    _Gepoel2esw12LinkAddVlan_Type()
)
gepoel2esw12LinkAddVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddVlan.setStatus("current")


class _Gepoel2esw12LinkAddMaxVlan_Type(Integer32):
    """Custom type gepoel2esw12LinkAddMaxVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gepoel2esw12LinkAddMaxVlan_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddMaxVlan_Object = MibScalar
gepoel2esw12LinkAddMaxVlan = _Gepoel2esw12LinkAddMaxVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 7),
    _Gepoel2esw12LinkAddMaxVlan_Type()
)
gepoel2esw12LinkAddMaxVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddMaxVlan.setStatus("current")


class _Gepoel2esw12LinkAddUpstreamCoS_Type(Integer32):
    """Custom type gepoel2esw12LinkAddUpstreamCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkAddUpstreamCoS_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddUpstreamCoS_Object = MibScalar
gepoel2esw12LinkAddUpstreamCoS = _Gepoel2esw12LinkAddUpstreamCoS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 8),
    _Gepoel2esw12LinkAddUpstreamCoS_Type()
)
gepoel2esw12LinkAddUpstreamCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddUpstreamCoS.setStatus("current")


class _Gepoel2esw12LinkAddMaxToSCoS_Type(Integer32):
    """Custom type gepoel2esw12LinkAddMaxToSCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkAddMaxToSCoS_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddMaxToSCoS_Object = MibScalar
gepoel2esw12LinkAddMaxToSCoS = _Gepoel2esw12LinkAddMaxToSCoS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 9),
    _Gepoel2esw12LinkAddMaxToSCoS_Type()
)
gepoel2esw12LinkAddMaxToSCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddMaxToSCoS.setStatus("current")


class _Gepoel2esw12LinkAddMinToSCoS_Type(Integer32):
    """Custom type gepoel2esw12LinkAddMinToSCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkAddMinToSCoS_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddMinToSCoS_Object = MibScalar
gepoel2esw12LinkAddMinToSCoS = _Gepoel2esw12LinkAddMinToSCoS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 10),
    _Gepoel2esw12LinkAddMinToSCoS_Type()
)
gepoel2esw12LinkAddMinToSCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddMinToSCoS.setStatus("current")


class _Gepoel2esw12LinkAddUsingCosTos_Type(Integer32):
    """Custom type gepoel2esw12LinkAddUsingCosTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkAddUsingCosTos_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddUsingCosTos_Object = MibScalar
gepoel2esw12LinkAddUsingCosTos = _Gepoel2esw12LinkAddUsingCosTos_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 11),
    _Gepoel2esw12LinkAddUsingCosTos_Type()
)
gepoel2esw12LinkAddUsingCosTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddUsingCosTos.setStatus("current")


class _Gepoel2esw12LinkAddNonIP_Type(Integer32):
    """Custom type gepoel2esw12LinkAddNonIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkAddNonIP_Type.__name__ = "Integer32"
_Gepoel2esw12LinkAddNonIP_Object = MibScalar
gepoel2esw12LinkAddNonIP = _Gepoel2esw12LinkAddNonIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 12),
    _Gepoel2esw12LinkAddNonIP_Type()
)
gepoel2esw12LinkAddNonIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkAddNonIP.setStatus("current")


class _Gepoel2esw12DoLinkAddBridgeMode_Type(Integer32):
    """Custom type gepoel2esw12DoLinkAddBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DoLinkAddBridgeMode_Type.__name__ = "Integer32"
_Gepoel2esw12DoLinkAddBridgeMode_Object = MibScalar
gepoel2esw12DoLinkAddBridgeMode = _Gepoel2esw12DoLinkAddBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 3, 13),
    _Gepoel2esw12DoLinkAddBridgeMode_Type()
)
gepoel2esw12DoLinkAddBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DoLinkAddBridgeMode.setStatus("current")
_Gepoel2esw12LinkVlanTagDel_ObjectIdentity = ObjectIdentity
gepoel2esw12LinkVlanTagDel = _Gepoel2esw12LinkVlanTagDel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4)
)


class _Gepoel2esw12LinkDelVlanOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkDelVlanOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkDelVlanOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDelVlanOltPort_Object = MibScalar
gepoel2esw12LinkDelVlanOltPort = _Gepoel2esw12LinkDelVlanOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4, 1),
    _Gepoel2esw12LinkDelVlanOltPort_Type()
)
gepoel2esw12LinkDelVlanOltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelVlanOltPort.setStatus("current")
_Gepoel2esw12LinkDelVlanMacAddress_Type = MacAddress
_Gepoel2esw12LinkDelVlanMacAddress_Object = MibScalar
gepoel2esw12LinkDelVlanMacAddress = _Gepoel2esw12LinkDelVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4, 2),
    _Gepoel2esw12LinkDelVlanMacAddress_Type()
)
gepoel2esw12LinkDelVlanMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelVlanMacAddress.setStatus("current")


class _Gepoel2esw12LinkDelVlan_Type(Integer32):
    """Custom type gepoel2esw12LinkDelVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gepoel2esw12LinkDelVlan_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDelVlan_Object = MibScalar
gepoel2esw12LinkDelVlan = _Gepoel2esw12LinkDelVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4, 3),
    _Gepoel2esw12LinkDelVlan_Type()
)
gepoel2esw12LinkDelVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelVlan.setStatus("current")


class _Gepoel2esw12LinkDelMaxVlan_Type(Integer32):
    """Custom type gepoel2esw12LinkDelMaxVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gepoel2esw12LinkDelMaxVlan_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDelMaxVlan_Object = MibScalar
gepoel2esw12LinkDelMaxVlan = _Gepoel2esw12LinkDelMaxVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4, 4),
    _Gepoel2esw12LinkDelMaxVlan_Type()
)
gepoel2esw12LinkDelMaxVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelMaxVlan.setStatus("current")


class _Gepoel2esw12LinkDelUpstreamCos_Type(Integer32):
    """Custom type gepoel2esw12LinkDelUpstreamCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12LinkDelUpstreamCos_Type.__name__ = "Integer32"
_Gepoel2esw12LinkDelUpstreamCos_Object = MibScalar
gepoel2esw12LinkDelUpstreamCos = _Gepoel2esw12LinkDelUpstreamCos_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4, 5),
    _Gepoel2esw12LinkDelUpstreamCos_Type()
)
gepoel2esw12LinkDelUpstreamCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkDelUpstreamCos.setStatus("current")


class _Gepoel2esw12DoLinkDelVlan_Type(Integer32):
    """Custom type gepoel2esw12DoLinkDelVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DoLinkDelVlan_Type.__name__ = "Integer32"
_Gepoel2esw12DoLinkDelVlan_Object = MibScalar
gepoel2esw12DoLinkDelVlan = _Gepoel2esw12DoLinkDelVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 3, 4, 6),
    _Gepoel2esw12DoLinkDelVlan_Type()
)
gepoel2esw12DoLinkDelVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DoLinkDelVlan.setStatus("current")
_Gepoel2esw12LinkStatistics_ObjectIdentity = ObjectIdentity
gepoel2esw12LinkStatistics = _Gepoel2esw12LinkStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4)
)
_Gepoel2esw12LinkStatisticsOltSideTable_Object = MibTable
gepoel2esw12LinkStatisticsOltSideTable = _Gepoel2esw12LinkStatisticsOltSideTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideTable.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideEntry_Object = MibTableRow
gepoel2esw12LinkStatisticsOltSideEntry = _Gepoel2esw12LinkStatisticsOltSideEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1)
)
gepoel2esw12LinkStatisticsOltSideEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkStaticOltSideOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkStaticOltSideLinkMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkStatisticsOltSideIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideEntry.setStatus("current")


class _Gepoel2esw12LinkStaticOltSideOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkStaticOltSideOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkStaticOltSideOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkStaticOltSideOltPort_Object = MibTableColumn
gepoel2esw12LinkStaticOltSideOltPort = _Gepoel2esw12LinkStaticOltSideOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 1),
    _Gepoel2esw12LinkStaticOltSideOltPort_Type()
)
gepoel2esw12LinkStaticOltSideOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStaticOltSideOltPort.setStatus("current")
_Gepoel2esw12LinkStaticOltSideLinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkStaticOltSideLinkMacAddress_Object = MibTableColumn
gepoel2esw12LinkStaticOltSideLinkMacAddress = _Gepoel2esw12LinkStaticOltSideLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 2),
    _Gepoel2esw12LinkStaticOltSideLinkMacAddress_Type()
)
gepoel2esw12LinkStaticOltSideLinkMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStaticOltSideLinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkStatisticsOltSideIndex_Type(Integer32):
    """Custom type gepoel2esw12LinkStatisticsOltSideIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12LinkStatisticsOltSideIndex_Type.__name__ = "Integer32"
_Gepoel2esw12LinkStatisticsOltSideIndex_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideIndex = _Gepoel2esw12LinkStatisticsOltSideIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 3),
    _Gepoel2esw12LinkStatisticsOltSideIndex_Type()
)
gepoel2esw12LinkStatisticsOltSideIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideIndex.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideBytes_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideBytes_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideBytes = _Gepoel2esw12LinkStatisticsOltSideBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 4),
    _Gepoel2esw12LinkStatisticsOltSideBytes_Type()
)
gepoel2esw12LinkStatisticsOltSideBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideBytes.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideTotalFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideTotalFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideTotalFrame = _Gepoel2esw12LinkStatisticsOltSideTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 5),
    _Gepoel2esw12LinkStatisticsOltSideTotalFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideTotalFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideUnicastFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideUnicastFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideUnicastFrame = _Gepoel2esw12LinkStatisticsOltSideUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 6),
    _Gepoel2esw12LinkStatisticsOltSideUnicastFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideUnicastFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideBroadcastFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideBroadcastFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideBroadcastFrame = _Gepoel2esw12LinkStatisticsOltSideBroadcastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 7),
    _Gepoel2esw12LinkStatisticsOltSideBroadcastFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideBroadcastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideBroadcastFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMulticastFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMulticastFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMulticastFrame = _Gepoel2esw12LinkStatisticsOltSideMulticastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 8),
    _Gepoel2esw12LinkStatisticsOltSideMulticastFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideMulticastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMulticastFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideUndersizeFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideUndersizeFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideUndersizeFrame = _Gepoel2esw12LinkStatisticsOltSideUndersizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 9),
    _Gepoel2esw12LinkStatisticsOltSideUndersizeFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideUndersizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideUndersizeFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideOversizedFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideOversizedFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideOversizedFrame = _Gepoel2esw12LinkStatisticsOltSideOversizedFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 10),
    _Gepoel2esw12LinkStatisticsOltSideOversizedFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideOversizedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideOversizedFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideFCSErrors_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideFCSErrors_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideFCSErrors = _Gepoel2esw12LinkStatisticsOltSideFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 11),
    _Gepoel2esw12LinkStatisticsOltSideFCSErrors_Type()
)
gepoel2esw12LinkStatisticsOltSideFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideFCSErrors.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide64OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide64OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide64OctetFrame = _Gepoel2esw12LinkStatisticsOltSide64OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 12),
    _Gepoel2esw12LinkStatisticsOltSide64OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide64OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide64OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide65to127OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide65to127OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide65to127OctetFrame = _Gepoel2esw12LinkStatisticsOltSide65to127OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 13),
    _Gepoel2esw12LinkStatisticsOltSide65to127OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide65to127OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide65to127OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide128to255OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide128to255OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide128to255OctetFrame = _Gepoel2esw12LinkStatisticsOltSide128to255OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 14),
    _Gepoel2esw12LinkStatisticsOltSide128to255OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide128to255OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide128to255OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide256to511OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide256to511OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide256to511OctetFrame = _Gepoel2esw12LinkStatisticsOltSide256to511OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 15),
    _Gepoel2esw12LinkStatisticsOltSide256to511OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide256to511OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide256to511OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame = _Gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 16),
    _Gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame = _Gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 17),
    _Gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSide1519upOctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSide1519upOctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSide1519upOctetFrame = _Gepoel2esw12LinkStatisticsOltSide1519upOctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 18),
    _Gepoel2esw12LinkStatisticsOltSide1519upOctetFrame_Type()
)
gepoel2esw12LinkStatisticsOltSide1519upOctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSide1519upOctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideFramesDropped_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideFramesDropped_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideFramesDropped = _Gepoel2esw12LinkStatisticsOltSideFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 19),
    _Gepoel2esw12LinkStatisticsOltSideFramesDropped_Type()
)
gepoel2esw12LinkStatisticsOltSideFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideFramesDropped.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMPCPFrames_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMPCPFrames_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMPCPFrames = _Gepoel2esw12LinkStatisticsOltSideMPCPFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 20),
    _Gepoel2esw12LinkStatisticsOltSideMPCPFrames_Type()
)
gepoel2esw12LinkStatisticsOltSideMPCPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMPCPFrames.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMPCPBytes_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMPCPBytes_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMPCPBytes = _Gepoel2esw12LinkStatisticsOltSideMPCPBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 21),
    _Gepoel2esw12LinkStatisticsOltSideMPCPBytes_Type()
)
gepoel2esw12LinkStatisticsOltSideMPCPBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMPCPBytes.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideReportFrames_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideReportFrames_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideReportFrames = _Gepoel2esw12LinkStatisticsOltSideReportFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 22),
    _Gepoel2esw12LinkStatisticsOltSideReportFrames_Type()
)
gepoel2esw12LinkStatisticsOltSideReportFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideReportFrames.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideReportBytes_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideReportBytes_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideReportBytes = _Gepoel2esw12LinkStatisticsOltSideReportBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 23),
    _Gepoel2esw12LinkStatisticsOltSideReportBytes_Type()
)
gepoel2esw12LinkStatisticsOltSideReportBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideReportBytes.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideOAMFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideOAMFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideOAMFrame = _Gepoel2esw12LinkStatisticsOltSideOAMFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 24),
    _Gepoel2esw12LinkStatisticsOltSideOAMFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideOAMFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideOAMFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideOAMBytes_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideOAMBytes_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideOAMBytes = _Gepoel2esw12LinkStatisticsOltSideOAMBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 25),
    _Gepoel2esw12LinkStatisticsOltSideOAMBytes_Type()
)
gepoel2esw12LinkStatisticsOltSideOAMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideOAMBytes.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest = _Gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 26),
    _Gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest_Type()
)
gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck = _Gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 27),
    _Gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck_Type()
)
gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame = _Gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 28),
    _Gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame = _Gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 29),
    _Gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame_Type()
)
gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideLineCodeError_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideLineCodeError_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideLineCodeError = _Gepoel2esw12LinkStatisticsOltSideLineCodeError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 30),
    _Gepoel2esw12LinkStatisticsOltSideLineCodeError_Type()
)
gepoel2esw12LinkStatisticsOltSideLineCodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideLineCodeError.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax = _Gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 31),
    _Gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax_Type()
)
gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideLaserPower_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideLaserPower_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideLaserPower = _Gepoel2esw12LinkStatisticsOltSideLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 32),
    _Gepoel2esw12LinkStatisticsOltSideLaserPower_Type()
)
gepoel2esw12LinkStatisticsOltSideLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideLaserPower.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideGateFrames_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideGateFrames_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideGateFrames = _Gepoel2esw12LinkStatisticsOltSideGateFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 33),
    _Gepoel2esw12LinkStatisticsOltSideGateFrames_Type()
)
gepoel2esw12LinkStatisticsOltSideGateFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideGateFrames.setStatus("current")
_Gepoel2esw12LinkStatisticsOltSideGateBytes_Type = Counter64
_Gepoel2esw12LinkStatisticsOltSideGateBytes_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideGateBytes = _Gepoel2esw12LinkStatisticsOltSideGateBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 34),
    _Gepoel2esw12LinkStatisticsOltSideGateBytes_Type()
)
gepoel2esw12LinkStatisticsOltSideGateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideGateBytes.setStatus("current")


class _Gepoel2esw12LinkStatisticsOltSideClear_Type(Integer32):
    """Custom type gepoel2esw12LinkStatisticsOltSideClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkStatisticsOltSideClear_Type.__name__ = "Integer32"
_Gepoel2esw12LinkStatisticsOltSideClear_Object = MibTableColumn
gepoel2esw12LinkStatisticsOltSideClear = _Gepoel2esw12LinkStatisticsOltSideClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 1, 1, 35),
    _Gepoel2esw12LinkStatisticsOltSideClear_Type()
)
gepoel2esw12LinkStatisticsOltSideClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOltSideClear.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideTable_Object = MibTable
gepoel2esw12LinkStatisticsOnuSideTable = _Gepoel2esw12LinkStatisticsOnuSideTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideTable.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideEntry_Object = MibTableRow
gepoel2esw12LinkStatisticsOnuSideEntry = _Gepoel2esw12LinkStatisticsOnuSideEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1)
)
gepoel2esw12LinkStatisticsOnuSideEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkStaticOnuSideOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkStaticOnuSideLinkMacAddress"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkStatisticsOnuSideIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideEntry.setStatus("current")


class _Gepoel2esw12LinkStaticOnuSideOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkStaticOnuSideOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkStaticOnuSideOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkStaticOnuSideOltPort_Object = MibTableColumn
gepoel2esw12LinkStaticOnuSideOltPort = _Gepoel2esw12LinkStaticOnuSideOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 1),
    _Gepoel2esw12LinkStaticOnuSideOltPort_Type()
)
gepoel2esw12LinkStaticOnuSideOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStaticOnuSideOltPort.setStatus("current")
_Gepoel2esw12LinkStaticOnuSideLinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkStaticOnuSideLinkMacAddress_Object = MibTableColumn
gepoel2esw12LinkStaticOnuSideLinkMacAddress = _Gepoel2esw12LinkStaticOnuSideLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 2),
    _Gepoel2esw12LinkStaticOnuSideLinkMacAddress_Type()
)
gepoel2esw12LinkStaticOnuSideLinkMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStaticOnuSideLinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkStatisticsOnuSideIndex_Type(Integer32):
    """Custom type gepoel2esw12LinkStatisticsOnuSideIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gepoel2esw12LinkStatisticsOnuSideIndex_Type.__name__ = "Integer32"
_Gepoel2esw12LinkStatisticsOnuSideIndex_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideIndex = _Gepoel2esw12LinkStatisticsOnuSideIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 3),
    _Gepoel2esw12LinkStatisticsOnuSideIndex_Type()
)
gepoel2esw12LinkStatisticsOnuSideIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideIndex.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideBytes_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideBytes_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideBytes = _Gepoel2esw12LinkStatisticsOnuSideBytes_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 4),
    _Gepoel2esw12LinkStatisticsOnuSideBytes_Type()
)
gepoel2esw12LinkStatisticsOnuSideBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideBytes.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideTotalFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideTotalFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideTotalFrame = _Gepoel2esw12LinkStatisticsOnuSideTotalFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 5),
    _Gepoel2esw12LinkStatisticsOnuSideTotalFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSideTotalFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideTotalFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideUnicastFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideUnicastFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideUnicastFrame = _Gepoel2esw12LinkStatisticsOnuSideUnicastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 6),
    _Gepoel2esw12LinkStatisticsOnuSideUnicastFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSideUnicastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideUnicastFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideBroadcastFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideBroadcastFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideBroadcastFrame = _Gepoel2esw12LinkStatisticsOnuSideBroadcastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 7),
    _Gepoel2esw12LinkStatisticsOnuSideBroadcastFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSideBroadcastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideBroadcastFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMulticastFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMulticastFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMulticastFrame = _Gepoel2esw12LinkStatisticsOnuSideMulticastFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 8),
    _Gepoel2esw12LinkStatisticsOnuSideMulticastFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSideMulticastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMulticastFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide64OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide64OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide64OctetFrame = _Gepoel2esw12LinkStatisticsOnuSide64OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 9),
    _Gepoel2esw12LinkStatisticsOnuSide64OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide64OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide64OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame = _Gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 10),
    _Gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame = _Gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 11),
    _Gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame = _Gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 12),
    _Gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame = _Gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 13),
    _Gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame = _Gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 14),
    _Gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame = _Gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 15),
    _Gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideUndersizeFrame_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideUndersizeFrame_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideUndersizeFrame = _Gepoel2esw12LinkStatisticsOnuSideUndersizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 16),
    _Gepoel2esw12LinkStatisticsOnuSideUndersizeFrame_Type()
)
gepoel2esw12LinkStatisticsOnuSideUndersizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideUndersizeFrame.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideFCSErrors_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideFCSErrors_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideFCSErrors = _Gepoel2esw12LinkStatisticsOnuSideFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 17),
    _Gepoel2esw12LinkStatisticsOnuSideFCSErrors_Type()
)
gepoel2esw12LinkStatisticsOnuSideFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideFCSErrors.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideBytesDropped_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideBytesDropped_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideBytesDropped = _Gepoel2esw12LinkStatisticsOnuSideBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 18),
    _Gepoel2esw12LinkStatisticsOnuSideBytesDropped_Type()
)
gepoel2esw12LinkStatisticsOnuSideBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideBytesDropped.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideFramesDropped_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideFramesDropped_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideFramesDropped = _Gepoel2esw12LinkStatisticsOnuSideFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 19),
    _Gepoel2esw12LinkStatisticsOnuSideFramesDropped_Type()
)
gepoel2esw12LinkStatisticsOnuSideFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideFramesDropped.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideBytesDelayed_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideBytesDelayed_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideBytesDelayed = _Gepoel2esw12LinkStatisticsOnuSideBytesDelayed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 20),
    _Gepoel2esw12LinkStatisticsOnuSideBytesDelayed_Type()
)
gepoel2esw12LinkStatisticsOnuSideBytesDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideBytesDelayed.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMaximumDelayed_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMaximumDelayed_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMaximumDelayed = _Gepoel2esw12LinkStatisticsOnuSideMaximumDelayed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 21),
    _Gepoel2esw12LinkStatisticsOnuSideMaximumDelayed_Type()
)
gepoel2esw12LinkStatisticsOnuSideMaximumDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMaximumDelayed.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideDelayThreshold_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideDelayThreshold_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideDelayThreshold = _Gepoel2esw12LinkStatisticsOnuSideDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 22),
    _Gepoel2esw12LinkStatisticsOnuSideDelayThreshold_Type()
)
gepoel2esw12LinkStatisticsOnuSideDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideDelayThreshold.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideOAMFrames_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideOAMFrames_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideOAMFrames = _Gepoel2esw12LinkStatisticsOnuSideOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 23),
    _Gepoel2esw12LinkStatisticsOnuSideOAMFrames_Type()
)
gepoel2esw12LinkStatisticsOnuSideOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideOAMFrames.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideErroredFrames_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideErroredFrames_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideErroredFrames = _Gepoel2esw12LinkStatisticsOnuSideErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 24),
    _Gepoel2esw12LinkStatisticsOnuSideErroredFrames_Type()
)
gepoel2esw12LinkStatisticsOnuSideErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideErroredFrames.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods = _Gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 25),
    _Gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods_Type()
)
gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMPCPGates_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMPCPGates_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMPCPGates = _Gepoel2esw12LinkStatisticsOnuSideMPCPGates_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 26),
    _Gepoel2esw12LinkStatisticsOnuSideMPCPGates_Type()
)
gepoel2esw12LinkStatisticsOnuSideMPCPGates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMPCPGates.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMPCPRegister_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMPCPRegister_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMPCPRegister = _Gepoel2esw12LinkStatisticsOnuSideMPCPRegister_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 27),
    _Gepoel2esw12LinkStatisticsOnuSideMPCPRegister_Type()
)
gepoel2esw12LinkStatisticsOnuSideMPCPRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMPCPRegister.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMPCPReport_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMPCPReport_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMPCPReport = _Gepoel2esw12LinkStatisticsOnuSideMPCPReport_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 28),
    _Gepoel2esw12LinkStatisticsOnuSideMPCPReport_Type()
)
gepoel2esw12LinkStatisticsOnuSideMPCPReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMPCPReport.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMPCPRequest_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMPCPRequest_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMPCPRequest = _Gepoel2esw12LinkStatisticsOnuSideMPCPRequest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 29),
    _Gepoel2esw12LinkStatisticsOnuSideMPCPRequest_Type()
)
gepoel2esw12LinkStatisticsOnuSideMPCPRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMPCPRequest.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck = _Gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 30),
    _Gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck_Type()
)
gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck.setStatus("current")
_Gepoel2esw12LinkStatisticsOnuSideUnused_Type = Counter64
_Gepoel2esw12LinkStatisticsOnuSideUnused_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideUnused = _Gepoel2esw12LinkStatisticsOnuSideUnused_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 31),
    _Gepoel2esw12LinkStatisticsOnuSideUnused_Type()
)
gepoel2esw12LinkStatisticsOnuSideUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideUnused.setStatus("current")


class _Gepoel2esw12LinkStatisticsOnuSideClear_Type(Integer32):
    """Custom type gepoel2esw12LinkStatisticsOnuSideClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkStatisticsOnuSideClear_Type.__name__ = "Integer32"
_Gepoel2esw12LinkStatisticsOnuSideClear_Object = MibTableColumn
gepoel2esw12LinkStatisticsOnuSideClear = _Gepoel2esw12LinkStatisticsOnuSideClear_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 4, 2, 1, 32),
    _Gepoel2esw12LinkStatisticsOnuSideClear_Type()
)
gepoel2esw12LinkStatisticsOnuSideClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkStatisticsOnuSideClear.setStatus("current")
_Gepoel2esw12LinkMiscOperationTable_Object = MibTable
gepoel2esw12LinkMiscOperationTable = _Gepoel2esw12LinkMiscOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 5)
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkMiscOperationTable.setStatus("current")
_Gepoel2esw12LinkMiscOperationEntry_Object = MibTableRow
gepoel2esw12LinkMiscOperationEntry = _Gepoel2esw12LinkMiscOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 5, 1)
)
gepoel2esw12LinkMiscOperationEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkMiscOptOltPort"),
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12LinkMiscOptLinkMacAddress"),
)
if mibBuilder.loadTexts:
    gepoel2esw12LinkMiscOperationEntry.setStatus("current")


class _Gepoel2esw12LinkMiscOptOltPort_Type(Integer32):
    """Custom type gepoel2esw12LinkMiscOptOltPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Gepoel2esw12LinkMiscOptOltPort_Type.__name__ = "Integer32"
_Gepoel2esw12LinkMiscOptOltPort_Object = MibTableColumn
gepoel2esw12LinkMiscOptOltPort = _Gepoel2esw12LinkMiscOptOltPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 5, 1, 1),
    _Gepoel2esw12LinkMiscOptOltPort_Type()
)
gepoel2esw12LinkMiscOptOltPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMiscOptOltPort.setStatus("current")
_Gepoel2esw12LinkMiscOptLinkMacAddress_Type = MacAddress
_Gepoel2esw12LinkMiscOptLinkMacAddress_Object = MibTableColumn
gepoel2esw12LinkMiscOptLinkMacAddress = _Gepoel2esw12LinkMiscOptLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 5, 1, 2),
    _Gepoel2esw12LinkMiscOptLinkMacAddress_Type()
)
gepoel2esw12LinkMiscOptLinkMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gepoel2esw12LinkMiscOptLinkMacAddress.setStatus("current")


class _Gepoel2esw12LinkBlockState_Type(Integer32):
    """Custom type gepoel2esw12LinkBlockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12LinkBlockState_Type.__name__ = "Integer32"
_Gepoel2esw12LinkBlockState_Object = MibTableColumn
gepoel2esw12LinkBlockState = _Gepoel2esw12LinkBlockState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 4, 5, 1, 3),
    _Gepoel2esw12LinkBlockState_Type()
)
gepoel2esw12LinkBlockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12LinkBlockState.setStatus("current")
_Gepoel2esw12Configuration_ObjectIdentity = ObjectIdentity
gepoel2esw12Configuration = _Gepoel2esw12Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5)
)
_Gepoel2esw12TrapEventSeverity_ObjectIdentity = ObjectIdentity
gepoel2esw12TrapEventSeverity = _Gepoel2esw12TrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1)
)


class _Gepoel2esw12TrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityAccessMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityAccessMgmt_Object = MibScalar
gepoel2esw12TrapEventSeverityAccessMgmt = _Gepoel2esw12TrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 1),
    _Gepoel2esw12TrapEventSeverityAccessMgmt_Type()
)
gepoel2esw12TrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityAccessMgmt.setStatus("current")


class _Gepoel2esw12TrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityAuthFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityAuthFailed_Object = MibScalar
gepoel2esw12TrapEventSeverityAuthFailed = _Gepoel2esw12TrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 2),
    _Gepoel2esw12TrapEventSeverityAuthFailed_Type()
)
gepoel2esw12TrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityAuthFailed.setStatus("current")


class _Gepoel2esw12TrapEventSeverityColdStart_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityColdStart_Object = MibScalar
gepoel2esw12TrapEventSeverityColdStart = _Gepoel2esw12TrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 3),
    _Gepoel2esw12TrapEventSeverityColdStart_Type()
)
gepoel2esw12TrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityColdStart.setStatus("current")


class _Gepoel2esw12TrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityConfigInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityConfigInfo_Object = MibScalar
gepoel2esw12TrapEventSeverityConfigInfo = _Gepoel2esw12TrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 4),
    _Gepoel2esw12TrapEventSeverityConfigInfo_Type()
)
gepoel2esw12TrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityConfigInfo.setStatus("current")


class _Gepoel2esw12TrapEventSeverityDyingGaspPowerFailure_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityDyingGaspPowerFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityDyingGaspPowerFailure_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityDyingGaspPowerFailure_Object = MibScalar
gepoel2esw12TrapEventSeverityDyingGaspPowerFailure = _Gepoel2esw12TrapEventSeverityDyingGaspPowerFailure_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 5),
    _Gepoel2esw12TrapEventSeverityDyingGaspPowerFailure_Type()
)
gepoel2esw12TrapEventSeverityDyingGaspPowerFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityDyingGaspPowerFailure.setStatus("current")


class _Gepoel2esw12TrapEventSeverityEPONLinkDown_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityEPONLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityEPONLinkDown_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityEPONLinkDown_Object = MibScalar
gepoel2esw12TrapEventSeverityEPONLinkDown = _Gepoel2esw12TrapEventSeverityEPONLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 6),
    _Gepoel2esw12TrapEventSeverityEPONLinkDown_Type()
)
gepoel2esw12TrapEventSeverityEPONLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityEPONLinkDown.setStatus("current")


class _Gepoel2esw12TrapEventSeverityEPONLinkUp_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityEPONLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityEPONLinkUp_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityEPONLinkUp_Object = MibScalar
gepoel2esw12TrapEventSeverityEPONLinkUp = _Gepoel2esw12TrapEventSeverityEPONLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 7),
    _Gepoel2esw12TrapEventSeverityEPONLinkUp_Type()
)
gepoel2esw12TrapEventSeverityEPONLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityEPONLinkUp.setStatus("current")


class _Gepoel2esw12TrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityFirmwareUpgrade_Object = MibScalar
gepoel2esw12TrapEventSeverityFirmwareUpgrade = _Gepoel2esw12TrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 8),
    _Gepoel2esw12TrapEventSeverityFirmwareUpgrade_Type()
)
gepoel2esw12TrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Gepoel2esw12TrapEventSeverityJumboFrameReceivedError_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityJumboFrameReceivedError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityJumboFrameReceivedError_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityJumboFrameReceivedError_Object = MibScalar
gepoel2esw12TrapEventSeverityJumboFrameReceivedError = _Gepoel2esw12TrapEventSeverityJumboFrameReceivedError_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 9),
    _Gepoel2esw12TrapEventSeverityJumboFrameReceivedError_Type()
)
gepoel2esw12TrapEventSeverityJumboFrameReceivedError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityJumboFrameReceivedError.setStatus("current")


class _Gepoel2esw12TrapEventSeverityKeyExchangeFailure_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityKeyExchangeFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityKeyExchangeFailure_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityKeyExchangeFailure_Object = MibScalar
gepoel2esw12TrapEventSeverityKeyExchangeFailure = _Gepoel2esw12TrapEventSeverityKeyExchangeFailure_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 10),
    _Gepoel2esw12TrapEventSeverityKeyExchangeFailure_Type()
)
gepoel2esw12TrapEventSeverityKeyExchangeFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityKeyExchangeFailure.setStatus("current")


class _Gepoel2esw12TrapEventSeverityLogin_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityLogin_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityLogin_Object = MibScalar
gepoel2esw12TrapEventSeverityLogin = _Gepoel2esw12TrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 11),
    _Gepoel2esw12TrapEventSeverityLogin_Type()
)
gepoel2esw12TrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityLogin.setStatus("current")


class _Gepoel2esw12TrapEventSeverityLogout_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityLogout_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityLogout_Object = MibScalar
gepoel2esw12TrapEventSeverityLogout = _Gepoel2esw12TrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 12),
    _Gepoel2esw12TrapEventSeverityLogout_Type()
)
gepoel2esw12TrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityLogout.setStatus("current")


class _Gepoel2esw12TrapEventSeverityLoopback_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityLoopback_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityLoopback_Object = MibScalar
gepoel2esw12TrapEventSeverityLoopback = _Gepoel2esw12TrapEventSeverityLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 13),
    _Gepoel2esw12TrapEventSeverityLoopback_Type()
)
gepoel2esw12TrapEventSeverityLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityLoopback.setStatus("current")


class _Gepoel2esw12TrapEventSeverityMACLearningTableOverflow_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityMACLearningTableOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityMACLearningTableOverflow_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityMACLearningTableOverflow_Object = MibScalar
gepoel2esw12TrapEventSeverityMACLearningTableOverflow = _Gepoel2esw12TrapEventSeverityMACLearningTableOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 14),
    _Gepoel2esw12TrapEventSeverityMACLearningTableOverflow_Type()
)
gepoel2esw12TrapEventSeverityMACLearningTableOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityMACLearningTableOverflow.setStatus("current")


class _Gepoel2esw12TrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityMgmtIPChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityMgmtIPChange_Object = MibScalar
gepoel2esw12TrapEventSeverityMgmtIPChange = _Gepoel2esw12TrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 15),
    _Gepoel2esw12TrapEventSeverityMgmtIPChange_Type()
)
gepoel2esw12TrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityMgmtIPChange.setStatus("current")


class _Gepoel2esw12TrapEventSeverityNumberOfLinksExceeded_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityNumberOfLinksExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityNumberOfLinksExceeded_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityNumberOfLinksExceeded_Object = MibScalar
gepoel2esw12TrapEventSeverityNumberOfLinksExceeded = _Gepoel2esw12TrapEventSeverityNumberOfLinksExceeded_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 16),
    _Gepoel2esw12TrapEventSeverityNumberOfLinksExceeded_Type()
)
gepoel2esw12TrapEventSeverityNumberOfLinksExceeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityNumberOfLinksExceeded.setStatus("current")


class _Gepoel2esw12TrapEventSeverityOLTBad_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityOLTBad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityOLTBad_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityOLTBad_Object = MibScalar
gepoel2esw12TrapEventSeverityOLTBad = _Gepoel2esw12TrapEventSeverityOLTBad_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 17),
    _Gepoel2esw12TrapEventSeverityOLTBad_Type()
)
gepoel2esw12TrapEventSeverityOLTBad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityOLTBad.setStatus("current")


class _Gepoel2esw12TrapEventSeverityONUPowerAbnormal_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityONUPowerAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityONUPowerAbnormal_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityONUPowerAbnormal_Object = MibScalar
gepoel2esw12TrapEventSeverityONUPowerAbnormal = _Gepoel2esw12TrapEventSeverityONUPowerAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 18),
    _Gepoel2esw12TrapEventSeverityONUPowerAbnormal_Type()
)
gepoel2esw12TrapEventSeverityONUPowerAbnormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityONUPowerAbnormal.setStatus("current")


class _Gepoel2esw12TrapEventSeverityPasswdChange_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityPasswdChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityPasswdChange_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityPasswdChange_Object = MibScalar
gepoel2esw12TrapEventSeverityPasswdChange = _Gepoel2esw12TrapEventSeverityPasswdChange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 19),
    _Gepoel2esw12TrapEventSeverityPasswdChange_Type()
)
gepoel2esw12TrapEventSeverityPasswdChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityPasswdChange.setStatus("current")


class _Gepoel2esw12TrapEventSeverityQueueOverflow_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityQueueOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityQueueOverflow_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityQueueOverflow_Object = MibScalar
gepoel2esw12TrapEventSeverityQueueOverflow = _Gepoel2esw12TrapEventSeverityQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 20),
    _Gepoel2esw12TrapEventSeverityQueueOverflow_Type()
)
gepoel2esw12TrapEventSeverityQueueOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityQueueOverflow.setStatus("current")


class _Gepoel2esw12TrapEventSeverityStandardDyingGasp_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityStandardDyingGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityStandardDyingGasp_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityStandardDyingGasp_Object = MibScalar
gepoel2esw12TrapEventSeverityStandardDyingGasp = _Gepoel2esw12TrapEventSeverityStandardDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 21),
    _Gepoel2esw12TrapEventSeverityStandardDyingGasp_Type()
)
gepoel2esw12TrapEventSeverityStandardDyingGasp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityStandardDyingGasp.setStatus("current")


class _Gepoel2esw12TrapEventSeverityStandardLinkFault_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityStandardLinkFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityStandardLinkFault_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityStandardLinkFault_Object = MibScalar
gepoel2esw12TrapEventSeverityStandardLinkFault = _Gepoel2esw12TrapEventSeverityStandardLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 22),
    _Gepoel2esw12TrapEventSeverityStandardLinkFault_Type()
)
gepoel2esw12TrapEventSeverityStandardLinkFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityStandardLinkFault.setStatus("current")


class _Gepoel2esw12TrapEventSeverityStatisticsAlarm_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityStatisticsAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityStatisticsAlarm_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityStatisticsAlarm_Object = MibScalar
gepoel2esw12TrapEventSeverityStatisticsAlarm = _Gepoel2esw12TrapEventSeverityStatisticsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 23),
    _Gepoel2esw12TrapEventSeverityStatisticsAlarm_Type()
)
gepoel2esw12TrapEventSeverityStatisticsAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityStatisticsAlarm.setStatus("current")


class _Gepoel2esw12TrapEventSeverityUNILinkDown_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityUNILinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityUNILinkDown_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityUNILinkDown_Object = MibScalar
gepoel2esw12TrapEventSeverityUNILinkDown = _Gepoel2esw12TrapEventSeverityUNILinkDown_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 24),
    _Gepoel2esw12TrapEventSeverityUNILinkDown_Type()
)
gepoel2esw12TrapEventSeverityUNILinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityUNILinkDown.setStatus("current")


class _Gepoel2esw12TrapEventSeverityUNILinkUp_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityUNILinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityUNILinkUp_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityUNILinkUp_Object = MibScalar
gepoel2esw12TrapEventSeverityUNILinkUp = _Gepoel2esw12TrapEventSeverityUNILinkUp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 25),
    _Gepoel2esw12TrapEventSeverityUNILinkUp_Type()
)
gepoel2esw12TrapEventSeverityUNILinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityUNILinkUp.setStatus("current")


class _Gepoel2esw12TrapEventSeverityWarmStart_Type(Integer32):
    """Custom type gepoel2esw12TrapEventSeverityWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12TrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Gepoel2esw12TrapEventSeverityWarmStart_Object = MibScalar
gepoel2esw12TrapEventSeverityWarmStart = _Gepoel2esw12TrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 1, 26),
    _Gepoel2esw12TrapEventSeverityWarmStart_Type()
)
gepoel2esw12TrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TrapEventSeverityWarmStart.setStatus("current")
_Gepoel2esw12SMTP_ObjectIdentity = ObjectIdentity
gepoel2esw12SMTP = _Gepoel2esw12SMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2)
)
_Gepoel2esw12SMTPMailServer_Type = DisplayString
_Gepoel2esw12SMTPMailServer_Object = MibScalar
gepoel2esw12SMTPMailServer = _Gepoel2esw12SMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 1),
    _Gepoel2esw12SMTPMailServer_Type()
)
gepoel2esw12SMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPMailServer.setStatus("current")
_Gepoel2esw12SMTPUserName_Type = DisplayString
_Gepoel2esw12SMTPUserName_Object = MibScalar
gepoel2esw12SMTPUserName = _Gepoel2esw12SMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 2),
    _Gepoel2esw12SMTPUserName_Type()
)
gepoel2esw12SMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPUserName.setStatus("current")
_Gepoel2esw12SMTPPassword_Type = DisplayString
_Gepoel2esw12SMTPPassword_Object = MibScalar
gepoel2esw12SMTPPassword = _Gepoel2esw12SMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 3),
    _Gepoel2esw12SMTPPassword_Type()
)
gepoel2esw12SMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPPassword.setStatus("current")


class _Gepoel2esw12SMTPServeriryLevel_Type(Integer32):
    """Custom type gepoel2esw12SMTPServeriryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gepoel2esw12SMTPServeriryLevel_Type.__name__ = "Integer32"
_Gepoel2esw12SMTPServeriryLevel_Object = MibScalar
gepoel2esw12SMTPServeriryLevel = _Gepoel2esw12SMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 4),
    _Gepoel2esw12SMTPServeriryLevel_Type()
)
gepoel2esw12SMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPServeriryLevel.setStatus("current")
_Gepoel2esw12SMTPSender_Type = DisplayString
_Gepoel2esw12SMTPSender_Object = MibScalar
gepoel2esw12SMTPSender = _Gepoel2esw12SMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 5),
    _Gepoel2esw12SMTPSender_Type()
)
gepoel2esw12SMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPSender.setStatus("current")
_Gepoel2esw12SMTPReturnPath_Type = DisplayString
_Gepoel2esw12SMTPReturnPath_Object = MibScalar
gepoel2esw12SMTPReturnPath = _Gepoel2esw12SMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 6),
    _Gepoel2esw12SMTPReturnPath_Type()
)
gepoel2esw12SMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPReturnPath.setStatus("current")
_Gepoel2esw12SMTPEmailAddress1_Type = DisplayString
_Gepoel2esw12SMTPEmailAddress1_Object = MibScalar
gepoel2esw12SMTPEmailAddress1 = _Gepoel2esw12SMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 7),
    _Gepoel2esw12SMTPEmailAddress1_Type()
)
gepoel2esw12SMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPEmailAddress1.setStatus("current")
_Gepoel2esw12SMTPEmailAddress2_Type = DisplayString
_Gepoel2esw12SMTPEmailAddress2_Object = MibScalar
gepoel2esw12SMTPEmailAddress2 = _Gepoel2esw12SMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 8),
    _Gepoel2esw12SMTPEmailAddress2_Type()
)
gepoel2esw12SMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPEmailAddress2.setStatus("current")
_Gepoel2esw12SMTPEmailAddress3_Type = DisplayString
_Gepoel2esw12SMTPEmailAddress3_Object = MibScalar
gepoel2esw12SMTPEmailAddress3 = _Gepoel2esw12SMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 9),
    _Gepoel2esw12SMTPEmailAddress3_Type()
)
gepoel2esw12SMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPEmailAddress3.setStatus("current")
_Gepoel2esw12SMTPEmailAddress4_Type = DisplayString
_Gepoel2esw12SMTPEmailAddress4_Object = MibScalar
gepoel2esw12SMTPEmailAddress4 = _Gepoel2esw12SMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 10),
    _Gepoel2esw12SMTPEmailAddress4_Type()
)
gepoel2esw12SMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPEmailAddress4.setStatus("current")
_Gepoel2esw12SMTPEmailAddress5_Type = DisplayString
_Gepoel2esw12SMTPEmailAddress5_Object = MibScalar
gepoel2esw12SMTPEmailAddress5 = _Gepoel2esw12SMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 11),
    _Gepoel2esw12SMTPEmailAddress5_Type()
)
gepoel2esw12SMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPEmailAddress5.setStatus("current")
_Gepoel2esw12SMTPEmailAddress6_Type = DisplayString
_Gepoel2esw12SMTPEmailAddress6_Object = MibScalar
gepoel2esw12SMTPEmailAddress6 = _Gepoel2esw12SMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 5, 2, 12),
    _Gepoel2esw12SMTPEmailAddress6_Type()
)
gepoel2esw12SMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SMTPEmailAddress6.setStatus("current")
_Gepoel2esw12Security_ObjectIdentity = ObjectIdentity
gepoel2esw12Security = _Gepoel2esw12Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6)
)
_Gepoel2esw12AccessManagement_ObjectIdentity = ObjectIdentity
gepoel2esw12AccessManagement = _Gepoel2esw12AccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1)
)
_Gepoel2esw12AccessMgtConf_ObjectIdentity = ObjectIdentity
gepoel2esw12AccessMgtConf = _Gepoel2esw12AccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1)
)


class _Gepoel2esw12AccessMgtConfMode_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtConfMode_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtConfMode_Object = MibScalar
gepoel2esw12AccessMgtConfMode = _Gepoel2esw12AccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 1),
    _Gepoel2esw12AccessMgtConfMode_Type()
)
gepoel2esw12AccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtConfMode.setStatus("current")


class _Gepoel2esw12AccessMgtConfCreate_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtConfCreate_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtConfCreate_Object = MibScalar
gepoel2esw12AccessMgtConfCreate = _Gepoel2esw12AccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 2),
    _Gepoel2esw12AccessMgtConfCreate_Type()
)
gepoel2esw12AccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtConfCreate.setStatus("current")
_Gepoel2esw12AccessMgtConfTable_Object = MibTable
gepoel2esw12AccessMgtConfTable = _Gepoel2esw12AccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtConfTable.setStatus("current")
_Gepoel2esw12AccessMgtConfEntry_Object = MibTableRow
gepoel2esw12AccessMgtConfEntry = _Gepoel2esw12AccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1)
)
gepoel2esw12AccessMgtConfEntry.setIndexNames(
    (0, "PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12AccessMgtIndex"),
)
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtConfEntry.setStatus("current")


class _Gepoel2esw12AccessMgtIndex_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gepoel2esw12AccessMgtIndex_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtIndex_Object = MibTableColumn
gepoel2esw12AccessMgtIndex = _Gepoel2esw12AccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 1),
    _Gepoel2esw12AccessMgtIndex_Type()
)
gepoel2esw12AccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtIndex.setStatus("current")


class _Gepoel2esw12AccessMgtAddresstype_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtAddresstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtAddresstype_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtAddresstype_Object = MibTableColumn
gepoel2esw12AccessMgtAddresstype = _Gepoel2esw12AccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 2),
    _Gepoel2esw12AccessMgtAddresstype_Type()
)
gepoel2esw12AccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtAddresstype.setStatus("current")
_Gepoel2esw12AccessMgtStartIpAddress_Type = DisplayString
_Gepoel2esw12AccessMgtStartIpAddress_Object = MibTableColumn
gepoel2esw12AccessMgtStartIpAddress = _Gepoel2esw12AccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 3),
    _Gepoel2esw12AccessMgtStartIpAddress_Type()
)
gepoel2esw12AccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtStartIpAddress.setStatus("current")
_Gepoel2esw12AccessMgtEndIpAddress_Type = DisplayString
_Gepoel2esw12AccessMgtEndIpAddress_Object = MibTableColumn
gepoel2esw12AccessMgtEndIpAddress = _Gepoel2esw12AccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 4),
    _Gepoel2esw12AccessMgtEndIpAddress_Type()
)
gepoel2esw12AccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtEndIpAddress.setStatus("current")


class _Gepoel2esw12AccessMgtHttpHttps_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtHttpHttps_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtHttpHttps_Object = MibTableColumn
gepoel2esw12AccessMgtHttpHttps = _Gepoel2esw12AccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 5),
    _Gepoel2esw12AccessMgtHttpHttps_Type()
)
gepoel2esw12AccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtHttpHttps.setStatus("current")


class _Gepoel2esw12AccessMgtSNMP_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtSNMP_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtSNMP_Object = MibTableColumn
gepoel2esw12AccessMgtSNMP = _Gepoel2esw12AccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 6),
    _Gepoel2esw12AccessMgtSNMP_Type()
)
gepoel2esw12AccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtSNMP.setStatus("current")


class _Gepoel2esw12AccessMgtTelnetSSH_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtTelnetSSH_Object = MibTableColumn
gepoel2esw12AccessMgtTelnetSSH = _Gepoel2esw12AccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 7),
    _Gepoel2esw12AccessMgtTelnetSSH_Type()
)
gepoel2esw12AccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtTelnetSSH.setStatus("current")


class _Gepoel2esw12AccessMgtRowStatus_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gepoel2esw12AccessMgtRowStatus_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtRowStatus_Object = MibTableColumn
gepoel2esw12AccessMgtRowStatus = _Gepoel2esw12AccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 1, 3, 1, 8),
    _Gepoel2esw12AccessMgtRowStatus_Type()
)
gepoel2esw12AccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtRowStatus.setStatus("current")
_Gepoel2esw12AccessMgtStatistics_ObjectIdentity = ObjectIdentity
gepoel2esw12AccessMgtStatistics = _Gepoel2esw12AccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2)
)
_Gepoel2esw12HttpReceivedPkts_Type = Counter32
_Gepoel2esw12HttpReceivedPkts_Object = MibScalar
gepoel2esw12HttpReceivedPkts = _Gepoel2esw12HttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 1),
    _Gepoel2esw12HttpReceivedPkts_Type()
)
gepoel2esw12HttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HttpReceivedPkts.setStatus("current")
_Gepoel2esw12HttpAllowedPkts_Type = Counter32
_Gepoel2esw12HttpAllowedPkts_Object = MibScalar
gepoel2esw12HttpAllowedPkts = _Gepoel2esw12HttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 2),
    _Gepoel2esw12HttpAllowedPkts_Type()
)
gepoel2esw12HttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HttpAllowedPkts.setStatus("current")
_Gepoel2esw12HttpDiscardedPkts_Type = Counter32
_Gepoel2esw12HttpDiscardedPkts_Object = MibScalar
gepoel2esw12HttpDiscardedPkts = _Gepoel2esw12HttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 3),
    _Gepoel2esw12HttpDiscardedPkts_Type()
)
gepoel2esw12HttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HttpDiscardedPkts.setStatus("current")
_Gepoel2esw12HttpsReceivedPkts_Type = Counter32
_Gepoel2esw12HttpsReceivedPkts_Object = MibScalar
gepoel2esw12HttpsReceivedPkts = _Gepoel2esw12HttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 4),
    _Gepoel2esw12HttpsReceivedPkts_Type()
)
gepoel2esw12HttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HttpsReceivedPkts.setStatus("current")
_Gepoel2esw12HttpsAllowedPkts_Type = Counter32
_Gepoel2esw12HttpsAllowedPkts_Object = MibScalar
gepoel2esw12HttpsAllowedPkts = _Gepoel2esw12HttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 5),
    _Gepoel2esw12HttpsAllowedPkts_Type()
)
gepoel2esw12HttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HttpsAllowedPkts.setStatus("current")
_Gepoel2esw12HttpsDiscardedPkts_Type = Counter32
_Gepoel2esw12HttpsDiscardedPkts_Object = MibScalar
gepoel2esw12HttpsDiscardedPkts = _Gepoel2esw12HttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 6),
    _Gepoel2esw12HttpsDiscardedPkts_Type()
)
gepoel2esw12HttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12HttpsDiscardedPkts.setStatus("current")
_Gepoel2esw12SnmpReceivedPkts_Type = Counter32
_Gepoel2esw12SnmpReceivedPkts_Object = MibScalar
gepoel2esw12SnmpReceivedPkts = _Gepoel2esw12SnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 7),
    _Gepoel2esw12SnmpReceivedPkts_Type()
)
gepoel2esw12SnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SnmpReceivedPkts.setStatus("current")
_Gepoel2esw12SnmpAllowedPkts_Type = Counter32
_Gepoel2esw12SnmpAllowedPkts_Object = MibScalar
gepoel2esw12SnmpAllowedPkts = _Gepoel2esw12SnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 8),
    _Gepoel2esw12SnmpAllowedPkts_Type()
)
gepoel2esw12SnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SnmpAllowedPkts.setStatus("current")
_Gepoel2esw12SnmpDiscardedPkts_Type = Counter32
_Gepoel2esw12SnmpDiscardedPkts_Object = MibScalar
gepoel2esw12SnmpDiscardedPkts = _Gepoel2esw12SnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 9),
    _Gepoel2esw12SnmpDiscardedPkts_Type()
)
gepoel2esw12SnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SnmpDiscardedPkts.setStatus("current")
_Gepoel2esw12TelnetReceivedPkts_Type = Counter32
_Gepoel2esw12TelnetReceivedPkts_Object = MibScalar
gepoel2esw12TelnetReceivedPkts = _Gepoel2esw12TelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 10),
    _Gepoel2esw12TelnetReceivedPkts_Type()
)
gepoel2esw12TelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12TelnetReceivedPkts.setStatus("current")
_Gepoel2esw12TelnetAllowedPkts_Type = Counter32
_Gepoel2esw12TelnetAllowedPkts_Object = MibScalar
gepoel2esw12TelnetAllowedPkts = _Gepoel2esw12TelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 11),
    _Gepoel2esw12TelnetAllowedPkts_Type()
)
gepoel2esw12TelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12TelnetAllowedPkts.setStatus("current")
_Gepoel2esw12TelnetDiscardedPkts_Type = Counter32
_Gepoel2esw12TelnetDiscardedPkts_Object = MibScalar
gepoel2esw12TelnetDiscardedPkts = _Gepoel2esw12TelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 12),
    _Gepoel2esw12TelnetDiscardedPkts_Type()
)
gepoel2esw12TelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12TelnetDiscardedPkts.setStatus("current")
_Gepoel2esw12SSHReceivedPkts_Type = Counter32
_Gepoel2esw12SSHReceivedPkts_Object = MibScalar
gepoel2esw12SSHReceivedPkts = _Gepoel2esw12SSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 13),
    _Gepoel2esw12SSHReceivedPkts_Type()
)
gepoel2esw12SSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SSHReceivedPkts.setStatus("current")
_Gepoel2esw12SSHAllowedPkts_Type = Counter32
_Gepoel2esw12SSHAllowedPkts_Object = MibScalar
gepoel2esw12SSHAllowedPkts = _Gepoel2esw12SSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 14),
    _Gepoel2esw12SSHAllowedPkts_Type()
)
gepoel2esw12SSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SSHAllowedPkts.setStatus("current")
_Gepoel2esw12SSHDiscardedPkts_Type = Counter32
_Gepoel2esw12SSHDiscardedPkts_Object = MibScalar
gepoel2esw12SSHDiscardedPkts = _Gepoel2esw12SSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 15),
    _Gepoel2esw12SSHDiscardedPkts_Type()
)
gepoel2esw12SSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12SSHDiscardedPkts.setStatus("current")


class _Gepoel2esw12AccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type gepoel2esw12AccessMgtStatisticsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12AccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Gepoel2esw12AccessMgtStatisticsClearAll_Object = MibScalar
gepoel2esw12AccessMgtStatisticsClearAll = _Gepoel2esw12AccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 1, 2, 16),
    _Gepoel2esw12AccessMgtStatisticsClearAll_Type()
)
gepoel2esw12AccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12AccessMgtStatisticsClearAll.setStatus("current")
_Gepoel2esw12SSH_ObjectIdentity = ObjectIdentity
gepoel2esw12SSH = _Gepoel2esw12SSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 7)
)


class _Gepoel2esw12SSHMode_Type(Integer32):
    """Custom type gepoel2esw12SSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SSHMode_Type.__name__ = "Integer32"
_Gepoel2esw12SSHMode_Object = MibScalar
gepoel2esw12SSHMode = _Gepoel2esw12SSHMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 7, 1),
    _Gepoel2esw12SSHMode_Type()
)
gepoel2esw12SSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SSHMode.setStatus("current")
_Gepoel2esw12HTTPS_ObjectIdentity = ObjectIdentity
gepoel2esw12HTTPS = _Gepoel2esw12HTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 8)
)


class _Gepoel2esw12HTTPSMode_Type(Integer32):
    """Custom type gepoel2esw12HTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12HTTPSMode_Type.__name__ = "Integer32"
_Gepoel2esw12HTTPSMode_Object = MibScalar
gepoel2esw12HTTPSMode = _Gepoel2esw12HTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 8, 1),
    _Gepoel2esw12HTTPSMode_Type()
)
gepoel2esw12HTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12HTTPSMode.setStatus("current")


class _Gepoel2esw12HTTPSAutoRedirect_Type(Integer32):
    """Custom type gepoel2esw12HTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12HTTPSAutoRedirect_Type.__name__ = "Integer32"
_Gepoel2esw12HTTPSAutoRedirect_Object = MibScalar
gepoel2esw12HTTPSAutoRedirect = _Gepoel2esw12HTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 8, 2),
    _Gepoel2esw12HTTPSAutoRedirect_Type()
)
gepoel2esw12HTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12HTTPSAutoRedirect.setStatus("current")
_Gepoel2esw12AuthMethod_ObjectIdentity = ObjectIdentity
gepoel2esw12AuthMethod = _Gepoel2esw12AuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9)
)


class _Gepoel2esw12ConsoleAuthMethod_Type(Integer32):
    """Custom type gepoel2esw12ConsoleAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gepoel2esw12ConsoleAuthMethod_Type.__name__ = "Integer32"
_Gepoel2esw12ConsoleAuthMethod_Object = MibScalar
gepoel2esw12ConsoleAuthMethod = _Gepoel2esw12ConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 1),
    _Gepoel2esw12ConsoleAuthMethod_Type()
)
gepoel2esw12ConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12ConsoleAuthMethod.setStatus("current")


class _Gepoel2esw12ConsoleFallback_Type(Integer32):
    """Custom type gepoel2esw12ConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12ConsoleFallback_Type.__name__ = "Integer32"
_Gepoel2esw12ConsoleFallback_Object = MibScalar
gepoel2esw12ConsoleFallback = _Gepoel2esw12ConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 2),
    _Gepoel2esw12ConsoleFallback_Type()
)
gepoel2esw12ConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12ConsoleFallback.setStatus("current")


class _Gepoel2esw12TelnetAuthMethod_Type(Integer32):
    """Custom type gepoel2esw12TelnetAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gepoel2esw12TelnetAuthMethod_Type.__name__ = "Integer32"
_Gepoel2esw12TelnetAuthMethod_Object = MibScalar
gepoel2esw12TelnetAuthMethod = _Gepoel2esw12TelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 3),
    _Gepoel2esw12TelnetAuthMethod_Type()
)
gepoel2esw12TelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TelnetAuthMethod.setStatus("current")


class _Gepoel2esw12TelnetFallback_Type(Integer32):
    """Custom type gepoel2esw12TelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12TelnetFallback_Type.__name__ = "Integer32"
_Gepoel2esw12TelnetFallback_Object = MibScalar
gepoel2esw12TelnetFallback = _Gepoel2esw12TelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 4),
    _Gepoel2esw12TelnetFallback_Type()
)
gepoel2esw12TelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12TelnetFallback.setStatus("current")


class _Gepoel2esw12SshAuthMethod_Type(Integer32):
    """Custom type gepoel2esw12SshAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gepoel2esw12SshAuthMethod_Type.__name__ = "Integer32"
_Gepoel2esw12SshAuthMethod_Object = MibScalar
gepoel2esw12SshAuthMethod = _Gepoel2esw12SshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 5),
    _Gepoel2esw12SshAuthMethod_Type()
)
gepoel2esw12SshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SshAuthMethod.setStatus("current")


class _Gepoel2esw12SshFallback_Type(Integer32):
    """Custom type gepoel2esw12SshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SshFallback_Type.__name__ = "Integer32"
_Gepoel2esw12SshFallback_Object = MibScalar
gepoel2esw12SshFallback = _Gepoel2esw12SshFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 6),
    _Gepoel2esw12SshFallback_Type()
)
gepoel2esw12SshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SshFallback.setStatus("current")


class _Gepoel2esw12WebAuthMethod_Type(Integer32):
    """Custom type gepoel2esw12WebAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gepoel2esw12WebAuthMethod_Type.__name__ = "Integer32"
_Gepoel2esw12WebAuthMethod_Object = MibScalar
gepoel2esw12WebAuthMethod = _Gepoel2esw12WebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 7),
    _Gepoel2esw12WebAuthMethod_Type()
)
gepoel2esw12WebAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12WebAuthMethod.setStatus("current")


class _Gepoel2esw12WebFallback_Type(Integer32):
    """Custom type gepoel2esw12WebFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12WebFallback_Type.__name__ = "Integer32"
_Gepoel2esw12WebFallback_Object = MibScalar
gepoel2esw12WebFallback = _Gepoel2esw12WebFallback_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 6, 9, 8),
    _Gepoel2esw12WebFallback_Type()
)
gepoel2esw12WebFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12WebFallback.setStatus("current")
_Gepoel2esw12Maintenance_ObjectIdentity = ObjectIdentity
gepoel2esw12Maintenance = _Gepoel2esw12Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7)
)


class _Gepoel2esw12RestartDevice_Type(Integer32):
    """Custom type gepoel2esw12RestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12RestartDevice_Type.__name__ = "Integer32"
_Gepoel2esw12RestartDevice_Object = MibScalar
gepoel2esw12RestartDevice = _Gepoel2esw12RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 1),
    _Gepoel2esw12RestartDevice_Type()
)
gepoel2esw12RestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12RestartDevice.setStatus("current")
_Gepoel2esw12Firmware_ObjectIdentity = ObjectIdentity
gepoel2esw12Firmware = _Gepoel2esw12Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 2)
)
_Gepoel2esw12FirmwareIpAddress_Type = IpAddress
_Gepoel2esw12FirmwareIpAddress_Object = MibScalar
gepoel2esw12FirmwareIpAddress = _Gepoel2esw12FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 2, 1),
    _Gepoel2esw12FirmwareIpAddress_Type()
)
gepoel2esw12FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12FirmwareIpAddress.setStatus("current")
_Gepoel2esw12FirmwareFileName_Type = DisplayString
_Gepoel2esw12FirmwareFileName_Object = MibScalar
gepoel2esw12FirmwareFileName = _Gepoel2esw12FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 2, 2),
    _Gepoel2esw12FirmwareFileName_Type()
)
gepoel2esw12FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12FirmwareFileName.setStatus("current")


class _Gepoel2esw12DoFirmwareUpgrade_Type(Integer32):
    """Custom type gepoel2esw12DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gepoel2esw12DoFirmwareUpgrade_Object = MibScalar
gepoel2esw12DoFirmwareUpgrade = _Gepoel2esw12DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 2, 3),
    _Gepoel2esw12DoFirmwareUpgrade_Type()
)
gepoel2esw12DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DoFirmwareUpgrade.setStatus("current")
_Gepoel2esw12SaveOrRestore_ObjectIdentity = ObjectIdentity
gepoel2esw12SaveOrRestore = _Gepoel2esw12SaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 3)
)


class _Gepoel2esw12FactoryDefaults_Type(Integer32):
    """Custom type gepoel2esw12FactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12FactoryDefaults_Type.__name__ = "Integer32"
_Gepoel2esw12FactoryDefaults_Object = MibScalar
gepoel2esw12FactoryDefaults = _Gepoel2esw12FactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 3, 1),
    _Gepoel2esw12FactoryDefaults_Type()
)
gepoel2esw12FactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12FactoryDefaults.setStatus("current")


class _Gepoel2esw12SaveStart_Type(Integer32):
    """Custom type gepoel2esw12SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SaveStart_Type.__name__ = "Integer32"
_Gepoel2esw12SaveStart_Object = MibScalar
gepoel2esw12SaveStart = _Gepoel2esw12SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 3, 2),
    _Gepoel2esw12SaveStart_Type()
)
gepoel2esw12SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SaveStart.setStatus("current")


class _Gepoel2esw12SaveUser_Type(Integer32):
    """Custom type gepoel2esw12SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12SaveUser_Type.__name__ = "Integer32"
_Gepoel2esw12SaveUser_Object = MibScalar
gepoel2esw12SaveUser = _Gepoel2esw12SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 3, 3),
    _Gepoel2esw12SaveUser_Type()
)
gepoel2esw12SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12SaveUser.setStatus("current")


class _Gepoel2esw12RestoreUser_Type(Integer32):
    """Custom type gepoel2esw12RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12RestoreUser_Type.__name__ = "Integer32"
_Gepoel2esw12RestoreUser_Object = MibScalar
gepoel2esw12RestoreUser = _Gepoel2esw12RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 3, 4),
    _Gepoel2esw12RestoreUser_Type()
)
gepoel2esw12RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12RestoreUser.setStatus("current")
_Gepoel2esw12Diagnostics_ObjectIdentity = ObjectIdentity
gepoel2esw12Diagnostics = _Gepoel2esw12Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5)
)
_Gepoel2esw12PingIpAddress_Type = IpAddress
_Gepoel2esw12PingIpAddress_Object = MibScalar
gepoel2esw12PingIpAddress = _Gepoel2esw12PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 1),
    _Gepoel2esw12PingIpAddress_Type()
)
gepoel2esw12PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PingIpAddress.setStatus("current")


class _Gepoel2esw12PingSize_Type(Integer32):
    """Custom type gepoel2esw12PingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gepoel2esw12PingSize_Type.__name__ = "Integer32"
_Gepoel2esw12PingSize_Object = MibScalar
gepoel2esw12PingSize = _Gepoel2esw12PingSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 2),
    _Gepoel2esw12PingSize_Type()
)
gepoel2esw12PingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12PingSize.setStatus("current")


class _Gepoel2esw12DoPingConfig_Type(Integer32):
    """Custom type gepoel2esw12DoPingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DoPingConfig_Type.__name__ = "Integer32"
_Gepoel2esw12DoPingConfig_Object = MibScalar
gepoel2esw12DoPingConfig = _Gepoel2esw12DoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 3),
    _Gepoel2esw12DoPingConfig_Type()
)
gepoel2esw12DoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DoPingConfig.setStatus("current")
_Gepoel2esw12PingResult_Type = DisplayString
_Gepoel2esw12PingResult_Object = MibScalar
gepoel2esw12PingResult = _Gepoel2esw12PingResult_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 4),
    _Gepoel2esw12PingResult_Type()
)
gepoel2esw12PingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12PingResult.setStatus("current")
_Gepoel2esw12Ping6IpAddress_Type = DisplayString
_Gepoel2esw12Ping6IpAddress_Object = MibScalar
gepoel2esw12Ping6IpAddress = _Gepoel2esw12Ping6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 5),
    _Gepoel2esw12Ping6IpAddress_Type()
)
gepoel2esw12Ping6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ping6IpAddress.setStatus("current")


class _Gepoel2esw12Ping6Size_Type(Integer32):
    """Custom type gepoel2esw12Ping6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gepoel2esw12Ping6Size_Type.__name__ = "Integer32"
_Gepoel2esw12Ping6Size_Object = MibScalar
gepoel2esw12Ping6Size = _Gepoel2esw12Ping6Size_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 6),
    _Gepoel2esw12Ping6Size_Type()
)
gepoel2esw12Ping6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12Ping6Size.setStatus("current")


class _Gepoel2esw12DoPing6Config_Type(Integer32):
    """Custom type gepoel2esw12DoPing6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Gepoel2esw12DoPing6Config_Type.__name__ = "Integer32"
_Gepoel2esw12DoPing6Config_Object = MibScalar
gepoel2esw12DoPing6Config = _Gepoel2esw12DoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 7),
    _Gepoel2esw12DoPing6Config_Type()
)
gepoel2esw12DoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gepoel2esw12DoPing6Config.setStatus("current")
_Gepoel2esw12Ping6Result_Type = DisplayString
_Gepoel2esw12Ping6Result_Object = MibScalar
gepoel2esw12Ping6Result = _Gepoel2esw12Ping6Result_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 7, 5, 8),
    _Gepoel2esw12Ping6Result_Type()
)
gepoel2esw12Ping6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Ping6Result.setStatus("current")
_Gepoel2esw12Trap_ObjectIdentity = ObjectIdentity
gepoel2esw12Trap = _Gepoel2esw12Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8)
)
_Gepoel2esw12TrapEvent_ObjectIdentity = ObjectIdentity
gepoel2esw12TrapEvent = _Gepoel2esw12TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1)
)
_Gepoel2esw12TrapVariable_ObjectIdentity = ObjectIdentity
gepoel2esw12TrapVariable = _Gepoel2esw12TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 2)
)
_Gepoel2esw12Information_Type = DisplayString
_Gepoel2esw12Information_Object = MibScalar
gepoel2esw12Information = _Gepoel2esw12Information_Object(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 2, 1),
    _Gepoel2esw12Information_Type()
)
gepoel2esw12Information.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gepoel2esw12Information.setStatus("current")

# Managed Objects groups


# Notification objects

gepoel2esw12Emergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 1)
)
gepoel2esw12Emergency.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Emergency.setStatus(
        "current"
    )

gepoel2esw12Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 2)
)
gepoel2esw12Alert.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Alert.setStatus(
        "current"
    )

gepoel2esw12Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 3)
)
gepoel2esw12Critical.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Critical.setStatus(
        "current"
    )

gepoel2esw12Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 4)
)
gepoel2esw12Error.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Error.setStatus(
        "current"
    )

gepoel2esw12Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 5)
)
gepoel2esw12Warning.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Warning.setStatus(
        "current"
    )

gepoel2esw12Notice = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 6)
)
gepoel2esw12Notice.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Notice.setStatus(
        "current"
    )

gepoel2esw12Informational = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 7)
)
gepoel2esw12Informational.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Informational.setStatus(
        "current"
    )

gepoel2esw12Debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 1, 24, 8, 1, 8)
)
gepoel2esw12Debug.setObjects(
    ("PRIVATETECH-GEPoEL2ESW12-MIB", "gepoel2esw12Information")
)
if mibBuilder.loadTexts:
    gepoel2esw12Debug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATETECH-GEPoEL2ESW12-MIB",
    **{"privatetech": privatetech,
       "switch": switch,
       "gepoel2esw12ProductId": gepoel2esw12ProductId,
       "gepoel2esw12System": gepoel2esw12System,
       "gepoel2esw12SystemInformation": gepoel2esw12SystemInformation,
       "gepoel2esw12ModelName": gepoel2esw12ModelName,
       "gepoel2esw12BIOSVersion": gepoel2esw12BIOSVersion,
       "gepoel2esw12FirmwareVersion": gepoel2esw12FirmwareVersion,
       "gepoel2esw12HardwareMechanicalVersion": gepoel2esw12HardwareMechanicalVersion,
       "gepoel2esw12SeriesNumber": gepoel2esw12SeriesNumber,
       "gepoel2esw12HostMACAddress": gepoel2esw12HostMACAddress,
       "gepoel2esw12ConsoleBaudrate": gepoel2esw12ConsoleBaudrate,
       "gepoel2esw12RAMSize": gepoel2esw12RAMSize,
       "gepoel2esw12FlashSize": gepoel2esw12FlashSize,
       "gepoel2esw12BridgeFBDSize": gepoel2esw12BridgeFBDSize,
       "gepoel2esw12TransmitQueue": gepoel2esw12TransmitQueue,
       "gepoel2esw12MaximumFrameSize": gepoel2esw12MaximumFrameSize,
       "gepoel2esw12CPULoad": gepoel2esw12CPULoad,
       "gepoel2esw12SystemTime": gepoel2esw12SystemTime,
       "gepoel2esw12SystemTimeManual": gepoel2esw12SystemTimeManual,
       "gepoel2esw12SystemTimeManualClockSource": gepoel2esw12SystemTimeManualClockSource,
       "gepoel2esw12SystemTimeManualLocaltime": gepoel2esw12SystemTimeManualLocaltime,
       "gepoel2esw12SystemTimeManualTimeZoneOffset": gepoel2esw12SystemTimeManualTimeZoneOffset,
       "gepoel2esw12SystemTimeManualDaylightSavings": gepoel2esw12SystemTimeManualDaylightSavings,
       "gepoel2esw12SystemTimeManualTimeSetOffset": gepoel2esw12SystemTimeManualTimeSetOffset,
       "gepoel2esw12SystemTimeManualDaylightSavingsType": gepoel2esw12SystemTimeManualDaylightSavingsType,
       "gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom": gepoel2esw12SystemTimeManualDaylightSavingsBydatesFrom,
       "gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo": gepoel2esw12SystemTimeManualDaylightSavingsBydatesTo,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom": gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayFrom,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom": gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekFrom,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom": gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthFrom,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom": gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeFrom,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo": gepoel2esw12SystemTimeManualDaylightSavingsRecurringDayTo,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo": gepoel2esw12SystemTimeManualDaylightSavingsRecurringWeekTo,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo": gepoel2esw12SystemTimeManualDaylightSavingsRecurringMonthTo,
       "gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo": gepoel2esw12SystemTimeManualDaylightSavingsRecurringTimeTo,
       "gepoel2esw12SystemTimeNTP": gepoel2esw12SystemTimeNTP,
       "gepoel2esw12SystemTimeNTPTable": gepoel2esw12SystemTimeNTPTable,
       "gepoel2esw12SystemTimeNTPEntry": gepoel2esw12SystemTimeNTPEntry,
       "gepoel2esw12SystemTimeNTPIndex": gepoel2esw12SystemTimeNTPIndex,
       "gepoel2esw12SystemTimeNTPServerIPType": gepoel2esw12SystemTimeNTPServerIPType,
       "gepoel2esw12SystemTimeNTPServer": gepoel2esw12SystemTimeNTPServer,
       "gepoel2esw12SystemTimeNTPCurrentMode": gepoel2esw12SystemTimeNTPCurrentMode,
       "gepoel2esw12SystemAccount": gepoel2esw12SystemAccount,
       "gepoel2esw12SystemAccountUsers": gepoel2esw12SystemAccountUsers,
       "gepoel2esw12SystemAccountUserCreate": gepoel2esw12SystemAccountUserCreate,
       "gepoel2esw12SystemAccountUsersTable": gepoel2esw12SystemAccountUsersTable,
       "gepoel2esw12SystemAccountUsersEntry": gepoel2esw12SystemAccountUsersEntry,
       "gepoel2esw12UserIndex": gepoel2esw12UserIndex,
       "gepoel2esw12UserName": gepoel2esw12UserName,
       "gepoel2esw12Password": gepoel2esw12Password,
       "gepoel2esw12UserPrivilegeLevel": gepoel2esw12UserPrivilegeLevel,
       "gepoel2esw12AccountUserRowStatus": gepoel2esw12AccountUserRowStatus,
       "gepoel2esw12SystemAccountPrivilegeLevel": gepoel2esw12SystemAccountPrivilegeLevel,
       "gepoel2esw12PrivilegeLevelAccount": gepoel2esw12PrivilegeLevelAccount,
       "gepoel2esw12PrivilegeLevelDiagnostics": gepoel2esw12PrivilegeLevelDiagnostics,
       "gepoel2esw12PrivilegeLevelIP": gepoel2esw12PrivilegeLevelIP,
       "gepoel2esw12PrivilegeLevelMaintenance": gepoel2esw12PrivilegeLevelMaintenance,
       "gepoel2esw12PrivilegeLevelOLT": gepoel2esw12PrivilegeLevelOLT,
       "gepoel2esw12PrivilegeLevelONU": gepoel2esw12PrivilegeLevelONU,
       "gepoel2esw12PrivilegeLevelSMTP": gepoel2esw12PrivilegeLevelSMTP,
       "gepoel2esw12PrivilegeLevelSNMP": gepoel2esw12PrivilegeLevelSNMP,
       "gepoel2esw12PrivilegeLevelSecurity": gepoel2esw12PrivilegeLevelSecurity,
       "gepoel2esw12PrivilegeLevelSystem": gepoel2esw12PrivilegeLevelSystem,
       "gepoel2esw12PrivilegeLevelTrapEvent": gepoel2esw12PrivilegeLevelTrapEvent,
       "gepoel2esw12IP": gepoel2esw12IP,
       "gepoel2esw12IPv4": gepoel2esw12IPv4,
       "gepoel2esw12IPv4Configured": gepoel2esw12IPv4Configured,
       "gepoel2esw12Ipv4DHCPClient": gepoel2esw12Ipv4DHCPClient,
       "gepoel2esw12IPv4Address": gepoel2esw12IPv4Address,
       "gepoel2esw12IPv4Mask": gepoel2esw12IPv4Mask,
       "gepoel2esw12IPv4Router": gepoel2esw12IPv4Router,
       "gepoel2esw12IPv4VLANId": gepoel2esw12IPv4VLANId,
       "gepoel2esw12IPv4DNSServer": gepoel2esw12IPv4DNSServer,
       "gepoel2esw12IPv4DNSProxy": gepoel2esw12IPv4DNSProxy,
       "gepoel2esw12IPv4Current": gepoel2esw12IPv4Current,
       "gepoel2esw12Ipv4CurrentDHCPClient": gepoel2esw12Ipv4CurrentDHCPClient,
       "gepoel2esw12IPv4CurrentAddress": gepoel2esw12IPv4CurrentAddress,
       "gepoel2esw12IPv4CurrentMask": gepoel2esw12IPv4CurrentMask,
       "gepoel2esw12IPv4CurrentRouter": gepoel2esw12IPv4CurrentRouter,
       "gepoel2esw12IPv4CurrentVLANId": gepoel2esw12IPv4CurrentVLANId,
       "gepoel2esw12IPv4CurrentDNSServer": gepoel2esw12IPv4CurrentDNSServer,
       "gepoel2esw12IPv6": gepoel2esw12IPv6,
       "gepoel2esw12IPv6Configured": gepoel2esw12IPv6Configured,
       "gepoel2esw12Ipv6AutoConfiguration": gepoel2esw12Ipv6AutoConfiguration,
       "gepoel2esw12Ipv6Address": gepoel2esw12Ipv6Address,
       "gepoel2esw12Ipv6Prefix": gepoel2esw12Ipv6Prefix,
       "gepoel2esw12Ipv6Router": gepoel2esw12Ipv6Router,
       "gepoel2esw12IPv6Current": gepoel2esw12IPv6Current,
       "gepoel2esw12Ipv6CurrentAutoConfiguration": gepoel2esw12Ipv6CurrentAutoConfiguration,
       "gepoel2esw12Ipv6CurrentAddress": gepoel2esw12Ipv6CurrentAddress,
       "gepoel2esw12Ipv6CurrentLinkLocalAddress": gepoel2esw12Ipv6CurrentLinkLocalAddress,
       "gepoel2esw12Ipv6CurrentPrefix": gepoel2esw12Ipv6CurrentPrefix,
       "gepoel2esw12Ipv6CurrentRouter": gepoel2esw12Ipv6CurrentRouter,
       "gepoel2esw12Syslog": gepoel2esw12Syslog,
       "gepoel2esw12SyslogConf": gepoel2esw12SyslogConf,
       "gepoel2esw12ServerMode": gepoel2esw12ServerMode,
       "gepoel2esw12ServerAddress1": gepoel2esw12ServerAddress1,
       "gepoel2esw12SyslogLevel": gepoel2esw12SyslogLevel,
       "gepoel2esw12SyslogDetailedInfo": gepoel2esw12SyslogDetailedInfo,
       "gepoel2esw12SyslogDetailedInfoClear": gepoel2esw12SyslogDetailedInfoClear,
       "gepoel2esw12SyslogDetailedInfoTable": gepoel2esw12SyslogDetailedInfoTable,
       "gepoel2esw12SyslogDetailedInfoEntry": gepoel2esw12SyslogDetailedInfoEntry,
       "gepoel2esw12SyslogDetailedInfoIndex": gepoel2esw12SyslogDetailedInfoIndex,
       "gepoel2esw12SyslogDetailedInfoLevel": gepoel2esw12SyslogDetailedInfoLevel,
       "gepoel2esw12SyslogDetailedInfoTime": gepoel2esw12SyslogDetailedInfoTime,
       "gepoel2esw12SyslogDetailedInfoMessage": gepoel2esw12SyslogDetailedInfoMessage,
       "gepoel2esw12Snmp": gepoel2esw12Snmp,
       "gepoel2esw12SnmpConf": gepoel2esw12SnmpConf,
       "gepoel2esw12TrapHostConfTable": gepoel2esw12TrapHostConfTable,
       "gepoel2esw12TrapHostConfEntry": gepoel2esw12TrapHostConfEntry,
       "gepoel2esw12TrapHostConfIndex": gepoel2esw12TrapHostConfIndex,
       "gepoel2esw12TrapHostConfVersion": gepoel2esw12TrapHostConfVersion,
       "gepoel2esw12TrapHostConfIPType": gepoel2esw12TrapHostConfIPType,
       "gepoel2esw12TrapHostConfIP": gepoel2esw12TrapHostConfIP,
       "gepoel2esw12TrapHostConfPort": gepoel2esw12TrapHostConfPort,
       "gepoel2esw12TrapHostConfCommunity": gepoel2esw12TrapHostConfCommunity,
       "gepoel2esw12TrapHostConfSeverityLevel": gepoel2esw12TrapHostConfSeverityLevel,
       "gepoel2esw12TrapHostConfSecurityLevel": gepoel2esw12TrapHostConfSecurityLevel,
       "gepoel2esw12TrapHostConfAuthPtc": gepoel2esw12TrapHostConfAuthPtc,
       "gepoel2esw12TrapHostConfAuthPassword": gepoel2esw12TrapHostConfAuthPassword,
       "gepoel2esw12TrapHostConfPrivPtc": gepoel2esw12TrapHostConfPrivPtc,
       "gepoel2esw12TrapHostConfPrivPassword": gepoel2esw12TrapHostConfPrivPassword,
       "gepoel2esw12TrapHostConfCurrentMode": gepoel2esw12TrapHostConfCurrentMode,
       "gepoel2esw12OltManagement": gepoel2esw12OltManagement,
       "gepoel2esw12OltPortTable": gepoel2esw12OltPortTable,
       "gepoel2esw12OltPortEntry": gepoel2esw12OltPortEntry,
       "gepoel2esw12OltPortStatusIndex": gepoel2esw12OltPortStatusIndex,
       "gepoel2esw12OltPortLinkStatus": gepoel2esw12OltPortLinkStatus,
       "gepoel2esw12OltPortState": gepoel2esw12OltPortState,
       "gepoel2esw12OltPortSpdDpxConf": gepoel2esw12OltPortSpdDpxConf,
       "gepoel2esw12OltPortSpdDpx": gepoel2esw12OltPortSpdDpx,
       "gepoel2esw12OltPortFlwCtlConf": gepoel2esw12OltPortFlwCtlConf,
       "gepoel2esw12OltPortFlwCtl": gepoel2esw12OltPortFlwCtl,
       "gepoel2esw12OltStatisticsTable": gepoel2esw12OltStatisticsTable,
       "gepoel2esw12OltStatisticsEntry": gepoel2esw12OltStatisticsEntry,
       "gepoel2esw12OltStatisticsPortType": gepoel2esw12OltStatisticsPortType,
       "gepoel2esw12OltStatisticsQueryGroup": gepoel2esw12OltStatisticsQueryGroup,
       "gepoel2esw12OltStatisticsOctet": gepoel2esw12OltStatisticsOctet,
       "gepoel2esw12OltStatisticsCRC8Errors": gepoel2esw12OltStatisticsCRC8Errors,
       "gepoel2esw12OltStatisticsErrorFrameTransfer": gepoel2esw12OltStatisticsErrorFrameTransfer,
       "gepoel2esw12OltStatisticsLineCodeError": gepoel2esw12OltStatisticsLineCodeError,
       "gepoel2esw12OltStatisticsCorrectableFECBlock": gepoel2esw12OltStatisticsCorrectableFECBlock,
       "gepoel2esw12OltStatisticsUncorrectableFECBlock": gepoel2esw12OltStatisticsUncorrectableFECBlock,
       "gepoel2esw12OltStatisticsUndersizeFrame": gepoel2esw12OltStatisticsUndersizeFrame,
       "gepoel2esw12OltStatisticsCorrectableFECBytes": gepoel2esw12OltStatisticsCorrectableFECBytes,
       "gepoel2esw12OltStatisticsPostFECGoodFrame": gepoel2esw12OltStatisticsPostFECGoodFrame,
       "gepoel2esw12OltStatisticsPostFECBadFrame": gepoel2esw12OltStatisticsPostFECBadFrame,
       "gepoel2esw12OltStatisticsPreFECGoodFrame": gepoel2esw12OltStatisticsPreFECGoodFrame,
       "gepoel2esw12OltStatisticsPreFECBadFrame": gepoel2esw12OltStatisticsPreFECBadFrame,
       "gepoel2esw12OltStatisticsLaserIdlePower": gepoel2esw12OltStatisticsLaserIdlePower,
       "gepoel2esw12OltStatisticsFECPacketTooLongEvent": gepoel2esw12OltStatisticsFECPacketTooLongEvent,
       "gepoel2esw12OltStatisticsFECBlock": gepoel2esw12OltStatisticsFECBlock,
       "gepoel2esw12OltStatisticsLaserPower": gepoel2esw12OltStatisticsLaserPower,
       "gepoel2esw12OltStatisticsLaserVCC": gepoel2esw12OltStatisticsLaserVCC,
       "gepoel2esw12OltStatisticsLaserBias": gepoel2esw12OltStatisticsLaserBias,
       "gepoel2esw12OltStatisticsLaserTemp": gepoel2esw12OltStatisticsLaserTemp,
       "gepoel2esw12OltStatisticsUnicastFrame": gepoel2esw12OltStatisticsUnicastFrame,
       "gepoel2esw12OltStatisticsMulticastFrame": gepoel2esw12OltStatisticsMulticastFrame,
       "gepoel2esw12OltStatisticsBroadcastFrame": gepoel2esw12OltStatisticsBroadcastFrame,
       "gepoel2esw12OltStatisticsOversizetFrame": gepoel2esw12OltStatisticsOversizetFrame,
       "gepoel2esw12OltStatisticsCRC32Frame": gepoel2esw12OltStatisticsCRC32Frame,
       "gepoel2esw12OltStatisticsMPCPFrame": gepoel2esw12OltStatisticsMPCPFrame,
       "gepoel2esw12OltStatisticsMPCPBytes": gepoel2esw12OltStatisticsMPCPBytes,
       "gepoel2esw12OltStatisticsMPCPDiscoveryTimeout": gepoel2esw12OltStatisticsMPCPDiscoveryTimeout,
       "gepoel2esw12OltStatisticsMPCPDiscoveryWindow": gepoel2esw12OltStatisticsMPCPDiscoveryWindow,
       "gepoel2esw12OltStatisticsReportFrame": gepoel2esw12OltStatisticsReportFrame,
       "gepoel2esw12OltStatisticsReportFrameAbort": gepoel2esw12OltStatisticsReportFrameAbort,
       "gepoel2esw12OltStatisticsOAMFrames": gepoel2esw12OltStatisticsOAMFrames,
       "gepoel2esw12OltStatisticsOAMBytes": gepoel2esw12OltStatisticsOAMBytes,
       "gepoel2esw12OltStatisticsLlidMisMatch": gepoel2esw12OltStatisticsLlidMisMatch,
       "gepoel2esw12OltStatisticsUngrantedFrames": gepoel2esw12OltStatisticsUngrantedFrames,
       "gepoel2esw12OltStatisticsRegisterRequests": gepoel2esw12OltStatisticsRegisterRequests,
       "gepoel2esw12OltStatisticsRegisterAcks": gepoel2esw12OltStatisticsRegisterAcks,
       "gepoel2esw12OltStatisticsGateFrame": gepoel2esw12OltStatisticsGateFrame,
       "gepoel2esw12OltStatisticsReport": gepoel2esw12OltStatisticsReport,
       "gepoel2esw12OltStatisticsClear": gepoel2esw12OltStatisticsClear,
       "gepoel2esw12OltInformation": gepoel2esw12OltInformation,
       "gepoel2esw12OltChipID": gepoel2esw12OltChipID,
       "gepoel2esw12OltFirmwareVersion": gepoel2esw12OltFirmwareVersion,
       "gepoel2esw12OltPersonalityVersion": gepoel2esw12OltPersonalityVersion,
       "gepoel2esw12OltOltApp0Version": gepoel2esw12OltOltApp0Version,
       "gepoel2esw12OltOltApp1Version": gepoel2esw12OltOltApp1Version,
       "gepoel2esw12OltGreenPonConf": gepoel2esw12OltGreenPonConf,
       "gepoel2esw12OltGreenPonTable": gepoel2esw12OltGreenPonTable,
       "gepoel2esw12OltGreenPonEntry": gepoel2esw12OltGreenPonEntry,
       "gepoel2esw12OltGreenPonIndex": gepoel2esw12OltGreenPonIndex,
       "gepoel2esw12OltGreenPonstate": gepoel2esw12OltGreenPonstate,
       "gepoel2esw12OltGreenPonSleepAfterNoTraffic": gepoel2esw12OltGreenPonSleepAfterNoTraffic,
       "gepoel2esw12OltGreenPonOffTime": gepoel2esw12OltGreenPonOffTime,
       "gepoel2esw12OltGreenPonMinOnTime": gepoel2esw12OltGreenPonMinOnTime,
       "gepoel2esw12OltGreenPonMinOnuOffTime": gepoel2esw12OltGreenPonMinOnuOffTime,
       "gepoel2esw12OltGreenPonSleepCheckTime": gepoel2esw12OltGreenPonSleepCheckTime,
       "gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep": gepoel2esw12OltGreenPonTimeForOnuToBeginToSleep,
       "gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup": gepoel2esw12OltGreenPonSleepGraceTimeAfterWakeup,
       "gepoel2esw12OltGreenPonProvisionOnu": gepoel2esw12OltGreenPonProvisionOnu,
       "gepoel2esw12OltGreenPonUnprovisionOnu": gepoel2esw12OltGreenPonUnprovisionOnu,
       "gepoel2esw12OltPowerSavingReportTable": gepoel2esw12OltPowerSavingReportTable,
       "gepoel2esw12OltPowerSavingReportEntry": gepoel2esw12OltPowerSavingReportEntry,
       "gepoel2esw12OltPowerSavingReportIndex": gepoel2esw12OltPowerSavingReportIndex,
       "gepoel2esw12OltPowerSavingReportOnuMac": gepoel2esw12OltPowerSavingReportOnuMac,
       "gepoel2esw12OltPowerSavingReportCandidate": gepoel2esw12OltPowerSavingReportCandidate,
       "gepoel2esw12OltPowerSavingReportAsleep": gepoel2esw12OltPowerSavingReportAsleep,
       "gepoel2esw12OltPowerSavingReportTimeAsleep": gepoel2esw12OltPowerSavingReportTimeAsleep,
       "gepoel2esw12OltPowerSavingReportTimeActive": gepoel2esw12OltPowerSavingReportTimeActive,
       "gepoel2esw12OltBridgeConfig": gepoel2esw12OltBridgeConfig,
       "gepoel2esw12OltBridgingConfAgeLimit": gepoel2esw12OltBridgingConfAgeLimit,
       "gepoel2esw12OltBridgingConfAllowVlanOnSimple": gepoel2esw12OltBridgingConfAllowVlanOnSimple,
       "gepoel2esw12OltDBA": gepoel2esw12OltDBA,
       "gepoel2esw12OltAggregateShaperTable": gepoel2esw12OltAggregateShaperTable,
       "gepoel2esw12OltAggregateShaperEntry": gepoel2esw12OltAggregateShaperEntry,
       "gepoel2esw12OltAggregateShaperIndex": gepoel2esw12OltAggregateShaperIndex,
       "gepoel2esw12OltAggregateShaperBwEnable": gepoel2esw12OltAggregateShaperBwEnable,
       "gepoel2esw12OltAggregateShaperMaxBw": gepoel2esw12OltAggregateShaperMaxBw,
       "gepoel2esw12OltAggregateShaperMaxBurst": gepoel2esw12OltAggregateShaperMaxBurst,
       "gepoel2esw12OltDropDownWeightsTable": gepoel2esw12OltDropDownWeightsTable,
       "gepoel2esw12OltDropDownWeightsEntry": gepoel2esw12OltDropDownWeightsEntry,
       "gepoel2esw12OltDropDownWeightsIndex": gepoel2esw12OltDropDownWeightsIndex,
       "gepoel2esw12OltDropDownLevel1": gepoel2esw12OltDropDownLevel1,
       "gepoel2esw12OltDropDownLevel2": gepoel2esw12OltDropDownLevel2,
       "gepoel2esw12OltDropDownLevel3": gepoel2esw12OltDropDownLevel3,
       "gepoel2esw12OltDropDownLevel4": gepoel2esw12OltDropDownLevel4,
       "gepoel2esw12OltDropDownLevel5": gepoel2esw12OltDropDownLevel5,
       "gepoel2esw12OltDropDownLevel6": gepoel2esw12OltDropDownLevel6,
       "gepoel2esw12OltDropDownLevel7": gepoel2esw12OltDropDownLevel7,
       "gepoel2esw12OltPollingRateTable": gepoel2esw12OltPollingRateTable,
       "gepoel2esw12OltPollingRateEntry": gepoel2esw12OltPollingRateEntry,
       "gepoel2esw12OltPollingRateIndex": gepoel2esw12OltPollingRateIndex,
       "gepoel2esw12OltPollingRateLevel0": gepoel2esw12OltPollingRateLevel0,
       "gepoel2esw12OltPollingRateLevel1": gepoel2esw12OltPollingRateLevel1,
       "gepoel2esw12OltPollingRateLevel2": gepoel2esw12OltPollingRateLevel2,
       "gepoel2esw12OltPollingRateLevel3": gepoel2esw12OltPollingRateLevel3,
       "gepoel2esw12OltPollingRateLevel4": gepoel2esw12OltPollingRateLevel4,
       "gepoel2esw12OltPollingRateLevel5": gepoel2esw12OltPollingRateLevel5,
       "gepoel2esw12OltPollingRateLevel6": gepoel2esw12OltPollingRateLevel6,
       "gepoel2esw12OltPollingRateLevel7": gepoel2esw12OltPollingRateLevel7,
       "gepoel2esw12OltIgmpProxy": gepoel2esw12OltIgmpProxy,
       "gepoel2esw12OltMaxIGMPGroup": gepoel2esw12OltMaxIGMPGroup,
       "gepoel2esw12OltGlobalBwPollSize": gepoel2esw12OltGlobalBwPollSize,
       "gepoel2esw12OltIgmpCaptureAllMode": gepoel2esw12OltIgmpCaptureAllMode,
       "gepoel2esw12OltIgmpDAForwarding": gepoel2esw12OltIgmpDAForwarding,
       "gepoel2esw12OltIgmpSAForwarding": gepoel2esw12OltIgmpSAForwarding,
       "gepoel2esw12OltNetworkParameters": gepoel2esw12OltNetworkParameters,
       "gepoel2esw12OltOamParameters": gepoel2esw12OltOamParameters,
       "gepoel2esw12OltMaxOamRate": gepoel2esw12OltMaxOamRate,
       "gepoel2esw12OltMinOamRate": gepoel2esw12OltMinOamRate,
       "gepoel2esw12OltLoopbackTimeout": gepoel2esw12OltLoopbackTimeout,
       "gepoel2esw12OltVlanParameters": gepoel2esw12OltVlanParameters,
       "gepoel2esw12OltVlanEtherType": gepoel2esw12OltVlanEtherType,
       "gepoel2esw12OltTagUp": gepoel2esw12OltTagUp,
       "gepoel2esw12OltTagDown": gepoel2esw12OltTagDown,
       "gepoel2esw12OltMpcpParametersTable": gepoel2esw12OltMpcpParametersTable,
       "gepoel2esw12OltMpcpParametersEntry": gepoel2esw12OltMpcpParametersEntry,
       "gepoel2esw12OltMpcpParametersIndex": gepoel2esw12OltMpcpParametersIndex,
       "gepoel2esw12OltMpcpDiscoveryPeriod": gepoel2esw12OltMpcpDiscoveryPeriod,
       "gepoel2esw12OltMpcpDiscoveryWindow": gepoel2esw12OltMpcpDiscoveryWindow,
       "gepoel2esw12OltOperation": gepoel2esw12OltOperation,
       "gepoel2esw12OltEnable": gepoel2esw12OltEnable,
       "gepoel2esw12OltDisable": gepoel2esw12OltDisable,
       "gepoel2esw12OltBlockLinkListTable": gepoel2esw12OltBlockLinkListTable,
       "gepoel2esw12OltBlockLinkListEntry": gepoel2esw12OltBlockLinkListEntry,
       "gepoel2esw12OltBlockLinkIndex": gepoel2esw12OltBlockLinkIndex,
       "gepoel2esw12OltBlockLinkLabel": gepoel2esw12OltBlockLinkLabel,
       "gepoel2esw12OltBlockLinkUnblock": gepoel2esw12OltBlockLinkUnblock,
       "gepoel2esw12OltAllKnownLinkProvision": gepoel2esw12OltAllKnownLinkProvision,
       "gepoel2esw12OltProvisionInOltTable": gepoel2esw12OltProvisionInOltTable,
       "gepoel2esw12OltProvisionInOltEntry": gepoel2esw12OltProvisionInOltEntry,
       "gepoel2esw12ProvInOltIndex": gepoel2esw12ProvInOltIndex,
       "gepoel2esw12ProvInOltLinkLabel": gepoel2esw12ProvInOltLinkLabel,
       "gepoel2esw12ProvInOltBridge": gepoel2esw12ProvInOltBridge,
       "gepoel2esw12ProvInOltSourceEpon": gepoel2esw12ProvInOltSourceEpon,
       "gepoel2esw12ProvInOltDestNNI": gepoel2esw12ProvInOltDestNNI,
       "gepoel2esw12ProvInOltVlan": gepoel2esw12ProvInOltVlan,
       "gepoel2esw12DelProvInOlt": gepoel2esw12DelProvInOlt,
       "gepoel2esw12OltProvisionInHostTable": gepoel2esw12OltProvisionInHostTable,
       "gepoel2esw12OltProvisionInHostEntry": gepoel2esw12OltProvisionInHostEntry,
       "gepoel2esw12ProvInHostEponPort": gepoel2esw12ProvInHostEponPort,
       "gepoel2esw12ProvInHostIndex": gepoel2esw12ProvInHostIndex,
       "gepoel2esw12ProvInHostLinkLabel": gepoel2esw12ProvInHostLinkLabel,
       "gepoel2esw12ProvInHostBridge": gepoel2esw12ProvInHostBridge,
       "gepoel2esw12ProvInHostBridgeDestNNI": gepoel2esw12ProvInHostBridgeDestNNI,
       "gepoel2esw12ProvInHostVlan": gepoel2esw12ProvInHostVlan,
       "gepoel2esw12DelProvInHost": gepoel2esw12DelProvInHost,
       "gepoel2esw12OnuManagement": gepoel2esw12OnuManagement,
       "gepoel2esw12OnuStatisticsTable": gepoel2esw12OnuStatisticsTable,
       "gepoel2esw12OnuStatisticsEntry": gepoel2esw12OnuStatisticsEntry,
       "gepoel2esw12OnuPortStatisticsMacAddress": gepoel2esw12OnuPortStatisticsMacAddress,
       "gepoel2esw12OnuPortStatisticsIndex": gepoel2esw12OnuPortStatisticsIndex,
       "gepoel2esw12OnuPortStatisticsOctetTransfer": gepoel2esw12OnuPortStatisticsOctetTransfer,
       "gepoel2esw12OnuPortStatisticsTotalFrame": gepoel2esw12OnuPortStatisticsTotalFrame,
       "gepoel2esw12OnuPortStatisticsUnicastFrame": gepoel2esw12OnuPortStatisticsUnicastFrame,
       "gepoel2esw12OnuPortStatisticsMulticastFrame": gepoel2esw12OnuPortStatisticsMulticastFrame,
       "gepoel2esw12OnuPortStatisticsBroadcastFrame": gepoel2esw12OnuPortStatisticsBroadcastFrame,
       "gepoel2esw12OnuPortStatistics64OctetFrame": gepoel2esw12OnuPortStatistics64OctetFrame,
       "gepoel2esw12OnuPortStatistics65to127OctetFrame": gepoel2esw12OnuPortStatistics65to127OctetFrame,
       "gepoel2esw12OnuPortStatistics128to255OctetFrame": gepoel2esw12OnuPortStatistics128to255OctetFrame,
       "gepoel2esw12OnuPortStatistics256to511OctetFrame": gepoel2esw12OnuPortStatistics256to511OctetFrame,
       "gepoel2esw12OnuPortStatistics512to1023OctetFrame": gepoel2esw12OnuPortStatistics512to1023OctetFrame,
       "gepoel2esw12OnuPortStatistics1024to1518OctetFrame": gepoel2esw12OnuPortStatistics1024to1518OctetFrame,
       "gepoel2esw12OnuPortStatistics1519upOctetFrame": gepoel2esw12OnuPortStatistics1519upOctetFrame,
       "gepoel2esw12OnuPortStatisticsUndersizeFrame": gepoel2esw12OnuPortStatisticsUndersizeFrame,
       "gepoel2esw12OnuPortStatisticsFCSError": gepoel2esw12OnuPortStatisticsFCSError,
       "gepoel2esw12OnuPortStatisticsCRC8Error": gepoel2esw12OnuPortStatisticsCRC8Error,
       "gepoel2esw12OnuPortStatisticsLineCodeError": gepoel2esw12OnuPortStatisticsLineCodeError,
       "gepoel2esw12OnuPortStatisticsBytesDropped": gepoel2esw12OnuPortStatisticsBytesDropped,
       "gepoel2esw12OnuPortStatisticsFramesDropped": gepoel2esw12OnuPortStatisticsFramesDropped,
       "gepoel2esw12OnuPortStatisticsBytesDelayed": gepoel2esw12OnuPortStatisticsBytesDelayed,
       "gepoel2esw12OnuPortStatisticsMaxDelay": gepoel2esw12OnuPortStatisticsMaxDelay,
       "gepoel2esw12OnuPortStatisticsDelayThreshold": gepoel2esw12OnuPortStatisticsDelayThreshold,
       "gepoel2esw12OnuPortStatisticsErroredFrame": gepoel2esw12OnuPortStatisticsErroredFrame,
       "gepoel2esw12OnuPortStatisticsUnusedBytes": gepoel2esw12OnuPortStatisticsUnusedBytes,
       "gepoel2esw12OnuPortStatisticsOversizedFrame": gepoel2esw12OnuPortStatisticsOversizedFrame,
       "gepoel2esw12OnuPortStatisticsPauseFrames": gepoel2esw12OnuPortStatisticsPauseFrames,
       "gepoel2esw12OnuPortStatisticsLengthErrors": gepoel2esw12OnuPortStatisticsLengthErrors,
       "gepoel2esw12OnuPortStatisticsAligmentErrors": gepoel2esw12OnuPortStatisticsAligmentErrors,
       "gepoel2esw12OnuPortStatisticsCRC32Error": gepoel2esw12OnuPortStatisticsCRC32Error,
       "gepoel2esw12OnuPortStatisticsSingleCollision": gepoel2esw12OnuPortStatisticsSingleCollision,
       "gepoel2esw12OnuPortStatisticsMultipleCollision": gepoel2esw12OnuPortStatisticsMultipleCollision,
       "gepoel2esw12OnuPortStatisticsLateCollision": gepoel2esw12OnuPortStatisticsLateCollision,
       "gepoel2esw12OnuPortStatisticsExcessiveCollision": gepoel2esw12OnuPortStatisticsExcessiveCollision,
       "gepoel2esw12OnuStatisticsClear": gepoel2esw12OnuStatisticsClear,
       "gepoel2esw12OnuInformationTable": gepoel2esw12OnuInformationTable,
       "gepoel2esw12OnuInformationEntry": gepoel2esw12OnuInformationEntry,
       "gepoel2esw12OnuInfoOltPort": gepoel2esw12OnuInfoOltPort,
       "gepoel2esw12OnuInfoMacAddress": gepoel2esw12OnuInfoMacAddress,
       "gepoel2esw12OnuModelName": gepoel2esw12OnuModelName,
       "gepoel2esw12OnuSerialNumber": gepoel2esw12OnuSerialNumber,
       "gepoel2esw12OnuOutputOpticalWavelength": gepoel2esw12OnuOutputOpticalWavelength,
       "gepoel2esw12OnuFirmwaveVersion": gepoel2esw12OnuFirmwaveVersion,
       "gepoel2esw12OnuBootCodeVersion": gepoel2esw12OnuBootCodeVersion,
       "gepoel2esw12OnuPersonalityVersion": gepoel2esw12OnuPersonalityVersion,
       "gepoel2esw12OnuApp0Version": gepoel2esw12OnuApp0Version,
       "gepoel2esw12OnuApp1Version": gepoel2esw12OnuApp1Version,
       "gepoel2esw12OnuTrafficManagement": gepoel2esw12OnuTrafficManagement,
       "gepoel2esw12OnuQueueConfig": gepoel2esw12OnuQueueConfig,
       "gepoel2esw12OnuUpstreamQueueConfigTable": gepoel2esw12OnuUpstreamQueueConfigTable,
       "gepoel2esw12OnuUpstreamQueueConfigEntry": gepoel2esw12OnuUpstreamQueueConfigEntry,
       "gepoel2esw12OnuUpstreamQueueOltPort": gepoel2esw12OnuUpstreamQueueOltPort,
       "gepoel2esw12OnuUpstreamMacAddress": gepoel2esw12OnuUpstreamMacAddress,
       "gepoel2esw12OnuUpstreamConfigIndex": gepoel2esw12OnuUpstreamConfigIndex,
       "gepoel2esw12OnuUpstreamQueueSize": gepoel2esw12OnuUpstreamQueueSize,
       "gepoel2esw12OnuUpstreamQueueSizeDoModify": gepoel2esw12OnuUpstreamQueueSizeDoModify,
       "gepoel2esw12OnuDownstreamQueueConfigTable": gepoel2esw12OnuDownstreamQueueConfigTable,
       "gepoel2esw12OnuDownstreamQueueConfigEntry": gepoel2esw12OnuDownstreamQueueConfigEntry,
       "gepoel2esw12OnuDownstreamQueueConfigOltPort": gepoel2esw12OnuDownstreamQueueConfigOltPort,
       "gepoel2esw12OnuDownstreamMacAddress": gepoel2esw12OnuDownstreamMacAddress,
       "gepoel2esw12OnuDownstreamPort": gepoel2esw12OnuDownstreamPort,
       "gepoel2esw12OnuDownstreamQueueSize": gepoel2esw12OnuDownstreamQueueSize,
       "gepoel2esw12OnuDownstreamQueueSizeDoModify": gepoel2esw12OnuDownstreamQueueSizeDoModify,
       "gepoel2esw12OnuUpstreamQueueConfigAdd": gepoel2esw12OnuUpstreamQueueConfigAdd,
       "gepoel2esw12OnuUpstreamQueueAddOltPort": gepoel2esw12OnuUpstreamQueueAddOltPort,
       "gepoel2esw12OnuUpstreamQueueAddMacAddress": gepoel2esw12OnuUpstreamQueueAddMacAddress,
       "gepoel2esw12OnuUpstreamQueueAddSize": gepoel2esw12OnuUpstreamQueueAddSize,
       "gepoel2esw12OnuUpstreamQueueAdd": gepoel2esw12OnuUpstreamQueueAdd,
       "gepoel2esw12OnuUpstreamQueueConfigDel": gepoel2esw12OnuUpstreamQueueConfigDel,
       "gepoel2esw12OnuUpstreamQueueDelConfigOltPort": gepoel2esw12OnuUpstreamQueueDelConfigOltPort,
       "gepoel2esw12OnuUpstreamQueueDelMacAddress": gepoel2esw12OnuUpstreamQueueDelMacAddress,
       "gepoel2esw12OnuUpstreamQueueDel": gepoel2esw12OnuUpstreamQueueDel,
       "gepoel2esw12OnuFieldSelectTable": gepoel2esw12OnuFieldSelectTable,
       "gepoel2esw12OnuFieldSelectEntry": gepoel2esw12OnuFieldSelectEntry,
       "gepoel2esw12OnuFieldSelectOltPort": gepoel2esw12OnuFieldSelectOltPort,
       "gepoel2esw12OnuMacAddress": gepoel2esw12OnuMacAddress,
       "gepoel2esw12OnuPort": gepoel2esw12OnuPort,
       "gepoel2esw12OnuFieldIndex": gepoel2esw12OnuFieldIndex,
       "gepoel2esw12OnuFieldName": gepoel2esw12OnuFieldName,
       "gepoel2esw12OnuRefCount": gepoel2esw12OnuRefCount,
       "gepoel2esw12OnuLayerSel": gepoel2esw12OnuLayerSel,
       "gepoel2esw12OnuDWord": gepoel2esw12OnuDWord,
       "gepoel2esw12OnuBitOffset": gepoel2esw12OnuBitOffset,
       "gepoel2esw12OnuFieldWidth": gepoel2esw12OnuFieldWidth,
       "gepoel2esw12OnuFieldModify": gepoel2esw12OnuFieldModify,
       "gepoel2esw12OnuFieldClear": gepoel2esw12OnuFieldClear,
       "gepoel2esw12OnuRule": gepoel2esw12OnuRule,
       "gepoel2esw12OnuRuleNumberTable": gepoel2esw12OnuRuleNumberTable,
       "gepoel2esw12OnuRuleNumberEntry": gepoel2esw12OnuRuleNumberEntry,
       "gepoel2esw12OnuRuleNumberOltPort": gepoel2esw12OnuRuleNumberOltPort,
       "gepoel2esw12OnuRuleNumberMacAddress": gepoel2esw12OnuRuleNumberMacAddress,
       "gepoel2esw12OnuRuleNumberPort": gepoel2esw12OnuRuleNumberPort,
       "gepoel2esw12OnuRuleNumber": gepoel2esw12OnuRuleNumber,
       "gepoel2esw12OnuRuleClauseNumberTable": gepoel2esw12OnuRuleClauseNumberTable,
       "gepoel2esw12OnuRuleClauseNumberEntry": gepoel2esw12OnuRuleClauseNumberEntry,
       "gepoel2esw12OnuRuleClauseNumberOltPort": gepoel2esw12OnuRuleClauseNumberOltPort,
       "gepoel2esw12OnuRuleClauseMacAddress": gepoel2esw12OnuRuleClauseMacAddress,
       "gepoel2esw12OnuRuleClausePort": gepoel2esw12OnuRuleClausePort,
       "gepoel2esw12OnuRuleClauseNumberIndex": gepoel2esw12OnuRuleClauseNumberIndex,
       "gepoel2esw12OnuRuleClauseNumber": gepoel2esw12OnuRuleClauseNumber,
       "gepoel2esw12OnuRuleTable": gepoel2esw12OnuRuleTable,
       "gepoel2esw12OnuRuleEntry": gepoel2esw12OnuRuleEntry,
       "gepoel2esw12OnuRuleOltPort": gepoel2esw12OnuRuleOltPort,
       "gepoel2esw12OnuRuleMacAddress": gepoel2esw12OnuRuleMacAddress,
       "gepoel2esw12OnuRulePort": gepoel2esw12OnuRulePort,
       "gepoel2esw12OnuPortRuleIndex": gepoel2esw12OnuPortRuleIndex,
       "gepoel2esw12OnuPortRuleDelete": gepoel2esw12OnuPortRuleDelete,
       "gepoel2esw12OnuPortRuleAction": gepoel2esw12OnuPortRuleAction,
       "gepoel2esw12OnuPortRuleClauses": gepoel2esw12OnuPortRuleClauses,
       "gepoel2esw12OnuPortRuleNextClauses": gepoel2esw12OnuPortRuleNextClauses,
       "gepoel2esw12OnuRuleAdd": gepoel2esw12OnuRuleAdd,
       "gepoel2esw12OnuRuleAddOltPort": gepoel2esw12OnuRuleAddOltPort,
       "gepoel2esw12OnuRuleAddMacAddress": gepoel2esw12OnuRuleAddMacAddress,
       "gepoel2esw12OnuRuleAddPort": gepoel2esw12OnuRuleAddPort,
       "gepoel2esw12OnuPortRuleAddPriority": gepoel2esw12OnuPortRuleAddPriority,
       "gepoel2esw12OnuPortRuleAddAction": gepoel2esw12OnuPortRuleAddAction,
       "gepoel2esw12OnuPortRuleAddActionPort": gepoel2esw12OnuPortRuleAddActionPort,
       "gepoel2esw12OnuPortRuleAddActionQueue": gepoel2esw12OnuPortRuleAddActionQueue,
       "gepoel2esw12OnuPortRuleAddClauseNum": gepoel2esw12OnuPortRuleAddClauseNum,
       "gepoel2esw12OnuPortRuleAddClauseTable": gepoel2esw12OnuPortRuleAddClauseTable,
       "gepoel2esw12OnuPortRuleAddClauseEntry": gepoel2esw12OnuPortRuleAddClauseEntry,
       "gepoel2esw12OnuPortRuleAddClauseIndex": gepoel2esw12OnuPortRuleAddClauseIndex,
       "gepoel2esw12OnuPortRuleAddField": gepoel2esw12OnuPortRuleAddField,
       "gepoel2esw12OnuPortRuleAddOperation": gepoel2esw12OnuPortRuleAddOperation,
       "gepoel2esw12OnuPortRuleAddValueType": gepoel2esw12OnuPortRuleAddValueType,
       "gepoel2esw12OnuPortRuleAddValue": gepoel2esw12OnuPortRuleAddValue,
       "gepoel2esw12DoOnuRulerAdd": gepoel2esw12DoOnuRulerAdd,
       "gepoel2esw12OnuIGMP": gepoel2esw12OnuIGMP,
       "gepoel2esw12OnuIGMPSnoopingTable": gepoel2esw12OnuIGMPSnoopingTable,
       "gepoel2esw12OnuIGMPSnoopingEntry": gepoel2esw12OnuIGMPSnoopingEntry,
       "gepoel2esw12OnuIGMPSnoopingOltPort": gepoel2esw12OnuIGMPSnoopingOltPort,
       "gepoel2esw12OnuIGMPSnoopingMacAddress": gepoel2esw12OnuIGMPSnoopingMacAddress,
       "gepoel2esw12OnuRobustnessCount": gepoel2esw12OnuRobustnessCount,
       "gepoel2esw12OnuLastMemberQuery": gepoel2esw12OnuLastMemberQuery,
       "gepoel2esw12OnuPort1IGMPGroupNumber": gepoel2esw12OnuPort1IGMPGroupNumber,
       "gepoel2esw12OnuPort1QueueForClassification": gepoel2esw12OnuPort1QueueForClassification,
       "gepoel2esw12OnuPort2IGMPGroupNumber": gepoel2esw12OnuPort2IGMPGroupNumber,
       "gepoel2esw12OnuPort2QueueForClassification": gepoel2esw12OnuPort2QueueForClassification,
       "gepoel2esw12OnuIGMPForwardGroupByL2DA": gepoel2esw12OnuIGMPForwardGroupByL2DA,
       "gepoel2esw12OnuIGMPForwardGroupByVID": gepoel2esw12OnuIGMPForwardGroupByVID,
       "gepoel2esw12OnuIGMPForwardGroupByIPDA": gepoel2esw12OnuIGMPForwardGroupByIPDA,
       "gepoel2esw12OnuIGMPVlanProvision": gepoel2esw12OnuIGMPVlanProvision,
       "gepoel2esw12OnuIGMPVlanProvisionTable": gepoel2esw12OnuIGMPVlanProvisionTable,
       "gepoel2esw12OnuIGMPVlanProvisionEntry": gepoel2esw12OnuIGMPVlanProvisionEntry,
       "gepoel2esw12OnuIGMPVlanProvisionOltPort": gepoel2esw12OnuIGMPVlanProvisionOltPort,
       "gepoel2esw12OnuIGMPVlanProvisionMacAddress": gepoel2esw12OnuIGMPVlanProvisionMacAddress,
       "gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup": gepoel2esw12OnuIGMPVlanProvisionActionforUnmanagedGroup,
       "gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan": gepoel2esw12OnuIGMPVlanProvisionNumberofIGMPVlan,
       "gepoel2esw12OnuIGMPVlanTable": gepoel2esw12OnuIGMPVlanTable,
       "gepoel2esw12OnuIGMPVlanEntry": gepoel2esw12OnuIGMPVlanEntry,
       "gepoel2esw12OnuIGMPVlanOltPort": gepoel2esw12OnuIGMPVlanOltPort,
       "gepoel2esw12OnuIGMPVlanMacAddress": gepoel2esw12OnuIGMPVlanMacAddress,
       "gepoel2esw12OnuIGMPVlanIndex": gepoel2esw12OnuIGMPVlanIndex,
       "gepoel2esw12OnuIGMPVlanEponVlanID": gepoel2esw12OnuIGMPVlanEponVlanID,
       "gepoel2esw12OnuIGMPVlanUserVlanID": gepoel2esw12OnuIGMPVlanUserVlanID,
       "gepoel2esw12OnuIGMPVlanMaxAllowedGroup": gepoel2esw12OnuIGMPVlanMaxAllowedGroup,
       "gepoel2esw12OnuIGMPVlanDel": gepoel2esw12OnuIGMPVlanDel,
       "gepoel2esw12OnuIGMPVlanAdd": gepoel2esw12OnuIGMPVlanAdd,
       "gepoel2esw12OnuIGMPVlanAddOltPort": gepoel2esw12OnuIGMPVlanAddOltPort,
       "gepoel2esw12OnuIGMPVlanAddMacAddress": gepoel2esw12OnuIGMPVlanAddMacAddress,
       "gepoel2esw12OnuIGMPVlanAddEponVlanID": gepoel2esw12OnuIGMPVlanAddEponVlanID,
       "gepoel2esw12OnuIGMPVlanAddUserVlanID": gepoel2esw12OnuIGMPVlanAddUserVlanID,
       "gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup": gepoel2esw12OnuIGMPVlanAddMaxAllowedGroup,
       "gepoel2esw12OnuIGMPVlanAddDo": gepoel2esw12OnuIGMPVlanAddDo,
       "gepoel2esw12OnuIGMPGroup": gepoel2esw12OnuIGMPGroup,
       "gepoel2esw12OnuIGMPGroupTable": gepoel2esw12OnuIGMPGroupTable,
       "gepoel2esw12OnuIGMPGroupEntry": gepoel2esw12OnuIGMPGroupEntry,
       "gepoel2esw12OnuIGMPGroupOltPort": gepoel2esw12OnuIGMPGroupOltPort,
       "gepoel2esw12OnuIGMPGroupMacAddress": gepoel2esw12OnuIGMPGroupMacAddress,
       "gepoel2esw12OnuIGMPGroupJoinedIndex": gepoel2esw12OnuIGMPGroupJoinedIndex,
       "gepoel2esw12OnuIGMPGroupJoinedID": gepoel2esw12OnuIGMPGroupJoinedID,
       "gepoel2esw12OnuIGMPGroupJoinedPort": gepoel2esw12OnuIGMPGroupJoinedPort,
       "gepoel2esw12OnuBridgeConfig": gepoel2esw12OnuBridgeConfig,
       "gepoel2esw12OnuBridgeConfigTable": gepoel2esw12OnuBridgeConfigTable,
       "gepoel2esw12OnuBridgeConfigEntry": gepoel2esw12OnuBridgeConfigEntry,
       "gepoel2esw12OnuBridgeConfigOltPort": gepoel2esw12OnuBridgeConfigOltPort,
       "gepoel2esw12OnuBridgeConfigMacAddress": gepoel2esw12OnuBridgeConfigMacAddress,
       "gepoel2esw12OnuBridgeConfigPort": gepoel2esw12OnuBridgeConfigPort,
       "gepoel2esw12OnuBridgeConfigAgeLimit": gepoel2esw12OnuBridgeConfigAgeLimit,
       "gepoel2esw12OnuBridgeConfigEntryLimit": gepoel2esw12OnuBridgeConfigEntryLimit,
       "gepoel2esw12OnuBridgeConfigLearningMode": gepoel2esw12OnuBridgeConfigLearningMode,
       "gepoel2esw12OnuDynamicMac": gepoel2esw12OnuDynamicMac,
       "gepoel2esw12OnuDynamicMacTable": gepoel2esw12OnuDynamicMacTable,
       "gepoel2esw12OnuDynamicMacEntry": gepoel2esw12OnuDynamicMacEntry,
       "gepoel2esw12OnuDynamicOltPort": gepoel2esw12OnuDynamicOltPort,
       "gepoel2esw12OnuDynamicLink": gepoel2esw12OnuDynamicLink,
       "gepoel2esw12OnuDynamicPort": gepoel2esw12OnuDynamicPort,
       "gepoel2esw12OnuDynamicMacIndex": gepoel2esw12OnuDynamicMacIndex,
       "gepoel2esw12OnuDynamicMacLink": gepoel2esw12OnuDynamicMacLink,
       "gepoel2esw12OnuClearDynamicMacTable": gepoel2esw12OnuClearDynamicMacTable,
       "gepoel2esw12OnuClearDynamicMacEntry": gepoel2esw12OnuClearDynamicMacEntry,
       "gepoel2esw12OnuClearDynamicMacOltPort": gepoel2esw12OnuClearDynamicMacOltPort,
       "gepoel2esw12OnuClearDynamicMacLink": gepoel2esw12OnuClearDynamicMacLink,
       "gepoel2esw12OnuClearDynamicMacPort": gepoel2esw12OnuClearDynamicMacPort,
       "gepoel2esw12OnuClearDynamicMacClear": gepoel2esw12OnuClearDynamicMacClear,
       "gepoel2esw12OnuVlanOption": gepoel2esw12OnuVlanOption,
       "gepoel2esw12OnuVlanOptionTable": gepoel2esw12OnuVlanOptionTable,
       "gepoel2esw12OnuVlanOptionEntry": gepoel2esw12OnuVlanOptionEntry,
       "gepoel2esw12OnuVlanOptionOltPort": gepoel2esw12OnuVlanOptionOltPort,
       "gepoel2esw12OnuVlanOptionMac": gepoel2esw12OnuVlanOptionMac,
       "gepoel2esw12OnuVlanOptionEtherType": gepoel2esw12OnuVlanOptionEtherType,
       "gepoel2esw12OnuVlanOptionTagUp": gepoel2esw12OnuVlanOptionTagUp,
       "gepoel2esw12OnuVlanOptionTagDown": gepoel2esw12OnuVlanOptionTagDown,
       "gepoel2esw12OnuBroadcastQueue": gepoel2esw12OnuBroadcastQueue,
       "gepoel2esw12OnuBroadcastQueueTable": gepoel2esw12OnuBroadcastQueueTable,
       "gepoel2esw12OnuBroadcastQueueEntry": gepoel2esw12OnuBroadcastQueueEntry,
       "gepoel2esw12OnuBroadcastQueueOltPort": gepoel2esw12OnuBroadcastQueueOltPort,
       "gepoel2esw12OnuBroadcastQueueMacAddress": gepoel2esw12OnuBroadcastQueueMacAddress,
       "gepoel2esw12OnuBroadcastQueuePort": gepoel2esw12OnuBroadcastQueuePort,
       "gepoel2esw12OnuBroadcastQueueIndex": gepoel2esw12OnuBroadcastQueueIndex,
       "gepoel2esw12OnuMiscOperationTable": gepoel2esw12OnuMiscOperationTable,
       "gepoel2esw12OnuMiscOperationEntry": gepoel2esw12OnuMiscOperationEntry,
       "gepoel2esw12OnuMiscOperationOltPort": gepoel2esw12OnuMiscOperationOltPort,
       "gepoel2esw12OnuMiscOperationMacAddress": gepoel2esw12OnuMiscOperationMacAddress,
       "gepoel2esw12OnuMiscOperationEnable": gepoel2esw12OnuMiscOperationEnable,
       "gepoel2esw12OnuMiscOperationDisable": gepoel2esw12OnuMiscOperationDisable,
       "gepoel2esw12OnuMiscOperationReset": gepoel2esw12OnuMiscOperationReset,
       "gepoel2esw12OnuMiscOperationRestore": gepoel2esw12OnuMiscOperationRestore,
       "gepoel2esw12OnuMiscOperationExportFilePath": gepoel2esw12OnuMiscOperationExportFilePath,
       "gepoel2esw12OnuMiscOperationDoExport": gepoel2esw12OnuMiscOperationDoExport,
       "gepoel2esw12OnuMiscOperationImportFilePath": gepoel2esw12OnuMiscOperationImportFilePath,
       "gepoel2esw12OnuMiscOperationDoImport": gepoel2esw12OnuMiscOperationDoImport,
       "gepoel2esw12OnuMiscOperationRFModule": gepoel2esw12OnuMiscOperationRFModule,
       "gepoel2esw12OnuGreenPonTable": gepoel2esw12OnuGreenPonTable,
       "gepoel2esw12OnuGreenPonEntry": gepoel2esw12OnuGreenPonEntry,
       "gepoel2esw12OnuGreenPonOltPort": gepoel2esw12OnuGreenPonOltPort,
       "gepoel2esw12OnuGreenPonMacAddress": gepoel2esw12OnuGreenPonMacAddress,
       "gepoel2esw12OnuGreenPonEnable": gepoel2esw12OnuGreenPonEnable,
       "gepoel2esw12OnuPowerSaveEnable": gepoel2esw12OnuPowerSaveEnable,
       "gepoel2esw12OnuGreenPonPDnLaserTransmit": gepoel2esw12OnuGreenPonPDnLaserTransmit,
       "gepoel2esw12OnuGreenPonPDnLaserRecv": gepoel2esw12OnuGreenPonPDnLaserRecv,
       "gepoel2esw12OnuGreenPonPDnSerdes": gepoel2esw12OnuGreenPonPDnSerdes,
       "gepoel2esw12OnuAuthorization": gepoel2esw12OnuAuthorization,
       "gepoel2esw12OnuAuthorizationTable": gepoel2esw12OnuAuthorizationTable,
       "gepoel2esw12OnuAuthorizationEntry": gepoel2esw12OnuAuthorizationEntry,
       "gepoel2esw12OnuAuthorizationOltPort": gepoel2esw12OnuAuthorizationOltPort,
       "gepoel2esw12OnuAuthorizationMacAddress": gepoel2esw12OnuAuthorizationMacAddress,
       "gepoel2esw12OnuAuthorizationAllLinks": gepoel2esw12OnuAuthorizationAllLinks,
       "gepoel2esw12OnuAuthorizationStatus": gepoel2esw12OnuAuthorizationStatus,
       "gepoel2esw12OnuAuthorizations": gepoel2esw12OnuAuthorizations,
       "gepoel2esw12OnuAuthorize": gepoel2esw12OnuAuthorize,
       "gepoel2esw12OnuAuthorizationAdd": gepoel2esw12OnuAuthorizationAdd,
       "gepoel2esw12OnuAuthorizationAddOltPort": gepoel2esw12OnuAuthorizationAddOltPort,
       "gepoel2esw12OnuAuthorizationAddOnuMac": gepoel2esw12OnuAuthorizationAddOnuMac,
       "gepoel2esw12OnuAuthorizationAddLinkNumber": gepoel2esw12OnuAuthorizationAddLinkNumber,
       "gepoel2esw12OnuAuthorizationAddDo": gepoel2esw12OnuAuthorizationAddDo,
       "gepoel2esw12LlidManagement": gepoel2esw12LlidManagement,
       "gepoel2esw12LinkQue": gepoel2esw12LinkQue,
       "gepoel2esw12LinkSLATable": gepoel2esw12LinkSLATable,
       "gepoel2esw12LinkSLAEntry": gepoel2esw12LinkSLAEntry,
       "gepoel2esw12LinkOltPort": gepoel2esw12LinkOltPort,
       "gepoel2esw12LinkMacAddress": gepoel2esw12LinkMacAddress,
       "gepoel2esw12LinkSLAMinShaperEnable": gepoel2esw12LinkSLAMinShaperEnable,
       "gepoel2esw12LinkSLAMaxShaperMaxBw": gepoel2esw12LinkSLAMaxShaperMaxBw,
       "gepoel2esw12LinkSLAMaxShaperMaxBurst": gepoel2esw12LinkSLAMaxShaperMaxBurst,
       "gepoel2esw12LinkSLAMaxShaperSchedulerLevel": gepoel2esw12LinkSLAMaxShaperSchedulerLevel,
       "gepoel2esw12LinkSLAMaxShaperSchedulerWeight": gepoel2esw12LinkSLAMaxShaperSchedulerWeight,
       "gepoel2esw12LinkSLAMinShaperMinBw": gepoel2esw12LinkSLAMinShaperMinBw,
       "gepoel2esw12LinkSLAMinShaperMaxBurst": gepoel2esw12LinkSLAMinShaperMaxBurst,
       "gepoel2esw12LinkSLAMinShaperSchedulerLevel": gepoel2esw12LinkSLAMinShaperSchedulerLevel,
       "gepoel2esw12LinkSLAMinShaperSchedulerWeight": gepoel2esw12LinkSLAMinShaperSchedulerWeight,
       "gepoel2esw12LinkUpQSLATable": gepoel2esw12LinkUpQSLATable,
       "gepoel2esw12LinkUpQSLAEntry": gepoel2esw12LinkUpQSLAEntry,
       "gepoel2esw12LinkUpQOltPort": gepoel2esw12LinkUpQOltPort,
       "gepoel2esw12LinkUpQMacAddress": gepoel2esw12LinkUpQMacAddress,
       "gepoel2esw12LinkUpQSLAMinShaperEnable": gepoel2esw12LinkUpQSLAMinShaperEnable,
       "gepoel2esw12LinkUpQSLAMaxShaperMaxBw": gepoel2esw12LinkUpQSLAMaxShaperMaxBw,
       "gepoel2esw12LinkUpQSLAMaxShaperMaxBurst": gepoel2esw12LinkUpQSLAMaxShaperMaxBurst,
       "gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel": gepoel2esw12LinkUpQSLAMaxShaperSchedulerLevel,
       "gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight": gepoel2esw12LinkUpQSLAMaxShaperSchedulerWeight,
       "gepoel2esw12LinkUpQSLAMinShaperMinBw": gepoel2esw12LinkUpQSLAMinShaperMinBw,
       "gepoel2esw12LinkUpQSLAMinShaperMaxBurst": gepoel2esw12LinkUpQSLAMinShaperMaxBurst,
       "gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel": gepoel2esw12LinkUpQSLAMinShaperSchedulerLevel,
       "gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight": gepoel2esw12LinkUpQSLAMinShaperSchedulerWeight,
       "gepoel2esw12LinkDnQSLATable": gepoel2esw12LinkDnQSLATable,
       "gepoel2esw12LinkDnQSLAEntry": gepoel2esw12LinkDnQSLAEntry,
       "gepoel2esw12LinkDnQOltPort": gepoel2esw12LinkDnQOltPort,
       "gepoel2esw12LinkDnQMacAddress": gepoel2esw12LinkDnQMacAddress,
       "gepoel2esw12LinkDnQSLAMinShaperEnable": gepoel2esw12LinkDnQSLAMinShaperEnable,
       "gepoel2esw12LinkDnQSLAMaxShaperMaxBw": gepoel2esw12LinkDnQSLAMaxShaperMaxBw,
       "gepoel2esw12LinkDnQSLAMaxShaperMaxBurst": gepoel2esw12LinkDnQSLAMaxShaperMaxBurst,
       "gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel": gepoel2esw12LinkDnQSLAMaxShaperSchedulerLevel,
       "gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight": gepoel2esw12LinkDnQSLAMaxShaperSchedulerWeight,
       "gepoel2esw12LinkDnQSLAMinShaperMinBw": gepoel2esw12LinkDnQSLAMinShaperMinBw,
       "gepoel2esw12LinkDnQSLAMinShaperMaxBurst": gepoel2esw12LinkDnQSLAMinShaperMaxBurst,
       "gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel": gepoel2esw12LinkDnQSLAMinShaperSchedulerLevel,
       "gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight": gepoel2esw12LinkDnQSLAMinShaperSchedulerWeight,
       "gepoel2esw12LinkMulticastSLATable": gepoel2esw12LinkMulticastSLATable,
       "gepoel2esw12LinkMulticastSLAEntry": gepoel2esw12LinkMulticastSLAEntry,
       "gepoel2esw12LinkMulticastOltPort": gepoel2esw12LinkMulticastOltPort,
       "gepoel2esw12LinkMulticastMacAddress": gepoel2esw12LinkMulticastMacAddress,
       "gepoel2esw12LinkMulticastSLAMinShaperEnable": gepoel2esw12LinkMulticastSLAMinShaperEnable,
       "gepoel2esw12LinkMulticastSLAMaxShaperMaxBw": gepoel2esw12LinkMulticastSLAMaxShaperMaxBw,
       "gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst": gepoel2esw12LinkMulticastSLAMaxShaperMaxBurst,
       "gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel": gepoel2esw12LinkMulticastSLAMaxShaperSchedulerLevel,
       "gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight": gepoel2esw12LinkMulticastSLAMaxShaperSchedulerWeight,
       "gepoel2esw12LinkMulticastSLAMinShaperMinBw": gepoel2esw12LinkMulticastSLAMinShaperMinBw,
       "gepoel2esw12LinkMulticastSLAMinShaperMaxBurst": gepoel2esw12LinkMulticastSLAMinShaperMaxBurst,
       "gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel": gepoel2esw12LinkMulticastSLAMinShaperSchedulerLevel,
       "gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight": gepoel2esw12LinkMulticastSLAMinShaperSchedulerWeight,
       "gepoel2esw12LinkBridge": gepoel2esw12LinkBridge,
       "gepoel2esw12LinkBridgeModeTable": gepoel2esw12LinkBridgeModeTable,
       "gepoel2esw12LinkBridgeModeEntry": gepoel2esw12LinkBridgeModeEntry,
       "gepoel2esw12LinkBridgeOltPort": gepoel2esw12LinkBridgeOltPort,
       "gepoel2esw12LinkBridgeLinkMacAddress": gepoel2esw12LinkBridgeLinkMacAddress,
       "gepoel2esw12LinkBridgeMode": gepoel2esw12LinkBridgeMode,
       "gepoel2esw12LinkBridgeDestNNI": gepoel2esw12LinkBridgeDestNNI,
       "gepoel2esw12LinkEntryLimit": gepoel2esw12LinkEntryLimit,
       "gepoel2esw12LinkVlan": gepoel2esw12LinkVlan,
       "gepoel2esw12LinkUpstreamCoS": gepoel2esw12LinkUpstreamCoS,
       "gepoel2esw12LinkMaxToSCoS": gepoel2esw12LinkMaxToSCoS,
       "gepoel2esw12LinkMinToSCoS": gepoel2esw12LinkMinToSCoS,
       "gepoel2esw12LinkUsingCosTos": gepoel2esw12LinkUsingCosTos,
       "gepoel2esw12LinkNonIP": gepoel2esw12LinkNonIP,
       "gepoel2esw12LinkBridgeModeDel": gepoel2esw12LinkBridgeModeDel,
       "gepoel2esw12LinkDelBridgeOltPort": gepoel2esw12LinkDelBridgeOltPort,
       "gepoel2esw12LinkDelBridgeLinkMacAddress": gepoel2esw12LinkDelBridgeLinkMacAddress,
       "gepoel2esw12LinkDelBridgeMode": gepoel2esw12LinkDelBridgeMode,
       "gepoel2esw12D0DelLinkBridgeMode": gepoel2esw12D0DelLinkBridgeMode,
       "gepoel2esw12LinkBridgeModeAdd": gepoel2esw12LinkBridgeModeAdd,
       "gepoel2esw12LinkAddBridgeOltPort": gepoel2esw12LinkAddBridgeOltPort,
       "gepoel2esw12LinkAddBridgeLinkMacAddress": gepoel2esw12LinkAddBridgeLinkMacAddress,
       "gepoel2esw12LinkAddBridgeMode": gepoel2esw12LinkAddBridgeMode,
       "gepoel2esw12LinkAddBridgeDestNNI": gepoel2esw12LinkAddBridgeDestNNI,
       "gepoel2esw12LinkAddEntryLimit": gepoel2esw12LinkAddEntryLimit,
       "gepoel2esw12LinkAddVlan": gepoel2esw12LinkAddVlan,
       "gepoel2esw12LinkAddMaxVlan": gepoel2esw12LinkAddMaxVlan,
       "gepoel2esw12LinkAddUpstreamCoS": gepoel2esw12LinkAddUpstreamCoS,
       "gepoel2esw12LinkAddMaxToSCoS": gepoel2esw12LinkAddMaxToSCoS,
       "gepoel2esw12LinkAddMinToSCoS": gepoel2esw12LinkAddMinToSCoS,
       "gepoel2esw12LinkAddUsingCosTos": gepoel2esw12LinkAddUsingCosTos,
       "gepoel2esw12LinkAddNonIP": gepoel2esw12LinkAddNonIP,
       "gepoel2esw12DoLinkAddBridgeMode": gepoel2esw12DoLinkAddBridgeMode,
       "gepoel2esw12LinkVlanTagDel": gepoel2esw12LinkVlanTagDel,
       "gepoel2esw12LinkDelVlanOltPort": gepoel2esw12LinkDelVlanOltPort,
       "gepoel2esw12LinkDelVlanMacAddress": gepoel2esw12LinkDelVlanMacAddress,
       "gepoel2esw12LinkDelVlan": gepoel2esw12LinkDelVlan,
       "gepoel2esw12LinkDelMaxVlan": gepoel2esw12LinkDelMaxVlan,
       "gepoel2esw12LinkDelUpstreamCos": gepoel2esw12LinkDelUpstreamCos,
       "gepoel2esw12DoLinkDelVlan": gepoel2esw12DoLinkDelVlan,
       "gepoel2esw12LinkStatistics": gepoel2esw12LinkStatistics,
       "gepoel2esw12LinkStatisticsOltSideTable": gepoel2esw12LinkStatisticsOltSideTable,
       "gepoel2esw12LinkStatisticsOltSideEntry": gepoel2esw12LinkStatisticsOltSideEntry,
       "gepoel2esw12LinkStaticOltSideOltPort": gepoel2esw12LinkStaticOltSideOltPort,
       "gepoel2esw12LinkStaticOltSideLinkMacAddress": gepoel2esw12LinkStaticOltSideLinkMacAddress,
       "gepoel2esw12LinkStatisticsOltSideIndex": gepoel2esw12LinkStatisticsOltSideIndex,
       "gepoel2esw12LinkStatisticsOltSideBytes": gepoel2esw12LinkStatisticsOltSideBytes,
       "gepoel2esw12LinkStatisticsOltSideTotalFrame": gepoel2esw12LinkStatisticsOltSideTotalFrame,
       "gepoel2esw12LinkStatisticsOltSideUnicastFrame": gepoel2esw12LinkStatisticsOltSideUnicastFrame,
       "gepoel2esw12LinkStatisticsOltSideBroadcastFrame": gepoel2esw12LinkStatisticsOltSideBroadcastFrame,
       "gepoel2esw12LinkStatisticsOltSideMulticastFrame": gepoel2esw12LinkStatisticsOltSideMulticastFrame,
       "gepoel2esw12LinkStatisticsOltSideUndersizeFrame": gepoel2esw12LinkStatisticsOltSideUndersizeFrame,
       "gepoel2esw12LinkStatisticsOltSideOversizedFrame": gepoel2esw12LinkStatisticsOltSideOversizedFrame,
       "gepoel2esw12LinkStatisticsOltSideFCSErrors": gepoel2esw12LinkStatisticsOltSideFCSErrors,
       "gepoel2esw12LinkStatisticsOltSide64OctetFrame": gepoel2esw12LinkStatisticsOltSide64OctetFrame,
       "gepoel2esw12LinkStatisticsOltSide65to127OctetFrame": gepoel2esw12LinkStatisticsOltSide65to127OctetFrame,
       "gepoel2esw12LinkStatisticsOltSide128to255OctetFrame": gepoel2esw12LinkStatisticsOltSide128to255OctetFrame,
       "gepoel2esw12LinkStatisticsOltSide256to511OctetFrame": gepoel2esw12LinkStatisticsOltSide256to511OctetFrame,
       "gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame": gepoel2esw12LinkStatisticsOltSide512to1023OctetFrame,
       "gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame": gepoel2esw12LinkStatisticsOltSide1024to1518OctetFrame,
       "gepoel2esw12LinkStatisticsOltSide1519upOctetFrame": gepoel2esw12LinkStatisticsOltSide1519upOctetFrame,
       "gepoel2esw12LinkStatisticsOltSideFramesDropped": gepoel2esw12LinkStatisticsOltSideFramesDropped,
       "gepoel2esw12LinkStatisticsOltSideMPCPFrames": gepoel2esw12LinkStatisticsOltSideMPCPFrames,
       "gepoel2esw12LinkStatisticsOltSideMPCPBytes": gepoel2esw12LinkStatisticsOltSideMPCPBytes,
       "gepoel2esw12LinkStatisticsOltSideReportFrames": gepoel2esw12LinkStatisticsOltSideReportFrames,
       "gepoel2esw12LinkStatisticsOltSideReportBytes": gepoel2esw12LinkStatisticsOltSideReportBytes,
       "gepoel2esw12LinkStatisticsOltSideOAMFrame": gepoel2esw12LinkStatisticsOltSideOAMFrame,
       "gepoel2esw12LinkStatisticsOltSideOAMBytes": gepoel2esw12LinkStatisticsOltSideOAMBytes,
       "gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest": gepoel2esw12LinkStatisticsOltSideMPCPRegisterRequest,
       "gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck": gepoel2esw12LinkStatisticsOltSideMPCPRegisterAck,
       "gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame": gepoel2esw12LinkStatisticsOltSideMPCPRegisterFrame,
       "gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame": gepoel2esw12LinkStatisticsOltSideMPCPGatesFrame,
       "gepoel2esw12LinkStatisticsOltSideLineCodeError": gepoel2esw12LinkStatisticsOltSideLineCodeError,
       "gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax": gepoel2esw12LinkStatisticsOltSideLineCodeErrorMax,
       "gepoel2esw12LinkStatisticsOltSideLaserPower": gepoel2esw12LinkStatisticsOltSideLaserPower,
       "gepoel2esw12LinkStatisticsOltSideGateFrames": gepoel2esw12LinkStatisticsOltSideGateFrames,
       "gepoel2esw12LinkStatisticsOltSideGateBytes": gepoel2esw12LinkStatisticsOltSideGateBytes,
       "gepoel2esw12LinkStatisticsOltSideClear": gepoel2esw12LinkStatisticsOltSideClear,
       "gepoel2esw12LinkStatisticsOnuSideTable": gepoel2esw12LinkStatisticsOnuSideTable,
       "gepoel2esw12LinkStatisticsOnuSideEntry": gepoel2esw12LinkStatisticsOnuSideEntry,
       "gepoel2esw12LinkStaticOnuSideOltPort": gepoel2esw12LinkStaticOnuSideOltPort,
       "gepoel2esw12LinkStaticOnuSideLinkMacAddress": gepoel2esw12LinkStaticOnuSideLinkMacAddress,
       "gepoel2esw12LinkStatisticsOnuSideIndex": gepoel2esw12LinkStatisticsOnuSideIndex,
       "gepoel2esw12LinkStatisticsOnuSideBytes": gepoel2esw12LinkStatisticsOnuSideBytes,
       "gepoel2esw12LinkStatisticsOnuSideTotalFrame": gepoel2esw12LinkStatisticsOnuSideTotalFrame,
       "gepoel2esw12LinkStatisticsOnuSideUnicastFrame": gepoel2esw12LinkStatisticsOnuSideUnicastFrame,
       "gepoel2esw12LinkStatisticsOnuSideBroadcastFrame": gepoel2esw12LinkStatisticsOnuSideBroadcastFrame,
       "gepoel2esw12LinkStatisticsOnuSideMulticastFrame": gepoel2esw12LinkStatisticsOnuSideMulticastFrame,
       "gepoel2esw12LinkStatisticsOnuSide64OctetFrame": gepoel2esw12LinkStatisticsOnuSide64OctetFrame,
       "gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame": gepoel2esw12LinkStatisticsOnuSide65to127OctetFrame,
       "gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame": gepoel2esw12LinkStatisticsOnuSide128to255OctetFrame,
       "gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame": gepoel2esw12LinkStatisticsOnuSide256to511OctetFrame,
       "gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame": gepoel2esw12LinkStatisticsOnuSide512to1023OctetFrame,
       "gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame": gepoel2esw12LinkStatisticsOnuSide1024to1518OctetFrame,
       "gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame": gepoel2esw12LinkStatisticsOnuSide1519upOctetFrame,
       "gepoel2esw12LinkStatisticsOnuSideUndersizeFrame": gepoel2esw12LinkStatisticsOnuSideUndersizeFrame,
       "gepoel2esw12LinkStatisticsOnuSideFCSErrors": gepoel2esw12LinkStatisticsOnuSideFCSErrors,
       "gepoel2esw12LinkStatisticsOnuSideBytesDropped": gepoel2esw12LinkStatisticsOnuSideBytesDropped,
       "gepoel2esw12LinkStatisticsOnuSideFramesDropped": gepoel2esw12LinkStatisticsOnuSideFramesDropped,
       "gepoel2esw12LinkStatisticsOnuSideBytesDelayed": gepoel2esw12LinkStatisticsOnuSideBytesDelayed,
       "gepoel2esw12LinkStatisticsOnuSideMaximumDelayed": gepoel2esw12LinkStatisticsOnuSideMaximumDelayed,
       "gepoel2esw12LinkStatisticsOnuSideDelayThreshold": gepoel2esw12LinkStatisticsOnuSideDelayThreshold,
       "gepoel2esw12LinkStatisticsOnuSideOAMFrames": gepoel2esw12LinkStatisticsOnuSideOAMFrames,
       "gepoel2esw12LinkStatisticsOnuSideErroredFrames": gepoel2esw12LinkStatisticsOnuSideErroredFrames,
       "gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods": gepoel2esw12LinkStatisticsOnuSideErroredFramePeriods,
       "gepoel2esw12LinkStatisticsOnuSideMPCPGates": gepoel2esw12LinkStatisticsOnuSideMPCPGates,
       "gepoel2esw12LinkStatisticsOnuSideMPCPRegister": gepoel2esw12LinkStatisticsOnuSideMPCPRegister,
       "gepoel2esw12LinkStatisticsOnuSideMPCPReport": gepoel2esw12LinkStatisticsOnuSideMPCPReport,
       "gepoel2esw12LinkStatisticsOnuSideMPCPRequest": gepoel2esw12LinkStatisticsOnuSideMPCPRequest,
       "gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck": gepoel2esw12LinkStatisticsOnuSideMPCPRegisterAck,
       "gepoel2esw12LinkStatisticsOnuSideUnused": gepoel2esw12LinkStatisticsOnuSideUnused,
       "gepoel2esw12LinkStatisticsOnuSideClear": gepoel2esw12LinkStatisticsOnuSideClear,
       "gepoel2esw12LinkMiscOperationTable": gepoel2esw12LinkMiscOperationTable,
       "gepoel2esw12LinkMiscOperationEntry": gepoel2esw12LinkMiscOperationEntry,
       "gepoel2esw12LinkMiscOptOltPort": gepoel2esw12LinkMiscOptOltPort,
       "gepoel2esw12LinkMiscOptLinkMacAddress": gepoel2esw12LinkMiscOptLinkMacAddress,
       "gepoel2esw12LinkBlockState": gepoel2esw12LinkBlockState,
       "gepoel2esw12Configuration": gepoel2esw12Configuration,
       "gepoel2esw12TrapEventSeverity": gepoel2esw12TrapEventSeverity,
       "gepoel2esw12TrapEventSeverityAccessMgmt": gepoel2esw12TrapEventSeverityAccessMgmt,
       "gepoel2esw12TrapEventSeverityAuthFailed": gepoel2esw12TrapEventSeverityAuthFailed,
       "gepoel2esw12TrapEventSeverityColdStart": gepoel2esw12TrapEventSeverityColdStart,
       "gepoel2esw12TrapEventSeverityConfigInfo": gepoel2esw12TrapEventSeverityConfigInfo,
       "gepoel2esw12TrapEventSeverityDyingGaspPowerFailure": gepoel2esw12TrapEventSeverityDyingGaspPowerFailure,
       "gepoel2esw12TrapEventSeverityEPONLinkDown": gepoel2esw12TrapEventSeverityEPONLinkDown,
       "gepoel2esw12TrapEventSeverityEPONLinkUp": gepoel2esw12TrapEventSeverityEPONLinkUp,
       "gepoel2esw12TrapEventSeverityFirmwareUpgrade": gepoel2esw12TrapEventSeverityFirmwareUpgrade,
       "gepoel2esw12TrapEventSeverityJumboFrameReceivedError": gepoel2esw12TrapEventSeverityJumboFrameReceivedError,
       "gepoel2esw12TrapEventSeverityKeyExchangeFailure": gepoel2esw12TrapEventSeverityKeyExchangeFailure,
       "gepoel2esw12TrapEventSeverityLogin": gepoel2esw12TrapEventSeverityLogin,
       "gepoel2esw12TrapEventSeverityLogout": gepoel2esw12TrapEventSeverityLogout,
       "gepoel2esw12TrapEventSeverityLoopback": gepoel2esw12TrapEventSeverityLoopback,
       "gepoel2esw12TrapEventSeverityMACLearningTableOverflow": gepoel2esw12TrapEventSeverityMACLearningTableOverflow,
       "gepoel2esw12TrapEventSeverityMgmtIPChange": gepoel2esw12TrapEventSeverityMgmtIPChange,
       "gepoel2esw12TrapEventSeverityNumberOfLinksExceeded": gepoel2esw12TrapEventSeverityNumberOfLinksExceeded,
       "gepoel2esw12TrapEventSeverityOLTBad": gepoel2esw12TrapEventSeverityOLTBad,
       "gepoel2esw12TrapEventSeverityONUPowerAbnormal": gepoel2esw12TrapEventSeverityONUPowerAbnormal,
       "gepoel2esw12TrapEventSeverityPasswdChange": gepoel2esw12TrapEventSeverityPasswdChange,
       "gepoel2esw12TrapEventSeverityQueueOverflow": gepoel2esw12TrapEventSeverityQueueOverflow,
       "gepoel2esw12TrapEventSeverityStandardDyingGasp": gepoel2esw12TrapEventSeverityStandardDyingGasp,
       "gepoel2esw12TrapEventSeverityStandardLinkFault": gepoel2esw12TrapEventSeverityStandardLinkFault,
       "gepoel2esw12TrapEventSeverityStatisticsAlarm": gepoel2esw12TrapEventSeverityStatisticsAlarm,
       "gepoel2esw12TrapEventSeverityUNILinkDown": gepoel2esw12TrapEventSeverityUNILinkDown,
       "gepoel2esw12TrapEventSeverityUNILinkUp": gepoel2esw12TrapEventSeverityUNILinkUp,
       "gepoel2esw12TrapEventSeverityWarmStart": gepoel2esw12TrapEventSeverityWarmStart,
       "gepoel2esw12SMTP": gepoel2esw12SMTP,
       "gepoel2esw12SMTPMailServer": gepoel2esw12SMTPMailServer,
       "gepoel2esw12SMTPUserName": gepoel2esw12SMTPUserName,
       "gepoel2esw12SMTPPassword": gepoel2esw12SMTPPassword,
       "gepoel2esw12SMTPServeriryLevel": gepoel2esw12SMTPServeriryLevel,
       "gepoel2esw12SMTPSender": gepoel2esw12SMTPSender,
       "gepoel2esw12SMTPReturnPath": gepoel2esw12SMTPReturnPath,
       "gepoel2esw12SMTPEmailAddress1": gepoel2esw12SMTPEmailAddress1,
       "gepoel2esw12SMTPEmailAddress2": gepoel2esw12SMTPEmailAddress2,
       "gepoel2esw12SMTPEmailAddress3": gepoel2esw12SMTPEmailAddress3,
       "gepoel2esw12SMTPEmailAddress4": gepoel2esw12SMTPEmailAddress4,
       "gepoel2esw12SMTPEmailAddress5": gepoel2esw12SMTPEmailAddress5,
       "gepoel2esw12SMTPEmailAddress6": gepoel2esw12SMTPEmailAddress6,
       "gepoel2esw12Security": gepoel2esw12Security,
       "gepoel2esw12AccessManagement": gepoel2esw12AccessManagement,
       "gepoel2esw12AccessMgtConf": gepoel2esw12AccessMgtConf,
       "gepoel2esw12AccessMgtConfMode": gepoel2esw12AccessMgtConfMode,
       "gepoel2esw12AccessMgtConfCreate": gepoel2esw12AccessMgtConfCreate,
       "gepoel2esw12AccessMgtConfTable": gepoel2esw12AccessMgtConfTable,
       "gepoel2esw12AccessMgtConfEntry": gepoel2esw12AccessMgtConfEntry,
       "gepoel2esw12AccessMgtIndex": gepoel2esw12AccessMgtIndex,
       "gepoel2esw12AccessMgtAddresstype": gepoel2esw12AccessMgtAddresstype,
       "gepoel2esw12AccessMgtStartIpAddress": gepoel2esw12AccessMgtStartIpAddress,
       "gepoel2esw12AccessMgtEndIpAddress": gepoel2esw12AccessMgtEndIpAddress,
       "gepoel2esw12AccessMgtHttpHttps": gepoel2esw12AccessMgtHttpHttps,
       "gepoel2esw12AccessMgtSNMP": gepoel2esw12AccessMgtSNMP,
       "gepoel2esw12AccessMgtTelnetSSH": gepoel2esw12AccessMgtTelnetSSH,
       "gepoel2esw12AccessMgtRowStatus": gepoel2esw12AccessMgtRowStatus,
       "gepoel2esw12AccessMgtStatistics": gepoel2esw12AccessMgtStatistics,
       "gepoel2esw12HttpReceivedPkts": gepoel2esw12HttpReceivedPkts,
       "gepoel2esw12HttpAllowedPkts": gepoel2esw12HttpAllowedPkts,
       "gepoel2esw12HttpDiscardedPkts": gepoel2esw12HttpDiscardedPkts,
       "gepoel2esw12HttpsReceivedPkts": gepoel2esw12HttpsReceivedPkts,
       "gepoel2esw12HttpsAllowedPkts": gepoel2esw12HttpsAllowedPkts,
       "gepoel2esw12HttpsDiscardedPkts": gepoel2esw12HttpsDiscardedPkts,
       "gepoel2esw12SnmpReceivedPkts": gepoel2esw12SnmpReceivedPkts,
       "gepoel2esw12SnmpAllowedPkts": gepoel2esw12SnmpAllowedPkts,
       "gepoel2esw12SnmpDiscardedPkts": gepoel2esw12SnmpDiscardedPkts,
       "gepoel2esw12TelnetReceivedPkts": gepoel2esw12TelnetReceivedPkts,
       "gepoel2esw12TelnetAllowedPkts": gepoel2esw12TelnetAllowedPkts,
       "gepoel2esw12TelnetDiscardedPkts": gepoel2esw12TelnetDiscardedPkts,
       "gepoel2esw12SSHReceivedPkts": gepoel2esw12SSHReceivedPkts,
       "gepoel2esw12SSHAllowedPkts": gepoel2esw12SSHAllowedPkts,
       "gepoel2esw12SSHDiscardedPkts": gepoel2esw12SSHDiscardedPkts,
       "gepoel2esw12AccessMgtStatisticsClearAll": gepoel2esw12AccessMgtStatisticsClearAll,
       "gepoel2esw12SSH": gepoel2esw12SSH,
       "gepoel2esw12SSHMode": gepoel2esw12SSHMode,
       "gepoel2esw12HTTPS": gepoel2esw12HTTPS,
       "gepoel2esw12HTTPSMode": gepoel2esw12HTTPSMode,
       "gepoel2esw12HTTPSAutoRedirect": gepoel2esw12HTTPSAutoRedirect,
       "gepoel2esw12AuthMethod": gepoel2esw12AuthMethod,
       "gepoel2esw12ConsoleAuthMethod": gepoel2esw12ConsoleAuthMethod,
       "gepoel2esw12ConsoleFallback": gepoel2esw12ConsoleFallback,
       "gepoel2esw12TelnetAuthMethod": gepoel2esw12TelnetAuthMethod,
       "gepoel2esw12TelnetFallback": gepoel2esw12TelnetFallback,
       "gepoel2esw12SshAuthMethod": gepoel2esw12SshAuthMethod,
       "gepoel2esw12SshFallback": gepoel2esw12SshFallback,
       "gepoel2esw12WebAuthMethod": gepoel2esw12WebAuthMethod,
       "gepoel2esw12WebFallback": gepoel2esw12WebFallback,
       "gepoel2esw12Maintenance": gepoel2esw12Maintenance,
       "gepoel2esw12RestartDevice": gepoel2esw12RestartDevice,
       "gepoel2esw12Firmware": gepoel2esw12Firmware,
       "gepoel2esw12FirmwareIpAddress": gepoel2esw12FirmwareIpAddress,
       "gepoel2esw12FirmwareFileName": gepoel2esw12FirmwareFileName,
       "gepoel2esw12DoFirmwareUpgrade": gepoel2esw12DoFirmwareUpgrade,
       "gepoel2esw12SaveOrRestore": gepoel2esw12SaveOrRestore,
       "gepoel2esw12FactoryDefaults": gepoel2esw12FactoryDefaults,
       "gepoel2esw12SaveStart": gepoel2esw12SaveStart,
       "gepoel2esw12SaveUser": gepoel2esw12SaveUser,
       "gepoel2esw12RestoreUser": gepoel2esw12RestoreUser,
       "gepoel2esw12Diagnostics": gepoel2esw12Diagnostics,
       "gepoel2esw12PingIpAddress": gepoel2esw12PingIpAddress,
       "gepoel2esw12PingSize": gepoel2esw12PingSize,
       "gepoel2esw12DoPingConfig": gepoel2esw12DoPingConfig,
       "gepoel2esw12PingResult": gepoel2esw12PingResult,
       "gepoel2esw12Ping6IpAddress": gepoel2esw12Ping6IpAddress,
       "gepoel2esw12Ping6Size": gepoel2esw12Ping6Size,
       "gepoel2esw12DoPing6Config": gepoel2esw12DoPing6Config,
       "gepoel2esw12Ping6Result": gepoel2esw12Ping6Result,
       "gepoel2esw12Trap": gepoel2esw12Trap,
       "gepoel2esw12TrapEvent": gepoel2esw12TrapEvent,
       "gepoel2esw12Emergency": gepoel2esw12Emergency,
       "gepoel2esw12Alert": gepoel2esw12Alert,
       "gepoel2esw12Critical": gepoel2esw12Critical,
       "gepoel2esw12Error": gepoel2esw12Error,
       "gepoel2esw12Warning": gepoel2esw12Warning,
       "gepoel2esw12Notice": gepoel2esw12Notice,
       "gepoel2esw12Informational": gepoel2esw12Informational,
       "gepoel2esw12Debug": gepoel2esw12Debug,
       "gepoel2esw12TrapVariable": gepoel2esw12TrapVariable,
       "gepoel2esw12Information": gepoel2esw12Information}
)
