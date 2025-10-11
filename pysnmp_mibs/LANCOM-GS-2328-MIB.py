# SNMP MIB module (LANCOM-GS-2328-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-GS-2328-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:07 2025
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
_LancomGS2328_ObjectIdentity = ObjectIdentity
lancomGS2328 = _LancomGS2328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330)
)
_Gs2328System_ObjectIdentity = ObjectIdentity
gs2328System = _Gs2328System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1)
)
_Gs2328SystemInformation_ObjectIdentity = ObjectIdentity
gs2328SystemInformation = _Gs2328SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1)
)
_Gs2328ModelName_Type = DisplayString
_Gs2328ModelName_Object = MibScalar
gs2328ModelName = _Gs2328ModelName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 1),
    _Gs2328ModelName_Type()
)
gs2328ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ModelName.setStatus("current")
_Gs2328BIOSVersion_Type = DisplayString
_Gs2328BIOSVersion_Object = MibScalar
gs2328BIOSVersion = _Gs2328BIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 2),
    _Gs2328BIOSVersion_Type()
)
gs2328BIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328BIOSVersion.setStatus("current")
_Gs2328FirmwareVersion_Type = DisplayString
_Gs2328FirmwareVersion_Object = MibScalar
gs2328FirmwareVersion = _Gs2328FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 3),
    _Gs2328FirmwareVersion_Type()
)
gs2328FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FirmwareVersion.setStatus("current")
_Gs2328HardwareMechanicalVersion_Type = DisplayString
_Gs2328HardwareMechanicalVersion_Object = MibScalar
gs2328HardwareMechanicalVersion = _Gs2328HardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 4),
    _Gs2328HardwareMechanicalVersion_Type()
)
gs2328HardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HardwareMechanicalVersion.setStatus("current")
_Gs2328SerialNumber_Type = DisplayString
_Gs2328SerialNumber_Object = MibScalar
gs2328SerialNumber = _Gs2328SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 5),
    _Gs2328SerialNumber_Type()
)
gs2328SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SerialNumber.setStatus("current")
_Gs2328HostMACAddress_Type = MacAddress
_Gs2328HostMACAddress_Object = MibScalar
gs2328HostMACAddress = _Gs2328HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 6),
    _Gs2328HostMACAddress_Type()
)
gs2328HostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HostMACAddress.setStatus("current")
_Gs2328ConsoleBaudrate_Type = DisplayString
_Gs2328ConsoleBaudrate_Object = MibScalar
gs2328ConsoleBaudrate = _Gs2328ConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 7),
    _Gs2328ConsoleBaudrate_Type()
)
gs2328ConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ConsoleBaudrate.setStatus("current")
_Gs2328RAMSize_Type = DisplayString
_Gs2328RAMSize_Object = MibScalar
gs2328RAMSize = _Gs2328RAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 8),
    _Gs2328RAMSize_Type()
)
gs2328RAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RAMSize.setStatus("current")
_Gs2328FlashSize_Type = DisplayString
_Gs2328FlashSize_Object = MibScalar
gs2328FlashSize = _Gs2328FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 9),
    _Gs2328FlashSize_Type()
)
gs2328FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FlashSize.setStatus("current")
_Gs2328BridgeFDBSize_Type = DisplayString
_Gs2328BridgeFDBSize_Object = MibScalar
gs2328BridgeFDBSize = _Gs2328BridgeFDBSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 10),
    _Gs2328BridgeFDBSize_Type()
)
gs2328BridgeFDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328BridgeFDBSize.setStatus("current")
_Gs2328TransmitQueue_Type = DisplayString
_Gs2328TransmitQueue_Object = MibScalar
gs2328TransmitQueue = _Gs2328TransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 11),
    _Gs2328TransmitQueue_Type()
)
gs2328TransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328TransmitQueue.setStatus("current")
_Gs2328MaximumFrameSize_Type = DisplayString
_Gs2328MaximumFrameSize_Object = MibScalar
gs2328MaximumFrameSize = _Gs2328MaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 12),
    _Gs2328MaximumFrameSize_Type()
)
gs2328MaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MaximumFrameSize.setStatus("current")
_Gs2328CPULoad_Type = DisplayString
_Gs2328CPULoad_Object = MibScalar
gs2328CPULoad = _Gs2328CPULoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 13),
    _Gs2328CPULoad_Type()
)
gs2328CPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CPULoad.setStatus("current")
_Gs2328FanSpeed_Type = DisplayString
_Gs2328FanSpeed_Object = MibScalar
gs2328FanSpeed = _Gs2328FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 17),
    _Gs2328FanSpeed_Type()
)
gs2328FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FanSpeed.setStatus("current")
_Gs2328Temperature_Type = DisplayString
_Gs2328Temperature_Object = MibScalar
gs2328Temperature = _Gs2328Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 19),
    _Gs2328Temperature_Type()
)
gs2328Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Temperature.setStatus("current")
_Gs2328SystemDescription_Type = DisplayString
_Gs2328SystemDescription_Object = MibScalar
gs2328SystemDescription = _Gs2328SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 21),
    _Gs2328SystemDescription_Type()
)
gs2328SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SystemDescription.setStatus("current")
_Gs2328Location_Type = DisplayString
_Gs2328Location_Object = MibScalar
gs2328Location = _Gs2328Location_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 22),
    _Gs2328Location_Type()
)
gs2328Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Location.setStatus("current")
_Gs2328Contact_Type = DisplayString
_Gs2328Contact_Object = MibScalar
gs2328Contact = _Gs2328Contact_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 23),
    _Gs2328Contact_Type()
)
gs2328Contact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Contact.setStatus("current")
_Gs2328DeviceName_Type = DisplayString
_Gs2328DeviceName_Object = MibScalar
gs2328DeviceName = _Gs2328DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 24),
    _Gs2328DeviceName_Type()
)
gs2328DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DeviceName.setStatus("current")
_Gs2328SystemDate_Type = DisplayString
_Gs2328SystemDate_Object = MibScalar
gs2328SystemDate = _Gs2328SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 25),
    _Gs2328SystemDate_Type()
)
gs2328SystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SystemDate.setStatus("current")
_Gs2328SystemUptime_Type = DisplayString
_Gs2328SystemUptime_Object = MibScalar
gs2328SystemUptime = _Gs2328SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 26),
    _Gs2328SystemUptime_Type()
)
gs2328SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SystemUptime.setStatus("current")
_Gs2328SystemIPv4Address_Type = DisplayString
_Gs2328SystemIPv4Address_Object = MibScalar
gs2328SystemIPv4Address = _Gs2328SystemIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 27),
    _Gs2328SystemIPv4Address_Type()
)
gs2328SystemIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SystemIPv4Address.setStatus("current")
_Gs2328SystemIPv4SubnetMask_Type = DisplayString
_Gs2328SystemIPv4SubnetMask_Object = MibScalar
gs2328SystemIPv4SubnetMask = _Gs2328SystemIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 28),
    _Gs2328SystemIPv4SubnetMask_Type()
)
gs2328SystemIPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SystemIPv4SubnetMask.setStatus("current")
_Gs2328SystemIPv4Gateway_Type = DisplayString
_Gs2328SystemIPv4Gateway_Object = MibScalar
gs2328SystemIPv4Gateway = _Gs2328SystemIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 29),
    _Gs2328SystemIPv4Gateway_Type()
)
gs2328SystemIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SystemIPv4Gateway.setStatus("current")
_Gs2328IPv6LinkLocalAddress_Type = DisplayString
_Gs2328IPv6LinkLocalAddress_Object = MibScalar
gs2328IPv6LinkLocalAddress = _Gs2328IPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 30),
    _Gs2328IPv6LinkLocalAddress_Type()
)
gs2328IPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv6LinkLocalAddress.setStatus("current")
_Gs2328IPv6Address_Type = DisplayString
_Gs2328IPv6Address_Object = MibScalar
gs2328IPv6Address = _Gs2328IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 31),
    _Gs2328IPv6Address_Type()
)
gs2328IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv6Address.setStatus("current")
_Gs2328IPv6Prefix_Type = DisplayString
_Gs2328IPv6Prefix_Object = MibScalar
gs2328IPv6Prefix = _Gs2328IPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 32),
    _Gs2328IPv6Prefix_Type()
)
gs2328IPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv6Prefix.setStatus("current")
_Gs2328IPv6Gateway_Type = DisplayString
_Gs2328IPv6Gateway_Object = MibScalar
gs2328IPv6Gateway = _Gs2328IPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 33),
    _Gs2328IPv6Gateway_Type()
)
gs2328IPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv6Gateway.setStatus("current")
_Gs2328LargestFreeMemBlock_Type = Integer32
_Gs2328LargestFreeMemBlock_Object = MibScalar
gs2328LargestFreeMemBlock = _Gs2328LargestFreeMemBlock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 1500),
    _Gs2328LargestFreeMemBlock_Type()
)
gs2328LargestFreeMemBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LargestFreeMemBlock.setStatus("current")
_Gs2328MemFree_Type = Integer32
_Gs2328MemFree_Object = MibScalar
gs2328MemFree = _Gs2328MemFree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 1, 1501),
    _Gs2328MemFree_Type()
)
gs2328MemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MemFree.setStatus("current")
_Gs2328SystemTime_ObjectIdentity = ObjectIdentity
gs2328SystemTime = _Gs2328SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2)
)
_Gs2328SystemTimeManual_ObjectIdentity = ObjectIdentity
gs2328SystemTimeManual = _Gs2328SystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1)
)


class _Gs2328SystemTimeManualClockSource_Type(Integer32):
    """Custom type gs2328SystemTimeManualClockSource based on Integer32"""
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


_Gs2328SystemTimeManualClockSource_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualClockSource_Object = MibScalar
gs2328SystemTimeManualClockSource = _Gs2328SystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 1),
    _Gs2328SystemTimeManualClockSource_Type()
)
gs2328SystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualClockSource.setStatus("current")
_Gs2328SystemTimeManualLocaltime_Type = DisplayString
_Gs2328SystemTimeManualLocaltime_Object = MibScalar
gs2328SystemTimeManualLocaltime = _Gs2328SystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 2),
    _Gs2328SystemTimeManualLocaltime_Type()
)
gs2328SystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualLocaltime.setStatus("current")


class _Gs2328SystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type gs2328SystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Gs2328SystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualTimeZoneOffset_Object = MibScalar
gs2328SystemTimeManualTimeZoneOffset = _Gs2328SystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 3),
    _Gs2328SystemTimeManualTimeZoneOffset_Type()
)
gs2328SystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualTimeZoneOffset.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavings based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavings_Object = MibScalar
gs2328SystemTimeManualDaylightSavings = _Gs2328SystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 4),
    _Gs2328SystemTimeManualDaylightSavings_Type()
)
gs2328SystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavings.setStatus("current")


class _Gs2328SystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type gs2328SystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Gs2328SystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualTimeSetOffset_Object = MibScalar
gs2328SystemTimeManualTimeSetOffset = _Gs2328SystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 5),
    _Gs2328SystemTimeManualTimeSetOffset_Type()
)
gs2328SystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualTimeSetOffset.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsType based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsType_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsType = _Gs2328SystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 6),
    _Gs2328SystemTimeManualDaylightSavingsType_Type()
)
gs2328SystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsType.setStatus("current")
_Gs2328SystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Gs2328SystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsBydatesFrom = _Gs2328SystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 7),
    _Gs2328SystemTimeManualDaylightSavingsBydatesFrom_Type()
)
gs2328SystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Gs2328SystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Gs2328SystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsBydatesTo = _Gs2328SystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 8),
    _Gs2328SystemTimeManualDaylightSavingsBydatesTo_Type()
)
gs2328SystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringDayFrom = _Gs2328SystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 9),
    _Gs2328SystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom = _Gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 10),
    _Gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom = _Gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 11),
    _Gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom = _Gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 12),
    _Gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringDayTo = _Gs2328SystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 13),
    _Gs2328SystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringWeekTo = _Gs2328SystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 14),
    _Gs2328SystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Gs2328SystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type gs2328SystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
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


_Gs2328SystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Gs2328SystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringMonthTo = _Gs2328SystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 15),
    _Gs2328SystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Gs2328SystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Gs2328SystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
gs2328SystemTimeManualDaylightSavingsRecurringTimeTo = _Gs2328SystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 1, 16),
    _Gs2328SystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
gs2328SystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Gs2328SystemTimeNTP_ObjectIdentity = ObjectIdentity
gs2328SystemTimeNTP = _Gs2328SystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2)
)
_Gs2328SystemTimeNTPTable_Object = MibTable
gs2328SystemTimeNTPTable = _Gs2328SystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPTable.setStatus("current")
_Gs2328SystemTimeNTPEntry_Object = MibTableRow
gs2328SystemTimeNTPEntry = _Gs2328SystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 1, 1)
)
gs2328SystemTimeNTPEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPEntry.setStatus("current")


class _Gs2328SystemTimeNTPIndex_Type(Integer32):
    """Custom type gs2328SystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328SystemTimeNTPIndex_Type.__name__ = "Integer32"
_Gs2328SystemTimeNTPIndex_Object = MibTableColumn
gs2328SystemTimeNTPIndex = _Gs2328SystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 1, 1, 1),
    _Gs2328SystemTimeNTPIndex_Type()
)
gs2328SystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPIndex.setStatus("current")


class _Gs2328SystemTimeNTPServerIPType_Type(Integer32):
    """Custom type gs2328SystemTimeNTPServerIPType based on Integer32"""
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


_Gs2328SystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Gs2328SystemTimeNTPServerIPType_Object = MibTableColumn
gs2328SystemTimeNTPServerIPType = _Gs2328SystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 1, 1, 2),
    _Gs2328SystemTimeNTPServerIPType_Type()
)
gs2328SystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPServerIPType.setStatus("current")
_Gs2328SystemTimeNTPServer_Type = DisplayString
_Gs2328SystemTimeNTPServer_Object = MibTableColumn
gs2328SystemTimeNTPServer = _Gs2328SystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 1, 1, 3),
    _Gs2328SystemTimeNTPServer_Type()
)
gs2328SystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPServer.setStatus("current")


class _Gs2328SystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type gs2328SystemTimeNTPCurrentMode based on Integer32"""
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


_Gs2328SystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Gs2328SystemTimeNTPCurrentMode_Object = MibTableColumn
gs2328SystemTimeNTPCurrentMode = _Gs2328SystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 1, 1, 4),
    _Gs2328SystemTimeNTPCurrentMode_Type()
)
gs2328SystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPCurrentMode.setStatus("current")


class _Gs2328SystemTimeNTPRequestInterval_Type(Integer32):
    """Custom type gs2328SystemTimeNTPRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 999999999),
    )


_Gs2328SystemTimeNTPRequestInterval_Type.__name__ = "Integer32"
_Gs2328SystemTimeNTPRequestInterval_Object = MibScalar
gs2328SystemTimeNTPRequestInterval = _Gs2328SystemTimeNTPRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 2),
    _Gs2328SystemTimeNTPRequestInterval_Type()
)
gs2328SystemTimeNTPRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPRequestInterval.setStatus("current")


class _Gs2328SystemTimeNTPTriesNumber_Type(Integer32):
    """Custom type gs2328SystemTimeNTPTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_Gs2328SystemTimeNTPTriesNumber_Type.__name__ = "Integer32"
_Gs2328SystemTimeNTPTriesNumber_Object = MibScalar
gs2328SystemTimeNTPTriesNumber = _Gs2328SystemTimeNTPTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 2, 2, 3),
    _Gs2328SystemTimeNTPTriesNumber_Type()
)
gs2328SystemTimeNTPTriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemTimeNTPTriesNumber.setStatus("current")
_Gs2328SystemAccount_ObjectIdentity = ObjectIdentity
gs2328SystemAccount = _Gs2328SystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3)
)
_Gs2328SystemAccountUsers_ObjectIdentity = ObjectIdentity
gs2328SystemAccountUsers = _Gs2328SystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1)
)


class _Gs2328SystemAccountUserCreate_Type(Integer32):
    """Custom type gs2328SystemAccountUserCreate based on Integer32"""
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


_Gs2328SystemAccountUserCreate_Type.__name__ = "Integer32"
_Gs2328SystemAccountUserCreate_Object = MibScalar
gs2328SystemAccountUserCreate = _Gs2328SystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 1),
    _Gs2328SystemAccountUserCreate_Type()
)
gs2328SystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemAccountUserCreate.setStatus("current")
_Gs2328SystemAccountUsersTable_Object = MibTable
gs2328SystemAccountUsersTable = _Gs2328SystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328SystemAccountUsersTable.setStatus("current")
_Gs2328SystemAccountUsersEntry_Object = MibTableRow
gs2328SystemAccountUsersEntry = _Gs2328SystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2, 1)
)
gs2328SystemAccountUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328UserIndex"),
)
if mibBuilder.loadTexts:
    gs2328SystemAccountUsersEntry.setStatus("current")


class _Gs2328UserIndex_Type(Integer32):
    """Custom type gs2328UserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Gs2328UserIndex_Type.__name__ = "Integer32"
_Gs2328UserIndex_Object = MibTableColumn
gs2328UserIndex = _Gs2328UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2, 1, 1),
    _Gs2328UserIndex_Type()
)
gs2328UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328UserIndex.setStatus("current")


class _Gs2328UserName_Type(DisplayString):
    """Custom type gs2328UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328UserName_Type.__name__ = "DisplayString"
_Gs2328UserName_Object = MibTableColumn
gs2328UserName = _Gs2328UserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2, 1, 2),
    _Gs2328UserName_Type()
)
gs2328UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328UserName.setStatus("current")


class _Gs2328Password_Type(DisplayString):
    """Custom type gs2328Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328Password_Type.__name__ = "DisplayString"
_Gs2328Password_Object = MibTableColumn
gs2328Password = _Gs2328Password_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2, 1, 3),
    _Gs2328Password_Type()
)
gs2328Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Password.setStatus("current")


class _Gs2328UserPrivilegeLevel_Type(Integer32):
    """Custom type gs2328UserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328UserPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328UserPrivilegeLevel_Object = MibTableColumn
gs2328UserPrivilegeLevel = _Gs2328UserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2, 1, 4),
    _Gs2328UserPrivilegeLevel_Type()
)
gs2328UserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328UserPrivilegeLevel.setStatus("current")


class _Gs2328AccountUserRowStatus_Type(Integer32):
    """Custom type gs2328AccountUserRowStatus based on Integer32"""
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


_Gs2328AccountUserRowStatus_Type.__name__ = "Integer32"
_Gs2328AccountUserRowStatus_Object = MibTableColumn
gs2328AccountUserRowStatus = _Gs2328AccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 2, 1, 5),
    _Gs2328AccountUserRowStatus_Type()
)
gs2328AccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccountUserRowStatus.setStatus("current")


class _Gs2328SystemAccountUsersSuperUserPassword_Type(OctetString):
    """Custom type gs2328SystemAccountUsersSuperUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2328SystemAccountUsersSuperUserPassword_Type.__name__ = "OctetString"
_Gs2328SystemAccountUsersSuperUserPassword_Object = MibScalar
gs2328SystemAccountUsersSuperUserPassword = _Gs2328SystemAccountUsersSuperUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 1500),
    _Gs2328SystemAccountUsersSuperUserPassword_Type()
)
gs2328SystemAccountUsersSuperUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemAccountUsersSuperUserPassword.setStatus("current")


class _Gs2328SystemAccountEnforcePasswordRules_Type(Integer32):
    """Custom type gs2328SystemAccountEnforcePasswordRules based on Integer32"""
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


_Gs2328SystemAccountEnforcePasswordRules_Type.__name__ = "Integer32"
_Gs2328SystemAccountEnforcePasswordRules_Object = MibScalar
gs2328SystemAccountEnforcePasswordRules = _Gs2328SystemAccountEnforcePasswordRules_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 1, 1501),
    _Gs2328SystemAccountEnforcePasswordRules_Type()
)
gs2328SystemAccountEnforcePasswordRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemAccountEnforcePasswordRules.setStatus("current")
_Gs2328SystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
gs2328SystemAccountPrivilegeLevel = _Gs2328SystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2)
)


class _Gs2328AccountPrivilegeLevel_Type(Integer32):
    """Custom type gs2328AccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328AccountPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328AccountPrivilegeLevel_Object = MibScalar
gs2328AccountPrivilegeLevel = _Gs2328AccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 1),
    _Gs2328AccountPrivilegeLevel_Type()
)
gs2328AccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccountPrivilegeLevel.setStatus("current")


class _Gs2328AggregationPrivilegeLevel_Type(Integer32):
    """Custom type gs2328AggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328AggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328AggregationPrivilegeLevel_Object = MibScalar
gs2328AggregationPrivilegeLevel = _Gs2328AggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 2),
    _Gs2328AggregationPrivilegeLevel_Type()
)
gs2328AggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AggregationPrivilegeLevel.setStatus("current")


class _Gs2328DiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328DiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328DiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328DiagnosticsPrivilegeLevel_Object = MibScalar
gs2328DiagnosticsPrivilegeLevel = _Gs2328DiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 3),
    _Gs2328DiagnosticsPrivilegeLevel_Type()
)
gs2328DiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DiagnosticsPrivilegeLevel.setStatus("current")


class _Gs2328EEEPrivilegeLevel_Type(Integer32):
    """Custom type gs2328EEEPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328EEEPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328EEEPrivilegeLevel_Object = MibScalar
gs2328EEEPrivilegeLevel = _Gs2328EEEPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 4),
    _Gs2328EEEPrivilegeLevel_Type()
)
gs2328EEEPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328EEEPrivilegeLevel.setStatus("current")


class _Gs2328EasyportPrivilegeLevel_Type(Integer32):
    """Custom type gs2328EasyportPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328EasyportPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328EasyportPrivilegeLevel_Object = MibScalar
gs2328EasyportPrivilegeLevel = _Gs2328EasyportPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 9),
    _Gs2328EasyportPrivilegeLevel_Type()
)
gs2328EasyportPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328EasyportPrivilegeLevel.setStatus("current")


class _Gs2328GARPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328GARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328GARPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328GARPPrivilegeLevel_Object = MibScalar
gs2328GARPPrivilegeLevel = _Gs2328GARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 10),
    _Gs2328GARPPrivilegeLevel_Type()
)
gs2328GARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPPrivilegeLevel.setStatus("current")


class _Gs2328GVRPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328GVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328GVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328GVRPPrivilegeLevel_Object = MibScalar
gs2328GVRPPrivilegeLevel = _Gs2328GVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 11),
    _Gs2328GVRPPrivilegeLevel_Type()
)
gs2328GVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GVRPPrivilegeLevel.setStatus("current")


class _Gs2328IPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328IPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328IPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328IPPrivilegeLevel_Object = MibScalar
gs2328IPPrivilegeLevel = _Gs2328IPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 12),
    _Gs2328IPPrivilegeLevel_Type()
)
gs2328IPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPPrivilegeLevel.setStatus("current")


class _Gs2328IPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type gs2328IPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328IPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328IPMCSnoopingPrivilegeLevel_Object = MibScalar
gs2328IPMCSnoopingPrivilegeLevel = _Gs2328IPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 13),
    _Gs2328IPMCSnoopingPrivilegeLevel_Type()
)
gs2328IPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPMCSnoopingPrivilegeLevel.setStatus("current")


class _Gs2328LACPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328LACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328LACPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328LACPPrivilegeLevel_Object = MibScalar
gs2328LACPPrivilegeLevel = _Gs2328LACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 14),
    _Gs2328LACPPrivilegeLevel_Type()
)
gs2328LACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LACPPrivilegeLevel.setStatus("current")


class _Gs2328LLDPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328LLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328LLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328LLDPPrivilegeLevel_Object = MibScalar
gs2328LLDPPrivilegeLevel = _Gs2328LLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 15),
    _Gs2328LLDPPrivilegeLevel_Type()
)
gs2328LLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LLDPPrivilegeLevel.setStatus("current")


class _Gs2328LLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type gs2328LLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328LLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328LLDPMEDPrivilegeLevel_Object = MibScalar
gs2328LLDPMEDPrivilegeLevel = _Gs2328LLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 16),
    _Gs2328LLDPMEDPrivilegeLevel_Type()
)
gs2328LLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LLDPMEDPrivilegeLevel.setStatus("current")


class _Gs2328LoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type gs2328LoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328LoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328LoopProtectPrivilegeLevel_Object = MibScalar
gs2328LoopProtectPrivilegeLevel = _Gs2328LoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 17),
    _Gs2328LoopProtectPrivilegeLevel_Type()
)
gs2328LoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectPrivilegeLevel.setStatus("current")


class _Gs2328MACTablePrivilegeLevel_Type(Integer32):
    """Custom type gs2328MACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328MACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328MACTablePrivilegeLevel_Object = MibScalar
gs2328MACTablePrivilegeLevel = _Gs2328MACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 18),
    _Gs2328MACTablePrivilegeLevel_Type()
)
gs2328MACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACTablePrivilegeLevel.setStatus("current")


class _Gs2328MVRPrivilegeLevel_Type(Integer32):
    """Custom type gs2328MVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328MVRPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328MVRPrivilegeLevel_Object = MibScalar
gs2328MVRPrivilegeLevel = _Gs2328MVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 22),
    _Gs2328MVRPrivilegeLevel_Type()
)
gs2328MVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPrivilegeLevel.setStatus("current")


class _Gs2328MaintenancePrivilegeLevel_Type(Integer32):
    """Custom type gs2328MaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328MaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328MaintenancePrivilegeLevel_Object = MibScalar
gs2328MaintenancePrivilegeLevel = _Gs2328MaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 24),
    _Gs2328MaintenancePrivilegeLevel_Type()
)
gs2328MaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MaintenancePrivilegeLevel.setStatus("current")


class _Gs2328MirroringPrivilegeLevel_Type(Integer32):
    """Custom type gs2328MirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328MirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328MirroringPrivilegeLevel_Object = MibScalar
gs2328MirroringPrivilegeLevel = _Gs2328MirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 25),
    _Gs2328MirroringPrivilegeLevel_Type()
)
gs2328MirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MirroringPrivilegeLevel.setStatus("current")


class _Gs2328PortsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328PortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328PortsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328PortsPrivilegeLevel_Object = MibScalar
gs2328PortsPrivilegeLevel = _Gs2328PortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 27),
    _Gs2328PortsPrivilegeLevel_Type()
)
gs2328PortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortsPrivilegeLevel.setStatus("current")


class _Gs2328PrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328PrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328PrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328PrivateVLANsPrivilegeLevel_Object = MibScalar
gs2328PrivateVLANsPrivilegeLevel = _Gs2328PrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 28),
    _Gs2328PrivateVLANsPrivilegeLevel_Type()
)
gs2328PrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PrivateVLANsPrivilegeLevel.setStatus("current")


class _Gs2328QoSPrivilegeLevel_Type(Integer32):
    """Custom type gs2328QoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328QoSPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328QoSPrivilegeLevel_Object = MibScalar
gs2328QoSPrivilegeLevel = _Gs2328QoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 29),
    _Gs2328QoSPrivilegeLevel_Type()
)
gs2328QoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSPrivilegeLevel.setStatus("current")


class _Gs2328SFlowPrivilegeLevel_Type(Integer32):
    """Custom type gs2328SFlowPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SFlowPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SFlowPrivilegeLevel_Object = MibScalar
gs2328SFlowPrivilegeLevel = _Gs2328SFlowPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 30),
    _Gs2328SFlowPrivilegeLevel_Type()
)
gs2328SFlowPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SFlowPrivilegeLevel.setStatus("current")


class _Gs2328SMTPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328SMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SMTPPrivilegeLevel_Object = MibScalar
gs2328SMTPPrivilegeLevel = _Gs2328SMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 31),
    _Gs2328SMTPPrivilegeLevel_Type()
)
gs2328SMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPPrivilegeLevel.setStatus("current")


class _Gs2328SNMPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328SNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SNMPPrivilegeLevel_Object = MibScalar
gs2328SNMPPrivilegeLevel = _Gs2328SNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 32),
    _Gs2328SNMPPrivilegeLevel_Type()
)
gs2328SNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SNMPPrivilegeLevel.setStatus("current")


class _Gs2328SecurityPrivilegeLevel_Type(Integer32):
    """Custom type gs2328SecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SecurityPrivilegeLevel_Object = MibScalar
gs2328SecurityPrivilegeLevel = _Gs2328SecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 33),
    _Gs2328SecurityPrivilegeLevel_Type()
)
gs2328SecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SecurityPrivilegeLevel.setStatus("current")


class _Gs2328SingleIPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328SingleIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SingleIPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SingleIPPrivilegeLevel_Object = MibScalar
gs2328SingleIPPrivilegeLevel = _Gs2328SingleIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 34),
    _Gs2328SingleIPPrivilegeLevel_Type()
)
gs2328SingleIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SingleIPPrivilegeLevel.setStatus("current")


class _Gs2328SpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type gs2328SpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SpanningTreePrivilegeLevel_Object = MibScalar
gs2328SpanningTreePrivilegeLevel = _Gs2328SpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 35),
    _Gs2328SpanningTreePrivilegeLevel_Type()
)
gs2328SpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SpanningTreePrivilegeLevel.setStatus("current")


class _Gs2328SystemPrivilegeLevel_Type(Integer32):
    """Custom type gs2328SystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328SystemPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328SystemPrivilegeLevel_Object = MibScalar
gs2328SystemPrivilegeLevel = _Gs2328SystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 36),
    _Gs2328SystemPrivilegeLevel_Type()
)
gs2328SystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SystemPrivilegeLevel.setStatus("current")


class _Gs2328TrapEventPrivilegeLevel_Type(Integer32):
    """Custom type gs2328TrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328TrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328TrapEventPrivilegeLevel_Object = MibScalar
gs2328TrapEventPrivilegeLevel = _Gs2328TrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 37),
    _Gs2328TrapEventPrivilegeLevel_Type()
)
gs2328TrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventPrivilegeLevel.setStatus("current")


class _Gs2328UPnPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328UPnPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328UPnPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328UPnPPrivilegeLevel_Object = MibScalar
gs2328UPnPPrivilegeLevel = _Gs2328UPnPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 38),
    _Gs2328UPnPPrivilegeLevel_Type()
)
gs2328UPnPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328UPnPPrivilegeLevel.setStatus("current")


class _Gs2328VCLPrivilegeLevel_Type(Integer32):
    """Custom type gs2328VCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328VCLPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328VCLPrivilegeLevel_Object = MibScalar
gs2328VCLPrivilegeLevel = _Gs2328VCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 39),
    _Gs2328VCLPrivilegeLevel_Type()
)
gs2328VCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VCLPrivilegeLevel.setStatus("current")


class _Gs2328VLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328VLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328VLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328VLANsPrivilegeLevel_Object = MibScalar
gs2328VLANsPrivilegeLevel = _Gs2328VLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 41),
    _Gs2328VLANsPrivilegeLevel_Type()
)
gs2328VLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VLANsPrivilegeLevel.setStatus("current")


class _Gs2328VoiceVLANPrivilegeLevel_Type(Integer32):
    """Custom type gs2328VoiceVLANPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328VoiceVLANPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328VoiceVLANPrivilegeLevel_Object = MibScalar
gs2328VoiceVLANPrivilegeLevel = _Gs2328VoiceVLANPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 3, 2, 42),
    _Gs2328VoiceVLANPrivilegeLevel_Type()
)
gs2328VoiceVLANPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANPrivilegeLevel.setStatus("current")
_Gs2328IP_ObjectIdentity = ObjectIdentity
gs2328IP = _Gs2328IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4)
)
_Gs2328IPv4_ObjectIdentity = ObjectIdentity
gs2328IPv4 = _Gs2328IPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1)
)
_Gs2328IPv4Configured_ObjectIdentity = ObjectIdentity
gs2328IPv4Configured = _Gs2328IPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1)
)


class _Gs2328Ipv4DHCPClient_Type(Integer32):
    """Custom type gs2328Ipv4DHCPClient based on Integer32"""
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


_Gs2328Ipv4DHCPClient_Type.__name__ = "Integer32"
_Gs2328Ipv4DHCPClient_Object = MibScalar
gs2328Ipv4DHCPClient = _Gs2328Ipv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 1),
    _Gs2328Ipv4DHCPClient_Type()
)
gs2328Ipv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ipv4DHCPClient.setStatus("current")
_Gs2328IPv4Address_Type = IpAddress
_Gs2328IPv4Address_Object = MibScalar
gs2328IPv4Address = _Gs2328IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 2),
    _Gs2328IPv4Address_Type()
)
gs2328IPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPv4Address.setStatus("current")
_Gs2328IPv4Mask_Type = IpAddress
_Gs2328IPv4Mask_Object = MibScalar
gs2328IPv4Mask = _Gs2328IPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 3),
    _Gs2328IPv4Mask_Type()
)
gs2328IPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPv4Mask.setStatus("current")
_Gs2328IPv4Gateway_Type = IpAddress
_Gs2328IPv4Gateway_Object = MibScalar
gs2328IPv4Gateway = _Gs2328IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 4),
    _Gs2328IPv4Gateway_Type()
)
gs2328IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPv4Gateway.setStatus("current")


class _Gs2328IPv4VLANId_Type(Integer32):
    """Custom type gs2328IPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328IPv4VLANId_Type.__name__ = "Integer32"
_Gs2328IPv4VLANId_Object = MibScalar
gs2328IPv4VLANId = _Gs2328IPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 5),
    _Gs2328IPv4VLANId_Type()
)
gs2328IPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPv4VLANId.setStatus("current")
_Gs2328IPv4DNSServer_Type = IpAddress
_Gs2328IPv4DNSServer_Object = MibScalar
gs2328IPv4DNSServer = _Gs2328IPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 6),
    _Gs2328IPv4DNSServer_Type()
)
gs2328IPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPv4DNSServer.setStatus("current")


class _Gs2328IPv4DNSProxy_Type(Integer32):
    """Custom type gs2328IPv4DNSProxy based on Integer32"""
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


_Gs2328IPv4DNSProxy_Type.__name__ = "Integer32"
_Gs2328IPv4DNSProxy_Object = MibScalar
gs2328IPv4DNSProxy = _Gs2328IPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 1, 7),
    _Gs2328IPv4DNSProxy_Type()
)
gs2328IPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPv4DNSProxy.setStatus("current")
_Gs2328IPv4Current_ObjectIdentity = ObjectIdentity
gs2328IPv4Current = _Gs2328IPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2)
)


class _Gs2328Ipv4CurrentDHCPClient_Type(Integer32):
    """Custom type gs2328Ipv4CurrentDHCPClient based on Integer32"""
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


_Gs2328Ipv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Gs2328Ipv4CurrentDHCPClient_Object = MibScalar
gs2328Ipv4CurrentDHCPClient = _Gs2328Ipv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2, 1),
    _Gs2328Ipv4CurrentDHCPClient_Type()
)
gs2328Ipv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ipv4CurrentDHCPClient.setStatus("current")
_Gs2328IPv4CurrentAddress_Type = IpAddress
_Gs2328IPv4CurrentAddress_Object = MibScalar
gs2328IPv4CurrentAddress = _Gs2328IPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2, 2),
    _Gs2328IPv4CurrentAddress_Type()
)
gs2328IPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv4CurrentAddress.setStatus("current")
_Gs2328IPv4CurrentMask_Type = IpAddress
_Gs2328IPv4CurrentMask_Object = MibScalar
gs2328IPv4CurrentMask = _Gs2328IPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2, 3),
    _Gs2328IPv4CurrentMask_Type()
)
gs2328IPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv4CurrentMask.setStatus("current")
_Gs2328IPv4CurrentGateway_Type = IpAddress
_Gs2328IPv4CurrentGateway_Object = MibScalar
gs2328IPv4CurrentGateway = _Gs2328IPv4CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2, 4),
    _Gs2328IPv4CurrentGateway_Type()
)
gs2328IPv4CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv4CurrentGateway.setStatus("current")


class _Gs2328IPv4CurrentVLANId_Type(Integer32):
    """Custom type gs2328IPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328IPv4CurrentVLANId_Type.__name__ = "Integer32"
_Gs2328IPv4CurrentVLANId_Object = MibScalar
gs2328IPv4CurrentVLANId = _Gs2328IPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2, 5),
    _Gs2328IPv4CurrentVLANId_Type()
)
gs2328IPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv4CurrentVLANId.setStatus("current")
_Gs2328IPv4CurrentDNSServer_Type = IpAddress
_Gs2328IPv4CurrentDNSServer_Object = MibScalar
gs2328IPv4CurrentDNSServer = _Gs2328IPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 1, 2, 6),
    _Gs2328IPv4CurrentDNSServer_Type()
)
gs2328IPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPv4CurrentDNSServer.setStatus("current")
_Gs2328IPv6_ObjectIdentity = ObjectIdentity
gs2328IPv6 = _Gs2328IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2)
)
_Gs2328IPv6Configured_ObjectIdentity = ObjectIdentity
gs2328IPv6Configured = _Gs2328IPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 1)
)


class _Gs2328Ipv6AutoConfiguration_Type(Integer32):
    """Custom type gs2328Ipv6AutoConfiguration based on Integer32"""
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


_Gs2328Ipv6AutoConfiguration_Type.__name__ = "Integer32"
_Gs2328Ipv6AutoConfiguration_Object = MibScalar
gs2328Ipv6AutoConfiguration = _Gs2328Ipv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 1, 1),
    _Gs2328Ipv6AutoConfiguration_Type()
)
gs2328Ipv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ipv6AutoConfiguration.setStatus("current")


class _Gs2328Ipv6Address_Type(DisplayString):
    """Custom type gs2328Ipv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328Ipv6Address_Type.__name__ = "DisplayString"
_Gs2328Ipv6Address_Object = MibScalar
gs2328Ipv6Address = _Gs2328Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 1, 2),
    _Gs2328Ipv6Address_Type()
)
gs2328Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ipv6Address.setStatus("current")


class _Gs2328Ipv6Prefix_Type(Integer32):
    """Custom type gs2328Ipv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2328Ipv6Prefix_Type.__name__ = "Integer32"
_Gs2328Ipv6Prefix_Object = MibScalar
gs2328Ipv6Prefix = _Gs2328Ipv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 1, 3),
    _Gs2328Ipv6Prefix_Type()
)
gs2328Ipv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ipv6Prefix.setStatus("current")


class _Gs2328Ipv6Gateway_Type(DisplayString):
    """Custom type gs2328Ipv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328Ipv6Gateway_Type.__name__ = "DisplayString"
_Gs2328Ipv6Gateway_Object = MibScalar
gs2328Ipv6Gateway = _Gs2328Ipv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 1, 4),
    _Gs2328Ipv6Gateway_Type()
)
gs2328Ipv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ipv6Gateway.setStatus("current")
_Gs2328IPv6Current_ObjectIdentity = ObjectIdentity
gs2328IPv6Current = _Gs2328IPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 2)
)


class _Gs2328Ipv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type gs2328Ipv6CurrentAutoConfiguration based on Integer32"""
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


_Gs2328Ipv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Gs2328Ipv6CurrentAutoConfiguration_Object = MibScalar
gs2328Ipv6CurrentAutoConfiguration = _Gs2328Ipv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 2, 1),
    _Gs2328Ipv6CurrentAutoConfiguration_Type()
)
gs2328Ipv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Ipv6CurrentAutoConfiguration.setStatus("current")


class _Gs2328Ipv6CurrentAddress_Type(DisplayString):
    """Custom type gs2328Ipv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328Ipv6CurrentAddress_Type.__name__ = "DisplayString"
_Gs2328Ipv6CurrentAddress_Object = MibScalar
gs2328Ipv6CurrentAddress = _Gs2328Ipv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 2, 2),
    _Gs2328Ipv6CurrentAddress_Type()
)
gs2328Ipv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Ipv6CurrentAddress.setStatus("current")


class _Gs2328Ipv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type gs2328Ipv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328Ipv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Gs2328Ipv6CurrentLinkLocalAddress_Object = MibScalar
gs2328Ipv6CurrentLinkLocalAddress = _Gs2328Ipv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 2, 3),
    _Gs2328Ipv6CurrentLinkLocalAddress_Type()
)
gs2328Ipv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Ipv6CurrentLinkLocalAddress.setStatus("current")


class _Gs2328Ipv6CurrentPrefix_Type(DisplayString):
    """Custom type gs2328Ipv6CurrentPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Gs2328Ipv6CurrentPrefix_Type.__name__ = "DisplayString"
_Gs2328Ipv6CurrentPrefix_Object = MibScalar
gs2328Ipv6CurrentPrefix = _Gs2328Ipv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 2, 4),
    _Gs2328Ipv6CurrentPrefix_Type()
)
gs2328Ipv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Ipv6CurrentPrefix.setStatus("current")


class _Gs2328Ipv6CurrentGateway_Type(DisplayString):
    """Custom type gs2328Ipv6CurrentGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328Ipv6CurrentGateway_Type.__name__ = "DisplayString"
_Gs2328Ipv6CurrentGateway_Object = MibScalar
gs2328Ipv6CurrentGateway = _Gs2328Ipv6CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 4, 2, 2, 5),
    _Gs2328Ipv6CurrentGateway_Type()
)
gs2328Ipv6CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Ipv6CurrentGateway.setStatus("current")
_Gs2328Syslog_ObjectIdentity = ObjectIdentity
gs2328Syslog = _Gs2328Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5)
)
_Gs2328SyslogConf_ObjectIdentity = ObjectIdentity
gs2328SyslogConf = _Gs2328SyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 1)
)


class _Gs2328ServerMode_Type(Integer32):
    """Custom type gs2328ServerMode based on Integer32"""
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


_Gs2328ServerMode_Type.__name__ = "Integer32"
_Gs2328ServerMode_Object = MibScalar
gs2328ServerMode = _Gs2328ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 1, 1),
    _Gs2328ServerMode_Type()
)
gs2328ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ServerMode.setStatus("current")
_Gs2328ServerAddress1_Type = IpAddress
_Gs2328ServerAddress1_Object = MibScalar
gs2328ServerAddress1 = _Gs2328ServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 1, 2),
    _Gs2328ServerAddress1_Type()
)
gs2328ServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ServerAddress1.setStatus("current")
_Gs2328ServerAddress2_Type = IpAddress
_Gs2328ServerAddress2_Object = MibScalar
gs2328ServerAddress2 = _Gs2328ServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 1, 3),
    _Gs2328ServerAddress2_Type()
)
gs2328ServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ServerAddress2.setStatus("current")


class _Gs2328SyslogLevel_Type(Integer32):
    """Custom type gs2328SyslogLevel based on Integer32"""
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


_Gs2328SyslogLevel_Type.__name__ = "Integer32"
_Gs2328SyslogLevel_Object = MibScalar
gs2328SyslogLevel = _Gs2328SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 1, 4),
    _Gs2328SyslogLevel_Type()
)
gs2328SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SyslogLevel.setStatus("current")
_Gs2328SyslogDetailedInfo_ObjectIdentity = ObjectIdentity
gs2328SyslogDetailedInfo = _Gs2328SyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2)
)


class _Gs2328SyslogDetailedInfoClear_Type(Integer32):
    """Custom type gs2328SyslogDetailedInfoClear based on Integer32"""
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


_Gs2328SyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Gs2328SyslogDetailedInfoClear_Object = MibScalar
gs2328SyslogDetailedInfoClear = _Gs2328SyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 1),
    _Gs2328SyslogDetailedInfoClear_Type()
)
gs2328SyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoClear.setStatus("current")
_Gs2328SyslogDetailedInfoTable_Object = MibTable
gs2328SyslogDetailedInfoTable = _Gs2328SyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoTable.setStatus("current")
_Gs2328SyslogDetailedInfoEntry_Object = MibTableRow
gs2328SyslogDetailedInfoEntry = _Gs2328SyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 2, 1)
)
gs2328SyslogDetailedInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoEntry.setStatus("current")


class _Gs2328SyslogDetailedInfoIndex_Type(Integer32):
    """Custom type gs2328SyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2328SyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Gs2328SyslogDetailedInfoIndex_Object = MibTableColumn
gs2328SyslogDetailedInfoIndex = _Gs2328SyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 2, 1, 1),
    _Gs2328SyslogDetailedInfoIndex_Type()
)
gs2328SyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoIndex.setStatus("current")
_Gs2328SyslogDetailedInfoLevel_Type = DisplayString
_Gs2328SyslogDetailedInfoLevel_Object = MibTableColumn
gs2328SyslogDetailedInfoLevel = _Gs2328SyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 2, 1, 2),
    _Gs2328SyslogDetailedInfoLevel_Type()
)
gs2328SyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoLevel.setStatus("current")


class _Gs2328SyslogDetailedInfoTime_Type(DisplayString):
    """Custom type gs2328SyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gs2328SyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Gs2328SyslogDetailedInfoTime_Object = MibTableColumn
gs2328SyslogDetailedInfoTime = _Gs2328SyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 2, 1, 3),
    _Gs2328SyslogDetailedInfoTime_Type()
)
gs2328SyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoTime.setStatus("current")
_Gs2328SyslogDetailedInfoMessage_Type = DisplayString
_Gs2328SyslogDetailedInfoMessage_Object = MibTableColumn
gs2328SyslogDetailedInfoMessage = _Gs2328SyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 5, 2, 2, 1, 4),
    _Gs2328SyslogDetailedInfoMessage_Type()
)
gs2328SyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SyslogDetailedInfoMessage.setStatus("current")
_Gs2328Snmp_ObjectIdentity = ObjectIdentity
gs2328Snmp = _Gs2328Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6)
)
_Gs2328SnmpConf_ObjectIdentity = ObjectIdentity
gs2328SnmpConf = _Gs2328SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1)
)


class _Gs2328GetCommunityMode_Type(Integer32):
    """Custom type gs2328GetCommunityMode based on Integer32"""
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


_Gs2328GetCommunityMode_Type.__name__ = "Integer32"
_Gs2328GetCommunityMode_Object = MibScalar
gs2328GetCommunityMode = _Gs2328GetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 1),
    _Gs2328GetCommunityMode_Type()
)
gs2328GetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GetCommunityMode.setStatus("current")
_Gs2328GetCommunity_Type = DisplayString
_Gs2328GetCommunity_Object = MibScalar
gs2328GetCommunity = _Gs2328GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 2),
    _Gs2328GetCommunity_Type()
)
gs2328GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GetCommunity.setStatus("current")


class _Gs2328SetCommunityMode_Type(Integer32):
    """Custom type gs2328SetCommunityMode based on Integer32"""
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


_Gs2328SetCommunityMode_Type.__name__ = "Integer32"
_Gs2328SetCommunityMode_Object = MibScalar
gs2328SetCommunityMode = _Gs2328SetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 3),
    _Gs2328SetCommunityMode_Type()
)
gs2328SetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SetCommunityMode.setStatus("current")
_Gs2328SetCommunity_Type = DisplayString
_Gs2328SetCommunity_Object = MibScalar
gs2328SetCommunity = _Gs2328SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 4),
    _Gs2328SetCommunity_Type()
)
gs2328SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SetCommunity.setStatus("current")
_Gs2328GetCommunityConfTable_Object = MibTable
gs2328GetCommunityConfTable = _Gs2328GetCommunityConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    gs2328GetCommunityConfTable.setStatus("current")
_Gs2328GetCommunityConfEntry_Object = MibTableRow
gs2328GetCommunityConfEntry = _Gs2328GetCommunityConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 5, 1)
)
gs2328GetCommunityConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328CommunityConfIndex"),
)
if mibBuilder.loadTexts:
    gs2328GetCommunityConfEntry.setStatus("current")


class _Gs2328CommunityConfIndex_Type(Integer32):
    """Custom type gs2328CommunityConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328CommunityConfIndex_Type.__name__ = "Integer32"
_Gs2328CommunityConfIndex_Object = MibTableColumn
gs2328CommunityConfIndex = _Gs2328CommunityConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 5, 1, 1),
    _Gs2328CommunityConfIndex_Type()
)
gs2328CommunityConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328CommunityConfIndex.setStatus("current")
_Gs2328CommunityConfGetCommunity_Type = DisplayString
_Gs2328CommunityConfGetCommunity_Object = MibTableColumn
gs2328CommunityConfGetCommunity = _Gs2328CommunityConfGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 5, 1, 2),
    _Gs2328CommunityConfGetCommunity_Type()
)
gs2328CommunityConfGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328CommunityConfGetCommunity.setStatus("current")
_Gs2328TrapHostConfTable_Object = MibTable
gs2328TrapHostConfTable = _Gs2328TrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    gs2328TrapHostConfTable.setStatus("current")
_Gs2328TrapHostConfEntry_Object = MibTableRow
gs2328TrapHostConfEntry = _Gs2328TrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1)
)
gs2328TrapHostConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328TrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    gs2328TrapHostConfEntry.setStatus("current")


class _Gs2328TrapHostConfIndex_Type(Integer32):
    """Custom type gs2328TrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2328TrapHostConfIndex_Type.__name__ = "Integer32"
_Gs2328TrapHostConfIndex_Object = MibTableColumn
gs2328TrapHostConfIndex = _Gs2328TrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 1),
    _Gs2328TrapHostConfIndex_Type()
)
gs2328TrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328TrapHostConfIndex.setStatus("current")


class _Gs2328TrapHostConfVersion_Type(Integer32):
    """Custom type gs2328TrapHostConfVersion based on Integer32"""
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


_Gs2328TrapHostConfVersion_Type.__name__ = "Integer32"
_Gs2328TrapHostConfVersion_Object = MibTableColumn
gs2328TrapHostConfVersion = _Gs2328TrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 2),
    _Gs2328TrapHostConfVersion_Type()
)
gs2328TrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfVersion.setStatus("current")


class _Gs2328TrapHostConfIPType_Type(Integer32):
    """Custom type gs2328TrapHostConfIPType based on Integer32"""
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


_Gs2328TrapHostConfIPType_Type.__name__ = "Integer32"
_Gs2328TrapHostConfIPType_Object = MibTableColumn
gs2328TrapHostConfIPType = _Gs2328TrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 3),
    _Gs2328TrapHostConfIPType_Type()
)
gs2328TrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfIPType.setStatus("current")
_Gs2328TrapHostConfIP_Type = DisplayString
_Gs2328TrapHostConfIP_Object = MibTableColumn
gs2328TrapHostConfIP = _Gs2328TrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 4),
    _Gs2328TrapHostConfIP_Type()
)
gs2328TrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfIP.setStatus("current")


class _Gs2328TrapHostConfPort_Type(Integer32):
    """Custom type gs2328TrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328TrapHostConfPort_Type.__name__ = "Integer32"
_Gs2328TrapHostConfPort_Object = MibTableColumn
gs2328TrapHostConfPort = _Gs2328TrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 5),
    _Gs2328TrapHostConfPort_Type()
)
gs2328TrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfPort.setStatus("current")


class _Gs2328TrapHostConfCommunity_Type(DisplayString):
    """Custom type gs2328TrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328TrapHostConfCommunity_Type.__name__ = "DisplayString"
_Gs2328TrapHostConfCommunity_Object = MibTableColumn
gs2328TrapHostConfCommunity = _Gs2328TrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 6),
    _Gs2328TrapHostConfCommunity_Type()
)
gs2328TrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfCommunity.setStatus("current")


class _Gs2328TrapHostConfSeverityLevel_Type(Integer32):
    """Custom type gs2328TrapHostConfSeverityLevel based on Integer32"""
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


_Gs2328TrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Gs2328TrapHostConfSeverityLevel_Object = MibTableColumn
gs2328TrapHostConfSeverityLevel = _Gs2328TrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 7),
    _Gs2328TrapHostConfSeverityLevel_Type()
)
gs2328TrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfSeverityLevel.setStatus("current")


class _Gs2328TrapHostConfSecurityLevel_Type(Integer32):
    """Custom type gs2328TrapHostConfSecurityLevel based on Integer32"""
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


_Gs2328TrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Gs2328TrapHostConfSecurityLevel_Object = MibTableColumn
gs2328TrapHostConfSecurityLevel = _Gs2328TrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 8),
    _Gs2328TrapHostConfSecurityLevel_Type()
)
gs2328TrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfSecurityLevel.setStatus("current")


class _Gs2328TrapHostConfAuthPtc_Type(Integer32):
    """Custom type gs2328TrapHostConfAuthPtc based on Integer32"""
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


_Gs2328TrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Gs2328TrapHostConfAuthPtc_Object = MibTableColumn
gs2328TrapHostConfAuthPtc = _Gs2328TrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 9),
    _Gs2328TrapHostConfAuthPtc_Type()
)
gs2328TrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfAuthPtc.setStatus("current")
_Gs2328TrapHostConfAuthPassword_Type = DisplayString
_Gs2328TrapHostConfAuthPassword_Object = MibTableColumn
gs2328TrapHostConfAuthPassword = _Gs2328TrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 10),
    _Gs2328TrapHostConfAuthPassword_Type()
)
gs2328TrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfAuthPassword.setStatus("current")


class _Gs2328TrapHostConfPrivPtc_Type(Integer32):
    """Custom type gs2328TrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("des", 1)
    )


_Gs2328TrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Gs2328TrapHostConfPrivPtc_Object = MibTableColumn
gs2328TrapHostConfPrivPtc = _Gs2328TrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 11),
    _Gs2328TrapHostConfPrivPtc_Type()
)
gs2328TrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfPrivPtc.setStatus("current")
_Gs2328TrapHostConfPrivPassword_Type = DisplayString
_Gs2328TrapHostConfPrivPassword_Object = MibTableColumn
gs2328TrapHostConfPrivPassword = _Gs2328TrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 12),
    _Gs2328TrapHostConfPrivPassword_Type()
)
gs2328TrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfPrivPassword.setStatus("current")


class _Gs2328TrapHostConfCurrentMode_Type(Integer32):
    """Custom type gs2328TrapHostConfCurrentMode based on Integer32"""
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


_Gs2328TrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Gs2328TrapHostConfCurrentMode_Object = MibTableColumn
gs2328TrapHostConfCurrentMode = _Gs2328TrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 1, 6, 1, 13),
    _Gs2328TrapHostConfCurrentMode_Type()
)
gs2328TrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapHostConfCurrentMode.setStatus("current")
_Gs2328SnmpSystem_ObjectIdentity = ObjectIdentity
gs2328SnmpSystem = _Gs2328SnmpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 2)
)


class _Gs2328SnmpState_Type(Integer32):
    """Custom type gs2328SnmpState based on Integer32"""
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


_Gs2328SnmpState_Type.__name__ = "Integer32"
_Gs2328SnmpState_Object = MibScalar
gs2328SnmpState = _Gs2328SnmpState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 2, 1),
    _Gs2328SnmpState_Type()
)
gs2328SnmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpState.setStatus("current")


class _Gs2328SnmpEngineID_Type(OctetString):
    """Custom type gs2328SnmpEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Gs2328SnmpEngineID_Type.__name__ = "OctetString"
_Gs2328SnmpEngineID_Object = MibScalar
gs2328SnmpEngineID = _Gs2328SnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 2, 2),
    _Gs2328SnmpEngineID_Type()
)
gs2328SnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpEngineID.setStatus("current")
_Gs2328SnmpCommunities_ObjectIdentity = ObjectIdentity
gs2328SnmpCommunities = _Gs2328SnmpCommunities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3)
)


class _Gs2328SnmpCommunitiesCreate_Type(Integer32):
    """Custom type gs2328SnmpCommunitiesCreate based on Integer32"""
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


_Gs2328SnmpCommunitiesCreate_Type.__name__ = "Integer32"
_Gs2328SnmpCommunitiesCreate_Object = MibScalar
gs2328SnmpCommunitiesCreate = _Gs2328SnmpCommunitiesCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 1),
    _Gs2328SnmpCommunitiesCreate_Type()
)
gs2328SnmpCommunitiesCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesCreate.setStatus("current")
_Gs2328SnmpCommunitiesTable_Object = MibTable
gs2328SnmpCommunitiesTable = _Gs2328SnmpCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesTable.setStatus("current")
_Gs2328SnmpCommunitiesEntry_Object = MibTableRow
gs2328SnmpCommunitiesEntry = _Gs2328SnmpCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1)
)
gs2328SnmpCommunitiesEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SnmpCommunitiesIndex"),
)
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesEntry.setStatus("current")


class _Gs2328SnmpCommunitiesIndex_Type(Integer32):
    """Custom type gs2328SnmpCommunitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2328SnmpCommunitiesIndex_Type.__name__ = "Integer32"
_Gs2328SnmpCommunitiesIndex_Object = MibTableColumn
gs2328SnmpCommunitiesIndex = _Gs2328SnmpCommunitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1, 1),
    _Gs2328SnmpCommunitiesIndex_Type()
)
gs2328SnmpCommunitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesIndex.setStatus("current")


class _Gs2328SnmpCommunitiesCommunity_Type(DisplayString):
    """Custom type gs2328SnmpCommunitiesCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpCommunitiesCommunity_Type.__name__ = "DisplayString"
_Gs2328SnmpCommunitiesCommunity_Object = MibTableColumn
gs2328SnmpCommunitiesCommunity = _Gs2328SnmpCommunitiesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1, 2),
    _Gs2328SnmpCommunitiesCommunity_Type()
)
gs2328SnmpCommunitiesCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesCommunity.setStatus("current")


class _Gs2328SnmpCommunitiesUserName_Type(DisplayString):
    """Custom type gs2328SnmpCommunitiesUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpCommunitiesUserName_Type.__name__ = "DisplayString"
_Gs2328SnmpCommunitiesUserName_Object = MibTableColumn
gs2328SnmpCommunitiesUserName = _Gs2328SnmpCommunitiesUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1, 3),
    _Gs2328SnmpCommunitiesUserName_Type()
)
gs2328SnmpCommunitiesUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesUserName.setStatus("current")
_Gs2328SnmpCommunitiesSourceIP_Type = IpAddress
_Gs2328SnmpCommunitiesSourceIP_Object = MibTableColumn
gs2328SnmpCommunitiesSourceIP = _Gs2328SnmpCommunitiesSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1, 4),
    _Gs2328SnmpCommunitiesSourceIP_Type()
)
gs2328SnmpCommunitiesSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesSourceIP.setStatus("current")
_Gs2328SnmpCommunitiesSourceMask_Type = IpAddress
_Gs2328SnmpCommunitiesSourceMask_Object = MibTableColumn
gs2328SnmpCommunitiesSourceMask = _Gs2328SnmpCommunitiesSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1, 5),
    _Gs2328SnmpCommunitiesSourceMask_Type()
)
gs2328SnmpCommunitiesSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesSourceMask.setStatus("current")


class _Gs2328SnmpCommunitiesRowStatus_Type(Integer32):
    """Custom type gs2328SnmpCommunitiesRowStatus based on Integer32"""
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


_Gs2328SnmpCommunitiesRowStatus_Type.__name__ = "Integer32"
_Gs2328SnmpCommunitiesRowStatus_Object = MibTableColumn
gs2328SnmpCommunitiesRowStatus = _Gs2328SnmpCommunitiesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 3, 2, 1, 6),
    _Gs2328SnmpCommunitiesRowStatus_Type()
)
gs2328SnmpCommunitiesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpCommunitiesRowStatus.setStatus("current")
_Gs2328SnmpUsers_ObjectIdentity = ObjectIdentity
gs2328SnmpUsers = _Gs2328SnmpUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4)
)


class _Gs2328SnmpUsersCreate_Type(Integer32):
    """Custom type gs2328SnmpUsersCreate based on Integer32"""
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


_Gs2328SnmpUsersCreate_Type.__name__ = "Integer32"
_Gs2328SnmpUsersCreate_Object = MibScalar
gs2328SnmpUsersCreate = _Gs2328SnmpUsersCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 1),
    _Gs2328SnmpUsersCreate_Type()
)
gs2328SnmpUsersCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersCreate.setStatus("current")
_Gs2328SnmpUsersTable_Object = MibTable
gs2328SnmpUsersTable = _Gs2328SnmpUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328SnmpUsersTable.setStatus("current")
_Gs2328SnmpUsersEntry_Object = MibTableRow
gs2328SnmpUsersEntry = _Gs2328SnmpUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1)
)
gs2328SnmpUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SnmpUsersIndex"),
)
if mibBuilder.loadTexts:
    gs2328SnmpUsersEntry.setStatus("current")


class _Gs2328SnmpUsersIndex_Type(Integer32):
    """Custom type gs2328SnmpUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328SnmpUsersIndex_Type.__name__ = "Integer32"
_Gs2328SnmpUsersIndex_Object = MibTableColumn
gs2328SnmpUsersIndex = _Gs2328SnmpUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 1),
    _Gs2328SnmpUsersIndex_Type()
)
gs2328SnmpUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SnmpUsersIndex.setStatus("current")


class _Gs2328SnmpUsersUserName_Type(DisplayString):
    """Custom type gs2328SnmpUsersUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpUsersUserName_Type.__name__ = "DisplayString"
_Gs2328SnmpUsersUserName_Object = MibTableColumn
gs2328SnmpUsersUserName = _Gs2328SnmpUsersUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 2),
    _Gs2328SnmpUsersUserName_Type()
)
gs2328SnmpUsersUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersUserName.setStatus("current")


class _Gs2328SnmpUsersSecurityLevel_Type(Integer32):
    """Custom type gs2328SnmpUsersSecurityLevel based on Integer32"""
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


_Gs2328SnmpUsersSecurityLevel_Type.__name__ = "Integer32"
_Gs2328SnmpUsersSecurityLevel_Object = MibTableColumn
gs2328SnmpUsersSecurityLevel = _Gs2328SnmpUsersSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 3),
    _Gs2328SnmpUsersSecurityLevel_Type()
)
gs2328SnmpUsersSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersSecurityLevel.setStatus("current")


class _Gs2328SnmpUsersAuthenticationProtocol_Type(Integer32):
    """Custom type gs2328SnmpUsersAuthenticationProtocol based on Integer32"""
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


_Gs2328SnmpUsersAuthenticationProtocol_Type.__name__ = "Integer32"
_Gs2328SnmpUsersAuthenticationProtocol_Object = MibTableColumn
gs2328SnmpUsersAuthenticationProtocol = _Gs2328SnmpUsersAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 4),
    _Gs2328SnmpUsersAuthenticationProtocol_Type()
)
gs2328SnmpUsersAuthenticationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersAuthenticationProtocol.setStatus("current")
_Gs2328SnmpUsersAuthenticationPassword_Type = DisplayString
_Gs2328SnmpUsersAuthenticationPassword_Object = MibTableColumn
gs2328SnmpUsersAuthenticationPassword = _Gs2328SnmpUsersAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 5),
    _Gs2328SnmpUsersAuthenticationPassword_Type()
)
gs2328SnmpUsersAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersAuthenticationPassword.setStatus("current")


class _Gs2328SnmpUsersPrivacyProtocol_Type(Integer32):
    """Custom type gs2328SnmpUsersPrivacyProtocol based on Integer32"""
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


_Gs2328SnmpUsersPrivacyProtocol_Type.__name__ = "Integer32"
_Gs2328SnmpUsersPrivacyProtocol_Object = MibTableColumn
gs2328SnmpUsersPrivacyProtocol = _Gs2328SnmpUsersPrivacyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 6),
    _Gs2328SnmpUsersPrivacyProtocol_Type()
)
gs2328SnmpUsersPrivacyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersPrivacyProtocol.setStatus("current")
_Gs2328SnmpUsersPrivacyPassword_Type = DisplayString
_Gs2328SnmpUsersPrivacyPassword_Object = MibTableColumn
gs2328SnmpUsersPrivacyPassword = _Gs2328SnmpUsersPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 7),
    _Gs2328SnmpUsersPrivacyPassword_Type()
)
gs2328SnmpUsersPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersPrivacyPassword.setStatus("current")


class _Gs2328SnmpUsersRowStatus_Type(Integer32):
    """Custom type gs2328SnmpUsersRowStatus based on Integer32"""
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


_Gs2328SnmpUsersRowStatus_Type.__name__ = "Integer32"
_Gs2328SnmpUsersRowStatus_Object = MibTableColumn
gs2328SnmpUsersRowStatus = _Gs2328SnmpUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 4, 2, 1, 8),
    _Gs2328SnmpUsersRowStatus_Type()
)
gs2328SnmpUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpUsersRowStatus.setStatus("current")
_Gs2328SnmpGroups_ObjectIdentity = ObjectIdentity
gs2328SnmpGroups = _Gs2328SnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5)
)


class _Gs2328SnmpGroupsCreate_Type(Integer32):
    """Custom type gs2328SnmpGroupsCreate based on Integer32"""
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


_Gs2328SnmpGroupsCreate_Type.__name__ = "Integer32"
_Gs2328SnmpGroupsCreate_Object = MibScalar
gs2328SnmpGroupsCreate = _Gs2328SnmpGroupsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 1),
    _Gs2328SnmpGroupsCreate_Type()
)
gs2328SnmpGroupsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpGroupsCreate.setStatus("current")
_Gs2328SnmpGroupsTable_Object = MibTable
gs2328SnmpGroupsTable = _Gs2328SnmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328SnmpGroupsTable.setStatus("current")
_Gs2328SnmpGroupsEntry_Object = MibTableRow
gs2328SnmpGroupsEntry = _Gs2328SnmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2, 1)
)
gs2328SnmpGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SnmpGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328SnmpGroupsEntry.setStatus("current")


class _Gs2328SnmpGroupsIndex_Type(Integer32):
    """Custom type gs2328SnmpGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2328SnmpGroupsIndex_Type.__name__ = "Integer32"
_Gs2328SnmpGroupsIndex_Object = MibTableColumn
gs2328SnmpGroupsIndex = _Gs2328SnmpGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2, 1, 1),
    _Gs2328SnmpGroupsIndex_Type()
)
gs2328SnmpGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SnmpGroupsIndex.setStatus("current")


class _Gs2328SnmpGroupsSecurityModel_Type(Integer32):
    """Custom type gs2328SnmpGroupsSecurityModel based on Integer32"""
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


_Gs2328SnmpGroupsSecurityModel_Type.__name__ = "Integer32"
_Gs2328SnmpGroupsSecurityModel_Object = MibTableColumn
gs2328SnmpGroupsSecurityModel = _Gs2328SnmpGroupsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2, 1, 2),
    _Gs2328SnmpGroupsSecurityModel_Type()
)
gs2328SnmpGroupsSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpGroupsSecurityModel.setStatus("current")


class _Gs2328SnmpGroupsSecurityName_Type(DisplayString):
    """Custom type gs2328SnmpGroupsSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpGroupsSecurityName_Type.__name__ = "DisplayString"
_Gs2328SnmpGroupsSecurityName_Object = MibTableColumn
gs2328SnmpGroupsSecurityName = _Gs2328SnmpGroupsSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2, 1, 3),
    _Gs2328SnmpGroupsSecurityName_Type()
)
gs2328SnmpGroupsSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpGroupsSecurityName.setStatus("current")


class _Gs2328SnmpGroupsGroupName_Type(DisplayString):
    """Custom type gs2328SnmpGroupsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpGroupsGroupName_Type.__name__ = "DisplayString"
_Gs2328SnmpGroupsGroupName_Object = MibTableColumn
gs2328SnmpGroupsGroupName = _Gs2328SnmpGroupsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2, 1, 4),
    _Gs2328SnmpGroupsGroupName_Type()
)
gs2328SnmpGroupsGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpGroupsGroupName.setStatus("current")


class _Gs2328SnmpGroupsRowStatus_Type(Integer32):
    """Custom type gs2328SnmpGroupsRowStatus based on Integer32"""
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


_Gs2328SnmpGroupsRowStatus_Type.__name__ = "Integer32"
_Gs2328SnmpGroupsRowStatus_Object = MibTableColumn
gs2328SnmpGroupsRowStatus = _Gs2328SnmpGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 5, 2, 1, 5),
    _Gs2328SnmpGroupsRowStatus_Type()
)
gs2328SnmpGroupsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpGroupsRowStatus.setStatus("current")
_Gs2328SnmpViews_ObjectIdentity = ObjectIdentity
gs2328SnmpViews = _Gs2328SnmpViews_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6)
)


class _Gs2328SnmpViewsCreate_Type(Integer32):
    """Custom type gs2328SnmpViewsCreate based on Integer32"""
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


_Gs2328SnmpViewsCreate_Type.__name__ = "Integer32"
_Gs2328SnmpViewsCreate_Object = MibScalar
gs2328SnmpViewsCreate = _Gs2328SnmpViewsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 1),
    _Gs2328SnmpViewsCreate_Type()
)
gs2328SnmpViewsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpViewsCreate.setStatus("current")
_Gs2328SnmpViewsTable_Object = MibTable
gs2328SnmpViewsTable = _Gs2328SnmpViewsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328SnmpViewsTable.setStatus("current")
_Gs2328SnmpViewsEntry_Object = MibTableRow
gs2328SnmpViewsEntry = _Gs2328SnmpViewsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2, 1)
)
gs2328SnmpViewsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SnmpViewsIndex"),
)
if mibBuilder.loadTexts:
    gs2328SnmpViewsEntry.setStatus("current")


class _Gs2328SnmpViewsIndex_Type(Integer32):
    """Custom type gs2328SnmpViewsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2328SnmpViewsIndex_Type.__name__ = "Integer32"
_Gs2328SnmpViewsIndex_Object = MibTableColumn
gs2328SnmpViewsIndex = _Gs2328SnmpViewsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2, 1, 1),
    _Gs2328SnmpViewsIndex_Type()
)
gs2328SnmpViewsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SnmpViewsIndex.setStatus("current")


class _Gs2328SnmpViewsName_Type(DisplayString):
    """Custom type gs2328SnmpViewsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpViewsName_Type.__name__ = "DisplayString"
_Gs2328SnmpViewsName_Object = MibTableColumn
gs2328SnmpViewsName = _Gs2328SnmpViewsName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2, 1, 2),
    _Gs2328SnmpViewsName_Type()
)
gs2328SnmpViewsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpViewsName.setStatus("current")


class _Gs2328SnmpViewsType_Type(Integer32):
    """Custom type gs2328SnmpViewsType based on Integer32"""
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


_Gs2328SnmpViewsType_Type.__name__ = "Integer32"
_Gs2328SnmpViewsType_Object = MibTableColumn
gs2328SnmpViewsType = _Gs2328SnmpViewsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2, 1, 3),
    _Gs2328SnmpViewsType_Type()
)
gs2328SnmpViewsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpViewsType.setStatus("current")


class _Gs2328SnmpViewsOIDSubtree_Type(DisplayString):
    """Custom type gs2328SnmpViewsOIDSubtree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Gs2328SnmpViewsOIDSubtree_Type.__name__ = "DisplayString"
_Gs2328SnmpViewsOIDSubtree_Object = MibTableColumn
gs2328SnmpViewsOIDSubtree = _Gs2328SnmpViewsOIDSubtree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2, 1, 4),
    _Gs2328SnmpViewsOIDSubtree_Type()
)
gs2328SnmpViewsOIDSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpViewsOIDSubtree.setStatus("current")


class _Gs2328SnmpViewsRowStatus_Type(Integer32):
    """Custom type gs2328SnmpViewsRowStatus based on Integer32"""
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


_Gs2328SnmpViewsRowStatus_Type.__name__ = "Integer32"
_Gs2328SnmpViewsRowStatus_Object = MibTableColumn
gs2328SnmpViewsRowStatus = _Gs2328SnmpViewsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 6, 2, 1, 5),
    _Gs2328SnmpViewsRowStatus_Type()
)
gs2328SnmpViewsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpViewsRowStatus.setStatus("current")
_Gs2328SnmpAccess_ObjectIdentity = ObjectIdentity
gs2328SnmpAccess = _Gs2328SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7)
)


class _Gs2328SnmpAccessCreate_Type(Integer32):
    """Custom type gs2328SnmpAccessCreate based on Integer32"""
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


_Gs2328SnmpAccessCreate_Type.__name__ = "Integer32"
_Gs2328SnmpAccessCreate_Object = MibScalar
gs2328SnmpAccessCreate = _Gs2328SnmpAccessCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 1),
    _Gs2328SnmpAccessCreate_Type()
)
gs2328SnmpAccessCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessCreate.setStatus("current")
_Gs2328SnmpAccessTable_Object = MibTable
gs2328SnmpAccessTable = _Gs2328SnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328SnmpAccessTable.setStatus("current")
_Gs2328SnmpAccessEntry_Object = MibTableRow
gs2328SnmpAccessEntry = _Gs2328SnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1)
)
gs2328SnmpAccessEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    gs2328SnmpAccessEntry.setStatus("current")


class _Gs2328SnmpAccessIndex_Type(Integer32):
    """Custom type gs2328SnmpAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2328SnmpAccessIndex_Type.__name__ = "Integer32"
_Gs2328SnmpAccessIndex_Object = MibTableColumn
gs2328SnmpAccessIndex = _Gs2328SnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 1),
    _Gs2328SnmpAccessIndex_Type()
)
gs2328SnmpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SnmpAccessIndex.setStatus("current")


class _Gs2328SnmpAccessGroupName_Type(DisplayString):
    """Custom type gs2328SnmpAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpAccessGroupName_Type.__name__ = "DisplayString"
_Gs2328SnmpAccessGroupName_Object = MibTableColumn
gs2328SnmpAccessGroupName = _Gs2328SnmpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 2),
    _Gs2328SnmpAccessGroupName_Type()
)
gs2328SnmpAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessGroupName.setStatus("current")


class _Gs2328SnmpAccessSecurityModel_Type(Integer32):
    """Custom type gs2328SnmpAccessSecurityModel based on Integer32"""
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


_Gs2328SnmpAccessSecurityModel_Type.__name__ = "Integer32"
_Gs2328SnmpAccessSecurityModel_Object = MibTableColumn
gs2328SnmpAccessSecurityModel = _Gs2328SnmpAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 3),
    _Gs2328SnmpAccessSecurityModel_Type()
)
gs2328SnmpAccessSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessSecurityModel.setStatus("current")


class _Gs2328SnmpAccessSecurityLevel_Type(Integer32):
    """Custom type gs2328SnmpAccessSecurityLevel based on Integer32"""
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


_Gs2328SnmpAccessSecurityLevel_Type.__name__ = "Integer32"
_Gs2328SnmpAccessSecurityLevel_Object = MibTableColumn
gs2328SnmpAccessSecurityLevel = _Gs2328SnmpAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 4),
    _Gs2328SnmpAccessSecurityLevel_Type()
)
gs2328SnmpAccessSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessSecurityLevel.setStatus("current")


class _Gs2328SnmpAccessReadViewName_Type(DisplayString):
    """Custom type gs2328SnmpAccessReadViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpAccessReadViewName_Type.__name__ = "DisplayString"
_Gs2328SnmpAccessReadViewName_Object = MibTableColumn
gs2328SnmpAccessReadViewName = _Gs2328SnmpAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 5),
    _Gs2328SnmpAccessReadViewName_Type()
)
gs2328SnmpAccessReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessReadViewName.setStatus("current")


class _Gs2328SnmpAccessWriteViewName_Type(DisplayString):
    """Custom type gs2328SnmpAccessWriteViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328SnmpAccessWriteViewName_Type.__name__ = "DisplayString"
_Gs2328SnmpAccessWriteViewName_Object = MibTableColumn
gs2328SnmpAccessWriteViewName = _Gs2328SnmpAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 6),
    _Gs2328SnmpAccessWriteViewName_Type()
)
gs2328SnmpAccessWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessWriteViewName.setStatus("current")


class _Gs2328SnmpAccessRowStatus_Type(Integer32):
    """Custom type gs2328SnmpAccessRowStatus based on Integer32"""
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


_Gs2328SnmpAccessRowStatus_Type.__name__ = "Integer32"
_Gs2328SnmpAccessRowStatus_Object = MibTableColumn
gs2328SnmpAccessRowStatus = _Gs2328SnmpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 1, 6, 7, 2, 1, 7),
    _Gs2328SnmpAccessRowStatus_Type()
)
gs2328SnmpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SnmpAccessRowStatus.setStatus("current")
_Gs2328Configuration_ObjectIdentity = ObjectIdentity
gs2328Configuration = _Gs2328Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2)
)
_Gs2328Port_ObjectIdentity = ObjectIdentity
gs2328Port = _Gs2328Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1)
)
_Gs2328PortConfigurationTable_Object = MibTable
gs2328PortConfigurationTable = _Gs2328PortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1)
)
if mibBuilder.loadTexts:
    gs2328PortConfigurationTable.setStatus("current")
_Gs2328PortConfigurationEntry_Object = MibTableRow
gs2328PortConfigurationEntry = _Gs2328PortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1)
)
gs2328PortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328PortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328PortConfigurationEntry.setStatus("current")


class _Gs2328PortConfPort_Type(Integer32):
    """Custom type gs2328PortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortConfPort_Type.__name__ = "Integer32"
_Gs2328PortConfPort_Object = MibTableColumn
gs2328PortConfPort = _Gs2328PortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 1),
    _Gs2328PortConfPort_Type()
)
gs2328PortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328PortConfPort.setStatus("current")


class _Gs2328PortConfPortMedia_Type(DisplayString):
    """Custom type gs2328PortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Gs2328PortConfPortMedia_Type.__name__ = "DisplayString"
_Gs2328PortConfPortMedia_Object = MibTableColumn
gs2328PortConfPortMedia = _Gs2328PortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 2),
    _Gs2328PortConfPortMedia_Type()
)
gs2328PortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortConfPortMedia.setStatus("current")


class _Gs2328PortConfLink_Type(DisplayString):
    """Custom type gs2328PortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Gs2328PortConfLink_Type.__name__ = "DisplayString"
_Gs2328PortConfLink_Object = MibTableColumn
gs2328PortConfLink = _Gs2328PortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 3),
    _Gs2328PortConfLink_Type()
)
gs2328PortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortConfLink.setStatus("current")


class _Gs2328PortConfCurrentSpeed_Type(DisplayString):
    """Custom type gs2328PortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Gs2328PortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Gs2328PortConfCurrentSpeed_Object = MibTableColumn
gs2328PortConfCurrentSpeed = _Gs2328PortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 4),
    _Gs2328PortConfCurrentSpeed_Type()
)
gs2328PortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortConfCurrentSpeed.setStatus("current")


class _Gs2328PortConfSpeed_Type(Integer32):
    """Custom type gs2328PortConfSpeed based on Integer32"""
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


_Gs2328PortConfSpeed_Type.__name__ = "Integer32"
_Gs2328PortConfSpeed_Object = MibTableColumn
gs2328PortConfSpeed = _Gs2328PortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 5),
    _Gs2328PortConfSpeed_Type()
)
gs2328PortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortConfSpeed.setStatus("current")


class _Gs2328PortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type gs2328PortConfCurrentFlowControlRx based on Integer32"""
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


_Gs2328PortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Gs2328PortConfCurrentFlowControlRx_Object = MibTableColumn
gs2328PortConfCurrentFlowControlRx = _Gs2328PortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 6),
    _Gs2328PortConfCurrentFlowControlRx_Type()
)
gs2328PortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortConfCurrentFlowControlRx.setStatus("current")


class _Gs2328PortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type gs2328PortConfCurrentFlowControlTx based on Integer32"""
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


_Gs2328PortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Gs2328PortConfCurrentFlowControlTx_Object = MibTableColumn
gs2328PortConfCurrentFlowControlTx = _Gs2328PortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 7),
    _Gs2328PortConfCurrentFlowControlTx_Type()
)
gs2328PortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortConfCurrentFlowControlTx.setStatus("current")


class _Gs2328PortConfFlowControl_Type(Integer32):
    """Custom type gs2328PortConfFlowControl based on Integer32"""
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


_Gs2328PortConfFlowControl_Type.__name__ = "Integer32"
_Gs2328PortConfFlowControl_Object = MibTableColumn
gs2328PortConfFlowControl = _Gs2328PortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 8),
    _Gs2328PortConfFlowControl_Type()
)
gs2328PortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortConfFlowControl.setStatus("current")


class _Gs2328PortConfMaxFrameSize_Type(Integer32):
    """Custom type gs2328PortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Gs2328PortConfMaxFrameSize_Type.__name__ = "Integer32"
_Gs2328PortConfMaxFrameSize_Object = MibTableColumn
gs2328PortConfMaxFrameSize = _Gs2328PortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 9),
    _Gs2328PortConfMaxFrameSize_Type()
)
gs2328PortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortConfMaxFrameSize.setStatus("current")


class _Gs2328PortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type gs2328PortConfExcessiveCollisionMode based on Integer32"""
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


_Gs2328PortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Gs2328PortConfExcessiveCollisionMode_Object = MibTableColumn
gs2328PortConfExcessiveCollisionMode = _Gs2328PortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 10),
    _Gs2328PortConfExcessiveCollisionMode_Type()
)
gs2328PortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortConfExcessiveCollisionMode.setStatus("current")


class _Gs2328PortConfPowerControl_Type(Integer32):
    """Custom type gs2328PortConfPowerControl based on Integer32"""
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


_Gs2328PortConfPowerControl_Type.__name__ = "Integer32"
_Gs2328PortConfPowerControl_Object = MibTableColumn
gs2328PortConfPowerControl = _Gs2328PortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 11),
    _Gs2328PortConfPowerControl_Type()
)
gs2328PortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortConfPowerControl.setStatus("current")
_Gs2328PortConfDescription_Type = DisplayString
_Gs2328PortConfDescription_Object = MibTableColumn
gs2328PortConfDescription = _Gs2328PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 1, 1, 12),
    _Gs2328PortConfDescription_Type()
)
gs2328PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortConfDescription.setStatus("current")
_Gs2328PortTrafficStatisticsTable_Object = MibTable
gs2328PortTrafficStatisticsTable = _Gs2328PortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328PortTrafficStatisticsTable.setStatus("current")
_Gs2328PortTrafficStatisticsEntry_Object = MibTableRow
gs2328PortTrafficStatisticsEntry = _Gs2328PortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1)
)
gs2328PortTrafficStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328PortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328PortTrafficStatisticsEntry.setStatus("current")


class _Gs2328PortTrafficStatisticsPort_Type(Integer32):
    """Custom type gs2328PortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Gs2328PortTrafficStatisticsPort_Object = MibTableColumn
gs2328PortTrafficStatisticsPort = _Gs2328PortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 1),
    _Gs2328PortTrafficStatisticsPort_Type()
)
gs2328PortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328PortTrafficStatisticsPort.setStatus("current")


class _Gs2328PortTrafficStatisticsClear_Type(Integer32):
    """Custom type gs2328PortTrafficStatisticsClear based on Integer32"""
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


_Gs2328PortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Gs2328PortTrafficStatisticsClear_Object = MibTableColumn
gs2328PortTrafficStatisticsClear = _Gs2328PortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 2),
    _Gs2328PortTrafficStatisticsClear_Type()
)
gs2328PortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortTrafficStatisticsClear.setStatus("current")
_Gs2328PortTrafficRxPackets_Type = Counter64
_Gs2328PortTrafficRxPackets_Object = MibTableColumn
gs2328PortTrafficRxPackets = _Gs2328PortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 3),
    _Gs2328PortTrafficRxPackets_Type()
)
gs2328PortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxPackets.setStatus("current")
_Gs2328PortTrafficRxOctets_Type = Counter64
_Gs2328PortTrafficRxOctets_Object = MibTableColumn
gs2328PortTrafficRxOctets = _Gs2328PortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 4),
    _Gs2328PortTrafficRxOctets_Type()
)
gs2328PortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxOctets.setStatus("current")
_Gs2328PortTrafficRxUnicast_Type = Counter64
_Gs2328PortTrafficRxUnicast_Object = MibTableColumn
gs2328PortTrafficRxUnicast = _Gs2328PortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 5),
    _Gs2328PortTrafficRxUnicast_Type()
)
gs2328PortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxUnicast.setStatus("current")
_Gs2328PortTrafficRxMulticast_Type = Counter64
_Gs2328PortTrafficRxMulticast_Object = MibTableColumn
gs2328PortTrafficRxMulticast = _Gs2328PortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 6),
    _Gs2328PortTrafficRxMulticast_Type()
)
gs2328PortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxMulticast.setStatus("current")
_Gs2328PortTrafficRxBroadcast_Type = Counter64
_Gs2328PortTrafficRxBroadcast_Object = MibTableColumn
gs2328PortTrafficRxBroadcast = _Gs2328PortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 7),
    _Gs2328PortTrafficRxBroadcast_Type()
)
gs2328PortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxBroadcast.setStatus("current")
_Gs2328PortTrafficRxPause_Type = Counter64
_Gs2328PortTrafficRxPause_Object = MibTableColumn
gs2328PortTrafficRxPause = _Gs2328PortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 8),
    _Gs2328PortTrafficRxPause_Type()
)
gs2328PortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxPause.setStatus("current")
_Gs2328PortTrafficRx64Bytes_Type = Counter64
_Gs2328PortTrafficRx64Bytes_Object = MibTableColumn
gs2328PortTrafficRx64Bytes = _Gs2328PortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 9),
    _Gs2328PortTrafficRx64Bytes_Type()
)
gs2328PortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRx64Bytes.setStatus("current")
_Gs2328PortTrafficRx65to127Bytes_Type = Counter64
_Gs2328PortTrafficRx65to127Bytes_Object = MibTableColumn
gs2328PortTrafficRx65to127Bytes = _Gs2328PortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 10),
    _Gs2328PortTrafficRx65to127Bytes_Type()
)
gs2328PortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRx65to127Bytes.setStatus("current")
_Gs2328PortTrafficRx128to255Bytes_Type = Counter64
_Gs2328PortTrafficRx128to255Bytes_Object = MibTableColumn
gs2328PortTrafficRx128to255Bytes = _Gs2328PortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 11),
    _Gs2328PortTrafficRx128to255Bytes_Type()
)
gs2328PortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRx128to255Bytes.setStatus("current")
_Gs2328PortTrafficRx256to511Bytes_Type = Counter64
_Gs2328PortTrafficRx256to511Bytes_Object = MibTableColumn
gs2328PortTrafficRx256to511Bytes = _Gs2328PortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 12),
    _Gs2328PortTrafficRx256to511Bytes_Type()
)
gs2328PortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRx256to511Bytes.setStatus("current")
_Gs2328PortTrafficRx512to1023Bytes_Type = Counter64
_Gs2328PortTrafficRx512to1023Bytes_Object = MibTableColumn
gs2328PortTrafficRx512to1023Bytes = _Gs2328PortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 13),
    _Gs2328PortTrafficRx512to1023Bytes_Type()
)
gs2328PortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRx512to1023Bytes.setStatus("current")
_Gs2328PortTrafficRx1024to1526Bytes_Type = Counter64
_Gs2328PortTrafficRx1024to1526Bytes_Object = MibTableColumn
gs2328PortTrafficRx1024to1526Bytes = _Gs2328PortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 14),
    _Gs2328PortTrafficRx1024to1526Bytes_Type()
)
gs2328PortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRx1024to1526Bytes.setStatus("current")
_Gs2328PortTrafficRxExceecd1527Bytes_Type = Counter64
_Gs2328PortTrafficRxExceecd1527Bytes_Object = MibTableColumn
gs2328PortTrafficRxExceecd1527Bytes = _Gs2328PortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 15),
    _Gs2328PortTrafficRxExceecd1527Bytes_Type()
)
gs2328PortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxExceecd1527Bytes.setStatus("current")
_Gs2328PortTrafficRxQ0_Type = Counter64
_Gs2328PortTrafficRxQ0_Object = MibTableColumn
gs2328PortTrafficRxQ0 = _Gs2328PortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 16),
    _Gs2328PortTrafficRxQ0_Type()
)
gs2328PortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ0.setStatus("current")
_Gs2328PortTrafficRxQ1_Type = Counter64
_Gs2328PortTrafficRxQ1_Object = MibTableColumn
gs2328PortTrafficRxQ1 = _Gs2328PortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 17),
    _Gs2328PortTrafficRxQ1_Type()
)
gs2328PortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ1.setStatus("current")
_Gs2328PortTrafficRxQ2_Type = Counter64
_Gs2328PortTrafficRxQ2_Object = MibTableColumn
gs2328PortTrafficRxQ2 = _Gs2328PortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 18),
    _Gs2328PortTrafficRxQ2_Type()
)
gs2328PortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ2.setStatus("current")
_Gs2328PortTrafficRxQ3_Type = Counter64
_Gs2328PortTrafficRxQ3_Object = MibTableColumn
gs2328PortTrafficRxQ3 = _Gs2328PortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 19),
    _Gs2328PortTrafficRxQ3_Type()
)
gs2328PortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ3.setStatus("current")
_Gs2328PortTrafficRxQ4_Type = Counter64
_Gs2328PortTrafficRxQ4_Object = MibTableColumn
gs2328PortTrafficRxQ4 = _Gs2328PortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 20),
    _Gs2328PortTrafficRxQ4_Type()
)
gs2328PortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ4.setStatus("current")
_Gs2328PortTrafficRxQ5_Type = Counter64
_Gs2328PortTrafficRxQ5_Object = MibTableColumn
gs2328PortTrafficRxQ5 = _Gs2328PortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 21),
    _Gs2328PortTrafficRxQ5_Type()
)
gs2328PortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ5.setStatus("current")
_Gs2328PortTrafficRxQ6_Type = Counter64
_Gs2328PortTrafficRxQ6_Object = MibTableColumn
gs2328PortTrafficRxQ6 = _Gs2328PortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 22),
    _Gs2328PortTrafficRxQ6_Type()
)
gs2328PortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ6.setStatus("current")
_Gs2328PortTrafficRxQ7_Type = Counter64
_Gs2328PortTrafficRxQ7_Object = MibTableColumn
gs2328PortTrafficRxQ7 = _Gs2328PortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 23),
    _Gs2328PortTrafficRxQ7_Type()
)
gs2328PortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxQ7.setStatus("current")
_Gs2328PortTrafficRxDrops_Type = Counter64
_Gs2328PortTrafficRxDrops_Object = MibTableColumn
gs2328PortTrafficRxDrops = _Gs2328PortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 24),
    _Gs2328PortTrafficRxDrops_Type()
)
gs2328PortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxDrops.setStatus("current")
_Gs2328PortTrafficRxCRCorAlignment_Type = Counter64
_Gs2328PortTrafficRxCRCorAlignment_Object = MibTableColumn
gs2328PortTrafficRxCRCorAlignment = _Gs2328PortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 25),
    _Gs2328PortTrafficRxCRCorAlignment_Type()
)
gs2328PortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxCRCorAlignment.setStatus("current")
_Gs2328PortTrafficRxUndersize_Type = Counter64
_Gs2328PortTrafficRxUndersize_Object = MibTableColumn
gs2328PortTrafficRxUndersize = _Gs2328PortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 26),
    _Gs2328PortTrafficRxUndersize_Type()
)
gs2328PortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxUndersize.setStatus("current")
_Gs2328PortTrafficRxOversize_Type = Counter64
_Gs2328PortTrafficRxOversize_Object = MibTableColumn
gs2328PortTrafficRxOversize = _Gs2328PortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 27),
    _Gs2328PortTrafficRxOversize_Type()
)
gs2328PortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxOversize.setStatus("current")
_Gs2328PortTrafficRxFragments_Type = Counter64
_Gs2328PortTrafficRxFragments_Object = MibTableColumn
gs2328PortTrafficRxFragments = _Gs2328PortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 28),
    _Gs2328PortTrafficRxFragments_Type()
)
gs2328PortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxFragments.setStatus("current")
_Gs2328PortTrafficRxJabber_Type = Counter64
_Gs2328PortTrafficRxJabber_Object = MibTableColumn
gs2328PortTrafficRxJabber = _Gs2328PortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 29),
    _Gs2328PortTrafficRxJabber_Type()
)
gs2328PortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxJabber.setStatus("current")
_Gs2328PortTrafficRxFiltered_Type = Counter64
_Gs2328PortTrafficRxFiltered_Object = MibTableColumn
gs2328PortTrafficRxFiltered = _Gs2328PortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 30),
    _Gs2328PortTrafficRxFiltered_Type()
)
gs2328PortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficRxFiltered.setStatus("current")
_Gs2328PortTrafficTxPackets_Type = Counter64
_Gs2328PortTrafficTxPackets_Object = MibTableColumn
gs2328PortTrafficTxPackets = _Gs2328PortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 31),
    _Gs2328PortTrafficTxPackets_Type()
)
gs2328PortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxPackets.setStatus("current")
_Gs2328PortTrafficTxOctets_Type = Counter64
_Gs2328PortTrafficTxOctets_Object = MibTableColumn
gs2328PortTrafficTxOctets = _Gs2328PortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 32),
    _Gs2328PortTrafficTxOctets_Type()
)
gs2328PortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxOctets.setStatus("current")
_Gs2328PortTrafficTxUnicast_Type = Counter64
_Gs2328PortTrafficTxUnicast_Object = MibTableColumn
gs2328PortTrafficTxUnicast = _Gs2328PortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 33),
    _Gs2328PortTrafficTxUnicast_Type()
)
gs2328PortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxUnicast.setStatus("current")
_Gs2328PortTrafficTxMulticast_Type = Counter64
_Gs2328PortTrafficTxMulticast_Object = MibTableColumn
gs2328PortTrafficTxMulticast = _Gs2328PortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 34),
    _Gs2328PortTrafficTxMulticast_Type()
)
gs2328PortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxMulticast.setStatus("current")
_Gs2328PortTrafficTxBroadcast_Type = Counter64
_Gs2328PortTrafficTxBroadcast_Object = MibTableColumn
gs2328PortTrafficTxBroadcast = _Gs2328PortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 35),
    _Gs2328PortTrafficTxBroadcast_Type()
)
gs2328PortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxBroadcast.setStatus("current")
_Gs2328PortTrafficTxPause_Type = Counter64
_Gs2328PortTrafficTxPause_Object = MibTableColumn
gs2328PortTrafficTxPause = _Gs2328PortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 36),
    _Gs2328PortTrafficTxPause_Type()
)
gs2328PortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxPause.setStatus("current")
_Gs2328PortTrafficTx64Bytes_Type = Counter64
_Gs2328PortTrafficTx64Bytes_Object = MibTableColumn
gs2328PortTrafficTx64Bytes = _Gs2328PortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 37),
    _Gs2328PortTrafficTx64Bytes_Type()
)
gs2328PortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTx64Bytes.setStatus("current")
_Gs2328PortTrafficTx65to127Bytes_Type = Counter64
_Gs2328PortTrafficTx65to127Bytes_Object = MibTableColumn
gs2328PortTrafficTx65to127Bytes = _Gs2328PortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 38),
    _Gs2328PortTrafficTx65to127Bytes_Type()
)
gs2328PortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTx65to127Bytes.setStatus("current")
_Gs2328PortTrafficTx128to255Bytes_Type = Counter64
_Gs2328PortTrafficTx128to255Bytes_Object = MibTableColumn
gs2328PortTrafficTx128to255Bytes = _Gs2328PortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 39),
    _Gs2328PortTrafficTx128to255Bytes_Type()
)
gs2328PortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTx128to255Bytes.setStatus("current")
_Gs2328PortTrafficTx256to511Bytes_Type = Counter64
_Gs2328PortTrafficTx256to511Bytes_Object = MibTableColumn
gs2328PortTrafficTx256to511Bytes = _Gs2328PortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 40),
    _Gs2328PortTrafficTx256to511Bytes_Type()
)
gs2328PortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTx256to511Bytes.setStatus("current")
_Gs2328PortTrafficTx512to1023Bytes_Type = Counter64
_Gs2328PortTrafficTx512to1023Bytes_Object = MibTableColumn
gs2328PortTrafficTx512to1023Bytes = _Gs2328PortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 41),
    _Gs2328PortTrafficTx512to1023Bytes_Type()
)
gs2328PortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTx512to1023Bytes.setStatus("current")
_Gs2328PortTrafficTx1024to1526Bytes_Type = Counter64
_Gs2328PortTrafficTx1024to1526Bytes_Object = MibTableColumn
gs2328PortTrafficTx1024to1526Bytes = _Gs2328PortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 42),
    _Gs2328PortTrafficTx1024to1526Bytes_Type()
)
gs2328PortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTx1024to1526Bytes.setStatus("current")
_Gs2328PortTrafficTxExceecd1527Bytes_Type = Counter64
_Gs2328PortTrafficTxExceecd1527Bytes_Object = MibTableColumn
gs2328PortTrafficTxExceecd1527Bytes = _Gs2328PortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 43),
    _Gs2328PortTrafficTxExceecd1527Bytes_Type()
)
gs2328PortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxExceecd1527Bytes.setStatus("current")
_Gs2328PortTrafficTxQ0_Type = Counter64
_Gs2328PortTrafficTxQ0_Object = MibTableColumn
gs2328PortTrafficTxQ0 = _Gs2328PortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 44),
    _Gs2328PortTrafficTxQ0_Type()
)
gs2328PortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ0.setStatus("current")
_Gs2328PortTrafficTxQ1_Type = Counter64
_Gs2328PortTrafficTxQ1_Object = MibTableColumn
gs2328PortTrafficTxQ1 = _Gs2328PortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 45),
    _Gs2328PortTrafficTxQ1_Type()
)
gs2328PortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ1.setStatus("current")
_Gs2328PortTrafficTxQ2_Type = Counter64
_Gs2328PortTrafficTxQ2_Object = MibTableColumn
gs2328PortTrafficTxQ2 = _Gs2328PortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 46),
    _Gs2328PortTrafficTxQ2_Type()
)
gs2328PortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ2.setStatus("current")
_Gs2328PortTrafficTxQ3_Type = Counter64
_Gs2328PortTrafficTxQ3_Object = MibTableColumn
gs2328PortTrafficTxQ3 = _Gs2328PortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 47),
    _Gs2328PortTrafficTxQ3_Type()
)
gs2328PortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ3.setStatus("current")
_Gs2328PortTrafficTxQ4_Type = Counter64
_Gs2328PortTrafficTxQ4_Object = MibTableColumn
gs2328PortTrafficTxQ4 = _Gs2328PortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 48),
    _Gs2328PortTrafficTxQ4_Type()
)
gs2328PortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ4.setStatus("current")
_Gs2328PortTrafficTxQ5_Type = Counter64
_Gs2328PortTrafficTxQ5_Object = MibTableColumn
gs2328PortTrafficTxQ5 = _Gs2328PortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 49),
    _Gs2328PortTrafficTxQ5_Type()
)
gs2328PortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ5.setStatus("current")
_Gs2328PortTrafficTxQ6_Type = Counter64
_Gs2328PortTrafficTxQ6_Object = MibTableColumn
gs2328PortTrafficTxQ6 = _Gs2328PortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 50),
    _Gs2328PortTrafficTxQ6_Type()
)
gs2328PortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ6.setStatus("current")
_Gs2328PortTrafficTxQ7_Type = Counter64
_Gs2328PortTrafficTxQ7_Object = MibTableColumn
gs2328PortTrafficTxQ7 = _Gs2328PortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 51),
    _Gs2328PortTrafficTxQ7_Type()
)
gs2328PortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxQ7.setStatus("current")
_Gs2328PortTrafficTxDrops_Type = Counter64
_Gs2328PortTrafficTxDrops_Object = MibTableColumn
gs2328PortTrafficTxDrops = _Gs2328PortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 52),
    _Gs2328PortTrafficTxDrops_Type()
)
gs2328PortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxDrops.setStatus("current")
_Gs2328PortTrafficTxLateOrExcColl_Type = Counter64
_Gs2328PortTrafficTxLateOrExcColl_Object = MibTableColumn
gs2328PortTrafficTxLateOrExcColl = _Gs2328PortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 2, 1, 53),
    _Gs2328PortTrafficTxLateOrExcColl_Type()
)
gs2328PortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortTrafficTxLateOrExcColl.setStatus("current")
_Gs2328PortQoSStatistics_ObjectIdentity = ObjectIdentity
gs2328PortQoSStatistics = _Gs2328PortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3)
)


class _Gs2328PortQoSStatisticsClear_Type(Integer32):
    """Custom type gs2328PortQoSStatisticsClear based on Integer32"""
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


_Gs2328PortQoSStatisticsClear_Type.__name__ = "Integer32"
_Gs2328PortQoSStatisticsClear_Object = MibScalar
gs2328PortQoSStatisticsClear = _Gs2328PortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 1),
    _Gs2328PortQoSStatisticsClear_Type()
)
gs2328PortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSStatisticsClear.setStatus("current")
_Gs2328PortQoSStatisticsTable_Object = MibTable
gs2328PortQoSStatisticsTable = _Gs2328PortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328PortQoSStatisticsTable.setStatus("current")
_Gs2328PortQoSStatisticsEntry_Object = MibTableRow
gs2328PortQoSStatisticsEntry = _Gs2328PortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1)
)
gs2328PortQoSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328PortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328PortQoSStatisticsEntry.setStatus("current")


class _Gs2328PortQoSStatisticsPort_Type(Integer32):
    """Custom type gs2328PortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortQoSStatisticsPort_Type.__name__ = "Integer32"
_Gs2328PortQoSStatisticsPort_Object = MibTableColumn
gs2328PortQoSStatisticsPort = _Gs2328PortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 1),
    _Gs2328PortQoSStatisticsPort_Type()
)
gs2328PortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328PortQoSStatisticsPort.setStatus("current")
_Gs2328PortQoSQ0Rx_Type = Counter64
_Gs2328PortQoSQ0Rx_Object = MibTableColumn
gs2328PortQoSQ0Rx = _Gs2328PortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 2),
    _Gs2328PortQoSQ0Rx_Type()
)
gs2328PortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ0Rx.setStatus("current")
_Gs2328PortQoSQ0Tx_Type = Counter64
_Gs2328PortQoSQ0Tx_Object = MibTableColumn
gs2328PortQoSQ0Tx = _Gs2328PortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 3),
    _Gs2328PortQoSQ0Tx_Type()
)
gs2328PortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ0Tx.setStatus("current")
_Gs2328PortQoSQ1Rx_Type = Counter64
_Gs2328PortQoSQ1Rx_Object = MibTableColumn
gs2328PortQoSQ1Rx = _Gs2328PortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 4),
    _Gs2328PortQoSQ1Rx_Type()
)
gs2328PortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ1Rx.setStatus("current")
_Gs2328PortQoSQ1Tx_Type = Counter64
_Gs2328PortQoSQ1Tx_Object = MibTableColumn
gs2328PortQoSQ1Tx = _Gs2328PortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 5),
    _Gs2328PortQoSQ1Tx_Type()
)
gs2328PortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ1Tx.setStatus("current")
_Gs2328PortQoSQ2Rx_Type = Counter64
_Gs2328PortQoSQ2Rx_Object = MibTableColumn
gs2328PortQoSQ2Rx = _Gs2328PortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 6),
    _Gs2328PortQoSQ2Rx_Type()
)
gs2328PortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ2Rx.setStatus("current")
_Gs2328PortQoSQ2Tx_Type = Counter64
_Gs2328PortQoSQ2Tx_Object = MibTableColumn
gs2328PortQoSQ2Tx = _Gs2328PortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 7),
    _Gs2328PortQoSQ2Tx_Type()
)
gs2328PortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ2Tx.setStatus("current")
_Gs2328PortQoSQ3Rx_Type = Counter64
_Gs2328PortQoSQ3Rx_Object = MibTableColumn
gs2328PortQoSQ3Rx = _Gs2328PortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 8),
    _Gs2328PortQoSQ3Rx_Type()
)
gs2328PortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ3Rx.setStatus("current")
_Gs2328PortQoSQ3Tx_Type = Counter64
_Gs2328PortQoSQ3Tx_Object = MibTableColumn
gs2328PortQoSQ3Tx = _Gs2328PortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 9),
    _Gs2328PortQoSQ3Tx_Type()
)
gs2328PortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ3Tx.setStatus("current")
_Gs2328PortQoSQ4Rx_Type = Counter64
_Gs2328PortQoSQ4Rx_Object = MibTableColumn
gs2328PortQoSQ4Rx = _Gs2328PortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 10),
    _Gs2328PortQoSQ4Rx_Type()
)
gs2328PortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ4Rx.setStatus("current")
_Gs2328PortQoSQ4Tx_Type = Counter64
_Gs2328PortQoSQ4Tx_Object = MibTableColumn
gs2328PortQoSQ4Tx = _Gs2328PortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 11),
    _Gs2328PortQoSQ4Tx_Type()
)
gs2328PortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ4Tx.setStatus("current")
_Gs2328PortQoSQ5Rx_Type = Counter64
_Gs2328PortQoSQ5Rx_Object = MibTableColumn
gs2328PortQoSQ5Rx = _Gs2328PortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 12),
    _Gs2328PortQoSQ5Rx_Type()
)
gs2328PortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ5Rx.setStatus("current")
_Gs2328PortQoSQ5Tx_Type = Counter64
_Gs2328PortQoSQ5Tx_Object = MibTableColumn
gs2328PortQoSQ5Tx = _Gs2328PortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 13),
    _Gs2328PortQoSQ5Tx_Type()
)
gs2328PortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ5Tx.setStatus("current")
_Gs2328PortQoSQ6Rx_Type = Counter64
_Gs2328PortQoSQ6Rx_Object = MibTableColumn
gs2328PortQoSQ6Rx = _Gs2328PortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 14),
    _Gs2328PortQoSQ6Rx_Type()
)
gs2328PortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ6Rx.setStatus("current")
_Gs2328PortQoSQ6Tx_Type = Counter64
_Gs2328PortQoSQ6Tx_Object = MibTableColumn
gs2328PortQoSQ6Tx = _Gs2328PortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 15),
    _Gs2328PortQoSQ6Tx_Type()
)
gs2328PortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ6Tx.setStatus("current")
_Gs2328PortQoSQ7Rx_Type = Counter64
_Gs2328PortQoSQ7Rx_Object = MibTableColumn
gs2328PortQoSQ7Rx = _Gs2328PortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 16),
    _Gs2328PortQoSQ7Rx_Type()
)
gs2328PortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ7Rx.setStatus("current")
_Gs2328PortQoSQ7Tx_Type = Counter64
_Gs2328PortQoSQ7Tx_Object = MibTableColumn
gs2328PortQoSQ7Tx = _Gs2328PortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 3, 2, 1, 17),
    _Gs2328PortQoSQ7Tx_Type()
)
gs2328PortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortQoSQ7Tx.setStatus("current")
_Gs2328SFPInfoTable_Object = MibTable
gs2328SFPInfoTable = _Gs2328SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4)
)
if mibBuilder.loadTexts:
    gs2328SFPInfoTable.setStatus("current")
_Gs2328SFPInfoEntry_Object = MibTableRow
gs2328SFPInfoEntry = _Gs2328SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1)
)
gs2328SFPInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2328SFPInfoEntry.setStatus("current")


class _Gs2328SFPInfoIndex_Type(Integer32):
    """Custom type gs2328SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328SFPInfoIndex_Type.__name__ = "Integer32"
_Gs2328SFPInfoIndex_Object = MibTableColumn
gs2328SFPInfoIndex = _Gs2328SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 1),
    _Gs2328SFPInfoIndex_Type()
)
gs2328SFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328SFPInfoIndex.setStatus("current")
_Gs2328SFPInfoPort_Type = DisplayString
_Gs2328SFPInfoPort_Object = MibTableColumn
gs2328SFPInfoPort = _Gs2328SFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 2),
    _Gs2328SFPInfoPort_Type()
)
gs2328SFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPInfoPort.setStatus("current")
_Gs2328SFPConnectorType_Type = DisplayString
_Gs2328SFPConnectorType_Object = MibTableColumn
gs2328SFPConnectorType = _Gs2328SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 3),
    _Gs2328SFPConnectorType_Type()
)
gs2328SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPConnectorType.setStatus("current")
_Gs2328SFPFiberType_Type = DisplayString
_Gs2328SFPFiberType_Object = MibTableColumn
gs2328SFPFiberType = _Gs2328SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 4),
    _Gs2328SFPFiberType_Type()
)
gs2328SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPFiberType.setStatus("current")
_Gs2328SFPTxCentralWavelength_Type = DisplayString
_Gs2328SFPTxCentralWavelength_Object = MibTableColumn
gs2328SFPTxCentralWavelength = _Gs2328SFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 5),
    _Gs2328SFPTxCentralWavelength_Type()
)
gs2328SFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPTxCentralWavelength.setStatus("current")
_Gs2328SFPBaudRate_Type = DisplayString
_Gs2328SFPBaudRate_Object = MibTableColumn
gs2328SFPBaudRate = _Gs2328SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 6),
    _Gs2328SFPBaudRate_Type()
)
gs2328SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPBaudRate.setStatus("current")
_Gs2328SFPVendorOUI_Type = DisplayString
_Gs2328SFPVendorOUI_Object = MibTableColumn
gs2328SFPVendorOUI = _Gs2328SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 7),
    _Gs2328SFPVendorOUI_Type()
)
gs2328SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPVendorOUI.setStatus("current")
_Gs2328SFPVendorName_Type = DisplayString
_Gs2328SFPVendorName_Object = MibTableColumn
gs2328SFPVendorName = _Gs2328SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 8),
    _Gs2328SFPVendorName_Type()
)
gs2328SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPVendorName.setStatus("current")
_Gs2328SFPVendorPN_Type = DisplayString
_Gs2328SFPVendorPN_Object = MibTableColumn
gs2328SFPVendorPN = _Gs2328SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 9),
    _Gs2328SFPVendorPN_Type()
)
gs2328SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPVendorPN.setStatus("current")
_Gs2328SFPVendorRev_Type = DisplayString
_Gs2328SFPVendorRev_Object = MibTableColumn
gs2328SFPVendorRev = _Gs2328SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 10),
    _Gs2328SFPVendorRev_Type()
)
gs2328SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPVendorRev.setStatus("current")
_Gs2328SFPVendorSN_Type = DisplayString
_Gs2328SFPVendorSN_Object = MibTableColumn
gs2328SFPVendorSN = _Gs2328SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 11),
    _Gs2328SFPVendorSN_Type()
)
gs2328SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPVendorSN.setStatus("current")
_Gs2328SFPDateCode_Type = DisplayString
_Gs2328SFPDateCode_Object = MibTableColumn
gs2328SFPDateCode = _Gs2328SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 12),
    _Gs2328SFPDateCode_Type()
)
gs2328SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPDateCode.setStatus("current")
_Gs2328SFPTemperature_Type = DisplayString
_Gs2328SFPTemperature_Object = MibTableColumn
gs2328SFPTemperature = _Gs2328SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 13),
    _Gs2328SFPTemperature_Type()
)
gs2328SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPTemperature.setStatus("current")
_Gs2328SFPVcc_Type = DisplayString
_Gs2328SFPVcc_Object = MibTableColumn
gs2328SFPVcc = _Gs2328SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 14),
    _Gs2328SFPVcc_Type()
)
gs2328SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPVcc.setStatus("current")
_Gs2328SFPMon1Bias_Type = DisplayString
_Gs2328SFPMon1Bias_Object = MibTableColumn
gs2328SFPMon1Bias = _Gs2328SFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 15),
    _Gs2328SFPMon1Bias_Type()
)
gs2328SFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPMon1Bias.setStatus("current")
_Gs2328SFPMon2TxPWR_Type = DisplayString
_Gs2328SFPMon2TxPWR_Object = MibTableColumn
gs2328SFPMon2TxPWR = _Gs2328SFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 16),
    _Gs2328SFPMon2TxPWR_Type()
)
gs2328SFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPMon2TxPWR.setStatus("current")
_Gs2328SFPMon3RxPWR_Type = DisplayString
_Gs2328SFPMon3RxPWR_Object = MibTableColumn
gs2328SFPMon3RxPWR = _Gs2328SFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1, 4, 1, 17),
    _Gs2328SFPMon3RxPWR_Type()
)
gs2328SFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SFPMon3RxPWR.setStatus("current")
_Gs2328VoiceVLAN_ObjectIdentity = ObjectIdentity
gs2328VoiceVLAN = _Gs2328VoiceVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2)
)
_Gs2328VoiceVLANConf_ObjectIdentity = ObjectIdentity
gs2328VoiceVLANConf = _Gs2328VoiceVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1)
)


class _Gs2328VoiceVLANMode_Type(Integer32):
    """Custom type gs2328VoiceVLANMode based on Integer32"""
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


_Gs2328VoiceVLANMode_Type.__name__ = "Integer32"
_Gs2328VoiceVLANMode_Object = MibScalar
gs2328VoiceVLANMode = _Gs2328VoiceVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 1),
    _Gs2328VoiceVLANMode_Type()
)
gs2328VoiceVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANMode.setStatus("current")


class _Gs2328VoiceVLANVLANId_Type(Integer32):
    """Custom type gs2328VoiceVLANVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328VoiceVLANVLANId_Type.__name__ = "Integer32"
_Gs2328VoiceVLANVLANId_Object = MibScalar
gs2328VoiceVLANVLANId = _Gs2328VoiceVLANVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 2),
    _Gs2328VoiceVLANVLANId_Type()
)
gs2328VoiceVLANVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANVLANId.setStatus("current")


class _Gs2328VoiceVLANAgingTime_Type(Integer32):
    """Custom type gs2328VoiceVLANAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2328VoiceVLANAgingTime_Type.__name__ = "Integer32"
_Gs2328VoiceVLANAgingTime_Object = MibScalar
gs2328VoiceVLANAgingTime = _Gs2328VoiceVLANAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 3),
    _Gs2328VoiceVLANAgingTime_Type()
)
gs2328VoiceVLANAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANAgingTime.setStatus("current")


class _Gs2328VoiceVLANTrafficClass_Type(Integer32):
    """Custom type gs2328VoiceVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328VoiceVLANTrafficClass_Type.__name__ = "Integer32"
_Gs2328VoiceVLANTrafficClass_Object = MibScalar
gs2328VoiceVLANTrafficClass = _Gs2328VoiceVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 4),
    _Gs2328VoiceVLANTrafficClass_Type()
)
gs2328VoiceVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANTrafficClass.setStatus("current")
_Gs2328VoiceVLANPortTable_Object = MibTable
gs2328VoiceVLANPortTable = _Gs2328VoiceVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2328VoiceVLANPortTable.setStatus("current")
_Gs2328VoiceVLANPortEntry_Object = MibTableRow
gs2328VoiceVLANPortEntry = _Gs2328VoiceVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5, 1)
)
gs2328VoiceVLANPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328VoiceVLANPort"),
)
if mibBuilder.loadTexts:
    gs2328VoiceVLANPortEntry.setStatus("current")


class _Gs2328VoiceVLANPort_Type(Integer32):
    """Custom type gs2328VoiceVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328VoiceVLANPort_Type.__name__ = "Integer32"
_Gs2328VoiceVLANPort_Object = MibTableColumn
gs2328VoiceVLANPort = _Gs2328VoiceVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5, 1, 1),
    _Gs2328VoiceVLANPort_Type()
)
gs2328VoiceVLANPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328VoiceVLANPort.setStatus("current")


class _Gs2328VoiceVLANPortMode_Type(Integer32):
    """Custom type gs2328VoiceVLANPortMode based on Integer32"""
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


_Gs2328VoiceVLANPortMode_Type.__name__ = "Integer32"
_Gs2328VoiceVLANPortMode_Object = MibTableColumn
gs2328VoiceVLANPortMode = _Gs2328VoiceVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5, 1, 2),
    _Gs2328VoiceVLANPortMode_Type()
)
gs2328VoiceVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANPortMode.setStatus("current")


class _Gs2328VoiceVLANPortSecurity_Type(Integer32):
    """Custom type gs2328VoiceVLANPortSecurity based on Integer32"""
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


_Gs2328VoiceVLANPortSecurity_Type.__name__ = "Integer32"
_Gs2328VoiceVLANPortSecurity_Object = MibTableColumn
gs2328VoiceVLANPortSecurity = _Gs2328VoiceVLANPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5, 1, 3),
    _Gs2328VoiceVLANPortSecurity_Type()
)
gs2328VoiceVLANPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANPortSecurity.setStatus("current")


class _Gs2328VoiceVLANPortDiscoveryProtocol_Type(Integer32):
    """Custom type gs2328VoiceVLANPortDiscoveryProtocol based on Integer32"""
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


_Gs2328VoiceVLANPortDiscoveryProtocol_Type.__name__ = "Integer32"
_Gs2328VoiceVLANPortDiscoveryProtocol_Object = MibTableColumn
gs2328VoiceVLANPortDiscoveryProtocol = _Gs2328VoiceVLANPortDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5, 1, 4),
    _Gs2328VoiceVLANPortDiscoveryProtocol_Type()
)
gs2328VoiceVLANPortDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANPortDiscoveryProtocol.setStatus("current")


class _Gs2328VoiceVLANSkipNAS_Type(Integer32):
    """Custom type gs2328VoiceVLANSkipNAS based on Integer32"""
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


_Gs2328VoiceVLANSkipNAS_Type.__name__ = "Integer32"
_Gs2328VoiceVLANSkipNAS_Object = MibScalar
gs2328VoiceVLANSkipNAS = _Gs2328VoiceVLANSkipNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 1, 5, 1, 5),
    _Gs2328VoiceVLANSkipNAS_Type()
)
gs2328VoiceVLANSkipNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANSkipNAS.setStatus("current")
_Gs2328VoiceVLANOUI_ObjectIdentity = ObjectIdentity
gs2328VoiceVLANOUI = _Gs2328VoiceVLANOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2)
)


class _Gs2328VoiceVLANOUICreate_Type(Integer32):
    """Custom type gs2328VoiceVLANOUICreate based on Integer32"""
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


_Gs2328VoiceVLANOUICreate_Type.__name__ = "Integer32"
_Gs2328VoiceVLANOUICreate_Object = MibScalar
gs2328VoiceVLANOUICreate = _Gs2328VoiceVLANOUICreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 1),
    _Gs2328VoiceVLANOUICreate_Type()
)
gs2328VoiceVLANOUICreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANOUICreate.setStatus("current")
_Gs2328VoiceVLANOUITable_Object = MibTable
gs2328VoiceVLANOUITable = _Gs2328VoiceVLANOUITable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328VoiceVLANOUITable.setStatus("current")
_Gs2328VoiceVLANOUIEntry_Object = MibTableRow
gs2328VoiceVLANOUIEntry = _Gs2328VoiceVLANOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 2, 1)
)
gs2328VoiceVLANOUIEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328VoiceVLANOUIIndex"),
)
if mibBuilder.loadTexts:
    gs2328VoiceVLANOUIEntry.setStatus("current")


class _Gs2328VoiceVLANOUIIndex_Type(Integer32):
    """Custom type gs2328VoiceVLANOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2328VoiceVLANOUIIndex_Type.__name__ = "Integer32"
_Gs2328VoiceVLANOUIIndex_Object = MibTableColumn
gs2328VoiceVLANOUIIndex = _Gs2328VoiceVLANOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 2, 1, 1),
    _Gs2328VoiceVLANOUIIndex_Type()
)
gs2328VoiceVLANOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328VoiceVLANOUIIndex.setStatus("current")


class _Gs2328VoiceVLANTelephonyOUI_Type(OctetString):
    """Custom type gs2328VoiceVLANTelephonyOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328VoiceVLANTelephonyOUI_Type.__name__ = "OctetString"
_Gs2328VoiceVLANTelephonyOUI_Object = MibTableColumn
gs2328VoiceVLANTelephonyOUI = _Gs2328VoiceVLANTelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 2, 1, 2),
    _Gs2328VoiceVLANTelephonyOUI_Type()
)
gs2328VoiceVLANTelephonyOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANTelephonyOUI.setStatus("current")


class _Gs2328VoiceVLANDescription_Type(DisplayString):
    """Custom type gs2328VoiceVLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328VoiceVLANDescription_Type.__name__ = "DisplayString"
_Gs2328VoiceVLANDescription_Object = MibTableColumn
gs2328VoiceVLANDescription = _Gs2328VoiceVLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 2, 1, 3),
    _Gs2328VoiceVLANDescription_Type()
)
gs2328VoiceVLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANDescription.setStatus("current")


class _Gs2328VoiceVLANOUIRowStatus_Type(Integer32):
    """Custom type gs2328VoiceVLANOUIRowStatus based on Integer32"""
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


_Gs2328VoiceVLANOUIRowStatus_Type.__name__ = "Integer32"
_Gs2328VoiceVLANOUIRowStatus_Object = MibTableColumn
gs2328VoiceVLANOUIRowStatus = _Gs2328VoiceVLANOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 2, 2, 2, 1, 4),
    _Gs2328VoiceVLANOUIRowStatus_Type()
)
gs2328VoiceVLANOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VoiceVLANOUIRowStatus.setStatus("current")
_Gs2328GARP_ObjectIdentity = ObjectIdentity
gs2328GARP = _Gs2328GARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3)
)
_Gs2328GARPConfTable_Object = MibTable
gs2328GARPConfTable = _Gs2328GARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gs2328GARPConfTable.setStatus("current")
_Gs2328GARPConfEntry_Object = MibTableRow
gs2328GARPConfEntry = _Gs2328GARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1)
)
gs2328GARPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328GARPConfPort"),
)
if mibBuilder.loadTexts:
    gs2328GARPConfEntry.setStatus("current")


class _Gs2328GARPConfPort_Type(Integer32):
    """Custom type gs2328GARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328GARPConfPort_Type.__name__ = "Integer32"
_Gs2328GARPConfPort_Object = MibTableColumn
gs2328GARPConfPort = _Gs2328GARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 1),
    _Gs2328GARPConfPort_Type()
)
gs2328GARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328GARPConfPort.setStatus("current")


class _Gs2328GARPJoinTimer_Type(Integer32):
    """Custom type gs2328GARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Gs2328GARPJoinTimer_Type.__name__ = "Integer32"
_Gs2328GARPJoinTimer_Object = MibTableColumn
gs2328GARPJoinTimer = _Gs2328GARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 2),
    _Gs2328GARPJoinTimer_Type()
)
gs2328GARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPJoinTimer.setStatus("current")


class _Gs2328GARPLeaveTimer_Type(Integer32):
    """Custom type gs2328GARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Gs2328GARPLeaveTimer_Type.__name__ = "Integer32"
_Gs2328GARPLeaveTimer_Object = MibTableColumn
gs2328GARPLeaveTimer = _Gs2328GARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 3),
    _Gs2328GARPLeaveTimer_Type()
)
gs2328GARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPLeaveTimer.setStatus("current")


class _Gs2328GARPLeaveAllTimer_Type(Integer32):
    """Custom type gs2328GARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Gs2328GARPLeaveAllTimer_Type.__name__ = "Integer32"
_Gs2328GARPLeaveAllTimer_Object = MibTableColumn
gs2328GARPLeaveAllTimer = _Gs2328GARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 4),
    _Gs2328GARPLeaveAllTimer_Type()
)
gs2328GARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPLeaveAllTimer.setStatus("current")


class _Gs2328GARPApplicantion_Type(Integer32):
    """Custom type gs2328GARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gvrp", 1)
    )


_Gs2328GARPApplicantion_Type.__name__ = "Integer32"
_Gs2328GARPApplicantion_Object = MibTableColumn
gs2328GARPApplicantion = _Gs2328GARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 5),
    _Gs2328GARPApplicantion_Type()
)
gs2328GARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPApplicantion.setStatus("current")


class _Gs2328GARPAttributeType_Type(Integer32):
    """Custom type gs2328GARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_Gs2328GARPAttributeType_Type.__name__ = "Integer32"
_Gs2328GARPAttributeType_Object = MibTableColumn
gs2328GARPAttributeType = _Gs2328GARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 6),
    _Gs2328GARPAttributeType_Type()
)
gs2328GARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPAttributeType.setStatus("current")


class _Gs2328GARPApplicant_Type(Integer32):
    """Custom type gs2328GARPApplicant based on Integer32"""
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


_Gs2328GARPApplicant_Type.__name__ = "Integer32"
_Gs2328GARPApplicant_Object = MibTableColumn
gs2328GARPApplicant = _Gs2328GARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 1, 1, 7),
    _Gs2328GARPApplicant_Type()
)
gs2328GARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GARPApplicant.setStatus("current")
_Gs2328GARPStatisticsTable_Object = MibTable
gs2328GARPStatisticsTable = _Gs2328GARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328GARPStatisticsTable.setStatus("current")
_Gs2328GARPStatisticsEntry_Object = MibTableRow
gs2328GARPStatisticsEntry = _Gs2328GARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 2, 1)
)
gs2328GARPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328GARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328GARPStatisticsEntry.setStatus("current")


class _Gs2328GARPStatisticsPort_Type(Integer32):
    """Custom type gs2328GARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328GARPStatisticsPort_Type.__name__ = "Integer32"
_Gs2328GARPStatisticsPort_Object = MibTableColumn
gs2328GARPStatisticsPort = _Gs2328GARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 2, 1, 1),
    _Gs2328GARPStatisticsPort_Type()
)
gs2328GARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328GARPStatisticsPort.setStatus("current")
_Gs2328GARPStatisticsPeerMAC_Type = DisplayString
_Gs2328GARPStatisticsPeerMAC_Object = MibTableColumn
gs2328GARPStatisticsPeerMAC = _Gs2328GARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 2, 1, 2),
    _Gs2328GARPStatisticsPeerMAC_Type()
)
gs2328GARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328GARPStatisticsPeerMAC.setStatus("current")
_Gs2328GARPStatisticsFailedCount_Type = Counter32
_Gs2328GARPStatisticsFailedCount_Object = MibTableColumn
gs2328GARPStatisticsFailedCount = _Gs2328GARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 3, 2, 1, 3),
    _Gs2328GARPStatisticsFailedCount_Type()
)
gs2328GARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328GARPStatisticsFailedCount.setStatus("current")
_Gs2328GVRP_ObjectIdentity = ObjectIdentity
gs2328GVRP = _Gs2328GVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4)
)
_Gs2328GVRPConf_ObjectIdentity = ObjectIdentity
gs2328GVRPConf = _Gs2328GVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1)
)


class _Gs2328GVRPMode_Type(Integer32):
    """Custom type gs2328GVRPMode based on Integer32"""
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


_Gs2328GVRPMode_Type.__name__ = "Integer32"
_Gs2328GVRPMode_Object = MibScalar
gs2328GVRPMode = _Gs2328GVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1, 1),
    _Gs2328GVRPMode_Type()
)
gs2328GVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GVRPMode.setStatus("current")
_Gs2328GVRPConfTable_Object = MibTable
gs2328GVRPConfTable = _Gs2328GVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328GVRPConfTable.setStatus("current")
_Gs2328GVRPConfEntry_Object = MibTableRow
gs2328GVRPConfEntry = _Gs2328GVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1, 2, 1)
)
gs2328GVRPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328GVRPConfPort"),
)
if mibBuilder.loadTexts:
    gs2328GVRPConfEntry.setStatus("current")


class _Gs2328GVRPConfPort_Type(Integer32):
    """Custom type gs2328GVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328GVRPConfPort_Type.__name__ = "Integer32"
_Gs2328GVRPConfPort_Object = MibTableColumn
gs2328GVRPConfPort = _Gs2328GVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1, 2, 1, 1),
    _Gs2328GVRPConfPort_Type()
)
gs2328GVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328GVRPConfPort.setStatus("current")


class _Gs2328GVRPConfPortMode_Type(Integer32):
    """Custom type gs2328GVRPConfPortMode based on Integer32"""
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


_Gs2328GVRPConfPortMode_Type.__name__ = "Integer32"
_Gs2328GVRPConfPortMode_Object = MibTableColumn
gs2328GVRPConfPortMode = _Gs2328GVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1, 2, 1, 2),
    _Gs2328GVRPConfPortMode_Type()
)
gs2328GVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GVRPConfPortMode.setStatus("current")


class _Gs2328GVRPConfPortRRole_Type(Integer32):
    """Custom type gs2328GVRPConfPortRRole based on Integer32"""
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


_Gs2328GVRPConfPortRRole_Type.__name__ = "Integer32"
_Gs2328GVRPConfPortRRole_Object = MibTableColumn
gs2328GVRPConfPortRRole = _Gs2328GVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 1, 2, 1, 3),
    _Gs2328GVRPConfPortRRole_Type()
)
gs2328GVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328GVRPConfPortRRole.setStatus("current")
_Gs2328GVRPStatisticsTable_Object = MibTable
gs2328GVRPStatisticsTable = _Gs2328GVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328GVRPStatisticsTable.setStatus("current")
_Gs2328GVRPStatisticsEntry_Object = MibTableRow
gs2328GVRPStatisticsEntry = _Gs2328GVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 2, 1)
)
gs2328GVRPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328GVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328GVRPStatisticsEntry.setStatus("current")


class _Gs2328GVRPStatisticsPort_Type(Integer32):
    """Custom type gs2328GVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328GVRPStatisticsPort_Type.__name__ = "Integer32"
_Gs2328GVRPStatisticsPort_Object = MibTableColumn
gs2328GVRPStatisticsPort = _Gs2328GVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 2, 1, 1),
    _Gs2328GVRPStatisticsPort_Type()
)
gs2328GVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328GVRPStatisticsPort.setStatus("current")
_Gs2328GVRPStatisticsJoinTxCnt_Type = Counter32
_Gs2328GVRPStatisticsJoinTxCnt_Object = MibTableColumn
gs2328GVRPStatisticsJoinTxCnt = _Gs2328GVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 2, 1, 2),
    _Gs2328GVRPStatisticsJoinTxCnt_Type()
)
gs2328GVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328GVRPStatisticsJoinTxCnt.setStatus("current")
_Gs2328GVRPStatisticsLeaveTxCnt_Type = Counter32
_Gs2328GVRPStatisticsLeaveTxCnt_Object = MibTableColumn
gs2328GVRPStatisticsLeaveTxCnt = _Gs2328GVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 4, 2, 1, 3),
    _Gs2328GVRPStatisticsLeaveTxCnt_Type()
)
gs2328GVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328GVRPStatisticsLeaveTxCnt.setStatus("current")
_Gs2328Mirroring_ObjectIdentity = ObjectIdentity
gs2328Mirroring = _Gs2328Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 6)
)


class _Gs2328PortToMirrorOn_Type(Integer32):
    """Custom type gs2328PortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2328PortToMirrorOn_Type.__name__ = "Integer32"
_Gs2328PortToMirrorOn_Object = MibScalar
gs2328PortToMirrorOn = _Gs2328PortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 6, 1),
    _Gs2328PortToMirrorOn_Type()
)
gs2328PortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortToMirrorOn.setStatus("current")
_Gs2328MirrorTable_Object = MibTable
gs2328MirrorTable = _Gs2328MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328MirrorTable.setStatus("current")
_Gs2328MirrorEntry_Object = MibTableRow
gs2328MirrorEntry = _Gs2328MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 6, 2, 1)
)
gs2328MirrorEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MirrorPort"),
)
if mibBuilder.loadTexts:
    gs2328MirrorEntry.setStatus("current")


class _Gs2328MirrorPort_Type(Integer32):
    """Custom type gs2328MirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MirrorPort_Type.__name__ = "Integer32"
_Gs2328MirrorPort_Object = MibTableColumn
gs2328MirrorPort = _Gs2328MirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 6, 2, 1, 1),
    _Gs2328MirrorPort_Type()
)
gs2328MirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MirrorPort.setStatus("current")


class _Gs2328MirrorMode_Type(Integer32):
    """Custom type gs2328MirrorMode based on Integer32"""
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


_Gs2328MirrorMode_Type.__name__ = "Integer32"
_Gs2328MirrorMode_Object = MibTableColumn
gs2328MirrorMode = _Gs2328MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 6, 2, 1, 2),
    _Gs2328MirrorMode_Type()
)
gs2328MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MirrorMode.setStatus("current")
_Gs2328TrapEventSeverity_ObjectIdentity = ObjectIdentity
gs2328TrapEventSeverity = _Gs2328TrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7)
)


class _Gs2328TrapEventSeverityACL_Type(Integer32):
    """Custom type gs2328TrapEventSeverityACL based on Integer32"""
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


_Gs2328TrapEventSeverityACL_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityACL_Object = MibScalar
gs2328TrapEventSeverityACL = _Gs2328TrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 1),
    _Gs2328TrapEventSeverityACL_Type()
)
gs2328TrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityACL.setStatus("current")


class _Gs2328TrapEventSeverityACLLog_Type(Integer32):
    """Custom type gs2328TrapEventSeverityACLLog based on Integer32"""
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


_Gs2328TrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityACLLog_Object = MibScalar
gs2328TrapEventSeverityACLLog = _Gs2328TrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 2),
    _Gs2328TrapEventSeverityACLLog_Type()
)
gs2328TrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityACLLog.setStatus("current")


class _Gs2328TrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type gs2328TrapEventSeverityAccessMgmt based on Integer32"""
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


_Gs2328TrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityAccessMgmt_Object = MibScalar
gs2328TrapEventSeverityAccessMgmt = _Gs2328TrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 3),
    _Gs2328TrapEventSeverityAccessMgmt_Type()
)
gs2328TrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityAccessMgmt.setStatus("current")


class _Gs2328TrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type gs2328TrapEventSeverityAuthFailed based on Integer32"""
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


_Gs2328TrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityAuthFailed_Object = MibScalar
gs2328TrapEventSeverityAuthFailed = _Gs2328TrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 4),
    _Gs2328TrapEventSeverityAuthFailed_Type()
)
gs2328TrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityAuthFailed.setStatus("current")


class _Gs2328TrapEventSeverityColdStart_Type(Integer32):
    """Custom type gs2328TrapEventSeverityColdStart based on Integer32"""
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


_Gs2328TrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityColdStart_Object = MibScalar
gs2328TrapEventSeverityColdStart = _Gs2328TrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 5),
    _Gs2328TrapEventSeverityColdStart_Type()
)
gs2328TrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityColdStart.setStatus("current")


class _Gs2328TrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type gs2328TrapEventSeverityConfigInfo based on Integer32"""
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


_Gs2328TrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityConfigInfo_Object = MibScalar
gs2328TrapEventSeverityConfigInfo = _Gs2328TrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 6),
    _Gs2328TrapEventSeverityConfigInfo_Type()
)
gs2328TrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityConfigInfo.setStatus("current")


class _Gs2328TrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type gs2328TrapEventSeverityFirmwareUpgrade based on Integer32"""
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


_Gs2328TrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityFirmwareUpgrade_Object = MibScalar
gs2328TrapEventSeverityFirmwareUpgrade = _Gs2328TrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 7),
    _Gs2328TrapEventSeverityFirmwareUpgrade_Type()
)
gs2328TrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Gs2328TrapEventSeverityImportExport_Type(Integer32):
    """Custom type gs2328TrapEventSeverityImportExport based on Integer32"""
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


_Gs2328TrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityImportExport_Object = MibScalar
gs2328TrapEventSeverityImportExport = _Gs2328TrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 8),
    _Gs2328TrapEventSeverityImportExport_Type()
)
gs2328TrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityImportExport.setStatus("current")


class _Gs2328TrapEventSeverityLACP_Type(Integer32):
    """Custom type gs2328TrapEventSeverityLACP based on Integer32"""
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


_Gs2328TrapEventSeverityLACP_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityLACP_Object = MibScalar
gs2328TrapEventSeverityLACP = _Gs2328TrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 9),
    _Gs2328TrapEventSeverityLACP_Type()
)
gs2328TrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityLACP.setStatus("current")


class _Gs2328TrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type gs2328TrapEventSeverityLinkStatus based on Integer32"""
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


_Gs2328TrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityLinkStatus_Object = MibScalar
gs2328TrapEventSeverityLinkStatus = _Gs2328TrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 10),
    _Gs2328TrapEventSeverityLinkStatus_Type()
)
gs2328TrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityLinkStatus.setStatus("current")


class _Gs2328TrapEventSeverityLogin_Type(Integer32):
    """Custom type gs2328TrapEventSeverityLogin based on Integer32"""
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


_Gs2328TrapEventSeverityLogin_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityLogin_Object = MibScalar
gs2328TrapEventSeverityLogin = _Gs2328TrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 11),
    _Gs2328TrapEventSeverityLogin_Type()
)
gs2328TrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityLogin.setStatus("current")


class _Gs2328TrapEventSeverityLogout_Type(Integer32):
    """Custom type gs2328TrapEventSeverityLogout based on Integer32"""
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


_Gs2328TrapEventSeverityLogout_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityLogout_Object = MibScalar
gs2328TrapEventSeverityLogout = _Gs2328TrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 12),
    _Gs2328TrapEventSeverityLogout_Type()
)
gs2328TrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityLogout.setStatus("current")


class _Gs2328TrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type gs2328TrapEventSeverityLoopProtect based on Integer32"""
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


_Gs2328TrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityLoopProtect_Object = MibScalar
gs2328TrapEventSeverityLoopProtect = _Gs2328TrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 13),
    _Gs2328TrapEventSeverityLoopProtect_Type()
)
gs2328TrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityLoopProtect.setStatus("current")


class _Gs2328TrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type gs2328TrapEventSeverityMgmtIPChange based on Integer32"""
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


_Gs2328TrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityMgmtIPChange_Object = MibScalar
gs2328TrapEventSeverityMgmtIPChange = _Gs2328TrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 14),
    _Gs2328TrapEventSeverityMgmtIPChange_Type()
)
gs2328TrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityMgmtIPChange.setStatus("current")


class _Gs2328TrapEventSeverityModuleChange_Type(Integer32):
    """Custom type gs2328TrapEventSeverityModuleChange based on Integer32"""
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


_Gs2328TrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityModuleChange_Object = MibScalar
gs2328TrapEventSeverityModuleChange = _Gs2328TrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 15),
    _Gs2328TrapEventSeverityModuleChange_Type()
)
gs2328TrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityModuleChange.setStatus("current")


class _Gs2328TrapEventSeverityNAS_Type(Integer32):
    """Custom type gs2328TrapEventSeverityNAS based on Integer32"""
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


_Gs2328TrapEventSeverityNAS_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityNAS_Object = MibScalar
gs2328TrapEventSeverityNAS = _Gs2328TrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 16),
    _Gs2328TrapEventSeverityNAS_Type()
)
gs2328TrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityNAS.setStatus("current")


class _Gs2328TrapEventSeverityPasswordChange_Type(Integer32):
    """Custom type gs2328TrapEventSeverityPasswordChange based on Integer32"""
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


_Gs2328TrapEventSeverityPasswordChange_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityPasswordChange_Object = MibScalar
gs2328TrapEventSeverityPasswordChange = _Gs2328TrapEventSeverityPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 17),
    _Gs2328TrapEventSeverityPasswordChange_Type()
)
gs2328TrapEventSeverityPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityPasswordChange.setStatus("current")


class _Gs2328TrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type gs2328TrapEventSeverityPortSecurity based on Integer32"""
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


_Gs2328TrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityPortSecurity_Object = MibScalar
gs2328TrapEventSeverityPortSecurity = _Gs2328TrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 18),
    _Gs2328TrapEventSeverityPortSecurity_Type()
)
gs2328TrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityPortSecurity.setStatus("current")


class _Gs2328TrapEventSeverityVLAN_Type(Integer32):
    """Custom type gs2328TrapEventSeverityVLAN based on Integer32"""
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


_Gs2328TrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityVLAN_Object = MibScalar
gs2328TrapEventSeverityVLAN = _Gs2328TrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 20),
    _Gs2328TrapEventSeverityVLAN_Type()
)
gs2328TrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityVLAN.setStatus("current")


class _Gs2328TrapEventSeverityWarmStart_Type(Integer32):
    """Custom type gs2328TrapEventSeverityWarmStart based on Integer32"""
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


_Gs2328TrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityWarmStart_Object = MibScalar
gs2328TrapEventSeverityWarmStart = _Gs2328TrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 21),
    _Gs2328TrapEventSeverityWarmStart_Type()
)
gs2328TrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityWarmStart.setStatus("current")


class _Gs2328TrapEventSeverityARPConflict_Type(Integer32):
    """Custom type gs2328TrapEventSeverityARPConflict based on Integer32"""
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


_Gs2328TrapEventSeverityARPConflict_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityARPConflict_Object = MibScalar
gs2328TrapEventSeverityARPConflict = _Gs2328TrapEventSeverityARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 25),
    _Gs2328TrapEventSeverityARPConflict_Type()
)
gs2328TrapEventSeverityARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityARPConflict.setStatus("current")


class _Gs2328TrapEventSeveritySpoofingLimit_Type(Integer32):
    """Custom type gs2328TrapEventSeveritySpoofingLimit based on Integer32"""
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


_Gs2328TrapEventSeveritySpoofingLimit_Type.__name__ = "Integer32"
_Gs2328TrapEventSeveritySpoofingLimit_Object = MibScalar
gs2328TrapEventSeveritySpoofingLimit = _Gs2328TrapEventSeveritySpoofingLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 27),
    _Gs2328TrapEventSeveritySpoofingLimit_Type()
)
gs2328TrapEventSeveritySpoofingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeveritySpoofingLimit.setStatus("current")


class _Gs2328TrapEventSeverityStaticARPConflict_Type(Integer32):
    """Custom type gs2328TrapEventSeverityStaticARPConflict based on Integer32"""
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


_Gs2328TrapEventSeverityStaticARPConflict_Type.__name__ = "Integer32"
_Gs2328TrapEventSeverityStaticARPConflict_Object = MibScalar
gs2328TrapEventSeverityStaticARPConflict = _Gs2328TrapEventSeverityStaticARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 7, 28),
    _Gs2328TrapEventSeverityStaticARPConflict_Type()
)
gs2328TrapEventSeverityStaticARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TrapEventSeverityStaticARPConflict.setStatus("current")
_Gs2328SMTP_ObjectIdentity = ObjectIdentity
gs2328SMTP = _Gs2328SMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8)
)
_Gs2328SMTPMailServer_Type = DisplayString
_Gs2328SMTPMailServer_Object = MibScalar
gs2328SMTPMailServer = _Gs2328SMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 1),
    _Gs2328SMTPMailServer_Type()
)
gs2328SMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPMailServer.setStatus("current")
_Gs2328SMTPUserName_Type = DisplayString
_Gs2328SMTPUserName_Object = MibScalar
gs2328SMTPUserName = _Gs2328SMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 2),
    _Gs2328SMTPUserName_Type()
)
gs2328SMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPUserName.setStatus("current")
_Gs2328SMTPPassword_Type = DisplayString
_Gs2328SMTPPassword_Object = MibScalar
gs2328SMTPPassword = _Gs2328SMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 3),
    _Gs2328SMTPPassword_Type()
)
gs2328SMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPPassword.setStatus("current")


class _Gs2328SMTPServeriryLevel_Type(Integer32):
    """Custom type gs2328SMTPServeriryLevel based on Integer32"""
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


_Gs2328SMTPServeriryLevel_Type.__name__ = "Integer32"
_Gs2328SMTPServeriryLevel_Object = MibScalar
gs2328SMTPServeriryLevel = _Gs2328SMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 4),
    _Gs2328SMTPServeriryLevel_Type()
)
gs2328SMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPServeriryLevel.setStatus("current")
_Gs2328SMTPSender_Type = DisplayString
_Gs2328SMTPSender_Object = MibScalar
gs2328SMTPSender = _Gs2328SMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 5),
    _Gs2328SMTPSender_Type()
)
gs2328SMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPSender.setStatus("current")
_Gs2328SMTPReturnPath_Type = DisplayString
_Gs2328SMTPReturnPath_Object = MibScalar
gs2328SMTPReturnPath = _Gs2328SMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 6),
    _Gs2328SMTPReturnPath_Type()
)
gs2328SMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPReturnPath.setStatus("current")
_Gs2328SMTPEmailAddress1_Type = DisplayString
_Gs2328SMTPEmailAddress1_Object = MibScalar
gs2328SMTPEmailAddress1 = _Gs2328SMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 7),
    _Gs2328SMTPEmailAddress1_Type()
)
gs2328SMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPEmailAddress1.setStatus("current")
_Gs2328SMTPEmailAddress2_Type = DisplayString
_Gs2328SMTPEmailAddress2_Object = MibScalar
gs2328SMTPEmailAddress2 = _Gs2328SMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 8),
    _Gs2328SMTPEmailAddress2_Type()
)
gs2328SMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPEmailAddress2.setStatus("current")
_Gs2328SMTPEmailAddress3_Type = DisplayString
_Gs2328SMTPEmailAddress3_Object = MibScalar
gs2328SMTPEmailAddress3 = _Gs2328SMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 9),
    _Gs2328SMTPEmailAddress3_Type()
)
gs2328SMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPEmailAddress3.setStatus("current")
_Gs2328SMTPEmailAddress4_Type = DisplayString
_Gs2328SMTPEmailAddress4_Object = MibScalar
gs2328SMTPEmailAddress4 = _Gs2328SMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 10),
    _Gs2328SMTPEmailAddress4_Type()
)
gs2328SMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPEmailAddress4.setStatus("current")
_Gs2328SMTPEmailAddress5_Type = DisplayString
_Gs2328SMTPEmailAddress5_Object = MibScalar
gs2328SMTPEmailAddress5 = _Gs2328SMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 11),
    _Gs2328SMTPEmailAddress5_Type()
)
gs2328SMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPEmailAddress5.setStatus("current")
_Gs2328SMTPEmailAddress6_Type = DisplayString
_Gs2328SMTPEmailAddress6_Object = MibScalar
gs2328SMTPEmailAddress6 = _Gs2328SMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 8, 12),
    _Gs2328SMTPEmailAddress6_Type()
)
gs2328SMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SMTPEmailAddress6.setStatus("current")
_Gs2328ACL_ObjectIdentity = ObjectIdentity
gs2328ACL = _Gs2328ACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9)
)
_Gs2328ACLPortsConfTable_Object = MibTable
gs2328ACLPortsConfTable = _Gs2328ACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1)
)
if mibBuilder.loadTexts:
    gs2328ACLPortsConfTable.setStatus("current")
_Gs2328ACLPortsConfEntry_Object = MibTableRow
gs2328ACLPortsConfEntry = _Gs2328ACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1)
)
gs2328ACLPortsConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    gs2328ACLPortsConfEntry.setStatus("current")


class _Gs2328ACLPortsConfPort_Type(Integer32):
    """Custom type gs2328ACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ACLPortsConfPort_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfPort_Object = MibTableColumn
gs2328ACLPortsConfPort = _Gs2328ACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 1),
    _Gs2328ACLPortsConfPort_Type()
)
gs2328ACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfPort.setStatus("current")


class _Gs2328ACLPortsConfPolicyID_Type(Integer32):
    """Custom type gs2328ACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328ACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfPolicyID_Object = MibTableColumn
gs2328ACLPortsConfPolicyID = _Gs2328ACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 2),
    _Gs2328ACLPortsConfPolicyID_Type()
)
gs2328ACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfPolicyID.setStatus("current")


class _Gs2328ACLPortsConfAction_Type(Integer32):
    """Custom type gs2328ACLPortsConfAction based on Integer32"""
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


_Gs2328ACLPortsConfAction_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfAction_Object = MibTableColumn
gs2328ACLPortsConfAction = _Gs2328ACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 3),
    _Gs2328ACLPortsConfAction_Type()
)
gs2328ACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfAction.setStatus("current")


class _Gs2328ACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type gs2328ACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2328ACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfRateLimiterID_Object = MibTableColumn
gs2328ACLPortsConfRateLimiterID = _Gs2328ACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 4),
    _Gs2328ACLPortsConfRateLimiterID_Type()
)
gs2328ACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfRateLimiterID.setStatus("current")


class _Gs2328ACLPortsConfPortRedirect_Type(Integer32):
    """Custom type gs2328ACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gs2328ACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfPortRedirect_Object = MibTableColumn
gs2328ACLPortsConfPortRedirect = _Gs2328ACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 5),
    _Gs2328ACLPortsConfPortRedirect_Type()
)
gs2328ACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfPortRedirect.setStatus("current")


class _Gs2328ACLPortsConfMirror_Type(Integer32):
    """Custom type gs2328ACLPortsConfMirror based on Integer32"""
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


_Gs2328ACLPortsConfMirror_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfMirror_Object = MibTableColumn
gs2328ACLPortsConfMirror = _Gs2328ACLPortsConfMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 6),
    _Gs2328ACLPortsConfMirror_Type()
)
gs2328ACLPortsConfMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfMirror.setStatus("current")


class _Gs2328ACLPortsConfLogging_Type(Integer32):
    """Custom type gs2328ACLPortsConfLogging based on Integer32"""
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


_Gs2328ACLPortsConfLogging_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfLogging_Object = MibTableColumn
gs2328ACLPortsConfLogging = _Gs2328ACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 7),
    _Gs2328ACLPortsConfLogging_Type()
)
gs2328ACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfLogging.setStatus("current")


class _Gs2328ACLPortsConfShutdown_Type(Integer32):
    """Custom type gs2328ACLPortsConfShutdown based on Integer32"""
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


_Gs2328ACLPortsConfShutdown_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfShutdown_Object = MibTableColumn
gs2328ACLPortsConfShutdown = _Gs2328ACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 8),
    _Gs2328ACLPortsConfShutdown_Type()
)
gs2328ACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfShutdown.setStatus("current")


class _Gs2328ACLPortsConfState_Type(Integer32):
    """Custom type gs2328ACLPortsConfState based on Integer32"""
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


_Gs2328ACLPortsConfState_Type.__name__ = "Integer32"
_Gs2328ACLPortsConfState_Object = MibTableColumn
gs2328ACLPortsConfState = _Gs2328ACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 9),
    _Gs2328ACLPortsConfState_Type()
)
gs2328ACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfState.setStatus("current")
_Gs2328ACLPortsConfCounter_Type = Counter32
_Gs2328ACLPortsConfCounter_Object = MibTableColumn
gs2328ACLPortsConfCounter = _Gs2328ACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 1, 1, 10),
    _Gs2328ACLPortsConfCounter_Type()
)
gs2328ACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLPortsConfCounter.setStatus("current")
_Gs2328ACLRateLimiterTable_Object = MibTable
gs2328ACLRateLimiterTable = _Gs2328ACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 2)
)
if mibBuilder.loadTexts:
    gs2328ACLRateLimiterTable.setStatus("current")
_Gs2328ACLRateLimiterEntry_Object = MibTableRow
gs2328ACLRateLimiterEntry = _Gs2328ACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 2, 1)
)
gs2328ACLRateLimiterEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    gs2328ACLRateLimiterEntry.setStatus("current")


class _Gs2328ACLRateLimiterID_Type(Integer32):
    """Custom type gs2328ACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2328ACLRateLimiterID_Type.__name__ = "Integer32"
_Gs2328ACLRateLimiterID_Object = MibTableColumn
gs2328ACLRateLimiterID = _Gs2328ACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 2, 1, 1),
    _Gs2328ACLRateLimiterID_Type()
)
gs2328ACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ACLRateLimiterID.setStatus("current")


class _Gs2328ACLRateLimiterUnit_Type(Integer32):
    """Custom type gs2328ACLRateLimiterUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pps", 0),
          ("kbps", 1))
    )


_Gs2328ACLRateLimiterUnit_Type.__name__ = "Integer32"
_Gs2328ACLRateLimiterUnit_Object = MibTableColumn
gs2328ACLRateLimiterUnit = _Gs2328ACLRateLimiterUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 2, 1, 2),
    _Gs2328ACLRateLimiterUnit_Type()
)
gs2328ACLRateLimiterUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLRateLimiterUnit.setStatus("current")


class _Gs2328ACLRateLimiterRate_Type(Integer32):
    """Custom type gs2328ACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Gs2328ACLRateLimiterRate_Type.__name__ = "Integer32"
_Gs2328ACLRateLimiterRate_Object = MibTableColumn
gs2328ACLRateLimiterRate = _Gs2328ACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 2, 1, 3),
    _Gs2328ACLRateLimiterRate_Type()
)
gs2328ACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLRateLimiterRate.setStatus("current")
_Gs2328ACLACE_ObjectIdentity = ObjectIdentity
gs2328ACLACE = _Gs2328ACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3)
)


class _Gs2328ACLACECreate_Type(Integer32):
    """Custom type gs2328ACLACECreate based on Integer32"""
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


_Gs2328ACLACECreate_Type.__name__ = "Integer32"
_Gs2328ACLACECreate_Object = MibScalar
gs2328ACLACECreate = _Gs2328ACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 1),
    _Gs2328ACLACECreate_Type()
)
gs2328ACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACECreate.setStatus("current")
_Gs2328ACLACETable_Object = MibTable
gs2328ACLACETable = _Gs2328ACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328ACLACETable.setStatus("current")
_Gs2328ACLACEEntry_Object = MibTableRow
gs2328ACLACEEntry = _Gs2328ACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1)
)
gs2328ACLACEEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ACLACEIndex"),
)
if mibBuilder.loadTexts:
    gs2328ACLACEEntry.setStatus("current")


class _Gs2328ACLACEIndex_Type(Integer32):
    """Custom type gs2328ACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328ACLACEIndex_Type.__name__ = "Integer32"
_Gs2328ACLACEIndex_Object = MibTableColumn
gs2328ACLACEIndex = _Gs2328ACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 1),
    _Gs2328ACLACEIndex_Type()
)
gs2328ACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ACLACEIndex.setStatus("current")


class _Gs2328ACLACEID_Type(Integer32):
    """Custom type gs2328ACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328ACLACEID_Type.__name__ = "Integer32"
_Gs2328ACLACEID_Object = MibTableColumn
gs2328ACLACEID = _Gs2328ACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 2),
    _Gs2328ACLACEID_Type()
)
gs2328ACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEID.setStatus("current")


class _Gs2328ACLACENextID_Type(Integer32):
    """Custom type gs2328ACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328ACLACENextID_Type.__name__ = "Integer32"
_Gs2328ACLACENextID_Object = MibTableColumn
gs2328ACLACENextID = _Gs2328ACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 3),
    _Gs2328ACLACENextID_Type()
)
gs2328ACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACENextID.setStatus("current")
_Gs2328ACLACEIngressPort_Type = DisplayString
_Gs2328ACLACEIngressPort_Object = MibTableColumn
gs2328ACLACEIngressPort = _Gs2328ACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 4),
    _Gs2328ACLACEIngressPort_Type()
)
gs2328ACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEIngressPort.setStatus("current")


class _Gs2328ACLACEPortPolicyNumber_Type(Integer32):
    """Custom type gs2328ACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328ACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Gs2328ACLACEPortPolicyNumber_Object = MibTableColumn
gs2328ACLACEPortPolicyNumber = _Gs2328ACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 5),
    _Gs2328ACLACEPortPolicyNumber_Type()
)
gs2328ACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEPortPolicyNumber.setStatus("current")


class _Gs2328ACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type gs2328ACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328ACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Gs2328ACLACEPortPolicyBitmask_Object = MibTableColumn
gs2328ACLACEPortPolicyBitmask = _Gs2328ACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 6),
    _Gs2328ACLACEPortPolicyBitmask_Type()
)
gs2328ACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEPortPolicyBitmask.setStatus("current")


class _Gs2328ACLACEFrameType_Type(Integer32):
    """Custom type gs2328ACLACEFrameType based on Integer32"""
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


_Gs2328ACLACEFrameType_Type.__name__ = "Integer32"
_Gs2328ACLACEFrameType_Object = MibTableColumn
gs2328ACLACEFrameType = _Gs2328ACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 7),
    _Gs2328ACLACEFrameType_Type()
)
gs2328ACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEFrameType.setStatus("current")


class _Gs2328ACLACEAction_Type(Integer32):
    """Custom type gs2328ACLACEAction based on Integer32"""
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


_Gs2328ACLACEAction_Type.__name__ = "Integer32"
_Gs2328ACLACEAction_Object = MibTableColumn
gs2328ACLACEAction = _Gs2328ACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 8),
    _Gs2328ACLACEAction_Type()
)
gs2328ACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEAction.setStatus("current")
_Gs2328ACLACEDenyPortRedirect_Type = DisplayString
_Gs2328ACLACEDenyPortRedirect_Object = MibTableColumn
gs2328ACLACEDenyPortRedirect = _Gs2328ACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 9),
    _Gs2328ACLACEDenyPortRedirect_Type()
)
gs2328ACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDenyPortRedirect.setStatus("current")


class _Gs2328ACLACELogging_Type(Integer32):
    """Custom type gs2328ACLACELogging based on Integer32"""
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


_Gs2328ACLACELogging_Type.__name__ = "Integer32"
_Gs2328ACLACELogging_Object = MibTableColumn
gs2328ACLACELogging = _Gs2328ACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 10),
    _Gs2328ACLACELogging_Type()
)
gs2328ACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACELogging.setStatus("current")


class _Gs2328ACLACEMirror_Type(Integer32):
    """Custom type gs2328ACLACEMirror based on Integer32"""
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


_Gs2328ACLACEMirror_Type.__name__ = "Integer32"
_Gs2328ACLACEMirror_Object = MibTableColumn
gs2328ACLACEMirror = _Gs2328ACLACEMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 11),
    _Gs2328ACLACEMirror_Type()
)
gs2328ACLACEMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEMirror.setStatus("current")


class _Gs2328ACLACERateLimiter_Type(Integer32):
    """Custom type gs2328ACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2328ACLACERateLimiter_Type.__name__ = "Integer32"
_Gs2328ACLACERateLimiter_Object = MibTableColumn
gs2328ACLACERateLimiter = _Gs2328ACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 12),
    _Gs2328ACLACERateLimiter_Type()
)
gs2328ACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACERateLimiter.setStatus("current")


class _Gs2328ACLACEShutdown_Type(Integer32):
    """Custom type gs2328ACLACEShutdown based on Integer32"""
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


_Gs2328ACLACEShutdown_Type.__name__ = "Integer32"
_Gs2328ACLACEShutdown_Object = MibTableColumn
gs2328ACLACEShutdown = _Gs2328ACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 13),
    _Gs2328ACLACEShutdown_Type()
)
gs2328ACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEShutdown.setStatus("current")


class _Gs2328ACLACEVLAN8021QTagged_Type(Integer32):
    """Custom type gs2328ACLACEVLAN8021QTagged based on Integer32"""
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
          ("any", 2))
    )


_Gs2328ACLACEVLAN8021QTagged_Type.__name__ = "Integer32"
_Gs2328ACLACEVLAN8021QTagged_Object = MibTableColumn
gs2328ACLACEVLAN8021QTagged = _Gs2328ACLACEVLAN8021QTagged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 14),
    _Gs2328ACLACEVLAN8021QTagged_Type()
)
gs2328ACLACEVLAN8021QTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEVLAN8021QTagged.setStatus("current")


class _Gs2328ACLACEVLANTagPriority_Type(Integer32):
    """Custom type gs2328ACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2328ACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Gs2328ACLACEVLANTagPriority_Object = MibTableColumn
gs2328ACLACEVLANTagPriority = _Gs2328ACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 15),
    _Gs2328ACLACEVLANTagPriority_Type()
)
gs2328ACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEVLANTagPriority.setStatus("current")


class _Gs2328ACLACEVLANVID_Type(Integer32):
    """Custom type gs2328ACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328ACLACEVLANVID_Type.__name__ = "Integer32"
_Gs2328ACLACEVLANVID_Object = MibTableColumn
gs2328ACLACEVLANVID = _Gs2328ACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 16),
    _Gs2328ACLACEVLANVID_Type()
)
gs2328ACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEVLANVID.setStatus("current")


class _Gs2328ACLACEEtherType_Type(Integer32):
    """Custom type gs2328ACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328ACLACEEtherType_Type.__name__ = "Integer32"
_Gs2328ACLACEEtherType_Object = MibTableColumn
gs2328ACLACEEtherType = _Gs2328ACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 17),
    _Gs2328ACLACEEtherType_Type()
)
gs2328ACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEEtherType.setStatus("current")
_Gs2328ACLACESMAC_Type = DisplayString
_Gs2328ACLACESMAC_Object = MibTableColumn
gs2328ACLACESMAC = _Gs2328ACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 18),
    _Gs2328ACLACESMAC_Type()
)
gs2328ACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACESMAC.setStatus("current")


class _Gs2328ACLACEDMACType_Type(Integer32):
    """Custom type gs2328ACLACEDMACType based on Integer32"""
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
          ("macAddress", 4))
    )


_Gs2328ACLACEDMACType_Type.__name__ = "Integer32"
_Gs2328ACLACEDMACType_Object = MibTableColumn
gs2328ACLACEDMACType = _Gs2328ACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 19),
    _Gs2328ACLACEDMACType_Type()
)
gs2328ACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDMACType.setStatus("current")
_Gs2328ACLACEDMAC_Type = DisplayString
_Gs2328ACLACEDMAC_Object = MibTableColumn
gs2328ACLACEDMAC = _Gs2328ACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 20),
    _Gs2328ACLACEDMAC_Type()
)
gs2328ACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDMAC.setStatus("current")


class _Gs2328ACLACEArpOpcode_Type(Integer32):
    """Custom type gs2328ACLACEArpOpcode based on Integer32"""
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


_Gs2328ACLACEArpOpcode_Type.__name__ = "Integer32"
_Gs2328ACLACEArpOpcode_Object = MibTableColumn
gs2328ACLACEArpOpcode = _Gs2328ACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 21),
    _Gs2328ACLACEArpOpcode_Type()
)
gs2328ACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpOpcode.setStatus("current")


class _Gs2328ACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type gs2328ACLACEArpFlagsRequestReply based on Integer32"""
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


_Gs2328ACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Gs2328ACLACEArpFlagsRequestReply_Object = MibTableColumn
gs2328ACLACEArpFlagsRequestReply = _Gs2328ACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 22),
    _Gs2328ACLACEArpFlagsRequestReply_Type()
)
gs2328ACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpFlagsRequestReply.setStatus("current")


class _Gs2328ACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type gs2328ACLACEArpFlagsArpSmac based on Integer32"""
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


_Gs2328ACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Gs2328ACLACEArpFlagsArpSmac_Object = MibTableColumn
gs2328ACLACEArpFlagsArpSmac = _Gs2328ACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 23),
    _Gs2328ACLACEArpFlagsArpSmac_Type()
)
gs2328ACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpFlagsArpSmac.setStatus("current")


class _Gs2328ACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type gs2328ACLACEArpFlagsRarpDmac based on Integer32"""
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


_Gs2328ACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Gs2328ACLACEArpFlagsRarpDmac_Object = MibTableColumn
gs2328ACLACEArpFlagsRarpDmac = _Gs2328ACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 24),
    _Gs2328ACLACEArpFlagsRarpDmac_Type()
)
gs2328ACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpFlagsRarpDmac.setStatus("current")


class _Gs2328ACLACEArpFlagsLength_Type(Integer32):
    """Custom type gs2328ACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328ACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Gs2328ACLACEArpFlagsLength_Object = MibTableColumn
gs2328ACLACEArpFlagsLength = _Gs2328ACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 25),
    _Gs2328ACLACEArpFlagsLength_Type()
)
gs2328ACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpFlagsLength.setStatus("current")


class _Gs2328ACLACEArpFlagsIp_Type(Integer32):
    """Custom type gs2328ACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328ACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Gs2328ACLACEArpFlagsIp_Object = MibTableColumn
gs2328ACLACEArpFlagsIp = _Gs2328ACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 26),
    _Gs2328ACLACEArpFlagsIp_Type()
)
gs2328ACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpFlagsIp.setStatus("current")


class _Gs2328ACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type gs2328ACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328ACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Gs2328ACLACEArpFlagsEthernet_Object = MibTableColumn
gs2328ACLACEArpFlagsEthernet = _Gs2328ACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 27),
    _Gs2328ACLACEArpFlagsEthernet_Type()
)
gs2328ACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEArpFlagsEthernet.setStatus("current")


class _Gs2328ACLACESIPType_Type(Integer32):
    """Custom type gs2328ACLACESIPType based on Integer32"""
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


_Gs2328ACLACESIPType_Type.__name__ = "Integer32"
_Gs2328ACLACESIPType_Object = MibTableColumn
gs2328ACLACESIPType = _Gs2328ACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 28),
    _Gs2328ACLACESIPType_Type()
)
gs2328ACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACESIPType.setStatus("current")
_Gs2328ACLACESIPIPAddress_Type = IpAddress
_Gs2328ACLACESIPIPAddress_Object = MibTableColumn
gs2328ACLACESIPIPAddress = _Gs2328ACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 29),
    _Gs2328ACLACESIPIPAddress_Type()
)
gs2328ACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACESIPIPAddress.setStatus("current")


class _Gs2328ACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type gs2328ACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2328ACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2328ACLACESIPNetworkPrefix_Object = MibTableColumn
gs2328ACLACESIPNetworkPrefix = _Gs2328ACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 30),
    _Gs2328ACLACESIPNetworkPrefix_Type()
)
gs2328ACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACESIPNetworkPrefix.setStatus("current")


class _Gs2328ACLACEDIPType_Type(Integer32):
    """Custom type gs2328ACLACEDIPType based on Integer32"""
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


_Gs2328ACLACEDIPType_Type.__name__ = "Integer32"
_Gs2328ACLACEDIPType_Object = MibTableColumn
gs2328ACLACEDIPType = _Gs2328ACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 32),
    _Gs2328ACLACEDIPType_Type()
)
gs2328ACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDIPType.setStatus("current")
_Gs2328ACLACEDIPIPAddress_Type = IpAddress
_Gs2328ACLACEDIPIPAddress_Object = MibTableColumn
gs2328ACLACEDIPIPAddress = _Gs2328ACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 33),
    _Gs2328ACLACEDIPIPAddress_Type()
)
gs2328ACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDIPIPAddress.setStatus("current")


class _Gs2328ACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type gs2328ACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2328ACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2328ACLACEDIPNetworkPrefix_Object = MibTableColumn
gs2328ACLACEDIPNetworkPrefix = _Gs2328ACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 34),
    _Gs2328ACLACEDIPNetworkPrefix_Type()
)
gs2328ACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDIPNetworkPrefix.setStatus("current")


class _Gs2328ACLACEIPProtocol_Type(Integer32):
    """Custom type gs2328ACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2328ACLACEIPProtocol_Type.__name__ = "Integer32"
_Gs2328ACLACEIPProtocol_Object = MibTableColumn
gs2328ACLACEIPProtocol = _Gs2328ACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 36),
    _Gs2328ACLACEIPProtocol_Type()
)
gs2328ACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEIPProtocol.setStatus("current")


class _Gs2328ACLACEIPFlagsTTL_Type(Integer32):
    """Custom type gs2328ACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328ACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Gs2328ACLACEIPFlagsTTL_Object = MibTableColumn
gs2328ACLACEIPFlagsTTL = _Gs2328ACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 37),
    _Gs2328ACLACEIPFlagsTTL_Type()
)
gs2328ACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEIPFlagsTTL.setStatus("current")


class _Gs2328ACLACEIPFlagsOptions_Type(Integer32):
    """Custom type gs2328ACLACEIPFlagsOptions based on Integer32"""
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


_Gs2328ACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Gs2328ACLACEIPFlagsOptions_Object = MibTableColumn
gs2328ACLACEIPFlagsOptions = _Gs2328ACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 38),
    _Gs2328ACLACEIPFlagsOptions_Type()
)
gs2328ACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEIPFlagsOptions.setStatus("current")


class _Gs2328ACLACEIPFlagsFragment_Type(Integer32):
    """Custom type gs2328ACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328ACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Gs2328ACLACEIPFlagsFragment_Object = MibTableColumn
gs2328ACLACEIPFlagsFragment = _Gs2328ACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 39),
    _Gs2328ACLACEIPFlagsFragment_Type()
)
gs2328ACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEIPFlagsFragment.setStatus("current")


class _Gs2328ACLACEICMPType_Type(Integer32):
    """Custom type gs2328ACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2328ACLACEICMPType_Type.__name__ = "Integer32"
_Gs2328ACLACEICMPType_Object = MibTableColumn
gs2328ACLACEICMPType = _Gs2328ACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 40),
    _Gs2328ACLACEICMPType_Type()
)
gs2328ACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEICMPType.setStatus("current")


class _Gs2328ACLACEICMPCode_Type(Integer32):
    """Custom type gs2328ACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2328ACLACEICMPCode_Type.__name__ = "Integer32"
_Gs2328ACLACEICMPCode_Object = MibTableColumn
gs2328ACLACEICMPCode = _Gs2328ACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 41),
    _Gs2328ACLACEICMPCode_Type()
)
gs2328ACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEICMPCode.setStatus("current")


class _Gs2328ACLACESourcePortMin_Type(Integer32):
    """Custom type gs2328ACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328ACLACESourcePortMin_Type.__name__ = "Integer32"
_Gs2328ACLACESourcePortMin_Object = MibTableColumn
gs2328ACLACESourcePortMin = _Gs2328ACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 42),
    _Gs2328ACLACESourcePortMin_Type()
)
gs2328ACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACESourcePortMin.setStatus("current")


class _Gs2328ACLACESourcePortMax_Type(Integer32):
    """Custom type gs2328ACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328ACLACESourcePortMax_Type.__name__ = "Integer32"
_Gs2328ACLACESourcePortMax_Object = MibTableColumn
gs2328ACLACESourcePortMax = _Gs2328ACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 43),
    _Gs2328ACLACESourcePortMax_Type()
)
gs2328ACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACESourcePortMax.setStatus("current")


class _Gs2328ACLACEDestPortMin_Type(Integer32):
    """Custom type gs2328ACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328ACLACEDestPortMin_Type.__name__ = "Integer32"
_Gs2328ACLACEDestPortMin_Object = MibTableColumn
gs2328ACLACEDestPortMin = _Gs2328ACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 44),
    _Gs2328ACLACEDestPortMin_Type()
)
gs2328ACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDestPortMin.setStatus("current")


class _Gs2328ACLACEDestPortMax_Type(Integer32):
    """Custom type gs2328ACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328ACLACEDestPortMax_Type.__name__ = "Integer32"
_Gs2328ACLACEDestPortMax_Object = MibTableColumn
gs2328ACLACEDestPortMax = _Gs2328ACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 45),
    _Gs2328ACLACEDestPortMax_Type()
)
gs2328ACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEDestPortMax.setStatus("current")


class _Gs2328ACLACETCPFlagsFin_Type(Integer32):
    """Custom type gs2328ACLACETCPFlagsFin based on Integer32"""
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


_Gs2328ACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Gs2328ACLACETCPFlagsFin_Object = MibTableColumn
gs2328ACLACETCPFlagsFin = _Gs2328ACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 46),
    _Gs2328ACLACETCPFlagsFin_Type()
)
gs2328ACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACETCPFlagsFin.setStatus("current")


class _Gs2328ACLACETCPFlagsSyn_Type(Integer32):
    """Custom type gs2328ACLACETCPFlagsSyn based on Integer32"""
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


_Gs2328ACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Gs2328ACLACETCPFlagsSyn_Object = MibTableColumn
gs2328ACLACETCPFlagsSyn = _Gs2328ACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 47),
    _Gs2328ACLACETCPFlagsSyn_Type()
)
gs2328ACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACETCPFlagsSyn.setStatus("current")


class _Gs2328ACLACETCPFlagsRst_Type(Integer32):
    """Custom type gs2328ACLACETCPFlagsRst based on Integer32"""
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


_Gs2328ACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Gs2328ACLACETCPFlagsRst_Object = MibTableColumn
gs2328ACLACETCPFlagsRst = _Gs2328ACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 48),
    _Gs2328ACLACETCPFlagsRst_Type()
)
gs2328ACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACETCPFlagsRst.setStatus("current")


class _Gs2328ACLACETCPFlagsPsh_Type(Integer32):
    """Custom type gs2328ACLACETCPFlagsPsh based on Integer32"""
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


_Gs2328ACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Gs2328ACLACETCPFlagsPsh_Object = MibTableColumn
gs2328ACLACETCPFlagsPsh = _Gs2328ACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 49),
    _Gs2328ACLACETCPFlagsPsh_Type()
)
gs2328ACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACETCPFlagsPsh.setStatus("current")


class _Gs2328ACLACETCPFlagsAck_Type(Integer32):
    """Custom type gs2328ACLACETCPFlagsAck based on Integer32"""
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


_Gs2328ACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Gs2328ACLACETCPFlagsAck_Object = MibTableColumn
gs2328ACLACETCPFlagsAck = _Gs2328ACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 50),
    _Gs2328ACLACETCPFlagsAck_Type()
)
gs2328ACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACETCPFlagsAck.setStatus("current")


class _Gs2328ACLACETCPFlagsUrg_Type(Integer32):
    """Custom type gs2328ACLACETCPFlagsUrg based on Integer32"""
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


_Gs2328ACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Gs2328ACLACETCPFlagsUrg_Object = MibTableColumn
gs2328ACLACETCPFlagsUrg = _Gs2328ACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 51),
    _Gs2328ACLACETCPFlagsUrg_Type()
)
gs2328ACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACETCPFlagsUrg.setStatus("current")


class _Gs2328ACLACERowStatus_Type(Integer32):
    """Custom type gs2328ACLACERowStatus based on Integer32"""
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


_Gs2328ACLACERowStatus_Type.__name__ = "Integer32"
_Gs2328ACLACERowStatus_Object = MibTableColumn
gs2328ACLACERowStatus = _Gs2328ACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 2, 1, 66),
    _Gs2328ACLACERowStatus_Type()
)
gs2328ACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACERowStatus.setStatus("current")


class _Gs2328ACLACEClear_Type(Integer32):
    """Custom type gs2328ACLACEClear based on Integer32"""
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


_Gs2328ACLACEClear_Type.__name__ = "Integer32"
_Gs2328ACLACEClear_Object = MibScalar
gs2328ACLACEClear = _Gs2328ACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 3),
    _Gs2328ACLACEClear_Type()
)
gs2328ACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEClear.setStatus("current")


class _Gs2328ACLACEMoveACEID_Type(Integer32):
    """Custom type gs2328ACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328ACLACEMoveACEID_Type.__name__ = "Integer32"
_Gs2328ACLACEMoveACEID_Object = MibScalar
gs2328ACLACEMoveACEID = _Gs2328ACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 4),
    _Gs2328ACLACEMoveACEID_Type()
)
gs2328ACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEMoveACEID.setStatus("current")


class _Gs2328ACLACEMoveNextACEID_Type(Integer32):
    """Custom type gs2328ACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328ACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Gs2328ACLACEMoveNextACEID_Object = MibScalar
gs2328ACLACEMoveNextACEID = _Gs2328ACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 5),
    _Gs2328ACLACEMoveNextACEID_Type()
)
gs2328ACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ACLACEMoveNextACEID.setStatus("current")
_Gs2328ACLACEStatusTable_Object = MibTable
gs2328ACLACEStatusTable = _Gs2328ACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    gs2328ACLACEStatusTable.setStatus("current")
_Gs2328ACLACEStatusEntry_Object = MibTableRow
gs2328ACLACEStatusEntry = _Gs2328ACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1)
)
gs2328ACLACEStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2328ACLACEStatusEntry.setStatus("current")


class _Gs2328ACLACEStatusIndex_Type(Integer32):
    """Custom type gs2328ACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328ACLACEStatusIndex_Type.__name__ = "Integer32"
_Gs2328ACLACEStatusIndex_Object = MibTableColumn
gs2328ACLACEStatusIndex = _Gs2328ACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 1),
    _Gs2328ACLACEStatusIndex_Type()
)
gs2328ACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusIndex.setStatus("current")
_Gs2328ACLACEStatusUser_Type = DisplayString
_Gs2328ACLACEStatusUser_Object = MibTableColumn
gs2328ACLACEStatusUser = _Gs2328ACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 2),
    _Gs2328ACLACEStatusUser_Type()
)
gs2328ACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusUser.setStatus("current")


class _Gs2328ACLACEStatusID_Type(Integer32):
    """Custom type gs2328ACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328ACLACEStatusID_Type.__name__ = "Integer32"
_Gs2328ACLACEStatusID_Object = MibTableColumn
gs2328ACLACEStatusID = _Gs2328ACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 3),
    _Gs2328ACLACEStatusID_Type()
)
gs2328ACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusID.setStatus("current")
_Gs2328ACLACEStatusIngressPort_Type = DisplayString
_Gs2328ACLACEStatusIngressPort_Object = MibTableColumn
gs2328ACLACEStatusIngressPort = _Gs2328ACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 4),
    _Gs2328ACLACEStatusIngressPort_Type()
)
gs2328ACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusIngressPort.setStatus("current")
_Gs2328ACLACEStatusFrameType_Type = DisplayString
_Gs2328ACLACEStatusFrameType_Object = MibTableColumn
gs2328ACLACEStatusFrameType = _Gs2328ACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 5),
    _Gs2328ACLACEStatusFrameType_Type()
)
gs2328ACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusFrameType.setStatus("current")
_Gs2328ACLACEStatusAction_Type = DisplayString
_Gs2328ACLACEStatusAction_Object = MibTableColumn
gs2328ACLACEStatusAction = _Gs2328ACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 6),
    _Gs2328ACLACEStatusAction_Type()
)
gs2328ACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusAction.setStatus("current")
_Gs2328ACLACEStatusRateLimiter_Type = DisplayString
_Gs2328ACLACEStatusRateLimiter_Object = MibTableColumn
gs2328ACLACEStatusRateLimiter = _Gs2328ACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 7),
    _Gs2328ACLACEStatusRateLimiter_Type()
)
gs2328ACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusRateLimiter.setStatus("current")
_Gs2328ACLACEStatusPortCopy_Type = DisplayString
_Gs2328ACLACEStatusPortCopy_Object = MibTableColumn
gs2328ACLACEStatusPortCopy = _Gs2328ACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 8),
    _Gs2328ACLACEStatusPortCopy_Type()
)
gs2328ACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusPortCopy.setStatus("current")
_Gs2328ACLACEStatusMirror_Type = DisplayString
_Gs2328ACLACEStatusMirror_Object = MibTableColumn
gs2328ACLACEStatusMirror = _Gs2328ACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 9),
    _Gs2328ACLACEStatusMirror_Type()
)
gs2328ACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusMirror.setStatus("current")
_Gs2328ACLACEStatusCPU_Type = DisplayString
_Gs2328ACLACEStatusCPU_Object = MibTableColumn
gs2328ACLACEStatusCPU = _Gs2328ACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 10),
    _Gs2328ACLACEStatusCPU_Type()
)
gs2328ACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusCPU.setStatus("current")
_Gs2328ACLACEStatusCounter_Type = Counter32
_Gs2328ACLACEStatusCounter_Object = MibTableColumn
gs2328ACLACEStatusCounter = _Gs2328ACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 11),
    _Gs2328ACLACEStatusCounter_Type()
)
gs2328ACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusCounter.setStatus("current")
_Gs2328ACLACEStatusConflict_Type = DisplayString
_Gs2328ACLACEStatusConflict_Object = MibTableColumn
gs2328ACLACEStatusConflict = _Gs2328ACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 9, 3, 6, 1, 12),
    _Gs2328ACLACEStatusConflict_Type()
)
gs2328ACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ACLACEStatusConflict.setStatus("current")
_Gs2328LoopProtection_ObjectIdentity = ObjectIdentity
gs2328LoopProtection = _Gs2328LoopProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12)
)
_Gs2328LoopProtectionConfig_ObjectIdentity = ObjectIdentity
gs2328LoopProtectionConfig = _Gs2328LoopProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1)
)


class _Gs2328LoopProtectionGlobalEnable_Type(Integer32):
    """Custom type gs2328LoopProtectionGlobalEnable based on Integer32"""
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


_Gs2328LoopProtectionGlobalEnable_Type.__name__ = "Integer32"
_Gs2328LoopProtectionGlobalEnable_Object = MibScalar
gs2328LoopProtectionGlobalEnable = _Gs2328LoopProtectionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 1),
    _Gs2328LoopProtectionGlobalEnable_Type()
)
gs2328LoopProtectionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectionGlobalEnable.setStatus("current")


class _Gs2328LoopProtectionTranmisstionTime_Type(Integer32):
    """Custom type gs2328LoopProtectionTranmisstionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328LoopProtectionTranmisstionTime_Type.__name__ = "Integer32"
_Gs2328LoopProtectionTranmisstionTime_Object = MibScalar
gs2328LoopProtectionTranmisstionTime = _Gs2328LoopProtectionTranmisstionTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 2),
    _Gs2328LoopProtectionTranmisstionTime_Type()
)
gs2328LoopProtectionTranmisstionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectionTranmisstionTime.setStatus("current")


class _Gs2328LoopProtectionShutdownTime_Type(Integer32):
    """Custom type gs2328LoopProtectionShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Gs2328LoopProtectionShutdownTime_Type.__name__ = "Integer32"
_Gs2328LoopProtectionShutdownTime_Object = MibScalar
gs2328LoopProtectionShutdownTime = _Gs2328LoopProtectionShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 3),
    _Gs2328LoopProtectionShutdownTime_Type()
)
gs2328LoopProtectionShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectionShutdownTime.setStatus("current")
_Gs2328LoopProtectionConfigurationTable_Object = MibTable
gs2328LoopProtectionConfigurationTable = _Gs2328LoopProtectionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    gs2328LoopProtectionConfigurationTable.setStatus("current")
_Gs2328LoopProtectionConfigurationEntry_Object = MibTableRow
gs2328LoopProtectionConfigurationEntry = _Gs2328LoopProtectionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 4, 1)
)
gs2328LoopProtectionConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328LoopProtectionConfPort"),
)
if mibBuilder.loadTexts:
    gs2328LoopProtectionConfigurationEntry.setStatus("current")


class _Gs2328LoopProtectionConfPort_Type(Integer32):
    """Custom type gs2328LoopProtectionConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328LoopProtectionConfPort_Type.__name__ = "Integer32"
_Gs2328LoopProtectionConfPort_Object = MibTableColumn
gs2328LoopProtectionConfPort = _Gs2328LoopProtectionConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 4, 1, 1),
    _Gs2328LoopProtectionConfPort_Type()
)
gs2328LoopProtectionConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328LoopProtectionConfPort.setStatus("current")


class _Gs2328LoopProtectionConfEnable_Type(Integer32):
    """Custom type gs2328LoopProtectionConfEnable based on Integer32"""
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


_Gs2328LoopProtectionConfEnable_Type.__name__ = "Integer32"
_Gs2328LoopProtectionConfEnable_Object = MibTableColumn
gs2328LoopProtectionConfEnable = _Gs2328LoopProtectionConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 4, 1, 2),
    _Gs2328LoopProtectionConfEnable_Type()
)
gs2328LoopProtectionConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectionConfEnable.setStatus("current")


class _Gs2328LoopProtectionConfAction_Type(Integer32):
    """Custom type gs2328LoopProtectionConfAction based on Integer32"""
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


_Gs2328LoopProtectionConfAction_Type.__name__ = "Integer32"
_Gs2328LoopProtectionConfAction_Object = MibTableColumn
gs2328LoopProtectionConfAction = _Gs2328LoopProtectionConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 4, 1, 3),
    _Gs2328LoopProtectionConfAction_Type()
)
gs2328LoopProtectionConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectionConfAction.setStatus("current")


class _Gs2328LoopProtectionConfTxmode_Type(Integer32):
    """Custom type gs2328LoopProtectionConfTxmode based on Integer32"""
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


_Gs2328LoopProtectionConfTxmode_Type.__name__ = "Integer32"
_Gs2328LoopProtectionConfTxmode_Object = MibTableColumn
gs2328LoopProtectionConfTxmode = _Gs2328LoopProtectionConfTxmode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 1, 4, 1, 4),
    _Gs2328LoopProtectionConfTxmode_Type()
)
gs2328LoopProtectionConfTxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoopProtectionConfTxmode.setStatus("current")
_Gs2328LoopProtectionStatusTable_Object = MibTable
gs2328LoopProtectionStatusTable = _Gs2328LoopProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2)
)
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusTable.setStatus("current")
_Gs2328LoopProtectionStatusEntry_Object = MibTableRow
gs2328LoopProtectionStatusEntry = _Gs2328LoopProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1)
)
gs2328LoopProtectionStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328LoopProtectionStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusEntry.setStatus("current")


class _Gs2328LoopProtectionStatusPort_Type(Integer32):
    """Custom type gs2328LoopProtectionStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328LoopProtectionStatusPort_Type.__name__ = "Integer32"
_Gs2328LoopProtectionStatusPort_Object = MibTableColumn
gs2328LoopProtectionStatusPort = _Gs2328LoopProtectionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 1),
    _Gs2328LoopProtectionStatusPort_Type()
)
gs2328LoopProtectionStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusPort.setStatus("current")
_Gs2328LoopProtectionStatusAction_Type = DisplayString
_Gs2328LoopProtectionStatusAction_Object = MibTableColumn
gs2328LoopProtectionStatusAction = _Gs2328LoopProtectionStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 2),
    _Gs2328LoopProtectionStatusAction_Type()
)
gs2328LoopProtectionStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusAction.setStatus("current")
_Gs2328LoopProtectionStatusTransmit_Type = DisplayString
_Gs2328LoopProtectionStatusTransmit_Object = MibTableColumn
gs2328LoopProtectionStatusTransmit = _Gs2328LoopProtectionStatusTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 3),
    _Gs2328LoopProtectionStatusTransmit_Type()
)
gs2328LoopProtectionStatusTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusTransmit.setStatus("current")


class _Gs2328LoopProtectionStatusLoops_Type(Integer32):
    """Custom type gs2328LoopProtectionStatusLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2328LoopProtectionStatusLoops_Type.__name__ = "Integer32"
_Gs2328LoopProtectionStatusLoops_Object = MibTableColumn
gs2328LoopProtectionStatusLoops = _Gs2328LoopProtectionStatusLoops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 4),
    _Gs2328LoopProtectionStatusLoops_Type()
)
gs2328LoopProtectionStatusLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusLoops.setStatus("current")
_Gs2328LoopProtectionStatusStatus_Type = DisplayString
_Gs2328LoopProtectionStatusStatus_Object = MibTableColumn
gs2328LoopProtectionStatusStatus = _Gs2328LoopProtectionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 5),
    _Gs2328LoopProtectionStatusStatus_Type()
)
gs2328LoopProtectionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusStatus.setStatus("current")
_Gs2328LoopProtectionStatusLoop_Type = DisplayString
_Gs2328LoopProtectionStatusLoop_Object = MibTableColumn
gs2328LoopProtectionStatusLoop = _Gs2328LoopProtectionStatusLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 6),
    _Gs2328LoopProtectionStatusLoop_Type()
)
gs2328LoopProtectionStatusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusLoop.setStatus("current")
_Gs2328LoopProtectionStatusTimeLastLoop_Type = DisplayString
_Gs2328LoopProtectionStatusTimeLastLoop_Object = MibTableColumn
gs2328LoopProtectionStatusTimeLastLoop = _Gs2328LoopProtectionStatusTimeLastLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 12, 2, 1, 7),
    _Gs2328LoopProtectionStatusTimeLastLoop_Type()
)
gs2328LoopProtectionStatusTimeLastLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LoopProtectionStatusTimeLastLoop.setStatus("current")
_Gs2328Qos_ObjectIdentity = ObjectIdentity
gs2328Qos = _Gs2328Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14)
)
_Gs2328QosPortClassification_ObjectIdentity = ObjectIdentity
gs2328QosPortClassification = _Gs2328QosPortClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1)
)
_Gs2328QosPortClassificationTable_Object = MibTable
gs2328QosPortClassificationTable = _Gs2328QosPortClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    gs2328QosPortClassificationTable.setStatus("current")
_Gs2328QosPortClassificationEntry_Object = MibTableRow
gs2328QosPortClassificationEntry = _Gs2328QosPortClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1)
)
gs2328QosPortClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosPortClassificationPort"),
)
if mibBuilder.loadTexts:
    gs2328QosPortClassificationEntry.setStatus("current")


class _Gs2328QosPortClassificationPort_Type(Integer32):
    """Custom type gs2328QosPortClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosPortClassificationPort_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationPort_Object = MibTableColumn
gs2328QosPortClassificationPort = _Gs2328QosPortClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 1),
    _Gs2328QosPortClassificationPort_Type()
)
gs2328QosPortClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationPort.setStatus("current")


class _Gs2328QosPortClassificationQoSclass_Type(Integer32):
    """Custom type gs2328QosPortClassificationQoSclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328QosPortClassificationQoSclass_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationQoSclass_Object = MibTableColumn
gs2328QosPortClassificationQoSclass = _Gs2328QosPortClassificationQoSclass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 2),
    _Gs2328QosPortClassificationQoSclass_Type()
)
gs2328QosPortClassificationQoSclass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationQoSclass.setStatus("current")


class _Gs2328QosPortClassificationDPlevel_Type(Integer32):
    """Custom type gs2328QosPortClassificationDPlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328QosPortClassificationDPlevel_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationDPlevel_Object = MibTableColumn
gs2328QosPortClassificationDPlevel = _Gs2328QosPortClassificationDPlevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 3),
    _Gs2328QosPortClassificationDPlevel_Type()
)
gs2328QosPortClassificationDPlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationDPlevel.setStatus("current")


class _Gs2328QosPortClassificationPCP_Type(Integer32):
    """Custom type gs2328QosPortClassificationPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328QosPortClassificationPCP_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationPCP_Object = MibTableColumn
gs2328QosPortClassificationPCP = _Gs2328QosPortClassificationPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 4),
    _Gs2328QosPortClassificationPCP_Type()
)
gs2328QosPortClassificationPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationPCP.setStatus("current")


class _Gs2328QosPortClassificationDEI_Type(Integer32):
    """Custom type gs2328QosPortClassificationDEI based on Integer32"""
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


_Gs2328QosPortClassificationDEI_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationDEI_Object = MibTableColumn
gs2328QosPortClassificationDEI = _Gs2328QosPortClassificationDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 5),
    _Gs2328QosPortClassificationDEI_Type()
)
gs2328QosPortClassificationDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationDEI.setStatus("current")


class _Gs2328QosPortClassificationTagClass_Type(Integer32):
    """Custom type gs2328QosPortClassificationTagClass based on Integer32"""
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


_Gs2328QosPortClassificationTagClass_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationTagClass_Object = MibTableColumn
gs2328QosPortClassificationTagClass = _Gs2328QosPortClassificationTagClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 6),
    _Gs2328QosPortClassificationTagClass_Type()
)
gs2328QosPortClassificationTagClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationTagClass.setStatus("current")


class _Gs2328QosPortClassificationDSCPBased_Type(Integer32):
    """Custom type gs2328QosPortClassificationDSCPBased based on Integer32"""
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


_Gs2328QosPortClassificationDSCPBased_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationDSCPBased_Object = MibTableColumn
gs2328QosPortClassificationDSCPBased = _Gs2328QosPortClassificationDSCPBased_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 7),
    _Gs2328QosPortClassificationDSCPBased_Type()
)
gs2328QosPortClassificationDSCPBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationDSCPBased.setStatus("current")


class _Gs2328QosPortClassificationAddressMode_Type(Integer32):
    """Custom type gs2328QosPortClassificationAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("source", 0),
          ("destination", 1))
    )


_Gs2328QosPortClassificationAddressMode_Type.__name__ = "Integer32"
_Gs2328QosPortClassificationAddressMode_Object = MibTableColumn
gs2328QosPortClassificationAddressMode = _Gs2328QosPortClassificationAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 1, 1, 8),
    _Gs2328QosPortClassificationAddressMode_Type()
)
gs2328QosPortClassificationAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortClassificationAddressMode.setStatus("current")
_Gs2328QoSIngressPortTagClassificationTable_Object = MibTable
gs2328QoSIngressPortTagClassificationTable = _Gs2328QoSIngressPortTagClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagClassificationTable.setStatus("current")
_Gs2328QoSIngressPortTagClassificationEntry_Object = MibTableRow
gs2328QoSIngressPortTagClassificationEntry = _Gs2328QoSIngressPortTagClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2, 1)
)
gs2328QoSIngressPortTagClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QoSIngressPortTagClassificationPort"),
    (0, "LANCOM-GS-2328-MIB", "gs2328QoSIngressPortTagPCP"),
    (0, "LANCOM-GS-2328-MIB", "gs2328QoSIngressPortTagDEI"),
)
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagClassificationEntry.setStatus("current")


class _Gs2328QoSIngressPortTagClassificationPort_Type(Integer32):
    """Custom type gs2328QoSIngressPortTagClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QoSIngressPortTagClassificationPort_Type.__name__ = "Integer32"
_Gs2328QoSIngressPortTagClassificationPort_Object = MibTableColumn
gs2328QoSIngressPortTagClassificationPort = _Gs2328QoSIngressPortTagClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2, 1, 1),
    _Gs2328QoSIngressPortTagClassificationPort_Type()
)
gs2328QoSIngressPortTagClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagClassificationPort.setStatus("current")


class _Gs2328QoSIngressPortTagPCP_Type(Integer32):
    """Custom type gs2328QoSIngressPortTagPCP based on Integer32"""
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


_Gs2328QoSIngressPortTagPCP_Type.__name__ = "Integer32"
_Gs2328QoSIngressPortTagPCP_Object = MibTableColumn
gs2328QoSIngressPortTagPCP = _Gs2328QoSIngressPortTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2, 1, 2),
    _Gs2328QoSIngressPortTagPCP_Type()
)
gs2328QoSIngressPortTagPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagPCP.setStatus("current")


class _Gs2328QoSIngressPortTagDEI_Type(Integer32):
    """Custom type gs2328QoSIngressPortTagDEI based on Integer32"""
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


_Gs2328QoSIngressPortTagDEI_Type.__name__ = "Integer32"
_Gs2328QoSIngressPortTagDEI_Object = MibTableColumn
gs2328QoSIngressPortTagDEI = _Gs2328QoSIngressPortTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2, 1, 3),
    _Gs2328QoSIngressPortTagDEI_Type()
)
gs2328QoSIngressPortTagDEI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagDEI.setStatus("current")


class _Gs2328QoSIngressPortTagQosClass_Type(Integer32):
    """Custom type gs2328QoSIngressPortTagQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328QoSIngressPortTagQosClass_Type.__name__ = "Integer32"
_Gs2328QoSIngressPortTagQosClass_Object = MibTableColumn
gs2328QoSIngressPortTagQosClass = _Gs2328QoSIngressPortTagQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2, 1, 4),
    _Gs2328QoSIngressPortTagQosClass_Type()
)
gs2328QoSIngressPortTagQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagQosClass.setStatus("current")


class _Gs2328QoSIngressPortTagDPLevel_Type(Integer32):
    """Custom type gs2328QoSIngressPortTagDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328QoSIngressPortTagDPLevel_Type.__name__ = "Integer32"
_Gs2328QoSIngressPortTagDPLevel_Object = MibTableColumn
gs2328QoSIngressPortTagDPLevel = _Gs2328QoSIngressPortTagDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 1, 2, 1, 5),
    _Gs2328QoSIngressPortTagDPLevel_Type()
)
gs2328QoSIngressPortTagDPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSIngressPortTagDPLevel.setStatus("current")
_Gs2328QosPortPolicingTable_Object = MibTable
gs2328QosPortPolicingTable = _Gs2328QosPortPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gs2328QosPortPolicingTable.setStatus("current")
_Gs2328QosPortPolicingEntry_Object = MibTableRow
gs2328QosPortPolicingEntry = _Gs2328QosPortPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2, 1)
)
gs2328QosPortPolicingEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosPortPolicingPort"),
)
if mibBuilder.loadTexts:
    gs2328QosPortPolicingEntry.setStatus("current")


class _Gs2328QosPortPolicingPort_Type(Integer32):
    """Custom type gs2328QosPortPolicingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosPortPolicingPort_Type.__name__ = "Integer32"
_Gs2328QosPortPolicingPort_Object = MibTableColumn
gs2328QosPortPolicingPort = _Gs2328QosPortPolicingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2, 1, 1),
    _Gs2328QosPortPolicingPort_Type()
)
gs2328QosPortPolicingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosPortPolicingPort.setStatus("current")


class _Gs2328QosPortPolicingMode_Type(Integer32):
    """Custom type gs2328QosPortPolicingMode based on Integer32"""
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


_Gs2328QosPortPolicingMode_Type.__name__ = "Integer32"
_Gs2328QosPortPolicingMode_Object = MibTableColumn
gs2328QosPortPolicingMode = _Gs2328QosPortPolicingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2, 1, 2),
    _Gs2328QosPortPolicingMode_Type()
)
gs2328QosPortPolicingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortPolicingMode.setStatus("current")


class _Gs2328QosPortPolicingRate_Type(Integer32):
    """Custom type gs2328QosPortPolicingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2328QosPortPolicingRate_Type.__name__ = "Integer32"
_Gs2328QosPortPolicingRate_Object = MibTableColumn
gs2328QosPortPolicingRate = _Gs2328QosPortPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2, 1, 3),
    _Gs2328QosPortPolicingRate_Type()
)
gs2328QosPortPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortPolicingRate.setStatus("current")


class _Gs2328QosPortPolicingUnit_Type(Integer32):
    """Custom type gs2328QosPortPolicingUnit based on Integer32"""
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


_Gs2328QosPortPolicingUnit_Type.__name__ = "Integer32"
_Gs2328QosPortPolicingUnit_Object = MibTableColumn
gs2328QosPortPolicingUnit = _Gs2328QosPortPolicingUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2, 1, 4),
    _Gs2328QosPortPolicingUnit_Type()
)
gs2328QosPortPolicingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortPolicingUnit.setStatus("current")


class _Gs2328QosPortPolicingFlowControl_Type(Integer32):
    """Custom type gs2328QosPortPolicingFlowControl based on Integer32"""
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


_Gs2328QosPortPolicingFlowControl_Type.__name__ = "Integer32"
_Gs2328QosPortPolicingFlowControl_Object = MibTableColumn
gs2328QosPortPolicingFlowControl = _Gs2328QosPortPolicingFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 2, 1, 5),
    _Gs2328QosPortPolicingFlowControl_Type()
)
gs2328QosPortPolicingFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortPolicingFlowControl.setStatus("current")
_Gs2328QosPortScheduler_ObjectIdentity = ObjectIdentity
gs2328QosPortScheduler = _Gs2328QosPortScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3)
)
_Gs2328QosPortSchedulerModeTable_Object = MibTable
gs2328QosPortSchedulerModeTable = _Gs2328QosPortSchedulerModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    gs2328QosPortSchedulerModeTable.setStatus("current")
_Gs2328QosPortSchedulerModeEntry_Object = MibTableRow
gs2328QosPortSchedulerModeEntry = _Gs2328QosPortSchedulerModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 1, 1)
)
gs2328QosPortSchedulerModeEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosSchedulerModePort"),
)
if mibBuilder.loadTexts:
    gs2328QosPortSchedulerModeEntry.setStatus("current")


class _Gs2328QosSchedulerModePort_Type(Integer32):
    """Custom type gs2328QosSchedulerModePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosSchedulerModePort_Type.__name__ = "Integer32"
_Gs2328QosSchedulerModePort_Object = MibTableColumn
gs2328QosSchedulerModePort = _Gs2328QosSchedulerModePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 1, 1, 1),
    _Gs2328QosSchedulerModePort_Type()
)
gs2328QosSchedulerModePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosSchedulerModePort.setStatus("current")


class _Gs2328QosSchedulerMode_Type(Integer32):
    """Custom type gs2328QosSchedulerMode based on Integer32"""
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


_Gs2328QosSchedulerMode_Type.__name__ = "Integer32"
_Gs2328QosSchedulerMode_Object = MibTableColumn
gs2328QosSchedulerMode = _Gs2328QosSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 1, 1, 2),
    _Gs2328QosSchedulerMode_Type()
)
gs2328QosSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerMode.setStatus("current")


class _Gs2328QosSchedulerShaper_Type(Integer32):
    """Custom type gs2328QosSchedulerShaper based on Integer32"""
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


_Gs2328QosSchedulerShaper_Type.__name__ = "Integer32"
_Gs2328QosSchedulerShaper_Object = MibTableColumn
gs2328QosSchedulerShaper = _Gs2328QosSchedulerShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 1, 1, 3),
    _Gs2328QosSchedulerShaper_Type()
)
gs2328QosSchedulerShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerShaper.setStatus("current")


class _Gs2328QosSchedulerShaperRate_Type(Integer32):
    """Custom type gs2328QosSchedulerShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2328QosSchedulerShaperRate_Type.__name__ = "Integer32"
_Gs2328QosSchedulerShaperRate_Object = MibTableColumn
gs2328QosSchedulerShaperRate = _Gs2328QosSchedulerShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 1, 1, 4),
    _Gs2328QosSchedulerShaperRate_Type()
)
gs2328QosSchedulerShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerShaperRate.setStatus("current")
_Gs2328QosPortSchedulerTable_Object = MibTable
gs2328QosPortSchedulerTable = _Gs2328QosPortSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328QosPortSchedulerTable.setStatus("current")
_Gs2328QosPortSchedulerEntry_Object = MibTableRow
gs2328QosPortSchedulerEntry = _Gs2328QosPortSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1)
)
gs2328QosPortSchedulerEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosSchedulerPort"),
    (0, "LANCOM-GS-2328-MIB", "gs2328QosSchedulerPortQueue"),
)
if mibBuilder.loadTexts:
    gs2328QosPortSchedulerEntry.setStatus("current")


class _Gs2328QosSchedulerPort_Type(Integer32):
    """Custom type gs2328QosSchedulerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosSchedulerPort_Type.__name__ = "Integer32"
_Gs2328QosSchedulerPort_Object = MibTableColumn
gs2328QosSchedulerPort = _Gs2328QosSchedulerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 1),
    _Gs2328QosSchedulerPort_Type()
)
gs2328QosSchedulerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPort.setStatus("current")


class _Gs2328QosSchedulerPortQueue_Type(Integer32):
    """Custom type gs2328QosSchedulerPortQueue based on Integer32"""
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


_Gs2328QosSchedulerPortQueue_Type.__name__ = "Integer32"
_Gs2328QosSchedulerPortQueue_Object = MibTableColumn
gs2328QosSchedulerPortQueue = _Gs2328QosSchedulerPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 2),
    _Gs2328QosSchedulerPortQueue_Type()
)
gs2328QosSchedulerPortQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPortQueue.setStatus("current")


class _Gs2328QosSchedulerPortQueueShaper_Type(Integer32):
    """Custom type gs2328QosSchedulerPortQueueShaper based on Integer32"""
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


_Gs2328QosSchedulerPortQueueShaper_Type.__name__ = "Integer32"
_Gs2328QosSchedulerPortQueueShaper_Object = MibTableColumn
gs2328QosSchedulerPortQueueShaper = _Gs2328QosSchedulerPortQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 3),
    _Gs2328QosSchedulerPortQueueShaper_Type()
)
gs2328QosSchedulerPortQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPortQueueShaper.setStatus("current")


class _Gs2328QosSchedulerPortQueueShaperRate_Type(Integer32):
    """Custom type gs2328QosSchedulerPortQueueShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2328QosSchedulerPortQueueShaperRate_Type.__name__ = "Integer32"
_Gs2328QosSchedulerPortQueueShaperRate_Object = MibTableColumn
gs2328QosSchedulerPortQueueShaperRate = _Gs2328QosSchedulerPortQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 4),
    _Gs2328QosSchedulerPortQueueShaperRate_Type()
)
gs2328QosSchedulerPortQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPortQueueShaperRate.setStatus("current")


class _Gs2328QosSchedulerPortQueueShaperExcess_Type(Integer32):
    """Custom type gs2328QosSchedulerPortQueueShaperExcess based on Integer32"""
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


_Gs2328QosSchedulerPortQueueShaperExcess_Type.__name__ = "Integer32"
_Gs2328QosSchedulerPortQueueShaperExcess_Object = MibTableColumn
gs2328QosSchedulerPortQueueShaperExcess = _Gs2328QosSchedulerPortQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 5),
    _Gs2328QosSchedulerPortQueueShaperExcess_Type()
)
gs2328QosSchedulerPortQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPortQueueShaperExcess.setStatus("current")


class _Gs2328QosSchedulerPortQueueSchedulerWeight_Type(Integer32):
    """Custom type gs2328QosSchedulerPortQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2328QosSchedulerPortQueueSchedulerWeight_Type.__name__ = "Integer32"
_Gs2328QosSchedulerPortQueueSchedulerWeight_Object = MibTableColumn
gs2328QosSchedulerPortQueueSchedulerWeight = _Gs2328QosSchedulerPortQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 6),
    _Gs2328QosSchedulerPortQueueSchedulerWeight_Type()
)
gs2328QosSchedulerPortQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPortQueueSchedulerWeight.setStatus("current")
_Gs2328QosSchedulerPortQueueSchedulerPercent_Type = DisplayString
_Gs2328QosSchedulerPortQueueSchedulerPercent_Object = MibTableColumn
gs2328QosSchedulerPortQueueSchedulerPercent = _Gs2328QosSchedulerPortQueueSchedulerPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 3, 2, 1, 7),
    _Gs2328QosSchedulerPortQueueSchedulerPercent_Type()
)
gs2328QosSchedulerPortQueueSchedulerPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosSchedulerPortQueueSchedulerPercent.setStatus("current")
_Gs2328QosPortEgressTagRemarking_ObjectIdentity = ObjectIdentity
gs2328QosPortEgressTagRemarking = _Gs2328QosPortEgressTagRemarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4)
)
_Gs2328QosPortEgressTagRemarkingTable_Object = MibTable
gs2328QosPortEgressTagRemarkingTable = _Gs2328QosPortEgressTagRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 1)
)
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingTable.setStatus("current")
_Gs2328QosPortEgressTagRemarkingEntry_Object = MibTableRow
gs2328QosPortEgressTagRemarkingEntry = _Gs2328QosPortEgressTagRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 1, 1)
)
gs2328QosPortEgressTagRemarkingEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosEgressTagRemarkingPort"),
)
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingEntry.setStatus("current")


class _Gs2328QosEgressTagRemarkingPort_Type(Integer32):
    """Custom type gs2328QosEgressTagRemarkingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosEgressTagRemarkingPort_Type.__name__ = "Integer32"
_Gs2328QosEgressTagRemarkingPort_Object = MibTableColumn
gs2328QosEgressTagRemarkingPort = _Gs2328QosEgressTagRemarkingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 1, 1, 1),
    _Gs2328QosEgressTagRemarkingPort_Type()
)
gs2328QosEgressTagRemarkingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosEgressTagRemarkingPort.setStatus("current")


class _Gs2328QosEgressTagRemarkingMode_Type(Integer32):
    """Custom type gs2328QosEgressTagRemarkingMode based on Integer32"""
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


_Gs2328QosEgressTagRemarkingMode_Type.__name__ = "Integer32"
_Gs2328QosEgressTagRemarkingMode_Object = MibTableColumn
gs2328QosEgressTagRemarkingMode = _Gs2328QosEgressTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 1, 1, 2),
    _Gs2328QosEgressTagRemarkingMode_Type()
)
gs2328QosEgressTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosEgressTagRemarkingMode.setStatus("current")
_Gs2328QosPortEgressTagRemarkingDefTable_Object = MibTable
gs2328QosPortEgressTagRemarkingDefTable = _Gs2328QosPortEgressTagRemarkingDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingDefTable.setStatus("current")
_Gs2328QosPortEgressTagRemarkingDefEntry_Object = MibTableRow
gs2328QosPortEgressTagRemarkingDefEntry = _Gs2328QosPortEgressTagRemarkingDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 2, 1)
)
gs2328QosPortEgressTagRemarkingDefEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosEgressTagRemarkingDefPort"),
)
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingDefEntry.setStatus("current")


class _Gs2328QosEgressTagRemarkingDefPort_Type(Integer32):
    """Custom type gs2328QosEgressTagRemarkingDefPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosEgressTagRemarkingDefPort_Type.__name__ = "Integer32"
_Gs2328QosEgressTagRemarkingDefPort_Object = MibTableColumn
gs2328QosEgressTagRemarkingDefPort = _Gs2328QosEgressTagRemarkingDefPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 2, 1, 1),
    _Gs2328QosEgressTagRemarkingDefPort_Type()
)
gs2328QosEgressTagRemarkingDefPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosEgressTagRemarkingDefPort.setStatus("current")


class _Gs2328QosEgressTagRemarkingDefPCP_Type(Integer32):
    """Custom type gs2328QosEgressTagRemarkingDefPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328QosEgressTagRemarkingDefPCP_Type.__name__ = "Integer32"
_Gs2328QosEgressTagRemarkingDefPCP_Object = MibTableColumn
gs2328QosEgressTagRemarkingDefPCP = _Gs2328QosEgressTagRemarkingDefPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 2, 1, 2),
    _Gs2328QosEgressTagRemarkingDefPCP_Type()
)
gs2328QosEgressTagRemarkingDefPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosEgressTagRemarkingDefPCP.setStatus("current")


class _Gs2328QosEgressTagRemarkingDefDEI_Type(Integer32):
    """Custom type gs2328QosEgressTagRemarkingDefDEI based on Integer32"""
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


_Gs2328QosEgressTagRemarkingDefDEI_Type.__name__ = "Integer32"
_Gs2328QosEgressTagRemarkingDefDEI_Object = MibTableColumn
gs2328QosEgressTagRemarkingDefDEI = _Gs2328QosEgressTagRemarkingDefDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 2, 1, 3),
    _Gs2328QosEgressTagRemarkingDefDEI_Type()
)
gs2328QosEgressTagRemarkingDefDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosEgressTagRemarkingDefDEI.setStatus("current")
_Gs2328QosPortEgressTagRemarkingMapTable_Object = MibTable
gs2328QosPortEgressTagRemarkingMapTable = _Gs2328QosPortEgressTagRemarkingMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingMapTable.setStatus("current")
_Gs2328QosPortEgressTagRemarkingMapEntry_Object = MibTableRow
gs2328QosPortEgressTagRemarkingMapEntry = _Gs2328QosPortEgressTagRemarkingMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4, 1)
)
gs2328QosPortEgressTagRemarkingMapEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosPortEgressTagRemarkingMapPort"),
    (0, "LANCOM-GS-2328-MIB", "gs2328QosTagRemarkingQoSClass"),
    (0, "LANCOM-GS-2328-MIB", "gs2328QosTagRemarkingDPLevel"),
)
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingMapEntry.setStatus("current")


class _Gs2328QosPortEgressTagRemarkingMapPort_Type(Integer32):
    """Custom type gs2328QosPortEgressTagRemarkingMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosPortEgressTagRemarkingMapPort_Type.__name__ = "Integer32"
_Gs2328QosPortEgressTagRemarkingMapPort_Object = MibTableColumn
gs2328QosPortEgressTagRemarkingMapPort = _Gs2328QosPortEgressTagRemarkingMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4, 1, 1),
    _Gs2328QosPortEgressTagRemarkingMapPort_Type()
)
gs2328QosPortEgressTagRemarkingMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosPortEgressTagRemarkingMapPort.setStatus("current")


class _Gs2328QosTagRemarkingQoSClass_Type(Integer32):
    """Custom type gs2328QosTagRemarkingQoSClass based on Integer32"""
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


_Gs2328QosTagRemarkingQoSClass_Type.__name__ = "Integer32"
_Gs2328QosTagRemarkingQoSClass_Object = MibTableColumn
gs2328QosTagRemarkingQoSClass = _Gs2328QosTagRemarkingQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4, 1, 2),
    _Gs2328QosTagRemarkingQoSClass_Type()
)
gs2328QosTagRemarkingQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosTagRemarkingQoSClass.setStatus("current")


class _Gs2328QosTagRemarkingDPLevel_Type(Integer32):
    """Custom type gs2328QosTagRemarkingDPLevel based on Integer32"""
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


_Gs2328QosTagRemarkingDPLevel_Type.__name__ = "Integer32"
_Gs2328QosTagRemarkingDPLevel_Object = MibTableColumn
gs2328QosTagRemarkingDPLevel = _Gs2328QosTagRemarkingDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4, 1, 3),
    _Gs2328QosTagRemarkingDPLevel_Type()
)
gs2328QosTagRemarkingDPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosTagRemarkingDPLevel.setStatus("current")


class _Gs2328QosTagRemarkingPCP_Type(Integer32):
    """Custom type gs2328QosTagRemarkingPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328QosTagRemarkingPCP_Type.__name__ = "Integer32"
_Gs2328QosTagRemarkingPCP_Object = MibTableColumn
gs2328QosTagRemarkingPCP = _Gs2328QosTagRemarkingPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4, 1, 4),
    _Gs2328QosTagRemarkingPCP_Type()
)
gs2328QosTagRemarkingPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosTagRemarkingPCP.setStatus("current")


class _Gs2328QosTagRemarkingDEI_Type(Integer32):
    """Custom type gs2328QosTagRemarkingDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328QosTagRemarkingDEI_Type.__name__ = "Integer32"
_Gs2328QosTagRemarkingDEI_Object = MibTableColumn
gs2328QosTagRemarkingDEI = _Gs2328QosTagRemarkingDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 4, 4, 1, 5),
    _Gs2328QosTagRemarkingDEI_Type()
)
gs2328QosTagRemarkingDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosTagRemarkingDEI.setStatus("current")
_Gs2328QosPortDSCPTable_Object = MibTable
gs2328QosPortDSCPTable = _Gs2328QosPortDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 5)
)
if mibBuilder.loadTexts:
    gs2328QosPortDSCPTable.setStatus("current")
_Gs2328QosPortDSCPEntry_Object = MibTableRow
gs2328QosPortDSCPEntry = _Gs2328QosPortDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 5, 1)
)
gs2328QosPortDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosPortDSCPPort"),
)
if mibBuilder.loadTexts:
    gs2328QosPortDSCPEntry.setStatus("current")


class _Gs2328QosPortDSCPPort_Type(Integer32):
    """Custom type gs2328QosPortDSCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosPortDSCPPort_Type.__name__ = "Integer32"
_Gs2328QosPortDSCPPort_Object = MibTableColumn
gs2328QosPortDSCPPort = _Gs2328QosPortDSCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 5, 1, 1),
    _Gs2328QosPortDSCPPort_Type()
)
gs2328QosPortDSCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosPortDSCPPort.setStatus("current")


class _Gs2328QosPortDSCPIngressTranslate_Type(Integer32):
    """Custom type gs2328QosPortDSCPIngressTranslate based on Integer32"""
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


_Gs2328QosPortDSCPIngressTranslate_Type.__name__ = "Integer32"
_Gs2328QosPortDSCPIngressTranslate_Object = MibTableColumn
gs2328QosPortDSCPIngressTranslate = _Gs2328QosPortDSCPIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 5, 1, 2),
    _Gs2328QosPortDSCPIngressTranslate_Type()
)
gs2328QosPortDSCPIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortDSCPIngressTranslate.setStatus("current")


class _Gs2328QosPortDSCPIngressClassify_Type(Integer32):
    """Custom type gs2328QosPortDSCPIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328QosPortDSCPIngressClassify_Type.__name__ = "Integer32"
_Gs2328QosPortDSCPIngressClassify_Object = MibTableColumn
gs2328QosPortDSCPIngressClassify = _Gs2328QosPortDSCPIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 5, 1, 3),
    _Gs2328QosPortDSCPIngressClassify_Type()
)
gs2328QosPortDSCPIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortDSCPIngressClassify.setStatus("current")


class _Gs2328QosPortDSCPEgressRewrite_Type(Integer32):
    """Custom type gs2328QosPortDSCPEgressRewrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328QosPortDSCPEgressRewrite_Type.__name__ = "Integer32"
_Gs2328QosPortDSCPEgressRewrite_Object = MibTableColumn
gs2328QosPortDSCPEgressRewrite = _Gs2328QosPortDSCPEgressRewrite_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 5, 1, 4),
    _Gs2328QosPortDSCPEgressRewrite_Type()
)
gs2328QosPortDSCPEgressRewrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPortDSCPEgressRewrite.setStatus("current")
_Gs2328QosDSCPTable_Object = MibTable
gs2328QosDSCPTable = _Gs2328QosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6)
)
if mibBuilder.loadTexts:
    gs2328QosDSCPTable.setStatus("current")
_Gs2328QosDSCPEntry_Object = MibTableRow
gs2328QosDSCPEntry = _Gs2328QosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6, 1)
)
gs2328QosDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosDSCPList"),
)
if mibBuilder.loadTexts:
    gs2328QosDSCPEntry.setStatus("current")


class _Gs2328QosDSCPList_Type(Integer32):
    """Custom type gs2328QosDSCPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2328QosDSCPList_Type.__name__ = "Integer32"
_Gs2328QosDSCPList_Object = MibTableColumn
gs2328QosDSCPList = _Gs2328QosDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6, 1, 1),
    _Gs2328QosDSCPList_Type()
)
gs2328QosDSCPList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosDSCPList.setStatus("current")
_Gs2328QosDSCP_Type = DisplayString
_Gs2328QosDSCP_Object = MibTableColumn
gs2328QosDSCP = _Gs2328QosDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6, 1, 2),
    _Gs2328QosDSCP_Type()
)
gs2328QosDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosDSCP.setStatus("current")


class _Gs2328QosDSCPTrust_Type(Integer32):
    """Custom type gs2328QosDSCPTrust based on Integer32"""
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


_Gs2328QosDSCPTrust_Type.__name__ = "Integer32"
_Gs2328QosDSCPTrust_Object = MibTableColumn
gs2328QosDSCPTrust = _Gs2328QosDSCPTrust_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6, 1, 3),
    _Gs2328QosDSCPTrust_Type()
)
gs2328QosDSCPTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPTrust.setStatus("current")


class _Gs2328QosDSCPQosClass_Type(Integer32):
    """Custom type gs2328QosDSCPQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328QosDSCPQosClass_Type.__name__ = "Integer32"
_Gs2328QosDSCPQosClass_Object = MibTableColumn
gs2328QosDSCPQosClass = _Gs2328QosDSCPQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6, 1, 4),
    _Gs2328QosDSCPQosClass_Type()
)
gs2328QosDSCPQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPQosClass.setStatus("current")


class _Gs2328QosDSCPDPL_Type(Integer32):
    """Custom type gs2328QosDSCPDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328QosDSCPDPL_Type.__name__ = "Integer32"
_Gs2328QosDSCPDPL_Object = MibTableColumn
gs2328QosDSCPDPL = _Gs2328QosDSCPDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 6, 1, 5),
    _Gs2328QosDSCPDPL_Type()
)
gs2328QosDSCPDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPDPL.setStatus("current")
_Gs2328QosDSCPTranslationTable_Object = MibTable
gs2328QosDSCPTranslationTable = _Gs2328QosDSCPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7)
)
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationTable.setStatus("current")
_Gs2328QosDSCPTranslationEntry_Object = MibTableRow
gs2328QosDSCPTranslationEntry = _Gs2328QosDSCPTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1)
)
gs2328QosDSCPTranslationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosDSCPTranslationList"),
)
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationEntry.setStatus("current")


class _Gs2328QosDSCPTranslationList_Type(Integer32):
    """Custom type gs2328QosDSCPTranslationList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2328QosDSCPTranslationList_Type.__name__ = "Integer32"
_Gs2328QosDSCPTranslationList_Object = MibTableColumn
gs2328QosDSCPTranslationList = _Gs2328QosDSCPTranslationList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1, 1),
    _Gs2328QosDSCPTranslationList_Type()
)
gs2328QosDSCPTranslationList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationList.setStatus("current")
_Gs2328QosDSCPTranslationDSCPBasedId_Type = DisplayString
_Gs2328QosDSCPTranslationDSCPBasedId_Object = MibTableColumn
gs2328QosDSCPTranslationDSCPBasedId = _Gs2328QosDSCPTranslationDSCPBasedId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1, 2),
    _Gs2328QosDSCPTranslationDSCPBasedId_Type()
)
gs2328QosDSCPTranslationDSCPBasedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationDSCPBasedId.setStatus("current")


class _Gs2328QosDSCPTranslationIngressTranslate_Type(Integer32):
    """Custom type gs2328QosDSCPTranslationIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328QosDSCPTranslationIngressTranslate_Type.__name__ = "Integer32"
_Gs2328QosDSCPTranslationIngressTranslate_Object = MibTableColumn
gs2328QosDSCPTranslationIngressTranslate = _Gs2328QosDSCPTranslationIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1, 3),
    _Gs2328QosDSCPTranslationIngressTranslate_Type()
)
gs2328QosDSCPTranslationIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationIngressTranslate.setStatus("current")


class _Gs2328QosDSCPTranslationIngressClassify_Type(Integer32):
    """Custom type gs2328QosDSCPTranslationIngressClassify based on Integer32"""
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


_Gs2328QosDSCPTranslationIngressClassify_Type.__name__ = "Integer32"
_Gs2328QosDSCPTranslationIngressClassify_Object = MibTableColumn
gs2328QosDSCPTranslationIngressClassify = _Gs2328QosDSCPTranslationIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1, 4),
    _Gs2328QosDSCPTranslationIngressClassify_Type()
)
gs2328QosDSCPTranslationIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationIngressClassify.setStatus("current")


class _Gs2328QosDSCPTranslationEgressRemapDP0_Type(Integer32):
    """Custom type gs2328QosDSCPTranslationEgressRemapDP0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328QosDSCPTranslationEgressRemapDP0_Type.__name__ = "Integer32"
_Gs2328QosDSCPTranslationEgressRemapDP0_Object = MibTableColumn
gs2328QosDSCPTranslationEgressRemapDP0 = _Gs2328QosDSCPTranslationEgressRemapDP0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1, 5),
    _Gs2328QosDSCPTranslationEgressRemapDP0_Type()
)
gs2328QosDSCPTranslationEgressRemapDP0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationEgressRemapDP0.setStatus("current")


class _Gs2328QosDSCPTranslationEgressRemapDP1_Type(Integer32):
    """Custom type gs2328QosDSCPTranslationEgressRemapDP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328QosDSCPTranslationEgressRemapDP1_Type.__name__ = "Integer32"
_Gs2328QosDSCPTranslationEgressRemapDP1_Object = MibTableColumn
gs2328QosDSCPTranslationEgressRemapDP1 = _Gs2328QosDSCPTranslationEgressRemapDP1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 7, 1, 6),
    _Gs2328QosDSCPTranslationEgressRemapDP1_Type()
)
gs2328QosDSCPTranslationEgressRemapDP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPTranslationEgressRemapDP1.setStatus("current")
_Gs2328QosDSCPClassificationTable_Object = MibTable
gs2328QosDSCPClassificationTable = _Gs2328QosDSCPClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 8)
)
if mibBuilder.loadTexts:
    gs2328QosDSCPClassificationTable.setStatus("current")
_Gs2328QosDSCPClassificationEntry_Object = MibTableRow
gs2328QosDSCPClassificationEntry = _Gs2328QosDSCPClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 8, 1)
)
gs2328QosDSCPClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosDSCPClassificationQoSClass"),
    (0, "LANCOM-GS-2328-MIB", "gs2328QosDSCPClassificationDPL"),
)
if mibBuilder.loadTexts:
    gs2328QosDSCPClassificationEntry.setStatus("current")


class _Gs2328QosDSCPClassificationQoSClass_Type(Integer32):
    """Custom type gs2328QosDSCPClassificationQoSClass based on Integer32"""
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


_Gs2328QosDSCPClassificationQoSClass_Type.__name__ = "Integer32"
_Gs2328QosDSCPClassificationQoSClass_Object = MibTableColumn
gs2328QosDSCPClassificationQoSClass = _Gs2328QosDSCPClassificationQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 8, 1, 1),
    _Gs2328QosDSCPClassificationQoSClass_Type()
)
gs2328QosDSCPClassificationQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosDSCPClassificationQoSClass.setStatus("current")


class _Gs2328QosDSCPClassificationDPL_Type(Integer32):
    """Custom type gs2328QosDSCPClassificationDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2328QosDSCPClassificationDPL_Type.__name__ = "Integer32"
_Gs2328QosDSCPClassificationDPL_Object = MibTableColumn
gs2328QosDSCPClassificationDPL = _Gs2328QosDSCPClassificationDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 8, 1, 2),
    _Gs2328QosDSCPClassificationDPL_Type()
)
gs2328QosDSCPClassificationDPL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosDSCPClassificationDPL.setStatus("current")


class _Gs2328QosDSCPClassificationDSCP_Type(Integer32):
    """Custom type gs2328QosDSCPClassificationDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328QosDSCPClassificationDSCP_Type.__name__ = "Integer32"
_Gs2328QosDSCPClassificationDSCP_Object = MibTableColumn
gs2328QosDSCPClassificationDSCP = _Gs2328QosDSCPClassificationDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 8, 1, 3),
    _Gs2328QosDSCPClassificationDSCP_Type()
)
gs2328QosDSCPClassificationDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDSCPClassificationDSCP.setStatus("current")
_Gs2328QosControlList_ObjectIdentity = ObjectIdentity
gs2328QosControlList = _Gs2328QosControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9)
)


class _Gs2328QosQceCreate_Type(Integer32):
    """Custom type gs2328QosQceCreate based on Integer32"""
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


_Gs2328QosQceCreate_Type.__name__ = "Integer32"
_Gs2328QosQceCreate_Object = MibScalar
gs2328QosQceCreate = _Gs2328QosQceCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 1),
    _Gs2328QosQceCreate_Type()
)
gs2328QosQceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceCreate.setStatus("current")
_Gs2328QosQceTable_Object = MibTable
gs2328QosQceTable = _Gs2328QosQceTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2)
)
if mibBuilder.loadTexts:
    gs2328QosQceTable.setStatus("current")
_Gs2328QosQceEntry_Object = MibTableRow
gs2328QosQceEntry = _Gs2328QosQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1)
)
gs2328QosQceEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosQceIndex"),
)
if mibBuilder.loadTexts:
    gs2328QosQceEntry.setStatus("current")


class _Gs2328QosQceIndex_Type(Integer32):
    """Custom type gs2328QosQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328QosQceIndex_Type.__name__ = "Integer32"
_Gs2328QosQceIndex_Object = MibTableColumn
gs2328QosQceIndex = _Gs2328QosQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 1),
    _Gs2328QosQceIndex_Type()
)
gs2328QosQceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosQceIndex.setStatus("current")


class _Gs2328QosQceID_Type(Integer32):
    """Custom type gs2328QosQceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328QosQceID_Type.__name__ = "Integer32"
_Gs2328QosQceID_Object = MibTableColumn
gs2328QosQceID = _Gs2328QosQceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 2),
    _Gs2328QosQceID_Type()
)
gs2328QosQceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceID.setStatus("current")


class _Gs2328QosQceNextID_Type(Integer32):
    """Custom type gs2328QosQceNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328QosQceNextID_Type.__name__ = "Integer32"
_Gs2328QosQceNextID_Object = MibTableColumn
gs2328QosQceNextID = _Gs2328QosQceNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 3),
    _Gs2328QosQceNextID_Type()
)
gs2328QosQceNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceNextID.setStatus("current")
_Gs2328QosQcePortMembers_Type = DisplayString
_Gs2328QosQcePortMembers_Object = MibTableColumn
gs2328QosQcePortMembers = _Gs2328QosQcePortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 4),
    _Gs2328QosQcePortMembers_Type()
)
gs2328QosQcePortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQcePortMembers.setStatus("current")
_Gs2328QosQceTag_Type = DisplayString
_Gs2328QosQceTag_Object = MibTableColumn
gs2328QosQceTag = _Gs2328QosQceTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 5),
    _Gs2328QosQceTag_Type()
)
gs2328QosQceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceTag.setStatus("current")
_Gs2328QosQceVID_Type = DisplayString
_Gs2328QosQceVID_Object = MibTableColumn
gs2328QosQceVID = _Gs2328QosQceVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 6),
    _Gs2328QosQceVID_Type()
)
gs2328QosQceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceVID.setStatus("current")
_Gs2328QosPCP_Type = DisplayString
_Gs2328QosPCP_Object = MibTableColumn
gs2328QosPCP = _Gs2328QosPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 7),
    _Gs2328QosPCP_Type()
)
gs2328QosPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosPCP.setStatus("current")
_Gs2328QosDEI_Type = DisplayString
_Gs2328QosDEI_Object = MibTableColumn
gs2328QosDEI = _Gs2328QosDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 8),
    _Gs2328QosDEI_Type()
)
gs2328QosDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDEI.setStatus("current")
_Gs2328QosSMAC_Type = DisplayString
_Gs2328QosSMAC_Object = MibTableColumn
gs2328QosSMAC = _Gs2328QosSMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 9),
    _Gs2328QosSMAC_Type()
)
gs2328QosSMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSMAC.setStatus("current")
_Gs2328QosDMACType_Type = DisplayString
_Gs2328QosDMACType_Object = MibTableColumn
gs2328QosDMACType = _Gs2328QosDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 10),
    _Gs2328QosDMACType_Type()
)
gs2328QosDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosDMACType.setStatus("current")


class _Gs2328QosFrameType_Type(Integer32):
    """Custom type gs2328QosFrameType based on Integer32"""
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


_Gs2328QosFrameType_Type.__name__ = "Integer32"
_Gs2328QosFrameType_Object = MibTableColumn
gs2328QosFrameType = _Gs2328QosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 11),
    _Gs2328QosFrameType_Type()
)
gs2328QosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosFrameType.setStatus("current")
_Gs2328QosMacEtherType_Type = DisplayString
_Gs2328QosMacEtherType_Object = MibTableColumn
gs2328QosMacEtherType = _Gs2328QosMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 12),
    _Gs2328QosMacEtherType_Type()
)
gs2328QosMacEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosMacEtherType.setStatus("current")
_Gs2328QosLLCSSAPAddr_Type = DisplayString
_Gs2328QosLLCSSAPAddr_Object = MibTableColumn
gs2328QosLLCSSAPAddr = _Gs2328QosLLCSSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 13),
    _Gs2328QosLLCSSAPAddr_Type()
)
gs2328QosLLCSSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosLLCSSAPAddr.setStatus("current")
_Gs2328QosLLCDSAPAddr_Type = DisplayString
_Gs2328QosLLCDSAPAddr_Object = MibTableColumn
gs2328QosLLCDSAPAddr = _Gs2328QosLLCDSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 14),
    _Gs2328QosLLCDSAPAddr_Type()
)
gs2328QosLLCDSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosLLCDSAPAddr.setStatus("current")
_Gs2328QosLLCControl_Type = DisplayString
_Gs2328QosLLCControl_Object = MibTableColumn
gs2328QosLLCControl = _Gs2328QosLLCControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 15),
    _Gs2328QosLLCControl_Type()
)
gs2328QosLLCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosLLCControl.setStatus("current")
_Gs2328QosSNAPPID_Type = DisplayString
_Gs2328QosSNAPPID_Object = MibTableColumn
gs2328QosSNAPPID = _Gs2328QosSNAPPID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 16),
    _Gs2328QosSNAPPID_Type()
)
gs2328QosSNAPPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosSNAPPID.setStatus("current")
_Gs2328QosIpv4Protocol_Type = DisplayString
_Gs2328QosIpv4Protocol_Object = MibTableColumn
gs2328QosIpv4Protocol = _Gs2328QosIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 17),
    _Gs2328QosIpv4Protocol_Type()
)
gs2328QosIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4Protocol.setStatus("current")


class _Gs2328QosIpv4ProtocolValue_Type(Integer32):
    """Custom type gs2328QosIpv4ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328QosIpv4ProtocolValue_Type.__name__ = "Integer32"
_Gs2328QosIpv4ProtocolValue_Object = MibTableColumn
gs2328QosIpv4ProtocolValue = _Gs2328QosIpv4ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 18),
    _Gs2328QosIpv4ProtocolValue_Type()
)
gs2328QosIpv4ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4ProtocolValue.setStatus("current")
_Gs2328QosIpv4ProtocolUDPSport_Type = DisplayString
_Gs2328QosIpv4ProtocolUDPSport_Object = MibTableColumn
gs2328QosIpv4ProtocolUDPSport = _Gs2328QosIpv4ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 19),
    _Gs2328QosIpv4ProtocolUDPSport_Type()
)
gs2328QosIpv4ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4ProtocolUDPSport.setStatus("current")
_Gs2328QosIpv4ProtocolUDPDport_Type = DisplayString
_Gs2328QosIpv4ProtocolUDPDport_Object = MibTableColumn
gs2328QosIpv4ProtocolUDPDport = _Gs2328QosIpv4ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 20),
    _Gs2328QosIpv4ProtocolUDPDport_Type()
)
gs2328QosIpv4ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4ProtocolUDPDport.setStatus("current")
_Gs2328QosIpv4ProtocolTCPSport_Type = DisplayString
_Gs2328QosIpv4ProtocolTCPSport_Object = MibTableColumn
gs2328QosIpv4ProtocolTCPSport = _Gs2328QosIpv4ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 21),
    _Gs2328QosIpv4ProtocolTCPSport_Type()
)
gs2328QosIpv4ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4ProtocolTCPSport.setStatus("current")
_Gs2328QosIpv4ProtocolTCPDport_Type = DisplayString
_Gs2328QosIpv4ProtocolTCPDport_Object = MibTableColumn
gs2328QosIpv4ProtocolTCPDport = _Gs2328QosIpv4ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 22),
    _Gs2328QosIpv4ProtocolTCPDport_Type()
)
gs2328QosIpv4ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4ProtocolTCPDport.setStatus("current")
_Gs2328QosIpv4Ip_Type = DisplayString
_Gs2328QosIpv4Ip_Object = MibTableColumn
gs2328QosIpv4Ip = _Gs2328QosIpv4Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 23),
    _Gs2328QosIpv4Ip_Type()
)
gs2328QosIpv4Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4Ip.setStatus("current")
_Gs2328QosIpv4Mask_Type = DisplayString
_Gs2328QosIpv4Mask_Object = MibTableColumn
gs2328QosIpv4Mask = _Gs2328QosIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 24),
    _Gs2328QosIpv4Mask_Type()
)
gs2328QosIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4Mask.setStatus("current")


class _Gs2328QosIpv4IPFragment_Type(Integer32):
    """Custom type gs2328QosIpv4IPFragment based on Integer32"""
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


_Gs2328QosIpv4IPFragment_Type.__name__ = "Integer32"
_Gs2328QosIpv4IPFragment_Object = MibTableColumn
gs2328QosIpv4IPFragment = _Gs2328QosIpv4IPFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 25),
    _Gs2328QosIpv4IPFragment_Type()
)
gs2328QosIpv4IPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4IPFragment.setStatus("current")
_Gs2328QosIpv4DSCP_Type = DisplayString
_Gs2328QosIpv4DSCP_Object = MibTableColumn
gs2328QosIpv4DSCP = _Gs2328QosIpv4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 26),
    _Gs2328QosIpv4DSCP_Type()
)
gs2328QosIpv4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv4DSCP.setStatus("current")
_Gs2328QosIpv6Protocol_Type = DisplayString
_Gs2328QosIpv6Protocol_Object = MibTableColumn
gs2328QosIpv6Protocol = _Gs2328QosIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 27),
    _Gs2328QosIpv6Protocol_Type()
)
gs2328QosIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6Protocol.setStatus("current")


class _Gs2328QosIpv6ProtocolValue_Type(Integer32):
    """Custom type gs2328QosIpv6ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328QosIpv6ProtocolValue_Type.__name__ = "Integer32"
_Gs2328QosIpv6ProtocolValue_Object = MibTableColumn
gs2328QosIpv6ProtocolValue = _Gs2328QosIpv6ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 28),
    _Gs2328QosIpv6ProtocolValue_Type()
)
gs2328QosIpv6ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6ProtocolValue.setStatus("current")
_Gs2328QosIpv6ProtocolUDPSport_Type = DisplayString
_Gs2328QosIpv6ProtocolUDPSport_Object = MibTableColumn
gs2328QosIpv6ProtocolUDPSport = _Gs2328QosIpv6ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 29),
    _Gs2328QosIpv6ProtocolUDPSport_Type()
)
gs2328QosIpv6ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6ProtocolUDPSport.setStatus("current")
_Gs2328QosIpv6ProtocolUDPDport_Type = DisplayString
_Gs2328QosIpv6ProtocolUDPDport_Object = MibTableColumn
gs2328QosIpv6ProtocolUDPDport = _Gs2328QosIpv6ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 30),
    _Gs2328QosIpv6ProtocolUDPDport_Type()
)
gs2328QosIpv6ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6ProtocolUDPDport.setStatus("current")
_Gs2328QosIpv6ProtocolTCPSport_Type = DisplayString
_Gs2328QosIpv6ProtocolTCPSport_Object = MibTableColumn
gs2328QosIpv6ProtocolTCPSport = _Gs2328QosIpv6ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 31),
    _Gs2328QosIpv6ProtocolTCPSport_Type()
)
gs2328QosIpv6ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6ProtocolTCPSport.setStatus("current")
_Gs2328QosIpv6ProtocolTCPDport_Type = DisplayString
_Gs2328QosIpv6ProtocolTCPDport_Object = MibTableColumn
gs2328QosIpv6ProtocolTCPDport = _Gs2328QosIpv6ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 32),
    _Gs2328QosIpv6ProtocolTCPDport_Type()
)
gs2328QosIpv6ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6ProtocolTCPDport.setStatus("current")
_Gs2328QosIpv6Ip_Type = DisplayString
_Gs2328QosIpv6Ip_Object = MibTableColumn
gs2328QosIpv6Ip = _Gs2328QosIpv6Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 33),
    _Gs2328QosIpv6Ip_Type()
)
gs2328QosIpv6Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6Ip.setStatus("current")
_Gs2328QosIpv6Mask_Type = DisplayString
_Gs2328QosIpv6Mask_Object = MibTableColumn
gs2328QosIpv6Mask = _Gs2328QosIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 34),
    _Gs2328QosIpv6Mask_Type()
)
gs2328QosIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6Mask.setStatus("current")
_Gs2328QosIpv6DSCP_Type = DisplayString
_Gs2328QosIpv6DSCP_Object = MibTableColumn
gs2328QosIpv6DSCP = _Gs2328QosIpv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 35),
    _Gs2328QosIpv6DSCP_Type()
)
gs2328QosIpv6DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosIpv6DSCP.setStatus("current")


class _Gs2328QosActionClass_Type(Integer32):
    """Custom type gs2328QosActionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2328QosActionClass_Type.__name__ = "Integer32"
_Gs2328QosActionClass_Object = MibTableColumn
gs2328QosActionClass = _Gs2328QosActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 36),
    _Gs2328QosActionClass_Type()
)
gs2328QosActionClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosActionClass.setStatus("current")


class _Gs2328QosActionDPL_Type(Integer32):
    """Custom type gs2328QosActionDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2328QosActionDPL_Type.__name__ = "Integer32"
_Gs2328QosActionDPL_Object = MibTableColumn
gs2328QosActionDPL = _Gs2328QosActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 37),
    _Gs2328QosActionDPL_Type()
)
gs2328QosActionDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosActionDPL.setStatus("current")


class _Gs2328QosActionDSCP_Type(Integer32):
    """Custom type gs2328QosActionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2328QosActionDSCP_Type.__name__ = "Integer32"
_Gs2328QosActionDSCP_Object = MibTableColumn
gs2328QosActionDSCP = _Gs2328QosActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 38),
    _Gs2328QosActionDSCP_Type()
)
gs2328QosActionDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosActionDSCP.setStatus("current")


class _Gs2328QosQceRowStatus_Type(Integer32):
    """Custom type gs2328QosQceRowStatus based on Integer32"""
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


_Gs2328QosQceRowStatus_Type.__name__ = "Integer32"
_Gs2328QosQceRowStatus_Object = MibTableColumn
gs2328QosQceRowStatus = _Gs2328QosQceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 2, 1, 39),
    _Gs2328QosQceRowStatus_Type()
)
gs2328QosQceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceRowStatus.setStatus("current")


class _Gs2328QosQceMoveID_Type(Integer32):
    """Custom type gs2328QosQceMoveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328QosQceMoveID_Type.__name__ = "Integer32"
_Gs2328QosQceMoveID_Object = MibScalar
gs2328QosQceMoveID = _Gs2328QosQceMoveID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 3),
    _Gs2328QosQceMoveID_Type()
)
gs2328QosQceMoveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceMoveID.setStatus("current")


class _Gs2328QosQceMoveNextID_Type(Integer32):
    """Custom type gs2328QosQceMoveNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328QosQceMoveNextID_Type.__name__ = "Integer32"
_Gs2328QosQceMoveNextID_Object = MibScalar
gs2328QosQceMoveNextID = _Gs2328QosQceMoveNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 9, 4),
    _Gs2328QosQceMoveNextID_Type()
)
gs2328QosQceMoveNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QosQceMoveNextID.setStatus("current")
_Gs2328QosQCLStatusTable_Object = MibTable
gs2328QosQCLStatusTable = _Gs2328QosQCLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10)
)
if mibBuilder.loadTexts:
    gs2328QosQCLStatusTable.setStatus("current")
_Gs2328QosQCLStatusEntry_Object = MibTableRow
gs2328QosQCLStatusEntry = _Gs2328QosQCLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1)
)
gs2328QosQCLStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328QosQCLStatusList"),
)
if mibBuilder.loadTexts:
    gs2328QosQCLStatusEntry.setStatus("current")


class _Gs2328QosQCLStatusList_Type(Integer32):
    """Custom type gs2328QosQCLStatusList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328QosQCLStatusList_Type.__name__ = "Integer32"
_Gs2328QosQCLStatusList_Object = MibTableColumn
gs2328QosQCLStatusList = _Gs2328QosQCLStatusList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 1),
    _Gs2328QosQCLStatusList_Type()
)
gs2328QosQCLStatusList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusList.setStatus("current")
_Gs2328QosQCLStatusUser_Type = DisplayString
_Gs2328QosQCLStatusUser_Object = MibTableColumn
gs2328QosQCLStatusUser = _Gs2328QosQCLStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 2),
    _Gs2328QosQCLStatusUser_Type()
)
gs2328QosQCLStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusUser.setStatus("current")
_Gs2328QosQCLStatusQCEId_Type = DisplayString
_Gs2328QosQCLStatusQCEId_Object = MibTableColumn
gs2328QosQCLStatusQCEId = _Gs2328QosQCLStatusQCEId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 3),
    _Gs2328QosQCLStatusQCEId_Type()
)
gs2328QosQCLStatusQCEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusQCEId.setStatus("current")
_Gs2328QosQCLStatusFrameType_Type = DisplayString
_Gs2328QosQCLStatusFrameType_Object = MibTableColumn
gs2328QosQCLStatusFrameType = _Gs2328QosQCLStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 4),
    _Gs2328QosQCLStatusFrameType_Type()
)
gs2328QosQCLStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusFrameType.setStatus("current")
_Gs2328QosQCLStatusPortlist_Type = DisplayString
_Gs2328QosQCLStatusPortlist_Object = MibTableColumn
gs2328QosQCLStatusPortlist = _Gs2328QosQCLStatusPortlist_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 5),
    _Gs2328QosQCLStatusPortlist_Type()
)
gs2328QosQCLStatusPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusPortlist.setStatus("current")
_Gs2328QosQCLStatusActionClass_Type = DisplayString
_Gs2328QosQCLStatusActionClass_Object = MibTableColumn
gs2328QosQCLStatusActionClass = _Gs2328QosQCLStatusActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 6),
    _Gs2328QosQCLStatusActionClass_Type()
)
gs2328QosQCLStatusActionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusActionClass.setStatus("current")
_Gs2328QosQCLStatusActionDPL_Type = DisplayString
_Gs2328QosQCLStatusActionDPL_Object = MibTableColumn
gs2328QosQCLStatusActionDPL = _Gs2328QosQCLStatusActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 7),
    _Gs2328QosQCLStatusActionDPL_Type()
)
gs2328QosQCLStatusActionDPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusActionDPL.setStatus("current")
_Gs2328QosQCLStatusActionDSCP_Type = DisplayString
_Gs2328QosQCLStatusActionDSCP_Object = MibTableColumn
gs2328QosQCLStatusActionDSCP = _Gs2328QosQCLStatusActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 8),
    _Gs2328QosQCLStatusActionDSCP_Type()
)
gs2328QosQCLStatusActionDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusActionDSCP.setStatus("current")
_Gs2328QosQCLStatusActionConflict_Type = DisplayString
_Gs2328QosQCLStatusActionConflict_Object = MibTableColumn
gs2328QosQCLStatusActionConflict = _Gs2328QosQCLStatusActionConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 10, 1, 9),
    _Gs2328QosQCLStatusActionConflict_Type()
)
gs2328QosQCLStatusActionConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328QosQCLStatusActionConflict.setStatus("current")
_Gs2328QosStormControl_ObjectIdentity = ObjectIdentity
gs2328QosStormControl = _Gs2328QosStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11)
)


class _Gs2328QoSStormControlUC_Type(Integer32):
    """Custom type gs2328QoSStormControlUC based on Integer32"""
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


_Gs2328QoSStormControlUC_Type.__name__ = "Integer32"
_Gs2328QoSStormControlUC_Object = MibScalar
gs2328QoSStormControlUC = _Gs2328QoSStormControlUC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11, 2),
    _Gs2328QoSStormControlUC_Type()
)
gs2328QoSStormControlUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSStormControlUC.setStatus("current")
_Gs2328QoSStormControlUCRate_Type = DisplayString
_Gs2328QoSStormControlUCRate_Object = MibScalar
gs2328QoSStormControlUCRate = _Gs2328QoSStormControlUCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11, 3),
    _Gs2328QoSStormControlUCRate_Type()
)
gs2328QoSStormControlUCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSStormControlUCRate.setStatus("current")


class _Gs2328QoSStormControlMC_Type(Integer32):
    """Custom type gs2328QoSStormControlMC based on Integer32"""
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


_Gs2328QoSStormControlMC_Type.__name__ = "Integer32"
_Gs2328QoSStormControlMC_Object = MibScalar
gs2328QoSStormControlMC = _Gs2328QoSStormControlMC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11, 4),
    _Gs2328QoSStormControlMC_Type()
)
gs2328QoSStormControlMC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSStormControlMC.setStatus("current")
_Gs2328QoSStormControlMCRate_Type = DisplayString
_Gs2328QoSStormControlMCRate_Object = MibScalar
gs2328QoSStormControlMCRate = _Gs2328QoSStormControlMCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11, 5),
    _Gs2328QoSStormControlMCRate_Type()
)
gs2328QoSStormControlMCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSStormControlMCRate.setStatus("current")


class _Gs2328QoSStormControlBC_Type(Integer32):
    """Custom type gs2328QoSStormControlBC based on Integer32"""
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


_Gs2328QoSStormControlBC_Type.__name__ = "Integer32"
_Gs2328QoSStormControlBC_Object = MibScalar
gs2328QoSStormControlBC = _Gs2328QoSStormControlBC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11, 6),
    _Gs2328QoSStormControlBC_Type()
)
gs2328QoSStormControlBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSStormControlBC.setStatus("current")
_Gs2328QoSStormControlBCRate_Type = DisplayString
_Gs2328QoSStormControlBCRate_Object = MibScalar
gs2328QoSStormControlBCRate = _Gs2328QoSStormControlBCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 14, 11, 7),
    _Gs2328QoSStormControlBCRate_Type()
)
gs2328QoSStormControlBCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328QoSStormControlBCRate.setStatus("current")
_Gs2328Vlan_ObjectIdentity = ObjectIdentity
gs2328Vlan = _Gs2328Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15)
)
_Gs2328VlanPorts_ObjectIdentity = ObjectIdentity
gs2328VlanPorts = _Gs2328VlanPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1)
)


class _Gs2328VlanPortsTPIDforCustomSport_Type(OctetString):
    """Custom type gs2328VlanPortsTPIDforCustomSport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Gs2328VlanPortsTPIDforCustomSport_Type.__name__ = "OctetString"
_Gs2328VlanPortsTPIDforCustomSport_Object = MibScalar
gs2328VlanPortsTPIDforCustomSport = _Gs2328VlanPortsTPIDforCustomSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 1),
    _Gs2328VlanPortsTPIDforCustomSport_Type()
)
gs2328VlanPortsTPIDforCustomSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortsTPIDforCustomSport.setStatus("current")
_Gs2328VlanPortsTable_Object = MibTable
gs2328VlanPortsTable = _Gs2328VlanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328VlanPortsTable.setStatus("current")
_Gs2328VlanPortsEntry_Object = MibTableRow
gs2328VlanPortsEntry = _Gs2328VlanPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1)
)
gs2328VlanPortsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328VlanPortsPort"),
)
if mibBuilder.loadTexts:
    gs2328VlanPortsEntry.setStatus("current")


class _Gs2328VlanPortsPort_Type(Integer32):
    """Custom type gs2328VlanPortsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328VlanPortsPort_Type.__name__ = "Integer32"
_Gs2328VlanPortsPort_Object = MibTableColumn
gs2328VlanPortsPort = _Gs2328VlanPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1, 1),
    _Gs2328VlanPortsPort_Type()
)
gs2328VlanPortsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328VlanPortsPort.setStatus("current")


class _Gs2328VlanPortsPVID_Type(Integer32):
    """Custom type gs2328VlanPortsPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328VlanPortsPVID_Type.__name__ = "Integer32"
_Gs2328VlanPortsPVID_Object = MibTableColumn
gs2328VlanPortsPVID = _Gs2328VlanPortsPVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1, 2),
    _Gs2328VlanPortsPVID_Type()
)
gs2328VlanPortsPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortsPVID.setStatus("current")


class _Gs2328VlanPortsFrameType_Type(Integer32):
    """Custom type gs2328VlanPortsFrameType based on Integer32"""
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


_Gs2328VlanPortsFrameType_Type.__name__ = "Integer32"
_Gs2328VlanPortsFrameType_Object = MibTableColumn
gs2328VlanPortsFrameType = _Gs2328VlanPortsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1, 3),
    _Gs2328VlanPortsFrameType_Type()
)
gs2328VlanPortsFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortsFrameType.setStatus("current")


class _Gs2328VlanPortsIngressFilter_Type(Integer32):
    """Custom type gs2328VlanPortsIngressFilter based on Integer32"""
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


_Gs2328VlanPortsIngressFilter_Type.__name__ = "Integer32"
_Gs2328VlanPortsIngressFilter_Object = MibTableColumn
gs2328VlanPortsIngressFilter = _Gs2328VlanPortsIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1, 4),
    _Gs2328VlanPortsIngressFilter_Type()
)
gs2328VlanPortsIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortsIngressFilter.setStatus("current")


class _Gs2328VlanPortsEgressRule_Type(Integer32):
    """Custom type gs2328VlanPortsEgressRule based on Integer32"""
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


_Gs2328VlanPortsEgressRule_Type.__name__ = "Integer32"
_Gs2328VlanPortsEgressRule_Object = MibTableColumn
gs2328VlanPortsEgressRule = _Gs2328VlanPortsEgressRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1, 5),
    _Gs2328VlanPortsEgressRule_Type()
)
gs2328VlanPortsEgressRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortsEgressRule.setStatus("current")


class _Gs2328VlanPortsPortType_Type(Integer32):
    """Custom type gs2328VlanPortsPortType based on Integer32"""
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


_Gs2328VlanPortsPortType_Type.__name__ = "Integer32"
_Gs2328VlanPortsPortType_Object = MibTableColumn
gs2328VlanPortsPortType = _Gs2328VlanPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 1, 2, 1, 6),
    _Gs2328VlanPortsPortType_Type()
)
gs2328VlanPortsPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortsPortType.setStatus("current")
_Gs2328VlanPrivateVLAN_ObjectIdentity = ObjectIdentity
gs2328VlanPrivateVLAN = _Gs2328VlanPrivateVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2)
)
_Gs2328VlanPrivateVLANMembership_ObjectIdentity = ObjectIdentity
gs2328VlanPrivateVLANMembership = _Gs2328VlanPrivateVLANMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1)
)


class _Gs2328VlanPrivateVLANMembershipCreate_Type(Integer32):
    """Custom type gs2328VlanPrivateVLANMembershipCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328VlanPrivateVLANMembershipCreate_Type.__name__ = "Integer32"
_Gs2328VlanPrivateVLANMembershipCreate_Object = MibScalar
gs2328VlanPrivateVLANMembershipCreate = _Gs2328VlanPrivateVLANMembershipCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 1),
    _Gs2328VlanPrivateVLANMembershipCreate_Type()
)
gs2328VlanPrivateVLANMembershipCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANMembershipCreate.setStatus("current")
_Gs2328VlanPrivateVLANMembershipTable_Object = MibTable
gs2328VlanPrivateVLANMembershipTable = _Gs2328VlanPrivateVLANMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANMembershipTable.setStatus("current")
_Gs2328VlanPrivateVLANMembershipEntry_Object = MibTableRow
gs2328VlanPrivateVLANMembershipEntry = _Gs2328VlanPrivateVLANMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 2, 1)
)
gs2328VlanPrivateVLANMembershipEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328VlanPrivateVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANMembershipEntry.setStatus("current")


class _Gs2328VlanPrivateVLANIndex_Type(Integer32):
    """Custom type gs2328VlanPrivateVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2328VlanPrivateVLANIndex_Type.__name__ = "Integer32"
_Gs2328VlanPrivateVLANIndex_Object = MibTableColumn
gs2328VlanPrivateVLANIndex = _Gs2328VlanPrivateVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 2, 1, 1),
    _Gs2328VlanPrivateVLANIndex_Type()
)
gs2328VlanPrivateVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANIndex.setStatus("current")


class _Gs2328VlanPrivateVLANID_Type(Integer32):
    """Custom type gs2328VlanPrivateVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2328VlanPrivateVLANID_Type.__name__ = "Integer32"
_Gs2328VlanPrivateVLANID_Object = MibTableColumn
gs2328VlanPrivateVLANID = _Gs2328VlanPrivateVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 2, 1, 2),
    _Gs2328VlanPrivateVLANID_Type()
)
gs2328VlanPrivateVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANID.setStatus("current")
_Gs2328VlanPrivateVLANMemberships_Type = DisplayString
_Gs2328VlanPrivateVLANMemberships_Object = MibTableColumn
gs2328VlanPrivateVLANMemberships = _Gs2328VlanPrivateVLANMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 2, 1, 3),
    _Gs2328VlanPrivateVLANMemberships_Type()
)
gs2328VlanPrivateVLANMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANMemberships.setStatus("current")


class _Gs2328VlanPrivateVLANRowStatus_Type(Integer32):
    """Custom type gs2328VlanPrivateVLANRowStatus based on Integer32"""
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


_Gs2328VlanPrivateVLANRowStatus_Type.__name__ = "Integer32"
_Gs2328VlanPrivateVLANRowStatus_Object = MibTableColumn
gs2328VlanPrivateVLANRowStatus = _Gs2328VlanPrivateVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 1, 2, 1, 4),
    _Gs2328VlanPrivateVLANRowStatus_Type()
)
gs2328VlanPrivateVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPrivateVLANRowStatus.setStatus("current")
_Gs2328VlanPortIsolationTable_Object = MibTable
gs2328VlanPortIsolationTable = _Gs2328VlanPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328VlanPortIsolationTable.setStatus("current")
_Gs2328VlanPortIsolationEntry_Object = MibTableRow
gs2328VlanPortIsolationEntry = _Gs2328VlanPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 2, 1)
)
gs2328VlanPortIsolationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328VlanPortIsolationPort"),
)
if mibBuilder.loadTexts:
    gs2328VlanPortIsolationEntry.setStatus("current")


class _Gs2328VlanPortIsolationPort_Type(Integer32):
    """Custom type gs2328VlanPortIsolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328VlanPortIsolationPort_Type.__name__ = "Integer32"
_Gs2328VlanPortIsolationPort_Object = MibTableColumn
gs2328VlanPortIsolationPort = _Gs2328VlanPortIsolationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 2, 1, 1),
    _Gs2328VlanPortIsolationPort_Type()
)
gs2328VlanPortIsolationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328VlanPortIsolationPort.setStatus("current")


class _Gs2328VlanPortIsolation_Type(Integer32):
    """Custom type gs2328VlanPortIsolation based on Integer32"""
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


_Gs2328VlanPortIsolation_Type.__name__ = "Integer32"
_Gs2328VlanPortIsolation_Object = MibTableColumn
gs2328VlanPortIsolation = _Gs2328VlanPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 2, 2, 1, 2),
    _Gs2328VlanPortIsolation_Type()
)
gs2328VlanPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328VlanPortIsolation.setStatus("current")
_Gs2328MACbasedVLAN_ObjectIdentity = ObjectIdentity
gs2328MACbasedVLAN = _Gs2328MACbasedVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3)
)
_Gs2328MACbasedVLANConf_ObjectIdentity = ObjectIdentity
gs2328MACbasedVLANConf = _Gs2328MACbasedVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1)
)
_Gs2328MACbasedVLANConfCreate_Type = Integer32
_Gs2328MACbasedVLANConfCreate_Object = MibScalar
gs2328MACbasedVLANConfCreate = _Gs2328MACbasedVLANConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 1),
    _Gs2328MACbasedVLANConfCreate_Type()
)
gs2328MACbasedVLANConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACbasedVLANConfCreate.setStatus("current")
_Gs2328MACbasedVLANConfTable_Object = MibTable
gs2328MACbasedVLANConfTable = _Gs2328MACbasedVLANConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328MACbasedVLANConfTable.setStatus("current")
_Gs2328MACbasedVLANConfEntry_Object = MibTableRow
gs2328MACbasedVLANConfEntry = _Gs2328MACbasedVLANConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2, 1)
)
gs2328MACbasedVLANConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MACbasedVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2328MACbasedVLANConfEntry.setStatus("current")


class _Gs2328MACbasedVLANIndex_Type(Integer32):
    """Custom type gs2328MACbasedVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328MACbasedVLANIndex_Type.__name__ = "Integer32"
_Gs2328MACbasedVLANIndex_Object = MibTableColumn
gs2328MACbasedVLANIndex = _Gs2328MACbasedVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2, 1, 1),
    _Gs2328MACbasedVLANIndex_Type()
)
gs2328MACbasedVLANIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACbasedVLANIndex.setStatus("current")
_Gs2328MACbasedVLANMACAddress_Type = MacAddress
_Gs2328MACbasedVLANMACAddress_Object = MibTableColumn
gs2328MACbasedVLANMACAddress = _Gs2328MACbasedVLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2, 1, 2),
    _Gs2328MACbasedVLANMACAddress_Type()
)
gs2328MACbasedVLANMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACbasedVLANMACAddress.setStatus("current")


class _Gs2328MACbasedVLANID_Type(Integer32):
    """Custom type gs2328MACbasedVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328MACbasedVLANID_Type.__name__ = "Integer32"
_Gs2328MACbasedVLANID_Object = MibTableColumn
gs2328MACbasedVLANID = _Gs2328MACbasedVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2, 1, 3),
    _Gs2328MACbasedVLANID_Type()
)
gs2328MACbasedVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACbasedVLANID.setStatus("current")
_Gs2328MACbasedMemberships_Type = DisplayString
_Gs2328MACbasedMemberships_Object = MibTableColumn
gs2328MACbasedMemberships = _Gs2328MACbasedMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2, 1, 4),
    _Gs2328MACbasedMemberships_Type()
)
gs2328MACbasedMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACbasedMemberships.setStatus("current")


class _Gs2328MACbaseRowStatus_Type(Integer32):
    """Custom type gs2328MACbaseRowStatus based on Integer32"""
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


_Gs2328MACbaseRowStatus_Type.__name__ = "Integer32"
_Gs2328MACbaseRowStatus_Object = MibTableColumn
gs2328MACbaseRowStatus = _Gs2328MACbaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 15, 3, 1, 2, 1, 5),
    _Gs2328MACbaseRowStatus_Type()
)
gs2328MACbaseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MACbaseRowStatus.setStatus("current")
_Gs2328IGMPSnooping_ObjectIdentity = ObjectIdentity
gs2328IGMPSnooping = _Gs2328IGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16)
)
_Gs2328IGMPSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2328IGMPSnoopingBasic = _Gs2328IGMPSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1)
)


class _Gs2328IGMPSnoopingEnable_Type(Integer32):
    """Custom type gs2328IGMPSnoopingEnable based on Integer32"""
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


_Gs2328IGMPSnoopingEnable_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingEnable_Object = MibScalar
gs2328IGMPSnoopingEnable = _Gs2328IGMPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 1),
    _Gs2328IGMPSnoopingEnable_Type()
)
gs2328IGMPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingEnable.setStatus("current")


class _Gs2328IGMPSnoopingUnregisteredIPMCv4Flooding_Type(Integer32):
    """Custom type gs2328IGMPSnoopingUnregisteredIPMCv4Flooding based on Integer32"""
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


_Gs2328IGMPSnoopingUnregisteredIPMCv4Flooding_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingUnregisteredIPMCv4Flooding_Object = MibScalar
gs2328IGMPSnoopingUnregisteredIPMCv4Flooding = _Gs2328IGMPSnoopingUnregisteredIPMCv4Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 2),
    _Gs2328IGMPSnoopingUnregisteredIPMCv4Flooding_Type()
)
gs2328IGMPSnoopingUnregisteredIPMCv4Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingUnregisteredIPMCv4Flooding.setStatus("current")
_Gs2328IGMPSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2328IGMPSnoopingSSMIPRangeAddr_Object = MibScalar
gs2328IGMPSnoopingSSMIPRangeAddr = _Gs2328IGMPSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 3),
    _Gs2328IGMPSnoopingSSMIPRangeAddr_Type()
)
gs2328IGMPSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2328IGMPSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2328IGMPSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_Gs2328IGMPSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingSSMIPRangeValue_Object = MibScalar
gs2328IGMPSnoopingSSMIPRangeValue = _Gs2328IGMPSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 4),
    _Gs2328IGMPSnoopingSSMIPRangeValue_Type()
)
gs2328IGMPSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2328IGMPSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2328IGMPSnoopingProxyEnabled based on Integer32"""
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


_Gs2328IGMPSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingProxyEnabled_Object = MibScalar
gs2328IGMPSnoopingProxyEnabled = _Gs2328IGMPSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 5),
    _Gs2328IGMPSnoopingProxyEnabled_Type()
)
gs2328IGMPSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingProxyEnabled.setStatus("current")
_Gs2328IGMPSnoopingPortRelatedTable_Object = MibTable
gs2328IGMPSnoopingPortRelatedTable = _Gs2328IGMPSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortRelatedTable.setStatus("current")
_Gs2328IGMPSnoopingPortRelatedEntry_Object = MibTableRow
gs2328IGMPSnoopingPortRelatedEntry = _Gs2328IGMPSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 6, 1)
)
gs2328IGMPSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortRelatedEntry.setStatus("current")


class _Gs2328IGMPSnoopingRouterPort_Type(Integer32):
    """Custom type gs2328IGMPSnoopingRouterPort based on Integer32"""
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


_Gs2328IGMPSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingRouterPort_Object = MibTableColumn
gs2328IGMPSnoopingRouterPort = _Gs2328IGMPSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 6, 1, 1),
    _Gs2328IGMPSnoopingRouterPort_Type()
)
gs2328IGMPSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingRouterPort.setStatus("current")


class _Gs2328IGMPSnoopingFastLeave_Type(Integer32):
    """Custom type gs2328IGMPSnoopingFastLeave based on Integer32"""
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


_Gs2328IGMPSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingFastLeave_Object = MibTableColumn
gs2328IGMPSnoopingFastLeave = _Gs2328IGMPSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 6, 1, 2),
    _Gs2328IGMPSnoopingFastLeave_Type()
)
gs2328IGMPSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingFastLeave.setStatus("current")


class _Gs2328IGMPSnoopingThrottling_Type(Integer32):
    """Custom type gs2328IGMPSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2328IGMPSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingThrottling_Object = MibTableColumn
gs2328IGMPSnoopingThrottling = _Gs2328IGMPSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 1, 6, 1, 3),
    _Gs2328IGMPSnoopingThrottling_Type()
)
gs2328IGMPSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingThrottling.setStatus("current")
_Gs2328IGMPSnoopingVLANTable_Object = MibTable
gs2328IGMPSnoopingVLANTable = _Gs2328IGMPSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANTable.setStatus("current")
_Gs2328IGMPSnoopingVLANEntry_Object = MibTableRow
gs2328IGMPSnoopingVLANEntry = _Gs2328IGMPSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1)
)
gs2328IGMPSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IGMPSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANEntry.setStatus("current")


class _Gs2328IGMPSnoopingVLANID_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IGMPSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANID_Object = MibTableColumn
gs2328IGMPSnoopingVLANID = _Gs2328IGMPSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 1),
    _Gs2328IGMPSnoopingVLANID_Type()
)
gs2328IGMPSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANID.setStatus("current")


class _Gs2328IGMPSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANEnable based on Integer32"""
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


_Gs2328IGMPSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANEnable_Object = MibTableColumn
gs2328IGMPSnoopingVLANEnable = _Gs2328IGMPSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 2),
    _Gs2328IGMPSnoopingVLANEnable_Type()
)
gs2328IGMPSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANEnable.setStatus("current")


class _Gs2328IGMPSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANIGMPQuerier based on Integer32"""
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


_Gs2328IGMPSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2328IGMPSnoopingVLANIGMPQuerier = _Gs2328IGMPSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 3),
    _Gs2328IGMPSnoopingVLANIGMPQuerier_Type()
)
gs2328IGMPSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2328IGMPSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANCompatibility based on Integer32"""
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


_Gs2328IGMPSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANCompatibility_Object = MibTableColumn
gs2328IGMPSnoopingVLANCompatibility = _Gs2328IGMPSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 4),
    _Gs2328IGMPSnoopingVLANCompatibility_Type()
)
gs2328IGMPSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANCompatibility.setStatus("current")


class _Gs2328IGMPSnoopingVLANRV_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2328IGMPSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANRV_Object = MibTableColumn
gs2328IGMPSnoopingVLANRV = _Gs2328IGMPSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 5),
    _Gs2328IGMPSnoopingVLANRV_Type()
)
gs2328IGMPSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANRV.setStatus("current")


class _Gs2328IGMPSnoopingVLANQI_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2328IGMPSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANQI_Object = MibTableColumn
gs2328IGMPSnoopingVLANQI = _Gs2328IGMPSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 6),
    _Gs2328IGMPSnoopingVLANQI_Type()
)
gs2328IGMPSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANQI.setStatus("current")


class _Gs2328IGMPSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328IGMPSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANQRI_Object = MibTableColumn
gs2328IGMPSnoopingVLANQRI = _Gs2328IGMPSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 7),
    _Gs2328IGMPSnoopingVLANQRI_Type()
)
gs2328IGMPSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANQRI.setStatus("current")


class _Gs2328IGMPSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328IGMPSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANLLQI_Object = MibTableColumn
gs2328IGMPSnoopingVLANLLQI = _Gs2328IGMPSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 8),
    _Gs2328IGMPSnoopingVLANLLQI_Type()
)
gs2328IGMPSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANLLQI.setStatus("current")


class _Gs2328IGMPSnoopingVLANURI_Type(Integer32):
    """Custom type gs2328IGMPSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328IGMPSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingVLANURI_Object = MibTableColumn
gs2328IGMPSnoopingVLANURI = _Gs2328IGMPSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 2, 1, 9),
    _Gs2328IGMPSnoopingVLANURI_Type()
)
gs2328IGMPSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingVLANURI.setStatus("current")
_Gs2328IGMPSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2328IGMPSnoopingPortGroupFiltering = _Gs2328IGMPSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3)
)
_Gs2328IGMPSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2328IGMPSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2328IGMPSnoopingPortGroupFilteringCreate = _Gs2328IGMPSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 1),
    _Gs2328IGMPSnoopingPortGroupFilteringCreate_Type()
)
gs2328IGMPSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2328IGMPSnoopingPortGroupFilteringTable_Object = MibTable
gs2328IGMPSnoopingPortGroupFilteringTable = _Gs2328IGMPSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2328IGMPSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2328IGMPSnoopingPortGroupFilteringEntry = _Gs2328IGMPSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 2, 1)
)
gs2328IGMPSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IGMPSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2328IGMPSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2328IGMPSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328IGMPSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2328IGMPSnoopingPortGroupFilteringIndex = _Gs2328IGMPSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 2, 1, 1),
    _Gs2328IGMPSnoopingPortGroupFilteringIndex_Type()
)
gs2328IGMPSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2328IGMPSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2328IGMPSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328IGMPSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2328IGMPSnoopingPortGroupFilteringPort = _Gs2328IGMPSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 2, 1, 2),
    _Gs2328IGMPSnoopingPortGroupFilteringPort_Type()
)
gs2328IGMPSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2328IGMPSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2328IGMPSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2328IGMPSnoopingPortGroupFilteringGroups = _Gs2328IGMPSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 2, 1, 3),
    _Gs2328IGMPSnoopingPortGroupFilteringGroups_Type()
)
gs2328IGMPSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2328IGMPSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2328IGMPSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2328IGMPSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2328IGMPSnoopingPortGroupFilteringRowStatus = _Gs2328IGMPSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 3, 2, 1, 4),
    _Gs2328IGMPSnoopingPortGroupFilteringRowStatus_Type()
)
gs2328IGMPSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2328IGMPSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2328IGMPSnoopingStatus = _Gs2328IGMPSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4)
)


class _Gs2328IGMPSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2328IGMPSnoopingstatisticClear based on Integer32"""
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


_Gs2328IGMPSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingstatisticClear_Object = MibScalar
gs2328IGMPSnoopingstatisticClear = _Gs2328IGMPSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 1),
    _Gs2328IGMPSnoopingstatisticClear_Type()
)
gs2328IGMPSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticClear.setStatus("current")
_Gs2328IGMPSnoopingstatisticTable_Object = MibTable
gs2328IGMPSnoopingstatisticTable = _Gs2328IGMPSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticTable.setStatus("current")
_Gs2328IGMPSnoopingstatisticEntry_Object = MibTableRow
gs2328IGMPSnoopingstatisticEntry = _Gs2328IGMPSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1)
)
gs2328IGMPSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IGMPSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticEntry.setStatus("current")


class _Gs2328IGMPSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2328IGMPSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IGMPSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingstatisticVLANID_Object = MibTableColumn
gs2328IGMPSnoopingstatisticVLANID = _Gs2328IGMPSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 1),
    _Gs2328IGMPSnoopingstatisticVLANID_Type()
)
gs2328IGMPSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticVLANID.setStatus("current")
_Gs2328IGMPSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2328IGMPSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2328IGMPSnoopingstatisticQuerierVersion = _Gs2328IGMPSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 2),
    _Gs2328IGMPSnoopingstatisticQuerierVersion_Type()
)
gs2328IGMPSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2328IGMPSnoopingstatisticHostVersion_Type = DisplayString
_Gs2328IGMPSnoopingstatisticHostVersion_Object = MibTableColumn
gs2328IGMPSnoopingstatisticHostVersion = _Gs2328IGMPSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 3),
    _Gs2328IGMPSnoopingstatisticHostVersion_Type()
)
gs2328IGMPSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticHostVersion.setStatus("current")
_Gs2328IGMPSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2328IGMPSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2328IGMPSnoopingstatisticQuerierStatus = _Gs2328IGMPSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 4),
    _Gs2328IGMPSnoopingstatisticQuerierStatus_Type()
)
gs2328IGMPSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2328IGMPSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2328IGMPSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2328IGMPSnoopingstatisticQueriesTransmitted = _Gs2328IGMPSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 5),
    _Gs2328IGMPSnoopingstatisticQueriesTransmitted_Type()
)
gs2328IGMPSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2328IGMPSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2328IGMPSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2328IGMPSnoopingstatisticQueriesReceived = _Gs2328IGMPSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 6),
    _Gs2328IGMPSnoopingstatisticQueriesReceived_Type()
)
gs2328IGMPSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2328IGMPSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2328IGMPSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2328IGMPSnoopingstatisticV1ReportsReceived = _Gs2328IGMPSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 7),
    _Gs2328IGMPSnoopingstatisticV1ReportsReceived_Type()
)
gs2328IGMPSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2328IGMPSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2328IGMPSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2328IGMPSnoopingstatisticV2ReportsReceived = _Gs2328IGMPSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 8),
    _Gs2328IGMPSnoopingstatisticV2ReportsReceived_Type()
)
gs2328IGMPSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2328IGMPSnoopingstatisticV3ReportsReceived_Type = Counter32
_Gs2328IGMPSnoopingstatisticV3ReportsReceived_Object = MibTableColumn
gs2328IGMPSnoopingstatisticV3ReportsReceived = _Gs2328IGMPSnoopingstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 9),
    _Gs2328IGMPSnoopingstatisticV3ReportsReceived_Type()
)
gs2328IGMPSnoopingstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticV3ReportsReceived.setStatus("current")
_Gs2328IGMPSnoopingstatisticV2LeavesReceived_Type = Counter32
_Gs2328IGMPSnoopingstatisticV2LeavesReceived_Object = MibTableColumn
gs2328IGMPSnoopingstatisticV2LeavesReceived = _Gs2328IGMPSnoopingstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 2, 1, 10),
    _Gs2328IGMPSnoopingstatisticV2LeavesReceived_Type()
)
gs2328IGMPSnoopingstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingstatisticV2LeavesReceived.setStatus("current")
_Gs2328IGMPSnoopingRouterPortTable_Object = MibTable
gs2328IGMPSnoopingRouterPortTable = _Gs2328IGMPSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 3)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingRouterPortTable.setStatus("current")
_Gs2328IGMPSnoopingRouterPortEntry_Object = MibTableRow
gs2328IGMPSnoopingRouterPortEntry = _Gs2328IGMPSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 3, 1)
)
gs2328IGMPSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingRouterPortEntry.setStatus("current")
_Gs2328IGMPSnoopingRouterPortStatus_Type = DisplayString
_Gs2328IGMPSnoopingRouterPortStatus_Object = MibTableColumn
gs2328IGMPSnoopingRouterPortStatus = _Gs2328IGMPSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 4, 3, 1, 1),
    _Gs2328IGMPSnoopingRouterPortStatus_Type()
)
gs2328IGMPSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingRouterPortStatus.setStatus("current")
_Gs2328IGMPSnoopingGroupsTable_Object = MibTable
gs2328IGMPSnoopingGroupsTable = _Gs2328IGMPSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 5)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingGroupsTable.setStatus("current")
_Gs2328IGMPSnoopingGroupsEntry_Object = MibTableRow
gs2328IGMPSnoopingGroupsEntry = _Gs2328IGMPSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 5, 1)
)
gs2328IGMPSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IGMPSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingGroupsEntry.setStatus("current")


class _Gs2328IGMPSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2328IGMPSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328IGMPSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingGroupsIndex_Object = MibTableColumn
gs2328IGMPSnoopingGroupsIndex = _Gs2328IGMPSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 5, 1, 1),
    _Gs2328IGMPSnoopingGroupsIndex_Type()
)
gs2328IGMPSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingGroupsIndex.setStatus("current")


class _Gs2328IGMPSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2328IGMPSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IGMPSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingGroupsVLANID_Object = MibTableColumn
gs2328IGMPSnoopingGroupsVLANID = _Gs2328IGMPSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 5, 1, 2),
    _Gs2328IGMPSnoopingGroupsVLANID_Type()
)
gs2328IGMPSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingGroupsVLANID.setStatus("current")
_Gs2328IGMPSnoopingGroups_Type = DisplayString
_Gs2328IGMPSnoopingGroups_Object = MibTableColumn
gs2328IGMPSnoopingGroups = _Gs2328IGMPSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 5, 1, 3),
    _Gs2328IGMPSnoopingGroups_Type()
)
gs2328IGMPSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingGroups.setStatus("current")
_Gs2328IGMPSnoopingGroupsMemberships_Type = DisplayString
_Gs2328IGMPSnoopingGroupsMemberships_Object = MibTableColumn
gs2328IGMPSnoopingGroupsMemberships = _Gs2328IGMPSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 5, 1, 4),
    _Gs2328IGMPSnoopingGroupsMemberships_Type()
)
gs2328IGMPSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingGroupsMemberships.setStatus("current")
_Gs2328IGMPSnoopingSSMTable_Object = MibTable
gs2328IGMPSnoopingSSMTable = _Gs2328IGMPSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6)
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMTable.setStatus("current")
_Gs2328IGMPSnoopingSSMEntry_Object = MibTableRow
gs2328IGMPSnoopingSSMEntry = _Gs2328IGMPSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1)
)
gs2328IGMPSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IGMPSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMEntry.setStatus("current")


class _Gs2328IGMPSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2328IGMPSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328IGMPSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingSSMIndex_Object = MibTableColumn
gs2328IGMPSnoopingSSMIndex = _Gs2328IGMPSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 1),
    _Gs2328IGMPSnoopingSSMIndex_Type()
)
gs2328IGMPSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMIndex.setStatus("current")


class _Gs2328IGMPSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2328IGMPSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IGMPSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingSSMVLANID_Object = MibTableColumn
gs2328IGMPSnoopingSSMVLANID = _Gs2328IGMPSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 2),
    _Gs2328IGMPSnoopingSSMVLANID_Type()
)
gs2328IGMPSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMVLANID.setStatus("current")
_Gs2328IGMPSnoopingSSMGroup_Type = DisplayString
_Gs2328IGMPSnoopingSSMGroup_Object = MibTableColumn
gs2328IGMPSnoopingSSMGroup = _Gs2328IGMPSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 3),
    _Gs2328IGMPSnoopingSSMGroup_Type()
)
gs2328IGMPSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMGroup.setStatus("current")


class _Gs2328IGMPSnoopingSSMPort_Type(Integer32):
    """Custom type gs2328IGMPSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328IGMPSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2328IGMPSnoopingSSMPort_Object = MibTableColumn
gs2328IGMPSnoopingSSMPort = _Gs2328IGMPSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 4),
    _Gs2328IGMPSnoopingSSMPort_Type()
)
gs2328IGMPSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMPort.setStatus("current")
_Gs2328IGMPSnoopingSSMMode_Type = DisplayString
_Gs2328IGMPSnoopingSSMMode_Object = MibTableColumn
gs2328IGMPSnoopingSSMMode = _Gs2328IGMPSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 5),
    _Gs2328IGMPSnoopingSSMMode_Type()
)
gs2328IGMPSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMMode.setStatus("current")
_Gs2328IGMPSnoopingSSMSourceAddress_Type = DisplayString
_Gs2328IGMPSnoopingSSMSourceAddress_Object = MibTableColumn
gs2328IGMPSnoopingSSMSourceAddress = _Gs2328IGMPSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 6),
    _Gs2328IGMPSnoopingSSMSourceAddress_Type()
)
gs2328IGMPSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMSourceAddress.setStatus("current")
_Gs2328IGMPSnoopingSSMType_Type = DisplayString
_Gs2328IGMPSnoopingSSMType_Object = MibTableColumn
gs2328IGMPSnoopingSSMType = _Gs2328IGMPSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 16, 6, 1, 7),
    _Gs2328IGMPSnoopingSSMType_Type()
)
gs2328IGMPSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IGMPSnoopingSSMType.setStatus("current")
_Gs2328MLDSnooping_ObjectIdentity = ObjectIdentity
gs2328MLDSnooping = _Gs2328MLDSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17)
)
_Gs2328MLDSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2328MLDSnoopingBasic = _Gs2328MLDSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1)
)


class _Gs2328MLDSnoopingEnable_Type(Integer32):
    """Custom type gs2328MLDSnoopingEnable based on Integer32"""
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


_Gs2328MLDSnoopingEnable_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingEnable_Object = MibScalar
gs2328MLDSnoopingEnable = _Gs2328MLDSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 1),
    _Gs2328MLDSnoopingEnable_Type()
)
gs2328MLDSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingEnable.setStatus("current")


class _Gs2328MLDSnoopingUnregisteredIPMCv6Flooding_Type(Integer32):
    """Custom type gs2328MLDSnoopingUnregisteredIPMCv6Flooding based on Integer32"""
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


_Gs2328MLDSnoopingUnregisteredIPMCv6Flooding_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingUnregisteredIPMCv6Flooding_Object = MibScalar
gs2328MLDSnoopingUnregisteredIPMCv6Flooding = _Gs2328MLDSnoopingUnregisteredIPMCv6Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 2),
    _Gs2328MLDSnoopingUnregisteredIPMCv6Flooding_Type()
)
gs2328MLDSnoopingUnregisteredIPMCv6Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingUnregisteredIPMCv6Flooding.setStatus("current")
_Gs2328MLDSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2328MLDSnoopingSSMIPRangeAddr_Object = MibScalar
gs2328MLDSnoopingSSMIPRangeAddr = _Gs2328MLDSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 3),
    _Gs2328MLDSnoopingSSMIPRangeAddr_Type()
)
gs2328MLDSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2328MLDSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2328MLDSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_Gs2328MLDSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingSSMIPRangeValue_Object = MibScalar
gs2328MLDSnoopingSSMIPRangeValue = _Gs2328MLDSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 4),
    _Gs2328MLDSnoopingSSMIPRangeValue_Type()
)
gs2328MLDSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2328MLDSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2328MLDSnoopingProxyEnabled based on Integer32"""
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


_Gs2328MLDSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingProxyEnabled_Object = MibScalar
gs2328MLDSnoopingProxyEnabled = _Gs2328MLDSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 5),
    _Gs2328MLDSnoopingProxyEnabled_Type()
)
gs2328MLDSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingProxyEnabled.setStatus("current")
_Gs2328MLDSnoopingPortRelatedTable_Object = MibTable
gs2328MLDSnoopingPortRelatedTable = _Gs2328MLDSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 6)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortRelatedTable.setStatus("current")
_Gs2328MLDSnoopingPortRelatedEntry_Object = MibTableRow
gs2328MLDSnoopingPortRelatedEntry = _Gs2328MLDSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 6, 1)
)
gs2328MLDSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortRelatedEntry.setStatus("current")


class _Gs2328MLDSnoopingRouterPort_Type(Integer32):
    """Custom type gs2328MLDSnoopingRouterPort based on Integer32"""
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


_Gs2328MLDSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingRouterPort_Object = MibTableColumn
gs2328MLDSnoopingRouterPort = _Gs2328MLDSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 6, 1, 1),
    _Gs2328MLDSnoopingRouterPort_Type()
)
gs2328MLDSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingRouterPort.setStatus("current")


class _Gs2328MLDSnoopingFastLeave_Type(Integer32):
    """Custom type gs2328MLDSnoopingFastLeave based on Integer32"""
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


_Gs2328MLDSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingFastLeave_Object = MibTableColumn
gs2328MLDSnoopingFastLeave = _Gs2328MLDSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 6, 1, 2),
    _Gs2328MLDSnoopingFastLeave_Type()
)
gs2328MLDSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingFastLeave.setStatus("current")


class _Gs2328MLDSnoopingThrottling_Type(Integer32):
    """Custom type gs2328MLDSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2328MLDSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingThrottling_Object = MibTableColumn
gs2328MLDSnoopingThrottling = _Gs2328MLDSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 1, 6, 1, 3),
    _Gs2328MLDSnoopingThrottling_Type()
)
gs2328MLDSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingThrottling.setStatus("current")
_Gs2328MLDSnoopingVLANTable_Object = MibTable
gs2328MLDSnoopingVLANTable = _Gs2328MLDSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANTable.setStatus("current")
_Gs2328MLDSnoopingVLANEntry_Object = MibTableRow
gs2328MLDSnoopingVLANEntry = _Gs2328MLDSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1)
)
gs2328MLDSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MLDSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANEntry.setStatus("current")


class _Gs2328MLDSnoopingVLANID_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MLDSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANID_Object = MibTableColumn
gs2328MLDSnoopingVLANID = _Gs2328MLDSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 1),
    _Gs2328MLDSnoopingVLANID_Type()
)
gs2328MLDSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANID.setStatus("current")


class _Gs2328MLDSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANEnable based on Integer32"""
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


_Gs2328MLDSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANEnable_Object = MibTableColumn
gs2328MLDSnoopingVLANEnable = _Gs2328MLDSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 2),
    _Gs2328MLDSnoopingVLANEnable_Type()
)
gs2328MLDSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANEnable.setStatus("current")


class _Gs2328MLDSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANIGMPQuerier based on Integer32"""
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


_Gs2328MLDSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2328MLDSnoopingVLANIGMPQuerier = _Gs2328MLDSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 3),
    _Gs2328MLDSnoopingVLANIGMPQuerier_Type()
)
gs2328MLDSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2328MLDSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANCompatibility based on Integer32"""
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


_Gs2328MLDSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANCompatibility_Object = MibTableColumn
gs2328MLDSnoopingVLANCompatibility = _Gs2328MLDSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 4),
    _Gs2328MLDSnoopingVLANCompatibility_Type()
)
gs2328MLDSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANCompatibility.setStatus("current")


class _Gs2328MLDSnoopingVLANRV_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2328MLDSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANRV_Object = MibTableColumn
gs2328MLDSnoopingVLANRV = _Gs2328MLDSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 5),
    _Gs2328MLDSnoopingVLANRV_Type()
)
gs2328MLDSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANRV.setStatus("current")


class _Gs2328MLDSnoopingVLANQI_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2328MLDSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANQI_Object = MibTableColumn
gs2328MLDSnoopingVLANQI = _Gs2328MLDSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 6),
    _Gs2328MLDSnoopingVLANQI_Type()
)
gs2328MLDSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANQI.setStatus("current")


class _Gs2328MLDSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328MLDSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANQRI_Object = MibTableColumn
gs2328MLDSnoopingVLANQRI = _Gs2328MLDSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 7),
    _Gs2328MLDSnoopingVLANQRI_Type()
)
gs2328MLDSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANQRI.setStatus("current")


class _Gs2328MLDSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328MLDSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANLLQI_Object = MibTableColumn
gs2328MLDSnoopingVLANLLQI = _Gs2328MLDSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 8),
    _Gs2328MLDSnoopingVLANLLQI_Type()
)
gs2328MLDSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANLLQI.setStatus("current")


class _Gs2328MLDSnoopingVLANURI_Type(Integer32):
    """Custom type gs2328MLDSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328MLDSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingVLANURI_Object = MibTableColumn
gs2328MLDSnoopingVLANURI = _Gs2328MLDSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 2, 1, 9),
    _Gs2328MLDSnoopingVLANURI_Type()
)
gs2328MLDSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingVLANURI.setStatus("current")
_Gs2328MLDSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2328MLDSnoopingPortGroupFiltering = _Gs2328MLDSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3)
)
_Gs2328MLDSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2328MLDSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2328MLDSnoopingPortGroupFilteringCreate = _Gs2328MLDSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 1),
    _Gs2328MLDSnoopingPortGroupFilteringCreate_Type()
)
gs2328MLDSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2328MLDSnoopingPortGroupFilteringTable_Object = MibTable
gs2328MLDSnoopingPortGroupFilteringTable = _Gs2328MLDSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2328MLDSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2328MLDSnoopingPortGroupFilteringEntry = _Gs2328MLDSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 2, 1)
)
gs2328MLDSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MLDSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2328MLDSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2328MLDSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MLDSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2328MLDSnoopingPortGroupFilteringIndex = _Gs2328MLDSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 2, 1, 1),
    _Gs2328MLDSnoopingPortGroupFilteringIndex_Type()
)
gs2328MLDSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2328MLDSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2328MLDSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MLDSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2328MLDSnoopingPortGroupFilteringPort = _Gs2328MLDSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 2, 1, 2),
    _Gs2328MLDSnoopingPortGroupFilteringPort_Type()
)
gs2328MLDSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2328MLDSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2328MLDSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2328MLDSnoopingPortGroupFilteringGroups = _Gs2328MLDSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 2, 1, 3),
    _Gs2328MLDSnoopingPortGroupFilteringGroups_Type()
)
gs2328MLDSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2328MLDSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2328MLDSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2328MLDSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2328MLDSnoopingPortGroupFilteringRowStatus = _Gs2328MLDSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 3, 2, 1, 4),
    _Gs2328MLDSnoopingPortGroupFilteringRowStatus_Type()
)
gs2328MLDSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2328MLDSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2328MLDSnoopingStatus = _Gs2328MLDSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4)
)


class _Gs2328MLDSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2328MLDSnoopingstatisticClear based on Integer32"""
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


_Gs2328MLDSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingstatisticClear_Object = MibScalar
gs2328MLDSnoopingstatisticClear = _Gs2328MLDSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 1),
    _Gs2328MLDSnoopingstatisticClear_Type()
)
gs2328MLDSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticClear.setStatus("current")
_Gs2328MLDSnoopingstatisticTable_Object = MibTable
gs2328MLDSnoopingstatisticTable = _Gs2328MLDSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticTable.setStatus("current")
_Gs2328MLDSnoopingstatisticEntry_Object = MibTableRow
gs2328MLDSnoopingstatisticEntry = _Gs2328MLDSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1)
)
gs2328MLDSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MLDSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticEntry.setStatus("current")


class _Gs2328MLDSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2328MLDSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MLDSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingstatisticVLANID_Object = MibTableColumn
gs2328MLDSnoopingstatisticVLANID = _Gs2328MLDSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 1),
    _Gs2328MLDSnoopingstatisticVLANID_Type()
)
gs2328MLDSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticVLANID.setStatus("current")
_Gs2328MLDSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2328MLDSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2328MLDSnoopingstatisticQuerierVersion = _Gs2328MLDSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 2),
    _Gs2328MLDSnoopingstatisticQuerierVersion_Type()
)
gs2328MLDSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2328MLDSnoopingstatisticHostVersion_Type = DisplayString
_Gs2328MLDSnoopingstatisticHostVersion_Object = MibTableColumn
gs2328MLDSnoopingstatisticHostVersion = _Gs2328MLDSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 3),
    _Gs2328MLDSnoopingstatisticHostVersion_Type()
)
gs2328MLDSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticHostVersion.setStatus("current")
_Gs2328MLDSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2328MLDSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2328MLDSnoopingstatisticQuerierStatus = _Gs2328MLDSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 4),
    _Gs2328MLDSnoopingstatisticQuerierStatus_Type()
)
gs2328MLDSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2328MLDSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2328MLDSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2328MLDSnoopingstatisticQueriesTransmitted = _Gs2328MLDSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 5),
    _Gs2328MLDSnoopingstatisticQueriesTransmitted_Type()
)
gs2328MLDSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2328MLDSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2328MLDSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2328MLDSnoopingstatisticQueriesReceived = _Gs2328MLDSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 6),
    _Gs2328MLDSnoopingstatisticQueriesReceived_Type()
)
gs2328MLDSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2328MLDSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2328MLDSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2328MLDSnoopingstatisticV1ReportsReceived = _Gs2328MLDSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 7),
    _Gs2328MLDSnoopingstatisticV1ReportsReceived_Type()
)
gs2328MLDSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2328MLDSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2328MLDSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2328MLDSnoopingstatisticV2ReportsReceived = _Gs2328MLDSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 8),
    _Gs2328MLDSnoopingstatisticV2ReportsReceived_Type()
)
gs2328MLDSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2328MLDSnoopingstatisticV1LeavesReceived_Type = Counter32
_Gs2328MLDSnoopingstatisticV1LeavesReceived_Object = MibTableColumn
gs2328MLDSnoopingstatisticV1LeavesReceived = _Gs2328MLDSnoopingstatisticV1LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 2, 1, 9),
    _Gs2328MLDSnoopingstatisticV1LeavesReceived_Type()
)
gs2328MLDSnoopingstatisticV1LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingstatisticV1LeavesReceived.setStatus("current")
_Gs2328MLDSnoopingRouterPortTable_Object = MibTable
gs2328MLDSnoopingRouterPortTable = _Gs2328MLDSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 3)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingRouterPortTable.setStatus("current")
_Gs2328MLDSnoopingRouterPortEntry_Object = MibTableRow
gs2328MLDSnoopingRouterPortEntry = _Gs2328MLDSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 3, 1)
)
gs2328MLDSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingRouterPortEntry.setStatus("current")
_Gs2328MLDSnoopingRouterPortStatus_Type = DisplayString
_Gs2328MLDSnoopingRouterPortStatus_Object = MibTableColumn
gs2328MLDSnoopingRouterPortStatus = _Gs2328MLDSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 4, 3, 1, 1),
    _Gs2328MLDSnoopingRouterPortStatus_Type()
)
gs2328MLDSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingRouterPortStatus.setStatus("current")
_Gs2328MLDSnoopingGroupsTable_Object = MibTable
gs2328MLDSnoopingGroupsTable = _Gs2328MLDSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 5)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingGroupsTable.setStatus("current")
_Gs2328MLDSnoopingGroupsEntry_Object = MibTableRow
gs2328MLDSnoopingGroupsEntry = _Gs2328MLDSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 5, 1)
)
gs2328MLDSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MLDSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingGroupsEntry.setStatus("current")


class _Gs2328MLDSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2328MLDSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MLDSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingGroupsIndex_Object = MibTableColumn
gs2328MLDSnoopingGroupsIndex = _Gs2328MLDSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 5, 1, 1),
    _Gs2328MLDSnoopingGroupsIndex_Type()
)
gs2328MLDSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingGroupsIndex.setStatus("current")


class _Gs2328MLDSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2328MLDSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MLDSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingGroupsVLANID_Object = MibTableColumn
gs2328MLDSnoopingGroupsVLANID = _Gs2328MLDSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 5, 1, 2),
    _Gs2328MLDSnoopingGroupsVLANID_Type()
)
gs2328MLDSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingGroupsVLANID.setStatus("current")
_Gs2328MLDSnoopingGroups_Type = DisplayString
_Gs2328MLDSnoopingGroups_Object = MibTableColumn
gs2328MLDSnoopingGroups = _Gs2328MLDSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 5, 1, 3),
    _Gs2328MLDSnoopingGroups_Type()
)
gs2328MLDSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingGroups.setStatus("current")
_Gs2328MLDSnoopingGroupsMemberships_Type = DisplayString
_Gs2328MLDSnoopingGroupsMemberships_Object = MibTableColumn
gs2328MLDSnoopingGroupsMemberships = _Gs2328MLDSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 5, 1, 4),
    _Gs2328MLDSnoopingGroupsMemberships_Type()
)
gs2328MLDSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingGroupsMemberships.setStatus("current")
_Gs2328MLDSnoopingSSMTable_Object = MibTable
gs2328MLDSnoopingSSMTable = _Gs2328MLDSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6)
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMTable.setStatus("current")
_Gs2328MLDSnoopingSSMEntry_Object = MibTableRow
gs2328MLDSnoopingSSMEntry = _Gs2328MLDSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1)
)
gs2328MLDSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MLDSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMEntry.setStatus("current")


class _Gs2328MLDSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2328MLDSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MLDSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingSSMIndex_Object = MibTableColumn
gs2328MLDSnoopingSSMIndex = _Gs2328MLDSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 1),
    _Gs2328MLDSnoopingSSMIndex_Type()
)
gs2328MLDSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMIndex.setStatus("current")


class _Gs2328MLDSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2328MLDSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MLDSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingSSMVLANID_Object = MibTableColumn
gs2328MLDSnoopingSSMVLANID = _Gs2328MLDSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 2),
    _Gs2328MLDSnoopingSSMVLANID_Type()
)
gs2328MLDSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMVLANID.setStatus("current")
_Gs2328MLDSnoopingSSMGroup_Type = DisplayString
_Gs2328MLDSnoopingSSMGroup_Object = MibTableColumn
gs2328MLDSnoopingSSMGroup = _Gs2328MLDSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 3),
    _Gs2328MLDSnoopingSSMGroup_Type()
)
gs2328MLDSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMGroup.setStatus("current")


class _Gs2328MLDSnoopingSSMPort_Type(Integer32):
    """Custom type gs2328MLDSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MLDSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2328MLDSnoopingSSMPort_Object = MibTableColumn
gs2328MLDSnoopingSSMPort = _Gs2328MLDSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 4),
    _Gs2328MLDSnoopingSSMPort_Type()
)
gs2328MLDSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMPort.setStatus("current")
_Gs2328MLDSnoopingSSMMode_Type = DisplayString
_Gs2328MLDSnoopingSSMMode_Object = MibTableColumn
gs2328MLDSnoopingSSMMode = _Gs2328MLDSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 5),
    _Gs2328MLDSnoopingSSMMode_Type()
)
gs2328MLDSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMMode.setStatus("current")
_Gs2328MLDSnoopingSSMSourceAddress_Type = DisplayString
_Gs2328MLDSnoopingSSMSourceAddress_Object = MibTableColumn
gs2328MLDSnoopingSSMSourceAddress = _Gs2328MLDSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 6),
    _Gs2328MLDSnoopingSSMSourceAddress_Type()
)
gs2328MLDSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMSourceAddress.setStatus("current")
_Gs2328MLDSnoopingSSMType_Type = DisplayString
_Gs2328MLDSnoopingSSMType_Object = MibTableColumn
gs2328MLDSnoopingSSMType = _Gs2328MLDSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 17, 6, 1, 7),
    _Gs2328MLDSnoopingSSMType_Type()
)
gs2328MLDSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MLDSnoopingSSMType.setStatus("current")
_Gs2328MVR_ObjectIdentity = ObjectIdentity
gs2328MVR = _Gs2328MVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18)
)
_Gs2328MVRConfiguration_ObjectIdentity = ObjectIdentity
gs2328MVRConfiguration = _Gs2328MVRConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1)
)


class _Gs2328MVRMode_Type(Integer32):
    """Custom type gs2328MVRMode based on Integer32"""
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


_Gs2328MVRMode_Type.__name__ = "Integer32"
_Gs2328MVRMode_Object = MibScalar
gs2328MVRMode = _Gs2328MVRMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 1),
    _Gs2328MVRMode_Type()
)
gs2328MVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRMode.setStatus("current")


class _Gs2328MVRVLANId_Type(Integer32):
    """Custom type gs2328MVRVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328MVRVLANId_Type.__name__ = "Integer32"
_Gs2328MVRVLANId_Object = MibScalar
gs2328MVRVLANId = _Gs2328MVRVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 2),
    _Gs2328MVRVLANId_Type()
)
gs2328MVRVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRVLANId.setStatus("current")
_Gs2328MVRPortConfigurationTable_Object = MibTable
gs2328MVRPortConfigurationTable = _Gs2328MVRPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 3)
)
if mibBuilder.loadTexts:
    gs2328MVRPortConfigurationTable.setStatus("current")
_Gs2328MVRPortConfigurationEntry_Object = MibTableRow
gs2328MVRPortConfigurationEntry = _Gs2328MVRPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 3, 1)
)
gs2328MVRPortConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328MVRPortConfigurationEntry.setStatus("current")


class _Gs2328MVRPortConfigurationMode_Type(Integer32):
    """Custom type gs2328MVRPortConfigurationMode based on Integer32"""
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


_Gs2328MVRPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2328MVRPortConfigurationMode_Object = MibTableColumn
gs2328MVRPortConfigurationMode = _Gs2328MVRPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 3, 1, 1),
    _Gs2328MVRPortConfigurationMode_Type()
)
gs2328MVRPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortConfigurationMode.setStatus("current")


class _Gs2328MVRPortConfigurationType_Type(Integer32):
    """Custom type gs2328MVRPortConfigurationType based on Integer32"""
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


_Gs2328MVRPortConfigurationType_Type.__name__ = "Integer32"
_Gs2328MVRPortConfigurationType_Object = MibTableColumn
gs2328MVRPortConfigurationType = _Gs2328MVRPortConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 3, 1, 2),
    _Gs2328MVRPortConfigurationType_Type()
)
gs2328MVRPortConfigurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortConfigurationType.setStatus("current")


class _Gs2328MVRPortConfigurationImmediateLeave_Type(Integer32):
    """Custom type gs2328MVRPortConfigurationImmediateLeave based on Integer32"""
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


_Gs2328MVRPortConfigurationImmediateLeave_Type.__name__ = "Integer32"
_Gs2328MVRPortConfigurationImmediateLeave_Object = MibTableColumn
gs2328MVRPortConfigurationImmediateLeave = _Gs2328MVRPortConfigurationImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 1, 3, 1, 3),
    _Gs2328MVRPortConfigurationImmediateLeave_Type()
)
gs2328MVRPortConfigurationImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortConfigurationImmediateLeave.setStatus("current")
_Gs2328MVRPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2328MVRPortGroupFiltering = _Gs2328MVRPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2)
)
_Gs2328MVRPortGroupFilteringCreate_Type = Integer32
_Gs2328MVRPortGroupFilteringCreate_Object = MibScalar
gs2328MVRPortGroupFilteringCreate = _Gs2328MVRPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 1),
    _Gs2328MVRPortGroupFilteringCreate_Type()
)
gs2328MVRPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringCreate.setStatus("current")
_Gs2328MVRPortGroupFilteringTable_Object = MibTable
gs2328MVRPortGroupFilteringTable = _Gs2328MVRPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringTable.setStatus("current")
_Gs2328MVRPortGroupFilteringEntry_Object = MibTableRow
gs2328MVRPortGroupFilteringEntry = _Gs2328MVRPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2, 1)
)
gs2328MVRPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MVRPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringEntry.setStatus("current")


class _Gs2328MVRPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2328MVRPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MVRPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2328MVRPortGroupFilteringIndex_Object = MibTableColumn
gs2328MVRPortGroupFilteringIndex = _Gs2328MVRPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2, 1, 1),
    _Gs2328MVRPortGroupFilteringIndex_Type()
)
gs2328MVRPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringIndex.setStatus("current")


class _Gs2328MVRPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2328MVRPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MVRPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2328MVRPortGroupFilteringPort_Object = MibTableColumn
gs2328MVRPortGroupFilteringPort = _Gs2328MVRPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2, 1, 2),
    _Gs2328MVRPortGroupFilteringPort_Type()
)
gs2328MVRPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringPort.setStatus("current")
_Gs2328MVRPortGroupFilteringStartGroups_Type = DisplayString
_Gs2328MVRPortGroupFilteringStartGroups_Object = MibTableColumn
gs2328MVRPortGroupFilteringStartGroups = _Gs2328MVRPortGroupFilteringStartGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2, 1, 3),
    _Gs2328MVRPortGroupFilteringStartGroups_Type()
)
gs2328MVRPortGroupFilteringStartGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringStartGroups.setStatus("current")
_Gs2328MVRPortGroupFilteringEndGroups_Type = DisplayString
_Gs2328MVRPortGroupFilteringEndGroups_Object = MibTableColumn
gs2328MVRPortGroupFilteringEndGroups = _Gs2328MVRPortGroupFilteringEndGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2, 1, 4),
    _Gs2328MVRPortGroupFilteringEndGroups_Type()
)
gs2328MVRPortGroupFilteringEndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringEndGroups.setStatus("current")


class _Gs2328MVRPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2328MVRPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2328MVRPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2328MVRPortGroupFilteringRowStatus_Object = MibTableColumn
gs2328MVRPortGroupFilteringRowStatus = _Gs2328MVRPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 2, 2, 1, 5),
    _Gs2328MVRPortGroupFilteringRowStatus_Type()
)
gs2328MVRPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRPortGroupFilteringRowStatus.setStatus("current")
_Gs2328MVRGroupsTable_Object = MibTable
gs2328MVRGroupsTable = _Gs2328MVRGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gs2328MVRGroupsTable.setStatus("current")
_Gs2328MVRGroupsEntry_Object = MibTableRow
gs2328MVRGroupsEntry = _Gs2328MVRGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 3, 1)
)
gs2328MVRGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MVRGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328MVRGroupsEntry.setStatus("current")


class _Gs2328MVRGroupsIndex_Type(Integer32):
    """Custom type gs2328MVRGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328MVRGroupsIndex_Type.__name__ = "Integer32"
_Gs2328MVRGroupsIndex_Object = MibTableColumn
gs2328MVRGroupsIndex = _Gs2328MVRGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 3, 1, 1),
    _Gs2328MVRGroupsIndex_Type()
)
gs2328MVRGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MVRGroupsIndex.setStatus("current")


class _Gs2328MVRGroupsVLANID_Type(Integer32):
    """Custom type gs2328MVRGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MVRGroupsVLANID_Type.__name__ = "Integer32"
_Gs2328MVRGroupsVLANID_Object = MibTableColumn
gs2328MVRGroupsVLANID = _Gs2328MVRGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 3, 1, 2),
    _Gs2328MVRGroupsVLANID_Type()
)
gs2328MVRGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRGroupsVLANID.setStatus("current")
_Gs2328MVRGroups_Type = DisplayString
_Gs2328MVRGroups_Object = MibTableColumn
gs2328MVRGroups = _Gs2328MVRGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 3, 1, 3),
    _Gs2328MVRGroups_Type()
)
gs2328MVRGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRGroups.setStatus("current")
_Gs2328MVRGroupsMemberships_Type = DisplayString
_Gs2328MVRGroupsMemberships_Object = MibTableColumn
gs2328MVRGroupsMemberships = _Gs2328MVRGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 3, 1, 4),
    _Gs2328MVRGroupsMemberships_Type()
)
gs2328MVRGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRGroupsMemberships.setStatus("current")
_Gs2328MVRStatus_ObjectIdentity = ObjectIdentity
gs2328MVRStatus = _Gs2328MVRStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4)
)


class _Gs2328MVRstatisticClear_Type(Integer32):
    """Custom type gs2328MVRstatisticClear based on Integer32"""
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


_Gs2328MVRstatisticClear_Type.__name__ = "Integer32"
_Gs2328MVRstatisticClear_Object = MibScalar
gs2328MVRstatisticClear = _Gs2328MVRstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4, 1),
    _Gs2328MVRstatisticClear_Type()
)
gs2328MVRstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328MVRstatisticClear.setStatus("current")


class _Gs2328MVRstatisticVLANID_Type(Integer32):
    """Custom type gs2328MVRstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MVRstatisticVLANID_Type.__name__ = "Integer32"
_Gs2328MVRstatisticVLANID_Object = MibScalar
gs2328MVRstatisticVLANID = _Gs2328MVRstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4, 2),
    _Gs2328MVRstatisticVLANID_Type()
)
gs2328MVRstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRstatisticVLANID.setStatus("current")
_Gs2328MVRstatisticV1ReportsReceived_Type = Counter32
_Gs2328MVRstatisticV1ReportsReceived_Object = MibScalar
gs2328MVRstatisticV1ReportsReceived = _Gs2328MVRstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4, 3),
    _Gs2328MVRstatisticV1ReportsReceived_Type()
)
gs2328MVRstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRstatisticV1ReportsReceived.setStatus("current")
_Gs2328MVRstatisticV2ReportsReceived_Type = Counter32
_Gs2328MVRstatisticV2ReportsReceived_Object = MibScalar
gs2328MVRstatisticV2ReportsReceived = _Gs2328MVRstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4, 4),
    _Gs2328MVRstatisticV2ReportsReceived_Type()
)
gs2328MVRstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRstatisticV2ReportsReceived.setStatus("current")
_Gs2328MVRstatisticV3ReportsReceived_Type = Counter32
_Gs2328MVRstatisticV3ReportsReceived_Object = MibScalar
gs2328MVRstatisticV3ReportsReceived = _Gs2328MVRstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4, 5),
    _Gs2328MVRstatisticV3ReportsReceived_Type()
)
gs2328MVRstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRstatisticV3ReportsReceived.setStatus("current")
_Gs2328MVRstatisticV2LeavesReceived_Type = Counter32
_Gs2328MVRstatisticV2LeavesReceived_Object = MibScalar
gs2328MVRstatisticV2LeavesReceived = _Gs2328MVRstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 18, 4, 6),
    _Gs2328MVRstatisticV2LeavesReceived_Type()
)
gs2328MVRstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MVRstatisticV2LeavesReceived.setStatus("current")
_Gs2328LACP_ObjectIdentity = ObjectIdentity
gs2328LACP = _Gs2328LACP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19)
)
_Gs2328LACPConf_ObjectIdentity = ObjectIdentity
gs2328LACPConf = _Gs2328LACPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1)
)
_Gs2328LACPPortConfigurationTable_Object = MibTable
gs2328LACPPortConfigurationTable = _Gs2328LACPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    gs2328LACPPortConfigurationTable.setStatus("current")
_Gs2328LACPPortConfigurationEntry_Object = MibTableRow
gs2328LACPPortConfigurationEntry = _Gs2328LACPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1, 1, 1)
)
gs2328LACPPortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328LACPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2328LACPPortConfigurationEntry.setStatus("current")


class _Gs2328LACPPortConfigurationPort_Type(Integer32):
    """Custom type gs2328LACPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328LACPPortConfigurationPort_Type.__name__ = "Integer32"
_Gs2328LACPPortConfigurationPort_Object = MibTableColumn
gs2328LACPPortConfigurationPort = _Gs2328LACPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1, 1, 1, 1),
    _Gs2328LACPPortConfigurationPort_Type()
)
gs2328LACPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328LACPPortConfigurationPort.setStatus("current")


class _Gs2328LACPPortConfigurationMode_Type(Integer32):
    """Custom type gs2328LACPPortConfigurationMode based on Integer32"""
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


_Gs2328LACPPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2328LACPPortConfigurationMode_Object = MibTableColumn
gs2328LACPPortConfigurationMode = _Gs2328LACPPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1, 1, 1, 2),
    _Gs2328LACPPortConfigurationMode_Type()
)
gs2328LACPPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LACPPortConfigurationMode.setStatus("current")


class _Gs2328LACPPortConfigurationKey_Type(Integer32):
    """Custom type gs2328LACPPortConfigurationKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328LACPPortConfigurationKey_Type.__name__ = "Integer32"
_Gs2328LACPPortConfigurationKey_Object = MibTableColumn
gs2328LACPPortConfigurationKey = _Gs2328LACPPortConfigurationKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1, 1, 1, 3),
    _Gs2328LACPPortConfigurationKey_Type()
)
gs2328LACPPortConfigurationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LACPPortConfigurationKey.setStatus("current")


class _Gs2328LACPPortConfigurationRole_Type(Integer32):
    """Custom type gs2328LACPPortConfigurationRole based on Integer32"""
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


_Gs2328LACPPortConfigurationRole_Type.__name__ = "Integer32"
_Gs2328LACPPortConfigurationRole_Object = MibTableColumn
gs2328LACPPortConfigurationRole = _Gs2328LACPPortConfigurationRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 1, 1, 1, 4),
    _Gs2328LACPPortConfigurationRole_Type()
)
gs2328LACPPortConfigurationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LACPPortConfigurationRole.setStatus("current")
_Gs2328LACPSystemStatusTable_Object = MibTable
gs2328LACPSystemStatusTable = _Gs2328LACPSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusTable.setStatus("current")
_Gs2328LACPSystemStatusEntry_Object = MibTableRow
gs2328LACPSystemStatusEntry = _Gs2328LACPSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1)
)
gs2328LACPSystemStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328LACPSystemStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusEntry.setStatus("current")


class _Gs2328LACPSystemStatusIndex_Type(Integer32):
    """Custom type gs2328LACPSystemStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2328LACPSystemStatusIndex_Type.__name__ = "Integer32"
_Gs2328LACPSystemStatusIndex_Object = MibTableColumn
gs2328LACPSystemStatusIndex = _Gs2328LACPSystemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1, 1),
    _Gs2328LACPSystemStatusIndex_Type()
)
gs2328LACPSystemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusIndex.setStatus("current")
_Gs2328LACPSystemStatusAggrID_Type = DisplayString
_Gs2328LACPSystemStatusAggrID_Object = MibTableColumn
gs2328LACPSystemStatusAggrID = _Gs2328LACPSystemStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1, 2),
    _Gs2328LACPSystemStatusAggrID_Type()
)
gs2328LACPSystemStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusAggrID.setStatus("current")
_Gs2328LACPSystemStatusPartnerSystemID_Type = MacAddress
_Gs2328LACPSystemStatusPartnerSystemID_Object = MibTableColumn
gs2328LACPSystemStatusPartnerSystemID = _Gs2328LACPSystemStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1, 3),
    _Gs2328LACPSystemStatusPartnerSystemID_Type()
)
gs2328LACPSystemStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusPartnerSystemID.setStatus("current")
_Gs2328LACPSystemStatusPartnerKey_Type = DisplayString
_Gs2328LACPSystemStatusPartnerKey_Object = MibTableColumn
gs2328LACPSystemStatusPartnerKey = _Gs2328LACPSystemStatusPartnerKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1, 4),
    _Gs2328LACPSystemStatusPartnerKey_Type()
)
gs2328LACPSystemStatusPartnerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusPartnerKey.setStatus("current")
_Gs2328LACPSystemStatusLastchanged_Type = DisplayString
_Gs2328LACPSystemStatusLastchanged_Object = MibTableColumn
gs2328LACPSystemStatusLastchanged = _Gs2328LACPSystemStatusLastchanged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1, 5),
    _Gs2328LACPSystemStatusLastchanged_Type()
)
gs2328LACPSystemStatusLastchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusLastchanged.setStatus("current")
_Gs2328LACPSystemStatusLocalPorts_Type = DisplayString
_Gs2328LACPSystemStatusLocalPorts_Object = MibTableColumn
gs2328LACPSystemStatusLocalPorts = _Gs2328LACPSystemStatusLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 2, 1, 6),
    _Gs2328LACPSystemStatusLocalPorts_Type()
)
gs2328LACPSystemStatusLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPSystemStatusLocalPorts.setStatus("current")
_Gs2328LACPStatusTable_Object = MibTable
gs2328LACPStatusTable = _Gs2328LACPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gs2328LACPStatusTable.setStatus("current")
_Gs2328LACPStatusEntry_Object = MibTableRow
gs2328LACPStatusEntry = _Gs2328LACPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1)
)
gs2328LACPStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328LACPStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328LACPStatusEntry.setStatus("current")


class _Gs2328LACPStatusPort_Type(Integer32):
    """Custom type gs2328LACPStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328LACPStatusPort_Type.__name__ = "Integer32"
_Gs2328LACPStatusPort_Object = MibTableColumn
gs2328LACPStatusPort = _Gs2328LACPStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1, 1),
    _Gs2328LACPStatusPort_Type()
)
gs2328LACPStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328LACPStatusPort.setStatus("current")
_Gs2328LACPStatusLACP_Type = DisplayString
_Gs2328LACPStatusLACP_Object = MibTableColumn
gs2328LACPStatusLACP = _Gs2328LACPStatusLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1, 2),
    _Gs2328LACPStatusLACP_Type()
)
gs2328LACPStatusLACP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPStatusLACP.setStatus("current")
_Gs2328LACPStatusKey_Type = DisplayString
_Gs2328LACPStatusKey_Object = MibTableColumn
gs2328LACPStatusKey = _Gs2328LACPStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1, 3),
    _Gs2328LACPStatusKey_Type()
)
gs2328LACPStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPStatusKey.setStatus("current")
_Gs2328LACPStatusAggrID_Type = DisplayString
_Gs2328LACPStatusAggrID_Object = MibTableColumn
gs2328LACPStatusAggrID = _Gs2328LACPStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1, 4),
    _Gs2328LACPStatusAggrID_Type()
)
gs2328LACPStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPStatusAggrID.setStatus("current")
_Gs2328LACPStatusPartnerSystemID_Type = DisplayString
_Gs2328LACPStatusPartnerSystemID_Object = MibTableColumn
gs2328LACPStatusPartnerSystemID = _Gs2328LACPStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1, 5),
    _Gs2328LACPStatusPartnerSystemID_Type()
)
gs2328LACPStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPStatusPartnerSystemID.setStatus("current")
_Gs2328LACPStatusPartnerPort_Type = DisplayString
_Gs2328LACPStatusPartnerPort_Object = MibTableColumn
gs2328LACPStatusPartnerPort = _Gs2328LACPStatusPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 3, 1, 6),
    _Gs2328LACPStatusPartnerPort_Type()
)
gs2328LACPStatusPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPStatusPartnerPort.setStatus("current")
_Gs2328LACPStatisticsTable_Object = MibTable
gs2328LACPStatisticsTable = _Gs2328LACPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4)
)
if mibBuilder.loadTexts:
    gs2328LACPStatisticsTable.setStatus("current")
_Gs2328LACPStatisticsEntry_Object = MibTableRow
gs2328LACPStatisticsEntry = _Gs2328LACPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4, 1)
)
gs2328LACPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328LACPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328LACPStatisticsEntry.setStatus("current")


class _Gs2328LACPStatisticsPort_Type(Integer32):
    """Custom type gs2328LACPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328LACPStatisticsPort_Type.__name__ = "Integer32"
_Gs2328LACPStatisticsPort_Object = MibTableColumn
gs2328LACPStatisticsPort = _Gs2328LACPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4, 1, 1),
    _Gs2328LACPStatisticsPort_Type()
)
gs2328LACPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328LACPStatisticsPort.setStatus("current")
_Gs2328LACPReceived_Type = Counter32
_Gs2328LACPReceived_Object = MibTableColumn
gs2328LACPReceived = _Gs2328LACPReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4, 1, 2),
    _Gs2328LACPReceived_Type()
)
gs2328LACPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPReceived.setStatus("current")
_Gs2328LACPTransmitted_Type = Counter32
_Gs2328LACPTransmitted_Object = MibTableColumn
gs2328LACPTransmitted = _Gs2328LACPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4, 1, 3),
    _Gs2328LACPTransmitted_Type()
)
gs2328LACPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPTransmitted.setStatus("current")
_Gs2328LACPDiscardedUnknown_Type = Counter32
_Gs2328LACPDiscardedUnknown_Object = MibTableColumn
gs2328LACPDiscardedUnknown = _Gs2328LACPDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4, 1, 4),
    _Gs2328LACPDiscardedUnknown_Type()
)
gs2328LACPDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPDiscardedUnknown.setStatus("current")
_Gs2328LACPDiscardedIllegal_Type = Counter32
_Gs2328LACPDiscardedIllegal_Object = MibTableColumn
gs2328LACPDiscardedIllegal = _Gs2328LACPDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 4, 1, 5),
    _Gs2328LACPDiscardedIllegal_Type()
)
gs2328LACPDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LACPDiscardedIllegal.setStatus("current")


class _Gs2328LACPStatisticsClear_Type(Integer32):
    """Custom type gs2328LACPStatisticsClear based on Integer32"""
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


_Gs2328LACPStatisticsClear_Type.__name__ = "Integer32"
_Gs2328LACPStatisticsClear_Object = MibScalar
gs2328LACPStatisticsClear = _Gs2328LACPStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 19, 5),
    _Gs2328LACPStatisticsClear_Type()
)
gs2328LACPStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LACPStatisticsClear.setStatus("current")
_Gs2328STP_ObjectIdentity = ObjectIdentity
gs2328STP = _Gs2328STP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20)
)
_Gs2328STPBridgeBasicConf_ObjectIdentity = ObjectIdentity
gs2328STPBridgeBasicConf = _Gs2328STPBridgeBasicConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1)
)


class _Gs2328STPBridgeProtocolVersion_Type(Integer32):
    """Custom type gs2328STPBridgeProtocolVersion based on Integer32"""
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


_Gs2328STPBridgeProtocolVersion_Type.__name__ = "Integer32"
_Gs2328STPBridgeProtocolVersion_Object = MibScalar
gs2328STPBridgeProtocolVersion = _Gs2328STPBridgeProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1, 1),
    _Gs2328STPBridgeProtocolVersion_Type()
)
gs2328STPBridgeProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeProtocolVersion.setStatus("current")


class _Gs2328STPBridgePriority_Type(Integer32):
    """Custom type gs2328STPBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPBridgePriority_Type.__name__ = "Integer32"
_Gs2328STPBridgePriority_Object = MibScalar
gs2328STPBridgePriority = _Gs2328STPBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1, 2),
    _Gs2328STPBridgePriority_Type()
)
gs2328STPBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgePriority.setStatus("current")


class _Gs2328STPBridgeForwardDelay_Type(Integer32):
    """Custom type gs2328STPBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Gs2328STPBridgeForwardDelay_Type.__name__ = "Integer32"
_Gs2328STPBridgeForwardDelay_Object = MibScalar
gs2328STPBridgeForwardDelay = _Gs2328STPBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1, 3),
    _Gs2328STPBridgeForwardDelay_Type()
)
gs2328STPBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeForwardDelay.setStatus("current")


class _Gs2328STPBridgeMaxAge_Type(Integer32):
    """Custom type gs2328STPBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2328STPBridgeMaxAge_Type.__name__ = "Integer32"
_Gs2328STPBridgeMaxAge_Object = MibScalar
gs2328STPBridgeMaxAge = _Gs2328STPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1, 4),
    _Gs2328STPBridgeMaxAge_Type()
)
gs2328STPBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeMaxAge.setStatus("current")


class _Gs2328STPBridgeMaximumHopCount_Type(Integer32):
    """Custom type gs2328STPBridgeMaximumHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2328STPBridgeMaximumHopCount_Type.__name__ = "Integer32"
_Gs2328STPBridgeMaximumHopCount_Object = MibScalar
gs2328STPBridgeMaximumHopCount = _Gs2328STPBridgeMaximumHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1, 5),
    _Gs2328STPBridgeMaximumHopCount_Type()
)
gs2328STPBridgeMaximumHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeMaximumHopCount.setStatus("current")


class _Gs2328STPBridgeTransmitHoldCount_Type(Integer32):
    """Custom type gs2328STPBridgeTransmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328STPBridgeTransmitHoldCount_Type.__name__ = "Integer32"
_Gs2328STPBridgeTransmitHoldCount_Object = MibScalar
gs2328STPBridgeTransmitHoldCount = _Gs2328STPBridgeTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 1, 6),
    _Gs2328STPBridgeTransmitHoldCount_Type()
)
gs2328STPBridgeTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeTransmitHoldCount.setStatus("current")
_Gs2328STPBridgeAdvancedConf_ObjectIdentity = ObjectIdentity
gs2328STPBridgeAdvancedConf = _Gs2328STPBridgeAdvancedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 2)
)


class _Gs2328STPBridgeEdgePortBPDUFiltering_Type(Integer32):
    """Custom type gs2328STPBridgeEdgePortBPDUFiltering based on Integer32"""
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


_Gs2328STPBridgeEdgePortBPDUFiltering_Type.__name__ = "Integer32"
_Gs2328STPBridgeEdgePortBPDUFiltering_Object = MibScalar
gs2328STPBridgeEdgePortBPDUFiltering = _Gs2328STPBridgeEdgePortBPDUFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 2, 1),
    _Gs2328STPBridgeEdgePortBPDUFiltering_Type()
)
gs2328STPBridgeEdgePortBPDUFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeEdgePortBPDUFiltering.setStatus("current")


class _Gs2328STPBridgeEdgePortBPDUGuard_Type(Integer32):
    """Custom type gs2328STPBridgeEdgePortBPDUGuard based on Integer32"""
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


_Gs2328STPBridgeEdgePortBPDUGuard_Type.__name__ = "Integer32"
_Gs2328STPBridgeEdgePortBPDUGuard_Object = MibScalar
gs2328STPBridgeEdgePortBPDUGuard = _Gs2328STPBridgeEdgePortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 2, 2),
    _Gs2328STPBridgeEdgePortBPDUGuard_Type()
)
gs2328STPBridgeEdgePortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgeEdgePortBPDUGuard.setStatus("current")


class _Gs2328STPBridgePortErrorRecoveryTimeout_Type(Integer32):
    """Custom type gs2328STPBridgePortErrorRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Gs2328STPBridgePortErrorRecoveryTimeout_Type.__name__ = "Integer32"
_Gs2328STPBridgePortErrorRecoveryTimeout_Object = MibScalar
gs2328STPBridgePortErrorRecoveryTimeout = _Gs2328STPBridgePortErrorRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 2, 3),
    _Gs2328STPBridgePortErrorRecoveryTimeout_Type()
)
gs2328STPBridgePortErrorRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPBridgePortErrorRecoveryTimeout.setStatus("current")
_Gs2328STPMSTIConf_ObjectIdentity = ObjectIdentity
gs2328STPMSTIConf = _Gs2328STPMSTIConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 3)
)


class _Gs2328STPMSTIConfigurationName_Type(DisplayString):
    """Custom type gs2328STPMSTIConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328STPMSTIConfigurationName_Type.__name__ = "DisplayString"
_Gs2328STPMSTIConfigurationName_Object = MibScalar
gs2328STPMSTIConfigurationName = _Gs2328STPMSTIConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 3, 1),
    _Gs2328STPMSTIConfigurationName_Type()
)
gs2328STPMSTIConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTIConfigurationName.setStatus("current")


class _Gs2328STPMSTIConfigurationRevision_Type(Integer32):
    """Custom type gs2328STPMSTIConfigurationRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328STPMSTIConfigurationRevision_Type.__name__ = "Integer32"
_Gs2328STPMSTIConfigurationRevision_Object = MibScalar
gs2328STPMSTIConfigurationRevision = _Gs2328STPMSTIConfigurationRevision_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 3, 2),
    _Gs2328STPMSTIConfigurationRevision_Type()
)
gs2328STPMSTIConfigurationRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTIConfigurationRevision.setStatus("current")
_Gs2328STPMSTIMappingConf_ObjectIdentity = ObjectIdentity
gs2328STPMSTIMappingConf = _Gs2328STPMSTIMappingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4)
)


class _Gs2328STPMSTI1VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI1VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI1VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI1VLANsMapped_Object = MibScalar
gs2328STPMSTI1VLANsMapped = _Gs2328STPMSTI1VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 1),
    _Gs2328STPMSTI1VLANsMapped_Type()
)
gs2328STPMSTI1VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI1VLANsMapped.setStatus("current")


class _Gs2328STPMSTI2VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI2VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI2VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI2VLANsMapped_Object = MibScalar
gs2328STPMSTI2VLANsMapped = _Gs2328STPMSTI2VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 2),
    _Gs2328STPMSTI2VLANsMapped_Type()
)
gs2328STPMSTI2VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI2VLANsMapped.setStatus("current")


class _Gs2328STPMSTI3VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI3VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI3VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI3VLANsMapped_Object = MibScalar
gs2328STPMSTI3VLANsMapped = _Gs2328STPMSTI3VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 3),
    _Gs2328STPMSTI3VLANsMapped_Type()
)
gs2328STPMSTI3VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI3VLANsMapped.setStatus("current")


class _Gs2328STPMSTI4VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI4VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI4VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI4VLANsMapped_Object = MibScalar
gs2328STPMSTI4VLANsMapped = _Gs2328STPMSTI4VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 4),
    _Gs2328STPMSTI4VLANsMapped_Type()
)
gs2328STPMSTI4VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI4VLANsMapped.setStatus("current")


class _Gs2328STPMSTI5VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI5VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI5VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI5VLANsMapped_Object = MibScalar
gs2328STPMSTI5VLANsMapped = _Gs2328STPMSTI5VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 5),
    _Gs2328STPMSTI5VLANsMapped_Type()
)
gs2328STPMSTI5VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI5VLANsMapped.setStatus("current")


class _Gs2328STPMSTI6VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI6VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI6VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI6VLANsMapped_Object = MibScalar
gs2328STPMSTI6VLANsMapped = _Gs2328STPMSTI6VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 6),
    _Gs2328STPMSTI6VLANsMapped_Type()
)
gs2328STPMSTI6VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI6VLANsMapped.setStatus("current")


class _Gs2328STPMSTI7VLANsMapped_Type(DisplayString):
    """Custom type gs2328STPMSTI7VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328STPMSTI7VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328STPMSTI7VLANsMapped_Object = MibScalar
gs2328STPMSTI7VLANsMapped = _Gs2328STPMSTI7VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 4, 7),
    _Gs2328STPMSTI7VLANsMapped_Type()
)
gs2328STPMSTI7VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI7VLANsMapped.setStatus("current")
_Gs2328STPMSTIPriority_ObjectIdentity = ObjectIdentity
gs2328STPMSTIPriority = _Gs2328STPMSTIPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5)
)


class _Gs2328STPCISTPriority_Type(Integer32):
    """Custom type gs2328STPCISTPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPCISTPriority_Type.__name__ = "Integer32"
_Gs2328STPCISTPriority_Object = MibScalar
gs2328STPCISTPriority = _Gs2328STPCISTPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 1),
    _Gs2328STPCISTPriority_Type()
)
gs2328STPCISTPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTPriority.setStatus("current")


class _Gs2328STPMSTI1Priority_Type(Integer32):
    """Custom type gs2328STPMSTI1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI1Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI1Priority_Object = MibScalar
gs2328STPMSTI1Priority = _Gs2328STPMSTI1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 2),
    _Gs2328STPMSTI1Priority_Type()
)
gs2328STPMSTI1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI1Priority.setStatus("current")


class _Gs2328STPMSTI2Priority_Type(Integer32):
    """Custom type gs2328STPMSTI2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI2Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI2Priority_Object = MibScalar
gs2328STPMSTI2Priority = _Gs2328STPMSTI2Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 3),
    _Gs2328STPMSTI2Priority_Type()
)
gs2328STPMSTI2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI2Priority.setStatus("current")


class _Gs2328STPMSTI3Priority_Type(Integer32):
    """Custom type gs2328STPMSTI3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI3Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI3Priority_Object = MibScalar
gs2328STPMSTI3Priority = _Gs2328STPMSTI3Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 4),
    _Gs2328STPMSTI3Priority_Type()
)
gs2328STPMSTI3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI3Priority.setStatus("current")


class _Gs2328STPMSTI4Priority_Type(Integer32):
    """Custom type gs2328STPMSTI4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI4Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI4Priority_Object = MibScalar
gs2328STPMSTI4Priority = _Gs2328STPMSTI4Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 5),
    _Gs2328STPMSTI4Priority_Type()
)
gs2328STPMSTI4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI4Priority.setStatus("current")


class _Gs2328STPMSTI5Priority_Type(Integer32):
    """Custom type gs2328STPMSTI5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI5Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI5Priority_Object = MibScalar
gs2328STPMSTI5Priority = _Gs2328STPMSTI5Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 6),
    _Gs2328STPMSTI5Priority_Type()
)
gs2328STPMSTI5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI5Priority.setStatus("current")


class _Gs2328STPMSTI6Priority_Type(Integer32):
    """Custom type gs2328STPMSTI6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI6Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI6Priority_Object = MibScalar
gs2328STPMSTI6Priority = _Gs2328STPMSTI6Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 7),
    _Gs2328STPMSTI6Priority_Type()
)
gs2328STPMSTI6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI6Priority.setStatus("current")


class _Gs2328STPMSTI7Priority_Type(Integer32):
    """Custom type gs2328STPMSTI7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328STPMSTI7Priority_Type.__name__ = "Integer32"
_Gs2328STPMSTI7Priority_Object = MibScalar
gs2328STPMSTI7Priority = _Gs2328STPMSTI7Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 5, 8),
    _Gs2328STPMSTI7Priority_Type()
)
gs2328STPMSTI7Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI7Priority.setStatus("current")
_Gs2328STPCISTPort_ObjectIdentity = ObjectIdentity
gs2328STPCISTPort = _Gs2328STPCISTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6)
)
_Gs2328STPCISTAggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPCISTAggregatedPort = _Gs2328STPCISTAggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1)
)


class _Gs2328STPCISTAggregatedPortSTPEnabled_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortSTPEnabled based on Integer32"""
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


_Gs2328STPCISTAggregatedPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortSTPEnabled_Object = MibScalar
gs2328STPCISTAggregatedPortSTPEnabled = _Gs2328STPCISTAggregatedPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 1),
    _Gs2328STPCISTAggregatedPortSTPEnabled_Type()
)
gs2328STPCISTAggregatedPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortSTPEnabled.setStatus("current")


class _Gs2328STPCISTAggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPCISTAggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortPathCost_Object = MibScalar
gs2328STPCISTAggregatedPortPathCost = _Gs2328STPCISTAggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 2),
    _Gs2328STPCISTAggregatedPortPathCost_Type()
)
gs2328STPCISTAggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortPathCost.setStatus("current")


class _Gs2328STPCISTAggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPCISTAggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortPriority_Object = MibScalar
gs2328STPCISTAggregatedPortPriority = _Gs2328STPCISTAggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 3),
    _Gs2328STPCISTAggregatedPortPriority_Type()
)
gs2328STPCISTAggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortPriority.setStatus("current")


class _Gs2328STPCISTAggregatedPortAdminEdge_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortAdminEdge based on Integer32"""
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


_Gs2328STPCISTAggregatedPortAdminEdge_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortAdminEdge_Object = MibScalar
gs2328STPCISTAggregatedPortAdminEdge = _Gs2328STPCISTAggregatedPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 4),
    _Gs2328STPCISTAggregatedPortAdminEdge_Type()
)
gs2328STPCISTAggregatedPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortAdminEdge.setStatus("current")


class _Gs2328STPCISTAggregatedPortAutoEdge_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortAutoEdge based on Integer32"""
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


_Gs2328STPCISTAggregatedPortAutoEdge_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortAutoEdge_Object = MibScalar
gs2328STPCISTAggregatedPortAutoEdge = _Gs2328STPCISTAggregatedPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 5),
    _Gs2328STPCISTAggregatedPortAutoEdge_Type()
)
gs2328STPCISTAggregatedPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortAutoEdge.setStatus("current")


class _Gs2328STPCISTAggregatedPortRestrictedRole_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortRestrictedRole based on Integer32"""
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


_Gs2328STPCISTAggregatedPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortRestrictedRole_Object = MibScalar
gs2328STPCISTAggregatedPortRestrictedRole = _Gs2328STPCISTAggregatedPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 6),
    _Gs2328STPCISTAggregatedPortRestrictedRole_Type()
)
gs2328STPCISTAggregatedPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortRestrictedRole.setStatus("current")


class _Gs2328STPCISTAggregatedPortRestrictedTCN_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortRestrictedTCN based on Integer32"""
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


_Gs2328STPCISTAggregatedPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortRestrictedTCN_Object = MibScalar
gs2328STPCISTAggregatedPortRestrictedTCN = _Gs2328STPCISTAggregatedPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 7),
    _Gs2328STPCISTAggregatedPortRestrictedTCN_Type()
)
gs2328STPCISTAggregatedPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortRestrictedTCN.setStatus("current")


class _Gs2328STPCISTAggregatedPortBPDUGuard_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortBPDUGuard based on Integer32"""
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


_Gs2328STPCISTAggregatedPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortBPDUGuard_Object = MibScalar
gs2328STPCISTAggregatedPortBPDUGuard = _Gs2328STPCISTAggregatedPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 8),
    _Gs2328STPCISTAggregatedPortBPDUGuard_Type()
)
gs2328STPCISTAggregatedPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortBPDUGuard.setStatus("current")


class _Gs2328STPCISTAggregatedPortPointtoPoint_Type(Integer32):
    """Custom type gs2328STPCISTAggregatedPortPointtoPoint based on Integer32"""
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


_Gs2328STPCISTAggregatedPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2328STPCISTAggregatedPortPointtoPoint_Object = MibScalar
gs2328STPCISTAggregatedPortPointtoPoint = _Gs2328STPCISTAggregatedPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 1, 9),
    _Gs2328STPCISTAggregatedPortPointtoPoint_Type()
)
gs2328STPCISTAggregatedPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTAggregatedPortPointtoPoint.setStatus("current")
_Gs2328STPCISTNormalPortTable_Object = MibTable
gs2328STPCISTNormalPortTable = _Gs2328STPCISTNormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortTable.setStatus("current")
_Gs2328STPCISTNormalPortEntry_Object = MibTableRow
gs2328STPCISTNormalPortEntry = _Gs2328STPCISTNormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1)
)
gs2328STPCISTNormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPCISTNormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortEntry.setStatus("current")


class _Gs2328STPCISTNormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPCISTNormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortConfPort_Object = MibTableColumn
gs2328STPCISTNormalPortConfPort = _Gs2328STPCISTNormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 1),
    _Gs2328STPCISTNormalPortConfPort_Type()
)
gs2328STPCISTNormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortConfPort.setStatus("current")


class _Gs2328STPCISTNormalPortSTPEnabled_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortSTPEnabled based on Integer32"""
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


_Gs2328STPCISTNormalPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortSTPEnabled_Object = MibTableColumn
gs2328STPCISTNormalPortSTPEnabled = _Gs2328STPCISTNormalPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 2),
    _Gs2328STPCISTNormalPortSTPEnabled_Type()
)
gs2328STPCISTNormalPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortSTPEnabled.setStatus("current")


class _Gs2328STPCISTNormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPCISTNormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortPathCost_Object = MibTableColumn
gs2328STPCISTNormalPortPathCost = _Gs2328STPCISTNormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 3),
    _Gs2328STPCISTNormalPortPathCost_Type()
)
gs2328STPCISTNormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortPathCost.setStatus("current")


class _Gs2328STPCISTNormalPortPriority_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPCISTNormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortPriority_Object = MibTableColumn
gs2328STPCISTNormalPortPriority = _Gs2328STPCISTNormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 4),
    _Gs2328STPCISTNormalPortPriority_Type()
)
gs2328STPCISTNormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortPriority.setStatus("current")


class _Gs2328STPCISTNormalPortAdminEdge_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortAdminEdge based on Integer32"""
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


_Gs2328STPCISTNormalPortAdminEdge_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortAdminEdge_Object = MibTableColumn
gs2328STPCISTNormalPortAdminEdge = _Gs2328STPCISTNormalPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 5),
    _Gs2328STPCISTNormalPortAdminEdge_Type()
)
gs2328STPCISTNormalPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortAdminEdge.setStatus("current")


class _Gs2328STPCISTNormalPortAutoEdge_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortAutoEdge based on Integer32"""
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


_Gs2328STPCISTNormalPortAutoEdge_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortAutoEdge_Object = MibTableColumn
gs2328STPCISTNormalPortAutoEdge = _Gs2328STPCISTNormalPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 6),
    _Gs2328STPCISTNormalPortAutoEdge_Type()
)
gs2328STPCISTNormalPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortAutoEdge.setStatus("current")


class _Gs2328STPCISTNormalPortRestrictedRole_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortRestrictedRole based on Integer32"""
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


_Gs2328STPCISTNormalPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortRestrictedRole_Object = MibTableColumn
gs2328STPCISTNormalPortRestrictedRole = _Gs2328STPCISTNormalPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 7),
    _Gs2328STPCISTNormalPortRestrictedRole_Type()
)
gs2328STPCISTNormalPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortRestrictedRole.setStatus("current")


class _Gs2328STPCISTNormalPortRestrictedTCN_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortRestrictedTCN based on Integer32"""
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


_Gs2328STPCISTNormalPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortRestrictedTCN_Object = MibTableColumn
gs2328STPCISTNormalPortRestrictedTCN = _Gs2328STPCISTNormalPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 8),
    _Gs2328STPCISTNormalPortRestrictedTCN_Type()
)
gs2328STPCISTNormalPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortRestrictedTCN.setStatus("current")


class _Gs2328STPCISTNormalPortBPDUGuard_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortBPDUGuard based on Integer32"""
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


_Gs2328STPCISTNormalPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortBPDUGuard_Object = MibTableColumn
gs2328STPCISTNormalPortBPDUGuard = _Gs2328STPCISTNormalPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 9),
    _Gs2328STPCISTNormalPortBPDUGuard_Type()
)
gs2328STPCISTNormalPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortBPDUGuard.setStatus("current")


class _Gs2328STPCISTNormalPortPointtoPoint_Type(Integer32):
    """Custom type gs2328STPCISTNormalPortPointtoPoint based on Integer32"""
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


_Gs2328STPCISTNormalPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2328STPCISTNormalPortPointtoPoint_Object = MibTableColumn
gs2328STPCISTNormalPortPointtoPoint = _Gs2328STPCISTNormalPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 6, 2, 1, 10),
    _Gs2328STPCISTNormalPortPointtoPoint_Type()
)
gs2328STPCISTNormalPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPCISTNormalPortPointtoPoint.setStatus("current")
_Gs2328STPMSTIPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTIPort = _Gs2328STPMSTIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7)
)
_Gs2328STPMSTI1Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI1Port = _Gs2328STPMSTI1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1)
)
_Gs2328STPMSTI1AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI1AggregatedPort = _Gs2328STPMSTI1AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 1)
)


class _Gs2328STPMSTI1AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI1AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI1AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI1AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI1AggregatedPortPathCost = _Gs2328STPMSTI1AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 1, 1),
    _Gs2328STPMSTI1AggregatedPortPathCost_Type()
)
gs2328STPMSTI1AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI1AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI1AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI1AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI1AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI1AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI1AggregatedPortPriority = _Gs2328STPMSTI1AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 1, 2),
    _Gs2328STPMSTI1AggregatedPortPriority_Type()
)
gs2328STPMSTI1AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI1AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI1NormalPortTable_Object = MibTable
gs2328STPMSTI1NormalPortTable = _Gs2328STPMSTI1NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI1NormalPortTable.setStatus("current")
_Gs2328STPMSTI1NormalPortEntry_Object = MibTableRow
gs2328STPMSTI1NormalPortEntry = _Gs2328STPMSTI1NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 2, 1)
)
gs2328STPMSTI1NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI1NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI1NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI1NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI1NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI1NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI1NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI1NormalPortConfPort = _Gs2328STPMSTI1NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 2, 1, 1),
    _Gs2328STPMSTI1NormalPortConfPort_Type()
)
gs2328STPMSTI1NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI1NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI1NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI1NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI1NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI1NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI1NormalPortPathCost = _Gs2328STPMSTI1NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 2, 1, 2),
    _Gs2328STPMSTI1NormalPortPathCost_Type()
)
gs2328STPMSTI1NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI1NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI1NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI1NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI1NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI1NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI1NormalPortPriority = _Gs2328STPMSTI1NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 1, 2, 1, 3),
    _Gs2328STPMSTI1NormalPortPriority_Type()
)
gs2328STPMSTI1NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI1NormalPortPriority.setStatus("current")
_Gs2328STPMSTI2Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI2Port = _Gs2328STPMSTI2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2)
)
_Gs2328STPMSTI2AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI2AggregatedPort = _Gs2328STPMSTI2AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 1)
)


class _Gs2328STPMSTI2AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI2AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI2AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI2AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI2AggregatedPortPathCost = _Gs2328STPMSTI2AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 1, 1),
    _Gs2328STPMSTI2AggregatedPortPathCost_Type()
)
gs2328STPMSTI2AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI2AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI2AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI2AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI2AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI2AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI2AggregatedPortPriority = _Gs2328STPMSTI2AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 1, 2),
    _Gs2328STPMSTI2AggregatedPortPriority_Type()
)
gs2328STPMSTI2AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI2AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI2NormalPortTable_Object = MibTable
gs2328STPMSTI2NormalPortTable = _Gs2328STPMSTI2NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI2NormalPortTable.setStatus("current")
_Gs2328STPMSTI2NormalPortEntry_Object = MibTableRow
gs2328STPMSTI2NormalPortEntry = _Gs2328STPMSTI2NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 2, 1)
)
gs2328STPMSTI2NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI2NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI2NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI2NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI2NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI2NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI2NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI2NormalPortConfPort = _Gs2328STPMSTI2NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 2, 1, 1),
    _Gs2328STPMSTI2NormalPortConfPort_Type()
)
gs2328STPMSTI2NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI2NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI2NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI2NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI2NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI2NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI2NormalPortPathCost = _Gs2328STPMSTI2NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 2, 1, 2),
    _Gs2328STPMSTI2NormalPortPathCost_Type()
)
gs2328STPMSTI2NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI2NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI2NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI2NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI2NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI2NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI2NormalPortPriority = _Gs2328STPMSTI2NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 2, 2, 1, 3),
    _Gs2328STPMSTI2NormalPortPriority_Type()
)
gs2328STPMSTI2NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI2NormalPortPriority.setStatus("current")
_Gs2328STPMSTI3Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI3Port = _Gs2328STPMSTI3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3)
)
_Gs2328STPMSTI3AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI3AggregatedPort = _Gs2328STPMSTI3AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 1)
)


class _Gs2328STPMSTI3AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI3AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI3AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI3AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI3AggregatedPortPathCost = _Gs2328STPMSTI3AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 1, 1),
    _Gs2328STPMSTI3AggregatedPortPathCost_Type()
)
gs2328STPMSTI3AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI3AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI3AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI3AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI3AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI3AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI3AggregatedPortPriority = _Gs2328STPMSTI3AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 1, 2),
    _Gs2328STPMSTI3AggregatedPortPriority_Type()
)
gs2328STPMSTI3AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI3AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI3NormalPortTable_Object = MibTable
gs2328STPMSTI3NormalPortTable = _Gs2328STPMSTI3NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI3NormalPortTable.setStatus("current")
_Gs2328STPMSTI3NormalPortEntry_Object = MibTableRow
gs2328STPMSTI3NormalPortEntry = _Gs2328STPMSTI3NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 2, 1)
)
gs2328STPMSTI3NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI3NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI3NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI3NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI3NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI3NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI3NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI3NormalPortConfPort = _Gs2328STPMSTI3NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 2, 1, 1),
    _Gs2328STPMSTI3NormalPortConfPort_Type()
)
gs2328STPMSTI3NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI3NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI3NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI3NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI3NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI3NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI3NormalPortPathCost = _Gs2328STPMSTI3NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 2, 1, 2),
    _Gs2328STPMSTI3NormalPortPathCost_Type()
)
gs2328STPMSTI3NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI3NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI3NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI3NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI3NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI3NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI3NormalPortPriority = _Gs2328STPMSTI3NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 3, 2, 1, 3),
    _Gs2328STPMSTI3NormalPortPriority_Type()
)
gs2328STPMSTI3NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI3NormalPortPriority.setStatus("current")
_Gs2328STPMSTI4Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI4Port = _Gs2328STPMSTI4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4)
)
_Gs2328STPMSTI4AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI4AggregatedPort = _Gs2328STPMSTI4AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 1)
)


class _Gs2328STPMSTI4AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI4AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI4AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI4AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI4AggregatedPortPathCost = _Gs2328STPMSTI4AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 1, 1),
    _Gs2328STPMSTI4AggregatedPortPathCost_Type()
)
gs2328STPMSTI4AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI4AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI4AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI4AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI4AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI4AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI4AggregatedPortPriority = _Gs2328STPMSTI4AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 1, 2),
    _Gs2328STPMSTI4AggregatedPortPriority_Type()
)
gs2328STPMSTI4AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI4AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI4NormalPortTable_Object = MibTable
gs2328STPMSTI4NormalPortTable = _Gs2328STPMSTI4NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI4NormalPortTable.setStatus("current")
_Gs2328STPMSTI4NormalPortEntry_Object = MibTableRow
gs2328STPMSTI4NormalPortEntry = _Gs2328STPMSTI4NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 2, 1)
)
gs2328STPMSTI4NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI4NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI4NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI4NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI4NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI4NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI4NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI4NormalPortConfPort = _Gs2328STPMSTI4NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 2, 1, 1),
    _Gs2328STPMSTI4NormalPortConfPort_Type()
)
gs2328STPMSTI4NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI4NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI4NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI4NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI4NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI4NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI4NormalPortPathCost = _Gs2328STPMSTI4NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 2, 1, 2),
    _Gs2328STPMSTI4NormalPortPathCost_Type()
)
gs2328STPMSTI4NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI4NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI4NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI4NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI4NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI4NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI4NormalPortPriority = _Gs2328STPMSTI4NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 4, 2, 1, 3),
    _Gs2328STPMSTI4NormalPortPriority_Type()
)
gs2328STPMSTI4NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI4NormalPortPriority.setStatus("current")
_Gs2328STPMSTI5Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI5Port = _Gs2328STPMSTI5Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5)
)
_Gs2328STPMSTI5AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI5AggregatedPort = _Gs2328STPMSTI5AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 1)
)


class _Gs2328STPMSTI5AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI5AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI5AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI5AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI5AggregatedPortPathCost = _Gs2328STPMSTI5AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 1, 1),
    _Gs2328STPMSTI5AggregatedPortPathCost_Type()
)
gs2328STPMSTI5AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI5AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI5AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI5AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI5AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI5AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI5AggregatedPortPriority = _Gs2328STPMSTI5AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 1, 2),
    _Gs2328STPMSTI5AggregatedPortPriority_Type()
)
gs2328STPMSTI5AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI5AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI5NormalPortTable_Object = MibTable
gs2328STPMSTI5NormalPortTable = _Gs2328STPMSTI5NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI5NormalPortTable.setStatus("current")
_Gs2328STPMSTI5NormalPortEntry_Object = MibTableRow
gs2328STPMSTI5NormalPortEntry = _Gs2328STPMSTI5NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 2, 1)
)
gs2328STPMSTI5NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI5NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI5NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI5NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI5NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI5NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI5NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI5NormalPortConfPort = _Gs2328STPMSTI5NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 2, 1, 1),
    _Gs2328STPMSTI5NormalPortConfPort_Type()
)
gs2328STPMSTI5NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI5NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI5NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI5NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI5NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI5NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI5NormalPortPathCost = _Gs2328STPMSTI5NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 2, 1, 2),
    _Gs2328STPMSTI5NormalPortPathCost_Type()
)
gs2328STPMSTI5NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI5NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI5NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI5NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI5NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI5NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI5NormalPortPriority = _Gs2328STPMSTI5NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 5, 2, 1, 3),
    _Gs2328STPMSTI5NormalPortPriority_Type()
)
gs2328STPMSTI5NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI5NormalPortPriority.setStatus("current")
_Gs2328STPMSTI6Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI6Port = _Gs2328STPMSTI6Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6)
)
_Gs2328STPMSTI6AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI6AggregatedPort = _Gs2328STPMSTI6AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 1)
)


class _Gs2328STPMSTI6AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI6AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI6AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI6AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI6AggregatedPortPathCost = _Gs2328STPMSTI6AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 1, 1),
    _Gs2328STPMSTI6AggregatedPortPathCost_Type()
)
gs2328STPMSTI6AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI6AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI6AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI6AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI6AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI6AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI6AggregatedPortPriority = _Gs2328STPMSTI6AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 1, 2),
    _Gs2328STPMSTI6AggregatedPortPriority_Type()
)
gs2328STPMSTI6AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI6AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI6NormalPortTable_Object = MibTable
gs2328STPMSTI6NormalPortTable = _Gs2328STPMSTI6NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI6NormalPortTable.setStatus("current")
_Gs2328STPMSTI6NormalPortEntry_Object = MibTableRow
gs2328STPMSTI6NormalPortEntry = _Gs2328STPMSTI6NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 2, 1)
)
gs2328STPMSTI6NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI6NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI6NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI6NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI6NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI6NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI6NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI6NormalPortConfPort = _Gs2328STPMSTI6NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 2, 1, 1),
    _Gs2328STPMSTI6NormalPortConfPort_Type()
)
gs2328STPMSTI6NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI6NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI6NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI6NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI6NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI6NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI6NormalPortPathCost = _Gs2328STPMSTI6NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 2, 1, 2),
    _Gs2328STPMSTI6NormalPortPathCost_Type()
)
gs2328STPMSTI6NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI6NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI6NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI6NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI6NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI6NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI6NormalPortPriority = _Gs2328STPMSTI6NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 6, 2, 1, 3),
    _Gs2328STPMSTI6NormalPortPriority_Type()
)
gs2328STPMSTI6NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI6NormalPortPriority.setStatus("current")
_Gs2328STPMSTI7Port_ObjectIdentity = ObjectIdentity
gs2328STPMSTI7Port = _Gs2328STPMSTI7Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7)
)
_Gs2328STPMSTI7AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328STPMSTI7AggregatedPort = _Gs2328STPMSTI7AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 1)
)


class _Gs2328STPMSTI7AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI7AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI7AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI7AggregatedPortPathCost_Object = MibScalar
gs2328STPMSTI7AggregatedPortPathCost = _Gs2328STPMSTI7AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 1, 1),
    _Gs2328STPMSTI7AggregatedPortPathCost_Type()
)
gs2328STPMSTI7AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI7AggregatedPortPathCost.setStatus("current")


class _Gs2328STPMSTI7AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI7AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI7AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI7AggregatedPortPriority_Object = MibScalar
gs2328STPMSTI7AggregatedPortPriority = _Gs2328STPMSTI7AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 1, 2),
    _Gs2328STPMSTI7AggregatedPortPriority_Type()
)
gs2328STPMSTI7AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI7AggregatedPortPriority.setStatus("current")
_Gs2328STPMSTI7NormalPortTable_Object = MibTable
gs2328STPMSTI7NormalPortTable = _Gs2328STPMSTI7NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328STPMSTI7NormalPortTable.setStatus("current")
_Gs2328STPMSTI7NormalPortEntry_Object = MibTableRow
gs2328STPMSTI7NormalPortEntry = _Gs2328STPMSTI7NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 2, 1)
)
gs2328STPMSTI7NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPMSTI7NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328STPMSTI7NormalPortEntry.setStatus("current")


class _Gs2328STPMSTI7NormalPortConfPort_Type(Integer32):
    """Custom type gs2328STPMSTI7NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPMSTI7NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328STPMSTI7NormalPortConfPort_Object = MibTableColumn
gs2328STPMSTI7NormalPortConfPort = _Gs2328STPMSTI7NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 2, 1, 1),
    _Gs2328STPMSTI7NormalPortConfPort_Type()
)
gs2328STPMSTI7NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPMSTI7NormalPortConfPort.setStatus("current")


class _Gs2328STPMSTI7NormalPortPathCost_Type(Integer32):
    """Custom type gs2328STPMSTI7NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328STPMSTI7NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328STPMSTI7NormalPortPathCost_Object = MibTableColumn
gs2328STPMSTI7NormalPortPathCost = _Gs2328STPMSTI7NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 2, 1, 2),
    _Gs2328STPMSTI7NormalPortPathCost_Type()
)
gs2328STPMSTI7NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI7NormalPortPathCost.setStatus("current")


class _Gs2328STPMSTI7NormalPortPriority_Type(Integer32):
    """Custom type gs2328STPMSTI7NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328STPMSTI7NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328STPMSTI7NormalPortPriority_Object = MibTableColumn
gs2328STPMSTI7NormalPortPriority = _Gs2328STPMSTI7NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 7, 7, 2, 1, 3),
    _Gs2328STPMSTI7NormalPortPriority_Type()
)
gs2328STPMSTI7NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328STPMSTI7NormalPortPriority.setStatus("current")
_Gs2328STPBridgeStatus_ObjectIdentity = ObjectIdentity
gs2328STPBridgeStatus = _Gs2328STPBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8)
)
_Gs2328CISTBridgeSTP_ObjectIdentity = ObjectIdentity
gs2328CISTBridgeSTP = _Gs2328CISTBridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1)
)
_Gs2328CISTBridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328CISTBridgeSTPStatus = _Gs2328CISTBridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1)
)
_Gs2328CISTBridgeInstance_Type = DisplayString
_Gs2328CISTBridgeInstance_Object = MibScalar
gs2328CISTBridgeInstance = _Gs2328CISTBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 1),
    _Gs2328CISTBridgeInstance_Type()
)
gs2328CISTBridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTBridgeInstance.setStatus("current")
_Gs2328CISTBridgeID_Type = DisplayString
_Gs2328CISTBridgeID_Object = MibScalar
gs2328CISTBridgeID = _Gs2328CISTBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 2),
    _Gs2328CISTBridgeID_Type()
)
gs2328CISTBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTBridgeID.setStatus("current")
_Gs2328CISTRootID_Type = DisplayString
_Gs2328CISTRootID_Object = MibScalar
gs2328CISTRootID = _Gs2328CISTRootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 3),
    _Gs2328CISTRootID_Type()
)
gs2328CISTRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTRootID.setStatus("current")
_Gs2328CISTRootPort_Type = DisplayString
_Gs2328CISTRootPort_Object = MibScalar
gs2328CISTRootPort = _Gs2328CISTRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 4),
    _Gs2328CISTRootPort_Type()
)
gs2328CISTRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTRootPort.setStatus("current")


class _Gs2328CISTRootCost_Type(Integer32):
    """Custom type gs2328CISTRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328CISTRootCost_Type.__name__ = "Integer32"
_Gs2328CISTRootCost_Object = MibScalar
gs2328CISTRootCost = _Gs2328CISTRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 5),
    _Gs2328CISTRootCost_Type()
)
gs2328CISTRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTRootCost.setStatus("current")
_Gs2328CISTRegionalRoot_Type = DisplayString
_Gs2328CISTRegionalRoot_Object = MibScalar
gs2328CISTRegionalRoot = _Gs2328CISTRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 6),
    _Gs2328CISTRegionalRoot_Type()
)
gs2328CISTRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTRegionalRoot.setStatus("current")


class _Gs2328CISTInternalRootCost_Type(Integer32):
    """Custom type gs2328CISTInternalRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328CISTInternalRootCost_Type.__name__ = "Integer32"
_Gs2328CISTInternalRootCost_Object = MibScalar
gs2328CISTInternalRootCost = _Gs2328CISTInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 7),
    _Gs2328CISTInternalRootCost_Type()
)
gs2328CISTInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTInternalRootCost.setStatus("current")
_Gs2328CISTTopologyFlag_Type = DisplayString
_Gs2328CISTTopologyFlag_Object = MibScalar
gs2328CISTTopologyFlag = _Gs2328CISTTopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 8),
    _Gs2328CISTTopologyFlag_Type()
)
gs2328CISTTopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTTopologyFlag.setStatus("current")
_Gs2328CISTTopologyChangeCount_Type = Counter32
_Gs2328CISTTopologyChangeCount_Object = MibScalar
gs2328CISTTopologyChangeCount = _Gs2328CISTTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 9),
    _Gs2328CISTTopologyChangeCount_Type()
)
gs2328CISTTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTTopologyChangeCount.setStatus("current")
_Gs2328CISTTopologyChangeLast_Type = DisplayString
_Gs2328CISTTopologyChangeLast_Object = MibScalar
gs2328CISTTopologyChangeLast = _Gs2328CISTTopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 1, 10),
    _Gs2328CISTTopologyChangeLast_Type()
)
gs2328CISTTopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTTopologyChangeLast.setStatus("current")
_Gs2328CISTPortStateTable_Object = MibTable
gs2328CISTPortStateTable = _Gs2328CISTPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328CISTPortStateTable.setStatus("current")
_Gs2328CISTPortStateEntry_Object = MibTableRow
gs2328CISTPortStateEntry = _Gs2328CISTPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1)
)
gs2328CISTPortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328CISTPortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328CISTPortStateEntry.setStatus("current")


class _Gs2328CISTPortStateIndex_Type(Integer32):
    """Custom type gs2328CISTPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328CISTPortStateIndex_Type.__name__ = "Integer32"
_Gs2328CISTPortStateIndex_Object = MibTableColumn
gs2328CISTPortStateIndex = _Gs2328CISTPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 1),
    _Gs2328CISTPortStateIndex_Type()
)
gs2328CISTPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328CISTPortStateIndex.setStatus("current")
_Gs2328CISTPortStatePort_Type = DisplayString
_Gs2328CISTPortStatePort_Object = MibTableColumn
gs2328CISTPortStatePort = _Gs2328CISTPortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 2),
    _Gs2328CISTPortStatePort_Type()
)
gs2328CISTPortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStatePort.setStatus("current")
_Gs2328CISTPortStatePortID_Type = DisplayString
_Gs2328CISTPortStatePortID_Object = MibTableColumn
gs2328CISTPortStatePortID = _Gs2328CISTPortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 3),
    _Gs2328CISTPortStatePortID_Type()
)
gs2328CISTPortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStatePortID.setStatus("current")
_Gs2328CISTPortStateRole_Type = DisplayString
_Gs2328CISTPortStateRole_Object = MibTableColumn
gs2328CISTPortStateRole = _Gs2328CISTPortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 4),
    _Gs2328CISTPortStateRole_Type()
)
gs2328CISTPortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStateRole.setStatus("current")
_Gs2328CISTPortStateState_Type = DisplayString
_Gs2328CISTPortStateState_Object = MibTableColumn
gs2328CISTPortStateState = _Gs2328CISTPortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 5),
    _Gs2328CISTPortStateState_Type()
)
gs2328CISTPortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStateState.setStatus("current")


class _Gs2328CISTPortStatePathCost_Type(Integer32):
    """Custom type gs2328CISTPortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328CISTPortStatePathCost_Type.__name__ = "Integer32"
_Gs2328CISTPortStatePathCost_Object = MibTableColumn
gs2328CISTPortStatePathCost = _Gs2328CISTPortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 6),
    _Gs2328CISTPortStatePathCost_Type()
)
gs2328CISTPortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStatePathCost.setStatus("current")
_Gs2328CISTPortStateEdge_Type = DisplayString
_Gs2328CISTPortStateEdge_Object = MibTableColumn
gs2328CISTPortStateEdge = _Gs2328CISTPortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 7),
    _Gs2328CISTPortStateEdge_Type()
)
gs2328CISTPortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStateEdge.setStatus("current")
_Gs2328CISTPortStatePoint2Point_Type = DisplayString
_Gs2328CISTPortStatePoint2Point_Object = MibTableColumn
gs2328CISTPortStatePoint2Point = _Gs2328CISTPortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 8),
    _Gs2328CISTPortStatePoint2Point_Type()
)
gs2328CISTPortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStatePoint2Point.setStatus("current")
_Gs2328CISTPortStateUptime_Type = DisplayString
_Gs2328CISTPortStateUptime_Object = MibTableColumn
gs2328CISTPortStateUptime = _Gs2328CISTPortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 1, 2, 1, 9),
    _Gs2328CISTPortStateUptime_Type()
)
gs2328CISTPortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328CISTPortStateUptime.setStatus("current")
_Gs2328MSTI1BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI1BridgeSTP = _Gs2328MSTI1BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2)
)
_Gs2328MSTI1BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI1BridgeSTPStatus = _Gs2328MSTI1BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1)
)
_Gs2328MSTI1BridgeInstance_Type = DisplayString
_Gs2328MSTI1BridgeInstance_Object = MibScalar
gs2328MSTI1BridgeInstance = _Gs2328MSTI1BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 1),
    _Gs2328MSTI1BridgeInstance_Type()
)
gs2328MSTI1BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1BridgeInstance.setStatus("current")
_Gs2328MSTI1BridgeID_Type = DisplayString
_Gs2328MSTI1BridgeID_Object = MibScalar
gs2328MSTI1BridgeID = _Gs2328MSTI1BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 2),
    _Gs2328MSTI1BridgeID_Type()
)
gs2328MSTI1BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1BridgeID.setStatus("current")
_Gs2328MSTI1RootID_Type = DisplayString
_Gs2328MSTI1RootID_Object = MibScalar
gs2328MSTI1RootID = _Gs2328MSTI1RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 3),
    _Gs2328MSTI1RootID_Type()
)
gs2328MSTI1RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1RootID.setStatus("current")
_Gs2328MSTI1RootPort_Type = DisplayString
_Gs2328MSTI1RootPort_Object = MibScalar
gs2328MSTI1RootPort = _Gs2328MSTI1RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 4),
    _Gs2328MSTI1RootPort_Type()
)
gs2328MSTI1RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1RootPort.setStatus("current")


class _Gs2328MSTI1RootCost_Type(Integer32):
    """Custom type gs2328MSTI1RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI1RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI1RootCost_Object = MibScalar
gs2328MSTI1RootCost = _Gs2328MSTI1RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 5),
    _Gs2328MSTI1RootCost_Type()
)
gs2328MSTI1RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1RootCost.setStatus("current")
_Gs2328MSTI1TopologyFlag_Type = DisplayString
_Gs2328MSTI1TopologyFlag_Object = MibScalar
gs2328MSTI1TopologyFlag = _Gs2328MSTI1TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 8),
    _Gs2328MSTI1TopologyFlag_Type()
)
gs2328MSTI1TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1TopologyFlag.setStatus("current")
_Gs2328MSTI1TopologyChangeCount_Type = Counter32
_Gs2328MSTI1TopologyChangeCount_Object = MibScalar
gs2328MSTI1TopologyChangeCount = _Gs2328MSTI1TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 9),
    _Gs2328MSTI1TopologyChangeCount_Type()
)
gs2328MSTI1TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1TopologyChangeCount.setStatus("current")
_Gs2328MSTI1TopologyChangeLast_Type = DisplayString
_Gs2328MSTI1TopologyChangeLast_Object = MibScalar
gs2328MSTI1TopologyChangeLast = _Gs2328MSTI1TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 1, 10),
    _Gs2328MSTI1TopologyChangeLast_Type()
)
gs2328MSTI1TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1TopologyChangeLast.setStatus("current")
_Gs2328MSTI1PortStateTable_Object = MibTable
gs2328MSTI1PortStateTable = _Gs2328MSTI1PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateTable.setStatus("current")
_Gs2328MSTI1PortStateEntry_Object = MibTableRow
gs2328MSTI1PortStateEntry = _Gs2328MSTI1PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1)
)
gs2328MSTI1PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI1PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateEntry.setStatus("current")


class _Gs2328MSTI1PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI1PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI1PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI1PortStateIndex_Object = MibTableColumn
gs2328MSTI1PortStateIndex = _Gs2328MSTI1PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 1),
    _Gs2328MSTI1PortStateIndex_Type()
)
gs2328MSTI1PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateIndex.setStatus("current")
_Gs2328MSTI1PortStatePort_Type = DisplayString
_Gs2328MSTI1PortStatePort_Object = MibTableColumn
gs2328MSTI1PortStatePort = _Gs2328MSTI1PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 2),
    _Gs2328MSTI1PortStatePort_Type()
)
gs2328MSTI1PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStatePort.setStatus("current")
_Gs2328MSTI1PortStatePortID_Type = DisplayString
_Gs2328MSTI1PortStatePortID_Object = MibTableColumn
gs2328MSTI1PortStatePortID = _Gs2328MSTI1PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 3),
    _Gs2328MSTI1PortStatePortID_Type()
)
gs2328MSTI1PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStatePortID.setStatus("current")
_Gs2328MSTI1PortStateRole_Type = DisplayString
_Gs2328MSTI1PortStateRole_Object = MibTableColumn
gs2328MSTI1PortStateRole = _Gs2328MSTI1PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 4),
    _Gs2328MSTI1PortStateRole_Type()
)
gs2328MSTI1PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateRole.setStatus("current")
_Gs2328MSTI1PortStateState_Type = DisplayString
_Gs2328MSTI1PortStateState_Object = MibTableColumn
gs2328MSTI1PortStateState = _Gs2328MSTI1PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 5),
    _Gs2328MSTI1PortStateState_Type()
)
gs2328MSTI1PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateState.setStatus("current")


class _Gs2328MSTI1PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI1PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI1PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI1PortStatePathCost_Object = MibTableColumn
gs2328MSTI1PortStatePathCost = _Gs2328MSTI1PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 6),
    _Gs2328MSTI1PortStatePathCost_Type()
)
gs2328MSTI1PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStatePathCost.setStatus("current")
_Gs2328MSTI1PortStateEdge_Type = DisplayString
_Gs2328MSTI1PortStateEdge_Object = MibTableColumn
gs2328MSTI1PortStateEdge = _Gs2328MSTI1PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 7),
    _Gs2328MSTI1PortStateEdge_Type()
)
gs2328MSTI1PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateEdge.setStatus("current")
_Gs2328MSTI1PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI1PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI1PortStatePoint2Point = _Gs2328MSTI1PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 8),
    _Gs2328MSTI1PortStatePoint2Point_Type()
)
gs2328MSTI1PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStatePoint2Point.setStatus("current")
_Gs2328MSTI1PortStateUptime_Type = DisplayString
_Gs2328MSTI1PortStateUptime_Object = MibTableColumn
gs2328MSTI1PortStateUptime = _Gs2328MSTI1PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 2, 2, 1, 9),
    _Gs2328MSTI1PortStateUptime_Type()
)
gs2328MSTI1PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI1PortStateUptime.setStatus("current")
_Gs2328MSTI2BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI2BridgeSTP = _Gs2328MSTI2BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3)
)
_Gs2328MSTI2BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI2BridgeSTPStatus = _Gs2328MSTI2BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1)
)
_Gs2328MSTI2BridgeInstance_Type = DisplayString
_Gs2328MSTI2BridgeInstance_Object = MibScalar
gs2328MSTI2BridgeInstance = _Gs2328MSTI2BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 1),
    _Gs2328MSTI2BridgeInstance_Type()
)
gs2328MSTI2BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2BridgeInstance.setStatus("current")
_Gs2328MSTI2BridgeID_Type = DisplayString
_Gs2328MSTI2BridgeID_Object = MibScalar
gs2328MSTI2BridgeID = _Gs2328MSTI2BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 2),
    _Gs2328MSTI2BridgeID_Type()
)
gs2328MSTI2BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2BridgeID.setStatus("current")
_Gs2328MSTI2RootID_Type = DisplayString
_Gs2328MSTI2RootID_Object = MibScalar
gs2328MSTI2RootID = _Gs2328MSTI2RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 3),
    _Gs2328MSTI2RootID_Type()
)
gs2328MSTI2RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2RootID.setStatus("current")
_Gs2328MSTI2RootPort_Type = DisplayString
_Gs2328MSTI2RootPort_Object = MibScalar
gs2328MSTI2RootPort = _Gs2328MSTI2RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 4),
    _Gs2328MSTI2RootPort_Type()
)
gs2328MSTI2RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2RootPort.setStatus("current")


class _Gs2328MSTI2RootCost_Type(Integer32):
    """Custom type gs2328MSTI2RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI2RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI2RootCost_Object = MibScalar
gs2328MSTI2RootCost = _Gs2328MSTI2RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 5),
    _Gs2328MSTI2RootCost_Type()
)
gs2328MSTI2RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2RootCost.setStatus("current")
_Gs2328MSTI2TopologyFlag_Type = DisplayString
_Gs2328MSTI2TopologyFlag_Object = MibScalar
gs2328MSTI2TopologyFlag = _Gs2328MSTI2TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 8),
    _Gs2328MSTI2TopologyFlag_Type()
)
gs2328MSTI2TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2TopologyFlag.setStatus("current")
_Gs2328MSTI2TopologyChangeCount_Type = Counter32
_Gs2328MSTI2TopologyChangeCount_Object = MibScalar
gs2328MSTI2TopologyChangeCount = _Gs2328MSTI2TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 9),
    _Gs2328MSTI2TopologyChangeCount_Type()
)
gs2328MSTI2TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2TopologyChangeCount.setStatus("current")
_Gs2328MSTI2TopologyChangeLast_Type = DisplayString
_Gs2328MSTI2TopologyChangeLast_Object = MibScalar
gs2328MSTI2TopologyChangeLast = _Gs2328MSTI2TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 1, 10),
    _Gs2328MSTI2TopologyChangeLast_Type()
)
gs2328MSTI2TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2TopologyChangeLast.setStatus("current")
_Gs2328MSTI2PortStateTable_Object = MibTable
gs2328MSTI2PortStateTable = _Gs2328MSTI2PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateTable.setStatus("current")
_Gs2328MSTI2PortStateEntry_Object = MibTableRow
gs2328MSTI2PortStateEntry = _Gs2328MSTI2PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1)
)
gs2328MSTI2PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI2PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateEntry.setStatus("current")


class _Gs2328MSTI2PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI2PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI2PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI2PortStateIndex_Object = MibTableColumn
gs2328MSTI2PortStateIndex = _Gs2328MSTI2PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 1),
    _Gs2328MSTI2PortStateIndex_Type()
)
gs2328MSTI2PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateIndex.setStatus("current")
_Gs2328MSTI2PortStatePort_Type = DisplayString
_Gs2328MSTI2PortStatePort_Object = MibTableColumn
gs2328MSTI2PortStatePort = _Gs2328MSTI2PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 2),
    _Gs2328MSTI2PortStatePort_Type()
)
gs2328MSTI2PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStatePort.setStatus("current")
_Gs2328MSTI2PortStatePortID_Type = DisplayString
_Gs2328MSTI2PortStatePortID_Object = MibTableColumn
gs2328MSTI2PortStatePortID = _Gs2328MSTI2PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 3),
    _Gs2328MSTI2PortStatePortID_Type()
)
gs2328MSTI2PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStatePortID.setStatus("current")
_Gs2328MSTI2PortStateRole_Type = DisplayString
_Gs2328MSTI2PortStateRole_Object = MibTableColumn
gs2328MSTI2PortStateRole = _Gs2328MSTI2PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 4),
    _Gs2328MSTI2PortStateRole_Type()
)
gs2328MSTI2PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateRole.setStatus("current")
_Gs2328MSTI2PortStateState_Type = DisplayString
_Gs2328MSTI2PortStateState_Object = MibTableColumn
gs2328MSTI2PortStateState = _Gs2328MSTI2PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 5),
    _Gs2328MSTI2PortStateState_Type()
)
gs2328MSTI2PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateState.setStatus("current")


class _Gs2328MSTI2PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI2PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI2PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI2PortStatePathCost_Object = MibTableColumn
gs2328MSTI2PortStatePathCost = _Gs2328MSTI2PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 6),
    _Gs2328MSTI2PortStatePathCost_Type()
)
gs2328MSTI2PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStatePathCost.setStatus("current")
_Gs2328MSTI2PortStateEdge_Type = DisplayString
_Gs2328MSTI2PortStateEdge_Object = MibTableColumn
gs2328MSTI2PortStateEdge = _Gs2328MSTI2PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 7),
    _Gs2328MSTI2PortStateEdge_Type()
)
gs2328MSTI2PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateEdge.setStatus("current")
_Gs2328MSTI2PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI2PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI2PortStatePoint2Point = _Gs2328MSTI2PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 8),
    _Gs2328MSTI2PortStatePoint2Point_Type()
)
gs2328MSTI2PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStatePoint2Point.setStatus("current")
_Gs2328MSTI2PortStateUptime_Type = DisplayString
_Gs2328MSTI2PortStateUptime_Object = MibTableColumn
gs2328MSTI2PortStateUptime = _Gs2328MSTI2PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 3, 2, 1, 9),
    _Gs2328MSTI2PortStateUptime_Type()
)
gs2328MSTI2PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI2PortStateUptime.setStatus("current")
_Gs2328MSTI3BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI3BridgeSTP = _Gs2328MSTI3BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4)
)
_Gs2328MSTI3BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI3BridgeSTPStatus = _Gs2328MSTI3BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1)
)
_Gs2328MSTI3BridgeInstance_Type = DisplayString
_Gs2328MSTI3BridgeInstance_Object = MibScalar
gs2328MSTI3BridgeInstance = _Gs2328MSTI3BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 1),
    _Gs2328MSTI3BridgeInstance_Type()
)
gs2328MSTI3BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3BridgeInstance.setStatus("current")
_Gs2328MSTI3BridgeID_Type = DisplayString
_Gs2328MSTI3BridgeID_Object = MibScalar
gs2328MSTI3BridgeID = _Gs2328MSTI3BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 2),
    _Gs2328MSTI3BridgeID_Type()
)
gs2328MSTI3BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3BridgeID.setStatus("current")
_Gs2328MSTI3RootID_Type = DisplayString
_Gs2328MSTI3RootID_Object = MibScalar
gs2328MSTI3RootID = _Gs2328MSTI3RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 3),
    _Gs2328MSTI3RootID_Type()
)
gs2328MSTI3RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3RootID.setStatus("current")
_Gs2328MSTI3RootPort_Type = DisplayString
_Gs2328MSTI3RootPort_Object = MibScalar
gs2328MSTI3RootPort = _Gs2328MSTI3RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 4),
    _Gs2328MSTI3RootPort_Type()
)
gs2328MSTI3RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3RootPort.setStatus("current")


class _Gs2328MSTI3RootCost_Type(Integer32):
    """Custom type gs2328MSTI3RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI3RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI3RootCost_Object = MibScalar
gs2328MSTI3RootCost = _Gs2328MSTI3RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 5),
    _Gs2328MSTI3RootCost_Type()
)
gs2328MSTI3RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3RootCost.setStatus("current")
_Gs2328MSTI3TopologyFlag_Type = DisplayString
_Gs2328MSTI3TopologyFlag_Object = MibScalar
gs2328MSTI3TopologyFlag = _Gs2328MSTI3TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 8),
    _Gs2328MSTI3TopologyFlag_Type()
)
gs2328MSTI3TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3TopologyFlag.setStatus("current")
_Gs2328MSTI3TopologyChangeCount_Type = Counter32
_Gs2328MSTI3TopologyChangeCount_Object = MibScalar
gs2328MSTI3TopologyChangeCount = _Gs2328MSTI3TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 9),
    _Gs2328MSTI3TopologyChangeCount_Type()
)
gs2328MSTI3TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3TopologyChangeCount.setStatus("current")
_Gs2328MSTI3TopologyChangeLast_Type = DisplayString
_Gs2328MSTI3TopologyChangeLast_Object = MibScalar
gs2328MSTI3TopologyChangeLast = _Gs2328MSTI3TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 1, 10),
    _Gs2328MSTI3TopologyChangeLast_Type()
)
gs2328MSTI3TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3TopologyChangeLast.setStatus("current")
_Gs2328MSTI3PortStateTable_Object = MibTable
gs2328MSTI3PortStateTable = _Gs2328MSTI3PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateTable.setStatus("current")
_Gs2328MSTI3PortStateEntry_Object = MibTableRow
gs2328MSTI3PortStateEntry = _Gs2328MSTI3PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1)
)
gs2328MSTI3PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI3PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateEntry.setStatus("current")


class _Gs2328MSTI3PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI3PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI3PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI3PortStateIndex_Object = MibTableColumn
gs2328MSTI3PortStateIndex = _Gs2328MSTI3PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 1),
    _Gs2328MSTI3PortStateIndex_Type()
)
gs2328MSTI3PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateIndex.setStatus("current")
_Gs2328MSTI3PortStatePort_Type = DisplayString
_Gs2328MSTI3PortStatePort_Object = MibTableColumn
gs2328MSTI3PortStatePort = _Gs2328MSTI3PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 2),
    _Gs2328MSTI3PortStatePort_Type()
)
gs2328MSTI3PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStatePort.setStatus("current")
_Gs2328MSTI3PortStatePortID_Type = DisplayString
_Gs2328MSTI3PortStatePortID_Object = MibTableColumn
gs2328MSTI3PortStatePortID = _Gs2328MSTI3PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 3),
    _Gs2328MSTI3PortStatePortID_Type()
)
gs2328MSTI3PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStatePortID.setStatus("current")
_Gs2328MSTI3PortStateRole_Type = DisplayString
_Gs2328MSTI3PortStateRole_Object = MibTableColumn
gs2328MSTI3PortStateRole = _Gs2328MSTI3PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 4),
    _Gs2328MSTI3PortStateRole_Type()
)
gs2328MSTI3PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateRole.setStatus("current")
_Gs2328MSTI3PortStateState_Type = DisplayString
_Gs2328MSTI3PortStateState_Object = MibTableColumn
gs2328MSTI3PortStateState = _Gs2328MSTI3PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 5),
    _Gs2328MSTI3PortStateState_Type()
)
gs2328MSTI3PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateState.setStatus("current")


class _Gs2328MSTI3PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI3PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI3PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI3PortStatePathCost_Object = MibTableColumn
gs2328MSTI3PortStatePathCost = _Gs2328MSTI3PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 6),
    _Gs2328MSTI3PortStatePathCost_Type()
)
gs2328MSTI3PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStatePathCost.setStatus("current")
_Gs2328MSTI3PortStateEdge_Type = DisplayString
_Gs2328MSTI3PortStateEdge_Object = MibTableColumn
gs2328MSTI3PortStateEdge = _Gs2328MSTI3PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 7),
    _Gs2328MSTI3PortStateEdge_Type()
)
gs2328MSTI3PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateEdge.setStatus("current")
_Gs2328MSTI3PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI3PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI3PortStatePoint2Point = _Gs2328MSTI3PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 8),
    _Gs2328MSTI3PortStatePoint2Point_Type()
)
gs2328MSTI3PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStatePoint2Point.setStatus("current")
_Gs2328MSTI3PortStateUptime_Type = DisplayString
_Gs2328MSTI3PortStateUptime_Object = MibTableColumn
gs2328MSTI3PortStateUptime = _Gs2328MSTI3PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 4, 2, 1, 9),
    _Gs2328MSTI3PortStateUptime_Type()
)
gs2328MSTI3PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI3PortStateUptime.setStatus("current")
_Gs2328MSTI4BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI4BridgeSTP = _Gs2328MSTI4BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5)
)
_Gs2328MSTI4BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI4BridgeSTPStatus = _Gs2328MSTI4BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1)
)
_Gs2328MSTI4BridgeInstance_Type = DisplayString
_Gs2328MSTI4BridgeInstance_Object = MibScalar
gs2328MSTI4BridgeInstance = _Gs2328MSTI4BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 1),
    _Gs2328MSTI4BridgeInstance_Type()
)
gs2328MSTI4BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4BridgeInstance.setStatus("current")
_Gs2328MSTI4BridgeID_Type = DisplayString
_Gs2328MSTI4BridgeID_Object = MibScalar
gs2328MSTI4BridgeID = _Gs2328MSTI4BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 2),
    _Gs2328MSTI4BridgeID_Type()
)
gs2328MSTI4BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4BridgeID.setStatus("current")
_Gs2328MSTI4RootID_Type = DisplayString
_Gs2328MSTI4RootID_Object = MibScalar
gs2328MSTI4RootID = _Gs2328MSTI4RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 3),
    _Gs2328MSTI4RootID_Type()
)
gs2328MSTI4RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4RootID.setStatus("current")
_Gs2328MSTI4RootPort_Type = DisplayString
_Gs2328MSTI4RootPort_Object = MibScalar
gs2328MSTI4RootPort = _Gs2328MSTI4RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 4),
    _Gs2328MSTI4RootPort_Type()
)
gs2328MSTI4RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4RootPort.setStatus("current")


class _Gs2328MSTI4RootCost_Type(Integer32):
    """Custom type gs2328MSTI4RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI4RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI4RootCost_Object = MibScalar
gs2328MSTI4RootCost = _Gs2328MSTI4RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 5),
    _Gs2328MSTI4RootCost_Type()
)
gs2328MSTI4RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4RootCost.setStatus("current")
_Gs2328MSTI4TopologyFlag_Type = DisplayString
_Gs2328MSTI4TopologyFlag_Object = MibScalar
gs2328MSTI4TopologyFlag = _Gs2328MSTI4TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 8),
    _Gs2328MSTI4TopologyFlag_Type()
)
gs2328MSTI4TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4TopologyFlag.setStatus("current")
_Gs2328MSTI4TopologyChangeCount_Type = Counter32
_Gs2328MSTI4TopologyChangeCount_Object = MibScalar
gs2328MSTI4TopologyChangeCount = _Gs2328MSTI4TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 9),
    _Gs2328MSTI4TopologyChangeCount_Type()
)
gs2328MSTI4TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4TopologyChangeCount.setStatus("current")
_Gs2328MSTI4TopologyChangeLast_Type = DisplayString
_Gs2328MSTI4TopologyChangeLast_Object = MibScalar
gs2328MSTI4TopologyChangeLast = _Gs2328MSTI4TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 1, 10),
    _Gs2328MSTI4TopologyChangeLast_Type()
)
gs2328MSTI4TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4TopologyChangeLast.setStatus("current")
_Gs2328MSTI4PortStateTable_Object = MibTable
gs2328MSTI4PortStateTable = _Gs2328MSTI4PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateTable.setStatus("current")
_Gs2328MSTI4PortStateEntry_Object = MibTableRow
gs2328MSTI4PortStateEntry = _Gs2328MSTI4PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1)
)
gs2328MSTI4PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI4PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateEntry.setStatus("current")


class _Gs2328MSTI4PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI4PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI4PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI4PortStateIndex_Object = MibTableColumn
gs2328MSTI4PortStateIndex = _Gs2328MSTI4PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 1),
    _Gs2328MSTI4PortStateIndex_Type()
)
gs2328MSTI4PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateIndex.setStatus("current")
_Gs2328MSTI4PortStatePort_Type = DisplayString
_Gs2328MSTI4PortStatePort_Object = MibTableColumn
gs2328MSTI4PortStatePort = _Gs2328MSTI4PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 2),
    _Gs2328MSTI4PortStatePort_Type()
)
gs2328MSTI4PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStatePort.setStatus("current")
_Gs2328MSTI4PortStatePortID_Type = DisplayString
_Gs2328MSTI4PortStatePortID_Object = MibTableColumn
gs2328MSTI4PortStatePortID = _Gs2328MSTI4PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 3),
    _Gs2328MSTI4PortStatePortID_Type()
)
gs2328MSTI4PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStatePortID.setStatus("current")
_Gs2328MSTI4PortStateRole_Type = DisplayString
_Gs2328MSTI4PortStateRole_Object = MibTableColumn
gs2328MSTI4PortStateRole = _Gs2328MSTI4PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 4),
    _Gs2328MSTI4PortStateRole_Type()
)
gs2328MSTI4PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateRole.setStatus("current")
_Gs2328MSTI4PortStateState_Type = DisplayString
_Gs2328MSTI4PortStateState_Object = MibTableColumn
gs2328MSTI4PortStateState = _Gs2328MSTI4PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 5),
    _Gs2328MSTI4PortStateState_Type()
)
gs2328MSTI4PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateState.setStatus("current")


class _Gs2328MSTI4PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI4PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI4PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI4PortStatePathCost_Object = MibTableColumn
gs2328MSTI4PortStatePathCost = _Gs2328MSTI4PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 6),
    _Gs2328MSTI4PortStatePathCost_Type()
)
gs2328MSTI4PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStatePathCost.setStatus("current")
_Gs2328MSTI4PortStateEdge_Type = DisplayString
_Gs2328MSTI4PortStateEdge_Object = MibTableColumn
gs2328MSTI4PortStateEdge = _Gs2328MSTI4PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 7),
    _Gs2328MSTI4PortStateEdge_Type()
)
gs2328MSTI4PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateEdge.setStatus("current")
_Gs2328MSTI4PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI4PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI4PortStatePoint2Point = _Gs2328MSTI4PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 8),
    _Gs2328MSTI4PortStatePoint2Point_Type()
)
gs2328MSTI4PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStatePoint2Point.setStatus("current")
_Gs2328MSTI4PortStateUptime_Type = DisplayString
_Gs2328MSTI4PortStateUptime_Object = MibTableColumn
gs2328MSTI4PortStateUptime = _Gs2328MSTI4PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 5, 2, 1, 9),
    _Gs2328MSTI4PortStateUptime_Type()
)
gs2328MSTI4PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI4PortStateUptime.setStatus("current")
_Gs2328MSTI5BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI5BridgeSTP = _Gs2328MSTI5BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6)
)
_Gs2328MSTI5BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI5BridgeSTPStatus = _Gs2328MSTI5BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1)
)
_Gs2328MSTI5BridgeInstance_Type = DisplayString
_Gs2328MSTI5BridgeInstance_Object = MibScalar
gs2328MSTI5BridgeInstance = _Gs2328MSTI5BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 1),
    _Gs2328MSTI5BridgeInstance_Type()
)
gs2328MSTI5BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5BridgeInstance.setStatus("current")
_Gs2328MSTI5BridgeID_Type = DisplayString
_Gs2328MSTI5BridgeID_Object = MibScalar
gs2328MSTI5BridgeID = _Gs2328MSTI5BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 2),
    _Gs2328MSTI5BridgeID_Type()
)
gs2328MSTI5BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5BridgeID.setStatus("current")
_Gs2328MSTI5RootID_Type = DisplayString
_Gs2328MSTI5RootID_Object = MibScalar
gs2328MSTI5RootID = _Gs2328MSTI5RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 3),
    _Gs2328MSTI5RootID_Type()
)
gs2328MSTI5RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5RootID.setStatus("current")
_Gs2328MSTI5RootPort_Type = DisplayString
_Gs2328MSTI5RootPort_Object = MibScalar
gs2328MSTI5RootPort = _Gs2328MSTI5RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 4),
    _Gs2328MSTI5RootPort_Type()
)
gs2328MSTI5RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5RootPort.setStatus("current")


class _Gs2328MSTI5RootCost_Type(Integer32):
    """Custom type gs2328MSTI5RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI5RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI5RootCost_Object = MibScalar
gs2328MSTI5RootCost = _Gs2328MSTI5RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 5),
    _Gs2328MSTI5RootCost_Type()
)
gs2328MSTI5RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5RootCost.setStatus("current")
_Gs2328MSTI5TopologyFlag_Type = DisplayString
_Gs2328MSTI5TopologyFlag_Object = MibScalar
gs2328MSTI5TopologyFlag = _Gs2328MSTI5TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 8),
    _Gs2328MSTI5TopologyFlag_Type()
)
gs2328MSTI5TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5TopologyFlag.setStatus("current")
_Gs2328MSTI5TopologyChangeCount_Type = Counter32
_Gs2328MSTI5TopologyChangeCount_Object = MibScalar
gs2328MSTI5TopologyChangeCount = _Gs2328MSTI5TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 9),
    _Gs2328MSTI5TopologyChangeCount_Type()
)
gs2328MSTI5TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5TopologyChangeCount.setStatus("current")
_Gs2328MSTI5TopologyChangeLast_Type = DisplayString
_Gs2328MSTI5TopologyChangeLast_Object = MibScalar
gs2328MSTI5TopologyChangeLast = _Gs2328MSTI5TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 1, 10),
    _Gs2328MSTI5TopologyChangeLast_Type()
)
gs2328MSTI5TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5TopologyChangeLast.setStatus("current")
_Gs2328MSTI5PortStateTable_Object = MibTable
gs2328MSTI5PortStateTable = _Gs2328MSTI5PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateTable.setStatus("current")
_Gs2328MSTI5PortStateEntry_Object = MibTableRow
gs2328MSTI5PortStateEntry = _Gs2328MSTI5PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1)
)
gs2328MSTI5PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI5PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateEntry.setStatus("current")


class _Gs2328MSTI5PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI5PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI5PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI5PortStateIndex_Object = MibTableColumn
gs2328MSTI5PortStateIndex = _Gs2328MSTI5PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 1),
    _Gs2328MSTI5PortStateIndex_Type()
)
gs2328MSTI5PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateIndex.setStatus("current")
_Gs2328MSTI5PortStatePort_Type = DisplayString
_Gs2328MSTI5PortStatePort_Object = MibTableColumn
gs2328MSTI5PortStatePort = _Gs2328MSTI5PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 2),
    _Gs2328MSTI5PortStatePort_Type()
)
gs2328MSTI5PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStatePort.setStatus("current")
_Gs2328MSTI5PortStatePortID_Type = DisplayString
_Gs2328MSTI5PortStatePortID_Object = MibTableColumn
gs2328MSTI5PortStatePortID = _Gs2328MSTI5PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 3),
    _Gs2328MSTI5PortStatePortID_Type()
)
gs2328MSTI5PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStatePortID.setStatus("current")
_Gs2328MSTI5PortStateRole_Type = DisplayString
_Gs2328MSTI5PortStateRole_Object = MibTableColumn
gs2328MSTI5PortStateRole = _Gs2328MSTI5PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 4),
    _Gs2328MSTI5PortStateRole_Type()
)
gs2328MSTI5PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateRole.setStatus("current")
_Gs2328MSTI5PortStateState_Type = DisplayString
_Gs2328MSTI5PortStateState_Object = MibTableColumn
gs2328MSTI5PortStateState = _Gs2328MSTI5PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 5),
    _Gs2328MSTI5PortStateState_Type()
)
gs2328MSTI5PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateState.setStatus("current")


class _Gs2328MSTI5PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI5PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI5PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI5PortStatePathCost_Object = MibTableColumn
gs2328MSTI5PortStatePathCost = _Gs2328MSTI5PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 6),
    _Gs2328MSTI5PortStatePathCost_Type()
)
gs2328MSTI5PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStatePathCost.setStatus("current")
_Gs2328MSTI5PortStateEdge_Type = DisplayString
_Gs2328MSTI5PortStateEdge_Object = MibTableColumn
gs2328MSTI5PortStateEdge = _Gs2328MSTI5PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 7),
    _Gs2328MSTI5PortStateEdge_Type()
)
gs2328MSTI5PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateEdge.setStatus("current")
_Gs2328MSTI5PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI5PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI5PortStatePoint2Point = _Gs2328MSTI5PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 8),
    _Gs2328MSTI5PortStatePoint2Point_Type()
)
gs2328MSTI5PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStatePoint2Point.setStatus("current")
_Gs2328MSTI5PortStateUptime_Type = DisplayString
_Gs2328MSTI5PortStateUptime_Object = MibTableColumn
gs2328MSTI5PortStateUptime = _Gs2328MSTI5PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 6, 2, 1, 9),
    _Gs2328MSTI5PortStateUptime_Type()
)
gs2328MSTI5PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI5PortStateUptime.setStatus("current")
_Gs2328MSTI6BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI6BridgeSTP = _Gs2328MSTI6BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7)
)
_Gs2328MSTI6BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI6BridgeSTPStatus = _Gs2328MSTI6BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1)
)
_Gs2328MSTI6BridgeInstance_Type = DisplayString
_Gs2328MSTI6BridgeInstance_Object = MibScalar
gs2328MSTI6BridgeInstance = _Gs2328MSTI6BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 1),
    _Gs2328MSTI6BridgeInstance_Type()
)
gs2328MSTI6BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6BridgeInstance.setStatus("current")
_Gs2328MSTI6BridgeID_Type = DisplayString
_Gs2328MSTI6BridgeID_Object = MibScalar
gs2328MSTI6BridgeID = _Gs2328MSTI6BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 2),
    _Gs2328MSTI6BridgeID_Type()
)
gs2328MSTI6BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6BridgeID.setStatus("current")
_Gs2328MSTI6RootID_Type = DisplayString
_Gs2328MSTI6RootID_Object = MibScalar
gs2328MSTI6RootID = _Gs2328MSTI6RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 3),
    _Gs2328MSTI6RootID_Type()
)
gs2328MSTI6RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6RootID.setStatus("current")
_Gs2328MSTI6RootPort_Type = DisplayString
_Gs2328MSTI6RootPort_Object = MibScalar
gs2328MSTI6RootPort = _Gs2328MSTI6RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 4),
    _Gs2328MSTI6RootPort_Type()
)
gs2328MSTI6RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6RootPort.setStatus("current")


class _Gs2328MSTI6RootCost_Type(Integer32):
    """Custom type gs2328MSTI6RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI6RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI6RootCost_Object = MibScalar
gs2328MSTI6RootCost = _Gs2328MSTI6RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 5),
    _Gs2328MSTI6RootCost_Type()
)
gs2328MSTI6RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6RootCost.setStatus("current")
_Gs2328MSTI6TopologyFlag_Type = DisplayString
_Gs2328MSTI6TopologyFlag_Object = MibScalar
gs2328MSTI6TopologyFlag = _Gs2328MSTI6TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 8),
    _Gs2328MSTI6TopologyFlag_Type()
)
gs2328MSTI6TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6TopologyFlag.setStatus("current")
_Gs2328MSTI6TopologyChangeCount_Type = Counter32
_Gs2328MSTI6TopologyChangeCount_Object = MibScalar
gs2328MSTI6TopologyChangeCount = _Gs2328MSTI6TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 9),
    _Gs2328MSTI6TopologyChangeCount_Type()
)
gs2328MSTI6TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6TopologyChangeCount.setStatus("current")
_Gs2328MSTI6TopologyChangeLast_Type = DisplayString
_Gs2328MSTI6TopologyChangeLast_Object = MibScalar
gs2328MSTI6TopologyChangeLast = _Gs2328MSTI6TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 1, 10),
    _Gs2328MSTI6TopologyChangeLast_Type()
)
gs2328MSTI6TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6TopologyChangeLast.setStatus("current")
_Gs2328MSTI6PortStateTable_Object = MibTable
gs2328MSTI6PortStateTable = _Gs2328MSTI6PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateTable.setStatus("current")
_Gs2328MSTI6PortStateEntry_Object = MibTableRow
gs2328MSTI6PortStateEntry = _Gs2328MSTI6PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1)
)
gs2328MSTI6PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI6PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateEntry.setStatus("current")


class _Gs2328MSTI6PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI6PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI6PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI6PortStateIndex_Object = MibTableColumn
gs2328MSTI6PortStateIndex = _Gs2328MSTI6PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 1),
    _Gs2328MSTI6PortStateIndex_Type()
)
gs2328MSTI6PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateIndex.setStatus("current")
_Gs2328MSTI6PortStatePort_Type = DisplayString
_Gs2328MSTI6PortStatePort_Object = MibTableColumn
gs2328MSTI6PortStatePort = _Gs2328MSTI6PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 2),
    _Gs2328MSTI6PortStatePort_Type()
)
gs2328MSTI6PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStatePort.setStatus("current")
_Gs2328MSTI6PortStatePortID_Type = DisplayString
_Gs2328MSTI6PortStatePortID_Object = MibTableColumn
gs2328MSTI6PortStatePortID = _Gs2328MSTI6PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 3),
    _Gs2328MSTI6PortStatePortID_Type()
)
gs2328MSTI6PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStatePortID.setStatus("current")
_Gs2328MSTI6PortStateRole_Type = DisplayString
_Gs2328MSTI6PortStateRole_Object = MibTableColumn
gs2328MSTI6PortStateRole = _Gs2328MSTI6PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 4),
    _Gs2328MSTI6PortStateRole_Type()
)
gs2328MSTI6PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateRole.setStatus("current")
_Gs2328MSTI6PortStateState_Type = DisplayString
_Gs2328MSTI6PortStateState_Object = MibTableColumn
gs2328MSTI6PortStateState = _Gs2328MSTI6PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 5),
    _Gs2328MSTI6PortStateState_Type()
)
gs2328MSTI6PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateState.setStatus("current")


class _Gs2328MSTI6PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI6PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI6PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI6PortStatePathCost_Object = MibTableColumn
gs2328MSTI6PortStatePathCost = _Gs2328MSTI6PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 6),
    _Gs2328MSTI6PortStatePathCost_Type()
)
gs2328MSTI6PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStatePathCost.setStatus("current")
_Gs2328MSTI6PortStateEdge_Type = DisplayString
_Gs2328MSTI6PortStateEdge_Object = MibTableColumn
gs2328MSTI6PortStateEdge = _Gs2328MSTI6PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 7),
    _Gs2328MSTI6PortStateEdge_Type()
)
gs2328MSTI6PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateEdge.setStatus("current")
_Gs2328MSTI6PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI6PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI6PortStatePoint2Point = _Gs2328MSTI6PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 8),
    _Gs2328MSTI6PortStatePoint2Point_Type()
)
gs2328MSTI6PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStatePoint2Point.setStatus("current")
_Gs2328MSTI6PortStateUptime_Type = DisplayString
_Gs2328MSTI6PortStateUptime_Object = MibTableColumn
gs2328MSTI6PortStateUptime = _Gs2328MSTI6PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 7, 2, 1, 9),
    _Gs2328MSTI6PortStateUptime_Type()
)
gs2328MSTI6PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI6PortStateUptime.setStatus("current")
_Gs2328MSTI7BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328MSTI7BridgeSTP = _Gs2328MSTI7BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8)
)
_Gs2328MSTI7BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328MSTI7BridgeSTPStatus = _Gs2328MSTI7BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1)
)
_Gs2328MSTI7BridgeInstance_Type = DisplayString
_Gs2328MSTI7BridgeInstance_Object = MibScalar
gs2328MSTI7BridgeInstance = _Gs2328MSTI7BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 1),
    _Gs2328MSTI7BridgeInstance_Type()
)
gs2328MSTI7BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7BridgeInstance.setStatus("current")
_Gs2328MSTI7BridgeID_Type = DisplayString
_Gs2328MSTI7BridgeID_Object = MibScalar
gs2328MSTI7BridgeID = _Gs2328MSTI7BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 2),
    _Gs2328MSTI7BridgeID_Type()
)
gs2328MSTI7BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7BridgeID.setStatus("current")
_Gs2328MSTI7RootID_Type = DisplayString
_Gs2328MSTI7RootID_Object = MibScalar
gs2328MSTI7RootID = _Gs2328MSTI7RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 3),
    _Gs2328MSTI7RootID_Type()
)
gs2328MSTI7RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7RootID.setStatus("current")
_Gs2328MSTI7RootPort_Type = DisplayString
_Gs2328MSTI7RootPort_Object = MibScalar
gs2328MSTI7RootPort = _Gs2328MSTI7RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 4),
    _Gs2328MSTI7RootPort_Type()
)
gs2328MSTI7RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7RootPort.setStatus("current")


class _Gs2328MSTI7RootCost_Type(Integer32):
    """Custom type gs2328MSTI7RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI7RootCost_Type.__name__ = "Integer32"
_Gs2328MSTI7RootCost_Object = MibScalar
gs2328MSTI7RootCost = _Gs2328MSTI7RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 5),
    _Gs2328MSTI7RootCost_Type()
)
gs2328MSTI7RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7RootCost.setStatus("current")
_Gs2328MSTI7TopologyFlag_Type = DisplayString
_Gs2328MSTI7TopologyFlag_Object = MibScalar
gs2328MSTI7TopologyFlag = _Gs2328MSTI7TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 8),
    _Gs2328MSTI7TopologyFlag_Type()
)
gs2328MSTI7TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7TopologyFlag.setStatus("current")
_Gs2328MSTI7TopologyChangeCount_Type = Counter32
_Gs2328MSTI7TopologyChangeCount_Object = MibScalar
gs2328MSTI7TopologyChangeCount = _Gs2328MSTI7TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 9),
    _Gs2328MSTI7TopologyChangeCount_Type()
)
gs2328MSTI7TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7TopologyChangeCount.setStatus("current")
_Gs2328MSTI7TopologyChangeLast_Type = DisplayString
_Gs2328MSTI7TopologyChangeLast_Object = MibScalar
gs2328MSTI7TopologyChangeLast = _Gs2328MSTI7TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 1, 10),
    _Gs2328MSTI7TopologyChangeLast_Type()
)
gs2328MSTI7TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7TopologyChangeLast.setStatus("current")
_Gs2328MSTI7PortStateTable_Object = MibTable
gs2328MSTI7PortStateTable = _Gs2328MSTI7PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2)
)
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateTable.setStatus("current")
_Gs2328MSTI7PortStateEntry_Object = MibTableRow
gs2328MSTI7PortStateEntry = _Gs2328MSTI7PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1)
)
gs2328MSTI7PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328MSTI7PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateEntry.setStatus("current")


class _Gs2328MSTI7PortStateIndex_Type(Integer32):
    """Custom type gs2328MSTI7PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328MSTI7PortStateIndex_Type.__name__ = "Integer32"
_Gs2328MSTI7PortStateIndex_Object = MibTableColumn
gs2328MSTI7PortStateIndex = _Gs2328MSTI7PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 1),
    _Gs2328MSTI7PortStateIndex_Type()
)
gs2328MSTI7PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateIndex.setStatus("current")
_Gs2328MSTI7PortStatePort_Type = DisplayString
_Gs2328MSTI7PortStatePort_Object = MibTableColumn
gs2328MSTI7PortStatePort = _Gs2328MSTI7PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 2),
    _Gs2328MSTI7PortStatePort_Type()
)
gs2328MSTI7PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStatePort.setStatus("current")
_Gs2328MSTI7PortStatePortID_Type = DisplayString
_Gs2328MSTI7PortStatePortID_Object = MibTableColumn
gs2328MSTI7PortStatePortID = _Gs2328MSTI7PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 3),
    _Gs2328MSTI7PortStatePortID_Type()
)
gs2328MSTI7PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStatePortID.setStatus("current")
_Gs2328MSTI7PortStateRole_Type = DisplayString
_Gs2328MSTI7PortStateRole_Object = MibTableColumn
gs2328MSTI7PortStateRole = _Gs2328MSTI7PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 4),
    _Gs2328MSTI7PortStateRole_Type()
)
gs2328MSTI7PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateRole.setStatus("current")
_Gs2328MSTI7PortStateState_Type = DisplayString
_Gs2328MSTI7PortStateState_Object = MibTableColumn
gs2328MSTI7PortStateState = _Gs2328MSTI7PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 5),
    _Gs2328MSTI7PortStateState_Type()
)
gs2328MSTI7PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateState.setStatus("current")


class _Gs2328MSTI7PortStatePathCost_Type(Integer32):
    """Custom type gs2328MSTI7PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328MSTI7PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328MSTI7PortStatePathCost_Object = MibTableColumn
gs2328MSTI7PortStatePathCost = _Gs2328MSTI7PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 6),
    _Gs2328MSTI7PortStatePathCost_Type()
)
gs2328MSTI7PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStatePathCost.setStatus("current")
_Gs2328MSTI7PortStateEdge_Type = DisplayString
_Gs2328MSTI7PortStateEdge_Object = MibTableColumn
gs2328MSTI7PortStateEdge = _Gs2328MSTI7PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 7),
    _Gs2328MSTI7PortStateEdge_Type()
)
gs2328MSTI7PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateEdge.setStatus("current")
_Gs2328MSTI7PortStatePoint2Point_Type = DisplayString
_Gs2328MSTI7PortStatePoint2Point_Object = MibTableColumn
gs2328MSTI7PortStatePoint2Point = _Gs2328MSTI7PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 8),
    _Gs2328MSTI7PortStatePoint2Point_Type()
)
gs2328MSTI7PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStatePoint2Point.setStatus("current")
_Gs2328MSTI7PortStateUptime_Type = DisplayString
_Gs2328MSTI7PortStateUptime_Object = MibTableColumn
gs2328MSTI7PortStateUptime = _Gs2328MSTI7PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 8, 8, 2, 1, 9),
    _Gs2328MSTI7PortStateUptime_Type()
)
gs2328MSTI7PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328MSTI7PortStateUptime.setStatus("current")
_Gs2328STPPortStatusTable_Object = MibTable
gs2328STPPortStatusTable = _Gs2328STPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 9)
)
if mibBuilder.loadTexts:
    gs2328STPPortStatusTable.setStatus("current")
_Gs2328STPPortStatusEntry_Object = MibTableRow
gs2328STPPortStatusEntry = _Gs2328STPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 9, 1)
)
gs2328STPPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPPortStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328STPPortStatusEntry.setStatus("current")


class _Gs2328STPPortStatusPort_Type(Integer32):
    """Custom type gs2328STPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPPortStatusPort_Type.__name__ = "Integer32"
_Gs2328STPPortStatusPort_Object = MibTableColumn
gs2328STPPortStatusPort = _Gs2328STPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 9, 1, 1),
    _Gs2328STPPortStatusPort_Type()
)
gs2328STPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPPortStatusPort.setStatus("current")
_Gs2328STPPortStatusCISTRole_Type = DisplayString
_Gs2328STPPortStatusCISTRole_Object = MibTableColumn
gs2328STPPortStatusCISTRole = _Gs2328STPPortStatusCISTRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 9, 1, 2),
    _Gs2328STPPortStatusCISTRole_Type()
)
gs2328STPPortStatusCISTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPPortStatusCISTRole.setStatus("current")
_Gs2328STPPortStatusCISTState_Type = DisplayString
_Gs2328STPPortStatusCISTState_Object = MibTableColumn
gs2328STPPortStatusCISTState = _Gs2328STPPortStatusCISTState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 9, 1, 3),
    _Gs2328STPPortStatusCISTState_Type()
)
gs2328STPPortStatusCISTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPPortStatusCISTState.setStatus("current")
_Gs2328STPPortStatusUptime_Type = DisplayString
_Gs2328STPPortStatusUptime_Object = MibTableColumn
gs2328STPPortStatusUptime = _Gs2328STPPortStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 9, 1, 4),
    _Gs2328STPPortStatusUptime_Type()
)
gs2328STPPortStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPPortStatusUptime.setStatus("current")
_Gs2328STPPortStatisticsTable_Object = MibTable
gs2328STPPortStatisticsTable = _Gs2328STPPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10)
)
if mibBuilder.loadTexts:
    gs2328STPPortStatisticsTable.setStatus("current")
_Gs2328STPPortStatisticsEntry_Object = MibTableRow
gs2328STPPortStatisticsEntry = _Gs2328STPPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1)
)
gs2328STPPortStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328STPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gs2328STPPortStatisticsEntry.setStatus("current")


class _Gs2328STPStatisticsIndex_Type(Integer32):
    """Custom type gs2328STPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328STPStatisticsIndex_Type.__name__ = "Integer32"
_Gs2328STPStatisticsIndex_Object = MibTableColumn
gs2328STPStatisticsIndex = _Gs2328STPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 1),
    _Gs2328STPStatisticsIndex_Type()
)
gs2328STPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPStatisticsIndex.setStatus("current")
_Gs2328STPStatisticsPort_Type = DisplayString
_Gs2328STPStatisticsPort_Object = MibTableColumn
gs2328STPStatisticsPort = _Gs2328STPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 2),
    _Gs2328STPStatisticsPort_Type()
)
gs2328STPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328STPStatisticsPort.setStatus("current")
_Gs2328STPStatisticsTxMSTP_Type = Counter32
_Gs2328STPStatisticsTxMSTP_Object = MibTableColumn
gs2328STPStatisticsTxMSTP = _Gs2328STPStatisticsTxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 3),
    _Gs2328STPStatisticsTxMSTP_Type()
)
gs2328STPStatisticsTxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsTxMSTP.setStatus("current")
_Gs2328STPStatisticsTxRSTP_Type = Counter32
_Gs2328STPStatisticsTxRSTP_Object = MibTableColumn
gs2328STPStatisticsTxRSTP = _Gs2328STPStatisticsTxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 4),
    _Gs2328STPStatisticsTxRSTP_Type()
)
gs2328STPStatisticsTxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsTxRSTP.setStatus("current")
_Gs2328STPStatisticsTxSTP_Type = Counter32
_Gs2328STPStatisticsTxSTP_Object = MibTableColumn
gs2328STPStatisticsTxSTP = _Gs2328STPStatisticsTxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 5),
    _Gs2328STPStatisticsTxSTP_Type()
)
gs2328STPStatisticsTxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsTxSTP.setStatus("current")
_Gs2328STPStatisticsTxTCN_Type = Counter32
_Gs2328STPStatisticsTxTCN_Object = MibTableColumn
gs2328STPStatisticsTxTCN = _Gs2328STPStatisticsTxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 6),
    _Gs2328STPStatisticsTxTCN_Type()
)
gs2328STPStatisticsTxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsTxTCN.setStatus("current")
_Gs2328STPStatisticsRxMSTP_Type = Counter32
_Gs2328STPStatisticsRxMSTP_Object = MibTableColumn
gs2328STPStatisticsRxMSTP = _Gs2328STPStatisticsRxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 7),
    _Gs2328STPStatisticsRxMSTP_Type()
)
gs2328STPStatisticsRxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsRxMSTP.setStatus("current")
_Gs2328STPStatisticsRxRSTP_Type = Counter32
_Gs2328STPStatisticsRxRSTP_Object = MibTableColumn
gs2328STPStatisticsRxRSTP = _Gs2328STPStatisticsRxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 8),
    _Gs2328STPStatisticsRxRSTP_Type()
)
gs2328STPStatisticsRxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsRxRSTP.setStatus("current")
_Gs2328STPStatisticsRxSTP_Type = Counter32
_Gs2328STPStatisticsRxSTP_Object = MibTableColumn
gs2328STPStatisticsRxSTP = _Gs2328STPStatisticsRxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 9),
    _Gs2328STPStatisticsRxSTP_Type()
)
gs2328STPStatisticsRxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsRxSTP.setStatus("current")
_Gs2328STPStatisticsRxTCN_Type = Counter32
_Gs2328STPStatisticsRxTCN_Object = MibTableColumn
gs2328STPStatisticsRxTCN = _Gs2328STPStatisticsRxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 10),
    _Gs2328STPStatisticsRxTCN_Type()
)
gs2328STPStatisticsRxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsRxTCN.setStatus("current")
_Gs2328STPStatisticsDiscardedUnknown_Type = Counter32
_Gs2328STPStatisticsDiscardedUnknown_Object = MibTableColumn
gs2328STPStatisticsDiscardedUnknown = _Gs2328STPStatisticsDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 11),
    _Gs2328STPStatisticsDiscardedUnknown_Type()
)
gs2328STPStatisticsDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsDiscardedUnknown.setStatus("current")
_Gs2328STPStatisticsDiscardedIllegal_Type = Counter32
_Gs2328STPStatisticsDiscardedIllegal_Object = MibTableColumn
gs2328STPStatisticsDiscardedIllegal = _Gs2328STPStatisticsDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 20, 10, 1, 12),
    _Gs2328STPStatisticsDiscardedIllegal_Type()
)
gs2328STPStatisticsDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328STPStatisticsDiscardedIllegal.setStatus("current")
_Gs2328FilteringDataBase_ObjectIdentity = ObjectIdentity
gs2328FilteringDataBase = _Gs2328FilteringDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21)
)
_Gs2328FilteringDataBaseConfig_ObjectIdentity = ObjectIdentity
gs2328FilteringDataBaseConfig = _Gs2328FilteringDataBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1)
)


class _Gs2328FilteringDataBaseAgingTime_Type(Integer32):
    """Custom type gs2328FilteringDataBaseAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2328FilteringDataBaseAgingTime_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseAgingTime_Object = MibScalar
gs2328FilteringDataBaseAgingTime = _Gs2328FilteringDataBaseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 1),
    _Gs2328FilteringDataBaseAgingTime_Type()
)
gs2328FilteringDataBaseAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseAgingTime.setStatus("current")
_Gs2328FilteringDataBaseConfigTable_Object = MibTable
gs2328FilteringDataBaseConfigTable = _Gs2328FilteringDataBaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseConfigTable.setStatus("current")
_Gs2328FilteringDataBaseConfigEntry_Object = MibTableRow
gs2328FilteringDataBaseConfigEntry = _Gs2328FilteringDataBaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 2, 1)
)
gs2328FilteringDataBaseConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328FilteringDataBaseConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseConfigEntry.setStatus("current")


class _Gs2328FilteringDataBaseConfigPort_Type(Integer32):
    """Custom type gs2328FilteringDataBaseConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328FilteringDataBaseConfigPort_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseConfigPort_Object = MibTableColumn
gs2328FilteringDataBaseConfigPort = _Gs2328FilteringDataBaseConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 2, 1, 1),
    _Gs2328FilteringDataBaseConfigPort_Type()
)
gs2328FilteringDataBaseConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseConfigPort.setStatus("current")


class _Gs2328FilteringDataBaseConfigLearning_Type(Integer32):
    """Custom type gs2328FilteringDataBaseConfigLearning based on Integer32"""
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


_Gs2328FilteringDataBaseConfigLearning_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseConfigLearning_Object = MibTableColumn
gs2328FilteringDataBaseConfigLearning = _Gs2328FilteringDataBaseConfigLearning_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 2, 1, 2),
    _Gs2328FilteringDataBaseConfigLearning_Type()
)
gs2328FilteringDataBaseConfigLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseConfigLearning.setStatus("current")
_Gs2328FilteringDataBaseStaticMAC_ObjectIdentity = ObjectIdentity
gs2328FilteringDataBaseStaticMAC = _Gs2328FilteringDataBaseStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3)
)


class _Gs2328FilteringDataBaseStaticMACCreate_Type(Integer32):
    """Custom type gs2328FilteringDataBaseStaticMACCreate based on Integer32"""
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


_Gs2328FilteringDataBaseStaticMACCreate_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseStaticMACCreate_Object = MibScalar
gs2328FilteringDataBaseStaticMACCreate = _Gs2328FilteringDataBaseStaticMACCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 1),
    _Gs2328FilteringDataBaseStaticMACCreate_Type()
)
gs2328FilteringDataBaseStaticMACCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACCreate.setStatus("current")
_Gs2328FilteringDataBaseStaticMACTable_Object = MibTable
gs2328FilteringDataBaseStaticMACTable = _Gs2328FilteringDataBaseStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACTable.setStatus("current")
_Gs2328FilteringDataBaseStaticMACEntry_Object = MibTableRow
gs2328FilteringDataBaseStaticMACEntry = _Gs2328FilteringDataBaseStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2, 1)
)
gs2328FilteringDataBaseStaticMACEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328FilteringDataBaseStaticMACIndex"),
)
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACEntry.setStatus("current")


class _Gs2328FilteringDataBaseStaticMACIndex_Type(Integer32):
    """Custom type gs2328FilteringDataBaseStaticMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328FilteringDataBaseStaticMACIndex_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseStaticMACIndex_Object = MibTableColumn
gs2328FilteringDataBaseStaticMACIndex = _Gs2328FilteringDataBaseStaticMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2, 1, 1),
    _Gs2328FilteringDataBaseStaticMACIndex_Type()
)
gs2328FilteringDataBaseStaticMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACIndex.setStatus("current")


class _Gs2328FilteringDataBaseStaticMACVLANId_Type(Integer32):
    """Custom type gs2328FilteringDataBaseStaticMACVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328FilteringDataBaseStaticMACVLANId_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseStaticMACVLANId_Object = MibTableColumn
gs2328FilteringDataBaseStaticMACVLANId = _Gs2328FilteringDataBaseStaticMACVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2, 1, 2),
    _Gs2328FilteringDataBaseStaticMACVLANId_Type()
)
gs2328FilteringDataBaseStaticMACVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACVLANId.setStatus("current")
_Gs2328FilteringDataBaseStaticMACAddress_Type = MacAddress
_Gs2328FilteringDataBaseStaticMACAddress_Object = MibTableColumn
gs2328FilteringDataBaseStaticMACAddress = _Gs2328FilteringDataBaseStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2, 1, 3),
    _Gs2328FilteringDataBaseStaticMACAddress_Type()
)
gs2328FilteringDataBaseStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACAddress.setStatus("current")
_Gs2328FilteringDataBaseStaticMACPortMembers_Type = DisplayString
_Gs2328FilteringDataBaseStaticMACPortMembers_Object = MibTableColumn
gs2328FilteringDataBaseStaticMACPortMembers = _Gs2328FilteringDataBaseStaticMACPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2, 1, 4),
    _Gs2328FilteringDataBaseStaticMACPortMembers_Type()
)
gs2328FilteringDataBaseStaticMACPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACPortMembers.setStatus("current")


class _Gs2328FilteringDataBaseStaticMACRowStatus_Type(Integer32):
    """Custom type gs2328FilteringDataBaseStaticMACRowStatus based on Integer32"""
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


_Gs2328FilteringDataBaseStaticMACRowStatus_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseStaticMACRowStatus_Object = MibTableColumn
gs2328FilteringDataBaseStaticMACRowStatus = _Gs2328FilteringDataBaseStaticMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 3, 2, 1, 5),
    _Gs2328FilteringDataBaseStaticMACRowStatus_Type()
)
gs2328FilteringDataBaseStaticMACRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseStaticMACRowStatus.setStatus("current")
_Gs2328FilteringDataBaseDynamicMACTable_Object = MibTable
gs2328FilteringDataBaseDynamicMACTable = _Gs2328FilteringDataBaseDynamicMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicMACTable.setStatus("current")
_Gs2328FilteringDataBaseDynamicMACEntry_Object = MibTableRow
gs2328FilteringDataBaseDynamicMACEntry = _Gs2328FilteringDataBaseDynamicMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4, 1)
)
gs2328FilteringDataBaseDynamicMACEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328FilteringDataBaseDynamicMACIndex"),
)
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicMACEntry.setStatus("current")


class _Gs2328FilteringDataBaseDynamicMACIndex_Type(Integer32):
    """Custom type gs2328FilteringDataBaseDynamicMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328FilteringDataBaseDynamicMACIndex_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseDynamicMACIndex_Object = MibTableColumn
gs2328FilteringDataBaseDynamicMACIndex = _Gs2328FilteringDataBaseDynamicMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4, 1, 1),
    _Gs2328FilteringDataBaseDynamicMACIndex_Type()
)
gs2328FilteringDataBaseDynamicMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicMACIndex.setStatus("current")


class _Gs2328FilteringDataBaseDynamicMACType_Type(Integer32):
    """Custom type gs2328FilteringDataBaseDynamicMACType based on Integer32"""
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


_Gs2328FilteringDataBaseDynamicMACType_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseDynamicMACType_Object = MibTableColumn
gs2328FilteringDataBaseDynamicMACType = _Gs2328FilteringDataBaseDynamicMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4, 1, 2),
    _Gs2328FilteringDataBaseDynamicMACType_Type()
)
gs2328FilteringDataBaseDynamicMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicMACType.setStatus("current")


class _Gs2328FilteringDataBaseDynamicMACVLAN_Type(Integer32):
    """Custom type gs2328FilteringDataBaseDynamicMACVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328FilteringDataBaseDynamicMACVLAN_Type.__name__ = "Integer32"
_Gs2328FilteringDataBaseDynamicMACVLAN_Object = MibTableColumn
gs2328FilteringDataBaseDynamicMACVLAN = _Gs2328FilteringDataBaseDynamicMACVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4, 1, 3),
    _Gs2328FilteringDataBaseDynamicMACVLAN_Type()
)
gs2328FilteringDataBaseDynamicMACVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicMACVLAN.setStatus("current")
_Gs2328FilteringDataBaseDynamicMACAddress_Type = MacAddress
_Gs2328FilteringDataBaseDynamicMACAddress_Object = MibTableColumn
gs2328FilteringDataBaseDynamicMACAddress = _Gs2328FilteringDataBaseDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4, 1, 4),
    _Gs2328FilteringDataBaseDynamicMACAddress_Type()
)
gs2328FilteringDataBaseDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicMACAddress.setStatus("current")
_Gs2328FilteringDataBaseDynamicPortMembers_Type = DisplayString
_Gs2328FilteringDataBaseDynamicPortMembers_Object = MibTableColumn
gs2328FilteringDataBaseDynamicPortMembers = _Gs2328FilteringDataBaseDynamicPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 21, 1, 4, 1, 5),
    _Gs2328FilteringDataBaseDynamicPortMembers_Type()
)
gs2328FilteringDataBaseDynamicPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328FilteringDataBaseDynamicPortMembers.setStatus("current")
_Gs2328SFlowAgent_ObjectIdentity = ObjectIdentity
gs2328SFlowAgent = _Gs2328SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 22)
)
_Gs2328SFlowAgentCollector_ObjectIdentity = ObjectIdentity
gs2328SFlowAgentCollector = _Gs2328SFlowAgentCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 22, 1)
)


class _Gs2328SFlowAgentReceiverMode_Type(Integer32):
    """Custom type gs2328SFlowAgentReceiverMode based on Integer32"""
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


_Gs2328SFlowAgentReceiverMode_Type.__name__ = "Integer32"
_Gs2328SFlowAgentReceiverMode_Object = MibScalar
gs2328SFlowAgentReceiverMode = _Gs2328SFlowAgentReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 22, 1, 1),
    _Gs2328SFlowAgentReceiverMode_Type()
)
gs2328SFlowAgentReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SFlowAgentReceiverMode.setStatus("current")
_Gs2328LMC_ObjectIdentity = ObjectIdentity
gs2328LMC = _Gs2328LMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500)
)


class _Gs2328LMCOperating_Type(Integer32):
    """Custom type gs2328LMCOperating based on Integer32"""
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


_Gs2328LMCOperating_Type.__name__ = "Integer32"
_Gs2328LMCOperating_Object = MibScalar
gs2328LMCOperating = _Gs2328LMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 1),
    _Gs2328LMCOperating_Type()
)
gs2328LMCOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LMCOperating.setStatus("current")


class _Gs2328LMCConfigViaDhcp_Type(Integer32):
    """Custom type gs2328LMCConfigViaDhcp based on Integer32"""
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


_Gs2328LMCConfigViaDhcp_Type.__name__ = "Integer32"
_Gs2328LMCConfigViaDhcp_Object = MibScalar
gs2328LMCConfigViaDhcp = _Gs2328LMCConfigViaDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 2),
    _Gs2328LMCConfigViaDhcp_Type()
)
gs2328LMCConfigViaDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LMCConfigViaDhcp.setStatus("current")


class _Gs2328LMCDomain_Type(DisplayString):
    """Custom type gs2328LMCDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gs2328LMCDomain_Type.__name__ = "DisplayString"
_Gs2328LMCDomain_Object = MibScalar
gs2328LMCDomain = _Gs2328LMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 3),
    _Gs2328LMCDomain_Type()
)
gs2328LMCDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LMCDomain.setStatus("current")


class _Gs2328LMChcpClientAutoRenew_Type(Integer32):
    """Custom type gs2328LMChcpClientAutoRenew based on Integer32"""
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


_Gs2328LMChcpClientAutoRenew_Type.__name__ = "Integer32"
_Gs2328LMChcpClientAutoRenew_Object = MibScalar
gs2328LMChcpClientAutoRenew = _Gs2328LMChcpClientAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 4),
    _Gs2328LMChcpClientAutoRenew_Type()
)
gs2328LMChcpClientAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LMChcpClientAutoRenew.setStatus("current")


class _Gs2328LMCZeroTouchSupport_Type(Integer32):
    """Custom type gs2328LMCZeroTouchSupport based on Integer32"""
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


_Gs2328LMCZeroTouchSupport_Type.__name__ = "Integer32"
_Gs2328LMCZeroTouchSupport_Object = MibScalar
gs2328LMCZeroTouchSupport = _Gs2328LMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 50),
    _Gs2328LMCZeroTouchSupport_Type()
)
gs2328LMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCZeroTouchSupport.setStatus("current")


class _Gs2328LMCPairingTokenPresent_Type(Integer32):
    """Custom type gs2328LMCPairingTokenPresent based on Integer32"""
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


_Gs2328LMCPairingTokenPresent_Type.__name__ = "Integer32"
_Gs2328LMCPairingTokenPresent_Object = MibScalar
gs2328LMCPairingTokenPresent = _Gs2328LMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 51),
    _Gs2328LMCPairingTokenPresent_Type()
)
gs2328LMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCPairingTokenPresent.setStatus("current")
_Gs2328LMCClientStatus_Type = DisplayString
_Gs2328LMCClientStatus_Object = MibScalar
gs2328LMCClientStatus = _Gs2328LMCClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 52),
    _Gs2328LMCClientStatus_Type()
)
gs2328LMCClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCClientStatus.setStatus("current")


class _Gs2328LMCManagementStatus_Type(Integer32):
    """Custom type gs2328LMCManagementStatus based on Integer32"""
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


_Gs2328LMCManagementStatus_Type.__name__ = "Integer32"
_Gs2328LMCManagementStatus_Object = MibScalar
gs2328LMCManagementStatus = _Gs2328LMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 53),
    _Gs2328LMCManagementStatus_Type()
)
gs2328LMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCManagementStatus.setStatus("current")


class _Gs2328LMCControlStatus_Type(Integer32):
    """Custom type gs2328LMCControlStatus based on Integer32"""
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


_Gs2328LMCControlStatus_Type.__name__ = "Integer32"
_Gs2328LMCControlStatus_Object = MibScalar
gs2328LMCControlStatus = _Gs2328LMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 54),
    _Gs2328LMCControlStatus_Type()
)
gs2328LMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCControlStatus.setStatus("current")


class _Gs2328LMCMonitoringStatus_Type(Integer32):
    """Custom type gs2328LMCMonitoringStatus based on Integer32"""
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


_Gs2328LMCMonitoringStatus_Type.__name__ = "Integer32"
_Gs2328LMCMonitoringStatus_Object = MibScalar
gs2328LMCMonitoringStatus = _Gs2328LMCMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 55),
    _Gs2328LMCMonitoringStatus_Type()
)
gs2328LMCMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCMonitoringStatus.setStatus("current")
_Gs2328LMCConfigurationSource_Type = DisplayString
_Gs2328LMCConfigurationSource_Object = MibScalar
gs2328LMCConfigurationSource = _Gs2328LMCConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 56),
    _Gs2328LMCConfigurationSource_Type()
)
gs2328LMCConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCConfigurationSource.setStatus("current")


class _Gs2328LMCConfigModified_Type(Integer32):
    """Custom type gs2328LMCConfigModified based on Integer32"""
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


_Gs2328LMCConfigModified_Type.__name__ = "Integer32"
_Gs2328LMCConfigModified_Object = MibScalar
gs2328LMCConfigModified = _Gs2328LMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 57),
    _Gs2328LMCConfigModified_Type()
)
gs2328LMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCConfigModified.setStatus("current")
_Gs2328LMCDeviceID_Type = DisplayString
_Gs2328LMCDeviceID_Object = MibScalar
gs2328LMCDeviceID = _Gs2328LMCDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 58),
    _Gs2328LMCDeviceID_Type()
)
gs2328LMCDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCDeviceID.setStatus("current")
_Gs2328LMCRoundTripTime_Type = Integer32
_Gs2328LMCRoundTripTime_Object = MibScalar
gs2328LMCRoundTripTime = _Gs2328LMCRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 2, 1500, 100),
    _Gs2328LMCRoundTripTime_Type()
)
gs2328LMCRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328LMCRoundTripTime.setStatus("current")
_Gs2328Security_ObjectIdentity = ObjectIdentity
gs2328Security = _Gs2328Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3)
)
_Gs2328IPSourceGuard_ObjectIdentity = ObjectIdentity
gs2328IPSourceGuard = _Gs2328IPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1)
)
_Gs2328IPSourceGuardConf_ObjectIdentity = ObjectIdentity
gs2328IPSourceGuardConf = _Gs2328IPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1)
)


class _Gs2328IPSourceGuardMode_Type(Integer32):
    """Custom type gs2328IPSourceGuardMode based on Integer32"""
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


_Gs2328IPSourceGuardMode_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardMode_Object = MibScalar
gs2328IPSourceGuardMode = _Gs2328IPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1, 1),
    _Gs2328IPSourceGuardMode_Type()
)
gs2328IPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardMode.setStatus("current")
_Gs2328IPSourceGuardPortConfigTable_Object = MibTable
gs2328IPSourceGuardPortConfigTable = _Gs2328IPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328IPSourceGuardPortConfigTable.setStatus("current")
_Gs2328IPSourceGuardPortConfigEntry_Object = MibTableRow
gs2328IPSourceGuardPortConfigEntry = _Gs2328IPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1, 2, 1)
)
gs2328IPSourceGuardPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328IPSourceGuardPortConfigEntry.setStatus("current")


class _Gs2328IPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type gs2328IPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardPortConfigPort_Object = MibTableColumn
gs2328IPSourceGuardPortConfigPort = _Gs2328IPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1, 2, 1, 1),
    _Gs2328IPSourceGuardPortConfigPort_Type()
)
gs2328IPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardPortConfigPort.setStatus("current")


class _Gs2328IPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type gs2328IPSourceGuardPortConfigMode based on Integer32"""
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


_Gs2328IPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardPortConfigMode_Object = MibTableColumn
gs2328IPSourceGuardPortConfigMode = _Gs2328IPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1, 2, 1, 2),
    _Gs2328IPSourceGuardPortConfigMode_Type()
)
gs2328IPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardPortConfigMode.setStatus("current")


class _Gs2328IPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type gs2328IPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Gs2328IPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
gs2328IPSourceGuardPortMaxDynamicClients = _Gs2328IPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 1, 2, 1, 3),
    _Gs2328IPSourceGuardPortMaxDynamicClients_Type()
)
gs2328IPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardPortMaxDynamicClients.setStatus("current")
_Gs2328IPSourceGuardStatic_ObjectIdentity = ObjectIdentity
gs2328IPSourceGuardStatic = _Gs2328IPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2)
)


class _Gs2328IPSourceGuardStaticCreate_Type(Integer32):
    """Custom type gs2328IPSourceGuardStaticCreate based on Integer32"""
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


_Gs2328IPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardStaticCreate_Object = MibScalar
gs2328IPSourceGuardStaticCreate = _Gs2328IPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 1),
    _Gs2328IPSourceGuardStaticCreate_Type()
)
gs2328IPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticCreate.setStatus("current")
_Gs2328IPSourceGuardStaticTable_Object = MibTable
gs2328IPSourceGuardStaticTable = _Gs2328IPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticTable.setStatus("current")
_Gs2328IPSourceGuardStaticEntry_Object = MibTableRow
gs2328IPSourceGuardStaticEntry = _Gs2328IPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1)
)
gs2328IPSourceGuardStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticEntry.setStatus("current")


class _Gs2328IPSourceGuardStaticIndex_Type(Integer32):
    """Custom type gs2328IPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Gs2328IPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardStaticIndex_Object = MibTableColumn
gs2328IPSourceGuardStaticIndex = _Gs2328IPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1, 1),
    _Gs2328IPSourceGuardStaticIndex_Type()
)
gs2328IPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticIndex.setStatus("current")


class _Gs2328IPSourceGuardStaticPort_Type(Integer32):
    """Custom type gs2328IPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardStaticPort_Object = MibTableColumn
gs2328IPSourceGuardStaticPort = _Gs2328IPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1, 2),
    _Gs2328IPSourceGuardStaticPort_Type()
)
gs2328IPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticPort.setStatus("current")


class _Gs2328IPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type gs2328IPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328IPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardStaticVLANId_Object = MibTableColumn
gs2328IPSourceGuardStaticVLANId = _Gs2328IPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1, 3),
    _Gs2328IPSourceGuardStaticVLANId_Type()
)
gs2328IPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticVLANId.setStatus("current")
_Gs2328IPSourceGuardStaticIPAddress_Type = IpAddress
_Gs2328IPSourceGuardStaticIPAddress_Object = MibTableColumn
gs2328IPSourceGuardStaticIPAddress = _Gs2328IPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1, 4),
    _Gs2328IPSourceGuardStaticIPAddress_Type()
)
gs2328IPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticIPAddress.setStatus("current")
_Gs2328IPSourceGuardStaticMACAddress_Type = MacAddress
_Gs2328IPSourceGuardStaticMACAddress_Object = MibTableColumn
gs2328IPSourceGuardStaticMACAddress = _Gs2328IPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1, 5),
    _Gs2328IPSourceGuardStaticMACAddress_Type()
)
gs2328IPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticMACAddress.setStatus("current")


class _Gs2328IPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type gs2328IPSourceGuardStaticRowStatus based on Integer32"""
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


_Gs2328IPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardStaticRowStatus_Object = MibTableColumn
gs2328IPSourceGuardStaticRowStatus = _Gs2328IPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 2, 2, 1, 6),
    _Gs2328IPSourceGuardStaticRowStatus_Type()
)
gs2328IPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardStaticRowStatus.setStatus("current")
_Gs2328IPSourceGuardDynamicTable_Object = MibTable
gs2328IPSourceGuardDynamicTable = _Gs2328IPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3)
)
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicTable.setStatus("current")
_Gs2328IPSourceGuardDynamicEntry_Object = MibTableRow
gs2328IPSourceGuardDynamicEntry = _Gs2328IPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3, 1)
)
gs2328IPSourceGuardDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328IPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicEntry.setStatus("current")


class _Gs2328IPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type gs2328IPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328IPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardDynamicIndex_Object = MibTableColumn
gs2328IPSourceGuardDynamicIndex = _Gs2328IPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3, 1, 1),
    _Gs2328IPSourceGuardDynamicIndex_Type()
)
gs2328IPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicIndex.setStatus("current")


class _Gs2328IPSourceGuardDynamicPort_Type(Integer32):
    """Custom type gs2328IPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328IPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardDynamicPort_Object = MibTableColumn
gs2328IPSourceGuardDynamicPort = _Gs2328IPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3, 1, 2),
    _Gs2328IPSourceGuardDynamicPort_Type()
)
gs2328IPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicPort.setStatus("current")


class _Gs2328IPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type gs2328IPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328IPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Gs2328IPSourceGuardDynamicVLANId_Object = MibTableColumn
gs2328IPSourceGuardDynamicVLANId = _Gs2328IPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3, 1, 3),
    _Gs2328IPSourceGuardDynamicVLANId_Type()
)
gs2328IPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicVLANId.setStatus("current")
_Gs2328IPSourceGuardDynamicIPAddress_Type = IpAddress
_Gs2328IPSourceGuardDynamicIPAddress_Object = MibTableColumn
gs2328IPSourceGuardDynamicIPAddress = _Gs2328IPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3, 1, 4),
    _Gs2328IPSourceGuardDynamicIPAddress_Type()
)
gs2328IPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicIPAddress.setStatus("current")
_Gs2328IPSourceGuardDynamicMACAddress_Type = MacAddress
_Gs2328IPSourceGuardDynamicMACAddress_Object = MibTableColumn
gs2328IPSourceGuardDynamicMACAddress = _Gs2328IPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 1, 3, 1, 5),
    _Gs2328IPSourceGuardDynamicMACAddress_Type()
)
gs2328IPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328IPSourceGuardDynamicMACAddress.setStatus("current")
_Gs2328ARPInspection_ObjectIdentity = ObjectIdentity
gs2328ARPInspection = _Gs2328ARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2)
)
_Gs2328ARPInspectionConf_ObjectIdentity = ObjectIdentity
gs2328ARPInspectionConf = _Gs2328ARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 1)
)


class _Gs2328ARPInspectionConfMode_Type(Integer32):
    """Custom type gs2328ARPInspectionConfMode based on Integer32"""
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


_Gs2328ARPInspectionConfMode_Type.__name__ = "Integer32"
_Gs2328ARPInspectionConfMode_Object = MibScalar
gs2328ARPInspectionConfMode = _Gs2328ARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 1, 1),
    _Gs2328ARPInspectionConfMode_Type()
)
gs2328ARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionConfMode.setStatus("current")
_Gs2328ARPInspectionConfTable_Object = MibTable
gs2328ARPInspectionConfTable = _Gs2328ARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328ARPInspectionConfTable.setStatus("current")
_Gs2328ARPInspectionConfEntry_Object = MibTableRow
gs2328ARPInspectionConfEntry = _Gs2328ARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 1, 2, 1)
)
gs2328ARPInspectionConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    gs2328ARPInspectionConfEntry.setStatus("current")


class _Gs2328ARPInspectionConfPortIndex_Type(Integer32):
    """Custom type gs2328ARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Gs2328ARPInspectionConfPortIndex_Object = MibTableColumn
gs2328ARPInspectionConfPortIndex = _Gs2328ARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 1, 2, 1, 1),
    _Gs2328ARPInspectionConfPortIndex_Type()
)
gs2328ARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ARPInspectionConfPortIndex.setStatus("current")


class _Gs2328ARPInspectionConfPortMode_Type(Integer32):
    """Custom type gs2328ARPInspectionConfPortMode based on Integer32"""
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


_Gs2328ARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Gs2328ARPInspectionConfPortMode_Object = MibTableColumn
gs2328ARPInspectionConfPortMode = _Gs2328ARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 1, 2, 1, 2),
    _Gs2328ARPInspectionConfPortMode_Type()
)
gs2328ARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionConfPortMode.setStatus("current")
_Gs2328ARPInspectionStatic_ObjectIdentity = ObjectIdentity
gs2328ARPInspectionStatic = _Gs2328ARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2)
)


class _Gs2328ARPInspectionStaticCreate_Type(Integer32):
    """Custom type gs2328ARPInspectionStaticCreate based on Integer32"""
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


_Gs2328ARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Gs2328ARPInspectionStaticCreate_Object = MibScalar
gs2328ARPInspectionStaticCreate = _Gs2328ARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 1),
    _Gs2328ARPInspectionStaticCreate_Type()
)
gs2328ARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticCreate.setStatus("current")
_Gs2328ARPInspectionStaticTable_Object = MibTable
gs2328ARPInspectionStaticTable = _Gs2328ARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticTable.setStatus("current")
_Gs2328ARPInspectionStaticEntry_Object = MibTableRow
gs2328ARPInspectionStaticEntry = _Gs2328ARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1)
)
gs2328ARPInspectionStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticEntry.setStatus("current")


class _Gs2328ARPInspectionStaticIndex_Type(Integer32):
    """Custom type gs2328ARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Gs2328ARPInspectionStaticIndex_Object = MibTableColumn
gs2328ARPInspectionStaticIndex = _Gs2328ARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1, 1),
    _Gs2328ARPInspectionStaticIndex_Type()
)
gs2328ARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticIndex.setStatus("current")


class _Gs2328ARPInspectionStaticPort_Type(Integer32):
    """Custom type gs2328ARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPInspectionStaticPort_Type.__name__ = "Integer32"
_Gs2328ARPInspectionStaticPort_Object = MibTableColumn
gs2328ARPInspectionStaticPort = _Gs2328ARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1, 2),
    _Gs2328ARPInspectionStaticPort_Type()
)
gs2328ARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticPort.setStatus("current")


class _Gs2328ARPInspectionStaticVLANId_Type(Integer32):
    """Custom type gs2328ARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328ARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Gs2328ARPInspectionStaticVLANId_Object = MibTableColumn
gs2328ARPInspectionStaticVLANId = _Gs2328ARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1, 3),
    _Gs2328ARPInspectionStaticVLANId_Type()
)
gs2328ARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticVLANId.setStatus("current")
_Gs2328ARPInspectionStaticIPAddress_Type = IpAddress
_Gs2328ARPInspectionStaticIPAddress_Object = MibTableColumn
gs2328ARPInspectionStaticIPAddress = _Gs2328ARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1, 4),
    _Gs2328ARPInspectionStaticIPAddress_Type()
)
gs2328ARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticIPAddress.setStatus("current")
_Gs2328ARPInspectionStaticMACAddress_Type = MacAddress
_Gs2328ARPInspectionStaticMACAddress_Object = MibTableColumn
gs2328ARPInspectionStaticMACAddress = _Gs2328ARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1, 5),
    _Gs2328ARPInspectionStaticMACAddress_Type()
)
gs2328ARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticMACAddress.setStatus("current")


class _Gs2328ARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type gs2328ARPInspectionStaticRowStatus based on Integer32"""
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


_Gs2328ARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Gs2328ARPInspectionStaticRowStatus_Object = MibTableColumn
gs2328ARPInspectionStaticRowStatus = _Gs2328ARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 2, 2, 1, 6),
    _Gs2328ARPInspectionStaticRowStatus_Type()
)
gs2328ARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPInspectionStaticRowStatus.setStatus("current")
_Gs2328ARPInspectionDynamicTable_Object = MibTable
gs2328ARPInspectionDynamicTable = _Gs2328ARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicTable.setStatus("current")
_Gs2328ARPInspectionDynamicEntry_Object = MibTableRow
gs2328ARPInspectionDynamicEntry = _Gs2328ARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3, 1)
)
gs2328ARPInspectionDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicEntry.setStatus("current")


class _Gs2328ARPInspectionDynamicIndex_Type(Integer32):
    """Custom type gs2328ARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Gs2328ARPInspectionDynamicIndex_Object = MibTableColumn
gs2328ARPInspectionDynamicIndex = _Gs2328ARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3, 1, 1),
    _Gs2328ARPInspectionDynamicIndex_Type()
)
gs2328ARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicIndex.setStatus("current")


class _Gs2328ARPInspectionDynamicPort_Type(Integer32):
    """Custom type gs2328ARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Gs2328ARPInspectionDynamicPort_Object = MibTableColumn
gs2328ARPInspectionDynamicPort = _Gs2328ARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3, 1, 2),
    _Gs2328ARPInspectionDynamicPort_Type()
)
gs2328ARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicPort.setStatus("current")


class _Gs2328ARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type gs2328ARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328ARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Gs2328ARPInspectionDynamicVLANId_Object = MibTableColumn
gs2328ARPInspectionDynamicVLANId = _Gs2328ARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3, 1, 3),
    _Gs2328ARPInspectionDynamicVLANId_Type()
)
gs2328ARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicVLANId.setStatus("current")
_Gs2328ARPInspectionDynamicIPAddress_Type = IpAddress
_Gs2328ARPInspectionDynamicIPAddress_Object = MibTableColumn
gs2328ARPInspectionDynamicIPAddress = _Gs2328ARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3, 1, 4),
    _Gs2328ARPInspectionDynamicIPAddress_Type()
)
gs2328ARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicIPAddress.setStatus("current")
_Gs2328ARPInspectionDynamicMACAddress_Type = MacAddress
_Gs2328ARPInspectionDynamicMACAddress_Object = MibTableColumn
gs2328ARPInspectionDynamicMACAddress = _Gs2328ARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 3, 1, 5),
    _Gs2328ARPInspectionDynamicMACAddress_Type()
)
gs2328ARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ARPInspectionDynamicMACAddress.setStatus("current")
_Gs2328ARPStaticGatewayCtrl_ObjectIdentity = ObjectIdentity
gs2328ARPStaticGatewayCtrl = _Gs2328ARPStaticGatewayCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6)
)
_Gs2328ARPStaticGatewayCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2328ARPStaticGatewayCtrlSystemConf = _Gs2328ARPStaticGatewayCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 1)
)


class _Gs2328ARPStaticGatewayCtrlMode_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlMode based on Integer32"""
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


_Gs2328ARPStaticGatewayCtrlMode_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlMode_Object = MibScalar
gs2328ARPStaticGatewayCtrlMode = _Gs2328ARPStaticGatewayCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 1, 1),
    _Gs2328ARPStaticGatewayCtrlMode_Type()
)
gs2328ARPStaticGatewayCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlMode.setStatus("current")


class _Gs2328ARPStaticGatewayCtrlCreate_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlCreate based on Integer32"""
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


_Gs2328ARPStaticGatewayCtrlCreate_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlCreate_Object = MibScalar
gs2328ARPStaticGatewayCtrlCreate = _Gs2328ARPStaticGatewayCtrlCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 2),
    _Gs2328ARPStaticGatewayCtrlCreate_Type()
)
gs2328ARPStaticGatewayCtrlCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlCreate.setStatus("current")
_Gs2328ARPStaticGatewayCtrlTable_Object = MibTable
gs2328ARPStaticGatewayCtrlTable = _Gs2328ARPStaticGatewayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlTable.setStatus("current")
_Gs2328ARPStaticGatewayCtrlEntry_Object = MibTableRow
gs2328ARPStaticGatewayCtrlEntry = _Gs2328ARPStaticGatewayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1)
)
gs2328ARPStaticGatewayCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ARPStaticGatewayCtrlIndex"),
)
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlEntry.setStatus("current")


class _Gs2328ARPStaticGatewayCtrlIndex_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2328ARPStaticGatewayCtrlIndex_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlIndex_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlIndex = _Gs2328ARPStaticGatewayCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 1),
    _Gs2328ARPStaticGatewayCtrlIndex_Type()
)
gs2328ARPStaticGatewayCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlIndex.setStatus("current")
_Gs2328ARPStaticGatewayCtrlIPAddress_Type = IpAddress
_Gs2328ARPStaticGatewayCtrlIPAddress_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlIPAddress = _Gs2328ARPStaticGatewayCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 2),
    _Gs2328ARPStaticGatewayCtrlIPAddress_Type()
)
gs2328ARPStaticGatewayCtrlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlIPAddress.setStatus("current")
_Gs2328ARPStaticGatewayCtrlMACAddress_Type = MacAddress
_Gs2328ARPStaticGatewayCtrlMACAddress_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlMACAddress = _Gs2328ARPStaticGatewayCtrlMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 3),
    _Gs2328ARPStaticGatewayCtrlMACAddress_Type()
)
gs2328ARPStaticGatewayCtrlMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlMACAddress.setStatus("current")


class _Gs2328ARPStaticGatewayCtrlPort_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPStaticGatewayCtrlPort_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlPort_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlPort = _Gs2328ARPStaticGatewayCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 4),
    _Gs2328ARPStaticGatewayCtrlPort_Type()
)
gs2328ARPStaticGatewayCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlPort.setStatus("current")


class _Gs2328ARPStaticGatewayCtrlAction_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlAction based on Integer32"""
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


_Gs2328ARPStaticGatewayCtrlAction_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlAction_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlAction = _Gs2328ARPStaticGatewayCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 5),
    _Gs2328ARPStaticGatewayCtrlAction_Type()
)
gs2328ARPStaticGatewayCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlAction.setStatus("current")
_Gs2328ARPStaticGatewayCtrlState_Type = DisplayString
_Gs2328ARPStaticGatewayCtrlState_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlState = _Gs2328ARPStaticGatewayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 6),
    _Gs2328ARPStaticGatewayCtrlState_Type()
)
gs2328ARPStaticGatewayCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlState.setStatus("current")


class _Gs2328ARPStaticGatewayCtrlReOpen_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlReOpen based on Integer32"""
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


_Gs2328ARPStaticGatewayCtrlReOpen_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlReOpen_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlReOpen = _Gs2328ARPStaticGatewayCtrlReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 7),
    _Gs2328ARPStaticGatewayCtrlReOpen_Type()
)
gs2328ARPStaticGatewayCtrlReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlReOpen.setStatus("current")


class _Gs2328ARPStaticGatewayCtrlRowStatus_Type(Integer32):
    """Custom type gs2328ARPStaticGatewayCtrlRowStatus based on Integer32"""
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


_Gs2328ARPStaticGatewayCtrlRowStatus_Type.__name__ = "Integer32"
_Gs2328ARPStaticGatewayCtrlRowStatus_Object = MibTableColumn
gs2328ARPStaticGatewayCtrlRowStatus = _Gs2328ARPStaticGatewayCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 6, 3, 1, 8),
    _Gs2328ARPStaticGatewayCtrlRowStatus_Type()
)
gs2328ARPStaticGatewayCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPStaticGatewayCtrlRowStatus.setStatus("current")
_Gs2328ARPSpoofingPrevention_ObjectIdentity = ObjectIdentity
gs2328ARPSpoofingPrevention = _Gs2328ARPSpoofingPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7)
)
_Gs2328ARPSpoofingPreventionSystemConf_ObjectIdentity = ObjectIdentity
gs2328ARPSpoofingPreventionSystemConf = _Gs2328ARPSpoofingPreventionSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 1)
)


class _Gs2328ARPSpoofingPreventionMode_Type(Integer32):
    """Custom type gs2328ARPSpoofingPreventionMode based on Integer32"""
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


_Gs2328ARPSpoofingPreventionMode_Type.__name__ = "Integer32"
_Gs2328ARPSpoofingPreventionMode_Object = MibScalar
gs2328ARPSpoofingPreventionMode = _Gs2328ARPSpoofingPreventionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 1, 1),
    _Gs2328ARPSpoofingPreventionMode_Type()
)
gs2328ARPSpoofingPreventionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionMode.setStatus("current")
_Gs2328ARPSpoofingPreventionTable_Object = MibTable
gs2328ARPSpoofingPreventionTable = _Gs2328ARPSpoofingPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionTable.setStatus("current")
_Gs2328ARPSpoofingPreventionEntry_Object = MibTableRow
gs2328ARPSpoofingPreventionEntry = _Gs2328ARPSpoofingPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1)
)
gs2328ARPSpoofingPreventionEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328ARPSpoofingPreventionPort"),
)
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionEntry.setStatus("current")


class _Gs2328ARPSpoofingPreventionPort_Type(Integer32):
    """Custom type gs2328ARPSpoofingPreventionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328ARPSpoofingPreventionPort_Type.__name__ = "Integer32"
_Gs2328ARPSpoofingPreventionPort_Object = MibTableColumn
gs2328ARPSpoofingPreventionPort = _Gs2328ARPSpoofingPreventionPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1, 1),
    _Gs2328ARPSpoofingPreventionPort_Type()
)
gs2328ARPSpoofingPreventionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionPort.setStatus("current")


class _Gs2328ARPSpoofingPreventionPortMode_Type(Integer32):
    """Custom type gs2328ARPSpoofingPreventionPortMode based on Integer32"""
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


_Gs2328ARPSpoofingPreventionPortMode_Type.__name__ = "Integer32"
_Gs2328ARPSpoofingPreventionPortMode_Object = MibTableColumn
gs2328ARPSpoofingPreventionPortMode = _Gs2328ARPSpoofingPreventionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1, 2),
    _Gs2328ARPSpoofingPreventionPortMode_Type()
)
gs2328ARPSpoofingPreventionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionPortMode.setStatus("current")


class _Gs2328ARPSpoofingPreventionPortLimit_Type(Integer32):
    """Custom type gs2328ARPSpoofingPreventionPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Gs2328ARPSpoofingPreventionPortLimit_Type.__name__ = "Integer32"
_Gs2328ARPSpoofingPreventionPortLimit_Object = MibTableColumn
gs2328ARPSpoofingPreventionPortLimit = _Gs2328ARPSpoofingPreventionPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1, 3),
    _Gs2328ARPSpoofingPreventionPortLimit_Type()
)
gs2328ARPSpoofingPreventionPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionPortLimit.setStatus("current")


class _Gs2328ARPSpoofingPreventionPortAction_Type(Integer32):
    """Custom type gs2328ARPSpoofingPreventionPortAction based on Integer32"""
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


_Gs2328ARPSpoofingPreventionPortAction_Type.__name__ = "Integer32"
_Gs2328ARPSpoofingPreventionPortAction_Object = MibTableColumn
gs2328ARPSpoofingPreventionPortAction = _Gs2328ARPSpoofingPreventionPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1, 4),
    _Gs2328ARPSpoofingPreventionPortAction_Type()
)
gs2328ARPSpoofingPreventionPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionPortAction.setStatus("current")
_Gs2328ARPSpoofingPreventionPortState_Type = DisplayString
_Gs2328ARPSpoofingPreventionPortState_Object = MibTableColumn
gs2328ARPSpoofingPreventionPortState = _Gs2328ARPSpoofingPreventionPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1, 5),
    _Gs2328ARPSpoofingPreventionPortState_Type()
)
gs2328ARPSpoofingPreventionPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionPortState.setStatus("current")


class _Gs2328ARPSpoofingPreventionPortReOpen_Type(Integer32):
    """Custom type gs2328ARPSpoofingPreventionPortReOpen based on Integer32"""
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


_Gs2328ARPSpoofingPreventionPortReOpen_Type.__name__ = "Integer32"
_Gs2328ARPSpoofingPreventionPortReOpen_Object = MibTableColumn
gs2328ARPSpoofingPreventionPortReOpen = _Gs2328ARPSpoofingPreventionPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 7, 2, 1, 6),
    _Gs2328ARPSpoofingPreventionPortReOpen_Type()
)
gs2328ARPSpoofingPreventionPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPSpoofingPreventionPortReOpen.setStatus("current")
_Gs2328ARPIPDoSPrevention_ObjectIdentity = ObjectIdentity
gs2328ARPIPDoSPrevention = _Gs2328ARPIPDoSPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8)
)


class _Gs2328ARPIPDoSPreventionTCPMode_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionTCPMode based on Integer32"""
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


_Gs2328ARPIPDoSPreventionTCPMode_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionTCPMode_Object = MibScalar
gs2328ARPIPDoSPreventionTCPMode = _Gs2328ARPIPDoSPreventionTCPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 1),
    _Gs2328ARPIPDoSPreventionTCPMode_Type()
)
gs2328ARPIPDoSPreventionTCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionTCPMode.setStatus("current")


class _Gs2328ARPIPDoSPreventionUDPMode_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionUDPMode based on Integer32"""
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


_Gs2328ARPIPDoSPreventionUDPMode_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionUDPMode_Object = MibScalar
gs2328ARPIPDoSPreventionUDPMode = _Gs2328ARPIPDoSPreventionUDPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 2),
    _Gs2328ARPIPDoSPreventionUDPMode_Type()
)
gs2328ARPIPDoSPreventionUDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionUDPMode.setStatus("current")


class _Gs2328ARPIPDoSPreventionICMPMode_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionICMPMode based on Integer32"""
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


_Gs2328ARPIPDoSPreventionICMPMode_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionICMPMode_Object = MibScalar
gs2328ARPIPDoSPreventionICMPMode = _Gs2328ARPIPDoSPreventionICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 3),
    _Gs2328ARPIPDoSPreventionICMPMode_Type()
)
gs2328ARPIPDoSPreventionICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionICMPMode.setStatus("current")


class _Gs2328ARPIPDoSPreventionServerPort1_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionServerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328ARPIPDoSPreventionServerPort1_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionServerPort1_Object = MibScalar
gs2328ARPIPDoSPreventionServerPort1 = _Gs2328ARPIPDoSPreventionServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 4),
    _Gs2328ARPIPDoSPreventionServerPort1_Type()
)
gs2328ARPIPDoSPreventionServerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionServerPort1.setStatus("current")


class _Gs2328ARPIPDoSPreventionServerPort2_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionServerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328ARPIPDoSPreventionServerPort2_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionServerPort2_Object = MibScalar
gs2328ARPIPDoSPreventionServerPort2 = _Gs2328ARPIPDoSPreventionServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 5),
    _Gs2328ARPIPDoSPreventionServerPort2_Type()
)
gs2328ARPIPDoSPreventionServerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionServerPort2.setStatus("current")


class _Gs2328ARPIPDoSPreventionServerPort3_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionServerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328ARPIPDoSPreventionServerPort3_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionServerPort3_Object = MibScalar
gs2328ARPIPDoSPreventionServerPort3 = _Gs2328ARPIPDoSPreventionServerPort3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 6),
    _Gs2328ARPIPDoSPreventionServerPort3_Type()
)
gs2328ARPIPDoSPreventionServerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionServerPort3.setStatus("current")


class _Gs2328ARPIPDoSPreventionServerPort4_Type(Integer32):
    """Custom type gs2328ARPIPDoSPreventionServerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328ARPIPDoSPreventionServerPort4_Type.__name__ = "Integer32"
_Gs2328ARPIPDoSPreventionServerPort4_Object = MibScalar
gs2328ARPIPDoSPreventionServerPort4 = _Gs2328ARPIPDoSPreventionServerPort4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 2, 8, 7),
    _Gs2328ARPIPDoSPreventionServerPort4_Type()
)
gs2328ARPIPDoSPreventionServerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ARPIPDoSPreventionServerPort4.setStatus("current")
_Gs2328DHCPSnooping_ObjectIdentity = ObjectIdentity
gs2328DHCPSnooping = _Gs2328DHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3)
)
_Gs2328DHCPSnoopingConf_ObjectIdentity = ObjectIdentity
gs2328DHCPSnoopingConf = _Gs2328DHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 1)
)


class _Gs2328DHCPSnoopingMode_Type(Integer32):
    """Custom type gs2328DHCPSnoopingMode based on Integer32"""
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


_Gs2328DHCPSnoopingMode_Type.__name__ = "Integer32"
_Gs2328DHCPSnoopingMode_Object = MibScalar
gs2328DHCPSnoopingMode = _Gs2328DHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 1, 1),
    _Gs2328DHCPSnoopingMode_Type()
)
gs2328DHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingMode.setStatus("current")
_Gs2328DHCPSnoopingPortModeConfigurationTable_Object = MibTable
gs2328DHCPSnoopingPortModeConfigurationTable = _Gs2328DHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Gs2328DHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
gs2328DHCPSnoopingPortModeConfigurationEntry = _Gs2328DHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 1, 2, 1)
)
gs2328DHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328DHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Gs2328DHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type gs2328DHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328DHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Gs2328DHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
gs2328DHCPSnoopingPortModeConfigurationPort = _Gs2328DHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 1, 2, 1, 1),
    _Gs2328DHCPSnoopingPortModeConfigurationPort_Type()
)
gs2328DHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Gs2328DHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type gs2328DHCPSnoopingPortModeConfigurationMode based on Integer32"""
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


_Gs2328DHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Gs2328DHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
gs2328DHCPSnoopingPortModeConfigurationMode = _Gs2328DHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 1, 2, 1, 2),
    _Gs2328DHCPSnoopingPortModeConfigurationMode_Type()
)
gs2328DHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Gs2328DHCPSnoopingStatisticsTable_Object = MibTable
gs2328DHCPSnoopingStatisticsTable = _Gs2328DHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingStatisticsTable.setStatus("current")
_Gs2328DHCPSnoopingStatisticsEntry_Object = MibTableRow
gs2328DHCPSnoopingStatisticsEntry = _Gs2328DHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1)
)
gs2328DHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328DHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingStatisticsEntry.setStatus("current")


class _Gs2328DHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type gs2328DHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328DHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Gs2328DHCPSnoopingStatisticsPort_Object = MibTableColumn
gs2328DHCPSnoopingStatisticsPort = _Gs2328DHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 1),
    _Gs2328DHCPSnoopingStatisticsPort_Type()
)
gs2328DHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingStatisticsPort.setStatus("current")


class _Gs2328DHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type gs2328DHCPSnoopingStatisticsClear based on Integer32"""
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


_Gs2328DHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Gs2328DHCPSnoopingStatisticsClear_Object = MibTableColumn
gs2328DHCPSnoopingStatisticsClear = _Gs2328DHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 2),
    _Gs2328DHCPSnoopingStatisticsClear_Type()
)
gs2328DHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingStatisticsClear.setStatus("current")
_Gs2328DHCPSnoopingRxDiscover_Type = Counter32
_Gs2328DHCPSnoopingRxDiscover_Object = MibTableColumn
gs2328DHCPSnoopingRxDiscover = _Gs2328DHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 3),
    _Gs2328DHCPSnoopingRxDiscover_Type()
)
gs2328DHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxDiscover.setStatus("current")
_Gs2328DHCPSnoopingRxOffer_Type = Counter32
_Gs2328DHCPSnoopingRxOffer_Object = MibTableColumn
gs2328DHCPSnoopingRxOffer = _Gs2328DHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 4),
    _Gs2328DHCPSnoopingRxOffer_Type()
)
gs2328DHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxOffer.setStatus("current")
_Gs2328DHCPSnoopingRxRequest_Type = Counter32
_Gs2328DHCPSnoopingRxRequest_Object = MibTableColumn
gs2328DHCPSnoopingRxRequest = _Gs2328DHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 5),
    _Gs2328DHCPSnoopingRxRequest_Type()
)
gs2328DHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxRequest.setStatus("current")
_Gs2328DHCPSnoopingRxDecline_Type = Counter32
_Gs2328DHCPSnoopingRxDecline_Object = MibTableColumn
gs2328DHCPSnoopingRxDecline = _Gs2328DHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 6),
    _Gs2328DHCPSnoopingRxDecline_Type()
)
gs2328DHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxDecline.setStatus("current")
_Gs2328DHCPSnoopingRxACK_Type = Counter32
_Gs2328DHCPSnoopingRxACK_Object = MibTableColumn
gs2328DHCPSnoopingRxACK = _Gs2328DHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 7),
    _Gs2328DHCPSnoopingRxACK_Type()
)
gs2328DHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxACK.setStatus("current")
_Gs2328DHCPSnoopingRxNAK_Type = Counter32
_Gs2328DHCPSnoopingRxNAK_Object = MibTableColumn
gs2328DHCPSnoopingRxNAK = _Gs2328DHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 8),
    _Gs2328DHCPSnoopingRxNAK_Type()
)
gs2328DHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxNAK.setStatus("current")
_Gs2328DHCPSnoopingRxRelease_Type = Counter32
_Gs2328DHCPSnoopingRxRelease_Object = MibTableColumn
gs2328DHCPSnoopingRxRelease = _Gs2328DHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 9),
    _Gs2328DHCPSnoopingRxRelease_Type()
)
gs2328DHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxRelease.setStatus("current")
_Gs2328DHCPSnoopingRxInform_Type = Counter32
_Gs2328DHCPSnoopingRxInform_Object = MibTableColumn
gs2328DHCPSnoopingRxInform = _Gs2328DHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 10),
    _Gs2328DHCPSnoopingRxInform_Type()
)
gs2328DHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxInform.setStatus("current")
_Gs2328DHCPSnoopingRxLeaseQuery_Type = Counter32
_Gs2328DHCPSnoopingRxLeaseQuery_Object = MibTableColumn
gs2328DHCPSnoopingRxLeaseQuery = _Gs2328DHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 11),
    _Gs2328DHCPSnoopingRxLeaseQuery_Type()
)
gs2328DHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxLeaseQuery.setStatus("current")
_Gs2328DHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Gs2328DHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
gs2328DHCPSnoopingRxLeaseUnassigned = _Gs2328DHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 12),
    _Gs2328DHCPSnoopingRxLeaseUnassigned_Type()
)
gs2328DHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Gs2328DHCPSnoopingRxLeaseUnknown_Type = Counter32
_Gs2328DHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
gs2328DHCPSnoopingRxLeaseUnknown = _Gs2328DHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 13),
    _Gs2328DHCPSnoopingRxLeaseUnknown_Type()
)
gs2328DHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxLeaseUnknown.setStatus("current")
_Gs2328DHCPSnoopingRxLeaseActive_Type = Counter32
_Gs2328DHCPSnoopingRxLeaseActive_Object = MibTableColumn
gs2328DHCPSnoopingRxLeaseActive = _Gs2328DHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 14),
    _Gs2328DHCPSnoopingRxLeaseActive_Type()
)
gs2328DHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingRxLeaseActive.setStatus("current")
_Gs2328DHCPSnoopingTxDiscover_Type = Counter32
_Gs2328DHCPSnoopingTxDiscover_Object = MibTableColumn
gs2328DHCPSnoopingTxDiscover = _Gs2328DHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 15),
    _Gs2328DHCPSnoopingTxDiscover_Type()
)
gs2328DHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxDiscover.setStatus("current")
_Gs2328DHCPSnoopingTxOffer_Type = Counter32
_Gs2328DHCPSnoopingTxOffer_Object = MibTableColumn
gs2328DHCPSnoopingTxOffer = _Gs2328DHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 16),
    _Gs2328DHCPSnoopingTxOffer_Type()
)
gs2328DHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxOffer.setStatus("current")
_Gs2328DHCPSnoopingTxRequest_Type = Counter32
_Gs2328DHCPSnoopingTxRequest_Object = MibTableColumn
gs2328DHCPSnoopingTxRequest = _Gs2328DHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 17),
    _Gs2328DHCPSnoopingTxRequest_Type()
)
gs2328DHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxRequest.setStatus("current")
_Gs2328DHCPSnoopingTxDecline_Type = Counter32
_Gs2328DHCPSnoopingTxDecline_Object = MibTableColumn
gs2328DHCPSnoopingTxDecline = _Gs2328DHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 18),
    _Gs2328DHCPSnoopingTxDecline_Type()
)
gs2328DHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxDecline.setStatus("current")
_Gs2328DHCPSnoopingTxACK_Type = Counter32
_Gs2328DHCPSnoopingTxACK_Object = MibTableColumn
gs2328DHCPSnoopingTxACK = _Gs2328DHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 19),
    _Gs2328DHCPSnoopingTxACK_Type()
)
gs2328DHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxACK.setStatus("current")
_Gs2328DHCPSnoopingTxNAK_Type = Counter32
_Gs2328DHCPSnoopingTxNAK_Object = MibTableColumn
gs2328DHCPSnoopingTxNAK = _Gs2328DHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 20),
    _Gs2328DHCPSnoopingTxNAK_Type()
)
gs2328DHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxNAK.setStatus("current")
_Gs2328DHCPSnoopingTxRelease_Type = Counter32
_Gs2328DHCPSnoopingTxRelease_Object = MibTableColumn
gs2328DHCPSnoopingTxRelease = _Gs2328DHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 21),
    _Gs2328DHCPSnoopingTxRelease_Type()
)
gs2328DHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxRelease.setStatus("current")
_Gs2328DHCPSnoopingTxInform_Type = Counter32
_Gs2328DHCPSnoopingTxInform_Object = MibTableColumn
gs2328DHCPSnoopingTxInform = _Gs2328DHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 22),
    _Gs2328DHCPSnoopingTxInform_Type()
)
gs2328DHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxInform.setStatus("current")
_Gs2328DHCPSnoopingTxLeaseQuery_Type = Counter32
_Gs2328DHCPSnoopingTxLeaseQuery_Object = MibTableColumn
gs2328DHCPSnoopingTxLeaseQuery = _Gs2328DHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 23),
    _Gs2328DHCPSnoopingTxLeaseQuery_Type()
)
gs2328DHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxLeaseQuery.setStatus("current")
_Gs2328DHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Gs2328DHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
gs2328DHCPSnoopingTxLeaseUnassigned = _Gs2328DHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 24),
    _Gs2328DHCPSnoopingTxLeaseUnassigned_Type()
)
gs2328DHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Gs2328DHCPSnoopingTxLeaseUnknown_Type = Counter32
_Gs2328DHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
gs2328DHCPSnoopingTxLeaseUnknown = _Gs2328DHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 25),
    _Gs2328DHCPSnoopingTxLeaseUnknown_Type()
)
gs2328DHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxLeaseUnknown.setStatus("current")
_Gs2328DHCPSnoopingTxLeaseActive_Type = Counter32
_Gs2328DHCPSnoopingTxLeaseActive_Object = MibTableColumn
gs2328DHCPSnoopingTxLeaseActive = _Gs2328DHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 3, 2, 1, 26),
    _Gs2328DHCPSnoopingTxLeaseActive_Type()
)
gs2328DHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328DHCPSnoopingTxLeaseActive.setStatus("current")
_Gs2328DHCPRelay_ObjectIdentity = ObjectIdentity
gs2328DHCPRelay = _Gs2328DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4)
)
_Gs2328DHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
gs2328DHCPRelayConfiguration = _Gs2328DHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1)
)


class _Gs2328DHCPRelayMode_Type(Integer32):
    """Custom type gs2328DHCPRelayMode based on Integer32"""
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


_Gs2328DHCPRelayMode_Type.__name__ = "Integer32"
_Gs2328DHCPRelayMode_Object = MibScalar
gs2328DHCPRelayMode = _Gs2328DHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 1),
    _Gs2328DHCPRelayMode_Type()
)
gs2328DHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayMode.setStatus("current")
_Gs2328DHCPRelayServer_Type = IpAddress
_Gs2328DHCPRelayServer_Object = MibScalar
gs2328DHCPRelayServer = _Gs2328DHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 2),
    _Gs2328DHCPRelayServer_Type()
)
gs2328DHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayServer.setStatus("current")


class _Gs2328DHCPRelayInformationMode_Type(Integer32):
    """Custom type gs2328DHCPRelayInformationMode based on Integer32"""
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


_Gs2328DHCPRelayInformationMode_Type.__name__ = "Integer32"
_Gs2328DHCPRelayInformationMode_Object = MibScalar
gs2328DHCPRelayInformationMode = _Gs2328DHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 3),
    _Gs2328DHCPRelayInformationMode_Type()
)
gs2328DHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayInformationMode.setStatus("current")


class _Gs2328DHCPRelayInformationPolicy_Type(Integer32):
    """Custom type gs2328DHCPRelayInformationPolicy based on Integer32"""
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


_Gs2328DHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Gs2328DHCPRelayInformationPolicy_Object = MibScalar
gs2328DHCPRelayInformationPolicy = _Gs2328DHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 4),
    _Gs2328DHCPRelayInformationPolicy_Type()
)
gs2328DHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayInformationPolicy.setStatus("current")
_Gs2328DHCPRelayConfigurationGateways_ObjectIdentity = ObjectIdentity
gs2328DHCPRelayConfigurationGateways = _Gs2328DHCPRelayConfigurationGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5)
)


class _Gs2328DHCPRelayConfigurationGatewaysCreate_Type(Integer32):
    """Custom type gs2328DHCPRelayConfigurationGatewaysCreate based on Integer32"""
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


_Gs2328DHCPRelayConfigurationGatewaysCreate_Type.__name__ = "Integer32"
_Gs2328DHCPRelayConfigurationGatewaysCreate_Object = MibScalar
gs2328DHCPRelayConfigurationGatewaysCreate = _Gs2328DHCPRelayConfigurationGatewaysCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 1),
    _Gs2328DHCPRelayConfigurationGatewaysCreate_Type()
)
gs2328DHCPRelayConfigurationGatewaysCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysCreate.setStatus("current")
_Gs2328DHCPRelayConfigurationGatewaysTable_Object = MibTable
gs2328DHCPRelayConfigurationGatewaysTable = _Gs2328DHCPRelayConfigurationGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysTable.setStatus("current")
_Gs2328DHCPRelayConfigurationGatewaysEntry_Object = MibTableRow
gs2328DHCPRelayConfigurationGatewaysEntry = _Gs2328DHCPRelayConfigurationGatewaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 2, 1)
)
gs2328DHCPRelayConfigurationGatewaysEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328DHCPRelayConfigurationGatewaysIndex"),
)
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysEntry.setStatus("current")


class _Gs2328DHCPRelayConfigurationGatewaysIndex_Type(Integer32):
    """Custom type gs2328DHCPRelayConfigurationGatewaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2328DHCPRelayConfigurationGatewaysIndex_Type.__name__ = "Integer32"
_Gs2328DHCPRelayConfigurationGatewaysIndex_Object = MibTableColumn
gs2328DHCPRelayConfigurationGatewaysIndex = _Gs2328DHCPRelayConfigurationGatewaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 2, 1, 1),
    _Gs2328DHCPRelayConfigurationGatewaysIndex_Type()
)
gs2328DHCPRelayConfigurationGatewaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysIndex.setStatus("current")


class _Gs2328DHCPRelayConfigurationGatewaysVLANId_Type(Integer32):
    """Custom type gs2328DHCPRelayConfigurationGatewaysVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328DHCPRelayConfigurationGatewaysVLANId_Type.__name__ = "Integer32"
_Gs2328DHCPRelayConfigurationGatewaysVLANId_Object = MibTableColumn
gs2328DHCPRelayConfigurationGatewaysVLANId = _Gs2328DHCPRelayConfigurationGatewaysVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 2, 1, 2),
    _Gs2328DHCPRelayConfigurationGatewaysVLANId_Type()
)
gs2328DHCPRelayConfigurationGatewaysVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysVLANId.setStatus("current")
_Gs2328DHCPRelayConfigurationGatewaysIP_Type = IpAddress
_Gs2328DHCPRelayConfigurationGatewaysIP_Object = MibTableColumn
gs2328DHCPRelayConfigurationGatewaysIP = _Gs2328DHCPRelayConfigurationGatewaysIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 2, 1, 3),
    _Gs2328DHCPRelayConfigurationGatewaysIP_Type()
)
gs2328DHCPRelayConfigurationGatewaysIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysIP.setStatus("current")


class _Gs2328DHCPRelayConfigurationGatewaysRowStatus_Type(Integer32):
    """Custom type gs2328DHCPRelayConfigurationGatewaysRowStatus based on Integer32"""
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


_Gs2328DHCPRelayConfigurationGatewaysRowStatus_Type.__name__ = "Integer32"
_Gs2328DHCPRelayConfigurationGatewaysRowStatus_Object = MibTableColumn
gs2328DHCPRelayConfigurationGatewaysRowStatus = _Gs2328DHCPRelayConfigurationGatewaysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 5, 2, 1, 4),
    _Gs2328DHCPRelayConfigurationGatewaysRowStatus_Type()
)
gs2328DHCPRelayConfigurationGatewaysRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayConfigurationGatewaysRowStatus.setStatus("current")


class _Gs2328DHCPRelayInformationCustom_Type(DisplayString):
    """Custom type gs2328DHCPRelayInformationCustom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2328DHCPRelayInformationCustom_Type.__name__ = "DisplayString"
_Gs2328DHCPRelayInformationCustom_Object = MibScalar
gs2328DHCPRelayInformationCustom = _Gs2328DHCPRelayInformationCustom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 1, 1500),
    _Gs2328DHCPRelayInformationCustom_Type()
)
gs2328DHCPRelayInformationCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DHCPRelayInformationCustom.setStatus("current")
_Gs2328DHCPRelayStatistics_ObjectIdentity = ObjectIdentity
gs2328DHCPRelayStatistics = _Gs2328DHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2)
)
_Gs2328DHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
gs2328DHCPRelayServerStatistics = _Gs2328DHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1)
)
_Gs2328ServerStatTransmitToServer_Type = Counter32
_Gs2328ServerStatTransmitToServer_Object = MibScalar
gs2328ServerStatTransmitToServer = _Gs2328ServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 1),
    _Gs2328ServerStatTransmitToServer_Type()
)
gs2328ServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatTransmitToServer.setStatus("current")
_Gs2328ServerStatTransmitError_Type = Counter32
_Gs2328ServerStatTransmitError_Object = MibScalar
gs2328ServerStatTransmitError = _Gs2328ServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 2),
    _Gs2328ServerStatTransmitError_Type()
)
gs2328ServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatTransmitError.setStatus("current")
_Gs2328ServerStatReceiveFromServer_Type = Counter32
_Gs2328ServerStatReceiveFromServer_Object = MibScalar
gs2328ServerStatReceiveFromServer = _Gs2328ServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 3),
    _Gs2328ServerStatReceiveFromServer_Type()
)
gs2328ServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatReceiveFromServer.setStatus("current")
_Gs2328ServerStatReceiveMissingAgentOption_Type = Counter32
_Gs2328ServerStatReceiveMissingAgentOption_Object = MibScalar
gs2328ServerStatReceiveMissingAgentOption = _Gs2328ServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 4),
    _Gs2328ServerStatReceiveMissingAgentOption_Type()
)
gs2328ServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatReceiveMissingAgentOption.setStatus("current")
_Gs2328ServerStatReceiveMissingCircuitID_Type = Counter32
_Gs2328ServerStatReceiveMissingCircuitID_Object = MibScalar
gs2328ServerStatReceiveMissingCircuitID = _Gs2328ServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 5),
    _Gs2328ServerStatReceiveMissingCircuitID_Type()
)
gs2328ServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatReceiveMissingCircuitID.setStatus("current")
_Gs2328ServerStatReceiveMissingRemoteID_Type = Counter32
_Gs2328ServerStatReceiveMissingRemoteID_Object = MibScalar
gs2328ServerStatReceiveMissingRemoteID = _Gs2328ServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 6),
    _Gs2328ServerStatReceiveMissingRemoteID_Type()
)
gs2328ServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatReceiveMissingRemoteID.setStatus("current")
_Gs2328ServerStatReceiveBadCircuitID_Type = Counter32
_Gs2328ServerStatReceiveBadCircuitID_Object = MibScalar
gs2328ServerStatReceiveBadCircuitID = _Gs2328ServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 7),
    _Gs2328ServerStatReceiveBadCircuitID_Type()
)
gs2328ServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatReceiveBadCircuitID.setStatus("current")
_Gs2328ServerStatReceiveBadRemoteID_Type = Counter32
_Gs2328ServerStatReceiveBadRemoteID_Object = MibScalar
gs2328ServerStatReceiveBadRemoteID = _Gs2328ServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 1, 8),
    _Gs2328ServerStatReceiveBadRemoteID_Type()
)
gs2328ServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ServerStatReceiveBadRemoteID.setStatus("current")
_Gs2328DHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
gs2328DHCPRelayClientStatistics = _Gs2328DHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2)
)
_Gs2328ClientStatTransmitToClient_Type = Counter32
_Gs2328ClientStatTransmitToClient_Object = MibScalar
gs2328ClientStatTransmitToClient = _Gs2328ClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 1),
    _Gs2328ClientStatTransmitToClient_Type()
)
gs2328ClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatTransmitToClient.setStatus("current")
_Gs2328ClientStatTransmitError_Type = Counter32
_Gs2328ClientStatTransmitError_Object = MibScalar
gs2328ClientStatTransmitError = _Gs2328ClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 2),
    _Gs2328ClientStatTransmitError_Type()
)
gs2328ClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatTransmitError.setStatus("current")
_Gs2328ClientStatReceivefromClient_Type = Counter32
_Gs2328ClientStatReceivefromClient_Object = MibScalar
gs2328ClientStatReceivefromClient = _Gs2328ClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 3),
    _Gs2328ClientStatReceivefromClient_Type()
)
gs2328ClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatReceivefromClient.setStatus("current")
_Gs2328ClientStatReceiveAgentOption_Type = Counter32
_Gs2328ClientStatReceiveAgentOption_Object = MibScalar
gs2328ClientStatReceiveAgentOption = _Gs2328ClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 4),
    _Gs2328ClientStatReceiveAgentOption_Type()
)
gs2328ClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatReceiveAgentOption.setStatus("current")
_Gs2328ClientStatReplaceAgentOption_Type = Counter32
_Gs2328ClientStatReplaceAgentOption_Object = MibScalar
gs2328ClientStatReplaceAgentOption = _Gs2328ClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 5),
    _Gs2328ClientStatReplaceAgentOption_Type()
)
gs2328ClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatReplaceAgentOption.setStatus("current")
_Gs2328ClientStatKeepAgentOption_Type = Counter32
_Gs2328ClientStatKeepAgentOption_Object = MibScalar
gs2328ClientStatKeepAgentOption = _Gs2328ClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 6),
    _Gs2328ClientStatKeepAgentOption_Type()
)
gs2328ClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatKeepAgentOption.setStatus("current")
_Gs2328ClientStatDropAgentOption_Type = Counter32
_Gs2328ClientStatDropAgentOption_Object = MibScalar
gs2328ClientStatDropAgentOption = _Gs2328ClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 4, 2, 2, 7),
    _Gs2328ClientStatDropAgentOption_Type()
)
gs2328ClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328ClientStatDropAgentOption.setStatus("current")
_Gs2328PortSecurity_ObjectIdentity = ObjectIdentity
gs2328PortSecurity = _Gs2328PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5)
)
_Gs2328PortSecLimitCtrl_ObjectIdentity = ObjectIdentity
gs2328PortSecLimitCtrl = _Gs2328PortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1)
)
_Gs2328PortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2328PortSecLimitCtrlSystemConf = _Gs2328PortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 1)
)


class _Gs2328PortSecurityMode_Type(Integer32):
    """Custom type gs2328PortSecurityMode based on Integer32"""
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


_Gs2328PortSecurityMode_Type.__name__ = "Integer32"
_Gs2328PortSecurityMode_Object = MibScalar
gs2328PortSecurityMode = _Gs2328PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 1, 1),
    _Gs2328PortSecurityMode_Type()
)
gs2328PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecurityMode.setStatus("current")


class _Gs2328PortSecurityAging_Type(Integer32):
    """Custom type gs2328PortSecurityAging based on Integer32"""
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


_Gs2328PortSecurityAging_Type.__name__ = "Integer32"
_Gs2328PortSecurityAging_Object = MibScalar
gs2328PortSecurityAging = _Gs2328PortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 1, 2),
    _Gs2328PortSecurityAging_Type()
)
gs2328PortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecurityAging.setStatus("current")


class _Gs2328PortSecurityAgingPeriod_Type(Integer32):
    """Custom type gs2328PortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Gs2328PortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Gs2328PortSecurityAgingPeriod_Object = MibScalar
gs2328PortSecurityAgingPeriod = _Gs2328PortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 1, 3),
    _Gs2328PortSecurityAgingPeriod_Type()
)
gs2328PortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecurityAgingPeriod.setStatus("current")
_Gs2328PortSecLimitCtrlTable_Object = MibTable
gs2328PortSecLimitCtrlTable = _Gs2328PortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlTable.setStatus("current")
_Gs2328PortSecLimitCtrlEntry_Object = MibTableRow
gs2328PortSecLimitCtrlEntry = _Gs2328PortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1)
)
gs2328PortSecLimitCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328PortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlEntry.setStatus("current")


class _Gs2328PortSecLimitCtrlPort_Type(Integer32):
    """Custom type gs2328PortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Gs2328PortSecLimitCtrlPort_Object = MibTableColumn
gs2328PortSecLimitCtrlPort = _Gs2328PortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1, 1),
    _Gs2328PortSecLimitCtrlPort_Type()
)
gs2328PortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlPort.setStatus("current")


class _Gs2328PortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type gs2328PortSecLimitCtrlPortMode based on Integer32"""
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


_Gs2328PortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Gs2328PortSecLimitCtrlPortMode_Object = MibTableColumn
gs2328PortSecLimitCtrlPortMode = _Gs2328PortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1, 2),
    _Gs2328PortSecLimitCtrlPortMode_Type()
)
gs2328PortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlPortMode.setStatus("current")


class _Gs2328PortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type gs2328PortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2328PortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Gs2328PortSecLimitCtrlPortLimit_Object = MibTableColumn
gs2328PortSecLimitCtrlPortLimit = _Gs2328PortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1, 3),
    _Gs2328PortSecLimitCtrlPortLimit_Type()
)
gs2328PortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlPortLimit.setStatus("current")


class _Gs2328PortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type gs2328PortSecLimitCtrlPortAction based on Integer32"""
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


_Gs2328PortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Gs2328PortSecLimitCtrlPortAction_Object = MibTableColumn
gs2328PortSecLimitCtrlPortAction = _Gs2328PortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1, 4),
    _Gs2328PortSecLimitCtrlPortAction_Type()
)
gs2328PortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlPortAction.setStatus("current")
_Gs2328PortSecLimitCtrlPortState_Type = DisplayString
_Gs2328PortSecLimitCtrlPortState_Object = MibTableColumn
gs2328PortSecLimitCtrlPortState = _Gs2328PortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1, 5),
    _Gs2328PortSecLimitCtrlPortState_Type()
)
gs2328PortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlPortState.setStatus("current")


class _Gs2328PortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type gs2328PortSecLimitCtrlPortReOpen based on Integer32"""
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


_Gs2328PortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Gs2328PortSecLimitCtrlPortReOpen_Object = MibTableColumn
gs2328PortSecLimitCtrlPortReOpen = _Gs2328PortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 1, 2, 1, 6),
    _Gs2328PortSecLimitCtrlPortReOpen_Type()
)
gs2328PortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecLimitCtrlPortReOpen.setStatus("current")
_Gs2328PortSecSwitchStatusTable_Object = MibTable
gs2328PortSecSwitchStatusTable = _Gs2328PortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusTable.setStatus("current")
_Gs2328PortSecSwitchStatusEntry_Object = MibTableRow
gs2328PortSecSwitchStatusEntry = _Gs2328PortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2, 1)
)
gs2328PortSecSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328PortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusEntry.setStatus("current")


class _Gs2328PortSecSwitchStatusPort_Type(Integer32):
    """Custom type gs2328PortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Gs2328PortSecSwitchStatusPort_Object = MibTableColumn
gs2328PortSecSwitchStatusPort = _Gs2328PortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2, 1, 1),
    _Gs2328PortSecSwitchStatusPort_Type()
)
gs2328PortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusPort.setStatus("current")
_Gs2328PortSecSwitchStatusUsers_Type = DisplayString
_Gs2328PortSecSwitchStatusUsers_Object = MibTableColumn
gs2328PortSecSwitchStatusUsers = _Gs2328PortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2, 1, 2),
    _Gs2328PortSecSwitchStatusUsers_Type()
)
gs2328PortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusUsers.setStatus("current")
_Gs2328PortSecSwitchStatusState_Type = DisplayString
_Gs2328PortSecSwitchStatusState_Object = MibTableColumn
gs2328PortSecSwitchStatusState = _Gs2328PortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2, 1, 3),
    _Gs2328PortSecSwitchStatusState_Type()
)
gs2328PortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusState.setStatus("current")


class _Gs2328PortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type gs2328PortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Gs2328PortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
gs2328PortSecSwitchStatusMACCountCurrent = _Gs2328PortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2, 1, 4),
    _Gs2328PortSecSwitchStatusMACCountCurrent_Type()
)
gs2328PortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Gs2328PortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type gs2328PortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Gs2328PortSecSwitchStatusMACCountLimit_Object = MibTableColumn
gs2328PortSecSwitchStatusMACCountLimit = _Gs2328PortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 2, 1, 5),
    _Gs2328PortSecSwitchStatusMACCountLimit_Type()
)
gs2328PortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecSwitchStatusMACCountLimit.setStatus("current")
_Gs2328PortSecPortStatus_ObjectIdentity = ObjectIdentity
gs2328PortSecPortStatus = _Gs2328PortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3)
)


class _Gs2328PortSecPortStatusPort_Type(Integer32):
    """Custom type gs2328PortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortSecPortStatusPort_Type.__name__ = "Integer32"
_Gs2328PortSecPortStatusPort_Object = MibScalar
gs2328PortSecPortStatusPort = _Gs2328PortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 1),
    _Gs2328PortSecPortStatusPort_Type()
)
gs2328PortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusPort.setStatus("current")
_Gs2328PortSecPortStatusTable_Object = MibTable
gs2328PortSecPortStatusTable = _Gs2328PortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusTable.setStatus("current")
_Gs2328PortSecPortStatusEntry_Object = MibTableRow
gs2328PortSecPortStatusEntry = _Gs2328PortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1)
)
gs2328PortSecPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328PortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusEntry.setStatus("current")


class _Gs2328PortSecPortStatusIndex_Type(Integer32):
    """Custom type gs2328PortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328PortSecPortStatusIndex_Type.__name__ = "Integer32"
_Gs2328PortSecPortStatusIndex_Object = MibTableColumn
gs2328PortSecPortStatusIndex = _Gs2328PortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1, 1),
    _Gs2328PortSecPortStatusIndex_Type()
)
gs2328PortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusIndex.setStatus("current")
_Gs2328PortSecPortStatusMACAddress_Type = MacAddress
_Gs2328PortSecPortStatusMACAddress_Object = MibTableColumn
gs2328PortSecPortStatusMACAddress = _Gs2328PortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1, 2),
    _Gs2328PortSecPortStatusMACAddress_Type()
)
gs2328PortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusMACAddress.setStatus("current")


class _Gs2328PortSecPortStatusVLANId_Type(Integer32):
    """Custom type gs2328PortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328PortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Gs2328PortSecPortStatusVLANId_Object = MibTableColumn
gs2328PortSecPortStatusVLANId = _Gs2328PortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1, 3),
    _Gs2328PortSecPortStatusVLANId_Type()
)
gs2328PortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusVLANId.setStatus("current")
_Gs2328PortSecPortStatusState_Type = DisplayString
_Gs2328PortSecPortStatusState_Object = MibTableColumn
gs2328PortSecPortStatusState = _Gs2328PortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1, 4),
    _Gs2328PortSecPortStatusState_Type()
)
gs2328PortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusState.setStatus("current")
_Gs2328PortSecPortStatusTimeOfAddition_Type = DisplayString
_Gs2328PortSecPortStatusTimeOfAddition_Object = MibTableColumn
gs2328PortSecPortStatusTimeOfAddition = _Gs2328PortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1, 5),
    _Gs2328PortSecPortStatusTimeOfAddition_Type()
)
gs2328PortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusTimeOfAddition.setStatus("current")
_Gs2328PortSecPortStatusAgeAndHold_Type = DisplayString
_Gs2328PortSecPortStatusAgeAndHold_Object = MibTableColumn
gs2328PortSecPortStatusAgeAndHold = _Gs2328PortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 5, 3, 2, 1, 6),
    _Gs2328PortSecPortStatusAgeAndHold_Type()
)
gs2328PortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PortSecPortStatusAgeAndHold.setStatus("current")
_Gs2328AccessManagement_ObjectIdentity = ObjectIdentity
gs2328AccessManagement = _Gs2328AccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6)
)
_Gs2328AccessMgtConf_ObjectIdentity = ObjectIdentity
gs2328AccessMgtConf = _Gs2328AccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1)
)


class _Gs2328AccessMgtConfMode_Type(Integer32):
    """Custom type gs2328AccessMgtConfMode based on Integer32"""
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


_Gs2328AccessMgtConfMode_Type.__name__ = "Integer32"
_Gs2328AccessMgtConfMode_Object = MibScalar
gs2328AccessMgtConfMode = _Gs2328AccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 1),
    _Gs2328AccessMgtConfMode_Type()
)
gs2328AccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtConfMode.setStatus("current")


class _Gs2328AccessMgtConfCreate_Type(Integer32):
    """Custom type gs2328AccessMgtConfCreate based on Integer32"""
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


_Gs2328AccessMgtConfCreate_Type.__name__ = "Integer32"
_Gs2328AccessMgtConfCreate_Object = MibScalar
gs2328AccessMgtConfCreate = _Gs2328AccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 2),
    _Gs2328AccessMgtConfCreate_Type()
)
gs2328AccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtConfCreate.setStatus("current")
_Gs2328AccessMgtConfTable_Object = MibTable
gs2328AccessMgtConfTable = _Gs2328AccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    gs2328AccessMgtConfTable.setStatus("current")
_Gs2328AccessMgtConfEntry_Object = MibTableRow
gs2328AccessMgtConfEntry = _Gs2328AccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1)
)
gs2328AccessMgtConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328AccessMgtIndex"),
)
if mibBuilder.loadTexts:
    gs2328AccessMgtConfEntry.setStatus("current")


class _Gs2328AccessMgtIndex_Type(Integer32):
    """Custom type gs2328AccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2328AccessMgtIndex_Type.__name__ = "Integer32"
_Gs2328AccessMgtIndex_Object = MibTableColumn
gs2328AccessMgtIndex = _Gs2328AccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 1),
    _Gs2328AccessMgtIndex_Type()
)
gs2328AccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtIndex.setStatus("current")


class _Gs2328AccessMgtAddresstype_Type(Integer32):
    """Custom type gs2328AccessMgtAddresstype based on Integer32"""
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


_Gs2328AccessMgtAddresstype_Type.__name__ = "Integer32"
_Gs2328AccessMgtAddresstype_Object = MibTableColumn
gs2328AccessMgtAddresstype = _Gs2328AccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 2),
    _Gs2328AccessMgtAddresstype_Type()
)
gs2328AccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtAddresstype.setStatus("current")
_Gs2328AccessMgtStartIpAddress_Type = DisplayString
_Gs2328AccessMgtStartIpAddress_Object = MibTableColumn
gs2328AccessMgtStartIpAddress = _Gs2328AccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 3),
    _Gs2328AccessMgtStartIpAddress_Type()
)
gs2328AccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtStartIpAddress.setStatus("current")
_Gs2328AccessMgtEndIpAddress_Type = DisplayString
_Gs2328AccessMgtEndIpAddress_Object = MibTableColumn
gs2328AccessMgtEndIpAddress = _Gs2328AccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 4),
    _Gs2328AccessMgtEndIpAddress_Type()
)
gs2328AccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtEndIpAddress.setStatus("current")


class _Gs2328AccessMgtHttpHttps_Type(Integer32):
    """Custom type gs2328AccessMgtHttpHttps based on Integer32"""
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


_Gs2328AccessMgtHttpHttps_Type.__name__ = "Integer32"
_Gs2328AccessMgtHttpHttps_Object = MibTableColumn
gs2328AccessMgtHttpHttps = _Gs2328AccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 5),
    _Gs2328AccessMgtHttpHttps_Type()
)
gs2328AccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtHttpHttps.setStatus("current")


class _Gs2328AccessMgtSNMP_Type(Integer32):
    """Custom type gs2328AccessMgtSNMP based on Integer32"""
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


_Gs2328AccessMgtSNMP_Type.__name__ = "Integer32"
_Gs2328AccessMgtSNMP_Object = MibTableColumn
gs2328AccessMgtSNMP = _Gs2328AccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 6),
    _Gs2328AccessMgtSNMP_Type()
)
gs2328AccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtSNMP.setStatus("current")


class _Gs2328AccessMgtTelnetSSH_Type(Integer32):
    """Custom type gs2328AccessMgtTelnetSSH based on Integer32"""
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


_Gs2328AccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Gs2328AccessMgtTelnetSSH_Object = MibTableColumn
gs2328AccessMgtTelnetSSH = _Gs2328AccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 7),
    _Gs2328AccessMgtTelnetSSH_Type()
)
gs2328AccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtTelnetSSH.setStatus("current")


class _Gs2328AccessMgtRowStatus_Type(Integer32):
    """Custom type gs2328AccessMgtRowStatus based on Integer32"""
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


_Gs2328AccessMgtRowStatus_Type.__name__ = "Integer32"
_Gs2328AccessMgtRowStatus_Object = MibTableColumn
gs2328AccessMgtRowStatus = _Gs2328AccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 1, 3, 1, 8),
    _Gs2328AccessMgtRowStatus_Type()
)
gs2328AccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtRowStatus.setStatus("current")
_Gs2328AccessMgtStatistics_ObjectIdentity = ObjectIdentity
gs2328AccessMgtStatistics = _Gs2328AccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2)
)
_Gs2328HttpReceivedPkts_Type = Counter32
_Gs2328HttpReceivedPkts_Object = MibScalar
gs2328HttpReceivedPkts = _Gs2328HttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 1),
    _Gs2328HttpReceivedPkts_Type()
)
gs2328HttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HttpReceivedPkts.setStatus("current")
_Gs2328HttpAllowedPkts_Type = Counter32
_Gs2328HttpAllowedPkts_Object = MibScalar
gs2328HttpAllowedPkts = _Gs2328HttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 2),
    _Gs2328HttpAllowedPkts_Type()
)
gs2328HttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HttpAllowedPkts.setStatus("current")
_Gs2328HttpDiscardedPkts_Type = Counter32
_Gs2328HttpDiscardedPkts_Object = MibScalar
gs2328HttpDiscardedPkts = _Gs2328HttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 3),
    _Gs2328HttpDiscardedPkts_Type()
)
gs2328HttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HttpDiscardedPkts.setStatus("current")
_Gs2328HttpsReceivedPkts_Type = Counter32
_Gs2328HttpsReceivedPkts_Object = MibScalar
gs2328HttpsReceivedPkts = _Gs2328HttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 4),
    _Gs2328HttpsReceivedPkts_Type()
)
gs2328HttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HttpsReceivedPkts.setStatus("current")
_Gs2328HttpsAllowedPkts_Type = Counter32
_Gs2328HttpsAllowedPkts_Object = MibScalar
gs2328HttpsAllowedPkts = _Gs2328HttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 5),
    _Gs2328HttpsAllowedPkts_Type()
)
gs2328HttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HttpsAllowedPkts.setStatus("current")
_Gs2328HttpsDiscardedPkts_Type = Counter32
_Gs2328HttpsDiscardedPkts_Object = MibScalar
gs2328HttpsDiscardedPkts = _Gs2328HttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 6),
    _Gs2328HttpsDiscardedPkts_Type()
)
gs2328HttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328HttpsDiscardedPkts.setStatus("current")
_Gs2328SnmpReceivedPkts_Type = Counter32
_Gs2328SnmpReceivedPkts_Object = MibScalar
gs2328SnmpReceivedPkts = _Gs2328SnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 7),
    _Gs2328SnmpReceivedPkts_Type()
)
gs2328SnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SnmpReceivedPkts.setStatus("current")
_Gs2328SnmpAllowedPkts_Type = Counter32
_Gs2328SnmpAllowedPkts_Object = MibScalar
gs2328SnmpAllowedPkts = _Gs2328SnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 8),
    _Gs2328SnmpAllowedPkts_Type()
)
gs2328SnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SnmpAllowedPkts.setStatus("current")
_Gs2328SnmpDiscardedPkts_Type = Counter32
_Gs2328SnmpDiscardedPkts_Object = MibScalar
gs2328SnmpDiscardedPkts = _Gs2328SnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 9),
    _Gs2328SnmpDiscardedPkts_Type()
)
gs2328SnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SnmpDiscardedPkts.setStatus("current")
_Gs2328TelnetReceivedPkts_Type = Counter32
_Gs2328TelnetReceivedPkts_Object = MibScalar
gs2328TelnetReceivedPkts = _Gs2328TelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 10),
    _Gs2328TelnetReceivedPkts_Type()
)
gs2328TelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328TelnetReceivedPkts.setStatus("current")
_Gs2328TelnetAllowedPkts_Type = Counter32
_Gs2328TelnetAllowedPkts_Object = MibScalar
gs2328TelnetAllowedPkts = _Gs2328TelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 11),
    _Gs2328TelnetAllowedPkts_Type()
)
gs2328TelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328TelnetAllowedPkts.setStatus("current")
_Gs2328TelnetDiscardedPkts_Type = Counter32
_Gs2328TelnetDiscardedPkts_Object = MibScalar
gs2328TelnetDiscardedPkts = _Gs2328TelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 12),
    _Gs2328TelnetDiscardedPkts_Type()
)
gs2328TelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328TelnetDiscardedPkts.setStatus("current")
_Gs2328SSHReceivedPkts_Type = Counter32
_Gs2328SSHReceivedPkts_Object = MibScalar
gs2328SSHReceivedPkts = _Gs2328SSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 13),
    _Gs2328SSHReceivedPkts_Type()
)
gs2328SSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SSHReceivedPkts.setStatus("current")
_Gs2328SSHAllowedPkts_Type = Counter32
_Gs2328SSHAllowedPkts_Object = MibScalar
gs2328SSHAllowedPkts = _Gs2328SSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 14),
    _Gs2328SSHAllowedPkts_Type()
)
gs2328SSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SSHAllowedPkts.setStatus("current")
_Gs2328SSHDiscardedPkts_Type = Counter32
_Gs2328SSHDiscardedPkts_Object = MibScalar
gs2328SSHDiscardedPkts = _Gs2328SSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 15),
    _Gs2328SSHDiscardedPkts_Type()
)
gs2328SSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328SSHDiscardedPkts.setStatus("current")


class _Gs2328AccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type gs2328AccessMgtStatisticsClearAll based on Integer32"""
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


_Gs2328AccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Gs2328AccessMgtStatisticsClearAll_Object = MibScalar
gs2328AccessMgtStatisticsClearAll = _Gs2328AccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 6, 2, 16),
    _Gs2328AccessMgtStatisticsClearAll_Type()
)
gs2328AccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AccessMgtStatisticsClearAll.setStatus("current")
_Gs2328SSH_ObjectIdentity = ObjectIdentity
gs2328SSH = _Gs2328SSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 7)
)


class _Gs2328SSHMode_Type(Integer32):
    """Custom type gs2328SSHMode based on Integer32"""
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


_Gs2328SSHMode_Type.__name__ = "Integer32"
_Gs2328SSHMode_Object = MibScalar
gs2328SSHMode = _Gs2328SSHMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 7, 1),
    _Gs2328SSHMode_Type()
)
gs2328SSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SSHMode.setStatus("current")
_Gs2328HTTPS_ObjectIdentity = ObjectIdentity
gs2328HTTPS = _Gs2328HTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 8)
)


class _Gs2328HTTPSMode_Type(Integer32):
    """Custom type gs2328HTTPSMode based on Integer32"""
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


_Gs2328HTTPSMode_Type.__name__ = "Integer32"
_Gs2328HTTPSMode_Object = MibScalar
gs2328HTTPSMode = _Gs2328HTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 8, 1),
    _Gs2328HTTPSMode_Type()
)
gs2328HTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HTTPSMode.setStatus("current")


class _Gs2328HTTPSAutoRedirect_Type(Integer32):
    """Custom type gs2328HTTPSAutoRedirect based on Integer32"""
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


_Gs2328HTTPSAutoRedirect_Type.__name__ = "Integer32"
_Gs2328HTTPSAutoRedirect_Object = MibScalar
gs2328HTTPSAutoRedirect = _Gs2328HTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 8, 2),
    _Gs2328HTTPSAutoRedirect_Type()
)
gs2328HTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HTTPSAutoRedirect.setStatus("current")


class _Gs2328HTTPSCertRenew_Type(Integer32):
    """Custom type gs2328HTTPSCertRenew based on Integer32"""
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


_Gs2328HTTPSCertRenew_Type.__name__ = "Integer32"
_Gs2328HTTPSCertRenew_Object = MibScalar
gs2328HTTPSCertRenew = _Gs2328HTTPSCertRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 8, 3),
    _Gs2328HTTPSCertRenew_Type()
)
gs2328HTTPSCertRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HTTPSCertRenew.setStatus("current")


class _Gs2328HTTPSMinProtoVersion_Type(Integer32):
    """Custom type gs2328HTTPSMinProtoVersion based on Integer32"""
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


_Gs2328HTTPSMinProtoVersion_Type.__name__ = "Integer32"
_Gs2328HTTPSMinProtoVersion_Object = MibScalar
gs2328HTTPSMinProtoVersion = _Gs2328HTTPSMinProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 8, 4),
    _Gs2328HTTPSMinProtoVersion_Type()
)
gs2328HTTPSMinProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HTTPSMinProtoVersion.setStatus("current")


class _Gs2328HTTPMode_Type(Integer32):
    """Custom type gs2328HTTPMode based on Integer32"""
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


_Gs2328HTTPMode_Type.__name__ = "Integer32"
_Gs2328HTTPMode_Object = MibScalar
gs2328HTTPMode = _Gs2328HTTPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 8, 5),
    _Gs2328HTTPMode_Type()
)
gs2328HTTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HTTPMode.setStatus("current")
_Gs2328AuthMethod_ObjectIdentity = ObjectIdentity
gs2328AuthMethod = _Gs2328AuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9)
)


class _Gs2328ConsoleAuthMethod_Type(Integer32):
    """Custom type gs2328ConsoleAuthMethod based on Integer32"""
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


_Gs2328ConsoleAuthMethod_Type.__name__ = "Integer32"
_Gs2328ConsoleAuthMethod_Object = MibScalar
gs2328ConsoleAuthMethod = _Gs2328ConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 1),
    _Gs2328ConsoleAuthMethod_Type()
)
gs2328ConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ConsoleAuthMethod.setStatus("current")


class _Gs2328ConsoleFallback_Type(Integer32):
    """Custom type gs2328ConsoleFallback based on Integer32"""
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


_Gs2328ConsoleFallback_Type.__name__ = "Integer32"
_Gs2328ConsoleFallback_Object = MibScalar
gs2328ConsoleFallback = _Gs2328ConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 2),
    _Gs2328ConsoleFallback_Type()
)
gs2328ConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ConsoleFallback.setStatus("current")


class _Gs2328TelnetAuthMethod_Type(Integer32):
    """Custom type gs2328TelnetAuthMethod based on Integer32"""
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


_Gs2328TelnetAuthMethod_Type.__name__ = "Integer32"
_Gs2328TelnetAuthMethod_Object = MibScalar
gs2328TelnetAuthMethod = _Gs2328TelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 3),
    _Gs2328TelnetAuthMethod_Type()
)
gs2328TelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TelnetAuthMethod.setStatus("current")


class _Gs2328TelnetFallback_Type(Integer32):
    """Custom type gs2328TelnetFallback based on Integer32"""
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


_Gs2328TelnetFallback_Type.__name__ = "Integer32"
_Gs2328TelnetFallback_Object = MibScalar
gs2328TelnetFallback = _Gs2328TelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 4),
    _Gs2328TelnetFallback_Type()
)
gs2328TelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TelnetFallback.setStatus("current")


class _Gs2328SshAuthMethod_Type(Integer32):
    """Custom type gs2328SshAuthMethod based on Integer32"""
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


_Gs2328SshAuthMethod_Type.__name__ = "Integer32"
_Gs2328SshAuthMethod_Object = MibScalar
gs2328SshAuthMethod = _Gs2328SshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 5),
    _Gs2328SshAuthMethod_Type()
)
gs2328SshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SshAuthMethod.setStatus("current")


class _Gs2328SshFallback_Type(Integer32):
    """Custom type gs2328SshFallback based on Integer32"""
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


_Gs2328SshFallback_Type.__name__ = "Integer32"
_Gs2328SshFallback_Object = MibScalar
gs2328SshFallback = _Gs2328SshFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 6),
    _Gs2328SshFallback_Type()
)
gs2328SshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SshFallback.setStatus("current")


class _Gs2328TftpAuthMethod_Type(Integer32):
    """Custom type gs2328TftpAuthMethod based on Integer32"""
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


_Gs2328TftpAuthMethod_Type.__name__ = "Integer32"
_Gs2328TftpAuthMethod_Object = MibScalar
gs2328TftpAuthMethod = _Gs2328TftpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 9),
    _Gs2328TftpAuthMethod_Type()
)
gs2328TftpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TftpAuthMethod.setStatus("current")


class _Gs2328TftpFallback_Type(Integer32):
    """Custom type gs2328TftpFallback based on Integer32"""
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


_Gs2328TftpFallback_Type.__name__ = "Integer32"
_Gs2328TftpFallback_Object = MibScalar
gs2328TftpFallback = _Gs2328TftpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 10),
    _Gs2328TftpFallback_Type()
)
gs2328TftpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TftpFallback.setStatus("current")


class _Gs2328LoginFailures_Type(Integer32):
    """Custom type gs2328LoginFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Gs2328LoginFailures_Type.__name__ = "Integer32"
_Gs2328LoginFailures_Object = MibScalar
gs2328LoginFailures = _Gs2328LoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 11),
    _Gs2328LoginFailures_Type()
)
gs2328LoginFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LoginFailures.setStatus("current")


class _Gs2328LockMinutes_Type(Integer32):
    """Custom type gs2328LockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Gs2328LockMinutes_Type.__name__ = "Integer32"
_Gs2328LockMinutes_Object = MibScalar
gs2328LockMinutes = _Gs2328LockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 12),
    _Gs2328LockMinutes_Type()
)
gs2328LockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328LockMinutes.setStatus("current")


class _Gs2328HttpAuthMethod_Type(Integer32):
    """Custom type gs2328HttpAuthMethod based on Integer32"""
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


_Gs2328HttpAuthMethod_Type.__name__ = "Integer32"
_Gs2328HttpAuthMethod_Object = MibScalar
gs2328HttpAuthMethod = _Gs2328HttpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 13),
    _Gs2328HttpAuthMethod_Type()
)
gs2328HttpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HttpAuthMethod.setStatus("current")


class _Gs2328HttpFallback_Type(Integer32):
    """Custom type gs2328HttpFallback based on Integer32"""
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


_Gs2328HttpFallback_Type.__name__ = "Integer32"
_Gs2328HttpFallback_Object = MibScalar
gs2328HttpFallback = _Gs2328HttpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 14),
    _Gs2328HttpFallback_Type()
)
gs2328HttpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HttpFallback.setStatus("current")


class _Gs2328HttpsAuthMethod_Type(Integer32):
    """Custom type gs2328HttpsAuthMethod based on Integer32"""
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


_Gs2328HttpsAuthMethod_Type.__name__ = "Integer32"
_Gs2328HttpsAuthMethod_Object = MibScalar
gs2328HttpsAuthMethod = _Gs2328HttpsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 15),
    _Gs2328HttpsAuthMethod_Type()
)
gs2328HttpsAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HttpsAuthMethod.setStatus("current")


class _Gs2328HttpsFallback_Type(Integer32):
    """Custom type gs2328HttpsFallback based on Integer32"""
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


_Gs2328HttpsFallback_Type.__name__ = "Integer32"
_Gs2328HttpsFallback_Object = MibScalar
gs2328HttpsFallback = _Gs2328HttpsFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 9, 16),
    _Gs2328HttpsFallback_Type()
)
gs2328HttpsFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328HttpsFallback.setStatus("current")
_Gs2328AAA_ObjectIdentity = ObjectIdentity
gs2328AAA = _Gs2328AAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10)
)
_Gs2328AAACommonServer_ObjectIdentity = ObjectIdentity
gs2328AAACommonServer = _Gs2328AAACommonServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 1)
)


class _Gs2328AAACommonServerTimeout_Type(Integer32):
    """Custom type gs2328AAACommonServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_Gs2328AAACommonServerTimeout_Type.__name__ = "Integer32"
_Gs2328AAACommonServerTimeout_Object = MibScalar
gs2328AAACommonServerTimeout = _Gs2328AAACommonServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 1, 1),
    _Gs2328AAACommonServerTimeout_Type()
)
gs2328AAACommonServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AAACommonServerTimeout.setStatus("current")


class _Gs2328AAACommonServerDeadTime_Type(Integer32):
    """Custom type gs2328AAACommonServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Gs2328AAACommonServerDeadTime_Type.__name__ = "Integer32"
_Gs2328AAACommonServerDeadTime_Object = MibScalar
gs2328AAACommonServerDeadTime = _Gs2328AAACommonServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 1, 2),
    _Gs2328AAACommonServerDeadTime_Type()
)
gs2328AAACommonServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AAACommonServerDeadTime.setStatus("current")
_Gs2328AAATACACSPlusAuthAndAccounting_ObjectIdentity = ObjectIdentity
gs2328AAATACACSPlusAuthAndAccounting = _Gs2328AAATACACSPlusAuthAndAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 2)
)


class _Gs2328AAAAuthorization_Type(Integer32):
    """Custom type gs2328AAAAuthorization based on Integer32"""
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


_Gs2328AAAAuthorization_Type.__name__ = "Integer32"
_Gs2328AAAAuthorization_Object = MibScalar
gs2328AAAAuthorization = _Gs2328AAAAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 2, 1),
    _Gs2328AAAAuthorization_Type()
)
gs2328AAAAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AAAAuthorization.setStatus("current")


class _Gs2328AAAFallbackToLocalAuthorization_Type(Integer32):
    """Custom type gs2328AAAFallbackToLocalAuthorization based on Integer32"""
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


_Gs2328AAAFallbackToLocalAuthorization_Type.__name__ = "Integer32"
_Gs2328AAAFallbackToLocalAuthorization_Object = MibScalar
gs2328AAAFallbackToLocalAuthorization = _Gs2328AAAFallbackToLocalAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 2, 2),
    _Gs2328AAAFallbackToLocalAuthorization_Type()
)
gs2328AAAFallbackToLocalAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AAAFallbackToLocalAuthorization.setStatus("current")


class _Gs2328AAAAccounting_Type(Integer32):
    """Custom type gs2328AAAAccounting based on Integer32"""
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


_Gs2328AAAAccounting_Type.__name__ = "Integer32"
_Gs2328AAAAccounting_Object = MibScalar
gs2328AAAAccounting = _Gs2328AAAAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 2, 3),
    _Gs2328AAAAccounting_Type()
)
gs2328AAAAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328AAAAccounting.setStatus("current")
_Gs2328RADIUSAuthenticationServerTable_Object = MibTable
gs2328RADIUSAuthenticationServerTable = _Gs2328RADIUSAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3)
)
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerTable.setStatus("current")
_Gs2328RADIUSAuthenticationServerEntry_Object = MibTableRow
gs2328RADIUSAuthenticationServerEntry = _Gs2328RADIUSAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3, 1)
)
gs2328RADIUSAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328RADIUSAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerEntry.setStatus("current")


class _Gs2328RADIUSAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2328RADIUSAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328RADIUSAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2328RADIUSAuthenticationServerIndex_Object = MibTableColumn
gs2328RADIUSAuthenticationServerIndex = _Gs2328RADIUSAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3, 1, 1),
    _Gs2328RADIUSAuthenticationServerIndex_Type()
)
gs2328RADIUSAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerIndex.setStatus("current")


class _Gs2328RADIUSAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2328RADIUSAuthenticationServerEnable based on Integer32"""
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


_Gs2328RADIUSAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2328RADIUSAuthenticationServerEnable_Object = MibTableColumn
gs2328RADIUSAuthenticationServerEnable = _Gs2328RADIUSAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3, 1, 2),
    _Gs2328RADIUSAuthenticationServerEnable_Type()
)
gs2328RADIUSAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerEnable.setStatus("current")
_Gs2328RADIUSAuthenticationServerIP_Type = DisplayString
_Gs2328RADIUSAuthenticationServerIP_Object = MibTableColumn
gs2328RADIUSAuthenticationServerIP = _Gs2328RADIUSAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3, 1, 3),
    _Gs2328RADIUSAuthenticationServerIP_Type()
)
gs2328RADIUSAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerIP.setStatus("current")


class _Gs2328RADIUSAuthenticationServerPort_Type(Integer32):
    """Custom type gs2328RADIUSAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328RADIUSAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2328RADIUSAuthenticationServerPort_Object = MibTableColumn
gs2328RADIUSAuthenticationServerPort = _Gs2328RADIUSAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3, 1, 4),
    _Gs2328RADIUSAuthenticationServerPort_Type()
)
gs2328RADIUSAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerPort.setStatus("current")
_Gs2328RADIUSAuthenticationServerSecret_Type = DisplayString
_Gs2328RADIUSAuthenticationServerSecret_Object = MibTableColumn
gs2328RADIUSAuthenticationServerSecret = _Gs2328RADIUSAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 3, 1, 5),
    _Gs2328RADIUSAuthenticationServerSecret_Type()
)
gs2328RADIUSAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthenticationServerSecret.setStatus("current")
_Gs2328RADIUSAccountingServerTable_Object = MibTable
gs2328RADIUSAccountingServerTable = _Gs2328RADIUSAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4)
)
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerTable.setStatus("current")
_Gs2328RADIUSAccountingServerEntry_Object = MibTableRow
gs2328RADIUSAccountingServerEntry = _Gs2328RADIUSAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4, 1)
)
gs2328RADIUSAccountingServerEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328RADIUSAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerEntry.setStatus("current")


class _Gs2328RADIUSAccountingServerIndex_Type(Integer32):
    """Custom type gs2328RADIUSAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328RADIUSAccountingServerIndex_Type.__name__ = "Integer32"
_Gs2328RADIUSAccountingServerIndex_Object = MibTableColumn
gs2328RADIUSAccountingServerIndex = _Gs2328RADIUSAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4, 1, 1),
    _Gs2328RADIUSAccountingServerIndex_Type()
)
gs2328RADIUSAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerIndex.setStatus("current")


class _Gs2328RADIUSAccountingServerEnable_Type(Integer32):
    """Custom type gs2328RADIUSAccountingServerEnable based on Integer32"""
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


_Gs2328RADIUSAccountingServerEnable_Type.__name__ = "Integer32"
_Gs2328RADIUSAccountingServerEnable_Object = MibTableColumn
gs2328RADIUSAccountingServerEnable = _Gs2328RADIUSAccountingServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4, 1, 2),
    _Gs2328RADIUSAccountingServerEnable_Type()
)
gs2328RADIUSAccountingServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerEnable.setStatus("current")
_Gs2328RADIUSAccountingServerIP_Type = DisplayString
_Gs2328RADIUSAccountingServerIP_Object = MibTableColumn
gs2328RADIUSAccountingServerIP = _Gs2328RADIUSAccountingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4, 1, 3),
    _Gs2328RADIUSAccountingServerIP_Type()
)
gs2328RADIUSAccountingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerIP.setStatus("current")


class _Gs2328RADIUSAccountingServerPort_Type(Integer32):
    """Custom type gs2328RADIUSAccountingServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328RADIUSAccountingServerPort_Type.__name__ = "Integer32"
_Gs2328RADIUSAccountingServerPort_Object = MibTableColumn
gs2328RADIUSAccountingServerPort = _Gs2328RADIUSAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4, 1, 4),
    _Gs2328RADIUSAccountingServerPort_Type()
)
gs2328RADIUSAccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerPort.setStatus("current")
_Gs2328RADIUSAccountingServerSecret_Type = DisplayString
_Gs2328RADIUSAccountingServerSecret_Object = MibTableColumn
gs2328RADIUSAccountingServerSecret = _Gs2328RADIUSAccountingServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 4, 1, 5),
    _Gs2328RADIUSAccountingServerSecret_Type()
)
gs2328RADIUSAccountingServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingServerSecret.setStatus("current")
_Gs2328TACACSPlusAuthenticationServerTable_Object = MibTable
gs2328TACACSPlusAuthenticationServerTable = _Gs2328TACACSPlusAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5)
)
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerTable.setStatus("current")
_Gs2328TACACSPlusAuthenticationServerEntry_Object = MibTableRow
gs2328TACACSPlusAuthenticationServerEntry = _Gs2328TACACSPlusAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5, 1)
)
gs2328TACACSPlusAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328TACACSPlusAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerEntry.setStatus("current")


class _Gs2328TACACSPlusAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2328TACACSPlusAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328TACACSPlusAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2328TACACSPlusAuthenticationServerIndex_Object = MibTableColumn
gs2328TACACSPlusAuthenticationServerIndex = _Gs2328TACACSPlusAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5, 1, 1),
    _Gs2328TACACSPlusAuthenticationServerIndex_Type()
)
gs2328TACACSPlusAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerIndex.setStatus("current")


class _Gs2328TACACSPlusAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2328TACACSPlusAuthenticationServerEnable based on Integer32"""
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


_Gs2328TACACSPlusAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2328TACACSPlusAuthenticationServerEnable_Object = MibTableColumn
gs2328TACACSPlusAuthenticationServerEnable = _Gs2328TACACSPlusAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5, 1, 2),
    _Gs2328TACACSPlusAuthenticationServerEnable_Type()
)
gs2328TACACSPlusAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerEnable.setStatus("current")
_Gs2328TACACSPlusAuthenticationServerIP_Type = DisplayString
_Gs2328TACACSPlusAuthenticationServerIP_Object = MibTableColumn
gs2328TACACSPlusAuthenticationServerIP = _Gs2328TACACSPlusAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5, 1, 3),
    _Gs2328TACACSPlusAuthenticationServerIP_Type()
)
gs2328TACACSPlusAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerIP.setStatus("current")


class _Gs2328TACACSPlusAuthenticationServerPort_Type(Integer32):
    """Custom type gs2328TACACSPlusAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328TACACSPlusAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2328TACACSPlusAuthenticationServerPort_Object = MibTableColumn
gs2328TACACSPlusAuthenticationServerPort = _Gs2328TACACSPlusAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5, 1, 4),
    _Gs2328TACACSPlusAuthenticationServerPort_Type()
)
gs2328TACACSPlusAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerPort.setStatus("current")
_Gs2328TACACSPlusAuthenticationServerSecret_Type = DisplayString
_Gs2328TACACSPlusAuthenticationServerSecret_Object = MibTableColumn
gs2328TACACSPlusAuthenticationServerSecret = _Gs2328TACACSPlusAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 5, 1, 5),
    _Gs2328TACACSPlusAuthenticationServerSecret_Type()
)
gs2328TACACSPlusAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328TACACSPlusAuthenticationServerSecret.setStatus("current")
_Gs2328RADIUSStatisticsTable_Object = MibTable
gs2328RADIUSStatisticsTable = _Gs2328RADIUSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6)
)
if mibBuilder.loadTexts:
    gs2328RADIUSStatisticsTable.setStatus("current")
_Gs2328RADIUSStatisticsEntry_Object = MibTableRow
gs2328RADIUSStatisticsEntry = _Gs2328RADIUSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1)
)
gs2328RADIUSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328RADIUSAuthStatisticsServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328RADIUSStatisticsEntry.setStatus("current")


class _Gs2328RADIUSAuthStatisticsServerIndex_Type(Integer32):
    """Custom type gs2328RADIUSAuthStatisticsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328RADIUSAuthStatisticsServerIndex_Type.__name__ = "Integer32"
_Gs2328RADIUSAuthStatisticsServerIndex_Object = MibTableColumn
gs2328RADIUSAuthStatisticsServerIndex = _Gs2328RADIUSAuthStatisticsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 1),
    _Gs2328RADIUSAuthStatisticsServerIndex_Type()
)
gs2328RADIUSAuthStatisticsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsServerIndex.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktAccessAccepts_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktAccessAccepts_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktAccessAccepts = _Gs2328RADIUSAuthStatisticsRecPktAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 2),
    _Gs2328RADIUSAuthStatisticsRecPktAccessAccepts_Type()
)
gs2328RADIUSAuthStatisticsRecPktAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktAccessAccepts.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktAccessRejects_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktAccessRejects_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktAccessRejects = _Gs2328RADIUSAuthStatisticsRecPktAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 3),
    _Gs2328RADIUSAuthStatisticsRecPktAccessRejects_Type()
)
gs2328RADIUSAuthStatisticsRecPktAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktAccessRejects.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktAccessChallenges_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktAccessChallenges_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktAccessChallenges = _Gs2328RADIUSAuthStatisticsRecPktAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 4),
    _Gs2328RADIUSAuthStatisticsRecPktAccessChallenges_Type()
)
gs2328RADIUSAuthStatisticsRecPktAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktAccessChallenges.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses = _Gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 5),
    _Gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses_Type()
)
gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktBadAuthenticators = _Gs2328RADIUSAuthStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 6),
    _Gs2328RADIUSAuthStatisticsRecPktBadAuthenticators_Type()
)
gs2328RADIUSAuthStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktUnknownTypes = _Gs2328RADIUSAuthStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 7),
    _Gs2328RADIUSAuthStatisticsRecPktUnknownTypes_Type()
)
gs2328RADIUSAuthStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2328RADIUSAuthStatisticsRecPktDropped_Type = Counter32
_Gs2328RADIUSAuthStatisticsRecPktDropped_Object = MibTableColumn
gs2328RADIUSAuthStatisticsRecPktDropped = _Gs2328RADIUSAuthStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 8),
    _Gs2328RADIUSAuthStatisticsRecPktDropped_Type()
)
gs2328RADIUSAuthStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsRecPktDropped.setStatus("current")
_Gs2328RADIUSAuthStatisticsTransmitPktAccessRequests_Type = Counter32
_Gs2328RADIUSAuthStatisticsTransmitPktAccessRequests_Object = MibTableColumn
gs2328RADIUSAuthStatisticsTransmitPktAccessRequests = _Gs2328RADIUSAuthStatisticsTransmitPktAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 9),
    _Gs2328RADIUSAuthStatisticsTransmitPktAccessRequests_Type()
)
gs2328RADIUSAuthStatisticsTransmitPktAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsTransmitPktAccessRequests.setStatus("current")
_Gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type = Counter32
_Gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object = MibTableColumn
gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions = _Gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 10),
    _Gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type()
)
gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setStatus("current")
_Gs2328RADIUSAuthStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2328RADIUSAuthStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2328RADIUSAuthStatisticsTransmitPktPendingRequests = _Gs2328RADIUSAuthStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 11),
    _Gs2328RADIUSAuthStatisticsTransmitPktPendingRequests_Type()
)
gs2328RADIUSAuthStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2328RADIUSAuthStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2328RADIUSAuthStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2328RADIUSAuthStatisticsTransmitPktTimeouts = _Gs2328RADIUSAuthStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 12),
    _Gs2328RADIUSAuthStatisticsTransmitPktTimeouts_Type()
)
gs2328RADIUSAuthStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2328RADIUSAuthIP_Type = DisplayString
_Gs2328RADIUSAuthIP_Object = MibTableColumn
gs2328RADIUSAuthIP = _Gs2328RADIUSAuthIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 13),
    _Gs2328RADIUSAuthIP_Type()
)
gs2328RADIUSAuthIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthIP.setStatus("current")
_Gs2328RADIUSAuthState_Type = DisplayString
_Gs2328RADIUSAuthState_Object = MibTableColumn
gs2328RADIUSAuthState = _Gs2328RADIUSAuthState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 14),
    _Gs2328RADIUSAuthState_Type()
)
gs2328RADIUSAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthState.setStatus("current")
_Gs2328RADIUSAuthRoundTripTime_Type = DisplayString
_Gs2328RADIUSAuthRoundTripTime_Object = MibTableColumn
gs2328RADIUSAuthRoundTripTime = _Gs2328RADIUSAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 15),
    _Gs2328RADIUSAuthRoundTripTime_Type()
)
gs2328RADIUSAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAuthRoundTripTime.setStatus("current")
_Gs2328RADIUSAccountingStatisticsRecPktResponses_Type = Counter32
_Gs2328RADIUSAccountingStatisticsRecPktResponses_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsRecPktResponses = _Gs2328RADIUSAccountingStatisticsRecPktResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 16),
    _Gs2328RADIUSAccountingStatisticsRecPktResponses_Type()
)
gs2328RADIUSAccountingStatisticsRecPktResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsRecPktResponses.setStatus("current")
_Gs2328RADIUSAccountingStatisticsRecPktMalformedResponses_Type = Counter32
_Gs2328RADIUSAccountingStatisticsRecPktMalformedResponses_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsRecPktMalformedResponses = _Gs2328RADIUSAccountingStatisticsRecPktMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 17),
    _Gs2328RADIUSAccountingStatisticsRecPktMalformedResponses_Type()
)
gs2328RADIUSAccountingStatisticsRecPktMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsRecPktMalformedResponses.setStatus("current")
_Gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators = _Gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 18),
    _Gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators_Type()
)
gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2328RADIUSAccountingStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2328RADIUSAccountingStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsRecPktUnknownTypes = _Gs2328RADIUSAccountingStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 19),
    _Gs2328RADIUSAccountingStatisticsRecPktUnknownTypes_Type()
)
gs2328RADIUSAccountingStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2328RADIUSAccountingStatisticsRecPktDropped_Type = Counter32
_Gs2328RADIUSAccountingStatisticsRecPktDropped_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsRecPktDropped = _Gs2328RADIUSAccountingStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 20),
    _Gs2328RADIUSAccountingStatisticsRecPktDropped_Type()
)
gs2328RADIUSAccountingStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsRecPktDropped.setStatus("current")
_Gs2328RADIUSAccountingStatisticsTransmitPktRequests_Type = Counter32
_Gs2328RADIUSAccountingStatisticsTransmitPktRequests_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsTransmitPktRequests = _Gs2328RADIUSAccountingStatisticsTransmitPktRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 21),
    _Gs2328RADIUSAccountingStatisticsTransmitPktRequests_Type()
)
gs2328RADIUSAccountingStatisticsTransmitPktRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsTransmitPktRequests.setStatus("current")
_Gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions_Type = Counter32
_Gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions = _Gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 22),
    _Gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions_Type()
)
gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions.setStatus("current")
_Gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests = _Gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 23),
    _Gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests_Type()
)
gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2328RADIUSAccountingStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2328RADIUSAccountingStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2328RADIUSAccountingStatisticsTransmitPktTimeouts = _Gs2328RADIUSAccountingStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 24),
    _Gs2328RADIUSAccountingStatisticsTransmitPktTimeouts_Type()
)
gs2328RADIUSAccountingStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2328RADIUSAccountingIP_Type = DisplayString
_Gs2328RADIUSAccountingIP_Object = MibTableColumn
gs2328RADIUSAccountingIP = _Gs2328RADIUSAccountingIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 25),
    _Gs2328RADIUSAccountingIP_Type()
)
gs2328RADIUSAccountingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingIP.setStatus("current")
_Gs2328RADIUSAccountingState_Type = DisplayString
_Gs2328RADIUSAccountingState_Object = MibTableColumn
gs2328RADIUSAccountingState = _Gs2328RADIUSAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 26),
    _Gs2328RADIUSAccountingState_Type()
)
gs2328RADIUSAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingState.setStatus("current")
_Gs2328RADIUSAccountingRoundTripTime_Type = DisplayString
_Gs2328RADIUSAccountingRoundTripTime_Object = MibTableColumn
gs2328RADIUSAccountingRoundTripTime = _Gs2328RADIUSAccountingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 27),
    _Gs2328RADIUSAccountingRoundTripTime_Type()
)
gs2328RADIUSAccountingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328RADIUSAccountingRoundTripTime.setStatus("current")


class _Gs2328RADIUSStatisticsClear_Type(Integer32):
    """Custom type gs2328RADIUSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328RADIUSStatisticsClear_Type.__name__ = "Integer32"
_Gs2328RADIUSStatisticsClear_Object = MibTableColumn
gs2328RADIUSStatisticsClear = _Gs2328RADIUSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 10, 6, 1, 28),
    _Gs2328RADIUSStatisticsClear_Type()
)
gs2328RADIUSStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RADIUSStatisticsClear.setStatus("current")
_Gs2328NAS_ObjectIdentity = ObjectIdentity
gs2328NAS = _Gs2328NAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11)
)
_Gs2328NASConfiguration_ObjectIdentity = ObjectIdentity
gs2328NASConfiguration = _Gs2328NASConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1)
)


class _Gs2328NASConfigMode_Type(Integer32):
    """Custom type gs2328NASConfigMode based on Integer32"""
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


_Gs2328NASConfigMode_Type.__name__ = "Integer32"
_Gs2328NASConfigMode_Object = MibScalar
gs2328NASConfigMode = _Gs2328NASConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 1),
    _Gs2328NASConfigMode_Type()
)
gs2328NASConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigMode.setStatus("current")


class _Gs2328NASConfigReauthEnabled_Type(Integer32):
    """Custom type gs2328NASConfigReauthEnabled based on Integer32"""
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


_Gs2328NASConfigReauthEnabled_Type.__name__ = "Integer32"
_Gs2328NASConfigReauthEnabled_Object = MibScalar
gs2328NASConfigReauthEnabled = _Gs2328NASConfigReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 2),
    _Gs2328NASConfigReauthEnabled_Type()
)
gs2328NASConfigReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigReauthEnabled.setStatus("current")


class _Gs2328NASConfigReauthPeriod_Type(Integer32):
    """Custom type gs2328NASConfigReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Gs2328NASConfigReauthPeriod_Type.__name__ = "Integer32"
_Gs2328NASConfigReauthPeriod_Object = MibScalar
gs2328NASConfigReauthPeriod = _Gs2328NASConfigReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 3),
    _Gs2328NASConfigReauthPeriod_Type()
)
gs2328NASConfigReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigReauthPeriod.setStatus("current")


class _Gs2328NASConfigEAPOLTimeout_Type(Integer32):
    """Custom type gs2328NASConfigEAPOLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328NASConfigEAPOLTimeout_Type.__name__ = "Integer32"
_Gs2328NASConfigEAPOLTimeout_Object = MibScalar
gs2328NASConfigEAPOLTimeout = _Gs2328NASConfigEAPOLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 4),
    _Gs2328NASConfigEAPOLTimeout_Type()
)
gs2328NASConfigEAPOLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigEAPOLTimeout.setStatus("current")


class _Gs2328NASConfigAgingPeriod_Type(Integer32):
    """Custom type gs2328NASConfigAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2328NASConfigAgingPeriod_Type.__name__ = "Integer32"
_Gs2328NASConfigAgingPeriod_Object = MibScalar
gs2328NASConfigAgingPeriod = _Gs2328NASConfigAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 5),
    _Gs2328NASConfigAgingPeriod_Type()
)
gs2328NASConfigAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigAgingPeriod.setStatus("current")


class _Gs2328NASConfigHoldTime_Type(Integer32):
    """Custom type gs2328NASConfigHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2328NASConfigHoldTime_Type.__name__ = "Integer32"
_Gs2328NASConfigHoldTime_Object = MibScalar
gs2328NASConfigHoldTime = _Gs2328NASConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 6),
    _Gs2328NASConfigHoldTime_Type()
)
gs2328NASConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigHoldTime.setStatus("current")


class _Gs2328NASConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2328NASConfigRADIUSAssignedQoSEnabled based on Integer32"""
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


_Gs2328NASConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2328NASConfigRADIUSAssignedQoSEnabled_Object = MibScalar
gs2328NASConfigRADIUSAssignedQoSEnabled = _Gs2328NASConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 7),
    _Gs2328NASConfigRADIUSAssignedQoSEnabled_Type()
)
gs2328NASConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2328NASConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2328NASConfigRADIUSAssignedVLANEnabled based on Integer32"""
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


_Gs2328NASConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2328NASConfigRADIUSAssignedVLANEnabled_Object = MibScalar
gs2328NASConfigRADIUSAssignedVLANEnabled = _Gs2328NASConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 8),
    _Gs2328NASConfigRADIUSAssignedVLANEnabled_Type()
)
gs2328NASConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2328NASConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2328NASConfigGuestVLANEnabled based on Integer32"""
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


_Gs2328NASConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2328NASConfigGuestVLANEnabled_Object = MibScalar
gs2328NASConfigGuestVLANEnabled = _Gs2328NASConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 9),
    _Gs2328NASConfigGuestVLANEnabled_Type()
)
gs2328NASConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigGuestVLANEnabled.setStatus("current")


class _Gs2328NASConfigGuestVLANID_Type(Integer32):
    """Custom type gs2328NASConfigGuestVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328NASConfigGuestVLANID_Type.__name__ = "Integer32"
_Gs2328NASConfigGuestVLANID_Object = MibScalar
gs2328NASConfigGuestVLANID = _Gs2328NASConfigGuestVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 10),
    _Gs2328NASConfigGuestVLANID_Type()
)
gs2328NASConfigGuestVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigGuestVLANID.setStatus("current")


class _Gs2328NASConfigMaxReauthCount_Type(Integer32):
    """Custom type gs2328NASConfigMaxReauthCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2328NASConfigMaxReauthCount_Type.__name__ = "Integer32"
_Gs2328NASConfigMaxReauthCount_Object = MibScalar
gs2328NASConfigMaxReauthCount = _Gs2328NASConfigMaxReauthCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 11),
    _Gs2328NASConfigMaxReauthCount_Type()
)
gs2328NASConfigMaxReauthCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigMaxReauthCount.setStatus("current")


class _Gs2328NASConfigAllowGuestVLANEAPOLSeen_Type(Integer32):
    """Custom type gs2328NASConfigAllowGuestVLANEAPOLSeen based on Integer32"""
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


_Gs2328NASConfigAllowGuestVLANEAPOLSeen_Type.__name__ = "Integer32"
_Gs2328NASConfigAllowGuestVLANEAPOLSeen_Object = MibScalar
gs2328NASConfigAllowGuestVLANEAPOLSeen = _Gs2328NASConfigAllowGuestVLANEAPOLSeen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 12),
    _Gs2328NASConfigAllowGuestVLANEAPOLSeen_Type()
)
gs2328NASConfigAllowGuestVLANEAPOLSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigAllowGuestVLANEAPOLSeen.setStatus("current")
_Gs2328NASPortConfigTable_Object = MibTable
gs2328NASPortConfigTable = _Gs2328NASPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13)
)
if mibBuilder.loadTexts:
    gs2328NASPortConfigTable.setStatus("current")
_Gs2328NASPortConfigEntry_Object = MibTableRow
gs2328NASPortConfigEntry = _Gs2328NASPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1)
)
gs2328NASPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328NASPortConfigEntry.setStatus("current")


class _Gs2328NASPortConfigPort_Type(Integer32):
    """Custom type gs2328NASPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2328NASPortConfigPort_Type.__name__ = "Integer32"
_Gs2328NASPortConfigPort_Object = MibTableColumn
gs2328NASPortConfigPort = _Gs2328NASPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 1),
    _Gs2328NASPortConfigPort_Type()
)
gs2328NASPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328NASPortConfigPort.setStatus("current")


class _Gs2328NASPortConfigAdminState_Type(Integer32):
    """Custom type gs2328NASPortConfigAdminState based on Integer32"""
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


_Gs2328NASPortConfigAdminState_Type.__name__ = "Integer32"
_Gs2328NASPortConfigAdminState_Object = MibTableColumn
gs2328NASPortConfigAdminState = _Gs2328NASPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 2),
    _Gs2328NASPortConfigAdminState_Type()
)
gs2328NASPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigAdminState.setStatus("current")


class _Gs2328NASPortConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2328NASPortConfigRADIUSAssignedQoSEnabled based on Integer32"""
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


_Gs2328NASPortConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2328NASPortConfigRADIUSAssignedQoSEnabled_Object = MibTableColumn
gs2328NASPortConfigRADIUSAssignedQoSEnabled = _Gs2328NASPortConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 3),
    _Gs2328NASPortConfigRADIUSAssignedQoSEnabled_Type()
)
gs2328NASPortConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2328NASPortConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2328NASPortConfigRADIUSAssignedVLANEnabled based on Integer32"""
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


_Gs2328NASPortConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2328NASPortConfigRADIUSAssignedVLANEnabled_Object = MibTableColumn
gs2328NASPortConfigRADIUSAssignedVLANEnabled = _Gs2328NASPortConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 4),
    _Gs2328NASPortConfigRADIUSAssignedVLANEnabled_Type()
)
gs2328NASPortConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2328NASPortConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2328NASPortConfigGuestVLANEnabled based on Integer32"""
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


_Gs2328NASPortConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2328NASPortConfigGuestVLANEnabled_Object = MibTableColumn
gs2328NASPortConfigGuestVLANEnabled = _Gs2328NASPortConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 5),
    _Gs2328NASPortConfigGuestVLANEnabled_Type()
)
gs2328NASPortConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigGuestVLANEnabled.setStatus("current")
_Gs2328NASPortConfigPortState_Type = DisplayString
_Gs2328NASPortConfigPortState_Object = MibTableColumn
gs2328NASPortConfigPortState = _Gs2328NASPortConfigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 6),
    _Gs2328NASPortConfigPortState_Type()
)
gs2328NASPortConfigPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASPortConfigPortState.setStatus("current")


class _Gs2328NASPortConfigReauthenticate_Type(Integer32):
    """Custom type gs2328NASPortConfigReauthenticate based on Integer32"""
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


_Gs2328NASPortConfigReauthenticate_Type.__name__ = "Integer32"
_Gs2328NASPortConfigReauthenticate_Object = MibTableColumn
gs2328NASPortConfigReauthenticate = _Gs2328NASPortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 7),
    _Gs2328NASPortConfigReauthenticate_Type()
)
gs2328NASPortConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigReauthenticate.setStatus("current")


class _Gs2328NASPortConfigReinitialize_Type(Integer32):
    """Custom type gs2328NASPortConfigReinitialize based on Integer32"""
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


_Gs2328NASPortConfigReinitialize_Type.__name__ = "Integer32"
_Gs2328NASPortConfigReinitialize_Object = MibTableColumn
gs2328NASPortConfigReinitialize = _Gs2328NASPortConfigReinitialize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 8),
    _Gs2328NASPortConfigReinitialize_Type()
)
gs2328NASPortConfigReinitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigReinitialize.setStatus("current")


class _Gs2328NASPortConfigFallbackEnabled_Type(Integer32):
    """Custom type gs2328NASPortConfigFallbackEnabled based on Integer32"""
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


_Gs2328NASPortConfigFallbackEnabled_Type.__name__ = "Integer32"
_Gs2328NASPortConfigFallbackEnabled_Object = MibTableColumn
gs2328NASPortConfigFallbackEnabled = _Gs2328NASPortConfigFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 13, 1, 101),
    _Gs2328NASPortConfigFallbackEnabled_Type()
)
gs2328NASPortConfigFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASPortConfigFallbackEnabled.setStatus("current")


class _Gs2328NASConfigMacBasedUseEAP_Type(Integer32):
    """Custom type gs2328NASConfigMacBasedUseEAP based on Integer32"""
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


_Gs2328NASConfigMacBasedUseEAP_Type.__name__ = "Integer32"
_Gs2328NASConfigMacBasedUseEAP_Object = MibScalar
gs2328NASConfigMacBasedUseEAP = _Gs2328NASConfigMacBasedUseEAP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 1, 101),
    _Gs2328NASConfigMacBasedUseEAP_Type()
)
gs2328NASConfigMacBasedUseEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASConfigMacBasedUseEAP.setStatus("current")
_Gs2328NASSwitchStatusTable_Object = MibTable
gs2328NASSwitchStatusTable = _Gs2328NASSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2)
)
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusTable.setStatus("current")
_Gs2328NASSwitchStatusEntry_Object = MibTableRow
gs2328NASSwitchStatusEntry = _Gs2328NASSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1)
)
gs2328NASSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusEntry.setStatus("current")
_Gs2328NASSwitchStatusAdminState_Type = DisplayString
_Gs2328NASSwitchStatusAdminState_Object = MibTableColumn
gs2328NASSwitchStatusAdminState = _Gs2328NASSwitchStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1, 2),
    _Gs2328NASSwitchStatusAdminState_Type()
)
gs2328NASSwitchStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusAdminState.setStatus("current")
_Gs2328NASSwitchStatusPortState_Type = DisplayString
_Gs2328NASSwitchStatusPortState_Object = MibTableColumn
gs2328NASSwitchStatusPortState = _Gs2328NASSwitchStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1, 3),
    _Gs2328NASSwitchStatusPortState_Type()
)
gs2328NASSwitchStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusPortState.setStatus("current")
_Gs2328NASSwitchStatusLastSource_Type = DisplayString
_Gs2328NASSwitchStatusLastSource_Object = MibTableColumn
gs2328NASSwitchStatusLastSource = _Gs2328NASSwitchStatusLastSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1, 4),
    _Gs2328NASSwitchStatusLastSource_Type()
)
gs2328NASSwitchStatusLastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusLastSource.setStatus("current")
_Gs2328NASSwitchStatusLastID_Type = DisplayString
_Gs2328NASSwitchStatusLastID_Object = MibTableColumn
gs2328NASSwitchStatusLastID = _Gs2328NASSwitchStatusLastID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1, 5),
    _Gs2328NASSwitchStatusLastID_Type()
)
gs2328NASSwitchStatusLastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusLastID.setStatus("current")
_Gs2328NASSwitchStatusQoSClass_Type = DisplayString
_Gs2328NASSwitchStatusQoSClass_Object = MibTableColumn
gs2328NASSwitchStatusQoSClass = _Gs2328NASSwitchStatusQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1, 6),
    _Gs2328NASSwitchStatusQoSClass_Type()
)
gs2328NASSwitchStatusQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusQoSClass.setStatus("current")
_Gs2328NASSwitchStatusPortVlanID_Type = DisplayString
_Gs2328NASSwitchStatusPortVlanID_Object = MibTableColumn
gs2328NASSwitchStatusPortVlanID = _Gs2328NASSwitchStatusPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 2, 1, 7),
    _Gs2328NASSwitchStatusPortVlanID_Type()
)
gs2328NASSwitchStatusPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASSwitchStatusPortVlanID.setStatus("current")
_Gs2328NASPortStatus_ObjectIdentity = ObjectIdentity
gs2328NASPortStatus = _Gs2328NASPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3)
)
_Gs2328NASPortStatusCountersTable_Object = MibTable
gs2328NASPortStatusCountersTable = _Gs2328NASPortStatusCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    gs2328NASPortStatusCountersTable.setStatus("current")
_Gs2328NASPortStatusCountersEntry_Object = MibTableRow
gs2328NASPortStatusCountersEntry = _Gs2328NASPortStatusCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1)
)
gs2328NASPortStatusCountersEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328NASPortStatusCountersEntry.setStatus("current")
_Gs2328NASRxCountersEAPOLTotal_Type = Counter32
_Gs2328NASRxCountersEAPOLTotal_Object = MibTableColumn
gs2328NASRxCountersEAPOLTotal = _Gs2328NASRxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 2),
    _Gs2328NASRxCountersEAPOLTotal_Type()
)
gs2328NASRxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLTotal.setStatus("current")
_Gs2328NASRxCountersEAPOLResponseID_Type = Counter32
_Gs2328NASRxCountersEAPOLResponseID_Object = MibTableColumn
gs2328NASRxCountersEAPOLResponseID = _Gs2328NASRxCountersEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 3),
    _Gs2328NASRxCountersEAPOLResponseID_Type()
)
gs2328NASRxCountersEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLResponseID.setStatus("current")
_Gs2328NASRxCountersEAPOLResponses_Type = Counter32
_Gs2328NASRxCountersEAPOLResponses_Object = MibTableColumn
gs2328NASRxCountersEAPOLResponses = _Gs2328NASRxCountersEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 4),
    _Gs2328NASRxCountersEAPOLResponses_Type()
)
gs2328NASRxCountersEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLResponses.setStatus("current")
_Gs2328NASRxCountersEAPOLStart_Type = Counter32
_Gs2328NASRxCountersEAPOLStart_Object = MibTableColumn
gs2328NASRxCountersEAPOLStart = _Gs2328NASRxCountersEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 5),
    _Gs2328NASRxCountersEAPOLStart_Type()
)
gs2328NASRxCountersEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLStart.setStatus("current")
_Gs2328NASRxCountersEAPOLLogoff_Type = Counter32
_Gs2328NASRxCountersEAPOLLogoff_Object = MibTableColumn
gs2328NASRxCountersEAPOLLogoff = _Gs2328NASRxCountersEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 6),
    _Gs2328NASRxCountersEAPOLLogoff_Type()
)
gs2328NASRxCountersEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLLogoff.setStatus("current")
_Gs2328NASRxCountersEAPOLInvalidType_Type = Counter32
_Gs2328NASRxCountersEAPOLInvalidType_Object = MibTableColumn
gs2328NASRxCountersEAPOLInvalidType = _Gs2328NASRxCountersEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 7),
    _Gs2328NASRxCountersEAPOLInvalidType_Type()
)
gs2328NASRxCountersEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLInvalidType.setStatus("current")
_Gs2328NASRxCountersEAPOLInvalidLength_Type = Counter32
_Gs2328NASRxCountersEAPOLInvalidLength_Object = MibTableColumn
gs2328NASRxCountersEAPOLInvalidLength = _Gs2328NASRxCountersEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 8),
    _Gs2328NASRxCountersEAPOLInvalidLength_Type()
)
gs2328NASRxCountersEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxCountersEAPOLInvalidLength.setStatus("current")
_Gs2328NASTxCountersEAPOLTotal_Type = Counter32
_Gs2328NASTxCountersEAPOLTotal_Object = MibTableColumn
gs2328NASTxCountersEAPOLTotal = _Gs2328NASTxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 9),
    _Gs2328NASTxCountersEAPOLTotal_Type()
)
gs2328NASTxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxCountersEAPOLTotal.setStatus("current")
_Gs2328NASTxCountersEAPOLRequestID_Type = Counter32
_Gs2328NASTxCountersEAPOLRequestID_Object = MibTableColumn
gs2328NASTxCountersEAPOLRequestID = _Gs2328NASTxCountersEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 10),
    _Gs2328NASTxCountersEAPOLRequestID_Type()
)
gs2328NASTxCountersEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxCountersEAPOLRequestID.setStatus("current")
_Gs2328NASTxCountersEAPOLRequests_Type = Counter32
_Gs2328NASTxCountersEAPOLRequests_Object = MibTableColumn
gs2328NASTxCountersEAPOLRequests = _Gs2328NASTxCountersEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 11),
    _Gs2328NASTxCountersEAPOLRequests_Type()
)
gs2328NASTxCountersEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxCountersEAPOLRequests.setStatus("current")
_Gs2328NASRxBackendServerCountersAccessChallenges_Type = Counter32
_Gs2328NASRxBackendServerCountersAccessChallenges_Object = MibTableColumn
gs2328NASRxBackendServerCountersAccessChallenges = _Gs2328NASRxBackendServerCountersAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 12),
    _Gs2328NASRxBackendServerCountersAccessChallenges_Type()
)
gs2328NASRxBackendServerCountersAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerCountersAccessChallenges.setStatus("current")
_Gs2328NASRxBackendServerCountersOtherRequests_Type = Counter32
_Gs2328NASRxBackendServerCountersOtherRequests_Object = MibTableColumn
gs2328NASRxBackendServerCountersOtherRequests = _Gs2328NASRxBackendServerCountersOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 13),
    _Gs2328NASRxBackendServerCountersOtherRequests_Type()
)
gs2328NASRxBackendServerCountersOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerCountersOtherRequests.setStatus("current")
_Gs2328NASRxBackendServerCountersAuthSuccesses_Type = Counter32
_Gs2328NASRxBackendServerCountersAuthSuccesses_Object = MibTableColumn
gs2328NASRxBackendServerCountersAuthSuccesses = _Gs2328NASRxBackendServerCountersAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 14),
    _Gs2328NASRxBackendServerCountersAuthSuccesses_Type()
)
gs2328NASRxBackendServerCountersAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerCountersAuthSuccesses.setStatus("current")
_Gs2328NASRxBackendServerCountersAuthFailures_Type = Counter32
_Gs2328NASRxBackendServerCountersAuthFailures_Object = MibTableColumn
gs2328NASRxBackendServerCountersAuthFailures = _Gs2328NASRxBackendServerCountersAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 15),
    _Gs2328NASRxBackendServerCountersAuthFailures_Type()
)
gs2328NASRxBackendServerCountersAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerCountersAuthFailures.setStatus("current")
_Gs2328NASTxBackendServerCountersResponses_Type = Counter32
_Gs2328NASTxBackendServerCountersResponses_Object = MibTableColumn
gs2328NASTxBackendServerCountersResponses = _Gs2328NASTxBackendServerCountersResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 16),
    _Gs2328NASTxBackendServerCountersResponses_Type()
)
gs2328NASTxBackendServerCountersResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxBackendServerCountersResponses.setStatus("current")
_Gs2328NASLastSupplicantInfoMACAddress_Type = DisplayString
_Gs2328NASLastSupplicantInfoMACAddress_Object = MibTableColumn
gs2328NASLastSupplicantInfoMACAddress = _Gs2328NASLastSupplicantInfoMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 17),
    _Gs2328NASLastSupplicantInfoMACAddress_Type()
)
gs2328NASLastSupplicantInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASLastSupplicantInfoMACAddress.setStatus("current")
_Gs2328NASLastSupplicantInfoVlanID_Type = Integer32
_Gs2328NASLastSupplicantInfoVlanID_Object = MibTableColumn
gs2328NASLastSupplicantInfoVlanID = _Gs2328NASLastSupplicantInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 18),
    _Gs2328NASLastSupplicantInfoVlanID_Type()
)
gs2328NASLastSupplicantInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASLastSupplicantInfoVlanID.setStatus("current")
_Gs2328NASLastSupplicantInfoVersion_Type = Integer32
_Gs2328NASLastSupplicantInfoVersion_Object = MibTableColumn
gs2328NASLastSupplicantInfoVersion = _Gs2328NASLastSupplicantInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 19),
    _Gs2328NASLastSupplicantInfoVersion_Type()
)
gs2328NASLastSupplicantInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASLastSupplicantInfoVersion.setStatus("current")
_Gs2328NASLastSupplicantInfoIdentity_Type = DisplayString
_Gs2328NASLastSupplicantInfoIdentity_Object = MibTableColumn
gs2328NASLastSupplicantInfoIdentity = _Gs2328NASLastSupplicantInfoIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 20),
    _Gs2328NASLastSupplicantInfoIdentity_Type()
)
gs2328NASLastSupplicantInfoIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASLastSupplicantInfoIdentity.setStatus("current")


class _Gs2328NASCountersDoClear_Type(Integer32):
    """Custom type gs2328NASCountersDoClear based on Integer32"""
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


_Gs2328NASCountersDoClear_Type.__name__ = "Integer32"
_Gs2328NASCountersDoClear_Object = MibTableColumn
gs2328NASCountersDoClear = _Gs2328NASCountersDoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 1, 1, 21),
    _Gs2328NASCountersDoClear_Type()
)
gs2328NASCountersDoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328NASCountersDoClear.setStatus("current")
_Gs2328NASPortStatusClientsTable_Object = MibTable
gs2328NASPortStatusClientsTable = _Gs2328NASPortStatusClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328NASPortStatusClientsTable.setStatus("current")
_Gs2328NASPortStatusClientsEntry_Object = MibTableRow
gs2328NASPortStatusClientsEntry = _Gs2328NASPortStatusClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1)
)
gs2328NASPortStatusClientsEntry.setIndexNames(
    (0, "LANCOM-GS-2328-MIB", "gs2328NASPortConfigPort"),
    (0, "LANCOM-GS-2328-MIB", "gs2328NASClientsIndex"),
)
if mibBuilder.loadTexts:
    gs2328NASPortStatusClientsEntry.setStatus("current")


class _Gs2328NASClientsIndex_Type(Integer32):
    """Custom type gs2328NASClientsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2328NASClientsIndex_Type.__name__ = "Integer32"
_Gs2328NASClientsIndex_Object = MibTableColumn
gs2328NASClientsIndex = _Gs2328NASClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 1),
    _Gs2328NASClientsIndex_Type()
)
gs2328NASClientsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328NASClientsIndex.setStatus("current")
_Gs2328NASClientsIdentity_Type = DisplayString
_Gs2328NASClientsIdentity_Object = MibTableColumn
gs2328NASClientsIdentity = _Gs2328NASClientsIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 2),
    _Gs2328NASClientsIdentity_Type()
)
gs2328NASClientsIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASClientsIdentity.setStatus("current")
_Gs2328NASClientsMACAddress_Type = DisplayString
_Gs2328NASClientsMACAddress_Object = MibTableColumn
gs2328NASClientsMACAddress = _Gs2328NASClientsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 3),
    _Gs2328NASClientsMACAddress_Type()
)
gs2328NASClientsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASClientsMACAddress.setStatus("current")


class _Gs2328NASClientsVlanID_Type(Integer32):
    """Custom type gs2328NASClientsVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328NASClientsVlanID_Type.__name__ = "Integer32"
_Gs2328NASClientsVlanID_Object = MibTableColumn
gs2328NASClientsVlanID = _Gs2328NASClientsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 4),
    _Gs2328NASClientsVlanID_Type()
)
gs2328NASClientsVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASClientsVlanID.setStatus("current")
_Gs2328NASClientsState_Type = DisplayString
_Gs2328NASClientsState_Object = MibTableColumn
gs2328NASClientsState = _Gs2328NASClientsState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 5),
    _Gs2328NASClientsState_Type()
)
gs2328NASClientsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASClientsState.setStatus("current")
_Gs2328NASClientsLastAuth_Type = DisplayString
_Gs2328NASClientsLastAuth_Object = MibTableColumn
gs2328NASClientsLastAuth = _Gs2328NASClientsLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 6),
    _Gs2328NASClientsLastAuth_Type()
)
gs2328NASClientsLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASClientsLastAuth.setStatus("current")
_Gs2328NASRxClientsEAPOLTotal_Type = Counter32
_Gs2328NASRxClientsEAPOLTotal_Object = MibTableColumn
gs2328NASRxClientsEAPOLTotal = _Gs2328NASRxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 7),
    _Gs2328NASRxClientsEAPOLTotal_Type()
)
gs2328NASRxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLTotal.setStatus("current")
_Gs2328NASRxClientsEAPOLResponseID_Type = Counter32
_Gs2328NASRxClientsEAPOLResponseID_Object = MibTableColumn
gs2328NASRxClientsEAPOLResponseID = _Gs2328NASRxClientsEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 8),
    _Gs2328NASRxClientsEAPOLResponseID_Type()
)
gs2328NASRxClientsEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLResponseID.setStatus("current")
_Gs2328NASRxClientsEAPOLResponses_Type = Counter32
_Gs2328NASRxClientsEAPOLResponses_Object = MibTableColumn
gs2328NASRxClientsEAPOLResponses = _Gs2328NASRxClientsEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 9),
    _Gs2328NASRxClientsEAPOLResponses_Type()
)
gs2328NASRxClientsEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLResponses.setStatus("current")
_Gs2328NASRxClientsEAPOLStart_Type = Counter32
_Gs2328NASRxClientsEAPOLStart_Object = MibTableColumn
gs2328NASRxClientsEAPOLStart = _Gs2328NASRxClientsEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 10),
    _Gs2328NASRxClientsEAPOLStart_Type()
)
gs2328NASRxClientsEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLStart.setStatus("current")
_Gs2328NASRxClientsEAPOLLogoff_Type = Counter32
_Gs2328NASRxClientsEAPOLLogoff_Object = MibTableColumn
gs2328NASRxClientsEAPOLLogoff = _Gs2328NASRxClientsEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 11),
    _Gs2328NASRxClientsEAPOLLogoff_Type()
)
gs2328NASRxClientsEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLLogoff.setStatus("current")
_Gs2328NASRxClientsEAPOLInvalidType_Type = Counter32
_Gs2328NASRxClientsEAPOLInvalidType_Object = MibTableColumn
gs2328NASRxClientsEAPOLInvalidType = _Gs2328NASRxClientsEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 12),
    _Gs2328NASRxClientsEAPOLInvalidType_Type()
)
gs2328NASRxClientsEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLInvalidType.setStatus("current")
_Gs2328NASRxClientsEAPOLInvalidLength_Type = Counter32
_Gs2328NASRxClientsEAPOLInvalidLength_Object = MibTableColumn
gs2328NASRxClientsEAPOLInvalidLength = _Gs2328NASRxClientsEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 13),
    _Gs2328NASRxClientsEAPOLInvalidLength_Type()
)
gs2328NASRxClientsEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxClientsEAPOLInvalidLength.setStatus("current")
_Gs2328NASTxClientsEAPOLTotal_Type = Counter32
_Gs2328NASTxClientsEAPOLTotal_Object = MibTableColumn
gs2328NASTxClientsEAPOLTotal = _Gs2328NASTxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 14),
    _Gs2328NASTxClientsEAPOLTotal_Type()
)
gs2328NASTxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxClientsEAPOLTotal.setStatus("current")
_Gs2328NASTxClientsEAPOLRequestID_Type = Counter32
_Gs2328NASTxClientsEAPOLRequestID_Object = MibTableColumn
gs2328NASTxClientsEAPOLRequestID = _Gs2328NASTxClientsEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 15),
    _Gs2328NASTxClientsEAPOLRequestID_Type()
)
gs2328NASTxClientsEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxClientsEAPOLRequestID.setStatus("current")
_Gs2328NASTxClientsEAPOLRequests_Type = Counter32
_Gs2328NASTxClientsEAPOLRequests_Object = MibTableColumn
gs2328NASTxClientsEAPOLRequests = _Gs2328NASTxClientsEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 16),
    _Gs2328NASTxClientsEAPOLRequests_Type()
)
gs2328NASTxClientsEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxClientsEAPOLRequests.setStatus("current")
_Gs2328NASRxBackendServerClientsAccessChallenges_Type = Counter32
_Gs2328NASRxBackendServerClientsAccessChallenges_Object = MibTableColumn
gs2328NASRxBackendServerClientsAccessChallenges = _Gs2328NASRxBackendServerClientsAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 17),
    _Gs2328NASRxBackendServerClientsAccessChallenges_Type()
)
gs2328NASRxBackendServerClientsAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerClientsAccessChallenges.setStatus("current")
_Gs2328NASRxBackendServerClientsOtherRequests_Type = Counter32
_Gs2328NASRxBackendServerClientsOtherRequests_Object = MibTableColumn
gs2328NASRxBackendServerClientsOtherRequests = _Gs2328NASRxBackendServerClientsOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 18),
    _Gs2328NASRxBackendServerClientsOtherRequests_Type()
)
gs2328NASRxBackendServerClientsOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerClientsOtherRequests.setStatus("current")
_Gs2328NASRxBackendServerClientsAuthSuccesses_Type = Counter32
_Gs2328NASRxBackendServerClientsAuthSuccesses_Object = MibTableColumn
gs2328NASRxBackendServerClientsAuthSuccesses = _Gs2328NASRxBackendServerClientsAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 19),
    _Gs2328NASRxBackendServerClientsAuthSuccesses_Type()
)
gs2328NASRxBackendServerClientsAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerClientsAuthSuccesses.setStatus("current")
_Gs2328NASRxBackendServerClientsAuthFailures_Type = Counter32
_Gs2328NASRxBackendServerClientsAuthFailures_Object = MibTableColumn
gs2328NASRxBackendServerClientsAuthFailures = _Gs2328NASRxBackendServerClientsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 20),
    _Gs2328NASRxBackendServerClientsAuthFailures_Type()
)
gs2328NASRxBackendServerClientsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASRxBackendServerClientsAuthFailures.setStatus("current")
_Gs2328NASTxBackendServerClientsResponses_Type = Counter32
_Gs2328NASTxBackendServerClientsResponses_Object = MibTableColumn
gs2328NASTxBackendServerClientsResponses = _Gs2328NASTxBackendServerClientsResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 3, 11, 3, 2, 1, 21),
    _Gs2328NASTxBackendServerClientsResponses_Type()
)
gs2328NASTxBackendServerClientsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328NASTxBackendServerClientsResponses.setStatus("current")
_Gs2328Maintenance_ObjectIdentity = ObjectIdentity
gs2328Maintenance = _Gs2328Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4)
)


class _Gs2328RestartDevice_Type(Integer32):
    """Custom type gs2328RestartDevice based on Integer32"""
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


_Gs2328RestartDevice_Type.__name__ = "Integer32"
_Gs2328RestartDevice_Object = MibScalar
gs2328RestartDevice = _Gs2328RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 1),
    _Gs2328RestartDevice_Type()
)
gs2328RestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RestartDevice.setStatus("current")
_Gs2328Firmware_ObjectIdentity = ObjectIdentity
gs2328Firmware = _Gs2328Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 2)
)
_Gs2328FirmwareIpAddress_Type = IpAddress
_Gs2328FirmwareIpAddress_Object = MibScalar
gs2328FirmwareIpAddress = _Gs2328FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 2, 1),
    _Gs2328FirmwareIpAddress_Type()
)
gs2328FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FirmwareIpAddress.setStatus("current")
_Gs2328FirmwareFileName_Type = DisplayString
_Gs2328FirmwareFileName_Object = MibScalar
gs2328FirmwareFileName = _Gs2328FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 2, 2),
    _Gs2328FirmwareFileName_Type()
)
gs2328FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FirmwareFileName.setStatus("current")


class _Gs2328DoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2328DoFirmwareUpgrade based on Integer32"""
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


_Gs2328DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2328DoFirmwareUpgrade_Object = MibScalar
gs2328DoFirmwareUpgrade = _Gs2328DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 2, 3),
    _Gs2328DoFirmwareUpgrade_Type()
)
gs2328DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DoFirmwareUpgrade.setStatus("current")
_Gs2328SaveOrRestore_ObjectIdentity = ObjectIdentity
gs2328SaveOrRestore = _Gs2328SaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 3)
)


class _Gs2328FactoryDefaults_Type(Integer32):
    """Custom type gs2328FactoryDefaults based on Integer32"""
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


_Gs2328FactoryDefaults_Type.__name__ = "Integer32"
_Gs2328FactoryDefaults_Object = MibScalar
gs2328FactoryDefaults = _Gs2328FactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 3, 1),
    _Gs2328FactoryDefaults_Type()
)
gs2328FactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328FactoryDefaults.setStatus("current")


class _Gs2328SaveStart_Type(Integer32):
    """Custom type gs2328SaveStart based on Integer32"""
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


_Gs2328SaveStart_Type.__name__ = "Integer32"
_Gs2328SaveStart_Object = MibScalar
gs2328SaveStart = _Gs2328SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 3, 2),
    _Gs2328SaveStart_Type()
)
gs2328SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SaveStart.setStatus("current")


class _Gs2328SaveUser_Type(Integer32):
    """Custom type gs2328SaveUser based on Integer32"""
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


_Gs2328SaveUser_Type.__name__ = "Integer32"
_Gs2328SaveUser_Object = MibScalar
gs2328SaveUser = _Gs2328SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 3, 3),
    _Gs2328SaveUser_Type()
)
gs2328SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328SaveUser.setStatus("current")


class _Gs2328RestoreUser_Type(Integer32):
    """Custom type gs2328RestoreUser based on Integer32"""
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


_Gs2328RestoreUser_Type.__name__ = "Integer32"
_Gs2328RestoreUser_Object = MibScalar
gs2328RestoreUser = _Gs2328RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 3, 4),
    _Gs2328RestoreUser_Type()
)
gs2328RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328RestoreUser.setStatus("current")
_Gs2328ExportOrImport_ObjectIdentity = ObjectIdentity
gs2328ExportOrImport = _Gs2328ExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4)
)
_Gs2328ExportIpAddress_Type = IpAddress
_Gs2328ExportIpAddress_Object = MibScalar
gs2328ExportIpAddress = _Gs2328ExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4, 1),
    _Gs2328ExportIpAddress_Type()
)
gs2328ExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ExportIpAddress.setStatus("current")
_Gs2328ExportConfigName_Type = DisplayString
_Gs2328ExportConfigName_Object = MibScalar
gs2328ExportConfigName = _Gs2328ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4, 2),
    _Gs2328ExportConfigName_Type()
)
gs2328ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ExportConfigName.setStatus("current")


class _Gs2328DoExportConfig_Type(Integer32):
    """Custom type gs2328DoExportConfig based on Integer32"""
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


_Gs2328DoExportConfig_Type.__name__ = "Integer32"
_Gs2328DoExportConfig_Object = MibScalar
gs2328DoExportConfig = _Gs2328DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4, 3),
    _Gs2328DoExportConfig_Type()
)
gs2328DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DoExportConfig.setStatus("current")
_Gs2328ImportIpAddress_Type = IpAddress
_Gs2328ImportIpAddress_Object = MibScalar
gs2328ImportIpAddress = _Gs2328ImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4, 4),
    _Gs2328ImportIpAddress_Type()
)
gs2328ImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ImportIpAddress.setStatus("current")
_Gs2328ImportConfigName_Type = DisplayString
_Gs2328ImportConfigName_Object = MibScalar
gs2328ImportConfigName = _Gs2328ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4, 5),
    _Gs2328ImportConfigName_Type()
)
gs2328ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ImportConfigName.setStatus("current")


class _Gs2328DoImportConfig_Type(Integer32):
    """Custom type gs2328DoImportConfig based on Integer32"""
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


_Gs2328DoImportConfig_Type.__name__ = "Integer32"
_Gs2328DoImportConfig_Object = MibScalar
gs2328DoImportConfig = _Gs2328DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 4, 6),
    _Gs2328DoImportConfig_Type()
)
gs2328DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DoImportConfig.setStatus("current")
_Gs2328Diagnostics_ObjectIdentity = ObjectIdentity
gs2328Diagnostics = _Gs2328Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5)
)
_Gs2328PingIpAddress_Type = IpAddress
_Gs2328PingIpAddress_Object = MibScalar
gs2328PingIpAddress = _Gs2328PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 1),
    _Gs2328PingIpAddress_Type()
)
gs2328PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PingIpAddress.setStatus("current")


class _Gs2328PingSize_Type(Integer32):
    """Custom type gs2328PingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2328PingSize_Type.__name__ = "Integer32"
_Gs2328PingSize_Object = MibScalar
gs2328PingSize = _Gs2328PingSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 2),
    _Gs2328PingSize_Type()
)
gs2328PingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328PingSize.setStatus("current")


class _Gs2328DoPingConfig_Type(Integer32):
    """Custom type gs2328DoPingConfig based on Integer32"""
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


_Gs2328DoPingConfig_Type.__name__ = "Integer32"
_Gs2328DoPingConfig_Object = MibScalar
gs2328DoPingConfig = _Gs2328DoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 3),
    _Gs2328DoPingConfig_Type()
)
gs2328DoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DoPingConfig.setStatus("current")
_Gs2328PingResult_Type = DisplayString
_Gs2328PingResult_Object = MibScalar
gs2328PingResult = _Gs2328PingResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 4),
    _Gs2328PingResult_Type()
)
gs2328PingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328PingResult.setStatus("current")
_Gs2328Ping6IpAddress_Type = DisplayString
_Gs2328Ping6IpAddress_Object = MibScalar
gs2328Ping6IpAddress = _Gs2328Ping6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 5),
    _Gs2328Ping6IpAddress_Type()
)
gs2328Ping6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ping6IpAddress.setStatus("current")


class _Gs2328Ping6Size_Type(Integer32):
    """Custom type gs2328Ping6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2328Ping6Size_Type.__name__ = "Integer32"
_Gs2328Ping6Size_Object = MibScalar
gs2328Ping6Size = _Gs2328Ping6Size_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 6),
    _Gs2328Ping6Size_Type()
)
gs2328Ping6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328Ping6Size.setStatus("current")


class _Gs2328DoPing6Config_Type(Integer32):
    """Custom type gs2328DoPing6Config based on Integer32"""
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


_Gs2328DoPing6Config_Type.__name__ = "Integer32"
_Gs2328DoPing6Config_Object = MibScalar
gs2328DoPing6Config = _Gs2328DoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 7),
    _Gs2328DoPing6Config_Type()
)
gs2328DoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328DoPing6Config.setStatus("current")
_Gs2328Ping6Result_Type = DisplayString
_Gs2328Ping6Result_Object = MibScalar
gs2328Ping6Result = _Gs2328Ping6Result_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 5, 8),
    _Gs2328Ping6Result_Type()
)
gs2328Ping6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Ping6Result.setStatus("current")


class _Gs2328ColdRestartDevice_Type(Integer32):
    """Custom type gs2328ColdRestartDevice based on Integer32"""
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


_Gs2328ColdRestartDevice_Type.__name__ = "Integer32"
_Gs2328ColdRestartDevice_Object = MibScalar
gs2328ColdRestartDevice = _Gs2328ColdRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 4, 1500),
    _Gs2328ColdRestartDevice_Type()
)
gs2328ColdRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328ColdRestartDevice.setStatus("current")
_Gs2328Trap_ObjectIdentity = ObjectIdentity
gs2328Trap = _Gs2328Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5)
)
_Gs2328TrapEvent_ObjectIdentity = ObjectIdentity
gs2328TrapEvent = _Gs2328TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1)
)
_Gs2328TrapVariable_ObjectIdentity = ObjectIdentity
gs2328TrapVariable = _Gs2328TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 2)
)
_Gs2328Information_Type = DisplayString
_Gs2328Information_Object = MibScalar
gs2328Information = _Gs2328Information_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 2, 1),
    _Gs2328Information_Type()
)
gs2328Information.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328Information.setStatus("current")

# Managed Objects groups


# Notification objects

gs2328Emergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 1)
)
gs2328Emergency.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Emergency.setStatus(
        "current"
    )

gs2328Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 2)
)
gs2328Alert.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Alert.setStatus(
        "current"
    )

gs2328Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 3)
)
gs2328Critical.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Critical.setStatus(
        "current"
    )

gs2328Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 4)
)
gs2328Error.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Error.setStatus(
        "current"
    )

gs2328Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 5)
)
gs2328Warning.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Warning.setStatus(
        "current"
    )

gs2328Notice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 6)
)
gs2328Notice.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Notice.setStatus(
        "current"
    )

gs2328Informational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 7)
)
gs2328Informational.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Informational.setStatus(
        "current"
    )

gs2328Debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2330, 5, 1, 8)
)
gs2328Debug.setObjects(
    ("LANCOM-GS-2328-MIB", "gs2328Information")
)
if mibBuilder.loadTexts:
    gs2328Debug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-GS-2328-MIB",
    **{"lancom-systems": lancom_systems,
       "switchingSystems": switchingSystems,
       "gigabitEthernetSwitches": gigabitEthernetSwitches,
       "lancomGS2328": lancomGS2328,
       "gs2328System": gs2328System,
       "gs2328SystemInformation": gs2328SystemInformation,
       "gs2328ModelName": gs2328ModelName,
       "gs2328BIOSVersion": gs2328BIOSVersion,
       "gs2328FirmwareVersion": gs2328FirmwareVersion,
       "gs2328HardwareMechanicalVersion": gs2328HardwareMechanicalVersion,
       "gs2328SerialNumber": gs2328SerialNumber,
       "gs2328HostMACAddress": gs2328HostMACAddress,
       "gs2328ConsoleBaudrate": gs2328ConsoleBaudrate,
       "gs2328RAMSize": gs2328RAMSize,
       "gs2328FlashSize": gs2328FlashSize,
       "gs2328BridgeFDBSize": gs2328BridgeFDBSize,
       "gs2328TransmitQueue": gs2328TransmitQueue,
       "gs2328MaximumFrameSize": gs2328MaximumFrameSize,
       "gs2328CPULoad": gs2328CPULoad,
       "gs2328FanSpeed": gs2328FanSpeed,
       "gs2328Temperature": gs2328Temperature,
       "gs2328SystemDescription": gs2328SystemDescription,
       "gs2328Location": gs2328Location,
       "gs2328Contact": gs2328Contact,
       "gs2328DeviceName": gs2328DeviceName,
       "gs2328SystemDate": gs2328SystemDate,
       "gs2328SystemUptime": gs2328SystemUptime,
       "gs2328SystemIPv4Address": gs2328SystemIPv4Address,
       "gs2328SystemIPv4SubnetMask": gs2328SystemIPv4SubnetMask,
       "gs2328SystemIPv4Gateway": gs2328SystemIPv4Gateway,
       "gs2328IPv6LinkLocalAddress": gs2328IPv6LinkLocalAddress,
       "gs2328IPv6Address": gs2328IPv6Address,
       "gs2328IPv6Prefix": gs2328IPv6Prefix,
       "gs2328IPv6Gateway": gs2328IPv6Gateway,
       "gs2328LargestFreeMemBlock": gs2328LargestFreeMemBlock,
       "gs2328MemFree": gs2328MemFree,
       "gs2328SystemTime": gs2328SystemTime,
       "gs2328SystemTimeManual": gs2328SystemTimeManual,
       "gs2328SystemTimeManualClockSource": gs2328SystemTimeManualClockSource,
       "gs2328SystemTimeManualLocaltime": gs2328SystemTimeManualLocaltime,
       "gs2328SystemTimeManualTimeZoneOffset": gs2328SystemTimeManualTimeZoneOffset,
       "gs2328SystemTimeManualDaylightSavings": gs2328SystemTimeManualDaylightSavings,
       "gs2328SystemTimeManualTimeSetOffset": gs2328SystemTimeManualTimeSetOffset,
       "gs2328SystemTimeManualDaylightSavingsType": gs2328SystemTimeManualDaylightSavingsType,
       "gs2328SystemTimeManualDaylightSavingsBydatesFrom": gs2328SystemTimeManualDaylightSavingsBydatesFrom,
       "gs2328SystemTimeManualDaylightSavingsBydatesTo": gs2328SystemTimeManualDaylightSavingsBydatesTo,
       "gs2328SystemTimeManualDaylightSavingsRecurringDayFrom": gs2328SystemTimeManualDaylightSavingsRecurringDayFrom,
       "gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom": gs2328SystemTimeManualDaylightSavingsRecurringWeekFrom,
       "gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom": gs2328SystemTimeManualDaylightSavingsRecurringMonthFrom,
       "gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom": gs2328SystemTimeManualDaylightSavingsRecurringTimeFrom,
       "gs2328SystemTimeManualDaylightSavingsRecurringDayTo": gs2328SystemTimeManualDaylightSavingsRecurringDayTo,
       "gs2328SystemTimeManualDaylightSavingsRecurringWeekTo": gs2328SystemTimeManualDaylightSavingsRecurringWeekTo,
       "gs2328SystemTimeManualDaylightSavingsRecurringMonthTo": gs2328SystemTimeManualDaylightSavingsRecurringMonthTo,
       "gs2328SystemTimeManualDaylightSavingsRecurringTimeTo": gs2328SystemTimeManualDaylightSavingsRecurringTimeTo,
       "gs2328SystemTimeNTP": gs2328SystemTimeNTP,
       "gs2328SystemTimeNTPTable": gs2328SystemTimeNTPTable,
       "gs2328SystemTimeNTPEntry": gs2328SystemTimeNTPEntry,
       "gs2328SystemTimeNTPIndex": gs2328SystemTimeNTPIndex,
       "gs2328SystemTimeNTPServerIPType": gs2328SystemTimeNTPServerIPType,
       "gs2328SystemTimeNTPServer": gs2328SystemTimeNTPServer,
       "gs2328SystemTimeNTPCurrentMode": gs2328SystemTimeNTPCurrentMode,
       "gs2328SystemTimeNTPRequestInterval": gs2328SystemTimeNTPRequestInterval,
       "gs2328SystemTimeNTPTriesNumber": gs2328SystemTimeNTPTriesNumber,
       "gs2328SystemAccount": gs2328SystemAccount,
       "gs2328SystemAccountUsers": gs2328SystemAccountUsers,
       "gs2328SystemAccountUserCreate": gs2328SystemAccountUserCreate,
       "gs2328SystemAccountUsersTable": gs2328SystemAccountUsersTable,
       "gs2328SystemAccountUsersEntry": gs2328SystemAccountUsersEntry,
       "gs2328UserIndex": gs2328UserIndex,
       "gs2328UserName": gs2328UserName,
       "gs2328Password": gs2328Password,
       "gs2328UserPrivilegeLevel": gs2328UserPrivilegeLevel,
       "gs2328AccountUserRowStatus": gs2328AccountUserRowStatus,
       "gs2328SystemAccountUsersSuperUserPassword": gs2328SystemAccountUsersSuperUserPassword,
       "gs2328SystemAccountEnforcePasswordRules": gs2328SystemAccountEnforcePasswordRules,
       "gs2328SystemAccountPrivilegeLevel": gs2328SystemAccountPrivilegeLevel,
       "gs2328AccountPrivilegeLevel": gs2328AccountPrivilegeLevel,
       "gs2328AggregationPrivilegeLevel": gs2328AggregationPrivilegeLevel,
       "gs2328DiagnosticsPrivilegeLevel": gs2328DiagnosticsPrivilegeLevel,
       "gs2328EEEPrivilegeLevel": gs2328EEEPrivilegeLevel,
       "gs2328EasyportPrivilegeLevel": gs2328EasyportPrivilegeLevel,
       "gs2328GARPPrivilegeLevel": gs2328GARPPrivilegeLevel,
       "gs2328GVRPPrivilegeLevel": gs2328GVRPPrivilegeLevel,
       "gs2328IPPrivilegeLevel": gs2328IPPrivilegeLevel,
       "gs2328IPMCSnoopingPrivilegeLevel": gs2328IPMCSnoopingPrivilegeLevel,
       "gs2328LACPPrivilegeLevel": gs2328LACPPrivilegeLevel,
       "gs2328LLDPPrivilegeLevel": gs2328LLDPPrivilegeLevel,
       "gs2328LLDPMEDPrivilegeLevel": gs2328LLDPMEDPrivilegeLevel,
       "gs2328LoopProtectPrivilegeLevel": gs2328LoopProtectPrivilegeLevel,
       "gs2328MACTablePrivilegeLevel": gs2328MACTablePrivilegeLevel,
       "gs2328MVRPrivilegeLevel": gs2328MVRPrivilegeLevel,
       "gs2328MaintenancePrivilegeLevel": gs2328MaintenancePrivilegeLevel,
       "gs2328MirroringPrivilegeLevel": gs2328MirroringPrivilegeLevel,
       "gs2328PortsPrivilegeLevel": gs2328PortsPrivilegeLevel,
       "gs2328PrivateVLANsPrivilegeLevel": gs2328PrivateVLANsPrivilegeLevel,
       "gs2328QoSPrivilegeLevel": gs2328QoSPrivilegeLevel,
       "gs2328SFlowPrivilegeLevel": gs2328SFlowPrivilegeLevel,
       "gs2328SMTPPrivilegeLevel": gs2328SMTPPrivilegeLevel,
       "gs2328SNMPPrivilegeLevel": gs2328SNMPPrivilegeLevel,
       "gs2328SecurityPrivilegeLevel": gs2328SecurityPrivilegeLevel,
       "gs2328SingleIPPrivilegeLevel": gs2328SingleIPPrivilegeLevel,
       "gs2328SpanningTreePrivilegeLevel": gs2328SpanningTreePrivilegeLevel,
       "gs2328SystemPrivilegeLevel": gs2328SystemPrivilegeLevel,
       "gs2328TrapEventPrivilegeLevel": gs2328TrapEventPrivilegeLevel,
       "gs2328UPnPPrivilegeLevel": gs2328UPnPPrivilegeLevel,
       "gs2328VCLPrivilegeLevel": gs2328VCLPrivilegeLevel,
       "gs2328VLANsPrivilegeLevel": gs2328VLANsPrivilegeLevel,
       "gs2328VoiceVLANPrivilegeLevel": gs2328VoiceVLANPrivilegeLevel,
       "gs2328IP": gs2328IP,
       "gs2328IPv4": gs2328IPv4,
       "gs2328IPv4Configured": gs2328IPv4Configured,
       "gs2328Ipv4DHCPClient": gs2328Ipv4DHCPClient,
       "gs2328IPv4Address": gs2328IPv4Address,
       "gs2328IPv4Mask": gs2328IPv4Mask,
       "gs2328IPv4Gateway": gs2328IPv4Gateway,
       "gs2328IPv4VLANId": gs2328IPv4VLANId,
       "gs2328IPv4DNSServer": gs2328IPv4DNSServer,
       "gs2328IPv4DNSProxy": gs2328IPv4DNSProxy,
       "gs2328IPv4Current": gs2328IPv4Current,
       "gs2328Ipv4CurrentDHCPClient": gs2328Ipv4CurrentDHCPClient,
       "gs2328IPv4CurrentAddress": gs2328IPv4CurrentAddress,
       "gs2328IPv4CurrentMask": gs2328IPv4CurrentMask,
       "gs2328IPv4CurrentGateway": gs2328IPv4CurrentGateway,
       "gs2328IPv4CurrentVLANId": gs2328IPv4CurrentVLANId,
       "gs2328IPv4CurrentDNSServer": gs2328IPv4CurrentDNSServer,
       "gs2328IPv6": gs2328IPv6,
       "gs2328IPv6Configured": gs2328IPv6Configured,
       "gs2328Ipv6AutoConfiguration": gs2328Ipv6AutoConfiguration,
       "gs2328Ipv6Address": gs2328Ipv6Address,
       "gs2328Ipv6Prefix": gs2328Ipv6Prefix,
       "gs2328Ipv6Gateway": gs2328Ipv6Gateway,
       "gs2328IPv6Current": gs2328IPv6Current,
       "gs2328Ipv6CurrentAutoConfiguration": gs2328Ipv6CurrentAutoConfiguration,
       "gs2328Ipv6CurrentAddress": gs2328Ipv6CurrentAddress,
       "gs2328Ipv6CurrentLinkLocalAddress": gs2328Ipv6CurrentLinkLocalAddress,
       "gs2328Ipv6CurrentPrefix": gs2328Ipv6CurrentPrefix,
       "gs2328Ipv6CurrentGateway": gs2328Ipv6CurrentGateway,
       "gs2328Syslog": gs2328Syslog,
       "gs2328SyslogConf": gs2328SyslogConf,
       "gs2328ServerMode": gs2328ServerMode,
       "gs2328ServerAddress1": gs2328ServerAddress1,
       "gs2328ServerAddress2": gs2328ServerAddress2,
       "gs2328SyslogLevel": gs2328SyslogLevel,
       "gs2328SyslogDetailedInfo": gs2328SyslogDetailedInfo,
       "gs2328SyslogDetailedInfoClear": gs2328SyslogDetailedInfoClear,
       "gs2328SyslogDetailedInfoTable": gs2328SyslogDetailedInfoTable,
       "gs2328SyslogDetailedInfoEntry": gs2328SyslogDetailedInfoEntry,
       "gs2328SyslogDetailedInfoIndex": gs2328SyslogDetailedInfoIndex,
       "gs2328SyslogDetailedInfoLevel": gs2328SyslogDetailedInfoLevel,
       "gs2328SyslogDetailedInfoTime": gs2328SyslogDetailedInfoTime,
       "gs2328SyslogDetailedInfoMessage": gs2328SyslogDetailedInfoMessage,
       "gs2328Snmp": gs2328Snmp,
       "gs2328SnmpConf": gs2328SnmpConf,
       "gs2328GetCommunityMode": gs2328GetCommunityMode,
       "gs2328GetCommunity": gs2328GetCommunity,
       "gs2328SetCommunityMode": gs2328SetCommunityMode,
       "gs2328SetCommunity": gs2328SetCommunity,
       "gs2328GetCommunityConfTable": gs2328GetCommunityConfTable,
       "gs2328GetCommunityConfEntry": gs2328GetCommunityConfEntry,
       "gs2328CommunityConfIndex": gs2328CommunityConfIndex,
       "gs2328CommunityConfGetCommunity": gs2328CommunityConfGetCommunity,
       "gs2328TrapHostConfTable": gs2328TrapHostConfTable,
       "gs2328TrapHostConfEntry": gs2328TrapHostConfEntry,
       "gs2328TrapHostConfIndex": gs2328TrapHostConfIndex,
       "gs2328TrapHostConfVersion": gs2328TrapHostConfVersion,
       "gs2328TrapHostConfIPType": gs2328TrapHostConfIPType,
       "gs2328TrapHostConfIP": gs2328TrapHostConfIP,
       "gs2328TrapHostConfPort": gs2328TrapHostConfPort,
       "gs2328TrapHostConfCommunity": gs2328TrapHostConfCommunity,
       "gs2328TrapHostConfSeverityLevel": gs2328TrapHostConfSeverityLevel,
       "gs2328TrapHostConfSecurityLevel": gs2328TrapHostConfSecurityLevel,
       "gs2328TrapHostConfAuthPtc": gs2328TrapHostConfAuthPtc,
       "gs2328TrapHostConfAuthPassword": gs2328TrapHostConfAuthPassword,
       "gs2328TrapHostConfPrivPtc": gs2328TrapHostConfPrivPtc,
       "gs2328TrapHostConfPrivPassword": gs2328TrapHostConfPrivPassword,
       "gs2328TrapHostConfCurrentMode": gs2328TrapHostConfCurrentMode,
       "gs2328SnmpSystem": gs2328SnmpSystem,
       "gs2328SnmpState": gs2328SnmpState,
       "gs2328SnmpEngineID": gs2328SnmpEngineID,
       "gs2328SnmpCommunities": gs2328SnmpCommunities,
       "gs2328SnmpCommunitiesCreate": gs2328SnmpCommunitiesCreate,
       "gs2328SnmpCommunitiesTable": gs2328SnmpCommunitiesTable,
       "gs2328SnmpCommunitiesEntry": gs2328SnmpCommunitiesEntry,
       "gs2328SnmpCommunitiesIndex": gs2328SnmpCommunitiesIndex,
       "gs2328SnmpCommunitiesCommunity": gs2328SnmpCommunitiesCommunity,
       "gs2328SnmpCommunitiesUserName": gs2328SnmpCommunitiesUserName,
       "gs2328SnmpCommunitiesSourceIP": gs2328SnmpCommunitiesSourceIP,
       "gs2328SnmpCommunitiesSourceMask": gs2328SnmpCommunitiesSourceMask,
       "gs2328SnmpCommunitiesRowStatus": gs2328SnmpCommunitiesRowStatus,
       "gs2328SnmpUsers": gs2328SnmpUsers,
       "gs2328SnmpUsersCreate": gs2328SnmpUsersCreate,
       "gs2328SnmpUsersTable": gs2328SnmpUsersTable,
       "gs2328SnmpUsersEntry": gs2328SnmpUsersEntry,
       "gs2328SnmpUsersIndex": gs2328SnmpUsersIndex,
       "gs2328SnmpUsersUserName": gs2328SnmpUsersUserName,
       "gs2328SnmpUsersSecurityLevel": gs2328SnmpUsersSecurityLevel,
       "gs2328SnmpUsersAuthenticationProtocol": gs2328SnmpUsersAuthenticationProtocol,
       "gs2328SnmpUsersAuthenticationPassword": gs2328SnmpUsersAuthenticationPassword,
       "gs2328SnmpUsersPrivacyProtocol": gs2328SnmpUsersPrivacyProtocol,
       "gs2328SnmpUsersPrivacyPassword": gs2328SnmpUsersPrivacyPassword,
       "gs2328SnmpUsersRowStatus": gs2328SnmpUsersRowStatus,
       "gs2328SnmpGroups": gs2328SnmpGroups,
       "gs2328SnmpGroupsCreate": gs2328SnmpGroupsCreate,
       "gs2328SnmpGroupsTable": gs2328SnmpGroupsTable,
       "gs2328SnmpGroupsEntry": gs2328SnmpGroupsEntry,
       "gs2328SnmpGroupsIndex": gs2328SnmpGroupsIndex,
       "gs2328SnmpGroupsSecurityModel": gs2328SnmpGroupsSecurityModel,
       "gs2328SnmpGroupsSecurityName": gs2328SnmpGroupsSecurityName,
       "gs2328SnmpGroupsGroupName": gs2328SnmpGroupsGroupName,
       "gs2328SnmpGroupsRowStatus": gs2328SnmpGroupsRowStatus,
       "gs2328SnmpViews": gs2328SnmpViews,
       "gs2328SnmpViewsCreate": gs2328SnmpViewsCreate,
       "gs2328SnmpViewsTable": gs2328SnmpViewsTable,
       "gs2328SnmpViewsEntry": gs2328SnmpViewsEntry,
       "gs2328SnmpViewsIndex": gs2328SnmpViewsIndex,
       "gs2328SnmpViewsName": gs2328SnmpViewsName,
       "gs2328SnmpViewsType": gs2328SnmpViewsType,
       "gs2328SnmpViewsOIDSubtree": gs2328SnmpViewsOIDSubtree,
       "gs2328SnmpViewsRowStatus": gs2328SnmpViewsRowStatus,
       "gs2328SnmpAccess": gs2328SnmpAccess,
       "gs2328SnmpAccessCreate": gs2328SnmpAccessCreate,
       "gs2328SnmpAccessTable": gs2328SnmpAccessTable,
       "gs2328SnmpAccessEntry": gs2328SnmpAccessEntry,
       "gs2328SnmpAccessIndex": gs2328SnmpAccessIndex,
       "gs2328SnmpAccessGroupName": gs2328SnmpAccessGroupName,
       "gs2328SnmpAccessSecurityModel": gs2328SnmpAccessSecurityModel,
       "gs2328SnmpAccessSecurityLevel": gs2328SnmpAccessSecurityLevel,
       "gs2328SnmpAccessReadViewName": gs2328SnmpAccessReadViewName,
       "gs2328SnmpAccessWriteViewName": gs2328SnmpAccessWriteViewName,
       "gs2328SnmpAccessRowStatus": gs2328SnmpAccessRowStatus,
       "gs2328Configuration": gs2328Configuration,
       "gs2328Port": gs2328Port,
       "gs2328PortConfigurationTable": gs2328PortConfigurationTable,
       "gs2328PortConfigurationEntry": gs2328PortConfigurationEntry,
       "gs2328PortConfPort": gs2328PortConfPort,
       "gs2328PortConfPortMedia": gs2328PortConfPortMedia,
       "gs2328PortConfLink": gs2328PortConfLink,
       "gs2328PortConfCurrentSpeed": gs2328PortConfCurrentSpeed,
       "gs2328PortConfSpeed": gs2328PortConfSpeed,
       "gs2328PortConfCurrentFlowControlRx": gs2328PortConfCurrentFlowControlRx,
       "gs2328PortConfCurrentFlowControlTx": gs2328PortConfCurrentFlowControlTx,
       "gs2328PortConfFlowControl": gs2328PortConfFlowControl,
       "gs2328PortConfMaxFrameSize": gs2328PortConfMaxFrameSize,
       "gs2328PortConfExcessiveCollisionMode": gs2328PortConfExcessiveCollisionMode,
       "gs2328PortConfPowerControl": gs2328PortConfPowerControl,
       "gs2328PortConfDescription": gs2328PortConfDescription,
       "gs2328PortTrafficStatisticsTable": gs2328PortTrafficStatisticsTable,
       "gs2328PortTrafficStatisticsEntry": gs2328PortTrafficStatisticsEntry,
       "gs2328PortTrafficStatisticsPort": gs2328PortTrafficStatisticsPort,
       "gs2328PortTrafficStatisticsClear": gs2328PortTrafficStatisticsClear,
       "gs2328PortTrafficRxPackets": gs2328PortTrafficRxPackets,
       "gs2328PortTrafficRxOctets": gs2328PortTrafficRxOctets,
       "gs2328PortTrafficRxUnicast": gs2328PortTrafficRxUnicast,
       "gs2328PortTrafficRxMulticast": gs2328PortTrafficRxMulticast,
       "gs2328PortTrafficRxBroadcast": gs2328PortTrafficRxBroadcast,
       "gs2328PortTrafficRxPause": gs2328PortTrafficRxPause,
       "gs2328PortTrafficRx64Bytes": gs2328PortTrafficRx64Bytes,
       "gs2328PortTrafficRx65to127Bytes": gs2328PortTrafficRx65to127Bytes,
       "gs2328PortTrafficRx128to255Bytes": gs2328PortTrafficRx128to255Bytes,
       "gs2328PortTrafficRx256to511Bytes": gs2328PortTrafficRx256to511Bytes,
       "gs2328PortTrafficRx512to1023Bytes": gs2328PortTrafficRx512to1023Bytes,
       "gs2328PortTrafficRx1024to1526Bytes": gs2328PortTrafficRx1024to1526Bytes,
       "gs2328PortTrafficRxExceecd1527Bytes": gs2328PortTrafficRxExceecd1527Bytes,
       "gs2328PortTrafficRxQ0": gs2328PortTrafficRxQ0,
       "gs2328PortTrafficRxQ1": gs2328PortTrafficRxQ1,
       "gs2328PortTrafficRxQ2": gs2328PortTrafficRxQ2,
       "gs2328PortTrafficRxQ3": gs2328PortTrafficRxQ3,
       "gs2328PortTrafficRxQ4": gs2328PortTrafficRxQ4,
       "gs2328PortTrafficRxQ5": gs2328PortTrafficRxQ5,
       "gs2328PortTrafficRxQ6": gs2328PortTrafficRxQ6,
       "gs2328PortTrafficRxQ7": gs2328PortTrafficRxQ7,
       "gs2328PortTrafficRxDrops": gs2328PortTrafficRxDrops,
       "gs2328PortTrafficRxCRCorAlignment": gs2328PortTrafficRxCRCorAlignment,
       "gs2328PortTrafficRxUndersize": gs2328PortTrafficRxUndersize,
       "gs2328PortTrafficRxOversize": gs2328PortTrafficRxOversize,
       "gs2328PortTrafficRxFragments": gs2328PortTrafficRxFragments,
       "gs2328PortTrafficRxJabber": gs2328PortTrafficRxJabber,
       "gs2328PortTrafficRxFiltered": gs2328PortTrafficRxFiltered,
       "gs2328PortTrafficTxPackets": gs2328PortTrafficTxPackets,
       "gs2328PortTrafficTxOctets": gs2328PortTrafficTxOctets,
       "gs2328PortTrafficTxUnicast": gs2328PortTrafficTxUnicast,
       "gs2328PortTrafficTxMulticast": gs2328PortTrafficTxMulticast,
       "gs2328PortTrafficTxBroadcast": gs2328PortTrafficTxBroadcast,
       "gs2328PortTrafficTxPause": gs2328PortTrafficTxPause,
       "gs2328PortTrafficTx64Bytes": gs2328PortTrafficTx64Bytes,
       "gs2328PortTrafficTx65to127Bytes": gs2328PortTrafficTx65to127Bytes,
       "gs2328PortTrafficTx128to255Bytes": gs2328PortTrafficTx128to255Bytes,
       "gs2328PortTrafficTx256to511Bytes": gs2328PortTrafficTx256to511Bytes,
       "gs2328PortTrafficTx512to1023Bytes": gs2328PortTrafficTx512to1023Bytes,
       "gs2328PortTrafficTx1024to1526Bytes": gs2328PortTrafficTx1024to1526Bytes,
       "gs2328PortTrafficTxExceecd1527Bytes": gs2328PortTrafficTxExceecd1527Bytes,
       "gs2328PortTrafficTxQ0": gs2328PortTrafficTxQ0,
       "gs2328PortTrafficTxQ1": gs2328PortTrafficTxQ1,
       "gs2328PortTrafficTxQ2": gs2328PortTrafficTxQ2,
       "gs2328PortTrafficTxQ3": gs2328PortTrafficTxQ3,
       "gs2328PortTrafficTxQ4": gs2328PortTrafficTxQ4,
       "gs2328PortTrafficTxQ5": gs2328PortTrafficTxQ5,
       "gs2328PortTrafficTxQ6": gs2328PortTrafficTxQ6,
       "gs2328PortTrafficTxQ7": gs2328PortTrafficTxQ7,
       "gs2328PortTrafficTxDrops": gs2328PortTrafficTxDrops,
       "gs2328PortTrafficTxLateOrExcColl": gs2328PortTrafficTxLateOrExcColl,
       "gs2328PortQoSStatistics": gs2328PortQoSStatistics,
       "gs2328PortQoSStatisticsClear": gs2328PortQoSStatisticsClear,
       "gs2328PortQoSStatisticsTable": gs2328PortQoSStatisticsTable,
       "gs2328PortQoSStatisticsEntry": gs2328PortQoSStatisticsEntry,
       "gs2328PortQoSStatisticsPort": gs2328PortQoSStatisticsPort,
       "gs2328PortQoSQ0Rx": gs2328PortQoSQ0Rx,
       "gs2328PortQoSQ0Tx": gs2328PortQoSQ0Tx,
       "gs2328PortQoSQ1Rx": gs2328PortQoSQ1Rx,
       "gs2328PortQoSQ1Tx": gs2328PortQoSQ1Tx,
       "gs2328PortQoSQ2Rx": gs2328PortQoSQ2Rx,
       "gs2328PortQoSQ2Tx": gs2328PortQoSQ2Tx,
       "gs2328PortQoSQ3Rx": gs2328PortQoSQ3Rx,
       "gs2328PortQoSQ3Tx": gs2328PortQoSQ3Tx,
       "gs2328PortQoSQ4Rx": gs2328PortQoSQ4Rx,
       "gs2328PortQoSQ4Tx": gs2328PortQoSQ4Tx,
       "gs2328PortQoSQ5Rx": gs2328PortQoSQ5Rx,
       "gs2328PortQoSQ5Tx": gs2328PortQoSQ5Tx,
       "gs2328PortQoSQ6Rx": gs2328PortQoSQ6Rx,
       "gs2328PortQoSQ6Tx": gs2328PortQoSQ6Tx,
       "gs2328PortQoSQ7Rx": gs2328PortQoSQ7Rx,
       "gs2328PortQoSQ7Tx": gs2328PortQoSQ7Tx,
       "gs2328SFPInfoTable": gs2328SFPInfoTable,
       "gs2328SFPInfoEntry": gs2328SFPInfoEntry,
       "gs2328SFPInfoIndex": gs2328SFPInfoIndex,
       "gs2328SFPInfoPort": gs2328SFPInfoPort,
       "gs2328SFPConnectorType": gs2328SFPConnectorType,
       "gs2328SFPFiberType": gs2328SFPFiberType,
       "gs2328SFPTxCentralWavelength": gs2328SFPTxCentralWavelength,
       "gs2328SFPBaudRate": gs2328SFPBaudRate,
       "gs2328SFPVendorOUI": gs2328SFPVendorOUI,
       "gs2328SFPVendorName": gs2328SFPVendorName,
       "gs2328SFPVendorPN": gs2328SFPVendorPN,
       "gs2328SFPVendorRev": gs2328SFPVendorRev,
       "gs2328SFPVendorSN": gs2328SFPVendorSN,
       "gs2328SFPDateCode": gs2328SFPDateCode,
       "gs2328SFPTemperature": gs2328SFPTemperature,
       "gs2328SFPVcc": gs2328SFPVcc,
       "gs2328SFPMon1Bias": gs2328SFPMon1Bias,
       "gs2328SFPMon2TxPWR": gs2328SFPMon2TxPWR,
       "gs2328SFPMon3RxPWR": gs2328SFPMon3RxPWR,
       "gs2328VoiceVLAN": gs2328VoiceVLAN,
       "gs2328VoiceVLANConf": gs2328VoiceVLANConf,
       "gs2328VoiceVLANMode": gs2328VoiceVLANMode,
       "gs2328VoiceVLANVLANId": gs2328VoiceVLANVLANId,
       "gs2328VoiceVLANAgingTime": gs2328VoiceVLANAgingTime,
       "gs2328VoiceVLANTrafficClass": gs2328VoiceVLANTrafficClass,
       "gs2328VoiceVLANPortTable": gs2328VoiceVLANPortTable,
       "gs2328VoiceVLANPortEntry": gs2328VoiceVLANPortEntry,
       "gs2328VoiceVLANPort": gs2328VoiceVLANPort,
       "gs2328VoiceVLANPortMode": gs2328VoiceVLANPortMode,
       "gs2328VoiceVLANPortSecurity": gs2328VoiceVLANPortSecurity,
       "gs2328VoiceVLANPortDiscoveryProtocol": gs2328VoiceVLANPortDiscoveryProtocol,
       "gs2328VoiceVLANSkipNAS": gs2328VoiceVLANSkipNAS,
       "gs2328VoiceVLANOUI": gs2328VoiceVLANOUI,
       "gs2328VoiceVLANOUICreate": gs2328VoiceVLANOUICreate,
       "gs2328VoiceVLANOUITable": gs2328VoiceVLANOUITable,
       "gs2328VoiceVLANOUIEntry": gs2328VoiceVLANOUIEntry,
       "gs2328VoiceVLANOUIIndex": gs2328VoiceVLANOUIIndex,
       "gs2328VoiceVLANTelephonyOUI": gs2328VoiceVLANTelephonyOUI,
       "gs2328VoiceVLANDescription": gs2328VoiceVLANDescription,
       "gs2328VoiceVLANOUIRowStatus": gs2328VoiceVLANOUIRowStatus,
       "gs2328GARP": gs2328GARP,
       "gs2328GARPConfTable": gs2328GARPConfTable,
       "gs2328GARPConfEntry": gs2328GARPConfEntry,
       "gs2328GARPConfPort": gs2328GARPConfPort,
       "gs2328GARPJoinTimer": gs2328GARPJoinTimer,
       "gs2328GARPLeaveTimer": gs2328GARPLeaveTimer,
       "gs2328GARPLeaveAllTimer": gs2328GARPLeaveAllTimer,
       "gs2328GARPApplicantion": gs2328GARPApplicantion,
       "gs2328GARPAttributeType": gs2328GARPAttributeType,
       "gs2328GARPApplicant": gs2328GARPApplicant,
       "gs2328GARPStatisticsTable": gs2328GARPStatisticsTable,
       "gs2328GARPStatisticsEntry": gs2328GARPStatisticsEntry,
       "gs2328GARPStatisticsPort": gs2328GARPStatisticsPort,
       "gs2328GARPStatisticsPeerMAC": gs2328GARPStatisticsPeerMAC,
       "gs2328GARPStatisticsFailedCount": gs2328GARPStatisticsFailedCount,
       "gs2328GVRP": gs2328GVRP,
       "gs2328GVRPConf": gs2328GVRPConf,
       "gs2328GVRPMode": gs2328GVRPMode,
       "gs2328GVRPConfTable": gs2328GVRPConfTable,
       "gs2328GVRPConfEntry": gs2328GVRPConfEntry,
       "gs2328GVRPConfPort": gs2328GVRPConfPort,
       "gs2328GVRPConfPortMode": gs2328GVRPConfPortMode,
       "gs2328GVRPConfPortRRole": gs2328GVRPConfPortRRole,
       "gs2328GVRPStatisticsTable": gs2328GVRPStatisticsTable,
       "gs2328GVRPStatisticsEntry": gs2328GVRPStatisticsEntry,
       "gs2328GVRPStatisticsPort": gs2328GVRPStatisticsPort,
       "gs2328GVRPStatisticsJoinTxCnt": gs2328GVRPStatisticsJoinTxCnt,
       "gs2328GVRPStatisticsLeaveTxCnt": gs2328GVRPStatisticsLeaveTxCnt,
       "gs2328Mirroring": gs2328Mirroring,
       "gs2328PortToMirrorOn": gs2328PortToMirrorOn,
       "gs2328MirrorTable": gs2328MirrorTable,
       "gs2328MirrorEntry": gs2328MirrorEntry,
       "gs2328MirrorPort": gs2328MirrorPort,
       "gs2328MirrorMode": gs2328MirrorMode,
       "gs2328TrapEventSeverity": gs2328TrapEventSeverity,
       "gs2328TrapEventSeverityACL": gs2328TrapEventSeverityACL,
       "gs2328TrapEventSeverityACLLog": gs2328TrapEventSeverityACLLog,
       "gs2328TrapEventSeverityAccessMgmt": gs2328TrapEventSeverityAccessMgmt,
       "gs2328TrapEventSeverityAuthFailed": gs2328TrapEventSeverityAuthFailed,
       "gs2328TrapEventSeverityColdStart": gs2328TrapEventSeverityColdStart,
       "gs2328TrapEventSeverityConfigInfo": gs2328TrapEventSeverityConfigInfo,
       "gs2328TrapEventSeverityFirmwareUpgrade": gs2328TrapEventSeverityFirmwareUpgrade,
       "gs2328TrapEventSeverityImportExport": gs2328TrapEventSeverityImportExport,
       "gs2328TrapEventSeverityLACP": gs2328TrapEventSeverityLACP,
       "gs2328TrapEventSeverityLinkStatus": gs2328TrapEventSeverityLinkStatus,
       "gs2328TrapEventSeverityLogin": gs2328TrapEventSeverityLogin,
       "gs2328TrapEventSeverityLogout": gs2328TrapEventSeverityLogout,
       "gs2328TrapEventSeverityLoopProtect": gs2328TrapEventSeverityLoopProtect,
       "gs2328TrapEventSeverityMgmtIPChange": gs2328TrapEventSeverityMgmtIPChange,
       "gs2328TrapEventSeverityModuleChange": gs2328TrapEventSeverityModuleChange,
       "gs2328TrapEventSeverityNAS": gs2328TrapEventSeverityNAS,
       "gs2328TrapEventSeverityPasswordChange": gs2328TrapEventSeverityPasswordChange,
       "gs2328TrapEventSeverityPortSecurity": gs2328TrapEventSeverityPortSecurity,
       "gs2328TrapEventSeverityVLAN": gs2328TrapEventSeverityVLAN,
       "gs2328TrapEventSeverityWarmStart": gs2328TrapEventSeverityWarmStart,
       "gs2328TrapEventSeverityARPConflict": gs2328TrapEventSeverityARPConflict,
       "gs2328TrapEventSeveritySpoofingLimit": gs2328TrapEventSeveritySpoofingLimit,
       "gs2328TrapEventSeverityStaticARPConflict": gs2328TrapEventSeverityStaticARPConflict,
       "gs2328SMTP": gs2328SMTP,
       "gs2328SMTPMailServer": gs2328SMTPMailServer,
       "gs2328SMTPUserName": gs2328SMTPUserName,
       "gs2328SMTPPassword": gs2328SMTPPassword,
       "gs2328SMTPServeriryLevel": gs2328SMTPServeriryLevel,
       "gs2328SMTPSender": gs2328SMTPSender,
       "gs2328SMTPReturnPath": gs2328SMTPReturnPath,
       "gs2328SMTPEmailAddress1": gs2328SMTPEmailAddress1,
       "gs2328SMTPEmailAddress2": gs2328SMTPEmailAddress2,
       "gs2328SMTPEmailAddress3": gs2328SMTPEmailAddress3,
       "gs2328SMTPEmailAddress4": gs2328SMTPEmailAddress4,
       "gs2328SMTPEmailAddress5": gs2328SMTPEmailAddress5,
       "gs2328SMTPEmailAddress6": gs2328SMTPEmailAddress6,
       "gs2328ACL": gs2328ACL,
       "gs2328ACLPortsConfTable": gs2328ACLPortsConfTable,
       "gs2328ACLPortsConfEntry": gs2328ACLPortsConfEntry,
       "gs2328ACLPortsConfPort": gs2328ACLPortsConfPort,
       "gs2328ACLPortsConfPolicyID": gs2328ACLPortsConfPolicyID,
       "gs2328ACLPortsConfAction": gs2328ACLPortsConfAction,
       "gs2328ACLPortsConfRateLimiterID": gs2328ACLPortsConfRateLimiterID,
       "gs2328ACLPortsConfPortRedirect": gs2328ACLPortsConfPortRedirect,
       "gs2328ACLPortsConfMirror": gs2328ACLPortsConfMirror,
       "gs2328ACLPortsConfLogging": gs2328ACLPortsConfLogging,
       "gs2328ACLPortsConfShutdown": gs2328ACLPortsConfShutdown,
       "gs2328ACLPortsConfState": gs2328ACLPortsConfState,
       "gs2328ACLPortsConfCounter": gs2328ACLPortsConfCounter,
       "gs2328ACLRateLimiterTable": gs2328ACLRateLimiterTable,
       "gs2328ACLRateLimiterEntry": gs2328ACLRateLimiterEntry,
       "gs2328ACLRateLimiterID": gs2328ACLRateLimiterID,
       "gs2328ACLRateLimiterUnit": gs2328ACLRateLimiterUnit,
       "gs2328ACLRateLimiterRate": gs2328ACLRateLimiterRate,
       "gs2328ACLACE": gs2328ACLACE,
       "gs2328ACLACECreate": gs2328ACLACECreate,
       "gs2328ACLACETable": gs2328ACLACETable,
       "gs2328ACLACEEntry": gs2328ACLACEEntry,
       "gs2328ACLACEIndex": gs2328ACLACEIndex,
       "gs2328ACLACEID": gs2328ACLACEID,
       "gs2328ACLACENextID": gs2328ACLACENextID,
       "gs2328ACLACEIngressPort": gs2328ACLACEIngressPort,
       "gs2328ACLACEPortPolicyNumber": gs2328ACLACEPortPolicyNumber,
       "gs2328ACLACEPortPolicyBitmask": gs2328ACLACEPortPolicyBitmask,
       "gs2328ACLACEFrameType": gs2328ACLACEFrameType,
       "gs2328ACLACEAction": gs2328ACLACEAction,
       "gs2328ACLACEDenyPortRedirect": gs2328ACLACEDenyPortRedirect,
       "gs2328ACLACELogging": gs2328ACLACELogging,
       "gs2328ACLACEMirror": gs2328ACLACEMirror,
       "gs2328ACLACERateLimiter": gs2328ACLACERateLimiter,
       "gs2328ACLACEShutdown": gs2328ACLACEShutdown,
       "gs2328ACLACEVLAN8021QTagged": gs2328ACLACEVLAN8021QTagged,
       "gs2328ACLACEVLANTagPriority": gs2328ACLACEVLANTagPriority,
       "gs2328ACLACEVLANVID": gs2328ACLACEVLANVID,
       "gs2328ACLACEEtherType": gs2328ACLACEEtherType,
       "gs2328ACLACESMAC": gs2328ACLACESMAC,
       "gs2328ACLACEDMACType": gs2328ACLACEDMACType,
       "gs2328ACLACEDMAC": gs2328ACLACEDMAC,
       "gs2328ACLACEArpOpcode": gs2328ACLACEArpOpcode,
       "gs2328ACLACEArpFlagsRequestReply": gs2328ACLACEArpFlagsRequestReply,
       "gs2328ACLACEArpFlagsArpSmac": gs2328ACLACEArpFlagsArpSmac,
       "gs2328ACLACEArpFlagsRarpDmac": gs2328ACLACEArpFlagsRarpDmac,
       "gs2328ACLACEArpFlagsLength": gs2328ACLACEArpFlagsLength,
       "gs2328ACLACEArpFlagsIp": gs2328ACLACEArpFlagsIp,
       "gs2328ACLACEArpFlagsEthernet": gs2328ACLACEArpFlagsEthernet,
       "gs2328ACLACESIPType": gs2328ACLACESIPType,
       "gs2328ACLACESIPIPAddress": gs2328ACLACESIPIPAddress,
       "gs2328ACLACESIPNetworkPrefix": gs2328ACLACESIPNetworkPrefix,
       "gs2328ACLACEDIPType": gs2328ACLACEDIPType,
       "gs2328ACLACEDIPIPAddress": gs2328ACLACEDIPIPAddress,
       "gs2328ACLACEDIPNetworkPrefix": gs2328ACLACEDIPNetworkPrefix,
       "gs2328ACLACEIPProtocol": gs2328ACLACEIPProtocol,
       "gs2328ACLACEIPFlagsTTL": gs2328ACLACEIPFlagsTTL,
       "gs2328ACLACEIPFlagsOptions": gs2328ACLACEIPFlagsOptions,
       "gs2328ACLACEIPFlagsFragment": gs2328ACLACEIPFlagsFragment,
       "gs2328ACLACEICMPType": gs2328ACLACEICMPType,
       "gs2328ACLACEICMPCode": gs2328ACLACEICMPCode,
       "gs2328ACLACESourcePortMin": gs2328ACLACESourcePortMin,
       "gs2328ACLACESourcePortMax": gs2328ACLACESourcePortMax,
       "gs2328ACLACEDestPortMin": gs2328ACLACEDestPortMin,
       "gs2328ACLACEDestPortMax": gs2328ACLACEDestPortMax,
       "gs2328ACLACETCPFlagsFin": gs2328ACLACETCPFlagsFin,
       "gs2328ACLACETCPFlagsSyn": gs2328ACLACETCPFlagsSyn,
       "gs2328ACLACETCPFlagsRst": gs2328ACLACETCPFlagsRst,
       "gs2328ACLACETCPFlagsPsh": gs2328ACLACETCPFlagsPsh,
       "gs2328ACLACETCPFlagsAck": gs2328ACLACETCPFlagsAck,
       "gs2328ACLACETCPFlagsUrg": gs2328ACLACETCPFlagsUrg,
       "gs2328ACLACERowStatus": gs2328ACLACERowStatus,
       "gs2328ACLACEClear": gs2328ACLACEClear,
       "gs2328ACLACEMoveACEID": gs2328ACLACEMoveACEID,
       "gs2328ACLACEMoveNextACEID": gs2328ACLACEMoveNextACEID,
       "gs2328ACLACEStatusTable": gs2328ACLACEStatusTable,
       "gs2328ACLACEStatusEntry": gs2328ACLACEStatusEntry,
       "gs2328ACLACEStatusIndex": gs2328ACLACEStatusIndex,
       "gs2328ACLACEStatusUser": gs2328ACLACEStatusUser,
       "gs2328ACLACEStatusID": gs2328ACLACEStatusID,
       "gs2328ACLACEStatusIngressPort": gs2328ACLACEStatusIngressPort,
       "gs2328ACLACEStatusFrameType": gs2328ACLACEStatusFrameType,
       "gs2328ACLACEStatusAction": gs2328ACLACEStatusAction,
       "gs2328ACLACEStatusRateLimiter": gs2328ACLACEStatusRateLimiter,
       "gs2328ACLACEStatusPortCopy": gs2328ACLACEStatusPortCopy,
       "gs2328ACLACEStatusMirror": gs2328ACLACEStatusMirror,
       "gs2328ACLACEStatusCPU": gs2328ACLACEStatusCPU,
       "gs2328ACLACEStatusCounter": gs2328ACLACEStatusCounter,
       "gs2328ACLACEStatusConflict": gs2328ACLACEStatusConflict,
       "gs2328LoopProtection": gs2328LoopProtection,
       "gs2328LoopProtectionConfig": gs2328LoopProtectionConfig,
       "gs2328LoopProtectionGlobalEnable": gs2328LoopProtectionGlobalEnable,
       "gs2328LoopProtectionTranmisstionTime": gs2328LoopProtectionTranmisstionTime,
       "gs2328LoopProtectionShutdownTime": gs2328LoopProtectionShutdownTime,
       "gs2328LoopProtectionConfigurationTable": gs2328LoopProtectionConfigurationTable,
       "gs2328LoopProtectionConfigurationEntry": gs2328LoopProtectionConfigurationEntry,
       "gs2328LoopProtectionConfPort": gs2328LoopProtectionConfPort,
       "gs2328LoopProtectionConfEnable": gs2328LoopProtectionConfEnable,
       "gs2328LoopProtectionConfAction": gs2328LoopProtectionConfAction,
       "gs2328LoopProtectionConfTxmode": gs2328LoopProtectionConfTxmode,
       "gs2328LoopProtectionStatusTable": gs2328LoopProtectionStatusTable,
       "gs2328LoopProtectionStatusEntry": gs2328LoopProtectionStatusEntry,
       "gs2328LoopProtectionStatusPort": gs2328LoopProtectionStatusPort,
       "gs2328LoopProtectionStatusAction": gs2328LoopProtectionStatusAction,
       "gs2328LoopProtectionStatusTransmit": gs2328LoopProtectionStatusTransmit,
       "gs2328LoopProtectionStatusLoops": gs2328LoopProtectionStatusLoops,
       "gs2328LoopProtectionStatusStatus": gs2328LoopProtectionStatusStatus,
       "gs2328LoopProtectionStatusLoop": gs2328LoopProtectionStatusLoop,
       "gs2328LoopProtectionStatusTimeLastLoop": gs2328LoopProtectionStatusTimeLastLoop,
       "gs2328Qos": gs2328Qos,
       "gs2328QosPortClassification": gs2328QosPortClassification,
       "gs2328QosPortClassificationTable": gs2328QosPortClassificationTable,
       "gs2328QosPortClassificationEntry": gs2328QosPortClassificationEntry,
       "gs2328QosPortClassificationPort": gs2328QosPortClassificationPort,
       "gs2328QosPortClassificationQoSclass": gs2328QosPortClassificationQoSclass,
       "gs2328QosPortClassificationDPlevel": gs2328QosPortClassificationDPlevel,
       "gs2328QosPortClassificationPCP": gs2328QosPortClassificationPCP,
       "gs2328QosPortClassificationDEI": gs2328QosPortClassificationDEI,
       "gs2328QosPortClassificationTagClass": gs2328QosPortClassificationTagClass,
       "gs2328QosPortClassificationDSCPBased": gs2328QosPortClassificationDSCPBased,
       "gs2328QosPortClassificationAddressMode": gs2328QosPortClassificationAddressMode,
       "gs2328QoSIngressPortTagClassificationTable": gs2328QoSIngressPortTagClassificationTable,
       "gs2328QoSIngressPortTagClassificationEntry": gs2328QoSIngressPortTagClassificationEntry,
       "gs2328QoSIngressPortTagClassificationPort": gs2328QoSIngressPortTagClassificationPort,
       "gs2328QoSIngressPortTagPCP": gs2328QoSIngressPortTagPCP,
       "gs2328QoSIngressPortTagDEI": gs2328QoSIngressPortTagDEI,
       "gs2328QoSIngressPortTagQosClass": gs2328QoSIngressPortTagQosClass,
       "gs2328QoSIngressPortTagDPLevel": gs2328QoSIngressPortTagDPLevel,
       "gs2328QosPortPolicingTable": gs2328QosPortPolicingTable,
       "gs2328QosPortPolicingEntry": gs2328QosPortPolicingEntry,
       "gs2328QosPortPolicingPort": gs2328QosPortPolicingPort,
       "gs2328QosPortPolicingMode": gs2328QosPortPolicingMode,
       "gs2328QosPortPolicingRate": gs2328QosPortPolicingRate,
       "gs2328QosPortPolicingUnit": gs2328QosPortPolicingUnit,
       "gs2328QosPortPolicingFlowControl": gs2328QosPortPolicingFlowControl,
       "gs2328QosPortScheduler": gs2328QosPortScheduler,
       "gs2328QosPortSchedulerModeTable": gs2328QosPortSchedulerModeTable,
       "gs2328QosPortSchedulerModeEntry": gs2328QosPortSchedulerModeEntry,
       "gs2328QosSchedulerModePort": gs2328QosSchedulerModePort,
       "gs2328QosSchedulerMode": gs2328QosSchedulerMode,
       "gs2328QosSchedulerShaper": gs2328QosSchedulerShaper,
       "gs2328QosSchedulerShaperRate": gs2328QosSchedulerShaperRate,
       "gs2328QosPortSchedulerTable": gs2328QosPortSchedulerTable,
       "gs2328QosPortSchedulerEntry": gs2328QosPortSchedulerEntry,
       "gs2328QosSchedulerPort": gs2328QosSchedulerPort,
       "gs2328QosSchedulerPortQueue": gs2328QosSchedulerPortQueue,
       "gs2328QosSchedulerPortQueueShaper": gs2328QosSchedulerPortQueueShaper,
       "gs2328QosSchedulerPortQueueShaperRate": gs2328QosSchedulerPortQueueShaperRate,
       "gs2328QosSchedulerPortQueueShaperExcess": gs2328QosSchedulerPortQueueShaperExcess,
       "gs2328QosSchedulerPortQueueSchedulerWeight": gs2328QosSchedulerPortQueueSchedulerWeight,
       "gs2328QosSchedulerPortQueueSchedulerPercent": gs2328QosSchedulerPortQueueSchedulerPercent,
       "gs2328QosPortEgressTagRemarking": gs2328QosPortEgressTagRemarking,
       "gs2328QosPortEgressTagRemarkingTable": gs2328QosPortEgressTagRemarkingTable,
       "gs2328QosPortEgressTagRemarkingEntry": gs2328QosPortEgressTagRemarkingEntry,
       "gs2328QosEgressTagRemarkingPort": gs2328QosEgressTagRemarkingPort,
       "gs2328QosEgressTagRemarkingMode": gs2328QosEgressTagRemarkingMode,
       "gs2328QosPortEgressTagRemarkingDefTable": gs2328QosPortEgressTagRemarkingDefTable,
       "gs2328QosPortEgressTagRemarkingDefEntry": gs2328QosPortEgressTagRemarkingDefEntry,
       "gs2328QosEgressTagRemarkingDefPort": gs2328QosEgressTagRemarkingDefPort,
       "gs2328QosEgressTagRemarkingDefPCP": gs2328QosEgressTagRemarkingDefPCP,
       "gs2328QosEgressTagRemarkingDefDEI": gs2328QosEgressTagRemarkingDefDEI,
       "gs2328QosPortEgressTagRemarkingMapTable": gs2328QosPortEgressTagRemarkingMapTable,
       "gs2328QosPortEgressTagRemarkingMapEntry": gs2328QosPortEgressTagRemarkingMapEntry,
       "gs2328QosPortEgressTagRemarkingMapPort": gs2328QosPortEgressTagRemarkingMapPort,
       "gs2328QosTagRemarkingQoSClass": gs2328QosTagRemarkingQoSClass,
       "gs2328QosTagRemarkingDPLevel": gs2328QosTagRemarkingDPLevel,
       "gs2328QosTagRemarkingPCP": gs2328QosTagRemarkingPCP,
       "gs2328QosTagRemarkingDEI": gs2328QosTagRemarkingDEI,
       "gs2328QosPortDSCPTable": gs2328QosPortDSCPTable,
       "gs2328QosPortDSCPEntry": gs2328QosPortDSCPEntry,
       "gs2328QosPortDSCPPort": gs2328QosPortDSCPPort,
       "gs2328QosPortDSCPIngressTranslate": gs2328QosPortDSCPIngressTranslate,
       "gs2328QosPortDSCPIngressClassify": gs2328QosPortDSCPIngressClassify,
       "gs2328QosPortDSCPEgressRewrite": gs2328QosPortDSCPEgressRewrite,
       "gs2328QosDSCPTable": gs2328QosDSCPTable,
       "gs2328QosDSCPEntry": gs2328QosDSCPEntry,
       "gs2328QosDSCPList": gs2328QosDSCPList,
       "gs2328QosDSCP": gs2328QosDSCP,
       "gs2328QosDSCPTrust": gs2328QosDSCPTrust,
       "gs2328QosDSCPQosClass": gs2328QosDSCPQosClass,
       "gs2328QosDSCPDPL": gs2328QosDSCPDPL,
       "gs2328QosDSCPTranslationTable": gs2328QosDSCPTranslationTable,
       "gs2328QosDSCPTranslationEntry": gs2328QosDSCPTranslationEntry,
       "gs2328QosDSCPTranslationList": gs2328QosDSCPTranslationList,
       "gs2328QosDSCPTranslationDSCPBasedId": gs2328QosDSCPTranslationDSCPBasedId,
       "gs2328QosDSCPTranslationIngressTranslate": gs2328QosDSCPTranslationIngressTranslate,
       "gs2328QosDSCPTranslationIngressClassify": gs2328QosDSCPTranslationIngressClassify,
       "gs2328QosDSCPTranslationEgressRemapDP0": gs2328QosDSCPTranslationEgressRemapDP0,
       "gs2328QosDSCPTranslationEgressRemapDP1": gs2328QosDSCPTranslationEgressRemapDP1,
       "gs2328QosDSCPClassificationTable": gs2328QosDSCPClassificationTable,
       "gs2328QosDSCPClassificationEntry": gs2328QosDSCPClassificationEntry,
       "gs2328QosDSCPClassificationQoSClass": gs2328QosDSCPClassificationQoSClass,
       "gs2328QosDSCPClassificationDPL": gs2328QosDSCPClassificationDPL,
       "gs2328QosDSCPClassificationDSCP": gs2328QosDSCPClassificationDSCP,
       "gs2328QosControlList": gs2328QosControlList,
       "gs2328QosQceCreate": gs2328QosQceCreate,
       "gs2328QosQceTable": gs2328QosQceTable,
       "gs2328QosQceEntry": gs2328QosQceEntry,
       "gs2328QosQceIndex": gs2328QosQceIndex,
       "gs2328QosQceID": gs2328QosQceID,
       "gs2328QosQceNextID": gs2328QosQceNextID,
       "gs2328QosQcePortMembers": gs2328QosQcePortMembers,
       "gs2328QosQceTag": gs2328QosQceTag,
       "gs2328QosQceVID": gs2328QosQceVID,
       "gs2328QosPCP": gs2328QosPCP,
       "gs2328QosDEI": gs2328QosDEI,
       "gs2328QosSMAC": gs2328QosSMAC,
       "gs2328QosDMACType": gs2328QosDMACType,
       "gs2328QosFrameType": gs2328QosFrameType,
       "gs2328QosMacEtherType": gs2328QosMacEtherType,
       "gs2328QosLLCSSAPAddr": gs2328QosLLCSSAPAddr,
       "gs2328QosLLCDSAPAddr": gs2328QosLLCDSAPAddr,
       "gs2328QosLLCControl": gs2328QosLLCControl,
       "gs2328QosSNAPPID": gs2328QosSNAPPID,
       "gs2328QosIpv4Protocol": gs2328QosIpv4Protocol,
       "gs2328QosIpv4ProtocolValue": gs2328QosIpv4ProtocolValue,
       "gs2328QosIpv4ProtocolUDPSport": gs2328QosIpv4ProtocolUDPSport,
       "gs2328QosIpv4ProtocolUDPDport": gs2328QosIpv4ProtocolUDPDport,
       "gs2328QosIpv4ProtocolTCPSport": gs2328QosIpv4ProtocolTCPSport,
       "gs2328QosIpv4ProtocolTCPDport": gs2328QosIpv4ProtocolTCPDport,
       "gs2328QosIpv4Ip": gs2328QosIpv4Ip,
       "gs2328QosIpv4Mask": gs2328QosIpv4Mask,
       "gs2328QosIpv4IPFragment": gs2328QosIpv4IPFragment,
       "gs2328QosIpv4DSCP": gs2328QosIpv4DSCP,
       "gs2328QosIpv6Protocol": gs2328QosIpv6Protocol,
       "gs2328QosIpv6ProtocolValue": gs2328QosIpv6ProtocolValue,
       "gs2328QosIpv6ProtocolUDPSport": gs2328QosIpv6ProtocolUDPSport,
       "gs2328QosIpv6ProtocolUDPDport": gs2328QosIpv6ProtocolUDPDport,
       "gs2328QosIpv6ProtocolTCPSport": gs2328QosIpv6ProtocolTCPSport,
       "gs2328QosIpv6ProtocolTCPDport": gs2328QosIpv6ProtocolTCPDport,
       "gs2328QosIpv6Ip": gs2328QosIpv6Ip,
       "gs2328QosIpv6Mask": gs2328QosIpv6Mask,
       "gs2328QosIpv6DSCP": gs2328QosIpv6DSCP,
       "gs2328QosActionClass": gs2328QosActionClass,
       "gs2328QosActionDPL": gs2328QosActionDPL,
       "gs2328QosActionDSCP": gs2328QosActionDSCP,
       "gs2328QosQceRowStatus": gs2328QosQceRowStatus,
       "gs2328QosQceMoveID": gs2328QosQceMoveID,
       "gs2328QosQceMoveNextID": gs2328QosQceMoveNextID,
       "gs2328QosQCLStatusTable": gs2328QosQCLStatusTable,
       "gs2328QosQCLStatusEntry": gs2328QosQCLStatusEntry,
       "gs2328QosQCLStatusList": gs2328QosQCLStatusList,
       "gs2328QosQCLStatusUser": gs2328QosQCLStatusUser,
       "gs2328QosQCLStatusQCEId": gs2328QosQCLStatusQCEId,
       "gs2328QosQCLStatusFrameType": gs2328QosQCLStatusFrameType,
       "gs2328QosQCLStatusPortlist": gs2328QosQCLStatusPortlist,
       "gs2328QosQCLStatusActionClass": gs2328QosQCLStatusActionClass,
       "gs2328QosQCLStatusActionDPL": gs2328QosQCLStatusActionDPL,
       "gs2328QosQCLStatusActionDSCP": gs2328QosQCLStatusActionDSCP,
       "gs2328QosQCLStatusActionConflict": gs2328QosQCLStatusActionConflict,
       "gs2328QosStormControl": gs2328QosStormControl,
       "gs2328QoSStormControlUC": gs2328QoSStormControlUC,
       "gs2328QoSStormControlUCRate": gs2328QoSStormControlUCRate,
       "gs2328QoSStormControlMC": gs2328QoSStormControlMC,
       "gs2328QoSStormControlMCRate": gs2328QoSStormControlMCRate,
       "gs2328QoSStormControlBC": gs2328QoSStormControlBC,
       "gs2328QoSStormControlBCRate": gs2328QoSStormControlBCRate,
       "gs2328Vlan": gs2328Vlan,
       "gs2328VlanPorts": gs2328VlanPorts,
       "gs2328VlanPortsTPIDforCustomSport": gs2328VlanPortsTPIDforCustomSport,
       "gs2328VlanPortsTable": gs2328VlanPortsTable,
       "gs2328VlanPortsEntry": gs2328VlanPortsEntry,
       "gs2328VlanPortsPort": gs2328VlanPortsPort,
       "gs2328VlanPortsPVID": gs2328VlanPortsPVID,
       "gs2328VlanPortsFrameType": gs2328VlanPortsFrameType,
       "gs2328VlanPortsIngressFilter": gs2328VlanPortsIngressFilter,
       "gs2328VlanPortsEgressRule": gs2328VlanPortsEgressRule,
       "gs2328VlanPortsPortType": gs2328VlanPortsPortType,
       "gs2328VlanPrivateVLAN": gs2328VlanPrivateVLAN,
       "gs2328VlanPrivateVLANMembership": gs2328VlanPrivateVLANMembership,
       "gs2328VlanPrivateVLANMembershipCreate": gs2328VlanPrivateVLANMembershipCreate,
       "gs2328VlanPrivateVLANMembershipTable": gs2328VlanPrivateVLANMembershipTable,
       "gs2328VlanPrivateVLANMembershipEntry": gs2328VlanPrivateVLANMembershipEntry,
       "gs2328VlanPrivateVLANIndex": gs2328VlanPrivateVLANIndex,
       "gs2328VlanPrivateVLANID": gs2328VlanPrivateVLANID,
       "gs2328VlanPrivateVLANMemberships": gs2328VlanPrivateVLANMemberships,
       "gs2328VlanPrivateVLANRowStatus": gs2328VlanPrivateVLANRowStatus,
       "gs2328VlanPortIsolationTable": gs2328VlanPortIsolationTable,
       "gs2328VlanPortIsolationEntry": gs2328VlanPortIsolationEntry,
       "gs2328VlanPortIsolationPort": gs2328VlanPortIsolationPort,
       "gs2328VlanPortIsolation": gs2328VlanPortIsolation,
       "gs2328MACbasedVLAN": gs2328MACbasedVLAN,
       "gs2328MACbasedVLANConf": gs2328MACbasedVLANConf,
       "gs2328MACbasedVLANConfCreate": gs2328MACbasedVLANConfCreate,
       "gs2328MACbasedVLANConfTable": gs2328MACbasedVLANConfTable,
       "gs2328MACbasedVLANConfEntry": gs2328MACbasedVLANConfEntry,
       "gs2328MACbasedVLANIndex": gs2328MACbasedVLANIndex,
       "gs2328MACbasedVLANMACAddress": gs2328MACbasedVLANMACAddress,
       "gs2328MACbasedVLANID": gs2328MACbasedVLANID,
       "gs2328MACbasedMemberships": gs2328MACbasedMemberships,
       "gs2328MACbaseRowStatus": gs2328MACbaseRowStatus,
       "gs2328IGMPSnooping": gs2328IGMPSnooping,
       "gs2328IGMPSnoopingBasic": gs2328IGMPSnoopingBasic,
       "gs2328IGMPSnoopingEnable": gs2328IGMPSnoopingEnable,
       "gs2328IGMPSnoopingUnregisteredIPMCv4Flooding": gs2328IGMPSnoopingUnregisteredIPMCv4Flooding,
       "gs2328IGMPSnoopingSSMIPRangeAddr": gs2328IGMPSnoopingSSMIPRangeAddr,
       "gs2328IGMPSnoopingSSMIPRangeValue": gs2328IGMPSnoopingSSMIPRangeValue,
       "gs2328IGMPSnoopingProxyEnabled": gs2328IGMPSnoopingProxyEnabled,
       "gs2328IGMPSnoopingPortRelatedTable": gs2328IGMPSnoopingPortRelatedTable,
       "gs2328IGMPSnoopingPortRelatedEntry": gs2328IGMPSnoopingPortRelatedEntry,
       "gs2328IGMPSnoopingRouterPort": gs2328IGMPSnoopingRouterPort,
       "gs2328IGMPSnoopingFastLeave": gs2328IGMPSnoopingFastLeave,
       "gs2328IGMPSnoopingThrottling": gs2328IGMPSnoopingThrottling,
       "gs2328IGMPSnoopingVLANTable": gs2328IGMPSnoopingVLANTable,
       "gs2328IGMPSnoopingVLANEntry": gs2328IGMPSnoopingVLANEntry,
       "gs2328IGMPSnoopingVLANID": gs2328IGMPSnoopingVLANID,
       "gs2328IGMPSnoopingVLANEnable": gs2328IGMPSnoopingVLANEnable,
       "gs2328IGMPSnoopingVLANIGMPQuerier": gs2328IGMPSnoopingVLANIGMPQuerier,
       "gs2328IGMPSnoopingVLANCompatibility": gs2328IGMPSnoopingVLANCompatibility,
       "gs2328IGMPSnoopingVLANRV": gs2328IGMPSnoopingVLANRV,
       "gs2328IGMPSnoopingVLANQI": gs2328IGMPSnoopingVLANQI,
       "gs2328IGMPSnoopingVLANQRI": gs2328IGMPSnoopingVLANQRI,
       "gs2328IGMPSnoopingVLANLLQI": gs2328IGMPSnoopingVLANLLQI,
       "gs2328IGMPSnoopingVLANURI": gs2328IGMPSnoopingVLANURI,
       "gs2328IGMPSnoopingPortGroupFiltering": gs2328IGMPSnoopingPortGroupFiltering,
       "gs2328IGMPSnoopingPortGroupFilteringCreate": gs2328IGMPSnoopingPortGroupFilteringCreate,
       "gs2328IGMPSnoopingPortGroupFilteringTable": gs2328IGMPSnoopingPortGroupFilteringTable,
       "gs2328IGMPSnoopingPortGroupFilteringEntry": gs2328IGMPSnoopingPortGroupFilteringEntry,
       "gs2328IGMPSnoopingPortGroupFilteringIndex": gs2328IGMPSnoopingPortGroupFilteringIndex,
       "gs2328IGMPSnoopingPortGroupFilteringPort": gs2328IGMPSnoopingPortGroupFilteringPort,
       "gs2328IGMPSnoopingPortGroupFilteringGroups": gs2328IGMPSnoopingPortGroupFilteringGroups,
       "gs2328IGMPSnoopingPortGroupFilteringRowStatus": gs2328IGMPSnoopingPortGroupFilteringRowStatus,
       "gs2328IGMPSnoopingStatus": gs2328IGMPSnoopingStatus,
       "gs2328IGMPSnoopingstatisticClear": gs2328IGMPSnoopingstatisticClear,
       "gs2328IGMPSnoopingstatisticTable": gs2328IGMPSnoopingstatisticTable,
       "gs2328IGMPSnoopingstatisticEntry": gs2328IGMPSnoopingstatisticEntry,
       "gs2328IGMPSnoopingstatisticVLANID": gs2328IGMPSnoopingstatisticVLANID,
       "gs2328IGMPSnoopingstatisticQuerierVersion": gs2328IGMPSnoopingstatisticQuerierVersion,
       "gs2328IGMPSnoopingstatisticHostVersion": gs2328IGMPSnoopingstatisticHostVersion,
       "gs2328IGMPSnoopingstatisticQuerierStatus": gs2328IGMPSnoopingstatisticQuerierStatus,
       "gs2328IGMPSnoopingstatisticQueriesTransmitted": gs2328IGMPSnoopingstatisticQueriesTransmitted,
       "gs2328IGMPSnoopingstatisticQueriesReceived": gs2328IGMPSnoopingstatisticQueriesReceived,
       "gs2328IGMPSnoopingstatisticV1ReportsReceived": gs2328IGMPSnoopingstatisticV1ReportsReceived,
       "gs2328IGMPSnoopingstatisticV2ReportsReceived": gs2328IGMPSnoopingstatisticV2ReportsReceived,
       "gs2328IGMPSnoopingstatisticV3ReportsReceived": gs2328IGMPSnoopingstatisticV3ReportsReceived,
       "gs2328IGMPSnoopingstatisticV2LeavesReceived": gs2328IGMPSnoopingstatisticV2LeavesReceived,
       "gs2328IGMPSnoopingRouterPortTable": gs2328IGMPSnoopingRouterPortTable,
       "gs2328IGMPSnoopingRouterPortEntry": gs2328IGMPSnoopingRouterPortEntry,
       "gs2328IGMPSnoopingRouterPortStatus": gs2328IGMPSnoopingRouterPortStatus,
       "gs2328IGMPSnoopingGroupsTable": gs2328IGMPSnoopingGroupsTable,
       "gs2328IGMPSnoopingGroupsEntry": gs2328IGMPSnoopingGroupsEntry,
       "gs2328IGMPSnoopingGroupsIndex": gs2328IGMPSnoopingGroupsIndex,
       "gs2328IGMPSnoopingGroupsVLANID": gs2328IGMPSnoopingGroupsVLANID,
       "gs2328IGMPSnoopingGroups": gs2328IGMPSnoopingGroups,
       "gs2328IGMPSnoopingGroupsMemberships": gs2328IGMPSnoopingGroupsMemberships,
       "gs2328IGMPSnoopingSSMTable": gs2328IGMPSnoopingSSMTable,
       "gs2328IGMPSnoopingSSMEntry": gs2328IGMPSnoopingSSMEntry,
       "gs2328IGMPSnoopingSSMIndex": gs2328IGMPSnoopingSSMIndex,
       "gs2328IGMPSnoopingSSMVLANID": gs2328IGMPSnoopingSSMVLANID,
       "gs2328IGMPSnoopingSSMGroup": gs2328IGMPSnoopingSSMGroup,
       "gs2328IGMPSnoopingSSMPort": gs2328IGMPSnoopingSSMPort,
       "gs2328IGMPSnoopingSSMMode": gs2328IGMPSnoopingSSMMode,
       "gs2328IGMPSnoopingSSMSourceAddress": gs2328IGMPSnoopingSSMSourceAddress,
       "gs2328IGMPSnoopingSSMType": gs2328IGMPSnoopingSSMType,
       "gs2328MLDSnooping": gs2328MLDSnooping,
       "gs2328MLDSnoopingBasic": gs2328MLDSnoopingBasic,
       "gs2328MLDSnoopingEnable": gs2328MLDSnoopingEnable,
       "gs2328MLDSnoopingUnregisteredIPMCv6Flooding": gs2328MLDSnoopingUnregisteredIPMCv6Flooding,
       "gs2328MLDSnoopingSSMIPRangeAddr": gs2328MLDSnoopingSSMIPRangeAddr,
       "gs2328MLDSnoopingSSMIPRangeValue": gs2328MLDSnoopingSSMIPRangeValue,
       "gs2328MLDSnoopingProxyEnabled": gs2328MLDSnoopingProxyEnabled,
       "gs2328MLDSnoopingPortRelatedTable": gs2328MLDSnoopingPortRelatedTable,
       "gs2328MLDSnoopingPortRelatedEntry": gs2328MLDSnoopingPortRelatedEntry,
       "gs2328MLDSnoopingRouterPort": gs2328MLDSnoopingRouterPort,
       "gs2328MLDSnoopingFastLeave": gs2328MLDSnoopingFastLeave,
       "gs2328MLDSnoopingThrottling": gs2328MLDSnoopingThrottling,
       "gs2328MLDSnoopingVLANTable": gs2328MLDSnoopingVLANTable,
       "gs2328MLDSnoopingVLANEntry": gs2328MLDSnoopingVLANEntry,
       "gs2328MLDSnoopingVLANID": gs2328MLDSnoopingVLANID,
       "gs2328MLDSnoopingVLANEnable": gs2328MLDSnoopingVLANEnable,
       "gs2328MLDSnoopingVLANIGMPQuerier": gs2328MLDSnoopingVLANIGMPQuerier,
       "gs2328MLDSnoopingVLANCompatibility": gs2328MLDSnoopingVLANCompatibility,
       "gs2328MLDSnoopingVLANRV": gs2328MLDSnoopingVLANRV,
       "gs2328MLDSnoopingVLANQI": gs2328MLDSnoopingVLANQI,
       "gs2328MLDSnoopingVLANQRI": gs2328MLDSnoopingVLANQRI,
       "gs2328MLDSnoopingVLANLLQI": gs2328MLDSnoopingVLANLLQI,
       "gs2328MLDSnoopingVLANURI": gs2328MLDSnoopingVLANURI,
       "gs2328MLDSnoopingPortGroupFiltering": gs2328MLDSnoopingPortGroupFiltering,
       "gs2328MLDSnoopingPortGroupFilteringCreate": gs2328MLDSnoopingPortGroupFilteringCreate,
       "gs2328MLDSnoopingPortGroupFilteringTable": gs2328MLDSnoopingPortGroupFilteringTable,
       "gs2328MLDSnoopingPortGroupFilteringEntry": gs2328MLDSnoopingPortGroupFilteringEntry,
       "gs2328MLDSnoopingPortGroupFilteringIndex": gs2328MLDSnoopingPortGroupFilteringIndex,
       "gs2328MLDSnoopingPortGroupFilteringPort": gs2328MLDSnoopingPortGroupFilteringPort,
       "gs2328MLDSnoopingPortGroupFilteringGroups": gs2328MLDSnoopingPortGroupFilteringGroups,
       "gs2328MLDSnoopingPortGroupFilteringRowStatus": gs2328MLDSnoopingPortGroupFilteringRowStatus,
       "gs2328MLDSnoopingStatus": gs2328MLDSnoopingStatus,
       "gs2328MLDSnoopingstatisticClear": gs2328MLDSnoopingstatisticClear,
       "gs2328MLDSnoopingstatisticTable": gs2328MLDSnoopingstatisticTable,
       "gs2328MLDSnoopingstatisticEntry": gs2328MLDSnoopingstatisticEntry,
       "gs2328MLDSnoopingstatisticVLANID": gs2328MLDSnoopingstatisticVLANID,
       "gs2328MLDSnoopingstatisticQuerierVersion": gs2328MLDSnoopingstatisticQuerierVersion,
       "gs2328MLDSnoopingstatisticHostVersion": gs2328MLDSnoopingstatisticHostVersion,
       "gs2328MLDSnoopingstatisticQuerierStatus": gs2328MLDSnoopingstatisticQuerierStatus,
       "gs2328MLDSnoopingstatisticQueriesTransmitted": gs2328MLDSnoopingstatisticQueriesTransmitted,
       "gs2328MLDSnoopingstatisticQueriesReceived": gs2328MLDSnoopingstatisticQueriesReceived,
       "gs2328MLDSnoopingstatisticV1ReportsReceived": gs2328MLDSnoopingstatisticV1ReportsReceived,
       "gs2328MLDSnoopingstatisticV2ReportsReceived": gs2328MLDSnoopingstatisticV2ReportsReceived,
       "gs2328MLDSnoopingstatisticV1LeavesReceived": gs2328MLDSnoopingstatisticV1LeavesReceived,
       "gs2328MLDSnoopingRouterPortTable": gs2328MLDSnoopingRouterPortTable,
       "gs2328MLDSnoopingRouterPortEntry": gs2328MLDSnoopingRouterPortEntry,
       "gs2328MLDSnoopingRouterPortStatus": gs2328MLDSnoopingRouterPortStatus,
       "gs2328MLDSnoopingGroupsTable": gs2328MLDSnoopingGroupsTable,
       "gs2328MLDSnoopingGroupsEntry": gs2328MLDSnoopingGroupsEntry,
       "gs2328MLDSnoopingGroupsIndex": gs2328MLDSnoopingGroupsIndex,
       "gs2328MLDSnoopingGroupsVLANID": gs2328MLDSnoopingGroupsVLANID,
       "gs2328MLDSnoopingGroups": gs2328MLDSnoopingGroups,
       "gs2328MLDSnoopingGroupsMemberships": gs2328MLDSnoopingGroupsMemberships,
       "gs2328MLDSnoopingSSMTable": gs2328MLDSnoopingSSMTable,
       "gs2328MLDSnoopingSSMEntry": gs2328MLDSnoopingSSMEntry,
       "gs2328MLDSnoopingSSMIndex": gs2328MLDSnoopingSSMIndex,
       "gs2328MLDSnoopingSSMVLANID": gs2328MLDSnoopingSSMVLANID,
       "gs2328MLDSnoopingSSMGroup": gs2328MLDSnoopingSSMGroup,
       "gs2328MLDSnoopingSSMPort": gs2328MLDSnoopingSSMPort,
       "gs2328MLDSnoopingSSMMode": gs2328MLDSnoopingSSMMode,
       "gs2328MLDSnoopingSSMSourceAddress": gs2328MLDSnoopingSSMSourceAddress,
       "gs2328MLDSnoopingSSMType": gs2328MLDSnoopingSSMType,
       "gs2328MVR": gs2328MVR,
       "gs2328MVRConfiguration": gs2328MVRConfiguration,
       "gs2328MVRMode": gs2328MVRMode,
       "gs2328MVRVLANId": gs2328MVRVLANId,
       "gs2328MVRPortConfigurationTable": gs2328MVRPortConfigurationTable,
       "gs2328MVRPortConfigurationEntry": gs2328MVRPortConfigurationEntry,
       "gs2328MVRPortConfigurationMode": gs2328MVRPortConfigurationMode,
       "gs2328MVRPortConfigurationType": gs2328MVRPortConfigurationType,
       "gs2328MVRPortConfigurationImmediateLeave": gs2328MVRPortConfigurationImmediateLeave,
       "gs2328MVRPortGroupFiltering": gs2328MVRPortGroupFiltering,
       "gs2328MVRPortGroupFilteringCreate": gs2328MVRPortGroupFilteringCreate,
       "gs2328MVRPortGroupFilteringTable": gs2328MVRPortGroupFilteringTable,
       "gs2328MVRPortGroupFilteringEntry": gs2328MVRPortGroupFilteringEntry,
       "gs2328MVRPortGroupFilteringIndex": gs2328MVRPortGroupFilteringIndex,
       "gs2328MVRPortGroupFilteringPort": gs2328MVRPortGroupFilteringPort,
       "gs2328MVRPortGroupFilteringStartGroups": gs2328MVRPortGroupFilteringStartGroups,
       "gs2328MVRPortGroupFilteringEndGroups": gs2328MVRPortGroupFilteringEndGroups,
       "gs2328MVRPortGroupFilteringRowStatus": gs2328MVRPortGroupFilteringRowStatus,
       "gs2328MVRGroupsTable": gs2328MVRGroupsTable,
       "gs2328MVRGroupsEntry": gs2328MVRGroupsEntry,
       "gs2328MVRGroupsIndex": gs2328MVRGroupsIndex,
       "gs2328MVRGroupsVLANID": gs2328MVRGroupsVLANID,
       "gs2328MVRGroups": gs2328MVRGroups,
       "gs2328MVRGroupsMemberships": gs2328MVRGroupsMemberships,
       "gs2328MVRStatus": gs2328MVRStatus,
       "gs2328MVRstatisticClear": gs2328MVRstatisticClear,
       "gs2328MVRstatisticVLANID": gs2328MVRstatisticVLANID,
       "gs2328MVRstatisticV1ReportsReceived": gs2328MVRstatisticV1ReportsReceived,
       "gs2328MVRstatisticV2ReportsReceived": gs2328MVRstatisticV2ReportsReceived,
       "gs2328MVRstatisticV3ReportsReceived": gs2328MVRstatisticV3ReportsReceived,
       "gs2328MVRstatisticV2LeavesReceived": gs2328MVRstatisticV2LeavesReceived,
       "gs2328LACP": gs2328LACP,
       "gs2328LACPConf": gs2328LACPConf,
       "gs2328LACPPortConfigurationTable": gs2328LACPPortConfigurationTable,
       "gs2328LACPPortConfigurationEntry": gs2328LACPPortConfigurationEntry,
       "gs2328LACPPortConfigurationPort": gs2328LACPPortConfigurationPort,
       "gs2328LACPPortConfigurationMode": gs2328LACPPortConfigurationMode,
       "gs2328LACPPortConfigurationKey": gs2328LACPPortConfigurationKey,
       "gs2328LACPPortConfigurationRole": gs2328LACPPortConfigurationRole,
       "gs2328LACPSystemStatusTable": gs2328LACPSystemStatusTable,
       "gs2328LACPSystemStatusEntry": gs2328LACPSystemStatusEntry,
       "gs2328LACPSystemStatusIndex": gs2328LACPSystemStatusIndex,
       "gs2328LACPSystemStatusAggrID": gs2328LACPSystemStatusAggrID,
       "gs2328LACPSystemStatusPartnerSystemID": gs2328LACPSystemStatusPartnerSystemID,
       "gs2328LACPSystemStatusPartnerKey": gs2328LACPSystemStatusPartnerKey,
       "gs2328LACPSystemStatusLastchanged": gs2328LACPSystemStatusLastchanged,
       "gs2328LACPSystemStatusLocalPorts": gs2328LACPSystemStatusLocalPorts,
       "gs2328LACPStatusTable": gs2328LACPStatusTable,
       "gs2328LACPStatusEntry": gs2328LACPStatusEntry,
       "gs2328LACPStatusPort": gs2328LACPStatusPort,
       "gs2328LACPStatusLACP": gs2328LACPStatusLACP,
       "gs2328LACPStatusKey": gs2328LACPStatusKey,
       "gs2328LACPStatusAggrID": gs2328LACPStatusAggrID,
       "gs2328LACPStatusPartnerSystemID": gs2328LACPStatusPartnerSystemID,
       "gs2328LACPStatusPartnerPort": gs2328LACPStatusPartnerPort,
       "gs2328LACPStatisticsTable": gs2328LACPStatisticsTable,
       "gs2328LACPStatisticsEntry": gs2328LACPStatisticsEntry,
       "gs2328LACPStatisticsPort": gs2328LACPStatisticsPort,
       "gs2328LACPReceived": gs2328LACPReceived,
       "gs2328LACPTransmitted": gs2328LACPTransmitted,
       "gs2328LACPDiscardedUnknown": gs2328LACPDiscardedUnknown,
       "gs2328LACPDiscardedIllegal": gs2328LACPDiscardedIllegal,
       "gs2328LACPStatisticsClear": gs2328LACPStatisticsClear,
       "gs2328STP": gs2328STP,
       "gs2328STPBridgeBasicConf": gs2328STPBridgeBasicConf,
       "gs2328STPBridgeProtocolVersion": gs2328STPBridgeProtocolVersion,
       "gs2328STPBridgePriority": gs2328STPBridgePriority,
       "gs2328STPBridgeForwardDelay": gs2328STPBridgeForwardDelay,
       "gs2328STPBridgeMaxAge": gs2328STPBridgeMaxAge,
       "gs2328STPBridgeMaximumHopCount": gs2328STPBridgeMaximumHopCount,
       "gs2328STPBridgeTransmitHoldCount": gs2328STPBridgeTransmitHoldCount,
       "gs2328STPBridgeAdvancedConf": gs2328STPBridgeAdvancedConf,
       "gs2328STPBridgeEdgePortBPDUFiltering": gs2328STPBridgeEdgePortBPDUFiltering,
       "gs2328STPBridgeEdgePortBPDUGuard": gs2328STPBridgeEdgePortBPDUGuard,
       "gs2328STPBridgePortErrorRecoveryTimeout": gs2328STPBridgePortErrorRecoveryTimeout,
       "gs2328STPMSTIConf": gs2328STPMSTIConf,
       "gs2328STPMSTIConfigurationName": gs2328STPMSTIConfigurationName,
       "gs2328STPMSTIConfigurationRevision": gs2328STPMSTIConfigurationRevision,
       "gs2328STPMSTIMappingConf": gs2328STPMSTIMappingConf,
       "gs2328STPMSTI1VLANsMapped": gs2328STPMSTI1VLANsMapped,
       "gs2328STPMSTI2VLANsMapped": gs2328STPMSTI2VLANsMapped,
       "gs2328STPMSTI3VLANsMapped": gs2328STPMSTI3VLANsMapped,
       "gs2328STPMSTI4VLANsMapped": gs2328STPMSTI4VLANsMapped,
       "gs2328STPMSTI5VLANsMapped": gs2328STPMSTI5VLANsMapped,
       "gs2328STPMSTI6VLANsMapped": gs2328STPMSTI6VLANsMapped,
       "gs2328STPMSTI7VLANsMapped": gs2328STPMSTI7VLANsMapped,
       "gs2328STPMSTIPriority": gs2328STPMSTIPriority,
       "gs2328STPCISTPriority": gs2328STPCISTPriority,
       "gs2328STPMSTI1Priority": gs2328STPMSTI1Priority,
       "gs2328STPMSTI2Priority": gs2328STPMSTI2Priority,
       "gs2328STPMSTI3Priority": gs2328STPMSTI3Priority,
       "gs2328STPMSTI4Priority": gs2328STPMSTI4Priority,
       "gs2328STPMSTI5Priority": gs2328STPMSTI5Priority,
       "gs2328STPMSTI6Priority": gs2328STPMSTI6Priority,
       "gs2328STPMSTI7Priority": gs2328STPMSTI7Priority,
       "gs2328STPCISTPort": gs2328STPCISTPort,
       "gs2328STPCISTAggregatedPort": gs2328STPCISTAggregatedPort,
       "gs2328STPCISTAggregatedPortSTPEnabled": gs2328STPCISTAggregatedPortSTPEnabled,
       "gs2328STPCISTAggregatedPortPathCost": gs2328STPCISTAggregatedPortPathCost,
       "gs2328STPCISTAggregatedPortPriority": gs2328STPCISTAggregatedPortPriority,
       "gs2328STPCISTAggregatedPortAdminEdge": gs2328STPCISTAggregatedPortAdminEdge,
       "gs2328STPCISTAggregatedPortAutoEdge": gs2328STPCISTAggregatedPortAutoEdge,
       "gs2328STPCISTAggregatedPortRestrictedRole": gs2328STPCISTAggregatedPortRestrictedRole,
       "gs2328STPCISTAggregatedPortRestrictedTCN": gs2328STPCISTAggregatedPortRestrictedTCN,
       "gs2328STPCISTAggregatedPortBPDUGuard": gs2328STPCISTAggregatedPortBPDUGuard,
       "gs2328STPCISTAggregatedPortPointtoPoint": gs2328STPCISTAggregatedPortPointtoPoint,
       "gs2328STPCISTNormalPortTable": gs2328STPCISTNormalPortTable,
       "gs2328STPCISTNormalPortEntry": gs2328STPCISTNormalPortEntry,
       "gs2328STPCISTNormalPortConfPort": gs2328STPCISTNormalPortConfPort,
       "gs2328STPCISTNormalPortSTPEnabled": gs2328STPCISTNormalPortSTPEnabled,
       "gs2328STPCISTNormalPortPathCost": gs2328STPCISTNormalPortPathCost,
       "gs2328STPCISTNormalPortPriority": gs2328STPCISTNormalPortPriority,
       "gs2328STPCISTNormalPortAdminEdge": gs2328STPCISTNormalPortAdminEdge,
       "gs2328STPCISTNormalPortAutoEdge": gs2328STPCISTNormalPortAutoEdge,
       "gs2328STPCISTNormalPortRestrictedRole": gs2328STPCISTNormalPortRestrictedRole,
       "gs2328STPCISTNormalPortRestrictedTCN": gs2328STPCISTNormalPortRestrictedTCN,
       "gs2328STPCISTNormalPortBPDUGuard": gs2328STPCISTNormalPortBPDUGuard,
       "gs2328STPCISTNormalPortPointtoPoint": gs2328STPCISTNormalPortPointtoPoint,
       "gs2328STPMSTIPort": gs2328STPMSTIPort,
       "gs2328STPMSTI1Port": gs2328STPMSTI1Port,
       "gs2328STPMSTI1AggregatedPort": gs2328STPMSTI1AggregatedPort,
       "gs2328STPMSTI1AggregatedPortPathCost": gs2328STPMSTI1AggregatedPortPathCost,
       "gs2328STPMSTI1AggregatedPortPriority": gs2328STPMSTI1AggregatedPortPriority,
       "gs2328STPMSTI1NormalPortTable": gs2328STPMSTI1NormalPortTable,
       "gs2328STPMSTI1NormalPortEntry": gs2328STPMSTI1NormalPortEntry,
       "gs2328STPMSTI1NormalPortConfPort": gs2328STPMSTI1NormalPortConfPort,
       "gs2328STPMSTI1NormalPortPathCost": gs2328STPMSTI1NormalPortPathCost,
       "gs2328STPMSTI1NormalPortPriority": gs2328STPMSTI1NormalPortPriority,
       "gs2328STPMSTI2Port": gs2328STPMSTI2Port,
       "gs2328STPMSTI2AggregatedPort": gs2328STPMSTI2AggregatedPort,
       "gs2328STPMSTI2AggregatedPortPathCost": gs2328STPMSTI2AggregatedPortPathCost,
       "gs2328STPMSTI2AggregatedPortPriority": gs2328STPMSTI2AggregatedPortPriority,
       "gs2328STPMSTI2NormalPortTable": gs2328STPMSTI2NormalPortTable,
       "gs2328STPMSTI2NormalPortEntry": gs2328STPMSTI2NormalPortEntry,
       "gs2328STPMSTI2NormalPortConfPort": gs2328STPMSTI2NormalPortConfPort,
       "gs2328STPMSTI2NormalPortPathCost": gs2328STPMSTI2NormalPortPathCost,
       "gs2328STPMSTI2NormalPortPriority": gs2328STPMSTI2NormalPortPriority,
       "gs2328STPMSTI3Port": gs2328STPMSTI3Port,
       "gs2328STPMSTI3AggregatedPort": gs2328STPMSTI3AggregatedPort,
       "gs2328STPMSTI3AggregatedPortPathCost": gs2328STPMSTI3AggregatedPortPathCost,
       "gs2328STPMSTI3AggregatedPortPriority": gs2328STPMSTI3AggregatedPortPriority,
       "gs2328STPMSTI3NormalPortTable": gs2328STPMSTI3NormalPortTable,
       "gs2328STPMSTI3NormalPortEntry": gs2328STPMSTI3NormalPortEntry,
       "gs2328STPMSTI3NormalPortConfPort": gs2328STPMSTI3NormalPortConfPort,
       "gs2328STPMSTI3NormalPortPathCost": gs2328STPMSTI3NormalPortPathCost,
       "gs2328STPMSTI3NormalPortPriority": gs2328STPMSTI3NormalPortPriority,
       "gs2328STPMSTI4Port": gs2328STPMSTI4Port,
       "gs2328STPMSTI4AggregatedPort": gs2328STPMSTI4AggregatedPort,
       "gs2328STPMSTI4AggregatedPortPathCost": gs2328STPMSTI4AggregatedPortPathCost,
       "gs2328STPMSTI4AggregatedPortPriority": gs2328STPMSTI4AggregatedPortPriority,
       "gs2328STPMSTI4NormalPortTable": gs2328STPMSTI4NormalPortTable,
       "gs2328STPMSTI4NormalPortEntry": gs2328STPMSTI4NormalPortEntry,
       "gs2328STPMSTI4NormalPortConfPort": gs2328STPMSTI4NormalPortConfPort,
       "gs2328STPMSTI4NormalPortPathCost": gs2328STPMSTI4NormalPortPathCost,
       "gs2328STPMSTI4NormalPortPriority": gs2328STPMSTI4NormalPortPriority,
       "gs2328STPMSTI5Port": gs2328STPMSTI5Port,
       "gs2328STPMSTI5AggregatedPort": gs2328STPMSTI5AggregatedPort,
       "gs2328STPMSTI5AggregatedPortPathCost": gs2328STPMSTI5AggregatedPortPathCost,
       "gs2328STPMSTI5AggregatedPortPriority": gs2328STPMSTI5AggregatedPortPriority,
       "gs2328STPMSTI5NormalPortTable": gs2328STPMSTI5NormalPortTable,
       "gs2328STPMSTI5NormalPortEntry": gs2328STPMSTI5NormalPortEntry,
       "gs2328STPMSTI5NormalPortConfPort": gs2328STPMSTI5NormalPortConfPort,
       "gs2328STPMSTI5NormalPortPathCost": gs2328STPMSTI5NormalPortPathCost,
       "gs2328STPMSTI5NormalPortPriority": gs2328STPMSTI5NormalPortPriority,
       "gs2328STPMSTI6Port": gs2328STPMSTI6Port,
       "gs2328STPMSTI6AggregatedPort": gs2328STPMSTI6AggregatedPort,
       "gs2328STPMSTI6AggregatedPortPathCost": gs2328STPMSTI6AggregatedPortPathCost,
       "gs2328STPMSTI6AggregatedPortPriority": gs2328STPMSTI6AggregatedPortPriority,
       "gs2328STPMSTI6NormalPortTable": gs2328STPMSTI6NormalPortTable,
       "gs2328STPMSTI6NormalPortEntry": gs2328STPMSTI6NormalPortEntry,
       "gs2328STPMSTI6NormalPortConfPort": gs2328STPMSTI6NormalPortConfPort,
       "gs2328STPMSTI6NormalPortPathCost": gs2328STPMSTI6NormalPortPathCost,
       "gs2328STPMSTI6NormalPortPriority": gs2328STPMSTI6NormalPortPriority,
       "gs2328STPMSTI7Port": gs2328STPMSTI7Port,
       "gs2328STPMSTI7AggregatedPort": gs2328STPMSTI7AggregatedPort,
       "gs2328STPMSTI7AggregatedPortPathCost": gs2328STPMSTI7AggregatedPortPathCost,
       "gs2328STPMSTI7AggregatedPortPriority": gs2328STPMSTI7AggregatedPortPriority,
       "gs2328STPMSTI7NormalPortTable": gs2328STPMSTI7NormalPortTable,
       "gs2328STPMSTI7NormalPortEntry": gs2328STPMSTI7NormalPortEntry,
       "gs2328STPMSTI7NormalPortConfPort": gs2328STPMSTI7NormalPortConfPort,
       "gs2328STPMSTI7NormalPortPathCost": gs2328STPMSTI7NormalPortPathCost,
       "gs2328STPMSTI7NormalPortPriority": gs2328STPMSTI7NormalPortPriority,
       "gs2328STPBridgeStatus": gs2328STPBridgeStatus,
       "gs2328CISTBridgeSTP": gs2328CISTBridgeSTP,
       "gs2328CISTBridgeSTPStatus": gs2328CISTBridgeSTPStatus,
       "gs2328CISTBridgeInstance": gs2328CISTBridgeInstance,
       "gs2328CISTBridgeID": gs2328CISTBridgeID,
       "gs2328CISTRootID": gs2328CISTRootID,
       "gs2328CISTRootPort": gs2328CISTRootPort,
       "gs2328CISTRootCost": gs2328CISTRootCost,
       "gs2328CISTRegionalRoot": gs2328CISTRegionalRoot,
       "gs2328CISTInternalRootCost": gs2328CISTInternalRootCost,
       "gs2328CISTTopologyFlag": gs2328CISTTopologyFlag,
       "gs2328CISTTopologyChangeCount": gs2328CISTTopologyChangeCount,
       "gs2328CISTTopologyChangeLast": gs2328CISTTopologyChangeLast,
       "gs2328CISTPortStateTable": gs2328CISTPortStateTable,
       "gs2328CISTPortStateEntry": gs2328CISTPortStateEntry,
       "gs2328CISTPortStateIndex": gs2328CISTPortStateIndex,
       "gs2328CISTPortStatePort": gs2328CISTPortStatePort,
       "gs2328CISTPortStatePortID": gs2328CISTPortStatePortID,
       "gs2328CISTPortStateRole": gs2328CISTPortStateRole,
       "gs2328CISTPortStateState": gs2328CISTPortStateState,
       "gs2328CISTPortStatePathCost": gs2328CISTPortStatePathCost,
       "gs2328CISTPortStateEdge": gs2328CISTPortStateEdge,
       "gs2328CISTPortStatePoint2Point": gs2328CISTPortStatePoint2Point,
       "gs2328CISTPortStateUptime": gs2328CISTPortStateUptime,
       "gs2328MSTI1BridgeSTP": gs2328MSTI1BridgeSTP,
       "gs2328MSTI1BridgeSTPStatus": gs2328MSTI1BridgeSTPStatus,
       "gs2328MSTI1BridgeInstance": gs2328MSTI1BridgeInstance,
       "gs2328MSTI1BridgeID": gs2328MSTI1BridgeID,
       "gs2328MSTI1RootID": gs2328MSTI1RootID,
       "gs2328MSTI1RootPort": gs2328MSTI1RootPort,
       "gs2328MSTI1RootCost": gs2328MSTI1RootCost,
       "gs2328MSTI1TopologyFlag": gs2328MSTI1TopologyFlag,
       "gs2328MSTI1TopologyChangeCount": gs2328MSTI1TopologyChangeCount,
       "gs2328MSTI1TopologyChangeLast": gs2328MSTI1TopologyChangeLast,
       "gs2328MSTI1PortStateTable": gs2328MSTI1PortStateTable,
       "gs2328MSTI1PortStateEntry": gs2328MSTI1PortStateEntry,
       "gs2328MSTI1PortStateIndex": gs2328MSTI1PortStateIndex,
       "gs2328MSTI1PortStatePort": gs2328MSTI1PortStatePort,
       "gs2328MSTI1PortStatePortID": gs2328MSTI1PortStatePortID,
       "gs2328MSTI1PortStateRole": gs2328MSTI1PortStateRole,
       "gs2328MSTI1PortStateState": gs2328MSTI1PortStateState,
       "gs2328MSTI1PortStatePathCost": gs2328MSTI1PortStatePathCost,
       "gs2328MSTI1PortStateEdge": gs2328MSTI1PortStateEdge,
       "gs2328MSTI1PortStatePoint2Point": gs2328MSTI1PortStatePoint2Point,
       "gs2328MSTI1PortStateUptime": gs2328MSTI1PortStateUptime,
       "gs2328MSTI2BridgeSTP": gs2328MSTI2BridgeSTP,
       "gs2328MSTI2BridgeSTPStatus": gs2328MSTI2BridgeSTPStatus,
       "gs2328MSTI2BridgeInstance": gs2328MSTI2BridgeInstance,
       "gs2328MSTI2BridgeID": gs2328MSTI2BridgeID,
       "gs2328MSTI2RootID": gs2328MSTI2RootID,
       "gs2328MSTI2RootPort": gs2328MSTI2RootPort,
       "gs2328MSTI2RootCost": gs2328MSTI2RootCost,
       "gs2328MSTI2TopologyFlag": gs2328MSTI2TopologyFlag,
       "gs2328MSTI2TopologyChangeCount": gs2328MSTI2TopologyChangeCount,
       "gs2328MSTI2TopologyChangeLast": gs2328MSTI2TopologyChangeLast,
       "gs2328MSTI2PortStateTable": gs2328MSTI2PortStateTable,
       "gs2328MSTI2PortStateEntry": gs2328MSTI2PortStateEntry,
       "gs2328MSTI2PortStateIndex": gs2328MSTI2PortStateIndex,
       "gs2328MSTI2PortStatePort": gs2328MSTI2PortStatePort,
       "gs2328MSTI2PortStatePortID": gs2328MSTI2PortStatePortID,
       "gs2328MSTI2PortStateRole": gs2328MSTI2PortStateRole,
       "gs2328MSTI2PortStateState": gs2328MSTI2PortStateState,
       "gs2328MSTI2PortStatePathCost": gs2328MSTI2PortStatePathCost,
       "gs2328MSTI2PortStateEdge": gs2328MSTI2PortStateEdge,
       "gs2328MSTI2PortStatePoint2Point": gs2328MSTI2PortStatePoint2Point,
       "gs2328MSTI2PortStateUptime": gs2328MSTI2PortStateUptime,
       "gs2328MSTI3BridgeSTP": gs2328MSTI3BridgeSTP,
       "gs2328MSTI3BridgeSTPStatus": gs2328MSTI3BridgeSTPStatus,
       "gs2328MSTI3BridgeInstance": gs2328MSTI3BridgeInstance,
       "gs2328MSTI3BridgeID": gs2328MSTI3BridgeID,
       "gs2328MSTI3RootID": gs2328MSTI3RootID,
       "gs2328MSTI3RootPort": gs2328MSTI3RootPort,
       "gs2328MSTI3RootCost": gs2328MSTI3RootCost,
       "gs2328MSTI3TopologyFlag": gs2328MSTI3TopologyFlag,
       "gs2328MSTI3TopologyChangeCount": gs2328MSTI3TopologyChangeCount,
       "gs2328MSTI3TopologyChangeLast": gs2328MSTI3TopologyChangeLast,
       "gs2328MSTI3PortStateTable": gs2328MSTI3PortStateTable,
       "gs2328MSTI3PortStateEntry": gs2328MSTI3PortStateEntry,
       "gs2328MSTI3PortStateIndex": gs2328MSTI3PortStateIndex,
       "gs2328MSTI3PortStatePort": gs2328MSTI3PortStatePort,
       "gs2328MSTI3PortStatePortID": gs2328MSTI3PortStatePortID,
       "gs2328MSTI3PortStateRole": gs2328MSTI3PortStateRole,
       "gs2328MSTI3PortStateState": gs2328MSTI3PortStateState,
       "gs2328MSTI3PortStatePathCost": gs2328MSTI3PortStatePathCost,
       "gs2328MSTI3PortStateEdge": gs2328MSTI3PortStateEdge,
       "gs2328MSTI3PortStatePoint2Point": gs2328MSTI3PortStatePoint2Point,
       "gs2328MSTI3PortStateUptime": gs2328MSTI3PortStateUptime,
       "gs2328MSTI4BridgeSTP": gs2328MSTI4BridgeSTP,
       "gs2328MSTI4BridgeSTPStatus": gs2328MSTI4BridgeSTPStatus,
       "gs2328MSTI4BridgeInstance": gs2328MSTI4BridgeInstance,
       "gs2328MSTI4BridgeID": gs2328MSTI4BridgeID,
       "gs2328MSTI4RootID": gs2328MSTI4RootID,
       "gs2328MSTI4RootPort": gs2328MSTI4RootPort,
       "gs2328MSTI4RootCost": gs2328MSTI4RootCost,
       "gs2328MSTI4TopologyFlag": gs2328MSTI4TopologyFlag,
       "gs2328MSTI4TopologyChangeCount": gs2328MSTI4TopologyChangeCount,
       "gs2328MSTI4TopologyChangeLast": gs2328MSTI4TopologyChangeLast,
       "gs2328MSTI4PortStateTable": gs2328MSTI4PortStateTable,
       "gs2328MSTI4PortStateEntry": gs2328MSTI4PortStateEntry,
       "gs2328MSTI4PortStateIndex": gs2328MSTI4PortStateIndex,
       "gs2328MSTI4PortStatePort": gs2328MSTI4PortStatePort,
       "gs2328MSTI4PortStatePortID": gs2328MSTI4PortStatePortID,
       "gs2328MSTI4PortStateRole": gs2328MSTI4PortStateRole,
       "gs2328MSTI4PortStateState": gs2328MSTI4PortStateState,
       "gs2328MSTI4PortStatePathCost": gs2328MSTI4PortStatePathCost,
       "gs2328MSTI4PortStateEdge": gs2328MSTI4PortStateEdge,
       "gs2328MSTI4PortStatePoint2Point": gs2328MSTI4PortStatePoint2Point,
       "gs2328MSTI4PortStateUptime": gs2328MSTI4PortStateUptime,
       "gs2328MSTI5BridgeSTP": gs2328MSTI5BridgeSTP,
       "gs2328MSTI5BridgeSTPStatus": gs2328MSTI5BridgeSTPStatus,
       "gs2328MSTI5BridgeInstance": gs2328MSTI5BridgeInstance,
       "gs2328MSTI5BridgeID": gs2328MSTI5BridgeID,
       "gs2328MSTI5RootID": gs2328MSTI5RootID,
       "gs2328MSTI5RootPort": gs2328MSTI5RootPort,
       "gs2328MSTI5RootCost": gs2328MSTI5RootCost,
       "gs2328MSTI5TopologyFlag": gs2328MSTI5TopologyFlag,
       "gs2328MSTI5TopologyChangeCount": gs2328MSTI5TopologyChangeCount,
       "gs2328MSTI5TopologyChangeLast": gs2328MSTI5TopologyChangeLast,
       "gs2328MSTI5PortStateTable": gs2328MSTI5PortStateTable,
       "gs2328MSTI5PortStateEntry": gs2328MSTI5PortStateEntry,
       "gs2328MSTI5PortStateIndex": gs2328MSTI5PortStateIndex,
       "gs2328MSTI5PortStatePort": gs2328MSTI5PortStatePort,
       "gs2328MSTI5PortStatePortID": gs2328MSTI5PortStatePortID,
       "gs2328MSTI5PortStateRole": gs2328MSTI5PortStateRole,
       "gs2328MSTI5PortStateState": gs2328MSTI5PortStateState,
       "gs2328MSTI5PortStatePathCost": gs2328MSTI5PortStatePathCost,
       "gs2328MSTI5PortStateEdge": gs2328MSTI5PortStateEdge,
       "gs2328MSTI5PortStatePoint2Point": gs2328MSTI5PortStatePoint2Point,
       "gs2328MSTI5PortStateUptime": gs2328MSTI5PortStateUptime,
       "gs2328MSTI6BridgeSTP": gs2328MSTI6BridgeSTP,
       "gs2328MSTI6BridgeSTPStatus": gs2328MSTI6BridgeSTPStatus,
       "gs2328MSTI6BridgeInstance": gs2328MSTI6BridgeInstance,
       "gs2328MSTI6BridgeID": gs2328MSTI6BridgeID,
       "gs2328MSTI6RootID": gs2328MSTI6RootID,
       "gs2328MSTI6RootPort": gs2328MSTI6RootPort,
       "gs2328MSTI6RootCost": gs2328MSTI6RootCost,
       "gs2328MSTI6TopologyFlag": gs2328MSTI6TopologyFlag,
       "gs2328MSTI6TopologyChangeCount": gs2328MSTI6TopologyChangeCount,
       "gs2328MSTI6TopologyChangeLast": gs2328MSTI6TopologyChangeLast,
       "gs2328MSTI6PortStateTable": gs2328MSTI6PortStateTable,
       "gs2328MSTI6PortStateEntry": gs2328MSTI6PortStateEntry,
       "gs2328MSTI6PortStateIndex": gs2328MSTI6PortStateIndex,
       "gs2328MSTI6PortStatePort": gs2328MSTI6PortStatePort,
       "gs2328MSTI6PortStatePortID": gs2328MSTI6PortStatePortID,
       "gs2328MSTI6PortStateRole": gs2328MSTI6PortStateRole,
       "gs2328MSTI6PortStateState": gs2328MSTI6PortStateState,
       "gs2328MSTI6PortStatePathCost": gs2328MSTI6PortStatePathCost,
       "gs2328MSTI6PortStateEdge": gs2328MSTI6PortStateEdge,
       "gs2328MSTI6PortStatePoint2Point": gs2328MSTI6PortStatePoint2Point,
       "gs2328MSTI6PortStateUptime": gs2328MSTI6PortStateUptime,
       "gs2328MSTI7BridgeSTP": gs2328MSTI7BridgeSTP,
       "gs2328MSTI7BridgeSTPStatus": gs2328MSTI7BridgeSTPStatus,
       "gs2328MSTI7BridgeInstance": gs2328MSTI7BridgeInstance,
       "gs2328MSTI7BridgeID": gs2328MSTI7BridgeID,
       "gs2328MSTI7RootID": gs2328MSTI7RootID,
       "gs2328MSTI7RootPort": gs2328MSTI7RootPort,
       "gs2328MSTI7RootCost": gs2328MSTI7RootCost,
       "gs2328MSTI7TopologyFlag": gs2328MSTI7TopologyFlag,
       "gs2328MSTI7TopologyChangeCount": gs2328MSTI7TopologyChangeCount,
       "gs2328MSTI7TopologyChangeLast": gs2328MSTI7TopologyChangeLast,
       "gs2328MSTI7PortStateTable": gs2328MSTI7PortStateTable,
       "gs2328MSTI7PortStateEntry": gs2328MSTI7PortStateEntry,
       "gs2328MSTI7PortStateIndex": gs2328MSTI7PortStateIndex,
       "gs2328MSTI7PortStatePort": gs2328MSTI7PortStatePort,
       "gs2328MSTI7PortStatePortID": gs2328MSTI7PortStatePortID,
       "gs2328MSTI7PortStateRole": gs2328MSTI7PortStateRole,
       "gs2328MSTI7PortStateState": gs2328MSTI7PortStateState,
       "gs2328MSTI7PortStatePathCost": gs2328MSTI7PortStatePathCost,
       "gs2328MSTI7PortStateEdge": gs2328MSTI7PortStateEdge,
       "gs2328MSTI7PortStatePoint2Point": gs2328MSTI7PortStatePoint2Point,
       "gs2328MSTI7PortStateUptime": gs2328MSTI7PortStateUptime,
       "gs2328STPPortStatusTable": gs2328STPPortStatusTable,
       "gs2328STPPortStatusEntry": gs2328STPPortStatusEntry,
       "gs2328STPPortStatusPort": gs2328STPPortStatusPort,
       "gs2328STPPortStatusCISTRole": gs2328STPPortStatusCISTRole,
       "gs2328STPPortStatusCISTState": gs2328STPPortStatusCISTState,
       "gs2328STPPortStatusUptime": gs2328STPPortStatusUptime,
       "gs2328STPPortStatisticsTable": gs2328STPPortStatisticsTable,
       "gs2328STPPortStatisticsEntry": gs2328STPPortStatisticsEntry,
       "gs2328STPStatisticsIndex": gs2328STPStatisticsIndex,
       "gs2328STPStatisticsPort": gs2328STPStatisticsPort,
       "gs2328STPStatisticsTxMSTP": gs2328STPStatisticsTxMSTP,
       "gs2328STPStatisticsTxRSTP": gs2328STPStatisticsTxRSTP,
       "gs2328STPStatisticsTxSTP": gs2328STPStatisticsTxSTP,
       "gs2328STPStatisticsTxTCN": gs2328STPStatisticsTxTCN,
       "gs2328STPStatisticsRxMSTP": gs2328STPStatisticsRxMSTP,
       "gs2328STPStatisticsRxRSTP": gs2328STPStatisticsRxRSTP,
       "gs2328STPStatisticsRxSTP": gs2328STPStatisticsRxSTP,
       "gs2328STPStatisticsRxTCN": gs2328STPStatisticsRxTCN,
       "gs2328STPStatisticsDiscardedUnknown": gs2328STPStatisticsDiscardedUnknown,
       "gs2328STPStatisticsDiscardedIllegal": gs2328STPStatisticsDiscardedIllegal,
       "gs2328FilteringDataBase": gs2328FilteringDataBase,
       "gs2328FilteringDataBaseConfig": gs2328FilteringDataBaseConfig,
       "gs2328FilteringDataBaseAgingTime": gs2328FilteringDataBaseAgingTime,
       "gs2328FilteringDataBaseConfigTable": gs2328FilteringDataBaseConfigTable,
       "gs2328FilteringDataBaseConfigEntry": gs2328FilteringDataBaseConfigEntry,
       "gs2328FilteringDataBaseConfigPort": gs2328FilteringDataBaseConfigPort,
       "gs2328FilteringDataBaseConfigLearning": gs2328FilteringDataBaseConfigLearning,
       "gs2328FilteringDataBaseStaticMAC": gs2328FilteringDataBaseStaticMAC,
       "gs2328FilteringDataBaseStaticMACCreate": gs2328FilteringDataBaseStaticMACCreate,
       "gs2328FilteringDataBaseStaticMACTable": gs2328FilteringDataBaseStaticMACTable,
       "gs2328FilteringDataBaseStaticMACEntry": gs2328FilteringDataBaseStaticMACEntry,
       "gs2328FilteringDataBaseStaticMACIndex": gs2328FilteringDataBaseStaticMACIndex,
       "gs2328FilteringDataBaseStaticMACVLANId": gs2328FilteringDataBaseStaticMACVLANId,
       "gs2328FilteringDataBaseStaticMACAddress": gs2328FilteringDataBaseStaticMACAddress,
       "gs2328FilteringDataBaseStaticMACPortMembers": gs2328FilteringDataBaseStaticMACPortMembers,
       "gs2328FilteringDataBaseStaticMACRowStatus": gs2328FilteringDataBaseStaticMACRowStatus,
       "gs2328FilteringDataBaseDynamicMACTable": gs2328FilteringDataBaseDynamicMACTable,
       "gs2328FilteringDataBaseDynamicMACEntry": gs2328FilteringDataBaseDynamicMACEntry,
       "gs2328FilteringDataBaseDynamicMACIndex": gs2328FilteringDataBaseDynamicMACIndex,
       "gs2328FilteringDataBaseDynamicMACType": gs2328FilteringDataBaseDynamicMACType,
       "gs2328FilteringDataBaseDynamicMACVLAN": gs2328FilteringDataBaseDynamicMACVLAN,
       "gs2328FilteringDataBaseDynamicMACAddress": gs2328FilteringDataBaseDynamicMACAddress,
       "gs2328FilteringDataBaseDynamicPortMembers": gs2328FilteringDataBaseDynamicPortMembers,
       "gs2328SFlowAgent": gs2328SFlowAgent,
       "gs2328SFlowAgentCollector": gs2328SFlowAgentCollector,
       "gs2328SFlowAgentReceiverMode": gs2328SFlowAgentReceiverMode,
       "gs2328LMC": gs2328LMC,
       "gs2328LMCOperating": gs2328LMCOperating,
       "gs2328LMCConfigViaDhcp": gs2328LMCConfigViaDhcp,
       "gs2328LMCDomain": gs2328LMCDomain,
       "gs2328LMChcpClientAutoRenew": gs2328LMChcpClientAutoRenew,
       "gs2328LMCZeroTouchSupport": gs2328LMCZeroTouchSupport,
       "gs2328LMCPairingTokenPresent": gs2328LMCPairingTokenPresent,
       "gs2328LMCClientStatus": gs2328LMCClientStatus,
       "gs2328LMCManagementStatus": gs2328LMCManagementStatus,
       "gs2328LMCControlStatus": gs2328LMCControlStatus,
       "gs2328LMCMonitoringStatus": gs2328LMCMonitoringStatus,
       "gs2328LMCConfigurationSource": gs2328LMCConfigurationSource,
       "gs2328LMCConfigModified": gs2328LMCConfigModified,
       "gs2328LMCDeviceID": gs2328LMCDeviceID,
       "gs2328LMCRoundTripTime": gs2328LMCRoundTripTime,
       "gs2328Security": gs2328Security,
       "gs2328IPSourceGuard": gs2328IPSourceGuard,
       "gs2328IPSourceGuardConf": gs2328IPSourceGuardConf,
       "gs2328IPSourceGuardMode": gs2328IPSourceGuardMode,
       "gs2328IPSourceGuardPortConfigTable": gs2328IPSourceGuardPortConfigTable,
       "gs2328IPSourceGuardPortConfigEntry": gs2328IPSourceGuardPortConfigEntry,
       "gs2328IPSourceGuardPortConfigPort": gs2328IPSourceGuardPortConfigPort,
       "gs2328IPSourceGuardPortConfigMode": gs2328IPSourceGuardPortConfigMode,
       "gs2328IPSourceGuardPortMaxDynamicClients": gs2328IPSourceGuardPortMaxDynamicClients,
       "gs2328IPSourceGuardStatic": gs2328IPSourceGuardStatic,
       "gs2328IPSourceGuardStaticCreate": gs2328IPSourceGuardStaticCreate,
       "gs2328IPSourceGuardStaticTable": gs2328IPSourceGuardStaticTable,
       "gs2328IPSourceGuardStaticEntry": gs2328IPSourceGuardStaticEntry,
       "gs2328IPSourceGuardStaticIndex": gs2328IPSourceGuardStaticIndex,
       "gs2328IPSourceGuardStaticPort": gs2328IPSourceGuardStaticPort,
       "gs2328IPSourceGuardStaticVLANId": gs2328IPSourceGuardStaticVLANId,
       "gs2328IPSourceGuardStaticIPAddress": gs2328IPSourceGuardStaticIPAddress,
       "gs2328IPSourceGuardStaticMACAddress": gs2328IPSourceGuardStaticMACAddress,
       "gs2328IPSourceGuardStaticRowStatus": gs2328IPSourceGuardStaticRowStatus,
       "gs2328IPSourceGuardDynamicTable": gs2328IPSourceGuardDynamicTable,
       "gs2328IPSourceGuardDynamicEntry": gs2328IPSourceGuardDynamicEntry,
       "gs2328IPSourceGuardDynamicIndex": gs2328IPSourceGuardDynamicIndex,
       "gs2328IPSourceGuardDynamicPort": gs2328IPSourceGuardDynamicPort,
       "gs2328IPSourceGuardDynamicVLANId": gs2328IPSourceGuardDynamicVLANId,
       "gs2328IPSourceGuardDynamicIPAddress": gs2328IPSourceGuardDynamicIPAddress,
       "gs2328IPSourceGuardDynamicMACAddress": gs2328IPSourceGuardDynamicMACAddress,
       "gs2328ARPInspection": gs2328ARPInspection,
       "gs2328ARPInspectionConf": gs2328ARPInspectionConf,
       "gs2328ARPInspectionConfMode": gs2328ARPInspectionConfMode,
       "gs2328ARPInspectionConfTable": gs2328ARPInspectionConfTable,
       "gs2328ARPInspectionConfEntry": gs2328ARPInspectionConfEntry,
       "gs2328ARPInspectionConfPortIndex": gs2328ARPInspectionConfPortIndex,
       "gs2328ARPInspectionConfPortMode": gs2328ARPInspectionConfPortMode,
       "gs2328ARPInspectionStatic": gs2328ARPInspectionStatic,
       "gs2328ARPInspectionStaticCreate": gs2328ARPInspectionStaticCreate,
       "gs2328ARPInspectionStaticTable": gs2328ARPInspectionStaticTable,
       "gs2328ARPInspectionStaticEntry": gs2328ARPInspectionStaticEntry,
       "gs2328ARPInspectionStaticIndex": gs2328ARPInspectionStaticIndex,
       "gs2328ARPInspectionStaticPort": gs2328ARPInspectionStaticPort,
       "gs2328ARPInspectionStaticVLANId": gs2328ARPInspectionStaticVLANId,
       "gs2328ARPInspectionStaticIPAddress": gs2328ARPInspectionStaticIPAddress,
       "gs2328ARPInspectionStaticMACAddress": gs2328ARPInspectionStaticMACAddress,
       "gs2328ARPInspectionStaticRowStatus": gs2328ARPInspectionStaticRowStatus,
       "gs2328ARPInspectionDynamicTable": gs2328ARPInspectionDynamicTable,
       "gs2328ARPInspectionDynamicEntry": gs2328ARPInspectionDynamicEntry,
       "gs2328ARPInspectionDynamicIndex": gs2328ARPInspectionDynamicIndex,
       "gs2328ARPInspectionDynamicPort": gs2328ARPInspectionDynamicPort,
       "gs2328ARPInspectionDynamicVLANId": gs2328ARPInspectionDynamicVLANId,
       "gs2328ARPInspectionDynamicIPAddress": gs2328ARPInspectionDynamicIPAddress,
       "gs2328ARPInspectionDynamicMACAddress": gs2328ARPInspectionDynamicMACAddress,
       "gs2328ARPStaticGatewayCtrl": gs2328ARPStaticGatewayCtrl,
       "gs2328ARPStaticGatewayCtrlSystemConf": gs2328ARPStaticGatewayCtrlSystemConf,
       "gs2328ARPStaticGatewayCtrlMode": gs2328ARPStaticGatewayCtrlMode,
       "gs2328ARPStaticGatewayCtrlCreate": gs2328ARPStaticGatewayCtrlCreate,
       "gs2328ARPStaticGatewayCtrlTable": gs2328ARPStaticGatewayCtrlTable,
       "gs2328ARPStaticGatewayCtrlEntry": gs2328ARPStaticGatewayCtrlEntry,
       "gs2328ARPStaticGatewayCtrlIndex": gs2328ARPStaticGatewayCtrlIndex,
       "gs2328ARPStaticGatewayCtrlIPAddress": gs2328ARPStaticGatewayCtrlIPAddress,
       "gs2328ARPStaticGatewayCtrlMACAddress": gs2328ARPStaticGatewayCtrlMACAddress,
       "gs2328ARPStaticGatewayCtrlPort": gs2328ARPStaticGatewayCtrlPort,
       "gs2328ARPStaticGatewayCtrlAction": gs2328ARPStaticGatewayCtrlAction,
       "gs2328ARPStaticGatewayCtrlState": gs2328ARPStaticGatewayCtrlState,
       "gs2328ARPStaticGatewayCtrlReOpen": gs2328ARPStaticGatewayCtrlReOpen,
       "gs2328ARPStaticGatewayCtrlRowStatus": gs2328ARPStaticGatewayCtrlRowStatus,
       "gs2328ARPSpoofingPrevention": gs2328ARPSpoofingPrevention,
       "gs2328ARPSpoofingPreventionSystemConf": gs2328ARPSpoofingPreventionSystemConf,
       "gs2328ARPSpoofingPreventionMode": gs2328ARPSpoofingPreventionMode,
       "gs2328ARPSpoofingPreventionTable": gs2328ARPSpoofingPreventionTable,
       "gs2328ARPSpoofingPreventionEntry": gs2328ARPSpoofingPreventionEntry,
       "gs2328ARPSpoofingPreventionPort": gs2328ARPSpoofingPreventionPort,
       "gs2328ARPSpoofingPreventionPortMode": gs2328ARPSpoofingPreventionPortMode,
       "gs2328ARPSpoofingPreventionPortLimit": gs2328ARPSpoofingPreventionPortLimit,
       "gs2328ARPSpoofingPreventionPortAction": gs2328ARPSpoofingPreventionPortAction,
       "gs2328ARPSpoofingPreventionPortState": gs2328ARPSpoofingPreventionPortState,
       "gs2328ARPSpoofingPreventionPortReOpen": gs2328ARPSpoofingPreventionPortReOpen,
       "gs2328ARPIPDoSPrevention": gs2328ARPIPDoSPrevention,
       "gs2328ARPIPDoSPreventionTCPMode": gs2328ARPIPDoSPreventionTCPMode,
       "gs2328ARPIPDoSPreventionUDPMode": gs2328ARPIPDoSPreventionUDPMode,
       "gs2328ARPIPDoSPreventionICMPMode": gs2328ARPIPDoSPreventionICMPMode,
       "gs2328ARPIPDoSPreventionServerPort1": gs2328ARPIPDoSPreventionServerPort1,
       "gs2328ARPIPDoSPreventionServerPort2": gs2328ARPIPDoSPreventionServerPort2,
       "gs2328ARPIPDoSPreventionServerPort3": gs2328ARPIPDoSPreventionServerPort3,
       "gs2328ARPIPDoSPreventionServerPort4": gs2328ARPIPDoSPreventionServerPort4,
       "gs2328DHCPSnooping": gs2328DHCPSnooping,
       "gs2328DHCPSnoopingConf": gs2328DHCPSnoopingConf,
       "gs2328DHCPSnoopingMode": gs2328DHCPSnoopingMode,
       "gs2328DHCPSnoopingPortModeConfigurationTable": gs2328DHCPSnoopingPortModeConfigurationTable,
       "gs2328DHCPSnoopingPortModeConfigurationEntry": gs2328DHCPSnoopingPortModeConfigurationEntry,
       "gs2328DHCPSnoopingPortModeConfigurationPort": gs2328DHCPSnoopingPortModeConfigurationPort,
       "gs2328DHCPSnoopingPortModeConfigurationMode": gs2328DHCPSnoopingPortModeConfigurationMode,
       "gs2328DHCPSnoopingStatisticsTable": gs2328DHCPSnoopingStatisticsTable,
       "gs2328DHCPSnoopingStatisticsEntry": gs2328DHCPSnoopingStatisticsEntry,
       "gs2328DHCPSnoopingStatisticsPort": gs2328DHCPSnoopingStatisticsPort,
       "gs2328DHCPSnoopingStatisticsClear": gs2328DHCPSnoopingStatisticsClear,
       "gs2328DHCPSnoopingRxDiscover": gs2328DHCPSnoopingRxDiscover,
       "gs2328DHCPSnoopingRxOffer": gs2328DHCPSnoopingRxOffer,
       "gs2328DHCPSnoopingRxRequest": gs2328DHCPSnoopingRxRequest,
       "gs2328DHCPSnoopingRxDecline": gs2328DHCPSnoopingRxDecline,
       "gs2328DHCPSnoopingRxACK": gs2328DHCPSnoopingRxACK,
       "gs2328DHCPSnoopingRxNAK": gs2328DHCPSnoopingRxNAK,
       "gs2328DHCPSnoopingRxRelease": gs2328DHCPSnoopingRxRelease,
       "gs2328DHCPSnoopingRxInform": gs2328DHCPSnoopingRxInform,
       "gs2328DHCPSnoopingRxLeaseQuery": gs2328DHCPSnoopingRxLeaseQuery,
       "gs2328DHCPSnoopingRxLeaseUnassigned": gs2328DHCPSnoopingRxLeaseUnassigned,
       "gs2328DHCPSnoopingRxLeaseUnknown": gs2328DHCPSnoopingRxLeaseUnknown,
       "gs2328DHCPSnoopingRxLeaseActive": gs2328DHCPSnoopingRxLeaseActive,
       "gs2328DHCPSnoopingTxDiscover": gs2328DHCPSnoopingTxDiscover,
       "gs2328DHCPSnoopingTxOffer": gs2328DHCPSnoopingTxOffer,
       "gs2328DHCPSnoopingTxRequest": gs2328DHCPSnoopingTxRequest,
       "gs2328DHCPSnoopingTxDecline": gs2328DHCPSnoopingTxDecline,
       "gs2328DHCPSnoopingTxACK": gs2328DHCPSnoopingTxACK,
       "gs2328DHCPSnoopingTxNAK": gs2328DHCPSnoopingTxNAK,
       "gs2328DHCPSnoopingTxRelease": gs2328DHCPSnoopingTxRelease,
       "gs2328DHCPSnoopingTxInform": gs2328DHCPSnoopingTxInform,
       "gs2328DHCPSnoopingTxLeaseQuery": gs2328DHCPSnoopingTxLeaseQuery,
       "gs2328DHCPSnoopingTxLeaseUnassigned": gs2328DHCPSnoopingTxLeaseUnassigned,
       "gs2328DHCPSnoopingTxLeaseUnknown": gs2328DHCPSnoopingTxLeaseUnknown,
       "gs2328DHCPSnoopingTxLeaseActive": gs2328DHCPSnoopingTxLeaseActive,
       "gs2328DHCPRelay": gs2328DHCPRelay,
       "gs2328DHCPRelayConfiguration": gs2328DHCPRelayConfiguration,
       "gs2328DHCPRelayMode": gs2328DHCPRelayMode,
       "gs2328DHCPRelayServer": gs2328DHCPRelayServer,
       "gs2328DHCPRelayInformationMode": gs2328DHCPRelayInformationMode,
       "gs2328DHCPRelayInformationPolicy": gs2328DHCPRelayInformationPolicy,
       "gs2328DHCPRelayConfigurationGateways": gs2328DHCPRelayConfigurationGateways,
       "gs2328DHCPRelayConfigurationGatewaysCreate": gs2328DHCPRelayConfigurationGatewaysCreate,
       "gs2328DHCPRelayConfigurationGatewaysTable": gs2328DHCPRelayConfigurationGatewaysTable,
       "gs2328DHCPRelayConfigurationGatewaysEntry": gs2328DHCPRelayConfigurationGatewaysEntry,
       "gs2328DHCPRelayConfigurationGatewaysIndex": gs2328DHCPRelayConfigurationGatewaysIndex,
       "gs2328DHCPRelayConfigurationGatewaysVLANId": gs2328DHCPRelayConfigurationGatewaysVLANId,
       "gs2328DHCPRelayConfigurationGatewaysIP": gs2328DHCPRelayConfigurationGatewaysIP,
       "gs2328DHCPRelayConfigurationGatewaysRowStatus": gs2328DHCPRelayConfigurationGatewaysRowStatus,
       "gs2328DHCPRelayInformationCustom": gs2328DHCPRelayInformationCustom,
       "gs2328DHCPRelayStatistics": gs2328DHCPRelayStatistics,
       "gs2328DHCPRelayServerStatistics": gs2328DHCPRelayServerStatistics,
       "gs2328ServerStatTransmitToServer": gs2328ServerStatTransmitToServer,
       "gs2328ServerStatTransmitError": gs2328ServerStatTransmitError,
       "gs2328ServerStatReceiveFromServer": gs2328ServerStatReceiveFromServer,
       "gs2328ServerStatReceiveMissingAgentOption": gs2328ServerStatReceiveMissingAgentOption,
       "gs2328ServerStatReceiveMissingCircuitID": gs2328ServerStatReceiveMissingCircuitID,
       "gs2328ServerStatReceiveMissingRemoteID": gs2328ServerStatReceiveMissingRemoteID,
       "gs2328ServerStatReceiveBadCircuitID": gs2328ServerStatReceiveBadCircuitID,
       "gs2328ServerStatReceiveBadRemoteID": gs2328ServerStatReceiveBadRemoteID,
       "gs2328DHCPRelayClientStatistics": gs2328DHCPRelayClientStatistics,
       "gs2328ClientStatTransmitToClient": gs2328ClientStatTransmitToClient,
       "gs2328ClientStatTransmitError": gs2328ClientStatTransmitError,
       "gs2328ClientStatReceivefromClient": gs2328ClientStatReceivefromClient,
       "gs2328ClientStatReceiveAgentOption": gs2328ClientStatReceiveAgentOption,
       "gs2328ClientStatReplaceAgentOption": gs2328ClientStatReplaceAgentOption,
       "gs2328ClientStatKeepAgentOption": gs2328ClientStatKeepAgentOption,
       "gs2328ClientStatDropAgentOption": gs2328ClientStatDropAgentOption,
       "gs2328PortSecurity": gs2328PortSecurity,
       "gs2328PortSecLimitCtrl": gs2328PortSecLimitCtrl,
       "gs2328PortSecLimitCtrlSystemConf": gs2328PortSecLimitCtrlSystemConf,
       "gs2328PortSecurityMode": gs2328PortSecurityMode,
       "gs2328PortSecurityAging": gs2328PortSecurityAging,
       "gs2328PortSecurityAgingPeriod": gs2328PortSecurityAgingPeriod,
       "gs2328PortSecLimitCtrlTable": gs2328PortSecLimitCtrlTable,
       "gs2328PortSecLimitCtrlEntry": gs2328PortSecLimitCtrlEntry,
       "gs2328PortSecLimitCtrlPort": gs2328PortSecLimitCtrlPort,
       "gs2328PortSecLimitCtrlPortMode": gs2328PortSecLimitCtrlPortMode,
       "gs2328PortSecLimitCtrlPortLimit": gs2328PortSecLimitCtrlPortLimit,
       "gs2328PortSecLimitCtrlPortAction": gs2328PortSecLimitCtrlPortAction,
       "gs2328PortSecLimitCtrlPortState": gs2328PortSecLimitCtrlPortState,
       "gs2328PortSecLimitCtrlPortReOpen": gs2328PortSecLimitCtrlPortReOpen,
       "gs2328PortSecSwitchStatusTable": gs2328PortSecSwitchStatusTable,
       "gs2328PortSecSwitchStatusEntry": gs2328PortSecSwitchStatusEntry,
       "gs2328PortSecSwitchStatusPort": gs2328PortSecSwitchStatusPort,
       "gs2328PortSecSwitchStatusUsers": gs2328PortSecSwitchStatusUsers,
       "gs2328PortSecSwitchStatusState": gs2328PortSecSwitchStatusState,
       "gs2328PortSecSwitchStatusMACCountCurrent": gs2328PortSecSwitchStatusMACCountCurrent,
       "gs2328PortSecSwitchStatusMACCountLimit": gs2328PortSecSwitchStatusMACCountLimit,
       "gs2328PortSecPortStatus": gs2328PortSecPortStatus,
       "gs2328PortSecPortStatusPort": gs2328PortSecPortStatusPort,
       "gs2328PortSecPortStatusTable": gs2328PortSecPortStatusTable,
       "gs2328PortSecPortStatusEntry": gs2328PortSecPortStatusEntry,
       "gs2328PortSecPortStatusIndex": gs2328PortSecPortStatusIndex,
       "gs2328PortSecPortStatusMACAddress": gs2328PortSecPortStatusMACAddress,
       "gs2328PortSecPortStatusVLANId": gs2328PortSecPortStatusVLANId,
       "gs2328PortSecPortStatusState": gs2328PortSecPortStatusState,
       "gs2328PortSecPortStatusTimeOfAddition": gs2328PortSecPortStatusTimeOfAddition,
       "gs2328PortSecPortStatusAgeAndHold": gs2328PortSecPortStatusAgeAndHold,
       "gs2328AccessManagement": gs2328AccessManagement,
       "gs2328AccessMgtConf": gs2328AccessMgtConf,
       "gs2328AccessMgtConfMode": gs2328AccessMgtConfMode,
       "gs2328AccessMgtConfCreate": gs2328AccessMgtConfCreate,
       "gs2328AccessMgtConfTable": gs2328AccessMgtConfTable,
       "gs2328AccessMgtConfEntry": gs2328AccessMgtConfEntry,
       "gs2328AccessMgtIndex": gs2328AccessMgtIndex,
       "gs2328AccessMgtAddresstype": gs2328AccessMgtAddresstype,
       "gs2328AccessMgtStartIpAddress": gs2328AccessMgtStartIpAddress,
       "gs2328AccessMgtEndIpAddress": gs2328AccessMgtEndIpAddress,
       "gs2328AccessMgtHttpHttps": gs2328AccessMgtHttpHttps,
       "gs2328AccessMgtSNMP": gs2328AccessMgtSNMP,
       "gs2328AccessMgtTelnetSSH": gs2328AccessMgtTelnetSSH,
       "gs2328AccessMgtRowStatus": gs2328AccessMgtRowStatus,
       "gs2328AccessMgtStatistics": gs2328AccessMgtStatistics,
       "gs2328HttpReceivedPkts": gs2328HttpReceivedPkts,
       "gs2328HttpAllowedPkts": gs2328HttpAllowedPkts,
       "gs2328HttpDiscardedPkts": gs2328HttpDiscardedPkts,
       "gs2328HttpsReceivedPkts": gs2328HttpsReceivedPkts,
       "gs2328HttpsAllowedPkts": gs2328HttpsAllowedPkts,
       "gs2328HttpsDiscardedPkts": gs2328HttpsDiscardedPkts,
       "gs2328SnmpReceivedPkts": gs2328SnmpReceivedPkts,
       "gs2328SnmpAllowedPkts": gs2328SnmpAllowedPkts,
       "gs2328SnmpDiscardedPkts": gs2328SnmpDiscardedPkts,
       "gs2328TelnetReceivedPkts": gs2328TelnetReceivedPkts,
       "gs2328TelnetAllowedPkts": gs2328TelnetAllowedPkts,
       "gs2328TelnetDiscardedPkts": gs2328TelnetDiscardedPkts,
       "gs2328SSHReceivedPkts": gs2328SSHReceivedPkts,
       "gs2328SSHAllowedPkts": gs2328SSHAllowedPkts,
       "gs2328SSHDiscardedPkts": gs2328SSHDiscardedPkts,
       "gs2328AccessMgtStatisticsClearAll": gs2328AccessMgtStatisticsClearAll,
       "gs2328SSH": gs2328SSH,
       "gs2328SSHMode": gs2328SSHMode,
       "gs2328HTTPS": gs2328HTTPS,
       "gs2328HTTPSMode": gs2328HTTPSMode,
       "gs2328HTTPSAutoRedirect": gs2328HTTPSAutoRedirect,
       "gs2328HTTPSCertRenew": gs2328HTTPSCertRenew,
       "gs2328HTTPSMinProtoVersion": gs2328HTTPSMinProtoVersion,
       "gs2328HTTPMode": gs2328HTTPMode,
       "gs2328AuthMethod": gs2328AuthMethod,
       "gs2328ConsoleAuthMethod": gs2328ConsoleAuthMethod,
       "gs2328ConsoleFallback": gs2328ConsoleFallback,
       "gs2328TelnetAuthMethod": gs2328TelnetAuthMethod,
       "gs2328TelnetFallback": gs2328TelnetFallback,
       "gs2328SshAuthMethod": gs2328SshAuthMethod,
       "gs2328SshFallback": gs2328SshFallback,
       "gs2328TftpAuthMethod": gs2328TftpAuthMethod,
       "gs2328TftpFallback": gs2328TftpFallback,
       "gs2328LoginFailures": gs2328LoginFailures,
       "gs2328LockMinutes": gs2328LockMinutes,
       "gs2328HttpAuthMethod": gs2328HttpAuthMethod,
       "gs2328HttpFallback": gs2328HttpFallback,
       "gs2328HttpsAuthMethod": gs2328HttpsAuthMethod,
       "gs2328HttpsFallback": gs2328HttpsFallback,
       "gs2328AAA": gs2328AAA,
       "gs2328AAACommonServer": gs2328AAACommonServer,
       "gs2328AAACommonServerTimeout": gs2328AAACommonServerTimeout,
       "gs2328AAACommonServerDeadTime": gs2328AAACommonServerDeadTime,
       "gs2328AAATACACSPlusAuthAndAccounting": gs2328AAATACACSPlusAuthAndAccounting,
       "gs2328AAAAuthorization": gs2328AAAAuthorization,
       "gs2328AAAFallbackToLocalAuthorization": gs2328AAAFallbackToLocalAuthorization,
       "gs2328AAAAccounting": gs2328AAAAccounting,
       "gs2328RADIUSAuthenticationServerTable": gs2328RADIUSAuthenticationServerTable,
       "gs2328RADIUSAuthenticationServerEntry": gs2328RADIUSAuthenticationServerEntry,
       "gs2328RADIUSAuthenticationServerIndex": gs2328RADIUSAuthenticationServerIndex,
       "gs2328RADIUSAuthenticationServerEnable": gs2328RADIUSAuthenticationServerEnable,
       "gs2328RADIUSAuthenticationServerIP": gs2328RADIUSAuthenticationServerIP,
       "gs2328RADIUSAuthenticationServerPort": gs2328RADIUSAuthenticationServerPort,
       "gs2328RADIUSAuthenticationServerSecret": gs2328RADIUSAuthenticationServerSecret,
       "gs2328RADIUSAccountingServerTable": gs2328RADIUSAccountingServerTable,
       "gs2328RADIUSAccountingServerEntry": gs2328RADIUSAccountingServerEntry,
       "gs2328RADIUSAccountingServerIndex": gs2328RADIUSAccountingServerIndex,
       "gs2328RADIUSAccountingServerEnable": gs2328RADIUSAccountingServerEnable,
       "gs2328RADIUSAccountingServerIP": gs2328RADIUSAccountingServerIP,
       "gs2328RADIUSAccountingServerPort": gs2328RADIUSAccountingServerPort,
       "gs2328RADIUSAccountingServerSecret": gs2328RADIUSAccountingServerSecret,
       "gs2328TACACSPlusAuthenticationServerTable": gs2328TACACSPlusAuthenticationServerTable,
       "gs2328TACACSPlusAuthenticationServerEntry": gs2328TACACSPlusAuthenticationServerEntry,
       "gs2328TACACSPlusAuthenticationServerIndex": gs2328TACACSPlusAuthenticationServerIndex,
       "gs2328TACACSPlusAuthenticationServerEnable": gs2328TACACSPlusAuthenticationServerEnable,
       "gs2328TACACSPlusAuthenticationServerIP": gs2328TACACSPlusAuthenticationServerIP,
       "gs2328TACACSPlusAuthenticationServerPort": gs2328TACACSPlusAuthenticationServerPort,
       "gs2328TACACSPlusAuthenticationServerSecret": gs2328TACACSPlusAuthenticationServerSecret,
       "gs2328RADIUSStatisticsTable": gs2328RADIUSStatisticsTable,
       "gs2328RADIUSStatisticsEntry": gs2328RADIUSStatisticsEntry,
       "gs2328RADIUSAuthStatisticsServerIndex": gs2328RADIUSAuthStatisticsServerIndex,
       "gs2328RADIUSAuthStatisticsRecPktAccessAccepts": gs2328RADIUSAuthStatisticsRecPktAccessAccepts,
       "gs2328RADIUSAuthStatisticsRecPktAccessRejects": gs2328RADIUSAuthStatisticsRecPktAccessRejects,
       "gs2328RADIUSAuthStatisticsRecPktAccessChallenges": gs2328RADIUSAuthStatisticsRecPktAccessChallenges,
       "gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses": gs2328RADIUSAuthStatisticsRecPktMalformedAccResponses,
       "gs2328RADIUSAuthStatisticsRecPktBadAuthenticators": gs2328RADIUSAuthStatisticsRecPktBadAuthenticators,
       "gs2328RADIUSAuthStatisticsRecPktUnknownTypes": gs2328RADIUSAuthStatisticsRecPktUnknownTypes,
       "gs2328RADIUSAuthStatisticsRecPktDropped": gs2328RADIUSAuthStatisticsRecPktDropped,
       "gs2328RADIUSAuthStatisticsTransmitPktAccessRequests": gs2328RADIUSAuthStatisticsTransmitPktAccessRequests,
       "gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions": gs2328RADIUSAuthStatisticsTransmitPktAccessRetransmissions,
       "gs2328RADIUSAuthStatisticsTransmitPktPendingRequests": gs2328RADIUSAuthStatisticsTransmitPktPendingRequests,
       "gs2328RADIUSAuthStatisticsTransmitPktTimeouts": gs2328RADIUSAuthStatisticsTransmitPktTimeouts,
       "gs2328RADIUSAuthIP": gs2328RADIUSAuthIP,
       "gs2328RADIUSAuthState": gs2328RADIUSAuthState,
       "gs2328RADIUSAuthRoundTripTime": gs2328RADIUSAuthRoundTripTime,
       "gs2328RADIUSAccountingStatisticsRecPktResponses": gs2328RADIUSAccountingStatisticsRecPktResponses,
       "gs2328RADIUSAccountingStatisticsRecPktMalformedResponses": gs2328RADIUSAccountingStatisticsRecPktMalformedResponses,
       "gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators": gs2328RADIUSAccountingStatisticsRecPktBadAuthenticators,
       "gs2328RADIUSAccountingStatisticsRecPktUnknownTypes": gs2328RADIUSAccountingStatisticsRecPktUnknownTypes,
       "gs2328RADIUSAccountingStatisticsRecPktDropped": gs2328RADIUSAccountingStatisticsRecPktDropped,
       "gs2328RADIUSAccountingStatisticsTransmitPktRequests": gs2328RADIUSAccountingStatisticsTransmitPktRequests,
       "gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions": gs2328RADIUSAccountingStatisticsTransmitPktRetransmissions,
       "gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests": gs2328RADIUSAccountingStatisticsTransmitPktPendingRequests,
       "gs2328RADIUSAccountingStatisticsTransmitPktTimeouts": gs2328RADIUSAccountingStatisticsTransmitPktTimeouts,
       "gs2328RADIUSAccountingIP": gs2328RADIUSAccountingIP,
       "gs2328RADIUSAccountingState": gs2328RADIUSAccountingState,
       "gs2328RADIUSAccountingRoundTripTime": gs2328RADIUSAccountingRoundTripTime,
       "gs2328RADIUSStatisticsClear": gs2328RADIUSStatisticsClear,
       "gs2328NAS": gs2328NAS,
       "gs2328NASConfiguration": gs2328NASConfiguration,
       "gs2328NASConfigMode": gs2328NASConfigMode,
       "gs2328NASConfigReauthEnabled": gs2328NASConfigReauthEnabled,
       "gs2328NASConfigReauthPeriod": gs2328NASConfigReauthPeriod,
       "gs2328NASConfigEAPOLTimeout": gs2328NASConfigEAPOLTimeout,
       "gs2328NASConfigAgingPeriod": gs2328NASConfigAgingPeriod,
       "gs2328NASConfigHoldTime": gs2328NASConfigHoldTime,
       "gs2328NASConfigRADIUSAssignedQoSEnabled": gs2328NASConfigRADIUSAssignedQoSEnabled,
       "gs2328NASConfigRADIUSAssignedVLANEnabled": gs2328NASConfigRADIUSAssignedVLANEnabled,
       "gs2328NASConfigGuestVLANEnabled": gs2328NASConfigGuestVLANEnabled,
       "gs2328NASConfigGuestVLANID": gs2328NASConfigGuestVLANID,
       "gs2328NASConfigMaxReauthCount": gs2328NASConfigMaxReauthCount,
       "gs2328NASConfigAllowGuestVLANEAPOLSeen": gs2328NASConfigAllowGuestVLANEAPOLSeen,
       "gs2328NASPortConfigTable": gs2328NASPortConfigTable,
       "gs2328NASPortConfigEntry": gs2328NASPortConfigEntry,
       "gs2328NASPortConfigPort": gs2328NASPortConfigPort,
       "gs2328NASPortConfigAdminState": gs2328NASPortConfigAdminState,
       "gs2328NASPortConfigRADIUSAssignedQoSEnabled": gs2328NASPortConfigRADIUSAssignedQoSEnabled,
       "gs2328NASPortConfigRADIUSAssignedVLANEnabled": gs2328NASPortConfigRADIUSAssignedVLANEnabled,
       "gs2328NASPortConfigGuestVLANEnabled": gs2328NASPortConfigGuestVLANEnabled,
       "gs2328NASPortConfigPortState": gs2328NASPortConfigPortState,
       "gs2328NASPortConfigReauthenticate": gs2328NASPortConfigReauthenticate,
       "gs2328NASPortConfigReinitialize": gs2328NASPortConfigReinitialize,
       "gs2328NASPortConfigFallbackEnabled": gs2328NASPortConfigFallbackEnabled,
       "gs2328NASConfigMacBasedUseEAP": gs2328NASConfigMacBasedUseEAP,
       "gs2328NASSwitchStatusTable": gs2328NASSwitchStatusTable,
       "gs2328NASSwitchStatusEntry": gs2328NASSwitchStatusEntry,
       "gs2328NASSwitchStatusAdminState": gs2328NASSwitchStatusAdminState,
       "gs2328NASSwitchStatusPortState": gs2328NASSwitchStatusPortState,
       "gs2328NASSwitchStatusLastSource": gs2328NASSwitchStatusLastSource,
       "gs2328NASSwitchStatusLastID": gs2328NASSwitchStatusLastID,
       "gs2328NASSwitchStatusQoSClass": gs2328NASSwitchStatusQoSClass,
       "gs2328NASSwitchStatusPortVlanID": gs2328NASSwitchStatusPortVlanID,
       "gs2328NASPortStatus": gs2328NASPortStatus,
       "gs2328NASPortStatusCountersTable": gs2328NASPortStatusCountersTable,
       "gs2328NASPortStatusCountersEntry": gs2328NASPortStatusCountersEntry,
       "gs2328NASRxCountersEAPOLTotal": gs2328NASRxCountersEAPOLTotal,
       "gs2328NASRxCountersEAPOLResponseID": gs2328NASRxCountersEAPOLResponseID,
       "gs2328NASRxCountersEAPOLResponses": gs2328NASRxCountersEAPOLResponses,
       "gs2328NASRxCountersEAPOLStart": gs2328NASRxCountersEAPOLStart,
       "gs2328NASRxCountersEAPOLLogoff": gs2328NASRxCountersEAPOLLogoff,
       "gs2328NASRxCountersEAPOLInvalidType": gs2328NASRxCountersEAPOLInvalidType,
       "gs2328NASRxCountersEAPOLInvalidLength": gs2328NASRxCountersEAPOLInvalidLength,
       "gs2328NASTxCountersEAPOLTotal": gs2328NASTxCountersEAPOLTotal,
       "gs2328NASTxCountersEAPOLRequestID": gs2328NASTxCountersEAPOLRequestID,
       "gs2328NASTxCountersEAPOLRequests": gs2328NASTxCountersEAPOLRequests,
       "gs2328NASRxBackendServerCountersAccessChallenges": gs2328NASRxBackendServerCountersAccessChallenges,
       "gs2328NASRxBackendServerCountersOtherRequests": gs2328NASRxBackendServerCountersOtherRequests,
       "gs2328NASRxBackendServerCountersAuthSuccesses": gs2328NASRxBackendServerCountersAuthSuccesses,
       "gs2328NASRxBackendServerCountersAuthFailures": gs2328NASRxBackendServerCountersAuthFailures,
       "gs2328NASTxBackendServerCountersResponses": gs2328NASTxBackendServerCountersResponses,
       "gs2328NASLastSupplicantInfoMACAddress": gs2328NASLastSupplicantInfoMACAddress,
       "gs2328NASLastSupplicantInfoVlanID": gs2328NASLastSupplicantInfoVlanID,
       "gs2328NASLastSupplicantInfoVersion": gs2328NASLastSupplicantInfoVersion,
       "gs2328NASLastSupplicantInfoIdentity": gs2328NASLastSupplicantInfoIdentity,
       "gs2328NASCountersDoClear": gs2328NASCountersDoClear,
       "gs2328NASPortStatusClientsTable": gs2328NASPortStatusClientsTable,
       "gs2328NASPortStatusClientsEntry": gs2328NASPortStatusClientsEntry,
       "gs2328NASClientsIndex": gs2328NASClientsIndex,
       "gs2328NASClientsIdentity": gs2328NASClientsIdentity,
       "gs2328NASClientsMACAddress": gs2328NASClientsMACAddress,
       "gs2328NASClientsVlanID": gs2328NASClientsVlanID,
       "gs2328NASClientsState": gs2328NASClientsState,
       "gs2328NASClientsLastAuth": gs2328NASClientsLastAuth,
       "gs2328NASRxClientsEAPOLTotal": gs2328NASRxClientsEAPOLTotal,
       "gs2328NASRxClientsEAPOLResponseID": gs2328NASRxClientsEAPOLResponseID,
       "gs2328NASRxClientsEAPOLResponses": gs2328NASRxClientsEAPOLResponses,
       "gs2328NASRxClientsEAPOLStart": gs2328NASRxClientsEAPOLStart,
       "gs2328NASRxClientsEAPOLLogoff": gs2328NASRxClientsEAPOLLogoff,
       "gs2328NASRxClientsEAPOLInvalidType": gs2328NASRxClientsEAPOLInvalidType,
       "gs2328NASRxClientsEAPOLInvalidLength": gs2328NASRxClientsEAPOLInvalidLength,
       "gs2328NASTxClientsEAPOLTotal": gs2328NASTxClientsEAPOLTotal,
       "gs2328NASTxClientsEAPOLRequestID": gs2328NASTxClientsEAPOLRequestID,
       "gs2328NASTxClientsEAPOLRequests": gs2328NASTxClientsEAPOLRequests,
       "gs2328NASRxBackendServerClientsAccessChallenges": gs2328NASRxBackendServerClientsAccessChallenges,
       "gs2328NASRxBackendServerClientsOtherRequests": gs2328NASRxBackendServerClientsOtherRequests,
       "gs2328NASRxBackendServerClientsAuthSuccesses": gs2328NASRxBackendServerClientsAuthSuccesses,
       "gs2328NASRxBackendServerClientsAuthFailures": gs2328NASRxBackendServerClientsAuthFailures,
       "gs2328NASTxBackendServerClientsResponses": gs2328NASTxBackendServerClientsResponses,
       "gs2328Maintenance": gs2328Maintenance,
       "gs2328RestartDevice": gs2328RestartDevice,
       "gs2328Firmware": gs2328Firmware,
       "gs2328FirmwareIpAddress": gs2328FirmwareIpAddress,
       "gs2328FirmwareFileName": gs2328FirmwareFileName,
       "gs2328DoFirmwareUpgrade": gs2328DoFirmwareUpgrade,
       "gs2328SaveOrRestore": gs2328SaveOrRestore,
       "gs2328FactoryDefaults": gs2328FactoryDefaults,
       "gs2328SaveStart": gs2328SaveStart,
       "gs2328SaveUser": gs2328SaveUser,
       "gs2328RestoreUser": gs2328RestoreUser,
       "gs2328ExportOrImport": gs2328ExportOrImport,
       "gs2328ExportIpAddress": gs2328ExportIpAddress,
       "gs2328ExportConfigName": gs2328ExportConfigName,
       "gs2328DoExportConfig": gs2328DoExportConfig,
       "gs2328ImportIpAddress": gs2328ImportIpAddress,
       "gs2328ImportConfigName": gs2328ImportConfigName,
       "gs2328DoImportConfig": gs2328DoImportConfig,
       "gs2328Diagnostics": gs2328Diagnostics,
       "gs2328PingIpAddress": gs2328PingIpAddress,
       "gs2328PingSize": gs2328PingSize,
       "gs2328DoPingConfig": gs2328DoPingConfig,
       "gs2328PingResult": gs2328PingResult,
       "gs2328Ping6IpAddress": gs2328Ping6IpAddress,
       "gs2328Ping6Size": gs2328Ping6Size,
       "gs2328DoPing6Config": gs2328DoPing6Config,
       "gs2328Ping6Result": gs2328Ping6Result,
       "gs2328ColdRestartDevice": gs2328ColdRestartDevice,
       "gs2328Trap": gs2328Trap,
       "gs2328TrapEvent": gs2328TrapEvent,
       "gs2328Emergency": gs2328Emergency,
       "gs2328Alert": gs2328Alert,
       "gs2328Critical": gs2328Critical,
       "gs2328Error": gs2328Error,
       "gs2328Warning": gs2328Warning,
       "gs2328Notice": gs2328Notice,
       "gs2328Informational": gs2328Informational,
       "gs2328Debug": gs2328Debug,
       "gs2328TrapVariable": gs2328TrapVariable,
       "gs2328Information": gs2328Information}
)
