# SNMP MIB module (LANCOM-GS-2326-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-GS-2326-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:47 2025
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
_LancomGS2326_ObjectIdentity = ObjectIdentity
lancomGS2326 = _LancomGS2326_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326)
)
_Gs2326System_ObjectIdentity = ObjectIdentity
gs2326System = _Gs2326System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1)
)
_Gs2326SystemInformation_ObjectIdentity = ObjectIdentity
gs2326SystemInformation = _Gs2326SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1)
)
_Gs2326ModelName_Type = DisplayString
_Gs2326ModelName_Object = MibScalar
gs2326ModelName = _Gs2326ModelName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 1),
    _Gs2326ModelName_Type()
)
gs2326ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ModelName.setStatus("current")
_Gs2326BIOSVersion_Type = DisplayString
_Gs2326BIOSVersion_Object = MibScalar
gs2326BIOSVersion = _Gs2326BIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 2),
    _Gs2326BIOSVersion_Type()
)
gs2326BIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326BIOSVersion.setStatus("current")
_Gs2326FirmwareVersion_Type = DisplayString
_Gs2326FirmwareVersion_Object = MibScalar
gs2326FirmwareVersion = _Gs2326FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 3),
    _Gs2326FirmwareVersion_Type()
)
gs2326FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326FirmwareVersion.setStatus("current")
_Gs2326HardwareMechanicalVersion_Type = DisplayString
_Gs2326HardwareMechanicalVersion_Object = MibScalar
gs2326HardwareMechanicalVersion = _Gs2326HardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 4),
    _Gs2326HardwareMechanicalVersion_Type()
)
gs2326HardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HardwareMechanicalVersion.setStatus("current")
_Gs2326SerialNumber_Type = DisplayString
_Gs2326SerialNumber_Object = MibScalar
gs2326SerialNumber = _Gs2326SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 5),
    _Gs2326SerialNumber_Type()
)
gs2326SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SerialNumber.setStatus("current")
_Gs2326HostMACAddress_Type = MacAddress
_Gs2326HostMACAddress_Object = MibScalar
gs2326HostMACAddress = _Gs2326HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 6),
    _Gs2326HostMACAddress_Type()
)
gs2326HostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HostMACAddress.setStatus("current")
_Gs2326ConsoleBaudrate_Type = DisplayString
_Gs2326ConsoleBaudrate_Object = MibScalar
gs2326ConsoleBaudrate = _Gs2326ConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 7),
    _Gs2326ConsoleBaudrate_Type()
)
gs2326ConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ConsoleBaudrate.setStatus("current")
_Gs2326RAMSize_Type = DisplayString
_Gs2326RAMSize_Object = MibScalar
gs2326RAMSize = _Gs2326RAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 8),
    _Gs2326RAMSize_Type()
)
gs2326RAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RAMSize.setStatus("current")
_Gs2326FlashSize_Type = DisplayString
_Gs2326FlashSize_Object = MibScalar
gs2326FlashSize = _Gs2326FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 9),
    _Gs2326FlashSize_Type()
)
gs2326FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326FlashSize.setStatus("current")
_Gs2326BridgeFDBSize_Type = DisplayString
_Gs2326BridgeFDBSize_Object = MibScalar
gs2326BridgeFDBSize = _Gs2326BridgeFDBSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 10),
    _Gs2326BridgeFDBSize_Type()
)
gs2326BridgeFDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326BridgeFDBSize.setStatus("current")
_Gs2326TransmitQueue_Type = DisplayString
_Gs2326TransmitQueue_Object = MibScalar
gs2326TransmitQueue = _Gs2326TransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 11),
    _Gs2326TransmitQueue_Type()
)
gs2326TransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326TransmitQueue.setStatus("current")
_Gs2326MaximumFrameSize_Type = DisplayString
_Gs2326MaximumFrameSize_Object = MibScalar
gs2326MaximumFrameSize = _Gs2326MaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 12),
    _Gs2326MaximumFrameSize_Type()
)
gs2326MaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MaximumFrameSize.setStatus("current")
_Gs2326CPULoad_Type = DisplayString
_Gs2326CPULoad_Object = MibScalar
gs2326CPULoad = _Gs2326CPULoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 13),
    _Gs2326CPULoad_Type()
)
gs2326CPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CPULoad.setStatus("current")
_Gs2326SystemDescription_Type = DisplayString
_Gs2326SystemDescription_Object = MibScalar
gs2326SystemDescription = _Gs2326SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 21),
    _Gs2326SystemDescription_Type()
)
gs2326SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SystemDescription.setStatus("current")
_Gs2326Location_Type = DisplayString
_Gs2326Location_Object = MibScalar
gs2326Location = _Gs2326Location_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 22),
    _Gs2326Location_Type()
)
gs2326Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Location.setStatus("current")
_Gs2326Contact_Type = DisplayString
_Gs2326Contact_Object = MibScalar
gs2326Contact = _Gs2326Contact_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 23),
    _Gs2326Contact_Type()
)
gs2326Contact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Contact.setStatus("current")
_Gs2326DeviceName_Type = DisplayString
_Gs2326DeviceName_Object = MibScalar
gs2326DeviceName = _Gs2326DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 24),
    _Gs2326DeviceName_Type()
)
gs2326DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DeviceName.setStatus("current")
_Gs2326SystemDate_Type = DisplayString
_Gs2326SystemDate_Object = MibScalar
gs2326SystemDate = _Gs2326SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 25),
    _Gs2326SystemDate_Type()
)
gs2326SystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SystemDate.setStatus("current")
_Gs2326SystemUptime_Type = DisplayString
_Gs2326SystemUptime_Object = MibScalar
gs2326SystemUptime = _Gs2326SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 26),
    _Gs2326SystemUptime_Type()
)
gs2326SystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SystemUptime.setStatus("current")
_Gs2326SystemIPv4Address_Type = DisplayString
_Gs2326SystemIPv4Address_Object = MibScalar
gs2326SystemIPv4Address = _Gs2326SystemIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 27),
    _Gs2326SystemIPv4Address_Type()
)
gs2326SystemIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SystemIPv4Address.setStatus("current")
_Gs2326SystemIPv4SubnetMask_Type = DisplayString
_Gs2326SystemIPv4SubnetMask_Object = MibScalar
gs2326SystemIPv4SubnetMask = _Gs2326SystemIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 28),
    _Gs2326SystemIPv4SubnetMask_Type()
)
gs2326SystemIPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SystemIPv4SubnetMask.setStatus("current")
_Gs2326SystemIPv4Gateway_Type = DisplayString
_Gs2326SystemIPv4Gateway_Object = MibScalar
gs2326SystemIPv4Gateway = _Gs2326SystemIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 29),
    _Gs2326SystemIPv4Gateway_Type()
)
gs2326SystemIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SystemIPv4Gateway.setStatus("current")
_Gs2326IPv6LinkLocalAddress_Type = DisplayString
_Gs2326IPv6LinkLocalAddress_Object = MibScalar
gs2326IPv6LinkLocalAddress = _Gs2326IPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 30),
    _Gs2326IPv6LinkLocalAddress_Type()
)
gs2326IPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv6LinkLocalAddress.setStatus("current")
_Gs2326IPv6Address_Type = DisplayString
_Gs2326IPv6Address_Object = MibScalar
gs2326IPv6Address = _Gs2326IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 31),
    _Gs2326IPv6Address_Type()
)
gs2326IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv6Address.setStatus("current")
_Gs2326IPv6Prefix_Type = DisplayString
_Gs2326IPv6Prefix_Object = MibScalar
gs2326IPv6Prefix = _Gs2326IPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 32),
    _Gs2326IPv6Prefix_Type()
)
gs2326IPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv6Prefix.setStatus("current")
_Gs2326IPv6Gateway_Type = DisplayString
_Gs2326IPv6Gateway_Object = MibScalar
gs2326IPv6Gateway = _Gs2326IPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 33),
    _Gs2326IPv6Gateway_Type()
)
gs2326IPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv6Gateway.setStatus("current")
_Gs2326LargestFreeMemBlock_Type = Integer32
_Gs2326LargestFreeMemBlock_Object = MibScalar
gs2326LargestFreeMemBlock = _Gs2326LargestFreeMemBlock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 1500),
    _Gs2326LargestFreeMemBlock_Type()
)
gs2326LargestFreeMemBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LargestFreeMemBlock.setStatus("current")
_Gs2326MemFree_Type = Integer32
_Gs2326MemFree_Object = MibScalar
gs2326MemFree = _Gs2326MemFree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 1, 1501),
    _Gs2326MemFree_Type()
)
gs2326MemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MemFree.setStatus("current")
_Gs2326SystemTime_ObjectIdentity = ObjectIdentity
gs2326SystemTime = _Gs2326SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2)
)
_Gs2326SystemTimeManual_ObjectIdentity = ObjectIdentity
gs2326SystemTimeManual = _Gs2326SystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1)
)


class _Gs2326SystemTimeManualClockSource_Type(Integer32):
    """Custom type gs2326SystemTimeManualClockSource based on Integer32"""
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


_Gs2326SystemTimeManualClockSource_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualClockSource_Object = MibScalar
gs2326SystemTimeManualClockSource = _Gs2326SystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 1),
    _Gs2326SystemTimeManualClockSource_Type()
)
gs2326SystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualClockSource.setStatus("current")
_Gs2326SystemTimeManualLocaltime_Type = DisplayString
_Gs2326SystemTimeManualLocaltime_Object = MibScalar
gs2326SystemTimeManualLocaltime = _Gs2326SystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 2),
    _Gs2326SystemTimeManualLocaltime_Type()
)
gs2326SystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualLocaltime.setStatus("current")


class _Gs2326SystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type gs2326SystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Gs2326SystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualTimeZoneOffset_Object = MibScalar
gs2326SystemTimeManualTimeZoneOffset = _Gs2326SystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 3),
    _Gs2326SystemTimeManualTimeZoneOffset_Type()
)
gs2326SystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualTimeZoneOffset.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326SystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavings_Object = MibScalar
gs2326SystemTimeManualDaylightSavings = _Gs2326SystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 4),
    _Gs2326SystemTimeManualDaylightSavings_Type()
)
gs2326SystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavings.setStatus("current")


class _Gs2326SystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type gs2326SystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Gs2326SystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualTimeSetOffset_Object = MibScalar
gs2326SystemTimeManualTimeSetOffset = _Gs2326SystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 5),
    _Gs2326SystemTimeManualTimeSetOffset_Type()
)
gs2326SystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualTimeSetOffset.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsType based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsType_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsType = _Gs2326SystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 6),
    _Gs2326SystemTimeManualDaylightSavingsType_Type()
)
gs2326SystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsType.setStatus("current")
_Gs2326SystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Gs2326SystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsBydatesFrom = _Gs2326SystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 7),
    _Gs2326SystemTimeManualDaylightSavingsBydatesFrom_Type()
)
gs2326SystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Gs2326SystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Gs2326SystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsBydatesTo = _Gs2326SystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 8),
    _Gs2326SystemTimeManualDaylightSavingsBydatesTo_Type()
)
gs2326SystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringDayFrom = _Gs2326SystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 9),
    _Gs2326SystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom = _Gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 10),
    _Gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom = _Gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 11),
    _Gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom = _Gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 12),
    _Gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringDayTo = _Gs2326SystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 13),
    _Gs2326SystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringWeekTo = _Gs2326SystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 14),
    _Gs2326SystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Gs2326SystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type gs2326SystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
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


_Gs2326SystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Gs2326SystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringMonthTo = _Gs2326SystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 15),
    _Gs2326SystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Gs2326SystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Gs2326SystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
gs2326SystemTimeManualDaylightSavingsRecurringTimeTo = _Gs2326SystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 1, 16),
    _Gs2326SystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
gs2326SystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Gs2326SystemTimeNTP_ObjectIdentity = ObjectIdentity
gs2326SystemTimeNTP = _Gs2326SystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2)
)
_Gs2326SystemTimeNTPTable_Object = MibTable
gs2326SystemTimeNTPTable = _Gs2326SystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPTable.setStatus("current")
_Gs2326SystemTimeNTPEntry_Object = MibTableRow
gs2326SystemTimeNTPEntry = _Gs2326SystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 1, 1)
)
gs2326SystemTimeNTPEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPEntry.setStatus("current")


class _Gs2326SystemTimeNTPIndex_Type(Integer32):
    """Custom type gs2326SystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2326SystemTimeNTPIndex_Type.__name__ = "Integer32"
_Gs2326SystemTimeNTPIndex_Object = MibTableColumn
gs2326SystemTimeNTPIndex = _Gs2326SystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 1, 1, 1),
    _Gs2326SystemTimeNTPIndex_Type()
)
gs2326SystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPIndex.setStatus("current")


class _Gs2326SystemTimeNTPServerIPType_Type(Integer32):
    """Custom type gs2326SystemTimeNTPServerIPType based on Integer32"""
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


_Gs2326SystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Gs2326SystemTimeNTPServerIPType_Object = MibTableColumn
gs2326SystemTimeNTPServerIPType = _Gs2326SystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 1, 1, 2),
    _Gs2326SystemTimeNTPServerIPType_Type()
)
gs2326SystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPServerIPType.setStatus("current")
_Gs2326SystemTimeNTPServer_Type = DisplayString
_Gs2326SystemTimeNTPServer_Object = MibTableColumn
gs2326SystemTimeNTPServer = _Gs2326SystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 1, 1, 3),
    _Gs2326SystemTimeNTPServer_Type()
)
gs2326SystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPServer.setStatus("current")


class _Gs2326SystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type gs2326SystemTimeNTPCurrentMode based on Integer32"""
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


_Gs2326SystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Gs2326SystemTimeNTPCurrentMode_Object = MibTableColumn
gs2326SystemTimeNTPCurrentMode = _Gs2326SystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 1, 1, 4),
    _Gs2326SystemTimeNTPCurrentMode_Type()
)
gs2326SystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPCurrentMode.setStatus("current")


class _Gs2326SystemTimeNTPRequestInterval_Type(Integer32):
    """Custom type gs2326SystemTimeNTPRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 999999999),
    )


_Gs2326SystemTimeNTPRequestInterval_Type.__name__ = "Integer32"
_Gs2326SystemTimeNTPRequestInterval_Object = MibScalar
gs2326SystemTimeNTPRequestInterval = _Gs2326SystemTimeNTPRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 2),
    _Gs2326SystemTimeNTPRequestInterval_Type()
)
gs2326SystemTimeNTPRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPRequestInterval.setStatus("current")


class _Gs2326SystemTimeNTPTriesNumber_Type(Integer32):
    """Custom type gs2326SystemTimeNTPTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_Gs2326SystemTimeNTPTriesNumber_Type.__name__ = "Integer32"
_Gs2326SystemTimeNTPTriesNumber_Object = MibScalar
gs2326SystemTimeNTPTriesNumber = _Gs2326SystemTimeNTPTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 2, 2, 3),
    _Gs2326SystemTimeNTPTriesNumber_Type()
)
gs2326SystemTimeNTPTriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemTimeNTPTriesNumber.setStatus("current")
_Gs2326SystemAccount_ObjectIdentity = ObjectIdentity
gs2326SystemAccount = _Gs2326SystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3)
)
_Gs2326SystemAccountUsers_ObjectIdentity = ObjectIdentity
gs2326SystemAccountUsers = _Gs2326SystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1)
)


class _Gs2326SystemAccountUserCreate_Type(Integer32):
    """Custom type gs2326SystemAccountUserCreate based on Integer32"""
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


_Gs2326SystemAccountUserCreate_Type.__name__ = "Integer32"
_Gs2326SystemAccountUserCreate_Object = MibScalar
gs2326SystemAccountUserCreate = _Gs2326SystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 1),
    _Gs2326SystemAccountUserCreate_Type()
)
gs2326SystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemAccountUserCreate.setStatus("current")
_Gs2326SystemAccountUsersTable_Object = MibTable
gs2326SystemAccountUsersTable = _Gs2326SystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326SystemAccountUsersTable.setStatus("current")
_Gs2326SystemAccountUsersEntry_Object = MibTableRow
gs2326SystemAccountUsersEntry = _Gs2326SystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2, 1)
)
gs2326SystemAccountUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326UserIndex"),
)
if mibBuilder.loadTexts:
    gs2326SystemAccountUsersEntry.setStatus("current")


class _Gs2326UserIndex_Type(Integer32):
    """Custom type gs2326UserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Gs2326UserIndex_Type.__name__ = "Integer32"
_Gs2326UserIndex_Object = MibTableColumn
gs2326UserIndex = _Gs2326UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2, 1, 1),
    _Gs2326UserIndex_Type()
)
gs2326UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326UserIndex.setStatus("current")


class _Gs2326UserName_Type(DisplayString):
    """Custom type gs2326UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326UserName_Type.__name__ = "DisplayString"
_Gs2326UserName_Object = MibTableColumn
gs2326UserName = _Gs2326UserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2, 1, 2),
    _Gs2326UserName_Type()
)
gs2326UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326UserName.setStatus("current")


class _Gs2326Password_Type(DisplayString):
    """Custom type gs2326Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326Password_Type.__name__ = "DisplayString"
_Gs2326Password_Object = MibTableColumn
gs2326Password = _Gs2326Password_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2, 1, 3),
    _Gs2326Password_Type()
)
gs2326Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Password.setStatus("current")


class _Gs2326UserPrivilegeLevel_Type(Integer32):
    """Custom type gs2326UserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326UserPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326UserPrivilegeLevel_Object = MibTableColumn
gs2326UserPrivilegeLevel = _Gs2326UserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2, 1, 4),
    _Gs2326UserPrivilegeLevel_Type()
)
gs2326UserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326UserPrivilegeLevel.setStatus("current")


class _Gs2326AccountUserRowStatus_Type(Integer32):
    """Custom type gs2326AccountUserRowStatus based on Integer32"""
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


_Gs2326AccountUserRowStatus_Type.__name__ = "Integer32"
_Gs2326AccountUserRowStatus_Object = MibTableColumn
gs2326AccountUserRowStatus = _Gs2326AccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 2, 1, 5),
    _Gs2326AccountUserRowStatus_Type()
)
gs2326AccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccountUserRowStatus.setStatus("current")


class _Gs2326SystemAccountUsersSuperUserPassword_Type(OctetString):
    """Custom type gs2326SystemAccountUsersSuperUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2326SystemAccountUsersSuperUserPassword_Type.__name__ = "OctetString"
_Gs2326SystemAccountUsersSuperUserPassword_Object = MibScalar
gs2326SystemAccountUsersSuperUserPassword = _Gs2326SystemAccountUsersSuperUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 1500),
    _Gs2326SystemAccountUsersSuperUserPassword_Type()
)
gs2326SystemAccountUsersSuperUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemAccountUsersSuperUserPassword.setStatus("current")


class _Gs2326SystemAccountEnforcePasswordRules_Type(Integer32):
    """Custom type gs2326SystemAccountEnforcePasswordRules based on Integer32"""
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


_Gs2326SystemAccountEnforcePasswordRules_Type.__name__ = "Integer32"
_Gs2326SystemAccountEnforcePasswordRules_Object = MibScalar
gs2326SystemAccountEnforcePasswordRules = _Gs2326SystemAccountEnforcePasswordRules_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 1, 1501),
    _Gs2326SystemAccountEnforcePasswordRules_Type()
)
gs2326SystemAccountEnforcePasswordRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemAccountEnforcePasswordRules.setStatus("current")
_Gs2326SystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
gs2326SystemAccountPrivilegeLevel = _Gs2326SystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2)
)


class _Gs2326AccountPrivilegeLevel_Type(Integer32):
    """Custom type gs2326AccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326AccountPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326AccountPrivilegeLevel_Object = MibScalar
gs2326AccountPrivilegeLevel = _Gs2326AccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 1),
    _Gs2326AccountPrivilegeLevel_Type()
)
gs2326AccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccountPrivilegeLevel.setStatus("current")


class _Gs2326AggregationPrivilegeLevel_Type(Integer32):
    """Custom type gs2326AggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326AggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326AggregationPrivilegeLevel_Object = MibScalar
gs2326AggregationPrivilegeLevel = _Gs2326AggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 2),
    _Gs2326AggregationPrivilegeLevel_Type()
)
gs2326AggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AggregationPrivilegeLevel.setStatus("current")


class _Gs2326DiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type gs2326DiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326DiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326DiagnosticsPrivilegeLevel_Object = MibScalar
gs2326DiagnosticsPrivilegeLevel = _Gs2326DiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 3),
    _Gs2326DiagnosticsPrivilegeLevel_Type()
)
gs2326DiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DiagnosticsPrivilegeLevel.setStatus("current")


class _Gs2326EEEPrivilegeLevel_Type(Integer32):
    """Custom type gs2326EEEPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326EEEPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326EEEPrivilegeLevel_Object = MibScalar
gs2326EEEPrivilegeLevel = _Gs2326EEEPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 4),
    _Gs2326EEEPrivilegeLevel_Type()
)
gs2326EEEPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326EEEPrivilegeLevel.setStatus("current")


class _Gs2326EasyportPrivilegeLevel_Type(Integer32):
    """Custom type gs2326EasyportPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326EasyportPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326EasyportPrivilegeLevel_Object = MibScalar
gs2326EasyportPrivilegeLevel = _Gs2326EasyportPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 9),
    _Gs2326EasyportPrivilegeLevel_Type()
)
gs2326EasyportPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326EasyportPrivilegeLevel.setStatus("current")


class _Gs2326GARPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326GARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326GARPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326GARPPrivilegeLevel_Object = MibScalar
gs2326GARPPrivilegeLevel = _Gs2326GARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 10),
    _Gs2326GARPPrivilegeLevel_Type()
)
gs2326GARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPPrivilegeLevel.setStatus("current")


class _Gs2326GVRPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326GVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326GVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326GVRPPrivilegeLevel_Object = MibScalar
gs2326GVRPPrivilegeLevel = _Gs2326GVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 11),
    _Gs2326GVRPPrivilegeLevel_Type()
)
gs2326GVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GVRPPrivilegeLevel.setStatus("current")


class _Gs2326IPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326IPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326IPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326IPPrivilegeLevel_Object = MibScalar
gs2326IPPrivilegeLevel = _Gs2326IPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 12),
    _Gs2326IPPrivilegeLevel_Type()
)
gs2326IPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPPrivilegeLevel.setStatus("current")


class _Gs2326IPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type gs2326IPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326IPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326IPMCSnoopingPrivilegeLevel_Object = MibScalar
gs2326IPMCSnoopingPrivilegeLevel = _Gs2326IPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 13),
    _Gs2326IPMCSnoopingPrivilegeLevel_Type()
)
gs2326IPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPMCSnoopingPrivilegeLevel.setStatus("current")


class _Gs2326LACPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326LACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326LACPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326LACPPrivilegeLevel_Object = MibScalar
gs2326LACPPrivilegeLevel = _Gs2326LACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 14),
    _Gs2326LACPPrivilegeLevel_Type()
)
gs2326LACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LACPPrivilegeLevel.setStatus("current")


class _Gs2326LLDPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326LLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326LLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326LLDPPrivilegeLevel_Object = MibScalar
gs2326LLDPPrivilegeLevel = _Gs2326LLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 15),
    _Gs2326LLDPPrivilegeLevel_Type()
)
gs2326LLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LLDPPrivilegeLevel.setStatus("current")


class _Gs2326LLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type gs2326LLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326LLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326LLDPMEDPrivilegeLevel_Object = MibScalar
gs2326LLDPMEDPrivilegeLevel = _Gs2326LLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 16),
    _Gs2326LLDPMEDPrivilegeLevel_Type()
)
gs2326LLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LLDPMEDPrivilegeLevel.setStatus("current")


class _Gs2326LoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type gs2326LoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326LoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326LoopProtectPrivilegeLevel_Object = MibScalar
gs2326LoopProtectPrivilegeLevel = _Gs2326LoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 17),
    _Gs2326LoopProtectPrivilegeLevel_Type()
)
gs2326LoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectPrivilegeLevel.setStatus("current")


class _Gs2326MACTablePrivilegeLevel_Type(Integer32):
    """Custom type gs2326MACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326MACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326MACTablePrivilegeLevel_Object = MibScalar
gs2326MACTablePrivilegeLevel = _Gs2326MACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 18),
    _Gs2326MACTablePrivilegeLevel_Type()
)
gs2326MACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACTablePrivilegeLevel.setStatus("current")


class _Gs2326MVRPrivilegeLevel_Type(Integer32):
    """Custom type gs2326MVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326MVRPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326MVRPrivilegeLevel_Object = MibScalar
gs2326MVRPrivilegeLevel = _Gs2326MVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 22),
    _Gs2326MVRPrivilegeLevel_Type()
)
gs2326MVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPrivilegeLevel.setStatus("current")


class _Gs2326MaintenancePrivilegeLevel_Type(Integer32):
    """Custom type gs2326MaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326MaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326MaintenancePrivilegeLevel_Object = MibScalar
gs2326MaintenancePrivilegeLevel = _Gs2326MaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 24),
    _Gs2326MaintenancePrivilegeLevel_Type()
)
gs2326MaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MaintenancePrivilegeLevel.setStatus("current")


class _Gs2326MirroringPrivilegeLevel_Type(Integer32):
    """Custom type gs2326MirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326MirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326MirroringPrivilegeLevel_Object = MibScalar
gs2326MirroringPrivilegeLevel = _Gs2326MirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 25),
    _Gs2326MirroringPrivilegeLevel_Type()
)
gs2326MirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MirroringPrivilegeLevel.setStatus("current")


class _Gs2326PortsPrivilegeLevel_Type(Integer32):
    """Custom type gs2326PortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326PortsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326PortsPrivilegeLevel_Object = MibScalar
gs2326PortsPrivilegeLevel = _Gs2326PortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 27),
    _Gs2326PortsPrivilegeLevel_Type()
)
gs2326PortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortsPrivilegeLevel.setStatus("current")


class _Gs2326PrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2326PrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326PrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326PrivateVLANsPrivilegeLevel_Object = MibScalar
gs2326PrivateVLANsPrivilegeLevel = _Gs2326PrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 28),
    _Gs2326PrivateVLANsPrivilegeLevel_Type()
)
gs2326PrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PrivateVLANsPrivilegeLevel.setStatus("current")


class _Gs2326QoSPrivilegeLevel_Type(Integer32):
    """Custom type gs2326QoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326QoSPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326QoSPrivilegeLevel_Object = MibScalar
gs2326QoSPrivilegeLevel = _Gs2326QoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 29),
    _Gs2326QoSPrivilegeLevel_Type()
)
gs2326QoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSPrivilegeLevel.setStatus("current")


class _Gs2326SFlowPrivilegeLevel_Type(Integer32):
    """Custom type gs2326SFlowPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SFlowPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SFlowPrivilegeLevel_Object = MibScalar
gs2326SFlowPrivilegeLevel = _Gs2326SFlowPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 30),
    _Gs2326SFlowPrivilegeLevel_Type()
)
gs2326SFlowPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SFlowPrivilegeLevel.setStatus("current")


class _Gs2326SMTPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326SMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SMTPPrivilegeLevel_Object = MibScalar
gs2326SMTPPrivilegeLevel = _Gs2326SMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 31),
    _Gs2326SMTPPrivilegeLevel_Type()
)
gs2326SMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPPrivilegeLevel.setStatus("current")


class _Gs2326SNMPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326SNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SNMPPrivilegeLevel_Object = MibScalar
gs2326SNMPPrivilegeLevel = _Gs2326SNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 32),
    _Gs2326SNMPPrivilegeLevel_Type()
)
gs2326SNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SNMPPrivilegeLevel.setStatus("current")


class _Gs2326SecurityPrivilegeLevel_Type(Integer32):
    """Custom type gs2326SecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SecurityPrivilegeLevel_Object = MibScalar
gs2326SecurityPrivilegeLevel = _Gs2326SecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 33),
    _Gs2326SecurityPrivilegeLevel_Type()
)
gs2326SecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SecurityPrivilegeLevel.setStatus("current")


class _Gs2326SingleIPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326SingleIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SingleIPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SingleIPPrivilegeLevel_Object = MibScalar
gs2326SingleIPPrivilegeLevel = _Gs2326SingleIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 34),
    _Gs2326SingleIPPrivilegeLevel_Type()
)
gs2326SingleIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SingleIPPrivilegeLevel.setStatus("current")


class _Gs2326SpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type gs2326SpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SpanningTreePrivilegeLevel_Object = MibScalar
gs2326SpanningTreePrivilegeLevel = _Gs2326SpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 35),
    _Gs2326SpanningTreePrivilegeLevel_Type()
)
gs2326SpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SpanningTreePrivilegeLevel.setStatus("current")


class _Gs2326SystemPrivilegeLevel_Type(Integer32):
    """Custom type gs2326SystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326SystemPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326SystemPrivilegeLevel_Object = MibScalar
gs2326SystemPrivilegeLevel = _Gs2326SystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 36),
    _Gs2326SystemPrivilegeLevel_Type()
)
gs2326SystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SystemPrivilegeLevel.setStatus("current")


class _Gs2326TrapEventPrivilegeLevel_Type(Integer32):
    """Custom type gs2326TrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326TrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326TrapEventPrivilegeLevel_Object = MibScalar
gs2326TrapEventPrivilegeLevel = _Gs2326TrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 37),
    _Gs2326TrapEventPrivilegeLevel_Type()
)
gs2326TrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventPrivilegeLevel.setStatus("current")


class _Gs2326UPnPPrivilegeLevel_Type(Integer32):
    """Custom type gs2326UPnPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326UPnPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326UPnPPrivilegeLevel_Object = MibScalar
gs2326UPnPPrivilegeLevel = _Gs2326UPnPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 38),
    _Gs2326UPnPPrivilegeLevel_Type()
)
gs2326UPnPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326UPnPPrivilegeLevel.setStatus("current")


class _Gs2326VCLPrivilegeLevel_Type(Integer32):
    """Custom type gs2326VCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326VCLPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326VCLPrivilegeLevel_Object = MibScalar
gs2326VCLPrivilegeLevel = _Gs2326VCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 39),
    _Gs2326VCLPrivilegeLevel_Type()
)
gs2326VCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VCLPrivilegeLevel.setStatus("current")


class _Gs2326VLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2326VLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326VLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326VLANsPrivilegeLevel_Object = MibScalar
gs2326VLANsPrivilegeLevel = _Gs2326VLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 41),
    _Gs2326VLANsPrivilegeLevel_Type()
)
gs2326VLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VLANsPrivilegeLevel.setStatus("current")


class _Gs2326VoiceVLANPrivilegeLevel_Type(Integer32):
    """Custom type gs2326VoiceVLANPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2326VoiceVLANPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2326VoiceVLANPrivilegeLevel_Object = MibScalar
gs2326VoiceVLANPrivilegeLevel = _Gs2326VoiceVLANPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 3, 2, 42),
    _Gs2326VoiceVLANPrivilegeLevel_Type()
)
gs2326VoiceVLANPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANPrivilegeLevel.setStatus("current")
_Gs2326IP_ObjectIdentity = ObjectIdentity
gs2326IP = _Gs2326IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4)
)
_Gs2326IPv4_ObjectIdentity = ObjectIdentity
gs2326IPv4 = _Gs2326IPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1)
)
_Gs2326IPv4Configured_ObjectIdentity = ObjectIdentity
gs2326IPv4Configured = _Gs2326IPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1)
)


class _Gs2326Ipv4DHCPClient_Type(Integer32):
    """Custom type gs2326Ipv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326Ipv4DHCPClient_Type.__name__ = "Integer32"
_Gs2326Ipv4DHCPClient_Object = MibScalar
gs2326Ipv4DHCPClient = _Gs2326Ipv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 1),
    _Gs2326Ipv4DHCPClient_Type()
)
gs2326Ipv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ipv4DHCPClient.setStatus("current")
_Gs2326IPv4Address_Type = IpAddress
_Gs2326IPv4Address_Object = MibScalar
gs2326IPv4Address = _Gs2326IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 2),
    _Gs2326IPv4Address_Type()
)
gs2326IPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPv4Address.setStatus("current")
_Gs2326IPv4Mask_Type = IpAddress
_Gs2326IPv4Mask_Object = MibScalar
gs2326IPv4Mask = _Gs2326IPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 3),
    _Gs2326IPv4Mask_Type()
)
gs2326IPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPv4Mask.setStatus("current")
_Gs2326IPv4Gateway_Type = IpAddress
_Gs2326IPv4Gateway_Object = MibScalar
gs2326IPv4Gateway = _Gs2326IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 4),
    _Gs2326IPv4Gateway_Type()
)
gs2326IPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPv4Gateway.setStatus("current")


class _Gs2326IPv4VLANId_Type(Integer32):
    """Custom type gs2326IPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326IPv4VLANId_Type.__name__ = "Integer32"
_Gs2326IPv4VLANId_Object = MibScalar
gs2326IPv4VLANId = _Gs2326IPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 5),
    _Gs2326IPv4VLANId_Type()
)
gs2326IPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPv4VLANId.setStatus("current")
_Gs2326IPv4DNSServer_Type = IpAddress
_Gs2326IPv4DNSServer_Object = MibScalar
gs2326IPv4DNSServer = _Gs2326IPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 6),
    _Gs2326IPv4DNSServer_Type()
)
gs2326IPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPv4DNSServer.setStatus("current")


class _Gs2326IPv4DNSProxy_Type(Integer32):
    """Custom type gs2326IPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IPv4DNSProxy_Type.__name__ = "Integer32"
_Gs2326IPv4DNSProxy_Object = MibScalar
gs2326IPv4DNSProxy = _Gs2326IPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 1, 7),
    _Gs2326IPv4DNSProxy_Type()
)
gs2326IPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPv4DNSProxy.setStatus("current")
_Gs2326IPv4Current_ObjectIdentity = ObjectIdentity
gs2326IPv4Current = _Gs2326IPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2)
)


class _Gs2326Ipv4CurrentDHCPClient_Type(Integer32):
    """Custom type gs2326Ipv4CurrentDHCPClient based on Integer32"""
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


_Gs2326Ipv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Gs2326Ipv4CurrentDHCPClient_Object = MibScalar
gs2326Ipv4CurrentDHCPClient = _Gs2326Ipv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2, 1),
    _Gs2326Ipv4CurrentDHCPClient_Type()
)
gs2326Ipv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ipv4CurrentDHCPClient.setStatus("current")
_Gs2326IPv4CurrentAddress_Type = IpAddress
_Gs2326IPv4CurrentAddress_Object = MibScalar
gs2326IPv4CurrentAddress = _Gs2326IPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2, 2),
    _Gs2326IPv4CurrentAddress_Type()
)
gs2326IPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv4CurrentAddress.setStatus("current")
_Gs2326IPv4CurrentMask_Type = IpAddress
_Gs2326IPv4CurrentMask_Object = MibScalar
gs2326IPv4CurrentMask = _Gs2326IPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2, 3),
    _Gs2326IPv4CurrentMask_Type()
)
gs2326IPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv4CurrentMask.setStatus("current")
_Gs2326IPv4CurrentGateway_Type = IpAddress
_Gs2326IPv4CurrentGateway_Object = MibScalar
gs2326IPv4CurrentGateway = _Gs2326IPv4CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2, 4),
    _Gs2326IPv4CurrentGateway_Type()
)
gs2326IPv4CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv4CurrentGateway.setStatus("current")


class _Gs2326IPv4CurrentVLANId_Type(Integer32):
    """Custom type gs2326IPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326IPv4CurrentVLANId_Type.__name__ = "Integer32"
_Gs2326IPv4CurrentVLANId_Object = MibScalar
gs2326IPv4CurrentVLANId = _Gs2326IPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2, 5),
    _Gs2326IPv4CurrentVLANId_Type()
)
gs2326IPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv4CurrentVLANId.setStatus("current")
_Gs2326IPv4CurrentDNSServer_Type = IpAddress
_Gs2326IPv4CurrentDNSServer_Object = MibScalar
gs2326IPv4CurrentDNSServer = _Gs2326IPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 1, 2, 6),
    _Gs2326IPv4CurrentDNSServer_Type()
)
gs2326IPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPv4CurrentDNSServer.setStatus("current")
_Gs2326IPv6_ObjectIdentity = ObjectIdentity
gs2326IPv6 = _Gs2326IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2)
)
_Gs2326IPv6Configured_ObjectIdentity = ObjectIdentity
gs2326IPv6Configured = _Gs2326IPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 1)
)


class _Gs2326Ipv6AutoConfiguration_Type(Integer32):
    """Custom type gs2326Ipv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326Ipv6AutoConfiguration_Type.__name__ = "Integer32"
_Gs2326Ipv6AutoConfiguration_Object = MibScalar
gs2326Ipv6AutoConfiguration = _Gs2326Ipv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 1, 1),
    _Gs2326Ipv6AutoConfiguration_Type()
)
gs2326Ipv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ipv6AutoConfiguration.setStatus("current")


class _Gs2326Ipv6Address_Type(DisplayString):
    """Custom type gs2326Ipv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2326Ipv6Address_Type.__name__ = "DisplayString"
_Gs2326Ipv6Address_Object = MibScalar
gs2326Ipv6Address = _Gs2326Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 1, 2),
    _Gs2326Ipv6Address_Type()
)
gs2326Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ipv6Address.setStatus("current")


class _Gs2326Ipv6Prefix_Type(Integer32):
    """Custom type gs2326Ipv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2326Ipv6Prefix_Type.__name__ = "Integer32"
_Gs2326Ipv6Prefix_Object = MibScalar
gs2326Ipv6Prefix = _Gs2326Ipv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 1, 3),
    _Gs2326Ipv6Prefix_Type()
)
gs2326Ipv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ipv6Prefix.setStatus("current")


class _Gs2326Ipv6Gateway_Type(DisplayString):
    """Custom type gs2326Ipv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2326Ipv6Gateway_Type.__name__ = "DisplayString"
_Gs2326Ipv6Gateway_Object = MibScalar
gs2326Ipv6Gateway = _Gs2326Ipv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 1, 4),
    _Gs2326Ipv6Gateway_Type()
)
gs2326Ipv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ipv6Gateway.setStatus("current")
_Gs2326IPv6Current_ObjectIdentity = ObjectIdentity
gs2326IPv6Current = _Gs2326IPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 2)
)


class _Gs2326Ipv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type gs2326Ipv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326Ipv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Gs2326Ipv6CurrentAutoConfiguration_Object = MibScalar
gs2326Ipv6CurrentAutoConfiguration = _Gs2326Ipv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 2, 1),
    _Gs2326Ipv6CurrentAutoConfiguration_Type()
)
gs2326Ipv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Ipv6CurrentAutoConfiguration.setStatus("current")


class _Gs2326Ipv6CurrentAddress_Type(DisplayString):
    """Custom type gs2326Ipv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2326Ipv6CurrentAddress_Type.__name__ = "DisplayString"
_Gs2326Ipv6CurrentAddress_Object = MibScalar
gs2326Ipv6CurrentAddress = _Gs2326Ipv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 2, 2),
    _Gs2326Ipv6CurrentAddress_Type()
)
gs2326Ipv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Ipv6CurrentAddress.setStatus("current")


class _Gs2326Ipv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type gs2326Ipv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2326Ipv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Gs2326Ipv6CurrentLinkLocalAddress_Object = MibScalar
gs2326Ipv6CurrentLinkLocalAddress = _Gs2326Ipv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 2, 3),
    _Gs2326Ipv6CurrentLinkLocalAddress_Type()
)
gs2326Ipv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Ipv6CurrentLinkLocalAddress.setStatus("current")


class _Gs2326Ipv6CurrentPrefix_Type(DisplayString):
    """Custom type gs2326Ipv6CurrentPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Gs2326Ipv6CurrentPrefix_Type.__name__ = "DisplayString"
_Gs2326Ipv6CurrentPrefix_Object = MibScalar
gs2326Ipv6CurrentPrefix = _Gs2326Ipv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 2, 4),
    _Gs2326Ipv6CurrentPrefix_Type()
)
gs2326Ipv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Ipv6CurrentPrefix.setStatus("current")


class _Gs2326Ipv6CurrentGateway_Type(DisplayString):
    """Custom type gs2326Ipv6CurrentGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2326Ipv6CurrentGateway_Type.__name__ = "DisplayString"
_Gs2326Ipv6CurrentGateway_Object = MibScalar
gs2326Ipv6CurrentGateway = _Gs2326Ipv6CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 4, 2, 2, 5),
    _Gs2326Ipv6CurrentGateway_Type()
)
gs2326Ipv6CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Ipv6CurrentGateway.setStatus("current")
_Gs2326Syslog_ObjectIdentity = ObjectIdentity
gs2326Syslog = _Gs2326Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5)
)
_Gs2326SyslogConf_ObjectIdentity = ObjectIdentity
gs2326SyslogConf = _Gs2326SyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 1)
)


class _Gs2326ServerMode_Type(Integer32):
    """Custom type gs2326ServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ServerMode_Type.__name__ = "Integer32"
_Gs2326ServerMode_Object = MibScalar
gs2326ServerMode = _Gs2326ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 1, 1),
    _Gs2326ServerMode_Type()
)
gs2326ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ServerMode.setStatus("current")
_Gs2326ServerAddress1_Type = IpAddress
_Gs2326ServerAddress1_Object = MibScalar
gs2326ServerAddress1 = _Gs2326ServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 1, 2),
    _Gs2326ServerAddress1_Type()
)
gs2326ServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ServerAddress1.setStatus("current")
_Gs2326ServerAddress2_Type = IpAddress
_Gs2326ServerAddress2_Object = MibScalar
gs2326ServerAddress2 = _Gs2326ServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 1, 3),
    _Gs2326ServerAddress2_Type()
)
gs2326ServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ServerAddress2.setStatus("current")


class _Gs2326SyslogLevel_Type(Integer32):
    """Custom type gs2326SyslogLevel based on Integer32"""
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


_Gs2326SyslogLevel_Type.__name__ = "Integer32"
_Gs2326SyslogLevel_Object = MibScalar
gs2326SyslogLevel = _Gs2326SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 1, 4),
    _Gs2326SyslogLevel_Type()
)
gs2326SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SyslogLevel.setStatus("current")
_Gs2326SyslogDetailedInfo_ObjectIdentity = ObjectIdentity
gs2326SyslogDetailedInfo = _Gs2326SyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2)
)


class _Gs2326SyslogDetailedInfoClear_Type(Integer32):
    """Custom type gs2326SyslogDetailedInfoClear based on Integer32"""
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


_Gs2326SyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Gs2326SyslogDetailedInfoClear_Object = MibScalar
gs2326SyslogDetailedInfoClear = _Gs2326SyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 1),
    _Gs2326SyslogDetailedInfoClear_Type()
)
gs2326SyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoClear.setStatus("current")
_Gs2326SyslogDetailedInfoTable_Object = MibTable
gs2326SyslogDetailedInfoTable = _Gs2326SyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoTable.setStatus("current")
_Gs2326SyslogDetailedInfoEntry_Object = MibTableRow
gs2326SyslogDetailedInfoEntry = _Gs2326SyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 2, 1)
)
gs2326SyslogDetailedInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoEntry.setStatus("current")


class _Gs2326SyslogDetailedInfoIndex_Type(Integer32):
    """Custom type gs2326SyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2326SyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Gs2326SyslogDetailedInfoIndex_Object = MibTableColumn
gs2326SyslogDetailedInfoIndex = _Gs2326SyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 2, 1, 1),
    _Gs2326SyslogDetailedInfoIndex_Type()
)
gs2326SyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoIndex.setStatus("current")
_Gs2326SyslogDetailedInfoLevel_Type = DisplayString
_Gs2326SyslogDetailedInfoLevel_Object = MibTableColumn
gs2326SyslogDetailedInfoLevel = _Gs2326SyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 2, 1, 2),
    _Gs2326SyslogDetailedInfoLevel_Type()
)
gs2326SyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoLevel.setStatus("current")


class _Gs2326SyslogDetailedInfoTime_Type(DisplayString):
    """Custom type gs2326SyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gs2326SyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Gs2326SyslogDetailedInfoTime_Object = MibTableColumn
gs2326SyslogDetailedInfoTime = _Gs2326SyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 2, 1, 3),
    _Gs2326SyslogDetailedInfoTime_Type()
)
gs2326SyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoTime.setStatus("current")
_Gs2326SyslogDetailedInfoMessage_Type = DisplayString
_Gs2326SyslogDetailedInfoMessage_Object = MibTableColumn
gs2326SyslogDetailedInfoMessage = _Gs2326SyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 5, 2, 2, 1, 4),
    _Gs2326SyslogDetailedInfoMessage_Type()
)
gs2326SyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SyslogDetailedInfoMessage.setStatus("current")
_Gs2326Snmp_ObjectIdentity = ObjectIdentity
gs2326Snmp = _Gs2326Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6)
)
_Gs2326SnmpConf_ObjectIdentity = ObjectIdentity
gs2326SnmpConf = _Gs2326SnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1)
)


class _Gs2326GetCommunityMode_Type(Integer32):
    """Custom type gs2326GetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326GetCommunityMode_Type.__name__ = "Integer32"
_Gs2326GetCommunityMode_Object = MibScalar
gs2326GetCommunityMode = _Gs2326GetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 1),
    _Gs2326GetCommunityMode_Type()
)
gs2326GetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GetCommunityMode.setStatus("current")
_Gs2326GetCommunity_Type = DisplayString
_Gs2326GetCommunity_Object = MibScalar
gs2326GetCommunity = _Gs2326GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 2),
    _Gs2326GetCommunity_Type()
)
gs2326GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GetCommunity.setStatus("current")


class _Gs2326SetCommunityMode_Type(Integer32):
    """Custom type gs2326SetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326SetCommunityMode_Type.__name__ = "Integer32"
_Gs2326SetCommunityMode_Object = MibScalar
gs2326SetCommunityMode = _Gs2326SetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 3),
    _Gs2326SetCommunityMode_Type()
)
gs2326SetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SetCommunityMode.setStatus("current")
_Gs2326SetCommunity_Type = DisplayString
_Gs2326SetCommunity_Object = MibScalar
gs2326SetCommunity = _Gs2326SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 4),
    _Gs2326SetCommunity_Type()
)
gs2326SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SetCommunity.setStatus("current")
_Gs2326GetCommunityConfTable_Object = MibTable
gs2326GetCommunityConfTable = _Gs2326GetCommunityConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    gs2326GetCommunityConfTable.setStatus("current")
_Gs2326GetCommunityConfEntry_Object = MibTableRow
gs2326GetCommunityConfEntry = _Gs2326GetCommunityConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 5, 1)
)
gs2326GetCommunityConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326CommunityConfIndex"),
)
if mibBuilder.loadTexts:
    gs2326GetCommunityConfEntry.setStatus("current")


class _Gs2326CommunityConfIndex_Type(Integer32):
    """Custom type gs2326CommunityConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326CommunityConfIndex_Type.__name__ = "Integer32"
_Gs2326CommunityConfIndex_Object = MibTableColumn
gs2326CommunityConfIndex = _Gs2326CommunityConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 5, 1, 1),
    _Gs2326CommunityConfIndex_Type()
)
gs2326CommunityConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326CommunityConfIndex.setStatus("current")
_Gs2326CommunityConfGetCommunity_Type = DisplayString
_Gs2326CommunityConfGetCommunity_Object = MibTableColumn
gs2326CommunityConfGetCommunity = _Gs2326CommunityConfGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 5, 1, 2),
    _Gs2326CommunityConfGetCommunity_Type()
)
gs2326CommunityConfGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326CommunityConfGetCommunity.setStatus("current")
_Gs2326TrapHostConfTable_Object = MibTable
gs2326TrapHostConfTable = _Gs2326TrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    gs2326TrapHostConfTable.setStatus("current")
_Gs2326TrapHostConfEntry_Object = MibTableRow
gs2326TrapHostConfEntry = _Gs2326TrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1)
)
gs2326TrapHostConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326TrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    gs2326TrapHostConfEntry.setStatus("current")


class _Gs2326TrapHostConfIndex_Type(Integer32):
    """Custom type gs2326TrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2326TrapHostConfIndex_Type.__name__ = "Integer32"
_Gs2326TrapHostConfIndex_Object = MibTableColumn
gs2326TrapHostConfIndex = _Gs2326TrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 1),
    _Gs2326TrapHostConfIndex_Type()
)
gs2326TrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326TrapHostConfIndex.setStatus("current")


class _Gs2326TrapHostConfVersion_Type(Integer32):
    """Custom type gs2326TrapHostConfVersion based on Integer32"""
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


_Gs2326TrapHostConfVersion_Type.__name__ = "Integer32"
_Gs2326TrapHostConfVersion_Object = MibTableColumn
gs2326TrapHostConfVersion = _Gs2326TrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 2),
    _Gs2326TrapHostConfVersion_Type()
)
gs2326TrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfVersion.setStatus("current")


class _Gs2326TrapHostConfIPType_Type(Integer32):
    """Custom type gs2326TrapHostConfIPType based on Integer32"""
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


_Gs2326TrapHostConfIPType_Type.__name__ = "Integer32"
_Gs2326TrapHostConfIPType_Object = MibTableColumn
gs2326TrapHostConfIPType = _Gs2326TrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 3),
    _Gs2326TrapHostConfIPType_Type()
)
gs2326TrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfIPType.setStatus("current")
_Gs2326TrapHostConfIP_Type = DisplayString
_Gs2326TrapHostConfIP_Object = MibTableColumn
gs2326TrapHostConfIP = _Gs2326TrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 4),
    _Gs2326TrapHostConfIP_Type()
)
gs2326TrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfIP.setStatus("current")


class _Gs2326TrapHostConfPort_Type(Integer32):
    """Custom type gs2326TrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326TrapHostConfPort_Type.__name__ = "Integer32"
_Gs2326TrapHostConfPort_Object = MibTableColumn
gs2326TrapHostConfPort = _Gs2326TrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 5),
    _Gs2326TrapHostConfPort_Type()
)
gs2326TrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfPort.setStatus("current")


class _Gs2326TrapHostConfCommunity_Type(DisplayString):
    """Custom type gs2326TrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326TrapHostConfCommunity_Type.__name__ = "DisplayString"
_Gs2326TrapHostConfCommunity_Object = MibTableColumn
gs2326TrapHostConfCommunity = _Gs2326TrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 6),
    _Gs2326TrapHostConfCommunity_Type()
)
gs2326TrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfCommunity.setStatus("current")


class _Gs2326TrapHostConfSeverityLevel_Type(Integer32):
    """Custom type gs2326TrapHostConfSeverityLevel based on Integer32"""
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


_Gs2326TrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Gs2326TrapHostConfSeverityLevel_Object = MibTableColumn
gs2326TrapHostConfSeverityLevel = _Gs2326TrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 7),
    _Gs2326TrapHostConfSeverityLevel_Type()
)
gs2326TrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfSeverityLevel.setStatus("current")


class _Gs2326TrapHostConfSecurityLevel_Type(Integer32):
    """Custom type gs2326TrapHostConfSecurityLevel based on Integer32"""
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


_Gs2326TrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Gs2326TrapHostConfSecurityLevel_Object = MibTableColumn
gs2326TrapHostConfSecurityLevel = _Gs2326TrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 8),
    _Gs2326TrapHostConfSecurityLevel_Type()
)
gs2326TrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfSecurityLevel.setStatus("current")


class _Gs2326TrapHostConfAuthPtc_Type(Integer32):
    """Custom type gs2326TrapHostConfAuthPtc based on Integer32"""
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


_Gs2326TrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Gs2326TrapHostConfAuthPtc_Object = MibTableColumn
gs2326TrapHostConfAuthPtc = _Gs2326TrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 9),
    _Gs2326TrapHostConfAuthPtc_Type()
)
gs2326TrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfAuthPtc.setStatus("current")
_Gs2326TrapHostConfAuthPassword_Type = DisplayString
_Gs2326TrapHostConfAuthPassword_Object = MibTableColumn
gs2326TrapHostConfAuthPassword = _Gs2326TrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 10),
    _Gs2326TrapHostConfAuthPassword_Type()
)
gs2326TrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfAuthPassword.setStatus("current")


class _Gs2326TrapHostConfPrivPtc_Type(Integer32):
    """Custom type gs2326TrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("des", 1)
    )


_Gs2326TrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Gs2326TrapHostConfPrivPtc_Object = MibTableColumn
gs2326TrapHostConfPrivPtc = _Gs2326TrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 11),
    _Gs2326TrapHostConfPrivPtc_Type()
)
gs2326TrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfPrivPtc.setStatus("current")
_Gs2326TrapHostConfPrivPassword_Type = DisplayString
_Gs2326TrapHostConfPrivPassword_Object = MibTableColumn
gs2326TrapHostConfPrivPassword = _Gs2326TrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 12),
    _Gs2326TrapHostConfPrivPassword_Type()
)
gs2326TrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfPrivPassword.setStatus("current")


class _Gs2326TrapHostConfCurrentMode_Type(Integer32):
    """Custom type gs2326TrapHostConfCurrentMode based on Integer32"""
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


_Gs2326TrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Gs2326TrapHostConfCurrentMode_Object = MibTableColumn
gs2326TrapHostConfCurrentMode = _Gs2326TrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 1, 6, 1, 13),
    _Gs2326TrapHostConfCurrentMode_Type()
)
gs2326TrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapHostConfCurrentMode.setStatus("current")
_Gs2326SnmpSystem_ObjectIdentity = ObjectIdentity
gs2326SnmpSystem = _Gs2326SnmpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 2)
)


class _Gs2326SnmpState_Type(Integer32):
    """Custom type gs2326SnmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326SnmpState_Type.__name__ = "Integer32"
_Gs2326SnmpState_Object = MibScalar
gs2326SnmpState = _Gs2326SnmpState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 2, 1),
    _Gs2326SnmpState_Type()
)
gs2326SnmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpState.setStatus("current")


class _Gs2326SnmpEngineID_Type(OctetString):
    """Custom type gs2326SnmpEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Gs2326SnmpEngineID_Type.__name__ = "OctetString"
_Gs2326SnmpEngineID_Object = MibScalar
gs2326SnmpEngineID = _Gs2326SnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 2, 2),
    _Gs2326SnmpEngineID_Type()
)
gs2326SnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpEngineID.setStatus("current")
_Gs2326SnmpCommunities_ObjectIdentity = ObjectIdentity
gs2326SnmpCommunities = _Gs2326SnmpCommunities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3)
)


class _Gs2326SnmpCommunitiesCreate_Type(Integer32):
    """Custom type gs2326SnmpCommunitiesCreate based on Integer32"""
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


_Gs2326SnmpCommunitiesCreate_Type.__name__ = "Integer32"
_Gs2326SnmpCommunitiesCreate_Object = MibScalar
gs2326SnmpCommunitiesCreate = _Gs2326SnmpCommunitiesCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 1),
    _Gs2326SnmpCommunitiesCreate_Type()
)
gs2326SnmpCommunitiesCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesCreate.setStatus("current")
_Gs2326SnmpCommunitiesTable_Object = MibTable
gs2326SnmpCommunitiesTable = _Gs2326SnmpCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesTable.setStatus("current")
_Gs2326SnmpCommunitiesEntry_Object = MibTableRow
gs2326SnmpCommunitiesEntry = _Gs2326SnmpCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1)
)
gs2326SnmpCommunitiesEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SnmpCommunitiesIndex"),
)
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesEntry.setStatus("current")


class _Gs2326SnmpCommunitiesIndex_Type(Integer32):
    """Custom type gs2326SnmpCommunitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2326SnmpCommunitiesIndex_Type.__name__ = "Integer32"
_Gs2326SnmpCommunitiesIndex_Object = MibTableColumn
gs2326SnmpCommunitiesIndex = _Gs2326SnmpCommunitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1, 1),
    _Gs2326SnmpCommunitiesIndex_Type()
)
gs2326SnmpCommunitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesIndex.setStatus("current")


class _Gs2326SnmpCommunitiesCommunity_Type(DisplayString):
    """Custom type gs2326SnmpCommunitiesCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpCommunitiesCommunity_Type.__name__ = "DisplayString"
_Gs2326SnmpCommunitiesCommunity_Object = MibTableColumn
gs2326SnmpCommunitiesCommunity = _Gs2326SnmpCommunitiesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1, 2),
    _Gs2326SnmpCommunitiesCommunity_Type()
)
gs2326SnmpCommunitiesCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesCommunity.setStatus("current")


class _Gs2326SnmpCommunitiesUserName_Type(DisplayString):
    """Custom type gs2326SnmpCommunitiesUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpCommunitiesUserName_Type.__name__ = "DisplayString"
_Gs2326SnmpCommunitiesUserName_Object = MibTableColumn
gs2326SnmpCommunitiesUserName = _Gs2326SnmpCommunitiesUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1, 3),
    _Gs2326SnmpCommunitiesUserName_Type()
)
gs2326SnmpCommunitiesUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesUserName.setStatus("current")
_Gs2326SnmpCommunitiesSourceIP_Type = IpAddress
_Gs2326SnmpCommunitiesSourceIP_Object = MibTableColumn
gs2326SnmpCommunitiesSourceIP = _Gs2326SnmpCommunitiesSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1, 4),
    _Gs2326SnmpCommunitiesSourceIP_Type()
)
gs2326SnmpCommunitiesSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesSourceIP.setStatus("current")
_Gs2326SnmpCommunitiesSourceMask_Type = IpAddress
_Gs2326SnmpCommunitiesSourceMask_Object = MibTableColumn
gs2326SnmpCommunitiesSourceMask = _Gs2326SnmpCommunitiesSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1, 5),
    _Gs2326SnmpCommunitiesSourceMask_Type()
)
gs2326SnmpCommunitiesSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesSourceMask.setStatus("current")


class _Gs2326SnmpCommunitiesRowStatus_Type(Integer32):
    """Custom type gs2326SnmpCommunitiesRowStatus based on Integer32"""
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


_Gs2326SnmpCommunitiesRowStatus_Type.__name__ = "Integer32"
_Gs2326SnmpCommunitiesRowStatus_Object = MibTableColumn
gs2326SnmpCommunitiesRowStatus = _Gs2326SnmpCommunitiesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 3, 2, 1, 6),
    _Gs2326SnmpCommunitiesRowStatus_Type()
)
gs2326SnmpCommunitiesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpCommunitiesRowStatus.setStatus("current")
_Gs2326SnmpUsers_ObjectIdentity = ObjectIdentity
gs2326SnmpUsers = _Gs2326SnmpUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4)
)


class _Gs2326SnmpUsersCreate_Type(Integer32):
    """Custom type gs2326SnmpUsersCreate based on Integer32"""
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


_Gs2326SnmpUsersCreate_Type.__name__ = "Integer32"
_Gs2326SnmpUsersCreate_Object = MibScalar
gs2326SnmpUsersCreate = _Gs2326SnmpUsersCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 1),
    _Gs2326SnmpUsersCreate_Type()
)
gs2326SnmpUsersCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersCreate.setStatus("current")
_Gs2326SnmpUsersTable_Object = MibTable
gs2326SnmpUsersTable = _Gs2326SnmpUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326SnmpUsersTable.setStatus("current")
_Gs2326SnmpUsersEntry_Object = MibTableRow
gs2326SnmpUsersEntry = _Gs2326SnmpUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1)
)
gs2326SnmpUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SnmpUsersIndex"),
)
if mibBuilder.loadTexts:
    gs2326SnmpUsersEntry.setStatus("current")


class _Gs2326SnmpUsersIndex_Type(Integer32):
    """Custom type gs2326SnmpUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2326SnmpUsersIndex_Type.__name__ = "Integer32"
_Gs2326SnmpUsersIndex_Object = MibTableColumn
gs2326SnmpUsersIndex = _Gs2326SnmpUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 1),
    _Gs2326SnmpUsersIndex_Type()
)
gs2326SnmpUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SnmpUsersIndex.setStatus("current")


class _Gs2326SnmpUsersUserName_Type(DisplayString):
    """Custom type gs2326SnmpUsersUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpUsersUserName_Type.__name__ = "DisplayString"
_Gs2326SnmpUsersUserName_Object = MibTableColumn
gs2326SnmpUsersUserName = _Gs2326SnmpUsersUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 2),
    _Gs2326SnmpUsersUserName_Type()
)
gs2326SnmpUsersUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersUserName.setStatus("current")


class _Gs2326SnmpUsersSecurityLevel_Type(Integer32):
    """Custom type gs2326SnmpUsersSecurityLevel based on Integer32"""
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


_Gs2326SnmpUsersSecurityLevel_Type.__name__ = "Integer32"
_Gs2326SnmpUsersSecurityLevel_Object = MibTableColumn
gs2326SnmpUsersSecurityLevel = _Gs2326SnmpUsersSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 3),
    _Gs2326SnmpUsersSecurityLevel_Type()
)
gs2326SnmpUsersSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersSecurityLevel.setStatus("current")


class _Gs2326SnmpUsersAuthenticationProtocol_Type(Integer32):
    """Custom type gs2326SnmpUsersAuthenticationProtocol based on Integer32"""
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


_Gs2326SnmpUsersAuthenticationProtocol_Type.__name__ = "Integer32"
_Gs2326SnmpUsersAuthenticationProtocol_Object = MibTableColumn
gs2326SnmpUsersAuthenticationProtocol = _Gs2326SnmpUsersAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 4),
    _Gs2326SnmpUsersAuthenticationProtocol_Type()
)
gs2326SnmpUsersAuthenticationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersAuthenticationProtocol.setStatus("current")
_Gs2326SnmpUsersAuthenticationPassword_Type = DisplayString
_Gs2326SnmpUsersAuthenticationPassword_Object = MibTableColumn
gs2326SnmpUsersAuthenticationPassword = _Gs2326SnmpUsersAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 5),
    _Gs2326SnmpUsersAuthenticationPassword_Type()
)
gs2326SnmpUsersAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersAuthenticationPassword.setStatus("current")


class _Gs2326SnmpUsersPrivacyProtocol_Type(Integer32):
    """Custom type gs2326SnmpUsersPrivacyProtocol based on Integer32"""
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


_Gs2326SnmpUsersPrivacyProtocol_Type.__name__ = "Integer32"
_Gs2326SnmpUsersPrivacyProtocol_Object = MibTableColumn
gs2326SnmpUsersPrivacyProtocol = _Gs2326SnmpUsersPrivacyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 6),
    _Gs2326SnmpUsersPrivacyProtocol_Type()
)
gs2326SnmpUsersPrivacyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersPrivacyProtocol.setStatus("current")
_Gs2326SnmpUsersPrivacyPassword_Type = DisplayString
_Gs2326SnmpUsersPrivacyPassword_Object = MibTableColumn
gs2326SnmpUsersPrivacyPassword = _Gs2326SnmpUsersPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 7),
    _Gs2326SnmpUsersPrivacyPassword_Type()
)
gs2326SnmpUsersPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersPrivacyPassword.setStatus("current")


class _Gs2326SnmpUsersRowStatus_Type(Integer32):
    """Custom type gs2326SnmpUsersRowStatus based on Integer32"""
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


_Gs2326SnmpUsersRowStatus_Type.__name__ = "Integer32"
_Gs2326SnmpUsersRowStatus_Object = MibTableColumn
gs2326SnmpUsersRowStatus = _Gs2326SnmpUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 4, 2, 1, 8),
    _Gs2326SnmpUsersRowStatus_Type()
)
gs2326SnmpUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpUsersRowStatus.setStatus("current")
_Gs2326SnmpGroups_ObjectIdentity = ObjectIdentity
gs2326SnmpGroups = _Gs2326SnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5)
)


class _Gs2326SnmpGroupsCreate_Type(Integer32):
    """Custom type gs2326SnmpGroupsCreate based on Integer32"""
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


_Gs2326SnmpGroupsCreate_Type.__name__ = "Integer32"
_Gs2326SnmpGroupsCreate_Object = MibScalar
gs2326SnmpGroupsCreate = _Gs2326SnmpGroupsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 1),
    _Gs2326SnmpGroupsCreate_Type()
)
gs2326SnmpGroupsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpGroupsCreate.setStatus("current")
_Gs2326SnmpGroupsTable_Object = MibTable
gs2326SnmpGroupsTable = _Gs2326SnmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gs2326SnmpGroupsTable.setStatus("current")
_Gs2326SnmpGroupsEntry_Object = MibTableRow
gs2326SnmpGroupsEntry = _Gs2326SnmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2, 1)
)
gs2326SnmpGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SnmpGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2326SnmpGroupsEntry.setStatus("current")


class _Gs2326SnmpGroupsIndex_Type(Integer32):
    """Custom type gs2326SnmpGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2326SnmpGroupsIndex_Type.__name__ = "Integer32"
_Gs2326SnmpGroupsIndex_Object = MibTableColumn
gs2326SnmpGroupsIndex = _Gs2326SnmpGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2, 1, 1),
    _Gs2326SnmpGroupsIndex_Type()
)
gs2326SnmpGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SnmpGroupsIndex.setStatus("current")


class _Gs2326SnmpGroupsSecurityModel_Type(Integer32):
    """Custom type gs2326SnmpGroupsSecurityModel based on Integer32"""
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


_Gs2326SnmpGroupsSecurityModel_Type.__name__ = "Integer32"
_Gs2326SnmpGroupsSecurityModel_Object = MibTableColumn
gs2326SnmpGroupsSecurityModel = _Gs2326SnmpGroupsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2, 1, 2),
    _Gs2326SnmpGroupsSecurityModel_Type()
)
gs2326SnmpGroupsSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpGroupsSecurityModel.setStatus("current")


class _Gs2326SnmpGroupsSecurityName_Type(DisplayString):
    """Custom type gs2326SnmpGroupsSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpGroupsSecurityName_Type.__name__ = "DisplayString"
_Gs2326SnmpGroupsSecurityName_Object = MibTableColumn
gs2326SnmpGroupsSecurityName = _Gs2326SnmpGroupsSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2, 1, 3),
    _Gs2326SnmpGroupsSecurityName_Type()
)
gs2326SnmpGroupsSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpGroupsSecurityName.setStatus("current")


class _Gs2326SnmpGroupsGroupName_Type(DisplayString):
    """Custom type gs2326SnmpGroupsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpGroupsGroupName_Type.__name__ = "DisplayString"
_Gs2326SnmpGroupsGroupName_Object = MibTableColumn
gs2326SnmpGroupsGroupName = _Gs2326SnmpGroupsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2, 1, 4),
    _Gs2326SnmpGroupsGroupName_Type()
)
gs2326SnmpGroupsGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpGroupsGroupName.setStatus("current")


class _Gs2326SnmpGroupsRowStatus_Type(Integer32):
    """Custom type gs2326SnmpGroupsRowStatus based on Integer32"""
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


_Gs2326SnmpGroupsRowStatus_Type.__name__ = "Integer32"
_Gs2326SnmpGroupsRowStatus_Object = MibTableColumn
gs2326SnmpGroupsRowStatus = _Gs2326SnmpGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 5, 2, 1, 5),
    _Gs2326SnmpGroupsRowStatus_Type()
)
gs2326SnmpGroupsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpGroupsRowStatus.setStatus("current")
_Gs2326SnmpViews_ObjectIdentity = ObjectIdentity
gs2326SnmpViews = _Gs2326SnmpViews_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6)
)


class _Gs2326SnmpViewsCreate_Type(Integer32):
    """Custom type gs2326SnmpViewsCreate based on Integer32"""
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


_Gs2326SnmpViewsCreate_Type.__name__ = "Integer32"
_Gs2326SnmpViewsCreate_Object = MibScalar
gs2326SnmpViewsCreate = _Gs2326SnmpViewsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 1),
    _Gs2326SnmpViewsCreate_Type()
)
gs2326SnmpViewsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpViewsCreate.setStatus("current")
_Gs2326SnmpViewsTable_Object = MibTable
gs2326SnmpViewsTable = _Gs2326SnmpViewsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    gs2326SnmpViewsTable.setStatus("current")
_Gs2326SnmpViewsEntry_Object = MibTableRow
gs2326SnmpViewsEntry = _Gs2326SnmpViewsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2, 1)
)
gs2326SnmpViewsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SnmpViewsIndex"),
)
if mibBuilder.loadTexts:
    gs2326SnmpViewsEntry.setStatus("current")


class _Gs2326SnmpViewsIndex_Type(Integer32):
    """Custom type gs2326SnmpViewsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2326SnmpViewsIndex_Type.__name__ = "Integer32"
_Gs2326SnmpViewsIndex_Object = MibTableColumn
gs2326SnmpViewsIndex = _Gs2326SnmpViewsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2, 1, 1),
    _Gs2326SnmpViewsIndex_Type()
)
gs2326SnmpViewsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SnmpViewsIndex.setStatus("current")


class _Gs2326SnmpViewsName_Type(DisplayString):
    """Custom type gs2326SnmpViewsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpViewsName_Type.__name__ = "DisplayString"
_Gs2326SnmpViewsName_Object = MibTableColumn
gs2326SnmpViewsName = _Gs2326SnmpViewsName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2, 1, 2),
    _Gs2326SnmpViewsName_Type()
)
gs2326SnmpViewsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpViewsName.setStatus("current")


class _Gs2326SnmpViewsType_Type(Integer32):
    """Custom type gs2326SnmpViewsType based on Integer32"""
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


_Gs2326SnmpViewsType_Type.__name__ = "Integer32"
_Gs2326SnmpViewsType_Object = MibTableColumn
gs2326SnmpViewsType = _Gs2326SnmpViewsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2, 1, 3),
    _Gs2326SnmpViewsType_Type()
)
gs2326SnmpViewsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpViewsType.setStatus("current")


class _Gs2326SnmpViewsOIDSubtree_Type(DisplayString):
    """Custom type gs2326SnmpViewsOIDSubtree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Gs2326SnmpViewsOIDSubtree_Type.__name__ = "DisplayString"
_Gs2326SnmpViewsOIDSubtree_Object = MibTableColumn
gs2326SnmpViewsOIDSubtree = _Gs2326SnmpViewsOIDSubtree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2, 1, 4),
    _Gs2326SnmpViewsOIDSubtree_Type()
)
gs2326SnmpViewsOIDSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpViewsOIDSubtree.setStatus("current")


class _Gs2326SnmpViewsRowStatus_Type(Integer32):
    """Custom type gs2326SnmpViewsRowStatus based on Integer32"""
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


_Gs2326SnmpViewsRowStatus_Type.__name__ = "Integer32"
_Gs2326SnmpViewsRowStatus_Object = MibTableColumn
gs2326SnmpViewsRowStatus = _Gs2326SnmpViewsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 6, 2, 1, 5),
    _Gs2326SnmpViewsRowStatus_Type()
)
gs2326SnmpViewsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpViewsRowStatus.setStatus("current")
_Gs2326SnmpAccess_ObjectIdentity = ObjectIdentity
gs2326SnmpAccess = _Gs2326SnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7)
)


class _Gs2326SnmpAccessCreate_Type(Integer32):
    """Custom type gs2326SnmpAccessCreate based on Integer32"""
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


_Gs2326SnmpAccessCreate_Type.__name__ = "Integer32"
_Gs2326SnmpAccessCreate_Object = MibScalar
gs2326SnmpAccessCreate = _Gs2326SnmpAccessCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 1),
    _Gs2326SnmpAccessCreate_Type()
)
gs2326SnmpAccessCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessCreate.setStatus("current")
_Gs2326SnmpAccessTable_Object = MibTable
gs2326SnmpAccessTable = _Gs2326SnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    gs2326SnmpAccessTable.setStatus("current")
_Gs2326SnmpAccessEntry_Object = MibTableRow
gs2326SnmpAccessEntry = _Gs2326SnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1)
)
gs2326SnmpAccessEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    gs2326SnmpAccessEntry.setStatus("current")


class _Gs2326SnmpAccessIndex_Type(Integer32):
    """Custom type gs2326SnmpAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2326SnmpAccessIndex_Type.__name__ = "Integer32"
_Gs2326SnmpAccessIndex_Object = MibTableColumn
gs2326SnmpAccessIndex = _Gs2326SnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 1),
    _Gs2326SnmpAccessIndex_Type()
)
gs2326SnmpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SnmpAccessIndex.setStatus("current")


class _Gs2326SnmpAccessGroupName_Type(DisplayString):
    """Custom type gs2326SnmpAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpAccessGroupName_Type.__name__ = "DisplayString"
_Gs2326SnmpAccessGroupName_Object = MibTableColumn
gs2326SnmpAccessGroupName = _Gs2326SnmpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 2),
    _Gs2326SnmpAccessGroupName_Type()
)
gs2326SnmpAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessGroupName.setStatus("current")


class _Gs2326SnmpAccessSecurityModel_Type(Integer32):
    """Custom type gs2326SnmpAccessSecurityModel based on Integer32"""
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


_Gs2326SnmpAccessSecurityModel_Type.__name__ = "Integer32"
_Gs2326SnmpAccessSecurityModel_Object = MibTableColumn
gs2326SnmpAccessSecurityModel = _Gs2326SnmpAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 3),
    _Gs2326SnmpAccessSecurityModel_Type()
)
gs2326SnmpAccessSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessSecurityModel.setStatus("current")


class _Gs2326SnmpAccessSecurityLevel_Type(Integer32):
    """Custom type gs2326SnmpAccessSecurityLevel based on Integer32"""
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


_Gs2326SnmpAccessSecurityLevel_Type.__name__ = "Integer32"
_Gs2326SnmpAccessSecurityLevel_Object = MibTableColumn
gs2326SnmpAccessSecurityLevel = _Gs2326SnmpAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 4),
    _Gs2326SnmpAccessSecurityLevel_Type()
)
gs2326SnmpAccessSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessSecurityLevel.setStatus("current")


class _Gs2326SnmpAccessReadViewName_Type(DisplayString):
    """Custom type gs2326SnmpAccessReadViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpAccessReadViewName_Type.__name__ = "DisplayString"
_Gs2326SnmpAccessReadViewName_Object = MibTableColumn
gs2326SnmpAccessReadViewName = _Gs2326SnmpAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 5),
    _Gs2326SnmpAccessReadViewName_Type()
)
gs2326SnmpAccessReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessReadViewName.setStatus("current")


class _Gs2326SnmpAccessWriteViewName_Type(DisplayString):
    """Custom type gs2326SnmpAccessWriteViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326SnmpAccessWriteViewName_Type.__name__ = "DisplayString"
_Gs2326SnmpAccessWriteViewName_Object = MibTableColumn
gs2326SnmpAccessWriteViewName = _Gs2326SnmpAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 6),
    _Gs2326SnmpAccessWriteViewName_Type()
)
gs2326SnmpAccessWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessWriteViewName.setStatus("current")


class _Gs2326SnmpAccessRowStatus_Type(Integer32):
    """Custom type gs2326SnmpAccessRowStatus based on Integer32"""
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


_Gs2326SnmpAccessRowStatus_Type.__name__ = "Integer32"
_Gs2326SnmpAccessRowStatus_Object = MibTableColumn
gs2326SnmpAccessRowStatus = _Gs2326SnmpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 1, 6, 7, 2, 1, 7),
    _Gs2326SnmpAccessRowStatus_Type()
)
gs2326SnmpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SnmpAccessRowStatus.setStatus("current")
_Gs2326Configuration_ObjectIdentity = ObjectIdentity
gs2326Configuration = _Gs2326Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2)
)
_Gs2326Port_ObjectIdentity = ObjectIdentity
gs2326Port = _Gs2326Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1)
)
_Gs2326PortConfigurationTable_Object = MibTable
gs2326PortConfigurationTable = _Gs2326PortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1)
)
if mibBuilder.loadTexts:
    gs2326PortConfigurationTable.setStatus("current")
_Gs2326PortConfigurationEntry_Object = MibTableRow
gs2326PortConfigurationEntry = _Gs2326PortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1)
)
gs2326PortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326PortConfigurationEntry.setStatus("current")


class _Gs2326PortConfPort_Type(Integer32):
    """Custom type gs2326PortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortConfPort_Type.__name__ = "Integer32"
_Gs2326PortConfPort_Object = MibTableColumn
gs2326PortConfPort = _Gs2326PortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 1),
    _Gs2326PortConfPort_Type()
)
gs2326PortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortConfPort.setStatus("current")


class _Gs2326PortConfPortMedia_Type(DisplayString):
    """Custom type gs2326PortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Gs2326PortConfPortMedia_Type.__name__ = "DisplayString"
_Gs2326PortConfPortMedia_Object = MibTableColumn
gs2326PortConfPortMedia = _Gs2326PortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 2),
    _Gs2326PortConfPortMedia_Type()
)
gs2326PortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortConfPortMedia.setStatus("current")


class _Gs2326PortConfLink_Type(DisplayString):
    """Custom type gs2326PortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Gs2326PortConfLink_Type.__name__ = "DisplayString"
_Gs2326PortConfLink_Object = MibTableColumn
gs2326PortConfLink = _Gs2326PortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 3),
    _Gs2326PortConfLink_Type()
)
gs2326PortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortConfLink.setStatus("current")


class _Gs2326PortConfCurrentSpeed_Type(DisplayString):
    """Custom type gs2326PortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Gs2326PortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Gs2326PortConfCurrentSpeed_Object = MibTableColumn
gs2326PortConfCurrentSpeed = _Gs2326PortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 4),
    _Gs2326PortConfCurrentSpeed_Type()
)
gs2326PortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortConfCurrentSpeed.setStatus("current")


class _Gs2326PortConfSpeed_Type(Integer32):
    """Custom type gs2326PortConfSpeed based on Integer32"""
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


_Gs2326PortConfSpeed_Type.__name__ = "Integer32"
_Gs2326PortConfSpeed_Object = MibTableColumn
gs2326PortConfSpeed = _Gs2326PortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 5),
    _Gs2326PortConfSpeed_Type()
)
gs2326PortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortConfSpeed.setStatus("current")


class _Gs2326PortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type gs2326PortConfCurrentFlowControlRx based on Integer32"""
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


_Gs2326PortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Gs2326PortConfCurrentFlowControlRx_Object = MibTableColumn
gs2326PortConfCurrentFlowControlRx = _Gs2326PortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 6),
    _Gs2326PortConfCurrentFlowControlRx_Type()
)
gs2326PortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortConfCurrentFlowControlRx.setStatus("current")


class _Gs2326PortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type gs2326PortConfCurrentFlowControlTx based on Integer32"""
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


_Gs2326PortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Gs2326PortConfCurrentFlowControlTx_Object = MibTableColumn
gs2326PortConfCurrentFlowControlTx = _Gs2326PortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 7),
    _Gs2326PortConfCurrentFlowControlTx_Type()
)
gs2326PortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortConfCurrentFlowControlTx.setStatus("current")


class _Gs2326PortConfFlowControl_Type(Integer32):
    """Custom type gs2326PortConfFlowControl based on Integer32"""
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


_Gs2326PortConfFlowControl_Type.__name__ = "Integer32"
_Gs2326PortConfFlowControl_Object = MibTableColumn
gs2326PortConfFlowControl = _Gs2326PortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 8),
    _Gs2326PortConfFlowControl_Type()
)
gs2326PortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortConfFlowControl.setStatus("current")


class _Gs2326PortConfMaxFrameSize_Type(Integer32):
    """Custom type gs2326PortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Gs2326PortConfMaxFrameSize_Type.__name__ = "Integer32"
_Gs2326PortConfMaxFrameSize_Object = MibTableColumn
gs2326PortConfMaxFrameSize = _Gs2326PortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 9),
    _Gs2326PortConfMaxFrameSize_Type()
)
gs2326PortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortConfMaxFrameSize.setStatus("current")


class _Gs2326PortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type gs2326PortConfExcessiveCollisionMode based on Integer32"""
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


_Gs2326PortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Gs2326PortConfExcessiveCollisionMode_Object = MibTableColumn
gs2326PortConfExcessiveCollisionMode = _Gs2326PortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 10),
    _Gs2326PortConfExcessiveCollisionMode_Type()
)
gs2326PortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortConfExcessiveCollisionMode.setStatus("current")


class _Gs2326PortConfPowerControl_Type(Integer32):
    """Custom type gs2326PortConfPowerControl based on Integer32"""
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


_Gs2326PortConfPowerControl_Type.__name__ = "Integer32"
_Gs2326PortConfPowerControl_Object = MibTableColumn
gs2326PortConfPowerControl = _Gs2326PortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 11),
    _Gs2326PortConfPowerControl_Type()
)
gs2326PortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortConfPowerControl.setStatus("current")
_Gs2326PortConfDescription_Type = DisplayString
_Gs2326PortConfDescription_Object = MibTableColumn
gs2326PortConfDescription = _Gs2326PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 1, 1, 12),
    _Gs2326PortConfDescription_Type()
)
gs2326PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortConfDescription.setStatus("current")
_Gs2326PortTrafficStatisticsTable_Object = MibTable
gs2326PortTrafficStatisticsTable = _Gs2326PortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326PortTrafficStatisticsTable.setStatus("current")
_Gs2326PortTrafficStatisticsEntry_Object = MibTableRow
gs2326PortTrafficStatisticsEntry = _Gs2326PortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1)
)
gs2326PortTrafficStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2326PortTrafficStatisticsEntry.setStatus("current")


class _Gs2326PortTrafficStatisticsPort_Type(Integer32):
    """Custom type gs2326PortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Gs2326PortTrafficStatisticsPort_Object = MibTableColumn
gs2326PortTrafficStatisticsPort = _Gs2326PortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 1),
    _Gs2326PortTrafficStatisticsPort_Type()
)
gs2326PortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortTrafficStatisticsPort.setStatus("current")


class _Gs2326PortTrafficStatisticsClear_Type(Integer32):
    """Custom type gs2326PortTrafficStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Gs2326PortTrafficStatisticsClear_Object = MibTableColumn
gs2326PortTrafficStatisticsClear = _Gs2326PortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 2),
    _Gs2326PortTrafficStatisticsClear_Type()
)
gs2326PortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortTrafficStatisticsClear.setStatus("current")
_Gs2326PortTrafficRxPackets_Type = Counter64
_Gs2326PortTrafficRxPackets_Object = MibTableColumn
gs2326PortTrafficRxPackets = _Gs2326PortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 3),
    _Gs2326PortTrafficRxPackets_Type()
)
gs2326PortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxPackets.setStatus("current")
_Gs2326PortTrafficRxOctets_Type = Counter64
_Gs2326PortTrafficRxOctets_Object = MibTableColumn
gs2326PortTrafficRxOctets = _Gs2326PortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 4),
    _Gs2326PortTrafficRxOctets_Type()
)
gs2326PortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxOctets.setStatus("current")
_Gs2326PortTrafficRxUnicast_Type = Counter64
_Gs2326PortTrafficRxUnicast_Object = MibTableColumn
gs2326PortTrafficRxUnicast = _Gs2326PortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 5),
    _Gs2326PortTrafficRxUnicast_Type()
)
gs2326PortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxUnicast.setStatus("current")
_Gs2326PortTrafficRxMulticast_Type = Counter64
_Gs2326PortTrafficRxMulticast_Object = MibTableColumn
gs2326PortTrafficRxMulticast = _Gs2326PortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 6),
    _Gs2326PortTrafficRxMulticast_Type()
)
gs2326PortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxMulticast.setStatus("current")
_Gs2326PortTrafficRxBroadcast_Type = Counter64
_Gs2326PortTrafficRxBroadcast_Object = MibTableColumn
gs2326PortTrafficRxBroadcast = _Gs2326PortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 7),
    _Gs2326PortTrafficRxBroadcast_Type()
)
gs2326PortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxBroadcast.setStatus("current")
_Gs2326PortTrafficRxPause_Type = Counter64
_Gs2326PortTrafficRxPause_Object = MibTableColumn
gs2326PortTrafficRxPause = _Gs2326PortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 8),
    _Gs2326PortTrafficRxPause_Type()
)
gs2326PortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxPause.setStatus("current")
_Gs2326PortTrafficRx64Bytes_Type = Counter64
_Gs2326PortTrafficRx64Bytes_Object = MibTableColumn
gs2326PortTrafficRx64Bytes = _Gs2326PortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 9),
    _Gs2326PortTrafficRx64Bytes_Type()
)
gs2326PortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRx64Bytes.setStatus("current")
_Gs2326PortTrafficRx65to127Bytes_Type = Counter64
_Gs2326PortTrafficRx65to127Bytes_Object = MibTableColumn
gs2326PortTrafficRx65to127Bytes = _Gs2326PortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 10),
    _Gs2326PortTrafficRx65to127Bytes_Type()
)
gs2326PortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRx65to127Bytes.setStatus("current")
_Gs2326PortTrafficRx128to255Bytes_Type = Counter64
_Gs2326PortTrafficRx128to255Bytes_Object = MibTableColumn
gs2326PortTrafficRx128to255Bytes = _Gs2326PortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 11),
    _Gs2326PortTrafficRx128to255Bytes_Type()
)
gs2326PortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRx128to255Bytes.setStatus("current")
_Gs2326PortTrafficRx256to511Bytes_Type = Counter64
_Gs2326PortTrafficRx256to511Bytes_Object = MibTableColumn
gs2326PortTrafficRx256to511Bytes = _Gs2326PortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 12),
    _Gs2326PortTrafficRx256to511Bytes_Type()
)
gs2326PortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRx256to511Bytes.setStatus("current")
_Gs2326PortTrafficRx512to1023Bytes_Type = Counter64
_Gs2326PortTrafficRx512to1023Bytes_Object = MibTableColumn
gs2326PortTrafficRx512to1023Bytes = _Gs2326PortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 13),
    _Gs2326PortTrafficRx512to1023Bytes_Type()
)
gs2326PortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRx512to1023Bytes.setStatus("current")
_Gs2326PortTrafficRx1024to1526Bytes_Type = Counter64
_Gs2326PortTrafficRx1024to1526Bytes_Object = MibTableColumn
gs2326PortTrafficRx1024to1526Bytes = _Gs2326PortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 14),
    _Gs2326PortTrafficRx1024to1526Bytes_Type()
)
gs2326PortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRx1024to1526Bytes.setStatus("current")
_Gs2326PortTrafficRxExceecd1527Bytes_Type = Counter64
_Gs2326PortTrafficRxExceecd1527Bytes_Object = MibTableColumn
gs2326PortTrafficRxExceecd1527Bytes = _Gs2326PortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 15),
    _Gs2326PortTrafficRxExceecd1527Bytes_Type()
)
gs2326PortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxExceecd1527Bytes.setStatus("current")
_Gs2326PortTrafficRxQ0_Type = Counter64
_Gs2326PortTrafficRxQ0_Object = MibTableColumn
gs2326PortTrafficRxQ0 = _Gs2326PortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 16),
    _Gs2326PortTrafficRxQ0_Type()
)
gs2326PortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ0.setStatus("current")
_Gs2326PortTrafficRxQ1_Type = Counter64
_Gs2326PortTrafficRxQ1_Object = MibTableColumn
gs2326PortTrafficRxQ1 = _Gs2326PortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 17),
    _Gs2326PortTrafficRxQ1_Type()
)
gs2326PortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ1.setStatus("current")
_Gs2326PortTrafficRxQ2_Type = Counter64
_Gs2326PortTrafficRxQ2_Object = MibTableColumn
gs2326PortTrafficRxQ2 = _Gs2326PortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 18),
    _Gs2326PortTrafficRxQ2_Type()
)
gs2326PortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ2.setStatus("current")
_Gs2326PortTrafficRxQ3_Type = Counter64
_Gs2326PortTrafficRxQ3_Object = MibTableColumn
gs2326PortTrafficRxQ3 = _Gs2326PortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 19),
    _Gs2326PortTrafficRxQ3_Type()
)
gs2326PortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ3.setStatus("current")
_Gs2326PortTrafficRxQ4_Type = Counter64
_Gs2326PortTrafficRxQ4_Object = MibTableColumn
gs2326PortTrafficRxQ4 = _Gs2326PortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 20),
    _Gs2326PortTrafficRxQ4_Type()
)
gs2326PortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ4.setStatus("current")
_Gs2326PortTrafficRxQ5_Type = Counter64
_Gs2326PortTrafficRxQ5_Object = MibTableColumn
gs2326PortTrafficRxQ5 = _Gs2326PortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 21),
    _Gs2326PortTrafficRxQ5_Type()
)
gs2326PortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ5.setStatus("current")
_Gs2326PortTrafficRxQ6_Type = Counter64
_Gs2326PortTrafficRxQ6_Object = MibTableColumn
gs2326PortTrafficRxQ6 = _Gs2326PortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 22),
    _Gs2326PortTrafficRxQ6_Type()
)
gs2326PortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ6.setStatus("current")
_Gs2326PortTrafficRxQ7_Type = Counter64
_Gs2326PortTrafficRxQ7_Object = MibTableColumn
gs2326PortTrafficRxQ7 = _Gs2326PortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 23),
    _Gs2326PortTrafficRxQ7_Type()
)
gs2326PortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxQ7.setStatus("current")
_Gs2326PortTrafficRxDrops_Type = Counter64
_Gs2326PortTrafficRxDrops_Object = MibTableColumn
gs2326PortTrafficRxDrops = _Gs2326PortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 24),
    _Gs2326PortTrafficRxDrops_Type()
)
gs2326PortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxDrops.setStatus("current")
_Gs2326PortTrafficRxCRCorAlignment_Type = Counter64
_Gs2326PortTrafficRxCRCorAlignment_Object = MibTableColumn
gs2326PortTrafficRxCRCorAlignment = _Gs2326PortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 25),
    _Gs2326PortTrafficRxCRCorAlignment_Type()
)
gs2326PortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxCRCorAlignment.setStatus("current")
_Gs2326PortTrafficRxUndersize_Type = Counter64
_Gs2326PortTrafficRxUndersize_Object = MibTableColumn
gs2326PortTrafficRxUndersize = _Gs2326PortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 26),
    _Gs2326PortTrafficRxUndersize_Type()
)
gs2326PortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxUndersize.setStatus("current")
_Gs2326PortTrafficRxOversize_Type = Counter64
_Gs2326PortTrafficRxOversize_Object = MibTableColumn
gs2326PortTrafficRxOversize = _Gs2326PortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 27),
    _Gs2326PortTrafficRxOversize_Type()
)
gs2326PortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxOversize.setStatus("current")
_Gs2326PortTrafficRxFragments_Type = Counter64
_Gs2326PortTrafficRxFragments_Object = MibTableColumn
gs2326PortTrafficRxFragments = _Gs2326PortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 28),
    _Gs2326PortTrafficRxFragments_Type()
)
gs2326PortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxFragments.setStatus("current")
_Gs2326PortTrafficRxJabber_Type = Counter64
_Gs2326PortTrafficRxJabber_Object = MibTableColumn
gs2326PortTrafficRxJabber = _Gs2326PortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 29),
    _Gs2326PortTrafficRxJabber_Type()
)
gs2326PortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxJabber.setStatus("current")
_Gs2326PortTrafficRxFiltered_Type = Counter64
_Gs2326PortTrafficRxFiltered_Object = MibTableColumn
gs2326PortTrafficRxFiltered = _Gs2326PortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 30),
    _Gs2326PortTrafficRxFiltered_Type()
)
gs2326PortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficRxFiltered.setStatus("current")
_Gs2326PortTrafficTxPackets_Type = Counter64
_Gs2326PortTrafficTxPackets_Object = MibTableColumn
gs2326PortTrafficTxPackets = _Gs2326PortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 31),
    _Gs2326PortTrafficTxPackets_Type()
)
gs2326PortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxPackets.setStatus("current")
_Gs2326PortTrafficTxOctets_Type = Counter64
_Gs2326PortTrafficTxOctets_Object = MibTableColumn
gs2326PortTrafficTxOctets = _Gs2326PortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 32),
    _Gs2326PortTrafficTxOctets_Type()
)
gs2326PortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxOctets.setStatus("current")
_Gs2326PortTrafficTxUnicast_Type = Counter64
_Gs2326PortTrafficTxUnicast_Object = MibTableColumn
gs2326PortTrafficTxUnicast = _Gs2326PortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 33),
    _Gs2326PortTrafficTxUnicast_Type()
)
gs2326PortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxUnicast.setStatus("current")
_Gs2326PortTrafficTxMulticast_Type = Counter64
_Gs2326PortTrafficTxMulticast_Object = MibTableColumn
gs2326PortTrafficTxMulticast = _Gs2326PortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 34),
    _Gs2326PortTrafficTxMulticast_Type()
)
gs2326PortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxMulticast.setStatus("current")
_Gs2326PortTrafficTxBroadcast_Type = Counter64
_Gs2326PortTrafficTxBroadcast_Object = MibTableColumn
gs2326PortTrafficTxBroadcast = _Gs2326PortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 35),
    _Gs2326PortTrafficTxBroadcast_Type()
)
gs2326PortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxBroadcast.setStatus("current")
_Gs2326PortTrafficTxPause_Type = Counter64
_Gs2326PortTrafficTxPause_Object = MibTableColumn
gs2326PortTrafficTxPause = _Gs2326PortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 36),
    _Gs2326PortTrafficTxPause_Type()
)
gs2326PortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxPause.setStatus("current")
_Gs2326PortTrafficTx64Bytes_Type = Counter64
_Gs2326PortTrafficTx64Bytes_Object = MibTableColumn
gs2326PortTrafficTx64Bytes = _Gs2326PortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 37),
    _Gs2326PortTrafficTx64Bytes_Type()
)
gs2326PortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTx64Bytes.setStatus("current")
_Gs2326PortTrafficTx65to127Bytes_Type = Counter64
_Gs2326PortTrafficTx65to127Bytes_Object = MibTableColumn
gs2326PortTrafficTx65to127Bytes = _Gs2326PortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 38),
    _Gs2326PortTrafficTx65to127Bytes_Type()
)
gs2326PortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTx65to127Bytes.setStatus("current")
_Gs2326PortTrafficTx128to255Bytes_Type = Counter64
_Gs2326PortTrafficTx128to255Bytes_Object = MibTableColumn
gs2326PortTrafficTx128to255Bytes = _Gs2326PortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 39),
    _Gs2326PortTrafficTx128to255Bytes_Type()
)
gs2326PortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTx128to255Bytes.setStatus("current")
_Gs2326PortTrafficTx256to511Bytes_Type = Counter64
_Gs2326PortTrafficTx256to511Bytes_Object = MibTableColumn
gs2326PortTrafficTx256to511Bytes = _Gs2326PortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 40),
    _Gs2326PortTrafficTx256to511Bytes_Type()
)
gs2326PortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTx256to511Bytes.setStatus("current")
_Gs2326PortTrafficTx512to1023Bytes_Type = Counter64
_Gs2326PortTrafficTx512to1023Bytes_Object = MibTableColumn
gs2326PortTrafficTx512to1023Bytes = _Gs2326PortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 41),
    _Gs2326PortTrafficTx512to1023Bytes_Type()
)
gs2326PortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTx512to1023Bytes.setStatus("current")
_Gs2326PortTrafficTx1024to1526Bytes_Type = Counter64
_Gs2326PortTrafficTx1024to1526Bytes_Object = MibTableColumn
gs2326PortTrafficTx1024to1526Bytes = _Gs2326PortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 42),
    _Gs2326PortTrafficTx1024to1526Bytes_Type()
)
gs2326PortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTx1024to1526Bytes.setStatus("current")
_Gs2326PortTrafficTxExceecd1527Bytes_Type = Counter64
_Gs2326PortTrafficTxExceecd1527Bytes_Object = MibTableColumn
gs2326PortTrafficTxExceecd1527Bytes = _Gs2326PortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 43),
    _Gs2326PortTrafficTxExceecd1527Bytes_Type()
)
gs2326PortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxExceecd1527Bytes.setStatus("current")
_Gs2326PortTrafficTxQ0_Type = Counter64
_Gs2326PortTrafficTxQ0_Object = MibTableColumn
gs2326PortTrafficTxQ0 = _Gs2326PortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 44),
    _Gs2326PortTrafficTxQ0_Type()
)
gs2326PortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ0.setStatus("current")
_Gs2326PortTrafficTxQ1_Type = Counter64
_Gs2326PortTrafficTxQ1_Object = MibTableColumn
gs2326PortTrafficTxQ1 = _Gs2326PortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 45),
    _Gs2326PortTrafficTxQ1_Type()
)
gs2326PortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ1.setStatus("current")
_Gs2326PortTrafficTxQ2_Type = Counter64
_Gs2326PortTrafficTxQ2_Object = MibTableColumn
gs2326PortTrafficTxQ2 = _Gs2326PortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 46),
    _Gs2326PortTrafficTxQ2_Type()
)
gs2326PortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ2.setStatus("current")
_Gs2326PortTrafficTxQ3_Type = Counter64
_Gs2326PortTrafficTxQ3_Object = MibTableColumn
gs2326PortTrafficTxQ3 = _Gs2326PortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 47),
    _Gs2326PortTrafficTxQ3_Type()
)
gs2326PortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ3.setStatus("current")
_Gs2326PortTrafficTxQ4_Type = Counter64
_Gs2326PortTrafficTxQ4_Object = MibTableColumn
gs2326PortTrafficTxQ4 = _Gs2326PortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 48),
    _Gs2326PortTrafficTxQ4_Type()
)
gs2326PortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ4.setStatus("current")
_Gs2326PortTrafficTxQ5_Type = Counter64
_Gs2326PortTrafficTxQ5_Object = MibTableColumn
gs2326PortTrafficTxQ5 = _Gs2326PortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 49),
    _Gs2326PortTrafficTxQ5_Type()
)
gs2326PortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ5.setStatus("current")
_Gs2326PortTrafficTxQ6_Type = Counter64
_Gs2326PortTrafficTxQ6_Object = MibTableColumn
gs2326PortTrafficTxQ6 = _Gs2326PortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 50),
    _Gs2326PortTrafficTxQ6_Type()
)
gs2326PortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ6.setStatus("current")
_Gs2326PortTrafficTxQ7_Type = Counter64
_Gs2326PortTrafficTxQ7_Object = MibTableColumn
gs2326PortTrafficTxQ7 = _Gs2326PortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 51),
    _Gs2326PortTrafficTxQ7_Type()
)
gs2326PortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxQ7.setStatus("current")
_Gs2326PortTrafficTxDrops_Type = Counter64
_Gs2326PortTrafficTxDrops_Object = MibTableColumn
gs2326PortTrafficTxDrops = _Gs2326PortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 52),
    _Gs2326PortTrafficTxDrops_Type()
)
gs2326PortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxDrops.setStatus("current")
_Gs2326PortTrafficTxLateOrExcColl_Type = Counter64
_Gs2326PortTrafficTxLateOrExcColl_Object = MibTableColumn
gs2326PortTrafficTxLateOrExcColl = _Gs2326PortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 2, 1, 53),
    _Gs2326PortTrafficTxLateOrExcColl_Type()
)
gs2326PortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortTrafficTxLateOrExcColl.setStatus("current")
_Gs2326PortQoSStatistics_ObjectIdentity = ObjectIdentity
gs2326PortQoSStatistics = _Gs2326PortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3)
)


class _Gs2326PortQoSStatisticsClear_Type(Integer32):
    """Custom type gs2326PortQoSStatisticsClear based on Integer32"""
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


_Gs2326PortQoSStatisticsClear_Type.__name__ = "Integer32"
_Gs2326PortQoSStatisticsClear_Object = MibScalar
gs2326PortQoSStatisticsClear = _Gs2326PortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 1),
    _Gs2326PortQoSStatisticsClear_Type()
)
gs2326PortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSStatisticsClear.setStatus("current")
_Gs2326PortQoSStatisticsTable_Object = MibTable
gs2326PortQoSStatisticsTable = _Gs2326PortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326PortQoSStatisticsTable.setStatus("current")
_Gs2326PortQoSStatisticsEntry_Object = MibTableRow
gs2326PortQoSStatisticsEntry = _Gs2326PortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1)
)
gs2326PortQoSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2326PortQoSStatisticsEntry.setStatus("current")


class _Gs2326PortQoSStatisticsPort_Type(Integer32):
    """Custom type gs2326PortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortQoSStatisticsPort_Type.__name__ = "Integer32"
_Gs2326PortQoSStatisticsPort_Object = MibTableColumn
gs2326PortQoSStatisticsPort = _Gs2326PortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 1),
    _Gs2326PortQoSStatisticsPort_Type()
)
gs2326PortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortQoSStatisticsPort.setStatus("current")
_Gs2326PortQoSQ0Rx_Type = Counter64
_Gs2326PortQoSQ0Rx_Object = MibTableColumn
gs2326PortQoSQ0Rx = _Gs2326PortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 2),
    _Gs2326PortQoSQ0Rx_Type()
)
gs2326PortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ0Rx.setStatus("current")
_Gs2326PortQoSQ0Tx_Type = Counter64
_Gs2326PortQoSQ0Tx_Object = MibTableColumn
gs2326PortQoSQ0Tx = _Gs2326PortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 3),
    _Gs2326PortQoSQ0Tx_Type()
)
gs2326PortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ0Tx.setStatus("current")
_Gs2326PortQoSQ1Rx_Type = Counter64
_Gs2326PortQoSQ1Rx_Object = MibTableColumn
gs2326PortQoSQ1Rx = _Gs2326PortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 4),
    _Gs2326PortQoSQ1Rx_Type()
)
gs2326PortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ1Rx.setStatus("current")
_Gs2326PortQoSQ1Tx_Type = Counter64
_Gs2326PortQoSQ1Tx_Object = MibTableColumn
gs2326PortQoSQ1Tx = _Gs2326PortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 5),
    _Gs2326PortQoSQ1Tx_Type()
)
gs2326PortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ1Tx.setStatus("current")
_Gs2326PortQoSQ2Rx_Type = Counter64
_Gs2326PortQoSQ2Rx_Object = MibTableColumn
gs2326PortQoSQ2Rx = _Gs2326PortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 6),
    _Gs2326PortQoSQ2Rx_Type()
)
gs2326PortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ2Rx.setStatus("current")
_Gs2326PortQoSQ2Tx_Type = Counter64
_Gs2326PortQoSQ2Tx_Object = MibTableColumn
gs2326PortQoSQ2Tx = _Gs2326PortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 7),
    _Gs2326PortQoSQ2Tx_Type()
)
gs2326PortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ2Tx.setStatus("current")
_Gs2326PortQoSQ3Rx_Type = Counter64
_Gs2326PortQoSQ3Rx_Object = MibTableColumn
gs2326PortQoSQ3Rx = _Gs2326PortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 8),
    _Gs2326PortQoSQ3Rx_Type()
)
gs2326PortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ3Rx.setStatus("current")
_Gs2326PortQoSQ3Tx_Type = Counter64
_Gs2326PortQoSQ3Tx_Object = MibTableColumn
gs2326PortQoSQ3Tx = _Gs2326PortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 9),
    _Gs2326PortQoSQ3Tx_Type()
)
gs2326PortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ3Tx.setStatus("current")
_Gs2326PortQoSQ4Rx_Type = Counter64
_Gs2326PortQoSQ4Rx_Object = MibTableColumn
gs2326PortQoSQ4Rx = _Gs2326PortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 10),
    _Gs2326PortQoSQ4Rx_Type()
)
gs2326PortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ4Rx.setStatus("current")
_Gs2326PortQoSQ4Tx_Type = Counter64
_Gs2326PortQoSQ4Tx_Object = MibTableColumn
gs2326PortQoSQ4Tx = _Gs2326PortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 11),
    _Gs2326PortQoSQ4Tx_Type()
)
gs2326PortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ4Tx.setStatus("current")
_Gs2326PortQoSQ5Rx_Type = Counter64
_Gs2326PortQoSQ5Rx_Object = MibTableColumn
gs2326PortQoSQ5Rx = _Gs2326PortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 12),
    _Gs2326PortQoSQ5Rx_Type()
)
gs2326PortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ5Rx.setStatus("current")
_Gs2326PortQoSQ5Tx_Type = Counter64
_Gs2326PortQoSQ5Tx_Object = MibTableColumn
gs2326PortQoSQ5Tx = _Gs2326PortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 13),
    _Gs2326PortQoSQ5Tx_Type()
)
gs2326PortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ5Tx.setStatus("current")
_Gs2326PortQoSQ6Rx_Type = Counter64
_Gs2326PortQoSQ6Rx_Object = MibTableColumn
gs2326PortQoSQ6Rx = _Gs2326PortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 14),
    _Gs2326PortQoSQ6Rx_Type()
)
gs2326PortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ6Rx.setStatus("current")
_Gs2326PortQoSQ6Tx_Type = Counter64
_Gs2326PortQoSQ6Tx_Object = MibTableColumn
gs2326PortQoSQ6Tx = _Gs2326PortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 15),
    _Gs2326PortQoSQ6Tx_Type()
)
gs2326PortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ6Tx.setStatus("current")
_Gs2326PortQoSQ7Rx_Type = Counter64
_Gs2326PortQoSQ7Rx_Object = MibTableColumn
gs2326PortQoSQ7Rx = _Gs2326PortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 16),
    _Gs2326PortQoSQ7Rx_Type()
)
gs2326PortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ7Rx.setStatus("current")
_Gs2326PortQoSQ7Tx_Type = Counter64
_Gs2326PortQoSQ7Tx_Object = MibTableColumn
gs2326PortQoSQ7Tx = _Gs2326PortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 3, 2, 1, 17),
    _Gs2326PortQoSQ7Tx_Type()
)
gs2326PortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortQoSQ7Tx.setStatus("current")
_Gs2326SFPInfoTable_Object = MibTable
gs2326SFPInfoTable = _Gs2326SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4)
)
if mibBuilder.loadTexts:
    gs2326SFPInfoTable.setStatus("current")
_Gs2326SFPInfoEntry_Object = MibTableRow
gs2326SFPInfoEntry = _Gs2326SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1)
)
gs2326SFPInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2326SFPInfoEntry.setStatus("current")


class _Gs2326SFPInfoIndex_Type(Integer32):
    """Custom type gs2326SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326SFPInfoIndex_Type.__name__ = "Integer32"
_Gs2326SFPInfoIndex_Object = MibTableColumn
gs2326SFPInfoIndex = _Gs2326SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 1),
    _Gs2326SFPInfoIndex_Type()
)
gs2326SFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326SFPInfoIndex.setStatus("current")
_Gs2326SFPInfoPort_Type = DisplayString
_Gs2326SFPInfoPort_Object = MibTableColumn
gs2326SFPInfoPort = _Gs2326SFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 2),
    _Gs2326SFPInfoPort_Type()
)
gs2326SFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPInfoPort.setStatus("current")
_Gs2326SFPConnectorType_Type = DisplayString
_Gs2326SFPConnectorType_Object = MibTableColumn
gs2326SFPConnectorType = _Gs2326SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 3),
    _Gs2326SFPConnectorType_Type()
)
gs2326SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPConnectorType.setStatus("current")
_Gs2326SFPFiberType_Type = DisplayString
_Gs2326SFPFiberType_Object = MibTableColumn
gs2326SFPFiberType = _Gs2326SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 4),
    _Gs2326SFPFiberType_Type()
)
gs2326SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPFiberType.setStatus("current")
_Gs2326SFPTxCentralWavelength_Type = DisplayString
_Gs2326SFPTxCentralWavelength_Object = MibTableColumn
gs2326SFPTxCentralWavelength = _Gs2326SFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 5),
    _Gs2326SFPTxCentralWavelength_Type()
)
gs2326SFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPTxCentralWavelength.setStatus("current")
_Gs2326SFPBaudRate_Type = DisplayString
_Gs2326SFPBaudRate_Object = MibTableColumn
gs2326SFPBaudRate = _Gs2326SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 6),
    _Gs2326SFPBaudRate_Type()
)
gs2326SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPBaudRate.setStatus("current")
_Gs2326SFPVendorOUI_Type = DisplayString
_Gs2326SFPVendorOUI_Object = MibTableColumn
gs2326SFPVendorOUI = _Gs2326SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 7),
    _Gs2326SFPVendorOUI_Type()
)
gs2326SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPVendorOUI.setStatus("current")
_Gs2326SFPVendorName_Type = DisplayString
_Gs2326SFPVendorName_Object = MibTableColumn
gs2326SFPVendorName = _Gs2326SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 8),
    _Gs2326SFPVendorName_Type()
)
gs2326SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPVendorName.setStatus("current")
_Gs2326SFPVendorPN_Type = DisplayString
_Gs2326SFPVendorPN_Object = MibTableColumn
gs2326SFPVendorPN = _Gs2326SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 9),
    _Gs2326SFPVendorPN_Type()
)
gs2326SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPVendorPN.setStatus("current")
_Gs2326SFPVendorRev_Type = DisplayString
_Gs2326SFPVendorRev_Object = MibTableColumn
gs2326SFPVendorRev = _Gs2326SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 10),
    _Gs2326SFPVendorRev_Type()
)
gs2326SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPVendorRev.setStatus("current")
_Gs2326SFPVendorSN_Type = DisplayString
_Gs2326SFPVendorSN_Object = MibTableColumn
gs2326SFPVendorSN = _Gs2326SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 11),
    _Gs2326SFPVendorSN_Type()
)
gs2326SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPVendorSN.setStatus("current")
_Gs2326SFPDateCode_Type = DisplayString
_Gs2326SFPDateCode_Object = MibTableColumn
gs2326SFPDateCode = _Gs2326SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 12),
    _Gs2326SFPDateCode_Type()
)
gs2326SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPDateCode.setStatus("current")
_Gs2326SFPTemperature_Type = DisplayString
_Gs2326SFPTemperature_Object = MibTableColumn
gs2326SFPTemperature = _Gs2326SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 13),
    _Gs2326SFPTemperature_Type()
)
gs2326SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPTemperature.setStatus("current")
_Gs2326SFPVcc_Type = DisplayString
_Gs2326SFPVcc_Object = MibTableColumn
gs2326SFPVcc = _Gs2326SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 14),
    _Gs2326SFPVcc_Type()
)
gs2326SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPVcc.setStatus("current")
_Gs2326SFPMon1Bias_Type = DisplayString
_Gs2326SFPMon1Bias_Object = MibTableColumn
gs2326SFPMon1Bias = _Gs2326SFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 15),
    _Gs2326SFPMon1Bias_Type()
)
gs2326SFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPMon1Bias.setStatus("current")
_Gs2326SFPMon2TxPWR_Type = DisplayString
_Gs2326SFPMon2TxPWR_Object = MibTableColumn
gs2326SFPMon2TxPWR = _Gs2326SFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 16),
    _Gs2326SFPMon2TxPWR_Type()
)
gs2326SFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPMon2TxPWR.setStatus("current")
_Gs2326SFPMon3RxPWR_Type = DisplayString
_Gs2326SFPMon3RxPWR_Object = MibTableColumn
gs2326SFPMon3RxPWR = _Gs2326SFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 4, 1, 17),
    _Gs2326SFPMon3RxPWR_Type()
)
gs2326SFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SFPMon3RxPWR.setStatus("current")
_Gs2326PortEEETable_Object = MibTable
gs2326PortEEETable = _Gs2326PortEEETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2326PortEEETable.setStatus("current")
_Gs2326PortEEEEntry_Object = MibTableRow
gs2326PortEEEEntry = _Gs2326PortEEEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1)
)
gs2326PortEEEEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortEEEPort"),
)
if mibBuilder.loadTexts:
    gs2326PortEEEEntry.setStatus("current")


class _Gs2326PortEEEPort_Type(Integer32):
    """Custom type gs2326PortEEEPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortEEEPort_Type.__name__ = "Integer32"
_Gs2326PortEEEPort_Object = MibTableColumn
gs2326PortEEEPort = _Gs2326PortEEEPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 1),
    _Gs2326PortEEEPort_Type()
)
gs2326PortEEEPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortEEEPort.setStatus("current")


class _Gs2326PortEEEMode_Type(Integer32):
    """Custom type gs2326PortEEEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEMode_Type.__name__ = "Integer32"
_Gs2326PortEEEMode_Object = MibTableColumn
gs2326PortEEEMode = _Gs2326PortEEEMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 2),
    _Gs2326PortEEEMode_Type()
)
gs2326PortEEEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEMode.setStatus("current")


class _Gs2326PortEEEUrgentQueue1_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue1_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue1_Object = MibTableColumn
gs2326PortEEEUrgentQueue1 = _Gs2326PortEEEUrgentQueue1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 3),
    _Gs2326PortEEEUrgentQueue1_Type()
)
gs2326PortEEEUrgentQueue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue1.setStatus("current")


class _Gs2326PortEEEUrgentQueue2_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue2_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue2_Object = MibTableColumn
gs2326PortEEEUrgentQueue2 = _Gs2326PortEEEUrgentQueue2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 4),
    _Gs2326PortEEEUrgentQueue2_Type()
)
gs2326PortEEEUrgentQueue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue2.setStatus("current")


class _Gs2326PortEEEUrgentQueue3_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue3_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue3_Object = MibTableColumn
gs2326PortEEEUrgentQueue3 = _Gs2326PortEEEUrgentQueue3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 5),
    _Gs2326PortEEEUrgentQueue3_Type()
)
gs2326PortEEEUrgentQueue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue3.setStatus("current")


class _Gs2326PortEEEUrgentQueue4_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue4_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue4_Object = MibTableColumn
gs2326PortEEEUrgentQueue4 = _Gs2326PortEEEUrgentQueue4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 6),
    _Gs2326PortEEEUrgentQueue4_Type()
)
gs2326PortEEEUrgentQueue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue4.setStatus("current")


class _Gs2326PortEEEUrgentQueue5_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue5_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue5_Object = MibTableColumn
gs2326PortEEEUrgentQueue5 = _Gs2326PortEEEUrgentQueue5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 7),
    _Gs2326PortEEEUrgentQueue5_Type()
)
gs2326PortEEEUrgentQueue5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue5.setStatus("current")


class _Gs2326PortEEEUrgentQueue6_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue6_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue6_Object = MibTableColumn
gs2326PortEEEUrgentQueue6 = _Gs2326PortEEEUrgentQueue6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 8),
    _Gs2326PortEEEUrgentQueue6_Type()
)
gs2326PortEEEUrgentQueue6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue6.setStatus("current")


class _Gs2326PortEEEUrgentQueue7_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue7_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue7_Object = MibTableColumn
gs2326PortEEEUrgentQueue7 = _Gs2326PortEEEUrgentQueue7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 9),
    _Gs2326PortEEEUrgentQueue7_Type()
)
gs2326PortEEEUrgentQueue7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue7.setStatus("current")


class _Gs2326PortEEEUrgentQueue8_Type(Integer32):
    """Custom type gs2326PortEEEUrgentQueue8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortEEEUrgentQueue8_Type.__name__ = "Integer32"
_Gs2326PortEEEUrgentQueue8_Object = MibTableColumn
gs2326PortEEEUrgentQueue8 = _Gs2326PortEEEUrgentQueue8_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1, 5, 1, 10),
    _Gs2326PortEEEUrgentQueue8_Type()
)
gs2326PortEEEUrgentQueue8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortEEEUrgentQueue8.setStatus("current")
_Gs2326VoiceVLAN_ObjectIdentity = ObjectIdentity
gs2326VoiceVLAN = _Gs2326VoiceVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2)
)
_Gs2326VoiceVLANConf_ObjectIdentity = ObjectIdentity
gs2326VoiceVLANConf = _Gs2326VoiceVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1)
)


class _Gs2326VoiceVLANMode_Type(Integer32):
    """Custom type gs2326VoiceVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326VoiceVLANMode_Type.__name__ = "Integer32"
_Gs2326VoiceVLANMode_Object = MibScalar
gs2326VoiceVLANMode = _Gs2326VoiceVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 1),
    _Gs2326VoiceVLANMode_Type()
)
gs2326VoiceVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANMode.setStatus("current")


class _Gs2326VoiceVLANVLANId_Type(Integer32):
    """Custom type gs2326VoiceVLANVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326VoiceVLANVLANId_Type.__name__ = "Integer32"
_Gs2326VoiceVLANVLANId_Object = MibScalar
gs2326VoiceVLANVLANId = _Gs2326VoiceVLANVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 2),
    _Gs2326VoiceVLANVLANId_Type()
)
gs2326VoiceVLANVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANVLANId.setStatus("current")


class _Gs2326VoiceVLANAgingTime_Type(Integer32):
    """Custom type gs2326VoiceVLANAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2326VoiceVLANAgingTime_Type.__name__ = "Integer32"
_Gs2326VoiceVLANAgingTime_Object = MibScalar
gs2326VoiceVLANAgingTime = _Gs2326VoiceVLANAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 3),
    _Gs2326VoiceVLANAgingTime_Type()
)
gs2326VoiceVLANAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANAgingTime.setStatus("current")


class _Gs2326VoiceVLANTrafficClass_Type(Integer32):
    """Custom type gs2326VoiceVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326VoiceVLANTrafficClass_Type.__name__ = "Integer32"
_Gs2326VoiceVLANTrafficClass_Object = MibScalar
gs2326VoiceVLANTrafficClass = _Gs2326VoiceVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 4),
    _Gs2326VoiceVLANTrafficClass_Type()
)
gs2326VoiceVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANTrafficClass.setStatus("current")
_Gs2326VoiceVLANPortTable_Object = MibTable
gs2326VoiceVLANPortTable = _Gs2326VoiceVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2326VoiceVLANPortTable.setStatus("current")
_Gs2326VoiceVLANPortEntry_Object = MibTableRow
gs2326VoiceVLANPortEntry = _Gs2326VoiceVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5, 1)
)
gs2326VoiceVLANPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326VoiceVLANPort"),
)
if mibBuilder.loadTexts:
    gs2326VoiceVLANPortEntry.setStatus("current")


class _Gs2326VoiceVLANPort_Type(Integer32):
    """Custom type gs2326VoiceVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326VoiceVLANPort_Type.__name__ = "Integer32"
_Gs2326VoiceVLANPort_Object = MibTableColumn
gs2326VoiceVLANPort = _Gs2326VoiceVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5, 1, 1),
    _Gs2326VoiceVLANPort_Type()
)
gs2326VoiceVLANPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326VoiceVLANPort.setStatus("current")


class _Gs2326VoiceVLANPortMode_Type(Integer32):
    """Custom type gs2326VoiceVLANPortMode based on Integer32"""
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


_Gs2326VoiceVLANPortMode_Type.__name__ = "Integer32"
_Gs2326VoiceVLANPortMode_Object = MibTableColumn
gs2326VoiceVLANPortMode = _Gs2326VoiceVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5, 1, 2),
    _Gs2326VoiceVLANPortMode_Type()
)
gs2326VoiceVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANPortMode.setStatus("current")


class _Gs2326VoiceVLANPortSecurity_Type(Integer32):
    """Custom type gs2326VoiceVLANPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326VoiceVLANPortSecurity_Type.__name__ = "Integer32"
_Gs2326VoiceVLANPortSecurity_Object = MibTableColumn
gs2326VoiceVLANPortSecurity = _Gs2326VoiceVLANPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5, 1, 3),
    _Gs2326VoiceVLANPortSecurity_Type()
)
gs2326VoiceVLANPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANPortSecurity.setStatus("current")


class _Gs2326VoiceVLANPortDiscoveryProtocol_Type(Integer32):
    """Custom type gs2326VoiceVLANPortDiscoveryProtocol based on Integer32"""
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


_Gs2326VoiceVLANPortDiscoveryProtocol_Type.__name__ = "Integer32"
_Gs2326VoiceVLANPortDiscoveryProtocol_Object = MibTableColumn
gs2326VoiceVLANPortDiscoveryProtocol = _Gs2326VoiceVLANPortDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5, 1, 4),
    _Gs2326VoiceVLANPortDiscoveryProtocol_Type()
)
gs2326VoiceVLANPortDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANPortDiscoveryProtocol.setStatus("current")


class _Gs2326VoiceVLANSkipNAS_Type(Integer32):
    """Custom type gs2326VoiceVLANSkipNAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326VoiceVLANSkipNAS_Type.__name__ = "Integer32"
_Gs2326VoiceVLANSkipNAS_Object = MibScalar
gs2326VoiceVLANSkipNAS = _Gs2326VoiceVLANSkipNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 1, 5, 1, 5),
    _Gs2326VoiceVLANSkipNAS_Type()
)
gs2326VoiceVLANSkipNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANSkipNAS.setStatus("current")
_Gs2326VoiceVLANOUI_ObjectIdentity = ObjectIdentity
gs2326VoiceVLANOUI = _Gs2326VoiceVLANOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2)
)


class _Gs2326VoiceVLANOUICreate_Type(Integer32):
    """Custom type gs2326VoiceVLANOUICreate based on Integer32"""
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


_Gs2326VoiceVLANOUICreate_Type.__name__ = "Integer32"
_Gs2326VoiceVLANOUICreate_Object = MibScalar
gs2326VoiceVLANOUICreate = _Gs2326VoiceVLANOUICreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 1),
    _Gs2326VoiceVLANOUICreate_Type()
)
gs2326VoiceVLANOUICreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANOUICreate.setStatus("current")
_Gs2326VoiceVLANOUITable_Object = MibTable
gs2326VoiceVLANOUITable = _Gs2326VoiceVLANOUITable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326VoiceVLANOUITable.setStatus("current")
_Gs2326VoiceVLANOUIEntry_Object = MibTableRow
gs2326VoiceVLANOUIEntry = _Gs2326VoiceVLANOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 2, 1)
)
gs2326VoiceVLANOUIEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326VoiceVLANOUIIndex"),
)
if mibBuilder.loadTexts:
    gs2326VoiceVLANOUIEntry.setStatus("current")


class _Gs2326VoiceVLANOUIIndex_Type(Integer32):
    """Custom type gs2326VoiceVLANOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2326VoiceVLANOUIIndex_Type.__name__ = "Integer32"
_Gs2326VoiceVLANOUIIndex_Object = MibTableColumn
gs2326VoiceVLANOUIIndex = _Gs2326VoiceVLANOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 2, 1, 1),
    _Gs2326VoiceVLANOUIIndex_Type()
)
gs2326VoiceVLANOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326VoiceVLANOUIIndex.setStatus("current")


class _Gs2326VoiceVLANTelephonyOUI_Type(OctetString):
    """Custom type gs2326VoiceVLANTelephonyOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326VoiceVLANTelephonyOUI_Type.__name__ = "OctetString"
_Gs2326VoiceVLANTelephonyOUI_Object = MibTableColumn
gs2326VoiceVLANTelephonyOUI = _Gs2326VoiceVLANTelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 2, 1, 2),
    _Gs2326VoiceVLANTelephonyOUI_Type()
)
gs2326VoiceVLANTelephonyOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANTelephonyOUI.setStatus("current")


class _Gs2326VoiceVLANDescription_Type(DisplayString):
    """Custom type gs2326VoiceVLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326VoiceVLANDescription_Type.__name__ = "DisplayString"
_Gs2326VoiceVLANDescription_Object = MibTableColumn
gs2326VoiceVLANDescription = _Gs2326VoiceVLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 2, 1, 3),
    _Gs2326VoiceVLANDescription_Type()
)
gs2326VoiceVLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANDescription.setStatus("current")


class _Gs2326VoiceVLANOUIRowStatus_Type(Integer32):
    """Custom type gs2326VoiceVLANOUIRowStatus based on Integer32"""
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


_Gs2326VoiceVLANOUIRowStatus_Type.__name__ = "Integer32"
_Gs2326VoiceVLANOUIRowStatus_Object = MibTableColumn
gs2326VoiceVLANOUIRowStatus = _Gs2326VoiceVLANOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 2, 2, 2, 1, 4),
    _Gs2326VoiceVLANOUIRowStatus_Type()
)
gs2326VoiceVLANOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VoiceVLANOUIRowStatus.setStatus("current")
_Gs2326GARP_ObjectIdentity = ObjectIdentity
gs2326GARP = _Gs2326GARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3)
)
_Gs2326GARPConfTable_Object = MibTable
gs2326GARPConfTable = _Gs2326GARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gs2326GARPConfTable.setStatus("current")
_Gs2326GARPConfEntry_Object = MibTableRow
gs2326GARPConfEntry = _Gs2326GARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1)
)
gs2326GARPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326GARPConfPort"),
)
if mibBuilder.loadTexts:
    gs2326GARPConfEntry.setStatus("current")


class _Gs2326GARPConfPort_Type(Integer32):
    """Custom type gs2326GARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326GARPConfPort_Type.__name__ = "Integer32"
_Gs2326GARPConfPort_Object = MibTableColumn
gs2326GARPConfPort = _Gs2326GARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 1),
    _Gs2326GARPConfPort_Type()
)
gs2326GARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326GARPConfPort.setStatus("current")


class _Gs2326GARPJoinTimer_Type(Integer32):
    """Custom type gs2326GARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Gs2326GARPJoinTimer_Type.__name__ = "Integer32"
_Gs2326GARPJoinTimer_Object = MibTableColumn
gs2326GARPJoinTimer = _Gs2326GARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 2),
    _Gs2326GARPJoinTimer_Type()
)
gs2326GARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPJoinTimer.setStatus("current")


class _Gs2326GARPLeaveTimer_Type(Integer32):
    """Custom type gs2326GARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Gs2326GARPLeaveTimer_Type.__name__ = "Integer32"
_Gs2326GARPLeaveTimer_Object = MibTableColumn
gs2326GARPLeaveTimer = _Gs2326GARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 3),
    _Gs2326GARPLeaveTimer_Type()
)
gs2326GARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPLeaveTimer.setStatus("current")


class _Gs2326GARPLeaveAllTimer_Type(Integer32):
    """Custom type gs2326GARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Gs2326GARPLeaveAllTimer_Type.__name__ = "Integer32"
_Gs2326GARPLeaveAllTimer_Object = MibTableColumn
gs2326GARPLeaveAllTimer = _Gs2326GARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 4),
    _Gs2326GARPLeaveAllTimer_Type()
)
gs2326GARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPLeaveAllTimer.setStatus("current")


class _Gs2326GARPApplicantion_Type(Integer32):
    """Custom type gs2326GARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gvrp", 1)
    )


_Gs2326GARPApplicantion_Type.__name__ = "Integer32"
_Gs2326GARPApplicantion_Object = MibTableColumn
gs2326GARPApplicantion = _Gs2326GARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 5),
    _Gs2326GARPApplicantion_Type()
)
gs2326GARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPApplicantion.setStatus("current")


class _Gs2326GARPAttributeType_Type(Integer32):
    """Custom type gs2326GARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_Gs2326GARPAttributeType_Type.__name__ = "Integer32"
_Gs2326GARPAttributeType_Object = MibTableColumn
gs2326GARPAttributeType = _Gs2326GARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 6),
    _Gs2326GARPAttributeType_Type()
)
gs2326GARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPAttributeType.setStatus("current")


class _Gs2326GARPApplicant_Type(Integer32):
    """Custom type gs2326GARPApplicant based on Integer32"""
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


_Gs2326GARPApplicant_Type.__name__ = "Integer32"
_Gs2326GARPApplicant_Object = MibTableColumn
gs2326GARPApplicant = _Gs2326GARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 1, 1, 7),
    _Gs2326GARPApplicant_Type()
)
gs2326GARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GARPApplicant.setStatus("current")
_Gs2326GARPStatisticsTable_Object = MibTable
gs2326GARPStatisticsTable = _Gs2326GARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326GARPStatisticsTable.setStatus("current")
_Gs2326GARPStatisticsEntry_Object = MibTableRow
gs2326GARPStatisticsEntry = _Gs2326GARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 2, 1)
)
gs2326GARPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326GARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2326GARPStatisticsEntry.setStatus("current")


class _Gs2326GARPStatisticsPort_Type(Integer32):
    """Custom type gs2326GARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326GARPStatisticsPort_Type.__name__ = "Integer32"
_Gs2326GARPStatisticsPort_Object = MibTableColumn
gs2326GARPStatisticsPort = _Gs2326GARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 2, 1, 1),
    _Gs2326GARPStatisticsPort_Type()
)
gs2326GARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326GARPStatisticsPort.setStatus("current")
_Gs2326GARPStatisticsPeerMAC_Type = DisplayString
_Gs2326GARPStatisticsPeerMAC_Object = MibTableColumn
gs2326GARPStatisticsPeerMAC = _Gs2326GARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 2, 1, 2),
    _Gs2326GARPStatisticsPeerMAC_Type()
)
gs2326GARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326GARPStatisticsPeerMAC.setStatus("current")
_Gs2326GARPStatisticsFailedCount_Type = Counter32
_Gs2326GARPStatisticsFailedCount_Object = MibTableColumn
gs2326GARPStatisticsFailedCount = _Gs2326GARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 3, 2, 1, 3),
    _Gs2326GARPStatisticsFailedCount_Type()
)
gs2326GARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326GARPStatisticsFailedCount.setStatus("current")
_Gs2326GVRP_ObjectIdentity = ObjectIdentity
gs2326GVRP = _Gs2326GVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4)
)
_Gs2326GVRPConf_ObjectIdentity = ObjectIdentity
gs2326GVRPConf = _Gs2326GVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1)
)


class _Gs2326GVRPMode_Type(Integer32):
    """Custom type gs2326GVRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326GVRPMode_Type.__name__ = "Integer32"
_Gs2326GVRPMode_Object = MibScalar
gs2326GVRPMode = _Gs2326GVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1, 1),
    _Gs2326GVRPMode_Type()
)
gs2326GVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GVRPMode.setStatus("current")
_Gs2326GVRPConfTable_Object = MibTable
gs2326GVRPConfTable = _Gs2326GVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326GVRPConfTable.setStatus("current")
_Gs2326GVRPConfEntry_Object = MibTableRow
gs2326GVRPConfEntry = _Gs2326GVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1, 2, 1)
)
gs2326GVRPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326GVRPConfPort"),
)
if mibBuilder.loadTexts:
    gs2326GVRPConfEntry.setStatus("current")


class _Gs2326GVRPConfPort_Type(Integer32):
    """Custom type gs2326GVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326GVRPConfPort_Type.__name__ = "Integer32"
_Gs2326GVRPConfPort_Object = MibTableColumn
gs2326GVRPConfPort = _Gs2326GVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1, 2, 1, 1),
    _Gs2326GVRPConfPort_Type()
)
gs2326GVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326GVRPConfPort.setStatus("current")


class _Gs2326GVRPConfPortMode_Type(Integer32):
    """Custom type gs2326GVRPConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326GVRPConfPortMode_Type.__name__ = "Integer32"
_Gs2326GVRPConfPortMode_Object = MibTableColumn
gs2326GVRPConfPortMode = _Gs2326GVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1, 2, 1, 2),
    _Gs2326GVRPConfPortMode_Type()
)
gs2326GVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GVRPConfPortMode.setStatus("current")


class _Gs2326GVRPConfPortRRole_Type(Integer32):
    """Custom type gs2326GVRPConfPortRRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326GVRPConfPortRRole_Type.__name__ = "Integer32"
_Gs2326GVRPConfPortRRole_Object = MibTableColumn
gs2326GVRPConfPortRRole = _Gs2326GVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 1, 2, 1, 3),
    _Gs2326GVRPConfPortRRole_Type()
)
gs2326GVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326GVRPConfPortRRole.setStatus("current")
_Gs2326GVRPStatisticsTable_Object = MibTable
gs2326GVRPStatisticsTable = _Gs2326GVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326GVRPStatisticsTable.setStatus("current")
_Gs2326GVRPStatisticsEntry_Object = MibTableRow
gs2326GVRPStatisticsEntry = _Gs2326GVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 2, 1)
)
gs2326GVRPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326GVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2326GVRPStatisticsEntry.setStatus("current")


class _Gs2326GVRPStatisticsPort_Type(Integer32):
    """Custom type gs2326GVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326GVRPStatisticsPort_Type.__name__ = "Integer32"
_Gs2326GVRPStatisticsPort_Object = MibTableColumn
gs2326GVRPStatisticsPort = _Gs2326GVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 2, 1, 1),
    _Gs2326GVRPStatisticsPort_Type()
)
gs2326GVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326GVRPStatisticsPort.setStatus("current")
_Gs2326GVRPStatisticsJoinTxCnt_Type = Counter32
_Gs2326GVRPStatisticsJoinTxCnt_Object = MibTableColumn
gs2326GVRPStatisticsJoinTxCnt = _Gs2326GVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 2, 1, 2),
    _Gs2326GVRPStatisticsJoinTxCnt_Type()
)
gs2326GVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326GVRPStatisticsJoinTxCnt.setStatus("current")
_Gs2326GVRPStatisticsLeaveTxCnt_Type = Counter32
_Gs2326GVRPStatisticsLeaveTxCnt_Object = MibTableColumn
gs2326GVRPStatisticsLeaveTxCnt = _Gs2326GVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 4, 2, 1, 3),
    _Gs2326GVRPStatisticsLeaveTxCnt_Type()
)
gs2326GVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326GVRPStatisticsLeaveTxCnt.setStatus("current")
_Gs2326Mirroring_ObjectIdentity = ObjectIdentity
gs2326Mirroring = _Gs2326Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 6)
)


class _Gs2326PortToMirrorOn_Type(Integer32):
    """Custom type gs2326PortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2326PortToMirrorOn_Type.__name__ = "Integer32"
_Gs2326PortToMirrorOn_Object = MibScalar
gs2326PortToMirrorOn = _Gs2326PortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 6, 1),
    _Gs2326PortToMirrorOn_Type()
)
gs2326PortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortToMirrorOn.setStatus("current")
_Gs2326MirrorTable_Object = MibTable
gs2326MirrorTable = _Gs2326MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gs2326MirrorTable.setStatus("current")
_Gs2326MirrorEntry_Object = MibTableRow
gs2326MirrorEntry = _Gs2326MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 6, 2, 1)
)
gs2326MirrorEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MirrorPort"),
)
if mibBuilder.loadTexts:
    gs2326MirrorEntry.setStatus("current")


class _Gs2326MirrorPort_Type(Integer32):
    """Custom type gs2326MirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MirrorPort_Type.__name__ = "Integer32"
_Gs2326MirrorPort_Object = MibTableColumn
gs2326MirrorPort = _Gs2326MirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 6, 2, 1, 1),
    _Gs2326MirrorPort_Type()
)
gs2326MirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MirrorPort.setStatus("current")


class _Gs2326MirrorMode_Type(Integer32):
    """Custom type gs2326MirrorMode based on Integer32"""
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


_Gs2326MirrorMode_Type.__name__ = "Integer32"
_Gs2326MirrorMode_Object = MibTableColumn
gs2326MirrorMode = _Gs2326MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 6, 2, 1, 2),
    _Gs2326MirrorMode_Type()
)
gs2326MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MirrorMode.setStatus("current")
_Gs2326TrapEventSeverity_ObjectIdentity = ObjectIdentity
gs2326TrapEventSeverity = _Gs2326TrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7)
)


class _Gs2326TrapEventSeverityACL_Type(Integer32):
    """Custom type gs2326TrapEventSeverityACL based on Integer32"""
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


_Gs2326TrapEventSeverityACL_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityACL_Object = MibScalar
gs2326TrapEventSeverityACL = _Gs2326TrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 1),
    _Gs2326TrapEventSeverityACL_Type()
)
gs2326TrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityACL.setStatus("current")


class _Gs2326TrapEventSeverityACLLog_Type(Integer32):
    """Custom type gs2326TrapEventSeverityACLLog based on Integer32"""
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


_Gs2326TrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityACLLog_Object = MibScalar
gs2326TrapEventSeverityACLLog = _Gs2326TrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 2),
    _Gs2326TrapEventSeverityACLLog_Type()
)
gs2326TrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityACLLog.setStatus("current")


class _Gs2326TrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type gs2326TrapEventSeverityAccessMgmt based on Integer32"""
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


_Gs2326TrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityAccessMgmt_Object = MibScalar
gs2326TrapEventSeverityAccessMgmt = _Gs2326TrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 3),
    _Gs2326TrapEventSeverityAccessMgmt_Type()
)
gs2326TrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityAccessMgmt.setStatus("current")


class _Gs2326TrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type gs2326TrapEventSeverityAuthFailed based on Integer32"""
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


_Gs2326TrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityAuthFailed_Object = MibScalar
gs2326TrapEventSeverityAuthFailed = _Gs2326TrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 4),
    _Gs2326TrapEventSeverityAuthFailed_Type()
)
gs2326TrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityAuthFailed.setStatus("current")


class _Gs2326TrapEventSeverityColdStart_Type(Integer32):
    """Custom type gs2326TrapEventSeverityColdStart based on Integer32"""
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


_Gs2326TrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityColdStart_Object = MibScalar
gs2326TrapEventSeverityColdStart = _Gs2326TrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 5),
    _Gs2326TrapEventSeverityColdStart_Type()
)
gs2326TrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityColdStart.setStatus("current")


class _Gs2326TrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type gs2326TrapEventSeverityConfigInfo based on Integer32"""
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


_Gs2326TrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityConfigInfo_Object = MibScalar
gs2326TrapEventSeverityConfigInfo = _Gs2326TrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 6),
    _Gs2326TrapEventSeverityConfigInfo_Type()
)
gs2326TrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityConfigInfo.setStatus("current")


class _Gs2326TrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type gs2326TrapEventSeverityFirmwareUpgrade based on Integer32"""
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


_Gs2326TrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityFirmwareUpgrade_Object = MibScalar
gs2326TrapEventSeverityFirmwareUpgrade = _Gs2326TrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 7),
    _Gs2326TrapEventSeverityFirmwareUpgrade_Type()
)
gs2326TrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Gs2326TrapEventSeverityImportExport_Type(Integer32):
    """Custom type gs2326TrapEventSeverityImportExport based on Integer32"""
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


_Gs2326TrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityImportExport_Object = MibScalar
gs2326TrapEventSeverityImportExport = _Gs2326TrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 8),
    _Gs2326TrapEventSeverityImportExport_Type()
)
gs2326TrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityImportExport.setStatus("current")


class _Gs2326TrapEventSeverityLACP_Type(Integer32):
    """Custom type gs2326TrapEventSeverityLACP based on Integer32"""
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


_Gs2326TrapEventSeverityLACP_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityLACP_Object = MibScalar
gs2326TrapEventSeverityLACP = _Gs2326TrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 9),
    _Gs2326TrapEventSeverityLACP_Type()
)
gs2326TrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityLACP.setStatus("current")


class _Gs2326TrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type gs2326TrapEventSeverityLinkStatus based on Integer32"""
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


_Gs2326TrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityLinkStatus_Object = MibScalar
gs2326TrapEventSeverityLinkStatus = _Gs2326TrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 10),
    _Gs2326TrapEventSeverityLinkStatus_Type()
)
gs2326TrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityLinkStatus.setStatus("current")


class _Gs2326TrapEventSeverityLogin_Type(Integer32):
    """Custom type gs2326TrapEventSeverityLogin based on Integer32"""
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


_Gs2326TrapEventSeverityLogin_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityLogin_Object = MibScalar
gs2326TrapEventSeverityLogin = _Gs2326TrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 11),
    _Gs2326TrapEventSeverityLogin_Type()
)
gs2326TrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityLogin.setStatus("current")


class _Gs2326TrapEventSeverityLogout_Type(Integer32):
    """Custom type gs2326TrapEventSeverityLogout based on Integer32"""
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


_Gs2326TrapEventSeverityLogout_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityLogout_Object = MibScalar
gs2326TrapEventSeverityLogout = _Gs2326TrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 12),
    _Gs2326TrapEventSeverityLogout_Type()
)
gs2326TrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityLogout.setStatus("current")


class _Gs2326TrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type gs2326TrapEventSeverityLoopProtect based on Integer32"""
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


_Gs2326TrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityLoopProtect_Object = MibScalar
gs2326TrapEventSeverityLoopProtect = _Gs2326TrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 13),
    _Gs2326TrapEventSeverityLoopProtect_Type()
)
gs2326TrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityLoopProtect.setStatus("current")


class _Gs2326TrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type gs2326TrapEventSeverityMgmtIPChange based on Integer32"""
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


_Gs2326TrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityMgmtIPChange_Object = MibScalar
gs2326TrapEventSeverityMgmtIPChange = _Gs2326TrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 14),
    _Gs2326TrapEventSeverityMgmtIPChange_Type()
)
gs2326TrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityMgmtIPChange.setStatus("current")


class _Gs2326TrapEventSeverityModuleChange_Type(Integer32):
    """Custom type gs2326TrapEventSeverityModuleChange based on Integer32"""
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


_Gs2326TrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityModuleChange_Object = MibScalar
gs2326TrapEventSeverityModuleChange = _Gs2326TrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 15),
    _Gs2326TrapEventSeverityModuleChange_Type()
)
gs2326TrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityModuleChange.setStatus("current")


class _Gs2326TrapEventSeverityNAS_Type(Integer32):
    """Custom type gs2326TrapEventSeverityNAS based on Integer32"""
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


_Gs2326TrapEventSeverityNAS_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityNAS_Object = MibScalar
gs2326TrapEventSeverityNAS = _Gs2326TrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 16),
    _Gs2326TrapEventSeverityNAS_Type()
)
gs2326TrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityNAS.setStatus("current")


class _Gs2326TrapEventSeverityPasswordChange_Type(Integer32):
    """Custom type gs2326TrapEventSeverityPasswordChange based on Integer32"""
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


_Gs2326TrapEventSeverityPasswordChange_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityPasswordChange_Object = MibScalar
gs2326TrapEventSeverityPasswordChange = _Gs2326TrapEventSeverityPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 17),
    _Gs2326TrapEventSeverityPasswordChange_Type()
)
gs2326TrapEventSeverityPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityPasswordChange.setStatus("current")


class _Gs2326TrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type gs2326TrapEventSeverityPortSecurity based on Integer32"""
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


_Gs2326TrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityPortSecurity_Object = MibScalar
gs2326TrapEventSeverityPortSecurity = _Gs2326TrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 18),
    _Gs2326TrapEventSeverityPortSecurity_Type()
)
gs2326TrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityPortSecurity.setStatus("current")


class _Gs2326TrapEventSeverityVLAN_Type(Integer32):
    """Custom type gs2326TrapEventSeverityVLAN based on Integer32"""
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


_Gs2326TrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityVLAN_Object = MibScalar
gs2326TrapEventSeverityVLAN = _Gs2326TrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 20),
    _Gs2326TrapEventSeverityVLAN_Type()
)
gs2326TrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityVLAN.setStatus("current")


class _Gs2326TrapEventSeverityWarmStart_Type(Integer32):
    """Custom type gs2326TrapEventSeverityWarmStart based on Integer32"""
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


_Gs2326TrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityWarmStart_Object = MibScalar
gs2326TrapEventSeverityWarmStart = _Gs2326TrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 21),
    _Gs2326TrapEventSeverityWarmStart_Type()
)
gs2326TrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityWarmStart.setStatus("current")


class _Gs2326TrapEventSeverityARPConflict_Type(Integer32):
    """Custom type gs2326TrapEventSeverityARPConflict based on Integer32"""
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


_Gs2326TrapEventSeverityARPConflict_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityARPConflict_Object = MibScalar
gs2326TrapEventSeverityARPConflict = _Gs2326TrapEventSeverityARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 25),
    _Gs2326TrapEventSeverityARPConflict_Type()
)
gs2326TrapEventSeverityARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityARPConflict.setStatus("current")


class _Gs2326TrapEventSeveritySpoofingLimit_Type(Integer32):
    """Custom type gs2326TrapEventSeveritySpoofingLimit based on Integer32"""
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


_Gs2326TrapEventSeveritySpoofingLimit_Type.__name__ = "Integer32"
_Gs2326TrapEventSeveritySpoofingLimit_Object = MibScalar
gs2326TrapEventSeveritySpoofingLimit = _Gs2326TrapEventSeveritySpoofingLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 27),
    _Gs2326TrapEventSeveritySpoofingLimit_Type()
)
gs2326TrapEventSeveritySpoofingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeveritySpoofingLimit.setStatus("current")


class _Gs2326TrapEventSeverityStaticARPConflict_Type(Integer32):
    """Custom type gs2326TrapEventSeverityStaticARPConflict based on Integer32"""
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


_Gs2326TrapEventSeverityStaticARPConflict_Type.__name__ = "Integer32"
_Gs2326TrapEventSeverityStaticARPConflict_Object = MibScalar
gs2326TrapEventSeverityStaticARPConflict = _Gs2326TrapEventSeverityStaticARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 7, 28),
    _Gs2326TrapEventSeverityStaticARPConflict_Type()
)
gs2326TrapEventSeverityStaticARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TrapEventSeverityStaticARPConflict.setStatus("current")
_Gs2326SMTP_ObjectIdentity = ObjectIdentity
gs2326SMTP = _Gs2326SMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8)
)
_Gs2326SMTPMailServer_Type = DisplayString
_Gs2326SMTPMailServer_Object = MibScalar
gs2326SMTPMailServer = _Gs2326SMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 1),
    _Gs2326SMTPMailServer_Type()
)
gs2326SMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPMailServer.setStatus("current")
_Gs2326SMTPUserName_Type = DisplayString
_Gs2326SMTPUserName_Object = MibScalar
gs2326SMTPUserName = _Gs2326SMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 2),
    _Gs2326SMTPUserName_Type()
)
gs2326SMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPUserName.setStatus("current")
_Gs2326SMTPPassword_Type = DisplayString
_Gs2326SMTPPassword_Object = MibScalar
gs2326SMTPPassword = _Gs2326SMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 3),
    _Gs2326SMTPPassword_Type()
)
gs2326SMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPPassword.setStatus("current")


class _Gs2326SMTPServeriryLevel_Type(Integer32):
    """Custom type gs2326SMTPServeriryLevel based on Integer32"""
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


_Gs2326SMTPServeriryLevel_Type.__name__ = "Integer32"
_Gs2326SMTPServeriryLevel_Object = MibScalar
gs2326SMTPServeriryLevel = _Gs2326SMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 4),
    _Gs2326SMTPServeriryLevel_Type()
)
gs2326SMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPServeriryLevel.setStatus("current")
_Gs2326SMTPSender_Type = DisplayString
_Gs2326SMTPSender_Object = MibScalar
gs2326SMTPSender = _Gs2326SMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 5),
    _Gs2326SMTPSender_Type()
)
gs2326SMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPSender.setStatus("current")
_Gs2326SMTPReturnPath_Type = DisplayString
_Gs2326SMTPReturnPath_Object = MibScalar
gs2326SMTPReturnPath = _Gs2326SMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 6),
    _Gs2326SMTPReturnPath_Type()
)
gs2326SMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPReturnPath.setStatus("current")
_Gs2326SMTPEmailAddress1_Type = DisplayString
_Gs2326SMTPEmailAddress1_Object = MibScalar
gs2326SMTPEmailAddress1 = _Gs2326SMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 7),
    _Gs2326SMTPEmailAddress1_Type()
)
gs2326SMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPEmailAddress1.setStatus("current")
_Gs2326SMTPEmailAddress2_Type = DisplayString
_Gs2326SMTPEmailAddress2_Object = MibScalar
gs2326SMTPEmailAddress2 = _Gs2326SMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 8),
    _Gs2326SMTPEmailAddress2_Type()
)
gs2326SMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPEmailAddress2.setStatus("current")
_Gs2326SMTPEmailAddress3_Type = DisplayString
_Gs2326SMTPEmailAddress3_Object = MibScalar
gs2326SMTPEmailAddress3 = _Gs2326SMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 9),
    _Gs2326SMTPEmailAddress3_Type()
)
gs2326SMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPEmailAddress3.setStatus("current")
_Gs2326SMTPEmailAddress4_Type = DisplayString
_Gs2326SMTPEmailAddress4_Object = MibScalar
gs2326SMTPEmailAddress4 = _Gs2326SMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 10),
    _Gs2326SMTPEmailAddress4_Type()
)
gs2326SMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPEmailAddress4.setStatus("current")
_Gs2326SMTPEmailAddress5_Type = DisplayString
_Gs2326SMTPEmailAddress5_Object = MibScalar
gs2326SMTPEmailAddress5 = _Gs2326SMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 11),
    _Gs2326SMTPEmailAddress5_Type()
)
gs2326SMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPEmailAddress5.setStatus("current")
_Gs2326SMTPEmailAddress6_Type = DisplayString
_Gs2326SMTPEmailAddress6_Object = MibScalar
gs2326SMTPEmailAddress6 = _Gs2326SMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 8, 12),
    _Gs2326SMTPEmailAddress6_Type()
)
gs2326SMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SMTPEmailAddress6.setStatus("current")
_Gs2326ACL_ObjectIdentity = ObjectIdentity
gs2326ACL = _Gs2326ACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9)
)
_Gs2326ACLPortsConfTable_Object = MibTable
gs2326ACLPortsConfTable = _Gs2326ACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1)
)
if mibBuilder.loadTexts:
    gs2326ACLPortsConfTable.setStatus("current")
_Gs2326ACLPortsConfEntry_Object = MibTableRow
gs2326ACLPortsConfEntry = _Gs2326ACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1)
)
gs2326ACLPortsConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    gs2326ACLPortsConfEntry.setStatus("current")


class _Gs2326ACLPortsConfPort_Type(Integer32):
    """Custom type gs2326ACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ACLPortsConfPort_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfPort_Object = MibTableColumn
gs2326ACLPortsConfPort = _Gs2326ACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 1),
    _Gs2326ACLPortsConfPort_Type()
)
gs2326ACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfPort.setStatus("current")


class _Gs2326ACLPortsConfPolicyID_Type(Integer32):
    """Custom type gs2326ACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2326ACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfPolicyID_Object = MibTableColumn
gs2326ACLPortsConfPolicyID = _Gs2326ACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 2),
    _Gs2326ACLPortsConfPolicyID_Type()
)
gs2326ACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfPolicyID.setStatus("current")


class _Gs2326ACLPortsConfAction_Type(Integer32):
    """Custom type gs2326ACLPortsConfAction based on Integer32"""
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


_Gs2326ACLPortsConfAction_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfAction_Object = MibTableColumn
gs2326ACLPortsConfAction = _Gs2326ACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 3),
    _Gs2326ACLPortsConfAction_Type()
)
gs2326ACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfAction.setStatus("current")


class _Gs2326ACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type gs2326ACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2326ACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfRateLimiterID_Object = MibTableColumn
gs2326ACLPortsConfRateLimiterID = _Gs2326ACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 4),
    _Gs2326ACLPortsConfRateLimiterID_Type()
)
gs2326ACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfRateLimiterID.setStatus("current")


class _Gs2326ACLPortsConfPortRedirect_Type(Integer32):
    """Custom type gs2326ACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gs2326ACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfPortRedirect_Object = MibTableColumn
gs2326ACLPortsConfPortRedirect = _Gs2326ACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 5),
    _Gs2326ACLPortsConfPortRedirect_Type()
)
gs2326ACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfPortRedirect.setStatus("current")


class _Gs2326ACLPortsConfMirror_Type(Integer32):
    """Custom type gs2326ACLPortsConfMirror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLPortsConfMirror_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfMirror_Object = MibTableColumn
gs2326ACLPortsConfMirror = _Gs2326ACLPortsConfMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 6),
    _Gs2326ACLPortsConfMirror_Type()
)
gs2326ACLPortsConfMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfMirror.setStatus("current")


class _Gs2326ACLPortsConfLogging_Type(Integer32):
    """Custom type gs2326ACLPortsConfLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLPortsConfLogging_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfLogging_Object = MibTableColumn
gs2326ACLPortsConfLogging = _Gs2326ACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 7),
    _Gs2326ACLPortsConfLogging_Type()
)
gs2326ACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfLogging.setStatus("current")


class _Gs2326ACLPortsConfShutdown_Type(Integer32):
    """Custom type gs2326ACLPortsConfShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLPortsConfShutdown_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfShutdown_Object = MibTableColumn
gs2326ACLPortsConfShutdown = _Gs2326ACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 8),
    _Gs2326ACLPortsConfShutdown_Type()
)
gs2326ACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfShutdown.setStatus("current")


class _Gs2326ACLPortsConfState_Type(Integer32):
    """Custom type gs2326ACLPortsConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLPortsConfState_Type.__name__ = "Integer32"
_Gs2326ACLPortsConfState_Object = MibTableColumn
gs2326ACLPortsConfState = _Gs2326ACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 9),
    _Gs2326ACLPortsConfState_Type()
)
gs2326ACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfState.setStatus("current")
_Gs2326ACLPortsConfCounter_Type = Counter32
_Gs2326ACLPortsConfCounter_Object = MibTableColumn
gs2326ACLPortsConfCounter = _Gs2326ACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 1, 1, 10),
    _Gs2326ACLPortsConfCounter_Type()
)
gs2326ACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLPortsConfCounter.setStatus("current")
_Gs2326ACLRateLimiterTable_Object = MibTable
gs2326ACLRateLimiterTable = _Gs2326ACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 2)
)
if mibBuilder.loadTexts:
    gs2326ACLRateLimiterTable.setStatus("current")
_Gs2326ACLRateLimiterEntry_Object = MibTableRow
gs2326ACLRateLimiterEntry = _Gs2326ACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 2, 1)
)
gs2326ACLRateLimiterEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    gs2326ACLRateLimiterEntry.setStatus("current")


class _Gs2326ACLRateLimiterID_Type(Integer32):
    """Custom type gs2326ACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2326ACLRateLimiterID_Type.__name__ = "Integer32"
_Gs2326ACLRateLimiterID_Object = MibTableColumn
gs2326ACLRateLimiterID = _Gs2326ACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 2, 1, 1),
    _Gs2326ACLRateLimiterID_Type()
)
gs2326ACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ACLRateLimiterID.setStatus("current")


class _Gs2326ACLRateLimiterUnit_Type(Integer32):
    """Custom type gs2326ACLRateLimiterUnit based on Integer32"""
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


_Gs2326ACLRateLimiterUnit_Type.__name__ = "Integer32"
_Gs2326ACLRateLimiterUnit_Object = MibTableColumn
gs2326ACLRateLimiterUnit = _Gs2326ACLRateLimiterUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 2, 1, 2),
    _Gs2326ACLRateLimiterUnit_Type()
)
gs2326ACLRateLimiterUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLRateLimiterUnit.setStatus("current")


class _Gs2326ACLRateLimiterRate_Type(Integer32):
    """Custom type gs2326ACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Gs2326ACLRateLimiterRate_Type.__name__ = "Integer32"
_Gs2326ACLRateLimiterRate_Object = MibTableColumn
gs2326ACLRateLimiterRate = _Gs2326ACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 2, 1, 3),
    _Gs2326ACLRateLimiterRate_Type()
)
gs2326ACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLRateLimiterRate.setStatus("current")
_Gs2326ACLACE_ObjectIdentity = ObjectIdentity
gs2326ACLACE = _Gs2326ACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3)
)


class _Gs2326ACLACECreate_Type(Integer32):
    """Custom type gs2326ACLACECreate based on Integer32"""
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


_Gs2326ACLACECreate_Type.__name__ = "Integer32"
_Gs2326ACLACECreate_Object = MibScalar
gs2326ACLACECreate = _Gs2326ACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 1),
    _Gs2326ACLACECreate_Type()
)
gs2326ACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACECreate.setStatus("current")
_Gs2326ACLACETable_Object = MibTable
gs2326ACLACETable = _Gs2326ACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326ACLACETable.setStatus("current")
_Gs2326ACLACEEntry_Object = MibTableRow
gs2326ACLACEEntry = _Gs2326ACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1)
)
gs2326ACLACEEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ACLACEIndex"),
)
if mibBuilder.loadTexts:
    gs2326ACLACEEntry.setStatus("current")


class _Gs2326ACLACEIndex_Type(Integer32):
    """Custom type gs2326ACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326ACLACEIndex_Type.__name__ = "Integer32"
_Gs2326ACLACEIndex_Object = MibTableColumn
gs2326ACLACEIndex = _Gs2326ACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 1),
    _Gs2326ACLACEIndex_Type()
)
gs2326ACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ACLACEIndex.setStatus("current")


class _Gs2326ACLACEID_Type(Integer32):
    """Custom type gs2326ACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326ACLACEID_Type.__name__ = "Integer32"
_Gs2326ACLACEID_Object = MibTableColumn
gs2326ACLACEID = _Gs2326ACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 2),
    _Gs2326ACLACEID_Type()
)
gs2326ACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEID.setStatus("current")


class _Gs2326ACLACENextID_Type(Integer32):
    """Custom type gs2326ACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2326ACLACENextID_Type.__name__ = "Integer32"
_Gs2326ACLACENextID_Object = MibTableColumn
gs2326ACLACENextID = _Gs2326ACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 3),
    _Gs2326ACLACENextID_Type()
)
gs2326ACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACENextID.setStatus("current")
_Gs2326ACLACEIngressPort_Type = DisplayString
_Gs2326ACLACEIngressPort_Object = MibTableColumn
gs2326ACLACEIngressPort = _Gs2326ACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 4),
    _Gs2326ACLACEIngressPort_Type()
)
gs2326ACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEIngressPort.setStatus("current")


class _Gs2326ACLACEPortPolicyNumber_Type(Integer32):
    """Custom type gs2326ACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2326ACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Gs2326ACLACEPortPolicyNumber_Object = MibTableColumn
gs2326ACLACEPortPolicyNumber = _Gs2326ACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 5),
    _Gs2326ACLACEPortPolicyNumber_Type()
)
gs2326ACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEPortPolicyNumber.setStatus("current")


class _Gs2326ACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type gs2326ACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2326ACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Gs2326ACLACEPortPolicyBitmask_Object = MibTableColumn
gs2326ACLACEPortPolicyBitmask = _Gs2326ACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 6),
    _Gs2326ACLACEPortPolicyBitmask_Type()
)
gs2326ACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEPortPolicyBitmask.setStatus("current")


class _Gs2326ACLACEFrameType_Type(Integer32):
    """Custom type gs2326ACLACEFrameType based on Integer32"""
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


_Gs2326ACLACEFrameType_Type.__name__ = "Integer32"
_Gs2326ACLACEFrameType_Object = MibTableColumn
gs2326ACLACEFrameType = _Gs2326ACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 7),
    _Gs2326ACLACEFrameType_Type()
)
gs2326ACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEFrameType.setStatus("current")


class _Gs2326ACLACEAction_Type(Integer32):
    """Custom type gs2326ACLACEAction based on Integer32"""
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


_Gs2326ACLACEAction_Type.__name__ = "Integer32"
_Gs2326ACLACEAction_Object = MibTableColumn
gs2326ACLACEAction = _Gs2326ACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 8),
    _Gs2326ACLACEAction_Type()
)
gs2326ACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEAction.setStatus("current")
_Gs2326ACLACEDenyPortRedirect_Type = DisplayString
_Gs2326ACLACEDenyPortRedirect_Object = MibTableColumn
gs2326ACLACEDenyPortRedirect = _Gs2326ACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 9),
    _Gs2326ACLACEDenyPortRedirect_Type()
)
gs2326ACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDenyPortRedirect.setStatus("current")


class _Gs2326ACLACELogging_Type(Integer32):
    """Custom type gs2326ACLACELogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLACELogging_Type.__name__ = "Integer32"
_Gs2326ACLACELogging_Object = MibTableColumn
gs2326ACLACELogging = _Gs2326ACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 10),
    _Gs2326ACLACELogging_Type()
)
gs2326ACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACELogging.setStatus("current")


class _Gs2326ACLACEMirror_Type(Integer32):
    """Custom type gs2326ACLACEMirror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLACEMirror_Type.__name__ = "Integer32"
_Gs2326ACLACEMirror_Object = MibTableColumn
gs2326ACLACEMirror = _Gs2326ACLACEMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 11),
    _Gs2326ACLACEMirror_Type()
)
gs2326ACLACEMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEMirror.setStatus("current")


class _Gs2326ACLACERateLimiter_Type(Integer32):
    """Custom type gs2326ACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2326ACLACERateLimiter_Type.__name__ = "Integer32"
_Gs2326ACLACERateLimiter_Object = MibTableColumn
gs2326ACLACERateLimiter = _Gs2326ACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 12),
    _Gs2326ACLACERateLimiter_Type()
)
gs2326ACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACERateLimiter.setStatus("current")


class _Gs2326ACLACEShutdown_Type(Integer32):
    """Custom type gs2326ACLACEShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ACLACEShutdown_Type.__name__ = "Integer32"
_Gs2326ACLACEShutdown_Object = MibTableColumn
gs2326ACLACEShutdown = _Gs2326ACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 13),
    _Gs2326ACLACEShutdown_Type()
)
gs2326ACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEShutdown.setStatus("current")


class _Gs2326ACLACEVLAN8021QTagged_Type(Integer32):
    """Custom type gs2326ACLACEVLAN8021QTagged based on Integer32"""
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


_Gs2326ACLACEVLAN8021QTagged_Type.__name__ = "Integer32"
_Gs2326ACLACEVLAN8021QTagged_Object = MibTableColumn
gs2326ACLACEVLAN8021QTagged = _Gs2326ACLACEVLAN8021QTagged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 14),
    _Gs2326ACLACEVLAN8021QTagged_Type()
)
gs2326ACLACEVLAN8021QTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEVLAN8021QTagged.setStatus("current")


class _Gs2326ACLACEVLANTagPriority_Type(Integer32):
    """Custom type gs2326ACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2326ACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Gs2326ACLACEVLANTagPriority_Object = MibTableColumn
gs2326ACLACEVLANTagPriority = _Gs2326ACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 15),
    _Gs2326ACLACEVLANTagPriority_Type()
)
gs2326ACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEVLANTagPriority.setStatus("current")


class _Gs2326ACLACEVLANVID_Type(Integer32):
    """Custom type gs2326ACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2326ACLACEVLANVID_Type.__name__ = "Integer32"
_Gs2326ACLACEVLANVID_Object = MibTableColumn
gs2326ACLACEVLANVID = _Gs2326ACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 16),
    _Gs2326ACLACEVLANVID_Type()
)
gs2326ACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEVLANVID.setStatus("current")


class _Gs2326ACLACEEtherType_Type(Integer32):
    """Custom type gs2326ACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2326ACLACEEtherType_Type.__name__ = "Integer32"
_Gs2326ACLACEEtherType_Object = MibTableColumn
gs2326ACLACEEtherType = _Gs2326ACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 17),
    _Gs2326ACLACEEtherType_Type()
)
gs2326ACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEEtherType.setStatus("current")
_Gs2326ACLACESMAC_Type = DisplayString
_Gs2326ACLACESMAC_Object = MibTableColumn
gs2326ACLACESMAC = _Gs2326ACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 18),
    _Gs2326ACLACESMAC_Type()
)
gs2326ACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACESMAC.setStatus("current")


class _Gs2326ACLACEDMACType_Type(Integer32):
    """Custom type gs2326ACLACEDMACType based on Integer32"""
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


_Gs2326ACLACEDMACType_Type.__name__ = "Integer32"
_Gs2326ACLACEDMACType_Object = MibTableColumn
gs2326ACLACEDMACType = _Gs2326ACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 19),
    _Gs2326ACLACEDMACType_Type()
)
gs2326ACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDMACType.setStatus("current")
_Gs2326ACLACEDMAC_Type = DisplayString
_Gs2326ACLACEDMAC_Object = MibTableColumn
gs2326ACLACEDMAC = _Gs2326ACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 20),
    _Gs2326ACLACEDMAC_Type()
)
gs2326ACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDMAC.setStatus("current")


class _Gs2326ACLACEArpOpcode_Type(Integer32):
    """Custom type gs2326ACLACEArpOpcode based on Integer32"""
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


_Gs2326ACLACEArpOpcode_Type.__name__ = "Integer32"
_Gs2326ACLACEArpOpcode_Object = MibTableColumn
gs2326ACLACEArpOpcode = _Gs2326ACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 21),
    _Gs2326ACLACEArpOpcode_Type()
)
gs2326ACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpOpcode.setStatus("current")


class _Gs2326ACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type gs2326ACLACEArpFlagsRequestReply based on Integer32"""
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


_Gs2326ACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Gs2326ACLACEArpFlagsRequestReply_Object = MibTableColumn
gs2326ACLACEArpFlagsRequestReply = _Gs2326ACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 22),
    _Gs2326ACLACEArpFlagsRequestReply_Type()
)
gs2326ACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpFlagsRequestReply.setStatus("current")


class _Gs2326ACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type gs2326ACLACEArpFlagsArpSmac based on Integer32"""
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


_Gs2326ACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Gs2326ACLACEArpFlagsArpSmac_Object = MibTableColumn
gs2326ACLACEArpFlagsArpSmac = _Gs2326ACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 23),
    _Gs2326ACLACEArpFlagsArpSmac_Type()
)
gs2326ACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpFlagsArpSmac.setStatus("current")


class _Gs2326ACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type gs2326ACLACEArpFlagsRarpDmac based on Integer32"""
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


_Gs2326ACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Gs2326ACLACEArpFlagsRarpDmac_Object = MibTableColumn
gs2326ACLACEArpFlagsRarpDmac = _Gs2326ACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 24),
    _Gs2326ACLACEArpFlagsRarpDmac_Type()
)
gs2326ACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpFlagsRarpDmac.setStatus("current")


class _Gs2326ACLACEArpFlagsLength_Type(Integer32):
    """Custom type gs2326ACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326ACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Gs2326ACLACEArpFlagsLength_Object = MibTableColumn
gs2326ACLACEArpFlagsLength = _Gs2326ACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 25),
    _Gs2326ACLACEArpFlagsLength_Type()
)
gs2326ACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpFlagsLength.setStatus("current")


class _Gs2326ACLACEArpFlagsIp_Type(Integer32):
    """Custom type gs2326ACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326ACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Gs2326ACLACEArpFlagsIp_Object = MibTableColumn
gs2326ACLACEArpFlagsIp = _Gs2326ACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 26),
    _Gs2326ACLACEArpFlagsIp_Type()
)
gs2326ACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpFlagsIp.setStatus("current")


class _Gs2326ACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type gs2326ACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326ACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Gs2326ACLACEArpFlagsEthernet_Object = MibTableColumn
gs2326ACLACEArpFlagsEthernet = _Gs2326ACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 27),
    _Gs2326ACLACEArpFlagsEthernet_Type()
)
gs2326ACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEArpFlagsEthernet.setStatus("current")


class _Gs2326ACLACESIPType_Type(Integer32):
    """Custom type gs2326ACLACESIPType based on Integer32"""
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


_Gs2326ACLACESIPType_Type.__name__ = "Integer32"
_Gs2326ACLACESIPType_Object = MibTableColumn
gs2326ACLACESIPType = _Gs2326ACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 28),
    _Gs2326ACLACESIPType_Type()
)
gs2326ACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACESIPType.setStatus("current")
_Gs2326ACLACESIPIPAddress_Type = IpAddress
_Gs2326ACLACESIPIPAddress_Object = MibTableColumn
gs2326ACLACESIPIPAddress = _Gs2326ACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 29),
    _Gs2326ACLACESIPIPAddress_Type()
)
gs2326ACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACESIPIPAddress.setStatus("current")


class _Gs2326ACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type gs2326ACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2326ACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2326ACLACESIPNetworkPrefix_Object = MibTableColumn
gs2326ACLACESIPNetworkPrefix = _Gs2326ACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 30),
    _Gs2326ACLACESIPNetworkPrefix_Type()
)
gs2326ACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACESIPNetworkPrefix.setStatus("current")


class _Gs2326ACLACEDIPType_Type(Integer32):
    """Custom type gs2326ACLACEDIPType based on Integer32"""
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


_Gs2326ACLACEDIPType_Type.__name__ = "Integer32"
_Gs2326ACLACEDIPType_Object = MibTableColumn
gs2326ACLACEDIPType = _Gs2326ACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 32),
    _Gs2326ACLACEDIPType_Type()
)
gs2326ACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDIPType.setStatus("current")
_Gs2326ACLACEDIPIPAddress_Type = IpAddress
_Gs2326ACLACEDIPIPAddress_Object = MibTableColumn
gs2326ACLACEDIPIPAddress = _Gs2326ACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 33),
    _Gs2326ACLACEDIPIPAddress_Type()
)
gs2326ACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDIPIPAddress.setStatus("current")


class _Gs2326ACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type gs2326ACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2326ACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2326ACLACEDIPNetworkPrefix_Object = MibTableColumn
gs2326ACLACEDIPNetworkPrefix = _Gs2326ACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 34),
    _Gs2326ACLACEDIPNetworkPrefix_Type()
)
gs2326ACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDIPNetworkPrefix.setStatus("current")


class _Gs2326ACLACEIPProtocol_Type(Integer32):
    """Custom type gs2326ACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2326ACLACEIPProtocol_Type.__name__ = "Integer32"
_Gs2326ACLACEIPProtocol_Object = MibTableColumn
gs2326ACLACEIPProtocol = _Gs2326ACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 36),
    _Gs2326ACLACEIPProtocol_Type()
)
gs2326ACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEIPProtocol.setStatus("current")


class _Gs2326ACLACEIPFlagsTTL_Type(Integer32):
    """Custom type gs2326ACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326ACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Gs2326ACLACEIPFlagsTTL_Object = MibTableColumn
gs2326ACLACEIPFlagsTTL = _Gs2326ACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 37),
    _Gs2326ACLACEIPFlagsTTL_Type()
)
gs2326ACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEIPFlagsTTL.setStatus("current")


class _Gs2326ACLACEIPFlagsOptions_Type(Integer32):
    """Custom type gs2326ACLACEIPFlagsOptions based on Integer32"""
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


_Gs2326ACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Gs2326ACLACEIPFlagsOptions_Object = MibTableColumn
gs2326ACLACEIPFlagsOptions = _Gs2326ACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 38),
    _Gs2326ACLACEIPFlagsOptions_Type()
)
gs2326ACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEIPFlagsOptions.setStatus("current")


class _Gs2326ACLACEIPFlagsFragment_Type(Integer32):
    """Custom type gs2326ACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326ACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Gs2326ACLACEIPFlagsFragment_Object = MibTableColumn
gs2326ACLACEIPFlagsFragment = _Gs2326ACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 39),
    _Gs2326ACLACEIPFlagsFragment_Type()
)
gs2326ACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEIPFlagsFragment.setStatus("current")


class _Gs2326ACLACEICMPType_Type(Integer32):
    """Custom type gs2326ACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2326ACLACEICMPType_Type.__name__ = "Integer32"
_Gs2326ACLACEICMPType_Object = MibTableColumn
gs2326ACLACEICMPType = _Gs2326ACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 40),
    _Gs2326ACLACEICMPType_Type()
)
gs2326ACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEICMPType.setStatus("current")


class _Gs2326ACLACEICMPCode_Type(Integer32):
    """Custom type gs2326ACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2326ACLACEICMPCode_Type.__name__ = "Integer32"
_Gs2326ACLACEICMPCode_Object = MibTableColumn
gs2326ACLACEICMPCode = _Gs2326ACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 41),
    _Gs2326ACLACEICMPCode_Type()
)
gs2326ACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEICMPCode.setStatus("current")


class _Gs2326ACLACESourcePortMin_Type(Integer32):
    """Custom type gs2326ACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2326ACLACESourcePortMin_Type.__name__ = "Integer32"
_Gs2326ACLACESourcePortMin_Object = MibTableColumn
gs2326ACLACESourcePortMin = _Gs2326ACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 42),
    _Gs2326ACLACESourcePortMin_Type()
)
gs2326ACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACESourcePortMin.setStatus("current")


class _Gs2326ACLACESourcePortMax_Type(Integer32):
    """Custom type gs2326ACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2326ACLACESourcePortMax_Type.__name__ = "Integer32"
_Gs2326ACLACESourcePortMax_Object = MibTableColumn
gs2326ACLACESourcePortMax = _Gs2326ACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 43),
    _Gs2326ACLACESourcePortMax_Type()
)
gs2326ACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACESourcePortMax.setStatus("current")


class _Gs2326ACLACEDestPortMin_Type(Integer32):
    """Custom type gs2326ACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2326ACLACEDestPortMin_Type.__name__ = "Integer32"
_Gs2326ACLACEDestPortMin_Object = MibTableColumn
gs2326ACLACEDestPortMin = _Gs2326ACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 44),
    _Gs2326ACLACEDestPortMin_Type()
)
gs2326ACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDestPortMin.setStatus("current")


class _Gs2326ACLACEDestPortMax_Type(Integer32):
    """Custom type gs2326ACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2326ACLACEDestPortMax_Type.__name__ = "Integer32"
_Gs2326ACLACEDestPortMax_Object = MibTableColumn
gs2326ACLACEDestPortMax = _Gs2326ACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 45),
    _Gs2326ACLACEDestPortMax_Type()
)
gs2326ACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEDestPortMax.setStatus("current")


class _Gs2326ACLACETCPFlagsFin_Type(Integer32):
    """Custom type gs2326ACLACETCPFlagsFin based on Integer32"""
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


_Gs2326ACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Gs2326ACLACETCPFlagsFin_Object = MibTableColumn
gs2326ACLACETCPFlagsFin = _Gs2326ACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 46),
    _Gs2326ACLACETCPFlagsFin_Type()
)
gs2326ACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACETCPFlagsFin.setStatus("current")


class _Gs2326ACLACETCPFlagsSyn_Type(Integer32):
    """Custom type gs2326ACLACETCPFlagsSyn based on Integer32"""
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


_Gs2326ACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Gs2326ACLACETCPFlagsSyn_Object = MibTableColumn
gs2326ACLACETCPFlagsSyn = _Gs2326ACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 47),
    _Gs2326ACLACETCPFlagsSyn_Type()
)
gs2326ACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACETCPFlagsSyn.setStatus("current")


class _Gs2326ACLACETCPFlagsRst_Type(Integer32):
    """Custom type gs2326ACLACETCPFlagsRst based on Integer32"""
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


_Gs2326ACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Gs2326ACLACETCPFlagsRst_Object = MibTableColumn
gs2326ACLACETCPFlagsRst = _Gs2326ACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 48),
    _Gs2326ACLACETCPFlagsRst_Type()
)
gs2326ACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACETCPFlagsRst.setStatus("current")


class _Gs2326ACLACETCPFlagsPsh_Type(Integer32):
    """Custom type gs2326ACLACETCPFlagsPsh based on Integer32"""
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


_Gs2326ACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Gs2326ACLACETCPFlagsPsh_Object = MibTableColumn
gs2326ACLACETCPFlagsPsh = _Gs2326ACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 49),
    _Gs2326ACLACETCPFlagsPsh_Type()
)
gs2326ACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACETCPFlagsPsh.setStatus("current")


class _Gs2326ACLACETCPFlagsAck_Type(Integer32):
    """Custom type gs2326ACLACETCPFlagsAck based on Integer32"""
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


_Gs2326ACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Gs2326ACLACETCPFlagsAck_Object = MibTableColumn
gs2326ACLACETCPFlagsAck = _Gs2326ACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 50),
    _Gs2326ACLACETCPFlagsAck_Type()
)
gs2326ACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACETCPFlagsAck.setStatus("current")


class _Gs2326ACLACETCPFlagsUrg_Type(Integer32):
    """Custom type gs2326ACLACETCPFlagsUrg based on Integer32"""
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


_Gs2326ACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Gs2326ACLACETCPFlagsUrg_Object = MibTableColumn
gs2326ACLACETCPFlagsUrg = _Gs2326ACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 51),
    _Gs2326ACLACETCPFlagsUrg_Type()
)
gs2326ACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACETCPFlagsUrg.setStatus("current")


class _Gs2326ACLACERowStatus_Type(Integer32):
    """Custom type gs2326ACLACERowStatus based on Integer32"""
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


_Gs2326ACLACERowStatus_Type.__name__ = "Integer32"
_Gs2326ACLACERowStatus_Object = MibTableColumn
gs2326ACLACERowStatus = _Gs2326ACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 2, 1, 66),
    _Gs2326ACLACERowStatus_Type()
)
gs2326ACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACERowStatus.setStatus("current")


class _Gs2326ACLACEClear_Type(Integer32):
    """Custom type gs2326ACLACEClear based on Integer32"""
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


_Gs2326ACLACEClear_Type.__name__ = "Integer32"
_Gs2326ACLACEClear_Object = MibScalar
gs2326ACLACEClear = _Gs2326ACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 3),
    _Gs2326ACLACEClear_Type()
)
gs2326ACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEClear.setStatus("current")


class _Gs2326ACLACEMoveACEID_Type(Integer32):
    """Custom type gs2326ACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2326ACLACEMoveACEID_Type.__name__ = "Integer32"
_Gs2326ACLACEMoveACEID_Object = MibScalar
gs2326ACLACEMoveACEID = _Gs2326ACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 4),
    _Gs2326ACLACEMoveACEID_Type()
)
gs2326ACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEMoveACEID.setStatus("current")


class _Gs2326ACLACEMoveNextACEID_Type(Integer32):
    """Custom type gs2326ACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2326ACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Gs2326ACLACEMoveNextACEID_Object = MibScalar
gs2326ACLACEMoveNextACEID = _Gs2326ACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 5),
    _Gs2326ACLACEMoveNextACEID_Type()
)
gs2326ACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ACLACEMoveNextACEID.setStatus("current")
_Gs2326ACLACEStatusTable_Object = MibTable
gs2326ACLACEStatusTable = _Gs2326ACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    gs2326ACLACEStatusTable.setStatus("current")
_Gs2326ACLACEStatusEntry_Object = MibTableRow
gs2326ACLACEStatusEntry = _Gs2326ACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1)
)
gs2326ACLACEStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2326ACLACEStatusEntry.setStatus("current")


class _Gs2326ACLACEStatusIndex_Type(Integer32):
    """Custom type gs2326ACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326ACLACEStatusIndex_Type.__name__ = "Integer32"
_Gs2326ACLACEStatusIndex_Object = MibTableColumn
gs2326ACLACEStatusIndex = _Gs2326ACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 1),
    _Gs2326ACLACEStatusIndex_Type()
)
gs2326ACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusIndex.setStatus("current")
_Gs2326ACLACEStatusUser_Type = DisplayString
_Gs2326ACLACEStatusUser_Object = MibTableColumn
gs2326ACLACEStatusUser = _Gs2326ACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 2),
    _Gs2326ACLACEStatusUser_Type()
)
gs2326ACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusUser.setStatus("current")


class _Gs2326ACLACEStatusID_Type(Integer32):
    """Custom type gs2326ACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326ACLACEStatusID_Type.__name__ = "Integer32"
_Gs2326ACLACEStatusID_Object = MibTableColumn
gs2326ACLACEStatusID = _Gs2326ACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 3),
    _Gs2326ACLACEStatusID_Type()
)
gs2326ACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusID.setStatus("current")
_Gs2326ACLACEStatusIngressPort_Type = DisplayString
_Gs2326ACLACEStatusIngressPort_Object = MibTableColumn
gs2326ACLACEStatusIngressPort = _Gs2326ACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 4),
    _Gs2326ACLACEStatusIngressPort_Type()
)
gs2326ACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusIngressPort.setStatus("current")
_Gs2326ACLACEStatusFrameType_Type = DisplayString
_Gs2326ACLACEStatusFrameType_Object = MibTableColumn
gs2326ACLACEStatusFrameType = _Gs2326ACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 5),
    _Gs2326ACLACEStatusFrameType_Type()
)
gs2326ACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusFrameType.setStatus("current")
_Gs2326ACLACEStatusAction_Type = DisplayString
_Gs2326ACLACEStatusAction_Object = MibTableColumn
gs2326ACLACEStatusAction = _Gs2326ACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 6),
    _Gs2326ACLACEStatusAction_Type()
)
gs2326ACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusAction.setStatus("current")
_Gs2326ACLACEStatusRateLimiter_Type = DisplayString
_Gs2326ACLACEStatusRateLimiter_Object = MibTableColumn
gs2326ACLACEStatusRateLimiter = _Gs2326ACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 7),
    _Gs2326ACLACEStatusRateLimiter_Type()
)
gs2326ACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusRateLimiter.setStatus("current")
_Gs2326ACLACEStatusPortCopy_Type = DisplayString
_Gs2326ACLACEStatusPortCopy_Object = MibTableColumn
gs2326ACLACEStatusPortCopy = _Gs2326ACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 8),
    _Gs2326ACLACEStatusPortCopy_Type()
)
gs2326ACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusPortCopy.setStatus("current")
_Gs2326ACLACEStatusMirror_Type = DisplayString
_Gs2326ACLACEStatusMirror_Object = MibTableColumn
gs2326ACLACEStatusMirror = _Gs2326ACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 9),
    _Gs2326ACLACEStatusMirror_Type()
)
gs2326ACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusMirror.setStatus("current")
_Gs2326ACLACEStatusCPU_Type = DisplayString
_Gs2326ACLACEStatusCPU_Object = MibTableColumn
gs2326ACLACEStatusCPU = _Gs2326ACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 10),
    _Gs2326ACLACEStatusCPU_Type()
)
gs2326ACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusCPU.setStatus("current")
_Gs2326ACLACEStatusCounter_Type = Counter32
_Gs2326ACLACEStatusCounter_Object = MibTableColumn
gs2326ACLACEStatusCounter = _Gs2326ACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 11),
    _Gs2326ACLACEStatusCounter_Type()
)
gs2326ACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusCounter.setStatus("current")
_Gs2326ACLACEStatusConflict_Type = DisplayString
_Gs2326ACLACEStatusConflict_Object = MibTableColumn
gs2326ACLACEStatusConflict = _Gs2326ACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 9, 3, 6, 1, 12),
    _Gs2326ACLACEStatusConflict_Type()
)
gs2326ACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ACLACEStatusConflict.setStatus("current")
_Gs2326LoopProtection_ObjectIdentity = ObjectIdentity
gs2326LoopProtection = _Gs2326LoopProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12)
)
_Gs2326LoopProtectionConfig_ObjectIdentity = ObjectIdentity
gs2326LoopProtectionConfig = _Gs2326LoopProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1)
)


class _Gs2326LoopProtectionGlobalEnable_Type(Integer32):
    """Custom type gs2326LoopProtectionGlobalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326LoopProtectionGlobalEnable_Type.__name__ = "Integer32"
_Gs2326LoopProtectionGlobalEnable_Object = MibScalar
gs2326LoopProtectionGlobalEnable = _Gs2326LoopProtectionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 1),
    _Gs2326LoopProtectionGlobalEnable_Type()
)
gs2326LoopProtectionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectionGlobalEnable.setStatus("current")


class _Gs2326LoopProtectionTranmisstionTime_Type(Integer32):
    """Custom type gs2326LoopProtectionTranmisstionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2326LoopProtectionTranmisstionTime_Type.__name__ = "Integer32"
_Gs2326LoopProtectionTranmisstionTime_Object = MibScalar
gs2326LoopProtectionTranmisstionTime = _Gs2326LoopProtectionTranmisstionTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 2),
    _Gs2326LoopProtectionTranmisstionTime_Type()
)
gs2326LoopProtectionTranmisstionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectionTranmisstionTime.setStatus("current")


class _Gs2326LoopProtectionShutdownTime_Type(Integer32):
    """Custom type gs2326LoopProtectionShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Gs2326LoopProtectionShutdownTime_Type.__name__ = "Integer32"
_Gs2326LoopProtectionShutdownTime_Object = MibScalar
gs2326LoopProtectionShutdownTime = _Gs2326LoopProtectionShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 3),
    _Gs2326LoopProtectionShutdownTime_Type()
)
gs2326LoopProtectionShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectionShutdownTime.setStatus("current")
_Gs2326LoopProtectionConfigurationTable_Object = MibTable
gs2326LoopProtectionConfigurationTable = _Gs2326LoopProtectionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    gs2326LoopProtectionConfigurationTable.setStatus("current")
_Gs2326LoopProtectionConfigurationEntry_Object = MibTableRow
gs2326LoopProtectionConfigurationEntry = _Gs2326LoopProtectionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 4, 1)
)
gs2326LoopProtectionConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326LoopProtectionConfPort"),
)
if mibBuilder.loadTexts:
    gs2326LoopProtectionConfigurationEntry.setStatus("current")


class _Gs2326LoopProtectionConfPort_Type(Integer32):
    """Custom type gs2326LoopProtectionConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326LoopProtectionConfPort_Type.__name__ = "Integer32"
_Gs2326LoopProtectionConfPort_Object = MibTableColumn
gs2326LoopProtectionConfPort = _Gs2326LoopProtectionConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 4, 1, 1),
    _Gs2326LoopProtectionConfPort_Type()
)
gs2326LoopProtectionConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326LoopProtectionConfPort.setStatus("current")


class _Gs2326LoopProtectionConfEnable_Type(Integer32):
    """Custom type gs2326LoopProtectionConfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326LoopProtectionConfEnable_Type.__name__ = "Integer32"
_Gs2326LoopProtectionConfEnable_Object = MibTableColumn
gs2326LoopProtectionConfEnable = _Gs2326LoopProtectionConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 4, 1, 2),
    _Gs2326LoopProtectionConfEnable_Type()
)
gs2326LoopProtectionConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectionConfEnable.setStatus("current")


class _Gs2326LoopProtectionConfAction_Type(Integer32):
    """Custom type gs2326LoopProtectionConfAction based on Integer32"""
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


_Gs2326LoopProtectionConfAction_Type.__name__ = "Integer32"
_Gs2326LoopProtectionConfAction_Object = MibTableColumn
gs2326LoopProtectionConfAction = _Gs2326LoopProtectionConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 4, 1, 3),
    _Gs2326LoopProtectionConfAction_Type()
)
gs2326LoopProtectionConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectionConfAction.setStatus("current")


class _Gs2326LoopProtectionConfTxmode_Type(Integer32):
    """Custom type gs2326LoopProtectionConfTxmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326LoopProtectionConfTxmode_Type.__name__ = "Integer32"
_Gs2326LoopProtectionConfTxmode_Object = MibTableColumn
gs2326LoopProtectionConfTxmode = _Gs2326LoopProtectionConfTxmode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 1, 4, 1, 4),
    _Gs2326LoopProtectionConfTxmode_Type()
)
gs2326LoopProtectionConfTxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoopProtectionConfTxmode.setStatus("current")
_Gs2326LoopProtectionStatusTable_Object = MibTable
gs2326LoopProtectionStatusTable = _Gs2326LoopProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2)
)
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusTable.setStatus("current")
_Gs2326LoopProtectionStatusEntry_Object = MibTableRow
gs2326LoopProtectionStatusEntry = _Gs2326LoopProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1)
)
gs2326LoopProtectionStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326LoopProtectionStatusPort"),
)
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusEntry.setStatus("current")


class _Gs2326LoopProtectionStatusPort_Type(Integer32):
    """Custom type gs2326LoopProtectionStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326LoopProtectionStatusPort_Type.__name__ = "Integer32"
_Gs2326LoopProtectionStatusPort_Object = MibTableColumn
gs2326LoopProtectionStatusPort = _Gs2326LoopProtectionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 1),
    _Gs2326LoopProtectionStatusPort_Type()
)
gs2326LoopProtectionStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusPort.setStatus("current")
_Gs2326LoopProtectionStatusAction_Type = DisplayString
_Gs2326LoopProtectionStatusAction_Object = MibTableColumn
gs2326LoopProtectionStatusAction = _Gs2326LoopProtectionStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 2),
    _Gs2326LoopProtectionStatusAction_Type()
)
gs2326LoopProtectionStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusAction.setStatus("current")
_Gs2326LoopProtectionStatusTransmit_Type = DisplayString
_Gs2326LoopProtectionStatusTransmit_Object = MibTableColumn
gs2326LoopProtectionStatusTransmit = _Gs2326LoopProtectionStatusTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 3),
    _Gs2326LoopProtectionStatusTransmit_Type()
)
gs2326LoopProtectionStatusTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusTransmit.setStatus("current")


class _Gs2326LoopProtectionStatusLoops_Type(Integer32):
    """Custom type gs2326LoopProtectionStatusLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2326LoopProtectionStatusLoops_Type.__name__ = "Integer32"
_Gs2326LoopProtectionStatusLoops_Object = MibTableColumn
gs2326LoopProtectionStatusLoops = _Gs2326LoopProtectionStatusLoops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 4),
    _Gs2326LoopProtectionStatusLoops_Type()
)
gs2326LoopProtectionStatusLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusLoops.setStatus("current")
_Gs2326LoopProtectionStatusStatus_Type = DisplayString
_Gs2326LoopProtectionStatusStatus_Object = MibTableColumn
gs2326LoopProtectionStatusStatus = _Gs2326LoopProtectionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 5),
    _Gs2326LoopProtectionStatusStatus_Type()
)
gs2326LoopProtectionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusStatus.setStatus("current")
_Gs2326LoopProtectionStatusLoop_Type = DisplayString
_Gs2326LoopProtectionStatusLoop_Object = MibTableColumn
gs2326LoopProtectionStatusLoop = _Gs2326LoopProtectionStatusLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 6),
    _Gs2326LoopProtectionStatusLoop_Type()
)
gs2326LoopProtectionStatusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusLoop.setStatus("current")
_Gs2326LoopProtectionStatusTimeLastLoop_Type = DisplayString
_Gs2326LoopProtectionStatusTimeLastLoop_Object = MibTableColumn
gs2326LoopProtectionStatusTimeLastLoop = _Gs2326LoopProtectionStatusTimeLastLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 12, 2, 1, 7),
    _Gs2326LoopProtectionStatusTimeLastLoop_Type()
)
gs2326LoopProtectionStatusTimeLastLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LoopProtectionStatusTimeLastLoop.setStatus("current")
_Gs2326Qos_ObjectIdentity = ObjectIdentity
gs2326Qos = _Gs2326Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14)
)
_Gs2326QosPortClassification_ObjectIdentity = ObjectIdentity
gs2326QosPortClassification = _Gs2326QosPortClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1)
)
_Gs2326QosPortClassificationTable_Object = MibTable
gs2326QosPortClassificationTable = _Gs2326QosPortClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    gs2326QosPortClassificationTable.setStatus("current")
_Gs2326QosPortClassificationEntry_Object = MibTableRow
gs2326QosPortClassificationEntry = _Gs2326QosPortClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1)
)
gs2326QosPortClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosPortClassificationPort"),
)
if mibBuilder.loadTexts:
    gs2326QosPortClassificationEntry.setStatus("current")


class _Gs2326QosPortClassificationPort_Type(Integer32):
    """Custom type gs2326QosPortClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosPortClassificationPort_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationPort_Object = MibTableColumn
gs2326QosPortClassificationPort = _Gs2326QosPortClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 1),
    _Gs2326QosPortClassificationPort_Type()
)
gs2326QosPortClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationPort.setStatus("current")


class _Gs2326QosPortClassificationQoSclass_Type(Integer32):
    """Custom type gs2326QosPortClassificationQoSclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326QosPortClassificationQoSclass_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationQoSclass_Object = MibTableColumn
gs2326QosPortClassificationQoSclass = _Gs2326QosPortClassificationQoSclass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 2),
    _Gs2326QosPortClassificationQoSclass_Type()
)
gs2326QosPortClassificationQoSclass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationQoSclass.setStatus("current")


class _Gs2326QosPortClassificationDPlevel_Type(Integer32):
    """Custom type gs2326QosPortClassificationDPlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2326QosPortClassificationDPlevel_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationDPlevel_Object = MibTableColumn
gs2326QosPortClassificationDPlevel = _Gs2326QosPortClassificationDPlevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 3),
    _Gs2326QosPortClassificationDPlevel_Type()
)
gs2326QosPortClassificationDPlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationDPlevel.setStatus("current")


class _Gs2326QosPortClassificationPCP_Type(Integer32):
    """Custom type gs2326QosPortClassificationPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326QosPortClassificationPCP_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationPCP_Object = MibTableColumn
gs2326QosPortClassificationPCP = _Gs2326QosPortClassificationPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 4),
    _Gs2326QosPortClassificationPCP_Type()
)
gs2326QosPortClassificationPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationPCP.setStatus("current")


class _Gs2326QosPortClassificationDEI_Type(Integer32):
    """Custom type gs2326QosPortClassificationDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosPortClassificationDEI_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationDEI_Object = MibTableColumn
gs2326QosPortClassificationDEI = _Gs2326QosPortClassificationDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 5),
    _Gs2326QosPortClassificationDEI_Type()
)
gs2326QosPortClassificationDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationDEI.setStatus("current")


class _Gs2326QosPortClassificationTagClass_Type(Integer32):
    """Custom type gs2326QosPortClassificationTagClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosPortClassificationTagClass_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationTagClass_Object = MibTableColumn
gs2326QosPortClassificationTagClass = _Gs2326QosPortClassificationTagClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 6),
    _Gs2326QosPortClassificationTagClass_Type()
)
gs2326QosPortClassificationTagClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationTagClass.setStatus("current")


class _Gs2326QosPortClassificationDSCPBased_Type(Integer32):
    """Custom type gs2326QosPortClassificationDSCPBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosPortClassificationDSCPBased_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationDSCPBased_Object = MibTableColumn
gs2326QosPortClassificationDSCPBased = _Gs2326QosPortClassificationDSCPBased_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 7),
    _Gs2326QosPortClassificationDSCPBased_Type()
)
gs2326QosPortClassificationDSCPBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationDSCPBased.setStatus("current")


class _Gs2326QosPortClassificationAddressMode_Type(Integer32):
    """Custom type gs2326QosPortClassificationAddressMode based on Integer32"""
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


_Gs2326QosPortClassificationAddressMode_Type.__name__ = "Integer32"
_Gs2326QosPortClassificationAddressMode_Object = MibTableColumn
gs2326QosPortClassificationAddressMode = _Gs2326QosPortClassificationAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 1, 1, 8),
    _Gs2326QosPortClassificationAddressMode_Type()
)
gs2326QosPortClassificationAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortClassificationAddressMode.setStatus("current")
_Gs2326QoSIngressPortTagClassificationTable_Object = MibTable
gs2326QoSIngressPortTagClassificationTable = _Gs2326QoSIngressPortTagClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagClassificationTable.setStatus("current")
_Gs2326QoSIngressPortTagClassificationEntry_Object = MibTableRow
gs2326QoSIngressPortTagClassificationEntry = _Gs2326QoSIngressPortTagClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2, 1)
)
gs2326QoSIngressPortTagClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QoSIngressPortTagClassificationPort"),
    (0, "LANCOM-GS-2326-MIB", "gs2326QoSIngressPortTagPCP"),
    (0, "LANCOM-GS-2326-MIB", "gs2326QoSIngressPortTagDEI"),
)
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagClassificationEntry.setStatus("current")


class _Gs2326QoSIngressPortTagClassificationPort_Type(Integer32):
    """Custom type gs2326QoSIngressPortTagClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QoSIngressPortTagClassificationPort_Type.__name__ = "Integer32"
_Gs2326QoSIngressPortTagClassificationPort_Object = MibTableColumn
gs2326QoSIngressPortTagClassificationPort = _Gs2326QoSIngressPortTagClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2, 1, 1),
    _Gs2326QoSIngressPortTagClassificationPort_Type()
)
gs2326QoSIngressPortTagClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagClassificationPort.setStatus("current")


class _Gs2326QoSIngressPortTagPCP_Type(Integer32):
    """Custom type gs2326QoSIngressPortTagPCP based on Integer32"""
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


_Gs2326QoSIngressPortTagPCP_Type.__name__ = "Integer32"
_Gs2326QoSIngressPortTagPCP_Object = MibTableColumn
gs2326QoSIngressPortTagPCP = _Gs2326QoSIngressPortTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2, 1, 2),
    _Gs2326QoSIngressPortTagPCP_Type()
)
gs2326QoSIngressPortTagPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagPCP.setStatus("current")


class _Gs2326QoSIngressPortTagDEI_Type(Integer32):
    """Custom type gs2326QoSIngressPortTagDEI based on Integer32"""
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


_Gs2326QoSIngressPortTagDEI_Type.__name__ = "Integer32"
_Gs2326QoSIngressPortTagDEI_Object = MibTableColumn
gs2326QoSIngressPortTagDEI = _Gs2326QoSIngressPortTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2, 1, 3),
    _Gs2326QoSIngressPortTagDEI_Type()
)
gs2326QoSIngressPortTagDEI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagDEI.setStatus("current")


class _Gs2326QoSIngressPortTagQosClass_Type(Integer32):
    """Custom type gs2326QoSIngressPortTagQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326QoSIngressPortTagQosClass_Type.__name__ = "Integer32"
_Gs2326QoSIngressPortTagQosClass_Object = MibTableColumn
gs2326QoSIngressPortTagQosClass = _Gs2326QoSIngressPortTagQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2, 1, 4),
    _Gs2326QoSIngressPortTagQosClass_Type()
)
gs2326QoSIngressPortTagQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagQosClass.setStatus("current")


class _Gs2326QoSIngressPortTagDPLevel_Type(Integer32):
    """Custom type gs2326QoSIngressPortTagDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2326QoSIngressPortTagDPLevel_Type.__name__ = "Integer32"
_Gs2326QoSIngressPortTagDPLevel_Object = MibTableColumn
gs2326QoSIngressPortTagDPLevel = _Gs2326QoSIngressPortTagDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 1, 2, 1, 5),
    _Gs2326QoSIngressPortTagDPLevel_Type()
)
gs2326QoSIngressPortTagDPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSIngressPortTagDPLevel.setStatus("current")
_Gs2326QosPortPolicingTable_Object = MibTable
gs2326QosPortPolicingTable = _Gs2326QosPortPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gs2326QosPortPolicingTable.setStatus("current")
_Gs2326QosPortPolicingEntry_Object = MibTableRow
gs2326QosPortPolicingEntry = _Gs2326QosPortPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2, 1)
)
gs2326QosPortPolicingEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosPortPolicingPort"),
)
if mibBuilder.loadTexts:
    gs2326QosPortPolicingEntry.setStatus("current")


class _Gs2326QosPortPolicingPort_Type(Integer32):
    """Custom type gs2326QosPortPolicingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosPortPolicingPort_Type.__name__ = "Integer32"
_Gs2326QosPortPolicingPort_Object = MibTableColumn
gs2326QosPortPolicingPort = _Gs2326QosPortPolicingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2, 1, 1),
    _Gs2326QosPortPolicingPort_Type()
)
gs2326QosPortPolicingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosPortPolicingPort.setStatus("current")


class _Gs2326QosPortPolicingMode_Type(Integer32):
    """Custom type gs2326QosPortPolicingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosPortPolicingMode_Type.__name__ = "Integer32"
_Gs2326QosPortPolicingMode_Object = MibTableColumn
gs2326QosPortPolicingMode = _Gs2326QosPortPolicingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2, 1, 2),
    _Gs2326QosPortPolicingMode_Type()
)
gs2326QosPortPolicingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortPolicingMode.setStatus("current")


class _Gs2326QosPortPolicingRate_Type(Integer32):
    """Custom type gs2326QosPortPolicingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2326QosPortPolicingRate_Type.__name__ = "Integer32"
_Gs2326QosPortPolicingRate_Object = MibTableColumn
gs2326QosPortPolicingRate = _Gs2326QosPortPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2, 1, 3),
    _Gs2326QosPortPolicingRate_Type()
)
gs2326QosPortPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortPolicingRate.setStatus("current")


class _Gs2326QosPortPolicingUnit_Type(Integer32):
    """Custom type gs2326QosPortPolicingUnit based on Integer32"""
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


_Gs2326QosPortPolicingUnit_Type.__name__ = "Integer32"
_Gs2326QosPortPolicingUnit_Object = MibTableColumn
gs2326QosPortPolicingUnit = _Gs2326QosPortPolicingUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2, 1, 4),
    _Gs2326QosPortPolicingUnit_Type()
)
gs2326QosPortPolicingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortPolicingUnit.setStatus("current")


class _Gs2326QosPortPolicingFlowControl_Type(Integer32):
    """Custom type gs2326QosPortPolicingFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosPortPolicingFlowControl_Type.__name__ = "Integer32"
_Gs2326QosPortPolicingFlowControl_Object = MibTableColumn
gs2326QosPortPolicingFlowControl = _Gs2326QosPortPolicingFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 2, 1, 5),
    _Gs2326QosPortPolicingFlowControl_Type()
)
gs2326QosPortPolicingFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortPolicingFlowControl.setStatus("current")
_Gs2326QosPortScheduler_ObjectIdentity = ObjectIdentity
gs2326QosPortScheduler = _Gs2326QosPortScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3)
)
_Gs2326QosPortSchedulerModeTable_Object = MibTable
gs2326QosPortSchedulerModeTable = _Gs2326QosPortSchedulerModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    gs2326QosPortSchedulerModeTable.setStatus("current")
_Gs2326QosPortSchedulerModeEntry_Object = MibTableRow
gs2326QosPortSchedulerModeEntry = _Gs2326QosPortSchedulerModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 1, 1)
)
gs2326QosPortSchedulerModeEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosSchedulerModePort"),
)
if mibBuilder.loadTexts:
    gs2326QosPortSchedulerModeEntry.setStatus("current")


class _Gs2326QosSchedulerModePort_Type(Integer32):
    """Custom type gs2326QosSchedulerModePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosSchedulerModePort_Type.__name__ = "Integer32"
_Gs2326QosSchedulerModePort_Object = MibTableColumn
gs2326QosSchedulerModePort = _Gs2326QosSchedulerModePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 1, 1, 1),
    _Gs2326QosSchedulerModePort_Type()
)
gs2326QosSchedulerModePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosSchedulerModePort.setStatus("current")


class _Gs2326QosSchedulerMode_Type(Integer32):
    """Custom type gs2326QosSchedulerMode based on Integer32"""
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


_Gs2326QosSchedulerMode_Type.__name__ = "Integer32"
_Gs2326QosSchedulerMode_Object = MibTableColumn
gs2326QosSchedulerMode = _Gs2326QosSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 1, 1, 2),
    _Gs2326QosSchedulerMode_Type()
)
gs2326QosSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerMode.setStatus("current")


class _Gs2326QosSchedulerShaper_Type(Integer32):
    """Custom type gs2326QosSchedulerShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosSchedulerShaper_Type.__name__ = "Integer32"
_Gs2326QosSchedulerShaper_Object = MibTableColumn
gs2326QosSchedulerShaper = _Gs2326QosSchedulerShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 1, 1, 3),
    _Gs2326QosSchedulerShaper_Type()
)
gs2326QosSchedulerShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerShaper.setStatus("current")


class _Gs2326QosSchedulerShaperRate_Type(Integer32):
    """Custom type gs2326QosSchedulerShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2326QosSchedulerShaperRate_Type.__name__ = "Integer32"
_Gs2326QosSchedulerShaperRate_Object = MibTableColumn
gs2326QosSchedulerShaperRate = _Gs2326QosSchedulerShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 1, 1, 4),
    _Gs2326QosSchedulerShaperRate_Type()
)
gs2326QosSchedulerShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerShaperRate.setStatus("current")
_Gs2326QosPortSchedulerTable_Object = MibTable
gs2326QosPortSchedulerTable = _Gs2326QosPortSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326QosPortSchedulerTable.setStatus("current")
_Gs2326QosPortSchedulerEntry_Object = MibTableRow
gs2326QosPortSchedulerEntry = _Gs2326QosPortSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1)
)
gs2326QosPortSchedulerEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosSchedulerPort"),
    (0, "LANCOM-GS-2326-MIB", "gs2326QosSchedulerPortQueue"),
)
if mibBuilder.loadTexts:
    gs2326QosPortSchedulerEntry.setStatus("current")


class _Gs2326QosSchedulerPort_Type(Integer32):
    """Custom type gs2326QosSchedulerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosSchedulerPort_Type.__name__ = "Integer32"
_Gs2326QosSchedulerPort_Object = MibTableColumn
gs2326QosSchedulerPort = _Gs2326QosSchedulerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 1),
    _Gs2326QosSchedulerPort_Type()
)
gs2326QosSchedulerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPort.setStatus("current")


class _Gs2326QosSchedulerPortQueue_Type(Integer32):
    """Custom type gs2326QosSchedulerPortQueue based on Integer32"""
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


_Gs2326QosSchedulerPortQueue_Type.__name__ = "Integer32"
_Gs2326QosSchedulerPortQueue_Object = MibTableColumn
gs2326QosSchedulerPortQueue = _Gs2326QosSchedulerPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 2),
    _Gs2326QosSchedulerPortQueue_Type()
)
gs2326QosSchedulerPortQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPortQueue.setStatus("current")


class _Gs2326QosSchedulerPortQueueShaper_Type(Integer32):
    """Custom type gs2326QosSchedulerPortQueueShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosSchedulerPortQueueShaper_Type.__name__ = "Integer32"
_Gs2326QosSchedulerPortQueueShaper_Object = MibTableColumn
gs2326QosSchedulerPortQueueShaper = _Gs2326QosSchedulerPortQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 3),
    _Gs2326QosSchedulerPortQueueShaper_Type()
)
gs2326QosSchedulerPortQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPortQueueShaper.setStatus("current")


class _Gs2326QosSchedulerPortQueueShaperRate_Type(Integer32):
    """Custom type gs2326QosSchedulerPortQueueShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2326QosSchedulerPortQueueShaperRate_Type.__name__ = "Integer32"
_Gs2326QosSchedulerPortQueueShaperRate_Object = MibTableColumn
gs2326QosSchedulerPortQueueShaperRate = _Gs2326QosSchedulerPortQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 4),
    _Gs2326QosSchedulerPortQueueShaperRate_Type()
)
gs2326QosSchedulerPortQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPortQueueShaperRate.setStatus("current")


class _Gs2326QosSchedulerPortQueueShaperExcess_Type(Integer32):
    """Custom type gs2326QosSchedulerPortQueueShaperExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosSchedulerPortQueueShaperExcess_Type.__name__ = "Integer32"
_Gs2326QosSchedulerPortQueueShaperExcess_Object = MibTableColumn
gs2326QosSchedulerPortQueueShaperExcess = _Gs2326QosSchedulerPortQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 5),
    _Gs2326QosSchedulerPortQueueShaperExcess_Type()
)
gs2326QosSchedulerPortQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPortQueueShaperExcess.setStatus("current")


class _Gs2326QosSchedulerPortQueueSchedulerWeight_Type(Integer32):
    """Custom type gs2326QosSchedulerPortQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2326QosSchedulerPortQueueSchedulerWeight_Type.__name__ = "Integer32"
_Gs2326QosSchedulerPortQueueSchedulerWeight_Object = MibTableColumn
gs2326QosSchedulerPortQueueSchedulerWeight = _Gs2326QosSchedulerPortQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 6),
    _Gs2326QosSchedulerPortQueueSchedulerWeight_Type()
)
gs2326QosSchedulerPortQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPortQueueSchedulerWeight.setStatus("current")
_Gs2326QosSchedulerPortQueueSchedulerPercent_Type = DisplayString
_Gs2326QosSchedulerPortQueueSchedulerPercent_Object = MibTableColumn
gs2326QosSchedulerPortQueueSchedulerPercent = _Gs2326QosSchedulerPortQueueSchedulerPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 3, 2, 1, 7),
    _Gs2326QosSchedulerPortQueueSchedulerPercent_Type()
)
gs2326QosSchedulerPortQueueSchedulerPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosSchedulerPortQueueSchedulerPercent.setStatus("current")
_Gs2326QosPortEgressTagRemarking_ObjectIdentity = ObjectIdentity
gs2326QosPortEgressTagRemarking = _Gs2326QosPortEgressTagRemarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4)
)
_Gs2326QosPortEgressTagRemarkingTable_Object = MibTable
gs2326QosPortEgressTagRemarkingTable = _Gs2326QosPortEgressTagRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 1)
)
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingTable.setStatus("current")
_Gs2326QosPortEgressTagRemarkingEntry_Object = MibTableRow
gs2326QosPortEgressTagRemarkingEntry = _Gs2326QosPortEgressTagRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 1, 1)
)
gs2326QosPortEgressTagRemarkingEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosEgressTagRemarkingPort"),
)
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingEntry.setStatus("current")


class _Gs2326QosEgressTagRemarkingPort_Type(Integer32):
    """Custom type gs2326QosEgressTagRemarkingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosEgressTagRemarkingPort_Type.__name__ = "Integer32"
_Gs2326QosEgressTagRemarkingPort_Object = MibTableColumn
gs2326QosEgressTagRemarkingPort = _Gs2326QosEgressTagRemarkingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 1, 1, 1),
    _Gs2326QosEgressTagRemarkingPort_Type()
)
gs2326QosEgressTagRemarkingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosEgressTagRemarkingPort.setStatus("current")


class _Gs2326QosEgressTagRemarkingMode_Type(Integer32):
    """Custom type gs2326QosEgressTagRemarkingMode based on Integer32"""
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


_Gs2326QosEgressTagRemarkingMode_Type.__name__ = "Integer32"
_Gs2326QosEgressTagRemarkingMode_Object = MibTableColumn
gs2326QosEgressTagRemarkingMode = _Gs2326QosEgressTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 1, 1, 2),
    _Gs2326QosEgressTagRemarkingMode_Type()
)
gs2326QosEgressTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosEgressTagRemarkingMode.setStatus("current")
_Gs2326QosPortEgressTagRemarkingDefTable_Object = MibTable
gs2326QosPortEgressTagRemarkingDefTable = _Gs2326QosPortEgressTagRemarkingDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingDefTable.setStatus("current")
_Gs2326QosPortEgressTagRemarkingDefEntry_Object = MibTableRow
gs2326QosPortEgressTagRemarkingDefEntry = _Gs2326QosPortEgressTagRemarkingDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 2, 1)
)
gs2326QosPortEgressTagRemarkingDefEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosEgressTagRemarkingDefPort"),
)
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingDefEntry.setStatus("current")


class _Gs2326QosEgressTagRemarkingDefPort_Type(Integer32):
    """Custom type gs2326QosEgressTagRemarkingDefPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosEgressTagRemarkingDefPort_Type.__name__ = "Integer32"
_Gs2326QosEgressTagRemarkingDefPort_Object = MibTableColumn
gs2326QosEgressTagRemarkingDefPort = _Gs2326QosEgressTagRemarkingDefPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 2, 1, 1),
    _Gs2326QosEgressTagRemarkingDefPort_Type()
)
gs2326QosEgressTagRemarkingDefPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosEgressTagRemarkingDefPort.setStatus("current")


class _Gs2326QosEgressTagRemarkingDefPCP_Type(Integer32):
    """Custom type gs2326QosEgressTagRemarkingDefPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326QosEgressTagRemarkingDefPCP_Type.__name__ = "Integer32"
_Gs2326QosEgressTagRemarkingDefPCP_Object = MibTableColumn
gs2326QosEgressTagRemarkingDefPCP = _Gs2326QosEgressTagRemarkingDefPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 2, 1, 2),
    _Gs2326QosEgressTagRemarkingDefPCP_Type()
)
gs2326QosEgressTagRemarkingDefPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosEgressTagRemarkingDefPCP.setStatus("current")


class _Gs2326QosEgressTagRemarkingDefDEI_Type(Integer32):
    """Custom type gs2326QosEgressTagRemarkingDefDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosEgressTagRemarkingDefDEI_Type.__name__ = "Integer32"
_Gs2326QosEgressTagRemarkingDefDEI_Object = MibTableColumn
gs2326QosEgressTagRemarkingDefDEI = _Gs2326QosEgressTagRemarkingDefDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 2, 1, 3),
    _Gs2326QosEgressTagRemarkingDefDEI_Type()
)
gs2326QosEgressTagRemarkingDefDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosEgressTagRemarkingDefDEI.setStatus("current")
_Gs2326QosPortEgressTagRemarkingMapTable_Object = MibTable
gs2326QosPortEgressTagRemarkingMapTable = _Gs2326QosPortEgressTagRemarkingMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingMapTable.setStatus("current")
_Gs2326QosPortEgressTagRemarkingMapEntry_Object = MibTableRow
gs2326QosPortEgressTagRemarkingMapEntry = _Gs2326QosPortEgressTagRemarkingMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4, 1)
)
gs2326QosPortEgressTagRemarkingMapEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosPortEgressTagRemarkingMapPort"),
    (0, "LANCOM-GS-2326-MIB", "gs2326QosTagRemarkingQoSClass"),
    (0, "LANCOM-GS-2326-MIB", "gs2326QosTagRemarkingDPLevel"),
)
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingMapEntry.setStatus("current")


class _Gs2326QosPortEgressTagRemarkingMapPort_Type(Integer32):
    """Custom type gs2326QosPortEgressTagRemarkingMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosPortEgressTagRemarkingMapPort_Type.__name__ = "Integer32"
_Gs2326QosPortEgressTagRemarkingMapPort_Object = MibTableColumn
gs2326QosPortEgressTagRemarkingMapPort = _Gs2326QosPortEgressTagRemarkingMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4, 1, 1),
    _Gs2326QosPortEgressTagRemarkingMapPort_Type()
)
gs2326QosPortEgressTagRemarkingMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosPortEgressTagRemarkingMapPort.setStatus("current")


class _Gs2326QosTagRemarkingQoSClass_Type(Integer32):
    """Custom type gs2326QosTagRemarkingQoSClass based on Integer32"""
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


_Gs2326QosTagRemarkingQoSClass_Type.__name__ = "Integer32"
_Gs2326QosTagRemarkingQoSClass_Object = MibTableColumn
gs2326QosTagRemarkingQoSClass = _Gs2326QosTagRemarkingQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4, 1, 2),
    _Gs2326QosTagRemarkingQoSClass_Type()
)
gs2326QosTagRemarkingQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosTagRemarkingQoSClass.setStatus("current")


class _Gs2326QosTagRemarkingDPLevel_Type(Integer32):
    """Custom type gs2326QosTagRemarkingDPLevel based on Integer32"""
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


_Gs2326QosTagRemarkingDPLevel_Type.__name__ = "Integer32"
_Gs2326QosTagRemarkingDPLevel_Object = MibTableColumn
gs2326QosTagRemarkingDPLevel = _Gs2326QosTagRemarkingDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4, 1, 3),
    _Gs2326QosTagRemarkingDPLevel_Type()
)
gs2326QosTagRemarkingDPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosTagRemarkingDPLevel.setStatus("current")


class _Gs2326QosTagRemarkingPCP_Type(Integer32):
    """Custom type gs2326QosTagRemarkingPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326QosTagRemarkingPCP_Type.__name__ = "Integer32"
_Gs2326QosTagRemarkingPCP_Object = MibTableColumn
gs2326QosTagRemarkingPCP = _Gs2326QosTagRemarkingPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4, 1, 4),
    _Gs2326QosTagRemarkingPCP_Type()
)
gs2326QosTagRemarkingPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosTagRemarkingPCP.setStatus("current")


class _Gs2326QosTagRemarkingDEI_Type(Integer32):
    """Custom type gs2326QosTagRemarkingDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2326QosTagRemarkingDEI_Type.__name__ = "Integer32"
_Gs2326QosTagRemarkingDEI_Object = MibTableColumn
gs2326QosTagRemarkingDEI = _Gs2326QosTagRemarkingDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 4, 4, 1, 5),
    _Gs2326QosTagRemarkingDEI_Type()
)
gs2326QosTagRemarkingDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosTagRemarkingDEI.setStatus("current")
_Gs2326QosPortDSCPTable_Object = MibTable
gs2326QosPortDSCPTable = _Gs2326QosPortDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 5)
)
if mibBuilder.loadTexts:
    gs2326QosPortDSCPTable.setStatus("current")
_Gs2326QosPortDSCPEntry_Object = MibTableRow
gs2326QosPortDSCPEntry = _Gs2326QosPortDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 5, 1)
)
gs2326QosPortDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosPortDSCPPort"),
)
if mibBuilder.loadTexts:
    gs2326QosPortDSCPEntry.setStatus("current")


class _Gs2326QosPortDSCPPort_Type(Integer32):
    """Custom type gs2326QosPortDSCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosPortDSCPPort_Type.__name__ = "Integer32"
_Gs2326QosPortDSCPPort_Object = MibTableColumn
gs2326QosPortDSCPPort = _Gs2326QosPortDSCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 5, 1, 1),
    _Gs2326QosPortDSCPPort_Type()
)
gs2326QosPortDSCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosPortDSCPPort.setStatus("current")


class _Gs2326QosPortDSCPIngressTranslate_Type(Integer32):
    """Custom type gs2326QosPortDSCPIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosPortDSCPIngressTranslate_Type.__name__ = "Integer32"
_Gs2326QosPortDSCPIngressTranslate_Object = MibTableColumn
gs2326QosPortDSCPIngressTranslate = _Gs2326QosPortDSCPIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 5, 1, 2),
    _Gs2326QosPortDSCPIngressTranslate_Type()
)
gs2326QosPortDSCPIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortDSCPIngressTranslate.setStatus("current")


class _Gs2326QosPortDSCPIngressClassify_Type(Integer32):
    """Custom type gs2326QosPortDSCPIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326QosPortDSCPIngressClassify_Type.__name__ = "Integer32"
_Gs2326QosPortDSCPIngressClassify_Object = MibTableColumn
gs2326QosPortDSCPIngressClassify = _Gs2326QosPortDSCPIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 5, 1, 3),
    _Gs2326QosPortDSCPIngressClassify_Type()
)
gs2326QosPortDSCPIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortDSCPIngressClassify.setStatus("current")


class _Gs2326QosPortDSCPEgressRewrite_Type(Integer32):
    """Custom type gs2326QosPortDSCPEgressRewrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2326QosPortDSCPEgressRewrite_Type.__name__ = "Integer32"
_Gs2326QosPortDSCPEgressRewrite_Object = MibTableColumn
gs2326QosPortDSCPEgressRewrite = _Gs2326QosPortDSCPEgressRewrite_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 5, 1, 4),
    _Gs2326QosPortDSCPEgressRewrite_Type()
)
gs2326QosPortDSCPEgressRewrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPortDSCPEgressRewrite.setStatus("current")
_Gs2326QosDSCPTable_Object = MibTable
gs2326QosDSCPTable = _Gs2326QosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6)
)
if mibBuilder.loadTexts:
    gs2326QosDSCPTable.setStatus("current")
_Gs2326QosDSCPEntry_Object = MibTableRow
gs2326QosDSCPEntry = _Gs2326QosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6, 1)
)
gs2326QosDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosDSCPList"),
)
if mibBuilder.loadTexts:
    gs2326QosDSCPEntry.setStatus("current")


class _Gs2326QosDSCPList_Type(Integer32):
    """Custom type gs2326QosDSCPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2326QosDSCPList_Type.__name__ = "Integer32"
_Gs2326QosDSCPList_Object = MibTableColumn
gs2326QosDSCPList = _Gs2326QosDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6, 1, 1),
    _Gs2326QosDSCPList_Type()
)
gs2326QosDSCPList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosDSCPList.setStatus("current")
_Gs2326QosDSCP_Type = DisplayString
_Gs2326QosDSCP_Object = MibTableColumn
gs2326QosDSCP = _Gs2326QosDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6, 1, 2),
    _Gs2326QosDSCP_Type()
)
gs2326QosDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosDSCP.setStatus("current")


class _Gs2326QosDSCPTrust_Type(Integer32):
    """Custom type gs2326QosDSCPTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosDSCPTrust_Type.__name__ = "Integer32"
_Gs2326QosDSCPTrust_Object = MibTableColumn
gs2326QosDSCPTrust = _Gs2326QosDSCPTrust_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6, 1, 3),
    _Gs2326QosDSCPTrust_Type()
)
gs2326QosDSCPTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPTrust.setStatus("current")


class _Gs2326QosDSCPQosClass_Type(Integer32):
    """Custom type gs2326QosDSCPQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2326QosDSCPQosClass_Type.__name__ = "Integer32"
_Gs2326QosDSCPQosClass_Object = MibTableColumn
gs2326QosDSCPQosClass = _Gs2326QosDSCPQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6, 1, 4),
    _Gs2326QosDSCPQosClass_Type()
)
gs2326QosDSCPQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPQosClass.setStatus("current")


class _Gs2326QosDSCPDPL_Type(Integer32):
    """Custom type gs2326QosDSCPDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2326QosDSCPDPL_Type.__name__ = "Integer32"
_Gs2326QosDSCPDPL_Object = MibTableColumn
gs2326QosDSCPDPL = _Gs2326QosDSCPDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 6, 1, 5),
    _Gs2326QosDSCPDPL_Type()
)
gs2326QosDSCPDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPDPL.setStatus("current")
_Gs2326QosDSCPTranslationTable_Object = MibTable
gs2326QosDSCPTranslationTable = _Gs2326QosDSCPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7)
)
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationTable.setStatus("current")
_Gs2326QosDSCPTranslationEntry_Object = MibTableRow
gs2326QosDSCPTranslationEntry = _Gs2326QosDSCPTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1)
)
gs2326QosDSCPTranslationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosDSCPTranslationList"),
)
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationEntry.setStatus("current")


class _Gs2326QosDSCPTranslationList_Type(Integer32):
    """Custom type gs2326QosDSCPTranslationList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2326QosDSCPTranslationList_Type.__name__ = "Integer32"
_Gs2326QosDSCPTranslationList_Object = MibTableColumn
gs2326QosDSCPTranslationList = _Gs2326QosDSCPTranslationList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1, 1),
    _Gs2326QosDSCPTranslationList_Type()
)
gs2326QosDSCPTranslationList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationList.setStatus("current")
_Gs2326QosDSCPTranslationDSCPBasedId_Type = DisplayString
_Gs2326QosDSCPTranslationDSCPBasedId_Object = MibTableColumn
gs2326QosDSCPTranslationDSCPBasedId = _Gs2326QosDSCPTranslationDSCPBasedId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1, 2),
    _Gs2326QosDSCPTranslationDSCPBasedId_Type()
)
gs2326QosDSCPTranslationDSCPBasedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationDSCPBasedId.setStatus("current")


class _Gs2326QosDSCPTranslationIngressTranslate_Type(Integer32):
    """Custom type gs2326QosDSCPTranslationIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2326QosDSCPTranslationIngressTranslate_Type.__name__ = "Integer32"
_Gs2326QosDSCPTranslationIngressTranslate_Object = MibTableColumn
gs2326QosDSCPTranslationIngressTranslate = _Gs2326QosDSCPTranslationIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1, 3),
    _Gs2326QosDSCPTranslationIngressTranslate_Type()
)
gs2326QosDSCPTranslationIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationIngressTranslate.setStatus("current")


class _Gs2326QosDSCPTranslationIngressClassify_Type(Integer32):
    """Custom type gs2326QosDSCPTranslationIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QosDSCPTranslationIngressClassify_Type.__name__ = "Integer32"
_Gs2326QosDSCPTranslationIngressClassify_Object = MibTableColumn
gs2326QosDSCPTranslationIngressClassify = _Gs2326QosDSCPTranslationIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1, 4),
    _Gs2326QosDSCPTranslationIngressClassify_Type()
)
gs2326QosDSCPTranslationIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationIngressClassify.setStatus("current")


class _Gs2326QosDSCPTranslationEgressRemapDP0_Type(Integer32):
    """Custom type gs2326QosDSCPTranslationEgressRemapDP0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2326QosDSCPTranslationEgressRemapDP0_Type.__name__ = "Integer32"
_Gs2326QosDSCPTranslationEgressRemapDP0_Object = MibTableColumn
gs2326QosDSCPTranslationEgressRemapDP0 = _Gs2326QosDSCPTranslationEgressRemapDP0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1, 5),
    _Gs2326QosDSCPTranslationEgressRemapDP0_Type()
)
gs2326QosDSCPTranslationEgressRemapDP0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationEgressRemapDP0.setStatus("current")


class _Gs2326QosDSCPTranslationEgressRemapDP1_Type(Integer32):
    """Custom type gs2326QosDSCPTranslationEgressRemapDP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2326QosDSCPTranslationEgressRemapDP1_Type.__name__ = "Integer32"
_Gs2326QosDSCPTranslationEgressRemapDP1_Object = MibTableColumn
gs2326QosDSCPTranslationEgressRemapDP1 = _Gs2326QosDSCPTranslationEgressRemapDP1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 7, 1, 6),
    _Gs2326QosDSCPTranslationEgressRemapDP1_Type()
)
gs2326QosDSCPTranslationEgressRemapDP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPTranslationEgressRemapDP1.setStatus("current")
_Gs2326QosDSCPClassificationTable_Object = MibTable
gs2326QosDSCPClassificationTable = _Gs2326QosDSCPClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 8)
)
if mibBuilder.loadTexts:
    gs2326QosDSCPClassificationTable.setStatus("current")
_Gs2326QosDSCPClassificationEntry_Object = MibTableRow
gs2326QosDSCPClassificationEntry = _Gs2326QosDSCPClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 8, 1)
)
gs2326QosDSCPClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosDSCPClassificationQoSClass"),
    (0, "LANCOM-GS-2326-MIB", "gs2326QosDSCPClassificationDPL"),
)
if mibBuilder.loadTexts:
    gs2326QosDSCPClassificationEntry.setStatus("current")


class _Gs2326QosDSCPClassificationQoSClass_Type(Integer32):
    """Custom type gs2326QosDSCPClassificationQoSClass based on Integer32"""
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


_Gs2326QosDSCPClassificationQoSClass_Type.__name__ = "Integer32"
_Gs2326QosDSCPClassificationQoSClass_Object = MibTableColumn
gs2326QosDSCPClassificationQoSClass = _Gs2326QosDSCPClassificationQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 8, 1, 1),
    _Gs2326QosDSCPClassificationQoSClass_Type()
)
gs2326QosDSCPClassificationQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosDSCPClassificationQoSClass.setStatus("current")


class _Gs2326QosDSCPClassificationDPL_Type(Integer32):
    """Custom type gs2326QosDSCPClassificationDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2326QosDSCPClassificationDPL_Type.__name__ = "Integer32"
_Gs2326QosDSCPClassificationDPL_Object = MibTableColumn
gs2326QosDSCPClassificationDPL = _Gs2326QosDSCPClassificationDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 8, 1, 2),
    _Gs2326QosDSCPClassificationDPL_Type()
)
gs2326QosDSCPClassificationDPL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosDSCPClassificationDPL.setStatus("current")


class _Gs2326QosDSCPClassificationDSCP_Type(Integer32):
    """Custom type gs2326QosDSCPClassificationDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2326QosDSCPClassificationDSCP_Type.__name__ = "Integer32"
_Gs2326QosDSCPClassificationDSCP_Object = MibTableColumn
gs2326QosDSCPClassificationDSCP = _Gs2326QosDSCPClassificationDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 8, 1, 3),
    _Gs2326QosDSCPClassificationDSCP_Type()
)
gs2326QosDSCPClassificationDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDSCPClassificationDSCP.setStatus("current")
_Gs2326QosControlList_ObjectIdentity = ObjectIdentity
gs2326QosControlList = _Gs2326QosControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9)
)


class _Gs2326QosQceCreate_Type(Integer32):
    """Custom type gs2326QosQceCreate based on Integer32"""
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


_Gs2326QosQceCreate_Type.__name__ = "Integer32"
_Gs2326QosQceCreate_Object = MibScalar
gs2326QosQceCreate = _Gs2326QosQceCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 1),
    _Gs2326QosQceCreate_Type()
)
gs2326QosQceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceCreate.setStatus("current")
_Gs2326QosQceTable_Object = MibTable
gs2326QosQceTable = _Gs2326QosQceTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2)
)
if mibBuilder.loadTexts:
    gs2326QosQceTable.setStatus("current")
_Gs2326QosQceEntry_Object = MibTableRow
gs2326QosQceEntry = _Gs2326QosQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1)
)
gs2326QosQceEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosQceIndex"),
)
if mibBuilder.loadTexts:
    gs2326QosQceEntry.setStatus("current")


class _Gs2326QosQceIndex_Type(Integer32):
    """Custom type gs2326QosQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326QosQceIndex_Type.__name__ = "Integer32"
_Gs2326QosQceIndex_Object = MibTableColumn
gs2326QosQceIndex = _Gs2326QosQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 1),
    _Gs2326QosQceIndex_Type()
)
gs2326QosQceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosQceIndex.setStatus("current")


class _Gs2326QosQceID_Type(Integer32):
    """Custom type gs2326QosQceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326QosQceID_Type.__name__ = "Integer32"
_Gs2326QosQceID_Object = MibTableColumn
gs2326QosQceID = _Gs2326QosQceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 2),
    _Gs2326QosQceID_Type()
)
gs2326QosQceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceID.setStatus("current")


class _Gs2326QosQceNextID_Type(Integer32):
    """Custom type gs2326QosQceNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326QosQceNextID_Type.__name__ = "Integer32"
_Gs2326QosQceNextID_Object = MibTableColumn
gs2326QosQceNextID = _Gs2326QosQceNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 3),
    _Gs2326QosQceNextID_Type()
)
gs2326QosQceNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceNextID.setStatus("current")
_Gs2326QosQcePortMembers_Type = DisplayString
_Gs2326QosQcePortMembers_Object = MibTableColumn
gs2326QosQcePortMembers = _Gs2326QosQcePortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 4),
    _Gs2326QosQcePortMembers_Type()
)
gs2326QosQcePortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQcePortMembers.setStatus("current")
_Gs2326QosQceTag_Type = DisplayString
_Gs2326QosQceTag_Object = MibTableColumn
gs2326QosQceTag = _Gs2326QosQceTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 5),
    _Gs2326QosQceTag_Type()
)
gs2326QosQceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceTag.setStatus("current")
_Gs2326QosQceVID_Type = DisplayString
_Gs2326QosQceVID_Object = MibTableColumn
gs2326QosQceVID = _Gs2326QosQceVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 6),
    _Gs2326QosQceVID_Type()
)
gs2326QosQceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceVID.setStatus("current")
_Gs2326QosPCP_Type = DisplayString
_Gs2326QosPCP_Object = MibTableColumn
gs2326QosPCP = _Gs2326QosPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 7),
    _Gs2326QosPCP_Type()
)
gs2326QosPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosPCP.setStatus("current")
_Gs2326QosDEI_Type = DisplayString
_Gs2326QosDEI_Object = MibTableColumn
gs2326QosDEI = _Gs2326QosDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 8),
    _Gs2326QosDEI_Type()
)
gs2326QosDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDEI.setStatus("current")
_Gs2326QosSMAC_Type = DisplayString
_Gs2326QosSMAC_Object = MibTableColumn
gs2326QosSMAC = _Gs2326QosSMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 9),
    _Gs2326QosSMAC_Type()
)
gs2326QosSMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSMAC.setStatus("current")
_Gs2326QosDMACType_Type = DisplayString
_Gs2326QosDMACType_Object = MibTableColumn
gs2326QosDMACType = _Gs2326QosDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 10),
    _Gs2326QosDMACType_Type()
)
gs2326QosDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosDMACType.setStatus("current")


class _Gs2326QosFrameType_Type(Integer32):
    """Custom type gs2326QosFrameType based on Integer32"""
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


_Gs2326QosFrameType_Type.__name__ = "Integer32"
_Gs2326QosFrameType_Object = MibTableColumn
gs2326QosFrameType = _Gs2326QosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 11),
    _Gs2326QosFrameType_Type()
)
gs2326QosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosFrameType.setStatus("current")
_Gs2326QosMacEtherType_Type = DisplayString
_Gs2326QosMacEtherType_Object = MibTableColumn
gs2326QosMacEtherType = _Gs2326QosMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 12),
    _Gs2326QosMacEtherType_Type()
)
gs2326QosMacEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosMacEtherType.setStatus("current")
_Gs2326QosLLCSSAPAddr_Type = DisplayString
_Gs2326QosLLCSSAPAddr_Object = MibTableColumn
gs2326QosLLCSSAPAddr = _Gs2326QosLLCSSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 13),
    _Gs2326QosLLCSSAPAddr_Type()
)
gs2326QosLLCSSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosLLCSSAPAddr.setStatus("current")
_Gs2326QosLLCDSAPAddr_Type = DisplayString
_Gs2326QosLLCDSAPAddr_Object = MibTableColumn
gs2326QosLLCDSAPAddr = _Gs2326QosLLCDSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 14),
    _Gs2326QosLLCDSAPAddr_Type()
)
gs2326QosLLCDSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosLLCDSAPAddr.setStatus("current")
_Gs2326QosLLCControl_Type = DisplayString
_Gs2326QosLLCControl_Object = MibTableColumn
gs2326QosLLCControl = _Gs2326QosLLCControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 15),
    _Gs2326QosLLCControl_Type()
)
gs2326QosLLCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosLLCControl.setStatus("current")
_Gs2326QosSNAPPID_Type = DisplayString
_Gs2326QosSNAPPID_Object = MibTableColumn
gs2326QosSNAPPID = _Gs2326QosSNAPPID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 16),
    _Gs2326QosSNAPPID_Type()
)
gs2326QosSNAPPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosSNAPPID.setStatus("current")
_Gs2326QosIpv4Protocol_Type = DisplayString
_Gs2326QosIpv4Protocol_Object = MibTableColumn
gs2326QosIpv4Protocol = _Gs2326QosIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 17),
    _Gs2326QosIpv4Protocol_Type()
)
gs2326QosIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4Protocol.setStatus("current")


class _Gs2326QosIpv4ProtocolValue_Type(Integer32):
    """Custom type gs2326QosIpv4ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2326QosIpv4ProtocolValue_Type.__name__ = "Integer32"
_Gs2326QosIpv4ProtocolValue_Object = MibTableColumn
gs2326QosIpv4ProtocolValue = _Gs2326QosIpv4ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 18),
    _Gs2326QosIpv4ProtocolValue_Type()
)
gs2326QosIpv4ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4ProtocolValue.setStatus("current")
_Gs2326QosIpv4ProtocolUDPSport_Type = DisplayString
_Gs2326QosIpv4ProtocolUDPSport_Object = MibTableColumn
gs2326QosIpv4ProtocolUDPSport = _Gs2326QosIpv4ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 19),
    _Gs2326QosIpv4ProtocolUDPSport_Type()
)
gs2326QosIpv4ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4ProtocolUDPSport.setStatus("current")
_Gs2326QosIpv4ProtocolUDPDport_Type = DisplayString
_Gs2326QosIpv4ProtocolUDPDport_Object = MibTableColumn
gs2326QosIpv4ProtocolUDPDport = _Gs2326QosIpv4ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 20),
    _Gs2326QosIpv4ProtocolUDPDport_Type()
)
gs2326QosIpv4ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4ProtocolUDPDport.setStatus("current")
_Gs2326QosIpv4ProtocolTCPSport_Type = DisplayString
_Gs2326QosIpv4ProtocolTCPSport_Object = MibTableColumn
gs2326QosIpv4ProtocolTCPSport = _Gs2326QosIpv4ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 21),
    _Gs2326QosIpv4ProtocolTCPSport_Type()
)
gs2326QosIpv4ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4ProtocolTCPSport.setStatus("current")
_Gs2326QosIpv4ProtocolTCPDport_Type = DisplayString
_Gs2326QosIpv4ProtocolTCPDport_Object = MibTableColumn
gs2326QosIpv4ProtocolTCPDport = _Gs2326QosIpv4ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 22),
    _Gs2326QosIpv4ProtocolTCPDport_Type()
)
gs2326QosIpv4ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4ProtocolTCPDport.setStatus("current")
_Gs2326QosIpv4Ip_Type = DisplayString
_Gs2326QosIpv4Ip_Object = MibTableColumn
gs2326QosIpv4Ip = _Gs2326QosIpv4Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 23),
    _Gs2326QosIpv4Ip_Type()
)
gs2326QosIpv4Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4Ip.setStatus("current")
_Gs2326QosIpv4Mask_Type = DisplayString
_Gs2326QosIpv4Mask_Object = MibTableColumn
gs2326QosIpv4Mask = _Gs2326QosIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 24),
    _Gs2326QosIpv4Mask_Type()
)
gs2326QosIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4Mask.setStatus("current")


class _Gs2326QosIpv4IPFragment_Type(Integer32):
    """Custom type gs2326QosIpv4IPFragment based on Integer32"""
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


_Gs2326QosIpv4IPFragment_Type.__name__ = "Integer32"
_Gs2326QosIpv4IPFragment_Object = MibTableColumn
gs2326QosIpv4IPFragment = _Gs2326QosIpv4IPFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 25),
    _Gs2326QosIpv4IPFragment_Type()
)
gs2326QosIpv4IPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4IPFragment.setStatus("current")
_Gs2326QosIpv4DSCP_Type = DisplayString
_Gs2326QosIpv4DSCP_Object = MibTableColumn
gs2326QosIpv4DSCP = _Gs2326QosIpv4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 26),
    _Gs2326QosIpv4DSCP_Type()
)
gs2326QosIpv4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv4DSCP.setStatus("current")
_Gs2326QosIpv6Protocol_Type = DisplayString
_Gs2326QosIpv6Protocol_Object = MibTableColumn
gs2326QosIpv6Protocol = _Gs2326QosIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 27),
    _Gs2326QosIpv6Protocol_Type()
)
gs2326QosIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6Protocol.setStatus("current")


class _Gs2326QosIpv6ProtocolValue_Type(Integer32):
    """Custom type gs2326QosIpv6ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2326QosIpv6ProtocolValue_Type.__name__ = "Integer32"
_Gs2326QosIpv6ProtocolValue_Object = MibTableColumn
gs2326QosIpv6ProtocolValue = _Gs2326QosIpv6ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 28),
    _Gs2326QosIpv6ProtocolValue_Type()
)
gs2326QosIpv6ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6ProtocolValue.setStatus("current")
_Gs2326QosIpv6ProtocolUDPSport_Type = DisplayString
_Gs2326QosIpv6ProtocolUDPSport_Object = MibTableColumn
gs2326QosIpv6ProtocolUDPSport = _Gs2326QosIpv6ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 29),
    _Gs2326QosIpv6ProtocolUDPSport_Type()
)
gs2326QosIpv6ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6ProtocolUDPSport.setStatus("current")
_Gs2326QosIpv6ProtocolUDPDport_Type = DisplayString
_Gs2326QosIpv6ProtocolUDPDport_Object = MibTableColumn
gs2326QosIpv6ProtocolUDPDport = _Gs2326QosIpv6ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 30),
    _Gs2326QosIpv6ProtocolUDPDport_Type()
)
gs2326QosIpv6ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6ProtocolUDPDport.setStatus("current")
_Gs2326QosIpv6ProtocolTCPSport_Type = DisplayString
_Gs2326QosIpv6ProtocolTCPSport_Object = MibTableColumn
gs2326QosIpv6ProtocolTCPSport = _Gs2326QosIpv6ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 31),
    _Gs2326QosIpv6ProtocolTCPSport_Type()
)
gs2326QosIpv6ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6ProtocolTCPSport.setStatus("current")
_Gs2326QosIpv6ProtocolTCPDport_Type = DisplayString
_Gs2326QosIpv6ProtocolTCPDport_Object = MibTableColumn
gs2326QosIpv6ProtocolTCPDport = _Gs2326QosIpv6ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 32),
    _Gs2326QosIpv6ProtocolTCPDport_Type()
)
gs2326QosIpv6ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6ProtocolTCPDport.setStatus("current")
_Gs2326QosIpv6Ip_Type = DisplayString
_Gs2326QosIpv6Ip_Object = MibTableColumn
gs2326QosIpv6Ip = _Gs2326QosIpv6Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 33),
    _Gs2326QosIpv6Ip_Type()
)
gs2326QosIpv6Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6Ip.setStatus("current")
_Gs2326QosIpv6Mask_Type = DisplayString
_Gs2326QosIpv6Mask_Object = MibTableColumn
gs2326QosIpv6Mask = _Gs2326QosIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 34),
    _Gs2326QosIpv6Mask_Type()
)
gs2326QosIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6Mask.setStatus("current")
_Gs2326QosIpv6DSCP_Type = DisplayString
_Gs2326QosIpv6DSCP_Object = MibTableColumn
gs2326QosIpv6DSCP = _Gs2326QosIpv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 35),
    _Gs2326QosIpv6DSCP_Type()
)
gs2326QosIpv6DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosIpv6DSCP.setStatus("current")


class _Gs2326QosActionClass_Type(Integer32):
    """Custom type gs2326QosActionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2326QosActionClass_Type.__name__ = "Integer32"
_Gs2326QosActionClass_Object = MibTableColumn
gs2326QosActionClass = _Gs2326QosActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 36),
    _Gs2326QosActionClass_Type()
)
gs2326QosActionClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosActionClass.setStatus("current")


class _Gs2326QosActionDPL_Type(Integer32):
    """Custom type gs2326QosActionDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2326QosActionDPL_Type.__name__ = "Integer32"
_Gs2326QosActionDPL_Object = MibTableColumn
gs2326QosActionDPL = _Gs2326QosActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 37),
    _Gs2326QosActionDPL_Type()
)
gs2326QosActionDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosActionDPL.setStatus("current")


class _Gs2326QosActionDSCP_Type(Integer32):
    """Custom type gs2326QosActionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2326QosActionDSCP_Type.__name__ = "Integer32"
_Gs2326QosActionDSCP_Object = MibTableColumn
gs2326QosActionDSCP = _Gs2326QosActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 38),
    _Gs2326QosActionDSCP_Type()
)
gs2326QosActionDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosActionDSCP.setStatus("current")


class _Gs2326QosQceRowStatus_Type(Integer32):
    """Custom type gs2326QosQceRowStatus based on Integer32"""
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


_Gs2326QosQceRowStatus_Type.__name__ = "Integer32"
_Gs2326QosQceRowStatus_Object = MibTableColumn
gs2326QosQceRowStatus = _Gs2326QosQceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 2, 1, 39),
    _Gs2326QosQceRowStatus_Type()
)
gs2326QosQceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceRowStatus.setStatus("current")


class _Gs2326QosQceMoveID_Type(Integer32):
    """Custom type gs2326QosQceMoveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2326QosQceMoveID_Type.__name__ = "Integer32"
_Gs2326QosQceMoveID_Object = MibScalar
gs2326QosQceMoveID = _Gs2326QosQceMoveID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 3),
    _Gs2326QosQceMoveID_Type()
)
gs2326QosQceMoveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceMoveID.setStatus("current")


class _Gs2326QosQceMoveNextID_Type(Integer32):
    """Custom type gs2326QosQceMoveNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2326QosQceMoveNextID_Type.__name__ = "Integer32"
_Gs2326QosQceMoveNextID_Object = MibScalar
gs2326QosQceMoveNextID = _Gs2326QosQceMoveNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 9, 4),
    _Gs2326QosQceMoveNextID_Type()
)
gs2326QosQceMoveNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QosQceMoveNextID.setStatus("current")
_Gs2326QosQCLStatusTable_Object = MibTable
gs2326QosQCLStatusTable = _Gs2326QosQCLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10)
)
if mibBuilder.loadTexts:
    gs2326QosQCLStatusTable.setStatus("current")
_Gs2326QosQCLStatusEntry_Object = MibTableRow
gs2326QosQCLStatusEntry = _Gs2326QosQCLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1)
)
gs2326QosQCLStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326QosQCLStatusList"),
)
if mibBuilder.loadTexts:
    gs2326QosQCLStatusEntry.setStatus("current")


class _Gs2326QosQCLStatusList_Type(Integer32):
    """Custom type gs2326QosQCLStatusList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326QosQCLStatusList_Type.__name__ = "Integer32"
_Gs2326QosQCLStatusList_Object = MibTableColumn
gs2326QosQCLStatusList = _Gs2326QosQCLStatusList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 1),
    _Gs2326QosQCLStatusList_Type()
)
gs2326QosQCLStatusList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusList.setStatus("current")
_Gs2326QosQCLStatusUser_Type = DisplayString
_Gs2326QosQCLStatusUser_Object = MibTableColumn
gs2326QosQCLStatusUser = _Gs2326QosQCLStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 2),
    _Gs2326QosQCLStatusUser_Type()
)
gs2326QosQCLStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusUser.setStatus("current")
_Gs2326QosQCLStatusQCEId_Type = DisplayString
_Gs2326QosQCLStatusQCEId_Object = MibTableColumn
gs2326QosQCLStatusQCEId = _Gs2326QosQCLStatusQCEId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 3),
    _Gs2326QosQCLStatusQCEId_Type()
)
gs2326QosQCLStatusQCEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusQCEId.setStatus("current")
_Gs2326QosQCLStatusFrameType_Type = DisplayString
_Gs2326QosQCLStatusFrameType_Object = MibTableColumn
gs2326QosQCLStatusFrameType = _Gs2326QosQCLStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 4),
    _Gs2326QosQCLStatusFrameType_Type()
)
gs2326QosQCLStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusFrameType.setStatus("current")
_Gs2326QosQCLStatusPortlist_Type = DisplayString
_Gs2326QosQCLStatusPortlist_Object = MibTableColumn
gs2326QosQCLStatusPortlist = _Gs2326QosQCLStatusPortlist_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 5),
    _Gs2326QosQCLStatusPortlist_Type()
)
gs2326QosQCLStatusPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusPortlist.setStatus("current")
_Gs2326QosQCLStatusActionClass_Type = DisplayString
_Gs2326QosQCLStatusActionClass_Object = MibTableColumn
gs2326QosQCLStatusActionClass = _Gs2326QosQCLStatusActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 6),
    _Gs2326QosQCLStatusActionClass_Type()
)
gs2326QosQCLStatusActionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusActionClass.setStatus("current")
_Gs2326QosQCLStatusActionDPL_Type = DisplayString
_Gs2326QosQCLStatusActionDPL_Object = MibTableColumn
gs2326QosQCLStatusActionDPL = _Gs2326QosQCLStatusActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 7),
    _Gs2326QosQCLStatusActionDPL_Type()
)
gs2326QosQCLStatusActionDPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusActionDPL.setStatus("current")
_Gs2326QosQCLStatusActionDSCP_Type = DisplayString
_Gs2326QosQCLStatusActionDSCP_Object = MibTableColumn
gs2326QosQCLStatusActionDSCP = _Gs2326QosQCLStatusActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 8),
    _Gs2326QosQCLStatusActionDSCP_Type()
)
gs2326QosQCLStatusActionDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusActionDSCP.setStatus("current")
_Gs2326QosQCLStatusActionConflict_Type = DisplayString
_Gs2326QosQCLStatusActionConflict_Object = MibTableColumn
gs2326QosQCLStatusActionConflict = _Gs2326QosQCLStatusActionConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 10, 1, 9),
    _Gs2326QosQCLStatusActionConflict_Type()
)
gs2326QosQCLStatusActionConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326QosQCLStatusActionConflict.setStatus("current")
_Gs2326QosStormControl_ObjectIdentity = ObjectIdentity
gs2326QosStormControl = _Gs2326QosStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11)
)


class _Gs2326QoSStormControlUC_Type(Integer32):
    """Custom type gs2326QoSStormControlUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QoSStormControlUC_Type.__name__ = "Integer32"
_Gs2326QoSStormControlUC_Object = MibScalar
gs2326QoSStormControlUC = _Gs2326QoSStormControlUC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11, 2),
    _Gs2326QoSStormControlUC_Type()
)
gs2326QoSStormControlUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSStormControlUC.setStatus("current")
_Gs2326QoSStormControlUCRate_Type = DisplayString
_Gs2326QoSStormControlUCRate_Object = MibScalar
gs2326QoSStormControlUCRate = _Gs2326QoSStormControlUCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11, 3),
    _Gs2326QoSStormControlUCRate_Type()
)
gs2326QoSStormControlUCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSStormControlUCRate.setStatus("current")


class _Gs2326QoSStormControlMC_Type(Integer32):
    """Custom type gs2326QoSStormControlMC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QoSStormControlMC_Type.__name__ = "Integer32"
_Gs2326QoSStormControlMC_Object = MibScalar
gs2326QoSStormControlMC = _Gs2326QoSStormControlMC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11, 4),
    _Gs2326QoSStormControlMC_Type()
)
gs2326QoSStormControlMC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSStormControlMC.setStatus("current")
_Gs2326QoSStormControlMCRate_Type = DisplayString
_Gs2326QoSStormControlMCRate_Object = MibScalar
gs2326QoSStormControlMCRate = _Gs2326QoSStormControlMCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11, 5),
    _Gs2326QoSStormControlMCRate_Type()
)
gs2326QoSStormControlMCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSStormControlMCRate.setStatus("current")


class _Gs2326QoSStormControlBC_Type(Integer32):
    """Custom type gs2326QoSStormControlBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326QoSStormControlBC_Type.__name__ = "Integer32"
_Gs2326QoSStormControlBC_Object = MibScalar
gs2326QoSStormControlBC = _Gs2326QoSStormControlBC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11, 6),
    _Gs2326QoSStormControlBC_Type()
)
gs2326QoSStormControlBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSStormControlBC.setStatus("current")
_Gs2326QoSStormControlBCRate_Type = DisplayString
_Gs2326QoSStormControlBCRate_Object = MibScalar
gs2326QoSStormControlBCRate = _Gs2326QoSStormControlBCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 14, 11, 7),
    _Gs2326QoSStormControlBCRate_Type()
)
gs2326QoSStormControlBCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326QoSStormControlBCRate.setStatus("current")
_Gs2326Vlan_ObjectIdentity = ObjectIdentity
gs2326Vlan = _Gs2326Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15)
)
_Gs2326VlanPorts_ObjectIdentity = ObjectIdentity
gs2326VlanPorts = _Gs2326VlanPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1)
)


class _Gs2326VlanPortsTPIDforCustomSport_Type(OctetString):
    """Custom type gs2326VlanPortsTPIDforCustomSport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Gs2326VlanPortsTPIDforCustomSport_Type.__name__ = "OctetString"
_Gs2326VlanPortsTPIDforCustomSport_Object = MibScalar
gs2326VlanPortsTPIDforCustomSport = _Gs2326VlanPortsTPIDforCustomSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 1),
    _Gs2326VlanPortsTPIDforCustomSport_Type()
)
gs2326VlanPortsTPIDforCustomSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortsTPIDforCustomSport.setStatus("current")
_Gs2326VlanPortsTable_Object = MibTable
gs2326VlanPortsTable = _Gs2326VlanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326VlanPortsTable.setStatus("current")
_Gs2326VlanPortsEntry_Object = MibTableRow
gs2326VlanPortsEntry = _Gs2326VlanPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1)
)
gs2326VlanPortsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326VlanPortsPort"),
)
if mibBuilder.loadTexts:
    gs2326VlanPortsEntry.setStatus("current")


class _Gs2326VlanPortsPort_Type(Integer32):
    """Custom type gs2326VlanPortsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326VlanPortsPort_Type.__name__ = "Integer32"
_Gs2326VlanPortsPort_Object = MibTableColumn
gs2326VlanPortsPort = _Gs2326VlanPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1, 1),
    _Gs2326VlanPortsPort_Type()
)
gs2326VlanPortsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326VlanPortsPort.setStatus("current")


class _Gs2326VlanPortsPVID_Type(Integer32):
    """Custom type gs2326VlanPortsPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326VlanPortsPVID_Type.__name__ = "Integer32"
_Gs2326VlanPortsPVID_Object = MibTableColumn
gs2326VlanPortsPVID = _Gs2326VlanPortsPVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1, 2),
    _Gs2326VlanPortsPVID_Type()
)
gs2326VlanPortsPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortsPVID.setStatus("current")


class _Gs2326VlanPortsFrameType_Type(Integer32):
    """Custom type gs2326VlanPortsFrameType based on Integer32"""
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


_Gs2326VlanPortsFrameType_Type.__name__ = "Integer32"
_Gs2326VlanPortsFrameType_Object = MibTableColumn
gs2326VlanPortsFrameType = _Gs2326VlanPortsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1, 3),
    _Gs2326VlanPortsFrameType_Type()
)
gs2326VlanPortsFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortsFrameType.setStatus("current")


class _Gs2326VlanPortsIngressFilter_Type(Integer32):
    """Custom type gs2326VlanPortsIngressFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326VlanPortsIngressFilter_Type.__name__ = "Integer32"
_Gs2326VlanPortsIngressFilter_Object = MibTableColumn
gs2326VlanPortsIngressFilter = _Gs2326VlanPortsIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1, 4),
    _Gs2326VlanPortsIngressFilter_Type()
)
gs2326VlanPortsIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortsIngressFilter.setStatus("current")


class _Gs2326VlanPortsEgressRule_Type(Integer32):
    """Custom type gs2326VlanPortsEgressRule based on Integer32"""
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


_Gs2326VlanPortsEgressRule_Type.__name__ = "Integer32"
_Gs2326VlanPortsEgressRule_Object = MibTableColumn
gs2326VlanPortsEgressRule = _Gs2326VlanPortsEgressRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1, 5),
    _Gs2326VlanPortsEgressRule_Type()
)
gs2326VlanPortsEgressRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortsEgressRule.setStatus("current")


class _Gs2326VlanPortsPortType_Type(Integer32):
    """Custom type gs2326VlanPortsPortType based on Integer32"""
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


_Gs2326VlanPortsPortType_Type.__name__ = "Integer32"
_Gs2326VlanPortsPortType_Object = MibTableColumn
gs2326VlanPortsPortType = _Gs2326VlanPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 1, 2, 1, 6),
    _Gs2326VlanPortsPortType_Type()
)
gs2326VlanPortsPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortsPortType.setStatus("current")
_Gs2326VlanPrivateVLAN_ObjectIdentity = ObjectIdentity
gs2326VlanPrivateVLAN = _Gs2326VlanPrivateVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2)
)
_Gs2326VlanPrivateVLANMembership_ObjectIdentity = ObjectIdentity
gs2326VlanPrivateVLANMembership = _Gs2326VlanPrivateVLANMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1)
)


class _Gs2326VlanPrivateVLANMembershipCreate_Type(Integer32):
    """Custom type gs2326VlanPrivateVLANMembershipCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326VlanPrivateVLANMembershipCreate_Type.__name__ = "Integer32"
_Gs2326VlanPrivateVLANMembershipCreate_Object = MibScalar
gs2326VlanPrivateVLANMembershipCreate = _Gs2326VlanPrivateVLANMembershipCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 1),
    _Gs2326VlanPrivateVLANMembershipCreate_Type()
)
gs2326VlanPrivateVLANMembershipCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANMembershipCreate.setStatus("current")
_Gs2326VlanPrivateVLANMembershipTable_Object = MibTable
gs2326VlanPrivateVLANMembershipTable = _Gs2326VlanPrivateVLANMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANMembershipTable.setStatus("current")
_Gs2326VlanPrivateVLANMembershipEntry_Object = MibTableRow
gs2326VlanPrivateVLANMembershipEntry = _Gs2326VlanPrivateVLANMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 2, 1)
)
gs2326VlanPrivateVLANMembershipEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326VlanPrivateVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANMembershipEntry.setStatus("current")


class _Gs2326VlanPrivateVLANIndex_Type(Integer32):
    """Custom type gs2326VlanPrivateVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2326VlanPrivateVLANIndex_Type.__name__ = "Integer32"
_Gs2326VlanPrivateVLANIndex_Object = MibTableColumn
gs2326VlanPrivateVLANIndex = _Gs2326VlanPrivateVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 2, 1, 1),
    _Gs2326VlanPrivateVLANIndex_Type()
)
gs2326VlanPrivateVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANIndex.setStatus("current")


class _Gs2326VlanPrivateVLANID_Type(Integer32):
    """Custom type gs2326VlanPrivateVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2326VlanPrivateVLANID_Type.__name__ = "Integer32"
_Gs2326VlanPrivateVLANID_Object = MibTableColumn
gs2326VlanPrivateVLANID = _Gs2326VlanPrivateVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 2, 1, 2),
    _Gs2326VlanPrivateVLANID_Type()
)
gs2326VlanPrivateVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANID.setStatus("current")
_Gs2326VlanPrivateVLANMemberships_Type = DisplayString
_Gs2326VlanPrivateVLANMemberships_Object = MibTableColumn
gs2326VlanPrivateVLANMemberships = _Gs2326VlanPrivateVLANMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 2, 1, 3),
    _Gs2326VlanPrivateVLANMemberships_Type()
)
gs2326VlanPrivateVLANMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANMemberships.setStatus("current")


class _Gs2326VlanPrivateVLANRowStatus_Type(Integer32):
    """Custom type gs2326VlanPrivateVLANRowStatus based on Integer32"""
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


_Gs2326VlanPrivateVLANRowStatus_Type.__name__ = "Integer32"
_Gs2326VlanPrivateVLANRowStatus_Object = MibTableColumn
gs2326VlanPrivateVLANRowStatus = _Gs2326VlanPrivateVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 1, 2, 1, 4),
    _Gs2326VlanPrivateVLANRowStatus_Type()
)
gs2326VlanPrivateVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPrivateVLANRowStatus.setStatus("current")
_Gs2326VlanPortIsolationTable_Object = MibTable
gs2326VlanPortIsolationTable = _Gs2326VlanPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326VlanPortIsolationTable.setStatus("current")
_Gs2326VlanPortIsolationEntry_Object = MibTableRow
gs2326VlanPortIsolationEntry = _Gs2326VlanPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 2, 1)
)
gs2326VlanPortIsolationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326VlanPortIsolationPort"),
)
if mibBuilder.loadTexts:
    gs2326VlanPortIsolationEntry.setStatus("current")


class _Gs2326VlanPortIsolationPort_Type(Integer32):
    """Custom type gs2326VlanPortIsolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326VlanPortIsolationPort_Type.__name__ = "Integer32"
_Gs2326VlanPortIsolationPort_Object = MibTableColumn
gs2326VlanPortIsolationPort = _Gs2326VlanPortIsolationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 2, 1, 1),
    _Gs2326VlanPortIsolationPort_Type()
)
gs2326VlanPortIsolationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326VlanPortIsolationPort.setStatus("current")


class _Gs2326VlanPortIsolation_Type(Integer32):
    """Custom type gs2326VlanPortIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326VlanPortIsolation_Type.__name__ = "Integer32"
_Gs2326VlanPortIsolation_Object = MibTableColumn
gs2326VlanPortIsolation = _Gs2326VlanPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 2, 2, 1, 2),
    _Gs2326VlanPortIsolation_Type()
)
gs2326VlanPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VlanPortIsolation.setStatus("current")
_Gs2326MACbasedVLAN_ObjectIdentity = ObjectIdentity
gs2326MACbasedVLAN = _Gs2326MACbasedVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3)
)
_Gs2326MACbasedVLANConf_ObjectIdentity = ObjectIdentity
gs2326MACbasedVLANConf = _Gs2326MACbasedVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1)
)
_Gs2326MACbasedVLANConfCreate_Type = Integer32
_Gs2326MACbasedVLANConfCreate_Object = MibScalar
gs2326MACbasedVLANConfCreate = _Gs2326MACbasedVLANConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 1),
    _Gs2326MACbasedVLANConfCreate_Type()
)
gs2326MACbasedVLANConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACbasedVLANConfCreate.setStatus("current")
_Gs2326MACbasedVLANConfTable_Object = MibTable
gs2326MACbasedVLANConfTable = _Gs2326MACbasedVLANConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326MACbasedVLANConfTable.setStatus("current")
_Gs2326MACbasedVLANConfEntry_Object = MibTableRow
gs2326MACbasedVLANConfEntry = _Gs2326MACbasedVLANConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2, 1)
)
gs2326MACbasedVLANConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MACbasedVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2326MACbasedVLANConfEntry.setStatus("current")


class _Gs2326MACbasedVLANIndex_Type(Integer32):
    """Custom type gs2326MACbasedVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2326MACbasedVLANIndex_Type.__name__ = "Integer32"
_Gs2326MACbasedVLANIndex_Object = MibTableColumn
gs2326MACbasedVLANIndex = _Gs2326MACbasedVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2, 1, 1),
    _Gs2326MACbasedVLANIndex_Type()
)
gs2326MACbasedVLANIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACbasedVLANIndex.setStatus("current")
_Gs2326MACbasedVLANMACAddress_Type = MacAddress
_Gs2326MACbasedVLANMACAddress_Object = MibTableColumn
gs2326MACbasedVLANMACAddress = _Gs2326MACbasedVLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2, 1, 2),
    _Gs2326MACbasedVLANMACAddress_Type()
)
gs2326MACbasedVLANMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACbasedVLANMACAddress.setStatus("current")


class _Gs2326MACbasedVLANID_Type(Integer32):
    """Custom type gs2326MACbasedVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326MACbasedVLANID_Type.__name__ = "Integer32"
_Gs2326MACbasedVLANID_Object = MibTableColumn
gs2326MACbasedVLANID = _Gs2326MACbasedVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2, 1, 3),
    _Gs2326MACbasedVLANID_Type()
)
gs2326MACbasedVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACbasedVLANID.setStatus("current")
_Gs2326MACbasedMemberships_Type = DisplayString
_Gs2326MACbasedMemberships_Object = MibTableColumn
gs2326MACbasedMemberships = _Gs2326MACbasedMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2, 1, 4),
    _Gs2326MACbasedMemberships_Type()
)
gs2326MACbasedMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACbasedMemberships.setStatus("current")


class _Gs2326MACbaseRowStatus_Type(Integer32):
    """Custom type gs2326MACbaseRowStatus based on Integer32"""
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


_Gs2326MACbaseRowStatus_Type.__name__ = "Integer32"
_Gs2326MACbaseRowStatus_Object = MibTableColumn
gs2326MACbaseRowStatus = _Gs2326MACbaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 15, 3, 1, 2, 1, 5),
    _Gs2326MACbaseRowStatus_Type()
)
gs2326MACbaseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MACbaseRowStatus.setStatus("current")
_Gs2326IGMPSnooping_ObjectIdentity = ObjectIdentity
gs2326IGMPSnooping = _Gs2326IGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16)
)
_Gs2326IGMPSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2326IGMPSnoopingBasic = _Gs2326IGMPSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1)
)


class _Gs2326IGMPSnoopingEnable_Type(Integer32):
    """Custom type gs2326IGMPSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingEnable_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingEnable_Object = MibScalar
gs2326IGMPSnoopingEnable = _Gs2326IGMPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 1),
    _Gs2326IGMPSnoopingEnable_Type()
)
gs2326IGMPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingEnable.setStatus("current")


class _Gs2326IGMPSnoopingUnregisteredIPMCv4Flooding_Type(Integer32):
    """Custom type gs2326IGMPSnoopingUnregisteredIPMCv4Flooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingUnregisteredIPMCv4Flooding_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingUnregisteredIPMCv4Flooding_Object = MibScalar
gs2326IGMPSnoopingUnregisteredIPMCv4Flooding = _Gs2326IGMPSnoopingUnregisteredIPMCv4Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 2),
    _Gs2326IGMPSnoopingUnregisteredIPMCv4Flooding_Type()
)
gs2326IGMPSnoopingUnregisteredIPMCv4Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingUnregisteredIPMCv4Flooding.setStatus("current")
_Gs2326IGMPSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2326IGMPSnoopingSSMIPRangeAddr_Object = MibScalar
gs2326IGMPSnoopingSSMIPRangeAddr = _Gs2326IGMPSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 3),
    _Gs2326IGMPSnoopingSSMIPRangeAddr_Type()
)
gs2326IGMPSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2326IGMPSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2326IGMPSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_Gs2326IGMPSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingSSMIPRangeValue_Object = MibScalar
gs2326IGMPSnoopingSSMIPRangeValue = _Gs2326IGMPSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 4),
    _Gs2326IGMPSnoopingSSMIPRangeValue_Type()
)
gs2326IGMPSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2326IGMPSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2326IGMPSnoopingProxyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingProxyEnabled_Object = MibScalar
gs2326IGMPSnoopingProxyEnabled = _Gs2326IGMPSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 5),
    _Gs2326IGMPSnoopingProxyEnabled_Type()
)
gs2326IGMPSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingProxyEnabled.setStatus("current")
_Gs2326IGMPSnoopingPortRelatedTable_Object = MibTable
gs2326IGMPSnoopingPortRelatedTable = _Gs2326IGMPSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortRelatedTable.setStatus("current")
_Gs2326IGMPSnoopingPortRelatedEntry_Object = MibTableRow
gs2326IGMPSnoopingPortRelatedEntry = _Gs2326IGMPSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 6, 1)
)
gs2326IGMPSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortRelatedEntry.setStatus("current")


class _Gs2326IGMPSnoopingRouterPort_Type(Integer32):
    """Custom type gs2326IGMPSnoopingRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingRouterPort_Object = MibTableColumn
gs2326IGMPSnoopingRouterPort = _Gs2326IGMPSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 6, 1, 1),
    _Gs2326IGMPSnoopingRouterPort_Type()
)
gs2326IGMPSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingRouterPort.setStatus("current")


class _Gs2326IGMPSnoopingFastLeave_Type(Integer32):
    """Custom type gs2326IGMPSnoopingFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingFastLeave_Object = MibTableColumn
gs2326IGMPSnoopingFastLeave = _Gs2326IGMPSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 6, 1, 2),
    _Gs2326IGMPSnoopingFastLeave_Type()
)
gs2326IGMPSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingFastLeave.setStatus("current")


class _Gs2326IGMPSnoopingThrottling_Type(Integer32):
    """Custom type gs2326IGMPSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2326IGMPSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingThrottling_Object = MibTableColumn
gs2326IGMPSnoopingThrottling = _Gs2326IGMPSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 1, 6, 1, 3),
    _Gs2326IGMPSnoopingThrottling_Type()
)
gs2326IGMPSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingThrottling.setStatus("current")
_Gs2326IGMPSnoopingVLANTable_Object = MibTable
gs2326IGMPSnoopingVLANTable = _Gs2326IGMPSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANTable.setStatus("current")
_Gs2326IGMPSnoopingVLANEntry_Object = MibTableRow
gs2326IGMPSnoopingVLANEntry = _Gs2326IGMPSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1)
)
gs2326IGMPSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IGMPSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANEntry.setStatus("current")


class _Gs2326IGMPSnoopingVLANID_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IGMPSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANID_Object = MibTableColumn
gs2326IGMPSnoopingVLANID = _Gs2326IGMPSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 1),
    _Gs2326IGMPSnoopingVLANID_Type()
)
gs2326IGMPSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANID.setStatus("current")


class _Gs2326IGMPSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANEnable_Object = MibTableColumn
gs2326IGMPSnoopingVLANEnable = _Gs2326IGMPSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 2),
    _Gs2326IGMPSnoopingVLANEnable_Type()
)
gs2326IGMPSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANEnable.setStatus("current")


class _Gs2326IGMPSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANIGMPQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IGMPSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2326IGMPSnoopingVLANIGMPQuerier = _Gs2326IGMPSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 3),
    _Gs2326IGMPSnoopingVLANIGMPQuerier_Type()
)
gs2326IGMPSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2326IGMPSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANCompatibility based on Integer32"""
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


_Gs2326IGMPSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANCompatibility_Object = MibTableColumn
gs2326IGMPSnoopingVLANCompatibility = _Gs2326IGMPSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 4),
    _Gs2326IGMPSnoopingVLANCompatibility_Type()
)
gs2326IGMPSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANCompatibility.setStatus("current")


class _Gs2326IGMPSnoopingVLANRV_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2326IGMPSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANRV_Object = MibTableColumn
gs2326IGMPSnoopingVLANRV = _Gs2326IGMPSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 5),
    _Gs2326IGMPSnoopingVLANRV_Type()
)
gs2326IGMPSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANRV.setStatus("current")


class _Gs2326IGMPSnoopingVLANQI_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2326IGMPSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANQI_Object = MibTableColumn
gs2326IGMPSnoopingVLANQI = _Gs2326IGMPSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 6),
    _Gs2326IGMPSnoopingVLANQI_Type()
)
gs2326IGMPSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANQI.setStatus("current")


class _Gs2326IGMPSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2326IGMPSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANQRI_Object = MibTableColumn
gs2326IGMPSnoopingVLANQRI = _Gs2326IGMPSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 7),
    _Gs2326IGMPSnoopingVLANQRI_Type()
)
gs2326IGMPSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANQRI.setStatus("current")


class _Gs2326IGMPSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2326IGMPSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANLLQI_Object = MibTableColumn
gs2326IGMPSnoopingVLANLLQI = _Gs2326IGMPSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 8),
    _Gs2326IGMPSnoopingVLANLLQI_Type()
)
gs2326IGMPSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANLLQI.setStatus("current")


class _Gs2326IGMPSnoopingVLANURI_Type(Integer32):
    """Custom type gs2326IGMPSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2326IGMPSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingVLANURI_Object = MibTableColumn
gs2326IGMPSnoopingVLANURI = _Gs2326IGMPSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 2, 1, 9),
    _Gs2326IGMPSnoopingVLANURI_Type()
)
gs2326IGMPSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingVLANURI.setStatus("current")
_Gs2326IGMPSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2326IGMPSnoopingPortGroupFiltering = _Gs2326IGMPSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3)
)
_Gs2326IGMPSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2326IGMPSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2326IGMPSnoopingPortGroupFilteringCreate = _Gs2326IGMPSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 1),
    _Gs2326IGMPSnoopingPortGroupFilteringCreate_Type()
)
gs2326IGMPSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2326IGMPSnoopingPortGroupFilteringTable_Object = MibTable
gs2326IGMPSnoopingPortGroupFilteringTable = _Gs2326IGMPSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2326IGMPSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2326IGMPSnoopingPortGroupFilteringEntry = _Gs2326IGMPSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 2, 1)
)
gs2326IGMPSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IGMPSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2326IGMPSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2326IGMPSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326IGMPSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2326IGMPSnoopingPortGroupFilteringIndex = _Gs2326IGMPSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 2, 1, 1),
    _Gs2326IGMPSnoopingPortGroupFilteringIndex_Type()
)
gs2326IGMPSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2326IGMPSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2326IGMPSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326IGMPSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2326IGMPSnoopingPortGroupFilteringPort = _Gs2326IGMPSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 2, 1, 2),
    _Gs2326IGMPSnoopingPortGroupFilteringPort_Type()
)
gs2326IGMPSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2326IGMPSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2326IGMPSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2326IGMPSnoopingPortGroupFilteringGroups = _Gs2326IGMPSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 2, 1, 3),
    _Gs2326IGMPSnoopingPortGroupFilteringGroups_Type()
)
gs2326IGMPSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2326IGMPSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2326IGMPSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2326IGMPSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2326IGMPSnoopingPortGroupFilteringRowStatus = _Gs2326IGMPSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 3, 2, 1, 4),
    _Gs2326IGMPSnoopingPortGroupFilteringRowStatus_Type()
)
gs2326IGMPSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2326IGMPSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2326IGMPSnoopingStatus = _Gs2326IGMPSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4)
)


class _Gs2326IGMPSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2326IGMPSnoopingstatisticClear based on Integer32"""
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


_Gs2326IGMPSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingstatisticClear_Object = MibScalar
gs2326IGMPSnoopingstatisticClear = _Gs2326IGMPSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 1),
    _Gs2326IGMPSnoopingstatisticClear_Type()
)
gs2326IGMPSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticClear.setStatus("current")
_Gs2326IGMPSnoopingstatisticTable_Object = MibTable
gs2326IGMPSnoopingstatisticTable = _Gs2326IGMPSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticTable.setStatus("current")
_Gs2326IGMPSnoopingstatisticEntry_Object = MibTableRow
gs2326IGMPSnoopingstatisticEntry = _Gs2326IGMPSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1)
)
gs2326IGMPSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IGMPSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticEntry.setStatus("current")


class _Gs2326IGMPSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2326IGMPSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IGMPSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingstatisticVLANID_Object = MibTableColumn
gs2326IGMPSnoopingstatisticVLANID = _Gs2326IGMPSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 1),
    _Gs2326IGMPSnoopingstatisticVLANID_Type()
)
gs2326IGMPSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticVLANID.setStatus("current")
_Gs2326IGMPSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2326IGMPSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2326IGMPSnoopingstatisticQuerierVersion = _Gs2326IGMPSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 2),
    _Gs2326IGMPSnoopingstatisticQuerierVersion_Type()
)
gs2326IGMPSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2326IGMPSnoopingstatisticHostVersion_Type = DisplayString
_Gs2326IGMPSnoopingstatisticHostVersion_Object = MibTableColumn
gs2326IGMPSnoopingstatisticHostVersion = _Gs2326IGMPSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 3),
    _Gs2326IGMPSnoopingstatisticHostVersion_Type()
)
gs2326IGMPSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticHostVersion.setStatus("current")
_Gs2326IGMPSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2326IGMPSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2326IGMPSnoopingstatisticQuerierStatus = _Gs2326IGMPSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 4),
    _Gs2326IGMPSnoopingstatisticQuerierStatus_Type()
)
gs2326IGMPSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2326IGMPSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2326IGMPSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2326IGMPSnoopingstatisticQueriesTransmitted = _Gs2326IGMPSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 5),
    _Gs2326IGMPSnoopingstatisticQueriesTransmitted_Type()
)
gs2326IGMPSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2326IGMPSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2326IGMPSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2326IGMPSnoopingstatisticQueriesReceived = _Gs2326IGMPSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 6),
    _Gs2326IGMPSnoopingstatisticQueriesReceived_Type()
)
gs2326IGMPSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2326IGMPSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2326IGMPSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2326IGMPSnoopingstatisticV1ReportsReceived = _Gs2326IGMPSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 7),
    _Gs2326IGMPSnoopingstatisticV1ReportsReceived_Type()
)
gs2326IGMPSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2326IGMPSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2326IGMPSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2326IGMPSnoopingstatisticV2ReportsReceived = _Gs2326IGMPSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 8),
    _Gs2326IGMPSnoopingstatisticV2ReportsReceived_Type()
)
gs2326IGMPSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2326IGMPSnoopingstatisticV3ReportsReceived_Type = Counter32
_Gs2326IGMPSnoopingstatisticV3ReportsReceived_Object = MibTableColumn
gs2326IGMPSnoopingstatisticV3ReportsReceived = _Gs2326IGMPSnoopingstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 9),
    _Gs2326IGMPSnoopingstatisticV3ReportsReceived_Type()
)
gs2326IGMPSnoopingstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticV3ReportsReceived.setStatus("current")
_Gs2326IGMPSnoopingstatisticV2LeavesReceived_Type = Counter32
_Gs2326IGMPSnoopingstatisticV2LeavesReceived_Object = MibTableColumn
gs2326IGMPSnoopingstatisticV2LeavesReceived = _Gs2326IGMPSnoopingstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 2, 1, 10),
    _Gs2326IGMPSnoopingstatisticV2LeavesReceived_Type()
)
gs2326IGMPSnoopingstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingstatisticV2LeavesReceived.setStatus("current")
_Gs2326IGMPSnoopingRouterPortTable_Object = MibTable
gs2326IGMPSnoopingRouterPortTable = _Gs2326IGMPSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 3)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingRouterPortTable.setStatus("current")
_Gs2326IGMPSnoopingRouterPortEntry_Object = MibTableRow
gs2326IGMPSnoopingRouterPortEntry = _Gs2326IGMPSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 3, 1)
)
gs2326IGMPSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingRouterPortEntry.setStatus("current")
_Gs2326IGMPSnoopingRouterPortStatus_Type = DisplayString
_Gs2326IGMPSnoopingRouterPortStatus_Object = MibTableColumn
gs2326IGMPSnoopingRouterPortStatus = _Gs2326IGMPSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 4, 3, 1, 1),
    _Gs2326IGMPSnoopingRouterPortStatus_Type()
)
gs2326IGMPSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingRouterPortStatus.setStatus("current")
_Gs2326IGMPSnoopingGroupsTable_Object = MibTable
gs2326IGMPSnoopingGroupsTable = _Gs2326IGMPSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 5)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingGroupsTable.setStatus("current")
_Gs2326IGMPSnoopingGroupsEntry_Object = MibTableRow
gs2326IGMPSnoopingGroupsEntry = _Gs2326IGMPSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 5, 1)
)
gs2326IGMPSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IGMPSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingGroupsEntry.setStatus("current")


class _Gs2326IGMPSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2326IGMPSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326IGMPSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingGroupsIndex_Object = MibTableColumn
gs2326IGMPSnoopingGroupsIndex = _Gs2326IGMPSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 5, 1, 1),
    _Gs2326IGMPSnoopingGroupsIndex_Type()
)
gs2326IGMPSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingGroupsIndex.setStatus("current")


class _Gs2326IGMPSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2326IGMPSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IGMPSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingGroupsVLANID_Object = MibTableColumn
gs2326IGMPSnoopingGroupsVLANID = _Gs2326IGMPSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 5, 1, 2),
    _Gs2326IGMPSnoopingGroupsVLANID_Type()
)
gs2326IGMPSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingGroupsVLANID.setStatus("current")
_Gs2326IGMPSnoopingGroups_Type = DisplayString
_Gs2326IGMPSnoopingGroups_Object = MibTableColumn
gs2326IGMPSnoopingGroups = _Gs2326IGMPSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 5, 1, 3),
    _Gs2326IGMPSnoopingGroups_Type()
)
gs2326IGMPSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingGroups.setStatus("current")
_Gs2326IGMPSnoopingGroupsMemberships_Type = DisplayString
_Gs2326IGMPSnoopingGroupsMemberships_Object = MibTableColumn
gs2326IGMPSnoopingGroupsMemberships = _Gs2326IGMPSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 5, 1, 4),
    _Gs2326IGMPSnoopingGroupsMemberships_Type()
)
gs2326IGMPSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingGroupsMemberships.setStatus("current")
_Gs2326IGMPSnoopingSSMTable_Object = MibTable
gs2326IGMPSnoopingSSMTable = _Gs2326IGMPSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6)
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMTable.setStatus("current")
_Gs2326IGMPSnoopingSSMEntry_Object = MibTableRow
gs2326IGMPSnoopingSSMEntry = _Gs2326IGMPSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1)
)
gs2326IGMPSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IGMPSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMEntry.setStatus("current")


class _Gs2326IGMPSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2326IGMPSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326IGMPSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingSSMIndex_Object = MibTableColumn
gs2326IGMPSnoopingSSMIndex = _Gs2326IGMPSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 1),
    _Gs2326IGMPSnoopingSSMIndex_Type()
)
gs2326IGMPSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMIndex.setStatus("current")


class _Gs2326IGMPSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2326IGMPSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IGMPSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingSSMVLANID_Object = MibTableColumn
gs2326IGMPSnoopingSSMVLANID = _Gs2326IGMPSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 2),
    _Gs2326IGMPSnoopingSSMVLANID_Type()
)
gs2326IGMPSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMVLANID.setStatus("current")
_Gs2326IGMPSnoopingSSMGroup_Type = DisplayString
_Gs2326IGMPSnoopingSSMGroup_Object = MibTableColumn
gs2326IGMPSnoopingSSMGroup = _Gs2326IGMPSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 3),
    _Gs2326IGMPSnoopingSSMGroup_Type()
)
gs2326IGMPSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMGroup.setStatus("current")


class _Gs2326IGMPSnoopingSSMPort_Type(Integer32):
    """Custom type gs2326IGMPSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326IGMPSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2326IGMPSnoopingSSMPort_Object = MibTableColumn
gs2326IGMPSnoopingSSMPort = _Gs2326IGMPSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 4),
    _Gs2326IGMPSnoopingSSMPort_Type()
)
gs2326IGMPSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMPort.setStatus("current")
_Gs2326IGMPSnoopingSSMMode_Type = DisplayString
_Gs2326IGMPSnoopingSSMMode_Object = MibTableColumn
gs2326IGMPSnoopingSSMMode = _Gs2326IGMPSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 5),
    _Gs2326IGMPSnoopingSSMMode_Type()
)
gs2326IGMPSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMMode.setStatus("current")
_Gs2326IGMPSnoopingSSMSourceAddress_Type = DisplayString
_Gs2326IGMPSnoopingSSMSourceAddress_Object = MibTableColumn
gs2326IGMPSnoopingSSMSourceAddress = _Gs2326IGMPSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 6),
    _Gs2326IGMPSnoopingSSMSourceAddress_Type()
)
gs2326IGMPSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMSourceAddress.setStatus("current")
_Gs2326IGMPSnoopingSSMType_Type = DisplayString
_Gs2326IGMPSnoopingSSMType_Object = MibTableColumn
gs2326IGMPSnoopingSSMType = _Gs2326IGMPSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 16, 6, 1, 7),
    _Gs2326IGMPSnoopingSSMType_Type()
)
gs2326IGMPSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IGMPSnoopingSSMType.setStatus("current")
_Gs2326MLDSnooping_ObjectIdentity = ObjectIdentity
gs2326MLDSnooping = _Gs2326MLDSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17)
)
_Gs2326MLDSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2326MLDSnoopingBasic = _Gs2326MLDSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1)
)


class _Gs2326MLDSnoopingEnable_Type(Integer32):
    """Custom type gs2326MLDSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingEnable_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingEnable_Object = MibScalar
gs2326MLDSnoopingEnable = _Gs2326MLDSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 1),
    _Gs2326MLDSnoopingEnable_Type()
)
gs2326MLDSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingEnable.setStatus("current")


class _Gs2326MLDSnoopingUnregisteredIPMCv6Flooding_Type(Integer32):
    """Custom type gs2326MLDSnoopingUnregisteredIPMCv6Flooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingUnregisteredIPMCv6Flooding_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingUnregisteredIPMCv6Flooding_Object = MibScalar
gs2326MLDSnoopingUnregisteredIPMCv6Flooding = _Gs2326MLDSnoopingUnregisteredIPMCv6Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 2),
    _Gs2326MLDSnoopingUnregisteredIPMCv6Flooding_Type()
)
gs2326MLDSnoopingUnregisteredIPMCv6Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingUnregisteredIPMCv6Flooding.setStatus("current")
_Gs2326MLDSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2326MLDSnoopingSSMIPRangeAddr_Object = MibScalar
gs2326MLDSnoopingSSMIPRangeAddr = _Gs2326MLDSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 3),
    _Gs2326MLDSnoopingSSMIPRangeAddr_Type()
)
gs2326MLDSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2326MLDSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2326MLDSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_Gs2326MLDSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingSSMIPRangeValue_Object = MibScalar
gs2326MLDSnoopingSSMIPRangeValue = _Gs2326MLDSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 4),
    _Gs2326MLDSnoopingSSMIPRangeValue_Type()
)
gs2326MLDSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2326MLDSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2326MLDSnoopingProxyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingProxyEnabled_Object = MibScalar
gs2326MLDSnoopingProxyEnabled = _Gs2326MLDSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 5),
    _Gs2326MLDSnoopingProxyEnabled_Type()
)
gs2326MLDSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingProxyEnabled.setStatus("current")
_Gs2326MLDSnoopingPortRelatedTable_Object = MibTable
gs2326MLDSnoopingPortRelatedTable = _Gs2326MLDSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 6)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortRelatedTable.setStatus("current")
_Gs2326MLDSnoopingPortRelatedEntry_Object = MibTableRow
gs2326MLDSnoopingPortRelatedEntry = _Gs2326MLDSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 6, 1)
)
gs2326MLDSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortRelatedEntry.setStatus("current")


class _Gs2326MLDSnoopingRouterPort_Type(Integer32):
    """Custom type gs2326MLDSnoopingRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingRouterPort_Object = MibTableColumn
gs2326MLDSnoopingRouterPort = _Gs2326MLDSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 6, 1, 1),
    _Gs2326MLDSnoopingRouterPort_Type()
)
gs2326MLDSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingRouterPort.setStatus("current")


class _Gs2326MLDSnoopingFastLeave_Type(Integer32):
    """Custom type gs2326MLDSnoopingFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingFastLeave_Object = MibTableColumn
gs2326MLDSnoopingFastLeave = _Gs2326MLDSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 6, 1, 2),
    _Gs2326MLDSnoopingFastLeave_Type()
)
gs2326MLDSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingFastLeave.setStatus("current")


class _Gs2326MLDSnoopingThrottling_Type(Integer32):
    """Custom type gs2326MLDSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2326MLDSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingThrottling_Object = MibTableColumn
gs2326MLDSnoopingThrottling = _Gs2326MLDSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 1, 6, 1, 3),
    _Gs2326MLDSnoopingThrottling_Type()
)
gs2326MLDSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingThrottling.setStatus("current")
_Gs2326MLDSnoopingVLANTable_Object = MibTable
gs2326MLDSnoopingVLANTable = _Gs2326MLDSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANTable.setStatus("current")
_Gs2326MLDSnoopingVLANEntry_Object = MibTableRow
gs2326MLDSnoopingVLANEntry = _Gs2326MLDSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1)
)
gs2326MLDSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MLDSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANEntry.setStatus("current")


class _Gs2326MLDSnoopingVLANID_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MLDSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANID_Object = MibTableColumn
gs2326MLDSnoopingVLANID = _Gs2326MLDSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 1),
    _Gs2326MLDSnoopingVLANID_Type()
)
gs2326MLDSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANID.setStatus("current")


class _Gs2326MLDSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANEnable_Object = MibTableColumn
gs2326MLDSnoopingVLANEnable = _Gs2326MLDSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 2),
    _Gs2326MLDSnoopingVLANEnable_Type()
)
gs2326MLDSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANEnable.setStatus("current")


class _Gs2326MLDSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANIGMPQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MLDSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2326MLDSnoopingVLANIGMPQuerier = _Gs2326MLDSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 3),
    _Gs2326MLDSnoopingVLANIGMPQuerier_Type()
)
gs2326MLDSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2326MLDSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANCompatibility based on Integer32"""
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


_Gs2326MLDSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANCompatibility_Object = MibTableColumn
gs2326MLDSnoopingVLANCompatibility = _Gs2326MLDSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 4),
    _Gs2326MLDSnoopingVLANCompatibility_Type()
)
gs2326MLDSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANCompatibility.setStatus("current")


class _Gs2326MLDSnoopingVLANRV_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2326MLDSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANRV_Object = MibTableColumn
gs2326MLDSnoopingVLANRV = _Gs2326MLDSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 5),
    _Gs2326MLDSnoopingVLANRV_Type()
)
gs2326MLDSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANRV.setStatus("current")


class _Gs2326MLDSnoopingVLANQI_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2326MLDSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANQI_Object = MibTableColumn
gs2326MLDSnoopingVLANQI = _Gs2326MLDSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 6),
    _Gs2326MLDSnoopingVLANQI_Type()
)
gs2326MLDSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANQI.setStatus("current")


class _Gs2326MLDSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2326MLDSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANQRI_Object = MibTableColumn
gs2326MLDSnoopingVLANQRI = _Gs2326MLDSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 7),
    _Gs2326MLDSnoopingVLANQRI_Type()
)
gs2326MLDSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANQRI.setStatus("current")


class _Gs2326MLDSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2326MLDSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANLLQI_Object = MibTableColumn
gs2326MLDSnoopingVLANLLQI = _Gs2326MLDSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 8),
    _Gs2326MLDSnoopingVLANLLQI_Type()
)
gs2326MLDSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANLLQI.setStatus("current")


class _Gs2326MLDSnoopingVLANURI_Type(Integer32):
    """Custom type gs2326MLDSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2326MLDSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingVLANURI_Object = MibTableColumn
gs2326MLDSnoopingVLANURI = _Gs2326MLDSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 2, 1, 9),
    _Gs2326MLDSnoopingVLANURI_Type()
)
gs2326MLDSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingVLANURI.setStatus("current")
_Gs2326MLDSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2326MLDSnoopingPortGroupFiltering = _Gs2326MLDSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3)
)
_Gs2326MLDSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2326MLDSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2326MLDSnoopingPortGroupFilteringCreate = _Gs2326MLDSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 1),
    _Gs2326MLDSnoopingPortGroupFilteringCreate_Type()
)
gs2326MLDSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2326MLDSnoopingPortGroupFilteringTable_Object = MibTable
gs2326MLDSnoopingPortGroupFilteringTable = _Gs2326MLDSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2326MLDSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2326MLDSnoopingPortGroupFilteringEntry = _Gs2326MLDSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 2, 1)
)
gs2326MLDSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MLDSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2326MLDSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2326MLDSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MLDSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2326MLDSnoopingPortGroupFilteringIndex = _Gs2326MLDSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 2, 1, 1),
    _Gs2326MLDSnoopingPortGroupFilteringIndex_Type()
)
gs2326MLDSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2326MLDSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2326MLDSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MLDSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2326MLDSnoopingPortGroupFilteringPort = _Gs2326MLDSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 2, 1, 2),
    _Gs2326MLDSnoopingPortGroupFilteringPort_Type()
)
gs2326MLDSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2326MLDSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2326MLDSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2326MLDSnoopingPortGroupFilteringGroups = _Gs2326MLDSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 2, 1, 3),
    _Gs2326MLDSnoopingPortGroupFilteringGroups_Type()
)
gs2326MLDSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2326MLDSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2326MLDSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2326MLDSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2326MLDSnoopingPortGroupFilteringRowStatus = _Gs2326MLDSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 3, 2, 1, 4),
    _Gs2326MLDSnoopingPortGroupFilteringRowStatus_Type()
)
gs2326MLDSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2326MLDSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2326MLDSnoopingStatus = _Gs2326MLDSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4)
)


class _Gs2326MLDSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2326MLDSnoopingstatisticClear based on Integer32"""
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


_Gs2326MLDSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingstatisticClear_Object = MibScalar
gs2326MLDSnoopingstatisticClear = _Gs2326MLDSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 1),
    _Gs2326MLDSnoopingstatisticClear_Type()
)
gs2326MLDSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticClear.setStatus("current")
_Gs2326MLDSnoopingstatisticTable_Object = MibTable
gs2326MLDSnoopingstatisticTable = _Gs2326MLDSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticTable.setStatus("current")
_Gs2326MLDSnoopingstatisticEntry_Object = MibTableRow
gs2326MLDSnoopingstatisticEntry = _Gs2326MLDSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1)
)
gs2326MLDSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MLDSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticEntry.setStatus("current")


class _Gs2326MLDSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2326MLDSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MLDSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingstatisticVLANID_Object = MibTableColumn
gs2326MLDSnoopingstatisticVLANID = _Gs2326MLDSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 1),
    _Gs2326MLDSnoopingstatisticVLANID_Type()
)
gs2326MLDSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticVLANID.setStatus("current")
_Gs2326MLDSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2326MLDSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2326MLDSnoopingstatisticQuerierVersion = _Gs2326MLDSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 2),
    _Gs2326MLDSnoopingstatisticQuerierVersion_Type()
)
gs2326MLDSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2326MLDSnoopingstatisticHostVersion_Type = DisplayString
_Gs2326MLDSnoopingstatisticHostVersion_Object = MibTableColumn
gs2326MLDSnoopingstatisticHostVersion = _Gs2326MLDSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 3),
    _Gs2326MLDSnoopingstatisticHostVersion_Type()
)
gs2326MLDSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticHostVersion.setStatus("current")
_Gs2326MLDSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2326MLDSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2326MLDSnoopingstatisticQuerierStatus = _Gs2326MLDSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 4),
    _Gs2326MLDSnoopingstatisticQuerierStatus_Type()
)
gs2326MLDSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2326MLDSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2326MLDSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2326MLDSnoopingstatisticQueriesTransmitted = _Gs2326MLDSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 5),
    _Gs2326MLDSnoopingstatisticQueriesTransmitted_Type()
)
gs2326MLDSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2326MLDSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2326MLDSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2326MLDSnoopingstatisticQueriesReceived = _Gs2326MLDSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 6),
    _Gs2326MLDSnoopingstatisticQueriesReceived_Type()
)
gs2326MLDSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2326MLDSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2326MLDSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2326MLDSnoopingstatisticV1ReportsReceived = _Gs2326MLDSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 7),
    _Gs2326MLDSnoopingstatisticV1ReportsReceived_Type()
)
gs2326MLDSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2326MLDSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2326MLDSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2326MLDSnoopingstatisticV2ReportsReceived = _Gs2326MLDSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 8),
    _Gs2326MLDSnoopingstatisticV2ReportsReceived_Type()
)
gs2326MLDSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2326MLDSnoopingstatisticV1LeavesReceived_Type = Counter32
_Gs2326MLDSnoopingstatisticV1LeavesReceived_Object = MibTableColumn
gs2326MLDSnoopingstatisticV1LeavesReceived = _Gs2326MLDSnoopingstatisticV1LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 2, 1, 9),
    _Gs2326MLDSnoopingstatisticV1LeavesReceived_Type()
)
gs2326MLDSnoopingstatisticV1LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingstatisticV1LeavesReceived.setStatus("current")
_Gs2326MLDSnoopingRouterPortTable_Object = MibTable
gs2326MLDSnoopingRouterPortTable = _Gs2326MLDSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 3)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingRouterPortTable.setStatus("current")
_Gs2326MLDSnoopingRouterPortEntry_Object = MibTableRow
gs2326MLDSnoopingRouterPortEntry = _Gs2326MLDSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 3, 1)
)
gs2326MLDSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingRouterPortEntry.setStatus("current")
_Gs2326MLDSnoopingRouterPortStatus_Type = DisplayString
_Gs2326MLDSnoopingRouterPortStatus_Object = MibTableColumn
gs2326MLDSnoopingRouterPortStatus = _Gs2326MLDSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 4, 3, 1, 1),
    _Gs2326MLDSnoopingRouterPortStatus_Type()
)
gs2326MLDSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingRouterPortStatus.setStatus("current")
_Gs2326MLDSnoopingGroupsTable_Object = MibTable
gs2326MLDSnoopingGroupsTable = _Gs2326MLDSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 5)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingGroupsTable.setStatus("current")
_Gs2326MLDSnoopingGroupsEntry_Object = MibTableRow
gs2326MLDSnoopingGroupsEntry = _Gs2326MLDSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 5, 1)
)
gs2326MLDSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MLDSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingGroupsEntry.setStatus("current")


class _Gs2326MLDSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2326MLDSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MLDSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingGroupsIndex_Object = MibTableColumn
gs2326MLDSnoopingGroupsIndex = _Gs2326MLDSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 5, 1, 1),
    _Gs2326MLDSnoopingGroupsIndex_Type()
)
gs2326MLDSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingGroupsIndex.setStatus("current")


class _Gs2326MLDSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2326MLDSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MLDSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingGroupsVLANID_Object = MibTableColumn
gs2326MLDSnoopingGroupsVLANID = _Gs2326MLDSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 5, 1, 2),
    _Gs2326MLDSnoopingGroupsVLANID_Type()
)
gs2326MLDSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingGroupsVLANID.setStatus("current")
_Gs2326MLDSnoopingGroups_Type = DisplayString
_Gs2326MLDSnoopingGroups_Object = MibTableColumn
gs2326MLDSnoopingGroups = _Gs2326MLDSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 5, 1, 3),
    _Gs2326MLDSnoopingGroups_Type()
)
gs2326MLDSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingGroups.setStatus("current")
_Gs2326MLDSnoopingGroupsMemberships_Type = DisplayString
_Gs2326MLDSnoopingGroupsMemberships_Object = MibTableColumn
gs2326MLDSnoopingGroupsMemberships = _Gs2326MLDSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 5, 1, 4),
    _Gs2326MLDSnoopingGroupsMemberships_Type()
)
gs2326MLDSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingGroupsMemberships.setStatus("current")
_Gs2326MLDSnoopingSSMTable_Object = MibTable
gs2326MLDSnoopingSSMTable = _Gs2326MLDSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6)
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMTable.setStatus("current")
_Gs2326MLDSnoopingSSMEntry_Object = MibTableRow
gs2326MLDSnoopingSSMEntry = _Gs2326MLDSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1)
)
gs2326MLDSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MLDSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMEntry.setStatus("current")


class _Gs2326MLDSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2326MLDSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MLDSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingSSMIndex_Object = MibTableColumn
gs2326MLDSnoopingSSMIndex = _Gs2326MLDSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 1),
    _Gs2326MLDSnoopingSSMIndex_Type()
)
gs2326MLDSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMIndex.setStatus("current")


class _Gs2326MLDSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2326MLDSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MLDSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingSSMVLANID_Object = MibTableColumn
gs2326MLDSnoopingSSMVLANID = _Gs2326MLDSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 2),
    _Gs2326MLDSnoopingSSMVLANID_Type()
)
gs2326MLDSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMVLANID.setStatus("current")
_Gs2326MLDSnoopingSSMGroup_Type = DisplayString
_Gs2326MLDSnoopingSSMGroup_Object = MibTableColumn
gs2326MLDSnoopingSSMGroup = _Gs2326MLDSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 3),
    _Gs2326MLDSnoopingSSMGroup_Type()
)
gs2326MLDSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMGroup.setStatus("current")


class _Gs2326MLDSnoopingSSMPort_Type(Integer32):
    """Custom type gs2326MLDSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MLDSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2326MLDSnoopingSSMPort_Object = MibTableColumn
gs2326MLDSnoopingSSMPort = _Gs2326MLDSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 4),
    _Gs2326MLDSnoopingSSMPort_Type()
)
gs2326MLDSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMPort.setStatus("current")
_Gs2326MLDSnoopingSSMMode_Type = DisplayString
_Gs2326MLDSnoopingSSMMode_Object = MibTableColumn
gs2326MLDSnoopingSSMMode = _Gs2326MLDSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 5),
    _Gs2326MLDSnoopingSSMMode_Type()
)
gs2326MLDSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMMode.setStatus("current")
_Gs2326MLDSnoopingSSMSourceAddress_Type = DisplayString
_Gs2326MLDSnoopingSSMSourceAddress_Object = MibTableColumn
gs2326MLDSnoopingSSMSourceAddress = _Gs2326MLDSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 6),
    _Gs2326MLDSnoopingSSMSourceAddress_Type()
)
gs2326MLDSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMSourceAddress.setStatus("current")
_Gs2326MLDSnoopingSSMType_Type = DisplayString
_Gs2326MLDSnoopingSSMType_Object = MibTableColumn
gs2326MLDSnoopingSSMType = _Gs2326MLDSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 17, 6, 1, 7),
    _Gs2326MLDSnoopingSSMType_Type()
)
gs2326MLDSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MLDSnoopingSSMType.setStatus("current")
_Gs2326MVR_ObjectIdentity = ObjectIdentity
gs2326MVR = _Gs2326MVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18)
)
_Gs2326MVRConfiguration_ObjectIdentity = ObjectIdentity
gs2326MVRConfiguration = _Gs2326MVRConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1)
)


class _Gs2326MVRMode_Type(Integer32):
    """Custom type gs2326MVRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MVRMode_Type.__name__ = "Integer32"
_Gs2326MVRMode_Object = MibScalar
gs2326MVRMode = _Gs2326MVRMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 1),
    _Gs2326MVRMode_Type()
)
gs2326MVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRMode.setStatus("current")


class _Gs2326MVRVLANId_Type(Integer32):
    """Custom type gs2326MVRVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326MVRVLANId_Type.__name__ = "Integer32"
_Gs2326MVRVLANId_Object = MibScalar
gs2326MVRVLANId = _Gs2326MVRVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 2),
    _Gs2326MVRVLANId_Type()
)
gs2326MVRVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRVLANId.setStatus("current")
_Gs2326MVRPortConfigurationTable_Object = MibTable
gs2326MVRPortConfigurationTable = _Gs2326MVRPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 3)
)
if mibBuilder.loadTexts:
    gs2326MVRPortConfigurationTable.setStatus("current")
_Gs2326MVRPortConfigurationEntry_Object = MibTableRow
gs2326MVRPortConfigurationEntry = _Gs2326MVRPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 3, 1)
)
gs2326MVRPortConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2326MVRPortConfigurationEntry.setStatus("current")


class _Gs2326MVRPortConfigurationMode_Type(Integer32):
    """Custom type gs2326MVRPortConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MVRPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2326MVRPortConfigurationMode_Object = MibTableColumn
gs2326MVRPortConfigurationMode = _Gs2326MVRPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 3, 1, 1),
    _Gs2326MVRPortConfigurationMode_Type()
)
gs2326MVRPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortConfigurationMode.setStatus("current")


class _Gs2326MVRPortConfigurationType_Type(Integer32):
    """Custom type gs2326MVRPortConfigurationType based on Integer32"""
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


_Gs2326MVRPortConfigurationType_Type.__name__ = "Integer32"
_Gs2326MVRPortConfigurationType_Object = MibTableColumn
gs2326MVRPortConfigurationType = _Gs2326MVRPortConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 3, 1, 2),
    _Gs2326MVRPortConfigurationType_Type()
)
gs2326MVRPortConfigurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortConfigurationType.setStatus("current")


class _Gs2326MVRPortConfigurationImmediateLeave_Type(Integer32):
    """Custom type gs2326MVRPortConfigurationImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326MVRPortConfigurationImmediateLeave_Type.__name__ = "Integer32"
_Gs2326MVRPortConfigurationImmediateLeave_Object = MibTableColumn
gs2326MVRPortConfigurationImmediateLeave = _Gs2326MVRPortConfigurationImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 1, 3, 1, 3),
    _Gs2326MVRPortConfigurationImmediateLeave_Type()
)
gs2326MVRPortConfigurationImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortConfigurationImmediateLeave.setStatus("current")
_Gs2326MVRPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2326MVRPortGroupFiltering = _Gs2326MVRPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2)
)
_Gs2326MVRPortGroupFilteringCreate_Type = Integer32
_Gs2326MVRPortGroupFilteringCreate_Object = MibScalar
gs2326MVRPortGroupFilteringCreate = _Gs2326MVRPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 1),
    _Gs2326MVRPortGroupFilteringCreate_Type()
)
gs2326MVRPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringCreate.setStatus("current")
_Gs2326MVRPortGroupFilteringTable_Object = MibTable
gs2326MVRPortGroupFilteringTable = _Gs2326MVRPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringTable.setStatus("current")
_Gs2326MVRPortGroupFilteringEntry_Object = MibTableRow
gs2326MVRPortGroupFilteringEntry = _Gs2326MVRPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2, 1)
)
gs2326MVRPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MVRPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringEntry.setStatus("current")


class _Gs2326MVRPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2326MVRPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MVRPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2326MVRPortGroupFilteringIndex_Object = MibTableColumn
gs2326MVRPortGroupFilteringIndex = _Gs2326MVRPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2, 1, 1),
    _Gs2326MVRPortGroupFilteringIndex_Type()
)
gs2326MVRPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringIndex.setStatus("current")


class _Gs2326MVRPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2326MVRPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MVRPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2326MVRPortGroupFilteringPort_Object = MibTableColumn
gs2326MVRPortGroupFilteringPort = _Gs2326MVRPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2, 1, 2),
    _Gs2326MVRPortGroupFilteringPort_Type()
)
gs2326MVRPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringPort.setStatus("current")
_Gs2326MVRPortGroupFilteringStartGroups_Type = DisplayString
_Gs2326MVRPortGroupFilteringStartGroups_Object = MibTableColumn
gs2326MVRPortGroupFilteringStartGroups = _Gs2326MVRPortGroupFilteringStartGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2, 1, 3),
    _Gs2326MVRPortGroupFilteringStartGroups_Type()
)
gs2326MVRPortGroupFilteringStartGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringStartGroups.setStatus("current")
_Gs2326MVRPortGroupFilteringEndGroups_Type = DisplayString
_Gs2326MVRPortGroupFilteringEndGroups_Object = MibTableColumn
gs2326MVRPortGroupFilteringEndGroups = _Gs2326MVRPortGroupFilteringEndGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2, 1, 4),
    _Gs2326MVRPortGroupFilteringEndGroups_Type()
)
gs2326MVRPortGroupFilteringEndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringEndGroups.setStatus("current")


class _Gs2326MVRPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2326MVRPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2326MVRPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2326MVRPortGroupFilteringRowStatus_Object = MibTableColumn
gs2326MVRPortGroupFilteringRowStatus = _Gs2326MVRPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 2, 2, 1, 5),
    _Gs2326MVRPortGroupFilteringRowStatus_Type()
)
gs2326MVRPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRPortGroupFilteringRowStatus.setStatus("current")
_Gs2326MVRGroupsTable_Object = MibTable
gs2326MVRGroupsTable = _Gs2326MVRGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gs2326MVRGroupsTable.setStatus("current")
_Gs2326MVRGroupsEntry_Object = MibTableRow
gs2326MVRGroupsEntry = _Gs2326MVRGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 3, 1)
)
gs2326MVRGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MVRGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2326MVRGroupsEntry.setStatus("current")


class _Gs2326MVRGroupsIndex_Type(Integer32):
    """Custom type gs2326MVRGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326MVRGroupsIndex_Type.__name__ = "Integer32"
_Gs2326MVRGroupsIndex_Object = MibTableColumn
gs2326MVRGroupsIndex = _Gs2326MVRGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 3, 1, 1),
    _Gs2326MVRGroupsIndex_Type()
)
gs2326MVRGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MVRGroupsIndex.setStatus("current")


class _Gs2326MVRGroupsVLANID_Type(Integer32):
    """Custom type gs2326MVRGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MVRGroupsVLANID_Type.__name__ = "Integer32"
_Gs2326MVRGroupsVLANID_Object = MibTableColumn
gs2326MVRGroupsVLANID = _Gs2326MVRGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 3, 1, 2),
    _Gs2326MVRGroupsVLANID_Type()
)
gs2326MVRGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRGroupsVLANID.setStatus("current")
_Gs2326MVRGroups_Type = DisplayString
_Gs2326MVRGroups_Object = MibTableColumn
gs2326MVRGroups = _Gs2326MVRGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 3, 1, 3),
    _Gs2326MVRGroups_Type()
)
gs2326MVRGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRGroups.setStatus("current")
_Gs2326MVRGroupsMemberships_Type = DisplayString
_Gs2326MVRGroupsMemberships_Object = MibTableColumn
gs2326MVRGroupsMemberships = _Gs2326MVRGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 3, 1, 4),
    _Gs2326MVRGroupsMemberships_Type()
)
gs2326MVRGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRGroupsMemberships.setStatus("current")
_Gs2326MVRStatus_ObjectIdentity = ObjectIdentity
gs2326MVRStatus = _Gs2326MVRStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4)
)


class _Gs2326MVRstatisticClear_Type(Integer32):
    """Custom type gs2326MVRstatisticClear based on Integer32"""
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


_Gs2326MVRstatisticClear_Type.__name__ = "Integer32"
_Gs2326MVRstatisticClear_Object = MibScalar
gs2326MVRstatisticClear = _Gs2326MVRstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4, 1),
    _Gs2326MVRstatisticClear_Type()
)
gs2326MVRstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326MVRstatisticClear.setStatus("current")


class _Gs2326MVRstatisticVLANID_Type(Integer32):
    """Custom type gs2326MVRstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MVRstatisticVLANID_Type.__name__ = "Integer32"
_Gs2326MVRstatisticVLANID_Object = MibScalar
gs2326MVRstatisticVLANID = _Gs2326MVRstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4, 2),
    _Gs2326MVRstatisticVLANID_Type()
)
gs2326MVRstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRstatisticVLANID.setStatus("current")
_Gs2326MVRstatisticV1ReportsReceived_Type = Counter32
_Gs2326MVRstatisticV1ReportsReceived_Object = MibScalar
gs2326MVRstatisticV1ReportsReceived = _Gs2326MVRstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4, 3),
    _Gs2326MVRstatisticV1ReportsReceived_Type()
)
gs2326MVRstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRstatisticV1ReportsReceived.setStatus("current")
_Gs2326MVRstatisticV2ReportsReceived_Type = Counter32
_Gs2326MVRstatisticV2ReportsReceived_Object = MibScalar
gs2326MVRstatisticV2ReportsReceived = _Gs2326MVRstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4, 4),
    _Gs2326MVRstatisticV2ReportsReceived_Type()
)
gs2326MVRstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRstatisticV2ReportsReceived.setStatus("current")
_Gs2326MVRstatisticV3ReportsReceived_Type = Counter32
_Gs2326MVRstatisticV3ReportsReceived_Object = MibScalar
gs2326MVRstatisticV3ReportsReceived = _Gs2326MVRstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4, 5),
    _Gs2326MVRstatisticV3ReportsReceived_Type()
)
gs2326MVRstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRstatisticV3ReportsReceived.setStatus("current")
_Gs2326MVRstatisticV2LeavesReceived_Type = Counter32
_Gs2326MVRstatisticV2LeavesReceived_Object = MibScalar
gs2326MVRstatisticV2LeavesReceived = _Gs2326MVRstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 18, 4, 6),
    _Gs2326MVRstatisticV2LeavesReceived_Type()
)
gs2326MVRstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MVRstatisticV2LeavesReceived.setStatus("current")
_Gs2326LACP_ObjectIdentity = ObjectIdentity
gs2326LACP = _Gs2326LACP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19)
)
_Gs2326LACPConf_ObjectIdentity = ObjectIdentity
gs2326LACPConf = _Gs2326LACPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1)
)
_Gs2326LACPPortConfigurationTable_Object = MibTable
gs2326LACPPortConfigurationTable = _Gs2326LACPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    gs2326LACPPortConfigurationTable.setStatus("current")
_Gs2326LACPPortConfigurationEntry_Object = MibTableRow
gs2326LACPPortConfigurationEntry = _Gs2326LACPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1, 1, 1)
)
gs2326LACPPortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326LACPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2326LACPPortConfigurationEntry.setStatus("current")


class _Gs2326LACPPortConfigurationPort_Type(Integer32):
    """Custom type gs2326LACPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326LACPPortConfigurationPort_Type.__name__ = "Integer32"
_Gs2326LACPPortConfigurationPort_Object = MibTableColumn
gs2326LACPPortConfigurationPort = _Gs2326LACPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1, 1, 1, 1),
    _Gs2326LACPPortConfigurationPort_Type()
)
gs2326LACPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326LACPPortConfigurationPort.setStatus("current")


class _Gs2326LACPPortConfigurationMode_Type(Integer32):
    """Custom type gs2326LACPPortConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326LACPPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2326LACPPortConfigurationMode_Object = MibTableColumn
gs2326LACPPortConfigurationMode = _Gs2326LACPPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1, 1, 1, 2),
    _Gs2326LACPPortConfigurationMode_Type()
)
gs2326LACPPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LACPPortConfigurationMode.setStatus("current")


class _Gs2326LACPPortConfigurationKey_Type(Integer32):
    """Custom type gs2326LACPPortConfigurationKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2326LACPPortConfigurationKey_Type.__name__ = "Integer32"
_Gs2326LACPPortConfigurationKey_Object = MibTableColumn
gs2326LACPPortConfigurationKey = _Gs2326LACPPortConfigurationKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1, 1, 1, 3),
    _Gs2326LACPPortConfigurationKey_Type()
)
gs2326LACPPortConfigurationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LACPPortConfigurationKey.setStatus("current")


class _Gs2326LACPPortConfigurationRole_Type(Integer32):
    """Custom type gs2326LACPPortConfigurationRole based on Integer32"""
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


_Gs2326LACPPortConfigurationRole_Type.__name__ = "Integer32"
_Gs2326LACPPortConfigurationRole_Object = MibTableColumn
gs2326LACPPortConfigurationRole = _Gs2326LACPPortConfigurationRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 1, 1, 1, 4),
    _Gs2326LACPPortConfigurationRole_Type()
)
gs2326LACPPortConfigurationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LACPPortConfigurationRole.setStatus("current")
_Gs2326LACPSystemStatusTable_Object = MibTable
gs2326LACPSystemStatusTable = _Gs2326LACPSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusTable.setStatus("current")
_Gs2326LACPSystemStatusEntry_Object = MibTableRow
gs2326LACPSystemStatusEntry = _Gs2326LACPSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1)
)
gs2326LACPSystemStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326LACPSystemStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusEntry.setStatus("current")


class _Gs2326LACPSystemStatusIndex_Type(Integer32):
    """Custom type gs2326LACPSystemStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2326LACPSystemStatusIndex_Type.__name__ = "Integer32"
_Gs2326LACPSystemStatusIndex_Object = MibTableColumn
gs2326LACPSystemStatusIndex = _Gs2326LACPSystemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1, 1),
    _Gs2326LACPSystemStatusIndex_Type()
)
gs2326LACPSystemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusIndex.setStatus("current")
_Gs2326LACPSystemStatusAggrID_Type = DisplayString
_Gs2326LACPSystemStatusAggrID_Object = MibTableColumn
gs2326LACPSystemStatusAggrID = _Gs2326LACPSystemStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1, 2),
    _Gs2326LACPSystemStatusAggrID_Type()
)
gs2326LACPSystemStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusAggrID.setStatus("current")
_Gs2326LACPSystemStatusPartnerSystemID_Type = MacAddress
_Gs2326LACPSystemStatusPartnerSystemID_Object = MibTableColumn
gs2326LACPSystemStatusPartnerSystemID = _Gs2326LACPSystemStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1, 3),
    _Gs2326LACPSystemStatusPartnerSystemID_Type()
)
gs2326LACPSystemStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusPartnerSystemID.setStatus("current")
_Gs2326LACPSystemStatusPartnerKey_Type = DisplayString
_Gs2326LACPSystemStatusPartnerKey_Object = MibTableColumn
gs2326LACPSystemStatusPartnerKey = _Gs2326LACPSystemStatusPartnerKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1, 4),
    _Gs2326LACPSystemStatusPartnerKey_Type()
)
gs2326LACPSystemStatusPartnerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusPartnerKey.setStatus("current")
_Gs2326LACPSystemStatusLastchanged_Type = DisplayString
_Gs2326LACPSystemStatusLastchanged_Object = MibTableColumn
gs2326LACPSystemStatusLastchanged = _Gs2326LACPSystemStatusLastchanged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1, 5),
    _Gs2326LACPSystemStatusLastchanged_Type()
)
gs2326LACPSystemStatusLastchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusLastchanged.setStatus("current")
_Gs2326LACPSystemStatusLocalPorts_Type = DisplayString
_Gs2326LACPSystemStatusLocalPorts_Object = MibTableColumn
gs2326LACPSystemStatusLocalPorts = _Gs2326LACPSystemStatusLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 2, 1, 6),
    _Gs2326LACPSystemStatusLocalPorts_Type()
)
gs2326LACPSystemStatusLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPSystemStatusLocalPorts.setStatus("current")
_Gs2326LACPStatusTable_Object = MibTable
gs2326LACPStatusTable = _Gs2326LACPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gs2326LACPStatusTable.setStatus("current")
_Gs2326LACPStatusEntry_Object = MibTableRow
gs2326LACPStatusEntry = _Gs2326LACPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1)
)
gs2326LACPStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326LACPStatusPort"),
)
if mibBuilder.loadTexts:
    gs2326LACPStatusEntry.setStatus("current")


class _Gs2326LACPStatusPort_Type(Integer32):
    """Custom type gs2326LACPStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326LACPStatusPort_Type.__name__ = "Integer32"
_Gs2326LACPStatusPort_Object = MibTableColumn
gs2326LACPStatusPort = _Gs2326LACPStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1, 1),
    _Gs2326LACPStatusPort_Type()
)
gs2326LACPStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326LACPStatusPort.setStatus("current")
_Gs2326LACPStatusLACP_Type = DisplayString
_Gs2326LACPStatusLACP_Object = MibTableColumn
gs2326LACPStatusLACP = _Gs2326LACPStatusLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1, 2),
    _Gs2326LACPStatusLACP_Type()
)
gs2326LACPStatusLACP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPStatusLACP.setStatus("current")
_Gs2326LACPStatusKey_Type = DisplayString
_Gs2326LACPStatusKey_Object = MibTableColumn
gs2326LACPStatusKey = _Gs2326LACPStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1, 3),
    _Gs2326LACPStatusKey_Type()
)
gs2326LACPStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPStatusKey.setStatus("current")
_Gs2326LACPStatusAggrID_Type = DisplayString
_Gs2326LACPStatusAggrID_Object = MibTableColumn
gs2326LACPStatusAggrID = _Gs2326LACPStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1, 4),
    _Gs2326LACPStatusAggrID_Type()
)
gs2326LACPStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPStatusAggrID.setStatus("current")
_Gs2326LACPStatusPartnerSystemID_Type = DisplayString
_Gs2326LACPStatusPartnerSystemID_Object = MibTableColumn
gs2326LACPStatusPartnerSystemID = _Gs2326LACPStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1, 5),
    _Gs2326LACPStatusPartnerSystemID_Type()
)
gs2326LACPStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPStatusPartnerSystemID.setStatus("current")
_Gs2326LACPStatusPartnerPort_Type = DisplayString
_Gs2326LACPStatusPartnerPort_Object = MibTableColumn
gs2326LACPStatusPartnerPort = _Gs2326LACPStatusPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 3, 1, 6),
    _Gs2326LACPStatusPartnerPort_Type()
)
gs2326LACPStatusPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPStatusPartnerPort.setStatus("current")
_Gs2326LACPStatisticsTable_Object = MibTable
gs2326LACPStatisticsTable = _Gs2326LACPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4)
)
if mibBuilder.loadTexts:
    gs2326LACPStatisticsTable.setStatus("current")
_Gs2326LACPStatisticsEntry_Object = MibTableRow
gs2326LACPStatisticsEntry = _Gs2326LACPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4, 1)
)
gs2326LACPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326LACPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2326LACPStatisticsEntry.setStatus("current")


class _Gs2326LACPStatisticsPort_Type(Integer32):
    """Custom type gs2326LACPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326LACPStatisticsPort_Type.__name__ = "Integer32"
_Gs2326LACPStatisticsPort_Object = MibTableColumn
gs2326LACPStatisticsPort = _Gs2326LACPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4, 1, 1),
    _Gs2326LACPStatisticsPort_Type()
)
gs2326LACPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326LACPStatisticsPort.setStatus("current")
_Gs2326LACPReceived_Type = Counter32
_Gs2326LACPReceived_Object = MibTableColumn
gs2326LACPReceived = _Gs2326LACPReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4, 1, 2),
    _Gs2326LACPReceived_Type()
)
gs2326LACPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPReceived.setStatus("current")
_Gs2326LACPTransmitted_Type = Counter32
_Gs2326LACPTransmitted_Object = MibTableColumn
gs2326LACPTransmitted = _Gs2326LACPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4, 1, 3),
    _Gs2326LACPTransmitted_Type()
)
gs2326LACPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPTransmitted.setStatus("current")
_Gs2326LACPDiscardedUnknown_Type = Counter32
_Gs2326LACPDiscardedUnknown_Object = MibTableColumn
gs2326LACPDiscardedUnknown = _Gs2326LACPDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4, 1, 4),
    _Gs2326LACPDiscardedUnknown_Type()
)
gs2326LACPDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPDiscardedUnknown.setStatus("current")
_Gs2326LACPDiscardedIllegal_Type = Counter32
_Gs2326LACPDiscardedIllegal_Object = MibTableColumn
gs2326LACPDiscardedIllegal = _Gs2326LACPDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 4, 1, 5),
    _Gs2326LACPDiscardedIllegal_Type()
)
gs2326LACPDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LACPDiscardedIllegal.setStatus("current")


class _Gs2326LACPStatisticsClear_Type(Integer32):
    """Custom type gs2326LACPStatisticsClear based on Integer32"""
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


_Gs2326LACPStatisticsClear_Type.__name__ = "Integer32"
_Gs2326LACPStatisticsClear_Object = MibScalar
gs2326LACPStatisticsClear = _Gs2326LACPStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 19, 5),
    _Gs2326LACPStatisticsClear_Type()
)
gs2326LACPStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LACPStatisticsClear.setStatus("current")
_Gs2326STP_ObjectIdentity = ObjectIdentity
gs2326STP = _Gs2326STP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20)
)
_Gs2326STPBridgeBasicConf_ObjectIdentity = ObjectIdentity
gs2326STPBridgeBasicConf = _Gs2326STPBridgeBasicConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1)
)


class _Gs2326STPBridgeProtocolVersion_Type(Integer32):
    """Custom type gs2326STPBridgeProtocolVersion based on Integer32"""
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


_Gs2326STPBridgeProtocolVersion_Type.__name__ = "Integer32"
_Gs2326STPBridgeProtocolVersion_Object = MibScalar
gs2326STPBridgeProtocolVersion = _Gs2326STPBridgeProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1, 1),
    _Gs2326STPBridgeProtocolVersion_Type()
)
gs2326STPBridgeProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeProtocolVersion.setStatus("current")


class _Gs2326STPBridgePriority_Type(Integer32):
    """Custom type gs2326STPBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPBridgePriority_Type.__name__ = "Integer32"
_Gs2326STPBridgePriority_Object = MibScalar
gs2326STPBridgePriority = _Gs2326STPBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1, 2),
    _Gs2326STPBridgePriority_Type()
)
gs2326STPBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgePriority.setStatus("current")


class _Gs2326STPBridgeForwardDelay_Type(Integer32):
    """Custom type gs2326STPBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Gs2326STPBridgeForwardDelay_Type.__name__ = "Integer32"
_Gs2326STPBridgeForwardDelay_Object = MibScalar
gs2326STPBridgeForwardDelay = _Gs2326STPBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1, 3),
    _Gs2326STPBridgeForwardDelay_Type()
)
gs2326STPBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeForwardDelay.setStatus("current")


class _Gs2326STPBridgeMaxAge_Type(Integer32):
    """Custom type gs2326STPBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2326STPBridgeMaxAge_Type.__name__ = "Integer32"
_Gs2326STPBridgeMaxAge_Object = MibScalar
gs2326STPBridgeMaxAge = _Gs2326STPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1, 4),
    _Gs2326STPBridgeMaxAge_Type()
)
gs2326STPBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeMaxAge.setStatus("current")


class _Gs2326STPBridgeMaximumHopCount_Type(Integer32):
    """Custom type gs2326STPBridgeMaximumHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2326STPBridgeMaximumHopCount_Type.__name__ = "Integer32"
_Gs2326STPBridgeMaximumHopCount_Object = MibScalar
gs2326STPBridgeMaximumHopCount = _Gs2326STPBridgeMaximumHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1, 5),
    _Gs2326STPBridgeMaximumHopCount_Type()
)
gs2326STPBridgeMaximumHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeMaximumHopCount.setStatus("current")


class _Gs2326STPBridgeTransmitHoldCount_Type(Integer32):
    """Custom type gs2326STPBridgeTransmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2326STPBridgeTransmitHoldCount_Type.__name__ = "Integer32"
_Gs2326STPBridgeTransmitHoldCount_Object = MibScalar
gs2326STPBridgeTransmitHoldCount = _Gs2326STPBridgeTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 1, 6),
    _Gs2326STPBridgeTransmitHoldCount_Type()
)
gs2326STPBridgeTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeTransmitHoldCount.setStatus("current")
_Gs2326STPBridgeAdvancedConf_ObjectIdentity = ObjectIdentity
gs2326STPBridgeAdvancedConf = _Gs2326STPBridgeAdvancedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 2)
)


class _Gs2326STPBridgeEdgePortBPDUFiltering_Type(Integer32):
    """Custom type gs2326STPBridgeEdgePortBPDUFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPBridgeEdgePortBPDUFiltering_Type.__name__ = "Integer32"
_Gs2326STPBridgeEdgePortBPDUFiltering_Object = MibScalar
gs2326STPBridgeEdgePortBPDUFiltering = _Gs2326STPBridgeEdgePortBPDUFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 2, 1),
    _Gs2326STPBridgeEdgePortBPDUFiltering_Type()
)
gs2326STPBridgeEdgePortBPDUFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeEdgePortBPDUFiltering.setStatus("current")


class _Gs2326STPBridgeEdgePortBPDUGuard_Type(Integer32):
    """Custom type gs2326STPBridgeEdgePortBPDUGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPBridgeEdgePortBPDUGuard_Type.__name__ = "Integer32"
_Gs2326STPBridgeEdgePortBPDUGuard_Object = MibScalar
gs2326STPBridgeEdgePortBPDUGuard = _Gs2326STPBridgeEdgePortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 2, 2),
    _Gs2326STPBridgeEdgePortBPDUGuard_Type()
)
gs2326STPBridgeEdgePortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgeEdgePortBPDUGuard.setStatus("current")


class _Gs2326STPBridgePortErrorRecoveryTimeout_Type(Integer32):
    """Custom type gs2326STPBridgePortErrorRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Gs2326STPBridgePortErrorRecoveryTimeout_Type.__name__ = "Integer32"
_Gs2326STPBridgePortErrorRecoveryTimeout_Object = MibScalar
gs2326STPBridgePortErrorRecoveryTimeout = _Gs2326STPBridgePortErrorRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 2, 3),
    _Gs2326STPBridgePortErrorRecoveryTimeout_Type()
)
gs2326STPBridgePortErrorRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPBridgePortErrorRecoveryTimeout.setStatus("current")
_Gs2326STPMSTIConf_ObjectIdentity = ObjectIdentity
gs2326STPMSTIConf = _Gs2326STPMSTIConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 3)
)


class _Gs2326STPMSTIConfigurationName_Type(DisplayString):
    """Custom type gs2326STPMSTIConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2326STPMSTIConfigurationName_Type.__name__ = "DisplayString"
_Gs2326STPMSTIConfigurationName_Object = MibScalar
gs2326STPMSTIConfigurationName = _Gs2326STPMSTIConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 3, 1),
    _Gs2326STPMSTIConfigurationName_Type()
)
gs2326STPMSTIConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTIConfigurationName.setStatus("current")


class _Gs2326STPMSTIConfigurationRevision_Type(Integer32):
    """Custom type gs2326STPMSTIConfigurationRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2326STPMSTIConfigurationRevision_Type.__name__ = "Integer32"
_Gs2326STPMSTIConfigurationRevision_Object = MibScalar
gs2326STPMSTIConfigurationRevision = _Gs2326STPMSTIConfigurationRevision_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 3, 2),
    _Gs2326STPMSTIConfigurationRevision_Type()
)
gs2326STPMSTIConfigurationRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTIConfigurationRevision.setStatus("current")
_Gs2326STPMSTIMappingConf_ObjectIdentity = ObjectIdentity
gs2326STPMSTIMappingConf = _Gs2326STPMSTIMappingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4)
)


class _Gs2326STPMSTI1VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI1VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI1VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI1VLANsMapped_Object = MibScalar
gs2326STPMSTI1VLANsMapped = _Gs2326STPMSTI1VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 1),
    _Gs2326STPMSTI1VLANsMapped_Type()
)
gs2326STPMSTI1VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI1VLANsMapped.setStatus("current")


class _Gs2326STPMSTI2VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI2VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI2VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI2VLANsMapped_Object = MibScalar
gs2326STPMSTI2VLANsMapped = _Gs2326STPMSTI2VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 2),
    _Gs2326STPMSTI2VLANsMapped_Type()
)
gs2326STPMSTI2VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI2VLANsMapped.setStatus("current")


class _Gs2326STPMSTI3VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI3VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI3VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI3VLANsMapped_Object = MibScalar
gs2326STPMSTI3VLANsMapped = _Gs2326STPMSTI3VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 3),
    _Gs2326STPMSTI3VLANsMapped_Type()
)
gs2326STPMSTI3VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI3VLANsMapped.setStatus("current")


class _Gs2326STPMSTI4VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI4VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI4VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI4VLANsMapped_Object = MibScalar
gs2326STPMSTI4VLANsMapped = _Gs2326STPMSTI4VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 4),
    _Gs2326STPMSTI4VLANsMapped_Type()
)
gs2326STPMSTI4VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI4VLANsMapped.setStatus("current")


class _Gs2326STPMSTI5VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI5VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI5VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI5VLANsMapped_Object = MibScalar
gs2326STPMSTI5VLANsMapped = _Gs2326STPMSTI5VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 5),
    _Gs2326STPMSTI5VLANsMapped_Type()
)
gs2326STPMSTI5VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI5VLANsMapped.setStatus("current")


class _Gs2326STPMSTI6VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI6VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI6VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI6VLANsMapped_Object = MibScalar
gs2326STPMSTI6VLANsMapped = _Gs2326STPMSTI6VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 6),
    _Gs2326STPMSTI6VLANsMapped_Type()
)
gs2326STPMSTI6VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI6VLANsMapped.setStatus("current")


class _Gs2326STPMSTI7VLANsMapped_Type(DisplayString):
    """Custom type gs2326STPMSTI7VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2326STPMSTI7VLANsMapped_Type.__name__ = "DisplayString"
_Gs2326STPMSTI7VLANsMapped_Object = MibScalar
gs2326STPMSTI7VLANsMapped = _Gs2326STPMSTI7VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 4, 7),
    _Gs2326STPMSTI7VLANsMapped_Type()
)
gs2326STPMSTI7VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI7VLANsMapped.setStatus("current")
_Gs2326STPMSTIPriority_ObjectIdentity = ObjectIdentity
gs2326STPMSTIPriority = _Gs2326STPMSTIPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5)
)


class _Gs2326STPCISTPriority_Type(Integer32):
    """Custom type gs2326STPCISTPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPCISTPriority_Type.__name__ = "Integer32"
_Gs2326STPCISTPriority_Object = MibScalar
gs2326STPCISTPriority = _Gs2326STPCISTPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 1),
    _Gs2326STPCISTPriority_Type()
)
gs2326STPCISTPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTPriority.setStatus("current")


class _Gs2326STPMSTI1Priority_Type(Integer32):
    """Custom type gs2326STPMSTI1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI1Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI1Priority_Object = MibScalar
gs2326STPMSTI1Priority = _Gs2326STPMSTI1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 2),
    _Gs2326STPMSTI1Priority_Type()
)
gs2326STPMSTI1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI1Priority.setStatus("current")


class _Gs2326STPMSTI2Priority_Type(Integer32):
    """Custom type gs2326STPMSTI2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI2Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI2Priority_Object = MibScalar
gs2326STPMSTI2Priority = _Gs2326STPMSTI2Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 3),
    _Gs2326STPMSTI2Priority_Type()
)
gs2326STPMSTI2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI2Priority.setStatus("current")


class _Gs2326STPMSTI3Priority_Type(Integer32):
    """Custom type gs2326STPMSTI3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI3Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI3Priority_Object = MibScalar
gs2326STPMSTI3Priority = _Gs2326STPMSTI3Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 4),
    _Gs2326STPMSTI3Priority_Type()
)
gs2326STPMSTI3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI3Priority.setStatus("current")


class _Gs2326STPMSTI4Priority_Type(Integer32):
    """Custom type gs2326STPMSTI4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI4Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI4Priority_Object = MibScalar
gs2326STPMSTI4Priority = _Gs2326STPMSTI4Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 5),
    _Gs2326STPMSTI4Priority_Type()
)
gs2326STPMSTI4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI4Priority.setStatus("current")


class _Gs2326STPMSTI5Priority_Type(Integer32):
    """Custom type gs2326STPMSTI5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI5Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI5Priority_Object = MibScalar
gs2326STPMSTI5Priority = _Gs2326STPMSTI5Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 6),
    _Gs2326STPMSTI5Priority_Type()
)
gs2326STPMSTI5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI5Priority.setStatus("current")


class _Gs2326STPMSTI6Priority_Type(Integer32):
    """Custom type gs2326STPMSTI6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI6Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI6Priority_Object = MibScalar
gs2326STPMSTI6Priority = _Gs2326STPMSTI6Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 7),
    _Gs2326STPMSTI6Priority_Type()
)
gs2326STPMSTI6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI6Priority.setStatus("current")


class _Gs2326STPMSTI7Priority_Type(Integer32):
    """Custom type gs2326STPMSTI7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2326STPMSTI7Priority_Type.__name__ = "Integer32"
_Gs2326STPMSTI7Priority_Object = MibScalar
gs2326STPMSTI7Priority = _Gs2326STPMSTI7Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 5, 8),
    _Gs2326STPMSTI7Priority_Type()
)
gs2326STPMSTI7Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI7Priority.setStatus("current")
_Gs2326STPCISTPort_ObjectIdentity = ObjectIdentity
gs2326STPCISTPort = _Gs2326STPCISTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6)
)
_Gs2326STPCISTAggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPCISTAggregatedPort = _Gs2326STPCISTAggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1)
)


class _Gs2326STPCISTAggregatedPortSTPEnabled_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortSTPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTAggregatedPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortSTPEnabled_Object = MibScalar
gs2326STPCISTAggregatedPortSTPEnabled = _Gs2326STPCISTAggregatedPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 1),
    _Gs2326STPCISTAggregatedPortSTPEnabled_Type()
)
gs2326STPCISTAggregatedPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortSTPEnabled.setStatus("current")


class _Gs2326STPCISTAggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPCISTAggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortPathCost_Object = MibScalar
gs2326STPCISTAggregatedPortPathCost = _Gs2326STPCISTAggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 2),
    _Gs2326STPCISTAggregatedPortPathCost_Type()
)
gs2326STPCISTAggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortPathCost.setStatus("current")


class _Gs2326STPCISTAggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPCISTAggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortPriority_Object = MibScalar
gs2326STPCISTAggregatedPortPriority = _Gs2326STPCISTAggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 3),
    _Gs2326STPCISTAggregatedPortPriority_Type()
)
gs2326STPCISTAggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortPriority.setStatus("current")


class _Gs2326STPCISTAggregatedPortAdminEdge_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortAdminEdge based on Integer32"""
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


_Gs2326STPCISTAggregatedPortAdminEdge_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortAdminEdge_Object = MibScalar
gs2326STPCISTAggregatedPortAdminEdge = _Gs2326STPCISTAggregatedPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 4),
    _Gs2326STPCISTAggregatedPortAdminEdge_Type()
)
gs2326STPCISTAggregatedPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortAdminEdge.setStatus("current")


class _Gs2326STPCISTAggregatedPortAutoEdge_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortAutoEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTAggregatedPortAutoEdge_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortAutoEdge_Object = MibScalar
gs2326STPCISTAggregatedPortAutoEdge = _Gs2326STPCISTAggregatedPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 5),
    _Gs2326STPCISTAggregatedPortAutoEdge_Type()
)
gs2326STPCISTAggregatedPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortAutoEdge.setStatus("current")


class _Gs2326STPCISTAggregatedPortRestrictedRole_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortRestrictedRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTAggregatedPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortRestrictedRole_Object = MibScalar
gs2326STPCISTAggregatedPortRestrictedRole = _Gs2326STPCISTAggregatedPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 6),
    _Gs2326STPCISTAggregatedPortRestrictedRole_Type()
)
gs2326STPCISTAggregatedPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortRestrictedRole.setStatus("current")


class _Gs2326STPCISTAggregatedPortRestrictedTCN_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortRestrictedTCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTAggregatedPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortRestrictedTCN_Object = MibScalar
gs2326STPCISTAggregatedPortRestrictedTCN = _Gs2326STPCISTAggregatedPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 7),
    _Gs2326STPCISTAggregatedPortRestrictedTCN_Type()
)
gs2326STPCISTAggregatedPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortRestrictedTCN.setStatus("current")


class _Gs2326STPCISTAggregatedPortBPDUGuard_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortBPDUGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTAggregatedPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortBPDUGuard_Object = MibScalar
gs2326STPCISTAggregatedPortBPDUGuard = _Gs2326STPCISTAggregatedPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 8),
    _Gs2326STPCISTAggregatedPortBPDUGuard_Type()
)
gs2326STPCISTAggregatedPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortBPDUGuard.setStatus("current")


class _Gs2326STPCISTAggregatedPortPointtoPoint_Type(Integer32):
    """Custom type gs2326STPCISTAggregatedPortPointtoPoint based on Integer32"""
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


_Gs2326STPCISTAggregatedPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2326STPCISTAggregatedPortPointtoPoint_Object = MibScalar
gs2326STPCISTAggregatedPortPointtoPoint = _Gs2326STPCISTAggregatedPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 1, 9),
    _Gs2326STPCISTAggregatedPortPointtoPoint_Type()
)
gs2326STPCISTAggregatedPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTAggregatedPortPointtoPoint.setStatus("current")
_Gs2326STPCISTNormalPortTable_Object = MibTable
gs2326STPCISTNormalPortTable = _Gs2326STPCISTNormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2)
)
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortTable.setStatus("current")
_Gs2326STPCISTNormalPortEntry_Object = MibTableRow
gs2326STPCISTNormalPortEntry = _Gs2326STPCISTNormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1)
)
gs2326STPCISTNormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPCISTNormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortEntry.setStatus("current")


class _Gs2326STPCISTNormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPCISTNormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortConfPort_Object = MibTableColumn
gs2326STPCISTNormalPortConfPort = _Gs2326STPCISTNormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 1),
    _Gs2326STPCISTNormalPortConfPort_Type()
)
gs2326STPCISTNormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortConfPort.setStatus("current")


class _Gs2326STPCISTNormalPortSTPEnabled_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortSTPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTNormalPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortSTPEnabled_Object = MibTableColumn
gs2326STPCISTNormalPortSTPEnabled = _Gs2326STPCISTNormalPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 2),
    _Gs2326STPCISTNormalPortSTPEnabled_Type()
)
gs2326STPCISTNormalPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortSTPEnabled.setStatus("current")


class _Gs2326STPCISTNormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPCISTNormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortPathCost_Object = MibTableColumn
gs2326STPCISTNormalPortPathCost = _Gs2326STPCISTNormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 3),
    _Gs2326STPCISTNormalPortPathCost_Type()
)
gs2326STPCISTNormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortPathCost.setStatus("current")


class _Gs2326STPCISTNormalPortPriority_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPCISTNormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortPriority_Object = MibTableColumn
gs2326STPCISTNormalPortPriority = _Gs2326STPCISTNormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 4),
    _Gs2326STPCISTNormalPortPriority_Type()
)
gs2326STPCISTNormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortPriority.setStatus("current")


class _Gs2326STPCISTNormalPortAdminEdge_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortAdminEdge based on Integer32"""
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


_Gs2326STPCISTNormalPortAdminEdge_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortAdminEdge_Object = MibTableColumn
gs2326STPCISTNormalPortAdminEdge = _Gs2326STPCISTNormalPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 5),
    _Gs2326STPCISTNormalPortAdminEdge_Type()
)
gs2326STPCISTNormalPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortAdminEdge.setStatus("current")


class _Gs2326STPCISTNormalPortAutoEdge_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortAutoEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTNormalPortAutoEdge_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortAutoEdge_Object = MibTableColumn
gs2326STPCISTNormalPortAutoEdge = _Gs2326STPCISTNormalPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 6),
    _Gs2326STPCISTNormalPortAutoEdge_Type()
)
gs2326STPCISTNormalPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortAutoEdge.setStatus("current")


class _Gs2326STPCISTNormalPortRestrictedRole_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortRestrictedRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTNormalPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortRestrictedRole_Object = MibTableColumn
gs2326STPCISTNormalPortRestrictedRole = _Gs2326STPCISTNormalPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 7),
    _Gs2326STPCISTNormalPortRestrictedRole_Type()
)
gs2326STPCISTNormalPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortRestrictedRole.setStatus("current")


class _Gs2326STPCISTNormalPortRestrictedTCN_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortRestrictedTCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTNormalPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortRestrictedTCN_Object = MibTableColumn
gs2326STPCISTNormalPortRestrictedTCN = _Gs2326STPCISTNormalPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 8),
    _Gs2326STPCISTNormalPortRestrictedTCN_Type()
)
gs2326STPCISTNormalPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortRestrictedTCN.setStatus("current")


class _Gs2326STPCISTNormalPortBPDUGuard_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortBPDUGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326STPCISTNormalPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortBPDUGuard_Object = MibTableColumn
gs2326STPCISTNormalPortBPDUGuard = _Gs2326STPCISTNormalPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 9),
    _Gs2326STPCISTNormalPortBPDUGuard_Type()
)
gs2326STPCISTNormalPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortBPDUGuard.setStatus("current")


class _Gs2326STPCISTNormalPortPointtoPoint_Type(Integer32):
    """Custom type gs2326STPCISTNormalPortPointtoPoint based on Integer32"""
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


_Gs2326STPCISTNormalPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2326STPCISTNormalPortPointtoPoint_Object = MibTableColumn
gs2326STPCISTNormalPortPointtoPoint = _Gs2326STPCISTNormalPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 6, 2, 1, 10),
    _Gs2326STPCISTNormalPortPointtoPoint_Type()
)
gs2326STPCISTNormalPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPCISTNormalPortPointtoPoint.setStatus("current")
_Gs2326STPMSTIPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTIPort = _Gs2326STPMSTIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7)
)
_Gs2326STPMSTI1Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI1Port = _Gs2326STPMSTI1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1)
)
_Gs2326STPMSTI1AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI1AggregatedPort = _Gs2326STPMSTI1AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 1)
)


class _Gs2326STPMSTI1AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI1AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI1AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI1AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI1AggregatedPortPathCost = _Gs2326STPMSTI1AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 1, 1),
    _Gs2326STPMSTI1AggregatedPortPathCost_Type()
)
gs2326STPMSTI1AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI1AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI1AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI1AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI1AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI1AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI1AggregatedPortPriority = _Gs2326STPMSTI1AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 1, 2),
    _Gs2326STPMSTI1AggregatedPortPriority_Type()
)
gs2326STPMSTI1AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI1AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI1NormalPortTable_Object = MibTable
gs2326STPMSTI1NormalPortTable = _Gs2326STPMSTI1NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI1NormalPortTable.setStatus("current")
_Gs2326STPMSTI1NormalPortEntry_Object = MibTableRow
gs2326STPMSTI1NormalPortEntry = _Gs2326STPMSTI1NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 2, 1)
)
gs2326STPMSTI1NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI1NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI1NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI1NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI1NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI1NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI1NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI1NormalPortConfPort = _Gs2326STPMSTI1NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 2, 1, 1),
    _Gs2326STPMSTI1NormalPortConfPort_Type()
)
gs2326STPMSTI1NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI1NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI1NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI1NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI1NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI1NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI1NormalPortPathCost = _Gs2326STPMSTI1NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 2, 1, 2),
    _Gs2326STPMSTI1NormalPortPathCost_Type()
)
gs2326STPMSTI1NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI1NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI1NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI1NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI1NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI1NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI1NormalPortPriority = _Gs2326STPMSTI1NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 1, 2, 1, 3),
    _Gs2326STPMSTI1NormalPortPriority_Type()
)
gs2326STPMSTI1NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI1NormalPortPriority.setStatus("current")
_Gs2326STPMSTI2Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI2Port = _Gs2326STPMSTI2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2)
)
_Gs2326STPMSTI2AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI2AggregatedPort = _Gs2326STPMSTI2AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 1)
)


class _Gs2326STPMSTI2AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI2AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI2AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI2AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI2AggregatedPortPathCost = _Gs2326STPMSTI2AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 1, 1),
    _Gs2326STPMSTI2AggregatedPortPathCost_Type()
)
gs2326STPMSTI2AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI2AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI2AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI2AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI2AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI2AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI2AggregatedPortPriority = _Gs2326STPMSTI2AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 1, 2),
    _Gs2326STPMSTI2AggregatedPortPriority_Type()
)
gs2326STPMSTI2AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI2AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI2NormalPortTable_Object = MibTable
gs2326STPMSTI2NormalPortTable = _Gs2326STPMSTI2NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI2NormalPortTable.setStatus("current")
_Gs2326STPMSTI2NormalPortEntry_Object = MibTableRow
gs2326STPMSTI2NormalPortEntry = _Gs2326STPMSTI2NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 2, 1)
)
gs2326STPMSTI2NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI2NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI2NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI2NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI2NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI2NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI2NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI2NormalPortConfPort = _Gs2326STPMSTI2NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 2, 1, 1),
    _Gs2326STPMSTI2NormalPortConfPort_Type()
)
gs2326STPMSTI2NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI2NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI2NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI2NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI2NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI2NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI2NormalPortPathCost = _Gs2326STPMSTI2NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 2, 1, 2),
    _Gs2326STPMSTI2NormalPortPathCost_Type()
)
gs2326STPMSTI2NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI2NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI2NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI2NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI2NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI2NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI2NormalPortPriority = _Gs2326STPMSTI2NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 2, 2, 1, 3),
    _Gs2326STPMSTI2NormalPortPriority_Type()
)
gs2326STPMSTI2NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI2NormalPortPriority.setStatus("current")
_Gs2326STPMSTI3Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI3Port = _Gs2326STPMSTI3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3)
)
_Gs2326STPMSTI3AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI3AggregatedPort = _Gs2326STPMSTI3AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 1)
)


class _Gs2326STPMSTI3AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI3AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI3AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI3AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI3AggregatedPortPathCost = _Gs2326STPMSTI3AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 1, 1),
    _Gs2326STPMSTI3AggregatedPortPathCost_Type()
)
gs2326STPMSTI3AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI3AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI3AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI3AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI3AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI3AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI3AggregatedPortPriority = _Gs2326STPMSTI3AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 1, 2),
    _Gs2326STPMSTI3AggregatedPortPriority_Type()
)
gs2326STPMSTI3AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI3AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI3NormalPortTable_Object = MibTable
gs2326STPMSTI3NormalPortTable = _Gs2326STPMSTI3NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI3NormalPortTable.setStatus("current")
_Gs2326STPMSTI3NormalPortEntry_Object = MibTableRow
gs2326STPMSTI3NormalPortEntry = _Gs2326STPMSTI3NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 2, 1)
)
gs2326STPMSTI3NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI3NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI3NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI3NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI3NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI3NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI3NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI3NormalPortConfPort = _Gs2326STPMSTI3NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 2, 1, 1),
    _Gs2326STPMSTI3NormalPortConfPort_Type()
)
gs2326STPMSTI3NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI3NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI3NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI3NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI3NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI3NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI3NormalPortPathCost = _Gs2326STPMSTI3NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 2, 1, 2),
    _Gs2326STPMSTI3NormalPortPathCost_Type()
)
gs2326STPMSTI3NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI3NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI3NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI3NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI3NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI3NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI3NormalPortPriority = _Gs2326STPMSTI3NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 3, 2, 1, 3),
    _Gs2326STPMSTI3NormalPortPriority_Type()
)
gs2326STPMSTI3NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI3NormalPortPriority.setStatus("current")
_Gs2326STPMSTI4Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI4Port = _Gs2326STPMSTI4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4)
)
_Gs2326STPMSTI4AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI4AggregatedPort = _Gs2326STPMSTI4AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 1)
)


class _Gs2326STPMSTI4AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI4AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI4AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI4AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI4AggregatedPortPathCost = _Gs2326STPMSTI4AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 1, 1),
    _Gs2326STPMSTI4AggregatedPortPathCost_Type()
)
gs2326STPMSTI4AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI4AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI4AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI4AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI4AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI4AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI4AggregatedPortPriority = _Gs2326STPMSTI4AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 1, 2),
    _Gs2326STPMSTI4AggregatedPortPriority_Type()
)
gs2326STPMSTI4AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI4AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI4NormalPortTable_Object = MibTable
gs2326STPMSTI4NormalPortTable = _Gs2326STPMSTI4NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI4NormalPortTable.setStatus("current")
_Gs2326STPMSTI4NormalPortEntry_Object = MibTableRow
gs2326STPMSTI4NormalPortEntry = _Gs2326STPMSTI4NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 2, 1)
)
gs2326STPMSTI4NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI4NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI4NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI4NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI4NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI4NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI4NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI4NormalPortConfPort = _Gs2326STPMSTI4NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 2, 1, 1),
    _Gs2326STPMSTI4NormalPortConfPort_Type()
)
gs2326STPMSTI4NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI4NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI4NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI4NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI4NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI4NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI4NormalPortPathCost = _Gs2326STPMSTI4NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 2, 1, 2),
    _Gs2326STPMSTI4NormalPortPathCost_Type()
)
gs2326STPMSTI4NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI4NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI4NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI4NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI4NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI4NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI4NormalPortPriority = _Gs2326STPMSTI4NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 4, 2, 1, 3),
    _Gs2326STPMSTI4NormalPortPriority_Type()
)
gs2326STPMSTI4NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI4NormalPortPriority.setStatus("current")
_Gs2326STPMSTI5Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI5Port = _Gs2326STPMSTI5Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5)
)
_Gs2326STPMSTI5AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI5AggregatedPort = _Gs2326STPMSTI5AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 1)
)


class _Gs2326STPMSTI5AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI5AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI5AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI5AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI5AggregatedPortPathCost = _Gs2326STPMSTI5AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 1, 1),
    _Gs2326STPMSTI5AggregatedPortPathCost_Type()
)
gs2326STPMSTI5AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI5AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI5AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI5AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI5AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI5AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI5AggregatedPortPriority = _Gs2326STPMSTI5AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 1, 2),
    _Gs2326STPMSTI5AggregatedPortPriority_Type()
)
gs2326STPMSTI5AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI5AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI5NormalPortTable_Object = MibTable
gs2326STPMSTI5NormalPortTable = _Gs2326STPMSTI5NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI5NormalPortTable.setStatus("current")
_Gs2326STPMSTI5NormalPortEntry_Object = MibTableRow
gs2326STPMSTI5NormalPortEntry = _Gs2326STPMSTI5NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 2, 1)
)
gs2326STPMSTI5NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI5NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI5NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI5NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI5NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI5NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI5NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI5NormalPortConfPort = _Gs2326STPMSTI5NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 2, 1, 1),
    _Gs2326STPMSTI5NormalPortConfPort_Type()
)
gs2326STPMSTI5NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI5NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI5NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI5NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI5NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI5NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI5NormalPortPathCost = _Gs2326STPMSTI5NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 2, 1, 2),
    _Gs2326STPMSTI5NormalPortPathCost_Type()
)
gs2326STPMSTI5NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI5NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI5NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI5NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI5NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI5NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI5NormalPortPriority = _Gs2326STPMSTI5NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 5, 2, 1, 3),
    _Gs2326STPMSTI5NormalPortPriority_Type()
)
gs2326STPMSTI5NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI5NormalPortPriority.setStatus("current")
_Gs2326STPMSTI6Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI6Port = _Gs2326STPMSTI6Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6)
)
_Gs2326STPMSTI6AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI6AggregatedPort = _Gs2326STPMSTI6AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 1)
)


class _Gs2326STPMSTI6AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI6AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI6AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI6AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI6AggregatedPortPathCost = _Gs2326STPMSTI6AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 1, 1),
    _Gs2326STPMSTI6AggregatedPortPathCost_Type()
)
gs2326STPMSTI6AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI6AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI6AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI6AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI6AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI6AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI6AggregatedPortPriority = _Gs2326STPMSTI6AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 1, 2),
    _Gs2326STPMSTI6AggregatedPortPriority_Type()
)
gs2326STPMSTI6AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI6AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI6NormalPortTable_Object = MibTable
gs2326STPMSTI6NormalPortTable = _Gs2326STPMSTI6NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI6NormalPortTable.setStatus("current")
_Gs2326STPMSTI6NormalPortEntry_Object = MibTableRow
gs2326STPMSTI6NormalPortEntry = _Gs2326STPMSTI6NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 2, 1)
)
gs2326STPMSTI6NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI6NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI6NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI6NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI6NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI6NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI6NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI6NormalPortConfPort = _Gs2326STPMSTI6NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 2, 1, 1),
    _Gs2326STPMSTI6NormalPortConfPort_Type()
)
gs2326STPMSTI6NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI6NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI6NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI6NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI6NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI6NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI6NormalPortPathCost = _Gs2326STPMSTI6NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 2, 1, 2),
    _Gs2326STPMSTI6NormalPortPathCost_Type()
)
gs2326STPMSTI6NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI6NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI6NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI6NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI6NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI6NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI6NormalPortPriority = _Gs2326STPMSTI6NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 6, 2, 1, 3),
    _Gs2326STPMSTI6NormalPortPriority_Type()
)
gs2326STPMSTI6NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI6NormalPortPriority.setStatus("current")
_Gs2326STPMSTI7Port_ObjectIdentity = ObjectIdentity
gs2326STPMSTI7Port = _Gs2326STPMSTI7Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7)
)
_Gs2326STPMSTI7AggregatedPort_ObjectIdentity = ObjectIdentity
gs2326STPMSTI7AggregatedPort = _Gs2326STPMSTI7AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 1)
)


class _Gs2326STPMSTI7AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI7AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI7AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI7AggregatedPortPathCost_Object = MibScalar
gs2326STPMSTI7AggregatedPortPathCost = _Gs2326STPMSTI7AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 1, 1),
    _Gs2326STPMSTI7AggregatedPortPathCost_Type()
)
gs2326STPMSTI7AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI7AggregatedPortPathCost.setStatus("current")


class _Gs2326STPMSTI7AggregatedPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI7AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI7AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI7AggregatedPortPriority_Object = MibScalar
gs2326STPMSTI7AggregatedPortPriority = _Gs2326STPMSTI7AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 1, 2),
    _Gs2326STPMSTI7AggregatedPortPriority_Type()
)
gs2326STPMSTI7AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI7AggregatedPortPriority.setStatus("current")
_Gs2326STPMSTI7NormalPortTable_Object = MibTable
gs2326STPMSTI7NormalPortTable = _Gs2326STPMSTI7NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 2)
)
if mibBuilder.loadTexts:
    gs2326STPMSTI7NormalPortTable.setStatus("current")
_Gs2326STPMSTI7NormalPortEntry_Object = MibTableRow
gs2326STPMSTI7NormalPortEntry = _Gs2326STPMSTI7NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 2, 1)
)
gs2326STPMSTI7NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPMSTI7NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2326STPMSTI7NormalPortEntry.setStatus("current")


class _Gs2326STPMSTI7NormalPortConfPort_Type(Integer32):
    """Custom type gs2326STPMSTI7NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPMSTI7NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2326STPMSTI7NormalPortConfPort_Object = MibTableColumn
gs2326STPMSTI7NormalPortConfPort = _Gs2326STPMSTI7NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 2, 1, 1),
    _Gs2326STPMSTI7NormalPortConfPort_Type()
)
gs2326STPMSTI7NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPMSTI7NormalPortConfPort.setStatus("current")


class _Gs2326STPMSTI7NormalPortPathCost_Type(Integer32):
    """Custom type gs2326STPMSTI7NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326STPMSTI7NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2326STPMSTI7NormalPortPathCost_Object = MibTableColumn
gs2326STPMSTI7NormalPortPathCost = _Gs2326STPMSTI7NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 2, 1, 2),
    _Gs2326STPMSTI7NormalPortPathCost_Type()
)
gs2326STPMSTI7NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI7NormalPortPathCost.setStatus("current")


class _Gs2326STPMSTI7NormalPortPriority_Type(Integer32):
    """Custom type gs2326STPMSTI7NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2326STPMSTI7NormalPortPriority_Type.__name__ = "Integer32"
_Gs2326STPMSTI7NormalPortPriority_Object = MibTableColumn
gs2326STPMSTI7NormalPortPriority = _Gs2326STPMSTI7NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 7, 7, 2, 1, 3),
    _Gs2326STPMSTI7NormalPortPriority_Type()
)
gs2326STPMSTI7NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326STPMSTI7NormalPortPriority.setStatus("current")
_Gs2326STPBridgeStatus_ObjectIdentity = ObjectIdentity
gs2326STPBridgeStatus = _Gs2326STPBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8)
)
_Gs2326CISTBridgeSTP_ObjectIdentity = ObjectIdentity
gs2326CISTBridgeSTP = _Gs2326CISTBridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1)
)
_Gs2326CISTBridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326CISTBridgeSTPStatus = _Gs2326CISTBridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1)
)
_Gs2326CISTBridgeInstance_Type = DisplayString
_Gs2326CISTBridgeInstance_Object = MibScalar
gs2326CISTBridgeInstance = _Gs2326CISTBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 1),
    _Gs2326CISTBridgeInstance_Type()
)
gs2326CISTBridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTBridgeInstance.setStatus("current")
_Gs2326CISTBridgeID_Type = DisplayString
_Gs2326CISTBridgeID_Object = MibScalar
gs2326CISTBridgeID = _Gs2326CISTBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 2),
    _Gs2326CISTBridgeID_Type()
)
gs2326CISTBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTBridgeID.setStatus("current")
_Gs2326CISTRootID_Type = DisplayString
_Gs2326CISTRootID_Object = MibScalar
gs2326CISTRootID = _Gs2326CISTRootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 3),
    _Gs2326CISTRootID_Type()
)
gs2326CISTRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTRootID.setStatus("current")
_Gs2326CISTRootPort_Type = DisplayString
_Gs2326CISTRootPort_Object = MibScalar
gs2326CISTRootPort = _Gs2326CISTRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 4),
    _Gs2326CISTRootPort_Type()
)
gs2326CISTRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTRootPort.setStatus("current")


class _Gs2326CISTRootCost_Type(Integer32):
    """Custom type gs2326CISTRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326CISTRootCost_Type.__name__ = "Integer32"
_Gs2326CISTRootCost_Object = MibScalar
gs2326CISTRootCost = _Gs2326CISTRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 5),
    _Gs2326CISTRootCost_Type()
)
gs2326CISTRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTRootCost.setStatus("current")
_Gs2326CISTRegionalRoot_Type = DisplayString
_Gs2326CISTRegionalRoot_Object = MibScalar
gs2326CISTRegionalRoot = _Gs2326CISTRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 6),
    _Gs2326CISTRegionalRoot_Type()
)
gs2326CISTRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTRegionalRoot.setStatus("current")


class _Gs2326CISTInternalRootCost_Type(Integer32):
    """Custom type gs2326CISTInternalRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326CISTInternalRootCost_Type.__name__ = "Integer32"
_Gs2326CISTInternalRootCost_Object = MibScalar
gs2326CISTInternalRootCost = _Gs2326CISTInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 7),
    _Gs2326CISTInternalRootCost_Type()
)
gs2326CISTInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTInternalRootCost.setStatus("current")
_Gs2326CISTTopologyFlag_Type = DisplayString
_Gs2326CISTTopologyFlag_Object = MibScalar
gs2326CISTTopologyFlag = _Gs2326CISTTopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 8),
    _Gs2326CISTTopologyFlag_Type()
)
gs2326CISTTopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTTopologyFlag.setStatus("current")
_Gs2326CISTTopologyChangeCount_Type = Counter32
_Gs2326CISTTopologyChangeCount_Object = MibScalar
gs2326CISTTopologyChangeCount = _Gs2326CISTTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 9),
    _Gs2326CISTTopologyChangeCount_Type()
)
gs2326CISTTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTTopologyChangeCount.setStatus("current")
_Gs2326CISTTopologyChangeLast_Type = DisplayString
_Gs2326CISTTopologyChangeLast_Object = MibScalar
gs2326CISTTopologyChangeLast = _Gs2326CISTTopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 1, 10),
    _Gs2326CISTTopologyChangeLast_Type()
)
gs2326CISTTopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTTopologyChangeLast.setStatus("current")
_Gs2326CISTPortStateTable_Object = MibTable
gs2326CISTPortStateTable = _Gs2326CISTPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326CISTPortStateTable.setStatus("current")
_Gs2326CISTPortStateEntry_Object = MibTableRow
gs2326CISTPortStateEntry = _Gs2326CISTPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1)
)
gs2326CISTPortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326CISTPortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326CISTPortStateEntry.setStatus("current")


class _Gs2326CISTPortStateIndex_Type(Integer32):
    """Custom type gs2326CISTPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326CISTPortStateIndex_Type.__name__ = "Integer32"
_Gs2326CISTPortStateIndex_Object = MibTableColumn
gs2326CISTPortStateIndex = _Gs2326CISTPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 1),
    _Gs2326CISTPortStateIndex_Type()
)
gs2326CISTPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326CISTPortStateIndex.setStatus("current")
_Gs2326CISTPortStatePort_Type = DisplayString
_Gs2326CISTPortStatePort_Object = MibTableColumn
gs2326CISTPortStatePort = _Gs2326CISTPortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 2),
    _Gs2326CISTPortStatePort_Type()
)
gs2326CISTPortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStatePort.setStatus("current")
_Gs2326CISTPortStatePortID_Type = DisplayString
_Gs2326CISTPortStatePortID_Object = MibTableColumn
gs2326CISTPortStatePortID = _Gs2326CISTPortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 3),
    _Gs2326CISTPortStatePortID_Type()
)
gs2326CISTPortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStatePortID.setStatus("current")
_Gs2326CISTPortStateRole_Type = DisplayString
_Gs2326CISTPortStateRole_Object = MibTableColumn
gs2326CISTPortStateRole = _Gs2326CISTPortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 4),
    _Gs2326CISTPortStateRole_Type()
)
gs2326CISTPortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStateRole.setStatus("current")
_Gs2326CISTPortStateState_Type = DisplayString
_Gs2326CISTPortStateState_Object = MibTableColumn
gs2326CISTPortStateState = _Gs2326CISTPortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 5),
    _Gs2326CISTPortStateState_Type()
)
gs2326CISTPortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStateState.setStatus("current")


class _Gs2326CISTPortStatePathCost_Type(Integer32):
    """Custom type gs2326CISTPortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326CISTPortStatePathCost_Type.__name__ = "Integer32"
_Gs2326CISTPortStatePathCost_Object = MibTableColumn
gs2326CISTPortStatePathCost = _Gs2326CISTPortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 6),
    _Gs2326CISTPortStatePathCost_Type()
)
gs2326CISTPortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStatePathCost.setStatus("current")
_Gs2326CISTPortStateEdge_Type = DisplayString
_Gs2326CISTPortStateEdge_Object = MibTableColumn
gs2326CISTPortStateEdge = _Gs2326CISTPortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 7),
    _Gs2326CISTPortStateEdge_Type()
)
gs2326CISTPortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStateEdge.setStatus("current")
_Gs2326CISTPortStatePoint2Point_Type = DisplayString
_Gs2326CISTPortStatePoint2Point_Object = MibTableColumn
gs2326CISTPortStatePoint2Point = _Gs2326CISTPortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 8),
    _Gs2326CISTPortStatePoint2Point_Type()
)
gs2326CISTPortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStatePoint2Point.setStatus("current")
_Gs2326CISTPortStateUptime_Type = DisplayString
_Gs2326CISTPortStateUptime_Object = MibTableColumn
gs2326CISTPortStateUptime = _Gs2326CISTPortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 1, 2, 1, 9),
    _Gs2326CISTPortStateUptime_Type()
)
gs2326CISTPortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326CISTPortStateUptime.setStatus("current")
_Gs2326MSTI1BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI1BridgeSTP = _Gs2326MSTI1BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2)
)
_Gs2326MSTI1BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI1BridgeSTPStatus = _Gs2326MSTI1BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1)
)
_Gs2326MSTI1BridgeInstance_Type = DisplayString
_Gs2326MSTI1BridgeInstance_Object = MibScalar
gs2326MSTI1BridgeInstance = _Gs2326MSTI1BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 1),
    _Gs2326MSTI1BridgeInstance_Type()
)
gs2326MSTI1BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1BridgeInstance.setStatus("current")
_Gs2326MSTI1BridgeID_Type = DisplayString
_Gs2326MSTI1BridgeID_Object = MibScalar
gs2326MSTI1BridgeID = _Gs2326MSTI1BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 2),
    _Gs2326MSTI1BridgeID_Type()
)
gs2326MSTI1BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1BridgeID.setStatus("current")
_Gs2326MSTI1RootID_Type = DisplayString
_Gs2326MSTI1RootID_Object = MibScalar
gs2326MSTI1RootID = _Gs2326MSTI1RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 3),
    _Gs2326MSTI1RootID_Type()
)
gs2326MSTI1RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1RootID.setStatus("current")
_Gs2326MSTI1RootPort_Type = DisplayString
_Gs2326MSTI1RootPort_Object = MibScalar
gs2326MSTI1RootPort = _Gs2326MSTI1RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 4),
    _Gs2326MSTI1RootPort_Type()
)
gs2326MSTI1RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1RootPort.setStatus("current")


class _Gs2326MSTI1RootCost_Type(Integer32):
    """Custom type gs2326MSTI1RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI1RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI1RootCost_Object = MibScalar
gs2326MSTI1RootCost = _Gs2326MSTI1RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 5),
    _Gs2326MSTI1RootCost_Type()
)
gs2326MSTI1RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1RootCost.setStatus("current")
_Gs2326MSTI1TopologyFlag_Type = DisplayString
_Gs2326MSTI1TopologyFlag_Object = MibScalar
gs2326MSTI1TopologyFlag = _Gs2326MSTI1TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 8),
    _Gs2326MSTI1TopologyFlag_Type()
)
gs2326MSTI1TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1TopologyFlag.setStatus("current")
_Gs2326MSTI1TopologyChangeCount_Type = Counter32
_Gs2326MSTI1TopologyChangeCount_Object = MibScalar
gs2326MSTI1TopologyChangeCount = _Gs2326MSTI1TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 9),
    _Gs2326MSTI1TopologyChangeCount_Type()
)
gs2326MSTI1TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1TopologyChangeCount.setStatus("current")
_Gs2326MSTI1TopologyChangeLast_Type = DisplayString
_Gs2326MSTI1TopologyChangeLast_Object = MibScalar
gs2326MSTI1TopologyChangeLast = _Gs2326MSTI1TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 1, 10),
    _Gs2326MSTI1TopologyChangeLast_Type()
)
gs2326MSTI1TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1TopologyChangeLast.setStatus("current")
_Gs2326MSTI1PortStateTable_Object = MibTable
gs2326MSTI1PortStateTable = _Gs2326MSTI1PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateTable.setStatus("current")
_Gs2326MSTI1PortStateEntry_Object = MibTableRow
gs2326MSTI1PortStateEntry = _Gs2326MSTI1PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1)
)
gs2326MSTI1PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI1PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateEntry.setStatus("current")


class _Gs2326MSTI1PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI1PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI1PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI1PortStateIndex_Object = MibTableColumn
gs2326MSTI1PortStateIndex = _Gs2326MSTI1PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 1),
    _Gs2326MSTI1PortStateIndex_Type()
)
gs2326MSTI1PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateIndex.setStatus("current")
_Gs2326MSTI1PortStatePort_Type = DisplayString
_Gs2326MSTI1PortStatePort_Object = MibTableColumn
gs2326MSTI1PortStatePort = _Gs2326MSTI1PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 2),
    _Gs2326MSTI1PortStatePort_Type()
)
gs2326MSTI1PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStatePort.setStatus("current")
_Gs2326MSTI1PortStatePortID_Type = DisplayString
_Gs2326MSTI1PortStatePortID_Object = MibTableColumn
gs2326MSTI1PortStatePortID = _Gs2326MSTI1PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 3),
    _Gs2326MSTI1PortStatePortID_Type()
)
gs2326MSTI1PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStatePortID.setStatus("current")
_Gs2326MSTI1PortStateRole_Type = DisplayString
_Gs2326MSTI1PortStateRole_Object = MibTableColumn
gs2326MSTI1PortStateRole = _Gs2326MSTI1PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 4),
    _Gs2326MSTI1PortStateRole_Type()
)
gs2326MSTI1PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateRole.setStatus("current")
_Gs2326MSTI1PortStateState_Type = DisplayString
_Gs2326MSTI1PortStateState_Object = MibTableColumn
gs2326MSTI1PortStateState = _Gs2326MSTI1PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 5),
    _Gs2326MSTI1PortStateState_Type()
)
gs2326MSTI1PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateState.setStatus("current")


class _Gs2326MSTI1PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI1PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI1PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI1PortStatePathCost_Object = MibTableColumn
gs2326MSTI1PortStatePathCost = _Gs2326MSTI1PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 6),
    _Gs2326MSTI1PortStatePathCost_Type()
)
gs2326MSTI1PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStatePathCost.setStatus("current")
_Gs2326MSTI1PortStateEdge_Type = DisplayString
_Gs2326MSTI1PortStateEdge_Object = MibTableColumn
gs2326MSTI1PortStateEdge = _Gs2326MSTI1PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 7),
    _Gs2326MSTI1PortStateEdge_Type()
)
gs2326MSTI1PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateEdge.setStatus("current")
_Gs2326MSTI1PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI1PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI1PortStatePoint2Point = _Gs2326MSTI1PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 8),
    _Gs2326MSTI1PortStatePoint2Point_Type()
)
gs2326MSTI1PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStatePoint2Point.setStatus("current")
_Gs2326MSTI1PortStateUptime_Type = DisplayString
_Gs2326MSTI1PortStateUptime_Object = MibTableColumn
gs2326MSTI1PortStateUptime = _Gs2326MSTI1PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 2, 2, 1, 9),
    _Gs2326MSTI1PortStateUptime_Type()
)
gs2326MSTI1PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI1PortStateUptime.setStatus("current")
_Gs2326MSTI2BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI2BridgeSTP = _Gs2326MSTI2BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3)
)
_Gs2326MSTI2BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI2BridgeSTPStatus = _Gs2326MSTI2BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1)
)
_Gs2326MSTI2BridgeInstance_Type = DisplayString
_Gs2326MSTI2BridgeInstance_Object = MibScalar
gs2326MSTI2BridgeInstance = _Gs2326MSTI2BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 1),
    _Gs2326MSTI2BridgeInstance_Type()
)
gs2326MSTI2BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2BridgeInstance.setStatus("current")
_Gs2326MSTI2BridgeID_Type = DisplayString
_Gs2326MSTI2BridgeID_Object = MibScalar
gs2326MSTI2BridgeID = _Gs2326MSTI2BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 2),
    _Gs2326MSTI2BridgeID_Type()
)
gs2326MSTI2BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2BridgeID.setStatus("current")
_Gs2326MSTI2RootID_Type = DisplayString
_Gs2326MSTI2RootID_Object = MibScalar
gs2326MSTI2RootID = _Gs2326MSTI2RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 3),
    _Gs2326MSTI2RootID_Type()
)
gs2326MSTI2RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2RootID.setStatus("current")
_Gs2326MSTI2RootPort_Type = DisplayString
_Gs2326MSTI2RootPort_Object = MibScalar
gs2326MSTI2RootPort = _Gs2326MSTI2RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 4),
    _Gs2326MSTI2RootPort_Type()
)
gs2326MSTI2RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2RootPort.setStatus("current")


class _Gs2326MSTI2RootCost_Type(Integer32):
    """Custom type gs2326MSTI2RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI2RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI2RootCost_Object = MibScalar
gs2326MSTI2RootCost = _Gs2326MSTI2RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 5),
    _Gs2326MSTI2RootCost_Type()
)
gs2326MSTI2RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2RootCost.setStatus("current")
_Gs2326MSTI2TopologyFlag_Type = DisplayString
_Gs2326MSTI2TopologyFlag_Object = MibScalar
gs2326MSTI2TopologyFlag = _Gs2326MSTI2TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 8),
    _Gs2326MSTI2TopologyFlag_Type()
)
gs2326MSTI2TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2TopologyFlag.setStatus("current")
_Gs2326MSTI2TopologyChangeCount_Type = Counter32
_Gs2326MSTI2TopologyChangeCount_Object = MibScalar
gs2326MSTI2TopologyChangeCount = _Gs2326MSTI2TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 9),
    _Gs2326MSTI2TopologyChangeCount_Type()
)
gs2326MSTI2TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2TopologyChangeCount.setStatus("current")
_Gs2326MSTI2TopologyChangeLast_Type = DisplayString
_Gs2326MSTI2TopologyChangeLast_Object = MibScalar
gs2326MSTI2TopologyChangeLast = _Gs2326MSTI2TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 1, 10),
    _Gs2326MSTI2TopologyChangeLast_Type()
)
gs2326MSTI2TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2TopologyChangeLast.setStatus("current")
_Gs2326MSTI2PortStateTable_Object = MibTable
gs2326MSTI2PortStateTable = _Gs2326MSTI2PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateTable.setStatus("current")
_Gs2326MSTI2PortStateEntry_Object = MibTableRow
gs2326MSTI2PortStateEntry = _Gs2326MSTI2PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1)
)
gs2326MSTI2PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI2PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateEntry.setStatus("current")


class _Gs2326MSTI2PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI2PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI2PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI2PortStateIndex_Object = MibTableColumn
gs2326MSTI2PortStateIndex = _Gs2326MSTI2PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 1),
    _Gs2326MSTI2PortStateIndex_Type()
)
gs2326MSTI2PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateIndex.setStatus("current")
_Gs2326MSTI2PortStatePort_Type = DisplayString
_Gs2326MSTI2PortStatePort_Object = MibTableColumn
gs2326MSTI2PortStatePort = _Gs2326MSTI2PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 2),
    _Gs2326MSTI2PortStatePort_Type()
)
gs2326MSTI2PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStatePort.setStatus("current")
_Gs2326MSTI2PortStatePortID_Type = DisplayString
_Gs2326MSTI2PortStatePortID_Object = MibTableColumn
gs2326MSTI2PortStatePortID = _Gs2326MSTI2PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 3),
    _Gs2326MSTI2PortStatePortID_Type()
)
gs2326MSTI2PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStatePortID.setStatus("current")
_Gs2326MSTI2PortStateRole_Type = DisplayString
_Gs2326MSTI2PortStateRole_Object = MibTableColumn
gs2326MSTI2PortStateRole = _Gs2326MSTI2PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 4),
    _Gs2326MSTI2PortStateRole_Type()
)
gs2326MSTI2PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateRole.setStatus("current")
_Gs2326MSTI2PortStateState_Type = DisplayString
_Gs2326MSTI2PortStateState_Object = MibTableColumn
gs2326MSTI2PortStateState = _Gs2326MSTI2PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 5),
    _Gs2326MSTI2PortStateState_Type()
)
gs2326MSTI2PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateState.setStatus("current")


class _Gs2326MSTI2PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI2PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI2PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI2PortStatePathCost_Object = MibTableColumn
gs2326MSTI2PortStatePathCost = _Gs2326MSTI2PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 6),
    _Gs2326MSTI2PortStatePathCost_Type()
)
gs2326MSTI2PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStatePathCost.setStatus("current")
_Gs2326MSTI2PortStateEdge_Type = DisplayString
_Gs2326MSTI2PortStateEdge_Object = MibTableColumn
gs2326MSTI2PortStateEdge = _Gs2326MSTI2PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 7),
    _Gs2326MSTI2PortStateEdge_Type()
)
gs2326MSTI2PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateEdge.setStatus("current")
_Gs2326MSTI2PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI2PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI2PortStatePoint2Point = _Gs2326MSTI2PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 8),
    _Gs2326MSTI2PortStatePoint2Point_Type()
)
gs2326MSTI2PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStatePoint2Point.setStatus("current")
_Gs2326MSTI2PortStateUptime_Type = DisplayString
_Gs2326MSTI2PortStateUptime_Object = MibTableColumn
gs2326MSTI2PortStateUptime = _Gs2326MSTI2PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 3, 2, 1, 9),
    _Gs2326MSTI2PortStateUptime_Type()
)
gs2326MSTI2PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI2PortStateUptime.setStatus("current")
_Gs2326MSTI3BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI3BridgeSTP = _Gs2326MSTI3BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4)
)
_Gs2326MSTI3BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI3BridgeSTPStatus = _Gs2326MSTI3BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1)
)
_Gs2326MSTI3BridgeInstance_Type = DisplayString
_Gs2326MSTI3BridgeInstance_Object = MibScalar
gs2326MSTI3BridgeInstance = _Gs2326MSTI3BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 1),
    _Gs2326MSTI3BridgeInstance_Type()
)
gs2326MSTI3BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3BridgeInstance.setStatus("current")
_Gs2326MSTI3BridgeID_Type = DisplayString
_Gs2326MSTI3BridgeID_Object = MibScalar
gs2326MSTI3BridgeID = _Gs2326MSTI3BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 2),
    _Gs2326MSTI3BridgeID_Type()
)
gs2326MSTI3BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3BridgeID.setStatus("current")
_Gs2326MSTI3RootID_Type = DisplayString
_Gs2326MSTI3RootID_Object = MibScalar
gs2326MSTI3RootID = _Gs2326MSTI3RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 3),
    _Gs2326MSTI3RootID_Type()
)
gs2326MSTI3RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3RootID.setStatus("current")
_Gs2326MSTI3RootPort_Type = DisplayString
_Gs2326MSTI3RootPort_Object = MibScalar
gs2326MSTI3RootPort = _Gs2326MSTI3RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 4),
    _Gs2326MSTI3RootPort_Type()
)
gs2326MSTI3RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3RootPort.setStatus("current")


class _Gs2326MSTI3RootCost_Type(Integer32):
    """Custom type gs2326MSTI3RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI3RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI3RootCost_Object = MibScalar
gs2326MSTI3RootCost = _Gs2326MSTI3RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 5),
    _Gs2326MSTI3RootCost_Type()
)
gs2326MSTI3RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3RootCost.setStatus("current")
_Gs2326MSTI3TopologyFlag_Type = DisplayString
_Gs2326MSTI3TopologyFlag_Object = MibScalar
gs2326MSTI3TopologyFlag = _Gs2326MSTI3TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 8),
    _Gs2326MSTI3TopologyFlag_Type()
)
gs2326MSTI3TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3TopologyFlag.setStatus("current")
_Gs2326MSTI3TopologyChangeCount_Type = Counter32
_Gs2326MSTI3TopologyChangeCount_Object = MibScalar
gs2326MSTI3TopologyChangeCount = _Gs2326MSTI3TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 9),
    _Gs2326MSTI3TopologyChangeCount_Type()
)
gs2326MSTI3TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3TopologyChangeCount.setStatus("current")
_Gs2326MSTI3TopologyChangeLast_Type = DisplayString
_Gs2326MSTI3TopologyChangeLast_Object = MibScalar
gs2326MSTI3TopologyChangeLast = _Gs2326MSTI3TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 1, 10),
    _Gs2326MSTI3TopologyChangeLast_Type()
)
gs2326MSTI3TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3TopologyChangeLast.setStatus("current")
_Gs2326MSTI3PortStateTable_Object = MibTable
gs2326MSTI3PortStateTable = _Gs2326MSTI3PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateTable.setStatus("current")
_Gs2326MSTI3PortStateEntry_Object = MibTableRow
gs2326MSTI3PortStateEntry = _Gs2326MSTI3PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1)
)
gs2326MSTI3PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI3PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateEntry.setStatus("current")


class _Gs2326MSTI3PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI3PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI3PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI3PortStateIndex_Object = MibTableColumn
gs2326MSTI3PortStateIndex = _Gs2326MSTI3PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 1),
    _Gs2326MSTI3PortStateIndex_Type()
)
gs2326MSTI3PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateIndex.setStatus("current")
_Gs2326MSTI3PortStatePort_Type = DisplayString
_Gs2326MSTI3PortStatePort_Object = MibTableColumn
gs2326MSTI3PortStatePort = _Gs2326MSTI3PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 2),
    _Gs2326MSTI3PortStatePort_Type()
)
gs2326MSTI3PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStatePort.setStatus("current")
_Gs2326MSTI3PortStatePortID_Type = DisplayString
_Gs2326MSTI3PortStatePortID_Object = MibTableColumn
gs2326MSTI3PortStatePortID = _Gs2326MSTI3PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 3),
    _Gs2326MSTI3PortStatePortID_Type()
)
gs2326MSTI3PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStatePortID.setStatus("current")
_Gs2326MSTI3PortStateRole_Type = DisplayString
_Gs2326MSTI3PortStateRole_Object = MibTableColumn
gs2326MSTI3PortStateRole = _Gs2326MSTI3PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 4),
    _Gs2326MSTI3PortStateRole_Type()
)
gs2326MSTI3PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateRole.setStatus("current")
_Gs2326MSTI3PortStateState_Type = DisplayString
_Gs2326MSTI3PortStateState_Object = MibTableColumn
gs2326MSTI3PortStateState = _Gs2326MSTI3PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 5),
    _Gs2326MSTI3PortStateState_Type()
)
gs2326MSTI3PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateState.setStatus("current")


class _Gs2326MSTI3PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI3PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI3PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI3PortStatePathCost_Object = MibTableColumn
gs2326MSTI3PortStatePathCost = _Gs2326MSTI3PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 6),
    _Gs2326MSTI3PortStatePathCost_Type()
)
gs2326MSTI3PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStatePathCost.setStatus("current")
_Gs2326MSTI3PortStateEdge_Type = DisplayString
_Gs2326MSTI3PortStateEdge_Object = MibTableColumn
gs2326MSTI3PortStateEdge = _Gs2326MSTI3PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 7),
    _Gs2326MSTI3PortStateEdge_Type()
)
gs2326MSTI3PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateEdge.setStatus("current")
_Gs2326MSTI3PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI3PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI3PortStatePoint2Point = _Gs2326MSTI3PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 8),
    _Gs2326MSTI3PortStatePoint2Point_Type()
)
gs2326MSTI3PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStatePoint2Point.setStatus("current")
_Gs2326MSTI3PortStateUptime_Type = DisplayString
_Gs2326MSTI3PortStateUptime_Object = MibTableColumn
gs2326MSTI3PortStateUptime = _Gs2326MSTI3PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 4, 2, 1, 9),
    _Gs2326MSTI3PortStateUptime_Type()
)
gs2326MSTI3PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI3PortStateUptime.setStatus("current")
_Gs2326MSTI4BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI4BridgeSTP = _Gs2326MSTI4BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5)
)
_Gs2326MSTI4BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI4BridgeSTPStatus = _Gs2326MSTI4BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1)
)
_Gs2326MSTI4BridgeInstance_Type = DisplayString
_Gs2326MSTI4BridgeInstance_Object = MibScalar
gs2326MSTI4BridgeInstance = _Gs2326MSTI4BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 1),
    _Gs2326MSTI4BridgeInstance_Type()
)
gs2326MSTI4BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4BridgeInstance.setStatus("current")
_Gs2326MSTI4BridgeID_Type = DisplayString
_Gs2326MSTI4BridgeID_Object = MibScalar
gs2326MSTI4BridgeID = _Gs2326MSTI4BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 2),
    _Gs2326MSTI4BridgeID_Type()
)
gs2326MSTI4BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4BridgeID.setStatus("current")
_Gs2326MSTI4RootID_Type = DisplayString
_Gs2326MSTI4RootID_Object = MibScalar
gs2326MSTI4RootID = _Gs2326MSTI4RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 3),
    _Gs2326MSTI4RootID_Type()
)
gs2326MSTI4RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4RootID.setStatus("current")
_Gs2326MSTI4RootPort_Type = DisplayString
_Gs2326MSTI4RootPort_Object = MibScalar
gs2326MSTI4RootPort = _Gs2326MSTI4RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 4),
    _Gs2326MSTI4RootPort_Type()
)
gs2326MSTI4RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4RootPort.setStatus("current")


class _Gs2326MSTI4RootCost_Type(Integer32):
    """Custom type gs2326MSTI4RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI4RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI4RootCost_Object = MibScalar
gs2326MSTI4RootCost = _Gs2326MSTI4RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 5),
    _Gs2326MSTI4RootCost_Type()
)
gs2326MSTI4RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4RootCost.setStatus("current")
_Gs2326MSTI4TopologyFlag_Type = DisplayString
_Gs2326MSTI4TopologyFlag_Object = MibScalar
gs2326MSTI4TopologyFlag = _Gs2326MSTI4TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 8),
    _Gs2326MSTI4TopologyFlag_Type()
)
gs2326MSTI4TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4TopologyFlag.setStatus("current")
_Gs2326MSTI4TopologyChangeCount_Type = Counter32
_Gs2326MSTI4TopologyChangeCount_Object = MibScalar
gs2326MSTI4TopologyChangeCount = _Gs2326MSTI4TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 9),
    _Gs2326MSTI4TopologyChangeCount_Type()
)
gs2326MSTI4TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4TopologyChangeCount.setStatus("current")
_Gs2326MSTI4TopologyChangeLast_Type = DisplayString
_Gs2326MSTI4TopologyChangeLast_Object = MibScalar
gs2326MSTI4TopologyChangeLast = _Gs2326MSTI4TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 1, 10),
    _Gs2326MSTI4TopologyChangeLast_Type()
)
gs2326MSTI4TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4TopologyChangeLast.setStatus("current")
_Gs2326MSTI4PortStateTable_Object = MibTable
gs2326MSTI4PortStateTable = _Gs2326MSTI4PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateTable.setStatus("current")
_Gs2326MSTI4PortStateEntry_Object = MibTableRow
gs2326MSTI4PortStateEntry = _Gs2326MSTI4PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1)
)
gs2326MSTI4PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI4PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateEntry.setStatus("current")


class _Gs2326MSTI4PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI4PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI4PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI4PortStateIndex_Object = MibTableColumn
gs2326MSTI4PortStateIndex = _Gs2326MSTI4PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 1),
    _Gs2326MSTI4PortStateIndex_Type()
)
gs2326MSTI4PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateIndex.setStatus("current")
_Gs2326MSTI4PortStatePort_Type = DisplayString
_Gs2326MSTI4PortStatePort_Object = MibTableColumn
gs2326MSTI4PortStatePort = _Gs2326MSTI4PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 2),
    _Gs2326MSTI4PortStatePort_Type()
)
gs2326MSTI4PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStatePort.setStatus("current")
_Gs2326MSTI4PortStatePortID_Type = DisplayString
_Gs2326MSTI4PortStatePortID_Object = MibTableColumn
gs2326MSTI4PortStatePortID = _Gs2326MSTI4PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 3),
    _Gs2326MSTI4PortStatePortID_Type()
)
gs2326MSTI4PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStatePortID.setStatus("current")
_Gs2326MSTI4PortStateRole_Type = DisplayString
_Gs2326MSTI4PortStateRole_Object = MibTableColumn
gs2326MSTI4PortStateRole = _Gs2326MSTI4PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 4),
    _Gs2326MSTI4PortStateRole_Type()
)
gs2326MSTI4PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateRole.setStatus("current")
_Gs2326MSTI4PortStateState_Type = DisplayString
_Gs2326MSTI4PortStateState_Object = MibTableColumn
gs2326MSTI4PortStateState = _Gs2326MSTI4PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 5),
    _Gs2326MSTI4PortStateState_Type()
)
gs2326MSTI4PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateState.setStatus("current")


class _Gs2326MSTI4PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI4PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI4PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI4PortStatePathCost_Object = MibTableColumn
gs2326MSTI4PortStatePathCost = _Gs2326MSTI4PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 6),
    _Gs2326MSTI4PortStatePathCost_Type()
)
gs2326MSTI4PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStatePathCost.setStatus("current")
_Gs2326MSTI4PortStateEdge_Type = DisplayString
_Gs2326MSTI4PortStateEdge_Object = MibTableColumn
gs2326MSTI4PortStateEdge = _Gs2326MSTI4PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 7),
    _Gs2326MSTI4PortStateEdge_Type()
)
gs2326MSTI4PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateEdge.setStatus("current")
_Gs2326MSTI4PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI4PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI4PortStatePoint2Point = _Gs2326MSTI4PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 8),
    _Gs2326MSTI4PortStatePoint2Point_Type()
)
gs2326MSTI4PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStatePoint2Point.setStatus("current")
_Gs2326MSTI4PortStateUptime_Type = DisplayString
_Gs2326MSTI4PortStateUptime_Object = MibTableColumn
gs2326MSTI4PortStateUptime = _Gs2326MSTI4PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 5, 2, 1, 9),
    _Gs2326MSTI4PortStateUptime_Type()
)
gs2326MSTI4PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI4PortStateUptime.setStatus("current")
_Gs2326MSTI5BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI5BridgeSTP = _Gs2326MSTI5BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6)
)
_Gs2326MSTI5BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI5BridgeSTPStatus = _Gs2326MSTI5BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1)
)
_Gs2326MSTI5BridgeInstance_Type = DisplayString
_Gs2326MSTI5BridgeInstance_Object = MibScalar
gs2326MSTI5BridgeInstance = _Gs2326MSTI5BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 1),
    _Gs2326MSTI5BridgeInstance_Type()
)
gs2326MSTI5BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5BridgeInstance.setStatus("current")
_Gs2326MSTI5BridgeID_Type = DisplayString
_Gs2326MSTI5BridgeID_Object = MibScalar
gs2326MSTI5BridgeID = _Gs2326MSTI5BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 2),
    _Gs2326MSTI5BridgeID_Type()
)
gs2326MSTI5BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5BridgeID.setStatus("current")
_Gs2326MSTI5RootID_Type = DisplayString
_Gs2326MSTI5RootID_Object = MibScalar
gs2326MSTI5RootID = _Gs2326MSTI5RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 3),
    _Gs2326MSTI5RootID_Type()
)
gs2326MSTI5RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5RootID.setStatus("current")
_Gs2326MSTI5RootPort_Type = DisplayString
_Gs2326MSTI5RootPort_Object = MibScalar
gs2326MSTI5RootPort = _Gs2326MSTI5RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 4),
    _Gs2326MSTI5RootPort_Type()
)
gs2326MSTI5RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5RootPort.setStatus("current")


class _Gs2326MSTI5RootCost_Type(Integer32):
    """Custom type gs2326MSTI5RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI5RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI5RootCost_Object = MibScalar
gs2326MSTI5RootCost = _Gs2326MSTI5RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 5),
    _Gs2326MSTI5RootCost_Type()
)
gs2326MSTI5RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5RootCost.setStatus("current")
_Gs2326MSTI5TopologyFlag_Type = DisplayString
_Gs2326MSTI5TopologyFlag_Object = MibScalar
gs2326MSTI5TopologyFlag = _Gs2326MSTI5TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 8),
    _Gs2326MSTI5TopologyFlag_Type()
)
gs2326MSTI5TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5TopologyFlag.setStatus("current")
_Gs2326MSTI5TopologyChangeCount_Type = Counter32
_Gs2326MSTI5TopologyChangeCount_Object = MibScalar
gs2326MSTI5TopologyChangeCount = _Gs2326MSTI5TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 9),
    _Gs2326MSTI5TopologyChangeCount_Type()
)
gs2326MSTI5TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5TopologyChangeCount.setStatus("current")
_Gs2326MSTI5TopologyChangeLast_Type = DisplayString
_Gs2326MSTI5TopologyChangeLast_Object = MibScalar
gs2326MSTI5TopologyChangeLast = _Gs2326MSTI5TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 1, 10),
    _Gs2326MSTI5TopologyChangeLast_Type()
)
gs2326MSTI5TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5TopologyChangeLast.setStatus("current")
_Gs2326MSTI5PortStateTable_Object = MibTable
gs2326MSTI5PortStateTable = _Gs2326MSTI5PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateTable.setStatus("current")
_Gs2326MSTI5PortStateEntry_Object = MibTableRow
gs2326MSTI5PortStateEntry = _Gs2326MSTI5PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1)
)
gs2326MSTI5PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI5PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateEntry.setStatus("current")


class _Gs2326MSTI5PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI5PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI5PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI5PortStateIndex_Object = MibTableColumn
gs2326MSTI5PortStateIndex = _Gs2326MSTI5PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 1),
    _Gs2326MSTI5PortStateIndex_Type()
)
gs2326MSTI5PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateIndex.setStatus("current")
_Gs2326MSTI5PortStatePort_Type = DisplayString
_Gs2326MSTI5PortStatePort_Object = MibTableColumn
gs2326MSTI5PortStatePort = _Gs2326MSTI5PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 2),
    _Gs2326MSTI5PortStatePort_Type()
)
gs2326MSTI5PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStatePort.setStatus("current")
_Gs2326MSTI5PortStatePortID_Type = DisplayString
_Gs2326MSTI5PortStatePortID_Object = MibTableColumn
gs2326MSTI5PortStatePortID = _Gs2326MSTI5PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 3),
    _Gs2326MSTI5PortStatePortID_Type()
)
gs2326MSTI5PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStatePortID.setStatus("current")
_Gs2326MSTI5PortStateRole_Type = DisplayString
_Gs2326MSTI5PortStateRole_Object = MibTableColumn
gs2326MSTI5PortStateRole = _Gs2326MSTI5PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 4),
    _Gs2326MSTI5PortStateRole_Type()
)
gs2326MSTI5PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateRole.setStatus("current")
_Gs2326MSTI5PortStateState_Type = DisplayString
_Gs2326MSTI5PortStateState_Object = MibTableColumn
gs2326MSTI5PortStateState = _Gs2326MSTI5PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 5),
    _Gs2326MSTI5PortStateState_Type()
)
gs2326MSTI5PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateState.setStatus("current")


class _Gs2326MSTI5PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI5PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI5PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI5PortStatePathCost_Object = MibTableColumn
gs2326MSTI5PortStatePathCost = _Gs2326MSTI5PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 6),
    _Gs2326MSTI5PortStatePathCost_Type()
)
gs2326MSTI5PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStatePathCost.setStatus("current")
_Gs2326MSTI5PortStateEdge_Type = DisplayString
_Gs2326MSTI5PortStateEdge_Object = MibTableColumn
gs2326MSTI5PortStateEdge = _Gs2326MSTI5PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 7),
    _Gs2326MSTI5PortStateEdge_Type()
)
gs2326MSTI5PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateEdge.setStatus("current")
_Gs2326MSTI5PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI5PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI5PortStatePoint2Point = _Gs2326MSTI5PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 8),
    _Gs2326MSTI5PortStatePoint2Point_Type()
)
gs2326MSTI5PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStatePoint2Point.setStatus("current")
_Gs2326MSTI5PortStateUptime_Type = DisplayString
_Gs2326MSTI5PortStateUptime_Object = MibTableColumn
gs2326MSTI5PortStateUptime = _Gs2326MSTI5PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 6, 2, 1, 9),
    _Gs2326MSTI5PortStateUptime_Type()
)
gs2326MSTI5PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI5PortStateUptime.setStatus("current")
_Gs2326MSTI6BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI6BridgeSTP = _Gs2326MSTI6BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7)
)
_Gs2326MSTI6BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI6BridgeSTPStatus = _Gs2326MSTI6BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1)
)
_Gs2326MSTI6BridgeInstance_Type = DisplayString
_Gs2326MSTI6BridgeInstance_Object = MibScalar
gs2326MSTI6BridgeInstance = _Gs2326MSTI6BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 1),
    _Gs2326MSTI6BridgeInstance_Type()
)
gs2326MSTI6BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6BridgeInstance.setStatus("current")
_Gs2326MSTI6BridgeID_Type = DisplayString
_Gs2326MSTI6BridgeID_Object = MibScalar
gs2326MSTI6BridgeID = _Gs2326MSTI6BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 2),
    _Gs2326MSTI6BridgeID_Type()
)
gs2326MSTI6BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6BridgeID.setStatus("current")
_Gs2326MSTI6RootID_Type = DisplayString
_Gs2326MSTI6RootID_Object = MibScalar
gs2326MSTI6RootID = _Gs2326MSTI6RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 3),
    _Gs2326MSTI6RootID_Type()
)
gs2326MSTI6RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6RootID.setStatus("current")
_Gs2326MSTI6RootPort_Type = DisplayString
_Gs2326MSTI6RootPort_Object = MibScalar
gs2326MSTI6RootPort = _Gs2326MSTI6RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 4),
    _Gs2326MSTI6RootPort_Type()
)
gs2326MSTI6RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6RootPort.setStatus("current")


class _Gs2326MSTI6RootCost_Type(Integer32):
    """Custom type gs2326MSTI6RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI6RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI6RootCost_Object = MibScalar
gs2326MSTI6RootCost = _Gs2326MSTI6RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 5),
    _Gs2326MSTI6RootCost_Type()
)
gs2326MSTI6RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6RootCost.setStatus("current")
_Gs2326MSTI6TopologyFlag_Type = DisplayString
_Gs2326MSTI6TopologyFlag_Object = MibScalar
gs2326MSTI6TopologyFlag = _Gs2326MSTI6TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 8),
    _Gs2326MSTI6TopologyFlag_Type()
)
gs2326MSTI6TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6TopologyFlag.setStatus("current")
_Gs2326MSTI6TopologyChangeCount_Type = Counter32
_Gs2326MSTI6TopologyChangeCount_Object = MibScalar
gs2326MSTI6TopologyChangeCount = _Gs2326MSTI6TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 9),
    _Gs2326MSTI6TopologyChangeCount_Type()
)
gs2326MSTI6TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6TopologyChangeCount.setStatus("current")
_Gs2326MSTI6TopologyChangeLast_Type = DisplayString
_Gs2326MSTI6TopologyChangeLast_Object = MibScalar
gs2326MSTI6TopologyChangeLast = _Gs2326MSTI6TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 1, 10),
    _Gs2326MSTI6TopologyChangeLast_Type()
)
gs2326MSTI6TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6TopologyChangeLast.setStatus("current")
_Gs2326MSTI6PortStateTable_Object = MibTable
gs2326MSTI6PortStateTable = _Gs2326MSTI6PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateTable.setStatus("current")
_Gs2326MSTI6PortStateEntry_Object = MibTableRow
gs2326MSTI6PortStateEntry = _Gs2326MSTI6PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1)
)
gs2326MSTI6PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI6PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateEntry.setStatus("current")


class _Gs2326MSTI6PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI6PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI6PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI6PortStateIndex_Object = MibTableColumn
gs2326MSTI6PortStateIndex = _Gs2326MSTI6PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 1),
    _Gs2326MSTI6PortStateIndex_Type()
)
gs2326MSTI6PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateIndex.setStatus("current")
_Gs2326MSTI6PortStatePort_Type = DisplayString
_Gs2326MSTI6PortStatePort_Object = MibTableColumn
gs2326MSTI6PortStatePort = _Gs2326MSTI6PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 2),
    _Gs2326MSTI6PortStatePort_Type()
)
gs2326MSTI6PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStatePort.setStatus("current")
_Gs2326MSTI6PortStatePortID_Type = DisplayString
_Gs2326MSTI6PortStatePortID_Object = MibTableColumn
gs2326MSTI6PortStatePortID = _Gs2326MSTI6PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 3),
    _Gs2326MSTI6PortStatePortID_Type()
)
gs2326MSTI6PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStatePortID.setStatus("current")
_Gs2326MSTI6PortStateRole_Type = DisplayString
_Gs2326MSTI6PortStateRole_Object = MibTableColumn
gs2326MSTI6PortStateRole = _Gs2326MSTI6PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 4),
    _Gs2326MSTI6PortStateRole_Type()
)
gs2326MSTI6PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateRole.setStatus("current")
_Gs2326MSTI6PortStateState_Type = DisplayString
_Gs2326MSTI6PortStateState_Object = MibTableColumn
gs2326MSTI6PortStateState = _Gs2326MSTI6PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 5),
    _Gs2326MSTI6PortStateState_Type()
)
gs2326MSTI6PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateState.setStatus("current")


class _Gs2326MSTI6PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI6PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI6PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI6PortStatePathCost_Object = MibTableColumn
gs2326MSTI6PortStatePathCost = _Gs2326MSTI6PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 6),
    _Gs2326MSTI6PortStatePathCost_Type()
)
gs2326MSTI6PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStatePathCost.setStatus("current")
_Gs2326MSTI6PortStateEdge_Type = DisplayString
_Gs2326MSTI6PortStateEdge_Object = MibTableColumn
gs2326MSTI6PortStateEdge = _Gs2326MSTI6PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 7),
    _Gs2326MSTI6PortStateEdge_Type()
)
gs2326MSTI6PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateEdge.setStatus("current")
_Gs2326MSTI6PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI6PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI6PortStatePoint2Point = _Gs2326MSTI6PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 8),
    _Gs2326MSTI6PortStatePoint2Point_Type()
)
gs2326MSTI6PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStatePoint2Point.setStatus("current")
_Gs2326MSTI6PortStateUptime_Type = DisplayString
_Gs2326MSTI6PortStateUptime_Object = MibTableColumn
gs2326MSTI6PortStateUptime = _Gs2326MSTI6PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 7, 2, 1, 9),
    _Gs2326MSTI6PortStateUptime_Type()
)
gs2326MSTI6PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI6PortStateUptime.setStatus("current")
_Gs2326MSTI7BridgeSTP_ObjectIdentity = ObjectIdentity
gs2326MSTI7BridgeSTP = _Gs2326MSTI7BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8)
)
_Gs2326MSTI7BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2326MSTI7BridgeSTPStatus = _Gs2326MSTI7BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1)
)
_Gs2326MSTI7BridgeInstance_Type = DisplayString
_Gs2326MSTI7BridgeInstance_Object = MibScalar
gs2326MSTI7BridgeInstance = _Gs2326MSTI7BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 1),
    _Gs2326MSTI7BridgeInstance_Type()
)
gs2326MSTI7BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7BridgeInstance.setStatus("current")
_Gs2326MSTI7BridgeID_Type = DisplayString
_Gs2326MSTI7BridgeID_Object = MibScalar
gs2326MSTI7BridgeID = _Gs2326MSTI7BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 2),
    _Gs2326MSTI7BridgeID_Type()
)
gs2326MSTI7BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7BridgeID.setStatus("current")
_Gs2326MSTI7RootID_Type = DisplayString
_Gs2326MSTI7RootID_Object = MibScalar
gs2326MSTI7RootID = _Gs2326MSTI7RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 3),
    _Gs2326MSTI7RootID_Type()
)
gs2326MSTI7RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7RootID.setStatus("current")
_Gs2326MSTI7RootPort_Type = DisplayString
_Gs2326MSTI7RootPort_Object = MibScalar
gs2326MSTI7RootPort = _Gs2326MSTI7RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 4),
    _Gs2326MSTI7RootPort_Type()
)
gs2326MSTI7RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7RootPort.setStatus("current")


class _Gs2326MSTI7RootCost_Type(Integer32):
    """Custom type gs2326MSTI7RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI7RootCost_Type.__name__ = "Integer32"
_Gs2326MSTI7RootCost_Object = MibScalar
gs2326MSTI7RootCost = _Gs2326MSTI7RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 5),
    _Gs2326MSTI7RootCost_Type()
)
gs2326MSTI7RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7RootCost.setStatus("current")
_Gs2326MSTI7TopologyFlag_Type = DisplayString
_Gs2326MSTI7TopologyFlag_Object = MibScalar
gs2326MSTI7TopologyFlag = _Gs2326MSTI7TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 8),
    _Gs2326MSTI7TopologyFlag_Type()
)
gs2326MSTI7TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7TopologyFlag.setStatus("current")
_Gs2326MSTI7TopologyChangeCount_Type = Counter32
_Gs2326MSTI7TopologyChangeCount_Object = MibScalar
gs2326MSTI7TopologyChangeCount = _Gs2326MSTI7TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 9),
    _Gs2326MSTI7TopologyChangeCount_Type()
)
gs2326MSTI7TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7TopologyChangeCount.setStatus("current")
_Gs2326MSTI7TopologyChangeLast_Type = DisplayString
_Gs2326MSTI7TopologyChangeLast_Object = MibScalar
gs2326MSTI7TopologyChangeLast = _Gs2326MSTI7TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 1, 10),
    _Gs2326MSTI7TopologyChangeLast_Type()
)
gs2326MSTI7TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7TopologyChangeLast.setStatus("current")
_Gs2326MSTI7PortStateTable_Object = MibTable
gs2326MSTI7PortStateTable = _Gs2326MSTI7PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2)
)
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateTable.setStatus("current")
_Gs2326MSTI7PortStateEntry_Object = MibTableRow
gs2326MSTI7PortStateEntry = _Gs2326MSTI7PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1)
)
gs2326MSTI7PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326MSTI7PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateEntry.setStatus("current")


class _Gs2326MSTI7PortStateIndex_Type(Integer32):
    """Custom type gs2326MSTI7PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326MSTI7PortStateIndex_Type.__name__ = "Integer32"
_Gs2326MSTI7PortStateIndex_Object = MibTableColumn
gs2326MSTI7PortStateIndex = _Gs2326MSTI7PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 1),
    _Gs2326MSTI7PortStateIndex_Type()
)
gs2326MSTI7PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateIndex.setStatus("current")
_Gs2326MSTI7PortStatePort_Type = DisplayString
_Gs2326MSTI7PortStatePort_Object = MibTableColumn
gs2326MSTI7PortStatePort = _Gs2326MSTI7PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 2),
    _Gs2326MSTI7PortStatePort_Type()
)
gs2326MSTI7PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStatePort.setStatus("current")
_Gs2326MSTI7PortStatePortID_Type = DisplayString
_Gs2326MSTI7PortStatePortID_Object = MibTableColumn
gs2326MSTI7PortStatePortID = _Gs2326MSTI7PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 3),
    _Gs2326MSTI7PortStatePortID_Type()
)
gs2326MSTI7PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStatePortID.setStatus("current")
_Gs2326MSTI7PortStateRole_Type = DisplayString
_Gs2326MSTI7PortStateRole_Object = MibTableColumn
gs2326MSTI7PortStateRole = _Gs2326MSTI7PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 4),
    _Gs2326MSTI7PortStateRole_Type()
)
gs2326MSTI7PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateRole.setStatus("current")
_Gs2326MSTI7PortStateState_Type = DisplayString
_Gs2326MSTI7PortStateState_Object = MibTableColumn
gs2326MSTI7PortStateState = _Gs2326MSTI7PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 5),
    _Gs2326MSTI7PortStateState_Type()
)
gs2326MSTI7PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateState.setStatus("current")


class _Gs2326MSTI7PortStatePathCost_Type(Integer32):
    """Custom type gs2326MSTI7PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2326MSTI7PortStatePathCost_Type.__name__ = "Integer32"
_Gs2326MSTI7PortStatePathCost_Object = MibTableColumn
gs2326MSTI7PortStatePathCost = _Gs2326MSTI7PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 6),
    _Gs2326MSTI7PortStatePathCost_Type()
)
gs2326MSTI7PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStatePathCost.setStatus("current")
_Gs2326MSTI7PortStateEdge_Type = DisplayString
_Gs2326MSTI7PortStateEdge_Object = MibTableColumn
gs2326MSTI7PortStateEdge = _Gs2326MSTI7PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 7),
    _Gs2326MSTI7PortStateEdge_Type()
)
gs2326MSTI7PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateEdge.setStatus("current")
_Gs2326MSTI7PortStatePoint2Point_Type = DisplayString
_Gs2326MSTI7PortStatePoint2Point_Object = MibTableColumn
gs2326MSTI7PortStatePoint2Point = _Gs2326MSTI7PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 8),
    _Gs2326MSTI7PortStatePoint2Point_Type()
)
gs2326MSTI7PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStatePoint2Point.setStatus("current")
_Gs2326MSTI7PortStateUptime_Type = DisplayString
_Gs2326MSTI7PortStateUptime_Object = MibTableColumn
gs2326MSTI7PortStateUptime = _Gs2326MSTI7PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 8, 8, 2, 1, 9),
    _Gs2326MSTI7PortStateUptime_Type()
)
gs2326MSTI7PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326MSTI7PortStateUptime.setStatus("current")
_Gs2326STPPortStatusTable_Object = MibTable
gs2326STPPortStatusTable = _Gs2326STPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 9)
)
if mibBuilder.loadTexts:
    gs2326STPPortStatusTable.setStatus("current")
_Gs2326STPPortStatusEntry_Object = MibTableRow
gs2326STPPortStatusEntry = _Gs2326STPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 9, 1)
)
gs2326STPPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPPortStatusPort"),
)
if mibBuilder.loadTexts:
    gs2326STPPortStatusEntry.setStatus("current")


class _Gs2326STPPortStatusPort_Type(Integer32):
    """Custom type gs2326STPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPPortStatusPort_Type.__name__ = "Integer32"
_Gs2326STPPortStatusPort_Object = MibTableColumn
gs2326STPPortStatusPort = _Gs2326STPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 9, 1, 1),
    _Gs2326STPPortStatusPort_Type()
)
gs2326STPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPPortStatusPort.setStatus("current")
_Gs2326STPPortStatusCISTRole_Type = DisplayString
_Gs2326STPPortStatusCISTRole_Object = MibTableColumn
gs2326STPPortStatusCISTRole = _Gs2326STPPortStatusCISTRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 9, 1, 2),
    _Gs2326STPPortStatusCISTRole_Type()
)
gs2326STPPortStatusCISTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPPortStatusCISTRole.setStatus("current")
_Gs2326STPPortStatusCISTState_Type = DisplayString
_Gs2326STPPortStatusCISTState_Object = MibTableColumn
gs2326STPPortStatusCISTState = _Gs2326STPPortStatusCISTState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 9, 1, 3),
    _Gs2326STPPortStatusCISTState_Type()
)
gs2326STPPortStatusCISTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPPortStatusCISTState.setStatus("current")
_Gs2326STPPortStatusUptime_Type = DisplayString
_Gs2326STPPortStatusUptime_Object = MibTableColumn
gs2326STPPortStatusUptime = _Gs2326STPPortStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 9, 1, 4),
    _Gs2326STPPortStatusUptime_Type()
)
gs2326STPPortStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPPortStatusUptime.setStatus("current")
_Gs2326STPPortStatisticsTable_Object = MibTable
gs2326STPPortStatisticsTable = _Gs2326STPPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10)
)
if mibBuilder.loadTexts:
    gs2326STPPortStatisticsTable.setStatus("current")
_Gs2326STPPortStatisticsEntry_Object = MibTableRow
gs2326STPPortStatisticsEntry = _Gs2326STPPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1)
)
gs2326STPPortStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326STPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gs2326STPPortStatisticsEntry.setStatus("current")


class _Gs2326STPStatisticsIndex_Type(Integer32):
    """Custom type gs2326STPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326STPStatisticsIndex_Type.__name__ = "Integer32"
_Gs2326STPStatisticsIndex_Object = MibTableColumn
gs2326STPStatisticsIndex = _Gs2326STPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 1),
    _Gs2326STPStatisticsIndex_Type()
)
gs2326STPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPStatisticsIndex.setStatus("current")
_Gs2326STPStatisticsPort_Type = DisplayString
_Gs2326STPStatisticsPort_Object = MibTableColumn
gs2326STPStatisticsPort = _Gs2326STPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 2),
    _Gs2326STPStatisticsPort_Type()
)
gs2326STPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326STPStatisticsPort.setStatus("current")
_Gs2326STPStatisticsTxMSTP_Type = Counter32
_Gs2326STPStatisticsTxMSTP_Object = MibTableColumn
gs2326STPStatisticsTxMSTP = _Gs2326STPStatisticsTxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 3),
    _Gs2326STPStatisticsTxMSTP_Type()
)
gs2326STPStatisticsTxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsTxMSTP.setStatus("current")
_Gs2326STPStatisticsTxRSTP_Type = Counter32
_Gs2326STPStatisticsTxRSTP_Object = MibTableColumn
gs2326STPStatisticsTxRSTP = _Gs2326STPStatisticsTxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 4),
    _Gs2326STPStatisticsTxRSTP_Type()
)
gs2326STPStatisticsTxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsTxRSTP.setStatus("current")
_Gs2326STPStatisticsTxSTP_Type = Counter32
_Gs2326STPStatisticsTxSTP_Object = MibTableColumn
gs2326STPStatisticsTxSTP = _Gs2326STPStatisticsTxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 5),
    _Gs2326STPStatisticsTxSTP_Type()
)
gs2326STPStatisticsTxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsTxSTP.setStatus("current")
_Gs2326STPStatisticsTxTCN_Type = Counter32
_Gs2326STPStatisticsTxTCN_Object = MibTableColumn
gs2326STPStatisticsTxTCN = _Gs2326STPStatisticsTxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 6),
    _Gs2326STPStatisticsTxTCN_Type()
)
gs2326STPStatisticsTxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsTxTCN.setStatus("current")
_Gs2326STPStatisticsRxMSTP_Type = Counter32
_Gs2326STPStatisticsRxMSTP_Object = MibTableColumn
gs2326STPStatisticsRxMSTP = _Gs2326STPStatisticsRxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 7),
    _Gs2326STPStatisticsRxMSTP_Type()
)
gs2326STPStatisticsRxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsRxMSTP.setStatus("current")
_Gs2326STPStatisticsRxRSTP_Type = Counter32
_Gs2326STPStatisticsRxRSTP_Object = MibTableColumn
gs2326STPStatisticsRxRSTP = _Gs2326STPStatisticsRxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 8),
    _Gs2326STPStatisticsRxRSTP_Type()
)
gs2326STPStatisticsRxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsRxRSTP.setStatus("current")
_Gs2326STPStatisticsRxSTP_Type = Counter32
_Gs2326STPStatisticsRxSTP_Object = MibTableColumn
gs2326STPStatisticsRxSTP = _Gs2326STPStatisticsRxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 9),
    _Gs2326STPStatisticsRxSTP_Type()
)
gs2326STPStatisticsRxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsRxSTP.setStatus("current")
_Gs2326STPStatisticsRxTCN_Type = Counter32
_Gs2326STPStatisticsRxTCN_Object = MibTableColumn
gs2326STPStatisticsRxTCN = _Gs2326STPStatisticsRxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 10),
    _Gs2326STPStatisticsRxTCN_Type()
)
gs2326STPStatisticsRxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsRxTCN.setStatus("current")
_Gs2326STPStatisticsDiscardedUnknown_Type = Counter32
_Gs2326STPStatisticsDiscardedUnknown_Object = MibTableColumn
gs2326STPStatisticsDiscardedUnknown = _Gs2326STPStatisticsDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 11),
    _Gs2326STPStatisticsDiscardedUnknown_Type()
)
gs2326STPStatisticsDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsDiscardedUnknown.setStatus("current")
_Gs2326STPStatisticsDiscardedIllegal_Type = Counter32
_Gs2326STPStatisticsDiscardedIllegal_Object = MibTableColumn
gs2326STPStatisticsDiscardedIllegal = _Gs2326STPStatisticsDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 20, 10, 1, 12),
    _Gs2326STPStatisticsDiscardedIllegal_Type()
)
gs2326STPStatisticsDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326STPStatisticsDiscardedIllegal.setStatus("current")
_Gs2326FilteringDataBase_ObjectIdentity = ObjectIdentity
gs2326FilteringDataBase = _Gs2326FilteringDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21)
)
_Gs2326FilteringDataBaseConfig_ObjectIdentity = ObjectIdentity
gs2326FilteringDataBaseConfig = _Gs2326FilteringDataBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1)
)


class _Gs2326FilteringDataBaseAgingTime_Type(Integer32):
    """Custom type gs2326FilteringDataBaseAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2326FilteringDataBaseAgingTime_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseAgingTime_Object = MibScalar
gs2326FilteringDataBaseAgingTime = _Gs2326FilteringDataBaseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 1),
    _Gs2326FilteringDataBaseAgingTime_Type()
)
gs2326FilteringDataBaseAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseAgingTime.setStatus("current")
_Gs2326FilteringDataBaseConfigTable_Object = MibTable
gs2326FilteringDataBaseConfigTable = _Gs2326FilteringDataBaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseConfigTable.setStatus("current")
_Gs2326FilteringDataBaseConfigEntry_Object = MibTableRow
gs2326FilteringDataBaseConfigEntry = _Gs2326FilteringDataBaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 2, 1)
)
gs2326FilteringDataBaseConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326FilteringDataBaseConfigPort"),
)
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseConfigEntry.setStatus("current")


class _Gs2326FilteringDataBaseConfigPort_Type(Integer32):
    """Custom type gs2326FilteringDataBaseConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326FilteringDataBaseConfigPort_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseConfigPort_Object = MibTableColumn
gs2326FilteringDataBaseConfigPort = _Gs2326FilteringDataBaseConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 2, 1, 1),
    _Gs2326FilteringDataBaseConfigPort_Type()
)
gs2326FilteringDataBaseConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseConfigPort.setStatus("current")


class _Gs2326FilteringDataBaseConfigLearning_Type(Integer32):
    """Custom type gs2326FilteringDataBaseConfigLearning based on Integer32"""
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


_Gs2326FilteringDataBaseConfigLearning_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseConfigLearning_Object = MibTableColumn
gs2326FilteringDataBaseConfigLearning = _Gs2326FilteringDataBaseConfigLearning_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 2, 1, 2),
    _Gs2326FilteringDataBaseConfigLearning_Type()
)
gs2326FilteringDataBaseConfigLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseConfigLearning.setStatus("current")
_Gs2326FilteringDataBaseStaticMAC_ObjectIdentity = ObjectIdentity
gs2326FilteringDataBaseStaticMAC = _Gs2326FilteringDataBaseStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3)
)


class _Gs2326FilteringDataBaseStaticMACCreate_Type(Integer32):
    """Custom type gs2326FilteringDataBaseStaticMACCreate based on Integer32"""
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


_Gs2326FilteringDataBaseStaticMACCreate_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseStaticMACCreate_Object = MibScalar
gs2326FilteringDataBaseStaticMACCreate = _Gs2326FilteringDataBaseStaticMACCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 1),
    _Gs2326FilteringDataBaseStaticMACCreate_Type()
)
gs2326FilteringDataBaseStaticMACCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACCreate.setStatus("current")
_Gs2326FilteringDataBaseStaticMACTable_Object = MibTable
gs2326FilteringDataBaseStaticMACTable = _Gs2326FilteringDataBaseStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACTable.setStatus("current")
_Gs2326FilteringDataBaseStaticMACEntry_Object = MibTableRow
gs2326FilteringDataBaseStaticMACEntry = _Gs2326FilteringDataBaseStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2, 1)
)
gs2326FilteringDataBaseStaticMACEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326FilteringDataBaseStaticMACIndex"),
)
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACEntry.setStatus("current")


class _Gs2326FilteringDataBaseStaticMACIndex_Type(Integer32):
    """Custom type gs2326FilteringDataBaseStaticMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326FilteringDataBaseStaticMACIndex_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseStaticMACIndex_Object = MibTableColumn
gs2326FilteringDataBaseStaticMACIndex = _Gs2326FilteringDataBaseStaticMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2, 1, 1),
    _Gs2326FilteringDataBaseStaticMACIndex_Type()
)
gs2326FilteringDataBaseStaticMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACIndex.setStatus("current")


class _Gs2326FilteringDataBaseStaticMACVLANId_Type(Integer32):
    """Custom type gs2326FilteringDataBaseStaticMACVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326FilteringDataBaseStaticMACVLANId_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseStaticMACVLANId_Object = MibTableColumn
gs2326FilteringDataBaseStaticMACVLANId = _Gs2326FilteringDataBaseStaticMACVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2, 1, 2),
    _Gs2326FilteringDataBaseStaticMACVLANId_Type()
)
gs2326FilteringDataBaseStaticMACVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACVLANId.setStatus("current")
_Gs2326FilteringDataBaseStaticMACAddress_Type = MacAddress
_Gs2326FilteringDataBaseStaticMACAddress_Object = MibTableColumn
gs2326FilteringDataBaseStaticMACAddress = _Gs2326FilteringDataBaseStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2, 1, 3),
    _Gs2326FilteringDataBaseStaticMACAddress_Type()
)
gs2326FilteringDataBaseStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACAddress.setStatus("current")
_Gs2326FilteringDataBaseStaticMACPortMembers_Type = DisplayString
_Gs2326FilteringDataBaseStaticMACPortMembers_Object = MibTableColumn
gs2326FilteringDataBaseStaticMACPortMembers = _Gs2326FilteringDataBaseStaticMACPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2, 1, 4),
    _Gs2326FilteringDataBaseStaticMACPortMembers_Type()
)
gs2326FilteringDataBaseStaticMACPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACPortMembers.setStatus("current")


class _Gs2326FilteringDataBaseStaticMACRowStatus_Type(Integer32):
    """Custom type gs2326FilteringDataBaseStaticMACRowStatus based on Integer32"""
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


_Gs2326FilteringDataBaseStaticMACRowStatus_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseStaticMACRowStatus_Object = MibTableColumn
gs2326FilteringDataBaseStaticMACRowStatus = _Gs2326FilteringDataBaseStaticMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 3, 2, 1, 5),
    _Gs2326FilteringDataBaseStaticMACRowStatus_Type()
)
gs2326FilteringDataBaseStaticMACRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseStaticMACRowStatus.setStatus("current")
_Gs2326FilteringDataBaseDynamicMACTable_Object = MibTable
gs2326FilteringDataBaseDynamicMACTable = _Gs2326FilteringDataBaseDynamicMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicMACTable.setStatus("current")
_Gs2326FilteringDataBaseDynamicMACEntry_Object = MibTableRow
gs2326FilteringDataBaseDynamicMACEntry = _Gs2326FilteringDataBaseDynamicMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4, 1)
)
gs2326FilteringDataBaseDynamicMACEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326FilteringDataBaseDynamicMACIndex"),
)
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicMACEntry.setStatus("current")


class _Gs2326FilteringDataBaseDynamicMACIndex_Type(Integer32):
    """Custom type gs2326FilteringDataBaseDynamicMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326FilteringDataBaseDynamicMACIndex_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseDynamicMACIndex_Object = MibTableColumn
gs2326FilteringDataBaseDynamicMACIndex = _Gs2326FilteringDataBaseDynamicMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4, 1, 1),
    _Gs2326FilteringDataBaseDynamicMACIndex_Type()
)
gs2326FilteringDataBaseDynamicMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicMACIndex.setStatus("current")


class _Gs2326FilteringDataBaseDynamicMACType_Type(Integer32):
    """Custom type gs2326FilteringDataBaseDynamicMACType based on Integer32"""
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


_Gs2326FilteringDataBaseDynamicMACType_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseDynamicMACType_Object = MibTableColumn
gs2326FilteringDataBaseDynamicMACType = _Gs2326FilteringDataBaseDynamicMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4, 1, 2),
    _Gs2326FilteringDataBaseDynamicMACType_Type()
)
gs2326FilteringDataBaseDynamicMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicMACType.setStatus("current")


class _Gs2326FilteringDataBaseDynamicMACVLAN_Type(Integer32):
    """Custom type gs2326FilteringDataBaseDynamicMACVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326FilteringDataBaseDynamicMACVLAN_Type.__name__ = "Integer32"
_Gs2326FilteringDataBaseDynamicMACVLAN_Object = MibTableColumn
gs2326FilteringDataBaseDynamicMACVLAN = _Gs2326FilteringDataBaseDynamicMACVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4, 1, 3),
    _Gs2326FilteringDataBaseDynamicMACVLAN_Type()
)
gs2326FilteringDataBaseDynamicMACVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicMACVLAN.setStatus("current")
_Gs2326FilteringDataBaseDynamicMACAddress_Type = MacAddress
_Gs2326FilteringDataBaseDynamicMACAddress_Object = MibTableColumn
gs2326FilteringDataBaseDynamicMACAddress = _Gs2326FilteringDataBaseDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4, 1, 4),
    _Gs2326FilteringDataBaseDynamicMACAddress_Type()
)
gs2326FilteringDataBaseDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicMACAddress.setStatus("current")
_Gs2326FilteringDataBaseDynamicPortMembers_Type = DisplayString
_Gs2326FilteringDataBaseDynamicPortMembers_Object = MibTableColumn
gs2326FilteringDataBaseDynamicPortMembers = _Gs2326FilteringDataBaseDynamicPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 21, 1, 4, 1, 5),
    _Gs2326FilteringDataBaseDynamicPortMembers_Type()
)
gs2326FilteringDataBaseDynamicPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326FilteringDataBaseDynamicPortMembers.setStatus("current")
_Gs2326SFlowAgent_ObjectIdentity = ObjectIdentity
gs2326SFlowAgent = _Gs2326SFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 22)
)
_Gs2326SFlowAgentCollector_ObjectIdentity = ObjectIdentity
gs2326SFlowAgentCollector = _Gs2326SFlowAgentCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 22, 1)
)


class _Gs2326SFlowAgentReceiverMode_Type(Integer32):
    """Custom type gs2326SFlowAgentReceiverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326SFlowAgentReceiverMode_Type.__name__ = "Integer32"
_Gs2326SFlowAgentReceiverMode_Object = MibScalar
gs2326SFlowAgentReceiverMode = _Gs2326SFlowAgentReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 22, 1, 1),
    _Gs2326SFlowAgentReceiverMode_Type()
)
gs2326SFlowAgentReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SFlowAgentReceiverMode.setStatus("current")
_Gs2326LMC_ObjectIdentity = ObjectIdentity
gs2326LMC = _Gs2326LMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500)
)


class _Gs2326LMCOperating_Type(Integer32):
    """Custom type gs2326LMCOperating based on Integer32"""
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


_Gs2326LMCOperating_Type.__name__ = "Integer32"
_Gs2326LMCOperating_Object = MibScalar
gs2326LMCOperating = _Gs2326LMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 1),
    _Gs2326LMCOperating_Type()
)
gs2326LMCOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LMCOperating.setStatus("current")


class _Gs2326LMCConfigViaDhcp_Type(Integer32):
    """Custom type gs2326LMCConfigViaDhcp based on Integer32"""
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


_Gs2326LMCConfigViaDhcp_Type.__name__ = "Integer32"
_Gs2326LMCConfigViaDhcp_Object = MibScalar
gs2326LMCConfigViaDhcp = _Gs2326LMCConfigViaDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 2),
    _Gs2326LMCConfigViaDhcp_Type()
)
gs2326LMCConfigViaDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LMCConfigViaDhcp.setStatus("current")


class _Gs2326LMCDomain_Type(DisplayString):
    """Custom type gs2326LMCDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gs2326LMCDomain_Type.__name__ = "DisplayString"
_Gs2326LMCDomain_Object = MibScalar
gs2326LMCDomain = _Gs2326LMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 3),
    _Gs2326LMCDomain_Type()
)
gs2326LMCDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LMCDomain.setStatus("current")


class _Gs2326LMCDhcpClientAutoRenew_Type(Integer32):
    """Custom type gs2326LMCDhcpClientAutoRenew based on Integer32"""
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


_Gs2326LMCDhcpClientAutoRenew_Type.__name__ = "Integer32"
_Gs2326LMCDhcpClientAutoRenew_Object = MibScalar
gs2326LMCDhcpClientAutoRenew = _Gs2326LMCDhcpClientAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 4),
    _Gs2326LMCDhcpClientAutoRenew_Type()
)
gs2326LMCDhcpClientAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LMCDhcpClientAutoRenew.setStatus("current")


class _Gs2326LMCZeroTouchSupport_Type(Integer32):
    """Custom type gs2326LMCZeroTouchSupport based on Integer32"""
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


_Gs2326LMCZeroTouchSupport_Type.__name__ = "Integer32"
_Gs2326LMCZeroTouchSupport_Object = MibScalar
gs2326LMCZeroTouchSupport = _Gs2326LMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 50),
    _Gs2326LMCZeroTouchSupport_Type()
)
gs2326LMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCZeroTouchSupport.setStatus("current")


class _Gs2326LMCPairingTokenPresent_Type(Integer32):
    """Custom type gs2326LMCPairingTokenPresent based on Integer32"""
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


_Gs2326LMCPairingTokenPresent_Type.__name__ = "Integer32"
_Gs2326LMCPairingTokenPresent_Object = MibScalar
gs2326LMCPairingTokenPresent = _Gs2326LMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 51),
    _Gs2326LMCPairingTokenPresent_Type()
)
gs2326LMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCPairingTokenPresent.setStatus("current")
_Gs2326LMCClientStatus_Type = DisplayString
_Gs2326LMCClientStatus_Object = MibScalar
gs2326LMCClientStatus = _Gs2326LMCClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 52),
    _Gs2326LMCClientStatus_Type()
)
gs2326LMCClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCClientStatus.setStatus("current")


class _Gs2326LMCManagementStatus_Type(Integer32):
    """Custom type gs2326LMCManagementStatus based on Integer32"""
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


_Gs2326LMCManagementStatus_Type.__name__ = "Integer32"
_Gs2326LMCManagementStatus_Object = MibScalar
gs2326LMCManagementStatus = _Gs2326LMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 53),
    _Gs2326LMCManagementStatus_Type()
)
gs2326LMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCManagementStatus.setStatus("current")


class _Gs2326LMCControlStatus_Type(Integer32):
    """Custom type gs2326LMCControlStatus based on Integer32"""
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


_Gs2326LMCControlStatus_Type.__name__ = "Integer32"
_Gs2326LMCControlStatus_Object = MibScalar
gs2326LMCControlStatus = _Gs2326LMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 54),
    _Gs2326LMCControlStatus_Type()
)
gs2326LMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCControlStatus.setStatus("current")


class _Gs2326LMCMonitoringStatus_Type(Integer32):
    """Custom type gs2326LMCMonitoringStatus based on Integer32"""
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


_Gs2326LMCMonitoringStatus_Type.__name__ = "Integer32"
_Gs2326LMCMonitoringStatus_Object = MibScalar
gs2326LMCMonitoringStatus = _Gs2326LMCMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 55),
    _Gs2326LMCMonitoringStatus_Type()
)
gs2326LMCMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCMonitoringStatus.setStatus("current")
_Gs2326LMCConfigurationSource_Type = DisplayString
_Gs2326LMCConfigurationSource_Object = MibScalar
gs2326LMCConfigurationSource = _Gs2326LMCConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 56),
    _Gs2326LMCConfigurationSource_Type()
)
gs2326LMCConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCConfigurationSource.setStatus("current")


class _Gs2326LMCConfigModified_Type(Integer32):
    """Custom type gs2326LMCConfigModified based on Integer32"""
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


_Gs2326LMCConfigModified_Type.__name__ = "Integer32"
_Gs2326LMCConfigModified_Object = MibScalar
gs2326LMCConfigModified = _Gs2326LMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 57),
    _Gs2326LMCConfigModified_Type()
)
gs2326LMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCConfigModified.setStatus("current")
_Gs2326LMCDeviceID_Type = DisplayString
_Gs2326LMCDeviceID_Object = MibScalar
gs2326LMCDeviceID = _Gs2326LMCDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 58),
    _Gs2326LMCDeviceID_Type()
)
gs2326LMCDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCDeviceID.setStatus("current")
_Gs2326LMCRoundTripTime_Type = Integer32
_Gs2326LMCRoundTripTime_Object = MibScalar
gs2326LMCRoundTripTime = _Gs2326LMCRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 2, 1500, 100),
    _Gs2326LMCRoundTripTime_Type()
)
gs2326LMCRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326LMCRoundTripTime.setStatus("current")
_Gs2326Security_ObjectIdentity = ObjectIdentity
gs2326Security = _Gs2326Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3)
)
_Gs2326IPSourceGuard_ObjectIdentity = ObjectIdentity
gs2326IPSourceGuard = _Gs2326IPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1)
)
_Gs2326IPSourceGuardConf_ObjectIdentity = ObjectIdentity
gs2326IPSourceGuardConf = _Gs2326IPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1)
)


class _Gs2326IPSourceGuardMode_Type(Integer32):
    """Custom type gs2326IPSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IPSourceGuardMode_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardMode_Object = MibScalar
gs2326IPSourceGuardMode = _Gs2326IPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1, 1),
    _Gs2326IPSourceGuardMode_Type()
)
gs2326IPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardMode.setStatus("current")
_Gs2326IPSourceGuardPortConfigTable_Object = MibTable
gs2326IPSourceGuardPortConfigTable = _Gs2326IPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326IPSourceGuardPortConfigTable.setStatus("current")
_Gs2326IPSourceGuardPortConfigEntry_Object = MibTableRow
gs2326IPSourceGuardPortConfigEntry = _Gs2326IPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1, 2, 1)
)
gs2326IPSourceGuardPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2326IPSourceGuardPortConfigEntry.setStatus("current")


class _Gs2326IPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type gs2326IPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardPortConfigPort_Object = MibTableColumn
gs2326IPSourceGuardPortConfigPort = _Gs2326IPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1, 2, 1, 1),
    _Gs2326IPSourceGuardPortConfigPort_Type()
)
gs2326IPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardPortConfigPort.setStatus("current")


class _Gs2326IPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type gs2326IPSourceGuardPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326IPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardPortConfigMode_Object = MibTableColumn
gs2326IPSourceGuardPortConfigMode = _Gs2326IPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1, 2, 1, 2),
    _Gs2326IPSourceGuardPortConfigMode_Type()
)
gs2326IPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardPortConfigMode.setStatus("current")


class _Gs2326IPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type gs2326IPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Gs2326IPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
gs2326IPSourceGuardPortMaxDynamicClients = _Gs2326IPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 1, 2, 1, 3),
    _Gs2326IPSourceGuardPortMaxDynamicClients_Type()
)
gs2326IPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardPortMaxDynamicClients.setStatus("current")
_Gs2326IPSourceGuardStatic_ObjectIdentity = ObjectIdentity
gs2326IPSourceGuardStatic = _Gs2326IPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2)
)


class _Gs2326IPSourceGuardStaticCreate_Type(Integer32):
    """Custom type gs2326IPSourceGuardStaticCreate based on Integer32"""
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


_Gs2326IPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardStaticCreate_Object = MibScalar
gs2326IPSourceGuardStaticCreate = _Gs2326IPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 1),
    _Gs2326IPSourceGuardStaticCreate_Type()
)
gs2326IPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticCreate.setStatus("current")
_Gs2326IPSourceGuardStaticTable_Object = MibTable
gs2326IPSourceGuardStaticTable = _Gs2326IPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticTable.setStatus("current")
_Gs2326IPSourceGuardStaticEntry_Object = MibTableRow
gs2326IPSourceGuardStaticEntry = _Gs2326IPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1)
)
gs2326IPSourceGuardStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticEntry.setStatus("current")


class _Gs2326IPSourceGuardStaticIndex_Type(Integer32):
    """Custom type gs2326IPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Gs2326IPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardStaticIndex_Object = MibTableColumn
gs2326IPSourceGuardStaticIndex = _Gs2326IPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1, 1),
    _Gs2326IPSourceGuardStaticIndex_Type()
)
gs2326IPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticIndex.setStatus("current")


class _Gs2326IPSourceGuardStaticPort_Type(Integer32):
    """Custom type gs2326IPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardStaticPort_Object = MibTableColumn
gs2326IPSourceGuardStaticPort = _Gs2326IPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1, 2),
    _Gs2326IPSourceGuardStaticPort_Type()
)
gs2326IPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticPort.setStatus("current")


class _Gs2326IPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type gs2326IPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326IPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardStaticVLANId_Object = MibTableColumn
gs2326IPSourceGuardStaticVLANId = _Gs2326IPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1, 3),
    _Gs2326IPSourceGuardStaticVLANId_Type()
)
gs2326IPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticVLANId.setStatus("current")
_Gs2326IPSourceGuardStaticIPAddress_Type = IpAddress
_Gs2326IPSourceGuardStaticIPAddress_Object = MibTableColumn
gs2326IPSourceGuardStaticIPAddress = _Gs2326IPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1, 4),
    _Gs2326IPSourceGuardStaticIPAddress_Type()
)
gs2326IPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticIPAddress.setStatus("current")
_Gs2326IPSourceGuardStaticMACAddress_Type = MacAddress
_Gs2326IPSourceGuardStaticMACAddress_Object = MibTableColumn
gs2326IPSourceGuardStaticMACAddress = _Gs2326IPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1, 5),
    _Gs2326IPSourceGuardStaticMACAddress_Type()
)
gs2326IPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticMACAddress.setStatus("current")


class _Gs2326IPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type gs2326IPSourceGuardStaticRowStatus based on Integer32"""
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


_Gs2326IPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardStaticRowStatus_Object = MibTableColumn
gs2326IPSourceGuardStaticRowStatus = _Gs2326IPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 2, 2, 1, 6),
    _Gs2326IPSourceGuardStaticRowStatus_Type()
)
gs2326IPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardStaticRowStatus.setStatus("current")
_Gs2326IPSourceGuardDynamicTable_Object = MibTable
gs2326IPSourceGuardDynamicTable = _Gs2326IPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3)
)
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicTable.setStatus("current")
_Gs2326IPSourceGuardDynamicEntry_Object = MibTableRow
gs2326IPSourceGuardDynamicEntry = _Gs2326IPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3, 1)
)
gs2326IPSourceGuardDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326IPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicEntry.setStatus("current")


class _Gs2326IPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type gs2326IPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326IPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardDynamicIndex_Object = MibTableColumn
gs2326IPSourceGuardDynamicIndex = _Gs2326IPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3, 1, 1),
    _Gs2326IPSourceGuardDynamicIndex_Type()
)
gs2326IPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicIndex.setStatus("current")


class _Gs2326IPSourceGuardDynamicPort_Type(Integer32):
    """Custom type gs2326IPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2326IPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardDynamicPort_Object = MibTableColumn
gs2326IPSourceGuardDynamicPort = _Gs2326IPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3, 1, 2),
    _Gs2326IPSourceGuardDynamicPort_Type()
)
gs2326IPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicPort.setStatus("current")


class _Gs2326IPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type gs2326IPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326IPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Gs2326IPSourceGuardDynamicVLANId_Object = MibTableColumn
gs2326IPSourceGuardDynamicVLANId = _Gs2326IPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3, 1, 3),
    _Gs2326IPSourceGuardDynamicVLANId_Type()
)
gs2326IPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicVLANId.setStatus("current")
_Gs2326IPSourceGuardDynamicIPAddress_Type = IpAddress
_Gs2326IPSourceGuardDynamicIPAddress_Object = MibTableColumn
gs2326IPSourceGuardDynamicIPAddress = _Gs2326IPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3, 1, 4),
    _Gs2326IPSourceGuardDynamicIPAddress_Type()
)
gs2326IPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicIPAddress.setStatus("current")
_Gs2326IPSourceGuardDynamicMACAddress_Type = MacAddress
_Gs2326IPSourceGuardDynamicMACAddress_Object = MibTableColumn
gs2326IPSourceGuardDynamicMACAddress = _Gs2326IPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 1, 3, 1, 5),
    _Gs2326IPSourceGuardDynamicMACAddress_Type()
)
gs2326IPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326IPSourceGuardDynamicMACAddress.setStatus("current")
_Gs2326ARPInspection_ObjectIdentity = ObjectIdentity
gs2326ARPInspection = _Gs2326ARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2)
)
_Gs2326ARPInspectionConf_ObjectIdentity = ObjectIdentity
gs2326ARPInspectionConf = _Gs2326ARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 1)
)


class _Gs2326ARPInspectionConfMode_Type(Integer32):
    """Custom type gs2326ARPInspectionConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPInspectionConfMode_Type.__name__ = "Integer32"
_Gs2326ARPInspectionConfMode_Object = MibScalar
gs2326ARPInspectionConfMode = _Gs2326ARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 1, 1),
    _Gs2326ARPInspectionConfMode_Type()
)
gs2326ARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionConfMode.setStatus("current")
_Gs2326ARPInspectionConfTable_Object = MibTable
gs2326ARPInspectionConfTable = _Gs2326ARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326ARPInspectionConfTable.setStatus("current")
_Gs2326ARPInspectionConfEntry_Object = MibTableRow
gs2326ARPInspectionConfEntry = _Gs2326ARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 1, 2, 1)
)
gs2326ARPInspectionConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    gs2326ARPInspectionConfEntry.setStatus("current")


class _Gs2326ARPInspectionConfPortIndex_Type(Integer32):
    """Custom type gs2326ARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Gs2326ARPInspectionConfPortIndex_Object = MibTableColumn
gs2326ARPInspectionConfPortIndex = _Gs2326ARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 1, 2, 1, 1),
    _Gs2326ARPInspectionConfPortIndex_Type()
)
gs2326ARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ARPInspectionConfPortIndex.setStatus("current")


class _Gs2326ARPInspectionConfPortMode_Type(Integer32):
    """Custom type gs2326ARPInspectionConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Gs2326ARPInspectionConfPortMode_Object = MibTableColumn
gs2326ARPInspectionConfPortMode = _Gs2326ARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 1, 2, 1, 2),
    _Gs2326ARPInspectionConfPortMode_Type()
)
gs2326ARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionConfPortMode.setStatus("current")
_Gs2326ARPInspectionStatic_ObjectIdentity = ObjectIdentity
gs2326ARPInspectionStatic = _Gs2326ARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2)
)


class _Gs2326ARPInspectionStaticCreate_Type(Integer32):
    """Custom type gs2326ARPInspectionStaticCreate based on Integer32"""
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


_Gs2326ARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Gs2326ARPInspectionStaticCreate_Object = MibScalar
gs2326ARPInspectionStaticCreate = _Gs2326ARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 1),
    _Gs2326ARPInspectionStaticCreate_Type()
)
gs2326ARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticCreate.setStatus("current")
_Gs2326ARPInspectionStaticTable_Object = MibTable
gs2326ARPInspectionStaticTable = _Gs2326ARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticTable.setStatus("current")
_Gs2326ARPInspectionStaticEntry_Object = MibTableRow
gs2326ARPInspectionStaticEntry = _Gs2326ARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1)
)
gs2326ARPInspectionStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticEntry.setStatus("current")


class _Gs2326ARPInspectionStaticIndex_Type(Integer32):
    """Custom type gs2326ARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Gs2326ARPInspectionStaticIndex_Object = MibTableColumn
gs2326ARPInspectionStaticIndex = _Gs2326ARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1, 1),
    _Gs2326ARPInspectionStaticIndex_Type()
)
gs2326ARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticIndex.setStatus("current")


class _Gs2326ARPInspectionStaticPort_Type(Integer32):
    """Custom type gs2326ARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPInspectionStaticPort_Type.__name__ = "Integer32"
_Gs2326ARPInspectionStaticPort_Object = MibTableColumn
gs2326ARPInspectionStaticPort = _Gs2326ARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1, 2),
    _Gs2326ARPInspectionStaticPort_Type()
)
gs2326ARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticPort.setStatus("current")


class _Gs2326ARPInspectionStaticVLANId_Type(Integer32):
    """Custom type gs2326ARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326ARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Gs2326ARPInspectionStaticVLANId_Object = MibTableColumn
gs2326ARPInspectionStaticVLANId = _Gs2326ARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1, 3),
    _Gs2326ARPInspectionStaticVLANId_Type()
)
gs2326ARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticVLANId.setStatus("current")
_Gs2326ARPInspectionStaticIPAddress_Type = IpAddress
_Gs2326ARPInspectionStaticIPAddress_Object = MibTableColumn
gs2326ARPInspectionStaticIPAddress = _Gs2326ARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1, 4),
    _Gs2326ARPInspectionStaticIPAddress_Type()
)
gs2326ARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticIPAddress.setStatus("current")
_Gs2326ARPInspectionStaticMACAddress_Type = MacAddress
_Gs2326ARPInspectionStaticMACAddress_Object = MibTableColumn
gs2326ARPInspectionStaticMACAddress = _Gs2326ARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1, 5),
    _Gs2326ARPInspectionStaticMACAddress_Type()
)
gs2326ARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticMACAddress.setStatus("current")


class _Gs2326ARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type gs2326ARPInspectionStaticRowStatus based on Integer32"""
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


_Gs2326ARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Gs2326ARPInspectionStaticRowStatus_Object = MibTableColumn
gs2326ARPInspectionStaticRowStatus = _Gs2326ARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 2, 2, 1, 6),
    _Gs2326ARPInspectionStaticRowStatus_Type()
)
gs2326ARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPInspectionStaticRowStatus.setStatus("current")
_Gs2326ARPInspectionDynamicTable_Object = MibTable
gs2326ARPInspectionDynamicTable = _Gs2326ARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicTable.setStatus("current")
_Gs2326ARPInspectionDynamicEntry_Object = MibTableRow
gs2326ARPInspectionDynamicEntry = _Gs2326ARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3, 1)
)
gs2326ARPInspectionDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicEntry.setStatus("current")


class _Gs2326ARPInspectionDynamicIndex_Type(Integer32):
    """Custom type gs2326ARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Gs2326ARPInspectionDynamicIndex_Object = MibTableColumn
gs2326ARPInspectionDynamicIndex = _Gs2326ARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3, 1, 1),
    _Gs2326ARPInspectionDynamicIndex_Type()
)
gs2326ARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicIndex.setStatus("current")


class _Gs2326ARPInspectionDynamicPort_Type(Integer32):
    """Custom type gs2326ARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Gs2326ARPInspectionDynamicPort_Object = MibTableColumn
gs2326ARPInspectionDynamicPort = _Gs2326ARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3, 1, 2),
    _Gs2326ARPInspectionDynamicPort_Type()
)
gs2326ARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicPort.setStatus("current")


class _Gs2326ARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type gs2326ARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326ARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Gs2326ARPInspectionDynamicVLANId_Object = MibTableColumn
gs2326ARPInspectionDynamicVLANId = _Gs2326ARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3, 1, 3),
    _Gs2326ARPInspectionDynamicVLANId_Type()
)
gs2326ARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicVLANId.setStatus("current")
_Gs2326ARPInspectionDynamicIPAddress_Type = IpAddress
_Gs2326ARPInspectionDynamicIPAddress_Object = MibTableColumn
gs2326ARPInspectionDynamicIPAddress = _Gs2326ARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3, 1, 4),
    _Gs2326ARPInspectionDynamicIPAddress_Type()
)
gs2326ARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicIPAddress.setStatus("current")
_Gs2326ARPInspectionDynamicMACAddress_Type = MacAddress
_Gs2326ARPInspectionDynamicMACAddress_Object = MibTableColumn
gs2326ARPInspectionDynamicMACAddress = _Gs2326ARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 3, 1, 5),
    _Gs2326ARPInspectionDynamicMACAddress_Type()
)
gs2326ARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ARPInspectionDynamicMACAddress.setStatus("current")
_Gs2326ARPStaticGatewayCtrl_ObjectIdentity = ObjectIdentity
gs2326ARPStaticGatewayCtrl = _Gs2326ARPStaticGatewayCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6)
)
_Gs2326ARPStaticGatewayCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2326ARPStaticGatewayCtrlSystemConf = _Gs2326ARPStaticGatewayCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 1)
)


class _Gs2326ARPStaticGatewayCtrlMode_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPStaticGatewayCtrlMode_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlMode_Object = MibScalar
gs2326ARPStaticGatewayCtrlMode = _Gs2326ARPStaticGatewayCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 1, 1),
    _Gs2326ARPStaticGatewayCtrlMode_Type()
)
gs2326ARPStaticGatewayCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlMode.setStatus("current")


class _Gs2326ARPStaticGatewayCtrlCreate_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlCreate based on Integer32"""
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


_Gs2326ARPStaticGatewayCtrlCreate_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlCreate_Object = MibScalar
gs2326ARPStaticGatewayCtrlCreate = _Gs2326ARPStaticGatewayCtrlCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 2),
    _Gs2326ARPStaticGatewayCtrlCreate_Type()
)
gs2326ARPStaticGatewayCtrlCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlCreate.setStatus("current")
_Gs2326ARPStaticGatewayCtrlTable_Object = MibTable
gs2326ARPStaticGatewayCtrlTable = _Gs2326ARPStaticGatewayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlTable.setStatus("current")
_Gs2326ARPStaticGatewayCtrlEntry_Object = MibTableRow
gs2326ARPStaticGatewayCtrlEntry = _Gs2326ARPStaticGatewayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1)
)
gs2326ARPStaticGatewayCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ARPStaticGatewayCtrlIndex"),
)
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlEntry.setStatus("current")


class _Gs2326ARPStaticGatewayCtrlIndex_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2326ARPStaticGatewayCtrlIndex_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlIndex_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlIndex = _Gs2326ARPStaticGatewayCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 1),
    _Gs2326ARPStaticGatewayCtrlIndex_Type()
)
gs2326ARPStaticGatewayCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlIndex.setStatus("current")
_Gs2326ARPStaticGatewayCtrlIPAddress_Type = IpAddress
_Gs2326ARPStaticGatewayCtrlIPAddress_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlIPAddress = _Gs2326ARPStaticGatewayCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 2),
    _Gs2326ARPStaticGatewayCtrlIPAddress_Type()
)
gs2326ARPStaticGatewayCtrlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlIPAddress.setStatus("current")
_Gs2326ARPStaticGatewayCtrlMACAddress_Type = MacAddress
_Gs2326ARPStaticGatewayCtrlMACAddress_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlMACAddress = _Gs2326ARPStaticGatewayCtrlMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 3),
    _Gs2326ARPStaticGatewayCtrlMACAddress_Type()
)
gs2326ARPStaticGatewayCtrlMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlMACAddress.setStatus("current")


class _Gs2326ARPStaticGatewayCtrlPort_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPStaticGatewayCtrlPort_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlPort_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlPort = _Gs2326ARPStaticGatewayCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 4),
    _Gs2326ARPStaticGatewayCtrlPort_Type()
)
gs2326ARPStaticGatewayCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlPort.setStatus("current")


class _Gs2326ARPStaticGatewayCtrlAction_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlAction based on Integer32"""
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


_Gs2326ARPStaticGatewayCtrlAction_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlAction_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlAction = _Gs2326ARPStaticGatewayCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 5),
    _Gs2326ARPStaticGatewayCtrlAction_Type()
)
gs2326ARPStaticGatewayCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlAction.setStatus("current")
_Gs2326ARPStaticGatewayCtrlState_Type = DisplayString
_Gs2326ARPStaticGatewayCtrlState_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlState = _Gs2326ARPStaticGatewayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 6),
    _Gs2326ARPStaticGatewayCtrlState_Type()
)
gs2326ARPStaticGatewayCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlState.setStatus("current")


class _Gs2326ARPStaticGatewayCtrlReOpen_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlReOpen based on Integer32"""
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


_Gs2326ARPStaticGatewayCtrlReOpen_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlReOpen_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlReOpen = _Gs2326ARPStaticGatewayCtrlReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 7),
    _Gs2326ARPStaticGatewayCtrlReOpen_Type()
)
gs2326ARPStaticGatewayCtrlReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlReOpen.setStatus("current")


class _Gs2326ARPStaticGatewayCtrlRowStatus_Type(Integer32):
    """Custom type gs2326ARPStaticGatewayCtrlRowStatus based on Integer32"""
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


_Gs2326ARPStaticGatewayCtrlRowStatus_Type.__name__ = "Integer32"
_Gs2326ARPStaticGatewayCtrlRowStatus_Object = MibTableColumn
gs2326ARPStaticGatewayCtrlRowStatus = _Gs2326ARPStaticGatewayCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 6, 3, 1, 8),
    _Gs2326ARPStaticGatewayCtrlRowStatus_Type()
)
gs2326ARPStaticGatewayCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPStaticGatewayCtrlRowStatus.setStatus("current")
_Gs2326ARPSpoofingPrevention_ObjectIdentity = ObjectIdentity
gs2326ARPSpoofingPrevention = _Gs2326ARPSpoofingPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7)
)
_Gs2326ARPSpoofingPreventionSystemConf_ObjectIdentity = ObjectIdentity
gs2326ARPSpoofingPreventionSystemConf = _Gs2326ARPSpoofingPreventionSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 1)
)


class _Gs2326ARPSpoofingPreventionMode_Type(Integer32):
    """Custom type gs2326ARPSpoofingPreventionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPSpoofingPreventionMode_Type.__name__ = "Integer32"
_Gs2326ARPSpoofingPreventionMode_Object = MibScalar
gs2326ARPSpoofingPreventionMode = _Gs2326ARPSpoofingPreventionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 1, 1),
    _Gs2326ARPSpoofingPreventionMode_Type()
)
gs2326ARPSpoofingPreventionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionMode.setStatus("current")
_Gs2326ARPSpoofingPreventionTable_Object = MibTable
gs2326ARPSpoofingPreventionTable = _Gs2326ARPSpoofingPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionTable.setStatus("current")
_Gs2326ARPSpoofingPreventionEntry_Object = MibTableRow
gs2326ARPSpoofingPreventionEntry = _Gs2326ARPSpoofingPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1)
)
gs2326ARPSpoofingPreventionEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326ARPSpoofingPreventionPort"),
)
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionEntry.setStatus("current")


class _Gs2326ARPSpoofingPreventionPort_Type(Integer32):
    """Custom type gs2326ARPSpoofingPreventionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326ARPSpoofingPreventionPort_Type.__name__ = "Integer32"
_Gs2326ARPSpoofingPreventionPort_Object = MibTableColumn
gs2326ARPSpoofingPreventionPort = _Gs2326ARPSpoofingPreventionPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1, 1),
    _Gs2326ARPSpoofingPreventionPort_Type()
)
gs2326ARPSpoofingPreventionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionPort.setStatus("current")


class _Gs2326ARPSpoofingPreventionPortMode_Type(Integer32):
    """Custom type gs2326ARPSpoofingPreventionPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPSpoofingPreventionPortMode_Type.__name__ = "Integer32"
_Gs2326ARPSpoofingPreventionPortMode_Object = MibTableColumn
gs2326ARPSpoofingPreventionPortMode = _Gs2326ARPSpoofingPreventionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1, 2),
    _Gs2326ARPSpoofingPreventionPortMode_Type()
)
gs2326ARPSpoofingPreventionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionPortMode.setStatus("current")


class _Gs2326ARPSpoofingPreventionPortLimit_Type(Integer32):
    """Custom type gs2326ARPSpoofingPreventionPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Gs2326ARPSpoofingPreventionPortLimit_Type.__name__ = "Integer32"
_Gs2326ARPSpoofingPreventionPortLimit_Object = MibTableColumn
gs2326ARPSpoofingPreventionPortLimit = _Gs2326ARPSpoofingPreventionPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1, 3),
    _Gs2326ARPSpoofingPreventionPortLimit_Type()
)
gs2326ARPSpoofingPreventionPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionPortLimit.setStatus("current")


class _Gs2326ARPSpoofingPreventionPortAction_Type(Integer32):
    """Custom type gs2326ARPSpoofingPreventionPortAction based on Integer32"""
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


_Gs2326ARPSpoofingPreventionPortAction_Type.__name__ = "Integer32"
_Gs2326ARPSpoofingPreventionPortAction_Object = MibTableColumn
gs2326ARPSpoofingPreventionPortAction = _Gs2326ARPSpoofingPreventionPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1, 4),
    _Gs2326ARPSpoofingPreventionPortAction_Type()
)
gs2326ARPSpoofingPreventionPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionPortAction.setStatus("current")
_Gs2326ARPSpoofingPreventionPortState_Type = DisplayString
_Gs2326ARPSpoofingPreventionPortState_Object = MibTableColumn
gs2326ARPSpoofingPreventionPortState = _Gs2326ARPSpoofingPreventionPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1, 5),
    _Gs2326ARPSpoofingPreventionPortState_Type()
)
gs2326ARPSpoofingPreventionPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionPortState.setStatus("current")


class _Gs2326ARPSpoofingPreventionPortReOpen_Type(Integer32):
    """Custom type gs2326ARPSpoofingPreventionPortReOpen based on Integer32"""
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


_Gs2326ARPSpoofingPreventionPortReOpen_Type.__name__ = "Integer32"
_Gs2326ARPSpoofingPreventionPortReOpen_Object = MibTableColumn
gs2326ARPSpoofingPreventionPortReOpen = _Gs2326ARPSpoofingPreventionPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 7, 2, 1, 6),
    _Gs2326ARPSpoofingPreventionPortReOpen_Type()
)
gs2326ARPSpoofingPreventionPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPSpoofingPreventionPortReOpen.setStatus("current")
_Gs2326ARPIPDoSPrevention_ObjectIdentity = ObjectIdentity
gs2326ARPIPDoSPrevention = _Gs2326ARPIPDoSPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8)
)


class _Gs2326ARPIPDoSPreventionTCPMode_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionTCPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPIPDoSPreventionTCPMode_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionTCPMode_Object = MibScalar
gs2326ARPIPDoSPreventionTCPMode = _Gs2326ARPIPDoSPreventionTCPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 1),
    _Gs2326ARPIPDoSPreventionTCPMode_Type()
)
gs2326ARPIPDoSPreventionTCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionTCPMode.setStatus("current")


class _Gs2326ARPIPDoSPreventionUDPMode_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionUDPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPIPDoSPreventionUDPMode_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionUDPMode_Object = MibScalar
gs2326ARPIPDoSPreventionUDPMode = _Gs2326ARPIPDoSPreventionUDPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 2),
    _Gs2326ARPIPDoSPreventionUDPMode_Type()
)
gs2326ARPIPDoSPreventionUDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionUDPMode.setStatus("current")


class _Gs2326ARPIPDoSPreventionICMPMode_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionICMPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ARPIPDoSPreventionICMPMode_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionICMPMode_Object = MibScalar
gs2326ARPIPDoSPreventionICMPMode = _Gs2326ARPIPDoSPreventionICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 3),
    _Gs2326ARPIPDoSPreventionICMPMode_Type()
)
gs2326ARPIPDoSPreventionICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionICMPMode.setStatus("current")


class _Gs2326ARPIPDoSPreventionServerPort1_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionServerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2326ARPIPDoSPreventionServerPort1_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionServerPort1_Object = MibScalar
gs2326ARPIPDoSPreventionServerPort1 = _Gs2326ARPIPDoSPreventionServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 4),
    _Gs2326ARPIPDoSPreventionServerPort1_Type()
)
gs2326ARPIPDoSPreventionServerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionServerPort1.setStatus("current")


class _Gs2326ARPIPDoSPreventionServerPort2_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionServerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2326ARPIPDoSPreventionServerPort2_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionServerPort2_Object = MibScalar
gs2326ARPIPDoSPreventionServerPort2 = _Gs2326ARPIPDoSPreventionServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 5),
    _Gs2326ARPIPDoSPreventionServerPort2_Type()
)
gs2326ARPIPDoSPreventionServerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionServerPort2.setStatus("current")


class _Gs2326ARPIPDoSPreventionServerPort3_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionServerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2326ARPIPDoSPreventionServerPort3_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionServerPort3_Object = MibScalar
gs2326ARPIPDoSPreventionServerPort3 = _Gs2326ARPIPDoSPreventionServerPort3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 6),
    _Gs2326ARPIPDoSPreventionServerPort3_Type()
)
gs2326ARPIPDoSPreventionServerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionServerPort3.setStatus("current")


class _Gs2326ARPIPDoSPreventionServerPort4_Type(Integer32):
    """Custom type gs2326ARPIPDoSPreventionServerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2326ARPIPDoSPreventionServerPort4_Type.__name__ = "Integer32"
_Gs2326ARPIPDoSPreventionServerPort4_Object = MibScalar
gs2326ARPIPDoSPreventionServerPort4 = _Gs2326ARPIPDoSPreventionServerPort4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 2, 8, 7),
    _Gs2326ARPIPDoSPreventionServerPort4_Type()
)
gs2326ARPIPDoSPreventionServerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ARPIPDoSPreventionServerPort4.setStatus("current")
_Gs2326DHCPSnooping_ObjectIdentity = ObjectIdentity
gs2326DHCPSnooping = _Gs2326DHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3)
)
_Gs2326DHCPSnoopingConf_ObjectIdentity = ObjectIdentity
gs2326DHCPSnoopingConf = _Gs2326DHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 1)
)


class _Gs2326DHCPSnoopingMode_Type(Integer32):
    """Custom type gs2326DHCPSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326DHCPSnoopingMode_Type.__name__ = "Integer32"
_Gs2326DHCPSnoopingMode_Object = MibScalar
gs2326DHCPSnoopingMode = _Gs2326DHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 1, 1),
    _Gs2326DHCPSnoopingMode_Type()
)
gs2326DHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingMode.setStatus("current")
_Gs2326DHCPSnoopingPortModeConfigurationTable_Object = MibTable
gs2326DHCPSnoopingPortModeConfigurationTable = _Gs2326DHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Gs2326DHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
gs2326DHCPSnoopingPortModeConfigurationEntry = _Gs2326DHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 1, 2, 1)
)
gs2326DHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326DHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Gs2326DHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type gs2326DHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326DHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Gs2326DHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
gs2326DHCPSnoopingPortModeConfigurationPort = _Gs2326DHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 1, 2, 1, 1),
    _Gs2326DHCPSnoopingPortModeConfigurationPort_Type()
)
gs2326DHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Gs2326DHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type gs2326DHCPSnoopingPortModeConfigurationMode based on Integer32"""
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


_Gs2326DHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Gs2326DHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
gs2326DHCPSnoopingPortModeConfigurationMode = _Gs2326DHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 1, 2, 1, 2),
    _Gs2326DHCPSnoopingPortModeConfigurationMode_Type()
)
gs2326DHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Gs2326DHCPSnoopingStatisticsTable_Object = MibTable
gs2326DHCPSnoopingStatisticsTable = _Gs2326DHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingStatisticsTable.setStatus("current")
_Gs2326DHCPSnoopingStatisticsEntry_Object = MibTableRow
gs2326DHCPSnoopingStatisticsEntry = _Gs2326DHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1)
)
gs2326DHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326DHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingStatisticsEntry.setStatus("current")


class _Gs2326DHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type gs2326DHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326DHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Gs2326DHCPSnoopingStatisticsPort_Object = MibTableColumn
gs2326DHCPSnoopingStatisticsPort = _Gs2326DHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 1),
    _Gs2326DHCPSnoopingStatisticsPort_Type()
)
gs2326DHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingStatisticsPort.setStatus("current")


class _Gs2326DHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type gs2326DHCPSnoopingStatisticsClear based on Integer32"""
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


_Gs2326DHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Gs2326DHCPSnoopingStatisticsClear_Object = MibTableColumn
gs2326DHCPSnoopingStatisticsClear = _Gs2326DHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 2),
    _Gs2326DHCPSnoopingStatisticsClear_Type()
)
gs2326DHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingStatisticsClear.setStatus("current")
_Gs2326DHCPSnoopingRxDiscover_Type = Counter32
_Gs2326DHCPSnoopingRxDiscover_Object = MibTableColumn
gs2326DHCPSnoopingRxDiscover = _Gs2326DHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 3),
    _Gs2326DHCPSnoopingRxDiscover_Type()
)
gs2326DHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxDiscover.setStatus("current")
_Gs2326DHCPSnoopingRxOffer_Type = Counter32
_Gs2326DHCPSnoopingRxOffer_Object = MibTableColumn
gs2326DHCPSnoopingRxOffer = _Gs2326DHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 4),
    _Gs2326DHCPSnoopingRxOffer_Type()
)
gs2326DHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxOffer.setStatus("current")
_Gs2326DHCPSnoopingRxRequest_Type = Counter32
_Gs2326DHCPSnoopingRxRequest_Object = MibTableColumn
gs2326DHCPSnoopingRxRequest = _Gs2326DHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 5),
    _Gs2326DHCPSnoopingRxRequest_Type()
)
gs2326DHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxRequest.setStatus("current")
_Gs2326DHCPSnoopingRxDecline_Type = Counter32
_Gs2326DHCPSnoopingRxDecline_Object = MibTableColumn
gs2326DHCPSnoopingRxDecline = _Gs2326DHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 6),
    _Gs2326DHCPSnoopingRxDecline_Type()
)
gs2326DHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxDecline.setStatus("current")
_Gs2326DHCPSnoopingRxACK_Type = Counter32
_Gs2326DHCPSnoopingRxACK_Object = MibTableColumn
gs2326DHCPSnoopingRxACK = _Gs2326DHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 7),
    _Gs2326DHCPSnoopingRxACK_Type()
)
gs2326DHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxACK.setStatus("current")
_Gs2326DHCPSnoopingRxNAK_Type = Counter32
_Gs2326DHCPSnoopingRxNAK_Object = MibTableColumn
gs2326DHCPSnoopingRxNAK = _Gs2326DHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 8),
    _Gs2326DHCPSnoopingRxNAK_Type()
)
gs2326DHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxNAK.setStatus("current")
_Gs2326DHCPSnoopingRxRelease_Type = Counter32
_Gs2326DHCPSnoopingRxRelease_Object = MibTableColumn
gs2326DHCPSnoopingRxRelease = _Gs2326DHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 9),
    _Gs2326DHCPSnoopingRxRelease_Type()
)
gs2326DHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxRelease.setStatus("current")
_Gs2326DHCPSnoopingRxInform_Type = Counter32
_Gs2326DHCPSnoopingRxInform_Object = MibTableColumn
gs2326DHCPSnoopingRxInform = _Gs2326DHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 10),
    _Gs2326DHCPSnoopingRxInform_Type()
)
gs2326DHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxInform.setStatus("current")
_Gs2326DHCPSnoopingRxLeaseQuery_Type = Counter32
_Gs2326DHCPSnoopingRxLeaseQuery_Object = MibTableColumn
gs2326DHCPSnoopingRxLeaseQuery = _Gs2326DHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 11),
    _Gs2326DHCPSnoopingRxLeaseQuery_Type()
)
gs2326DHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxLeaseQuery.setStatus("current")
_Gs2326DHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Gs2326DHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
gs2326DHCPSnoopingRxLeaseUnassigned = _Gs2326DHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 12),
    _Gs2326DHCPSnoopingRxLeaseUnassigned_Type()
)
gs2326DHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Gs2326DHCPSnoopingRxLeaseUnknown_Type = Counter32
_Gs2326DHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
gs2326DHCPSnoopingRxLeaseUnknown = _Gs2326DHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 13),
    _Gs2326DHCPSnoopingRxLeaseUnknown_Type()
)
gs2326DHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxLeaseUnknown.setStatus("current")
_Gs2326DHCPSnoopingRxLeaseActive_Type = Counter32
_Gs2326DHCPSnoopingRxLeaseActive_Object = MibTableColumn
gs2326DHCPSnoopingRxLeaseActive = _Gs2326DHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 14),
    _Gs2326DHCPSnoopingRxLeaseActive_Type()
)
gs2326DHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingRxLeaseActive.setStatus("current")
_Gs2326DHCPSnoopingTxDiscover_Type = Counter32
_Gs2326DHCPSnoopingTxDiscover_Object = MibTableColumn
gs2326DHCPSnoopingTxDiscover = _Gs2326DHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 15),
    _Gs2326DHCPSnoopingTxDiscover_Type()
)
gs2326DHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxDiscover.setStatus("current")
_Gs2326DHCPSnoopingTxOffer_Type = Counter32
_Gs2326DHCPSnoopingTxOffer_Object = MibTableColumn
gs2326DHCPSnoopingTxOffer = _Gs2326DHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 16),
    _Gs2326DHCPSnoopingTxOffer_Type()
)
gs2326DHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxOffer.setStatus("current")
_Gs2326DHCPSnoopingTxRequest_Type = Counter32
_Gs2326DHCPSnoopingTxRequest_Object = MibTableColumn
gs2326DHCPSnoopingTxRequest = _Gs2326DHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 17),
    _Gs2326DHCPSnoopingTxRequest_Type()
)
gs2326DHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxRequest.setStatus("current")
_Gs2326DHCPSnoopingTxDecline_Type = Counter32
_Gs2326DHCPSnoopingTxDecline_Object = MibTableColumn
gs2326DHCPSnoopingTxDecline = _Gs2326DHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 18),
    _Gs2326DHCPSnoopingTxDecline_Type()
)
gs2326DHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxDecline.setStatus("current")
_Gs2326DHCPSnoopingTxACK_Type = Counter32
_Gs2326DHCPSnoopingTxACK_Object = MibTableColumn
gs2326DHCPSnoopingTxACK = _Gs2326DHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 19),
    _Gs2326DHCPSnoopingTxACK_Type()
)
gs2326DHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxACK.setStatus("current")
_Gs2326DHCPSnoopingTxNAK_Type = Counter32
_Gs2326DHCPSnoopingTxNAK_Object = MibTableColumn
gs2326DHCPSnoopingTxNAK = _Gs2326DHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 20),
    _Gs2326DHCPSnoopingTxNAK_Type()
)
gs2326DHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxNAK.setStatus("current")
_Gs2326DHCPSnoopingTxRelease_Type = Counter32
_Gs2326DHCPSnoopingTxRelease_Object = MibTableColumn
gs2326DHCPSnoopingTxRelease = _Gs2326DHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 21),
    _Gs2326DHCPSnoopingTxRelease_Type()
)
gs2326DHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxRelease.setStatus("current")
_Gs2326DHCPSnoopingTxInform_Type = Counter32
_Gs2326DHCPSnoopingTxInform_Object = MibTableColumn
gs2326DHCPSnoopingTxInform = _Gs2326DHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 22),
    _Gs2326DHCPSnoopingTxInform_Type()
)
gs2326DHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxInform.setStatus("current")
_Gs2326DHCPSnoopingTxLeaseQuery_Type = Counter32
_Gs2326DHCPSnoopingTxLeaseQuery_Object = MibTableColumn
gs2326DHCPSnoopingTxLeaseQuery = _Gs2326DHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 23),
    _Gs2326DHCPSnoopingTxLeaseQuery_Type()
)
gs2326DHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxLeaseQuery.setStatus("current")
_Gs2326DHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Gs2326DHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
gs2326DHCPSnoopingTxLeaseUnassigned = _Gs2326DHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 24),
    _Gs2326DHCPSnoopingTxLeaseUnassigned_Type()
)
gs2326DHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Gs2326DHCPSnoopingTxLeaseUnknown_Type = Counter32
_Gs2326DHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
gs2326DHCPSnoopingTxLeaseUnknown = _Gs2326DHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 25),
    _Gs2326DHCPSnoopingTxLeaseUnknown_Type()
)
gs2326DHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxLeaseUnknown.setStatus("current")
_Gs2326DHCPSnoopingTxLeaseActive_Type = Counter32
_Gs2326DHCPSnoopingTxLeaseActive_Object = MibTableColumn
gs2326DHCPSnoopingTxLeaseActive = _Gs2326DHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 3, 2, 1, 26),
    _Gs2326DHCPSnoopingTxLeaseActive_Type()
)
gs2326DHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326DHCPSnoopingTxLeaseActive.setStatus("current")
_Gs2326DHCPRelay_ObjectIdentity = ObjectIdentity
gs2326DHCPRelay = _Gs2326DHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4)
)
_Gs2326DHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
gs2326DHCPRelayConfiguration = _Gs2326DHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1)
)


class _Gs2326DHCPRelayMode_Type(Integer32):
    """Custom type gs2326DHCPRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326DHCPRelayMode_Type.__name__ = "Integer32"
_Gs2326DHCPRelayMode_Object = MibScalar
gs2326DHCPRelayMode = _Gs2326DHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 1),
    _Gs2326DHCPRelayMode_Type()
)
gs2326DHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayMode.setStatus("current")
_Gs2326DHCPRelayServer_Type = IpAddress
_Gs2326DHCPRelayServer_Object = MibScalar
gs2326DHCPRelayServer = _Gs2326DHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 2),
    _Gs2326DHCPRelayServer_Type()
)
gs2326DHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayServer.setStatus("current")


class _Gs2326DHCPRelayInformationMode_Type(Integer32):
    """Custom type gs2326DHCPRelayInformationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326DHCPRelayInformationMode_Type.__name__ = "Integer32"
_Gs2326DHCPRelayInformationMode_Object = MibScalar
gs2326DHCPRelayInformationMode = _Gs2326DHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 3),
    _Gs2326DHCPRelayInformationMode_Type()
)
gs2326DHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayInformationMode.setStatus("current")


class _Gs2326DHCPRelayInformationPolicy_Type(Integer32):
    """Custom type gs2326DHCPRelayInformationPolicy based on Integer32"""
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


_Gs2326DHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Gs2326DHCPRelayInformationPolicy_Object = MibScalar
gs2326DHCPRelayInformationPolicy = _Gs2326DHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 4),
    _Gs2326DHCPRelayInformationPolicy_Type()
)
gs2326DHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayInformationPolicy.setStatus("current")
_Gs2326DHCPRelayConfigurationGateways_ObjectIdentity = ObjectIdentity
gs2326DHCPRelayConfigurationGateways = _Gs2326DHCPRelayConfigurationGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5)
)


class _Gs2326DHCPRelayConfigurationGatewaysCreate_Type(Integer32):
    """Custom type gs2326DHCPRelayConfigurationGatewaysCreate based on Integer32"""
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


_Gs2326DHCPRelayConfigurationGatewaysCreate_Type.__name__ = "Integer32"
_Gs2326DHCPRelayConfigurationGatewaysCreate_Object = MibScalar
gs2326DHCPRelayConfigurationGatewaysCreate = _Gs2326DHCPRelayConfigurationGatewaysCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 1),
    _Gs2326DHCPRelayConfigurationGatewaysCreate_Type()
)
gs2326DHCPRelayConfigurationGatewaysCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysCreate.setStatus("current")
_Gs2326DHCPRelayConfigurationGatewaysTable_Object = MibTable
gs2326DHCPRelayConfigurationGatewaysTable = _Gs2326DHCPRelayConfigurationGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysTable.setStatus("current")
_Gs2326DHCPRelayConfigurationGatewaysEntry_Object = MibTableRow
gs2326DHCPRelayConfigurationGatewaysEntry = _Gs2326DHCPRelayConfigurationGatewaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 2, 1)
)
gs2326DHCPRelayConfigurationGatewaysEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326DHCPRelayConfigurationGatewaysIndex"),
)
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysEntry.setStatus("current")


class _Gs2326DHCPRelayConfigurationGatewaysIndex_Type(Integer32):
    """Custom type gs2326DHCPRelayConfigurationGatewaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2326DHCPRelayConfigurationGatewaysIndex_Type.__name__ = "Integer32"
_Gs2326DHCPRelayConfigurationGatewaysIndex_Object = MibTableColumn
gs2326DHCPRelayConfigurationGatewaysIndex = _Gs2326DHCPRelayConfigurationGatewaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 2, 1, 1),
    _Gs2326DHCPRelayConfigurationGatewaysIndex_Type()
)
gs2326DHCPRelayConfigurationGatewaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysIndex.setStatus("current")


class _Gs2326DHCPRelayConfigurationGatewaysVLANId_Type(Integer32):
    """Custom type gs2326DHCPRelayConfigurationGatewaysVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326DHCPRelayConfigurationGatewaysVLANId_Type.__name__ = "Integer32"
_Gs2326DHCPRelayConfigurationGatewaysVLANId_Object = MibTableColumn
gs2326DHCPRelayConfigurationGatewaysVLANId = _Gs2326DHCPRelayConfigurationGatewaysVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 2, 1, 2),
    _Gs2326DHCPRelayConfigurationGatewaysVLANId_Type()
)
gs2326DHCPRelayConfigurationGatewaysVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysVLANId.setStatus("current")
_Gs2326DHCPRelayConfigurationGatewaysIP_Type = IpAddress
_Gs2326DHCPRelayConfigurationGatewaysIP_Object = MibTableColumn
gs2326DHCPRelayConfigurationGatewaysIP = _Gs2326DHCPRelayConfigurationGatewaysIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 2, 1, 3),
    _Gs2326DHCPRelayConfigurationGatewaysIP_Type()
)
gs2326DHCPRelayConfigurationGatewaysIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysIP.setStatus("current")


class _Gs2326DHCPRelayConfigurationGatewaysRowStatus_Type(Integer32):
    """Custom type gs2326DHCPRelayConfigurationGatewaysRowStatus based on Integer32"""
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


_Gs2326DHCPRelayConfigurationGatewaysRowStatus_Type.__name__ = "Integer32"
_Gs2326DHCPRelayConfigurationGatewaysRowStatus_Object = MibTableColumn
gs2326DHCPRelayConfigurationGatewaysRowStatus = _Gs2326DHCPRelayConfigurationGatewaysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 5, 2, 1, 4),
    _Gs2326DHCPRelayConfigurationGatewaysRowStatus_Type()
)
gs2326DHCPRelayConfigurationGatewaysRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayConfigurationGatewaysRowStatus.setStatus("current")


class _Gs2326DHCPRelayInformationCustom_Type(DisplayString):
    """Custom type gs2326DHCPRelayInformationCustom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2326DHCPRelayInformationCustom_Type.__name__ = "DisplayString"
_Gs2326DHCPRelayInformationCustom_Object = MibScalar
gs2326DHCPRelayInformationCustom = _Gs2326DHCPRelayInformationCustom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 1, 1500),
    _Gs2326DHCPRelayInformationCustom_Type()
)
gs2326DHCPRelayInformationCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DHCPRelayInformationCustom.setStatus("current")
_Gs2326DHCPRelayStatistics_ObjectIdentity = ObjectIdentity
gs2326DHCPRelayStatistics = _Gs2326DHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2)
)
_Gs2326DHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
gs2326DHCPRelayServerStatistics = _Gs2326DHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1)
)
_Gs2326ServerStatTransmitToServer_Type = Counter32
_Gs2326ServerStatTransmitToServer_Object = MibScalar
gs2326ServerStatTransmitToServer = _Gs2326ServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 1),
    _Gs2326ServerStatTransmitToServer_Type()
)
gs2326ServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatTransmitToServer.setStatus("current")
_Gs2326ServerStatTransmitError_Type = Counter32
_Gs2326ServerStatTransmitError_Object = MibScalar
gs2326ServerStatTransmitError = _Gs2326ServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 2),
    _Gs2326ServerStatTransmitError_Type()
)
gs2326ServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatTransmitError.setStatus("current")
_Gs2326ServerStatReceiveFromServer_Type = Counter32
_Gs2326ServerStatReceiveFromServer_Object = MibScalar
gs2326ServerStatReceiveFromServer = _Gs2326ServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 3),
    _Gs2326ServerStatReceiveFromServer_Type()
)
gs2326ServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatReceiveFromServer.setStatus("current")
_Gs2326ServerStatReceiveMissingAgentOption_Type = Counter32
_Gs2326ServerStatReceiveMissingAgentOption_Object = MibScalar
gs2326ServerStatReceiveMissingAgentOption = _Gs2326ServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 4),
    _Gs2326ServerStatReceiveMissingAgentOption_Type()
)
gs2326ServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatReceiveMissingAgentOption.setStatus("current")
_Gs2326ServerStatReceiveMissingCircuitID_Type = Counter32
_Gs2326ServerStatReceiveMissingCircuitID_Object = MibScalar
gs2326ServerStatReceiveMissingCircuitID = _Gs2326ServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 5),
    _Gs2326ServerStatReceiveMissingCircuitID_Type()
)
gs2326ServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatReceiveMissingCircuitID.setStatus("current")
_Gs2326ServerStatReceiveMissingRemoteID_Type = Counter32
_Gs2326ServerStatReceiveMissingRemoteID_Object = MibScalar
gs2326ServerStatReceiveMissingRemoteID = _Gs2326ServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 6),
    _Gs2326ServerStatReceiveMissingRemoteID_Type()
)
gs2326ServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatReceiveMissingRemoteID.setStatus("current")
_Gs2326ServerStatReceiveBadCircuitID_Type = Counter32
_Gs2326ServerStatReceiveBadCircuitID_Object = MibScalar
gs2326ServerStatReceiveBadCircuitID = _Gs2326ServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 7),
    _Gs2326ServerStatReceiveBadCircuitID_Type()
)
gs2326ServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatReceiveBadCircuitID.setStatus("current")
_Gs2326ServerStatReceiveBadRemoteID_Type = Counter32
_Gs2326ServerStatReceiveBadRemoteID_Object = MibScalar
gs2326ServerStatReceiveBadRemoteID = _Gs2326ServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 1, 8),
    _Gs2326ServerStatReceiveBadRemoteID_Type()
)
gs2326ServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ServerStatReceiveBadRemoteID.setStatus("current")
_Gs2326DHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
gs2326DHCPRelayClientStatistics = _Gs2326DHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2)
)
_Gs2326ClientStatTransmitToClient_Type = Counter32
_Gs2326ClientStatTransmitToClient_Object = MibScalar
gs2326ClientStatTransmitToClient = _Gs2326ClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 1),
    _Gs2326ClientStatTransmitToClient_Type()
)
gs2326ClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatTransmitToClient.setStatus("current")
_Gs2326ClientStatTransmitError_Type = Counter32
_Gs2326ClientStatTransmitError_Object = MibScalar
gs2326ClientStatTransmitError = _Gs2326ClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 2),
    _Gs2326ClientStatTransmitError_Type()
)
gs2326ClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatTransmitError.setStatus("current")
_Gs2326ClientStatReceivefromClient_Type = Counter32
_Gs2326ClientStatReceivefromClient_Object = MibScalar
gs2326ClientStatReceivefromClient = _Gs2326ClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 3),
    _Gs2326ClientStatReceivefromClient_Type()
)
gs2326ClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatReceivefromClient.setStatus("current")
_Gs2326ClientStatReceiveAgentOption_Type = Counter32
_Gs2326ClientStatReceiveAgentOption_Object = MibScalar
gs2326ClientStatReceiveAgentOption = _Gs2326ClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 4),
    _Gs2326ClientStatReceiveAgentOption_Type()
)
gs2326ClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatReceiveAgentOption.setStatus("current")
_Gs2326ClientStatReplaceAgentOption_Type = Counter32
_Gs2326ClientStatReplaceAgentOption_Object = MibScalar
gs2326ClientStatReplaceAgentOption = _Gs2326ClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 5),
    _Gs2326ClientStatReplaceAgentOption_Type()
)
gs2326ClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatReplaceAgentOption.setStatus("current")
_Gs2326ClientStatKeepAgentOption_Type = Counter32
_Gs2326ClientStatKeepAgentOption_Object = MibScalar
gs2326ClientStatKeepAgentOption = _Gs2326ClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 6),
    _Gs2326ClientStatKeepAgentOption_Type()
)
gs2326ClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatKeepAgentOption.setStatus("current")
_Gs2326ClientStatDropAgentOption_Type = Counter32
_Gs2326ClientStatDropAgentOption_Object = MibScalar
gs2326ClientStatDropAgentOption = _Gs2326ClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 4, 2, 2, 7),
    _Gs2326ClientStatDropAgentOption_Type()
)
gs2326ClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326ClientStatDropAgentOption.setStatus("current")
_Gs2326PortSecurity_ObjectIdentity = ObjectIdentity
gs2326PortSecurity = _Gs2326PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5)
)
_Gs2326PortSecLimitCtrl_ObjectIdentity = ObjectIdentity
gs2326PortSecLimitCtrl = _Gs2326PortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1)
)
_Gs2326PortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2326PortSecLimitCtrlSystemConf = _Gs2326PortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 1)
)


class _Gs2326PortSecurityMode_Type(Integer32):
    """Custom type gs2326PortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortSecurityMode_Type.__name__ = "Integer32"
_Gs2326PortSecurityMode_Object = MibScalar
gs2326PortSecurityMode = _Gs2326PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 1, 1),
    _Gs2326PortSecurityMode_Type()
)
gs2326PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecurityMode.setStatus("current")


class _Gs2326PortSecurityAging_Type(Integer32):
    """Custom type gs2326PortSecurityAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortSecurityAging_Type.__name__ = "Integer32"
_Gs2326PortSecurityAging_Object = MibScalar
gs2326PortSecurityAging = _Gs2326PortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 1, 2),
    _Gs2326PortSecurityAging_Type()
)
gs2326PortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecurityAging.setStatus("current")


class _Gs2326PortSecurityAgingPeriod_Type(Integer32):
    """Custom type gs2326PortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Gs2326PortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Gs2326PortSecurityAgingPeriod_Object = MibScalar
gs2326PortSecurityAgingPeriod = _Gs2326PortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 1, 3),
    _Gs2326PortSecurityAgingPeriod_Type()
)
gs2326PortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecurityAgingPeriod.setStatus("current")
_Gs2326PortSecLimitCtrlTable_Object = MibTable
gs2326PortSecLimitCtrlTable = _Gs2326PortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlTable.setStatus("current")
_Gs2326PortSecLimitCtrlEntry_Object = MibTableRow
gs2326PortSecLimitCtrlEntry = _Gs2326PortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1)
)
gs2326PortSecLimitCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlEntry.setStatus("current")


class _Gs2326PortSecLimitCtrlPort_Type(Integer32):
    """Custom type gs2326PortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Gs2326PortSecLimitCtrlPort_Object = MibTableColumn
gs2326PortSecLimitCtrlPort = _Gs2326PortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1, 1),
    _Gs2326PortSecLimitCtrlPort_Type()
)
gs2326PortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlPort.setStatus("current")


class _Gs2326PortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type gs2326PortSecLimitCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326PortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Gs2326PortSecLimitCtrlPortMode_Object = MibTableColumn
gs2326PortSecLimitCtrlPortMode = _Gs2326PortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1, 2),
    _Gs2326PortSecLimitCtrlPortMode_Type()
)
gs2326PortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlPortMode.setStatus("current")


class _Gs2326PortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type gs2326PortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2326PortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Gs2326PortSecLimitCtrlPortLimit_Object = MibTableColumn
gs2326PortSecLimitCtrlPortLimit = _Gs2326PortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1, 3),
    _Gs2326PortSecLimitCtrlPortLimit_Type()
)
gs2326PortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlPortLimit.setStatus("current")


class _Gs2326PortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type gs2326PortSecLimitCtrlPortAction based on Integer32"""
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


_Gs2326PortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Gs2326PortSecLimitCtrlPortAction_Object = MibTableColumn
gs2326PortSecLimitCtrlPortAction = _Gs2326PortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1, 4),
    _Gs2326PortSecLimitCtrlPortAction_Type()
)
gs2326PortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlPortAction.setStatus("current")
_Gs2326PortSecLimitCtrlPortState_Type = DisplayString
_Gs2326PortSecLimitCtrlPortState_Object = MibTableColumn
gs2326PortSecLimitCtrlPortState = _Gs2326PortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1, 5),
    _Gs2326PortSecLimitCtrlPortState_Type()
)
gs2326PortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlPortState.setStatus("current")


class _Gs2326PortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type gs2326PortSecLimitCtrlPortReOpen based on Integer32"""
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


_Gs2326PortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Gs2326PortSecLimitCtrlPortReOpen_Object = MibTableColumn
gs2326PortSecLimitCtrlPortReOpen = _Gs2326PortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 1, 2, 1, 6),
    _Gs2326PortSecLimitCtrlPortReOpen_Type()
)
gs2326PortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecLimitCtrlPortReOpen.setStatus("current")
_Gs2326PortSecSwitchStatusTable_Object = MibTable
gs2326PortSecSwitchStatusTable = _Gs2326PortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusTable.setStatus("current")
_Gs2326PortSecSwitchStatusEntry_Object = MibTableRow
gs2326PortSecSwitchStatusEntry = _Gs2326PortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2, 1)
)
gs2326PortSecSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusEntry.setStatus("current")


class _Gs2326PortSecSwitchStatusPort_Type(Integer32):
    """Custom type gs2326PortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Gs2326PortSecSwitchStatusPort_Object = MibTableColumn
gs2326PortSecSwitchStatusPort = _Gs2326PortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2, 1, 1),
    _Gs2326PortSecSwitchStatusPort_Type()
)
gs2326PortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusPort.setStatus("current")
_Gs2326PortSecSwitchStatusUsers_Type = DisplayString
_Gs2326PortSecSwitchStatusUsers_Object = MibTableColumn
gs2326PortSecSwitchStatusUsers = _Gs2326PortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2, 1, 2),
    _Gs2326PortSecSwitchStatusUsers_Type()
)
gs2326PortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusUsers.setStatus("current")
_Gs2326PortSecSwitchStatusState_Type = DisplayString
_Gs2326PortSecSwitchStatusState_Object = MibTableColumn
gs2326PortSecSwitchStatusState = _Gs2326PortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2, 1, 3),
    _Gs2326PortSecSwitchStatusState_Type()
)
gs2326PortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusState.setStatus("current")


class _Gs2326PortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type gs2326PortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Gs2326PortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
gs2326PortSecSwitchStatusMACCountCurrent = _Gs2326PortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2, 1, 4),
    _Gs2326PortSecSwitchStatusMACCountCurrent_Type()
)
gs2326PortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Gs2326PortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type gs2326PortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Gs2326PortSecSwitchStatusMACCountLimit_Object = MibTableColumn
gs2326PortSecSwitchStatusMACCountLimit = _Gs2326PortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 2, 1, 5),
    _Gs2326PortSecSwitchStatusMACCountLimit_Type()
)
gs2326PortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecSwitchStatusMACCountLimit.setStatus("current")
_Gs2326PortSecPortStatus_ObjectIdentity = ObjectIdentity
gs2326PortSecPortStatus = _Gs2326PortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3)
)


class _Gs2326PortSecPortStatusPort_Type(Integer32):
    """Custom type gs2326PortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortSecPortStatusPort_Type.__name__ = "Integer32"
_Gs2326PortSecPortStatusPort_Object = MibScalar
gs2326PortSecPortStatusPort = _Gs2326PortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 1),
    _Gs2326PortSecPortStatusPort_Type()
)
gs2326PortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusPort.setStatus("current")
_Gs2326PortSecPortStatusTable_Object = MibTable
gs2326PortSecPortStatusTable = _Gs2326PortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusTable.setStatus("current")
_Gs2326PortSecPortStatusEntry_Object = MibTableRow
gs2326PortSecPortStatusEntry = _Gs2326PortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1)
)
gs2326PortSecPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326PortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusEntry.setStatus("current")


class _Gs2326PortSecPortStatusIndex_Type(Integer32):
    """Custom type gs2326PortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326PortSecPortStatusIndex_Type.__name__ = "Integer32"
_Gs2326PortSecPortStatusIndex_Object = MibTableColumn
gs2326PortSecPortStatusIndex = _Gs2326PortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1, 1),
    _Gs2326PortSecPortStatusIndex_Type()
)
gs2326PortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusIndex.setStatus("current")
_Gs2326PortSecPortStatusMACAddress_Type = MacAddress
_Gs2326PortSecPortStatusMACAddress_Object = MibTableColumn
gs2326PortSecPortStatusMACAddress = _Gs2326PortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1, 2),
    _Gs2326PortSecPortStatusMACAddress_Type()
)
gs2326PortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusMACAddress.setStatus("current")


class _Gs2326PortSecPortStatusVLANId_Type(Integer32):
    """Custom type gs2326PortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326PortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Gs2326PortSecPortStatusVLANId_Object = MibTableColumn
gs2326PortSecPortStatusVLANId = _Gs2326PortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1, 3),
    _Gs2326PortSecPortStatusVLANId_Type()
)
gs2326PortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusVLANId.setStatus("current")
_Gs2326PortSecPortStatusState_Type = DisplayString
_Gs2326PortSecPortStatusState_Object = MibTableColumn
gs2326PortSecPortStatusState = _Gs2326PortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1, 4),
    _Gs2326PortSecPortStatusState_Type()
)
gs2326PortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusState.setStatus("current")
_Gs2326PortSecPortStatusTimeOfAddition_Type = DisplayString
_Gs2326PortSecPortStatusTimeOfAddition_Object = MibTableColumn
gs2326PortSecPortStatusTimeOfAddition = _Gs2326PortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1, 5),
    _Gs2326PortSecPortStatusTimeOfAddition_Type()
)
gs2326PortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusTimeOfAddition.setStatus("current")
_Gs2326PortSecPortStatusAgeAndHold_Type = DisplayString
_Gs2326PortSecPortStatusAgeAndHold_Object = MibTableColumn
gs2326PortSecPortStatusAgeAndHold = _Gs2326PortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 5, 3, 2, 1, 6),
    _Gs2326PortSecPortStatusAgeAndHold_Type()
)
gs2326PortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PortSecPortStatusAgeAndHold.setStatus("current")
_Gs2326AccessManagement_ObjectIdentity = ObjectIdentity
gs2326AccessManagement = _Gs2326AccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6)
)
_Gs2326AccessMgtConf_ObjectIdentity = ObjectIdentity
gs2326AccessMgtConf = _Gs2326AccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1)
)


class _Gs2326AccessMgtConfMode_Type(Integer32):
    """Custom type gs2326AccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AccessMgtConfMode_Type.__name__ = "Integer32"
_Gs2326AccessMgtConfMode_Object = MibScalar
gs2326AccessMgtConfMode = _Gs2326AccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 1),
    _Gs2326AccessMgtConfMode_Type()
)
gs2326AccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtConfMode.setStatus("current")


class _Gs2326AccessMgtConfCreate_Type(Integer32):
    """Custom type gs2326AccessMgtConfCreate based on Integer32"""
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


_Gs2326AccessMgtConfCreate_Type.__name__ = "Integer32"
_Gs2326AccessMgtConfCreate_Object = MibScalar
gs2326AccessMgtConfCreate = _Gs2326AccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 2),
    _Gs2326AccessMgtConfCreate_Type()
)
gs2326AccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtConfCreate.setStatus("current")
_Gs2326AccessMgtConfTable_Object = MibTable
gs2326AccessMgtConfTable = _Gs2326AccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    gs2326AccessMgtConfTable.setStatus("current")
_Gs2326AccessMgtConfEntry_Object = MibTableRow
gs2326AccessMgtConfEntry = _Gs2326AccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1)
)
gs2326AccessMgtConfEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326AccessMgtIndex"),
)
if mibBuilder.loadTexts:
    gs2326AccessMgtConfEntry.setStatus("current")


class _Gs2326AccessMgtIndex_Type(Integer32):
    """Custom type gs2326AccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2326AccessMgtIndex_Type.__name__ = "Integer32"
_Gs2326AccessMgtIndex_Object = MibTableColumn
gs2326AccessMgtIndex = _Gs2326AccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 1),
    _Gs2326AccessMgtIndex_Type()
)
gs2326AccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtIndex.setStatus("current")


class _Gs2326AccessMgtAddresstype_Type(Integer32):
    """Custom type gs2326AccessMgtAddresstype based on Integer32"""
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


_Gs2326AccessMgtAddresstype_Type.__name__ = "Integer32"
_Gs2326AccessMgtAddresstype_Object = MibTableColumn
gs2326AccessMgtAddresstype = _Gs2326AccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 2),
    _Gs2326AccessMgtAddresstype_Type()
)
gs2326AccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtAddresstype.setStatus("current")
_Gs2326AccessMgtStartIpAddress_Type = DisplayString
_Gs2326AccessMgtStartIpAddress_Object = MibTableColumn
gs2326AccessMgtStartIpAddress = _Gs2326AccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 3),
    _Gs2326AccessMgtStartIpAddress_Type()
)
gs2326AccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtStartIpAddress.setStatus("current")
_Gs2326AccessMgtEndIpAddress_Type = DisplayString
_Gs2326AccessMgtEndIpAddress_Object = MibTableColumn
gs2326AccessMgtEndIpAddress = _Gs2326AccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 4),
    _Gs2326AccessMgtEndIpAddress_Type()
)
gs2326AccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtEndIpAddress.setStatus("current")


class _Gs2326AccessMgtHttpHttps_Type(Integer32):
    """Custom type gs2326AccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AccessMgtHttpHttps_Type.__name__ = "Integer32"
_Gs2326AccessMgtHttpHttps_Object = MibTableColumn
gs2326AccessMgtHttpHttps = _Gs2326AccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 5),
    _Gs2326AccessMgtHttpHttps_Type()
)
gs2326AccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtHttpHttps.setStatus("current")


class _Gs2326AccessMgtSNMP_Type(Integer32):
    """Custom type gs2326AccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AccessMgtSNMP_Type.__name__ = "Integer32"
_Gs2326AccessMgtSNMP_Object = MibTableColumn
gs2326AccessMgtSNMP = _Gs2326AccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 6),
    _Gs2326AccessMgtSNMP_Type()
)
gs2326AccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtSNMP.setStatus("current")


class _Gs2326AccessMgtTelnetSSH_Type(Integer32):
    """Custom type gs2326AccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Gs2326AccessMgtTelnetSSH_Object = MibTableColumn
gs2326AccessMgtTelnetSSH = _Gs2326AccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 7),
    _Gs2326AccessMgtTelnetSSH_Type()
)
gs2326AccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtTelnetSSH.setStatus("current")


class _Gs2326AccessMgtRowStatus_Type(Integer32):
    """Custom type gs2326AccessMgtRowStatus based on Integer32"""
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


_Gs2326AccessMgtRowStatus_Type.__name__ = "Integer32"
_Gs2326AccessMgtRowStatus_Object = MibTableColumn
gs2326AccessMgtRowStatus = _Gs2326AccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 1, 3, 1, 8),
    _Gs2326AccessMgtRowStatus_Type()
)
gs2326AccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtRowStatus.setStatus("current")
_Gs2326AccessMgtStatistics_ObjectIdentity = ObjectIdentity
gs2326AccessMgtStatistics = _Gs2326AccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2)
)
_Gs2326HttpReceivedPkts_Type = Counter32
_Gs2326HttpReceivedPkts_Object = MibScalar
gs2326HttpReceivedPkts = _Gs2326HttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 1),
    _Gs2326HttpReceivedPkts_Type()
)
gs2326HttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HttpReceivedPkts.setStatus("current")
_Gs2326HttpAllowedPkts_Type = Counter32
_Gs2326HttpAllowedPkts_Object = MibScalar
gs2326HttpAllowedPkts = _Gs2326HttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 2),
    _Gs2326HttpAllowedPkts_Type()
)
gs2326HttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HttpAllowedPkts.setStatus("current")
_Gs2326HttpDiscardedPkts_Type = Counter32
_Gs2326HttpDiscardedPkts_Object = MibScalar
gs2326HttpDiscardedPkts = _Gs2326HttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 3),
    _Gs2326HttpDiscardedPkts_Type()
)
gs2326HttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HttpDiscardedPkts.setStatus("current")
_Gs2326HttpsReceivedPkts_Type = Counter32
_Gs2326HttpsReceivedPkts_Object = MibScalar
gs2326HttpsReceivedPkts = _Gs2326HttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 4),
    _Gs2326HttpsReceivedPkts_Type()
)
gs2326HttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HttpsReceivedPkts.setStatus("current")
_Gs2326HttpsAllowedPkts_Type = Counter32
_Gs2326HttpsAllowedPkts_Object = MibScalar
gs2326HttpsAllowedPkts = _Gs2326HttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 5),
    _Gs2326HttpsAllowedPkts_Type()
)
gs2326HttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HttpsAllowedPkts.setStatus("current")
_Gs2326HttpsDiscardedPkts_Type = Counter32
_Gs2326HttpsDiscardedPkts_Object = MibScalar
gs2326HttpsDiscardedPkts = _Gs2326HttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 6),
    _Gs2326HttpsDiscardedPkts_Type()
)
gs2326HttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326HttpsDiscardedPkts.setStatus("current")
_Gs2326SnmpReceivedPkts_Type = Counter32
_Gs2326SnmpReceivedPkts_Object = MibScalar
gs2326SnmpReceivedPkts = _Gs2326SnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 7),
    _Gs2326SnmpReceivedPkts_Type()
)
gs2326SnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SnmpReceivedPkts.setStatus("current")
_Gs2326SnmpAllowedPkts_Type = Counter32
_Gs2326SnmpAllowedPkts_Object = MibScalar
gs2326SnmpAllowedPkts = _Gs2326SnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 8),
    _Gs2326SnmpAllowedPkts_Type()
)
gs2326SnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SnmpAllowedPkts.setStatus("current")
_Gs2326SnmpDiscardedPkts_Type = Counter32
_Gs2326SnmpDiscardedPkts_Object = MibScalar
gs2326SnmpDiscardedPkts = _Gs2326SnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 9),
    _Gs2326SnmpDiscardedPkts_Type()
)
gs2326SnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SnmpDiscardedPkts.setStatus("current")
_Gs2326TelnetReceivedPkts_Type = Counter32
_Gs2326TelnetReceivedPkts_Object = MibScalar
gs2326TelnetReceivedPkts = _Gs2326TelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 10),
    _Gs2326TelnetReceivedPkts_Type()
)
gs2326TelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326TelnetReceivedPkts.setStatus("current")
_Gs2326TelnetAllowedPkts_Type = Counter32
_Gs2326TelnetAllowedPkts_Object = MibScalar
gs2326TelnetAllowedPkts = _Gs2326TelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 11),
    _Gs2326TelnetAllowedPkts_Type()
)
gs2326TelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326TelnetAllowedPkts.setStatus("current")
_Gs2326TelnetDiscardedPkts_Type = Counter32
_Gs2326TelnetDiscardedPkts_Object = MibScalar
gs2326TelnetDiscardedPkts = _Gs2326TelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 12),
    _Gs2326TelnetDiscardedPkts_Type()
)
gs2326TelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326TelnetDiscardedPkts.setStatus("current")
_Gs2326SSHReceivedPkts_Type = Counter32
_Gs2326SSHReceivedPkts_Object = MibScalar
gs2326SSHReceivedPkts = _Gs2326SSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 13),
    _Gs2326SSHReceivedPkts_Type()
)
gs2326SSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SSHReceivedPkts.setStatus("current")
_Gs2326SSHAllowedPkts_Type = Counter32
_Gs2326SSHAllowedPkts_Object = MibScalar
gs2326SSHAllowedPkts = _Gs2326SSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 14),
    _Gs2326SSHAllowedPkts_Type()
)
gs2326SSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SSHAllowedPkts.setStatus("current")
_Gs2326SSHDiscardedPkts_Type = Counter32
_Gs2326SSHDiscardedPkts_Object = MibScalar
gs2326SSHDiscardedPkts = _Gs2326SSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 15),
    _Gs2326SSHDiscardedPkts_Type()
)
gs2326SSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326SSHDiscardedPkts.setStatus("current")


class _Gs2326AccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type gs2326AccessMgtStatisticsClearAll based on Integer32"""
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


_Gs2326AccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Gs2326AccessMgtStatisticsClearAll_Object = MibScalar
gs2326AccessMgtStatisticsClearAll = _Gs2326AccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 6, 2, 16),
    _Gs2326AccessMgtStatisticsClearAll_Type()
)
gs2326AccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AccessMgtStatisticsClearAll.setStatus("current")
_Gs2326SSH_ObjectIdentity = ObjectIdentity
gs2326SSH = _Gs2326SSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 7)
)


class _Gs2326SSHMode_Type(Integer32):
    """Custom type gs2326SSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326SSHMode_Type.__name__ = "Integer32"
_Gs2326SSHMode_Object = MibScalar
gs2326SSHMode = _Gs2326SSHMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 7, 1),
    _Gs2326SSHMode_Type()
)
gs2326SSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SSHMode.setStatus("current")
_Gs2326HTTPS_ObjectIdentity = ObjectIdentity
gs2326HTTPS = _Gs2326HTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 8)
)


class _Gs2326HTTPSMode_Type(Integer32):
    """Custom type gs2326HTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326HTTPSMode_Type.__name__ = "Integer32"
_Gs2326HTTPSMode_Object = MibScalar
gs2326HTTPSMode = _Gs2326HTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 8, 1),
    _Gs2326HTTPSMode_Type()
)
gs2326HTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HTTPSMode.setStatus("current")


class _Gs2326HTTPSAutoRedirect_Type(Integer32):
    """Custom type gs2326HTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326HTTPSAutoRedirect_Type.__name__ = "Integer32"
_Gs2326HTTPSAutoRedirect_Object = MibScalar
gs2326HTTPSAutoRedirect = _Gs2326HTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 8, 2),
    _Gs2326HTTPSAutoRedirect_Type()
)
gs2326HTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HTTPSAutoRedirect.setStatus("current")


class _Gs2326HTTPSCertRenew_Type(Integer32):
    """Custom type gs2326HTTPSCertRenew based on Integer32"""
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


_Gs2326HTTPSCertRenew_Type.__name__ = "Integer32"
_Gs2326HTTPSCertRenew_Object = MibScalar
gs2326HTTPSCertRenew = _Gs2326HTTPSCertRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 8, 3),
    _Gs2326HTTPSCertRenew_Type()
)
gs2326HTTPSCertRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HTTPSCertRenew.setStatus("current")


class _Gs2326HTTPSMinProtoVersion_Type(Integer32):
    """Custom type gs2326HTTPSMinProtoVersion based on Integer32"""
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


_Gs2326HTTPSMinProtoVersion_Type.__name__ = "Integer32"
_Gs2326HTTPSMinProtoVersion_Object = MibScalar
gs2326HTTPSMinProtoVersion = _Gs2326HTTPSMinProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 8, 4),
    _Gs2326HTTPSMinProtoVersion_Type()
)
gs2326HTTPSMinProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HTTPSMinProtoVersion.setStatus("current")


class _Gs2326HTTPMode_Type(Integer32):
    """Custom type gs2326HTTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326HTTPMode_Type.__name__ = "Integer32"
_Gs2326HTTPMode_Object = MibScalar
gs2326HTTPMode = _Gs2326HTTPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 8, 5),
    _Gs2326HTTPMode_Type()
)
gs2326HTTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HTTPMode.setStatus("current")
_Gs2326AuthMethod_ObjectIdentity = ObjectIdentity
gs2326AuthMethod = _Gs2326AuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9)
)


class _Gs2326ConsoleAuthMethod_Type(Integer32):
    """Custom type gs2326ConsoleAuthMethod based on Integer32"""
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


_Gs2326ConsoleAuthMethod_Type.__name__ = "Integer32"
_Gs2326ConsoleAuthMethod_Object = MibScalar
gs2326ConsoleAuthMethod = _Gs2326ConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 1),
    _Gs2326ConsoleAuthMethod_Type()
)
gs2326ConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ConsoleAuthMethod.setStatus("current")


class _Gs2326ConsoleFallback_Type(Integer32):
    """Custom type gs2326ConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ConsoleFallback_Type.__name__ = "Integer32"
_Gs2326ConsoleFallback_Object = MibScalar
gs2326ConsoleFallback = _Gs2326ConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 2),
    _Gs2326ConsoleFallback_Type()
)
gs2326ConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ConsoleFallback.setStatus("current")


class _Gs2326TelnetAuthMethod_Type(Integer32):
    """Custom type gs2326TelnetAuthMethod based on Integer32"""
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


_Gs2326TelnetAuthMethod_Type.__name__ = "Integer32"
_Gs2326TelnetAuthMethod_Object = MibScalar
gs2326TelnetAuthMethod = _Gs2326TelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 3),
    _Gs2326TelnetAuthMethod_Type()
)
gs2326TelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TelnetAuthMethod.setStatus("current")


class _Gs2326TelnetFallback_Type(Integer32):
    """Custom type gs2326TelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326TelnetFallback_Type.__name__ = "Integer32"
_Gs2326TelnetFallback_Object = MibScalar
gs2326TelnetFallback = _Gs2326TelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 4),
    _Gs2326TelnetFallback_Type()
)
gs2326TelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TelnetFallback.setStatus("current")


class _Gs2326SshAuthMethod_Type(Integer32):
    """Custom type gs2326SshAuthMethod based on Integer32"""
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


_Gs2326SshAuthMethod_Type.__name__ = "Integer32"
_Gs2326SshAuthMethod_Object = MibScalar
gs2326SshAuthMethod = _Gs2326SshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 5),
    _Gs2326SshAuthMethod_Type()
)
gs2326SshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SshAuthMethod.setStatus("current")


class _Gs2326SshFallback_Type(Integer32):
    """Custom type gs2326SshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326SshFallback_Type.__name__ = "Integer32"
_Gs2326SshFallback_Object = MibScalar
gs2326SshFallback = _Gs2326SshFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 6),
    _Gs2326SshFallback_Type()
)
gs2326SshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SshFallback.setStatus("current")


class _Gs2326TftpAuthMethod_Type(Integer32):
    """Custom type gs2326TftpAuthMethod based on Integer32"""
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


_Gs2326TftpAuthMethod_Type.__name__ = "Integer32"
_Gs2326TftpAuthMethod_Object = MibScalar
gs2326TftpAuthMethod = _Gs2326TftpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 9),
    _Gs2326TftpAuthMethod_Type()
)
gs2326TftpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TftpAuthMethod.setStatus("current")


class _Gs2326TftpFallback_Type(Integer32):
    """Custom type gs2326TftpFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326TftpFallback_Type.__name__ = "Integer32"
_Gs2326TftpFallback_Object = MibScalar
gs2326TftpFallback = _Gs2326TftpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 10),
    _Gs2326TftpFallback_Type()
)
gs2326TftpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TftpFallback.setStatus("current")


class _Gs2326LoginFailures_Type(Integer32):
    """Custom type gs2326LoginFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Gs2326LoginFailures_Type.__name__ = "Integer32"
_Gs2326LoginFailures_Object = MibScalar
gs2326LoginFailures = _Gs2326LoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 11),
    _Gs2326LoginFailures_Type()
)
gs2326LoginFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LoginFailures.setStatus("current")


class _Gs2326LockMinutes_Type(Integer32):
    """Custom type gs2326LockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Gs2326LockMinutes_Type.__name__ = "Integer32"
_Gs2326LockMinutes_Object = MibScalar
gs2326LockMinutes = _Gs2326LockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 12),
    _Gs2326LockMinutes_Type()
)
gs2326LockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326LockMinutes.setStatus("current")


class _Gs2326HttpAuthMethod_Type(Integer32):
    """Custom type gs2326HttpAuthMethod based on Integer32"""
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


_Gs2326HttpAuthMethod_Type.__name__ = "Integer32"
_Gs2326HttpAuthMethod_Object = MibScalar
gs2326HttpAuthMethod = _Gs2326HttpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 13),
    _Gs2326HttpAuthMethod_Type()
)
gs2326HttpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HttpAuthMethod.setStatus("current")


class _Gs2326HttpFallback_Type(Integer32):
    """Custom type gs2326HttpFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326HttpFallback_Type.__name__ = "Integer32"
_Gs2326HttpFallback_Object = MibScalar
gs2326HttpFallback = _Gs2326HttpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 14),
    _Gs2326HttpFallback_Type()
)
gs2326HttpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HttpFallback.setStatus("current")


class _Gs2326HttpsAuthMethod_Type(Integer32):
    """Custom type gs2326HttpsAuthMethod based on Integer32"""
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


_Gs2326HttpsAuthMethod_Type.__name__ = "Integer32"
_Gs2326HttpsAuthMethod_Object = MibScalar
gs2326HttpsAuthMethod = _Gs2326HttpsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 15),
    _Gs2326HttpsAuthMethod_Type()
)
gs2326HttpsAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HttpsAuthMethod.setStatus("current")


class _Gs2326HttpsFallback_Type(Integer32):
    """Custom type gs2326HttpsFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326HttpsFallback_Type.__name__ = "Integer32"
_Gs2326HttpsFallback_Object = MibScalar
gs2326HttpsFallback = _Gs2326HttpsFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 9, 16),
    _Gs2326HttpsFallback_Type()
)
gs2326HttpsFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326HttpsFallback.setStatus("current")
_Gs2326AAA_ObjectIdentity = ObjectIdentity
gs2326AAA = _Gs2326AAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10)
)
_Gs2326AAACommonServer_ObjectIdentity = ObjectIdentity
gs2326AAACommonServer = _Gs2326AAACommonServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 1)
)


class _Gs2326AAACommonServerTimeout_Type(Integer32):
    """Custom type gs2326AAACommonServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_Gs2326AAACommonServerTimeout_Type.__name__ = "Integer32"
_Gs2326AAACommonServerTimeout_Object = MibScalar
gs2326AAACommonServerTimeout = _Gs2326AAACommonServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 1, 1),
    _Gs2326AAACommonServerTimeout_Type()
)
gs2326AAACommonServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AAACommonServerTimeout.setStatus("current")


class _Gs2326AAACommonServerDeadTime_Type(Integer32):
    """Custom type gs2326AAACommonServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Gs2326AAACommonServerDeadTime_Type.__name__ = "Integer32"
_Gs2326AAACommonServerDeadTime_Object = MibScalar
gs2326AAACommonServerDeadTime = _Gs2326AAACommonServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 1, 2),
    _Gs2326AAACommonServerDeadTime_Type()
)
gs2326AAACommonServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AAACommonServerDeadTime.setStatus("current")
_Gs2326AAATACACSPlusAuthAndAccounting_ObjectIdentity = ObjectIdentity
gs2326AAATACACSPlusAuthAndAccounting = _Gs2326AAATACACSPlusAuthAndAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 2)
)


class _Gs2326AAAAuthorization_Type(Integer32):
    """Custom type gs2326AAAAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AAAAuthorization_Type.__name__ = "Integer32"
_Gs2326AAAAuthorization_Object = MibScalar
gs2326AAAAuthorization = _Gs2326AAAAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 2, 1),
    _Gs2326AAAAuthorization_Type()
)
gs2326AAAAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AAAAuthorization.setStatus("current")


class _Gs2326AAAFallbackToLocalAuthorization_Type(Integer32):
    """Custom type gs2326AAAFallbackToLocalAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AAAFallbackToLocalAuthorization_Type.__name__ = "Integer32"
_Gs2326AAAFallbackToLocalAuthorization_Object = MibScalar
gs2326AAAFallbackToLocalAuthorization = _Gs2326AAAFallbackToLocalAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 2, 2),
    _Gs2326AAAFallbackToLocalAuthorization_Type()
)
gs2326AAAFallbackToLocalAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AAAFallbackToLocalAuthorization.setStatus("current")


class _Gs2326AAAAccounting_Type(Integer32):
    """Custom type gs2326AAAAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326AAAAccounting_Type.__name__ = "Integer32"
_Gs2326AAAAccounting_Object = MibScalar
gs2326AAAAccounting = _Gs2326AAAAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 2, 3),
    _Gs2326AAAAccounting_Type()
)
gs2326AAAAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326AAAAccounting.setStatus("current")
_Gs2326RADIUSAuthenticationServerTable_Object = MibTable
gs2326RADIUSAuthenticationServerTable = _Gs2326RADIUSAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3)
)
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerTable.setStatus("current")
_Gs2326RADIUSAuthenticationServerEntry_Object = MibTableRow
gs2326RADIUSAuthenticationServerEntry = _Gs2326RADIUSAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3, 1)
)
gs2326RADIUSAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326RADIUSAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerEntry.setStatus("current")


class _Gs2326RADIUSAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2326RADIUSAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2326RADIUSAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2326RADIUSAuthenticationServerIndex_Object = MibTableColumn
gs2326RADIUSAuthenticationServerIndex = _Gs2326RADIUSAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3, 1, 1),
    _Gs2326RADIUSAuthenticationServerIndex_Type()
)
gs2326RADIUSAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerIndex.setStatus("current")


class _Gs2326RADIUSAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2326RADIUSAuthenticationServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326RADIUSAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2326RADIUSAuthenticationServerEnable_Object = MibTableColumn
gs2326RADIUSAuthenticationServerEnable = _Gs2326RADIUSAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3, 1, 2),
    _Gs2326RADIUSAuthenticationServerEnable_Type()
)
gs2326RADIUSAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerEnable.setStatus("current")
_Gs2326RADIUSAuthenticationServerIP_Type = DisplayString
_Gs2326RADIUSAuthenticationServerIP_Object = MibTableColumn
gs2326RADIUSAuthenticationServerIP = _Gs2326RADIUSAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3, 1, 3),
    _Gs2326RADIUSAuthenticationServerIP_Type()
)
gs2326RADIUSAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerIP.setStatus("current")


class _Gs2326RADIUSAuthenticationServerPort_Type(Integer32):
    """Custom type gs2326RADIUSAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2326RADIUSAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2326RADIUSAuthenticationServerPort_Object = MibTableColumn
gs2326RADIUSAuthenticationServerPort = _Gs2326RADIUSAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3, 1, 4),
    _Gs2326RADIUSAuthenticationServerPort_Type()
)
gs2326RADIUSAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerPort.setStatus("current")
_Gs2326RADIUSAuthenticationServerSecret_Type = DisplayString
_Gs2326RADIUSAuthenticationServerSecret_Object = MibTableColumn
gs2326RADIUSAuthenticationServerSecret = _Gs2326RADIUSAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 3, 1, 5),
    _Gs2326RADIUSAuthenticationServerSecret_Type()
)
gs2326RADIUSAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthenticationServerSecret.setStatus("current")
_Gs2326RADIUSAccountingServerTable_Object = MibTable
gs2326RADIUSAccountingServerTable = _Gs2326RADIUSAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4)
)
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerTable.setStatus("current")
_Gs2326RADIUSAccountingServerEntry_Object = MibTableRow
gs2326RADIUSAccountingServerEntry = _Gs2326RADIUSAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4, 1)
)
gs2326RADIUSAccountingServerEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326RADIUSAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerEntry.setStatus("current")


class _Gs2326RADIUSAccountingServerIndex_Type(Integer32):
    """Custom type gs2326RADIUSAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2326RADIUSAccountingServerIndex_Type.__name__ = "Integer32"
_Gs2326RADIUSAccountingServerIndex_Object = MibTableColumn
gs2326RADIUSAccountingServerIndex = _Gs2326RADIUSAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4, 1, 1),
    _Gs2326RADIUSAccountingServerIndex_Type()
)
gs2326RADIUSAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerIndex.setStatus("current")


class _Gs2326RADIUSAccountingServerEnable_Type(Integer32):
    """Custom type gs2326RADIUSAccountingServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326RADIUSAccountingServerEnable_Type.__name__ = "Integer32"
_Gs2326RADIUSAccountingServerEnable_Object = MibTableColumn
gs2326RADIUSAccountingServerEnable = _Gs2326RADIUSAccountingServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4, 1, 2),
    _Gs2326RADIUSAccountingServerEnable_Type()
)
gs2326RADIUSAccountingServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerEnable.setStatus("current")
_Gs2326RADIUSAccountingServerIP_Type = DisplayString
_Gs2326RADIUSAccountingServerIP_Object = MibTableColumn
gs2326RADIUSAccountingServerIP = _Gs2326RADIUSAccountingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4, 1, 3),
    _Gs2326RADIUSAccountingServerIP_Type()
)
gs2326RADIUSAccountingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerIP.setStatus("current")


class _Gs2326RADIUSAccountingServerPort_Type(Integer32):
    """Custom type gs2326RADIUSAccountingServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2326RADIUSAccountingServerPort_Type.__name__ = "Integer32"
_Gs2326RADIUSAccountingServerPort_Object = MibTableColumn
gs2326RADIUSAccountingServerPort = _Gs2326RADIUSAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4, 1, 4),
    _Gs2326RADIUSAccountingServerPort_Type()
)
gs2326RADIUSAccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerPort.setStatus("current")
_Gs2326RADIUSAccountingServerSecret_Type = DisplayString
_Gs2326RADIUSAccountingServerSecret_Object = MibTableColumn
gs2326RADIUSAccountingServerSecret = _Gs2326RADIUSAccountingServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 4, 1, 5),
    _Gs2326RADIUSAccountingServerSecret_Type()
)
gs2326RADIUSAccountingServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingServerSecret.setStatus("current")
_Gs2326TACACSPlusAuthenticationServerTable_Object = MibTable
gs2326TACACSPlusAuthenticationServerTable = _Gs2326TACACSPlusAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5)
)
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerTable.setStatus("current")
_Gs2326TACACSPlusAuthenticationServerEntry_Object = MibTableRow
gs2326TACACSPlusAuthenticationServerEntry = _Gs2326TACACSPlusAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5, 1)
)
gs2326TACACSPlusAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326TACACSPlusAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerEntry.setStatus("current")


class _Gs2326TACACSPlusAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2326TACACSPlusAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2326TACACSPlusAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2326TACACSPlusAuthenticationServerIndex_Object = MibTableColumn
gs2326TACACSPlusAuthenticationServerIndex = _Gs2326TACACSPlusAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5, 1, 1),
    _Gs2326TACACSPlusAuthenticationServerIndex_Type()
)
gs2326TACACSPlusAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerIndex.setStatus("current")


class _Gs2326TACACSPlusAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2326TACACSPlusAuthenticationServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326TACACSPlusAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2326TACACSPlusAuthenticationServerEnable_Object = MibTableColumn
gs2326TACACSPlusAuthenticationServerEnable = _Gs2326TACACSPlusAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5, 1, 2),
    _Gs2326TACACSPlusAuthenticationServerEnable_Type()
)
gs2326TACACSPlusAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerEnable.setStatus("current")
_Gs2326TACACSPlusAuthenticationServerIP_Type = DisplayString
_Gs2326TACACSPlusAuthenticationServerIP_Object = MibTableColumn
gs2326TACACSPlusAuthenticationServerIP = _Gs2326TACACSPlusAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5, 1, 3),
    _Gs2326TACACSPlusAuthenticationServerIP_Type()
)
gs2326TACACSPlusAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerIP.setStatus("current")


class _Gs2326TACACSPlusAuthenticationServerPort_Type(Integer32):
    """Custom type gs2326TACACSPlusAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2326TACACSPlusAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2326TACACSPlusAuthenticationServerPort_Object = MibTableColumn
gs2326TACACSPlusAuthenticationServerPort = _Gs2326TACACSPlusAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5, 1, 4),
    _Gs2326TACACSPlusAuthenticationServerPort_Type()
)
gs2326TACACSPlusAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerPort.setStatus("current")
_Gs2326TACACSPlusAuthenticationServerSecret_Type = DisplayString
_Gs2326TACACSPlusAuthenticationServerSecret_Object = MibTableColumn
gs2326TACACSPlusAuthenticationServerSecret = _Gs2326TACACSPlusAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 5, 1, 5),
    _Gs2326TACACSPlusAuthenticationServerSecret_Type()
)
gs2326TACACSPlusAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326TACACSPlusAuthenticationServerSecret.setStatus("current")
_Gs2326RADIUSStatisticsTable_Object = MibTable
gs2326RADIUSStatisticsTable = _Gs2326RADIUSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6)
)
if mibBuilder.loadTexts:
    gs2326RADIUSStatisticsTable.setStatus("current")
_Gs2326RADIUSStatisticsEntry_Object = MibTableRow
gs2326RADIUSStatisticsEntry = _Gs2326RADIUSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1)
)
gs2326RADIUSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326RADIUSAuthStatisticsServerIndex"),
)
if mibBuilder.loadTexts:
    gs2326RADIUSStatisticsEntry.setStatus("current")


class _Gs2326RADIUSAuthStatisticsServerIndex_Type(Integer32):
    """Custom type gs2326RADIUSAuthStatisticsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2326RADIUSAuthStatisticsServerIndex_Type.__name__ = "Integer32"
_Gs2326RADIUSAuthStatisticsServerIndex_Object = MibTableColumn
gs2326RADIUSAuthStatisticsServerIndex = _Gs2326RADIUSAuthStatisticsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 1),
    _Gs2326RADIUSAuthStatisticsServerIndex_Type()
)
gs2326RADIUSAuthStatisticsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsServerIndex.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktAccessAccepts_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktAccessAccepts_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktAccessAccepts = _Gs2326RADIUSAuthStatisticsRecPktAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 2),
    _Gs2326RADIUSAuthStatisticsRecPktAccessAccepts_Type()
)
gs2326RADIUSAuthStatisticsRecPktAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktAccessAccepts.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktAccessRejects_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktAccessRejects_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktAccessRejects = _Gs2326RADIUSAuthStatisticsRecPktAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 3),
    _Gs2326RADIUSAuthStatisticsRecPktAccessRejects_Type()
)
gs2326RADIUSAuthStatisticsRecPktAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktAccessRejects.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktAccessChallenges_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktAccessChallenges_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktAccessChallenges = _Gs2326RADIUSAuthStatisticsRecPktAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 4),
    _Gs2326RADIUSAuthStatisticsRecPktAccessChallenges_Type()
)
gs2326RADIUSAuthStatisticsRecPktAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktAccessChallenges.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses = _Gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 5),
    _Gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses_Type()
)
gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktBadAuthenticators = _Gs2326RADIUSAuthStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 6),
    _Gs2326RADIUSAuthStatisticsRecPktBadAuthenticators_Type()
)
gs2326RADIUSAuthStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktUnknownTypes = _Gs2326RADIUSAuthStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 7),
    _Gs2326RADIUSAuthStatisticsRecPktUnknownTypes_Type()
)
gs2326RADIUSAuthStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2326RADIUSAuthStatisticsRecPktDropped_Type = Counter32
_Gs2326RADIUSAuthStatisticsRecPktDropped_Object = MibTableColumn
gs2326RADIUSAuthStatisticsRecPktDropped = _Gs2326RADIUSAuthStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 8),
    _Gs2326RADIUSAuthStatisticsRecPktDropped_Type()
)
gs2326RADIUSAuthStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsRecPktDropped.setStatus("current")
_Gs2326RADIUSAuthStatisticsTransmitPktAccessRequests_Type = Counter32
_Gs2326RADIUSAuthStatisticsTransmitPktAccessRequests_Object = MibTableColumn
gs2326RADIUSAuthStatisticsTransmitPktAccessRequests = _Gs2326RADIUSAuthStatisticsTransmitPktAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 9),
    _Gs2326RADIUSAuthStatisticsTransmitPktAccessRequests_Type()
)
gs2326RADIUSAuthStatisticsTransmitPktAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsTransmitPktAccessRequests.setStatus("current")
_Gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type = Counter32
_Gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object = MibTableColumn
gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions = _Gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 10),
    _Gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type()
)
gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions.setStatus("current")
_Gs2326RADIUSAuthStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2326RADIUSAuthStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2326RADIUSAuthStatisticsTransmitPktPendingRequests = _Gs2326RADIUSAuthStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 11),
    _Gs2326RADIUSAuthStatisticsTransmitPktPendingRequests_Type()
)
gs2326RADIUSAuthStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2326RADIUSAuthStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2326RADIUSAuthStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2326RADIUSAuthStatisticsTransmitPktTimeouts = _Gs2326RADIUSAuthStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 12),
    _Gs2326RADIUSAuthStatisticsTransmitPktTimeouts_Type()
)
gs2326RADIUSAuthStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2326RADIUSAuthIP_Type = DisplayString
_Gs2326RADIUSAuthIP_Object = MibTableColumn
gs2326RADIUSAuthIP = _Gs2326RADIUSAuthIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 13),
    _Gs2326RADIUSAuthIP_Type()
)
gs2326RADIUSAuthIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthIP.setStatus("current")
_Gs2326RADIUSAuthState_Type = DisplayString
_Gs2326RADIUSAuthState_Object = MibTableColumn
gs2326RADIUSAuthState = _Gs2326RADIUSAuthState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 14),
    _Gs2326RADIUSAuthState_Type()
)
gs2326RADIUSAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthState.setStatus("current")
_Gs2326RADIUSAuthRoundTripTime_Type = DisplayString
_Gs2326RADIUSAuthRoundTripTime_Object = MibTableColumn
gs2326RADIUSAuthRoundTripTime = _Gs2326RADIUSAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 15),
    _Gs2326RADIUSAuthRoundTripTime_Type()
)
gs2326RADIUSAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAuthRoundTripTime.setStatus("current")
_Gs2326RADIUSAccountingStatisticsRecPktResponses_Type = Counter32
_Gs2326RADIUSAccountingStatisticsRecPktResponses_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsRecPktResponses = _Gs2326RADIUSAccountingStatisticsRecPktResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 16),
    _Gs2326RADIUSAccountingStatisticsRecPktResponses_Type()
)
gs2326RADIUSAccountingStatisticsRecPktResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsRecPktResponses.setStatus("current")
_Gs2326RADIUSAccountingStatisticsRecPktMalformedResponses_Type = Counter32
_Gs2326RADIUSAccountingStatisticsRecPktMalformedResponses_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsRecPktMalformedResponses = _Gs2326RADIUSAccountingStatisticsRecPktMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 17),
    _Gs2326RADIUSAccountingStatisticsRecPktMalformedResponses_Type()
)
gs2326RADIUSAccountingStatisticsRecPktMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsRecPktMalformedResponses.setStatus("current")
_Gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators = _Gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 18),
    _Gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators_Type()
)
gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2326RADIUSAccountingStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2326RADIUSAccountingStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsRecPktUnknownTypes = _Gs2326RADIUSAccountingStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 19),
    _Gs2326RADIUSAccountingStatisticsRecPktUnknownTypes_Type()
)
gs2326RADIUSAccountingStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2326RADIUSAccountingStatisticsRecPktDropped_Type = Counter32
_Gs2326RADIUSAccountingStatisticsRecPktDropped_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsRecPktDropped = _Gs2326RADIUSAccountingStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 20),
    _Gs2326RADIUSAccountingStatisticsRecPktDropped_Type()
)
gs2326RADIUSAccountingStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsRecPktDropped.setStatus("current")
_Gs2326RADIUSAccountingStatisticsTransmitPktRequests_Type = Counter32
_Gs2326RADIUSAccountingStatisticsTransmitPktRequests_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsTransmitPktRequests = _Gs2326RADIUSAccountingStatisticsTransmitPktRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 21),
    _Gs2326RADIUSAccountingStatisticsTransmitPktRequests_Type()
)
gs2326RADIUSAccountingStatisticsTransmitPktRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsTransmitPktRequests.setStatus("current")
_Gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions_Type = Counter32
_Gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions = _Gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 22),
    _Gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions_Type()
)
gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions.setStatus("current")
_Gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests = _Gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 23),
    _Gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests_Type()
)
gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2326RADIUSAccountingStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2326RADIUSAccountingStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2326RADIUSAccountingStatisticsTransmitPktTimeouts = _Gs2326RADIUSAccountingStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 24),
    _Gs2326RADIUSAccountingStatisticsTransmitPktTimeouts_Type()
)
gs2326RADIUSAccountingStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2326RADIUSAccountingIP_Type = DisplayString
_Gs2326RADIUSAccountingIP_Object = MibTableColumn
gs2326RADIUSAccountingIP = _Gs2326RADIUSAccountingIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 25),
    _Gs2326RADIUSAccountingIP_Type()
)
gs2326RADIUSAccountingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingIP.setStatus("current")
_Gs2326RADIUSAccountingState_Type = DisplayString
_Gs2326RADIUSAccountingState_Object = MibTableColumn
gs2326RADIUSAccountingState = _Gs2326RADIUSAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 26),
    _Gs2326RADIUSAccountingState_Type()
)
gs2326RADIUSAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingState.setStatus("current")
_Gs2326RADIUSAccountingRoundTripTime_Type = DisplayString
_Gs2326RADIUSAccountingRoundTripTime_Object = MibTableColumn
gs2326RADIUSAccountingRoundTripTime = _Gs2326RADIUSAccountingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 27),
    _Gs2326RADIUSAccountingRoundTripTime_Type()
)
gs2326RADIUSAccountingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326RADIUSAccountingRoundTripTime.setStatus("current")


class _Gs2326RADIUSStatisticsClear_Type(Integer32):
    """Custom type gs2326RADIUSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2326RADIUSStatisticsClear_Type.__name__ = "Integer32"
_Gs2326RADIUSStatisticsClear_Object = MibTableColumn
gs2326RADIUSStatisticsClear = _Gs2326RADIUSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 10, 6, 1, 28),
    _Gs2326RADIUSStatisticsClear_Type()
)
gs2326RADIUSStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RADIUSStatisticsClear.setStatus("current")
_Gs2326NAS_ObjectIdentity = ObjectIdentity
gs2326NAS = _Gs2326NAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11)
)
_Gs2326NASConfiguration_ObjectIdentity = ObjectIdentity
gs2326NASConfiguration = _Gs2326NASConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1)
)


class _Gs2326NASConfigMode_Type(Integer32):
    """Custom type gs2326NASConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigMode_Type.__name__ = "Integer32"
_Gs2326NASConfigMode_Object = MibScalar
gs2326NASConfigMode = _Gs2326NASConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 1),
    _Gs2326NASConfigMode_Type()
)
gs2326NASConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigMode.setStatus("current")


class _Gs2326NASConfigReauthEnabled_Type(Integer32):
    """Custom type gs2326NASConfigReauthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigReauthEnabled_Type.__name__ = "Integer32"
_Gs2326NASConfigReauthEnabled_Object = MibScalar
gs2326NASConfigReauthEnabled = _Gs2326NASConfigReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 2),
    _Gs2326NASConfigReauthEnabled_Type()
)
gs2326NASConfigReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigReauthEnabled.setStatus("current")


class _Gs2326NASConfigReauthPeriod_Type(Integer32):
    """Custom type gs2326NASConfigReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Gs2326NASConfigReauthPeriod_Type.__name__ = "Integer32"
_Gs2326NASConfigReauthPeriod_Object = MibScalar
gs2326NASConfigReauthPeriod = _Gs2326NASConfigReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 3),
    _Gs2326NASConfigReauthPeriod_Type()
)
gs2326NASConfigReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigReauthPeriod.setStatus("current")


class _Gs2326NASConfigEAPOLTimeout_Type(Integer32):
    """Custom type gs2326NASConfigEAPOLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2326NASConfigEAPOLTimeout_Type.__name__ = "Integer32"
_Gs2326NASConfigEAPOLTimeout_Object = MibScalar
gs2326NASConfigEAPOLTimeout = _Gs2326NASConfigEAPOLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 4),
    _Gs2326NASConfigEAPOLTimeout_Type()
)
gs2326NASConfigEAPOLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigEAPOLTimeout.setStatus("current")


class _Gs2326NASConfigAgingPeriod_Type(Integer32):
    """Custom type gs2326NASConfigAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2326NASConfigAgingPeriod_Type.__name__ = "Integer32"
_Gs2326NASConfigAgingPeriod_Object = MibScalar
gs2326NASConfigAgingPeriod = _Gs2326NASConfigAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 5),
    _Gs2326NASConfigAgingPeriod_Type()
)
gs2326NASConfigAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigAgingPeriod.setStatus("current")


class _Gs2326NASConfigHoldTime_Type(Integer32):
    """Custom type gs2326NASConfigHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2326NASConfigHoldTime_Type.__name__ = "Integer32"
_Gs2326NASConfigHoldTime_Object = MibScalar
gs2326NASConfigHoldTime = _Gs2326NASConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 6),
    _Gs2326NASConfigHoldTime_Type()
)
gs2326NASConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigHoldTime.setStatus("current")


class _Gs2326NASConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2326NASConfigRADIUSAssignedQoSEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2326NASConfigRADIUSAssignedQoSEnabled_Object = MibScalar
gs2326NASConfigRADIUSAssignedQoSEnabled = _Gs2326NASConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 7),
    _Gs2326NASConfigRADIUSAssignedQoSEnabled_Type()
)
gs2326NASConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2326NASConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2326NASConfigRADIUSAssignedVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2326NASConfigRADIUSAssignedVLANEnabled_Object = MibScalar
gs2326NASConfigRADIUSAssignedVLANEnabled = _Gs2326NASConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 8),
    _Gs2326NASConfigRADIUSAssignedVLANEnabled_Type()
)
gs2326NASConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2326NASConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2326NASConfigGuestVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2326NASConfigGuestVLANEnabled_Object = MibScalar
gs2326NASConfigGuestVLANEnabled = _Gs2326NASConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 9),
    _Gs2326NASConfigGuestVLANEnabled_Type()
)
gs2326NASConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigGuestVLANEnabled.setStatus("current")


class _Gs2326NASConfigGuestVLANID_Type(Integer32):
    """Custom type gs2326NASConfigGuestVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2326NASConfigGuestVLANID_Type.__name__ = "Integer32"
_Gs2326NASConfigGuestVLANID_Object = MibScalar
gs2326NASConfigGuestVLANID = _Gs2326NASConfigGuestVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 10),
    _Gs2326NASConfigGuestVLANID_Type()
)
gs2326NASConfigGuestVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigGuestVLANID.setStatus("current")


class _Gs2326NASConfigMaxReauthCount_Type(Integer32):
    """Custom type gs2326NASConfigMaxReauthCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2326NASConfigMaxReauthCount_Type.__name__ = "Integer32"
_Gs2326NASConfigMaxReauthCount_Object = MibScalar
gs2326NASConfigMaxReauthCount = _Gs2326NASConfigMaxReauthCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 11),
    _Gs2326NASConfigMaxReauthCount_Type()
)
gs2326NASConfigMaxReauthCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigMaxReauthCount.setStatus("current")


class _Gs2326NASConfigAllowGuestVLANEAPOLSeen_Type(Integer32):
    """Custom type gs2326NASConfigAllowGuestVLANEAPOLSeen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigAllowGuestVLANEAPOLSeen_Type.__name__ = "Integer32"
_Gs2326NASConfigAllowGuestVLANEAPOLSeen_Object = MibScalar
gs2326NASConfigAllowGuestVLANEAPOLSeen = _Gs2326NASConfigAllowGuestVLANEAPOLSeen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 12),
    _Gs2326NASConfigAllowGuestVLANEAPOLSeen_Type()
)
gs2326NASConfigAllowGuestVLANEAPOLSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigAllowGuestVLANEAPOLSeen.setStatus("current")
_Gs2326NASPortConfigTable_Object = MibTable
gs2326NASPortConfigTable = _Gs2326NASPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13)
)
if mibBuilder.loadTexts:
    gs2326NASPortConfigTable.setStatus("current")
_Gs2326NASPortConfigEntry_Object = MibTableRow
gs2326NASPortConfigEntry = _Gs2326NASPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1)
)
gs2326NASPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2326NASPortConfigEntry.setStatus("current")


class _Gs2326NASPortConfigPort_Type(Integer32):
    """Custom type gs2326NASPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2326NASPortConfigPort_Type.__name__ = "Integer32"
_Gs2326NASPortConfigPort_Object = MibTableColumn
gs2326NASPortConfigPort = _Gs2326NASPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 1),
    _Gs2326NASPortConfigPort_Type()
)
gs2326NASPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326NASPortConfigPort.setStatus("current")


class _Gs2326NASPortConfigAdminState_Type(Integer32):
    """Custom type gs2326NASPortConfigAdminState based on Integer32"""
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


_Gs2326NASPortConfigAdminState_Type.__name__ = "Integer32"
_Gs2326NASPortConfigAdminState_Object = MibTableColumn
gs2326NASPortConfigAdminState = _Gs2326NASPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 2),
    _Gs2326NASPortConfigAdminState_Type()
)
gs2326NASPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigAdminState.setStatus("current")


class _Gs2326NASPortConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2326NASPortConfigRADIUSAssignedQoSEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASPortConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2326NASPortConfigRADIUSAssignedQoSEnabled_Object = MibTableColumn
gs2326NASPortConfigRADIUSAssignedQoSEnabled = _Gs2326NASPortConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 3),
    _Gs2326NASPortConfigRADIUSAssignedQoSEnabled_Type()
)
gs2326NASPortConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2326NASPortConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2326NASPortConfigRADIUSAssignedVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASPortConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2326NASPortConfigRADIUSAssignedVLANEnabled_Object = MibTableColumn
gs2326NASPortConfigRADIUSAssignedVLANEnabled = _Gs2326NASPortConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 4),
    _Gs2326NASPortConfigRADIUSAssignedVLANEnabled_Type()
)
gs2326NASPortConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2326NASPortConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2326NASPortConfigGuestVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASPortConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2326NASPortConfigGuestVLANEnabled_Object = MibTableColumn
gs2326NASPortConfigGuestVLANEnabled = _Gs2326NASPortConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 5),
    _Gs2326NASPortConfigGuestVLANEnabled_Type()
)
gs2326NASPortConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigGuestVLANEnabled.setStatus("current")
_Gs2326NASPortConfigPortState_Type = DisplayString
_Gs2326NASPortConfigPortState_Object = MibTableColumn
gs2326NASPortConfigPortState = _Gs2326NASPortConfigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 6),
    _Gs2326NASPortConfigPortState_Type()
)
gs2326NASPortConfigPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASPortConfigPortState.setStatus("current")


class _Gs2326NASPortConfigReauthenticate_Type(Integer32):
    """Custom type gs2326NASPortConfigReauthenticate based on Integer32"""
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


_Gs2326NASPortConfigReauthenticate_Type.__name__ = "Integer32"
_Gs2326NASPortConfigReauthenticate_Object = MibTableColumn
gs2326NASPortConfigReauthenticate = _Gs2326NASPortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 7),
    _Gs2326NASPortConfigReauthenticate_Type()
)
gs2326NASPortConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigReauthenticate.setStatus("current")


class _Gs2326NASPortConfigReinitialize_Type(Integer32):
    """Custom type gs2326NASPortConfigReinitialize based on Integer32"""
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


_Gs2326NASPortConfigReinitialize_Type.__name__ = "Integer32"
_Gs2326NASPortConfigReinitialize_Object = MibTableColumn
gs2326NASPortConfigReinitialize = _Gs2326NASPortConfigReinitialize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 8),
    _Gs2326NASPortConfigReinitialize_Type()
)
gs2326NASPortConfigReinitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigReinitialize.setStatus("current")


class _Gs2326NASPortConfigFallbackEnabled_Type(Integer32):
    """Custom type gs2326NASPortConfigFallbackEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASPortConfigFallbackEnabled_Type.__name__ = "Integer32"
_Gs2326NASPortConfigFallbackEnabled_Object = MibTableColumn
gs2326NASPortConfigFallbackEnabled = _Gs2326NASPortConfigFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 13, 1, 101),
    _Gs2326NASPortConfigFallbackEnabled_Type()
)
gs2326NASPortConfigFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASPortConfigFallbackEnabled.setStatus("current")


class _Gs2326NASConfigMacBasedUseEAP_Type(Integer32):
    """Custom type gs2326NASConfigMacBasedUseEAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326NASConfigMacBasedUseEAP_Type.__name__ = "Integer32"
_Gs2326NASConfigMacBasedUseEAP_Object = MibScalar
gs2326NASConfigMacBasedUseEAP = _Gs2326NASConfigMacBasedUseEAP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 1, 101),
    _Gs2326NASConfigMacBasedUseEAP_Type()
)
gs2326NASConfigMacBasedUseEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASConfigMacBasedUseEAP.setStatus("current")
_Gs2326NASSwitchStatusTable_Object = MibTable
gs2326NASSwitchStatusTable = _Gs2326NASSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2)
)
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusTable.setStatus("current")
_Gs2326NASSwitchStatusEntry_Object = MibTableRow
gs2326NASSwitchStatusEntry = _Gs2326NASSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1)
)
gs2326NASSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusEntry.setStatus("current")
_Gs2326NASSwitchStatusAdminState_Type = DisplayString
_Gs2326NASSwitchStatusAdminState_Object = MibTableColumn
gs2326NASSwitchStatusAdminState = _Gs2326NASSwitchStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1, 2),
    _Gs2326NASSwitchStatusAdminState_Type()
)
gs2326NASSwitchStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusAdminState.setStatus("current")
_Gs2326NASSwitchStatusPortState_Type = DisplayString
_Gs2326NASSwitchStatusPortState_Object = MibTableColumn
gs2326NASSwitchStatusPortState = _Gs2326NASSwitchStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1, 3),
    _Gs2326NASSwitchStatusPortState_Type()
)
gs2326NASSwitchStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusPortState.setStatus("current")
_Gs2326NASSwitchStatusLastSource_Type = DisplayString
_Gs2326NASSwitchStatusLastSource_Object = MibTableColumn
gs2326NASSwitchStatusLastSource = _Gs2326NASSwitchStatusLastSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1, 4),
    _Gs2326NASSwitchStatusLastSource_Type()
)
gs2326NASSwitchStatusLastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusLastSource.setStatus("current")
_Gs2326NASSwitchStatusLastID_Type = DisplayString
_Gs2326NASSwitchStatusLastID_Object = MibTableColumn
gs2326NASSwitchStatusLastID = _Gs2326NASSwitchStatusLastID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1, 5),
    _Gs2326NASSwitchStatusLastID_Type()
)
gs2326NASSwitchStatusLastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusLastID.setStatus("current")
_Gs2326NASSwitchStatusQoSClass_Type = DisplayString
_Gs2326NASSwitchStatusQoSClass_Object = MibTableColumn
gs2326NASSwitchStatusQoSClass = _Gs2326NASSwitchStatusQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1, 6),
    _Gs2326NASSwitchStatusQoSClass_Type()
)
gs2326NASSwitchStatusQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusQoSClass.setStatus("current")
_Gs2326NASSwitchStatusPortVlanID_Type = DisplayString
_Gs2326NASSwitchStatusPortVlanID_Object = MibTableColumn
gs2326NASSwitchStatusPortVlanID = _Gs2326NASSwitchStatusPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 2, 1, 7),
    _Gs2326NASSwitchStatusPortVlanID_Type()
)
gs2326NASSwitchStatusPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASSwitchStatusPortVlanID.setStatus("current")
_Gs2326NASPortStatus_ObjectIdentity = ObjectIdentity
gs2326NASPortStatus = _Gs2326NASPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3)
)
_Gs2326NASPortStatusCountersTable_Object = MibTable
gs2326NASPortStatusCountersTable = _Gs2326NASPortStatusCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    gs2326NASPortStatusCountersTable.setStatus("current")
_Gs2326NASPortStatusCountersEntry_Object = MibTableRow
gs2326NASPortStatusCountersEntry = _Gs2326NASPortStatusCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1)
)
gs2326NASPortStatusCountersEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326NASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2326NASPortStatusCountersEntry.setStatus("current")
_Gs2326NASRxCountersEAPOLTotal_Type = Counter32
_Gs2326NASRxCountersEAPOLTotal_Object = MibTableColumn
gs2326NASRxCountersEAPOLTotal = _Gs2326NASRxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 2),
    _Gs2326NASRxCountersEAPOLTotal_Type()
)
gs2326NASRxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLTotal.setStatus("current")
_Gs2326NASRxCountersEAPOLResponseID_Type = Counter32
_Gs2326NASRxCountersEAPOLResponseID_Object = MibTableColumn
gs2326NASRxCountersEAPOLResponseID = _Gs2326NASRxCountersEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 3),
    _Gs2326NASRxCountersEAPOLResponseID_Type()
)
gs2326NASRxCountersEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLResponseID.setStatus("current")
_Gs2326NASRxCountersEAPOLResponses_Type = Counter32
_Gs2326NASRxCountersEAPOLResponses_Object = MibTableColumn
gs2326NASRxCountersEAPOLResponses = _Gs2326NASRxCountersEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 4),
    _Gs2326NASRxCountersEAPOLResponses_Type()
)
gs2326NASRxCountersEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLResponses.setStatus("current")
_Gs2326NASRxCountersEAPOLStart_Type = Counter32
_Gs2326NASRxCountersEAPOLStart_Object = MibTableColumn
gs2326NASRxCountersEAPOLStart = _Gs2326NASRxCountersEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 5),
    _Gs2326NASRxCountersEAPOLStart_Type()
)
gs2326NASRxCountersEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLStart.setStatus("current")
_Gs2326NASRxCountersEAPOLLogoff_Type = Counter32
_Gs2326NASRxCountersEAPOLLogoff_Object = MibTableColumn
gs2326NASRxCountersEAPOLLogoff = _Gs2326NASRxCountersEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 6),
    _Gs2326NASRxCountersEAPOLLogoff_Type()
)
gs2326NASRxCountersEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLLogoff.setStatus("current")
_Gs2326NASRxCountersEAPOLInvalidType_Type = Counter32
_Gs2326NASRxCountersEAPOLInvalidType_Object = MibTableColumn
gs2326NASRxCountersEAPOLInvalidType = _Gs2326NASRxCountersEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 7),
    _Gs2326NASRxCountersEAPOLInvalidType_Type()
)
gs2326NASRxCountersEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLInvalidType.setStatus("current")
_Gs2326NASRxCountersEAPOLInvalidLength_Type = Counter32
_Gs2326NASRxCountersEAPOLInvalidLength_Object = MibTableColumn
gs2326NASRxCountersEAPOLInvalidLength = _Gs2326NASRxCountersEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 8),
    _Gs2326NASRxCountersEAPOLInvalidLength_Type()
)
gs2326NASRxCountersEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxCountersEAPOLInvalidLength.setStatus("current")
_Gs2326NASTxCountersEAPOLTotal_Type = Counter32
_Gs2326NASTxCountersEAPOLTotal_Object = MibTableColumn
gs2326NASTxCountersEAPOLTotal = _Gs2326NASTxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 9),
    _Gs2326NASTxCountersEAPOLTotal_Type()
)
gs2326NASTxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxCountersEAPOLTotal.setStatus("current")
_Gs2326NASTxCountersEAPOLRequestID_Type = Counter32
_Gs2326NASTxCountersEAPOLRequestID_Object = MibTableColumn
gs2326NASTxCountersEAPOLRequestID = _Gs2326NASTxCountersEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 10),
    _Gs2326NASTxCountersEAPOLRequestID_Type()
)
gs2326NASTxCountersEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxCountersEAPOLRequestID.setStatus("current")
_Gs2326NASTxCountersEAPOLRequests_Type = Counter32
_Gs2326NASTxCountersEAPOLRequests_Object = MibTableColumn
gs2326NASTxCountersEAPOLRequests = _Gs2326NASTxCountersEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 11),
    _Gs2326NASTxCountersEAPOLRequests_Type()
)
gs2326NASTxCountersEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxCountersEAPOLRequests.setStatus("current")
_Gs2326NASRxBackendServerCountersAccessChallenges_Type = Counter32
_Gs2326NASRxBackendServerCountersAccessChallenges_Object = MibTableColumn
gs2326NASRxBackendServerCountersAccessChallenges = _Gs2326NASRxBackendServerCountersAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 12),
    _Gs2326NASRxBackendServerCountersAccessChallenges_Type()
)
gs2326NASRxBackendServerCountersAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerCountersAccessChallenges.setStatus("current")
_Gs2326NASRxBackendServerCountersOtherRequests_Type = Counter32
_Gs2326NASRxBackendServerCountersOtherRequests_Object = MibTableColumn
gs2326NASRxBackendServerCountersOtherRequests = _Gs2326NASRxBackendServerCountersOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 13),
    _Gs2326NASRxBackendServerCountersOtherRequests_Type()
)
gs2326NASRxBackendServerCountersOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerCountersOtherRequests.setStatus("current")
_Gs2326NASRxBackendServerCountersAuthSuccesses_Type = Counter32
_Gs2326NASRxBackendServerCountersAuthSuccesses_Object = MibTableColumn
gs2326NASRxBackendServerCountersAuthSuccesses = _Gs2326NASRxBackendServerCountersAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 14),
    _Gs2326NASRxBackendServerCountersAuthSuccesses_Type()
)
gs2326NASRxBackendServerCountersAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerCountersAuthSuccesses.setStatus("current")
_Gs2326NASRxBackendServerCountersAuthFailures_Type = Counter32
_Gs2326NASRxBackendServerCountersAuthFailures_Object = MibTableColumn
gs2326NASRxBackendServerCountersAuthFailures = _Gs2326NASRxBackendServerCountersAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 15),
    _Gs2326NASRxBackendServerCountersAuthFailures_Type()
)
gs2326NASRxBackendServerCountersAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerCountersAuthFailures.setStatus("current")
_Gs2326NASTxBackendServerCountersResponses_Type = Counter32
_Gs2326NASTxBackendServerCountersResponses_Object = MibTableColumn
gs2326NASTxBackendServerCountersResponses = _Gs2326NASTxBackendServerCountersResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 16),
    _Gs2326NASTxBackendServerCountersResponses_Type()
)
gs2326NASTxBackendServerCountersResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxBackendServerCountersResponses.setStatus("current")
_Gs2326NASLastSupplicantInfoMACAddress_Type = DisplayString
_Gs2326NASLastSupplicantInfoMACAddress_Object = MibTableColumn
gs2326NASLastSupplicantInfoMACAddress = _Gs2326NASLastSupplicantInfoMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 17),
    _Gs2326NASLastSupplicantInfoMACAddress_Type()
)
gs2326NASLastSupplicantInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASLastSupplicantInfoMACAddress.setStatus("current")
_Gs2326NASLastSupplicantInfoVlanID_Type = Integer32
_Gs2326NASLastSupplicantInfoVlanID_Object = MibTableColumn
gs2326NASLastSupplicantInfoVlanID = _Gs2326NASLastSupplicantInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 18),
    _Gs2326NASLastSupplicantInfoVlanID_Type()
)
gs2326NASLastSupplicantInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASLastSupplicantInfoVlanID.setStatus("current")
_Gs2326NASLastSupplicantInfoVersion_Type = Integer32
_Gs2326NASLastSupplicantInfoVersion_Object = MibTableColumn
gs2326NASLastSupplicantInfoVersion = _Gs2326NASLastSupplicantInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 19),
    _Gs2326NASLastSupplicantInfoVersion_Type()
)
gs2326NASLastSupplicantInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASLastSupplicantInfoVersion.setStatus("current")
_Gs2326NASLastSupplicantInfoIdentity_Type = DisplayString
_Gs2326NASLastSupplicantInfoIdentity_Object = MibTableColumn
gs2326NASLastSupplicantInfoIdentity = _Gs2326NASLastSupplicantInfoIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 20),
    _Gs2326NASLastSupplicantInfoIdentity_Type()
)
gs2326NASLastSupplicantInfoIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASLastSupplicantInfoIdentity.setStatus("current")


class _Gs2326NASCountersDoClear_Type(Integer32):
    """Custom type gs2326NASCountersDoClear based on Integer32"""
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


_Gs2326NASCountersDoClear_Type.__name__ = "Integer32"
_Gs2326NASCountersDoClear_Object = MibTableColumn
gs2326NASCountersDoClear = _Gs2326NASCountersDoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 1, 1, 21),
    _Gs2326NASCountersDoClear_Type()
)
gs2326NASCountersDoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326NASCountersDoClear.setStatus("current")
_Gs2326NASPortStatusClientsTable_Object = MibTable
gs2326NASPortStatusClientsTable = _Gs2326NASPortStatusClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gs2326NASPortStatusClientsTable.setStatus("current")
_Gs2326NASPortStatusClientsEntry_Object = MibTableRow
gs2326NASPortStatusClientsEntry = _Gs2326NASPortStatusClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1)
)
gs2326NASPortStatusClientsEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326NASPortConfigPort"),
    (0, "LANCOM-GS-2326-MIB", "gs2326NASClientsIndex"),
)
if mibBuilder.loadTexts:
    gs2326NASPortStatusClientsEntry.setStatus("current")


class _Gs2326NASClientsIndex_Type(Integer32):
    """Custom type gs2326NASClientsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2326NASClientsIndex_Type.__name__ = "Integer32"
_Gs2326NASClientsIndex_Object = MibTableColumn
gs2326NASClientsIndex = _Gs2326NASClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 1),
    _Gs2326NASClientsIndex_Type()
)
gs2326NASClientsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326NASClientsIndex.setStatus("current")
_Gs2326NASClientsIdentity_Type = DisplayString
_Gs2326NASClientsIdentity_Object = MibTableColumn
gs2326NASClientsIdentity = _Gs2326NASClientsIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 2),
    _Gs2326NASClientsIdentity_Type()
)
gs2326NASClientsIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASClientsIdentity.setStatus("current")
_Gs2326NASClientsMACAddress_Type = DisplayString
_Gs2326NASClientsMACAddress_Object = MibTableColumn
gs2326NASClientsMACAddress = _Gs2326NASClientsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 3),
    _Gs2326NASClientsMACAddress_Type()
)
gs2326NASClientsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASClientsMACAddress.setStatus("current")


class _Gs2326NASClientsVlanID_Type(Integer32):
    """Custom type gs2326NASClientsVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326NASClientsVlanID_Type.__name__ = "Integer32"
_Gs2326NASClientsVlanID_Object = MibTableColumn
gs2326NASClientsVlanID = _Gs2326NASClientsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 4),
    _Gs2326NASClientsVlanID_Type()
)
gs2326NASClientsVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASClientsVlanID.setStatus("current")
_Gs2326NASClientsState_Type = DisplayString
_Gs2326NASClientsState_Object = MibTableColumn
gs2326NASClientsState = _Gs2326NASClientsState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 5),
    _Gs2326NASClientsState_Type()
)
gs2326NASClientsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASClientsState.setStatus("current")
_Gs2326NASClientsLastAuth_Type = DisplayString
_Gs2326NASClientsLastAuth_Object = MibTableColumn
gs2326NASClientsLastAuth = _Gs2326NASClientsLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 6),
    _Gs2326NASClientsLastAuth_Type()
)
gs2326NASClientsLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASClientsLastAuth.setStatus("current")
_Gs2326NASRxClientsEAPOLTotal_Type = Counter32
_Gs2326NASRxClientsEAPOLTotal_Object = MibTableColumn
gs2326NASRxClientsEAPOLTotal = _Gs2326NASRxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 7),
    _Gs2326NASRxClientsEAPOLTotal_Type()
)
gs2326NASRxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLTotal.setStatus("current")
_Gs2326NASRxClientsEAPOLResponseID_Type = Counter32
_Gs2326NASRxClientsEAPOLResponseID_Object = MibTableColumn
gs2326NASRxClientsEAPOLResponseID = _Gs2326NASRxClientsEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 8),
    _Gs2326NASRxClientsEAPOLResponseID_Type()
)
gs2326NASRxClientsEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLResponseID.setStatus("current")
_Gs2326NASRxClientsEAPOLResponses_Type = Counter32
_Gs2326NASRxClientsEAPOLResponses_Object = MibTableColumn
gs2326NASRxClientsEAPOLResponses = _Gs2326NASRxClientsEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 9),
    _Gs2326NASRxClientsEAPOLResponses_Type()
)
gs2326NASRxClientsEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLResponses.setStatus("current")
_Gs2326NASRxClientsEAPOLStart_Type = Counter32
_Gs2326NASRxClientsEAPOLStart_Object = MibTableColumn
gs2326NASRxClientsEAPOLStart = _Gs2326NASRxClientsEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 10),
    _Gs2326NASRxClientsEAPOLStart_Type()
)
gs2326NASRxClientsEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLStart.setStatus("current")
_Gs2326NASRxClientsEAPOLLogoff_Type = Counter32
_Gs2326NASRxClientsEAPOLLogoff_Object = MibTableColumn
gs2326NASRxClientsEAPOLLogoff = _Gs2326NASRxClientsEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 11),
    _Gs2326NASRxClientsEAPOLLogoff_Type()
)
gs2326NASRxClientsEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLLogoff.setStatus("current")
_Gs2326NASRxClientsEAPOLInvalidType_Type = Counter32
_Gs2326NASRxClientsEAPOLInvalidType_Object = MibTableColumn
gs2326NASRxClientsEAPOLInvalidType = _Gs2326NASRxClientsEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 12),
    _Gs2326NASRxClientsEAPOLInvalidType_Type()
)
gs2326NASRxClientsEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLInvalidType.setStatus("current")
_Gs2326NASRxClientsEAPOLInvalidLength_Type = Counter32
_Gs2326NASRxClientsEAPOLInvalidLength_Object = MibTableColumn
gs2326NASRxClientsEAPOLInvalidLength = _Gs2326NASRxClientsEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 13),
    _Gs2326NASRxClientsEAPOLInvalidLength_Type()
)
gs2326NASRxClientsEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxClientsEAPOLInvalidLength.setStatus("current")
_Gs2326NASTxClientsEAPOLTotal_Type = Counter32
_Gs2326NASTxClientsEAPOLTotal_Object = MibTableColumn
gs2326NASTxClientsEAPOLTotal = _Gs2326NASTxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 14),
    _Gs2326NASTxClientsEAPOLTotal_Type()
)
gs2326NASTxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxClientsEAPOLTotal.setStatus("current")
_Gs2326NASTxClientsEAPOLRequestID_Type = Counter32
_Gs2326NASTxClientsEAPOLRequestID_Object = MibTableColumn
gs2326NASTxClientsEAPOLRequestID = _Gs2326NASTxClientsEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 15),
    _Gs2326NASTxClientsEAPOLRequestID_Type()
)
gs2326NASTxClientsEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxClientsEAPOLRequestID.setStatus("current")
_Gs2326NASTxClientsEAPOLRequests_Type = Counter32
_Gs2326NASTxClientsEAPOLRequests_Object = MibTableColumn
gs2326NASTxClientsEAPOLRequests = _Gs2326NASTxClientsEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 16),
    _Gs2326NASTxClientsEAPOLRequests_Type()
)
gs2326NASTxClientsEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxClientsEAPOLRequests.setStatus("current")
_Gs2326NASRxBackendServerClientsAccessChallenges_Type = Counter32
_Gs2326NASRxBackendServerClientsAccessChallenges_Object = MibTableColumn
gs2326NASRxBackendServerClientsAccessChallenges = _Gs2326NASRxBackendServerClientsAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 17),
    _Gs2326NASRxBackendServerClientsAccessChallenges_Type()
)
gs2326NASRxBackendServerClientsAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerClientsAccessChallenges.setStatus("current")
_Gs2326NASRxBackendServerClientsOtherRequests_Type = Counter32
_Gs2326NASRxBackendServerClientsOtherRequests_Object = MibTableColumn
gs2326NASRxBackendServerClientsOtherRequests = _Gs2326NASRxBackendServerClientsOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 18),
    _Gs2326NASRxBackendServerClientsOtherRequests_Type()
)
gs2326NASRxBackendServerClientsOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerClientsOtherRequests.setStatus("current")
_Gs2326NASRxBackendServerClientsAuthSuccesses_Type = Counter32
_Gs2326NASRxBackendServerClientsAuthSuccesses_Object = MibTableColumn
gs2326NASRxBackendServerClientsAuthSuccesses = _Gs2326NASRxBackendServerClientsAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 19),
    _Gs2326NASRxBackendServerClientsAuthSuccesses_Type()
)
gs2326NASRxBackendServerClientsAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerClientsAuthSuccesses.setStatus("current")
_Gs2326NASRxBackendServerClientsAuthFailures_Type = Counter32
_Gs2326NASRxBackendServerClientsAuthFailures_Object = MibTableColumn
gs2326NASRxBackendServerClientsAuthFailures = _Gs2326NASRxBackendServerClientsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 20),
    _Gs2326NASRxBackendServerClientsAuthFailures_Type()
)
gs2326NASRxBackendServerClientsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASRxBackendServerClientsAuthFailures.setStatus("current")
_Gs2326NASTxBackendServerClientsResponses_Type = Counter32
_Gs2326NASTxBackendServerClientsResponses_Object = MibTableColumn
gs2326NASTxBackendServerClientsResponses = _Gs2326NASTxBackendServerClientsResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 3, 11, 3, 2, 1, 21),
    _Gs2326NASTxBackendServerClientsResponses_Type()
)
gs2326NASTxBackendServerClientsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326NASTxBackendServerClientsResponses.setStatus("current")
_Gs2326Maintenance_ObjectIdentity = ObjectIdentity
gs2326Maintenance = _Gs2326Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4)
)


class _Gs2326RestartDevice_Type(Integer32):
    """Custom type gs2326RestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326RestartDevice_Type.__name__ = "Integer32"
_Gs2326RestartDevice_Object = MibScalar
gs2326RestartDevice = _Gs2326RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 1),
    _Gs2326RestartDevice_Type()
)
gs2326RestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RestartDevice.setStatus("current")
_Gs2326Firmware_ObjectIdentity = ObjectIdentity
gs2326Firmware = _Gs2326Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 2)
)
_Gs2326FirmwareIpAddress_Type = IpAddress
_Gs2326FirmwareIpAddress_Object = MibScalar
gs2326FirmwareIpAddress = _Gs2326FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 2, 1),
    _Gs2326FirmwareIpAddress_Type()
)
gs2326FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FirmwareIpAddress.setStatus("current")
_Gs2326FirmwareFileName_Type = DisplayString
_Gs2326FirmwareFileName_Object = MibScalar
gs2326FirmwareFileName = _Gs2326FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 2, 2),
    _Gs2326FirmwareFileName_Type()
)
gs2326FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FirmwareFileName.setStatus("current")


class _Gs2326DoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2326DoFirmwareUpgrade based on Integer32"""
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


_Gs2326DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2326DoFirmwareUpgrade_Object = MibScalar
gs2326DoFirmwareUpgrade = _Gs2326DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 2, 3),
    _Gs2326DoFirmwareUpgrade_Type()
)
gs2326DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DoFirmwareUpgrade.setStatus("current")
_Gs2326SaveOrRestore_ObjectIdentity = ObjectIdentity
gs2326SaveOrRestore = _Gs2326SaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 3)
)


class _Gs2326FactoryDefaults_Type(Integer32):
    """Custom type gs2326FactoryDefaults based on Integer32"""
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


_Gs2326FactoryDefaults_Type.__name__ = "Integer32"
_Gs2326FactoryDefaults_Object = MibScalar
gs2326FactoryDefaults = _Gs2326FactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 3, 1),
    _Gs2326FactoryDefaults_Type()
)
gs2326FactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326FactoryDefaults.setStatus("current")


class _Gs2326SaveStart_Type(Integer32):
    """Custom type gs2326SaveStart based on Integer32"""
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


_Gs2326SaveStart_Type.__name__ = "Integer32"
_Gs2326SaveStart_Object = MibScalar
gs2326SaveStart = _Gs2326SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 3, 2),
    _Gs2326SaveStart_Type()
)
gs2326SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SaveStart.setStatus("current")


class _Gs2326SaveUser_Type(Integer32):
    """Custom type gs2326SaveUser based on Integer32"""
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


_Gs2326SaveUser_Type.__name__ = "Integer32"
_Gs2326SaveUser_Object = MibScalar
gs2326SaveUser = _Gs2326SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 3, 3),
    _Gs2326SaveUser_Type()
)
gs2326SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326SaveUser.setStatus("current")


class _Gs2326RestoreUser_Type(Integer32):
    """Custom type gs2326RestoreUser based on Integer32"""
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


_Gs2326RestoreUser_Type.__name__ = "Integer32"
_Gs2326RestoreUser_Object = MibScalar
gs2326RestoreUser = _Gs2326RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 3, 4),
    _Gs2326RestoreUser_Type()
)
gs2326RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326RestoreUser.setStatus("current")
_Gs2326ExportOrImport_ObjectIdentity = ObjectIdentity
gs2326ExportOrImport = _Gs2326ExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4)
)
_Gs2326ExportIpAddress_Type = IpAddress
_Gs2326ExportIpAddress_Object = MibScalar
gs2326ExportIpAddress = _Gs2326ExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4, 1),
    _Gs2326ExportIpAddress_Type()
)
gs2326ExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ExportIpAddress.setStatus("current")
_Gs2326ExportConfigName_Type = DisplayString
_Gs2326ExportConfigName_Object = MibScalar
gs2326ExportConfigName = _Gs2326ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4, 2),
    _Gs2326ExportConfigName_Type()
)
gs2326ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ExportConfigName.setStatus("current")


class _Gs2326DoExportConfig_Type(Integer32):
    """Custom type gs2326DoExportConfig based on Integer32"""
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


_Gs2326DoExportConfig_Type.__name__ = "Integer32"
_Gs2326DoExportConfig_Object = MibScalar
gs2326DoExportConfig = _Gs2326DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4, 3),
    _Gs2326DoExportConfig_Type()
)
gs2326DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DoExportConfig.setStatus("current")
_Gs2326ImportIpAddress_Type = IpAddress
_Gs2326ImportIpAddress_Object = MibScalar
gs2326ImportIpAddress = _Gs2326ImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4, 4),
    _Gs2326ImportIpAddress_Type()
)
gs2326ImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ImportIpAddress.setStatus("current")
_Gs2326ImportConfigName_Type = DisplayString
_Gs2326ImportConfigName_Object = MibScalar
gs2326ImportConfigName = _Gs2326ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4, 5),
    _Gs2326ImportConfigName_Type()
)
gs2326ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ImportConfigName.setStatus("current")


class _Gs2326DoImportConfig_Type(Integer32):
    """Custom type gs2326DoImportConfig based on Integer32"""
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


_Gs2326DoImportConfig_Type.__name__ = "Integer32"
_Gs2326DoImportConfig_Object = MibScalar
gs2326DoImportConfig = _Gs2326DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 4, 6),
    _Gs2326DoImportConfig_Type()
)
gs2326DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DoImportConfig.setStatus("current")
_Gs2326Diagnostics_ObjectIdentity = ObjectIdentity
gs2326Diagnostics = _Gs2326Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5)
)
_Gs2326PingIpAddress_Type = IpAddress
_Gs2326PingIpAddress_Object = MibScalar
gs2326PingIpAddress = _Gs2326PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 1),
    _Gs2326PingIpAddress_Type()
)
gs2326PingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PingIpAddress.setStatus("current")


class _Gs2326PingSize_Type(Integer32):
    """Custom type gs2326PingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2326PingSize_Type.__name__ = "Integer32"
_Gs2326PingSize_Object = MibScalar
gs2326PingSize = _Gs2326PingSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 2),
    _Gs2326PingSize_Type()
)
gs2326PingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326PingSize.setStatus("current")


class _Gs2326DoPingConfig_Type(Integer32):
    """Custom type gs2326DoPingConfig based on Integer32"""
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


_Gs2326DoPingConfig_Type.__name__ = "Integer32"
_Gs2326DoPingConfig_Object = MibScalar
gs2326DoPingConfig = _Gs2326DoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 3),
    _Gs2326DoPingConfig_Type()
)
gs2326DoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DoPingConfig.setStatus("current")
_Gs2326PingResult_Type = DisplayString
_Gs2326PingResult_Object = MibScalar
gs2326PingResult = _Gs2326PingResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 4),
    _Gs2326PingResult_Type()
)
gs2326PingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326PingResult.setStatus("current")
_Gs2326Ping6IpAddress_Type = DisplayString
_Gs2326Ping6IpAddress_Object = MibScalar
gs2326Ping6IpAddress = _Gs2326Ping6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 5),
    _Gs2326Ping6IpAddress_Type()
)
gs2326Ping6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ping6IpAddress.setStatus("current")


class _Gs2326Ping6Size_Type(Integer32):
    """Custom type gs2326Ping6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2326Ping6Size_Type.__name__ = "Integer32"
_Gs2326Ping6Size_Object = MibScalar
gs2326Ping6Size = _Gs2326Ping6Size_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 6),
    _Gs2326Ping6Size_Type()
)
gs2326Ping6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326Ping6Size.setStatus("current")


class _Gs2326DoPing6Config_Type(Integer32):
    """Custom type gs2326DoPing6Config based on Integer32"""
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


_Gs2326DoPing6Config_Type.__name__ = "Integer32"
_Gs2326DoPing6Config_Object = MibScalar
gs2326DoPing6Config = _Gs2326DoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 7),
    _Gs2326DoPing6Config_Type()
)
gs2326DoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326DoPing6Config.setStatus("current")
_Gs2326Ping6Result_Type = DisplayString
_Gs2326Ping6Result_Object = MibScalar
gs2326Ping6Result = _Gs2326Ping6Result_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 8),
    _Gs2326Ping6Result_Type()
)
gs2326Ping6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Ping6Result.setStatus("current")
_Gs2326VeriPHY_ObjectIdentity = ObjectIdentity
gs2326VeriPHY = _Gs2326VeriPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9)
)


class _Gs2326VeriPHYTest_Type(Integer32):
    """Custom type gs2326VeriPHYTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326VeriPHYTest_Type.__name__ = "Integer32"
_Gs2326VeriPHYTest_Object = MibScalar
gs2326VeriPHYTest = _Gs2326VeriPHYTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 1),
    _Gs2326VeriPHYTest_Type()
)
gs2326VeriPHYTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326VeriPHYTest.setStatus("current")
_Gs2326VeriPHYTable_Object = MibTable
gs2326VeriPHYTable = _Gs2326VeriPHYTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2)
)
if mibBuilder.loadTexts:
    gs2326VeriPHYTable.setStatus("current")
_Gs2326VeriPHYEntry_Object = MibTableRow
gs2326VeriPHYEntry = _Gs2326VeriPHYEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1)
)
gs2326VeriPHYEntry.setIndexNames(
    (0, "LANCOM-GS-2326-MIB", "gs2326VeriPHYPort"),
)
if mibBuilder.loadTexts:
    gs2326VeriPHYEntry.setStatus("current")


class _Gs2326VeriPHYPort_Type(Integer32):
    """Custom type gs2326VeriPHYPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2326VeriPHYPort_Type.__name__ = "Integer32"
_Gs2326VeriPHYPort_Object = MibTableColumn
gs2326VeriPHYPort = _Gs2326VeriPHYPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 1),
    _Gs2326VeriPHYPort_Type()
)
gs2326VeriPHYPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2326VeriPHYPort.setStatus("current")
_Gs2326VeriPHYPairA_Type = DisplayString
_Gs2326VeriPHYPairA_Object = MibTableColumn
gs2326VeriPHYPairA = _Gs2326VeriPHYPairA_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 2),
    _Gs2326VeriPHYPairA_Type()
)
gs2326VeriPHYPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYPairA.setStatus("current")
_Gs2326VeriPHYLengthA_Type = DisplayString
_Gs2326VeriPHYLengthA_Object = MibTableColumn
gs2326VeriPHYLengthA = _Gs2326VeriPHYLengthA_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 3),
    _Gs2326VeriPHYLengthA_Type()
)
gs2326VeriPHYLengthA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYLengthA.setStatus("current")
_Gs2326VeriPHYPairB_Type = DisplayString
_Gs2326VeriPHYPairB_Object = MibTableColumn
gs2326VeriPHYPairB = _Gs2326VeriPHYPairB_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 4),
    _Gs2326VeriPHYPairB_Type()
)
gs2326VeriPHYPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYPairB.setStatus("current")
_Gs2326VeriPHYLengthB_Type = DisplayString
_Gs2326VeriPHYLengthB_Object = MibTableColumn
gs2326VeriPHYLengthB = _Gs2326VeriPHYLengthB_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 5),
    _Gs2326VeriPHYLengthB_Type()
)
gs2326VeriPHYLengthB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYLengthB.setStatus("current")
_Gs2326VeriPHYPairC_Type = DisplayString
_Gs2326VeriPHYPairC_Object = MibTableColumn
gs2326VeriPHYPairC = _Gs2326VeriPHYPairC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 6),
    _Gs2326VeriPHYPairC_Type()
)
gs2326VeriPHYPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYPairC.setStatus("current")
_Gs2326VeriPHYLengthC_Type = DisplayString
_Gs2326VeriPHYLengthC_Object = MibTableColumn
gs2326VeriPHYLengthC = _Gs2326VeriPHYLengthC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 7),
    _Gs2326VeriPHYLengthC_Type()
)
gs2326VeriPHYLengthC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYLengthC.setStatus("current")
_Gs2326VeriPHYPairD_Type = DisplayString
_Gs2326VeriPHYPairD_Object = MibTableColumn
gs2326VeriPHYPairD = _Gs2326VeriPHYPairD_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 8),
    _Gs2326VeriPHYPairD_Type()
)
gs2326VeriPHYPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYPairD.setStatus("current")
_Gs2326VeriPHYLengthD_Type = DisplayString
_Gs2326VeriPHYLengthD_Object = MibTableColumn
gs2326VeriPHYLengthD = _Gs2326VeriPHYLengthD_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 5, 9, 2, 1, 9),
    _Gs2326VeriPHYLengthD_Type()
)
gs2326VeriPHYLengthD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326VeriPHYLengthD.setStatus("current")


class _Gs2326ColdRestartDevice_Type(Integer32):
    """Custom type gs2326ColdRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2326ColdRestartDevice_Type.__name__ = "Integer32"
_Gs2326ColdRestartDevice_Object = MibScalar
gs2326ColdRestartDevice = _Gs2326ColdRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 4, 1500),
    _Gs2326ColdRestartDevice_Type()
)
gs2326ColdRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2326ColdRestartDevice.setStatus("current")
_Gs2326Trap_ObjectIdentity = ObjectIdentity
gs2326Trap = _Gs2326Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5)
)
_Gs2326TrapEvent_ObjectIdentity = ObjectIdentity
gs2326TrapEvent = _Gs2326TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1)
)
_Gs2326TrapVariable_ObjectIdentity = ObjectIdentity
gs2326TrapVariable = _Gs2326TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 2)
)
_Gs2326Information_Type = DisplayString
_Gs2326Information_Object = MibScalar
gs2326Information = _Gs2326Information_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 2, 1),
    _Gs2326Information_Type()
)
gs2326Information.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2326Information.setStatus("current")

# Managed Objects groups


# Notification objects

gs2326Emergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 1)
)
gs2326Emergency.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Emergency.setStatus(
        "current"
    )

gs2326Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 2)
)
gs2326Alert.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Alert.setStatus(
        "current"
    )

gs2326Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 3)
)
gs2326Critical.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Critical.setStatus(
        "current"
    )

gs2326Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 4)
)
gs2326Error.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Error.setStatus(
        "current"
    )

gs2326Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 5)
)
gs2326Warning.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Warning.setStatus(
        "current"
    )

gs2326Notice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 6)
)
gs2326Notice.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Notice.setStatus(
        "current"
    )

gs2326Informational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 7)
)
gs2326Informational.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Informational.setStatus(
        "current"
    )

gs2326Debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2326, 5, 1, 8)
)
gs2326Debug.setObjects(
    ("LANCOM-GS-2326-MIB", "gs2326Information")
)
if mibBuilder.loadTexts:
    gs2326Debug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-GS-2326-MIB",
    **{"lancom-systems": lancom_systems,
       "switchingSystems": switchingSystems,
       "gigabitEthernetSwitches": gigabitEthernetSwitches,
       "lancomGS2326": lancomGS2326,
       "gs2326System": gs2326System,
       "gs2326SystemInformation": gs2326SystemInformation,
       "gs2326ModelName": gs2326ModelName,
       "gs2326BIOSVersion": gs2326BIOSVersion,
       "gs2326FirmwareVersion": gs2326FirmwareVersion,
       "gs2326HardwareMechanicalVersion": gs2326HardwareMechanicalVersion,
       "gs2326SerialNumber": gs2326SerialNumber,
       "gs2326HostMACAddress": gs2326HostMACAddress,
       "gs2326ConsoleBaudrate": gs2326ConsoleBaudrate,
       "gs2326RAMSize": gs2326RAMSize,
       "gs2326FlashSize": gs2326FlashSize,
       "gs2326BridgeFDBSize": gs2326BridgeFDBSize,
       "gs2326TransmitQueue": gs2326TransmitQueue,
       "gs2326MaximumFrameSize": gs2326MaximumFrameSize,
       "gs2326CPULoad": gs2326CPULoad,
       "gs2326SystemDescription": gs2326SystemDescription,
       "gs2326Location": gs2326Location,
       "gs2326Contact": gs2326Contact,
       "gs2326DeviceName": gs2326DeviceName,
       "gs2326SystemDate": gs2326SystemDate,
       "gs2326SystemUptime": gs2326SystemUptime,
       "gs2326SystemIPv4Address": gs2326SystemIPv4Address,
       "gs2326SystemIPv4SubnetMask": gs2326SystemIPv4SubnetMask,
       "gs2326SystemIPv4Gateway": gs2326SystemIPv4Gateway,
       "gs2326IPv6LinkLocalAddress": gs2326IPv6LinkLocalAddress,
       "gs2326IPv6Address": gs2326IPv6Address,
       "gs2326IPv6Prefix": gs2326IPv6Prefix,
       "gs2326IPv6Gateway": gs2326IPv6Gateway,
       "gs2326LargestFreeMemBlock": gs2326LargestFreeMemBlock,
       "gs2326MemFree": gs2326MemFree,
       "gs2326SystemTime": gs2326SystemTime,
       "gs2326SystemTimeManual": gs2326SystemTimeManual,
       "gs2326SystemTimeManualClockSource": gs2326SystemTimeManualClockSource,
       "gs2326SystemTimeManualLocaltime": gs2326SystemTimeManualLocaltime,
       "gs2326SystemTimeManualTimeZoneOffset": gs2326SystemTimeManualTimeZoneOffset,
       "gs2326SystemTimeManualDaylightSavings": gs2326SystemTimeManualDaylightSavings,
       "gs2326SystemTimeManualTimeSetOffset": gs2326SystemTimeManualTimeSetOffset,
       "gs2326SystemTimeManualDaylightSavingsType": gs2326SystemTimeManualDaylightSavingsType,
       "gs2326SystemTimeManualDaylightSavingsBydatesFrom": gs2326SystemTimeManualDaylightSavingsBydatesFrom,
       "gs2326SystemTimeManualDaylightSavingsBydatesTo": gs2326SystemTimeManualDaylightSavingsBydatesTo,
       "gs2326SystemTimeManualDaylightSavingsRecurringDayFrom": gs2326SystemTimeManualDaylightSavingsRecurringDayFrom,
       "gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom": gs2326SystemTimeManualDaylightSavingsRecurringWeekFrom,
       "gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom": gs2326SystemTimeManualDaylightSavingsRecurringMonthFrom,
       "gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom": gs2326SystemTimeManualDaylightSavingsRecurringTimeFrom,
       "gs2326SystemTimeManualDaylightSavingsRecurringDayTo": gs2326SystemTimeManualDaylightSavingsRecurringDayTo,
       "gs2326SystemTimeManualDaylightSavingsRecurringWeekTo": gs2326SystemTimeManualDaylightSavingsRecurringWeekTo,
       "gs2326SystemTimeManualDaylightSavingsRecurringMonthTo": gs2326SystemTimeManualDaylightSavingsRecurringMonthTo,
       "gs2326SystemTimeManualDaylightSavingsRecurringTimeTo": gs2326SystemTimeManualDaylightSavingsRecurringTimeTo,
       "gs2326SystemTimeNTP": gs2326SystemTimeNTP,
       "gs2326SystemTimeNTPTable": gs2326SystemTimeNTPTable,
       "gs2326SystemTimeNTPEntry": gs2326SystemTimeNTPEntry,
       "gs2326SystemTimeNTPIndex": gs2326SystemTimeNTPIndex,
       "gs2326SystemTimeNTPServerIPType": gs2326SystemTimeNTPServerIPType,
       "gs2326SystemTimeNTPServer": gs2326SystemTimeNTPServer,
       "gs2326SystemTimeNTPCurrentMode": gs2326SystemTimeNTPCurrentMode,
       "gs2326SystemTimeNTPRequestInterval": gs2326SystemTimeNTPRequestInterval,
       "gs2326SystemTimeNTPTriesNumber": gs2326SystemTimeNTPTriesNumber,
       "gs2326SystemAccount": gs2326SystemAccount,
       "gs2326SystemAccountUsers": gs2326SystemAccountUsers,
       "gs2326SystemAccountUserCreate": gs2326SystemAccountUserCreate,
       "gs2326SystemAccountUsersTable": gs2326SystemAccountUsersTable,
       "gs2326SystemAccountUsersEntry": gs2326SystemAccountUsersEntry,
       "gs2326UserIndex": gs2326UserIndex,
       "gs2326UserName": gs2326UserName,
       "gs2326Password": gs2326Password,
       "gs2326UserPrivilegeLevel": gs2326UserPrivilegeLevel,
       "gs2326AccountUserRowStatus": gs2326AccountUserRowStatus,
       "gs2326SystemAccountUsersSuperUserPassword": gs2326SystemAccountUsersSuperUserPassword,
       "gs2326SystemAccountEnforcePasswordRules": gs2326SystemAccountEnforcePasswordRules,
       "gs2326SystemAccountPrivilegeLevel": gs2326SystemAccountPrivilegeLevel,
       "gs2326AccountPrivilegeLevel": gs2326AccountPrivilegeLevel,
       "gs2326AggregationPrivilegeLevel": gs2326AggregationPrivilegeLevel,
       "gs2326DiagnosticsPrivilegeLevel": gs2326DiagnosticsPrivilegeLevel,
       "gs2326EEEPrivilegeLevel": gs2326EEEPrivilegeLevel,
       "gs2326EasyportPrivilegeLevel": gs2326EasyportPrivilegeLevel,
       "gs2326GARPPrivilegeLevel": gs2326GARPPrivilegeLevel,
       "gs2326GVRPPrivilegeLevel": gs2326GVRPPrivilegeLevel,
       "gs2326IPPrivilegeLevel": gs2326IPPrivilegeLevel,
       "gs2326IPMCSnoopingPrivilegeLevel": gs2326IPMCSnoopingPrivilegeLevel,
       "gs2326LACPPrivilegeLevel": gs2326LACPPrivilegeLevel,
       "gs2326LLDPPrivilegeLevel": gs2326LLDPPrivilegeLevel,
       "gs2326LLDPMEDPrivilegeLevel": gs2326LLDPMEDPrivilegeLevel,
       "gs2326LoopProtectPrivilegeLevel": gs2326LoopProtectPrivilegeLevel,
       "gs2326MACTablePrivilegeLevel": gs2326MACTablePrivilegeLevel,
       "gs2326MVRPrivilegeLevel": gs2326MVRPrivilegeLevel,
       "gs2326MaintenancePrivilegeLevel": gs2326MaintenancePrivilegeLevel,
       "gs2326MirroringPrivilegeLevel": gs2326MirroringPrivilegeLevel,
       "gs2326PortsPrivilegeLevel": gs2326PortsPrivilegeLevel,
       "gs2326PrivateVLANsPrivilegeLevel": gs2326PrivateVLANsPrivilegeLevel,
       "gs2326QoSPrivilegeLevel": gs2326QoSPrivilegeLevel,
       "gs2326SFlowPrivilegeLevel": gs2326SFlowPrivilegeLevel,
       "gs2326SMTPPrivilegeLevel": gs2326SMTPPrivilegeLevel,
       "gs2326SNMPPrivilegeLevel": gs2326SNMPPrivilegeLevel,
       "gs2326SecurityPrivilegeLevel": gs2326SecurityPrivilegeLevel,
       "gs2326SingleIPPrivilegeLevel": gs2326SingleIPPrivilegeLevel,
       "gs2326SpanningTreePrivilegeLevel": gs2326SpanningTreePrivilegeLevel,
       "gs2326SystemPrivilegeLevel": gs2326SystemPrivilegeLevel,
       "gs2326TrapEventPrivilegeLevel": gs2326TrapEventPrivilegeLevel,
       "gs2326UPnPPrivilegeLevel": gs2326UPnPPrivilegeLevel,
       "gs2326VCLPrivilegeLevel": gs2326VCLPrivilegeLevel,
       "gs2326VLANsPrivilegeLevel": gs2326VLANsPrivilegeLevel,
       "gs2326VoiceVLANPrivilegeLevel": gs2326VoiceVLANPrivilegeLevel,
       "gs2326IP": gs2326IP,
       "gs2326IPv4": gs2326IPv4,
       "gs2326IPv4Configured": gs2326IPv4Configured,
       "gs2326Ipv4DHCPClient": gs2326Ipv4DHCPClient,
       "gs2326IPv4Address": gs2326IPv4Address,
       "gs2326IPv4Mask": gs2326IPv4Mask,
       "gs2326IPv4Gateway": gs2326IPv4Gateway,
       "gs2326IPv4VLANId": gs2326IPv4VLANId,
       "gs2326IPv4DNSServer": gs2326IPv4DNSServer,
       "gs2326IPv4DNSProxy": gs2326IPv4DNSProxy,
       "gs2326IPv4Current": gs2326IPv4Current,
       "gs2326Ipv4CurrentDHCPClient": gs2326Ipv4CurrentDHCPClient,
       "gs2326IPv4CurrentAddress": gs2326IPv4CurrentAddress,
       "gs2326IPv4CurrentMask": gs2326IPv4CurrentMask,
       "gs2326IPv4CurrentGateway": gs2326IPv4CurrentGateway,
       "gs2326IPv4CurrentVLANId": gs2326IPv4CurrentVLANId,
       "gs2326IPv4CurrentDNSServer": gs2326IPv4CurrentDNSServer,
       "gs2326IPv6": gs2326IPv6,
       "gs2326IPv6Configured": gs2326IPv6Configured,
       "gs2326Ipv6AutoConfiguration": gs2326Ipv6AutoConfiguration,
       "gs2326Ipv6Address": gs2326Ipv6Address,
       "gs2326Ipv6Prefix": gs2326Ipv6Prefix,
       "gs2326Ipv6Gateway": gs2326Ipv6Gateway,
       "gs2326IPv6Current": gs2326IPv6Current,
       "gs2326Ipv6CurrentAutoConfiguration": gs2326Ipv6CurrentAutoConfiguration,
       "gs2326Ipv6CurrentAddress": gs2326Ipv6CurrentAddress,
       "gs2326Ipv6CurrentLinkLocalAddress": gs2326Ipv6CurrentLinkLocalAddress,
       "gs2326Ipv6CurrentPrefix": gs2326Ipv6CurrentPrefix,
       "gs2326Ipv6CurrentGateway": gs2326Ipv6CurrentGateway,
       "gs2326Syslog": gs2326Syslog,
       "gs2326SyslogConf": gs2326SyslogConf,
       "gs2326ServerMode": gs2326ServerMode,
       "gs2326ServerAddress1": gs2326ServerAddress1,
       "gs2326ServerAddress2": gs2326ServerAddress2,
       "gs2326SyslogLevel": gs2326SyslogLevel,
       "gs2326SyslogDetailedInfo": gs2326SyslogDetailedInfo,
       "gs2326SyslogDetailedInfoClear": gs2326SyslogDetailedInfoClear,
       "gs2326SyslogDetailedInfoTable": gs2326SyslogDetailedInfoTable,
       "gs2326SyslogDetailedInfoEntry": gs2326SyslogDetailedInfoEntry,
       "gs2326SyslogDetailedInfoIndex": gs2326SyslogDetailedInfoIndex,
       "gs2326SyslogDetailedInfoLevel": gs2326SyslogDetailedInfoLevel,
       "gs2326SyslogDetailedInfoTime": gs2326SyslogDetailedInfoTime,
       "gs2326SyslogDetailedInfoMessage": gs2326SyslogDetailedInfoMessage,
       "gs2326Snmp": gs2326Snmp,
       "gs2326SnmpConf": gs2326SnmpConf,
       "gs2326GetCommunityMode": gs2326GetCommunityMode,
       "gs2326GetCommunity": gs2326GetCommunity,
       "gs2326SetCommunityMode": gs2326SetCommunityMode,
       "gs2326SetCommunity": gs2326SetCommunity,
       "gs2326GetCommunityConfTable": gs2326GetCommunityConfTable,
       "gs2326GetCommunityConfEntry": gs2326GetCommunityConfEntry,
       "gs2326CommunityConfIndex": gs2326CommunityConfIndex,
       "gs2326CommunityConfGetCommunity": gs2326CommunityConfGetCommunity,
       "gs2326TrapHostConfTable": gs2326TrapHostConfTable,
       "gs2326TrapHostConfEntry": gs2326TrapHostConfEntry,
       "gs2326TrapHostConfIndex": gs2326TrapHostConfIndex,
       "gs2326TrapHostConfVersion": gs2326TrapHostConfVersion,
       "gs2326TrapHostConfIPType": gs2326TrapHostConfIPType,
       "gs2326TrapHostConfIP": gs2326TrapHostConfIP,
       "gs2326TrapHostConfPort": gs2326TrapHostConfPort,
       "gs2326TrapHostConfCommunity": gs2326TrapHostConfCommunity,
       "gs2326TrapHostConfSeverityLevel": gs2326TrapHostConfSeverityLevel,
       "gs2326TrapHostConfSecurityLevel": gs2326TrapHostConfSecurityLevel,
       "gs2326TrapHostConfAuthPtc": gs2326TrapHostConfAuthPtc,
       "gs2326TrapHostConfAuthPassword": gs2326TrapHostConfAuthPassword,
       "gs2326TrapHostConfPrivPtc": gs2326TrapHostConfPrivPtc,
       "gs2326TrapHostConfPrivPassword": gs2326TrapHostConfPrivPassword,
       "gs2326TrapHostConfCurrentMode": gs2326TrapHostConfCurrentMode,
       "gs2326SnmpSystem": gs2326SnmpSystem,
       "gs2326SnmpState": gs2326SnmpState,
       "gs2326SnmpEngineID": gs2326SnmpEngineID,
       "gs2326SnmpCommunities": gs2326SnmpCommunities,
       "gs2326SnmpCommunitiesCreate": gs2326SnmpCommunitiesCreate,
       "gs2326SnmpCommunitiesTable": gs2326SnmpCommunitiesTable,
       "gs2326SnmpCommunitiesEntry": gs2326SnmpCommunitiesEntry,
       "gs2326SnmpCommunitiesIndex": gs2326SnmpCommunitiesIndex,
       "gs2326SnmpCommunitiesCommunity": gs2326SnmpCommunitiesCommunity,
       "gs2326SnmpCommunitiesUserName": gs2326SnmpCommunitiesUserName,
       "gs2326SnmpCommunitiesSourceIP": gs2326SnmpCommunitiesSourceIP,
       "gs2326SnmpCommunitiesSourceMask": gs2326SnmpCommunitiesSourceMask,
       "gs2326SnmpCommunitiesRowStatus": gs2326SnmpCommunitiesRowStatus,
       "gs2326SnmpUsers": gs2326SnmpUsers,
       "gs2326SnmpUsersCreate": gs2326SnmpUsersCreate,
       "gs2326SnmpUsersTable": gs2326SnmpUsersTable,
       "gs2326SnmpUsersEntry": gs2326SnmpUsersEntry,
       "gs2326SnmpUsersIndex": gs2326SnmpUsersIndex,
       "gs2326SnmpUsersUserName": gs2326SnmpUsersUserName,
       "gs2326SnmpUsersSecurityLevel": gs2326SnmpUsersSecurityLevel,
       "gs2326SnmpUsersAuthenticationProtocol": gs2326SnmpUsersAuthenticationProtocol,
       "gs2326SnmpUsersAuthenticationPassword": gs2326SnmpUsersAuthenticationPassword,
       "gs2326SnmpUsersPrivacyProtocol": gs2326SnmpUsersPrivacyProtocol,
       "gs2326SnmpUsersPrivacyPassword": gs2326SnmpUsersPrivacyPassword,
       "gs2326SnmpUsersRowStatus": gs2326SnmpUsersRowStatus,
       "gs2326SnmpGroups": gs2326SnmpGroups,
       "gs2326SnmpGroupsCreate": gs2326SnmpGroupsCreate,
       "gs2326SnmpGroupsTable": gs2326SnmpGroupsTable,
       "gs2326SnmpGroupsEntry": gs2326SnmpGroupsEntry,
       "gs2326SnmpGroupsIndex": gs2326SnmpGroupsIndex,
       "gs2326SnmpGroupsSecurityModel": gs2326SnmpGroupsSecurityModel,
       "gs2326SnmpGroupsSecurityName": gs2326SnmpGroupsSecurityName,
       "gs2326SnmpGroupsGroupName": gs2326SnmpGroupsGroupName,
       "gs2326SnmpGroupsRowStatus": gs2326SnmpGroupsRowStatus,
       "gs2326SnmpViews": gs2326SnmpViews,
       "gs2326SnmpViewsCreate": gs2326SnmpViewsCreate,
       "gs2326SnmpViewsTable": gs2326SnmpViewsTable,
       "gs2326SnmpViewsEntry": gs2326SnmpViewsEntry,
       "gs2326SnmpViewsIndex": gs2326SnmpViewsIndex,
       "gs2326SnmpViewsName": gs2326SnmpViewsName,
       "gs2326SnmpViewsType": gs2326SnmpViewsType,
       "gs2326SnmpViewsOIDSubtree": gs2326SnmpViewsOIDSubtree,
       "gs2326SnmpViewsRowStatus": gs2326SnmpViewsRowStatus,
       "gs2326SnmpAccess": gs2326SnmpAccess,
       "gs2326SnmpAccessCreate": gs2326SnmpAccessCreate,
       "gs2326SnmpAccessTable": gs2326SnmpAccessTable,
       "gs2326SnmpAccessEntry": gs2326SnmpAccessEntry,
       "gs2326SnmpAccessIndex": gs2326SnmpAccessIndex,
       "gs2326SnmpAccessGroupName": gs2326SnmpAccessGroupName,
       "gs2326SnmpAccessSecurityModel": gs2326SnmpAccessSecurityModel,
       "gs2326SnmpAccessSecurityLevel": gs2326SnmpAccessSecurityLevel,
       "gs2326SnmpAccessReadViewName": gs2326SnmpAccessReadViewName,
       "gs2326SnmpAccessWriteViewName": gs2326SnmpAccessWriteViewName,
       "gs2326SnmpAccessRowStatus": gs2326SnmpAccessRowStatus,
       "gs2326Configuration": gs2326Configuration,
       "gs2326Port": gs2326Port,
       "gs2326PortConfigurationTable": gs2326PortConfigurationTable,
       "gs2326PortConfigurationEntry": gs2326PortConfigurationEntry,
       "gs2326PortConfPort": gs2326PortConfPort,
       "gs2326PortConfPortMedia": gs2326PortConfPortMedia,
       "gs2326PortConfLink": gs2326PortConfLink,
       "gs2326PortConfCurrentSpeed": gs2326PortConfCurrentSpeed,
       "gs2326PortConfSpeed": gs2326PortConfSpeed,
       "gs2326PortConfCurrentFlowControlRx": gs2326PortConfCurrentFlowControlRx,
       "gs2326PortConfCurrentFlowControlTx": gs2326PortConfCurrentFlowControlTx,
       "gs2326PortConfFlowControl": gs2326PortConfFlowControl,
       "gs2326PortConfMaxFrameSize": gs2326PortConfMaxFrameSize,
       "gs2326PortConfExcessiveCollisionMode": gs2326PortConfExcessiveCollisionMode,
       "gs2326PortConfPowerControl": gs2326PortConfPowerControl,
       "gs2326PortConfDescription": gs2326PortConfDescription,
       "gs2326PortTrafficStatisticsTable": gs2326PortTrafficStatisticsTable,
       "gs2326PortTrafficStatisticsEntry": gs2326PortTrafficStatisticsEntry,
       "gs2326PortTrafficStatisticsPort": gs2326PortTrafficStatisticsPort,
       "gs2326PortTrafficStatisticsClear": gs2326PortTrafficStatisticsClear,
       "gs2326PortTrafficRxPackets": gs2326PortTrafficRxPackets,
       "gs2326PortTrafficRxOctets": gs2326PortTrafficRxOctets,
       "gs2326PortTrafficRxUnicast": gs2326PortTrafficRxUnicast,
       "gs2326PortTrafficRxMulticast": gs2326PortTrafficRxMulticast,
       "gs2326PortTrafficRxBroadcast": gs2326PortTrafficRxBroadcast,
       "gs2326PortTrafficRxPause": gs2326PortTrafficRxPause,
       "gs2326PortTrafficRx64Bytes": gs2326PortTrafficRx64Bytes,
       "gs2326PortTrafficRx65to127Bytes": gs2326PortTrafficRx65to127Bytes,
       "gs2326PortTrafficRx128to255Bytes": gs2326PortTrafficRx128to255Bytes,
       "gs2326PortTrafficRx256to511Bytes": gs2326PortTrafficRx256to511Bytes,
       "gs2326PortTrafficRx512to1023Bytes": gs2326PortTrafficRx512to1023Bytes,
       "gs2326PortTrafficRx1024to1526Bytes": gs2326PortTrafficRx1024to1526Bytes,
       "gs2326PortTrafficRxExceecd1527Bytes": gs2326PortTrafficRxExceecd1527Bytes,
       "gs2326PortTrafficRxQ0": gs2326PortTrafficRxQ0,
       "gs2326PortTrafficRxQ1": gs2326PortTrafficRxQ1,
       "gs2326PortTrafficRxQ2": gs2326PortTrafficRxQ2,
       "gs2326PortTrafficRxQ3": gs2326PortTrafficRxQ3,
       "gs2326PortTrafficRxQ4": gs2326PortTrafficRxQ4,
       "gs2326PortTrafficRxQ5": gs2326PortTrafficRxQ5,
       "gs2326PortTrafficRxQ6": gs2326PortTrafficRxQ6,
       "gs2326PortTrafficRxQ7": gs2326PortTrafficRxQ7,
       "gs2326PortTrafficRxDrops": gs2326PortTrafficRxDrops,
       "gs2326PortTrafficRxCRCorAlignment": gs2326PortTrafficRxCRCorAlignment,
       "gs2326PortTrafficRxUndersize": gs2326PortTrafficRxUndersize,
       "gs2326PortTrafficRxOversize": gs2326PortTrafficRxOversize,
       "gs2326PortTrafficRxFragments": gs2326PortTrafficRxFragments,
       "gs2326PortTrafficRxJabber": gs2326PortTrafficRxJabber,
       "gs2326PortTrafficRxFiltered": gs2326PortTrafficRxFiltered,
       "gs2326PortTrafficTxPackets": gs2326PortTrafficTxPackets,
       "gs2326PortTrafficTxOctets": gs2326PortTrafficTxOctets,
       "gs2326PortTrafficTxUnicast": gs2326PortTrafficTxUnicast,
       "gs2326PortTrafficTxMulticast": gs2326PortTrafficTxMulticast,
       "gs2326PortTrafficTxBroadcast": gs2326PortTrafficTxBroadcast,
       "gs2326PortTrafficTxPause": gs2326PortTrafficTxPause,
       "gs2326PortTrafficTx64Bytes": gs2326PortTrafficTx64Bytes,
       "gs2326PortTrafficTx65to127Bytes": gs2326PortTrafficTx65to127Bytes,
       "gs2326PortTrafficTx128to255Bytes": gs2326PortTrafficTx128to255Bytes,
       "gs2326PortTrafficTx256to511Bytes": gs2326PortTrafficTx256to511Bytes,
       "gs2326PortTrafficTx512to1023Bytes": gs2326PortTrafficTx512to1023Bytes,
       "gs2326PortTrafficTx1024to1526Bytes": gs2326PortTrafficTx1024to1526Bytes,
       "gs2326PortTrafficTxExceecd1527Bytes": gs2326PortTrafficTxExceecd1527Bytes,
       "gs2326PortTrafficTxQ0": gs2326PortTrafficTxQ0,
       "gs2326PortTrafficTxQ1": gs2326PortTrafficTxQ1,
       "gs2326PortTrafficTxQ2": gs2326PortTrafficTxQ2,
       "gs2326PortTrafficTxQ3": gs2326PortTrafficTxQ3,
       "gs2326PortTrafficTxQ4": gs2326PortTrafficTxQ4,
       "gs2326PortTrafficTxQ5": gs2326PortTrafficTxQ5,
       "gs2326PortTrafficTxQ6": gs2326PortTrafficTxQ6,
       "gs2326PortTrafficTxQ7": gs2326PortTrafficTxQ7,
       "gs2326PortTrafficTxDrops": gs2326PortTrafficTxDrops,
       "gs2326PortTrafficTxLateOrExcColl": gs2326PortTrafficTxLateOrExcColl,
       "gs2326PortQoSStatistics": gs2326PortQoSStatistics,
       "gs2326PortQoSStatisticsClear": gs2326PortQoSStatisticsClear,
       "gs2326PortQoSStatisticsTable": gs2326PortQoSStatisticsTable,
       "gs2326PortQoSStatisticsEntry": gs2326PortQoSStatisticsEntry,
       "gs2326PortQoSStatisticsPort": gs2326PortQoSStatisticsPort,
       "gs2326PortQoSQ0Rx": gs2326PortQoSQ0Rx,
       "gs2326PortQoSQ0Tx": gs2326PortQoSQ0Tx,
       "gs2326PortQoSQ1Rx": gs2326PortQoSQ1Rx,
       "gs2326PortQoSQ1Tx": gs2326PortQoSQ1Tx,
       "gs2326PortQoSQ2Rx": gs2326PortQoSQ2Rx,
       "gs2326PortQoSQ2Tx": gs2326PortQoSQ2Tx,
       "gs2326PortQoSQ3Rx": gs2326PortQoSQ3Rx,
       "gs2326PortQoSQ3Tx": gs2326PortQoSQ3Tx,
       "gs2326PortQoSQ4Rx": gs2326PortQoSQ4Rx,
       "gs2326PortQoSQ4Tx": gs2326PortQoSQ4Tx,
       "gs2326PortQoSQ5Rx": gs2326PortQoSQ5Rx,
       "gs2326PortQoSQ5Tx": gs2326PortQoSQ5Tx,
       "gs2326PortQoSQ6Rx": gs2326PortQoSQ6Rx,
       "gs2326PortQoSQ6Tx": gs2326PortQoSQ6Tx,
       "gs2326PortQoSQ7Rx": gs2326PortQoSQ7Rx,
       "gs2326PortQoSQ7Tx": gs2326PortQoSQ7Tx,
       "gs2326SFPInfoTable": gs2326SFPInfoTable,
       "gs2326SFPInfoEntry": gs2326SFPInfoEntry,
       "gs2326SFPInfoIndex": gs2326SFPInfoIndex,
       "gs2326SFPInfoPort": gs2326SFPInfoPort,
       "gs2326SFPConnectorType": gs2326SFPConnectorType,
       "gs2326SFPFiberType": gs2326SFPFiberType,
       "gs2326SFPTxCentralWavelength": gs2326SFPTxCentralWavelength,
       "gs2326SFPBaudRate": gs2326SFPBaudRate,
       "gs2326SFPVendorOUI": gs2326SFPVendorOUI,
       "gs2326SFPVendorName": gs2326SFPVendorName,
       "gs2326SFPVendorPN": gs2326SFPVendorPN,
       "gs2326SFPVendorRev": gs2326SFPVendorRev,
       "gs2326SFPVendorSN": gs2326SFPVendorSN,
       "gs2326SFPDateCode": gs2326SFPDateCode,
       "gs2326SFPTemperature": gs2326SFPTemperature,
       "gs2326SFPVcc": gs2326SFPVcc,
       "gs2326SFPMon1Bias": gs2326SFPMon1Bias,
       "gs2326SFPMon2TxPWR": gs2326SFPMon2TxPWR,
       "gs2326SFPMon3RxPWR": gs2326SFPMon3RxPWR,
       "gs2326PortEEETable": gs2326PortEEETable,
       "gs2326PortEEEEntry": gs2326PortEEEEntry,
       "gs2326PortEEEPort": gs2326PortEEEPort,
       "gs2326PortEEEMode": gs2326PortEEEMode,
       "gs2326PortEEEUrgentQueue1": gs2326PortEEEUrgentQueue1,
       "gs2326PortEEEUrgentQueue2": gs2326PortEEEUrgentQueue2,
       "gs2326PortEEEUrgentQueue3": gs2326PortEEEUrgentQueue3,
       "gs2326PortEEEUrgentQueue4": gs2326PortEEEUrgentQueue4,
       "gs2326PortEEEUrgentQueue5": gs2326PortEEEUrgentQueue5,
       "gs2326PortEEEUrgentQueue6": gs2326PortEEEUrgentQueue6,
       "gs2326PortEEEUrgentQueue7": gs2326PortEEEUrgentQueue7,
       "gs2326PortEEEUrgentQueue8": gs2326PortEEEUrgentQueue8,
       "gs2326VoiceVLAN": gs2326VoiceVLAN,
       "gs2326VoiceVLANConf": gs2326VoiceVLANConf,
       "gs2326VoiceVLANMode": gs2326VoiceVLANMode,
       "gs2326VoiceVLANVLANId": gs2326VoiceVLANVLANId,
       "gs2326VoiceVLANAgingTime": gs2326VoiceVLANAgingTime,
       "gs2326VoiceVLANTrafficClass": gs2326VoiceVLANTrafficClass,
       "gs2326VoiceVLANPortTable": gs2326VoiceVLANPortTable,
       "gs2326VoiceVLANPortEntry": gs2326VoiceVLANPortEntry,
       "gs2326VoiceVLANPort": gs2326VoiceVLANPort,
       "gs2326VoiceVLANPortMode": gs2326VoiceVLANPortMode,
       "gs2326VoiceVLANPortSecurity": gs2326VoiceVLANPortSecurity,
       "gs2326VoiceVLANPortDiscoveryProtocol": gs2326VoiceVLANPortDiscoveryProtocol,
       "gs2326VoiceVLANSkipNAS": gs2326VoiceVLANSkipNAS,
       "gs2326VoiceVLANOUI": gs2326VoiceVLANOUI,
       "gs2326VoiceVLANOUICreate": gs2326VoiceVLANOUICreate,
       "gs2326VoiceVLANOUITable": gs2326VoiceVLANOUITable,
       "gs2326VoiceVLANOUIEntry": gs2326VoiceVLANOUIEntry,
       "gs2326VoiceVLANOUIIndex": gs2326VoiceVLANOUIIndex,
       "gs2326VoiceVLANTelephonyOUI": gs2326VoiceVLANTelephonyOUI,
       "gs2326VoiceVLANDescription": gs2326VoiceVLANDescription,
       "gs2326VoiceVLANOUIRowStatus": gs2326VoiceVLANOUIRowStatus,
       "gs2326GARP": gs2326GARP,
       "gs2326GARPConfTable": gs2326GARPConfTable,
       "gs2326GARPConfEntry": gs2326GARPConfEntry,
       "gs2326GARPConfPort": gs2326GARPConfPort,
       "gs2326GARPJoinTimer": gs2326GARPJoinTimer,
       "gs2326GARPLeaveTimer": gs2326GARPLeaveTimer,
       "gs2326GARPLeaveAllTimer": gs2326GARPLeaveAllTimer,
       "gs2326GARPApplicantion": gs2326GARPApplicantion,
       "gs2326GARPAttributeType": gs2326GARPAttributeType,
       "gs2326GARPApplicant": gs2326GARPApplicant,
       "gs2326GARPStatisticsTable": gs2326GARPStatisticsTable,
       "gs2326GARPStatisticsEntry": gs2326GARPStatisticsEntry,
       "gs2326GARPStatisticsPort": gs2326GARPStatisticsPort,
       "gs2326GARPStatisticsPeerMAC": gs2326GARPStatisticsPeerMAC,
       "gs2326GARPStatisticsFailedCount": gs2326GARPStatisticsFailedCount,
       "gs2326GVRP": gs2326GVRP,
       "gs2326GVRPConf": gs2326GVRPConf,
       "gs2326GVRPMode": gs2326GVRPMode,
       "gs2326GVRPConfTable": gs2326GVRPConfTable,
       "gs2326GVRPConfEntry": gs2326GVRPConfEntry,
       "gs2326GVRPConfPort": gs2326GVRPConfPort,
       "gs2326GVRPConfPortMode": gs2326GVRPConfPortMode,
       "gs2326GVRPConfPortRRole": gs2326GVRPConfPortRRole,
       "gs2326GVRPStatisticsTable": gs2326GVRPStatisticsTable,
       "gs2326GVRPStatisticsEntry": gs2326GVRPStatisticsEntry,
       "gs2326GVRPStatisticsPort": gs2326GVRPStatisticsPort,
       "gs2326GVRPStatisticsJoinTxCnt": gs2326GVRPStatisticsJoinTxCnt,
       "gs2326GVRPStatisticsLeaveTxCnt": gs2326GVRPStatisticsLeaveTxCnt,
       "gs2326Mirroring": gs2326Mirroring,
       "gs2326PortToMirrorOn": gs2326PortToMirrorOn,
       "gs2326MirrorTable": gs2326MirrorTable,
       "gs2326MirrorEntry": gs2326MirrorEntry,
       "gs2326MirrorPort": gs2326MirrorPort,
       "gs2326MirrorMode": gs2326MirrorMode,
       "gs2326TrapEventSeverity": gs2326TrapEventSeverity,
       "gs2326TrapEventSeverityACL": gs2326TrapEventSeverityACL,
       "gs2326TrapEventSeverityACLLog": gs2326TrapEventSeverityACLLog,
       "gs2326TrapEventSeverityAccessMgmt": gs2326TrapEventSeverityAccessMgmt,
       "gs2326TrapEventSeverityAuthFailed": gs2326TrapEventSeverityAuthFailed,
       "gs2326TrapEventSeverityColdStart": gs2326TrapEventSeverityColdStart,
       "gs2326TrapEventSeverityConfigInfo": gs2326TrapEventSeverityConfigInfo,
       "gs2326TrapEventSeverityFirmwareUpgrade": gs2326TrapEventSeverityFirmwareUpgrade,
       "gs2326TrapEventSeverityImportExport": gs2326TrapEventSeverityImportExport,
       "gs2326TrapEventSeverityLACP": gs2326TrapEventSeverityLACP,
       "gs2326TrapEventSeverityLinkStatus": gs2326TrapEventSeverityLinkStatus,
       "gs2326TrapEventSeverityLogin": gs2326TrapEventSeverityLogin,
       "gs2326TrapEventSeverityLogout": gs2326TrapEventSeverityLogout,
       "gs2326TrapEventSeverityLoopProtect": gs2326TrapEventSeverityLoopProtect,
       "gs2326TrapEventSeverityMgmtIPChange": gs2326TrapEventSeverityMgmtIPChange,
       "gs2326TrapEventSeverityModuleChange": gs2326TrapEventSeverityModuleChange,
       "gs2326TrapEventSeverityNAS": gs2326TrapEventSeverityNAS,
       "gs2326TrapEventSeverityPasswordChange": gs2326TrapEventSeverityPasswordChange,
       "gs2326TrapEventSeverityPortSecurity": gs2326TrapEventSeverityPortSecurity,
       "gs2326TrapEventSeverityVLAN": gs2326TrapEventSeverityVLAN,
       "gs2326TrapEventSeverityWarmStart": gs2326TrapEventSeverityWarmStart,
       "gs2326TrapEventSeverityARPConflict": gs2326TrapEventSeverityARPConflict,
       "gs2326TrapEventSeveritySpoofingLimit": gs2326TrapEventSeveritySpoofingLimit,
       "gs2326TrapEventSeverityStaticARPConflict": gs2326TrapEventSeverityStaticARPConflict,
       "gs2326SMTP": gs2326SMTP,
       "gs2326SMTPMailServer": gs2326SMTPMailServer,
       "gs2326SMTPUserName": gs2326SMTPUserName,
       "gs2326SMTPPassword": gs2326SMTPPassword,
       "gs2326SMTPServeriryLevel": gs2326SMTPServeriryLevel,
       "gs2326SMTPSender": gs2326SMTPSender,
       "gs2326SMTPReturnPath": gs2326SMTPReturnPath,
       "gs2326SMTPEmailAddress1": gs2326SMTPEmailAddress1,
       "gs2326SMTPEmailAddress2": gs2326SMTPEmailAddress2,
       "gs2326SMTPEmailAddress3": gs2326SMTPEmailAddress3,
       "gs2326SMTPEmailAddress4": gs2326SMTPEmailAddress4,
       "gs2326SMTPEmailAddress5": gs2326SMTPEmailAddress5,
       "gs2326SMTPEmailAddress6": gs2326SMTPEmailAddress6,
       "gs2326ACL": gs2326ACL,
       "gs2326ACLPortsConfTable": gs2326ACLPortsConfTable,
       "gs2326ACLPortsConfEntry": gs2326ACLPortsConfEntry,
       "gs2326ACLPortsConfPort": gs2326ACLPortsConfPort,
       "gs2326ACLPortsConfPolicyID": gs2326ACLPortsConfPolicyID,
       "gs2326ACLPortsConfAction": gs2326ACLPortsConfAction,
       "gs2326ACLPortsConfRateLimiterID": gs2326ACLPortsConfRateLimiterID,
       "gs2326ACLPortsConfPortRedirect": gs2326ACLPortsConfPortRedirect,
       "gs2326ACLPortsConfMirror": gs2326ACLPortsConfMirror,
       "gs2326ACLPortsConfLogging": gs2326ACLPortsConfLogging,
       "gs2326ACLPortsConfShutdown": gs2326ACLPortsConfShutdown,
       "gs2326ACLPortsConfState": gs2326ACLPortsConfState,
       "gs2326ACLPortsConfCounter": gs2326ACLPortsConfCounter,
       "gs2326ACLRateLimiterTable": gs2326ACLRateLimiterTable,
       "gs2326ACLRateLimiterEntry": gs2326ACLRateLimiterEntry,
       "gs2326ACLRateLimiterID": gs2326ACLRateLimiterID,
       "gs2326ACLRateLimiterUnit": gs2326ACLRateLimiterUnit,
       "gs2326ACLRateLimiterRate": gs2326ACLRateLimiterRate,
       "gs2326ACLACE": gs2326ACLACE,
       "gs2326ACLACECreate": gs2326ACLACECreate,
       "gs2326ACLACETable": gs2326ACLACETable,
       "gs2326ACLACEEntry": gs2326ACLACEEntry,
       "gs2326ACLACEIndex": gs2326ACLACEIndex,
       "gs2326ACLACEID": gs2326ACLACEID,
       "gs2326ACLACENextID": gs2326ACLACENextID,
       "gs2326ACLACEIngressPort": gs2326ACLACEIngressPort,
       "gs2326ACLACEPortPolicyNumber": gs2326ACLACEPortPolicyNumber,
       "gs2326ACLACEPortPolicyBitmask": gs2326ACLACEPortPolicyBitmask,
       "gs2326ACLACEFrameType": gs2326ACLACEFrameType,
       "gs2326ACLACEAction": gs2326ACLACEAction,
       "gs2326ACLACEDenyPortRedirect": gs2326ACLACEDenyPortRedirect,
       "gs2326ACLACELogging": gs2326ACLACELogging,
       "gs2326ACLACEMirror": gs2326ACLACEMirror,
       "gs2326ACLACERateLimiter": gs2326ACLACERateLimiter,
       "gs2326ACLACEShutdown": gs2326ACLACEShutdown,
       "gs2326ACLACEVLAN8021QTagged": gs2326ACLACEVLAN8021QTagged,
       "gs2326ACLACEVLANTagPriority": gs2326ACLACEVLANTagPriority,
       "gs2326ACLACEVLANVID": gs2326ACLACEVLANVID,
       "gs2326ACLACEEtherType": gs2326ACLACEEtherType,
       "gs2326ACLACESMAC": gs2326ACLACESMAC,
       "gs2326ACLACEDMACType": gs2326ACLACEDMACType,
       "gs2326ACLACEDMAC": gs2326ACLACEDMAC,
       "gs2326ACLACEArpOpcode": gs2326ACLACEArpOpcode,
       "gs2326ACLACEArpFlagsRequestReply": gs2326ACLACEArpFlagsRequestReply,
       "gs2326ACLACEArpFlagsArpSmac": gs2326ACLACEArpFlagsArpSmac,
       "gs2326ACLACEArpFlagsRarpDmac": gs2326ACLACEArpFlagsRarpDmac,
       "gs2326ACLACEArpFlagsLength": gs2326ACLACEArpFlagsLength,
       "gs2326ACLACEArpFlagsIp": gs2326ACLACEArpFlagsIp,
       "gs2326ACLACEArpFlagsEthernet": gs2326ACLACEArpFlagsEthernet,
       "gs2326ACLACESIPType": gs2326ACLACESIPType,
       "gs2326ACLACESIPIPAddress": gs2326ACLACESIPIPAddress,
       "gs2326ACLACESIPNetworkPrefix": gs2326ACLACESIPNetworkPrefix,
       "gs2326ACLACEDIPType": gs2326ACLACEDIPType,
       "gs2326ACLACEDIPIPAddress": gs2326ACLACEDIPIPAddress,
       "gs2326ACLACEDIPNetworkPrefix": gs2326ACLACEDIPNetworkPrefix,
       "gs2326ACLACEIPProtocol": gs2326ACLACEIPProtocol,
       "gs2326ACLACEIPFlagsTTL": gs2326ACLACEIPFlagsTTL,
       "gs2326ACLACEIPFlagsOptions": gs2326ACLACEIPFlagsOptions,
       "gs2326ACLACEIPFlagsFragment": gs2326ACLACEIPFlagsFragment,
       "gs2326ACLACEICMPType": gs2326ACLACEICMPType,
       "gs2326ACLACEICMPCode": gs2326ACLACEICMPCode,
       "gs2326ACLACESourcePortMin": gs2326ACLACESourcePortMin,
       "gs2326ACLACESourcePortMax": gs2326ACLACESourcePortMax,
       "gs2326ACLACEDestPortMin": gs2326ACLACEDestPortMin,
       "gs2326ACLACEDestPortMax": gs2326ACLACEDestPortMax,
       "gs2326ACLACETCPFlagsFin": gs2326ACLACETCPFlagsFin,
       "gs2326ACLACETCPFlagsSyn": gs2326ACLACETCPFlagsSyn,
       "gs2326ACLACETCPFlagsRst": gs2326ACLACETCPFlagsRst,
       "gs2326ACLACETCPFlagsPsh": gs2326ACLACETCPFlagsPsh,
       "gs2326ACLACETCPFlagsAck": gs2326ACLACETCPFlagsAck,
       "gs2326ACLACETCPFlagsUrg": gs2326ACLACETCPFlagsUrg,
       "gs2326ACLACERowStatus": gs2326ACLACERowStatus,
       "gs2326ACLACEClear": gs2326ACLACEClear,
       "gs2326ACLACEMoveACEID": gs2326ACLACEMoveACEID,
       "gs2326ACLACEMoveNextACEID": gs2326ACLACEMoveNextACEID,
       "gs2326ACLACEStatusTable": gs2326ACLACEStatusTable,
       "gs2326ACLACEStatusEntry": gs2326ACLACEStatusEntry,
       "gs2326ACLACEStatusIndex": gs2326ACLACEStatusIndex,
       "gs2326ACLACEStatusUser": gs2326ACLACEStatusUser,
       "gs2326ACLACEStatusID": gs2326ACLACEStatusID,
       "gs2326ACLACEStatusIngressPort": gs2326ACLACEStatusIngressPort,
       "gs2326ACLACEStatusFrameType": gs2326ACLACEStatusFrameType,
       "gs2326ACLACEStatusAction": gs2326ACLACEStatusAction,
       "gs2326ACLACEStatusRateLimiter": gs2326ACLACEStatusRateLimiter,
       "gs2326ACLACEStatusPortCopy": gs2326ACLACEStatusPortCopy,
       "gs2326ACLACEStatusMirror": gs2326ACLACEStatusMirror,
       "gs2326ACLACEStatusCPU": gs2326ACLACEStatusCPU,
       "gs2326ACLACEStatusCounter": gs2326ACLACEStatusCounter,
       "gs2326ACLACEStatusConflict": gs2326ACLACEStatusConflict,
       "gs2326LoopProtection": gs2326LoopProtection,
       "gs2326LoopProtectionConfig": gs2326LoopProtectionConfig,
       "gs2326LoopProtectionGlobalEnable": gs2326LoopProtectionGlobalEnable,
       "gs2326LoopProtectionTranmisstionTime": gs2326LoopProtectionTranmisstionTime,
       "gs2326LoopProtectionShutdownTime": gs2326LoopProtectionShutdownTime,
       "gs2326LoopProtectionConfigurationTable": gs2326LoopProtectionConfigurationTable,
       "gs2326LoopProtectionConfigurationEntry": gs2326LoopProtectionConfigurationEntry,
       "gs2326LoopProtectionConfPort": gs2326LoopProtectionConfPort,
       "gs2326LoopProtectionConfEnable": gs2326LoopProtectionConfEnable,
       "gs2326LoopProtectionConfAction": gs2326LoopProtectionConfAction,
       "gs2326LoopProtectionConfTxmode": gs2326LoopProtectionConfTxmode,
       "gs2326LoopProtectionStatusTable": gs2326LoopProtectionStatusTable,
       "gs2326LoopProtectionStatusEntry": gs2326LoopProtectionStatusEntry,
       "gs2326LoopProtectionStatusPort": gs2326LoopProtectionStatusPort,
       "gs2326LoopProtectionStatusAction": gs2326LoopProtectionStatusAction,
       "gs2326LoopProtectionStatusTransmit": gs2326LoopProtectionStatusTransmit,
       "gs2326LoopProtectionStatusLoops": gs2326LoopProtectionStatusLoops,
       "gs2326LoopProtectionStatusStatus": gs2326LoopProtectionStatusStatus,
       "gs2326LoopProtectionStatusLoop": gs2326LoopProtectionStatusLoop,
       "gs2326LoopProtectionStatusTimeLastLoop": gs2326LoopProtectionStatusTimeLastLoop,
       "gs2326Qos": gs2326Qos,
       "gs2326QosPortClassification": gs2326QosPortClassification,
       "gs2326QosPortClassificationTable": gs2326QosPortClassificationTable,
       "gs2326QosPortClassificationEntry": gs2326QosPortClassificationEntry,
       "gs2326QosPortClassificationPort": gs2326QosPortClassificationPort,
       "gs2326QosPortClassificationQoSclass": gs2326QosPortClassificationQoSclass,
       "gs2326QosPortClassificationDPlevel": gs2326QosPortClassificationDPlevel,
       "gs2326QosPortClassificationPCP": gs2326QosPortClassificationPCP,
       "gs2326QosPortClassificationDEI": gs2326QosPortClassificationDEI,
       "gs2326QosPortClassificationTagClass": gs2326QosPortClassificationTagClass,
       "gs2326QosPortClassificationDSCPBased": gs2326QosPortClassificationDSCPBased,
       "gs2326QosPortClassificationAddressMode": gs2326QosPortClassificationAddressMode,
       "gs2326QoSIngressPortTagClassificationTable": gs2326QoSIngressPortTagClassificationTable,
       "gs2326QoSIngressPortTagClassificationEntry": gs2326QoSIngressPortTagClassificationEntry,
       "gs2326QoSIngressPortTagClassificationPort": gs2326QoSIngressPortTagClassificationPort,
       "gs2326QoSIngressPortTagPCP": gs2326QoSIngressPortTagPCP,
       "gs2326QoSIngressPortTagDEI": gs2326QoSIngressPortTagDEI,
       "gs2326QoSIngressPortTagQosClass": gs2326QoSIngressPortTagQosClass,
       "gs2326QoSIngressPortTagDPLevel": gs2326QoSIngressPortTagDPLevel,
       "gs2326QosPortPolicingTable": gs2326QosPortPolicingTable,
       "gs2326QosPortPolicingEntry": gs2326QosPortPolicingEntry,
       "gs2326QosPortPolicingPort": gs2326QosPortPolicingPort,
       "gs2326QosPortPolicingMode": gs2326QosPortPolicingMode,
       "gs2326QosPortPolicingRate": gs2326QosPortPolicingRate,
       "gs2326QosPortPolicingUnit": gs2326QosPortPolicingUnit,
       "gs2326QosPortPolicingFlowControl": gs2326QosPortPolicingFlowControl,
       "gs2326QosPortScheduler": gs2326QosPortScheduler,
       "gs2326QosPortSchedulerModeTable": gs2326QosPortSchedulerModeTable,
       "gs2326QosPortSchedulerModeEntry": gs2326QosPortSchedulerModeEntry,
       "gs2326QosSchedulerModePort": gs2326QosSchedulerModePort,
       "gs2326QosSchedulerMode": gs2326QosSchedulerMode,
       "gs2326QosSchedulerShaper": gs2326QosSchedulerShaper,
       "gs2326QosSchedulerShaperRate": gs2326QosSchedulerShaperRate,
       "gs2326QosPortSchedulerTable": gs2326QosPortSchedulerTable,
       "gs2326QosPortSchedulerEntry": gs2326QosPortSchedulerEntry,
       "gs2326QosSchedulerPort": gs2326QosSchedulerPort,
       "gs2326QosSchedulerPortQueue": gs2326QosSchedulerPortQueue,
       "gs2326QosSchedulerPortQueueShaper": gs2326QosSchedulerPortQueueShaper,
       "gs2326QosSchedulerPortQueueShaperRate": gs2326QosSchedulerPortQueueShaperRate,
       "gs2326QosSchedulerPortQueueShaperExcess": gs2326QosSchedulerPortQueueShaperExcess,
       "gs2326QosSchedulerPortQueueSchedulerWeight": gs2326QosSchedulerPortQueueSchedulerWeight,
       "gs2326QosSchedulerPortQueueSchedulerPercent": gs2326QosSchedulerPortQueueSchedulerPercent,
       "gs2326QosPortEgressTagRemarking": gs2326QosPortEgressTagRemarking,
       "gs2326QosPortEgressTagRemarkingTable": gs2326QosPortEgressTagRemarkingTable,
       "gs2326QosPortEgressTagRemarkingEntry": gs2326QosPortEgressTagRemarkingEntry,
       "gs2326QosEgressTagRemarkingPort": gs2326QosEgressTagRemarkingPort,
       "gs2326QosEgressTagRemarkingMode": gs2326QosEgressTagRemarkingMode,
       "gs2326QosPortEgressTagRemarkingDefTable": gs2326QosPortEgressTagRemarkingDefTable,
       "gs2326QosPortEgressTagRemarkingDefEntry": gs2326QosPortEgressTagRemarkingDefEntry,
       "gs2326QosEgressTagRemarkingDefPort": gs2326QosEgressTagRemarkingDefPort,
       "gs2326QosEgressTagRemarkingDefPCP": gs2326QosEgressTagRemarkingDefPCP,
       "gs2326QosEgressTagRemarkingDefDEI": gs2326QosEgressTagRemarkingDefDEI,
       "gs2326QosPortEgressTagRemarkingMapTable": gs2326QosPortEgressTagRemarkingMapTable,
       "gs2326QosPortEgressTagRemarkingMapEntry": gs2326QosPortEgressTagRemarkingMapEntry,
       "gs2326QosPortEgressTagRemarkingMapPort": gs2326QosPortEgressTagRemarkingMapPort,
       "gs2326QosTagRemarkingQoSClass": gs2326QosTagRemarkingQoSClass,
       "gs2326QosTagRemarkingDPLevel": gs2326QosTagRemarkingDPLevel,
       "gs2326QosTagRemarkingPCP": gs2326QosTagRemarkingPCP,
       "gs2326QosTagRemarkingDEI": gs2326QosTagRemarkingDEI,
       "gs2326QosPortDSCPTable": gs2326QosPortDSCPTable,
       "gs2326QosPortDSCPEntry": gs2326QosPortDSCPEntry,
       "gs2326QosPortDSCPPort": gs2326QosPortDSCPPort,
       "gs2326QosPortDSCPIngressTranslate": gs2326QosPortDSCPIngressTranslate,
       "gs2326QosPortDSCPIngressClassify": gs2326QosPortDSCPIngressClassify,
       "gs2326QosPortDSCPEgressRewrite": gs2326QosPortDSCPEgressRewrite,
       "gs2326QosDSCPTable": gs2326QosDSCPTable,
       "gs2326QosDSCPEntry": gs2326QosDSCPEntry,
       "gs2326QosDSCPList": gs2326QosDSCPList,
       "gs2326QosDSCP": gs2326QosDSCP,
       "gs2326QosDSCPTrust": gs2326QosDSCPTrust,
       "gs2326QosDSCPQosClass": gs2326QosDSCPQosClass,
       "gs2326QosDSCPDPL": gs2326QosDSCPDPL,
       "gs2326QosDSCPTranslationTable": gs2326QosDSCPTranslationTable,
       "gs2326QosDSCPTranslationEntry": gs2326QosDSCPTranslationEntry,
       "gs2326QosDSCPTranslationList": gs2326QosDSCPTranslationList,
       "gs2326QosDSCPTranslationDSCPBasedId": gs2326QosDSCPTranslationDSCPBasedId,
       "gs2326QosDSCPTranslationIngressTranslate": gs2326QosDSCPTranslationIngressTranslate,
       "gs2326QosDSCPTranslationIngressClassify": gs2326QosDSCPTranslationIngressClassify,
       "gs2326QosDSCPTranslationEgressRemapDP0": gs2326QosDSCPTranslationEgressRemapDP0,
       "gs2326QosDSCPTranslationEgressRemapDP1": gs2326QosDSCPTranslationEgressRemapDP1,
       "gs2326QosDSCPClassificationTable": gs2326QosDSCPClassificationTable,
       "gs2326QosDSCPClassificationEntry": gs2326QosDSCPClassificationEntry,
       "gs2326QosDSCPClassificationQoSClass": gs2326QosDSCPClassificationQoSClass,
       "gs2326QosDSCPClassificationDPL": gs2326QosDSCPClassificationDPL,
       "gs2326QosDSCPClassificationDSCP": gs2326QosDSCPClassificationDSCP,
       "gs2326QosControlList": gs2326QosControlList,
       "gs2326QosQceCreate": gs2326QosQceCreate,
       "gs2326QosQceTable": gs2326QosQceTable,
       "gs2326QosQceEntry": gs2326QosQceEntry,
       "gs2326QosQceIndex": gs2326QosQceIndex,
       "gs2326QosQceID": gs2326QosQceID,
       "gs2326QosQceNextID": gs2326QosQceNextID,
       "gs2326QosQcePortMembers": gs2326QosQcePortMembers,
       "gs2326QosQceTag": gs2326QosQceTag,
       "gs2326QosQceVID": gs2326QosQceVID,
       "gs2326QosPCP": gs2326QosPCP,
       "gs2326QosDEI": gs2326QosDEI,
       "gs2326QosSMAC": gs2326QosSMAC,
       "gs2326QosDMACType": gs2326QosDMACType,
       "gs2326QosFrameType": gs2326QosFrameType,
       "gs2326QosMacEtherType": gs2326QosMacEtherType,
       "gs2326QosLLCSSAPAddr": gs2326QosLLCSSAPAddr,
       "gs2326QosLLCDSAPAddr": gs2326QosLLCDSAPAddr,
       "gs2326QosLLCControl": gs2326QosLLCControl,
       "gs2326QosSNAPPID": gs2326QosSNAPPID,
       "gs2326QosIpv4Protocol": gs2326QosIpv4Protocol,
       "gs2326QosIpv4ProtocolValue": gs2326QosIpv4ProtocolValue,
       "gs2326QosIpv4ProtocolUDPSport": gs2326QosIpv4ProtocolUDPSport,
       "gs2326QosIpv4ProtocolUDPDport": gs2326QosIpv4ProtocolUDPDport,
       "gs2326QosIpv4ProtocolTCPSport": gs2326QosIpv4ProtocolTCPSport,
       "gs2326QosIpv4ProtocolTCPDport": gs2326QosIpv4ProtocolTCPDport,
       "gs2326QosIpv4Ip": gs2326QosIpv4Ip,
       "gs2326QosIpv4Mask": gs2326QosIpv4Mask,
       "gs2326QosIpv4IPFragment": gs2326QosIpv4IPFragment,
       "gs2326QosIpv4DSCP": gs2326QosIpv4DSCP,
       "gs2326QosIpv6Protocol": gs2326QosIpv6Protocol,
       "gs2326QosIpv6ProtocolValue": gs2326QosIpv6ProtocolValue,
       "gs2326QosIpv6ProtocolUDPSport": gs2326QosIpv6ProtocolUDPSport,
       "gs2326QosIpv6ProtocolUDPDport": gs2326QosIpv6ProtocolUDPDport,
       "gs2326QosIpv6ProtocolTCPSport": gs2326QosIpv6ProtocolTCPSport,
       "gs2326QosIpv6ProtocolTCPDport": gs2326QosIpv6ProtocolTCPDport,
       "gs2326QosIpv6Ip": gs2326QosIpv6Ip,
       "gs2326QosIpv6Mask": gs2326QosIpv6Mask,
       "gs2326QosIpv6DSCP": gs2326QosIpv6DSCP,
       "gs2326QosActionClass": gs2326QosActionClass,
       "gs2326QosActionDPL": gs2326QosActionDPL,
       "gs2326QosActionDSCP": gs2326QosActionDSCP,
       "gs2326QosQceRowStatus": gs2326QosQceRowStatus,
       "gs2326QosQceMoveID": gs2326QosQceMoveID,
       "gs2326QosQceMoveNextID": gs2326QosQceMoveNextID,
       "gs2326QosQCLStatusTable": gs2326QosQCLStatusTable,
       "gs2326QosQCLStatusEntry": gs2326QosQCLStatusEntry,
       "gs2326QosQCLStatusList": gs2326QosQCLStatusList,
       "gs2326QosQCLStatusUser": gs2326QosQCLStatusUser,
       "gs2326QosQCLStatusQCEId": gs2326QosQCLStatusQCEId,
       "gs2326QosQCLStatusFrameType": gs2326QosQCLStatusFrameType,
       "gs2326QosQCLStatusPortlist": gs2326QosQCLStatusPortlist,
       "gs2326QosQCLStatusActionClass": gs2326QosQCLStatusActionClass,
       "gs2326QosQCLStatusActionDPL": gs2326QosQCLStatusActionDPL,
       "gs2326QosQCLStatusActionDSCP": gs2326QosQCLStatusActionDSCP,
       "gs2326QosQCLStatusActionConflict": gs2326QosQCLStatusActionConflict,
       "gs2326QosStormControl": gs2326QosStormControl,
       "gs2326QoSStormControlUC": gs2326QoSStormControlUC,
       "gs2326QoSStormControlUCRate": gs2326QoSStormControlUCRate,
       "gs2326QoSStormControlMC": gs2326QoSStormControlMC,
       "gs2326QoSStormControlMCRate": gs2326QoSStormControlMCRate,
       "gs2326QoSStormControlBC": gs2326QoSStormControlBC,
       "gs2326QoSStormControlBCRate": gs2326QoSStormControlBCRate,
       "gs2326Vlan": gs2326Vlan,
       "gs2326VlanPorts": gs2326VlanPorts,
       "gs2326VlanPortsTPIDforCustomSport": gs2326VlanPortsTPIDforCustomSport,
       "gs2326VlanPortsTable": gs2326VlanPortsTable,
       "gs2326VlanPortsEntry": gs2326VlanPortsEntry,
       "gs2326VlanPortsPort": gs2326VlanPortsPort,
       "gs2326VlanPortsPVID": gs2326VlanPortsPVID,
       "gs2326VlanPortsFrameType": gs2326VlanPortsFrameType,
       "gs2326VlanPortsIngressFilter": gs2326VlanPortsIngressFilter,
       "gs2326VlanPortsEgressRule": gs2326VlanPortsEgressRule,
       "gs2326VlanPortsPortType": gs2326VlanPortsPortType,
       "gs2326VlanPrivateVLAN": gs2326VlanPrivateVLAN,
       "gs2326VlanPrivateVLANMembership": gs2326VlanPrivateVLANMembership,
       "gs2326VlanPrivateVLANMembershipCreate": gs2326VlanPrivateVLANMembershipCreate,
       "gs2326VlanPrivateVLANMembershipTable": gs2326VlanPrivateVLANMembershipTable,
       "gs2326VlanPrivateVLANMembershipEntry": gs2326VlanPrivateVLANMembershipEntry,
       "gs2326VlanPrivateVLANIndex": gs2326VlanPrivateVLANIndex,
       "gs2326VlanPrivateVLANID": gs2326VlanPrivateVLANID,
       "gs2326VlanPrivateVLANMemberships": gs2326VlanPrivateVLANMemberships,
       "gs2326VlanPrivateVLANRowStatus": gs2326VlanPrivateVLANRowStatus,
       "gs2326VlanPortIsolationTable": gs2326VlanPortIsolationTable,
       "gs2326VlanPortIsolationEntry": gs2326VlanPortIsolationEntry,
       "gs2326VlanPortIsolationPort": gs2326VlanPortIsolationPort,
       "gs2326VlanPortIsolation": gs2326VlanPortIsolation,
       "gs2326MACbasedVLAN": gs2326MACbasedVLAN,
       "gs2326MACbasedVLANConf": gs2326MACbasedVLANConf,
       "gs2326MACbasedVLANConfCreate": gs2326MACbasedVLANConfCreate,
       "gs2326MACbasedVLANConfTable": gs2326MACbasedVLANConfTable,
       "gs2326MACbasedVLANConfEntry": gs2326MACbasedVLANConfEntry,
       "gs2326MACbasedVLANIndex": gs2326MACbasedVLANIndex,
       "gs2326MACbasedVLANMACAddress": gs2326MACbasedVLANMACAddress,
       "gs2326MACbasedVLANID": gs2326MACbasedVLANID,
       "gs2326MACbasedMemberships": gs2326MACbasedMemberships,
       "gs2326MACbaseRowStatus": gs2326MACbaseRowStatus,
       "gs2326IGMPSnooping": gs2326IGMPSnooping,
       "gs2326IGMPSnoopingBasic": gs2326IGMPSnoopingBasic,
       "gs2326IGMPSnoopingEnable": gs2326IGMPSnoopingEnable,
       "gs2326IGMPSnoopingUnregisteredIPMCv4Flooding": gs2326IGMPSnoopingUnregisteredIPMCv4Flooding,
       "gs2326IGMPSnoopingSSMIPRangeAddr": gs2326IGMPSnoopingSSMIPRangeAddr,
       "gs2326IGMPSnoopingSSMIPRangeValue": gs2326IGMPSnoopingSSMIPRangeValue,
       "gs2326IGMPSnoopingProxyEnabled": gs2326IGMPSnoopingProxyEnabled,
       "gs2326IGMPSnoopingPortRelatedTable": gs2326IGMPSnoopingPortRelatedTable,
       "gs2326IGMPSnoopingPortRelatedEntry": gs2326IGMPSnoopingPortRelatedEntry,
       "gs2326IGMPSnoopingRouterPort": gs2326IGMPSnoopingRouterPort,
       "gs2326IGMPSnoopingFastLeave": gs2326IGMPSnoopingFastLeave,
       "gs2326IGMPSnoopingThrottling": gs2326IGMPSnoopingThrottling,
       "gs2326IGMPSnoopingVLANTable": gs2326IGMPSnoopingVLANTable,
       "gs2326IGMPSnoopingVLANEntry": gs2326IGMPSnoopingVLANEntry,
       "gs2326IGMPSnoopingVLANID": gs2326IGMPSnoopingVLANID,
       "gs2326IGMPSnoopingVLANEnable": gs2326IGMPSnoopingVLANEnable,
       "gs2326IGMPSnoopingVLANIGMPQuerier": gs2326IGMPSnoopingVLANIGMPQuerier,
       "gs2326IGMPSnoopingVLANCompatibility": gs2326IGMPSnoopingVLANCompatibility,
       "gs2326IGMPSnoopingVLANRV": gs2326IGMPSnoopingVLANRV,
       "gs2326IGMPSnoopingVLANQI": gs2326IGMPSnoopingVLANQI,
       "gs2326IGMPSnoopingVLANQRI": gs2326IGMPSnoopingVLANQRI,
       "gs2326IGMPSnoopingVLANLLQI": gs2326IGMPSnoopingVLANLLQI,
       "gs2326IGMPSnoopingVLANURI": gs2326IGMPSnoopingVLANURI,
       "gs2326IGMPSnoopingPortGroupFiltering": gs2326IGMPSnoopingPortGroupFiltering,
       "gs2326IGMPSnoopingPortGroupFilteringCreate": gs2326IGMPSnoopingPortGroupFilteringCreate,
       "gs2326IGMPSnoopingPortGroupFilteringTable": gs2326IGMPSnoopingPortGroupFilteringTable,
       "gs2326IGMPSnoopingPortGroupFilteringEntry": gs2326IGMPSnoopingPortGroupFilteringEntry,
       "gs2326IGMPSnoopingPortGroupFilteringIndex": gs2326IGMPSnoopingPortGroupFilteringIndex,
       "gs2326IGMPSnoopingPortGroupFilteringPort": gs2326IGMPSnoopingPortGroupFilteringPort,
       "gs2326IGMPSnoopingPortGroupFilteringGroups": gs2326IGMPSnoopingPortGroupFilteringGroups,
       "gs2326IGMPSnoopingPortGroupFilteringRowStatus": gs2326IGMPSnoopingPortGroupFilteringRowStatus,
       "gs2326IGMPSnoopingStatus": gs2326IGMPSnoopingStatus,
       "gs2326IGMPSnoopingstatisticClear": gs2326IGMPSnoopingstatisticClear,
       "gs2326IGMPSnoopingstatisticTable": gs2326IGMPSnoopingstatisticTable,
       "gs2326IGMPSnoopingstatisticEntry": gs2326IGMPSnoopingstatisticEntry,
       "gs2326IGMPSnoopingstatisticVLANID": gs2326IGMPSnoopingstatisticVLANID,
       "gs2326IGMPSnoopingstatisticQuerierVersion": gs2326IGMPSnoopingstatisticQuerierVersion,
       "gs2326IGMPSnoopingstatisticHostVersion": gs2326IGMPSnoopingstatisticHostVersion,
       "gs2326IGMPSnoopingstatisticQuerierStatus": gs2326IGMPSnoopingstatisticQuerierStatus,
       "gs2326IGMPSnoopingstatisticQueriesTransmitted": gs2326IGMPSnoopingstatisticQueriesTransmitted,
       "gs2326IGMPSnoopingstatisticQueriesReceived": gs2326IGMPSnoopingstatisticQueriesReceived,
       "gs2326IGMPSnoopingstatisticV1ReportsReceived": gs2326IGMPSnoopingstatisticV1ReportsReceived,
       "gs2326IGMPSnoopingstatisticV2ReportsReceived": gs2326IGMPSnoopingstatisticV2ReportsReceived,
       "gs2326IGMPSnoopingstatisticV3ReportsReceived": gs2326IGMPSnoopingstatisticV3ReportsReceived,
       "gs2326IGMPSnoopingstatisticV2LeavesReceived": gs2326IGMPSnoopingstatisticV2LeavesReceived,
       "gs2326IGMPSnoopingRouterPortTable": gs2326IGMPSnoopingRouterPortTable,
       "gs2326IGMPSnoopingRouterPortEntry": gs2326IGMPSnoopingRouterPortEntry,
       "gs2326IGMPSnoopingRouterPortStatus": gs2326IGMPSnoopingRouterPortStatus,
       "gs2326IGMPSnoopingGroupsTable": gs2326IGMPSnoopingGroupsTable,
       "gs2326IGMPSnoopingGroupsEntry": gs2326IGMPSnoopingGroupsEntry,
       "gs2326IGMPSnoopingGroupsIndex": gs2326IGMPSnoopingGroupsIndex,
       "gs2326IGMPSnoopingGroupsVLANID": gs2326IGMPSnoopingGroupsVLANID,
       "gs2326IGMPSnoopingGroups": gs2326IGMPSnoopingGroups,
       "gs2326IGMPSnoopingGroupsMemberships": gs2326IGMPSnoopingGroupsMemberships,
       "gs2326IGMPSnoopingSSMTable": gs2326IGMPSnoopingSSMTable,
       "gs2326IGMPSnoopingSSMEntry": gs2326IGMPSnoopingSSMEntry,
       "gs2326IGMPSnoopingSSMIndex": gs2326IGMPSnoopingSSMIndex,
       "gs2326IGMPSnoopingSSMVLANID": gs2326IGMPSnoopingSSMVLANID,
       "gs2326IGMPSnoopingSSMGroup": gs2326IGMPSnoopingSSMGroup,
       "gs2326IGMPSnoopingSSMPort": gs2326IGMPSnoopingSSMPort,
       "gs2326IGMPSnoopingSSMMode": gs2326IGMPSnoopingSSMMode,
       "gs2326IGMPSnoopingSSMSourceAddress": gs2326IGMPSnoopingSSMSourceAddress,
       "gs2326IGMPSnoopingSSMType": gs2326IGMPSnoopingSSMType,
       "gs2326MLDSnooping": gs2326MLDSnooping,
       "gs2326MLDSnoopingBasic": gs2326MLDSnoopingBasic,
       "gs2326MLDSnoopingEnable": gs2326MLDSnoopingEnable,
       "gs2326MLDSnoopingUnregisteredIPMCv6Flooding": gs2326MLDSnoopingUnregisteredIPMCv6Flooding,
       "gs2326MLDSnoopingSSMIPRangeAddr": gs2326MLDSnoopingSSMIPRangeAddr,
       "gs2326MLDSnoopingSSMIPRangeValue": gs2326MLDSnoopingSSMIPRangeValue,
       "gs2326MLDSnoopingProxyEnabled": gs2326MLDSnoopingProxyEnabled,
       "gs2326MLDSnoopingPortRelatedTable": gs2326MLDSnoopingPortRelatedTable,
       "gs2326MLDSnoopingPortRelatedEntry": gs2326MLDSnoopingPortRelatedEntry,
       "gs2326MLDSnoopingRouterPort": gs2326MLDSnoopingRouterPort,
       "gs2326MLDSnoopingFastLeave": gs2326MLDSnoopingFastLeave,
       "gs2326MLDSnoopingThrottling": gs2326MLDSnoopingThrottling,
       "gs2326MLDSnoopingVLANTable": gs2326MLDSnoopingVLANTable,
       "gs2326MLDSnoopingVLANEntry": gs2326MLDSnoopingVLANEntry,
       "gs2326MLDSnoopingVLANID": gs2326MLDSnoopingVLANID,
       "gs2326MLDSnoopingVLANEnable": gs2326MLDSnoopingVLANEnable,
       "gs2326MLDSnoopingVLANIGMPQuerier": gs2326MLDSnoopingVLANIGMPQuerier,
       "gs2326MLDSnoopingVLANCompatibility": gs2326MLDSnoopingVLANCompatibility,
       "gs2326MLDSnoopingVLANRV": gs2326MLDSnoopingVLANRV,
       "gs2326MLDSnoopingVLANQI": gs2326MLDSnoopingVLANQI,
       "gs2326MLDSnoopingVLANQRI": gs2326MLDSnoopingVLANQRI,
       "gs2326MLDSnoopingVLANLLQI": gs2326MLDSnoopingVLANLLQI,
       "gs2326MLDSnoopingVLANURI": gs2326MLDSnoopingVLANURI,
       "gs2326MLDSnoopingPortGroupFiltering": gs2326MLDSnoopingPortGroupFiltering,
       "gs2326MLDSnoopingPortGroupFilteringCreate": gs2326MLDSnoopingPortGroupFilteringCreate,
       "gs2326MLDSnoopingPortGroupFilteringTable": gs2326MLDSnoopingPortGroupFilteringTable,
       "gs2326MLDSnoopingPortGroupFilteringEntry": gs2326MLDSnoopingPortGroupFilteringEntry,
       "gs2326MLDSnoopingPortGroupFilteringIndex": gs2326MLDSnoopingPortGroupFilteringIndex,
       "gs2326MLDSnoopingPortGroupFilteringPort": gs2326MLDSnoopingPortGroupFilteringPort,
       "gs2326MLDSnoopingPortGroupFilteringGroups": gs2326MLDSnoopingPortGroupFilteringGroups,
       "gs2326MLDSnoopingPortGroupFilteringRowStatus": gs2326MLDSnoopingPortGroupFilteringRowStatus,
       "gs2326MLDSnoopingStatus": gs2326MLDSnoopingStatus,
       "gs2326MLDSnoopingstatisticClear": gs2326MLDSnoopingstatisticClear,
       "gs2326MLDSnoopingstatisticTable": gs2326MLDSnoopingstatisticTable,
       "gs2326MLDSnoopingstatisticEntry": gs2326MLDSnoopingstatisticEntry,
       "gs2326MLDSnoopingstatisticVLANID": gs2326MLDSnoopingstatisticVLANID,
       "gs2326MLDSnoopingstatisticQuerierVersion": gs2326MLDSnoopingstatisticQuerierVersion,
       "gs2326MLDSnoopingstatisticHostVersion": gs2326MLDSnoopingstatisticHostVersion,
       "gs2326MLDSnoopingstatisticQuerierStatus": gs2326MLDSnoopingstatisticQuerierStatus,
       "gs2326MLDSnoopingstatisticQueriesTransmitted": gs2326MLDSnoopingstatisticQueriesTransmitted,
       "gs2326MLDSnoopingstatisticQueriesReceived": gs2326MLDSnoopingstatisticQueriesReceived,
       "gs2326MLDSnoopingstatisticV1ReportsReceived": gs2326MLDSnoopingstatisticV1ReportsReceived,
       "gs2326MLDSnoopingstatisticV2ReportsReceived": gs2326MLDSnoopingstatisticV2ReportsReceived,
       "gs2326MLDSnoopingstatisticV1LeavesReceived": gs2326MLDSnoopingstatisticV1LeavesReceived,
       "gs2326MLDSnoopingRouterPortTable": gs2326MLDSnoopingRouterPortTable,
       "gs2326MLDSnoopingRouterPortEntry": gs2326MLDSnoopingRouterPortEntry,
       "gs2326MLDSnoopingRouterPortStatus": gs2326MLDSnoopingRouterPortStatus,
       "gs2326MLDSnoopingGroupsTable": gs2326MLDSnoopingGroupsTable,
       "gs2326MLDSnoopingGroupsEntry": gs2326MLDSnoopingGroupsEntry,
       "gs2326MLDSnoopingGroupsIndex": gs2326MLDSnoopingGroupsIndex,
       "gs2326MLDSnoopingGroupsVLANID": gs2326MLDSnoopingGroupsVLANID,
       "gs2326MLDSnoopingGroups": gs2326MLDSnoopingGroups,
       "gs2326MLDSnoopingGroupsMemberships": gs2326MLDSnoopingGroupsMemberships,
       "gs2326MLDSnoopingSSMTable": gs2326MLDSnoopingSSMTable,
       "gs2326MLDSnoopingSSMEntry": gs2326MLDSnoopingSSMEntry,
       "gs2326MLDSnoopingSSMIndex": gs2326MLDSnoopingSSMIndex,
       "gs2326MLDSnoopingSSMVLANID": gs2326MLDSnoopingSSMVLANID,
       "gs2326MLDSnoopingSSMGroup": gs2326MLDSnoopingSSMGroup,
       "gs2326MLDSnoopingSSMPort": gs2326MLDSnoopingSSMPort,
       "gs2326MLDSnoopingSSMMode": gs2326MLDSnoopingSSMMode,
       "gs2326MLDSnoopingSSMSourceAddress": gs2326MLDSnoopingSSMSourceAddress,
       "gs2326MLDSnoopingSSMType": gs2326MLDSnoopingSSMType,
       "gs2326MVR": gs2326MVR,
       "gs2326MVRConfiguration": gs2326MVRConfiguration,
       "gs2326MVRMode": gs2326MVRMode,
       "gs2326MVRVLANId": gs2326MVRVLANId,
       "gs2326MVRPortConfigurationTable": gs2326MVRPortConfigurationTable,
       "gs2326MVRPortConfigurationEntry": gs2326MVRPortConfigurationEntry,
       "gs2326MVRPortConfigurationMode": gs2326MVRPortConfigurationMode,
       "gs2326MVRPortConfigurationType": gs2326MVRPortConfigurationType,
       "gs2326MVRPortConfigurationImmediateLeave": gs2326MVRPortConfigurationImmediateLeave,
       "gs2326MVRPortGroupFiltering": gs2326MVRPortGroupFiltering,
       "gs2326MVRPortGroupFilteringCreate": gs2326MVRPortGroupFilteringCreate,
       "gs2326MVRPortGroupFilteringTable": gs2326MVRPortGroupFilteringTable,
       "gs2326MVRPortGroupFilteringEntry": gs2326MVRPortGroupFilteringEntry,
       "gs2326MVRPortGroupFilteringIndex": gs2326MVRPortGroupFilteringIndex,
       "gs2326MVRPortGroupFilteringPort": gs2326MVRPortGroupFilteringPort,
       "gs2326MVRPortGroupFilteringStartGroups": gs2326MVRPortGroupFilteringStartGroups,
       "gs2326MVRPortGroupFilteringEndGroups": gs2326MVRPortGroupFilteringEndGroups,
       "gs2326MVRPortGroupFilteringRowStatus": gs2326MVRPortGroupFilteringRowStatus,
       "gs2326MVRGroupsTable": gs2326MVRGroupsTable,
       "gs2326MVRGroupsEntry": gs2326MVRGroupsEntry,
       "gs2326MVRGroupsIndex": gs2326MVRGroupsIndex,
       "gs2326MVRGroupsVLANID": gs2326MVRGroupsVLANID,
       "gs2326MVRGroups": gs2326MVRGroups,
       "gs2326MVRGroupsMemberships": gs2326MVRGroupsMemberships,
       "gs2326MVRStatus": gs2326MVRStatus,
       "gs2326MVRstatisticClear": gs2326MVRstatisticClear,
       "gs2326MVRstatisticVLANID": gs2326MVRstatisticVLANID,
       "gs2326MVRstatisticV1ReportsReceived": gs2326MVRstatisticV1ReportsReceived,
       "gs2326MVRstatisticV2ReportsReceived": gs2326MVRstatisticV2ReportsReceived,
       "gs2326MVRstatisticV3ReportsReceived": gs2326MVRstatisticV3ReportsReceived,
       "gs2326MVRstatisticV2LeavesReceived": gs2326MVRstatisticV2LeavesReceived,
       "gs2326LACP": gs2326LACP,
       "gs2326LACPConf": gs2326LACPConf,
       "gs2326LACPPortConfigurationTable": gs2326LACPPortConfigurationTable,
       "gs2326LACPPortConfigurationEntry": gs2326LACPPortConfigurationEntry,
       "gs2326LACPPortConfigurationPort": gs2326LACPPortConfigurationPort,
       "gs2326LACPPortConfigurationMode": gs2326LACPPortConfigurationMode,
       "gs2326LACPPortConfigurationKey": gs2326LACPPortConfigurationKey,
       "gs2326LACPPortConfigurationRole": gs2326LACPPortConfigurationRole,
       "gs2326LACPSystemStatusTable": gs2326LACPSystemStatusTable,
       "gs2326LACPSystemStatusEntry": gs2326LACPSystemStatusEntry,
       "gs2326LACPSystemStatusIndex": gs2326LACPSystemStatusIndex,
       "gs2326LACPSystemStatusAggrID": gs2326LACPSystemStatusAggrID,
       "gs2326LACPSystemStatusPartnerSystemID": gs2326LACPSystemStatusPartnerSystemID,
       "gs2326LACPSystemStatusPartnerKey": gs2326LACPSystemStatusPartnerKey,
       "gs2326LACPSystemStatusLastchanged": gs2326LACPSystemStatusLastchanged,
       "gs2326LACPSystemStatusLocalPorts": gs2326LACPSystemStatusLocalPorts,
       "gs2326LACPStatusTable": gs2326LACPStatusTable,
       "gs2326LACPStatusEntry": gs2326LACPStatusEntry,
       "gs2326LACPStatusPort": gs2326LACPStatusPort,
       "gs2326LACPStatusLACP": gs2326LACPStatusLACP,
       "gs2326LACPStatusKey": gs2326LACPStatusKey,
       "gs2326LACPStatusAggrID": gs2326LACPStatusAggrID,
       "gs2326LACPStatusPartnerSystemID": gs2326LACPStatusPartnerSystemID,
       "gs2326LACPStatusPartnerPort": gs2326LACPStatusPartnerPort,
       "gs2326LACPStatisticsTable": gs2326LACPStatisticsTable,
       "gs2326LACPStatisticsEntry": gs2326LACPStatisticsEntry,
       "gs2326LACPStatisticsPort": gs2326LACPStatisticsPort,
       "gs2326LACPReceived": gs2326LACPReceived,
       "gs2326LACPTransmitted": gs2326LACPTransmitted,
       "gs2326LACPDiscardedUnknown": gs2326LACPDiscardedUnknown,
       "gs2326LACPDiscardedIllegal": gs2326LACPDiscardedIllegal,
       "gs2326LACPStatisticsClear": gs2326LACPStatisticsClear,
       "gs2326STP": gs2326STP,
       "gs2326STPBridgeBasicConf": gs2326STPBridgeBasicConf,
       "gs2326STPBridgeProtocolVersion": gs2326STPBridgeProtocolVersion,
       "gs2326STPBridgePriority": gs2326STPBridgePriority,
       "gs2326STPBridgeForwardDelay": gs2326STPBridgeForwardDelay,
       "gs2326STPBridgeMaxAge": gs2326STPBridgeMaxAge,
       "gs2326STPBridgeMaximumHopCount": gs2326STPBridgeMaximumHopCount,
       "gs2326STPBridgeTransmitHoldCount": gs2326STPBridgeTransmitHoldCount,
       "gs2326STPBridgeAdvancedConf": gs2326STPBridgeAdvancedConf,
       "gs2326STPBridgeEdgePortBPDUFiltering": gs2326STPBridgeEdgePortBPDUFiltering,
       "gs2326STPBridgeEdgePortBPDUGuard": gs2326STPBridgeEdgePortBPDUGuard,
       "gs2326STPBridgePortErrorRecoveryTimeout": gs2326STPBridgePortErrorRecoveryTimeout,
       "gs2326STPMSTIConf": gs2326STPMSTIConf,
       "gs2326STPMSTIConfigurationName": gs2326STPMSTIConfigurationName,
       "gs2326STPMSTIConfigurationRevision": gs2326STPMSTIConfigurationRevision,
       "gs2326STPMSTIMappingConf": gs2326STPMSTIMappingConf,
       "gs2326STPMSTI1VLANsMapped": gs2326STPMSTI1VLANsMapped,
       "gs2326STPMSTI2VLANsMapped": gs2326STPMSTI2VLANsMapped,
       "gs2326STPMSTI3VLANsMapped": gs2326STPMSTI3VLANsMapped,
       "gs2326STPMSTI4VLANsMapped": gs2326STPMSTI4VLANsMapped,
       "gs2326STPMSTI5VLANsMapped": gs2326STPMSTI5VLANsMapped,
       "gs2326STPMSTI6VLANsMapped": gs2326STPMSTI6VLANsMapped,
       "gs2326STPMSTI7VLANsMapped": gs2326STPMSTI7VLANsMapped,
       "gs2326STPMSTIPriority": gs2326STPMSTIPriority,
       "gs2326STPCISTPriority": gs2326STPCISTPriority,
       "gs2326STPMSTI1Priority": gs2326STPMSTI1Priority,
       "gs2326STPMSTI2Priority": gs2326STPMSTI2Priority,
       "gs2326STPMSTI3Priority": gs2326STPMSTI3Priority,
       "gs2326STPMSTI4Priority": gs2326STPMSTI4Priority,
       "gs2326STPMSTI5Priority": gs2326STPMSTI5Priority,
       "gs2326STPMSTI6Priority": gs2326STPMSTI6Priority,
       "gs2326STPMSTI7Priority": gs2326STPMSTI7Priority,
       "gs2326STPCISTPort": gs2326STPCISTPort,
       "gs2326STPCISTAggregatedPort": gs2326STPCISTAggregatedPort,
       "gs2326STPCISTAggregatedPortSTPEnabled": gs2326STPCISTAggregatedPortSTPEnabled,
       "gs2326STPCISTAggregatedPortPathCost": gs2326STPCISTAggregatedPortPathCost,
       "gs2326STPCISTAggregatedPortPriority": gs2326STPCISTAggregatedPortPriority,
       "gs2326STPCISTAggregatedPortAdminEdge": gs2326STPCISTAggregatedPortAdminEdge,
       "gs2326STPCISTAggregatedPortAutoEdge": gs2326STPCISTAggregatedPortAutoEdge,
       "gs2326STPCISTAggregatedPortRestrictedRole": gs2326STPCISTAggregatedPortRestrictedRole,
       "gs2326STPCISTAggregatedPortRestrictedTCN": gs2326STPCISTAggregatedPortRestrictedTCN,
       "gs2326STPCISTAggregatedPortBPDUGuard": gs2326STPCISTAggregatedPortBPDUGuard,
       "gs2326STPCISTAggregatedPortPointtoPoint": gs2326STPCISTAggregatedPortPointtoPoint,
       "gs2326STPCISTNormalPortTable": gs2326STPCISTNormalPortTable,
       "gs2326STPCISTNormalPortEntry": gs2326STPCISTNormalPortEntry,
       "gs2326STPCISTNormalPortConfPort": gs2326STPCISTNormalPortConfPort,
       "gs2326STPCISTNormalPortSTPEnabled": gs2326STPCISTNormalPortSTPEnabled,
       "gs2326STPCISTNormalPortPathCost": gs2326STPCISTNormalPortPathCost,
       "gs2326STPCISTNormalPortPriority": gs2326STPCISTNormalPortPriority,
       "gs2326STPCISTNormalPortAdminEdge": gs2326STPCISTNormalPortAdminEdge,
       "gs2326STPCISTNormalPortAutoEdge": gs2326STPCISTNormalPortAutoEdge,
       "gs2326STPCISTNormalPortRestrictedRole": gs2326STPCISTNormalPortRestrictedRole,
       "gs2326STPCISTNormalPortRestrictedTCN": gs2326STPCISTNormalPortRestrictedTCN,
       "gs2326STPCISTNormalPortBPDUGuard": gs2326STPCISTNormalPortBPDUGuard,
       "gs2326STPCISTNormalPortPointtoPoint": gs2326STPCISTNormalPortPointtoPoint,
       "gs2326STPMSTIPort": gs2326STPMSTIPort,
       "gs2326STPMSTI1Port": gs2326STPMSTI1Port,
       "gs2326STPMSTI1AggregatedPort": gs2326STPMSTI1AggregatedPort,
       "gs2326STPMSTI1AggregatedPortPathCost": gs2326STPMSTI1AggregatedPortPathCost,
       "gs2326STPMSTI1AggregatedPortPriority": gs2326STPMSTI1AggregatedPortPriority,
       "gs2326STPMSTI1NormalPortTable": gs2326STPMSTI1NormalPortTable,
       "gs2326STPMSTI1NormalPortEntry": gs2326STPMSTI1NormalPortEntry,
       "gs2326STPMSTI1NormalPortConfPort": gs2326STPMSTI1NormalPortConfPort,
       "gs2326STPMSTI1NormalPortPathCost": gs2326STPMSTI1NormalPortPathCost,
       "gs2326STPMSTI1NormalPortPriority": gs2326STPMSTI1NormalPortPriority,
       "gs2326STPMSTI2Port": gs2326STPMSTI2Port,
       "gs2326STPMSTI2AggregatedPort": gs2326STPMSTI2AggregatedPort,
       "gs2326STPMSTI2AggregatedPortPathCost": gs2326STPMSTI2AggregatedPortPathCost,
       "gs2326STPMSTI2AggregatedPortPriority": gs2326STPMSTI2AggregatedPortPriority,
       "gs2326STPMSTI2NormalPortTable": gs2326STPMSTI2NormalPortTable,
       "gs2326STPMSTI2NormalPortEntry": gs2326STPMSTI2NormalPortEntry,
       "gs2326STPMSTI2NormalPortConfPort": gs2326STPMSTI2NormalPortConfPort,
       "gs2326STPMSTI2NormalPortPathCost": gs2326STPMSTI2NormalPortPathCost,
       "gs2326STPMSTI2NormalPortPriority": gs2326STPMSTI2NormalPortPriority,
       "gs2326STPMSTI3Port": gs2326STPMSTI3Port,
       "gs2326STPMSTI3AggregatedPort": gs2326STPMSTI3AggregatedPort,
       "gs2326STPMSTI3AggregatedPortPathCost": gs2326STPMSTI3AggregatedPortPathCost,
       "gs2326STPMSTI3AggregatedPortPriority": gs2326STPMSTI3AggregatedPortPriority,
       "gs2326STPMSTI3NormalPortTable": gs2326STPMSTI3NormalPortTable,
       "gs2326STPMSTI3NormalPortEntry": gs2326STPMSTI3NormalPortEntry,
       "gs2326STPMSTI3NormalPortConfPort": gs2326STPMSTI3NormalPortConfPort,
       "gs2326STPMSTI3NormalPortPathCost": gs2326STPMSTI3NormalPortPathCost,
       "gs2326STPMSTI3NormalPortPriority": gs2326STPMSTI3NormalPortPriority,
       "gs2326STPMSTI4Port": gs2326STPMSTI4Port,
       "gs2326STPMSTI4AggregatedPort": gs2326STPMSTI4AggregatedPort,
       "gs2326STPMSTI4AggregatedPortPathCost": gs2326STPMSTI4AggregatedPortPathCost,
       "gs2326STPMSTI4AggregatedPortPriority": gs2326STPMSTI4AggregatedPortPriority,
       "gs2326STPMSTI4NormalPortTable": gs2326STPMSTI4NormalPortTable,
       "gs2326STPMSTI4NormalPortEntry": gs2326STPMSTI4NormalPortEntry,
       "gs2326STPMSTI4NormalPortConfPort": gs2326STPMSTI4NormalPortConfPort,
       "gs2326STPMSTI4NormalPortPathCost": gs2326STPMSTI4NormalPortPathCost,
       "gs2326STPMSTI4NormalPortPriority": gs2326STPMSTI4NormalPortPriority,
       "gs2326STPMSTI5Port": gs2326STPMSTI5Port,
       "gs2326STPMSTI5AggregatedPort": gs2326STPMSTI5AggregatedPort,
       "gs2326STPMSTI5AggregatedPortPathCost": gs2326STPMSTI5AggregatedPortPathCost,
       "gs2326STPMSTI5AggregatedPortPriority": gs2326STPMSTI5AggregatedPortPriority,
       "gs2326STPMSTI5NormalPortTable": gs2326STPMSTI5NormalPortTable,
       "gs2326STPMSTI5NormalPortEntry": gs2326STPMSTI5NormalPortEntry,
       "gs2326STPMSTI5NormalPortConfPort": gs2326STPMSTI5NormalPortConfPort,
       "gs2326STPMSTI5NormalPortPathCost": gs2326STPMSTI5NormalPortPathCost,
       "gs2326STPMSTI5NormalPortPriority": gs2326STPMSTI5NormalPortPriority,
       "gs2326STPMSTI6Port": gs2326STPMSTI6Port,
       "gs2326STPMSTI6AggregatedPort": gs2326STPMSTI6AggregatedPort,
       "gs2326STPMSTI6AggregatedPortPathCost": gs2326STPMSTI6AggregatedPortPathCost,
       "gs2326STPMSTI6AggregatedPortPriority": gs2326STPMSTI6AggregatedPortPriority,
       "gs2326STPMSTI6NormalPortTable": gs2326STPMSTI6NormalPortTable,
       "gs2326STPMSTI6NormalPortEntry": gs2326STPMSTI6NormalPortEntry,
       "gs2326STPMSTI6NormalPortConfPort": gs2326STPMSTI6NormalPortConfPort,
       "gs2326STPMSTI6NormalPortPathCost": gs2326STPMSTI6NormalPortPathCost,
       "gs2326STPMSTI6NormalPortPriority": gs2326STPMSTI6NormalPortPriority,
       "gs2326STPMSTI7Port": gs2326STPMSTI7Port,
       "gs2326STPMSTI7AggregatedPort": gs2326STPMSTI7AggregatedPort,
       "gs2326STPMSTI7AggregatedPortPathCost": gs2326STPMSTI7AggregatedPortPathCost,
       "gs2326STPMSTI7AggregatedPortPriority": gs2326STPMSTI7AggregatedPortPriority,
       "gs2326STPMSTI7NormalPortTable": gs2326STPMSTI7NormalPortTable,
       "gs2326STPMSTI7NormalPortEntry": gs2326STPMSTI7NormalPortEntry,
       "gs2326STPMSTI7NormalPortConfPort": gs2326STPMSTI7NormalPortConfPort,
       "gs2326STPMSTI7NormalPortPathCost": gs2326STPMSTI7NormalPortPathCost,
       "gs2326STPMSTI7NormalPortPriority": gs2326STPMSTI7NormalPortPriority,
       "gs2326STPBridgeStatus": gs2326STPBridgeStatus,
       "gs2326CISTBridgeSTP": gs2326CISTBridgeSTP,
       "gs2326CISTBridgeSTPStatus": gs2326CISTBridgeSTPStatus,
       "gs2326CISTBridgeInstance": gs2326CISTBridgeInstance,
       "gs2326CISTBridgeID": gs2326CISTBridgeID,
       "gs2326CISTRootID": gs2326CISTRootID,
       "gs2326CISTRootPort": gs2326CISTRootPort,
       "gs2326CISTRootCost": gs2326CISTRootCost,
       "gs2326CISTRegionalRoot": gs2326CISTRegionalRoot,
       "gs2326CISTInternalRootCost": gs2326CISTInternalRootCost,
       "gs2326CISTTopologyFlag": gs2326CISTTopologyFlag,
       "gs2326CISTTopologyChangeCount": gs2326CISTTopologyChangeCount,
       "gs2326CISTTopologyChangeLast": gs2326CISTTopologyChangeLast,
       "gs2326CISTPortStateTable": gs2326CISTPortStateTable,
       "gs2326CISTPortStateEntry": gs2326CISTPortStateEntry,
       "gs2326CISTPortStateIndex": gs2326CISTPortStateIndex,
       "gs2326CISTPortStatePort": gs2326CISTPortStatePort,
       "gs2326CISTPortStatePortID": gs2326CISTPortStatePortID,
       "gs2326CISTPortStateRole": gs2326CISTPortStateRole,
       "gs2326CISTPortStateState": gs2326CISTPortStateState,
       "gs2326CISTPortStatePathCost": gs2326CISTPortStatePathCost,
       "gs2326CISTPortStateEdge": gs2326CISTPortStateEdge,
       "gs2326CISTPortStatePoint2Point": gs2326CISTPortStatePoint2Point,
       "gs2326CISTPortStateUptime": gs2326CISTPortStateUptime,
       "gs2326MSTI1BridgeSTP": gs2326MSTI1BridgeSTP,
       "gs2326MSTI1BridgeSTPStatus": gs2326MSTI1BridgeSTPStatus,
       "gs2326MSTI1BridgeInstance": gs2326MSTI1BridgeInstance,
       "gs2326MSTI1BridgeID": gs2326MSTI1BridgeID,
       "gs2326MSTI1RootID": gs2326MSTI1RootID,
       "gs2326MSTI1RootPort": gs2326MSTI1RootPort,
       "gs2326MSTI1RootCost": gs2326MSTI1RootCost,
       "gs2326MSTI1TopologyFlag": gs2326MSTI1TopologyFlag,
       "gs2326MSTI1TopologyChangeCount": gs2326MSTI1TopologyChangeCount,
       "gs2326MSTI1TopologyChangeLast": gs2326MSTI1TopologyChangeLast,
       "gs2326MSTI1PortStateTable": gs2326MSTI1PortStateTable,
       "gs2326MSTI1PortStateEntry": gs2326MSTI1PortStateEntry,
       "gs2326MSTI1PortStateIndex": gs2326MSTI1PortStateIndex,
       "gs2326MSTI1PortStatePort": gs2326MSTI1PortStatePort,
       "gs2326MSTI1PortStatePortID": gs2326MSTI1PortStatePortID,
       "gs2326MSTI1PortStateRole": gs2326MSTI1PortStateRole,
       "gs2326MSTI1PortStateState": gs2326MSTI1PortStateState,
       "gs2326MSTI1PortStatePathCost": gs2326MSTI1PortStatePathCost,
       "gs2326MSTI1PortStateEdge": gs2326MSTI1PortStateEdge,
       "gs2326MSTI1PortStatePoint2Point": gs2326MSTI1PortStatePoint2Point,
       "gs2326MSTI1PortStateUptime": gs2326MSTI1PortStateUptime,
       "gs2326MSTI2BridgeSTP": gs2326MSTI2BridgeSTP,
       "gs2326MSTI2BridgeSTPStatus": gs2326MSTI2BridgeSTPStatus,
       "gs2326MSTI2BridgeInstance": gs2326MSTI2BridgeInstance,
       "gs2326MSTI2BridgeID": gs2326MSTI2BridgeID,
       "gs2326MSTI2RootID": gs2326MSTI2RootID,
       "gs2326MSTI2RootPort": gs2326MSTI2RootPort,
       "gs2326MSTI2RootCost": gs2326MSTI2RootCost,
       "gs2326MSTI2TopologyFlag": gs2326MSTI2TopologyFlag,
       "gs2326MSTI2TopologyChangeCount": gs2326MSTI2TopologyChangeCount,
       "gs2326MSTI2TopologyChangeLast": gs2326MSTI2TopologyChangeLast,
       "gs2326MSTI2PortStateTable": gs2326MSTI2PortStateTable,
       "gs2326MSTI2PortStateEntry": gs2326MSTI2PortStateEntry,
       "gs2326MSTI2PortStateIndex": gs2326MSTI2PortStateIndex,
       "gs2326MSTI2PortStatePort": gs2326MSTI2PortStatePort,
       "gs2326MSTI2PortStatePortID": gs2326MSTI2PortStatePortID,
       "gs2326MSTI2PortStateRole": gs2326MSTI2PortStateRole,
       "gs2326MSTI2PortStateState": gs2326MSTI2PortStateState,
       "gs2326MSTI2PortStatePathCost": gs2326MSTI2PortStatePathCost,
       "gs2326MSTI2PortStateEdge": gs2326MSTI2PortStateEdge,
       "gs2326MSTI2PortStatePoint2Point": gs2326MSTI2PortStatePoint2Point,
       "gs2326MSTI2PortStateUptime": gs2326MSTI2PortStateUptime,
       "gs2326MSTI3BridgeSTP": gs2326MSTI3BridgeSTP,
       "gs2326MSTI3BridgeSTPStatus": gs2326MSTI3BridgeSTPStatus,
       "gs2326MSTI3BridgeInstance": gs2326MSTI3BridgeInstance,
       "gs2326MSTI3BridgeID": gs2326MSTI3BridgeID,
       "gs2326MSTI3RootID": gs2326MSTI3RootID,
       "gs2326MSTI3RootPort": gs2326MSTI3RootPort,
       "gs2326MSTI3RootCost": gs2326MSTI3RootCost,
       "gs2326MSTI3TopologyFlag": gs2326MSTI3TopologyFlag,
       "gs2326MSTI3TopologyChangeCount": gs2326MSTI3TopologyChangeCount,
       "gs2326MSTI3TopologyChangeLast": gs2326MSTI3TopologyChangeLast,
       "gs2326MSTI3PortStateTable": gs2326MSTI3PortStateTable,
       "gs2326MSTI3PortStateEntry": gs2326MSTI3PortStateEntry,
       "gs2326MSTI3PortStateIndex": gs2326MSTI3PortStateIndex,
       "gs2326MSTI3PortStatePort": gs2326MSTI3PortStatePort,
       "gs2326MSTI3PortStatePortID": gs2326MSTI3PortStatePortID,
       "gs2326MSTI3PortStateRole": gs2326MSTI3PortStateRole,
       "gs2326MSTI3PortStateState": gs2326MSTI3PortStateState,
       "gs2326MSTI3PortStatePathCost": gs2326MSTI3PortStatePathCost,
       "gs2326MSTI3PortStateEdge": gs2326MSTI3PortStateEdge,
       "gs2326MSTI3PortStatePoint2Point": gs2326MSTI3PortStatePoint2Point,
       "gs2326MSTI3PortStateUptime": gs2326MSTI3PortStateUptime,
       "gs2326MSTI4BridgeSTP": gs2326MSTI4BridgeSTP,
       "gs2326MSTI4BridgeSTPStatus": gs2326MSTI4BridgeSTPStatus,
       "gs2326MSTI4BridgeInstance": gs2326MSTI4BridgeInstance,
       "gs2326MSTI4BridgeID": gs2326MSTI4BridgeID,
       "gs2326MSTI4RootID": gs2326MSTI4RootID,
       "gs2326MSTI4RootPort": gs2326MSTI4RootPort,
       "gs2326MSTI4RootCost": gs2326MSTI4RootCost,
       "gs2326MSTI4TopologyFlag": gs2326MSTI4TopologyFlag,
       "gs2326MSTI4TopologyChangeCount": gs2326MSTI4TopologyChangeCount,
       "gs2326MSTI4TopologyChangeLast": gs2326MSTI4TopologyChangeLast,
       "gs2326MSTI4PortStateTable": gs2326MSTI4PortStateTable,
       "gs2326MSTI4PortStateEntry": gs2326MSTI4PortStateEntry,
       "gs2326MSTI4PortStateIndex": gs2326MSTI4PortStateIndex,
       "gs2326MSTI4PortStatePort": gs2326MSTI4PortStatePort,
       "gs2326MSTI4PortStatePortID": gs2326MSTI4PortStatePortID,
       "gs2326MSTI4PortStateRole": gs2326MSTI4PortStateRole,
       "gs2326MSTI4PortStateState": gs2326MSTI4PortStateState,
       "gs2326MSTI4PortStatePathCost": gs2326MSTI4PortStatePathCost,
       "gs2326MSTI4PortStateEdge": gs2326MSTI4PortStateEdge,
       "gs2326MSTI4PortStatePoint2Point": gs2326MSTI4PortStatePoint2Point,
       "gs2326MSTI4PortStateUptime": gs2326MSTI4PortStateUptime,
       "gs2326MSTI5BridgeSTP": gs2326MSTI5BridgeSTP,
       "gs2326MSTI5BridgeSTPStatus": gs2326MSTI5BridgeSTPStatus,
       "gs2326MSTI5BridgeInstance": gs2326MSTI5BridgeInstance,
       "gs2326MSTI5BridgeID": gs2326MSTI5BridgeID,
       "gs2326MSTI5RootID": gs2326MSTI5RootID,
       "gs2326MSTI5RootPort": gs2326MSTI5RootPort,
       "gs2326MSTI5RootCost": gs2326MSTI5RootCost,
       "gs2326MSTI5TopologyFlag": gs2326MSTI5TopologyFlag,
       "gs2326MSTI5TopologyChangeCount": gs2326MSTI5TopologyChangeCount,
       "gs2326MSTI5TopologyChangeLast": gs2326MSTI5TopologyChangeLast,
       "gs2326MSTI5PortStateTable": gs2326MSTI5PortStateTable,
       "gs2326MSTI5PortStateEntry": gs2326MSTI5PortStateEntry,
       "gs2326MSTI5PortStateIndex": gs2326MSTI5PortStateIndex,
       "gs2326MSTI5PortStatePort": gs2326MSTI5PortStatePort,
       "gs2326MSTI5PortStatePortID": gs2326MSTI5PortStatePortID,
       "gs2326MSTI5PortStateRole": gs2326MSTI5PortStateRole,
       "gs2326MSTI5PortStateState": gs2326MSTI5PortStateState,
       "gs2326MSTI5PortStatePathCost": gs2326MSTI5PortStatePathCost,
       "gs2326MSTI5PortStateEdge": gs2326MSTI5PortStateEdge,
       "gs2326MSTI5PortStatePoint2Point": gs2326MSTI5PortStatePoint2Point,
       "gs2326MSTI5PortStateUptime": gs2326MSTI5PortStateUptime,
       "gs2326MSTI6BridgeSTP": gs2326MSTI6BridgeSTP,
       "gs2326MSTI6BridgeSTPStatus": gs2326MSTI6BridgeSTPStatus,
       "gs2326MSTI6BridgeInstance": gs2326MSTI6BridgeInstance,
       "gs2326MSTI6BridgeID": gs2326MSTI6BridgeID,
       "gs2326MSTI6RootID": gs2326MSTI6RootID,
       "gs2326MSTI6RootPort": gs2326MSTI6RootPort,
       "gs2326MSTI6RootCost": gs2326MSTI6RootCost,
       "gs2326MSTI6TopologyFlag": gs2326MSTI6TopologyFlag,
       "gs2326MSTI6TopologyChangeCount": gs2326MSTI6TopologyChangeCount,
       "gs2326MSTI6TopologyChangeLast": gs2326MSTI6TopologyChangeLast,
       "gs2326MSTI6PortStateTable": gs2326MSTI6PortStateTable,
       "gs2326MSTI6PortStateEntry": gs2326MSTI6PortStateEntry,
       "gs2326MSTI6PortStateIndex": gs2326MSTI6PortStateIndex,
       "gs2326MSTI6PortStatePort": gs2326MSTI6PortStatePort,
       "gs2326MSTI6PortStatePortID": gs2326MSTI6PortStatePortID,
       "gs2326MSTI6PortStateRole": gs2326MSTI6PortStateRole,
       "gs2326MSTI6PortStateState": gs2326MSTI6PortStateState,
       "gs2326MSTI6PortStatePathCost": gs2326MSTI6PortStatePathCost,
       "gs2326MSTI6PortStateEdge": gs2326MSTI6PortStateEdge,
       "gs2326MSTI6PortStatePoint2Point": gs2326MSTI6PortStatePoint2Point,
       "gs2326MSTI6PortStateUptime": gs2326MSTI6PortStateUptime,
       "gs2326MSTI7BridgeSTP": gs2326MSTI7BridgeSTP,
       "gs2326MSTI7BridgeSTPStatus": gs2326MSTI7BridgeSTPStatus,
       "gs2326MSTI7BridgeInstance": gs2326MSTI7BridgeInstance,
       "gs2326MSTI7BridgeID": gs2326MSTI7BridgeID,
       "gs2326MSTI7RootID": gs2326MSTI7RootID,
       "gs2326MSTI7RootPort": gs2326MSTI7RootPort,
       "gs2326MSTI7RootCost": gs2326MSTI7RootCost,
       "gs2326MSTI7TopologyFlag": gs2326MSTI7TopologyFlag,
       "gs2326MSTI7TopologyChangeCount": gs2326MSTI7TopologyChangeCount,
       "gs2326MSTI7TopologyChangeLast": gs2326MSTI7TopologyChangeLast,
       "gs2326MSTI7PortStateTable": gs2326MSTI7PortStateTable,
       "gs2326MSTI7PortStateEntry": gs2326MSTI7PortStateEntry,
       "gs2326MSTI7PortStateIndex": gs2326MSTI7PortStateIndex,
       "gs2326MSTI7PortStatePort": gs2326MSTI7PortStatePort,
       "gs2326MSTI7PortStatePortID": gs2326MSTI7PortStatePortID,
       "gs2326MSTI7PortStateRole": gs2326MSTI7PortStateRole,
       "gs2326MSTI7PortStateState": gs2326MSTI7PortStateState,
       "gs2326MSTI7PortStatePathCost": gs2326MSTI7PortStatePathCost,
       "gs2326MSTI7PortStateEdge": gs2326MSTI7PortStateEdge,
       "gs2326MSTI7PortStatePoint2Point": gs2326MSTI7PortStatePoint2Point,
       "gs2326MSTI7PortStateUptime": gs2326MSTI7PortStateUptime,
       "gs2326STPPortStatusTable": gs2326STPPortStatusTable,
       "gs2326STPPortStatusEntry": gs2326STPPortStatusEntry,
       "gs2326STPPortStatusPort": gs2326STPPortStatusPort,
       "gs2326STPPortStatusCISTRole": gs2326STPPortStatusCISTRole,
       "gs2326STPPortStatusCISTState": gs2326STPPortStatusCISTState,
       "gs2326STPPortStatusUptime": gs2326STPPortStatusUptime,
       "gs2326STPPortStatisticsTable": gs2326STPPortStatisticsTable,
       "gs2326STPPortStatisticsEntry": gs2326STPPortStatisticsEntry,
       "gs2326STPStatisticsIndex": gs2326STPStatisticsIndex,
       "gs2326STPStatisticsPort": gs2326STPStatisticsPort,
       "gs2326STPStatisticsTxMSTP": gs2326STPStatisticsTxMSTP,
       "gs2326STPStatisticsTxRSTP": gs2326STPStatisticsTxRSTP,
       "gs2326STPStatisticsTxSTP": gs2326STPStatisticsTxSTP,
       "gs2326STPStatisticsTxTCN": gs2326STPStatisticsTxTCN,
       "gs2326STPStatisticsRxMSTP": gs2326STPStatisticsRxMSTP,
       "gs2326STPStatisticsRxRSTP": gs2326STPStatisticsRxRSTP,
       "gs2326STPStatisticsRxSTP": gs2326STPStatisticsRxSTP,
       "gs2326STPStatisticsRxTCN": gs2326STPStatisticsRxTCN,
       "gs2326STPStatisticsDiscardedUnknown": gs2326STPStatisticsDiscardedUnknown,
       "gs2326STPStatisticsDiscardedIllegal": gs2326STPStatisticsDiscardedIllegal,
       "gs2326FilteringDataBase": gs2326FilteringDataBase,
       "gs2326FilteringDataBaseConfig": gs2326FilteringDataBaseConfig,
       "gs2326FilteringDataBaseAgingTime": gs2326FilteringDataBaseAgingTime,
       "gs2326FilteringDataBaseConfigTable": gs2326FilteringDataBaseConfigTable,
       "gs2326FilteringDataBaseConfigEntry": gs2326FilteringDataBaseConfigEntry,
       "gs2326FilteringDataBaseConfigPort": gs2326FilteringDataBaseConfigPort,
       "gs2326FilteringDataBaseConfigLearning": gs2326FilteringDataBaseConfigLearning,
       "gs2326FilteringDataBaseStaticMAC": gs2326FilteringDataBaseStaticMAC,
       "gs2326FilteringDataBaseStaticMACCreate": gs2326FilteringDataBaseStaticMACCreate,
       "gs2326FilteringDataBaseStaticMACTable": gs2326FilteringDataBaseStaticMACTable,
       "gs2326FilteringDataBaseStaticMACEntry": gs2326FilteringDataBaseStaticMACEntry,
       "gs2326FilteringDataBaseStaticMACIndex": gs2326FilteringDataBaseStaticMACIndex,
       "gs2326FilteringDataBaseStaticMACVLANId": gs2326FilteringDataBaseStaticMACVLANId,
       "gs2326FilteringDataBaseStaticMACAddress": gs2326FilteringDataBaseStaticMACAddress,
       "gs2326FilteringDataBaseStaticMACPortMembers": gs2326FilteringDataBaseStaticMACPortMembers,
       "gs2326FilteringDataBaseStaticMACRowStatus": gs2326FilteringDataBaseStaticMACRowStatus,
       "gs2326FilteringDataBaseDynamicMACTable": gs2326FilteringDataBaseDynamicMACTable,
       "gs2326FilteringDataBaseDynamicMACEntry": gs2326FilteringDataBaseDynamicMACEntry,
       "gs2326FilteringDataBaseDynamicMACIndex": gs2326FilteringDataBaseDynamicMACIndex,
       "gs2326FilteringDataBaseDynamicMACType": gs2326FilteringDataBaseDynamicMACType,
       "gs2326FilteringDataBaseDynamicMACVLAN": gs2326FilteringDataBaseDynamicMACVLAN,
       "gs2326FilteringDataBaseDynamicMACAddress": gs2326FilteringDataBaseDynamicMACAddress,
       "gs2326FilteringDataBaseDynamicPortMembers": gs2326FilteringDataBaseDynamicPortMembers,
       "gs2326SFlowAgent": gs2326SFlowAgent,
       "gs2326SFlowAgentCollector": gs2326SFlowAgentCollector,
       "gs2326SFlowAgentReceiverMode": gs2326SFlowAgentReceiverMode,
       "gs2326LMC": gs2326LMC,
       "gs2326LMCOperating": gs2326LMCOperating,
       "gs2326LMCConfigViaDhcp": gs2326LMCConfigViaDhcp,
       "gs2326LMCDomain": gs2326LMCDomain,
       "gs2326LMCDhcpClientAutoRenew": gs2326LMCDhcpClientAutoRenew,
       "gs2326LMCZeroTouchSupport": gs2326LMCZeroTouchSupport,
       "gs2326LMCPairingTokenPresent": gs2326LMCPairingTokenPresent,
       "gs2326LMCClientStatus": gs2326LMCClientStatus,
       "gs2326LMCManagementStatus": gs2326LMCManagementStatus,
       "gs2326LMCControlStatus": gs2326LMCControlStatus,
       "gs2326LMCMonitoringStatus": gs2326LMCMonitoringStatus,
       "gs2326LMCConfigurationSource": gs2326LMCConfigurationSource,
       "gs2326LMCConfigModified": gs2326LMCConfigModified,
       "gs2326LMCDeviceID": gs2326LMCDeviceID,
       "gs2326LMCRoundTripTime": gs2326LMCRoundTripTime,
       "gs2326Security": gs2326Security,
       "gs2326IPSourceGuard": gs2326IPSourceGuard,
       "gs2326IPSourceGuardConf": gs2326IPSourceGuardConf,
       "gs2326IPSourceGuardMode": gs2326IPSourceGuardMode,
       "gs2326IPSourceGuardPortConfigTable": gs2326IPSourceGuardPortConfigTable,
       "gs2326IPSourceGuardPortConfigEntry": gs2326IPSourceGuardPortConfigEntry,
       "gs2326IPSourceGuardPortConfigPort": gs2326IPSourceGuardPortConfigPort,
       "gs2326IPSourceGuardPortConfigMode": gs2326IPSourceGuardPortConfigMode,
       "gs2326IPSourceGuardPortMaxDynamicClients": gs2326IPSourceGuardPortMaxDynamicClients,
       "gs2326IPSourceGuardStatic": gs2326IPSourceGuardStatic,
       "gs2326IPSourceGuardStaticCreate": gs2326IPSourceGuardStaticCreate,
       "gs2326IPSourceGuardStaticTable": gs2326IPSourceGuardStaticTable,
       "gs2326IPSourceGuardStaticEntry": gs2326IPSourceGuardStaticEntry,
       "gs2326IPSourceGuardStaticIndex": gs2326IPSourceGuardStaticIndex,
       "gs2326IPSourceGuardStaticPort": gs2326IPSourceGuardStaticPort,
       "gs2326IPSourceGuardStaticVLANId": gs2326IPSourceGuardStaticVLANId,
       "gs2326IPSourceGuardStaticIPAddress": gs2326IPSourceGuardStaticIPAddress,
       "gs2326IPSourceGuardStaticMACAddress": gs2326IPSourceGuardStaticMACAddress,
       "gs2326IPSourceGuardStaticRowStatus": gs2326IPSourceGuardStaticRowStatus,
       "gs2326IPSourceGuardDynamicTable": gs2326IPSourceGuardDynamicTable,
       "gs2326IPSourceGuardDynamicEntry": gs2326IPSourceGuardDynamicEntry,
       "gs2326IPSourceGuardDynamicIndex": gs2326IPSourceGuardDynamicIndex,
       "gs2326IPSourceGuardDynamicPort": gs2326IPSourceGuardDynamicPort,
       "gs2326IPSourceGuardDynamicVLANId": gs2326IPSourceGuardDynamicVLANId,
       "gs2326IPSourceGuardDynamicIPAddress": gs2326IPSourceGuardDynamicIPAddress,
       "gs2326IPSourceGuardDynamicMACAddress": gs2326IPSourceGuardDynamicMACAddress,
       "gs2326ARPInspection": gs2326ARPInspection,
       "gs2326ARPInspectionConf": gs2326ARPInspectionConf,
       "gs2326ARPInspectionConfMode": gs2326ARPInspectionConfMode,
       "gs2326ARPInspectionConfTable": gs2326ARPInspectionConfTable,
       "gs2326ARPInspectionConfEntry": gs2326ARPInspectionConfEntry,
       "gs2326ARPInspectionConfPortIndex": gs2326ARPInspectionConfPortIndex,
       "gs2326ARPInspectionConfPortMode": gs2326ARPInspectionConfPortMode,
       "gs2326ARPInspectionStatic": gs2326ARPInspectionStatic,
       "gs2326ARPInspectionStaticCreate": gs2326ARPInspectionStaticCreate,
       "gs2326ARPInspectionStaticTable": gs2326ARPInspectionStaticTable,
       "gs2326ARPInspectionStaticEntry": gs2326ARPInspectionStaticEntry,
       "gs2326ARPInspectionStaticIndex": gs2326ARPInspectionStaticIndex,
       "gs2326ARPInspectionStaticPort": gs2326ARPInspectionStaticPort,
       "gs2326ARPInspectionStaticVLANId": gs2326ARPInspectionStaticVLANId,
       "gs2326ARPInspectionStaticIPAddress": gs2326ARPInspectionStaticIPAddress,
       "gs2326ARPInspectionStaticMACAddress": gs2326ARPInspectionStaticMACAddress,
       "gs2326ARPInspectionStaticRowStatus": gs2326ARPInspectionStaticRowStatus,
       "gs2326ARPInspectionDynamicTable": gs2326ARPInspectionDynamicTable,
       "gs2326ARPInspectionDynamicEntry": gs2326ARPInspectionDynamicEntry,
       "gs2326ARPInspectionDynamicIndex": gs2326ARPInspectionDynamicIndex,
       "gs2326ARPInspectionDynamicPort": gs2326ARPInspectionDynamicPort,
       "gs2326ARPInspectionDynamicVLANId": gs2326ARPInspectionDynamicVLANId,
       "gs2326ARPInspectionDynamicIPAddress": gs2326ARPInspectionDynamicIPAddress,
       "gs2326ARPInspectionDynamicMACAddress": gs2326ARPInspectionDynamicMACAddress,
       "gs2326ARPStaticGatewayCtrl": gs2326ARPStaticGatewayCtrl,
       "gs2326ARPStaticGatewayCtrlSystemConf": gs2326ARPStaticGatewayCtrlSystemConf,
       "gs2326ARPStaticGatewayCtrlMode": gs2326ARPStaticGatewayCtrlMode,
       "gs2326ARPStaticGatewayCtrlCreate": gs2326ARPStaticGatewayCtrlCreate,
       "gs2326ARPStaticGatewayCtrlTable": gs2326ARPStaticGatewayCtrlTable,
       "gs2326ARPStaticGatewayCtrlEntry": gs2326ARPStaticGatewayCtrlEntry,
       "gs2326ARPStaticGatewayCtrlIndex": gs2326ARPStaticGatewayCtrlIndex,
       "gs2326ARPStaticGatewayCtrlIPAddress": gs2326ARPStaticGatewayCtrlIPAddress,
       "gs2326ARPStaticGatewayCtrlMACAddress": gs2326ARPStaticGatewayCtrlMACAddress,
       "gs2326ARPStaticGatewayCtrlPort": gs2326ARPStaticGatewayCtrlPort,
       "gs2326ARPStaticGatewayCtrlAction": gs2326ARPStaticGatewayCtrlAction,
       "gs2326ARPStaticGatewayCtrlState": gs2326ARPStaticGatewayCtrlState,
       "gs2326ARPStaticGatewayCtrlReOpen": gs2326ARPStaticGatewayCtrlReOpen,
       "gs2326ARPStaticGatewayCtrlRowStatus": gs2326ARPStaticGatewayCtrlRowStatus,
       "gs2326ARPSpoofingPrevention": gs2326ARPSpoofingPrevention,
       "gs2326ARPSpoofingPreventionSystemConf": gs2326ARPSpoofingPreventionSystemConf,
       "gs2326ARPSpoofingPreventionMode": gs2326ARPSpoofingPreventionMode,
       "gs2326ARPSpoofingPreventionTable": gs2326ARPSpoofingPreventionTable,
       "gs2326ARPSpoofingPreventionEntry": gs2326ARPSpoofingPreventionEntry,
       "gs2326ARPSpoofingPreventionPort": gs2326ARPSpoofingPreventionPort,
       "gs2326ARPSpoofingPreventionPortMode": gs2326ARPSpoofingPreventionPortMode,
       "gs2326ARPSpoofingPreventionPortLimit": gs2326ARPSpoofingPreventionPortLimit,
       "gs2326ARPSpoofingPreventionPortAction": gs2326ARPSpoofingPreventionPortAction,
       "gs2326ARPSpoofingPreventionPortState": gs2326ARPSpoofingPreventionPortState,
       "gs2326ARPSpoofingPreventionPortReOpen": gs2326ARPSpoofingPreventionPortReOpen,
       "gs2326ARPIPDoSPrevention": gs2326ARPIPDoSPrevention,
       "gs2326ARPIPDoSPreventionTCPMode": gs2326ARPIPDoSPreventionTCPMode,
       "gs2326ARPIPDoSPreventionUDPMode": gs2326ARPIPDoSPreventionUDPMode,
       "gs2326ARPIPDoSPreventionICMPMode": gs2326ARPIPDoSPreventionICMPMode,
       "gs2326ARPIPDoSPreventionServerPort1": gs2326ARPIPDoSPreventionServerPort1,
       "gs2326ARPIPDoSPreventionServerPort2": gs2326ARPIPDoSPreventionServerPort2,
       "gs2326ARPIPDoSPreventionServerPort3": gs2326ARPIPDoSPreventionServerPort3,
       "gs2326ARPIPDoSPreventionServerPort4": gs2326ARPIPDoSPreventionServerPort4,
       "gs2326DHCPSnooping": gs2326DHCPSnooping,
       "gs2326DHCPSnoopingConf": gs2326DHCPSnoopingConf,
       "gs2326DHCPSnoopingMode": gs2326DHCPSnoopingMode,
       "gs2326DHCPSnoopingPortModeConfigurationTable": gs2326DHCPSnoopingPortModeConfigurationTable,
       "gs2326DHCPSnoopingPortModeConfigurationEntry": gs2326DHCPSnoopingPortModeConfigurationEntry,
       "gs2326DHCPSnoopingPortModeConfigurationPort": gs2326DHCPSnoopingPortModeConfigurationPort,
       "gs2326DHCPSnoopingPortModeConfigurationMode": gs2326DHCPSnoopingPortModeConfigurationMode,
       "gs2326DHCPSnoopingStatisticsTable": gs2326DHCPSnoopingStatisticsTable,
       "gs2326DHCPSnoopingStatisticsEntry": gs2326DHCPSnoopingStatisticsEntry,
       "gs2326DHCPSnoopingStatisticsPort": gs2326DHCPSnoopingStatisticsPort,
       "gs2326DHCPSnoopingStatisticsClear": gs2326DHCPSnoopingStatisticsClear,
       "gs2326DHCPSnoopingRxDiscover": gs2326DHCPSnoopingRxDiscover,
       "gs2326DHCPSnoopingRxOffer": gs2326DHCPSnoopingRxOffer,
       "gs2326DHCPSnoopingRxRequest": gs2326DHCPSnoopingRxRequest,
       "gs2326DHCPSnoopingRxDecline": gs2326DHCPSnoopingRxDecline,
       "gs2326DHCPSnoopingRxACK": gs2326DHCPSnoopingRxACK,
       "gs2326DHCPSnoopingRxNAK": gs2326DHCPSnoopingRxNAK,
       "gs2326DHCPSnoopingRxRelease": gs2326DHCPSnoopingRxRelease,
       "gs2326DHCPSnoopingRxInform": gs2326DHCPSnoopingRxInform,
       "gs2326DHCPSnoopingRxLeaseQuery": gs2326DHCPSnoopingRxLeaseQuery,
       "gs2326DHCPSnoopingRxLeaseUnassigned": gs2326DHCPSnoopingRxLeaseUnassigned,
       "gs2326DHCPSnoopingRxLeaseUnknown": gs2326DHCPSnoopingRxLeaseUnknown,
       "gs2326DHCPSnoopingRxLeaseActive": gs2326DHCPSnoopingRxLeaseActive,
       "gs2326DHCPSnoopingTxDiscover": gs2326DHCPSnoopingTxDiscover,
       "gs2326DHCPSnoopingTxOffer": gs2326DHCPSnoopingTxOffer,
       "gs2326DHCPSnoopingTxRequest": gs2326DHCPSnoopingTxRequest,
       "gs2326DHCPSnoopingTxDecline": gs2326DHCPSnoopingTxDecline,
       "gs2326DHCPSnoopingTxACK": gs2326DHCPSnoopingTxACK,
       "gs2326DHCPSnoopingTxNAK": gs2326DHCPSnoopingTxNAK,
       "gs2326DHCPSnoopingTxRelease": gs2326DHCPSnoopingTxRelease,
       "gs2326DHCPSnoopingTxInform": gs2326DHCPSnoopingTxInform,
       "gs2326DHCPSnoopingTxLeaseQuery": gs2326DHCPSnoopingTxLeaseQuery,
       "gs2326DHCPSnoopingTxLeaseUnassigned": gs2326DHCPSnoopingTxLeaseUnassigned,
       "gs2326DHCPSnoopingTxLeaseUnknown": gs2326DHCPSnoopingTxLeaseUnknown,
       "gs2326DHCPSnoopingTxLeaseActive": gs2326DHCPSnoopingTxLeaseActive,
       "gs2326DHCPRelay": gs2326DHCPRelay,
       "gs2326DHCPRelayConfiguration": gs2326DHCPRelayConfiguration,
       "gs2326DHCPRelayMode": gs2326DHCPRelayMode,
       "gs2326DHCPRelayServer": gs2326DHCPRelayServer,
       "gs2326DHCPRelayInformationMode": gs2326DHCPRelayInformationMode,
       "gs2326DHCPRelayInformationPolicy": gs2326DHCPRelayInformationPolicy,
       "gs2326DHCPRelayConfigurationGateways": gs2326DHCPRelayConfigurationGateways,
       "gs2326DHCPRelayConfigurationGatewaysCreate": gs2326DHCPRelayConfigurationGatewaysCreate,
       "gs2326DHCPRelayConfigurationGatewaysTable": gs2326DHCPRelayConfigurationGatewaysTable,
       "gs2326DHCPRelayConfigurationGatewaysEntry": gs2326DHCPRelayConfigurationGatewaysEntry,
       "gs2326DHCPRelayConfigurationGatewaysIndex": gs2326DHCPRelayConfigurationGatewaysIndex,
       "gs2326DHCPRelayConfigurationGatewaysVLANId": gs2326DHCPRelayConfigurationGatewaysVLANId,
       "gs2326DHCPRelayConfigurationGatewaysIP": gs2326DHCPRelayConfigurationGatewaysIP,
       "gs2326DHCPRelayConfigurationGatewaysRowStatus": gs2326DHCPRelayConfigurationGatewaysRowStatus,
       "gs2326DHCPRelayInformationCustom": gs2326DHCPRelayInformationCustom,
       "gs2326DHCPRelayStatistics": gs2326DHCPRelayStatistics,
       "gs2326DHCPRelayServerStatistics": gs2326DHCPRelayServerStatistics,
       "gs2326ServerStatTransmitToServer": gs2326ServerStatTransmitToServer,
       "gs2326ServerStatTransmitError": gs2326ServerStatTransmitError,
       "gs2326ServerStatReceiveFromServer": gs2326ServerStatReceiveFromServer,
       "gs2326ServerStatReceiveMissingAgentOption": gs2326ServerStatReceiveMissingAgentOption,
       "gs2326ServerStatReceiveMissingCircuitID": gs2326ServerStatReceiveMissingCircuitID,
       "gs2326ServerStatReceiveMissingRemoteID": gs2326ServerStatReceiveMissingRemoteID,
       "gs2326ServerStatReceiveBadCircuitID": gs2326ServerStatReceiveBadCircuitID,
       "gs2326ServerStatReceiveBadRemoteID": gs2326ServerStatReceiveBadRemoteID,
       "gs2326DHCPRelayClientStatistics": gs2326DHCPRelayClientStatistics,
       "gs2326ClientStatTransmitToClient": gs2326ClientStatTransmitToClient,
       "gs2326ClientStatTransmitError": gs2326ClientStatTransmitError,
       "gs2326ClientStatReceivefromClient": gs2326ClientStatReceivefromClient,
       "gs2326ClientStatReceiveAgentOption": gs2326ClientStatReceiveAgentOption,
       "gs2326ClientStatReplaceAgentOption": gs2326ClientStatReplaceAgentOption,
       "gs2326ClientStatKeepAgentOption": gs2326ClientStatKeepAgentOption,
       "gs2326ClientStatDropAgentOption": gs2326ClientStatDropAgentOption,
       "gs2326PortSecurity": gs2326PortSecurity,
       "gs2326PortSecLimitCtrl": gs2326PortSecLimitCtrl,
       "gs2326PortSecLimitCtrlSystemConf": gs2326PortSecLimitCtrlSystemConf,
       "gs2326PortSecurityMode": gs2326PortSecurityMode,
       "gs2326PortSecurityAging": gs2326PortSecurityAging,
       "gs2326PortSecurityAgingPeriod": gs2326PortSecurityAgingPeriod,
       "gs2326PortSecLimitCtrlTable": gs2326PortSecLimitCtrlTable,
       "gs2326PortSecLimitCtrlEntry": gs2326PortSecLimitCtrlEntry,
       "gs2326PortSecLimitCtrlPort": gs2326PortSecLimitCtrlPort,
       "gs2326PortSecLimitCtrlPortMode": gs2326PortSecLimitCtrlPortMode,
       "gs2326PortSecLimitCtrlPortLimit": gs2326PortSecLimitCtrlPortLimit,
       "gs2326PortSecLimitCtrlPortAction": gs2326PortSecLimitCtrlPortAction,
       "gs2326PortSecLimitCtrlPortState": gs2326PortSecLimitCtrlPortState,
       "gs2326PortSecLimitCtrlPortReOpen": gs2326PortSecLimitCtrlPortReOpen,
       "gs2326PortSecSwitchStatusTable": gs2326PortSecSwitchStatusTable,
       "gs2326PortSecSwitchStatusEntry": gs2326PortSecSwitchStatusEntry,
       "gs2326PortSecSwitchStatusPort": gs2326PortSecSwitchStatusPort,
       "gs2326PortSecSwitchStatusUsers": gs2326PortSecSwitchStatusUsers,
       "gs2326PortSecSwitchStatusState": gs2326PortSecSwitchStatusState,
       "gs2326PortSecSwitchStatusMACCountCurrent": gs2326PortSecSwitchStatusMACCountCurrent,
       "gs2326PortSecSwitchStatusMACCountLimit": gs2326PortSecSwitchStatusMACCountLimit,
       "gs2326PortSecPortStatus": gs2326PortSecPortStatus,
       "gs2326PortSecPortStatusPort": gs2326PortSecPortStatusPort,
       "gs2326PortSecPortStatusTable": gs2326PortSecPortStatusTable,
       "gs2326PortSecPortStatusEntry": gs2326PortSecPortStatusEntry,
       "gs2326PortSecPortStatusIndex": gs2326PortSecPortStatusIndex,
       "gs2326PortSecPortStatusMACAddress": gs2326PortSecPortStatusMACAddress,
       "gs2326PortSecPortStatusVLANId": gs2326PortSecPortStatusVLANId,
       "gs2326PortSecPortStatusState": gs2326PortSecPortStatusState,
       "gs2326PortSecPortStatusTimeOfAddition": gs2326PortSecPortStatusTimeOfAddition,
       "gs2326PortSecPortStatusAgeAndHold": gs2326PortSecPortStatusAgeAndHold,
       "gs2326AccessManagement": gs2326AccessManagement,
       "gs2326AccessMgtConf": gs2326AccessMgtConf,
       "gs2326AccessMgtConfMode": gs2326AccessMgtConfMode,
       "gs2326AccessMgtConfCreate": gs2326AccessMgtConfCreate,
       "gs2326AccessMgtConfTable": gs2326AccessMgtConfTable,
       "gs2326AccessMgtConfEntry": gs2326AccessMgtConfEntry,
       "gs2326AccessMgtIndex": gs2326AccessMgtIndex,
       "gs2326AccessMgtAddresstype": gs2326AccessMgtAddresstype,
       "gs2326AccessMgtStartIpAddress": gs2326AccessMgtStartIpAddress,
       "gs2326AccessMgtEndIpAddress": gs2326AccessMgtEndIpAddress,
       "gs2326AccessMgtHttpHttps": gs2326AccessMgtHttpHttps,
       "gs2326AccessMgtSNMP": gs2326AccessMgtSNMP,
       "gs2326AccessMgtTelnetSSH": gs2326AccessMgtTelnetSSH,
       "gs2326AccessMgtRowStatus": gs2326AccessMgtRowStatus,
       "gs2326AccessMgtStatistics": gs2326AccessMgtStatistics,
       "gs2326HttpReceivedPkts": gs2326HttpReceivedPkts,
       "gs2326HttpAllowedPkts": gs2326HttpAllowedPkts,
       "gs2326HttpDiscardedPkts": gs2326HttpDiscardedPkts,
       "gs2326HttpsReceivedPkts": gs2326HttpsReceivedPkts,
       "gs2326HttpsAllowedPkts": gs2326HttpsAllowedPkts,
       "gs2326HttpsDiscardedPkts": gs2326HttpsDiscardedPkts,
       "gs2326SnmpReceivedPkts": gs2326SnmpReceivedPkts,
       "gs2326SnmpAllowedPkts": gs2326SnmpAllowedPkts,
       "gs2326SnmpDiscardedPkts": gs2326SnmpDiscardedPkts,
       "gs2326TelnetReceivedPkts": gs2326TelnetReceivedPkts,
       "gs2326TelnetAllowedPkts": gs2326TelnetAllowedPkts,
       "gs2326TelnetDiscardedPkts": gs2326TelnetDiscardedPkts,
       "gs2326SSHReceivedPkts": gs2326SSHReceivedPkts,
       "gs2326SSHAllowedPkts": gs2326SSHAllowedPkts,
       "gs2326SSHDiscardedPkts": gs2326SSHDiscardedPkts,
       "gs2326AccessMgtStatisticsClearAll": gs2326AccessMgtStatisticsClearAll,
       "gs2326SSH": gs2326SSH,
       "gs2326SSHMode": gs2326SSHMode,
       "gs2326HTTPS": gs2326HTTPS,
       "gs2326HTTPSMode": gs2326HTTPSMode,
       "gs2326HTTPSAutoRedirect": gs2326HTTPSAutoRedirect,
       "gs2326HTTPSCertRenew": gs2326HTTPSCertRenew,
       "gs2326HTTPSMinProtoVersion": gs2326HTTPSMinProtoVersion,
       "gs2326HTTPMode": gs2326HTTPMode,
       "gs2326AuthMethod": gs2326AuthMethod,
       "gs2326ConsoleAuthMethod": gs2326ConsoleAuthMethod,
       "gs2326ConsoleFallback": gs2326ConsoleFallback,
       "gs2326TelnetAuthMethod": gs2326TelnetAuthMethod,
       "gs2326TelnetFallback": gs2326TelnetFallback,
       "gs2326SshAuthMethod": gs2326SshAuthMethod,
       "gs2326SshFallback": gs2326SshFallback,
       "gs2326TftpAuthMethod": gs2326TftpAuthMethod,
       "gs2326TftpFallback": gs2326TftpFallback,
       "gs2326LoginFailures": gs2326LoginFailures,
       "gs2326LockMinutes": gs2326LockMinutes,
       "gs2326HttpAuthMethod": gs2326HttpAuthMethod,
       "gs2326HttpFallback": gs2326HttpFallback,
       "gs2326HttpsAuthMethod": gs2326HttpsAuthMethod,
       "gs2326HttpsFallback": gs2326HttpsFallback,
       "gs2326AAA": gs2326AAA,
       "gs2326AAACommonServer": gs2326AAACommonServer,
       "gs2326AAACommonServerTimeout": gs2326AAACommonServerTimeout,
       "gs2326AAACommonServerDeadTime": gs2326AAACommonServerDeadTime,
       "gs2326AAATACACSPlusAuthAndAccounting": gs2326AAATACACSPlusAuthAndAccounting,
       "gs2326AAAAuthorization": gs2326AAAAuthorization,
       "gs2326AAAFallbackToLocalAuthorization": gs2326AAAFallbackToLocalAuthorization,
       "gs2326AAAAccounting": gs2326AAAAccounting,
       "gs2326RADIUSAuthenticationServerTable": gs2326RADIUSAuthenticationServerTable,
       "gs2326RADIUSAuthenticationServerEntry": gs2326RADIUSAuthenticationServerEntry,
       "gs2326RADIUSAuthenticationServerIndex": gs2326RADIUSAuthenticationServerIndex,
       "gs2326RADIUSAuthenticationServerEnable": gs2326RADIUSAuthenticationServerEnable,
       "gs2326RADIUSAuthenticationServerIP": gs2326RADIUSAuthenticationServerIP,
       "gs2326RADIUSAuthenticationServerPort": gs2326RADIUSAuthenticationServerPort,
       "gs2326RADIUSAuthenticationServerSecret": gs2326RADIUSAuthenticationServerSecret,
       "gs2326RADIUSAccountingServerTable": gs2326RADIUSAccountingServerTable,
       "gs2326RADIUSAccountingServerEntry": gs2326RADIUSAccountingServerEntry,
       "gs2326RADIUSAccountingServerIndex": gs2326RADIUSAccountingServerIndex,
       "gs2326RADIUSAccountingServerEnable": gs2326RADIUSAccountingServerEnable,
       "gs2326RADIUSAccountingServerIP": gs2326RADIUSAccountingServerIP,
       "gs2326RADIUSAccountingServerPort": gs2326RADIUSAccountingServerPort,
       "gs2326RADIUSAccountingServerSecret": gs2326RADIUSAccountingServerSecret,
       "gs2326TACACSPlusAuthenticationServerTable": gs2326TACACSPlusAuthenticationServerTable,
       "gs2326TACACSPlusAuthenticationServerEntry": gs2326TACACSPlusAuthenticationServerEntry,
       "gs2326TACACSPlusAuthenticationServerIndex": gs2326TACACSPlusAuthenticationServerIndex,
       "gs2326TACACSPlusAuthenticationServerEnable": gs2326TACACSPlusAuthenticationServerEnable,
       "gs2326TACACSPlusAuthenticationServerIP": gs2326TACACSPlusAuthenticationServerIP,
       "gs2326TACACSPlusAuthenticationServerPort": gs2326TACACSPlusAuthenticationServerPort,
       "gs2326TACACSPlusAuthenticationServerSecret": gs2326TACACSPlusAuthenticationServerSecret,
       "gs2326RADIUSStatisticsTable": gs2326RADIUSStatisticsTable,
       "gs2326RADIUSStatisticsEntry": gs2326RADIUSStatisticsEntry,
       "gs2326RADIUSAuthStatisticsServerIndex": gs2326RADIUSAuthStatisticsServerIndex,
       "gs2326RADIUSAuthStatisticsRecPktAccessAccepts": gs2326RADIUSAuthStatisticsRecPktAccessAccepts,
       "gs2326RADIUSAuthStatisticsRecPktAccessRejects": gs2326RADIUSAuthStatisticsRecPktAccessRejects,
       "gs2326RADIUSAuthStatisticsRecPktAccessChallenges": gs2326RADIUSAuthStatisticsRecPktAccessChallenges,
       "gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses": gs2326RADIUSAuthStatisticsRecPktMalformedAccResponses,
       "gs2326RADIUSAuthStatisticsRecPktBadAuthenticators": gs2326RADIUSAuthStatisticsRecPktBadAuthenticators,
       "gs2326RADIUSAuthStatisticsRecPktUnknownTypes": gs2326RADIUSAuthStatisticsRecPktUnknownTypes,
       "gs2326RADIUSAuthStatisticsRecPktDropped": gs2326RADIUSAuthStatisticsRecPktDropped,
       "gs2326RADIUSAuthStatisticsTransmitPktAccessRequests": gs2326RADIUSAuthStatisticsTransmitPktAccessRequests,
       "gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions": gs2326RADIUSAuthStatisticsTransmitPktAccessRetransmissions,
       "gs2326RADIUSAuthStatisticsTransmitPktPendingRequests": gs2326RADIUSAuthStatisticsTransmitPktPendingRequests,
       "gs2326RADIUSAuthStatisticsTransmitPktTimeouts": gs2326RADIUSAuthStatisticsTransmitPktTimeouts,
       "gs2326RADIUSAuthIP": gs2326RADIUSAuthIP,
       "gs2326RADIUSAuthState": gs2326RADIUSAuthState,
       "gs2326RADIUSAuthRoundTripTime": gs2326RADIUSAuthRoundTripTime,
       "gs2326RADIUSAccountingStatisticsRecPktResponses": gs2326RADIUSAccountingStatisticsRecPktResponses,
       "gs2326RADIUSAccountingStatisticsRecPktMalformedResponses": gs2326RADIUSAccountingStatisticsRecPktMalformedResponses,
       "gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators": gs2326RADIUSAccountingStatisticsRecPktBadAuthenticators,
       "gs2326RADIUSAccountingStatisticsRecPktUnknownTypes": gs2326RADIUSAccountingStatisticsRecPktUnknownTypes,
       "gs2326RADIUSAccountingStatisticsRecPktDropped": gs2326RADIUSAccountingStatisticsRecPktDropped,
       "gs2326RADIUSAccountingStatisticsTransmitPktRequests": gs2326RADIUSAccountingStatisticsTransmitPktRequests,
       "gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions": gs2326RADIUSAccountingStatisticsTransmitPktRetransmissions,
       "gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests": gs2326RADIUSAccountingStatisticsTransmitPktPendingRequests,
       "gs2326RADIUSAccountingStatisticsTransmitPktTimeouts": gs2326RADIUSAccountingStatisticsTransmitPktTimeouts,
       "gs2326RADIUSAccountingIP": gs2326RADIUSAccountingIP,
       "gs2326RADIUSAccountingState": gs2326RADIUSAccountingState,
       "gs2326RADIUSAccountingRoundTripTime": gs2326RADIUSAccountingRoundTripTime,
       "gs2326RADIUSStatisticsClear": gs2326RADIUSStatisticsClear,
       "gs2326NAS": gs2326NAS,
       "gs2326NASConfiguration": gs2326NASConfiguration,
       "gs2326NASConfigMode": gs2326NASConfigMode,
       "gs2326NASConfigReauthEnabled": gs2326NASConfigReauthEnabled,
       "gs2326NASConfigReauthPeriod": gs2326NASConfigReauthPeriod,
       "gs2326NASConfigEAPOLTimeout": gs2326NASConfigEAPOLTimeout,
       "gs2326NASConfigAgingPeriod": gs2326NASConfigAgingPeriod,
       "gs2326NASConfigHoldTime": gs2326NASConfigHoldTime,
       "gs2326NASConfigRADIUSAssignedQoSEnabled": gs2326NASConfigRADIUSAssignedQoSEnabled,
       "gs2326NASConfigRADIUSAssignedVLANEnabled": gs2326NASConfigRADIUSAssignedVLANEnabled,
       "gs2326NASConfigGuestVLANEnabled": gs2326NASConfigGuestVLANEnabled,
       "gs2326NASConfigGuestVLANID": gs2326NASConfigGuestVLANID,
       "gs2326NASConfigMaxReauthCount": gs2326NASConfigMaxReauthCount,
       "gs2326NASConfigAllowGuestVLANEAPOLSeen": gs2326NASConfigAllowGuestVLANEAPOLSeen,
       "gs2326NASPortConfigTable": gs2326NASPortConfigTable,
       "gs2326NASPortConfigEntry": gs2326NASPortConfigEntry,
       "gs2326NASPortConfigPort": gs2326NASPortConfigPort,
       "gs2326NASPortConfigAdminState": gs2326NASPortConfigAdminState,
       "gs2326NASPortConfigRADIUSAssignedQoSEnabled": gs2326NASPortConfigRADIUSAssignedQoSEnabled,
       "gs2326NASPortConfigRADIUSAssignedVLANEnabled": gs2326NASPortConfigRADIUSAssignedVLANEnabled,
       "gs2326NASPortConfigGuestVLANEnabled": gs2326NASPortConfigGuestVLANEnabled,
       "gs2326NASPortConfigPortState": gs2326NASPortConfigPortState,
       "gs2326NASPortConfigReauthenticate": gs2326NASPortConfigReauthenticate,
       "gs2326NASPortConfigReinitialize": gs2326NASPortConfigReinitialize,
       "gs2326NASPortConfigFallbackEnabled": gs2326NASPortConfigFallbackEnabled,
       "gs2326NASConfigMacBasedUseEAP": gs2326NASConfigMacBasedUseEAP,
       "gs2326NASSwitchStatusTable": gs2326NASSwitchStatusTable,
       "gs2326NASSwitchStatusEntry": gs2326NASSwitchStatusEntry,
       "gs2326NASSwitchStatusAdminState": gs2326NASSwitchStatusAdminState,
       "gs2326NASSwitchStatusPortState": gs2326NASSwitchStatusPortState,
       "gs2326NASSwitchStatusLastSource": gs2326NASSwitchStatusLastSource,
       "gs2326NASSwitchStatusLastID": gs2326NASSwitchStatusLastID,
       "gs2326NASSwitchStatusQoSClass": gs2326NASSwitchStatusQoSClass,
       "gs2326NASSwitchStatusPortVlanID": gs2326NASSwitchStatusPortVlanID,
       "gs2326NASPortStatus": gs2326NASPortStatus,
       "gs2326NASPortStatusCountersTable": gs2326NASPortStatusCountersTable,
       "gs2326NASPortStatusCountersEntry": gs2326NASPortStatusCountersEntry,
       "gs2326NASRxCountersEAPOLTotal": gs2326NASRxCountersEAPOLTotal,
       "gs2326NASRxCountersEAPOLResponseID": gs2326NASRxCountersEAPOLResponseID,
       "gs2326NASRxCountersEAPOLResponses": gs2326NASRxCountersEAPOLResponses,
       "gs2326NASRxCountersEAPOLStart": gs2326NASRxCountersEAPOLStart,
       "gs2326NASRxCountersEAPOLLogoff": gs2326NASRxCountersEAPOLLogoff,
       "gs2326NASRxCountersEAPOLInvalidType": gs2326NASRxCountersEAPOLInvalidType,
       "gs2326NASRxCountersEAPOLInvalidLength": gs2326NASRxCountersEAPOLInvalidLength,
       "gs2326NASTxCountersEAPOLTotal": gs2326NASTxCountersEAPOLTotal,
       "gs2326NASTxCountersEAPOLRequestID": gs2326NASTxCountersEAPOLRequestID,
       "gs2326NASTxCountersEAPOLRequests": gs2326NASTxCountersEAPOLRequests,
       "gs2326NASRxBackendServerCountersAccessChallenges": gs2326NASRxBackendServerCountersAccessChallenges,
       "gs2326NASRxBackendServerCountersOtherRequests": gs2326NASRxBackendServerCountersOtherRequests,
       "gs2326NASRxBackendServerCountersAuthSuccesses": gs2326NASRxBackendServerCountersAuthSuccesses,
       "gs2326NASRxBackendServerCountersAuthFailures": gs2326NASRxBackendServerCountersAuthFailures,
       "gs2326NASTxBackendServerCountersResponses": gs2326NASTxBackendServerCountersResponses,
       "gs2326NASLastSupplicantInfoMACAddress": gs2326NASLastSupplicantInfoMACAddress,
       "gs2326NASLastSupplicantInfoVlanID": gs2326NASLastSupplicantInfoVlanID,
       "gs2326NASLastSupplicantInfoVersion": gs2326NASLastSupplicantInfoVersion,
       "gs2326NASLastSupplicantInfoIdentity": gs2326NASLastSupplicantInfoIdentity,
       "gs2326NASCountersDoClear": gs2326NASCountersDoClear,
       "gs2326NASPortStatusClientsTable": gs2326NASPortStatusClientsTable,
       "gs2326NASPortStatusClientsEntry": gs2326NASPortStatusClientsEntry,
       "gs2326NASClientsIndex": gs2326NASClientsIndex,
       "gs2326NASClientsIdentity": gs2326NASClientsIdentity,
       "gs2326NASClientsMACAddress": gs2326NASClientsMACAddress,
       "gs2326NASClientsVlanID": gs2326NASClientsVlanID,
       "gs2326NASClientsState": gs2326NASClientsState,
       "gs2326NASClientsLastAuth": gs2326NASClientsLastAuth,
       "gs2326NASRxClientsEAPOLTotal": gs2326NASRxClientsEAPOLTotal,
       "gs2326NASRxClientsEAPOLResponseID": gs2326NASRxClientsEAPOLResponseID,
       "gs2326NASRxClientsEAPOLResponses": gs2326NASRxClientsEAPOLResponses,
       "gs2326NASRxClientsEAPOLStart": gs2326NASRxClientsEAPOLStart,
       "gs2326NASRxClientsEAPOLLogoff": gs2326NASRxClientsEAPOLLogoff,
       "gs2326NASRxClientsEAPOLInvalidType": gs2326NASRxClientsEAPOLInvalidType,
       "gs2326NASRxClientsEAPOLInvalidLength": gs2326NASRxClientsEAPOLInvalidLength,
       "gs2326NASTxClientsEAPOLTotal": gs2326NASTxClientsEAPOLTotal,
       "gs2326NASTxClientsEAPOLRequestID": gs2326NASTxClientsEAPOLRequestID,
       "gs2326NASTxClientsEAPOLRequests": gs2326NASTxClientsEAPOLRequests,
       "gs2326NASRxBackendServerClientsAccessChallenges": gs2326NASRxBackendServerClientsAccessChallenges,
       "gs2326NASRxBackendServerClientsOtherRequests": gs2326NASRxBackendServerClientsOtherRequests,
       "gs2326NASRxBackendServerClientsAuthSuccesses": gs2326NASRxBackendServerClientsAuthSuccesses,
       "gs2326NASRxBackendServerClientsAuthFailures": gs2326NASRxBackendServerClientsAuthFailures,
       "gs2326NASTxBackendServerClientsResponses": gs2326NASTxBackendServerClientsResponses,
       "gs2326Maintenance": gs2326Maintenance,
       "gs2326RestartDevice": gs2326RestartDevice,
       "gs2326Firmware": gs2326Firmware,
       "gs2326FirmwareIpAddress": gs2326FirmwareIpAddress,
       "gs2326FirmwareFileName": gs2326FirmwareFileName,
       "gs2326DoFirmwareUpgrade": gs2326DoFirmwareUpgrade,
       "gs2326SaveOrRestore": gs2326SaveOrRestore,
       "gs2326FactoryDefaults": gs2326FactoryDefaults,
       "gs2326SaveStart": gs2326SaveStart,
       "gs2326SaveUser": gs2326SaveUser,
       "gs2326RestoreUser": gs2326RestoreUser,
       "gs2326ExportOrImport": gs2326ExportOrImport,
       "gs2326ExportIpAddress": gs2326ExportIpAddress,
       "gs2326ExportConfigName": gs2326ExportConfigName,
       "gs2326DoExportConfig": gs2326DoExportConfig,
       "gs2326ImportIpAddress": gs2326ImportIpAddress,
       "gs2326ImportConfigName": gs2326ImportConfigName,
       "gs2326DoImportConfig": gs2326DoImportConfig,
       "gs2326Diagnostics": gs2326Diagnostics,
       "gs2326PingIpAddress": gs2326PingIpAddress,
       "gs2326PingSize": gs2326PingSize,
       "gs2326DoPingConfig": gs2326DoPingConfig,
       "gs2326PingResult": gs2326PingResult,
       "gs2326Ping6IpAddress": gs2326Ping6IpAddress,
       "gs2326Ping6Size": gs2326Ping6Size,
       "gs2326DoPing6Config": gs2326DoPing6Config,
       "gs2326Ping6Result": gs2326Ping6Result,
       "gs2326VeriPHY": gs2326VeriPHY,
       "gs2326VeriPHYTest": gs2326VeriPHYTest,
       "gs2326VeriPHYTable": gs2326VeriPHYTable,
       "gs2326VeriPHYEntry": gs2326VeriPHYEntry,
       "gs2326VeriPHYPort": gs2326VeriPHYPort,
       "gs2326VeriPHYPairA": gs2326VeriPHYPairA,
       "gs2326VeriPHYLengthA": gs2326VeriPHYLengthA,
       "gs2326VeriPHYPairB": gs2326VeriPHYPairB,
       "gs2326VeriPHYLengthB": gs2326VeriPHYLengthB,
       "gs2326VeriPHYPairC": gs2326VeriPHYPairC,
       "gs2326VeriPHYLengthC": gs2326VeriPHYLengthC,
       "gs2326VeriPHYPairD": gs2326VeriPHYPairD,
       "gs2326VeriPHYLengthD": gs2326VeriPHYLengthD,
       "gs2326ColdRestartDevice": gs2326ColdRestartDevice,
       "gs2326Trap": gs2326Trap,
       "gs2326TrapEvent": gs2326TrapEvent,
       "gs2326Emergency": gs2326Emergency,
       "gs2326Alert": gs2326Alert,
       "gs2326Critical": gs2326Critical,
       "gs2326Error": gs2326Error,
       "gs2326Warning": gs2326Warning,
       "gs2326Notice": gs2326Notice,
       "gs2326Informational": gs2326Informational,
       "gs2326Debug": gs2326Debug,
       "gs2326TrapVariable": gs2326TrapVariable,
       "gs2326Information": gs2326Information}
)
