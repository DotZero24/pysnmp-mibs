# SNMP MIB module (LANCOM-GS2310-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-GS2310-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:22 2025
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
_LancomGS2310_ObjectIdentity = ObjectIdentity
lancomGS2310 = _LancomGS2310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313)
)
_Gs2310System_ObjectIdentity = ObjectIdentity
gs2310System = _Gs2310System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1)
)
_Gs2310SystemInformation_ObjectIdentity = ObjectIdentity
gs2310SystemInformation = _Gs2310SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1)
)
_Gs2310ModelName_Type = DisplayString
_Gs2310ModelName_Object = MibScalar
gs2310ModelName = _Gs2310ModelName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 1),
    _Gs2310ModelName_Type()
)
gs2310ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ModelName.setStatus("current")
_Gs2310BIOSVersion_Type = DisplayString
_Gs2310BIOSVersion_Object = MibScalar
gs2310BIOSVersion = _Gs2310BIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 2),
    _Gs2310BIOSVersion_Type()
)
gs2310BIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310BIOSVersion.setStatus("current")
_Gs2310FirmwareVersion_Type = DisplayString
_Gs2310FirmwareVersion_Object = MibScalar
gs2310FirmwareVersion = _Gs2310FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 3),
    _Gs2310FirmwareVersion_Type()
)
gs2310FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310FirmwareVersion.setStatus("current")
_Gs2310HardwareMechanicalVersion_Type = DisplayString
_Gs2310HardwareMechanicalVersion_Object = MibScalar
gs2310HardwareMechanicalVersion = _Gs2310HardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 4),
    _Gs2310HardwareMechanicalVersion_Type()
)
gs2310HardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HardwareMechanicalVersion.setStatus("current")
_Gs2310SerialNumber_Type = DisplayString
_Gs2310SerialNumber_Object = MibScalar
gs2310SerialNumber = _Gs2310SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 5),
    _Gs2310SerialNumber_Type()
)
gs2310SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SerialNumber.setStatus("current")
_Gs2310HostMACAddress_Type = MacAddress
_Gs2310HostMACAddress_Object = MibScalar
gs2310HostMACAddress = _Gs2310HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 6),
    _Gs2310HostMACAddress_Type()
)
gs2310HostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HostMACAddress.setStatus("current")
_Gs2310ConsoleBaudrate_Type = DisplayString
_Gs2310ConsoleBaudrate_Object = MibScalar
gs2310ConsoleBaudrate = _Gs2310ConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 7),
    _Gs2310ConsoleBaudrate_Type()
)
gs2310ConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ConsoleBaudrate.setStatus("current")
_Gs2310RAMSize_Type = DisplayString
_Gs2310RAMSize_Object = MibScalar
gs2310RAMSize = _Gs2310RAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 8),
    _Gs2310RAMSize_Type()
)
gs2310RAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RAMSize.setStatus("current")
_Gs2310FlashSize_Type = DisplayString
_Gs2310FlashSize_Object = MibScalar
gs2310FlashSize = _Gs2310FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 9),
    _Gs2310FlashSize_Type()
)
gs2310FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310FlashSize.setStatus("current")
_Gs2310BridgeFDBSize_Type = DisplayString
_Gs2310BridgeFDBSize_Object = MibScalar
gs2310BridgeFDBSize = _Gs2310BridgeFDBSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 10),
    _Gs2310BridgeFDBSize_Type()
)
gs2310BridgeFDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310BridgeFDBSize.setStatus("current")
_Gs2310TransmitQueue_Type = DisplayString
_Gs2310TransmitQueue_Object = MibScalar
gs2310TransmitQueue = _Gs2310TransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 11),
    _Gs2310TransmitQueue_Type()
)
gs2310TransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310TransmitQueue.setStatus("current")
_Gs2310MaximumFrameSize_Type = DisplayString
_Gs2310MaximumFrameSize_Object = MibScalar
gs2310MaximumFrameSize = _Gs2310MaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 12),
    _Gs2310MaximumFrameSize_Type()
)
gs2310MaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MaximumFrameSize.setStatus("current")
_Gs2310CPULoad_Type = DisplayString
_Gs2310CPULoad_Object = MibScalar
gs2310CPULoad = _Gs2310CPULoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 13),
    _Gs2310CPULoad_Type()
)
gs2310CPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CPULoad.setStatus("current")
_Gs2310SystemDescription_Type = DisplayString
_Gs2310SystemDescription_Object = MibScalar
gs2310SystemDescription = _Gs2310SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 21),
    _Gs2310SystemDescription_Type()
)
gs2310SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SystemDescription.setStatus("current")
_Gs2310Location_Type = DisplayString
_Gs2310Location_Object = MibScalar
gs2310Location = _Gs2310Location_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 22),
    _Gs2310Location_Type()
)
gs2310Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Location.setStatus("current")
_Gs2310Contact_Type = DisplayString
_Gs2310Contact_Object = MibScalar
gs2310Contact = _Gs2310Contact_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 23),
    _Gs2310Contact_Type()
)
gs2310Contact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Contact.setStatus("current")
_Gs2310DeviceName_Type = DisplayString
_Gs2310DeviceName_Object = MibScalar
gs2310DeviceName = _Gs2310DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 24),
    _Gs2310DeviceName_Type()
)
gs2310DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DeviceName.setStatus("current")
_Gs2310SystemDate_Type = DisplayString
_Gs2310SystemDate_Object = MibScalar
gs2310SystemDate = _Gs2310SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 25),
    _Gs2310SystemDate_Type()
)
gs2310SystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SystemDate.setStatus("current")
_Gs2310SystemUptime_Type = DisplayString
_Gs2310SystemUptime_Object = MibScalar
gs2310SystemUptime = _Gs2310SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 26),
    _Gs2310SystemUptime_Type()
)
gs2310SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SystemUptime.setStatus("current")
_Gs2310SystemIPv4Address_Type = DisplayString
_Gs2310SystemIPv4Address_Object = MibScalar
gs2310SystemIPv4Address = _Gs2310SystemIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 27),
    _Gs2310SystemIPv4Address_Type()
)
gs2310SystemIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SystemIPv4Address.setStatus("current")
_Gs2310SystemIPv4SubnetMask_Type = DisplayString
_Gs2310SystemIPv4SubnetMask_Object = MibScalar
gs2310SystemIPv4SubnetMask = _Gs2310SystemIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 28),
    _Gs2310SystemIPv4SubnetMask_Type()
)
gs2310SystemIPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SystemIPv4SubnetMask.setStatus("current")
_Gs2310SystemIPv4Gateway_Type = DisplayString
_Gs2310SystemIPv4Gateway_Object = MibScalar
gs2310SystemIPv4Gateway = _Gs2310SystemIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 29),
    _Gs2310SystemIPv4Gateway_Type()
)
gs2310SystemIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SystemIPv4Gateway.setStatus("current")
_Gs2310IPv6LinkLocalAddress_Type = DisplayString
_Gs2310IPv6LinkLocalAddress_Object = MibScalar
gs2310IPv6LinkLocalAddress = _Gs2310IPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 30),
    _Gs2310IPv6LinkLocalAddress_Type()
)
gs2310IPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv6LinkLocalAddress.setStatus("current")
_Gs2310IPv6Address_Type = DisplayString
_Gs2310IPv6Address_Object = MibScalar
gs2310IPv6Address = _Gs2310IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 31),
    _Gs2310IPv6Address_Type()
)
gs2310IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv6Address.setStatus("current")
_Gs2310IPv6Prefix_Type = DisplayString
_Gs2310IPv6Prefix_Object = MibScalar
gs2310IPv6Prefix = _Gs2310IPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 32),
    _Gs2310IPv6Prefix_Type()
)
gs2310IPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv6Prefix.setStatus("current")
_Gs2310IPv6Gateway_Type = DisplayString
_Gs2310IPv6Gateway_Object = MibScalar
gs2310IPv6Gateway = _Gs2310IPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 33),
    _Gs2310IPv6Gateway_Type()
)
gs2310IPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv6Gateway.setStatus("current")
_Gs2310LargestFreeMemBlock_Type = Integer32
_Gs2310LargestFreeMemBlock_Object = MibScalar
gs2310LargestFreeMemBlock = _Gs2310LargestFreeMemBlock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 1500),
    _Gs2310LargestFreeMemBlock_Type()
)
gs2310LargestFreeMemBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LargestFreeMemBlock.setStatus("current")
_Gs2310MemFree_Type = Integer32
_Gs2310MemFree_Object = MibScalar
gs2310MemFree = _Gs2310MemFree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 1, 1501),
    _Gs2310MemFree_Type()
)
gs2310MemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MemFree.setStatus("current")
_Gs2310SystemTime_ObjectIdentity = ObjectIdentity
gs2310SystemTime = _Gs2310SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2)
)
_Gs2310SystemTimeManual_ObjectIdentity = ObjectIdentity
gs2310SystemTimeManual = _Gs2310SystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1)
)


class _Gs2310SystemTimeManualClockSource_Type(Integer32):
    """Custom type gs2310SystemTimeManualClockSource based on Integer32"""
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


_Gs2310SystemTimeManualClockSource_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualClockSource_Object = MibScalar
gs2310SystemTimeManualClockSource = _Gs2310SystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 1),
    _Gs2310SystemTimeManualClockSource_Type()
)
gs2310SystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualClockSource.setStatus("current")
_Gs2310SystemTimeManualLocaltime_Type = DisplayString
_Gs2310SystemTimeManualLocaltime_Object = MibScalar
gs2310SystemTimeManualLocaltime = _Gs2310SystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 2),
    _Gs2310SystemTimeManualLocaltime_Type()
)
gs2310SystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualLocaltime.setStatus("current")


class _Gs2310SystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type gs2310SystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Gs2310SystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualTimeZoneOffset_Object = MibScalar
gs2310SystemTimeManualTimeZoneOffset = _Gs2310SystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 3),
    _Gs2310SystemTimeManualTimeZoneOffset_Type()
)
gs2310SystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualTimeZoneOffset.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavings based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavings_Object = MibScalar
gs2310SystemTimeManualDaylightSavings = _Gs2310SystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 4),
    _Gs2310SystemTimeManualDaylightSavings_Type()
)
gs2310SystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavings.setStatus("current")


class _Gs2310SystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type gs2310SystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Gs2310SystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualTimeSetOffset_Object = MibScalar
gs2310SystemTimeManualTimeSetOffset = _Gs2310SystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 5),
    _Gs2310SystemTimeManualTimeSetOffset_Type()
)
gs2310SystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualTimeSetOffset.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsType based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsType_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsType = _Gs2310SystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 6),
    _Gs2310SystemTimeManualDaylightSavingsType_Type()
)
gs2310SystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsType.setStatus("current")
_Gs2310SystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Gs2310SystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsBydatesFrom = _Gs2310SystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 7),
    _Gs2310SystemTimeManualDaylightSavingsBydatesFrom_Type()
)
gs2310SystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Gs2310SystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Gs2310SystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsBydatesTo = _Gs2310SystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 8),
    _Gs2310SystemTimeManualDaylightSavingsBydatesTo_Type()
)
gs2310SystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringDayFrom = _Gs2310SystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 9),
    _Gs2310SystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom = _Gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 10),
    _Gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom = _Gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 11),
    _Gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom = _Gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 12),
    _Gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringDayTo = _Gs2310SystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 13),
    _Gs2310SystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringWeekTo = _Gs2310SystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 14),
    _Gs2310SystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Gs2310SystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type gs2310SystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
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


_Gs2310SystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Gs2310SystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringMonthTo = _Gs2310SystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 15),
    _Gs2310SystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Gs2310SystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Gs2310SystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
gs2310SystemTimeManualDaylightSavingsRecurringTimeTo = _Gs2310SystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 1, 16),
    _Gs2310SystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
gs2310SystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Gs2310SystemTimeNTP_ObjectIdentity = ObjectIdentity
gs2310SystemTimeNTP = _Gs2310SystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2)
)
_Gs2310SystemTimeNTPTable_Object = MibTable
gs2310SystemTimeNTPTable = _Gs2310SystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPTable.setStatus("current")
_Gs2310SystemTimeNTPEntry_Object = MibTableRow
gs2310SystemTimeNTPEntry = _Gs2310SystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 1, 1)
)
gs2310SystemTimeNTPEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPEntry.setStatus("current")


class _Gs2310SystemTimeNTPIndex_Type(Integer32):
    """Custom type gs2310SystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2310SystemTimeNTPIndex_Type.__name__ = "Integer32"
_Gs2310SystemTimeNTPIndex_Object = MibTableColumn
gs2310SystemTimeNTPIndex = _Gs2310SystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 1, 1, 1),
    _Gs2310SystemTimeNTPIndex_Type()
)
gs2310SystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPIndex.setStatus("current")


class _Gs2310SystemTimeNTPServerIPType_Type(Integer32):
    """Custom type gs2310SystemTimeNTPServerIPType based on Integer32"""
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


_Gs2310SystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Gs2310SystemTimeNTPServerIPType_Object = MibTableColumn
gs2310SystemTimeNTPServerIPType = _Gs2310SystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 1, 1, 2),
    _Gs2310SystemTimeNTPServerIPType_Type()
)
gs2310SystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPServerIPType.setStatus("current")
_Gs2310SystemTimeNTPServer_Type = DisplayString
_Gs2310SystemTimeNTPServer_Object = MibTableColumn
gs2310SystemTimeNTPServer = _Gs2310SystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 1, 1, 3),
    _Gs2310SystemTimeNTPServer_Type()
)
gs2310SystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPServer.setStatus("current")


class _Gs2310SystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type gs2310SystemTimeNTPCurrentMode based on Integer32"""
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


_Gs2310SystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Gs2310SystemTimeNTPCurrentMode_Object = MibTableColumn
gs2310SystemTimeNTPCurrentMode = _Gs2310SystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 1, 1, 4),
    _Gs2310SystemTimeNTPCurrentMode_Type()
)
gs2310SystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPCurrentMode.setStatus("current")


class _Gs2310SystemTimeNTPRequestInterval_Type(Integer32):
    """Custom type gs2310SystemTimeNTPRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 999999999),
    )


_Gs2310SystemTimeNTPRequestInterval_Type.__name__ = "Integer32"
_Gs2310SystemTimeNTPRequestInterval_Object = MibScalar
gs2310SystemTimeNTPRequestInterval = _Gs2310SystemTimeNTPRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 2),
    _Gs2310SystemTimeNTPRequestInterval_Type()
)
gs2310SystemTimeNTPRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPRequestInterval.setStatus("current")


class _Gs2310SystemTimeNTPTriesNumber_Type(Integer32):
    """Custom type gs2310SystemTimeNTPTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_Gs2310SystemTimeNTPTriesNumber_Type.__name__ = "Integer32"
_Gs2310SystemTimeNTPTriesNumber_Object = MibScalar
gs2310SystemTimeNTPTriesNumber = _Gs2310SystemTimeNTPTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 2, 2, 3),
    _Gs2310SystemTimeNTPTriesNumber_Type()
)
gs2310SystemTimeNTPTriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemTimeNTPTriesNumber.setStatus("current")
_Gs2310SystemAccount_ObjectIdentity = ObjectIdentity
gs2310SystemAccount = _Gs2310SystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3)
)
_Gs2310SystemAccountUsers_ObjectIdentity = ObjectIdentity
gs2310SystemAccountUsers = _Gs2310SystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1)
)


class _Gs2310SystemAccountUserCreate_Type(Integer32):
    """Custom type gs2310SystemAccountUserCreate based on Integer32"""
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


_Gs2310SystemAccountUserCreate_Type.__name__ = "Integer32"
_Gs2310SystemAccountUserCreate_Object = MibScalar
gs2310SystemAccountUserCreate = _Gs2310SystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 1),
    _Gs2310SystemAccountUserCreate_Type()
)
gs2310SystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemAccountUserCreate.setStatus("current")
_Gs2310SystemAccountUsersTable_Object = MibTable
gs2310SystemAccountUsersTable = _Gs2310SystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310SystemAccountUsersTable.setStatus("current")
_Gs2310SystemAccountUsersEntry_Object = MibTableRow
gs2310SystemAccountUsersEntry = _Gs2310SystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2, 1)
)
gs2310SystemAccountUsersEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310UserIndex"),
)
if mibBuilder.loadTexts:
    gs2310SystemAccountUsersEntry.setStatus("current")


class _Gs2310UserIndex_Type(Integer32):
    """Custom type gs2310UserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Gs2310UserIndex_Type.__name__ = "Integer32"
_Gs2310UserIndex_Object = MibTableColumn
gs2310UserIndex = _Gs2310UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2, 1, 1),
    _Gs2310UserIndex_Type()
)
gs2310UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310UserIndex.setStatus("current")


class _Gs2310UserName_Type(DisplayString):
    """Custom type gs2310UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310UserName_Type.__name__ = "DisplayString"
_Gs2310UserName_Object = MibTableColumn
gs2310UserName = _Gs2310UserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2, 1, 2),
    _Gs2310UserName_Type()
)
gs2310UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310UserName.setStatus("current")


class _Gs2310Password_Type(DisplayString):
    """Custom type gs2310Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310Password_Type.__name__ = "DisplayString"
_Gs2310Password_Object = MibTableColumn
gs2310Password = _Gs2310Password_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2, 1, 3),
    _Gs2310Password_Type()
)
gs2310Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Password.setStatus("current")


class _Gs2310UserPrivilegeLevel_Type(Integer32):
    """Custom type gs2310UserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310UserPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310UserPrivilegeLevel_Object = MibTableColumn
gs2310UserPrivilegeLevel = _Gs2310UserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2, 1, 4),
    _Gs2310UserPrivilegeLevel_Type()
)
gs2310UserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310UserPrivilegeLevel.setStatus("current")


class _Gs2310AccountUserRowStatus_Type(Integer32):
    """Custom type gs2310AccountUserRowStatus based on Integer32"""
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


_Gs2310AccountUserRowStatus_Type.__name__ = "Integer32"
_Gs2310AccountUserRowStatus_Object = MibTableColumn
gs2310AccountUserRowStatus = _Gs2310AccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 2, 1, 5),
    _Gs2310AccountUserRowStatus_Type()
)
gs2310AccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccountUserRowStatus.setStatus("current")


class _Gs2310SystemAccountUsersSuperUserPassword_Type(OctetString):
    """Custom type gs2310SystemAccountUsersSuperUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2310SystemAccountUsersSuperUserPassword_Type.__name__ = "OctetString"
_Gs2310SystemAccountUsersSuperUserPassword_Object = MibScalar
gs2310SystemAccountUsersSuperUserPassword = _Gs2310SystemAccountUsersSuperUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 1500),
    _Gs2310SystemAccountUsersSuperUserPassword_Type()
)
gs2310SystemAccountUsersSuperUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemAccountUsersSuperUserPassword.setStatus("current")


class _Gs2310SystemAccountEnforcePasswordRules_Type(Integer32):
    """Custom type gs2310SystemAccountEnforcePasswordRules based on Integer32"""
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


_Gs2310SystemAccountEnforcePasswordRules_Type.__name__ = "Integer32"
_Gs2310SystemAccountEnforcePasswordRules_Object = MibScalar
gs2310SystemAccountEnforcePasswordRules = _Gs2310SystemAccountEnforcePasswordRules_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 1, 1501),
    _Gs2310SystemAccountEnforcePasswordRules_Type()
)
gs2310SystemAccountEnforcePasswordRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemAccountEnforcePasswordRules.setStatus("current")
_Gs2310SystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
gs2310SystemAccountPrivilegeLevel = _Gs2310SystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2)
)


class _Gs2310AccountPrivilegeLevel_Type(Integer32):
    """Custom type gs2310AccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310AccountPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310AccountPrivilegeLevel_Object = MibScalar
gs2310AccountPrivilegeLevel = _Gs2310AccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 1),
    _Gs2310AccountPrivilegeLevel_Type()
)
gs2310AccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccountPrivilegeLevel.setStatus("current")


class _Gs2310AggregationPrivilegeLevel_Type(Integer32):
    """Custom type gs2310AggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310AggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310AggregationPrivilegeLevel_Object = MibScalar
gs2310AggregationPrivilegeLevel = _Gs2310AggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 2),
    _Gs2310AggregationPrivilegeLevel_Type()
)
gs2310AggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AggregationPrivilegeLevel.setStatus("current")


class _Gs2310DiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type gs2310DiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310DiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310DiagnosticsPrivilegeLevel_Object = MibScalar
gs2310DiagnosticsPrivilegeLevel = _Gs2310DiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 3),
    _Gs2310DiagnosticsPrivilegeLevel_Type()
)
gs2310DiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DiagnosticsPrivilegeLevel.setStatus("current")


class _Gs2310EEEPrivilegeLevel_Type(Integer32):
    """Custom type gs2310EEEPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310EEEPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310EEEPrivilegeLevel_Object = MibScalar
gs2310EEEPrivilegeLevel = _Gs2310EEEPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 4),
    _Gs2310EEEPrivilegeLevel_Type()
)
gs2310EEEPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310EEEPrivilegeLevel.setStatus("current")


class _Gs2310EasyportPrivilegeLevel_Type(Integer32):
    """Custom type gs2310EasyportPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310EasyportPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310EasyportPrivilegeLevel_Object = MibScalar
gs2310EasyportPrivilegeLevel = _Gs2310EasyportPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 9),
    _Gs2310EasyportPrivilegeLevel_Type()
)
gs2310EasyportPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310EasyportPrivilegeLevel.setStatus("current")


class _Gs2310GARPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310GARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310GARPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310GARPPrivilegeLevel_Object = MibScalar
gs2310GARPPrivilegeLevel = _Gs2310GARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 10),
    _Gs2310GARPPrivilegeLevel_Type()
)
gs2310GARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPPrivilegeLevel.setStatus("current")


class _Gs2310GVRPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310GVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310GVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310GVRPPrivilegeLevel_Object = MibScalar
gs2310GVRPPrivilegeLevel = _Gs2310GVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 11),
    _Gs2310GVRPPrivilegeLevel_Type()
)
gs2310GVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GVRPPrivilegeLevel.setStatus("current")


class _Gs2310IPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310IPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310IPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310IPPrivilegeLevel_Object = MibScalar
gs2310IPPrivilegeLevel = _Gs2310IPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 12),
    _Gs2310IPPrivilegeLevel_Type()
)
gs2310IPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPPrivilegeLevel.setStatus("current")


class _Gs2310IPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type gs2310IPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310IPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310IPMCSnoopingPrivilegeLevel_Object = MibScalar
gs2310IPMCSnoopingPrivilegeLevel = _Gs2310IPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 13),
    _Gs2310IPMCSnoopingPrivilegeLevel_Type()
)
gs2310IPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPMCSnoopingPrivilegeLevel.setStatus("current")


class _Gs2310LACPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310LACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310LACPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310LACPPrivilegeLevel_Object = MibScalar
gs2310LACPPrivilegeLevel = _Gs2310LACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 14),
    _Gs2310LACPPrivilegeLevel_Type()
)
gs2310LACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LACPPrivilegeLevel.setStatus("current")


class _Gs2310LLDPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310LLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310LLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310LLDPPrivilegeLevel_Object = MibScalar
gs2310LLDPPrivilegeLevel = _Gs2310LLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 15),
    _Gs2310LLDPPrivilegeLevel_Type()
)
gs2310LLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LLDPPrivilegeLevel.setStatus("current")


class _Gs2310LLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type gs2310LLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310LLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310LLDPMEDPrivilegeLevel_Object = MibScalar
gs2310LLDPMEDPrivilegeLevel = _Gs2310LLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 16),
    _Gs2310LLDPMEDPrivilegeLevel_Type()
)
gs2310LLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LLDPMEDPrivilegeLevel.setStatus("current")


class _Gs2310LoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type gs2310LoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310LoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310LoopProtectPrivilegeLevel_Object = MibScalar
gs2310LoopProtectPrivilegeLevel = _Gs2310LoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 17),
    _Gs2310LoopProtectPrivilegeLevel_Type()
)
gs2310LoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectPrivilegeLevel.setStatus("current")


class _Gs2310MACTablePrivilegeLevel_Type(Integer32):
    """Custom type gs2310MACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310MACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310MACTablePrivilegeLevel_Object = MibScalar
gs2310MACTablePrivilegeLevel = _Gs2310MACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 18),
    _Gs2310MACTablePrivilegeLevel_Type()
)
gs2310MACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACTablePrivilegeLevel.setStatus("current")


class _Gs2310MVRPrivilegeLevel_Type(Integer32):
    """Custom type gs2310MVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310MVRPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310MVRPrivilegeLevel_Object = MibScalar
gs2310MVRPrivilegeLevel = _Gs2310MVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 22),
    _Gs2310MVRPrivilegeLevel_Type()
)
gs2310MVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPrivilegeLevel.setStatus("current")


class _Gs2310MaintenancePrivilegeLevel_Type(Integer32):
    """Custom type gs2310MaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310MaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310MaintenancePrivilegeLevel_Object = MibScalar
gs2310MaintenancePrivilegeLevel = _Gs2310MaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 24),
    _Gs2310MaintenancePrivilegeLevel_Type()
)
gs2310MaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MaintenancePrivilegeLevel.setStatus("current")


class _Gs2310MirroringPrivilegeLevel_Type(Integer32):
    """Custom type gs2310MirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310MirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310MirroringPrivilegeLevel_Object = MibScalar
gs2310MirroringPrivilegeLevel = _Gs2310MirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 25),
    _Gs2310MirroringPrivilegeLevel_Type()
)
gs2310MirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MirroringPrivilegeLevel.setStatus("current")


class _Gs2310PortsPrivilegeLevel_Type(Integer32):
    """Custom type gs2310PortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310PortsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310PortsPrivilegeLevel_Object = MibScalar
gs2310PortsPrivilegeLevel = _Gs2310PortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 27),
    _Gs2310PortsPrivilegeLevel_Type()
)
gs2310PortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortsPrivilegeLevel.setStatus("current")


class _Gs2310PrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2310PrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310PrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310PrivateVLANsPrivilegeLevel_Object = MibScalar
gs2310PrivateVLANsPrivilegeLevel = _Gs2310PrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 28),
    _Gs2310PrivateVLANsPrivilegeLevel_Type()
)
gs2310PrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PrivateVLANsPrivilegeLevel.setStatus("current")


class _Gs2310QoSPrivilegeLevel_Type(Integer32):
    """Custom type gs2310QoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310QoSPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310QoSPrivilegeLevel_Object = MibScalar
gs2310QoSPrivilegeLevel = _Gs2310QoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 29),
    _Gs2310QoSPrivilegeLevel_Type()
)
gs2310QoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSPrivilegeLevel.setStatus("current")


class _Gs2310SFlowPrivilegeLevel_Type(Integer32):
    """Custom type gs2310SFlowPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SFlowPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SFlowPrivilegeLevel_Object = MibScalar
gs2310SFlowPrivilegeLevel = _Gs2310SFlowPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 30),
    _Gs2310SFlowPrivilegeLevel_Type()
)
gs2310SFlowPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SFlowPrivilegeLevel.setStatus("current")


class _Gs2310SMTPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310SMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SMTPPrivilegeLevel_Object = MibScalar
gs2310SMTPPrivilegeLevel = _Gs2310SMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 31),
    _Gs2310SMTPPrivilegeLevel_Type()
)
gs2310SMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPPrivilegeLevel.setStatus("current")


class _Gs2310SNMPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310SNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SNMPPrivilegeLevel_Object = MibScalar
gs2310SNMPPrivilegeLevel = _Gs2310SNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 32),
    _Gs2310SNMPPrivilegeLevel_Type()
)
gs2310SNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SNMPPrivilegeLevel.setStatus("current")


class _Gs2310SecurityPrivilegeLevel_Type(Integer32):
    """Custom type gs2310SecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SecurityPrivilegeLevel_Object = MibScalar
gs2310SecurityPrivilegeLevel = _Gs2310SecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 33),
    _Gs2310SecurityPrivilegeLevel_Type()
)
gs2310SecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SecurityPrivilegeLevel.setStatus("current")


class _Gs2310SingleIPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310SingleIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SingleIPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SingleIPPrivilegeLevel_Object = MibScalar
gs2310SingleIPPrivilegeLevel = _Gs2310SingleIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 34),
    _Gs2310SingleIPPrivilegeLevel_Type()
)
gs2310SingleIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SingleIPPrivilegeLevel.setStatus("current")


class _Gs2310SpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type gs2310SpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SpanningTreePrivilegeLevel_Object = MibScalar
gs2310SpanningTreePrivilegeLevel = _Gs2310SpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 35),
    _Gs2310SpanningTreePrivilegeLevel_Type()
)
gs2310SpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SpanningTreePrivilegeLevel.setStatus("current")


class _Gs2310SystemPrivilegeLevel_Type(Integer32):
    """Custom type gs2310SystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310SystemPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310SystemPrivilegeLevel_Object = MibScalar
gs2310SystemPrivilegeLevel = _Gs2310SystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 36),
    _Gs2310SystemPrivilegeLevel_Type()
)
gs2310SystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SystemPrivilegeLevel.setStatus("current")


class _Gs2310TrapEventPrivilegeLevel_Type(Integer32):
    """Custom type gs2310TrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310TrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310TrapEventPrivilegeLevel_Object = MibScalar
gs2310TrapEventPrivilegeLevel = _Gs2310TrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 37),
    _Gs2310TrapEventPrivilegeLevel_Type()
)
gs2310TrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventPrivilegeLevel.setStatus("current")


class _Gs2310UPnPPrivilegeLevel_Type(Integer32):
    """Custom type gs2310UPnPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310UPnPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310UPnPPrivilegeLevel_Object = MibScalar
gs2310UPnPPrivilegeLevel = _Gs2310UPnPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 38),
    _Gs2310UPnPPrivilegeLevel_Type()
)
gs2310UPnPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310UPnPPrivilegeLevel.setStatus("current")


class _Gs2310VCLPrivilegeLevel_Type(Integer32):
    """Custom type gs2310VCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310VCLPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310VCLPrivilegeLevel_Object = MibScalar
gs2310VCLPrivilegeLevel = _Gs2310VCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 39),
    _Gs2310VCLPrivilegeLevel_Type()
)
gs2310VCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VCLPrivilegeLevel.setStatus("current")


class _Gs2310VLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2310VLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310VLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310VLANsPrivilegeLevel_Object = MibScalar
gs2310VLANsPrivilegeLevel = _Gs2310VLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 41),
    _Gs2310VLANsPrivilegeLevel_Type()
)
gs2310VLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VLANsPrivilegeLevel.setStatus("current")


class _Gs2310VoiceVLANPrivilegeLevel_Type(Integer32):
    """Custom type gs2310VoiceVLANPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2310VoiceVLANPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2310VoiceVLANPrivilegeLevel_Object = MibScalar
gs2310VoiceVLANPrivilegeLevel = _Gs2310VoiceVLANPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 3, 2, 42),
    _Gs2310VoiceVLANPrivilegeLevel_Type()
)
gs2310VoiceVLANPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANPrivilegeLevel.setStatus("current")
_Gs2310IP_ObjectIdentity = ObjectIdentity
gs2310IP = _Gs2310IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4)
)
_Gs2310IPv4_ObjectIdentity = ObjectIdentity
gs2310IPv4 = _Gs2310IPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1)
)
_Gs2310IPv4Configured_ObjectIdentity = ObjectIdentity
gs2310IPv4Configured = _Gs2310IPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1)
)


class _Gs2310Ipv4DHCPClient_Type(Integer32):
    """Custom type gs2310Ipv4DHCPClient based on Integer32"""
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


_Gs2310Ipv4DHCPClient_Type.__name__ = "Integer32"
_Gs2310Ipv4DHCPClient_Object = MibScalar
gs2310Ipv4DHCPClient = _Gs2310Ipv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 1),
    _Gs2310Ipv4DHCPClient_Type()
)
gs2310Ipv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ipv4DHCPClient.setStatus("current")
_Gs2310IPv4Address_Type = IpAddress
_Gs2310IPv4Address_Object = MibScalar
gs2310IPv4Address = _Gs2310IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 2),
    _Gs2310IPv4Address_Type()
)
gs2310IPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPv4Address.setStatus("current")
_Gs2310IPv4Mask_Type = IpAddress
_Gs2310IPv4Mask_Object = MibScalar
gs2310IPv4Mask = _Gs2310IPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 3),
    _Gs2310IPv4Mask_Type()
)
gs2310IPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPv4Mask.setStatus("current")
_Gs2310IPv4Gateway_Type = IpAddress
_Gs2310IPv4Gateway_Object = MibScalar
gs2310IPv4Gateway = _Gs2310IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 4),
    _Gs2310IPv4Gateway_Type()
)
gs2310IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPv4Gateway.setStatus("current")


class _Gs2310IPv4VLANId_Type(Integer32):
    """Custom type gs2310IPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310IPv4VLANId_Type.__name__ = "Integer32"
_Gs2310IPv4VLANId_Object = MibScalar
gs2310IPv4VLANId = _Gs2310IPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 5),
    _Gs2310IPv4VLANId_Type()
)
gs2310IPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPv4VLANId.setStatus("current")
_Gs2310IPv4DNSServer_Type = IpAddress
_Gs2310IPv4DNSServer_Object = MibScalar
gs2310IPv4DNSServer = _Gs2310IPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 6),
    _Gs2310IPv4DNSServer_Type()
)
gs2310IPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPv4DNSServer.setStatus("current")


class _Gs2310IPv4DNSProxy_Type(Integer32):
    """Custom type gs2310IPv4DNSProxy based on Integer32"""
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


_Gs2310IPv4DNSProxy_Type.__name__ = "Integer32"
_Gs2310IPv4DNSProxy_Object = MibScalar
gs2310IPv4DNSProxy = _Gs2310IPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 1, 7),
    _Gs2310IPv4DNSProxy_Type()
)
gs2310IPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPv4DNSProxy.setStatus("current")
_Gs2310IPv4Current_ObjectIdentity = ObjectIdentity
gs2310IPv4Current = _Gs2310IPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2)
)


class _Gs2310Ipv4CurrentDHCPClient_Type(Integer32):
    """Custom type gs2310Ipv4CurrentDHCPClient based on Integer32"""
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


_Gs2310Ipv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Gs2310Ipv4CurrentDHCPClient_Object = MibScalar
gs2310Ipv4CurrentDHCPClient = _Gs2310Ipv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2, 1),
    _Gs2310Ipv4CurrentDHCPClient_Type()
)
gs2310Ipv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ipv4CurrentDHCPClient.setStatus("current")
_Gs2310IPv4CurrentAddress_Type = IpAddress
_Gs2310IPv4CurrentAddress_Object = MibScalar
gs2310IPv4CurrentAddress = _Gs2310IPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2, 2),
    _Gs2310IPv4CurrentAddress_Type()
)
gs2310IPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv4CurrentAddress.setStatus("current")
_Gs2310IPv4CurrentMask_Type = IpAddress
_Gs2310IPv4CurrentMask_Object = MibScalar
gs2310IPv4CurrentMask = _Gs2310IPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2, 3),
    _Gs2310IPv4CurrentMask_Type()
)
gs2310IPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv4CurrentMask.setStatus("current")
_Gs2310IPv4CurrentGateway_Type = IpAddress
_Gs2310IPv4CurrentGateway_Object = MibScalar
gs2310IPv4CurrentGateway = _Gs2310IPv4CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2, 4),
    _Gs2310IPv4CurrentGateway_Type()
)
gs2310IPv4CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv4CurrentGateway.setStatus("current")


class _Gs2310IPv4CurrentVLANId_Type(Integer32):
    """Custom type gs2310IPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310IPv4CurrentVLANId_Type.__name__ = "Integer32"
_Gs2310IPv4CurrentVLANId_Object = MibScalar
gs2310IPv4CurrentVLANId = _Gs2310IPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2, 5),
    _Gs2310IPv4CurrentVLANId_Type()
)
gs2310IPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv4CurrentVLANId.setStatus("current")
_Gs2310IPv4CurrentDNSServer_Type = IpAddress
_Gs2310IPv4CurrentDNSServer_Object = MibScalar
gs2310IPv4CurrentDNSServer = _Gs2310IPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 1, 2, 6),
    _Gs2310IPv4CurrentDNSServer_Type()
)
gs2310IPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPv4CurrentDNSServer.setStatus("current")
_Gs2310IPv6_ObjectIdentity = ObjectIdentity
gs2310IPv6 = _Gs2310IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2)
)
_Gs2310IPv6Configured_ObjectIdentity = ObjectIdentity
gs2310IPv6Configured = _Gs2310IPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 1)
)


class _Gs2310Ipv6AutoConfiguration_Type(Integer32):
    """Custom type gs2310Ipv6AutoConfiguration based on Integer32"""
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


_Gs2310Ipv6AutoConfiguration_Type.__name__ = "Integer32"
_Gs2310Ipv6AutoConfiguration_Object = MibScalar
gs2310Ipv6AutoConfiguration = _Gs2310Ipv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 1, 1),
    _Gs2310Ipv6AutoConfiguration_Type()
)
gs2310Ipv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ipv6AutoConfiguration.setStatus("current")


class _Gs2310Ipv6Address_Type(DisplayString):
    """Custom type gs2310Ipv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2310Ipv6Address_Type.__name__ = "DisplayString"
_Gs2310Ipv6Address_Object = MibScalar
gs2310Ipv6Address = _Gs2310Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 1, 2),
    _Gs2310Ipv6Address_Type()
)
gs2310Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ipv6Address.setStatus("current")


class _Gs2310Ipv6Prefix_Type(Integer32):
    """Custom type gs2310Ipv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2310Ipv6Prefix_Type.__name__ = "Integer32"
_Gs2310Ipv6Prefix_Object = MibScalar
gs2310Ipv6Prefix = _Gs2310Ipv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 1, 3),
    _Gs2310Ipv6Prefix_Type()
)
gs2310Ipv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ipv6Prefix.setStatus("current")


class _Gs2310Ipv6Gateway_Type(DisplayString):
    """Custom type gs2310Ipv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2310Ipv6Gateway_Type.__name__ = "DisplayString"
_Gs2310Ipv6Gateway_Object = MibScalar
gs2310Ipv6Gateway = _Gs2310Ipv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 1, 4),
    _Gs2310Ipv6Gateway_Type()
)
gs2310Ipv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ipv6Gateway.setStatus("current")
_Gs2310IPv6Current_ObjectIdentity = ObjectIdentity
gs2310IPv6Current = _Gs2310IPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 2)
)


class _Gs2310Ipv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type gs2310Ipv6CurrentAutoConfiguration based on Integer32"""
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


_Gs2310Ipv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Gs2310Ipv6CurrentAutoConfiguration_Object = MibScalar
gs2310Ipv6CurrentAutoConfiguration = _Gs2310Ipv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 2, 1),
    _Gs2310Ipv6CurrentAutoConfiguration_Type()
)
gs2310Ipv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Ipv6CurrentAutoConfiguration.setStatus("current")


class _Gs2310Ipv6CurrentAddress_Type(DisplayString):
    """Custom type gs2310Ipv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2310Ipv6CurrentAddress_Type.__name__ = "DisplayString"
_Gs2310Ipv6CurrentAddress_Object = MibScalar
gs2310Ipv6CurrentAddress = _Gs2310Ipv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 2, 2),
    _Gs2310Ipv6CurrentAddress_Type()
)
gs2310Ipv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Ipv6CurrentAddress.setStatus("current")


class _Gs2310Ipv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type gs2310Ipv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2310Ipv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Gs2310Ipv6CurrentLinkLocalAddress_Object = MibScalar
gs2310Ipv6CurrentLinkLocalAddress = _Gs2310Ipv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 2, 3),
    _Gs2310Ipv6CurrentLinkLocalAddress_Type()
)
gs2310Ipv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Ipv6CurrentLinkLocalAddress.setStatus("current")


class _Gs2310Ipv6CurrentPrefix_Type(DisplayString):
    """Custom type gs2310Ipv6CurrentPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Gs2310Ipv6CurrentPrefix_Type.__name__ = "DisplayString"
_Gs2310Ipv6CurrentPrefix_Object = MibScalar
gs2310Ipv6CurrentPrefix = _Gs2310Ipv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 2, 4),
    _Gs2310Ipv6CurrentPrefix_Type()
)
gs2310Ipv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Ipv6CurrentPrefix.setStatus("current")


class _Gs2310Ipv6CurrentGateway_Type(DisplayString):
    """Custom type gs2310Ipv6CurrentGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2310Ipv6CurrentGateway_Type.__name__ = "DisplayString"
_Gs2310Ipv6CurrentGateway_Object = MibScalar
gs2310Ipv6CurrentGateway = _Gs2310Ipv6CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 4, 2, 2, 5),
    _Gs2310Ipv6CurrentGateway_Type()
)
gs2310Ipv6CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Ipv6CurrentGateway.setStatus("current")
_Gs2310Syslog_ObjectIdentity = ObjectIdentity
gs2310Syslog = _Gs2310Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5)
)
_Gs2310SyslogConf_ObjectIdentity = ObjectIdentity
gs2310SyslogConf = _Gs2310SyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 1)
)


class _Gs2310ServerMode_Type(Integer32):
    """Custom type gs2310ServerMode based on Integer32"""
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


_Gs2310ServerMode_Type.__name__ = "Integer32"
_Gs2310ServerMode_Object = MibScalar
gs2310ServerMode = _Gs2310ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 1, 1),
    _Gs2310ServerMode_Type()
)
gs2310ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ServerMode.setStatus("current")
_Gs2310ServerAddress1_Type = IpAddress
_Gs2310ServerAddress1_Object = MibScalar
gs2310ServerAddress1 = _Gs2310ServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 1, 2),
    _Gs2310ServerAddress1_Type()
)
gs2310ServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ServerAddress1.setStatus("current")
_Gs2310ServerAddress2_Type = IpAddress
_Gs2310ServerAddress2_Object = MibScalar
gs2310ServerAddress2 = _Gs2310ServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 1, 3),
    _Gs2310ServerAddress2_Type()
)
gs2310ServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ServerAddress2.setStatus("current")


class _Gs2310SyslogLevel_Type(Integer32):
    """Custom type gs2310SyslogLevel based on Integer32"""
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


_Gs2310SyslogLevel_Type.__name__ = "Integer32"
_Gs2310SyslogLevel_Object = MibScalar
gs2310SyslogLevel = _Gs2310SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 1, 4),
    _Gs2310SyslogLevel_Type()
)
gs2310SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SyslogLevel.setStatus("current")
_Gs2310SyslogDetailedInfo_ObjectIdentity = ObjectIdentity
gs2310SyslogDetailedInfo = _Gs2310SyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2)
)


class _Gs2310SyslogDetailedInfoClear_Type(Integer32):
    """Custom type gs2310SyslogDetailedInfoClear based on Integer32"""
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


_Gs2310SyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Gs2310SyslogDetailedInfoClear_Object = MibScalar
gs2310SyslogDetailedInfoClear = _Gs2310SyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 1),
    _Gs2310SyslogDetailedInfoClear_Type()
)
gs2310SyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoClear.setStatus("current")
_Gs2310SyslogDetailedInfoTable_Object = MibTable
gs2310SyslogDetailedInfoTable = _Gs2310SyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoTable.setStatus("current")
_Gs2310SyslogDetailedInfoEntry_Object = MibTableRow
gs2310SyslogDetailedInfoEntry = _Gs2310SyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 2, 1)
)
gs2310SyslogDetailedInfoEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoEntry.setStatus("current")


class _Gs2310SyslogDetailedInfoIndex_Type(Integer32):
    """Custom type gs2310SyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2310SyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Gs2310SyslogDetailedInfoIndex_Object = MibTableColumn
gs2310SyslogDetailedInfoIndex = _Gs2310SyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 2, 1, 1),
    _Gs2310SyslogDetailedInfoIndex_Type()
)
gs2310SyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoIndex.setStatus("current")
_Gs2310SyslogDetailedInfoLevel_Type = DisplayString
_Gs2310SyslogDetailedInfoLevel_Object = MibTableColumn
gs2310SyslogDetailedInfoLevel = _Gs2310SyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 2, 1, 2),
    _Gs2310SyslogDetailedInfoLevel_Type()
)
gs2310SyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoLevel.setStatus("current")


class _Gs2310SyslogDetailedInfoTime_Type(DisplayString):
    """Custom type gs2310SyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gs2310SyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Gs2310SyslogDetailedInfoTime_Object = MibTableColumn
gs2310SyslogDetailedInfoTime = _Gs2310SyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 2, 1, 3),
    _Gs2310SyslogDetailedInfoTime_Type()
)
gs2310SyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoTime.setStatus("current")
_Gs2310SyslogDetailedInfoMessage_Type = DisplayString
_Gs2310SyslogDetailedInfoMessage_Object = MibTableColumn
gs2310SyslogDetailedInfoMessage = _Gs2310SyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 5, 2, 2, 1, 4),
    _Gs2310SyslogDetailedInfoMessage_Type()
)
gs2310SyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SyslogDetailedInfoMessage.setStatus("current")
_Gs2310Snmp_ObjectIdentity = ObjectIdentity
gs2310Snmp = _Gs2310Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6)
)
_Gs2310SnmpConf_ObjectIdentity = ObjectIdentity
gs2310SnmpConf = _Gs2310SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1)
)


class _Gs2310GetCommunityMode_Type(Integer32):
    """Custom type gs2310GetCommunityMode based on Integer32"""
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


_Gs2310GetCommunityMode_Type.__name__ = "Integer32"
_Gs2310GetCommunityMode_Object = MibScalar
gs2310GetCommunityMode = _Gs2310GetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 1),
    _Gs2310GetCommunityMode_Type()
)
gs2310GetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GetCommunityMode.setStatus("current")
_Gs2310GetCommunity_Type = DisplayString
_Gs2310GetCommunity_Object = MibScalar
gs2310GetCommunity = _Gs2310GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 2),
    _Gs2310GetCommunity_Type()
)
gs2310GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GetCommunity.setStatus("current")


class _Gs2310SetCommunityMode_Type(Integer32):
    """Custom type gs2310SetCommunityMode based on Integer32"""
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


_Gs2310SetCommunityMode_Type.__name__ = "Integer32"
_Gs2310SetCommunityMode_Object = MibScalar
gs2310SetCommunityMode = _Gs2310SetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 3),
    _Gs2310SetCommunityMode_Type()
)
gs2310SetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SetCommunityMode.setStatus("current")
_Gs2310SetCommunity_Type = DisplayString
_Gs2310SetCommunity_Object = MibScalar
gs2310SetCommunity = _Gs2310SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 4),
    _Gs2310SetCommunity_Type()
)
gs2310SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SetCommunity.setStatus("current")
_Gs2310GetCommunityConfTable_Object = MibTable
gs2310GetCommunityConfTable = _Gs2310GetCommunityConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    gs2310GetCommunityConfTable.setStatus("current")
_Gs2310GetCommunityConfEntry_Object = MibTableRow
gs2310GetCommunityConfEntry = _Gs2310GetCommunityConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 5, 1)
)
gs2310GetCommunityConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310CommunityConfIndex"),
)
if mibBuilder.loadTexts:
    gs2310GetCommunityConfEntry.setStatus("current")


class _Gs2310CommunityConfIndex_Type(Integer32):
    """Custom type gs2310CommunityConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310CommunityConfIndex_Type.__name__ = "Integer32"
_Gs2310CommunityConfIndex_Object = MibTableColumn
gs2310CommunityConfIndex = _Gs2310CommunityConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 5, 1, 1),
    _Gs2310CommunityConfIndex_Type()
)
gs2310CommunityConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310CommunityConfIndex.setStatus("current")
_Gs2310CommunityConfGetCommunity_Type = DisplayString
_Gs2310CommunityConfGetCommunity_Object = MibTableColumn
gs2310CommunityConfGetCommunity = _Gs2310CommunityConfGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 5, 1, 2),
    _Gs2310CommunityConfGetCommunity_Type()
)
gs2310CommunityConfGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310CommunityConfGetCommunity.setStatus("current")
_Gs2310TrapHostConfTable_Object = MibTable
gs2310TrapHostConfTable = _Gs2310TrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    gs2310TrapHostConfTable.setStatus("current")
_Gs2310TrapHostConfEntry_Object = MibTableRow
gs2310TrapHostConfEntry = _Gs2310TrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1)
)
gs2310TrapHostConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310TrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    gs2310TrapHostConfEntry.setStatus("current")


class _Gs2310TrapHostConfIndex_Type(Integer32):
    """Custom type gs2310TrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2310TrapHostConfIndex_Type.__name__ = "Integer32"
_Gs2310TrapHostConfIndex_Object = MibTableColumn
gs2310TrapHostConfIndex = _Gs2310TrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 1),
    _Gs2310TrapHostConfIndex_Type()
)
gs2310TrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310TrapHostConfIndex.setStatus("current")


class _Gs2310TrapHostConfVersion_Type(Integer32):
    """Custom type gs2310TrapHostConfVersion based on Integer32"""
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


_Gs2310TrapHostConfVersion_Type.__name__ = "Integer32"
_Gs2310TrapHostConfVersion_Object = MibTableColumn
gs2310TrapHostConfVersion = _Gs2310TrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 2),
    _Gs2310TrapHostConfVersion_Type()
)
gs2310TrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfVersion.setStatus("current")


class _Gs2310TrapHostConfIPType_Type(Integer32):
    """Custom type gs2310TrapHostConfIPType based on Integer32"""
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


_Gs2310TrapHostConfIPType_Type.__name__ = "Integer32"
_Gs2310TrapHostConfIPType_Object = MibTableColumn
gs2310TrapHostConfIPType = _Gs2310TrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 3),
    _Gs2310TrapHostConfIPType_Type()
)
gs2310TrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfIPType.setStatus("current")
_Gs2310TrapHostConfIP_Type = DisplayString
_Gs2310TrapHostConfIP_Object = MibTableColumn
gs2310TrapHostConfIP = _Gs2310TrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 4),
    _Gs2310TrapHostConfIP_Type()
)
gs2310TrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfIP.setStatus("current")


class _Gs2310TrapHostConfPort_Type(Integer32):
    """Custom type gs2310TrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310TrapHostConfPort_Type.__name__ = "Integer32"
_Gs2310TrapHostConfPort_Object = MibTableColumn
gs2310TrapHostConfPort = _Gs2310TrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 5),
    _Gs2310TrapHostConfPort_Type()
)
gs2310TrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfPort.setStatus("current")


class _Gs2310TrapHostConfCommunity_Type(DisplayString):
    """Custom type gs2310TrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310TrapHostConfCommunity_Type.__name__ = "DisplayString"
_Gs2310TrapHostConfCommunity_Object = MibTableColumn
gs2310TrapHostConfCommunity = _Gs2310TrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 6),
    _Gs2310TrapHostConfCommunity_Type()
)
gs2310TrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfCommunity.setStatus("current")


class _Gs2310TrapHostConfSeverityLevel_Type(Integer32):
    """Custom type gs2310TrapHostConfSeverityLevel based on Integer32"""
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


_Gs2310TrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Gs2310TrapHostConfSeverityLevel_Object = MibTableColumn
gs2310TrapHostConfSeverityLevel = _Gs2310TrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 7),
    _Gs2310TrapHostConfSeverityLevel_Type()
)
gs2310TrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfSeverityLevel.setStatus("current")


class _Gs2310TrapHostConfSecurityLevel_Type(Integer32):
    """Custom type gs2310TrapHostConfSecurityLevel based on Integer32"""
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


_Gs2310TrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Gs2310TrapHostConfSecurityLevel_Object = MibTableColumn
gs2310TrapHostConfSecurityLevel = _Gs2310TrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 8),
    _Gs2310TrapHostConfSecurityLevel_Type()
)
gs2310TrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfSecurityLevel.setStatus("current")


class _Gs2310TrapHostConfAuthPtc_Type(Integer32):
    """Custom type gs2310TrapHostConfAuthPtc based on Integer32"""
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


_Gs2310TrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Gs2310TrapHostConfAuthPtc_Object = MibTableColumn
gs2310TrapHostConfAuthPtc = _Gs2310TrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 9),
    _Gs2310TrapHostConfAuthPtc_Type()
)
gs2310TrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfAuthPtc.setStatus("current")
_Gs2310TrapHostConfAuthPassword_Type = DisplayString
_Gs2310TrapHostConfAuthPassword_Object = MibTableColumn
gs2310TrapHostConfAuthPassword = _Gs2310TrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 10),
    _Gs2310TrapHostConfAuthPassword_Type()
)
gs2310TrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfAuthPassword.setStatus("current")


class _Gs2310TrapHostConfPrivPtc_Type(Integer32):
    """Custom type gs2310TrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("des", 1)
    )


_Gs2310TrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Gs2310TrapHostConfPrivPtc_Object = MibTableColumn
gs2310TrapHostConfPrivPtc = _Gs2310TrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 11),
    _Gs2310TrapHostConfPrivPtc_Type()
)
gs2310TrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfPrivPtc.setStatus("current")
_Gs2310TrapHostConfPrivPassword_Type = DisplayString
_Gs2310TrapHostConfPrivPassword_Object = MibTableColumn
gs2310TrapHostConfPrivPassword = _Gs2310TrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 12),
    _Gs2310TrapHostConfPrivPassword_Type()
)
gs2310TrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfPrivPassword.setStatus("current")


class _Gs2310TrapHostConfCurrentMode_Type(Integer32):
    """Custom type gs2310TrapHostConfCurrentMode based on Integer32"""
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


_Gs2310TrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Gs2310TrapHostConfCurrentMode_Object = MibTableColumn
gs2310TrapHostConfCurrentMode = _Gs2310TrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 1, 6, 1, 13),
    _Gs2310TrapHostConfCurrentMode_Type()
)
gs2310TrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapHostConfCurrentMode.setStatus("current")
_Gs2310SnmpSystem_ObjectIdentity = ObjectIdentity
gs2310SnmpSystem = _Gs2310SnmpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 2)
)


class _Gs2310SnmpState_Type(Integer32):
    """Custom type gs2310SnmpState based on Integer32"""
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


_Gs2310SnmpState_Type.__name__ = "Integer32"
_Gs2310SnmpState_Object = MibScalar
gs2310SnmpState = _Gs2310SnmpState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 2, 1),
    _Gs2310SnmpState_Type()
)
gs2310SnmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpState.setStatus("current")


class _Gs2310SnmpEngineID_Type(OctetString):
    """Custom type gs2310SnmpEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Gs2310SnmpEngineID_Type.__name__ = "OctetString"
_Gs2310SnmpEngineID_Object = MibScalar
gs2310SnmpEngineID = _Gs2310SnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 2, 2),
    _Gs2310SnmpEngineID_Type()
)
gs2310SnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpEngineID.setStatus("current")
_Gs2310SnmpCommunities_ObjectIdentity = ObjectIdentity
gs2310SnmpCommunities = _Gs2310SnmpCommunities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3)
)


class _Gs2310SnmpCommunitiesCreate_Type(Integer32):
    """Custom type gs2310SnmpCommunitiesCreate based on Integer32"""
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


_Gs2310SnmpCommunitiesCreate_Type.__name__ = "Integer32"
_Gs2310SnmpCommunitiesCreate_Object = MibScalar
gs2310SnmpCommunitiesCreate = _Gs2310SnmpCommunitiesCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 1),
    _Gs2310SnmpCommunitiesCreate_Type()
)
gs2310SnmpCommunitiesCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesCreate.setStatus("current")
_Gs2310SnmpCommunitiesTable_Object = MibTable
gs2310SnmpCommunitiesTable = _Gs2310SnmpCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesTable.setStatus("current")
_Gs2310SnmpCommunitiesEntry_Object = MibTableRow
gs2310SnmpCommunitiesEntry = _Gs2310SnmpCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1)
)
gs2310SnmpCommunitiesEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SnmpCommunitiesIndex"),
)
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesEntry.setStatus("current")


class _Gs2310SnmpCommunitiesIndex_Type(Integer32):
    """Custom type gs2310SnmpCommunitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2310SnmpCommunitiesIndex_Type.__name__ = "Integer32"
_Gs2310SnmpCommunitiesIndex_Object = MibTableColumn
gs2310SnmpCommunitiesIndex = _Gs2310SnmpCommunitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1, 1),
    _Gs2310SnmpCommunitiesIndex_Type()
)
gs2310SnmpCommunitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesIndex.setStatus("current")


class _Gs2310SnmpCommunitiesCommunity_Type(DisplayString):
    """Custom type gs2310SnmpCommunitiesCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpCommunitiesCommunity_Type.__name__ = "DisplayString"
_Gs2310SnmpCommunitiesCommunity_Object = MibTableColumn
gs2310SnmpCommunitiesCommunity = _Gs2310SnmpCommunitiesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1, 2),
    _Gs2310SnmpCommunitiesCommunity_Type()
)
gs2310SnmpCommunitiesCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesCommunity.setStatus("current")


class _Gs2310SnmpCommunitiesUserName_Type(DisplayString):
    """Custom type gs2310SnmpCommunitiesUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpCommunitiesUserName_Type.__name__ = "DisplayString"
_Gs2310SnmpCommunitiesUserName_Object = MibTableColumn
gs2310SnmpCommunitiesUserName = _Gs2310SnmpCommunitiesUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1, 3),
    _Gs2310SnmpCommunitiesUserName_Type()
)
gs2310SnmpCommunitiesUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesUserName.setStatus("current")
_Gs2310SnmpCommunitiesSourceIP_Type = IpAddress
_Gs2310SnmpCommunitiesSourceIP_Object = MibTableColumn
gs2310SnmpCommunitiesSourceIP = _Gs2310SnmpCommunitiesSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1, 4),
    _Gs2310SnmpCommunitiesSourceIP_Type()
)
gs2310SnmpCommunitiesSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesSourceIP.setStatus("current")
_Gs2310SnmpCommunitiesSourceMask_Type = IpAddress
_Gs2310SnmpCommunitiesSourceMask_Object = MibTableColumn
gs2310SnmpCommunitiesSourceMask = _Gs2310SnmpCommunitiesSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1, 5),
    _Gs2310SnmpCommunitiesSourceMask_Type()
)
gs2310SnmpCommunitiesSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesSourceMask.setStatus("current")


class _Gs2310SnmpCommunitiesRowStatus_Type(Integer32):
    """Custom type gs2310SnmpCommunitiesRowStatus based on Integer32"""
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


_Gs2310SnmpCommunitiesRowStatus_Type.__name__ = "Integer32"
_Gs2310SnmpCommunitiesRowStatus_Object = MibTableColumn
gs2310SnmpCommunitiesRowStatus = _Gs2310SnmpCommunitiesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 3, 2, 1, 6),
    _Gs2310SnmpCommunitiesRowStatus_Type()
)
gs2310SnmpCommunitiesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpCommunitiesRowStatus.setStatus("current")
_Gs2310SnmpUsers_ObjectIdentity = ObjectIdentity
gs2310SnmpUsers = _Gs2310SnmpUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4)
)


class _Gs2310SnmpUsersCreate_Type(Integer32):
    """Custom type gs2310SnmpUsersCreate based on Integer32"""
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


_Gs2310SnmpUsersCreate_Type.__name__ = "Integer32"
_Gs2310SnmpUsersCreate_Object = MibScalar
gs2310SnmpUsersCreate = _Gs2310SnmpUsersCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 1),
    _Gs2310SnmpUsersCreate_Type()
)
gs2310SnmpUsersCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersCreate.setStatus("current")
_Gs2310SnmpUsersTable_Object = MibTable
gs2310SnmpUsersTable = _Gs2310SnmpUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310SnmpUsersTable.setStatus("current")
_Gs2310SnmpUsersEntry_Object = MibTableRow
gs2310SnmpUsersEntry = _Gs2310SnmpUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1)
)
gs2310SnmpUsersEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SnmpUsersIndex"),
)
if mibBuilder.loadTexts:
    gs2310SnmpUsersEntry.setStatus("current")


class _Gs2310SnmpUsersIndex_Type(Integer32):
    """Custom type gs2310SnmpUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2310SnmpUsersIndex_Type.__name__ = "Integer32"
_Gs2310SnmpUsersIndex_Object = MibTableColumn
gs2310SnmpUsersIndex = _Gs2310SnmpUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 1),
    _Gs2310SnmpUsersIndex_Type()
)
gs2310SnmpUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SnmpUsersIndex.setStatus("current")


class _Gs2310SnmpUsersUserName_Type(DisplayString):
    """Custom type gs2310SnmpUsersUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpUsersUserName_Type.__name__ = "DisplayString"
_Gs2310SnmpUsersUserName_Object = MibTableColumn
gs2310SnmpUsersUserName = _Gs2310SnmpUsersUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 2),
    _Gs2310SnmpUsersUserName_Type()
)
gs2310SnmpUsersUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersUserName.setStatus("current")


class _Gs2310SnmpUsersSecurityLevel_Type(Integer32):
    """Custom type gs2310SnmpUsersSecurityLevel based on Integer32"""
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


_Gs2310SnmpUsersSecurityLevel_Type.__name__ = "Integer32"
_Gs2310SnmpUsersSecurityLevel_Object = MibTableColumn
gs2310SnmpUsersSecurityLevel = _Gs2310SnmpUsersSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 3),
    _Gs2310SnmpUsersSecurityLevel_Type()
)
gs2310SnmpUsersSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersSecurityLevel.setStatus("current")


class _Gs2310SnmpUsersAuthenticationProtocol_Type(Integer32):
    """Custom type gs2310SnmpUsersAuthenticationProtocol based on Integer32"""
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


_Gs2310SnmpUsersAuthenticationProtocol_Type.__name__ = "Integer32"
_Gs2310SnmpUsersAuthenticationProtocol_Object = MibTableColumn
gs2310SnmpUsersAuthenticationProtocol = _Gs2310SnmpUsersAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 4),
    _Gs2310SnmpUsersAuthenticationProtocol_Type()
)
gs2310SnmpUsersAuthenticationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersAuthenticationProtocol.setStatus("current")
_Gs2310SnmpUsersAuthenticationPassword_Type = DisplayString
_Gs2310SnmpUsersAuthenticationPassword_Object = MibTableColumn
gs2310SnmpUsersAuthenticationPassword = _Gs2310SnmpUsersAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 5),
    _Gs2310SnmpUsersAuthenticationPassword_Type()
)
gs2310SnmpUsersAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersAuthenticationPassword.setStatus("current")


class _Gs2310SnmpUsersPrivacyProtocol_Type(Integer32):
    """Custom type gs2310SnmpUsersPrivacyProtocol based on Integer32"""
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


_Gs2310SnmpUsersPrivacyProtocol_Type.__name__ = "Integer32"
_Gs2310SnmpUsersPrivacyProtocol_Object = MibTableColumn
gs2310SnmpUsersPrivacyProtocol = _Gs2310SnmpUsersPrivacyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 6),
    _Gs2310SnmpUsersPrivacyProtocol_Type()
)
gs2310SnmpUsersPrivacyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersPrivacyProtocol.setStatus("current")
_Gs2310SnmpUsersPrivacyPassword_Type = DisplayString
_Gs2310SnmpUsersPrivacyPassword_Object = MibTableColumn
gs2310SnmpUsersPrivacyPassword = _Gs2310SnmpUsersPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 7),
    _Gs2310SnmpUsersPrivacyPassword_Type()
)
gs2310SnmpUsersPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersPrivacyPassword.setStatus("current")


class _Gs2310SnmpUsersRowStatus_Type(Integer32):
    """Custom type gs2310SnmpUsersRowStatus based on Integer32"""
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


_Gs2310SnmpUsersRowStatus_Type.__name__ = "Integer32"
_Gs2310SnmpUsersRowStatus_Object = MibTableColumn
gs2310SnmpUsersRowStatus = _Gs2310SnmpUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 4, 2, 1, 8),
    _Gs2310SnmpUsersRowStatus_Type()
)
gs2310SnmpUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpUsersRowStatus.setStatus("current")
_Gs2310SnmpGroups_ObjectIdentity = ObjectIdentity
gs2310SnmpGroups = _Gs2310SnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5)
)


class _Gs2310SnmpGroupsCreate_Type(Integer32):
    """Custom type gs2310SnmpGroupsCreate based on Integer32"""
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


_Gs2310SnmpGroupsCreate_Type.__name__ = "Integer32"
_Gs2310SnmpGroupsCreate_Object = MibScalar
gs2310SnmpGroupsCreate = _Gs2310SnmpGroupsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 1),
    _Gs2310SnmpGroupsCreate_Type()
)
gs2310SnmpGroupsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpGroupsCreate.setStatus("current")
_Gs2310SnmpGroupsTable_Object = MibTable
gs2310SnmpGroupsTable = _Gs2310SnmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gs2310SnmpGroupsTable.setStatus("current")
_Gs2310SnmpGroupsEntry_Object = MibTableRow
gs2310SnmpGroupsEntry = _Gs2310SnmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2, 1)
)
gs2310SnmpGroupsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SnmpGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2310SnmpGroupsEntry.setStatus("current")


class _Gs2310SnmpGroupsIndex_Type(Integer32):
    """Custom type gs2310SnmpGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2310SnmpGroupsIndex_Type.__name__ = "Integer32"
_Gs2310SnmpGroupsIndex_Object = MibTableColumn
gs2310SnmpGroupsIndex = _Gs2310SnmpGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2, 1, 1),
    _Gs2310SnmpGroupsIndex_Type()
)
gs2310SnmpGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SnmpGroupsIndex.setStatus("current")


class _Gs2310SnmpGroupsSecurityModel_Type(Integer32):
    """Custom type gs2310SnmpGroupsSecurityModel based on Integer32"""
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


_Gs2310SnmpGroupsSecurityModel_Type.__name__ = "Integer32"
_Gs2310SnmpGroupsSecurityModel_Object = MibTableColumn
gs2310SnmpGroupsSecurityModel = _Gs2310SnmpGroupsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2, 1, 2),
    _Gs2310SnmpGroupsSecurityModel_Type()
)
gs2310SnmpGroupsSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpGroupsSecurityModel.setStatus("current")


class _Gs2310SnmpGroupsSecurityName_Type(DisplayString):
    """Custom type gs2310SnmpGroupsSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpGroupsSecurityName_Type.__name__ = "DisplayString"
_Gs2310SnmpGroupsSecurityName_Object = MibTableColumn
gs2310SnmpGroupsSecurityName = _Gs2310SnmpGroupsSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2, 1, 3),
    _Gs2310SnmpGroupsSecurityName_Type()
)
gs2310SnmpGroupsSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpGroupsSecurityName.setStatus("current")


class _Gs2310SnmpGroupsGroupName_Type(DisplayString):
    """Custom type gs2310SnmpGroupsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpGroupsGroupName_Type.__name__ = "DisplayString"
_Gs2310SnmpGroupsGroupName_Object = MibTableColumn
gs2310SnmpGroupsGroupName = _Gs2310SnmpGroupsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2, 1, 4),
    _Gs2310SnmpGroupsGroupName_Type()
)
gs2310SnmpGroupsGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpGroupsGroupName.setStatus("current")


class _Gs2310SnmpGroupsRowStatus_Type(Integer32):
    """Custom type gs2310SnmpGroupsRowStatus based on Integer32"""
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


_Gs2310SnmpGroupsRowStatus_Type.__name__ = "Integer32"
_Gs2310SnmpGroupsRowStatus_Object = MibTableColumn
gs2310SnmpGroupsRowStatus = _Gs2310SnmpGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 5, 2, 1, 5),
    _Gs2310SnmpGroupsRowStatus_Type()
)
gs2310SnmpGroupsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpGroupsRowStatus.setStatus("current")
_Gs2310SnmpViews_ObjectIdentity = ObjectIdentity
gs2310SnmpViews = _Gs2310SnmpViews_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6)
)


class _Gs2310SnmpViewsCreate_Type(Integer32):
    """Custom type gs2310SnmpViewsCreate based on Integer32"""
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


_Gs2310SnmpViewsCreate_Type.__name__ = "Integer32"
_Gs2310SnmpViewsCreate_Object = MibScalar
gs2310SnmpViewsCreate = _Gs2310SnmpViewsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 1),
    _Gs2310SnmpViewsCreate_Type()
)
gs2310SnmpViewsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpViewsCreate.setStatus("current")
_Gs2310SnmpViewsTable_Object = MibTable
gs2310SnmpViewsTable = _Gs2310SnmpViewsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    gs2310SnmpViewsTable.setStatus("current")
_Gs2310SnmpViewsEntry_Object = MibTableRow
gs2310SnmpViewsEntry = _Gs2310SnmpViewsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2, 1)
)
gs2310SnmpViewsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SnmpViewsIndex"),
)
if mibBuilder.loadTexts:
    gs2310SnmpViewsEntry.setStatus("current")


class _Gs2310SnmpViewsIndex_Type(Integer32):
    """Custom type gs2310SnmpViewsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2310SnmpViewsIndex_Type.__name__ = "Integer32"
_Gs2310SnmpViewsIndex_Object = MibTableColumn
gs2310SnmpViewsIndex = _Gs2310SnmpViewsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2, 1, 1),
    _Gs2310SnmpViewsIndex_Type()
)
gs2310SnmpViewsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SnmpViewsIndex.setStatus("current")


class _Gs2310SnmpViewsName_Type(DisplayString):
    """Custom type gs2310SnmpViewsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpViewsName_Type.__name__ = "DisplayString"
_Gs2310SnmpViewsName_Object = MibTableColumn
gs2310SnmpViewsName = _Gs2310SnmpViewsName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2, 1, 2),
    _Gs2310SnmpViewsName_Type()
)
gs2310SnmpViewsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpViewsName.setStatus("current")


class _Gs2310SnmpViewsType_Type(Integer32):
    """Custom type gs2310SnmpViewsType based on Integer32"""
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


_Gs2310SnmpViewsType_Type.__name__ = "Integer32"
_Gs2310SnmpViewsType_Object = MibTableColumn
gs2310SnmpViewsType = _Gs2310SnmpViewsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2, 1, 3),
    _Gs2310SnmpViewsType_Type()
)
gs2310SnmpViewsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpViewsType.setStatus("current")


class _Gs2310SnmpViewsOIDSubtree_Type(DisplayString):
    """Custom type gs2310SnmpViewsOIDSubtree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Gs2310SnmpViewsOIDSubtree_Type.__name__ = "DisplayString"
_Gs2310SnmpViewsOIDSubtree_Object = MibTableColumn
gs2310SnmpViewsOIDSubtree = _Gs2310SnmpViewsOIDSubtree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2, 1, 4),
    _Gs2310SnmpViewsOIDSubtree_Type()
)
gs2310SnmpViewsOIDSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpViewsOIDSubtree.setStatus("current")


class _Gs2310SnmpViewsRowStatus_Type(Integer32):
    """Custom type gs2310SnmpViewsRowStatus based on Integer32"""
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


_Gs2310SnmpViewsRowStatus_Type.__name__ = "Integer32"
_Gs2310SnmpViewsRowStatus_Object = MibTableColumn
gs2310SnmpViewsRowStatus = _Gs2310SnmpViewsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 6, 2, 1, 5),
    _Gs2310SnmpViewsRowStatus_Type()
)
gs2310SnmpViewsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpViewsRowStatus.setStatus("current")
_Gs2310SnmpAccess_ObjectIdentity = ObjectIdentity
gs2310SnmpAccess = _Gs2310SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7)
)


class _Gs2310SnmpAccessCreate_Type(Integer32):
    """Custom type gs2310SnmpAccessCreate based on Integer32"""
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


_Gs2310SnmpAccessCreate_Type.__name__ = "Integer32"
_Gs2310SnmpAccessCreate_Object = MibScalar
gs2310SnmpAccessCreate = _Gs2310SnmpAccessCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 1),
    _Gs2310SnmpAccessCreate_Type()
)
gs2310SnmpAccessCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessCreate.setStatus("current")
_Gs2310SnmpAccessTable_Object = MibTable
gs2310SnmpAccessTable = _Gs2310SnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    gs2310SnmpAccessTable.setStatus("current")
_Gs2310SnmpAccessEntry_Object = MibTableRow
gs2310SnmpAccessEntry = _Gs2310SnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1)
)
gs2310SnmpAccessEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    gs2310SnmpAccessEntry.setStatus("current")


class _Gs2310SnmpAccessIndex_Type(Integer32):
    """Custom type gs2310SnmpAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2310SnmpAccessIndex_Type.__name__ = "Integer32"
_Gs2310SnmpAccessIndex_Object = MibTableColumn
gs2310SnmpAccessIndex = _Gs2310SnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 1),
    _Gs2310SnmpAccessIndex_Type()
)
gs2310SnmpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SnmpAccessIndex.setStatus("current")


class _Gs2310SnmpAccessGroupName_Type(DisplayString):
    """Custom type gs2310SnmpAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpAccessGroupName_Type.__name__ = "DisplayString"
_Gs2310SnmpAccessGroupName_Object = MibTableColumn
gs2310SnmpAccessGroupName = _Gs2310SnmpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 2),
    _Gs2310SnmpAccessGroupName_Type()
)
gs2310SnmpAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessGroupName.setStatus("current")


class _Gs2310SnmpAccessSecurityModel_Type(Integer32):
    """Custom type gs2310SnmpAccessSecurityModel based on Integer32"""
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


_Gs2310SnmpAccessSecurityModel_Type.__name__ = "Integer32"
_Gs2310SnmpAccessSecurityModel_Object = MibTableColumn
gs2310SnmpAccessSecurityModel = _Gs2310SnmpAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 3),
    _Gs2310SnmpAccessSecurityModel_Type()
)
gs2310SnmpAccessSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessSecurityModel.setStatus("current")


class _Gs2310SnmpAccessSecurityLevel_Type(Integer32):
    """Custom type gs2310SnmpAccessSecurityLevel based on Integer32"""
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


_Gs2310SnmpAccessSecurityLevel_Type.__name__ = "Integer32"
_Gs2310SnmpAccessSecurityLevel_Object = MibTableColumn
gs2310SnmpAccessSecurityLevel = _Gs2310SnmpAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 4),
    _Gs2310SnmpAccessSecurityLevel_Type()
)
gs2310SnmpAccessSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessSecurityLevel.setStatus("current")


class _Gs2310SnmpAccessReadViewName_Type(DisplayString):
    """Custom type gs2310SnmpAccessReadViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpAccessReadViewName_Type.__name__ = "DisplayString"
_Gs2310SnmpAccessReadViewName_Object = MibTableColumn
gs2310SnmpAccessReadViewName = _Gs2310SnmpAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 5),
    _Gs2310SnmpAccessReadViewName_Type()
)
gs2310SnmpAccessReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessReadViewName.setStatus("current")


class _Gs2310SnmpAccessWriteViewName_Type(DisplayString):
    """Custom type gs2310SnmpAccessWriteViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310SnmpAccessWriteViewName_Type.__name__ = "DisplayString"
_Gs2310SnmpAccessWriteViewName_Object = MibTableColumn
gs2310SnmpAccessWriteViewName = _Gs2310SnmpAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 6),
    _Gs2310SnmpAccessWriteViewName_Type()
)
gs2310SnmpAccessWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessWriteViewName.setStatus("current")


class _Gs2310SnmpAccessRowStatus_Type(Integer32):
    """Custom type gs2310SnmpAccessRowStatus based on Integer32"""
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


_Gs2310SnmpAccessRowStatus_Type.__name__ = "Integer32"
_Gs2310SnmpAccessRowStatus_Object = MibTableColumn
gs2310SnmpAccessRowStatus = _Gs2310SnmpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 1, 6, 7, 2, 1, 7),
    _Gs2310SnmpAccessRowStatus_Type()
)
gs2310SnmpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SnmpAccessRowStatus.setStatus("current")
_Gs2310Configuration_ObjectIdentity = ObjectIdentity
gs2310Configuration = _Gs2310Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2)
)
_Gs2310Port_ObjectIdentity = ObjectIdentity
gs2310Port = _Gs2310Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1)
)
_Gs2310PortConfigurationTable_Object = MibTable
gs2310PortConfigurationTable = _Gs2310PortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1)
)
if mibBuilder.loadTexts:
    gs2310PortConfigurationTable.setStatus("current")
_Gs2310PortConfigurationEntry_Object = MibTableRow
gs2310PortConfigurationEntry = _Gs2310PortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1)
)
gs2310PortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310PortConfigurationEntry.setStatus("current")


class _Gs2310PortConfPort_Type(Integer32):
    """Custom type gs2310PortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortConfPort_Type.__name__ = "Integer32"
_Gs2310PortConfPort_Object = MibTableColumn
gs2310PortConfPort = _Gs2310PortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 1),
    _Gs2310PortConfPort_Type()
)
gs2310PortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortConfPort.setStatus("current")


class _Gs2310PortConfPortMedia_Type(DisplayString):
    """Custom type gs2310PortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Gs2310PortConfPortMedia_Type.__name__ = "DisplayString"
_Gs2310PortConfPortMedia_Object = MibTableColumn
gs2310PortConfPortMedia = _Gs2310PortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 2),
    _Gs2310PortConfPortMedia_Type()
)
gs2310PortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortConfPortMedia.setStatus("current")


class _Gs2310PortConfLink_Type(DisplayString):
    """Custom type gs2310PortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Gs2310PortConfLink_Type.__name__ = "DisplayString"
_Gs2310PortConfLink_Object = MibTableColumn
gs2310PortConfLink = _Gs2310PortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 3),
    _Gs2310PortConfLink_Type()
)
gs2310PortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortConfLink.setStatus("current")


class _Gs2310PortConfCurrentSpeed_Type(DisplayString):
    """Custom type gs2310PortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Gs2310PortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Gs2310PortConfCurrentSpeed_Object = MibTableColumn
gs2310PortConfCurrentSpeed = _Gs2310PortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 4),
    _Gs2310PortConfCurrentSpeed_Type()
)
gs2310PortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortConfCurrentSpeed.setStatus("current")


class _Gs2310PortConfSpeed_Type(Integer32):
    """Custom type gs2310PortConfSpeed based on Integer32"""
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
              11)
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
          ("speed1000X", 11))
    )


_Gs2310PortConfSpeed_Type.__name__ = "Integer32"
_Gs2310PortConfSpeed_Object = MibTableColumn
gs2310PortConfSpeed = _Gs2310PortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 5),
    _Gs2310PortConfSpeed_Type()
)
gs2310PortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortConfSpeed.setStatus("current")


class _Gs2310PortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type gs2310PortConfCurrentFlowControlRx based on Integer32"""
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


_Gs2310PortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Gs2310PortConfCurrentFlowControlRx_Object = MibTableColumn
gs2310PortConfCurrentFlowControlRx = _Gs2310PortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 6),
    _Gs2310PortConfCurrentFlowControlRx_Type()
)
gs2310PortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortConfCurrentFlowControlRx.setStatus("current")


class _Gs2310PortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type gs2310PortConfCurrentFlowControlTx based on Integer32"""
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


_Gs2310PortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Gs2310PortConfCurrentFlowControlTx_Object = MibTableColumn
gs2310PortConfCurrentFlowControlTx = _Gs2310PortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 7),
    _Gs2310PortConfCurrentFlowControlTx_Type()
)
gs2310PortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortConfCurrentFlowControlTx.setStatus("current")


class _Gs2310PortConfFlowControl_Type(Integer32):
    """Custom type gs2310PortConfFlowControl based on Integer32"""
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


_Gs2310PortConfFlowControl_Type.__name__ = "Integer32"
_Gs2310PortConfFlowControl_Object = MibTableColumn
gs2310PortConfFlowControl = _Gs2310PortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 8),
    _Gs2310PortConfFlowControl_Type()
)
gs2310PortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortConfFlowControl.setStatus("current")


class _Gs2310PortConfMaxFrameSize_Type(Integer32):
    """Custom type gs2310PortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Gs2310PortConfMaxFrameSize_Type.__name__ = "Integer32"
_Gs2310PortConfMaxFrameSize_Object = MibTableColumn
gs2310PortConfMaxFrameSize = _Gs2310PortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 9),
    _Gs2310PortConfMaxFrameSize_Type()
)
gs2310PortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortConfMaxFrameSize.setStatus("current")


class _Gs2310PortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type gs2310PortConfExcessiveCollisionMode based on Integer32"""
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


_Gs2310PortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Gs2310PortConfExcessiveCollisionMode_Object = MibTableColumn
gs2310PortConfExcessiveCollisionMode = _Gs2310PortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 10),
    _Gs2310PortConfExcessiveCollisionMode_Type()
)
gs2310PortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortConfExcessiveCollisionMode.setStatus("current")


class _Gs2310PortConfPowerControl_Type(Integer32):
    """Custom type gs2310PortConfPowerControl based on Integer32"""
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


_Gs2310PortConfPowerControl_Type.__name__ = "Integer32"
_Gs2310PortConfPowerControl_Object = MibTableColumn
gs2310PortConfPowerControl = _Gs2310PortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 11),
    _Gs2310PortConfPowerControl_Type()
)
gs2310PortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortConfPowerControl.setStatus("current")
_Gs2310PortConfDescription_Type = DisplayString
_Gs2310PortConfDescription_Object = MibTableColumn
gs2310PortConfDescription = _Gs2310PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 1, 1, 12),
    _Gs2310PortConfDescription_Type()
)
gs2310PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortConfDescription.setStatus("current")
_Gs2310PortTrafficStatisticsTable_Object = MibTable
gs2310PortTrafficStatisticsTable = _Gs2310PortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310PortTrafficStatisticsTable.setStatus("current")
_Gs2310PortTrafficStatisticsEntry_Object = MibTableRow
gs2310PortTrafficStatisticsEntry = _Gs2310PortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1)
)
gs2310PortTrafficStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2310PortTrafficStatisticsEntry.setStatus("current")


class _Gs2310PortTrafficStatisticsPort_Type(Integer32):
    """Custom type gs2310PortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Gs2310PortTrafficStatisticsPort_Object = MibTableColumn
gs2310PortTrafficStatisticsPort = _Gs2310PortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 1),
    _Gs2310PortTrafficStatisticsPort_Type()
)
gs2310PortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortTrafficStatisticsPort.setStatus("current")


class _Gs2310PortTrafficStatisticsClear_Type(Integer32):
    """Custom type gs2310PortTrafficStatisticsClear based on Integer32"""
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


_Gs2310PortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Gs2310PortTrafficStatisticsClear_Object = MibTableColumn
gs2310PortTrafficStatisticsClear = _Gs2310PortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 2),
    _Gs2310PortTrafficStatisticsClear_Type()
)
gs2310PortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortTrafficStatisticsClear.setStatus("current")
_Gs2310PortTrafficRxPackets_Type = Counter64
_Gs2310PortTrafficRxPackets_Object = MibTableColumn
gs2310PortTrafficRxPackets = _Gs2310PortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 3),
    _Gs2310PortTrafficRxPackets_Type()
)
gs2310PortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxPackets.setStatus("current")
_Gs2310PortTrafficRxOctets_Type = Counter64
_Gs2310PortTrafficRxOctets_Object = MibTableColumn
gs2310PortTrafficRxOctets = _Gs2310PortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 4),
    _Gs2310PortTrafficRxOctets_Type()
)
gs2310PortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxOctets.setStatus("current")
_Gs2310PortTrafficRxUnicast_Type = Counter64
_Gs2310PortTrafficRxUnicast_Object = MibTableColumn
gs2310PortTrafficRxUnicast = _Gs2310PortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 5),
    _Gs2310PortTrafficRxUnicast_Type()
)
gs2310PortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxUnicast.setStatus("current")
_Gs2310PortTrafficRxMulticast_Type = Counter64
_Gs2310PortTrafficRxMulticast_Object = MibTableColumn
gs2310PortTrafficRxMulticast = _Gs2310PortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 6),
    _Gs2310PortTrafficRxMulticast_Type()
)
gs2310PortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxMulticast.setStatus("current")
_Gs2310PortTrafficRxBroadcast_Type = Counter64
_Gs2310PortTrafficRxBroadcast_Object = MibTableColumn
gs2310PortTrafficRxBroadcast = _Gs2310PortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 7),
    _Gs2310PortTrafficRxBroadcast_Type()
)
gs2310PortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxBroadcast.setStatus("current")
_Gs2310PortTrafficRxPause_Type = Counter64
_Gs2310PortTrafficRxPause_Object = MibTableColumn
gs2310PortTrafficRxPause = _Gs2310PortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 8),
    _Gs2310PortTrafficRxPause_Type()
)
gs2310PortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxPause.setStatus("current")
_Gs2310PortTrafficRx64Bytes_Type = Counter64
_Gs2310PortTrafficRx64Bytes_Object = MibTableColumn
gs2310PortTrafficRx64Bytes = _Gs2310PortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 9),
    _Gs2310PortTrafficRx64Bytes_Type()
)
gs2310PortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRx64Bytes.setStatus("current")
_Gs2310PortTrafficRx65to127Bytes_Type = Counter64
_Gs2310PortTrafficRx65to127Bytes_Object = MibTableColumn
gs2310PortTrafficRx65to127Bytes = _Gs2310PortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 10),
    _Gs2310PortTrafficRx65to127Bytes_Type()
)
gs2310PortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRx65to127Bytes.setStatus("current")
_Gs2310PortTrafficRx128to255Bytes_Type = Counter64
_Gs2310PortTrafficRx128to255Bytes_Object = MibTableColumn
gs2310PortTrafficRx128to255Bytes = _Gs2310PortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 11),
    _Gs2310PortTrafficRx128to255Bytes_Type()
)
gs2310PortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRx128to255Bytes.setStatus("current")
_Gs2310PortTrafficRx256to511Bytes_Type = Counter64
_Gs2310PortTrafficRx256to511Bytes_Object = MibTableColumn
gs2310PortTrafficRx256to511Bytes = _Gs2310PortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 12),
    _Gs2310PortTrafficRx256to511Bytes_Type()
)
gs2310PortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRx256to511Bytes.setStatus("current")
_Gs2310PortTrafficRx512to1023Bytes_Type = Counter64
_Gs2310PortTrafficRx512to1023Bytes_Object = MibTableColumn
gs2310PortTrafficRx512to1023Bytes = _Gs2310PortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 13),
    _Gs2310PortTrafficRx512to1023Bytes_Type()
)
gs2310PortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRx512to1023Bytes.setStatus("current")
_Gs2310PortTrafficRx1024to1526Bytes_Type = Counter64
_Gs2310PortTrafficRx1024to1526Bytes_Object = MibTableColumn
gs2310PortTrafficRx1024to1526Bytes = _Gs2310PortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 14),
    _Gs2310PortTrafficRx1024to1526Bytes_Type()
)
gs2310PortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRx1024to1526Bytes.setStatus("current")
_Gs2310PortTrafficRxExceecd1527Bytes_Type = Counter64
_Gs2310PortTrafficRxExceecd1527Bytes_Object = MibTableColumn
gs2310PortTrafficRxExceecd1527Bytes = _Gs2310PortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 15),
    _Gs2310PortTrafficRxExceecd1527Bytes_Type()
)
gs2310PortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxExceecd1527Bytes.setStatus("current")
_Gs2310PortTrafficRxQ0_Type = Counter64
_Gs2310PortTrafficRxQ0_Object = MibTableColumn
gs2310PortTrafficRxQ0 = _Gs2310PortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 16),
    _Gs2310PortTrafficRxQ0_Type()
)
gs2310PortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ0.setStatus("current")
_Gs2310PortTrafficRxQ1_Type = Counter64
_Gs2310PortTrafficRxQ1_Object = MibTableColumn
gs2310PortTrafficRxQ1 = _Gs2310PortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 17),
    _Gs2310PortTrafficRxQ1_Type()
)
gs2310PortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ1.setStatus("current")
_Gs2310PortTrafficRxQ2_Type = Counter64
_Gs2310PortTrafficRxQ2_Object = MibTableColumn
gs2310PortTrafficRxQ2 = _Gs2310PortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 18),
    _Gs2310PortTrafficRxQ2_Type()
)
gs2310PortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ2.setStatus("current")
_Gs2310PortTrafficRxQ3_Type = Counter64
_Gs2310PortTrafficRxQ3_Object = MibTableColumn
gs2310PortTrafficRxQ3 = _Gs2310PortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 19),
    _Gs2310PortTrafficRxQ3_Type()
)
gs2310PortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ3.setStatus("current")
_Gs2310PortTrafficRxQ4_Type = Counter64
_Gs2310PortTrafficRxQ4_Object = MibTableColumn
gs2310PortTrafficRxQ4 = _Gs2310PortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 20),
    _Gs2310PortTrafficRxQ4_Type()
)
gs2310PortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ4.setStatus("current")
_Gs2310PortTrafficRxQ5_Type = Counter64
_Gs2310PortTrafficRxQ5_Object = MibTableColumn
gs2310PortTrafficRxQ5 = _Gs2310PortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 21),
    _Gs2310PortTrafficRxQ5_Type()
)
gs2310PortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ5.setStatus("current")
_Gs2310PortTrafficRxQ6_Type = Counter64
_Gs2310PortTrafficRxQ6_Object = MibTableColumn
gs2310PortTrafficRxQ6 = _Gs2310PortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 22),
    _Gs2310PortTrafficRxQ6_Type()
)
gs2310PortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ6.setStatus("current")
_Gs2310PortTrafficRxQ7_Type = Counter64
_Gs2310PortTrafficRxQ7_Object = MibTableColumn
gs2310PortTrafficRxQ7 = _Gs2310PortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 23),
    _Gs2310PortTrafficRxQ7_Type()
)
gs2310PortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxQ7.setStatus("current")
_Gs2310PortTrafficRxDrops_Type = Counter64
_Gs2310PortTrafficRxDrops_Object = MibTableColumn
gs2310PortTrafficRxDrops = _Gs2310PortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 24),
    _Gs2310PortTrafficRxDrops_Type()
)
gs2310PortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxDrops.setStatus("current")
_Gs2310PortTrafficRxCRCorAlignment_Type = Counter64
_Gs2310PortTrafficRxCRCorAlignment_Object = MibTableColumn
gs2310PortTrafficRxCRCorAlignment = _Gs2310PortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 25),
    _Gs2310PortTrafficRxCRCorAlignment_Type()
)
gs2310PortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxCRCorAlignment.setStatus("current")
_Gs2310PortTrafficRxUndersize_Type = Counter64
_Gs2310PortTrafficRxUndersize_Object = MibTableColumn
gs2310PortTrafficRxUndersize = _Gs2310PortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 26),
    _Gs2310PortTrafficRxUndersize_Type()
)
gs2310PortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxUndersize.setStatus("current")
_Gs2310PortTrafficRxOversize_Type = Counter64
_Gs2310PortTrafficRxOversize_Object = MibTableColumn
gs2310PortTrafficRxOversize = _Gs2310PortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 27),
    _Gs2310PortTrafficRxOversize_Type()
)
gs2310PortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxOversize.setStatus("current")
_Gs2310PortTrafficRxFragments_Type = Counter64
_Gs2310PortTrafficRxFragments_Object = MibTableColumn
gs2310PortTrafficRxFragments = _Gs2310PortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 28),
    _Gs2310PortTrafficRxFragments_Type()
)
gs2310PortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxFragments.setStatus("current")
_Gs2310PortTrafficRxJabber_Type = Counter64
_Gs2310PortTrafficRxJabber_Object = MibTableColumn
gs2310PortTrafficRxJabber = _Gs2310PortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 29),
    _Gs2310PortTrafficRxJabber_Type()
)
gs2310PortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxJabber.setStatus("current")
_Gs2310PortTrafficRxFiltered_Type = Counter64
_Gs2310PortTrafficRxFiltered_Object = MibTableColumn
gs2310PortTrafficRxFiltered = _Gs2310PortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 30),
    _Gs2310PortTrafficRxFiltered_Type()
)
gs2310PortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficRxFiltered.setStatus("current")
_Gs2310PortTrafficTxPackets_Type = Counter64
_Gs2310PortTrafficTxPackets_Object = MibTableColumn
gs2310PortTrafficTxPackets = _Gs2310PortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 31),
    _Gs2310PortTrafficTxPackets_Type()
)
gs2310PortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxPackets.setStatus("current")
_Gs2310PortTrafficTxOctets_Type = Counter64
_Gs2310PortTrafficTxOctets_Object = MibTableColumn
gs2310PortTrafficTxOctets = _Gs2310PortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 32),
    _Gs2310PortTrafficTxOctets_Type()
)
gs2310PortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxOctets.setStatus("current")
_Gs2310PortTrafficTxUnicast_Type = Counter64
_Gs2310PortTrafficTxUnicast_Object = MibTableColumn
gs2310PortTrafficTxUnicast = _Gs2310PortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 33),
    _Gs2310PortTrafficTxUnicast_Type()
)
gs2310PortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxUnicast.setStatus("current")
_Gs2310PortTrafficTxMulticast_Type = Counter64
_Gs2310PortTrafficTxMulticast_Object = MibTableColumn
gs2310PortTrafficTxMulticast = _Gs2310PortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 34),
    _Gs2310PortTrafficTxMulticast_Type()
)
gs2310PortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxMulticast.setStatus("current")
_Gs2310PortTrafficTxBroadcast_Type = Counter64
_Gs2310PortTrafficTxBroadcast_Object = MibTableColumn
gs2310PortTrafficTxBroadcast = _Gs2310PortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 35),
    _Gs2310PortTrafficTxBroadcast_Type()
)
gs2310PortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxBroadcast.setStatus("current")
_Gs2310PortTrafficTxPause_Type = Counter64
_Gs2310PortTrafficTxPause_Object = MibTableColumn
gs2310PortTrafficTxPause = _Gs2310PortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 36),
    _Gs2310PortTrafficTxPause_Type()
)
gs2310PortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxPause.setStatus("current")
_Gs2310PortTrafficTx64Bytes_Type = Counter64
_Gs2310PortTrafficTx64Bytes_Object = MibTableColumn
gs2310PortTrafficTx64Bytes = _Gs2310PortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 37),
    _Gs2310PortTrafficTx64Bytes_Type()
)
gs2310PortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTx64Bytes.setStatus("current")
_Gs2310PortTrafficTx65to127Bytes_Type = Counter64
_Gs2310PortTrafficTx65to127Bytes_Object = MibTableColumn
gs2310PortTrafficTx65to127Bytes = _Gs2310PortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 38),
    _Gs2310PortTrafficTx65to127Bytes_Type()
)
gs2310PortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTx65to127Bytes.setStatus("current")
_Gs2310PortTrafficTx128to255Bytes_Type = Counter64
_Gs2310PortTrafficTx128to255Bytes_Object = MibTableColumn
gs2310PortTrafficTx128to255Bytes = _Gs2310PortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 39),
    _Gs2310PortTrafficTx128to255Bytes_Type()
)
gs2310PortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTx128to255Bytes.setStatus("current")
_Gs2310PortTrafficTx256to511Bytes_Type = Counter64
_Gs2310PortTrafficTx256to511Bytes_Object = MibTableColumn
gs2310PortTrafficTx256to511Bytes = _Gs2310PortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 40),
    _Gs2310PortTrafficTx256to511Bytes_Type()
)
gs2310PortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTx256to511Bytes.setStatus("current")
_Gs2310PortTrafficTx512to1023Bytes_Type = Counter64
_Gs2310PortTrafficTx512to1023Bytes_Object = MibTableColumn
gs2310PortTrafficTx512to1023Bytes = _Gs2310PortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 41),
    _Gs2310PortTrafficTx512to1023Bytes_Type()
)
gs2310PortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTx512to1023Bytes.setStatus("current")
_Gs2310PortTrafficTx1024to1526Bytes_Type = Counter64
_Gs2310PortTrafficTx1024to1526Bytes_Object = MibTableColumn
gs2310PortTrafficTx1024to1526Bytes = _Gs2310PortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 42),
    _Gs2310PortTrafficTx1024to1526Bytes_Type()
)
gs2310PortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTx1024to1526Bytes.setStatus("current")
_Gs2310PortTrafficTxExceecd1527Bytes_Type = Counter64
_Gs2310PortTrafficTxExceecd1527Bytes_Object = MibTableColumn
gs2310PortTrafficTxExceecd1527Bytes = _Gs2310PortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 43),
    _Gs2310PortTrafficTxExceecd1527Bytes_Type()
)
gs2310PortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxExceecd1527Bytes.setStatus("current")
_Gs2310PortTrafficTxQ0_Type = Counter64
_Gs2310PortTrafficTxQ0_Object = MibTableColumn
gs2310PortTrafficTxQ0 = _Gs2310PortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 44),
    _Gs2310PortTrafficTxQ0_Type()
)
gs2310PortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ0.setStatus("current")
_Gs2310PortTrafficTxQ1_Type = Counter64
_Gs2310PortTrafficTxQ1_Object = MibTableColumn
gs2310PortTrafficTxQ1 = _Gs2310PortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 45),
    _Gs2310PortTrafficTxQ1_Type()
)
gs2310PortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ1.setStatus("current")
_Gs2310PortTrafficTxQ2_Type = Counter64
_Gs2310PortTrafficTxQ2_Object = MibTableColumn
gs2310PortTrafficTxQ2 = _Gs2310PortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 46),
    _Gs2310PortTrafficTxQ2_Type()
)
gs2310PortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ2.setStatus("current")
_Gs2310PortTrafficTxQ3_Type = Counter64
_Gs2310PortTrafficTxQ3_Object = MibTableColumn
gs2310PortTrafficTxQ3 = _Gs2310PortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 47),
    _Gs2310PortTrafficTxQ3_Type()
)
gs2310PortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ3.setStatus("current")
_Gs2310PortTrafficTxQ4_Type = Counter64
_Gs2310PortTrafficTxQ4_Object = MibTableColumn
gs2310PortTrafficTxQ4 = _Gs2310PortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 48),
    _Gs2310PortTrafficTxQ4_Type()
)
gs2310PortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ4.setStatus("current")
_Gs2310PortTrafficTxQ5_Type = Counter64
_Gs2310PortTrafficTxQ5_Object = MibTableColumn
gs2310PortTrafficTxQ5 = _Gs2310PortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 49),
    _Gs2310PortTrafficTxQ5_Type()
)
gs2310PortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ5.setStatus("current")
_Gs2310PortTrafficTxQ6_Type = Counter64
_Gs2310PortTrafficTxQ6_Object = MibTableColumn
gs2310PortTrafficTxQ6 = _Gs2310PortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 50),
    _Gs2310PortTrafficTxQ6_Type()
)
gs2310PortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ6.setStatus("current")
_Gs2310PortTrafficTxQ7_Type = Counter64
_Gs2310PortTrafficTxQ7_Object = MibTableColumn
gs2310PortTrafficTxQ7 = _Gs2310PortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 51),
    _Gs2310PortTrafficTxQ7_Type()
)
gs2310PortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxQ7.setStatus("current")
_Gs2310PortTrafficTxDrops_Type = Counter64
_Gs2310PortTrafficTxDrops_Object = MibTableColumn
gs2310PortTrafficTxDrops = _Gs2310PortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 52),
    _Gs2310PortTrafficTxDrops_Type()
)
gs2310PortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxDrops.setStatus("current")
_Gs2310PortTrafficTxLateOrExcColl_Type = Counter64
_Gs2310PortTrafficTxLateOrExcColl_Object = MibTableColumn
gs2310PortTrafficTxLateOrExcColl = _Gs2310PortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 2, 1, 53),
    _Gs2310PortTrafficTxLateOrExcColl_Type()
)
gs2310PortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortTrafficTxLateOrExcColl.setStatus("current")
_Gs2310PortQoSStatistics_ObjectIdentity = ObjectIdentity
gs2310PortQoSStatistics = _Gs2310PortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3)
)


class _Gs2310PortQoSStatisticsClear_Type(Integer32):
    """Custom type gs2310PortQoSStatisticsClear based on Integer32"""
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


_Gs2310PortQoSStatisticsClear_Type.__name__ = "Integer32"
_Gs2310PortQoSStatisticsClear_Object = MibScalar
gs2310PortQoSStatisticsClear = _Gs2310PortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 1),
    _Gs2310PortQoSStatisticsClear_Type()
)
gs2310PortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSStatisticsClear.setStatus("current")
_Gs2310PortQoSStatisticsTable_Object = MibTable
gs2310PortQoSStatisticsTable = _Gs2310PortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310PortQoSStatisticsTable.setStatus("current")
_Gs2310PortQoSStatisticsEntry_Object = MibTableRow
gs2310PortQoSStatisticsEntry = _Gs2310PortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1)
)
gs2310PortQoSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2310PortQoSStatisticsEntry.setStatus("current")


class _Gs2310PortQoSStatisticsPort_Type(Integer32):
    """Custom type gs2310PortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortQoSStatisticsPort_Type.__name__ = "Integer32"
_Gs2310PortQoSStatisticsPort_Object = MibTableColumn
gs2310PortQoSStatisticsPort = _Gs2310PortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 1),
    _Gs2310PortQoSStatisticsPort_Type()
)
gs2310PortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortQoSStatisticsPort.setStatus("current")
_Gs2310PortQoSQ0Rx_Type = Counter64
_Gs2310PortQoSQ0Rx_Object = MibTableColumn
gs2310PortQoSQ0Rx = _Gs2310PortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 2),
    _Gs2310PortQoSQ0Rx_Type()
)
gs2310PortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ0Rx.setStatus("current")
_Gs2310PortQoSQ0Tx_Type = Counter64
_Gs2310PortQoSQ0Tx_Object = MibTableColumn
gs2310PortQoSQ0Tx = _Gs2310PortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 3),
    _Gs2310PortQoSQ0Tx_Type()
)
gs2310PortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ0Tx.setStatus("current")
_Gs2310PortQoSQ1Rx_Type = Counter64
_Gs2310PortQoSQ1Rx_Object = MibTableColumn
gs2310PortQoSQ1Rx = _Gs2310PortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 4),
    _Gs2310PortQoSQ1Rx_Type()
)
gs2310PortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ1Rx.setStatus("current")
_Gs2310PortQoSQ1Tx_Type = Counter64
_Gs2310PortQoSQ1Tx_Object = MibTableColumn
gs2310PortQoSQ1Tx = _Gs2310PortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 5),
    _Gs2310PortQoSQ1Tx_Type()
)
gs2310PortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ1Tx.setStatus("current")
_Gs2310PortQoSQ2Rx_Type = Counter64
_Gs2310PortQoSQ2Rx_Object = MibTableColumn
gs2310PortQoSQ2Rx = _Gs2310PortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 6),
    _Gs2310PortQoSQ2Rx_Type()
)
gs2310PortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ2Rx.setStatus("current")
_Gs2310PortQoSQ2Tx_Type = Counter64
_Gs2310PortQoSQ2Tx_Object = MibTableColumn
gs2310PortQoSQ2Tx = _Gs2310PortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 7),
    _Gs2310PortQoSQ2Tx_Type()
)
gs2310PortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ2Tx.setStatus("current")
_Gs2310PortQoSQ3Rx_Type = Counter64
_Gs2310PortQoSQ3Rx_Object = MibTableColumn
gs2310PortQoSQ3Rx = _Gs2310PortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 8),
    _Gs2310PortQoSQ3Rx_Type()
)
gs2310PortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ3Rx.setStatus("current")
_Gs2310PortQoSQ3Tx_Type = Counter64
_Gs2310PortQoSQ3Tx_Object = MibTableColumn
gs2310PortQoSQ3Tx = _Gs2310PortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 9),
    _Gs2310PortQoSQ3Tx_Type()
)
gs2310PortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ3Tx.setStatus("current")
_Gs2310PortQoSQ4Rx_Type = Counter64
_Gs2310PortQoSQ4Rx_Object = MibTableColumn
gs2310PortQoSQ4Rx = _Gs2310PortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 10),
    _Gs2310PortQoSQ4Rx_Type()
)
gs2310PortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ4Rx.setStatus("current")
_Gs2310PortQoSQ4Tx_Type = Counter64
_Gs2310PortQoSQ4Tx_Object = MibTableColumn
gs2310PortQoSQ4Tx = _Gs2310PortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 11),
    _Gs2310PortQoSQ4Tx_Type()
)
gs2310PortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ4Tx.setStatus("current")
_Gs2310PortQoSQ5Rx_Type = Counter64
_Gs2310PortQoSQ5Rx_Object = MibTableColumn
gs2310PortQoSQ5Rx = _Gs2310PortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 12),
    _Gs2310PortQoSQ5Rx_Type()
)
gs2310PortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ5Rx.setStatus("current")
_Gs2310PortQoSQ5Tx_Type = Counter64
_Gs2310PortQoSQ5Tx_Object = MibTableColumn
gs2310PortQoSQ5Tx = _Gs2310PortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 13),
    _Gs2310PortQoSQ5Tx_Type()
)
gs2310PortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ5Tx.setStatus("current")
_Gs2310PortQoSQ6Rx_Type = Counter64
_Gs2310PortQoSQ6Rx_Object = MibTableColumn
gs2310PortQoSQ6Rx = _Gs2310PortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 14),
    _Gs2310PortQoSQ6Rx_Type()
)
gs2310PortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ6Rx.setStatus("current")
_Gs2310PortQoSQ6Tx_Type = Counter64
_Gs2310PortQoSQ6Tx_Object = MibTableColumn
gs2310PortQoSQ6Tx = _Gs2310PortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 15),
    _Gs2310PortQoSQ6Tx_Type()
)
gs2310PortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ6Tx.setStatus("current")
_Gs2310PortQoSQ7Rx_Type = Counter64
_Gs2310PortQoSQ7Rx_Object = MibTableColumn
gs2310PortQoSQ7Rx = _Gs2310PortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 16),
    _Gs2310PortQoSQ7Rx_Type()
)
gs2310PortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ7Rx.setStatus("current")
_Gs2310PortQoSQ7Tx_Type = Counter64
_Gs2310PortQoSQ7Tx_Object = MibTableColumn
gs2310PortQoSQ7Tx = _Gs2310PortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 3, 2, 1, 17),
    _Gs2310PortQoSQ7Tx_Type()
)
gs2310PortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortQoSQ7Tx.setStatus("current")
_Gs2310SFPInfoTable_Object = MibTable
gs2310SFPInfoTable = _Gs2310SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4)
)
if mibBuilder.loadTexts:
    gs2310SFPInfoTable.setStatus("current")
_Gs2310SFPInfoEntry_Object = MibTableRow
gs2310SFPInfoEntry = _Gs2310SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1)
)
gs2310SFPInfoEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2310SFPInfoEntry.setStatus("current")


class _Gs2310SFPInfoIndex_Type(Integer32):
    """Custom type gs2310SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310SFPInfoIndex_Type.__name__ = "Integer32"
_Gs2310SFPInfoIndex_Object = MibTableColumn
gs2310SFPInfoIndex = _Gs2310SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 1),
    _Gs2310SFPInfoIndex_Type()
)
gs2310SFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310SFPInfoIndex.setStatus("current")
_Gs2310SFPInfoPort_Type = DisplayString
_Gs2310SFPInfoPort_Object = MibTableColumn
gs2310SFPInfoPort = _Gs2310SFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 2),
    _Gs2310SFPInfoPort_Type()
)
gs2310SFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPInfoPort.setStatus("current")
_Gs2310SFPConnectorType_Type = DisplayString
_Gs2310SFPConnectorType_Object = MibTableColumn
gs2310SFPConnectorType = _Gs2310SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 3),
    _Gs2310SFPConnectorType_Type()
)
gs2310SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPConnectorType.setStatus("current")
_Gs2310SFPFiberType_Type = DisplayString
_Gs2310SFPFiberType_Object = MibTableColumn
gs2310SFPFiberType = _Gs2310SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 4),
    _Gs2310SFPFiberType_Type()
)
gs2310SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPFiberType.setStatus("current")
_Gs2310SFPTxCentralWavelength_Type = DisplayString
_Gs2310SFPTxCentralWavelength_Object = MibTableColumn
gs2310SFPTxCentralWavelength = _Gs2310SFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 5),
    _Gs2310SFPTxCentralWavelength_Type()
)
gs2310SFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPTxCentralWavelength.setStatus("current")
_Gs2310SFPBaudRate_Type = DisplayString
_Gs2310SFPBaudRate_Object = MibTableColumn
gs2310SFPBaudRate = _Gs2310SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 6),
    _Gs2310SFPBaudRate_Type()
)
gs2310SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPBaudRate.setStatus("current")
_Gs2310SFPVendorOUI_Type = DisplayString
_Gs2310SFPVendorOUI_Object = MibTableColumn
gs2310SFPVendorOUI = _Gs2310SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 7),
    _Gs2310SFPVendorOUI_Type()
)
gs2310SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPVendorOUI.setStatus("current")
_Gs2310SFPVendorName_Type = DisplayString
_Gs2310SFPVendorName_Object = MibTableColumn
gs2310SFPVendorName = _Gs2310SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 8),
    _Gs2310SFPVendorName_Type()
)
gs2310SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPVendorName.setStatus("current")
_Gs2310SFPVendorPN_Type = DisplayString
_Gs2310SFPVendorPN_Object = MibTableColumn
gs2310SFPVendorPN = _Gs2310SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 9),
    _Gs2310SFPVendorPN_Type()
)
gs2310SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPVendorPN.setStatus("current")
_Gs2310SFPVendorRev_Type = DisplayString
_Gs2310SFPVendorRev_Object = MibTableColumn
gs2310SFPVendorRev = _Gs2310SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 10),
    _Gs2310SFPVendorRev_Type()
)
gs2310SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPVendorRev.setStatus("current")
_Gs2310SFPVendorSN_Type = DisplayString
_Gs2310SFPVendorSN_Object = MibTableColumn
gs2310SFPVendorSN = _Gs2310SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 11),
    _Gs2310SFPVendorSN_Type()
)
gs2310SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPVendorSN.setStatus("current")
_Gs2310SFPDateCode_Type = DisplayString
_Gs2310SFPDateCode_Object = MibTableColumn
gs2310SFPDateCode = _Gs2310SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 12),
    _Gs2310SFPDateCode_Type()
)
gs2310SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPDateCode.setStatus("current")
_Gs2310SFPTemperature_Type = DisplayString
_Gs2310SFPTemperature_Object = MibTableColumn
gs2310SFPTemperature = _Gs2310SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 13),
    _Gs2310SFPTemperature_Type()
)
gs2310SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPTemperature.setStatus("current")
_Gs2310SFPVcc_Type = DisplayString
_Gs2310SFPVcc_Object = MibTableColumn
gs2310SFPVcc = _Gs2310SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 14),
    _Gs2310SFPVcc_Type()
)
gs2310SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPVcc.setStatus("current")
_Gs2310SFPMon1Bias_Type = DisplayString
_Gs2310SFPMon1Bias_Object = MibTableColumn
gs2310SFPMon1Bias = _Gs2310SFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 15),
    _Gs2310SFPMon1Bias_Type()
)
gs2310SFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPMon1Bias.setStatus("current")
_Gs2310SFPMon2TxPWR_Type = DisplayString
_Gs2310SFPMon2TxPWR_Object = MibTableColumn
gs2310SFPMon2TxPWR = _Gs2310SFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 16),
    _Gs2310SFPMon2TxPWR_Type()
)
gs2310SFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPMon2TxPWR.setStatus("current")
_Gs2310SFPMon3RxPWR_Type = DisplayString
_Gs2310SFPMon3RxPWR_Object = MibTableColumn
gs2310SFPMon3RxPWR = _Gs2310SFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 4, 1, 17),
    _Gs2310SFPMon3RxPWR_Type()
)
gs2310SFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SFPMon3RxPWR.setStatus("current")
_Gs2310PortEEETable_Object = MibTable
gs2310PortEEETable = _Gs2310PortEEETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2310PortEEETable.setStatus("current")
_Gs2310PortEEEEntry_Object = MibTableRow
gs2310PortEEEEntry = _Gs2310PortEEEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1)
)
gs2310PortEEEEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortEEEPort"),
)
if mibBuilder.loadTexts:
    gs2310PortEEEEntry.setStatus("current")


class _Gs2310PortEEEPort_Type(Integer32):
    """Custom type gs2310PortEEEPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortEEEPort_Type.__name__ = "Integer32"
_Gs2310PortEEEPort_Object = MibTableColumn
gs2310PortEEEPort = _Gs2310PortEEEPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 1),
    _Gs2310PortEEEPort_Type()
)
gs2310PortEEEPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortEEEPort.setStatus("current")


class _Gs2310PortEEEMode_Type(Integer32):
    """Custom type gs2310PortEEEMode based on Integer32"""
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


_Gs2310PortEEEMode_Type.__name__ = "Integer32"
_Gs2310PortEEEMode_Object = MibTableColumn
gs2310PortEEEMode = _Gs2310PortEEEMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 2),
    _Gs2310PortEEEMode_Type()
)
gs2310PortEEEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEMode.setStatus("current")


class _Gs2310PortEEEUrgentQueue1_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue1 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue1_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue1_Object = MibTableColumn
gs2310PortEEEUrgentQueue1 = _Gs2310PortEEEUrgentQueue1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 3),
    _Gs2310PortEEEUrgentQueue1_Type()
)
gs2310PortEEEUrgentQueue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue1.setStatus("current")


class _Gs2310PortEEEUrgentQueue2_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue2 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue2_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue2_Object = MibTableColumn
gs2310PortEEEUrgentQueue2 = _Gs2310PortEEEUrgentQueue2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 4),
    _Gs2310PortEEEUrgentQueue2_Type()
)
gs2310PortEEEUrgentQueue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue2.setStatus("current")


class _Gs2310PortEEEUrgentQueue3_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue3 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue3_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue3_Object = MibTableColumn
gs2310PortEEEUrgentQueue3 = _Gs2310PortEEEUrgentQueue3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 5),
    _Gs2310PortEEEUrgentQueue3_Type()
)
gs2310PortEEEUrgentQueue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue3.setStatus("current")


class _Gs2310PortEEEUrgentQueue4_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue4 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue4_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue4_Object = MibTableColumn
gs2310PortEEEUrgentQueue4 = _Gs2310PortEEEUrgentQueue4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 6),
    _Gs2310PortEEEUrgentQueue4_Type()
)
gs2310PortEEEUrgentQueue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue4.setStatus("current")


class _Gs2310PortEEEUrgentQueue5_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue5 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue5_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue5_Object = MibTableColumn
gs2310PortEEEUrgentQueue5 = _Gs2310PortEEEUrgentQueue5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 7),
    _Gs2310PortEEEUrgentQueue5_Type()
)
gs2310PortEEEUrgentQueue5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue5.setStatus("current")


class _Gs2310PortEEEUrgentQueue6_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue6 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue6_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue6_Object = MibTableColumn
gs2310PortEEEUrgentQueue6 = _Gs2310PortEEEUrgentQueue6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 8),
    _Gs2310PortEEEUrgentQueue6_Type()
)
gs2310PortEEEUrgentQueue6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue6.setStatus("current")


class _Gs2310PortEEEUrgentQueue7_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue7 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue7_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue7_Object = MibTableColumn
gs2310PortEEEUrgentQueue7 = _Gs2310PortEEEUrgentQueue7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 9),
    _Gs2310PortEEEUrgentQueue7_Type()
)
gs2310PortEEEUrgentQueue7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue7.setStatus("current")


class _Gs2310PortEEEUrgentQueue8_Type(Integer32):
    """Custom type gs2310PortEEEUrgentQueue8 based on Integer32"""
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


_Gs2310PortEEEUrgentQueue8_Type.__name__ = "Integer32"
_Gs2310PortEEEUrgentQueue8_Object = MibTableColumn
gs2310PortEEEUrgentQueue8 = _Gs2310PortEEEUrgentQueue8_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1, 5, 1, 10),
    _Gs2310PortEEEUrgentQueue8_Type()
)
gs2310PortEEEUrgentQueue8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortEEEUrgentQueue8.setStatus("current")
_Gs2310VoiceVLAN_ObjectIdentity = ObjectIdentity
gs2310VoiceVLAN = _Gs2310VoiceVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2)
)
_Gs2310VoiceVLANConf_ObjectIdentity = ObjectIdentity
gs2310VoiceVLANConf = _Gs2310VoiceVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1)
)


class _Gs2310VoiceVLANMode_Type(Integer32):
    """Custom type gs2310VoiceVLANMode based on Integer32"""
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


_Gs2310VoiceVLANMode_Type.__name__ = "Integer32"
_Gs2310VoiceVLANMode_Object = MibScalar
gs2310VoiceVLANMode = _Gs2310VoiceVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 1),
    _Gs2310VoiceVLANMode_Type()
)
gs2310VoiceVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANMode.setStatus("current")


class _Gs2310VoiceVLANVLANId_Type(Integer32):
    """Custom type gs2310VoiceVLANVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310VoiceVLANVLANId_Type.__name__ = "Integer32"
_Gs2310VoiceVLANVLANId_Object = MibScalar
gs2310VoiceVLANVLANId = _Gs2310VoiceVLANVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 2),
    _Gs2310VoiceVLANVLANId_Type()
)
gs2310VoiceVLANVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANVLANId.setStatus("current")


class _Gs2310VoiceVLANAgingTime_Type(Integer32):
    """Custom type gs2310VoiceVLANAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2310VoiceVLANAgingTime_Type.__name__ = "Integer32"
_Gs2310VoiceVLANAgingTime_Object = MibScalar
gs2310VoiceVLANAgingTime = _Gs2310VoiceVLANAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 3),
    _Gs2310VoiceVLANAgingTime_Type()
)
gs2310VoiceVLANAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANAgingTime.setStatus("current")


class _Gs2310VoiceVLANTrafficClass_Type(Integer32):
    """Custom type gs2310VoiceVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310VoiceVLANTrafficClass_Type.__name__ = "Integer32"
_Gs2310VoiceVLANTrafficClass_Object = MibScalar
gs2310VoiceVLANTrafficClass = _Gs2310VoiceVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 4),
    _Gs2310VoiceVLANTrafficClass_Type()
)
gs2310VoiceVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANTrafficClass.setStatus("current")
_Gs2310VoiceVLANPortTable_Object = MibTable
gs2310VoiceVLANPortTable = _Gs2310VoiceVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2310VoiceVLANPortTable.setStatus("current")
_Gs2310VoiceVLANPortEntry_Object = MibTableRow
gs2310VoiceVLANPortEntry = _Gs2310VoiceVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5, 1)
)
gs2310VoiceVLANPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310VoiceVLANPort"),
)
if mibBuilder.loadTexts:
    gs2310VoiceVLANPortEntry.setStatus("current")


class _Gs2310VoiceVLANPort_Type(Integer32):
    """Custom type gs2310VoiceVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310VoiceVLANPort_Type.__name__ = "Integer32"
_Gs2310VoiceVLANPort_Object = MibTableColumn
gs2310VoiceVLANPort = _Gs2310VoiceVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5, 1, 1),
    _Gs2310VoiceVLANPort_Type()
)
gs2310VoiceVLANPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310VoiceVLANPort.setStatus("current")


class _Gs2310VoiceVLANPortMode_Type(Integer32):
    """Custom type gs2310VoiceVLANPortMode based on Integer32"""
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


_Gs2310VoiceVLANPortMode_Type.__name__ = "Integer32"
_Gs2310VoiceVLANPortMode_Object = MibTableColumn
gs2310VoiceVLANPortMode = _Gs2310VoiceVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5, 1, 2),
    _Gs2310VoiceVLANPortMode_Type()
)
gs2310VoiceVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANPortMode.setStatus("current")


class _Gs2310VoiceVLANPortSecurity_Type(Integer32):
    """Custom type gs2310VoiceVLANPortSecurity based on Integer32"""
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


_Gs2310VoiceVLANPortSecurity_Type.__name__ = "Integer32"
_Gs2310VoiceVLANPortSecurity_Object = MibTableColumn
gs2310VoiceVLANPortSecurity = _Gs2310VoiceVLANPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5, 1, 3),
    _Gs2310VoiceVLANPortSecurity_Type()
)
gs2310VoiceVLANPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANPortSecurity.setStatus("current")


class _Gs2310VoiceVLANPortDiscoveryProtocol_Type(Integer32):
    """Custom type gs2310VoiceVLANPortDiscoveryProtocol based on Integer32"""
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


_Gs2310VoiceVLANPortDiscoveryProtocol_Type.__name__ = "Integer32"
_Gs2310VoiceVLANPortDiscoveryProtocol_Object = MibTableColumn
gs2310VoiceVLANPortDiscoveryProtocol = _Gs2310VoiceVLANPortDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5, 1, 4),
    _Gs2310VoiceVLANPortDiscoveryProtocol_Type()
)
gs2310VoiceVLANPortDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANPortDiscoveryProtocol.setStatus("current")


class _Gs2310VoiceVLANSkipNAS_Type(Integer32):
    """Custom type gs2310VoiceVLANSkipNAS based on Integer32"""
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


_Gs2310VoiceVLANSkipNAS_Type.__name__ = "Integer32"
_Gs2310VoiceVLANSkipNAS_Object = MibScalar
gs2310VoiceVLANSkipNAS = _Gs2310VoiceVLANSkipNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 1, 5, 1, 5),
    _Gs2310VoiceVLANSkipNAS_Type()
)
gs2310VoiceVLANSkipNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANSkipNAS.setStatus("current")
_Gs2310VoiceVLANOUI_ObjectIdentity = ObjectIdentity
gs2310VoiceVLANOUI = _Gs2310VoiceVLANOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2)
)


class _Gs2310VoiceVLANOUICreate_Type(Integer32):
    """Custom type gs2310VoiceVLANOUICreate based on Integer32"""
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


_Gs2310VoiceVLANOUICreate_Type.__name__ = "Integer32"
_Gs2310VoiceVLANOUICreate_Object = MibScalar
gs2310VoiceVLANOUICreate = _Gs2310VoiceVLANOUICreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 1),
    _Gs2310VoiceVLANOUICreate_Type()
)
gs2310VoiceVLANOUICreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANOUICreate.setStatus("current")
_Gs2310VoiceVLANOUITable_Object = MibTable
gs2310VoiceVLANOUITable = _Gs2310VoiceVLANOUITable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310VoiceVLANOUITable.setStatus("current")
_Gs2310VoiceVLANOUIEntry_Object = MibTableRow
gs2310VoiceVLANOUIEntry = _Gs2310VoiceVLANOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 2, 1)
)
gs2310VoiceVLANOUIEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310VoiceVLANOUIIndex"),
)
if mibBuilder.loadTexts:
    gs2310VoiceVLANOUIEntry.setStatus("current")


class _Gs2310VoiceVLANOUIIndex_Type(Integer32):
    """Custom type gs2310VoiceVLANOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2310VoiceVLANOUIIndex_Type.__name__ = "Integer32"
_Gs2310VoiceVLANOUIIndex_Object = MibTableColumn
gs2310VoiceVLANOUIIndex = _Gs2310VoiceVLANOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 2, 1, 1),
    _Gs2310VoiceVLANOUIIndex_Type()
)
gs2310VoiceVLANOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310VoiceVLANOUIIndex.setStatus("current")


class _Gs2310VoiceVLANTelephonyOUI_Type(OctetString):
    """Custom type gs2310VoiceVLANTelephonyOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310VoiceVLANTelephonyOUI_Type.__name__ = "OctetString"
_Gs2310VoiceVLANTelephonyOUI_Object = MibTableColumn
gs2310VoiceVLANTelephonyOUI = _Gs2310VoiceVLANTelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 2, 1, 2),
    _Gs2310VoiceVLANTelephonyOUI_Type()
)
gs2310VoiceVLANTelephonyOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANTelephonyOUI.setStatus("current")


class _Gs2310VoiceVLANDescription_Type(DisplayString):
    """Custom type gs2310VoiceVLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310VoiceVLANDescription_Type.__name__ = "DisplayString"
_Gs2310VoiceVLANDescription_Object = MibTableColumn
gs2310VoiceVLANDescription = _Gs2310VoiceVLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 2, 1, 3),
    _Gs2310VoiceVLANDescription_Type()
)
gs2310VoiceVLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANDescription.setStatus("current")


class _Gs2310VoiceVLANOUIRowStatus_Type(Integer32):
    """Custom type gs2310VoiceVLANOUIRowStatus based on Integer32"""
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


_Gs2310VoiceVLANOUIRowStatus_Type.__name__ = "Integer32"
_Gs2310VoiceVLANOUIRowStatus_Object = MibTableColumn
gs2310VoiceVLANOUIRowStatus = _Gs2310VoiceVLANOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 2, 2, 2, 1, 4),
    _Gs2310VoiceVLANOUIRowStatus_Type()
)
gs2310VoiceVLANOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VoiceVLANOUIRowStatus.setStatus("current")
_Gs2310GARP_ObjectIdentity = ObjectIdentity
gs2310GARP = _Gs2310GARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3)
)
_Gs2310GARPConfTable_Object = MibTable
gs2310GARPConfTable = _Gs2310GARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gs2310GARPConfTable.setStatus("current")
_Gs2310GARPConfEntry_Object = MibTableRow
gs2310GARPConfEntry = _Gs2310GARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1)
)
gs2310GARPConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310GARPConfPort"),
)
if mibBuilder.loadTexts:
    gs2310GARPConfEntry.setStatus("current")


class _Gs2310GARPConfPort_Type(Integer32):
    """Custom type gs2310GARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310GARPConfPort_Type.__name__ = "Integer32"
_Gs2310GARPConfPort_Object = MibTableColumn
gs2310GARPConfPort = _Gs2310GARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 1),
    _Gs2310GARPConfPort_Type()
)
gs2310GARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310GARPConfPort.setStatus("current")


class _Gs2310GARPJoinTimer_Type(Integer32):
    """Custom type gs2310GARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Gs2310GARPJoinTimer_Type.__name__ = "Integer32"
_Gs2310GARPJoinTimer_Object = MibTableColumn
gs2310GARPJoinTimer = _Gs2310GARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 2),
    _Gs2310GARPJoinTimer_Type()
)
gs2310GARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPJoinTimer.setStatus("current")


class _Gs2310GARPLeaveTimer_Type(Integer32):
    """Custom type gs2310GARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Gs2310GARPLeaveTimer_Type.__name__ = "Integer32"
_Gs2310GARPLeaveTimer_Object = MibTableColumn
gs2310GARPLeaveTimer = _Gs2310GARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 3),
    _Gs2310GARPLeaveTimer_Type()
)
gs2310GARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPLeaveTimer.setStatus("current")


class _Gs2310GARPLeaveAllTimer_Type(Integer32):
    """Custom type gs2310GARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Gs2310GARPLeaveAllTimer_Type.__name__ = "Integer32"
_Gs2310GARPLeaveAllTimer_Object = MibTableColumn
gs2310GARPLeaveAllTimer = _Gs2310GARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 4),
    _Gs2310GARPLeaveAllTimer_Type()
)
gs2310GARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPLeaveAllTimer.setStatus("current")


class _Gs2310GARPApplicantion_Type(Integer32):
    """Custom type gs2310GARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gvrp", 1)
    )


_Gs2310GARPApplicantion_Type.__name__ = "Integer32"
_Gs2310GARPApplicantion_Object = MibTableColumn
gs2310GARPApplicantion = _Gs2310GARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 5),
    _Gs2310GARPApplicantion_Type()
)
gs2310GARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPApplicantion.setStatus("current")


class _Gs2310GARPAttributeType_Type(Integer32):
    """Custom type gs2310GARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_Gs2310GARPAttributeType_Type.__name__ = "Integer32"
_Gs2310GARPAttributeType_Object = MibTableColumn
gs2310GARPAttributeType = _Gs2310GARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 6),
    _Gs2310GARPAttributeType_Type()
)
gs2310GARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPAttributeType.setStatus("current")


class _Gs2310GARPApplicant_Type(Integer32):
    """Custom type gs2310GARPApplicant based on Integer32"""
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


_Gs2310GARPApplicant_Type.__name__ = "Integer32"
_Gs2310GARPApplicant_Object = MibTableColumn
gs2310GARPApplicant = _Gs2310GARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 1, 1, 7),
    _Gs2310GARPApplicant_Type()
)
gs2310GARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GARPApplicant.setStatus("current")
_Gs2310GARPStatisticsTable_Object = MibTable
gs2310GARPStatisticsTable = _Gs2310GARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310GARPStatisticsTable.setStatus("current")
_Gs2310GARPStatisticsEntry_Object = MibTableRow
gs2310GARPStatisticsEntry = _Gs2310GARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 2, 1)
)
gs2310GARPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310GARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2310GARPStatisticsEntry.setStatus("current")


class _Gs2310GARPStatisticsPort_Type(Integer32):
    """Custom type gs2310GARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310GARPStatisticsPort_Type.__name__ = "Integer32"
_Gs2310GARPStatisticsPort_Object = MibTableColumn
gs2310GARPStatisticsPort = _Gs2310GARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 2, 1, 1),
    _Gs2310GARPStatisticsPort_Type()
)
gs2310GARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310GARPStatisticsPort.setStatus("current")
_Gs2310GARPStatisticsPeerMAC_Type = DisplayString
_Gs2310GARPStatisticsPeerMAC_Object = MibTableColumn
gs2310GARPStatisticsPeerMAC = _Gs2310GARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 2, 1, 2),
    _Gs2310GARPStatisticsPeerMAC_Type()
)
gs2310GARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310GARPStatisticsPeerMAC.setStatus("current")
_Gs2310GARPStatisticsFailedCount_Type = Counter32
_Gs2310GARPStatisticsFailedCount_Object = MibTableColumn
gs2310GARPStatisticsFailedCount = _Gs2310GARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 3, 2, 1, 3),
    _Gs2310GARPStatisticsFailedCount_Type()
)
gs2310GARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310GARPStatisticsFailedCount.setStatus("current")
_Gs2310GVRP_ObjectIdentity = ObjectIdentity
gs2310GVRP = _Gs2310GVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4)
)
_Gs2310GVRPConf_ObjectIdentity = ObjectIdentity
gs2310GVRPConf = _Gs2310GVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1)
)


class _Gs2310GVRPMode_Type(Integer32):
    """Custom type gs2310GVRPMode based on Integer32"""
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


_Gs2310GVRPMode_Type.__name__ = "Integer32"
_Gs2310GVRPMode_Object = MibScalar
gs2310GVRPMode = _Gs2310GVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1, 1),
    _Gs2310GVRPMode_Type()
)
gs2310GVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GVRPMode.setStatus("current")
_Gs2310GVRPConfTable_Object = MibTable
gs2310GVRPConfTable = _Gs2310GVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310GVRPConfTable.setStatus("current")
_Gs2310GVRPConfEntry_Object = MibTableRow
gs2310GVRPConfEntry = _Gs2310GVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1, 2, 1)
)
gs2310GVRPConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310GVRPConfPort"),
)
if mibBuilder.loadTexts:
    gs2310GVRPConfEntry.setStatus("current")


class _Gs2310GVRPConfPort_Type(Integer32):
    """Custom type gs2310GVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310GVRPConfPort_Type.__name__ = "Integer32"
_Gs2310GVRPConfPort_Object = MibTableColumn
gs2310GVRPConfPort = _Gs2310GVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1, 2, 1, 1),
    _Gs2310GVRPConfPort_Type()
)
gs2310GVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310GVRPConfPort.setStatus("current")


class _Gs2310GVRPConfPortMode_Type(Integer32):
    """Custom type gs2310GVRPConfPortMode based on Integer32"""
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


_Gs2310GVRPConfPortMode_Type.__name__ = "Integer32"
_Gs2310GVRPConfPortMode_Object = MibTableColumn
gs2310GVRPConfPortMode = _Gs2310GVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1, 2, 1, 2),
    _Gs2310GVRPConfPortMode_Type()
)
gs2310GVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GVRPConfPortMode.setStatus("current")


class _Gs2310GVRPConfPortRRole_Type(Integer32):
    """Custom type gs2310GVRPConfPortRRole based on Integer32"""
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


_Gs2310GVRPConfPortRRole_Type.__name__ = "Integer32"
_Gs2310GVRPConfPortRRole_Object = MibTableColumn
gs2310GVRPConfPortRRole = _Gs2310GVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 1, 2, 1, 3),
    _Gs2310GVRPConfPortRRole_Type()
)
gs2310GVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310GVRPConfPortRRole.setStatus("current")
_Gs2310GVRPStatisticsTable_Object = MibTable
gs2310GVRPStatisticsTable = _Gs2310GVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310GVRPStatisticsTable.setStatus("current")
_Gs2310GVRPStatisticsEntry_Object = MibTableRow
gs2310GVRPStatisticsEntry = _Gs2310GVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 2, 1)
)
gs2310GVRPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310GVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2310GVRPStatisticsEntry.setStatus("current")


class _Gs2310GVRPStatisticsPort_Type(Integer32):
    """Custom type gs2310GVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310GVRPStatisticsPort_Type.__name__ = "Integer32"
_Gs2310GVRPStatisticsPort_Object = MibTableColumn
gs2310GVRPStatisticsPort = _Gs2310GVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 2, 1, 1),
    _Gs2310GVRPStatisticsPort_Type()
)
gs2310GVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310GVRPStatisticsPort.setStatus("current")
_Gs2310GVRPStatisticsJoinTxCnt_Type = Counter32
_Gs2310GVRPStatisticsJoinTxCnt_Object = MibTableColumn
gs2310GVRPStatisticsJoinTxCnt = _Gs2310GVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 2, 1, 2),
    _Gs2310GVRPStatisticsJoinTxCnt_Type()
)
gs2310GVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310GVRPStatisticsJoinTxCnt.setStatus("current")
_Gs2310GVRPStatisticsLeaveTxCnt_Type = Counter32
_Gs2310GVRPStatisticsLeaveTxCnt_Object = MibTableColumn
gs2310GVRPStatisticsLeaveTxCnt = _Gs2310GVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 4, 2, 1, 3),
    _Gs2310GVRPStatisticsLeaveTxCnt_Type()
)
gs2310GVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310GVRPStatisticsLeaveTxCnt.setStatus("current")
_Gs2310Mirroring_ObjectIdentity = ObjectIdentity
gs2310Mirroring = _Gs2310Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 6)
)


class _Gs2310PortToMirrorOn_Type(Integer32):
    """Custom type gs2310PortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2310PortToMirrorOn_Type.__name__ = "Integer32"
_Gs2310PortToMirrorOn_Object = MibScalar
gs2310PortToMirrorOn = _Gs2310PortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 6, 1),
    _Gs2310PortToMirrorOn_Type()
)
gs2310PortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortToMirrorOn.setStatus("current")
_Gs2310MirrorTable_Object = MibTable
gs2310MirrorTable = _Gs2310MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gs2310MirrorTable.setStatus("current")
_Gs2310MirrorEntry_Object = MibTableRow
gs2310MirrorEntry = _Gs2310MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 6, 2, 1)
)
gs2310MirrorEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MirrorPort"),
)
if mibBuilder.loadTexts:
    gs2310MirrorEntry.setStatus("current")


class _Gs2310MirrorPort_Type(Integer32):
    """Custom type gs2310MirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MirrorPort_Type.__name__ = "Integer32"
_Gs2310MirrorPort_Object = MibTableColumn
gs2310MirrorPort = _Gs2310MirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 6, 2, 1, 1),
    _Gs2310MirrorPort_Type()
)
gs2310MirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MirrorPort.setStatus("current")


class _Gs2310MirrorMode_Type(Integer32):
    """Custom type gs2310MirrorMode based on Integer32"""
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


_Gs2310MirrorMode_Type.__name__ = "Integer32"
_Gs2310MirrorMode_Object = MibTableColumn
gs2310MirrorMode = _Gs2310MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 6, 2, 1, 2),
    _Gs2310MirrorMode_Type()
)
gs2310MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MirrorMode.setStatus("current")
_Gs2310TrapEventSeverity_ObjectIdentity = ObjectIdentity
gs2310TrapEventSeverity = _Gs2310TrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7)
)


class _Gs2310TrapEventSeverityACL_Type(Integer32):
    """Custom type gs2310TrapEventSeverityACL based on Integer32"""
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


_Gs2310TrapEventSeverityACL_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityACL_Object = MibScalar
gs2310TrapEventSeverityACL = _Gs2310TrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 1),
    _Gs2310TrapEventSeverityACL_Type()
)
gs2310TrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityACL.setStatus("current")


class _Gs2310TrapEventSeverityACLLog_Type(Integer32):
    """Custom type gs2310TrapEventSeverityACLLog based on Integer32"""
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


_Gs2310TrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityACLLog_Object = MibScalar
gs2310TrapEventSeverityACLLog = _Gs2310TrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 2),
    _Gs2310TrapEventSeverityACLLog_Type()
)
gs2310TrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityACLLog.setStatus("current")


class _Gs2310TrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type gs2310TrapEventSeverityAccessMgmt based on Integer32"""
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


_Gs2310TrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityAccessMgmt_Object = MibScalar
gs2310TrapEventSeverityAccessMgmt = _Gs2310TrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 3),
    _Gs2310TrapEventSeverityAccessMgmt_Type()
)
gs2310TrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityAccessMgmt.setStatus("current")


class _Gs2310TrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type gs2310TrapEventSeverityAuthFailed based on Integer32"""
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


_Gs2310TrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityAuthFailed_Object = MibScalar
gs2310TrapEventSeverityAuthFailed = _Gs2310TrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 4),
    _Gs2310TrapEventSeverityAuthFailed_Type()
)
gs2310TrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityAuthFailed.setStatus("current")


class _Gs2310TrapEventSeverityColdStart_Type(Integer32):
    """Custom type gs2310TrapEventSeverityColdStart based on Integer32"""
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


_Gs2310TrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityColdStart_Object = MibScalar
gs2310TrapEventSeverityColdStart = _Gs2310TrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 5),
    _Gs2310TrapEventSeverityColdStart_Type()
)
gs2310TrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityColdStart.setStatus("current")


class _Gs2310TrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type gs2310TrapEventSeverityConfigInfo based on Integer32"""
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


_Gs2310TrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityConfigInfo_Object = MibScalar
gs2310TrapEventSeverityConfigInfo = _Gs2310TrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 6),
    _Gs2310TrapEventSeverityConfigInfo_Type()
)
gs2310TrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityConfigInfo.setStatus("current")


class _Gs2310TrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type gs2310TrapEventSeverityFirmwareUpgrade based on Integer32"""
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


_Gs2310TrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityFirmwareUpgrade_Object = MibScalar
gs2310TrapEventSeverityFirmwareUpgrade = _Gs2310TrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 7),
    _Gs2310TrapEventSeverityFirmwareUpgrade_Type()
)
gs2310TrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Gs2310TrapEventSeverityImportExport_Type(Integer32):
    """Custom type gs2310TrapEventSeverityImportExport based on Integer32"""
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


_Gs2310TrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityImportExport_Object = MibScalar
gs2310TrapEventSeverityImportExport = _Gs2310TrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 8),
    _Gs2310TrapEventSeverityImportExport_Type()
)
gs2310TrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityImportExport.setStatus("current")


class _Gs2310TrapEventSeverityLACP_Type(Integer32):
    """Custom type gs2310TrapEventSeverityLACP based on Integer32"""
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


_Gs2310TrapEventSeverityLACP_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityLACP_Object = MibScalar
gs2310TrapEventSeverityLACP = _Gs2310TrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 9),
    _Gs2310TrapEventSeverityLACP_Type()
)
gs2310TrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityLACP.setStatus("current")


class _Gs2310TrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type gs2310TrapEventSeverityLinkStatus based on Integer32"""
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


_Gs2310TrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityLinkStatus_Object = MibScalar
gs2310TrapEventSeverityLinkStatus = _Gs2310TrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 10),
    _Gs2310TrapEventSeverityLinkStatus_Type()
)
gs2310TrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityLinkStatus.setStatus("current")


class _Gs2310TrapEventSeverityLogin_Type(Integer32):
    """Custom type gs2310TrapEventSeverityLogin based on Integer32"""
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


_Gs2310TrapEventSeverityLogin_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityLogin_Object = MibScalar
gs2310TrapEventSeverityLogin = _Gs2310TrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 11),
    _Gs2310TrapEventSeverityLogin_Type()
)
gs2310TrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityLogin.setStatus("current")


class _Gs2310TrapEventSeverityLogout_Type(Integer32):
    """Custom type gs2310TrapEventSeverityLogout based on Integer32"""
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


_Gs2310TrapEventSeverityLogout_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityLogout_Object = MibScalar
gs2310TrapEventSeverityLogout = _Gs2310TrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 12),
    _Gs2310TrapEventSeverityLogout_Type()
)
gs2310TrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityLogout.setStatus("current")


class _Gs2310TrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type gs2310TrapEventSeverityLoopProtect based on Integer32"""
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


_Gs2310TrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityLoopProtect_Object = MibScalar
gs2310TrapEventSeverityLoopProtect = _Gs2310TrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 13),
    _Gs2310TrapEventSeverityLoopProtect_Type()
)
gs2310TrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityLoopProtect.setStatus("current")


class _Gs2310TrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type gs2310TrapEventSeverityMgmtIPChange based on Integer32"""
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


_Gs2310TrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityMgmtIPChange_Object = MibScalar
gs2310TrapEventSeverityMgmtIPChange = _Gs2310TrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 14),
    _Gs2310TrapEventSeverityMgmtIPChange_Type()
)
gs2310TrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityMgmtIPChange.setStatus("current")


class _Gs2310TrapEventSeverityModuleChange_Type(Integer32):
    """Custom type gs2310TrapEventSeverityModuleChange based on Integer32"""
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


_Gs2310TrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityModuleChange_Object = MibScalar
gs2310TrapEventSeverityModuleChange = _Gs2310TrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 15),
    _Gs2310TrapEventSeverityModuleChange_Type()
)
gs2310TrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityModuleChange.setStatus("current")


class _Gs2310TrapEventSeverityNAS_Type(Integer32):
    """Custom type gs2310TrapEventSeverityNAS based on Integer32"""
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


_Gs2310TrapEventSeverityNAS_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityNAS_Object = MibScalar
gs2310TrapEventSeverityNAS = _Gs2310TrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 16),
    _Gs2310TrapEventSeverityNAS_Type()
)
gs2310TrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityNAS.setStatus("current")


class _Gs2310TrapEventSeverityPasswordChange_Type(Integer32):
    """Custom type gs2310TrapEventSeverityPasswordChange based on Integer32"""
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


_Gs2310TrapEventSeverityPasswordChange_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityPasswordChange_Object = MibScalar
gs2310TrapEventSeverityPasswordChange = _Gs2310TrapEventSeverityPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 17),
    _Gs2310TrapEventSeverityPasswordChange_Type()
)
gs2310TrapEventSeverityPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityPasswordChange.setStatus("current")


class _Gs2310TrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type gs2310TrapEventSeverityPortSecurity based on Integer32"""
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


_Gs2310TrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityPortSecurity_Object = MibScalar
gs2310TrapEventSeverityPortSecurity = _Gs2310TrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 18),
    _Gs2310TrapEventSeverityPortSecurity_Type()
)
gs2310TrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityPortSecurity.setStatus("current")


class _Gs2310TrapEventSeverityVLAN_Type(Integer32):
    """Custom type gs2310TrapEventSeverityVLAN based on Integer32"""
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


_Gs2310TrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityVLAN_Object = MibScalar
gs2310TrapEventSeverityVLAN = _Gs2310TrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 20),
    _Gs2310TrapEventSeverityVLAN_Type()
)
gs2310TrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityVLAN.setStatus("current")


class _Gs2310TrapEventSeverityWarmStart_Type(Integer32):
    """Custom type gs2310TrapEventSeverityWarmStart based on Integer32"""
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


_Gs2310TrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityWarmStart_Object = MibScalar
gs2310TrapEventSeverityWarmStart = _Gs2310TrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 21),
    _Gs2310TrapEventSeverityWarmStart_Type()
)
gs2310TrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityWarmStart.setStatus("current")


class _Gs2310TrapEventSeverityARPConflict_Type(Integer32):
    """Custom type gs2310TrapEventSeverityARPConflict based on Integer32"""
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


_Gs2310TrapEventSeverityARPConflict_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityARPConflict_Object = MibScalar
gs2310TrapEventSeverityARPConflict = _Gs2310TrapEventSeverityARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 25),
    _Gs2310TrapEventSeverityARPConflict_Type()
)
gs2310TrapEventSeverityARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityARPConflict.setStatus("current")


class _Gs2310TrapEventSeveritySpoofingLimit_Type(Integer32):
    """Custom type gs2310TrapEventSeveritySpoofingLimit based on Integer32"""
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


_Gs2310TrapEventSeveritySpoofingLimit_Type.__name__ = "Integer32"
_Gs2310TrapEventSeveritySpoofingLimit_Object = MibScalar
gs2310TrapEventSeveritySpoofingLimit = _Gs2310TrapEventSeveritySpoofingLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 27),
    _Gs2310TrapEventSeveritySpoofingLimit_Type()
)
gs2310TrapEventSeveritySpoofingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeveritySpoofingLimit.setStatus("current")


class _Gs2310TrapEventSeverityStaticARPConflict_Type(Integer32):
    """Custom type gs2310TrapEventSeverityStaticARPConflict based on Integer32"""
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


_Gs2310TrapEventSeverityStaticARPConflict_Type.__name__ = "Integer32"
_Gs2310TrapEventSeverityStaticARPConflict_Object = MibScalar
gs2310TrapEventSeverityStaticARPConflict = _Gs2310TrapEventSeverityStaticARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 7, 28),
    _Gs2310TrapEventSeverityStaticARPConflict_Type()
)
gs2310TrapEventSeverityStaticARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TrapEventSeverityStaticARPConflict.setStatus("current")
_Gs2310SMTP_ObjectIdentity = ObjectIdentity
gs2310SMTP = _Gs2310SMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8)
)
_Gs2310SMTPMailServer_Type = DisplayString
_Gs2310SMTPMailServer_Object = MibScalar
gs2310SMTPMailServer = _Gs2310SMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 1),
    _Gs2310SMTPMailServer_Type()
)
gs2310SMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPMailServer.setStatus("current")
_Gs2310SMTPUserName_Type = DisplayString
_Gs2310SMTPUserName_Object = MibScalar
gs2310SMTPUserName = _Gs2310SMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 2),
    _Gs2310SMTPUserName_Type()
)
gs2310SMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPUserName.setStatus("current")
_Gs2310SMTPPassword_Type = DisplayString
_Gs2310SMTPPassword_Object = MibScalar
gs2310SMTPPassword = _Gs2310SMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 3),
    _Gs2310SMTPPassword_Type()
)
gs2310SMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPPassword.setStatus("current")


class _Gs2310SMTPServeriryLevel_Type(Integer32):
    """Custom type gs2310SMTPServeriryLevel based on Integer32"""
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


_Gs2310SMTPServeriryLevel_Type.__name__ = "Integer32"
_Gs2310SMTPServeriryLevel_Object = MibScalar
gs2310SMTPServeriryLevel = _Gs2310SMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 4),
    _Gs2310SMTPServeriryLevel_Type()
)
gs2310SMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPServeriryLevel.setStatus("current")
_Gs2310SMTPSender_Type = DisplayString
_Gs2310SMTPSender_Object = MibScalar
gs2310SMTPSender = _Gs2310SMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 5),
    _Gs2310SMTPSender_Type()
)
gs2310SMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPSender.setStatus("current")
_Gs2310SMTPReturnPath_Type = DisplayString
_Gs2310SMTPReturnPath_Object = MibScalar
gs2310SMTPReturnPath = _Gs2310SMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 6),
    _Gs2310SMTPReturnPath_Type()
)
gs2310SMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPReturnPath.setStatus("current")
_Gs2310SMTPEmailAddress1_Type = DisplayString
_Gs2310SMTPEmailAddress1_Object = MibScalar
gs2310SMTPEmailAddress1 = _Gs2310SMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 7),
    _Gs2310SMTPEmailAddress1_Type()
)
gs2310SMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPEmailAddress1.setStatus("current")
_Gs2310SMTPEmailAddress2_Type = DisplayString
_Gs2310SMTPEmailAddress2_Object = MibScalar
gs2310SMTPEmailAddress2 = _Gs2310SMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 8),
    _Gs2310SMTPEmailAddress2_Type()
)
gs2310SMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPEmailAddress2.setStatus("current")
_Gs2310SMTPEmailAddress3_Type = DisplayString
_Gs2310SMTPEmailAddress3_Object = MibScalar
gs2310SMTPEmailAddress3 = _Gs2310SMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 9),
    _Gs2310SMTPEmailAddress3_Type()
)
gs2310SMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPEmailAddress3.setStatus("current")
_Gs2310SMTPEmailAddress4_Type = DisplayString
_Gs2310SMTPEmailAddress4_Object = MibScalar
gs2310SMTPEmailAddress4 = _Gs2310SMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 10),
    _Gs2310SMTPEmailAddress4_Type()
)
gs2310SMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPEmailAddress4.setStatus("current")
_Gs2310SMTPEmailAddress5_Type = DisplayString
_Gs2310SMTPEmailAddress5_Object = MibScalar
gs2310SMTPEmailAddress5 = _Gs2310SMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 11),
    _Gs2310SMTPEmailAddress5_Type()
)
gs2310SMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPEmailAddress5.setStatus("current")
_Gs2310SMTPEmailAddress6_Type = DisplayString
_Gs2310SMTPEmailAddress6_Object = MibScalar
gs2310SMTPEmailAddress6 = _Gs2310SMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 8, 12),
    _Gs2310SMTPEmailAddress6_Type()
)
gs2310SMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SMTPEmailAddress6.setStatus("current")
_Gs2310ACL_ObjectIdentity = ObjectIdentity
gs2310ACL = _Gs2310ACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9)
)
_Gs2310ACLPortsConfTable_Object = MibTable
gs2310ACLPortsConfTable = _Gs2310ACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1)
)
if mibBuilder.loadTexts:
    gs2310ACLPortsConfTable.setStatus("current")
_Gs2310ACLPortsConfEntry_Object = MibTableRow
gs2310ACLPortsConfEntry = _Gs2310ACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1)
)
gs2310ACLPortsConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    gs2310ACLPortsConfEntry.setStatus("current")


class _Gs2310ACLPortsConfPort_Type(Integer32):
    """Custom type gs2310ACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ACLPortsConfPort_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfPort_Object = MibTableColumn
gs2310ACLPortsConfPort = _Gs2310ACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 1),
    _Gs2310ACLPortsConfPort_Type()
)
gs2310ACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfPort.setStatus("current")


class _Gs2310ACLPortsConfPolicyID_Type(Integer32):
    """Custom type gs2310ACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2310ACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfPolicyID_Object = MibTableColumn
gs2310ACLPortsConfPolicyID = _Gs2310ACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 2),
    _Gs2310ACLPortsConfPolicyID_Type()
)
gs2310ACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfPolicyID.setStatus("current")


class _Gs2310ACLPortsConfAction_Type(Integer32):
    """Custom type gs2310ACLPortsConfAction based on Integer32"""
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


_Gs2310ACLPortsConfAction_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfAction_Object = MibTableColumn
gs2310ACLPortsConfAction = _Gs2310ACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 3),
    _Gs2310ACLPortsConfAction_Type()
)
gs2310ACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfAction.setStatus("current")


class _Gs2310ACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type gs2310ACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2310ACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfRateLimiterID_Object = MibTableColumn
gs2310ACLPortsConfRateLimiterID = _Gs2310ACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 4),
    _Gs2310ACLPortsConfRateLimiterID_Type()
)
gs2310ACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfRateLimiterID.setStatus("current")


class _Gs2310ACLPortsConfPortRedirect_Type(Integer32):
    """Custom type gs2310ACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gs2310ACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfPortRedirect_Object = MibTableColumn
gs2310ACLPortsConfPortRedirect = _Gs2310ACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 5),
    _Gs2310ACLPortsConfPortRedirect_Type()
)
gs2310ACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfPortRedirect.setStatus("current")


class _Gs2310ACLPortsConfMirror_Type(Integer32):
    """Custom type gs2310ACLPortsConfMirror based on Integer32"""
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


_Gs2310ACLPortsConfMirror_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfMirror_Object = MibTableColumn
gs2310ACLPortsConfMirror = _Gs2310ACLPortsConfMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 6),
    _Gs2310ACLPortsConfMirror_Type()
)
gs2310ACLPortsConfMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfMirror.setStatus("current")


class _Gs2310ACLPortsConfLogging_Type(Integer32):
    """Custom type gs2310ACLPortsConfLogging based on Integer32"""
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


_Gs2310ACLPortsConfLogging_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfLogging_Object = MibTableColumn
gs2310ACLPortsConfLogging = _Gs2310ACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 7),
    _Gs2310ACLPortsConfLogging_Type()
)
gs2310ACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfLogging.setStatus("current")


class _Gs2310ACLPortsConfShutdown_Type(Integer32):
    """Custom type gs2310ACLPortsConfShutdown based on Integer32"""
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


_Gs2310ACLPortsConfShutdown_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfShutdown_Object = MibTableColumn
gs2310ACLPortsConfShutdown = _Gs2310ACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 8),
    _Gs2310ACLPortsConfShutdown_Type()
)
gs2310ACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfShutdown.setStatus("current")


class _Gs2310ACLPortsConfState_Type(Integer32):
    """Custom type gs2310ACLPortsConfState based on Integer32"""
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


_Gs2310ACLPortsConfState_Type.__name__ = "Integer32"
_Gs2310ACLPortsConfState_Object = MibTableColumn
gs2310ACLPortsConfState = _Gs2310ACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 9),
    _Gs2310ACLPortsConfState_Type()
)
gs2310ACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfState.setStatus("current")
_Gs2310ACLPortsConfCounter_Type = Counter32
_Gs2310ACLPortsConfCounter_Object = MibTableColumn
gs2310ACLPortsConfCounter = _Gs2310ACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 1, 1, 10),
    _Gs2310ACLPortsConfCounter_Type()
)
gs2310ACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLPortsConfCounter.setStatus("current")
_Gs2310ACLRateLimiterTable_Object = MibTable
gs2310ACLRateLimiterTable = _Gs2310ACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 2)
)
if mibBuilder.loadTexts:
    gs2310ACLRateLimiterTable.setStatus("current")
_Gs2310ACLRateLimiterEntry_Object = MibTableRow
gs2310ACLRateLimiterEntry = _Gs2310ACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 2, 1)
)
gs2310ACLRateLimiterEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    gs2310ACLRateLimiterEntry.setStatus("current")


class _Gs2310ACLRateLimiterID_Type(Integer32):
    """Custom type gs2310ACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2310ACLRateLimiterID_Type.__name__ = "Integer32"
_Gs2310ACLRateLimiterID_Object = MibTableColumn
gs2310ACLRateLimiterID = _Gs2310ACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 2, 1, 1),
    _Gs2310ACLRateLimiterID_Type()
)
gs2310ACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ACLRateLimiterID.setStatus("current")


class _Gs2310ACLRateLimiterUnit_Type(Integer32):
    """Custom type gs2310ACLRateLimiterUnit based on Integer32"""
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


_Gs2310ACLRateLimiterUnit_Type.__name__ = "Integer32"
_Gs2310ACLRateLimiterUnit_Object = MibTableColumn
gs2310ACLRateLimiterUnit = _Gs2310ACLRateLimiterUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 2, 1, 2),
    _Gs2310ACLRateLimiterUnit_Type()
)
gs2310ACLRateLimiterUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLRateLimiterUnit.setStatus("current")


class _Gs2310ACLRateLimiterRate_Type(Integer32):
    """Custom type gs2310ACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Gs2310ACLRateLimiterRate_Type.__name__ = "Integer32"
_Gs2310ACLRateLimiterRate_Object = MibTableColumn
gs2310ACLRateLimiterRate = _Gs2310ACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 2, 1, 3),
    _Gs2310ACLRateLimiterRate_Type()
)
gs2310ACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLRateLimiterRate.setStatus("current")
_Gs2310ACLACE_ObjectIdentity = ObjectIdentity
gs2310ACLACE = _Gs2310ACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3)
)


class _Gs2310ACLACECreate_Type(Integer32):
    """Custom type gs2310ACLACECreate based on Integer32"""
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


_Gs2310ACLACECreate_Type.__name__ = "Integer32"
_Gs2310ACLACECreate_Object = MibScalar
gs2310ACLACECreate = _Gs2310ACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 1),
    _Gs2310ACLACECreate_Type()
)
gs2310ACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACECreate.setStatus("current")
_Gs2310ACLACETable_Object = MibTable
gs2310ACLACETable = _Gs2310ACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310ACLACETable.setStatus("current")
_Gs2310ACLACEEntry_Object = MibTableRow
gs2310ACLACEEntry = _Gs2310ACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1)
)
gs2310ACLACEEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ACLACEIndex"),
)
if mibBuilder.loadTexts:
    gs2310ACLACEEntry.setStatus("current")


class _Gs2310ACLACEIndex_Type(Integer32):
    """Custom type gs2310ACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310ACLACEIndex_Type.__name__ = "Integer32"
_Gs2310ACLACEIndex_Object = MibTableColumn
gs2310ACLACEIndex = _Gs2310ACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 1),
    _Gs2310ACLACEIndex_Type()
)
gs2310ACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ACLACEIndex.setStatus("current")


class _Gs2310ACLACEID_Type(Integer32):
    """Custom type gs2310ACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310ACLACEID_Type.__name__ = "Integer32"
_Gs2310ACLACEID_Object = MibTableColumn
gs2310ACLACEID = _Gs2310ACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 2),
    _Gs2310ACLACEID_Type()
)
gs2310ACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEID.setStatus("current")


class _Gs2310ACLACENextID_Type(Integer32):
    """Custom type gs2310ACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2310ACLACENextID_Type.__name__ = "Integer32"
_Gs2310ACLACENextID_Object = MibTableColumn
gs2310ACLACENextID = _Gs2310ACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 3),
    _Gs2310ACLACENextID_Type()
)
gs2310ACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACENextID.setStatus("current")
_Gs2310ACLACEIngressPort_Type = DisplayString
_Gs2310ACLACEIngressPort_Object = MibTableColumn
gs2310ACLACEIngressPort = _Gs2310ACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 4),
    _Gs2310ACLACEIngressPort_Type()
)
gs2310ACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEIngressPort.setStatus("current")


class _Gs2310ACLACEPortPolicyNumber_Type(Integer32):
    """Custom type gs2310ACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2310ACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Gs2310ACLACEPortPolicyNumber_Object = MibTableColumn
gs2310ACLACEPortPolicyNumber = _Gs2310ACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 5),
    _Gs2310ACLACEPortPolicyNumber_Type()
)
gs2310ACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEPortPolicyNumber.setStatus("current")


class _Gs2310ACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type gs2310ACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2310ACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Gs2310ACLACEPortPolicyBitmask_Object = MibTableColumn
gs2310ACLACEPortPolicyBitmask = _Gs2310ACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 6),
    _Gs2310ACLACEPortPolicyBitmask_Type()
)
gs2310ACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEPortPolicyBitmask.setStatus("current")


class _Gs2310ACLACEFrameType_Type(Integer32):
    """Custom type gs2310ACLACEFrameType based on Integer32"""
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


_Gs2310ACLACEFrameType_Type.__name__ = "Integer32"
_Gs2310ACLACEFrameType_Object = MibTableColumn
gs2310ACLACEFrameType = _Gs2310ACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 7),
    _Gs2310ACLACEFrameType_Type()
)
gs2310ACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEFrameType.setStatus("current")


class _Gs2310ACLACEAction_Type(Integer32):
    """Custom type gs2310ACLACEAction based on Integer32"""
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


_Gs2310ACLACEAction_Type.__name__ = "Integer32"
_Gs2310ACLACEAction_Object = MibTableColumn
gs2310ACLACEAction = _Gs2310ACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 8),
    _Gs2310ACLACEAction_Type()
)
gs2310ACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEAction.setStatus("current")
_Gs2310ACLACEDenyPortRedirect_Type = DisplayString
_Gs2310ACLACEDenyPortRedirect_Object = MibTableColumn
gs2310ACLACEDenyPortRedirect = _Gs2310ACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 9),
    _Gs2310ACLACEDenyPortRedirect_Type()
)
gs2310ACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDenyPortRedirect.setStatus("current")


class _Gs2310ACLACELogging_Type(Integer32):
    """Custom type gs2310ACLACELogging based on Integer32"""
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


_Gs2310ACLACELogging_Type.__name__ = "Integer32"
_Gs2310ACLACELogging_Object = MibTableColumn
gs2310ACLACELogging = _Gs2310ACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 10),
    _Gs2310ACLACELogging_Type()
)
gs2310ACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACELogging.setStatus("current")


class _Gs2310ACLACEMirror_Type(Integer32):
    """Custom type gs2310ACLACEMirror based on Integer32"""
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


_Gs2310ACLACEMirror_Type.__name__ = "Integer32"
_Gs2310ACLACEMirror_Object = MibTableColumn
gs2310ACLACEMirror = _Gs2310ACLACEMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 11),
    _Gs2310ACLACEMirror_Type()
)
gs2310ACLACEMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEMirror.setStatus("current")


class _Gs2310ACLACERateLimiter_Type(Integer32):
    """Custom type gs2310ACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2310ACLACERateLimiter_Type.__name__ = "Integer32"
_Gs2310ACLACERateLimiter_Object = MibTableColumn
gs2310ACLACERateLimiter = _Gs2310ACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 12),
    _Gs2310ACLACERateLimiter_Type()
)
gs2310ACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACERateLimiter.setStatus("current")


class _Gs2310ACLACEShutdown_Type(Integer32):
    """Custom type gs2310ACLACEShutdown based on Integer32"""
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


_Gs2310ACLACEShutdown_Type.__name__ = "Integer32"
_Gs2310ACLACEShutdown_Object = MibTableColumn
gs2310ACLACEShutdown = _Gs2310ACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 13),
    _Gs2310ACLACEShutdown_Type()
)
gs2310ACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEShutdown.setStatus("current")


class _Gs2310ACLACEVLAN8021QTagged_Type(Integer32):
    """Custom type gs2310ACLACEVLAN8021QTagged based on Integer32"""
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


_Gs2310ACLACEVLAN8021QTagged_Type.__name__ = "Integer32"
_Gs2310ACLACEVLAN8021QTagged_Object = MibTableColumn
gs2310ACLACEVLAN8021QTagged = _Gs2310ACLACEVLAN8021QTagged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 14),
    _Gs2310ACLACEVLAN8021QTagged_Type()
)
gs2310ACLACEVLAN8021QTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEVLAN8021QTagged.setStatus("current")


class _Gs2310ACLACEVLANTagPriority_Type(Integer32):
    """Custom type gs2310ACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2310ACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Gs2310ACLACEVLANTagPriority_Object = MibTableColumn
gs2310ACLACEVLANTagPriority = _Gs2310ACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 15),
    _Gs2310ACLACEVLANTagPriority_Type()
)
gs2310ACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEVLANTagPriority.setStatus("current")


class _Gs2310ACLACEVLANVID_Type(Integer32):
    """Custom type gs2310ACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2310ACLACEVLANVID_Type.__name__ = "Integer32"
_Gs2310ACLACEVLANVID_Object = MibTableColumn
gs2310ACLACEVLANVID = _Gs2310ACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 16),
    _Gs2310ACLACEVLANVID_Type()
)
gs2310ACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEVLANVID.setStatus("current")


class _Gs2310ACLACEEtherType_Type(Integer32):
    """Custom type gs2310ACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2310ACLACEEtherType_Type.__name__ = "Integer32"
_Gs2310ACLACEEtherType_Object = MibTableColumn
gs2310ACLACEEtherType = _Gs2310ACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 17),
    _Gs2310ACLACEEtherType_Type()
)
gs2310ACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEEtherType.setStatus("current")
_Gs2310ACLACESMAC_Type = DisplayString
_Gs2310ACLACESMAC_Object = MibTableColumn
gs2310ACLACESMAC = _Gs2310ACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 18),
    _Gs2310ACLACESMAC_Type()
)
gs2310ACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACESMAC.setStatus("current")


class _Gs2310ACLACEDMACType_Type(Integer32):
    """Custom type gs2310ACLACEDMACType based on Integer32"""
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


_Gs2310ACLACEDMACType_Type.__name__ = "Integer32"
_Gs2310ACLACEDMACType_Object = MibTableColumn
gs2310ACLACEDMACType = _Gs2310ACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 19),
    _Gs2310ACLACEDMACType_Type()
)
gs2310ACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDMACType.setStatus("current")
_Gs2310ACLACEDMAC_Type = DisplayString
_Gs2310ACLACEDMAC_Object = MibTableColumn
gs2310ACLACEDMAC = _Gs2310ACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 20),
    _Gs2310ACLACEDMAC_Type()
)
gs2310ACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDMAC.setStatus("current")


class _Gs2310ACLACEArpOpcode_Type(Integer32):
    """Custom type gs2310ACLACEArpOpcode based on Integer32"""
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


_Gs2310ACLACEArpOpcode_Type.__name__ = "Integer32"
_Gs2310ACLACEArpOpcode_Object = MibTableColumn
gs2310ACLACEArpOpcode = _Gs2310ACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 21),
    _Gs2310ACLACEArpOpcode_Type()
)
gs2310ACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpOpcode.setStatus("current")


class _Gs2310ACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type gs2310ACLACEArpFlagsRequestReply based on Integer32"""
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


_Gs2310ACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Gs2310ACLACEArpFlagsRequestReply_Object = MibTableColumn
gs2310ACLACEArpFlagsRequestReply = _Gs2310ACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 22),
    _Gs2310ACLACEArpFlagsRequestReply_Type()
)
gs2310ACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpFlagsRequestReply.setStatus("current")


class _Gs2310ACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type gs2310ACLACEArpFlagsArpSmac based on Integer32"""
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


_Gs2310ACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Gs2310ACLACEArpFlagsArpSmac_Object = MibTableColumn
gs2310ACLACEArpFlagsArpSmac = _Gs2310ACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 23),
    _Gs2310ACLACEArpFlagsArpSmac_Type()
)
gs2310ACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpFlagsArpSmac.setStatus("current")


class _Gs2310ACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type gs2310ACLACEArpFlagsRarpDmac based on Integer32"""
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


_Gs2310ACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Gs2310ACLACEArpFlagsRarpDmac_Object = MibTableColumn
gs2310ACLACEArpFlagsRarpDmac = _Gs2310ACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 24),
    _Gs2310ACLACEArpFlagsRarpDmac_Type()
)
gs2310ACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpFlagsRarpDmac.setStatus("current")


class _Gs2310ACLACEArpFlagsLength_Type(Integer32):
    """Custom type gs2310ACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310ACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Gs2310ACLACEArpFlagsLength_Object = MibTableColumn
gs2310ACLACEArpFlagsLength = _Gs2310ACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 25),
    _Gs2310ACLACEArpFlagsLength_Type()
)
gs2310ACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpFlagsLength.setStatus("current")


class _Gs2310ACLACEArpFlagsIp_Type(Integer32):
    """Custom type gs2310ACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310ACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Gs2310ACLACEArpFlagsIp_Object = MibTableColumn
gs2310ACLACEArpFlagsIp = _Gs2310ACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 26),
    _Gs2310ACLACEArpFlagsIp_Type()
)
gs2310ACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpFlagsIp.setStatus("current")


class _Gs2310ACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type gs2310ACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310ACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Gs2310ACLACEArpFlagsEthernet_Object = MibTableColumn
gs2310ACLACEArpFlagsEthernet = _Gs2310ACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 27),
    _Gs2310ACLACEArpFlagsEthernet_Type()
)
gs2310ACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEArpFlagsEthernet.setStatus("current")


class _Gs2310ACLACESIPType_Type(Integer32):
    """Custom type gs2310ACLACESIPType based on Integer32"""
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


_Gs2310ACLACESIPType_Type.__name__ = "Integer32"
_Gs2310ACLACESIPType_Object = MibTableColumn
gs2310ACLACESIPType = _Gs2310ACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 28),
    _Gs2310ACLACESIPType_Type()
)
gs2310ACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACESIPType.setStatus("current")
_Gs2310ACLACESIPIPAddress_Type = IpAddress
_Gs2310ACLACESIPIPAddress_Object = MibTableColumn
gs2310ACLACESIPIPAddress = _Gs2310ACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 29),
    _Gs2310ACLACESIPIPAddress_Type()
)
gs2310ACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACESIPIPAddress.setStatus("current")


class _Gs2310ACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type gs2310ACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2310ACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2310ACLACESIPNetworkPrefix_Object = MibTableColumn
gs2310ACLACESIPNetworkPrefix = _Gs2310ACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 30),
    _Gs2310ACLACESIPNetworkPrefix_Type()
)
gs2310ACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACESIPNetworkPrefix.setStatus("current")


class _Gs2310ACLACEDIPType_Type(Integer32):
    """Custom type gs2310ACLACEDIPType based on Integer32"""
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


_Gs2310ACLACEDIPType_Type.__name__ = "Integer32"
_Gs2310ACLACEDIPType_Object = MibTableColumn
gs2310ACLACEDIPType = _Gs2310ACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 32),
    _Gs2310ACLACEDIPType_Type()
)
gs2310ACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDIPType.setStatus("current")
_Gs2310ACLACEDIPIPAddress_Type = IpAddress
_Gs2310ACLACEDIPIPAddress_Object = MibTableColumn
gs2310ACLACEDIPIPAddress = _Gs2310ACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 33),
    _Gs2310ACLACEDIPIPAddress_Type()
)
gs2310ACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDIPIPAddress.setStatus("current")


class _Gs2310ACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type gs2310ACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2310ACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2310ACLACEDIPNetworkPrefix_Object = MibTableColumn
gs2310ACLACEDIPNetworkPrefix = _Gs2310ACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 34),
    _Gs2310ACLACEDIPNetworkPrefix_Type()
)
gs2310ACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDIPNetworkPrefix.setStatus("current")


class _Gs2310ACLACEIPProtocol_Type(Integer32):
    """Custom type gs2310ACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2310ACLACEIPProtocol_Type.__name__ = "Integer32"
_Gs2310ACLACEIPProtocol_Object = MibTableColumn
gs2310ACLACEIPProtocol = _Gs2310ACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 36),
    _Gs2310ACLACEIPProtocol_Type()
)
gs2310ACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEIPProtocol.setStatus("current")


class _Gs2310ACLACEIPFlagsTTL_Type(Integer32):
    """Custom type gs2310ACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310ACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Gs2310ACLACEIPFlagsTTL_Object = MibTableColumn
gs2310ACLACEIPFlagsTTL = _Gs2310ACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 37),
    _Gs2310ACLACEIPFlagsTTL_Type()
)
gs2310ACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEIPFlagsTTL.setStatus("current")


class _Gs2310ACLACEIPFlagsOptions_Type(Integer32):
    """Custom type gs2310ACLACEIPFlagsOptions based on Integer32"""
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


_Gs2310ACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Gs2310ACLACEIPFlagsOptions_Object = MibTableColumn
gs2310ACLACEIPFlagsOptions = _Gs2310ACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 38),
    _Gs2310ACLACEIPFlagsOptions_Type()
)
gs2310ACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEIPFlagsOptions.setStatus("current")


class _Gs2310ACLACEIPFlagsFragment_Type(Integer32):
    """Custom type gs2310ACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310ACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Gs2310ACLACEIPFlagsFragment_Object = MibTableColumn
gs2310ACLACEIPFlagsFragment = _Gs2310ACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 39),
    _Gs2310ACLACEIPFlagsFragment_Type()
)
gs2310ACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEIPFlagsFragment.setStatus("current")


class _Gs2310ACLACEICMPType_Type(Integer32):
    """Custom type gs2310ACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2310ACLACEICMPType_Type.__name__ = "Integer32"
_Gs2310ACLACEICMPType_Object = MibTableColumn
gs2310ACLACEICMPType = _Gs2310ACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 40),
    _Gs2310ACLACEICMPType_Type()
)
gs2310ACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEICMPType.setStatus("current")


class _Gs2310ACLACEICMPCode_Type(Integer32):
    """Custom type gs2310ACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2310ACLACEICMPCode_Type.__name__ = "Integer32"
_Gs2310ACLACEICMPCode_Object = MibTableColumn
gs2310ACLACEICMPCode = _Gs2310ACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 41),
    _Gs2310ACLACEICMPCode_Type()
)
gs2310ACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEICMPCode.setStatus("current")


class _Gs2310ACLACESourcePortMin_Type(Integer32):
    """Custom type gs2310ACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2310ACLACESourcePortMin_Type.__name__ = "Integer32"
_Gs2310ACLACESourcePortMin_Object = MibTableColumn
gs2310ACLACESourcePortMin = _Gs2310ACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 42),
    _Gs2310ACLACESourcePortMin_Type()
)
gs2310ACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACESourcePortMin.setStatus("current")


class _Gs2310ACLACESourcePortMax_Type(Integer32):
    """Custom type gs2310ACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2310ACLACESourcePortMax_Type.__name__ = "Integer32"
_Gs2310ACLACESourcePortMax_Object = MibTableColumn
gs2310ACLACESourcePortMax = _Gs2310ACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 43),
    _Gs2310ACLACESourcePortMax_Type()
)
gs2310ACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACESourcePortMax.setStatus("current")


class _Gs2310ACLACEDestPortMin_Type(Integer32):
    """Custom type gs2310ACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2310ACLACEDestPortMin_Type.__name__ = "Integer32"
_Gs2310ACLACEDestPortMin_Object = MibTableColumn
gs2310ACLACEDestPortMin = _Gs2310ACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 44),
    _Gs2310ACLACEDestPortMin_Type()
)
gs2310ACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDestPortMin.setStatus("current")


class _Gs2310ACLACEDestPortMax_Type(Integer32):
    """Custom type gs2310ACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2310ACLACEDestPortMax_Type.__name__ = "Integer32"
_Gs2310ACLACEDestPortMax_Object = MibTableColumn
gs2310ACLACEDestPortMax = _Gs2310ACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 45),
    _Gs2310ACLACEDestPortMax_Type()
)
gs2310ACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEDestPortMax.setStatus("current")


class _Gs2310ACLACETCPFlagsFin_Type(Integer32):
    """Custom type gs2310ACLACETCPFlagsFin based on Integer32"""
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


_Gs2310ACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Gs2310ACLACETCPFlagsFin_Object = MibTableColumn
gs2310ACLACETCPFlagsFin = _Gs2310ACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 46),
    _Gs2310ACLACETCPFlagsFin_Type()
)
gs2310ACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACETCPFlagsFin.setStatus("current")


class _Gs2310ACLACETCPFlagsSyn_Type(Integer32):
    """Custom type gs2310ACLACETCPFlagsSyn based on Integer32"""
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


_Gs2310ACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Gs2310ACLACETCPFlagsSyn_Object = MibTableColumn
gs2310ACLACETCPFlagsSyn = _Gs2310ACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 47),
    _Gs2310ACLACETCPFlagsSyn_Type()
)
gs2310ACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACETCPFlagsSyn.setStatus("current")


class _Gs2310ACLACETCPFlagsRst_Type(Integer32):
    """Custom type gs2310ACLACETCPFlagsRst based on Integer32"""
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


_Gs2310ACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Gs2310ACLACETCPFlagsRst_Object = MibTableColumn
gs2310ACLACETCPFlagsRst = _Gs2310ACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 48),
    _Gs2310ACLACETCPFlagsRst_Type()
)
gs2310ACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACETCPFlagsRst.setStatus("current")


class _Gs2310ACLACETCPFlagsPsh_Type(Integer32):
    """Custom type gs2310ACLACETCPFlagsPsh based on Integer32"""
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


_Gs2310ACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Gs2310ACLACETCPFlagsPsh_Object = MibTableColumn
gs2310ACLACETCPFlagsPsh = _Gs2310ACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 49),
    _Gs2310ACLACETCPFlagsPsh_Type()
)
gs2310ACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACETCPFlagsPsh.setStatus("current")


class _Gs2310ACLACETCPFlagsAck_Type(Integer32):
    """Custom type gs2310ACLACETCPFlagsAck based on Integer32"""
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


_Gs2310ACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Gs2310ACLACETCPFlagsAck_Object = MibTableColumn
gs2310ACLACETCPFlagsAck = _Gs2310ACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 50),
    _Gs2310ACLACETCPFlagsAck_Type()
)
gs2310ACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACETCPFlagsAck.setStatus("current")


class _Gs2310ACLACETCPFlagsUrg_Type(Integer32):
    """Custom type gs2310ACLACETCPFlagsUrg based on Integer32"""
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


_Gs2310ACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Gs2310ACLACETCPFlagsUrg_Object = MibTableColumn
gs2310ACLACETCPFlagsUrg = _Gs2310ACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 51),
    _Gs2310ACLACETCPFlagsUrg_Type()
)
gs2310ACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACETCPFlagsUrg.setStatus("current")


class _Gs2310ACLACERowStatus_Type(Integer32):
    """Custom type gs2310ACLACERowStatus based on Integer32"""
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


_Gs2310ACLACERowStatus_Type.__name__ = "Integer32"
_Gs2310ACLACERowStatus_Object = MibTableColumn
gs2310ACLACERowStatus = _Gs2310ACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 2, 1, 66),
    _Gs2310ACLACERowStatus_Type()
)
gs2310ACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACERowStatus.setStatus("current")


class _Gs2310ACLACEClear_Type(Integer32):
    """Custom type gs2310ACLACEClear based on Integer32"""
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


_Gs2310ACLACEClear_Type.__name__ = "Integer32"
_Gs2310ACLACEClear_Object = MibScalar
gs2310ACLACEClear = _Gs2310ACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 3),
    _Gs2310ACLACEClear_Type()
)
gs2310ACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEClear.setStatus("current")


class _Gs2310ACLACEMoveACEID_Type(Integer32):
    """Custom type gs2310ACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2310ACLACEMoveACEID_Type.__name__ = "Integer32"
_Gs2310ACLACEMoveACEID_Object = MibScalar
gs2310ACLACEMoveACEID = _Gs2310ACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 4),
    _Gs2310ACLACEMoveACEID_Type()
)
gs2310ACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEMoveACEID.setStatus("current")


class _Gs2310ACLACEMoveNextACEID_Type(Integer32):
    """Custom type gs2310ACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2310ACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Gs2310ACLACEMoveNextACEID_Object = MibScalar
gs2310ACLACEMoveNextACEID = _Gs2310ACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 5),
    _Gs2310ACLACEMoveNextACEID_Type()
)
gs2310ACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ACLACEMoveNextACEID.setStatus("current")
_Gs2310ACLACEStatusTable_Object = MibTable
gs2310ACLACEStatusTable = _Gs2310ACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    gs2310ACLACEStatusTable.setStatus("current")
_Gs2310ACLACEStatusEntry_Object = MibTableRow
gs2310ACLACEStatusEntry = _Gs2310ACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1)
)
gs2310ACLACEStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2310ACLACEStatusEntry.setStatus("current")


class _Gs2310ACLACEStatusIndex_Type(Integer32):
    """Custom type gs2310ACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310ACLACEStatusIndex_Type.__name__ = "Integer32"
_Gs2310ACLACEStatusIndex_Object = MibTableColumn
gs2310ACLACEStatusIndex = _Gs2310ACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 1),
    _Gs2310ACLACEStatusIndex_Type()
)
gs2310ACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusIndex.setStatus("current")
_Gs2310ACLACEStatusUser_Type = DisplayString
_Gs2310ACLACEStatusUser_Object = MibTableColumn
gs2310ACLACEStatusUser = _Gs2310ACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 2),
    _Gs2310ACLACEStatusUser_Type()
)
gs2310ACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusUser.setStatus("current")


class _Gs2310ACLACEStatusID_Type(Integer32):
    """Custom type gs2310ACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310ACLACEStatusID_Type.__name__ = "Integer32"
_Gs2310ACLACEStatusID_Object = MibTableColumn
gs2310ACLACEStatusID = _Gs2310ACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 3),
    _Gs2310ACLACEStatusID_Type()
)
gs2310ACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusID.setStatus("current")
_Gs2310ACLACEStatusIngressPort_Type = DisplayString
_Gs2310ACLACEStatusIngressPort_Object = MibTableColumn
gs2310ACLACEStatusIngressPort = _Gs2310ACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 4),
    _Gs2310ACLACEStatusIngressPort_Type()
)
gs2310ACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusIngressPort.setStatus("current")
_Gs2310ACLACEStatusFrameType_Type = DisplayString
_Gs2310ACLACEStatusFrameType_Object = MibTableColumn
gs2310ACLACEStatusFrameType = _Gs2310ACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 5),
    _Gs2310ACLACEStatusFrameType_Type()
)
gs2310ACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusFrameType.setStatus("current")
_Gs2310ACLACEStatusAction_Type = DisplayString
_Gs2310ACLACEStatusAction_Object = MibTableColumn
gs2310ACLACEStatusAction = _Gs2310ACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 6),
    _Gs2310ACLACEStatusAction_Type()
)
gs2310ACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusAction.setStatus("current")
_Gs2310ACLACEStatusRateLimiter_Type = DisplayString
_Gs2310ACLACEStatusRateLimiter_Object = MibTableColumn
gs2310ACLACEStatusRateLimiter = _Gs2310ACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 7),
    _Gs2310ACLACEStatusRateLimiter_Type()
)
gs2310ACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusRateLimiter.setStatus("current")
_Gs2310ACLACEStatusPortCopy_Type = DisplayString
_Gs2310ACLACEStatusPortCopy_Object = MibTableColumn
gs2310ACLACEStatusPortCopy = _Gs2310ACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 8),
    _Gs2310ACLACEStatusPortCopy_Type()
)
gs2310ACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusPortCopy.setStatus("current")
_Gs2310ACLACEStatusMirror_Type = DisplayString
_Gs2310ACLACEStatusMirror_Object = MibTableColumn
gs2310ACLACEStatusMirror = _Gs2310ACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 9),
    _Gs2310ACLACEStatusMirror_Type()
)
gs2310ACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusMirror.setStatus("current")
_Gs2310ACLACEStatusCPU_Type = DisplayString
_Gs2310ACLACEStatusCPU_Object = MibTableColumn
gs2310ACLACEStatusCPU = _Gs2310ACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 10),
    _Gs2310ACLACEStatusCPU_Type()
)
gs2310ACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusCPU.setStatus("current")
_Gs2310ACLACEStatusCounter_Type = Counter32
_Gs2310ACLACEStatusCounter_Object = MibTableColumn
gs2310ACLACEStatusCounter = _Gs2310ACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 11),
    _Gs2310ACLACEStatusCounter_Type()
)
gs2310ACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusCounter.setStatus("current")
_Gs2310ACLACEStatusConflict_Type = DisplayString
_Gs2310ACLACEStatusConflict_Object = MibTableColumn
gs2310ACLACEStatusConflict = _Gs2310ACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 9, 3, 6, 1, 12),
    _Gs2310ACLACEStatusConflict_Type()
)
gs2310ACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ACLACEStatusConflict.setStatus("current")
_Gs2310LoopProtection_ObjectIdentity = ObjectIdentity
gs2310LoopProtection = _Gs2310LoopProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12)
)
_Gs2310LoopProtectionConfig_ObjectIdentity = ObjectIdentity
gs2310LoopProtectionConfig = _Gs2310LoopProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1)
)


class _Gs2310LoopProtectionGlobalEnable_Type(Integer32):
    """Custom type gs2310LoopProtectionGlobalEnable based on Integer32"""
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


_Gs2310LoopProtectionGlobalEnable_Type.__name__ = "Integer32"
_Gs2310LoopProtectionGlobalEnable_Object = MibScalar
gs2310LoopProtectionGlobalEnable = _Gs2310LoopProtectionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 1),
    _Gs2310LoopProtectionGlobalEnable_Type()
)
gs2310LoopProtectionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectionGlobalEnable.setStatus("current")


class _Gs2310LoopProtectionTranmisstionTime_Type(Integer32):
    """Custom type gs2310LoopProtectionTranmisstionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2310LoopProtectionTranmisstionTime_Type.__name__ = "Integer32"
_Gs2310LoopProtectionTranmisstionTime_Object = MibScalar
gs2310LoopProtectionTranmisstionTime = _Gs2310LoopProtectionTranmisstionTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 2),
    _Gs2310LoopProtectionTranmisstionTime_Type()
)
gs2310LoopProtectionTranmisstionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectionTranmisstionTime.setStatus("current")


class _Gs2310LoopProtectionShutdownTime_Type(Integer32):
    """Custom type gs2310LoopProtectionShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Gs2310LoopProtectionShutdownTime_Type.__name__ = "Integer32"
_Gs2310LoopProtectionShutdownTime_Object = MibScalar
gs2310LoopProtectionShutdownTime = _Gs2310LoopProtectionShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 3),
    _Gs2310LoopProtectionShutdownTime_Type()
)
gs2310LoopProtectionShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectionShutdownTime.setStatus("current")
_Gs2310LoopProtectionConfigurationTable_Object = MibTable
gs2310LoopProtectionConfigurationTable = _Gs2310LoopProtectionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    gs2310LoopProtectionConfigurationTable.setStatus("current")
_Gs2310LoopProtectionConfigurationEntry_Object = MibTableRow
gs2310LoopProtectionConfigurationEntry = _Gs2310LoopProtectionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 4, 1)
)
gs2310LoopProtectionConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310LoopProtectionConfPort"),
)
if mibBuilder.loadTexts:
    gs2310LoopProtectionConfigurationEntry.setStatus("current")


class _Gs2310LoopProtectionConfPort_Type(Integer32):
    """Custom type gs2310LoopProtectionConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310LoopProtectionConfPort_Type.__name__ = "Integer32"
_Gs2310LoopProtectionConfPort_Object = MibTableColumn
gs2310LoopProtectionConfPort = _Gs2310LoopProtectionConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 4, 1, 1),
    _Gs2310LoopProtectionConfPort_Type()
)
gs2310LoopProtectionConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310LoopProtectionConfPort.setStatus("current")


class _Gs2310LoopProtectionConfEnable_Type(Integer32):
    """Custom type gs2310LoopProtectionConfEnable based on Integer32"""
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


_Gs2310LoopProtectionConfEnable_Type.__name__ = "Integer32"
_Gs2310LoopProtectionConfEnable_Object = MibTableColumn
gs2310LoopProtectionConfEnable = _Gs2310LoopProtectionConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 4, 1, 2),
    _Gs2310LoopProtectionConfEnable_Type()
)
gs2310LoopProtectionConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectionConfEnable.setStatus("current")


class _Gs2310LoopProtectionConfAction_Type(Integer32):
    """Custom type gs2310LoopProtectionConfAction based on Integer32"""
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


_Gs2310LoopProtectionConfAction_Type.__name__ = "Integer32"
_Gs2310LoopProtectionConfAction_Object = MibTableColumn
gs2310LoopProtectionConfAction = _Gs2310LoopProtectionConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 4, 1, 3),
    _Gs2310LoopProtectionConfAction_Type()
)
gs2310LoopProtectionConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectionConfAction.setStatus("current")


class _Gs2310LoopProtectionConfTxmode_Type(Integer32):
    """Custom type gs2310LoopProtectionConfTxmode based on Integer32"""
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


_Gs2310LoopProtectionConfTxmode_Type.__name__ = "Integer32"
_Gs2310LoopProtectionConfTxmode_Object = MibTableColumn
gs2310LoopProtectionConfTxmode = _Gs2310LoopProtectionConfTxmode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 1, 4, 1, 4),
    _Gs2310LoopProtectionConfTxmode_Type()
)
gs2310LoopProtectionConfTxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoopProtectionConfTxmode.setStatus("current")
_Gs2310LoopProtectionStatusTable_Object = MibTable
gs2310LoopProtectionStatusTable = _Gs2310LoopProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2)
)
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusTable.setStatus("current")
_Gs2310LoopProtectionStatusEntry_Object = MibTableRow
gs2310LoopProtectionStatusEntry = _Gs2310LoopProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1)
)
gs2310LoopProtectionStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310LoopProtectionStatusPort"),
)
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusEntry.setStatus("current")


class _Gs2310LoopProtectionStatusPort_Type(Integer32):
    """Custom type gs2310LoopProtectionStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310LoopProtectionStatusPort_Type.__name__ = "Integer32"
_Gs2310LoopProtectionStatusPort_Object = MibTableColumn
gs2310LoopProtectionStatusPort = _Gs2310LoopProtectionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 1),
    _Gs2310LoopProtectionStatusPort_Type()
)
gs2310LoopProtectionStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusPort.setStatus("current")
_Gs2310LoopProtectionStatusAction_Type = DisplayString
_Gs2310LoopProtectionStatusAction_Object = MibTableColumn
gs2310LoopProtectionStatusAction = _Gs2310LoopProtectionStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 2),
    _Gs2310LoopProtectionStatusAction_Type()
)
gs2310LoopProtectionStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusAction.setStatus("current")
_Gs2310LoopProtectionStatusTransmit_Type = DisplayString
_Gs2310LoopProtectionStatusTransmit_Object = MibTableColumn
gs2310LoopProtectionStatusTransmit = _Gs2310LoopProtectionStatusTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 3),
    _Gs2310LoopProtectionStatusTransmit_Type()
)
gs2310LoopProtectionStatusTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusTransmit.setStatus("current")


class _Gs2310LoopProtectionStatusLoops_Type(Integer32):
    """Custom type gs2310LoopProtectionStatusLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2310LoopProtectionStatusLoops_Type.__name__ = "Integer32"
_Gs2310LoopProtectionStatusLoops_Object = MibTableColumn
gs2310LoopProtectionStatusLoops = _Gs2310LoopProtectionStatusLoops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 4),
    _Gs2310LoopProtectionStatusLoops_Type()
)
gs2310LoopProtectionStatusLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusLoops.setStatus("current")
_Gs2310LoopProtectionStatusStatus_Type = DisplayString
_Gs2310LoopProtectionStatusStatus_Object = MibTableColumn
gs2310LoopProtectionStatusStatus = _Gs2310LoopProtectionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 5),
    _Gs2310LoopProtectionStatusStatus_Type()
)
gs2310LoopProtectionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusStatus.setStatus("current")
_Gs2310LoopProtectionStatusLoop_Type = DisplayString
_Gs2310LoopProtectionStatusLoop_Object = MibTableColumn
gs2310LoopProtectionStatusLoop = _Gs2310LoopProtectionStatusLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 6),
    _Gs2310LoopProtectionStatusLoop_Type()
)
gs2310LoopProtectionStatusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusLoop.setStatus("current")
_Gs2310LoopProtectionStatusTimeLastLoop_Type = DisplayString
_Gs2310LoopProtectionStatusTimeLastLoop_Object = MibTableColumn
gs2310LoopProtectionStatusTimeLastLoop = _Gs2310LoopProtectionStatusTimeLastLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 12, 2, 1, 7),
    _Gs2310LoopProtectionStatusTimeLastLoop_Type()
)
gs2310LoopProtectionStatusTimeLastLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LoopProtectionStatusTimeLastLoop.setStatus("current")
_Gs2310Qos_ObjectIdentity = ObjectIdentity
gs2310Qos = _Gs2310Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14)
)
_Gs2310QosPortClassification_ObjectIdentity = ObjectIdentity
gs2310QosPortClassification = _Gs2310QosPortClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1)
)
_Gs2310QosPortClassificationTable_Object = MibTable
gs2310QosPortClassificationTable = _Gs2310QosPortClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    gs2310QosPortClassificationTable.setStatus("current")
_Gs2310QosPortClassificationEntry_Object = MibTableRow
gs2310QosPortClassificationEntry = _Gs2310QosPortClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1)
)
gs2310QosPortClassificationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosPortClassificationPort"),
)
if mibBuilder.loadTexts:
    gs2310QosPortClassificationEntry.setStatus("current")


class _Gs2310QosPortClassificationPort_Type(Integer32):
    """Custom type gs2310QosPortClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosPortClassificationPort_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationPort_Object = MibTableColumn
gs2310QosPortClassificationPort = _Gs2310QosPortClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 1),
    _Gs2310QosPortClassificationPort_Type()
)
gs2310QosPortClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationPort.setStatus("current")


class _Gs2310QosPortClassificationQoSclass_Type(Integer32):
    """Custom type gs2310QosPortClassificationQoSclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310QosPortClassificationQoSclass_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationQoSclass_Object = MibTableColumn
gs2310QosPortClassificationQoSclass = _Gs2310QosPortClassificationQoSclass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 2),
    _Gs2310QosPortClassificationQoSclass_Type()
)
gs2310QosPortClassificationQoSclass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationQoSclass.setStatus("current")


class _Gs2310QosPortClassificationDPlevel_Type(Integer32):
    """Custom type gs2310QosPortClassificationDPlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2310QosPortClassificationDPlevel_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationDPlevel_Object = MibTableColumn
gs2310QosPortClassificationDPlevel = _Gs2310QosPortClassificationDPlevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 3),
    _Gs2310QosPortClassificationDPlevel_Type()
)
gs2310QosPortClassificationDPlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationDPlevel.setStatus("current")


class _Gs2310QosPortClassificationPCP_Type(Integer32):
    """Custom type gs2310QosPortClassificationPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310QosPortClassificationPCP_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationPCP_Object = MibTableColumn
gs2310QosPortClassificationPCP = _Gs2310QosPortClassificationPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 4),
    _Gs2310QosPortClassificationPCP_Type()
)
gs2310QosPortClassificationPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationPCP.setStatus("current")


class _Gs2310QosPortClassificationDEI_Type(Integer32):
    """Custom type gs2310QosPortClassificationDEI based on Integer32"""
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


_Gs2310QosPortClassificationDEI_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationDEI_Object = MibTableColumn
gs2310QosPortClassificationDEI = _Gs2310QosPortClassificationDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 5),
    _Gs2310QosPortClassificationDEI_Type()
)
gs2310QosPortClassificationDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationDEI.setStatus("current")


class _Gs2310QosPortClassificationTagClass_Type(Integer32):
    """Custom type gs2310QosPortClassificationTagClass based on Integer32"""
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


_Gs2310QosPortClassificationTagClass_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationTagClass_Object = MibTableColumn
gs2310QosPortClassificationTagClass = _Gs2310QosPortClassificationTagClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 6),
    _Gs2310QosPortClassificationTagClass_Type()
)
gs2310QosPortClassificationTagClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationTagClass.setStatus("current")


class _Gs2310QosPortClassificationDSCPBased_Type(Integer32):
    """Custom type gs2310QosPortClassificationDSCPBased based on Integer32"""
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


_Gs2310QosPortClassificationDSCPBased_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationDSCPBased_Object = MibTableColumn
gs2310QosPortClassificationDSCPBased = _Gs2310QosPortClassificationDSCPBased_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 7),
    _Gs2310QosPortClassificationDSCPBased_Type()
)
gs2310QosPortClassificationDSCPBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationDSCPBased.setStatus("current")


class _Gs2310QosPortClassificationAddressMode_Type(Integer32):
    """Custom type gs2310QosPortClassificationAddressMode based on Integer32"""
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


_Gs2310QosPortClassificationAddressMode_Type.__name__ = "Integer32"
_Gs2310QosPortClassificationAddressMode_Object = MibTableColumn
gs2310QosPortClassificationAddressMode = _Gs2310QosPortClassificationAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 1, 1, 8),
    _Gs2310QosPortClassificationAddressMode_Type()
)
gs2310QosPortClassificationAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortClassificationAddressMode.setStatus("current")
_Gs2310QoSIngressPortTagClassificationTable_Object = MibTable
gs2310QoSIngressPortTagClassificationTable = _Gs2310QoSIngressPortTagClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagClassificationTable.setStatus("current")
_Gs2310QoSIngressPortTagClassificationEntry_Object = MibTableRow
gs2310QoSIngressPortTagClassificationEntry = _Gs2310QoSIngressPortTagClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2, 1)
)
gs2310QoSIngressPortTagClassificationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QoSIngressPortTagClassificationPort"),
    (0, "LANCOM-GS2310-MIB", "gs2310QoSIngressPortTagPCP"),
    (0, "LANCOM-GS2310-MIB", "gs2310QoSIngressPortTagDEI"),
)
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagClassificationEntry.setStatus("current")


class _Gs2310QoSIngressPortTagClassificationPort_Type(Integer32):
    """Custom type gs2310QoSIngressPortTagClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QoSIngressPortTagClassificationPort_Type.__name__ = "Integer32"
_Gs2310QoSIngressPortTagClassificationPort_Object = MibTableColumn
gs2310QoSIngressPortTagClassificationPort = _Gs2310QoSIngressPortTagClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2, 1, 1),
    _Gs2310QoSIngressPortTagClassificationPort_Type()
)
gs2310QoSIngressPortTagClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagClassificationPort.setStatus("current")


class _Gs2310QoSIngressPortTagPCP_Type(Integer32):
    """Custom type gs2310QoSIngressPortTagPCP based on Integer32"""
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


_Gs2310QoSIngressPortTagPCP_Type.__name__ = "Integer32"
_Gs2310QoSIngressPortTagPCP_Object = MibTableColumn
gs2310QoSIngressPortTagPCP = _Gs2310QoSIngressPortTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2, 1, 2),
    _Gs2310QoSIngressPortTagPCP_Type()
)
gs2310QoSIngressPortTagPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagPCP.setStatus("current")


class _Gs2310QoSIngressPortTagDEI_Type(Integer32):
    """Custom type gs2310QoSIngressPortTagDEI based on Integer32"""
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


_Gs2310QoSIngressPortTagDEI_Type.__name__ = "Integer32"
_Gs2310QoSIngressPortTagDEI_Object = MibTableColumn
gs2310QoSIngressPortTagDEI = _Gs2310QoSIngressPortTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2, 1, 3),
    _Gs2310QoSIngressPortTagDEI_Type()
)
gs2310QoSIngressPortTagDEI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagDEI.setStatus("current")


class _Gs2310QoSIngressPortTagQosClass_Type(Integer32):
    """Custom type gs2310QoSIngressPortTagQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310QoSIngressPortTagQosClass_Type.__name__ = "Integer32"
_Gs2310QoSIngressPortTagQosClass_Object = MibTableColumn
gs2310QoSIngressPortTagQosClass = _Gs2310QoSIngressPortTagQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2, 1, 4),
    _Gs2310QoSIngressPortTagQosClass_Type()
)
gs2310QoSIngressPortTagQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagQosClass.setStatus("current")


class _Gs2310QoSIngressPortTagDPLevel_Type(Integer32):
    """Custom type gs2310QoSIngressPortTagDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2310QoSIngressPortTagDPLevel_Type.__name__ = "Integer32"
_Gs2310QoSIngressPortTagDPLevel_Object = MibTableColumn
gs2310QoSIngressPortTagDPLevel = _Gs2310QoSIngressPortTagDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 1, 2, 1, 5),
    _Gs2310QoSIngressPortTagDPLevel_Type()
)
gs2310QoSIngressPortTagDPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSIngressPortTagDPLevel.setStatus("current")
_Gs2310QosPortPolicingTable_Object = MibTable
gs2310QosPortPolicingTable = _Gs2310QosPortPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gs2310QosPortPolicingTable.setStatus("current")
_Gs2310QosPortPolicingEntry_Object = MibTableRow
gs2310QosPortPolicingEntry = _Gs2310QosPortPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2, 1)
)
gs2310QosPortPolicingEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosPortPolicingPort"),
)
if mibBuilder.loadTexts:
    gs2310QosPortPolicingEntry.setStatus("current")


class _Gs2310QosPortPolicingPort_Type(Integer32):
    """Custom type gs2310QosPortPolicingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosPortPolicingPort_Type.__name__ = "Integer32"
_Gs2310QosPortPolicingPort_Object = MibTableColumn
gs2310QosPortPolicingPort = _Gs2310QosPortPolicingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2, 1, 1),
    _Gs2310QosPortPolicingPort_Type()
)
gs2310QosPortPolicingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosPortPolicingPort.setStatus("current")


class _Gs2310QosPortPolicingMode_Type(Integer32):
    """Custom type gs2310QosPortPolicingMode based on Integer32"""
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


_Gs2310QosPortPolicingMode_Type.__name__ = "Integer32"
_Gs2310QosPortPolicingMode_Object = MibTableColumn
gs2310QosPortPolicingMode = _Gs2310QosPortPolicingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2, 1, 2),
    _Gs2310QosPortPolicingMode_Type()
)
gs2310QosPortPolicingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortPolicingMode.setStatus("current")


class _Gs2310QosPortPolicingRate_Type(Integer32):
    """Custom type gs2310QosPortPolicingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2310QosPortPolicingRate_Type.__name__ = "Integer32"
_Gs2310QosPortPolicingRate_Object = MibTableColumn
gs2310QosPortPolicingRate = _Gs2310QosPortPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2, 1, 3),
    _Gs2310QosPortPolicingRate_Type()
)
gs2310QosPortPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortPolicingRate.setStatus("current")


class _Gs2310QosPortPolicingUnit_Type(Integer32):
    """Custom type gs2310QosPortPolicingUnit based on Integer32"""
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


_Gs2310QosPortPolicingUnit_Type.__name__ = "Integer32"
_Gs2310QosPortPolicingUnit_Object = MibTableColumn
gs2310QosPortPolicingUnit = _Gs2310QosPortPolicingUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2, 1, 4),
    _Gs2310QosPortPolicingUnit_Type()
)
gs2310QosPortPolicingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortPolicingUnit.setStatus("current")


class _Gs2310QosPortPolicingFlowControl_Type(Integer32):
    """Custom type gs2310QosPortPolicingFlowControl based on Integer32"""
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


_Gs2310QosPortPolicingFlowControl_Type.__name__ = "Integer32"
_Gs2310QosPortPolicingFlowControl_Object = MibTableColumn
gs2310QosPortPolicingFlowControl = _Gs2310QosPortPolicingFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 2, 1, 5),
    _Gs2310QosPortPolicingFlowControl_Type()
)
gs2310QosPortPolicingFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortPolicingFlowControl.setStatus("current")
_Gs2310QosPortScheduler_ObjectIdentity = ObjectIdentity
gs2310QosPortScheduler = _Gs2310QosPortScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3)
)
_Gs2310QosPortSchedulerModeTable_Object = MibTable
gs2310QosPortSchedulerModeTable = _Gs2310QosPortSchedulerModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    gs2310QosPortSchedulerModeTable.setStatus("current")
_Gs2310QosPortSchedulerModeEntry_Object = MibTableRow
gs2310QosPortSchedulerModeEntry = _Gs2310QosPortSchedulerModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 1, 1)
)
gs2310QosPortSchedulerModeEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosSchedulerModePort"),
)
if mibBuilder.loadTexts:
    gs2310QosPortSchedulerModeEntry.setStatus("current")


class _Gs2310QosSchedulerModePort_Type(Integer32):
    """Custom type gs2310QosSchedulerModePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosSchedulerModePort_Type.__name__ = "Integer32"
_Gs2310QosSchedulerModePort_Object = MibTableColumn
gs2310QosSchedulerModePort = _Gs2310QosSchedulerModePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 1, 1, 1),
    _Gs2310QosSchedulerModePort_Type()
)
gs2310QosSchedulerModePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosSchedulerModePort.setStatus("current")


class _Gs2310QosSchedulerMode_Type(Integer32):
    """Custom type gs2310QosSchedulerMode based on Integer32"""
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


_Gs2310QosSchedulerMode_Type.__name__ = "Integer32"
_Gs2310QosSchedulerMode_Object = MibTableColumn
gs2310QosSchedulerMode = _Gs2310QosSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 1, 1, 2),
    _Gs2310QosSchedulerMode_Type()
)
gs2310QosSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerMode.setStatus("current")


class _Gs2310QosSchedulerShaper_Type(Integer32):
    """Custom type gs2310QosSchedulerShaper based on Integer32"""
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


_Gs2310QosSchedulerShaper_Type.__name__ = "Integer32"
_Gs2310QosSchedulerShaper_Object = MibTableColumn
gs2310QosSchedulerShaper = _Gs2310QosSchedulerShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 1, 1, 3),
    _Gs2310QosSchedulerShaper_Type()
)
gs2310QosSchedulerShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerShaper.setStatus("current")


class _Gs2310QosSchedulerShaperRate_Type(Integer32):
    """Custom type gs2310QosSchedulerShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2310QosSchedulerShaperRate_Type.__name__ = "Integer32"
_Gs2310QosSchedulerShaperRate_Object = MibTableColumn
gs2310QosSchedulerShaperRate = _Gs2310QosSchedulerShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 1, 1, 4),
    _Gs2310QosSchedulerShaperRate_Type()
)
gs2310QosSchedulerShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerShaperRate.setStatus("current")
_Gs2310QosPortSchedulerTable_Object = MibTable
gs2310QosPortSchedulerTable = _Gs2310QosPortSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310QosPortSchedulerTable.setStatus("current")
_Gs2310QosPortSchedulerEntry_Object = MibTableRow
gs2310QosPortSchedulerEntry = _Gs2310QosPortSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1)
)
gs2310QosPortSchedulerEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosSchedulerPort"),
    (0, "LANCOM-GS2310-MIB", "gs2310QosSchedulerPortQueue"),
)
if mibBuilder.loadTexts:
    gs2310QosPortSchedulerEntry.setStatus("current")


class _Gs2310QosSchedulerPort_Type(Integer32):
    """Custom type gs2310QosSchedulerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosSchedulerPort_Type.__name__ = "Integer32"
_Gs2310QosSchedulerPort_Object = MibTableColumn
gs2310QosSchedulerPort = _Gs2310QosSchedulerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 1),
    _Gs2310QosSchedulerPort_Type()
)
gs2310QosSchedulerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPort.setStatus("current")


class _Gs2310QosSchedulerPortQueue_Type(Integer32):
    """Custom type gs2310QosSchedulerPortQueue based on Integer32"""
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


_Gs2310QosSchedulerPortQueue_Type.__name__ = "Integer32"
_Gs2310QosSchedulerPortQueue_Object = MibTableColumn
gs2310QosSchedulerPortQueue = _Gs2310QosSchedulerPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 2),
    _Gs2310QosSchedulerPortQueue_Type()
)
gs2310QosSchedulerPortQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPortQueue.setStatus("current")


class _Gs2310QosSchedulerPortQueueShaper_Type(Integer32):
    """Custom type gs2310QosSchedulerPortQueueShaper based on Integer32"""
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


_Gs2310QosSchedulerPortQueueShaper_Type.__name__ = "Integer32"
_Gs2310QosSchedulerPortQueueShaper_Object = MibTableColumn
gs2310QosSchedulerPortQueueShaper = _Gs2310QosSchedulerPortQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 3),
    _Gs2310QosSchedulerPortQueueShaper_Type()
)
gs2310QosSchedulerPortQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPortQueueShaper.setStatus("current")


class _Gs2310QosSchedulerPortQueueShaperRate_Type(Integer32):
    """Custom type gs2310QosSchedulerPortQueueShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2310QosSchedulerPortQueueShaperRate_Type.__name__ = "Integer32"
_Gs2310QosSchedulerPortQueueShaperRate_Object = MibTableColumn
gs2310QosSchedulerPortQueueShaperRate = _Gs2310QosSchedulerPortQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 4),
    _Gs2310QosSchedulerPortQueueShaperRate_Type()
)
gs2310QosSchedulerPortQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPortQueueShaperRate.setStatus("current")


class _Gs2310QosSchedulerPortQueueShaperExcess_Type(Integer32):
    """Custom type gs2310QosSchedulerPortQueueShaperExcess based on Integer32"""
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


_Gs2310QosSchedulerPortQueueShaperExcess_Type.__name__ = "Integer32"
_Gs2310QosSchedulerPortQueueShaperExcess_Object = MibTableColumn
gs2310QosSchedulerPortQueueShaperExcess = _Gs2310QosSchedulerPortQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 5),
    _Gs2310QosSchedulerPortQueueShaperExcess_Type()
)
gs2310QosSchedulerPortQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPortQueueShaperExcess.setStatus("current")


class _Gs2310QosSchedulerPortQueueSchedulerWeight_Type(Integer32):
    """Custom type gs2310QosSchedulerPortQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2310QosSchedulerPortQueueSchedulerWeight_Type.__name__ = "Integer32"
_Gs2310QosSchedulerPortQueueSchedulerWeight_Object = MibTableColumn
gs2310QosSchedulerPortQueueSchedulerWeight = _Gs2310QosSchedulerPortQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 6),
    _Gs2310QosSchedulerPortQueueSchedulerWeight_Type()
)
gs2310QosSchedulerPortQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPortQueueSchedulerWeight.setStatus("current")
_Gs2310QosSchedulerPortQueueSchedulerPercent_Type = DisplayString
_Gs2310QosSchedulerPortQueueSchedulerPercent_Object = MibTableColumn
gs2310QosSchedulerPortQueueSchedulerPercent = _Gs2310QosSchedulerPortQueueSchedulerPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 3, 2, 1, 7),
    _Gs2310QosSchedulerPortQueueSchedulerPercent_Type()
)
gs2310QosSchedulerPortQueueSchedulerPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosSchedulerPortQueueSchedulerPercent.setStatus("current")
_Gs2310QosPortEgressTagRemarking_ObjectIdentity = ObjectIdentity
gs2310QosPortEgressTagRemarking = _Gs2310QosPortEgressTagRemarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4)
)
_Gs2310QosPortEgressTagRemarkingTable_Object = MibTable
gs2310QosPortEgressTagRemarkingTable = _Gs2310QosPortEgressTagRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 1)
)
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingTable.setStatus("current")
_Gs2310QosPortEgressTagRemarkingEntry_Object = MibTableRow
gs2310QosPortEgressTagRemarkingEntry = _Gs2310QosPortEgressTagRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 1, 1)
)
gs2310QosPortEgressTagRemarkingEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosEgressTagRemarkingPort"),
)
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingEntry.setStatus("current")


class _Gs2310QosEgressTagRemarkingPort_Type(Integer32):
    """Custom type gs2310QosEgressTagRemarkingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosEgressTagRemarkingPort_Type.__name__ = "Integer32"
_Gs2310QosEgressTagRemarkingPort_Object = MibTableColumn
gs2310QosEgressTagRemarkingPort = _Gs2310QosEgressTagRemarkingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 1, 1, 1),
    _Gs2310QosEgressTagRemarkingPort_Type()
)
gs2310QosEgressTagRemarkingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosEgressTagRemarkingPort.setStatus("current")


class _Gs2310QosEgressTagRemarkingMode_Type(Integer32):
    """Custom type gs2310QosEgressTagRemarkingMode based on Integer32"""
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


_Gs2310QosEgressTagRemarkingMode_Type.__name__ = "Integer32"
_Gs2310QosEgressTagRemarkingMode_Object = MibTableColumn
gs2310QosEgressTagRemarkingMode = _Gs2310QosEgressTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 1, 1, 2),
    _Gs2310QosEgressTagRemarkingMode_Type()
)
gs2310QosEgressTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosEgressTagRemarkingMode.setStatus("current")
_Gs2310QosPortEgressTagRemarkingDefTable_Object = MibTable
gs2310QosPortEgressTagRemarkingDefTable = _Gs2310QosPortEgressTagRemarkingDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingDefTable.setStatus("current")
_Gs2310QosPortEgressTagRemarkingDefEntry_Object = MibTableRow
gs2310QosPortEgressTagRemarkingDefEntry = _Gs2310QosPortEgressTagRemarkingDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 2, 1)
)
gs2310QosPortEgressTagRemarkingDefEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosEgressTagRemarkingDefPort"),
)
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingDefEntry.setStatus("current")


class _Gs2310QosEgressTagRemarkingDefPort_Type(Integer32):
    """Custom type gs2310QosEgressTagRemarkingDefPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosEgressTagRemarkingDefPort_Type.__name__ = "Integer32"
_Gs2310QosEgressTagRemarkingDefPort_Object = MibTableColumn
gs2310QosEgressTagRemarkingDefPort = _Gs2310QosEgressTagRemarkingDefPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 2, 1, 1),
    _Gs2310QosEgressTagRemarkingDefPort_Type()
)
gs2310QosEgressTagRemarkingDefPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosEgressTagRemarkingDefPort.setStatus("current")


class _Gs2310QosEgressTagRemarkingDefPCP_Type(Integer32):
    """Custom type gs2310QosEgressTagRemarkingDefPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310QosEgressTagRemarkingDefPCP_Type.__name__ = "Integer32"
_Gs2310QosEgressTagRemarkingDefPCP_Object = MibTableColumn
gs2310QosEgressTagRemarkingDefPCP = _Gs2310QosEgressTagRemarkingDefPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 2, 1, 2),
    _Gs2310QosEgressTagRemarkingDefPCP_Type()
)
gs2310QosEgressTagRemarkingDefPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosEgressTagRemarkingDefPCP.setStatus("current")


class _Gs2310QosEgressTagRemarkingDefDEI_Type(Integer32):
    """Custom type gs2310QosEgressTagRemarkingDefDEI based on Integer32"""
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


_Gs2310QosEgressTagRemarkingDefDEI_Type.__name__ = "Integer32"
_Gs2310QosEgressTagRemarkingDefDEI_Object = MibTableColumn
gs2310QosEgressTagRemarkingDefDEI = _Gs2310QosEgressTagRemarkingDefDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 2, 1, 3),
    _Gs2310QosEgressTagRemarkingDefDEI_Type()
)
gs2310QosEgressTagRemarkingDefDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosEgressTagRemarkingDefDEI.setStatus("current")
_Gs2310QosPortEgressTagRemarkingMapTable_Object = MibTable
gs2310QosPortEgressTagRemarkingMapTable = _Gs2310QosPortEgressTagRemarkingMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingMapTable.setStatus("current")
_Gs2310QosPortEgressTagRemarkingMapEntry_Object = MibTableRow
gs2310QosPortEgressTagRemarkingMapEntry = _Gs2310QosPortEgressTagRemarkingMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4, 1)
)
gs2310QosPortEgressTagRemarkingMapEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosPortEgressTagRemarkingMapPort"),
    (0, "LANCOM-GS2310-MIB", "gs2310QosTagRemarkingQoSClass"),
    (0, "LANCOM-GS2310-MIB", "gs2310QosTagRemarkingDPLevel"),
)
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingMapEntry.setStatus("current")


class _Gs2310QosPortEgressTagRemarkingMapPort_Type(Integer32):
    """Custom type gs2310QosPortEgressTagRemarkingMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosPortEgressTagRemarkingMapPort_Type.__name__ = "Integer32"
_Gs2310QosPortEgressTagRemarkingMapPort_Object = MibTableColumn
gs2310QosPortEgressTagRemarkingMapPort = _Gs2310QosPortEgressTagRemarkingMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4, 1, 1),
    _Gs2310QosPortEgressTagRemarkingMapPort_Type()
)
gs2310QosPortEgressTagRemarkingMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosPortEgressTagRemarkingMapPort.setStatus("current")


class _Gs2310QosTagRemarkingQoSClass_Type(Integer32):
    """Custom type gs2310QosTagRemarkingQoSClass based on Integer32"""
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


_Gs2310QosTagRemarkingQoSClass_Type.__name__ = "Integer32"
_Gs2310QosTagRemarkingQoSClass_Object = MibTableColumn
gs2310QosTagRemarkingQoSClass = _Gs2310QosTagRemarkingQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4, 1, 2),
    _Gs2310QosTagRemarkingQoSClass_Type()
)
gs2310QosTagRemarkingQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosTagRemarkingQoSClass.setStatus("current")


class _Gs2310QosTagRemarkingDPLevel_Type(Integer32):
    """Custom type gs2310QosTagRemarkingDPLevel based on Integer32"""
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


_Gs2310QosTagRemarkingDPLevel_Type.__name__ = "Integer32"
_Gs2310QosTagRemarkingDPLevel_Object = MibTableColumn
gs2310QosTagRemarkingDPLevel = _Gs2310QosTagRemarkingDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4, 1, 3),
    _Gs2310QosTagRemarkingDPLevel_Type()
)
gs2310QosTagRemarkingDPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosTagRemarkingDPLevel.setStatus("current")


class _Gs2310QosTagRemarkingPCP_Type(Integer32):
    """Custom type gs2310QosTagRemarkingPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310QosTagRemarkingPCP_Type.__name__ = "Integer32"
_Gs2310QosTagRemarkingPCP_Object = MibTableColumn
gs2310QosTagRemarkingPCP = _Gs2310QosTagRemarkingPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4, 1, 4),
    _Gs2310QosTagRemarkingPCP_Type()
)
gs2310QosTagRemarkingPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosTagRemarkingPCP.setStatus("current")


class _Gs2310QosTagRemarkingDEI_Type(Integer32):
    """Custom type gs2310QosTagRemarkingDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2310QosTagRemarkingDEI_Type.__name__ = "Integer32"
_Gs2310QosTagRemarkingDEI_Object = MibTableColumn
gs2310QosTagRemarkingDEI = _Gs2310QosTagRemarkingDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 4, 4, 1, 5),
    _Gs2310QosTagRemarkingDEI_Type()
)
gs2310QosTagRemarkingDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosTagRemarkingDEI.setStatus("current")
_Gs2310QosPortDSCPTable_Object = MibTable
gs2310QosPortDSCPTable = _Gs2310QosPortDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 5)
)
if mibBuilder.loadTexts:
    gs2310QosPortDSCPTable.setStatus("current")
_Gs2310QosPortDSCPEntry_Object = MibTableRow
gs2310QosPortDSCPEntry = _Gs2310QosPortDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 5, 1)
)
gs2310QosPortDSCPEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosPortDSCPPort"),
)
if mibBuilder.loadTexts:
    gs2310QosPortDSCPEntry.setStatus("current")


class _Gs2310QosPortDSCPPort_Type(Integer32):
    """Custom type gs2310QosPortDSCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosPortDSCPPort_Type.__name__ = "Integer32"
_Gs2310QosPortDSCPPort_Object = MibTableColumn
gs2310QosPortDSCPPort = _Gs2310QosPortDSCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 5, 1, 1),
    _Gs2310QosPortDSCPPort_Type()
)
gs2310QosPortDSCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosPortDSCPPort.setStatus("current")


class _Gs2310QosPortDSCPIngressTranslate_Type(Integer32):
    """Custom type gs2310QosPortDSCPIngressTranslate based on Integer32"""
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


_Gs2310QosPortDSCPIngressTranslate_Type.__name__ = "Integer32"
_Gs2310QosPortDSCPIngressTranslate_Object = MibTableColumn
gs2310QosPortDSCPIngressTranslate = _Gs2310QosPortDSCPIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 5, 1, 2),
    _Gs2310QosPortDSCPIngressTranslate_Type()
)
gs2310QosPortDSCPIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortDSCPIngressTranslate.setStatus("current")


class _Gs2310QosPortDSCPIngressClassify_Type(Integer32):
    """Custom type gs2310QosPortDSCPIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310QosPortDSCPIngressClassify_Type.__name__ = "Integer32"
_Gs2310QosPortDSCPIngressClassify_Object = MibTableColumn
gs2310QosPortDSCPIngressClassify = _Gs2310QosPortDSCPIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 5, 1, 3),
    _Gs2310QosPortDSCPIngressClassify_Type()
)
gs2310QosPortDSCPIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortDSCPIngressClassify.setStatus("current")


class _Gs2310QosPortDSCPEgressRewrite_Type(Integer32):
    """Custom type gs2310QosPortDSCPEgressRewrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2310QosPortDSCPEgressRewrite_Type.__name__ = "Integer32"
_Gs2310QosPortDSCPEgressRewrite_Object = MibTableColumn
gs2310QosPortDSCPEgressRewrite = _Gs2310QosPortDSCPEgressRewrite_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 5, 1, 4),
    _Gs2310QosPortDSCPEgressRewrite_Type()
)
gs2310QosPortDSCPEgressRewrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPortDSCPEgressRewrite.setStatus("current")
_Gs2310QosDSCPTable_Object = MibTable
gs2310QosDSCPTable = _Gs2310QosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6)
)
if mibBuilder.loadTexts:
    gs2310QosDSCPTable.setStatus("current")
_Gs2310QosDSCPEntry_Object = MibTableRow
gs2310QosDSCPEntry = _Gs2310QosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6, 1)
)
gs2310QosDSCPEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosDSCPList"),
)
if mibBuilder.loadTexts:
    gs2310QosDSCPEntry.setStatus("current")


class _Gs2310QosDSCPList_Type(Integer32):
    """Custom type gs2310QosDSCPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2310QosDSCPList_Type.__name__ = "Integer32"
_Gs2310QosDSCPList_Object = MibTableColumn
gs2310QosDSCPList = _Gs2310QosDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6, 1, 1),
    _Gs2310QosDSCPList_Type()
)
gs2310QosDSCPList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosDSCPList.setStatus("current")
_Gs2310QosDSCP_Type = DisplayString
_Gs2310QosDSCP_Object = MibTableColumn
gs2310QosDSCP = _Gs2310QosDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6, 1, 2),
    _Gs2310QosDSCP_Type()
)
gs2310QosDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosDSCP.setStatus("current")


class _Gs2310QosDSCPTrust_Type(Integer32):
    """Custom type gs2310QosDSCPTrust based on Integer32"""
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


_Gs2310QosDSCPTrust_Type.__name__ = "Integer32"
_Gs2310QosDSCPTrust_Object = MibTableColumn
gs2310QosDSCPTrust = _Gs2310QosDSCPTrust_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6, 1, 3),
    _Gs2310QosDSCPTrust_Type()
)
gs2310QosDSCPTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPTrust.setStatus("current")


class _Gs2310QosDSCPQosClass_Type(Integer32):
    """Custom type gs2310QosDSCPQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2310QosDSCPQosClass_Type.__name__ = "Integer32"
_Gs2310QosDSCPQosClass_Object = MibTableColumn
gs2310QosDSCPQosClass = _Gs2310QosDSCPQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6, 1, 4),
    _Gs2310QosDSCPQosClass_Type()
)
gs2310QosDSCPQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPQosClass.setStatus("current")


class _Gs2310QosDSCPDPL_Type(Integer32):
    """Custom type gs2310QosDSCPDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2310QosDSCPDPL_Type.__name__ = "Integer32"
_Gs2310QosDSCPDPL_Object = MibTableColumn
gs2310QosDSCPDPL = _Gs2310QosDSCPDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 6, 1, 5),
    _Gs2310QosDSCPDPL_Type()
)
gs2310QosDSCPDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPDPL.setStatus("current")
_Gs2310QosDSCPTranslationTable_Object = MibTable
gs2310QosDSCPTranslationTable = _Gs2310QosDSCPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7)
)
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationTable.setStatus("current")
_Gs2310QosDSCPTranslationEntry_Object = MibTableRow
gs2310QosDSCPTranslationEntry = _Gs2310QosDSCPTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1)
)
gs2310QosDSCPTranslationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosDSCPTranslationList"),
)
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationEntry.setStatus("current")


class _Gs2310QosDSCPTranslationList_Type(Integer32):
    """Custom type gs2310QosDSCPTranslationList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2310QosDSCPTranslationList_Type.__name__ = "Integer32"
_Gs2310QosDSCPTranslationList_Object = MibTableColumn
gs2310QosDSCPTranslationList = _Gs2310QosDSCPTranslationList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1, 1),
    _Gs2310QosDSCPTranslationList_Type()
)
gs2310QosDSCPTranslationList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationList.setStatus("current")
_Gs2310QosDSCPTranslationDSCPBasedId_Type = DisplayString
_Gs2310QosDSCPTranslationDSCPBasedId_Object = MibTableColumn
gs2310QosDSCPTranslationDSCPBasedId = _Gs2310QosDSCPTranslationDSCPBasedId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1, 2),
    _Gs2310QosDSCPTranslationDSCPBasedId_Type()
)
gs2310QosDSCPTranslationDSCPBasedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationDSCPBasedId.setStatus("current")


class _Gs2310QosDSCPTranslationIngressTranslate_Type(Integer32):
    """Custom type gs2310QosDSCPTranslationIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2310QosDSCPTranslationIngressTranslate_Type.__name__ = "Integer32"
_Gs2310QosDSCPTranslationIngressTranslate_Object = MibTableColumn
gs2310QosDSCPTranslationIngressTranslate = _Gs2310QosDSCPTranslationIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1, 3),
    _Gs2310QosDSCPTranslationIngressTranslate_Type()
)
gs2310QosDSCPTranslationIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationIngressTranslate.setStatus("current")


class _Gs2310QosDSCPTranslationIngressClassify_Type(Integer32):
    """Custom type gs2310QosDSCPTranslationIngressClassify based on Integer32"""
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


_Gs2310QosDSCPTranslationIngressClassify_Type.__name__ = "Integer32"
_Gs2310QosDSCPTranslationIngressClassify_Object = MibTableColumn
gs2310QosDSCPTranslationIngressClassify = _Gs2310QosDSCPTranslationIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1, 4),
    _Gs2310QosDSCPTranslationIngressClassify_Type()
)
gs2310QosDSCPTranslationIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationIngressClassify.setStatus("current")


class _Gs2310QosDSCPTranslationEgressRemapDP0_Type(Integer32):
    """Custom type gs2310QosDSCPTranslationEgressRemapDP0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2310QosDSCPTranslationEgressRemapDP0_Type.__name__ = "Integer32"
_Gs2310QosDSCPTranslationEgressRemapDP0_Object = MibTableColumn
gs2310QosDSCPTranslationEgressRemapDP0 = _Gs2310QosDSCPTranslationEgressRemapDP0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1, 5),
    _Gs2310QosDSCPTranslationEgressRemapDP0_Type()
)
gs2310QosDSCPTranslationEgressRemapDP0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationEgressRemapDP0.setStatus("current")


class _Gs2310QosDSCPTranslationEgressRemapDP1_Type(Integer32):
    """Custom type gs2310QosDSCPTranslationEgressRemapDP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2310QosDSCPTranslationEgressRemapDP1_Type.__name__ = "Integer32"
_Gs2310QosDSCPTranslationEgressRemapDP1_Object = MibTableColumn
gs2310QosDSCPTranslationEgressRemapDP1 = _Gs2310QosDSCPTranslationEgressRemapDP1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 7, 1, 6),
    _Gs2310QosDSCPTranslationEgressRemapDP1_Type()
)
gs2310QosDSCPTranslationEgressRemapDP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPTranslationEgressRemapDP1.setStatus("current")
_Gs2310QosDSCPClassificationTable_Object = MibTable
gs2310QosDSCPClassificationTable = _Gs2310QosDSCPClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 8)
)
if mibBuilder.loadTexts:
    gs2310QosDSCPClassificationTable.setStatus("current")
_Gs2310QosDSCPClassificationEntry_Object = MibTableRow
gs2310QosDSCPClassificationEntry = _Gs2310QosDSCPClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 8, 1)
)
gs2310QosDSCPClassificationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosDSCPClassificationQoSClass"),
    (0, "LANCOM-GS2310-MIB", "gs2310QosDSCPClassificationDPL"),
)
if mibBuilder.loadTexts:
    gs2310QosDSCPClassificationEntry.setStatus("current")


class _Gs2310QosDSCPClassificationQoSClass_Type(Integer32):
    """Custom type gs2310QosDSCPClassificationQoSClass based on Integer32"""
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


_Gs2310QosDSCPClassificationQoSClass_Type.__name__ = "Integer32"
_Gs2310QosDSCPClassificationQoSClass_Object = MibTableColumn
gs2310QosDSCPClassificationQoSClass = _Gs2310QosDSCPClassificationQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 8, 1, 1),
    _Gs2310QosDSCPClassificationQoSClass_Type()
)
gs2310QosDSCPClassificationQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosDSCPClassificationQoSClass.setStatus("current")


class _Gs2310QosDSCPClassificationDPL_Type(Integer32):
    """Custom type gs2310QosDSCPClassificationDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2310QosDSCPClassificationDPL_Type.__name__ = "Integer32"
_Gs2310QosDSCPClassificationDPL_Object = MibTableColumn
gs2310QosDSCPClassificationDPL = _Gs2310QosDSCPClassificationDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 8, 1, 2),
    _Gs2310QosDSCPClassificationDPL_Type()
)
gs2310QosDSCPClassificationDPL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosDSCPClassificationDPL.setStatus("current")


class _Gs2310QosDSCPClassificationDSCP_Type(Integer32):
    """Custom type gs2310QosDSCPClassificationDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2310QosDSCPClassificationDSCP_Type.__name__ = "Integer32"
_Gs2310QosDSCPClassificationDSCP_Object = MibTableColumn
gs2310QosDSCPClassificationDSCP = _Gs2310QosDSCPClassificationDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 8, 1, 3),
    _Gs2310QosDSCPClassificationDSCP_Type()
)
gs2310QosDSCPClassificationDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDSCPClassificationDSCP.setStatus("current")
_Gs2310QosControlList_ObjectIdentity = ObjectIdentity
gs2310QosControlList = _Gs2310QosControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9)
)


class _Gs2310QosQceCreate_Type(Integer32):
    """Custom type gs2310QosQceCreate based on Integer32"""
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


_Gs2310QosQceCreate_Type.__name__ = "Integer32"
_Gs2310QosQceCreate_Object = MibScalar
gs2310QosQceCreate = _Gs2310QosQceCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 1),
    _Gs2310QosQceCreate_Type()
)
gs2310QosQceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceCreate.setStatus("current")
_Gs2310QosQceTable_Object = MibTable
gs2310QosQceTable = _Gs2310QosQceTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2)
)
if mibBuilder.loadTexts:
    gs2310QosQceTable.setStatus("current")
_Gs2310QosQceEntry_Object = MibTableRow
gs2310QosQceEntry = _Gs2310QosQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1)
)
gs2310QosQceEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosQceIndex"),
)
if mibBuilder.loadTexts:
    gs2310QosQceEntry.setStatus("current")


class _Gs2310QosQceIndex_Type(Integer32):
    """Custom type gs2310QosQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310QosQceIndex_Type.__name__ = "Integer32"
_Gs2310QosQceIndex_Object = MibTableColumn
gs2310QosQceIndex = _Gs2310QosQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 1),
    _Gs2310QosQceIndex_Type()
)
gs2310QosQceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosQceIndex.setStatus("current")


class _Gs2310QosQceID_Type(Integer32):
    """Custom type gs2310QosQceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310QosQceID_Type.__name__ = "Integer32"
_Gs2310QosQceID_Object = MibTableColumn
gs2310QosQceID = _Gs2310QosQceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 2),
    _Gs2310QosQceID_Type()
)
gs2310QosQceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceID.setStatus("current")


class _Gs2310QosQceNextID_Type(Integer32):
    """Custom type gs2310QosQceNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310QosQceNextID_Type.__name__ = "Integer32"
_Gs2310QosQceNextID_Object = MibTableColumn
gs2310QosQceNextID = _Gs2310QosQceNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 3),
    _Gs2310QosQceNextID_Type()
)
gs2310QosQceNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceNextID.setStatus("current")
_Gs2310QosQcePortMembers_Type = DisplayString
_Gs2310QosQcePortMembers_Object = MibTableColumn
gs2310QosQcePortMembers = _Gs2310QosQcePortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 4),
    _Gs2310QosQcePortMembers_Type()
)
gs2310QosQcePortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQcePortMembers.setStatus("current")
_Gs2310QosQceTag_Type = DisplayString
_Gs2310QosQceTag_Object = MibTableColumn
gs2310QosQceTag = _Gs2310QosQceTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 5),
    _Gs2310QosQceTag_Type()
)
gs2310QosQceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceTag.setStatus("current")
_Gs2310QosQceVID_Type = DisplayString
_Gs2310QosQceVID_Object = MibTableColumn
gs2310QosQceVID = _Gs2310QosQceVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 6),
    _Gs2310QosQceVID_Type()
)
gs2310QosQceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceVID.setStatus("current")
_Gs2310QosPCP_Type = DisplayString
_Gs2310QosPCP_Object = MibTableColumn
gs2310QosPCP = _Gs2310QosPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 7),
    _Gs2310QosPCP_Type()
)
gs2310QosPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosPCP.setStatus("current")
_Gs2310QosDEI_Type = DisplayString
_Gs2310QosDEI_Object = MibTableColumn
gs2310QosDEI = _Gs2310QosDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 8),
    _Gs2310QosDEI_Type()
)
gs2310QosDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDEI.setStatus("current")
_Gs2310QosSMAC_Type = DisplayString
_Gs2310QosSMAC_Object = MibTableColumn
gs2310QosSMAC = _Gs2310QosSMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 9),
    _Gs2310QosSMAC_Type()
)
gs2310QosSMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSMAC.setStatus("current")
_Gs2310QosDMACType_Type = DisplayString
_Gs2310QosDMACType_Object = MibTableColumn
gs2310QosDMACType = _Gs2310QosDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 10),
    _Gs2310QosDMACType_Type()
)
gs2310QosDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosDMACType.setStatus("current")


class _Gs2310QosFrameType_Type(Integer32):
    """Custom type gs2310QosFrameType based on Integer32"""
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


_Gs2310QosFrameType_Type.__name__ = "Integer32"
_Gs2310QosFrameType_Object = MibTableColumn
gs2310QosFrameType = _Gs2310QosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 11),
    _Gs2310QosFrameType_Type()
)
gs2310QosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosFrameType.setStatus("current")
_Gs2310QosMacEtherType_Type = DisplayString
_Gs2310QosMacEtherType_Object = MibTableColumn
gs2310QosMacEtherType = _Gs2310QosMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 12),
    _Gs2310QosMacEtherType_Type()
)
gs2310QosMacEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosMacEtherType.setStatus("current")
_Gs2310QosLLCSSAPAddr_Type = DisplayString
_Gs2310QosLLCSSAPAddr_Object = MibTableColumn
gs2310QosLLCSSAPAddr = _Gs2310QosLLCSSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 13),
    _Gs2310QosLLCSSAPAddr_Type()
)
gs2310QosLLCSSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosLLCSSAPAddr.setStatus("current")
_Gs2310QosLLCDSAPAddr_Type = DisplayString
_Gs2310QosLLCDSAPAddr_Object = MibTableColumn
gs2310QosLLCDSAPAddr = _Gs2310QosLLCDSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 14),
    _Gs2310QosLLCDSAPAddr_Type()
)
gs2310QosLLCDSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosLLCDSAPAddr.setStatus("current")
_Gs2310QosLLCControl_Type = DisplayString
_Gs2310QosLLCControl_Object = MibTableColumn
gs2310QosLLCControl = _Gs2310QosLLCControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 15),
    _Gs2310QosLLCControl_Type()
)
gs2310QosLLCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosLLCControl.setStatus("current")
_Gs2310QosSNAPPID_Type = DisplayString
_Gs2310QosSNAPPID_Object = MibTableColumn
gs2310QosSNAPPID = _Gs2310QosSNAPPID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 16),
    _Gs2310QosSNAPPID_Type()
)
gs2310QosSNAPPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosSNAPPID.setStatus("current")
_Gs2310QosIpv4Protocol_Type = DisplayString
_Gs2310QosIpv4Protocol_Object = MibTableColumn
gs2310QosIpv4Protocol = _Gs2310QosIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 17),
    _Gs2310QosIpv4Protocol_Type()
)
gs2310QosIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4Protocol.setStatus("current")


class _Gs2310QosIpv4ProtocolValue_Type(Integer32):
    """Custom type gs2310QosIpv4ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2310QosIpv4ProtocolValue_Type.__name__ = "Integer32"
_Gs2310QosIpv4ProtocolValue_Object = MibTableColumn
gs2310QosIpv4ProtocolValue = _Gs2310QosIpv4ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 18),
    _Gs2310QosIpv4ProtocolValue_Type()
)
gs2310QosIpv4ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4ProtocolValue.setStatus("current")
_Gs2310QosIpv4ProtocolUDPSport_Type = DisplayString
_Gs2310QosIpv4ProtocolUDPSport_Object = MibTableColumn
gs2310QosIpv4ProtocolUDPSport = _Gs2310QosIpv4ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 19),
    _Gs2310QosIpv4ProtocolUDPSport_Type()
)
gs2310QosIpv4ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4ProtocolUDPSport.setStatus("current")
_Gs2310QosIpv4ProtocolUDPDport_Type = DisplayString
_Gs2310QosIpv4ProtocolUDPDport_Object = MibTableColumn
gs2310QosIpv4ProtocolUDPDport = _Gs2310QosIpv4ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 20),
    _Gs2310QosIpv4ProtocolUDPDport_Type()
)
gs2310QosIpv4ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4ProtocolUDPDport.setStatus("current")
_Gs2310QosIpv4ProtocolTCPSport_Type = DisplayString
_Gs2310QosIpv4ProtocolTCPSport_Object = MibTableColumn
gs2310QosIpv4ProtocolTCPSport = _Gs2310QosIpv4ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 21),
    _Gs2310QosIpv4ProtocolTCPSport_Type()
)
gs2310QosIpv4ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4ProtocolTCPSport.setStatus("current")
_Gs2310QosIpv4ProtocolTCPDport_Type = DisplayString
_Gs2310QosIpv4ProtocolTCPDport_Object = MibTableColumn
gs2310QosIpv4ProtocolTCPDport = _Gs2310QosIpv4ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 22),
    _Gs2310QosIpv4ProtocolTCPDport_Type()
)
gs2310QosIpv4ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4ProtocolTCPDport.setStatus("current")
_Gs2310QosIpv4Ip_Type = DisplayString
_Gs2310QosIpv4Ip_Object = MibTableColumn
gs2310QosIpv4Ip = _Gs2310QosIpv4Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 23),
    _Gs2310QosIpv4Ip_Type()
)
gs2310QosIpv4Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4Ip.setStatus("current")
_Gs2310QosIpv4Mask_Type = DisplayString
_Gs2310QosIpv4Mask_Object = MibTableColumn
gs2310QosIpv4Mask = _Gs2310QosIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 24),
    _Gs2310QosIpv4Mask_Type()
)
gs2310QosIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4Mask.setStatus("current")


class _Gs2310QosIpv4IPFragment_Type(Integer32):
    """Custom type gs2310QosIpv4IPFragment based on Integer32"""
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


_Gs2310QosIpv4IPFragment_Type.__name__ = "Integer32"
_Gs2310QosIpv4IPFragment_Object = MibTableColumn
gs2310QosIpv4IPFragment = _Gs2310QosIpv4IPFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 25),
    _Gs2310QosIpv4IPFragment_Type()
)
gs2310QosIpv4IPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4IPFragment.setStatus("current")
_Gs2310QosIpv4DSCP_Type = DisplayString
_Gs2310QosIpv4DSCP_Object = MibTableColumn
gs2310QosIpv4DSCP = _Gs2310QosIpv4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 26),
    _Gs2310QosIpv4DSCP_Type()
)
gs2310QosIpv4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv4DSCP.setStatus("current")
_Gs2310QosIpv6Protocol_Type = DisplayString
_Gs2310QosIpv6Protocol_Object = MibTableColumn
gs2310QosIpv6Protocol = _Gs2310QosIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 27),
    _Gs2310QosIpv6Protocol_Type()
)
gs2310QosIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6Protocol.setStatus("current")


class _Gs2310QosIpv6ProtocolValue_Type(Integer32):
    """Custom type gs2310QosIpv6ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2310QosIpv6ProtocolValue_Type.__name__ = "Integer32"
_Gs2310QosIpv6ProtocolValue_Object = MibTableColumn
gs2310QosIpv6ProtocolValue = _Gs2310QosIpv6ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 28),
    _Gs2310QosIpv6ProtocolValue_Type()
)
gs2310QosIpv6ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6ProtocolValue.setStatus("current")
_Gs2310QosIpv6ProtocolUDPSport_Type = DisplayString
_Gs2310QosIpv6ProtocolUDPSport_Object = MibTableColumn
gs2310QosIpv6ProtocolUDPSport = _Gs2310QosIpv6ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 29),
    _Gs2310QosIpv6ProtocolUDPSport_Type()
)
gs2310QosIpv6ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6ProtocolUDPSport.setStatus("current")
_Gs2310QosIpv6ProtocolUDPDport_Type = DisplayString
_Gs2310QosIpv6ProtocolUDPDport_Object = MibTableColumn
gs2310QosIpv6ProtocolUDPDport = _Gs2310QosIpv6ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 30),
    _Gs2310QosIpv6ProtocolUDPDport_Type()
)
gs2310QosIpv6ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6ProtocolUDPDport.setStatus("current")
_Gs2310QosIpv6ProtocolTCPSport_Type = DisplayString
_Gs2310QosIpv6ProtocolTCPSport_Object = MibTableColumn
gs2310QosIpv6ProtocolTCPSport = _Gs2310QosIpv6ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 31),
    _Gs2310QosIpv6ProtocolTCPSport_Type()
)
gs2310QosIpv6ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6ProtocolTCPSport.setStatus("current")
_Gs2310QosIpv6ProtocolTCPDport_Type = DisplayString
_Gs2310QosIpv6ProtocolTCPDport_Object = MibTableColumn
gs2310QosIpv6ProtocolTCPDport = _Gs2310QosIpv6ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 32),
    _Gs2310QosIpv6ProtocolTCPDport_Type()
)
gs2310QosIpv6ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6ProtocolTCPDport.setStatus("current")
_Gs2310QosIpv6Ip_Type = DisplayString
_Gs2310QosIpv6Ip_Object = MibTableColumn
gs2310QosIpv6Ip = _Gs2310QosIpv6Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 33),
    _Gs2310QosIpv6Ip_Type()
)
gs2310QosIpv6Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6Ip.setStatus("current")
_Gs2310QosIpv6Mask_Type = DisplayString
_Gs2310QosIpv6Mask_Object = MibTableColumn
gs2310QosIpv6Mask = _Gs2310QosIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 34),
    _Gs2310QosIpv6Mask_Type()
)
gs2310QosIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6Mask.setStatus("current")
_Gs2310QosIpv6DSCP_Type = DisplayString
_Gs2310QosIpv6DSCP_Object = MibTableColumn
gs2310QosIpv6DSCP = _Gs2310QosIpv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 35),
    _Gs2310QosIpv6DSCP_Type()
)
gs2310QosIpv6DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosIpv6DSCP.setStatus("current")


class _Gs2310QosActionClass_Type(Integer32):
    """Custom type gs2310QosActionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2310QosActionClass_Type.__name__ = "Integer32"
_Gs2310QosActionClass_Object = MibTableColumn
gs2310QosActionClass = _Gs2310QosActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 36),
    _Gs2310QosActionClass_Type()
)
gs2310QosActionClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosActionClass.setStatus("current")


class _Gs2310QosActionDPL_Type(Integer32):
    """Custom type gs2310QosActionDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2310QosActionDPL_Type.__name__ = "Integer32"
_Gs2310QosActionDPL_Object = MibTableColumn
gs2310QosActionDPL = _Gs2310QosActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 37),
    _Gs2310QosActionDPL_Type()
)
gs2310QosActionDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosActionDPL.setStatus("current")


class _Gs2310QosActionDSCP_Type(Integer32):
    """Custom type gs2310QosActionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2310QosActionDSCP_Type.__name__ = "Integer32"
_Gs2310QosActionDSCP_Object = MibTableColumn
gs2310QosActionDSCP = _Gs2310QosActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 38),
    _Gs2310QosActionDSCP_Type()
)
gs2310QosActionDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosActionDSCP.setStatus("current")


class _Gs2310QosQceRowStatus_Type(Integer32):
    """Custom type gs2310QosQceRowStatus based on Integer32"""
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


_Gs2310QosQceRowStatus_Type.__name__ = "Integer32"
_Gs2310QosQceRowStatus_Object = MibTableColumn
gs2310QosQceRowStatus = _Gs2310QosQceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 2, 1, 39),
    _Gs2310QosQceRowStatus_Type()
)
gs2310QosQceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceRowStatus.setStatus("current")


class _Gs2310QosQceMoveID_Type(Integer32):
    """Custom type gs2310QosQceMoveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2310QosQceMoveID_Type.__name__ = "Integer32"
_Gs2310QosQceMoveID_Object = MibScalar
gs2310QosQceMoveID = _Gs2310QosQceMoveID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 3),
    _Gs2310QosQceMoveID_Type()
)
gs2310QosQceMoveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceMoveID.setStatus("current")


class _Gs2310QosQceMoveNextID_Type(Integer32):
    """Custom type gs2310QosQceMoveNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2310QosQceMoveNextID_Type.__name__ = "Integer32"
_Gs2310QosQceMoveNextID_Object = MibScalar
gs2310QosQceMoveNextID = _Gs2310QosQceMoveNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 9, 4),
    _Gs2310QosQceMoveNextID_Type()
)
gs2310QosQceMoveNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QosQceMoveNextID.setStatus("current")
_Gs2310QosQCLStatusTable_Object = MibTable
gs2310QosQCLStatusTable = _Gs2310QosQCLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10)
)
if mibBuilder.loadTexts:
    gs2310QosQCLStatusTable.setStatus("current")
_Gs2310QosQCLStatusEntry_Object = MibTableRow
gs2310QosQCLStatusEntry = _Gs2310QosQCLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1)
)
gs2310QosQCLStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310QosQCLStatusList"),
)
if mibBuilder.loadTexts:
    gs2310QosQCLStatusEntry.setStatus("current")


class _Gs2310QosQCLStatusList_Type(Integer32):
    """Custom type gs2310QosQCLStatusList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310QosQCLStatusList_Type.__name__ = "Integer32"
_Gs2310QosQCLStatusList_Object = MibTableColumn
gs2310QosQCLStatusList = _Gs2310QosQCLStatusList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 1),
    _Gs2310QosQCLStatusList_Type()
)
gs2310QosQCLStatusList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusList.setStatus("current")
_Gs2310QosQCLStatusUser_Type = DisplayString
_Gs2310QosQCLStatusUser_Object = MibTableColumn
gs2310QosQCLStatusUser = _Gs2310QosQCLStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 2),
    _Gs2310QosQCLStatusUser_Type()
)
gs2310QosQCLStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusUser.setStatus("current")
_Gs2310QosQCLStatusQCEId_Type = DisplayString
_Gs2310QosQCLStatusQCEId_Object = MibTableColumn
gs2310QosQCLStatusQCEId = _Gs2310QosQCLStatusQCEId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 3),
    _Gs2310QosQCLStatusQCEId_Type()
)
gs2310QosQCLStatusQCEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusQCEId.setStatus("current")
_Gs2310QosQCLStatusFrameType_Type = DisplayString
_Gs2310QosQCLStatusFrameType_Object = MibTableColumn
gs2310QosQCLStatusFrameType = _Gs2310QosQCLStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 4),
    _Gs2310QosQCLStatusFrameType_Type()
)
gs2310QosQCLStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusFrameType.setStatus("current")
_Gs2310QosQCLStatusPortlist_Type = DisplayString
_Gs2310QosQCLStatusPortlist_Object = MibTableColumn
gs2310QosQCLStatusPortlist = _Gs2310QosQCLStatusPortlist_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 5),
    _Gs2310QosQCLStatusPortlist_Type()
)
gs2310QosQCLStatusPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusPortlist.setStatus("current")
_Gs2310QosQCLStatusActionClass_Type = DisplayString
_Gs2310QosQCLStatusActionClass_Object = MibTableColumn
gs2310QosQCLStatusActionClass = _Gs2310QosQCLStatusActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 6),
    _Gs2310QosQCLStatusActionClass_Type()
)
gs2310QosQCLStatusActionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusActionClass.setStatus("current")
_Gs2310QosQCLStatusActionDPL_Type = DisplayString
_Gs2310QosQCLStatusActionDPL_Object = MibTableColumn
gs2310QosQCLStatusActionDPL = _Gs2310QosQCLStatusActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 7),
    _Gs2310QosQCLStatusActionDPL_Type()
)
gs2310QosQCLStatusActionDPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusActionDPL.setStatus("current")
_Gs2310QosQCLStatusActionDSCP_Type = DisplayString
_Gs2310QosQCLStatusActionDSCP_Object = MibTableColumn
gs2310QosQCLStatusActionDSCP = _Gs2310QosQCLStatusActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 8),
    _Gs2310QosQCLStatusActionDSCP_Type()
)
gs2310QosQCLStatusActionDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusActionDSCP.setStatus("current")
_Gs2310QosQCLStatusActionConflict_Type = DisplayString
_Gs2310QosQCLStatusActionConflict_Object = MibTableColumn
gs2310QosQCLStatusActionConflict = _Gs2310QosQCLStatusActionConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 10, 1, 9),
    _Gs2310QosQCLStatusActionConflict_Type()
)
gs2310QosQCLStatusActionConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310QosQCLStatusActionConflict.setStatus("current")
_Gs2310QosStormControl_ObjectIdentity = ObjectIdentity
gs2310QosStormControl = _Gs2310QosStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11)
)


class _Gs2310QoSStormControlUC_Type(Integer32):
    """Custom type gs2310QoSStormControlUC based on Integer32"""
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


_Gs2310QoSStormControlUC_Type.__name__ = "Integer32"
_Gs2310QoSStormControlUC_Object = MibScalar
gs2310QoSStormControlUC = _Gs2310QoSStormControlUC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11, 2),
    _Gs2310QoSStormControlUC_Type()
)
gs2310QoSStormControlUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSStormControlUC.setStatus("current")
_Gs2310QoSStormControlUCRate_Type = DisplayString
_Gs2310QoSStormControlUCRate_Object = MibScalar
gs2310QoSStormControlUCRate = _Gs2310QoSStormControlUCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11, 3),
    _Gs2310QoSStormControlUCRate_Type()
)
gs2310QoSStormControlUCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSStormControlUCRate.setStatus("current")


class _Gs2310QoSStormControlMC_Type(Integer32):
    """Custom type gs2310QoSStormControlMC based on Integer32"""
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


_Gs2310QoSStormControlMC_Type.__name__ = "Integer32"
_Gs2310QoSStormControlMC_Object = MibScalar
gs2310QoSStormControlMC = _Gs2310QoSStormControlMC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11, 4),
    _Gs2310QoSStormControlMC_Type()
)
gs2310QoSStormControlMC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSStormControlMC.setStatus("current")
_Gs2310QoSStormControlMCRate_Type = DisplayString
_Gs2310QoSStormControlMCRate_Object = MibScalar
gs2310QoSStormControlMCRate = _Gs2310QoSStormControlMCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11, 5),
    _Gs2310QoSStormControlMCRate_Type()
)
gs2310QoSStormControlMCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSStormControlMCRate.setStatus("current")


class _Gs2310QoSStormControlBC_Type(Integer32):
    """Custom type gs2310QoSStormControlBC based on Integer32"""
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


_Gs2310QoSStormControlBC_Type.__name__ = "Integer32"
_Gs2310QoSStormControlBC_Object = MibScalar
gs2310QoSStormControlBC = _Gs2310QoSStormControlBC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11, 6),
    _Gs2310QoSStormControlBC_Type()
)
gs2310QoSStormControlBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSStormControlBC.setStatus("current")
_Gs2310QoSStormControlBCRate_Type = DisplayString
_Gs2310QoSStormControlBCRate_Object = MibScalar
gs2310QoSStormControlBCRate = _Gs2310QoSStormControlBCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 14, 11, 7),
    _Gs2310QoSStormControlBCRate_Type()
)
gs2310QoSStormControlBCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310QoSStormControlBCRate.setStatus("current")
_Gs2310Vlan_ObjectIdentity = ObjectIdentity
gs2310Vlan = _Gs2310Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15)
)
_Gs2310VlanPorts_ObjectIdentity = ObjectIdentity
gs2310VlanPorts = _Gs2310VlanPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1)
)


class _Gs2310VlanPortsTPIDforCustomSport_Type(OctetString):
    """Custom type gs2310VlanPortsTPIDforCustomSport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Gs2310VlanPortsTPIDforCustomSport_Type.__name__ = "OctetString"
_Gs2310VlanPortsTPIDforCustomSport_Object = MibScalar
gs2310VlanPortsTPIDforCustomSport = _Gs2310VlanPortsTPIDforCustomSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 1),
    _Gs2310VlanPortsTPIDforCustomSport_Type()
)
gs2310VlanPortsTPIDforCustomSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortsTPIDforCustomSport.setStatus("current")
_Gs2310VlanPortsTable_Object = MibTable
gs2310VlanPortsTable = _Gs2310VlanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310VlanPortsTable.setStatus("current")
_Gs2310VlanPortsEntry_Object = MibTableRow
gs2310VlanPortsEntry = _Gs2310VlanPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1)
)
gs2310VlanPortsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310VlanPortsPort"),
)
if mibBuilder.loadTexts:
    gs2310VlanPortsEntry.setStatus("current")


class _Gs2310VlanPortsPort_Type(Integer32):
    """Custom type gs2310VlanPortsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310VlanPortsPort_Type.__name__ = "Integer32"
_Gs2310VlanPortsPort_Object = MibTableColumn
gs2310VlanPortsPort = _Gs2310VlanPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1, 1),
    _Gs2310VlanPortsPort_Type()
)
gs2310VlanPortsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310VlanPortsPort.setStatus("current")


class _Gs2310VlanPortsPVID_Type(Integer32):
    """Custom type gs2310VlanPortsPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310VlanPortsPVID_Type.__name__ = "Integer32"
_Gs2310VlanPortsPVID_Object = MibTableColumn
gs2310VlanPortsPVID = _Gs2310VlanPortsPVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1, 2),
    _Gs2310VlanPortsPVID_Type()
)
gs2310VlanPortsPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortsPVID.setStatus("current")


class _Gs2310VlanPortsFrameType_Type(Integer32):
    """Custom type gs2310VlanPortsFrameType based on Integer32"""
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


_Gs2310VlanPortsFrameType_Type.__name__ = "Integer32"
_Gs2310VlanPortsFrameType_Object = MibTableColumn
gs2310VlanPortsFrameType = _Gs2310VlanPortsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1, 3),
    _Gs2310VlanPortsFrameType_Type()
)
gs2310VlanPortsFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortsFrameType.setStatus("current")


class _Gs2310VlanPortsIngressFilter_Type(Integer32):
    """Custom type gs2310VlanPortsIngressFilter based on Integer32"""
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


_Gs2310VlanPortsIngressFilter_Type.__name__ = "Integer32"
_Gs2310VlanPortsIngressFilter_Object = MibTableColumn
gs2310VlanPortsIngressFilter = _Gs2310VlanPortsIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1, 4),
    _Gs2310VlanPortsIngressFilter_Type()
)
gs2310VlanPortsIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortsIngressFilter.setStatus("current")


class _Gs2310VlanPortsEgressRule_Type(Integer32):
    """Custom type gs2310VlanPortsEgressRule based on Integer32"""
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


_Gs2310VlanPortsEgressRule_Type.__name__ = "Integer32"
_Gs2310VlanPortsEgressRule_Object = MibTableColumn
gs2310VlanPortsEgressRule = _Gs2310VlanPortsEgressRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1, 5),
    _Gs2310VlanPortsEgressRule_Type()
)
gs2310VlanPortsEgressRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortsEgressRule.setStatus("current")


class _Gs2310VlanPortsPortType_Type(Integer32):
    """Custom type gs2310VlanPortsPortType based on Integer32"""
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


_Gs2310VlanPortsPortType_Type.__name__ = "Integer32"
_Gs2310VlanPortsPortType_Object = MibTableColumn
gs2310VlanPortsPortType = _Gs2310VlanPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 1, 2, 1, 6),
    _Gs2310VlanPortsPortType_Type()
)
gs2310VlanPortsPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortsPortType.setStatus("current")
_Gs2310VlanPrivateVLAN_ObjectIdentity = ObjectIdentity
gs2310VlanPrivateVLAN = _Gs2310VlanPrivateVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2)
)
_Gs2310VlanPrivateVLANMembership_ObjectIdentity = ObjectIdentity
gs2310VlanPrivateVLANMembership = _Gs2310VlanPrivateVLANMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1)
)


class _Gs2310VlanPrivateVLANMembershipCreate_Type(Integer32):
    """Custom type gs2310VlanPrivateVLANMembershipCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310VlanPrivateVLANMembershipCreate_Type.__name__ = "Integer32"
_Gs2310VlanPrivateVLANMembershipCreate_Object = MibScalar
gs2310VlanPrivateVLANMembershipCreate = _Gs2310VlanPrivateVLANMembershipCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 1),
    _Gs2310VlanPrivateVLANMembershipCreate_Type()
)
gs2310VlanPrivateVLANMembershipCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANMembershipCreate.setStatus("current")
_Gs2310VlanPrivateVLANMembershipTable_Object = MibTable
gs2310VlanPrivateVLANMembershipTable = _Gs2310VlanPrivateVLANMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANMembershipTable.setStatus("current")
_Gs2310VlanPrivateVLANMembershipEntry_Object = MibTableRow
gs2310VlanPrivateVLANMembershipEntry = _Gs2310VlanPrivateVLANMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 2, 1)
)
gs2310VlanPrivateVLANMembershipEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310VlanPrivateVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANMembershipEntry.setStatus("current")


class _Gs2310VlanPrivateVLANIndex_Type(Integer32):
    """Custom type gs2310VlanPrivateVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2310VlanPrivateVLANIndex_Type.__name__ = "Integer32"
_Gs2310VlanPrivateVLANIndex_Object = MibTableColumn
gs2310VlanPrivateVLANIndex = _Gs2310VlanPrivateVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 2, 1, 1),
    _Gs2310VlanPrivateVLANIndex_Type()
)
gs2310VlanPrivateVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANIndex.setStatus("current")


class _Gs2310VlanPrivateVLANID_Type(Integer32):
    """Custom type gs2310VlanPrivateVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2310VlanPrivateVLANID_Type.__name__ = "Integer32"
_Gs2310VlanPrivateVLANID_Object = MibTableColumn
gs2310VlanPrivateVLANID = _Gs2310VlanPrivateVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 2, 1, 2),
    _Gs2310VlanPrivateVLANID_Type()
)
gs2310VlanPrivateVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANID.setStatus("current")
_Gs2310VlanPrivateVLANMemberships_Type = DisplayString
_Gs2310VlanPrivateVLANMemberships_Object = MibTableColumn
gs2310VlanPrivateVLANMemberships = _Gs2310VlanPrivateVLANMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 2, 1, 3),
    _Gs2310VlanPrivateVLANMemberships_Type()
)
gs2310VlanPrivateVLANMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANMemberships.setStatus("current")


class _Gs2310VlanPrivateVLANRowStatus_Type(Integer32):
    """Custom type gs2310VlanPrivateVLANRowStatus based on Integer32"""
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


_Gs2310VlanPrivateVLANRowStatus_Type.__name__ = "Integer32"
_Gs2310VlanPrivateVLANRowStatus_Object = MibTableColumn
gs2310VlanPrivateVLANRowStatus = _Gs2310VlanPrivateVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 1, 2, 1, 4),
    _Gs2310VlanPrivateVLANRowStatus_Type()
)
gs2310VlanPrivateVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPrivateVLANRowStatus.setStatus("current")
_Gs2310VlanPortIsolationTable_Object = MibTable
gs2310VlanPortIsolationTable = _Gs2310VlanPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310VlanPortIsolationTable.setStatus("current")
_Gs2310VlanPortIsolationEntry_Object = MibTableRow
gs2310VlanPortIsolationEntry = _Gs2310VlanPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 2, 1)
)
gs2310VlanPortIsolationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310VlanPortIsolationPort"),
)
if mibBuilder.loadTexts:
    gs2310VlanPortIsolationEntry.setStatus("current")


class _Gs2310VlanPortIsolationPort_Type(Integer32):
    """Custom type gs2310VlanPortIsolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310VlanPortIsolationPort_Type.__name__ = "Integer32"
_Gs2310VlanPortIsolationPort_Object = MibTableColumn
gs2310VlanPortIsolationPort = _Gs2310VlanPortIsolationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 2, 1, 1),
    _Gs2310VlanPortIsolationPort_Type()
)
gs2310VlanPortIsolationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310VlanPortIsolationPort.setStatus("current")


class _Gs2310VlanPortIsolation_Type(Integer32):
    """Custom type gs2310VlanPortIsolation based on Integer32"""
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


_Gs2310VlanPortIsolation_Type.__name__ = "Integer32"
_Gs2310VlanPortIsolation_Object = MibTableColumn
gs2310VlanPortIsolation = _Gs2310VlanPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 2, 2, 1, 2),
    _Gs2310VlanPortIsolation_Type()
)
gs2310VlanPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310VlanPortIsolation.setStatus("current")
_Gs2310MACbasedVLAN_ObjectIdentity = ObjectIdentity
gs2310MACbasedVLAN = _Gs2310MACbasedVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3)
)
_Gs2310MACbasedVLANConf_ObjectIdentity = ObjectIdentity
gs2310MACbasedVLANConf = _Gs2310MACbasedVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1)
)
_Gs2310MACbasedVLANConfCreate_Type = Integer32
_Gs2310MACbasedVLANConfCreate_Object = MibScalar
gs2310MACbasedVLANConfCreate = _Gs2310MACbasedVLANConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 1),
    _Gs2310MACbasedVLANConfCreate_Type()
)
gs2310MACbasedVLANConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACbasedVLANConfCreate.setStatus("current")
_Gs2310MACbasedVLANConfTable_Object = MibTable
gs2310MACbasedVLANConfTable = _Gs2310MACbasedVLANConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310MACbasedVLANConfTable.setStatus("current")
_Gs2310MACbasedVLANConfEntry_Object = MibTableRow
gs2310MACbasedVLANConfEntry = _Gs2310MACbasedVLANConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2, 1)
)
gs2310MACbasedVLANConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MACbasedVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2310MACbasedVLANConfEntry.setStatus("current")


class _Gs2310MACbasedVLANIndex_Type(Integer32):
    """Custom type gs2310MACbasedVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2310MACbasedVLANIndex_Type.__name__ = "Integer32"
_Gs2310MACbasedVLANIndex_Object = MibTableColumn
gs2310MACbasedVLANIndex = _Gs2310MACbasedVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2, 1, 1),
    _Gs2310MACbasedVLANIndex_Type()
)
gs2310MACbasedVLANIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACbasedVLANIndex.setStatus("current")
_Gs2310MACbasedVLANMACAddress_Type = MacAddress
_Gs2310MACbasedVLANMACAddress_Object = MibTableColumn
gs2310MACbasedVLANMACAddress = _Gs2310MACbasedVLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2, 1, 2),
    _Gs2310MACbasedVLANMACAddress_Type()
)
gs2310MACbasedVLANMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACbasedVLANMACAddress.setStatus("current")


class _Gs2310MACbasedVLANID_Type(Integer32):
    """Custom type gs2310MACbasedVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310MACbasedVLANID_Type.__name__ = "Integer32"
_Gs2310MACbasedVLANID_Object = MibTableColumn
gs2310MACbasedVLANID = _Gs2310MACbasedVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2, 1, 3),
    _Gs2310MACbasedVLANID_Type()
)
gs2310MACbasedVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACbasedVLANID.setStatus("current")
_Gs2310MACbasedMemberships_Type = DisplayString
_Gs2310MACbasedMemberships_Object = MibTableColumn
gs2310MACbasedMemberships = _Gs2310MACbasedMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2, 1, 4),
    _Gs2310MACbasedMemberships_Type()
)
gs2310MACbasedMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACbasedMemberships.setStatus("current")


class _Gs2310MACbaseRowStatus_Type(Integer32):
    """Custom type gs2310MACbaseRowStatus based on Integer32"""
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


_Gs2310MACbaseRowStatus_Type.__name__ = "Integer32"
_Gs2310MACbaseRowStatus_Object = MibTableColumn
gs2310MACbaseRowStatus = _Gs2310MACbaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 15, 3, 1, 2, 1, 5),
    _Gs2310MACbaseRowStatus_Type()
)
gs2310MACbaseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MACbaseRowStatus.setStatus("current")
_Gs2310IGMPSnooping_ObjectIdentity = ObjectIdentity
gs2310IGMPSnooping = _Gs2310IGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16)
)
_Gs2310IGMPSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2310IGMPSnoopingBasic = _Gs2310IGMPSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1)
)


class _Gs2310IGMPSnoopingEnable_Type(Integer32):
    """Custom type gs2310IGMPSnoopingEnable based on Integer32"""
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


_Gs2310IGMPSnoopingEnable_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingEnable_Object = MibScalar
gs2310IGMPSnoopingEnable = _Gs2310IGMPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 1),
    _Gs2310IGMPSnoopingEnable_Type()
)
gs2310IGMPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingEnable.setStatus("current")


class _Gs2310IGMPSnoopingUnregisteredIPMCv4Flooding_Type(Integer32):
    """Custom type gs2310IGMPSnoopingUnregisteredIPMCv4Flooding based on Integer32"""
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


_Gs2310IGMPSnoopingUnregisteredIPMCv4Flooding_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingUnregisteredIPMCv4Flooding_Object = MibScalar
gs2310IGMPSnoopingUnregisteredIPMCv4Flooding = _Gs2310IGMPSnoopingUnregisteredIPMCv4Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 2),
    _Gs2310IGMPSnoopingUnregisteredIPMCv4Flooding_Type()
)
gs2310IGMPSnoopingUnregisteredIPMCv4Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingUnregisteredIPMCv4Flooding.setStatus("current")
_Gs2310IGMPSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2310IGMPSnoopingSSMIPRangeAddr_Object = MibScalar
gs2310IGMPSnoopingSSMIPRangeAddr = _Gs2310IGMPSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 3),
    _Gs2310IGMPSnoopingSSMIPRangeAddr_Type()
)
gs2310IGMPSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2310IGMPSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2310IGMPSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_Gs2310IGMPSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingSSMIPRangeValue_Object = MibScalar
gs2310IGMPSnoopingSSMIPRangeValue = _Gs2310IGMPSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 4),
    _Gs2310IGMPSnoopingSSMIPRangeValue_Type()
)
gs2310IGMPSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2310IGMPSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2310IGMPSnoopingProxyEnabled based on Integer32"""
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


_Gs2310IGMPSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingProxyEnabled_Object = MibScalar
gs2310IGMPSnoopingProxyEnabled = _Gs2310IGMPSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 5),
    _Gs2310IGMPSnoopingProxyEnabled_Type()
)
gs2310IGMPSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingProxyEnabled.setStatus("current")
_Gs2310IGMPSnoopingPortRelatedTable_Object = MibTable
gs2310IGMPSnoopingPortRelatedTable = _Gs2310IGMPSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortRelatedTable.setStatus("current")
_Gs2310IGMPSnoopingPortRelatedEntry_Object = MibTableRow
gs2310IGMPSnoopingPortRelatedEntry = _Gs2310IGMPSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 6, 1)
)
gs2310IGMPSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortRelatedEntry.setStatus("current")


class _Gs2310IGMPSnoopingRouterPort_Type(Integer32):
    """Custom type gs2310IGMPSnoopingRouterPort based on Integer32"""
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


_Gs2310IGMPSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingRouterPort_Object = MibTableColumn
gs2310IGMPSnoopingRouterPort = _Gs2310IGMPSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 6, 1, 1),
    _Gs2310IGMPSnoopingRouterPort_Type()
)
gs2310IGMPSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingRouterPort.setStatus("current")


class _Gs2310IGMPSnoopingFastLeave_Type(Integer32):
    """Custom type gs2310IGMPSnoopingFastLeave based on Integer32"""
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


_Gs2310IGMPSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingFastLeave_Object = MibTableColumn
gs2310IGMPSnoopingFastLeave = _Gs2310IGMPSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 6, 1, 2),
    _Gs2310IGMPSnoopingFastLeave_Type()
)
gs2310IGMPSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingFastLeave.setStatus("current")


class _Gs2310IGMPSnoopingThrottling_Type(Integer32):
    """Custom type gs2310IGMPSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2310IGMPSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingThrottling_Object = MibTableColumn
gs2310IGMPSnoopingThrottling = _Gs2310IGMPSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 1, 6, 1, 3),
    _Gs2310IGMPSnoopingThrottling_Type()
)
gs2310IGMPSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingThrottling.setStatus("current")
_Gs2310IGMPSnoopingVLANTable_Object = MibTable
gs2310IGMPSnoopingVLANTable = _Gs2310IGMPSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANTable.setStatus("current")
_Gs2310IGMPSnoopingVLANEntry_Object = MibTableRow
gs2310IGMPSnoopingVLANEntry = _Gs2310IGMPSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1)
)
gs2310IGMPSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IGMPSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANEntry.setStatus("current")


class _Gs2310IGMPSnoopingVLANID_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IGMPSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANID_Object = MibTableColumn
gs2310IGMPSnoopingVLANID = _Gs2310IGMPSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 1),
    _Gs2310IGMPSnoopingVLANID_Type()
)
gs2310IGMPSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANID.setStatus("current")


class _Gs2310IGMPSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANEnable based on Integer32"""
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


_Gs2310IGMPSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANEnable_Object = MibTableColumn
gs2310IGMPSnoopingVLANEnable = _Gs2310IGMPSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 2),
    _Gs2310IGMPSnoopingVLANEnable_Type()
)
gs2310IGMPSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANEnable.setStatus("current")


class _Gs2310IGMPSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANIGMPQuerier based on Integer32"""
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


_Gs2310IGMPSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2310IGMPSnoopingVLANIGMPQuerier = _Gs2310IGMPSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 3),
    _Gs2310IGMPSnoopingVLANIGMPQuerier_Type()
)
gs2310IGMPSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2310IGMPSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANCompatibility based on Integer32"""
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


_Gs2310IGMPSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANCompatibility_Object = MibTableColumn
gs2310IGMPSnoopingVLANCompatibility = _Gs2310IGMPSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 4),
    _Gs2310IGMPSnoopingVLANCompatibility_Type()
)
gs2310IGMPSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANCompatibility.setStatus("current")


class _Gs2310IGMPSnoopingVLANRV_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2310IGMPSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANRV_Object = MibTableColumn
gs2310IGMPSnoopingVLANRV = _Gs2310IGMPSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 5),
    _Gs2310IGMPSnoopingVLANRV_Type()
)
gs2310IGMPSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANRV.setStatus("current")


class _Gs2310IGMPSnoopingVLANQI_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2310IGMPSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANQI_Object = MibTableColumn
gs2310IGMPSnoopingVLANQI = _Gs2310IGMPSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 6),
    _Gs2310IGMPSnoopingVLANQI_Type()
)
gs2310IGMPSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANQI.setStatus("current")


class _Gs2310IGMPSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2310IGMPSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANQRI_Object = MibTableColumn
gs2310IGMPSnoopingVLANQRI = _Gs2310IGMPSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 7),
    _Gs2310IGMPSnoopingVLANQRI_Type()
)
gs2310IGMPSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANQRI.setStatus("current")


class _Gs2310IGMPSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2310IGMPSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANLLQI_Object = MibTableColumn
gs2310IGMPSnoopingVLANLLQI = _Gs2310IGMPSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 8),
    _Gs2310IGMPSnoopingVLANLLQI_Type()
)
gs2310IGMPSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANLLQI.setStatus("current")


class _Gs2310IGMPSnoopingVLANURI_Type(Integer32):
    """Custom type gs2310IGMPSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2310IGMPSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingVLANURI_Object = MibTableColumn
gs2310IGMPSnoopingVLANURI = _Gs2310IGMPSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 2, 1, 9),
    _Gs2310IGMPSnoopingVLANURI_Type()
)
gs2310IGMPSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingVLANURI.setStatus("current")
_Gs2310IGMPSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2310IGMPSnoopingPortGroupFiltering = _Gs2310IGMPSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3)
)
_Gs2310IGMPSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2310IGMPSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2310IGMPSnoopingPortGroupFilteringCreate = _Gs2310IGMPSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 1),
    _Gs2310IGMPSnoopingPortGroupFilteringCreate_Type()
)
gs2310IGMPSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2310IGMPSnoopingPortGroupFilteringTable_Object = MibTable
gs2310IGMPSnoopingPortGroupFilteringTable = _Gs2310IGMPSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2310IGMPSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2310IGMPSnoopingPortGroupFilteringEntry = _Gs2310IGMPSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 2, 1)
)
gs2310IGMPSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IGMPSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2310IGMPSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2310IGMPSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310IGMPSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2310IGMPSnoopingPortGroupFilteringIndex = _Gs2310IGMPSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 2, 1, 1),
    _Gs2310IGMPSnoopingPortGroupFilteringIndex_Type()
)
gs2310IGMPSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2310IGMPSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2310IGMPSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310IGMPSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2310IGMPSnoopingPortGroupFilteringPort = _Gs2310IGMPSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 2, 1, 2),
    _Gs2310IGMPSnoopingPortGroupFilteringPort_Type()
)
gs2310IGMPSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2310IGMPSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2310IGMPSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2310IGMPSnoopingPortGroupFilteringGroups = _Gs2310IGMPSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 2, 1, 3),
    _Gs2310IGMPSnoopingPortGroupFilteringGroups_Type()
)
gs2310IGMPSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2310IGMPSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2310IGMPSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2310IGMPSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2310IGMPSnoopingPortGroupFilteringRowStatus = _Gs2310IGMPSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 3, 2, 1, 4),
    _Gs2310IGMPSnoopingPortGroupFilteringRowStatus_Type()
)
gs2310IGMPSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2310IGMPSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2310IGMPSnoopingStatus = _Gs2310IGMPSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4)
)


class _Gs2310IGMPSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2310IGMPSnoopingstatisticClear based on Integer32"""
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


_Gs2310IGMPSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingstatisticClear_Object = MibScalar
gs2310IGMPSnoopingstatisticClear = _Gs2310IGMPSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 1),
    _Gs2310IGMPSnoopingstatisticClear_Type()
)
gs2310IGMPSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticClear.setStatus("current")
_Gs2310IGMPSnoopingstatisticTable_Object = MibTable
gs2310IGMPSnoopingstatisticTable = _Gs2310IGMPSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticTable.setStatus("current")
_Gs2310IGMPSnoopingstatisticEntry_Object = MibTableRow
gs2310IGMPSnoopingstatisticEntry = _Gs2310IGMPSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1)
)
gs2310IGMPSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IGMPSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticEntry.setStatus("current")


class _Gs2310IGMPSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2310IGMPSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IGMPSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingstatisticVLANID_Object = MibTableColumn
gs2310IGMPSnoopingstatisticVLANID = _Gs2310IGMPSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 1),
    _Gs2310IGMPSnoopingstatisticVLANID_Type()
)
gs2310IGMPSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticVLANID.setStatus("current")
_Gs2310IGMPSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2310IGMPSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2310IGMPSnoopingstatisticQuerierVersion = _Gs2310IGMPSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 2),
    _Gs2310IGMPSnoopingstatisticQuerierVersion_Type()
)
gs2310IGMPSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2310IGMPSnoopingstatisticHostVersion_Type = DisplayString
_Gs2310IGMPSnoopingstatisticHostVersion_Object = MibTableColumn
gs2310IGMPSnoopingstatisticHostVersion = _Gs2310IGMPSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 3),
    _Gs2310IGMPSnoopingstatisticHostVersion_Type()
)
gs2310IGMPSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticHostVersion.setStatus("current")
_Gs2310IGMPSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2310IGMPSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2310IGMPSnoopingstatisticQuerierStatus = _Gs2310IGMPSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 4),
    _Gs2310IGMPSnoopingstatisticQuerierStatus_Type()
)
gs2310IGMPSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2310IGMPSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2310IGMPSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2310IGMPSnoopingstatisticQueriesTransmitted = _Gs2310IGMPSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 5),
    _Gs2310IGMPSnoopingstatisticQueriesTransmitted_Type()
)
gs2310IGMPSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2310IGMPSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2310IGMPSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2310IGMPSnoopingstatisticQueriesReceived = _Gs2310IGMPSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 6),
    _Gs2310IGMPSnoopingstatisticQueriesReceived_Type()
)
gs2310IGMPSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2310IGMPSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2310IGMPSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2310IGMPSnoopingstatisticV1ReportsReceived = _Gs2310IGMPSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 7),
    _Gs2310IGMPSnoopingstatisticV1ReportsReceived_Type()
)
gs2310IGMPSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2310IGMPSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2310IGMPSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2310IGMPSnoopingstatisticV2ReportsReceived = _Gs2310IGMPSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 8),
    _Gs2310IGMPSnoopingstatisticV2ReportsReceived_Type()
)
gs2310IGMPSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2310IGMPSnoopingstatisticV3ReportsReceived_Type = Counter32
_Gs2310IGMPSnoopingstatisticV3ReportsReceived_Object = MibTableColumn
gs2310IGMPSnoopingstatisticV3ReportsReceived = _Gs2310IGMPSnoopingstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 9),
    _Gs2310IGMPSnoopingstatisticV3ReportsReceived_Type()
)
gs2310IGMPSnoopingstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticV3ReportsReceived.setStatus("current")
_Gs2310IGMPSnoopingstatisticV2LeavesReceived_Type = Counter32
_Gs2310IGMPSnoopingstatisticV2LeavesReceived_Object = MibTableColumn
gs2310IGMPSnoopingstatisticV2LeavesReceived = _Gs2310IGMPSnoopingstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 2, 1, 10),
    _Gs2310IGMPSnoopingstatisticV2LeavesReceived_Type()
)
gs2310IGMPSnoopingstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingstatisticV2LeavesReceived.setStatus("current")
_Gs2310IGMPSnoopingRouterPortTable_Object = MibTable
gs2310IGMPSnoopingRouterPortTable = _Gs2310IGMPSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 3)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingRouterPortTable.setStatus("current")
_Gs2310IGMPSnoopingRouterPortEntry_Object = MibTableRow
gs2310IGMPSnoopingRouterPortEntry = _Gs2310IGMPSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 3, 1)
)
gs2310IGMPSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingRouterPortEntry.setStatus("current")
_Gs2310IGMPSnoopingRouterPortStatus_Type = DisplayString
_Gs2310IGMPSnoopingRouterPortStatus_Object = MibTableColumn
gs2310IGMPSnoopingRouterPortStatus = _Gs2310IGMPSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 4, 3, 1, 1),
    _Gs2310IGMPSnoopingRouterPortStatus_Type()
)
gs2310IGMPSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingRouterPortStatus.setStatus("current")
_Gs2310IGMPSnoopingGroupsTable_Object = MibTable
gs2310IGMPSnoopingGroupsTable = _Gs2310IGMPSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 5)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingGroupsTable.setStatus("current")
_Gs2310IGMPSnoopingGroupsEntry_Object = MibTableRow
gs2310IGMPSnoopingGroupsEntry = _Gs2310IGMPSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 5, 1)
)
gs2310IGMPSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IGMPSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingGroupsEntry.setStatus("current")


class _Gs2310IGMPSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2310IGMPSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310IGMPSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingGroupsIndex_Object = MibTableColumn
gs2310IGMPSnoopingGroupsIndex = _Gs2310IGMPSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 5, 1, 1),
    _Gs2310IGMPSnoopingGroupsIndex_Type()
)
gs2310IGMPSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingGroupsIndex.setStatus("current")


class _Gs2310IGMPSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2310IGMPSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IGMPSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingGroupsVLANID_Object = MibTableColumn
gs2310IGMPSnoopingGroupsVLANID = _Gs2310IGMPSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 5, 1, 2),
    _Gs2310IGMPSnoopingGroupsVLANID_Type()
)
gs2310IGMPSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingGroupsVLANID.setStatus("current")
_Gs2310IGMPSnoopingGroups_Type = DisplayString
_Gs2310IGMPSnoopingGroups_Object = MibTableColumn
gs2310IGMPSnoopingGroups = _Gs2310IGMPSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 5, 1, 3),
    _Gs2310IGMPSnoopingGroups_Type()
)
gs2310IGMPSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingGroups.setStatus("current")
_Gs2310IGMPSnoopingGroupsMemberships_Type = DisplayString
_Gs2310IGMPSnoopingGroupsMemberships_Object = MibTableColumn
gs2310IGMPSnoopingGroupsMemberships = _Gs2310IGMPSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 5, 1, 4),
    _Gs2310IGMPSnoopingGroupsMemberships_Type()
)
gs2310IGMPSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingGroupsMemberships.setStatus("current")
_Gs2310IGMPSnoopingSSMTable_Object = MibTable
gs2310IGMPSnoopingSSMTable = _Gs2310IGMPSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6)
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMTable.setStatus("current")
_Gs2310IGMPSnoopingSSMEntry_Object = MibTableRow
gs2310IGMPSnoopingSSMEntry = _Gs2310IGMPSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1)
)
gs2310IGMPSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IGMPSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMEntry.setStatus("current")


class _Gs2310IGMPSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2310IGMPSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310IGMPSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingSSMIndex_Object = MibTableColumn
gs2310IGMPSnoopingSSMIndex = _Gs2310IGMPSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 1),
    _Gs2310IGMPSnoopingSSMIndex_Type()
)
gs2310IGMPSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMIndex.setStatus("current")


class _Gs2310IGMPSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2310IGMPSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IGMPSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingSSMVLANID_Object = MibTableColumn
gs2310IGMPSnoopingSSMVLANID = _Gs2310IGMPSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 2),
    _Gs2310IGMPSnoopingSSMVLANID_Type()
)
gs2310IGMPSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMVLANID.setStatus("current")
_Gs2310IGMPSnoopingSSMGroup_Type = DisplayString
_Gs2310IGMPSnoopingSSMGroup_Object = MibTableColumn
gs2310IGMPSnoopingSSMGroup = _Gs2310IGMPSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 3),
    _Gs2310IGMPSnoopingSSMGroup_Type()
)
gs2310IGMPSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMGroup.setStatus("current")


class _Gs2310IGMPSnoopingSSMPort_Type(Integer32):
    """Custom type gs2310IGMPSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310IGMPSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2310IGMPSnoopingSSMPort_Object = MibTableColumn
gs2310IGMPSnoopingSSMPort = _Gs2310IGMPSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 4),
    _Gs2310IGMPSnoopingSSMPort_Type()
)
gs2310IGMPSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMPort.setStatus("current")
_Gs2310IGMPSnoopingSSMMode_Type = DisplayString
_Gs2310IGMPSnoopingSSMMode_Object = MibTableColumn
gs2310IGMPSnoopingSSMMode = _Gs2310IGMPSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 5),
    _Gs2310IGMPSnoopingSSMMode_Type()
)
gs2310IGMPSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMMode.setStatus("current")
_Gs2310IGMPSnoopingSSMSourceAddress_Type = DisplayString
_Gs2310IGMPSnoopingSSMSourceAddress_Object = MibTableColumn
gs2310IGMPSnoopingSSMSourceAddress = _Gs2310IGMPSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 6),
    _Gs2310IGMPSnoopingSSMSourceAddress_Type()
)
gs2310IGMPSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMSourceAddress.setStatus("current")
_Gs2310IGMPSnoopingSSMType_Type = DisplayString
_Gs2310IGMPSnoopingSSMType_Object = MibTableColumn
gs2310IGMPSnoopingSSMType = _Gs2310IGMPSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 16, 6, 1, 7),
    _Gs2310IGMPSnoopingSSMType_Type()
)
gs2310IGMPSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IGMPSnoopingSSMType.setStatus("current")
_Gs2310MLDSnooping_ObjectIdentity = ObjectIdentity
gs2310MLDSnooping = _Gs2310MLDSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17)
)
_Gs2310MLDSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2310MLDSnoopingBasic = _Gs2310MLDSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1)
)


class _Gs2310MLDSnoopingEnable_Type(Integer32):
    """Custom type gs2310MLDSnoopingEnable based on Integer32"""
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


_Gs2310MLDSnoopingEnable_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingEnable_Object = MibScalar
gs2310MLDSnoopingEnable = _Gs2310MLDSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 1),
    _Gs2310MLDSnoopingEnable_Type()
)
gs2310MLDSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingEnable.setStatus("current")


class _Gs2310MLDSnoopingUnregisteredIPMCv6Flooding_Type(Integer32):
    """Custom type gs2310MLDSnoopingUnregisteredIPMCv6Flooding based on Integer32"""
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


_Gs2310MLDSnoopingUnregisteredIPMCv6Flooding_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingUnregisteredIPMCv6Flooding_Object = MibScalar
gs2310MLDSnoopingUnregisteredIPMCv6Flooding = _Gs2310MLDSnoopingUnregisteredIPMCv6Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 2),
    _Gs2310MLDSnoopingUnregisteredIPMCv6Flooding_Type()
)
gs2310MLDSnoopingUnregisteredIPMCv6Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingUnregisteredIPMCv6Flooding.setStatus("current")
_Gs2310MLDSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2310MLDSnoopingSSMIPRangeAddr_Object = MibScalar
gs2310MLDSnoopingSSMIPRangeAddr = _Gs2310MLDSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 3),
    _Gs2310MLDSnoopingSSMIPRangeAddr_Type()
)
gs2310MLDSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2310MLDSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2310MLDSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_Gs2310MLDSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingSSMIPRangeValue_Object = MibScalar
gs2310MLDSnoopingSSMIPRangeValue = _Gs2310MLDSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 4),
    _Gs2310MLDSnoopingSSMIPRangeValue_Type()
)
gs2310MLDSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2310MLDSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2310MLDSnoopingProxyEnabled based on Integer32"""
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


_Gs2310MLDSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingProxyEnabled_Object = MibScalar
gs2310MLDSnoopingProxyEnabled = _Gs2310MLDSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 5),
    _Gs2310MLDSnoopingProxyEnabled_Type()
)
gs2310MLDSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingProxyEnabled.setStatus("current")
_Gs2310MLDSnoopingPortRelatedTable_Object = MibTable
gs2310MLDSnoopingPortRelatedTable = _Gs2310MLDSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 6)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortRelatedTable.setStatus("current")
_Gs2310MLDSnoopingPortRelatedEntry_Object = MibTableRow
gs2310MLDSnoopingPortRelatedEntry = _Gs2310MLDSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 6, 1)
)
gs2310MLDSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortRelatedEntry.setStatus("current")


class _Gs2310MLDSnoopingRouterPort_Type(Integer32):
    """Custom type gs2310MLDSnoopingRouterPort based on Integer32"""
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


_Gs2310MLDSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingRouterPort_Object = MibTableColumn
gs2310MLDSnoopingRouterPort = _Gs2310MLDSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 6, 1, 1),
    _Gs2310MLDSnoopingRouterPort_Type()
)
gs2310MLDSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingRouterPort.setStatus("current")


class _Gs2310MLDSnoopingFastLeave_Type(Integer32):
    """Custom type gs2310MLDSnoopingFastLeave based on Integer32"""
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


_Gs2310MLDSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingFastLeave_Object = MibTableColumn
gs2310MLDSnoopingFastLeave = _Gs2310MLDSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 6, 1, 2),
    _Gs2310MLDSnoopingFastLeave_Type()
)
gs2310MLDSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingFastLeave.setStatus("current")


class _Gs2310MLDSnoopingThrottling_Type(Integer32):
    """Custom type gs2310MLDSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2310MLDSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingThrottling_Object = MibTableColumn
gs2310MLDSnoopingThrottling = _Gs2310MLDSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 1, 6, 1, 3),
    _Gs2310MLDSnoopingThrottling_Type()
)
gs2310MLDSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingThrottling.setStatus("current")
_Gs2310MLDSnoopingVLANTable_Object = MibTable
gs2310MLDSnoopingVLANTable = _Gs2310MLDSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANTable.setStatus("current")
_Gs2310MLDSnoopingVLANEntry_Object = MibTableRow
gs2310MLDSnoopingVLANEntry = _Gs2310MLDSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1)
)
gs2310MLDSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MLDSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANEntry.setStatus("current")


class _Gs2310MLDSnoopingVLANID_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MLDSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANID_Object = MibTableColumn
gs2310MLDSnoopingVLANID = _Gs2310MLDSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 1),
    _Gs2310MLDSnoopingVLANID_Type()
)
gs2310MLDSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANID.setStatus("current")


class _Gs2310MLDSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANEnable based on Integer32"""
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


_Gs2310MLDSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANEnable_Object = MibTableColumn
gs2310MLDSnoopingVLANEnable = _Gs2310MLDSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 2),
    _Gs2310MLDSnoopingVLANEnable_Type()
)
gs2310MLDSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANEnable.setStatus("current")


class _Gs2310MLDSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANIGMPQuerier based on Integer32"""
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


_Gs2310MLDSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2310MLDSnoopingVLANIGMPQuerier = _Gs2310MLDSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 3),
    _Gs2310MLDSnoopingVLANIGMPQuerier_Type()
)
gs2310MLDSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2310MLDSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANCompatibility based on Integer32"""
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


_Gs2310MLDSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANCompatibility_Object = MibTableColumn
gs2310MLDSnoopingVLANCompatibility = _Gs2310MLDSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 4),
    _Gs2310MLDSnoopingVLANCompatibility_Type()
)
gs2310MLDSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANCompatibility.setStatus("current")


class _Gs2310MLDSnoopingVLANRV_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2310MLDSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANRV_Object = MibTableColumn
gs2310MLDSnoopingVLANRV = _Gs2310MLDSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 5),
    _Gs2310MLDSnoopingVLANRV_Type()
)
gs2310MLDSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANRV.setStatus("current")


class _Gs2310MLDSnoopingVLANQI_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2310MLDSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANQI_Object = MibTableColumn
gs2310MLDSnoopingVLANQI = _Gs2310MLDSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 6),
    _Gs2310MLDSnoopingVLANQI_Type()
)
gs2310MLDSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANQI.setStatus("current")


class _Gs2310MLDSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2310MLDSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANQRI_Object = MibTableColumn
gs2310MLDSnoopingVLANQRI = _Gs2310MLDSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 7),
    _Gs2310MLDSnoopingVLANQRI_Type()
)
gs2310MLDSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANQRI.setStatus("current")


class _Gs2310MLDSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2310MLDSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANLLQI_Object = MibTableColumn
gs2310MLDSnoopingVLANLLQI = _Gs2310MLDSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 8),
    _Gs2310MLDSnoopingVLANLLQI_Type()
)
gs2310MLDSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANLLQI.setStatus("current")


class _Gs2310MLDSnoopingVLANURI_Type(Integer32):
    """Custom type gs2310MLDSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2310MLDSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingVLANURI_Object = MibTableColumn
gs2310MLDSnoopingVLANURI = _Gs2310MLDSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 2, 1, 9),
    _Gs2310MLDSnoopingVLANURI_Type()
)
gs2310MLDSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingVLANURI.setStatus("current")
_Gs2310MLDSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2310MLDSnoopingPortGroupFiltering = _Gs2310MLDSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3)
)
_Gs2310MLDSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2310MLDSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2310MLDSnoopingPortGroupFilteringCreate = _Gs2310MLDSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 1),
    _Gs2310MLDSnoopingPortGroupFilteringCreate_Type()
)
gs2310MLDSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2310MLDSnoopingPortGroupFilteringTable_Object = MibTable
gs2310MLDSnoopingPortGroupFilteringTable = _Gs2310MLDSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2310MLDSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2310MLDSnoopingPortGroupFilteringEntry = _Gs2310MLDSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 2, 1)
)
gs2310MLDSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MLDSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2310MLDSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2310MLDSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MLDSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2310MLDSnoopingPortGroupFilteringIndex = _Gs2310MLDSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 2, 1, 1),
    _Gs2310MLDSnoopingPortGroupFilteringIndex_Type()
)
gs2310MLDSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2310MLDSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2310MLDSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MLDSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2310MLDSnoopingPortGroupFilteringPort = _Gs2310MLDSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 2, 1, 2),
    _Gs2310MLDSnoopingPortGroupFilteringPort_Type()
)
gs2310MLDSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2310MLDSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2310MLDSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2310MLDSnoopingPortGroupFilteringGroups = _Gs2310MLDSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 2, 1, 3),
    _Gs2310MLDSnoopingPortGroupFilteringGroups_Type()
)
gs2310MLDSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2310MLDSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2310MLDSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2310MLDSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2310MLDSnoopingPortGroupFilteringRowStatus = _Gs2310MLDSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 3, 2, 1, 4),
    _Gs2310MLDSnoopingPortGroupFilteringRowStatus_Type()
)
gs2310MLDSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2310MLDSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2310MLDSnoopingStatus = _Gs2310MLDSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4)
)


class _Gs2310MLDSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2310MLDSnoopingstatisticClear based on Integer32"""
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


_Gs2310MLDSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingstatisticClear_Object = MibScalar
gs2310MLDSnoopingstatisticClear = _Gs2310MLDSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 1),
    _Gs2310MLDSnoopingstatisticClear_Type()
)
gs2310MLDSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticClear.setStatus("current")
_Gs2310MLDSnoopingstatisticTable_Object = MibTable
gs2310MLDSnoopingstatisticTable = _Gs2310MLDSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticTable.setStatus("current")
_Gs2310MLDSnoopingstatisticEntry_Object = MibTableRow
gs2310MLDSnoopingstatisticEntry = _Gs2310MLDSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1)
)
gs2310MLDSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MLDSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticEntry.setStatus("current")


class _Gs2310MLDSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2310MLDSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MLDSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingstatisticVLANID_Object = MibTableColumn
gs2310MLDSnoopingstatisticVLANID = _Gs2310MLDSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 1),
    _Gs2310MLDSnoopingstatisticVLANID_Type()
)
gs2310MLDSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticVLANID.setStatus("current")
_Gs2310MLDSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2310MLDSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2310MLDSnoopingstatisticQuerierVersion = _Gs2310MLDSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 2),
    _Gs2310MLDSnoopingstatisticQuerierVersion_Type()
)
gs2310MLDSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2310MLDSnoopingstatisticHostVersion_Type = DisplayString
_Gs2310MLDSnoopingstatisticHostVersion_Object = MibTableColumn
gs2310MLDSnoopingstatisticHostVersion = _Gs2310MLDSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 3),
    _Gs2310MLDSnoopingstatisticHostVersion_Type()
)
gs2310MLDSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticHostVersion.setStatus("current")
_Gs2310MLDSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2310MLDSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2310MLDSnoopingstatisticQuerierStatus = _Gs2310MLDSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 4),
    _Gs2310MLDSnoopingstatisticQuerierStatus_Type()
)
gs2310MLDSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2310MLDSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2310MLDSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2310MLDSnoopingstatisticQueriesTransmitted = _Gs2310MLDSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 5),
    _Gs2310MLDSnoopingstatisticQueriesTransmitted_Type()
)
gs2310MLDSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2310MLDSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2310MLDSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2310MLDSnoopingstatisticQueriesReceived = _Gs2310MLDSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 6),
    _Gs2310MLDSnoopingstatisticQueriesReceived_Type()
)
gs2310MLDSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2310MLDSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2310MLDSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2310MLDSnoopingstatisticV1ReportsReceived = _Gs2310MLDSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 7),
    _Gs2310MLDSnoopingstatisticV1ReportsReceived_Type()
)
gs2310MLDSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2310MLDSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2310MLDSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2310MLDSnoopingstatisticV2ReportsReceived = _Gs2310MLDSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 8),
    _Gs2310MLDSnoopingstatisticV2ReportsReceived_Type()
)
gs2310MLDSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2310MLDSnoopingstatisticV1LeavesReceived_Type = Counter32
_Gs2310MLDSnoopingstatisticV1LeavesReceived_Object = MibTableColumn
gs2310MLDSnoopingstatisticV1LeavesReceived = _Gs2310MLDSnoopingstatisticV1LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 2, 1, 9),
    _Gs2310MLDSnoopingstatisticV1LeavesReceived_Type()
)
gs2310MLDSnoopingstatisticV1LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingstatisticV1LeavesReceived.setStatus("current")
_Gs2310MLDSnoopingRouterPortTable_Object = MibTable
gs2310MLDSnoopingRouterPortTable = _Gs2310MLDSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 3)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingRouterPortTable.setStatus("current")
_Gs2310MLDSnoopingRouterPortEntry_Object = MibTableRow
gs2310MLDSnoopingRouterPortEntry = _Gs2310MLDSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 3, 1)
)
gs2310MLDSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingRouterPortEntry.setStatus("current")
_Gs2310MLDSnoopingRouterPortStatus_Type = DisplayString
_Gs2310MLDSnoopingRouterPortStatus_Object = MibTableColumn
gs2310MLDSnoopingRouterPortStatus = _Gs2310MLDSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 4, 3, 1, 1),
    _Gs2310MLDSnoopingRouterPortStatus_Type()
)
gs2310MLDSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingRouterPortStatus.setStatus("current")
_Gs2310MLDSnoopingGroupsTable_Object = MibTable
gs2310MLDSnoopingGroupsTable = _Gs2310MLDSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 5)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingGroupsTable.setStatus("current")
_Gs2310MLDSnoopingGroupsEntry_Object = MibTableRow
gs2310MLDSnoopingGroupsEntry = _Gs2310MLDSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 5, 1)
)
gs2310MLDSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MLDSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingGroupsEntry.setStatus("current")


class _Gs2310MLDSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2310MLDSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MLDSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingGroupsIndex_Object = MibTableColumn
gs2310MLDSnoopingGroupsIndex = _Gs2310MLDSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 5, 1, 1),
    _Gs2310MLDSnoopingGroupsIndex_Type()
)
gs2310MLDSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingGroupsIndex.setStatus("current")


class _Gs2310MLDSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2310MLDSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MLDSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingGroupsVLANID_Object = MibTableColumn
gs2310MLDSnoopingGroupsVLANID = _Gs2310MLDSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 5, 1, 2),
    _Gs2310MLDSnoopingGroupsVLANID_Type()
)
gs2310MLDSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingGroupsVLANID.setStatus("current")
_Gs2310MLDSnoopingGroups_Type = DisplayString
_Gs2310MLDSnoopingGroups_Object = MibTableColumn
gs2310MLDSnoopingGroups = _Gs2310MLDSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 5, 1, 3),
    _Gs2310MLDSnoopingGroups_Type()
)
gs2310MLDSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingGroups.setStatus("current")
_Gs2310MLDSnoopingGroupsMemberships_Type = DisplayString
_Gs2310MLDSnoopingGroupsMemberships_Object = MibTableColumn
gs2310MLDSnoopingGroupsMemberships = _Gs2310MLDSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 5, 1, 4),
    _Gs2310MLDSnoopingGroupsMemberships_Type()
)
gs2310MLDSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingGroupsMemberships.setStatus("current")
_Gs2310MLDSnoopingSSMTable_Object = MibTable
gs2310MLDSnoopingSSMTable = _Gs2310MLDSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6)
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMTable.setStatus("current")
_Gs2310MLDSnoopingSSMEntry_Object = MibTableRow
gs2310MLDSnoopingSSMEntry = _Gs2310MLDSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1)
)
gs2310MLDSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MLDSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMEntry.setStatus("current")


class _Gs2310MLDSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2310MLDSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MLDSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingSSMIndex_Object = MibTableColumn
gs2310MLDSnoopingSSMIndex = _Gs2310MLDSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 1),
    _Gs2310MLDSnoopingSSMIndex_Type()
)
gs2310MLDSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMIndex.setStatus("current")


class _Gs2310MLDSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2310MLDSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MLDSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingSSMVLANID_Object = MibTableColumn
gs2310MLDSnoopingSSMVLANID = _Gs2310MLDSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 2),
    _Gs2310MLDSnoopingSSMVLANID_Type()
)
gs2310MLDSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMVLANID.setStatus("current")
_Gs2310MLDSnoopingSSMGroup_Type = DisplayString
_Gs2310MLDSnoopingSSMGroup_Object = MibTableColumn
gs2310MLDSnoopingSSMGroup = _Gs2310MLDSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 3),
    _Gs2310MLDSnoopingSSMGroup_Type()
)
gs2310MLDSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMGroup.setStatus("current")


class _Gs2310MLDSnoopingSSMPort_Type(Integer32):
    """Custom type gs2310MLDSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MLDSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2310MLDSnoopingSSMPort_Object = MibTableColumn
gs2310MLDSnoopingSSMPort = _Gs2310MLDSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 4),
    _Gs2310MLDSnoopingSSMPort_Type()
)
gs2310MLDSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMPort.setStatus("current")
_Gs2310MLDSnoopingSSMMode_Type = DisplayString
_Gs2310MLDSnoopingSSMMode_Object = MibTableColumn
gs2310MLDSnoopingSSMMode = _Gs2310MLDSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 5),
    _Gs2310MLDSnoopingSSMMode_Type()
)
gs2310MLDSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMMode.setStatus("current")
_Gs2310MLDSnoopingSSMSourceAddress_Type = DisplayString
_Gs2310MLDSnoopingSSMSourceAddress_Object = MibTableColumn
gs2310MLDSnoopingSSMSourceAddress = _Gs2310MLDSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 6),
    _Gs2310MLDSnoopingSSMSourceAddress_Type()
)
gs2310MLDSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMSourceAddress.setStatus("current")
_Gs2310MLDSnoopingSSMType_Type = DisplayString
_Gs2310MLDSnoopingSSMType_Object = MibTableColumn
gs2310MLDSnoopingSSMType = _Gs2310MLDSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 17, 6, 1, 7),
    _Gs2310MLDSnoopingSSMType_Type()
)
gs2310MLDSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MLDSnoopingSSMType.setStatus("current")
_Gs2310MVR_ObjectIdentity = ObjectIdentity
gs2310MVR = _Gs2310MVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18)
)
_Gs2310MVRConfiguration_ObjectIdentity = ObjectIdentity
gs2310MVRConfiguration = _Gs2310MVRConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1)
)


class _Gs2310MVRMode_Type(Integer32):
    """Custom type gs2310MVRMode based on Integer32"""
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


_Gs2310MVRMode_Type.__name__ = "Integer32"
_Gs2310MVRMode_Object = MibScalar
gs2310MVRMode = _Gs2310MVRMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 1),
    _Gs2310MVRMode_Type()
)
gs2310MVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRMode.setStatus("current")


class _Gs2310MVRVLANId_Type(Integer32):
    """Custom type gs2310MVRVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310MVRVLANId_Type.__name__ = "Integer32"
_Gs2310MVRVLANId_Object = MibScalar
gs2310MVRVLANId = _Gs2310MVRVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 2),
    _Gs2310MVRVLANId_Type()
)
gs2310MVRVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRVLANId.setStatus("current")
_Gs2310MVRPortConfigurationTable_Object = MibTable
gs2310MVRPortConfigurationTable = _Gs2310MVRPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 3)
)
if mibBuilder.loadTexts:
    gs2310MVRPortConfigurationTable.setStatus("current")
_Gs2310MVRPortConfigurationEntry_Object = MibTableRow
gs2310MVRPortConfigurationEntry = _Gs2310MVRPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 3, 1)
)
gs2310MVRPortConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2310MVRPortConfigurationEntry.setStatus("current")


class _Gs2310MVRPortConfigurationMode_Type(Integer32):
    """Custom type gs2310MVRPortConfigurationMode based on Integer32"""
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


_Gs2310MVRPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2310MVRPortConfigurationMode_Object = MibTableColumn
gs2310MVRPortConfigurationMode = _Gs2310MVRPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 3, 1, 1),
    _Gs2310MVRPortConfigurationMode_Type()
)
gs2310MVRPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortConfigurationMode.setStatus("current")


class _Gs2310MVRPortConfigurationType_Type(Integer32):
    """Custom type gs2310MVRPortConfigurationType based on Integer32"""
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


_Gs2310MVRPortConfigurationType_Type.__name__ = "Integer32"
_Gs2310MVRPortConfigurationType_Object = MibTableColumn
gs2310MVRPortConfigurationType = _Gs2310MVRPortConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 3, 1, 2),
    _Gs2310MVRPortConfigurationType_Type()
)
gs2310MVRPortConfigurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortConfigurationType.setStatus("current")


class _Gs2310MVRPortConfigurationImmediateLeave_Type(Integer32):
    """Custom type gs2310MVRPortConfigurationImmediateLeave based on Integer32"""
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


_Gs2310MVRPortConfigurationImmediateLeave_Type.__name__ = "Integer32"
_Gs2310MVRPortConfigurationImmediateLeave_Object = MibTableColumn
gs2310MVRPortConfigurationImmediateLeave = _Gs2310MVRPortConfigurationImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 1, 3, 1, 3),
    _Gs2310MVRPortConfigurationImmediateLeave_Type()
)
gs2310MVRPortConfigurationImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortConfigurationImmediateLeave.setStatus("current")
_Gs2310MVRPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2310MVRPortGroupFiltering = _Gs2310MVRPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2)
)
_Gs2310MVRPortGroupFilteringCreate_Type = Integer32
_Gs2310MVRPortGroupFilteringCreate_Object = MibScalar
gs2310MVRPortGroupFilteringCreate = _Gs2310MVRPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 1),
    _Gs2310MVRPortGroupFilteringCreate_Type()
)
gs2310MVRPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringCreate.setStatus("current")
_Gs2310MVRPortGroupFilteringTable_Object = MibTable
gs2310MVRPortGroupFilteringTable = _Gs2310MVRPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringTable.setStatus("current")
_Gs2310MVRPortGroupFilteringEntry_Object = MibTableRow
gs2310MVRPortGroupFilteringEntry = _Gs2310MVRPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2, 1)
)
gs2310MVRPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MVRPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringEntry.setStatus("current")


class _Gs2310MVRPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2310MVRPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MVRPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2310MVRPortGroupFilteringIndex_Object = MibTableColumn
gs2310MVRPortGroupFilteringIndex = _Gs2310MVRPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2, 1, 1),
    _Gs2310MVRPortGroupFilteringIndex_Type()
)
gs2310MVRPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringIndex.setStatus("current")


class _Gs2310MVRPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2310MVRPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MVRPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2310MVRPortGroupFilteringPort_Object = MibTableColumn
gs2310MVRPortGroupFilteringPort = _Gs2310MVRPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2, 1, 2),
    _Gs2310MVRPortGroupFilteringPort_Type()
)
gs2310MVRPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringPort.setStatus("current")
_Gs2310MVRPortGroupFilteringStartGroups_Type = DisplayString
_Gs2310MVRPortGroupFilteringStartGroups_Object = MibTableColumn
gs2310MVRPortGroupFilteringStartGroups = _Gs2310MVRPortGroupFilteringStartGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2, 1, 3),
    _Gs2310MVRPortGroupFilteringStartGroups_Type()
)
gs2310MVRPortGroupFilteringStartGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringStartGroups.setStatus("current")
_Gs2310MVRPortGroupFilteringEndGroups_Type = DisplayString
_Gs2310MVRPortGroupFilteringEndGroups_Object = MibTableColumn
gs2310MVRPortGroupFilteringEndGroups = _Gs2310MVRPortGroupFilteringEndGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2, 1, 4),
    _Gs2310MVRPortGroupFilteringEndGroups_Type()
)
gs2310MVRPortGroupFilteringEndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringEndGroups.setStatus("current")


class _Gs2310MVRPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2310MVRPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2310MVRPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2310MVRPortGroupFilteringRowStatus_Object = MibTableColumn
gs2310MVRPortGroupFilteringRowStatus = _Gs2310MVRPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 2, 2, 1, 5),
    _Gs2310MVRPortGroupFilteringRowStatus_Type()
)
gs2310MVRPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRPortGroupFilteringRowStatus.setStatus("current")
_Gs2310MVRGroupsTable_Object = MibTable
gs2310MVRGroupsTable = _Gs2310MVRGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gs2310MVRGroupsTable.setStatus("current")
_Gs2310MVRGroupsEntry_Object = MibTableRow
gs2310MVRGroupsEntry = _Gs2310MVRGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 3, 1)
)
gs2310MVRGroupsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MVRGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2310MVRGroupsEntry.setStatus("current")


class _Gs2310MVRGroupsIndex_Type(Integer32):
    """Custom type gs2310MVRGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310MVRGroupsIndex_Type.__name__ = "Integer32"
_Gs2310MVRGroupsIndex_Object = MibTableColumn
gs2310MVRGroupsIndex = _Gs2310MVRGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 3, 1, 1),
    _Gs2310MVRGroupsIndex_Type()
)
gs2310MVRGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MVRGroupsIndex.setStatus("current")


class _Gs2310MVRGroupsVLANID_Type(Integer32):
    """Custom type gs2310MVRGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MVRGroupsVLANID_Type.__name__ = "Integer32"
_Gs2310MVRGroupsVLANID_Object = MibTableColumn
gs2310MVRGroupsVLANID = _Gs2310MVRGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 3, 1, 2),
    _Gs2310MVRGroupsVLANID_Type()
)
gs2310MVRGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRGroupsVLANID.setStatus("current")
_Gs2310MVRGroups_Type = DisplayString
_Gs2310MVRGroups_Object = MibTableColumn
gs2310MVRGroups = _Gs2310MVRGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 3, 1, 3),
    _Gs2310MVRGroups_Type()
)
gs2310MVRGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRGroups.setStatus("current")
_Gs2310MVRGroupsMemberships_Type = DisplayString
_Gs2310MVRGroupsMemberships_Object = MibTableColumn
gs2310MVRGroupsMemberships = _Gs2310MVRGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 3, 1, 4),
    _Gs2310MVRGroupsMemberships_Type()
)
gs2310MVRGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRGroupsMemberships.setStatus("current")
_Gs2310MVRStatus_ObjectIdentity = ObjectIdentity
gs2310MVRStatus = _Gs2310MVRStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4)
)


class _Gs2310MVRstatisticClear_Type(Integer32):
    """Custom type gs2310MVRstatisticClear based on Integer32"""
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


_Gs2310MVRstatisticClear_Type.__name__ = "Integer32"
_Gs2310MVRstatisticClear_Object = MibScalar
gs2310MVRstatisticClear = _Gs2310MVRstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4, 1),
    _Gs2310MVRstatisticClear_Type()
)
gs2310MVRstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310MVRstatisticClear.setStatus("current")


class _Gs2310MVRstatisticVLANID_Type(Integer32):
    """Custom type gs2310MVRstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MVRstatisticVLANID_Type.__name__ = "Integer32"
_Gs2310MVRstatisticVLANID_Object = MibScalar
gs2310MVRstatisticVLANID = _Gs2310MVRstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4, 2),
    _Gs2310MVRstatisticVLANID_Type()
)
gs2310MVRstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRstatisticVLANID.setStatus("current")
_Gs2310MVRstatisticV1ReportsReceived_Type = Counter32
_Gs2310MVRstatisticV1ReportsReceived_Object = MibScalar
gs2310MVRstatisticV1ReportsReceived = _Gs2310MVRstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4, 3),
    _Gs2310MVRstatisticV1ReportsReceived_Type()
)
gs2310MVRstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRstatisticV1ReportsReceived.setStatus("current")
_Gs2310MVRstatisticV2ReportsReceived_Type = Counter32
_Gs2310MVRstatisticV2ReportsReceived_Object = MibScalar
gs2310MVRstatisticV2ReportsReceived = _Gs2310MVRstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4, 4),
    _Gs2310MVRstatisticV2ReportsReceived_Type()
)
gs2310MVRstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRstatisticV2ReportsReceived.setStatus("current")
_Gs2310MVRstatisticV3ReportsReceived_Type = Counter32
_Gs2310MVRstatisticV3ReportsReceived_Object = MibScalar
gs2310MVRstatisticV3ReportsReceived = _Gs2310MVRstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4, 5),
    _Gs2310MVRstatisticV3ReportsReceived_Type()
)
gs2310MVRstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRstatisticV3ReportsReceived.setStatus("current")
_Gs2310MVRstatisticV2LeavesReceived_Type = Counter32
_Gs2310MVRstatisticV2LeavesReceived_Object = MibScalar
gs2310MVRstatisticV2LeavesReceived = _Gs2310MVRstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 18, 4, 6),
    _Gs2310MVRstatisticV2LeavesReceived_Type()
)
gs2310MVRstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MVRstatisticV2LeavesReceived.setStatus("current")
_Gs2310LACP_ObjectIdentity = ObjectIdentity
gs2310LACP = _Gs2310LACP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19)
)
_Gs2310LACPConf_ObjectIdentity = ObjectIdentity
gs2310LACPConf = _Gs2310LACPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1)
)
_Gs2310LACPPortConfigurationTable_Object = MibTable
gs2310LACPPortConfigurationTable = _Gs2310LACPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    gs2310LACPPortConfigurationTable.setStatus("current")
_Gs2310LACPPortConfigurationEntry_Object = MibTableRow
gs2310LACPPortConfigurationEntry = _Gs2310LACPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1, 1, 1)
)
gs2310LACPPortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310LACPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2310LACPPortConfigurationEntry.setStatus("current")


class _Gs2310LACPPortConfigurationPort_Type(Integer32):
    """Custom type gs2310LACPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310LACPPortConfigurationPort_Type.__name__ = "Integer32"
_Gs2310LACPPortConfigurationPort_Object = MibTableColumn
gs2310LACPPortConfigurationPort = _Gs2310LACPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1, 1, 1, 1),
    _Gs2310LACPPortConfigurationPort_Type()
)
gs2310LACPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310LACPPortConfigurationPort.setStatus("current")


class _Gs2310LACPPortConfigurationMode_Type(Integer32):
    """Custom type gs2310LACPPortConfigurationMode based on Integer32"""
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


_Gs2310LACPPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2310LACPPortConfigurationMode_Object = MibTableColumn
gs2310LACPPortConfigurationMode = _Gs2310LACPPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1, 1, 1, 2),
    _Gs2310LACPPortConfigurationMode_Type()
)
gs2310LACPPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LACPPortConfigurationMode.setStatus("current")


class _Gs2310LACPPortConfigurationKey_Type(Integer32):
    """Custom type gs2310LACPPortConfigurationKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2310LACPPortConfigurationKey_Type.__name__ = "Integer32"
_Gs2310LACPPortConfigurationKey_Object = MibTableColumn
gs2310LACPPortConfigurationKey = _Gs2310LACPPortConfigurationKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1, 1, 1, 3),
    _Gs2310LACPPortConfigurationKey_Type()
)
gs2310LACPPortConfigurationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LACPPortConfigurationKey.setStatus("current")


class _Gs2310LACPPortConfigurationRole_Type(Integer32):
    """Custom type gs2310LACPPortConfigurationRole based on Integer32"""
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


_Gs2310LACPPortConfigurationRole_Type.__name__ = "Integer32"
_Gs2310LACPPortConfigurationRole_Object = MibTableColumn
gs2310LACPPortConfigurationRole = _Gs2310LACPPortConfigurationRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 1, 1, 1, 4),
    _Gs2310LACPPortConfigurationRole_Type()
)
gs2310LACPPortConfigurationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LACPPortConfigurationRole.setStatus("current")
_Gs2310LACPSystemStatusTable_Object = MibTable
gs2310LACPSystemStatusTable = _Gs2310LACPSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusTable.setStatus("current")
_Gs2310LACPSystemStatusEntry_Object = MibTableRow
gs2310LACPSystemStatusEntry = _Gs2310LACPSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1)
)
gs2310LACPSystemStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310LACPSystemStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusEntry.setStatus("current")


class _Gs2310LACPSystemStatusIndex_Type(Integer32):
    """Custom type gs2310LACPSystemStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2310LACPSystemStatusIndex_Type.__name__ = "Integer32"
_Gs2310LACPSystemStatusIndex_Object = MibTableColumn
gs2310LACPSystemStatusIndex = _Gs2310LACPSystemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1, 1),
    _Gs2310LACPSystemStatusIndex_Type()
)
gs2310LACPSystemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusIndex.setStatus("current")
_Gs2310LACPSystemStatusAggrID_Type = DisplayString
_Gs2310LACPSystemStatusAggrID_Object = MibTableColumn
gs2310LACPSystemStatusAggrID = _Gs2310LACPSystemStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1, 2),
    _Gs2310LACPSystemStatusAggrID_Type()
)
gs2310LACPSystemStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusAggrID.setStatus("current")
_Gs2310LACPSystemStatusPartnerSystemID_Type = MacAddress
_Gs2310LACPSystemStatusPartnerSystemID_Object = MibTableColumn
gs2310LACPSystemStatusPartnerSystemID = _Gs2310LACPSystemStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1, 3),
    _Gs2310LACPSystemStatusPartnerSystemID_Type()
)
gs2310LACPSystemStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusPartnerSystemID.setStatus("current")
_Gs2310LACPSystemStatusPartnerKey_Type = DisplayString
_Gs2310LACPSystemStatusPartnerKey_Object = MibTableColumn
gs2310LACPSystemStatusPartnerKey = _Gs2310LACPSystemStatusPartnerKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1, 4),
    _Gs2310LACPSystemStatusPartnerKey_Type()
)
gs2310LACPSystemStatusPartnerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusPartnerKey.setStatus("current")
_Gs2310LACPSystemStatusLastchanged_Type = DisplayString
_Gs2310LACPSystemStatusLastchanged_Object = MibTableColumn
gs2310LACPSystemStatusLastchanged = _Gs2310LACPSystemStatusLastchanged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1, 5),
    _Gs2310LACPSystemStatusLastchanged_Type()
)
gs2310LACPSystemStatusLastchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusLastchanged.setStatus("current")
_Gs2310LACPSystemStatusLocalPorts_Type = DisplayString
_Gs2310LACPSystemStatusLocalPorts_Object = MibTableColumn
gs2310LACPSystemStatusLocalPorts = _Gs2310LACPSystemStatusLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 2, 1, 6),
    _Gs2310LACPSystemStatusLocalPorts_Type()
)
gs2310LACPSystemStatusLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPSystemStatusLocalPorts.setStatus("current")
_Gs2310LACPStatusTable_Object = MibTable
gs2310LACPStatusTable = _Gs2310LACPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gs2310LACPStatusTable.setStatus("current")
_Gs2310LACPStatusEntry_Object = MibTableRow
gs2310LACPStatusEntry = _Gs2310LACPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1)
)
gs2310LACPStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310LACPStatusPort"),
)
if mibBuilder.loadTexts:
    gs2310LACPStatusEntry.setStatus("current")


class _Gs2310LACPStatusPort_Type(Integer32):
    """Custom type gs2310LACPStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310LACPStatusPort_Type.__name__ = "Integer32"
_Gs2310LACPStatusPort_Object = MibTableColumn
gs2310LACPStatusPort = _Gs2310LACPStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1, 1),
    _Gs2310LACPStatusPort_Type()
)
gs2310LACPStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310LACPStatusPort.setStatus("current")
_Gs2310LACPStatusLACP_Type = DisplayString
_Gs2310LACPStatusLACP_Object = MibTableColumn
gs2310LACPStatusLACP = _Gs2310LACPStatusLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1, 2),
    _Gs2310LACPStatusLACP_Type()
)
gs2310LACPStatusLACP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPStatusLACP.setStatus("current")
_Gs2310LACPStatusKey_Type = DisplayString
_Gs2310LACPStatusKey_Object = MibTableColumn
gs2310LACPStatusKey = _Gs2310LACPStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1, 3),
    _Gs2310LACPStatusKey_Type()
)
gs2310LACPStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPStatusKey.setStatus("current")
_Gs2310LACPStatusAggrID_Type = DisplayString
_Gs2310LACPStatusAggrID_Object = MibTableColumn
gs2310LACPStatusAggrID = _Gs2310LACPStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1, 4),
    _Gs2310LACPStatusAggrID_Type()
)
gs2310LACPStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPStatusAggrID.setStatus("current")
_Gs2310LACPStatusPartnerSystemID_Type = DisplayString
_Gs2310LACPStatusPartnerSystemID_Object = MibTableColumn
gs2310LACPStatusPartnerSystemID = _Gs2310LACPStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1, 5),
    _Gs2310LACPStatusPartnerSystemID_Type()
)
gs2310LACPStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPStatusPartnerSystemID.setStatus("current")
_Gs2310LACPStatusPartnerPort_Type = DisplayString
_Gs2310LACPStatusPartnerPort_Object = MibTableColumn
gs2310LACPStatusPartnerPort = _Gs2310LACPStatusPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 3, 1, 6),
    _Gs2310LACPStatusPartnerPort_Type()
)
gs2310LACPStatusPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPStatusPartnerPort.setStatus("current")
_Gs2310LACPStatisticsTable_Object = MibTable
gs2310LACPStatisticsTable = _Gs2310LACPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4)
)
if mibBuilder.loadTexts:
    gs2310LACPStatisticsTable.setStatus("current")
_Gs2310LACPStatisticsEntry_Object = MibTableRow
gs2310LACPStatisticsEntry = _Gs2310LACPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4, 1)
)
gs2310LACPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310LACPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2310LACPStatisticsEntry.setStatus("current")


class _Gs2310LACPStatisticsPort_Type(Integer32):
    """Custom type gs2310LACPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310LACPStatisticsPort_Type.__name__ = "Integer32"
_Gs2310LACPStatisticsPort_Object = MibTableColumn
gs2310LACPStatisticsPort = _Gs2310LACPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4, 1, 1),
    _Gs2310LACPStatisticsPort_Type()
)
gs2310LACPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310LACPStatisticsPort.setStatus("current")
_Gs2310LACPReceived_Type = Counter32
_Gs2310LACPReceived_Object = MibTableColumn
gs2310LACPReceived = _Gs2310LACPReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4, 1, 2),
    _Gs2310LACPReceived_Type()
)
gs2310LACPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPReceived.setStatus("current")
_Gs2310LACPTransmitted_Type = Counter32
_Gs2310LACPTransmitted_Object = MibTableColumn
gs2310LACPTransmitted = _Gs2310LACPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4, 1, 3),
    _Gs2310LACPTransmitted_Type()
)
gs2310LACPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPTransmitted.setStatus("current")
_Gs2310LACPDiscardedUnknown_Type = Counter32
_Gs2310LACPDiscardedUnknown_Object = MibTableColumn
gs2310LACPDiscardedUnknown = _Gs2310LACPDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4, 1, 4),
    _Gs2310LACPDiscardedUnknown_Type()
)
gs2310LACPDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPDiscardedUnknown.setStatus("current")
_Gs2310LACPDiscardedIllegal_Type = Counter32
_Gs2310LACPDiscardedIllegal_Object = MibTableColumn
gs2310LACPDiscardedIllegal = _Gs2310LACPDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 4, 1, 5),
    _Gs2310LACPDiscardedIllegal_Type()
)
gs2310LACPDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LACPDiscardedIllegal.setStatus("current")


class _Gs2310LACPStatisticsClear_Type(Integer32):
    """Custom type gs2310LACPStatisticsClear based on Integer32"""
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


_Gs2310LACPStatisticsClear_Type.__name__ = "Integer32"
_Gs2310LACPStatisticsClear_Object = MibScalar
gs2310LACPStatisticsClear = _Gs2310LACPStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 19, 5),
    _Gs2310LACPStatisticsClear_Type()
)
gs2310LACPStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LACPStatisticsClear.setStatus("current")
_Gs2310STP_ObjectIdentity = ObjectIdentity
gs2310STP = _Gs2310STP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20)
)
_Gs2310STPBridgeBasicConf_ObjectIdentity = ObjectIdentity
gs2310STPBridgeBasicConf = _Gs2310STPBridgeBasicConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1)
)


class _Gs2310STPBridgeProtocolVersion_Type(Integer32):
    """Custom type gs2310STPBridgeProtocolVersion based on Integer32"""
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


_Gs2310STPBridgeProtocolVersion_Type.__name__ = "Integer32"
_Gs2310STPBridgeProtocolVersion_Object = MibScalar
gs2310STPBridgeProtocolVersion = _Gs2310STPBridgeProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1, 1),
    _Gs2310STPBridgeProtocolVersion_Type()
)
gs2310STPBridgeProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeProtocolVersion.setStatus("current")


class _Gs2310STPBridgePriority_Type(Integer32):
    """Custom type gs2310STPBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPBridgePriority_Type.__name__ = "Integer32"
_Gs2310STPBridgePriority_Object = MibScalar
gs2310STPBridgePriority = _Gs2310STPBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1, 2),
    _Gs2310STPBridgePriority_Type()
)
gs2310STPBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgePriority.setStatus("current")


class _Gs2310STPBridgeForwardDelay_Type(Integer32):
    """Custom type gs2310STPBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Gs2310STPBridgeForwardDelay_Type.__name__ = "Integer32"
_Gs2310STPBridgeForwardDelay_Object = MibScalar
gs2310STPBridgeForwardDelay = _Gs2310STPBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1, 3),
    _Gs2310STPBridgeForwardDelay_Type()
)
gs2310STPBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeForwardDelay.setStatus("current")


class _Gs2310STPBridgeMaxAge_Type(Integer32):
    """Custom type gs2310STPBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2310STPBridgeMaxAge_Type.__name__ = "Integer32"
_Gs2310STPBridgeMaxAge_Object = MibScalar
gs2310STPBridgeMaxAge = _Gs2310STPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1, 4),
    _Gs2310STPBridgeMaxAge_Type()
)
gs2310STPBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeMaxAge.setStatus("current")


class _Gs2310STPBridgeMaximumHopCount_Type(Integer32):
    """Custom type gs2310STPBridgeMaximumHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2310STPBridgeMaximumHopCount_Type.__name__ = "Integer32"
_Gs2310STPBridgeMaximumHopCount_Object = MibScalar
gs2310STPBridgeMaximumHopCount = _Gs2310STPBridgeMaximumHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1, 5),
    _Gs2310STPBridgeMaximumHopCount_Type()
)
gs2310STPBridgeMaximumHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeMaximumHopCount.setStatus("current")


class _Gs2310STPBridgeTransmitHoldCount_Type(Integer32):
    """Custom type gs2310STPBridgeTransmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2310STPBridgeTransmitHoldCount_Type.__name__ = "Integer32"
_Gs2310STPBridgeTransmitHoldCount_Object = MibScalar
gs2310STPBridgeTransmitHoldCount = _Gs2310STPBridgeTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 1, 6),
    _Gs2310STPBridgeTransmitHoldCount_Type()
)
gs2310STPBridgeTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeTransmitHoldCount.setStatus("current")
_Gs2310STPBridgeAdvancedConf_ObjectIdentity = ObjectIdentity
gs2310STPBridgeAdvancedConf = _Gs2310STPBridgeAdvancedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 2)
)


class _Gs2310STPBridgeEdgePortBPDUFiltering_Type(Integer32):
    """Custom type gs2310STPBridgeEdgePortBPDUFiltering based on Integer32"""
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


_Gs2310STPBridgeEdgePortBPDUFiltering_Type.__name__ = "Integer32"
_Gs2310STPBridgeEdgePortBPDUFiltering_Object = MibScalar
gs2310STPBridgeEdgePortBPDUFiltering = _Gs2310STPBridgeEdgePortBPDUFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 2, 1),
    _Gs2310STPBridgeEdgePortBPDUFiltering_Type()
)
gs2310STPBridgeEdgePortBPDUFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeEdgePortBPDUFiltering.setStatus("current")


class _Gs2310STPBridgeEdgePortBPDUGuard_Type(Integer32):
    """Custom type gs2310STPBridgeEdgePortBPDUGuard based on Integer32"""
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


_Gs2310STPBridgeEdgePortBPDUGuard_Type.__name__ = "Integer32"
_Gs2310STPBridgeEdgePortBPDUGuard_Object = MibScalar
gs2310STPBridgeEdgePortBPDUGuard = _Gs2310STPBridgeEdgePortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 2, 2),
    _Gs2310STPBridgeEdgePortBPDUGuard_Type()
)
gs2310STPBridgeEdgePortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgeEdgePortBPDUGuard.setStatus("current")


class _Gs2310STPBridgePortErrorRecoveryTimeout_Type(Integer32):
    """Custom type gs2310STPBridgePortErrorRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Gs2310STPBridgePortErrorRecoveryTimeout_Type.__name__ = "Integer32"
_Gs2310STPBridgePortErrorRecoveryTimeout_Object = MibScalar
gs2310STPBridgePortErrorRecoveryTimeout = _Gs2310STPBridgePortErrorRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 2, 3),
    _Gs2310STPBridgePortErrorRecoveryTimeout_Type()
)
gs2310STPBridgePortErrorRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPBridgePortErrorRecoveryTimeout.setStatus("current")
_Gs2310STPMSTIConf_ObjectIdentity = ObjectIdentity
gs2310STPMSTIConf = _Gs2310STPMSTIConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 3)
)


class _Gs2310STPMSTIConfigurationName_Type(DisplayString):
    """Custom type gs2310STPMSTIConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2310STPMSTIConfigurationName_Type.__name__ = "DisplayString"
_Gs2310STPMSTIConfigurationName_Object = MibScalar
gs2310STPMSTIConfigurationName = _Gs2310STPMSTIConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 3, 1),
    _Gs2310STPMSTIConfigurationName_Type()
)
gs2310STPMSTIConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTIConfigurationName.setStatus("current")


class _Gs2310STPMSTIConfigurationRevision_Type(Integer32):
    """Custom type gs2310STPMSTIConfigurationRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2310STPMSTIConfigurationRevision_Type.__name__ = "Integer32"
_Gs2310STPMSTIConfigurationRevision_Object = MibScalar
gs2310STPMSTIConfigurationRevision = _Gs2310STPMSTIConfigurationRevision_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 3, 2),
    _Gs2310STPMSTIConfigurationRevision_Type()
)
gs2310STPMSTIConfigurationRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTIConfigurationRevision.setStatus("current")
_Gs2310STPMSTIMappingConf_ObjectIdentity = ObjectIdentity
gs2310STPMSTIMappingConf = _Gs2310STPMSTIMappingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4)
)


class _Gs2310STPMSTI1VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI1VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI1VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI1VLANsMapped_Object = MibScalar
gs2310STPMSTI1VLANsMapped = _Gs2310STPMSTI1VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 1),
    _Gs2310STPMSTI1VLANsMapped_Type()
)
gs2310STPMSTI1VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI1VLANsMapped.setStatus("current")


class _Gs2310STPMSTI2VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI2VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI2VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI2VLANsMapped_Object = MibScalar
gs2310STPMSTI2VLANsMapped = _Gs2310STPMSTI2VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 2),
    _Gs2310STPMSTI2VLANsMapped_Type()
)
gs2310STPMSTI2VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI2VLANsMapped.setStatus("current")


class _Gs2310STPMSTI3VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI3VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI3VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI3VLANsMapped_Object = MibScalar
gs2310STPMSTI3VLANsMapped = _Gs2310STPMSTI3VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 3),
    _Gs2310STPMSTI3VLANsMapped_Type()
)
gs2310STPMSTI3VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI3VLANsMapped.setStatus("current")


class _Gs2310STPMSTI4VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI4VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI4VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI4VLANsMapped_Object = MibScalar
gs2310STPMSTI4VLANsMapped = _Gs2310STPMSTI4VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 4),
    _Gs2310STPMSTI4VLANsMapped_Type()
)
gs2310STPMSTI4VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI4VLANsMapped.setStatus("current")


class _Gs2310STPMSTI5VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI5VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI5VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI5VLANsMapped_Object = MibScalar
gs2310STPMSTI5VLANsMapped = _Gs2310STPMSTI5VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 5),
    _Gs2310STPMSTI5VLANsMapped_Type()
)
gs2310STPMSTI5VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI5VLANsMapped.setStatus("current")


class _Gs2310STPMSTI6VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI6VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI6VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI6VLANsMapped_Object = MibScalar
gs2310STPMSTI6VLANsMapped = _Gs2310STPMSTI6VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 6),
    _Gs2310STPMSTI6VLANsMapped_Type()
)
gs2310STPMSTI6VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI6VLANsMapped.setStatus("current")


class _Gs2310STPMSTI7VLANsMapped_Type(DisplayString):
    """Custom type gs2310STPMSTI7VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2310STPMSTI7VLANsMapped_Type.__name__ = "DisplayString"
_Gs2310STPMSTI7VLANsMapped_Object = MibScalar
gs2310STPMSTI7VLANsMapped = _Gs2310STPMSTI7VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 4, 7),
    _Gs2310STPMSTI7VLANsMapped_Type()
)
gs2310STPMSTI7VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI7VLANsMapped.setStatus("current")
_Gs2310STPMSTIPriority_ObjectIdentity = ObjectIdentity
gs2310STPMSTIPriority = _Gs2310STPMSTIPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5)
)


class _Gs2310STPCISTPriority_Type(Integer32):
    """Custom type gs2310STPCISTPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPCISTPriority_Type.__name__ = "Integer32"
_Gs2310STPCISTPriority_Object = MibScalar
gs2310STPCISTPriority = _Gs2310STPCISTPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 1),
    _Gs2310STPCISTPriority_Type()
)
gs2310STPCISTPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTPriority.setStatus("current")


class _Gs2310STPMSTI1Priority_Type(Integer32):
    """Custom type gs2310STPMSTI1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI1Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI1Priority_Object = MibScalar
gs2310STPMSTI1Priority = _Gs2310STPMSTI1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 2),
    _Gs2310STPMSTI1Priority_Type()
)
gs2310STPMSTI1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI1Priority.setStatus("current")


class _Gs2310STPMSTI2Priority_Type(Integer32):
    """Custom type gs2310STPMSTI2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI2Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI2Priority_Object = MibScalar
gs2310STPMSTI2Priority = _Gs2310STPMSTI2Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 3),
    _Gs2310STPMSTI2Priority_Type()
)
gs2310STPMSTI2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI2Priority.setStatus("current")


class _Gs2310STPMSTI3Priority_Type(Integer32):
    """Custom type gs2310STPMSTI3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI3Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI3Priority_Object = MibScalar
gs2310STPMSTI3Priority = _Gs2310STPMSTI3Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 4),
    _Gs2310STPMSTI3Priority_Type()
)
gs2310STPMSTI3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI3Priority.setStatus("current")


class _Gs2310STPMSTI4Priority_Type(Integer32):
    """Custom type gs2310STPMSTI4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI4Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI4Priority_Object = MibScalar
gs2310STPMSTI4Priority = _Gs2310STPMSTI4Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 5),
    _Gs2310STPMSTI4Priority_Type()
)
gs2310STPMSTI4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI4Priority.setStatus("current")


class _Gs2310STPMSTI5Priority_Type(Integer32):
    """Custom type gs2310STPMSTI5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI5Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI5Priority_Object = MibScalar
gs2310STPMSTI5Priority = _Gs2310STPMSTI5Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 6),
    _Gs2310STPMSTI5Priority_Type()
)
gs2310STPMSTI5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI5Priority.setStatus("current")


class _Gs2310STPMSTI6Priority_Type(Integer32):
    """Custom type gs2310STPMSTI6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI6Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI6Priority_Object = MibScalar
gs2310STPMSTI6Priority = _Gs2310STPMSTI6Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 7),
    _Gs2310STPMSTI6Priority_Type()
)
gs2310STPMSTI6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI6Priority.setStatus("current")


class _Gs2310STPMSTI7Priority_Type(Integer32):
    """Custom type gs2310STPMSTI7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2310STPMSTI7Priority_Type.__name__ = "Integer32"
_Gs2310STPMSTI7Priority_Object = MibScalar
gs2310STPMSTI7Priority = _Gs2310STPMSTI7Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 5, 8),
    _Gs2310STPMSTI7Priority_Type()
)
gs2310STPMSTI7Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI7Priority.setStatus("current")
_Gs2310STPCISTPort_ObjectIdentity = ObjectIdentity
gs2310STPCISTPort = _Gs2310STPCISTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6)
)
_Gs2310STPCISTAggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPCISTAggregatedPort = _Gs2310STPCISTAggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1)
)


class _Gs2310STPCISTAggregatedPortSTPEnabled_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortSTPEnabled based on Integer32"""
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


_Gs2310STPCISTAggregatedPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortSTPEnabled_Object = MibScalar
gs2310STPCISTAggregatedPortSTPEnabled = _Gs2310STPCISTAggregatedPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 1),
    _Gs2310STPCISTAggregatedPortSTPEnabled_Type()
)
gs2310STPCISTAggregatedPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortSTPEnabled.setStatus("current")


class _Gs2310STPCISTAggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPCISTAggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortPathCost_Object = MibScalar
gs2310STPCISTAggregatedPortPathCost = _Gs2310STPCISTAggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 2),
    _Gs2310STPCISTAggregatedPortPathCost_Type()
)
gs2310STPCISTAggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortPathCost.setStatus("current")


class _Gs2310STPCISTAggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPCISTAggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortPriority_Object = MibScalar
gs2310STPCISTAggregatedPortPriority = _Gs2310STPCISTAggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 3),
    _Gs2310STPCISTAggregatedPortPriority_Type()
)
gs2310STPCISTAggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortPriority.setStatus("current")


class _Gs2310STPCISTAggregatedPortAdminEdge_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortAdminEdge based on Integer32"""
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


_Gs2310STPCISTAggregatedPortAdminEdge_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortAdminEdge_Object = MibScalar
gs2310STPCISTAggregatedPortAdminEdge = _Gs2310STPCISTAggregatedPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 4),
    _Gs2310STPCISTAggregatedPortAdminEdge_Type()
)
gs2310STPCISTAggregatedPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortAdminEdge.setStatus("current")


class _Gs2310STPCISTAggregatedPortAutoEdge_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortAutoEdge based on Integer32"""
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


_Gs2310STPCISTAggregatedPortAutoEdge_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortAutoEdge_Object = MibScalar
gs2310STPCISTAggregatedPortAutoEdge = _Gs2310STPCISTAggregatedPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 5),
    _Gs2310STPCISTAggregatedPortAutoEdge_Type()
)
gs2310STPCISTAggregatedPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortAutoEdge.setStatus("current")


class _Gs2310STPCISTAggregatedPortRestrictedRole_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortRestrictedRole based on Integer32"""
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


_Gs2310STPCISTAggregatedPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortRestrictedRole_Object = MibScalar
gs2310STPCISTAggregatedPortRestrictedRole = _Gs2310STPCISTAggregatedPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 6),
    _Gs2310STPCISTAggregatedPortRestrictedRole_Type()
)
gs2310STPCISTAggregatedPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortRestrictedRole.setStatus("current")


class _Gs2310STPCISTAggregatedPortRestrictedTCN_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortRestrictedTCN based on Integer32"""
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


_Gs2310STPCISTAggregatedPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortRestrictedTCN_Object = MibScalar
gs2310STPCISTAggregatedPortRestrictedTCN = _Gs2310STPCISTAggregatedPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 7),
    _Gs2310STPCISTAggregatedPortRestrictedTCN_Type()
)
gs2310STPCISTAggregatedPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortRestrictedTCN.setStatus("current")


class _Gs2310STPCISTAggregatedPortBPDUGuard_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortBPDUGuard based on Integer32"""
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


_Gs2310STPCISTAggregatedPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortBPDUGuard_Object = MibScalar
gs2310STPCISTAggregatedPortBPDUGuard = _Gs2310STPCISTAggregatedPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 8),
    _Gs2310STPCISTAggregatedPortBPDUGuard_Type()
)
gs2310STPCISTAggregatedPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortBPDUGuard.setStatus("current")


class _Gs2310STPCISTAggregatedPortPointtoPoint_Type(Integer32):
    """Custom type gs2310STPCISTAggregatedPortPointtoPoint based on Integer32"""
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


_Gs2310STPCISTAggregatedPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2310STPCISTAggregatedPortPointtoPoint_Object = MibScalar
gs2310STPCISTAggregatedPortPointtoPoint = _Gs2310STPCISTAggregatedPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 1, 9),
    _Gs2310STPCISTAggregatedPortPointtoPoint_Type()
)
gs2310STPCISTAggregatedPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTAggregatedPortPointtoPoint.setStatus("current")
_Gs2310STPCISTNormalPortTable_Object = MibTable
gs2310STPCISTNormalPortTable = _Gs2310STPCISTNormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2)
)
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortTable.setStatus("current")
_Gs2310STPCISTNormalPortEntry_Object = MibTableRow
gs2310STPCISTNormalPortEntry = _Gs2310STPCISTNormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1)
)
gs2310STPCISTNormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPCISTNormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortEntry.setStatus("current")


class _Gs2310STPCISTNormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPCISTNormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortConfPort_Object = MibTableColumn
gs2310STPCISTNormalPortConfPort = _Gs2310STPCISTNormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 1),
    _Gs2310STPCISTNormalPortConfPort_Type()
)
gs2310STPCISTNormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortConfPort.setStatus("current")


class _Gs2310STPCISTNormalPortSTPEnabled_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortSTPEnabled based on Integer32"""
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


_Gs2310STPCISTNormalPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortSTPEnabled_Object = MibTableColumn
gs2310STPCISTNormalPortSTPEnabled = _Gs2310STPCISTNormalPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 2),
    _Gs2310STPCISTNormalPortSTPEnabled_Type()
)
gs2310STPCISTNormalPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortSTPEnabled.setStatus("current")


class _Gs2310STPCISTNormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPCISTNormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortPathCost_Object = MibTableColumn
gs2310STPCISTNormalPortPathCost = _Gs2310STPCISTNormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 3),
    _Gs2310STPCISTNormalPortPathCost_Type()
)
gs2310STPCISTNormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortPathCost.setStatus("current")


class _Gs2310STPCISTNormalPortPriority_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPCISTNormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortPriority_Object = MibTableColumn
gs2310STPCISTNormalPortPriority = _Gs2310STPCISTNormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 4),
    _Gs2310STPCISTNormalPortPriority_Type()
)
gs2310STPCISTNormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortPriority.setStatus("current")


class _Gs2310STPCISTNormalPortAdminEdge_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortAdminEdge based on Integer32"""
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


_Gs2310STPCISTNormalPortAdminEdge_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortAdminEdge_Object = MibTableColumn
gs2310STPCISTNormalPortAdminEdge = _Gs2310STPCISTNormalPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 5),
    _Gs2310STPCISTNormalPortAdminEdge_Type()
)
gs2310STPCISTNormalPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortAdminEdge.setStatus("current")


class _Gs2310STPCISTNormalPortAutoEdge_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortAutoEdge based on Integer32"""
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


_Gs2310STPCISTNormalPortAutoEdge_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortAutoEdge_Object = MibTableColumn
gs2310STPCISTNormalPortAutoEdge = _Gs2310STPCISTNormalPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 6),
    _Gs2310STPCISTNormalPortAutoEdge_Type()
)
gs2310STPCISTNormalPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortAutoEdge.setStatus("current")


class _Gs2310STPCISTNormalPortRestrictedRole_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortRestrictedRole based on Integer32"""
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


_Gs2310STPCISTNormalPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortRestrictedRole_Object = MibTableColumn
gs2310STPCISTNormalPortRestrictedRole = _Gs2310STPCISTNormalPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 7),
    _Gs2310STPCISTNormalPortRestrictedRole_Type()
)
gs2310STPCISTNormalPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortRestrictedRole.setStatus("current")


class _Gs2310STPCISTNormalPortRestrictedTCN_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortRestrictedTCN based on Integer32"""
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


_Gs2310STPCISTNormalPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortRestrictedTCN_Object = MibTableColumn
gs2310STPCISTNormalPortRestrictedTCN = _Gs2310STPCISTNormalPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 8),
    _Gs2310STPCISTNormalPortRestrictedTCN_Type()
)
gs2310STPCISTNormalPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortRestrictedTCN.setStatus("current")


class _Gs2310STPCISTNormalPortBPDUGuard_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortBPDUGuard based on Integer32"""
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


_Gs2310STPCISTNormalPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortBPDUGuard_Object = MibTableColumn
gs2310STPCISTNormalPortBPDUGuard = _Gs2310STPCISTNormalPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 9),
    _Gs2310STPCISTNormalPortBPDUGuard_Type()
)
gs2310STPCISTNormalPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortBPDUGuard.setStatus("current")


class _Gs2310STPCISTNormalPortPointtoPoint_Type(Integer32):
    """Custom type gs2310STPCISTNormalPortPointtoPoint based on Integer32"""
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


_Gs2310STPCISTNormalPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2310STPCISTNormalPortPointtoPoint_Object = MibTableColumn
gs2310STPCISTNormalPortPointtoPoint = _Gs2310STPCISTNormalPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 6, 2, 1, 10),
    _Gs2310STPCISTNormalPortPointtoPoint_Type()
)
gs2310STPCISTNormalPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPCISTNormalPortPointtoPoint.setStatus("current")
_Gs2310STPMSTIPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTIPort = _Gs2310STPMSTIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7)
)
_Gs2310STPMSTI1Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI1Port = _Gs2310STPMSTI1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1)
)
_Gs2310STPMSTI1AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI1AggregatedPort = _Gs2310STPMSTI1AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 1)
)


class _Gs2310STPMSTI1AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI1AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI1AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI1AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI1AggregatedPortPathCost = _Gs2310STPMSTI1AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 1, 1),
    _Gs2310STPMSTI1AggregatedPortPathCost_Type()
)
gs2310STPMSTI1AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI1AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI1AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI1AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI1AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI1AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI1AggregatedPortPriority = _Gs2310STPMSTI1AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 1, 2),
    _Gs2310STPMSTI1AggregatedPortPriority_Type()
)
gs2310STPMSTI1AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI1AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI1NormalPortTable_Object = MibTable
gs2310STPMSTI1NormalPortTable = _Gs2310STPMSTI1NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI1NormalPortTable.setStatus("current")
_Gs2310STPMSTI1NormalPortEntry_Object = MibTableRow
gs2310STPMSTI1NormalPortEntry = _Gs2310STPMSTI1NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 2, 1)
)
gs2310STPMSTI1NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI1NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI1NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI1NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI1NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI1NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI1NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI1NormalPortConfPort = _Gs2310STPMSTI1NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 2, 1, 1),
    _Gs2310STPMSTI1NormalPortConfPort_Type()
)
gs2310STPMSTI1NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI1NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI1NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI1NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI1NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI1NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI1NormalPortPathCost = _Gs2310STPMSTI1NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 2, 1, 2),
    _Gs2310STPMSTI1NormalPortPathCost_Type()
)
gs2310STPMSTI1NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI1NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI1NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI1NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI1NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI1NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI1NormalPortPriority = _Gs2310STPMSTI1NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 1, 2, 1, 3),
    _Gs2310STPMSTI1NormalPortPriority_Type()
)
gs2310STPMSTI1NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI1NormalPortPriority.setStatus("current")
_Gs2310STPMSTI2Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI2Port = _Gs2310STPMSTI2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2)
)
_Gs2310STPMSTI2AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI2AggregatedPort = _Gs2310STPMSTI2AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 1)
)


class _Gs2310STPMSTI2AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI2AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI2AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI2AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI2AggregatedPortPathCost = _Gs2310STPMSTI2AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 1, 1),
    _Gs2310STPMSTI2AggregatedPortPathCost_Type()
)
gs2310STPMSTI2AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI2AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI2AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI2AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI2AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI2AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI2AggregatedPortPriority = _Gs2310STPMSTI2AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 1, 2),
    _Gs2310STPMSTI2AggregatedPortPriority_Type()
)
gs2310STPMSTI2AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI2AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI2NormalPortTable_Object = MibTable
gs2310STPMSTI2NormalPortTable = _Gs2310STPMSTI2NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI2NormalPortTable.setStatus("current")
_Gs2310STPMSTI2NormalPortEntry_Object = MibTableRow
gs2310STPMSTI2NormalPortEntry = _Gs2310STPMSTI2NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 2, 1)
)
gs2310STPMSTI2NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI2NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI2NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI2NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI2NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI2NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI2NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI2NormalPortConfPort = _Gs2310STPMSTI2NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 2, 1, 1),
    _Gs2310STPMSTI2NormalPortConfPort_Type()
)
gs2310STPMSTI2NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI2NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI2NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI2NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI2NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI2NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI2NormalPortPathCost = _Gs2310STPMSTI2NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 2, 1, 2),
    _Gs2310STPMSTI2NormalPortPathCost_Type()
)
gs2310STPMSTI2NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI2NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI2NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI2NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI2NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI2NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI2NormalPortPriority = _Gs2310STPMSTI2NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 2, 2, 1, 3),
    _Gs2310STPMSTI2NormalPortPriority_Type()
)
gs2310STPMSTI2NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI2NormalPortPriority.setStatus("current")
_Gs2310STPMSTI3Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI3Port = _Gs2310STPMSTI3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3)
)
_Gs2310STPMSTI3AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI3AggregatedPort = _Gs2310STPMSTI3AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 1)
)


class _Gs2310STPMSTI3AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI3AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI3AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI3AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI3AggregatedPortPathCost = _Gs2310STPMSTI3AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 1, 1),
    _Gs2310STPMSTI3AggregatedPortPathCost_Type()
)
gs2310STPMSTI3AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI3AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI3AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI3AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI3AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI3AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI3AggregatedPortPriority = _Gs2310STPMSTI3AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 1, 2),
    _Gs2310STPMSTI3AggregatedPortPriority_Type()
)
gs2310STPMSTI3AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI3AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI3NormalPortTable_Object = MibTable
gs2310STPMSTI3NormalPortTable = _Gs2310STPMSTI3NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI3NormalPortTable.setStatus("current")
_Gs2310STPMSTI3NormalPortEntry_Object = MibTableRow
gs2310STPMSTI3NormalPortEntry = _Gs2310STPMSTI3NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 2, 1)
)
gs2310STPMSTI3NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI3NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI3NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI3NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI3NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI3NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI3NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI3NormalPortConfPort = _Gs2310STPMSTI3NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 2, 1, 1),
    _Gs2310STPMSTI3NormalPortConfPort_Type()
)
gs2310STPMSTI3NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI3NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI3NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI3NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI3NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI3NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI3NormalPortPathCost = _Gs2310STPMSTI3NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 2, 1, 2),
    _Gs2310STPMSTI3NormalPortPathCost_Type()
)
gs2310STPMSTI3NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI3NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI3NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI3NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI3NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI3NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI3NormalPortPriority = _Gs2310STPMSTI3NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 3, 2, 1, 3),
    _Gs2310STPMSTI3NormalPortPriority_Type()
)
gs2310STPMSTI3NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI3NormalPortPriority.setStatus("current")
_Gs2310STPMSTI4Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI4Port = _Gs2310STPMSTI4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4)
)
_Gs2310STPMSTI4AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI4AggregatedPort = _Gs2310STPMSTI4AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 1)
)


class _Gs2310STPMSTI4AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI4AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI4AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI4AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI4AggregatedPortPathCost = _Gs2310STPMSTI4AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 1, 1),
    _Gs2310STPMSTI4AggregatedPortPathCost_Type()
)
gs2310STPMSTI4AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI4AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI4AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI4AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI4AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI4AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI4AggregatedPortPriority = _Gs2310STPMSTI4AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 1, 2),
    _Gs2310STPMSTI4AggregatedPortPriority_Type()
)
gs2310STPMSTI4AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI4AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI4NormalPortTable_Object = MibTable
gs2310STPMSTI4NormalPortTable = _Gs2310STPMSTI4NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI4NormalPortTable.setStatus("current")
_Gs2310STPMSTI4NormalPortEntry_Object = MibTableRow
gs2310STPMSTI4NormalPortEntry = _Gs2310STPMSTI4NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 2, 1)
)
gs2310STPMSTI4NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI4NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI4NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI4NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI4NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI4NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI4NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI4NormalPortConfPort = _Gs2310STPMSTI4NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 2, 1, 1),
    _Gs2310STPMSTI4NormalPortConfPort_Type()
)
gs2310STPMSTI4NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI4NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI4NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI4NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI4NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI4NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI4NormalPortPathCost = _Gs2310STPMSTI4NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 2, 1, 2),
    _Gs2310STPMSTI4NormalPortPathCost_Type()
)
gs2310STPMSTI4NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI4NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI4NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI4NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI4NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI4NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI4NormalPortPriority = _Gs2310STPMSTI4NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 4, 2, 1, 3),
    _Gs2310STPMSTI4NormalPortPriority_Type()
)
gs2310STPMSTI4NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI4NormalPortPriority.setStatus("current")
_Gs2310STPMSTI5Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI5Port = _Gs2310STPMSTI5Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5)
)
_Gs2310STPMSTI5AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI5AggregatedPort = _Gs2310STPMSTI5AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 1)
)


class _Gs2310STPMSTI5AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI5AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI5AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI5AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI5AggregatedPortPathCost = _Gs2310STPMSTI5AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 1, 1),
    _Gs2310STPMSTI5AggregatedPortPathCost_Type()
)
gs2310STPMSTI5AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI5AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI5AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI5AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI5AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI5AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI5AggregatedPortPriority = _Gs2310STPMSTI5AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 1, 2),
    _Gs2310STPMSTI5AggregatedPortPriority_Type()
)
gs2310STPMSTI5AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI5AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI5NormalPortTable_Object = MibTable
gs2310STPMSTI5NormalPortTable = _Gs2310STPMSTI5NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI5NormalPortTable.setStatus("current")
_Gs2310STPMSTI5NormalPortEntry_Object = MibTableRow
gs2310STPMSTI5NormalPortEntry = _Gs2310STPMSTI5NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 2, 1)
)
gs2310STPMSTI5NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI5NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI5NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI5NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI5NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI5NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI5NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI5NormalPortConfPort = _Gs2310STPMSTI5NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 2, 1, 1),
    _Gs2310STPMSTI5NormalPortConfPort_Type()
)
gs2310STPMSTI5NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI5NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI5NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI5NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI5NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI5NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI5NormalPortPathCost = _Gs2310STPMSTI5NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 2, 1, 2),
    _Gs2310STPMSTI5NormalPortPathCost_Type()
)
gs2310STPMSTI5NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI5NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI5NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI5NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI5NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI5NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI5NormalPortPriority = _Gs2310STPMSTI5NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 5, 2, 1, 3),
    _Gs2310STPMSTI5NormalPortPriority_Type()
)
gs2310STPMSTI5NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI5NormalPortPriority.setStatus("current")
_Gs2310STPMSTI6Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI6Port = _Gs2310STPMSTI6Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6)
)
_Gs2310STPMSTI6AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI6AggregatedPort = _Gs2310STPMSTI6AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 1)
)


class _Gs2310STPMSTI6AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI6AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI6AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI6AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI6AggregatedPortPathCost = _Gs2310STPMSTI6AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 1, 1),
    _Gs2310STPMSTI6AggregatedPortPathCost_Type()
)
gs2310STPMSTI6AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI6AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI6AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI6AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI6AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI6AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI6AggregatedPortPriority = _Gs2310STPMSTI6AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 1, 2),
    _Gs2310STPMSTI6AggregatedPortPriority_Type()
)
gs2310STPMSTI6AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI6AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI6NormalPortTable_Object = MibTable
gs2310STPMSTI6NormalPortTable = _Gs2310STPMSTI6NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI6NormalPortTable.setStatus("current")
_Gs2310STPMSTI6NormalPortEntry_Object = MibTableRow
gs2310STPMSTI6NormalPortEntry = _Gs2310STPMSTI6NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 2, 1)
)
gs2310STPMSTI6NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI6NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI6NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI6NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI6NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI6NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI6NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI6NormalPortConfPort = _Gs2310STPMSTI6NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 2, 1, 1),
    _Gs2310STPMSTI6NormalPortConfPort_Type()
)
gs2310STPMSTI6NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI6NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI6NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI6NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI6NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI6NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI6NormalPortPathCost = _Gs2310STPMSTI6NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 2, 1, 2),
    _Gs2310STPMSTI6NormalPortPathCost_Type()
)
gs2310STPMSTI6NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI6NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI6NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI6NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI6NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI6NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI6NormalPortPriority = _Gs2310STPMSTI6NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 6, 2, 1, 3),
    _Gs2310STPMSTI6NormalPortPriority_Type()
)
gs2310STPMSTI6NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI6NormalPortPriority.setStatus("current")
_Gs2310STPMSTI7Port_ObjectIdentity = ObjectIdentity
gs2310STPMSTI7Port = _Gs2310STPMSTI7Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7)
)
_Gs2310STPMSTI7AggregatedPort_ObjectIdentity = ObjectIdentity
gs2310STPMSTI7AggregatedPort = _Gs2310STPMSTI7AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 1)
)


class _Gs2310STPMSTI7AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI7AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI7AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI7AggregatedPortPathCost_Object = MibScalar
gs2310STPMSTI7AggregatedPortPathCost = _Gs2310STPMSTI7AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 1, 1),
    _Gs2310STPMSTI7AggregatedPortPathCost_Type()
)
gs2310STPMSTI7AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI7AggregatedPortPathCost.setStatus("current")


class _Gs2310STPMSTI7AggregatedPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI7AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI7AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI7AggregatedPortPriority_Object = MibScalar
gs2310STPMSTI7AggregatedPortPriority = _Gs2310STPMSTI7AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 1, 2),
    _Gs2310STPMSTI7AggregatedPortPriority_Type()
)
gs2310STPMSTI7AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI7AggregatedPortPriority.setStatus("current")
_Gs2310STPMSTI7NormalPortTable_Object = MibTable
gs2310STPMSTI7NormalPortTable = _Gs2310STPMSTI7NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 2)
)
if mibBuilder.loadTexts:
    gs2310STPMSTI7NormalPortTable.setStatus("current")
_Gs2310STPMSTI7NormalPortEntry_Object = MibTableRow
gs2310STPMSTI7NormalPortEntry = _Gs2310STPMSTI7NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 2, 1)
)
gs2310STPMSTI7NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPMSTI7NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2310STPMSTI7NormalPortEntry.setStatus("current")


class _Gs2310STPMSTI7NormalPortConfPort_Type(Integer32):
    """Custom type gs2310STPMSTI7NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPMSTI7NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2310STPMSTI7NormalPortConfPort_Object = MibTableColumn
gs2310STPMSTI7NormalPortConfPort = _Gs2310STPMSTI7NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 2, 1, 1),
    _Gs2310STPMSTI7NormalPortConfPort_Type()
)
gs2310STPMSTI7NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPMSTI7NormalPortConfPort.setStatus("current")


class _Gs2310STPMSTI7NormalPortPathCost_Type(Integer32):
    """Custom type gs2310STPMSTI7NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310STPMSTI7NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2310STPMSTI7NormalPortPathCost_Object = MibTableColumn
gs2310STPMSTI7NormalPortPathCost = _Gs2310STPMSTI7NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 2, 1, 2),
    _Gs2310STPMSTI7NormalPortPathCost_Type()
)
gs2310STPMSTI7NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI7NormalPortPathCost.setStatus("current")


class _Gs2310STPMSTI7NormalPortPriority_Type(Integer32):
    """Custom type gs2310STPMSTI7NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2310STPMSTI7NormalPortPriority_Type.__name__ = "Integer32"
_Gs2310STPMSTI7NormalPortPriority_Object = MibTableColumn
gs2310STPMSTI7NormalPortPriority = _Gs2310STPMSTI7NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 7, 7, 2, 1, 3),
    _Gs2310STPMSTI7NormalPortPriority_Type()
)
gs2310STPMSTI7NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310STPMSTI7NormalPortPriority.setStatus("current")
_Gs2310STPBridgeStatus_ObjectIdentity = ObjectIdentity
gs2310STPBridgeStatus = _Gs2310STPBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8)
)
_Gs2310CISTBridgeSTP_ObjectIdentity = ObjectIdentity
gs2310CISTBridgeSTP = _Gs2310CISTBridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1)
)
_Gs2310CISTBridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310CISTBridgeSTPStatus = _Gs2310CISTBridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1)
)
_Gs2310CISTBridgeInstance_Type = DisplayString
_Gs2310CISTBridgeInstance_Object = MibScalar
gs2310CISTBridgeInstance = _Gs2310CISTBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 1),
    _Gs2310CISTBridgeInstance_Type()
)
gs2310CISTBridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTBridgeInstance.setStatus("current")
_Gs2310CISTBridgeID_Type = DisplayString
_Gs2310CISTBridgeID_Object = MibScalar
gs2310CISTBridgeID = _Gs2310CISTBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 2),
    _Gs2310CISTBridgeID_Type()
)
gs2310CISTBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTBridgeID.setStatus("current")
_Gs2310CISTRootID_Type = DisplayString
_Gs2310CISTRootID_Object = MibScalar
gs2310CISTRootID = _Gs2310CISTRootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 3),
    _Gs2310CISTRootID_Type()
)
gs2310CISTRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTRootID.setStatus("current")
_Gs2310CISTRootPort_Type = DisplayString
_Gs2310CISTRootPort_Object = MibScalar
gs2310CISTRootPort = _Gs2310CISTRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 4),
    _Gs2310CISTRootPort_Type()
)
gs2310CISTRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTRootPort.setStatus("current")


class _Gs2310CISTRootCost_Type(Integer32):
    """Custom type gs2310CISTRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310CISTRootCost_Type.__name__ = "Integer32"
_Gs2310CISTRootCost_Object = MibScalar
gs2310CISTRootCost = _Gs2310CISTRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 5),
    _Gs2310CISTRootCost_Type()
)
gs2310CISTRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTRootCost.setStatus("current")
_Gs2310CISTRegionalRoot_Type = DisplayString
_Gs2310CISTRegionalRoot_Object = MibScalar
gs2310CISTRegionalRoot = _Gs2310CISTRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 6),
    _Gs2310CISTRegionalRoot_Type()
)
gs2310CISTRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTRegionalRoot.setStatus("current")


class _Gs2310CISTInternalRootCost_Type(Integer32):
    """Custom type gs2310CISTInternalRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310CISTInternalRootCost_Type.__name__ = "Integer32"
_Gs2310CISTInternalRootCost_Object = MibScalar
gs2310CISTInternalRootCost = _Gs2310CISTInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 7),
    _Gs2310CISTInternalRootCost_Type()
)
gs2310CISTInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTInternalRootCost.setStatus("current")
_Gs2310CISTTopologyFlag_Type = DisplayString
_Gs2310CISTTopologyFlag_Object = MibScalar
gs2310CISTTopologyFlag = _Gs2310CISTTopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 8),
    _Gs2310CISTTopologyFlag_Type()
)
gs2310CISTTopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTTopologyFlag.setStatus("current")
_Gs2310CISTTopologyChangeCount_Type = Counter32
_Gs2310CISTTopologyChangeCount_Object = MibScalar
gs2310CISTTopologyChangeCount = _Gs2310CISTTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 9),
    _Gs2310CISTTopologyChangeCount_Type()
)
gs2310CISTTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTTopologyChangeCount.setStatus("current")
_Gs2310CISTTopologyChangeLast_Type = DisplayString
_Gs2310CISTTopologyChangeLast_Object = MibScalar
gs2310CISTTopologyChangeLast = _Gs2310CISTTopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 1, 10),
    _Gs2310CISTTopologyChangeLast_Type()
)
gs2310CISTTopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTTopologyChangeLast.setStatus("current")
_Gs2310CISTPortStateTable_Object = MibTable
gs2310CISTPortStateTable = _Gs2310CISTPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310CISTPortStateTable.setStatus("current")
_Gs2310CISTPortStateEntry_Object = MibTableRow
gs2310CISTPortStateEntry = _Gs2310CISTPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1)
)
gs2310CISTPortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310CISTPortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310CISTPortStateEntry.setStatus("current")


class _Gs2310CISTPortStateIndex_Type(Integer32):
    """Custom type gs2310CISTPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310CISTPortStateIndex_Type.__name__ = "Integer32"
_Gs2310CISTPortStateIndex_Object = MibTableColumn
gs2310CISTPortStateIndex = _Gs2310CISTPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 1),
    _Gs2310CISTPortStateIndex_Type()
)
gs2310CISTPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310CISTPortStateIndex.setStatus("current")
_Gs2310CISTPortStatePort_Type = DisplayString
_Gs2310CISTPortStatePort_Object = MibTableColumn
gs2310CISTPortStatePort = _Gs2310CISTPortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 2),
    _Gs2310CISTPortStatePort_Type()
)
gs2310CISTPortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStatePort.setStatus("current")
_Gs2310CISTPortStatePortID_Type = DisplayString
_Gs2310CISTPortStatePortID_Object = MibTableColumn
gs2310CISTPortStatePortID = _Gs2310CISTPortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 3),
    _Gs2310CISTPortStatePortID_Type()
)
gs2310CISTPortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStatePortID.setStatus("current")
_Gs2310CISTPortStateRole_Type = DisplayString
_Gs2310CISTPortStateRole_Object = MibTableColumn
gs2310CISTPortStateRole = _Gs2310CISTPortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 4),
    _Gs2310CISTPortStateRole_Type()
)
gs2310CISTPortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStateRole.setStatus("current")
_Gs2310CISTPortStateState_Type = DisplayString
_Gs2310CISTPortStateState_Object = MibTableColumn
gs2310CISTPortStateState = _Gs2310CISTPortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 5),
    _Gs2310CISTPortStateState_Type()
)
gs2310CISTPortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStateState.setStatus("current")


class _Gs2310CISTPortStatePathCost_Type(Integer32):
    """Custom type gs2310CISTPortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310CISTPortStatePathCost_Type.__name__ = "Integer32"
_Gs2310CISTPortStatePathCost_Object = MibTableColumn
gs2310CISTPortStatePathCost = _Gs2310CISTPortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 6),
    _Gs2310CISTPortStatePathCost_Type()
)
gs2310CISTPortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStatePathCost.setStatus("current")
_Gs2310CISTPortStateEdge_Type = DisplayString
_Gs2310CISTPortStateEdge_Object = MibTableColumn
gs2310CISTPortStateEdge = _Gs2310CISTPortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 7),
    _Gs2310CISTPortStateEdge_Type()
)
gs2310CISTPortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStateEdge.setStatus("current")
_Gs2310CISTPortStatePoint2Point_Type = DisplayString
_Gs2310CISTPortStatePoint2Point_Object = MibTableColumn
gs2310CISTPortStatePoint2Point = _Gs2310CISTPortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 8),
    _Gs2310CISTPortStatePoint2Point_Type()
)
gs2310CISTPortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStatePoint2Point.setStatus("current")
_Gs2310CISTPortStateUptime_Type = DisplayString
_Gs2310CISTPortStateUptime_Object = MibTableColumn
gs2310CISTPortStateUptime = _Gs2310CISTPortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 1, 2, 1, 9),
    _Gs2310CISTPortStateUptime_Type()
)
gs2310CISTPortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310CISTPortStateUptime.setStatus("current")
_Gs2310MSTI1BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI1BridgeSTP = _Gs2310MSTI1BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2)
)
_Gs2310MSTI1BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI1BridgeSTPStatus = _Gs2310MSTI1BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1)
)
_Gs2310MSTI1BridgeInstance_Type = DisplayString
_Gs2310MSTI1BridgeInstance_Object = MibScalar
gs2310MSTI1BridgeInstance = _Gs2310MSTI1BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 1),
    _Gs2310MSTI1BridgeInstance_Type()
)
gs2310MSTI1BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1BridgeInstance.setStatus("current")
_Gs2310MSTI1BridgeID_Type = DisplayString
_Gs2310MSTI1BridgeID_Object = MibScalar
gs2310MSTI1BridgeID = _Gs2310MSTI1BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 2),
    _Gs2310MSTI1BridgeID_Type()
)
gs2310MSTI1BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1BridgeID.setStatus("current")
_Gs2310MSTI1RootID_Type = DisplayString
_Gs2310MSTI1RootID_Object = MibScalar
gs2310MSTI1RootID = _Gs2310MSTI1RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 3),
    _Gs2310MSTI1RootID_Type()
)
gs2310MSTI1RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1RootID.setStatus("current")
_Gs2310MSTI1RootPort_Type = DisplayString
_Gs2310MSTI1RootPort_Object = MibScalar
gs2310MSTI1RootPort = _Gs2310MSTI1RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 4),
    _Gs2310MSTI1RootPort_Type()
)
gs2310MSTI1RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1RootPort.setStatus("current")


class _Gs2310MSTI1RootCost_Type(Integer32):
    """Custom type gs2310MSTI1RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI1RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI1RootCost_Object = MibScalar
gs2310MSTI1RootCost = _Gs2310MSTI1RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 5),
    _Gs2310MSTI1RootCost_Type()
)
gs2310MSTI1RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1RootCost.setStatus("current")
_Gs2310MSTI1TopologyFlag_Type = DisplayString
_Gs2310MSTI1TopologyFlag_Object = MibScalar
gs2310MSTI1TopologyFlag = _Gs2310MSTI1TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 8),
    _Gs2310MSTI1TopologyFlag_Type()
)
gs2310MSTI1TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1TopologyFlag.setStatus("current")
_Gs2310MSTI1TopologyChangeCount_Type = Counter32
_Gs2310MSTI1TopologyChangeCount_Object = MibScalar
gs2310MSTI1TopologyChangeCount = _Gs2310MSTI1TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 9),
    _Gs2310MSTI1TopologyChangeCount_Type()
)
gs2310MSTI1TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1TopologyChangeCount.setStatus("current")
_Gs2310MSTI1TopologyChangeLast_Type = DisplayString
_Gs2310MSTI1TopologyChangeLast_Object = MibScalar
gs2310MSTI1TopologyChangeLast = _Gs2310MSTI1TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 1, 10),
    _Gs2310MSTI1TopologyChangeLast_Type()
)
gs2310MSTI1TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1TopologyChangeLast.setStatus("current")
_Gs2310MSTI1PortStateTable_Object = MibTable
gs2310MSTI1PortStateTable = _Gs2310MSTI1PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateTable.setStatus("current")
_Gs2310MSTI1PortStateEntry_Object = MibTableRow
gs2310MSTI1PortStateEntry = _Gs2310MSTI1PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1)
)
gs2310MSTI1PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI1PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateEntry.setStatus("current")


class _Gs2310MSTI1PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI1PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI1PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI1PortStateIndex_Object = MibTableColumn
gs2310MSTI1PortStateIndex = _Gs2310MSTI1PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 1),
    _Gs2310MSTI1PortStateIndex_Type()
)
gs2310MSTI1PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateIndex.setStatus("current")
_Gs2310MSTI1PortStatePort_Type = DisplayString
_Gs2310MSTI1PortStatePort_Object = MibTableColumn
gs2310MSTI1PortStatePort = _Gs2310MSTI1PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 2),
    _Gs2310MSTI1PortStatePort_Type()
)
gs2310MSTI1PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStatePort.setStatus("current")
_Gs2310MSTI1PortStatePortID_Type = DisplayString
_Gs2310MSTI1PortStatePortID_Object = MibTableColumn
gs2310MSTI1PortStatePortID = _Gs2310MSTI1PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 3),
    _Gs2310MSTI1PortStatePortID_Type()
)
gs2310MSTI1PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStatePortID.setStatus("current")
_Gs2310MSTI1PortStateRole_Type = DisplayString
_Gs2310MSTI1PortStateRole_Object = MibTableColumn
gs2310MSTI1PortStateRole = _Gs2310MSTI1PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 4),
    _Gs2310MSTI1PortStateRole_Type()
)
gs2310MSTI1PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateRole.setStatus("current")
_Gs2310MSTI1PortStateState_Type = DisplayString
_Gs2310MSTI1PortStateState_Object = MibTableColumn
gs2310MSTI1PortStateState = _Gs2310MSTI1PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 5),
    _Gs2310MSTI1PortStateState_Type()
)
gs2310MSTI1PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateState.setStatus("current")


class _Gs2310MSTI1PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI1PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI1PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI1PortStatePathCost_Object = MibTableColumn
gs2310MSTI1PortStatePathCost = _Gs2310MSTI1PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 6),
    _Gs2310MSTI1PortStatePathCost_Type()
)
gs2310MSTI1PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStatePathCost.setStatus("current")
_Gs2310MSTI1PortStateEdge_Type = DisplayString
_Gs2310MSTI1PortStateEdge_Object = MibTableColumn
gs2310MSTI1PortStateEdge = _Gs2310MSTI1PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 7),
    _Gs2310MSTI1PortStateEdge_Type()
)
gs2310MSTI1PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateEdge.setStatus("current")
_Gs2310MSTI1PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI1PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI1PortStatePoint2Point = _Gs2310MSTI1PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 8),
    _Gs2310MSTI1PortStatePoint2Point_Type()
)
gs2310MSTI1PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStatePoint2Point.setStatus("current")
_Gs2310MSTI1PortStateUptime_Type = DisplayString
_Gs2310MSTI1PortStateUptime_Object = MibTableColumn
gs2310MSTI1PortStateUptime = _Gs2310MSTI1PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 2, 2, 1, 9),
    _Gs2310MSTI1PortStateUptime_Type()
)
gs2310MSTI1PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI1PortStateUptime.setStatus("current")
_Gs2310MSTI2BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI2BridgeSTP = _Gs2310MSTI2BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3)
)
_Gs2310MSTI2BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI2BridgeSTPStatus = _Gs2310MSTI2BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1)
)
_Gs2310MSTI2BridgeInstance_Type = DisplayString
_Gs2310MSTI2BridgeInstance_Object = MibScalar
gs2310MSTI2BridgeInstance = _Gs2310MSTI2BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 1),
    _Gs2310MSTI2BridgeInstance_Type()
)
gs2310MSTI2BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2BridgeInstance.setStatus("current")
_Gs2310MSTI2BridgeID_Type = DisplayString
_Gs2310MSTI2BridgeID_Object = MibScalar
gs2310MSTI2BridgeID = _Gs2310MSTI2BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 2),
    _Gs2310MSTI2BridgeID_Type()
)
gs2310MSTI2BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2BridgeID.setStatus("current")
_Gs2310MSTI2RootID_Type = DisplayString
_Gs2310MSTI2RootID_Object = MibScalar
gs2310MSTI2RootID = _Gs2310MSTI2RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 3),
    _Gs2310MSTI2RootID_Type()
)
gs2310MSTI2RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2RootID.setStatus("current")
_Gs2310MSTI2RootPort_Type = DisplayString
_Gs2310MSTI2RootPort_Object = MibScalar
gs2310MSTI2RootPort = _Gs2310MSTI2RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 4),
    _Gs2310MSTI2RootPort_Type()
)
gs2310MSTI2RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2RootPort.setStatus("current")


class _Gs2310MSTI2RootCost_Type(Integer32):
    """Custom type gs2310MSTI2RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI2RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI2RootCost_Object = MibScalar
gs2310MSTI2RootCost = _Gs2310MSTI2RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 5),
    _Gs2310MSTI2RootCost_Type()
)
gs2310MSTI2RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2RootCost.setStatus("current")
_Gs2310MSTI2TopologyFlag_Type = DisplayString
_Gs2310MSTI2TopologyFlag_Object = MibScalar
gs2310MSTI2TopologyFlag = _Gs2310MSTI2TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 8),
    _Gs2310MSTI2TopologyFlag_Type()
)
gs2310MSTI2TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2TopologyFlag.setStatus("current")
_Gs2310MSTI2TopologyChangeCount_Type = Counter32
_Gs2310MSTI2TopologyChangeCount_Object = MibScalar
gs2310MSTI2TopologyChangeCount = _Gs2310MSTI2TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 9),
    _Gs2310MSTI2TopologyChangeCount_Type()
)
gs2310MSTI2TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2TopologyChangeCount.setStatus("current")
_Gs2310MSTI2TopologyChangeLast_Type = DisplayString
_Gs2310MSTI2TopologyChangeLast_Object = MibScalar
gs2310MSTI2TopologyChangeLast = _Gs2310MSTI2TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 1, 10),
    _Gs2310MSTI2TopologyChangeLast_Type()
)
gs2310MSTI2TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2TopologyChangeLast.setStatus("current")
_Gs2310MSTI2PortStateTable_Object = MibTable
gs2310MSTI2PortStateTable = _Gs2310MSTI2PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateTable.setStatus("current")
_Gs2310MSTI2PortStateEntry_Object = MibTableRow
gs2310MSTI2PortStateEntry = _Gs2310MSTI2PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1)
)
gs2310MSTI2PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI2PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateEntry.setStatus("current")


class _Gs2310MSTI2PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI2PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI2PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI2PortStateIndex_Object = MibTableColumn
gs2310MSTI2PortStateIndex = _Gs2310MSTI2PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 1),
    _Gs2310MSTI2PortStateIndex_Type()
)
gs2310MSTI2PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateIndex.setStatus("current")
_Gs2310MSTI2PortStatePort_Type = DisplayString
_Gs2310MSTI2PortStatePort_Object = MibTableColumn
gs2310MSTI2PortStatePort = _Gs2310MSTI2PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 2),
    _Gs2310MSTI2PortStatePort_Type()
)
gs2310MSTI2PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStatePort.setStatus("current")
_Gs2310MSTI2PortStatePortID_Type = DisplayString
_Gs2310MSTI2PortStatePortID_Object = MibTableColumn
gs2310MSTI2PortStatePortID = _Gs2310MSTI2PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 3),
    _Gs2310MSTI2PortStatePortID_Type()
)
gs2310MSTI2PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStatePortID.setStatus("current")
_Gs2310MSTI2PortStateRole_Type = DisplayString
_Gs2310MSTI2PortStateRole_Object = MibTableColumn
gs2310MSTI2PortStateRole = _Gs2310MSTI2PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 4),
    _Gs2310MSTI2PortStateRole_Type()
)
gs2310MSTI2PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateRole.setStatus("current")
_Gs2310MSTI2PortStateState_Type = DisplayString
_Gs2310MSTI2PortStateState_Object = MibTableColumn
gs2310MSTI2PortStateState = _Gs2310MSTI2PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 5),
    _Gs2310MSTI2PortStateState_Type()
)
gs2310MSTI2PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateState.setStatus("current")


class _Gs2310MSTI2PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI2PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI2PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI2PortStatePathCost_Object = MibTableColumn
gs2310MSTI2PortStatePathCost = _Gs2310MSTI2PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 6),
    _Gs2310MSTI2PortStatePathCost_Type()
)
gs2310MSTI2PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStatePathCost.setStatus("current")
_Gs2310MSTI2PortStateEdge_Type = DisplayString
_Gs2310MSTI2PortStateEdge_Object = MibTableColumn
gs2310MSTI2PortStateEdge = _Gs2310MSTI2PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 7),
    _Gs2310MSTI2PortStateEdge_Type()
)
gs2310MSTI2PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateEdge.setStatus("current")
_Gs2310MSTI2PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI2PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI2PortStatePoint2Point = _Gs2310MSTI2PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 8),
    _Gs2310MSTI2PortStatePoint2Point_Type()
)
gs2310MSTI2PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStatePoint2Point.setStatus("current")
_Gs2310MSTI2PortStateUptime_Type = DisplayString
_Gs2310MSTI2PortStateUptime_Object = MibTableColumn
gs2310MSTI2PortStateUptime = _Gs2310MSTI2PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 3, 2, 1, 9),
    _Gs2310MSTI2PortStateUptime_Type()
)
gs2310MSTI2PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI2PortStateUptime.setStatus("current")
_Gs2310MSTI3BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI3BridgeSTP = _Gs2310MSTI3BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4)
)
_Gs2310MSTI3BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI3BridgeSTPStatus = _Gs2310MSTI3BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1)
)
_Gs2310MSTI3BridgeInstance_Type = DisplayString
_Gs2310MSTI3BridgeInstance_Object = MibScalar
gs2310MSTI3BridgeInstance = _Gs2310MSTI3BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 1),
    _Gs2310MSTI3BridgeInstance_Type()
)
gs2310MSTI3BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3BridgeInstance.setStatus("current")
_Gs2310MSTI3BridgeID_Type = DisplayString
_Gs2310MSTI3BridgeID_Object = MibScalar
gs2310MSTI3BridgeID = _Gs2310MSTI3BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 2),
    _Gs2310MSTI3BridgeID_Type()
)
gs2310MSTI3BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3BridgeID.setStatus("current")
_Gs2310MSTI3RootID_Type = DisplayString
_Gs2310MSTI3RootID_Object = MibScalar
gs2310MSTI3RootID = _Gs2310MSTI3RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 3),
    _Gs2310MSTI3RootID_Type()
)
gs2310MSTI3RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3RootID.setStatus("current")
_Gs2310MSTI3RootPort_Type = DisplayString
_Gs2310MSTI3RootPort_Object = MibScalar
gs2310MSTI3RootPort = _Gs2310MSTI3RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 4),
    _Gs2310MSTI3RootPort_Type()
)
gs2310MSTI3RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3RootPort.setStatus("current")


class _Gs2310MSTI3RootCost_Type(Integer32):
    """Custom type gs2310MSTI3RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI3RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI3RootCost_Object = MibScalar
gs2310MSTI3RootCost = _Gs2310MSTI3RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 5),
    _Gs2310MSTI3RootCost_Type()
)
gs2310MSTI3RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3RootCost.setStatus("current")
_Gs2310MSTI3TopologyFlag_Type = DisplayString
_Gs2310MSTI3TopologyFlag_Object = MibScalar
gs2310MSTI3TopologyFlag = _Gs2310MSTI3TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 8),
    _Gs2310MSTI3TopologyFlag_Type()
)
gs2310MSTI3TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3TopologyFlag.setStatus("current")
_Gs2310MSTI3TopologyChangeCount_Type = Counter32
_Gs2310MSTI3TopologyChangeCount_Object = MibScalar
gs2310MSTI3TopologyChangeCount = _Gs2310MSTI3TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 9),
    _Gs2310MSTI3TopologyChangeCount_Type()
)
gs2310MSTI3TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3TopologyChangeCount.setStatus("current")
_Gs2310MSTI3TopologyChangeLast_Type = DisplayString
_Gs2310MSTI3TopologyChangeLast_Object = MibScalar
gs2310MSTI3TopologyChangeLast = _Gs2310MSTI3TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 1, 10),
    _Gs2310MSTI3TopologyChangeLast_Type()
)
gs2310MSTI3TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3TopologyChangeLast.setStatus("current")
_Gs2310MSTI3PortStateTable_Object = MibTable
gs2310MSTI3PortStateTable = _Gs2310MSTI3PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateTable.setStatus("current")
_Gs2310MSTI3PortStateEntry_Object = MibTableRow
gs2310MSTI3PortStateEntry = _Gs2310MSTI3PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1)
)
gs2310MSTI3PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI3PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateEntry.setStatus("current")


class _Gs2310MSTI3PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI3PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI3PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI3PortStateIndex_Object = MibTableColumn
gs2310MSTI3PortStateIndex = _Gs2310MSTI3PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 1),
    _Gs2310MSTI3PortStateIndex_Type()
)
gs2310MSTI3PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateIndex.setStatus("current")
_Gs2310MSTI3PortStatePort_Type = DisplayString
_Gs2310MSTI3PortStatePort_Object = MibTableColumn
gs2310MSTI3PortStatePort = _Gs2310MSTI3PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 2),
    _Gs2310MSTI3PortStatePort_Type()
)
gs2310MSTI3PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStatePort.setStatus("current")
_Gs2310MSTI3PortStatePortID_Type = DisplayString
_Gs2310MSTI3PortStatePortID_Object = MibTableColumn
gs2310MSTI3PortStatePortID = _Gs2310MSTI3PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 3),
    _Gs2310MSTI3PortStatePortID_Type()
)
gs2310MSTI3PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStatePortID.setStatus("current")
_Gs2310MSTI3PortStateRole_Type = DisplayString
_Gs2310MSTI3PortStateRole_Object = MibTableColumn
gs2310MSTI3PortStateRole = _Gs2310MSTI3PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 4),
    _Gs2310MSTI3PortStateRole_Type()
)
gs2310MSTI3PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateRole.setStatus("current")
_Gs2310MSTI3PortStateState_Type = DisplayString
_Gs2310MSTI3PortStateState_Object = MibTableColumn
gs2310MSTI3PortStateState = _Gs2310MSTI3PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 5),
    _Gs2310MSTI3PortStateState_Type()
)
gs2310MSTI3PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateState.setStatus("current")


class _Gs2310MSTI3PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI3PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI3PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI3PortStatePathCost_Object = MibTableColumn
gs2310MSTI3PortStatePathCost = _Gs2310MSTI3PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 6),
    _Gs2310MSTI3PortStatePathCost_Type()
)
gs2310MSTI3PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStatePathCost.setStatus("current")
_Gs2310MSTI3PortStateEdge_Type = DisplayString
_Gs2310MSTI3PortStateEdge_Object = MibTableColumn
gs2310MSTI3PortStateEdge = _Gs2310MSTI3PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 7),
    _Gs2310MSTI3PortStateEdge_Type()
)
gs2310MSTI3PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateEdge.setStatus("current")
_Gs2310MSTI3PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI3PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI3PortStatePoint2Point = _Gs2310MSTI3PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 8),
    _Gs2310MSTI3PortStatePoint2Point_Type()
)
gs2310MSTI3PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStatePoint2Point.setStatus("current")
_Gs2310MSTI3PortStateUptime_Type = DisplayString
_Gs2310MSTI3PortStateUptime_Object = MibTableColumn
gs2310MSTI3PortStateUptime = _Gs2310MSTI3PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 4, 2, 1, 9),
    _Gs2310MSTI3PortStateUptime_Type()
)
gs2310MSTI3PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI3PortStateUptime.setStatus("current")
_Gs2310MSTI4BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI4BridgeSTP = _Gs2310MSTI4BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5)
)
_Gs2310MSTI4BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI4BridgeSTPStatus = _Gs2310MSTI4BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1)
)
_Gs2310MSTI4BridgeInstance_Type = DisplayString
_Gs2310MSTI4BridgeInstance_Object = MibScalar
gs2310MSTI4BridgeInstance = _Gs2310MSTI4BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 1),
    _Gs2310MSTI4BridgeInstance_Type()
)
gs2310MSTI4BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4BridgeInstance.setStatus("current")
_Gs2310MSTI4BridgeID_Type = DisplayString
_Gs2310MSTI4BridgeID_Object = MibScalar
gs2310MSTI4BridgeID = _Gs2310MSTI4BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 2),
    _Gs2310MSTI4BridgeID_Type()
)
gs2310MSTI4BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4BridgeID.setStatus("current")
_Gs2310MSTI4RootID_Type = DisplayString
_Gs2310MSTI4RootID_Object = MibScalar
gs2310MSTI4RootID = _Gs2310MSTI4RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 3),
    _Gs2310MSTI4RootID_Type()
)
gs2310MSTI4RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4RootID.setStatus("current")
_Gs2310MSTI4RootPort_Type = DisplayString
_Gs2310MSTI4RootPort_Object = MibScalar
gs2310MSTI4RootPort = _Gs2310MSTI4RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 4),
    _Gs2310MSTI4RootPort_Type()
)
gs2310MSTI4RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4RootPort.setStatus("current")


class _Gs2310MSTI4RootCost_Type(Integer32):
    """Custom type gs2310MSTI4RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI4RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI4RootCost_Object = MibScalar
gs2310MSTI4RootCost = _Gs2310MSTI4RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 5),
    _Gs2310MSTI4RootCost_Type()
)
gs2310MSTI4RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4RootCost.setStatus("current")
_Gs2310MSTI4TopologyFlag_Type = DisplayString
_Gs2310MSTI4TopologyFlag_Object = MibScalar
gs2310MSTI4TopologyFlag = _Gs2310MSTI4TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 8),
    _Gs2310MSTI4TopologyFlag_Type()
)
gs2310MSTI4TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4TopologyFlag.setStatus("current")
_Gs2310MSTI4TopologyChangeCount_Type = Counter32
_Gs2310MSTI4TopologyChangeCount_Object = MibScalar
gs2310MSTI4TopologyChangeCount = _Gs2310MSTI4TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 9),
    _Gs2310MSTI4TopologyChangeCount_Type()
)
gs2310MSTI4TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4TopologyChangeCount.setStatus("current")
_Gs2310MSTI4TopologyChangeLast_Type = DisplayString
_Gs2310MSTI4TopologyChangeLast_Object = MibScalar
gs2310MSTI4TopologyChangeLast = _Gs2310MSTI4TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 1, 10),
    _Gs2310MSTI4TopologyChangeLast_Type()
)
gs2310MSTI4TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4TopologyChangeLast.setStatus("current")
_Gs2310MSTI4PortStateTable_Object = MibTable
gs2310MSTI4PortStateTable = _Gs2310MSTI4PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateTable.setStatus("current")
_Gs2310MSTI4PortStateEntry_Object = MibTableRow
gs2310MSTI4PortStateEntry = _Gs2310MSTI4PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1)
)
gs2310MSTI4PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI4PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateEntry.setStatus("current")


class _Gs2310MSTI4PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI4PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI4PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI4PortStateIndex_Object = MibTableColumn
gs2310MSTI4PortStateIndex = _Gs2310MSTI4PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 1),
    _Gs2310MSTI4PortStateIndex_Type()
)
gs2310MSTI4PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateIndex.setStatus("current")
_Gs2310MSTI4PortStatePort_Type = DisplayString
_Gs2310MSTI4PortStatePort_Object = MibTableColumn
gs2310MSTI4PortStatePort = _Gs2310MSTI4PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 2),
    _Gs2310MSTI4PortStatePort_Type()
)
gs2310MSTI4PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStatePort.setStatus("current")
_Gs2310MSTI4PortStatePortID_Type = DisplayString
_Gs2310MSTI4PortStatePortID_Object = MibTableColumn
gs2310MSTI4PortStatePortID = _Gs2310MSTI4PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 3),
    _Gs2310MSTI4PortStatePortID_Type()
)
gs2310MSTI4PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStatePortID.setStatus("current")
_Gs2310MSTI4PortStateRole_Type = DisplayString
_Gs2310MSTI4PortStateRole_Object = MibTableColumn
gs2310MSTI4PortStateRole = _Gs2310MSTI4PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 4),
    _Gs2310MSTI4PortStateRole_Type()
)
gs2310MSTI4PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateRole.setStatus("current")
_Gs2310MSTI4PortStateState_Type = DisplayString
_Gs2310MSTI4PortStateState_Object = MibTableColumn
gs2310MSTI4PortStateState = _Gs2310MSTI4PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 5),
    _Gs2310MSTI4PortStateState_Type()
)
gs2310MSTI4PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateState.setStatus("current")


class _Gs2310MSTI4PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI4PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI4PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI4PortStatePathCost_Object = MibTableColumn
gs2310MSTI4PortStatePathCost = _Gs2310MSTI4PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 6),
    _Gs2310MSTI4PortStatePathCost_Type()
)
gs2310MSTI4PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStatePathCost.setStatus("current")
_Gs2310MSTI4PortStateEdge_Type = DisplayString
_Gs2310MSTI4PortStateEdge_Object = MibTableColumn
gs2310MSTI4PortStateEdge = _Gs2310MSTI4PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 7),
    _Gs2310MSTI4PortStateEdge_Type()
)
gs2310MSTI4PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateEdge.setStatus("current")
_Gs2310MSTI4PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI4PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI4PortStatePoint2Point = _Gs2310MSTI4PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 8),
    _Gs2310MSTI4PortStatePoint2Point_Type()
)
gs2310MSTI4PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStatePoint2Point.setStatus("current")
_Gs2310MSTI4PortStateUptime_Type = DisplayString
_Gs2310MSTI4PortStateUptime_Object = MibTableColumn
gs2310MSTI4PortStateUptime = _Gs2310MSTI4PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 5, 2, 1, 9),
    _Gs2310MSTI4PortStateUptime_Type()
)
gs2310MSTI4PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI4PortStateUptime.setStatus("current")
_Gs2310MSTI5BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI5BridgeSTP = _Gs2310MSTI5BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6)
)
_Gs2310MSTI5BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI5BridgeSTPStatus = _Gs2310MSTI5BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1)
)
_Gs2310MSTI5BridgeInstance_Type = DisplayString
_Gs2310MSTI5BridgeInstance_Object = MibScalar
gs2310MSTI5BridgeInstance = _Gs2310MSTI5BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 1),
    _Gs2310MSTI5BridgeInstance_Type()
)
gs2310MSTI5BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5BridgeInstance.setStatus("current")
_Gs2310MSTI5BridgeID_Type = DisplayString
_Gs2310MSTI5BridgeID_Object = MibScalar
gs2310MSTI5BridgeID = _Gs2310MSTI5BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 2),
    _Gs2310MSTI5BridgeID_Type()
)
gs2310MSTI5BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5BridgeID.setStatus("current")
_Gs2310MSTI5RootID_Type = DisplayString
_Gs2310MSTI5RootID_Object = MibScalar
gs2310MSTI5RootID = _Gs2310MSTI5RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 3),
    _Gs2310MSTI5RootID_Type()
)
gs2310MSTI5RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5RootID.setStatus("current")
_Gs2310MSTI5RootPort_Type = DisplayString
_Gs2310MSTI5RootPort_Object = MibScalar
gs2310MSTI5RootPort = _Gs2310MSTI5RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 4),
    _Gs2310MSTI5RootPort_Type()
)
gs2310MSTI5RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5RootPort.setStatus("current")


class _Gs2310MSTI5RootCost_Type(Integer32):
    """Custom type gs2310MSTI5RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI5RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI5RootCost_Object = MibScalar
gs2310MSTI5RootCost = _Gs2310MSTI5RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 5),
    _Gs2310MSTI5RootCost_Type()
)
gs2310MSTI5RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5RootCost.setStatus("current")
_Gs2310MSTI5TopologyFlag_Type = DisplayString
_Gs2310MSTI5TopologyFlag_Object = MibScalar
gs2310MSTI5TopologyFlag = _Gs2310MSTI5TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 8),
    _Gs2310MSTI5TopologyFlag_Type()
)
gs2310MSTI5TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5TopologyFlag.setStatus("current")
_Gs2310MSTI5TopologyChangeCount_Type = Counter32
_Gs2310MSTI5TopologyChangeCount_Object = MibScalar
gs2310MSTI5TopologyChangeCount = _Gs2310MSTI5TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 9),
    _Gs2310MSTI5TopologyChangeCount_Type()
)
gs2310MSTI5TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5TopologyChangeCount.setStatus("current")
_Gs2310MSTI5TopologyChangeLast_Type = DisplayString
_Gs2310MSTI5TopologyChangeLast_Object = MibScalar
gs2310MSTI5TopologyChangeLast = _Gs2310MSTI5TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 1, 10),
    _Gs2310MSTI5TopologyChangeLast_Type()
)
gs2310MSTI5TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5TopologyChangeLast.setStatus("current")
_Gs2310MSTI5PortStateTable_Object = MibTable
gs2310MSTI5PortStateTable = _Gs2310MSTI5PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateTable.setStatus("current")
_Gs2310MSTI5PortStateEntry_Object = MibTableRow
gs2310MSTI5PortStateEntry = _Gs2310MSTI5PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1)
)
gs2310MSTI5PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI5PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateEntry.setStatus("current")


class _Gs2310MSTI5PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI5PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI5PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI5PortStateIndex_Object = MibTableColumn
gs2310MSTI5PortStateIndex = _Gs2310MSTI5PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 1),
    _Gs2310MSTI5PortStateIndex_Type()
)
gs2310MSTI5PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateIndex.setStatus("current")
_Gs2310MSTI5PortStatePort_Type = DisplayString
_Gs2310MSTI5PortStatePort_Object = MibTableColumn
gs2310MSTI5PortStatePort = _Gs2310MSTI5PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 2),
    _Gs2310MSTI5PortStatePort_Type()
)
gs2310MSTI5PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStatePort.setStatus("current")
_Gs2310MSTI5PortStatePortID_Type = DisplayString
_Gs2310MSTI5PortStatePortID_Object = MibTableColumn
gs2310MSTI5PortStatePortID = _Gs2310MSTI5PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 3),
    _Gs2310MSTI5PortStatePortID_Type()
)
gs2310MSTI5PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStatePortID.setStatus("current")
_Gs2310MSTI5PortStateRole_Type = DisplayString
_Gs2310MSTI5PortStateRole_Object = MibTableColumn
gs2310MSTI5PortStateRole = _Gs2310MSTI5PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 4),
    _Gs2310MSTI5PortStateRole_Type()
)
gs2310MSTI5PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateRole.setStatus("current")
_Gs2310MSTI5PortStateState_Type = DisplayString
_Gs2310MSTI5PortStateState_Object = MibTableColumn
gs2310MSTI5PortStateState = _Gs2310MSTI5PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 5),
    _Gs2310MSTI5PortStateState_Type()
)
gs2310MSTI5PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateState.setStatus("current")


class _Gs2310MSTI5PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI5PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI5PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI5PortStatePathCost_Object = MibTableColumn
gs2310MSTI5PortStatePathCost = _Gs2310MSTI5PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 6),
    _Gs2310MSTI5PortStatePathCost_Type()
)
gs2310MSTI5PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStatePathCost.setStatus("current")
_Gs2310MSTI5PortStateEdge_Type = DisplayString
_Gs2310MSTI5PortStateEdge_Object = MibTableColumn
gs2310MSTI5PortStateEdge = _Gs2310MSTI5PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 7),
    _Gs2310MSTI5PortStateEdge_Type()
)
gs2310MSTI5PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateEdge.setStatus("current")
_Gs2310MSTI5PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI5PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI5PortStatePoint2Point = _Gs2310MSTI5PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 8),
    _Gs2310MSTI5PortStatePoint2Point_Type()
)
gs2310MSTI5PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStatePoint2Point.setStatus("current")
_Gs2310MSTI5PortStateUptime_Type = DisplayString
_Gs2310MSTI5PortStateUptime_Object = MibTableColumn
gs2310MSTI5PortStateUptime = _Gs2310MSTI5PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 6, 2, 1, 9),
    _Gs2310MSTI5PortStateUptime_Type()
)
gs2310MSTI5PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI5PortStateUptime.setStatus("current")
_Gs2310MSTI6BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI6BridgeSTP = _Gs2310MSTI6BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7)
)
_Gs2310MSTI6BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI6BridgeSTPStatus = _Gs2310MSTI6BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1)
)
_Gs2310MSTI6BridgeInstance_Type = DisplayString
_Gs2310MSTI6BridgeInstance_Object = MibScalar
gs2310MSTI6BridgeInstance = _Gs2310MSTI6BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 1),
    _Gs2310MSTI6BridgeInstance_Type()
)
gs2310MSTI6BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6BridgeInstance.setStatus("current")
_Gs2310MSTI6BridgeID_Type = DisplayString
_Gs2310MSTI6BridgeID_Object = MibScalar
gs2310MSTI6BridgeID = _Gs2310MSTI6BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 2),
    _Gs2310MSTI6BridgeID_Type()
)
gs2310MSTI6BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6BridgeID.setStatus("current")
_Gs2310MSTI6RootID_Type = DisplayString
_Gs2310MSTI6RootID_Object = MibScalar
gs2310MSTI6RootID = _Gs2310MSTI6RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 3),
    _Gs2310MSTI6RootID_Type()
)
gs2310MSTI6RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6RootID.setStatus("current")
_Gs2310MSTI6RootPort_Type = DisplayString
_Gs2310MSTI6RootPort_Object = MibScalar
gs2310MSTI6RootPort = _Gs2310MSTI6RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 4),
    _Gs2310MSTI6RootPort_Type()
)
gs2310MSTI6RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6RootPort.setStatus("current")


class _Gs2310MSTI6RootCost_Type(Integer32):
    """Custom type gs2310MSTI6RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI6RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI6RootCost_Object = MibScalar
gs2310MSTI6RootCost = _Gs2310MSTI6RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 5),
    _Gs2310MSTI6RootCost_Type()
)
gs2310MSTI6RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6RootCost.setStatus("current")
_Gs2310MSTI6TopologyFlag_Type = DisplayString
_Gs2310MSTI6TopologyFlag_Object = MibScalar
gs2310MSTI6TopologyFlag = _Gs2310MSTI6TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 8),
    _Gs2310MSTI6TopologyFlag_Type()
)
gs2310MSTI6TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6TopologyFlag.setStatus("current")
_Gs2310MSTI6TopologyChangeCount_Type = Counter32
_Gs2310MSTI6TopologyChangeCount_Object = MibScalar
gs2310MSTI6TopologyChangeCount = _Gs2310MSTI6TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 9),
    _Gs2310MSTI6TopologyChangeCount_Type()
)
gs2310MSTI6TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6TopologyChangeCount.setStatus("current")
_Gs2310MSTI6TopologyChangeLast_Type = DisplayString
_Gs2310MSTI6TopologyChangeLast_Object = MibScalar
gs2310MSTI6TopologyChangeLast = _Gs2310MSTI6TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 1, 10),
    _Gs2310MSTI6TopologyChangeLast_Type()
)
gs2310MSTI6TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6TopologyChangeLast.setStatus("current")
_Gs2310MSTI6PortStateTable_Object = MibTable
gs2310MSTI6PortStateTable = _Gs2310MSTI6PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateTable.setStatus("current")
_Gs2310MSTI6PortStateEntry_Object = MibTableRow
gs2310MSTI6PortStateEntry = _Gs2310MSTI6PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1)
)
gs2310MSTI6PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI6PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateEntry.setStatus("current")


class _Gs2310MSTI6PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI6PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI6PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI6PortStateIndex_Object = MibTableColumn
gs2310MSTI6PortStateIndex = _Gs2310MSTI6PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 1),
    _Gs2310MSTI6PortStateIndex_Type()
)
gs2310MSTI6PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateIndex.setStatus("current")
_Gs2310MSTI6PortStatePort_Type = DisplayString
_Gs2310MSTI6PortStatePort_Object = MibTableColumn
gs2310MSTI6PortStatePort = _Gs2310MSTI6PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 2),
    _Gs2310MSTI6PortStatePort_Type()
)
gs2310MSTI6PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStatePort.setStatus("current")
_Gs2310MSTI6PortStatePortID_Type = DisplayString
_Gs2310MSTI6PortStatePortID_Object = MibTableColumn
gs2310MSTI6PortStatePortID = _Gs2310MSTI6PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 3),
    _Gs2310MSTI6PortStatePortID_Type()
)
gs2310MSTI6PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStatePortID.setStatus("current")
_Gs2310MSTI6PortStateRole_Type = DisplayString
_Gs2310MSTI6PortStateRole_Object = MibTableColumn
gs2310MSTI6PortStateRole = _Gs2310MSTI6PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 4),
    _Gs2310MSTI6PortStateRole_Type()
)
gs2310MSTI6PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateRole.setStatus("current")
_Gs2310MSTI6PortStateState_Type = DisplayString
_Gs2310MSTI6PortStateState_Object = MibTableColumn
gs2310MSTI6PortStateState = _Gs2310MSTI6PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 5),
    _Gs2310MSTI6PortStateState_Type()
)
gs2310MSTI6PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateState.setStatus("current")


class _Gs2310MSTI6PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI6PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI6PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI6PortStatePathCost_Object = MibTableColumn
gs2310MSTI6PortStatePathCost = _Gs2310MSTI6PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 6),
    _Gs2310MSTI6PortStatePathCost_Type()
)
gs2310MSTI6PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStatePathCost.setStatus("current")
_Gs2310MSTI6PortStateEdge_Type = DisplayString
_Gs2310MSTI6PortStateEdge_Object = MibTableColumn
gs2310MSTI6PortStateEdge = _Gs2310MSTI6PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 7),
    _Gs2310MSTI6PortStateEdge_Type()
)
gs2310MSTI6PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateEdge.setStatus("current")
_Gs2310MSTI6PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI6PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI6PortStatePoint2Point = _Gs2310MSTI6PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 8),
    _Gs2310MSTI6PortStatePoint2Point_Type()
)
gs2310MSTI6PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStatePoint2Point.setStatus("current")
_Gs2310MSTI6PortStateUptime_Type = DisplayString
_Gs2310MSTI6PortStateUptime_Object = MibTableColumn
gs2310MSTI6PortStateUptime = _Gs2310MSTI6PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 7, 2, 1, 9),
    _Gs2310MSTI6PortStateUptime_Type()
)
gs2310MSTI6PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI6PortStateUptime.setStatus("current")
_Gs2310MSTI7BridgeSTP_ObjectIdentity = ObjectIdentity
gs2310MSTI7BridgeSTP = _Gs2310MSTI7BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8)
)
_Gs2310MSTI7BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2310MSTI7BridgeSTPStatus = _Gs2310MSTI7BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1)
)
_Gs2310MSTI7BridgeInstance_Type = DisplayString
_Gs2310MSTI7BridgeInstance_Object = MibScalar
gs2310MSTI7BridgeInstance = _Gs2310MSTI7BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 1),
    _Gs2310MSTI7BridgeInstance_Type()
)
gs2310MSTI7BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7BridgeInstance.setStatus("current")
_Gs2310MSTI7BridgeID_Type = DisplayString
_Gs2310MSTI7BridgeID_Object = MibScalar
gs2310MSTI7BridgeID = _Gs2310MSTI7BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 2),
    _Gs2310MSTI7BridgeID_Type()
)
gs2310MSTI7BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7BridgeID.setStatus("current")
_Gs2310MSTI7RootID_Type = DisplayString
_Gs2310MSTI7RootID_Object = MibScalar
gs2310MSTI7RootID = _Gs2310MSTI7RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 3),
    _Gs2310MSTI7RootID_Type()
)
gs2310MSTI7RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7RootID.setStatus("current")
_Gs2310MSTI7RootPort_Type = DisplayString
_Gs2310MSTI7RootPort_Object = MibScalar
gs2310MSTI7RootPort = _Gs2310MSTI7RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 4),
    _Gs2310MSTI7RootPort_Type()
)
gs2310MSTI7RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7RootPort.setStatus("current")


class _Gs2310MSTI7RootCost_Type(Integer32):
    """Custom type gs2310MSTI7RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI7RootCost_Type.__name__ = "Integer32"
_Gs2310MSTI7RootCost_Object = MibScalar
gs2310MSTI7RootCost = _Gs2310MSTI7RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 5),
    _Gs2310MSTI7RootCost_Type()
)
gs2310MSTI7RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7RootCost.setStatus("current")
_Gs2310MSTI7TopologyFlag_Type = DisplayString
_Gs2310MSTI7TopologyFlag_Object = MibScalar
gs2310MSTI7TopologyFlag = _Gs2310MSTI7TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 8),
    _Gs2310MSTI7TopologyFlag_Type()
)
gs2310MSTI7TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7TopologyFlag.setStatus("current")
_Gs2310MSTI7TopologyChangeCount_Type = Counter32
_Gs2310MSTI7TopologyChangeCount_Object = MibScalar
gs2310MSTI7TopologyChangeCount = _Gs2310MSTI7TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 9),
    _Gs2310MSTI7TopologyChangeCount_Type()
)
gs2310MSTI7TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7TopologyChangeCount.setStatus("current")
_Gs2310MSTI7TopologyChangeLast_Type = DisplayString
_Gs2310MSTI7TopologyChangeLast_Object = MibScalar
gs2310MSTI7TopologyChangeLast = _Gs2310MSTI7TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 1, 10),
    _Gs2310MSTI7TopologyChangeLast_Type()
)
gs2310MSTI7TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7TopologyChangeLast.setStatus("current")
_Gs2310MSTI7PortStateTable_Object = MibTable
gs2310MSTI7PortStateTable = _Gs2310MSTI7PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2)
)
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateTable.setStatus("current")
_Gs2310MSTI7PortStateEntry_Object = MibTableRow
gs2310MSTI7PortStateEntry = _Gs2310MSTI7PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1)
)
gs2310MSTI7PortStateEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310MSTI7PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateEntry.setStatus("current")


class _Gs2310MSTI7PortStateIndex_Type(Integer32):
    """Custom type gs2310MSTI7PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310MSTI7PortStateIndex_Type.__name__ = "Integer32"
_Gs2310MSTI7PortStateIndex_Object = MibTableColumn
gs2310MSTI7PortStateIndex = _Gs2310MSTI7PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 1),
    _Gs2310MSTI7PortStateIndex_Type()
)
gs2310MSTI7PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateIndex.setStatus("current")
_Gs2310MSTI7PortStatePort_Type = DisplayString
_Gs2310MSTI7PortStatePort_Object = MibTableColumn
gs2310MSTI7PortStatePort = _Gs2310MSTI7PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 2),
    _Gs2310MSTI7PortStatePort_Type()
)
gs2310MSTI7PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStatePort.setStatus("current")
_Gs2310MSTI7PortStatePortID_Type = DisplayString
_Gs2310MSTI7PortStatePortID_Object = MibTableColumn
gs2310MSTI7PortStatePortID = _Gs2310MSTI7PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 3),
    _Gs2310MSTI7PortStatePortID_Type()
)
gs2310MSTI7PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStatePortID.setStatus("current")
_Gs2310MSTI7PortStateRole_Type = DisplayString
_Gs2310MSTI7PortStateRole_Object = MibTableColumn
gs2310MSTI7PortStateRole = _Gs2310MSTI7PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 4),
    _Gs2310MSTI7PortStateRole_Type()
)
gs2310MSTI7PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateRole.setStatus("current")
_Gs2310MSTI7PortStateState_Type = DisplayString
_Gs2310MSTI7PortStateState_Object = MibTableColumn
gs2310MSTI7PortStateState = _Gs2310MSTI7PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 5),
    _Gs2310MSTI7PortStateState_Type()
)
gs2310MSTI7PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateState.setStatus("current")


class _Gs2310MSTI7PortStatePathCost_Type(Integer32):
    """Custom type gs2310MSTI7PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2310MSTI7PortStatePathCost_Type.__name__ = "Integer32"
_Gs2310MSTI7PortStatePathCost_Object = MibTableColumn
gs2310MSTI7PortStatePathCost = _Gs2310MSTI7PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 6),
    _Gs2310MSTI7PortStatePathCost_Type()
)
gs2310MSTI7PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStatePathCost.setStatus("current")
_Gs2310MSTI7PortStateEdge_Type = DisplayString
_Gs2310MSTI7PortStateEdge_Object = MibTableColumn
gs2310MSTI7PortStateEdge = _Gs2310MSTI7PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 7),
    _Gs2310MSTI7PortStateEdge_Type()
)
gs2310MSTI7PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateEdge.setStatus("current")
_Gs2310MSTI7PortStatePoint2Point_Type = DisplayString
_Gs2310MSTI7PortStatePoint2Point_Object = MibTableColumn
gs2310MSTI7PortStatePoint2Point = _Gs2310MSTI7PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 8),
    _Gs2310MSTI7PortStatePoint2Point_Type()
)
gs2310MSTI7PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStatePoint2Point.setStatus("current")
_Gs2310MSTI7PortStateUptime_Type = DisplayString
_Gs2310MSTI7PortStateUptime_Object = MibTableColumn
gs2310MSTI7PortStateUptime = _Gs2310MSTI7PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 8, 8, 2, 1, 9),
    _Gs2310MSTI7PortStateUptime_Type()
)
gs2310MSTI7PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310MSTI7PortStateUptime.setStatus("current")
_Gs2310STPPortStatusTable_Object = MibTable
gs2310STPPortStatusTable = _Gs2310STPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 9)
)
if mibBuilder.loadTexts:
    gs2310STPPortStatusTable.setStatus("current")
_Gs2310STPPortStatusEntry_Object = MibTableRow
gs2310STPPortStatusEntry = _Gs2310STPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 9, 1)
)
gs2310STPPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPPortStatusPort"),
)
if mibBuilder.loadTexts:
    gs2310STPPortStatusEntry.setStatus("current")


class _Gs2310STPPortStatusPort_Type(Integer32):
    """Custom type gs2310STPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPPortStatusPort_Type.__name__ = "Integer32"
_Gs2310STPPortStatusPort_Object = MibTableColumn
gs2310STPPortStatusPort = _Gs2310STPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 9, 1, 1),
    _Gs2310STPPortStatusPort_Type()
)
gs2310STPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPPortStatusPort.setStatus("current")
_Gs2310STPPortStatusCISTRole_Type = DisplayString
_Gs2310STPPortStatusCISTRole_Object = MibTableColumn
gs2310STPPortStatusCISTRole = _Gs2310STPPortStatusCISTRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 9, 1, 2),
    _Gs2310STPPortStatusCISTRole_Type()
)
gs2310STPPortStatusCISTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPPortStatusCISTRole.setStatus("current")
_Gs2310STPPortStatusCISTState_Type = DisplayString
_Gs2310STPPortStatusCISTState_Object = MibTableColumn
gs2310STPPortStatusCISTState = _Gs2310STPPortStatusCISTState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 9, 1, 3),
    _Gs2310STPPortStatusCISTState_Type()
)
gs2310STPPortStatusCISTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPPortStatusCISTState.setStatus("current")
_Gs2310STPPortStatusUptime_Type = DisplayString
_Gs2310STPPortStatusUptime_Object = MibTableColumn
gs2310STPPortStatusUptime = _Gs2310STPPortStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 9, 1, 4),
    _Gs2310STPPortStatusUptime_Type()
)
gs2310STPPortStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPPortStatusUptime.setStatus("current")
_Gs2310STPPortStatisticsTable_Object = MibTable
gs2310STPPortStatisticsTable = _Gs2310STPPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10)
)
if mibBuilder.loadTexts:
    gs2310STPPortStatisticsTable.setStatus("current")
_Gs2310STPPortStatisticsEntry_Object = MibTableRow
gs2310STPPortStatisticsEntry = _Gs2310STPPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1)
)
gs2310STPPortStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310STPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gs2310STPPortStatisticsEntry.setStatus("current")


class _Gs2310STPStatisticsIndex_Type(Integer32):
    """Custom type gs2310STPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310STPStatisticsIndex_Type.__name__ = "Integer32"
_Gs2310STPStatisticsIndex_Object = MibTableColumn
gs2310STPStatisticsIndex = _Gs2310STPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 1),
    _Gs2310STPStatisticsIndex_Type()
)
gs2310STPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPStatisticsIndex.setStatus("current")
_Gs2310STPStatisticsPort_Type = DisplayString
_Gs2310STPStatisticsPort_Object = MibTableColumn
gs2310STPStatisticsPort = _Gs2310STPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 2),
    _Gs2310STPStatisticsPort_Type()
)
gs2310STPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310STPStatisticsPort.setStatus("current")
_Gs2310STPStatisticsTxMSTP_Type = Counter32
_Gs2310STPStatisticsTxMSTP_Object = MibTableColumn
gs2310STPStatisticsTxMSTP = _Gs2310STPStatisticsTxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 3),
    _Gs2310STPStatisticsTxMSTP_Type()
)
gs2310STPStatisticsTxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsTxMSTP.setStatus("current")
_Gs2310STPStatisticsTxRSTP_Type = Counter32
_Gs2310STPStatisticsTxRSTP_Object = MibTableColumn
gs2310STPStatisticsTxRSTP = _Gs2310STPStatisticsTxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 4),
    _Gs2310STPStatisticsTxRSTP_Type()
)
gs2310STPStatisticsTxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsTxRSTP.setStatus("current")
_Gs2310STPStatisticsTxSTP_Type = Counter32
_Gs2310STPStatisticsTxSTP_Object = MibTableColumn
gs2310STPStatisticsTxSTP = _Gs2310STPStatisticsTxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 5),
    _Gs2310STPStatisticsTxSTP_Type()
)
gs2310STPStatisticsTxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsTxSTP.setStatus("current")
_Gs2310STPStatisticsTxTCN_Type = Counter32
_Gs2310STPStatisticsTxTCN_Object = MibTableColumn
gs2310STPStatisticsTxTCN = _Gs2310STPStatisticsTxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 6),
    _Gs2310STPStatisticsTxTCN_Type()
)
gs2310STPStatisticsTxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsTxTCN.setStatus("current")
_Gs2310STPStatisticsRxMSTP_Type = Counter32
_Gs2310STPStatisticsRxMSTP_Object = MibTableColumn
gs2310STPStatisticsRxMSTP = _Gs2310STPStatisticsRxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 7),
    _Gs2310STPStatisticsRxMSTP_Type()
)
gs2310STPStatisticsRxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsRxMSTP.setStatus("current")
_Gs2310STPStatisticsRxRSTP_Type = Counter32
_Gs2310STPStatisticsRxRSTP_Object = MibTableColumn
gs2310STPStatisticsRxRSTP = _Gs2310STPStatisticsRxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 8),
    _Gs2310STPStatisticsRxRSTP_Type()
)
gs2310STPStatisticsRxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsRxRSTP.setStatus("current")
_Gs2310STPStatisticsRxSTP_Type = Counter32
_Gs2310STPStatisticsRxSTP_Object = MibTableColumn
gs2310STPStatisticsRxSTP = _Gs2310STPStatisticsRxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 9),
    _Gs2310STPStatisticsRxSTP_Type()
)
gs2310STPStatisticsRxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsRxSTP.setStatus("current")
_Gs2310STPStatisticsRxTCN_Type = Counter32
_Gs2310STPStatisticsRxTCN_Object = MibTableColumn
gs2310STPStatisticsRxTCN = _Gs2310STPStatisticsRxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 10),
    _Gs2310STPStatisticsRxTCN_Type()
)
gs2310STPStatisticsRxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsRxTCN.setStatus("current")
_Gs2310STPStatisticsDiscardedUnknown_Type = Counter32
_Gs2310STPStatisticsDiscardedUnknown_Object = MibTableColumn
gs2310STPStatisticsDiscardedUnknown = _Gs2310STPStatisticsDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 11),
    _Gs2310STPStatisticsDiscardedUnknown_Type()
)
gs2310STPStatisticsDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsDiscardedUnknown.setStatus("current")
_Gs2310STPStatisticsDiscardedIllegal_Type = Counter32
_Gs2310STPStatisticsDiscardedIllegal_Object = MibTableColumn
gs2310STPStatisticsDiscardedIllegal = _Gs2310STPStatisticsDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 20, 10, 1, 12),
    _Gs2310STPStatisticsDiscardedIllegal_Type()
)
gs2310STPStatisticsDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310STPStatisticsDiscardedIllegal.setStatus("current")
_Gs2310FilteringDataBase_ObjectIdentity = ObjectIdentity
gs2310FilteringDataBase = _Gs2310FilteringDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21)
)
_Gs2310FilteringDataBaseConfig_ObjectIdentity = ObjectIdentity
gs2310FilteringDataBaseConfig = _Gs2310FilteringDataBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1)
)


class _Gs2310FilteringDataBaseAgingTime_Type(Integer32):
    """Custom type gs2310FilteringDataBaseAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2310FilteringDataBaseAgingTime_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseAgingTime_Object = MibScalar
gs2310FilteringDataBaseAgingTime = _Gs2310FilteringDataBaseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 1),
    _Gs2310FilteringDataBaseAgingTime_Type()
)
gs2310FilteringDataBaseAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseAgingTime.setStatus("current")
_Gs2310FilteringDataBaseConfigTable_Object = MibTable
gs2310FilteringDataBaseConfigTable = _Gs2310FilteringDataBaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseConfigTable.setStatus("current")
_Gs2310FilteringDataBaseConfigEntry_Object = MibTableRow
gs2310FilteringDataBaseConfigEntry = _Gs2310FilteringDataBaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 2, 1)
)
gs2310FilteringDataBaseConfigEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310FilteringDataBaseConfigPort"),
)
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseConfigEntry.setStatus("current")


class _Gs2310FilteringDataBaseConfigPort_Type(Integer32):
    """Custom type gs2310FilteringDataBaseConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310FilteringDataBaseConfigPort_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseConfigPort_Object = MibTableColumn
gs2310FilteringDataBaseConfigPort = _Gs2310FilteringDataBaseConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 2, 1, 1),
    _Gs2310FilteringDataBaseConfigPort_Type()
)
gs2310FilteringDataBaseConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseConfigPort.setStatus("current")


class _Gs2310FilteringDataBaseConfigLearning_Type(Integer32):
    """Custom type gs2310FilteringDataBaseConfigLearning based on Integer32"""
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


_Gs2310FilteringDataBaseConfigLearning_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseConfigLearning_Object = MibTableColumn
gs2310FilteringDataBaseConfigLearning = _Gs2310FilteringDataBaseConfigLearning_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 2, 1, 2),
    _Gs2310FilteringDataBaseConfigLearning_Type()
)
gs2310FilteringDataBaseConfigLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseConfigLearning.setStatus("current")
_Gs2310FilteringDataBaseStaticMAC_ObjectIdentity = ObjectIdentity
gs2310FilteringDataBaseStaticMAC = _Gs2310FilteringDataBaseStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3)
)


class _Gs2310FilteringDataBaseStaticMACCreate_Type(Integer32):
    """Custom type gs2310FilteringDataBaseStaticMACCreate based on Integer32"""
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


_Gs2310FilteringDataBaseStaticMACCreate_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseStaticMACCreate_Object = MibScalar
gs2310FilteringDataBaseStaticMACCreate = _Gs2310FilteringDataBaseStaticMACCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 1),
    _Gs2310FilteringDataBaseStaticMACCreate_Type()
)
gs2310FilteringDataBaseStaticMACCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACCreate.setStatus("current")
_Gs2310FilteringDataBaseStaticMACTable_Object = MibTable
gs2310FilteringDataBaseStaticMACTable = _Gs2310FilteringDataBaseStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACTable.setStatus("current")
_Gs2310FilteringDataBaseStaticMACEntry_Object = MibTableRow
gs2310FilteringDataBaseStaticMACEntry = _Gs2310FilteringDataBaseStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2, 1)
)
gs2310FilteringDataBaseStaticMACEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310FilteringDataBaseStaticMACIndex"),
)
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACEntry.setStatus("current")


class _Gs2310FilteringDataBaseStaticMACIndex_Type(Integer32):
    """Custom type gs2310FilteringDataBaseStaticMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310FilteringDataBaseStaticMACIndex_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseStaticMACIndex_Object = MibTableColumn
gs2310FilteringDataBaseStaticMACIndex = _Gs2310FilteringDataBaseStaticMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2, 1, 1),
    _Gs2310FilteringDataBaseStaticMACIndex_Type()
)
gs2310FilteringDataBaseStaticMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACIndex.setStatus("current")


class _Gs2310FilteringDataBaseStaticMACVLANId_Type(Integer32):
    """Custom type gs2310FilteringDataBaseStaticMACVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310FilteringDataBaseStaticMACVLANId_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseStaticMACVLANId_Object = MibTableColumn
gs2310FilteringDataBaseStaticMACVLANId = _Gs2310FilteringDataBaseStaticMACVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2, 1, 2),
    _Gs2310FilteringDataBaseStaticMACVLANId_Type()
)
gs2310FilteringDataBaseStaticMACVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACVLANId.setStatus("current")
_Gs2310FilteringDataBaseStaticMACAddress_Type = MacAddress
_Gs2310FilteringDataBaseStaticMACAddress_Object = MibTableColumn
gs2310FilteringDataBaseStaticMACAddress = _Gs2310FilteringDataBaseStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2, 1, 3),
    _Gs2310FilteringDataBaseStaticMACAddress_Type()
)
gs2310FilteringDataBaseStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACAddress.setStatus("current")
_Gs2310FilteringDataBaseStaticMACPortMembers_Type = DisplayString
_Gs2310FilteringDataBaseStaticMACPortMembers_Object = MibTableColumn
gs2310FilteringDataBaseStaticMACPortMembers = _Gs2310FilteringDataBaseStaticMACPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2, 1, 4),
    _Gs2310FilteringDataBaseStaticMACPortMembers_Type()
)
gs2310FilteringDataBaseStaticMACPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACPortMembers.setStatus("current")


class _Gs2310FilteringDataBaseStaticMACRowStatus_Type(Integer32):
    """Custom type gs2310FilteringDataBaseStaticMACRowStatus based on Integer32"""
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


_Gs2310FilteringDataBaseStaticMACRowStatus_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseStaticMACRowStatus_Object = MibTableColumn
gs2310FilteringDataBaseStaticMACRowStatus = _Gs2310FilteringDataBaseStaticMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 3, 2, 1, 5),
    _Gs2310FilteringDataBaseStaticMACRowStatus_Type()
)
gs2310FilteringDataBaseStaticMACRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseStaticMACRowStatus.setStatus("current")
_Gs2310FilteringDataBaseDynamicMACTable_Object = MibTable
gs2310FilteringDataBaseDynamicMACTable = _Gs2310FilteringDataBaseDynamicMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicMACTable.setStatus("current")
_Gs2310FilteringDataBaseDynamicMACEntry_Object = MibTableRow
gs2310FilteringDataBaseDynamicMACEntry = _Gs2310FilteringDataBaseDynamicMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4, 1)
)
gs2310FilteringDataBaseDynamicMACEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310FilteringDataBaseDynamicMACIndex"),
)
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicMACEntry.setStatus("current")


class _Gs2310FilteringDataBaseDynamicMACIndex_Type(Integer32):
    """Custom type gs2310FilteringDataBaseDynamicMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310FilteringDataBaseDynamicMACIndex_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseDynamicMACIndex_Object = MibTableColumn
gs2310FilteringDataBaseDynamicMACIndex = _Gs2310FilteringDataBaseDynamicMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4, 1, 1),
    _Gs2310FilteringDataBaseDynamicMACIndex_Type()
)
gs2310FilteringDataBaseDynamicMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicMACIndex.setStatus("current")


class _Gs2310FilteringDataBaseDynamicMACType_Type(Integer32):
    """Custom type gs2310FilteringDataBaseDynamicMACType based on Integer32"""
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


_Gs2310FilteringDataBaseDynamicMACType_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseDynamicMACType_Object = MibTableColumn
gs2310FilteringDataBaseDynamicMACType = _Gs2310FilteringDataBaseDynamicMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4, 1, 2),
    _Gs2310FilteringDataBaseDynamicMACType_Type()
)
gs2310FilteringDataBaseDynamicMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicMACType.setStatus("current")


class _Gs2310FilteringDataBaseDynamicMACVLAN_Type(Integer32):
    """Custom type gs2310FilteringDataBaseDynamicMACVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310FilteringDataBaseDynamicMACVLAN_Type.__name__ = "Integer32"
_Gs2310FilteringDataBaseDynamicMACVLAN_Object = MibTableColumn
gs2310FilteringDataBaseDynamicMACVLAN = _Gs2310FilteringDataBaseDynamicMACVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4, 1, 3),
    _Gs2310FilteringDataBaseDynamicMACVLAN_Type()
)
gs2310FilteringDataBaseDynamicMACVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicMACVLAN.setStatus("current")
_Gs2310FilteringDataBaseDynamicMACAddress_Type = MacAddress
_Gs2310FilteringDataBaseDynamicMACAddress_Object = MibTableColumn
gs2310FilteringDataBaseDynamicMACAddress = _Gs2310FilteringDataBaseDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4, 1, 4),
    _Gs2310FilteringDataBaseDynamicMACAddress_Type()
)
gs2310FilteringDataBaseDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicMACAddress.setStatus("current")
_Gs2310FilteringDataBaseDynamicPortMembers_Type = DisplayString
_Gs2310FilteringDataBaseDynamicPortMembers_Object = MibTableColumn
gs2310FilteringDataBaseDynamicPortMembers = _Gs2310FilteringDataBaseDynamicPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 21, 1, 4, 1, 5),
    _Gs2310FilteringDataBaseDynamicPortMembers_Type()
)
gs2310FilteringDataBaseDynamicPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310FilteringDataBaseDynamicPortMembers.setStatus("current")
_Gs2310SFlowAgent_ObjectIdentity = ObjectIdentity
gs2310SFlowAgent = _Gs2310SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 22)
)
_Gs2310SFlowAgentCollector_ObjectIdentity = ObjectIdentity
gs2310SFlowAgentCollector = _Gs2310SFlowAgentCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 22, 1)
)


class _Gs2310SFlowAgentReceiverMode_Type(Integer32):
    """Custom type gs2310SFlowAgentReceiverMode based on Integer32"""
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


_Gs2310SFlowAgentReceiverMode_Type.__name__ = "Integer32"
_Gs2310SFlowAgentReceiverMode_Object = MibScalar
gs2310SFlowAgentReceiverMode = _Gs2310SFlowAgentReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 22, 1, 1),
    _Gs2310SFlowAgentReceiverMode_Type()
)
gs2310SFlowAgentReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SFlowAgentReceiverMode.setStatus("current")
_Gs2310LMC_ObjectIdentity = ObjectIdentity
gs2310LMC = _Gs2310LMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500)
)


class _Gs2310LMCOperating_Type(Integer32):
    """Custom type gs2310LMCOperating based on Integer32"""
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


_Gs2310LMCOperating_Type.__name__ = "Integer32"
_Gs2310LMCOperating_Object = MibScalar
gs2310LMCOperating = _Gs2310LMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 1),
    _Gs2310LMCOperating_Type()
)
gs2310LMCOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LMCOperating.setStatus("current")


class _Gs2310LMCConfigViaDhcp_Type(Integer32):
    """Custom type gs2310LMCConfigViaDhcp based on Integer32"""
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


_Gs2310LMCConfigViaDhcp_Type.__name__ = "Integer32"
_Gs2310LMCConfigViaDhcp_Object = MibScalar
gs2310LMCConfigViaDhcp = _Gs2310LMCConfigViaDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 2),
    _Gs2310LMCConfigViaDhcp_Type()
)
gs2310LMCConfigViaDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LMCConfigViaDhcp.setStatus("current")


class _Gs2310LMCDomain_Type(DisplayString):
    """Custom type gs2310LMCDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gs2310LMCDomain_Type.__name__ = "DisplayString"
_Gs2310LMCDomain_Object = MibScalar
gs2310LMCDomain = _Gs2310LMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 3),
    _Gs2310LMCDomain_Type()
)
gs2310LMCDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LMCDomain.setStatus("current")


class _Gs2310LMCDhcpClientAutoRenew_Type(Integer32):
    """Custom type gs2310LMCDhcpClientAutoRenew based on Integer32"""
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


_Gs2310LMCDhcpClientAutoRenew_Type.__name__ = "Integer32"
_Gs2310LMCDhcpClientAutoRenew_Object = MibScalar
gs2310LMCDhcpClientAutoRenew = _Gs2310LMCDhcpClientAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 4),
    _Gs2310LMCDhcpClientAutoRenew_Type()
)
gs2310LMCDhcpClientAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LMCDhcpClientAutoRenew.setStatus("current")


class _Gs2310LMCZeroTouchSupport_Type(Integer32):
    """Custom type gs2310LMCZeroTouchSupport based on Integer32"""
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


_Gs2310LMCZeroTouchSupport_Type.__name__ = "Integer32"
_Gs2310LMCZeroTouchSupport_Object = MibScalar
gs2310LMCZeroTouchSupport = _Gs2310LMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 50),
    _Gs2310LMCZeroTouchSupport_Type()
)
gs2310LMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCZeroTouchSupport.setStatus("current")


class _Gs2310LMCPairingTokenPresent_Type(Integer32):
    """Custom type gs2310LMCPairingTokenPresent based on Integer32"""
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


_Gs2310LMCPairingTokenPresent_Type.__name__ = "Integer32"
_Gs2310LMCPairingTokenPresent_Object = MibScalar
gs2310LMCPairingTokenPresent = _Gs2310LMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 51),
    _Gs2310LMCPairingTokenPresent_Type()
)
gs2310LMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCPairingTokenPresent.setStatus("current")
_Gs2310LMCClientStatus_Type = DisplayString
_Gs2310LMCClientStatus_Object = MibScalar
gs2310LMCClientStatus = _Gs2310LMCClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 52),
    _Gs2310LMCClientStatus_Type()
)
gs2310LMCClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCClientStatus.setStatus("current")


class _Gs2310LMCManagementStatus_Type(Integer32):
    """Custom type gs2310LMCManagementStatus based on Integer32"""
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


_Gs2310LMCManagementStatus_Type.__name__ = "Integer32"
_Gs2310LMCManagementStatus_Object = MibScalar
gs2310LMCManagementStatus = _Gs2310LMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 53),
    _Gs2310LMCManagementStatus_Type()
)
gs2310LMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCManagementStatus.setStatus("current")


class _Gs2310LMCControlStatus_Type(Integer32):
    """Custom type gs2310LMCControlStatus based on Integer32"""
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


_Gs2310LMCControlStatus_Type.__name__ = "Integer32"
_Gs2310LMCControlStatus_Object = MibScalar
gs2310LMCControlStatus = _Gs2310LMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 54),
    _Gs2310LMCControlStatus_Type()
)
gs2310LMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCControlStatus.setStatus("current")


class _Gs2310pLMCMonitoringStatus_Type(Integer32):
    """Custom type gs2310pLMCMonitoringStatus based on Integer32"""
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


_Gs2310pLMCMonitoringStatus_Type.__name__ = "Integer32"
_Gs2310pLMCMonitoringStatus_Object = MibScalar
gs2310pLMCMonitoringStatus = _Gs2310pLMCMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 55),
    _Gs2310pLMCMonitoringStatus_Type()
)
gs2310pLMCMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310pLMCMonitoringStatus.setStatus("current")
_Gs2310LMCConfigurationSource_Type = DisplayString
_Gs2310LMCConfigurationSource_Object = MibScalar
gs2310LMCConfigurationSource = _Gs2310LMCConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 56),
    _Gs2310LMCConfigurationSource_Type()
)
gs2310LMCConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCConfigurationSource.setStatus("current")


class _Gs2310LMCConfigModified_Type(Integer32):
    """Custom type gs2310LMCConfigModified based on Integer32"""
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


_Gs2310LMCConfigModified_Type.__name__ = "Integer32"
_Gs2310LMCConfigModified_Object = MibScalar
gs2310LMCConfigModified = _Gs2310LMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 57),
    _Gs2310LMCConfigModified_Type()
)
gs2310LMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCConfigModified.setStatus("current")
_Gs2310LMCDeviceID_Type = DisplayString
_Gs2310LMCDeviceID_Object = MibScalar
gs2310LMCDeviceID = _Gs2310LMCDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 58),
    _Gs2310LMCDeviceID_Type()
)
gs2310LMCDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCDeviceID.setStatus("current")
_Gs2310LMCRoundTripTime_Type = Integer32
_Gs2310LMCRoundTripTime_Object = MibScalar
gs2310LMCRoundTripTime = _Gs2310LMCRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 2, 1500, 100),
    _Gs2310LMCRoundTripTime_Type()
)
gs2310LMCRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310LMCRoundTripTime.setStatus("current")
_Gs2310Security_ObjectIdentity = ObjectIdentity
gs2310Security = _Gs2310Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3)
)
_Gs2310IPSourceGuard_ObjectIdentity = ObjectIdentity
gs2310IPSourceGuard = _Gs2310IPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1)
)
_Gs2310IPSourceGuardConf_ObjectIdentity = ObjectIdentity
gs2310IPSourceGuardConf = _Gs2310IPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1)
)


class _Gs2310IPSourceGuardMode_Type(Integer32):
    """Custom type gs2310IPSourceGuardMode based on Integer32"""
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


_Gs2310IPSourceGuardMode_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardMode_Object = MibScalar
gs2310IPSourceGuardMode = _Gs2310IPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1, 1),
    _Gs2310IPSourceGuardMode_Type()
)
gs2310IPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardMode.setStatus("current")
_Gs2310IPSourceGuardPortConfigTable_Object = MibTable
gs2310IPSourceGuardPortConfigTable = _Gs2310IPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310IPSourceGuardPortConfigTable.setStatus("current")
_Gs2310IPSourceGuardPortConfigEntry_Object = MibTableRow
gs2310IPSourceGuardPortConfigEntry = _Gs2310IPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1, 2, 1)
)
gs2310IPSourceGuardPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2310IPSourceGuardPortConfigEntry.setStatus("current")


class _Gs2310IPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type gs2310IPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardPortConfigPort_Object = MibTableColumn
gs2310IPSourceGuardPortConfigPort = _Gs2310IPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1, 2, 1, 1),
    _Gs2310IPSourceGuardPortConfigPort_Type()
)
gs2310IPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardPortConfigPort.setStatus("current")


class _Gs2310IPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type gs2310IPSourceGuardPortConfigMode based on Integer32"""
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


_Gs2310IPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardPortConfigMode_Object = MibTableColumn
gs2310IPSourceGuardPortConfigMode = _Gs2310IPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1, 2, 1, 2),
    _Gs2310IPSourceGuardPortConfigMode_Type()
)
gs2310IPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardPortConfigMode.setStatus("current")


class _Gs2310IPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type gs2310IPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Gs2310IPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
gs2310IPSourceGuardPortMaxDynamicClients = _Gs2310IPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 1, 2, 1, 3),
    _Gs2310IPSourceGuardPortMaxDynamicClients_Type()
)
gs2310IPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardPortMaxDynamicClients.setStatus("current")
_Gs2310IPSourceGuardStatic_ObjectIdentity = ObjectIdentity
gs2310IPSourceGuardStatic = _Gs2310IPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2)
)


class _Gs2310IPSourceGuardStaticCreate_Type(Integer32):
    """Custom type gs2310IPSourceGuardStaticCreate based on Integer32"""
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


_Gs2310IPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardStaticCreate_Object = MibScalar
gs2310IPSourceGuardStaticCreate = _Gs2310IPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 1),
    _Gs2310IPSourceGuardStaticCreate_Type()
)
gs2310IPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticCreate.setStatus("current")
_Gs2310IPSourceGuardStaticTable_Object = MibTable
gs2310IPSourceGuardStaticTable = _Gs2310IPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticTable.setStatus("current")
_Gs2310IPSourceGuardStaticEntry_Object = MibTableRow
gs2310IPSourceGuardStaticEntry = _Gs2310IPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1)
)
gs2310IPSourceGuardStaticEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticEntry.setStatus("current")


class _Gs2310IPSourceGuardStaticIndex_Type(Integer32):
    """Custom type gs2310IPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Gs2310IPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardStaticIndex_Object = MibTableColumn
gs2310IPSourceGuardStaticIndex = _Gs2310IPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1, 1),
    _Gs2310IPSourceGuardStaticIndex_Type()
)
gs2310IPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticIndex.setStatus("current")


class _Gs2310IPSourceGuardStaticPort_Type(Integer32):
    """Custom type gs2310IPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardStaticPort_Object = MibTableColumn
gs2310IPSourceGuardStaticPort = _Gs2310IPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1, 2),
    _Gs2310IPSourceGuardStaticPort_Type()
)
gs2310IPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticPort.setStatus("current")


class _Gs2310IPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type gs2310IPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310IPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardStaticVLANId_Object = MibTableColumn
gs2310IPSourceGuardStaticVLANId = _Gs2310IPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1, 3),
    _Gs2310IPSourceGuardStaticVLANId_Type()
)
gs2310IPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticVLANId.setStatus("current")
_Gs2310IPSourceGuardStaticIPAddress_Type = IpAddress
_Gs2310IPSourceGuardStaticIPAddress_Object = MibTableColumn
gs2310IPSourceGuardStaticIPAddress = _Gs2310IPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1, 4),
    _Gs2310IPSourceGuardStaticIPAddress_Type()
)
gs2310IPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticIPAddress.setStatus("current")
_Gs2310IPSourceGuardStaticMACAddress_Type = MacAddress
_Gs2310IPSourceGuardStaticMACAddress_Object = MibTableColumn
gs2310IPSourceGuardStaticMACAddress = _Gs2310IPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1, 5),
    _Gs2310IPSourceGuardStaticMACAddress_Type()
)
gs2310IPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticMACAddress.setStatus("current")


class _Gs2310IPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type gs2310IPSourceGuardStaticRowStatus based on Integer32"""
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


_Gs2310IPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardStaticRowStatus_Object = MibTableColumn
gs2310IPSourceGuardStaticRowStatus = _Gs2310IPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 2, 2, 1, 6),
    _Gs2310IPSourceGuardStaticRowStatus_Type()
)
gs2310IPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardStaticRowStatus.setStatus("current")
_Gs2310IPSourceGuardDynamicTable_Object = MibTable
gs2310IPSourceGuardDynamicTable = _Gs2310IPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3)
)
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicTable.setStatus("current")
_Gs2310IPSourceGuardDynamicEntry_Object = MibTableRow
gs2310IPSourceGuardDynamicEntry = _Gs2310IPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3, 1)
)
gs2310IPSourceGuardDynamicEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310IPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicEntry.setStatus("current")


class _Gs2310IPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type gs2310IPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310IPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardDynamicIndex_Object = MibTableColumn
gs2310IPSourceGuardDynamicIndex = _Gs2310IPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3, 1, 1),
    _Gs2310IPSourceGuardDynamicIndex_Type()
)
gs2310IPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicIndex.setStatus("current")


class _Gs2310IPSourceGuardDynamicPort_Type(Integer32):
    """Custom type gs2310IPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2310IPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardDynamicPort_Object = MibTableColumn
gs2310IPSourceGuardDynamicPort = _Gs2310IPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3, 1, 2),
    _Gs2310IPSourceGuardDynamicPort_Type()
)
gs2310IPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicPort.setStatus("current")


class _Gs2310IPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type gs2310IPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310IPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Gs2310IPSourceGuardDynamicVLANId_Object = MibTableColumn
gs2310IPSourceGuardDynamicVLANId = _Gs2310IPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3, 1, 3),
    _Gs2310IPSourceGuardDynamicVLANId_Type()
)
gs2310IPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicVLANId.setStatus("current")
_Gs2310IPSourceGuardDynamicIPAddress_Type = IpAddress
_Gs2310IPSourceGuardDynamicIPAddress_Object = MibTableColumn
gs2310IPSourceGuardDynamicIPAddress = _Gs2310IPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3, 1, 4),
    _Gs2310IPSourceGuardDynamicIPAddress_Type()
)
gs2310IPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicIPAddress.setStatus("current")
_Gs2310IPSourceGuardDynamicMACAddress_Type = MacAddress
_Gs2310IPSourceGuardDynamicMACAddress_Object = MibTableColumn
gs2310IPSourceGuardDynamicMACAddress = _Gs2310IPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 1, 3, 1, 5),
    _Gs2310IPSourceGuardDynamicMACAddress_Type()
)
gs2310IPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310IPSourceGuardDynamicMACAddress.setStatus("current")
_Gs2310ARPInspection_ObjectIdentity = ObjectIdentity
gs2310ARPInspection = _Gs2310ARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2)
)
_Gs2310ARPInspectionConf_ObjectIdentity = ObjectIdentity
gs2310ARPInspectionConf = _Gs2310ARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 1)
)


class _Gs2310ARPInspectionConfMode_Type(Integer32):
    """Custom type gs2310ARPInspectionConfMode based on Integer32"""
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


_Gs2310ARPInspectionConfMode_Type.__name__ = "Integer32"
_Gs2310ARPInspectionConfMode_Object = MibScalar
gs2310ARPInspectionConfMode = _Gs2310ARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 1, 1),
    _Gs2310ARPInspectionConfMode_Type()
)
gs2310ARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionConfMode.setStatus("current")
_Gs2310ARPInspectionConfTable_Object = MibTable
gs2310ARPInspectionConfTable = _Gs2310ARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310ARPInspectionConfTable.setStatus("current")
_Gs2310ARPInspectionConfEntry_Object = MibTableRow
gs2310ARPInspectionConfEntry = _Gs2310ARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 1, 2, 1)
)
gs2310ARPInspectionConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    gs2310ARPInspectionConfEntry.setStatus("current")


class _Gs2310ARPInspectionConfPortIndex_Type(Integer32):
    """Custom type gs2310ARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Gs2310ARPInspectionConfPortIndex_Object = MibTableColumn
gs2310ARPInspectionConfPortIndex = _Gs2310ARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 1, 2, 1, 1),
    _Gs2310ARPInspectionConfPortIndex_Type()
)
gs2310ARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ARPInspectionConfPortIndex.setStatus("current")


class _Gs2310ARPInspectionConfPortMode_Type(Integer32):
    """Custom type gs2310ARPInspectionConfPortMode based on Integer32"""
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


_Gs2310ARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Gs2310ARPInspectionConfPortMode_Object = MibTableColumn
gs2310ARPInspectionConfPortMode = _Gs2310ARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 1, 2, 1, 2),
    _Gs2310ARPInspectionConfPortMode_Type()
)
gs2310ARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionConfPortMode.setStatus("current")
_Gs2310ARPInspectionStatic_ObjectIdentity = ObjectIdentity
gs2310ARPInspectionStatic = _Gs2310ARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2)
)


class _Gs2310ARPInspectionStaticCreate_Type(Integer32):
    """Custom type gs2310ARPInspectionStaticCreate based on Integer32"""
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


_Gs2310ARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Gs2310ARPInspectionStaticCreate_Object = MibScalar
gs2310ARPInspectionStaticCreate = _Gs2310ARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 1),
    _Gs2310ARPInspectionStaticCreate_Type()
)
gs2310ARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticCreate.setStatus("current")
_Gs2310ARPInspectionStaticTable_Object = MibTable
gs2310ARPInspectionStaticTable = _Gs2310ARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticTable.setStatus("current")
_Gs2310ARPInspectionStaticEntry_Object = MibTableRow
gs2310ARPInspectionStaticEntry = _Gs2310ARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1)
)
gs2310ARPInspectionStaticEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticEntry.setStatus("current")


class _Gs2310ARPInspectionStaticIndex_Type(Integer32):
    """Custom type gs2310ARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Gs2310ARPInspectionStaticIndex_Object = MibTableColumn
gs2310ARPInspectionStaticIndex = _Gs2310ARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1, 1),
    _Gs2310ARPInspectionStaticIndex_Type()
)
gs2310ARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticIndex.setStatus("current")


class _Gs2310ARPInspectionStaticPort_Type(Integer32):
    """Custom type gs2310ARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPInspectionStaticPort_Type.__name__ = "Integer32"
_Gs2310ARPInspectionStaticPort_Object = MibTableColumn
gs2310ARPInspectionStaticPort = _Gs2310ARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1, 2),
    _Gs2310ARPInspectionStaticPort_Type()
)
gs2310ARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticPort.setStatus("current")


class _Gs2310ARPInspectionStaticVLANId_Type(Integer32):
    """Custom type gs2310ARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310ARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Gs2310ARPInspectionStaticVLANId_Object = MibTableColumn
gs2310ARPInspectionStaticVLANId = _Gs2310ARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1, 3),
    _Gs2310ARPInspectionStaticVLANId_Type()
)
gs2310ARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticVLANId.setStatus("current")
_Gs2310ARPInspectionStaticIPAddress_Type = IpAddress
_Gs2310ARPInspectionStaticIPAddress_Object = MibTableColumn
gs2310ARPInspectionStaticIPAddress = _Gs2310ARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1, 4),
    _Gs2310ARPInspectionStaticIPAddress_Type()
)
gs2310ARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticIPAddress.setStatus("current")
_Gs2310ARPInspectionStaticMACAddress_Type = MacAddress
_Gs2310ARPInspectionStaticMACAddress_Object = MibTableColumn
gs2310ARPInspectionStaticMACAddress = _Gs2310ARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1, 5),
    _Gs2310ARPInspectionStaticMACAddress_Type()
)
gs2310ARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticMACAddress.setStatus("current")


class _Gs2310ARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type gs2310ARPInspectionStaticRowStatus based on Integer32"""
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


_Gs2310ARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Gs2310ARPInspectionStaticRowStatus_Object = MibTableColumn
gs2310ARPInspectionStaticRowStatus = _Gs2310ARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 2, 2, 1, 6),
    _Gs2310ARPInspectionStaticRowStatus_Type()
)
gs2310ARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPInspectionStaticRowStatus.setStatus("current")
_Gs2310ARPInspectionDynamicTable_Object = MibTable
gs2310ARPInspectionDynamicTable = _Gs2310ARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicTable.setStatus("current")
_Gs2310ARPInspectionDynamicEntry_Object = MibTableRow
gs2310ARPInspectionDynamicEntry = _Gs2310ARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3, 1)
)
gs2310ARPInspectionDynamicEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicEntry.setStatus("current")


class _Gs2310ARPInspectionDynamicIndex_Type(Integer32):
    """Custom type gs2310ARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Gs2310ARPInspectionDynamicIndex_Object = MibTableColumn
gs2310ARPInspectionDynamicIndex = _Gs2310ARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3, 1, 1),
    _Gs2310ARPInspectionDynamicIndex_Type()
)
gs2310ARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicIndex.setStatus("current")


class _Gs2310ARPInspectionDynamicPort_Type(Integer32):
    """Custom type gs2310ARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Gs2310ARPInspectionDynamicPort_Object = MibTableColumn
gs2310ARPInspectionDynamicPort = _Gs2310ARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3, 1, 2),
    _Gs2310ARPInspectionDynamicPort_Type()
)
gs2310ARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicPort.setStatus("current")


class _Gs2310ARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type gs2310ARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310ARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Gs2310ARPInspectionDynamicVLANId_Object = MibTableColumn
gs2310ARPInspectionDynamicVLANId = _Gs2310ARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3, 1, 3),
    _Gs2310ARPInspectionDynamicVLANId_Type()
)
gs2310ARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicVLANId.setStatus("current")
_Gs2310ARPInspectionDynamicIPAddress_Type = IpAddress
_Gs2310ARPInspectionDynamicIPAddress_Object = MibTableColumn
gs2310ARPInspectionDynamicIPAddress = _Gs2310ARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3, 1, 4),
    _Gs2310ARPInspectionDynamicIPAddress_Type()
)
gs2310ARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicIPAddress.setStatus("current")
_Gs2310ARPInspectionDynamicMACAddress_Type = MacAddress
_Gs2310ARPInspectionDynamicMACAddress_Object = MibTableColumn
gs2310ARPInspectionDynamicMACAddress = _Gs2310ARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 3, 1, 5),
    _Gs2310ARPInspectionDynamicMACAddress_Type()
)
gs2310ARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ARPInspectionDynamicMACAddress.setStatus("current")
_Gs2310ARPStaticGatewayCtrl_ObjectIdentity = ObjectIdentity
gs2310ARPStaticGatewayCtrl = _Gs2310ARPStaticGatewayCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6)
)
_Gs2310ARPStaticGatewayCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2310ARPStaticGatewayCtrlSystemConf = _Gs2310ARPStaticGatewayCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 1)
)


class _Gs2310ARPStaticGatewayCtrlMode_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlMode based on Integer32"""
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


_Gs2310ARPStaticGatewayCtrlMode_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlMode_Object = MibScalar
gs2310ARPStaticGatewayCtrlMode = _Gs2310ARPStaticGatewayCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 1, 1),
    _Gs2310ARPStaticGatewayCtrlMode_Type()
)
gs2310ARPStaticGatewayCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlMode.setStatus("current")


class _Gs2310ARPStaticGatewayCtrlCreate_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlCreate based on Integer32"""
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


_Gs2310ARPStaticGatewayCtrlCreate_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlCreate_Object = MibScalar
gs2310ARPStaticGatewayCtrlCreate = _Gs2310ARPStaticGatewayCtrlCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 2),
    _Gs2310ARPStaticGatewayCtrlCreate_Type()
)
gs2310ARPStaticGatewayCtrlCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlCreate.setStatus("current")
_Gs2310ARPStaticGatewayCtrlTable_Object = MibTable
gs2310ARPStaticGatewayCtrlTable = _Gs2310ARPStaticGatewayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlTable.setStatus("current")
_Gs2310ARPStaticGatewayCtrlEntry_Object = MibTableRow
gs2310ARPStaticGatewayCtrlEntry = _Gs2310ARPStaticGatewayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1)
)
gs2310ARPStaticGatewayCtrlEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ARPStaticGatewayCtrlIndex"),
)
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlEntry.setStatus("current")


class _Gs2310ARPStaticGatewayCtrlIndex_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2310ARPStaticGatewayCtrlIndex_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlIndex_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlIndex = _Gs2310ARPStaticGatewayCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 1),
    _Gs2310ARPStaticGatewayCtrlIndex_Type()
)
gs2310ARPStaticGatewayCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlIndex.setStatus("current")
_Gs2310ARPStaticGatewayCtrlIPAddress_Type = IpAddress
_Gs2310ARPStaticGatewayCtrlIPAddress_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlIPAddress = _Gs2310ARPStaticGatewayCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 2),
    _Gs2310ARPStaticGatewayCtrlIPAddress_Type()
)
gs2310ARPStaticGatewayCtrlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlIPAddress.setStatus("current")
_Gs2310ARPStaticGatewayCtrlMACAddress_Type = MacAddress
_Gs2310ARPStaticGatewayCtrlMACAddress_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlMACAddress = _Gs2310ARPStaticGatewayCtrlMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 3),
    _Gs2310ARPStaticGatewayCtrlMACAddress_Type()
)
gs2310ARPStaticGatewayCtrlMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlMACAddress.setStatus("current")


class _Gs2310ARPStaticGatewayCtrlPort_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPStaticGatewayCtrlPort_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlPort_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlPort = _Gs2310ARPStaticGatewayCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 4),
    _Gs2310ARPStaticGatewayCtrlPort_Type()
)
gs2310ARPStaticGatewayCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlPort.setStatus("current")


class _Gs2310ARPStaticGatewayCtrlAction_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlAction based on Integer32"""
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


_Gs2310ARPStaticGatewayCtrlAction_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlAction_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlAction = _Gs2310ARPStaticGatewayCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 5),
    _Gs2310ARPStaticGatewayCtrlAction_Type()
)
gs2310ARPStaticGatewayCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlAction.setStatus("current")
_Gs2310ARPStaticGatewayCtrlState_Type = DisplayString
_Gs2310ARPStaticGatewayCtrlState_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlState = _Gs2310ARPStaticGatewayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 6),
    _Gs2310ARPStaticGatewayCtrlState_Type()
)
gs2310ARPStaticGatewayCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlState.setStatus("current")


class _Gs2310ARPStaticGatewayCtrlReOpen_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlReOpen based on Integer32"""
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


_Gs2310ARPStaticGatewayCtrlReOpen_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlReOpen_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlReOpen = _Gs2310ARPStaticGatewayCtrlReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 7),
    _Gs2310ARPStaticGatewayCtrlReOpen_Type()
)
gs2310ARPStaticGatewayCtrlReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlReOpen.setStatus("current")


class _Gs2310ARPStaticGatewayCtrlRowStatus_Type(Integer32):
    """Custom type gs2310ARPStaticGatewayCtrlRowStatus based on Integer32"""
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


_Gs2310ARPStaticGatewayCtrlRowStatus_Type.__name__ = "Integer32"
_Gs2310ARPStaticGatewayCtrlRowStatus_Object = MibTableColumn
gs2310ARPStaticGatewayCtrlRowStatus = _Gs2310ARPStaticGatewayCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 6, 3, 1, 8),
    _Gs2310ARPStaticGatewayCtrlRowStatus_Type()
)
gs2310ARPStaticGatewayCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPStaticGatewayCtrlRowStatus.setStatus("current")
_Gs2310ARPSpoofingPrevention_ObjectIdentity = ObjectIdentity
gs2310ARPSpoofingPrevention = _Gs2310ARPSpoofingPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7)
)
_Gs2310ARPSpoofingPreventionSystemConf_ObjectIdentity = ObjectIdentity
gs2310ARPSpoofingPreventionSystemConf = _Gs2310ARPSpoofingPreventionSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 1)
)


class _Gs2310ARPSpoofingPreventionMode_Type(Integer32):
    """Custom type gs2310ARPSpoofingPreventionMode based on Integer32"""
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


_Gs2310ARPSpoofingPreventionMode_Type.__name__ = "Integer32"
_Gs2310ARPSpoofingPreventionMode_Object = MibScalar
gs2310ARPSpoofingPreventionMode = _Gs2310ARPSpoofingPreventionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 1, 1),
    _Gs2310ARPSpoofingPreventionMode_Type()
)
gs2310ARPSpoofingPreventionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionMode.setStatus("current")
_Gs2310ARPSpoofingPreventionTable_Object = MibTable
gs2310ARPSpoofingPreventionTable = _Gs2310ARPSpoofingPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionTable.setStatus("current")
_Gs2310ARPSpoofingPreventionEntry_Object = MibTableRow
gs2310ARPSpoofingPreventionEntry = _Gs2310ARPSpoofingPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1)
)
gs2310ARPSpoofingPreventionEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310ARPSpoofingPreventionPort"),
)
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionEntry.setStatus("current")


class _Gs2310ARPSpoofingPreventionPort_Type(Integer32):
    """Custom type gs2310ARPSpoofingPreventionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310ARPSpoofingPreventionPort_Type.__name__ = "Integer32"
_Gs2310ARPSpoofingPreventionPort_Object = MibTableColumn
gs2310ARPSpoofingPreventionPort = _Gs2310ARPSpoofingPreventionPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1, 1),
    _Gs2310ARPSpoofingPreventionPort_Type()
)
gs2310ARPSpoofingPreventionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionPort.setStatus("current")


class _Gs2310ARPSpoofingPreventionPortMode_Type(Integer32):
    """Custom type gs2310ARPSpoofingPreventionPortMode based on Integer32"""
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


_Gs2310ARPSpoofingPreventionPortMode_Type.__name__ = "Integer32"
_Gs2310ARPSpoofingPreventionPortMode_Object = MibTableColumn
gs2310ARPSpoofingPreventionPortMode = _Gs2310ARPSpoofingPreventionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1, 2),
    _Gs2310ARPSpoofingPreventionPortMode_Type()
)
gs2310ARPSpoofingPreventionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionPortMode.setStatus("current")


class _Gs2310ARPSpoofingPreventionPortLimit_Type(Integer32):
    """Custom type gs2310ARPSpoofingPreventionPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Gs2310ARPSpoofingPreventionPortLimit_Type.__name__ = "Integer32"
_Gs2310ARPSpoofingPreventionPortLimit_Object = MibTableColumn
gs2310ARPSpoofingPreventionPortLimit = _Gs2310ARPSpoofingPreventionPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1, 3),
    _Gs2310ARPSpoofingPreventionPortLimit_Type()
)
gs2310ARPSpoofingPreventionPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionPortLimit.setStatus("current")


class _Gs2310ARPSpoofingPreventionPortAction_Type(Integer32):
    """Custom type gs2310ARPSpoofingPreventionPortAction based on Integer32"""
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


_Gs2310ARPSpoofingPreventionPortAction_Type.__name__ = "Integer32"
_Gs2310ARPSpoofingPreventionPortAction_Object = MibTableColumn
gs2310ARPSpoofingPreventionPortAction = _Gs2310ARPSpoofingPreventionPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1, 4),
    _Gs2310ARPSpoofingPreventionPortAction_Type()
)
gs2310ARPSpoofingPreventionPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionPortAction.setStatus("current")
_Gs2310ARPSpoofingPreventionPortState_Type = DisplayString
_Gs2310ARPSpoofingPreventionPortState_Object = MibTableColumn
gs2310ARPSpoofingPreventionPortState = _Gs2310ARPSpoofingPreventionPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1, 5),
    _Gs2310ARPSpoofingPreventionPortState_Type()
)
gs2310ARPSpoofingPreventionPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionPortState.setStatus("current")


class _Gs2310ARPSpoofingPreventionPortReOpen_Type(Integer32):
    """Custom type gs2310ARPSpoofingPreventionPortReOpen based on Integer32"""
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


_Gs2310ARPSpoofingPreventionPortReOpen_Type.__name__ = "Integer32"
_Gs2310ARPSpoofingPreventionPortReOpen_Object = MibTableColumn
gs2310ARPSpoofingPreventionPortReOpen = _Gs2310ARPSpoofingPreventionPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 7, 2, 1, 6),
    _Gs2310ARPSpoofingPreventionPortReOpen_Type()
)
gs2310ARPSpoofingPreventionPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPSpoofingPreventionPortReOpen.setStatus("current")
_Gs2310ARPIPDoSPrevention_ObjectIdentity = ObjectIdentity
gs2310ARPIPDoSPrevention = _Gs2310ARPIPDoSPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8)
)


class _Gs2310ARPIPDoSPreventionTCPMode_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionTCPMode based on Integer32"""
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


_Gs2310ARPIPDoSPreventionTCPMode_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionTCPMode_Object = MibScalar
gs2310ARPIPDoSPreventionTCPMode = _Gs2310ARPIPDoSPreventionTCPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 1),
    _Gs2310ARPIPDoSPreventionTCPMode_Type()
)
gs2310ARPIPDoSPreventionTCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionTCPMode.setStatus("current")


class _Gs2310ARPIPDoSPreventionUDPMode_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionUDPMode based on Integer32"""
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


_Gs2310ARPIPDoSPreventionUDPMode_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionUDPMode_Object = MibScalar
gs2310ARPIPDoSPreventionUDPMode = _Gs2310ARPIPDoSPreventionUDPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 2),
    _Gs2310ARPIPDoSPreventionUDPMode_Type()
)
gs2310ARPIPDoSPreventionUDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionUDPMode.setStatus("current")


class _Gs2310ARPIPDoSPreventionICMPMode_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionICMPMode based on Integer32"""
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


_Gs2310ARPIPDoSPreventionICMPMode_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionICMPMode_Object = MibScalar
gs2310ARPIPDoSPreventionICMPMode = _Gs2310ARPIPDoSPreventionICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 3),
    _Gs2310ARPIPDoSPreventionICMPMode_Type()
)
gs2310ARPIPDoSPreventionICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionICMPMode.setStatus("current")


class _Gs2310ARPIPDoSPreventionServerPort1_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionServerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2310ARPIPDoSPreventionServerPort1_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionServerPort1_Object = MibScalar
gs2310ARPIPDoSPreventionServerPort1 = _Gs2310ARPIPDoSPreventionServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 4),
    _Gs2310ARPIPDoSPreventionServerPort1_Type()
)
gs2310ARPIPDoSPreventionServerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionServerPort1.setStatus("current")


class _Gs2310ARPIPDoSPreventionServerPort2_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionServerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2310ARPIPDoSPreventionServerPort2_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionServerPort2_Object = MibScalar
gs2310ARPIPDoSPreventionServerPort2 = _Gs2310ARPIPDoSPreventionServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 5),
    _Gs2310ARPIPDoSPreventionServerPort2_Type()
)
gs2310ARPIPDoSPreventionServerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionServerPort2.setStatus("current")


class _Gs2310ARPIPDoSPreventionServerPort3_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionServerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2310ARPIPDoSPreventionServerPort3_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionServerPort3_Object = MibScalar
gs2310ARPIPDoSPreventionServerPort3 = _Gs2310ARPIPDoSPreventionServerPort3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 6),
    _Gs2310ARPIPDoSPreventionServerPort3_Type()
)
gs2310ARPIPDoSPreventionServerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionServerPort3.setStatus("current")


class _Gs2310ARPIPDoSPreventionServerPort4_Type(Integer32):
    """Custom type gs2310ARPIPDoSPreventionServerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2310ARPIPDoSPreventionServerPort4_Type.__name__ = "Integer32"
_Gs2310ARPIPDoSPreventionServerPort4_Object = MibScalar
gs2310ARPIPDoSPreventionServerPort4 = _Gs2310ARPIPDoSPreventionServerPort4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 2, 8, 7),
    _Gs2310ARPIPDoSPreventionServerPort4_Type()
)
gs2310ARPIPDoSPreventionServerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ARPIPDoSPreventionServerPort4.setStatus("current")
_Gs2310DHCPSnooping_ObjectIdentity = ObjectIdentity
gs2310DHCPSnooping = _Gs2310DHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3)
)
_Gs2310DHCPSnoopingConf_ObjectIdentity = ObjectIdentity
gs2310DHCPSnoopingConf = _Gs2310DHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 1)
)


class _Gs2310DHCPSnoopingMode_Type(Integer32):
    """Custom type gs2310DHCPSnoopingMode based on Integer32"""
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


_Gs2310DHCPSnoopingMode_Type.__name__ = "Integer32"
_Gs2310DHCPSnoopingMode_Object = MibScalar
gs2310DHCPSnoopingMode = _Gs2310DHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 1, 1),
    _Gs2310DHCPSnoopingMode_Type()
)
gs2310DHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingMode.setStatus("current")
_Gs2310DHCPSnoopingPortModeConfigurationTable_Object = MibTable
gs2310DHCPSnoopingPortModeConfigurationTable = _Gs2310DHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Gs2310DHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
gs2310DHCPSnoopingPortModeConfigurationEntry = _Gs2310DHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 1, 2, 1)
)
gs2310DHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310DHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Gs2310DHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type gs2310DHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310DHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Gs2310DHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
gs2310DHCPSnoopingPortModeConfigurationPort = _Gs2310DHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 1, 2, 1, 1),
    _Gs2310DHCPSnoopingPortModeConfigurationPort_Type()
)
gs2310DHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Gs2310DHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type gs2310DHCPSnoopingPortModeConfigurationMode based on Integer32"""
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


_Gs2310DHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Gs2310DHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
gs2310DHCPSnoopingPortModeConfigurationMode = _Gs2310DHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 1, 2, 1, 2),
    _Gs2310DHCPSnoopingPortModeConfigurationMode_Type()
)
gs2310DHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Gs2310DHCPSnoopingStatisticsTable_Object = MibTable
gs2310DHCPSnoopingStatisticsTable = _Gs2310DHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingStatisticsTable.setStatus("current")
_Gs2310DHCPSnoopingStatisticsEntry_Object = MibTableRow
gs2310DHCPSnoopingStatisticsEntry = _Gs2310DHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1)
)
gs2310DHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310DHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingStatisticsEntry.setStatus("current")


class _Gs2310DHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type gs2310DHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310DHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Gs2310DHCPSnoopingStatisticsPort_Object = MibTableColumn
gs2310DHCPSnoopingStatisticsPort = _Gs2310DHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 1),
    _Gs2310DHCPSnoopingStatisticsPort_Type()
)
gs2310DHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingStatisticsPort.setStatus("current")


class _Gs2310DHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type gs2310DHCPSnoopingStatisticsClear based on Integer32"""
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


_Gs2310DHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Gs2310DHCPSnoopingStatisticsClear_Object = MibTableColumn
gs2310DHCPSnoopingStatisticsClear = _Gs2310DHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 2),
    _Gs2310DHCPSnoopingStatisticsClear_Type()
)
gs2310DHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingStatisticsClear.setStatus("current")
_Gs2310DHCPSnoopingRxDiscover_Type = Counter32
_Gs2310DHCPSnoopingRxDiscover_Object = MibTableColumn
gs2310DHCPSnoopingRxDiscover = _Gs2310DHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 3),
    _Gs2310DHCPSnoopingRxDiscover_Type()
)
gs2310DHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxDiscover.setStatus("current")
_Gs2310DHCPSnoopingRxOffer_Type = Counter32
_Gs2310DHCPSnoopingRxOffer_Object = MibTableColumn
gs2310DHCPSnoopingRxOffer = _Gs2310DHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 4),
    _Gs2310DHCPSnoopingRxOffer_Type()
)
gs2310DHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxOffer.setStatus("current")
_Gs2310DHCPSnoopingRxRequest_Type = Counter32
_Gs2310DHCPSnoopingRxRequest_Object = MibTableColumn
gs2310DHCPSnoopingRxRequest = _Gs2310DHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 5),
    _Gs2310DHCPSnoopingRxRequest_Type()
)
gs2310DHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxRequest.setStatus("current")
_Gs2310DHCPSnoopingRxDecline_Type = Counter32
_Gs2310DHCPSnoopingRxDecline_Object = MibTableColumn
gs2310DHCPSnoopingRxDecline = _Gs2310DHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 6),
    _Gs2310DHCPSnoopingRxDecline_Type()
)
gs2310DHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxDecline.setStatus("current")
_Gs2310DHCPSnoopingRxACK_Type = Counter32
_Gs2310DHCPSnoopingRxACK_Object = MibTableColumn
gs2310DHCPSnoopingRxACK = _Gs2310DHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 7),
    _Gs2310DHCPSnoopingRxACK_Type()
)
gs2310DHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxACK.setStatus("current")
_Gs2310DHCPSnoopingRxNAK_Type = Counter32
_Gs2310DHCPSnoopingRxNAK_Object = MibTableColumn
gs2310DHCPSnoopingRxNAK = _Gs2310DHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 8),
    _Gs2310DHCPSnoopingRxNAK_Type()
)
gs2310DHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxNAK.setStatus("current")
_Gs2310DHCPSnoopingRxRelease_Type = Counter32
_Gs2310DHCPSnoopingRxRelease_Object = MibTableColumn
gs2310DHCPSnoopingRxRelease = _Gs2310DHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 9),
    _Gs2310DHCPSnoopingRxRelease_Type()
)
gs2310DHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxRelease.setStatus("current")
_Gs2310DHCPSnoopingRxInform_Type = Counter32
_Gs2310DHCPSnoopingRxInform_Object = MibTableColumn
gs2310DHCPSnoopingRxInform = _Gs2310DHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 10),
    _Gs2310DHCPSnoopingRxInform_Type()
)
gs2310DHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxInform.setStatus("current")
_Gs2310DHCPSnoopingRxLeaseQuery_Type = Counter32
_Gs2310DHCPSnoopingRxLeaseQuery_Object = MibTableColumn
gs2310DHCPSnoopingRxLeaseQuery = _Gs2310DHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 11),
    _Gs2310DHCPSnoopingRxLeaseQuery_Type()
)
gs2310DHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxLeaseQuery.setStatus("current")
_Gs2310DHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Gs2310DHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
gs2310DHCPSnoopingRxLeaseUnassigned = _Gs2310DHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 12),
    _Gs2310DHCPSnoopingRxLeaseUnassigned_Type()
)
gs2310DHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Gs2310DHCPSnoopingRxLeaseUnknown_Type = Counter32
_Gs2310DHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
gs2310DHCPSnoopingRxLeaseUnknown = _Gs2310DHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 13),
    _Gs2310DHCPSnoopingRxLeaseUnknown_Type()
)
gs2310DHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxLeaseUnknown.setStatus("current")
_Gs2310DHCPSnoopingRxLeaseActive_Type = Counter32
_Gs2310DHCPSnoopingRxLeaseActive_Object = MibTableColumn
gs2310DHCPSnoopingRxLeaseActive = _Gs2310DHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 14),
    _Gs2310DHCPSnoopingRxLeaseActive_Type()
)
gs2310DHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingRxLeaseActive.setStatus("current")
_Gs2310DHCPSnoopingTxDiscover_Type = Counter32
_Gs2310DHCPSnoopingTxDiscover_Object = MibTableColumn
gs2310DHCPSnoopingTxDiscover = _Gs2310DHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 15),
    _Gs2310DHCPSnoopingTxDiscover_Type()
)
gs2310DHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxDiscover.setStatus("current")
_Gs2310DHCPSnoopingTxOffer_Type = Counter32
_Gs2310DHCPSnoopingTxOffer_Object = MibTableColumn
gs2310DHCPSnoopingTxOffer = _Gs2310DHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 16),
    _Gs2310DHCPSnoopingTxOffer_Type()
)
gs2310DHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxOffer.setStatus("current")
_Gs2310DHCPSnoopingTxRequest_Type = Counter32
_Gs2310DHCPSnoopingTxRequest_Object = MibTableColumn
gs2310DHCPSnoopingTxRequest = _Gs2310DHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 17),
    _Gs2310DHCPSnoopingTxRequest_Type()
)
gs2310DHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxRequest.setStatus("current")
_Gs2310DHCPSnoopingTxDecline_Type = Counter32
_Gs2310DHCPSnoopingTxDecline_Object = MibTableColumn
gs2310DHCPSnoopingTxDecline = _Gs2310DHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 18),
    _Gs2310DHCPSnoopingTxDecline_Type()
)
gs2310DHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxDecline.setStatus("current")
_Gs2310DHCPSnoopingTxACK_Type = Counter32
_Gs2310DHCPSnoopingTxACK_Object = MibTableColumn
gs2310DHCPSnoopingTxACK = _Gs2310DHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 19),
    _Gs2310DHCPSnoopingTxACK_Type()
)
gs2310DHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxACK.setStatus("current")
_Gs2310DHCPSnoopingTxNAK_Type = Counter32
_Gs2310DHCPSnoopingTxNAK_Object = MibTableColumn
gs2310DHCPSnoopingTxNAK = _Gs2310DHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 20),
    _Gs2310DHCPSnoopingTxNAK_Type()
)
gs2310DHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxNAK.setStatus("current")
_Gs2310DHCPSnoopingTxRelease_Type = Counter32
_Gs2310DHCPSnoopingTxRelease_Object = MibTableColumn
gs2310DHCPSnoopingTxRelease = _Gs2310DHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 21),
    _Gs2310DHCPSnoopingTxRelease_Type()
)
gs2310DHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxRelease.setStatus("current")
_Gs2310DHCPSnoopingTxInform_Type = Counter32
_Gs2310DHCPSnoopingTxInform_Object = MibTableColumn
gs2310DHCPSnoopingTxInform = _Gs2310DHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 22),
    _Gs2310DHCPSnoopingTxInform_Type()
)
gs2310DHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxInform.setStatus("current")
_Gs2310DHCPSnoopingTxLeaseQuery_Type = Counter32
_Gs2310DHCPSnoopingTxLeaseQuery_Object = MibTableColumn
gs2310DHCPSnoopingTxLeaseQuery = _Gs2310DHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 23),
    _Gs2310DHCPSnoopingTxLeaseQuery_Type()
)
gs2310DHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxLeaseQuery.setStatus("current")
_Gs2310DHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Gs2310DHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
gs2310DHCPSnoopingTxLeaseUnassigned = _Gs2310DHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 24),
    _Gs2310DHCPSnoopingTxLeaseUnassigned_Type()
)
gs2310DHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Gs2310DHCPSnoopingTxLeaseUnknown_Type = Counter32
_Gs2310DHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
gs2310DHCPSnoopingTxLeaseUnknown = _Gs2310DHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 25),
    _Gs2310DHCPSnoopingTxLeaseUnknown_Type()
)
gs2310DHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxLeaseUnknown.setStatus("current")
_Gs2310DHCPSnoopingTxLeaseActive_Type = Counter32
_Gs2310DHCPSnoopingTxLeaseActive_Object = MibTableColumn
gs2310DHCPSnoopingTxLeaseActive = _Gs2310DHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 3, 2, 1, 26),
    _Gs2310DHCPSnoopingTxLeaseActive_Type()
)
gs2310DHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310DHCPSnoopingTxLeaseActive.setStatus("current")
_Gs2310DHCPRelay_ObjectIdentity = ObjectIdentity
gs2310DHCPRelay = _Gs2310DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4)
)
_Gs2310DHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
gs2310DHCPRelayConfiguration = _Gs2310DHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1)
)


class _Gs2310DHCPRelayMode_Type(Integer32):
    """Custom type gs2310DHCPRelayMode based on Integer32"""
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


_Gs2310DHCPRelayMode_Type.__name__ = "Integer32"
_Gs2310DHCPRelayMode_Object = MibScalar
gs2310DHCPRelayMode = _Gs2310DHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 1),
    _Gs2310DHCPRelayMode_Type()
)
gs2310DHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayMode.setStatus("current")
_Gs2310DHCPRelayServer_Type = IpAddress
_Gs2310DHCPRelayServer_Object = MibScalar
gs2310DHCPRelayServer = _Gs2310DHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 2),
    _Gs2310DHCPRelayServer_Type()
)
gs2310DHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayServer.setStatus("current")


class _Gs2310DHCPRelayInformationMode_Type(Integer32):
    """Custom type gs2310DHCPRelayInformationMode based on Integer32"""
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


_Gs2310DHCPRelayInformationMode_Type.__name__ = "Integer32"
_Gs2310DHCPRelayInformationMode_Object = MibScalar
gs2310DHCPRelayInformationMode = _Gs2310DHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 3),
    _Gs2310DHCPRelayInformationMode_Type()
)
gs2310DHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayInformationMode.setStatus("current")


class _Gs2310DHCPRelayInformationPolicy_Type(Integer32):
    """Custom type gs2310DHCPRelayInformationPolicy based on Integer32"""
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


_Gs2310DHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Gs2310DHCPRelayInformationPolicy_Object = MibScalar
gs2310DHCPRelayInformationPolicy = _Gs2310DHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 4),
    _Gs2310DHCPRelayInformationPolicy_Type()
)
gs2310DHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayInformationPolicy.setStatus("current")
_Gs2310DHCPRelayConfigurationGateways_ObjectIdentity = ObjectIdentity
gs2310DHCPRelayConfigurationGateways = _Gs2310DHCPRelayConfigurationGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5)
)


class _Gs2310DHCPRelayConfigurationGatewaysCreate_Type(Integer32):
    """Custom type gs2310DHCPRelayConfigurationGatewaysCreate based on Integer32"""
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


_Gs2310DHCPRelayConfigurationGatewaysCreate_Type.__name__ = "Integer32"
_Gs2310DHCPRelayConfigurationGatewaysCreate_Object = MibScalar
gs2310DHCPRelayConfigurationGatewaysCreate = _Gs2310DHCPRelayConfigurationGatewaysCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 1),
    _Gs2310DHCPRelayConfigurationGatewaysCreate_Type()
)
gs2310DHCPRelayConfigurationGatewaysCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysCreate.setStatus("current")
_Gs2310DHCPRelayConfigurationGatewaysTable_Object = MibTable
gs2310DHCPRelayConfigurationGatewaysTable = _Gs2310DHCPRelayConfigurationGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysTable.setStatus("current")
_Gs2310DHCPRelayConfigurationGatewaysEntry_Object = MibTableRow
gs2310DHCPRelayConfigurationGatewaysEntry = _Gs2310DHCPRelayConfigurationGatewaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 2, 1)
)
gs2310DHCPRelayConfigurationGatewaysEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310DHCPRelayConfigurationGatewaysIndex"),
)
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysEntry.setStatus("current")


class _Gs2310DHCPRelayConfigurationGatewaysIndex_Type(Integer32):
    """Custom type gs2310DHCPRelayConfigurationGatewaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2310DHCPRelayConfigurationGatewaysIndex_Type.__name__ = "Integer32"
_Gs2310DHCPRelayConfigurationGatewaysIndex_Object = MibTableColumn
gs2310DHCPRelayConfigurationGatewaysIndex = _Gs2310DHCPRelayConfigurationGatewaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 2, 1, 1),
    _Gs2310DHCPRelayConfigurationGatewaysIndex_Type()
)
gs2310DHCPRelayConfigurationGatewaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysIndex.setStatus("current")


class _Gs2310DHCPRelayConfigurationGatewaysVLANId_Type(Integer32):
    """Custom type gs2310DHCPRelayConfigurationGatewaysVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310DHCPRelayConfigurationGatewaysVLANId_Type.__name__ = "Integer32"
_Gs2310DHCPRelayConfigurationGatewaysVLANId_Object = MibTableColumn
gs2310DHCPRelayConfigurationGatewaysVLANId = _Gs2310DHCPRelayConfigurationGatewaysVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 2, 1, 2),
    _Gs2310DHCPRelayConfigurationGatewaysVLANId_Type()
)
gs2310DHCPRelayConfigurationGatewaysVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysVLANId.setStatus("current")
_Gs2310DHCPRelayConfigurationGatewaysIP_Type = IpAddress
_Gs2310DHCPRelayConfigurationGatewaysIP_Object = MibTableColumn
gs2310DHCPRelayConfigurationGatewaysIP = _Gs2310DHCPRelayConfigurationGatewaysIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 2, 1, 3),
    _Gs2310DHCPRelayConfigurationGatewaysIP_Type()
)
gs2310DHCPRelayConfigurationGatewaysIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysIP.setStatus("current")


class _Gs2310DHCPRelayConfigurationGatewaysRowStatus_Type(Integer32):
    """Custom type gs2310DHCPRelayConfigurationGatewaysRowStatus based on Integer32"""
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


_Gs2310DHCPRelayConfigurationGatewaysRowStatus_Type.__name__ = "Integer32"
_Gs2310DHCPRelayConfigurationGatewaysRowStatus_Object = MibTableColumn
gs2310DHCPRelayConfigurationGatewaysRowStatus = _Gs2310DHCPRelayConfigurationGatewaysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 5, 2, 1, 4),
    _Gs2310DHCPRelayConfigurationGatewaysRowStatus_Type()
)
gs2310DHCPRelayConfigurationGatewaysRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayConfigurationGatewaysRowStatus.setStatus("current")


class _Gs2310DHCPRelayInformationCustom_Type(DisplayString):
    """Custom type gs2310DHCPRelayInformationCustom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2310DHCPRelayInformationCustom_Type.__name__ = "DisplayString"
_Gs2310DHCPRelayInformationCustom_Object = MibScalar
gs2310DHCPRelayInformationCustom = _Gs2310DHCPRelayInformationCustom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 1, 1500),
    _Gs2310DHCPRelayInformationCustom_Type()
)
gs2310DHCPRelayInformationCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DHCPRelayInformationCustom.setStatus("current")
_Gs2310DHCPRelayStatistics_ObjectIdentity = ObjectIdentity
gs2310DHCPRelayStatistics = _Gs2310DHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2)
)
_Gs2310DHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
gs2310DHCPRelayServerStatistics = _Gs2310DHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1)
)
_Gs2310ServerStatTransmitToServer_Type = Counter32
_Gs2310ServerStatTransmitToServer_Object = MibScalar
gs2310ServerStatTransmitToServer = _Gs2310ServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 1),
    _Gs2310ServerStatTransmitToServer_Type()
)
gs2310ServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatTransmitToServer.setStatus("current")
_Gs2310ServerStatTransmitError_Type = Counter32
_Gs2310ServerStatTransmitError_Object = MibScalar
gs2310ServerStatTransmitError = _Gs2310ServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 2),
    _Gs2310ServerStatTransmitError_Type()
)
gs2310ServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatTransmitError.setStatus("current")
_Gs2310ServerStatReceiveFromServer_Type = Counter32
_Gs2310ServerStatReceiveFromServer_Object = MibScalar
gs2310ServerStatReceiveFromServer = _Gs2310ServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 3),
    _Gs2310ServerStatReceiveFromServer_Type()
)
gs2310ServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatReceiveFromServer.setStatus("current")
_Gs2310ServerStatReceiveMissingAgentOption_Type = Counter32
_Gs2310ServerStatReceiveMissingAgentOption_Object = MibScalar
gs2310ServerStatReceiveMissingAgentOption = _Gs2310ServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 4),
    _Gs2310ServerStatReceiveMissingAgentOption_Type()
)
gs2310ServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatReceiveMissingAgentOption.setStatus("current")
_Gs2310ServerStatReceiveMissingCircuitID_Type = Counter32
_Gs2310ServerStatReceiveMissingCircuitID_Object = MibScalar
gs2310ServerStatReceiveMissingCircuitID = _Gs2310ServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 5),
    _Gs2310ServerStatReceiveMissingCircuitID_Type()
)
gs2310ServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatReceiveMissingCircuitID.setStatus("current")
_Gs2310ServerStatReceiveMissingRemoteID_Type = Counter32
_Gs2310ServerStatReceiveMissingRemoteID_Object = MibScalar
gs2310ServerStatReceiveMissingRemoteID = _Gs2310ServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 6),
    _Gs2310ServerStatReceiveMissingRemoteID_Type()
)
gs2310ServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatReceiveMissingRemoteID.setStatus("current")
_Gs2310ServerStatReceiveBadCircuitID_Type = Counter32
_Gs2310ServerStatReceiveBadCircuitID_Object = MibScalar
gs2310ServerStatReceiveBadCircuitID = _Gs2310ServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 7),
    _Gs2310ServerStatReceiveBadCircuitID_Type()
)
gs2310ServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatReceiveBadCircuitID.setStatus("current")
_Gs2310ServerStatReceiveBadRemoteID_Type = Counter32
_Gs2310ServerStatReceiveBadRemoteID_Object = MibScalar
gs2310ServerStatReceiveBadRemoteID = _Gs2310ServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 1, 8),
    _Gs2310ServerStatReceiveBadRemoteID_Type()
)
gs2310ServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ServerStatReceiveBadRemoteID.setStatus("current")
_Gs2310DHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
gs2310DHCPRelayClientStatistics = _Gs2310DHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2)
)
_Gs2310ClientStatTransmitToClient_Type = Counter32
_Gs2310ClientStatTransmitToClient_Object = MibScalar
gs2310ClientStatTransmitToClient = _Gs2310ClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 1),
    _Gs2310ClientStatTransmitToClient_Type()
)
gs2310ClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatTransmitToClient.setStatus("current")
_Gs2310ClientStatTransmitError_Type = Counter32
_Gs2310ClientStatTransmitError_Object = MibScalar
gs2310ClientStatTransmitError = _Gs2310ClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 2),
    _Gs2310ClientStatTransmitError_Type()
)
gs2310ClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatTransmitError.setStatus("current")
_Gs2310ClientStatReceivefromClient_Type = Counter32
_Gs2310ClientStatReceivefromClient_Object = MibScalar
gs2310ClientStatReceivefromClient = _Gs2310ClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 3),
    _Gs2310ClientStatReceivefromClient_Type()
)
gs2310ClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatReceivefromClient.setStatus("current")
_Gs2310ClientStatReceiveAgentOption_Type = Counter32
_Gs2310ClientStatReceiveAgentOption_Object = MibScalar
gs2310ClientStatReceiveAgentOption = _Gs2310ClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 4),
    _Gs2310ClientStatReceiveAgentOption_Type()
)
gs2310ClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatReceiveAgentOption.setStatus("current")
_Gs2310ClientStatReplaceAgentOption_Type = Counter32
_Gs2310ClientStatReplaceAgentOption_Object = MibScalar
gs2310ClientStatReplaceAgentOption = _Gs2310ClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 5),
    _Gs2310ClientStatReplaceAgentOption_Type()
)
gs2310ClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatReplaceAgentOption.setStatus("current")
_Gs2310ClientStatKeepAgentOption_Type = Counter32
_Gs2310ClientStatKeepAgentOption_Object = MibScalar
gs2310ClientStatKeepAgentOption = _Gs2310ClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 6),
    _Gs2310ClientStatKeepAgentOption_Type()
)
gs2310ClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatKeepAgentOption.setStatus("current")
_Gs2310ClientStatDropAgentOption_Type = Counter32
_Gs2310ClientStatDropAgentOption_Object = MibScalar
gs2310ClientStatDropAgentOption = _Gs2310ClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 4, 2, 2, 7),
    _Gs2310ClientStatDropAgentOption_Type()
)
gs2310ClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310ClientStatDropAgentOption.setStatus("current")
_Gs2310PortSecurity_ObjectIdentity = ObjectIdentity
gs2310PortSecurity = _Gs2310PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5)
)
_Gs2310PortSecLimitCtrl_ObjectIdentity = ObjectIdentity
gs2310PortSecLimitCtrl = _Gs2310PortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1)
)
_Gs2310PortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2310PortSecLimitCtrlSystemConf = _Gs2310PortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 1)
)


class _Gs2310PortSecurityMode_Type(Integer32):
    """Custom type gs2310PortSecurityMode based on Integer32"""
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


_Gs2310PortSecurityMode_Type.__name__ = "Integer32"
_Gs2310PortSecurityMode_Object = MibScalar
gs2310PortSecurityMode = _Gs2310PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 1, 1),
    _Gs2310PortSecurityMode_Type()
)
gs2310PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecurityMode.setStatus("current")


class _Gs2310PortSecurityAging_Type(Integer32):
    """Custom type gs2310PortSecurityAging based on Integer32"""
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


_Gs2310PortSecurityAging_Type.__name__ = "Integer32"
_Gs2310PortSecurityAging_Object = MibScalar
gs2310PortSecurityAging = _Gs2310PortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 1, 2),
    _Gs2310PortSecurityAging_Type()
)
gs2310PortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecurityAging.setStatus("current")


class _Gs2310PortSecurityAgingPeriod_Type(Integer32):
    """Custom type gs2310PortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Gs2310PortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Gs2310PortSecurityAgingPeriod_Object = MibScalar
gs2310PortSecurityAgingPeriod = _Gs2310PortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 1, 3),
    _Gs2310PortSecurityAgingPeriod_Type()
)
gs2310PortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecurityAgingPeriod.setStatus("current")
_Gs2310PortSecLimitCtrlTable_Object = MibTable
gs2310PortSecLimitCtrlTable = _Gs2310PortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlTable.setStatus("current")
_Gs2310PortSecLimitCtrlEntry_Object = MibTableRow
gs2310PortSecLimitCtrlEntry = _Gs2310PortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1)
)
gs2310PortSecLimitCtrlEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlEntry.setStatus("current")


class _Gs2310PortSecLimitCtrlPort_Type(Integer32):
    """Custom type gs2310PortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Gs2310PortSecLimitCtrlPort_Object = MibTableColumn
gs2310PortSecLimitCtrlPort = _Gs2310PortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1, 1),
    _Gs2310PortSecLimitCtrlPort_Type()
)
gs2310PortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlPort.setStatus("current")


class _Gs2310PortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type gs2310PortSecLimitCtrlPortMode based on Integer32"""
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


_Gs2310PortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Gs2310PortSecLimitCtrlPortMode_Object = MibTableColumn
gs2310PortSecLimitCtrlPortMode = _Gs2310PortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1, 2),
    _Gs2310PortSecLimitCtrlPortMode_Type()
)
gs2310PortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlPortMode.setStatus("current")


class _Gs2310PortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type gs2310PortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2310PortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Gs2310PortSecLimitCtrlPortLimit_Object = MibTableColumn
gs2310PortSecLimitCtrlPortLimit = _Gs2310PortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1, 3),
    _Gs2310PortSecLimitCtrlPortLimit_Type()
)
gs2310PortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlPortLimit.setStatus("current")


class _Gs2310PortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type gs2310PortSecLimitCtrlPortAction based on Integer32"""
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


_Gs2310PortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Gs2310PortSecLimitCtrlPortAction_Object = MibTableColumn
gs2310PortSecLimitCtrlPortAction = _Gs2310PortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1, 4),
    _Gs2310PortSecLimitCtrlPortAction_Type()
)
gs2310PortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlPortAction.setStatus("current")
_Gs2310PortSecLimitCtrlPortState_Type = DisplayString
_Gs2310PortSecLimitCtrlPortState_Object = MibTableColumn
gs2310PortSecLimitCtrlPortState = _Gs2310PortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1, 5),
    _Gs2310PortSecLimitCtrlPortState_Type()
)
gs2310PortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlPortState.setStatus("current")


class _Gs2310PortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type gs2310PortSecLimitCtrlPortReOpen based on Integer32"""
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


_Gs2310PortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Gs2310PortSecLimitCtrlPortReOpen_Object = MibTableColumn
gs2310PortSecLimitCtrlPortReOpen = _Gs2310PortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 1, 2, 1, 6),
    _Gs2310PortSecLimitCtrlPortReOpen_Type()
)
gs2310PortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecLimitCtrlPortReOpen.setStatus("current")
_Gs2310PortSecSwitchStatusTable_Object = MibTable
gs2310PortSecSwitchStatusTable = _Gs2310PortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusTable.setStatus("current")
_Gs2310PortSecSwitchStatusEntry_Object = MibTableRow
gs2310PortSecSwitchStatusEntry = _Gs2310PortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2, 1)
)
gs2310PortSecSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusEntry.setStatus("current")


class _Gs2310PortSecSwitchStatusPort_Type(Integer32):
    """Custom type gs2310PortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Gs2310PortSecSwitchStatusPort_Object = MibTableColumn
gs2310PortSecSwitchStatusPort = _Gs2310PortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2, 1, 1),
    _Gs2310PortSecSwitchStatusPort_Type()
)
gs2310PortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusPort.setStatus("current")
_Gs2310PortSecSwitchStatusUsers_Type = DisplayString
_Gs2310PortSecSwitchStatusUsers_Object = MibTableColumn
gs2310PortSecSwitchStatusUsers = _Gs2310PortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2, 1, 2),
    _Gs2310PortSecSwitchStatusUsers_Type()
)
gs2310PortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusUsers.setStatus("current")
_Gs2310PortSecSwitchStatusState_Type = DisplayString
_Gs2310PortSecSwitchStatusState_Object = MibTableColumn
gs2310PortSecSwitchStatusState = _Gs2310PortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2, 1, 3),
    _Gs2310PortSecSwitchStatusState_Type()
)
gs2310PortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusState.setStatus("current")


class _Gs2310PortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type gs2310PortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Gs2310PortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
gs2310PortSecSwitchStatusMACCountCurrent = _Gs2310PortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2, 1, 4),
    _Gs2310PortSecSwitchStatusMACCountCurrent_Type()
)
gs2310PortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Gs2310PortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type gs2310PortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Gs2310PortSecSwitchStatusMACCountLimit_Object = MibTableColumn
gs2310PortSecSwitchStatusMACCountLimit = _Gs2310PortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 2, 1, 5),
    _Gs2310PortSecSwitchStatusMACCountLimit_Type()
)
gs2310PortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecSwitchStatusMACCountLimit.setStatus("current")
_Gs2310PortSecPortStatus_ObjectIdentity = ObjectIdentity
gs2310PortSecPortStatus = _Gs2310PortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3)
)


class _Gs2310PortSecPortStatusPort_Type(Integer32):
    """Custom type gs2310PortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortSecPortStatusPort_Type.__name__ = "Integer32"
_Gs2310PortSecPortStatusPort_Object = MibScalar
gs2310PortSecPortStatusPort = _Gs2310PortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 1),
    _Gs2310PortSecPortStatusPort_Type()
)
gs2310PortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusPort.setStatus("current")
_Gs2310PortSecPortStatusTable_Object = MibTable
gs2310PortSecPortStatusTable = _Gs2310PortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusTable.setStatus("current")
_Gs2310PortSecPortStatusEntry_Object = MibTableRow
gs2310PortSecPortStatusEntry = _Gs2310PortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1)
)
gs2310PortSecPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310PortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusEntry.setStatus("current")


class _Gs2310PortSecPortStatusIndex_Type(Integer32):
    """Custom type gs2310PortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310PortSecPortStatusIndex_Type.__name__ = "Integer32"
_Gs2310PortSecPortStatusIndex_Object = MibTableColumn
gs2310PortSecPortStatusIndex = _Gs2310PortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1, 1),
    _Gs2310PortSecPortStatusIndex_Type()
)
gs2310PortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusIndex.setStatus("current")
_Gs2310PortSecPortStatusMACAddress_Type = MacAddress
_Gs2310PortSecPortStatusMACAddress_Object = MibTableColumn
gs2310PortSecPortStatusMACAddress = _Gs2310PortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1, 2),
    _Gs2310PortSecPortStatusMACAddress_Type()
)
gs2310PortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusMACAddress.setStatus("current")


class _Gs2310PortSecPortStatusVLANId_Type(Integer32):
    """Custom type gs2310PortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310PortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Gs2310PortSecPortStatusVLANId_Object = MibTableColumn
gs2310PortSecPortStatusVLANId = _Gs2310PortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1, 3),
    _Gs2310PortSecPortStatusVLANId_Type()
)
gs2310PortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusVLANId.setStatus("current")
_Gs2310PortSecPortStatusState_Type = DisplayString
_Gs2310PortSecPortStatusState_Object = MibTableColumn
gs2310PortSecPortStatusState = _Gs2310PortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1, 4),
    _Gs2310PortSecPortStatusState_Type()
)
gs2310PortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusState.setStatus("current")
_Gs2310PortSecPortStatusTimeOfAddition_Type = DisplayString
_Gs2310PortSecPortStatusTimeOfAddition_Object = MibTableColumn
gs2310PortSecPortStatusTimeOfAddition = _Gs2310PortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1, 5),
    _Gs2310PortSecPortStatusTimeOfAddition_Type()
)
gs2310PortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusTimeOfAddition.setStatus("current")
_Gs2310PortSecPortStatusAgeAndHold_Type = DisplayString
_Gs2310PortSecPortStatusAgeAndHold_Object = MibTableColumn
gs2310PortSecPortStatusAgeAndHold = _Gs2310PortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 5, 3, 2, 1, 6),
    _Gs2310PortSecPortStatusAgeAndHold_Type()
)
gs2310PortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PortSecPortStatusAgeAndHold.setStatus("current")
_Gs2310AccessManagement_ObjectIdentity = ObjectIdentity
gs2310AccessManagement = _Gs2310AccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6)
)
_Gs2310AccessMgtConf_ObjectIdentity = ObjectIdentity
gs2310AccessMgtConf = _Gs2310AccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1)
)


class _Gs2310AccessMgtConfMode_Type(Integer32):
    """Custom type gs2310AccessMgtConfMode based on Integer32"""
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


_Gs2310AccessMgtConfMode_Type.__name__ = "Integer32"
_Gs2310AccessMgtConfMode_Object = MibScalar
gs2310AccessMgtConfMode = _Gs2310AccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 1),
    _Gs2310AccessMgtConfMode_Type()
)
gs2310AccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtConfMode.setStatus("current")


class _Gs2310AccessMgtConfCreate_Type(Integer32):
    """Custom type gs2310AccessMgtConfCreate based on Integer32"""
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


_Gs2310AccessMgtConfCreate_Type.__name__ = "Integer32"
_Gs2310AccessMgtConfCreate_Object = MibScalar
gs2310AccessMgtConfCreate = _Gs2310AccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 2),
    _Gs2310AccessMgtConfCreate_Type()
)
gs2310AccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtConfCreate.setStatus("current")
_Gs2310AccessMgtConfTable_Object = MibTable
gs2310AccessMgtConfTable = _Gs2310AccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    gs2310AccessMgtConfTable.setStatus("current")
_Gs2310AccessMgtConfEntry_Object = MibTableRow
gs2310AccessMgtConfEntry = _Gs2310AccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1)
)
gs2310AccessMgtConfEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310AccessMgtIndex"),
)
if mibBuilder.loadTexts:
    gs2310AccessMgtConfEntry.setStatus("current")


class _Gs2310AccessMgtIndex_Type(Integer32):
    """Custom type gs2310AccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2310AccessMgtIndex_Type.__name__ = "Integer32"
_Gs2310AccessMgtIndex_Object = MibTableColumn
gs2310AccessMgtIndex = _Gs2310AccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 1),
    _Gs2310AccessMgtIndex_Type()
)
gs2310AccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtIndex.setStatus("current")


class _Gs2310AccessMgtAddresstype_Type(Integer32):
    """Custom type gs2310AccessMgtAddresstype based on Integer32"""
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


_Gs2310AccessMgtAddresstype_Type.__name__ = "Integer32"
_Gs2310AccessMgtAddresstype_Object = MibTableColumn
gs2310AccessMgtAddresstype = _Gs2310AccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 2),
    _Gs2310AccessMgtAddresstype_Type()
)
gs2310AccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtAddresstype.setStatus("current")
_Gs2310AccessMgtStartIpAddress_Type = DisplayString
_Gs2310AccessMgtStartIpAddress_Object = MibTableColumn
gs2310AccessMgtStartIpAddress = _Gs2310AccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 3),
    _Gs2310AccessMgtStartIpAddress_Type()
)
gs2310AccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtStartIpAddress.setStatus("current")
_Gs2310AccessMgtEndIpAddress_Type = DisplayString
_Gs2310AccessMgtEndIpAddress_Object = MibTableColumn
gs2310AccessMgtEndIpAddress = _Gs2310AccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 4),
    _Gs2310AccessMgtEndIpAddress_Type()
)
gs2310AccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtEndIpAddress.setStatus("current")


class _Gs2310AccessMgtHttpHttps_Type(Integer32):
    """Custom type gs2310AccessMgtHttpHttps based on Integer32"""
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


_Gs2310AccessMgtHttpHttps_Type.__name__ = "Integer32"
_Gs2310AccessMgtHttpHttps_Object = MibTableColumn
gs2310AccessMgtHttpHttps = _Gs2310AccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 5),
    _Gs2310AccessMgtHttpHttps_Type()
)
gs2310AccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtHttpHttps.setStatus("current")


class _Gs2310AccessMgtSNMP_Type(Integer32):
    """Custom type gs2310AccessMgtSNMP based on Integer32"""
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


_Gs2310AccessMgtSNMP_Type.__name__ = "Integer32"
_Gs2310AccessMgtSNMP_Object = MibTableColumn
gs2310AccessMgtSNMP = _Gs2310AccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 6),
    _Gs2310AccessMgtSNMP_Type()
)
gs2310AccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtSNMP.setStatus("current")


class _Gs2310AccessMgtTelnetSSH_Type(Integer32):
    """Custom type gs2310AccessMgtTelnetSSH based on Integer32"""
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


_Gs2310AccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Gs2310AccessMgtTelnetSSH_Object = MibTableColumn
gs2310AccessMgtTelnetSSH = _Gs2310AccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 7),
    _Gs2310AccessMgtTelnetSSH_Type()
)
gs2310AccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtTelnetSSH.setStatus("current")


class _Gs2310AccessMgtRowStatus_Type(Integer32):
    """Custom type gs2310AccessMgtRowStatus based on Integer32"""
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


_Gs2310AccessMgtRowStatus_Type.__name__ = "Integer32"
_Gs2310AccessMgtRowStatus_Object = MibTableColumn
gs2310AccessMgtRowStatus = _Gs2310AccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 1, 3, 1, 8),
    _Gs2310AccessMgtRowStatus_Type()
)
gs2310AccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtRowStatus.setStatus("current")
_Gs2310AccessMgtStatistics_ObjectIdentity = ObjectIdentity
gs2310AccessMgtStatistics = _Gs2310AccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2)
)
_Gs2310HttpReceivedPkts_Type = Counter32
_Gs2310HttpReceivedPkts_Object = MibScalar
gs2310HttpReceivedPkts = _Gs2310HttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 1),
    _Gs2310HttpReceivedPkts_Type()
)
gs2310HttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HttpReceivedPkts.setStatus("current")
_Gs2310HttpAllowedPkts_Type = Counter32
_Gs2310HttpAllowedPkts_Object = MibScalar
gs2310HttpAllowedPkts = _Gs2310HttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 2),
    _Gs2310HttpAllowedPkts_Type()
)
gs2310HttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HttpAllowedPkts.setStatus("current")
_Gs2310HttpDiscardedPkts_Type = Counter32
_Gs2310HttpDiscardedPkts_Object = MibScalar
gs2310HttpDiscardedPkts = _Gs2310HttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 3),
    _Gs2310HttpDiscardedPkts_Type()
)
gs2310HttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HttpDiscardedPkts.setStatus("current")
_Gs2310HttpsReceivedPkts_Type = Counter32
_Gs2310HttpsReceivedPkts_Object = MibScalar
gs2310HttpsReceivedPkts = _Gs2310HttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 4),
    _Gs2310HttpsReceivedPkts_Type()
)
gs2310HttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HttpsReceivedPkts.setStatus("current")
_Gs2310HttpsAllowedPkts_Type = Counter32
_Gs2310HttpsAllowedPkts_Object = MibScalar
gs2310HttpsAllowedPkts = _Gs2310HttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 5),
    _Gs2310HttpsAllowedPkts_Type()
)
gs2310HttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HttpsAllowedPkts.setStatus("current")
_Gs2310HttpsDiscardedPkts_Type = Counter32
_Gs2310HttpsDiscardedPkts_Object = MibScalar
gs2310HttpsDiscardedPkts = _Gs2310HttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 6),
    _Gs2310HttpsDiscardedPkts_Type()
)
gs2310HttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310HttpsDiscardedPkts.setStatus("current")
_Gs2310SnmpReceivedPkts_Type = Counter32
_Gs2310SnmpReceivedPkts_Object = MibScalar
gs2310SnmpReceivedPkts = _Gs2310SnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 7),
    _Gs2310SnmpReceivedPkts_Type()
)
gs2310SnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SnmpReceivedPkts.setStatus("current")
_Gs2310SnmpAllowedPkts_Type = Counter32
_Gs2310SnmpAllowedPkts_Object = MibScalar
gs2310SnmpAllowedPkts = _Gs2310SnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 8),
    _Gs2310SnmpAllowedPkts_Type()
)
gs2310SnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SnmpAllowedPkts.setStatus("current")
_Gs2310SnmpDiscardedPkts_Type = Counter32
_Gs2310SnmpDiscardedPkts_Object = MibScalar
gs2310SnmpDiscardedPkts = _Gs2310SnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 9),
    _Gs2310SnmpDiscardedPkts_Type()
)
gs2310SnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SnmpDiscardedPkts.setStatus("current")
_Gs2310TelnetReceivedPkts_Type = Counter32
_Gs2310TelnetReceivedPkts_Object = MibScalar
gs2310TelnetReceivedPkts = _Gs2310TelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 10),
    _Gs2310TelnetReceivedPkts_Type()
)
gs2310TelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310TelnetReceivedPkts.setStatus("current")
_Gs2310TelnetAllowedPkts_Type = Counter32
_Gs2310TelnetAllowedPkts_Object = MibScalar
gs2310TelnetAllowedPkts = _Gs2310TelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 11),
    _Gs2310TelnetAllowedPkts_Type()
)
gs2310TelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310TelnetAllowedPkts.setStatus("current")
_Gs2310TelnetDiscardedPkts_Type = Counter32
_Gs2310TelnetDiscardedPkts_Object = MibScalar
gs2310TelnetDiscardedPkts = _Gs2310TelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 12),
    _Gs2310TelnetDiscardedPkts_Type()
)
gs2310TelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310TelnetDiscardedPkts.setStatus("current")
_Gs2310SSHReceivedPkts_Type = Counter32
_Gs2310SSHReceivedPkts_Object = MibScalar
gs2310SSHReceivedPkts = _Gs2310SSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 13),
    _Gs2310SSHReceivedPkts_Type()
)
gs2310SSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SSHReceivedPkts.setStatus("current")
_Gs2310SSHAllowedPkts_Type = Counter32
_Gs2310SSHAllowedPkts_Object = MibScalar
gs2310SSHAllowedPkts = _Gs2310SSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 14),
    _Gs2310SSHAllowedPkts_Type()
)
gs2310SSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SSHAllowedPkts.setStatus("current")
_Gs2310SSHDiscardedPkts_Type = Counter32
_Gs2310SSHDiscardedPkts_Object = MibScalar
gs2310SSHDiscardedPkts = _Gs2310SSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 15),
    _Gs2310SSHDiscardedPkts_Type()
)
gs2310SSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310SSHDiscardedPkts.setStatus("current")


class _Gs2310AccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type gs2310AccessMgtStatisticsClearAll based on Integer32"""
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


_Gs2310AccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Gs2310AccessMgtStatisticsClearAll_Object = MibScalar
gs2310AccessMgtStatisticsClearAll = _Gs2310AccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 6, 2, 16),
    _Gs2310AccessMgtStatisticsClearAll_Type()
)
gs2310AccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AccessMgtStatisticsClearAll.setStatus("current")
_Gs2310SSH_ObjectIdentity = ObjectIdentity
gs2310SSH = _Gs2310SSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 7)
)


class _Gs2310SSHMode_Type(Integer32):
    """Custom type gs2310SSHMode based on Integer32"""
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


_Gs2310SSHMode_Type.__name__ = "Integer32"
_Gs2310SSHMode_Object = MibScalar
gs2310SSHMode = _Gs2310SSHMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 7, 1),
    _Gs2310SSHMode_Type()
)
gs2310SSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SSHMode.setStatus("current")
_Gs2310HTTPS_ObjectIdentity = ObjectIdentity
gs2310HTTPS = _Gs2310HTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 8)
)


class _Gs2310HTTPSMode_Type(Integer32):
    """Custom type gs2310HTTPSMode based on Integer32"""
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


_Gs2310HTTPSMode_Type.__name__ = "Integer32"
_Gs2310HTTPSMode_Object = MibScalar
gs2310HTTPSMode = _Gs2310HTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 8, 1),
    _Gs2310HTTPSMode_Type()
)
gs2310HTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HTTPSMode.setStatus("current")


class _Gs2310HTTPSAutoRedirect_Type(Integer32):
    """Custom type gs2310HTTPSAutoRedirect based on Integer32"""
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


_Gs2310HTTPSAutoRedirect_Type.__name__ = "Integer32"
_Gs2310HTTPSAutoRedirect_Object = MibScalar
gs2310HTTPSAutoRedirect = _Gs2310HTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 8, 2),
    _Gs2310HTTPSAutoRedirect_Type()
)
gs2310HTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HTTPSAutoRedirect.setStatus("current")


class _Gs2310HTTPSCertRenew_Type(Integer32):
    """Custom type gs2310HTTPSCertRenew based on Integer32"""
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


_Gs2310HTTPSCertRenew_Type.__name__ = "Integer32"
_Gs2310HTTPSCertRenew_Object = MibScalar
gs2310HTTPSCertRenew = _Gs2310HTTPSCertRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 8, 3),
    _Gs2310HTTPSCertRenew_Type()
)
gs2310HTTPSCertRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HTTPSCertRenew.setStatus("current")


class _Gs2310HTTPSMinProtoVersion_Type(Integer32):
    """Custom type gs2310HTTPSMinProtoVersion based on Integer32"""
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


_Gs2310HTTPSMinProtoVersion_Type.__name__ = "Integer32"
_Gs2310HTTPSMinProtoVersion_Object = MibScalar
gs2310HTTPSMinProtoVersion = _Gs2310HTTPSMinProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 8, 4),
    _Gs2310HTTPSMinProtoVersion_Type()
)
gs2310HTTPSMinProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HTTPSMinProtoVersion.setStatus("current")


class _Gs2310HTTPMode_Type(Integer32):
    """Custom type gs2310HTTPMode based on Integer32"""
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


_Gs2310HTTPMode_Type.__name__ = "Integer32"
_Gs2310HTTPMode_Object = MibScalar
gs2310HTTPMode = _Gs2310HTTPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 8, 5),
    _Gs2310HTTPMode_Type()
)
gs2310HTTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HTTPMode.setStatus("current")
_Gs2310AuthMethod_ObjectIdentity = ObjectIdentity
gs2310AuthMethod = _Gs2310AuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9)
)


class _Gs2310ConsoleAuthMethod_Type(Integer32):
    """Custom type gs2310ConsoleAuthMethod based on Integer32"""
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


_Gs2310ConsoleAuthMethod_Type.__name__ = "Integer32"
_Gs2310ConsoleAuthMethod_Object = MibScalar
gs2310ConsoleAuthMethod = _Gs2310ConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 1),
    _Gs2310ConsoleAuthMethod_Type()
)
gs2310ConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ConsoleAuthMethod.setStatus("current")


class _Gs2310ConsoleFallback_Type(Integer32):
    """Custom type gs2310ConsoleFallback based on Integer32"""
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


_Gs2310ConsoleFallback_Type.__name__ = "Integer32"
_Gs2310ConsoleFallback_Object = MibScalar
gs2310ConsoleFallback = _Gs2310ConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 2),
    _Gs2310ConsoleFallback_Type()
)
gs2310ConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ConsoleFallback.setStatus("current")


class _Gs2310TelnetAuthMethod_Type(Integer32):
    """Custom type gs2310TelnetAuthMethod based on Integer32"""
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


_Gs2310TelnetAuthMethod_Type.__name__ = "Integer32"
_Gs2310TelnetAuthMethod_Object = MibScalar
gs2310TelnetAuthMethod = _Gs2310TelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 3),
    _Gs2310TelnetAuthMethod_Type()
)
gs2310TelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TelnetAuthMethod.setStatus("current")


class _Gs2310TelnetFallback_Type(Integer32):
    """Custom type gs2310TelnetFallback based on Integer32"""
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


_Gs2310TelnetFallback_Type.__name__ = "Integer32"
_Gs2310TelnetFallback_Object = MibScalar
gs2310TelnetFallback = _Gs2310TelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 4),
    _Gs2310TelnetFallback_Type()
)
gs2310TelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TelnetFallback.setStatus("current")


class _Gs2310SshAuthMethod_Type(Integer32):
    """Custom type gs2310SshAuthMethod based on Integer32"""
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


_Gs2310SshAuthMethod_Type.__name__ = "Integer32"
_Gs2310SshAuthMethod_Object = MibScalar
gs2310SshAuthMethod = _Gs2310SshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 5),
    _Gs2310SshAuthMethod_Type()
)
gs2310SshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SshAuthMethod.setStatus("current")


class _Gs2310SshFallback_Type(Integer32):
    """Custom type gs2310SshFallback based on Integer32"""
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


_Gs2310SshFallback_Type.__name__ = "Integer32"
_Gs2310SshFallback_Object = MibScalar
gs2310SshFallback = _Gs2310SshFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 6),
    _Gs2310SshFallback_Type()
)
gs2310SshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SshFallback.setStatus("current")


class _Gs2310TftpAuthMethod_Type(Integer32):
    """Custom type gs2310TftpAuthMethod based on Integer32"""
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


_Gs2310TftpAuthMethod_Type.__name__ = "Integer32"
_Gs2310TftpAuthMethod_Object = MibScalar
gs2310TftpAuthMethod = _Gs2310TftpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 9),
    _Gs2310TftpAuthMethod_Type()
)
gs2310TftpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TftpAuthMethod.setStatus("current")


class _Gs2310TftpFallback_Type(Integer32):
    """Custom type gs2310TftpFallback based on Integer32"""
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


_Gs2310TftpFallback_Type.__name__ = "Integer32"
_Gs2310TftpFallback_Object = MibScalar
gs2310TftpFallback = _Gs2310TftpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 10),
    _Gs2310TftpFallback_Type()
)
gs2310TftpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TftpFallback.setStatus("current")


class _Gs2310LoginFailures_Type(Integer32):
    """Custom type gs2310LoginFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Gs2310LoginFailures_Type.__name__ = "Integer32"
_Gs2310LoginFailures_Object = MibScalar
gs2310LoginFailures = _Gs2310LoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 11),
    _Gs2310LoginFailures_Type()
)
gs2310LoginFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LoginFailures.setStatus("current")


class _Gs2310LockMinutes_Type(Integer32):
    """Custom type gs2310LockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Gs2310LockMinutes_Type.__name__ = "Integer32"
_Gs2310LockMinutes_Object = MibScalar
gs2310LockMinutes = _Gs2310LockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 12),
    _Gs2310LockMinutes_Type()
)
gs2310LockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310LockMinutes.setStatus("current")


class _Gs2310HttpAuthMethod_Type(Integer32):
    """Custom type gs2310HttpAuthMethod based on Integer32"""
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


_Gs2310HttpAuthMethod_Type.__name__ = "Integer32"
_Gs2310HttpAuthMethod_Object = MibScalar
gs2310HttpAuthMethod = _Gs2310HttpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 13),
    _Gs2310HttpAuthMethod_Type()
)
gs2310HttpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HttpAuthMethod.setStatus("current")


class _Gs2310HttpFallback_Type(Integer32):
    """Custom type gs2310HttpFallback based on Integer32"""
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


_Gs2310HttpFallback_Type.__name__ = "Integer32"
_Gs2310HttpFallback_Object = MibScalar
gs2310HttpFallback = _Gs2310HttpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 14),
    _Gs2310HttpFallback_Type()
)
gs2310HttpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HttpFallback.setStatus("current")


class _Gs2310HttpsAuthMethod_Type(Integer32):
    """Custom type gs2310HttpsAuthMethod based on Integer32"""
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


_Gs2310HttpsAuthMethod_Type.__name__ = "Integer32"
_Gs2310HttpsAuthMethod_Object = MibScalar
gs2310HttpsAuthMethod = _Gs2310HttpsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 15),
    _Gs2310HttpsAuthMethod_Type()
)
gs2310HttpsAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HttpsAuthMethod.setStatus("current")


class _Gs2310HttpsFallback_Type(Integer32):
    """Custom type gs2310HttpsFallback based on Integer32"""
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


_Gs2310HttpsFallback_Type.__name__ = "Integer32"
_Gs2310HttpsFallback_Object = MibScalar
gs2310HttpsFallback = _Gs2310HttpsFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 9, 16),
    _Gs2310HttpsFallback_Type()
)
gs2310HttpsFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310HttpsFallback.setStatus("current")
_Gs2310AAA_ObjectIdentity = ObjectIdentity
gs2310AAA = _Gs2310AAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10)
)
_Gs2310AAACommonServer_ObjectIdentity = ObjectIdentity
gs2310AAACommonServer = _Gs2310AAACommonServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 1)
)


class _Gs2310AAACommonServerTimeout_Type(Integer32):
    """Custom type gs2310AAACommonServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_Gs2310AAACommonServerTimeout_Type.__name__ = "Integer32"
_Gs2310AAACommonServerTimeout_Object = MibScalar
gs2310AAACommonServerTimeout = _Gs2310AAACommonServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 1, 1),
    _Gs2310AAACommonServerTimeout_Type()
)
gs2310AAACommonServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AAACommonServerTimeout.setStatus("current")


class _Gs2310AAACommonServerDeadTime_Type(Integer32):
    """Custom type gs2310AAACommonServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Gs2310AAACommonServerDeadTime_Type.__name__ = "Integer32"
_Gs2310AAACommonServerDeadTime_Object = MibScalar
gs2310AAACommonServerDeadTime = _Gs2310AAACommonServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 1, 2),
    _Gs2310AAACommonServerDeadTime_Type()
)
gs2310AAACommonServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AAACommonServerDeadTime.setStatus("current")
_Gs2310AAATACACSPlusAuthAndAccounting_ObjectIdentity = ObjectIdentity
gs2310AAATACACSPlusAuthAndAccounting = _Gs2310AAATACACSPlusAuthAndAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 2)
)


class _Gs2310AAAAuthorization_Type(Integer32):
    """Custom type gs2310AAAAuthorization based on Integer32"""
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


_Gs2310AAAAuthorization_Type.__name__ = "Integer32"
_Gs2310AAAAuthorization_Object = MibScalar
gs2310AAAAuthorization = _Gs2310AAAAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 2, 1),
    _Gs2310AAAAuthorization_Type()
)
gs2310AAAAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AAAAuthorization.setStatus("current")


class _Gs2310AAAFallbackToLocalAuthorization_Type(Integer32):
    """Custom type gs2310AAAFallbackToLocalAuthorization based on Integer32"""
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


_Gs2310AAAFallbackToLocalAuthorization_Type.__name__ = "Integer32"
_Gs2310AAAFallbackToLocalAuthorization_Object = MibScalar
gs2310AAAFallbackToLocalAuthorization = _Gs2310AAAFallbackToLocalAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 2, 2),
    _Gs2310AAAFallbackToLocalAuthorization_Type()
)
gs2310AAAFallbackToLocalAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AAAFallbackToLocalAuthorization.setStatus("current")


class _Gs2310AAAAccounting_Type(Integer32):
    """Custom type gs2310AAAAccounting based on Integer32"""
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


_Gs2310AAAAccounting_Type.__name__ = "Integer32"
_Gs2310AAAAccounting_Object = MibScalar
gs2310AAAAccounting = _Gs2310AAAAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 2, 3),
    _Gs2310AAAAccounting_Type()
)
gs2310AAAAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310AAAAccounting.setStatus("current")
_Gs2310RADIUSAuthenticationServerTable_Object = MibTable
gs2310RADIUSAuthenticationServerTable = _Gs2310RADIUSAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3)
)
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerTable.setStatus("current")
_Gs2310RADIUSAuthenticationServerEntry_Object = MibTableRow
gs2310RADIUSAuthenticationServerEntry = _Gs2310RADIUSAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3, 1)
)
gs2310RADIUSAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310RADIUSAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerEntry.setStatus("current")


class _Gs2310RADIUSAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2310RADIUSAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2310RADIUSAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2310RADIUSAuthenticationServerIndex_Object = MibTableColumn
gs2310RADIUSAuthenticationServerIndex = _Gs2310RADIUSAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3, 1, 1),
    _Gs2310RADIUSAuthenticationServerIndex_Type()
)
gs2310RADIUSAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerIndex.setStatus("current")


class _Gs2310RADIUSAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2310RADIUSAuthenticationServerEnable based on Integer32"""
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


_Gs2310RADIUSAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2310RADIUSAuthenticationServerEnable_Object = MibTableColumn
gs2310RADIUSAuthenticationServerEnable = _Gs2310RADIUSAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3, 1, 2),
    _Gs2310RADIUSAuthenticationServerEnable_Type()
)
gs2310RADIUSAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerEnable.setStatus("current")
_Gs2310RADIUSAuthenticationServerIP_Type = DisplayString
_Gs2310RADIUSAuthenticationServerIP_Object = MibTableColumn
gs2310RADIUSAuthenticationServerIP = _Gs2310RADIUSAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3, 1, 3),
    _Gs2310RADIUSAuthenticationServerIP_Type()
)
gs2310RADIUSAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerIP.setStatus("current")


class _Gs2310RADIUSAuthenticationServerPort_Type(Integer32):
    """Custom type gs2310RADIUSAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2310RADIUSAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2310RADIUSAuthenticationServerPort_Object = MibTableColumn
gs2310RADIUSAuthenticationServerPort = _Gs2310RADIUSAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3, 1, 4),
    _Gs2310RADIUSAuthenticationServerPort_Type()
)
gs2310RADIUSAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerPort.setStatus("current")
_Gs2310RADIUSAuthenticationServerSecret_Type = DisplayString
_Gs2310RADIUSAuthenticationServerSecret_Object = MibTableColumn
gs2310RADIUSAuthenticationServerSecret = _Gs2310RADIUSAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 3, 1, 5),
    _Gs2310RADIUSAuthenticationServerSecret_Type()
)
gs2310RADIUSAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthenticationServerSecret.setStatus("current")
_Gs2310RADIUSAccountingServerTable_Object = MibTable
gs2310RADIUSAccountingServerTable = _Gs2310RADIUSAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4)
)
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerTable.setStatus("current")
_Gs2310RADIUSAccountingServerEntry_Object = MibTableRow
gs2310RADIUSAccountingServerEntry = _Gs2310RADIUSAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4, 1)
)
gs2310RADIUSAccountingServerEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310RADIUSAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerEntry.setStatus("current")


class _Gs2310RADIUSAccountingServerIndex_Type(Integer32):
    """Custom type gs2310RADIUSAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2310RADIUSAccountingServerIndex_Type.__name__ = "Integer32"
_Gs2310RADIUSAccountingServerIndex_Object = MibTableColumn
gs2310RADIUSAccountingServerIndex = _Gs2310RADIUSAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4, 1, 1),
    _Gs2310RADIUSAccountingServerIndex_Type()
)
gs2310RADIUSAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerIndex.setStatus("current")


class _Gs2310RADIUSAccountingServerEnable_Type(Integer32):
    """Custom type gs2310RADIUSAccountingServerEnable based on Integer32"""
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


_Gs2310RADIUSAccountingServerEnable_Type.__name__ = "Integer32"
_Gs2310RADIUSAccountingServerEnable_Object = MibTableColumn
gs2310RADIUSAccountingServerEnable = _Gs2310RADIUSAccountingServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4, 1, 2),
    _Gs2310RADIUSAccountingServerEnable_Type()
)
gs2310RADIUSAccountingServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerEnable.setStatus("current")
_Gs2310RADIUSAccountingServerIP_Type = DisplayString
_Gs2310RADIUSAccountingServerIP_Object = MibTableColumn
gs2310RADIUSAccountingServerIP = _Gs2310RADIUSAccountingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4, 1, 3),
    _Gs2310RADIUSAccountingServerIP_Type()
)
gs2310RADIUSAccountingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerIP.setStatus("current")


class _Gs2310RADIUSAccountingServerPort_Type(Integer32):
    """Custom type gs2310RADIUSAccountingServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2310RADIUSAccountingServerPort_Type.__name__ = "Integer32"
_Gs2310RADIUSAccountingServerPort_Object = MibTableColumn
gs2310RADIUSAccountingServerPort = _Gs2310RADIUSAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4, 1, 4),
    _Gs2310RADIUSAccountingServerPort_Type()
)
gs2310RADIUSAccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerPort.setStatus("current")
_Gs2310RADIUSAccountingServerSecret_Type = DisplayString
_Gs2310RADIUSAccountingServerSecret_Object = MibTableColumn
gs2310RADIUSAccountingServerSecret = _Gs2310RADIUSAccountingServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 4, 1, 5),
    _Gs2310RADIUSAccountingServerSecret_Type()
)
gs2310RADIUSAccountingServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingServerSecret.setStatus("current")
_Gs2310TACACSPlusAuthenticationServerTable_Object = MibTable
gs2310TACACSPlusAuthenticationServerTable = _Gs2310TACACSPlusAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5)
)
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerTable.setStatus("current")
_Gs2310TACACSPlusAuthenticationServerEntry_Object = MibTableRow
gs2310TACACSPlusAuthenticationServerEntry = _Gs2310TACACSPlusAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5, 1)
)
gs2310TACACSPlusAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310TACACSPlusAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerEntry.setStatus("current")


class _Gs2310TACACSPlusAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2310TACACSPlusAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2310TACACSPlusAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2310TACACSPlusAuthenticationServerIndex_Object = MibTableColumn
gs2310TACACSPlusAuthenticationServerIndex = _Gs2310TACACSPlusAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5, 1, 1),
    _Gs2310TACACSPlusAuthenticationServerIndex_Type()
)
gs2310TACACSPlusAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerIndex.setStatus("current")


class _Gs2310TACACSPlusAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2310TACACSPlusAuthenticationServerEnable based on Integer32"""
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


_Gs2310TACACSPlusAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2310TACACSPlusAuthenticationServerEnable_Object = MibTableColumn
gs2310TACACSPlusAuthenticationServerEnable = _Gs2310TACACSPlusAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5, 1, 2),
    _Gs2310TACACSPlusAuthenticationServerEnable_Type()
)
gs2310TACACSPlusAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerEnable.setStatus("current")
_Gs2310TACACSPlusAuthenticationServerIP_Type = DisplayString
_Gs2310TACACSPlusAuthenticationServerIP_Object = MibTableColumn
gs2310TACACSPlusAuthenticationServerIP = _Gs2310TACACSPlusAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5, 1, 3),
    _Gs2310TACACSPlusAuthenticationServerIP_Type()
)
gs2310TACACSPlusAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerIP.setStatus("current")


class _Gs2310TACACSPlusAuthenticationServerPort_Type(Integer32):
    """Custom type gs2310TACACSPlusAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2310TACACSPlusAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2310TACACSPlusAuthenticationServerPort_Object = MibTableColumn
gs2310TACACSPlusAuthenticationServerPort = _Gs2310TACACSPlusAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5, 1, 4),
    _Gs2310TACACSPlusAuthenticationServerPort_Type()
)
gs2310TACACSPlusAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerPort.setStatus("current")
_Gs2310TACACSPlusAuthenticationServerSecret_Type = DisplayString
_Gs2310TACACSPlusAuthenticationServerSecret_Object = MibTableColumn
gs2310TACACSPlusAuthenticationServerSecret = _Gs2310TACACSPlusAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 5, 1, 5),
    _Gs2310TACACSPlusAuthenticationServerSecret_Type()
)
gs2310TACACSPlusAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310TACACSPlusAuthenticationServerSecret.setStatus("current")
_Gs2310RADIUSStatisticsTable_Object = MibTable
gs2310RADIUSStatisticsTable = _Gs2310RADIUSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6)
)
if mibBuilder.loadTexts:
    gs2310RADIUSStatisticsTable.setStatus("current")
_Gs2310RADIUSStatisticsEntry_Object = MibTableRow
gs2310RADIUSStatisticsEntry = _Gs2310RADIUSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1)
)
gs2310RADIUSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310RADIUSAuthStatisticsServerIndex"),
)
if mibBuilder.loadTexts:
    gs2310RADIUSStatisticsEntry.setStatus("current")


class _Gs2310RADIUSAuthStatisticsServerIndex_Type(Integer32):
    """Custom type gs2310RADIUSAuthStatisticsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2310RADIUSAuthStatisticsServerIndex_Type.__name__ = "Integer32"
_Gs2310RADIUSAuthStatisticsServerIndex_Object = MibTableColumn
gs2310RADIUSAuthStatisticsServerIndex = _Gs2310RADIUSAuthStatisticsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 1),
    _Gs2310RADIUSAuthStatisticsServerIndex_Type()
)
gs2310RADIUSAuthStatisticsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsServerIndex.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktAccessAccepts_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktAccessAccepts_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktAccessAccepts = _Gs2310RADIUSAuthStatisticsRecPktAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 2),
    _Gs2310RADIUSAuthStatisticsRecPktAccessAccepts_Type()
)
gs2310RADIUSAuthStatisticsRecPktAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktAccessAccepts.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktAccessRejects_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktAccessRejects_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktAccessRejects = _Gs2310RADIUSAuthStatisticsRecPktAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 3),
    _Gs2310RADIUSAuthStatisticsRecPktAccessRejects_Type()
)
gs2310RADIUSAuthStatisticsRecPktAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktAccessRejects.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktAccessChallenges_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktAccessChallenges_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktAccessChallenges = _Gs2310RADIUSAuthStatisticsRecPktAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 4),
    _Gs2310RADIUSAuthStatisticsRecPktAccessChallenges_Type()
)
gs2310RADIUSAuthStatisticsRecPktAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktAccessChallenges.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses = _Gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 5),
    _Gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses_Type()
)
gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktBadAuthenticators = _Gs2310RADIUSAuthStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 6),
    _Gs2310RADIUSAuthStatisticsRecPktBadAuthenticators_Type()
)
gs2310RADIUSAuthStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktUnknownTypes = _Gs2310RADIUSAuthStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 7),
    _Gs2310RADIUSAuthStatisticsRecPktUnknownTypes_Type()
)
gs2310RADIUSAuthStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2310RADIUSAuthStatisticsRecPktDropped_Type = Counter32
_Gs2310RADIUSAuthStatisticsRecPktDropped_Object = MibTableColumn
gs2310RADIUSAuthStatisticsRecPktDropped = _Gs2310RADIUSAuthStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 8),
    _Gs2310RADIUSAuthStatisticsRecPktDropped_Type()
)
gs2310RADIUSAuthStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsRecPktDropped.setStatus("current")
_Gs2310RADIUSAuthStatisticsTransmitPktAccessRequests_Type = Counter32
_Gs2310RADIUSAuthStatisticsTransmitPktAccessRequests_Object = MibTableColumn
gs2310RADIUSAuthStatisticsTransmitPktAccessRequests = _Gs2310RADIUSAuthStatisticsTransmitPktAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 9),
    _Gs2310RADIUSAuthStatisticsTransmitPktAccessRequests_Type()
)
gs2310RADIUSAuthStatisticsTransmitPktAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsTransmitPktAccessRequests.setStatus("current")
_Gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type = Counter32
_Gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object = MibTableColumn
gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions = _Gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 10),
    _Gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type()
)
gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setStatus("current")
_Gs2310RADIUSAuthStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2310RADIUSAuthStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2310RADIUSAuthStatisticsTransmitPktPendingRequests = _Gs2310RADIUSAuthStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 11),
    _Gs2310RADIUSAuthStatisticsTransmitPktPendingRequests_Type()
)
gs2310RADIUSAuthStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2310RADIUSAuthStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2310RADIUSAuthStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2310RADIUSAuthStatisticsTransmitPktTimeouts = _Gs2310RADIUSAuthStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 12),
    _Gs2310RADIUSAuthStatisticsTransmitPktTimeouts_Type()
)
gs2310RADIUSAuthStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2310RADIUSAuthIP_Type = DisplayString
_Gs2310RADIUSAuthIP_Object = MibTableColumn
gs2310RADIUSAuthIP = _Gs2310RADIUSAuthIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 13),
    _Gs2310RADIUSAuthIP_Type()
)
gs2310RADIUSAuthIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthIP.setStatus("current")
_Gs2310RADIUSAuthState_Type = DisplayString
_Gs2310RADIUSAuthState_Object = MibTableColumn
gs2310RADIUSAuthState = _Gs2310RADIUSAuthState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 14),
    _Gs2310RADIUSAuthState_Type()
)
gs2310RADIUSAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthState.setStatus("current")
_Gs2310RADIUSAuthRoundTripTime_Type = DisplayString
_Gs2310RADIUSAuthRoundTripTime_Object = MibTableColumn
gs2310RADIUSAuthRoundTripTime = _Gs2310RADIUSAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 15),
    _Gs2310RADIUSAuthRoundTripTime_Type()
)
gs2310RADIUSAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAuthRoundTripTime.setStatus("current")
_Gs2310RADIUSAccountingStatisticsRecPktResponses_Type = Counter32
_Gs2310RADIUSAccountingStatisticsRecPktResponses_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsRecPktResponses = _Gs2310RADIUSAccountingStatisticsRecPktResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 16),
    _Gs2310RADIUSAccountingStatisticsRecPktResponses_Type()
)
gs2310RADIUSAccountingStatisticsRecPktResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsRecPktResponses.setStatus("current")
_Gs2310RADIUSAccountingStatisticsRecPktMalformedResponses_Type = Counter32
_Gs2310RADIUSAccountingStatisticsRecPktMalformedResponses_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsRecPktMalformedResponses = _Gs2310RADIUSAccountingStatisticsRecPktMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 17),
    _Gs2310RADIUSAccountingStatisticsRecPktMalformedResponses_Type()
)
gs2310RADIUSAccountingStatisticsRecPktMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsRecPktMalformedResponses.setStatus("current")
_Gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators = _Gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 18),
    _Gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators_Type()
)
gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2310RADIUSAccountingStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2310RADIUSAccountingStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsRecPktUnknownTypes = _Gs2310RADIUSAccountingStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 19),
    _Gs2310RADIUSAccountingStatisticsRecPktUnknownTypes_Type()
)
gs2310RADIUSAccountingStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2310RADIUSAccountingStatisticsRecPktDropped_Type = Counter32
_Gs2310RADIUSAccountingStatisticsRecPktDropped_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsRecPktDropped = _Gs2310RADIUSAccountingStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 20),
    _Gs2310RADIUSAccountingStatisticsRecPktDropped_Type()
)
gs2310RADIUSAccountingStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsRecPktDropped.setStatus("current")
_Gs2310RADIUSAccountingStatisticsTransmitPktRequests_Type = Counter32
_Gs2310RADIUSAccountingStatisticsTransmitPktRequests_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsTransmitPktRequests = _Gs2310RADIUSAccountingStatisticsTransmitPktRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 21),
    _Gs2310RADIUSAccountingStatisticsTransmitPktRequests_Type()
)
gs2310RADIUSAccountingStatisticsTransmitPktRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsTransmitPktRequests.setStatus("current")
_Gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions_Type = Counter32
_Gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions = _Gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 22),
    _Gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions_Type()
)
gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions.setStatus("current")
_Gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests = _Gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 23),
    _Gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests_Type()
)
gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2310RADIUSAccountingStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2310RADIUSAccountingStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2310RADIUSAccountingStatisticsTransmitPktTimeouts = _Gs2310RADIUSAccountingStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 24),
    _Gs2310RADIUSAccountingStatisticsTransmitPktTimeouts_Type()
)
gs2310RADIUSAccountingStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2310RADIUSAccountingIP_Type = DisplayString
_Gs2310RADIUSAccountingIP_Object = MibTableColumn
gs2310RADIUSAccountingIP = _Gs2310RADIUSAccountingIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 25),
    _Gs2310RADIUSAccountingIP_Type()
)
gs2310RADIUSAccountingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingIP.setStatus("current")
_Gs2310RADIUSAccountingState_Type = DisplayString
_Gs2310RADIUSAccountingState_Object = MibTableColumn
gs2310RADIUSAccountingState = _Gs2310RADIUSAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 26),
    _Gs2310RADIUSAccountingState_Type()
)
gs2310RADIUSAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingState.setStatus("current")
_Gs2310RADIUSAccountingRoundTripTime_Type = DisplayString
_Gs2310RADIUSAccountingRoundTripTime_Object = MibTableColumn
gs2310RADIUSAccountingRoundTripTime = _Gs2310RADIUSAccountingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 27),
    _Gs2310RADIUSAccountingRoundTripTime_Type()
)
gs2310RADIUSAccountingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310RADIUSAccountingRoundTripTime.setStatus("current")


class _Gs2310RADIUSStatisticsClear_Type(Integer32):
    """Custom type gs2310RADIUSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2310RADIUSStatisticsClear_Type.__name__ = "Integer32"
_Gs2310RADIUSStatisticsClear_Object = MibTableColumn
gs2310RADIUSStatisticsClear = _Gs2310RADIUSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 10, 6, 1, 28),
    _Gs2310RADIUSStatisticsClear_Type()
)
gs2310RADIUSStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RADIUSStatisticsClear.setStatus("current")
_Gs2310NAS_ObjectIdentity = ObjectIdentity
gs2310NAS = _Gs2310NAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11)
)
_Gs2310NASConfiguration_ObjectIdentity = ObjectIdentity
gs2310NASConfiguration = _Gs2310NASConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1)
)


class _Gs2310NASConfigMode_Type(Integer32):
    """Custom type gs2310NASConfigMode based on Integer32"""
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


_Gs2310NASConfigMode_Type.__name__ = "Integer32"
_Gs2310NASConfigMode_Object = MibScalar
gs2310NASConfigMode = _Gs2310NASConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 1),
    _Gs2310NASConfigMode_Type()
)
gs2310NASConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigMode.setStatus("current")


class _Gs2310NASConfigReauthEnabled_Type(Integer32):
    """Custom type gs2310NASConfigReauthEnabled based on Integer32"""
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


_Gs2310NASConfigReauthEnabled_Type.__name__ = "Integer32"
_Gs2310NASConfigReauthEnabled_Object = MibScalar
gs2310NASConfigReauthEnabled = _Gs2310NASConfigReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 2),
    _Gs2310NASConfigReauthEnabled_Type()
)
gs2310NASConfigReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigReauthEnabled.setStatus("current")


class _Gs2310NASConfigReauthPeriod_Type(Integer32):
    """Custom type gs2310NASConfigReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Gs2310NASConfigReauthPeriod_Type.__name__ = "Integer32"
_Gs2310NASConfigReauthPeriod_Object = MibScalar
gs2310NASConfigReauthPeriod = _Gs2310NASConfigReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 3),
    _Gs2310NASConfigReauthPeriod_Type()
)
gs2310NASConfigReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigReauthPeriod.setStatus("current")


class _Gs2310NASConfigEAPOLTimeout_Type(Integer32):
    """Custom type gs2310NASConfigEAPOLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2310NASConfigEAPOLTimeout_Type.__name__ = "Integer32"
_Gs2310NASConfigEAPOLTimeout_Object = MibScalar
gs2310NASConfigEAPOLTimeout = _Gs2310NASConfigEAPOLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 4),
    _Gs2310NASConfigEAPOLTimeout_Type()
)
gs2310NASConfigEAPOLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigEAPOLTimeout.setStatus("current")


class _Gs2310NASConfigAgingPeriod_Type(Integer32):
    """Custom type gs2310NASConfigAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2310NASConfigAgingPeriod_Type.__name__ = "Integer32"
_Gs2310NASConfigAgingPeriod_Object = MibScalar
gs2310NASConfigAgingPeriod = _Gs2310NASConfigAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 5),
    _Gs2310NASConfigAgingPeriod_Type()
)
gs2310NASConfigAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigAgingPeriod.setStatus("current")


class _Gs2310NASConfigHoldTime_Type(Integer32):
    """Custom type gs2310NASConfigHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2310NASConfigHoldTime_Type.__name__ = "Integer32"
_Gs2310NASConfigHoldTime_Object = MibScalar
gs2310NASConfigHoldTime = _Gs2310NASConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 6),
    _Gs2310NASConfigHoldTime_Type()
)
gs2310NASConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigHoldTime.setStatus("current")


class _Gs2310NASConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2310NASConfigRADIUSAssignedQoSEnabled based on Integer32"""
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


_Gs2310NASConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2310NASConfigRADIUSAssignedQoSEnabled_Object = MibScalar
gs2310NASConfigRADIUSAssignedQoSEnabled = _Gs2310NASConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 7),
    _Gs2310NASConfigRADIUSAssignedQoSEnabled_Type()
)
gs2310NASConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2310NASConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2310NASConfigRADIUSAssignedVLANEnabled based on Integer32"""
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


_Gs2310NASConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2310NASConfigRADIUSAssignedVLANEnabled_Object = MibScalar
gs2310NASConfigRADIUSAssignedVLANEnabled = _Gs2310NASConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 8),
    _Gs2310NASConfigRADIUSAssignedVLANEnabled_Type()
)
gs2310NASConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2310NASConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2310NASConfigGuestVLANEnabled based on Integer32"""
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


_Gs2310NASConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2310NASConfigGuestVLANEnabled_Object = MibScalar
gs2310NASConfigGuestVLANEnabled = _Gs2310NASConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 9),
    _Gs2310NASConfigGuestVLANEnabled_Type()
)
gs2310NASConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigGuestVLANEnabled.setStatus("current")


class _Gs2310NASConfigGuestVLANID_Type(Integer32):
    """Custom type gs2310NASConfigGuestVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2310NASConfigGuestVLANID_Type.__name__ = "Integer32"
_Gs2310NASConfigGuestVLANID_Object = MibScalar
gs2310NASConfigGuestVLANID = _Gs2310NASConfigGuestVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 10),
    _Gs2310NASConfigGuestVLANID_Type()
)
gs2310NASConfigGuestVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigGuestVLANID.setStatus("current")


class _Gs2310NASConfigMaxReauthCount_Type(Integer32):
    """Custom type gs2310NASConfigMaxReauthCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2310NASConfigMaxReauthCount_Type.__name__ = "Integer32"
_Gs2310NASConfigMaxReauthCount_Object = MibScalar
gs2310NASConfigMaxReauthCount = _Gs2310NASConfigMaxReauthCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 11),
    _Gs2310NASConfigMaxReauthCount_Type()
)
gs2310NASConfigMaxReauthCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigMaxReauthCount.setStatus("current")


class _Gs2310NASConfigAllowGuestVLANEAPOLSeen_Type(Integer32):
    """Custom type gs2310NASConfigAllowGuestVLANEAPOLSeen based on Integer32"""
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


_Gs2310NASConfigAllowGuestVLANEAPOLSeen_Type.__name__ = "Integer32"
_Gs2310NASConfigAllowGuestVLANEAPOLSeen_Object = MibScalar
gs2310NASConfigAllowGuestVLANEAPOLSeen = _Gs2310NASConfigAllowGuestVLANEAPOLSeen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 12),
    _Gs2310NASConfigAllowGuestVLANEAPOLSeen_Type()
)
gs2310NASConfigAllowGuestVLANEAPOLSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigAllowGuestVLANEAPOLSeen.setStatus("current")
_Gs2310NASPortConfigTable_Object = MibTable
gs2310NASPortConfigTable = _Gs2310NASPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13)
)
if mibBuilder.loadTexts:
    gs2310NASPortConfigTable.setStatus("current")
_Gs2310NASPortConfigEntry_Object = MibTableRow
gs2310NASPortConfigEntry = _Gs2310NASPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1)
)
gs2310NASPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2310NASPortConfigEntry.setStatus("current")


class _Gs2310NASPortConfigPort_Type(Integer32):
    """Custom type gs2310NASPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2310NASPortConfigPort_Type.__name__ = "Integer32"
_Gs2310NASPortConfigPort_Object = MibTableColumn
gs2310NASPortConfigPort = _Gs2310NASPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 1),
    _Gs2310NASPortConfigPort_Type()
)
gs2310NASPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310NASPortConfigPort.setStatus("current")


class _Gs2310NASPortConfigAdminState_Type(Integer32):
    """Custom type gs2310NASPortConfigAdminState based on Integer32"""
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


_Gs2310NASPortConfigAdminState_Type.__name__ = "Integer32"
_Gs2310NASPortConfigAdminState_Object = MibTableColumn
gs2310NASPortConfigAdminState = _Gs2310NASPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 2),
    _Gs2310NASPortConfigAdminState_Type()
)
gs2310NASPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigAdminState.setStatus("current")


class _Gs2310NASPortConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2310NASPortConfigRADIUSAssignedQoSEnabled based on Integer32"""
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


_Gs2310NASPortConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2310NASPortConfigRADIUSAssignedQoSEnabled_Object = MibTableColumn
gs2310NASPortConfigRADIUSAssignedQoSEnabled = _Gs2310NASPortConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 3),
    _Gs2310NASPortConfigRADIUSAssignedQoSEnabled_Type()
)
gs2310NASPortConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2310NASPortConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2310NASPortConfigRADIUSAssignedVLANEnabled based on Integer32"""
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


_Gs2310NASPortConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2310NASPortConfigRADIUSAssignedVLANEnabled_Object = MibTableColumn
gs2310NASPortConfigRADIUSAssignedVLANEnabled = _Gs2310NASPortConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 4),
    _Gs2310NASPortConfigRADIUSAssignedVLANEnabled_Type()
)
gs2310NASPortConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2310NASPortConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2310NASPortConfigGuestVLANEnabled based on Integer32"""
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


_Gs2310NASPortConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2310NASPortConfigGuestVLANEnabled_Object = MibTableColumn
gs2310NASPortConfigGuestVLANEnabled = _Gs2310NASPortConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 5),
    _Gs2310NASPortConfigGuestVLANEnabled_Type()
)
gs2310NASPortConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigGuestVLANEnabled.setStatus("current")
_Gs2310NASPortConfigPortState_Type = DisplayString
_Gs2310NASPortConfigPortState_Object = MibTableColumn
gs2310NASPortConfigPortState = _Gs2310NASPortConfigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 6),
    _Gs2310NASPortConfigPortState_Type()
)
gs2310NASPortConfigPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASPortConfigPortState.setStatus("current")


class _Gs2310NASPortConfigReauthenticate_Type(Integer32):
    """Custom type gs2310NASPortConfigReauthenticate based on Integer32"""
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


_Gs2310NASPortConfigReauthenticate_Type.__name__ = "Integer32"
_Gs2310NASPortConfigReauthenticate_Object = MibTableColumn
gs2310NASPortConfigReauthenticate = _Gs2310NASPortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 7),
    _Gs2310NASPortConfigReauthenticate_Type()
)
gs2310NASPortConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigReauthenticate.setStatus("current")


class _Gs2310NASPortConfigReinitialize_Type(Integer32):
    """Custom type gs2310NASPortConfigReinitialize based on Integer32"""
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


_Gs2310NASPortConfigReinitialize_Type.__name__ = "Integer32"
_Gs2310NASPortConfigReinitialize_Object = MibTableColumn
gs2310NASPortConfigReinitialize = _Gs2310NASPortConfigReinitialize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 8),
    _Gs2310NASPortConfigReinitialize_Type()
)
gs2310NASPortConfigReinitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigReinitialize.setStatus("current")


class _Gs2310NASPortConfigFallbackEnabled_Type(Integer32):
    """Custom type gs2310NASPortConfigFallbackEnabled based on Integer32"""
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


_Gs2310NASPortConfigFallbackEnabled_Type.__name__ = "Integer32"
_Gs2310NASPortConfigFallbackEnabled_Object = MibTableColumn
gs2310NASPortConfigFallbackEnabled = _Gs2310NASPortConfigFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 13, 1, 101),
    _Gs2310NASPortConfigFallbackEnabled_Type()
)
gs2310NASPortConfigFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASPortConfigFallbackEnabled.setStatus("current")


class _Gs2310NASConfigMacBasedUseEAP_Type(Integer32):
    """Custom type gs2310NASConfigMacBasedUseEAP based on Integer32"""
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


_Gs2310NASConfigMacBasedUseEAP_Type.__name__ = "Integer32"
_Gs2310NASConfigMacBasedUseEAP_Object = MibScalar
gs2310NASConfigMacBasedUseEAP = _Gs2310NASConfigMacBasedUseEAP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 1, 101),
    _Gs2310NASConfigMacBasedUseEAP_Type()
)
gs2310NASConfigMacBasedUseEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASConfigMacBasedUseEAP.setStatus("current")
_Gs2310NASSwitchStatusTable_Object = MibTable
gs2310NASSwitchStatusTable = _Gs2310NASSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2)
)
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusTable.setStatus("current")
_Gs2310NASSwitchStatusEntry_Object = MibTableRow
gs2310NASSwitchStatusEntry = _Gs2310NASSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1)
)
gs2310NASSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusEntry.setStatus("current")
_Gs2310NASSwitchStatusAdminState_Type = DisplayString
_Gs2310NASSwitchStatusAdminState_Object = MibTableColumn
gs2310NASSwitchStatusAdminState = _Gs2310NASSwitchStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1, 2),
    _Gs2310NASSwitchStatusAdminState_Type()
)
gs2310NASSwitchStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusAdminState.setStatus("current")
_Gs2310NASSwitchStatusPortState_Type = DisplayString
_Gs2310NASSwitchStatusPortState_Object = MibTableColumn
gs2310NASSwitchStatusPortState = _Gs2310NASSwitchStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1, 3),
    _Gs2310NASSwitchStatusPortState_Type()
)
gs2310NASSwitchStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusPortState.setStatus("current")
_Gs2310NASSwitchStatusLastSource_Type = DisplayString
_Gs2310NASSwitchStatusLastSource_Object = MibTableColumn
gs2310NASSwitchStatusLastSource = _Gs2310NASSwitchStatusLastSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1, 4),
    _Gs2310NASSwitchStatusLastSource_Type()
)
gs2310NASSwitchStatusLastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusLastSource.setStatus("current")
_Gs2310NASSwitchStatusLastID_Type = DisplayString
_Gs2310NASSwitchStatusLastID_Object = MibTableColumn
gs2310NASSwitchStatusLastID = _Gs2310NASSwitchStatusLastID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1, 5),
    _Gs2310NASSwitchStatusLastID_Type()
)
gs2310NASSwitchStatusLastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusLastID.setStatus("current")
_Gs2310NASSwitchStatusQoSClass_Type = DisplayString
_Gs2310NASSwitchStatusQoSClass_Object = MibTableColumn
gs2310NASSwitchStatusQoSClass = _Gs2310NASSwitchStatusQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1, 6),
    _Gs2310NASSwitchStatusQoSClass_Type()
)
gs2310NASSwitchStatusQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusQoSClass.setStatus("current")
_Gs2310NASSwitchStatusPortVlanID_Type = DisplayString
_Gs2310NASSwitchStatusPortVlanID_Object = MibTableColumn
gs2310NASSwitchStatusPortVlanID = _Gs2310NASSwitchStatusPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 2, 1, 7),
    _Gs2310NASSwitchStatusPortVlanID_Type()
)
gs2310NASSwitchStatusPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASSwitchStatusPortVlanID.setStatus("current")
_Gs2310NASPortStatus_ObjectIdentity = ObjectIdentity
gs2310NASPortStatus = _Gs2310NASPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3)
)
_Gs2310NASPortStatusCountersTable_Object = MibTable
gs2310NASPortStatusCountersTable = _Gs2310NASPortStatusCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    gs2310NASPortStatusCountersTable.setStatus("current")
_Gs2310NASPortStatusCountersEntry_Object = MibTableRow
gs2310NASPortStatusCountersEntry = _Gs2310NASPortStatusCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1)
)
gs2310NASPortStatusCountersEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2310NASPortStatusCountersEntry.setStatus("current")
_Gs2310NASRxCountersEAPOLTotal_Type = Counter32
_Gs2310NASRxCountersEAPOLTotal_Object = MibTableColumn
gs2310NASRxCountersEAPOLTotal = _Gs2310NASRxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 2),
    _Gs2310NASRxCountersEAPOLTotal_Type()
)
gs2310NASRxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLTotal.setStatus("current")
_Gs2310NASRxCountersEAPOLResponseID_Type = Counter32
_Gs2310NASRxCountersEAPOLResponseID_Object = MibTableColumn
gs2310NASRxCountersEAPOLResponseID = _Gs2310NASRxCountersEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 3),
    _Gs2310NASRxCountersEAPOLResponseID_Type()
)
gs2310NASRxCountersEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLResponseID.setStatus("current")
_Gs2310NASRxCountersEAPOLResponses_Type = Counter32
_Gs2310NASRxCountersEAPOLResponses_Object = MibTableColumn
gs2310NASRxCountersEAPOLResponses = _Gs2310NASRxCountersEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 4),
    _Gs2310NASRxCountersEAPOLResponses_Type()
)
gs2310NASRxCountersEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLResponses.setStatus("current")
_Gs2310NASRxCountersEAPOLStart_Type = Counter32
_Gs2310NASRxCountersEAPOLStart_Object = MibTableColumn
gs2310NASRxCountersEAPOLStart = _Gs2310NASRxCountersEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 5),
    _Gs2310NASRxCountersEAPOLStart_Type()
)
gs2310NASRxCountersEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLStart.setStatus("current")
_Gs2310NASRxCountersEAPOLLogoff_Type = Counter32
_Gs2310NASRxCountersEAPOLLogoff_Object = MibTableColumn
gs2310NASRxCountersEAPOLLogoff = _Gs2310NASRxCountersEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 6),
    _Gs2310NASRxCountersEAPOLLogoff_Type()
)
gs2310NASRxCountersEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLLogoff.setStatus("current")
_Gs2310NASRxCountersEAPOLInvalidType_Type = Counter32
_Gs2310NASRxCountersEAPOLInvalidType_Object = MibTableColumn
gs2310NASRxCountersEAPOLInvalidType = _Gs2310NASRxCountersEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 7),
    _Gs2310NASRxCountersEAPOLInvalidType_Type()
)
gs2310NASRxCountersEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLInvalidType.setStatus("current")
_Gs2310NASRxCountersEAPOLInvalidLength_Type = Counter32
_Gs2310NASRxCountersEAPOLInvalidLength_Object = MibTableColumn
gs2310NASRxCountersEAPOLInvalidLength = _Gs2310NASRxCountersEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 8),
    _Gs2310NASRxCountersEAPOLInvalidLength_Type()
)
gs2310NASRxCountersEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxCountersEAPOLInvalidLength.setStatus("current")
_Gs2310NASTxCountersEAPOLTotal_Type = Counter32
_Gs2310NASTxCountersEAPOLTotal_Object = MibTableColumn
gs2310NASTxCountersEAPOLTotal = _Gs2310NASTxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 9),
    _Gs2310NASTxCountersEAPOLTotal_Type()
)
gs2310NASTxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxCountersEAPOLTotal.setStatus("current")
_Gs2310NASTxCountersEAPOLRequestID_Type = Counter32
_Gs2310NASTxCountersEAPOLRequestID_Object = MibTableColumn
gs2310NASTxCountersEAPOLRequestID = _Gs2310NASTxCountersEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 10),
    _Gs2310NASTxCountersEAPOLRequestID_Type()
)
gs2310NASTxCountersEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxCountersEAPOLRequestID.setStatus("current")
_Gs2310NASTxCountersEAPOLRequests_Type = Counter32
_Gs2310NASTxCountersEAPOLRequests_Object = MibTableColumn
gs2310NASTxCountersEAPOLRequests = _Gs2310NASTxCountersEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 11),
    _Gs2310NASTxCountersEAPOLRequests_Type()
)
gs2310NASTxCountersEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxCountersEAPOLRequests.setStatus("current")
_Gs2310NASRxBackendServerCountersAccessChallenges_Type = Counter32
_Gs2310NASRxBackendServerCountersAccessChallenges_Object = MibTableColumn
gs2310NASRxBackendServerCountersAccessChallenges = _Gs2310NASRxBackendServerCountersAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 12),
    _Gs2310NASRxBackendServerCountersAccessChallenges_Type()
)
gs2310NASRxBackendServerCountersAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerCountersAccessChallenges.setStatus("current")
_Gs2310NASRxBackendServerCountersOtherRequests_Type = Counter32
_Gs2310NASRxBackendServerCountersOtherRequests_Object = MibTableColumn
gs2310NASRxBackendServerCountersOtherRequests = _Gs2310NASRxBackendServerCountersOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 13),
    _Gs2310NASRxBackendServerCountersOtherRequests_Type()
)
gs2310NASRxBackendServerCountersOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerCountersOtherRequests.setStatus("current")
_Gs2310NASRxBackendServerCountersAuthSuccesses_Type = Counter32
_Gs2310NASRxBackendServerCountersAuthSuccesses_Object = MibTableColumn
gs2310NASRxBackendServerCountersAuthSuccesses = _Gs2310NASRxBackendServerCountersAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 14),
    _Gs2310NASRxBackendServerCountersAuthSuccesses_Type()
)
gs2310NASRxBackendServerCountersAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerCountersAuthSuccesses.setStatus("current")
_Gs2310NASRxBackendServerCountersAuthFailures_Type = Counter32
_Gs2310NASRxBackendServerCountersAuthFailures_Object = MibTableColumn
gs2310NASRxBackendServerCountersAuthFailures = _Gs2310NASRxBackendServerCountersAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 15),
    _Gs2310NASRxBackendServerCountersAuthFailures_Type()
)
gs2310NASRxBackendServerCountersAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerCountersAuthFailures.setStatus("current")
_Gs2310NASTxBackendServerCountersResponses_Type = Counter32
_Gs2310NASTxBackendServerCountersResponses_Object = MibTableColumn
gs2310NASTxBackendServerCountersResponses = _Gs2310NASTxBackendServerCountersResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 16),
    _Gs2310NASTxBackendServerCountersResponses_Type()
)
gs2310NASTxBackendServerCountersResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxBackendServerCountersResponses.setStatus("current")
_Gs2310NASLastSupplicantInfoMACAddress_Type = DisplayString
_Gs2310NASLastSupplicantInfoMACAddress_Object = MibTableColumn
gs2310NASLastSupplicantInfoMACAddress = _Gs2310NASLastSupplicantInfoMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 17),
    _Gs2310NASLastSupplicantInfoMACAddress_Type()
)
gs2310NASLastSupplicantInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASLastSupplicantInfoMACAddress.setStatus("current")
_Gs2310NASLastSupplicantInfoVlanID_Type = Integer32
_Gs2310NASLastSupplicantInfoVlanID_Object = MibTableColumn
gs2310NASLastSupplicantInfoVlanID = _Gs2310NASLastSupplicantInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 18),
    _Gs2310NASLastSupplicantInfoVlanID_Type()
)
gs2310NASLastSupplicantInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASLastSupplicantInfoVlanID.setStatus("current")
_Gs2310NASLastSupplicantInfoVersion_Type = Integer32
_Gs2310NASLastSupplicantInfoVersion_Object = MibTableColumn
gs2310NASLastSupplicantInfoVersion = _Gs2310NASLastSupplicantInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 19),
    _Gs2310NASLastSupplicantInfoVersion_Type()
)
gs2310NASLastSupplicantInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASLastSupplicantInfoVersion.setStatus("current")
_Gs2310NASLastSupplicantInfoIdentity_Type = DisplayString
_Gs2310NASLastSupplicantInfoIdentity_Object = MibTableColumn
gs2310NASLastSupplicantInfoIdentity = _Gs2310NASLastSupplicantInfoIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 20),
    _Gs2310NASLastSupplicantInfoIdentity_Type()
)
gs2310NASLastSupplicantInfoIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASLastSupplicantInfoIdentity.setStatus("current")


class _Gs2310NASCountersDoClear_Type(Integer32):
    """Custom type gs2310NASCountersDoClear based on Integer32"""
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


_Gs2310NASCountersDoClear_Type.__name__ = "Integer32"
_Gs2310NASCountersDoClear_Object = MibTableColumn
gs2310NASCountersDoClear = _Gs2310NASCountersDoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 1, 1, 21),
    _Gs2310NASCountersDoClear_Type()
)
gs2310NASCountersDoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310NASCountersDoClear.setStatus("current")
_Gs2310NASPortStatusClientsTable_Object = MibTable
gs2310NASPortStatusClientsTable = _Gs2310NASPortStatusClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gs2310NASPortStatusClientsTable.setStatus("current")
_Gs2310NASPortStatusClientsEntry_Object = MibTableRow
gs2310NASPortStatusClientsEntry = _Gs2310NASPortStatusClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1)
)
gs2310NASPortStatusClientsEntry.setIndexNames(
    (0, "LANCOM-GS2310-MIB", "gs2310NASPortConfigPort"),
    (0, "LANCOM-GS2310-MIB", "gs2310NASClientsIndex"),
)
if mibBuilder.loadTexts:
    gs2310NASPortStatusClientsEntry.setStatus("current")


class _Gs2310NASClientsIndex_Type(Integer32):
    """Custom type gs2310NASClientsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2310NASClientsIndex_Type.__name__ = "Integer32"
_Gs2310NASClientsIndex_Object = MibTableColumn
gs2310NASClientsIndex = _Gs2310NASClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 1),
    _Gs2310NASClientsIndex_Type()
)
gs2310NASClientsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2310NASClientsIndex.setStatus("current")
_Gs2310NASClientsIdentity_Type = DisplayString
_Gs2310NASClientsIdentity_Object = MibTableColumn
gs2310NASClientsIdentity = _Gs2310NASClientsIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 2),
    _Gs2310NASClientsIdentity_Type()
)
gs2310NASClientsIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASClientsIdentity.setStatus("current")
_Gs2310NASClientsMACAddress_Type = DisplayString
_Gs2310NASClientsMACAddress_Object = MibTableColumn
gs2310NASClientsMACAddress = _Gs2310NASClientsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 3),
    _Gs2310NASClientsMACAddress_Type()
)
gs2310NASClientsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASClientsMACAddress.setStatus("current")


class _Gs2310NASClientsVlanID_Type(Integer32):
    """Custom type gs2310NASClientsVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2310NASClientsVlanID_Type.__name__ = "Integer32"
_Gs2310NASClientsVlanID_Object = MibTableColumn
gs2310NASClientsVlanID = _Gs2310NASClientsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 4),
    _Gs2310NASClientsVlanID_Type()
)
gs2310NASClientsVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASClientsVlanID.setStatus("current")
_Gs2310NASClientsState_Type = DisplayString
_Gs2310NASClientsState_Object = MibTableColumn
gs2310NASClientsState = _Gs2310NASClientsState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 5),
    _Gs2310NASClientsState_Type()
)
gs2310NASClientsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASClientsState.setStatus("current")
_Gs2310NASClientsLastAuth_Type = DisplayString
_Gs2310NASClientsLastAuth_Object = MibTableColumn
gs2310NASClientsLastAuth = _Gs2310NASClientsLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 6),
    _Gs2310NASClientsLastAuth_Type()
)
gs2310NASClientsLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASClientsLastAuth.setStatus("current")
_Gs2310NASRxClientsEAPOLTotal_Type = Counter32
_Gs2310NASRxClientsEAPOLTotal_Object = MibTableColumn
gs2310NASRxClientsEAPOLTotal = _Gs2310NASRxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 7),
    _Gs2310NASRxClientsEAPOLTotal_Type()
)
gs2310NASRxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLTotal.setStatus("current")
_Gs2310NASRxClientsEAPOLResponseID_Type = Counter32
_Gs2310NASRxClientsEAPOLResponseID_Object = MibTableColumn
gs2310NASRxClientsEAPOLResponseID = _Gs2310NASRxClientsEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 8),
    _Gs2310NASRxClientsEAPOLResponseID_Type()
)
gs2310NASRxClientsEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLResponseID.setStatus("current")
_Gs2310NASRxClientsEAPOLResponses_Type = Counter32
_Gs2310NASRxClientsEAPOLResponses_Object = MibTableColumn
gs2310NASRxClientsEAPOLResponses = _Gs2310NASRxClientsEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 9),
    _Gs2310NASRxClientsEAPOLResponses_Type()
)
gs2310NASRxClientsEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLResponses.setStatus("current")
_Gs2310NASRxClientsEAPOLStart_Type = Counter32
_Gs2310NASRxClientsEAPOLStart_Object = MibTableColumn
gs2310NASRxClientsEAPOLStart = _Gs2310NASRxClientsEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 10),
    _Gs2310NASRxClientsEAPOLStart_Type()
)
gs2310NASRxClientsEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLStart.setStatus("current")
_Gs2310NASRxClientsEAPOLLogoff_Type = Counter32
_Gs2310NASRxClientsEAPOLLogoff_Object = MibTableColumn
gs2310NASRxClientsEAPOLLogoff = _Gs2310NASRxClientsEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 11),
    _Gs2310NASRxClientsEAPOLLogoff_Type()
)
gs2310NASRxClientsEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLLogoff.setStatus("current")
_Gs2310NASRxClientsEAPOLInvalidType_Type = Counter32
_Gs2310NASRxClientsEAPOLInvalidType_Object = MibTableColumn
gs2310NASRxClientsEAPOLInvalidType = _Gs2310NASRxClientsEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 12),
    _Gs2310NASRxClientsEAPOLInvalidType_Type()
)
gs2310NASRxClientsEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLInvalidType.setStatus("current")
_Gs2310NASRxClientsEAPOLInvalidLength_Type = Counter32
_Gs2310NASRxClientsEAPOLInvalidLength_Object = MibTableColumn
gs2310NASRxClientsEAPOLInvalidLength = _Gs2310NASRxClientsEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 13),
    _Gs2310NASRxClientsEAPOLInvalidLength_Type()
)
gs2310NASRxClientsEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxClientsEAPOLInvalidLength.setStatus("current")
_Gs2310NASTxClientsEAPOLTotal_Type = Counter32
_Gs2310NASTxClientsEAPOLTotal_Object = MibTableColumn
gs2310NASTxClientsEAPOLTotal = _Gs2310NASTxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 14),
    _Gs2310NASTxClientsEAPOLTotal_Type()
)
gs2310NASTxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxClientsEAPOLTotal.setStatus("current")
_Gs2310NASTxClientsEAPOLRequestID_Type = Counter32
_Gs2310NASTxClientsEAPOLRequestID_Object = MibTableColumn
gs2310NASTxClientsEAPOLRequestID = _Gs2310NASTxClientsEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 15),
    _Gs2310NASTxClientsEAPOLRequestID_Type()
)
gs2310NASTxClientsEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxClientsEAPOLRequestID.setStatus("current")
_Gs2310NASTxClientsEAPOLRequests_Type = Counter32
_Gs2310NASTxClientsEAPOLRequests_Object = MibTableColumn
gs2310NASTxClientsEAPOLRequests = _Gs2310NASTxClientsEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 16),
    _Gs2310NASTxClientsEAPOLRequests_Type()
)
gs2310NASTxClientsEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxClientsEAPOLRequests.setStatus("current")
_Gs2310NASRxBackendServerClientsAccessChallenges_Type = Counter32
_Gs2310NASRxBackendServerClientsAccessChallenges_Object = MibTableColumn
gs2310NASRxBackendServerClientsAccessChallenges = _Gs2310NASRxBackendServerClientsAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 17),
    _Gs2310NASRxBackendServerClientsAccessChallenges_Type()
)
gs2310NASRxBackendServerClientsAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerClientsAccessChallenges.setStatus("current")
_Gs2310NASRxBackendServerClientsOtherRequests_Type = Counter32
_Gs2310NASRxBackendServerClientsOtherRequests_Object = MibTableColumn
gs2310NASRxBackendServerClientsOtherRequests = _Gs2310NASRxBackendServerClientsOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 18),
    _Gs2310NASRxBackendServerClientsOtherRequests_Type()
)
gs2310NASRxBackendServerClientsOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerClientsOtherRequests.setStatus("current")
_Gs2310NASRxBackendServerClientsAuthSuccesses_Type = Counter32
_Gs2310NASRxBackendServerClientsAuthSuccesses_Object = MibTableColumn
gs2310NASRxBackendServerClientsAuthSuccesses = _Gs2310NASRxBackendServerClientsAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 19),
    _Gs2310NASRxBackendServerClientsAuthSuccesses_Type()
)
gs2310NASRxBackendServerClientsAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerClientsAuthSuccesses.setStatus("current")
_Gs2310NASRxBackendServerClientsAuthFailures_Type = Counter32
_Gs2310NASRxBackendServerClientsAuthFailures_Object = MibTableColumn
gs2310NASRxBackendServerClientsAuthFailures = _Gs2310NASRxBackendServerClientsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 20),
    _Gs2310NASRxBackendServerClientsAuthFailures_Type()
)
gs2310NASRxBackendServerClientsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASRxBackendServerClientsAuthFailures.setStatus("current")
_Gs2310NASTxBackendServerClientsResponses_Type = Counter32
_Gs2310NASTxBackendServerClientsResponses_Object = MibTableColumn
gs2310NASTxBackendServerClientsResponses = _Gs2310NASTxBackendServerClientsResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 3, 11, 3, 2, 1, 21),
    _Gs2310NASTxBackendServerClientsResponses_Type()
)
gs2310NASTxBackendServerClientsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310NASTxBackendServerClientsResponses.setStatus("current")
_Gs2310Maintenance_ObjectIdentity = ObjectIdentity
gs2310Maintenance = _Gs2310Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4)
)


class _Gs2310RestartDevice_Type(Integer32):
    """Custom type gs2310RestartDevice based on Integer32"""
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


_Gs2310RestartDevice_Type.__name__ = "Integer32"
_Gs2310RestartDevice_Object = MibScalar
gs2310RestartDevice = _Gs2310RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 1),
    _Gs2310RestartDevice_Type()
)
gs2310RestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RestartDevice.setStatus("current")
_Gs2310Firmware_ObjectIdentity = ObjectIdentity
gs2310Firmware = _Gs2310Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 2)
)
_Gs2310FirmwareIpAddress_Type = IpAddress
_Gs2310FirmwareIpAddress_Object = MibScalar
gs2310FirmwareIpAddress = _Gs2310FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 2, 1),
    _Gs2310FirmwareIpAddress_Type()
)
gs2310FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FirmwareIpAddress.setStatus("current")
_Gs2310FirmwareFileName_Type = DisplayString
_Gs2310FirmwareFileName_Object = MibScalar
gs2310FirmwareFileName = _Gs2310FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 2, 2),
    _Gs2310FirmwareFileName_Type()
)
gs2310FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FirmwareFileName.setStatus("current")


class _Gs2310DoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2310DoFirmwareUpgrade based on Integer32"""
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


_Gs2310DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2310DoFirmwareUpgrade_Object = MibScalar
gs2310DoFirmwareUpgrade = _Gs2310DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 2, 3),
    _Gs2310DoFirmwareUpgrade_Type()
)
gs2310DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DoFirmwareUpgrade.setStatus("current")
_Gs2310SaveOrRestore_ObjectIdentity = ObjectIdentity
gs2310SaveOrRestore = _Gs2310SaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 3)
)


class _Gs2310FactoryDefaults_Type(Integer32):
    """Custom type gs2310FactoryDefaults based on Integer32"""
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


_Gs2310FactoryDefaults_Type.__name__ = "Integer32"
_Gs2310FactoryDefaults_Object = MibScalar
gs2310FactoryDefaults = _Gs2310FactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 3, 1),
    _Gs2310FactoryDefaults_Type()
)
gs2310FactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310FactoryDefaults.setStatus("current")


class _Gs2310SaveStart_Type(Integer32):
    """Custom type gs2310SaveStart based on Integer32"""
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


_Gs2310SaveStart_Type.__name__ = "Integer32"
_Gs2310SaveStart_Object = MibScalar
gs2310SaveStart = _Gs2310SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 3, 2),
    _Gs2310SaveStart_Type()
)
gs2310SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SaveStart.setStatus("current")


class _Gs2310SaveUser_Type(Integer32):
    """Custom type gs2310SaveUser based on Integer32"""
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


_Gs2310SaveUser_Type.__name__ = "Integer32"
_Gs2310SaveUser_Object = MibScalar
gs2310SaveUser = _Gs2310SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 3, 3),
    _Gs2310SaveUser_Type()
)
gs2310SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310SaveUser.setStatus("current")


class _Gs2310RestoreUser_Type(Integer32):
    """Custom type gs2310RestoreUser based on Integer32"""
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


_Gs2310RestoreUser_Type.__name__ = "Integer32"
_Gs2310RestoreUser_Object = MibScalar
gs2310RestoreUser = _Gs2310RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 3, 4),
    _Gs2310RestoreUser_Type()
)
gs2310RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310RestoreUser.setStatus("current")
_Gs2310ExportOrImport_ObjectIdentity = ObjectIdentity
gs2310ExportOrImport = _Gs2310ExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4)
)
_Gs2310ExportIpAddress_Type = IpAddress
_Gs2310ExportIpAddress_Object = MibScalar
gs2310ExportIpAddress = _Gs2310ExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4, 1),
    _Gs2310ExportIpAddress_Type()
)
gs2310ExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ExportIpAddress.setStatus("current")
_Gs2310ExportConfigName_Type = DisplayString
_Gs2310ExportConfigName_Object = MibScalar
gs2310ExportConfigName = _Gs2310ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4, 2),
    _Gs2310ExportConfigName_Type()
)
gs2310ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ExportConfigName.setStatus("current")


class _Gs2310DoExportConfig_Type(Integer32):
    """Custom type gs2310DoExportConfig based on Integer32"""
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


_Gs2310DoExportConfig_Type.__name__ = "Integer32"
_Gs2310DoExportConfig_Object = MibScalar
gs2310DoExportConfig = _Gs2310DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4, 3),
    _Gs2310DoExportConfig_Type()
)
gs2310DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DoExportConfig.setStatus("current")
_Gs2310ImportIpAddress_Type = IpAddress
_Gs2310ImportIpAddress_Object = MibScalar
gs2310ImportIpAddress = _Gs2310ImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4, 4),
    _Gs2310ImportIpAddress_Type()
)
gs2310ImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ImportIpAddress.setStatus("current")
_Gs2310ImportConfigName_Type = DisplayString
_Gs2310ImportConfigName_Object = MibScalar
gs2310ImportConfigName = _Gs2310ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4, 5),
    _Gs2310ImportConfigName_Type()
)
gs2310ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ImportConfigName.setStatus("current")


class _Gs2310DoImportConfig_Type(Integer32):
    """Custom type gs2310DoImportConfig based on Integer32"""
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


_Gs2310DoImportConfig_Type.__name__ = "Integer32"
_Gs2310DoImportConfig_Object = MibScalar
gs2310DoImportConfig = _Gs2310DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 4, 6),
    _Gs2310DoImportConfig_Type()
)
gs2310DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DoImportConfig.setStatus("current")
_Gs2310Diagnostics_ObjectIdentity = ObjectIdentity
gs2310Diagnostics = _Gs2310Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5)
)
_Gs2310PingIpAddress_Type = IpAddress
_Gs2310PingIpAddress_Object = MibScalar
gs2310PingIpAddress = _Gs2310PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 1),
    _Gs2310PingIpAddress_Type()
)
gs2310PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PingIpAddress.setStatus("current")


class _Gs2310PingSize_Type(Integer32):
    """Custom type gs2310PingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2310PingSize_Type.__name__ = "Integer32"
_Gs2310PingSize_Object = MibScalar
gs2310PingSize = _Gs2310PingSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 2),
    _Gs2310PingSize_Type()
)
gs2310PingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310PingSize.setStatus("current")


class _Gs2310DoPingConfig_Type(Integer32):
    """Custom type gs2310DoPingConfig based on Integer32"""
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


_Gs2310DoPingConfig_Type.__name__ = "Integer32"
_Gs2310DoPingConfig_Object = MibScalar
gs2310DoPingConfig = _Gs2310DoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 3),
    _Gs2310DoPingConfig_Type()
)
gs2310DoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DoPingConfig.setStatus("current")
_Gs2310PingResult_Type = DisplayString
_Gs2310PingResult_Object = MibScalar
gs2310PingResult = _Gs2310PingResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 4),
    _Gs2310PingResult_Type()
)
gs2310PingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310PingResult.setStatus("current")
_Gs2310Ping6IpAddress_Type = DisplayString
_Gs2310Ping6IpAddress_Object = MibScalar
gs2310Ping6IpAddress = _Gs2310Ping6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 5),
    _Gs2310Ping6IpAddress_Type()
)
gs2310Ping6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ping6IpAddress.setStatus("current")


class _Gs2310Ping6Size_Type(Integer32):
    """Custom type gs2310Ping6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2310Ping6Size_Type.__name__ = "Integer32"
_Gs2310Ping6Size_Object = MibScalar
gs2310Ping6Size = _Gs2310Ping6Size_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 6),
    _Gs2310Ping6Size_Type()
)
gs2310Ping6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310Ping6Size.setStatus("current")


class _Gs2310DoPing6Config_Type(Integer32):
    """Custom type gs2310DoPing6Config based on Integer32"""
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


_Gs2310DoPing6Config_Type.__name__ = "Integer32"
_Gs2310DoPing6Config_Object = MibScalar
gs2310DoPing6Config = _Gs2310DoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 7),
    _Gs2310DoPing6Config_Type()
)
gs2310DoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310DoPing6Config.setStatus("current")
_Gs2310Ping6Result_Type = DisplayString
_Gs2310Ping6Result_Object = MibScalar
gs2310Ping6Result = _Gs2310Ping6Result_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 5, 8),
    _Gs2310Ping6Result_Type()
)
gs2310Ping6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Ping6Result.setStatus("current")


class _Gs2310ColdRestartDevice_Type(Integer32):
    """Custom type gs2310ColdRestartDevice based on Integer32"""
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


_Gs2310ColdRestartDevice_Type.__name__ = "Integer32"
_Gs2310ColdRestartDevice_Object = MibScalar
gs2310ColdRestartDevice = _Gs2310ColdRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 4, 1500),
    _Gs2310ColdRestartDevice_Type()
)
gs2310ColdRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2310ColdRestartDevice.setStatus("current")
_Gs2310Trap_ObjectIdentity = ObjectIdentity
gs2310Trap = _Gs2310Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5)
)
_Gs2310TrapEvent_ObjectIdentity = ObjectIdentity
gs2310TrapEvent = _Gs2310TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1)
)
_Gs2310TrapVariable_ObjectIdentity = ObjectIdentity
gs2310TrapVariable = _Gs2310TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 2)
)
_Gs2310Information_Type = DisplayString
_Gs2310Information_Object = MibScalar
gs2310Information = _Gs2310Information_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 2, 1),
    _Gs2310Information_Type()
)
gs2310Information.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2310Information.setStatus("current")

# Managed Objects groups


# Notification objects

gs2310Emergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 1)
)
gs2310Emergency.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Emergency.setStatus(
        "current"
    )

gs2310Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 2)
)
gs2310Alert.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Alert.setStatus(
        "current"
    )

gs2310Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 3)
)
gs2310Critical.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Critical.setStatus(
        "current"
    )

gs2310Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 4)
)
gs2310Error.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Error.setStatus(
        "current"
    )

gs2310Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 5)
)
gs2310Warning.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Warning.setStatus(
        "current"
    )

gs2310Notice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 6)
)
gs2310Notice.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Notice.setStatus(
        "current"
    )

gs2310Informational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 7)
)
gs2310Informational.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Informational.setStatus(
        "current"
    )

gs2310Debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2313, 5, 1, 8)
)
gs2310Debug.setObjects(
    ("LANCOM-GS2310-MIB", "gs2310Information")
)
if mibBuilder.loadTexts:
    gs2310Debug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-GS2310-MIB",
    **{"lancom-systems": lancom_systems,
       "switchingSystems": switchingSystems,
       "gigabitEthernetSwitches": gigabitEthernetSwitches,
       "lancomGS2310": lancomGS2310,
       "gs2310System": gs2310System,
       "gs2310SystemInformation": gs2310SystemInformation,
       "gs2310ModelName": gs2310ModelName,
       "gs2310BIOSVersion": gs2310BIOSVersion,
       "gs2310FirmwareVersion": gs2310FirmwareVersion,
       "gs2310HardwareMechanicalVersion": gs2310HardwareMechanicalVersion,
       "gs2310SerialNumber": gs2310SerialNumber,
       "gs2310HostMACAddress": gs2310HostMACAddress,
       "gs2310ConsoleBaudrate": gs2310ConsoleBaudrate,
       "gs2310RAMSize": gs2310RAMSize,
       "gs2310FlashSize": gs2310FlashSize,
       "gs2310BridgeFDBSize": gs2310BridgeFDBSize,
       "gs2310TransmitQueue": gs2310TransmitQueue,
       "gs2310MaximumFrameSize": gs2310MaximumFrameSize,
       "gs2310CPULoad": gs2310CPULoad,
       "gs2310SystemDescription": gs2310SystemDescription,
       "gs2310Location": gs2310Location,
       "gs2310Contact": gs2310Contact,
       "gs2310DeviceName": gs2310DeviceName,
       "gs2310SystemDate": gs2310SystemDate,
       "gs2310SystemUptime": gs2310SystemUptime,
       "gs2310SystemIPv4Address": gs2310SystemIPv4Address,
       "gs2310SystemIPv4SubnetMask": gs2310SystemIPv4SubnetMask,
       "gs2310SystemIPv4Gateway": gs2310SystemIPv4Gateway,
       "gs2310IPv6LinkLocalAddress": gs2310IPv6LinkLocalAddress,
       "gs2310IPv6Address": gs2310IPv6Address,
       "gs2310IPv6Prefix": gs2310IPv6Prefix,
       "gs2310IPv6Gateway": gs2310IPv6Gateway,
       "gs2310LargestFreeMemBlock": gs2310LargestFreeMemBlock,
       "gs2310MemFree": gs2310MemFree,
       "gs2310SystemTime": gs2310SystemTime,
       "gs2310SystemTimeManual": gs2310SystemTimeManual,
       "gs2310SystemTimeManualClockSource": gs2310SystemTimeManualClockSource,
       "gs2310SystemTimeManualLocaltime": gs2310SystemTimeManualLocaltime,
       "gs2310SystemTimeManualTimeZoneOffset": gs2310SystemTimeManualTimeZoneOffset,
       "gs2310SystemTimeManualDaylightSavings": gs2310SystemTimeManualDaylightSavings,
       "gs2310SystemTimeManualTimeSetOffset": gs2310SystemTimeManualTimeSetOffset,
       "gs2310SystemTimeManualDaylightSavingsType": gs2310SystemTimeManualDaylightSavingsType,
       "gs2310SystemTimeManualDaylightSavingsBydatesFrom": gs2310SystemTimeManualDaylightSavingsBydatesFrom,
       "gs2310SystemTimeManualDaylightSavingsBydatesTo": gs2310SystemTimeManualDaylightSavingsBydatesTo,
       "gs2310SystemTimeManualDaylightSavingsRecurringDayFrom": gs2310SystemTimeManualDaylightSavingsRecurringDayFrom,
       "gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom": gs2310SystemTimeManualDaylightSavingsRecurringWeekFrom,
       "gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom": gs2310SystemTimeManualDaylightSavingsRecurringMonthFrom,
       "gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom": gs2310SystemTimeManualDaylightSavingsRecurringTimeFrom,
       "gs2310SystemTimeManualDaylightSavingsRecurringDayTo": gs2310SystemTimeManualDaylightSavingsRecurringDayTo,
       "gs2310SystemTimeManualDaylightSavingsRecurringWeekTo": gs2310SystemTimeManualDaylightSavingsRecurringWeekTo,
       "gs2310SystemTimeManualDaylightSavingsRecurringMonthTo": gs2310SystemTimeManualDaylightSavingsRecurringMonthTo,
       "gs2310SystemTimeManualDaylightSavingsRecurringTimeTo": gs2310SystemTimeManualDaylightSavingsRecurringTimeTo,
       "gs2310SystemTimeNTP": gs2310SystemTimeNTP,
       "gs2310SystemTimeNTPTable": gs2310SystemTimeNTPTable,
       "gs2310SystemTimeNTPEntry": gs2310SystemTimeNTPEntry,
       "gs2310SystemTimeNTPIndex": gs2310SystemTimeNTPIndex,
       "gs2310SystemTimeNTPServerIPType": gs2310SystemTimeNTPServerIPType,
       "gs2310SystemTimeNTPServer": gs2310SystemTimeNTPServer,
       "gs2310SystemTimeNTPCurrentMode": gs2310SystemTimeNTPCurrentMode,
       "gs2310SystemTimeNTPRequestInterval": gs2310SystemTimeNTPRequestInterval,
       "gs2310SystemTimeNTPTriesNumber": gs2310SystemTimeNTPTriesNumber,
       "gs2310SystemAccount": gs2310SystemAccount,
       "gs2310SystemAccountUsers": gs2310SystemAccountUsers,
       "gs2310SystemAccountUserCreate": gs2310SystemAccountUserCreate,
       "gs2310SystemAccountUsersTable": gs2310SystemAccountUsersTable,
       "gs2310SystemAccountUsersEntry": gs2310SystemAccountUsersEntry,
       "gs2310UserIndex": gs2310UserIndex,
       "gs2310UserName": gs2310UserName,
       "gs2310Password": gs2310Password,
       "gs2310UserPrivilegeLevel": gs2310UserPrivilegeLevel,
       "gs2310AccountUserRowStatus": gs2310AccountUserRowStatus,
       "gs2310SystemAccountUsersSuperUserPassword": gs2310SystemAccountUsersSuperUserPassword,
       "gs2310SystemAccountEnforcePasswordRules": gs2310SystemAccountEnforcePasswordRules,
       "gs2310SystemAccountPrivilegeLevel": gs2310SystemAccountPrivilegeLevel,
       "gs2310AccountPrivilegeLevel": gs2310AccountPrivilegeLevel,
       "gs2310AggregationPrivilegeLevel": gs2310AggregationPrivilegeLevel,
       "gs2310DiagnosticsPrivilegeLevel": gs2310DiagnosticsPrivilegeLevel,
       "gs2310EEEPrivilegeLevel": gs2310EEEPrivilegeLevel,
       "gs2310EasyportPrivilegeLevel": gs2310EasyportPrivilegeLevel,
       "gs2310GARPPrivilegeLevel": gs2310GARPPrivilegeLevel,
       "gs2310GVRPPrivilegeLevel": gs2310GVRPPrivilegeLevel,
       "gs2310IPPrivilegeLevel": gs2310IPPrivilegeLevel,
       "gs2310IPMCSnoopingPrivilegeLevel": gs2310IPMCSnoopingPrivilegeLevel,
       "gs2310LACPPrivilegeLevel": gs2310LACPPrivilegeLevel,
       "gs2310LLDPPrivilegeLevel": gs2310LLDPPrivilegeLevel,
       "gs2310LLDPMEDPrivilegeLevel": gs2310LLDPMEDPrivilegeLevel,
       "gs2310LoopProtectPrivilegeLevel": gs2310LoopProtectPrivilegeLevel,
       "gs2310MACTablePrivilegeLevel": gs2310MACTablePrivilegeLevel,
       "gs2310MVRPrivilegeLevel": gs2310MVRPrivilegeLevel,
       "gs2310MaintenancePrivilegeLevel": gs2310MaintenancePrivilegeLevel,
       "gs2310MirroringPrivilegeLevel": gs2310MirroringPrivilegeLevel,
       "gs2310PortsPrivilegeLevel": gs2310PortsPrivilegeLevel,
       "gs2310PrivateVLANsPrivilegeLevel": gs2310PrivateVLANsPrivilegeLevel,
       "gs2310QoSPrivilegeLevel": gs2310QoSPrivilegeLevel,
       "gs2310SFlowPrivilegeLevel": gs2310SFlowPrivilegeLevel,
       "gs2310SMTPPrivilegeLevel": gs2310SMTPPrivilegeLevel,
       "gs2310SNMPPrivilegeLevel": gs2310SNMPPrivilegeLevel,
       "gs2310SecurityPrivilegeLevel": gs2310SecurityPrivilegeLevel,
       "gs2310SingleIPPrivilegeLevel": gs2310SingleIPPrivilegeLevel,
       "gs2310SpanningTreePrivilegeLevel": gs2310SpanningTreePrivilegeLevel,
       "gs2310SystemPrivilegeLevel": gs2310SystemPrivilegeLevel,
       "gs2310TrapEventPrivilegeLevel": gs2310TrapEventPrivilegeLevel,
       "gs2310UPnPPrivilegeLevel": gs2310UPnPPrivilegeLevel,
       "gs2310VCLPrivilegeLevel": gs2310VCLPrivilegeLevel,
       "gs2310VLANsPrivilegeLevel": gs2310VLANsPrivilegeLevel,
       "gs2310VoiceVLANPrivilegeLevel": gs2310VoiceVLANPrivilegeLevel,
       "gs2310IP": gs2310IP,
       "gs2310IPv4": gs2310IPv4,
       "gs2310IPv4Configured": gs2310IPv4Configured,
       "gs2310Ipv4DHCPClient": gs2310Ipv4DHCPClient,
       "gs2310IPv4Address": gs2310IPv4Address,
       "gs2310IPv4Mask": gs2310IPv4Mask,
       "gs2310IPv4Gateway": gs2310IPv4Gateway,
       "gs2310IPv4VLANId": gs2310IPv4VLANId,
       "gs2310IPv4DNSServer": gs2310IPv4DNSServer,
       "gs2310IPv4DNSProxy": gs2310IPv4DNSProxy,
       "gs2310IPv4Current": gs2310IPv4Current,
       "gs2310Ipv4CurrentDHCPClient": gs2310Ipv4CurrentDHCPClient,
       "gs2310IPv4CurrentAddress": gs2310IPv4CurrentAddress,
       "gs2310IPv4CurrentMask": gs2310IPv4CurrentMask,
       "gs2310IPv4CurrentGateway": gs2310IPv4CurrentGateway,
       "gs2310IPv4CurrentVLANId": gs2310IPv4CurrentVLANId,
       "gs2310IPv4CurrentDNSServer": gs2310IPv4CurrentDNSServer,
       "gs2310IPv6": gs2310IPv6,
       "gs2310IPv6Configured": gs2310IPv6Configured,
       "gs2310Ipv6AutoConfiguration": gs2310Ipv6AutoConfiguration,
       "gs2310Ipv6Address": gs2310Ipv6Address,
       "gs2310Ipv6Prefix": gs2310Ipv6Prefix,
       "gs2310Ipv6Gateway": gs2310Ipv6Gateway,
       "gs2310IPv6Current": gs2310IPv6Current,
       "gs2310Ipv6CurrentAutoConfiguration": gs2310Ipv6CurrentAutoConfiguration,
       "gs2310Ipv6CurrentAddress": gs2310Ipv6CurrentAddress,
       "gs2310Ipv6CurrentLinkLocalAddress": gs2310Ipv6CurrentLinkLocalAddress,
       "gs2310Ipv6CurrentPrefix": gs2310Ipv6CurrentPrefix,
       "gs2310Ipv6CurrentGateway": gs2310Ipv6CurrentGateway,
       "gs2310Syslog": gs2310Syslog,
       "gs2310SyslogConf": gs2310SyslogConf,
       "gs2310ServerMode": gs2310ServerMode,
       "gs2310ServerAddress1": gs2310ServerAddress1,
       "gs2310ServerAddress2": gs2310ServerAddress2,
       "gs2310SyslogLevel": gs2310SyslogLevel,
       "gs2310SyslogDetailedInfo": gs2310SyslogDetailedInfo,
       "gs2310SyslogDetailedInfoClear": gs2310SyslogDetailedInfoClear,
       "gs2310SyslogDetailedInfoTable": gs2310SyslogDetailedInfoTable,
       "gs2310SyslogDetailedInfoEntry": gs2310SyslogDetailedInfoEntry,
       "gs2310SyslogDetailedInfoIndex": gs2310SyslogDetailedInfoIndex,
       "gs2310SyslogDetailedInfoLevel": gs2310SyslogDetailedInfoLevel,
       "gs2310SyslogDetailedInfoTime": gs2310SyslogDetailedInfoTime,
       "gs2310SyslogDetailedInfoMessage": gs2310SyslogDetailedInfoMessage,
       "gs2310Snmp": gs2310Snmp,
       "gs2310SnmpConf": gs2310SnmpConf,
       "gs2310GetCommunityMode": gs2310GetCommunityMode,
       "gs2310GetCommunity": gs2310GetCommunity,
       "gs2310SetCommunityMode": gs2310SetCommunityMode,
       "gs2310SetCommunity": gs2310SetCommunity,
       "gs2310GetCommunityConfTable": gs2310GetCommunityConfTable,
       "gs2310GetCommunityConfEntry": gs2310GetCommunityConfEntry,
       "gs2310CommunityConfIndex": gs2310CommunityConfIndex,
       "gs2310CommunityConfGetCommunity": gs2310CommunityConfGetCommunity,
       "gs2310TrapHostConfTable": gs2310TrapHostConfTable,
       "gs2310TrapHostConfEntry": gs2310TrapHostConfEntry,
       "gs2310TrapHostConfIndex": gs2310TrapHostConfIndex,
       "gs2310TrapHostConfVersion": gs2310TrapHostConfVersion,
       "gs2310TrapHostConfIPType": gs2310TrapHostConfIPType,
       "gs2310TrapHostConfIP": gs2310TrapHostConfIP,
       "gs2310TrapHostConfPort": gs2310TrapHostConfPort,
       "gs2310TrapHostConfCommunity": gs2310TrapHostConfCommunity,
       "gs2310TrapHostConfSeverityLevel": gs2310TrapHostConfSeverityLevel,
       "gs2310TrapHostConfSecurityLevel": gs2310TrapHostConfSecurityLevel,
       "gs2310TrapHostConfAuthPtc": gs2310TrapHostConfAuthPtc,
       "gs2310TrapHostConfAuthPassword": gs2310TrapHostConfAuthPassword,
       "gs2310TrapHostConfPrivPtc": gs2310TrapHostConfPrivPtc,
       "gs2310TrapHostConfPrivPassword": gs2310TrapHostConfPrivPassword,
       "gs2310TrapHostConfCurrentMode": gs2310TrapHostConfCurrentMode,
       "gs2310SnmpSystem": gs2310SnmpSystem,
       "gs2310SnmpState": gs2310SnmpState,
       "gs2310SnmpEngineID": gs2310SnmpEngineID,
       "gs2310SnmpCommunities": gs2310SnmpCommunities,
       "gs2310SnmpCommunitiesCreate": gs2310SnmpCommunitiesCreate,
       "gs2310SnmpCommunitiesTable": gs2310SnmpCommunitiesTable,
       "gs2310SnmpCommunitiesEntry": gs2310SnmpCommunitiesEntry,
       "gs2310SnmpCommunitiesIndex": gs2310SnmpCommunitiesIndex,
       "gs2310SnmpCommunitiesCommunity": gs2310SnmpCommunitiesCommunity,
       "gs2310SnmpCommunitiesUserName": gs2310SnmpCommunitiesUserName,
       "gs2310SnmpCommunitiesSourceIP": gs2310SnmpCommunitiesSourceIP,
       "gs2310SnmpCommunitiesSourceMask": gs2310SnmpCommunitiesSourceMask,
       "gs2310SnmpCommunitiesRowStatus": gs2310SnmpCommunitiesRowStatus,
       "gs2310SnmpUsers": gs2310SnmpUsers,
       "gs2310SnmpUsersCreate": gs2310SnmpUsersCreate,
       "gs2310SnmpUsersTable": gs2310SnmpUsersTable,
       "gs2310SnmpUsersEntry": gs2310SnmpUsersEntry,
       "gs2310SnmpUsersIndex": gs2310SnmpUsersIndex,
       "gs2310SnmpUsersUserName": gs2310SnmpUsersUserName,
       "gs2310SnmpUsersSecurityLevel": gs2310SnmpUsersSecurityLevel,
       "gs2310SnmpUsersAuthenticationProtocol": gs2310SnmpUsersAuthenticationProtocol,
       "gs2310SnmpUsersAuthenticationPassword": gs2310SnmpUsersAuthenticationPassword,
       "gs2310SnmpUsersPrivacyProtocol": gs2310SnmpUsersPrivacyProtocol,
       "gs2310SnmpUsersPrivacyPassword": gs2310SnmpUsersPrivacyPassword,
       "gs2310SnmpUsersRowStatus": gs2310SnmpUsersRowStatus,
       "gs2310SnmpGroups": gs2310SnmpGroups,
       "gs2310SnmpGroupsCreate": gs2310SnmpGroupsCreate,
       "gs2310SnmpGroupsTable": gs2310SnmpGroupsTable,
       "gs2310SnmpGroupsEntry": gs2310SnmpGroupsEntry,
       "gs2310SnmpGroupsIndex": gs2310SnmpGroupsIndex,
       "gs2310SnmpGroupsSecurityModel": gs2310SnmpGroupsSecurityModel,
       "gs2310SnmpGroupsSecurityName": gs2310SnmpGroupsSecurityName,
       "gs2310SnmpGroupsGroupName": gs2310SnmpGroupsGroupName,
       "gs2310SnmpGroupsRowStatus": gs2310SnmpGroupsRowStatus,
       "gs2310SnmpViews": gs2310SnmpViews,
       "gs2310SnmpViewsCreate": gs2310SnmpViewsCreate,
       "gs2310SnmpViewsTable": gs2310SnmpViewsTable,
       "gs2310SnmpViewsEntry": gs2310SnmpViewsEntry,
       "gs2310SnmpViewsIndex": gs2310SnmpViewsIndex,
       "gs2310SnmpViewsName": gs2310SnmpViewsName,
       "gs2310SnmpViewsType": gs2310SnmpViewsType,
       "gs2310SnmpViewsOIDSubtree": gs2310SnmpViewsOIDSubtree,
       "gs2310SnmpViewsRowStatus": gs2310SnmpViewsRowStatus,
       "gs2310SnmpAccess": gs2310SnmpAccess,
       "gs2310SnmpAccessCreate": gs2310SnmpAccessCreate,
       "gs2310SnmpAccessTable": gs2310SnmpAccessTable,
       "gs2310SnmpAccessEntry": gs2310SnmpAccessEntry,
       "gs2310SnmpAccessIndex": gs2310SnmpAccessIndex,
       "gs2310SnmpAccessGroupName": gs2310SnmpAccessGroupName,
       "gs2310SnmpAccessSecurityModel": gs2310SnmpAccessSecurityModel,
       "gs2310SnmpAccessSecurityLevel": gs2310SnmpAccessSecurityLevel,
       "gs2310SnmpAccessReadViewName": gs2310SnmpAccessReadViewName,
       "gs2310SnmpAccessWriteViewName": gs2310SnmpAccessWriteViewName,
       "gs2310SnmpAccessRowStatus": gs2310SnmpAccessRowStatus,
       "gs2310Configuration": gs2310Configuration,
       "gs2310Port": gs2310Port,
       "gs2310PortConfigurationTable": gs2310PortConfigurationTable,
       "gs2310PortConfigurationEntry": gs2310PortConfigurationEntry,
       "gs2310PortConfPort": gs2310PortConfPort,
       "gs2310PortConfPortMedia": gs2310PortConfPortMedia,
       "gs2310PortConfLink": gs2310PortConfLink,
       "gs2310PortConfCurrentSpeed": gs2310PortConfCurrentSpeed,
       "gs2310PortConfSpeed": gs2310PortConfSpeed,
       "gs2310PortConfCurrentFlowControlRx": gs2310PortConfCurrentFlowControlRx,
       "gs2310PortConfCurrentFlowControlTx": gs2310PortConfCurrentFlowControlTx,
       "gs2310PortConfFlowControl": gs2310PortConfFlowControl,
       "gs2310PortConfMaxFrameSize": gs2310PortConfMaxFrameSize,
       "gs2310PortConfExcessiveCollisionMode": gs2310PortConfExcessiveCollisionMode,
       "gs2310PortConfPowerControl": gs2310PortConfPowerControl,
       "gs2310PortConfDescription": gs2310PortConfDescription,
       "gs2310PortTrafficStatisticsTable": gs2310PortTrafficStatisticsTable,
       "gs2310PortTrafficStatisticsEntry": gs2310PortTrafficStatisticsEntry,
       "gs2310PortTrafficStatisticsPort": gs2310PortTrafficStatisticsPort,
       "gs2310PortTrafficStatisticsClear": gs2310PortTrafficStatisticsClear,
       "gs2310PortTrafficRxPackets": gs2310PortTrafficRxPackets,
       "gs2310PortTrafficRxOctets": gs2310PortTrafficRxOctets,
       "gs2310PortTrafficRxUnicast": gs2310PortTrafficRxUnicast,
       "gs2310PortTrafficRxMulticast": gs2310PortTrafficRxMulticast,
       "gs2310PortTrafficRxBroadcast": gs2310PortTrafficRxBroadcast,
       "gs2310PortTrafficRxPause": gs2310PortTrafficRxPause,
       "gs2310PortTrafficRx64Bytes": gs2310PortTrafficRx64Bytes,
       "gs2310PortTrafficRx65to127Bytes": gs2310PortTrafficRx65to127Bytes,
       "gs2310PortTrafficRx128to255Bytes": gs2310PortTrafficRx128to255Bytes,
       "gs2310PortTrafficRx256to511Bytes": gs2310PortTrafficRx256to511Bytes,
       "gs2310PortTrafficRx512to1023Bytes": gs2310PortTrafficRx512to1023Bytes,
       "gs2310PortTrafficRx1024to1526Bytes": gs2310PortTrafficRx1024to1526Bytes,
       "gs2310PortTrafficRxExceecd1527Bytes": gs2310PortTrafficRxExceecd1527Bytes,
       "gs2310PortTrafficRxQ0": gs2310PortTrafficRxQ0,
       "gs2310PortTrafficRxQ1": gs2310PortTrafficRxQ1,
       "gs2310PortTrafficRxQ2": gs2310PortTrafficRxQ2,
       "gs2310PortTrafficRxQ3": gs2310PortTrafficRxQ3,
       "gs2310PortTrafficRxQ4": gs2310PortTrafficRxQ4,
       "gs2310PortTrafficRxQ5": gs2310PortTrafficRxQ5,
       "gs2310PortTrafficRxQ6": gs2310PortTrafficRxQ6,
       "gs2310PortTrafficRxQ7": gs2310PortTrafficRxQ7,
       "gs2310PortTrafficRxDrops": gs2310PortTrafficRxDrops,
       "gs2310PortTrafficRxCRCorAlignment": gs2310PortTrafficRxCRCorAlignment,
       "gs2310PortTrafficRxUndersize": gs2310PortTrafficRxUndersize,
       "gs2310PortTrafficRxOversize": gs2310PortTrafficRxOversize,
       "gs2310PortTrafficRxFragments": gs2310PortTrafficRxFragments,
       "gs2310PortTrafficRxJabber": gs2310PortTrafficRxJabber,
       "gs2310PortTrafficRxFiltered": gs2310PortTrafficRxFiltered,
       "gs2310PortTrafficTxPackets": gs2310PortTrafficTxPackets,
       "gs2310PortTrafficTxOctets": gs2310PortTrafficTxOctets,
       "gs2310PortTrafficTxUnicast": gs2310PortTrafficTxUnicast,
       "gs2310PortTrafficTxMulticast": gs2310PortTrafficTxMulticast,
       "gs2310PortTrafficTxBroadcast": gs2310PortTrafficTxBroadcast,
       "gs2310PortTrafficTxPause": gs2310PortTrafficTxPause,
       "gs2310PortTrafficTx64Bytes": gs2310PortTrafficTx64Bytes,
       "gs2310PortTrafficTx65to127Bytes": gs2310PortTrafficTx65to127Bytes,
       "gs2310PortTrafficTx128to255Bytes": gs2310PortTrafficTx128to255Bytes,
       "gs2310PortTrafficTx256to511Bytes": gs2310PortTrafficTx256to511Bytes,
       "gs2310PortTrafficTx512to1023Bytes": gs2310PortTrafficTx512to1023Bytes,
       "gs2310PortTrafficTx1024to1526Bytes": gs2310PortTrafficTx1024to1526Bytes,
       "gs2310PortTrafficTxExceecd1527Bytes": gs2310PortTrafficTxExceecd1527Bytes,
       "gs2310PortTrafficTxQ0": gs2310PortTrafficTxQ0,
       "gs2310PortTrafficTxQ1": gs2310PortTrafficTxQ1,
       "gs2310PortTrafficTxQ2": gs2310PortTrafficTxQ2,
       "gs2310PortTrafficTxQ3": gs2310PortTrafficTxQ3,
       "gs2310PortTrafficTxQ4": gs2310PortTrafficTxQ4,
       "gs2310PortTrafficTxQ5": gs2310PortTrafficTxQ5,
       "gs2310PortTrafficTxQ6": gs2310PortTrafficTxQ6,
       "gs2310PortTrafficTxQ7": gs2310PortTrafficTxQ7,
       "gs2310PortTrafficTxDrops": gs2310PortTrafficTxDrops,
       "gs2310PortTrafficTxLateOrExcColl": gs2310PortTrafficTxLateOrExcColl,
       "gs2310PortQoSStatistics": gs2310PortQoSStatistics,
       "gs2310PortQoSStatisticsClear": gs2310PortQoSStatisticsClear,
       "gs2310PortQoSStatisticsTable": gs2310PortQoSStatisticsTable,
       "gs2310PortQoSStatisticsEntry": gs2310PortQoSStatisticsEntry,
       "gs2310PortQoSStatisticsPort": gs2310PortQoSStatisticsPort,
       "gs2310PortQoSQ0Rx": gs2310PortQoSQ0Rx,
       "gs2310PortQoSQ0Tx": gs2310PortQoSQ0Tx,
       "gs2310PortQoSQ1Rx": gs2310PortQoSQ1Rx,
       "gs2310PortQoSQ1Tx": gs2310PortQoSQ1Tx,
       "gs2310PortQoSQ2Rx": gs2310PortQoSQ2Rx,
       "gs2310PortQoSQ2Tx": gs2310PortQoSQ2Tx,
       "gs2310PortQoSQ3Rx": gs2310PortQoSQ3Rx,
       "gs2310PortQoSQ3Tx": gs2310PortQoSQ3Tx,
       "gs2310PortQoSQ4Rx": gs2310PortQoSQ4Rx,
       "gs2310PortQoSQ4Tx": gs2310PortQoSQ4Tx,
       "gs2310PortQoSQ5Rx": gs2310PortQoSQ5Rx,
       "gs2310PortQoSQ5Tx": gs2310PortQoSQ5Tx,
       "gs2310PortQoSQ6Rx": gs2310PortQoSQ6Rx,
       "gs2310PortQoSQ6Tx": gs2310PortQoSQ6Tx,
       "gs2310PortQoSQ7Rx": gs2310PortQoSQ7Rx,
       "gs2310PortQoSQ7Tx": gs2310PortQoSQ7Tx,
       "gs2310SFPInfoTable": gs2310SFPInfoTable,
       "gs2310SFPInfoEntry": gs2310SFPInfoEntry,
       "gs2310SFPInfoIndex": gs2310SFPInfoIndex,
       "gs2310SFPInfoPort": gs2310SFPInfoPort,
       "gs2310SFPConnectorType": gs2310SFPConnectorType,
       "gs2310SFPFiberType": gs2310SFPFiberType,
       "gs2310SFPTxCentralWavelength": gs2310SFPTxCentralWavelength,
       "gs2310SFPBaudRate": gs2310SFPBaudRate,
       "gs2310SFPVendorOUI": gs2310SFPVendorOUI,
       "gs2310SFPVendorName": gs2310SFPVendorName,
       "gs2310SFPVendorPN": gs2310SFPVendorPN,
       "gs2310SFPVendorRev": gs2310SFPVendorRev,
       "gs2310SFPVendorSN": gs2310SFPVendorSN,
       "gs2310SFPDateCode": gs2310SFPDateCode,
       "gs2310SFPTemperature": gs2310SFPTemperature,
       "gs2310SFPVcc": gs2310SFPVcc,
       "gs2310SFPMon1Bias": gs2310SFPMon1Bias,
       "gs2310SFPMon2TxPWR": gs2310SFPMon2TxPWR,
       "gs2310SFPMon3RxPWR": gs2310SFPMon3RxPWR,
       "gs2310PortEEETable": gs2310PortEEETable,
       "gs2310PortEEEEntry": gs2310PortEEEEntry,
       "gs2310PortEEEPort": gs2310PortEEEPort,
       "gs2310PortEEEMode": gs2310PortEEEMode,
       "gs2310PortEEEUrgentQueue1": gs2310PortEEEUrgentQueue1,
       "gs2310PortEEEUrgentQueue2": gs2310PortEEEUrgentQueue2,
       "gs2310PortEEEUrgentQueue3": gs2310PortEEEUrgentQueue3,
       "gs2310PortEEEUrgentQueue4": gs2310PortEEEUrgentQueue4,
       "gs2310PortEEEUrgentQueue5": gs2310PortEEEUrgentQueue5,
       "gs2310PortEEEUrgentQueue6": gs2310PortEEEUrgentQueue6,
       "gs2310PortEEEUrgentQueue7": gs2310PortEEEUrgentQueue7,
       "gs2310PortEEEUrgentQueue8": gs2310PortEEEUrgentQueue8,
       "gs2310VoiceVLAN": gs2310VoiceVLAN,
       "gs2310VoiceVLANConf": gs2310VoiceVLANConf,
       "gs2310VoiceVLANMode": gs2310VoiceVLANMode,
       "gs2310VoiceVLANVLANId": gs2310VoiceVLANVLANId,
       "gs2310VoiceVLANAgingTime": gs2310VoiceVLANAgingTime,
       "gs2310VoiceVLANTrafficClass": gs2310VoiceVLANTrafficClass,
       "gs2310VoiceVLANPortTable": gs2310VoiceVLANPortTable,
       "gs2310VoiceVLANPortEntry": gs2310VoiceVLANPortEntry,
       "gs2310VoiceVLANPort": gs2310VoiceVLANPort,
       "gs2310VoiceVLANPortMode": gs2310VoiceVLANPortMode,
       "gs2310VoiceVLANPortSecurity": gs2310VoiceVLANPortSecurity,
       "gs2310VoiceVLANPortDiscoveryProtocol": gs2310VoiceVLANPortDiscoveryProtocol,
       "gs2310VoiceVLANSkipNAS": gs2310VoiceVLANSkipNAS,
       "gs2310VoiceVLANOUI": gs2310VoiceVLANOUI,
       "gs2310VoiceVLANOUICreate": gs2310VoiceVLANOUICreate,
       "gs2310VoiceVLANOUITable": gs2310VoiceVLANOUITable,
       "gs2310VoiceVLANOUIEntry": gs2310VoiceVLANOUIEntry,
       "gs2310VoiceVLANOUIIndex": gs2310VoiceVLANOUIIndex,
       "gs2310VoiceVLANTelephonyOUI": gs2310VoiceVLANTelephonyOUI,
       "gs2310VoiceVLANDescription": gs2310VoiceVLANDescription,
       "gs2310VoiceVLANOUIRowStatus": gs2310VoiceVLANOUIRowStatus,
       "gs2310GARP": gs2310GARP,
       "gs2310GARPConfTable": gs2310GARPConfTable,
       "gs2310GARPConfEntry": gs2310GARPConfEntry,
       "gs2310GARPConfPort": gs2310GARPConfPort,
       "gs2310GARPJoinTimer": gs2310GARPJoinTimer,
       "gs2310GARPLeaveTimer": gs2310GARPLeaveTimer,
       "gs2310GARPLeaveAllTimer": gs2310GARPLeaveAllTimer,
       "gs2310GARPApplicantion": gs2310GARPApplicantion,
       "gs2310GARPAttributeType": gs2310GARPAttributeType,
       "gs2310GARPApplicant": gs2310GARPApplicant,
       "gs2310GARPStatisticsTable": gs2310GARPStatisticsTable,
       "gs2310GARPStatisticsEntry": gs2310GARPStatisticsEntry,
       "gs2310GARPStatisticsPort": gs2310GARPStatisticsPort,
       "gs2310GARPStatisticsPeerMAC": gs2310GARPStatisticsPeerMAC,
       "gs2310GARPStatisticsFailedCount": gs2310GARPStatisticsFailedCount,
       "gs2310GVRP": gs2310GVRP,
       "gs2310GVRPConf": gs2310GVRPConf,
       "gs2310GVRPMode": gs2310GVRPMode,
       "gs2310GVRPConfTable": gs2310GVRPConfTable,
       "gs2310GVRPConfEntry": gs2310GVRPConfEntry,
       "gs2310GVRPConfPort": gs2310GVRPConfPort,
       "gs2310GVRPConfPortMode": gs2310GVRPConfPortMode,
       "gs2310GVRPConfPortRRole": gs2310GVRPConfPortRRole,
       "gs2310GVRPStatisticsTable": gs2310GVRPStatisticsTable,
       "gs2310GVRPStatisticsEntry": gs2310GVRPStatisticsEntry,
       "gs2310GVRPStatisticsPort": gs2310GVRPStatisticsPort,
       "gs2310GVRPStatisticsJoinTxCnt": gs2310GVRPStatisticsJoinTxCnt,
       "gs2310GVRPStatisticsLeaveTxCnt": gs2310GVRPStatisticsLeaveTxCnt,
       "gs2310Mirroring": gs2310Mirroring,
       "gs2310PortToMirrorOn": gs2310PortToMirrorOn,
       "gs2310MirrorTable": gs2310MirrorTable,
       "gs2310MirrorEntry": gs2310MirrorEntry,
       "gs2310MirrorPort": gs2310MirrorPort,
       "gs2310MirrorMode": gs2310MirrorMode,
       "gs2310TrapEventSeverity": gs2310TrapEventSeverity,
       "gs2310TrapEventSeverityACL": gs2310TrapEventSeverityACL,
       "gs2310TrapEventSeverityACLLog": gs2310TrapEventSeverityACLLog,
       "gs2310TrapEventSeverityAccessMgmt": gs2310TrapEventSeverityAccessMgmt,
       "gs2310TrapEventSeverityAuthFailed": gs2310TrapEventSeverityAuthFailed,
       "gs2310TrapEventSeverityColdStart": gs2310TrapEventSeverityColdStart,
       "gs2310TrapEventSeverityConfigInfo": gs2310TrapEventSeverityConfigInfo,
       "gs2310TrapEventSeverityFirmwareUpgrade": gs2310TrapEventSeverityFirmwareUpgrade,
       "gs2310TrapEventSeverityImportExport": gs2310TrapEventSeverityImportExport,
       "gs2310TrapEventSeverityLACP": gs2310TrapEventSeverityLACP,
       "gs2310TrapEventSeverityLinkStatus": gs2310TrapEventSeverityLinkStatus,
       "gs2310TrapEventSeverityLogin": gs2310TrapEventSeverityLogin,
       "gs2310TrapEventSeverityLogout": gs2310TrapEventSeverityLogout,
       "gs2310TrapEventSeverityLoopProtect": gs2310TrapEventSeverityLoopProtect,
       "gs2310TrapEventSeverityMgmtIPChange": gs2310TrapEventSeverityMgmtIPChange,
       "gs2310TrapEventSeverityModuleChange": gs2310TrapEventSeverityModuleChange,
       "gs2310TrapEventSeverityNAS": gs2310TrapEventSeverityNAS,
       "gs2310TrapEventSeverityPasswordChange": gs2310TrapEventSeverityPasswordChange,
       "gs2310TrapEventSeverityPortSecurity": gs2310TrapEventSeverityPortSecurity,
       "gs2310TrapEventSeverityVLAN": gs2310TrapEventSeverityVLAN,
       "gs2310TrapEventSeverityWarmStart": gs2310TrapEventSeverityWarmStart,
       "gs2310TrapEventSeverityARPConflict": gs2310TrapEventSeverityARPConflict,
       "gs2310TrapEventSeveritySpoofingLimit": gs2310TrapEventSeveritySpoofingLimit,
       "gs2310TrapEventSeverityStaticARPConflict": gs2310TrapEventSeverityStaticARPConflict,
       "gs2310SMTP": gs2310SMTP,
       "gs2310SMTPMailServer": gs2310SMTPMailServer,
       "gs2310SMTPUserName": gs2310SMTPUserName,
       "gs2310SMTPPassword": gs2310SMTPPassword,
       "gs2310SMTPServeriryLevel": gs2310SMTPServeriryLevel,
       "gs2310SMTPSender": gs2310SMTPSender,
       "gs2310SMTPReturnPath": gs2310SMTPReturnPath,
       "gs2310SMTPEmailAddress1": gs2310SMTPEmailAddress1,
       "gs2310SMTPEmailAddress2": gs2310SMTPEmailAddress2,
       "gs2310SMTPEmailAddress3": gs2310SMTPEmailAddress3,
       "gs2310SMTPEmailAddress4": gs2310SMTPEmailAddress4,
       "gs2310SMTPEmailAddress5": gs2310SMTPEmailAddress5,
       "gs2310SMTPEmailAddress6": gs2310SMTPEmailAddress6,
       "gs2310ACL": gs2310ACL,
       "gs2310ACLPortsConfTable": gs2310ACLPortsConfTable,
       "gs2310ACLPortsConfEntry": gs2310ACLPortsConfEntry,
       "gs2310ACLPortsConfPort": gs2310ACLPortsConfPort,
       "gs2310ACLPortsConfPolicyID": gs2310ACLPortsConfPolicyID,
       "gs2310ACLPortsConfAction": gs2310ACLPortsConfAction,
       "gs2310ACLPortsConfRateLimiterID": gs2310ACLPortsConfRateLimiterID,
       "gs2310ACLPortsConfPortRedirect": gs2310ACLPortsConfPortRedirect,
       "gs2310ACLPortsConfMirror": gs2310ACLPortsConfMirror,
       "gs2310ACLPortsConfLogging": gs2310ACLPortsConfLogging,
       "gs2310ACLPortsConfShutdown": gs2310ACLPortsConfShutdown,
       "gs2310ACLPortsConfState": gs2310ACLPortsConfState,
       "gs2310ACLPortsConfCounter": gs2310ACLPortsConfCounter,
       "gs2310ACLRateLimiterTable": gs2310ACLRateLimiterTable,
       "gs2310ACLRateLimiterEntry": gs2310ACLRateLimiterEntry,
       "gs2310ACLRateLimiterID": gs2310ACLRateLimiterID,
       "gs2310ACLRateLimiterUnit": gs2310ACLRateLimiterUnit,
       "gs2310ACLRateLimiterRate": gs2310ACLRateLimiterRate,
       "gs2310ACLACE": gs2310ACLACE,
       "gs2310ACLACECreate": gs2310ACLACECreate,
       "gs2310ACLACETable": gs2310ACLACETable,
       "gs2310ACLACEEntry": gs2310ACLACEEntry,
       "gs2310ACLACEIndex": gs2310ACLACEIndex,
       "gs2310ACLACEID": gs2310ACLACEID,
       "gs2310ACLACENextID": gs2310ACLACENextID,
       "gs2310ACLACEIngressPort": gs2310ACLACEIngressPort,
       "gs2310ACLACEPortPolicyNumber": gs2310ACLACEPortPolicyNumber,
       "gs2310ACLACEPortPolicyBitmask": gs2310ACLACEPortPolicyBitmask,
       "gs2310ACLACEFrameType": gs2310ACLACEFrameType,
       "gs2310ACLACEAction": gs2310ACLACEAction,
       "gs2310ACLACEDenyPortRedirect": gs2310ACLACEDenyPortRedirect,
       "gs2310ACLACELogging": gs2310ACLACELogging,
       "gs2310ACLACEMirror": gs2310ACLACEMirror,
       "gs2310ACLACERateLimiter": gs2310ACLACERateLimiter,
       "gs2310ACLACEShutdown": gs2310ACLACEShutdown,
       "gs2310ACLACEVLAN8021QTagged": gs2310ACLACEVLAN8021QTagged,
       "gs2310ACLACEVLANTagPriority": gs2310ACLACEVLANTagPriority,
       "gs2310ACLACEVLANVID": gs2310ACLACEVLANVID,
       "gs2310ACLACEEtherType": gs2310ACLACEEtherType,
       "gs2310ACLACESMAC": gs2310ACLACESMAC,
       "gs2310ACLACEDMACType": gs2310ACLACEDMACType,
       "gs2310ACLACEDMAC": gs2310ACLACEDMAC,
       "gs2310ACLACEArpOpcode": gs2310ACLACEArpOpcode,
       "gs2310ACLACEArpFlagsRequestReply": gs2310ACLACEArpFlagsRequestReply,
       "gs2310ACLACEArpFlagsArpSmac": gs2310ACLACEArpFlagsArpSmac,
       "gs2310ACLACEArpFlagsRarpDmac": gs2310ACLACEArpFlagsRarpDmac,
       "gs2310ACLACEArpFlagsLength": gs2310ACLACEArpFlagsLength,
       "gs2310ACLACEArpFlagsIp": gs2310ACLACEArpFlagsIp,
       "gs2310ACLACEArpFlagsEthernet": gs2310ACLACEArpFlagsEthernet,
       "gs2310ACLACESIPType": gs2310ACLACESIPType,
       "gs2310ACLACESIPIPAddress": gs2310ACLACESIPIPAddress,
       "gs2310ACLACESIPNetworkPrefix": gs2310ACLACESIPNetworkPrefix,
       "gs2310ACLACEDIPType": gs2310ACLACEDIPType,
       "gs2310ACLACEDIPIPAddress": gs2310ACLACEDIPIPAddress,
       "gs2310ACLACEDIPNetworkPrefix": gs2310ACLACEDIPNetworkPrefix,
       "gs2310ACLACEIPProtocol": gs2310ACLACEIPProtocol,
       "gs2310ACLACEIPFlagsTTL": gs2310ACLACEIPFlagsTTL,
       "gs2310ACLACEIPFlagsOptions": gs2310ACLACEIPFlagsOptions,
       "gs2310ACLACEIPFlagsFragment": gs2310ACLACEIPFlagsFragment,
       "gs2310ACLACEICMPType": gs2310ACLACEICMPType,
       "gs2310ACLACEICMPCode": gs2310ACLACEICMPCode,
       "gs2310ACLACESourcePortMin": gs2310ACLACESourcePortMin,
       "gs2310ACLACESourcePortMax": gs2310ACLACESourcePortMax,
       "gs2310ACLACEDestPortMin": gs2310ACLACEDestPortMin,
       "gs2310ACLACEDestPortMax": gs2310ACLACEDestPortMax,
       "gs2310ACLACETCPFlagsFin": gs2310ACLACETCPFlagsFin,
       "gs2310ACLACETCPFlagsSyn": gs2310ACLACETCPFlagsSyn,
       "gs2310ACLACETCPFlagsRst": gs2310ACLACETCPFlagsRst,
       "gs2310ACLACETCPFlagsPsh": gs2310ACLACETCPFlagsPsh,
       "gs2310ACLACETCPFlagsAck": gs2310ACLACETCPFlagsAck,
       "gs2310ACLACETCPFlagsUrg": gs2310ACLACETCPFlagsUrg,
       "gs2310ACLACERowStatus": gs2310ACLACERowStatus,
       "gs2310ACLACEClear": gs2310ACLACEClear,
       "gs2310ACLACEMoveACEID": gs2310ACLACEMoveACEID,
       "gs2310ACLACEMoveNextACEID": gs2310ACLACEMoveNextACEID,
       "gs2310ACLACEStatusTable": gs2310ACLACEStatusTable,
       "gs2310ACLACEStatusEntry": gs2310ACLACEStatusEntry,
       "gs2310ACLACEStatusIndex": gs2310ACLACEStatusIndex,
       "gs2310ACLACEStatusUser": gs2310ACLACEStatusUser,
       "gs2310ACLACEStatusID": gs2310ACLACEStatusID,
       "gs2310ACLACEStatusIngressPort": gs2310ACLACEStatusIngressPort,
       "gs2310ACLACEStatusFrameType": gs2310ACLACEStatusFrameType,
       "gs2310ACLACEStatusAction": gs2310ACLACEStatusAction,
       "gs2310ACLACEStatusRateLimiter": gs2310ACLACEStatusRateLimiter,
       "gs2310ACLACEStatusPortCopy": gs2310ACLACEStatusPortCopy,
       "gs2310ACLACEStatusMirror": gs2310ACLACEStatusMirror,
       "gs2310ACLACEStatusCPU": gs2310ACLACEStatusCPU,
       "gs2310ACLACEStatusCounter": gs2310ACLACEStatusCounter,
       "gs2310ACLACEStatusConflict": gs2310ACLACEStatusConflict,
       "gs2310LoopProtection": gs2310LoopProtection,
       "gs2310LoopProtectionConfig": gs2310LoopProtectionConfig,
       "gs2310LoopProtectionGlobalEnable": gs2310LoopProtectionGlobalEnable,
       "gs2310LoopProtectionTranmisstionTime": gs2310LoopProtectionTranmisstionTime,
       "gs2310LoopProtectionShutdownTime": gs2310LoopProtectionShutdownTime,
       "gs2310LoopProtectionConfigurationTable": gs2310LoopProtectionConfigurationTable,
       "gs2310LoopProtectionConfigurationEntry": gs2310LoopProtectionConfigurationEntry,
       "gs2310LoopProtectionConfPort": gs2310LoopProtectionConfPort,
       "gs2310LoopProtectionConfEnable": gs2310LoopProtectionConfEnable,
       "gs2310LoopProtectionConfAction": gs2310LoopProtectionConfAction,
       "gs2310LoopProtectionConfTxmode": gs2310LoopProtectionConfTxmode,
       "gs2310LoopProtectionStatusTable": gs2310LoopProtectionStatusTable,
       "gs2310LoopProtectionStatusEntry": gs2310LoopProtectionStatusEntry,
       "gs2310LoopProtectionStatusPort": gs2310LoopProtectionStatusPort,
       "gs2310LoopProtectionStatusAction": gs2310LoopProtectionStatusAction,
       "gs2310LoopProtectionStatusTransmit": gs2310LoopProtectionStatusTransmit,
       "gs2310LoopProtectionStatusLoops": gs2310LoopProtectionStatusLoops,
       "gs2310LoopProtectionStatusStatus": gs2310LoopProtectionStatusStatus,
       "gs2310LoopProtectionStatusLoop": gs2310LoopProtectionStatusLoop,
       "gs2310LoopProtectionStatusTimeLastLoop": gs2310LoopProtectionStatusTimeLastLoop,
       "gs2310Qos": gs2310Qos,
       "gs2310QosPortClassification": gs2310QosPortClassification,
       "gs2310QosPortClassificationTable": gs2310QosPortClassificationTable,
       "gs2310QosPortClassificationEntry": gs2310QosPortClassificationEntry,
       "gs2310QosPortClassificationPort": gs2310QosPortClassificationPort,
       "gs2310QosPortClassificationQoSclass": gs2310QosPortClassificationQoSclass,
       "gs2310QosPortClassificationDPlevel": gs2310QosPortClassificationDPlevel,
       "gs2310QosPortClassificationPCP": gs2310QosPortClassificationPCP,
       "gs2310QosPortClassificationDEI": gs2310QosPortClassificationDEI,
       "gs2310QosPortClassificationTagClass": gs2310QosPortClassificationTagClass,
       "gs2310QosPortClassificationDSCPBased": gs2310QosPortClassificationDSCPBased,
       "gs2310QosPortClassificationAddressMode": gs2310QosPortClassificationAddressMode,
       "gs2310QoSIngressPortTagClassificationTable": gs2310QoSIngressPortTagClassificationTable,
       "gs2310QoSIngressPortTagClassificationEntry": gs2310QoSIngressPortTagClassificationEntry,
       "gs2310QoSIngressPortTagClassificationPort": gs2310QoSIngressPortTagClassificationPort,
       "gs2310QoSIngressPortTagPCP": gs2310QoSIngressPortTagPCP,
       "gs2310QoSIngressPortTagDEI": gs2310QoSIngressPortTagDEI,
       "gs2310QoSIngressPortTagQosClass": gs2310QoSIngressPortTagQosClass,
       "gs2310QoSIngressPortTagDPLevel": gs2310QoSIngressPortTagDPLevel,
       "gs2310QosPortPolicingTable": gs2310QosPortPolicingTable,
       "gs2310QosPortPolicingEntry": gs2310QosPortPolicingEntry,
       "gs2310QosPortPolicingPort": gs2310QosPortPolicingPort,
       "gs2310QosPortPolicingMode": gs2310QosPortPolicingMode,
       "gs2310QosPortPolicingRate": gs2310QosPortPolicingRate,
       "gs2310QosPortPolicingUnit": gs2310QosPortPolicingUnit,
       "gs2310QosPortPolicingFlowControl": gs2310QosPortPolicingFlowControl,
       "gs2310QosPortScheduler": gs2310QosPortScheduler,
       "gs2310QosPortSchedulerModeTable": gs2310QosPortSchedulerModeTable,
       "gs2310QosPortSchedulerModeEntry": gs2310QosPortSchedulerModeEntry,
       "gs2310QosSchedulerModePort": gs2310QosSchedulerModePort,
       "gs2310QosSchedulerMode": gs2310QosSchedulerMode,
       "gs2310QosSchedulerShaper": gs2310QosSchedulerShaper,
       "gs2310QosSchedulerShaperRate": gs2310QosSchedulerShaperRate,
       "gs2310QosPortSchedulerTable": gs2310QosPortSchedulerTable,
       "gs2310QosPortSchedulerEntry": gs2310QosPortSchedulerEntry,
       "gs2310QosSchedulerPort": gs2310QosSchedulerPort,
       "gs2310QosSchedulerPortQueue": gs2310QosSchedulerPortQueue,
       "gs2310QosSchedulerPortQueueShaper": gs2310QosSchedulerPortQueueShaper,
       "gs2310QosSchedulerPortQueueShaperRate": gs2310QosSchedulerPortQueueShaperRate,
       "gs2310QosSchedulerPortQueueShaperExcess": gs2310QosSchedulerPortQueueShaperExcess,
       "gs2310QosSchedulerPortQueueSchedulerWeight": gs2310QosSchedulerPortQueueSchedulerWeight,
       "gs2310QosSchedulerPortQueueSchedulerPercent": gs2310QosSchedulerPortQueueSchedulerPercent,
       "gs2310QosPortEgressTagRemarking": gs2310QosPortEgressTagRemarking,
       "gs2310QosPortEgressTagRemarkingTable": gs2310QosPortEgressTagRemarkingTable,
       "gs2310QosPortEgressTagRemarkingEntry": gs2310QosPortEgressTagRemarkingEntry,
       "gs2310QosEgressTagRemarkingPort": gs2310QosEgressTagRemarkingPort,
       "gs2310QosEgressTagRemarkingMode": gs2310QosEgressTagRemarkingMode,
       "gs2310QosPortEgressTagRemarkingDefTable": gs2310QosPortEgressTagRemarkingDefTable,
       "gs2310QosPortEgressTagRemarkingDefEntry": gs2310QosPortEgressTagRemarkingDefEntry,
       "gs2310QosEgressTagRemarkingDefPort": gs2310QosEgressTagRemarkingDefPort,
       "gs2310QosEgressTagRemarkingDefPCP": gs2310QosEgressTagRemarkingDefPCP,
       "gs2310QosEgressTagRemarkingDefDEI": gs2310QosEgressTagRemarkingDefDEI,
       "gs2310QosPortEgressTagRemarkingMapTable": gs2310QosPortEgressTagRemarkingMapTable,
       "gs2310QosPortEgressTagRemarkingMapEntry": gs2310QosPortEgressTagRemarkingMapEntry,
       "gs2310QosPortEgressTagRemarkingMapPort": gs2310QosPortEgressTagRemarkingMapPort,
       "gs2310QosTagRemarkingQoSClass": gs2310QosTagRemarkingQoSClass,
       "gs2310QosTagRemarkingDPLevel": gs2310QosTagRemarkingDPLevel,
       "gs2310QosTagRemarkingPCP": gs2310QosTagRemarkingPCP,
       "gs2310QosTagRemarkingDEI": gs2310QosTagRemarkingDEI,
       "gs2310QosPortDSCPTable": gs2310QosPortDSCPTable,
       "gs2310QosPortDSCPEntry": gs2310QosPortDSCPEntry,
       "gs2310QosPortDSCPPort": gs2310QosPortDSCPPort,
       "gs2310QosPortDSCPIngressTranslate": gs2310QosPortDSCPIngressTranslate,
       "gs2310QosPortDSCPIngressClassify": gs2310QosPortDSCPIngressClassify,
       "gs2310QosPortDSCPEgressRewrite": gs2310QosPortDSCPEgressRewrite,
       "gs2310QosDSCPTable": gs2310QosDSCPTable,
       "gs2310QosDSCPEntry": gs2310QosDSCPEntry,
       "gs2310QosDSCPList": gs2310QosDSCPList,
       "gs2310QosDSCP": gs2310QosDSCP,
       "gs2310QosDSCPTrust": gs2310QosDSCPTrust,
       "gs2310QosDSCPQosClass": gs2310QosDSCPQosClass,
       "gs2310QosDSCPDPL": gs2310QosDSCPDPL,
       "gs2310QosDSCPTranslationTable": gs2310QosDSCPTranslationTable,
       "gs2310QosDSCPTranslationEntry": gs2310QosDSCPTranslationEntry,
       "gs2310QosDSCPTranslationList": gs2310QosDSCPTranslationList,
       "gs2310QosDSCPTranslationDSCPBasedId": gs2310QosDSCPTranslationDSCPBasedId,
       "gs2310QosDSCPTranslationIngressTranslate": gs2310QosDSCPTranslationIngressTranslate,
       "gs2310QosDSCPTranslationIngressClassify": gs2310QosDSCPTranslationIngressClassify,
       "gs2310QosDSCPTranslationEgressRemapDP0": gs2310QosDSCPTranslationEgressRemapDP0,
       "gs2310QosDSCPTranslationEgressRemapDP1": gs2310QosDSCPTranslationEgressRemapDP1,
       "gs2310QosDSCPClassificationTable": gs2310QosDSCPClassificationTable,
       "gs2310QosDSCPClassificationEntry": gs2310QosDSCPClassificationEntry,
       "gs2310QosDSCPClassificationQoSClass": gs2310QosDSCPClassificationQoSClass,
       "gs2310QosDSCPClassificationDPL": gs2310QosDSCPClassificationDPL,
       "gs2310QosDSCPClassificationDSCP": gs2310QosDSCPClassificationDSCP,
       "gs2310QosControlList": gs2310QosControlList,
       "gs2310QosQceCreate": gs2310QosQceCreate,
       "gs2310QosQceTable": gs2310QosQceTable,
       "gs2310QosQceEntry": gs2310QosQceEntry,
       "gs2310QosQceIndex": gs2310QosQceIndex,
       "gs2310QosQceID": gs2310QosQceID,
       "gs2310QosQceNextID": gs2310QosQceNextID,
       "gs2310QosQcePortMembers": gs2310QosQcePortMembers,
       "gs2310QosQceTag": gs2310QosQceTag,
       "gs2310QosQceVID": gs2310QosQceVID,
       "gs2310QosPCP": gs2310QosPCP,
       "gs2310QosDEI": gs2310QosDEI,
       "gs2310QosSMAC": gs2310QosSMAC,
       "gs2310QosDMACType": gs2310QosDMACType,
       "gs2310QosFrameType": gs2310QosFrameType,
       "gs2310QosMacEtherType": gs2310QosMacEtherType,
       "gs2310QosLLCSSAPAddr": gs2310QosLLCSSAPAddr,
       "gs2310QosLLCDSAPAddr": gs2310QosLLCDSAPAddr,
       "gs2310QosLLCControl": gs2310QosLLCControl,
       "gs2310QosSNAPPID": gs2310QosSNAPPID,
       "gs2310QosIpv4Protocol": gs2310QosIpv4Protocol,
       "gs2310QosIpv4ProtocolValue": gs2310QosIpv4ProtocolValue,
       "gs2310QosIpv4ProtocolUDPSport": gs2310QosIpv4ProtocolUDPSport,
       "gs2310QosIpv4ProtocolUDPDport": gs2310QosIpv4ProtocolUDPDport,
       "gs2310QosIpv4ProtocolTCPSport": gs2310QosIpv4ProtocolTCPSport,
       "gs2310QosIpv4ProtocolTCPDport": gs2310QosIpv4ProtocolTCPDport,
       "gs2310QosIpv4Ip": gs2310QosIpv4Ip,
       "gs2310QosIpv4Mask": gs2310QosIpv4Mask,
       "gs2310QosIpv4IPFragment": gs2310QosIpv4IPFragment,
       "gs2310QosIpv4DSCP": gs2310QosIpv4DSCP,
       "gs2310QosIpv6Protocol": gs2310QosIpv6Protocol,
       "gs2310QosIpv6ProtocolValue": gs2310QosIpv6ProtocolValue,
       "gs2310QosIpv6ProtocolUDPSport": gs2310QosIpv6ProtocolUDPSport,
       "gs2310QosIpv6ProtocolUDPDport": gs2310QosIpv6ProtocolUDPDport,
       "gs2310QosIpv6ProtocolTCPSport": gs2310QosIpv6ProtocolTCPSport,
       "gs2310QosIpv6ProtocolTCPDport": gs2310QosIpv6ProtocolTCPDport,
       "gs2310QosIpv6Ip": gs2310QosIpv6Ip,
       "gs2310QosIpv6Mask": gs2310QosIpv6Mask,
       "gs2310QosIpv6DSCP": gs2310QosIpv6DSCP,
       "gs2310QosActionClass": gs2310QosActionClass,
       "gs2310QosActionDPL": gs2310QosActionDPL,
       "gs2310QosActionDSCP": gs2310QosActionDSCP,
       "gs2310QosQceRowStatus": gs2310QosQceRowStatus,
       "gs2310QosQceMoveID": gs2310QosQceMoveID,
       "gs2310QosQceMoveNextID": gs2310QosQceMoveNextID,
       "gs2310QosQCLStatusTable": gs2310QosQCLStatusTable,
       "gs2310QosQCLStatusEntry": gs2310QosQCLStatusEntry,
       "gs2310QosQCLStatusList": gs2310QosQCLStatusList,
       "gs2310QosQCLStatusUser": gs2310QosQCLStatusUser,
       "gs2310QosQCLStatusQCEId": gs2310QosQCLStatusQCEId,
       "gs2310QosQCLStatusFrameType": gs2310QosQCLStatusFrameType,
       "gs2310QosQCLStatusPortlist": gs2310QosQCLStatusPortlist,
       "gs2310QosQCLStatusActionClass": gs2310QosQCLStatusActionClass,
       "gs2310QosQCLStatusActionDPL": gs2310QosQCLStatusActionDPL,
       "gs2310QosQCLStatusActionDSCP": gs2310QosQCLStatusActionDSCP,
       "gs2310QosQCLStatusActionConflict": gs2310QosQCLStatusActionConflict,
       "gs2310QosStormControl": gs2310QosStormControl,
       "gs2310QoSStormControlUC": gs2310QoSStormControlUC,
       "gs2310QoSStormControlUCRate": gs2310QoSStormControlUCRate,
       "gs2310QoSStormControlMC": gs2310QoSStormControlMC,
       "gs2310QoSStormControlMCRate": gs2310QoSStormControlMCRate,
       "gs2310QoSStormControlBC": gs2310QoSStormControlBC,
       "gs2310QoSStormControlBCRate": gs2310QoSStormControlBCRate,
       "gs2310Vlan": gs2310Vlan,
       "gs2310VlanPorts": gs2310VlanPorts,
       "gs2310VlanPortsTPIDforCustomSport": gs2310VlanPortsTPIDforCustomSport,
       "gs2310VlanPortsTable": gs2310VlanPortsTable,
       "gs2310VlanPortsEntry": gs2310VlanPortsEntry,
       "gs2310VlanPortsPort": gs2310VlanPortsPort,
       "gs2310VlanPortsPVID": gs2310VlanPortsPVID,
       "gs2310VlanPortsFrameType": gs2310VlanPortsFrameType,
       "gs2310VlanPortsIngressFilter": gs2310VlanPortsIngressFilter,
       "gs2310VlanPortsEgressRule": gs2310VlanPortsEgressRule,
       "gs2310VlanPortsPortType": gs2310VlanPortsPortType,
       "gs2310VlanPrivateVLAN": gs2310VlanPrivateVLAN,
       "gs2310VlanPrivateVLANMembership": gs2310VlanPrivateVLANMembership,
       "gs2310VlanPrivateVLANMembershipCreate": gs2310VlanPrivateVLANMembershipCreate,
       "gs2310VlanPrivateVLANMembershipTable": gs2310VlanPrivateVLANMembershipTable,
       "gs2310VlanPrivateVLANMembershipEntry": gs2310VlanPrivateVLANMembershipEntry,
       "gs2310VlanPrivateVLANIndex": gs2310VlanPrivateVLANIndex,
       "gs2310VlanPrivateVLANID": gs2310VlanPrivateVLANID,
       "gs2310VlanPrivateVLANMemberships": gs2310VlanPrivateVLANMemberships,
       "gs2310VlanPrivateVLANRowStatus": gs2310VlanPrivateVLANRowStatus,
       "gs2310VlanPortIsolationTable": gs2310VlanPortIsolationTable,
       "gs2310VlanPortIsolationEntry": gs2310VlanPortIsolationEntry,
       "gs2310VlanPortIsolationPort": gs2310VlanPortIsolationPort,
       "gs2310VlanPortIsolation": gs2310VlanPortIsolation,
       "gs2310MACbasedVLAN": gs2310MACbasedVLAN,
       "gs2310MACbasedVLANConf": gs2310MACbasedVLANConf,
       "gs2310MACbasedVLANConfCreate": gs2310MACbasedVLANConfCreate,
       "gs2310MACbasedVLANConfTable": gs2310MACbasedVLANConfTable,
       "gs2310MACbasedVLANConfEntry": gs2310MACbasedVLANConfEntry,
       "gs2310MACbasedVLANIndex": gs2310MACbasedVLANIndex,
       "gs2310MACbasedVLANMACAddress": gs2310MACbasedVLANMACAddress,
       "gs2310MACbasedVLANID": gs2310MACbasedVLANID,
       "gs2310MACbasedMemberships": gs2310MACbasedMemberships,
       "gs2310MACbaseRowStatus": gs2310MACbaseRowStatus,
       "gs2310IGMPSnooping": gs2310IGMPSnooping,
       "gs2310IGMPSnoopingBasic": gs2310IGMPSnoopingBasic,
       "gs2310IGMPSnoopingEnable": gs2310IGMPSnoopingEnable,
       "gs2310IGMPSnoopingUnregisteredIPMCv4Flooding": gs2310IGMPSnoopingUnregisteredIPMCv4Flooding,
       "gs2310IGMPSnoopingSSMIPRangeAddr": gs2310IGMPSnoopingSSMIPRangeAddr,
       "gs2310IGMPSnoopingSSMIPRangeValue": gs2310IGMPSnoopingSSMIPRangeValue,
       "gs2310IGMPSnoopingProxyEnabled": gs2310IGMPSnoopingProxyEnabled,
       "gs2310IGMPSnoopingPortRelatedTable": gs2310IGMPSnoopingPortRelatedTable,
       "gs2310IGMPSnoopingPortRelatedEntry": gs2310IGMPSnoopingPortRelatedEntry,
       "gs2310IGMPSnoopingRouterPort": gs2310IGMPSnoopingRouterPort,
       "gs2310IGMPSnoopingFastLeave": gs2310IGMPSnoopingFastLeave,
       "gs2310IGMPSnoopingThrottling": gs2310IGMPSnoopingThrottling,
       "gs2310IGMPSnoopingVLANTable": gs2310IGMPSnoopingVLANTable,
       "gs2310IGMPSnoopingVLANEntry": gs2310IGMPSnoopingVLANEntry,
       "gs2310IGMPSnoopingVLANID": gs2310IGMPSnoopingVLANID,
       "gs2310IGMPSnoopingVLANEnable": gs2310IGMPSnoopingVLANEnable,
       "gs2310IGMPSnoopingVLANIGMPQuerier": gs2310IGMPSnoopingVLANIGMPQuerier,
       "gs2310IGMPSnoopingVLANCompatibility": gs2310IGMPSnoopingVLANCompatibility,
       "gs2310IGMPSnoopingVLANRV": gs2310IGMPSnoopingVLANRV,
       "gs2310IGMPSnoopingVLANQI": gs2310IGMPSnoopingVLANQI,
       "gs2310IGMPSnoopingVLANQRI": gs2310IGMPSnoopingVLANQRI,
       "gs2310IGMPSnoopingVLANLLQI": gs2310IGMPSnoopingVLANLLQI,
       "gs2310IGMPSnoopingVLANURI": gs2310IGMPSnoopingVLANURI,
       "gs2310IGMPSnoopingPortGroupFiltering": gs2310IGMPSnoopingPortGroupFiltering,
       "gs2310IGMPSnoopingPortGroupFilteringCreate": gs2310IGMPSnoopingPortGroupFilteringCreate,
       "gs2310IGMPSnoopingPortGroupFilteringTable": gs2310IGMPSnoopingPortGroupFilteringTable,
       "gs2310IGMPSnoopingPortGroupFilteringEntry": gs2310IGMPSnoopingPortGroupFilteringEntry,
       "gs2310IGMPSnoopingPortGroupFilteringIndex": gs2310IGMPSnoopingPortGroupFilteringIndex,
       "gs2310IGMPSnoopingPortGroupFilteringPort": gs2310IGMPSnoopingPortGroupFilteringPort,
       "gs2310IGMPSnoopingPortGroupFilteringGroups": gs2310IGMPSnoopingPortGroupFilteringGroups,
       "gs2310IGMPSnoopingPortGroupFilteringRowStatus": gs2310IGMPSnoopingPortGroupFilteringRowStatus,
       "gs2310IGMPSnoopingStatus": gs2310IGMPSnoopingStatus,
       "gs2310IGMPSnoopingstatisticClear": gs2310IGMPSnoopingstatisticClear,
       "gs2310IGMPSnoopingstatisticTable": gs2310IGMPSnoopingstatisticTable,
       "gs2310IGMPSnoopingstatisticEntry": gs2310IGMPSnoopingstatisticEntry,
       "gs2310IGMPSnoopingstatisticVLANID": gs2310IGMPSnoopingstatisticVLANID,
       "gs2310IGMPSnoopingstatisticQuerierVersion": gs2310IGMPSnoopingstatisticQuerierVersion,
       "gs2310IGMPSnoopingstatisticHostVersion": gs2310IGMPSnoopingstatisticHostVersion,
       "gs2310IGMPSnoopingstatisticQuerierStatus": gs2310IGMPSnoopingstatisticQuerierStatus,
       "gs2310IGMPSnoopingstatisticQueriesTransmitted": gs2310IGMPSnoopingstatisticQueriesTransmitted,
       "gs2310IGMPSnoopingstatisticQueriesReceived": gs2310IGMPSnoopingstatisticQueriesReceived,
       "gs2310IGMPSnoopingstatisticV1ReportsReceived": gs2310IGMPSnoopingstatisticV1ReportsReceived,
       "gs2310IGMPSnoopingstatisticV2ReportsReceived": gs2310IGMPSnoopingstatisticV2ReportsReceived,
       "gs2310IGMPSnoopingstatisticV3ReportsReceived": gs2310IGMPSnoopingstatisticV3ReportsReceived,
       "gs2310IGMPSnoopingstatisticV2LeavesReceived": gs2310IGMPSnoopingstatisticV2LeavesReceived,
       "gs2310IGMPSnoopingRouterPortTable": gs2310IGMPSnoopingRouterPortTable,
       "gs2310IGMPSnoopingRouterPortEntry": gs2310IGMPSnoopingRouterPortEntry,
       "gs2310IGMPSnoopingRouterPortStatus": gs2310IGMPSnoopingRouterPortStatus,
       "gs2310IGMPSnoopingGroupsTable": gs2310IGMPSnoopingGroupsTable,
       "gs2310IGMPSnoopingGroupsEntry": gs2310IGMPSnoopingGroupsEntry,
       "gs2310IGMPSnoopingGroupsIndex": gs2310IGMPSnoopingGroupsIndex,
       "gs2310IGMPSnoopingGroupsVLANID": gs2310IGMPSnoopingGroupsVLANID,
       "gs2310IGMPSnoopingGroups": gs2310IGMPSnoopingGroups,
       "gs2310IGMPSnoopingGroupsMemberships": gs2310IGMPSnoopingGroupsMemberships,
       "gs2310IGMPSnoopingSSMTable": gs2310IGMPSnoopingSSMTable,
       "gs2310IGMPSnoopingSSMEntry": gs2310IGMPSnoopingSSMEntry,
       "gs2310IGMPSnoopingSSMIndex": gs2310IGMPSnoopingSSMIndex,
       "gs2310IGMPSnoopingSSMVLANID": gs2310IGMPSnoopingSSMVLANID,
       "gs2310IGMPSnoopingSSMGroup": gs2310IGMPSnoopingSSMGroup,
       "gs2310IGMPSnoopingSSMPort": gs2310IGMPSnoopingSSMPort,
       "gs2310IGMPSnoopingSSMMode": gs2310IGMPSnoopingSSMMode,
       "gs2310IGMPSnoopingSSMSourceAddress": gs2310IGMPSnoopingSSMSourceAddress,
       "gs2310IGMPSnoopingSSMType": gs2310IGMPSnoopingSSMType,
       "gs2310MLDSnooping": gs2310MLDSnooping,
       "gs2310MLDSnoopingBasic": gs2310MLDSnoopingBasic,
       "gs2310MLDSnoopingEnable": gs2310MLDSnoopingEnable,
       "gs2310MLDSnoopingUnregisteredIPMCv6Flooding": gs2310MLDSnoopingUnregisteredIPMCv6Flooding,
       "gs2310MLDSnoopingSSMIPRangeAddr": gs2310MLDSnoopingSSMIPRangeAddr,
       "gs2310MLDSnoopingSSMIPRangeValue": gs2310MLDSnoopingSSMIPRangeValue,
       "gs2310MLDSnoopingProxyEnabled": gs2310MLDSnoopingProxyEnabled,
       "gs2310MLDSnoopingPortRelatedTable": gs2310MLDSnoopingPortRelatedTable,
       "gs2310MLDSnoopingPortRelatedEntry": gs2310MLDSnoopingPortRelatedEntry,
       "gs2310MLDSnoopingRouterPort": gs2310MLDSnoopingRouterPort,
       "gs2310MLDSnoopingFastLeave": gs2310MLDSnoopingFastLeave,
       "gs2310MLDSnoopingThrottling": gs2310MLDSnoopingThrottling,
       "gs2310MLDSnoopingVLANTable": gs2310MLDSnoopingVLANTable,
       "gs2310MLDSnoopingVLANEntry": gs2310MLDSnoopingVLANEntry,
       "gs2310MLDSnoopingVLANID": gs2310MLDSnoopingVLANID,
       "gs2310MLDSnoopingVLANEnable": gs2310MLDSnoopingVLANEnable,
       "gs2310MLDSnoopingVLANIGMPQuerier": gs2310MLDSnoopingVLANIGMPQuerier,
       "gs2310MLDSnoopingVLANCompatibility": gs2310MLDSnoopingVLANCompatibility,
       "gs2310MLDSnoopingVLANRV": gs2310MLDSnoopingVLANRV,
       "gs2310MLDSnoopingVLANQI": gs2310MLDSnoopingVLANQI,
       "gs2310MLDSnoopingVLANQRI": gs2310MLDSnoopingVLANQRI,
       "gs2310MLDSnoopingVLANLLQI": gs2310MLDSnoopingVLANLLQI,
       "gs2310MLDSnoopingVLANURI": gs2310MLDSnoopingVLANURI,
       "gs2310MLDSnoopingPortGroupFiltering": gs2310MLDSnoopingPortGroupFiltering,
       "gs2310MLDSnoopingPortGroupFilteringCreate": gs2310MLDSnoopingPortGroupFilteringCreate,
       "gs2310MLDSnoopingPortGroupFilteringTable": gs2310MLDSnoopingPortGroupFilteringTable,
       "gs2310MLDSnoopingPortGroupFilteringEntry": gs2310MLDSnoopingPortGroupFilteringEntry,
       "gs2310MLDSnoopingPortGroupFilteringIndex": gs2310MLDSnoopingPortGroupFilteringIndex,
       "gs2310MLDSnoopingPortGroupFilteringPort": gs2310MLDSnoopingPortGroupFilteringPort,
       "gs2310MLDSnoopingPortGroupFilteringGroups": gs2310MLDSnoopingPortGroupFilteringGroups,
       "gs2310MLDSnoopingPortGroupFilteringRowStatus": gs2310MLDSnoopingPortGroupFilteringRowStatus,
       "gs2310MLDSnoopingStatus": gs2310MLDSnoopingStatus,
       "gs2310MLDSnoopingstatisticClear": gs2310MLDSnoopingstatisticClear,
       "gs2310MLDSnoopingstatisticTable": gs2310MLDSnoopingstatisticTable,
       "gs2310MLDSnoopingstatisticEntry": gs2310MLDSnoopingstatisticEntry,
       "gs2310MLDSnoopingstatisticVLANID": gs2310MLDSnoopingstatisticVLANID,
       "gs2310MLDSnoopingstatisticQuerierVersion": gs2310MLDSnoopingstatisticQuerierVersion,
       "gs2310MLDSnoopingstatisticHostVersion": gs2310MLDSnoopingstatisticHostVersion,
       "gs2310MLDSnoopingstatisticQuerierStatus": gs2310MLDSnoopingstatisticQuerierStatus,
       "gs2310MLDSnoopingstatisticQueriesTransmitted": gs2310MLDSnoopingstatisticQueriesTransmitted,
       "gs2310MLDSnoopingstatisticQueriesReceived": gs2310MLDSnoopingstatisticQueriesReceived,
       "gs2310MLDSnoopingstatisticV1ReportsReceived": gs2310MLDSnoopingstatisticV1ReportsReceived,
       "gs2310MLDSnoopingstatisticV2ReportsReceived": gs2310MLDSnoopingstatisticV2ReportsReceived,
       "gs2310MLDSnoopingstatisticV1LeavesReceived": gs2310MLDSnoopingstatisticV1LeavesReceived,
       "gs2310MLDSnoopingRouterPortTable": gs2310MLDSnoopingRouterPortTable,
       "gs2310MLDSnoopingRouterPortEntry": gs2310MLDSnoopingRouterPortEntry,
       "gs2310MLDSnoopingRouterPortStatus": gs2310MLDSnoopingRouterPortStatus,
       "gs2310MLDSnoopingGroupsTable": gs2310MLDSnoopingGroupsTable,
       "gs2310MLDSnoopingGroupsEntry": gs2310MLDSnoopingGroupsEntry,
       "gs2310MLDSnoopingGroupsIndex": gs2310MLDSnoopingGroupsIndex,
       "gs2310MLDSnoopingGroupsVLANID": gs2310MLDSnoopingGroupsVLANID,
       "gs2310MLDSnoopingGroups": gs2310MLDSnoopingGroups,
       "gs2310MLDSnoopingGroupsMemberships": gs2310MLDSnoopingGroupsMemberships,
       "gs2310MLDSnoopingSSMTable": gs2310MLDSnoopingSSMTable,
       "gs2310MLDSnoopingSSMEntry": gs2310MLDSnoopingSSMEntry,
       "gs2310MLDSnoopingSSMIndex": gs2310MLDSnoopingSSMIndex,
       "gs2310MLDSnoopingSSMVLANID": gs2310MLDSnoopingSSMVLANID,
       "gs2310MLDSnoopingSSMGroup": gs2310MLDSnoopingSSMGroup,
       "gs2310MLDSnoopingSSMPort": gs2310MLDSnoopingSSMPort,
       "gs2310MLDSnoopingSSMMode": gs2310MLDSnoopingSSMMode,
       "gs2310MLDSnoopingSSMSourceAddress": gs2310MLDSnoopingSSMSourceAddress,
       "gs2310MLDSnoopingSSMType": gs2310MLDSnoopingSSMType,
       "gs2310MVR": gs2310MVR,
       "gs2310MVRConfiguration": gs2310MVRConfiguration,
       "gs2310MVRMode": gs2310MVRMode,
       "gs2310MVRVLANId": gs2310MVRVLANId,
       "gs2310MVRPortConfigurationTable": gs2310MVRPortConfigurationTable,
       "gs2310MVRPortConfigurationEntry": gs2310MVRPortConfigurationEntry,
       "gs2310MVRPortConfigurationMode": gs2310MVRPortConfigurationMode,
       "gs2310MVRPortConfigurationType": gs2310MVRPortConfigurationType,
       "gs2310MVRPortConfigurationImmediateLeave": gs2310MVRPortConfigurationImmediateLeave,
       "gs2310MVRPortGroupFiltering": gs2310MVRPortGroupFiltering,
       "gs2310MVRPortGroupFilteringCreate": gs2310MVRPortGroupFilteringCreate,
       "gs2310MVRPortGroupFilteringTable": gs2310MVRPortGroupFilteringTable,
       "gs2310MVRPortGroupFilteringEntry": gs2310MVRPortGroupFilteringEntry,
       "gs2310MVRPortGroupFilteringIndex": gs2310MVRPortGroupFilteringIndex,
       "gs2310MVRPortGroupFilteringPort": gs2310MVRPortGroupFilteringPort,
       "gs2310MVRPortGroupFilteringStartGroups": gs2310MVRPortGroupFilteringStartGroups,
       "gs2310MVRPortGroupFilteringEndGroups": gs2310MVRPortGroupFilteringEndGroups,
       "gs2310MVRPortGroupFilteringRowStatus": gs2310MVRPortGroupFilteringRowStatus,
       "gs2310MVRGroupsTable": gs2310MVRGroupsTable,
       "gs2310MVRGroupsEntry": gs2310MVRGroupsEntry,
       "gs2310MVRGroupsIndex": gs2310MVRGroupsIndex,
       "gs2310MVRGroupsVLANID": gs2310MVRGroupsVLANID,
       "gs2310MVRGroups": gs2310MVRGroups,
       "gs2310MVRGroupsMemberships": gs2310MVRGroupsMemberships,
       "gs2310MVRStatus": gs2310MVRStatus,
       "gs2310MVRstatisticClear": gs2310MVRstatisticClear,
       "gs2310MVRstatisticVLANID": gs2310MVRstatisticVLANID,
       "gs2310MVRstatisticV1ReportsReceived": gs2310MVRstatisticV1ReportsReceived,
       "gs2310MVRstatisticV2ReportsReceived": gs2310MVRstatisticV2ReportsReceived,
       "gs2310MVRstatisticV3ReportsReceived": gs2310MVRstatisticV3ReportsReceived,
       "gs2310MVRstatisticV2LeavesReceived": gs2310MVRstatisticV2LeavesReceived,
       "gs2310LACP": gs2310LACP,
       "gs2310LACPConf": gs2310LACPConf,
       "gs2310LACPPortConfigurationTable": gs2310LACPPortConfigurationTable,
       "gs2310LACPPortConfigurationEntry": gs2310LACPPortConfigurationEntry,
       "gs2310LACPPortConfigurationPort": gs2310LACPPortConfigurationPort,
       "gs2310LACPPortConfigurationMode": gs2310LACPPortConfigurationMode,
       "gs2310LACPPortConfigurationKey": gs2310LACPPortConfigurationKey,
       "gs2310LACPPortConfigurationRole": gs2310LACPPortConfigurationRole,
       "gs2310LACPSystemStatusTable": gs2310LACPSystemStatusTable,
       "gs2310LACPSystemStatusEntry": gs2310LACPSystemStatusEntry,
       "gs2310LACPSystemStatusIndex": gs2310LACPSystemStatusIndex,
       "gs2310LACPSystemStatusAggrID": gs2310LACPSystemStatusAggrID,
       "gs2310LACPSystemStatusPartnerSystemID": gs2310LACPSystemStatusPartnerSystemID,
       "gs2310LACPSystemStatusPartnerKey": gs2310LACPSystemStatusPartnerKey,
       "gs2310LACPSystemStatusLastchanged": gs2310LACPSystemStatusLastchanged,
       "gs2310LACPSystemStatusLocalPorts": gs2310LACPSystemStatusLocalPorts,
       "gs2310LACPStatusTable": gs2310LACPStatusTable,
       "gs2310LACPStatusEntry": gs2310LACPStatusEntry,
       "gs2310LACPStatusPort": gs2310LACPStatusPort,
       "gs2310LACPStatusLACP": gs2310LACPStatusLACP,
       "gs2310LACPStatusKey": gs2310LACPStatusKey,
       "gs2310LACPStatusAggrID": gs2310LACPStatusAggrID,
       "gs2310LACPStatusPartnerSystemID": gs2310LACPStatusPartnerSystemID,
       "gs2310LACPStatusPartnerPort": gs2310LACPStatusPartnerPort,
       "gs2310LACPStatisticsTable": gs2310LACPStatisticsTable,
       "gs2310LACPStatisticsEntry": gs2310LACPStatisticsEntry,
       "gs2310LACPStatisticsPort": gs2310LACPStatisticsPort,
       "gs2310LACPReceived": gs2310LACPReceived,
       "gs2310LACPTransmitted": gs2310LACPTransmitted,
       "gs2310LACPDiscardedUnknown": gs2310LACPDiscardedUnknown,
       "gs2310LACPDiscardedIllegal": gs2310LACPDiscardedIllegal,
       "gs2310LACPStatisticsClear": gs2310LACPStatisticsClear,
       "gs2310STP": gs2310STP,
       "gs2310STPBridgeBasicConf": gs2310STPBridgeBasicConf,
       "gs2310STPBridgeProtocolVersion": gs2310STPBridgeProtocolVersion,
       "gs2310STPBridgePriority": gs2310STPBridgePriority,
       "gs2310STPBridgeForwardDelay": gs2310STPBridgeForwardDelay,
       "gs2310STPBridgeMaxAge": gs2310STPBridgeMaxAge,
       "gs2310STPBridgeMaximumHopCount": gs2310STPBridgeMaximumHopCount,
       "gs2310STPBridgeTransmitHoldCount": gs2310STPBridgeTransmitHoldCount,
       "gs2310STPBridgeAdvancedConf": gs2310STPBridgeAdvancedConf,
       "gs2310STPBridgeEdgePortBPDUFiltering": gs2310STPBridgeEdgePortBPDUFiltering,
       "gs2310STPBridgeEdgePortBPDUGuard": gs2310STPBridgeEdgePortBPDUGuard,
       "gs2310STPBridgePortErrorRecoveryTimeout": gs2310STPBridgePortErrorRecoveryTimeout,
       "gs2310STPMSTIConf": gs2310STPMSTIConf,
       "gs2310STPMSTIConfigurationName": gs2310STPMSTIConfigurationName,
       "gs2310STPMSTIConfigurationRevision": gs2310STPMSTIConfigurationRevision,
       "gs2310STPMSTIMappingConf": gs2310STPMSTIMappingConf,
       "gs2310STPMSTI1VLANsMapped": gs2310STPMSTI1VLANsMapped,
       "gs2310STPMSTI2VLANsMapped": gs2310STPMSTI2VLANsMapped,
       "gs2310STPMSTI3VLANsMapped": gs2310STPMSTI3VLANsMapped,
       "gs2310STPMSTI4VLANsMapped": gs2310STPMSTI4VLANsMapped,
       "gs2310STPMSTI5VLANsMapped": gs2310STPMSTI5VLANsMapped,
       "gs2310STPMSTI6VLANsMapped": gs2310STPMSTI6VLANsMapped,
       "gs2310STPMSTI7VLANsMapped": gs2310STPMSTI7VLANsMapped,
       "gs2310STPMSTIPriority": gs2310STPMSTIPriority,
       "gs2310STPCISTPriority": gs2310STPCISTPriority,
       "gs2310STPMSTI1Priority": gs2310STPMSTI1Priority,
       "gs2310STPMSTI2Priority": gs2310STPMSTI2Priority,
       "gs2310STPMSTI3Priority": gs2310STPMSTI3Priority,
       "gs2310STPMSTI4Priority": gs2310STPMSTI4Priority,
       "gs2310STPMSTI5Priority": gs2310STPMSTI5Priority,
       "gs2310STPMSTI6Priority": gs2310STPMSTI6Priority,
       "gs2310STPMSTI7Priority": gs2310STPMSTI7Priority,
       "gs2310STPCISTPort": gs2310STPCISTPort,
       "gs2310STPCISTAggregatedPort": gs2310STPCISTAggregatedPort,
       "gs2310STPCISTAggregatedPortSTPEnabled": gs2310STPCISTAggregatedPortSTPEnabled,
       "gs2310STPCISTAggregatedPortPathCost": gs2310STPCISTAggregatedPortPathCost,
       "gs2310STPCISTAggregatedPortPriority": gs2310STPCISTAggregatedPortPriority,
       "gs2310STPCISTAggregatedPortAdminEdge": gs2310STPCISTAggregatedPortAdminEdge,
       "gs2310STPCISTAggregatedPortAutoEdge": gs2310STPCISTAggregatedPortAutoEdge,
       "gs2310STPCISTAggregatedPortRestrictedRole": gs2310STPCISTAggregatedPortRestrictedRole,
       "gs2310STPCISTAggregatedPortRestrictedTCN": gs2310STPCISTAggregatedPortRestrictedTCN,
       "gs2310STPCISTAggregatedPortBPDUGuard": gs2310STPCISTAggregatedPortBPDUGuard,
       "gs2310STPCISTAggregatedPortPointtoPoint": gs2310STPCISTAggregatedPortPointtoPoint,
       "gs2310STPCISTNormalPortTable": gs2310STPCISTNormalPortTable,
       "gs2310STPCISTNormalPortEntry": gs2310STPCISTNormalPortEntry,
       "gs2310STPCISTNormalPortConfPort": gs2310STPCISTNormalPortConfPort,
       "gs2310STPCISTNormalPortSTPEnabled": gs2310STPCISTNormalPortSTPEnabled,
       "gs2310STPCISTNormalPortPathCost": gs2310STPCISTNormalPortPathCost,
       "gs2310STPCISTNormalPortPriority": gs2310STPCISTNormalPortPriority,
       "gs2310STPCISTNormalPortAdminEdge": gs2310STPCISTNormalPortAdminEdge,
       "gs2310STPCISTNormalPortAutoEdge": gs2310STPCISTNormalPortAutoEdge,
       "gs2310STPCISTNormalPortRestrictedRole": gs2310STPCISTNormalPortRestrictedRole,
       "gs2310STPCISTNormalPortRestrictedTCN": gs2310STPCISTNormalPortRestrictedTCN,
       "gs2310STPCISTNormalPortBPDUGuard": gs2310STPCISTNormalPortBPDUGuard,
       "gs2310STPCISTNormalPortPointtoPoint": gs2310STPCISTNormalPortPointtoPoint,
       "gs2310STPMSTIPort": gs2310STPMSTIPort,
       "gs2310STPMSTI1Port": gs2310STPMSTI1Port,
       "gs2310STPMSTI1AggregatedPort": gs2310STPMSTI1AggregatedPort,
       "gs2310STPMSTI1AggregatedPortPathCost": gs2310STPMSTI1AggregatedPortPathCost,
       "gs2310STPMSTI1AggregatedPortPriority": gs2310STPMSTI1AggregatedPortPriority,
       "gs2310STPMSTI1NormalPortTable": gs2310STPMSTI1NormalPortTable,
       "gs2310STPMSTI1NormalPortEntry": gs2310STPMSTI1NormalPortEntry,
       "gs2310STPMSTI1NormalPortConfPort": gs2310STPMSTI1NormalPortConfPort,
       "gs2310STPMSTI1NormalPortPathCost": gs2310STPMSTI1NormalPortPathCost,
       "gs2310STPMSTI1NormalPortPriority": gs2310STPMSTI1NormalPortPriority,
       "gs2310STPMSTI2Port": gs2310STPMSTI2Port,
       "gs2310STPMSTI2AggregatedPort": gs2310STPMSTI2AggregatedPort,
       "gs2310STPMSTI2AggregatedPortPathCost": gs2310STPMSTI2AggregatedPortPathCost,
       "gs2310STPMSTI2AggregatedPortPriority": gs2310STPMSTI2AggregatedPortPriority,
       "gs2310STPMSTI2NormalPortTable": gs2310STPMSTI2NormalPortTable,
       "gs2310STPMSTI2NormalPortEntry": gs2310STPMSTI2NormalPortEntry,
       "gs2310STPMSTI2NormalPortConfPort": gs2310STPMSTI2NormalPortConfPort,
       "gs2310STPMSTI2NormalPortPathCost": gs2310STPMSTI2NormalPortPathCost,
       "gs2310STPMSTI2NormalPortPriority": gs2310STPMSTI2NormalPortPriority,
       "gs2310STPMSTI3Port": gs2310STPMSTI3Port,
       "gs2310STPMSTI3AggregatedPort": gs2310STPMSTI3AggregatedPort,
       "gs2310STPMSTI3AggregatedPortPathCost": gs2310STPMSTI3AggregatedPortPathCost,
       "gs2310STPMSTI3AggregatedPortPriority": gs2310STPMSTI3AggregatedPortPriority,
       "gs2310STPMSTI3NormalPortTable": gs2310STPMSTI3NormalPortTable,
       "gs2310STPMSTI3NormalPortEntry": gs2310STPMSTI3NormalPortEntry,
       "gs2310STPMSTI3NormalPortConfPort": gs2310STPMSTI3NormalPortConfPort,
       "gs2310STPMSTI3NormalPortPathCost": gs2310STPMSTI3NormalPortPathCost,
       "gs2310STPMSTI3NormalPortPriority": gs2310STPMSTI3NormalPortPriority,
       "gs2310STPMSTI4Port": gs2310STPMSTI4Port,
       "gs2310STPMSTI4AggregatedPort": gs2310STPMSTI4AggregatedPort,
       "gs2310STPMSTI4AggregatedPortPathCost": gs2310STPMSTI4AggregatedPortPathCost,
       "gs2310STPMSTI4AggregatedPortPriority": gs2310STPMSTI4AggregatedPortPriority,
       "gs2310STPMSTI4NormalPortTable": gs2310STPMSTI4NormalPortTable,
       "gs2310STPMSTI4NormalPortEntry": gs2310STPMSTI4NormalPortEntry,
       "gs2310STPMSTI4NormalPortConfPort": gs2310STPMSTI4NormalPortConfPort,
       "gs2310STPMSTI4NormalPortPathCost": gs2310STPMSTI4NormalPortPathCost,
       "gs2310STPMSTI4NormalPortPriority": gs2310STPMSTI4NormalPortPriority,
       "gs2310STPMSTI5Port": gs2310STPMSTI5Port,
       "gs2310STPMSTI5AggregatedPort": gs2310STPMSTI5AggregatedPort,
       "gs2310STPMSTI5AggregatedPortPathCost": gs2310STPMSTI5AggregatedPortPathCost,
       "gs2310STPMSTI5AggregatedPortPriority": gs2310STPMSTI5AggregatedPortPriority,
       "gs2310STPMSTI5NormalPortTable": gs2310STPMSTI5NormalPortTable,
       "gs2310STPMSTI5NormalPortEntry": gs2310STPMSTI5NormalPortEntry,
       "gs2310STPMSTI5NormalPortConfPort": gs2310STPMSTI5NormalPortConfPort,
       "gs2310STPMSTI5NormalPortPathCost": gs2310STPMSTI5NormalPortPathCost,
       "gs2310STPMSTI5NormalPortPriority": gs2310STPMSTI5NormalPortPriority,
       "gs2310STPMSTI6Port": gs2310STPMSTI6Port,
       "gs2310STPMSTI6AggregatedPort": gs2310STPMSTI6AggregatedPort,
       "gs2310STPMSTI6AggregatedPortPathCost": gs2310STPMSTI6AggregatedPortPathCost,
       "gs2310STPMSTI6AggregatedPortPriority": gs2310STPMSTI6AggregatedPortPriority,
       "gs2310STPMSTI6NormalPortTable": gs2310STPMSTI6NormalPortTable,
       "gs2310STPMSTI6NormalPortEntry": gs2310STPMSTI6NormalPortEntry,
       "gs2310STPMSTI6NormalPortConfPort": gs2310STPMSTI6NormalPortConfPort,
       "gs2310STPMSTI6NormalPortPathCost": gs2310STPMSTI6NormalPortPathCost,
       "gs2310STPMSTI6NormalPortPriority": gs2310STPMSTI6NormalPortPriority,
       "gs2310STPMSTI7Port": gs2310STPMSTI7Port,
       "gs2310STPMSTI7AggregatedPort": gs2310STPMSTI7AggregatedPort,
       "gs2310STPMSTI7AggregatedPortPathCost": gs2310STPMSTI7AggregatedPortPathCost,
       "gs2310STPMSTI7AggregatedPortPriority": gs2310STPMSTI7AggregatedPortPriority,
       "gs2310STPMSTI7NormalPortTable": gs2310STPMSTI7NormalPortTable,
       "gs2310STPMSTI7NormalPortEntry": gs2310STPMSTI7NormalPortEntry,
       "gs2310STPMSTI7NormalPortConfPort": gs2310STPMSTI7NormalPortConfPort,
       "gs2310STPMSTI7NormalPortPathCost": gs2310STPMSTI7NormalPortPathCost,
       "gs2310STPMSTI7NormalPortPriority": gs2310STPMSTI7NormalPortPriority,
       "gs2310STPBridgeStatus": gs2310STPBridgeStatus,
       "gs2310CISTBridgeSTP": gs2310CISTBridgeSTP,
       "gs2310CISTBridgeSTPStatus": gs2310CISTBridgeSTPStatus,
       "gs2310CISTBridgeInstance": gs2310CISTBridgeInstance,
       "gs2310CISTBridgeID": gs2310CISTBridgeID,
       "gs2310CISTRootID": gs2310CISTRootID,
       "gs2310CISTRootPort": gs2310CISTRootPort,
       "gs2310CISTRootCost": gs2310CISTRootCost,
       "gs2310CISTRegionalRoot": gs2310CISTRegionalRoot,
       "gs2310CISTInternalRootCost": gs2310CISTInternalRootCost,
       "gs2310CISTTopologyFlag": gs2310CISTTopologyFlag,
       "gs2310CISTTopologyChangeCount": gs2310CISTTopologyChangeCount,
       "gs2310CISTTopologyChangeLast": gs2310CISTTopologyChangeLast,
       "gs2310CISTPortStateTable": gs2310CISTPortStateTable,
       "gs2310CISTPortStateEntry": gs2310CISTPortStateEntry,
       "gs2310CISTPortStateIndex": gs2310CISTPortStateIndex,
       "gs2310CISTPortStatePort": gs2310CISTPortStatePort,
       "gs2310CISTPortStatePortID": gs2310CISTPortStatePortID,
       "gs2310CISTPortStateRole": gs2310CISTPortStateRole,
       "gs2310CISTPortStateState": gs2310CISTPortStateState,
       "gs2310CISTPortStatePathCost": gs2310CISTPortStatePathCost,
       "gs2310CISTPortStateEdge": gs2310CISTPortStateEdge,
       "gs2310CISTPortStatePoint2Point": gs2310CISTPortStatePoint2Point,
       "gs2310CISTPortStateUptime": gs2310CISTPortStateUptime,
       "gs2310MSTI1BridgeSTP": gs2310MSTI1BridgeSTP,
       "gs2310MSTI1BridgeSTPStatus": gs2310MSTI1BridgeSTPStatus,
       "gs2310MSTI1BridgeInstance": gs2310MSTI1BridgeInstance,
       "gs2310MSTI1BridgeID": gs2310MSTI1BridgeID,
       "gs2310MSTI1RootID": gs2310MSTI1RootID,
       "gs2310MSTI1RootPort": gs2310MSTI1RootPort,
       "gs2310MSTI1RootCost": gs2310MSTI1RootCost,
       "gs2310MSTI1TopologyFlag": gs2310MSTI1TopologyFlag,
       "gs2310MSTI1TopologyChangeCount": gs2310MSTI1TopologyChangeCount,
       "gs2310MSTI1TopologyChangeLast": gs2310MSTI1TopologyChangeLast,
       "gs2310MSTI1PortStateTable": gs2310MSTI1PortStateTable,
       "gs2310MSTI1PortStateEntry": gs2310MSTI1PortStateEntry,
       "gs2310MSTI1PortStateIndex": gs2310MSTI1PortStateIndex,
       "gs2310MSTI1PortStatePort": gs2310MSTI1PortStatePort,
       "gs2310MSTI1PortStatePortID": gs2310MSTI1PortStatePortID,
       "gs2310MSTI1PortStateRole": gs2310MSTI1PortStateRole,
       "gs2310MSTI1PortStateState": gs2310MSTI1PortStateState,
       "gs2310MSTI1PortStatePathCost": gs2310MSTI1PortStatePathCost,
       "gs2310MSTI1PortStateEdge": gs2310MSTI1PortStateEdge,
       "gs2310MSTI1PortStatePoint2Point": gs2310MSTI1PortStatePoint2Point,
       "gs2310MSTI1PortStateUptime": gs2310MSTI1PortStateUptime,
       "gs2310MSTI2BridgeSTP": gs2310MSTI2BridgeSTP,
       "gs2310MSTI2BridgeSTPStatus": gs2310MSTI2BridgeSTPStatus,
       "gs2310MSTI2BridgeInstance": gs2310MSTI2BridgeInstance,
       "gs2310MSTI2BridgeID": gs2310MSTI2BridgeID,
       "gs2310MSTI2RootID": gs2310MSTI2RootID,
       "gs2310MSTI2RootPort": gs2310MSTI2RootPort,
       "gs2310MSTI2RootCost": gs2310MSTI2RootCost,
       "gs2310MSTI2TopologyFlag": gs2310MSTI2TopologyFlag,
       "gs2310MSTI2TopologyChangeCount": gs2310MSTI2TopologyChangeCount,
       "gs2310MSTI2TopologyChangeLast": gs2310MSTI2TopologyChangeLast,
       "gs2310MSTI2PortStateTable": gs2310MSTI2PortStateTable,
       "gs2310MSTI2PortStateEntry": gs2310MSTI2PortStateEntry,
       "gs2310MSTI2PortStateIndex": gs2310MSTI2PortStateIndex,
       "gs2310MSTI2PortStatePort": gs2310MSTI2PortStatePort,
       "gs2310MSTI2PortStatePortID": gs2310MSTI2PortStatePortID,
       "gs2310MSTI2PortStateRole": gs2310MSTI2PortStateRole,
       "gs2310MSTI2PortStateState": gs2310MSTI2PortStateState,
       "gs2310MSTI2PortStatePathCost": gs2310MSTI2PortStatePathCost,
       "gs2310MSTI2PortStateEdge": gs2310MSTI2PortStateEdge,
       "gs2310MSTI2PortStatePoint2Point": gs2310MSTI2PortStatePoint2Point,
       "gs2310MSTI2PortStateUptime": gs2310MSTI2PortStateUptime,
       "gs2310MSTI3BridgeSTP": gs2310MSTI3BridgeSTP,
       "gs2310MSTI3BridgeSTPStatus": gs2310MSTI3BridgeSTPStatus,
       "gs2310MSTI3BridgeInstance": gs2310MSTI3BridgeInstance,
       "gs2310MSTI3BridgeID": gs2310MSTI3BridgeID,
       "gs2310MSTI3RootID": gs2310MSTI3RootID,
       "gs2310MSTI3RootPort": gs2310MSTI3RootPort,
       "gs2310MSTI3RootCost": gs2310MSTI3RootCost,
       "gs2310MSTI3TopologyFlag": gs2310MSTI3TopologyFlag,
       "gs2310MSTI3TopologyChangeCount": gs2310MSTI3TopologyChangeCount,
       "gs2310MSTI3TopologyChangeLast": gs2310MSTI3TopologyChangeLast,
       "gs2310MSTI3PortStateTable": gs2310MSTI3PortStateTable,
       "gs2310MSTI3PortStateEntry": gs2310MSTI3PortStateEntry,
       "gs2310MSTI3PortStateIndex": gs2310MSTI3PortStateIndex,
       "gs2310MSTI3PortStatePort": gs2310MSTI3PortStatePort,
       "gs2310MSTI3PortStatePortID": gs2310MSTI3PortStatePortID,
       "gs2310MSTI3PortStateRole": gs2310MSTI3PortStateRole,
       "gs2310MSTI3PortStateState": gs2310MSTI3PortStateState,
       "gs2310MSTI3PortStatePathCost": gs2310MSTI3PortStatePathCost,
       "gs2310MSTI3PortStateEdge": gs2310MSTI3PortStateEdge,
       "gs2310MSTI3PortStatePoint2Point": gs2310MSTI3PortStatePoint2Point,
       "gs2310MSTI3PortStateUptime": gs2310MSTI3PortStateUptime,
       "gs2310MSTI4BridgeSTP": gs2310MSTI4BridgeSTP,
       "gs2310MSTI4BridgeSTPStatus": gs2310MSTI4BridgeSTPStatus,
       "gs2310MSTI4BridgeInstance": gs2310MSTI4BridgeInstance,
       "gs2310MSTI4BridgeID": gs2310MSTI4BridgeID,
       "gs2310MSTI4RootID": gs2310MSTI4RootID,
       "gs2310MSTI4RootPort": gs2310MSTI4RootPort,
       "gs2310MSTI4RootCost": gs2310MSTI4RootCost,
       "gs2310MSTI4TopologyFlag": gs2310MSTI4TopologyFlag,
       "gs2310MSTI4TopologyChangeCount": gs2310MSTI4TopologyChangeCount,
       "gs2310MSTI4TopologyChangeLast": gs2310MSTI4TopologyChangeLast,
       "gs2310MSTI4PortStateTable": gs2310MSTI4PortStateTable,
       "gs2310MSTI4PortStateEntry": gs2310MSTI4PortStateEntry,
       "gs2310MSTI4PortStateIndex": gs2310MSTI4PortStateIndex,
       "gs2310MSTI4PortStatePort": gs2310MSTI4PortStatePort,
       "gs2310MSTI4PortStatePortID": gs2310MSTI4PortStatePortID,
       "gs2310MSTI4PortStateRole": gs2310MSTI4PortStateRole,
       "gs2310MSTI4PortStateState": gs2310MSTI4PortStateState,
       "gs2310MSTI4PortStatePathCost": gs2310MSTI4PortStatePathCost,
       "gs2310MSTI4PortStateEdge": gs2310MSTI4PortStateEdge,
       "gs2310MSTI4PortStatePoint2Point": gs2310MSTI4PortStatePoint2Point,
       "gs2310MSTI4PortStateUptime": gs2310MSTI4PortStateUptime,
       "gs2310MSTI5BridgeSTP": gs2310MSTI5BridgeSTP,
       "gs2310MSTI5BridgeSTPStatus": gs2310MSTI5BridgeSTPStatus,
       "gs2310MSTI5BridgeInstance": gs2310MSTI5BridgeInstance,
       "gs2310MSTI5BridgeID": gs2310MSTI5BridgeID,
       "gs2310MSTI5RootID": gs2310MSTI5RootID,
       "gs2310MSTI5RootPort": gs2310MSTI5RootPort,
       "gs2310MSTI5RootCost": gs2310MSTI5RootCost,
       "gs2310MSTI5TopologyFlag": gs2310MSTI5TopologyFlag,
       "gs2310MSTI5TopologyChangeCount": gs2310MSTI5TopologyChangeCount,
       "gs2310MSTI5TopologyChangeLast": gs2310MSTI5TopologyChangeLast,
       "gs2310MSTI5PortStateTable": gs2310MSTI5PortStateTable,
       "gs2310MSTI5PortStateEntry": gs2310MSTI5PortStateEntry,
       "gs2310MSTI5PortStateIndex": gs2310MSTI5PortStateIndex,
       "gs2310MSTI5PortStatePort": gs2310MSTI5PortStatePort,
       "gs2310MSTI5PortStatePortID": gs2310MSTI5PortStatePortID,
       "gs2310MSTI5PortStateRole": gs2310MSTI5PortStateRole,
       "gs2310MSTI5PortStateState": gs2310MSTI5PortStateState,
       "gs2310MSTI5PortStatePathCost": gs2310MSTI5PortStatePathCost,
       "gs2310MSTI5PortStateEdge": gs2310MSTI5PortStateEdge,
       "gs2310MSTI5PortStatePoint2Point": gs2310MSTI5PortStatePoint2Point,
       "gs2310MSTI5PortStateUptime": gs2310MSTI5PortStateUptime,
       "gs2310MSTI6BridgeSTP": gs2310MSTI6BridgeSTP,
       "gs2310MSTI6BridgeSTPStatus": gs2310MSTI6BridgeSTPStatus,
       "gs2310MSTI6BridgeInstance": gs2310MSTI6BridgeInstance,
       "gs2310MSTI6BridgeID": gs2310MSTI6BridgeID,
       "gs2310MSTI6RootID": gs2310MSTI6RootID,
       "gs2310MSTI6RootPort": gs2310MSTI6RootPort,
       "gs2310MSTI6RootCost": gs2310MSTI6RootCost,
       "gs2310MSTI6TopologyFlag": gs2310MSTI6TopologyFlag,
       "gs2310MSTI6TopologyChangeCount": gs2310MSTI6TopologyChangeCount,
       "gs2310MSTI6TopologyChangeLast": gs2310MSTI6TopologyChangeLast,
       "gs2310MSTI6PortStateTable": gs2310MSTI6PortStateTable,
       "gs2310MSTI6PortStateEntry": gs2310MSTI6PortStateEntry,
       "gs2310MSTI6PortStateIndex": gs2310MSTI6PortStateIndex,
       "gs2310MSTI6PortStatePort": gs2310MSTI6PortStatePort,
       "gs2310MSTI6PortStatePortID": gs2310MSTI6PortStatePortID,
       "gs2310MSTI6PortStateRole": gs2310MSTI6PortStateRole,
       "gs2310MSTI6PortStateState": gs2310MSTI6PortStateState,
       "gs2310MSTI6PortStatePathCost": gs2310MSTI6PortStatePathCost,
       "gs2310MSTI6PortStateEdge": gs2310MSTI6PortStateEdge,
       "gs2310MSTI6PortStatePoint2Point": gs2310MSTI6PortStatePoint2Point,
       "gs2310MSTI6PortStateUptime": gs2310MSTI6PortStateUptime,
       "gs2310MSTI7BridgeSTP": gs2310MSTI7BridgeSTP,
       "gs2310MSTI7BridgeSTPStatus": gs2310MSTI7BridgeSTPStatus,
       "gs2310MSTI7BridgeInstance": gs2310MSTI7BridgeInstance,
       "gs2310MSTI7BridgeID": gs2310MSTI7BridgeID,
       "gs2310MSTI7RootID": gs2310MSTI7RootID,
       "gs2310MSTI7RootPort": gs2310MSTI7RootPort,
       "gs2310MSTI7RootCost": gs2310MSTI7RootCost,
       "gs2310MSTI7TopologyFlag": gs2310MSTI7TopologyFlag,
       "gs2310MSTI7TopologyChangeCount": gs2310MSTI7TopologyChangeCount,
       "gs2310MSTI7TopologyChangeLast": gs2310MSTI7TopologyChangeLast,
       "gs2310MSTI7PortStateTable": gs2310MSTI7PortStateTable,
       "gs2310MSTI7PortStateEntry": gs2310MSTI7PortStateEntry,
       "gs2310MSTI7PortStateIndex": gs2310MSTI7PortStateIndex,
       "gs2310MSTI7PortStatePort": gs2310MSTI7PortStatePort,
       "gs2310MSTI7PortStatePortID": gs2310MSTI7PortStatePortID,
       "gs2310MSTI7PortStateRole": gs2310MSTI7PortStateRole,
       "gs2310MSTI7PortStateState": gs2310MSTI7PortStateState,
       "gs2310MSTI7PortStatePathCost": gs2310MSTI7PortStatePathCost,
       "gs2310MSTI7PortStateEdge": gs2310MSTI7PortStateEdge,
       "gs2310MSTI7PortStatePoint2Point": gs2310MSTI7PortStatePoint2Point,
       "gs2310MSTI7PortStateUptime": gs2310MSTI7PortStateUptime,
       "gs2310STPPortStatusTable": gs2310STPPortStatusTable,
       "gs2310STPPortStatusEntry": gs2310STPPortStatusEntry,
       "gs2310STPPortStatusPort": gs2310STPPortStatusPort,
       "gs2310STPPortStatusCISTRole": gs2310STPPortStatusCISTRole,
       "gs2310STPPortStatusCISTState": gs2310STPPortStatusCISTState,
       "gs2310STPPortStatusUptime": gs2310STPPortStatusUptime,
       "gs2310STPPortStatisticsTable": gs2310STPPortStatisticsTable,
       "gs2310STPPortStatisticsEntry": gs2310STPPortStatisticsEntry,
       "gs2310STPStatisticsIndex": gs2310STPStatisticsIndex,
       "gs2310STPStatisticsPort": gs2310STPStatisticsPort,
       "gs2310STPStatisticsTxMSTP": gs2310STPStatisticsTxMSTP,
       "gs2310STPStatisticsTxRSTP": gs2310STPStatisticsTxRSTP,
       "gs2310STPStatisticsTxSTP": gs2310STPStatisticsTxSTP,
       "gs2310STPStatisticsTxTCN": gs2310STPStatisticsTxTCN,
       "gs2310STPStatisticsRxMSTP": gs2310STPStatisticsRxMSTP,
       "gs2310STPStatisticsRxRSTP": gs2310STPStatisticsRxRSTP,
       "gs2310STPStatisticsRxSTP": gs2310STPStatisticsRxSTP,
       "gs2310STPStatisticsRxTCN": gs2310STPStatisticsRxTCN,
       "gs2310STPStatisticsDiscardedUnknown": gs2310STPStatisticsDiscardedUnknown,
       "gs2310STPStatisticsDiscardedIllegal": gs2310STPStatisticsDiscardedIllegal,
       "gs2310FilteringDataBase": gs2310FilteringDataBase,
       "gs2310FilteringDataBaseConfig": gs2310FilteringDataBaseConfig,
       "gs2310FilteringDataBaseAgingTime": gs2310FilteringDataBaseAgingTime,
       "gs2310FilteringDataBaseConfigTable": gs2310FilteringDataBaseConfigTable,
       "gs2310FilteringDataBaseConfigEntry": gs2310FilteringDataBaseConfigEntry,
       "gs2310FilteringDataBaseConfigPort": gs2310FilteringDataBaseConfigPort,
       "gs2310FilteringDataBaseConfigLearning": gs2310FilteringDataBaseConfigLearning,
       "gs2310FilteringDataBaseStaticMAC": gs2310FilteringDataBaseStaticMAC,
       "gs2310FilteringDataBaseStaticMACCreate": gs2310FilteringDataBaseStaticMACCreate,
       "gs2310FilteringDataBaseStaticMACTable": gs2310FilteringDataBaseStaticMACTable,
       "gs2310FilteringDataBaseStaticMACEntry": gs2310FilteringDataBaseStaticMACEntry,
       "gs2310FilteringDataBaseStaticMACIndex": gs2310FilteringDataBaseStaticMACIndex,
       "gs2310FilteringDataBaseStaticMACVLANId": gs2310FilteringDataBaseStaticMACVLANId,
       "gs2310FilteringDataBaseStaticMACAddress": gs2310FilteringDataBaseStaticMACAddress,
       "gs2310FilteringDataBaseStaticMACPortMembers": gs2310FilteringDataBaseStaticMACPortMembers,
       "gs2310FilteringDataBaseStaticMACRowStatus": gs2310FilteringDataBaseStaticMACRowStatus,
       "gs2310FilteringDataBaseDynamicMACTable": gs2310FilteringDataBaseDynamicMACTable,
       "gs2310FilteringDataBaseDynamicMACEntry": gs2310FilteringDataBaseDynamicMACEntry,
       "gs2310FilteringDataBaseDynamicMACIndex": gs2310FilteringDataBaseDynamicMACIndex,
       "gs2310FilteringDataBaseDynamicMACType": gs2310FilteringDataBaseDynamicMACType,
       "gs2310FilteringDataBaseDynamicMACVLAN": gs2310FilteringDataBaseDynamicMACVLAN,
       "gs2310FilteringDataBaseDynamicMACAddress": gs2310FilteringDataBaseDynamicMACAddress,
       "gs2310FilteringDataBaseDynamicPortMembers": gs2310FilteringDataBaseDynamicPortMembers,
       "gs2310SFlowAgent": gs2310SFlowAgent,
       "gs2310SFlowAgentCollector": gs2310SFlowAgentCollector,
       "gs2310SFlowAgentReceiverMode": gs2310SFlowAgentReceiverMode,
       "gs2310LMC": gs2310LMC,
       "gs2310LMCOperating": gs2310LMCOperating,
       "gs2310LMCConfigViaDhcp": gs2310LMCConfigViaDhcp,
       "gs2310LMCDomain": gs2310LMCDomain,
       "gs2310LMCDhcpClientAutoRenew": gs2310LMCDhcpClientAutoRenew,
       "gs2310LMCZeroTouchSupport": gs2310LMCZeroTouchSupport,
       "gs2310LMCPairingTokenPresent": gs2310LMCPairingTokenPresent,
       "gs2310LMCClientStatus": gs2310LMCClientStatus,
       "gs2310LMCManagementStatus": gs2310LMCManagementStatus,
       "gs2310LMCControlStatus": gs2310LMCControlStatus,
       "gs2310pLMCMonitoringStatus": gs2310pLMCMonitoringStatus,
       "gs2310LMCConfigurationSource": gs2310LMCConfigurationSource,
       "gs2310LMCConfigModified": gs2310LMCConfigModified,
       "gs2310LMCDeviceID": gs2310LMCDeviceID,
       "gs2310LMCRoundTripTime": gs2310LMCRoundTripTime,
       "gs2310Security": gs2310Security,
       "gs2310IPSourceGuard": gs2310IPSourceGuard,
       "gs2310IPSourceGuardConf": gs2310IPSourceGuardConf,
       "gs2310IPSourceGuardMode": gs2310IPSourceGuardMode,
       "gs2310IPSourceGuardPortConfigTable": gs2310IPSourceGuardPortConfigTable,
       "gs2310IPSourceGuardPortConfigEntry": gs2310IPSourceGuardPortConfigEntry,
       "gs2310IPSourceGuardPortConfigPort": gs2310IPSourceGuardPortConfigPort,
       "gs2310IPSourceGuardPortConfigMode": gs2310IPSourceGuardPortConfigMode,
       "gs2310IPSourceGuardPortMaxDynamicClients": gs2310IPSourceGuardPortMaxDynamicClients,
       "gs2310IPSourceGuardStatic": gs2310IPSourceGuardStatic,
       "gs2310IPSourceGuardStaticCreate": gs2310IPSourceGuardStaticCreate,
       "gs2310IPSourceGuardStaticTable": gs2310IPSourceGuardStaticTable,
       "gs2310IPSourceGuardStaticEntry": gs2310IPSourceGuardStaticEntry,
       "gs2310IPSourceGuardStaticIndex": gs2310IPSourceGuardStaticIndex,
       "gs2310IPSourceGuardStaticPort": gs2310IPSourceGuardStaticPort,
       "gs2310IPSourceGuardStaticVLANId": gs2310IPSourceGuardStaticVLANId,
       "gs2310IPSourceGuardStaticIPAddress": gs2310IPSourceGuardStaticIPAddress,
       "gs2310IPSourceGuardStaticMACAddress": gs2310IPSourceGuardStaticMACAddress,
       "gs2310IPSourceGuardStaticRowStatus": gs2310IPSourceGuardStaticRowStatus,
       "gs2310IPSourceGuardDynamicTable": gs2310IPSourceGuardDynamicTable,
       "gs2310IPSourceGuardDynamicEntry": gs2310IPSourceGuardDynamicEntry,
       "gs2310IPSourceGuardDynamicIndex": gs2310IPSourceGuardDynamicIndex,
       "gs2310IPSourceGuardDynamicPort": gs2310IPSourceGuardDynamicPort,
       "gs2310IPSourceGuardDynamicVLANId": gs2310IPSourceGuardDynamicVLANId,
       "gs2310IPSourceGuardDynamicIPAddress": gs2310IPSourceGuardDynamicIPAddress,
       "gs2310IPSourceGuardDynamicMACAddress": gs2310IPSourceGuardDynamicMACAddress,
       "gs2310ARPInspection": gs2310ARPInspection,
       "gs2310ARPInspectionConf": gs2310ARPInspectionConf,
       "gs2310ARPInspectionConfMode": gs2310ARPInspectionConfMode,
       "gs2310ARPInspectionConfTable": gs2310ARPInspectionConfTable,
       "gs2310ARPInspectionConfEntry": gs2310ARPInspectionConfEntry,
       "gs2310ARPInspectionConfPortIndex": gs2310ARPInspectionConfPortIndex,
       "gs2310ARPInspectionConfPortMode": gs2310ARPInspectionConfPortMode,
       "gs2310ARPInspectionStatic": gs2310ARPInspectionStatic,
       "gs2310ARPInspectionStaticCreate": gs2310ARPInspectionStaticCreate,
       "gs2310ARPInspectionStaticTable": gs2310ARPInspectionStaticTable,
       "gs2310ARPInspectionStaticEntry": gs2310ARPInspectionStaticEntry,
       "gs2310ARPInspectionStaticIndex": gs2310ARPInspectionStaticIndex,
       "gs2310ARPInspectionStaticPort": gs2310ARPInspectionStaticPort,
       "gs2310ARPInspectionStaticVLANId": gs2310ARPInspectionStaticVLANId,
       "gs2310ARPInspectionStaticIPAddress": gs2310ARPInspectionStaticIPAddress,
       "gs2310ARPInspectionStaticMACAddress": gs2310ARPInspectionStaticMACAddress,
       "gs2310ARPInspectionStaticRowStatus": gs2310ARPInspectionStaticRowStatus,
       "gs2310ARPInspectionDynamicTable": gs2310ARPInspectionDynamicTable,
       "gs2310ARPInspectionDynamicEntry": gs2310ARPInspectionDynamicEntry,
       "gs2310ARPInspectionDynamicIndex": gs2310ARPInspectionDynamicIndex,
       "gs2310ARPInspectionDynamicPort": gs2310ARPInspectionDynamicPort,
       "gs2310ARPInspectionDynamicVLANId": gs2310ARPInspectionDynamicVLANId,
       "gs2310ARPInspectionDynamicIPAddress": gs2310ARPInspectionDynamicIPAddress,
       "gs2310ARPInspectionDynamicMACAddress": gs2310ARPInspectionDynamicMACAddress,
       "gs2310ARPStaticGatewayCtrl": gs2310ARPStaticGatewayCtrl,
       "gs2310ARPStaticGatewayCtrlSystemConf": gs2310ARPStaticGatewayCtrlSystemConf,
       "gs2310ARPStaticGatewayCtrlMode": gs2310ARPStaticGatewayCtrlMode,
       "gs2310ARPStaticGatewayCtrlCreate": gs2310ARPStaticGatewayCtrlCreate,
       "gs2310ARPStaticGatewayCtrlTable": gs2310ARPStaticGatewayCtrlTable,
       "gs2310ARPStaticGatewayCtrlEntry": gs2310ARPStaticGatewayCtrlEntry,
       "gs2310ARPStaticGatewayCtrlIndex": gs2310ARPStaticGatewayCtrlIndex,
       "gs2310ARPStaticGatewayCtrlIPAddress": gs2310ARPStaticGatewayCtrlIPAddress,
       "gs2310ARPStaticGatewayCtrlMACAddress": gs2310ARPStaticGatewayCtrlMACAddress,
       "gs2310ARPStaticGatewayCtrlPort": gs2310ARPStaticGatewayCtrlPort,
       "gs2310ARPStaticGatewayCtrlAction": gs2310ARPStaticGatewayCtrlAction,
       "gs2310ARPStaticGatewayCtrlState": gs2310ARPStaticGatewayCtrlState,
       "gs2310ARPStaticGatewayCtrlReOpen": gs2310ARPStaticGatewayCtrlReOpen,
       "gs2310ARPStaticGatewayCtrlRowStatus": gs2310ARPStaticGatewayCtrlRowStatus,
       "gs2310ARPSpoofingPrevention": gs2310ARPSpoofingPrevention,
       "gs2310ARPSpoofingPreventionSystemConf": gs2310ARPSpoofingPreventionSystemConf,
       "gs2310ARPSpoofingPreventionMode": gs2310ARPSpoofingPreventionMode,
       "gs2310ARPSpoofingPreventionTable": gs2310ARPSpoofingPreventionTable,
       "gs2310ARPSpoofingPreventionEntry": gs2310ARPSpoofingPreventionEntry,
       "gs2310ARPSpoofingPreventionPort": gs2310ARPSpoofingPreventionPort,
       "gs2310ARPSpoofingPreventionPortMode": gs2310ARPSpoofingPreventionPortMode,
       "gs2310ARPSpoofingPreventionPortLimit": gs2310ARPSpoofingPreventionPortLimit,
       "gs2310ARPSpoofingPreventionPortAction": gs2310ARPSpoofingPreventionPortAction,
       "gs2310ARPSpoofingPreventionPortState": gs2310ARPSpoofingPreventionPortState,
       "gs2310ARPSpoofingPreventionPortReOpen": gs2310ARPSpoofingPreventionPortReOpen,
       "gs2310ARPIPDoSPrevention": gs2310ARPIPDoSPrevention,
       "gs2310ARPIPDoSPreventionTCPMode": gs2310ARPIPDoSPreventionTCPMode,
       "gs2310ARPIPDoSPreventionUDPMode": gs2310ARPIPDoSPreventionUDPMode,
       "gs2310ARPIPDoSPreventionICMPMode": gs2310ARPIPDoSPreventionICMPMode,
       "gs2310ARPIPDoSPreventionServerPort1": gs2310ARPIPDoSPreventionServerPort1,
       "gs2310ARPIPDoSPreventionServerPort2": gs2310ARPIPDoSPreventionServerPort2,
       "gs2310ARPIPDoSPreventionServerPort3": gs2310ARPIPDoSPreventionServerPort3,
       "gs2310ARPIPDoSPreventionServerPort4": gs2310ARPIPDoSPreventionServerPort4,
       "gs2310DHCPSnooping": gs2310DHCPSnooping,
       "gs2310DHCPSnoopingConf": gs2310DHCPSnoopingConf,
       "gs2310DHCPSnoopingMode": gs2310DHCPSnoopingMode,
       "gs2310DHCPSnoopingPortModeConfigurationTable": gs2310DHCPSnoopingPortModeConfigurationTable,
       "gs2310DHCPSnoopingPortModeConfigurationEntry": gs2310DHCPSnoopingPortModeConfigurationEntry,
       "gs2310DHCPSnoopingPortModeConfigurationPort": gs2310DHCPSnoopingPortModeConfigurationPort,
       "gs2310DHCPSnoopingPortModeConfigurationMode": gs2310DHCPSnoopingPortModeConfigurationMode,
       "gs2310DHCPSnoopingStatisticsTable": gs2310DHCPSnoopingStatisticsTable,
       "gs2310DHCPSnoopingStatisticsEntry": gs2310DHCPSnoopingStatisticsEntry,
       "gs2310DHCPSnoopingStatisticsPort": gs2310DHCPSnoopingStatisticsPort,
       "gs2310DHCPSnoopingStatisticsClear": gs2310DHCPSnoopingStatisticsClear,
       "gs2310DHCPSnoopingRxDiscover": gs2310DHCPSnoopingRxDiscover,
       "gs2310DHCPSnoopingRxOffer": gs2310DHCPSnoopingRxOffer,
       "gs2310DHCPSnoopingRxRequest": gs2310DHCPSnoopingRxRequest,
       "gs2310DHCPSnoopingRxDecline": gs2310DHCPSnoopingRxDecline,
       "gs2310DHCPSnoopingRxACK": gs2310DHCPSnoopingRxACK,
       "gs2310DHCPSnoopingRxNAK": gs2310DHCPSnoopingRxNAK,
       "gs2310DHCPSnoopingRxRelease": gs2310DHCPSnoopingRxRelease,
       "gs2310DHCPSnoopingRxInform": gs2310DHCPSnoopingRxInform,
       "gs2310DHCPSnoopingRxLeaseQuery": gs2310DHCPSnoopingRxLeaseQuery,
       "gs2310DHCPSnoopingRxLeaseUnassigned": gs2310DHCPSnoopingRxLeaseUnassigned,
       "gs2310DHCPSnoopingRxLeaseUnknown": gs2310DHCPSnoopingRxLeaseUnknown,
       "gs2310DHCPSnoopingRxLeaseActive": gs2310DHCPSnoopingRxLeaseActive,
       "gs2310DHCPSnoopingTxDiscover": gs2310DHCPSnoopingTxDiscover,
       "gs2310DHCPSnoopingTxOffer": gs2310DHCPSnoopingTxOffer,
       "gs2310DHCPSnoopingTxRequest": gs2310DHCPSnoopingTxRequest,
       "gs2310DHCPSnoopingTxDecline": gs2310DHCPSnoopingTxDecline,
       "gs2310DHCPSnoopingTxACK": gs2310DHCPSnoopingTxACK,
       "gs2310DHCPSnoopingTxNAK": gs2310DHCPSnoopingTxNAK,
       "gs2310DHCPSnoopingTxRelease": gs2310DHCPSnoopingTxRelease,
       "gs2310DHCPSnoopingTxInform": gs2310DHCPSnoopingTxInform,
       "gs2310DHCPSnoopingTxLeaseQuery": gs2310DHCPSnoopingTxLeaseQuery,
       "gs2310DHCPSnoopingTxLeaseUnassigned": gs2310DHCPSnoopingTxLeaseUnassigned,
       "gs2310DHCPSnoopingTxLeaseUnknown": gs2310DHCPSnoopingTxLeaseUnknown,
       "gs2310DHCPSnoopingTxLeaseActive": gs2310DHCPSnoopingTxLeaseActive,
       "gs2310DHCPRelay": gs2310DHCPRelay,
       "gs2310DHCPRelayConfiguration": gs2310DHCPRelayConfiguration,
       "gs2310DHCPRelayMode": gs2310DHCPRelayMode,
       "gs2310DHCPRelayServer": gs2310DHCPRelayServer,
       "gs2310DHCPRelayInformationMode": gs2310DHCPRelayInformationMode,
       "gs2310DHCPRelayInformationPolicy": gs2310DHCPRelayInformationPolicy,
       "gs2310DHCPRelayConfigurationGateways": gs2310DHCPRelayConfigurationGateways,
       "gs2310DHCPRelayConfigurationGatewaysCreate": gs2310DHCPRelayConfigurationGatewaysCreate,
       "gs2310DHCPRelayConfigurationGatewaysTable": gs2310DHCPRelayConfigurationGatewaysTable,
       "gs2310DHCPRelayConfigurationGatewaysEntry": gs2310DHCPRelayConfigurationGatewaysEntry,
       "gs2310DHCPRelayConfigurationGatewaysIndex": gs2310DHCPRelayConfigurationGatewaysIndex,
       "gs2310DHCPRelayConfigurationGatewaysVLANId": gs2310DHCPRelayConfigurationGatewaysVLANId,
       "gs2310DHCPRelayConfigurationGatewaysIP": gs2310DHCPRelayConfigurationGatewaysIP,
       "gs2310DHCPRelayConfigurationGatewaysRowStatus": gs2310DHCPRelayConfigurationGatewaysRowStatus,
       "gs2310DHCPRelayInformationCustom": gs2310DHCPRelayInformationCustom,
       "gs2310DHCPRelayStatistics": gs2310DHCPRelayStatistics,
       "gs2310DHCPRelayServerStatistics": gs2310DHCPRelayServerStatistics,
       "gs2310ServerStatTransmitToServer": gs2310ServerStatTransmitToServer,
       "gs2310ServerStatTransmitError": gs2310ServerStatTransmitError,
       "gs2310ServerStatReceiveFromServer": gs2310ServerStatReceiveFromServer,
       "gs2310ServerStatReceiveMissingAgentOption": gs2310ServerStatReceiveMissingAgentOption,
       "gs2310ServerStatReceiveMissingCircuitID": gs2310ServerStatReceiveMissingCircuitID,
       "gs2310ServerStatReceiveMissingRemoteID": gs2310ServerStatReceiveMissingRemoteID,
       "gs2310ServerStatReceiveBadCircuitID": gs2310ServerStatReceiveBadCircuitID,
       "gs2310ServerStatReceiveBadRemoteID": gs2310ServerStatReceiveBadRemoteID,
       "gs2310DHCPRelayClientStatistics": gs2310DHCPRelayClientStatistics,
       "gs2310ClientStatTransmitToClient": gs2310ClientStatTransmitToClient,
       "gs2310ClientStatTransmitError": gs2310ClientStatTransmitError,
       "gs2310ClientStatReceivefromClient": gs2310ClientStatReceivefromClient,
       "gs2310ClientStatReceiveAgentOption": gs2310ClientStatReceiveAgentOption,
       "gs2310ClientStatReplaceAgentOption": gs2310ClientStatReplaceAgentOption,
       "gs2310ClientStatKeepAgentOption": gs2310ClientStatKeepAgentOption,
       "gs2310ClientStatDropAgentOption": gs2310ClientStatDropAgentOption,
       "gs2310PortSecurity": gs2310PortSecurity,
       "gs2310PortSecLimitCtrl": gs2310PortSecLimitCtrl,
       "gs2310PortSecLimitCtrlSystemConf": gs2310PortSecLimitCtrlSystemConf,
       "gs2310PortSecurityMode": gs2310PortSecurityMode,
       "gs2310PortSecurityAging": gs2310PortSecurityAging,
       "gs2310PortSecurityAgingPeriod": gs2310PortSecurityAgingPeriod,
       "gs2310PortSecLimitCtrlTable": gs2310PortSecLimitCtrlTable,
       "gs2310PortSecLimitCtrlEntry": gs2310PortSecLimitCtrlEntry,
       "gs2310PortSecLimitCtrlPort": gs2310PortSecLimitCtrlPort,
       "gs2310PortSecLimitCtrlPortMode": gs2310PortSecLimitCtrlPortMode,
       "gs2310PortSecLimitCtrlPortLimit": gs2310PortSecLimitCtrlPortLimit,
       "gs2310PortSecLimitCtrlPortAction": gs2310PortSecLimitCtrlPortAction,
       "gs2310PortSecLimitCtrlPortState": gs2310PortSecLimitCtrlPortState,
       "gs2310PortSecLimitCtrlPortReOpen": gs2310PortSecLimitCtrlPortReOpen,
       "gs2310PortSecSwitchStatusTable": gs2310PortSecSwitchStatusTable,
       "gs2310PortSecSwitchStatusEntry": gs2310PortSecSwitchStatusEntry,
       "gs2310PortSecSwitchStatusPort": gs2310PortSecSwitchStatusPort,
       "gs2310PortSecSwitchStatusUsers": gs2310PortSecSwitchStatusUsers,
       "gs2310PortSecSwitchStatusState": gs2310PortSecSwitchStatusState,
       "gs2310PortSecSwitchStatusMACCountCurrent": gs2310PortSecSwitchStatusMACCountCurrent,
       "gs2310PortSecSwitchStatusMACCountLimit": gs2310PortSecSwitchStatusMACCountLimit,
       "gs2310PortSecPortStatus": gs2310PortSecPortStatus,
       "gs2310PortSecPortStatusPort": gs2310PortSecPortStatusPort,
       "gs2310PortSecPortStatusTable": gs2310PortSecPortStatusTable,
       "gs2310PortSecPortStatusEntry": gs2310PortSecPortStatusEntry,
       "gs2310PortSecPortStatusIndex": gs2310PortSecPortStatusIndex,
       "gs2310PortSecPortStatusMACAddress": gs2310PortSecPortStatusMACAddress,
       "gs2310PortSecPortStatusVLANId": gs2310PortSecPortStatusVLANId,
       "gs2310PortSecPortStatusState": gs2310PortSecPortStatusState,
       "gs2310PortSecPortStatusTimeOfAddition": gs2310PortSecPortStatusTimeOfAddition,
       "gs2310PortSecPortStatusAgeAndHold": gs2310PortSecPortStatusAgeAndHold,
       "gs2310AccessManagement": gs2310AccessManagement,
       "gs2310AccessMgtConf": gs2310AccessMgtConf,
       "gs2310AccessMgtConfMode": gs2310AccessMgtConfMode,
       "gs2310AccessMgtConfCreate": gs2310AccessMgtConfCreate,
       "gs2310AccessMgtConfTable": gs2310AccessMgtConfTable,
       "gs2310AccessMgtConfEntry": gs2310AccessMgtConfEntry,
       "gs2310AccessMgtIndex": gs2310AccessMgtIndex,
       "gs2310AccessMgtAddresstype": gs2310AccessMgtAddresstype,
       "gs2310AccessMgtStartIpAddress": gs2310AccessMgtStartIpAddress,
       "gs2310AccessMgtEndIpAddress": gs2310AccessMgtEndIpAddress,
       "gs2310AccessMgtHttpHttps": gs2310AccessMgtHttpHttps,
       "gs2310AccessMgtSNMP": gs2310AccessMgtSNMP,
       "gs2310AccessMgtTelnetSSH": gs2310AccessMgtTelnetSSH,
       "gs2310AccessMgtRowStatus": gs2310AccessMgtRowStatus,
       "gs2310AccessMgtStatistics": gs2310AccessMgtStatistics,
       "gs2310HttpReceivedPkts": gs2310HttpReceivedPkts,
       "gs2310HttpAllowedPkts": gs2310HttpAllowedPkts,
       "gs2310HttpDiscardedPkts": gs2310HttpDiscardedPkts,
       "gs2310HttpsReceivedPkts": gs2310HttpsReceivedPkts,
       "gs2310HttpsAllowedPkts": gs2310HttpsAllowedPkts,
       "gs2310HttpsDiscardedPkts": gs2310HttpsDiscardedPkts,
       "gs2310SnmpReceivedPkts": gs2310SnmpReceivedPkts,
       "gs2310SnmpAllowedPkts": gs2310SnmpAllowedPkts,
       "gs2310SnmpDiscardedPkts": gs2310SnmpDiscardedPkts,
       "gs2310TelnetReceivedPkts": gs2310TelnetReceivedPkts,
       "gs2310TelnetAllowedPkts": gs2310TelnetAllowedPkts,
       "gs2310TelnetDiscardedPkts": gs2310TelnetDiscardedPkts,
       "gs2310SSHReceivedPkts": gs2310SSHReceivedPkts,
       "gs2310SSHAllowedPkts": gs2310SSHAllowedPkts,
       "gs2310SSHDiscardedPkts": gs2310SSHDiscardedPkts,
       "gs2310AccessMgtStatisticsClearAll": gs2310AccessMgtStatisticsClearAll,
       "gs2310SSH": gs2310SSH,
       "gs2310SSHMode": gs2310SSHMode,
       "gs2310HTTPS": gs2310HTTPS,
       "gs2310HTTPSMode": gs2310HTTPSMode,
       "gs2310HTTPSAutoRedirect": gs2310HTTPSAutoRedirect,
       "gs2310HTTPSCertRenew": gs2310HTTPSCertRenew,
       "gs2310HTTPSMinProtoVersion": gs2310HTTPSMinProtoVersion,
       "gs2310HTTPMode": gs2310HTTPMode,
       "gs2310AuthMethod": gs2310AuthMethod,
       "gs2310ConsoleAuthMethod": gs2310ConsoleAuthMethod,
       "gs2310ConsoleFallback": gs2310ConsoleFallback,
       "gs2310TelnetAuthMethod": gs2310TelnetAuthMethod,
       "gs2310TelnetFallback": gs2310TelnetFallback,
       "gs2310SshAuthMethod": gs2310SshAuthMethod,
       "gs2310SshFallback": gs2310SshFallback,
       "gs2310TftpAuthMethod": gs2310TftpAuthMethod,
       "gs2310TftpFallback": gs2310TftpFallback,
       "gs2310LoginFailures": gs2310LoginFailures,
       "gs2310LockMinutes": gs2310LockMinutes,
       "gs2310HttpAuthMethod": gs2310HttpAuthMethod,
       "gs2310HttpFallback": gs2310HttpFallback,
       "gs2310HttpsAuthMethod": gs2310HttpsAuthMethod,
       "gs2310HttpsFallback": gs2310HttpsFallback,
       "gs2310AAA": gs2310AAA,
       "gs2310AAACommonServer": gs2310AAACommonServer,
       "gs2310AAACommonServerTimeout": gs2310AAACommonServerTimeout,
       "gs2310AAACommonServerDeadTime": gs2310AAACommonServerDeadTime,
       "gs2310AAATACACSPlusAuthAndAccounting": gs2310AAATACACSPlusAuthAndAccounting,
       "gs2310AAAAuthorization": gs2310AAAAuthorization,
       "gs2310AAAFallbackToLocalAuthorization": gs2310AAAFallbackToLocalAuthorization,
       "gs2310AAAAccounting": gs2310AAAAccounting,
       "gs2310RADIUSAuthenticationServerTable": gs2310RADIUSAuthenticationServerTable,
       "gs2310RADIUSAuthenticationServerEntry": gs2310RADIUSAuthenticationServerEntry,
       "gs2310RADIUSAuthenticationServerIndex": gs2310RADIUSAuthenticationServerIndex,
       "gs2310RADIUSAuthenticationServerEnable": gs2310RADIUSAuthenticationServerEnable,
       "gs2310RADIUSAuthenticationServerIP": gs2310RADIUSAuthenticationServerIP,
       "gs2310RADIUSAuthenticationServerPort": gs2310RADIUSAuthenticationServerPort,
       "gs2310RADIUSAuthenticationServerSecret": gs2310RADIUSAuthenticationServerSecret,
       "gs2310RADIUSAccountingServerTable": gs2310RADIUSAccountingServerTable,
       "gs2310RADIUSAccountingServerEntry": gs2310RADIUSAccountingServerEntry,
       "gs2310RADIUSAccountingServerIndex": gs2310RADIUSAccountingServerIndex,
       "gs2310RADIUSAccountingServerEnable": gs2310RADIUSAccountingServerEnable,
       "gs2310RADIUSAccountingServerIP": gs2310RADIUSAccountingServerIP,
       "gs2310RADIUSAccountingServerPort": gs2310RADIUSAccountingServerPort,
       "gs2310RADIUSAccountingServerSecret": gs2310RADIUSAccountingServerSecret,
       "gs2310TACACSPlusAuthenticationServerTable": gs2310TACACSPlusAuthenticationServerTable,
       "gs2310TACACSPlusAuthenticationServerEntry": gs2310TACACSPlusAuthenticationServerEntry,
       "gs2310TACACSPlusAuthenticationServerIndex": gs2310TACACSPlusAuthenticationServerIndex,
       "gs2310TACACSPlusAuthenticationServerEnable": gs2310TACACSPlusAuthenticationServerEnable,
       "gs2310TACACSPlusAuthenticationServerIP": gs2310TACACSPlusAuthenticationServerIP,
       "gs2310TACACSPlusAuthenticationServerPort": gs2310TACACSPlusAuthenticationServerPort,
       "gs2310TACACSPlusAuthenticationServerSecret": gs2310TACACSPlusAuthenticationServerSecret,
       "gs2310RADIUSStatisticsTable": gs2310RADIUSStatisticsTable,
       "gs2310RADIUSStatisticsEntry": gs2310RADIUSStatisticsEntry,
       "gs2310RADIUSAuthStatisticsServerIndex": gs2310RADIUSAuthStatisticsServerIndex,
       "gs2310RADIUSAuthStatisticsRecPktAccessAccepts": gs2310RADIUSAuthStatisticsRecPktAccessAccepts,
       "gs2310RADIUSAuthStatisticsRecPktAccessRejects": gs2310RADIUSAuthStatisticsRecPktAccessRejects,
       "gs2310RADIUSAuthStatisticsRecPktAccessChallenges": gs2310RADIUSAuthStatisticsRecPktAccessChallenges,
       "gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses": gs2310RADIUSAuthStatisticsRecPktMalformedAccResponses,
       "gs2310RADIUSAuthStatisticsRecPktBadAuthenticators": gs2310RADIUSAuthStatisticsRecPktBadAuthenticators,
       "gs2310RADIUSAuthStatisticsRecPktUnknownTypes": gs2310RADIUSAuthStatisticsRecPktUnknownTypes,
       "gs2310RADIUSAuthStatisticsRecPktDropped": gs2310RADIUSAuthStatisticsRecPktDropped,
       "gs2310RADIUSAuthStatisticsTransmitPktAccessRequests": gs2310RADIUSAuthStatisticsTransmitPktAccessRequests,
       "gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions": gs2310RADIUSAuthStatisticsTransmitPktAccessRetransmissions,
       "gs2310RADIUSAuthStatisticsTransmitPktPendingRequests": gs2310RADIUSAuthStatisticsTransmitPktPendingRequests,
       "gs2310RADIUSAuthStatisticsTransmitPktTimeouts": gs2310RADIUSAuthStatisticsTransmitPktTimeouts,
       "gs2310RADIUSAuthIP": gs2310RADIUSAuthIP,
       "gs2310RADIUSAuthState": gs2310RADIUSAuthState,
       "gs2310RADIUSAuthRoundTripTime": gs2310RADIUSAuthRoundTripTime,
       "gs2310RADIUSAccountingStatisticsRecPktResponses": gs2310RADIUSAccountingStatisticsRecPktResponses,
       "gs2310RADIUSAccountingStatisticsRecPktMalformedResponses": gs2310RADIUSAccountingStatisticsRecPktMalformedResponses,
       "gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators": gs2310RADIUSAccountingStatisticsRecPktBadAuthenticators,
       "gs2310RADIUSAccountingStatisticsRecPktUnknownTypes": gs2310RADIUSAccountingStatisticsRecPktUnknownTypes,
       "gs2310RADIUSAccountingStatisticsRecPktDropped": gs2310RADIUSAccountingStatisticsRecPktDropped,
       "gs2310RADIUSAccountingStatisticsTransmitPktRequests": gs2310RADIUSAccountingStatisticsTransmitPktRequests,
       "gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions": gs2310RADIUSAccountingStatisticsTransmitPktRetransmissions,
       "gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests": gs2310RADIUSAccountingStatisticsTransmitPktPendingRequests,
       "gs2310RADIUSAccountingStatisticsTransmitPktTimeouts": gs2310RADIUSAccountingStatisticsTransmitPktTimeouts,
       "gs2310RADIUSAccountingIP": gs2310RADIUSAccountingIP,
       "gs2310RADIUSAccountingState": gs2310RADIUSAccountingState,
       "gs2310RADIUSAccountingRoundTripTime": gs2310RADIUSAccountingRoundTripTime,
       "gs2310RADIUSStatisticsClear": gs2310RADIUSStatisticsClear,
       "gs2310NAS": gs2310NAS,
       "gs2310NASConfiguration": gs2310NASConfiguration,
       "gs2310NASConfigMode": gs2310NASConfigMode,
       "gs2310NASConfigReauthEnabled": gs2310NASConfigReauthEnabled,
       "gs2310NASConfigReauthPeriod": gs2310NASConfigReauthPeriod,
       "gs2310NASConfigEAPOLTimeout": gs2310NASConfigEAPOLTimeout,
       "gs2310NASConfigAgingPeriod": gs2310NASConfigAgingPeriod,
       "gs2310NASConfigHoldTime": gs2310NASConfigHoldTime,
       "gs2310NASConfigRADIUSAssignedQoSEnabled": gs2310NASConfigRADIUSAssignedQoSEnabled,
       "gs2310NASConfigRADIUSAssignedVLANEnabled": gs2310NASConfigRADIUSAssignedVLANEnabled,
       "gs2310NASConfigGuestVLANEnabled": gs2310NASConfigGuestVLANEnabled,
       "gs2310NASConfigGuestVLANID": gs2310NASConfigGuestVLANID,
       "gs2310NASConfigMaxReauthCount": gs2310NASConfigMaxReauthCount,
       "gs2310NASConfigAllowGuestVLANEAPOLSeen": gs2310NASConfigAllowGuestVLANEAPOLSeen,
       "gs2310NASPortConfigTable": gs2310NASPortConfigTable,
       "gs2310NASPortConfigEntry": gs2310NASPortConfigEntry,
       "gs2310NASPortConfigPort": gs2310NASPortConfigPort,
       "gs2310NASPortConfigAdminState": gs2310NASPortConfigAdminState,
       "gs2310NASPortConfigRADIUSAssignedQoSEnabled": gs2310NASPortConfigRADIUSAssignedQoSEnabled,
       "gs2310NASPortConfigRADIUSAssignedVLANEnabled": gs2310NASPortConfigRADIUSAssignedVLANEnabled,
       "gs2310NASPortConfigGuestVLANEnabled": gs2310NASPortConfigGuestVLANEnabled,
       "gs2310NASPortConfigPortState": gs2310NASPortConfigPortState,
       "gs2310NASPortConfigReauthenticate": gs2310NASPortConfigReauthenticate,
       "gs2310NASPortConfigReinitialize": gs2310NASPortConfigReinitialize,
       "gs2310NASPortConfigFallbackEnabled": gs2310NASPortConfigFallbackEnabled,
       "gs2310NASConfigMacBasedUseEAP": gs2310NASConfigMacBasedUseEAP,
       "gs2310NASSwitchStatusTable": gs2310NASSwitchStatusTable,
       "gs2310NASSwitchStatusEntry": gs2310NASSwitchStatusEntry,
       "gs2310NASSwitchStatusAdminState": gs2310NASSwitchStatusAdminState,
       "gs2310NASSwitchStatusPortState": gs2310NASSwitchStatusPortState,
       "gs2310NASSwitchStatusLastSource": gs2310NASSwitchStatusLastSource,
       "gs2310NASSwitchStatusLastID": gs2310NASSwitchStatusLastID,
       "gs2310NASSwitchStatusQoSClass": gs2310NASSwitchStatusQoSClass,
       "gs2310NASSwitchStatusPortVlanID": gs2310NASSwitchStatusPortVlanID,
       "gs2310NASPortStatus": gs2310NASPortStatus,
       "gs2310NASPortStatusCountersTable": gs2310NASPortStatusCountersTable,
       "gs2310NASPortStatusCountersEntry": gs2310NASPortStatusCountersEntry,
       "gs2310NASRxCountersEAPOLTotal": gs2310NASRxCountersEAPOLTotal,
       "gs2310NASRxCountersEAPOLResponseID": gs2310NASRxCountersEAPOLResponseID,
       "gs2310NASRxCountersEAPOLResponses": gs2310NASRxCountersEAPOLResponses,
       "gs2310NASRxCountersEAPOLStart": gs2310NASRxCountersEAPOLStart,
       "gs2310NASRxCountersEAPOLLogoff": gs2310NASRxCountersEAPOLLogoff,
       "gs2310NASRxCountersEAPOLInvalidType": gs2310NASRxCountersEAPOLInvalidType,
       "gs2310NASRxCountersEAPOLInvalidLength": gs2310NASRxCountersEAPOLInvalidLength,
       "gs2310NASTxCountersEAPOLTotal": gs2310NASTxCountersEAPOLTotal,
       "gs2310NASTxCountersEAPOLRequestID": gs2310NASTxCountersEAPOLRequestID,
       "gs2310NASTxCountersEAPOLRequests": gs2310NASTxCountersEAPOLRequests,
       "gs2310NASRxBackendServerCountersAccessChallenges": gs2310NASRxBackendServerCountersAccessChallenges,
       "gs2310NASRxBackendServerCountersOtherRequests": gs2310NASRxBackendServerCountersOtherRequests,
       "gs2310NASRxBackendServerCountersAuthSuccesses": gs2310NASRxBackendServerCountersAuthSuccesses,
       "gs2310NASRxBackendServerCountersAuthFailures": gs2310NASRxBackendServerCountersAuthFailures,
       "gs2310NASTxBackendServerCountersResponses": gs2310NASTxBackendServerCountersResponses,
       "gs2310NASLastSupplicantInfoMACAddress": gs2310NASLastSupplicantInfoMACAddress,
       "gs2310NASLastSupplicantInfoVlanID": gs2310NASLastSupplicantInfoVlanID,
       "gs2310NASLastSupplicantInfoVersion": gs2310NASLastSupplicantInfoVersion,
       "gs2310NASLastSupplicantInfoIdentity": gs2310NASLastSupplicantInfoIdentity,
       "gs2310NASCountersDoClear": gs2310NASCountersDoClear,
       "gs2310NASPortStatusClientsTable": gs2310NASPortStatusClientsTable,
       "gs2310NASPortStatusClientsEntry": gs2310NASPortStatusClientsEntry,
       "gs2310NASClientsIndex": gs2310NASClientsIndex,
       "gs2310NASClientsIdentity": gs2310NASClientsIdentity,
       "gs2310NASClientsMACAddress": gs2310NASClientsMACAddress,
       "gs2310NASClientsVlanID": gs2310NASClientsVlanID,
       "gs2310NASClientsState": gs2310NASClientsState,
       "gs2310NASClientsLastAuth": gs2310NASClientsLastAuth,
       "gs2310NASRxClientsEAPOLTotal": gs2310NASRxClientsEAPOLTotal,
       "gs2310NASRxClientsEAPOLResponseID": gs2310NASRxClientsEAPOLResponseID,
       "gs2310NASRxClientsEAPOLResponses": gs2310NASRxClientsEAPOLResponses,
       "gs2310NASRxClientsEAPOLStart": gs2310NASRxClientsEAPOLStart,
       "gs2310NASRxClientsEAPOLLogoff": gs2310NASRxClientsEAPOLLogoff,
       "gs2310NASRxClientsEAPOLInvalidType": gs2310NASRxClientsEAPOLInvalidType,
       "gs2310NASRxClientsEAPOLInvalidLength": gs2310NASRxClientsEAPOLInvalidLength,
       "gs2310NASTxClientsEAPOLTotal": gs2310NASTxClientsEAPOLTotal,
       "gs2310NASTxClientsEAPOLRequestID": gs2310NASTxClientsEAPOLRequestID,
       "gs2310NASTxClientsEAPOLRequests": gs2310NASTxClientsEAPOLRequests,
       "gs2310NASRxBackendServerClientsAccessChallenges": gs2310NASRxBackendServerClientsAccessChallenges,
       "gs2310NASRxBackendServerClientsOtherRequests": gs2310NASRxBackendServerClientsOtherRequests,
       "gs2310NASRxBackendServerClientsAuthSuccesses": gs2310NASRxBackendServerClientsAuthSuccesses,
       "gs2310NASRxBackendServerClientsAuthFailures": gs2310NASRxBackendServerClientsAuthFailures,
       "gs2310NASTxBackendServerClientsResponses": gs2310NASTxBackendServerClientsResponses,
       "gs2310Maintenance": gs2310Maintenance,
       "gs2310RestartDevice": gs2310RestartDevice,
       "gs2310Firmware": gs2310Firmware,
       "gs2310FirmwareIpAddress": gs2310FirmwareIpAddress,
       "gs2310FirmwareFileName": gs2310FirmwareFileName,
       "gs2310DoFirmwareUpgrade": gs2310DoFirmwareUpgrade,
       "gs2310SaveOrRestore": gs2310SaveOrRestore,
       "gs2310FactoryDefaults": gs2310FactoryDefaults,
       "gs2310SaveStart": gs2310SaveStart,
       "gs2310SaveUser": gs2310SaveUser,
       "gs2310RestoreUser": gs2310RestoreUser,
       "gs2310ExportOrImport": gs2310ExportOrImport,
       "gs2310ExportIpAddress": gs2310ExportIpAddress,
       "gs2310ExportConfigName": gs2310ExportConfigName,
       "gs2310DoExportConfig": gs2310DoExportConfig,
       "gs2310ImportIpAddress": gs2310ImportIpAddress,
       "gs2310ImportConfigName": gs2310ImportConfigName,
       "gs2310DoImportConfig": gs2310DoImportConfig,
       "gs2310Diagnostics": gs2310Diagnostics,
       "gs2310PingIpAddress": gs2310PingIpAddress,
       "gs2310PingSize": gs2310PingSize,
       "gs2310DoPingConfig": gs2310DoPingConfig,
       "gs2310PingResult": gs2310PingResult,
       "gs2310Ping6IpAddress": gs2310Ping6IpAddress,
       "gs2310Ping6Size": gs2310Ping6Size,
       "gs2310DoPing6Config": gs2310DoPing6Config,
       "gs2310Ping6Result": gs2310Ping6Result,
       "gs2310ColdRestartDevice": gs2310ColdRestartDevice,
       "gs2310Trap": gs2310Trap,
       "gs2310TrapEvent": gs2310TrapEvent,
       "gs2310Emergency": gs2310Emergency,
       "gs2310Alert": gs2310Alert,
       "gs2310Critical": gs2310Critical,
       "gs2310Error": gs2310Error,
       "gs2310Warning": gs2310Warning,
       "gs2310Notice": gs2310Notice,
       "gs2310Informational": gs2310Informational,
       "gs2310Debug": gs2310Debug,
       "gs2310TrapVariable": gs2310TrapVariable,
       "gs2310Information": gs2310Information}
)
