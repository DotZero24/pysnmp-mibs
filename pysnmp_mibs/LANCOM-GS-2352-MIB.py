# SNMP MIB module (LANCOM-GS-2352-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-GS-2352-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:28 2025
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

lancom_systems = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwitchingSystems_ObjectIdentity = ObjectIdentity
switchingSystems = _SwitchingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800)
)
_GigabitEthernetSwitches_ObjectIdentity = ObjectIdentity
gigabitEthernetSwitches = _GigabitEthernetSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3)
)
_LancomGS2352_ObjectIdentity = ObjectIdentity
lancomGS2352 = _LancomGS2352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352)
)
_Gs2352System_ObjectIdentity = ObjectIdentity
gs2352System = _Gs2352System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1)
)
_Gs2352SystemInformation_ObjectIdentity = ObjectIdentity
gs2352SystemInformation = _Gs2352SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1)
)
_Gs2352ModelName_Type = DisplayString
_Gs2352ModelName_Object = MibScalar
gs2352ModelName = _Gs2352ModelName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 1),
    _Gs2352ModelName_Type()
)
gs2352ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ModelName.setStatus("current")
_Gs2352BIOSVersion_Type = DisplayString
_Gs2352BIOSVersion_Object = MibScalar
gs2352BIOSVersion = _Gs2352BIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 2),
    _Gs2352BIOSVersion_Type()
)
gs2352BIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352BIOSVersion.setStatus("current")
_Gs2352FirmwareVersion_Type = DisplayString
_Gs2352FirmwareVersion_Object = MibScalar
gs2352FirmwareVersion = _Gs2352FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 3),
    _Gs2352FirmwareVersion_Type()
)
gs2352FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FirmwareVersion.setStatus("current")
_Gs2352HardwareMechanicalVersion_Type = DisplayString
_Gs2352HardwareMechanicalVersion_Object = MibScalar
gs2352HardwareMechanicalVersion = _Gs2352HardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 4),
    _Gs2352HardwareMechanicalVersion_Type()
)
gs2352HardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HardwareMechanicalVersion.setStatus("current")
_Gs2352SerialNumber_Type = DisplayString
_Gs2352SerialNumber_Object = MibScalar
gs2352SerialNumber = _Gs2352SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 5),
    _Gs2352SerialNumber_Type()
)
gs2352SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SerialNumber.setStatus("current")
_Gs2352HostMACAddress_Type = MacAddress
_Gs2352HostMACAddress_Object = MibScalar
gs2352HostMACAddress = _Gs2352HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 6),
    _Gs2352HostMACAddress_Type()
)
gs2352HostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HostMACAddress.setStatus("current")
_Gs2352ConsoleBaudrate_Type = DisplayString
_Gs2352ConsoleBaudrate_Object = MibScalar
gs2352ConsoleBaudrate = _Gs2352ConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 7),
    _Gs2352ConsoleBaudrate_Type()
)
gs2352ConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ConsoleBaudrate.setStatus("current")
_Gs2352RAMSize_Type = DisplayString
_Gs2352RAMSize_Object = MibScalar
gs2352RAMSize = _Gs2352RAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 8),
    _Gs2352RAMSize_Type()
)
gs2352RAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RAMSize.setStatus("current")
_Gs2352FlashSize_Type = DisplayString
_Gs2352FlashSize_Object = MibScalar
gs2352FlashSize = _Gs2352FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 9),
    _Gs2352FlashSize_Type()
)
gs2352FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FlashSize.setStatus("current")
_Gs2352BridgeFDBSize_Type = DisplayString
_Gs2352BridgeFDBSize_Object = MibScalar
gs2352BridgeFDBSize = _Gs2352BridgeFDBSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 10),
    _Gs2352BridgeFDBSize_Type()
)
gs2352BridgeFDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352BridgeFDBSize.setStatus("current")
_Gs2352TransmitQueue_Type = DisplayString
_Gs2352TransmitQueue_Object = MibScalar
gs2352TransmitQueue = _Gs2352TransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 11),
    _Gs2352TransmitQueue_Type()
)
gs2352TransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352TransmitQueue.setStatus("current")
_Gs2352MaximumFrameSize_Type = DisplayString
_Gs2352MaximumFrameSize_Object = MibScalar
gs2352MaximumFrameSize = _Gs2352MaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 12),
    _Gs2352MaximumFrameSize_Type()
)
gs2352MaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MaximumFrameSize.setStatus("current")
_Gs2352CPULoad_Type = DisplayString
_Gs2352CPULoad_Object = MibScalar
gs2352CPULoad = _Gs2352CPULoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 13),
    _Gs2352CPULoad_Type()
)
gs2352CPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CPULoad.setStatus("current")
_Gs2352FanSpeed_Type = DisplayString
_Gs2352FanSpeed_Object = MibScalar
gs2352FanSpeed = _Gs2352FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 17),
    _Gs2352FanSpeed_Type()
)
gs2352FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FanSpeed.setStatus("current")
_Gs2352ACPower_Type = DisplayString
_Gs2352ACPower_Object = MibScalar
gs2352ACPower = _Gs2352ACPower_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 18),
    _Gs2352ACPower_Type()
)
gs2352ACPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACPower.setStatus("current")
_Gs2352Temperature_Type = DisplayString
_Gs2352Temperature_Object = MibScalar
gs2352Temperature = _Gs2352Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 19),
    _Gs2352Temperature_Type()
)
gs2352Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Temperature.setStatus("current")
_Gs2352SystemDescription_Type = DisplayString
_Gs2352SystemDescription_Object = MibScalar
gs2352SystemDescription = _Gs2352SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 21),
    _Gs2352SystemDescription_Type()
)
gs2352SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SystemDescription.setStatus("current")
_Gs2352Location_Type = DisplayString
_Gs2352Location_Object = MibScalar
gs2352Location = _Gs2352Location_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 22),
    _Gs2352Location_Type()
)
gs2352Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Location.setStatus("current")
_Gs2352Contact_Type = DisplayString
_Gs2352Contact_Object = MibScalar
gs2352Contact = _Gs2352Contact_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 23),
    _Gs2352Contact_Type()
)
gs2352Contact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Contact.setStatus("current")
_Gs2352DeviceName_Type = DisplayString
_Gs2352DeviceName_Object = MibScalar
gs2352DeviceName = _Gs2352DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 24),
    _Gs2352DeviceName_Type()
)
gs2352DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DeviceName.setStatus("current")
_Gs2352SystemDate_Type = DisplayString
_Gs2352SystemDate_Object = MibScalar
gs2352SystemDate = _Gs2352SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 25),
    _Gs2352SystemDate_Type()
)
gs2352SystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SystemDate.setStatus("current")
_Gs2352SystemUptime_Type = DisplayString
_Gs2352SystemUptime_Object = MibScalar
gs2352SystemUptime = _Gs2352SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 26),
    _Gs2352SystemUptime_Type()
)
gs2352SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SystemUptime.setStatus("current")
_Gs2352SystemIPv4Address_Type = DisplayString
_Gs2352SystemIPv4Address_Object = MibScalar
gs2352SystemIPv4Address = _Gs2352SystemIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 27),
    _Gs2352SystemIPv4Address_Type()
)
gs2352SystemIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SystemIPv4Address.setStatus("current")
_Gs2352SystemIPv4SubnetMask_Type = DisplayString
_Gs2352SystemIPv4SubnetMask_Object = MibScalar
gs2352SystemIPv4SubnetMask = _Gs2352SystemIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 28),
    _Gs2352SystemIPv4SubnetMask_Type()
)
gs2352SystemIPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SystemIPv4SubnetMask.setStatus("current")
_Gs2352SystemIPv4Gateway_Type = DisplayString
_Gs2352SystemIPv4Gateway_Object = MibScalar
gs2352SystemIPv4Gateway = _Gs2352SystemIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 29),
    _Gs2352SystemIPv4Gateway_Type()
)
gs2352SystemIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SystemIPv4Gateway.setStatus("current")
_Gs2352IPv6LinkLocalAddress_Type = DisplayString
_Gs2352IPv6LinkLocalAddress_Object = MibScalar
gs2352IPv6LinkLocalAddress = _Gs2352IPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 30),
    _Gs2352IPv6LinkLocalAddress_Type()
)
gs2352IPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv6LinkLocalAddress.setStatus("current")
_Gs2352IPv6Address_Type = DisplayString
_Gs2352IPv6Address_Object = MibScalar
gs2352IPv6Address = _Gs2352IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 31),
    _Gs2352IPv6Address_Type()
)
gs2352IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv6Address.setStatus("current")
_Gs2352IPv6Prefix_Type = DisplayString
_Gs2352IPv6Prefix_Object = MibScalar
gs2352IPv6Prefix = _Gs2352IPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 32),
    _Gs2352IPv6Prefix_Type()
)
gs2352IPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv6Prefix.setStatus("current")
_Gs2352IPv6Gateway_Type = DisplayString
_Gs2352IPv6Gateway_Object = MibScalar
gs2352IPv6Gateway = _Gs2352IPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 33),
    _Gs2352IPv6Gateway_Type()
)
gs2352IPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv6Gateway.setStatus("current")
_Gs2352LargestFreeMemBlock_Type = Integer32
_Gs2352LargestFreeMemBlock_Object = MibScalar
gs2352LargestFreeMemBlock = _Gs2352LargestFreeMemBlock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 1500),
    _Gs2352LargestFreeMemBlock_Type()
)
gs2352LargestFreeMemBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LargestFreeMemBlock.setStatus("current")
_Gs2352MemFree_Type = Integer32
_Gs2352MemFree_Object = MibScalar
gs2352MemFree = _Gs2352MemFree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 1, 1501),
    _Gs2352MemFree_Type()
)
gs2352MemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MemFree.setStatus("current")
_Gs2352SystemTime_ObjectIdentity = ObjectIdentity
gs2352SystemTime = _Gs2352SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2)
)
_Gs2352SystemTimeManual_ObjectIdentity = ObjectIdentity
gs2352SystemTimeManual = _Gs2352SystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1)
)


class _Gs2352SystemTimeManualClockSource_Type(Integer32):
    """Custom type gs2352SystemTimeManualClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useLocal", 0),
          ("useNTP", 1))
    )


_Gs2352SystemTimeManualClockSource_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualClockSource_Object = MibScalar
gs2352SystemTimeManualClockSource = _Gs2352SystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 1),
    _Gs2352SystemTimeManualClockSource_Type()
)
gs2352SystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualClockSource.setStatus("current")
_Gs2352SystemTimeManualLocaltime_Type = DisplayString
_Gs2352SystemTimeManualLocaltime_Object = MibScalar
gs2352SystemTimeManualLocaltime = _Gs2352SystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 2),
    _Gs2352SystemTimeManualLocaltime_Type()
)
gs2352SystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualLocaltime.setStatus("current")


class _Gs2352SystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type gs2352SystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Gs2352SystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualTimeZoneOffset_Object = MibScalar
gs2352SystemTimeManualTimeZoneOffset = _Gs2352SystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 3),
    _Gs2352SystemTimeManualTimeZoneOffset_Type()
)
gs2352SystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualTimeZoneOffset.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavings based on Integer32"""
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


_Gs2352SystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavings_Object = MibScalar
gs2352SystemTimeManualDaylightSavings = _Gs2352SystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 4),
    _Gs2352SystemTimeManualDaylightSavings_Type()
)
gs2352SystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavings.setStatus("current")


class _Gs2352SystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type gs2352SystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Gs2352SystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualTimeSetOffset_Object = MibScalar
gs2352SystemTimeManualTimeSetOffset = _Gs2352SystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 5),
    _Gs2352SystemTimeManualTimeSetOffset_Type()
)
gs2352SystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualTimeSetOffset.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("byDates", 0),
          ("recurring", 1))
    )


_Gs2352SystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsType_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsType = _Gs2352SystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 6),
    _Gs2352SystemTimeManualDaylightSavingsType_Type()
)
gs2352SystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsType.setStatus("current")
_Gs2352SystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Gs2352SystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsBydatesFrom = _Gs2352SystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 7),
    _Gs2352SystemTimeManualDaylightSavingsBydatesFrom_Type()
)
gs2352SystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Gs2352SystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Gs2352SystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsBydatesTo = _Gs2352SystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 8),
    _Gs2352SystemTimeManualDaylightSavingsBydatesTo_Type()
)
gs2352SystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
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
        *(("sunday", 0),
          ("monday", 1),
          ("tuseday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_Gs2352SystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringDayFrom = _Gs2352SystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 9),
    _Gs2352SystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
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
        *(("firstWeek", 1),
          ("secondWeek", 2),
          ("thirdWeek", 3),
          ("fourthWeek", 4),
          ("listWeek", 5))
    )


_Gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom = _Gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 10),
    _Gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_Gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom = _Gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 11),
    _Gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom = _Gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 12),
    _Gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
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
        *(("sunday", 0),
          ("monday", 1),
          ("tuseday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_Gs2352SystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringDayTo = _Gs2352SystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 13),
    _Gs2352SystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
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
        *(("firstWeek", 1),
          ("secondWeek", 2),
          ("thirdWeek", 3),
          ("fourthWeek", 4),
          ("listWeek", 5))
    )


_Gs2352SystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringWeekTo = _Gs2352SystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 14),
    _Gs2352SystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Gs2352SystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type gs2352SystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_Gs2352SystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Gs2352SystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringMonthTo = _Gs2352SystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 15),
    _Gs2352SystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Gs2352SystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Gs2352SystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
gs2352SystemTimeManualDaylightSavingsRecurringTimeTo = _Gs2352SystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 1, 16),
    _Gs2352SystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
gs2352SystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Gs2352SystemTimeNTP_ObjectIdentity = ObjectIdentity
gs2352SystemTimeNTP = _Gs2352SystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2)
)
_Gs2352SystemTimeNTPTable_Object = MibTable
gs2352SystemTimeNTPTable = _Gs2352SystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPTable.setStatus("current")
_Gs2352SystemTimeNTPEntry_Object = MibTableRow
gs2352SystemTimeNTPEntry = _Gs2352SystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 1, 1)
)
gs2352SystemTimeNTPEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPEntry.setStatus("current")


class _Gs2352SystemTimeNTPIndex_Type(Integer32):
    """Custom type gs2352SystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2352SystemTimeNTPIndex_Type.__name__ = "Integer32"
_Gs2352SystemTimeNTPIndex_Object = MibTableColumn
gs2352SystemTimeNTPIndex = _Gs2352SystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 1, 1, 1),
    _Gs2352SystemTimeNTPIndex_Type()
)
gs2352SystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPIndex.setStatus("current")


class _Gs2352SystemTimeNTPServerIPType_Type(Integer32):
    """Custom type gs2352SystemTimeNTPServerIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_Gs2352SystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Gs2352SystemTimeNTPServerIPType_Object = MibTableColumn
gs2352SystemTimeNTPServerIPType = _Gs2352SystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 1, 1, 2),
    _Gs2352SystemTimeNTPServerIPType_Type()
)
gs2352SystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPServerIPType.setStatus("current")
_Gs2352SystemTimeNTPServer_Type = DisplayString
_Gs2352SystemTimeNTPServer_Object = MibTableColumn
gs2352SystemTimeNTPServer = _Gs2352SystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 1, 1, 3),
    _Gs2352SystemTimeNTPServer_Type()
)
gs2352SystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPServer.setStatus("current")


class _Gs2352SystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type gs2352SystemTimeNTPCurrentMode based on Integer32"""
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
        *(("empty", 0),
          ("active", 1),
          ("edit", 2),
          ("delete", 3))
    )


_Gs2352SystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Gs2352SystemTimeNTPCurrentMode_Object = MibTableColumn
gs2352SystemTimeNTPCurrentMode = _Gs2352SystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 1, 1, 4),
    _Gs2352SystemTimeNTPCurrentMode_Type()
)
gs2352SystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPCurrentMode.setStatus("current")


class _Gs2352SystemTimeNTPRequestInterval_Type(Integer32):
    """Custom type gs2352SystemTimeNTPRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 999999999),
    )


_Gs2352SystemTimeNTPRequestInterval_Type.__name__ = "Integer32"
_Gs2352SystemTimeNTPRequestInterval_Object = MibScalar
gs2352SystemTimeNTPRequestInterval = _Gs2352SystemTimeNTPRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 2),
    _Gs2352SystemTimeNTPRequestInterval_Type()
)
gs2352SystemTimeNTPRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPRequestInterval.setStatus("current")


class _Gs2352SystemTimeNTPTriesNumber_Type(Integer32):
    """Custom type gs2352SystemTimeNTPTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_Gs2352SystemTimeNTPTriesNumber_Type.__name__ = "Integer32"
_Gs2352SystemTimeNTPTriesNumber_Object = MibScalar
gs2352SystemTimeNTPTriesNumber = _Gs2352SystemTimeNTPTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 2, 2, 3),
    _Gs2352SystemTimeNTPTriesNumber_Type()
)
gs2352SystemTimeNTPTriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemTimeNTPTriesNumber.setStatus("current")
_Gs2352SystemAccount_ObjectIdentity = ObjectIdentity
gs2352SystemAccount = _Gs2352SystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3)
)
_Gs2352SystemAccountUsers_ObjectIdentity = ObjectIdentity
gs2352SystemAccountUsers = _Gs2352SystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1)
)


class _Gs2352SystemAccountUserCreate_Type(Integer32):
    """Custom type gs2352SystemAccountUserCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352SystemAccountUserCreate_Type.__name__ = "Integer32"
_Gs2352SystemAccountUserCreate_Object = MibScalar
gs2352SystemAccountUserCreate = _Gs2352SystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 1),
    _Gs2352SystemAccountUserCreate_Type()
)
gs2352SystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemAccountUserCreate.setStatus("current")
_Gs2352SystemAccountUsersTable_Object = MibTable
gs2352SystemAccountUsersTable = _Gs2352SystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352SystemAccountUsersTable.setStatus("current")
_Gs2352SystemAccountUsersEntry_Object = MibTableRow
gs2352SystemAccountUsersEntry = _Gs2352SystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2, 1)
)
gs2352SystemAccountUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352UserIndex"),
)
if mibBuilder.loadTexts:
    gs2352SystemAccountUsersEntry.setStatus("current")


class _Gs2352UserIndex_Type(Integer32):
    """Custom type gs2352UserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Gs2352UserIndex_Type.__name__ = "Integer32"
_Gs2352UserIndex_Object = MibTableColumn
gs2352UserIndex = _Gs2352UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2, 1, 1),
    _Gs2352UserIndex_Type()
)
gs2352UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352UserIndex.setStatus("current")


class _Gs2352UserName_Type(DisplayString):
    """Custom type gs2352UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352UserName_Type.__name__ = "DisplayString"
_Gs2352UserName_Object = MibTableColumn
gs2352UserName = _Gs2352UserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2, 1, 2),
    _Gs2352UserName_Type()
)
gs2352UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352UserName.setStatus("current")


class _Gs2352Password_Type(DisplayString):
    """Custom type gs2352Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352Password_Type.__name__ = "DisplayString"
_Gs2352Password_Object = MibTableColumn
gs2352Password = _Gs2352Password_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2, 1, 3),
    _Gs2352Password_Type()
)
gs2352Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Password.setStatus("current")


class _Gs2352UserPrivilegeLevel_Type(Integer32):
    """Custom type gs2352UserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352UserPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352UserPrivilegeLevel_Object = MibTableColumn
gs2352UserPrivilegeLevel = _Gs2352UserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2, 1, 4),
    _Gs2352UserPrivilegeLevel_Type()
)
gs2352UserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352UserPrivilegeLevel.setStatus("current")


class _Gs2352AccountUserRowStatus_Type(Integer32):
    """Custom type gs2352AccountUserRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInservice", 2),
          ("edit", 3),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352AccountUserRowStatus_Type.__name__ = "Integer32"
_Gs2352AccountUserRowStatus_Object = MibTableColumn
gs2352AccountUserRowStatus = _Gs2352AccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 2, 1, 5),
    _Gs2352AccountUserRowStatus_Type()
)
gs2352AccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccountUserRowStatus.setStatus("current")


class _Gs2352SystemAccountUsersSuperUserPassword_Type(OctetString):
    """Custom type gs2352SystemAccountUsersSuperUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2352SystemAccountUsersSuperUserPassword_Type.__name__ = "OctetString"
_Gs2352SystemAccountUsersSuperUserPassword_Object = MibScalar
gs2352SystemAccountUsersSuperUserPassword = _Gs2352SystemAccountUsersSuperUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 1500),
    _Gs2352SystemAccountUsersSuperUserPassword_Type()
)
gs2352SystemAccountUsersSuperUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemAccountUsersSuperUserPassword.setStatus("current")


class _Gs2352SystemAccountEnforcePasswordRules_Type(Integer32):
    """Custom type gs2352SystemAccountEnforcePasswordRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1))
    )


_Gs2352SystemAccountEnforcePasswordRules_Type.__name__ = "Integer32"
_Gs2352SystemAccountEnforcePasswordRules_Object = MibScalar
gs2352SystemAccountEnforcePasswordRules = _Gs2352SystemAccountEnforcePasswordRules_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 1, 1501),
    _Gs2352SystemAccountEnforcePasswordRules_Type()
)
gs2352SystemAccountEnforcePasswordRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemAccountEnforcePasswordRules.setStatus("current")
_Gs2352SystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
gs2352SystemAccountPrivilegeLevel = _Gs2352SystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2)
)


class _Gs2352AccountPrivilegeLevel_Type(Integer32):
    """Custom type gs2352AccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352AccountPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352AccountPrivilegeLevel_Object = MibScalar
gs2352AccountPrivilegeLevel = _Gs2352AccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 1),
    _Gs2352AccountPrivilegeLevel_Type()
)
gs2352AccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccountPrivilegeLevel.setStatus("current")


class _Gs2352AggregationPrivilegeLevel_Type(Integer32):
    """Custom type gs2352AggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352AggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352AggregationPrivilegeLevel_Object = MibScalar
gs2352AggregationPrivilegeLevel = _Gs2352AggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 2),
    _Gs2352AggregationPrivilegeLevel_Type()
)
gs2352AggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AggregationPrivilegeLevel.setStatus("current")


class _Gs2352DiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type gs2352DiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352DiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352DiagnosticsPrivilegeLevel_Object = MibScalar
gs2352DiagnosticsPrivilegeLevel = _Gs2352DiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 3),
    _Gs2352DiagnosticsPrivilegeLevel_Type()
)
gs2352DiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DiagnosticsPrivilegeLevel.setStatus("current")


class _Gs2352EasyportPrivilegeLevel_Type(Integer32):
    """Custom type gs2352EasyportPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352EasyportPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352EasyportPrivilegeLevel_Object = MibScalar
gs2352EasyportPrivilegeLevel = _Gs2352EasyportPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 9),
    _Gs2352EasyportPrivilegeLevel_Type()
)
gs2352EasyportPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352EasyportPrivilegeLevel.setStatus("current")


class _Gs2352GARPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352GARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352GARPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352GARPPrivilegeLevel_Object = MibScalar
gs2352GARPPrivilegeLevel = _Gs2352GARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 10),
    _Gs2352GARPPrivilegeLevel_Type()
)
gs2352GARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPPrivilegeLevel.setStatus("current")


class _Gs2352GVRPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352GVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352GVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352GVRPPrivilegeLevel_Object = MibScalar
gs2352GVRPPrivilegeLevel = _Gs2352GVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 11),
    _Gs2352GVRPPrivilegeLevel_Type()
)
gs2352GVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GVRPPrivilegeLevel.setStatus("current")


class _Gs2352IPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352IPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352IPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352IPPrivilegeLevel_Object = MibScalar
gs2352IPPrivilegeLevel = _Gs2352IPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 12),
    _Gs2352IPPrivilegeLevel_Type()
)
gs2352IPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPPrivilegeLevel.setStatus("current")


class _Gs2352IPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type gs2352IPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352IPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352IPMCSnoopingPrivilegeLevel_Object = MibScalar
gs2352IPMCSnoopingPrivilegeLevel = _Gs2352IPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 13),
    _Gs2352IPMCSnoopingPrivilegeLevel_Type()
)
gs2352IPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPMCSnoopingPrivilegeLevel.setStatus("current")


class _Gs2352LACPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352LACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352LACPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352LACPPrivilegeLevel_Object = MibScalar
gs2352LACPPrivilegeLevel = _Gs2352LACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 14),
    _Gs2352LACPPrivilegeLevel_Type()
)
gs2352LACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LACPPrivilegeLevel.setStatus("current")


class _Gs2352LLDPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352LLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352LLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352LLDPPrivilegeLevel_Object = MibScalar
gs2352LLDPPrivilegeLevel = _Gs2352LLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 15),
    _Gs2352LLDPPrivilegeLevel_Type()
)
gs2352LLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LLDPPrivilegeLevel.setStatus("current")


class _Gs2352LLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type gs2352LLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352LLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352LLDPMEDPrivilegeLevel_Object = MibScalar
gs2352LLDPMEDPrivilegeLevel = _Gs2352LLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 16),
    _Gs2352LLDPMEDPrivilegeLevel_Type()
)
gs2352LLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LLDPMEDPrivilegeLevel.setStatus("current")


class _Gs2352LoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type gs2352LoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352LoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352LoopProtectPrivilegeLevel_Object = MibScalar
gs2352LoopProtectPrivilegeLevel = _Gs2352LoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 17),
    _Gs2352LoopProtectPrivilegeLevel_Type()
)
gs2352LoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectPrivilegeLevel.setStatus("current")


class _Gs2352MACTablePrivilegeLevel_Type(Integer32):
    """Custom type gs2352MACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352MACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352MACTablePrivilegeLevel_Object = MibScalar
gs2352MACTablePrivilegeLevel = _Gs2352MACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 18),
    _Gs2352MACTablePrivilegeLevel_Type()
)
gs2352MACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACTablePrivilegeLevel.setStatus("current")


class _Gs2352MVRPrivilegeLevel_Type(Integer32):
    """Custom type gs2352MVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352MVRPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352MVRPrivilegeLevel_Object = MibScalar
gs2352MVRPrivilegeLevel = _Gs2352MVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 22),
    _Gs2352MVRPrivilegeLevel_Type()
)
gs2352MVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPrivilegeLevel.setStatus("current")


class _Gs2352MaintenancePrivilegeLevel_Type(Integer32):
    """Custom type gs2352MaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352MaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352MaintenancePrivilegeLevel_Object = MibScalar
gs2352MaintenancePrivilegeLevel = _Gs2352MaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 24),
    _Gs2352MaintenancePrivilegeLevel_Type()
)
gs2352MaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MaintenancePrivilegeLevel.setStatus("current")


class _Gs2352MirroringPrivilegeLevel_Type(Integer32):
    """Custom type gs2352MirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352MirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352MirroringPrivilegeLevel_Object = MibScalar
gs2352MirroringPrivilegeLevel = _Gs2352MirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 25),
    _Gs2352MirroringPrivilegeLevel_Type()
)
gs2352MirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MirroringPrivilegeLevel.setStatus("current")


class _Gs2352PortsPrivilegeLevel_Type(Integer32):
    """Custom type gs2352PortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352PortsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352PortsPrivilegeLevel_Object = MibScalar
gs2352PortsPrivilegeLevel = _Gs2352PortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 27),
    _Gs2352PortsPrivilegeLevel_Type()
)
gs2352PortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortsPrivilegeLevel.setStatus("current")


class _Gs2352PrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2352PrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352PrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352PrivateVLANsPrivilegeLevel_Object = MibScalar
gs2352PrivateVLANsPrivilegeLevel = _Gs2352PrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 28),
    _Gs2352PrivateVLANsPrivilegeLevel_Type()
)
gs2352PrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PrivateVLANsPrivilegeLevel.setStatus("current")


class _Gs2352QoSPrivilegeLevel_Type(Integer32):
    """Custom type gs2352QoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352QoSPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352QoSPrivilegeLevel_Object = MibScalar
gs2352QoSPrivilegeLevel = _Gs2352QoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 29),
    _Gs2352QoSPrivilegeLevel_Type()
)
gs2352QoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QoSPrivilegeLevel.setStatus("current")


class _Gs2352SFlowPrivilegeLevel_Type(Integer32):
    """Custom type gs2352SFlowPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SFlowPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SFlowPrivilegeLevel_Object = MibScalar
gs2352SFlowPrivilegeLevel = _Gs2352SFlowPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 30),
    _Gs2352SFlowPrivilegeLevel_Type()
)
gs2352SFlowPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SFlowPrivilegeLevel.setStatus("current")


class _Gs2352SMTPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352SMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SMTPPrivilegeLevel_Object = MibScalar
gs2352SMTPPrivilegeLevel = _Gs2352SMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 31),
    _Gs2352SMTPPrivilegeLevel_Type()
)
gs2352SMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPPrivilegeLevel.setStatus("current")


class _Gs2352SNMPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352SNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SNMPPrivilegeLevel_Object = MibScalar
gs2352SNMPPrivilegeLevel = _Gs2352SNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 32),
    _Gs2352SNMPPrivilegeLevel_Type()
)
gs2352SNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SNMPPrivilegeLevel.setStatus("current")


class _Gs2352SecurityPrivilegeLevel_Type(Integer32):
    """Custom type gs2352SecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SecurityPrivilegeLevel_Object = MibScalar
gs2352SecurityPrivilegeLevel = _Gs2352SecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 33),
    _Gs2352SecurityPrivilegeLevel_Type()
)
gs2352SecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SecurityPrivilegeLevel.setStatus("current")


class _Gs2352SingleIPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352SingleIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SingleIPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SingleIPPrivilegeLevel_Object = MibScalar
gs2352SingleIPPrivilegeLevel = _Gs2352SingleIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 34),
    _Gs2352SingleIPPrivilegeLevel_Type()
)
gs2352SingleIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SingleIPPrivilegeLevel.setStatus("current")


class _Gs2352SpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type gs2352SpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SpanningTreePrivilegeLevel_Object = MibScalar
gs2352SpanningTreePrivilegeLevel = _Gs2352SpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 35),
    _Gs2352SpanningTreePrivilegeLevel_Type()
)
gs2352SpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SpanningTreePrivilegeLevel.setStatus("current")


class _Gs2352SystemPrivilegeLevel_Type(Integer32):
    """Custom type gs2352SystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352SystemPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352SystemPrivilegeLevel_Object = MibScalar
gs2352SystemPrivilegeLevel = _Gs2352SystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 36),
    _Gs2352SystemPrivilegeLevel_Type()
)
gs2352SystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SystemPrivilegeLevel.setStatus("current")


class _Gs2352TrapEventPrivilegeLevel_Type(Integer32):
    """Custom type gs2352TrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352TrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352TrapEventPrivilegeLevel_Object = MibScalar
gs2352TrapEventPrivilegeLevel = _Gs2352TrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 37),
    _Gs2352TrapEventPrivilegeLevel_Type()
)
gs2352TrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventPrivilegeLevel.setStatus("current")


class _Gs2352UPnPPrivilegeLevel_Type(Integer32):
    """Custom type gs2352UPnPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352UPnPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352UPnPPrivilegeLevel_Object = MibScalar
gs2352UPnPPrivilegeLevel = _Gs2352UPnPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 38),
    _Gs2352UPnPPrivilegeLevel_Type()
)
gs2352UPnPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352UPnPPrivilegeLevel.setStatus("current")


class _Gs2352VCLPrivilegeLevel_Type(Integer32):
    """Custom type gs2352VCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352VCLPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352VCLPrivilegeLevel_Object = MibScalar
gs2352VCLPrivilegeLevel = _Gs2352VCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 39),
    _Gs2352VCLPrivilegeLevel_Type()
)
gs2352VCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VCLPrivilegeLevel.setStatus("current")


class _Gs2352VLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2352VLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352VLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352VLANsPrivilegeLevel_Object = MibScalar
gs2352VLANsPrivilegeLevel = _Gs2352VLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 41),
    _Gs2352VLANsPrivilegeLevel_Type()
)
gs2352VLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VLANsPrivilegeLevel.setStatus("current")


class _Gs2352VoiceVLANPrivilegeLevel_Type(Integer32):
    """Custom type gs2352VoiceVLANPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2352VoiceVLANPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2352VoiceVLANPrivilegeLevel_Object = MibScalar
gs2352VoiceVLANPrivilegeLevel = _Gs2352VoiceVLANPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 3, 2, 42),
    _Gs2352VoiceVLANPrivilegeLevel_Type()
)
gs2352VoiceVLANPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANPrivilegeLevel.setStatus("current")
_Gs2352IP_ObjectIdentity = ObjectIdentity
gs2352IP = _Gs2352IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4)
)
_Gs2352IPv4_ObjectIdentity = ObjectIdentity
gs2352IPv4 = _Gs2352IPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1)
)
_Gs2352IPv4Configured_ObjectIdentity = ObjectIdentity
gs2352IPv4Configured = _Gs2352IPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1)
)


class _Gs2352Ipv4DHCPClient_Type(Integer32):
    """Custom type gs2352Ipv4DHCPClient based on Integer32"""
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


_Gs2352Ipv4DHCPClient_Type.__name__ = "Integer32"
_Gs2352Ipv4DHCPClient_Object = MibScalar
gs2352Ipv4DHCPClient = _Gs2352Ipv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 1),
    _Gs2352Ipv4DHCPClient_Type()
)
gs2352Ipv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ipv4DHCPClient.setStatus("current")
_Gs2352IPv4Address_Type = IpAddress
_Gs2352IPv4Address_Object = MibScalar
gs2352IPv4Address = _Gs2352IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 2),
    _Gs2352IPv4Address_Type()
)
gs2352IPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPv4Address.setStatus("current")
_Gs2352IPv4Mask_Type = IpAddress
_Gs2352IPv4Mask_Object = MibScalar
gs2352IPv4Mask = _Gs2352IPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 3),
    _Gs2352IPv4Mask_Type()
)
gs2352IPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPv4Mask.setStatus("current")
_Gs2352IPv4Gateway_Type = IpAddress
_Gs2352IPv4Gateway_Object = MibScalar
gs2352IPv4Gateway = _Gs2352IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 4),
    _Gs2352IPv4Gateway_Type()
)
gs2352IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPv4Gateway.setStatus("current")


class _Gs2352IPv4VLANId_Type(Integer32):
    """Custom type gs2352IPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352IPv4VLANId_Type.__name__ = "Integer32"
_Gs2352IPv4VLANId_Object = MibScalar
gs2352IPv4VLANId = _Gs2352IPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 5),
    _Gs2352IPv4VLANId_Type()
)
gs2352IPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPv4VLANId.setStatus("current")
_Gs2352IPv4DNSServer_Type = IpAddress
_Gs2352IPv4DNSServer_Object = MibScalar
gs2352IPv4DNSServer = _Gs2352IPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 6),
    _Gs2352IPv4DNSServer_Type()
)
gs2352IPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPv4DNSServer.setStatus("current")


class _Gs2352IPv4DNSProxy_Type(Integer32):
    """Custom type gs2352IPv4DNSProxy based on Integer32"""
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


_Gs2352IPv4DNSProxy_Type.__name__ = "Integer32"
_Gs2352IPv4DNSProxy_Object = MibScalar
gs2352IPv4DNSProxy = _Gs2352IPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 1, 7),
    _Gs2352IPv4DNSProxy_Type()
)
gs2352IPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPv4DNSProxy.setStatus("current")
_Gs2352IPv4Current_ObjectIdentity = ObjectIdentity
gs2352IPv4Current = _Gs2352IPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2)
)


class _Gs2352Ipv4CurrentDHCPClient_Type(Integer32):
    """Custom type gs2352Ipv4CurrentDHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renew", 1))
    )


_Gs2352Ipv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Gs2352Ipv4CurrentDHCPClient_Object = MibScalar
gs2352Ipv4CurrentDHCPClient = _Gs2352Ipv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2, 1),
    _Gs2352Ipv4CurrentDHCPClient_Type()
)
gs2352Ipv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ipv4CurrentDHCPClient.setStatus("current")
_Gs2352IPv4CurrentAddress_Type = IpAddress
_Gs2352IPv4CurrentAddress_Object = MibScalar
gs2352IPv4CurrentAddress = _Gs2352IPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2, 2),
    _Gs2352IPv4CurrentAddress_Type()
)
gs2352IPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv4CurrentAddress.setStatus("current")
_Gs2352IPv4CurrentMask_Type = IpAddress
_Gs2352IPv4CurrentMask_Object = MibScalar
gs2352IPv4CurrentMask = _Gs2352IPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2, 3),
    _Gs2352IPv4CurrentMask_Type()
)
gs2352IPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv4CurrentMask.setStatus("current")
_Gs2352IPv4CurrentGateway_Type = IpAddress
_Gs2352IPv4CurrentGateway_Object = MibScalar
gs2352IPv4CurrentGateway = _Gs2352IPv4CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2, 4),
    _Gs2352IPv4CurrentGateway_Type()
)
gs2352IPv4CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv4CurrentGateway.setStatus("current")


class _Gs2352IPv4CurrentVLANId_Type(Integer32):
    """Custom type gs2352IPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352IPv4CurrentVLANId_Type.__name__ = "Integer32"
_Gs2352IPv4CurrentVLANId_Object = MibScalar
gs2352IPv4CurrentVLANId = _Gs2352IPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2, 5),
    _Gs2352IPv4CurrentVLANId_Type()
)
gs2352IPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv4CurrentVLANId.setStatus("current")
_Gs2352IPv4CurrentDNSServer_Type = IpAddress
_Gs2352IPv4CurrentDNSServer_Object = MibScalar
gs2352IPv4CurrentDNSServer = _Gs2352IPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 1, 2, 6),
    _Gs2352IPv4CurrentDNSServer_Type()
)
gs2352IPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPv4CurrentDNSServer.setStatus("current")
_Gs2352IPv6_ObjectIdentity = ObjectIdentity
gs2352IPv6 = _Gs2352IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2)
)
_Gs2352IPv6Configured_ObjectIdentity = ObjectIdentity
gs2352IPv6Configured = _Gs2352IPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 1)
)


class _Gs2352Ipv6AutoConfiguration_Type(Integer32):
    """Custom type gs2352Ipv6AutoConfiguration based on Integer32"""
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


_Gs2352Ipv6AutoConfiguration_Type.__name__ = "Integer32"
_Gs2352Ipv6AutoConfiguration_Object = MibScalar
gs2352Ipv6AutoConfiguration = _Gs2352Ipv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 1, 1),
    _Gs2352Ipv6AutoConfiguration_Type()
)
gs2352Ipv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ipv6AutoConfiguration.setStatus("current")


class _Gs2352Ipv6Address_Type(DisplayString):
    """Custom type gs2352Ipv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2352Ipv6Address_Type.__name__ = "DisplayString"
_Gs2352Ipv6Address_Object = MibScalar
gs2352Ipv6Address = _Gs2352Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 1, 2),
    _Gs2352Ipv6Address_Type()
)
gs2352Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ipv6Address.setStatus("current")


class _Gs2352Ipv6Prefix_Type(Integer32):
    """Custom type gs2352Ipv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2352Ipv6Prefix_Type.__name__ = "Integer32"
_Gs2352Ipv6Prefix_Object = MibScalar
gs2352Ipv6Prefix = _Gs2352Ipv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 1, 3),
    _Gs2352Ipv6Prefix_Type()
)
gs2352Ipv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ipv6Prefix.setStatus("current")


class _Gs2352Ipv6Gateway_Type(DisplayString):
    """Custom type gs2352Ipv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2352Ipv6Gateway_Type.__name__ = "DisplayString"
_Gs2352Ipv6Gateway_Object = MibScalar
gs2352Ipv6Gateway = _Gs2352Ipv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 1, 4),
    _Gs2352Ipv6Gateway_Type()
)
gs2352Ipv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ipv6Gateway.setStatus("current")
_Gs2352IPv6Current_ObjectIdentity = ObjectIdentity
gs2352IPv6Current = _Gs2352IPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 2)
)


class _Gs2352Ipv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type gs2352Ipv6CurrentAutoConfiguration based on Integer32"""
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


_Gs2352Ipv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Gs2352Ipv6CurrentAutoConfiguration_Object = MibScalar
gs2352Ipv6CurrentAutoConfiguration = _Gs2352Ipv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 2, 1),
    _Gs2352Ipv6CurrentAutoConfiguration_Type()
)
gs2352Ipv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Ipv6CurrentAutoConfiguration.setStatus("current")


class _Gs2352Ipv6CurrentAddress_Type(DisplayString):
    """Custom type gs2352Ipv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2352Ipv6CurrentAddress_Type.__name__ = "DisplayString"
_Gs2352Ipv6CurrentAddress_Object = MibScalar
gs2352Ipv6CurrentAddress = _Gs2352Ipv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 2, 2),
    _Gs2352Ipv6CurrentAddress_Type()
)
gs2352Ipv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Ipv6CurrentAddress.setStatus("current")


class _Gs2352Ipv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type gs2352Ipv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2352Ipv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Gs2352Ipv6CurrentLinkLocalAddress_Object = MibScalar
gs2352Ipv6CurrentLinkLocalAddress = _Gs2352Ipv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 2, 3),
    _Gs2352Ipv6CurrentLinkLocalAddress_Type()
)
gs2352Ipv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Ipv6CurrentLinkLocalAddress.setStatus("current")


class _Gs2352Ipv6CurrentPrefix_Type(DisplayString):
    """Custom type gs2352Ipv6CurrentPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Gs2352Ipv6CurrentPrefix_Type.__name__ = "DisplayString"
_Gs2352Ipv6CurrentPrefix_Object = MibScalar
gs2352Ipv6CurrentPrefix = _Gs2352Ipv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 2, 4),
    _Gs2352Ipv6CurrentPrefix_Type()
)
gs2352Ipv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Ipv6CurrentPrefix.setStatus("current")


class _Gs2352Ipv6CurrentGateway_Type(DisplayString):
    """Custom type gs2352Ipv6CurrentGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2352Ipv6CurrentGateway_Type.__name__ = "DisplayString"
_Gs2352Ipv6CurrentGateway_Object = MibScalar
gs2352Ipv6CurrentGateway = _Gs2352Ipv6CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 4, 2, 2, 5),
    _Gs2352Ipv6CurrentGateway_Type()
)
gs2352Ipv6CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Ipv6CurrentGateway.setStatus("current")
_Gs2352Syslog_ObjectIdentity = ObjectIdentity
gs2352Syslog = _Gs2352Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5)
)
_Gs2352SyslogConf_ObjectIdentity = ObjectIdentity
gs2352SyslogConf = _Gs2352SyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 1)
)


class _Gs2352ServerMode_Type(Integer32):
    """Custom type gs2352ServerMode based on Integer32"""
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


_Gs2352ServerMode_Type.__name__ = "Integer32"
_Gs2352ServerMode_Object = MibScalar
gs2352ServerMode = _Gs2352ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 1, 1),
    _Gs2352ServerMode_Type()
)
gs2352ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ServerMode.setStatus("current")
_Gs2352ServerAddress1_Type = IpAddress
_Gs2352ServerAddress1_Object = MibScalar
gs2352ServerAddress1 = _Gs2352ServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 1, 2),
    _Gs2352ServerAddress1_Type()
)
gs2352ServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ServerAddress1.setStatus("current")
_Gs2352ServerAddress2_Type = IpAddress
_Gs2352ServerAddress2_Object = MibScalar
gs2352ServerAddress2 = _Gs2352ServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 1, 3),
    _Gs2352ServerAddress2_Type()
)
gs2352ServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ServerAddress2.setStatus("current")


class _Gs2352SyslogLevel_Type(Integer32):
    """Custom type gs2352SyslogLevel based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352SyslogLevel_Type.__name__ = "Integer32"
_Gs2352SyslogLevel_Object = MibScalar
gs2352SyslogLevel = _Gs2352SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 1, 4),
    _Gs2352SyslogLevel_Type()
)
gs2352SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SyslogLevel.setStatus("current")
_Gs2352SyslogDetailedInfo_ObjectIdentity = ObjectIdentity
gs2352SyslogDetailedInfo = _Gs2352SyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2)
)


class _Gs2352SyslogDetailedInfoClear_Type(Integer32):
    """Custom type gs2352SyslogDetailedInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352SyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Gs2352SyslogDetailedInfoClear_Object = MibScalar
gs2352SyslogDetailedInfoClear = _Gs2352SyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 1),
    _Gs2352SyslogDetailedInfoClear_Type()
)
gs2352SyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoClear.setStatus("current")
_Gs2352SyslogDetailedInfoTable_Object = MibTable
gs2352SyslogDetailedInfoTable = _Gs2352SyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoTable.setStatus("current")
_Gs2352SyslogDetailedInfoEntry_Object = MibTableRow
gs2352SyslogDetailedInfoEntry = _Gs2352SyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 2, 1)
)
gs2352SyslogDetailedInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoEntry.setStatus("current")


class _Gs2352SyslogDetailedInfoIndex_Type(Integer32):
    """Custom type gs2352SyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2352SyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Gs2352SyslogDetailedInfoIndex_Object = MibTableColumn
gs2352SyslogDetailedInfoIndex = _Gs2352SyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 2, 1, 1),
    _Gs2352SyslogDetailedInfoIndex_Type()
)
gs2352SyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoIndex.setStatus("current")
_Gs2352SyslogDetailedInfoLevel_Type = DisplayString
_Gs2352SyslogDetailedInfoLevel_Object = MibTableColumn
gs2352SyslogDetailedInfoLevel = _Gs2352SyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 2, 1, 2),
    _Gs2352SyslogDetailedInfoLevel_Type()
)
gs2352SyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoLevel.setStatus("current")


class _Gs2352SyslogDetailedInfoTime_Type(DisplayString):
    """Custom type gs2352SyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gs2352SyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Gs2352SyslogDetailedInfoTime_Object = MibTableColumn
gs2352SyslogDetailedInfoTime = _Gs2352SyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 2, 1, 3),
    _Gs2352SyslogDetailedInfoTime_Type()
)
gs2352SyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoTime.setStatus("current")
_Gs2352SyslogDetailedInfoMessage_Type = DisplayString
_Gs2352SyslogDetailedInfoMessage_Object = MibTableColumn
gs2352SyslogDetailedInfoMessage = _Gs2352SyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 5, 2, 2, 1, 4),
    _Gs2352SyslogDetailedInfoMessage_Type()
)
gs2352SyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SyslogDetailedInfoMessage.setStatus("current")
_Gs2352Snmp_ObjectIdentity = ObjectIdentity
gs2352Snmp = _Gs2352Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6)
)
_Gs2352SnmpConf_ObjectIdentity = ObjectIdentity
gs2352SnmpConf = _Gs2352SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1)
)


class _Gs2352GetCommunityMode_Type(Integer32):
    """Custom type gs2352GetCommunityMode based on Integer32"""
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


_Gs2352GetCommunityMode_Type.__name__ = "Integer32"
_Gs2352GetCommunityMode_Object = MibScalar
gs2352GetCommunityMode = _Gs2352GetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 1),
    _Gs2352GetCommunityMode_Type()
)
gs2352GetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GetCommunityMode.setStatus("current")
_Gs2352GetCommunity_Type = DisplayString
_Gs2352GetCommunity_Object = MibScalar
gs2352GetCommunity = _Gs2352GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 2),
    _Gs2352GetCommunity_Type()
)
gs2352GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GetCommunity.setStatus("current")


class _Gs2352SetCommunityMode_Type(Integer32):
    """Custom type gs2352SetCommunityMode based on Integer32"""
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


_Gs2352SetCommunityMode_Type.__name__ = "Integer32"
_Gs2352SetCommunityMode_Object = MibScalar
gs2352SetCommunityMode = _Gs2352SetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 3),
    _Gs2352SetCommunityMode_Type()
)
gs2352SetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SetCommunityMode.setStatus("current")
_Gs2352SetCommunity_Type = DisplayString
_Gs2352SetCommunity_Object = MibScalar
gs2352SetCommunity = _Gs2352SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 4),
    _Gs2352SetCommunity_Type()
)
gs2352SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SetCommunity.setStatus("current")
_Gs2352GetCommunityConfTable_Object = MibTable
gs2352GetCommunityConfTable = _Gs2352GetCommunityConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    gs2352GetCommunityConfTable.setStatus("current")
_Gs2352GetCommunityConfEntry_Object = MibTableRow
gs2352GetCommunityConfEntry = _Gs2352GetCommunityConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 5, 1)
)
gs2352GetCommunityConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352CommunityConfIndex"),
)
if mibBuilder.loadTexts:
    gs2352GetCommunityConfEntry.setStatus("current")


class _Gs2352CommunityConfIndex_Type(Integer32):
    """Custom type gs2352CommunityConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352CommunityConfIndex_Type.__name__ = "Integer32"
_Gs2352CommunityConfIndex_Object = MibTableColumn
gs2352CommunityConfIndex = _Gs2352CommunityConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 5, 1, 1),
    _Gs2352CommunityConfIndex_Type()
)
gs2352CommunityConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352CommunityConfIndex.setStatus("current")
_Gs2352CommunityConfGetCommunity_Type = DisplayString
_Gs2352CommunityConfGetCommunity_Object = MibTableColumn
gs2352CommunityConfGetCommunity = _Gs2352CommunityConfGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 5, 1, 2),
    _Gs2352CommunityConfGetCommunity_Type()
)
gs2352CommunityConfGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352CommunityConfGetCommunity.setStatus("current")
_Gs2352TrapHostConfTable_Object = MibTable
gs2352TrapHostConfTable = _Gs2352TrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    gs2352TrapHostConfTable.setStatus("current")
_Gs2352TrapHostConfEntry_Object = MibTableRow
gs2352TrapHostConfEntry = _Gs2352TrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1)
)
gs2352TrapHostConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352TrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    gs2352TrapHostConfEntry.setStatus("current")


class _Gs2352TrapHostConfIndex_Type(Integer32):
    """Custom type gs2352TrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2352TrapHostConfIndex_Type.__name__ = "Integer32"
_Gs2352TrapHostConfIndex_Object = MibTableColumn
gs2352TrapHostConfIndex = _Gs2352TrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 1),
    _Gs2352TrapHostConfIndex_Type()
)
gs2352TrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352TrapHostConfIndex.setStatus("current")


class _Gs2352TrapHostConfVersion_Type(Integer32):
    """Custom type gs2352TrapHostConfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv2c", 2),
          ("snmpv3", 3))
    )


_Gs2352TrapHostConfVersion_Type.__name__ = "Integer32"
_Gs2352TrapHostConfVersion_Object = MibTableColumn
gs2352TrapHostConfVersion = _Gs2352TrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 2),
    _Gs2352TrapHostConfVersion_Type()
)
gs2352TrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfVersion.setStatus("current")


class _Gs2352TrapHostConfIPType_Type(Integer32):
    """Custom type gs2352TrapHostConfIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 4),
          ("ipv6", 6))
    )


_Gs2352TrapHostConfIPType_Type.__name__ = "Integer32"
_Gs2352TrapHostConfIPType_Object = MibTableColumn
gs2352TrapHostConfIPType = _Gs2352TrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 3),
    _Gs2352TrapHostConfIPType_Type()
)
gs2352TrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfIPType.setStatus("current")
_Gs2352TrapHostConfIP_Type = DisplayString
_Gs2352TrapHostConfIP_Object = MibTableColumn
gs2352TrapHostConfIP = _Gs2352TrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 4),
    _Gs2352TrapHostConfIP_Type()
)
gs2352TrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfIP.setStatus("current")


class _Gs2352TrapHostConfPort_Type(Integer32):
    """Custom type gs2352TrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352TrapHostConfPort_Type.__name__ = "Integer32"
_Gs2352TrapHostConfPort_Object = MibTableColumn
gs2352TrapHostConfPort = _Gs2352TrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 5),
    _Gs2352TrapHostConfPort_Type()
)
gs2352TrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfPort.setStatus("current")


class _Gs2352TrapHostConfCommunity_Type(DisplayString):
    """Custom type gs2352TrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352TrapHostConfCommunity_Type.__name__ = "DisplayString"
_Gs2352TrapHostConfCommunity_Object = MibTableColumn
gs2352TrapHostConfCommunity = _Gs2352TrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 6),
    _Gs2352TrapHostConfCommunity_Type()
)
gs2352TrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfCommunity.setStatus("current")


class _Gs2352TrapHostConfSeverityLevel_Type(Integer32):
    """Custom type gs2352TrapHostConfSeverityLevel based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Gs2352TrapHostConfSeverityLevel_Object = MibTableColumn
gs2352TrapHostConfSeverityLevel = _Gs2352TrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 7),
    _Gs2352TrapHostConfSeverityLevel_Type()
)
gs2352TrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfSeverityLevel.setStatus("current")


class _Gs2352TrapHostConfSecurityLevel_Type(Integer32):
    """Custom type gs2352TrapHostConfSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_Gs2352TrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Gs2352TrapHostConfSecurityLevel_Object = MibTableColumn
gs2352TrapHostConfSecurityLevel = _Gs2352TrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 8),
    _Gs2352TrapHostConfSecurityLevel_Type()
)
gs2352TrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfSecurityLevel.setStatus("current")


class _Gs2352TrapHostConfAuthPtc_Type(Integer32):
    """Custom type gs2352TrapHostConfAuthPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_Gs2352TrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Gs2352TrapHostConfAuthPtc_Object = MibTableColumn
gs2352TrapHostConfAuthPtc = _Gs2352TrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 9),
    _Gs2352TrapHostConfAuthPtc_Type()
)
gs2352TrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfAuthPtc.setStatus("current")
_Gs2352TrapHostConfAuthPassword_Type = DisplayString
_Gs2352TrapHostConfAuthPassword_Object = MibTableColumn
gs2352TrapHostConfAuthPassword = _Gs2352TrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 10),
    _Gs2352TrapHostConfAuthPassword_Type()
)
gs2352TrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfAuthPassword.setStatus("current")


class _Gs2352TrapHostConfPrivPtc_Type(Integer32):
    """Custom type gs2352TrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("des", 1)
    )


_Gs2352TrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Gs2352TrapHostConfPrivPtc_Object = MibTableColumn
gs2352TrapHostConfPrivPtc = _Gs2352TrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 11),
    _Gs2352TrapHostConfPrivPtc_Type()
)
gs2352TrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfPrivPtc.setStatus("current")
_Gs2352TrapHostConfPrivPassword_Type = DisplayString
_Gs2352TrapHostConfPrivPassword_Object = MibTableColumn
gs2352TrapHostConfPrivPassword = _Gs2352TrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 12),
    _Gs2352TrapHostConfPrivPassword_Type()
)
gs2352TrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfPrivPassword.setStatus("current")


class _Gs2352TrapHostConfCurrentMode_Type(Integer32):
    """Custom type gs2352TrapHostConfCurrentMode based on Integer32"""
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
        *(("empty", 0),
          ("active", 1),
          ("edit", 2),
          ("delete", 3))
    )


_Gs2352TrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Gs2352TrapHostConfCurrentMode_Object = MibTableColumn
gs2352TrapHostConfCurrentMode = _Gs2352TrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 1, 6, 1, 13),
    _Gs2352TrapHostConfCurrentMode_Type()
)
gs2352TrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapHostConfCurrentMode.setStatus("current")
_Gs2352SnmpSystem_ObjectIdentity = ObjectIdentity
gs2352SnmpSystem = _Gs2352SnmpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 2)
)


class _Gs2352SnmpState_Type(Integer32):
    """Custom type gs2352SnmpState based on Integer32"""
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


_Gs2352SnmpState_Type.__name__ = "Integer32"
_Gs2352SnmpState_Object = MibScalar
gs2352SnmpState = _Gs2352SnmpState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 2, 1),
    _Gs2352SnmpState_Type()
)
gs2352SnmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpState.setStatus("current")


class _Gs2352SnmpEngineID_Type(OctetString):
    """Custom type gs2352SnmpEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Gs2352SnmpEngineID_Type.__name__ = "OctetString"
_Gs2352SnmpEngineID_Object = MibScalar
gs2352SnmpEngineID = _Gs2352SnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 2, 2),
    _Gs2352SnmpEngineID_Type()
)
gs2352SnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpEngineID.setStatus("current")
_Gs2352SnmpCommunities_ObjectIdentity = ObjectIdentity
gs2352SnmpCommunities = _Gs2352SnmpCommunities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3)
)


class _Gs2352SnmpCommunitiesCreate_Type(Integer32):
    """Custom type gs2352SnmpCommunitiesCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352SnmpCommunitiesCreate_Type.__name__ = "Integer32"
_Gs2352SnmpCommunitiesCreate_Object = MibScalar
gs2352SnmpCommunitiesCreate = _Gs2352SnmpCommunitiesCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 1),
    _Gs2352SnmpCommunitiesCreate_Type()
)
gs2352SnmpCommunitiesCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesCreate.setStatus("current")
_Gs2352SnmpCommunitiesTable_Object = MibTable
gs2352SnmpCommunitiesTable = _Gs2352SnmpCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesTable.setStatus("current")
_Gs2352SnmpCommunitiesEntry_Object = MibTableRow
gs2352SnmpCommunitiesEntry = _Gs2352SnmpCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1)
)
gs2352SnmpCommunitiesEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SnmpCommunitiesIndex"),
)
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesEntry.setStatus("current")


class _Gs2352SnmpCommunitiesIndex_Type(Integer32):
    """Custom type gs2352SnmpCommunitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2352SnmpCommunitiesIndex_Type.__name__ = "Integer32"
_Gs2352SnmpCommunitiesIndex_Object = MibTableColumn
gs2352SnmpCommunitiesIndex = _Gs2352SnmpCommunitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1, 1),
    _Gs2352SnmpCommunitiesIndex_Type()
)
gs2352SnmpCommunitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesIndex.setStatus("current")


class _Gs2352SnmpCommunitiesCommunity_Type(DisplayString):
    """Custom type gs2352SnmpCommunitiesCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpCommunitiesCommunity_Type.__name__ = "DisplayString"
_Gs2352SnmpCommunitiesCommunity_Object = MibTableColumn
gs2352SnmpCommunitiesCommunity = _Gs2352SnmpCommunitiesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1, 2),
    _Gs2352SnmpCommunitiesCommunity_Type()
)
gs2352SnmpCommunitiesCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesCommunity.setStatus("current")


class _Gs2352SnmpCommunitiesUserName_Type(DisplayString):
    """Custom type gs2352SnmpCommunitiesUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpCommunitiesUserName_Type.__name__ = "DisplayString"
_Gs2352SnmpCommunitiesUserName_Object = MibTableColumn
gs2352SnmpCommunitiesUserName = _Gs2352SnmpCommunitiesUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1, 3),
    _Gs2352SnmpCommunitiesUserName_Type()
)
gs2352SnmpCommunitiesUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesUserName.setStatus("current")
_Gs2352SnmpCommunitiesSourceIP_Type = IpAddress
_Gs2352SnmpCommunitiesSourceIP_Object = MibTableColumn
gs2352SnmpCommunitiesSourceIP = _Gs2352SnmpCommunitiesSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1, 4),
    _Gs2352SnmpCommunitiesSourceIP_Type()
)
gs2352SnmpCommunitiesSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesSourceIP.setStatus("current")
_Gs2352SnmpCommunitiesSourceMask_Type = IpAddress
_Gs2352SnmpCommunitiesSourceMask_Object = MibTableColumn
gs2352SnmpCommunitiesSourceMask = _Gs2352SnmpCommunitiesSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1, 5),
    _Gs2352SnmpCommunitiesSourceMask_Type()
)
gs2352SnmpCommunitiesSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesSourceMask.setStatus("current")


class _Gs2352SnmpCommunitiesRowStatus_Type(Integer32):
    """Custom type gs2352SnmpCommunitiesRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352SnmpCommunitiesRowStatus_Type.__name__ = "Integer32"
_Gs2352SnmpCommunitiesRowStatus_Object = MibTableColumn
gs2352SnmpCommunitiesRowStatus = _Gs2352SnmpCommunitiesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 3, 2, 1, 6),
    _Gs2352SnmpCommunitiesRowStatus_Type()
)
gs2352SnmpCommunitiesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpCommunitiesRowStatus.setStatus("current")
_Gs2352SnmpUsers_ObjectIdentity = ObjectIdentity
gs2352SnmpUsers = _Gs2352SnmpUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4)
)


class _Gs2352SnmpUsersCreate_Type(Integer32):
    """Custom type gs2352SnmpUsersCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352SnmpUsersCreate_Type.__name__ = "Integer32"
_Gs2352SnmpUsersCreate_Object = MibScalar
gs2352SnmpUsersCreate = _Gs2352SnmpUsersCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 1),
    _Gs2352SnmpUsersCreate_Type()
)
gs2352SnmpUsersCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersCreate.setStatus("current")
_Gs2352SnmpUsersTable_Object = MibTable
gs2352SnmpUsersTable = _Gs2352SnmpUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352SnmpUsersTable.setStatus("current")
_Gs2352SnmpUsersEntry_Object = MibTableRow
gs2352SnmpUsersEntry = _Gs2352SnmpUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1)
)
gs2352SnmpUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SnmpUsersIndex"),
)
if mibBuilder.loadTexts:
    gs2352SnmpUsersEntry.setStatus("current")


class _Gs2352SnmpUsersIndex_Type(Integer32):
    """Custom type gs2352SnmpUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2352SnmpUsersIndex_Type.__name__ = "Integer32"
_Gs2352SnmpUsersIndex_Object = MibTableColumn
gs2352SnmpUsersIndex = _Gs2352SnmpUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 1),
    _Gs2352SnmpUsersIndex_Type()
)
gs2352SnmpUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SnmpUsersIndex.setStatus("current")


class _Gs2352SnmpUsersUserName_Type(DisplayString):
    """Custom type gs2352SnmpUsersUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpUsersUserName_Type.__name__ = "DisplayString"
_Gs2352SnmpUsersUserName_Object = MibTableColumn
gs2352SnmpUsersUserName = _Gs2352SnmpUsersUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 2),
    _Gs2352SnmpUsersUserName_Type()
)
gs2352SnmpUsersUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersUserName.setStatus("current")


class _Gs2352SnmpUsersSecurityLevel_Type(Integer32):
    """Custom type gs2352SnmpUsersSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauthnopriv", 1),
          ("authnopriv", 2),
          ("authpriv", 3))
    )


_Gs2352SnmpUsersSecurityLevel_Type.__name__ = "Integer32"
_Gs2352SnmpUsersSecurityLevel_Object = MibTableColumn
gs2352SnmpUsersSecurityLevel = _Gs2352SnmpUsersSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 3),
    _Gs2352SnmpUsersSecurityLevel_Type()
)
gs2352SnmpUsersSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersSecurityLevel.setStatus("current")


class _Gs2352SnmpUsersAuthenticationProtocol_Type(Integer32):
    """Custom type gs2352SnmpUsersAuthenticationProtocol based on Integer32"""
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
          ("md5", 1),
          ("sha", 2))
    )


_Gs2352SnmpUsersAuthenticationProtocol_Type.__name__ = "Integer32"
_Gs2352SnmpUsersAuthenticationProtocol_Object = MibTableColumn
gs2352SnmpUsersAuthenticationProtocol = _Gs2352SnmpUsersAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 4),
    _Gs2352SnmpUsersAuthenticationProtocol_Type()
)
gs2352SnmpUsersAuthenticationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersAuthenticationProtocol.setStatus("current")
_Gs2352SnmpUsersAuthenticationPassword_Type = DisplayString
_Gs2352SnmpUsersAuthenticationPassword_Object = MibTableColumn
gs2352SnmpUsersAuthenticationPassword = _Gs2352SnmpUsersAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 5),
    _Gs2352SnmpUsersAuthenticationPassword_Type()
)
gs2352SnmpUsersAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersAuthenticationPassword.setStatus("current")


class _Gs2352SnmpUsersPrivacyProtocol_Type(Integer32):
    """Custom type gs2352SnmpUsersPrivacyProtocol based on Integer32"""
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
          ("des", 1),
          ("aes", 2))
    )


_Gs2352SnmpUsersPrivacyProtocol_Type.__name__ = "Integer32"
_Gs2352SnmpUsersPrivacyProtocol_Object = MibTableColumn
gs2352SnmpUsersPrivacyProtocol = _Gs2352SnmpUsersPrivacyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 6),
    _Gs2352SnmpUsersPrivacyProtocol_Type()
)
gs2352SnmpUsersPrivacyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersPrivacyProtocol.setStatus("current")
_Gs2352SnmpUsersPrivacyPassword_Type = DisplayString
_Gs2352SnmpUsersPrivacyPassword_Object = MibTableColumn
gs2352SnmpUsersPrivacyPassword = _Gs2352SnmpUsersPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 7),
    _Gs2352SnmpUsersPrivacyPassword_Type()
)
gs2352SnmpUsersPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersPrivacyPassword.setStatus("current")


class _Gs2352SnmpUsersRowStatus_Type(Integer32):
    """Custom type gs2352SnmpUsersRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352SnmpUsersRowStatus_Type.__name__ = "Integer32"
_Gs2352SnmpUsersRowStatus_Object = MibTableColumn
gs2352SnmpUsersRowStatus = _Gs2352SnmpUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 4, 2, 1, 8),
    _Gs2352SnmpUsersRowStatus_Type()
)
gs2352SnmpUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpUsersRowStatus.setStatus("current")
_Gs2352SnmpGroups_ObjectIdentity = ObjectIdentity
gs2352SnmpGroups = _Gs2352SnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5)
)


class _Gs2352SnmpGroupsCreate_Type(Integer32):
    """Custom type gs2352SnmpGroupsCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352SnmpGroupsCreate_Type.__name__ = "Integer32"
_Gs2352SnmpGroupsCreate_Object = MibScalar
gs2352SnmpGroupsCreate = _Gs2352SnmpGroupsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 1),
    _Gs2352SnmpGroupsCreate_Type()
)
gs2352SnmpGroupsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpGroupsCreate.setStatus("current")
_Gs2352SnmpGroupsTable_Object = MibTable
gs2352SnmpGroupsTable = _Gs2352SnmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gs2352SnmpGroupsTable.setStatus("current")
_Gs2352SnmpGroupsEntry_Object = MibTableRow
gs2352SnmpGroupsEntry = _Gs2352SnmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2, 1)
)
gs2352SnmpGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SnmpGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2352SnmpGroupsEntry.setStatus("current")


class _Gs2352SnmpGroupsIndex_Type(Integer32):
    """Custom type gs2352SnmpGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2352SnmpGroupsIndex_Type.__name__ = "Integer32"
_Gs2352SnmpGroupsIndex_Object = MibTableColumn
gs2352SnmpGroupsIndex = _Gs2352SnmpGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2, 1, 1),
    _Gs2352SnmpGroupsIndex_Type()
)
gs2352SnmpGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SnmpGroupsIndex.setStatus("current")


class _Gs2352SnmpGroupsSecurityModel_Type(Integer32):
    """Custom type gs2352SnmpGroupsSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("usm", 3))
    )


_Gs2352SnmpGroupsSecurityModel_Type.__name__ = "Integer32"
_Gs2352SnmpGroupsSecurityModel_Object = MibTableColumn
gs2352SnmpGroupsSecurityModel = _Gs2352SnmpGroupsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2, 1, 2),
    _Gs2352SnmpGroupsSecurityModel_Type()
)
gs2352SnmpGroupsSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpGroupsSecurityModel.setStatus("current")


class _Gs2352SnmpGroupsSecurityName_Type(DisplayString):
    """Custom type gs2352SnmpGroupsSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpGroupsSecurityName_Type.__name__ = "DisplayString"
_Gs2352SnmpGroupsSecurityName_Object = MibTableColumn
gs2352SnmpGroupsSecurityName = _Gs2352SnmpGroupsSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2, 1, 3),
    _Gs2352SnmpGroupsSecurityName_Type()
)
gs2352SnmpGroupsSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpGroupsSecurityName.setStatus("current")


class _Gs2352SnmpGroupsGroupName_Type(DisplayString):
    """Custom type gs2352SnmpGroupsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpGroupsGroupName_Type.__name__ = "DisplayString"
_Gs2352SnmpGroupsGroupName_Object = MibTableColumn
gs2352SnmpGroupsGroupName = _Gs2352SnmpGroupsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2, 1, 4),
    _Gs2352SnmpGroupsGroupName_Type()
)
gs2352SnmpGroupsGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpGroupsGroupName.setStatus("current")


class _Gs2352SnmpGroupsRowStatus_Type(Integer32):
    """Custom type gs2352SnmpGroupsRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352SnmpGroupsRowStatus_Type.__name__ = "Integer32"
_Gs2352SnmpGroupsRowStatus_Object = MibTableColumn
gs2352SnmpGroupsRowStatus = _Gs2352SnmpGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 5, 2, 1, 5),
    _Gs2352SnmpGroupsRowStatus_Type()
)
gs2352SnmpGroupsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpGroupsRowStatus.setStatus("current")
_Gs2352SnmpViews_ObjectIdentity = ObjectIdentity
gs2352SnmpViews = _Gs2352SnmpViews_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6)
)


class _Gs2352SnmpViewsCreate_Type(Integer32):
    """Custom type gs2352SnmpViewsCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352SnmpViewsCreate_Type.__name__ = "Integer32"
_Gs2352SnmpViewsCreate_Object = MibScalar
gs2352SnmpViewsCreate = _Gs2352SnmpViewsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 1),
    _Gs2352SnmpViewsCreate_Type()
)
gs2352SnmpViewsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpViewsCreate.setStatus("current")
_Gs2352SnmpViewsTable_Object = MibTable
gs2352SnmpViewsTable = _Gs2352SnmpViewsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    gs2352SnmpViewsTable.setStatus("current")
_Gs2352SnmpViewsEntry_Object = MibTableRow
gs2352SnmpViewsEntry = _Gs2352SnmpViewsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2, 1)
)
gs2352SnmpViewsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SnmpViewsIndex"),
)
if mibBuilder.loadTexts:
    gs2352SnmpViewsEntry.setStatus("current")


class _Gs2352SnmpViewsIndex_Type(Integer32):
    """Custom type gs2352SnmpViewsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2352SnmpViewsIndex_Type.__name__ = "Integer32"
_Gs2352SnmpViewsIndex_Object = MibTableColumn
gs2352SnmpViewsIndex = _Gs2352SnmpViewsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2, 1, 1),
    _Gs2352SnmpViewsIndex_Type()
)
gs2352SnmpViewsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SnmpViewsIndex.setStatus("current")


class _Gs2352SnmpViewsName_Type(DisplayString):
    """Custom type gs2352SnmpViewsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpViewsName_Type.__name__ = "DisplayString"
_Gs2352SnmpViewsName_Object = MibTableColumn
gs2352SnmpViewsName = _Gs2352SnmpViewsName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2, 1, 2),
    _Gs2352SnmpViewsName_Type()
)
gs2352SnmpViewsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpViewsName.setStatus("current")


class _Gs2352SnmpViewsType_Type(Integer32):
    """Custom type gs2352SnmpViewsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_Gs2352SnmpViewsType_Type.__name__ = "Integer32"
_Gs2352SnmpViewsType_Object = MibTableColumn
gs2352SnmpViewsType = _Gs2352SnmpViewsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2, 1, 3),
    _Gs2352SnmpViewsType_Type()
)
gs2352SnmpViewsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpViewsType.setStatus("current")


class _Gs2352SnmpViewsOIDSubtree_Type(DisplayString):
    """Custom type gs2352SnmpViewsOIDSubtree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Gs2352SnmpViewsOIDSubtree_Type.__name__ = "DisplayString"
_Gs2352SnmpViewsOIDSubtree_Object = MibTableColumn
gs2352SnmpViewsOIDSubtree = _Gs2352SnmpViewsOIDSubtree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2, 1, 4),
    _Gs2352SnmpViewsOIDSubtree_Type()
)
gs2352SnmpViewsOIDSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpViewsOIDSubtree.setStatus("current")


class _Gs2352SnmpViewsRowStatus_Type(Integer32):
    """Custom type gs2352SnmpViewsRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352SnmpViewsRowStatus_Type.__name__ = "Integer32"
_Gs2352SnmpViewsRowStatus_Object = MibTableColumn
gs2352SnmpViewsRowStatus = _Gs2352SnmpViewsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 6, 2, 1, 5),
    _Gs2352SnmpViewsRowStatus_Type()
)
gs2352SnmpViewsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpViewsRowStatus.setStatus("current")
_Gs2352SnmpAccess_ObjectIdentity = ObjectIdentity
gs2352SnmpAccess = _Gs2352SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7)
)


class _Gs2352SnmpAccessCreate_Type(Integer32):
    """Custom type gs2352SnmpAccessCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352SnmpAccessCreate_Type.__name__ = "Integer32"
_Gs2352SnmpAccessCreate_Object = MibScalar
gs2352SnmpAccessCreate = _Gs2352SnmpAccessCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 1),
    _Gs2352SnmpAccessCreate_Type()
)
gs2352SnmpAccessCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessCreate.setStatus("current")
_Gs2352SnmpAccessTable_Object = MibTable
gs2352SnmpAccessTable = _Gs2352SnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    gs2352SnmpAccessTable.setStatus("current")
_Gs2352SnmpAccessEntry_Object = MibTableRow
gs2352SnmpAccessEntry = _Gs2352SnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1)
)
gs2352SnmpAccessEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    gs2352SnmpAccessEntry.setStatus("current")


class _Gs2352SnmpAccessIndex_Type(Integer32):
    """Custom type gs2352SnmpAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2352SnmpAccessIndex_Type.__name__ = "Integer32"
_Gs2352SnmpAccessIndex_Object = MibTableColumn
gs2352SnmpAccessIndex = _Gs2352SnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 1),
    _Gs2352SnmpAccessIndex_Type()
)
gs2352SnmpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SnmpAccessIndex.setStatus("current")


class _Gs2352SnmpAccessGroupName_Type(DisplayString):
    """Custom type gs2352SnmpAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpAccessGroupName_Type.__name__ = "DisplayString"
_Gs2352SnmpAccessGroupName_Object = MibTableColumn
gs2352SnmpAccessGroupName = _Gs2352SnmpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 2),
    _Gs2352SnmpAccessGroupName_Type()
)
gs2352SnmpAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessGroupName.setStatus("current")


class _Gs2352SnmpAccessSecurityModel_Type(Integer32):
    """Custom type gs2352SnmpAccessSecurityModel based on Integer32"""
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
        *(("any", 0),
          ("v1", 1),
          ("v2c", 2),
          ("usm", 3))
    )


_Gs2352SnmpAccessSecurityModel_Type.__name__ = "Integer32"
_Gs2352SnmpAccessSecurityModel_Object = MibTableColumn
gs2352SnmpAccessSecurityModel = _Gs2352SnmpAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 3),
    _Gs2352SnmpAccessSecurityModel_Type()
)
gs2352SnmpAccessSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessSecurityModel.setStatus("current")


class _Gs2352SnmpAccessSecurityLevel_Type(Integer32):
    """Custom type gs2352SnmpAccessSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noauthnopriv", 1),
          ("authnopriv", 2),
          ("authpriv", 3))
    )


_Gs2352SnmpAccessSecurityLevel_Type.__name__ = "Integer32"
_Gs2352SnmpAccessSecurityLevel_Object = MibTableColumn
gs2352SnmpAccessSecurityLevel = _Gs2352SnmpAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 4),
    _Gs2352SnmpAccessSecurityLevel_Type()
)
gs2352SnmpAccessSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessSecurityLevel.setStatus("current")


class _Gs2352SnmpAccessReadViewName_Type(DisplayString):
    """Custom type gs2352SnmpAccessReadViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpAccessReadViewName_Type.__name__ = "DisplayString"
_Gs2352SnmpAccessReadViewName_Object = MibTableColumn
gs2352SnmpAccessReadViewName = _Gs2352SnmpAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 5),
    _Gs2352SnmpAccessReadViewName_Type()
)
gs2352SnmpAccessReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessReadViewName.setStatus("current")


class _Gs2352SnmpAccessWriteViewName_Type(DisplayString):
    """Custom type gs2352SnmpAccessWriteViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352SnmpAccessWriteViewName_Type.__name__ = "DisplayString"
_Gs2352SnmpAccessWriteViewName_Object = MibTableColumn
gs2352SnmpAccessWriteViewName = _Gs2352SnmpAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 6),
    _Gs2352SnmpAccessWriteViewName_Type()
)
gs2352SnmpAccessWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessWriteViewName.setStatus("current")


class _Gs2352SnmpAccessRowStatus_Type(Integer32):
    """Custom type gs2352SnmpAccessRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352SnmpAccessRowStatus_Type.__name__ = "Integer32"
_Gs2352SnmpAccessRowStatus_Object = MibTableColumn
gs2352SnmpAccessRowStatus = _Gs2352SnmpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 1, 6, 7, 2, 1, 7),
    _Gs2352SnmpAccessRowStatus_Type()
)
gs2352SnmpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SnmpAccessRowStatus.setStatus("current")
_Gs2352Configuration_ObjectIdentity = ObjectIdentity
gs2352Configuration = _Gs2352Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2)
)
_Gs2352Port_ObjectIdentity = ObjectIdentity
gs2352Port = _Gs2352Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1)
)
_Gs2352PortConfigurationTable_Object = MibTable
gs2352PortConfigurationTable = _Gs2352PortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1)
)
if mibBuilder.loadTexts:
    gs2352PortConfigurationTable.setStatus("current")
_Gs2352PortConfigurationEntry_Object = MibTableRow
gs2352PortConfigurationEntry = _Gs2352PortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1)
)
gs2352PortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352PortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352PortConfigurationEntry.setStatus("current")


class _Gs2352PortConfPort_Type(Integer32):
    """Custom type gs2352PortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortConfPort_Type.__name__ = "Integer32"
_Gs2352PortConfPort_Object = MibTableColumn
gs2352PortConfPort = _Gs2352PortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 1),
    _Gs2352PortConfPort_Type()
)
gs2352PortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352PortConfPort.setStatus("current")


class _Gs2352PortConfPortMedia_Type(DisplayString):
    """Custom type gs2352PortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Gs2352PortConfPortMedia_Type.__name__ = "DisplayString"
_Gs2352PortConfPortMedia_Object = MibTableColumn
gs2352PortConfPortMedia = _Gs2352PortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 2),
    _Gs2352PortConfPortMedia_Type()
)
gs2352PortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortConfPortMedia.setStatus("current")


class _Gs2352PortConfLink_Type(DisplayString):
    """Custom type gs2352PortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Gs2352PortConfLink_Type.__name__ = "DisplayString"
_Gs2352PortConfLink_Object = MibTableColumn
gs2352PortConfLink = _Gs2352PortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 3),
    _Gs2352PortConfLink_Type()
)
gs2352PortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortConfLink.setStatus("current")


class _Gs2352PortConfCurrentSpeed_Type(DisplayString):
    """Custom type gs2352PortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Gs2352PortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Gs2352PortConfCurrentSpeed_Object = MibTableColumn
gs2352PortConfCurrentSpeed = _Gs2352PortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 4),
    _Gs2352PortConfCurrentSpeed_Type()
)
gs2352PortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortConfCurrentSpeed.setStatus("current")


class _Gs2352PortConfSpeed_Type(Integer32):
    """Custom type gs2352PortConfSpeed based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("auto", 1),
          ("speed10Half", 2),
          ("speed10Full", 3),
          ("speed100Half", 4),
          ("speed100Full", 5),
          ("speed1Gfull", 6),
          ("sfpAutoAMS", 7),
          ("speed100FXAMS", 8),
          ("speed1000XAMS", 9),
          ("speed100FX", 10),
          ("speed1000X", 11),
          ("speed10GFull", 12))
    )


_Gs2352PortConfSpeed_Type.__name__ = "Integer32"
_Gs2352PortConfSpeed_Object = MibTableColumn
gs2352PortConfSpeed = _Gs2352PortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 5),
    _Gs2352PortConfSpeed_Type()
)
gs2352PortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortConfSpeed.setStatus("current")


class _Gs2352PortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type gs2352PortConfCurrentFlowControlRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("noSupport", 2))
    )


_Gs2352PortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Gs2352PortConfCurrentFlowControlRx_Object = MibTableColumn
gs2352PortConfCurrentFlowControlRx = _Gs2352PortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 6),
    _Gs2352PortConfCurrentFlowControlRx_Type()
)
gs2352PortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortConfCurrentFlowControlRx.setStatus("current")


class _Gs2352PortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type gs2352PortConfCurrentFlowControlTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("noSupport", 2))
    )


_Gs2352PortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Gs2352PortConfCurrentFlowControlTx_Object = MibTableColumn
gs2352PortConfCurrentFlowControlTx = _Gs2352PortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 7),
    _Gs2352PortConfCurrentFlowControlTx_Type()
)
gs2352PortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortConfCurrentFlowControlTx.setStatus("current")


class _Gs2352PortConfFlowControl_Type(Integer32):
    """Custom type gs2352PortConfFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("noSupport", 2))
    )


_Gs2352PortConfFlowControl_Type.__name__ = "Integer32"
_Gs2352PortConfFlowControl_Object = MibTableColumn
gs2352PortConfFlowControl = _Gs2352PortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 8),
    _Gs2352PortConfFlowControl_Type()
)
gs2352PortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortConfFlowControl.setStatus("current")


class _Gs2352PortConfMaxFrameSize_Type(Integer32):
    """Custom type gs2352PortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Gs2352PortConfMaxFrameSize_Type.__name__ = "Integer32"
_Gs2352PortConfMaxFrameSize_Object = MibTableColumn
gs2352PortConfMaxFrameSize = _Gs2352PortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 9),
    _Gs2352PortConfMaxFrameSize_Type()
)
gs2352PortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortConfMaxFrameSize.setStatus("current")


class _Gs2352PortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type gs2352PortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("restart", 1),
          ("noSupport", 2))
    )


_Gs2352PortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Gs2352PortConfExcessiveCollisionMode_Object = MibTableColumn
gs2352PortConfExcessiveCollisionMode = _Gs2352PortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 10),
    _Gs2352PortConfExcessiveCollisionMode_Type()
)
gs2352PortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortConfExcessiveCollisionMode.setStatus("current")


class _Gs2352PortConfPowerControl_Type(Integer32):
    """Custom type gs2352PortConfPowerControl based on Integer32"""
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
        *(("disable", 0),
          ("actiphy", 1),
          ("dynamic", 2),
          ("enable", 3),
          ("noSupport", 4))
    )


_Gs2352PortConfPowerControl_Type.__name__ = "Integer32"
_Gs2352PortConfPowerControl_Object = MibTableColumn
gs2352PortConfPowerControl = _Gs2352PortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 11),
    _Gs2352PortConfPowerControl_Type()
)
gs2352PortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortConfPowerControl.setStatus("current")
_Gs2352PortConfDescription_Type = DisplayString
_Gs2352PortConfDescription_Object = MibTableColumn
gs2352PortConfDescription = _Gs2352PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 1, 1, 12),
    _Gs2352PortConfDescription_Type()
)
gs2352PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortConfDescription.setStatus("current")
_Gs2352PortTrafficStatisticsTable_Object = MibTable
gs2352PortTrafficStatisticsTable = _Gs2352PortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352PortTrafficStatisticsTable.setStatus("current")
_Gs2352PortTrafficStatisticsEntry_Object = MibTableRow
gs2352PortTrafficStatisticsEntry = _Gs2352PortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1)
)
gs2352PortTrafficStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352PortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2352PortTrafficStatisticsEntry.setStatus("current")


class _Gs2352PortTrafficStatisticsPort_Type(Integer32):
    """Custom type gs2352PortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Gs2352PortTrafficStatisticsPort_Object = MibTableColumn
gs2352PortTrafficStatisticsPort = _Gs2352PortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 1),
    _Gs2352PortTrafficStatisticsPort_Type()
)
gs2352PortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352PortTrafficStatisticsPort.setStatus("current")


class _Gs2352PortTrafficStatisticsClear_Type(Integer32):
    """Custom type gs2352PortTrafficStatisticsClear based on Integer32"""
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


_Gs2352PortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Gs2352PortTrafficStatisticsClear_Object = MibTableColumn
gs2352PortTrafficStatisticsClear = _Gs2352PortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 2),
    _Gs2352PortTrafficStatisticsClear_Type()
)
gs2352PortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortTrafficStatisticsClear.setStatus("current")
_Gs2352PortTrafficRxPackets_Type = Counter64
_Gs2352PortTrafficRxPackets_Object = MibTableColumn
gs2352PortTrafficRxPackets = _Gs2352PortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 3),
    _Gs2352PortTrafficRxPackets_Type()
)
gs2352PortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxPackets.setStatus("current")
_Gs2352PortTrafficRxOctets_Type = Counter64
_Gs2352PortTrafficRxOctets_Object = MibTableColumn
gs2352PortTrafficRxOctets = _Gs2352PortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 4),
    _Gs2352PortTrafficRxOctets_Type()
)
gs2352PortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxOctets.setStatus("current")
_Gs2352PortTrafficRxUnicast_Type = Counter64
_Gs2352PortTrafficRxUnicast_Object = MibTableColumn
gs2352PortTrafficRxUnicast = _Gs2352PortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 5),
    _Gs2352PortTrafficRxUnicast_Type()
)
gs2352PortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxUnicast.setStatus("current")
_Gs2352PortTrafficRxMulticast_Type = Counter64
_Gs2352PortTrafficRxMulticast_Object = MibTableColumn
gs2352PortTrafficRxMulticast = _Gs2352PortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 6),
    _Gs2352PortTrafficRxMulticast_Type()
)
gs2352PortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxMulticast.setStatus("current")
_Gs2352PortTrafficRxBroadcast_Type = Counter64
_Gs2352PortTrafficRxBroadcast_Object = MibTableColumn
gs2352PortTrafficRxBroadcast = _Gs2352PortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 7),
    _Gs2352PortTrafficRxBroadcast_Type()
)
gs2352PortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxBroadcast.setStatus("current")
_Gs2352PortTrafficRxPause_Type = Counter64
_Gs2352PortTrafficRxPause_Object = MibTableColumn
gs2352PortTrafficRxPause = _Gs2352PortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 8),
    _Gs2352PortTrafficRxPause_Type()
)
gs2352PortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxPause.setStatus("current")
_Gs2352PortTrafficRx64Bytes_Type = Counter64
_Gs2352PortTrafficRx64Bytes_Object = MibTableColumn
gs2352PortTrafficRx64Bytes = _Gs2352PortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 9),
    _Gs2352PortTrafficRx64Bytes_Type()
)
gs2352PortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRx64Bytes.setStatus("current")
_Gs2352PortTrafficRx65to127Bytes_Type = Counter64
_Gs2352PortTrafficRx65to127Bytes_Object = MibTableColumn
gs2352PortTrafficRx65to127Bytes = _Gs2352PortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 10),
    _Gs2352PortTrafficRx65to127Bytes_Type()
)
gs2352PortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRx65to127Bytes.setStatus("current")
_Gs2352PortTrafficRx128to255Bytes_Type = Counter64
_Gs2352PortTrafficRx128to255Bytes_Object = MibTableColumn
gs2352PortTrafficRx128to255Bytes = _Gs2352PortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 11),
    _Gs2352PortTrafficRx128to255Bytes_Type()
)
gs2352PortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRx128to255Bytes.setStatus("current")
_Gs2352PortTrafficRx256to511Bytes_Type = Counter64
_Gs2352PortTrafficRx256to511Bytes_Object = MibTableColumn
gs2352PortTrafficRx256to511Bytes = _Gs2352PortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 12),
    _Gs2352PortTrafficRx256to511Bytes_Type()
)
gs2352PortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRx256to511Bytes.setStatus("current")
_Gs2352PortTrafficRx512to1023Bytes_Type = Counter64
_Gs2352PortTrafficRx512to1023Bytes_Object = MibTableColumn
gs2352PortTrafficRx512to1023Bytes = _Gs2352PortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 13),
    _Gs2352PortTrafficRx512to1023Bytes_Type()
)
gs2352PortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRx512to1023Bytes.setStatus("current")
_Gs2352PortTrafficRx1024to1526Bytes_Type = Counter64
_Gs2352PortTrafficRx1024to1526Bytes_Object = MibTableColumn
gs2352PortTrafficRx1024to1526Bytes = _Gs2352PortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 14),
    _Gs2352PortTrafficRx1024to1526Bytes_Type()
)
gs2352PortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRx1024to1526Bytes.setStatus("current")
_Gs2352PortTrafficRxExceecd1527Bytes_Type = Counter64
_Gs2352PortTrafficRxExceecd1527Bytes_Object = MibTableColumn
gs2352PortTrafficRxExceecd1527Bytes = _Gs2352PortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 15),
    _Gs2352PortTrafficRxExceecd1527Bytes_Type()
)
gs2352PortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxExceecd1527Bytes.setStatus("current")
_Gs2352PortTrafficRxQ0_Type = Counter64
_Gs2352PortTrafficRxQ0_Object = MibTableColumn
gs2352PortTrafficRxQ0 = _Gs2352PortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 16),
    _Gs2352PortTrafficRxQ0_Type()
)
gs2352PortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ0.setStatus("current")
_Gs2352PortTrafficRxQ1_Type = Counter64
_Gs2352PortTrafficRxQ1_Object = MibTableColumn
gs2352PortTrafficRxQ1 = _Gs2352PortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 17),
    _Gs2352PortTrafficRxQ1_Type()
)
gs2352PortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ1.setStatus("current")
_Gs2352PortTrafficRxQ2_Type = Counter64
_Gs2352PortTrafficRxQ2_Object = MibTableColumn
gs2352PortTrafficRxQ2 = _Gs2352PortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 18),
    _Gs2352PortTrafficRxQ2_Type()
)
gs2352PortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ2.setStatus("current")
_Gs2352PortTrafficRxQ3_Type = Counter64
_Gs2352PortTrafficRxQ3_Object = MibTableColumn
gs2352PortTrafficRxQ3 = _Gs2352PortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 19),
    _Gs2352PortTrafficRxQ3_Type()
)
gs2352PortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ3.setStatus("current")
_Gs2352PortTrafficRxQ4_Type = Counter64
_Gs2352PortTrafficRxQ4_Object = MibTableColumn
gs2352PortTrafficRxQ4 = _Gs2352PortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 20),
    _Gs2352PortTrafficRxQ4_Type()
)
gs2352PortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ4.setStatus("current")
_Gs2352PortTrafficRxQ5_Type = Counter64
_Gs2352PortTrafficRxQ5_Object = MibTableColumn
gs2352PortTrafficRxQ5 = _Gs2352PortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 21),
    _Gs2352PortTrafficRxQ5_Type()
)
gs2352PortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ5.setStatus("current")
_Gs2352PortTrafficRxQ6_Type = Counter64
_Gs2352PortTrafficRxQ6_Object = MibTableColumn
gs2352PortTrafficRxQ6 = _Gs2352PortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 22),
    _Gs2352PortTrafficRxQ6_Type()
)
gs2352PortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ6.setStatus("current")
_Gs2352PortTrafficRxQ7_Type = Counter64
_Gs2352PortTrafficRxQ7_Object = MibTableColumn
gs2352PortTrafficRxQ7 = _Gs2352PortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 23),
    _Gs2352PortTrafficRxQ7_Type()
)
gs2352PortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxQ7.setStatus("current")
_Gs2352PortTrafficRxDrops_Type = Counter64
_Gs2352PortTrafficRxDrops_Object = MibTableColumn
gs2352PortTrafficRxDrops = _Gs2352PortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 24),
    _Gs2352PortTrafficRxDrops_Type()
)
gs2352PortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxDrops.setStatus("current")
_Gs2352PortTrafficRxCRCorAlignment_Type = Counter64
_Gs2352PortTrafficRxCRCorAlignment_Object = MibTableColumn
gs2352PortTrafficRxCRCorAlignment = _Gs2352PortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 25),
    _Gs2352PortTrafficRxCRCorAlignment_Type()
)
gs2352PortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxCRCorAlignment.setStatus("current")
_Gs2352PortTrafficRxUndersize_Type = Counter64
_Gs2352PortTrafficRxUndersize_Object = MibTableColumn
gs2352PortTrafficRxUndersize = _Gs2352PortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 26),
    _Gs2352PortTrafficRxUndersize_Type()
)
gs2352PortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxUndersize.setStatus("current")
_Gs2352PortTrafficRxOversize_Type = Counter64
_Gs2352PortTrafficRxOversize_Object = MibTableColumn
gs2352PortTrafficRxOversize = _Gs2352PortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 27),
    _Gs2352PortTrafficRxOversize_Type()
)
gs2352PortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxOversize.setStatus("current")
_Gs2352PortTrafficRxFragments_Type = Counter64
_Gs2352PortTrafficRxFragments_Object = MibTableColumn
gs2352PortTrafficRxFragments = _Gs2352PortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 28),
    _Gs2352PortTrafficRxFragments_Type()
)
gs2352PortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxFragments.setStatus("current")
_Gs2352PortTrafficRxJabber_Type = Counter64
_Gs2352PortTrafficRxJabber_Object = MibTableColumn
gs2352PortTrafficRxJabber = _Gs2352PortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 29),
    _Gs2352PortTrafficRxJabber_Type()
)
gs2352PortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxJabber.setStatus("current")
_Gs2352PortTrafficRxFiltered_Type = Counter64
_Gs2352PortTrafficRxFiltered_Object = MibTableColumn
gs2352PortTrafficRxFiltered = _Gs2352PortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 30),
    _Gs2352PortTrafficRxFiltered_Type()
)
gs2352PortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficRxFiltered.setStatus("current")
_Gs2352PortTrafficTxPackets_Type = Counter64
_Gs2352PortTrafficTxPackets_Object = MibTableColumn
gs2352PortTrafficTxPackets = _Gs2352PortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 31),
    _Gs2352PortTrafficTxPackets_Type()
)
gs2352PortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxPackets.setStatus("current")
_Gs2352PortTrafficTxOctets_Type = Counter64
_Gs2352PortTrafficTxOctets_Object = MibTableColumn
gs2352PortTrafficTxOctets = _Gs2352PortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 32),
    _Gs2352PortTrafficTxOctets_Type()
)
gs2352PortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxOctets.setStatus("current")
_Gs2352PortTrafficTxUnicast_Type = Counter64
_Gs2352PortTrafficTxUnicast_Object = MibTableColumn
gs2352PortTrafficTxUnicast = _Gs2352PortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 33),
    _Gs2352PortTrafficTxUnicast_Type()
)
gs2352PortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxUnicast.setStatus("current")
_Gs2352PortTrafficTxMulticast_Type = Counter64
_Gs2352PortTrafficTxMulticast_Object = MibTableColumn
gs2352PortTrafficTxMulticast = _Gs2352PortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 34),
    _Gs2352PortTrafficTxMulticast_Type()
)
gs2352PortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxMulticast.setStatus("current")
_Gs2352PortTrafficTxBroadcast_Type = Counter64
_Gs2352PortTrafficTxBroadcast_Object = MibTableColumn
gs2352PortTrafficTxBroadcast = _Gs2352PortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 35),
    _Gs2352PortTrafficTxBroadcast_Type()
)
gs2352PortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxBroadcast.setStatus("current")
_Gs2352PortTrafficTxPause_Type = Counter64
_Gs2352PortTrafficTxPause_Object = MibTableColumn
gs2352PortTrafficTxPause = _Gs2352PortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 36),
    _Gs2352PortTrafficTxPause_Type()
)
gs2352PortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxPause.setStatus("current")
_Gs2352PortTrafficTx64Bytes_Type = Counter64
_Gs2352PortTrafficTx64Bytes_Object = MibTableColumn
gs2352PortTrafficTx64Bytes = _Gs2352PortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 37),
    _Gs2352PortTrafficTx64Bytes_Type()
)
gs2352PortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTx64Bytes.setStatus("current")
_Gs2352PortTrafficTx65to127Bytes_Type = Counter64
_Gs2352PortTrafficTx65to127Bytes_Object = MibTableColumn
gs2352PortTrafficTx65to127Bytes = _Gs2352PortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 38),
    _Gs2352PortTrafficTx65to127Bytes_Type()
)
gs2352PortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTx65to127Bytes.setStatus("current")
_Gs2352PortTrafficTx128to255Bytes_Type = Counter64
_Gs2352PortTrafficTx128to255Bytes_Object = MibTableColumn
gs2352PortTrafficTx128to255Bytes = _Gs2352PortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 39),
    _Gs2352PortTrafficTx128to255Bytes_Type()
)
gs2352PortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTx128to255Bytes.setStatus("current")
_Gs2352PortTrafficTx256to511Bytes_Type = Counter64
_Gs2352PortTrafficTx256to511Bytes_Object = MibTableColumn
gs2352PortTrafficTx256to511Bytes = _Gs2352PortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 40),
    _Gs2352PortTrafficTx256to511Bytes_Type()
)
gs2352PortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTx256to511Bytes.setStatus("current")
_Gs2352PortTrafficTx512to1023Bytes_Type = Counter64
_Gs2352PortTrafficTx512to1023Bytes_Object = MibTableColumn
gs2352PortTrafficTx512to1023Bytes = _Gs2352PortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 41),
    _Gs2352PortTrafficTx512to1023Bytes_Type()
)
gs2352PortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTx512to1023Bytes.setStatus("current")
_Gs2352PortTrafficTx1024to1526Bytes_Type = Counter64
_Gs2352PortTrafficTx1024to1526Bytes_Object = MibTableColumn
gs2352PortTrafficTx1024to1526Bytes = _Gs2352PortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 42),
    _Gs2352PortTrafficTx1024to1526Bytes_Type()
)
gs2352PortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTx1024to1526Bytes.setStatus("current")
_Gs2352PortTrafficTxExceecd1527Bytes_Type = Counter64
_Gs2352PortTrafficTxExceecd1527Bytes_Object = MibTableColumn
gs2352PortTrafficTxExceecd1527Bytes = _Gs2352PortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 43),
    _Gs2352PortTrafficTxExceecd1527Bytes_Type()
)
gs2352PortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxExceecd1527Bytes.setStatus("current")
_Gs2352PortTrafficTxQ0_Type = Counter64
_Gs2352PortTrafficTxQ0_Object = MibTableColumn
gs2352PortTrafficTxQ0 = _Gs2352PortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 44),
    _Gs2352PortTrafficTxQ0_Type()
)
gs2352PortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ0.setStatus("current")
_Gs2352PortTrafficTxQ1_Type = Counter64
_Gs2352PortTrafficTxQ1_Object = MibTableColumn
gs2352PortTrafficTxQ1 = _Gs2352PortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 45),
    _Gs2352PortTrafficTxQ1_Type()
)
gs2352PortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ1.setStatus("current")
_Gs2352PortTrafficTxQ2_Type = Counter64
_Gs2352PortTrafficTxQ2_Object = MibTableColumn
gs2352PortTrafficTxQ2 = _Gs2352PortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 46),
    _Gs2352PortTrafficTxQ2_Type()
)
gs2352PortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ2.setStatus("current")
_Gs2352PortTrafficTxQ3_Type = Counter64
_Gs2352PortTrafficTxQ3_Object = MibTableColumn
gs2352PortTrafficTxQ3 = _Gs2352PortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 47),
    _Gs2352PortTrafficTxQ3_Type()
)
gs2352PortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ3.setStatus("current")
_Gs2352PortTrafficTxQ4_Type = Counter64
_Gs2352PortTrafficTxQ4_Object = MibTableColumn
gs2352PortTrafficTxQ4 = _Gs2352PortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 48),
    _Gs2352PortTrafficTxQ4_Type()
)
gs2352PortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ4.setStatus("current")
_Gs2352PortTrafficTxQ5_Type = Counter64
_Gs2352PortTrafficTxQ5_Object = MibTableColumn
gs2352PortTrafficTxQ5 = _Gs2352PortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 49),
    _Gs2352PortTrafficTxQ5_Type()
)
gs2352PortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ5.setStatus("current")
_Gs2352PortTrafficTxQ6_Type = Counter64
_Gs2352PortTrafficTxQ6_Object = MibTableColumn
gs2352PortTrafficTxQ6 = _Gs2352PortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 50),
    _Gs2352PortTrafficTxQ6_Type()
)
gs2352PortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ6.setStatus("current")
_Gs2352PortTrafficTxQ7_Type = Counter64
_Gs2352PortTrafficTxQ7_Object = MibTableColumn
gs2352PortTrafficTxQ7 = _Gs2352PortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 51),
    _Gs2352PortTrafficTxQ7_Type()
)
gs2352PortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxQ7.setStatus("current")
_Gs2352PortTrafficTxDrops_Type = Counter64
_Gs2352PortTrafficTxDrops_Object = MibTableColumn
gs2352PortTrafficTxDrops = _Gs2352PortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 52),
    _Gs2352PortTrafficTxDrops_Type()
)
gs2352PortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxDrops.setStatus("current")
_Gs2352PortTrafficTxLateOrExcColl_Type = Counter64
_Gs2352PortTrafficTxLateOrExcColl_Object = MibTableColumn
gs2352PortTrafficTxLateOrExcColl = _Gs2352PortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 2, 1, 53),
    _Gs2352PortTrafficTxLateOrExcColl_Type()
)
gs2352PortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortTrafficTxLateOrExcColl.setStatus("current")
_Gs2352PortQoSStatistics_ObjectIdentity = ObjectIdentity
gs2352PortQoSStatistics = _Gs2352PortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3)
)


class _Gs2352PortQoSStatisticsClear_Type(Integer32):
    """Custom type gs2352PortQoSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352PortQoSStatisticsClear_Type.__name__ = "Integer32"
_Gs2352PortQoSStatisticsClear_Object = MibScalar
gs2352PortQoSStatisticsClear = _Gs2352PortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 1),
    _Gs2352PortQoSStatisticsClear_Type()
)
gs2352PortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSStatisticsClear.setStatus("current")
_Gs2352PortQoSStatisticsTable_Object = MibTable
gs2352PortQoSStatisticsTable = _Gs2352PortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352PortQoSStatisticsTable.setStatus("current")
_Gs2352PortQoSStatisticsEntry_Object = MibTableRow
gs2352PortQoSStatisticsEntry = _Gs2352PortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1)
)
gs2352PortQoSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352PortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2352PortQoSStatisticsEntry.setStatus("current")


class _Gs2352PortQoSStatisticsPort_Type(Integer32):
    """Custom type gs2352PortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortQoSStatisticsPort_Type.__name__ = "Integer32"
_Gs2352PortQoSStatisticsPort_Object = MibTableColumn
gs2352PortQoSStatisticsPort = _Gs2352PortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 1),
    _Gs2352PortQoSStatisticsPort_Type()
)
gs2352PortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352PortQoSStatisticsPort.setStatus("current")
_Gs2352PortQoSQ0Rx_Type = Counter64
_Gs2352PortQoSQ0Rx_Object = MibTableColumn
gs2352PortQoSQ0Rx = _Gs2352PortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 2),
    _Gs2352PortQoSQ0Rx_Type()
)
gs2352PortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ0Rx.setStatus("current")
_Gs2352PortQoSQ0Tx_Type = Counter64
_Gs2352PortQoSQ0Tx_Object = MibTableColumn
gs2352PortQoSQ0Tx = _Gs2352PortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 3),
    _Gs2352PortQoSQ0Tx_Type()
)
gs2352PortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ0Tx.setStatus("current")
_Gs2352PortQoSQ1Rx_Type = Counter64
_Gs2352PortQoSQ1Rx_Object = MibTableColumn
gs2352PortQoSQ1Rx = _Gs2352PortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 4),
    _Gs2352PortQoSQ1Rx_Type()
)
gs2352PortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ1Rx.setStatus("current")
_Gs2352PortQoSQ1Tx_Type = Counter64
_Gs2352PortQoSQ1Tx_Object = MibTableColumn
gs2352PortQoSQ1Tx = _Gs2352PortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 5),
    _Gs2352PortQoSQ1Tx_Type()
)
gs2352PortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ1Tx.setStatus("current")
_Gs2352PortQoSQ2Rx_Type = Counter64
_Gs2352PortQoSQ2Rx_Object = MibTableColumn
gs2352PortQoSQ2Rx = _Gs2352PortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 6),
    _Gs2352PortQoSQ2Rx_Type()
)
gs2352PortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ2Rx.setStatus("current")
_Gs2352PortQoSQ2Tx_Type = Counter64
_Gs2352PortQoSQ2Tx_Object = MibTableColumn
gs2352PortQoSQ2Tx = _Gs2352PortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 7),
    _Gs2352PortQoSQ2Tx_Type()
)
gs2352PortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ2Tx.setStatus("current")
_Gs2352PortQoSQ3Rx_Type = Counter64
_Gs2352PortQoSQ3Rx_Object = MibTableColumn
gs2352PortQoSQ3Rx = _Gs2352PortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 8),
    _Gs2352PortQoSQ3Rx_Type()
)
gs2352PortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ3Rx.setStatus("current")
_Gs2352PortQoSQ3Tx_Type = Counter64
_Gs2352PortQoSQ3Tx_Object = MibTableColumn
gs2352PortQoSQ3Tx = _Gs2352PortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 9),
    _Gs2352PortQoSQ3Tx_Type()
)
gs2352PortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ3Tx.setStatus("current")
_Gs2352PortQoSQ4Rx_Type = Counter64
_Gs2352PortQoSQ4Rx_Object = MibTableColumn
gs2352PortQoSQ4Rx = _Gs2352PortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 10),
    _Gs2352PortQoSQ4Rx_Type()
)
gs2352PortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ4Rx.setStatus("current")
_Gs2352PortQoSQ4Tx_Type = Counter64
_Gs2352PortQoSQ4Tx_Object = MibTableColumn
gs2352PortQoSQ4Tx = _Gs2352PortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 11),
    _Gs2352PortQoSQ4Tx_Type()
)
gs2352PortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ4Tx.setStatus("current")
_Gs2352PortQoSQ5Rx_Type = Counter64
_Gs2352PortQoSQ5Rx_Object = MibTableColumn
gs2352PortQoSQ5Rx = _Gs2352PortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 12),
    _Gs2352PortQoSQ5Rx_Type()
)
gs2352PortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ5Rx.setStatus("current")
_Gs2352PortQoSQ5Tx_Type = Counter64
_Gs2352PortQoSQ5Tx_Object = MibTableColumn
gs2352PortQoSQ5Tx = _Gs2352PortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 13),
    _Gs2352PortQoSQ5Tx_Type()
)
gs2352PortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ5Tx.setStatus("current")
_Gs2352PortQoSQ6Rx_Type = Counter64
_Gs2352PortQoSQ6Rx_Object = MibTableColumn
gs2352PortQoSQ6Rx = _Gs2352PortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 14),
    _Gs2352PortQoSQ6Rx_Type()
)
gs2352PortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ6Rx.setStatus("current")
_Gs2352PortQoSQ6Tx_Type = Counter64
_Gs2352PortQoSQ6Tx_Object = MibTableColumn
gs2352PortQoSQ6Tx = _Gs2352PortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 15),
    _Gs2352PortQoSQ6Tx_Type()
)
gs2352PortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ6Tx.setStatus("current")
_Gs2352PortQoSQ7Rx_Type = Counter64
_Gs2352PortQoSQ7Rx_Object = MibTableColumn
gs2352PortQoSQ7Rx = _Gs2352PortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 16),
    _Gs2352PortQoSQ7Rx_Type()
)
gs2352PortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ7Rx.setStatus("current")
_Gs2352PortQoSQ7Tx_Type = Counter64
_Gs2352PortQoSQ7Tx_Object = MibTableColumn
gs2352PortQoSQ7Tx = _Gs2352PortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 3, 2, 1, 17),
    _Gs2352PortQoSQ7Tx_Type()
)
gs2352PortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortQoSQ7Tx.setStatus("current")
_Gs2352SFPInfoTable_Object = MibTable
gs2352SFPInfoTable = _Gs2352SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4)
)
if mibBuilder.loadTexts:
    gs2352SFPInfoTable.setStatus("current")
_Gs2352SFPInfoEntry_Object = MibTableRow
gs2352SFPInfoEntry = _Gs2352SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1)
)
gs2352SFPInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2352SFPInfoEntry.setStatus("current")


class _Gs2352SFPInfoIndex_Type(Integer32):
    """Custom type gs2352SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352SFPInfoIndex_Type.__name__ = "Integer32"
_Gs2352SFPInfoIndex_Object = MibTableColumn
gs2352SFPInfoIndex = _Gs2352SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 1),
    _Gs2352SFPInfoIndex_Type()
)
gs2352SFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352SFPInfoIndex.setStatus("current")
_Gs2352SFPInfoPort_Type = DisplayString
_Gs2352SFPInfoPort_Object = MibTableColumn
gs2352SFPInfoPort = _Gs2352SFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 2),
    _Gs2352SFPInfoPort_Type()
)
gs2352SFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPInfoPort.setStatus("current")
_Gs2352SFPConnectorType_Type = DisplayString
_Gs2352SFPConnectorType_Object = MibTableColumn
gs2352SFPConnectorType = _Gs2352SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 3),
    _Gs2352SFPConnectorType_Type()
)
gs2352SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPConnectorType.setStatus("current")
_Gs2352SFPFiberType_Type = DisplayString
_Gs2352SFPFiberType_Object = MibTableColumn
gs2352SFPFiberType = _Gs2352SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 4),
    _Gs2352SFPFiberType_Type()
)
gs2352SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPFiberType.setStatus("current")
_Gs2352SFPTxCentralWavelength_Type = DisplayString
_Gs2352SFPTxCentralWavelength_Object = MibTableColumn
gs2352SFPTxCentralWavelength = _Gs2352SFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 5),
    _Gs2352SFPTxCentralWavelength_Type()
)
gs2352SFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPTxCentralWavelength.setStatus("current")
_Gs2352SFPBaudRate_Type = DisplayString
_Gs2352SFPBaudRate_Object = MibTableColumn
gs2352SFPBaudRate = _Gs2352SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 6),
    _Gs2352SFPBaudRate_Type()
)
gs2352SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPBaudRate.setStatus("current")
_Gs2352SFPVendorOUI_Type = DisplayString
_Gs2352SFPVendorOUI_Object = MibTableColumn
gs2352SFPVendorOUI = _Gs2352SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 7),
    _Gs2352SFPVendorOUI_Type()
)
gs2352SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPVendorOUI.setStatus("current")
_Gs2352SFPVendorName_Type = DisplayString
_Gs2352SFPVendorName_Object = MibTableColumn
gs2352SFPVendorName = _Gs2352SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 8),
    _Gs2352SFPVendorName_Type()
)
gs2352SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPVendorName.setStatus("current")
_Gs2352SFPVendorPN_Type = DisplayString
_Gs2352SFPVendorPN_Object = MibTableColumn
gs2352SFPVendorPN = _Gs2352SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 9),
    _Gs2352SFPVendorPN_Type()
)
gs2352SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPVendorPN.setStatus("current")
_Gs2352SFPVendorRev_Type = DisplayString
_Gs2352SFPVendorRev_Object = MibTableColumn
gs2352SFPVendorRev = _Gs2352SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 10),
    _Gs2352SFPVendorRev_Type()
)
gs2352SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPVendorRev.setStatus("current")
_Gs2352SFPVendorSN_Type = DisplayString
_Gs2352SFPVendorSN_Object = MibTableColumn
gs2352SFPVendorSN = _Gs2352SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 11),
    _Gs2352SFPVendorSN_Type()
)
gs2352SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPVendorSN.setStatus("current")
_Gs2352SFPDateCode_Type = DisplayString
_Gs2352SFPDateCode_Object = MibTableColumn
gs2352SFPDateCode = _Gs2352SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 12),
    _Gs2352SFPDateCode_Type()
)
gs2352SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPDateCode.setStatus("current")
_Gs2352SFPTemperature_Type = DisplayString
_Gs2352SFPTemperature_Object = MibTableColumn
gs2352SFPTemperature = _Gs2352SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 13),
    _Gs2352SFPTemperature_Type()
)
gs2352SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPTemperature.setStatus("current")
_Gs2352SFPVcc_Type = DisplayString
_Gs2352SFPVcc_Object = MibTableColumn
gs2352SFPVcc = _Gs2352SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 14),
    _Gs2352SFPVcc_Type()
)
gs2352SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPVcc.setStatus("current")
_Gs2352SFPMon1Bias_Type = DisplayString
_Gs2352SFPMon1Bias_Object = MibTableColumn
gs2352SFPMon1Bias = _Gs2352SFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 15),
    _Gs2352SFPMon1Bias_Type()
)
gs2352SFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPMon1Bias.setStatus("current")
_Gs2352SFPMon2TxPWR_Type = DisplayString
_Gs2352SFPMon2TxPWR_Object = MibTableColumn
gs2352SFPMon2TxPWR = _Gs2352SFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 16),
    _Gs2352SFPMon2TxPWR_Type()
)
gs2352SFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPMon2TxPWR.setStatus("current")
_Gs2352SFPMon3RxPWR_Type = DisplayString
_Gs2352SFPMon3RxPWR_Object = MibTableColumn
gs2352SFPMon3RxPWR = _Gs2352SFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1, 4, 1, 17),
    _Gs2352SFPMon3RxPWR_Type()
)
gs2352SFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SFPMon3RxPWR.setStatus("current")
_Gs2352VoiceVLAN_ObjectIdentity = ObjectIdentity
gs2352VoiceVLAN = _Gs2352VoiceVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2)
)
_Gs2352VoiceVLANConf_ObjectIdentity = ObjectIdentity
gs2352VoiceVLANConf = _Gs2352VoiceVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1)
)


class _Gs2352VoiceVLANMode_Type(Integer32):
    """Custom type gs2352VoiceVLANMode based on Integer32"""
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


_Gs2352VoiceVLANMode_Type.__name__ = "Integer32"
_Gs2352VoiceVLANMode_Object = MibScalar
gs2352VoiceVLANMode = _Gs2352VoiceVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 1),
    _Gs2352VoiceVLANMode_Type()
)
gs2352VoiceVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANMode.setStatus("current")


class _Gs2352VoiceVLANVLANId_Type(Integer32):
    """Custom type gs2352VoiceVLANVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352VoiceVLANVLANId_Type.__name__ = "Integer32"
_Gs2352VoiceVLANVLANId_Object = MibScalar
gs2352VoiceVLANVLANId = _Gs2352VoiceVLANVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 2),
    _Gs2352VoiceVLANVLANId_Type()
)
gs2352VoiceVLANVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANVLANId.setStatus("current")


class _Gs2352VoiceVLANAgingTime_Type(Integer32):
    """Custom type gs2352VoiceVLANAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2352VoiceVLANAgingTime_Type.__name__ = "Integer32"
_Gs2352VoiceVLANAgingTime_Object = MibScalar
gs2352VoiceVLANAgingTime = _Gs2352VoiceVLANAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 3),
    _Gs2352VoiceVLANAgingTime_Type()
)
gs2352VoiceVLANAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANAgingTime.setStatus("current")


class _Gs2352VoiceVLANTrafficClass_Type(Integer32):
    """Custom type gs2352VoiceVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352VoiceVLANTrafficClass_Type.__name__ = "Integer32"
_Gs2352VoiceVLANTrafficClass_Object = MibScalar
gs2352VoiceVLANTrafficClass = _Gs2352VoiceVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 4),
    _Gs2352VoiceVLANTrafficClass_Type()
)
gs2352VoiceVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANTrafficClass.setStatus("current")
_Gs2352VoiceVLANPortTable_Object = MibTable
gs2352VoiceVLANPortTable = _Gs2352VoiceVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2352VoiceVLANPortTable.setStatus("current")
_Gs2352VoiceVLANPortEntry_Object = MibTableRow
gs2352VoiceVLANPortEntry = _Gs2352VoiceVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5, 1)
)
gs2352VoiceVLANPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352VoiceVLANPort"),
)
if mibBuilder.loadTexts:
    gs2352VoiceVLANPortEntry.setStatus("current")


class _Gs2352VoiceVLANPort_Type(Integer32):
    """Custom type gs2352VoiceVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352VoiceVLANPort_Type.__name__ = "Integer32"
_Gs2352VoiceVLANPort_Object = MibTableColumn
gs2352VoiceVLANPort = _Gs2352VoiceVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5, 1, 1),
    _Gs2352VoiceVLANPort_Type()
)
gs2352VoiceVLANPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352VoiceVLANPort.setStatus("current")


class _Gs2352VoiceVLANPortMode_Type(Integer32):
    """Custom type gs2352VoiceVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("auto", 1),
          ("forced", 2))
    )


_Gs2352VoiceVLANPortMode_Type.__name__ = "Integer32"
_Gs2352VoiceVLANPortMode_Object = MibTableColumn
gs2352VoiceVLANPortMode = _Gs2352VoiceVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5, 1, 2),
    _Gs2352VoiceVLANPortMode_Type()
)
gs2352VoiceVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANPortMode.setStatus("current")


class _Gs2352VoiceVLANPortSecurity_Type(Integer32):
    """Custom type gs2352VoiceVLANPortSecurity based on Integer32"""
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


_Gs2352VoiceVLANPortSecurity_Type.__name__ = "Integer32"
_Gs2352VoiceVLANPortSecurity_Object = MibTableColumn
gs2352VoiceVLANPortSecurity = _Gs2352VoiceVLANPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5, 1, 3),
    _Gs2352VoiceVLANPortSecurity_Type()
)
gs2352VoiceVLANPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANPortSecurity.setStatus("current")


class _Gs2352VoiceVLANPortDiscoveryProtocol_Type(Integer32):
    """Custom type gs2352VoiceVLANPortDiscoveryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oui", 0),
          ("lldp", 1),
          ("both", 2))
    )


_Gs2352VoiceVLANPortDiscoveryProtocol_Type.__name__ = "Integer32"
_Gs2352VoiceVLANPortDiscoveryProtocol_Object = MibTableColumn
gs2352VoiceVLANPortDiscoveryProtocol = _Gs2352VoiceVLANPortDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5, 1, 4),
    _Gs2352VoiceVLANPortDiscoveryProtocol_Type()
)
gs2352VoiceVLANPortDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANPortDiscoveryProtocol.setStatus("current")


class _Gs2352VoiceVLANSkipNAS_Type(Integer32):
    """Custom type gs2352VoiceVLANSkipNAS based on Integer32"""
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


_Gs2352VoiceVLANSkipNAS_Type.__name__ = "Integer32"
_Gs2352VoiceVLANSkipNAS_Object = MibScalar
gs2352VoiceVLANSkipNAS = _Gs2352VoiceVLANSkipNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 1, 5, 1, 5),
    _Gs2352VoiceVLANSkipNAS_Type()
)
gs2352VoiceVLANSkipNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANSkipNAS.setStatus("current")
_Gs2352VoiceVLANOUI_ObjectIdentity = ObjectIdentity
gs2352VoiceVLANOUI = _Gs2352VoiceVLANOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2)
)


class _Gs2352VoiceVLANOUICreate_Type(Integer32):
    """Custom type gs2352VoiceVLANOUICreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352VoiceVLANOUICreate_Type.__name__ = "Integer32"
_Gs2352VoiceVLANOUICreate_Object = MibScalar
gs2352VoiceVLANOUICreate = _Gs2352VoiceVLANOUICreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 1),
    _Gs2352VoiceVLANOUICreate_Type()
)
gs2352VoiceVLANOUICreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANOUICreate.setStatus("current")
_Gs2352VoiceVLANOUITable_Object = MibTable
gs2352VoiceVLANOUITable = _Gs2352VoiceVLANOUITable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352VoiceVLANOUITable.setStatus("current")
_Gs2352VoiceVLANOUIEntry_Object = MibTableRow
gs2352VoiceVLANOUIEntry = _Gs2352VoiceVLANOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 2, 1)
)
gs2352VoiceVLANOUIEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352VoiceVLANOUIIndex"),
)
if mibBuilder.loadTexts:
    gs2352VoiceVLANOUIEntry.setStatus("current")


class _Gs2352VoiceVLANOUIIndex_Type(Integer32):
    """Custom type gs2352VoiceVLANOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2352VoiceVLANOUIIndex_Type.__name__ = "Integer32"
_Gs2352VoiceVLANOUIIndex_Object = MibTableColumn
gs2352VoiceVLANOUIIndex = _Gs2352VoiceVLANOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 2, 1, 1),
    _Gs2352VoiceVLANOUIIndex_Type()
)
gs2352VoiceVLANOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352VoiceVLANOUIIndex.setStatus("current")


class _Gs2352VoiceVLANTelephonyOUI_Type(OctetString):
    """Custom type gs2352VoiceVLANTelephonyOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352VoiceVLANTelephonyOUI_Type.__name__ = "OctetString"
_Gs2352VoiceVLANTelephonyOUI_Object = MibTableColumn
gs2352VoiceVLANTelephonyOUI = _Gs2352VoiceVLANTelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 2, 1, 2),
    _Gs2352VoiceVLANTelephonyOUI_Type()
)
gs2352VoiceVLANTelephonyOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANTelephonyOUI.setStatus("current")


class _Gs2352VoiceVLANDescription_Type(DisplayString):
    """Custom type gs2352VoiceVLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352VoiceVLANDescription_Type.__name__ = "DisplayString"
_Gs2352VoiceVLANDescription_Object = MibTableColumn
gs2352VoiceVLANDescription = _Gs2352VoiceVLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 2, 1, 3),
    _Gs2352VoiceVLANDescription_Type()
)
gs2352VoiceVLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANDescription.setStatus("current")


class _Gs2352VoiceVLANOUIRowStatus_Type(Integer32):
    """Custom type gs2352VoiceVLANOUIRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352VoiceVLANOUIRowStatus_Type.__name__ = "Integer32"
_Gs2352VoiceVLANOUIRowStatus_Object = MibTableColumn
gs2352VoiceVLANOUIRowStatus = _Gs2352VoiceVLANOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 2, 2, 2, 1, 4),
    _Gs2352VoiceVLANOUIRowStatus_Type()
)
gs2352VoiceVLANOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VoiceVLANOUIRowStatus.setStatus("current")
_Gs2352GARP_ObjectIdentity = ObjectIdentity
gs2352GARP = _Gs2352GARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3)
)
_Gs2352GARPConfTable_Object = MibTable
gs2352GARPConfTable = _Gs2352GARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gs2352GARPConfTable.setStatus("current")
_Gs2352GARPConfEntry_Object = MibTableRow
gs2352GARPConfEntry = _Gs2352GARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1)
)
gs2352GARPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352GARPConfPort"),
)
if mibBuilder.loadTexts:
    gs2352GARPConfEntry.setStatus("current")


class _Gs2352GARPConfPort_Type(Integer32):
    """Custom type gs2352GARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352GARPConfPort_Type.__name__ = "Integer32"
_Gs2352GARPConfPort_Object = MibTableColumn
gs2352GARPConfPort = _Gs2352GARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 1),
    _Gs2352GARPConfPort_Type()
)
gs2352GARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352GARPConfPort.setStatus("current")


class _Gs2352GARPJoinTimer_Type(Integer32):
    """Custom type gs2352GARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Gs2352GARPJoinTimer_Type.__name__ = "Integer32"
_Gs2352GARPJoinTimer_Object = MibTableColumn
gs2352GARPJoinTimer = _Gs2352GARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 2),
    _Gs2352GARPJoinTimer_Type()
)
gs2352GARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPJoinTimer.setStatus("current")


class _Gs2352GARPLeaveTimer_Type(Integer32):
    """Custom type gs2352GARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Gs2352GARPLeaveTimer_Type.__name__ = "Integer32"
_Gs2352GARPLeaveTimer_Object = MibTableColumn
gs2352GARPLeaveTimer = _Gs2352GARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 3),
    _Gs2352GARPLeaveTimer_Type()
)
gs2352GARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPLeaveTimer.setStatus("current")


class _Gs2352GARPLeaveAllTimer_Type(Integer32):
    """Custom type gs2352GARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Gs2352GARPLeaveAllTimer_Type.__name__ = "Integer32"
_Gs2352GARPLeaveAllTimer_Object = MibTableColumn
gs2352GARPLeaveAllTimer = _Gs2352GARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 4),
    _Gs2352GARPLeaveAllTimer_Type()
)
gs2352GARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPLeaveAllTimer.setStatus("current")


class _Gs2352GARPApplicantion_Type(Integer32):
    """Custom type gs2352GARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gvrp", 1)
    )


_Gs2352GARPApplicantion_Type.__name__ = "Integer32"
_Gs2352GARPApplicantion_Object = MibTableColumn
gs2352GARPApplicantion = _Gs2352GARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 5),
    _Gs2352GARPApplicantion_Type()
)
gs2352GARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPApplicantion.setStatus("current")


class _Gs2352GARPAttributeType_Type(Integer32):
    """Custom type gs2352GARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_Gs2352GARPAttributeType_Type.__name__ = "Integer32"
_Gs2352GARPAttributeType_Object = MibTableColumn
gs2352GARPAttributeType = _Gs2352GARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 6),
    _Gs2352GARPAttributeType_Type()
)
gs2352GARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPAttributeType.setStatus("current")


class _Gs2352GARPApplicant_Type(Integer32):
    """Custom type gs2352GARPApplicant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("participant", 0),
          ("nonParticipant", 1))
    )


_Gs2352GARPApplicant_Type.__name__ = "Integer32"
_Gs2352GARPApplicant_Object = MibTableColumn
gs2352GARPApplicant = _Gs2352GARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 1, 1, 7),
    _Gs2352GARPApplicant_Type()
)
gs2352GARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GARPApplicant.setStatus("current")
_Gs2352GARPStatisticsTable_Object = MibTable
gs2352GARPStatisticsTable = _Gs2352GARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352GARPStatisticsTable.setStatus("current")
_Gs2352GARPStatisticsEntry_Object = MibTableRow
gs2352GARPStatisticsEntry = _Gs2352GARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 2, 1)
)
gs2352GARPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352GARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2352GARPStatisticsEntry.setStatus("current")


class _Gs2352GARPStatisticsPort_Type(Integer32):
    """Custom type gs2352GARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352GARPStatisticsPort_Type.__name__ = "Integer32"
_Gs2352GARPStatisticsPort_Object = MibTableColumn
gs2352GARPStatisticsPort = _Gs2352GARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 2, 1, 1),
    _Gs2352GARPStatisticsPort_Type()
)
gs2352GARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352GARPStatisticsPort.setStatus("current")
_Gs2352GARPStatisticsPeerMAC_Type = DisplayString
_Gs2352GARPStatisticsPeerMAC_Object = MibTableColumn
gs2352GARPStatisticsPeerMAC = _Gs2352GARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 2, 1, 2),
    _Gs2352GARPStatisticsPeerMAC_Type()
)
gs2352GARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352GARPStatisticsPeerMAC.setStatus("current")
_Gs2352GARPStatisticsFailedCount_Type = Counter32
_Gs2352GARPStatisticsFailedCount_Object = MibTableColumn
gs2352GARPStatisticsFailedCount = _Gs2352GARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 3, 2, 1, 3),
    _Gs2352GARPStatisticsFailedCount_Type()
)
gs2352GARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352GARPStatisticsFailedCount.setStatus("current")
_Gs2352GVRP_ObjectIdentity = ObjectIdentity
gs2352GVRP = _Gs2352GVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4)
)
_Gs2352GVRPConf_ObjectIdentity = ObjectIdentity
gs2352GVRPConf = _Gs2352GVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1)
)


class _Gs2352GVRPMode_Type(Integer32):
    """Custom type gs2352GVRPMode based on Integer32"""
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


_Gs2352GVRPMode_Type.__name__ = "Integer32"
_Gs2352GVRPMode_Object = MibScalar
gs2352GVRPMode = _Gs2352GVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1, 1),
    _Gs2352GVRPMode_Type()
)
gs2352GVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GVRPMode.setStatus("current")
_Gs2352GVRPConfTable_Object = MibTable
gs2352GVRPConfTable = _Gs2352GVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352GVRPConfTable.setStatus("current")
_Gs2352GVRPConfEntry_Object = MibTableRow
gs2352GVRPConfEntry = _Gs2352GVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1, 2, 1)
)
gs2352GVRPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352GVRPConfPort"),
)
if mibBuilder.loadTexts:
    gs2352GVRPConfEntry.setStatus("current")


class _Gs2352GVRPConfPort_Type(Integer32):
    """Custom type gs2352GVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352GVRPConfPort_Type.__name__ = "Integer32"
_Gs2352GVRPConfPort_Object = MibTableColumn
gs2352GVRPConfPort = _Gs2352GVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1, 2, 1, 1),
    _Gs2352GVRPConfPort_Type()
)
gs2352GVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352GVRPConfPort.setStatus("current")


class _Gs2352GVRPConfPortMode_Type(Integer32):
    """Custom type gs2352GVRPConfPortMode based on Integer32"""
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


_Gs2352GVRPConfPortMode_Type.__name__ = "Integer32"
_Gs2352GVRPConfPortMode_Object = MibTableColumn
gs2352GVRPConfPortMode = _Gs2352GVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1, 2, 1, 2),
    _Gs2352GVRPConfPortMode_Type()
)
gs2352GVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GVRPConfPortMode.setStatus("current")


class _Gs2352GVRPConfPortRRole_Type(Integer32):
    """Custom type gs2352GVRPConfPortRRole based on Integer32"""
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


_Gs2352GVRPConfPortRRole_Type.__name__ = "Integer32"
_Gs2352GVRPConfPortRRole_Object = MibTableColumn
gs2352GVRPConfPortRRole = _Gs2352GVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 1, 2, 1, 3),
    _Gs2352GVRPConfPortRRole_Type()
)
gs2352GVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352GVRPConfPortRRole.setStatus("current")
_Gs2352GVRPStatisticsTable_Object = MibTable
gs2352GVRPStatisticsTable = _Gs2352GVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352GVRPStatisticsTable.setStatus("current")
_Gs2352GVRPStatisticsEntry_Object = MibTableRow
gs2352GVRPStatisticsEntry = _Gs2352GVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 2, 1)
)
gs2352GVRPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352GVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2352GVRPStatisticsEntry.setStatus("current")


class _Gs2352GVRPStatisticsPort_Type(Integer32):
    """Custom type gs2352GVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352GVRPStatisticsPort_Type.__name__ = "Integer32"
_Gs2352GVRPStatisticsPort_Object = MibTableColumn
gs2352GVRPStatisticsPort = _Gs2352GVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 2, 1, 1),
    _Gs2352GVRPStatisticsPort_Type()
)
gs2352GVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352GVRPStatisticsPort.setStatus("current")
_Gs2352GVRPStatisticsJoinTxCnt_Type = Counter32
_Gs2352GVRPStatisticsJoinTxCnt_Object = MibTableColumn
gs2352GVRPStatisticsJoinTxCnt = _Gs2352GVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 2, 1, 2),
    _Gs2352GVRPStatisticsJoinTxCnt_Type()
)
gs2352GVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352GVRPStatisticsJoinTxCnt.setStatus("current")
_Gs2352GVRPStatisticsLeaveTxCnt_Type = Counter32
_Gs2352GVRPStatisticsLeaveTxCnt_Object = MibTableColumn
gs2352GVRPStatisticsLeaveTxCnt = _Gs2352GVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 4, 2, 1, 3),
    _Gs2352GVRPStatisticsLeaveTxCnt_Type()
)
gs2352GVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352GVRPStatisticsLeaveTxCnt.setStatus("current")
_Gs2352Mirroring_ObjectIdentity = ObjectIdentity
gs2352Mirroring = _Gs2352Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 6)
)


class _Gs2352PortToMirrorOn_Type(Integer32):
    """Custom type gs2352PortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2352PortToMirrorOn_Type.__name__ = "Integer32"
_Gs2352PortToMirrorOn_Object = MibScalar
gs2352PortToMirrorOn = _Gs2352PortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 6, 1),
    _Gs2352PortToMirrorOn_Type()
)
gs2352PortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortToMirrorOn.setStatus("current")
_Gs2352MirrorTable_Object = MibTable
gs2352MirrorTable = _Gs2352MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gs2352MirrorTable.setStatus("current")
_Gs2352MirrorEntry_Object = MibTableRow
gs2352MirrorEntry = _Gs2352MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 6, 2, 1)
)
gs2352MirrorEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MirrorPort"),
)
if mibBuilder.loadTexts:
    gs2352MirrorEntry.setStatus("current")


class _Gs2352MirrorPort_Type(Integer32):
    """Custom type gs2352MirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MirrorPort_Type.__name__ = "Integer32"
_Gs2352MirrorPort_Object = MibTableColumn
gs2352MirrorPort = _Gs2352MirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 6, 2, 1, 1),
    _Gs2352MirrorPort_Type()
)
gs2352MirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MirrorPort.setStatus("current")


class _Gs2352MirrorMode_Type(Integer32):
    """Custom type gs2352MirrorMode based on Integer32"""
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
        *(("disable", 0),
          ("enable", 1),
          ("rxOnly", 2),
          ("txOnly", 3))
    )


_Gs2352MirrorMode_Type.__name__ = "Integer32"
_Gs2352MirrorMode_Object = MibTableColumn
gs2352MirrorMode = _Gs2352MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 6, 2, 1, 2),
    _Gs2352MirrorMode_Type()
)
gs2352MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MirrorMode.setStatus("current")
_Gs2352TrapEventSeverity_ObjectIdentity = ObjectIdentity
gs2352TrapEventSeverity = _Gs2352TrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7)
)


class _Gs2352TrapEventSeverityACL_Type(Integer32):
    """Custom type gs2352TrapEventSeverityACL based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityACL_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityACL_Object = MibScalar
gs2352TrapEventSeverityACL = _Gs2352TrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 1),
    _Gs2352TrapEventSeverityACL_Type()
)
gs2352TrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityACL.setStatus("current")


class _Gs2352TrapEventSeverityACLLog_Type(Integer32):
    """Custom type gs2352TrapEventSeverityACLLog based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityACLLog_Object = MibScalar
gs2352TrapEventSeverityACLLog = _Gs2352TrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 2),
    _Gs2352TrapEventSeverityACLLog_Type()
)
gs2352TrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityACLLog.setStatus("current")


class _Gs2352TrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type gs2352TrapEventSeverityAccessMgmt based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityAccessMgmt_Object = MibScalar
gs2352TrapEventSeverityAccessMgmt = _Gs2352TrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 3),
    _Gs2352TrapEventSeverityAccessMgmt_Type()
)
gs2352TrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityAccessMgmt.setStatus("current")


class _Gs2352TrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type gs2352TrapEventSeverityAuthFailed based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityAuthFailed_Object = MibScalar
gs2352TrapEventSeverityAuthFailed = _Gs2352TrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 4),
    _Gs2352TrapEventSeverityAuthFailed_Type()
)
gs2352TrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityAuthFailed.setStatus("current")


class _Gs2352TrapEventSeverityColdStart_Type(Integer32):
    """Custom type gs2352TrapEventSeverityColdStart based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityColdStart_Object = MibScalar
gs2352TrapEventSeverityColdStart = _Gs2352TrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 5),
    _Gs2352TrapEventSeverityColdStart_Type()
)
gs2352TrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityColdStart.setStatus("current")


class _Gs2352TrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type gs2352TrapEventSeverityConfigInfo based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityConfigInfo_Object = MibScalar
gs2352TrapEventSeverityConfigInfo = _Gs2352TrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 6),
    _Gs2352TrapEventSeverityConfigInfo_Type()
)
gs2352TrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityConfigInfo.setStatus("current")


class _Gs2352TrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type gs2352TrapEventSeverityFirmwareUpgrade based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityFirmwareUpgrade_Object = MibScalar
gs2352TrapEventSeverityFirmwareUpgrade = _Gs2352TrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 7),
    _Gs2352TrapEventSeverityFirmwareUpgrade_Type()
)
gs2352TrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Gs2352TrapEventSeverityImportExport_Type(Integer32):
    """Custom type gs2352TrapEventSeverityImportExport based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityImportExport_Object = MibScalar
gs2352TrapEventSeverityImportExport = _Gs2352TrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 8),
    _Gs2352TrapEventSeverityImportExport_Type()
)
gs2352TrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityImportExport.setStatus("current")


class _Gs2352TrapEventSeverityLACP_Type(Integer32):
    """Custom type gs2352TrapEventSeverityLACP based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityLACP_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityLACP_Object = MibScalar
gs2352TrapEventSeverityLACP = _Gs2352TrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 9),
    _Gs2352TrapEventSeverityLACP_Type()
)
gs2352TrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityLACP.setStatus("current")


class _Gs2352TrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type gs2352TrapEventSeverityLinkStatus based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityLinkStatus_Object = MibScalar
gs2352TrapEventSeverityLinkStatus = _Gs2352TrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 10),
    _Gs2352TrapEventSeverityLinkStatus_Type()
)
gs2352TrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityLinkStatus.setStatus("current")


class _Gs2352TrapEventSeverityLogin_Type(Integer32):
    """Custom type gs2352TrapEventSeverityLogin based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityLogin_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityLogin_Object = MibScalar
gs2352TrapEventSeverityLogin = _Gs2352TrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 11),
    _Gs2352TrapEventSeverityLogin_Type()
)
gs2352TrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityLogin.setStatus("current")


class _Gs2352TrapEventSeverityLogout_Type(Integer32):
    """Custom type gs2352TrapEventSeverityLogout based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityLogout_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityLogout_Object = MibScalar
gs2352TrapEventSeverityLogout = _Gs2352TrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 12),
    _Gs2352TrapEventSeverityLogout_Type()
)
gs2352TrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityLogout.setStatus("current")


class _Gs2352TrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type gs2352TrapEventSeverityLoopProtect based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityLoopProtect_Object = MibScalar
gs2352TrapEventSeverityLoopProtect = _Gs2352TrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 13),
    _Gs2352TrapEventSeverityLoopProtect_Type()
)
gs2352TrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityLoopProtect.setStatus("current")


class _Gs2352TrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type gs2352TrapEventSeverityMgmtIPChange based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityMgmtIPChange_Object = MibScalar
gs2352TrapEventSeverityMgmtIPChange = _Gs2352TrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 14),
    _Gs2352TrapEventSeverityMgmtIPChange_Type()
)
gs2352TrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityMgmtIPChange.setStatus("current")


class _Gs2352TrapEventSeverityModuleChange_Type(Integer32):
    """Custom type gs2352TrapEventSeverityModuleChange based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityModuleChange_Object = MibScalar
gs2352TrapEventSeverityModuleChange = _Gs2352TrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 15),
    _Gs2352TrapEventSeverityModuleChange_Type()
)
gs2352TrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityModuleChange.setStatus("current")


class _Gs2352TrapEventSeverityNAS_Type(Integer32):
    """Custom type gs2352TrapEventSeverityNAS based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityNAS_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityNAS_Object = MibScalar
gs2352TrapEventSeverityNAS = _Gs2352TrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 16),
    _Gs2352TrapEventSeverityNAS_Type()
)
gs2352TrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityNAS.setStatus("current")


class _Gs2352TrapEventSeverityPasswordChange_Type(Integer32):
    """Custom type gs2352TrapEventSeverityPasswordChange based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityPasswordChange_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityPasswordChange_Object = MibScalar
gs2352TrapEventSeverityPasswordChange = _Gs2352TrapEventSeverityPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 17),
    _Gs2352TrapEventSeverityPasswordChange_Type()
)
gs2352TrapEventSeverityPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityPasswordChange.setStatus("current")


class _Gs2352TrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type gs2352TrapEventSeverityPortSecurity based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityPortSecurity_Object = MibScalar
gs2352TrapEventSeverityPortSecurity = _Gs2352TrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 18),
    _Gs2352TrapEventSeverityPortSecurity_Type()
)
gs2352TrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityPortSecurity.setStatus("current")


class _Gs2352TrapEventSeverityVLAN_Type(Integer32):
    """Custom type gs2352TrapEventSeverityVLAN based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityVLAN_Object = MibScalar
gs2352TrapEventSeverityVLAN = _Gs2352TrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 20),
    _Gs2352TrapEventSeverityVLAN_Type()
)
gs2352TrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityVLAN.setStatus("current")


class _Gs2352TrapEventSeverityWarmStart_Type(Integer32):
    """Custom type gs2352TrapEventSeverityWarmStart based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityWarmStart_Object = MibScalar
gs2352TrapEventSeverityWarmStart = _Gs2352TrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 21),
    _Gs2352TrapEventSeverityWarmStart_Type()
)
gs2352TrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityWarmStart.setStatus("current")


class _Gs2352TrapEventSeverityARPConflict_Type(Integer32):
    """Custom type gs2352TrapEventSeverityARPConflict based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityARPConflict_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityARPConflict_Object = MibScalar
gs2352TrapEventSeverityARPConflict = _Gs2352TrapEventSeverityARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 25),
    _Gs2352TrapEventSeverityARPConflict_Type()
)
gs2352TrapEventSeverityARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityARPConflict.setStatus("current")


class _Gs2352TrapEventSeveritySpoofingLimit_Type(Integer32):
    """Custom type gs2352TrapEventSeveritySpoofingLimit based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeveritySpoofingLimit_Type.__name__ = "Integer32"
_Gs2352TrapEventSeveritySpoofingLimit_Object = MibScalar
gs2352TrapEventSeveritySpoofingLimit = _Gs2352TrapEventSeveritySpoofingLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 27),
    _Gs2352TrapEventSeveritySpoofingLimit_Type()
)
gs2352TrapEventSeveritySpoofingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeveritySpoofingLimit.setStatus("current")


class _Gs2352TrapEventSeverityStaticARPConflict_Type(Integer32):
    """Custom type gs2352TrapEventSeverityStaticARPConflict based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352TrapEventSeverityStaticARPConflict_Type.__name__ = "Integer32"
_Gs2352TrapEventSeverityStaticARPConflict_Object = MibScalar
gs2352TrapEventSeverityStaticARPConflict = _Gs2352TrapEventSeverityStaticARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 7, 28),
    _Gs2352TrapEventSeverityStaticARPConflict_Type()
)
gs2352TrapEventSeverityStaticARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TrapEventSeverityStaticARPConflict.setStatus("current")
_Gs2352SMTP_ObjectIdentity = ObjectIdentity
gs2352SMTP = _Gs2352SMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8)
)
_Gs2352SMTPMailServer_Type = DisplayString
_Gs2352SMTPMailServer_Object = MibScalar
gs2352SMTPMailServer = _Gs2352SMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 1),
    _Gs2352SMTPMailServer_Type()
)
gs2352SMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPMailServer.setStatus("current")
_Gs2352SMTPUserName_Type = DisplayString
_Gs2352SMTPUserName_Object = MibScalar
gs2352SMTPUserName = _Gs2352SMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 2),
    _Gs2352SMTPUserName_Type()
)
gs2352SMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPUserName.setStatus("current")
_Gs2352SMTPPassword_Type = DisplayString
_Gs2352SMTPPassword_Object = MibScalar
gs2352SMTPPassword = _Gs2352SMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 3),
    _Gs2352SMTPPassword_Type()
)
gs2352SMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPPassword.setStatus("current")


class _Gs2352SMTPServeriryLevel_Type(Integer32):
    """Custom type gs2352SMTPServeriryLevel based on Integer32"""
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
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_Gs2352SMTPServeriryLevel_Type.__name__ = "Integer32"
_Gs2352SMTPServeriryLevel_Object = MibScalar
gs2352SMTPServeriryLevel = _Gs2352SMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 4),
    _Gs2352SMTPServeriryLevel_Type()
)
gs2352SMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPServeriryLevel.setStatus("current")
_Gs2352SMTPSender_Type = DisplayString
_Gs2352SMTPSender_Object = MibScalar
gs2352SMTPSender = _Gs2352SMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 5),
    _Gs2352SMTPSender_Type()
)
gs2352SMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPSender.setStatus("current")
_Gs2352SMTPReturnPath_Type = DisplayString
_Gs2352SMTPReturnPath_Object = MibScalar
gs2352SMTPReturnPath = _Gs2352SMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 6),
    _Gs2352SMTPReturnPath_Type()
)
gs2352SMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPReturnPath.setStatus("current")
_Gs2352SMTPEmailAddress1_Type = DisplayString
_Gs2352SMTPEmailAddress1_Object = MibScalar
gs2352SMTPEmailAddress1 = _Gs2352SMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 7),
    _Gs2352SMTPEmailAddress1_Type()
)
gs2352SMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPEmailAddress1.setStatus("current")
_Gs2352SMTPEmailAddress2_Type = DisplayString
_Gs2352SMTPEmailAddress2_Object = MibScalar
gs2352SMTPEmailAddress2 = _Gs2352SMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 8),
    _Gs2352SMTPEmailAddress2_Type()
)
gs2352SMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPEmailAddress2.setStatus("current")
_Gs2352SMTPEmailAddress3_Type = DisplayString
_Gs2352SMTPEmailAddress3_Object = MibScalar
gs2352SMTPEmailAddress3 = _Gs2352SMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 9),
    _Gs2352SMTPEmailAddress3_Type()
)
gs2352SMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPEmailAddress3.setStatus("current")
_Gs2352SMTPEmailAddress4_Type = DisplayString
_Gs2352SMTPEmailAddress4_Object = MibScalar
gs2352SMTPEmailAddress4 = _Gs2352SMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 10),
    _Gs2352SMTPEmailAddress4_Type()
)
gs2352SMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPEmailAddress4.setStatus("current")
_Gs2352SMTPEmailAddress5_Type = DisplayString
_Gs2352SMTPEmailAddress5_Object = MibScalar
gs2352SMTPEmailAddress5 = _Gs2352SMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 11),
    _Gs2352SMTPEmailAddress5_Type()
)
gs2352SMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPEmailAddress5.setStatus("current")
_Gs2352SMTPEmailAddress6_Type = DisplayString
_Gs2352SMTPEmailAddress6_Object = MibScalar
gs2352SMTPEmailAddress6 = _Gs2352SMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 8, 12),
    _Gs2352SMTPEmailAddress6_Type()
)
gs2352SMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SMTPEmailAddress6.setStatus("current")
_Gs2352ACL_ObjectIdentity = ObjectIdentity
gs2352ACL = _Gs2352ACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9)
)
_Gs2352ACLPortsConfTable_Object = MibTable
gs2352ACLPortsConfTable = _Gs2352ACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1)
)
if mibBuilder.loadTexts:
    gs2352ACLPortsConfTable.setStatus("current")
_Gs2352ACLPortsConfEntry_Object = MibTableRow
gs2352ACLPortsConfEntry = _Gs2352ACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1)
)
gs2352ACLPortsConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    gs2352ACLPortsConfEntry.setStatus("current")


class _Gs2352ACLPortsConfPort_Type(Integer32):
    """Custom type gs2352ACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ACLPortsConfPort_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfPort_Object = MibTableColumn
gs2352ACLPortsConfPort = _Gs2352ACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 1),
    _Gs2352ACLPortsConfPort_Type()
)
gs2352ACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfPort.setStatus("current")


class _Gs2352ACLPortsConfPolicyID_Type(Integer32):
    """Custom type gs2352ACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2352ACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfPolicyID_Object = MibTableColumn
gs2352ACLPortsConfPolicyID = _Gs2352ACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 2),
    _Gs2352ACLPortsConfPolicyID_Type()
)
gs2352ACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfPolicyID.setStatus("current")


class _Gs2352ACLPortsConfAction_Type(Integer32):
    """Custom type gs2352ACLPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_Gs2352ACLPortsConfAction_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfAction_Object = MibTableColumn
gs2352ACLPortsConfAction = _Gs2352ACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 3),
    _Gs2352ACLPortsConfAction_Type()
)
gs2352ACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfAction.setStatus("current")


class _Gs2352ACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type gs2352ACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2352ACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfRateLimiterID_Object = MibTableColumn
gs2352ACLPortsConfRateLimiterID = _Gs2352ACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 4),
    _Gs2352ACLPortsConfRateLimiterID_Type()
)
gs2352ACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfRateLimiterID.setStatus("current")


class _Gs2352ACLPortsConfPortRedirect_Type(Integer32):
    """Custom type gs2352ACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gs2352ACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfPortRedirect_Object = MibTableColumn
gs2352ACLPortsConfPortRedirect = _Gs2352ACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 5),
    _Gs2352ACLPortsConfPortRedirect_Type()
)
gs2352ACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfPortRedirect.setStatus("current")


class _Gs2352ACLPortsConfLogging_Type(Integer32):
    """Custom type gs2352ACLPortsConfLogging based on Integer32"""
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


_Gs2352ACLPortsConfLogging_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfLogging_Object = MibTableColumn
gs2352ACLPortsConfLogging = _Gs2352ACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 7),
    _Gs2352ACLPortsConfLogging_Type()
)
gs2352ACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfLogging.setStatus("current")


class _Gs2352ACLPortsConfShutdown_Type(Integer32):
    """Custom type gs2352ACLPortsConfShutdown based on Integer32"""
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


_Gs2352ACLPortsConfShutdown_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfShutdown_Object = MibTableColumn
gs2352ACLPortsConfShutdown = _Gs2352ACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 8),
    _Gs2352ACLPortsConfShutdown_Type()
)
gs2352ACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfShutdown.setStatus("current")


class _Gs2352ACLPortsConfState_Type(Integer32):
    """Custom type gs2352ACLPortsConfState based on Integer32"""
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


_Gs2352ACLPortsConfState_Type.__name__ = "Integer32"
_Gs2352ACLPortsConfState_Object = MibTableColumn
gs2352ACLPortsConfState = _Gs2352ACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 9),
    _Gs2352ACLPortsConfState_Type()
)
gs2352ACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfState.setStatus("current")
_Gs2352ACLPortsConfCounter_Type = Counter32
_Gs2352ACLPortsConfCounter_Object = MibTableColumn
gs2352ACLPortsConfCounter = _Gs2352ACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 1, 1, 10),
    _Gs2352ACLPortsConfCounter_Type()
)
gs2352ACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLPortsConfCounter.setStatus("current")
_Gs2352ACLRateLimiterTable_Object = MibTable
gs2352ACLRateLimiterTable = _Gs2352ACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 2)
)
if mibBuilder.loadTexts:
    gs2352ACLRateLimiterTable.setStatus("current")
_Gs2352ACLRateLimiterEntry_Object = MibTableRow
gs2352ACLRateLimiterEntry = _Gs2352ACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 2, 1)
)
gs2352ACLRateLimiterEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    gs2352ACLRateLimiterEntry.setStatus("current")


class _Gs2352ACLRateLimiterID_Type(Integer32):
    """Custom type gs2352ACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2352ACLRateLimiterID_Type.__name__ = "Integer32"
_Gs2352ACLRateLimiterID_Object = MibTableColumn
gs2352ACLRateLimiterID = _Gs2352ACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 2, 1, 1),
    _Gs2352ACLRateLimiterID_Type()
)
gs2352ACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ACLRateLimiterID.setStatus("current")


class _Gs2352ACLRateLimiterRate_Type(Integer32):
    """Custom type gs2352ACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Gs2352ACLRateLimiterRate_Type.__name__ = "Integer32"
_Gs2352ACLRateLimiterRate_Object = MibTableColumn
gs2352ACLRateLimiterRate = _Gs2352ACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 2, 1, 3),
    _Gs2352ACLRateLimiterRate_Type()
)
gs2352ACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLRateLimiterRate.setStatus("current")
_Gs2352ACLACE_ObjectIdentity = ObjectIdentity
gs2352ACLACE = _Gs2352ACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3)
)


class _Gs2352ACLACECreate_Type(Integer32):
    """Custom type gs2352ACLACECreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352ACLACECreate_Type.__name__ = "Integer32"
_Gs2352ACLACECreate_Object = MibScalar
gs2352ACLACECreate = _Gs2352ACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 1),
    _Gs2352ACLACECreate_Type()
)
gs2352ACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACECreate.setStatus("current")
_Gs2352ACLACETable_Object = MibTable
gs2352ACLACETable = _Gs2352ACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352ACLACETable.setStatus("current")
_Gs2352ACLACEEntry_Object = MibTableRow
gs2352ACLACEEntry = _Gs2352ACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1)
)
gs2352ACLACEEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ACLACEIndex"),
)
if mibBuilder.loadTexts:
    gs2352ACLACEEntry.setStatus("current")


class _Gs2352ACLACEIndex_Type(Integer32):
    """Custom type gs2352ACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352ACLACEIndex_Type.__name__ = "Integer32"
_Gs2352ACLACEIndex_Object = MibTableColumn
gs2352ACLACEIndex = _Gs2352ACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 1),
    _Gs2352ACLACEIndex_Type()
)
gs2352ACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ACLACEIndex.setStatus("current")


class _Gs2352ACLACEID_Type(Integer32):
    """Custom type gs2352ACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352ACLACEID_Type.__name__ = "Integer32"
_Gs2352ACLACEID_Object = MibTableColumn
gs2352ACLACEID = _Gs2352ACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 2),
    _Gs2352ACLACEID_Type()
)
gs2352ACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEID.setStatus("current")


class _Gs2352ACLACENextID_Type(Integer32):
    """Custom type gs2352ACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2352ACLACENextID_Type.__name__ = "Integer32"
_Gs2352ACLACENextID_Object = MibTableColumn
gs2352ACLACENextID = _Gs2352ACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 3),
    _Gs2352ACLACENextID_Type()
)
gs2352ACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACENextID.setStatus("current")
_Gs2352ACLACEIngressPort_Type = DisplayString
_Gs2352ACLACEIngressPort_Object = MibTableColumn
gs2352ACLACEIngressPort = _Gs2352ACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 4),
    _Gs2352ACLACEIngressPort_Type()
)
gs2352ACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEIngressPort.setStatus("current")


class _Gs2352ACLACEPortPolicyNumber_Type(Integer32):
    """Custom type gs2352ACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2352ACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Gs2352ACLACEPortPolicyNumber_Object = MibTableColumn
gs2352ACLACEPortPolicyNumber = _Gs2352ACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 5),
    _Gs2352ACLACEPortPolicyNumber_Type()
)
gs2352ACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEPortPolicyNumber.setStatus("current")


class _Gs2352ACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type gs2352ACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2352ACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Gs2352ACLACEPortPolicyBitmask_Object = MibTableColumn
gs2352ACLACEPortPolicyBitmask = _Gs2352ACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 6),
    _Gs2352ACLACEPortPolicyBitmask_Type()
)
gs2352ACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEPortPolicyBitmask.setStatus("current")


class _Gs2352ACLACEFrameType_Type(Integer32):
    """Custom type gs2352ACLACEFrameType based on Integer32"""
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
        *(("any", 0),
          ("arp", 1),
          ("etype", 2),
          ("icmp", 3),
          ("ipv4", 4),
          ("tcp", 5),
          ("udp", 6))
    )


_Gs2352ACLACEFrameType_Type.__name__ = "Integer32"
_Gs2352ACLACEFrameType_Object = MibTableColumn
gs2352ACLACEFrameType = _Gs2352ACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 7),
    _Gs2352ACLACEFrameType_Type()
)
gs2352ACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEFrameType.setStatus("current")


class _Gs2352ACLACEAction_Type(Integer32):
    """Custom type gs2352ACLACEAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_Gs2352ACLACEAction_Type.__name__ = "Integer32"
_Gs2352ACLACEAction_Object = MibTableColumn
gs2352ACLACEAction = _Gs2352ACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 8),
    _Gs2352ACLACEAction_Type()
)
gs2352ACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEAction.setStatus("current")
_Gs2352ACLACEDenyPortRedirect_Type = DisplayString
_Gs2352ACLACEDenyPortRedirect_Object = MibTableColumn
gs2352ACLACEDenyPortRedirect = _Gs2352ACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 9),
    _Gs2352ACLACEDenyPortRedirect_Type()
)
gs2352ACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDenyPortRedirect.setStatus("current")


class _Gs2352ACLACELogging_Type(Integer32):
    """Custom type gs2352ACLACELogging based on Integer32"""
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


_Gs2352ACLACELogging_Type.__name__ = "Integer32"
_Gs2352ACLACELogging_Object = MibTableColumn
gs2352ACLACELogging = _Gs2352ACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 10),
    _Gs2352ACLACELogging_Type()
)
gs2352ACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACELogging.setStatus("current")


class _Gs2352ACLACERateLimiter_Type(Integer32):
    """Custom type gs2352ACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2352ACLACERateLimiter_Type.__name__ = "Integer32"
_Gs2352ACLACERateLimiter_Object = MibTableColumn
gs2352ACLACERateLimiter = _Gs2352ACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 12),
    _Gs2352ACLACERateLimiter_Type()
)
gs2352ACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACERateLimiter.setStatus("current")


class _Gs2352ACLACEShutdown_Type(Integer32):
    """Custom type gs2352ACLACEShutdown based on Integer32"""
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


_Gs2352ACLACEShutdown_Type.__name__ = "Integer32"
_Gs2352ACLACEShutdown_Object = MibTableColumn
gs2352ACLACEShutdown = _Gs2352ACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 13),
    _Gs2352ACLACEShutdown_Type()
)
gs2352ACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEShutdown.setStatus("current")


class _Gs2352ACLACEVLANTagPriority_Type(Integer32):
    """Custom type gs2352ACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2352ACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Gs2352ACLACEVLANTagPriority_Object = MibTableColumn
gs2352ACLACEVLANTagPriority = _Gs2352ACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 15),
    _Gs2352ACLACEVLANTagPriority_Type()
)
gs2352ACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEVLANTagPriority.setStatus("current")


class _Gs2352ACLACEVLANVID_Type(Integer32):
    """Custom type gs2352ACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2352ACLACEVLANVID_Type.__name__ = "Integer32"
_Gs2352ACLACEVLANVID_Object = MibTableColumn
gs2352ACLACEVLANVID = _Gs2352ACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 16),
    _Gs2352ACLACEVLANVID_Type()
)
gs2352ACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEVLANVID.setStatus("current")


class _Gs2352ACLACEEtherType_Type(Integer32):
    """Custom type gs2352ACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2352ACLACEEtherType_Type.__name__ = "Integer32"
_Gs2352ACLACEEtherType_Object = MibTableColumn
gs2352ACLACEEtherType = _Gs2352ACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 17),
    _Gs2352ACLACEEtherType_Type()
)
gs2352ACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEEtherType.setStatus("current")
_Gs2352ACLACESMAC_Type = DisplayString
_Gs2352ACLACESMAC_Object = MibTableColumn
gs2352ACLACESMAC = _Gs2352ACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 18),
    _Gs2352ACLACESMAC_Type()
)
gs2352ACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACESMAC.setStatus("current")


class _Gs2352ACLACEDMACType_Type(Integer32):
    """Custom type gs2352ACLACEDMACType based on Integer32"""
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
        *(("any", 0),
          ("broadcast", 1),
          ("unicast", 2),
          ("multicast", 3),
          ("macaddress", 4))
    )


_Gs2352ACLACEDMACType_Type.__name__ = "Integer32"
_Gs2352ACLACEDMACType_Object = MibTableColumn
gs2352ACLACEDMACType = _Gs2352ACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 19),
    _Gs2352ACLACEDMACType_Type()
)
gs2352ACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDMACType.setStatus("current")
_Gs2352ACLACEDMAC_Type = DisplayString
_Gs2352ACLACEDMAC_Object = MibTableColumn
gs2352ACLACEDMAC = _Gs2352ACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 20),
    _Gs2352ACLACEDMAC_Type()
)
gs2352ACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDMAC.setStatus("current")


class _Gs2352ACLACEArpOpcode_Type(Integer32):
    """Custom type gs2352ACLACEArpOpcode based on Integer32"""
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
        *(("any", 0),
          ("arp", 1),
          ("rarp", 2),
          ("other", 3),
          ("noData", 4))
    )


_Gs2352ACLACEArpOpcode_Type.__name__ = "Integer32"
_Gs2352ACLACEArpOpcode_Object = MibTableColumn
gs2352ACLACEArpOpcode = _Gs2352ACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 21),
    _Gs2352ACLACEArpOpcode_Type()
)
gs2352ACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpOpcode.setStatus("current")


class _Gs2352ACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type gs2352ACLACEArpFlagsRequestReply based on Integer32"""
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
        *(("reply", 0),
          ("request", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Gs2352ACLACEArpFlagsRequestReply_Object = MibTableColumn
gs2352ACLACEArpFlagsRequestReply = _Gs2352ACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 22),
    _Gs2352ACLACEArpFlagsRequestReply_Type()
)
gs2352ACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpFlagsRequestReply.setStatus("current")


class _Gs2352ACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type gs2352ACLACEArpFlagsArpSmac based on Integer32"""
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
        *(("notEqualSMAC", 0),
          ("equalSMAC", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Gs2352ACLACEArpFlagsArpSmac_Object = MibTableColumn
gs2352ACLACEArpFlagsArpSmac = _Gs2352ACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 23),
    _Gs2352ACLACEArpFlagsArpSmac_Type()
)
gs2352ACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpFlagsArpSmac.setStatus("current")


class _Gs2352ACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type gs2352ACLACEArpFlagsRarpDmac based on Integer32"""
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
        *(("notEqualDMAC", 0),
          ("equalDMAC", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Gs2352ACLACEArpFlagsRarpDmac_Object = MibTableColumn
gs2352ACLACEArpFlagsRarpDmac = _Gs2352ACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 24),
    _Gs2352ACLACEArpFlagsRarpDmac_Type()
)
gs2352ACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpFlagsRarpDmac.setStatus("current")


class _Gs2352ACLACEArpFlagsLength_Type(Integer32):
    """Custom type gs2352ACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352ACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Gs2352ACLACEArpFlagsLength_Object = MibTableColumn
gs2352ACLACEArpFlagsLength = _Gs2352ACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 25),
    _Gs2352ACLACEArpFlagsLength_Type()
)
gs2352ACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpFlagsLength.setStatus("current")


class _Gs2352ACLACEArpFlagsIp_Type(Integer32):
    """Custom type gs2352ACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352ACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Gs2352ACLACEArpFlagsIp_Object = MibTableColumn
gs2352ACLACEArpFlagsIp = _Gs2352ACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 26),
    _Gs2352ACLACEArpFlagsIp_Type()
)
gs2352ACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpFlagsIp.setStatus("current")


class _Gs2352ACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type gs2352ACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352ACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Gs2352ACLACEArpFlagsEthernet_Object = MibTableColumn
gs2352ACLACEArpFlagsEthernet = _Gs2352ACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 27),
    _Gs2352ACLACEArpFlagsEthernet_Type()
)
gs2352ACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEArpFlagsEthernet.setStatus("current")


class _Gs2352ACLACESIPType_Type(Integer32):
    """Custom type gs2352ACLACESIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ip", 1),
          ("noData", 2))
    )


_Gs2352ACLACESIPType_Type.__name__ = "Integer32"
_Gs2352ACLACESIPType_Object = MibTableColumn
gs2352ACLACESIPType = _Gs2352ACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 28),
    _Gs2352ACLACESIPType_Type()
)
gs2352ACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACESIPType.setStatus("current")
_Gs2352ACLACESIPIPAddress_Type = IpAddress
_Gs2352ACLACESIPIPAddress_Object = MibTableColumn
gs2352ACLACESIPIPAddress = _Gs2352ACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 29),
    _Gs2352ACLACESIPIPAddress_Type()
)
gs2352ACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACESIPIPAddress.setStatus("current")


class _Gs2352ACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type gs2352ACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Gs2352ACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2352ACLACESIPNetworkPrefix_Object = MibTableColumn
gs2352ACLACESIPNetworkPrefix = _Gs2352ACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 30),
    _Gs2352ACLACESIPNetworkPrefix_Type()
)
gs2352ACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACESIPNetworkPrefix.setStatus("current")


class _Gs2352ACLACEDIPType_Type(Integer32):
    """Custom type gs2352ACLACEDIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ip", 1),
          ("noData", 2))
    )


_Gs2352ACLACEDIPType_Type.__name__ = "Integer32"
_Gs2352ACLACEDIPType_Object = MibTableColumn
gs2352ACLACEDIPType = _Gs2352ACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 32),
    _Gs2352ACLACEDIPType_Type()
)
gs2352ACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDIPType.setStatus("current")
_Gs2352ACLACEDIPIPAddress_Type = IpAddress
_Gs2352ACLACEDIPIPAddress_Object = MibTableColumn
gs2352ACLACEDIPIPAddress = _Gs2352ACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 33),
    _Gs2352ACLACEDIPIPAddress_Type()
)
gs2352ACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDIPIPAddress.setStatus("current")


class _Gs2352ACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type gs2352ACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2352ACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2352ACLACEDIPNetworkPrefix_Object = MibTableColumn
gs2352ACLACEDIPNetworkPrefix = _Gs2352ACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 34),
    _Gs2352ACLACEDIPNetworkPrefix_Type()
)
gs2352ACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDIPNetworkPrefix.setStatus("current")


class _Gs2352ACLACEIPProtocol_Type(Integer32):
    """Custom type gs2352ACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2352ACLACEIPProtocol_Type.__name__ = "Integer32"
_Gs2352ACLACEIPProtocol_Object = MibTableColumn
gs2352ACLACEIPProtocol = _Gs2352ACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 36),
    _Gs2352ACLACEIPProtocol_Type()
)
gs2352ACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEIPProtocol.setStatus("current")


class _Gs2352ACLACEIPFlagsTTL_Type(Integer32):
    """Custom type gs2352ACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352ACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Gs2352ACLACEIPFlagsTTL_Object = MibTableColumn
gs2352ACLACEIPFlagsTTL = _Gs2352ACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 37),
    _Gs2352ACLACEIPFlagsTTL_Type()
)
gs2352ACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEIPFlagsTTL.setStatus("current")


class _Gs2352ACLACEIPFlagsOptions_Type(Integer32):
    """Custom type gs2352ACLACEIPFlagsOptions based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Gs2352ACLACEIPFlagsOptions_Object = MibTableColumn
gs2352ACLACEIPFlagsOptions = _Gs2352ACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 38),
    _Gs2352ACLACEIPFlagsOptions_Type()
)
gs2352ACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEIPFlagsOptions.setStatus("current")


class _Gs2352ACLACEIPFlagsFragment_Type(Integer32):
    """Custom type gs2352ACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352ACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Gs2352ACLACEIPFlagsFragment_Object = MibTableColumn
gs2352ACLACEIPFlagsFragment = _Gs2352ACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 39),
    _Gs2352ACLACEIPFlagsFragment_Type()
)
gs2352ACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEIPFlagsFragment.setStatus("current")


class _Gs2352ACLACEICMPType_Type(Integer32):
    """Custom type gs2352ACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2352ACLACEICMPType_Type.__name__ = "Integer32"
_Gs2352ACLACEICMPType_Object = MibTableColumn
gs2352ACLACEICMPType = _Gs2352ACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 40),
    _Gs2352ACLACEICMPType_Type()
)
gs2352ACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEICMPType.setStatus("current")


class _Gs2352ACLACEICMPCode_Type(Integer32):
    """Custom type gs2352ACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2352ACLACEICMPCode_Type.__name__ = "Integer32"
_Gs2352ACLACEICMPCode_Object = MibTableColumn
gs2352ACLACEICMPCode = _Gs2352ACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 41),
    _Gs2352ACLACEICMPCode_Type()
)
gs2352ACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEICMPCode.setStatus("current")


class _Gs2352ACLACESourcePortMin_Type(Integer32):
    """Custom type gs2352ACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2352ACLACESourcePortMin_Type.__name__ = "Integer32"
_Gs2352ACLACESourcePortMin_Object = MibTableColumn
gs2352ACLACESourcePortMin = _Gs2352ACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 42),
    _Gs2352ACLACESourcePortMin_Type()
)
gs2352ACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACESourcePortMin.setStatus("current")


class _Gs2352ACLACESourcePortMax_Type(Integer32):
    """Custom type gs2352ACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2352ACLACESourcePortMax_Type.__name__ = "Integer32"
_Gs2352ACLACESourcePortMax_Object = MibTableColumn
gs2352ACLACESourcePortMax = _Gs2352ACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 43),
    _Gs2352ACLACESourcePortMax_Type()
)
gs2352ACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACESourcePortMax.setStatus("current")


class _Gs2352ACLACEDestPortMin_Type(Integer32):
    """Custom type gs2352ACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2352ACLACEDestPortMin_Type.__name__ = "Integer32"
_Gs2352ACLACEDestPortMin_Object = MibTableColumn
gs2352ACLACEDestPortMin = _Gs2352ACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 44),
    _Gs2352ACLACEDestPortMin_Type()
)
gs2352ACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDestPortMin.setStatus("current")


class _Gs2352ACLACEDestPortMax_Type(Integer32):
    """Custom type gs2352ACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2352ACLACEDestPortMax_Type.__name__ = "Integer32"
_Gs2352ACLACEDestPortMax_Object = MibTableColumn
gs2352ACLACEDestPortMax = _Gs2352ACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 45),
    _Gs2352ACLACEDestPortMax_Type()
)
gs2352ACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEDestPortMax.setStatus("current")


class _Gs2352ACLACETCPFlagsFin_Type(Integer32):
    """Custom type gs2352ACLACETCPFlagsFin based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Gs2352ACLACETCPFlagsFin_Object = MibTableColumn
gs2352ACLACETCPFlagsFin = _Gs2352ACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 46),
    _Gs2352ACLACETCPFlagsFin_Type()
)
gs2352ACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACETCPFlagsFin.setStatus("current")


class _Gs2352ACLACETCPFlagsSyn_Type(Integer32):
    """Custom type gs2352ACLACETCPFlagsSyn based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Gs2352ACLACETCPFlagsSyn_Object = MibTableColumn
gs2352ACLACETCPFlagsSyn = _Gs2352ACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 47),
    _Gs2352ACLACETCPFlagsSyn_Type()
)
gs2352ACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACETCPFlagsSyn.setStatus("current")


class _Gs2352ACLACETCPFlagsRst_Type(Integer32):
    """Custom type gs2352ACLACETCPFlagsRst based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Gs2352ACLACETCPFlagsRst_Object = MibTableColumn
gs2352ACLACETCPFlagsRst = _Gs2352ACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 48),
    _Gs2352ACLACETCPFlagsRst_Type()
)
gs2352ACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACETCPFlagsRst.setStatus("current")


class _Gs2352ACLACETCPFlagsPsh_Type(Integer32):
    """Custom type gs2352ACLACETCPFlagsPsh based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Gs2352ACLACETCPFlagsPsh_Object = MibTableColumn
gs2352ACLACETCPFlagsPsh = _Gs2352ACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 49),
    _Gs2352ACLACETCPFlagsPsh_Type()
)
gs2352ACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACETCPFlagsPsh.setStatus("current")


class _Gs2352ACLACETCPFlagsAck_Type(Integer32):
    """Custom type gs2352ACLACETCPFlagsAck based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Gs2352ACLACETCPFlagsAck_Object = MibTableColumn
gs2352ACLACETCPFlagsAck = _Gs2352ACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 50),
    _Gs2352ACLACETCPFlagsAck_Type()
)
gs2352ACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACETCPFlagsAck.setStatus("current")


class _Gs2352ACLACETCPFlagsUrg_Type(Integer32):
    """Custom type gs2352ACLACETCPFlagsUrg based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("any", 2),
          ("noData", 3))
    )


_Gs2352ACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Gs2352ACLACETCPFlagsUrg_Object = MibTableColumn
gs2352ACLACETCPFlagsUrg = _Gs2352ACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 51),
    _Gs2352ACLACETCPFlagsUrg_Type()
)
gs2352ACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACETCPFlagsUrg.setStatus("current")


class _Gs2352ACLACERowStatus_Type(Integer32):
    """Custom type gs2352ACLACERowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352ACLACERowStatus_Type.__name__ = "Integer32"
_Gs2352ACLACERowStatus_Object = MibTableColumn
gs2352ACLACERowStatus = _Gs2352ACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 2, 1, 66),
    _Gs2352ACLACERowStatus_Type()
)
gs2352ACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACERowStatus.setStatus("current")


class _Gs2352ACLACEClear_Type(Integer32):
    """Custom type gs2352ACLACEClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("clear", 1))
    )


_Gs2352ACLACEClear_Type.__name__ = "Integer32"
_Gs2352ACLACEClear_Object = MibScalar
gs2352ACLACEClear = _Gs2352ACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 3),
    _Gs2352ACLACEClear_Type()
)
gs2352ACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEClear.setStatus("current")


class _Gs2352ACLACEMoveACEID_Type(Integer32):
    """Custom type gs2352ACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2352ACLACEMoveACEID_Type.__name__ = "Integer32"
_Gs2352ACLACEMoveACEID_Object = MibScalar
gs2352ACLACEMoveACEID = _Gs2352ACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 4),
    _Gs2352ACLACEMoveACEID_Type()
)
gs2352ACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEMoveACEID.setStatus("current")


class _Gs2352ACLACEMoveNextACEID_Type(Integer32):
    """Custom type gs2352ACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2352ACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Gs2352ACLACEMoveNextACEID_Object = MibScalar
gs2352ACLACEMoveNextACEID = _Gs2352ACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 5),
    _Gs2352ACLACEMoveNextACEID_Type()
)
gs2352ACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ACLACEMoveNextACEID.setStatus("current")
_Gs2352ACLACEStatusTable_Object = MibTable
gs2352ACLACEStatusTable = _Gs2352ACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    gs2352ACLACEStatusTable.setStatus("current")
_Gs2352ACLACEStatusEntry_Object = MibTableRow
gs2352ACLACEStatusEntry = _Gs2352ACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1)
)
gs2352ACLACEStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2352ACLACEStatusEntry.setStatus("current")


class _Gs2352ACLACEStatusIndex_Type(Integer32):
    """Custom type gs2352ACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352ACLACEStatusIndex_Type.__name__ = "Integer32"
_Gs2352ACLACEStatusIndex_Object = MibTableColumn
gs2352ACLACEStatusIndex = _Gs2352ACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 1),
    _Gs2352ACLACEStatusIndex_Type()
)
gs2352ACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusIndex.setStatus("current")
_Gs2352ACLACEStatusUser_Type = DisplayString
_Gs2352ACLACEStatusUser_Object = MibTableColumn
gs2352ACLACEStatusUser = _Gs2352ACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 2),
    _Gs2352ACLACEStatusUser_Type()
)
gs2352ACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusUser.setStatus("current")


class _Gs2352ACLACEStatusID_Type(Integer32):
    """Custom type gs2352ACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352ACLACEStatusID_Type.__name__ = "Integer32"
_Gs2352ACLACEStatusID_Object = MibTableColumn
gs2352ACLACEStatusID = _Gs2352ACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 3),
    _Gs2352ACLACEStatusID_Type()
)
gs2352ACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusID.setStatus("current")
_Gs2352ACLACEStatusIngressPort_Type = DisplayString
_Gs2352ACLACEStatusIngressPort_Object = MibTableColumn
gs2352ACLACEStatusIngressPort = _Gs2352ACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 4),
    _Gs2352ACLACEStatusIngressPort_Type()
)
gs2352ACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusIngressPort.setStatus("current")
_Gs2352ACLACEStatusFrameType_Type = DisplayString
_Gs2352ACLACEStatusFrameType_Object = MibTableColumn
gs2352ACLACEStatusFrameType = _Gs2352ACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 5),
    _Gs2352ACLACEStatusFrameType_Type()
)
gs2352ACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusFrameType.setStatus("current")
_Gs2352ACLACEStatusAction_Type = DisplayString
_Gs2352ACLACEStatusAction_Object = MibTableColumn
gs2352ACLACEStatusAction = _Gs2352ACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 6),
    _Gs2352ACLACEStatusAction_Type()
)
gs2352ACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusAction.setStatus("current")
_Gs2352ACLACEStatusRateLimiter_Type = DisplayString
_Gs2352ACLACEStatusRateLimiter_Object = MibTableColumn
gs2352ACLACEStatusRateLimiter = _Gs2352ACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 7),
    _Gs2352ACLACEStatusRateLimiter_Type()
)
gs2352ACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusRateLimiter.setStatus("current")
_Gs2352ACLACEStatusPortCopy_Type = DisplayString
_Gs2352ACLACEStatusPortCopy_Object = MibTableColumn
gs2352ACLACEStatusPortCopy = _Gs2352ACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 8),
    _Gs2352ACLACEStatusPortCopy_Type()
)
gs2352ACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusPortCopy.setStatus("current")
_Gs2352ACLACEStatusMirror_Type = DisplayString
_Gs2352ACLACEStatusMirror_Object = MibTableColumn
gs2352ACLACEStatusMirror = _Gs2352ACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 9),
    _Gs2352ACLACEStatusMirror_Type()
)
gs2352ACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusMirror.setStatus("current")
_Gs2352ACLACEStatusCPU_Type = DisplayString
_Gs2352ACLACEStatusCPU_Object = MibTableColumn
gs2352ACLACEStatusCPU = _Gs2352ACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 10),
    _Gs2352ACLACEStatusCPU_Type()
)
gs2352ACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusCPU.setStatus("current")
_Gs2352ACLACEStatusCounter_Type = Counter32
_Gs2352ACLACEStatusCounter_Object = MibTableColumn
gs2352ACLACEStatusCounter = _Gs2352ACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 11),
    _Gs2352ACLACEStatusCounter_Type()
)
gs2352ACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusCounter.setStatus("current")
_Gs2352ACLACEStatusConflict_Type = DisplayString
_Gs2352ACLACEStatusConflict_Object = MibTableColumn
gs2352ACLACEStatusConflict = _Gs2352ACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 9, 3, 6, 1, 12),
    _Gs2352ACLACEStatusConflict_Type()
)
gs2352ACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ACLACEStatusConflict.setStatus("current")
_Gs2352LoopProtection_ObjectIdentity = ObjectIdentity
gs2352LoopProtection = _Gs2352LoopProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12)
)
_Gs2352LoopProtectionConfig_ObjectIdentity = ObjectIdentity
gs2352LoopProtectionConfig = _Gs2352LoopProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1)
)


class _Gs2352LoopProtectionGlobalEnable_Type(Integer32):
    """Custom type gs2352LoopProtectionGlobalEnable based on Integer32"""
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


_Gs2352LoopProtectionGlobalEnable_Type.__name__ = "Integer32"
_Gs2352LoopProtectionGlobalEnable_Object = MibScalar
gs2352LoopProtectionGlobalEnable = _Gs2352LoopProtectionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 1),
    _Gs2352LoopProtectionGlobalEnable_Type()
)
gs2352LoopProtectionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectionGlobalEnable.setStatus("current")


class _Gs2352LoopProtectionTranmisstionTime_Type(Integer32):
    """Custom type gs2352LoopProtectionTranmisstionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2352LoopProtectionTranmisstionTime_Type.__name__ = "Integer32"
_Gs2352LoopProtectionTranmisstionTime_Object = MibScalar
gs2352LoopProtectionTranmisstionTime = _Gs2352LoopProtectionTranmisstionTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 2),
    _Gs2352LoopProtectionTranmisstionTime_Type()
)
gs2352LoopProtectionTranmisstionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectionTranmisstionTime.setStatus("current")


class _Gs2352LoopProtectionShutdownTime_Type(Integer32):
    """Custom type gs2352LoopProtectionShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Gs2352LoopProtectionShutdownTime_Type.__name__ = "Integer32"
_Gs2352LoopProtectionShutdownTime_Object = MibScalar
gs2352LoopProtectionShutdownTime = _Gs2352LoopProtectionShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 3),
    _Gs2352LoopProtectionShutdownTime_Type()
)
gs2352LoopProtectionShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectionShutdownTime.setStatus("current")
_Gs2352LoopProtectionConfigurationTable_Object = MibTable
gs2352LoopProtectionConfigurationTable = _Gs2352LoopProtectionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    gs2352LoopProtectionConfigurationTable.setStatus("current")
_Gs2352LoopProtectionConfigurationEntry_Object = MibTableRow
gs2352LoopProtectionConfigurationEntry = _Gs2352LoopProtectionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 4, 1)
)
gs2352LoopProtectionConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352LoopProtectionConfPort"),
)
if mibBuilder.loadTexts:
    gs2352LoopProtectionConfigurationEntry.setStatus("current")


class _Gs2352LoopProtectionConfPort_Type(Integer32):
    """Custom type gs2352LoopProtectionConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352LoopProtectionConfPort_Type.__name__ = "Integer32"
_Gs2352LoopProtectionConfPort_Object = MibTableColumn
gs2352LoopProtectionConfPort = _Gs2352LoopProtectionConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 4, 1, 1),
    _Gs2352LoopProtectionConfPort_Type()
)
gs2352LoopProtectionConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352LoopProtectionConfPort.setStatus("current")


class _Gs2352LoopProtectionConfEnable_Type(Integer32):
    """Custom type gs2352LoopProtectionConfEnable based on Integer32"""
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


_Gs2352LoopProtectionConfEnable_Type.__name__ = "Integer32"
_Gs2352LoopProtectionConfEnable_Object = MibTableColumn
gs2352LoopProtectionConfEnable = _Gs2352LoopProtectionConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 4, 1, 2),
    _Gs2352LoopProtectionConfEnable_Type()
)
gs2352LoopProtectionConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectionConfEnable.setStatus("current")


class _Gs2352LoopProtectionConfAction_Type(Integer32):
    """Custom type gs2352LoopProtectionConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 0),
          ("shutdownLog", 1),
          ("log", 2))
    )


_Gs2352LoopProtectionConfAction_Type.__name__ = "Integer32"
_Gs2352LoopProtectionConfAction_Object = MibTableColumn
gs2352LoopProtectionConfAction = _Gs2352LoopProtectionConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 4, 1, 3),
    _Gs2352LoopProtectionConfAction_Type()
)
gs2352LoopProtectionConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectionConfAction.setStatus("current")


class _Gs2352LoopProtectionConfTxmode_Type(Integer32):
    """Custom type gs2352LoopProtectionConfTxmode based on Integer32"""
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


_Gs2352LoopProtectionConfTxmode_Type.__name__ = "Integer32"
_Gs2352LoopProtectionConfTxmode_Object = MibTableColumn
gs2352LoopProtectionConfTxmode = _Gs2352LoopProtectionConfTxmode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 1, 4, 1, 4),
    _Gs2352LoopProtectionConfTxmode_Type()
)
gs2352LoopProtectionConfTxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoopProtectionConfTxmode.setStatus("current")
_Gs2352LoopProtectionStatusTable_Object = MibTable
gs2352LoopProtectionStatusTable = _Gs2352LoopProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2)
)
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusTable.setStatus("current")
_Gs2352LoopProtectionStatusEntry_Object = MibTableRow
gs2352LoopProtectionStatusEntry = _Gs2352LoopProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1)
)
gs2352LoopProtectionStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352LoopProtectionStatusPort"),
)
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusEntry.setStatus("current")


class _Gs2352LoopProtectionStatusPort_Type(Integer32):
    """Custom type gs2352LoopProtectionStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352LoopProtectionStatusPort_Type.__name__ = "Integer32"
_Gs2352LoopProtectionStatusPort_Object = MibTableColumn
gs2352LoopProtectionStatusPort = _Gs2352LoopProtectionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 1),
    _Gs2352LoopProtectionStatusPort_Type()
)
gs2352LoopProtectionStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusPort.setStatus("current")
_Gs2352LoopProtectionStatusAction_Type = DisplayString
_Gs2352LoopProtectionStatusAction_Object = MibTableColumn
gs2352LoopProtectionStatusAction = _Gs2352LoopProtectionStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 2),
    _Gs2352LoopProtectionStatusAction_Type()
)
gs2352LoopProtectionStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusAction.setStatus("current")
_Gs2352LoopProtectionStatusTransmit_Type = DisplayString
_Gs2352LoopProtectionStatusTransmit_Object = MibTableColumn
gs2352LoopProtectionStatusTransmit = _Gs2352LoopProtectionStatusTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 3),
    _Gs2352LoopProtectionStatusTransmit_Type()
)
gs2352LoopProtectionStatusTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusTransmit.setStatus("current")


class _Gs2352LoopProtectionStatusLoops_Type(Integer32):
    """Custom type gs2352LoopProtectionStatusLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2352LoopProtectionStatusLoops_Type.__name__ = "Integer32"
_Gs2352LoopProtectionStatusLoops_Object = MibTableColumn
gs2352LoopProtectionStatusLoops = _Gs2352LoopProtectionStatusLoops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 4),
    _Gs2352LoopProtectionStatusLoops_Type()
)
gs2352LoopProtectionStatusLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusLoops.setStatus("current")
_Gs2352LoopProtectionStatusStatus_Type = DisplayString
_Gs2352LoopProtectionStatusStatus_Object = MibTableColumn
gs2352LoopProtectionStatusStatus = _Gs2352LoopProtectionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 5),
    _Gs2352LoopProtectionStatusStatus_Type()
)
gs2352LoopProtectionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusStatus.setStatus("current")
_Gs2352LoopProtectionStatusLoop_Type = DisplayString
_Gs2352LoopProtectionStatusLoop_Object = MibTableColumn
gs2352LoopProtectionStatusLoop = _Gs2352LoopProtectionStatusLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 6),
    _Gs2352LoopProtectionStatusLoop_Type()
)
gs2352LoopProtectionStatusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusLoop.setStatus("current")
_Gs2352LoopProtectionStatusTimeLastLoop_Type = DisplayString
_Gs2352LoopProtectionStatusTimeLastLoop_Object = MibTableColumn
gs2352LoopProtectionStatusTimeLastLoop = _Gs2352LoopProtectionStatusTimeLastLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 12, 2, 1, 7),
    _Gs2352LoopProtectionStatusTimeLastLoop_Type()
)
gs2352LoopProtectionStatusTimeLastLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LoopProtectionStatusTimeLastLoop.setStatus("current")
_Gs2352Qos_ObjectIdentity = ObjectIdentity
gs2352Qos = _Gs2352Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14)
)
_Gs2352QosPortClassification_ObjectIdentity = ObjectIdentity
gs2352QosPortClassification = _Gs2352QosPortClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1)
)
_Gs2352QosPortClassificationTable_Object = MibTable
gs2352QosPortClassificationTable = _Gs2352QosPortClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    gs2352QosPortClassificationTable.setStatus("current")
_Gs2352QosPortClassificationEntry_Object = MibTableRow
gs2352QosPortClassificationEntry = _Gs2352QosPortClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1)
)
gs2352QosPortClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosPortClassificationPort"),
)
if mibBuilder.loadTexts:
    gs2352QosPortClassificationEntry.setStatus("current")


class _Gs2352QosPortClassificationPort_Type(Integer32):
    """Custom type gs2352QosPortClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosPortClassificationPort_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationPort_Object = MibTableColumn
gs2352QosPortClassificationPort = _Gs2352QosPortClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 1),
    _Gs2352QosPortClassificationPort_Type()
)
gs2352QosPortClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationPort.setStatus("current")


class _Gs2352QosPortClassificationQoSclass_Type(Integer32):
    """Custom type gs2352QosPortClassificationQoSclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352QosPortClassificationQoSclass_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationQoSclass_Object = MibTableColumn
gs2352QosPortClassificationQoSclass = _Gs2352QosPortClassificationQoSclass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 2),
    _Gs2352QosPortClassificationQoSclass_Type()
)
gs2352QosPortClassificationQoSclass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationQoSclass.setStatus("current")


class _Gs2352QosPortClassificationDPlevel_Type(Integer32):
    """Custom type gs2352QosPortClassificationDPlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352QosPortClassificationDPlevel_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationDPlevel_Object = MibTableColumn
gs2352QosPortClassificationDPlevel = _Gs2352QosPortClassificationDPlevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 3),
    _Gs2352QosPortClassificationDPlevel_Type()
)
gs2352QosPortClassificationDPlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationDPlevel.setStatus("current")


class _Gs2352QosPortClassificationPCP_Type(Integer32):
    """Custom type gs2352QosPortClassificationPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352QosPortClassificationPCP_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationPCP_Object = MibTableColumn
gs2352QosPortClassificationPCP = _Gs2352QosPortClassificationPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 4),
    _Gs2352QosPortClassificationPCP_Type()
)
gs2352QosPortClassificationPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationPCP.setStatus("current")


class _Gs2352QosPortClassificationDEI_Type(Integer32):
    """Custom type gs2352QosPortClassificationDEI based on Integer32"""
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


_Gs2352QosPortClassificationDEI_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationDEI_Object = MibTableColumn
gs2352QosPortClassificationDEI = _Gs2352QosPortClassificationDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 5),
    _Gs2352QosPortClassificationDEI_Type()
)
gs2352QosPortClassificationDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationDEI.setStatus("current")


class _Gs2352QosPortClassificationTagClass_Type(Integer32):
    """Custom type gs2352QosPortClassificationTagClass based on Integer32"""
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


_Gs2352QosPortClassificationTagClass_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationTagClass_Object = MibTableColumn
gs2352QosPortClassificationTagClass = _Gs2352QosPortClassificationTagClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 6),
    _Gs2352QosPortClassificationTagClass_Type()
)
gs2352QosPortClassificationTagClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationTagClass.setStatus("current")


class _Gs2352QosPortClassificationDSCPBased_Type(Integer32):
    """Custom type gs2352QosPortClassificationDSCPBased based on Integer32"""
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


_Gs2352QosPortClassificationDSCPBased_Type.__name__ = "Integer32"
_Gs2352QosPortClassificationDSCPBased_Object = MibTableColumn
gs2352QosPortClassificationDSCPBased = _Gs2352QosPortClassificationDSCPBased_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 1, 1, 7),
    _Gs2352QosPortClassificationDSCPBased_Type()
)
gs2352QosPortClassificationDSCPBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortClassificationDSCPBased.setStatus("current")
_Gs2352QoSIngressPortTagClassificationTable_Object = MibTable
gs2352QoSIngressPortTagClassificationTable = _Gs2352QoSIngressPortTagClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagClassificationTable.setStatus("current")
_Gs2352QoSIngressPortTagClassificationEntry_Object = MibTableRow
gs2352QoSIngressPortTagClassificationEntry = _Gs2352QoSIngressPortTagClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2, 1)
)
gs2352QoSIngressPortTagClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QoSIngressPortTagClassificationPort"),
    (0, "LANCOM-GS-2352-MIB", "gs2352QoSIngressPortTagPCP"),
    (0, "LANCOM-GS-2352-MIB", "gs2352QoSIngressPortTagDEI"),
)
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagClassificationEntry.setStatus("current")


class _Gs2352QoSIngressPortTagClassificationPort_Type(Integer32):
    """Custom type gs2352QoSIngressPortTagClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QoSIngressPortTagClassificationPort_Type.__name__ = "Integer32"
_Gs2352QoSIngressPortTagClassificationPort_Object = MibTableColumn
gs2352QoSIngressPortTagClassificationPort = _Gs2352QoSIngressPortTagClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2, 1, 1),
    _Gs2352QoSIngressPortTagClassificationPort_Type()
)
gs2352QoSIngressPortTagClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagClassificationPort.setStatus("current")


class _Gs2352QoSIngressPortTagPCP_Type(Integer32):
    """Custom type gs2352QoSIngressPortTagPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("pcp0", 1),
          ("pcp1", 2),
          ("pcp2", 3),
          ("pcp3", 4),
          ("pcp4", 5),
          ("pcp5", 6),
          ("pcp6", 7),
          ("pcp7", 8))
    )


_Gs2352QoSIngressPortTagPCP_Type.__name__ = "Integer32"
_Gs2352QoSIngressPortTagPCP_Object = MibTableColumn
gs2352QoSIngressPortTagPCP = _Gs2352QoSIngressPortTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2, 1, 2),
    _Gs2352QoSIngressPortTagPCP_Type()
)
gs2352QoSIngressPortTagPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagPCP.setStatus("current")


class _Gs2352QoSIngressPortTagDEI_Type(Integer32):
    """Custom type gs2352QoSIngressPortTagDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dei0", 1),
          ("dei1", 2))
    )


_Gs2352QoSIngressPortTagDEI_Type.__name__ = "Integer32"
_Gs2352QoSIngressPortTagDEI_Object = MibTableColumn
gs2352QoSIngressPortTagDEI = _Gs2352QoSIngressPortTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2, 1, 3),
    _Gs2352QoSIngressPortTagDEI_Type()
)
gs2352QoSIngressPortTagDEI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagDEI.setStatus("current")


class _Gs2352QoSIngressPortTagQosClass_Type(Integer32):
    """Custom type gs2352QoSIngressPortTagQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352QoSIngressPortTagQosClass_Type.__name__ = "Integer32"
_Gs2352QoSIngressPortTagQosClass_Object = MibTableColumn
gs2352QoSIngressPortTagQosClass = _Gs2352QoSIngressPortTagQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2, 1, 4),
    _Gs2352QoSIngressPortTagQosClass_Type()
)
gs2352QoSIngressPortTagQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagQosClass.setStatus("current")


class _Gs2352QoSIngressPortTagDPLevel_Type(Integer32):
    """Custom type gs2352QoSIngressPortTagDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352QoSIngressPortTagDPLevel_Type.__name__ = "Integer32"
_Gs2352QoSIngressPortTagDPLevel_Object = MibTableColumn
gs2352QoSIngressPortTagDPLevel = _Gs2352QoSIngressPortTagDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 1, 2, 1, 5),
    _Gs2352QoSIngressPortTagDPLevel_Type()
)
gs2352QoSIngressPortTagDPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QoSIngressPortTagDPLevel.setStatus("current")
_Gs2352QosPortPolicingTable_Object = MibTable
gs2352QosPortPolicingTable = _Gs2352QosPortPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gs2352QosPortPolicingTable.setStatus("current")
_Gs2352QosPortPolicingEntry_Object = MibTableRow
gs2352QosPortPolicingEntry = _Gs2352QosPortPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2, 1)
)
gs2352QosPortPolicingEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosPortPolicingPort"),
)
if mibBuilder.loadTexts:
    gs2352QosPortPolicingEntry.setStatus("current")


class _Gs2352QosPortPolicingPort_Type(Integer32):
    """Custom type gs2352QosPortPolicingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosPortPolicingPort_Type.__name__ = "Integer32"
_Gs2352QosPortPolicingPort_Object = MibTableColumn
gs2352QosPortPolicingPort = _Gs2352QosPortPolicingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2, 1, 1),
    _Gs2352QosPortPolicingPort_Type()
)
gs2352QosPortPolicingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosPortPolicingPort.setStatus("current")


class _Gs2352QosPortPolicingMode_Type(Integer32):
    """Custom type gs2352QosPortPolicingMode based on Integer32"""
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


_Gs2352QosPortPolicingMode_Type.__name__ = "Integer32"
_Gs2352QosPortPolicingMode_Object = MibTableColumn
gs2352QosPortPolicingMode = _Gs2352QosPortPolicingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2, 1, 2),
    _Gs2352QosPortPolicingMode_Type()
)
gs2352QosPortPolicingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortPolicingMode.setStatus("current")


class _Gs2352QosPortPolicingRate_Type(Integer32):
    """Custom type gs2352QosPortPolicingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2352QosPortPolicingRate_Type.__name__ = "Integer32"
_Gs2352QosPortPolicingRate_Object = MibTableColumn
gs2352QosPortPolicingRate = _Gs2352QosPortPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2, 1, 3),
    _Gs2352QosPortPolicingRate_Type()
)
gs2352QosPortPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortPolicingRate.setStatus("current")


class _Gs2352QosPortPolicingUnit_Type(Integer32):
    """Custom type gs2352QosPortPolicingUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("fps", 1))
    )


_Gs2352QosPortPolicingUnit_Type.__name__ = "Integer32"
_Gs2352QosPortPolicingUnit_Object = MibTableColumn
gs2352QosPortPolicingUnit = _Gs2352QosPortPolicingUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2, 1, 4),
    _Gs2352QosPortPolicingUnit_Type()
)
gs2352QosPortPolicingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortPolicingUnit.setStatus("current")


class _Gs2352QosPortPolicingFlowControl_Type(Integer32):
    """Custom type gs2352QosPortPolicingFlowControl based on Integer32"""
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


_Gs2352QosPortPolicingFlowControl_Type.__name__ = "Integer32"
_Gs2352QosPortPolicingFlowControl_Object = MibTableColumn
gs2352QosPortPolicingFlowControl = _Gs2352QosPortPolicingFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 2, 1, 5),
    _Gs2352QosPortPolicingFlowControl_Type()
)
gs2352QosPortPolicingFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortPolicingFlowControl.setStatus("current")
_Gs2352QosPortScheduler_ObjectIdentity = ObjectIdentity
gs2352QosPortScheduler = _Gs2352QosPortScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3)
)
_Gs2352QosPortSchedulerModeTable_Object = MibTable
gs2352QosPortSchedulerModeTable = _Gs2352QosPortSchedulerModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    gs2352QosPortSchedulerModeTable.setStatus("current")
_Gs2352QosPortSchedulerModeEntry_Object = MibTableRow
gs2352QosPortSchedulerModeEntry = _Gs2352QosPortSchedulerModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 1, 1)
)
gs2352QosPortSchedulerModeEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosSchedulerModePort"),
)
if mibBuilder.loadTexts:
    gs2352QosPortSchedulerModeEntry.setStatus("current")


class _Gs2352QosSchedulerModePort_Type(Integer32):
    """Custom type gs2352QosSchedulerModePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosSchedulerModePort_Type.__name__ = "Integer32"
_Gs2352QosSchedulerModePort_Object = MibTableColumn
gs2352QosSchedulerModePort = _Gs2352QosSchedulerModePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 1, 1, 1),
    _Gs2352QosSchedulerModePort_Type()
)
gs2352QosSchedulerModePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosSchedulerModePort.setStatus("current")


class _Gs2352QosSchedulerMode_Type(Integer32):
    """Custom type gs2352QosSchedulerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 0),
          ("weighted", 1))
    )


_Gs2352QosSchedulerMode_Type.__name__ = "Integer32"
_Gs2352QosSchedulerMode_Object = MibTableColumn
gs2352QosSchedulerMode = _Gs2352QosSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 1, 1, 2),
    _Gs2352QosSchedulerMode_Type()
)
gs2352QosSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerMode.setStatus("current")


class _Gs2352QosSchedulerShaper_Type(Integer32):
    """Custom type gs2352QosSchedulerShaper based on Integer32"""
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


_Gs2352QosSchedulerShaper_Type.__name__ = "Integer32"
_Gs2352QosSchedulerShaper_Object = MibTableColumn
gs2352QosSchedulerShaper = _Gs2352QosSchedulerShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 1, 1, 3),
    _Gs2352QosSchedulerShaper_Type()
)
gs2352QosSchedulerShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerShaper.setStatus("current")


class _Gs2352QosSchedulerShaperRate_Type(Integer32):
    """Custom type gs2352QosSchedulerShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2352QosSchedulerShaperRate_Type.__name__ = "Integer32"
_Gs2352QosSchedulerShaperRate_Object = MibTableColumn
gs2352QosSchedulerShaperRate = _Gs2352QosSchedulerShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 1, 1, 4),
    _Gs2352QosSchedulerShaperRate_Type()
)
gs2352QosSchedulerShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerShaperRate.setStatus("current")
_Gs2352QosPortSchedulerTable_Object = MibTable
gs2352QosPortSchedulerTable = _Gs2352QosPortSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352QosPortSchedulerTable.setStatus("current")
_Gs2352QosPortSchedulerEntry_Object = MibTableRow
gs2352QosPortSchedulerEntry = _Gs2352QosPortSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1)
)
gs2352QosPortSchedulerEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosSchedulerPort"),
    (0, "LANCOM-GS-2352-MIB", "gs2352QosSchedulerPortQueue"),
)
if mibBuilder.loadTexts:
    gs2352QosPortSchedulerEntry.setStatus("current")


class _Gs2352QosSchedulerPort_Type(Integer32):
    """Custom type gs2352QosSchedulerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosSchedulerPort_Type.__name__ = "Integer32"
_Gs2352QosSchedulerPort_Object = MibTableColumn
gs2352QosSchedulerPort = _Gs2352QosSchedulerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 1),
    _Gs2352QosSchedulerPort_Type()
)
gs2352QosSchedulerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPort.setStatus("current")


class _Gs2352QosSchedulerPortQueue_Type(Integer32):
    """Custom type gs2352QosSchedulerPortQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("q0", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("q5", 6),
          ("q6", 7),
          ("q7", 8))
    )


_Gs2352QosSchedulerPortQueue_Type.__name__ = "Integer32"
_Gs2352QosSchedulerPortQueue_Object = MibTableColumn
gs2352QosSchedulerPortQueue = _Gs2352QosSchedulerPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 2),
    _Gs2352QosSchedulerPortQueue_Type()
)
gs2352QosSchedulerPortQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPortQueue.setStatus("current")


class _Gs2352QosSchedulerPortQueueShaper_Type(Integer32):
    """Custom type gs2352QosSchedulerPortQueueShaper based on Integer32"""
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


_Gs2352QosSchedulerPortQueueShaper_Type.__name__ = "Integer32"
_Gs2352QosSchedulerPortQueueShaper_Object = MibTableColumn
gs2352QosSchedulerPortQueueShaper = _Gs2352QosSchedulerPortQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 3),
    _Gs2352QosSchedulerPortQueueShaper_Type()
)
gs2352QosSchedulerPortQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPortQueueShaper.setStatus("current")


class _Gs2352QosSchedulerPortQueueShaperRate_Type(Integer32):
    """Custom type gs2352QosSchedulerPortQueueShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2352QosSchedulerPortQueueShaperRate_Type.__name__ = "Integer32"
_Gs2352QosSchedulerPortQueueShaperRate_Object = MibTableColumn
gs2352QosSchedulerPortQueueShaperRate = _Gs2352QosSchedulerPortQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 4),
    _Gs2352QosSchedulerPortQueueShaperRate_Type()
)
gs2352QosSchedulerPortQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPortQueueShaperRate.setStatus("current")


class _Gs2352QosSchedulerPortQueueShaperExcess_Type(Integer32):
    """Custom type gs2352QosSchedulerPortQueueShaperExcess based on Integer32"""
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


_Gs2352QosSchedulerPortQueueShaperExcess_Type.__name__ = "Integer32"
_Gs2352QosSchedulerPortQueueShaperExcess_Object = MibTableColumn
gs2352QosSchedulerPortQueueShaperExcess = _Gs2352QosSchedulerPortQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 5),
    _Gs2352QosSchedulerPortQueueShaperExcess_Type()
)
gs2352QosSchedulerPortQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPortQueueShaperExcess.setStatus("current")


class _Gs2352QosSchedulerPortQueueSchedulerWeight_Type(Integer32):
    """Custom type gs2352QosSchedulerPortQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2352QosSchedulerPortQueueSchedulerWeight_Type.__name__ = "Integer32"
_Gs2352QosSchedulerPortQueueSchedulerWeight_Object = MibTableColumn
gs2352QosSchedulerPortQueueSchedulerWeight = _Gs2352QosSchedulerPortQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 6),
    _Gs2352QosSchedulerPortQueueSchedulerWeight_Type()
)
gs2352QosSchedulerPortQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPortQueueSchedulerWeight.setStatus("current")
_Gs2352QosSchedulerPortQueueSchedulerPercent_Type = DisplayString
_Gs2352QosSchedulerPortQueueSchedulerPercent_Object = MibTableColumn
gs2352QosSchedulerPortQueueSchedulerPercent = _Gs2352QosSchedulerPortQueueSchedulerPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 3, 2, 1, 7),
    _Gs2352QosSchedulerPortQueueSchedulerPercent_Type()
)
gs2352QosSchedulerPortQueueSchedulerPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosSchedulerPortQueueSchedulerPercent.setStatus("current")
_Gs2352QosPortEgressTagRemarking_ObjectIdentity = ObjectIdentity
gs2352QosPortEgressTagRemarking = _Gs2352QosPortEgressTagRemarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4)
)
_Gs2352QosPortEgressTagRemarkingTable_Object = MibTable
gs2352QosPortEgressTagRemarkingTable = _Gs2352QosPortEgressTagRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 1)
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingTable.setStatus("current")
_Gs2352QosPortEgressTagRemarkingEntry_Object = MibTableRow
gs2352QosPortEgressTagRemarkingEntry = _Gs2352QosPortEgressTagRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 1, 1)
)
gs2352QosPortEgressTagRemarkingEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosEgressTagRemarkingPort"),
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingEntry.setStatus("current")


class _Gs2352QosEgressTagRemarkingPort_Type(Integer32):
    """Custom type gs2352QosEgressTagRemarkingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosEgressTagRemarkingPort_Type.__name__ = "Integer32"
_Gs2352QosEgressTagRemarkingPort_Object = MibTableColumn
gs2352QosEgressTagRemarkingPort = _Gs2352QosEgressTagRemarkingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 1, 1, 1),
    _Gs2352QosEgressTagRemarkingPort_Type()
)
gs2352QosEgressTagRemarkingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosEgressTagRemarkingPort.setStatus("current")


class _Gs2352QosEgressTagRemarkingMode_Type(Integer32):
    """Custom type gs2352QosEgressTagRemarkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classified", 0),
          ("default", 1),
          ("mapped", 2))
    )


_Gs2352QosEgressTagRemarkingMode_Type.__name__ = "Integer32"
_Gs2352QosEgressTagRemarkingMode_Object = MibTableColumn
gs2352QosEgressTagRemarkingMode = _Gs2352QosEgressTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 1, 1, 2),
    _Gs2352QosEgressTagRemarkingMode_Type()
)
gs2352QosEgressTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosEgressTagRemarkingMode.setStatus("current")
_Gs2352QosPortEgressTagRemarkingDefTable_Object = MibTable
gs2352QosPortEgressTagRemarkingDefTable = _Gs2352QosPortEgressTagRemarkingDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingDefTable.setStatus("current")
_Gs2352QosPortEgressTagRemarkingDefEntry_Object = MibTableRow
gs2352QosPortEgressTagRemarkingDefEntry = _Gs2352QosPortEgressTagRemarkingDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 2, 1)
)
gs2352QosPortEgressTagRemarkingDefEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosEgressTagRemarkingDefPort"),
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingDefEntry.setStatus("current")


class _Gs2352QosEgressTagRemarkingDefPort_Type(Integer32):
    """Custom type gs2352QosEgressTagRemarkingDefPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosEgressTagRemarkingDefPort_Type.__name__ = "Integer32"
_Gs2352QosEgressTagRemarkingDefPort_Object = MibTableColumn
gs2352QosEgressTagRemarkingDefPort = _Gs2352QosEgressTagRemarkingDefPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 2, 1, 1),
    _Gs2352QosEgressTagRemarkingDefPort_Type()
)
gs2352QosEgressTagRemarkingDefPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosEgressTagRemarkingDefPort.setStatus("current")


class _Gs2352QosEgressTagRemarkingDefPCP_Type(Integer32):
    """Custom type gs2352QosEgressTagRemarkingDefPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352QosEgressTagRemarkingDefPCP_Type.__name__ = "Integer32"
_Gs2352QosEgressTagRemarkingDefPCP_Object = MibTableColumn
gs2352QosEgressTagRemarkingDefPCP = _Gs2352QosEgressTagRemarkingDefPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 2, 1, 2),
    _Gs2352QosEgressTagRemarkingDefPCP_Type()
)
gs2352QosEgressTagRemarkingDefPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosEgressTagRemarkingDefPCP.setStatus("current")


class _Gs2352QosEgressTagRemarkingDefDEI_Type(Integer32):
    """Custom type gs2352QosEgressTagRemarkingDefDEI based on Integer32"""
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


_Gs2352QosEgressTagRemarkingDefDEI_Type.__name__ = "Integer32"
_Gs2352QosEgressTagRemarkingDefDEI_Object = MibTableColumn
gs2352QosEgressTagRemarkingDefDEI = _Gs2352QosEgressTagRemarkingDefDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 2, 1, 3),
    _Gs2352QosEgressTagRemarkingDefDEI_Type()
)
gs2352QosEgressTagRemarkingDefDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosEgressTagRemarkingDefDEI.setStatus("current")
_Gs2352QosPortEgressTagRemarkingMapDPTable_Object = MibTable
gs2352QosPortEgressTagRemarkingMapDPTable = _Gs2352QosPortEgressTagRemarkingMapDPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 3)
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingMapDPTable.setStatus("current")
_Gs2352QosPortEgressTagRemarkingMapDPEntry_Object = MibTableRow
gs2352QosPortEgressTagRemarkingMapDPEntry = _Gs2352QosPortEgressTagRemarkingMapDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 3, 1)
)
gs2352QosPortEgressTagRemarkingMapDPEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosPortEgressTagRemarkingDPPort"),
    (0, "LANCOM-GS-2352-MIB", "gs2352QosPortEgressTagRemarkingClassifiedDPLevel"),
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingMapDPEntry.setStatus("current")


class _Gs2352QosPortEgressTagRemarkingDPPort_Type(Integer32):
    """Custom type gs2352QosPortEgressTagRemarkingDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosPortEgressTagRemarkingDPPort_Type.__name__ = "Integer32"
_Gs2352QosPortEgressTagRemarkingDPPort_Object = MibTableColumn
gs2352QosPortEgressTagRemarkingDPPort = _Gs2352QosPortEgressTagRemarkingDPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 3, 1, 1),
    _Gs2352QosPortEgressTagRemarkingDPPort_Type()
)
gs2352QosPortEgressTagRemarkingDPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingDPPort.setStatus("current")


class _Gs2352QosPortEgressTagRemarkingClassifiedDPLevel_Type(Integer32):
    """Custom type gs2352QosPortEgressTagRemarkingClassifiedDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2352QosPortEgressTagRemarkingClassifiedDPLevel_Type.__name__ = "Integer32"
_Gs2352QosPortEgressTagRemarkingClassifiedDPLevel_Object = MibTableColumn
gs2352QosPortEgressTagRemarkingClassifiedDPLevel = _Gs2352QosPortEgressTagRemarkingClassifiedDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 3, 1, 2),
    _Gs2352QosPortEgressTagRemarkingClassifiedDPLevel_Type()
)
gs2352QosPortEgressTagRemarkingClassifiedDPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingClassifiedDPLevel.setStatus("current")


class _Gs2352QosPortEgressTagRemarkingDPLevel_Type(Integer32):
    """Custom type gs2352QosPortEgressTagRemarkingDPLevel based on Integer32"""
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


_Gs2352QosPortEgressTagRemarkingDPLevel_Type.__name__ = "Integer32"
_Gs2352QosPortEgressTagRemarkingDPLevel_Object = MibTableColumn
gs2352QosPortEgressTagRemarkingDPLevel = _Gs2352QosPortEgressTagRemarkingDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 3, 1, 3),
    _Gs2352QosPortEgressTagRemarkingDPLevel_Type()
)
gs2352QosPortEgressTagRemarkingDPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingDPLevel.setStatus("current")
_Gs2352QosPortEgressTagRemarkingMapTable_Object = MibTable
gs2352QosPortEgressTagRemarkingMapTable = _Gs2352QosPortEgressTagRemarkingMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingMapTable.setStatus("current")
_Gs2352QosPortEgressTagRemarkingMapEntry_Object = MibTableRow
gs2352QosPortEgressTagRemarkingMapEntry = _Gs2352QosPortEgressTagRemarkingMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4, 1)
)
gs2352QosPortEgressTagRemarkingMapEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosPortEgressTagRemarkingMapPort"),
    (0, "LANCOM-GS-2352-MIB", "gs2352QosTagRemarkingQoSClass"),
    (0, "LANCOM-GS-2352-MIB", "gs2352QosTagRemarkingDPLevel"),
)
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingMapEntry.setStatus("current")


class _Gs2352QosPortEgressTagRemarkingMapPort_Type(Integer32):
    """Custom type gs2352QosPortEgressTagRemarkingMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosPortEgressTagRemarkingMapPort_Type.__name__ = "Integer32"
_Gs2352QosPortEgressTagRemarkingMapPort_Object = MibTableColumn
gs2352QosPortEgressTagRemarkingMapPort = _Gs2352QosPortEgressTagRemarkingMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4, 1, 1),
    _Gs2352QosPortEgressTagRemarkingMapPort_Type()
)
gs2352QosPortEgressTagRemarkingMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosPortEgressTagRemarkingMapPort.setStatus("current")


class _Gs2352QosTagRemarkingQoSClass_Type(Integer32):
    """Custom type gs2352QosTagRemarkingQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8))
    )


_Gs2352QosTagRemarkingQoSClass_Type.__name__ = "Integer32"
_Gs2352QosTagRemarkingQoSClass_Object = MibTableColumn
gs2352QosTagRemarkingQoSClass = _Gs2352QosTagRemarkingQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4, 1, 2),
    _Gs2352QosTagRemarkingQoSClass_Type()
)
gs2352QosTagRemarkingQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosTagRemarkingQoSClass.setStatus("current")


class _Gs2352QosTagRemarkingDPLevel_Type(Integer32):
    """Custom type gs2352QosTagRemarkingDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level0", 1),
          ("level1", 2))
    )


_Gs2352QosTagRemarkingDPLevel_Type.__name__ = "Integer32"
_Gs2352QosTagRemarkingDPLevel_Object = MibTableColumn
gs2352QosTagRemarkingDPLevel = _Gs2352QosTagRemarkingDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4, 1, 3),
    _Gs2352QosTagRemarkingDPLevel_Type()
)
gs2352QosTagRemarkingDPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosTagRemarkingDPLevel.setStatus("current")


class _Gs2352QosTagRemarkingPCP_Type(Integer32):
    """Custom type gs2352QosTagRemarkingPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352QosTagRemarkingPCP_Type.__name__ = "Integer32"
_Gs2352QosTagRemarkingPCP_Object = MibTableColumn
gs2352QosTagRemarkingPCP = _Gs2352QosTagRemarkingPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4, 1, 4),
    _Gs2352QosTagRemarkingPCP_Type()
)
gs2352QosTagRemarkingPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosTagRemarkingPCP.setStatus("current")


class _Gs2352QosTagRemarkingDEI_Type(Integer32):
    """Custom type gs2352QosTagRemarkingDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2352QosTagRemarkingDEI_Type.__name__ = "Integer32"
_Gs2352QosTagRemarkingDEI_Object = MibTableColumn
gs2352QosTagRemarkingDEI = _Gs2352QosTagRemarkingDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 4, 4, 1, 5),
    _Gs2352QosTagRemarkingDEI_Type()
)
gs2352QosTagRemarkingDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosTagRemarkingDEI.setStatus("current")
_Gs2352QosPortDSCPTable_Object = MibTable
gs2352QosPortDSCPTable = _Gs2352QosPortDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 5)
)
if mibBuilder.loadTexts:
    gs2352QosPortDSCPTable.setStatus("current")
_Gs2352QosPortDSCPEntry_Object = MibTableRow
gs2352QosPortDSCPEntry = _Gs2352QosPortDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 5, 1)
)
gs2352QosPortDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosPortDSCPPort"),
)
if mibBuilder.loadTexts:
    gs2352QosPortDSCPEntry.setStatus("current")


class _Gs2352QosPortDSCPPort_Type(Integer32):
    """Custom type gs2352QosPortDSCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosPortDSCPPort_Type.__name__ = "Integer32"
_Gs2352QosPortDSCPPort_Object = MibTableColumn
gs2352QosPortDSCPPort = _Gs2352QosPortDSCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 5, 1, 1),
    _Gs2352QosPortDSCPPort_Type()
)
gs2352QosPortDSCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosPortDSCPPort.setStatus("current")


class _Gs2352QosPortDSCPIngressTranslate_Type(Integer32):
    """Custom type gs2352QosPortDSCPIngressTranslate based on Integer32"""
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


_Gs2352QosPortDSCPIngressTranslate_Type.__name__ = "Integer32"
_Gs2352QosPortDSCPIngressTranslate_Object = MibTableColumn
gs2352QosPortDSCPIngressTranslate = _Gs2352QosPortDSCPIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 5, 1, 2),
    _Gs2352QosPortDSCPIngressTranslate_Type()
)
gs2352QosPortDSCPIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortDSCPIngressTranslate.setStatus("current")


class _Gs2352QosPortDSCPIngressClassify_Type(Integer32):
    """Custom type gs2352QosPortDSCPIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352QosPortDSCPIngressClassify_Type.__name__ = "Integer32"
_Gs2352QosPortDSCPIngressClassify_Object = MibTableColumn
gs2352QosPortDSCPIngressClassify = _Gs2352QosPortDSCPIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 5, 1, 3),
    _Gs2352QosPortDSCPIngressClassify_Type()
)
gs2352QosPortDSCPIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortDSCPIngressClassify.setStatus("current")


class _Gs2352QosPortDSCPEgressRewrite_Type(Integer32):
    """Custom type gs2352QosPortDSCPEgressRewrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("remap", 2))
    )


_Gs2352QosPortDSCPEgressRewrite_Type.__name__ = "Integer32"
_Gs2352QosPortDSCPEgressRewrite_Object = MibTableColumn
gs2352QosPortDSCPEgressRewrite = _Gs2352QosPortDSCPEgressRewrite_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 5, 1, 4),
    _Gs2352QosPortDSCPEgressRewrite_Type()
)
gs2352QosPortDSCPEgressRewrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPortDSCPEgressRewrite.setStatus("current")
_Gs2352QosDSCPTable_Object = MibTable
gs2352QosDSCPTable = _Gs2352QosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6)
)
if mibBuilder.loadTexts:
    gs2352QosDSCPTable.setStatus("current")
_Gs2352QosDSCPEntry_Object = MibTableRow
gs2352QosDSCPEntry = _Gs2352QosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6, 1)
)
gs2352QosDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosDSCPList"),
)
if mibBuilder.loadTexts:
    gs2352QosDSCPEntry.setStatus("current")


class _Gs2352QosDSCPList_Type(Integer32):
    """Custom type gs2352QosDSCPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2352QosDSCPList_Type.__name__ = "Integer32"
_Gs2352QosDSCPList_Object = MibTableColumn
gs2352QosDSCPList = _Gs2352QosDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6, 1, 1),
    _Gs2352QosDSCPList_Type()
)
gs2352QosDSCPList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosDSCPList.setStatus("current")
_Gs2352QosDSCP_Type = DisplayString
_Gs2352QosDSCP_Object = MibTableColumn
gs2352QosDSCP = _Gs2352QosDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6, 1, 2),
    _Gs2352QosDSCP_Type()
)
gs2352QosDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosDSCP.setStatus("current")


class _Gs2352QosDSCPTrust_Type(Integer32):
    """Custom type gs2352QosDSCPTrust based on Integer32"""
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


_Gs2352QosDSCPTrust_Type.__name__ = "Integer32"
_Gs2352QosDSCPTrust_Object = MibTableColumn
gs2352QosDSCPTrust = _Gs2352QosDSCPTrust_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6, 1, 3),
    _Gs2352QosDSCPTrust_Type()
)
gs2352QosDSCPTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPTrust.setStatus("current")


class _Gs2352QosDSCPQosClass_Type(Integer32):
    """Custom type gs2352QosDSCPQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2352QosDSCPQosClass_Type.__name__ = "Integer32"
_Gs2352QosDSCPQosClass_Object = MibTableColumn
gs2352QosDSCPQosClass = _Gs2352QosDSCPQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6, 1, 4),
    _Gs2352QosDSCPQosClass_Type()
)
gs2352QosDSCPQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPQosClass.setStatus("current")


class _Gs2352QosDSCPDPL_Type(Integer32):
    """Custom type gs2352QosDSCPDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2352QosDSCPDPL_Type.__name__ = "Integer32"
_Gs2352QosDSCPDPL_Object = MibTableColumn
gs2352QosDSCPDPL = _Gs2352QosDSCPDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 6, 1, 5),
    _Gs2352QosDSCPDPL_Type()
)
gs2352QosDSCPDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPDPL.setStatus("current")
_Gs2352QosDSCPTranslationTable_Object = MibTable
gs2352QosDSCPTranslationTable = _Gs2352QosDSCPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7)
)
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationTable.setStatus("current")
_Gs2352QosDSCPTranslationEntry_Object = MibTableRow
gs2352QosDSCPTranslationEntry = _Gs2352QosDSCPTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7, 1)
)
gs2352QosDSCPTranslationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosDSCPTranslationList"),
)
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationEntry.setStatus("current")


class _Gs2352QosDSCPTranslationList_Type(Integer32):
    """Custom type gs2352QosDSCPTranslationList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2352QosDSCPTranslationList_Type.__name__ = "Integer32"
_Gs2352QosDSCPTranslationList_Object = MibTableColumn
gs2352QosDSCPTranslationList = _Gs2352QosDSCPTranslationList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7, 1, 1),
    _Gs2352QosDSCPTranslationList_Type()
)
gs2352QosDSCPTranslationList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationList.setStatus("current")
_Gs2352QosDSCPTranslationDSCPBasedId_Type = DisplayString
_Gs2352QosDSCPTranslationDSCPBasedId_Object = MibTableColumn
gs2352QosDSCPTranslationDSCPBasedId = _Gs2352QosDSCPTranslationDSCPBasedId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7, 1, 2),
    _Gs2352QosDSCPTranslationDSCPBasedId_Type()
)
gs2352QosDSCPTranslationDSCPBasedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationDSCPBasedId.setStatus("current")


class _Gs2352QosDSCPTranslationIngressTranslate_Type(Integer32):
    """Custom type gs2352QosDSCPTranslationIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2352QosDSCPTranslationIngressTranslate_Type.__name__ = "Integer32"
_Gs2352QosDSCPTranslationIngressTranslate_Object = MibTableColumn
gs2352QosDSCPTranslationIngressTranslate = _Gs2352QosDSCPTranslationIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7, 1, 3),
    _Gs2352QosDSCPTranslationIngressTranslate_Type()
)
gs2352QosDSCPTranslationIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationIngressTranslate.setStatus("current")


class _Gs2352QosDSCPTranslationIngressClassify_Type(Integer32):
    """Custom type gs2352QosDSCPTranslationIngressClassify based on Integer32"""
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


_Gs2352QosDSCPTranslationIngressClassify_Type.__name__ = "Integer32"
_Gs2352QosDSCPTranslationIngressClassify_Object = MibTableColumn
gs2352QosDSCPTranslationIngressClassify = _Gs2352QosDSCPTranslationIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7, 1, 4),
    _Gs2352QosDSCPTranslationIngressClassify_Type()
)
gs2352QosDSCPTranslationIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationIngressClassify.setStatus("current")


class _Gs2352QosDSCPTranslationEgressRemap_Type(Integer32):
    """Custom type gs2352QosDSCPTranslationEgressRemap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2352QosDSCPTranslationEgressRemap_Type.__name__ = "Integer32"
_Gs2352QosDSCPTranslationEgressRemap_Object = MibTableColumn
gs2352QosDSCPTranslationEgressRemap = _Gs2352QosDSCPTranslationEgressRemap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 7, 1, 5),
    _Gs2352QosDSCPTranslationEgressRemap_Type()
)
gs2352QosDSCPTranslationEgressRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPTranslationEgressRemap.setStatus("current")
_Gs2352QosDSCPClassificationTable_Object = MibTable
gs2352QosDSCPClassificationTable = _Gs2352QosDSCPClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 8)
)
if mibBuilder.loadTexts:
    gs2352QosDSCPClassificationTable.setStatus("current")
_Gs2352QosDSCPClassificationEntry_Object = MibTableRow
gs2352QosDSCPClassificationEntry = _Gs2352QosDSCPClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 8, 1)
)
gs2352QosDSCPClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosDSCPClassificationQoSClass"),
)
if mibBuilder.loadTexts:
    gs2352QosDSCPClassificationEntry.setStatus("current")


class _Gs2352QosDSCPClassificationQoSClass_Type(Integer32):
    """Custom type gs2352QosDSCPClassificationQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8))
    )


_Gs2352QosDSCPClassificationQoSClass_Type.__name__ = "Integer32"
_Gs2352QosDSCPClassificationQoSClass_Object = MibTableColumn
gs2352QosDSCPClassificationQoSClass = _Gs2352QosDSCPClassificationQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 8, 1, 1),
    _Gs2352QosDSCPClassificationQoSClass_Type()
)
gs2352QosDSCPClassificationQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosDSCPClassificationQoSClass.setStatus("current")


class _Gs2352QosDSCPClassificationDSCP_Type(Integer32):
    """Custom type gs2352QosDSCPClassificationDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2352QosDSCPClassificationDSCP_Type.__name__ = "Integer32"
_Gs2352QosDSCPClassificationDSCP_Object = MibTableColumn
gs2352QosDSCPClassificationDSCP = _Gs2352QosDSCPClassificationDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 8, 1, 3),
    _Gs2352QosDSCPClassificationDSCP_Type()
)
gs2352QosDSCPClassificationDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDSCPClassificationDSCP.setStatus("current")
_Gs2352QosControlList_ObjectIdentity = ObjectIdentity
gs2352QosControlList = _Gs2352QosControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9)
)


class _Gs2352QosQceCreate_Type(Integer32):
    """Custom type gs2352QosQceCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352QosQceCreate_Type.__name__ = "Integer32"
_Gs2352QosQceCreate_Object = MibScalar
gs2352QosQceCreate = _Gs2352QosQceCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 1),
    _Gs2352QosQceCreate_Type()
)
gs2352QosQceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceCreate.setStatus("current")
_Gs2352QosQceTable_Object = MibTable
gs2352QosQceTable = _Gs2352QosQceTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2)
)
if mibBuilder.loadTexts:
    gs2352QosQceTable.setStatus("current")
_Gs2352QosQceEntry_Object = MibTableRow
gs2352QosQceEntry = _Gs2352QosQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1)
)
gs2352QosQceEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosQceIndex"),
)
if mibBuilder.loadTexts:
    gs2352QosQceEntry.setStatus("current")


class _Gs2352QosQceIndex_Type(Integer32):
    """Custom type gs2352QosQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352QosQceIndex_Type.__name__ = "Integer32"
_Gs2352QosQceIndex_Object = MibTableColumn
gs2352QosQceIndex = _Gs2352QosQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 1),
    _Gs2352QosQceIndex_Type()
)
gs2352QosQceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosQceIndex.setStatus("current")


class _Gs2352QosQceID_Type(Integer32):
    """Custom type gs2352QosQceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352QosQceID_Type.__name__ = "Integer32"
_Gs2352QosQceID_Object = MibTableColumn
gs2352QosQceID = _Gs2352QosQceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 2),
    _Gs2352QosQceID_Type()
)
gs2352QosQceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceID.setStatus("current")


class _Gs2352QosQceNextID_Type(Integer32):
    """Custom type gs2352QosQceNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352QosQceNextID_Type.__name__ = "Integer32"
_Gs2352QosQceNextID_Object = MibTableColumn
gs2352QosQceNextID = _Gs2352QosQceNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 3),
    _Gs2352QosQceNextID_Type()
)
gs2352QosQceNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceNextID.setStatus("current")
_Gs2352QosQcePortMembers_Type = DisplayString
_Gs2352QosQcePortMembers_Object = MibTableColumn
gs2352QosQcePortMembers = _Gs2352QosQcePortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 4),
    _Gs2352QosQcePortMembers_Type()
)
gs2352QosQcePortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQcePortMembers.setStatus("current")
_Gs2352QosQceTag_Type = DisplayString
_Gs2352QosQceTag_Object = MibTableColumn
gs2352QosQceTag = _Gs2352QosQceTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 5),
    _Gs2352QosQceTag_Type()
)
gs2352QosQceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceTag.setStatus("current")
_Gs2352QosQceVID_Type = DisplayString
_Gs2352QosQceVID_Object = MibTableColumn
gs2352QosQceVID = _Gs2352QosQceVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 6),
    _Gs2352QosQceVID_Type()
)
gs2352QosQceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceVID.setStatus("current")
_Gs2352QosPCP_Type = DisplayString
_Gs2352QosPCP_Object = MibTableColumn
gs2352QosPCP = _Gs2352QosPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 7),
    _Gs2352QosPCP_Type()
)
gs2352QosPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosPCP.setStatus("current")
_Gs2352QosDEI_Type = DisplayString
_Gs2352QosDEI_Object = MibTableColumn
gs2352QosDEI = _Gs2352QosDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 8),
    _Gs2352QosDEI_Type()
)
gs2352QosDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDEI.setStatus("current")
_Gs2352QosSMAC_Type = DisplayString
_Gs2352QosSMAC_Object = MibTableColumn
gs2352QosSMAC = _Gs2352QosSMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 9),
    _Gs2352QosSMAC_Type()
)
gs2352QosSMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSMAC.setStatus("current")
_Gs2352QosDMACType_Type = DisplayString
_Gs2352QosDMACType_Object = MibTableColumn
gs2352QosDMACType = _Gs2352QosDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 10),
    _Gs2352QosDMACType_Type()
)
gs2352QosDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosDMACType.setStatus("current")


class _Gs2352QosFrameType_Type(Integer32):
    """Custom type gs2352QosFrameType based on Integer32"""
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
        *(("any", 1),
          ("ethernet", 2),
          ("llc", 3),
          ("snap", 4),
          ("ipv4", 5),
          ("ipv6", 6))
    )


_Gs2352QosFrameType_Type.__name__ = "Integer32"
_Gs2352QosFrameType_Object = MibTableColumn
gs2352QosFrameType = _Gs2352QosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 11),
    _Gs2352QosFrameType_Type()
)
gs2352QosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosFrameType.setStatus("current")
_Gs2352QosMacEtherType_Type = DisplayString
_Gs2352QosMacEtherType_Object = MibTableColumn
gs2352QosMacEtherType = _Gs2352QosMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 12),
    _Gs2352QosMacEtherType_Type()
)
gs2352QosMacEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosMacEtherType.setStatus("current")
_Gs2352QosLLCSSAPAddr_Type = DisplayString
_Gs2352QosLLCSSAPAddr_Object = MibTableColumn
gs2352QosLLCSSAPAddr = _Gs2352QosLLCSSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 13),
    _Gs2352QosLLCSSAPAddr_Type()
)
gs2352QosLLCSSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosLLCSSAPAddr.setStatus("current")
_Gs2352QosLLCDSAPAddr_Type = DisplayString
_Gs2352QosLLCDSAPAddr_Object = MibTableColumn
gs2352QosLLCDSAPAddr = _Gs2352QosLLCDSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 14),
    _Gs2352QosLLCDSAPAddr_Type()
)
gs2352QosLLCDSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosLLCDSAPAddr.setStatus("current")
_Gs2352QosLLCControl_Type = DisplayString
_Gs2352QosLLCControl_Object = MibTableColumn
gs2352QosLLCControl = _Gs2352QosLLCControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 15),
    _Gs2352QosLLCControl_Type()
)
gs2352QosLLCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosLLCControl.setStatus("current")
_Gs2352QosSNAPPID_Type = DisplayString
_Gs2352QosSNAPPID_Object = MibTableColumn
gs2352QosSNAPPID = _Gs2352QosSNAPPID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 16),
    _Gs2352QosSNAPPID_Type()
)
gs2352QosSNAPPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosSNAPPID.setStatus("current")
_Gs2352QosIpv4Protocol_Type = DisplayString
_Gs2352QosIpv4Protocol_Object = MibTableColumn
gs2352QosIpv4Protocol = _Gs2352QosIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 17),
    _Gs2352QosIpv4Protocol_Type()
)
gs2352QosIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4Protocol.setStatus("current")


class _Gs2352QosIpv4ProtocolValue_Type(Integer32):
    """Custom type gs2352QosIpv4ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2352QosIpv4ProtocolValue_Type.__name__ = "Integer32"
_Gs2352QosIpv4ProtocolValue_Object = MibTableColumn
gs2352QosIpv4ProtocolValue = _Gs2352QosIpv4ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 18),
    _Gs2352QosIpv4ProtocolValue_Type()
)
gs2352QosIpv4ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4ProtocolValue.setStatus("current")
_Gs2352QosIpv4ProtocolUDPSport_Type = DisplayString
_Gs2352QosIpv4ProtocolUDPSport_Object = MibTableColumn
gs2352QosIpv4ProtocolUDPSport = _Gs2352QosIpv4ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 19),
    _Gs2352QosIpv4ProtocolUDPSport_Type()
)
gs2352QosIpv4ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4ProtocolUDPSport.setStatus("current")
_Gs2352QosIpv4ProtocolUDPDport_Type = DisplayString
_Gs2352QosIpv4ProtocolUDPDport_Object = MibTableColumn
gs2352QosIpv4ProtocolUDPDport = _Gs2352QosIpv4ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 20),
    _Gs2352QosIpv4ProtocolUDPDport_Type()
)
gs2352QosIpv4ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4ProtocolUDPDport.setStatus("current")
_Gs2352QosIpv4ProtocolTCPSport_Type = DisplayString
_Gs2352QosIpv4ProtocolTCPSport_Object = MibTableColumn
gs2352QosIpv4ProtocolTCPSport = _Gs2352QosIpv4ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 21),
    _Gs2352QosIpv4ProtocolTCPSport_Type()
)
gs2352QosIpv4ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4ProtocolTCPSport.setStatus("current")
_Gs2352QosIpv4ProtocolTCPDport_Type = DisplayString
_Gs2352QosIpv4ProtocolTCPDport_Object = MibTableColumn
gs2352QosIpv4ProtocolTCPDport = _Gs2352QosIpv4ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 22),
    _Gs2352QosIpv4ProtocolTCPDport_Type()
)
gs2352QosIpv4ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4ProtocolTCPDport.setStatus("current")
_Gs2352QosIpv4SourceIp_Type = DisplayString
_Gs2352QosIpv4SourceIp_Object = MibTableColumn
gs2352QosIpv4SourceIp = _Gs2352QosIpv4SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 23),
    _Gs2352QosIpv4SourceIp_Type()
)
gs2352QosIpv4SourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4SourceIp.setStatus("current")
_Gs2352QosIpv4SourceMask_Type = DisplayString
_Gs2352QosIpv4SourceMask_Object = MibTableColumn
gs2352QosIpv4SourceMask = _Gs2352QosIpv4SourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 24),
    _Gs2352QosIpv4SourceMask_Type()
)
gs2352QosIpv4SourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4SourceMask.setStatus("current")


class _Gs2352QosIpv4IPFragment_Type(Integer32):
    """Custom type gs2352QosIpv4IPFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("no", 1),
          ("yes", 2))
    )


_Gs2352QosIpv4IPFragment_Type.__name__ = "Integer32"
_Gs2352QosIpv4IPFragment_Object = MibTableColumn
gs2352QosIpv4IPFragment = _Gs2352QosIpv4IPFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 25),
    _Gs2352QosIpv4IPFragment_Type()
)
gs2352QosIpv4IPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4IPFragment.setStatus("current")
_Gs2352QosIpv4DSCP_Type = DisplayString
_Gs2352QosIpv4DSCP_Object = MibTableColumn
gs2352QosIpv4DSCP = _Gs2352QosIpv4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 26),
    _Gs2352QosIpv4DSCP_Type()
)
gs2352QosIpv4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv4DSCP.setStatus("current")
_Gs2352QosIpv6Protocol_Type = DisplayString
_Gs2352QosIpv6Protocol_Object = MibTableColumn
gs2352QosIpv6Protocol = _Gs2352QosIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 27),
    _Gs2352QosIpv6Protocol_Type()
)
gs2352QosIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6Protocol.setStatus("current")


class _Gs2352QosIpv6ProtocolValue_Type(Integer32):
    """Custom type gs2352QosIpv6ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2352QosIpv6ProtocolValue_Type.__name__ = "Integer32"
_Gs2352QosIpv6ProtocolValue_Object = MibTableColumn
gs2352QosIpv6ProtocolValue = _Gs2352QosIpv6ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 28),
    _Gs2352QosIpv6ProtocolValue_Type()
)
gs2352QosIpv6ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6ProtocolValue.setStatus("current")
_Gs2352QosIpv6ProtocolUDPSport_Type = DisplayString
_Gs2352QosIpv6ProtocolUDPSport_Object = MibTableColumn
gs2352QosIpv6ProtocolUDPSport = _Gs2352QosIpv6ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 29),
    _Gs2352QosIpv6ProtocolUDPSport_Type()
)
gs2352QosIpv6ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6ProtocolUDPSport.setStatus("current")
_Gs2352QosIpv6ProtocolUDPDport_Type = DisplayString
_Gs2352QosIpv6ProtocolUDPDport_Object = MibTableColumn
gs2352QosIpv6ProtocolUDPDport = _Gs2352QosIpv6ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 30),
    _Gs2352QosIpv6ProtocolUDPDport_Type()
)
gs2352QosIpv6ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6ProtocolUDPDport.setStatus("current")
_Gs2352QosIpv6ProtocolTCPSport_Type = DisplayString
_Gs2352QosIpv6ProtocolTCPSport_Object = MibTableColumn
gs2352QosIpv6ProtocolTCPSport = _Gs2352QosIpv6ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 31),
    _Gs2352QosIpv6ProtocolTCPSport_Type()
)
gs2352QosIpv6ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6ProtocolTCPSport.setStatus("current")
_Gs2352QosIpv6ProtocolTCPDport_Type = DisplayString
_Gs2352QosIpv6ProtocolTCPDport_Object = MibTableColumn
gs2352QosIpv6ProtocolTCPDport = _Gs2352QosIpv6ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 32),
    _Gs2352QosIpv6ProtocolTCPDport_Type()
)
gs2352QosIpv6ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6ProtocolTCPDport.setStatus("current")
_Gs2352QosIpv6SourceIp_Type = DisplayString
_Gs2352QosIpv6SourceIp_Object = MibTableColumn
gs2352QosIpv6SourceIp = _Gs2352QosIpv6SourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 33),
    _Gs2352QosIpv6SourceIp_Type()
)
gs2352QosIpv6SourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6SourceIp.setStatus("current")
_Gs2352QosIpv6SourceMask_Type = DisplayString
_Gs2352QosIpv6SourceMask_Object = MibTableColumn
gs2352QosIpv6SourceMask = _Gs2352QosIpv6SourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 34),
    _Gs2352QosIpv6SourceMask_Type()
)
gs2352QosIpv6SourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6SourceMask.setStatus("current")
_Gs2352QosIpv6DSCP_Type = DisplayString
_Gs2352QosIpv6DSCP_Object = MibTableColumn
gs2352QosIpv6DSCP = _Gs2352QosIpv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 35),
    _Gs2352QosIpv6DSCP_Type()
)
gs2352QosIpv6DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosIpv6DSCP.setStatus("current")


class _Gs2352QosActionClass_Type(Integer32):
    """Custom type gs2352QosActionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2352QosActionClass_Type.__name__ = "Integer32"
_Gs2352QosActionClass_Object = MibTableColumn
gs2352QosActionClass = _Gs2352QosActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 36),
    _Gs2352QosActionClass_Type()
)
gs2352QosActionClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosActionClass.setStatus("current")


class _Gs2352QosActionDPL_Type(Integer32):
    """Custom type gs2352QosActionDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2352QosActionDPL_Type.__name__ = "Integer32"
_Gs2352QosActionDPL_Object = MibTableColumn
gs2352QosActionDPL = _Gs2352QosActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 37),
    _Gs2352QosActionDPL_Type()
)
gs2352QosActionDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosActionDPL.setStatus("current")


class _Gs2352QosActionDSCP_Type(Integer32):
    """Custom type gs2352QosActionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2352QosActionDSCP_Type.__name__ = "Integer32"
_Gs2352QosActionDSCP_Object = MibTableColumn
gs2352QosActionDSCP = _Gs2352QosActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 38),
    _Gs2352QosActionDSCP_Type()
)
gs2352QosActionDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosActionDSCP.setStatus("current")


class _Gs2352QosQceRowStatus_Type(Integer32):
    """Custom type gs2352QosQceRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4))
    )


_Gs2352QosQceRowStatus_Type.__name__ = "Integer32"
_Gs2352QosQceRowStatus_Object = MibTableColumn
gs2352QosQceRowStatus = _Gs2352QosQceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 2, 1, 39),
    _Gs2352QosQceRowStatus_Type()
)
gs2352QosQceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceRowStatus.setStatus("current")


class _Gs2352QosQceMoveID_Type(Integer32):
    """Custom type gs2352QosQceMoveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2352QosQceMoveID_Type.__name__ = "Integer32"
_Gs2352QosQceMoveID_Object = MibScalar
gs2352QosQceMoveID = _Gs2352QosQceMoveID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 3),
    _Gs2352QosQceMoveID_Type()
)
gs2352QosQceMoveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceMoveID.setStatus("current")


class _Gs2352QosQceMoveNextID_Type(Integer32):
    """Custom type gs2352QosQceMoveNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2352QosQceMoveNextID_Type.__name__ = "Integer32"
_Gs2352QosQceMoveNextID_Object = MibScalar
gs2352QosQceMoveNextID = _Gs2352QosQceMoveNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 9, 4),
    _Gs2352QosQceMoveNextID_Type()
)
gs2352QosQceMoveNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosQceMoveNextID.setStatus("current")
_Gs2352QosQCLStatusTable_Object = MibTable
gs2352QosQCLStatusTable = _Gs2352QosQCLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10)
)
if mibBuilder.loadTexts:
    gs2352QosQCLStatusTable.setStatus("current")
_Gs2352QosQCLStatusEntry_Object = MibTableRow
gs2352QosQCLStatusEntry = _Gs2352QosQCLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1)
)
gs2352QosQCLStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosQCLStatusList"),
)
if mibBuilder.loadTexts:
    gs2352QosQCLStatusEntry.setStatus("current")


class _Gs2352QosQCLStatusList_Type(Integer32):
    """Custom type gs2352QosQCLStatusList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosQCLStatusList_Type.__name__ = "Integer32"
_Gs2352QosQCLStatusList_Object = MibTableColumn
gs2352QosQCLStatusList = _Gs2352QosQCLStatusList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 1),
    _Gs2352QosQCLStatusList_Type()
)
gs2352QosQCLStatusList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusList.setStatus("current")
_Gs2352QosQCLStatusUser_Type = DisplayString
_Gs2352QosQCLStatusUser_Object = MibTableColumn
gs2352QosQCLStatusUser = _Gs2352QosQCLStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 2),
    _Gs2352QosQCLStatusUser_Type()
)
gs2352QosQCLStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusUser.setStatus("current")
_Gs2352QosQCLStatusQCEId_Type = DisplayString
_Gs2352QosQCLStatusQCEId_Object = MibTableColumn
gs2352QosQCLStatusQCEId = _Gs2352QosQCLStatusQCEId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 3),
    _Gs2352QosQCLStatusQCEId_Type()
)
gs2352QosQCLStatusQCEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusQCEId.setStatus("current")
_Gs2352QosQCLStatusFrameType_Type = DisplayString
_Gs2352QosQCLStatusFrameType_Object = MibTableColumn
gs2352QosQCLStatusFrameType = _Gs2352QosQCLStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 4),
    _Gs2352QosQCLStatusFrameType_Type()
)
gs2352QosQCLStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusFrameType.setStatus("current")
_Gs2352QosQCLStatusPortlist_Type = DisplayString
_Gs2352QosQCLStatusPortlist_Object = MibTableColumn
gs2352QosQCLStatusPortlist = _Gs2352QosQCLStatusPortlist_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 5),
    _Gs2352QosQCLStatusPortlist_Type()
)
gs2352QosQCLStatusPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusPortlist.setStatus("current")
_Gs2352QosQCLStatusActionClass_Type = DisplayString
_Gs2352QosQCLStatusActionClass_Object = MibTableColumn
gs2352QosQCLStatusActionClass = _Gs2352QosQCLStatusActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 6),
    _Gs2352QosQCLStatusActionClass_Type()
)
gs2352QosQCLStatusActionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusActionClass.setStatus("current")
_Gs2352QosQCLStatusActionDPL_Type = DisplayString
_Gs2352QosQCLStatusActionDPL_Object = MibTableColumn
gs2352QosQCLStatusActionDPL = _Gs2352QosQCLStatusActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 7),
    _Gs2352QosQCLStatusActionDPL_Type()
)
gs2352QosQCLStatusActionDPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusActionDPL.setStatus("current")
_Gs2352QosQCLStatusActionDSCP_Type = DisplayString
_Gs2352QosQCLStatusActionDSCP_Object = MibTableColumn
gs2352QosQCLStatusActionDSCP = _Gs2352QosQCLStatusActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 8),
    _Gs2352QosQCLStatusActionDSCP_Type()
)
gs2352QosQCLStatusActionDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusActionDSCP.setStatus("current")
_Gs2352QosQCLStatusActionConflict_Type = DisplayString
_Gs2352QosQCLStatusActionConflict_Object = MibTableColumn
gs2352QosQCLStatusActionConflict = _Gs2352QosQCLStatusActionConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 10, 1, 9),
    _Gs2352QosQCLStatusActionConflict_Type()
)
gs2352QosQCLStatusActionConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352QosQCLStatusActionConflict.setStatus("current")
_Gs2352QosStormControl_ObjectIdentity = ObjectIdentity
gs2352QosStormControl = _Gs2352QosStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11)
)
_Gs2352QosStormControlTable_Object = MibTable
gs2352QosStormControlTable = _Gs2352QosStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1)
)
if mibBuilder.loadTexts:
    gs2352QosStormControlTable.setStatus("current")
_Gs2352QosStormControlEntry_Object = MibTableRow
gs2352QosStormControlEntry = _Gs2352QosStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1)
)
gs2352QosStormControlEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosStormControlPort"),
)
if mibBuilder.loadTexts:
    gs2352QosStormControlEntry.setStatus("current")


class _Gs2352QosStormControlPort_Type(Integer32):
    """Custom type gs2352QosStormControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352QosStormControlPort_Type.__name__ = "Integer32"
_Gs2352QosStormControlPort_Object = MibTableColumn
gs2352QosStormControlPort = _Gs2352QosStormControlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 1),
    _Gs2352QosStormControlPort_Type()
)
gs2352QosStormControlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosStormControlPort.setStatus("current")


class _Gs2352QosStormControlUnicastEnabled_Type(Integer32):
    """Custom type gs2352QosStormControlUnicastEnabled based on Integer32"""
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


_Gs2352QosStormControlUnicastEnabled_Type.__name__ = "Integer32"
_Gs2352QosStormControlUnicastEnabled_Object = MibTableColumn
gs2352QosStormControlUnicastEnabled = _Gs2352QosStormControlUnicastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 2),
    _Gs2352QosStormControlUnicastEnabled_Type()
)
gs2352QosStormControlUnicastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlUnicastEnabled.setStatus("current")


class _Gs2352QosStormControlUnicastRate_Type(Integer32):
    """Custom type gs2352QosStormControlUnicastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2352QosStormControlUnicastRate_Type.__name__ = "Integer32"
_Gs2352QosStormControlUnicastRate_Object = MibTableColumn
gs2352QosStormControlUnicastRate = _Gs2352QosStormControlUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 3),
    _Gs2352QosStormControlUnicastRate_Type()
)
gs2352QosStormControlUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlUnicastRate.setStatus("current")


class _Gs2352QosStormControlUnicastUnit_Type(Integer32):
    """Custom type gs2352QosStormControlUnicastUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("fps", 1))
    )


_Gs2352QosStormControlUnicastUnit_Type.__name__ = "Integer32"
_Gs2352QosStormControlUnicastUnit_Object = MibTableColumn
gs2352QosStormControlUnicastUnit = _Gs2352QosStormControlUnicastUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 4),
    _Gs2352QosStormControlUnicastUnit_Type()
)
gs2352QosStormControlUnicastUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlUnicastUnit.setStatus("current")


class _Gs2352QosStormControlBroadcastEnabled_Type(Integer32):
    """Custom type gs2352QosStormControlBroadcastEnabled based on Integer32"""
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


_Gs2352QosStormControlBroadcastEnabled_Type.__name__ = "Integer32"
_Gs2352QosStormControlBroadcastEnabled_Object = MibTableColumn
gs2352QosStormControlBroadcastEnabled = _Gs2352QosStormControlBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 5),
    _Gs2352QosStormControlBroadcastEnabled_Type()
)
gs2352QosStormControlBroadcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlBroadcastEnabled.setStatus("current")


class _Gs2352QosStormControlBroadcastRate_Type(Integer32):
    """Custom type gs2352QosStormControlBroadcastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2352QosStormControlBroadcastRate_Type.__name__ = "Integer32"
_Gs2352QosStormControlBroadcastRate_Object = MibTableColumn
gs2352QosStormControlBroadcastRate = _Gs2352QosStormControlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 6),
    _Gs2352QosStormControlBroadcastRate_Type()
)
gs2352QosStormControlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlBroadcastRate.setStatus("current")


class _Gs2352QosStormControlBroadcastUnit_Type(Integer32):
    """Custom type gs2352QosStormControlBroadcastUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("fps", 1))
    )


_Gs2352QosStormControlBroadcastUnit_Type.__name__ = "Integer32"
_Gs2352QosStormControlBroadcastUnit_Object = MibTableColumn
gs2352QosStormControlBroadcastUnit = _Gs2352QosStormControlBroadcastUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 7),
    _Gs2352QosStormControlBroadcastUnit_Type()
)
gs2352QosStormControlBroadcastUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlBroadcastUnit.setStatus("current")


class _Gs2352QosStormControlUnknownEnabled_Type(Integer32):
    """Custom type gs2352QosStormControlUnknownEnabled based on Integer32"""
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


_Gs2352QosStormControlUnknownEnabled_Type.__name__ = "Integer32"
_Gs2352QosStormControlUnknownEnabled_Object = MibTableColumn
gs2352QosStormControlUnknownEnabled = _Gs2352QosStormControlUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 8),
    _Gs2352QosStormControlUnknownEnabled_Type()
)
gs2352QosStormControlUnknownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlUnknownEnabled.setStatus("current")


class _Gs2352QosStormControlUnknownRate_Type(Integer32):
    """Custom type gs2352QosStormControlUnknownRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2352QosStormControlUnknownRate_Type.__name__ = "Integer32"
_Gs2352QosStormControlUnknownRate_Object = MibTableColumn
gs2352QosStormControlUnknownRate = _Gs2352QosStormControlUnknownRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 9),
    _Gs2352QosStormControlUnknownRate_Type()
)
gs2352QosStormControlUnknownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlUnknownRate.setStatus("current")


class _Gs2352QosStormControlUnknownUnit_Type(Integer32):
    """Custom type gs2352QosStormControlUnknownUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("fps", 1))
    )


_Gs2352QosStormControlUnknownUnit_Type.__name__ = "Integer32"
_Gs2352QosStormControlUnknownUnit_Object = MibTableColumn
gs2352QosStormControlUnknownUnit = _Gs2352QosStormControlUnknownUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 11, 1, 1, 10),
    _Gs2352QosStormControlUnknownUnit_Type()
)
gs2352QosStormControlUnknownUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosStormControlUnknownUnit.setStatus("current")
_Gs2352QosWREDTable_Object = MibTable
gs2352QosWREDTable = _Gs2352QosWREDTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12)
)
if mibBuilder.loadTexts:
    gs2352QosWREDTable.setStatus("current")
_Gs2352QosWREDEntry_Object = MibTableRow
gs2352QosWREDEntry = _Gs2352QosWREDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1)
)
gs2352QosWREDEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352QosWREDQueueList"),
)
if mibBuilder.loadTexts:
    gs2352QosWREDEntry.setStatus("current")


class _Gs2352QosWREDQueueList_Type(Integer32):
    """Custom type gs2352QosWREDQueueList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2352QosWREDQueueList_Type.__name__ = "Integer32"
_Gs2352QosWREDQueueList_Object = MibTableColumn
gs2352QosWREDQueueList = _Gs2352QosWREDQueueList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1, 1),
    _Gs2352QosWREDQueueList_Type()
)
gs2352QosWREDQueueList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352QosWREDQueueList.setStatus("current")


class _Gs2352QosWREDQueue_Type(Integer32):
    """Custom type gs2352QosWREDQueue based on Integer32"""
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


_Gs2352QosWREDQueue_Type.__name__ = "Integer32"
_Gs2352QosWREDQueue_Object = MibTableColumn
gs2352QosWREDQueue = _Gs2352QosWREDQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1, 2),
    _Gs2352QosWREDQueue_Type()
)
gs2352QosWREDQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosWREDQueue.setStatus("current")


class _Gs2352QosWREDMinThreshold_Type(Integer32):
    """Custom type gs2352QosWREDMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2352QosWREDMinThreshold_Type.__name__ = "Integer32"
_Gs2352QosWREDMinThreshold_Object = MibTableColumn
gs2352QosWREDMinThreshold = _Gs2352QosWREDMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1, 3),
    _Gs2352QosWREDMinThreshold_Type()
)
gs2352QosWREDMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosWREDMinThreshold.setStatus("current")


class _Gs2352QosWREDMaxDP1_Type(Integer32):
    """Custom type gs2352QosWREDMaxDP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2352QosWREDMaxDP1_Type.__name__ = "Integer32"
_Gs2352QosWREDMaxDP1_Object = MibTableColumn
gs2352QosWREDMaxDP1 = _Gs2352QosWREDMaxDP1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1, 4),
    _Gs2352QosWREDMaxDP1_Type()
)
gs2352QosWREDMaxDP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosWREDMaxDP1.setStatus("current")


class _Gs2352QosWREDMaxDP2_Type(Integer32):
    """Custom type gs2352QosWREDMaxDP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2352QosWREDMaxDP2_Type.__name__ = "Integer32"
_Gs2352QosWREDMaxDP2_Object = MibTableColumn
gs2352QosWREDMaxDP2 = _Gs2352QosWREDMaxDP2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1, 5),
    _Gs2352QosWREDMaxDP2_Type()
)
gs2352QosWREDMaxDP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosWREDMaxDP2.setStatus("current")


class _Gs2352QosWREDMaxDP3_Type(Integer32):
    """Custom type gs2352QosWREDMaxDP3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2352QosWREDMaxDP3_Type.__name__ = "Integer32"
_Gs2352QosWREDMaxDP3_Object = MibTableColumn
gs2352QosWREDMaxDP3 = _Gs2352QosWREDMaxDP3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 14, 12, 1, 6),
    _Gs2352QosWREDMaxDP3_Type()
)
gs2352QosWREDMaxDP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352QosWREDMaxDP3.setStatus("current")
_Gs2352Vlan_ObjectIdentity = ObjectIdentity
gs2352Vlan = _Gs2352Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15)
)
_Gs2352VlanPorts_ObjectIdentity = ObjectIdentity
gs2352VlanPorts = _Gs2352VlanPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1)
)


class _Gs2352VlanPortsTPIDforCustomSport_Type(OctetString):
    """Custom type gs2352VlanPortsTPIDforCustomSport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Gs2352VlanPortsTPIDforCustomSport_Type.__name__ = "OctetString"
_Gs2352VlanPortsTPIDforCustomSport_Object = MibScalar
gs2352VlanPortsTPIDforCustomSport = _Gs2352VlanPortsTPIDforCustomSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 1),
    _Gs2352VlanPortsTPIDforCustomSport_Type()
)
gs2352VlanPortsTPIDforCustomSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortsTPIDforCustomSport.setStatus("current")
_Gs2352VlanPortsTable_Object = MibTable
gs2352VlanPortsTable = _Gs2352VlanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352VlanPortsTable.setStatus("current")
_Gs2352VlanPortsEntry_Object = MibTableRow
gs2352VlanPortsEntry = _Gs2352VlanPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1)
)
gs2352VlanPortsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352VlanPortsPort"),
)
if mibBuilder.loadTexts:
    gs2352VlanPortsEntry.setStatus("current")


class _Gs2352VlanPortsPort_Type(Integer32):
    """Custom type gs2352VlanPortsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352VlanPortsPort_Type.__name__ = "Integer32"
_Gs2352VlanPortsPort_Object = MibTableColumn
gs2352VlanPortsPort = _Gs2352VlanPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1, 1),
    _Gs2352VlanPortsPort_Type()
)
gs2352VlanPortsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352VlanPortsPort.setStatus("current")


class _Gs2352VlanPortsPVID_Type(Integer32):
    """Custom type gs2352VlanPortsPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352VlanPortsPVID_Type.__name__ = "Integer32"
_Gs2352VlanPortsPVID_Object = MibTableColumn
gs2352VlanPortsPVID = _Gs2352VlanPortsPVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1, 2),
    _Gs2352VlanPortsPVID_Type()
)
gs2352VlanPortsPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortsPVID.setStatus("current")


class _Gs2352VlanPortsFrameType_Type(Integer32):
    """Custom type gs2352VlanPortsFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_Gs2352VlanPortsFrameType_Type.__name__ = "Integer32"
_Gs2352VlanPortsFrameType_Object = MibTableColumn
gs2352VlanPortsFrameType = _Gs2352VlanPortsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1, 3),
    _Gs2352VlanPortsFrameType_Type()
)
gs2352VlanPortsFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortsFrameType.setStatus("current")


class _Gs2352VlanPortsIngressFilter_Type(Integer32):
    """Custom type gs2352VlanPortsIngressFilter based on Integer32"""
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


_Gs2352VlanPortsIngressFilter_Type.__name__ = "Integer32"
_Gs2352VlanPortsIngressFilter_Object = MibTableColumn
gs2352VlanPortsIngressFilter = _Gs2352VlanPortsIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1, 4),
    _Gs2352VlanPortsIngressFilter_Type()
)
gs2352VlanPortsIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortsIngressFilter.setStatus("current")


class _Gs2352VlanPortsEgressRule_Type(Integer32):
    """Custom type gs2352VlanPortsEgressRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("hybrid", 1),
          ("trunk", 2))
    )


_Gs2352VlanPortsEgressRule_Type.__name__ = "Integer32"
_Gs2352VlanPortsEgressRule_Object = MibTableColumn
gs2352VlanPortsEgressRule = _Gs2352VlanPortsEgressRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1, 5),
    _Gs2352VlanPortsEgressRule_Type()
)
gs2352VlanPortsEgressRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortsEgressRule.setStatus("current")


class _Gs2352VlanPortsPortType_Type(Integer32):
    """Custom type gs2352VlanPortsPortType based on Integer32"""
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
        *(("cPort", 0),
          ("sCustomPort", 1),
          ("sPort", 2),
          ("unaware", 3))
    )


_Gs2352VlanPortsPortType_Type.__name__ = "Integer32"
_Gs2352VlanPortsPortType_Object = MibTableColumn
gs2352VlanPortsPortType = _Gs2352VlanPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 1, 2, 1, 6),
    _Gs2352VlanPortsPortType_Type()
)
gs2352VlanPortsPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortsPortType.setStatus("current")
_Gs2352VlanPrivateVLAN_ObjectIdentity = ObjectIdentity
gs2352VlanPrivateVLAN = _Gs2352VlanPrivateVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 2)
)
_Gs2352VlanPortIsolationTable_Object = MibTable
gs2352VlanPortIsolationTable = _Gs2352VlanPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352VlanPortIsolationTable.setStatus("current")
_Gs2352VlanPortIsolationEntry_Object = MibTableRow
gs2352VlanPortIsolationEntry = _Gs2352VlanPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 2, 2, 1)
)
gs2352VlanPortIsolationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352VlanPortIsolationPort"),
)
if mibBuilder.loadTexts:
    gs2352VlanPortIsolationEntry.setStatus("current")


class _Gs2352VlanPortIsolationPort_Type(Integer32):
    """Custom type gs2352VlanPortIsolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352VlanPortIsolationPort_Type.__name__ = "Integer32"
_Gs2352VlanPortIsolationPort_Object = MibTableColumn
gs2352VlanPortIsolationPort = _Gs2352VlanPortIsolationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 2, 2, 1, 1),
    _Gs2352VlanPortIsolationPort_Type()
)
gs2352VlanPortIsolationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352VlanPortIsolationPort.setStatus("current")


class _Gs2352VlanPortIsolation_Type(Integer32):
    """Custom type gs2352VlanPortIsolation based on Integer32"""
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


_Gs2352VlanPortIsolation_Type.__name__ = "Integer32"
_Gs2352VlanPortIsolation_Object = MibTableColumn
gs2352VlanPortIsolation = _Gs2352VlanPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 2, 2, 1, 2),
    _Gs2352VlanPortIsolation_Type()
)
gs2352VlanPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VlanPortIsolation.setStatus("current")
_Gs2352MACbasedVLAN_ObjectIdentity = ObjectIdentity
gs2352MACbasedVLAN = _Gs2352MACbasedVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3)
)
_Gs2352MACbasedVLANConf_ObjectIdentity = ObjectIdentity
gs2352MACbasedVLANConf = _Gs2352MACbasedVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1)
)
_Gs2352MACbasedVLANConfCreate_Type = Integer32
_Gs2352MACbasedVLANConfCreate_Object = MibScalar
gs2352MACbasedVLANConfCreate = _Gs2352MACbasedVLANConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 1),
    _Gs2352MACbasedVLANConfCreate_Type()
)
gs2352MACbasedVLANConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACbasedVLANConfCreate.setStatus("current")
_Gs2352MACbasedVLANConfTable_Object = MibTable
gs2352MACbasedVLANConfTable = _Gs2352MACbasedVLANConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352MACbasedVLANConfTable.setStatus("current")
_Gs2352MACbasedVLANConfEntry_Object = MibTableRow
gs2352MACbasedVLANConfEntry = _Gs2352MACbasedVLANConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2, 1)
)
gs2352MACbasedVLANConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MACbasedVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2352MACbasedVLANConfEntry.setStatus("current")


class _Gs2352MACbasedVLANIndex_Type(Integer32):
    """Custom type gs2352MACbasedVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2352MACbasedVLANIndex_Type.__name__ = "Integer32"
_Gs2352MACbasedVLANIndex_Object = MibTableColumn
gs2352MACbasedVLANIndex = _Gs2352MACbasedVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2, 1, 1),
    _Gs2352MACbasedVLANIndex_Type()
)
gs2352MACbasedVLANIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACbasedVLANIndex.setStatus("current")
_Gs2352MACbasedVLANMACAddress_Type = MacAddress
_Gs2352MACbasedVLANMACAddress_Object = MibTableColumn
gs2352MACbasedVLANMACAddress = _Gs2352MACbasedVLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2, 1, 2),
    _Gs2352MACbasedVLANMACAddress_Type()
)
gs2352MACbasedVLANMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACbasedVLANMACAddress.setStatus("current")


class _Gs2352MACbasedVLANID_Type(Integer32):
    """Custom type gs2352MACbasedVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352MACbasedVLANID_Type.__name__ = "Integer32"
_Gs2352MACbasedVLANID_Object = MibTableColumn
gs2352MACbasedVLANID = _Gs2352MACbasedVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2, 1, 3),
    _Gs2352MACbasedVLANID_Type()
)
gs2352MACbasedVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACbasedVLANID.setStatus("current")
_Gs2352MACbasedMemberships_Type = DisplayString
_Gs2352MACbasedMemberships_Object = MibTableColumn
gs2352MACbasedMemberships = _Gs2352MACbasedMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2, 1, 4),
    _Gs2352MACbasedMemberships_Type()
)
gs2352MACbasedMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACbasedMemberships.setStatus("current")


class _Gs2352MACbaseRowStatus_Type(Integer32):
    """Custom type gs2352MACbaseRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4))
    )


_Gs2352MACbaseRowStatus_Type.__name__ = "Integer32"
_Gs2352MACbaseRowStatus_Object = MibTableColumn
gs2352MACbaseRowStatus = _Gs2352MACbaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 15, 3, 1, 2, 1, 5),
    _Gs2352MACbaseRowStatus_Type()
)
gs2352MACbaseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MACbaseRowStatus.setStatus("current")
_Gs2352IGMPSnooping_ObjectIdentity = ObjectIdentity
gs2352IGMPSnooping = _Gs2352IGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16)
)
_Gs2352IGMPSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2352IGMPSnoopingBasic = _Gs2352IGMPSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1)
)


class _Gs2352IGMPSnoopingEnable_Type(Integer32):
    """Custom type gs2352IGMPSnoopingEnable based on Integer32"""
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


_Gs2352IGMPSnoopingEnable_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingEnable_Object = MibScalar
gs2352IGMPSnoopingEnable = _Gs2352IGMPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 1),
    _Gs2352IGMPSnoopingEnable_Type()
)
gs2352IGMPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingEnable.setStatus("current")


class _Gs2352IGMPSnoopingUnregisteredIPMCv4Flooding_Type(Integer32):
    """Custom type gs2352IGMPSnoopingUnregisteredIPMCv4Flooding based on Integer32"""
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


_Gs2352IGMPSnoopingUnregisteredIPMCv4Flooding_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingUnregisteredIPMCv4Flooding_Object = MibScalar
gs2352IGMPSnoopingUnregisteredIPMCv4Flooding = _Gs2352IGMPSnoopingUnregisteredIPMCv4Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 2),
    _Gs2352IGMPSnoopingUnregisteredIPMCv4Flooding_Type()
)
gs2352IGMPSnoopingUnregisteredIPMCv4Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingUnregisteredIPMCv4Flooding.setStatus("current")
_Gs2352IGMPSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2352IGMPSnoopingSSMIPRangeAddr_Object = MibScalar
gs2352IGMPSnoopingSSMIPRangeAddr = _Gs2352IGMPSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 3),
    _Gs2352IGMPSnoopingSSMIPRangeAddr_Type()
)
gs2352IGMPSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2352IGMPSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2352IGMPSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_Gs2352IGMPSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingSSMIPRangeValue_Object = MibScalar
gs2352IGMPSnoopingSSMIPRangeValue = _Gs2352IGMPSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 4),
    _Gs2352IGMPSnoopingSSMIPRangeValue_Type()
)
gs2352IGMPSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2352IGMPSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2352IGMPSnoopingProxyEnabled based on Integer32"""
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


_Gs2352IGMPSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingProxyEnabled_Object = MibScalar
gs2352IGMPSnoopingProxyEnabled = _Gs2352IGMPSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 5),
    _Gs2352IGMPSnoopingProxyEnabled_Type()
)
gs2352IGMPSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingProxyEnabled.setStatus("current")
_Gs2352IGMPSnoopingPortRelatedTable_Object = MibTable
gs2352IGMPSnoopingPortRelatedTable = _Gs2352IGMPSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortRelatedTable.setStatus("current")
_Gs2352IGMPSnoopingPortRelatedEntry_Object = MibTableRow
gs2352IGMPSnoopingPortRelatedEntry = _Gs2352IGMPSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 6, 1)
)
gs2352IGMPSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortRelatedEntry.setStatus("current")


class _Gs2352IGMPSnoopingRouterPort_Type(Integer32):
    """Custom type gs2352IGMPSnoopingRouterPort based on Integer32"""
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


_Gs2352IGMPSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingRouterPort_Object = MibTableColumn
gs2352IGMPSnoopingRouterPort = _Gs2352IGMPSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 6, 1, 1),
    _Gs2352IGMPSnoopingRouterPort_Type()
)
gs2352IGMPSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingRouterPort.setStatus("current")


class _Gs2352IGMPSnoopingFastLeave_Type(Integer32):
    """Custom type gs2352IGMPSnoopingFastLeave based on Integer32"""
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


_Gs2352IGMPSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingFastLeave_Object = MibTableColumn
gs2352IGMPSnoopingFastLeave = _Gs2352IGMPSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 6, 1, 2),
    _Gs2352IGMPSnoopingFastLeave_Type()
)
gs2352IGMPSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingFastLeave.setStatus("current")


class _Gs2352IGMPSnoopingThrottling_Type(Integer32):
    """Custom type gs2352IGMPSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2352IGMPSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingThrottling_Object = MibTableColumn
gs2352IGMPSnoopingThrottling = _Gs2352IGMPSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 1, 6, 1, 3),
    _Gs2352IGMPSnoopingThrottling_Type()
)
gs2352IGMPSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingThrottling.setStatus("current")
_Gs2352IGMPSnoopingVLANTable_Object = MibTable
gs2352IGMPSnoopingVLANTable = _Gs2352IGMPSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANTable.setStatus("current")
_Gs2352IGMPSnoopingVLANEntry_Object = MibTableRow
gs2352IGMPSnoopingVLANEntry = _Gs2352IGMPSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1)
)
gs2352IGMPSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IGMPSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANEntry.setStatus("current")


class _Gs2352IGMPSnoopingVLANID_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IGMPSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANID_Object = MibTableColumn
gs2352IGMPSnoopingVLANID = _Gs2352IGMPSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 1),
    _Gs2352IGMPSnoopingVLANID_Type()
)
gs2352IGMPSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANID.setStatus("current")


class _Gs2352IGMPSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANEnable based on Integer32"""
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


_Gs2352IGMPSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANEnable_Object = MibTableColumn
gs2352IGMPSnoopingVLANEnable = _Gs2352IGMPSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 2),
    _Gs2352IGMPSnoopingVLANEnable_Type()
)
gs2352IGMPSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANEnable.setStatus("current")


class _Gs2352IGMPSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANIGMPQuerier based on Integer32"""
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


_Gs2352IGMPSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2352IGMPSnoopingVLANIGMPQuerier = _Gs2352IGMPSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 3),
    _Gs2352IGMPSnoopingVLANIGMPQuerier_Type()
)
gs2352IGMPSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2352IGMPSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANCompatibility based on Integer32"""
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
        *(("igmpAuto", 0),
          ("forcedIGMPv1", 1),
          ("forcedIGMPv2", 2),
          ("forcedIGMPv3", 3),
          ("none", 4))
    )


_Gs2352IGMPSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANCompatibility_Object = MibTableColumn
gs2352IGMPSnoopingVLANCompatibility = _Gs2352IGMPSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 4),
    _Gs2352IGMPSnoopingVLANCompatibility_Type()
)
gs2352IGMPSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANCompatibility.setStatus("current")


class _Gs2352IGMPSnoopingVLANRV_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2352IGMPSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANRV_Object = MibTableColumn
gs2352IGMPSnoopingVLANRV = _Gs2352IGMPSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 5),
    _Gs2352IGMPSnoopingVLANRV_Type()
)
gs2352IGMPSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANRV.setStatus("current")


class _Gs2352IGMPSnoopingVLANQI_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2352IGMPSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANQI_Object = MibTableColumn
gs2352IGMPSnoopingVLANQI = _Gs2352IGMPSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 6),
    _Gs2352IGMPSnoopingVLANQI_Type()
)
gs2352IGMPSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANQI.setStatus("current")


class _Gs2352IGMPSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2352IGMPSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANQRI_Object = MibTableColumn
gs2352IGMPSnoopingVLANQRI = _Gs2352IGMPSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 7),
    _Gs2352IGMPSnoopingVLANQRI_Type()
)
gs2352IGMPSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANQRI.setStatus("current")


class _Gs2352IGMPSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2352IGMPSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANLLQI_Object = MibTableColumn
gs2352IGMPSnoopingVLANLLQI = _Gs2352IGMPSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 8),
    _Gs2352IGMPSnoopingVLANLLQI_Type()
)
gs2352IGMPSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANLLQI.setStatus("current")


class _Gs2352IGMPSnoopingVLANURI_Type(Integer32):
    """Custom type gs2352IGMPSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2352IGMPSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingVLANURI_Object = MibTableColumn
gs2352IGMPSnoopingVLANURI = _Gs2352IGMPSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 2, 1, 9),
    _Gs2352IGMPSnoopingVLANURI_Type()
)
gs2352IGMPSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingVLANURI.setStatus("current")
_Gs2352IGMPSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2352IGMPSnoopingPortGroupFiltering = _Gs2352IGMPSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3)
)
_Gs2352IGMPSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2352IGMPSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2352IGMPSnoopingPortGroupFilteringCreate = _Gs2352IGMPSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 1),
    _Gs2352IGMPSnoopingPortGroupFilteringCreate_Type()
)
gs2352IGMPSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2352IGMPSnoopingPortGroupFilteringTable_Object = MibTable
gs2352IGMPSnoopingPortGroupFilteringTable = _Gs2352IGMPSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2352IGMPSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2352IGMPSnoopingPortGroupFilteringEntry = _Gs2352IGMPSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 2, 1)
)
gs2352IGMPSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IGMPSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2352IGMPSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2352IGMPSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352IGMPSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2352IGMPSnoopingPortGroupFilteringIndex = _Gs2352IGMPSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 2, 1, 1),
    _Gs2352IGMPSnoopingPortGroupFilteringIndex_Type()
)
gs2352IGMPSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2352IGMPSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2352IGMPSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352IGMPSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2352IGMPSnoopingPortGroupFilteringPort = _Gs2352IGMPSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 2, 1, 2),
    _Gs2352IGMPSnoopingPortGroupFilteringPort_Type()
)
gs2352IGMPSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2352IGMPSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2352IGMPSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2352IGMPSnoopingPortGroupFilteringGroups = _Gs2352IGMPSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 2, 1, 3),
    _Gs2352IGMPSnoopingPortGroupFilteringGroups_Type()
)
gs2352IGMPSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2352IGMPSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2352IGMPSnoopingPortGroupFilteringRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4))
    )


_Gs2352IGMPSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2352IGMPSnoopingPortGroupFilteringRowStatus = _Gs2352IGMPSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 3, 2, 1, 4),
    _Gs2352IGMPSnoopingPortGroupFilteringRowStatus_Type()
)
gs2352IGMPSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2352IGMPSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2352IGMPSnoopingStatus = _Gs2352IGMPSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4)
)


class _Gs2352IGMPSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2352IGMPSnoopingstatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352IGMPSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingstatisticClear_Object = MibScalar
gs2352IGMPSnoopingstatisticClear = _Gs2352IGMPSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 1),
    _Gs2352IGMPSnoopingstatisticClear_Type()
)
gs2352IGMPSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticClear.setStatus("current")
_Gs2352IGMPSnoopingstatisticTable_Object = MibTable
gs2352IGMPSnoopingstatisticTable = _Gs2352IGMPSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticTable.setStatus("current")
_Gs2352IGMPSnoopingstatisticEntry_Object = MibTableRow
gs2352IGMPSnoopingstatisticEntry = _Gs2352IGMPSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1)
)
gs2352IGMPSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IGMPSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticEntry.setStatus("current")


class _Gs2352IGMPSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2352IGMPSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IGMPSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingstatisticVLANID_Object = MibTableColumn
gs2352IGMPSnoopingstatisticVLANID = _Gs2352IGMPSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 1),
    _Gs2352IGMPSnoopingstatisticVLANID_Type()
)
gs2352IGMPSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticVLANID.setStatus("current")
_Gs2352IGMPSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2352IGMPSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2352IGMPSnoopingstatisticQuerierVersion = _Gs2352IGMPSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 2),
    _Gs2352IGMPSnoopingstatisticQuerierVersion_Type()
)
gs2352IGMPSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2352IGMPSnoopingstatisticHostVersion_Type = DisplayString
_Gs2352IGMPSnoopingstatisticHostVersion_Object = MibTableColumn
gs2352IGMPSnoopingstatisticHostVersion = _Gs2352IGMPSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 3),
    _Gs2352IGMPSnoopingstatisticHostVersion_Type()
)
gs2352IGMPSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticHostVersion.setStatus("current")
_Gs2352IGMPSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2352IGMPSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2352IGMPSnoopingstatisticQuerierStatus = _Gs2352IGMPSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 4),
    _Gs2352IGMPSnoopingstatisticQuerierStatus_Type()
)
gs2352IGMPSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2352IGMPSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2352IGMPSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2352IGMPSnoopingstatisticQueriesTransmitted = _Gs2352IGMPSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 5),
    _Gs2352IGMPSnoopingstatisticQueriesTransmitted_Type()
)
gs2352IGMPSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2352IGMPSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2352IGMPSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2352IGMPSnoopingstatisticQueriesReceived = _Gs2352IGMPSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 6),
    _Gs2352IGMPSnoopingstatisticQueriesReceived_Type()
)
gs2352IGMPSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2352IGMPSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2352IGMPSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2352IGMPSnoopingstatisticV1ReportsReceived = _Gs2352IGMPSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 7),
    _Gs2352IGMPSnoopingstatisticV1ReportsReceived_Type()
)
gs2352IGMPSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2352IGMPSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2352IGMPSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2352IGMPSnoopingstatisticV2ReportsReceived = _Gs2352IGMPSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 8),
    _Gs2352IGMPSnoopingstatisticV2ReportsReceived_Type()
)
gs2352IGMPSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2352IGMPSnoopingstatisticV3ReportsReceived_Type = Counter32
_Gs2352IGMPSnoopingstatisticV3ReportsReceived_Object = MibTableColumn
gs2352IGMPSnoopingstatisticV3ReportsReceived = _Gs2352IGMPSnoopingstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 9),
    _Gs2352IGMPSnoopingstatisticV3ReportsReceived_Type()
)
gs2352IGMPSnoopingstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticV3ReportsReceived.setStatus("current")
_Gs2352IGMPSnoopingstatisticV2LeavesReceived_Type = Counter32
_Gs2352IGMPSnoopingstatisticV2LeavesReceived_Object = MibTableColumn
gs2352IGMPSnoopingstatisticV2LeavesReceived = _Gs2352IGMPSnoopingstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 2, 1, 10),
    _Gs2352IGMPSnoopingstatisticV2LeavesReceived_Type()
)
gs2352IGMPSnoopingstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingstatisticV2LeavesReceived.setStatus("current")
_Gs2352IGMPSnoopingRouterPortTable_Object = MibTable
gs2352IGMPSnoopingRouterPortTable = _Gs2352IGMPSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 3)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingRouterPortTable.setStatus("current")
_Gs2352IGMPSnoopingRouterPortEntry_Object = MibTableRow
gs2352IGMPSnoopingRouterPortEntry = _Gs2352IGMPSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 3, 1)
)
gs2352IGMPSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingRouterPortEntry.setStatus("current")
_Gs2352IGMPSnoopingRouterPortStatus_Type = DisplayString
_Gs2352IGMPSnoopingRouterPortStatus_Object = MibTableColumn
gs2352IGMPSnoopingRouterPortStatus = _Gs2352IGMPSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 4, 3, 1, 1),
    _Gs2352IGMPSnoopingRouterPortStatus_Type()
)
gs2352IGMPSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingRouterPortStatus.setStatus("current")
_Gs2352IGMPSnoopingGroupsTable_Object = MibTable
gs2352IGMPSnoopingGroupsTable = _Gs2352IGMPSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 5)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingGroupsTable.setStatus("current")
_Gs2352IGMPSnoopingGroupsEntry_Object = MibTableRow
gs2352IGMPSnoopingGroupsEntry = _Gs2352IGMPSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 5, 1)
)
gs2352IGMPSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IGMPSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingGroupsEntry.setStatus("current")


class _Gs2352IGMPSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2352IGMPSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352IGMPSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingGroupsIndex_Object = MibTableColumn
gs2352IGMPSnoopingGroupsIndex = _Gs2352IGMPSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 5, 1, 1),
    _Gs2352IGMPSnoopingGroupsIndex_Type()
)
gs2352IGMPSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingGroupsIndex.setStatus("current")


class _Gs2352IGMPSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2352IGMPSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IGMPSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingGroupsVLANID_Object = MibTableColumn
gs2352IGMPSnoopingGroupsVLANID = _Gs2352IGMPSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 5, 1, 2),
    _Gs2352IGMPSnoopingGroupsVLANID_Type()
)
gs2352IGMPSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingGroupsVLANID.setStatus("current")
_Gs2352IGMPSnoopingGroups_Type = DisplayString
_Gs2352IGMPSnoopingGroups_Object = MibTableColumn
gs2352IGMPSnoopingGroups = _Gs2352IGMPSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 5, 1, 3),
    _Gs2352IGMPSnoopingGroups_Type()
)
gs2352IGMPSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingGroups.setStatus("current")
_Gs2352IGMPSnoopingGroupsMemberships_Type = DisplayString
_Gs2352IGMPSnoopingGroupsMemberships_Object = MibTableColumn
gs2352IGMPSnoopingGroupsMemberships = _Gs2352IGMPSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 5, 1, 4),
    _Gs2352IGMPSnoopingGroupsMemberships_Type()
)
gs2352IGMPSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingGroupsMemberships.setStatus("current")
_Gs2352IGMPSnoopingSSMTable_Object = MibTable
gs2352IGMPSnoopingSSMTable = _Gs2352IGMPSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6)
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMTable.setStatus("current")
_Gs2352IGMPSnoopingSSMEntry_Object = MibTableRow
gs2352IGMPSnoopingSSMEntry = _Gs2352IGMPSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1)
)
gs2352IGMPSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IGMPSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMEntry.setStatus("current")


class _Gs2352IGMPSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2352IGMPSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352IGMPSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingSSMIndex_Object = MibTableColumn
gs2352IGMPSnoopingSSMIndex = _Gs2352IGMPSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 1),
    _Gs2352IGMPSnoopingSSMIndex_Type()
)
gs2352IGMPSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMIndex.setStatus("current")


class _Gs2352IGMPSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2352IGMPSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IGMPSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingSSMVLANID_Object = MibTableColumn
gs2352IGMPSnoopingSSMVLANID = _Gs2352IGMPSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 2),
    _Gs2352IGMPSnoopingSSMVLANID_Type()
)
gs2352IGMPSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMVLANID.setStatus("current")
_Gs2352IGMPSnoopingSSMGroup_Type = DisplayString
_Gs2352IGMPSnoopingSSMGroup_Object = MibTableColumn
gs2352IGMPSnoopingSSMGroup = _Gs2352IGMPSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 3),
    _Gs2352IGMPSnoopingSSMGroup_Type()
)
gs2352IGMPSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMGroup.setStatus("current")


class _Gs2352IGMPSnoopingSSMPort_Type(Integer32):
    """Custom type gs2352IGMPSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352IGMPSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2352IGMPSnoopingSSMPort_Object = MibTableColumn
gs2352IGMPSnoopingSSMPort = _Gs2352IGMPSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 4),
    _Gs2352IGMPSnoopingSSMPort_Type()
)
gs2352IGMPSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMPort.setStatus("current")
_Gs2352IGMPSnoopingSSMMode_Type = DisplayString
_Gs2352IGMPSnoopingSSMMode_Object = MibTableColumn
gs2352IGMPSnoopingSSMMode = _Gs2352IGMPSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 5),
    _Gs2352IGMPSnoopingSSMMode_Type()
)
gs2352IGMPSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMMode.setStatus("current")
_Gs2352IGMPSnoopingSSMSourceAddress_Type = DisplayString
_Gs2352IGMPSnoopingSSMSourceAddress_Object = MibTableColumn
gs2352IGMPSnoopingSSMSourceAddress = _Gs2352IGMPSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 6),
    _Gs2352IGMPSnoopingSSMSourceAddress_Type()
)
gs2352IGMPSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMSourceAddress.setStatus("current")
_Gs2352IGMPSnoopingSSMType_Type = DisplayString
_Gs2352IGMPSnoopingSSMType_Object = MibTableColumn
gs2352IGMPSnoopingSSMType = _Gs2352IGMPSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 16, 6, 1, 7),
    _Gs2352IGMPSnoopingSSMType_Type()
)
gs2352IGMPSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IGMPSnoopingSSMType.setStatus("current")
_Gs2352MLDSnooping_ObjectIdentity = ObjectIdentity
gs2352MLDSnooping = _Gs2352MLDSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17)
)
_Gs2352MLDSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2352MLDSnoopingBasic = _Gs2352MLDSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1)
)


class _Gs2352MLDSnoopingEnable_Type(Integer32):
    """Custom type gs2352MLDSnoopingEnable based on Integer32"""
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


_Gs2352MLDSnoopingEnable_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingEnable_Object = MibScalar
gs2352MLDSnoopingEnable = _Gs2352MLDSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 1),
    _Gs2352MLDSnoopingEnable_Type()
)
gs2352MLDSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingEnable.setStatus("current")


class _Gs2352MLDSnoopingUnregisteredIPMCv6Flooding_Type(Integer32):
    """Custom type gs2352MLDSnoopingUnregisteredIPMCv6Flooding based on Integer32"""
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


_Gs2352MLDSnoopingUnregisteredIPMCv6Flooding_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingUnregisteredIPMCv6Flooding_Object = MibScalar
gs2352MLDSnoopingUnregisteredIPMCv6Flooding = _Gs2352MLDSnoopingUnregisteredIPMCv6Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 2),
    _Gs2352MLDSnoopingUnregisteredIPMCv6Flooding_Type()
)
gs2352MLDSnoopingUnregisteredIPMCv6Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingUnregisteredIPMCv6Flooding.setStatus("current")
_Gs2352MLDSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2352MLDSnoopingSSMIPRangeAddr_Object = MibScalar
gs2352MLDSnoopingSSMIPRangeAddr = _Gs2352MLDSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 3),
    _Gs2352MLDSnoopingSSMIPRangeAddr_Type()
)
gs2352MLDSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2352MLDSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2352MLDSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_Gs2352MLDSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingSSMIPRangeValue_Object = MibScalar
gs2352MLDSnoopingSSMIPRangeValue = _Gs2352MLDSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 4),
    _Gs2352MLDSnoopingSSMIPRangeValue_Type()
)
gs2352MLDSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2352MLDSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2352MLDSnoopingProxyEnabled based on Integer32"""
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


_Gs2352MLDSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingProxyEnabled_Object = MibScalar
gs2352MLDSnoopingProxyEnabled = _Gs2352MLDSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 5),
    _Gs2352MLDSnoopingProxyEnabled_Type()
)
gs2352MLDSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingProxyEnabled.setStatus("current")
_Gs2352MLDSnoopingPortRelatedTable_Object = MibTable
gs2352MLDSnoopingPortRelatedTable = _Gs2352MLDSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 6)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortRelatedTable.setStatus("current")
_Gs2352MLDSnoopingPortRelatedEntry_Object = MibTableRow
gs2352MLDSnoopingPortRelatedEntry = _Gs2352MLDSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 6, 1)
)
gs2352MLDSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortRelatedEntry.setStatus("current")


class _Gs2352MLDSnoopingRouterPort_Type(Integer32):
    """Custom type gs2352MLDSnoopingRouterPort based on Integer32"""
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


_Gs2352MLDSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingRouterPort_Object = MibTableColumn
gs2352MLDSnoopingRouterPort = _Gs2352MLDSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 6, 1, 1),
    _Gs2352MLDSnoopingRouterPort_Type()
)
gs2352MLDSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingRouterPort.setStatus("current")


class _Gs2352MLDSnoopingFastLeave_Type(Integer32):
    """Custom type gs2352MLDSnoopingFastLeave based on Integer32"""
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


_Gs2352MLDSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingFastLeave_Object = MibTableColumn
gs2352MLDSnoopingFastLeave = _Gs2352MLDSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 6, 1, 2),
    _Gs2352MLDSnoopingFastLeave_Type()
)
gs2352MLDSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingFastLeave.setStatus("current")


class _Gs2352MLDSnoopingThrottling_Type(Integer32):
    """Custom type gs2352MLDSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2352MLDSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingThrottling_Object = MibTableColumn
gs2352MLDSnoopingThrottling = _Gs2352MLDSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 1, 6, 1, 3),
    _Gs2352MLDSnoopingThrottling_Type()
)
gs2352MLDSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingThrottling.setStatus("current")
_Gs2352MLDSnoopingVLANTable_Object = MibTable
gs2352MLDSnoopingVLANTable = _Gs2352MLDSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANTable.setStatus("current")
_Gs2352MLDSnoopingVLANEntry_Object = MibTableRow
gs2352MLDSnoopingVLANEntry = _Gs2352MLDSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1)
)
gs2352MLDSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MLDSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANEntry.setStatus("current")


class _Gs2352MLDSnoopingVLANID_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MLDSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANID_Object = MibTableColumn
gs2352MLDSnoopingVLANID = _Gs2352MLDSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 1),
    _Gs2352MLDSnoopingVLANID_Type()
)
gs2352MLDSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANID.setStatus("current")


class _Gs2352MLDSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANEnable based on Integer32"""
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


_Gs2352MLDSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANEnable_Object = MibTableColumn
gs2352MLDSnoopingVLANEnable = _Gs2352MLDSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 2),
    _Gs2352MLDSnoopingVLANEnable_Type()
)
gs2352MLDSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANEnable.setStatus("current")


class _Gs2352MLDSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANIGMPQuerier based on Integer32"""
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


_Gs2352MLDSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2352MLDSnoopingVLANIGMPQuerier = _Gs2352MLDSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 3),
    _Gs2352MLDSnoopingVLANIGMPQuerier_Type()
)
gs2352MLDSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2352MLDSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANCompatibility based on Integer32"""
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
        *(("mldAuto", 0),
          ("forcedMLDv1", 1),
          ("forcedMLDv2", 2),
          ("none", 3))
    )


_Gs2352MLDSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANCompatibility_Object = MibTableColumn
gs2352MLDSnoopingVLANCompatibility = _Gs2352MLDSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 4),
    _Gs2352MLDSnoopingVLANCompatibility_Type()
)
gs2352MLDSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANCompatibility.setStatus("current")


class _Gs2352MLDSnoopingVLANRV_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2352MLDSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANRV_Object = MibTableColumn
gs2352MLDSnoopingVLANRV = _Gs2352MLDSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 5),
    _Gs2352MLDSnoopingVLANRV_Type()
)
gs2352MLDSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANRV.setStatus("current")


class _Gs2352MLDSnoopingVLANQI_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2352MLDSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANQI_Object = MibTableColumn
gs2352MLDSnoopingVLANQI = _Gs2352MLDSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 6),
    _Gs2352MLDSnoopingVLANQI_Type()
)
gs2352MLDSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANQI.setStatus("current")


class _Gs2352MLDSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2352MLDSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANQRI_Object = MibTableColumn
gs2352MLDSnoopingVLANQRI = _Gs2352MLDSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 7),
    _Gs2352MLDSnoopingVLANQRI_Type()
)
gs2352MLDSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANQRI.setStatus("current")


class _Gs2352MLDSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2352MLDSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANLLQI_Object = MibTableColumn
gs2352MLDSnoopingVLANLLQI = _Gs2352MLDSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 8),
    _Gs2352MLDSnoopingVLANLLQI_Type()
)
gs2352MLDSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANLLQI.setStatus("current")


class _Gs2352MLDSnoopingVLANURI_Type(Integer32):
    """Custom type gs2352MLDSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2352MLDSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingVLANURI_Object = MibTableColumn
gs2352MLDSnoopingVLANURI = _Gs2352MLDSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 2, 1, 9),
    _Gs2352MLDSnoopingVLANURI_Type()
)
gs2352MLDSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingVLANURI.setStatus("current")
_Gs2352MLDSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2352MLDSnoopingPortGroupFiltering = _Gs2352MLDSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3)
)
_Gs2352MLDSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2352MLDSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2352MLDSnoopingPortGroupFilteringCreate = _Gs2352MLDSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 1),
    _Gs2352MLDSnoopingPortGroupFilteringCreate_Type()
)
gs2352MLDSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2352MLDSnoopingPortGroupFilteringTable_Object = MibTable
gs2352MLDSnoopingPortGroupFilteringTable = _Gs2352MLDSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2352MLDSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2352MLDSnoopingPortGroupFilteringEntry = _Gs2352MLDSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 2, 1)
)
gs2352MLDSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MLDSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2352MLDSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2352MLDSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MLDSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2352MLDSnoopingPortGroupFilteringIndex = _Gs2352MLDSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 2, 1, 1),
    _Gs2352MLDSnoopingPortGroupFilteringIndex_Type()
)
gs2352MLDSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2352MLDSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2352MLDSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MLDSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2352MLDSnoopingPortGroupFilteringPort = _Gs2352MLDSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 2, 1, 2),
    _Gs2352MLDSnoopingPortGroupFilteringPort_Type()
)
gs2352MLDSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2352MLDSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2352MLDSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2352MLDSnoopingPortGroupFilteringGroups = _Gs2352MLDSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 2, 1, 3),
    _Gs2352MLDSnoopingPortGroupFilteringGroups_Type()
)
gs2352MLDSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2352MLDSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2352MLDSnoopingPortGroupFilteringRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4))
    )


_Gs2352MLDSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2352MLDSnoopingPortGroupFilteringRowStatus = _Gs2352MLDSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 3, 2, 1, 4),
    _Gs2352MLDSnoopingPortGroupFilteringRowStatus_Type()
)
gs2352MLDSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2352MLDSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2352MLDSnoopingStatus = _Gs2352MLDSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4)
)


class _Gs2352MLDSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2352MLDSnoopingstatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352MLDSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingstatisticClear_Object = MibScalar
gs2352MLDSnoopingstatisticClear = _Gs2352MLDSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 1),
    _Gs2352MLDSnoopingstatisticClear_Type()
)
gs2352MLDSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticClear.setStatus("current")
_Gs2352MLDSnoopingstatisticTable_Object = MibTable
gs2352MLDSnoopingstatisticTable = _Gs2352MLDSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticTable.setStatus("current")
_Gs2352MLDSnoopingstatisticEntry_Object = MibTableRow
gs2352MLDSnoopingstatisticEntry = _Gs2352MLDSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1)
)
gs2352MLDSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MLDSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticEntry.setStatus("current")


class _Gs2352MLDSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2352MLDSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MLDSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingstatisticVLANID_Object = MibTableColumn
gs2352MLDSnoopingstatisticVLANID = _Gs2352MLDSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 1),
    _Gs2352MLDSnoopingstatisticVLANID_Type()
)
gs2352MLDSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticVLANID.setStatus("current")
_Gs2352MLDSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2352MLDSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2352MLDSnoopingstatisticQuerierVersion = _Gs2352MLDSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 2),
    _Gs2352MLDSnoopingstatisticQuerierVersion_Type()
)
gs2352MLDSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2352MLDSnoopingstatisticHostVersion_Type = DisplayString
_Gs2352MLDSnoopingstatisticHostVersion_Object = MibTableColumn
gs2352MLDSnoopingstatisticHostVersion = _Gs2352MLDSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 3),
    _Gs2352MLDSnoopingstatisticHostVersion_Type()
)
gs2352MLDSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticHostVersion.setStatus("current")
_Gs2352MLDSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2352MLDSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2352MLDSnoopingstatisticQuerierStatus = _Gs2352MLDSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 4),
    _Gs2352MLDSnoopingstatisticQuerierStatus_Type()
)
gs2352MLDSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2352MLDSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2352MLDSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2352MLDSnoopingstatisticQueriesTransmitted = _Gs2352MLDSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 5),
    _Gs2352MLDSnoopingstatisticQueriesTransmitted_Type()
)
gs2352MLDSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2352MLDSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2352MLDSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2352MLDSnoopingstatisticQueriesReceived = _Gs2352MLDSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 6),
    _Gs2352MLDSnoopingstatisticQueriesReceived_Type()
)
gs2352MLDSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2352MLDSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2352MLDSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2352MLDSnoopingstatisticV1ReportsReceived = _Gs2352MLDSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 7),
    _Gs2352MLDSnoopingstatisticV1ReportsReceived_Type()
)
gs2352MLDSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2352MLDSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2352MLDSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2352MLDSnoopingstatisticV2ReportsReceived = _Gs2352MLDSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 8),
    _Gs2352MLDSnoopingstatisticV2ReportsReceived_Type()
)
gs2352MLDSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2352MLDSnoopingstatisticV1LeavesReceived_Type = Counter32
_Gs2352MLDSnoopingstatisticV1LeavesReceived_Object = MibTableColumn
gs2352MLDSnoopingstatisticV1LeavesReceived = _Gs2352MLDSnoopingstatisticV1LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 2, 1, 9),
    _Gs2352MLDSnoopingstatisticV1LeavesReceived_Type()
)
gs2352MLDSnoopingstatisticV1LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingstatisticV1LeavesReceived.setStatus("current")
_Gs2352MLDSnoopingRouterPortTable_Object = MibTable
gs2352MLDSnoopingRouterPortTable = _Gs2352MLDSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 3)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingRouterPortTable.setStatus("current")
_Gs2352MLDSnoopingRouterPortEntry_Object = MibTableRow
gs2352MLDSnoopingRouterPortEntry = _Gs2352MLDSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 3, 1)
)
gs2352MLDSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingRouterPortEntry.setStatus("current")
_Gs2352MLDSnoopingRouterPortStatus_Type = DisplayString
_Gs2352MLDSnoopingRouterPortStatus_Object = MibTableColumn
gs2352MLDSnoopingRouterPortStatus = _Gs2352MLDSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 4, 3, 1, 1),
    _Gs2352MLDSnoopingRouterPortStatus_Type()
)
gs2352MLDSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingRouterPortStatus.setStatus("current")
_Gs2352MLDSnoopingGroupsTable_Object = MibTable
gs2352MLDSnoopingGroupsTable = _Gs2352MLDSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 5)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingGroupsTable.setStatus("current")
_Gs2352MLDSnoopingGroupsEntry_Object = MibTableRow
gs2352MLDSnoopingGroupsEntry = _Gs2352MLDSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 5, 1)
)
gs2352MLDSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MLDSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingGroupsEntry.setStatus("current")


class _Gs2352MLDSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2352MLDSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MLDSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingGroupsIndex_Object = MibTableColumn
gs2352MLDSnoopingGroupsIndex = _Gs2352MLDSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 5, 1, 1),
    _Gs2352MLDSnoopingGroupsIndex_Type()
)
gs2352MLDSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingGroupsIndex.setStatus("current")


class _Gs2352MLDSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2352MLDSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MLDSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingGroupsVLANID_Object = MibTableColumn
gs2352MLDSnoopingGroupsVLANID = _Gs2352MLDSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 5, 1, 2),
    _Gs2352MLDSnoopingGroupsVLANID_Type()
)
gs2352MLDSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingGroupsVLANID.setStatus("current")
_Gs2352MLDSnoopingGroups_Type = DisplayString
_Gs2352MLDSnoopingGroups_Object = MibTableColumn
gs2352MLDSnoopingGroups = _Gs2352MLDSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 5, 1, 3),
    _Gs2352MLDSnoopingGroups_Type()
)
gs2352MLDSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingGroups.setStatus("current")
_Gs2352MLDSnoopingGroupsMemberships_Type = DisplayString
_Gs2352MLDSnoopingGroupsMemberships_Object = MibTableColumn
gs2352MLDSnoopingGroupsMemberships = _Gs2352MLDSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 5, 1, 4),
    _Gs2352MLDSnoopingGroupsMemberships_Type()
)
gs2352MLDSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingGroupsMemberships.setStatus("current")
_Gs2352MLDSnoopingSSMTable_Object = MibTable
gs2352MLDSnoopingSSMTable = _Gs2352MLDSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6)
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMTable.setStatus("current")
_Gs2352MLDSnoopingSSMEntry_Object = MibTableRow
gs2352MLDSnoopingSSMEntry = _Gs2352MLDSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1)
)
gs2352MLDSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MLDSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMEntry.setStatus("current")


class _Gs2352MLDSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2352MLDSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MLDSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingSSMIndex_Object = MibTableColumn
gs2352MLDSnoopingSSMIndex = _Gs2352MLDSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 1),
    _Gs2352MLDSnoopingSSMIndex_Type()
)
gs2352MLDSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMIndex.setStatus("current")


class _Gs2352MLDSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2352MLDSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MLDSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingSSMVLANID_Object = MibTableColumn
gs2352MLDSnoopingSSMVLANID = _Gs2352MLDSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 2),
    _Gs2352MLDSnoopingSSMVLANID_Type()
)
gs2352MLDSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMVLANID.setStatus("current")
_Gs2352MLDSnoopingSSMGroup_Type = DisplayString
_Gs2352MLDSnoopingSSMGroup_Object = MibTableColumn
gs2352MLDSnoopingSSMGroup = _Gs2352MLDSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 3),
    _Gs2352MLDSnoopingSSMGroup_Type()
)
gs2352MLDSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMGroup.setStatus("current")


class _Gs2352MLDSnoopingSSMPort_Type(Integer32):
    """Custom type gs2352MLDSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MLDSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2352MLDSnoopingSSMPort_Object = MibTableColumn
gs2352MLDSnoopingSSMPort = _Gs2352MLDSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 4),
    _Gs2352MLDSnoopingSSMPort_Type()
)
gs2352MLDSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMPort.setStatus("current")
_Gs2352MLDSnoopingSSMMode_Type = DisplayString
_Gs2352MLDSnoopingSSMMode_Object = MibTableColumn
gs2352MLDSnoopingSSMMode = _Gs2352MLDSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 5),
    _Gs2352MLDSnoopingSSMMode_Type()
)
gs2352MLDSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMMode.setStatus("current")
_Gs2352MLDSnoopingSSMSourceAddress_Type = DisplayString
_Gs2352MLDSnoopingSSMSourceAddress_Object = MibTableColumn
gs2352MLDSnoopingSSMSourceAddress = _Gs2352MLDSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 6),
    _Gs2352MLDSnoopingSSMSourceAddress_Type()
)
gs2352MLDSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMSourceAddress.setStatus("current")
_Gs2352MLDSnoopingSSMType_Type = DisplayString
_Gs2352MLDSnoopingSSMType_Object = MibTableColumn
gs2352MLDSnoopingSSMType = _Gs2352MLDSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 17, 6, 1, 7),
    _Gs2352MLDSnoopingSSMType_Type()
)
gs2352MLDSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MLDSnoopingSSMType.setStatus("current")
_Gs2352MVR_ObjectIdentity = ObjectIdentity
gs2352MVR = _Gs2352MVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18)
)
_Gs2352MVRConfiguration_ObjectIdentity = ObjectIdentity
gs2352MVRConfiguration = _Gs2352MVRConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1)
)


class _Gs2352MVRMode_Type(Integer32):
    """Custom type gs2352MVRMode based on Integer32"""
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


_Gs2352MVRMode_Type.__name__ = "Integer32"
_Gs2352MVRMode_Object = MibScalar
gs2352MVRMode = _Gs2352MVRMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 1),
    _Gs2352MVRMode_Type()
)
gs2352MVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRMode.setStatus("current")


class _Gs2352MVRVLANId_Type(Integer32):
    """Custom type gs2352MVRVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352MVRVLANId_Type.__name__ = "Integer32"
_Gs2352MVRVLANId_Object = MibScalar
gs2352MVRVLANId = _Gs2352MVRVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 2),
    _Gs2352MVRVLANId_Type()
)
gs2352MVRVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRVLANId.setStatus("current")
_Gs2352MVRPortConfigurationTable_Object = MibTable
gs2352MVRPortConfigurationTable = _Gs2352MVRPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 3)
)
if mibBuilder.loadTexts:
    gs2352MVRPortConfigurationTable.setStatus("current")
_Gs2352MVRPortConfigurationEntry_Object = MibTableRow
gs2352MVRPortConfigurationEntry = _Gs2352MVRPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 3, 1)
)
gs2352MVRPortConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2352MVRPortConfigurationEntry.setStatus("current")


class _Gs2352MVRPortConfigurationMode_Type(Integer32):
    """Custom type gs2352MVRPortConfigurationMode based on Integer32"""
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


_Gs2352MVRPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2352MVRPortConfigurationMode_Object = MibTableColumn
gs2352MVRPortConfigurationMode = _Gs2352MVRPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 3, 1, 1),
    _Gs2352MVRPortConfigurationMode_Type()
)
gs2352MVRPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortConfigurationMode.setStatus("current")


class _Gs2352MVRPortConfigurationType_Type(Integer32):
    """Custom type gs2352MVRPortConfigurationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("receiver", 0),
          ("source", 1))
    )


_Gs2352MVRPortConfigurationType_Type.__name__ = "Integer32"
_Gs2352MVRPortConfigurationType_Object = MibTableColumn
gs2352MVRPortConfigurationType = _Gs2352MVRPortConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 3, 1, 2),
    _Gs2352MVRPortConfigurationType_Type()
)
gs2352MVRPortConfigurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortConfigurationType.setStatus("current")


class _Gs2352MVRPortConfigurationImmediateLeave_Type(Integer32):
    """Custom type gs2352MVRPortConfigurationImmediateLeave based on Integer32"""
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


_Gs2352MVRPortConfigurationImmediateLeave_Type.__name__ = "Integer32"
_Gs2352MVRPortConfigurationImmediateLeave_Object = MibTableColumn
gs2352MVRPortConfigurationImmediateLeave = _Gs2352MVRPortConfigurationImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 1, 3, 1, 3),
    _Gs2352MVRPortConfigurationImmediateLeave_Type()
)
gs2352MVRPortConfigurationImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortConfigurationImmediateLeave.setStatus("current")
_Gs2352MVRPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2352MVRPortGroupFiltering = _Gs2352MVRPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2)
)
_Gs2352MVRPortGroupFilteringCreate_Type = Integer32
_Gs2352MVRPortGroupFilteringCreate_Object = MibScalar
gs2352MVRPortGroupFilteringCreate = _Gs2352MVRPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 1),
    _Gs2352MVRPortGroupFilteringCreate_Type()
)
gs2352MVRPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringCreate.setStatus("current")
_Gs2352MVRPortGroupFilteringTable_Object = MibTable
gs2352MVRPortGroupFilteringTable = _Gs2352MVRPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringTable.setStatus("current")
_Gs2352MVRPortGroupFilteringEntry_Object = MibTableRow
gs2352MVRPortGroupFilteringEntry = _Gs2352MVRPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2, 1)
)
gs2352MVRPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MVRPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringEntry.setStatus("current")


class _Gs2352MVRPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2352MVRPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MVRPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2352MVRPortGroupFilteringIndex_Object = MibTableColumn
gs2352MVRPortGroupFilteringIndex = _Gs2352MVRPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2, 1, 1),
    _Gs2352MVRPortGroupFilteringIndex_Type()
)
gs2352MVRPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringIndex.setStatus("current")


class _Gs2352MVRPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2352MVRPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MVRPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2352MVRPortGroupFilteringPort_Object = MibTableColumn
gs2352MVRPortGroupFilteringPort = _Gs2352MVRPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2, 1, 2),
    _Gs2352MVRPortGroupFilteringPort_Type()
)
gs2352MVRPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringPort.setStatus("current")
_Gs2352MVRPortGroupFilteringStartGroups_Type = DisplayString
_Gs2352MVRPortGroupFilteringStartGroups_Object = MibTableColumn
gs2352MVRPortGroupFilteringStartGroups = _Gs2352MVRPortGroupFilteringStartGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2, 1, 3),
    _Gs2352MVRPortGroupFilteringStartGroups_Type()
)
gs2352MVRPortGroupFilteringStartGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringStartGroups.setStatus("current")
_Gs2352MVRPortGroupFilteringEndGroups_Type = DisplayString
_Gs2352MVRPortGroupFilteringEndGroups_Object = MibTableColumn
gs2352MVRPortGroupFilteringEndGroups = _Gs2352MVRPortGroupFilteringEndGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2, 1, 4),
    _Gs2352MVRPortGroupFilteringEndGroups_Type()
)
gs2352MVRPortGroupFilteringEndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringEndGroups.setStatus("current")


class _Gs2352MVRPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2352MVRPortGroupFilteringRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4))
    )


_Gs2352MVRPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2352MVRPortGroupFilteringRowStatus_Object = MibTableColumn
gs2352MVRPortGroupFilteringRowStatus = _Gs2352MVRPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 2, 2, 1, 5),
    _Gs2352MVRPortGroupFilteringRowStatus_Type()
)
gs2352MVRPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRPortGroupFilteringRowStatus.setStatus("current")
_Gs2352MVRGroupsTable_Object = MibTable
gs2352MVRGroupsTable = _Gs2352MVRGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gs2352MVRGroupsTable.setStatus("current")
_Gs2352MVRGroupsEntry_Object = MibTableRow
gs2352MVRGroupsEntry = _Gs2352MVRGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 3, 1)
)
gs2352MVRGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MVRGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2352MVRGroupsEntry.setStatus("current")


class _Gs2352MVRGroupsIndex_Type(Integer32):
    """Custom type gs2352MVRGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352MVRGroupsIndex_Type.__name__ = "Integer32"
_Gs2352MVRGroupsIndex_Object = MibTableColumn
gs2352MVRGroupsIndex = _Gs2352MVRGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 3, 1, 1),
    _Gs2352MVRGroupsIndex_Type()
)
gs2352MVRGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MVRGroupsIndex.setStatus("current")


class _Gs2352MVRGroupsVLANID_Type(Integer32):
    """Custom type gs2352MVRGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MVRGroupsVLANID_Type.__name__ = "Integer32"
_Gs2352MVRGroupsVLANID_Object = MibTableColumn
gs2352MVRGroupsVLANID = _Gs2352MVRGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 3, 1, 2),
    _Gs2352MVRGroupsVLANID_Type()
)
gs2352MVRGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRGroupsVLANID.setStatus("current")
_Gs2352MVRGroups_Type = DisplayString
_Gs2352MVRGroups_Object = MibTableColumn
gs2352MVRGroups = _Gs2352MVRGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 3, 1, 3),
    _Gs2352MVRGroups_Type()
)
gs2352MVRGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRGroups.setStatus("current")
_Gs2352MVRGroupsMemberships_Type = DisplayString
_Gs2352MVRGroupsMemberships_Object = MibTableColumn
gs2352MVRGroupsMemberships = _Gs2352MVRGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 3, 1, 4),
    _Gs2352MVRGroupsMemberships_Type()
)
gs2352MVRGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRGroupsMemberships.setStatus("current")
_Gs2352MVRStatus_ObjectIdentity = ObjectIdentity
gs2352MVRStatus = _Gs2352MVRStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4)
)


class _Gs2352MVRstatisticClear_Type(Integer32):
    """Custom type gs2352MVRstatisticClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352MVRstatisticClear_Type.__name__ = "Integer32"
_Gs2352MVRstatisticClear_Object = MibScalar
gs2352MVRstatisticClear = _Gs2352MVRstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4, 1),
    _Gs2352MVRstatisticClear_Type()
)
gs2352MVRstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352MVRstatisticClear.setStatus("current")


class _Gs2352MVRstatisticVLANID_Type(Integer32):
    """Custom type gs2352MVRstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MVRstatisticVLANID_Type.__name__ = "Integer32"
_Gs2352MVRstatisticVLANID_Object = MibScalar
gs2352MVRstatisticVLANID = _Gs2352MVRstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4, 2),
    _Gs2352MVRstatisticVLANID_Type()
)
gs2352MVRstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRstatisticVLANID.setStatus("current")
_Gs2352MVRstatisticV1ReportsReceived_Type = Counter32
_Gs2352MVRstatisticV1ReportsReceived_Object = MibScalar
gs2352MVRstatisticV1ReportsReceived = _Gs2352MVRstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4, 3),
    _Gs2352MVRstatisticV1ReportsReceived_Type()
)
gs2352MVRstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRstatisticV1ReportsReceived.setStatus("current")
_Gs2352MVRstatisticV2ReportsReceived_Type = Counter32
_Gs2352MVRstatisticV2ReportsReceived_Object = MibScalar
gs2352MVRstatisticV2ReportsReceived = _Gs2352MVRstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4, 4),
    _Gs2352MVRstatisticV2ReportsReceived_Type()
)
gs2352MVRstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRstatisticV2ReportsReceived.setStatus("current")
_Gs2352MVRstatisticV3ReportsReceived_Type = Counter32
_Gs2352MVRstatisticV3ReportsReceived_Object = MibScalar
gs2352MVRstatisticV3ReportsReceived = _Gs2352MVRstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4, 5),
    _Gs2352MVRstatisticV3ReportsReceived_Type()
)
gs2352MVRstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRstatisticV3ReportsReceived.setStatus("current")
_Gs2352MVRstatisticV2LeavesReceived_Type = Counter32
_Gs2352MVRstatisticV2LeavesReceived_Object = MibScalar
gs2352MVRstatisticV2LeavesReceived = _Gs2352MVRstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 18, 4, 6),
    _Gs2352MVRstatisticV2LeavesReceived_Type()
)
gs2352MVRstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MVRstatisticV2LeavesReceived.setStatus("current")
_Gs2352LACP_ObjectIdentity = ObjectIdentity
gs2352LACP = _Gs2352LACP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19)
)
_Gs2352LACPConf_ObjectIdentity = ObjectIdentity
gs2352LACPConf = _Gs2352LACPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1)
)
_Gs2352LACPPortConfigurationTable_Object = MibTable
gs2352LACPPortConfigurationTable = _Gs2352LACPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    gs2352LACPPortConfigurationTable.setStatus("current")
_Gs2352LACPPortConfigurationEntry_Object = MibTableRow
gs2352LACPPortConfigurationEntry = _Gs2352LACPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1, 1, 1)
)
gs2352LACPPortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352LACPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2352LACPPortConfigurationEntry.setStatus("current")


class _Gs2352LACPPortConfigurationPort_Type(Integer32):
    """Custom type gs2352LACPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352LACPPortConfigurationPort_Type.__name__ = "Integer32"
_Gs2352LACPPortConfigurationPort_Object = MibTableColumn
gs2352LACPPortConfigurationPort = _Gs2352LACPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1, 1, 1, 1),
    _Gs2352LACPPortConfigurationPort_Type()
)
gs2352LACPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352LACPPortConfigurationPort.setStatus("current")


class _Gs2352LACPPortConfigurationMode_Type(Integer32):
    """Custom type gs2352LACPPortConfigurationMode based on Integer32"""
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


_Gs2352LACPPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2352LACPPortConfigurationMode_Object = MibTableColumn
gs2352LACPPortConfigurationMode = _Gs2352LACPPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1, 1, 1, 2),
    _Gs2352LACPPortConfigurationMode_Type()
)
gs2352LACPPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LACPPortConfigurationMode.setStatus("current")


class _Gs2352LACPPortConfigurationKey_Type(Integer32):
    """Custom type gs2352LACPPortConfigurationKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2352LACPPortConfigurationKey_Type.__name__ = "Integer32"
_Gs2352LACPPortConfigurationKey_Object = MibTableColumn
gs2352LACPPortConfigurationKey = _Gs2352LACPPortConfigurationKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1, 1, 1, 3),
    _Gs2352LACPPortConfigurationKey_Type()
)
gs2352LACPPortConfigurationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LACPPortConfigurationKey.setStatus("current")


class _Gs2352LACPPortConfigurationRole_Type(Integer32):
    """Custom type gs2352LACPPortConfigurationRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("active", 1))
    )


_Gs2352LACPPortConfigurationRole_Type.__name__ = "Integer32"
_Gs2352LACPPortConfigurationRole_Object = MibTableColumn
gs2352LACPPortConfigurationRole = _Gs2352LACPPortConfigurationRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 1, 1, 1, 4),
    _Gs2352LACPPortConfigurationRole_Type()
)
gs2352LACPPortConfigurationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LACPPortConfigurationRole.setStatus("current")
_Gs2352LACPSystemStatusTable_Object = MibTable
gs2352LACPSystemStatusTable = _Gs2352LACPSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusTable.setStatus("current")
_Gs2352LACPSystemStatusEntry_Object = MibTableRow
gs2352LACPSystemStatusEntry = _Gs2352LACPSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1)
)
gs2352LACPSystemStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352LACPSystemStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusEntry.setStatus("current")


class _Gs2352LACPSystemStatusIndex_Type(Integer32):
    """Custom type gs2352LACPSystemStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2352LACPSystemStatusIndex_Type.__name__ = "Integer32"
_Gs2352LACPSystemStatusIndex_Object = MibTableColumn
gs2352LACPSystemStatusIndex = _Gs2352LACPSystemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1, 1),
    _Gs2352LACPSystemStatusIndex_Type()
)
gs2352LACPSystemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusIndex.setStatus("current")
_Gs2352LACPSystemStatusAggrID_Type = DisplayString
_Gs2352LACPSystemStatusAggrID_Object = MibTableColumn
gs2352LACPSystemStatusAggrID = _Gs2352LACPSystemStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1, 2),
    _Gs2352LACPSystemStatusAggrID_Type()
)
gs2352LACPSystemStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusAggrID.setStatus("current")
_Gs2352LACPSystemStatusPartnerSystemID_Type = MacAddress
_Gs2352LACPSystemStatusPartnerSystemID_Object = MibTableColumn
gs2352LACPSystemStatusPartnerSystemID = _Gs2352LACPSystemStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1, 3),
    _Gs2352LACPSystemStatusPartnerSystemID_Type()
)
gs2352LACPSystemStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusPartnerSystemID.setStatus("current")
_Gs2352LACPSystemStatusPartnerKey_Type = DisplayString
_Gs2352LACPSystemStatusPartnerKey_Object = MibTableColumn
gs2352LACPSystemStatusPartnerKey = _Gs2352LACPSystemStatusPartnerKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1, 4),
    _Gs2352LACPSystemStatusPartnerKey_Type()
)
gs2352LACPSystemStatusPartnerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusPartnerKey.setStatus("current")
_Gs2352LACPSystemStatusLastchanged_Type = DisplayString
_Gs2352LACPSystemStatusLastchanged_Object = MibTableColumn
gs2352LACPSystemStatusLastchanged = _Gs2352LACPSystemStatusLastchanged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1, 5),
    _Gs2352LACPSystemStatusLastchanged_Type()
)
gs2352LACPSystemStatusLastchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusLastchanged.setStatus("current")
_Gs2352LACPSystemStatusLocalPorts_Type = DisplayString
_Gs2352LACPSystemStatusLocalPorts_Object = MibTableColumn
gs2352LACPSystemStatusLocalPorts = _Gs2352LACPSystemStatusLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 2, 1, 6),
    _Gs2352LACPSystemStatusLocalPorts_Type()
)
gs2352LACPSystemStatusLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPSystemStatusLocalPorts.setStatus("current")
_Gs2352LACPStatusTable_Object = MibTable
gs2352LACPStatusTable = _Gs2352LACPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gs2352LACPStatusTable.setStatus("current")
_Gs2352LACPStatusEntry_Object = MibTableRow
gs2352LACPStatusEntry = _Gs2352LACPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1)
)
gs2352LACPStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352LACPStatusPort"),
)
if mibBuilder.loadTexts:
    gs2352LACPStatusEntry.setStatus("current")


class _Gs2352LACPStatusPort_Type(Integer32):
    """Custom type gs2352LACPStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352LACPStatusPort_Type.__name__ = "Integer32"
_Gs2352LACPStatusPort_Object = MibTableColumn
gs2352LACPStatusPort = _Gs2352LACPStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1, 1),
    _Gs2352LACPStatusPort_Type()
)
gs2352LACPStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352LACPStatusPort.setStatus("current")
_Gs2352LACPStatusLACP_Type = DisplayString
_Gs2352LACPStatusLACP_Object = MibTableColumn
gs2352LACPStatusLACP = _Gs2352LACPStatusLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1, 2),
    _Gs2352LACPStatusLACP_Type()
)
gs2352LACPStatusLACP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPStatusLACP.setStatus("current")
_Gs2352LACPStatusKey_Type = DisplayString
_Gs2352LACPStatusKey_Object = MibTableColumn
gs2352LACPStatusKey = _Gs2352LACPStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1, 3),
    _Gs2352LACPStatusKey_Type()
)
gs2352LACPStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPStatusKey.setStatus("current")
_Gs2352LACPStatusAggrID_Type = DisplayString
_Gs2352LACPStatusAggrID_Object = MibTableColumn
gs2352LACPStatusAggrID = _Gs2352LACPStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1, 4),
    _Gs2352LACPStatusAggrID_Type()
)
gs2352LACPStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPStatusAggrID.setStatus("current")
_Gs2352LACPStatusPartnerSystemID_Type = DisplayString
_Gs2352LACPStatusPartnerSystemID_Object = MibTableColumn
gs2352LACPStatusPartnerSystemID = _Gs2352LACPStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1, 5),
    _Gs2352LACPStatusPartnerSystemID_Type()
)
gs2352LACPStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPStatusPartnerSystemID.setStatus("current")
_Gs2352LACPStatusPartnerPort_Type = DisplayString
_Gs2352LACPStatusPartnerPort_Object = MibTableColumn
gs2352LACPStatusPartnerPort = _Gs2352LACPStatusPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 3, 1, 6),
    _Gs2352LACPStatusPartnerPort_Type()
)
gs2352LACPStatusPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPStatusPartnerPort.setStatus("current")
_Gs2352LACPStatisticsTable_Object = MibTable
gs2352LACPStatisticsTable = _Gs2352LACPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4)
)
if mibBuilder.loadTexts:
    gs2352LACPStatisticsTable.setStatus("current")
_Gs2352LACPStatisticsEntry_Object = MibTableRow
gs2352LACPStatisticsEntry = _Gs2352LACPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4, 1)
)
gs2352LACPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352LACPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2352LACPStatisticsEntry.setStatus("current")


class _Gs2352LACPStatisticsPort_Type(Integer32):
    """Custom type gs2352LACPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352LACPStatisticsPort_Type.__name__ = "Integer32"
_Gs2352LACPStatisticsPort_Object = MibTableColumn
gs2352LACPStatisticsPort = _Gs2352LACPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4, 1, 1),
    _Gs2352LACPStatisticsPort_Type()
)
gs2352LACPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352LACPStatisticsPort.setStatus("current")
_Gs2352LACPReceived_Type = Counter32
_Gs2352LACPReceived_Object = MibTableColumn
gs2352LACPReceived = _Gs2352LACPReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4, 1, 2),
    _Gs2352LACPReceived_Type()
)
gs2352LACPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPReceived.setStatus("current")
_Gs2352LACPTransmitted_Type = Counter32
_Gs2352LACPTransmitted_Object = MibTableColumn
gs2352LACPTransmitted = _Gs2352LACPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4, 1, 3),
    _Gs2352LACPTransmitted_Type()
)
gs2352LACPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPTransmitted.setStatus("current")
_Gs2352LACPDiscardedUnknown_Type = Counter32
_Gs2352LACPDiscardedUnknown_Object = MibTableColumn
gs2352LACPDiscardedUnknown = _Gs2352LACPDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4, 1, 4),
    _Gs2352LACPDiscardedUnknown_Type()
)
gs2352LACPDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPDiscardedUnknown.setStatus("current")
_Gs2352LACPDiscardedIllegal_Type = Counter32
_Gs2352LACPDiscardedIllegal_Object = MibTableColumn
gs2352LACPDiscardedIllegal = _Gs2352LACPDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 4, 1, 5),
    _Gs2352LACPDiscardedIllegal_Type()
)
gs2352LACPDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LACPDiscardedIllegal.setStatus("current")


class _Gs2352LACPStatisticsClear_Type(Integer32):
    """Custom type gs2352LACPStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352LACPStatisticsClear_Type.__name__ = "Integer32"
_Gs2352LACPStatisticsClear_Object = MibScalar
gs2352LACPStatisticsClear = _Gs2352LACPStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 19, 5),
    _Gs2352LACPStatisticsClear_Type()
)
gs2352LACPStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LACPStatisticsClear.setStatus("current")
_Gs2352STP_ObjectIdentity = ObjectIdentity
gs2352STP = _Gs2352STP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20)
)
_Gs2352STPBridgeBasicConf_ObjectIdentity = ObjectIdentity
gs2352STPBridgeBasicConf = _Gs2352STPBridgeBasicConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1)
)


class _Gs2352STPBridgeProtocolVersion_Type(Integer32):
    """Custom type gs2352STPBridgeProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp", 0),
          ("rstp", 2),
          ("mstp", 3))
    )


_Gs2352STPBridgeProtocolVersion_Type.__name__ = "Integer32"
_Gs2352STPBridgeProtocolVersion_Object = MibScalar
gs2352STPBridgeProtocolVersion = _Gs2352STPBridgeProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1, 1),
    _Gs2352STPBridgeProtocolVersion_Type()
)
gs2352STPBridgeProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeProtocolVersion.setStatus("current")


class _Gs2352STPBridgePriority_Type(Integer32):
    """Custom type gs2352STPBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPBridgePriority_Type.__name__ = "Integer32"
_Gs2352STPBridgePriority_Object = MibScalar
gs2352STPBridgePriority = _Gs2352STPBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1, 2),
    _Gs2352STPBridgePriority_Type()
)
gs2352STPBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgePriority.setStatus("current")


class _Gs2352STPBridgeForwardDelay_Type(Integer32):
    """Custom type gs2352STPBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Gs2352STPBridgeForwardDelay_Type.__name__ = "Integer32"
_Gs2352STPBridgeForwardDelay_Object = MibScalar
gs2352STPBridgeForwardDelay = _Gs2352STPBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1, 3),
    _Gs2352STPBridgeForwardDelay_Type()
)
gs2352STPBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeForwardDelay.setStatus("current")


class _Gs2352STPBridgeMaxAge_Type(Integer32):
    """Custom type gs2352STPBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2352STPBridgeMaxAge_Type.__name__ = "Integer32"
_Gs2352STPBridgeMaxAge_Object = MibScalar
gs2352STPBridgeMaxAge = _Gs2352STPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1, 4),
    _Gs2352STPBridgeMaxAge_Type()
)
gs2352STPBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeMaxAge.setStatus("current")


class _Gs2352STPBridgeMaximumHopCount_Type(Integer32):
    """Custom type gs2352STPBridgeMaximumHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2352STPBridgeMaximumHopCount_Type.__name__ = "Integer32"
_Gs2352STPBridgeMaximumHopCount_Object = MibScalar
gs2352STPBridgeMaximumHopCount = _Gs2352STPBridgeMaximumHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1, 5),
    _Gs2352STPBridgeMaximumHopCount_Type()
)
gs2352STPBridgeMaximumHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeMaximumHopCount.setStatus("current")


class _Gs2352STPBridgeTransmitHoldCount_Type(Integer32):
    """Custom type gs2352STPBridgeTransmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2352STPBridgeTransmitHoldCount_Type.__name__ = "Integer32"
_Gs2352STPBridgeTransmitHoldCount_Object = MibScalar
gs2352STPBridgeTransmitHoldCount = _Gs2352STPBridgeTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 1, 6),
    _Gs2352STPBridgeTransmitHoldCount_Type()
)
gs2352STPBridgeTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeTransmitHoldCount.setStatus("current")
_Gs2352STPBridgeAdvancedConf_ObjectIdentity = ObjectIdentity
gs2352STPBridgeAdvancedConf = _Gs2352STPBridgeAdvancedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 2)
)


class _Gs2352STPBridgeEdgePortBPDUFiltering_Type(Integer32):
    """Custom type gs2352STPBridgeEdgePortBPDUFiltering based on Integer32"""
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


_Gs2352STPBridgeEdgePortBPDUFiltering_Type.__name__ = "Integer32"
_Gs2352STPBridgeEdgePortBPDUFiltering_Object = MibScalar
gs2352STPBridgeEdgePortBPDUFiltering = _Gs2352STPBridgeEdgePortBPDUFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 2, 1),
    _Gs2352STPBridgeEdgePortBPDUFiltering_Type()
)
gs2352STPBridgeEdgePortBPDUFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeEdgePortBPDUFiltering.setStatus("current")


class _Gs2352STPBridgeEdgePortBPDUGuard_Type(Integer32):
    """Custom type gs2352STPBridgeEdgePortBPDUGuard based on Integer32"""
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


_Gs2352STPBridgeEdgePortBPDUGuard_Type.__name__ = "Integer32"
_Gs2352STPBridgeEdgePortBPDUGuard_Object = MibScalar
gs2352STPBridgeEdgePortBPDUGuard = _Gs2352STPBridgeEdgePortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 2, 2),
    _Gs2352STPBridgeEdgePortBPDUGuard_Type()
)
gs2352STPBridgeEdgePortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgeEdgePortBPDUGuard.setStatus("current")


class _Gs2352STPBridgePortErrorRecoveryTimeout_Type(Integer32):
    """Custom type gs2352STPBridgePortErrorRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Gs2352STPBridgePortErrorRecoveryTimeout_Type.__name__ = "Integer32"
_Gs2352STPBridgePortErrorRecoveryTimeout_Object = MibScalar
gs2352STPBridgePortErrorRecoveryTimeout = _Gs2352STPBridgePortErrorRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 2, 3),
    _Gs2352STPBridgePortErrorRecoveryTimeout_Type()
)
gs2352STPBridgePortErrorRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPBridgePortErrorRecoveryTimeout.setStatus("current")
_Gs2352STPMSTIConf_ObjectIdentity = ObjectIdentity
gs2352STPMSTIConf = _Gs2352STPMSTIConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 3)
)


class _Gs2352STPMSTIConfigurationName_Type(DisplayString):
    """Custom type gs2352STPMSTIConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2352STPMSTIConfigurationName_Type.__name__ = "DisplayString"
_Gs2352STPMSTIConfigurationName_Object = MibScalar
gs2352STPMSTIConfigurationName = _Gs2352STPMSTIConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 3, 1),
    _Gs2352STPMSTIConfigurationName_Type()
)
gs2352STPMSTIConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTIConfigurationName.setStatus("current")


class _Gs2352STPMSTIConfigurationRevision_Type(Integer32):
    """Custom type gs2352STPMSTIConfigurationRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2352STPMSTIConfigurationRevision_Type.__name__ = "Integer32"
_Gs2352STPMSTIConfigurationRevision_Object = MibScalar
gs2352STPMSTIConfigurationRevision = _Gs2352STPMSTIConfigurationRevision_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 3, 2),
    _Gs2352STPMSTIConfigurationRevision_Type()
)
gs2352STPMSTIConfigurationRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTIConfigurationRevision.setStatus("current")
_Gs2352STPMSTIMappingConf_ObjectIdentity = ObjectIdentity
gs2352STPMSTIMappingConf = _Gs2352STPMSTIMappingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4)
)


class _Gs2352STPMSTI1VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI1VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI1VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI1VLANsMapped_Object = MibScalar
gs2352STPMSTI1VLANsMapped = _Gs2352STPMSTI1VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 1),
    _Gs2352STPMSTI1VLANsMapped_Type()
)
gs2352STPMSTI1VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI1VLANsMapped.setStatus("current")


class _Gs2352STPMSTI2VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI2VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI2VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI2VLANsMapped_Object = MibScalar
gs2352STPMSTI2VLANsMapped = _Gs2352STPMSTI2VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 2),
    _Gs2352STPMSTI2VLANsMapped_Type()
)
gs2352STPMSTI2VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI2VLANsMapped.setStatus("current")


class _Gs2352STPMSTI3VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI3VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI3VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI3VLANsMapped_Object = MibScalar
gs2352STPMSTI3VLANsMapped = _Gs2352STPMSTI3VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 3),
    _Gs2352STPMSTI3VLANsMapped_Type()
)
gs2352STPMSTI3VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI3VLANsMapped.setStatus("current")


class _Gs2352STPMSTI4VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI4VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI4VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI4VLANsMapped_Object = MibScalar
gs2352STPMSTI4VLANsMapped = _Gs2352STPMSTI4VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 4),
    _Gs2352STPMSTI4VLANsMapped_Type()
)
gs2352STPMSTI4VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI4VLANsMapped.setStatus("current")


class _Gs2352STPMSTI5VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI5VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI5VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI5VLANsMapped_Object = MibScalar
gs2352STPMSTI5VLANsMapped = _Gs2352STPMSTI5VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 5),
    _Gs2352STPMSTI5VLANsMapped_Type()
)
gs2352STPMSTI5VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI5VLANsMapped.setStatus("current")


class _Gs2352STPMSTI6VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI6VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI6VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI6VLANsMapped_Object = MibScalar
gs2352STPMSTI6VLANsMapped = _Gs2352STPMSTI6VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 6),
    _Gs2352STPMSTI6VLANsMapped_Type()
)
gs2352STPMSTI6VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI6VLANsMapped.setStatus("current")


class _Gs2352STPMSTI7VLANsMapped_Type(DisplayString):
    """Custom type gs2352STPMSTI7VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2352STPMSTI7VLANsMapped_Type.__name__ = "DisplayString"
_Gs2352STPMSTI7VLANsMapped_Object = MibScalar
gs2352STPMSTI7VLANsMapped = _Gs2352STPMSTI7VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 4, 7),
    _Gs2352STPMSTI7VLANsMapped_Type()
)
gs2352STPMSTI7VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI7VLANsMapped.setStatus("current")
_Gs2352STPMSTIPriority_ObjectIdentity = ObjectIdentity
gs2352STPMSTIPriority = _Gs2352STPMSTIPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5)
)


class _Gs2352STPCISTPriority_Type(Integer32):
    """Custom type gs2352STPCISTPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPCISTPriority_Type.__name__ = "Integer32"
_Gs2352STPCISTPriority_Object = MibScalar
gs2352STPCISTPriority = _Gs2352STPCISTPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 1),
    _Gs2352STPCISTPriority_Type()
)
gs2352STPCISTPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTPriority.setStatus("current")


class _Gs2352STPMSTI1Priority_Type(Integer32):
    """Custom type gs2352STPMSTI1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI1Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI1Priority_Object = MibScalar
gs2352STPMSTI1Priority = _Gs2352STPMSTI1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 2),
    _Gs2352STPMSTI1Priority_Type()
)
gs2352STPMSTI1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI1Priority.setStatus("current")


class _Gs2352STPMSTI2Priority_Type(Integer32):
    """Custom type gs2352STPMSTI2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI2Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI2Priority_Object = MibScalar
gs2352STPMSTI2Priority = _Gs2352STPMSTI2Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 3),
    _Gs2352STPMSTI2Priority_Type()
)
gs2352STPMSTI2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI2Priority.setStatus("current")


class _Gs2352STPMSTI3Priority_Type(Integer32):
    """Custom type gs2352STPMSTI3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI3Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI3Priority_Object = MibScalar
gs2352STPMSTI3Priority = _Gs2352STPMSTI3Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 4),
    _Gs2352STPMSTI3Priority_Type()
)
gs2352STPMSTI3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI3Priority.setStatus("current")


class _Gs2352STPMSTI4Priority_Type(Integer32):
    """Custom type gs2352STPMSTI4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI4Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI4Priority_Object = MibScalar
gs2352STPMSTI4Priority = _Gs2352STPMSTI4Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 5),
    _Gs2352STPMSTI4Priority_Type()
)
gs2352STPMSTI4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI4Priority.setStatus("current")


class _Gs2352STPMSTI5Priority_Type(Integer32):
    """Custom type gs2352STPMSTI5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI5Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI5Priority_Object = MibScalar
gs2352STPMSTI5Priority = _Gs2352STPMSTI5Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 6),
    _Gs2352STPMSTI5Priority_Type()
)
gs2352STPMSTI5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI5Priority.setStatus("current")


class _Gs2352STPMSTI6Priority_Type(Integer32):
    """Custom type gs2352STPMSTI6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI6Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI6Priority_Object = MibScalar
gs2352STPMSTI6Priority = _Gs2352STPMSTI6Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 7),
    _Gs2352STPMSTI6Priority_Type()
)
gs2352STPMSTI6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI6Priority.setStatus("current")


class _Gs2352STPMSTI7Priority_Type(Integer32):
    """Custom type gs2352STPMSTI7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2352STPMSTI7Priority_Type.__name__ = "Integer32"
_Gs2352STPMSTI7Priority_Object = MibScalar
gs2352STPMSTI7Priority = _Gs2352STPMSTI7Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 5, 8),
    _Gs2352STPMSTI7Priority_Type()
)
gs2352STPMSTI7Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI7Priority.setStatus("current")
_Gs2352STPCISTPort_ObjectIdentity = ObjectIdentity
gs2352STPCISTPort = _Gs2352STPCISTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6)
)
_Gs2352STPCISTAggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPCISTAggregatedPort = _Gs2352STPCISTAggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1)
)


class _Gs2352STPCISTAggregatedPortSTPEnabled_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortSTPEnabled based on Integer32"""
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


_Gs2352STPCISTAggregatedPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortSTPEnabled_Object = MibScalar
gs2352STPCISTAggregatedPortSTPEnabled = _Gs2352STPCISTAggregatedPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 1),
    _Gs2352STPCISTAggregatedPortSTPEnabled_Type()
)
gs2352STPCISTAggregatedPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortSTPEnabled.setStatus("current")


class _Gs2352STPCISTAggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPCISTAggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortPathCost_Object = MibScalar
gs2352STPCISTAggregatedPortPathCost = _Gs2352STPCISTAggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 2),
    _Gs2352STPCISTAggregatedPortPathCost_Type()
)
gs2352STPCISTAggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortPathCost.setStatus("current")


class _Gs2352STPCISTAggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPCISTAggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortPriority_Object = MibScalar
gs2352STPCISTAggregatedPortPriority = _Gs2352STPCISTAggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 3),
    _Gs2352STPCISTAggregatedPortPriority_Type()
)
gs2352STPCISTAggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortPriority.setStatus("current")


class _Gs2352STPCISTAggregatedPortAdminEdge_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-edge", 0),
          ("edge", 1))
    )


_Gs2352STPCISTAggregatedPortAdminEdge_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortAdminEdge_Object = MibScalar
gs2352STPCISTAggregatedPortAdminEdge = _Gs2352STPCISTAggregatedPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 4),
    _Gs2352STPCISTAggregatedPortAdminEdge_Type()
)
gs2352STPCISTAggregatedPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortAdminEdge.setStatus("current")


class _Gs2352STPCISTAggregatedPortAutoEdge_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortAutoEdge based on Integer32"""
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


_Gs2352STPCISTAggregatedPortAutoEdge_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortAutoEdge_Object = MibScalar
gs2352STPCISTAggregatedPortAutoEdge = _Gs2352STPCISTAggregatedPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 5),
    _Gs2352STPCISTAggregatedPortAutoEdge_Type()
)
gs2352STPCISTAggregatedPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortAutoEdge.setStatus("current")


class _Gs2352STPCISTAggregatedPortRestrictedRole_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortRestrictedRole based on Integer32"""
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


_Gs2352STPCISTAggregatedPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortRestrictedRole_Object = MibScalar
gs2352STPCISTAggregatedPortRestrictedRole = _Gs2352STPCISTAggregatedPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 6),
    _Gs2352STPCISTAggregatedPortRestrictedRole_Type()
)
gs2352STPCISTAggregatedPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortRestrictedRole.setStatus("current")


class _Gs2352STPCISTAggregatedPortRestrictedTCN_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortRestrictedTCN based on Integer32"""
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


_Gs2352STPCISTAggregatedPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortRestrictedTCN_Object = MibScalar
gs2352STPCISTAggregatedPortRestrictedTCN = _Gs2352STPCISTAggregatedPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 7),
    _Gs2352STPCISTAggregatedPortRestrictedTCN_Type()
)
gs2352STPCISTAggregatedPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortRestrictedTCN.setStatus("current")


class _Gs2352STPCISTAggregatedPortBPDUGuard_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortBPDUGuard based on Integer32"""
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


_Gs2352STPCISTAggregatedPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortBPDUGuard_Object = MibScalar
gs2352STPCISTAggregatedPortBPDUGuard = _Gs2352STPCISTAggregatedPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 8),
    _Gs2352STPCISTAggregatedPortBPDUGuard_Type()
)
gs2352STPCISTAggregatedPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortBPDUGuard.setStatus("current")


class _Gs2352STPCISTAggregatedPortPointtoPoint_Type(Integer32):
    """Custom type gs2352STPCISTAggregatedPortPointtoPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcetrue", 0),
          ("forcefalse", 1),
          ("auto", 2))
    )


_Gs2352STPCISTAggregatedPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2352STPCISTAggregatedPortPointtoPoint_Object = MibScalar
gs2352STPCISTAggregatedPortPointtoPoint = _Gs2352STPCISTAggregatedPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 1, 9),
    _Gs2352STPCISTAggregatedPortPointtoPoint_Type()
)
gs2352STPCISTAggregatedPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTAggregatedPortPointtoPoint.setStatus("current")
_Gs2352STPCISTNormalPortTable_Object = MibTable
gs2352STPCISTNormalPortTable = _Gs2352STPCISTNormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2)
)
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortTable.setStatus("current")
_Gs2352STPCISTNormalPortEntry_Object = MibTableRow
gs2352STPCISTNormalPortEntry = _Gs2352STPCISTNormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1)
)
gs2352STPCISTNormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPCISTNormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortEntry.setStatus("current")


class _Gs2352STPCISTNormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPCISTNormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortConfPort_Object = MibTableColumn
gs2352STPCISTNormalPortConfPort = _Gs2352STPCISTNormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 1),
    _Gs2352STPCISTNormalPortConfPort_Type()
)
gs2352STPCISTNormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortConfPort.setStatus("current")


class _Gs2352STPCISTNormalPortSTPEnabled_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortSTPEnabled based on Integer32"""
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


_Gs2352STPCISTNormalPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortSTPEnabled_Object = MibTableColumn
gs2352STPCISTNormalPortSTPEnabled = _Gs2352STPCISTNormalPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 2),
    _Gs2352STPCISTNormalPortSTPEnabled_Type()
)
gs2352STPCISTNormalPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortSTPEnabled.setStatus("current")


class _Gs2352STPCISTNormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPCISTNormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortPathCost_Object = MibTableColumn
gs2352STPCISTNormalPortPathCost = _Gs2352STPCISTNormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 3),
    _Gs2352STPCISTNormalPortPathCost_Type()
)
gs2352STPCISTNormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortPathCost.setStatus("current")


class _Gs2352STPCISTNormalPortPriority_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPCISTNormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortPriority_Object = MibTableColumn
gs2352STPCISTNormalPortPriority = _Gs2352STPCISTNormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 4),
    _Gs2352STPCISTNormalPortPriority_Type()
)
gs2352STPCISTNormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortPriority.setStatus("current")


class _Gs2352STPCISTNormalPortAdminEdge_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-edge", 0),
          ("edge", 1))
    )


_Gs2352STPCISTNormalPortAdminEdge_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortAdminEdge_Object = MibTableColumn
gs2352STPCISTNormalPortAdminEdge = _Gs2352STPCISTNormalPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 5),
    _Gs2352STPCISTNormalPortAdminEdge_Type()
)
gs2352STPCISTNormalPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortAdminEdge.setStatus("current")


class _Gs2352STPCISTNormalPortAutoEdge_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortAutoEdge based on Integer32"""
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


_Gs2352STPCISTNormalPortAutoEdge_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortAutoEdge_Object = MibTableColumn
gs2352STPCISTNormalPortAutoEdge = _Gs2352STPCISTNormalPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 6),
    _Gs2352STPCISTNormalPortAutoEdge_Type()
)
gs2352STPCISTNormalPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortAutoEdge.setStatus("current")


class _Gs2352STPCISTNormalPortRestrictedRole_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortRestrictedRole based on Integer32"""
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


_Gs2352STPCISTNormalPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortRestrictedRole_Object = MibTableColumn
gs2352STPCISTNormalPortRestrictedRole = _Gs2352STPCISTNormalPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 7),
    _Gs2352STPCISTNormalPortRestrictedRole_Type()
)
gs2352STPCISTNormalPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortRestrictedRole.setStatus("current")


class _Gs2352STPCISTNormalPortRestrictedTCN_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortRestrictedTCN based on Integer32"""
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


_Gs2352STPCISTNormalPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortRestrictedTCN_Object = MibTableColumn
gs2352STPCISTNormalPortRestrictedTCN = _Gs2352STPCISTNormalPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 8),
    _Gs2352STPCISTNormalPortRestrictedTCN_Type()
)
gs2352STPCISTNormalPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortRestrictedTCN.setStatus("current")


class _Gs2352STPCISTNormalPortBPDUGuard_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortBPDUGuard based on Integer32"""
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


_Gs2352STPCISTNormalPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortBPDUGuard_Object = MibTableColumn
gs2352STPCISTNormalPortBPDUGuard = _Gs2352STPCISTNormalPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 9),
    _Gs2352STPCISTNormalPortBPDUGuard_Type()
)
gs2352STPCISTNormalPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortBPDUGuard.setStatus("current")


class _Gs2352STPCISTNormalPortPointtoPoint_Type(Integer32):
    """Custom type gs2352STPCISTNormalPortPointtoPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcetrue", 0),
          ("forcefalse", 1),
          ("auto", 2))
    )


_Gs2352STPCISTNormalPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2352STPCISTNormalPortPointtoPoint_Object = MibTableColumn
gs2352STPCISTNormalPortPointtoPoint = _Gs2352STPCISTNormalPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 6, 2, 1, 10),
    _Gs2352STPCISTNormalPortPointtoPoint_Type()
)
gs2352STPCISTNormalPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPCISTNormalPortPointtoPoint.setStatus("current")
_Gs2352STPMSTIPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTIPort = _Gs2352STPMSTIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7)
)
_Gs2352STPMSTI1Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI1Port = _Gs2352STPMSTI1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1)
)
_Gs2352STPMSTI1AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI1AggregatedPort = _Gs2352STPMSTI1AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 1)
)


class _Gs2352STPMSTI1AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI1AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI1AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI1AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI1AggregatedPortPathCost = _Gs2352STPMSTI1AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 1, 1),
    _Gs2352STPMSTI1AggregatedPortPathCost_Type()
)
gs2352STPMSTI1AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI1AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI1AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI1AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI1AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI1AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI1AggregatedPortPriority = _Gs2352STPMSTI1AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 1, 2),
    _Gs2352STPMSTI1AggregatedPortPriority_Type()
)
gs2352STPMSTI1AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI1AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI1NormalPortTable_Object = MibTable
gs2352STPMSTI1NormalPortTable = _Gs2352STPMSTI1NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI1NormalPortTable.setStatus("current")
_Gs2352STPMSTI1NormalPortEntry_Object = MibTableRow
gs2352STPMSTI1NormalPortEntry = _Gs2352STPMSTI1NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 2, 1)
)
gs2352STPMSTI1NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI1NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI1NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI1NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI1NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI1NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI1NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI1NormalPortConfPort = _Gs2352STPMSTI1NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 2, 1, 1),
    _Gs2352STPMSTI1NormalPortConfPort_Type()
)
gs2352STPMSTI1NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI1NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI1NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI1NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI1NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI1NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI1NormalPortPathCost = _Gs2352STPMSTI1NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 2, 1, 2),
    _Gs2352STPMSTI1NormalPortPathCost_Type()
)
gs2352STPMSTI1NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI1NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI1NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI1NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI1NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI1NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI1NormalPortPriority = _Gs2352STPMSTI1NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 1, 2, 1, 3),
    _Gs2352STPMSTI1NormalPortPriority_Type()
)
gs2352STPMSTI1NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI1NormalPortPriority.setStatus("current")
_Gs2352STPMSTI2Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI2Port = _Gs2352STPMSTI2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2)
)
_Gs2352STPMSTI2AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI2AggregatedPort = _Gs2352STPMSTI2AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 1)
)


class _Gs2352STPMSTI2AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI2AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI2AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI2AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI2AggregatedPortPathCost = _Gs2352STPMSTI2AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 1, 1),
    _Gs2352STPMSTI2AggregatedPortPathCost_Type()
)
gs2352STPMSTI2AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI2AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI2AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI2AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI2AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI2AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI2AggregatedPortPriority = _Gs2352STPMSTI2AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 1, 2),
    _Gs2352STPMSTI2AggregatedPortPriority_Type()
)
gs2352STPMSTI2AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI2AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI2NormalPortTable_Object = MibTable
gs2352STPMSTI2NormalPortTable = _Gs2352STPMSTI2NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI2NormalPortTable.setStatus("current")
_Gs2352STPMSTI2NormalPortEntry_Object = MibTableRow
gs2352STPMSTI2NormalPortEntry = _Gs2352STPMSTI2NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 2, 1)
)
gs2352STPMSTI2NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI2NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI2NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI2NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI2NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI2NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI2NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI2NormalPortConfPort = _Gs2352STPMSTI2NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 2, 1, 1),
    _Gs2352STPMSTI2NormalPortConfPort_Type()
)
gs2352STPMSTI2NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI2NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI2NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI2NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI2NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI2NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI2NormalPortPathCost = _Gs2352STPMSTI2NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 2, 1, 2),
    _Gs2352STPMSTI2NormalPortPathCost_Type()
)
gs2352STPMSTI2NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI2NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI2NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI2NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI2NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI2NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI2NormalPortPriority = _Gs2352STPMSTI2NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 2, 2, 1, 3),
    _Gs2352STPMSTI2NormalPortPriority_Type()
)
gs2352STPMSTI2NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI2NormalPortPriority.setStatus("current")
_Gs2352STPMSTI3Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI3Port = _Gs2352STPMSTI3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3)
)
_Gs2352STPMSTI3AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI3AggregatedPort = _Gs2352STPMSTI3AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 1)
)


class _Gs2352STPMSTI3AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI3AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI3AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI3AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI3AggregatedPortPathCost = _Gs2352STPMSTI3AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 1, 1),
    _Gs2352STPMSTI3AggregatedPortPathCost_Type()
)
gs2352STPMSTI3AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI3AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI3AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI3AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI3AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI3AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI3AggregatedPortPriority = _Gs2352STPMSTI3AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 1, 2),
    _Gs2352STPMSTI3AggregatedPortPriority_Type()
)
gs2352STPMSTI3AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI3AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI3NormalPortTable_Object = MibTable
gs2352STPMSTI3NormalPortTable = _Gs2352STPMSTI3NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI3NormalPortTable.setStatus("current")
_Gs2352STPMSTI3NormalPortEntry_Object = MibTableRow
gs2352STPMSTI3NormalPortEntry = _Gs2352STPMSTI3NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 2, 1)
)
gs2352STPMSTI3NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI3NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI3NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI3NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI3NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI3NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI3NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI3NormalPortConfPort = _Gs2352STPMSTI3NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 2, 1, 1),
    _Gs2352STPMSTI3NormalPortConfPort_Type()
)
gs2352STPMSTI3NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI3NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI3NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI3NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI3NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI3NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI3NormalPortPathCost = _Gs2352STPMSTI3NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 2, 1, 2),
    _Gs2352STPMSTI3NormalPortPathCost_Type()
)
gs2352STPMSTI3NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI3NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI3NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI3NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI3NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI3NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI3NormalPortPriority = _Gs2352STPMSTI3NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 3, 2, 1, 3),
    _Gs2352STPMSTI3NormalPortPriority_Type()
)
gs2352STPMSTI3NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI3NormalPortPriority.setStatus("current")
_Gs2352STPMSTI4Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI4Port = _Gs2352STPMSTI4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4)
)
_Gs2352STPMSTI4AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI4AggregatedPort = _Gs2352STPMSTI4AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 1)
)


class _Gs2352STPMSTI4AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI4AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI4AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI4AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI4AggregatedPortPathCost = _Gs2352STPMSTI4AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 1, 1),
    _Gs2352STPMSTI4AggregatedPortPathCost_Type()
)
gs2352STPMSTI4AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI4AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI4AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI4AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI4AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI4AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI4AggregatedPortPriority = _Gs2352STPMSTI4AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 1, 2),
    _Gs2352STPMSTI4AggregatedPortPriority_Type()
)
gs2352STPMSTI4AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI4AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI4NormalPortTable_Object = MibTable
gs2352STPMSTI4NormalPortTable = _Gs2352STPMSTI4NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI4NormalPortTable.setStatus("current")
_Gs2352STPMSTI4NormalPortEntry_Object = MibTableRow
gs2352STPMSTI4NormalPortEntry = _Gs2352STPMSTI4NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 2, 1)
)
gs2352STPMSTI4NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI4NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI4NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI4NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI4NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI4NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI4NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI4NormalPortConfPort = _Gs2352STPMSTI4NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 2, 1, 1),
    _Gs2352STPMSTI4NormalPortConfPort_Type()
)
gs2352STPMSTI4NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI4NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI4NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI4NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI4NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI4NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI4NormalPortPathCost = _Gs2352STPMSTI4NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 2, 1, 2),
    _Gs2352STPMSTI4NormalPortPathCost_Type()
)
gs2352STPMSTI4NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI4NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI4NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI4NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI4NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI4NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI4NormalPortPriority = _Gs2352STPMSTI4NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 4, 2, 1, 3),
    _Gs2352STPMSTI4NormalPortPriority_Type()
)
gs2352STPMSTI4NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI4NormalPortPriority.setStatus("current")
_Gs2352STPMSTI5Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI5Port = _Gs2352STPMSTI5Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5)
)
_Gs2352STPMSTI5AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI5AggregatedPort = _Gs2352STPMSTI5AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 1)
)


class _Gs2352STPMSTI5AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI5AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI5AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI5AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI5AggregatedPortPathCost = _Gs2352STPMSTI5AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 1, 1),
    _Gs2352STPMSTI5AggregatedPortPathCost_Type()
)
gs2352STPMSTI5AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI5AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI5AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI5AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI5AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI5AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI5AggregatedPortPriority = _Gs2352STPMSTI5AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 1, 2),
    _Gs2352STPMSTI5AggregatedPortPriority_Type()
)
gs2352STPMSTI5AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI5AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI5NormalPortTable_Object = MibTable
gs2352STPMSTI5NormalPortTable = _Gs2352STPMSTI5NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI5NormalPortTable.setStatus("current")
_Gs2352STPMSTI5NormalPortEntry_Object = MibTableRow
gs2352STPMSTI5NormalPortEntry = _Gs2352STPMSTI5NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 2, 1)
)
gs2352STPMSTI5NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI5NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI5NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI5NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI5NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI5NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI5NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI5NormalPortConfPort = _Gs2352STPMSTI5NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 2, 1, 1),
    _Gs2352STPMSTI5NormalPortConfPort_Type()
)
gs2352STPMSTI5NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI5NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI5NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI5NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI5NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI5NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI5NormalPortPathCost = _Gs2352STPMSTI5NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 2, 1, 2),
    _Gs2352STPMSTI5NormalPortPathCost_Type()
)
gs2352STPMSTI5NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI5NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI5NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI5NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI5NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI5NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI5NormalPortPriority = _Gs2352STPMSTI5NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 5, 2, 1, 3),
    _Gs2352STPMSTI5NormalPortPriority_Type()
)
gs2352STPMSTI5NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI5NormalPortPriority.setStatus("current")
_Gs2352STPMSTI6Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI6Port = _Gs2352STPMSTI6Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6)
)
_Gs2352STPMSTI6AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI6AggregatedPort = _Gs2352STPMSTI6AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 1)
)


class _Gs2352STPMSTI6AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI6AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI6AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI6AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI6AggregatedPortPathCost = _Gs2352STPMSTI6AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 1, 1),
    _Gs2352STPMSTI6AggregatedPortPathCost_Type()
)
gs2352STPMSTI6AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI6AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI6AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI6AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI6AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI6AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI6AggregatedPortPriority = _Gs2352STPMSTI6AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 1, 2),
    _Gs2352STPMSTI6AggregatedPortPriority_Type()
)
gs2352STPMSTI6AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI6AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI6NormalPortTable_Object = MibTable
gs2352STPMSTI6NormalPortTable = _Gs2352STPMSTI6NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI6NormalPortTable.setStatus("current")
_Gs2352STPMSTI6NormalPortEntry_Object = MibTableRow
gs2352STPMSTI6NormalPortEntry = _Gs2352STPMSTI6NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 2, 1)
)
gs2352STPMSTI6NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI6NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI6NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI6NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI6NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI6NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI6NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI6NormalPortConfPort = _Gs2352STPMSTI6NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 2, 1, 1),
    _Gs2352STPMSTI6NormalPortConfPort_Type()
)
gs2352STPMSTI6NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI6NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI6NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI6NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI6NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI6NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI6NormalPortPathCost = _Gs2352STPMSTI6NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 2, 1, 2),
    _Gs2352STPMSTI6NormalPortPathCost_Type()
)
gs2352STPMSTI6NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI6NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI6NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI6NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI6NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI6NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI6NormalPortPriority = _Gs2352STPMSTI6NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 6, 2, 1, 3),
    _Gs2352STPMSTI6NormalPortPriority_Type()
)
gs2352STPMSTI6NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI6NormalPortPriority.setStatus("current")
_Gs2352STPMSTI7Port_ObjectIdentity = ObjectIdentity
gs2352STPMSTI7Port = _Gs2352STPMSTI7Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7)
)
_Gs2352STPMSTI7AggregatedPort_ObjectIdentity = ObjectIdentity
gs2352STPMSTI7AggregatedPort = _Gs2352STPMSTI7AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 1)
)


class _Gs2352STPMSTI7AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI7AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI7AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI7AggregatedPortPathCost_Object = MibScalar
gs2352STPMSTI7AggregatedPortPathCost = _Gs2352STPMSTI7AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 1, 1),
    _Gs2352STPMSTI7AggregatedPortPathCost_Type()
)
gs2352STPMSTI7AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI7AggregatedPortPathCost.setStatus("current")


class _Gs2352STPMSTI7AggregatedPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI7AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI7AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI7AggregatedPortPriority_Object = MibScalar
gs2352STPMSTI7AggregatedPortPriority = _Gs2352STPMSTI7AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 1, 2),
    _Gs2352STPMSTI7AggregatedPortPriority_Type()
)
gs2352STPMSTI7AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI7AggregatedPortPriority.setStatus("current")
_Gs2352STPMSTI7NormalPortTable_Object = MibTable
gs2352STPMSTI7NormalPortTable = _Gs2352STPMSTI7NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 2)
)
if mibBuilder.loadTexts:
    gs2352STPMSTI7NormalPortTable.setStatus("current")
_Gs2352STPMSTI7NormalPortEntry_Object = MibTableRow
gs2352STPMSTI7NormalPortEntry = _Gs2352STPMSTI7NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 2, 1)
)
gs2352STPMSTI7NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPMSTI7NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2352STPMSTI7NormalPortEntry.setStatus("current")


class _Gs2352STPMSTI7NormalPortConfPort_Type(Integer32):
    """Custom type gs2352STPMSTI7NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPMSTI7NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2352STPMSTI7NormalPortConfPort_Object = MibTableColumn
gs2352STPMSTI7NormalPortConfPort = _Gs2352STPMSTI7NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 2, 1, 1),
    _Gs2352STPMSTI7NormalPortConfPort_Type()
)
gs2352STPMSTI7NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPMSTI7NormalPortConfPort.setStatus("current")


class _Gs2352STPMSTI7NormalPortPathCost_Type(Integer32):
    """Custom type gs2352STPMSTI7NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352STPMSTI7NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2352STPMSTI7NormalPortPathCost_Object = MibTableColumn
gs2352STPMSTI7NormalPortPathCost = _Gs2352STPMSTI7NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 2, 1, 2),
    _Gs2352STPMSTI7NormalPortPathCost_Type()
)
gs2352STPMSTI7NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI7NormalPortPathCost.setStatus("current")


class _Gs2352STPMSTI7NormalPortPriority_Type(Integer32):
    """Custom type gs2352STPMSTI7NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2352STPMSTI7NormalPortPriority_Type.__name__ = "Integer32"
_Gs2352STPMSTI7NormalPortPriority_Object = MibTableColumn
gs2352STPMSTI7NormalPortPriority = _Gs2352STPMSTI7NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 7, 7, 2, 1, 3),
    _Gs2352STPMSTI7NormalPortPriority_Type()
)
gs2352STPMSTI7NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352STPMSTI7NormalPortPriority.setStatus("current")
_Gs2352STPBridgeStatus_ObjectIdentity = ObjectIdentity
gs2352STPBridgeStatus = _Gs2352STPBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8)
)
_Gs2352CISTBridgeSTP_ObjectIdentity = ObjectIdentity
gs2352CISTBridgeSTP = _Gs2352CISTBridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1)
)
_Gs2352CISTBridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352CISTBridgeSTPStatus = _Gs2352CISTBridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1)
)
_Gs2352CISTBridgeInstance_Type = DisplayString
_Gs2352CISTBridgeInstance_Object = MibScalar
gs2352CISTBridgeInstance = _Gs2352CISTBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 1),
    _Gs2352CISTBridgeInstance_Type()
)
gs2352CISTBridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTBridgeInstance.setStatus("current")
_Gs2352CISTBridgeID_Type = DisplayString
_Gs2352CISTBridgeID_Object = MibScalar
gs2352CISTBridgeID = _Gs2352CISTBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 2),
    _Gs2352CISTBridgeID_Type()
)
gs2352CISTBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTBridgeID.setStatus("current")
_Gs2352CISTRootID_Type = DisplayString
_Gs2352CISTRootID_Object = MibScalar
gs2352CISTRootID = _Gs2352CISTRootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 3),
    _Gs2352CISTRootID_Type()
)
gs2352CISTRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTRootID.setStatus("current")
_Gs2352CISTRootPort_Type = DisplayString
_Gs2352CISTRootPort_Object = MibScalar
gs2352CISTRootPort = _Gs2352CISTRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 4),
    _Gs2352CISTRootPort_Type()
)
gs2352CISTRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTRootPort.setStatus("current")


class _Gs2352CISTRootCost_Type(Integer32):
    """Custom type gs2352CISTRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352CISTRootCost_Type.__name__ = "Integer32"
_Gs2352CISTRootCost_Object = MibScalar
gs2352CISTRootCost = _Gs2352CISTRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 5),
    _Gs2352CISTRootCost_Type()
)
gs2352CISTRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTRootCost.setStatus("current")
_Gs2352CISTRegionalRoot_Type = DisplayString
_Gs2352CISTRegionalRoot_Object = MibScalar
gs2352CISTRegionalRoot = _Gs2352CISTRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 6),
    _Gs2352CISTRegionalRoot_Type()
)
gs2352CISTRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTRegionalRoot.setStatus("current")


class _Gs2352CISTInternalRootCost_Type(Integer32):
    """Custom type gs2352CISTInternalRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352CISTInternalRootCost_Type.__name__ = "Integer32"
_Gs2352CISTInternalRootCost_Object = MibScalar
gs2352CISTInternalRootCost = _Gs2352CISTInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 7),
    _Gs2352CISTInternalRootCost_Type()
)
gs2352CISTInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTInternalRootCost.setStatus("current")
_Gs2352CISTTopologyFlag_Type = DisplayString
_Gs2352CISTTopologyFlag_Object = MibScalar
gs2352CISTTopologyFlag = _Gs2352CISTTopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 8),
    _Gs2352CISTTopologyFlag_Type()
)
gs2352CISTTopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTTopologyFlag.setStatus("current")
_Gs2352CISTTopologyChangeCount_Type = Counter32
_Gs2352CISTTopologyChangeCount_Object = MibScalar
gs2352CISTTopologyChangeCount = _Gs2352CISTTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 9),
    _Gs2352CISTTopologyChangeCount_Type()
)
gs2352CISTTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTTopologyChangeCount.setStatus("current")
_Gs2352CISTTopologyChangeLast_Type = DisplayString
_Gs2352CISTTopologyChangeLast_Object = MibScalar
gs2352CISTTopologyChangeLast = _Gs2352CISTTopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 1, 10),
    _Gs2352CISTTopologyChangeLast_Type()
)
gs2352CISTTopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTTopologyChangeLast.setStatus("current")
_Gs2352CISTPortStateTable_Object = MibTable
gs2352CISTPortStateTable = _Gs2352CISTPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352CISTPortStateTable.setStatus("current")
_Gs2352CISTPortStateEntry_Object = MibTableRow
gs2352CISTPortStateEntry = _Gs2352CISTPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1)
)
gs2352CISTPortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352CISTPortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352CISTPortStateEntry.setStatus("current")


class _Gs2352CISTPortStateIndex_Type(Integer32):
    """Custom type gs2352CISTPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352CISTPortStateIndex_Type.__name__ = "Integer32"
_Gs2352CISTPortStateIndex_Object = MibTableColumn
gs2352CISTPortStateIndex = _Gs2352CISTPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 1),
    _Gs2352CISTPortStateIndex_Type()
)
gs2352CISTPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352CISTPortStateIndex.setStatus("current")
_Gs2352CISTPortStatePort_Type = DisplayString
_Gs2352CISTPortStatePort_Object = MibTableColumn
gs2352CISTPortStatePort = _Gs2352CISTPortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 2),
    _Gs2352CISTPortStatePort_Type()
)
gs2352CISTPortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStatePort.setStatus("current")
_Gs2352CISTPortStatePortID_Type = DisplayString
_Gs2352CISTPortStatePortID_Object = MibTableColumn
gs2352CISTPortStatePortID = _Gs2352CISTPortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 3),
    _Gs2352CISTPortStatePortID_Type()
)
gs2352CISTPortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStatePortID.setStatus("current")
_Gs2352CISTPortStateRole_Type = DisplayString
_Gs2352CISTPortStateRole_Object = MibTableColumn
gs2352CISTPortStateRole = _Gs2352CISTPortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 4),
    _Gs2352CISTPortStateRole_Type()
)
gs2352CISTPortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStateRole.setStatus("current")
_Gs2352CISTPortStateState_Type = DisplayString
_Gs2352CISTPortStateState_Object = MibTableColumn
gs2352CISTPortStateState = _Gs2352CISTPortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 5),
    _Gs2352CISTPortStateState_Type()
)
gs2352CISTPortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStateState.setStatus("current")


class _Gs2352CISTPortStatePathCost_Type(Integer32):
    """Custom type gs2352CISTPortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352CISTPortStatePathCost_Type.__name__ = "Integer32"
_Gs2352CISTPortStatePathCost_Object = MibTableColumn
gs2352CISTPortStatePathCost = _Gs2352CISTPortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 6),
    _Gs2352CISTPortStatePathCost_Type()
)
gs2352CISTPortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStatePathCost.setStatus("current")
_Gs2352CISTPortStateEdge_Type = DisplayString
_Gs2352CISTPortStateEdge_Object = MibTableColumn
gs2352CISTPortStateEdge = _Gs2352CISTPortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 7),
    _Gs2352CISTPortStateEdge_Type()
)
gs2352CISTPortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStateEdge.setStatus("current")
_Gs2352CISTPortStatePoint2Point_Type = DisplayString
_Gs2352CISTPortStatePoint2Point_Object = MibTableColumn
gs2352CISTPortStatePoint2Point = _Gs2352CISTPortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 8),
    _Gs2352CISTPortStatePoint2Point_Type()
)
gs2352CISTPortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStatePoint2Point.setStatus("current")
_Gs2352CISTPortStateUptime_Type = DisplayString
_Gs2352CISTPortStateUptime_Object = MibTableColumn
gs2352CISTPortStateUptime = _Gs2352CISTPortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 1, 2, 1, 9),
    _Gs2352CISTPortStateUptime_Type()
)
gs2352CISTPortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352CISTPortStateUptime.setStatus("current")
_Gs2352MSTI1BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI1BridgeSTP = _Gs2352MSTI1BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2)
)
_Gs2352MSTI1BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI1BridgeSTPStatus = _Gs2352MSTI1BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1)
)
_Gs2352MSTI1BridgeInstance_Type = DisplayString
_Gs2352MSTI1BridgeInstance_Object = MibScalar
gs2352MSTI1BridgeInstance = _Gs2352MSTI1BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 1),
    _Gs2352MSTI1BridgeInstance_Type()
)
gs2352MSTI1BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1BridgeInstance.setStatus("current")
_Gs2352MSTI1BridgeID_Type = DisplayString
_Gs2352MSTI1BridgeID_Object = MibScalar
gs2352MSTI1BridgeID = _Gs2352MSTI1BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 2),
    _Gs2352MSTI1BridgeID_Type()
)
gs2352MSTI1BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1BridgeID.setStatus("current")
_Gs2352MSTI1RootID_Type = DisplayString
_Gs2352MSTI1RootID_Object = MibScalar
gs2352MSTI1RootID = _Gs2352MSTI1RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 3),
    _Gs2352MSTI1RootID_Type()
)
gs2352MSTI1RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1RootID.setStatus("current")
_Gs2352MSTI1RootPort_Type = DisplayString
_Gs2352MSTI1RootPort_Object = MibScalar
gs2352MSTI1RootPort = _Gs2352MSTI1RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 4),
    _Gs2352MSTI1RootPort_Type()
)
gs2352MSTI1RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1RootPort.setStatus("current")


class _Gs2352MSTI1RootCost_Type(Integer32):
    """Custom type gs2352MSTI1RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI1RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI1RootCost_Object = MibScalar
gs2352MSTI1RootCost = _Gs2352MSTI1RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 5),
    _Gs2352MSTI1RootCost_Type()
)
gs2352MSTI1RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1RootCost.setStatus("current")
_Gs2352MSTI1TopologyFlag_Type = DisplayString
_Gs2352MSTI1TopologyFlag_Object = MibScalar
gs2352MSTI1TopologyFlag = _Gs2352MSTI1TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 8),
    _Gs2352MSTI1TopologyFlag_Type()
)
gs2352MSTI1TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1TopologyFlag.setStatus("current")
_Gs2352MSTI1TopologyChangeCount_Type = Counter32
_Gs2352MSTI1TopologyChangeCount_Object = MibScalar
gs2352MSTI1TopologyChangeCount = _Gs2352MSTI1TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 9),
    _Gs2352MSTI1TopologyChangeCount_Type()
)
gs2352MSTI1TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1TopologyChangeCount.setStatus("current")
_Gs2352MSTI1TopologyChangeLast_Type = DisplayString
_Gs2352MSTI1TopologyChangeLast_Object = MibScalar
gs2352MSTI1TopologyChangeLast = _Gs2352MSTI1TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 1, 10),
    _Gs2352MSTI1TopologyChangeLast_Type()
)
gs2352MSTI1TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1TopologyChangeLast.setStatus("current")
_Gs2352MSTI1PortStateTable_Object = MibTable
gs2352MSTI1PortStateTable = _Gs2352MSTI1PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateTable.setStatus("current")
_Gs2352MSTI1PortStateEntry_Object = MibTableRow
gs2352MSTI1PortStateEntry = _Gs2352MSTI1PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1)
)
gs2352MSTI1PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI1PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateEntry.setStatus("current")


class _Gs2352MSTI1PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI1PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI1PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI1PortStateIndex_Object = MibTableColumn
gs2352MSTI1PortStateIndex = _Gs2352MSTI1PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 1),
    _Gs2352MSTI1PortStateIndex_Type()
)
gs2352MSTI1PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateIndex.setStatus("current")
_Gs2352MSTI1PortStatePort_Type = DisplayString
_Gs2352MSTI1PortStatePort_Object = MibTableColumn
gs2352MSTI1PortStatePort = _Gs2352MSTI1PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 2),
    _Gs2352MSTI1PortStatePort_Type()
)
gs2352MSTI1PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStatePort.setStatus("current")
_Gs2352MSTI1PortStatePortID_Type = DisplayString
_Gs2352MSTI1PortStatePortID_Object = MibTableColumn
gs2352MSTI1PortStatePortID = _Gs2352MSTI1PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 3),
    _Gs2352MSTI1PortStatePortID_Type()
)
gs2352MSTI1PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStatePortID.setStatus("current")
_Gs2352MSTI1PortStateRole_Type = DisplayString
_Gs2352MSTI1PortStateRole_Object = MibTableColumn
gs2352MSTI1PortStateRole = _Gs2352MSTI1PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 4),
    _Gs2352MSTI1PortStateRole_Type()
)
gs2352MSTI1PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateRole.setStatus("current")
_Gs2352MSTI1PortStateState_Type = DisplayString
_Gs2352MSTI1PortStateState_Object = MibTableColumn
gs2352MSTI1PortStateState = _Gs2352MSTI1PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 5),
    _Gs2352MSTI1PortStateState_Type()
)
gs2352MSTI1PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateState.setStatus("current")


class _Gs2352MSTI1PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI1PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI1PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI1PortStatePathCost_Object = MibTableColumn
gs2352MSTI1PortStatePathCost = _Gs2352MSTI1PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 6),
    _Gs2352MSTI1PortStatePathCost_Type()
)
gs2352MSTI1PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStatePathCost.setStatus("current")
_Gs2352MSTI1PortStateEdge_Type = DisplayString
_Gs2352MSTI1PortStateEdge_Object = MibTableColumn
gs2352MSTI1PortStateEdge = _Gs2352MSTI1PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 7),
    _Gs2352MSTI1PortStateEdge_Type()
)
gs2352MSTI1PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateEdge.setStatus("current")
_Gs2352MSTI1PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI1PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI1PortStatePoint2Point = _Gs2352MSTI1PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 8),
    _Gs2352MSTI1PortStatePoint2Point_Type()
)
gs2352MSTI1PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStatePoint2Point.setStatus("current")
_Gs2352MSTI1PortStateUptime_Type = DisplayString
_Gs2352MSTI1PortStateUptime_Object = MibTableColumn
gs2352MSTI1PortStateUptime = _Gs2352MSTI1PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 2, 2, 1, 9),
    _Gs2352MSTI1PortStateUptime_Type()
)
gs2352MSTI1PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI1PortStateUptime.setStatus("current")
_Gs2352MSTI2BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI2BridgeSTP = _Gs2352MSTI2BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3)
)
_Gs2352MSTI2BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI2BridgeSTPStatus = _Gs2352MSTI2BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1)
)
_Gs2352MSTI2BridgeInstance_Type = DisplayString
_Gs2352MSTI2BridgeInstance_Object = MibScalar
gs2352MSTI2BridgeInstance = _Gs2352MSTI2BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 1),
    _Gs2352MSTI2BridgeInstance_Type()
)
gs2352MSTI2BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2BridgeInstance.setStatus("current")
_Gs2352MSTI2BridgeID_Type = DisplayString
_Gs2352MSTI2BridgeID_Object = MibScalar
gs2352MSTI2BridgeID = _Gs2352MSTI2BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 2),
    _Gs2352MSTI2BridgeID_Type()
)
gs2352MSTI2BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2BridgeID.setStatus("current")
_Gs2352MSTI2RootID_Type = DisplayString
_Gs2352MSTI2RootID_Object = MibScalar
gs2352MSTI2RootID = _Gs2352MSTI2RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 3),
    _Gs2352MSTI2RootID_Type()
)
gs2352MSTI2RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2RootID.setStatus("current")
_Gs2352MSTI2RootPort_Type = DisplayString
_Gs2352MSTI2RootPort_Object = MibScalar
gs2352MSTI2RootPort = _Gs2352MSTI2RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 4),
    _Gs2352MSTI2RootPort_Type()
)
gs2352MSTI2RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2RootPort.setStatus("current")


class _Gs2352MSTI2RootCost_Type(Integer32):
    """Custom type gs2352MSTI2RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI2RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI2RootCost_Object = MibScalar
gs2352MSTI2RootCost = _Gs2352MSTI2RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 5),
    _Gs2352MSTI2RootCost_Type()
)
gs2352MSTI2RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2RootCost.setStatus("current")
_Gs2352MSTI2TopologyFlag_Type = DisplayString
_Gs2352MSTI2TopologyFlag_Object = MibScalar
gs2352MSTI2TopologyFlag = _Gs2352MSTI2TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 8),
    _Gs2352MSTI2TopologyFlag_Type()
)
gs2352MSTI2TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2TopologyFlag.setStatus("current")
_Gs2352MSTI2TopologyChangeCount_Type = Counter32
_Gs2352MSTI2TopologyChangeCount_Object = MibScalar
gs2352MSTI2TopologyChangeCount = _Gs2352MSTI2TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 9),
    _Gs2352MSTI2TopologyChangeCount_Type()
)
gs2352MSTI2TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2TopologyChangeCount.setStatus("current")
_Gs2352MSTI2TopologyChangeLast_Type = DisplayString
_Gs2352MSTI2TopologyChangeLast_Object = MibScalar
gs2352MSTI2TopologyChangeLast = _Gs2352MSTI2TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 1, 10),
    _Gs2352MSTI2TopologyChangeLast_Type()
)
gs2352MSTI2TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2TopologyChangeLast.setStatus("current")
_Gs2352MSTI2PortStateTable_Object = MibTable
gs2352MSTI2PortStateTable = _Gs2352MSTI2PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateTable.setStatus("current")
_Gs2352MSTI2PortStateEntry_Object = MibTableRow
gs2352MSTI2PortStateEntry = _Gs2352MSTI2PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1)
)
gs2352MSTI2PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI2PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateEntry.setStatus("current")


class _Gs2352MSTI2PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI2PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI2PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI2PortStateIndex_Object = MibTableColumn
gs2352MSTI2PortStateIndex = _Gs2352MSTI2PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 1),
    _Gs2352MSTI2PortStateIndex_Type()
)
gs2352MSTI2PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateIndex.setStatus("current")
_Gs2352MSTI2PortStatePort_Type = DisplayString
_Gs2352MSTI2PortStatePort_Object = MibTableColumn
gs2352MSTI2PortStatePort = _Gs2352MSTI2PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 2),
    _Gs2352MSTI2PortStatePort_Type()
)
gs2352MSTI2PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStatePort.setStatus("current")
_Gs2352MSTI2PortStatePortID_Type = DisplayString
_Gs2352MSTI2PortStatePortID_Object = MibTableColumn
gs2352MSTI2PortStatePortID = _Gs2352MSTI2PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 3),
    _Gs2352MSTI2PortStatePortID_Type()
)
gs2352MSTI2PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStatePortID.setStatus("current")
_Gs2352MSTI2PortStateRole_Type = DisplayString
_Gs2352MSTI2PortStateRole_Object = MibTableColumn
gs2352MSTI2PortStateRole = _Gs2352MSTI2PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 4),
    _Gs2352MSTI2PortStateRole_Type()
)
gs2352MSTI2PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateRole.setStatus("current")
_Gs2352MSTI2PortStateState_Type = DisplayString
_Gs2352MSTI2PortStateState_Object = MibTableColumn
gs2352MSTI2PortStateState = _Gs2352MSTI2PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 5),
    _Gs2352MSTI2PortStateState_Type()
)
gs2352MSTI2PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateState.setStatus("current")


class _Gs2352MSTI2PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI2PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI2PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI2PortStatePathCost_Object = MibTableColumn
gs2352MSTI2PortStatePathCost = _Gs2352MSTI2PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 6),
    _Gs2352MSTI2PortStatePathCost_Type()
)
gs2352MSTI2PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStatePathCost.setStatus("current")
_Gs2352MSTI2PortStateEdge_Type = DisplayString
_Gs2352MSTI2PortStateEdge_Object = MibTableColumn
gs2352MSTI2PortStateEdge = _Gs2352MSTI2PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 7),
    _Gs2352MSTI2PortStateEdge_Type()
)
gs2352MSTI2PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateEdge.setStatus("current")
_Gs2352MSTI2PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI2PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI2PortStatePoint2Point = _Gs2352MSTI2PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 8),
    _Gs2352MSTI2PortStatePoint2Point_Type()
)
gs2352MSTI2PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStatePoint2Point.setStatus("current")
_Gs2352MSTI2PortStateUptime_Type = DisplayString
_Gs2352MSTI2PortStateUptime_Object = MibTableColumn
gs2352MSTI2PortStateUptime = _Gs2352MSTI2PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 3, 2, 1, 9),
    _Gs2352MSTI2PortStateUptime_Type()
)
gs2352MSTI2PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI2PortStateUptime.setStatus("current")
_Gs2352MSTI3BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI3BridgeSTP = _Gs2352MSTI3BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4)
)
_Gs2352MSTI3BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI3BridgeSTPStatus = _Gs2352MSTI3BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1)
)
_Gs2352MSTI3BridgeInstance_Type = DisplayString
_Gs2352MSTI3BridgeInstance_Object = MibScalar
gs2352MSTI3BridgeInstance = _Gs2352MSTI3BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 1),
    _Gs2352MSTI3BridgeInstance_Type()
)
gs2352MSTI3BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3BridgeInstance.setStatus("current")
_Gs2352MSTI3BridgeID_Type = DisplayString
_Gs2352MSTI3BridgeID_Object = MibScalar
gs2352MSTI3BridgeID = _Gs2352MSTI3BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 2),
    _Gs2352MSTI3BridgeID_Type()
)
gs2352MSTI3BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3BridgeID.setStatus("current")
_Gs2352MSTI3RootID_Type = DisplayString
_Gs2352MSTI3RootID_Object = MibScalar
gs2352MSTI3RootID = _Gs2352MSTI3RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 3),
    _Gs2352MSTI3RootID_Type()
)
gs2352MSTI3RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3RootID.setStatus("current")
_Gs2352MSTI3RootPort_Type = DisplayString
_Gs2352MSTI3RootPort_Object = MibScalar
gs2352MSTI3RootPort = _Gs2352MSTI3RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 4),
    _Gs2352MSTI3RootPort_Type()
)
gs2352MSTI3RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3RootPort.setStatus("current")


class _Gs2352MSTI3RootCost_Type(Integer32):
    """Custom type gs2352MSTI3RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI3RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI3RootCost_Object = MibScalar
gs2352MSTI3RootCost = _Gs2352MSTI3RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 5),
    _Gs2352MSTI3RootCost_Type()
)
gs2352MSTI3RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3RootCost.setStatus("current")
_Gs2352MSTI3TopologyFlag_Type = DisplayString
_Gs2352MSTI3TopologyFlag_Object = MibScalar
gs2352MSTI3TopologyFlag = _Gs2352MSTI3TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 8),
    _Gs2352MSTI3TopologyFlag_Type()
)
gs2352MSTI3TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3TopologyFlag.setStatus("current")
_Gs2352MSTI3TopologyChangeCount_Type = Counter32
_Gs2352MSTI3TopologyChangeCount_Object = MibScalar
gs2352MSTI3TopologyChangeCount = _Gs2352MSTI3TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 9),
    _Gs2352MSTI3TopologyChangeCount_Type()
)
gs2352MSTI3TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3TopologyChangeCount.setStatus("current")
_Gs2352MSTI3TopologyChangeLast_Type = DisplayString
_Gs2352MSTI3TopologyChangeLast_Object = MibScalar
gs2352MSTI3TopologyChangeLast = _Gs2352MSTI3TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 1, 10),
    _Gs2352MSTI3TopologyChangeLast_Type()
)
gs2352MSTI3TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3TopologyChangeLast.setStatus("current")
_Gs2352MSTI3PortStateTable_Object = MibTable
gs2352MSTI3PortStateTable = _Gs2352MSTI3PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateTable.setStatus("current")
_Gs2352MSTI3PortStateEntry_Object = MibTableRow
gs2352MSTI3PortStateEntry = _Gs2352MSTI3PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1)
)
gs2352MSTI3PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI3PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateEntry.setStatus("current")


class _Gs2352MSTI3PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI3PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI3PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI3PortStateIndex_Object = MibTableColumn
gs2352MSTI3PortStateIndex = _Gs2352MSTI3PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 1),
    _Gs2352MSTI3PortStateIndex_Type()
)
gs2352MSTI3PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateIndex.setStatus("current")
_Gs2352MSTI3PortStatePort_Type = DisplayString
_Gs2352MSTI3PortStatePort_Object = MibTableColumn
gs2352MSTI3PortStatePort = _Gs2352MSTI3PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 2),
    _Gs2352MSTI3PortStatePort_Type()
)
gs2352MSTI3PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStatePort.setStatus("current")
_Gs2352MSTI3PortStatePortID_Type = DisplayString
_Gs2352MSTI3PortStatePortID_Object = MibTableColumn
gs2352MSTI3PortStatePortID = _Gs2352MSTI3PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 3),
    _Gs2352MSTI3PortStatePortID_Type()
)
gs2352MSTI3PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStatePortID.setStatus("current")
_Gs2352MSTI3PortStateRole_Type = DisplayString
_Gs2352MSTI3PortStateRole_Object = MibTableColumn
gs2352MSTI3PortStateRole = _Gs2352MSTI3PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 4),
    _Gs2352MSTI3PortStateRole_Type()
)
gs2352MSTI3PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateRole.setStatus("current")
_Gs2352MSTI3PortStateState_Type = DisplayString
_Gs2352MSTI3PortStateState_Object = MibTableColumn
gs2352MSTI3PortStateState = _Gs2352MSTI3PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 5),
    _Gs2352MSTI3PortStateState_Type()
)
gs2352MSTI3PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateState.setStatus("current")


class _Gs2352MSTI3PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI3PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI3PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI3PortStatePathCost_Object = MibTableColumn
gs2352MSTI3PortStatePathCost = _Gs2352MSTI3PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 6),
    _Gs2352MSTI3PortStatePathCost_Type()
)
gs2352MSTI3PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStatePathCost.setStatus("current")
_Gs2352MSTI3PortStateEdge_Type = DisplayString
_Gs2352MSTI3PortStateEdge_Object = MibTableColumn
gs2352MSTI3PortStateEdge = _Gs2352MSTI3PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 7),
    _Gs2352MSTI3PortStateEdge_Type()
)
gs2352MSTI3PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateEdge.setStatus("current")
_Gs2352MSTI3PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI3PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI3PortStatePoint2Point = _Gs2352MSTI3PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 8),
    _Gs2352MSTI3PortStatePoint2Point_Type()
)
gs2352MSTI3PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStatePoint2Point.setStatus("current")
_Gs2352MSTI3PortStateUptime_Type = DisplayString
_Gs2352MSTI3PortStateUptime_Object = MibTableColumn
gs2352MSTI3PortStateUptime = _Gs2352MSTI3PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 4, 2, 1, 9),
    _Gs2352MSTI3PortStateUptime_Type()
)
gs2352MSTI3PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI3PortStateUptime.setStatus("current")
_Gs2352MSTI4BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI4BridgeSTP = _Gs2352MSTI4BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5)
)
_Gs2352MSTI4BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI4BridgeSTPStatus = _Gs2352MSTI4BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1)
)
_Gs2352MSTI4BridgeInstance_Type = DisplayString
_Gs2352MSTI4BridgeInstance_Object = MibScalar
gs2352MSTI4BridgeInstance = _Gs2352MSTI4BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 1),
    _Gs2352MSTI4BridgeInstance_Type()
)
gs2352MSTI4BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4BridgeInstance.setStatus("current")
_Gs2352MSTI4BridgeID_Type = DisplayString
_Gs2352MSTI4BridgeID_Object = MibScalar
gs2352MSTI4BridgeID = _Gs2352MSTI4BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 2),
    _Gs2352MSTI4BridgeID_Type()
)
gs2352MSTI4BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4BridgeID.setStatus("current")
_Gs2352MSTI4RootID_Type = DisplayString
_Gs2352MSTI4RootID_Object = MibScalar
gs2352MSTI4RootID = _Gs2352MSTI4RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 3),
    _Gs2352MSTI4RootID_Type()
)
gs2352MSTI4RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4RootID.setStatus("current")
_Gs2352MSTI4RootPort_Type = DisplayString
_Gs2352MSTI4RootPort_Object = MibScalar
gs2352MSTI4RootPort = _Gs2352MSTI4RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 4),
    _Gs2352MSTI4RootPort_Type()
)
gs2352MSTI4RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4RootPort.setStatus("current")


class _Gs2352MSTI4RootCost_Type(Integer32):
    """Custom type gs2352MSTI4RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI4RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI4RootCost_Object = MibScalar
gs2352MSTI4RootCost = _Gs2352MSTI4RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 5),
    _Gs2352MSTI4RootCost_Type()
)
gs2352MSTI4RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4RootCost.setStatus("current")
_Gs2352MSTI4TopologyFlag_Type = DisplayString
_Gs2352MSTI4TopologyFlag_Object = MibScalar
gs2352MSTI4TopologyFlag = _Gs2352MSTI4TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 8),
    _Gs2352MSTI4TopologyFlag_Type()
)
gs2352MSTI4TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4TopologyFlag.setStatus("current")
_Gs2352MSTI4TopologyChangeCount_Type = Counter32
_Gs2352MSTI4TopologyChangeCount_Object = MibScalar
gs2352MSTI4TopologyChangeCount = _Gs2352MSTI4TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 9),
    _Gs2352MSTI4TopologyChangeCount_Type()
)
gs2352MSTI4TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4TopologyChangeCount.setStatus("current")
_Gs2352MSTI4TopologyChangeLast_Type = DisplayString
_Gs2352MSTI4TopologyChangeLast_Object = MibScalar
gs2352MSTI4TopologyChangeLast = _Gs2352MSTI4TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 1, 10),
    _Gs2352MSTI4TopologyChangeLast_Type()
)
gs2352MSTI4TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4TopologyChangeLast.setStatus("current")
_Gs2352MSTI4PortStateTable_Object = MibTable
gs2352MSTI4PortStateTable = _Gs2352MSTI4PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateTable.setStatus("current")
_Gs2352MSTI4PortStateEntry_Object = MibTableRow
gs2352MSTI4PortStateEntry = _Gs2352MSTI4PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1)
)
gs2352MSTI4PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI4PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateEntry.setStatus("current")


class _Gs2352MSTI4PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI4PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI4PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI4PortStateIndex_Object = MibTableColumn
gs2352MSTI4PortStateIndex = _Gs2352MSTI4PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 1),
    _Gs2352MSTI4PortStateIndex_Type()
)
gs2352MSTI4PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateIndex.setStatus("current")
_Gs2352MSTI4PortStatePort_Type = DisplayString
_Gs2352MSTI4PortStatePort_Object = MibTableColumn
gs2352MSTI4PortStatePort = _Gs2352MSTI4PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 2),
    _Gs2352MSTI4PortStatePort_Type()
)
gs2352MSTI4PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStatePort.setStatus("current")
_Gs2352MSTI4PortStatePortID_Type = DisplayString
_Gs2352MSTI4PortStatePortID_Object = MibTableColumn
gs2352MSTI4PortStatePortID = _Gs2352MSTI4PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 3),
    _Gs2352MSTI4PortStatePortID_Type()
)
gs2352MSTI4PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStatePortID.setStatus("current")
_Gs2352MSTI4PortStateRole_Type = DisplayString
_Gs2352MSTI4PortStateRole_Object = MibTableColumn
gs2352MSTI4PortStateRole = _Gs2352MSTI4PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 4),
    _Gs2352MSTI4PortStateRole_Type()
)
gs2352MSTI4PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateRole.setStatus("current")
_Gs2352MSTI4PortStateState_Type = DisplayString
_Gs2352MSTI4PortStateState_Object = MibTableColumn
gs2352MSTI4PortStateState = _Gs2352MSTI4PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 5),
    _Gs2352MSTI4PortStateState_Type()
)
gs2352MSTI4PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateState.setStatus("current")


class _Gs2352MSTI4PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI4PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI4PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI4PortStatePathCost_Object = MibTableColumn
gs2352MSTI4PortStatePathCost = _Gs2352MSTI4PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 6),
    _Gs2352MSTI4PortStatePathCost_Type()
)
gs2352MSTI4PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStatePathCost.setStatus("current")
_Gs2352MSTI4PortStateEdge_Type = DisplayString
_Gs2352MSTI4PortStateEdge_Object = MibTableColumn
gs2352MSTI4PortStateEdge = _Gs2352MSTI4PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 7),
    _Gs2352MSTI4PortStateEdge_Type()
)
gs2352MSTI4PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateEdge.setStatus("current")
_Gs2352MSTI4PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI4PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI4PortStatePoint2Point = _Gs2352MSTI4PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 8),
    _Gs2352MSTI4PortStatePoint2Point_Type()
)
gs2352MSTI4PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStatePoint2Point.setStatus("current")
_Gs2352MSTI4PortStateUptime_Type = DisplayString
_Gs2352MSTI4PortStateUptime_Object = MibTableColumn
gs2352MSTI4PortStateUptime = _Gs2352MSTI4PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 5, 2, 1, 9),
    _Gs2352MSTI4PortStateUptime_Type()
)
gs2352MSTI4PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI4PortStateUptime.setStatus("current")
_Gs2352MSTI5BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI5BridgeSTP = _Gs2352MSTI5BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6)
)
_Gs2352MSTI5BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI5BridgeSTPStatus = _Gs2352MSTI5BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1)
)
_Gs2352MSTI5BridgeInstance_Type = DisplayString
_Gs2352MSTI5BridgeInstance_Object = MibScalar
gs2352MSTI5BridgeInstance = _Gs2352MSTI5BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 1),
    _Gs2352MSTI5BridgeInstance_Type()
)
gs2352MSTI5BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5BridgeInstance.setStatus("current")
_Gs2352MSTI5BridgeID_Type = DisplayString
_Gs2352MSTI5BridgeID_Object = MibScalar
gs2352MSTI5BridgeID = _Gs2352MSTI5BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 2),
    _Gs2352MSTI5BridgeID_Type()
)
gs2352MSTI5BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5BridgeID.setStatus("current")
_Gs2352MSTI5RootID_Type = DisplayString
_Gs2352MSTI5RootID_Object = MibScalar
gs2352MSTI5RootID = _Gs2352MSTI5RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 3),
    _Gs2352MSTI5RootID_Type()
)
gs2352MSTI5RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5RootID.setStatus("current")
_Gs2352MSTI5RootPort_Type = DisplayString
_Gs2352MSTI5RootPort_Object = MibScalar
gs2352MSTI5RootPort = _Gs2352MSTI5RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 4),
    _Gs2352MSTI5RootPort_Type()
)
gs2352MSTI5RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5RootPort.setStatus("current")


class _Gs2352MSTI5RootCost_Type(Integer32):
    """Custom type gs2352MSTI5RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI5RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI5RootCost_Object = MibScalar
gs2352MSTI5RootCost = _Gs2352MSTI5RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 5),
    _Gs2352MSTI5RootCost_Type()
)
gs2352MSTI5RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5RootCost.setStatus("current")
_Gs2352MSTI5TopologyFlag_Type = DisplayString
_Gs2352MSTI5TopologyFlag_Object = MibScalar
gs2352MSTI5TopologyFlag = _Gs2352MSTI5TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 8),
    _Gs2352MSTI5TopologyFlag_Type()
)
gs2352MSTI5TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5TopologyFlag.setStatus("current")
_Gs2352MSTI5TopologyChangeCount_Type = Counter32
_Gs2352MSTI5TopologyChangeCount_Object = MibScalar
gs2352MSTI5TopologyChangeCount = _Gs2352MSTI5TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 9),
    _Gs2352MSTI5TopologyChangeCount_Type()
)
gs2352MSTI5TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5TopologyChangeCount.setStatus("current")
_Gs2352MSTI5TopologyChangeLast_Type = DisplayString
_Gs2352MSTI5TopologyChangeLast_Object = MibScalar
gs2352MSTI5TopologyChangeLast = _Gs2352MSTI5TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 1, 10),
    _Gs2352MSTI5TopologyChangeLast_Type()
)
gs2352MSTI5TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5TopologyChangeLast.setStatus("current")
_Gs2352MSTI5PortStateTable_Object = MibTable
gs2352MSTI5PortStateTable = _Gs2352MSTI5PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateTable.setStatus("current")
_Gs2352MSTI5PortStateEntry_Object = MibTableRow
gs2352MSTI5PortStateEntry = _Gs2352MSTI5PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1)
)
gs2352MSTI5PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI5PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateEntry.setStatus("current")


class _Gs2352MSTI5PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI5PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI5PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI5PortStateIndex_Object = MibTableColumn
gs2352MSTI5PortStateIndex = _Gs2352MSTI5PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 1),
    _Gs2352MSTI5PortStateIndex_Type()
)
gs2352MSTI5PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateIndex.setStatus("current")
_Gs2352MSTI5PortStatePort_Type = DisplayString
_Gs2352MSTI5PortStatePort_Object = MibTableColumn
gs2352MSTI5PortStatePort = _Gs2352MSTI5PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 2),
    _Gs2352MSTI5PortStatePort_Type()
)
gs2352MSTI5PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStatePort.setStatus("current")
_Gs2352MSTI5PortStatePortID_Type = DisplayString
_Gs2352MSTI5PortStatePortID_Object = MibTableColumn
gs2352MSTI5PortStatePortID = _Gs2352MSTI5PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 3),
    _Gs2352MSTI5PortStatePortID_Type()
)
gs2352MSTI5PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStatePortID.setStatus("current")
_Gs2352MSTI5PortStateRole_Type = DisplayString
_Gs2352MSTI5PortStateRole_Object = MibTableColumn
gs2352MSTI5PortStateRole = _Gs2352MSTI5PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 4),
    _Gs2352MSTI5PortStateRole_Type()
)
gs2352MSTI5PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateRole.setStatus("current")
_Gs2352MSTI5PortStateState_Type = DisplayString
_Gs2352MSTI5PortStateState_Object = MibTableColumn
gs2352MSTI5PortStateState = _Gs2352MSTI5PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 5),
    _Gs2352MSTI5PortStateState_Type()
)
gs2352MSTI5PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateState.setStatus("current")


class _Gs2352MSTI5PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI5PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI5PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI5PortStatePathCost_Object = MibTableColumn
gs2352MSTI5PortStatePathCost = _Gs2352MSTI5PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 6),
    _Gs2352MSTI5PortStatePathCost_Type()
)
gs2352MSTI5PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStatePathCost.setStatus("current")
_Gs2352MSTI5PortStateEdge_Type = DisplayString
_Gs2352MSTI5PortStateEdge_Object = MibTableColumn
gs2352MSTI5PortStateEdge = _Gs2352MSTI5PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 7),
    _Gs2352MSTI5PortStateEdge_Type()
)
gs2352MSTI5PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateEdge.setStatus("current")
_Gs2352MSTI5PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI5PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI5PortStatePoint2Point = _Gs2352MSTI5PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 8),
    _Gs2352MSTI5PortStatePoint2Point_Type()
)
gs2352MSTI5PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStatePoint2Point.setStatus("current")
_Gs2352MSTI5PortStateUptime_Type = DisplayString
_Gs2352MSTI5PortStateUptime_Object = MibTableColumn
gs2352MSTI5PortStateUptime = _Gs2352MSTI5PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 6, 2, 1, 9),
    _Gs2352MSTI5PortStateUptime_Type()
)
gs2352MSTI5PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI5PortStateUptime.setStatus("current")
_Gs2352MSTI6BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI6BridgeSTP = _Gs2352MSTI6BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7)
)
_Gs2352MSTI6BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI6BridgeSTPStatus = _Gs2352MSTI6BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1)
)
_Gs2352MSTI6BridgeInstance_Type = DisplayString
_Gs2352MSTI6BridgeInstance_Object = MibScalar
gs2352MSTI6BridgeInstance = _Gs2352MSTI6BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 1),
    _Gs2352MSTI6BridgeInstance_Type()
)
gs2352MSTI6BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6BridgeInstance.setStatus("current")
_Gs2352MSTI6BridgeID_Type = DisplayString
_Gs2352MSTI6BridgeID_Object = MibScalar
gs2352MSTI6BridgeID = _Gs2352MSTI6BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 2),
    _Gs2352MSTI6BridgeID_Type()
)
gs2352MSTI6BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6BridgeID.setStatus("current")
_Gs2352MSTI6RootID_Type = DisplayString
_Gs2352MSTI6RootID_Object = MibScalar
gs2352MSTI6RootID = _Gs2352MSTI6RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 3),
    _Gs2352MSTI6RootID_Type()
)
gs2352MSTI6RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6RootID.setStatus("current")
_Gs2352MSTI6RootPort_Type = DisplayString
_Gs2352MSTI6RootPort_Object = MibScalar
gs2352MSTI6RootPort = _Gs2352MSTI6RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 4),
    _Gs2352MSTI6RootPort_Type()
)
gs2352MSTI6RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6RootPort.setStatus("current")


class _Gs2352MSTI6RootCost_Type(Integer32):
    """Custom type gs2352MSTI6RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI6RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI6RootCost_Object = MibScalar
gs2352MSTI6RootCost = _Gs2352MSTI6RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 5),
    _Gs2352MSTI6RootCost_Type()
)
gs2352MSTI6RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6RootCost.setStatus("current")
_Gs2352MSTI6TopologyFlag_Type = DisplayString
_Gs2352MSTI6TopologyFlag_Object = MibScalar
gs2352MSTI6TopologyFlag = _Gs2352MSTI6TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 8),
    _Gs2352MSTI6TopologyFlag_Type()
)
gs2352MSTI6TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6TopologyFlag.setStatus("current")
_Gs2352MSTI6TopologyChangeCount_Type = Counter32
_Gs2352MSTI6TopologyChangeCount_Object = MibScalar
gs2352MSTI6TopologyChangeCount = _Gs2352MSTI6TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 9),
    _Gs2352MSTI6TopologyChangeCount_Type()
)
gs2352MSTI6TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6TopologyChangeCount.setStatus("current")
_Gs2352MSTI6TopologyChangeLast_Type = DisplayString
_Gs2352MSTI6TopologyChangeLast_Object = MibScalar
gs2352MSTI6TopologyChangeLast = _Gs2352MSTI6TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 1, 10),
    _Gs2352MSTI6TopologyChangeLast_Type()
)
gs2352MSTI6TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6TopologyChangeLast.setStatus("current")
_Gs2352MSTI6PortStateTable_Object = MibTable
gs2352MSTI6PortStateTable = _Gs2352MSTI6PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateTable.setStatus("current")
_Gs2352MSTI6PortStateEntry_Object = MibTableRow
gs2352MSTI6PortStateEntry = _Gs2352MSTI6PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1)
)
gs2352MSTI6PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI6PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateEntry.setStatus("current")


class _Gs2352MSTI6PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI6PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI6PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI6PortStateIndex_Object = MibTableColumn
gs2352MSTI6PortStateIndex = _Gs2352MSTI6PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 1),
    _Gs2352MSTI6PortStateIndex_Type()
)
gs2352MSTI6PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateIndex.setStatus("current")
_Gs2352MSTI6PortStatePort_Type = DisplayString
_Gs2352MSTI6PortStatePort_Object = MibTableColumn
gs2352MSTI6PortStatePort = _Gs2352MSTI6PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 2),
    _Gs2352MSTI6PortStatePort_Type()
)
gs2352MSTI6PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStatePort.setStatus("current")
_Gs2352MSTI6PortStatePortID_Type = DisplayString
_Gs2352MSTI6PortStatePortID_Object = MibTableColumn
gs2352MSTI6PortStatePortID = _Gs2352MSTI6PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 3),
    _Gs2352MSTI6PortStatePortID_Type()
)
gs2352MSTI6PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStatePortID.setStatus("current")
_Gs2352MSTI6PortStateRole_Type = DisplayString
_Gs2352MSTI6PortStateRole_Object = MibTableColumn
gs2352MSTI6PortStateRole = _Gs2352MSTI6PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 4),
    _Gs2352MSTI6PortStateRole_Type()
)
gs2352MSTI6PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateRole.setStatus("current")
_Gs2352MSTI6PortStateState_Type = DisplayString
_Gs2352MSTI6PortStateState_Object = MibTableColumn
gs2352MSTI6PortStateState = _Gs2352MSTI6PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 5),
    _Gs2352MSTI6PortStateState_Type()
)
gs2352MSTI6PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateState.setStatus("current")


class _Gs2352MSTI6PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI6PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI6PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI6PortStatePathCost_Object = MibTableColumn
gs2352MSTI6PortStatePathCost = _Gs2352MSTI6PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 6),
    _Gs2352MSTI6PortStatePathCost_Type()
)
gs2352MSTI6PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStatePathCost.setStatus("current")
_Gs2352MSTI6PortStateEdge_Type = DisplayString
_Gs2352MSTI6PortStateEdge_Object = MibTableColumn
gs2352MSTI6PortStateEdge = _Gs2352MSTI6PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 7),
    _Gs2352MSTI6PortStateEdge_Type()
)
gs2352MSTI6PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateEdge.setStatus("current")
_Gs2352MSTI6PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI6PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI6PortStatePoint2Point = _Gs2352MSTI6PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 8),
    _Gs2352MSTI6PortStatePoint2Point_Type()
)
gs2352MSTI6PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStatePoint2Point.setStatus("current")
_Gs2352MSTI6PortStateUptime_Type = DisplayString
_Gs2352MSTI6PortStateUptime_Object = MibTableColumn
gs2352MSTI6PortStateUptime = _Gs2352MSTI6PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 7, 2, 1, 9),
    _Gs2352MSTI6PortStateUptime_Type()
)
gs2352MSTI6PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI6PortStateUptime.setStatus("current")
_Gs2352MSTI7BridgeSTP_ObjectIdentity = ObjectIdentity
gs2352MSTI7BridgeSTP = _Gs2352MSTI7BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8)
)
_Gs2352MSTI7BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2352MSTI7BridgeSTPStatus = _Gs2352MSTI7BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1)
)
_Gs2352MSTI7BridgeInstance_Type = DisplayString
_Gs2352MSTI7BridgeInstance_Object = MibScalar
gs2352MSTI7BridgeInstance = _Gs2352MSTI7BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 1),
    _Gs2352MSTI7BridgeInstance_Type()
)
gs2352MSTI7BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7BridgeInstance.setStatus("current")
_Gs2352MSTI7BridgeID_Type = DisplayString
_Gs2352MSTI7BridgeID_Object = MibScalar
gs2352MSTI7BridgeID = _Gs2352MSTI7BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 2),
    _Gs2352MSTI7BridgeID_Type()
)
gs2352MSTI7BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7BridgeID.setStatus("current")
_Gs2352MSTI7RootID_Type = DisplayString
_Gs2352MSTI7RootID_Object = MibScalar
gs2352MSTI7RootID = _Gs2352MSTI7RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 3),
    _Gs2352MSTI7RootID_Type()
)
gs2352MSTI7RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7RootID.setStatus("current")
_Gs2352MSTI7RootPort_Type = DisplayString
_Gs2352MSTI7RootPort_Object = MibScalar
gs2352MSTI7RootPort = _Gs2352MSTI7RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 4),
    _Gs2352MSTI7RootPort_Type()
)
gs2352MSTI7RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7RootPort.setStatus("current")


class _Gs2352MSTI7RootCost_Type(Integer32):
    """Custom type gs2352MSTI7RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI7RootCost_Type.__name__ = "Integer32"
_Gs2352MSTI7RootCost_Object = MibScalar
gs2352MSTI7RootCost = _Gs2352MSTI7RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 5),
    _Gs2352MSTI7RootCost_Type()
)
gs2352MSTI7RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7RootCost.setStatus("current")
_Gs2352MSTI7TopologyFlag_Type = DisplayString
_Gs2352MSTI7TopologyFlag_Object = MibScalar
gs2352MSTI7TopologyFlag = _Gs2352MSTI7TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 8),
    _Gs2352MSTI7TopologyFlag_Type()
)
gs2352MSTI7TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7TopologyFlag.setStatus("current")
_Gs2352MSTI7TopologyChangeCount_Type = Counter32
_Gs2352MSTI7TopologyChangeCount_Object = MibScalar
gs2352MSTI7TopologyChangeCount = _Gs2352MSTI7TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 9),
    _Gs2352MSTI7TopologyChangeCount_Type()
)
gs2352MSTI7TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7TopologyChangeCount.setStatus("current")
_Gs2352MSTI7TopologyChangeLast_Type = DisplayString
_Gs2352MSTI7TopologyChangeLast_Object = MibScalar
gs2352MSTI7TopologyChangeLast = _Gs2352MSTI7TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 1, 10),
    _Gs2352MSTI7TopologyChangeLast_Type()
)
gs2352MSTI7TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7TopologyChangeLast.setStatus("current")
_Gs2352MSTI7PortStateTable_Object = MibTable
gs2352MSTI7PortStateTable = _Gs2352MSTI7PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2)
)
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateTable.setStatus("current")
_Gs2352MSTI7PortStateEntry_Object = MibTableRow
gs2352MSTI7PortStateEntry = _Gs2352MSTI7PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1)
)
gs2352MSTI7PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352MSTI7PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateEntry.setStatus("current")


class _Gs2352MSTI7PortStateIndex_Type(Integer32):
    """Custom type gs2352MSTI7PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352MSTI7PortStateIndex_Type.__name__ = "Integer32"
_Gs2352MSTI7PortStateIndex_Object = MibTableColumn
gs2352MSTI7PortStateIndex = _Gs2352MSTI7PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 1),
    _Gs2352MSTI7PortStateIndex_Type()
)
gs2352MSTI7PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateIndex.setStatus("current")
_Gs2352MSTI7PortStatePort_Type = DisplayString
_Gs2352MSTI7PortStatePort_Object = MibTableColumn
gs2352MSTI7PortStatePort = _Gs2352MSTI7PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 2),
    _Gs2352MSTI7PortStatePort_Type()
)
gs2352MSTI7PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStatePort.setStatus("current")
_Gs2352MSTI7PortStatePortID_Type = DisplayString
_Gs2352MSTI7PortStatePortID_Object = MibTableColumn
gs2352MSTI7PortStatePortID = _Gs2352MSTI7PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 3),
    _Gs2352MSTI7PortStatePortID_Type()
)
gs2352MSTI7PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStatePortID.setStatus("current")
_Gs2352MSTI7PortStateRole_Type = DisplayString
_Gs2352MSTI7PortStateRole_Object = MibTableColumn
gs2352MSTI7PortStateRole = _Gs2352MSTI7PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 4),
    _Gs2352MSTI7PortStateRole_Type()
)
gs2352MSTI7PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateRole.setStatus("current")
_Gs2352MSTI7PortStateState_Type = DisplayString
_Gs2352MSTI7PortStateState_Object = MibTableColumn
gs2352MSTI7PortStateState = _Gs2352MSTI7PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 5),
    _Gs2352MSTI7PortStateState_Type()
)
gs2352MSTI7PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateState.setStatus("current")


class _Gs2352MSTI7PortStatePathCost_Type(Integer32):
    """Custom type gs2352MSTI7PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2352MSTI7PortStatePathCost_Type.__name__ = "Integer32"
_Gs2352MSTI7PortStatePathCost_Object = MibTableColumn
gs2352MSTI7PortStatePathCost = _Gs2352MSTI7PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 6),
    _Gs2352MSTI7PortStatePathCost_Type()
)
gs2352MSTI7PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStatePathCost.setStatus("current")
_Gs2352MSTI7PortStateEdge_Type = DisplayString
_Gs2352MSTI7PortStateEdge_Object = MibTableColumn
gs2352MSTI7PortStateEdge = _Gs2352MSTI7PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 7),
    _Gs2352MSTI7PortStateEdge_Type()
)
gs2352MSTI7PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateEdge.setStatus("current")
_Gs2352MSTI7PortStatePoint2Point_Type = DisplayString
_Gs2352MSTI7PortStatePoint2Point_Object = MibTableColumn
gs2352MSTI7PortStatePoint2Point = _Gs2352MSTI7PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 8),
    _Gs2352MSTI7PortStatePoint2Point_Type()
)
gs2352MSTI7PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStatePoint2Point.setStatus("current")
_Gs2352MSTI7PortStateUptime_Type = DisplayString
_Gs2352MSTI7PortStateUptime_Object = MibTableColumn
gs2352MSTI7PortStateUptime = _Gs2352MSTI7PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 8, 8, 2, 1, 9),
    _Gs2352MSTI7PortStateUptime_Type()
)
gs2352MSTI7PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352MSTI7PortStateUptime.setStatus("current")
_Gs2352STPPortStatusTable_Object = MibTable
gs2352STPPortStatusTable = _Gs2352STPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 9)
)
if mibBuilder.loadTexts:
    gs2352STPPortStatusTable.setStatus("current")
_Gs2352STPPortStatusEntry_Object = MibTableRow
gs2352STPPortStatusEntry = _Gs2352STPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 9, 1)
)
gs2352STPPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPPortStatusPort"),
)
if mibBuilder.loadTexts:
    gs2352STPPortStatusEntry.setStatus("current")


class _Gs2352STPPortStatusPort_Type(Integer32):
    """Custom type gs2352STPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPPortStatusPort_Type.__name__ = "Integer32"
_Gs2352STPPortStatusPort_Object = MibTableColumn
gs2352STPPortStatusPort = _Gs2352STPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 9, 1, 1),
    _Gs2352STPPortStatusPort_Type()
)
gs2352STPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPPortStatusPort.setStatus("current")
_Gs2352STPPortStatusCISTRole_Type = DisplayString
_Gs2352STPPortStatusCISTRole_Object = MibTableColumn
gs2352STPPortStatusCISTRole = _Gs2352STPPortStatusCISTRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 9, 1, 2),
    _Gs2352STPPortStatusCISTRole_Type()
)
gs2352STPPortStatusCISTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPPortStatusCISTRole.setStatus("current")
_Gs2352STPPortStatusCISTState_Type = DisplayString
_Gs2352STPPortStatusCISTState_Object = MibTableColumn
gs2352STPPortStatusCISTState = _Gs2352STPPortStatusCISTState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 9, 1, 3),
    _Gs2352STPPortStatusCISTState_Type()
)
gs2352STPPortStatusCISTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPPortStatusCISTState.setStatus("current")
_Gs2352STPPortStatusUptime_Type = DisplayString
_Gs2352STPPortStatusUptime_Object = MibTableColumn
gs2352STPPortStatusUptime = _Gs2352STPPortStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 9, 1, 4),
    _Gs2352STPPortStatusUptime_Type()
)
gs2352STPPortStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPPortStatusUptime.setStatus("current")
_Gs2352STPPortStatisticsTable_Object = MibTable
gs2352STPPortStatisticsTable = _Gs2352STPPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10)
)
if mibBuilder.loadTexts:
    gs2352STPPortStatisticsTable.setStatus("current")
_Gs2352STPPortStatisticsEntry_Object = MibTableRow
gs2352STPPortStatisticsEntry = _Gs2352STPPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1)
)
gs2352STPPortStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352STPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gs2352STPPortStatisticsEntry.setStatus("current")


class _Gs2352STPStatisticsIndex_Type(Integer32):
    """Custom type gs2352STPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352STPStatisticsIndex_Type.__name__ = "Integer32"
_Gs2352STPStatisticsIndex_Object = MibTableColumn
gs2352STPStatisticsIndex = _Gs2352STPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 1),
    _Gs2352STPStatisticsIndex_Type()
)
gs2352STPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPStatisticsIndex.setStatus("current")
_Gs2352STPStatisticsPort_Type = DisplayString
_Gs2352STPStatisticsPort_Object = MibTableColumn
gs2352STPStatisticsPort = _Gs2352STPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 2),
    _Gs2352STPStatisticsPort_Type()
)
gs2352STPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352STPStatisticsPort.setStatus("current")
_Gs2352STPStatisticsTxMSTP_Type = Counter32
_Gs2352STPStatisticsTxMSTP_Object = MibTableColumn
gs2352STPStatisticsTxMSTP = _Gs2352STPStatisticsTxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 3),
    _Gs2352STPStatisticsTxMSTP_Type()
)
gs2352STPStatisticsTxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsTxMSTP.setStatus("current")
_Gs2352STPStatisticsTxRSTP_Type = Counter32
_Gs2352STPStatisticsTxRSTP_Object = MibTableColumn
gs2352STPStatisticsTxRSTP = _Gs2352STPStatisticsTxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 4),
    _Gs2352STPStatisticsTxRSTP_Type()
)
gs2352STPStatisticsTxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsTxRSTP.setStatus("current")
_Gs2352STPStatisticsTxSTP_Type = Counter32
_Gs2352STPStatisticsTxSTP_Object = MibTableColumn
gs2352STPStatisticsTxSTP = _Gs2352STPStatisticsTxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 5),
    _Gs2352STPStatisticsTxSTP_Type()
)
gs2352STPStatisticsTxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsTxSTP.setStatus("current")
_Gs2352STPStatisticsTxTCN_Type = Counter32
_Gs2352STPStatisticsTxTCN_Object = MibTableColumn
gs2352STPStatisticsTxTCN = _Gs2352STPStatisticsTxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 6),
    _Gs2352STPStatisticsTxTCN_Type()
)
gs2352STPStatisticsTxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsTxTCN.setStatus("current")
_Gs2352STPStatisticsRxMSTP_Type = Counter32
_Gs2352STPStatisticsRxMSTP_Object = MibTableColumn
gs2352STPStatisticsRxMSTP = _Gs2352STPStatisticsRxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 7),
    _Gs2352STPStatisticsRxMSTP_Type()
)
gs2352STPStatisticsRxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsRxMSTP.setStatus("current")
_Gs2352STPStatisticsRxRSTP_Type = Counter32
_Gs2352STPStatisticsRxRSTP_Object = MibTableColumn
gs2352STPStatisticsRxRSTP = _Gs2352STPStatisticsRxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 8),
    _Gs2352STPStatisticsRxRSTP_Type()
)
gs2352STPStatisticsRxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsRxRSTP.setStatus("current")
_Gs2352STPStatisticsRxSTP_Type = Counter32
_Gs2352STPStatisticsRxSTP_Object = MibTableColumn
gs2352STPStatisticsRxSTP = _Gs2352STPStatisticsRxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 9),
    _Gs2352STPStatisticsRxSTP_Type()
)
gs2352STPStatisticsRxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsRxSTP.setStatus("current")
_Gs2352STPStatisticsRxTCN_Type = Counter32
_Gs2352STPStatisticsRxTCN_Object = MibTableColumn
gs2352STPStatisticsRxTCN = _Gs2352STPStatisticsRxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 10),
    _Gs2352STPStatisticsRxTCN_Type()
)
gs2352STPStatisticsRxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsRxTCN.setStatus("current")
_Gs2352STPStatisticsDiscardedUnknown_Type = Counter32
_Gs2352STPStatisticsDiscardedUnknown_Object = MibTableColumn
gs2352STPStatisticsDiscardedUnknown = _Gs2352STPStatisticsDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 11),
    _Gs2352STPStatisticsDiscardedUnknown_Type()
)
gs2352STPStatisticsDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsDiscardedUnknown.setStatus("current")
_Gs2352STPStatisticsDiscardedIllegal_Type = Counter32
_Gs2352STPStatisticsDiscardedIllegal_Object = MibTableColumn
gs2352STPStatisticsDiscardedIllegal = _Gs2352STPStatisticsDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 20, 10, 1, 12),
    _Gs2352STPStatisticsDiscardedIllegal_Type()
)
gs2352STPStatisticsDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352STPStatisticsDiscardedIllegal.setStatus("current")
_Gs2352FilteringDataBase_ObjectIdentity = ObjectIdentity
gs2352FilteringDataBase = _Gs2352FilteringDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21)
)
_Gs2352FilteringDataBaseConfig_ObjectIdentity = ObjectIdentity
gs2352FilteringDataBaseConfig = _Gs2352FilteringDataBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1)
)


class _Gs2352FilteringDataBaseAgingTime_Type(Integer32):
    """Custom type gs2352FilteringDataBaseAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2352FilteringDataBaseAgingTime_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseAgingTime_Object = MibScalar
gs2352FilteringDataBaseAgingTime = _Gs2352FilteringDataBaseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 1),
    _Gs2352FilteringDataBaseAgingTime_Type()
)
gs2352FilteringDataBaseAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseAgingTime.setStatus("current")
_Gs2352FilteringDataBaseConfigTable_Object = MibTable
gs2352FilteringDataBaseConfigTable = _Gs2352FilteringDataBaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseConfigTable.setStatus("current")
_Gs2352FilteringDataBaseConfigEntry_Object = MibTableRow
gs2352FilteringDataBaseConfigEntry = _Gs2352FilteringDataBaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 2, 1)
)
gs2352FilteringDataBaseConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352FilteringDataBaseConfigPort"),
)
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseConfigEntry.setStatus("current")


class _Gs2352FilteringDataBaseConfigPort_Type(Integer32):
    """Custom type gs2352FilteringDataBaseConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352FilteringDataBaseConfigPort_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseConfigPort_Object = MibTableColumn
gs2352FilteringDataBaseConfigPort = _Gs2352FilteringDataBaseConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 2, 1, 1),
    _Gs2352FilteringDataBaseConfigPort_Type()
)
gs2352FilteringDataBaseConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseConfigPort.setStatus("current")


class _Gs2352FilteringDataBaseConfigLearning_Type(Integer32):
    """Custom type gs2352FilteringDataBaseConfigLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("disable", 1),
          ("secure", 2))
    )


_Gs2352FilteringDataBaseConfigLearning_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseConfigLearning_Object = MibTableColumn
gs2352FilteringDataBaseConfigLearning = _Gs2352FilteringDataBaseConfigLearning_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 2, 1, 2),
    _Gs2352FilteringDataBaseConfigLearning_Type()
)
gs2352FilteringDataBaseConfigLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseConfigLearning.setStatus("current")
_Gs2352FilteringDataBaseStaticMAC_ObjectIdentity = ObjectIdentity
gs2352FilteringDataBaseStaticMAC = _Gs2352FilteringDataBaseStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3)
)


class _Gs2352FilteringDataBaseStaticMACCreate_Type(Integer32):
    """Custom type gs2352FilteringDataBaseStaticMACCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352FilteringDataBaseStaticMACCreate_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseStaticMACCreate_Object = MibScalar
gs2352FilteringDataBaseStaticMACCreate = _Gs2352FilteringDataBaseStaticMACCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 1),
    _Gs2352FilteringDataBaseStaticMACCreate_Type()
)
gs2352FilteringDataBaseStaticMACCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACCreate.setStatus("current")
_Gs2352FilteringDataBaseStaticMACTable_Object = MibTable
gs2352FilteringDataBaseStaticMACTable = _Gs2352FilteringDataBaseStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACTable.setStatus("current")
_Gs2352FilteringDataBaseStaticMACEntry_Object = MibTableRow
gs2352FilteringDataBaseStaticMACEntry = _Gs2352FilteringDataBaseStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2, 1)
)
gs2352FilteringDataBaseStaticMACEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352FilteringDataBaseStaticMACIndex"),
)
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACEntry.setStatus("current")


class _Gs2352FilteringDataBaseStaticMACIndex_Type(Integer32):
    """Custom type gs2352FilteringDataBaseStaticMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352FilteringDataBaseStaticMACIndex_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseStaticMACIndex_Object = MibTableColumn
gs2352FilteringDataBaseStaticMACIndex = _Gs2352FilteringDataBaseStaticMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2, 1, 1),
    _Gs2352FilteringDataBaseStaticMACIndex_Type()
)
gs2352FilteringDataBaseStaticMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACIndex.setStatus("current")


class _Gs2352FilteringDataBaseStaticMACVLANId_Type(Integer32):
    """Custom type gs2352FilteringDataBaseStaticMACVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352FilteringDataBaseStaticMACVLANId_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseStaticMACVLANId_Object = MibTableColumn
gs2352FilteringDataBaseStaticMACVLANId = _Gs2352FilteringDataBaseStaticMACVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2, 1, 2),
    _Gs2352FilteringDataBaseStaticMACVLANId_Type()
)
gs2352FilteringDataBaseStaticMACVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACVLANId.setStatus("current")
_Gs2352FilteringDataBaseStaticMACAddress_Type = MacAddress
_Gs2352FilteringDataBaseStaticMACAddress_Object = MibTableColumn
gs2352FilteringDataBaseStaticMACAddress = _Gs2352FilteringDataBaseStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2, 1, 3),
    _Gs2352FilteringDataBaseStaticMACAddress_Type()
)
gs2352FilteringDataBaseStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACAddress.setStatus("current")
_Gs2352FilteringDataBaseStaticMACPortMembers_Type = DisplayString
_Gs2352FilteringDataBaseStaticMACPortMembers_Object = MibTableColumn
gs2352FilteringDataBaseStaticMACPortMembers = _Gs2352FilteringDataBaseStaticMACPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2, 1, 4),
    _Gs2352FilteringDataBaseStaticMACPortMembers_Type()
)
gs2352FilteringDataBaseStaticMACPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACPortMembers.setStatus("current")


class _Gs2352FilteringDataBaseStaticMACRowStatus_Type(Integer32):
    """Custom type gs2352FilteringDataBaseStaticMACRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352FilteringDataBaseStaticMACRowStatus_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseStaticMACRowStatus_Object = MibTableColumn
gs2352FilteringDataBaseStaticMACRowStatus = _Gs2352FilteringDataBaseStaticMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 3, 2, 1, 5),
    _Gs2352FilteringDataBaseStaticMACRowStatus_Type()
)
gs2352FilteringDataBaseStaticMACRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseStaticMACRowStatus.setStatus("current")
_Gs2352FilteringDataBaseDynamicMACTable_Object = MibTable
gs2352FilteringDataBaseDynamicMACTable = _Gs2352FilteringDataBaseDynamicMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicMACTable.setStatus("current")
_Gs2352FilteringDataBaseDynamicMACEntry_Object = MibTableRow
gs2352FilteringDataBaseDynamicMACEntry = _Gs2352FilteringDataBaseDynamicMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4, 1)
)
gs2352FilteringDataBaseDynamicMACEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352FilteringDataBaseDynamicMACIndex"),
)
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicMACEntry.setStatus("current")


class _Gs2352FilteringDataBaseDynamicMACIndex_Type(Integer32):
    """Custom type gs2352FilteringDataBaseDynamicMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352FilteringDataBaseDynamicMACIndex_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseDynamicMACIndex_Object = MibTableColumn
gs2352FilteringDataBaseDynamicMACIndex = _Gs2352FilteringDataBaseDynamicMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4, 1, 1),
    _Gs2352FilteringDataBaseDynamicMACIndex_Type()
)
gs2352FilteringDataBaseDynamicMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicMACIndex.setStatus("current")


class _Gs2352FilteringDataBaseDynamicMACType_Type(Integer32):
    """Custom type gs2352FilteringDataBaseDynamicMACType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_Gs2352FilteringDataBaseDynamicMACType_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseDynamicMACType_Object = MibTableColumn
gs2352FilteringDataBaseDynamicMACType = _Gs2352FilteringDataBaseDynamicMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4, 1, 2),
    _Gs2352FilteringDataBaseDynamicMACType_Type()
)
gs2352FilteringDataBaseDynamicMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicMACType.setStatus("current")


class _Gs2352FilteringDataBaseDynamicMACVLAN_Type(Integer32):
    """Custom type gs2352FilteringDataBaseDynamicMACVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352FilteringDataBaseDynamicMACVLAN_Type.__name__ = "Integer32"
_Gs2352FilteringDataBaseDynamicMACVLAN_Object = MibTableColumn
gs2352FilteringDataBaseDynamicMACVLAN = _Gs2352FilteringDataBaseDynamicMACVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4, 1, 3),
    _Gs2352FilteringDataBaseDynamicMACVLAN_Type()
)
gs2352FilteringDataBaseDynamicMACVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicMACVLAN.setStatus("current")
_Gs2352FilteringDataBaseDynamicMACAddress_Type = MacAddress
_Gs2352FilteringDataBaseDynamicMACAddress_Object = MibTableColumn
gs2352FilteringDataBaseDynamicMACAddress = _Gs2352FilteringDataBaseDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4, 1, 4),
    _Gs2352FilteringDataBaseDynamicMACAddress_Type()
)
gs2352FilteringDataBaseDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicMACAddress.setStatus("current")
_Gs2352FilteringDataBaseDynamicPortMembers_Type = DisplayString
_Gs2352FilteringDataBaseDynamicPortMembers_Object = MibTableColumn
gs2352FilteringDataBaseDynamicPortMembers = _Gs2352FilteringDataBaseDynamicPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 21, 1, 4, 1, 5),
    _Gs2352FilteringDataBaseDynamicPortMembers_Type()
)
gs2352FilteringDataBaseDynamicPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352FilteringDataBaseDynamicPortMembers.setStatus("current")
_Gs2352SFlowAgent_ObjectIdentity = ObjectIdentity
gs2352SFlowAgent = _Gs2352SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 22)
)
_Gs2352SFlowAgentCollector_ObjectIdentity = ObjectIdentity
gs2352SFlowAgentCollector = _Gs2352SFlowAgentCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 22, 1)
)


class _Gs2352SFlowAgentReceiverMode_Type(Integer32):
    """Custom type gs2352SFlowAgentReceiverMode based on Integer32"""
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


_Gs2352SFlowAgentReceiverMode_Type.__name__ = "Integer32"
_Gs2352SFlowAgentReceiverMode_Object = MibScalar
gs2352SFlowAgentReceiverMode = _Gs2352SFlowAgentReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 22, 1, 1),
    _Gs2352SFlowAgentReceiverMode_Type()
)
gs2352SFlowAgentReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SFlowAgentReceiverMode.setStatus("current")
_Gs2352LMC_ObjectIdentity = ObjectIdentity
gs2352LMC = _Gs2352LMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500)
)


class _Gs2352LMCOperating_Type(Integer32):
    """Custom type gs2352LMCOperating based on Integer32"""
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
          ("enabled", 1),
          ("try", 2))
    )


_Gs2352LMCOperating_Type.__name__ = "Integer32"
_Gs2352LMCOperating_Object = MibScalar
gs2352LMCOperating = _Gs2352LMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 1),
    _Gs2352LMCOperating_Type()
)
gs2352LMCOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LMCOperating.setStatus("current")


class _Gs2352LMCConfigViaDhcp_Type(Integer32):
    """Custom type gs2352LMCConfigViaDhcp based on Integer32"""
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


_Gs2352LMCConfigViaDhcp_Type.__name__ = "Integer32"
_Gs2352LMCConfigViaDhcp_Object = MibScalar
gs2352LMCConfigViaDhcp = _Gs2352LMCConfigViaDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 2),
    _Gs2352LMCConfigViaDhcp_Type()
)
gs2352LMCConfigViaDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LMCConfigViaDhcp.setStatus("current")


class _Gs2352LMCDomain_Type(DisplayString):
    """Custom type gs2352LMCDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gs2352LMCDomain_Type.__name__ = "DisplayString"
_Gs2352LMCDomain_Object = MibScalar
gs2352LMCDomain = _Gs2352LMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 3),
    _Gs2352LMCDomain_Type()
)
gs2352LMCDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LMCDomain.setStatus("current")


class _Gs2352LMCDhcpClientAutoRenew_Type(Integer32):
    """Custom type gs2352LMCDhcpClientAutoRenew based on Integer32"""
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


_Gs2352LMCDhcpClientAutoRenew_Type.__name__ = "Integer32"
_Gs2352LMCDhcpClientAutoRenew_Object = MibScalar
gs2352LMCDhcpClientAutoRenew = _Gs2352LMCDhcpClientAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 4),
    _Gs2352LMCDhcpClientAutoRenew_Type()
)
gs2352LMCDhcpClientAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LMCDhcpClientAutoRenew.setStatus("current")


class _Gs2352LMCZeroTouchSupport_Type(Integer32):
    """Custom type gs2352LMCZeroTouchSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("No", 0),
          ("Yes", 1))
    )


_Gs2352LMCZeroTouchSupport_Type.__name__ = "Integer32"
_Gs2352LMCZeroTouchSupport_Object = MibScalar
gs2352LMCZeroTouchSupport = _Gs2352LMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 50),
    _Gs2352LMCZeroTouchSupport_Type()
)
gs2352LMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCZeroTouchSupport.setStatus("current")


class _Gs2352LMCPairingTokenPresent_Type(Integer32):
    """Custom type gs2352LMCPairingTokenPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("No", 0),
          ("Yes", 1))
    )


_Gs2352LMCPairingTokenPresent_Type.__name__ = "Integer32"
_Gs2352LMCPairingTokenPresent_Object = MibScalar
gs2352LMCPairingTokenPresent = _Gs2352LMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 51),
    _Gs2352LMCPairingTokenPresent_Type()
)
gs2352LMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCPairingTokenPresent.setStatus("current")
_Gs2352LMCClientStatus_Type = DisplayString
_Gs2352LMCClientStatus_Object = MibScalar
gs2352LMCClientStatus = _Gs2352LMCClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 52),
    _Gs2352LMCClientStatus_Type()
)
gs2352LMCClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCClientStatus.setStatus("current")


class _Gs2352LMCManagementStatus_Type(Integer32):
    """Custom type gs2352LMCManagementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14)
        )
    )
    namedValues = NamedValues(
        *(("Unpaired", 0),
          ("Paired", 1),
          ("PairedAndClaimed", 14))
    )


_Gs2352LMCManagementStatus_Type.__name__ = "Integer32"
_Gs2352LMCManagementStatus_Object = MibScalar
gs2352LMCManagementStatus = _Gs2352LMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 53),
    _Gs2352LMCManagementStatus_Type()
)
gs2352LMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCManagementStatus.setStatus("current")


class _Gs2352LMCControlStatus_Type(Integer32):
    """Custom type gs2352LMCControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("Disabled", 2),
          ("Operating", 4))
    )


_Gs2352LMCControlStatus_Type.__name__ = "Integer32"
_Gs2352LMCControlStatus_Object = MibScalar
gs2352LMCControlStatus = _Gs2352LMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 54),
    _Gs2352LMCControlStatus_Type()
)
gs2352LMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCControlStatus.setStatus("current")


class _Gs2352LMCMonitoringStatus_Type(Integer32):
    """Custom type gs2352LMCMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("Disabled", 2),
          ("Operating", 4))
    )


_Gs2352LMCMonitoringStatus_Type.__name__ = "Integer32"
_Gs2352LMCMonitoringStatus_Object = MibScalar
gs2352LMCMonitoringStatus = _Gs2352LMCMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 55),
    _Gs2352LMCMonitoringStatus_Type()
)
gs2352LMCMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCMonitoringStatus.setStatus("current")
_Gs2352LMCConfigurationSource_Type = DisplayString
_Gs2352LMCConfigurationSource_Object = MibScalar
gs2352LMCConfigurationSource = _Gs2352LMCConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 56),
    _Gs2352LMCConfigurationSource_Type()
)
gs2352LMCConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCConfigurationSource.setStatus("current")


class _Gs2352LMCConfigModified_Type(Integer32):
    """Custom type gs2352LMCConfigModified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("No", 0),
          ("Yes", 1))
    )


_Gs2352LMCConfigModified_Type.__name__ = "Integer32"
_Gs2352LMCConfigModified_Object = MibScalar
gs2352LMCConfigModified = _Gs2352LMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 57),
    _Gs2352LMCConfigModified_Type()
)
gs2352LMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCConfigModified.setStatus("current")
_Gs2352LMCDeviceID_Type = DisplayString
_Gs2352LMCDeviceID_Object = MibScalar
gs2352LMCDeviceID = _Gs2352LMCDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 58),
    _Gs2352LMCDeviceID_Type()
)
gs2352LMCDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCDeviceID.setStatus("current")
_Gs2352LMCRoundTripTime_Type = Integer32
_Gs2352LMCRoundTripTime_Object = MibScalar
gs2352LMCRoundTripTime = _Gs2352LMCRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 2, 1500, 100),
    _Gs2352LMCRoundTripTime_Type()
)
gs2352LMCRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352LMCRoundTripTime.setStatus("current")
_Gs2352Security_ObjectIdentity = ObjectIdentity
gs2352Security = _Gs2352Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3)
)
_Gs2352IPSourceGuard_ObjectIdentity = ObjectIdentity
gs2352IPSourceGuard = _Gs2352IPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1)
)
_Gs2352IPSourceGuardConf_ObjectIdentity = ObjectIdentity
gs2352IPSourceGuardConf = _Gs2352IPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1)
)


class _Gs2352IPSourceGuardMode_Type(Integer32):
    """Custom type gs2352IPSourceGuardMode based on Integer32"""
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


_Gs2352IPSourceGuardMode_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardMode_Object = MibScalar
gs2352IPSourceGuardMode = _Gs2352IPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1, 1),
    _Gs2352IPSourceGuardMode_Type()
)
gs2352IPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardMode.setStatus("current")
_Gs2352IPSourceGuardPortConfigTable_Object = MibTable
gs2352IPSourceGuardPortConfigTable = _Gs2352IPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352IPSourceGuardPortConfigTable.setStatus("current")
_Gs2352IPSourceGuardPortConfigEntry_Object = MibTableRow
gs2352IPSourceGuardPortConfigEntry = _Gs2352IPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1, 2, 1)
)
gs2352IPSourceGuardPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2352IPSourceGuardPortConfigEntry.setStatus("current")


class _Gs2352IPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type gs2352IPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardPortConfigPort_Object = MibTableColumn
gs2352IPSourceGuardPortConfigPort = _Gs2352IPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1, 2, 1, 1),
    _Gs2352IPSourceGuardPortConfigPort_Type()
)
gs2352IPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardPortConfigPort.setStatus("current")


class _Gs2352IPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type gs2352IPSourceGuardPortConfigMode based on Integer32"""
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


_Gs2352IPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardPortConfigMode_Object = MibTableColumn
gs2352IPSourceGuardPortConfigMode = _Gs2352IPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1, 2, 1, 2),
    _Gs2352IPSourceGuardPortConfigMode_Type()
)
gs2352IPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardPortConfigMode.setStatus("current")


class _Gs2352IPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type gs2352IPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Gs2352IPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
gs2352IPSourceGuardPortMaxDynamicClients = _Gs2352IPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 1, 2, 1, 3),
    _Gs2352IPSourceGuardPortMaxDynamicClients_Type()
)
gs2352IPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardPortMaxDynamicClients.setStatus("current")
_Gs2352IPSourceGuardStatic_ObjectIdentity = ObjectIdentity
gs2352IPSourceGuardStatic = _Gs2352IPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2)
)


class _Gs2352IPSourceGuardStaticCreate_Type(Integer32):
    """Custom type gs2352IPSourceGuardStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352IPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardStaticCreate_Object = MibScalar
gs2352IPSourceGuardStaticCreate = _Gs2352IPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 1),
    _Gs2352IPSourceGuardStaticCreate_Type()
)
gs2352IPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticCreate.setStatus("current")
_Gs2352IPSourceGuardStaticTable_Object = MibTable
gs2352IPSourceGuardStaticTable = _Gs2352IPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticTable.setStatus("current")
_Gs2352IPSourceGuardStaticEntry_Object = MibTableRow
gs2352IPSourceGuardStaticEntry = _Gs2352IPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1)
)
gs2352IPSourceGuardStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticEntry.setStatus("current")


class _Gs2352IPSourceGuardStaticIndex_Type(Integer32):
    """Custom type gs2352IPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Gs2352IPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardStaticIndex_Object = MibTableColumn
gs2352IPSourceGuardStaticIndex = _Gs2352IPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1, 1),
    _Gs2352IPSourceGuardStaticIndex_Type()
)
gs2352IPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticIndex.setStatus("current")


class _Gs2352IPSourceGuardStaticPort_Type(Integer32):
    """Custom type gs2352IPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardStaticPort_Object = MibTableColumn
gs2352IPSourceGuardStaticPort = _Gs2352IPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1, 2),
    _Gs2352IPSourceGuardStaticPort_Type()
)
gs2352IPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticPort.setStatus("current")


class _Gs2352IPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type gs2352IPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352IPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardStaticVLANId_Object = MibTableColumn
gs2352IPSourceGuardStaticVLANId = _Gs2352IPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1, 3),
    _Gs2352IPSourceGuardStaticVLANId_Type()
)
gs2352IPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticVLANId.setStatus("current")
_Gs2352IPSourceGuardStaticIPAddress_Type = IpAddress
_Gs2352IPSourceGuardStaticIPAddress_Object = MibTableColumn
gs2352IPSourceGuardStaticIPAddress = _Gs2352IPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1, 4),
    _Gs2352IPSourceGuardStaticIPAddress_Type()
)
gs2352IPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticIPAddress.setStatus("current")
_Gs2352IPSourceGuardStaticMACAddress_Type = MacAddress
_Gs2352IPSourceGuardStaticMACAddress_Object = MibTableColumn
gs2352IPSourceGuardStaticMACAddress = _Gs2352IPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1, 5),
    _Gs2352IPSourceGuardStaticMACAddress_Type()
)
gs2352IPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticMACAddress.setStatus("current")


class _Gs2352IPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type gs2352IPSourceGuardStaticRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInservice", 2),
          ("edit", 3),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352IPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardStaticRowStatus_Object = MibTableColumn
gs2352IPSourceGuardStaticRowStatus = _Gs2352IPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 2, 2, 1, 6),
    _Gs2352IPSourceGuardStaticRowStatus_Type()
)
gs2352IPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardStaticRowStatus.setStatus("current")
_Gs2352IPSourceGuardDynamicTable_Object = MibTable
gs2352IPSourceGuardDynamicTable = _Gs2352IPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3)
)
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicTable.setStatus("current")
_Gs2352IPSourceGuardDynamicEntry_Object = MibTableRow
gs2352IPSourceGuardDynamicEntry = _Gs2352IPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3, 1)
)
gs2352IPSourceGuardDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352IPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicEntry.setStatus("current")


class _Gs2352IPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type gs2352IPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352IPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardDynamicIndex_Object = MibTableColumn
gs2352IPSourceGuardDynamicIndex = _Gs2352IPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3, 1, 1),
    _Gs2352IPSourceGuardDynamicIndex_Type()
)
gs2352IPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicIndex.setStatus("current")


class _Gs2352IPSourceGuardDynamicPort_Type(Integer32):
    """Custom type gs2352IPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2352IPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardDynamicPort_Object = MibTableColumn
gs2352IPSourceGuardDynamicPort = _Gs2352IPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3, 1, 2),
    _Gs2352IPSourceGuardDynamicPort_Type()
)
gs2352IPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicPort.setStatus("current")


class _Gs2352IPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type gs2352IPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352IPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Gs2352IPSourceGuardDynamicVLANId_Object = MibTableColumn
gs2352IPSourceGuardDynamicVLANId = _Gs2352IPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3, 1, 3),
    _Gs2352IPSourceGuardDynamicVLANId_Type()
)
gs2352IPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicVLANId.setStatus("current")
_Gs2352IPSourceGuardDynamicIPAddress_Type = IpAddress
_Gs2352IPSourceGuardDynamicIPAddress_Object = MibTableColumn
gs2352IPSourceGuardDynamicIPAddress = _Gs2352IPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3, 1, 4),
    _Gs2352IPSourceGuardDynamicIPAddress_Type()
)
gs2352IPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicIPAddress.setStatus("current")
_Gs2352IPSourceGuardDynamicMACAddress_Type = MacAddress
_Gs2352IPSourceGuardDynamicMACAddress_Object = MibTableColumn
gs2352IPSourceGuardDynamicMACAddress = _Gs2352IPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 1, 3, 1, 5),
    _Gs2352IPSourceGuardDynamicMACAddress_Type()
)
gs2352IPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352IPSourceGuardDynamicMACAddress.setStatus("current")
_Gs2352ARPInspection_ObjectIdentity = ObjectIdentity
gs2352ARPInspection = _Gs2352ARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2)
)
_Gs2352ARPInspectionConf_ObjectIdentity = ObjectIdentity
gs2352ARPInspectionConf = _Gs2352ARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 1)
)


class _Gs2352ARPInspectionConfMode_Type(Integer32):
    """Custom type gs2352ARPInspectionConfMode based on Integer32"""
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


_Gs2352ARPInspectionConfMode_Type.__name__ = "Integer32"
_Gs2352ARPInspectionConfMode_Object = MibScalar
gs2352ARPInspectionConfMode = _Gs2352ARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 1, 1),
    _Gs2352ARPInspectionConfMode_Type()
)
gs2352ARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionConfMode.setStatus("current")
_Gs2352ARPInspectionConfTable_Object = MibTable
gs2352ARPInspectionConfTable = _Gs2352ARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352ARPInspectionConfTable.setStatus("current")
_Gs2352ARPInspectionConfEntry_Object = MibTableRow
gs2352ARPInspectionConfEntry = _Gs2352ARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 1, 2, 1)
)
gs2352ARPInspectionConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    gs2352ARPInspectionConfEntry.setStatus("current")


class _Gs2352ARPInspectionConfPortIndex_Type(Integer32):
    """Custom type gs2352ARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Gs2352ARPInspectionConfPortIndex_Object = MibTableColumn
gs2352ARPInspectionConfPortIndex = _Gs2352ARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 1, 2, 1, 1),
    _Gs2352ARPInspectionConfPortIndex_Type()
)
gs2352ARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ARPInspectionConfPortIndex.setStatus("current")


class _Gs2352ARPInspectionConfPortMode_Type(Integer32):
    """Custom type gs2352ARPInspectionConfPortMode based on Integer32"""
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


_Gs2352ARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Gs2352ARPInspectionConfPortMode_Object = MibTableColumn
gs2352ARPInspectionConfPortMode = _Gs2352ARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 1, 2, 1, 2),
    _Gs2352ARPInspectionConfPortMode_Type()
)
gs2352ARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionConfPortMode.setStatus("current")
_Gs2352ARPInspectionStatic_ObjectIdentity = ObjectIdentity
gs2352ARPInspectionStatic = _Gs2352ARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2)
)


class _Gs2352ARPInspectionStaticCreate_Type(Integer32):
    """Custom type gs2352ARPInspectionStaticCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352ARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Gs2352ARPInspectionStaticCreate_Object = MibScalar
gs2352ARPInspectionStaticCreate = _Gs2352ARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 1),
    _Gs2352ARPInspectionStaticCreate_Type()
)
gs2352ARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticCreate.setStatus("current")
_Gs2352ARPInspectionStaticTable_Object = MibTable
gs2352ARPInspectionStaticTable = _Gs2352ARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticTable.setStatus("current")
_Gs2352ARPInspectionStaticEntry_Object = MibTableRow
gs2352ARPInspectionStaticEntry = _Gs2352ARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1)
)
gs2352ARPInspectionStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticEntry.setStatus("current")


class _Gs2352ARPInspectionStaticIndex_Type(Integer32):
    """Custom type gs2352ARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Gs2352ARPInspectionStaticIndex_Object = MibTableColumn
gs2352ARPInspectionStaticIndex = _Gs2352ARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1, 1),
    _Gs2352ARPInspectionStaticIndex_Type()
)
gs2352ARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticIndex.setStatus("current")


class _Gs2352ARPInspectionStaticPort_Type(Integer32):
    """Custom type gs2352ARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPInspectionStaticPort_Type.__name__ = "Integer32"
_Gs2352ARPInspectionStaticPort_Object = MibTableColumn
gs2352ARPInspectionStaticPort = _Gs2352ARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1, 2),
    _Gs2352ARPInspectionStaticPort_Type()
)
gs2352ARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticPort.setStatus("current")


class _Gs2352ARPInspectionStaticVLANId_Type(Integer32):
    """Custom type gs2352ARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352ARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Gs2352ARPInspectionStaticVLANId_Object = MibTableColumn
gs2352ARPInspectionStaticVLANId = _Gs2352ARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1, 3),
    _Gs2352ARPInspectionStaticVLANId_Type()
)
gs2352ARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticVLANId.setStatus("current")
_Gs2352ARPInspectionStaticIPAddress_Type = IpAddress
_Gs2352ARPInspectionStaticIPAddress_Object = MibTableColumn
gs2352ARPInspectionStaticIPAddress = _Gs2352ARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1, 4),
    _Gs2352ARPInspectionStaticIPAddress_Type()
)
gs2352ARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticIPAddress.setStatus("current")
_Gs2352ARPInspectionStaticMACAddress_Type = MacAddress
_Gs2352ARPInspectionStaticMACAddress_Object = MibTableColumn
gs2352ARPInspectionStaticMACAddress = _Gs2352ARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1, 5),
    _Gs2352ARPInspectionStaticMACAddress_Type()
)
gs2352ARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticMACAddress.setStatus("current")


class _Gs2352ARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type gs2352ARPInspectionStaticRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInservice", 2),
          ("edit", 3),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352ARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Gs2352ARPInspectionStaticRowStatus_Object = MibTableColumn
gs2352ARPInspectionStaticRowStatus = _Gs2352ARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 2, 2, 1, 6),
    _Gs2352ARPInspectionStaticRowStatus_Type()
)
gs2352ARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPInspectionStaticRowStatus.setStatus("current")
_Gs2352ARPInspectionDynamicTable_Object = MibTable
gs2352ARPInspectionDynamicTable = _Gs2352ARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicTable.setStatus("current")
_Gs2352ARPInspectionDynamicEntry_Object = MibTableRow
gs2352ARPInspectionDynamicEntry = _Gs2352ARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3, 1)
)
gs2352ARPInspectionDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicEntry.setStatus("current")


class _Gs2352ARPInspectionDynamicIndex_Type(Integer32):
    """Custom type gs2352ARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Gs2352ARPInspectionDynamicIndex_Object = MibTableColumn
gs2352ARPInspectionDynamicIndex = _Gs2352ARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3, 1, 1),
    _Gs2352ARPInspectionDynamicIndex_Type()
)
gs2352ARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicIndex.setStatus("current")


class _Gs2352ARPInspectionDynamicPort_Type(Integer32):
    """Custom type gs2352ARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Gs2352ARPInspectionDynamicPort_Object = MibTableColumn
gs2352ARPInspectionDynamicPort = _Gs2352ARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3, 1, 2),
    _Gs2352ARPInspectionDynamicPort_Type()
)
gs2352ARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicPort.setStatus("current")


class _Gs2352ARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type gs2352ARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352ARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Gs2352ARPInspectionDynamicVLANId_Object = MibTableColumn
gs2352ARPInspectionDynamicVLANId = _Gs2352ARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3, 1, 3),
    _Gs2352ARPInspectionDynamicVLANId_Type()
)
gs2352ARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicVLANId.setStatus("current")
_Gs2352ARPInspectionDynamicIPAddress_Type = IpAddress
_Gs2352ARPInspectionDynamicIPAddress_Object = MibTableColumn
gs2352ARPInspectionDynamicIPAddress = _Gs2352ARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3, 1, 4),
    _Gs2352ARPInspectionDynamicIPAddress_Type()
)
gs2352ARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicIPAddress.setStatus("current")
_Gs2352ARPInspectionDynamicMACAddress_Type = MacAddress
_Gs2352ARPInspectionDynamicMACAddress_Object = MibTableColumn
gs2352ARPInspectionDynamicMACAddress = _Gs2352ARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 3, 1, 5),
    _Gs2352ARPInspectionDynamicMACAddress_Type()
)
gs2352ARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ARPInspectionDynamicMACAddress.setStatus("current")
_Gs2352ARPStaticGatewayCtrl_ObjectIdentity = ObjectIdentity
gs2352ARPStaticGatewayCtrl = _Gs2352ARPStaticGatewayCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6)
)
_Gs2352ARPStaticGatewayCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2352ARPStaticGatewayCtrlSystemConf = _Gs2352ARPStaticGatewayCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 1)
)


class _Gs2352ARPStaticGatewayCtrlMode_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlMode based on Integer32"""
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


_Gs2352ARPStaticGatewayCtrlMode_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlMode_Object = MibScalar
gs2352ARPStaticGatewayCtrlMode = _Gs2352ARPStaticGatewayCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 1, 1),
    _Gs2352ARPStaticGatewayCtrlMode_Type()
)
gs2352ARPStaticGatewayCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlMode.setStatus("current")


class _Gs2352ARPStaticGatewayCtrlCreate_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352ARPStaticGatewayCtrlCreate_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlCreate_Object = MibScalar
gs2352ARPStaticGatewayCtrlCreate = _Gs2352ARPStaticGatewayCtrlCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 2),
    _Gs2352ARPStaticGatewayCtrlCreate_Type()
)
gs2352ARPStaticGatewayCtrlCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlCreate.setStatus("current")
_Gs2352ARPStaticGatewayCtrlTable_Object = MibTable
gs2352ARPStaticGatewayCtrlTable = _Gs2352ARPStaticGatewayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlTable.setStatus("current")
_Gs2352ARPStaticGatewayCtrlEntry_Object = MibTableRow
gs2352ARPStaticGatewayCtrlEntry = _Gs2352ARPStaticGatewayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1)
)
gs2352ARPStaticGatewayCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ARPStaticGatewayCtrlIndex"),
)
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlEntry.setStatus("current")


class _Gs2352ARPStaticGatewayCtrlIndex_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2352ARPStaticGatewayCtrlIndex_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlIndex_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlIndex = _Gs2352ARPStaticGatewayCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 1),
    _Gs2352ARPStaticGatewayCtrlIndex_Type()
)
gs2352ARPStaticGatewayCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlIndex.setStatus("current")
_Gs2352ARPStaticGatewayCtrlIPAddress_Type = IpAddress
_Gs2352ARPStaticGatewayCtrlIPAddress_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlIPAddress = _Gs2352ARPStaticGatewayCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 2),
    _Gs2352ARPStaticGatewayCtrlIPAddress_Type()
)
gs2352ARPStaticGatewayCtrlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlIPAddress.setStatus("current")
_Gs2352ARPStaticGatewayCtrlMACAddress_Type = MacAddress
_Gs2352ARPStaticGatewayCtrlMACAddress_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlMACAddress = _Gs2352ARPStaticGatewayCtrlMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 3),
    _Gs2352ARPStaticGatewayCtrlMACAddress_Type()
)
gs2352ARPStaticGatewayCtrlMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlMACAddress.setStatus("current")


class _Gs2352ARPStaticGatewayCtrlPort_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPStaticGatewayCtrlPort_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlPort_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlPort = _Gs2352ARPStaticGatewayCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 4),
    _Gs2352ARPStaticGatewayCtrlPort_Type()
)
gs2352ARPStaticGatewayCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlPort.setStatus("current")


class _Gs2352ARPStaticGatewayCtrlAction_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlAction based on Integer32"""
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
        *(("none", 0),
          ("trap", 1),
          ("dropAndTrap", 2),
          ("shutdown", 3),
          ("trapAndShutdown", 4))
    )


_Gs2352ARPStaticGatewayCtrlAction_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlAction_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlAction = _Gs2352ARPStaticGatewayCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 5),
    _Gs2352ARPStaticGatewayCtrlAction_Type()
)
gs2352ARPStaticGatewayCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlAction.setStatus("current")
_Gs2352ARPStaticGatewayCtrlState_Type = DisplayString
_Gs2352ARPStaticGatewayCtrlState_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlState = _Gs2352ARPStaticGatewayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 6),
    _Gs2352ARPStaticGatewayCtrlState_Type()
)
gs2352ARPStaticGatewayCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlState.setStatus("current")


class _Gs2352ARPStaticGatewayCtrlReOpen_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reopen", 1))
    )


_Gs2352ARPStaticGatewayCtrlReOpen_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlReOpen_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlReOpen = _Gs2352ARPStaticGatewayCtrlReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 7),
    _Gs2352ARPStaticGatewayCtrlReOpen_Type()
)
gs2352ARPStaticGatewayCtrlReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlReOpen.setStatus("current")


class _Gs2352ARPStaticGatewayCtrlRowStatus_Type(Integer32):
    """Custom type gs2352ARPStaticGatewayCtrlRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInservice", 2),
          ("edit", 3),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352ARPStaticGatewayCtrlRowStatus_Type.__name__ = "Integer32"
_Gs2352ARPStaticGatewayCtrlRowStatus_Object = MibTableColumn
gs2352ARPStaticGatewayCtrlRowStatus = _Gs2352ARPStaticGatewayCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 6, 3, 1, 8),
    _Gs2352ARPStaticGatewayCtrlRowStatus_Type()
)
gs2352ARPStaticGatewayCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPStaticGatewayCtrlRowStatus.setStatus("current")
_Gs2352ARPSpoofingPrevention_ObjectIdentity = ObjectIdentity
gs2352ARPSpoofingPrevention = _Gs2352ARPSpoofingPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7)
)
_Gs2352ARPSpoofingPreventionSystemConf_ObjectIdentity = ObjectIdentity
gs2352ARPSpoofingPreventionSystemConf = _Gs2352ARPSpoofingPreventionSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 1)
)


class _Gs2352ARPSpoofingPreventionMode_Type(Integer32):
    """Custom type gs2352ARPSpoofingPreventionMode based on Integer32"""
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


_Gs2352ARPSpoofingPreventionMode_Type.__name__ = "Integer32"
_Gs2352ARPSpoofingPreventionMode_Object = MibScalar
gs2352ARPSpoofingPreventionMode = _Gs2352ARPSpoofingPreventionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 1, 1),
    _Gs2352ARPSpoofingPreventionMode_Type()
)
gs2352ARPSpoofingPreventionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionMode.setStatus("current")
_Gs2352ARPSpoofingPreventionTable_Object = MibTable
gs2352ARPSpoofingPreventionTable = _Gs2352ARPSpoofingPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionTable.setStatus("current")
_Gs2352ARPSpoofingPreventionEntry_Object = MibTableRow
gs2352ARPSpoofingPreventionEntry = _Gs2352ARPSpoofingPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1)
)
gs2352ARPSpoofingPreventionEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352ARPSpoofingPreventionPort"),
)
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionEntry.setStatus("current")


class _Gs2352ARPSpoofingPreventionPort_Type(Integer32):
    """Custom type gs2352ARPSpoofingPreventionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352ARPSpoofingPreventionPort_Type.__name__ = "Integer32"
_Gs2352ARPSpoofingPreventionPort_Object = MibTableColumn
gs2352ARPSpoofingPreventionPort = _Gs2352ARPSpoofingPreventionPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1, 1),
    _Gs2352ARPSpoofingPreventionPort_Type()
)
gs2352ARPSpoofingPreventionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionPort.setStatus("current")


class _Gs2352ARPSpoofingPreventionPortMode_Type(Integer32):
    """Custom type gs2352ARPSpoofingPreventionPortMode based on Integer32"""
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


_Gs2352ARPSpoofingPreventionPortMode_Type.__name__ = "Integer32"
_Gs2352ARPSpoofingPreventionPortMode_Object = MibTableColumn
gs2352ARPSpoofingPreventionPortMode = _Gs2352ARPSpoofingPreventionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1, 2),
    _Gs2352ARPSpoofingPreventionPortMode_Type()
)
gs2352ARPSpoofingPreventionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionPortMode.setStatus("current")


class _Gs2352ARPSpoofingPreventionPortLimit_Type(Integer32):
    """Custom type gs2352ARPSpoofingPreventionPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Gs2352ARPSpoofingPreventionPortLimit_Type.__name__ = "Integer32"
_Gs2352ARPSpoofingPreventionPortLimit_Object = MibTableColumn
gs2352ARPSpoofingPreventionPortLimit = _Gs2352ARPSpoofingPreventionPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1, 3),
    _Gs2352ARPSpoofingPreventionPortLimit_Type()
)
gs2352ARPSpoofingPreventionPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionPortLimit.setStatus("current")


class _Gs2352ARPSpoofingPreventionPortAction_Type(Integer32):
    """Custom type gs2352ARPSpoofingPreventionPortAction based on Integer32"""
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
        *(("none", 0),
          ("trap", 1),
          ("dropAndTrap", 2),
          ("shutdown", 3),
          ("trapAndShutdown", 4))
    )


_Gs2352ARPSpoofingPreventionPortAction_Type.__name__ = "Integer32"
_Gs2352ARPSpoofingPreventionPortAction_Object = MibTableColumn
gs2352ARPSpoofingPreventionPortAction = _Gs2352ARPSpoofingPreventionPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1, 4),
    _Gs2352ARPSpoofingPreventionPortAction_Type()
)
gs2352ARPSpoofingPreventionPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionPortAction.setStatus("current")
_Gs2352ARPSpoofingPreventionPortState_Type = DisplayString
_Gs2352ARPSpoofingPreventionPortState_Object = MibTableColumn
gs2352ARPSpoofingPreventionPortState = _Gs2352ARPSpoofingPreventionPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1, 5),
    _Gs2352ARPSpoofingPreventionPortState_Type()
)
gs2352ARPSpoofingPreventionPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionPortState.setStatus("current")


class _Gs2352ARPSpoofingPreventionPortReOpen_Type(Integer32):
    """Custom type gs2352ARPSpoofingPreventionPortReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reopen", 1))
    )


_Gs2352ARPSpoofingPreventionPortReOpen_Type.__name__ = "Integer32"
_Gs2352ARPSpoofingPreventionPortReOpen_Object = MibTableColumn
gs2352ARPSpoofingPreventionPortReOpen = _Gs2352ARPSpoofingPreventionPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 7, 2, 1, 6),
    _Gs2352ARPSpoofingPreventionPortReOpen_Type()
)
gs2352ARPSpoofingPreventionPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPSpoofingPreventionPortReOpen.setStatus("current")
_Gs2352ARPIPDoSPrevention_ObjectIdentity = ObjectIdentity
gs2352ARPIPDoSPrevention = _Gs2352ARPIPDoSPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8)
)


class _Gs2352ARPIPDoSPreventionTCPMode_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionTCPMode based on Integer32"""
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


_Gs2352ARPIPDoSPreventionTCPMode_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionTCPMode_Object = MibScalar
gs2352ARPIPDoSPreventionTCPMode = _Gs2352ARPIPDoSPreventionTCPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 1),
    _Gs2352ARPIPDoSPreventionTCPMode_Type()
)
gs2352ARPIPDoSPreventionTCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionTCPMode.setStatus("current")


class _Gs2352ARPIPDoSPreventionUDPMode_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionUDPMode based on Integer32"""
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


_Gs2352ARPIPDoSPreventionUDPMode_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionUDPMode_Object = MibScalar
gs2352ARPIPDoSPreventionUDPMode = _Gs2352ARPIPDoSPreventionUDPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 2),
    _Gs2352ARPIPDoSPreventionUDPMode_Type()
)
gs2352ARPIPDoSPreventionUDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionUDPMode.setStatus("current")


class _Gs2352ARPIPDoSPreventionICMPMode_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionICMPMode based on Integer32"""
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


_Gs2352ARPIPDoSPreventionICMPMode_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionICMPMode_Object = MibScalar
gs2352ARPIPDoSPreventionICMPMode = _Gs2352ARPIPDoSPreventionICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 3),
    _Gs2352ARPIPDoSPreventionICMPMode_Type()
)
gs2352ARPIPDoSPreventionICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionICMPMode.setStatus("current")


class _Gs2352ARPIPDoSPreventionServerPort1_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionServerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2352ARPIPDoSPreventionServerPort1_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionServerPort1_Object = MibScalar
gs2352ARPIPDoSPreventionServerPort1 = _Gs2352ARPIPDoSPreventionServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 4),
    _Gs2352ARPIPDoSPreventionServerPort1_Type()
)
gs2352ARPIPDoSPreventionServerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionServerPort1.setStatus("current")


class _Gs2352ARPIPDoSPreventionServerPort2_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionServerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2352ARPIPDoSPreventionServerPort2_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionServerPort2_Object = MibScalar
gs2352ARPIPDoSPreventionServerPort2 = _Gs2352ARPIPDoSPreventionServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 5),
    _Gs2352ARPIPDoSPreventionServerPort2_Type()
)
gs2352ARPIPDoSPreventionServerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionServerPort2.setStatus("current")


class _Gs2352ARPIPDoSPreventionServerPort3_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionServerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2352ARPIPDoSPreventionServerPort3_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionServerPort3_Object = MibScalar
gs2352ARPIPDoSPreventionServerPort3 = _Gs2352ARPIPDoSPreventionServerPort3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 6),
    _Gs2352ARPIPDoSPreventionServerPort3_Type()
)
gs2352ARPIPDoSPreventionServerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionServerPort3.setStatus("current")


class _Gs2352ARPIPDoSPreventionServerPort4_Type(Integer32):
    """Custom type gs2352ARPIPDoSPreventionServerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2352ARPIPDoSPreventionServerPort4_Type.__name__ = "Integer32"
_Gs2352ARPIPDoSPreventionServerPort4_Object = MibScalar
gs2352ARPIPDoSPreventionServerPort4 = _Gs2352ARPIPDoSPreventionServerPort4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 2, 8, 7),
    _Gs2352ARPIPDoSPreventionServerPort4_Type()
)
gs2352ARPIPDoSPreventionServerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ARPIPDoSPreventionServerPort4.setStatus("current")
_Gs2352DHCPSnooping_ObjectIdentity = ObjectIdentity
gs2352DHCPSnooping = _Gs2352DHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3)
)
_Gs2352DHCPSnoopingConf_ObjectIdentity = ObjectIdentity
gs2352DHCPSnoopingConf = _Gs2352DHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 1)
)


class _Gs2352DHCPSnoopingMode_Type(Integer32):
    """Custom type gs2352DHCPSnoopingMode based on Integer32"""
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


_Gs2352DHCPSnoopingMode_Type.__name__ = "Integer32"
_Gs2352DHCPSnoopingMode_Object = MibScalar
gs2352DHCPSnoopingMode = _Gs2352DHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 1, 1),
    _Gs2352DHCPSnoopingMode_Type()
)
gs2352DHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingMode.setStatus("current")
_Gs2352DHCPSnoopingPortModeConfigurationTable_Object = MibTable
gs2352DHCPSnoopingPortModeConfigurationTable = _Gs2352DHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Gs2352DHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
gs2352DHCPSnoopingPortModeConfigurationEntry = _Gs2352DHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 1, 2, 1)
)
gs2352DHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352DHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Gs2352DHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type gs2352DHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352DHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Gs2352DHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
gs2352DHCPSnoopingPortModeConfigurationPort = _Gs2352DHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 1, 2, 1, 1),
    _Gs2352DHCPSnoopingPortModeConfigurationPort_Type()
)
gs2352DHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Gs2352DHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type gs2352DHCPSnoopingPortModeConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trust", 0),
          ("untrust", 1))
    )


_Gs2352DHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Gs2352DHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
gs2352DHCPSnoopingPortModeConfigurationMode = _Gs2352DHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 1, 2, 1, 2),
    _Gs2352DHCPSnoopingPortModeConfigurationMode_Type()
)
gs2352DHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Gs2352DHCPSnoopingStatisticsTable_Object = MibTable
gs2352DHCPSnoopingStatisticsTable = _Gs2352DHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingStatisticsTable.setStatus("current")
_Gs2352DHCPSnoopingStatisticsEntry_Object = MibTableRow
gs2352DHCPSnoopingStatisticsEntry = _Gs2352DHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1)
)
gs2352DHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352DHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingStatisticsEntry.setStatus("current")


class _Gs2352DHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type gs2352DHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352DHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Gs2352DHCPSnoopingStatisticsPort_Object = MibTableColumn
gs2352DHCPSnoopingStatisticsPort = _Gs2352DHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 1),
    _Gs2352DHCPSnoopingStatisticsPort_Type()
)
gs2352DHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingStatisticsPort.setStatus("current")


class _Gs2352DHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type gs2352DHCPSnoopingStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352DHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Gs2352DHCPSnoopingStatisticsClear_Object = MibTableColumn
gs2352DHCPSnoopingStatisticsClear = _Gs2352DHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 2),
    _Gs2352DHCPSnoopingStatisticsClear_Type()
)
gs2352DHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingStatisticsClear.setStatus("current")
_Gs2352DHCPSnoopingRxDiscover_Type = Counter32
_Gs2352DHCPSnoopingRxDiscover_Object = MibTableColumn
gs2352DHCPSnoopingRxDiscover = _Gs2352DHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 3),
    _Gs2352DHCPSnoopingRxDiscover_Type()
)
gs2352DHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxDiscover.setStatus("current")
_Gs2352DHCPSnoopingRxOffer_Type = Counter32
_Gs2352DHCPSnoopingRxOffer_Object = MibTableColumn
gs2352DHCPSnoopingRxOffer = _Gs2352DHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 4),
    _Gs2352DHCPSnoopingRxOffer_Type()
)
gs2352DHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxOffer.setStatus("current")
_Gs2352DHCPSnoopingRxRequest_Type = Counter32
_Gs2352DHCPSnoopingRxRequest_Object = MibTableColumn
gs2352DHCPSnoopingRxRequest = _Gs2352DHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 5),
    _Gs2352DHCPSnoopingRxRequest_Type()
)
gs2352DHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxRequest.setStatus("current")
_Gs2352DHCPSnoopingRxDecline_Type = Counter32
_Gs2352DHCPSnoopingRxDecline_Object = MibTableColumn
gs2352DHCPSnoopingRxDecline = _Gs2352DHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 6),
    _Gs2352DHCPSnoopingRxDecline_Type()
)
gs2352DHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxDecline.setStatus("current")
_Gs2352DHCPSnoopingRxACK_Type = Counter32
_Gs2352DHCPSnoopingRxACK_Object = MibTableColumn
gs2352DHCPSnoopingRxACK = _Gs2352DHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 7),
    _Gs2352DHCPSnoopingRxACK_Type()
)
gs2352DHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxACK.setStatus("current")
_Gs2352DHCPSnoopingRxNAK_Type = Counter32
_Gs2352DHCPSnoopingRxNAK_Object = MibTableColumn
gs2352DHCPSnoopingRxNAK = _Gs2352DHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 8),
    _Gs2352DHCPSnoopingRxNAK_Type()
)
gs2352DHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxNAK.setStatus("current")
_Gs2352DHCPSnoopingRxRelease_Type = Counter32
_Gs2352DHCPSnoopingRxRelease_Object = MibTableColumn
gs2352DHCPSnoopingRxRelease = _Gs2352DHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 9),
    _Gs2352DHCPSnoopingRxRelease_Type()
)
gs2352DHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxRelease.setStatus("current")
_Gs2352DHCPSnoopingRxInform_Type = Counter32
_Gs2352DHCPSnoopingRxInform_Object = MibTableColumn
gs2352DHCPSnoopingRxInform = _Gs2352DHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 10),
    _Gs2352DHCPSnoopingRxInform_Type()
)
gs2352DHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxInform.setStatus("current")
_Gs2352DHCPSnoopingRxLeaseQuery_Type = Counter32
_Gs2352DHCPSnoopingRxLeaseQuery_Object = MibTableColumn
gs2352DHCPSnoopingRxLeaseQuery = _Gs2352DHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 11),
    _Gs2352DHCPSnoopingRxLeaseQuery_Type()
)
gs2352DHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxLeaseQuery.setStatus("current")
_Gs2352DHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Gs2352DHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
gs2352DHCPSnoopingRxLeaseUnassigned = _Gs2352DHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 12),
    _Gs2352DHCPSnoopingRxLeaseUnassigned_Type()
)
gs2352DHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Gs2352DHCPSnoopingRxLeaseUnknown_Type = Counter32
_Gs2352DHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
gs2352DHCPSnoopingRxLeaseUnknown = _Gs2352DHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 13),
    _Gs2352DHCPSnoopingRxLeaseUnknown_Type()
)
gs2352DHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxLeaseUnknown.setStatus("current")
_Gs2352DHCPSnoopingRxLeaseActive_Type = Counter32
_Gs2352DHCPSnoopingRxLeaseActive_Object = MibTableColumn
gs2352DHCPSnoopingRxLeaseActive = _Gs2352DHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 14),
    _Gs2352DHCPSnoopingRxLeaseActive_Type()
)
gs2352DHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingRxLeaseActive.setStatus("current")
_Gs2352DHCPSnoopingTxDiscover_Type = Counter32
_Gs2352DHCPSnoopingTxDiscover_Object = MibTableColumn
gs2352DHCPSnoopingTxDiscover = _Gs2352DHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 15),
    _Gs2352DHCPSnoopingTxDiscover_Type()
)
gs2352DHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxDiscover.setStatus("current")
_Gs2352DHCPSnoopingTxOffer_Type = Counter32
_Gs2352DHCPSnoopingTxOffer_Object = MibTableColumn
gs2352DHCPSnoopingTxOffer = _Gs2352DHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 16),
    _Gs2352DHCPSnoopingTxOffer_Type()
)
gs2352DHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxOffer.setStatus("current")
_Gs2352DHCPSnoopingTxRequest_Type = Counter32
_Gs2352DHCPSnoopingTxRequest_Object = MibTableColumn
gs2352DHCPSnoopingTxRequest = _Gs2352DHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 17),
    _Gs2352DHCPSnoopingTxRequest_Type()
)
gs2352DHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxRequest.setStatus("current")
_Gs2352DHCPSnoopingTxDecline_Type = Counter32
_Gs2352DHCPSnoopingTxDecline_Object = MibTableColumn
gs2352DHCPSnoopingTxDecline = _Gs2352DHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 18),
    _Gs2352DHCPSnoopingTxDecline_Type()
)
gs2352DHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxDecline.setStatus("current")
_Gs2352DHCPSnoopingTxACK_Type = Counter32
_Gs2352DHCPSnoopingTxACK_Object = MibTableColumn
gs2352DHCPSnoopingTxACK = _Gs2352DHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 19),
    _Gs2352DHCPSnoopingTxACK_Type()
)
gs2352DHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxACK.setStatus("current")
_Gs2352DHCPSnoopingTxNAK_Type = Counter32
_Gs2352DHCPSnoopingTxNAK_Object = MibTableColumn
gs2352DHCPSnoopingTxNAK = _Gs2352DHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 20),
    _Gs2352DHCPSnoopingTxNAK_Type()
)
gs2352DHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxNAK.setStatus("current")
_Gs2352DHCPSnoopingTxRelease_Type = Counter32
_Gs2352DHCPSnoopingTxRelease_Object = MibTableColumn
gs2352DHCPSnoopingTxRelease = _Gs2352DHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 21),
    _Gs2352DHCPSnoopingTxRelease_Type()
)
gs2352DHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxRelease.setStatus("current")
_Gs2352DHCPSnoopingTxInform_Type = Counter32
_Gs2352DHCPSnoopingTxInform_Object = MibTableColumn
gs2352DHCPSnoopingTxInform = _Gs2352DHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 22),
    _Gs2352DHCPSnoopingTxInform_Type()
)
gs2352DHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxInform.setStatus("current")
_Gs2352DHCPSnoopingTxLeaseQuery_Type = Counter32
_Gs2352DHCPSnoopingTxLeaseQuery_Object = MibTableColumn
gs2352DHCPSnoopingTxLeaseQuery = _Gs2352DHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 23),
    _Gs2352DHCPSnoopingTxLeaseQuery_Type()
)
gs2352DHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxLeaseQuery.setStatus("current")
_Gs2352DHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Gs2352DHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
gs2352DHCPSnoopingTxLeaseUnassigned = _Gs2352DHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 24),
    _Gs2352DHCPSnoopingTxLeaseUnassigned_Type()
)
gs2352DHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Gs2352DHCPSnoopingTxLeaseUnknown_Type = Counter32
_Gs2352DHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
gs2352DHCPSnoopingTxLeaseUnknown = _Gs2352DHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 25),
    _Gs2352DHCPSnoopingTxLeaseUnknown_Type()
)
gs2352DHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxLeaseUnknown.setStatus("current")
_Gs2352DHCPSnoopingTxLeaseActive_Type = Counter32
_Gs2352DHCPSnoopingTxLeaseActive_Object = MibTableColumn
gs2352DHCPSnoopingTxLeaseActive = _Gs2352DHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 3, 2, 1, 26),
    _Gs2352DHCPSnoopingTxLeaseActive_Type()
)
gs2352DHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352DHCPSnoopingTxLeaseActive.setStatus("current")
_Gs2352DHCPRelay_ObjectIdentity = ObjectIdentity
gs2352DHCPRelay = _Gs2352DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4)
)
_Gs2352DHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
gs2352DHCPRelayConfiguration = _Gs2352DHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1)
)


class _Gs2352DHCPRelayMode_Type(Integer32):
    """Custom type gs2352DHCPRelayMode based on Integer32"""
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


_Gs2352DHCPRelayMode_Type.__name__ = "Integer32"
_Gs2352DHCPRelayMode_Object = MibScalar
gs2352DHCPRelayMode = _Gs2352DHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 1),
    _Gs2352DHCPRelayMode_Type()
)
gs2352DHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayMode.setStatus("current")
_Gs2352DHCPRelayServer_Type = IpAddress
_Gs2352DHCPRelayServer_Object = MibScalar
gs2352DHCPRelayServer = _Gs2352DHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 2),
    _Gs2352DHCPRelayServer_Type()
)
gs2352DHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayServer.setStatus("current")


class _Gs2352DHCPRelayInformationMode_Type(Integer32):
    """Custom type gs2352DHCPRelayInformationMode based on Integer32"""
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


_Gs2352DHCPRelayInformationMode_Type.__name__ = "Integer32"
_Gs2352DHCPRelayInformationMode_Object = MibScalar
gs2352DHCPRelayInformationMode = _Gs2352DHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 3),
    _Gs2352DHCPRelayInformationMode_Type()
)
gs2352DHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayInformationMode.setStatus("current")


class _Gs2352DHCPRelayInformationPolicy_Type(Integer32):
    """Custom type gs2352DHCPRelayInformationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 0),
          ("keep", 1),
          ("drop", 2))
    )


_Gs2352DHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Gs2352DHCPRelayInformationPolicy_Object = MibScalar
gs2352DHCPRelayInformationPolicy = _Gs2352DHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 4),
    _Gs2352DHCPRelayInformationPolicy_Type()
)
gs2352DHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayInformationPolicy.setStatus("current")
_Gs2352DHCPRelayConfigurationGateways_ObjectIdentity = ObjectIdentity
gs2352DHCPRelayConfigurationGateways = _Gs2352DHCPRelayConfigurationGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5)
)


class _Gs2352DHCPRelayConfigurationGatewaysCreate_Type(Integer32):
    """Custom type gs2352DHCPRelayConfigurationGatewaysCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352DHCPRelayConfigurationGatewaysCreate_Type.__name__ = "Integer32"
_Gs2352DHCPRelayConfigurationGatewaysCreate_Object = MibScalar
gs2352DHCPRelayConfigurationGatewaysCreate = _Gs2352DHCPRelayConfigurationGatewaysCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 1),
    _Gs2352DHCPRelayConfigurationGatewaysCreate_Type()
)
gs2352DHCPRelayConfigurationGatewaysCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysCreate.setStatus("current")
_Gs2352DHCPRelayConfigurationGatewaysTable_Object = MibTable
gs2352DHCPRelayConfigurationGatewaysTable = _Gs2352DHCPRelayConfigurationGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysTable.setStatus("current")
_Gs2352DHCPRelayConfigurationGatewaysEntry_Object = MibTableRow
gs2352DHCPRelayConfigurationGatewaysEntry = _Gs2352DHCPRelayConfigurationGatewaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 2, 1)
)
gs2352DHCPRelayConfigurationGatewaysEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352DHCPRelayConfigurationGatewaysIndex"),
)
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysEntry.setStatus("current")


class _Gs2352DHCPRelayConfigurationGatewaysIndex_Type(Integer32):
    """Custom type gs2352DHCPRelayConfigurationGatewaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2352DHCPRelayConfigurationGatewaysIndex_Type.__name__ = "Integer32"
_Gs2352DHCPRelayConfigurationGatewaysIndex_Object = MibTableColumn
gs2352DHCPRelayConfigurationGatewaysIndex = _Gs2352DHCPRelayConfigurationGatewaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 2, 1, 1),
    _Gs2352DHCPRelayConfigurationGatewaysIndex_Type()
)
gs2352DHCPRelayConfigurationGatewaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysIndex.setStatus("current")


class _Gs2352DHCPRelayConfigurationGatewaysVLANId_Type(Integer32):
    """Custom type gs2352DHCPRelayConfigurationGatewaysVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352DHCPRelayConfigurationGatewaysVLANId_Type.__name__ = "Integer32"
_Gs2352DHCPRelayConfigurationGatewaysVLANId_Object = MibTableColumn
gs2352DHCPRelayConfigurationGatewaysVLANId = _Gs2352DHCPRelayConfigurationGatewaysVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 2, 1, 2),
    _Gs2352DHCPRelayConfigurationGatewaysVLANId_Type()
)
gs2352DHCPRelayConfigurationGatewaysVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysVLANId.setStatus("current")
_Gs2352DHCPRelayConfigurationGatewaysIP_Type = IpAddress
_Gs2352DHCPRelayConfigurationGatewaysIP_Object = MibTableColumn
gs2352DHCPRelayConfigurationGatewaysIP = _Gs2352DHCPRelayConfigurationGatewaysIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 2, 1, 3),
    _Gs2352DHCPRelayConfigurationGatewaysIP_Type()
)
gs2352DHCPRelayConfigurationGatewaysIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysIP.setStatus("current")


class _Gs2352DHCPRelayConfigurationGatewaysRowStatus_Type(Integer32):
    """Custom type gs2352DHCPRelayConfigurationGatewaysRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInservice", 2),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352DHCPRelayConfigurationGatewaysRowStatus_Type.__name__ = "Integer32"
_Gs2352DHCPRelayConfigurationGatewaysRowStatus_Object = MibTableColumn
gs2352DHCPRelayConfigurationGatewaysRowStatus = _Gs2352DHCPRelayConfigurationGatewaysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 5, 2, 1, 4),
    _Gs2352DHCPRelayConfigurationGatewaysRowStatus_Type()
)
gs2352DHCPRelayConfigurationGatewaysRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayConfigurationGatewaysRowStatus.setStatus("current")


class _Gs2352DHCPRelayInformationCustom_Type(DisplayString):
    """Custom type gs2352DHCPRelayInformationCustom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2352DHCPRelayInformationCustom_Type.__name__ = "DisplayString"
_Gs2352DHCPRelayInformationCustom_Object = MibScalar
gs2352DHCPRelayInformationCustom = _Gs2352DHCPRelayInformationCustom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 1, 1500),
    _Gs2352DHCPRelayInformationCustom_Type()
)
gs2352DHCPRelayInformationCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DHCPRelayInformationCustom.setStatus("current")
_Gs2352DHCPRelayStatistics_ObjectIdentity = ObjectIdentity
gs2352DHCPRelayStatistics = _Gs2352DHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2)
)
_Gs2352DHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
gs2352DHCPRelayServerStatistics = _Gs2352DHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1)
)
_Gs2352ServerStatTransmitToServer_Type = Counter32
_Gs2352ServerStatTransmitToServer_Object = MibScalar
gs2352ServerStatTransmitToServer = _Gs2352ServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 1),
    _Gs2352ServerStatTransmitToServer_Type()
)
gs2352ServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatTransmitToServer.setStatus("current")
_Gs2352ServerStatTransmitError_Type = Counter32
_Gs2352ServerStatTransmitError_Object = MibScalar
gs2352ServerStatTransmitError = _Gs2352ServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 2),
    _Gs2352ServerStatTransmitError_Type()
)
gs2352ServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatTransmitError.setStatus("current")
_Gs2352ServerStatReceiveFromServer_Type = Counter32
_Gs2352ServerStatReceiveFromServer_Object = MibScalar
gs2352ServerStatReceiveFromServer = _Gs2352ServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 3),
    _Gs2352ServerStatReceiveFromServer_Type()
)
gs2352ServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatReceiveFromServer.setStatus("current")
_Gs2352ServerStatReceiveMissingAgentOption_Type = Counter32
_Gs2352ServerStatReceiveMissingAgentOption_Object = MibScalar
gs2352ServerStatReceiveMissingAgentOption = _Gs2352ServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 4),
    _Gs2352ServerStatReceiveMissingAgentOption_Type()
)
gs2352ServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatReceiveMissingAgentOption.setStatus("current")
_Gs2352ServerStatReceiveMissingCircuitID_Type = Counter32
_Gs2352ServerStatReceiveMissingCircuitID_Object = MibScalar
gs2352ServerStatReceiveMissingCircuitID = _Gs2352ServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 5),
    _Gs2352ServerStatReceiveMissingCircuitID_Type()
)
gs2352ServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatReceiveMissingCircuitID.setStatus("current")
_Gs2352ServerStatReceiveMissingRemoteID_Type = Counter32
_Gs2352ServerStatReceiveMissingRemoteID_Object = MibScalar
gs2352ServerStatReceiveMissingRemoteID = _Gs2352ServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 6),
    _Gs2352ServerStatReceiveMissingRemoteID_Type()
)
gs2352ServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatReceiveMissingRemoteID.setStatus("current")
_Gs2352ServerStatReceiveBadCircuitID_Type = Counter32
_Gs2352ServerStatReceiveBadCircuitID_Object = MibScalar
gs2352ServerStatReceiveBadCircuitID = _Gs2352ServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 7),
    _Gs2352ServerStatReceiveBadCircuitID_Type()
)
gs2352ServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatReceiveBadCircuitID.setStatus("current")
_Gs2352ServerStatReceiveBadRemoteID_Type = Counter32
_Gs2352ServerStatReceiveBadRemoteID_Object = MibScalar
gs2352ServerStatReceiveBadRemoteID = _Gs2352ServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 1, 8),
    _Gs2352ServerStatReceiveBadRemoteID_Type()
)
gs2352ServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ServerStatReceiveBadRemoteID.setStatus("current")
_Gs2352DHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
gs2352DHCPRelayClientStatistics = _Gs2352DHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2)
)
_Gs2352ClientStatTransmitToClient_Type = Counter32
_Gs2352ClientStatTransmitToClient_Object = MibScalar
gs2352ClientStatTransmitToClient = _Gs2352ClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 1),
    _Gs2352ClientStatTransmitToClient_Type()
)
gs2352ClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatTransmitToClient.setStatus("current")
_Gs2352ClientStatTransmitError_Type = Counter32
_Gs2352ClientStatTransmitError_Object = MibScalar
gs2352ClientStatTransmitError = _Gs2352ClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 2),
    _Gs2352ClientStatTransmitError_Type()
)
gs2352ClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatTransmitError.setStatus("current")
_Gs2352ClientStatReceivefromClient_Type = Counter32
_Gs2352ClientStatReceivefromClient_Object = MibScalar
gs2352ClientStatReceivefromClient = _Gs2352ClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 3),
    _Gs2352ClientStatReceivefromClient_Type()
)
gs2352ClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatReceivefromClient.setStatus("current")
_Gs2352ClientStatReceiveAgentOption_Type = Counter32
_Gs2352ClientStatReceiveAgentOption_Object = MibScalar
gs2352ClientStatReceiveAgentOption = _Gs2352ClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 4),
    _Gs2352ClientStatReceiveAgentOption_Type()
)
gs2352ClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatReceiveAgentOption.setStatus("current")
_Gs2352ClientStatReplaceAgentOption_Type = Counter32
_Gs2352ClientStatReplaceAgentOption_Object = MibScalar
gs2352ClientStatReplaceAgentOption = _Gs2352ClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 5),
    _Gs2352ClientStatReplaceAgentOption_Type()
)
gs2352ClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatReplaceAgentOption.setStatus("current")
_Gs2352ClientStatKeepAgentOption_Type = Counter32
_Gs2352ClientStatKeepAgentOption_Object = MibScalar
gs2352ClientStatKeepAgentOption = _Gs2352ClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 6),
    _Gs2352ClientStatKeepAgentOption_Type()
)
gs2352ClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatKeepAgentOption.setStatus("current")
_Gs2352ClientStatDropAgentOption_Type = Counter32
_Gs2352ClientStatDropAgentOption_Object = MibScalar
gs2352ClientStatDropAgentOption = _Gs2352ClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 4, 2, 2, 7),
    _Gs2352ClientStatDropAgentOption_Type()
)
gs2352ClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352ClientStatDropAgentOption.setStatus("current")
_Gs2352PortSecurity_ObjectIdentity = ObjectIdentity
gs2352PortSecurity = _Gs2352PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5)
)
_Gs2352PortSecLimitCtrl_ObjectIdentity = ObjectIdentity
gs2352PortSecLimitCtrl = _Gs2352PortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1)
)
_Gs2352PortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2352PortSecLimitCtrlSystemConf = _Gs2352PortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 1)
)


class _Gs2352PortSecurityMode_Type(Integer32):
    """Custom type gs2352PortSecurityMode based on Integer32"""
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


_Gs2352PortSecurityMode_Type.__name__ = "Integer32"
_Gs2352PortSecurityMode_Object = MibScalar
gs2352PortSecurityMode = _Gs2352PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 1, 1),
    _Gs2352PortSecurityMode_Type()
)
gs2352PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecurityMode.setStatus("current")


class _Gs2352PortSecurityAging_Type(Integer32):
    """Custom type gs2352PortSecurityAging based on Integer32"""
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


_Gs2352PortSecurityAging_Type.__name__ = "Integer32"
_Gs2352PortSecurityAging_Object = MibScalar
gs2352PortSecurityAging = _Gs2352PortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 1, 2),
    _Gs2352PortSecurityAging_Type()
)
gs2352PortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecurityAging.setStatus("current")


class _Gs2352PortSecurityAgingPeriod_Type(Integer32):
    """Custom type gs2352PortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Gs2352PortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Gs2352PortSecurityAgingPeriod_Object = MibScalar
gs2352PortSecurityAgingPeriod = _Gs2352PortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 1, 3),
    _Gs2352PortSecurityAgingPeriod_Type()
)
gs2352PortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecurityAgingPeriod.setStatus("current")
_Gs2352PortSecLimitCtrlTable_Object = MibTable
gs2352PortSecLimitCtrlTable = _Gs2352PortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlTable.setStatus("current")
_Gs2352PortSecLimitCtrlEntry_Object = MibTableRow
gs2352PortSecLimitCtrlEntry = _Gs2352PortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1)
)
gs2352PortSecLimitCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352PortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlEntry.setStatus("current")


class _Gs2352PortSecLimitCtrlPort_Type(Integer32):
    """Custom type gs2352PortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Gs2352PortSecLimitCtrlPort_Object = MibTableColumn
gs2352PortSecLimitCtrlPort = _Gs2352PortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1, 1),
    _Gs2352PortSecLimitCtrlPort_Type()
)
gs2352PortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlPort.setStatus("current")


class _Gs2352PortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type gs2352PortSecLimitCtrlPortMode based on Integer32"""
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


_Gs2352PortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Gs2352PortSecLimitCtrlPortMode_Object = MibTableColumn
gs2352PortSecLimitCtrlPortMode = _Gs2352PortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1, 2),
    _Gs2352PortSecLimitCtrlPortMode_Type()
)
gs2352PortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlPortMode.setStatus("current")


class _Gs2352PortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type gs2352PortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2352PortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Gs2352PortSecLimitCtrlPortLimit_Object = MibTableColumn
gs2352PortSecLimitCtrlPortLimit = _Gs2352PortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1, 3),
    _Gs2352PortSecLimitCtrlPortLimit_Type()
)
gs2352PortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlPortLimit.setStatus("current")


class _Gs2352PortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type gs2352PortSecLimitCtrlPortAction based on Integer32"""
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
          ("trap", 1),
          ("shutdown", 2),
          ("trapShutdown", 3))
    )


_Gs2352PortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Gs2352PortSecLimitCtrlPortAction_Object = MibTableColumn
gs2352PortSecLimitCtrlPortAction = _Gs2352PortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1, 4),
    _Gs2352PortSecLimitCtrlPortAction_Type()
)
gs2352PortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlPortAction.setStatus("current")
_Gs2352PortSecLimitCtrlPortState_Type = DisplayString
_Gs2352PortSecLimitCtrlPortState_Object = MibTableColumn
gs2352PortSecLimitCtrlPortState = _Gs2352PortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1, 5),
    _Gs2352PortSecLimitCtrlPortState_Type()
)
gs2352PortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlPortState.setStatus("current")


class _Gs2352PortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type gs2352PortSecLimitCtrlPortReOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reopen", 1))
    )


_Gs2352PortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Gs2352PortSecLimitCtrlPortReOpen_Object = MibTableColumn
gs2352PortSecLimitCtrlPortReOpen = _Gs2352PortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 1, 2, 1, 6),
    _Gs2352PortSecLimitCtrlPortReOpen_Type()
)
gs2352PortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecLimitCtrlPortReOpen.setStatus("current")
_Gs2352PortSecSwitchStatusTable_Object = MibTable
gs2352PortSecSwitchStatusTable = _Gs2352PortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusTable.setStatus("current")
_Gs2352PortSecSwitchStatusEntry_Object = MibTableRow
gs2352PortSecSwitchStatusEntry = _Gs2352PortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2, 1)
)
gs2352PortSecSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352PortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusEntry.setStatus("current")


class _Gs2352PortSecSwitchStatusPort_Type(Integer32):
    """Custom type gs2352PortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Gs2352PortSecSwitchStatusPort_Object = MibTableColumn
gs2352PortSecSwitchStatusPort = _Gs2352PortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2, 1, 1),
    _Gs2352PortSecSwitchStatusPort_Type()
)
gs2352PortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusPort.setStatus("current")
_Gs2352PortSecSwitchStatusUsers_Type = DisplayString
_Gs2352PortSecSwitchStatusUsers_Object = MibTableColumn
gs2352PortSecSwitchStatusUsers = _Gs2352PortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2, 1, 2),
    _Gs2352PortSecSwitchStatusUsers_Type()
)
gs2352PortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusUsers.setStatus("current")
_Gs2352PortSecSwitchStatusState_Type = DisplayString
_Gs2352PortSecSwitchStatusState_Object = MibTableColumn
gs2352PortSecSwitchStatusState = _Gs2352PortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2, 1, 3),
    _Gs2352PortSecSwitchStatusState_Type()
)
gs2352PortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusState.setStatus("current")


class _Gs2352PortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type gs2352PortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Gs2352PortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
gs2352PortSecSwitchStatusMACCountCurrent = _Gs2352PortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2, 1, 4),
    _Gs2352PortSecSwitchStatusMACCountCurrent_Type()
)
gs2352PortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Gs2352PortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type gs2352PortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Gs2352PortSecSwitchStatusMACCountLimit_Object = MibTableColumn
gs2352PortSecSwitchStatusMACCountLimit = _Gs2352PortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 2, 1, 5),
    _Gs2352PortSecSwitchStatusMACCountLimit_Type()
)
gs2352PortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecSwitchStatusMACCountLimit.setStatus("current")
_Gs2352PortSecPortStatus_ObjectIdentity = ObjectIdentity
gs2352PortSecPortStatus = _Gs2352PortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3)
)


class _Gs2352PortSecPortStatusPort_Type(Integer32):
    """Custom type gs2352PortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortSecPortStatusPort_Type.__name__ = "Integer32"
_Gs2352PortSecPortStatusPort_Object = MibScalar
gs2352PortSecPortStatusPort = _Gs2352PortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 1),
    _Gs2352PortSecPortStatusPort_Type()
)
gs2352PortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusPort.setStatus("current")
_Gs2352PortSecPortStatusTable_Object = MibTable
gs2352PortSecPortStatusTable = _Gs2352PortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusTable.setStatus("current")
_Gs2352PortSecPortStatusEntry_Object = MibTableRow
gs2352PortSecPortStatusEntry = _Gs2352PortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1)
)
gs2352PortSecPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352PortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusEntry.setStatus("current")


class _Gs2352PortSecPortStatusIndex_Type(Integer32):
    """Custom type gs2352PortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352PortSecPortStatusIndex_Type.__name__ = "Integer32"
_Gs2352PortSecPortStatusIndex_Object = MibTableColumn
gs2352PortSecPortStatusIndex = _Gs2352PortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1, 1),
    _Gs2352PortSecPortStatusIndex_Type()
)
gs2352PortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusIndex.setStatus("current")
_Gs2352PortSecPortStatusMACAddress_Type = MacAddress
_Gs2352PortSecPortStatusMACAddress_Object = MibTableColumn
gs2352PortSecPortStatusMACAddress = _Gs2352PortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1, 2),
    _Gs2352PortSecPortStatusMACAddress_Type()
)
gs2352PortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusMACAddress.setStatus("current")


class _Gs2352PortSecPortStatusVLANId_Type(Integer32):
    """Custom type gs2352PortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352PortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Gs2352PortSecPortStatusVLANId_Object = MibTableColumn
gs2352PortSecPortStatusVLANId = _Gs2352PortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1, 3),
    _Gs2352PortSecPortStatusVLANId_Type()
)
gs2352PortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusVLANId.setStatus("current")
_Gs2352PortSecPortStatusState_Type = DisplayString
_Gs2352PortSecPortStatusState_Object = MibTableColumn
gs2352PortSecPortStatusState = _Gs2352PortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1, 4),
    _Gs2352PortSecPortStatusState_Type()
)
gs2352PortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusState.setStatus("current")
_Gs2352PortSecPortStatusTimeOfAddition_Type = DisplayString
_Gs2352PortSecPortStatusTimeOfAddition_Object = MibTableColumn
gs2352PortSecPortStatusTimeOfAddition = _Gs2352PortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1, 5),
    _Gs2352PortSecPortStatusTimeOfAddition_Type()
)
gs2352PortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusTimeOfAddition.setStatus("current")
_Gs2352PortSecPortStatusAgeAndHold_Type = DisplayString
_Gs2352PortSecPortStatusAgeAndHold_Object = MibTableColumn
gs2352PortSecPortStatusAgeAndHold = _Gs2352PortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 5, 3, 2, 1, 6),
    _Gs2352PortSecPortStatusAgeAndHold_Type()
)
gs2352PortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PortSecPortStatusAgeAndHold.setStatus("current")
_Gs2352AccessManagement_ObjectIdentity = ObjectIdentity
gs2352AccessManagement = _Gs2352AccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6)
)
_Gs2352AccessMgtConf_ObjectIdentity = ObjectIdentity
gs2352AccessMgtConf = _Gs2352AccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1)
)


class _Gs2352AccessMgtConfMode_Type(Integer32):
    """Custom type gs2352AccessMgtConfMode based on Integer32"""
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


_Gs2352AccessMgtConfMode_Type.__name__ = "Integer32"
_Gs2352AccessMgtConfMode_Object = MibScalar
gs2352AccessMgtConfMode = _Gs2352AccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 1),
    _Gs2352AccessMgtConfMode_Type()
)
gs2352AccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtConfMode.setStatus("current")


class _Gs2352AccessMgtConfCreate_Type(Integer32):
    """Custom type gs2352AccessMgtConfCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("create", 1))
    )


_Gs2352AccessMgtConfCreate_Type.__name__ = "Integer32"
_Gs2352AccessMgtConfCreate_Object = MibScalar
gs2352AccessMgtConfCreate = _Gs2352AccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 2),
    _Gs2352AccessMgtConfCreate_Type()
)
gs2352AccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtConfCreate.setStatus("current")
_Gs2352AccessMgtConfTable_Object = MibTable
gs2352AccessMgtConfTable = _Gs2352AccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    gs2352AccessMgtConfTable.setStatus("current")
_Gs2352AccessMgtConfEntry_Object = MibTableRow
gs2352AccessMgtConfEntry = _Gs2352AccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1)
)
gs2352AccessMgtConfEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352AccessMgtIndex"),
)
if mibBuilder.loadTexts:
    gs2352AccessMgtConfEntry.setStatus("current")


class _Gs2352AccessMgtIndex_Type(Integer32):
    """Custom type gs2352AccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2352AccessMgtIndex_Type.__name__ = "Integer32"
_Gs2352AccessMgtIndex_Object = MibTableColumn
gs2352AccessMgtIndex = _Gs2352AccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 1),
    _Gs2352AccessMgtIndex_Type()
)
gs2352AccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtIndex.setStatus("current")


class _Gs2352AccessMgtAddresstype_Type(Integer32):
    """Custom type gs2352AccessMgtAddresstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_Gs2352AccessMgtAddresstype_Type.__name__ = "Integer32"
_Gs2352AccessMgtAddresstype_Object = MibTableColumn
gs2352AccessMgtAddresstype = _Gs2352AccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 2),
    _Gs2352AccessMgtAddresstype_Type()
)
gs2352AccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtAddresstype.setStatus("current")
_Gs2352AccessMgtStartIpAddress_Type = DisplayString
_Gs2352AccessMgtStartIpAddress_Object = MibTableColumn
gs2352AccessMgtStartIpAddress = _Gs2352AccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 3),
    _Gs2352AccessMgtStartIpAddress_Type()
)
gs2352AccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtStartIpAddress.setStatus("current")
_Gs2352AccessMgtEndIpAddress_Type = DisplayString
_Gs2352AccessMgtEndIpAddress_Object = MibTableColumn
gs2352AccessMgtEndIpAddress = _Gs2352AccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 4),
    _Gs2352AccessMgtEndIpAddress_Type()
)
gs2352AccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtEndIpAddress.setStatus("current")


class _Gs2352AccessMgtHttpHttps_Type(Integer32):
    """Custom type gs2352AccessMgtHttpHttps based on Integer32"""
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


_Gs2352AccessMgtHttpHttps_Type.__name__ = "Integer32"
_Gs2352AccessMgtHttpHttps_Object = MibTableColumn
gs2352AccessMgtHttpHttps = _Gs2352AccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 5),
    _Gs2352AccessMgtHttpHttps_Type()
)
gs2352AccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtHttpHttps.setStatus("current")


class _Gs2352AccessMgtSNMP_Type(Integer32):
    """Custom type gs2352AccessMgtSNMP based on Integer32"""
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


_Gs2352AccessMgtSNMP_Type.__name__ = "Integer32"
_Gs2352AccessMgtSNMP_Object = MibTableColumn
gs2352AccessMgtSNMP = _Gs2352AccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 6),
    _Gs2352AccessMgtSNMP_Type()
)
gs2352AccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtSNMP.setStatus("current")


class _Gs2352AccessMgtTelnetSSH_Type(Integer32):
    """Custom type gs2352AccessMgtTelnetSSH based on Integer32"""
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


_Gs2352AccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Gs2352AccessMgtTelnetSSH_Object = MibTableColumn
gs2352AccessMgtTelnetSSH = _Gs2352AccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 7),
    _Gs2352AccessMgtTelnetSSH_Type()
)
gs2352AccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtTelnetSSH.setStatus("current")


class _Gs2352AccessMgtRowStatus_Type(Integer32):
    """Custom type gs2352AccessMgtRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInservice", 2),
          ("edit", 3),
          ("destroy", 4),
          ("undo", 5))
    )


_Gs2352AccessMgtRowStatus_Type.__name__ = "Integer32"
_Gs2352AccessMgtRowStatus_Object = MibTableColumn
gs2352AccessMgtRowStatus = _Gs2352AccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 1, 3, 1, 8),
    _Gs2352AccessMgtRowStatus_Type()
)
gs2352AccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtRowStatus.setStatus("current")
_Gs2352AccessMgtStatistics_ObjectIdentity = ObjectIdentity
gs2352AccessMgtStatistics = _Gs2352AccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2)
)
_Gs2352HttpReceivedPkts_Type = Counter32
_Gs2352HttpReceivedPkts_Object = MibScalar
gs2352HttpReceivedPkts = _Gs2352HttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 1),
    _Gs2352HttpReceivedPkts_Type()
)
gs2352HttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HttpReceivedPkts.setStatus("current")
_Gs2352HttpAllowedPkts_Type = Counter32
_Gs2352HttpAllowedPkts_Object = MibScalar
gs2352HttpAllowedPkts = _Gs2352HttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 2),
    _Gs2352HttpAllowedPkts_Type()
)
gs2352HttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HttpAllowedPkts.setStatus("current")
_Gs2352HttpDiscardedPkts_Type = Counter32
_Gs2352HttpDiscardedPkts_Object = MibScalar
gs2352HttpDiscardedPkts = _Gs2352HttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 3),
    _Gs2352HttpDiscardedPkts_Type()
)
gs2352HttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HttpDiscardedPkts.setStatus("current")
_Gs2352HttpsReceivedPkts_Type = Counter32
_Gs2352HttpsReceivedPkts_Object = MibScalar
gs2352HttpsReceivedPkts = _Gs2352HttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 4),
    _Gs2352HttpsReceivedPkts_Type()
)
gs2352HttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HttpsReceivedPkts.setStatus("current")
_Gs2352HttpsAllowedPkts_Type = Counter32
_Gs2352HttpsAllowedPkts_Object = MibScalar
gs2352HttpsAllowedPkts = _Gs2352HttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 5),
    _Gs2352HttpsAllowedPkts_Type()
)
gs2352HttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HttpsAllowedPkts.setStatus("current")
_Gs2352HttpsDiscardedPkts_Type = Counter32
_Gs2352HttpsDiscardedPkts_Object = MibScalar
gs2352HttpsDiscardedPkts = _Gs2352HttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 6),
    _Gs2352HttpsDiscardedPkts_Type()
)
gs2352HttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352HttpsDiscardedPkts.setStatus("current")
_Gs2352SnmpReceivedPkts_Type = Counter32
_Gs2352SnmpReceivedPkts_Object = MibScalar
gs2352SnmpReceivedPkts = _Gs2352SnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 7),
    _Gs2352SnmpReceivedPkts_Type()
)
gs2352SnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SnmpReceivedPkts.setStatus("current")
_Gs2352SnmpAllowedPkts_Type = Counter32
_Gs2352SnmpAllowedPkts_Object = MibScalar
gs2352SnmpAllowedPkts = _Gs2352SnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 8),
    _Gs2352SnmpAllowedPkts_Type()
)
gs2352SnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SnmpAllowedPkts.setStatus("current")
_Gs2352SnmpDiscardedPkts_Type = Counter32
_Gs2352SnmpDiscardedPkts_Object = MibScalar
gs2352SnmpDiscardedPkts = _Gs2352SnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 9),
    _Gs2352SnmpDiscardedPkts_Type()
)
gs2352SnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SnmpDiscardedPkts.setStatus("current")
_Gs2352TelnetReceivedPkts_Type = Counter32
_Gs2352TelnetReceivedPkts_Object = MibScalar
gs2352TelnetReceivedPkts = _Gs2352TelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 10),
    _Gs2352TelnetReceivedPkts_Type()
)
gs2352TelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352TelnetReceivedPkts.setStatus("current")
_Gs2352TelnetAllowedPkts_Type = Counter32
_Gs2352TelnetAllowedPkts_Object = MibScalar
gs2352TelnetAllowedPkts = _Gs2352TelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 11),
    _Gs2352TelnetAllowedPkts_Type()
)
gs2352TelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352TelnetAllowedPkts.setStatus("current")
_Gs2352TelnetDiscardedPkts_Type = Counter32
_Gs2352TelnetDiscardedPkts_Object = MibScalar
gs2352TelnetDiscardedPkts = _Gs2352TelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 12),
    _Gs2352TelnetDiscardedPkts_Type()
)
gs2352TelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352TelnetDiscardedPkts.setStatus("current")
_Gs2352SSHReceivedPkts_Type = Counter32
_Gs2352SSHReceivedPkts_Object = MibScalar
gs2352SSHReceivedPkts = _Gs2352SSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 13),
    _Gs2352SSHReceivedPkts_Type()
)
gs2352SSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SSHReceivedPkts.setStatus("current")
_Gs2352SSHAllowedPkts_Type = Counter32
_Gs2352SSHAllowedPkts_Object = MibScalar
gs2352SSHAllowedPkts = _Gs2352SSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 14),
    _Gs2352SSHAllowedPkts_Type()
)
gs2352SSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SSHAllowedPkts.setStatus("current")
_Gs2352SSHDiscardedPkts_Type = Counter32
_Gs2352SSHDiscardedPkts_Object = MibScalar
gs2352SSHDiscardedPkts = _Gs2352SSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 15),
    _Gs2352SSHDiscardedPkts_Type()
)
gs2352SSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352SSHDiscardedPkts.setStatus("current")


class _Gs2352AccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type gs2352AccessMgtStatisticsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_Gs2352AccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Gs2352AccessMgtStatisticsClearAll_Object = MibScalar
gs2352AccessMgtStatisticsClearAll = _Gs2352AccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 6, 2, 16),
    _Gs2352AccessMgtStatisticsClearAll_Type()
)
gs2352AccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AccessMgtStatisticsClearAll.setStatus("current")
_Gs2352SSH_ObjectIdentity = ObjectIdentity
gs2352SSH = _Gs2352SSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 7)
)


class _Gs2352SSHMode_Type(Integer32):
    """Custom type gs2352SSHMode based on Integer32"""
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


_Gs2352SSHMode_Type.__name__ = "Integer32"
_Gs2352SSHMode_Object = MibScalar
gs2352SSHMode = _Gs2352SSHMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 7, 1),
    _Gs2352SSHMode_Type()
)
gs2352SSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SSHMode.setStatus("current")
_Gs2352HTTPS_ObjectIdentity = ObjectIdentity
gs2352HTTPS = _Gs2352HTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 8)
)


class _Gs2352HTTPSMode_Type(Integer32):
    """Custom type gs2352HTTPSMode based on Integer32"""
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


_Gs2352HTTPSMode_Type.__name__ = "Integer32"
_Gs2352HTTPSMode_Object = MibScalar
gs2352HTTPSMode = _Gs2352HTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 8, 1),
    _Gs2352HTTPSMode_Type()
)
gs2352HTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HTTPSMode.setStatus("current")


class _Gs2352HTTPSAutoRedirect_Type(Integer32):
    """Custom type gs2352HTTPSAutoRedirect based on Integer32"""
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


_Gs2352HTTPSAutoRedirect_Type.__name__ = "Integer32"
_Gs2352HTTPSAutoRedirect_Object = MibScalar
gs2352HTTPSAutoRedirect = _Gs2352HTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 8, 2),
    _Gs2352HTTPSAutoRedirect_Type()
)
gs2352HTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HTTPSAutoRedirect.setStatus("current")


class _Gs2352HTTPSCertRenew_Type(Integer32):
    """Custom type gs2352HTTPSCertRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("renew", 1))
    )


_Gs2352HTTPSCertRenew_Type.__name__ = "Integer32"
_Gs2352HTTPSCertRenew_Object = MibScalar
gs2352HTTPSCertRenew = _Gs2352HTTPSCertRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 8, 3),
    _Gs2352HTTPSCertRenew_Type()
)
gs2352HTTPSCertRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HTTPSCertRenew.setStatus("current")


class _Gs2352HTTPSMinProtoVersion_Type(Integer32):
    """Custom type gs2352HTTPSMinProtoVersion based on Integer32"""
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
        *(("SSLv3", 0),
          ("TLSv1", 1),
          ("TLSv11", 2),
          ("TLSv12", 3))
    )


_Gs2352HTTPSMinProtoVersion_Type.__name__ = "Integer32"
_Gs2352HTTPSMinProtoVersion_Object = MibScalar
gs2352HTTPSMinProtoVersion = _Gs2352HTTPSMinProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 8, 4),
    _Gs2352HTTPSMinProtoVersion_Type()
)
gs2352HTTPSMinProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HTTPSMinProtoVersion.setStatus("current")


class _Gs2352HTTPMode_Type(Integer32):
    """Custom type gs2352HTTPMode based on Integer32"""
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


_Gs2352HTTPMode_Type.__name__ = "Integer32"
_Gs2352HTTPMode_Object = MibScalar
gs2352HTTPMode = _Gs2352HTTPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 8, 5),
    _Gs2352HTTPMode_Type()
)
gs2352HTTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HTTPMode.setStatus("current")
_Gs2352AuthMethod_ObjectIdentity = ObjectIdentity
gs2352AuthMethod = _Gs2352AuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9)
)


class _Gs2352ConsoleAuthMethod_Type(Integer32):
    """Custom type gs2352ConsoleAuthMethod based on Integer32"""
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
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_Gs2352ConsoleAuthMethod_Type.__name__ = "Integer32"
_Gs2352ConsoleAuthMethod_Object = MibScalar
gs2352ConsoleAuthMethod = _Gs2352ConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 1),
    _Gs2352ConsoleAuthMethod_Type()
)
gs2352ConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ConsoleAuthMethod.setStatus("current")


class _Gs2352ConsoleFallback_Type(Integer32):
    """Custom type gs2352ConsoleFallback based on Integer32"""
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


_Gs2352ConsoleFallback_Type.__name__ = "Integer32"
_Gs2352ConsoleFallback_Object = MibScalar
gs2352ConsoleFallback = _Gs2352ConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 2),
    _Gs2352ConsoleFallback_Type()
)
gs2352ConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ConsoleFallback.setStatus("current")


class _Gs2352TelnetAuthMethod_Type(Integer32):
    """Custom type gs2352TelnetAuthMethod based on Integer32"""
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
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_Gs2352TelnetAuthMethod_Type.__name__ = "Integer32"
_Gs2352TelnetAuthMethod_Object = MibScalar
gs2352TelnetAuthMethod = _Gs2352TelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 3),
    _Gs2352TelnetAuthMethod_Type()
)
gs2352TelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TelnetAuthMethod.setStatus("current")


class _Gs2352TelnetFallback_Type(Integer32):
    """Custom type gs2352TelnetFallback based on Integer32"""
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


_Gs2352TelnetFallback_Type.__name__ = "Integer32"
_Gs2352TelnetFallback_Object = MibScalar
gs2352TelnetFallback = _Gs2352TelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 4),
    _Gs2352TelnetFallback_Type()
)
gs2352TelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TelnetFallback.setStatus("current")


class _Gs2352SshAuthMethod_Type(Integer32):
    """Custom type gs2352SshAuthMethod based on Integer32"""
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
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_Gs2352SshAuthMethod_Type.__name__ = "Integer32"
_Gs2352SshAuthMethod_Object = MibScalar
gs2352SshAuthMethod = _Gs2352SshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 5),
    _Gs2352SshAuthMethod_Type()
)
gs2352SshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SshAuthMethod.setStatus("current")


class _Gs2352SshFallback_Type(Integer32):
    """Custom type gs2352SshFallback based on Integer32"""
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


_Gs2352SshFallback_Type.__name__ = "Integer32"
_Gs2352SshFallback_Object = MibScalar
gs2352SshFallback = _Gs2352SshFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 6),
    _Gs2352SshFallback_Type()
)
gs2352SshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SshFallback.setStatus("current")


class _Gs2352TftpAuthMethod_Type(Integer32):
    """Custom type gs2352TftpAuthMethod based on Integer32"""
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
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_Gs2352TftpAuthMethod_Type.__name__ = "Integer32"
_Gs2352TftpAuthMethod_Object = MibScalar
gs2352TftpAuthMethod = _Gs2352TftpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 9),
    _Gs2352TftpAuthMethod_Type()
)
gs2352TftpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TftpAuthMethod.setStatus("current")


class _Gs2352TftpFallback_Type(Integer32):
    """Custom type gs2352TftpFallback based on Integer32"""
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


_Gs2352TftpFallback_Type.__name__ = "Integer32"
_Gs2352TftpFallback_Object = MibScalar
gs2352TftpFallback = _Gs2352TftpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 10),
    _Gs2352TftpFallback_Type()
)
gs2352TftpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TftpFallback.setStatus("current")


class _Gs2352LoginFailures_Type(Integer32):
    """Custom type gs2352LoginFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Gs2352LoginFailures_Type.__name__ = "Integer32"
_Gs2352LoginFailures_Object = MibScalar
gs2352LoginFailures = _Gs2352LoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 11),
    _Gs2352LoginFailures_Type()
)
gs2352LoginFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LoginFailures.setStatus("current")


class _Gs2352LockMinutes_Type(Integer32):
    """Custom type gs2352LockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Gs2352LockMinutes_Type.__name__ = "Integer32"
_Gs2352LockMinutes_Object = MibScalar
gs2352LockMinutes = _Gs2352LockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 12),
    _Gs2352LockMinutes_Type()
)
gs2352LockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352LockMinutes.setStatus("current")


class _Gs2352HttpAuthMethod_Type(Integer32):
    """Custom type gs2352HttpAuthMethod based on Integer32"""
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
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_Gs2352HttpAuthMethod_Type.__name__ = "Integer32"
_Gs2352HttpAuthMethod_Object = MibScalar
gs2352HttpAuthMethod = _Gs2352HttpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 13),
    _Gs2352HttpAuthMethod_Type()
)
gs2352HttpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HttpAuthMethod.setStatus("current")


class _Gs2352HttpFallback_Type(Integer32):
    """Custom type gs2352HttpFallback based on Integer32"""
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


_Gs2352HttpFallback_Type.__name__ = "Integer32"
_Gs2352HttpFallback_Object = MibScalar
gs2352HttpFallback = _Gs2352HttpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 14),
    _Gs2352HttpFallback_Type()
)
gs2352HttpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HttpFallback.setStatus("current")


class _Gs2352HttpsAuthMethod_Type(Integer32):
    """Custom type gs2352HttpsAuthMethod based on Integer32"""
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
          ("local", 1),
          ("radius", 2),
          ("tacacsplus", 3))
    )


_Gs2352HttpsAuthMethod_Type.__name__ = "Integer32"
_Gs2352HttpsAuthMethod_Object = MibScalar
gs2352HttpsAuthMethod = _Gs2352HttpsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 15),
    _Gs2352HttpsAuthMethod_Type()
)
gs2352HttpsAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HttpsAuthMethod.setStatus("current")


class _Gs2352HttpsFallback_Type(Integer32):
    """Custom type gs2352HttpsFallback based on Integer32"""
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


_Gs2352HttpsFallback_Type.__name__ = "Integer32"
_Gs2352HttpsFallback_Object = MibScalar
gs2352HttpsFallback = _Gs2352HttpsFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 9, 16),
    _Gs2352HttpsFallback_Type()
)
gs2352HttpsFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352HttpsFallback.setStatus("current")
_Gs2352AAA_ObjectIdentity = ObjectIdentity
gs2352AAA = _Gs2352AAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10)
)
_Gs2352AAACommonServer_ObjectIdentity = ObjectIdentity
gs2352AAACommonServer = _Gs2352AAACommonServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 1)
)


class _Gs2352AAACommonServerTimeout_Type(Integer32):
    """Custom type gs2352AAACommonServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_Gs2352AAACommonServerTimeout_Type.__name__ = "Integer32"
_Gs2352AAACommonServerTimeout_Object = MibScalar
gs2352AAACommonServerTimeout = _Gs2352AAACommonServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 1, 1),
    _Gs2352AAACommonServerTimeout_Type()
)
gs2352AAACommonServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AAACommonServerTimeout.setStatus("current")


class _Gs2352AAACommonServerDeadTime_Type(Integer32):
    """Custom type gs2352AAACommonServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Gs2352AAACommonServerDeadTime_Type.__name__ = "Integer32"
_Gs2352AAACommonServerDeadTime_Object = MibScalar
gs2352AAACommonServerDeadTime = _Gs2352AAACommonServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 1, 2),
    _Gs2352AAACommonServerDeadTime_Type()
)
gs2352AAACommonServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AAACommonServerDeadTime.setStatus("current")
_Gs2352AAATACACSPlusAuthAndAccounting_ObjectIdentity = ObjectIdentity
gs2352AAATACACSPlusAuthAndAccounting = _Gs2352AAATACACSPlusAuthAndAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 2)
)


class _Gs2352AAAAuthorization_Type(Integer32):
    """Custom type gs2352AAAAuthorization based on Integer32"""
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


_Gs2352AAAAuthorization_Type.__name__ = "Integer32"
_Gs2352AAAAuthorization_Object = MibScalar
gs2352AAAAuthorization = _Gs2352AAAAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 2, 1),
    _Gs2352AAAAuthorization_Type()
)
gs2352AAAAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AAAAuthorization.setStatus("current")


class _Gs2352AAAFallbackToLocalAuthorization_Type(Integer32):
    """Custom type gs2352AAAFallbackToLocalAuthorization based on Integer32"""
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


_Gs2352AAAFallbackToLocalAuthorization_Type.__name__ = "Integer32"
_Gs2352AAAFallbackToLocalAuthorization_Object = MibScalar
gs2352AAAFallbackToLocalAuthorization = _Gs2352AAAFallbackToLocalAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 2, 2),
    _Gs2352AAAFallbackToLocalAuthorization_Type()
)
gs2352AAAFallbackToLocalAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AAAFallbackToLocalAuthorization.setStatus("current")


class _Gs2352AAAAccounting_Type(Integer32):
    """Custom type gs2352AAAAccounting based on Integer32"""
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


_Gs2352AAAAccounting_Type.__name__ = "Integer32"
_Gs2352AAAAccounting_Object = MibScalar
gs2352AAAAccounting = _Gs2352AAAAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 2, 3),
    _Gs2352AAAAccounting_Type()
)
gs2352AAAAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352AAAAccounting.setStatus("current")
_Gs2352RADIUSAuthenticationServerTable_Object = MibTable
gs2352RADIUSAuthenticationServerTable = _Gs2352RADIUSAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3)
)
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerTable.setStatus("current")
_Gs2352RADIUSAuthenticationServerEntry_Object = MibTableRow
gs2352RADIUSAuthenticationServerEntry = _Gs2352RADIUSAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3, 1)
)
gs2352RADIUSAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352RADIUSAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerEntry.setStatus("current")


class _Gs2352RADIUSAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2352RADIUSAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2352RADIUSAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2352RADIUSAuthenticationServerIndex_Object = MibTableColumn
gs2352RADIUSAuthenticationServerIndex = _Gs2352RADIUSAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3, 1, 1),
    _Gs2352RADIUSAuthenticationServerIndex_Type()
)
gs2352RADIUSAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerIndex.setStatus("current")


class _Gs2352RADIUSAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2352RADIUSAuthenticationServerEnable based on Integer32"""
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


_Gs2352RADIUSAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2352RADIUSAuthenticationServerEnable_Object = MibTableColumn
gs2352RADIUSAuthenticationServerEnable = _Gs2352RADIUSAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3, 1, 2),
    _Gs2352RADIUSAuthenticationServerEnable_Type()
)
gs2352RADIUSAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerEnable.setStatus("current")
_Gs2352RADIUSAuthenticationServerIP_Type = DisplayString
_Gs2352RADIUSAuthenticationServerIP_Object = MibTableColumn
gs2352RADIUSAuthenticationServerIP = _Gs2352RADIUSAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3, 1, 3),
    _Gs2352RADIUSAuthenticationServerIP_Type()
)
gs2352RADIUSAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerIP.setStatus("current")


class _Gs2352RADIUSAuthenticationServerPort_Type(Integer32):
    """Custom type gs2352RADIUSAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2352RADIUSAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2352RADIUSAuthenticationServerPort_Object = MibTableColumn
gs2352RADIUSAuthenticationServerPort = _Gs2352RADIUSAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3, 1, 4),
    _Gs2352RADIUSAuthenticationServerPort_Type()
)
gs2352RADIUSAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerPort.setStatus("current")
_Gs2352RADIUSAuthenticationServerSecret_Type = DisplayString
_Gs2352RADIUSAuthenticationServerSecret_Object = MibTableColumn
gs2352RADIUSAuthenticationServerSecret = _Gs2352RADIUSAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 3, 1, 5),
    _Gs2352RADIUSAuthenticationServerSecret_Type()
)
gs2352RADIUSAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthenticationServerSecret.setStatus("current")
_Gs2352RADIUSAccountingServerTable_Object = MibTable
gs2352RADIUSAccountingServerTable = _Gs2352RADIUSAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4)
)
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerTable.setStatus("current")
_Gs2352RADIUSAccountingServerEntry_Object = MibTableRow
gs2352RADIUSAccountingServerEntry = _Gs2352RADIUSAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4, 1)
)
gs2352RADIUSAccountingServerEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352RADIUSAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerEntry.setStatus("current")


class _Gs2352RADIUSAccountingServerIndex_Type(Integer32):
    """Custom type gs2352RADIUSAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2352RADIUSAccountingServerIndex_Type.__name__ = "Integer32"
_Gs2352RADIUSAccountingServerIndex_Object = MibTableColumn
gs2352RADIUSAccountingServerIndex = _Gs2352RADIUSAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4, 1, 1),
    _Gs2352RADIUSAccountingServerIndex_Type()
)
gs2352RADIUSAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerIndex.setStatus("current")


class _Gs2352RADIUSAccountingServerEnable_Type(Integer32):
    """Custom type gs2352RADIUSAccountingServerEnable based on Integer32"""
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


_Gs2352RADIUSAccountingServerEnable_Type.__name__ = "Integer32"
_Gs2352RADIUSAccountingServerEnable_Object = MibTableColumn
gs2352RADIUSAccountingServerEnable = _Gs2352RADIUSAccountingServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4, 1, 2),
    _Gs2352RADIUSAccountingServerEnable_Type()
)
gs2352RADIUSAccountingServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerEnable.setStatus("current")
_Gs2352RADIUSAccountingServerIP_Type = DisplayString
_Gs2352RADIUSAccountingServerIP_Object = MibTableColumn
gs2352RADIUSAccountingServerIP = _Gs2352RADIUSAccountingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4, 1, 3),
    _Gs2352RADIUSAccountingServerIP_Type()
)
gs2352RADIUSAccountingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerIP.setStatus("current")


class _Gs2352RADIUSAccountingServerPort_Type(Integer32):
    """Custom type gs2352RADIUSAccountingServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2352RADIUSAccountingServerPort_Type.__name__ = "Integer32"
_Gs2352RADIUSAccountingServerPort_Object = MibTableColumn
gs2352RADIUSAccountingServerPort = _Gs2352RADIUSAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4, 1, 4),
    _Gs2352RADIUSAccountingServerPort_Type()
)
gs2352RADIUSAccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerPort.setStatus("current")
_Gs2352RADIUSAccountingServerSecret_Type = DisplayString
_Gs2352RADIUSAccountingServerSecret_Object = MibTableColumn
gs2352RADIUSAccountingServerSecret = _Gs2352RADIUSAccountingServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 4, 1, 5),
    _Gs2352RADIUSAccountingServerSecret_Type()
)
gs2352RADIUSAccountingServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingServerSecret.setStatus("current")
_Gs2352TACACSPlusAuthenticationServerTable_Object = MibTable
gs2352TACACSPlusAuthenticationServerTable = _Gs2352TACACSPlusAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5)
)
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerTable.setStatus("current")
_Gs2352TACACSPlusAuthenticationServerEntry_Object = MibTableRow
gs2352TACACSPlusAuthenticationServerEntry = _Gs2352TACACSPlusAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5, 1)
)
gs2352TACACSPlusAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352TACACSPlusAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerEntry.setStatus("current")


class _Gs2352TACACSPlusAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2352TACACSPlusAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2352TACACSPlusAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2352TACACSPlusAuthenticationServerIndex_Object = MibTableColumn
gs2352TACACSPlusAuthenticationServerIndex = _Gs2352TACACSPlusAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5, 1, 1),
    _Gs2352TACACSPlusAuthenticationServerIndex_Type()
)
gs2352TACACSPlusAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerIndex.setStatus("current")


class _Gs2352TACACSPlusAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2352TACACSPlusAuthenticationServerEnable based on Integer32"""
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


_Gs2352TACACSPlusAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2352TACACSPlusAuthenticationServerEnable_Object = MibTableColumn
gs2352TACACSPlusAuthenticationServerEnable = _Gs2352TACACSPlusAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5, 1, 2),
    _Gs2352TACACSPlusAuthenticationServerEnable_Type()
)
gs2352TACACSPlusAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerEnable.setStatus("current")
_Gs2352TACACSPlusAuthenticationServerIP_Type = DisplayString
_Gs2352TACACSPlusAuthenticationServerIP_Object = MibTableColumn
gs2352TACACSPlusAuthenticationServerIP = _Gs2352TACACSPlusAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5, 1, 3),
    _Gs2352TACACSPlusAuthenticationServerIP_Type()
)
gs2352TACACSPlusAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerIP.setStatus("current")


class _Gs2352TACACSPlusAuthenticationServerPort_Type(Integer32):
    """Custom type gs2352TACACSPlusAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2352TACACSPlusAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2352TACACSPlusAuthenticationServerPort_Object = MibTableColumn
gs2352TACACSPlusAuthenticationServerPort = _Gs2352TACACSPlusAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5, 1, 4),
    _Gs2352TACACSPlusAuthenticationServerPort_Type()
)
gs2352TACACSPlusAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerPort.setStatus("current")
_Gs2352TACACSPlusAuthenticationServerSecret_Type = DisplayString
_Gs2352TACACSPlusAuthenticationServerSecret_Object = MibTableColumn
gs2352TACACSPlusAuthenticationServerSecret = _Gs2352TACACSPlusAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 5, 1, 5),
    _Gs2352TACACSPlusAuthenticationServerSecret_Type()
)
gs2352TACACSPlusAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352TACACSPlusAuthenticationServerSecret.setStatus("current")
_Gs2352RADIUSStatisticsTable_Object = MibTable
gs2352RADIUSStatisticsTable = _Gs2352RADIUSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6)
)
if mibBuilder.loadTexts:
    gs2352RADIUSStatisticsTable.setStatus("current")
_Gs2352RADIUSStatisticsEntry_Object = MibTableRow
gs2352RADIUSStatisticsEntry = _Gs2352RADIUSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1)
)
gs2352RADIUSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352RADIUSAuthStatisticsServerIndex"),
)
if mibBuilder.loadTexts:
    gs2352RADIUSStatisticsEntry.setStatus("current")


class _Gs2352RADIUSAuthStatisticsServerIndex_Type(Integer32):
    """Custom type gs2352RADIUSAuthStatisticsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2352RADIUSAuthStatisticsServerIndex_Type.__name__ = "Integer32"
_Gs2352RADIUSAuthStatisticsServerIndex_Object = MibTableColumn
gs2352RADIUSAuthStatisticsServerIndex = _Gs2352RADIUSAuthStatisticsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 1),
    _Gs2352RADIUSAuthStatisticsServerIndex_Type()
)
gs2352RADIUSAuthStatisticsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsServerIndex.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktAccessAccepts_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktAccessAccepts_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktAccessAccepts = _Gs2352RADIUSAuthStatisticsRecPktAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 2),
    _Gs2352RADIUSAuthStatisticsRecPktAccessAccepts_Type()
)
gs2352RADIUSAuthStatisticsRecPktAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktAccessAccepts.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktAccessRejects_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktAccessRejects_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktAccessRejects = _Gs2352RADIUSAuthStatisticsRecPktAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 3),
    _Gs2352RADIUSAuthStatisticsRecPktAccessRejects_Type()
)
gs2352RADIUSAuthStatisticsRecPktAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktAccessRejects.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktAccessChallenges_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktAccessChallenges_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktAccessChallenges = _Gs2352RADIUSAuthStatisticsRecPktAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 4),
    _Gs2352RADIUSAuthStatisticsRecPktAccessChallenges_Type()
)
gs2352RADIUSAuthStatisticsRecPktAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktAccessChallenges.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses = _Gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 5),
    _Gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses_Type()
)
gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktBadAuthenticators = _Gs2352RADIUSAuthStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 6),
    _Gs2352RADIUSAuthStatisticsRecPktBadAuthenticators_Type()
)
gs2352RADIUSAuthStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktUnknownTypes = _Gs2352RADIUSAuthStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 7),
    _Gs2352RADIUSAuthStatisticsRecPktUnknownTypes_Type()
)
gs2352RADIUSAuthStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2352RADIUSAuthStatisticsRecPktDropped_Type = Counter32
_Gs2352RADIUSAuthStatisticsRecPktDropped_Object = MibTableColumn
gs2352RADIUSAuthStatisticsRecPktDropped = _Gs2352RADIUSAuthStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 8),
    _Gs2352RADIUSAuthStatisticsRecPktDropped_Type()
)
gs2352RADIUSAuthStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsRecPktDropped.setStatus("current")
_Gs2352RADIUSAuthStatisticsTransmitPktAccessRequests_Type = Counter32
_Gs2352RADIUSAuthStatisticsTransmitPktAccessRequests_Object = MibTableColumn
gs2352RADIUSAuthStatisticsTransmitPktAccessRequests = _Gs2352RADIUSAuthStatisticsTransmitPktAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 9),
    _Gs2352RADIUSAuthStatisticsTransmitPktAccessRequests_Type()
)
gs2352RADIUSAuthStatisticsTransmitPktAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsTransmitPktAccessRequests.setStatus("current")
_Gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type = Counter32
_Gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object = MibTableColumn
gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions = _Gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 10),
    _Gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type()
)
gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setStatus("current")
_Gs2352RADIUSAuthStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2352RADIUSAuthStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2352RADIUSAuthStatisticsTransmitPktPendingRequests = _Gs2352RADIUSAuthStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 11),
    _Gs2352RADIUSAuthStatisticsTransmitPktPendingRequests_Type()
)
gs2352RADIUSAuthStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2352RADIUSAuthStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2352RADIUSAuthStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2352RADIUSAuthStatisticsTransmitPktTimeouts = _Gs2352RADIUSAuthStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 12),
    _Gs2352RADIUSAuthStatisticsTransmitPktTimeouts_Type()
)
gs2352RADIUSAuthStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2352RADIUSAuthIP_Type = DisplayString
_Gs2352RADIUSAuthIP_Object = MibTableColumn
gs2352RADIUSAuthIP = _Gs2352RADIUSAuthIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 13),
    _Gs2352RADIUSAuthIP_Type()
)
gs2352RADIUSAuthIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthIP.setStatus("current")
_Gs2352RADIUSAuthState_Type = DisplayString
_Gs2352RADIUSAuthState_Object = MibTableColumn
gs2352RADIUSAuthState = _Gs2352RADIUSAuthState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 14),
    _Gs2352RADIUSAuthState_Type()
)
gs2352RADIUSAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthState.setStatus("current")
_Gs2352RADIUSAuthRoundTripTime_Type = DisplayString
_Gs2352RADIUSAuthRoundTripTime_Object = MibTableColumn
gs2352RADIUSAuthRoundTripTime = _Gs2352RADIUSAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 15),
    _Gs2352RADIUSAuthRoundTripTime_Type()
)
gs2352RADIUSAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAuthRoundTripTime.setStatus("current")
_Gs2352RADIUSAccountingStatisticsRecPktResponses_Type = Counter32
_Gs2352RADIUSAccountingStatisticsRecPktResponses_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsRecPktResponses = _Gs2352RADIUSAccountingStatisticsRecPktResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 16),
    _Gs2352RADIUSAccountingStatisticsRecPktResponses_Type()
)
gs2352RADIUSAccountingStatisticsRecPktResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsRecPktResponses.setStatus("current")
_Gs2352RADIUSAccountingStatisticsRecPktMalformedResponses_Type = Counter32
_Gs2352RADIUSAccountingStatisticsRecPktMalformedResponses_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsRecPktMalformedResponses = _Gs2352RADIUSAccountingStatisticsRecPktMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 17),
    _Gs2352RADIUSAccountingStatisticsRecPktMalformedResponses_Type()
)
gs2352RADIUSAccountingStatisticsRecPktMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsRecPktMalformedResponses.setStatus("current")
_Gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators = _Gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 18),
    _Gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators_Type()
)
gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2352RADIUSAccountingStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2352RADIUSAccountingStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsRecPktUnknownTypes = _Gs2352RADIUSAccountingStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 19),
    _Gs2352RADIUSAccountingStatisticsRecPktUnknownTypes_Type()
)
gs2352RADIUSAccountingStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2352RADIUSAccountingStatisticsRecPktDropped_Type = Counter32
_Gs2352RADIUSAccountingStatisticsRecPktDropped_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsRecPktDropped = _Gs2352RADIUSAccountingStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 20),
    _Gs2352RADIUSAccountingStatisticsRecPktDropped_Type()
)
gs2352RADIUSAccountingStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsRecPktDropped.setStatus("current")
_Gs2352RADIUSAccountingStatisticsTransmitPktRequests_Type = Counter32
_Gs2352RADIUSAccountingStatisticsTransmitPktRequests_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsTransmitPktRequests = _Gs2352RADIUSAccountingStatisticsTransmitPktRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 21),
    _Gs2352RADIUSAccountingStatisticsTransmitPktRequests_Type()
)
gs2352RADIUSAccountingStatisticsTransmitPktRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsTransmitPktRequests.setStatus("current")
_Gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions_Type = Counter32
_Gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions = _Gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 22),
    _Gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions_Type()
)
gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions.setStatus("current")
_Gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests = _Gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 23),
    _Gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests_Type()
)
gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2352RADIUSAccountingStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2352RADIUSAccountingStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2352RADIUSAccountingStatisticsTransmitPktTimeouts = _Gs2352RADIUSAccountingStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 24),
    _Gs2352RADIUSAccountingStatisticsTransmitPktTimeouts_Type()
)
gs2352RADIUSAccountingStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2352RADIUSAccountingIP_Type = DisplayString
_Gs2352RADIUSAccountingIP_Object = MibTableColumn
gs2352RADIUSAccountingIP = _Gs2352RADIUSAccountingIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 25),
    _Gs2352RADIUSAccountingIP_Type()
)
gs2352RADIUSAccountingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingIP.setStatus("current")
_Gs2352RADIUSAccountingState_Type = DisplayString
_Gs2352RADIUSAccountingState_Object = MibTableColumn
gs2352RADIUSAccountingState = _Gs2352RADIUSAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 26),
    _Gs2352RADIUSAccountingState_Type()
)
gs2352RADIUSAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingState.setStatus("current")
_Gs2352RADIUSAccountingRoundTripTime_Type = DisplayString
_Gs2352RADIUSAccountingRoundTripTime_Object = MibTableColumn
gs2352RADIUSAccountingRoundTripTime = _Gs2352RADIUSAccountingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 27),
    _Gs2352RADIUSAccountingRoundTripTime_Type()
)
gs2352RADIUSAccountingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352RADIUSAccountingRoundTripTime.setStatus("current")


class _Gs2352RADIUSStatisticsClear_Type(Integer32):
    """Custom type gs2352RADIUSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2352RADIUSStatisticsClear_Type.__name__ = "Integer32"
_Gs2352RADIUSStatisticsClear_Object = MibTableColumn
gs2352RADIUSStatisticsClear = _Gs2352RADIUSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 10, 6, 1, 28),
    _Gs2352RADIUSStatisticsClear_Type()
)
gs2352RADIUSStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RADIUSStatisticsClear.setStatus("current")
_Gs2352NAS_ObjectIdentity = ObjectIdentity
gs2352NAS = _Gs2352NAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11)
)
_Gs2352NASConfiguration_ObjectIdentity = ObjectIdentity
gs2352NASConfiguration = _Gs2352NASConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1)
)


class _Gs2352NASConfigMode_Type(Integer32):
    """Custom type gs2352NASConfigMode based on Integer32"""
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


_Gs2352NASConfigMode_Type.__name__ = "Integer32"
_Gs2352NASConfigMode_Object = MibScalar
gs2352NASConfigMode = _Gs2352NASConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 1),
    _Gs2352NASConfigMode_Type()
)
gs2352NASConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigMode.setStatus("current")


class _Gs2352NASConfigReauthEnabled_Type(Integer32):
    """Custom type gs2352NASConfigReauthEnabled based on Integer32"""
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


_Gs2352NASConfigReauthEnabled_Type.__name__ = "Integer32"
_Gs2352NASConfigReauthEnabled_Object = MibScalar
gs2352NASConfigReauthEnabled = _Gs2352NASConfigReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 2),
    _Gs2352NASConfigReauthEnabled_Type()
)
gs2352NASConfigReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigReauthEnabled.setStatus("current")


class _Gs2352NASConfigReauthPeriod_Type(Integer32):
    """Custom type gs2352NASConfigReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Gs2352NASConfigReauthPeriod_Type.__name__ = "Integer32"
_Gs2352NASConfigReauthPeriod_Object = MibScalar
gs2352NASConfigReauthPeriod = _Gs2352NASConfigReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 3),
    _Gs2352NASConfigReauthPeriod_Type()
)
gs2352NASConfigReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigReauthPeriod.setStatus("current")


class _Gs2352NASConfigEAPOLTimeout_Type(Integer32):
    """Custom type gs2352NASConfigEAPOLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2352NASConfigEAPOLTimeout_Type.__name__ = "Integer32"
_Gs2352NASConfigEAPOLTimeout_Object = MibScalar
gs2352NASConfigEAPOLTimeout = _Gs2352NASConfigEAPOLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 4),
    _Gs2352NASConfigEAPOLTimeout_Type()
)
gs2352NASConfigEAPOLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigEAPOLTimeout.setStatus("current")


class _Gs2352NASConfigAgingPeriod_Type(Integer32):
    """Custom type gs2352NASConfigAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2352NASConfigAgingPeriod_Type.__name__ = "Integer32"
_Gs2352NASConfigAgingPeriod_Object = MibScalar
gs2352NASConfigAgingPeriod = _Gs2352NASConfigAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 5),
    _Gs2352NASConfigAgingPeriod_Type()
)
gs2352NASConfigAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigAgingPeriod.setStatus("current")


class _Gs2352NASConfigHoldTime_Type(Integer32):
    """Custom type gs2352NASConfigHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2352NASConfigHoldTime_Type.__name__ = "Integer32"
_Gs2352NASConfigHoldTime_Object = MibScalar
gs2352NASConfigHoldTime = _Gs2352NASConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 6),
    _Gs2352NASConfigHoldTime_Type()
)
gs2352NASConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigHoldTime.setStatus("current")


class _Gs2352NASConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2352NASConfigRADIUSAssignedQoSEnabled based on Integer32"""
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


_Gs2352NASConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2352NASConfigRADIUSAssignedQoSEnabled_Object = MibScalar
gs2352NASConfigRADIUSAssignedQoSEnabled = _Gs2352NASConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 7),
    _Gs2352NASConfigRADIUSAssignedQoSEnabled_Type()
)
gs2352NASConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2352NASConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2352NASConfigRADIUSAssignedVLANEnabled based on Integer32"""
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


_Gs2352NASConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2352NASConfigRADIUSAssignedVLANEnabled_Object = MibScalar
gs2352NASConfigRADIUSAssignedVLANEnabled = _Gs2352NASConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 8),
    _Gs2352NASConfigRADIUSAssignedVLANEnabled_Type()
)
gs2352NASConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2352NASConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2352NASConfigGuestVLANEnabled based on Integer32"""
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


_Gs2352NASConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2352NASConfigGuestVLANEnabled_Object = MibScalar
gs2352NASConfigGuestVLANEnabled = _Gs2352NASConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 9),
    _Gs2352NASConfigGuestVLANEnabled_Type()
)
gs2352NASConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigGuestVLANEnabled.setStatus("current")


class _Gs2352NASConfigGuestVLANID_Type(Integer32):
    """Custom type gs2352NASConfigGuestVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2352NASConfigGuestVLANID_Type.__name__ = "Integer32"
_Gs2352NASConfigGuestVLANID_Object = MibScalar
gs2352NASConfigGuestVLANID = _Gs2352NASConfigGuestVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 10),
    _Gs2352NASConfigGuestVLANID_Type()
)
gs2352NASConfigGuestVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigGuestVLANID.setStatus("current")


class _Gs2352NASConfigMaxReauthCount_Type(Integer32):
    """Custom type gs2352NASConfigMaxReauthCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2352NASConfigMaxReauthCount_Type.__name__ = "Integer32"
_Gs2352NASConfigMaxReauthCount_Object = MibScalar
gs2352NASConfigMaxReauthCount = _Gs2352NASConfigMaxReauthCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 11),
    _Gs2352NASConfigMaxReauthCount_Type()
)
gs2352NASConfigMaxReauthCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigMaxReauthCount.setStatus("current")


class _Gs2352NASConfigAllowGuestVLANEAPOLSeen_Type(Integer32):
    """Custom type gs2352NASConfigAllowGuestVLANEAPOLSeen based on Integer32"""
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


_Gs2352NASConfigAllowGuestVLANEAPOLSeen_Type.__name__ = "Integer32"
_Gs2352NASConfigAllowGuestVLANEAPOLSeen_Object = MibScalar
gs2352NASConfigAllowGuestVLANEAPOLSeen = _Gs2352NASConfigAllowGuestVLANEAPOLSeen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 12),
    _Gs2352NASConfigAllowGuestVLANEAPOLSeen_Type()
)
gs2352NASConfigAllowGuestVLANEAPOLSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigAllowGuestVLANEAPOLSeen.setStatus("current")
_Gs2352NASPortConfigTable_Object = MibTable
gs2352NASPortConfigTable = _Gs2352NASPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13)
)
if mibBuilder.loadTexts:
    gs2352NASPortConfigTable.setStatus("current")
_Gs2352NASPortConfigEntry_Object = MibTableRow
gs2352NASPortConfigEntry = _Gs2352NASPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1)
)
gs2352NASPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2352NASPortConfigEntry.setStatus("current")


class _Gs2352NASPortConfigPort_Type(Integer32):
    """Custom type gs2352NASPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2352NASPortConfigPort_Type.__name__ = "Integer32"
_Gs2352NASPortConfigPort_Object = MibTableColumn
gs2352NASPortConfigPort = _Gs2352NASPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 1),
    _Gs2352NASPortConfigPort_Type()
)
gs2352NASPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352NASPortConfigPort.setStatus("current")


class _Gs2352NASPortConfigAdminState_Type(Integer32):
    """Custom type gs2352NASPortConfigAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("forceAuthorized", 1),
          ("forceUnauthorized", 2),
          ("portBased", 3),
          ("single", 4),
          ("multi", 5),
          ("macBased", 6),
          ("macBasedSingle", 7))
    )


_Gs2352NASPortConfigAdminState_Type.__name__ = "Integer32"
_Gs2352NASPortConfigAdminState_Object = MibTableColumn
gs2352NASPortConfigAdminState = _Gs2352NASPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 2),
    _Gs2352NASPortConfigAdminState_Type()
)
gs2352NASPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigAdminState.setStatus("current")


class _Gs2352NASPortConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2352NASPortConfigRADIUSAssignedQoSEnabled based on Integer32"""
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


_Gs2352NASPortConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2352NASPortConfigRADIUSAssignedQoSEnabled_Object = MibTableColumn
gs2352NASPortConfigRADIUSAssignedQoSEnabled = _Gs2352NASPortConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 3),
    _Gs2352NASPortConfigRADIUSAssignedQoSEnabled_Type()
)
gs2352NASPortConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2352NASPortConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2352NASPortConfigRADIUSAssignedVLANEnabled based on Integer32"""
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


_Gs2352NASPortConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2352NASPortConfigRADIUSAssignedVLANEnabled_Object = MibTableColumn
gs2352NASPortConfigRADIUSAssignedVLANEnabled = _Gs2352NASPortConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 4),
    _Gs2352NASPortConfigRADIUSAssignedVLANEnabled_Type()
)
gs2352NASPortConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2352NASPortConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2352NASPortConfigGuestVLANEnabled based on Integer32"""
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


_Gs2352NASPortConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2352NASPortConfigGuestVLANEnabled_Object = MibTableColumn
gs2352NASPortConfigGuestVLANEnabled = _Gs2352NASPortConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 5),
    _Gs2352NASPortConfigGuestVLANEnabled_Type()
)
gs2352NASPortConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigGuestVLANEnabled.setStatus("current")
_Gs2352NASPortConfigPortState_Type = DisplayString
_Gs2352NASPortConfigPortState_Object = MibTableColumn
gs2352NASPortConfigPortState = _Gs2352NASPortConfigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 6),
    _Gs2352NASPortConfigPortState_Type()
)
gs2352NASPortConfigPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASPortConfigPortState.setStatus("current")


class _Gs2352NASPortConfigReauthenticate_Type(Integer32):
    """Custom type gs2352NASPortConfigReauthenticate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352NASPortConfigReauthenticate_Type.__name__ = "Integer32"
_Gs2352NASPortConfigReauthenticate_Object = MibTableColumn
gs2352NASPortConfigReauthenticate = _Gs2352NASPortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 7),
    _Gs2352NASPortConfigReauthenticate_Type()
)
gs2352NASPortConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigReauthenticate.setStatus("current")


class _Gs2352NASPortConfigReinitialize_Type(Integer32):
    """Custom type gs2352NASPortConfigReinitialize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352NASPortConfigReinitialize_Type.__name__ = "Integer32"
_Gs2352NASPortConfigReinitialize_Object = MibTableColumn
gs2352NASPortConfigReinitialize = _Gs2352NASPortConfigReinitialize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 8),
    _Gs2352NASPortConfigReinitialize_Type()
)
gs2352NASPortConfigReinitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigReinitialize.setStatus("current")


class _Gs2352NASPortConfigFallbackEnabled_Type(Integer32):
    """Custom type gs2352NASPortConfigFallbackEnabled based on Integer32"""
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


_Gs2352NASPortConfigFallbackEnabled_Type.__name__ = "Integer32"
_Gs2352NASPortConfigFallbackEnabled_Object = MibTableColumn
gs2352NASPortConfigFallbackEnabled = _Gs2352NASPortConfigFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 13, 1, 101),
    _Gs2352NASPortConfigFallbackEnabled_Type()
)
gs2352NASPortConfigFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASPortConfigFallbackEnabled.setStatus("current")


class _Gs2352NASConfigMacBasedUseEAP_Type(Integer32):
    """Custom type gs2352NASConfigMacBasedUseEAP based on Integer32"""
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


_Gs2352NASConfigMacBasedUseEAP_Type.__name__ = "Integer32"
_Gs2352NASConfigMacBasedUseEAP_Object = MibScalar
gs2352NASConfigMacBasedUseEAP = _Gs2352NASConfigMacBasedUseEAP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 1, 101),
    _Gs2352NASConfigMacBasedUseEAP_Type()
)
gs2352NASConfigMacBasedUseEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASConfigMacBasedUseEAP.setStatus("current")
_Gs2352NASSwitchStatusTable_Object = MibTable
gs2352NASSwitchStatusTable = _Gs2352NASSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2)
)
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusTable.setStatus("current")
_Gs2352NASSwitchStatusEntry_Object = MibTableRow
gs2352NASSwitchStatusEntry = _Gs2352NASSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1)
)
gs2352NASSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusEntry.setStatus("current")
_Gs2352NASSwitchStatusAdminState_Type = DisplayString
_Gs2352NASSwitchStatusAdminState_Object = MibTableColumn
gs2352NASSwitchStatusAdminState = _Gs2352NASSwitchStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1, 2),
    _Gs2352NASSwitchStatusAdminState_Type()
)
gs2352NASSwitchStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusAdminState.setStatus("current")
_Gs2352NASSwitchStatusPortState_Type = DisplayString
_Gs2352NASSwitchStatusPortState_Object = MibTableColumn
gs2352NASSwitchStatusPortState = _Gs2352NASSwitchStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1, 3),
    _Gs2352NASSwitchStatusPortState_Type()
)
gs2352NASSwitchStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusPortState.setStatus("current")
_Gs2352NASSwitchStatusLastSource_Type = DisplayString
_Gs2352NASSwitchStatusLastSource_Object = MibTableColumn
gs2352NASSwitchStatusLastSource = _Gs2352NASSwitchStatusLastSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1, 4),
    _Gs2352NASSwitchStatusLastSource_Type()
)
gs2352NASSwitchStatusLastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusLastSource.setStatus("current")
_Gs2352NASSwitchStatusLastID_Type = DisplayString
_Gs2352NASSwitchStatusLastID_Object = MibTableColumn
gs2352NASSwitchStatusLastID = _Gs2352NASSwitchStatusLastID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1, 5),
    _Gs2352NASSwitchStatusLastID_Type()
)
gs2352NASSwitchStatusLastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusLastID.setStatus("current")
_Gs2352NASSwitchStatusQoSClass_Type = DisplayString
_Gs2352NASSwitchStatusQoSClass_Object = MibTableColumn
gs2352NASSwitchStatusQoSClass = _Gs2352NASSwitchStatusQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1, 6),
    _Gs2352NASSwitchStatusQoSClass_Type()
)
gs2352NASSwitchStatusQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusQoSClass.setStatus("current")
_Gs2352NASSwitchStatusPortVlanID_Type = DisplayString
_Gs2352NASSwitchStatusPortVlanID_Object = MibTableColumn
gs2352NASSwitchStatusPortVlanID = _Gs2352NASSwitchStatusPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 2, 1, 7),
    _Gs2352NASSwitchStatusPortVlanID_Type()
)
gs2352NASSwitchStatusPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASSwitchStatusPortVlanID.setStatus("current")
_Gs2352NASPortStatus_ObjectIdentity = ObjectIdentity
gs2352NASPortStatus = _Gs2352NASPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3)
)
_Gs2352NASPortStatusCountersTable_Object = MibTable
gs2352NASPortStatusCountersTable = _Gs2352NASPortStatusCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    gs2352NASPortStatusCountersTable.setStatus("current")
_Gs2352NASPortStatusCountersEntry_Object = MibTableRow
gs2352NASPortStatusCountersEntry = _Gs2352NASPortStatusCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1)
)
gs2352NASPortStatusCountersEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2352NASPortStatusCountersEntry.setStatus("current")
_Gs2352NASRxCountersEAPOLTotal_Type = Counter32
_Gs2352NASRxCountersEAPOLTotal_Object = MibTableColumn
gs2352NASRxCountersEAPOLTotal = _Gs2352NASRxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 2),
    _Gs2352NASRxCountersEAPOLTotal_Type()
)
gs2352NASRxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLTotal.setStatus("current")
_Gs2352NASRxCountersEAPOLResponseID_Type = Counter32
_Gs2352NASRxCountersEAPOLResponseID_Object = MibTableColumn
gs2352NASRxCountersEAPOLResponseID = _Gs2352NASRxCountersEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 3),
    _Gs2352NASRxCountersEAPOLResponseID_Type()
)
gs2352NASRxCountersEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLResponseID.setStatus("current")
_Gs2352NASRxCountersEAPOLResponses_Type = Counter32
_Gs2352NASRxCountersEAPOLResponses_Object = MibTableColumn
gs2352NASRxCountersEAPOLResponses = _Gs2352NASRxCountersEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 4),
    _Gs2352NASRxCountersEAPOLResponses_Type()
)
gs2352NASRxCountersEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLResponses.setStatus("current")
_Gs2352NASRxCountersEAPOLStart_Type = Counter32
_Gs2352NASRxCountersEAPOLStart_Object = MibTableColumn
gs2352NASRxCountersEAPOLStart = _Gs2352NASRxCountersEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 5),
    _Gs2352NASRxCountersEAPOLStart_Type()
)
gs2352NASRxCountersEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLStart.setStatus("current")
_Gs2352NASRxCountersEAPOLLogoff_Type = Counter32
_Gs2352NASRxCountersEAPOLLogoff_Object = MibTableColumn
gs2352NASRxCountersEAPOLLogoff = _Gs2352NASRxCountersEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 6),
    _Gs2352NASRxCountersEAPOLLogoff_Type()
)
gs2352NASRxCountersEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLLogoff.setStatus("current")
_Gs2352NASRxCountersEAPOLInvalidType_Type = Counter32
_Gs2352NASRxCountersEAPOLInvalidType_Object = MibTableColumn
gs2352NASRxCountersEAPOLInvalidType = _Gs2352NASRxCountersEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 7),
    _Gs2352NASRxCountersEAPOLInvalidType_Type()
)
gs2352NASRxCountersEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLInvalidType.setStatus("current")
_Gs2352NASRxCountersEAPOLInvalidLength_Type = Counter32
_Gs2352NASRxCountersEAPOLInvalidLength_Object = MibTableColumn
gs2352NASRxCountersEAPOLInvalidLength = _Gs2352NASRxCountersEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 8),
    _Gs2352NASRxCountersEAPOLInvalidLength_Type()
)
gs2352NASRxCountersEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxCountersEAPOLInvalidLength.setStatus("current")
_Gs2352NASTxCountersEAPOLTotal_Type = Counter32
_Gs2352NASTxCountersEAPOLTotal_Object = MibTableColumn
gs2352NASTxCountersEAPOLTotal = _Gs2352NASTxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 9),
    _Gs2352NASTxCountersEAPOLTotal_Type()
)
gs2352NASTxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxCountersEAPOLTotal.setStatus("current")
_Gs2352NASTxCountersEAPOLRequestID_Type = Counter32
_Gs2352NASTxCountersEAPOLRequestID_Object = MibTableColumn
gs2352NASTxCountersEAPOLRequestID = _Gs2352NASTxCountersEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 10),
    _Gs2352NASTxCountersEAPOLRequestID_Type()
)
gs2352NASTxCountersEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxCountersEAPOLRequestID.setStatus("current")
_Gs2352NASTxCountersEAPOLRequests_Type = Counter32
_Gs2352NASTxCountersEAPOLRequests_Object = MibTableColumn
gs2352NASTxCountersEAPOLRequests = _Gs2352NASTxCountersEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 11),
    _Gs2352NASTxCountersEAPOLRequests_Type()
)
gs2352NASTxCountersEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxCountersEAPOLRequests.setStatus("current")
_Gs2352NASRxBackendServerCountersAccessChallenges_Type = Counter32
_Gs2352NASRxBackendServerCountersAccessChallenges_Object = MibTableColumn
gs2352NASRxBackendServerCountersAccessChallenges = _Gs2352NASRxBackendServerCountersAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 12),
    _Gs2352NASRxBackendServerCountersAccessChallenges_Type()
)
gs2352NASRxBackendServerCountersAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerCountersAccessChallenges.setStatus("current")
_Gs2352NASRxBackendServerCountersOtherRequests_Type = Counter32
_Gs2352NASRxBackendServerCountersOtherRequests_Object = MibTableColumn
gs2352NASRxBackendServerCountersOtherRequests = _Gs2352NASRxBackendServerCountersOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 13),
    _Gs2352NASRxBackendServerCountersOtherRequests_Type()
)
gs2352NASRxBackendServerCountersOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerCountersOtherRequests.setStatus("current")
_Gs2352NASRxBackendServerCountersAuthSuccesses_Type = Counter32
_Gs2352NASRxBackendServerCountersAuthSuccesses_Object = MibTableColumn
gs2352NASRxBackendServerCountersAuthSuccesses = _Gs2352NASRxBackendServerCountersAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 14),
    _Gs2352NASRxBackendServerCountersAuthSuccesses_Type()
)
gs2352NASRxBackendServerCountersAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerCountersAuthSuccesses.setStatus("current")
_Gs2352NASRxBackendServerCountersAuthFailures_Type = Counter32
_Gs2352NASRxBackendServerCountersAuthFailures_Object = MibTableColumn
gs2352NASRxBackendServerCountersAuthFailures = _Gs2352NASRxBackendServerCountersAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 15),
    _Gs2352NASRxBackendServerCountersAuthFailures_Type()
)
gs2352NASRxBackendServerCountersAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerCountersAuthFailures.setStatus("current")
_Gs2352NASTxBackendServerCountersResponses_Type = Counter32
_Gs2352NASTxBackendServerCountersResponses_Object = MibTableColumn
gs2352NASTxBackendServerCountersResponses = _Gs2352NASTxBackendServerCountersResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 16),
    _Gs2352NASTxBackendServerCountersResponses_Type()
)
gs2352NASTxBackendServerCountersResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxBackendServerCountersResponses.setStatus("current")
_Gs2352NASLastSupplicantInfoMACAddress_Type = DisplayString
_Gs2352NASLastSupplicantInfoMACAddress_Object = MibTableColumn
gs2352NASLastSupplicantInfoMACAddress = _Gs2352NASLastSupplicantInfoMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 17),
    _Gs2352NASLastSupplicantInfoMACAddress_Type()
)
gs2352NASLastSupplicantInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASLastSupplicantInfoMACAddress.setStatus("current")
_Gs2352NASLastSupplicantInfoVlanID_Type = Integer32
_Gs2352NASLastSupplicantInfoVlanID_Object = MibTableColumn
gs2352NASLastSupplicantInfoVlanID = _Gs2352NASLastSupplicantInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 18),
    _Gs2352NASLastSupplicantInfoVlanID_Type()
)
gs2352NASLastSupplicantInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASLastSupplicantInfoVlanID.setStatus("current")
_Gs2352NASLastSupplicantInfoVersion_Type = Integer32
_Gs2352NASLastSupplicantInfoVersion_Object = MibTableColumn
gs2352NASLastSupplicantInfoVersion = _Gs2352NASLastSupplicantInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 19),
    _Gs2352NASLastSupplicantInfoVersion_Type()
)
gs2352NASLastSupplicantInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASLastSupplicantInfoVersion.setStatus("current")
_Gs2352NASLastSupplicantInfoIdentity_Type = DisplayString
_Gs2352NASLastSupplicantInfoIdentity_Object = MibTableColumn
gs2352NASLastSupplicantInfoIdentity = _Gs2352NASLastSupplicantInfoIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 20),
    _Gs2352NASLastSupplicantInfoIdentity_Type()
)
gs2352NASLastSupplicantInfoIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASLastSupplicantInfoIdentity.setStatus("current")


class _Gs2352NASCountersDoClear_Type(Integer32):
    """Custom type gs2352NASCountersDoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352NASCountersDoClear_Type.__name__ = "Integer32"
_Gs2352NASCountersDoClear_Object = MibTableColumn
gs2352NASCountersDoClear = _Gs2352NASCountersDoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 1, 1, 21),
    _Gs2352NASCountersDoClear_Type()
)
gs2352NASCountersDoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352NASCountersDoClear.setStatus("current")
_Gs2352NASPortStatusClientsTable_Object = MibTable
gs2352NASPortStatusClientsTable = _Gs2352NASPortStatusClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gs2352NASPortStatusClientsTable.setStatus("current")
_Gs2352NASPortStatusClientsEntry_Object = MibTableRow
gs2352NASPortStatusClientsEntry = _Gs2352NASPortStatusClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1)
)
gs2352NASPortStatusClientsEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352NASPortConfigPort"),
    (0, "LANCOM-GS-2352-MIB", "gs2352NASClientsIndex"),
)
if mibBuilder.loadTexts:
    gs2352NASPortStatusClientsEntry.setStatus("current")


class _Gs2352NASClientsIndex_Type(Integer32):
    """Custom type gs2352NASClientsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2352NASClientsIndex_Type.__name__ = "Integer32"
_Gs2352NASClientsIndex_Object = MibTableColumn
gs2352NASClientsIndex = _Gs2352NASClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 1),
    _Gs2352NASClientsIndex_Type()
)
gs2352NASClientsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352NASClientsIndex.setStatus("current")
_Gs2352NASClientsIdentity_Type = DisplayString
_Gs2352NASClientsIdentity_Object = MibTableColumn
gs2352NASClientsIdentity = _Gs2352NASClientsIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 2),
    _Gs2352NASClientsIdentity_Type()
)
gs2352NASClientsIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASClientsIdentity.setStatus("current")
_Gs2352NASClientsMACAddress_Type = DisplayString
_Gs2352NASClientsMACAddress_Object = MibTableColumn
gs2352NASClientsMACAddress = _Gs2352NASClientsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 3),
    _Gs2352NASClientsMACAddress_Type()
)
gs2352NASClientsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASClientsMACAddress.setStatus("current")


class _Gs2352NASClientsVlanID_Type(Integer32):
    """Custom type gs2352NASClientsVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352NASClientsVlanID_Type.__name__ = "Integer32"
_Gs2352NASClientsVlanID_Object = MibTableColumn
gs2352NASClientsVlanID = _Gs2352NASClientsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 4),
    _Gs2352NASClientsVlanID_Type()
)
gs2352NASClientsVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASClientsVlanID.setStatus("current")
_Gs2352NASClientsState_Type = DisplayString
_Gs2352NASClientsState_Object = MibTableColumn
gs2352NASClientsState = _Gs2352NASClientsState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 5),
    _Gs2352NASClientsState_Type()
)
gs2352NASClientsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASClientsState.setStatus("current")
_Gs2352NASClientsLastAuth_Type = DisplayString
_Gs2352NASClientsLastAuth_Object = MibTableColumn
gs2352NASClientsLastAuth = _Gs2352NASClientsLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 6),
    _Gs2352NASClientsLastAuth_Type()
)
gs2352NASClientsLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASClientsLastAuth.setStatus("current")
_Gs2352NASRxClientsEAPOLTotal_Type = Counter32
_Gs2352NASRxClientsEAPOLTotal_Object = MibTableColumn
gs2352NASRxClientsEAPOLTotal = _Gs2352NASRxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 7),
    _Gs2352NASRxClientsEAPOLTotal_Type()
)
gs2352NASRxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLTotal.setStatus("current")
_Gs2352NASRxClientsEAPOLResponseID_Type = Counter32
_Gs2352NASRxClientsEAPOLResponseID_Object = MibTableColumn
gs2352NASRxClientsEAPOLResponseID = _Gs2352NASRxClientsEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 8),
    _Gs2352NASRxClientsEAPOLResponseID_Type()
)
gs2352NASRxClientsEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLResponseID.setStatus("current")
_Gs2352NASRxClientsEAPOLResponses_Type = Counter32
_Gs2352NASRxClientsEAPOLResponses_Object = MibTableColumn
gs2352NASRxClientsEAPOLResponses = _Gs2352NASRxClientsEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 9),
    _Gs2352NASRxClientsEAPOLResponses_Type()
)
gs2352NASRxClientsEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLResponses.setStatus("current")
_Gs2352NASRxClientsEAPOLStart_Type = Counter32
_Gs2352NASRxClientsEAPOLStart_Object = MibTableColumn
gs2352NASRxClientsEAPOLStart = _Gs2352NASRxClientsEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 10),
    _Gs2352NASRxClientsEAPOLStart_Type()
)
gs2352NASRxClientsEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLStart.setStatus("current")
_Gs2352NASRxClientsEAPOLLogoff_Type = Counter32
_Gs2352NASRxClientsEAPOLLogoff_Object = MibTableColumn
gs2352NASRxClientsEAPOLLogoff = _Gs2352NASRxClientsEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 11),
    _Gs2352NASRxClientsEAPOLLogoff_Type()
)
gs2352NASRxClientsEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLLogoff.setStatus("current")
_Gs2352NASRxClientsEAPOLInvalidType_Type = Counter32
_Gs2352NASRxClientsEAPOLInvalidType_Object = MibTableColumn
gs2352NASRxClientsEAPOLInvalidType = _Gs2352NASRxClientsEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 12),
    _Gs2352NASRxClientsEAPOLInvalidType_Type()
)
gs2352NASRxClientsEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLInvalidType.setStatus("current")
_Gs2352NASRxClientsEAPOLInvalidLength_Type = Counter32
_Gs2352NASRxClientsEAPOLInvalidLength_Object = MibTableColumn
gs2352NASRxClientsEAPOLInvalidLength = _Gs2352NASRxClientsEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 13),
    _Gs2352NASRxClientsEAPOLInvalidLength_Type()
)
gs2352NASRxClientsEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxClientsEAPOLInvalidLength.setStatus("current")
_Gs2352NASTxClientsEAPOLTotal_Type = Counter32
_Gs2352NASTxClientsEAPOLTotal_Object = MibTableColumn
gs2352NASTxClientsEAPOLTotal = _Gs2352NASTxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 14),
    _Gs2352NASTxClientsEAPOLTotal_Type()
)
gs2352NASTxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxClientsEAPOLTotal.setStatus("current")
_Gs2352NASTxClientsEAPOLRequestID_Type = Counter32
_Gs2352NASTxClientsEAPOLRequestID_Object = MibTableColumn
gs2352NASTxClientsEAPOLRequestID = _Gs2352NASTxClientsEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 15),
    _Gs2352NASTxClientsEAPOLRequestID_Type()
)
gs2352NASTxClientsEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxClientsEAPOLRequestID.setStatus("current")
_Gs2352NASTxClientsEAPOLRequests_Type = Counter32
_Gs2352NASTxClientsEAPOLRequests_Object = MibTableColumn
gs2352NASTxClientsEAPOLRequests = _Gs2352NASTxClientsEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 16),
    _Gs2352NASTxClientsEAPOLRequests_Type()
)
gs2352NASTxClientsEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxClientsEAPOLRequests.setStatus("current")
_Gs2352NASRxBackendServerClientsAccessChallenges_Type = Counter32
_Gs2352NASRxBackendServerClientsAccessChallenges_Object = MibTableColumn
gs2352NASRxBackendServerClientsAccessChallenges = _Gs2352NASRxBackendServerClientsAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 17),
    _Gs2352NASRxBackendServerClientsAccessChallenges_Type()
)
gs2352NASRxBackendServerClientsAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerClientsAccessChallenges.setStatus("current")
_Gs2352NASRxBackendServerClientsOtherRequests_Type = Counter32
_Gs2352NASRxBackendServerClientsOtherRequests_Object = MibTableColumn
gs2352NASRxBackendServerClientsOtherRequests = _Gs2352NASRxBackendServerClientsOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 18),
    _Gs2352NASRxBackendServerClientsOtherRequests_Type()
)
gs2352NASRxBackendServerClientsOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerClientsOtherRequests.setStatus("current")
_Gs2352NASRxBackendServerClientsAuthSuccesses_Type = Counter32
_Gs2352NASRxBackendServerClientsAuthSuccesses_Object = MibTableColumn
gs2352NASRxBackendServerClientsAuthSuccesses = _Gs2352NASRxBackendServerClientsAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 19),
    _Gs2352NASRxBackendServerClientsAuthSuccesses_Type()
)
gs2352NASRxBackendServerClientsAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerClientsAuthSuccesses.setStatus("current")
_Gs2352NASRxBackendServerClientsAuthFailures_Type = Counter32
_Gs2352NASRxBackendServerClientsAuthFailures_Object = MibTableColumn
gs2352NASRxBackendServerClientsAuthFailures = _Gs2352NASRxBackendServerClientsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 20),
    _Gs2352NASRxBackendServerClientsAuthFailures_Type()
)
gs2352NASRxBackendServerClientsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASRxBackendServerClientsAuthFailures.setStatus("current")
_Gs2352NASTxBackendServerClientsResponses_Type = Counter32
_Gs2352NASTxBackendServerClientsResponses_Object = MibTableColumn
gs2352NASTxBackendServerClientsResponses = _Gs2352NASTxBackendServerClientsResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 3, 11, 3, 2, 1, 21),
    _Gs2352NASTxBackendServerClientsResponses_Type()
)
gs2352NASTxBackendServerClientsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352NASTxBackendServerClientsResponses.setStatus("current")
_Gs2352Maintenance_ObjectIdentity = ObjectIdentity
gs2352Maintenance = _Gs2352Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4)
)


class _Gs2352RestartDevice_Type(Integer32):
    """Custom type gs2352RestartDevice based on Integer32"""
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


_Gs2352RestartDevice_Type.__name__ = "Integer32"
_Gs2352RestartDevice_Object = MibScalar
gs2352RestartDevice = _Gs2352RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 1),
    _Gs2352RestartDevice_Type()
)
gs2352RestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RestartDevice.setStatus("current")
_Gs2352Firmware_ObjectIdentity = ObjectIdentity
gs2352Firmware = _Gs2352Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 2)
)
_Gs2352FirmwareIpAddress_Type = IpAddress
_Gs2352FirmwareIpAddress_Object = MibScalar
gs2352FirmwareIpAddress = _Gs2352FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 2, 1),
    _Gs2352FirmwareIpAddress_Type()
)
gs2352FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FirmwareIpAddress.setStatus("current")
_Gs2352FirmwareFileName_Type = DisplayString
_Gs2352FirmwareFileName_Object = MibScalar
gs2352FirmwareFileName = _Gs2352FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 2, 2),
    _Gs2352FirmwareFileName_Type()
)
gs2352FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FirmwareFileName.setStatus("current")


class _Gs2352DoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2352DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2352DoFirmwareUpgrade_Object = MibScalar
gs2352DoFirmwareUpgrade = _Gs2352DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 2, 3),
    _Gs2352DoFirmwareUpgrade_Type()
)
gs2352DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DoFirmwareUpgrade.setStatus("current")
_Gs2352SaveOrRestore_ObjectIdentity = ObjectIdentity
gs2352SaveOrRestore = _Gs2352SaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 3)
)


class _Gs2352FactoryDefaults_Type(Integer32):
    """Custom type gs2352FactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("yes", 1))
    )


_Gs2352FactoryDefaults_Type.__name__ = "Integer32"
_Gs2352FactoryDefaults_Object = MibScalar
gs2352FactoryDefaults = _Gs2352FactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 3, 1),
    _Gs2352FactoryDefaults_Type()
)
gs2352FactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352FactoryDefaults.setStatus("current")


class _Gs2352SaveStart_Type(Integer32):
    """Custom type gs2352SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("yes", 1))
    )


_Gs2352SaveStart_Type.__name__ = "Integer32"
_Gs2352SaveStart_Object = MibScalar
gs2352SaveStart = _Gs2352SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 3, 2),
    _Gs2352SaveStart_Type()
)
gs2352SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SaveStart.setStatus("current")


class _Gs2352SaveUser_Type(Integer32):
    """Custom type gs2352SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("yes", 1))
    )


_Gs2352SaveUser_Type.__name__ = "Integer32"
_Gs2352SaveUser_Object = MibScalar
gs2352SaveUser = _Gs2352SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 3, 3),
    _Gs2352SaveUser_Type()
)
gs2352SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352SaveUser.setStatus("current")


class _Gs2352RestoreUser_Type(Integer32):
    """Custom type gs2352RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("yes", 1))
    )


_Gs2352RestoreUser_Type.__name__ = "Integer32"
_Gs2352RestoreUser_Object = MibScalar
gs2352RestoreUser = _Gs2352RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 3, 4),
    _Gs2352RestoreUser_Type()
)
gs2352RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352RestoreUser.setStatus("current")
_Gs2352ExportOrImport_ObjectIdentity = ObjectIdentity
gs2352ExportOrImport = _Gs2352ExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4)
)
_Gs2352ExportIpAddress_Type = IpAddress
_Gs2352ExportIpAddress_Object = MibScalar
gs2352ExportIpAddress = _Gs2352ExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4, 1),
    _Gs2352ExportIpAddress_Type()
)
gs2352ExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ExportIpAddress.setStatus("current")
_Gs2352ExportConfigName_Type = DisplayString
_Gs2352ExportConfigName_Object = MibScalar
gs2352ExportConfigName = _Gs2352ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4, 2),
    _Gs2352ExportConfigName_Type()
)
gs2352ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ExportConfigName.setStatus("current")


class _Gs2352DoExportConfig_Type(Integer32):
    """Custom type gs2352DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352DoExportConfig_Type.__name__ = "Integer32"
_Gs2352DoExportConfig_Object = MibScalar
gs2352DoExportConfig = _Gs2352DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4, 3),
    _Gs2352DoExportConfig_Type()
)
gs2352DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DoExportConfig.setStatus("current")
_Gs2352ImportIpAddress_Type = IpAddress
_Gs2352ImportIpAddress_Object = MibScalar
gs2352ImportIpAddress = _Gs2352ImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4, 4),
    _Gs2352ImportIpAddress_Type()
)
gs2352ImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ImportIpAddress.setStatus("current")
_Gs2352ImportConfigName_Type = DisplayString
_Gs2352ImportConfigName_Object = MibScalar
gs2352ImportConfigName = _Gs2352ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4, 5),
    _Gs2352ImportConfigName_Type()
)
gs2352ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ImportConfigName.setStatus("current")


class _Gs2352DoImportConfig_Type(Integer32):
    """Custom type gs2352DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352DoImportConfig_Type.__name__ = "Integer32"
_Gs2352DoImportConfig_Object = MibScalar
gs2352DoImportConfig = _Gs2352DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 4, 6),
    _Gs2352DoImportConfig_Type()
)
gs2352DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DoImportConfig.setStatus("current")
_Gs2352Diagnostics_ObjectIdentity = ObjectIdentity
gs2352Diagnostics = _Gs2352Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5)
)
_Gs2352PingIpAddress_Type = IpAddress
_Gs2352PingIpAddress_Object = MibScalar
gs2352PingIpAddress = _Gs2352PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 1),
    _Gs2352PingIpAddress_Type()
)
gs2352PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PingIpAddress.setStatus("current")


class _Gs2352PingSize_Type(Integer32):
    """Custom type gs2352PingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1400),
    )


_Gs2352PingSize_Type.__name__ = "Integer32"
_Gs2352PingSize_Object = MibScalar
gs2352PingSize = _Gs2352PingSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 2),
    _Gs2352PingSize_Type()
)
gs2352PingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352PingSize.setStatus("current")


class _Gs2352DoPingConfig_Type(Integer32):
    """Custom type gs2352DoPingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352DoPingConfig_Type.__name__ = "Integer32"
_Gs2352DoPingConfig_Object = MibScalar
gs2352DoPingConfig = _Gs2352DoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 3),
    _Gs2352DoPingConfig_Type()
)
gs2352DoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DoPingConfig.setStatus("current")
_Gs2352PingResult_Type = DisplayString
_Gs2352PingResult_Object = MibScalar
gs2352PingResult = _Gs2352PingResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 4),
    _Gs2352PingResult_Type()
)
gs2352PingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352PingResult.setStatus("current")
_Gs2352Ping6IpAddress_Type = DisplayString
_Gs2352Ping6IpAddress_Object = MibScalar
gs2352Ping6IpAddress = _Gs2352Ping6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 5),
    _Gs2352Ping6IpAddress_Type()
)
gs2352Ping6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ping6IpAddress.setStatus("current")


class _Gs2352Ping6Size_Type(Integer32):
    """Custom type gs2352Ping6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2352Ping6Size_Type.__name__ = "Integer32"
_Gs2352Ping6Size_Object = MibScalar
gs2352Ping6Size = _Gs2352Ping6Size_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 6),
    _Gs2352Ping6Size_Type()
)
gs2352Ping6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352Ping6Size.setStatus("current")


class _Gs2352DoPing6Config_Type(Integer32):
    """Custom type gs2352DoPing6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("do", 1))
    )


_Gs2352DoPing6Config_Type.__name__ = "Integer32"
_Gs2352DoPing6Config_Object = MibScalar
gs2352DoPing6Config = _Gs2352DoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 7),
    _Gs2352DoPing6Config_Type()
)
gs2352DoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352DoPing6Config.setStatus("current")
_Gs2352Ping6Result_Type = DisplayString
_Gs2352Ping6Result_Object = MibScalar
gs2352Ping6Result = _Gs2352Ping6Result_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 8),
    _Gs2352Ping6Result_Type()
)
gs2352Ping6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Ping6Result.setStatus("current")
_Gs2352VeriPHY_ObjectIdentity = ObjectIdentity
gs2352VeriPHY = _Gs2352VeriPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9)
)


class _Gs2352VeriPHYTest_Type(Integer32):
    """Custom type gs2352VeriPHYTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352VeriPHYTest_Type.__name__ = "Integer32"
_Gs2352VeriPHYTest_Object = MibScalar
gs2352VeriPHYTest = _Gs2352VeriPHYTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 1),
    _Gs2352VeriPHYTest_Type()
)
gs2352VeriPHYTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352VeriPHYTest.setStatus("current")
_Gs2352VeriPHYTable_Object = MibTable
gs2352VeriPHYTable = _Gs2352VeriPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2)
)
if mibBuilder.loadTexts:
    gs2352VeriPHYTable.setStatus("current")
_Gs2352VeriPHYEntry_Object = MibTableRow
gs2352VeriPHYEntry = _Gs2352VeriPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1)
)
gs2352VeriPHYEntry.setIndexNames(
    (0, "LANCOM-GS-2352-MIB", "gs2352VeriPHYPort"),
)
if mibBuilder.loadTexts:
    gs2352VeriPHYEntry.setStatus("current")


class _Gs2352VeriPHYPort_Type(Integer32):
    """Custom type gs2352VeriPHYPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2352VeriPHYPort_Type.__name__ = "Integer32"
_Gs2352VeriPHYPort_Object = MibTableColumn
gs2352VeriPHYPort = _Gs2352VeriPHYPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 1),
    _Gs2352VeriPHYPort_Type()
)
gs2352VeriPHYPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2352VeriPHYPort.setStatus("current")
_Gs2352VeriPHYPairA_Type = DisplayString
_Gs2352VeriPHYPairA_Object = MibTableColumn
gs2352VeriPHYPairA = _Gs2352VeriPHYPairA_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 2),
    _Gs2352VeriPHYPairA_Type()
)
gs2352VeriPHYPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYPairA.setStatus("current")
_Gs2352VeriPHYLengthA_Type = DisplayString
_Gs2352VeriPHYLengthA_Object = MibTableColumn
gs2352VeriPHYLengthA = _Gs2352VeriPHYLengthA_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 3),
    _Gs2352VeriPHYLengthA_Type()
)
gs2352VeriPHYLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYLengthA.setStatus("current")
_Gs2352VeriPHYPairB_Type = DisplayString
_Gs2352VeriPHYPairB_Object = MibTableColumn
gs2352VeriPHYPairB = _Gs2352VeriPHYPairB_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 4),
    _Gs2352VeriPHYPairB_Type()
)
gs2352VeriPHYPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYPairB.setStatus("current")
_Gs2352VeriPHYLengthB_Type = DisplayString
_Gs2352VeriPHYLengthB_Object = MibTableColumn
gs2352VeriPHYLengthB = _Gs2352VeriPHYLengthB_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 5),
    _Gs2352VeriPHYLengthB_Type()
)
gs2352VeriPHYLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYLengthB.setStatus("current")
_Gs2352VeriPHYPairC_Type = DisplayString
_Gs2352VeriPHYPairC_Object = MibTableColumn
gs2352VeriPHYPairC = _Gs2352VeriPHYPairC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 6),
    _Gs2352VeriPHYPairC_Type()
)
gs2352VeriPHYPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYPairC.setStatus("current")
_Gs2352VeriPHYLengthC_Type = DisplayString
_Gs2352VeriPHYLengthC_Object = MibTableColumn
gs2352VeriPHYLengthC = _Gs2352VeriPHYLengthC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 7),
    _Gs2352VeriPHYLengthC_Type()
)
gs2352VeriPHYLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYLengthC.setStatus("current")
_Gs2352VeriPHYPairD_Type = DisplayString
_Gs2352VeriPHYPairD_Object = MibTableColumn
gs2352VeriPHYPairD = _Gs2352VeriPHYPairD_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 8),
    _Gs2352VeriPHYPairD_Type()
)
gs2352VeriPHYPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYPairD.setStatus("current")
_Gs2352VeriPHYLengthD_Type = DisplayString
_Gs2352VeriPHYLengthD_Object = MibTableColumn
gs2352VeriPHYLengthD = _Gs2352VeriPHYLengthD_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 5, 9, 2, 1, 9),
    _Gs2352VeriPHYLengthD_Type()
)
gs2352VeriPHYLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352VeriPHYLengthD.setStatus("current")


class _Gs2352ColdRestartDevice_Type(Integer32):
    """Custom type gs2352ColdRestartDevice based on Integer32"""
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


_Gs2352ColdRestartDevice_Type.__name__ = "Integer32"
_Gs2352ColdRestartDevice_Object = MibScalar
gs2352ColdRestartDevice = _Gs2352ColdRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 4, 1500),
    _Gs2352ColdRestartDevice_Type()
)
gs2352ColdRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2352ColdRestartDevice.setStatus("current")
_Gs2352Trap_ObjectIdentity = ObjectIdentity
gs2352Trap = _Gs2352Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5)
)
_Gs2352TrapEvent_ObjectIdentity = ObjectIdentity
gs2352TrapEvent = _Gs2352TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1)
)
_Gs2352TrapVariable_ObjectIdentity = ObjectIdentity
gs2352TrapVariable = _Gs2352TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 2)
)
_Gs2352Information_Type = DisplayString
_Gs2352Information_Object = MibScalar
gs2352Information = _Gs2352Information_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 2, 1),
    _Gs2352Information_Type()
)
gs2352Information.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2352Information.setStatus("current")

# Managed Objects groups


# Notification objects

gs2352Emergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 1)
)
gs2352Emergency.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Emergency.setStatus(
        "current"
    )

gs2352Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 2)
)
gs2352Alert.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Alert.setStatus(
        "current"
    )

gs2352Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 3)
)
gs2352Critical.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Critical.setStatus(
        "current"
    )

gs2352Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 4)
)
gs2352Error.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Error.setStatus(
        "current"
    )

gs2352Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 5)
)
gs2352Warning.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Warning.setStatus(
        "current"
    )

gs2352Notice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 6)
)
gs2352Notice.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Notice.setStatus(
        "current"
    )

gs2352Informational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 7)
)
gs2352Informational.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Informational.setStatus(
        "current"
    )

gs2352Debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2352, 5, 1, 8)
)
gs2352Debug.setObjects(
    ("LANCOM-GS-2352-MIB", "gs2352Information")
)
if mibBuilder.loadTexts:
    gs2352Debug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-GS-2352-MIB",
    **{"lancom-systems": lancom_systems,
       "switchingSystems": switchingSystems,
       "gigabitEthernetSwitches": gigabitEthernetSwitches,
       "lancomGS2352": lancomGS2352,
       "gs2352System": gs2352System,
       "gs2352SystemInformation": gs2352SystemInformation,
       "gs2352ModelName": gs2352ModelName,
       "gs2352BIOSVersion": gs2352BIOSVersion,
       "gs2352FirmwareVersion": gs2352FirmwareVersion,
       "gs2352HardwareMechanicalVersion": gs2352HardwareMechanicalVersion,
       "gs2352SerialNumber": gs2352SerialNumber,
       "gs2352HostMACAddress": gs2352HostMACAddress,
       "gs2352ConsoleBaudrate": gs2352ConsoleBaudrate,
       "gs2352RAMSize": gs2352RAMSize,
       "gs2352FlashSize": gs2352FlashSize,
       "gs2352BridgeFDBSize": gs2352BridgeFDBSize,
       "gs2352TransmitQueue": gs2352TransmitQueue,
       "gs2352MaximumFrameSize": gs2352MaximumFrameSize,
       "gs2352CPULoad": gs2352CPULoad,
       "gs2352FanSpeed": gs2352FanSpeed,
       "gs2352ACPower": gs2352ACPower,
       "gs2352Temperature": gs2352Temperature,
       "gs2352SystemDescription": gs2352SystemDescription,
       "gs2352Location": gs2352Location,
       "gs2352Contact": gs2352Contact,
       "gs2352DeviceName": gs2352DeviceName,
       "gs2352SystemDate": gs2352SystemDate,
       "gs2352SystemUptime": gs2352SystemUptime,
       "gs2352SystemIPv4Address": gs2352SystemIPv4Address,
       "gs2352SystemIPv4SubnetMask": gs2352SystemIPv4SubnetMask,
       "gs2352SystemIPv4Gateway": gs2352SystemIPv4Gateway,
       "gs2352IPv6LinkLocalAddress": gs2352IPv6LinkLocalAddress,
       "gs2352IPv6Address": gs2352IPv6Address,
       "gs2352IPv6Prefix": gs2352IPv6Prefix,
       "gs2352IPv6Gateway": gs2352IPv6Gateway,
       "gs2352LargestFreeMemBlock": gs2352LargestFreeMemBlock,
       "gs2352MemFree": gs2352MemFree,
       "gs2352SystemTime": gs2352SystemTime,
       "gs2352SystemTimeManual": gs2352SystemTimeManual,
       "gs2352SystemTimeManualClockSource": gs2352SystemTimeManualClockSource,
       "gs2352SystemTimeManualLocaltime": gs2352SystemTimeManualLocaltime,
       "gs2352SystemTimeManualTimeZoneOffset": gs2352SystemTimeManualTimeZoneOffset,
       "gs2352SystemTimeManualDaylightSavings": gs2352SystemTimeManualDaylightSavings,
       "gs2352SystemTimeManualTimeSetOffset": gs2352SystemTimeManualTimeSetOffset,
       "gs2352SystemTimeManualDaylightSavingsType": gs2352SystemTimeManualDaylightSavingsType,
       "gs2352SystemTimeManualDaylightSavingsBydatesFrom": gs2352SystemTimeManualDaylightSavingsBydatesFrom,
       "gs2352SystemTimeManualDaylightSavingsBydatesTo": gs2352SystemTimeManualDaylightSavingsBydatesTo,
       "gs2352SystemTimeManualDaylightSavingsRecurringDayFrom": gs2352SystemTimeManualDaylightSavingsRecurringDayFrom,
       "gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom": gs2352SystemTimeManualDaylightSavingsRecurringWeekFrom,
       "gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom": gs2352SystemTimeManualDaylightSavingsRecurringMonthFrom,
       "gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom": gs2352SystemTimeManualDaylightSavingsRecurringTimeFrom,
       "gs2352SystemTimeManualDaylightSavingsRecurringDayTo": gs2352SystemTimeManualDaylightSavingsRecurringDayTo,
       "gs2352SystemTimeManualDaylightSavingsRecurringWeekTo": gs2352SystemTimeManualDaylightSavingsRecurringWeekTo,
       "gs2352SystemTimeManualDaylightSavingsRecurringMonthTo": gs2352SystemTimeManualDaylightSavingsRecurringMonthTo,
       "gs2352SystemTimeManualDaylightSavingsRecurringTimeTo": gs2352SystemTimeManualDaylightSavingsRecurringTimeTo,
       "gs2352SystemTimeNTP": gs2352SystemTimeNTP,
       "gs2352SystemTimeNTPTable": gs2352SystemTimeNTPTable,
       "gs2352SystemTimeNTPEntry": gs2352SystemTimeNTPEntry,
       "gs2352SystemTimeNTPIndex": gs2352SystemTimeNTPIndex,
       "gs2352SystemTimeNTPServerIPType": gs2352SystemTimeNTPServerIPType,
       "gs2352SystemTimeNTPServer": gs2352SystemTimeNTPServer,
       "gs2352SystemTimeNTPCurrentMode": gs2352SystemTimeNTPCurrentMode,
       "gs2352SystemTimeNTPRequestInterval": gs2352SystemTimeNTPRequestInterval,
       "gs2352SystemTimeNTPTriesNumber": gs2352SystemTimeNTPTriesNumber,
       "gs2352SystemAccount": gs2352SystemAccount,
       "gs2352SystemAccountUsers": gs2352SystemAccountUsers,
       "gs2352SystemAccountUserCreate": gs2352SystemAccountUserCreate,
       "gs2352SystemAccountUsersTable": gs2352SystemAccountUsersTable,
       "gs2352SystemAccountUsersEntry": gs2352SystemAccountUsersEntry,
       "gs2352UserIndex": gs2352UserIndex,
       "gs2352UserName": gs2352UserName,
       "gs2352Password": gs2352Password,
       "gs2352UserPrivilegeLevel": gs2352UserPrivilegeLevel,
       "gs2352AccountUserRowStatus": gs2352AccountUserRowStatus,
       "gs2352SystemAccountUsersSuperUserPassword": gs2352SystemAccountUsersSuperUserPassword,
       "gs2352SystemAccountEnforcePasswordRules": gs2352SystemAccountEnforcePasswordRules,
       "gs2352SystemAccountPrivilegeLevel": gs2352SystemAccountPrivilegeLevel,
       "gs2352AccountPrivilegeLevel": gs2352AccountPrivilegeLevel,
       "gs2352AggregationPrivilegeLevel": gs2352AggregationPrivilegeLevel,
       "gs2352DiagnosticsPrivilegeLevel": gs2352DiagnosticsPrivilegeLevel,
       "gs2352EasyportPrivilegeLevel": gs2352EasyportPrivilegeLevel,
       "gs2352GARPPrivilegeLevel": gs2352GARPPrivilegeLevel,
       "gs2352GVRPPrivilegeLevel": gs2352GVRPPrivilegeLevel,
       "gs2352IPPrivilegeLevel": gs2352IPPrivilegeLevel,
       "gs2352IPMCSnoopingPrivilegeLevel": gs2352IPMCSnoopingPrivilegeLevel,
       "gs2352LACPPrivilegeLevel": gs2352LACPPrivilegeLevel,
       "gs2352LLDPPrivilegeLevel": gs2352LLDPPrivilegeLevel,
       "gs2352LLDPMEDPrivilegeLevel": gs2352LLDPMEDPrivilegeLevel,
       "gs2352LoopProtectPrivilegeLevel": gs2352LoopProtectPrivilegeLevel,
       "gs2352MACTablePrivilegeLevel": gs2352MACTablePrivilegeLevel,
       "gs2352MVRPrivilegeLevel": gs2352MVRPrivilegeLevel,
       "gs2352MaintenancePrivilegeLevel": gs2352MaintenancePrivilegeLevel,
       "gs2352MirroringPrivilegeLevel": gs2352MirroringPrivilegeLevel,
       "gs2352PortsPrivilegeLevel": gs2352PortsPrivilegeLevel,
       "gs2352PrivateVLANsPrivilegeLevel": gs2352PrivateVLANsPrivilegeLevel,
       "gs2352QoSPrivilegeLevel": gs2352QoSPrivilegeLevel,
       "gs2352SFlowPrivilegeLevel": gs2352SFlowPrivilegeLevel,
       "gs2352SMTPPrivilegeLevel": gs2352SMTPPrivilegeLevel,
       "gs2352SNMPPrivilegeLevel": gs2352SNMPPrivilegeLevel,
       "gs2352SecurityPrivilegeLevel": gs2352SecurityPrivilegeLevel,
       "gs2352SingleIPPrivilegeLevel": gs2352SingleIPPrivilegeLevel,
       "gs2352SpanningTreePrivilegeLevel": gs2352SpanningTreePrivilegeLevel,
       "gs2352SystemPrivilegeLevel": gs2352SystemPrivilegeLevel,
       "gs2352TrapEventPrivilegeLevel": gs2352TrapEventPrivilegeLevel,
       "gs2352UPnPPrivilegeLevel": gs2352UPnPPrivilegeLevel,
       "gs2352VCLPrivilegeLevel": gs2352VCLPrivilegeLevel,
       "gs2352VLANsPrivilegeLevel": gs2352VLANsPrivilegeLevel,
       "gs2352VoiceVLANPrivilegeLevel": gs2352VoiceVLANPrivilegeLevel,
       "gs2352IP": gs2352IP,
       "gs2352IPv4": gs2352IPv4,
       "gs2352IPv4Configured": gs2352IPv4Configured,
       "gs2352Ipv4DHCPClient": gs2352Ipv4DHCPClient,
       "gs2352IPv4Address": gs2352IPv4Address,
       "gs2352IPv4Mask": gs2352IPv4Mask,
       "gs2352IPv4Gateway": gs2352IPv4Gateway,
       "gs2352IPv4VLANId": gs2352IPv4VLANId,
       "gs2352IPv4DNSServer": gs2352IPv4DNSServer,
       "gs2352IPv4DNSProxy": gs2352IPv4DNSProxy,
       "gs2352IPv4Current": gs2352IPv4Current,
       "gs2352Ipv4CurrentDHCPClient": gs2352Ipv4CurrentDHCPClient,
       "gs2352IPv4CurrentAddress": gs2352IPv4CurrentAddress,
       "gs2352IPv4CurrentMask": gs2352IPv4CurrentMask,
       "gs2352IPv4CurrentGateway": gs2352IPv4CurrentGateway,
       "gs2352IPv4CurrentVLANId": gs2352IPv4CurrentVLANId,
       "gs2352IPv4CurrentDNSServer": gs2352IPv4CurrentDNSServer,
       "gs2352IPv6": gs2352IPv6,
       "gs2352IPv6Configured": gs2352IPv6Configured,
       "gs2352Ipv6AutoConfiguration": gs2352Ipv6AutoConfiguration,
       "gs2352Ipv6Address": gs2352Ipv6Address,
       "gs2352Ipv6Prefix": gs2352Ipv6Prefix,
       "gs2352Ipv6Gateway": gs2352Ipv6Gateway,
       "gs2352IPv6Current": gs2352IPv6Current,
       "gs2352Ipv6CurrentAutoConfiguration": gs2352Ipv6CurrentAutoConfiguration,
       "gs2352Ipv6CurrentAddress": gs2352Ipv6CurrentAddress,
       "gs2352Ipv6CurrentLinkLocalAddress": gs2352Ipv6CurrentLinkLocalAddress,
       "gs2352Ipv6CurrentPrefix": gs2352Ipv6CurrentPrefix,
       "gs2352Ipv6CurrentGateway": gs2352Ipv6CurrentGateway,
       "gs2352Syslog": gs2352Syslog,
       "gs2352SyslogConf": gs2352SyslogConf,
       "gs2352ServerMode": gs2352ServerMode,
       "gs2352ServerAddress1": gs2352ServerAddress1,
       "gs2352ServerAddress2": gs2352ServerAddress2,
       "gs2352SyslogLevel": gs2352SyslogLevel,
       "gs2352SyslogDetailedInfo": gs2352SyslogDetailedInfo,
       "gs2352SyslogDetailedInfoClear": gs2352SyslogDetailedInfoClear,
       "gs2352SyslogDetailedInfoTable": gs2352SyslogDetailedInfoTable,
       "gs2352SyslogDetailedInfoEntry": gs2352SyslogDetailedInfoEntry,
       "gs2352SyslogDetailedInfoIndex": gs2352SyslogDetailedInfoIndex,
       "gs2352SyslogDetailedInfoLevel": gs2352SyslogDetailedInfoLevel,
       "gs2352SyslogDetailedInfoTime": gs2352SyslogDetailedInfoTime,
       "gs2352SyslogDetailedInfoMessage": gs2352SyslogDetailedInfoMessage,
       "gs2352Snmp": gs2352Snmp,
       "gs2352SnmpConf": gs2352SnmpConf,
       "gs2352GetCommunityMode": gs2352GetCommunityMode,
       "gs2352GetCommunity": gs2352GetCommunity,
       "gs2352SetCommunityMode": gs2352SetCommunityMode,
       "gs2352SetCommunity": gs2352SetCommunity,
       "gs2352GetCommunityConfTable": gs2352GetCommunityConfTable,
       "gs2352GetCommunityConfEntry": gs2352GetCommunityConfEntry,
       "gs2352CommunityConfIndex": gs2352CommunityConfIndex,
       "gs2352CommunityConfGetCommunity": gs2352CommunityConfGetCommunity,
       "gs2352TrapHostConfTable": gs2352TrapHostConfTable,
       "gs2352TrapHostConfEntry": gs2352TrapHostConfEntry,
       "gs2352TrapHostConfIndex": gs2352TrapHostConfIndex,
       "gs2352TrapHostConfVersion": gs2352TrapHostConfVersion,
       "gs2352TrapHostConfIPType": gs2352TrapHostConfIPType,
       "gs2352TrapHostConfIP": gs2352TrapHostConfIP,
       "gs2352TrapHostConfPort": gs2352TrapHostConfPort,
       "gs2352TrapHostConfCommunity": gs2352TrapHostConfCommunity,
       "gs2352TrapHostConfSeverityLevel": gs2352TrapHostConfSeverityLevel,
       "gs2352TrapHostConfSecurityLevel": gs2352TrapHostConfSecurityLevel,
       "gs2352TrapHostConfAuthPtc": gs2352TrapHostConfAuthPtc,
       "gs2352TrapHostConfAuthPassword": gs2352TrapHostConfAuthPassword,
       "gs2352TrapHostConfPrivPtc": gs2352TrapHostConfPrivPtc,
       "gs2352TrapHostConfPrivPassword": gs2352TrapHostConfPrivPassword,
       "gs2352TrapHostConfCurrentMode": gs2352TrapHostConfCurrentMode,
       "gs2352SnmpSystem": gs2352SnmpSystem,
       "gs2352SnmpState": gs2352SnmpState,
       "gs2352SnmpEngineID": gs2352SnmpEngineID,
       "gs2352SnmpCommunities": gs2352SnmpCommunities,
       "gs2352SnmpCommunitiesCreate": gs2352SnmpCommunitiesCreate,
       "gs2352SnmpCommunitiesTable": gs2352SnmpCommunitiesTable,
       "gs2352SnmpCommunitiesEntry": gs2352SnmpCommunitiesEntry,
       "gs2352SnmpCommunitiesIndex": gs2352SnmpCommunitiesIndex,
       "gs2352SnmpCommunitiesCommunity": gs2352SnmpCommunitiesCommunity,
       "gs2352SnmpCommunitiesUserName": gs2352SnmpCommunitiesUserName,
       "gs2352SnmpCommunitiesSourceIP": gs2352SnmpCommunitiesSourceIP,
       "gs2352SnmpCommunitiesSourceMask": gs2352SnmpCommunitiesSourceMask,
       "gs2352SnmpCommunitiesRowStatus": gs2352SnmpCommunitiesRowStatus,
       "gs2352SnmpUsers": gs2352SnmpUsers,
       "gs2352SnmpUsersCreate": gs2352SnmpUsersCreate,
       "gs2352SnmpUsersTable": gs2352SnmpUsersTable,
       "gs2352SnmpUsersEntry": gs2352SnmpUsersEntry,
       "gs2352SnmpUsersIndex": gs2352SnmpUsersIndex,
       "gs2352SnmpUsersUserName": gs2352SnmpUsersUserName,
       "gs2352SnmpUsersSecurityLevel": gs2352SnmpUsersSecurityLevel,
       "gs2352SnmpUsersAuthenticationProtocol": gs2352SnmpUsersAuthenticationProtocol,
       "gs2352SnmpUsersAuthenticationPassword": gs2352SnmpUsersAuthenticationPassword,
       "gs2352SnmpUsersPrivacyProtocol": gs2352SnmpUsersPrivacyProtocol,
       "gs2352SnmpUsersPrivacyPassword": gs2352SnmpUsersPrivacyPassword,
       "gs2352SnmpUsersRowStatus": gs2352SnmpUsersRowStatus,
       "gs2352SnmpGroups": gs2352SnmpGroups,
       "gs2352SnmpGroupsCreate": gs2352SnmpGroupsCreate,
       "gs2352SnmpGroupsTable": gs2352SnmpGroupsTable,
       "gs2352SnmpGroupsEntry": gs2352SnmpGroupsEntry,
       "gs2352SnmpGroupsIndex": gs2352SnmpGroupsIndex,
       "gs2352SnmpGroupsSecurityModel": gs2352SnmpGroupsSecurityModel,
       "gs2352SnmpGroupsSecurityName": gs2352SnmpGroupsSecurityName,
       "gs2352SnmpGroupsGroupName": gs2352SnmpGroupsGroupName,
       "gs2352SnmpGroupsRowStatus": gs2352SnmpGroupsRowStatus,
       "gs2352SnmpViews": gs2352SnmpViews,
       "gs2352SnmpViewsCreate": gs2352SnmpViewsCreate,
       "gs2352SnmpViewsTable": gs2352SnmpViewsTable,
       "gs2352SnmpViewsEntry": gs2352SnmpViewsEntry,
       "gs2352SnmpViewsIndex": gs2352SnmpViewsIndex,
       "gs2352SnmpViewsName": gs2352SnmpViewsName,
       "gs2352SnmpViewsType": gs2352SnmpViewsType,
       "gs2352SnmpViewsOIDSubtree": gs2352SnmpViewsOIDSubtree,
       "gs2352SnmpViewsRowStatus": gs2352SnmpViewsRowStatus,
       "gs2352SnmpAccess": gs2352SnmpAccess,
       "gs2352SnmpAccessCreate": gs2352SnmpAccessCreate,
       "gs2352SnmpAccessTable": gs2352SnmpAccessTable,
       "gs2352SnmpAccessEntry": gs2352SnmpAccessEntry,
       "gs2352SnmpAccessIndex": gs2352SnmpAccessIndex,
       "gs2352SnmpAccessGroupName": gs2352SnmpAccessGroupName,
       "gs2352SnmpAccessSecurityModel": gs2352SnmpAccessSecurityModel,
       "gs2352SnmpAccessSecurityLevel": gs2352SnmpAccessSecurityLevel,
       "gs2352SnmpAccessReadViewName": gs2352SnmpAccessReadViewName,
       "gs2352SnmpAccessWriteViewName": gs2352SnmpAccessWriteViewName,
       "gs2352SnmpAccessRowStatus": gs2352SnmpAccessRowStatus,
       "gs2352Configuration": gs2352Configuration,
       "gs2352Port": gs2352Port,
       "gs2352PortConfigurationTable": gs2352PortConfigurationTable,
       "gs2352PortConfigurationEntry": gs2352PortConfigurationEntry,
       "gs2352PortConfPort": gs2352PortConfPort,
       "gs2352PortConfPortMedia": gs2352PortConfPortMedia,
       "gs2352PortConfLink": gs2352PortConfLink,
       "gs2352PortConfCurrentSpeed": gs2352PortConfCurrentSpeed,
       "gs2352PortConfSpeed": gs2352PortConfSpeed,
       "gs2352PortConfCurrentFlowControlRx": gs2352PortConfCurrentFlowControlRx,
       "gs2352PortConfCurrentFlowControlTx": gs2352PortConfCurrentFlowControlTx,
       "gs2352PortConfFlowControl": gs2352PortConfFlowControl,
       "gs2352PortConfMaxFrameSize": gs2352PortConfMaxFrameSize,
       "gs2352PortConfExcessiveCollisionMode": gs2352PortConfExcessiveCollisionMode,
       "gs2352PortConfPowerControl": gs2352PortConfPowerControl,
       "gs2352PortConfDescription": gs2352PortConfDescription,
       "gs2352PortTrafficStatisticsTable": gs2352PortTrafficStatisticsTable,
       "gs2352PortTrafficStatisticsEntry": gs2352PortTrafficStatisticsEntry,
       "gs2352PortTrafficStatisticsPort": gs2352PortTrafficStatisticsPort,
       "gs2352PortTrafficStatisticsClear": gs2352PortTrafficStatisticsClear,
       "gs2352PortTrafficRxPackets": gs2352PortTrafficRxPackets,
       "gs2352PortTrafficRxOctets": gs2352PortTrafficRxOctets,
       "gs2352PortTrafficRxUnicast": gs2352PortTrafficRxUnicast,
       "gs2352PortTrafficRxMulticast": gs2352PortTrafficRxMulticast,
       "gs2352PortTrafficRxBroadcast": gs2352PortTrafficRxBroadcast,
       "gs2352PortTrafficRxPause": gs2352PortTrafficRxPause,
       "gs2352PortTrafficRx64Bytes": gs2352PortTrafficRx64Bytes,
       "gs2352PortTrafficRx65to127Bytes": gs2352PortTrafficRx65to127Bytes,
       "gs2352PortTrafficRx128to255Bytes": gs2352PortTrafficRx128to255Bytes,
       "gs2352PortTrafficRx256to511Bytes": gs2352PortTrafficRx256to511Bytes,
       "gs2352PortTrafficRx512to1023Bytes": gs2352PortTrafficRx512to1023Bytes,
       "gs2352PortTrafficRx1024to1526Bytes": gs2352PortTrafficRx1024to1526Bytes,
       "gs2352PortTrafficRxExceecd1527Bytes": gs2352PortTrafficRxExceecd1527Bytes,
       "gs2352PortTrafficRxQ0": gs2352PortTrafficRxQ0,
       "gs2352PortTrafficRxQ1": gs2352PortTrafficRxQ1,
       "gs2352PortTrafficRxQ2": gs2352PortTrafficRxQ2,
       "gs2352PortTrafficRxQ3": gs2352PortTrafficRxQ3,
       "gs2352PortTrafficRxQ4": gs2352PortTrafficRxQ4,
       "gs2352PortTrafficRxQ5": gs2352PortTrafficRxQ5,
       "gs2352PortTrafficRxQ6": gs2352PortTrafficRxQ6,
       "gs2352PortTrafficRxQ7": gs2352PortTrafficRxQ7,
       "gs2352PortTrafficRxDrops": gs2352PortTrafficRxDrops,
       "gs2352PortTrafficRxCRCorAlignment": gs2352PortTrafficRxCRCorAlignment,
       "gs2352PortTrafficRxUndersize": gs2352PortTrafficRxUndersize,
       "gs2352PortTrafficRxOversize": gs2352PortTrafficRxOversize,
       "gs2352PortTrafficRxFragments": gs2352PortTrafficRxFragments,
       "gs2352PortTrafficRxJabber": gs2352PortTrafficRxJabber,
       "gs2352PortTrafficRxFiltered": gs2352PortTrafficRxFiltered,
       "gs2352PortTrafficTxPackets": gs2352PortTrafficTxPackets,
       "gs2352PortTrafficTxOctets": gs2352PortTrafficTxOctets,
       "gs2352PortTrafficTxUnicast": gs2352PortTrafficTxUnicast,
       "gs2352PortTrafficTxMulticast": gs2352PortTrafficTxMulticast,
       "gs2352PortTrafficTxBroadcast": gs2352PortTrafficTxBroadcast,
       "gs2352PortTrafficTxPause": gs2352PortTrafficTxPause,
       "gs2352PortTrafficTx64Bytes": gs2352PortTrafficTx64Bytes,
       "gs2352PortTrafficTx65to127Bytes": gs2352PortTrafficTx65to127Bytes,
       "gs2352PortTrafficTx128to255Bytes": gs2352PortTrafficTx128to255Bytes,
       "gs2352PortTrafficTx256to511Bytes": gs2352PortTrafficTx256to511Bytes,
       "gs2352PortTrafficTx512to1023Bytes": gs2352PortTrafficTx512to1023Bytes,
       "gs2352PortTrafficTx1024to1526Bytes": gs2352PortTrafficTx1024to1526Bytes,
       "gs2352PortTrafficTxExceecd1527Bytes": gs2352PortTrafficTxExceecd1527Bytes,
       "gs2352PortTrafficTxQ0": gs2352PortTrafficTxQ0,
       "gs2352PortTrafficTxQ1": gs2352PortTrafficTxQ1,
       "gs2352PortTrafficTxQ2": gs2352PortTrafficTxQ2,
       "gs2352PortTrafficTxQ3": gs2352PortTrafficTxQ3,
       "gs2352PortTrafficTxQ4": gs2352PortTrafficTxQ4,
       "gs2352PortTrafficTxQ5": gs2352PortTrafficTxQ5,
       "gs2352PortTrafficTxQ6": gs2352PortTrafficTxQ6,
       "gs2352PortTrafficTxQ7": gs2352PortTrafficTxQ7,
       "gs2352PortTrafficTxDrops": gs2352PortTrafficTxDrops,
       "gs2352PortTrafficTxLateOrExcColl": gs2352PortTrafficTxLateOrExcColl,
       "gs2352PortQoSStatistics": gs2352PortQoSStatistics,
       "gs2352PortQoSStatisticsClear": gs2352PortQoSStatisticsClear,
       "gs2352PortQoSStatisticsTable": gs2352PortQoSStatisticsTable,
       "gs2352PortQoSStatisticsEntry": gs2352PortQoSStatisticsEntry,
       "gs2352PortQoSStatisticsPort": gs2352PortQoSStatisticsPort,
       "gs2352PortQoSQ0Rx": gs2352PortQoSQ0Rx,
       "gs2352PortQoSQ0Tx": gs2352PortQoSQ0Tx,
       "gs2352PortQoSQ1Rx": gs2352PortQoSQ1Rx,
       "gs2352PortQoSQ1Tx": gs2352PortQoSQ1Tx,
       "gs2352PortQoSQ2Rx": gs2352PortQoSQ2Rx,
       "gs2352PortQoSQ2Tx": gs2352PortQoSQ2Tx,
       "gs2352PortQoSQ3Rx": gs2352PortQoSQ3Rx,
       "gs2352PortQoSQ3Tx": gs2352PortQoSQ3Tx,
       "gs2352PortQoSQ4Rx": gs2352PortQoSQ4Rx,
       "gs2352PortQoSQ4Tx": gs2352PortQoSQ4Tx,
       "gs2352PortQoSQ5Rx": gs2352PortQoSQ5Rx,
       "gs2352PortQoSQ5Tx": gs2352PortQoSQ5Tx,
       "gs2352PortQoSQ6Rx": gs2352PortQoSQ6Rx,
       "gs2352PortQoSQ6Tx": gs2352PortQoSQ6Tx,
       "gs2352PortQoSQ7Rx": gs2352PortQoSQ7Rx,
       "gs2352PortQoSQ7Tx": gs2352PortQoSQ7Tx,
       "gs2352SFPInfoTable": gs2352SFPInfoTable,
       "gs2352SFPInfoEntry": gs2352SFPInfoEntry,
       "gs2352SFPInfoIndex": gs2352SFPInfoIndex,
       "gs2352SFPInfoPort": gs2352SFPInfoPort,
       "gs2352SFPConnectorType": gs2352SFPConnectorType,
       "gs2352SFPFiberType": gs2352SFPFiberType,
       "gs2352SFPTxCentralWavelength": gs2352SFPTxCentralWavelength,
       "gs2352SFPBaudRate": gs2352SFPBaudRate,
       "gs2352SFPVendorOUI": gs2352SFPVendorOUI,
       "gs2352SFPVendorName": gs2352SFPVendorName,
       "gs2352SFPVendorPN": gs2352SFPVendorPN,
       "gs2352SFPVendorRev": gs2352SFPVendorRev,
       "gs2352SFPVendorSN": gs2352SFPVendorSN,
       "gs2352SFPDateCode": gs2352SFPDateCode,
       "gs2352SFPTemperature": gs2352SFPTemperature,
       "gs2352SFPVcc": gs2352SFPVcc,
       "gs2352SFPMon1Bias": gs2352SFPMon1Bias,
       "gs2352SFPMon2TxPWR": gs2352SFPMon2TxPWR,
       "gs2352SFPMon3RxPWR": gs2352SFPMon3RxPWR,
       "gs2352VoiceVLAN": gs2352VoiceVLAN,
       "gs2352VoiceVLANConf": gs2352VoiceVLANConf,
       "gs2352VoiceVLANMode": gs2352VoiceVLANMode,
       "gs2352VoiceVLANVLANId": gs2352VoiceVLANVLANId,
       "gs2352VoiceVLANAgingTime": gs2352VoiceVLANAgingTime,
       "gs2352VoiceVLANTrafficClass": gs2352VoiceVLANTrafficClass,
       "gs2352VoiceVLANPortTable": gs2352VoiceVLANPortTable,
       "gs2352VoiceVLANPortEntry": gs2352VoiceVLANPortEntry,
       "gs2352VoiceVLANPort": gs2352VoiceVLANPort,
       "gs2352VoiceVLANPortMode": gs2352VoiceVLANPortMode,
       "gs2352VoiceVLANPortSecurity": gs2352VoiceVLANPortSecurity,
       "gs2352VoiceVLANPortDiscoveryProtocol": gs2352VoiceVLANPortDiscoveryProtocol,
       "gs2352VoiceVLANSkipNAS": gs2352VoiceVLANSkipNAS,
       "gs2352VoiceVLANOUI": gs2352VoiceVLANOUI,
       "gs2352VoiceVLANOUICreate": gs2352VoiceVLANOUICreate,
       "gs2352VoiceVLANOUITable": gs2352VoiceVLANOUITable,
       "gs2352VoiceVLANOUIEntry": gs2352VoiceVLANOUIEntry,
       "gs2352VoiceVLANOUIIndex": gs2352VoiceVLANOUIIndex,
       "gs2352VoiceVLANTelephonyOUI": gs2352VoiceVLANTelephonyOUI,
       "gs2352VoiceVLANDescription": gs2352VoiceVLANDescription,
       "gs2352VoiceVLANOUIRowStatus": gs2352VoiceVLANOUIRowStatus,
       "gs2352GARP": gs2352GARP,
       "gs2352GARPConfTable": gs2352GARPConfTable,
       "gs2352GARPConfEntry": gs2352GARPConfEntry,
       "gs2352GARPConfPort": gs2352GARPConfPort,
       "gs2352GARPJoinTimer": gs2352GARPJoinTimer,
       "gs2352GARPLeaveTimer": gs2352GARPLeaveTimer,
       "gs2352GARPLeaveAllTimer": gs2352GARPLeaveAllTimer,
       "gs2352GARPApplicantion": gs2352GARPApplicantion,
       "gs2352GARPAttributeType": gs2352GARPAttributeType,
       "gs2352GARPApplicant": gs2352GARPApplicant,
       "gs2352GARPStatisticsTable": gs2352GARPStatisticsTable,
       "gs2352GARPStatisticsEntry": gs2352GARPStatisticsEntry,
       "gs2352GARPStatisticsPort": gs2352GARPStatisticsPort,
       "gs2352GARPStatisticsPeerMAC": gs2352GARPStatisticsPeerMAC,
       "gs2352GARPStatisticsFailedCount": gs2352GARPStatisticsFailedCount,
       "gs2352GVRP": gs2352GVRP,
       "gs2352GVRPConf": gs2352GVRPConf,
       "gs2352GVRPMode": gs2352GVRPMode,
       "gs2352GVRPConfTable": gs2352GVRPConfTable,
       "gs2352GVRPConfEntry": gs2352GVRPConfEntry,
       "gs2352GVRPConfPort": gs2352GVRPConfPort,
       "gs2352GVRPConfPortMode": gs2352GVRPConfPortMode,
       "gs2352GVRPConfPortRRole": gs2352GVRPConfPortRRole,
       "gs2352GVRPStatisticsTable": gs2352GVRPStatisticsTable,
       "gs2352GVRPStatisticsEntry": gs2352GVRPStatisticsEntry,
       "gs2352GVRPStatisticsPort": gs2352GVRPStatisticsPort,
       "gs2352GVRPStatisticsJoinTxCnt": gs2352GVRPStatisticsJoinTxCnt,
       "gs2352GVRPStatisticsLeaveTxCnt": gs2352GVRPStatisticsLeaveTxCnt,
       "gs2352Mirroring": gs2352Mirroring,
       "gs2352PortToMirrorOn": gs2352PortToMirrorOn,
       "gs2352MirrorTable": gs2352MirrorTable,
       "gs2352MirrorEntry": gs2352MirrorEntry,
       "gs2352MirrorPort": gs2352MirrorPort,
       "gs2352MirrorMode": gs2352MirrorMode,
       "gs2352TrapEventSeverity": gs2352TrapEventSeverity,
       "gs2352TrapEventSeverityACL": gs2352TrapEventSeverityACL,
       "gs2352TrapEventSeverityACLLog": gs2352TrapEventSeverityACLLog,
       "gs2352TrapEventSeverityAccessMgmt": gs2352TrapEventSeverityAccessMgmt,
       "gs2352TrapEventSeverityAuthFailed": gs2352TrapEventSeverityAuthFailed,
       "gs2352TrapEventSeverityColdStart": gs2352TrapEventSeverityColdStart,
       "gs2352TrapEventSeverityConfigInfo": gs2352TrapEventSeverityConfigInfo,
       "gs2352TrapEventSeverityFirmwareUpgrade": gs2352TrapEventSeverityFirmwareUpgrade,
       "gs2352TrapEventSeverityImportExport": gs2352TrapEventSeverityImportExport,
       "gs2352TrapEventSeverityLACP": gs2352TrapEventSeverityLACP,
       "gs2352TrapEventSeverityLinkStatus": gs2352TrapEventSeverityLinkStatus,
       "gs2352TrapEventSeverityLogin": gs2352TrapEventSeverityLogin,
       "gs2352TrapEventSeverityLogout": gs2352TrapEventSeverityLogout,
       "gs2352TrapEventSeverityLoopProtect": gs2352TrapEventSeverityLoopProtect,
       "gs2352TrapEventSeverityMgmtIPChange": gs2352TrapEventSeverityMgmtIPChange,
       "gs2352TrapEventSeverityModuleChange": gs2352TrapEventSeverityModuleChange,
       "gs2352TrapEventSeverityNAS": gs2352TrapEventSeverityNAS,
       "gs2352TrapEventSeverityPasswordChange": gs2352TrapEventSeverityPasswordChange,
       "gs2352TrapEventSeverityPortSecurity": gs2352TrapEventSeverityPortSecurity,
       "gs2352TrapEventSeverityVLAN": gs2352TrapEventSeverityVLAN,
       "gs2352TrapEventSeverityWarmStart": gs2352TrapEventSeverityWarmStart,
       "gs2352TrapEventSeverityARPConflict": gs2352TrapEventSeverityARPConflict,
       "gs2352TrapEventSeveritySpoofingLimit": gs2352TrapEventSeveritySpoofingLimit,
       "gs2352TrapEventSeverityStaticARPConflict": gs2352TrapEventSeverityStaticARPConflict,
       "gs2352SMTP": gs2352SMTP,
       "gs2352SMTPMailServer": gs2352SMTPMailServer,
       "gs2352SMTPUserName": gs2352SMTPUserName,
       "gs2352SMTPPassword": gs2352SMTPPassword,
       "gs2352SMTPServeriryLevel": gs2352SMTPServeriryLevel,
       "gs2352SMTPSender": gs2352SMTPSender,
       "gs2352SMTPReturnPath": gs2352SMTPReturnPath,
       "gs2352SMTPEmailAddress1": gs2352SMTPEmailAddress1,
       "gs2352SMTPEmailAddress2": gs2352SMTPEmailAddress2,
       "gs2352SMTPEmailAddress3": gs2352SMTPEmailAddress3,
       "gs2352SMTPEmailAddress4": gs2352SMTPEmailAddress4,
       "gs2352SMTPEmailAddress5": gs2352SMTPEmailAddress5,
       "gs2352SMTPEmailAddress6": gs2352SMTPEmailAddress6,
       "gs2352ACL": gs2352ACL,
       "gs2352ACLPortsConfTable": gs2352ACLPortsConfTable,
       "gs2352ACLPortsConfEntry": gs2352ACLPortsConfEntry,
       "gs2352ACLPortsConfPort": gs2352ACLPortsConfPort,
       "gs2352ACLPortsConfPolicyID": gs2352ACLPortsConfPolicyID,
       "gs2352ACLPortsConfAction": gs2352ACLPortsConfAction,
       "gs2352ACLPortsConfRateLimiterID": gs2352ACLPortsConfRateLimiterID,
       "gs2352ACLPortsConfPortRedirect": gs2352ACLPortsConfPortRedirect,
       "gs2352ACLPortsConfLogging": gs2352ACLPortsConfLogging,
       "gs2352ACLPortsConfShutdown": gs2352ACLPortsConfShutdown,
       "gs2352ACLPortsConfState": gs2352ACLPortsConfState,
       "gs2352ACLPortsConfCounter": gs2352ACLPortsConfCounter,
       "gs2352ACLRateLimiterTable": gs2352ACLRateLimiterTable,
       "gs2352ACLRateLimiterEntry": gs2352ACLRateLimiterEntry,
       "gs2352ACLRateLimiterID": gs2352ACLRateLimiterID,
       "gs2352ACLRateLimiterRate": gs2352ACLRateLimiterRate,
       "gs2352ACLACE": gs2352ACLACE,
       "gs2352ACLACECreate": gs2352ACLACECreate,
       "gs2352ACLACETable": gs2352ACLACETable,
       "gs2352ACLACEEntry": gs2352ACLACEEntry,
       "gs2352ACLACEIndex": gs2352ACLACEIndex,
       "gs2352ACLACEID": gs2352ACLACEID,
       "gs2352ACLACENextID": gs2352ACLACENextID,
       "gs2352ACLACEIngressPort": gs2352ACLACEIngressPort,
       "gs2352ACLACEPortPolicyNumber": gs2352ACLACEPortPolicyNumber,
       "gs2352ACLACEPortPolicyBitmask": gs2352ACLACEPortPolicyBitmask,
       "gs2352ACLACEFrameType": gs2352ACLACEFrameType,
       "gs2352ACLACEAction": gs2352ACLACEAction,
       "gs2352ACLACEDenyPortRedirect": gs2352ACLACEDenyPortRedirect,
       "gs2352ACLACELogging": gs2352ACLACELogging,
       "gs2352ACLACERateLimiter": gs2352ACLACERateLimiter,
       "gs2352ACLACEShutdown": gs2352ACLACEShutdown,
       "gs2352ACLACEVLANTagPriority": gs2352ACLACEVLANTagPriority,
       "gs2352ACLACEVLANVID": gs2352ACLACEVLANVID,
       "gs2352ACLACEEtherType": gs2352ACLACEEtherType,
       "gs2352ACLACESMAC": gs2352ACLACESMAC,
       "gs2352ACLACEDMACType": gs2352ACLACEDMACType,
       "gs2352ACLACEDMAC": gs2352ACLACEDMAC,
       "gs2352ACLACEArpOpcode": gs2352ACLACEArpOpcode,
       "gs2352ACLACEArpFlagsRequestReply": gs2352ACLACEArpFlagsRequestReply,
       "gs2352ACLACEArpFlagsArpSmac": gs2352ACLACEArpFlagsArpSmac,
       "gs2352ACLACEArpFlagsRarpDmac": gs2352ACLACEArpFlagsRarpDmac,
       "gs2352ACLACEArpFlagsLength": gs2352ACLACEArpFlagsLength,
       "gs2352ACLACEArpFlagsIp": gs2352ACLACEArpFlagsIp,
       "gs2352ACLACEArpFlagsEthernet": gs2352ACLACEArpFlagsEthernet,
       "gs2352ACLACESIPType": gs2352ACLACESIPType,
       "gs2352ACLACESIPIPAddress": gs2352ACLACESIPIPAddress,
       "gs2352ACLACESIPNetworkPrefix": gs2352ACLACESIPNetworkPrefix,
       "gs2352ACLACEDIPType": gs2352ACLACEDIPType,
       "gs2352ACLACEDIPIPAddress": gs2352ACLACEDIPIPAddress,
       "gs2352ACLACEDIPNetworkPrefix": gs2352ACLACEDIPNetworkPrefix,
       "gs2352ACLACEIPProtocol": gs2352ACLACEIPProtocol,
       "gs2352ACLACEIPFlagsTTL": gs2352ACLACEIPFlagsTTL,
       "gs2352ACLACEIPFlagsOptions": gs2352ACLACEIPFlagsOptions,
       "gs2352ACLACEIPFlagsFragment": gs2352ACLACEIPFlagsFragment,
       "gs2352ACLACEICMPType": gs2352ACLACEICMPType,
       "gs2352ACLACEICMPCode": gs2352ACLACEICMPCode,
       "gs2352ACLACESourcePortMin": gs2352ACLACESourcePortMin,
       "gs2352ACLACESourcePortMax": gs2352ACLACESourcePortMax,
       "gs2352ACLACEDestPortMin": gs2352ACLACEDestPortMin,
       "gs2352ACLACEDestPortMax": gs2352ACLACEDestPortMax,
       "gs2352ACLACETCPFlagsFin": gs2352ACLACETCPFlagsFin,
       "gs2352ACLACETCPFlagsSyn": gs2352ACLACETCPFlagsSyn,
       "gs2352ACLACETCPFlagsRst": gs2352ACLACETCPFlagsRst,
       "gs2352ACLACETCPFlagsPsh": gs2352ACLACETCPFlagsPsh,
       "gs2352ACLACETCPFlagsAck": gs2352ACLACETCPFlagsAck,
       "gs2352ACLACETCPFlagsUrg": gs2352ACLACETCPFlagsUrg,
       "gs2352ACLACERowStatus": gs2352ACLACERowStatus,
       "gs2352ACLACEClear": gs2352ACLACEClear,
       "gs2352ACLACEMoveACEID": gs2352ACLACEMoveACEID,
       "gs2352ACLACEMoveNextACEID": gs2352ACLACEMoveNextACEID,
       "gs2352ACLACEStatusTable": gs2352ACLACEStatusTable,
       "gs2352ACLACEStatusEntry": gs2352ACLACEStatusEntry,
       "gs2352ACLACEStatusIndex": gs2352ACLACEStatusIndex,
       "gs2352ACLACEStatusUser": gs2352ACLACEStatusUser,
       "gs2352ACLACEStatusID": gs2352ACLACEStatusID,
       "gs2352ACLACEStatusIngressPort": gs2352ACLACEStatusIngressPort,
       "gs2352ACLACEStatusFrameType": gs2352ACLACEStatusFrameType,
       "gs2352ACLACEStatusAction": gs2352ACLACEStatusAction,
       "gs2352ACLACEStatusRateLimiter": gs2352ACLACEStatusRateLimiter,
       "gs2352ACLACEStatusPortCopy": gs2352ACLACEStatusPortCopy,
       "gs2352ACLACEStatusMirror": gs2352ACLACEStatusMirror,
       "gs2352ACLACEStatusCPU": gs2352ACLACEStatusCPU,
       "gs2352ACLACEStatusCounter": gs2352ACLACEStatusCounter,
       "gs2352ACLACEStatusConflict": gs2352ACLACEStatusConflict,
       "gs2352LoopProtection": gs2352LoopProtection,
       "gs2352LoopProtectionConfig": gs2352LoopProtectionConfig,
       "gs2352LoopProtectionGlobalEnable": gs2352LoopProtectionGlobalEnable,
       "gs2352LoopProtectionTranmisstionTime": gs2352LoopProtectionTranmisstionTime,
       "gs2352LoopProtectionShutdownTime": gs2352LoopProtectionShutdownTime,
       "gs2352LoopProtectionConfigurationTable": gs2352LoopProtectionConfigurationTable,
       "gs2352LoopProtectionConfigurationEntry": gs2352LoopProtectionConfigurationEntry,
       "gs2352LoopProtectionConfPort": gs2352LoopProtectionConfPort,
       "gs2352LoopProtectionConfEnable": gs2352LoopProtectionConfEnable,
       "gs2352LoopProtectionConfAction": gs2352LoopProtectionConfAction,
       "gs2352LoopProtectionConfTxmode": gs2352LoopProtectionConfTxmode,
       "gs2352LoopProtectionStatusTable": gs2352LoopProtectionStatusTable,
       "gs2352LoopProtectionStatusEntry": gs2352LoopProtectionStatusEntry,
       "gs2352LoopProtectionStatusPort": gs2352LoopProtectionStatusPort,
       "gs2352LoopProtectionStatusAction": gs2352LoopProtectionStatusAction,
       "gs2352LoopProtectionStatusTransmit": gs2352LoopProtectionStatusTransmit,
       "gs2352LoopProtectionStatusLoops": gs2352LoopProtectionStatusLoops,
       "gs2352LoopProtectionStatusStatus": gs2352LoopProtectionStatusStatus,
       "gs2352LoopProtectionStatusLoop": gs2352LoopProtectionStatusLoop,
       "gs2352LoopProtectionStatusTimeLastLoop": gs2352LoopProtectionStatusTimeLastLoop,
       "gs2352Qos": gs2352Qos,
       "gs2352QosPortClassification": gs2352QosPortClassification,
       "gs2352QosPortClassificationTable": gs2352QosPortClassificationTable,
       "gs2352QosPortClassificationEntry": gs2352QosPortClassificationEntry,
       "gs2352QosPortClassificationPort": gs2352QosPortClassificationPort,
       "gs2352QosPortClassificationQoSclass": gs2352QosPortClassificationQoSclass,
       "gs2352QosPortClassificationDPlevel": gs2352QosPortClassificationDPlevel,
       "gs2352QosPortClassificationPCP": gs2352QosPortClassificationPCP,
       "gs2352QosPortClassificationDEI": gs2352QosPortClassificationDEI,
       "gs2352QosPortClassificationTagClass": gs2352QosPortClassificationTagClass,
       "gs2352QosPortClassificationDSCPBased": gs2352QosPortClassificationDSCPBased,
       "gs2352QoSIngressPortTagClassificationTable": gs2352QoSIngressPortTagClassificationTable,
       "gs2352QoSIngressPortTagClassificationEntry": gs2352QoSIngressPortTagClassificationEntry,
       "gs2352QoSIngressPortTagClassificationPort": gs2352QoSIngressPortTagClassificationPort,
       "gs2352QoSIngressPortTagPCP": gs2352QoSIngressPortTagPCP,
       "gs2352QoSIngressPortTagDEI": gs2352QoSIngressPortTagDEI,
       "gs2352QoSIngressPortTagQosClass": gs2352QoSIngressPortTagQosClass,
       "gs2352QoSIngressPortTagDPLevel": gs2352QoSIngressPortTagDPLevel,
       "gs2352QosPortPolicingTable": gs2352QosPortPolicingTable,
       "gs2352QosPortPolicingEntry": gs2352QosPortPolicingEntry,
       "gs2352QosPortPolicingPort": gs2352QosPortPolicingPort,
       "gs2352QosPortPolicingMode": gs2352QosPortPolicingMode,
       "gs2352QosPortPolicingRate": gs2352QosPortPolicingRate,
       "gs2352QosPortPolicingUnit": gs2352QosPortPolicingUnit,
       "gs2352QosPortPolicingFlowControl": gs2352QosPortPolicingFlowControl,
       "gs2352QosPortScheduler": gs2352QosPortScheduler,
       "gs2352QosPortSchedulerModeTable": gs2352QosPortSchedulerModeTable,
       "gs2352QosPortSchedulerModeEntry": gs2352QosPortSchedulerModeEntry,
       "gs2352QosSchedulerModePort": gs2352QosSchedulerModePort,
       "gs2352QosSchedulerMode": gs2352QosSchedulerMode,
       "gs2352QosSchedulerShaper": gs2352QosSchedulerShaper,
       "gs2352QosSchedulerShaperRate": gs2352QosSchedulerShaperRate,
       "gs2352QosPortSchedulerTable": gs2352QosPortSchedulerTable,
       "gs2352QosPortSchedulerEntry": gs2352QosPortSchedulerEntry,
       "gs2352QosSchedulerPort": gs2352QosSchedulerPort,
       "gs2352QosSchedulerPortQueue": gs2352QosSchedulerPortQueue,
       "gs2352QosSchedulerPortQueueShaper": gs2352QosSchedulerPortQueueShaper,
       "gs2352QosSchedulerPortQueueShaperRate": gs2352QosSchedulerPortQueueShaperRate,
       "gs2352QosSchedulerPortQueueShaperExcess": gs2352QosSchedulerPortQueueShaperExcess,
       "gs2352QosSchedulerPortQueueSchedulerWeight": gs2352QosSchedulerPortQueueSchedulerWeight,
       "gs2352QosSchedulerPortQueueSchedulerPercent": gs2352QosSchedulerPortQueueSchedulerPercent,
       "gs2352QosPortEgressTagRemarking": gs2352QosPortEgressTagRemarking,
       "gs2352QosPortEgressTagRemarkingTable": gs2352QosPortEgressTagRemarkingTable,
       "gs2352QosPortEgressTagRemarkingEntry": gs2352QosPortEgressTagRemarkingEntry,
       "gs2352QosEgressTagRemarkingPort": gs2352QosEgressTagRemarkingPort,
       "gs2352QosEgressTagRemarkingMode": gs2352QosEgressTagRemarkingMode,
       "gs2352QosPortEgressTagRemarkingDefTable": gs2352QosPortEgressTagRemarkingDefTable,
       "gs2352QosPortEgressTagRemarkingDefEntry": gs2352QosPortEgressTagRemarkingDefEntry,
       "gs2352QosEgressTagRemarkingDefPort": gs2352QosEgressTagRemarkingDefPort,
       "gs2352QosEgressTagRemarkingDefPCP": gs2352QosEgressTagRemarkingDefPCP,
       "gs2352QosEgressTagRemarkingDefDEI": gs2352QosEgressTagRemarkingDefDEI,
       "gs2352QosPortEgressTagRemarkingMapDPTable": gs2352QosPortEgressTagRemarkingMapDPTable,
       "gs2352QosPortEgressTagRemarkingMapDPEntry": gs2352QosPortEgressTagRemarkingMapDPEntry,
       "gs2352QosPortEgressTagRemarkingDPPort": gs2352QosPortEgressTagRemarkingDPPort,
       "gs2352QosPortEgressTagRemarkingClassifiedDPLevel": gs2352QosPortEgressTagRemarkingClassifiedDPLevel,
       "gs2352QosPortEgressTagRemarkingDPLevel": gs2352QosPortEgressTagRemarkingDPLevel,
       "gs2352QosPortEgressTagRemarkingMapTable": gs2352QosPortEgressTagRemarkingMapTable,
       "gs2352QosPortEgressTagRemarkingMapEntry": gs2352QosPortEgressTagRemarkingMapEntry,
       "gs2352QosPortEgressTagRemarkingMapPort": gs2352QosPortEgressTagRemarkingMapPort,
       "gs2352QosTagRemarkingQoSClass": gs2352QosTagRemarkingQoSClass,
       "gs2352QosTagRemarkingDPLevel": gs2352QosTagRemarkingDPLevel,
       "gs2352QosTagRemarkingPCP": gs2352QosTagRemarkingPCP,
       "gs2352QosTagRemarkingDEI": gs2352QosTagRemarkingDEI,
       "gs2352QosPortDSCPTable": gs2352QosPortDSCPTable,
       "gs2352QosPortDSCPEntry": gs2352QosPortDSCPEntry,
       "gs2352QosPortDSCPPort": gs2352QosPortDSCPPort,
       "gs2352QosPortDSCPIngressTranslate": gs2352QosPortDSCPIngressTranslate,
       "gs2352QosPortDSCPIngressClassify": gs2352QosPortDSCPIngressClassify,
       "gs2352QosPortDSCPEgressRewrite": gs2352QosPortDSCPEgressRewrite,
       "gs2352QosDSCPTable": gs2352QosDSCPTable,
       "gs2352QosDSCPEntry": gs2352QosDSCPEntry,
       "gs2352QosDSCPList": gs2352QosDSCPList,
       "gs2352QosDSCP": gs2352QosDSCP,
       "gs2352QosDSCPTrust": gs2352QosDSCPTrust,
       "gs2352QosDSCPQosClass": gs2352QosDSCPQosClass,
       "gs2352QosDSCPDPL": gs2352QosDSCPDPL,
       "gs2352QosDSCPTranslationTable": gs2352QosDSCPTranslationTable,
       "gs2352QosDSCPTranslationEntry": gs2352QosDSCPTranslationEntry,
       "gs2352QosDSCPTranslationList": gs2352QosDSCPTranslationList,
       "gs2352QosDSCPTranslationDSCPBasedId": gs2352QosDSCPTranslationDSCPBasedId,
       "gs2352QosDSCPTranslationIngressTranslate": gs2352QosDSCPTranslationIngressTranslate,
       "gs2352QosDSCPTranslationIngressClassify": gs2352QosDSCPTranslationIngressClassify,
       "gs2352QosDSCPTranslationEgressRemap": gs2352QosDSCPTranslationEgressRemap,
       "gs2352QosDSCPClassificationTable": gs2352QosDSCPClassificationTable,
       "gs2352QosDSCPClassificationEntry": gs2352QosDSCPClassificationEntry,
       "gs2352QosDSCPClassificationQoSClass": gs2352QosDSCPClassificationQoSClass,
       "gs2352QosDSCPClassificationDSCP": gs2352QosDSCPClassificationDSCP,
       "gs2352QosControlList": gs2352QosControlList,
       "gs2352QosQceCreate": gs2352QosQceCreate,
       "gs2352QosQceTable": gs2352QosQceTable,
       "gs2352QosQceEntry": gs2352QosQceEntry,
       "gs2352QosQceIndex": gs2352QosQceIndex,
       "gs2352QosQceID": gs2352QosQceID,
       "gs2352QosQceNextID": gs2352QosQceNextID,
       "gs2352QosQcePortMembers": gs2352QosQcePortMembers,
       "gs2352QosQceTag": gs2352QosQceTag,
       "gs2352QosQceVID": gs2352QosQceVID,
       "gs2352QosPCP": gs2352QosPCP,
       "gs2352QosDEI": gs2352QosDEI,
       "gs2352QosSMAC": gs2352QosSMAC,
       "gs2352QosDMACType": gs2352QosDMACType,
       "gs2352QosFrameType": gs2352QosFrameType,
       "gs2352QosMacEtherType": gs2352QosMacEtherType,
       "gs2352QosLLCSSAPAddr": gs2352QosLLCSSAPAddr,
       "gs2352QosLLCDSAPAddr": gs2352QosLLCDSAPAddr,
       "gs2352QosLLCControl": gs2352QosLLCControl,
       "gs2352QosSNAPPID": gs2352QosSNAPPID,
       "gs2352QosIpv4Protocol": gs2352QosIpv4Protocol,
       "gs2352QosIpv4ProtocolValue": gs2352QosIpv4ProtocolValue,
       "gs2352QosIpv4ProtocolUDPSport": gs2352QosIpv4ProtocolUDPSport,
       "gs2352QosIpv4ProtocolUDPDport": gs2352QosIpv4ProtocolUDPDport,
       "gs2352QosIpv4ProtocolTCPSport": gs2352QosIpv4ProtocolTCPSport,
       "gs2352QosIpv4ProtocolTCPDport": gs2352QosIpv4ProtocolTCPDport,
       "gs2352QosIpv4SourceIp": gs2352QosIpv4SourceIp,
       "gs2352QosIpv4SourceMask": gs2352QosIpv4SourceMask,
       "gs2352QosIpv4IPFragment": gs2352QosIpv4IPFragment,
       "gs2352QosIpv4DSCP": gs2352QosIpv4DSCP,
       "gs2352QosIpv6Protocol": gs2352QosIpv6Protocol,
       "gs2352QosIpv6ProtocolValue": gs2352QosIpv6ProtocolValue,
       "gs2352QosIpv6ProtocolUDPSport": gs2352QosIpv6ProtocolUDPSport,
       "gs2352QosIpv6ProtocolUDPDport": gs2352QosIpv6ProtocolUDPDport,
       "gs2352QosIpv6ProtocolTCPSport": gs2352QosIpv6ProtocolTCPSport,
       "gs2352QosIpv6ProtocolTCPDport": gs2352QosIpv6ProtocolTCPDport,
       "gs2352QosIpv6SourceIp": gs2352QosIpv6SourceIp,
       "gs2352QosIpv6SourceMask": gs2352QosIpv6SourceMask,
       "gs2352QosIpv6DSCP": gs2352QosIpv6DSCP,
       "gs2352QosActionClass": gs2352QosActionClass,
       "gs2352QosActionDPL": gs2352QosActionDPL,
       "gs2352QosActionDSCP": gs2352QosActionDSCP,
       "gs2352QosQceRowStatus": gs2352QosQceRowStatus,
       "gs2352QosQceMoveID": gs2352QosQceMoveID,
       "gs2352QosQceMoveNextID": gs2352QosQceMoveNextID,
       "gs2352QosQCLStatusTable": gs2352QosQCLStatusTable,
       "gs2352QosQCLStatusEntry": gs2352QosQCLStatusEntry,
       "gs2352QosQCLStatusList": gs2352QosQCLStatusList,
       "gs2352QosQCLStatusUser": gs2352QosQCLStatusUser,
       "gs2352QosQCLStatusQCEId": gs2352QosQCLStatusQCEId,
       "gs2352QosQCLStatusFrameType": gs2352QosQCLStatusFrameType,
       "gs2352QosQCLStatusPortlist": gs2352QosQCLStatusPortlist,
       "gs2352QosQCLStatusActionClass": gs2352QosQCLStatusActionClass,
       "gs2352QosQCLStatusActionDPL": gs2352QosQCLStatusActionDPL,
       "gs2352QosQCLStatusActionDSCP": gs2352QosQCLStatusActionDSCP,
       "gs2352QosQCLStatusActionConflict": gs2352QosQCLStatusActionConflict,
       "gs2352QosStormControl": gs2352QosStormControl,
       "gs2352QosStormControlTable": gs2352QosStormControlTable,
       "gs2352QosStormControlEntry": gs2352QosStormControlEntry,
       "gs2352QosStormControlPort": gs2352QosStormControlPort,
       "gs2352QosStormControlUnicastEnabled": gs2352QosStormControlUnicastEnabled,
       "gs2352QosStormControlUnicastRate": gs2352QosStormControlUnicastRate,
       "gs2352QosStormControlUnicastUnit": gs2352QosStormControlUnicastUnit,
       "gs2352QosStormControlBroadcastEnabled": gs2352QosStormControlBroadcastEnabled,
       "gs2352QosStormControlBroadcastRate": gs2352QosStormControlBroadcastRate,
       "gs2352QosStormControlBroadcastUnit": gs2352QosStormControlBroadcastUnit,
       "gs2352QosStormControlUnknownEnabled": gs2352QosStormControlUnknownEnabled,
       "gs2352QosStormControlUnknownRate": gs2352QosStormControlUnknownRate,
       "gs2352QosStormControlUnknownUnit": gs2352QosStormControlUnknownUnit,
       "gs2352QosWREDTable": gs2352QosWREDTable,
       "gs2352QosWREDEntry": gs2352QosWREDEntry,
       "gs2352QosWREDQueueList": gs2352QosWREDQueueList,
       "gs2352QosWREDQueue": gs2352QosWREDQueue,
       "gs2352QosWREDMinThreshold": gs2352QosWREDMinThreshold,
       "gs2352QosWREDMaxDP1": gs2352QosWREDMaxDP1,
       "gs2352QosWREDMaxDP2": gs2352QosWREDMaxDP2,
       "gs2352QosWREDMaxDP3": gs2352QosWREDMaxDP3,
       "gs2352Vlan": gs2352Vlan,
       "gs2352VlanPorts": gs2352VlanPorts,
       "gs2352VlanPortsTPIDforCustomSport": gs2352VlanPortsTPIDforCustomSport,
       "gs2352VlanPortsTable": gs2352VlanPortsTable,
       "gs2352VlanPortsEntry": gs2352VlanPortsEntry,
       "gs2352VlanPortsPort": gs2352VlanPortsPort,
       "gs2352VlanPortsPVID": gs2352VlanPortsPVID,
       "gs2352VlanPortsFrameType": gs2352VlanPortsFrameType,
       "gs2352VlanPortsIngressFilter": gs2352VlanPortsIngressFilter,
       "gs2352VlanPortsEgressRule": gs2352VlanPortsEgressRule,
       "gs2352VlanPortsPortType": gs2352VlanPortsPortType,
       "gs2352VlanPrivateVLAN": gs2352VlanPrivateVLAN,
       "gs2352VlanPortIsolationTable": gs2352VlanPortIsolationTable,
       "gs2352VlanPortIsolationEntry": gs2352VlanPortIsolationEntry,
       "gs2352VlanPortIsolationPort": gs2352VlanPortIsolationPort,
       "gs2352VlanPortIsolation": gs2352VlanPortIsolation,
       "gs2352MACbasedVLAN": gs2352MACbasedVLAN,
       "gs2352MACbasedVLANConf": gs2352MACbasedVLANConf,
       "gs2352MACbasedVLANConfCreate": gs2352MACbasedVLANConfCreate,
       "gs2352MACbasedVLANConfTable": gs2352MACbasedVLANConfTable,
       "gs2352MACbasedVLANConfEntry": gs2352MACbasedVLANConfEntry,
       "gs2352MACbasedVLANIndex": gs2352MACbasedVLANIndex,
       "gs2352MACbasedVLANMACAddress": gs2352MACbasedVLANMACAddress,
       "gs2352MACbasedVLANID": gs2352MACbasedVLANID,
       "gs2352MACbasedMemberships": gs2352MACbasedMemberships,
       "gs2352MACbaseRowStatus": gs2352MACbaseRowStatus,
       "gs2352IGMPSnooping": gs2352IGMPSnooping,
       "gs2352IGMPSnoopingBasic": gs2352IGMPSnoopingBasic,
       "gs2352IGMPSnoopingEnable": gs2352IGMPSnoopingEnable,
       "gs2352IGMPSnoopingUnregisteredIPMCv4Flooding": gs2352IGMPSnoopingUnregisteredIPMCv4Flooding,
       "gs2352IGMPSnoopingSSMIPRangeAddr": gs2352IGMPSnoopingSSMIPRangeAddr,
       "gs2352IGMPSnoopingSSMIPRangeValue": gs2352IGMPSnoopingSSMIPRangeValue,
       "gs2352IGMPSnoopingProxyEnabled": gs2352IGMPSnoopingProxyEnabled,
       "gs2352IGMPSnoopingPortRelatedTable": gs2352IGMPSnoopingPortRelatedTable,
       "gs2352IGMPSnoopingPortRelatedEntry": gs2352IGMPSnoopingPortRelatedEntry,
       "gs2352IGMPSnoopingRouterPort": gs2352IGMPSnoopingRouterPort,
       "gs2352IGMPSnoopingFastLeave": gs2352IGMPSnoopingFastLeave,
       "gs2352IGMPSnoopingThrottling": gs2352IGMPSnoopingThrottling,
       "gs2352IGMPSnoopingVLANTable": gs2352IGMPSnoopingVLANTable,
       "gs2352IGMPSnoopingVLANEntry": gs2352IGMPSnoopingVLANEntry,
       "gs2352IGMPSnoopingVLANID": gs2352IGMPSnoopingVLANID,
       "gs2352IGMPSnoopingVLANEnable": gs2352IGMPSnoopingVLANEnable,
       "gs2352IGMPSnoopingVLANIGMPQuerier": gs2352IGMPSnoopingVLANIGMPQuerier,
       "gs2352IGMPSnoopingVLANCompatibility": gs2352IGMPSnoopingVLANCompatibility,
       "gs2352IGMPSnoopingVLANRV": gs2352IGMPSnoopingVLANRV,
       "gs2352IGMPSnoopingVLANQI": gs2352IGMPSnoopingVLANQI,
       "gs2352IGMPSnoopingVLANQRI": gs2352IGMPSnoopingVLANQRI,
       "gs2352IGMPSnoopingVLANLLQI": gs2352IGMPSnoopingVLANLLQI,
       "gs2352IGMPSnoopingVLANURI": gs2352IGMPSnoopingVLANURI,
       "gs2352IGMPSnoopingPortGroupFiltering": gs2352IGMPSnoopingPortGroupFiltering,
       "gs2352IGMPSnoopingPortGroupFilteringCreate": gs2352IGMPSnoopingPortGroupFilteringCreate,
       "gs2352IGMPSnoopingPortGroupFilteringTable": gs2352IGMPSnoopingPortGroupFilteringTable,
       "gs2352IGMPSnoopingPortGroupFilteringEntry": gs2352IGMPSnoopingPortGroupFilteringEntry,
       "gs2352IGMPSnoopingPortGroupFilteringIndex": gs2352IGMPSnoopingPortGroupFilteringIndex,
       "gs2352IGMPSnoopingPortGroupFilteringPort": gs2352IGMPSnoopingPortGroupFilteringPort,
       "gs2352IGMPSnoopingPortGroupFilteringGroups": gs2352IGMPSnoopingPortGroupFilteringGroups,
       "gs2352IGMPSnoopingPortGroupFilteringRowStatus": gs2352IGMPSnoopingPortGroupFilteringRowStatus,
       "gs2352IGMPSnoopingStatus": gs2352IGMPSnoopingStatus,
       "gs2352IGMPSnoopingstatisticClear": gs2352IGMPSnoopingstatisticClear,
       "gs2352IGMPSnoopingstatisticTable": gs2352IGMPSnoopingstatisticTable,
       "gs2352IGMPSnoopingstatisticEntry": gs2352IGMPSnoopingstatisticEntry,
       "gs2352IGMPSnoopingstatisticVLANID": gs2352IGMPSnoopingstatisticVLANID,
       "gs2352IGMPSnoopingstatisticQuerierVersion": gs2352IGMPSnoopingstatisticQuerierVersion,
       "gs2352IGMPSnoopingstatisticHostVersion": gs2352IGMPSnoopingstatisticHostVersion,
       "gs2352IGMPSnoopingstatisticQuerierStatus": gs2352IGMPSnoopingstatisticQuerierStatus,
       "gs2352IGMPSnoopingstatisticQueriesTransmitted": gs2352IGMPSnoopingstatisticQueriesTransmitted,
       "gs2352IGMPSnoopingstatisticQueriesReceived": gs2352IGMPSnoopingstatisticQueriesReceived,
       "gs2352IGMPSnoopingstatisticV1ReportsReceived": gs2352IGMPSnoopingstatisticV1ReportsReceived,
       "gs2352IGMPSnoopingstatisticV2ReportsReceived": gs2352IGMPSnoopingstatisticV2ReportsReceived,
       "gs2352IGMPSnoopingstatisticV3ReportsReceived": gs2352IGMPSnoopingstatisticV3ReportsReceived,
       "gs2352IGMPSnoopingstatisticV2LeavesReceived": gs2352IGMPSnoopingstatisticV2LeavesReceived,
       "gs2352IGMPSnoopingRouterPortTable": gs2352IGMPSnoopingRouterPortTable,
       "gs2352IGMPSnoopingRouterPortEntry": gs2352IGMPSnoopingRouterPortEntry,
       "gs2352IGMPSnoopingRouterPortStatus": gs2352IGMPSnoopingRouterPortStatus,
       "gs2352IGMPSnoopingGroupsTable": gs2352IGMPSnoopingGroupsTable,
       "gs2352IGMPSnoopingGroupsEntry": gs2352IGMPSnoopingGroupsEntry,
       "gs2352IGMPSnoopingGroupsIndex": gs2352IGMPSnoopingGroupsIndex,
       "gs2352IGMPSnoopingGroupsVLANID": gs2352IGMPSnoopingGroupsVLANID,
       "gs2352IGMPSnoopingGroups": gs2352IGMPSnoopingGroups,
       "gs2352IGMPSnoopingGroupsMemberships": gs2352IGMPSnoopingGroupsMemberships,
       "gs2352IGMPSnoopingSSMTable": gs2352IGMPSnoopingSSMTable,
       "gs2352IGMPSnoopingSSMEntry": gs2352IGMPSnoopingSSMEntry,
       "gs2352IGMPSnoopingSSMIndex": gs2352IGMPSnoopingSSMIndex,
       "gs2352IGMPSnoopingSSMVLANID": gs2352IGMPSnoopingSSMVLANID,
       "gs2352IGMPSnoopingSSMGroup": gs2352IGMPSnoopingSSMGroup,
       "gs2352IGMPSnoopingSSMPort": gs2352IGMPSnoopingSSMPort,
       "gs2352IGMPSnoopingSSMMode": gs2352IGMPSnoopingSSMMode,
       "gs2352IGMPSnoopingSSMSourceAddress": gs2352IGMPSnoopingSSMSourceAddress,
       "gs2352IGMPSnoopingSSMType": gs2352IGMPSnoopingSSMType,
       "gs2352MLDSnooping": gs2352MLDSnooping,
       "gs2352MLDSnoopingBasic": gs2352MLDSnoopingBasic,
       "gs2352MLDSnoopingEnable": gs2352MLDSnoopingEnable,
       "gs2352MLDSnoopingUnregisteredIPMCv6Flooding": gs2352MLDSnoopingUnregisteredIPMCv6Flooding,
       "gs2352MLDSnoopingSSMIPRangeAddr": gs2352MLDSnoopingSSMIPRangeAddr,
       "gs2352MLDSnoopingSSMIPRangeValue": gs2352MLDSnoopingSSMIPRangeValue,
       "gs2352MLDSnoopingProxyEnabled": gs2352MLDSnoopingProxyEnabled,
       "gs2352MLDSnoopingPortRelatedTable": gs2352MLDSnoopingPortRelatedTable,
       "gs2352MLDSnoopingPortRelatedEntry": gs2352MLDSnoopingPortRelatedEntry,
       "gs2352MLDSnoopingRouterPort": gs2352MLDSnoopingRouterPort,
       "gs2352MLDSnoopingFastLeave": gs2352MLDSnoopingFastLeave,
       "gs2352MLDSnoopingThrottling": gs2352MLDSnoopingThrottling,
       "gs2352MLDSnoopingVLANTable": gs2352MLDSnoopingVLANTable,
       "gs2352MLDSnoopingVLANEntry": gs2352MLDSnoopingVLANEntry,
       "gs2352MLDSnoopingVLANID": gs2352MLDSnoopingVLANID,
       "gs2352MLDSnoopingVLANEnable": gs2352MLDSnoopingVLANEnable,
       "gs2352MLDSnoopingVLANIGMPQuerier": gs2352MLDSnoopingVLANIGMPQuerier,
       "gs2352MLDSnoopingVLANCompatibility": gs2352MLDSnoopingVLANCompatibility,
       "gs2352MLDSnoopingVLANRV": gs2352MLDSnoopingVLANRV,
       "gs2352MLDSnoopingVLANQI": gs2352MLDSnoopingVLANQI,
       "gs2352MLDSnoopingVLANQRI": gs2352MLDSnoopingVLANQRI,
       "gs2352MLDSnoopingVLANLLQI": gs2352MLDSnoopingVLANLLQI,
       "gs2352MLDSnoopingVLANURI": gs2352MLDSnoopingVLANURI,
       "gs2352MLDSnoopingPortGroupFiltering": gs2352MLDSnoopingPortGroupFiltering,
       "gs2352MLDSnoopingPortGroupFilteringCreate": gs2352MLDSnoopingPortGroupFilteringCreate,
       "gs2352MLDSnoopingPortGroupFilteringTable": gs2352MLDSnoopingPortGroupFilteringTable,
       "gs2352MLDSnoopingPortGroupFilteringEntry": gs2352MLDSnoopingPortGroupFilteringEntry,
       "gs2352MLDSnoopingPortGroupFilteringIndex": gs2352MLDSnoopingPortGroupFilteringIndex,
       "gs2352MLDSnoopingPortGroupFilteringPort": gs2352MLDSnoopingPortGroupFilteringPort,
       "gs2352MLDSnoopingPortGroupFilteringGroups": gs2352MLDSnoopingPortGroupFilteringGroups,
       "gs2352MLDSnoopingPortGroupFilteringRowStatus": gs2352MLDSnoopingPortGroupFilteringRowStatus,
       "gs2352MLDSnoopingStatus": gs2352MLDSnoopingStatus,
       "gs2352MLDSnoopingstatisticClear": gs2352MLDSnoopingstatisticClear,
       "gs2352MLDSnoopingstatisticTable": gs2352MLDSnoopingstatisticTable,
       "gs2352MLDSnoopingstatisticEntry": gs2352MLDSnoopingstatisticEntry,
       "gs2352MLDSnoopingstatisticVLANID": gs2352MLDSnoopingstatisticVLANID,
       "gs2352MLDSnoopingstatisticQuerierVersion": gs2352MLDSnoopingstatisticQuerierVersion,
       "gs2352MLDSnoopingstatisticHostVersion": gs2352MLDSnoopingstatisticHostVersion,
       "gs2352MLDSnoopingstatisticQuerierStatus": gs2352MLDSnoopingstatisticQuerierStatus,
       "gs2352MLDSnoopingstatisticQueriesTransmitted": gs2352MLDSnoopingstatisticQueriesTransmitted,
       "gs2352MLDSnoopingstatisticQueriesReceived": gs2352MLDSnoopingstatisticQueriesReceived,
       "gs2352MLDSnoopingstatisticV1ReportsReceived": gs2352MLDSnoopingstatisticV1ReportsReceived,
       "gs2352MLDSnoopingstatisticV2ReportsReceived": gs2352MLDSnoopingstatisticV2ReportsReceived,
       "gs2352MLDSnoopingstatisticV1LeavesReceived": gs2352MLDSnoopingstatisticV1LeavesReceived,
       "gs2352MLDSnoopingRouterPortTable": gs2352MLDSnoopingRouterPortTable,
       "gs2352MLDSnoopingRouterPortEntry": gs2352MLDSnoopingRouterPortEntry,
       "gs2352MLDSnoopingRouterPortStatus": gs2352MLDSnoopingRouterPortStatus,
       "gs2352MLDSnoopingGroupsTable": gs2352MLDSnoopingGroupsTable,
       "gs2352MLDSnoopingGroupsEntry": gs2352MLDSnoopingGroupsEntry,
       "gs2352MLDSnoopingGroupsIndex": gs2352MLDSnoopingGroupsIndex,
       "gs2352MLDSnoopingGroupsVLANID": gs2352MLDSnoopingGroupsVLANID,
       "gs2352MLDSnoopingGroups": gs2352MLDSnoopingGroups,
       "gs2352MLDSnoopingGroupsMemberships": gs2352MLDSnoopingGroupsMemberships,
       "gs2352MLDSnoopingSSMTable": gs2352MLDSnoopingSSMTable,
       "gs2352MLDSnoopingSSMEntry": gs2352MLDSnoopingSSMEntry,
       "gs2352MLDSnoopingSSMIndex": gs2352MLDSnoopingSSMIndex,
       "gs2352MLDSnoopingSSMVLANID": gs2352MLDSnoopingSSMVLANID,
       "gs2352MLDSnoopingSSMGroup": gs2352MLDSnoopingSSMGroup,
       "gs2352MLDSnoopingSSMPort": gs2352MLDSnoopingSSMPort,
       "gs2352MLDSnoopingSSMMode": gs2352MLDSnoopingSSMMode,
       "gs2352MLDSnoopingSSMSourceAddress": gs2352MLDSnoopingSSMSourceAddress,
       "gs2352MLDSnoopingSSMType": gs2352MLDSnoopingSSMType,
       "gs2352MVR": gs2352MVR,
       "gs2352MVRConfiguration": gs2352MVRConfiguration,
       "gs2352MVRMode": gs2352MVRMode,
       "gs2352MVRVLANId": gs2352MVRVLANId,
       "gs2352MVRPortConfigurationTable": gs2352MVRPortConfigurationTable,
       "gs2352MVRPortConfigurationEntry": gs2352MVRPortConfigurationEntry,
       "gs2352MVRPortConfigurationMode": gs2352MVRPortConfigurationMode,
       "gs2352MVRPortConfigurationType": gs2352MVRPortConfigurationType,
       "gs2352MVRPortConfigurationImmediateLeave": gs2352MVRPortConfigurationImmediateLeave,
       "gs2352MVRPortGroupFiltering": gs2352MVRPortGroupFiltering,
       "gs2352MVRPortGroupFilteringCreate": gs2352MVRPortGroupFilteringCreate,
       "gs2352MVRPortGroupFilteringTable": gs2352MVRPortGroupFilteringTable,
       "gs2352MVRPortGroupFilteringEntry": gs2352MVRPortGroupFilteringEntry,
       "gs2352MVRPortGroupFilteringIndex": gs2352MVRPortGroupFilteringIndex,
       "gs2352MVRPortGroupFilteringPort": gs2352MVRPortGroupFilteringPort,
       "gs2352MVRPortGroupFilteringStartGroups": gs2352MVRPortGroupFilteringStartGroups,
       "gs2352MVRPortGroupFilteringEndGroups": gs2352MVRPortGroupFilteringEndGroups,
       "gs2352MVRPortGroupFilteringRowStatus": gs2352MVRPortGroupFilteringRowStatus,
       "gs2352MVRGroupsTable": gs2352MVRGroupsTable,
       "gs2352MVRGroupsEntry": gs2352MVRGroupsEntry,
       "gs2352MVRGroupsIndex": gs2352MVRGroupsIndex,
       "gs2352MVRGroupsVLANID": gs2352MVRGroupsVLANID,
       "gs2352MVRGroups": gs2352MVRGroups,
       "gs2352MVRGroupsMemberships": gs2352MVRGroupsMemberships,
       "gs2352MVRStatus": gs2352MVRStatus,
       "gs2352MVRstatisticClear": gs2352MVRstatisticClear,
       "gs2352MVRstatisticVLANID": gs2352MVRstatisticVLANID,
       "gs2352MVRstatisticV1ReportsReceived": gs2352MVRstatisticV1ReportsReceived,
       "gs2352MVRstatisticV2ReportsReceived": gs2352MVRstatisticV2ReportsReceived,
       "gs2352MVRstatisticV3ReportsReceived": gs2352MVRstatisticV3ReportsReceived,
       "gs2352MVRstatisticV2LeavesReceived": gs2352MVRstatisticV2LeavesReceived,
       "gs2352LACP": gs2352LACP,
       "gs2352LACPConf": gs2352LACPConf,
       "gs2352LACPPortConfigurationTable": gs2352LACPPortConfigurationTable,
       "gs2352LACPPortConfigurationEntry": gs2352LACPPortConfigurationEntry,
       "gs2352LACPPortConfigurationPort": gs2352LACPPortConfigurationPort,
       "gs2352LACPPortConfigurationMode": gs2352LACPPortConfigurationMode,
       "gs2352LACPPortConfigurationKey": gs2352LACPPortConfigurationKey,
       "gs2352LACPPortConfigurationRole": gs2352LACPPortConfigurationRole,
       "gs2352LACPSystemStatusTable": gs2352LACPSystemStatusTable,
       "gs2352LACPSystemStatusEntry": gs2352LACPSystemStatusEntry,
       "gs2352LACPSystemStatusIndex": gs2352LACPSystemStatusIndex,
       "gs2352LACPSystemStatusAggrID": gs2352LACPSystemStatusAggrID,
       "gs2352LACPSystemStatusPartnerSystemID": gs2352LACPSystemStatusPartnerSystemID,
       "gs2352LACPSystemStatusPartnerKey": gs2352LACPSystemStatusPartnerKey,
       "gs2352LACPSystemStatusLastchanged": gs2352LACPSystemStatusLastchanged,
       "gs2352LACPSystemStatusLocalPorts": gs2352LACPSystemStatusLocalPorts,
       "gs2352LACPStatusTable": gs2352LACPStatusTable,
       "gs2352LACPStatusEntry": gs2352LACPStatusEntry,
       "gs2352LACPStatusPort": gs2352LACPStatusPort,
       "gs2352LACPStatusLACP": gs2352LACPStatusLACP,
       "gs2352LACPStatusKey": gs2352LACPStatusKey,
       "gs2352LACPStatusAggrID": gs2352LACPStatusAggrID,
       "gs2352LACPStatusPartnerSystemID": gs2352LACPStatusPartnerSystemID,
       "gs2352LACPStatusPartnerPort": gs2352LACPStatusPartnerPort,
       "gs2352LACPStatisticsTable": gs2352LACPStatisticsTable,
       "gs2352LACPStatisticsEntry": gs2352LACPStatisticsEntry,
       "gs2352LACPStatisticsPort": gs2352LACPStatisticsPort,
       "gs2352LACPReceived": gs2352LACPReceived,
       "gs2352LACPTransmitted": gs2352LACPTransmitted,
       "gs2352LACPDiscardedUnknown": gs2352LACPDiscardedUnknown,
       "gs2352LACPDiscardedIllegal": gs2352LACPDiscardedIllegal,
       "gs2352LACPStatisticsClear": gs2352LACPStatisticsClear,
       "gs2352STP": gs2352STP,
       "gs2352STPBridgeBasicConf": gs2352STPBridgeBasicConf,
       "gs2352STPBridgeProtocolVersion": gs2352STPBridgeProtocolVersion,
       "gs2352STPBridgePriority": gs2352STPBridgePriority,
       "gs2352STPBridgeForwardDelay": gs2352STPBridgeForwardDelay,
       "gs2352STPBridgeMaxAge": gs2352STPBridgeMaxAge,
       "gs2352STPBridgeMaximumHopCount": gs2352STPBridgeMaximumHopCount,
       "gs2352STPBridgeTransmitHoldCount": gs2352STPBridgeTransmitHoldCount,
       "gs2352STPBridgeAdvancedConf": gs2352STPBridgeAdvancedConf,
       "gs2352STPBridgeEdgePortBPDUFiltering": gs2352STPBridgeEdgePortBPDUFiltering,
       "gs2352STPBridgeEdgePortBPDUGuard": gs2352STPBridgeEdgePortBPDUGuard,
       "gs2352STPBridgePortErrorRecoveryTimeout": gs2352STPBridgePortErrorRecoveryTimeout,
       "gs2352STPMSTIConf": gs2352STPMSTIConf,
       "gs2352STPMSTIConfigurationName": gs2352STPMSTIConfigurationName,
       "gs2352STPMSTIConfigurationRevision": gs2352STPMSTIConfigurationRevision,
       "gs2352STPMSTIMappingConf": gs2352STPMSTIMappingConf,
       "gs2352STPMSTI1VLANsMapped": gs2352STPMSTI1VLANsMapped,
       "gs2352STPMSTI2VLANsMapped": gs2352STPMSTI2VLANsMapped,
       "gs2352STPMSTI3VLANsMapped": gs2352STPMSTI3VLANsMapped,
       "gs2352STPMSTI4VLANsMapped": gs2352STPMSTI4VLANsMapped,
       "gs2352STPMSTI5VLANsMapped": gs2352STPMSTI5VLANsMapped,
       "gs2352STPMSTI6VLANsMapped": gs2352STPMSTI6VLANsMapped,
       "gs2352STPMSTI7VLANsMapped": gs2352STPMSTI7VLANsMapped,
       "gs2352STPMSTIPriority": gs2352STPMSTIPriority,
       "gs2352STPCISTPriority": gs2352STPCISTPriority,
       "gs2352STPMSTI1Priority": gs2352STPMSTI1Priority,
       "gs2352STPMSTI2Priority": gs2352STPMSTI2Priority,
       "gs2352STPMSTI3Priority": gs2352STPMSTI3Priority,
       "gs2352STPMSTI4Priority": gs2352STPMSTI4Priority,
       "gs2352STPMSTI5Priority": gs2352STPMSTI5Priority,
       "gs2352STPMSTI6Priority": gs2352STPMSTI6Priority,
       "gs2352STPMSTI7Priority": gs2352STPMSTI7Priority,
       "gs2352STPCISTPort": gs2352STPCISTPort,
       "gs2352STPCISTAggregatedPort": gs2352STPCISTAggregatedPort,
       "gs2352STPCISTAggregatedPortSTPEnabled": gs2352STPCISTAggregatedPortSTPEnabled,
       "gs2352STPCISTAggregatedPortPathCost": gs2352STPCISTAggregatedPortPathCost,
       "gs2352STPCISTAggregatedPortPriority": gs2352STPCISTAggregatedPortPriority,
       "gs2352STPCISTAggregatedPortAdminEdge": gs2352STPCISTAggregatedPortAdminEdge,
       "gs2352STPCISTAggregatedPortAutoEdge": gs2352STPCISTAggregatedPortAutoEdge,
       "gs2352STPCISTAggregatedPortRestrictedRole": gs2352STPCISTAggregatedPortRestrictedRole,
       "gs2352STPCISTAggregatedPortRestrictedTCN": gs2352STPCISTAggregatedPortRestrictedTCN,
       "gs2352STPCISTAggregatedPortBPDUGuard": gs2352STPCISTAggregatedPortBPDUGuard,
       "gs2352STPCISTAggregatedPortPointtoPoint": gs2352STPCISTAggregatedPortPointtoPoint,
       "gs2352STPCISTNormalPortTable": gs2352STPCISTNormalPortTable,
       "gs2352STPCISTNormalPortEntry": gs2352STPCISTNormalPortEntry,
       "gs2352STPCISTNormalPortConfPort": gs2352STPCISTNormalPortConfPort,
       "gs2352STPCISTNormalPortSTPEnabled": gs2352STPCISTNormalPortSTPEnabled,
       "gs2352STPCISTNormalPortPathCost": gs2352STPCISTNormalPortPathCost,
       "gs2352STPCISTNormalPortPriority": gs2352STPCISTNormalPortPriority,
       "gs2352STPCISTNormalPortAdminEdge": gs2352STPCISTNormalPortAdminEdge,
       "gs2352STPCISTNormalPortAutoEdge": gs2352STPCISTNormalPortAutoEdge,
       "gs2352STPCISTNormalPortRestrictedRole": gs2352STPCISTNormalPortRestrictedRole,
       "gs2352STPCISTNormalPortRestrictedTCN": gs2352STPCISTNormalPortRestrictedTCN,
       "gs2352STPCISTNormalPortBPDUGuard": gs2352STPCISTNormalPortBPDUGuard,
       "gs2352STPCISTNormalPortPointtoPoint": gs2352STPCISTNormalPortPointtoPoint,
       "gs2352STPMSTIPort": gs2352STPMSTIPort,
       "gs2352STPMSTI1Port": gs2352STPMSTI1Port,
       "gs2352STPMSTI1AggregatedPort": gs2352STPMSTI1AggregatedPort,
       "gs2352STPMSTI1AggregatedPortPathCost": gs2352STPMSTI1AggregatedPortPathCost,
       "gs2352STPMSTI1AggregatedPortPriority": gs2352STPMSTI1AggregatedPortPriority,
       "gs2352STPMSTI1NormalPortTable": gs2352STPMSTI1NormalPortTable,
       "gs2352STPMSTI1NormalPortEntry": gs2352STPMSTI1NormalPortEntry,
       "gs2352STPMSTI1NormalPortConfPort": gs2352STPMSTI1NormalPortConfPort,
       "gs2352STPMSTI1NormalPortPathCost": gs2352STPMSTI1NormalPortPathCost,
       "gs2352STPMSTI1NormalPortPriority": gs2352STPMSTI1NormalPortPriority,
       "gs2352STPMSTI2Port": gs2352STPMSTI2Port,
       "gs2352STPMSTI2AggregatedPort": gs2352STPMSTI2AggregatedPort,
       "gs2352STPMSTI2AggregatedPortPathCost": gs2352STPMSTI2AggregatedPortPathCost,
       "gs2352STPMSTI2AggregatedPortPriority": gs2352STPMSTI2AggregatedPortPriority,
       "gs2352STPMSTI2NormalPortTable": gs2352STPMSTI2NormalPortTable,
       "gs2352STPMSTI2NormalPortEntry": gs2352STPMSTI2NormalPortEntry,
       "gs2352STPMSTI2NormalPortConfPort": gs2352STPMSTI2NormalPortConfPort,
       "gs2352STPMSTI2NormalPortPathCost": gs2352STPMSTI2NormalPortPathCost,
       "gs2352STPMSTI2NormalPortPriority": gs2352STPMSTI2NormalPortPriority,
       "gs2352STPMSTI3Port": gs2352STPMSTI3Port,
       "gs2352STPMSTI3AggregatedPort": gs2352STPMSTI3AggregatedPort,
       "gs2352STPMSTI3AggregatedPortPathCost": gs2352STPMSTI3AggregatedPortPathCost,
       "gs2352STPMSTI3AggregatedPortPriority": gs2352STPMSTI3AggregatedPortPriority,
       "gs2352STPMSTI3NormalPortTable": gs2352STPMSTI3NormalPortTable,
       "gs2352STPMSTI3NormalPortEntry": gs2352STPMSTI3NormalPortEntry,
       "gs2352STPMSTI3NormalPortConfPort": gs2352STPMSTI3NormalPortConfPort,
       "gs2352STPMSTI3NormalPortPathCost": gs2352STPMSTI3NormalPortPathCost,
       "gs2352STPMSTI3NormalPortPriority": gs2352STPMSTI3NormalPortPriority,
       "gs2352STPMSTI4Port": gs2352STPMSTI4Port,
       "gs2352STPMSTI4AggregatedPort": gs2352STPMSTI4AggregatedPort,
       "gs2352STPMSTI4AggregatedPortPathCost": gs2352STPMSTI4AggregatedPortPathCost,
       "gs2352STPMSTI4AggregatedPortPriority": gs2352STPMSTI4AggregatedPortPriority,
       "gs2352STPMSTI4NormalPortTable": gs2352STPMSTI4NormalPortTable,
       "gs2352STPMSTI4NormalPortEntry": gs2352STPMSTI4NormalPortEntry,
       "gs2352STPMSTI4NormalPortConfPort": gs2352STPMSTI4NormalPortConfPort,
       "gs2352STPMSTI4NormalPortPathCost": gs2352STPMSTI4NormalPortPathCost,
       "gs2352STPMSTI4NormalPortPriority": gs2352STPMSTI4NormalPortPriority,
       "gs2352STPMSTI5Port": gs2352STPMSTI5Port,
       "gs2352STPMSTI5AggregatedPort": gs2352STPMSTI5AggregatedPort,
       "gs2352STPMSTI5AggregatedPortPathCost": gs2352STPMSTI5AggregatedPortPathCost,
       "gs2352STPMSTI5AggregatedPortPriority": gs2352STPMSTI5AggregatedPortPriority,
       "gs2352STPMSTI5NormalPortTable": gs2352STPMSTI5NormalPortTable,
       "gs2352STPMSTI5NormalPortEntry": gs2352STPMSTI5NormalPortEntry,
       "gs2352STPMSTI5NormalPortConfPort": gs2352STPMSTI5NormalPortConfPort,
       "gs2352STPMSTI5NormalPortPathCost": gs2352STPMSTI5NormalPortPathCost,
       "gs2352STPMSTI5NormalPortPriority": gs2352STPMSTI5NormalPortPriority,
       "gs2352STPMSTI6Port": gs2352STPMSTI6Port,
       "gs2352STPMSTI6AggregatedPort": gs2352STPMSTI6AggregatedPort,
       "gs2352STPMSTI6AggregatedPortPathCost": gs2352STPMSTI6AggregatedPortPathCost,
       "gs2352STPMSTI6AggregatedPortPriority": gs2352STPMSTI6AggregatedPortPriority,
       "gs2352STPMSTI6NormalPortTable": gs2352STPMSTI6NormalPortTable,
       "gs2352STPMSTI6NormalPortEntry": gs2352STPMSTI6NormalPortEntry,
       "gs2352STPMSTI6NormalPortConfPort": gs2352STPMSTI6NormalPortConfPort,
       "gs2352STPMSTI6NormalPortPathCost": gs2352STPMSTI6NormalPortPathCost,
       "gs2352STPMSTI6NormalPortPriority": gs2352STPMSTI6NormalPortPriority,
       "gs2352STPMSTI7Port": gs2352STPMSTI7Port,
       "gs2352STPMSTI7AggregatedPort": gs2352STPMSTI7AggregatedPort,
       "gs2352STPMSTI7AggregatedPortPathCost": gs2352STPMSTI7AggregatedPortPathCost,
       "gs2352STPMSTI7AggregatedPortPriority": gs2352STPMSTI7AggregatedPortPriority,
       "gs2352STPMSTI7NormalPortTable": gs2352STPMSTI7NormalPortTable,
       "gs2352STPMSTI7NormalPortEntry": gs2352STPMSTI7NormalPortEntry,
       "gs2352STPMSTI7NormalPortConfPort": gs2352STPMSTI7NormalPortConfPort,
       "gs2352STPMSTI7NormalPortPathCost": gs2352STPMSTI7NormalPortPathCost,
       "gs2352STPMSTI7NormalPortPriority": gs2352STPMSTI7NormalPortPriority,
       "gs2352STPBridgeStatus": gs2352STPBridgeStatus,
       "gs2352CISTBridgeSTP": gs2352CISTBridgeSTP,
       "gs2352CISTBridgeSTPStatus": gs2352CISTBridgeSTPStatus,
       "gs2352CISTBridgeInstance": gs2352CISTBridgeInstance,
       "gs2352CISTBridgeID": gs2352CISTBridgeID,
       "gs2352CISTRootID": gs2352CISTRootID,
       "gs2352CISTRootPort": gs2352CISTRootPort,
       "gs2352CISTRootCost": gs2352CISTRootCost,
       "gs2352CISTRegionalRoot": gs2352CISTRegionalRoot,
       "gs2352CISTInternalRootCost": gs2352CISTInternalRootCost,
       "gs2352CISTTopologyFlag": gs2352CISTTopologyFlag,
       "gs2352CISTTopologyChangeCount": gs2352CISTTopologyChangeCount,
       "gs2352CISTTopologyChangeLast": gs2352CISTTopologyChangeLast,
       "gs2352CISTPortStateTable": gs2352CISTPortStateTable,
       "gs2352CISTPortStateEntry": gs2352CISTPortStateEntry,
       "gs2352CISTPortStateIndex": gs2352CISTPortStateIndex,
       "gs2352CISTPortStatePort": gs2352CISTPortStatePort,
       "gs2352CISTPortStatePortID": gs2352CISTPortStatePortID,
       "gs2352CISTPortStateRole": gs2352CISTPortStateRole,
       "gs2352CISTPortStateState": gs2352CISTPortStateState,
       "gs2352CISTPortStatePathCost": gs2352CISTPortStatePathCost,
       "gs2352CISTPortStateEdge": gs2352CISTPortStateEdge,
       "gs2352CISTPortStatePoint2Point": gs2352CISTPortStatePoint2Point,
       "gs2352CISTPortStateUptime": gs2352CISTPortStateUptime,
       "gs2352MSTI1BridgeSTP": gs2352MSTI1BridgeSTP,
       "gs2352MSTI1BridgeSTPStatus": gs2352MSTI1BridgeSTPStatus,
       "gs2352MSTI1BridgeInstance": gs2352MSTI1BridgeInstance,
       "gs2352MSTI1BridgeID": gs2352MSTI1BridgeID,
       "gs2352MSTI1RootID": gs2352MSTI1RootID,
       "gs2352MSTI1RootPort": gs2352MSTI1RootPort,
       "gs2352MSTI1RootCost": gs2352MSTI1RootCost,
       "gs2352MSTI1TopologyFlag": gs2352MSTI1TopologyFlag,
       "gs2352MSTI1TopologyChangeCount": gs2352MSTI1TopologyChangeCount,
       "gs2352MSTI1TopologyChangeLast": gs2352MSTI1TopologyChangeLast,
       "gs2352MSTI1PortStateTable": gs2352MSTI1PortStateTable,
       "gs2352MSTI1PortStateEntry": gs2352MSTI1PortStateEntry,
       "gs2352MSTI1PortStateIndex": gs2352MSTI1PortStateIndex,
       "gs2352MSTI1PortStatePort": gs2352MSTI1PortStatePort,
       "gs2352MSTI1PortStatePortID": gs2352MSTI1PortStatePortID,
       "gs2352MSTI1PortStateRole": gs2352MSTI1PortStateRole,
       "gs2352MSTI1PortStateState": gs2352MSTI1PortStateState,
       "gs2352MSTI1PortStatePathCost": gs2352MSTI1PortStatePathCost,
       "gs2352MSTI1PortStateEdge": gs2352MSTI1PortStateEdge,
       "gs2352MSTI1PortStatePoint2Point": gs2352MSTI1PortStatePoint2Point,
       "gs2352MSTI1PortStateUptime": gs2352MSTI1PortStateUptime,
       "gs2352MSTI2BridgeSTP": gs2352MSTI2BridgeSTP,
       "gs2352MSTI2BridgeSTPStatus": gs2352MSTI2BridgeSTPStatus,
       "gs2352MSTI2BridgeInstance": gs2352MSTI2BridgeInstance,
       "gs2352MSTI2BridgeID": gs2352MSTI2BridgeID,
       "gs2352MSTI2RootID": gs2352MSTI2RootID,
       "gs2352MSTI2RootPort": gs2352MSTI2RootPort,
       "gs2352MSTI2RootCost": gs2352MSTI2RootCost,
       "gs2352MSTI2TopologyFlag": gs2352MSTI2TopologyFlag,
       "gs2352MSTI2TopologyChangeCount": gs2352MSTI2TopologyChangeCount,
       "gs2352MSTI2TopologyChangeLast": gs2352MSTI2TopologyChangeLast,
       "gs2352MSTI2PortStateTable": gs2352MSTI2PortStateTable,
       "gs2352MSTI2PortStateEntry": gs2352MSTI2PortStateEntry,
       "gs2352MSTI2PortStateIndex": gs2352MSTI2PortStateIndex,
       "gs2352MSTI2PortStatePort": gs2352MSTI2PortStatePort,
       "gs2352MSTI2PortStatePortID": gs2352MSTI2PortStatePortID,
       "gs2352MSTI2PortStateRole": gs2352MSTI2PortStateRole,
       "gs2352MSTI2PortStateState": gs2352MSTI2PortStateState,
       "gs2352MSTI2PortStatePathCost": gs2352MSTI2PortStatePathCost,
       "gs2352MSTI2PortStateEdge": gs2352MSTI2PortStateEdge,
       "gs2352MSTI2PortStatePoint2Point": gs2352MSTI2PortStatePoint2Point,
       "gs2352MSTI2PortStateUptime": gs2352MSTI2PortStateUptime,
       "gs2352MSTI3BridgeSTP": gs2352MSTI3BridgeSTP,
       "gs2352MSTI3BridgeSTPStatus": gs2352MSTI3BridgeSTPStatus,
       "gs2352MSTI3BridgeInstance": gs2352MSTI3BridgeInstance,
       "gs2352MSTI3BridgeID": gs2352MSTI3BridgeID,
       "gs2352MSTI3RootID": gs2352MSTI3RootID,
       "gs2352MSTI3RootPort": gs2352MSTI3RootPort,
       "gs2352MSTI3RootCost": gs2352MSTI3RootCost,
       "gs2352MSTI3TopologyFlag": gs2352MSTI3TopologyFlag,
       "gs2352MSTI3TopologyChangeCount": gs2352MSTI3TopologyChangeCount,
       "gs2352MSTI3TopologyChangeLast": gs2352MSTI3TopologyChangeLast,
       "gs2352MSTI3PortStateTable": gs2352MSTI3PortStateTable,
       "gs2352MSTI3PortStateEntry": gs2352MSTI3PortStateEntry,
       "gs2352MSTI3PortStateIndex": gs2352MSTI3PortStateIndex,
       "gs2352MSTI3PortStatePort": gs2352MSTI3PortStatePort,
       "gs2352MSTI3PortStatePortID": gs2352MSTI3PortStatePortID,
       "gs2352MSTI3PortStateRole": gs2352MSTI3PortStateRole,
       "gs2352MSTI3PortStateState": gs2352MSTI3PortStateState,
       "gs2352MSTI3PortStatePathCost": gs2352MSTI3PortStatePathCost,
       "gs2352MSTI3PortStateEdge": gs2352MSTI3PortStateEdge,
       "gs2352MSTI3PortStatePoint2Point": gs2352MSTI3PortStatePoint2Point,
       "gs2352MSTI3PortStateUptime": gs2352MSTI3PortStateUptime,
       "gs2352MSTI4BridgeSTP": gs2352MSTI4BridgeSTP,
       "gs2352MSTI4BridgeSTPStatus": gs2352MSTI4BridgeSTPStatus,
       "gs2352MSTI4BridgeInstance": gs2352MSTI4BridgeInstance,
       "gs2352MSTI4BridgeID": gs2352MSTI4BridgeID,
       "gs2352MSTI4RootID": gs2352MSTI4RootID,
       "gs2352MSTI4RootPort": gs2352MSTI4RootPort,
       "gs2352MSTI4RootCost": gs2352MSTI4RootCost,
       "gs2352MSTI4TopologyFlag": gs2352MSTI4TopologyFlag,
       "gs2352MSTI4TopologyChangeCount": gs2352MSTI4TopologyChangeCount,
       "gs2352MSTI4TopologyChangeLast": gs2352MSTI4TopologyChangeLast,
       "gs2352MSTI4PortStateTable": gs2352MSTI4PortStateTable,
       "gs2352MSTI4PortStateEntry": gs2352MSTI4PortStateEntry,
       "gs2352MSTI4PortStateIndex": gs2352MSTI4PortStateIndex,
       "gs2352MSTI4PortStatePort": gs2352MSTI4PortStatePort,
       "gs2352MSTI4PortStatePortID": gs2352MSTI4PortStatePortID,
       "gs2352MSTI4PortStateRole": gs2352MSTI4PortStateRole,
       "gs2352MSTI4PortStateState": gs2352MSTI4PortStateState,
       "gs2352MSTI4PortStatePathCost": gs2352MSTI4PortStatePathCost,
       "gs2352MSTI4PortStateEdge": gs2352MSTI4PortStateEdge,
       "gs2352MSTI4PortStatePoint2Point": gs2352MSTI4PortStatePoint2Point,
       "gs2352MSTI4PortStateUptime": gs2352MSTI4PortStateUptime,
       "gs2352MSTI5BridgeSTP": gs2352MSTI5BridgeSTP,
       "gs2352MSTI5BridgeSTPStatus": gs2352MSTI5BridgeSTPStatus,
       "gs2352MSTI5BridgeInstance": gs2352MSTI5BridgeInstance,
       "gs2352MSTI5BridgeID": gs2352MSTI5BridgeID,
       "gs2352MSTI5RootID": gs2352MSTI5RootID,
       "gs2352MSTI5RootPort": gs2352MSTI5RootPort,
       "gs2352MSTI5RootCost": gs2352MSTI5RootCost,
       "gs2352MSTI5TopologyFlag": gs2352MSTI5TopologyFlag,
       "gs2352MSTI5TopologyChangeCount": gs2352MSTI5TopologyChangeCount,
       "gs2352MSTI5TopologyChangeLast": gs2352MSTI5TopologyChangeLast,
       "gs2352MSTI5PortStateTable": gs2352MSTI5PortStateTable,
       "gs2352MSTI5PortStateEntry": gs2352MSTI5PortStateEntry,
       "gs2352MSTI5PortStateIndex": gs2352MSTI5PortStateIndex,
       "gs2352MSTI5PortStatePort": gs2352MSTI5PortStatePort,
       "gs2352MSTI5PortStatePortID": gs2352MSTI5PortStatePortID,
       "gs2352MSTI5PortStateRole": gs2352MSTI5PortStateRole,
       "gs2352MSTI5PortStateState": gs2352MSTI5PortStateState,
       "gs2352MSTI5PortStatePathCost": gs2352MSTI5PortStatePathCost,
       "gs2352MSTI5PortStateEdge": gs2352MSTI5PortStateEdge,
       "gs2352MSTI5PortStatePoint2Point": gs2352MSTI5PortStatePoint2Point,
       "gs2352MSTI5PortStateUptime": gs2352MSTI5PortStateUptime,
       "gs2352MSTI6BridgeSTP": gs2352MSTI6BridgeSTP,
       "gs2352MSTI6BridgeSTPStatus": gs2352MSTI6BridgeSTPStatus,
       "gs2352MSTI6BridgeInstance": gs2352MSTI6BridgeInstance,
       "gs2352MSTI6BridgeID": gs2352MSTI6BridgeID,
       "gs2352MSTI6RootID": gs2352MSTI6RootID,
       "gs2352MSTI6RootPort": gs2352MSTI6RootPort,
       "gs2352MSTI6RootCost": gs2352MSTI6RootCost,
       "gs2352MSTI6TopologyFlag": gs2352MSTI6TopologyFlag,
       "gs2352MSTI6TopologyChangeCount": gs2352MSTI6TopologyChangeCount,
       "gs2352MSTI6TopologyChangeLast": gs2352MSTI6TopologyChangeLast,
       "gs2352MSTI6PortStateTable": gs2352MSTI6PortStateTable,
       "gs2352MSTI6PortStateEntry": gs2352MSTI6PortStateEntry,
       "gs2352MSTI6PortStateIndex": gs2352MSTI6PortStateIndex,
       "gs2352MSTI6PortStatePort": gs2352MSTI6PortStatePort,
       "gs2352MSTI6PortStatePortID": gs2352MSTI6PortStatePortID,
       "gs2352MSTI6PortStateRole": gs2352MSTI6PortStateRole,
       "gs2352MSTI6PortStateState": gs2352MSTI6PortStateState,
       "gs2352MSTI6PortStatePathCost": gs2352MSTI6PortStatePathCost,
       "gs2352MSTI6PortStateEdge": gs2352MSTI6PortStateEdge,
       "gs2352MSTI6PortStatePoint2Point": gs2352MSTI6PortStatePoint2Point,
       "gs2352MSTI6PortStateUptime": gs2352MSTI6PortStateUptime,
       "gs2352MSTI7BridgeSTP": gs2352MSTI7BridgeSTP,
       "gs2352MSTI7BridgeSTPStatus": gs2352MSTI7BridgeSTPStatus,
       "gs2352MSTI7BridgeInstance": gs2352MSTI7BridgeInstance,
       "gs2352MSTI7BridgeID": gs2352MSTI7BridgeID,
       "gs2352MSTI7RootID": gs2352MSTI7RootID,
       "gs2352MSTI7RootPort": gs2352MSTI7RootPort,
       "gs2352MSTI7RootCost": gs2352MSTI7RootCost,
       "gs2352MSTI7TopologyFlag": gs2352MSTI7TopologyFlag,
       "gs2352MSTI7TopologyChangeCount": gs2352MSTI7TopologyChangeCount,
       "gs2352MSTI7TopologyChangeLast": gs2352MSTI7TopologyChangeLast,
       "gs2352MSTI7PortStateTable": gs2352MSTI7PortStateTable,
       "gs2352MSTI7PortStateEntry": gs2352MSTI7PortStateEntry,
       "gs2352MSTI7PortStateIndex": gs2352MSTI7PortStateIndex,
       "gs2352MSTI7PortStatePort": gs2352MSTI7PortStatePort,
       "gs2352MSTI7PortStatePortID": gs2352MSTI7PortStatePortID,
       "gs2352MSTI7PortStateRole": gs2352MSTI7PortStateRole,
       "gs2352MSTI7PortStateState": gs2352MSTI7PortStateState,
       "gs2352MSTI7PortStatePathCost": gs2352MSTI7PortStatePathCost,
       "gs2352MSTI7PortStateEdge": gs2352MSTI7PortStateEdge,
       "gs2352MSTI7PortStatePoint2Point": gs2352MSTI7PortStatePoint2Point,
       "gs2352MSTI7PortStateUptime": gs2352MSTI7PortStateUptime,
       "gs2352STPPortStatusTable": gs2352STPPortStatusTable,
       "gs2352STPPortStatusEntry": gs2352STPPortStatusEntry,
       "gs2352STPPortStatusPort": gs2352STPPortStatusPort,
       "gs2352STPPortStatusCISTRole": gs2352STPPortStatusCISTRole,
       "gs2352STPPortStatusCISTState": gs2352STPPortStatusCISTState,
       "gs2352STPPortStatusUptime": gs2352STPPortStatusUptime,
       "gs2352STPPortStatisticsTable": gs2352STPPortStatisticsTable,
       "gs2352STPPortStatisticsEntry": gs2352STPPortStatisticsEntry,
       "gs2352STPStatisticsIndex": gs2352STPStatisticsIndex,
       "gs2352STPStatisticsPort": gs2352STPStatisticsPort,
       "gs2352STPStatisticsTxMSTP": gs2352STPStatisticsTxMSTP,
       "gs2352STPStatisticsTxRSTP": gs2352STPStatisticsTxRSTP,
       "gs2352STPStatisticsTxSTP": gs2352STPStatisticsTxSTP,
       "gs2352STPStatisticsTxTCN": gs2352STPStatisticsTxTCN,
       "gs2352STPStatisticsRxMSTP": gs2352STPStatisticsRxMSTP,
       "gs2352STPStatisticsRxRSTP": gs2352STPStatisticsRxRSTP,
       "gs2352STPStatisticsRxSTP": gs2352STPStatisticsRxSTP,
       "gs2352STPStatisticsRxTCN": gs2352STPStatisticsRxTCN,
       "gs2352STPStatisticsDiscardedUnknown": gs2352STPStatisticsDiscardedUnknown,
       "gs2352STPStatisticsDiscardedIllegal": gs2352STPStatisticsDiscardedIllegal,
       "gs2352FilteringDataBase": gs2352FilteringDataBase,
       "gs2352FilteringDataBaseConfig": gs2352FilteringDataBaseConfig,
       "gs2352FilteringDataBaseAgingTime": gs2352FilteringDataBaseAgingTime,
       "gs2352FilteringDataBaseConfigTable": gs2352FilteringDataBaseConfigTable,
       "gs2352FilteringDataBaseConfigEntry": gs2352FilteringDataBaseConfigEntry,
       "gs2352FilteringDataBaseConfigPort": gs2352FilteringDataBaseConfigPort,
       "gs2352FilteringDataBaseConfigLearning": gs2352FilteringDataBaseConfigLearning,
       "gs2352FilteringDataBaseStaticMAC": gs2352FilteringDataBaseStaticMAC,
       "gs2352FilteringDataBaseStaticMACCreate": gs2352FilteringDataBaseStaticMACCreate,
       "gs2352FilteringDataBaseStaticMACTable": gs2352FilteringDataBaseStaticMACTable,
       "gs2352FilteringDataBaseStaticMACEntry": gs2352FilteringDataBaseStaticMACEntry,
       "gs2352FilteringDataBaseStaticMACIndex": gs2352FilteringDataBaseStaticMACIndex,
       "gs2352FilteringDataBaseStaticMACVLANId": gs2352FilteringDataBaseStaticMACVLANId,
       "gs2352FilteringDataBaseStaticMACAddress": gs2352FilteringDataBaseStaticMACAddress,
       "gs2352FilteringDataBaseStaticMACPortMembers": gs2352FilteringDataBaseStaticMACPortMembers,
       "gs2352FilteringDataBaseStaticMACRowStatus": gs2352FilteringDataBaseStaticMACRowStatus,
       "gs2352FilteringDataBaseDynamicMACTable": gs2352FilteringDataBaseDynamicMACTable,
       "gs2352FilteringDataBaseDynamicMACEntry": gs2352FilteringDataBaseDynamicMACEntry,
       "gs2352FilteringDataBaseDynamicMACIndex": gs2352FilteringDataBaseDynamicMACIndex,
       "gs2352FilteringDataBaseDynamicMACType": gs2352FilteringDataBaseDynamicMACType,
       "gs2352FilteringDataBaseDynamicMACVLAN": gs2352FilteringDataBaseDynamicMACVLAN,
       "gs2352FilteringDataBaseDynamicMACAddress": gs2352FilteringDataBaseDynamicMACAddress,
       "gs2352FilteringDataBaseDynamicPortMembers": gs2352FilteringDataBaseDynamicPortMembers,
       "gs2352SFlowAgent": gs2352SFlowAgent,
       "gs2352SFlowAgentCollector": gs2352SFlowAgentCollector,
       "gs2352SFlowAgentReceiverMode": gs2352SFlowAgentReceiverMode,
       "gs2352LMC": gs2352LMC,
       "gs2352LMCOperating": gs2352LMCOperating,
       "gs2352LMCConfigViaDhcp": gs2352LMCConfigViaDhcp,
       "gs2352LMCDomain": gs2352LMCDomain,
       "gs2352LMCDhcpClientAutoRenew": gs2352LMCDhcpClientAutoRenew,
       "gs2352LMCZeroTouchSupport": gs2352LMCZeroTouchSupport,
       "gs2352LMCPairingTokenPresent": gs2352LMCPairingTokenPresent,
       "gs2352LMCClientStatus": gs2352LMCClientStatus,
       "gs2352LMCManagementStatus": gs2352LMCManagementStatus,
       "gs2352LMCControlStatus": gs2352LMCControlStatus,
       "gs2352LMCMonitoringStatus": gs2352LMCMonitoringStatus,
       "gs2352LMCConfigurationSource": gs2352LMCConfigurationSource,
       "gs2352LMCConfigModified": gs2352LMCConfigModified,
       "gs2352LMCDeviceID": gs2352LMCDeviceID,
       "gs2352LMCRoundTripTime": gs2352LMCRoundTripTime,
       "gs2352Security": gs2352Security,
       "gs2352IPSourceGuard": gs2352IPSourceGuard,
       "gs2352IPSourceGuardConf": gs2352IPSourceGuardConf,
       "gs2352IPSourceGuardMode": gs2352IPSourceGuardMode,
       "gs2352IPSourceGuardPortConfigTable": gs2352IPSourceGuardPortConfigTable,
       "gs2352IPSourceGuardPortConfigEntry": gs2352IPSourceGuardPortConfigEntry,
       "gs2352IPSourceGuardPortConfigPort": gs2352IPSourceGuardPortConfigPort,
       "gs2352IPSourceGuardPortConfigMode": gs2352IPSourceGuardPortConfigMode,
       "gs2352IPSourceGuardPortMaxDynamicClients": gs2352IPSourceGuardPortMaxDynamicClients,
       "gs2352IPSourceGuardStatic": gs2352IPSourceGuardStatic,
       "gs2352IPSourceGuardStaticCreate": gs2352IPSourceGuardStaticCreate,
       "gs2352IPSourceGuardStaticTable": gs2352IPSourceGuardStaticTable,
       "gs2352IPSourceGuardStaticEntry": gs2352IPSourceGuardStaticEntry,
       "gs2352IPSourceGuardStaticIndex": gs2352IPSourceGuardStaticIndex,
       "gs2352IPSourceGuardStaticPort": gs2352IPSourceGuardStaticPort,
       "gs2352IPSourceGuardStaticVLANId": gs2352IPSourceGuardStaticVLANId,
       "gs2352IPSourceGuardStaticIPAddress": gs2352IPSourceGuardStaticIPAddress,
       "gs2352IPSourceGuardStaticMACAddress": gs2352IPSourceGuardStaticMACAddress,
       "gs2352IPSourceGuardStaticRowStatus": gs2352IPSourceGuardStaticRowStatus,
       "gs2352IPSourceGuardDynamicTable": gs2352IPSourceGuardDynamicTable,
       "gs2352IPSourceGuardDynamicEntry": gs2352IPSourceGuardDynamicEntry,
       "gs2352IPSourceGuardDynamicIndex": gs2352IPSourceGuardDynamicIndex,
       "gs2352IPSourceGuardDynamicPort": gs2352IPSourceGuardDynamicPort,
       "gs2352IPSourceGuardDynamicVLANId": gs2352IPSourceGuardDynamicVLANId,
       "gs2352IPSourceGuardDynamicIPAddress": gs2352IPSourceGuardDynamicIPAddress,
       "gs2352IPSourceGuardDynamicMACAddress": gs2352IPSourceGuardDynamicMACAddress,
       "gs2352ARPInspection": gs2352ARPInspection,
       "gs2352ARPInspectionConf": gs2352ARPInspectionConf,
       "gs2352ARPInspectionConfMode": gs2352ARPInspectionConfMode,
       "gs2352ARPInspectionConfTable": gs2352ARPInspectionConfTable,
       "gs2352ARPInspectionConfEntry": gs2352ARPInspectionConfEntry,
       "gs2352ARPInspectionConfPortIndex": gs2352ARPInspectionConfPortIndex,
       "gs2352ARPInspectionConfPortMode": gs2352ARPInspectionConfPortMode,
       "gs2352ARPInspectionStatic": gs2352ARPInspectionStatic,
       "gs2352ARPInspectionStaticCreate": gs2352ARPInspectionStaticCreate,
       "gs2352ARPInspectionStaticTable": gs2352ARPInspectionStaticTable,
       "gs2352ARPInspectionStaticEntry": gs2352ARPInspectionStaticEntry,
       "gs2352ARPInspectionStaticIndex": gs2352ARPInspectionStaticIndex,
       "gs2352ARPInspectionStaticPort": gs2352ARPInspectionStaticPort,
       "gs2352ARPInspectionStaticVLANId": gs2352ARPInspectionStaticVLANId,
       "gs2352ARPInspectionStaticIPAddress": gs2352ARPInspectionStaticIPAddress,
       "gs2352ARPInspectionStaticMACAddress": gs2352ARPInspectionStaticMACAddress,
       "gs2352ARPInspectionStaticRowStatus": gs2352ARPInspectionStaticRowStatus,
       "gs2352ARPInspectionDynamicTable": gs2352ARPInspectionDynamicTable,
       "gs2352ARPInspectionDynamicEntry": gs2352ARPInspectionDynamicEntry,
       "gs2352ARPInspectionDynamicIndex": gs2352ARPInspectionDynamicIndex,
       "gs2352ARPInspectionDynamicPort": gs2352ARPInspectionDynamicPort,
       "gs2352ARPInspectionDynamicVLANId": gs2352ARPInspectionDynamicVLANId,
       "gs2352ARPInspectionDynamicIPAddress": gs2352ARPInspectionDynamicIPAddress,
       "gs2352ARPInspectionDynamicMACAddress": gs2352ARPInspectionDynamicMACAddress,
       "gs2352ARPStaticGatewayCtrl": gs2352ARPStaticGatewayCtrl,
       "gs2352ARPStaticGatewayCtrlSystemConf": gs2352ARPStaticGatewayCtrlSystemConf,
       "gs2352ARPStaticGatewayCtrlMode": gs2352ARPStaticGatewayCtrlMode,
       "gs2352ARPStaticGatewayCtrlCreate": gs2352ARPStaticGatewayCtrlCreate,
       "gs2352ARPStaticGatewayCtrlTable": gs2352ARPStaticGatewayCtrlTable,
       "gs2352ARPStaticGatewayCtrlEntry": gs2352ARPStaticGatewayCtrlEntry,
       "gs2352ARPStaticGatewayCtrlIndex": gs2352ARPStaticGatewayCtrlIndex,
       "gs2352ARPStaticGatewayCtrlIPAddress": gs2352ARPStaticGatewayCtrlIPAddress,
       "gs2352ARPStaticGatewayCtrlMACAddress": gs2352ARPStaticGatewayCtrlMACAddress,
       "gs2352ARPStaticGatewayCtrlPort": gs2352ARPStaticGatewayCtrlPort,
       "gs2352ARPStaticGatewayCtrlAction": gs2352ARPStaticGatewayCtrlAction,
       "gs2352ARPStaticGatewayCtrlState": gs2352ARPStaticGatewayCtrlState,
       "gs2352ARPStaticGatewayCtrlReOpen": gs2352ARPStaticGatewayCtrlReOpen,
       "gs2352ARPStaticGatewayCtrlRowStatus": gs2352ARPStaticGatewayCtrlRowStatus,
       "gs2352ARPSpoofingPrevention": gs2352ARPSpoofingPrevention,
       "gs2352ARPSpoofingPreventionSystemConf": gs2352ARPSpoofingPreventionSystemConf,
       "gs2352ARPSpoofingPreventionMode": gs2352ARPSpoofingPreventionMode,
       "gs2352ARPSpoofingPreventionTable": gs2352ARPSpoofingPreventionTable,
       "gs2352ARPSpoofingPreventionEntry": gs2352ARPSpoofingPreventionEntry,
       "gs2352ARPSpoofingPreventionPort": gs2352ARPSpoofingPreventionPort,
       "gs2352ARPSpoofingPreventionPortMode": gs2352ARPSpoofingPreventionPortMode,
       "gs2352ARPSpoofingPreventionPortLimit": gs2352ARPSpoofingPreventionPortLimit,
       "gs2352ARPSpoofingPreventionPortAction": gs2352ARPSpoofingPreventionPortAction,
       "gs2352ARPSpoofingPreventionPortState": gs2352ARPSpoofingPreventionPortState,
       "gs2352ARPSpoofingPreventionPortReOpen": gs2352ARPSpoofingPreventionPortReOpen,
       "gs2352ARPIPDoSPrevention": gs2352ARPIPDoSPrevention,
       "gs2352ARPIPDoSPreventionTCPMode": gs2352ARPIPDoSPreventionTCPMode,
       "gs2352ARPIPDoSPreventionUDPMode": gs2352ARPIPDoSPreventionUDPMode,
       "gs2352ARPIPDoSPreventionICMPMode": gs2352ARPIPDoSPreventionICMPMode,
       "gs2352ARPIPDoSPreventionServerPort1": gs2352ARPIPDoSPreventionServerPort1,
       "gs2352ARPIPDoSPreventionServerPort2": gs2352ARPIPDoSPreventionServerPort2,
       "gs2352ARPIPDoSPreventionServerPort3": gs2352ARPIPDoSPreventionServerPort3,
       "gs2352ARPIPDoSPreventionServerPort4": gs2352ARPIPDoSPreventionServerPort4,
       "gs2352DHCPSnooping": gs2352DHCPSnooping,
       "gs2352DHCPSnoopingConf": gs2352DHCPSnoopingConf,
       "gs2352DHCPSnoopingMode": gs2352DHCPSnoopingMode,
       "gs2352DHCPSnoopingPortModeConfigurationTable": gs2352DHCPSnoopingPortModeConfigurationTable,
       "gs2352DHCPSnoopingPortModeConfigurationEntry": gs2352DHCPSnoopingPortModeConfigurationEntry,
       "gs2352DHCPSnoopingPortModeConfigurationPort": gs2352DHCPSnoopingPortModeConfigurationPort,
       "gs2352DHCPSnoopingPortModeConfigurationMode": gs2352DHCPSnoopingPortModeConfigurationMode,
       "gs2352DHCPSnoopingStatisticsTable": gs2352DHCPSnoopingStatisticsTable,
       "gs2352DHCPSnoopingStatisticsEntry": gs2352DHCPSnoopingStatisticsEntry,
       "gs2352DHCPSnoopingStatisticsPort": gs2352DHCPSnoopingStatisticsPort,
       "gs2352DHCPSnoopingStatisticsClear": gs2352DHCPSnoopingStatisticsClear,
       "gs2352DHCPSnoopingRxDiscover": gs2352DHCPSnoopingRxDiscover,
       "gs2352DHCPSnoopingRxOffer": gs2352DHCPSnoopingRxOffer,
       "gs2352DHCPSnoopingRxRequest": gs2352DHCPSnoopingRxRequest,
       "gs2352DHCPSnoopingRxDecline": gs2352DHCPSnoopingRxDecline,
       "gs2352DHCPSnoopingRxACK": gs2352DHCPSnoopingRxACK,
       "gs2352DHCPSnoopingRxNAK": gs2352DHCPSnoopingRxNAK,
       "gs2352DHCPSnoopingRxRelease": gs2352DHCPSnoopingRxRelease,
       "gs2352DHCPSnoopingRxInform": gs2352DHCPSnoopingRxInform,
       "gs2352DHCPSnoopingRxLeaseQuery": gs2352DHCPSnoopingRxLeaseQuery,
       "gs2352DHCPSnoopingRxLeaseUnassigned": gs2352DHCPSnoopingRxLeaseUnassigned,
       "gs2352DHCPSnoopingRxLeaseUnknown": gs2352DHCPSnoopingRxLeaseUnknown,
       "gs2352DHCPSnoopingRxLeaseActive": gs2352DHCPSnoopingRxLeaseActive,
       "gs2352DHCPSnoopingTxDiscover": gs2352DHCPSnoopingTxDiscover,
       "gs2352DHCPSnoopingTxOffer": gs2352DHCPSnoopingTxOffer,
       "gs2352DHCPSnoopingTxRequest": gs2352DHCPSnoopingTxRequest,
       "gs2352DHCPSnoopingTxDecline": gs2352DHCPSnoopingTxDecline,
       "gs2352DHCPSnoopingTxACK": gs2352DHCPSnoopingTxACK,
       "gs2352DHCPSnoopingTxNAK": gs2352DHCPSnoopingTxNAK,
       "gs2352DHCPSnoopingTxRelease": gs2352DHCPSnoopingTxRelease,
       "gs2352DHCPSnoopingTxInform": gs2352DHCPSnoopingTxInform,
       "gs2352DHCPSnoopingTxLeaseQuery": gs2352DHCPSnoopingTxLeaseQuery,
       "gs2352DHCPSnoopingTxLeaseUnassigned": gs2352DHCPSnoopingTxLeaseUnassigned,
       "gs2352DHCPSnoopingTxLeaseUnknown": gs2352DHCPSnoopingTxLeaseUnknown,
       "gs2352DHCPSnoopingTxLeaseActive": gs2352DHCPSnoopingTxLeaseActive,
       "gs2352DHCPRelay": gs2352DHCPRelay,
       "gs2352DHCPRelayConfiguration": gs2352DHCPRelayConfiguration,
       "gs2352DHCPRelayMode": gs2352DHCPRelayMode,
       "gs2352DHCPRelayServer": gs2352DHCPRelayServer,
       "gs2352DHCPRelayInformationMode": gs2352DHCPRelayInformationMode,
       "gs2352DHCPRelayInformationPolicy": gs2352DHCPRelayInformationPolicy,
       "gs2352DHCPRelayConfigurationGateways": gs2352DHCPRelayConfigurationGateways,
       "gs2352DHCPRelayConfigurationGatewaysCreate": gs2352DHCPRelayConfigurationGatewaysCreate,
       "gs2352DHCPRelayConfigurationGatewaysTable": gs2352DHCPRelayConfigurationGatewaysTable,
       "gs2352DHCPRelayConfigurationGatewaysEntry": gs2352DHCPRelayConfigurationGatewaysEntry,
       "gs2352DHCPRelayConfigurationGatewaysIndex": gs2352DHCPRelayConfigurationGatewaysIndex,
       "gs2352DHCPRelayConfigurationGatewaysVLANId": gs2352DHCPRelayConfigurationGatewaysVLANId,
       "gs2352DHCPRelayConfigurationGatewaysIP": gs2352DHCPRelayConfigurationGatewaysIP,
       "gs2352DHCPRelayConfigurationGatewaysRowStatus": gs2352DHCPRelayConfigurationGatewaysRowStatus,
       "gs2352DHCPRelayInformationCustom": gs2352DHCPRelayInformationCustom,
       "gs2352DHCPRelayStatistics": gs2352DHCPRelayStatistics,
       "gs2352DHCPRelayServerStatistics": gs2352DHCPRelayServerStatistics,
       "gs2352ServerStatTransmitToServer": gs2352ServerStatTransmitToServer,
       "gs2352ServerStatTransmitError": gs2352ServerStatTransmitError,
       "gs2352ServerStatReceiveFromServer": gs2352ServerStatReceiveFromServer,
       "gs2352ServerStatReceiveMissingAgentOption": gs2352ServerStatReceiveMissingAgentOption,
       "gs2352ServerStatReceiveMissingCircuitID": gs2352ServerStatReceiveMissingCircuitID,
       "gs2352ServerStatReceiveMissingRemoteID": gs2352ServerStatReceiveMissingRemoteID,
       "gs2352ServerStatReceiveBadCircuitID": gs2352ServerStatReceiveBadCircuitID,
       "gs2352ServerStatReceiveBadRemoteID": gs2352ServerStatReceiveBadRemoteID,
       "gs2352DHCPRelayClientStatistics": gs2352DHCPRelayClientStatistics,
       "gs2352ClientStatTransmitToClient": gs2352ClientStatTransmitToClient,
       "gs2352ClientStatTransmitError": gs2352ClientStatTransmitError,
       "gs2352ClientStatReceivefromClient": gs2352ClientStatReceivefromClient,
       "gs2352ClientStatReceiveAgentOption": gs2352ClientStatReceiveAgentOption,
       "gs2352ClientStatReplaceAgentOption": gs2352ClientStatReplaceAgentOption,
       "gs2352ClientStatKeepAgentOption": gs2352ClientStatKeepAgentOption,
       "gs2352ClientStatDropAgentOption": gs2352ClientStatDropAgentOption,
       "gs2352PortSecurity": gs2352PortSecurity,
       "gs2352PortSecLimitCtrl": gs2352PortSecLimitCtrl,
       "gs2352PortSecLimitCtrlSystemConf": gs2352PortSecLimitCtrlSystemConf,
       "gs2352PortSecurityMode": gs2352PortSecurityMode,
       "gs2352PortSecurityAging": gs2352PortSecurityAging,
       "gs2352PortSecurityAgingPeriod": gs2352PortSecurityAgingPeriod,
       "gs2352PortSecLimitCtrlTable": gs2352PortSecLimitCtrlTable,
       "gs2352PortSecLimitCtrlEntry": gs2352PortSecLimitCtrlEntry,
       "gs2352PortSecLimitCtrlPort": gs2352PortSecLimitCtrlPort,
       "gs2352PortSecLimitCtrlPortMode": gs2352PortSecLimitCtrlPortMode,
       "gs2352PortSecLimitCtrlPortLimit": gs2352PortSecLimitCtrlPortLimit,
       "gs2352PortSecLimitCtrlPortAction": gs2352PortSecLimitCtrlPortAction,
       "gs2352PortSecLimitCtrlPortState": gs2352PortSecLimitCtrlPortState,
       "gs2352PortSecLimitCtrlPortReOpen": gs2352PortSecLimitCtrlPortReOpen,
       "gs2352PortSecSwitchStatusTable": gs2352PortSecSwitchStatusTable,
       "gs2352PortSecSwitchStatusEntry": gs2352PortSecSwitchStatusEntry,
       "gs2352PortSecSwitchStatusPort": gs2352PortSecSwitchStatusPort,
       "gs2352PortSecSwitchStatusUsers": gs2352PortSecSwitchStatusUsers,
       "gs2352PortSecSwitchStatusState": gs2352PortSecSwitchStatusState,
       "gs2352PortSecSwitchStatusMACCountCurrent": gs2352PortSecSwitchStatusMACCountCurrent,
       "gs2352PortSecSwitchStatusMACCountLimit": gs2352PortSecSwitchStatusMACCountLimit,
       "gs2352PortSecPortStatus": gs2352PortSecPortStatus,
       "gs2352PortSecPortStatusPort": gs2352PortSecPortStatusPort,
       "gs2352PortSecPortStatusTable": gs2352PortSecPortStatusTable,
       "gs2352PortSecPortStatusEntry": gs2352PortSecPortStatusEntry,
       "gs2352PortSecPortStatusIndex": gs2352PortSecPortStatusIndex,
       "gs2352PortSecPortStatusMACAddress": gs2352PortSecPortStatusMACAddress,
       "gs2352PortSecPortStatusVLANId": gs2352PortSecPortStatusVLANId,
       "gs2352PortSecPortStatusState": gs2352PortSecPortStatusState,
       "gs2352PortSecPortStatusTimeOfAddition": gs2352PortSecPortStatusTimeOfAddition,
       "gs2352PortSecPortStatusAgeAndHold": gs2352PortSecPortStatusAgeAndHold,
       "gs2352AccessManagement": gs2352AccessManagement,
       "gs2352AccessMgtConf": gs2352AccessMgtConf,
       "gs2352AccessMgtConfMode": gs2352AccessMgtConfMode,
       "gs2352AccessMgtConfCreate": gs2352AccessMgtConfCreate,
       "gs2352AccessMgtConfTable": gs2352AccessMgtConfTable,
       "gs2352AccessMgtConfEntry": gs2352AccessMgtConfEntry,
       "gs2352AccessMgtIndex": gs2352AccessMgtIndex,
       "gs2352AccessMgtAddresstype": gs2352AccessMgtAddresstype,
       "gs2352AccessMgtStartIpAddress": gs2352AccessMgtStartIpAddress,
       "gs2352AccessMgtEndIpAddress": gs2352AccessMgtEndIpAddress,
       "gs2352AccessMgtHttpHttps": gs2352AccessMgtHttpHttps,
       "gs2352AccessMgtSNMP": gs2352AccessMgtSNMP,
       "gs2352AccessMgtTelnetSSH": gs2352AccessMgtTelnetSSH,
       "gs2352AccessMgtRowStatus": gs2352AccessMgtRowStatus,
       "gs2352AccessMgtStatistics": gs2352AccessMgtStatistics,
       "gs2352HttpReceivedPkts": gs2352HttpReceivedPkts,
       "gs2352HttpAllowedPkts": gs2352HttpAllowedPkts,
       "gs2352HttpDiscardedPkts": gs2352HttpDiscardedPkts,
       "gs2352HttpsReceivedPkts": gs2352HttpsReceivedPkts,
       "gs2352HttpsAllowedPkts": gs2352HttpsAllowedPkts,
       "gs2352HttpsDiscardedPkts": gs2352HttpsDiscardedPkts,
       "gs2352SnmpReceivedPkts": gs2352SnmpReceivedPkts,
       "gs2352SnmpAllowedPkts": gs2352SnmpAllowedPkts,
       "gs2352SnmpDiscardedPkts": gs2352SnmpDiscardedPkts,
       "gs2352TelnetReceivedPkts": gs2352TelnetReceivedPkts,
       "gs2352TelnetAllowedPkts": gs2352TelnetAllowedPkts,
       "gs2352TelnetDiscardedPkts": gs2352TelnetDiscardedPkts,
       "gs2352SSHReceivedPkts": gs2352SSHReceivedPkts,
       "gs2352SSHAllowedPkts": gs2352SSHAllowedPkts,
       "gs2352SSHDiscardedPkts": gs2352SSHDiscardedPkts,
       "gs2352AccessMgtStatisticsClearAll": gs2352AccessMgtStatisticsClearAll,
       "gs2352SSH": gs2352SSH,
       "gs2352SSHMode": gs2352SSHMode,
       "gs2352HTTPS": gs2352HTTPS,
       "gs2352HTTPSMode": gs2352HTTPSMode,
       "gs2352HTTPSAutoRedirect": gs2352HTTPSAutoRedirect,
       "gs2352HTTPSCertRenew": gs2352HTTPSCertRenew,
       "gs2352HTTPSMinProtoVersion": gs2352HTTPSMinProtoVersion,
       "gs2352HTTPMode": gs2352HTTPMode,
       "gs2352AuthMethod": gs2352AuthMethod,
       "gs2352ConsoleAuthMethod": gs2352ConsoleAuthMethod,
       "gs2352ConsoleFallback": gs2352ConsoleFallback,
       "gs2352TelnetAuthMethod": gs2352TelnetAuthMethod,
       "gs2352TelnetFallback": gs2352TelnetFallback,
       "gs2352SshAuthMethod": gs2352SshAuthMethod,
       "gs2352SshFallback": gs2352SshFallback,
       "gs2352TftpAuthMethod": gs2352TftpAuthMethod,
       "gs2352TftpFallback": gs2352TftpFallback,
       "gs2352LoginFailures": gs2352LoginFailures,
       "gs2352LockMinutes": gs2352LockMinutes,
       "gs2352HttpAuthMethod": gs2352HttpAuthMethod,
       "gs2352HttpFallback": gs2352HttpFallback,
       "gs2352HttpsAuthMethod": gs2352HttpsAuthMethod,
       "gs2352HttpsFallback": gs2352HttpsFallback,
       "gs2352AAA": gs2352AAA,
       "gs2352AAACommonServer": gs2352AAACommonServer,
       "gs2352AAACommonServerTimeout": gs2352AAACommonServerTimeout,
       "gs2352AAACommonServerDeadTime": gs2352AAACommonServerDeadTime,
       "gs2352AAATACACSPlusAuthAndAccounting": gs2352AAATACACSPlusAuthAndAccounting,
       "gs2352AAAAuthorization": gs2352AAAAuthorization,
       "gs2352AAAFallbackToLocalAuthorization": gs2352AAAFallbackToLocalAuthorization,
       "gs2352AAAAccounting": gs2352AAAAccounting,
       "gs2352RADIUSAuthenticationServerTable": gs2352RADIUSAuthenticationServerTable,
       "gs2352RADIUSAuthenticationServerEntry": gs2352RADIUSAuthenticationServerEntry,
       "gs2352RADIUSAuthenticationServerIndex": gs2352RADIUSAuthenticationServerIndex,
       "gs2352RADIUSAuthenticationServerEnable": gs2352RADIUSAuthenticationServerEnable,
       "gs2352RADIUSAuthenticationServerIP": gs2352RADIUSAuthenticationServerIP,
       "gs2352RADIUSAuthenticationServerPort": gs2352RADIUSAuthenticationServerPort,
       "gs2352RADIUSAuthenticationServerSecret": gs2352RADIUSAuthenticationServerSecret,
       "gs2352RADIUSAccountingServerTable": gs2352RADIUSAccountingServerTable,
       "gs2352RADIUSAccountingServerEntry": gs2352RADIUSAccountingServerEntry,
       "gs2352RADIUSAccountingServerIndex": gs2352RADIUSAccountingServerIndex,
       "gs2352RADIUSAccountingServerEnable": gs2352RADIUSAccountingServerEnable,
       "gs2352RADIUSAccountingServerIP": gs2352RADIUSAccountingServerIP,
       "gs2352RADIUSAccountingServerPort": gs2352RADIUSAccountingServerPort,
       "gs2352RADIUSAccountingServerSecret": gs2352RADIUSAccountingServerSecret,
       "gs2352TACACSPlusAuthenticationServerTable": gs2352TACACSPlusAuthenticationServerTable,
       "gs2352TACACSPlusAuthenticationServerEntry": gs2352TACACSPlusAuthenticationServerEntry,
       "gs2352TACACSPlusAuthenticationServerIndex": gs2352TACACSPlusAuthenticationServerIndex,
       "gs2352TACACSPlusAuthenticationServerEnable": gs2352TACACSPlusAuthenticationServerEnable,
       "gs2352TACACSPlusAuthenticationServerIP": gs2352TACACSPlusAuthenticationServerIP,
       "gs2352TACACSPlusAuthenticationServerPort": gs2352TACACSPlusAuthenticationServerPort,
       "gs2352TACACSPlusAuthenticationServerSecret": gs2352TACACSPlusAuthenticationServerSecret,
       "gs2352RADIUSStatisticsTable": gs2352RADIUSStatisticsTable,
       "gs2352RADIUSStatisticsEntry": gs2352RADIUSStatisticsEntry,
       "gs2352RADIUSAuthStatisticsServerIndex": gs2352RADIUSAuthStatisticsServerIndex,
       "gs2352RADIUSAuthStatisticsRecPktAccessAccepts": gs2352RADIUSAuthStatisticsRecPktAccessAccepts,
       "gs2352RADIUSAuthStatisticsRecPktAccessRejects": gs2352RADIUSAuthStatisticsRecPktAccessRejects,
       "gs2352RADIUSAuthStatisticsRecPktAccessChallenges": gs2352RADIUSAuthStatisticsRecPktAccessChallenges,
       "gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses": gs2352RADIUSAuthStatisticsRecPktMalformedAccResponses,
       "gs2352RADIUSAuthStatisticsRecPktBadAuthenticators": gs2352RADIUSAuthStatisticsRecPktBadAuthenticators,
       "gs2352RADIUSAuthStatisticsRecPktUnknownTypes": gs2352RADIUSAuthStatisticsRecPktUnknownTypes,
       "gs2352RADIUSAuthStatisticsRecPktDropped": gs2352RADIUSAuthStatisticsRecPktDropped,
       "gs2352RADIUSAuthStatisticsTransmitPktAccessRequests": gs2352RADIUSAuthStatisticsTransmitPktAccessRequests,
       "gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions": gs2352RADIUSAuthStatisticsTransmitPktAccessRetransmissions,
       "gs2352RADIUSAuthStatisticsTransmitPktPendingRequests": gs2352RADIUSAuthStatisticsTransmitPktPendingRequests,
       "gs2352RADIUSAuthStatisticsTransmitPktTimeouts": gs2352RADIUSAuthStatisticsTransmitPktTimeouts,
       "gs2352RADIUSAuthIP": gs2352RADIUSAuthIP,
       "gs2352RADIUSAuthState": gs2352RADIUSAuthState,
       "gs2352RADIUSAuthRoundTripTime": gs2352RADIUSAuthRoundTripTime,
       "gs2352RADIUSAccountingStatisticsRecPktResponses": gs2352RADIUSAccountingStatisticsRecPktResponses,
       "gs2352RADIUSAccountingStatisticsRecPktMalformedResponses": gs2352RADIUSAccountingStatisticsRecPktMalformedResponses,
       "gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators": gs2352RADIUSAccountingStatisticsRecPktBadAuthenticators,
       "gs2352RADIUSAccountingStatisticsRecPktUnknownTypes": gs2352RADIUSAccountingStatisticsRecPktUnknownTypes,
       "gs2352RADIUSAccountingStatisticsRecPktDropped": gs2352RADIUSAccountingStatisticsRecPktDropped,
       "gs2352RADIUSAccountingStatisticsTransmitPktRequests": gs2352RADIUSAccountingStatisticsTransmitPktRequests,
       "gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions": gs2352RADIUSAccountingStatisticsTransmitPktRetransmissions,
       "gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests": gs2352RADIUSAccountingStatisticsTransmitPktPendingRequests,
       "gs2352RADIUSAccountingStatisticsTransmitPktTimeouts": gs2352RADIUSAccountingStatisticsTransmitPktTimeouts,
       "gs2352RADIUSAccountingIP": gs2352RADIUSAccountingIP,
       "gs2352RADIUSAccountingState": gs2352RADIUSAccountingState,
       "gs2352RADIUSAccountingRoundTripTime": gs2352RADIUSAccountingRoundTripTime,
       "gs2352RADIUSStatisticsClear": gs2352RADIUSStatisticsClear,
       "gs2352NAS": gs2352NAS,
       "gs2352NASConfiguration": gs2352NASConfiguration,
       "gs2352NASConfigMode": gs2352NASConfigMode,
       "gs2352NASConfigReauthEnabled": gs2352NASConfigReauthEnabled,
       "gs2352NASConfigReauthPeriod": gs2352NASConfigReauthPeriod,
       "gs2352NASConfigEAPOLTimeout": gs2352NASConfigEAPOLTimeout,
       "gs2352NASConfigAgingPeriod": gs2352NASConfigAgingPeriod,
       "gs2352NASConfigHoldTime": gs2352NASConfigHoldTime,
       "gs2352NASConfigRADIUSAssignedQoSEnabled": gs2352NASConfigRADIUSAssignedQoSEnabled,
       "gs2352NASConfigRADIUSAssignedVLANEnabled": gs2352NASConfigRADIUSAssignedVLANEnabled,
       "gs2352NASConfigGuestVLANEnabled": gs2352NASConfigGuestVLANEnabled,
       "gs2352NASConfigGuestVLANID": gs2352NASConfigGuestVLANID,
       "gs2352NASConfigMaxReauthCount": gs2352NASConfigMaxReauthCount,
       "gs2352NASConfigAllowGuestVLANEAPOLSeen": gs2352NASConfigAllowGuestVLANEAPOLSeen,
       "gs2352NASPortConfigTable": gs2352NASPortConfigTable,
       "gs2352NASPortConfigEntry": gs2352NASPortConfigEntry,
       "gs2352NASPortConfigPort": gs2352NASPortConfigPort,
       "gs2352NASPortConfigAdminState": gs2352NASPortConfigAdminState,
       "gs2352NASPortConfigRADIUSAssignedQoSEnabled": gs2352NASPortConfigRADIUSAssignedQoSEnabled,
       "gs2352NASPortConfigRADIUSAssignedVLANEnabled": gs2352NASPortConfigRADIUSAssignedVLANEnabled,
       "gs2352NASPortConfigGuestVLANEnabled": gs2352NASPortConfigGuestVLANEnabled,
       "gs2352NASPortConfigPortState": gs2352NASPortConfigPortState,
       "gs2352NASPortConfigReauthenticate": gs2352NASPortConfigReauthenticate,
       "gs2352NASPortConfigReinitialize": gs2352NASPortConfigReinitialize,
       "gs2352NASPortConfigFallbackEnabled": gs2352NASPortConfigFallbackEnabled,
       "gs2352NASConfigMacBasedUseEAP": gs2352NASConfigMacBasedUseEAP,
       "gs2352NASSwitchStatusTable": gs2352NASSwitchStatusTable,
       "gs2352NASSwitchStatusEntry": gs2352NASSwitchStatusEntry,
       "gs2352NASSwitchStatusAdminState": gs2352NASSwitchStatusAdminState,
       "gs2352NASSwitchStatusPortState": gs2352NASSwitchStatusPortState,
       "gs2352NASSwitchStatusLastSource": gs2352NASSwitchStatusLastSource,
       "gs2352NASSwitchStatusLastID": gs2352NASSwitchStatusLastID,
       "gs2352NASSwitchStatusQoSClass": gs2352NASSwitchStatusQoSClass,
       "gs2352NASSwitchStatusPortVlanID": gs2352NASSwitchStatusPortVlanID,
       "gs2352NASPortStatus": gs2352NASPortStatus,
       "gs2352NASPortStatusCountersTable": gs2352NASPortStatusCountersTable,
       "gs2352NASPortStatusCountersEntry": gs2352NASPortStatusCountersEntry,
       "gs2352NASRxCountersEAPOLTotal": gs2352NASRxCountersEAPOLTotal,
       "gs2352NASRxCountersEAPOLResponseID": gs2352NASRxCountersEAPOLResponseID,
       "gs2352NASRxCountersEAPOLResponses": gs2352NASRxCountersEAPOLResponses,
       "gs2352NASRxCountersEAPOLStart": gs2352NASRxCountersEAPOLStart,
       "gs2352NASRxCountersEAPOLLogoff": gs2352NASRxCountersEAPOLLogoff,
       "gs2352NASRxCountersEAPOLInvalidType": gs2352NASRxCountersEAPOLInvalidType,
       "gs2352NASRxCountersEAPOLInvalidLength": gs2352NASRxCountersEAPOLInvalidLength,
       "gs2352NASTxCountersEAPOLTotal": gs2352NASTxCountersEAPOLTotal,
       "gs2352NASTxCountersEAPOLRequestID": gs2352NASTxCountersEAPOLRequestID,
       "gs2352NASTxCountersEAPOLRequests": gs2352NASTxCountersEAPOLRequests,
       "gs2352NASRxBackendServerCountersAccessChallenges": gs2352NASRxBackendServerCountersAccessChallenges,
       "gs2352NASRxBackendServerCountersOtherRequests": gs2352NASRxBackendServerCountersOtherRequests,
       "gs2352NASRxBackendServerCountersAuthSuccesses": gs2352NASRxBackendServerCountersAuthSuccesses,
       "gs2352NASRxBackendServerCountersAuthFailures": gs2352NASRxBackendServerCountersAuthFailures,
       "gs2352NASTxBackendServerCountersResponses": gs2352NASTxBackendServerCountersResponses,
       "gs2352NASLastSupplicantInfoMACAddress": gs2352NASLastSupplicantInfoMACAddress,
       "gs2352NASLastSupplicantInfoVlanID": gs2352NASLastSupplicantInfoVlanID,
       "gs2352NASLastSupplicantInfoVersion": gs2352NASLastSupplicantInfoVersion,
       "gs2352NASLastSupplicantInfoIdentity": gs2352NASLastSupplicantInfoIdentity,
       "gs2352NASCountersDoClear": gs2352NASCountersDoClear,
       "gs2352NASPortStatusClientsTable": gs2352NASPortStatusClientsTable,
       "gs2352NASPortStatusClientsEntry": gs2352NASPortStatusClientsEntry,
       "gs2352NASClientsIndex": gs2352NASClientsIndex,
       "gs2352NASClientsIdentity": gs2352NASClientsIdentity,
       "gs2352NASClientsMACAddress": gs2352NASClientsMACAddress,
       "gs2352NASClientsVlanID": gs2352NASClientsVlanID,
       "gs2352NASClientsState": gs2352NASClientsState,
       "gs2352NASClientsLastAuth": gs2352NASClientsLastAuth,
       "gs2352NASRxClientsEAPOLTotal": gs2352NASRxClientsEAPOLTotal,
       "gs2352NASRxClientsEAPOLResponseID": gs2352NASRxClientsEAPOLResponseID,
       "gs2352NASRxClientsEAPOLResponses": gs2352NASRxClientsEAPOLResponses,
       "gs2352NASRxClientsEAPOLStart": gs2352NASRxClientsEAPOLStart,
       "gs2352NASRxClientsEAPOLLogoff": gs2352NASRxClientsEAPOLLogoff,
       "gs2352NASRxClientsEAPOLInvalidType": gs2352NASRxClientsEAPOLInvalidType,
       "gs2352NASRxClientsEAPOLInvalidLength": gs2352NASRxClientsEAPOLInvalidLength,
       "gs2352NASTxClientsEAPOLTotal": gs2352NASTxClientsEAPOLTotal,
       "gs2352NASTxClientsEAPOLRequestID": gs2352NASTxClientsEAPOLRequestID,
       "gs2352NASTxClientsEAPOLRequests": gs2352NASTxClientsEAPOLRequests,
       "gs2352NASRxBackendServerClientsAccessChallenges": gs2352NASRxBackendServerClientsAccessChallenges,
       "gs2352NASRxBackendServerClientsOtherRequests": gs2352NASRxBackendServerClientsOtherRequests,
       "gs2352NASRxBackendServerClientsAuthSuccesses": gs2352NASRxBackendServerClientsAuthSuccesses,
       "gs2352NASRxBackendServerClientsAuthFailures": gs2352NASRxBackendServerClientsAuthFailures,
       "gs2352NASTxBackendServerClientsResponses": gs2352NASTxBackendServerClientsResponses,
       "gs2352Maintenance": gs2352Maintenance,
       "gs2352RestartDevice": gs2352RestartDevice,
       "gs2352Firmware": gs2352Firmware,
       "gs2352FirmwareIpAddress": gs2352FirmwareIpAddress,
       "gs2352FirmwareFileName": gs2352FirmwareFileName,
       "gs2352DoFirmwareUpgrade": gs2352DoFirmwareUpgrade,
       "gs2352SaveOrRestore": gs2352SaveOrRestore,
       "gs2352FactoryDefaults": gs2352FactoryDefaults,
       "gs2352SaveStart": gs2352SaveStart,
       "gs2352SaveUser": gs2352SaveUser,
       "gs2352RestoreUser": gs2352RestoreUser,
       "gs2352ExportOrImport": gs2352ExportOrImport,
       "gs2352ExportIpAddress": gs2352ExportIpAddress,
       "gs2352ExportConfigName": gs2352ExportConfigName,
       "gs2352DoExportConfig": gs2352DoExportConfig,
       "gs2352ImportIpAddress": gs2352ImportIpAddress,
       "gs2352ImportConfigName": gs2352ImportConfigName,
       "gs2352DoImportConfig": gs2352DoImportConfig,
       "gs2352Diagnostics": gs2352Diagnostics,
       "gs2352PingIpAddress": gs2352PingIpAddress,
       "gs2352PingSize": gs2352PingSize,
       "gs2352DoPingConfig": gs2352DoPingConfig,
       "gs2352PingResult": gs2352PingResult,
       "gs2352Ping6IpAddress": gs2352Ping6IpAddress,
       "gs2352Ping6Size": gs2352Ping6Size,
       "gs2352DoPing6Config": gs2352DoPing6Config,
       "gs2352Ping6Result": gs2352Ping6Result,
       "gs2352VeriPHY": gs2352VeriPHY,
       "gs2352VeriPHYTest": gs2352VeriPHYTest,
       "gs2352VeriPHYTable": gs2352VeriPHYTable,
       "gs2352VeriPHYEntry": gs2352VeriPHYEntry,
       "gs2352VeriPHYPort": gs2352VeriPHYPort,
       "gs2352VeriPHYPairA": gs2352VeriPHYPairA,
       "gs2352VeriPHYLengthA": gs2352VeriPHYLengthA,
       "gs2352VeriPHYPairB": gs2352VeriPHYPairB,
       "gs2352VeriPHYLengthB": gs2352VeriPHYLengthB,
       "gs2352VeriPHYPairC": gs2352VeriPHYPairC,
       "gs2352VeriPHYLengthC": gs2352VeriPHYLengthC,
       "gs2352VeriPHYPairD": gs2352VeriPHYPairD,
       "gs2352VeriPHYLengthD": gs2352VeriPHYLengthD,
       "gs2352ColdRestartDevice": gs2352ColdRestartDevice,
       "gs2352Trap": gs2352Trap,
       "gs2352TrapEvent": gs2352TrapEvent,
       "gs2352Emergency": gs2352Emergency,
       "gs2352Alert": gs2352Alert,
       "gs2352Critical": gs2352Critical,
       "gs2352Error": gs2352Error,
       "gs2352Warning": gs2352Warning,
       "gs2352Notice": gs2352Notice,
       "gs2352Informational": gs2352Informational,
       "gs2352Debug": gs2352Debug,
       "gs2352TrapVariable": gs2352TrapVariable,
       "gs2352Information": gs2352Information}
)
