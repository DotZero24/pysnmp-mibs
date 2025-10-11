# SNMP MIB module (LANCOM-GS-2328F-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-GS-2328F-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:12 2025
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
_LancomGS2328F_ObjectIdentity = ObjectIdentity
lancomGS2328F = _LancomGS2328F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332)
)
_Gs2328fSystem_ObjectIdentity = ObjectIdentity
gs2328fSystem = _Gs2328fSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1)
)
_Gs2328fSystemInformation_ObjectIdentity = ObjectIdentity
gs2328fSystemInformation = _Gs2328fSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1)
)
_Gs2328fModelName_Type = DisplayString
_Gs2328fModelName_Object = MibScalar
gs2328fModelName = _Gs2328fModelName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 1),
    _Gs2328fModelName_Type()
)
gs2328fModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fModelName.setStatus("current")
_Gs2328fBIOSVersion_Type = DisplayString
_Gs2328fBIOSVersion_Object = MibScalar
gs2328fBIOSVersion = _Gs2328fBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 2),
    _Gs2328fBIOSVersion_Type()
)
gs2328fBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fBIOSVersion.setStatus("current")
_Gs2328fFirmwareVersion_Type = DisplayString
_Gs2328fFirmwareVersion_Object = MibScalar
gs2328fFirmwareVersion = _Gs2328fFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 3),
    _Gs2328fFirmwareVersion_Type()
)
gs2328fFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFirmwareVersion.setStatus("current")
_Gs2328fHardwareMechanicalVersion_Type = DisplayString
_Gs2328fHardwareMechanicalVersion_Object = MibScalar
gs2328fHardwareMechanicalVersion = _Gs2328fHardwareMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 4),
    _Gs2328fHardwareMechanicalVersion_Type()
)
gs2328fHardwareMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHardwareMechanicalVersion.setStatus("current")
_Gs2328fSerialNumber_Type = DisplayString
_Gs2328fSerialNumber_Object = MibScalar
gs2328fSerialNumber = _Gs2328fSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 5),
    _Gs2328fSerialNumber_Type()
)
gs2328fSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSerialNumber.setStatus("current")
_Gs2328fHostMACAddress_Type = MacAddress
_Gs2328fHostMACAddress_Object = MibScalar
gs2328fHostMACAddress = _Gs2328fHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 6),
    _Gs2328fHostMACAddress_Type()
)
gs2328fHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHostMACAddress.setStatus("current")
_Gs2328fConsoleBaudrate_Type = DisplayString
_Gs2328fConsoleBaudrate_Object = MibScalar
gs2328fConsoleBaudrate = _Gs2328fConsoleBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 7),
    _Gs2328fConsoleBaudrate_Type()
)
gs2328fConsoleBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fConsoleBaudrate.setStatus("current")
_Gs2328fRAMSize_Type = DisplayString
_Gs2328fRAMSize_Object = MibScalar
gs2328fRAMSize = _Gs2328fRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 8),
    _Gs2328fRAMSize_Type()
)
gs2328fRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRAMSize.setStatus("current")
_Gs2328fFlashSize_Type = DisplayString
_Gs2328fFlashSize_Object = MibScalar
gs2328fFlashSize = _Gs2328fFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 9),
    _Gs2328fFlashSize_Type()
)
gs2328fFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFlashSize.setStatus("current")
_Gs2328fBridgeFDBSize_Type = DisplayString
_Gs2328fBridgeFDBSize_Object = MibScalar
gs2328fBridgeFDBSize = _Gs2328fBridgeFDBSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 10),
    _Gs2328fBridgeFDBSize_Type()
)
gs2328fBridgeFDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fBridgeFDBSize.setStatus("current")
_Gs2328fTransmitQueue_Type = DisplayString
_Gs2328fTransmitQueue_Object = MibScalar
gs2328fTransmitQueue = _Gs2328fTransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 11),
    _Gs2328fTransmitQueue_Type()
)
gs2328fTransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fTransmitQueue.setStatus("current")
_Gs2328fMaximumFrameSize_Type = DisplayString
_Gs2328fMaximumFrameSize_Object = MibScalar
gs2328fMaximumFrameSize = _Gs2328fMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 12),
    _Gs2328fMaximumFrameSize_Type()
)
gs2328fMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMaximumFrameSize.setStatus("current")
_Gs2328fCPULoad_Type = DisplayString
_Gs2328fCPULoad_Object = MibScalar
gs2328fCPULoad = _Gs2328fCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 13),
    _Gs2328fCPULoad_Type()
)
gs2328fCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCPULoad.setStatus("current")
_Gs2328fFanSpeed_Type = DisplayString
_Gs2328fFanSpeed_Object = MibScalar
gs2328fFanSpeed = _Gs2328fFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 17),
    _Gs2328fFanSpeed_Type()
)
gs2328fFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFanSpeed.setStatus("current")
_Gs2328fACPower_Type = DisplayString
_Gs2328fACPower_Object = MibScalar
gs2328fACPower = _Gs2328fACPower_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 18),
    _Gs2328fACPower_Type()
)
gs2328fACPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACPower.setStatus("current")
_Gs2328fTemperature_Type = DisplayString
_Gs2328fTemperature_Object = MibScalar
gs2328fTemperature = _Gs2328fTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 19),
    _Gs2328fTemperature_Type()
)
gs2328fTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fTemperature.setStatus("current")
_Gs2328fDCPower_Type = DisplayString
_Gs2328fDCPower_Object = MibScalar
gs2328fDCPower = _Gs2328fDCPower_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 20),
    _Gs2328fDCPower_Type()
)
gs2328fDCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDCPower.setStatus("current")
_Gs2328fSystemDescription_Type = DisplayString
_Gs2328fSystemDescription_Object = MibScalar
gs2328fSystemDescription = _Gs2328fSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 21),
    _Gs2328fSystemDescription_Type()
)
gs2328fSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSystemDescription.setStatus("current")
_Gs2328fLocation_Type = DisplayString
_Gs2328fLocation_Object = MibScalar
gs2328fLocation = _Gs2328fLocation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 22),
    _Gs2328fLocation_Type()
)
gs2328fLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLocation.setStatus("current")
_Gs2328fContact_Type = DisplayString
_Gs2328fContact_Object = MibScalar
gs2328fContact = _Gs2328fContact_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 23),
    _Gs2328fContact_Type()
)
gs2328fContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fContact.setStatus("current")
_Gs2328fDeviceName_Type = DisplayString
_Gs2328fDeviceName_Object = MibScalar
gs2328fDeviceName = _Gs2328fDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 24),
    _Gs2328fDeviceName_Type()
)
gs2328fDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDeviceName.setStatus("current")
_Gs2328fSystemDate_Type = DisplayString
_Gs2328fSystemDate_Object = MibScalar
gs2328fSystemDate = _Gs2328fSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 25),
    _Gs2328fSystemDate_Type()
)
gs2328fSystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSystemDate.setStatus("current")
_Gs2328fSystemUptime_Type = DisplayString
_Gs2328fSystemUptime_Object = MibScalar
gs2328fSystemUptime = _Gs2328fSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 26),
    _Gs2328fSystemUptime_Type()
)
gs2328fSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSystemUptime.setStatus("current")
_Gs2328fSystemIPv4Address_Type = DisplayString
_Gs2328fSystemIPv4Address_Object = MibScalar
gs2328fSystemIPv4Address = _Gs2328fSystemIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 27),
    _Gs2328fSystemIPv4Address_Type()
)
gs2328fSystemIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSystemIPv4Address.setStatus("current")
_Gs2328fSystemIPv4SubnetMask_Type = DisplayString
_Gs2328fSystemIPv4SubnetMask_Object = MibScalar
gs2328fSystemIPv4SubnetMask = _Gs2328fSystemIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 28),
    _Gs2328fSystemIPv4SubnetMask_Type()
)
gs2328fSystemIPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSystemIPv4SubnetMask.setStatus("current")
_Gs2328fSystemIPv4Gateway_Type = DisplayString
_Gs2328fSystemIPv4Gateway_Object = MibScalar
gs2328fSystemIPv4Gateway = _Gs2328fSystemIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 29),
    _Gs2328fSystemIPv4Gateway_Type()
)
gs2328fSystemIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSystemIPv4Gateway.setStatus("current")
_Gs2328fIPv6LinkLocalAddress_Type = DisplayString
_Gs2328fIPv6LinkLocalAddress_Object = MibScalar
gs2328fIPv6LinkLocalAddress = _Gs2328fIPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 30),
    _Gs2328fIPv6LinkLocalAddress_Type()
)
gs2328fIPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv6LinkLocalAddress.setStatus("current")
_Gs2328fIPv6Address_Type = DisplayString
_Gs2328fIPv6Address_Object = MibScalar
gs2328fIPv6Address = _Gs2328fIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 31),
    _Gs2328fIPv6Address_Type()
)
gs2328fIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv6Address.setStatus("current")
_Gs2328fIPv6Prefix_Type = DisplayString
_Gs2328fIPv6Prefix_Object = MibScalar
gs2328fIPv6Prefix = _Gs2328fIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 32),
    _Gs2328fIPv6Prefix_Type()
)
gs2328fIPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv6Prefix.setStatus("current")
_Gs2328fIPv6Gateway_Type = DisplayString
_Gs2328fIPv6Gateway_Object = MibScalar
gs2328fIPv6Gateway = _Gs2328fIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 33),
    _Gs2328fIPv6Gateway_Type()
)
gs2328fIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv6Gateway.setStatus("current")
_Gs2328fLargestFreeMemBlock_Type = Integer32
_Gs2328fLargestFreeMemBlock_Object = MibScalar
gs2328fLargestFreeMemBlock = _Gs2328fLargestFreeMemBlock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 1500),
    _Gs2328fLargestFreeMemBlock_Type()
)
gs2328fLargestFreeMemBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLargestFreeMemBlock.setStatus("current")
_Gs2328fMemFree_Type = Integer32
_Gs2328fMemFree_Object = MibScalar
gs2328fMemFree = _Gs2328fMemFree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 1, 1501),
    _Gs2328fMemFree_Type()
)
gs2328fMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMemFree.setStatus("current")
_Gs2328fSystemTime_ObjectIdentity = ObjectIdentity
gs2328fSystemTime = _Gs2328fSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2)
)
_Gs2328fSystemTimeManual_ObjectIdentity = ObjectIdentity
gs2328fSystemTimeManual = _Gs2328fSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1)
)


class _Gs2328fSystemTimeManualClockSource_Type(Integer32):
    """Custom type gs2328fSystemTimeManualClockSource based on Integer32"""
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


_Gs2328fSystemTimeManualClockSource_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualClockSource_Object = MibScalar
gs2328fSystemTimeManualClockSource = _Gs2328fSystemTimeManualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 1),
    _Gs2328fSystemTimeManualClockSource_Type()
)
gs2328fSystemTimeManualClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualClockSource.setStatus("current")
_Gs2328fSystemTimeManualLocaltime_Type = DisplayString
_Gs2328fSystemTimeManualLocaltime_Object = MibScalar
gs2328fSystemTimeManualLocaltime = _Gs2328fSystemTimeManualLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 2),
    _Gs2328fSystemTimeManualLocaltime_Type()
)
gs2328fSystemTimeManualLocaltime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualLocaltime.setStatus("current")


class _Gs2328fSystemTimeManualTimeZoneOffset_Type(Integer32):
    """Custom type gs2328fSystemTimeManualTimeZoneOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 780),
    )


_Gs2328fSystemTimeManualTimeZoneOffset_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualTimeZoneOffset_Object = MibScalar
gs2328fSystemTimeManualTimeZoneOffset = _Gs2328fSystemTimeManualTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 3),
    _Gs2328fSystemTimeManualTimeZoneOffset_Type()
)
gs2328fSystemTimeManualTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualTimeZoneOffset.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavings_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSystemTimeManualDaylightSavings_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavings_Object = MibScalar
gs2328fSystemTimeManualDaylightSavings = _Gs2328fSystemTimeManualDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 4),
    _Gs2328fSystemTimeManualDaylightSavings_Type()
)
gs2328fSystemTimeManualDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavings.setStatus("current")


class _Gs2328fSystemTimeManualTimeSetOffset_Type(Integer32):
    """Custom type gs2328fSystemTimeManualTimeSetOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Gs2328fSystemTimeManualTimeSetOffset_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualTimeSetOffset_Object = MibScalar
gs2328fSystemTimeManualTimeSetOffset = _Gs2328fSystemTimeManualTimeSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 5),
    _Gs2328fSystemTimeManualTimeSetOffset_Type()
)
gs2328fSystemTimeManualTimeSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualTimeSetOffset.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsType_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsType based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsType_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsType_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsType = _Gs2328fSystemTimeManualDaylightSavingsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 6),
    _Gs2328fSystemTimeManualDaylightSavingsType_Type()
)
gs2328fSystemTimeManualDaylightSavingsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsType.setStatus("current")
_Gs2328fSystemTimeManualDaylightSavingsBydatesFrom_Type = DisplayString
_Gs2328fSystemTimeManualDaylightSavingsBydatesFrom_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsBydatesFrom = _Gs2328fSystemTimeManualDaylightSavingsBydatesFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 7),
    _Gs2328fSystemTimeManualDaylightSavingsBydatesFrom_Type()
)
gs2328fSystemTimeManualDaylightSavingsBydatesFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsBydatesFrom.setStatus("current")
_Gs2328fSystemTimeManualDaylightSavingsBydatesTo_Type = DisplayString
_Gs2328fSystemTimeManualDaylightSavingsBydatesTo_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsBydatesTo = _Gs2328fSystemTimeManualDaylightSavingsBydatesTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 8),
    _Gs2328fSystemTimeManualDaylightSavingsBydatesTo_Type()
)
gs2328fSystemTimeManualDaylightSavingsBydatesTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsBydatesTo.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom = _Gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 9),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom = _Gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 10),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom = _Gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 11),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom.setStatus("current")
_Gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type = DisplayString
_Gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom = _Gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 12),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsRecurringDayTo_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsRecurringDayTo based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsRecurringDayTo_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsRecurringDayTo_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringDayTo = _Gs2328fSystemTimeManualDaylightSavingsRecurringDayTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 13),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringDayTo_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringDayTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringDayTo.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo = _Gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 14),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo.setStatus("current")


class _Gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo_Type(Integer32):
    """Custom type gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo based on Integer32"""
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


_Gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo_Type.__name__ = "Integer32"
_Gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo = _Gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 15),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo.setStatus("current")
_Gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo_Type = DisplayString
_Gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo_Object = MibScalar
gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo = _Gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 1, 16),
    _Gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo_Type()
)
gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo.setStatus("current")
_Gs2328fSystemTimeNTP_ObjectIdentity = ObjectIdentity
gs2328fSystemTimeNTP = _Gs2328fSystemTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2)
)
_Gs2328fSystemTimeNTPTable_Object = MibTable
gs2328fSystemTimeNTPTable = _Gs2328fSystemTimeNTPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPTable.setStatus("current")
_Gs2328fSystemTimeNTPEntry_Object = MibTableRow
gs2328fSystemTimeNTPEntry = _Gs2328fSystemTimeNTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 1, 1)
)
gs2328fSystemTimeNTPEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSystemTimeNTPIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPEntry.setStatus("current")


class _Gs2328fSystemTimeNTPIndex_Type(Integer32):
    """Custom type gs2328fSystemTimeNTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328fSystemTimeNTPIndex_Type.__name__ = "Integer32"
_Gs2328fSystemTimeNTPIndex_Object = MibTableColumn
gs2328fSystemTimeNTPIndex = _Gs2328fSystemTimeNTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 1, 1, 1),
    _Gs2328fSystemTimeNTPIndex_Type()
)
gs2328fSystemTimeNTPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPIndex.setStatus("current")


class _Gs2328fSystemTimeNTPServerIPType_Type(Integer32):
    """Custom type gs2328fSystemTimeNTPServerIPType based on Integer32"""
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


_Gs2328fSystemTimeNTPServerIPType_Type.__name__ = "Integer32"
_Gs2328fSystemTimeNTPServerIPType_Object = MibTableColumn
gs2328fSystemTimeNTPServerIPType = _Gs2328fSystemTimeNTPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 1, 1, 2),
    _Gs2328fSystemTimeNTPServerIPType_Type()
)
gs2328fSystemTimeNTPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPServerIPType.setStatus("current")
_Gs2328fSystemTimeNTPServer_Type = DisplayString
_Gs2328fSystemTimeNTPServer_Object = MibTableColumn
gs2328fSystemTimeNTPServer = _Gs2328fSystemTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 1, 1, 3),
    _Gs2328fSystemTimeNTPServer_Type()
)
gs2328fSystemTimeNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPServer.setStatus("current")


class _Gs2328fSystemTimeNTPCurrentMode_Type(Integer32):
    """Custom type gs2328fSystemTimeNTPCurrentMode based on Integer32"""
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


_Gs2328fSystemTimeNTPCurrentMode_Type.__name__ = "Integer32"
_Gs2328fSystemTimeNTPCurrentMode_Object = MibTableColumn
gs2328fSystemTimeNTPCurrentMode = _Gs2328fSystemTimeNTPCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 1, 1, 4),
    _Gs2328fSystemTimeNTPCurrentMode_Type()
)
gs2328fSystemTimeNTPCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPCurrentMode.setStatus("current")


class _Gs2328fSystemTimeNTPRequestInterval_Type(Integer32):
    """Custom type gs2328fSystemTimeNTPRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 999999999),
    )


_Gs2328fSystemTimeNTPRequestInterval_Type.__name__ = "Integer32"
_Gs2328fSystemTimeNTPRequestInterval_Object = MibScalar
gs2328fSystemTimeNTPRequestInterval = _Gs2328fSystemTimeNTPRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 2),
    _Gs2328fSystemTimeNTPRequestInterval_Type()
)
gs2328fSystemTimeNTPRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPRequestInterval.setStatus("current")


class _Gs2328fSystemTimeNTPTriesNumber_Type(Integer32):
    """Custom type gs2328fSystemTimeNTPTriesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_Gs2328fSystemTimeNTPTriesNumber_Type.__name__ = "Integer32"
_Gs2328fSystemTimeNTPTriesNumber_Object = MibScalar
gs2328fSystemTimeNTPTriesNumber = _Gs2328fSystemTimeNTPTriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 2, 2, 3),
    _Gs2328fSystemTimeNTPTriesNumber_Type()
)
gs2328fSystemTimeNTPTriesNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemTimeNTPTriesNumber.setStatus("current")
_Gs2328fSystemAccount_ObjectIdentity = ObjectIdentity
gs2328fSystemAccount = _Gs2328fSystemAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3)
)
_Gs2328fSystemAccountUsers_ObjectIdentity = ObjectIdentity
gs2328fSystemAccountUsers = _Gs2328fSystemAccountUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1)
)


class _Gs2328fSystemAccountUserCreate_Type(Integer32):
    """Custom type gs2328fSystemAccountUserCreate based on Integer32"""
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


_Gs2328fSystemAccountUserCreate_Type.__name__ = "Integer32"
_Gs2328fSystemAccountUserCreate_Object = MibScalar
gs2328fSystemAccountUserCreate = _Gs2328fSystemAccountUserCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 1),
    _Gs2328fSystemAccountUserCreate_Type()
)
gs2328fSystemAccountUserCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemAccountUserCreate.setStatus("current")
_Gs2328fSystemAccountUsersTable_Object = MibTable
gs2328fSystemAccountUsersTable = _Gs2328fSystemAccountUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fSystemAccountUsersTable.setStatus("current")
_Gs2328fSystemAccountUsersEntry_Object = MibTableRow
gs2328fSystemAccountUsersEntry = _Gs2328fSystemAccountUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2, 1)
)
gs2328fSystemAccountUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fUserIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSystemAccountUsersEntry.setStatus("current")


class _Gs2328fUserIndex_Type(Integer32):
    """Custom type gs2328fUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Gs2328fUserIndex_Type.__name__ = "Integer32"
_Gs2328fUserIndex_Object = MibTableColumn
gs2328fUserIndex = _Gs2328fUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2, 1, 1),
    _Gs2328fUserIndex_Type()
)
gs2328fUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fUserIndex.setStatus("current")


class _Gs2328fUserName_Type(DisplayString):
    """Custom type gs2328fUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fUserName_Type.__name__ = "DisplayString"
_Gs2328fUserName_Object = MibTableColumn
gs2328fUserName = _Gs2328fUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2, 1, 2),
    _Gs2328fUserName_Type()
)
gs2328fUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fUserName.setStatus("current")


class _Gs2328fPassword_Type(DisplayString):
    """Custom type gs2328fPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fPassword_Type.__name__ = "DisplayString"
_Gs2328fPassword_Object = MibTableColumn
gs2328fPassword = _Gs2328fPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2, 1, 3),
    _Gs2328fPassword_Type()
)
gs2328fPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPassword.setStatus("current")


class _Gs2328fUserPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fUserPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fUserPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fUserPrivilegeLevel_Object = MibTableColumn
gs2328fUserPrivilegeLevel = _Gs2328fUserPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2, 1, 4),
    _Gs2328fUserPrivilegeLevel_Type()
)
gs2328fUserPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fUserPrivilegeLevel.setStatus("current")


class _Gs2328fAccountUserRowStatus_Type(Integer32):
    """Custom type gs2328fAccountUserRowStatus based on Integer32"""
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


_Gs2328fAccountUserRowStatus_Type.__name__ = "Integer32"
_Gs2328fAccountUserRowStatus_Object = MibTableColumn
gs2328fAccountUserRowStatus = _Gs2328fAccountUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 2, 1, 5),
    _Gs2328fAccountUserRowStatus_Type()
)
gs2328fAccountUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccountUserRowStatus.setStatus("current")


class _Gs2328fSystemAccountUsersSuperUserPassword_Type(OctetString):
    """Custom type gs2328fSystemAccountUsersSuperUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2328fSystemAccountUsersSuperUserPassword_Type.__name__ = "OctetString"
_Gs2328fSystemAccountUsersSuperUserPassword_Object = MibScalar
gs2328fSystemAccountUsersSuperUserPassword = _Gs2328fSystemAccountUsersSuperUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 1500),
    _Gs2328fSystemAccountUsersSuperUserPassword_Type()
)
gs2328fSystemAccountUsersSuperUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemAccountUsersSuperUserPassword.setStatus("current")


class _Gs2328fSystemAccountEnforcePasswordRules_Type(Integer32):
    """Custom type gs2328fSystemAccountEnforcePasswordRules based on Integer32"""
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


_Gs2328fSystemAccountEnforcePasswordRules_Type.__name__ = "Integer32"
_Gs2328fSystemAccountEnforcePasswordRules_Object = MibScalar
gs2328fSystemAccountEnforcePasswordRules = _Gs2328fSystemAccountEnforcePasswordRules_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 1, 1501),
    _Gs2328fSystemAccountEnforcePasswordRules_Type()
)
gs2328fSystemAccountEnforcePasswordRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemAccountEnforcePasswordRules.setStatus("current")
_Gs2328fSystemAccountPrivilegeLevel_ObjectIdentity = ObjectIdentity
gs2328fSystemAccountPrivilegeLevel = _Gs2328fSystemAccountPrivilegeLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2)
)


class _Gs2328fAccountPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fAccountPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fAccountPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fAccountPrivilegeLevel_Object = MibScalar
gs2328fAccountPrivilegeLevel = _Gs2328fAccountPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 1),
    _Gs2328fAccountPrivilegeLevel_Type()
)
gs2328fAccountPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccountPrivilegeLevel.setStatus("current")


class _Gs2328fAggregationPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fAggregationPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fAggregationPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fAggregationPrivilegeLevel_Object = MibScalar
gs2328fAggregationPrivilegeLevel = _Gs2328fAggregationPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 2),
    _Gs2328fAggregationPrivilegeLevel_Type()
)
gs2328fAggregationPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAggregationPrivilegeLevel.setStatus("current")


class _Gs2328fDiagnosticsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fDiagnosticsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fDiagnosticsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fDiagnosticsPrivilegeLevel_Object = MibScalar
gs2328fDiagnosticsPrivilegeLevel = _Gs2328fDiagnosticsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 3),
    _Gs2328fDiagnosticsPrivilegeLevel_Type()
)
gs2328fDiagnosticsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDiagnosticsPrivilegeLevel.setStatus("current")


class _Gs2328fEEEPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fEEEPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fEEEPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fEEEPrivilegeLevel_Object = MibScalar
gs2328fEEEPrivilegeLevel = _Gs2328fEEEPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 4),
    _Gs2328fEEEPrivilegeLevel_Type()
)
gs2328fEEEPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fEEEPrivilegeLevel.setStatus("current")


class _Gs2328fEasyportPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fEasyportPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fEasyportPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fEasyportPrivilegeLevel_Object = MibScalar
gs2328fEasyportPrivilegeLevel = _Gs2328fEasyportPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 9),
    _Gs2328fEasyportPrivilegeLevel_Type()
)
gs2328fEasyportPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fEasyportPrivilegeLevel.setStatus("current")


class _Gs2328fGARPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fGARPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fGARPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fGARPPrivilegeLevel_Object = MibScalar
gs2328fGARPPrivilegeLevel = _Gs2328fGARPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 10),
    _Gs2328fGARPPrivilegeLevel_Type()
)
gs2328fGARPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPPrivilegeLevel.setStatus("current")


class _Gs2328fGVRPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fGVRPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fGVRPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fGVRPPrivilegeLevel_Object = MibScalar
gs2328fGVRPPrivilegeLevel = _Gs2328fGVRPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 11),
    _Gs2328fGVRPPrivilegeLevel_Type()
)
gs2328fGVRPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGVRPPrivilegeLevel.setStatus("current")


class _Gs2328fIPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fIPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fIPPrivilegeLevel_Object = MibScalar
gs2328fIPPrivilegeLevel = _Gs2328fIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 12),
    _Gs2328fIPPrivilegeLevel_Type()
)
gs2328fIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPPrivilegeLevel.setStatus("current")


class _Gs2328fIPMCSnoopingPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fIPMCSnoopingPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fIPMCSnoopingPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fIPMCSnoopingPrivilegeLevel_Object = MibScalar
gs2328fIPMCSnoopingPrivilegeLevel = _Gs2328fIPMCSnoopingPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 13),
    _Gs2328fIPMCSnoopingPrivilegeLevel_Type()
)
gs2328fIPMCSnoopingPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPMCSnoopingPrivilegeLevel.setStatus("current")


class _Gs2328fLACPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fLACPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fLACPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fLACPPrivilegeLevel_Object = MibScalar
gs2328fLACPPrivilegeLevel = _Gs2328fLACPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 14),
    _Gs2328fLACPPrivilegeLevel_Type()
)
gs2328fLACPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLACPPrivilegeLevel.setStatus("current")


class _Gs2328fLLDPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fLLDPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fLLDPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fLLDPPrivilegeLevel_Object = MibScalar
gs2328fLLDPPrivilegeLevel = _Gs2328fLLDPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 15),
    _Gs2328fLLDPPrivilegeLevel_Type()
)
gs2328fLLDPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLLDPPrivilegeLevel.setStatus("current")


class _Gs2328fLLDPMEDPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fLLDPMEDPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fLLDPMEDPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fLLDPMEDPrivilegeLevel_Object = MibScalar
gs2328fLLDPMEDPrivilegeLevel = _Gs2328fLLDPMEDPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 16),
    _Gs2328fLLDPMEDPrivilegeLevel_Type()
)
gs2328fLLDPMEDPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLLDPMEDPrivilegeLevel.setStatus("current")


class _Gs2328fLoopProtectPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fLoopProtectPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fLoopProtectPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fLoopProtectPrivilegeLevel_Object = MibScalar
gs2328fLoopProtectPrivilegeLevel = _Gs2328fLoopProtectPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 17),
    _Gs2328fLoopProtectPrivilegeLevel_Type()
)
gs2328fLoopProtectPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectPrivilegeLevel.setStatus("current")


class _Gs2328fMACTablePrivilegeLevel_Type(Integer32):
    """Custom type gs2328fMACTablePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fMACTablePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fMACTablePrivilegeLevel_Object = MibScalar
gs2328fMACTablePrivilegeLevel = _Gs2328fMACTablePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 18),
    _Gs2328fMACTablePrivilegeLevel_Type()
)
gs2328fMACTablePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACTablePrivilegeLevel.setStatus("current")


class _Gs2328fMVRPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fMVRPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fMVRPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fMVRPrivilegeLevel_Object = MibScalar
gs2328fMVRPrivilegeLevel = _Gs2328fMVRPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 22),
    _Gs2328fMVRPrivilegeLevel_Type()
)
gs2328fMVRPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPrivilegeLevel.setStatus("current")


class _Gs2328fMaintenancePrivilegeLevel_Type(Integer32):
    """Custom type gs2328fMaintenancePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fMaintenancePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fMaintenancePrivilegeLevel_Object = MibScalar
gs2328fMaintenancePrivilegeLevel = _Gs2328fMaintenancePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 24),
    _Gs2328fMaintenancePrivilegeLevel_Type()
)
gs2328fMaintenancePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMaintenancePrivilegeLevel.setStatus("current")


class _Gs2328fMirroringPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fMirroringPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fMirroringPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fMirroringPrivilegeLevel_Object = MibScalar
gs2328fMirroringPrivilegeLevel = _Gs2328fMirroringPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 25),
    _Gs2328fMirroringPrivilegeLevel_Type()
)
gs2328fMirroringPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMirroringPrivilegeLevel.setStatus("current")


class _Gs2328fPortsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fPortsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fPortsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fPortsPrivilegeLevel_Object = MibScalar
gs2328fPortsPrivilegeLevel = _Gs2328fPortsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 27),
    _Gs2328fPortsPrivilegeLevel_Type()
)
gs2328fPortsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortsPrivilegeLevel.setStatus("current")


class _Gs2328fPrivateVLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fPrivateVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fPrivateVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fPrivateVLANsPrivilegeLevel_Object = MibScalar
gs2328fPrivateVLANsPrivilegeLevel = _Gs2328fPrivateVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 28),
    _Gs2328fPrivateVLANsPrivilegeLevel_Type()
)
gs2328fPrivateVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPrivateVLANsPrivilegeLevel.setStatus("current")


class _Gs2328fQoSPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fQoSPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fQoSPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fQoSPrivilegeLevel_Object = MibScalar
gs2328fQoSPrivilegeLevel = _Gs2328fQoSPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 29),
    _Gs2328fQoSPrivilegeLevel_Type()
)
gs2328fQoSPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSPrivilegeLevel.setStatus("current")


class _Gs2328fSFlowPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSFlowPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSFlowPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSFlowPrivilegeLevel_Object = MibScalar
gs2328fSFlowPrivilegeLevel = _Gs2328fSFlowPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 30),
    _Gs2328fSFlowPrivilegeLevel_Type()
)
gs2328fSFlowPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSFlowPrivilegeLevel.setStatus("current")


class _Gs2328fSMTPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSMTPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSMTPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSMTPPrivilegeLevel_Object = MibScalar
gs2328fSMTPPrivilegeLevel = _Gs2328fSMTPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 31),
    _Gs2328fSMTPPrivilegeLevel_Type()
)
gs2328fSMTPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPPrivilegeLevel.setStatus("current")


class _Gs2328fSNMPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSNMPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSNMPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSNMPPrivilegeLevel_Object = MibScalar
gs2328fSNMPPrivilegeLevel = _Gs2328fSNMPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 32),
    _Gs2328fSNMPPrivilegeLevel_Type()
)
gs2328fSNMPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSNMPPrivilegeLevel.setStatus("current")


class _Gs2328fSecurityPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSecurityPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSecurityPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSecurityPrivilegeLevel_Object = MibScalar
gs2328fSecurityPrivilegeLevel = _Gs2328fSecurityPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 33),
    _Gs2328fSecurityPrivilegeLevel_Type()
)
gs2328fSecurityPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSecurityPrivilegeLevel.setStatus("current")


class _Gs2328fSingleIPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSingleIPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSingleIPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSingleIPPrivilegeLevel_Object = MibScalar
gs2328fSingleIPPrivilegeLevel = _Gs2328fSingleIPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 34),
    _Gs2328fSingleIPPrivilegeLevel_Type()
)
gs2328fSingleIPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSingleIPPrivilegeLevel.setStatus("current")


class _Gs2328fSpanningTreePrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSpanningTreePrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSpanningTreePrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSpanningTreePrivilegeLevel_Object = MibScalar
gs2328fSpanningTreePrivilegeLevel = _Gs2328fSpanningTreePrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 35),
    _Gs2328fSpanningTreePrivilegeLevel_Type()
)
gs2328fSpanningTreePrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSpanningTreePrivilegeLevel.setStatus("current")


class _Gs2328fSystemPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fSystemPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fSystemPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fSystemPrivilegeLevel_Object = MibScalar
gs2328fSystemPrivilegeLevel = _Gs2328fSystemPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 36),
    _Gs2328fSystemPrivilegeLevel_Type()
)
gs2328fSystemPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSystemPrivilegeLevel.setStatus("current")


class _Gs2328fTrapEventPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fTrapEventPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fTrapEventPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fTrapEventPrivilegeLevel_Object = MibScalar
gs2328fTrapEventPrivilegeLevel = _Gs2328fTrapEventPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 37),
    _Gs2328fTrapEventPrivilegeLevel_Type()
)
gs2328fTrapEventPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventPrivilegeLevel.setStatus("current")


class _Gs2328fUPnPPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fUPnPPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fUPnPPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fUPnPPrivilegeLevel_Object = MibScalar
gs2328fUPnPPrivilegeLevel = _Gs2328fUPnPPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 38),
    _Gs2328fUPnPPrivilegeLevel_Type()
)
gs2328fUPnPPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fUPnPPrivilegeLevel.setStatus("current")


class _Gs2328fVCLPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fVCLPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fVCLPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fVCLPrivilegeLevel_Object = MibScalar
gs2328fVCLPrivilegeLevel = _Gs2328fVCLPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 39),
    _Gs2328fVCLPrivilegeLevel_Type()
)
gs2328fVCLPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVCLPrivilegeLevel.setStatus("current")


class _Gs2328fVLANsPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fVLANsPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fVLANsPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fVLANsPrivilegeLevel_Object = MibScalar
gs2328fVLANsPrivilegeLevel = _Gs2328fVLANsPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 41),
    _Gs2328fVLANsPrivilegeLevel_Type()
)
gs2328fVLANsPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVLANsPrivilegeLevel.setStatus("current")


class _Gs2328fVoiceVLANPrivilegeLevel_Type(Integer32):
    """Custom type gs2328fVoiceVLANPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Gs2328fVoiceVLANPrivilegeLevel_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANPrivilegeLevel_Object = MibScalar
gs2328fVoiceVLANPrivilegeLevel = _Gs2328fVoiceVLANPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 3, 2, 42),
    _Gs2328fVoiceVLANPrivilegeLevel_Type()
)
gs2328fVoiceVLANPrivilegeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPrivilegeLevel.setStatus("current")
_Gs2328fIP_ObjectIdentity = ObjectIdentity
gs2328fIP = _Gs2328fIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4)
)
_Gs2328fIPv4_ObjectIdentity = ObjectIdentity
gs2328fIPv4 = _Gs2328fIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1)
)
_Gs2328fIPv4Configured_ObjectIdentity = ObjectIdentity
gs2328fIPv4Configured = _Gs2328fIPv4Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1)
)


class _Gs2328fIpv4DHCPClient_Type(Integer32):
    """Custom type gs2328fIpv4DHCPClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIpv4DHCPClient_Type.__name__ = "Integer32"
_Gs2328fIpv4DHCPClient_Object = MibScalar
gs2328fIpv4DHCPClient = _Gs2328fIpv4DHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 1),
    _Gs2328fIpv4DHCPClient_Type()
)
gs2328fIpv4DHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIpv4DHCPClient.setStatus("current")
_Gs2328fIPv4Address_Type = IpAddress
_Gs2328fIPv4Address_Object = MibScalar
gs2328fIPv4Address = _Gs2328fIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 2),
    _Gs2328fIPv4Address_Type()
)
gs2328fIPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPv4Address.setStatus("current")
_Gs2328fIPv4Mask_Type = IpAddress
_Gs2328fIPv4Mask_Object = MibScalar
gs2328fIPv4Mask = _Gs2328fIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 3),
    _Gs2328fIPv4Mask_Type()
)
gs2328fIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPv4Mask.setStatus("current")
_Gs2328fIPv4Gateway_Type = IpAddress
_Gs2328fIPv4Gateway_Object = MibScalar
gs2328fIPv4Gateway = _Gs2328fIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 4),
    _Gs2328fIPv4Gateway_Type()
)
gs2328fIPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPv4Gateway.setStatus("current")


class _Gs2328fIPv4VLANId_Type(Integer32):
    """Custom type gs2328fIPv4VLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fIPv4VLANId_Type.__name__ = "Integer32"
_Gs2328fIPv4VLANId_Object = MibScalar
gs2328fIPv4VLANId = _Gs2328fIPv4VLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 5),
    _Gs2328fIPv4VLANId_Type()
)
gs2328fIPv4VLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPv4VLANId.setStatus("current")
_Gs2328fIPv4DNSServer_Type = IpAddress
_Gs2328fIPv4DNSServer_Object = MibScalar
gs2328fIPv4DNSServer = _Gs2328fIPv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 6),
    _Gs2328fIPv4DNSServer_Type()
)
gs2328fIPv4DNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPv4DNSServer.setStatus("current")


class _Gs2328fIPv4DNSProxy_Type(Integer32):
    """Custom type gs2328fIPv4DNSProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIPv4DNSProxy_Type.__name__ = "Integer32"
_Gs2328fIPv4DNSProxy_Object = MibScalar
gs2328fIPv4DNSProxy = _Gs2328fIPv4DNSProxy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 1, 7),
    _Gs2328fIPv4DNSProxy_Type()
)
gs2328fIPv4DNSProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPv4DNSProxy.setStatus("current")
_Gs2328fIPv4Current_ObjectIdentity = ObjectIdentity
gs2328fIPv4Current = _Gs2328fIPv4Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2)
)


class _Gs2328fIpv4CurrentDHCPClient_Type(Integer32):
    """Custom type gs2328fIpv4CurrentDHCPClient based on Integer32"""
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


_Gs2328fIpv4CurrentDHCPClient_Type.__name__ = "Integer32"
_Gs2328fIpv4CurrentDHCPClient_Object = MibScalar
gs2328fIpv4CurrentDHCPClient = _Gs2328fIpv4CurrentDHCPClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2, 1),
    _Gs2328fIpv4CurrentDHCPClient_Type()
)
gs2328fIpv4CurrentDHCPClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIpv4CurrentDHCPClient.setStatus("current")
_Gs2328fIPv4CurrentAddress_Type = IpAddress
_Gs2328fIPv4CurrentAddress_Object = MibScalar
gs2328fIPv4CurrentAddress = _Gs2328fIPv4CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2, 2),
    _Gs2328fIPv4CurrentAddress_Type()
)
gs2328fIPv4CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv4CurrentAddress.setStatus("current")
_Gs2328fIPv4CurrentMask_Type = IpAddress
_Gs2328fIPv4CurrentMask_Object = MibScalar
gs2328fIPv4CurrentMask = _Gs2328fIPv4CurrentMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2, 3),
    _Gs2328fIPv4CurrentMask_Type()
)
gs2328fIPv4CurrentMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv4CurrentMask.setStatus("current")
_Gs2328fIPv4CurrentGateway_Type = IpAddress
_Gs2328fIPv4CurrentGateway_Object = MibScalar
gs2328fIPv4CurrentGateway = _Gs2328fIPv4CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2, 4),
    _Gs2328fIPv4CurrentGateway_Type()
)
gs2328fIPv4CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv4CurrentGateway.setStatus("current")


class _Gs2328fIPv4CurrentVLANId_Type(Integer32):
    """Custom type gs2328fIPv4CurrentVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fIPv4CurrentVLANId_Type.__name__ = "Integer32"
_Gs2328fIPv4CurrentVLANId_Object = MibScalar
gs2328fIPv4CurrentVLANId = _Gs2328fIPv4CurrentVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2, 5),
    _Gs2328fIPv4CurrentVLANId_Type()
)
gs2328fIPv4CurrentVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv4CurrentVLANId.setStatus("current")
_Gs2328fIPv4CurrentDNSServer_Type = IpAddress
_Gs2328fIPv4CurrentDNSServer_Object = MibScalar
gs2328fIPv4CurrentDNSServer = _Gs2328fIPv4CurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 1, 2, 6),
    _Gs2328fIPv4CurrentDNSServer_Type()
)
gs2328fIPv4CurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPv4CurrentDNSServer.setStatus("current")
_Gs2328fIPv6_ObjectIdentity = ObjectIdentity
gs2328fIPv6 = _Gs2328fIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2)
)
_Gs2328fIPv6Configured_ObjectIdentity = ObjectIdentity
gs2328fIPv6Configured = _Gs2328fIPv6Configured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 1)
)


class _Gs2328fIpv6AutoConfiguration_Type(Integer32):
    """Custom type gs2328fIpv6AutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIpv6AutoConfiguration_Type.__name__ = "Integer32"
_Gs2328fIpv6AutoConfiguration_Object = MibScalar
gs2328fIpv6AutoConfiguration = _Gs2328fIpv6AutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 1, 1),
    _Gs2328fIpv6AutoConfiguration_Type()
)
gs2328fIpv6AutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIpv6AutoConfiguration.setStatus("current")


class _Gs2328fIpv6Address_Type(DisplayString):
    """Custom type gs2328fIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328fIpv6Address_Type.__name__ = "DisplayString"
_Gs2328fIpv6Address_Object = MibScalar
gs2328fIpv6Address = _Gs2328fIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 1, 2),
    _Gs2328fIpv6Address_Type()
)
gs2328fIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIpv6Address.setStatus("current")


class _Gs2328fIpv6Prefix_Type(Integer32):
    """Custom type gs2328fIpv6Prefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2328fIpv6Prefix_Type.__name__ = "Integer32"
_Gs2328fIpv6Prefix_Object = MibScalar
gs2328fIpv6Prefix = _Gs2328fIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 1, 3),
    _Gs2328fIpv6Prefix_Type()
)
gs2328fIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIpv6Prefix.setStatus("current")


class _Gs2328fIpv6Gateway_Type(DisplayString):
    """Custom type gs2328fIpv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328fIpv6Gateway_Type.__name__ = "DisplayString"
_Gs2328fIpv6Gateway_Object = MibScalar
gs2328fIpv6Gateway = _Gs2328fIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 1, 4),
    _Gs2328fIpv6Gateway_Type()
)
gs2328fIpv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIpv6Gateway.setStatus("current")
_Gs2328fIPv6Current_ObjectIdentity = ObjectIdentity
gs2328fIPv6Current = _Gs2328fIPv6Current_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 2)
)


class _Gs2328fIpv6CurrentAutoConfiguration_Type(Integer32):
    """Custom type gs2328fIpv6CurrentAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIpv6CurrentAutoConfiguration_Type.__name__ = "Integer32"
_Gs2328fIpv6CurrentAutoConfiguration_Object = MibScalar
gs2328fIpv6CurrentAutoConfiguration = _Gs2328fIpv6CurrentAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 2, 1),
    _Gs2328fIpv6CurrentAutoConfiguration_Type()
)
gs2328fIpv6CurrentAutoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIpv6CurrentAutoConfiguration.setStatus("current")


class _Gs2328fIpv6CurrentAddress_Type(DisplayString):
    """Custom type gs2328fIpv6CurrentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328fIpv6CurrentAddress_Type.__name__ = "DisplayString"
_Gs2328fIpv6CurrentAddress_Object = MibScalar
gs2328fIpv6CurrentAddress = _Gs2328fIpv6CurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 2, 2),
    _Gs2328fIpv6CurrentAddress_Type()
)
gs2328fIpv6CurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIpv6CurrentAddress.setStatus("current")


class _Gs2328fIpv6CurrentLinkLocalAddress_Type(DisplayString):
    """Custom type gs2328fIpv6CurrentLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328fIpv6CurrentLinkLocalAddress_Type.__name__ = "DisplayString"
_Gs2328fIpv6CurrentLinkLocalAddress_Object = MibScalar
gs2328fIpv6CurrentLinkLocalAddress = _Gs2328fIpv6CurrentLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 2, 3),
    _Gs2328fIpv6CurrentLinkLocalAddress_Type()
)
gs2328fIpv6CurrentLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIpv6CurrentLinkLocalAddress.setStatus("current")


class _Gs2328fIpv6CurrentPrefix_Type(DisplayString):
    """Custom type gs2328fIpv6CurrentPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Gs2328fIpv6CurrentPrefix_Type.__name__ = "DisplayString"
_Gs2328fIpv6CurrentPrefix_Object = MibScalar
gs2328fIpv6CurrentPrefix = _Gs2328fIpv6CurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 2, 4),
    _Gs2328fIpv6CurrentPrefix_Type()
)
gs2328fIpv6CurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIpv6CurrentPrefix.setStatus("current")


class _Gs2328fIpv6CurrentGateway_Type(DisplayString):
    """Custom type gs2328fIpv6CurrentGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Gs2328fIpv6CurrentGateway_Type.__name__ = "DisplayString"
_Gs2328fIpv6CurrentGateway_Object = MibScalar
gs2328fIpv6CurrentGateway = _Gs2328fIpv6CurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 4, 2, 2, 5),
    _Gs2328fIpv6CurrentGateway_Type()
)
gs2328fIpv6CurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIpv6CurrentGateway.setStatus("current")
_Gs2328fSyslog_ObjectIdentity = ObjectIdentity
gs2328fSyslog = _Gs2328fSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5)
)
_Gs2328fSyslogConf_ObjectIdentity = ObjectIdentity
gs2328fSyslogConf = _Gs2328fSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 1)
)


class _Gs2328fServerMode_Type(Integer32):
    """Custom type gs2328fServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fServerMode_Type.__name__ = "Integer32"
_Gs2328fServerMode_Object = MibScalar
gs2328fServerMode = _Gs2328fServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 1, 1),
    _Gs2328fServerMode_Type()
)
gs2328fServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fServerMode.setStatus("current")
_Gs2328fServerAddress1_Type = IpAddress
_Gs2328fServerAddress1_Object = MibScalar
gs2328fServerAddress1 = _Gs2328fServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 1, 2),
    _Gs2328fServerAddress1_Type()
)
gs2328fServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fServerAddress1.setStatus("current")
_Gs2328fServerAddress2_Type = IpAddress
_Gs2328fServerAddress2_Object = MibScalar
gs2328fServerAddress2 = _Gs2328fServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 1, 3),
    _Gs2328fServerAddress2_Type()
)
gs2328fServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fServerAddress2.setStatus("current")


class _Gs2328fSyslogLevel_Type(Integer32):
    """Custom type gs2328fSyslogLevel based on Integer32"""
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


_Gs2328fSyslogLevel_Type.__name__ = "Integer32"
_Gs2328fSyslogLevel_Object = MibScalar
gs2328fSyslogLevel = _Gs2328fSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 1, 4),
    _Gs2328fSyslogLevel_Type()
)
gs2328fSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSyslogLevel.setStatus("current")
_Gs2328fSyslogDetailedInfo_ObjectIdentity = ObjectIdentity
gs2328fSyslogDetailedInfo = _Gs2328fSyslogDetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2)
)


class _Gs2328fSyslogDetailedInfoClear_Type(Integer32):
    """Custom type gs2328fSyslogDetailedInfoClear based on Integer32"""
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


_Gs2328fSyslogDetailedInfoClear_Type.__name__ = "Integer32"
_Gs2328fSyslogDetailedInfoClear_Object = MibScalar
gs2328fSyslogDetailedInfoClear = _Gs2328fSyslogDetailedInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 1),
    _Gs2328fSyslogDetailedInfoClear_Type()
)
gs2328fSyslogDetailedInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoClear.setStatus("current")
_Gs2328fSyslogDetailedInfoTable_Object = MibTable
gs2328fSyslogDetailedInfoTable = _Gs2328fSyslogDetailedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoTable.setStatus("current")
_Gs2328fSyslogDetailedInfoEntry_Object = MibTableRow
gs2328fSyslogDetailedInfoEntry = _Gs2328fSyslogDetailedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 2, 1)
)
gs2328fSyslogDetailedInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSyslogDetailedInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoEntry.setStatus("current")


class _Gs2328fSyslogDetailedInfoIndex_Type(Integer32):
    """Custom type gs2328fSyslogDetailedInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2328fSyslogDetailedInfoIndex_Type.__name__ = "Integer32"
_Gs2328fSyslogDetailedInfoIndex_Object = MibTableColumn
gs2328fSyslogDetailedInfoIndex = _Gs2328fSyslogDetailedInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 2, 1, 1),
    _Gs2328fSyslogDetailedInfoIndex_Type()
)
gs2328fSyslogDetailedInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoIndex.setStatus("current")
_Gs2328fSyslogDetailedInfoLevel_Type = DisplayString
_Gs2328fSyslogDetailedInfoLevel_Object = MibTableColumn
gs2328fSyslogDetailedInfoLevel = _Gs2328fSyslogDetailedInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 2, 1, 2),
    _Gs2328fSyslogDetailedInfoLevel_Type()
)
gs2328fSyslogDetailedInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoLevel.setStatus("current")


class _Gs2328fSyslogDetailedInfoTime_Type(DisplayString):
    """Custom type gs2328fSyslogDetailedInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Gs2328fSyslogDetailedInfoTime_Type.__name__ = "DisplayString"
_Gs2328fSyslogDetailedInfoTime_Object = MibTableColumn
gs2328fSyslogDetailedInfoTime = _Gs2328fSyslogDetailedInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 2, 1, 3),
    _Gs2328fSyslogDetailedInfoTime_Type()
)
gs2328fSyslogDetailedInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoTime.setStatus("current")
_Gs2328fSyslogDetailedInfoMessage_Type = DisplayString
_Gs2328fSyslogDetailedInfoMessage_Object = MibTableColumn
gs2328fSyslogDetailedInfoMessage = _Gs2328fSyslogDetailedInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 5, 2, 2, 1, 4),
    _Gs2328fSyslogDetailedInfoMessage_Type()
)
gs2328fSyslogDetailedInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSyslogDetailedInfoMessage.setStatus("current")
_Gs2328fSnmp_ObjectIdentity = ObjectIdentity
gs2328fSnmp = _Gs2328fSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6)
)
_Gs2328fSnmpConf_ObjectIdentity = ObjectIdentity
gs2328fSnmpConf = _Gs2328fSnmpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1)
)


class _Gs2328fGetCommunityMode_Type(Integer32):
    """Custom type gs2328fGetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fGetCommunityMode_Type.__name__ = "Integer32"
_Gs2328fGetCommunityMode_Object = MibScalar
gs2328fGetCommunityMode = _Gs2328fGetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 1),
    _Gs2328fGetCommunityMode_Type()
)
gs2328fGetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGetCommunityMode.setStatus("current")
_Gs2328fGetCommunity_Type = DisplayString
_Gs2328fGetCommunity_Object = MibScalar
gs2328fGetCommunity = _Gs2328fGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 2),
    _Gs2328fGetCommunity_Type()
)
gs2328fGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGetCommunity.setStatus("current")


class _Gs2328fSetCommunityMode_Type(Integer32):
    """Custom type gs2328fSetCommunityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSetCommunityMode_Type.__name__ = "Integer32"
_Gs2328fSetCommunityMode_Object = MibScalar
gs2328fSetCommunityMode = _Gs2328fSetCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 3),
    _Gs2328fSetCommunityMode_Type()
)
gs2328fSetCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSetCommunityMode.setStatus("current")
_Gs2328fSetCommunity_Type = DisplayString
_Gs2328fSetCommunity_Object = MibScalar
gs2328fSetCommunity = _Gs2328fSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 4),
    _Gs2328fSetCommunity_Type()
)
gs2328fSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSetCommunity.setStatus("current")
_Gs2328fGetCommunityConfTable_Object = MibTable
gs2328fGetCommunityConfTable = _Gs2328fGetCommunityConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    gs2328fGetCommunityConfTable.setStatus("current")
_Gs2328fGetCommunityConfEntry_Object = MibTableRow
gs2328fGetCommunityConfEntry = _Gs2328fGetCommunityConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 5, 1)
)
gs2328fGetCommunityConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fCommunityConfIndex"),
)
if mibBuilder.loadTexts:
    gs2328fGetCommunityConfEntry.setStatus("current")


class _Gs2328fCommunityConfIndex_Type(Integer32):
    """Custom type gs2328fCommunityConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fCommunityConfIndex_Type.__name__ = "Integer32"
_Gs2328fCommunityConfIndex_Object = MibTableColumn
gs2328fCommunityConfIndex = _Gs2328fCommunityConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 5, 1, 1),
    _Gs2328fCommunityConfIndex_Type()
)
gs2328fCommunityConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fCommunityConfIndex.setStatus("current")
_Gs2328fCommunityConfGetCommunity_Type = DisplayString
_Gs2328fCommunityConfGetCommunity_Object = MibTableColumn
gs2328fCommunityConfGetCommunity = _Gs2328fCommunityConfGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 5, 1, 2),
    _Gs2328fCommunityConfGetCommunity_Type()
)
gs2328fCommunityConfGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fCommunityConfGetCommunity.setStatus("current")
_Gs2328fTrapHostConfTable_Object = MibTable
gs2328fTrapHostConfTable = _Gs2328fTrapHostConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    gs2328fTrapHostConfTable.setStatus("current")
_Gs2328fTrapHostConfEntry_Object = MibTableRow
gs2328fTrapHostConfEntry = _Gs2328fTrapHostConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1)
)
gs2328fTrapHostConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fTrapHostConfIndex"),
)
if mibBuilder.loadTexts:
    gs2328fTrapHostConfEntry.setStatus("current")


class _Gs2328fTrapHostConfIndex_Type(Integer32):
    """Custom type gs2328fTrapHostConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2328fTrapHostConfIndex_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfIndex_Object = MibTableColumn
gs2328fTrapHostConfIndex = _Gs2328fTrapHostConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 1),
    _Gs2328fTrapHostConfIndex_Type()
)
gs2328fTrapHostConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfIndex.setStatus("current")


class _Gs2328fTrapHostConfVersion_Type(Integer32):
    """Custom type gs2328fTrapHostConfVersion based on Integer32"""
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


_Gs2328fTrapHostConfVersion_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfVersion_Object = MibTableColumn
gs2328fTrapHostConfVersion = _Gs2328fTrapHostConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 2),
    _Gs2328fTrapHostConfVersion_Type()
)
gs2328fTrapHostConfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfVersion.setStatus("current")


class _Gs2328fTrapHostConfIPType_Type(Integer32):
    """Custom type gs2328fTrapHostConfIPType based on Integer32"""
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


_Gs2328fTrapHostConfIPType_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfIPType_Object = MibTableColumn
gs2328fTrapHostConfIPType = _Gs2328fTrapHostConfIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 3),
    _Gs2328fTrapHostConfIPType_Type()
)
gs2328fTrapHostConfIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfIPType.setStatus("current")
_Gs2328fTrapHostConfIP_Type = DisplayString
_Gs2328fTrapHostConfIP_Object = MibTableColumn
gs2328fTrapHostConfIP = _Gs2328fTrapHostConfIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 4),
    _Gs2328fTrapHostConfIP_Type()
)
gs2328fTrapHostConfIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfIP.setStatus("current")


class _Gs2328fTrapHostConfPort_Type(Integer32):
    """Custom type gs2328fTrapHostConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fTrapHostConfPort_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfPort_Object = MibTableColumn
gs2328fTrapHostConfPort = _Gs2328fTrapHostConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 5),
    _Gs2328fTrapHostConfPort_Type()
)
gs2328fTrapHostConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfPort.setStatus("current")


class _Gs2328fTrapHostConfCommunity_Type(DisplayString):
    """Custom type gs2328fTrapHostConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fTrapHostConfCommunity_Type.__name__ = "DisplayString"
_Gs2328fTrapHostConfCommunity_Object = MibTableColumn
gs2328fTrapHostConfCommunity = _Gs2328fTrapHostConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 6),
    _Gs2328fTrapHostConfCommunity_Type()
)
gs2328fTrapHostConfCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfCommunity.setStatus("current")


class _Gs2328fTrapHostConfSeverityLevel_Type(Integer32):
    """Custom type gs2328fTrapHostConfSeverityLevel based on Integer32"""
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


_Gs2328fTrapHostConfSeverityLevel_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfSeverityLevel_Object = MibTableColumn
gs2328fTrapHostConfSeverityLevel = _Gs2328fTrapHostConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 7),
    _Gs2328fTrapHostConfSeverityLevel_Type()
)
gs2328fTrapHostConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfSeverityLevel.setStatus("current")


class _Gs2328fTrapHostConfSecurityLevel_Type(Integer32):
    """Custom type gs2328fTrapHostConfSecurityLevel based on Integer32"""
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


_Gs2328fTrapHostConfSecurityLevel_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfSecurityLevel_Object = MibTableColumn
gs2328fTrapHostConfSecurityLevel = _Gs2328fTrapHostConfSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 8),
    _Gs2328fTrapHostConfSecurityLevel_Type()
)
gs2328fTrapHostConfSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfSecurityLevel.setStatus("current")


class _Gs2328fTrapHostConfAuthPtc_Type(Integer32):
    """Custom type gs2328fTrapHostConfAuthPtc based on Integer32"""
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


_Gs2328fTrapHostConfAuthPtc_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfAuthPtc_Object = MibTableColumn
gs2328fTrapHostConfAuthPtc = _Gs2328fTrapHostConfAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 9),
    _Gs2328fTrapHostConfAuthPtc_Type()
)
gs2328fTrapHostConfAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfAuthPtc.setStatus("current")
_Gs2328fTrapHostConfAuthPassword_Type = DisplayString
_Gs2328fTrapHostConfAuthPassword_Object = MibTableColumn
gs2328fTrapHostConfAuthPassword = _Gs2328fTrapHostConfAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 10),
    _Gs2328fTrapHostConfAuthPassword_Type()
)
gs2328fTrapHostConfAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfAuthPassword.setStatus("current")


class _Gs2328fTrapHostConfPrivPtc_Type(Integer32):
    """Custom type gs2328fTrapHostConfPrivPtc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("des", 1)
    )


_Gs2328fTrapHostConfPrivPtc_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfPrivPtc_Object = MibTableColumn
gs2328fTrapHostConfPrivPtc = _Gs2328fTrapHostConfPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 11),
    _Gs2328fTrapHostConfPrivPtc_Type()
)
gs2328fTrapHostConfPrivPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfPrivPtc.setStatus("current")
_Gs2328fTrapHostConfPrivPassword_Type = DisplayString
_Gs2328fTrapHostConfPrivPassword_Object = MibTableColumn
gs2328fTrapHostConfPrivPassword = _Gs2328fTrapHostConfPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 12),
    _Gs2328fTrapHostConfPrivPassword_Type()
)
gs2328fTrapHostConfPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfPrivPassword.setStatus("current")


class _Gs2328fTrapHostConfCurrentMode_Type(Integer32):
    """Custom type gs2328fTrapHostConfCurrentMode based on Integer32"""
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


_Gs2328fTrapHostConfCurrentMode_Type.__name__ = "Integer32"
_Gs2328fTrapHostConfCurrentMode_Object = MibTableColumn
gs2328fTrapHostConfCurrentMode = _Gs2328fTrapHostConfCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 1, 6, 1, 13),
    _Gs2328fTrapHostConfCurrentMode_Type()
)
gs2328fTrapHostConfCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapHostConfCurrentMode.setStatus("current")
_Gs2328fSnmpSystem_ObjectIdentity = ObjectIdentity
gs2328fSnmpSystem = _Gs2328fSnmpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 2)
)


class _Gs2328fSnmpState_Type(Integer32):
    """Custom type gs2328fSnmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSnmpState_Type.__name__ = "Integer32"
_Gs2328fSnmpState_Object = MibScalar
gs2328fSnmpState = _Gs2328fSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 2, 1),
    _Gs2328fSnmpState_Type()
)
gs2328fSnmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpState.setStatus("current")


class _Gs2328fSnmpEngineID_Type(OctetString):
    """Custom type gs2328fSnmpEngineID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Gs2328fSnmpEngineID_Type.__name__ = "OctetString"
_Gs2328fSnmpEngineID_Object = MibScalar
gs2328fSnmpEngineID = _Gs2328fSnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 2, 2),
    _Gs2328fSnmpEngineID_Type()
)
gs2328fSnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpEngineID.setStatus("current")
_Gs2328fSnmpCommunities_ObjectIdentity = ObjectIdentity
gs2328fSnmpCommunities = _Gs2328fSnmpCommunities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3)
)


class _Gs2328fSnmpCommunitiesCreate_Type(Integer32):
    """Custom type gs2328fSnmpCommunitiesCreate based on Integer32"""
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


_Gs2328fSnmpCommunitiesCreate_Type.__name__ = "Integer32"
_Gs2328fSnmpCommunitiesCreate_Object = MibScalar
gs2328fSnmpCommunitiesCreate = _Gs2328fSnmpCommunitiesCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 1),
    _Gs2328fSnmpCommunitiesCreate_Type()
)
gs2328fSnmpCommunitiesCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesCreate.setStatus("current")
_Gs2328fSnmpCommunitiesTable_Object = MibTable
gs2328fSnmpCommunitiesTable = _Gs2328fSnmpCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesTable.setStatus("current")
_Gs2328fSnmpCommunitiesEntry_Object = MibTableRow
gs2328fSnmpCommunitiesEntry = _Gs2328fSnmpCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1)
)
gs2328fSnmpCommunitiesEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSnmpCommunitiesIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesEntry.setStatus("current")


class _Gs2328fSnmpCommunitiesIndex_Type(Integer32):
    """Custom type gs2328fSnmpCommunitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2328fSnmpCommunitiesIndex_Type.__name__ = "Integer32"
_Gs2328fSnmpCommunitiesIndex_Object = MibTableColumn
gs2328fSnmpCommunitiesIndex = _Gs2328fSnmpCommunitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1, 1),
    _Gs2328fSnmpCommunitiesIndex_Type()
)
gs2328fSnmpCommunitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesIndex.setStatus("current")


class _Gs2328fSnmpCommunitiesCommunity_Type(DisplayString):
    """Custom type gs2328fSnmpCommunitiesCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpCommunitiesCommunity_Type.__name__ = "DisplayString"
_Gs2328fSnmpCommunitiesCommunity_Object = MibTableColumn
gs2328fSnmpCommunitiesCommunity = _Gs2328fSnmpCommunitiesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1, 2),
    _Gs2328fSnmpCommunitiesCommunity_Type()
)
gs2328fSnmpCommunitiesCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesCommunity.setStatus("current")


class _Gs2328fSnmpCommunitiesUserName_Type(DisplayString):
    """Custom type gs2328fSnmpCommunitiesUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpCommunitiesUserName_Type.__name__ = "DisplayString"
_Gs2328fSnmpCommunitiesUserName_Object = MibTableColumn
gs2328fSnmpCommunitiesUserName = _Gs2328fSnmpCommunitiesUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1, 3),
    _Gs2328fSnmpCommunitiesUserName_Type()
)
gs2328fSnmpCommunitiesUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesUserName.setStatus("current")
_Gs2328fSnmpCommunitiesSourceIP_Type = IpAddress
_Gs2328fSnmpCommunitiesSourceIP_Object = MibTableColumn
gs2328fSnmpCommunitiesSourceIP = _Gs2328fSnmpCommunitiesSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1, 4),
    _Gs2328fSnmpCommunitiesSourceIP_Type()
)
gs2328fSnmpCommunitiesSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesSourceIP.setStatus("current")
_Gs2328fSnmpCommunitiesSourceMask_Type = IpAddress
_Gs2328fSnmpCommunitiesSourceMask_Object = MibTableColumn
gs2328fSnmpCommunitiesSourceMask = _Gs2328fSnmpCommunitiesSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1, 5),
    _Gs2328fSnmpCommunitiesSourceMask_Type()
)
gs2328fSnmpCommunitiesSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesSourceMask.setStatus("current")


class _Gs2328fSnmpCommunitiesRowStatus_Type(Integer32):
    """Custom type gs2328fSnmpCommunitiesRowStatus based on Integer32"""
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


_Gs2328fSnmpCommunitiesRowStatus_Type.__name__ = "Integer32"
_Gs2328fSnmpCommunitiesRowStatus_Object = MibTableColumn
gs2328fSnmpCommunitiesRowStatus = _Gs2328fSnmpCommunitiesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 3, 2, 1, 6),
    _Gs2328fSnmpCommunitiesRowStatus_Type()
)
gs2328fSnmpCommunitiesRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpCommunitiesRowStatus.setStatus("current")
_Gs2328fSnmpUsers_ObjectIdentity = ObjectIdentity
gs2328fSnmpUsers = _Gs2328fSnmpUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4)
)


class _Gs2328fSnmpUsersCreate_Type(Integer32):
    """Custom type gs2328fSnmpUsersCreate based on Integer32"""
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


_Gs2328fSnmpUsersCreate_Type.__name__ = "Integer32"
_Gs2328fSnmpUsersCreate_Object = MibScalar
gs2328fSnmpUsersCreate = _Gs2328fSnmpUsersCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 1),
    _Gs2328fSnmpUsersCreate_Type()
)
gs2328fSnmpUsersCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersCreate.setStatus("current")
_Gs2328fSnmpUsersTable_Object = MibTable
gs2328fSnmpUsersTable = _Gs2328fSnmpUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fSnmpUsersTable.setStatus("current")
_Gs2328fSnmpUsersEntry_Object = MibTableRow
gs2328fSnmpUsersEntry = _Gs2328fSnmpUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1)
)
gs2328fSnmpUsersEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSnmpUsersIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSnmpUsersEntry.setStatus("current")


class _Gs2328fSnmpUsersIndex_Type(Integer32):
    """Custom type gs2328fSnmpUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328fSnmpUsersIndex_Type.__name__ = "Integer32"
_Gs2328fSnmpUsersIndex_Object = MibTableColumn
gs2328fSnmpUsersIndex = _Gs2328fSnmpUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 1),
    _Gs2328fSnmpUsersIndex_Type()
)
gs2328fSnmpUsersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersIndex.setStatus("current")


class _Gs2328fSnmpUsersUserName_Type(DisplayString):
    """Custom type gs2328fSnmpUsersUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpUsersUserName_Type.__name__ = "DisplayString"
_Gs2328fSnmpUsersUserName_Object = MibTableColumn
gs2328fSnmpUsersUserName = _Gs2328fSnmpUsersUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 2),
    _Gs2328fSnmpUsersUserName_Type()
)
gs2328fSnmpUsersUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersUserName.setStatus("current")


class _Gs2328fSnmpUsersSecurityLevel_Type(Integer32):
    """Custom type gs2328fSnmpUsersSecurityLevel based on Integer32"""
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


_Gs2328fSnmpUsersSecurityLevel_Type.__name__ = "Integer32"
_Gs2328fSnmpUsersSecurityLevel_Object = MibTableColumn
gs2328fSnmpUsersSecurityLevel = _Gs2328fSnmpUsersSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 3),
    _Gs2328fSnmpUsersSecurityLevel_Type()
)
gs2328fSnmpUsersSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersSecurityLevel.setStatus("current")


class _Gs2328fSnmpUsersAuthenticationProtocol_Type(Integer32):
    """Custom type gs2328fSnmpUsersAuthenticationProtocol based on Integer32"""
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


_Gs2328fSnmpUsersAuthenticationProtocol_Type.__name__ = "Integer32"
_Gs2328fSnmpUsersAuthenticationProtocol_Object = MibTableColumn
gs2328fSnmpUsersAuthenticationProtocol = _Gs2328fSnmpUsersAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 4),
    _Gs2328fSnmpUsersAuthenticationProtocol_Type()
)
gs2328fSnmpUsersAuthenticationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersAuthenticationProtocol.setStatus("current")
_Gs2328fSnmpUsersAuthenticationPassword_Type = DisplayString
_Gs2328fSnmpUsersAuthenticationPassword_Object = MibTableColumn
gs2328fSnmpUsersAuthenticationPassword = _Gs2328fSnmpUsersAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 5),
    _Gs2328fSnmpUsersAuthenticationPassword_Type()
)
gs2328fSnmpUsersAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersAuthenticationPassword.setStatus("current")


class _Gs2328fSnmpUsersPrivacyProtocol_Type(Integer32):
    """Custom type gs2328fSnmpUsersPrivacyProtocol based on Integer32"""
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


_Gs2328fSnmpUsersPrivacyProtocol_Type.__name__ = "Integer32"
_Gs2328fSnmpUsersPrivacyProtocol_Object = MibTableColumn
gs2328fSnmpUsersPrivacyProtocol = _Gs2328fSnmpUsersPrivacyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 6),
    _Gs2328fSnmpUsersPrivacyProtocol_Type()
)
gs2328fSnmpUsersPrivacyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersPrivacyProtocol.setStatus("current")
_Gs2328fSnmpUsersPrivacyPassword_Type = DisplayString
_Gs2328fSnmpUsersPrivacyPassword_Object = MibTableColumn
gs2328fSnmpUsersPrivacyPassword = _Gs2328fSnmpUsersPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 7),
    _Gs2328fSnmpUsersPrivacyPassword_Type()
)
gs2328fSnmpUsersPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersPrivacyPassword.setStatus("current")


class _Gs2328fSnmpUsersRowStatus_Type(Integer32):
    """Custom type gs2328fSnmpUsersRowStatus based on Integer32"""
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


_Gs2328fSnmpUsersRowStatus_Type.__name__ = "Integer32"
_Gs2328fSnmpUsersRowStatus_Object = MibTableColumn
gs2328fSnmpUsersRowStatus = _Gs2328fSnmpUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 4, 2, 1, 8),
    _Gs2328fSnmpUsersRowStatus_Type()
)
gs2328fSnmpUsersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpUsersRowStatus.setStatus("current")
_Gs2328fSnmpGroups_ObjectIdentity = ObjectIdentity
gs2328fSnmpGroups = _Gs2328fSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5)
)


class _Gs2328fSnmpGroupsCreate_Type(Integer32):
    """Custom type gs2328fSnmpGroupsCreate based on Integer32"""
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


_Gs2328fSnmpGroupsCreate_Type.__name__ = "Integer32"
_Gs2328fSnmpGroupsCreate_Object = MibScalar
gs2328fSnmpGroupsCreate = _Gs2328fSnmpGroupsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 1),
    _Gs2328fSnmpGroupsCreate_Type()
)
gs2328fSnmpGroupsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsCreate.setStatus("current")
_Gs2328fSnmpGroupsTable_Object = MibTable
gs2328fSnmpGroupsTable = _Gs2328fSnmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsTable.setStatus("current")
_Gs2328fSnmpGroupsEntry_Object = MibTableRow
gs2328fSnmpGroupsEntry = _Gs2328fSnmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2, 1)
)
gs2328fSnmpGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSnmpGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsEntry.setStatus("current")


class _Gs2328fSnmpGroupsIndex_Type(Integer32):
    """Custom type gs2328fSnmpGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2328fSnmpGroupsIndex_Type.__name__ = "Integer32"
_Gs2328fSnmpGroupsIndex_Object = MibTableColumn
gs2328fSnmpGroupsIndex = _Gs2328fSnmpGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2, 1, 1),
    _Gs2328fSnmpGroupsIndex_Type()
)
gs2328fSnmpGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsIndex.setStatus("current")


class _Gs2328fSnmpGroupsSecurityModel_Type(Integer32):
    """Custom type gs2328fSnmpGroupsSecurityModel based on Integer32"""
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


_Gs2328fSnmpGroupsSecurityModel_Type.__name__ = "Integer32"
_Gs2328fSnmpGroupsSecurityModel_Object = MibTableColumn
gs2328fSnmpGroupsSecurityModel = _Gs2328fSnmpGroupsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2, 1, 2),
    _Gs2328fSnmpGroupsSecurityModel_Type()
)
gs2328fSnmpGroupsSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsSecurityModel.setStatus("current")


class _Gs2328fSnmpGroupsSecurityName_Type(DisplayString):
    """Custom type gs2328fSnmpGroupsSecurityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpGroupsSecurityName_Type.__name__ = "DisplayString"
_Gs2328fSnmpGroupsSecurityName_Object = MibTableColumn
gs2328fSnmpGroupsSecurityName = _Gs2328fSnmpGroupsSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2, 1, 3),
    _Gs2328fSnmpGroupsSecurityName_Type()
)
gs2328fSnmpGroupsSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsSecurityName.setStatus("current")


class _Gs2328fSnmpGroupsGroupName_Type(DisplayString):
    """Custom type gs2328fSnmpGroupsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpGroupsGroupName_Type.__name__ = "DisplayString"
_Gs2328fSnmpGroupsGroupName_Object = MibTableColumn
gs2328fSnmpGroupsGroupName = _Gs2328fSnmpGroupsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2, 1, 4),
    _Gs2328fSnmpGroupsGroupName_Type()
)
gs2328fSnmpGroupsGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsGroupName.setStatus("current")


class _Gs2328fSnmpGroupsRowStatus_Type(Integer32):
    """Custom type gs2328fSnmpGroupsRowStatus based on Integer32"""
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


_Gs2328fSnmpGroupsRowStatus_Type.__name__ = "Integer32"
_Gs2328fSnmpGroupsRowStatus_Object = MibTableColumn
gs2328fSnmpGroupsRowStatus = _Gs2328fSnmpGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 5, 2, 1, 5),
    _Gs2328fSnmpGroupsRowStatus_Type()
)
gs2328fSnmpGroupsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpGroupsRowStatus.setStatus("current")
_Gs2328fSnmpViews_ObjectIdentity = ObjectIdentity
gs2328fSnmpViews = _Gs2328fSnmpViews_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6)
)


class _Gs2328fSnmpViewsCreate_Type(Integer32):
    """Custom type gs2328fSnmpViewsCreate based on Integer32"""
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


_Gs2328fSnmpViewsCreate_Type.__name__ = "Integer32"
_Gs2328fSnmpViewsCreate_Object = MibScalar
gs2328fSnmpViewsCreate = _Gs2328fSnmpViewsCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 1),
    _Gs2328fSnmpViewsCreate_Type()
)
gs2328fSnmpViewsCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpViewsCreate.setStatus("current")
_Gs2328fSnmpViewsTable_Object = MibTable
gs2328fSnmpViewsTable = _Gs2328fSnmpViewsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328fSnmpViewsTable.setStatus("current")
_Gs2328fSnmpViewsEntry_Object = MibTableRow
gs2328fSnmpViewsEntry = _Gs2328fSnmpViewsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2, 1)
)
gs2328fSnmpViewsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSnmpViewsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSnmpViewsEntry.setStatus("current")


class _Gs2328fSnmpViewsIndex_Type(Integer32):
    """Custom type gs2328fSnmpViewsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2328fSnmpViewsIndex_Type.__name__ = "Integer32"
_Gs2328fSnmpViewsIndex_Object = MibTableColumn
gs2328fSnmpViewsIndex = _Gs2328fSnmpViewsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2, 1, 1),
    _Gs2328fSnmpViewsIndex_Type()
)
gs2328fSnmpViewsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSnmpViewsIndex.setStatus("current")


class _Gs2328fSnmpViewsName_Type(DisplayString):
    """Custom type gs2328fSnmpViewsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpViewsName_Type.__name__ = "DisplayString"
_Gs2328fSnmpViewsName_Object = MibTableColumn
gs2328fSnmpViewsName = _Gs2328fSnmpViewsName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2, 1, 2),
    _Gs2328fSnmpViewsName_Type()
)
gs2328fSnmpViewsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpViewsName.setStatus("current")


class _Gs2328fSnmpViewsType_Type(Integer32):
    """Custom type gs2328fSnmpViewsType based on Integer32"""
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


_Gs2328fSnmpViewsType_Type.__name__ = "Integer32"
_Gs2328fSnmpViewsType_Object = MibTableColumn
gs2328fSnmpViewsType = _Gs2328fSnmpViewsType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2, 1, 3),
    _Gs2328fSnmpViewsType_Type()
)
gs2328fSnmpViewsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpViewsType.setStatus("current")


class _Gs2328fSnmpViewsOIDSubtree_Type(DisplayString):
    """Custom type gs2328fSnmpViewsOIDSubtree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Gs2328fSnmpViewsOIDSubtree_Type.__name__ = "DisplayString"
_Gs2328fSnmpViewsOIDSubtree_Object = MibTableColumn
gs2328fSnmpViewsOIDSubtree = _Gs2328fSnmpViewsOIDSubtree_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2, 1, 4),
    _Gs2328fSnmpViewsOIDSubtree_Type()
)
gs2328fSnmpViewsOIDSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpViewsOIDSubtree.setStatus("current")


class _Gs2328fSnmpViewsRowStatus_Type(Integer32):
    """Custom type gs2328fSnmpViewsRowStatus based on Integer32"""
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


_Gs2328fSnmpViewsRowStatus_Type.__name__ = "Integer32"
_Gs2328fSnmpViewsRowStatus_Object = MibTableColumn
gs2328fSnmpViewsRowStatus = _Gs2328fSnmpViewsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 6, 2, 1, 5),
    _Gs2328fSnmpViewsRowStatus_Type()
)
gs2328fSnmpViewsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpViewsRowStatus.setStatus("current")
_Gs2328fSnmpAccess_ObjectIdentity = ObjectIdentity
gs2328fSnmpAccess = _Gs2328fSnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7)
)


class _Gs2328fSnmpAccessCreate_Type(Integer32):
    """Custom type gs2328fSnmpAccessCreate based on Integer32"""
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


_Gs2328fSnmpAccessCreate_Type.__name__ = "Integer32"
_Gs2328fSnmpAccessCreate_Object = MibScalar
gs2328fSnmpAccessCreate = _Gs2328fSnmpAccessCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 1),
    _Gs2328fSnmpAccessCreate_Type()
)
gs2328fSnmpAccessCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessCreate.setStatus("current")
_Gs2328fSnmpAccessTable_Object = MibTable
gs2328fSnmpAccessTable = _Gs2328fSnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328fSnmpAccessTable.setStatus("current")
_Gs2328fSnmpAccessEntry_Object = MibTableRow
gs2328fSnmpAccessEntry = _Gs2328fSnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1)
)
gs2328fSnmpAccessEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSnmpAccessEntry.setStatus("current")


class _Gs2328fSnmpAccessIndex_Type(Integer32):
    """Custom type gs2328fSnmpAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Gs2328fSnmpAccessIndex_Type.__name__ = "Integer32"
_Gs2328fSnmpAccessIndex_Object = MibTableColumn
gs2328fSnmpAccessIndex = _Gs2328fSnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 1),
    _Gs2328fSnmpAccessIndex_Type()
)
gs2328fSnmpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessIndex.setStatus("current")


class _Gs2328fSnmpAccessGroupName_Type(DisplayString):
    """Custom type gs2328fSnmpAccessGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpAccessGroupName_Type.__name__ = "DisplayString"
_Gs2328fSnmpAccessGroupName_Object = MibTableColumn
gs2328fSnmpAccessGroupName = _Gs2328fSnmpAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 2),
    _Gs2328fSnmpAccessGroupName_Type()
)
gs2328fSnmpAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessGroupName.setStatus("current")


class _Gs2328fSnmpAccessSecurityModel_Type(Integer32):
    """Custom type gs2328fSnmpAccessSecurityModel based on Integer32"""
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


_Gs2328fSnmpAccessSecurityModel_Type.__name__ = "Integer32"
_Gs2328fSnmpAccessSecurityModel_Object = MibTableColumn
gs2328fSnmpAccessSecurityModel = _Gs2328fSnmpAccessSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 3),
    _Gs2328fSnmpAccessSecurityModel_Type()
)
gs2328fSnmpAccessSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessSecurityModel.setStatus("current")


class _Gs2328fSnmpAccessSecurityLevel_Type(Integer32):
    """Custom type gs2328fSnmpAccessSecurityLevel based on Integer32"""
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


_Gs2328fSnmpAccessSecurityLevel_Type.__name__ = "Integer32"
_Gs2328fSnmpAccessSecurityLevel_Object = MibTableColumn
gs2328fSnmpAccessSecurityLevel = _Gs2328fSnmpAccessSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 4),
    _Gs2328fSnmpAccessSecurityLevel_Type()
)
gs2328fSnmpAccessSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessSecurityLevel.setStatus("current")


class _Gs2328fSnmpAccessReadViewName_Type(DisplayString):
    """Custom type gs2328fSnmpAccessReadViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpAccessReadViewName_Type.__name__ = "DisplayString"
_Gs2328fSnmpAccessReadViewName_Object = MibTableColumn
gs2328fSnmpAccessReadViewName = _Gs2328fSnmpAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 5),
    _Gs2328fSnmpAccessReadViewName_Type()
)
gs2328fSnmpAccessReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessReadViewName.setStatus("current")


class _Gs2328fSnmpAccessWriteViewName_Type(DisplayString):
    """Custom type gs2328fSnmpAccessWriteViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSnmpAccessWriteViewName_Type.__name__ = "DisplayString"
_Gs2328fSnmpAccessWriteViewName_Object = MibTableColumn
gs2328fSnmpAccessWriteViewName = _Gs2328fSnmpAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 6),
    _Gs2328fSnmpAccessWriteViewName_Type()
)
gs2328fSnmpAccessWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessWriteViewName.setStatus("current")


class _Gs2328fSnmpAccessRowStatus_Type(Integer32):
    """Custom type gs2328fSnmpAccessRowStatus based on Integer32"""
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


_Gs2328fSnmpAccessRowStatus_Type.__name__ = "Integer32"
_Gs2328fSnmpAccessRowStatus_Object = MibTableColumn
gs2328fSnmpAccessRowStatus = _Gs2328fSnmpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 1, 6, 7, 2, 1, 7),
    _Gs2328fSnmpAccessRowStatus_Type()
)
gs2328fSnmpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSnmpAccessRowStatus.setStatus("current")
_Gs2328fConfiguration_ObjectIdentity = ObjectIdentity
gs2328fConfiguration = _Gs2328fConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2)
)
_Gs2328fPort_ObjectIdentity = ObjectIdentity
gs2328fPort = _Gs2328fPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1)
)
_Gs2328fPortConfigurationTable_Object = MibTable
gs2328fPortConfigurationTable = _Gs2328fPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1)
)
if mibBuilder.loadTexts:
    gs2328fPortConfigurationTable.setStatus("current")
_Gs2328fPortConfigurationEntry_Object = MibTableRow
gs2328fPortConfigurationEntry = _Gs2328fPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1)
)
gs2328fPortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fPortConfigurationEntry.setStatus("current")


class _Gs2328fPortConfPort_Type(Integer32):
    """Custom type gs2328fPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortConfPort_Type.__name__ = "Integer32"
_Gs2328fPortConfPort_Object = MibTableColumn
gs2328fPortConfPort = _Gs2328fPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 1),
    _Gs2328fPortConfPort_Type()
)
gs2328fPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fPortConfPort.setStatus("current")


class _Gs2328fPortConfPortMedia_Type(DisplayString):
    """Custom type gs2328fPortConfPortMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Gs2328fPortConfPortMedia_Type.__name__ = "DisplayString"
_Gs2328fPortConfPortMedia_Object = MibTableColumn
gs2328fPortConfPortMedia = _Gs2328fPortConfPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 2),
    _Gs2328fPortConfPortMedia_Type()
)
gs2328fPortConfPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortConfPortMedia.setStatus("current")


class _Gs2328fPortConfLink_Type(DisplayString):
    """Custom type gs2328fPortConfLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Gs2328fPortConfLink_Type.__name__ = "DisplayString"
_Gs2328fPortConfLink_Object = MibTableColumn
gs2328fPortConfLink = _Gs2328fPortConfLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 3),
    _Gs2328fPortConfLink_Type()
)
gs2328fPortConfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortConfLink.setStatus("current")


class _Gs2328fPortConfCurrentSpeed_Type(DisplayString):
    """Custom type gs2328fPortConfCurrentSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 12),
    )


_Gs2328fPortConfCurrentSpeed_Type.__name__ = "DisplayString"
_Gs2328fPortConfCurrentSpeed_Object = MibTableColumn
gs2328fPortConfCurrentSpeed = _Gs2328fPortConfCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 4),
    _Gs2328fPortConfCurrentSpeed_Type()
)
gs2328fPortConfCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortConfCurrentSpeed.setStatus("current")


class _Gs2328fPortConfSpeed_Type(Integer32):
    """Custom type gs2328fPortConfSpeed based on Integer32"""
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


_Gs2328fPortConfSpeed_Type.__name__ = "Integer32"
_Gs2328fPortConfSpeed_Object = MibTableColumn
gs2328fPortConfSpeed = _Gs2328fPortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 5),
    _Gs2328fPortConfSpeed_Type()
)
gs2328fPortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortConfSpeed.setStatus("current")


class _Gs2328fPortConfCurrentFlowControlRx_Type(Integer32):
    """Custom type gs2328fPortConfCurrentFlowControlRx based on Integer32"""
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


_Gs2328fPortConfCurrentFlowControlRx_Type.__name__ = "Integer32"
_Gs2328fPortConfCurrentFlowControlRx_Object = MibTableColumn
gs2328fPortConfCurrentFlowControlRx = _Gs2328fPortConfCurrentFlowControlRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 6),
    _Gs2328fPortConfCurrentFlowControlRx_Type()
)
gs2328fPortConfCurrentFlowControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortConfCurrentFlowControlRx.setStatus("current")


class _Gs2328fPortConfCurrentFlowControlTx_Type(Integer32):
    """Custom type gs2328fPortConfCurrentFlowControlTx based on Integer32"""
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


_Gs2328fPortConfCurrentFlowControlTx_Type.__name__ = "Integer32"
_Gs2328fPortConfCurrentFlowControlTx_Object = MibTableColumn
gs2328fPortConfCurrentFlowControlTx = _Gs2328fPortConfCurrentFlowControlTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 7),
    _Gs2328fPortConfCurrentFlowControlTx_Type()
)
gs2328fPortConfCurrentFlowControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortConfCurrentFlowControlTx.setStatus("current")


class _Gs2328fPortConfFlowControl_Type(Integer32):
    """Custom type gs2328fPortConfFlowControl based on Integer32"""
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


_Gs2328fPortConfFlowControl_Type.__name__ = "Integer32"
_Gs2328fPortConfFlowControl_Object = MibTableColumn
gs2328fPortConfFlowControl = _Gs2328fPortConfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 8),
    _Gs2328fPortConfFlowControl_Type()
)
gs2328fPortConfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortConfFlowControl.setStatus("current")


class _Gs2328fPortConfMaxFrameSize_Type(Integer32):
    """Custom type gs2328fPortConfMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Gs2328fPortConfMaxFrameSize_Type.__name__ = "Integer32"
_Gs2328fPortConfMaxFrameSize_Object = MibTableColumn
gs2328fPortConfMaxFrameSize = _Gs2328fPortConfMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 9),
    _Gs2328fPortConfMaxFrameSize_Type()
)
gs2328fPortConfMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortConfMaxFrameSize.setStatus("current")


class _Gs2328fPortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type gs2328fPortConfExcessiveCollisionMode based on Integer32"""
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


_Gs2328fPortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Gs2328fPortConfExcessiveCollisionMode_Object = MibTableColumn
gs2328fPortConfExcessiveCollisionMode = _Gs2328fPortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 10),
    _Gs2328fPortConfExcessiveCollisionMode_Type()
)
gs2328fPortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortConfExcessiveCollisionMode.setStatus("current")


class _Gs2328fPortConfPowerControl_Type(Integer32):
    """Custom type gs2328fPortConfPowerControl based on Integer32"""
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


_Gs2328fPortConfPowerControl_Type.__name__ = "Integer32"
_Gs2328fPortConfPowerControl_Object = MibTableColumn
gs2328fPortConfPowerControl = _Gs2328fPortConfPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 11),
    _Gs2328fPortConfPowerControl_Type()
)
gs2328fPortConfPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortConfPowerControl.setStatus("current")
_Gs2328fPortConfDescription_Type = DisplayString
_Gs2328fPortConfDescription_Object = MibTableColumn
gs2328fPortConfDescription = _Gs2328fPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 1, 1, 12),
    _Gs2328fPortConfDescription_Type()
)
gs2328fPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortConfDescription.setStatus("current")
_Gs2328fPortTrafficStatisticsTable_Object = MibTable
gs2328fPortTrafficStatisticsTable = _Gs2328fPortTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fPortTrafficStatisticsTable.setStatus("current")
_Gs2328fPortTrafficStatisticsEntry_Object = MibTableRow
gs2328fPortTrafficStatisticsEntry = _Gs2328fPortTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1)
)
gs2328fPortTrafficStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fPortTrafficStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328fPortTrafficStatisticsEntry.setStatus("current")


class _Gs2328fPortTrafficStatisticsPort_Type(Integer32):
    """Custom type gs2328fPortTrafficStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortTrafficStatisticsPort_Type.__name__ = "Integer32"
_Gs2328fPortTrafficStatisticsPort_Object = MibTableColumn
gs2328fPortTrafficStatisticsPort = _Gs2328fPortTrafficStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 1),
    _Gs2328fPortTrafficStatisticsPort_Type()
)
gs2328fPortTrafficStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fPortTrafficStatisticsPort.setStatus("current")


class _Gs2328fPortTrafficStatisticsClear_Type(Integer32):
    """Custom type gs2328fPortTrafficStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fPortTrafficStatisticsClear_Type.__name__ = "Integer32"
_Gs2328fPortTrafficStatisticsClear_Object = MibTableColumn
gs2328fPortTrafficStatisticsClear = _Gs2328fPortTrafficStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 2),
    _Gs2328fPortTrafficStatisticsClear_Type()
)
gs2328fPortTrafficStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortTrafficStatisticsClear.setStatus("current")
_Gs2328fPortTrafficRxPackets_Type = Counter64
_Gs2328fPortTrafficRxPackets_Object = MibTableColumn
gs2328fPortTrafficRxPackets = _Gs2328fPortTrafficRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 3),
    _Gs2328fPortTrafficRxPackets_Type()
)
gs2328fPortTrafficRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxPackets.setStatus("current")
_Gs2328fPortTrafficRxOctets_Type = Counter64
_Gs2328fPortTrafficRxOctets_Object = MibTableColumn
gs2328fPortTrafficRxOctets = _Gs2328fPortTrafficRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 4),
    _Gs2328fPortTrafficRxOctets_Type()
)
gs2328fPortTrafficRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxOctets.setStatus("current")
_Gs2328fPortTrafficRxUnicast_Type = Counter64
_Gs2328fPortTrafficRxUnicast_Object = MibTableColumn
gs2328fPortTrafficRxUnicast = _Gs2328fPortTrafficRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 5),
    _Gs2328fPortTrafficRxUnicast_Type()
)
gs2328fPortTrafficRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxUnicast.setStatus("current")
_Gs2328fPortTrafficRxMulticast_Type = Counter64
_Gs2328fPortTrafficRxMulticast_Object = MibTableColumn
gs2328fPortTrafficRxMulticast = _Gs2328fPortTrafficRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 6),
    _Gs2328fPortTrafficRxMulticast_Type()
)
gs2328fPortTrafficRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxMulticast.setStatus("current")
_Gs2328fPortTrafficRxBroadcast_Type = Counter64
_Gs2328fPortTrafficRxBroadcast_Object = MibTableColumn
gs2328fPortTrafficRxBroadcast = _Gs2328fPortTrafficRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 7),
    _Gs2328fPortTrafficRxBroadcast_Type()
)
gs2328fPortTrafficRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxBroadcast.setStatus("current")
_Gs2328fPortTrafficRxPause_Type = Counter64
_Gs2328fPortTrafficRxPause_Object = MibTableColumn
gs2328fPortTrafficRxPause = _Gs2328fPortTrafficRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 8),
    _Gs2328fPortTrafficRxPause_Type()
)
gs2328fPortTrafficRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxPause.setStatus("current")
_Gs2328fPortTrafficRx64Bytes_Type = Counter64
_Gs2328fPortTrafficRx64Bytes_Object = MibTableColumn
gs2328fPortTrafficRx64Bytes = _Gs2328fPortTrafficRx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 9),
    _Gs2328fPortTrafficRx64Bytes_Type()
)
gs2328fPortTrafficRx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRx64Bytes.setStatus("current")
_Gs2328fPortTrafficRx65to127Bytes_Type = Counter64
_Gs2328fPortTrafficRx65to127Bytes_Object = MibTableColumn
gs2328fPortTrafficRx65to127Bytes = _Gs2328fPortTrafficRx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 10),
    _Gs2328fPortTrafficRx65to127Bytes_Type()
)
gs2328fPortTrafficRx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRx65to127Bytes.setStatus("current")
_Gs2328fPortTrafficRx128to255Bytes_Type = Counter64
_Gs2328fPortTrafficRx128to255Bytes_Object = MibTableColumn
gs2328fPortTrafficRx128to255Bytes = _Gs2328fPortTrafficRx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 11),
    _Gs2328fPortTrafficRx128to255Bytes_Type()
)
gs2328fPortTrafficRx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRx128to255Bytes.setStatus("current")
_Gs2328fPortTrafficRx256to511Bytes_Type = Counter64
_Gs2328fPortTrafficRx256to511Bytes_Object = MibTableColumn
gs2328fPortTrafficRx256to511Bytes = _Gs2328fPortTrafficRx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 12),
    _Gs2328fPortTrafficRx256to511Bytes_Type()
)
gs2328fPortTrafficRx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRx256to511Bytes.setStatus("current")
_Gs2328fPortTrafficRx512to1023Bytes_Type = Counter64
_Gs2328fPortTrafficRx512to1023Bytes_Object = MibTableColumn
gs2328fPortTrafficRx512to1023Bytes = _Gs2328fPortTrafficRx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 13),
    _Gs2328fPortTrafficRx512to1023Bytes_Type()
)
gs2328fPortTrafficRx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRx512to1023Bytes.setStatus("current")
_Gs2328fPortTrafficRx1024to1526Bytes_Type = Counter64
_Gs2328fPortTrafficRx1024to1526Bytes_Object = MibTableColumn
gs2328fPortTrafficRx1024to1526Bytes = _Gs2328fPortTrafficRx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 14),
    _Gs2328fPortTrafficRx1024to1526Bytes_Type()
)
gs2328fPortTrafficRx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRx1024to1526Bytes.setStatus("current")
_Gs2328fPortTrafficRxExceecd1527Bytes_Type = Counter64
_Gs2328fPortTrafficRxExceecd1527Bytes_Object = MibTableColumn
gs2328fPortTrafficRxExceecd1527Bytes = _Gs2328fPortTrafficRxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 15),
    _Gs2328fPortTrafficRxExceecd1527Bytes_Type()
)
gs2328fPortTrafficRxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxExceecd1527Bytes.setStatus("current")
_Gs2328fPortTrafficRxQ0_Type = Counter64
_Gs2328fPortTrafficRxQ0_Object = MibTableColumn
gs2328fPortTrafficRxQ0 = _Gs2328fPortTrafficRxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 16),
    _Gs2328fPortTrafficRxQ0_Type()
)
gs2328fPortTrafficRxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ0.setStatus("current")
_Gs2328fPortTrafficRxQ1_Type = Counter64
_Gs2328fPortTrafficRxQ1_Object = MibTableColumn
gs2328fPortTrafficRxQ1 = _Gs2328fPortTrafficRxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 17),
    _Gs2328fPortTrafficRxQ1_Type()
)
gs2328fPortTrafficRxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ1.setStatus("current")
_Gs2328fPortTrafficRxQ2_Type = Counter64
_Gs2328fPortTrafficRxQ2_Object = MibTableColumn
gs2328fPortTrafficRxQ2 = _Gs2328fPortTrafficRxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 18),
    _Gs2328fPortTrafficRxQ2_Type()
)
gs2328fPortTrafficRxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ2.setStatus("current")
_Gs2328fPortTrafficRxQ3_Type = Counter64
_Gs2328fPortTrafficRxQ3_Object = MibTableColumn
gs2328fPortTrafficRxQ3 = _Gs2328fPortTrafficRxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 19),
    _Gs2328fPortTrafficRxQ3_Type()
)
gs2328fPortTrafficRxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ3.setStatus("current")
_Gs2328fPortTrafficRxQ4_Type = Counter64
_Gs2328fPortTrafficRxQ4_Object = MibTableColumn
gs2328fPortTrafficRxQ4 = _Gs2328fPortTrafficRxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 20),
    _Gs2328fPortTrafficRxQ4_Type()
)
gs2328fPortTrafficRxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ4.setStatus("current")
_Gs2328fPortTrafficRxQ5_Type = Counter64
_Gs2328fPortTrafficRxQ5_Object = MibTableColumn
gs2328fPortTrafficRxQ5 = _Gs2328fPortTrafficRxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 21),
    _Gs2328fPortTrafficRxQ5_Type()
)
gs2328fPortTrafficRxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ5.setStatus("current")
_Gs2328fPortTrafficRxQ6_Type = Counter64
_Gs2328fPortTrafficRxQ6_Object = MibTableColumn
gs2328fPortTrafficRxQ6 = _Gs2328fPortTrafficRxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 22),
    _Gs2328fPortTrafficRxQ6_Type()
)
gs2328fPortTrafficRxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ6.setStatus("current")
_Gs2328fPortTrafficRxQ7_Type = Counter64
_Gs2328fPortTrafficRxQ7_Object = MibTableColumn
gs2328fPortTrafficRxQ7 = _Gs2328fPortTrafficRxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 23),
    _Gs2328fPortTrafficRxQ7_Type()
)
gs2328fPortTrafficRxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxQ7.setStatus("current")
_Gs2328fPortTrafficRxDrops_Type = Counter64
_Gs2328fPortTrafficRxDrops_Object = MibTableColumn
gs2328fPortTrafficRxDrops = _Gs2328fPortTrafficRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 24),
    _Gs2328fPortTrafficRxDrops_Type()
)
gs2328fPortTrafficRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxDrops.setStatus("current")
_Gs2328fPortTrafficRxCRCorAlignment_Type = Counter64
_Gs2328fPortTrafficRxCRCorAlignment_Object = MibTableColumn
gs2328fPortTrafficRxCRCorAlignment = _Gs2328fPortTrafficRxCRCorAlignment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 25),
    _Gs2328fPortTrafficRxCRCorAlignment_Type()
)
gs2328fPortTrafficRxCRCorAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxCRCorAlignment.setStatus("current")
_Gs2328fPortTrafficRxUndersize_Type = Counter64
_Gs2328fPortTrafficRxUndersize_Object = MibTableColumn
gs2328fPortTrafficRxUndersize = _Gs2328fPortTrafficRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 26),
    _Gs2328fPortTrafficRxUndersize_Type()
)
gs2328fPortTrafficRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxUndersize.setStatus("current")
_Gs2328fPortTrafficRxOversize_Type = Counter64
_Gs2328fPortTrafficRxOversize_Object = MibTableColumn
gs2328fPortTrafficRxOversize = _Gs2328fPortTrafficRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 27),
    _Gs2328fPortTrafficRxOversize_Type()
)
gs2328fPortTrafficRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxOversize.setStatus("current")
_Gs2328fPortTrafficRxFragments_Type = Counter64
_Gs2328fPortTrafficRxFragments_Object = MibTableColumn
gs2328fPortTrafficRxFragments = _Gs2328fPortTrafficRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 28),
    _Gs2328fPortTrafficRxFragments_Type()
)
gs2328fPortTrafficRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxFragments.setStatus("current")
_Gs2328fPortTrafficRxJabber_Type = Counter64
_Gs2328fPortTrafficRxJabber_Object = MibTableColumn
gs2328fPortTrafficRxJabber = _Gs2328fPortTrafficRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 29),
    _Gs2328fPortTrafficRxJabber_Type()
)
gs2328fPortTrafficRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxJabber.setStatus("current")
_Gs2328fPortTrafficRxFiltered_Type = Counter64
_Gs2328fPortTrafficRxFiltered_Object = MibTableColumn
gs2328fPortTrafficRxFiltered = _Gs2328fPortTrafficRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 30),
    _Gs2328fPortTrafficRxFiltered_Type()
)
gs2328fPortTrafficRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficRxFiltered.setStatus("current")
_Gs2328fPortTrafficTxPackets_Type = Counter64
_Gs2328fPortTrafficTxPackets_Object = MibTableColumn
gs2328fPortTrafficTxPackets = _Gs2328fPortTrafficTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 31),
    _Gs2328fPortTrafficTxPackets_Type()
)
gs2328fPortTrafficTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxPackets.setStatus("current")
_Gs2328fPortTrafficTxOctets_Type = Counter64
_Gs2328fPortTrafficTxOctets_Object = MibTableColumn
gs2328fPortTrafficTxOctets = _Gs2328fPortTrafficTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 32),
    _Gs2328fPortTrafficTxOctets_Type()
)
gs2328fPortTrafficTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxOctets.setStatus("current")
_Gs2328fPortTrafficTxUnicast_Type = Counter64
_Gs2328fPortTrafficTxUnicast_Object = MibTableColumn
gs2328fPortTrafficTxUnicast = _Gs2328fPortTrafficTxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 33),
    _Gs2328fPortTrafficTxUnicast_Type()
)
gs2328fPortTrafficTxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxUnicast.setStatus("current")
_Gs2328fPortTrafficTxMulticast_Type = Counter64
_Gs2328fPortTrafficTxMulticast_Object = MibTableColumn
gs2328fPortTrafficTxMulticast = _Gs2328fPortTrafficTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 34),
    _Gs2328fPortTrafficTxMulticast_Type()
)
gs2328fPortTrafficTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxMulticast.setStatus("current")
_Gs2328fPortTrafficTxBroadcast_Type = Counter64
_Gs2328fPortTrafficTxBroadcast_Object = MibTableColumn
gs2328fPortTrafficTxBroadcast = _Gs2328fPortTrafficTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 35),
    _Gs2328fPortTrafficTxBroadcast_Type()
)
gs2328fPortTrafficTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxBroadcast.setStatus("current")
_Gs2328fPortTrafficTxPause_Type = Counter64
_Gs2328fPortTrafficTxPause_Object = MibTableColumn
gs2328fPortTrafficTxPause = _Gs2328fPortTrafficTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 36),
    _Gs2328fPortTrafficTxPause_Type()
)
gs2328fPortTrafficTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxPause.setStatus("current")
_Gs2328fPortTrafficTx64Bytes_Type = Counter64
_Gs2328fPortTrafficTx64Bytes_Object = MibTableColumn
gs2328fPortTrafficTx64Bytes = _Gs2328fPortTrafficTx64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 37),
    _Gs2328fPortTrafficTx64Bytes_Type()
)
gs2328fPortTrafficTx64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTx64Bytes.setStatus("current")
_Gs2328fPortTrafficTx65to127Bytes_Type = Counter64
_Gs2328fPortTrafficTx65to127Bytes_Object = MibTableColumn
gs2328fPortTrafficTx65to127Bytes = _Gs2328fPortTrafficTx65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 38),
    _Gs2328fPortTrafficTx65to127Bytes_Type()
)
gs2328fPortTrafficTx65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTx65to127Bytes.setStatus("current")
_Gs2328fPortTrafficTx128to255Bytes_Type = Counter64
_Gs2328fPortTrafficTx128to255Bytes_Object = MibTableColumn
gs2328fPortTrafficTx128to255Bytes = _Gs2328fPortTrafficTx128to255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 39),
    _Gs2328fPortTrafficTx128to255Bytes_Type()
)
gs2328fPortTrafficTx128to255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTx128to255Bytes.setStatus("current")
_Gs2328fPortTrafficTx256to511Bytes_Type = Counter64
_Gs2328fPortTrafficTx256to511Bytes_Object = MibTableColumn
gs2328fPortTrafficTx256to511Bytes = _Gs2328fPortTrafficTx256to511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 40),
    _Gs2328fPortTrafficTx256to511Bytes_Type()
)
gs2328fPortTrafficTx256to511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTx256to511Bytes.setStatus("current")
_Gs2328fPortTrafficTx512to1023Bytes_Type = Counter64
_Gs2328fPortTrafficTx512to1023Bytes_Object = MibTableColumn
gs2328fPortTrafficTx512to1023Bytes = _Gs2328fPortTrafficTx512to1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 41),
    _Gs2328fPortTrafficTx512to1023Bytes_Type()
)
gs2328fPortTrafficTx512to1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTx512to1023Bytes.setStatus("current")
_Gs2328fPortTrafficTx1024to1526Bytes_Type = Counter64
_Gs2328fPortTrafficTx1024to1526Bytes_Object = MibTableColumn
gs2328fPortTrafficTx1024to1526Bytes = _Gs2328fPortTrafficTx1024to1526Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 42),
    _Gs2328fPortTrafficTx1024to1526Bytes_Type()
)
gs2328fPortTrafficTx1024to1526Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTx1024to1526Bytes.setStatus("current")
_Gs2328fPortTrafficTxExceecd1527Bytes_Type = Counter64
_Gs2328fPortTrafficTxExceecd1527Bytes_Object = MibTableColumn
gs2328fPortTrafficTxExceecd1527Bytes = _Gs2328fPortTrafficTxExceecd1527Bytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 43),
    _Gs2328fPortTrafficTxExceecd1527Bytes_Type()
)
gs2328fPortTrafficTxExceecd1527Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxExceecd1527Bytes.setStatus("current")
_Gs2328fPortTrafficTxQ0_Type = Counter64
_Gs2328fPortTrafficTxQ0_Object = MibTableColumn
gs2328fPortTrafficTxQ0 = _Gs2328fPortTrafficTxQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 44),
    _Gs2328fPortTrafficTxQ0_Type()
)
gs2328fPortTrafficTxQ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ0.setStatus("current")
_Gs2328fPortTrafficTxQ1_Type = Counter64
_Gs2328fPortTrafficTxQ1_Object = MibTableColumn
gs2328fPortTrafficTxQ1 = _Gs2328fPortTrafficTxQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 45),
    _Gs2328fPortTrafficTxQ1_Type()
)
gs2328fPortTrafficTxQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ1.setStatus("current")
_Gs2328fPortTrafficTxQ2_Type = Counter64
_Gs2328fPortTrafficTxQ2_Object = MibTableColumn
gs2328fPortTrafficTxQ2 = _Gs2328fPortTrafficTxQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 46),
    _Gs2328fPortTrafficTxQ2_Type()
)
gs2328fPortTrafficTxQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ2.setStatus("current")
_Gs2328fPortTrafficTxQ3_Type = Counter64
_Gs2328fPortTrafficTxQ3_Object = MibTableColumn
gs2328fPortTrafficTxQ3 = _Gs2328fPortTrafficTxQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 47),
    _Gs2328fPortTrafficTxQ3_Type()
)
gs2328fPortTrafficTxQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ3.setStatus("current")
_Gs2328fPortTrafficTxQ4_Type = Counter64
_Gs2328fPortTrafficTxQ4_Object = MibTableColumn
gs2328fPortTrafficTxQ4 = _Gs2328fPortTrafficTxQ4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 48),
    _Gs2328fPortTrafficTxQ4_Type()
)
gs2328fPortTrafficTxQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ4.setStatus("current")
_Gs2328fPortTrafficTxQ5_Type = Counter64
_Gs2328fPortTrafficTxQ5_Object = MibTableColumn
gs2328fPortTrafficTxQ5 = _Gs2328fPortTrafficTxQ5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 49),
    _Gs2328fPortTrafficTxQ5_Type()
)
gs2328fPortTrafficTxQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ5.setStatus("current")
_Gs2328fPortTrafficTxQ6_Type = Counter64
_Gs2328fPortTrafficTxQ6_Object = MibTableColumn
gs2328fPortTrafficTxQ6 = _Gs2328fPortTrafficTxQ6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 50),
    _Gs2328fPortTrafficTxQ6_Type()
)
gs2328fPortTrafficTxQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ6.setStatus("current")
_Gs2328fPortTrafficTxQ7_Type = Counter64
_Gs2328fPortTrafficTxQ7_Object = MibTableColumn
gs2328fPortTrafficTxQ7 = _Gs2328fPortTrafficTxQ7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 51),
    _Gs2328fPortTrafficTxQ7_Type()
)
gs2328fPortTrafficTxQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxQ7.setStatus("current")
_Gs2328fPortTrafficTxDrops_Type = Counter64
_Gs2328fPortTrafficTxDrops_Object = MibTableColumn
gs2328fPortTrafficTxDrops = _Gs2328fPortTrafficTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 52),
    _Gs2328fPortTrafficTxDrops_Type()
)
gs2328fPortTrafficTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxDrops.setStatus("current")
_Gs2328fPortTrafficTxLateOrExcColl_Type = Counter64
_Gs2328fPortTrafficTxLateOrExcColl_Object = MibTableColumn
gs2328fPortTrafficTxLateOrExcColl = _Gs2328fPortTrafficTxLateOrExcColl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 2, 1, 53),
    _Gs2328fPortTrafficTxLateOrExcColl_Type()
)
gs2328fPortTrafficTxLateOrExcColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortTrafficTxLateOrExcColl.setStatus("current")
_Gs2328fPortQoSStatistics_ObjectIdentity = ObjectIdentity
gs2328fPortQoSStatistics = _Gs2328fPortQoSStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3)
)


class _Gs2328fPortQoSStatisticsClear_Type(Integer32):
    """Custom type gs2328fPortQoSStatisticsClear based on Integer32"""
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


_Gs2328fPortQoSStatisticsClear_Type.__name__ = "Integer32"
_Gs2328fPortQoSStatisticsClear_Object = MibScalar
gs2328fPortQoSStatisticsClear = _Gs2328fPortQoSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 1),
    _Gs2328fPortQoSStatisticsClear_Type()
)
gs2328fPortQoSStatisticsClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSStatisticsClear.setStatus("current")
_Gs2328fPortQoSStatisticsTable_Object = MibTable
gs2328fPortQoSStatisticsTable = _Gs2328fPortQoSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fPortQoSStatisticsTable.setStatus("current")
_Gs2328fPortQoSStatisticsEntry_Object = MibTableRow
gs2328fPortQoSStatisticsEntry = _Gs2328fPortQoSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1)
)
gs2328fPortQoSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fPortQoSStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328fPortQoSStatisticsEntry.setStatus("current")


class _Gs2328fPortQoSStatisticsPort_Type(Integer32):
    """Custom type gs2328fPortQoSStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortQoSStatisticsPort_Type.__name__ = "Integer32"
_Gs2328fPortQoSStatisticsPort_Object = MibTableColumn
gs2328fPortQoSStatisticsPort = _Gs2328fPortQoSStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 1),
    _Gs2328fPortQoSStatisticsPort_Type()
)
gs2328fPortQoSStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fPortQoSStatisticsPort.setStatus("current")
_Gs2328fPortQoSQ0Rx_Type = Counter64
_Gs2328fPortQoSQ0Rx_Object = MibTableColumn
gs2328fPortQoSQ0Rx = _Gs2328fPortQoSQ0Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 2),
    _Gs2328fPortQoSQ0Rx_Type()
)
gs2328fPortQoSQ0Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ0Rx.setStatus("current")
_Gs2328fPortQoSQ0Tx_Type = Counter64
_Gs2328fPortQoSQ0Tx_Object = MibTableColumn
gs2328fPortQoSQ0Tx = _Gs2328fPortQoSQ0Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 3),
    _Gs2328fPortQoSQ0Tx_Type()
)
gs2328fPortQoSQ0Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ0Tx.setStatus("current")
_Gs2328fPortQoSQ1Rx_Type = Counter64
_Gs2328fPortQoSQ1Rx_Object = MibTableColumn
gs2328fPortQoSQ1Rx = _Gs2328fPortQoSQ1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 4),
    _Gs2328fPortQoSQ1Rx_Type()
)
gs2328fPortQoSQ1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ1Rx.setStatus("current")
_Gs2328fPortQoSQ1Tx_Type = Counter64
_Gs2328fPortQoSQ1Tx_Object = MibTableColumn
gs2328fPortQoSQ1Tx = _Gs2328fPortQoSQ1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 5),
    _Gs2328fPortQoSQ1Tx_Type()
)
gs2328fPortQoSQ1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ1Tx.setStatus("current")
_Gs2328fPortQoSQ2Rx_Type = Counter64
_Gs2328fPortQoSQ2Rx_Object = MibTableColumn
gs2328fPortQoSQ2Rx = _Gs2328fPortQoSQ2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 6),
    _Gs2328fPortQoSQ2Rx_Type()
)
gs2328fPortQoSQ2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ2Rx.setStatus("current")
_Gs2328fPortQoSQ2Tx_Type = Counter64
_Gs2328fPortQoSQ2Tx_Object = MibTableColumn
gs2328fPortQoSQ2Tx = _Gs2328fPortQoSQ2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 7),
    _Gs2328fPortQoSQ2Tx_Type()
)
gs2328fPortQoSQ2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ2Tx.setStatus("current")
_Gs2328fPortQoSQ3Rx_Type = Counter64
_Gs2328fPortQoSQ3Rx_Object = MibTableColumn
gs2328fPortQoSQ3Rx = _Gs2328fPortQoSQ3Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 8),
    _Gs2328fPortQoSQ3Rx_Type()
)
gs2328fPortQoSQ3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ3Rx.setStatus("current")
_Gs2328fPortQoSQ3Tx_Type = Counter64
_Gs2328fPortQoSQ3Tx_Object = MibTableColumn
gs2328fPortQoSQ3Tx = _Gs2328fPortQoSQ3Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 9),
    _Gs2328fPortQoSQ3Tx_Type()
)
gs2328fPortQoSQ3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ3Tx.setStatus("current")
_Gs2328fPortQoSQ4Rx_Type = Counter64
_Gs2328fPortQoSQ4Rx_Object = MibTableColumn
gs2328fPortQoSQ4Rx = _Gs2328fPortQoSQ4Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 10),
    _Gs2328fPortQoSQ4Rx_Type()
)
gs2328fPortQoSQ4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ4Rx.setStatus("current")
_Gs2328fPortQoSQ4Tx_Type = Counter64
_Gs2328fPortQoSQ4Tx_Object = MibTableColumn
gs2328fPortQoSQ4Tx = _Gs2328fPortQoSQ4Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 11),
    _Gs2328fPortQoSQ4Tx_Type()
)
gs2328fPortQoSQ4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ4Tx.setStatus("current")
_Gs2328fPortQoSQ5Rx_Type = Counter64
_Gs2328fPortQoSQ5Rx_Object = MibTableColumn
gs2328fPortQoSQ5Rx = _Gs2328fPortQoSQ5Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 12),
    _Gs2328fPortQoSQ5Rx_Type()
)
gs2328fPortQoSQ5Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ5Rx.setStatus("current")
_Gs2328fPortQoSQ5Tx_Type = Counter64
_Gs2328fPortQoSQ5Tx_Object = MibTableColumn
gs2328fPortQoSQ5Tx = _Gs2328fPortQoSQ5Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 13),
    _Gs2328fPortQoSQ5Tx_Type()
)
gs2328fPortQoSQ5Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ5Tx.setStatus("current")
_Gs2328fPortQoSQ6Rx_Type = Counter64
_Gs2328fPortQoSQ6Rx_Object = MibTableColumn
gs2328fPortQoSQ6Rx = _Gs2328fPortQoSQ6Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 14),
    _Gs2328fPortQoSQ6Rx_Type()
)
gs2328fPortQoSQ6Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ6Rx.setStatus("current")
_Gs2328fPortQoSQ6Tx_Type = Counter64
_Gs2328fPortQoSQ6Tx_Object = MibTableColumn
gs2328fPortQoSQ6Tx = _Gs2328fPortQoSQ6Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 15),
    _Gs2328fPortQoSQ6Tx_Type()
)
gs2328fPortQoSQ6Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ6Tx.setStatus("current")
_Gs2328fPortQoSQ7Rx_Type = Counter64
_Gs2328fPortQoSQ7Rx_Object = MibTableColumn
gs2328fPortQoSQ7Rx = _Gs2328fPortQoSQ7Rx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 16),
    _Gs2328fPortQoSQ7Rx_Type()
)
gs2328fPortQoSQ7Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ7Rx.setStatus("current")
_Gs2328fPortQoSQ7Tx_Type = Counter64
_Gs2328fPortQoSQ7Tx_Object = MibTableColumn
gs2328fPortQoSQ7Tx = _Gs2328fPortQoSQ7Tx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 3, 2, 1, 17),
    _Gs2328fPortQoSQ7Tx_Type()
)
gs2328fPortQoSQ7Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortQoSQ7Tx.setStatus("current")
_Gs2328fSFPInfoTable_Object = MibTable
gs2328fSFPInfoTable = _Gs2328fSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4)
)
if mibBuilder.loadTexts:
    gs2328fSFPInfoTable.setStatus("current")
_Gs2328fSFPInfoEntry_Object = MibTableRow
gs2328fSFPInfoEntry = _Gs2328fSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1)
)
gs2328fSFPInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSFPInfoEntry.setStatus("current")


class _Gs2328fSFPInfoIndex_Type(Integer32):
    """Custom type gs2328fSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSFPInfoIndex_Type.__name__ = "Integer32"
_Gs2328fSFPInfoIndex_Object = MibTableColumn
gs2328fSFPInfoIndex = _Gs2328fSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 1),
    _Gs2328fSFPInfoIndex_Type()
)
gs2328fSFPInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSFPInfoIndex.setStatus("current")
_Gs2328fSFPInfoPort_Type = DisplayString
_Gs2328fSFPInfoPort_Object = MibTableColumn
gs2328fSFPInfoPort = _Gs2328fSFPInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 2),
    _Gs2328fSFPInfoPort_Type()
)
gs2328fSFPInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPInfoPort.setStatus("current")
_Gs2328fSFPConnectorType_Type = DisplayString
_Gs2328fSFPConnectorType_Object = MibTableColumn
gs2328fSFPConnectorType = _Gs2328fSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 3),
    _Gs2328fSFPConnectorType_Type()
)
gs2328fSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPConnectorType.setStatus("current")
_Gs2328fSFPFiberType_Type = DisplayString
_Gs2328fSFPFiberType_Object = MibTableColumn
gs2328fSFPFiberType = _Gs2328fSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 4),
    _Gs2328fSFPFiberType_Type()
)
gs2328fSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPFiberType.setStatus("current")
_Gs2328fSFPTxCentralWavelength_Type = DisplayString
_Gs2328fSFPTxCentralWavelength_Object = MibTableColumn
gs2328fSFPTxCentralWavelength = _Gs2328fSFPTxCentralWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 5),
    _Gs2328fSFPTxCentralWavelength_Type()
)
gs2328fSFPTxCentralWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPTxCentralWavelength.setStatus("current")
_Gs2328fSFPBaudRate_Type = DisplayString
_Gs2328fSFPBaudRate_Object = MibTableColumn
gs2328fSFPBaudRate = _Gs2328fSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 6),
    _Gs2328fSFPBaudRate_Type()
)
gs2328fSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPBaudRate.setStatus("current")
_Gs2328fSFPVendorOUI_Type = DisplayString
_Gs2328fSFPVendorOUI_Object = MibTableColumn
gs2328fSFPVendorOUI = _Gs2328fSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 7),
    _Gs2328fSFPVendorOUI_Type()
)
gs2328fSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPVendorOUI.setStatus("current")
_Gs2328fSFPVendorName_Type = DisplayString
_Gs2328fSFPVendorName_Object = MibTableColumn
gs2328fSFPVendorName = _Gs2328fSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 8),
    _Gs2328fSFPVendorName_Type()
)
gs2328fSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPVendorName.setStatus("current")
_Gs2328fSFPVendorPN_Type = DisplayString
_Gs2328fSFPVendorPN_Object = MibTableColumn
gs2328fSFPVendorPN = _Gs2328fSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 9),
    _Gs2328fSFPVendorPN_Type()
)
gs2328fSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPVendorPN.setStatus("current")
_Gs2328fSFPVendorRev_Type = DisplayString
_Gs2328fSFPVendorRev_Object = MibTableColumn
gs2328fSFPVendorRev = _Gs2328fSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 10),
    _Gs2328fSFPVendorRev_Type()
)
gs2328fSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPVendorRev.setStatus("current")
_Gs2328fSFPVendorSN_Type = DisplayString
_Gs2328fSFPVendorSN_Object = MibTableColumn
gs2328fSFPVendorSN = _Gs2328fSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 11),
    _Gs2328fSFPVendorSN_Type()
)
gs2328fSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPVendorSN.setStatus("current")
_Gs2328fSFPDateCode_Type = DisplayString
_Gs2328fSFPDateCode_Object = MibTableColumn
gs2328fSFPDateCode = _Gs2328fSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 12),
    _Gs2328fSFPDateCode_Type()
)
gs2328fSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPDateCode.setStatus("current")
_Gs2328fSFPTemperature_Type = DisplayString
_Gs2328fSFPTemperature_Object = MibTableColumn
gs2328fSFPTemperature = _Gs2328fSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 13),
    _Gs2328fSFPTemperature_Type()
)
gs2328fSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPTemperature.setStatus("current")
_Gs2328fSFPVcc_Type = DisplayString
_Gs2328fSFPVcc_Object = MibTableColumn
gs2328fSFPVcc = _Gs2328fSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 14),
    _Gs2328fSFPVcc_Type()
)
gs2328fSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPVcc.setStatus("current")
_Gs2328fSFPMon1Bias_Type = DisplayString
_Gs2328fSFPMon1Bias_Object = MibTableColumn
gs2328fSFPMon1Bias = _Gs2328fSFPMon1Bias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 15),
    _Gs2328fSFPMon1Bias_Type()
)
gs2328fSFPMon1Bias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPMon1Bias.setStatus("current")
_Gs2328fSFPMon2TxPWR_Type = DisplayString
_Gs2328fSFPMon2TxPWR_Object = MibTableColumn
gs2328fSFPMon2TxPWR = _Gs2328fSFPMon2TxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 16),
    _Gs2328fSFPMon2TxPWR_Type()
)
gs2328fSFPMon2TxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPMon2TxPWR.setStatus("current")
_Gs2328fSFPMon3RxPWR_Type = DisplayString
_Gs2328fSFPMon3RxPWR_Object = MibTableColumn
gs2328fSFPMon3RxPWR = _Gs2328fSFPMon3RxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1, 4, 1, 17),
    _Gs2328fSFPMon3RxPWR_Type()
)
gs2328fSFPMon3RxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSFPMon3RxPWR.setStatus("current")
_Gs2328fVoiceVLAN_ObjectIdentity = ObjectIdentity
gs2328fVoiceVLAN = _Gs2328fVoiceVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2)
)
_Gs2328fVoiceVLANConf_ObjectIdentity = ObjectIdentity
gs2328fVoiceVLANConf = _Gs2328fVoiceVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1)
)


class _Gs2328fVoiceVLANMode_Type(Integer32):
    """Custom type gs2328fVoiceVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fVoiceVLANMode_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANMode_Object = MibScalar
gs2328fVoiceVLANMode = _Gs2328fVoiceVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 1),
    _Gs2328fVoiceVLANMode_Type()
)
gs2328fVoiceVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANMode.setStatus("current")


class _Gs2328fVoiceVLANVLANId_Type(Integer32):
    """Custom type gs2328fVoiceVLANVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fVoiceVLANVLANId_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANVLANId_Object = MibScalar
gs2328fVoiceVLANVLANId = _Gs2328fVoiceVLANVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 2),
    _Gs2328fVoiceVLANVLANId_Type()
)
gs2328fVoiceVLANVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANVLANId.setStatus("current")


class _Gs2328fVoiceVLANAgingTime_Type(Integer32):
    """Custom type gs2328fVoiceVLANAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2328fVoiceVLANAgingTime_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANAgingTime_Object = MibScalar
gs2328fVoiceVLANAgingTime = _Gs2328fVoiceVLANAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 3),
    _Gs2328fVoiceVLANAgingTime_Type()
)
gs2328fVoiceVLANAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANAgingTime.setStatus("current")


class _Gs2328fVoiceVLANTrafficClass_Type(Integer32):
    """Custom type gs2328fVoiceVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fVoiceVLANTrafficClass_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANTrafficClass_Object = MibScalar
gs2328fVoiceVLANTrafficClass = _Gs2328fVoiceVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 4),
    _Gs2328fVoiceVLANTrafficClass_Type()
)
gs2328fVoiceVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANTrafficClass.setStatus("current")
_Gs2328fVoiceVLANPortTable_Object = MibTable
gs2328fVoiceVLANPortTable = _Gs2328fVoiceVLANPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPortTable.setStatus("current")
_Gs2328fVoiceVLANPortEntry_Object = MibTableRow
gs2328fVoiceVLANPortEntry = _Gs2328fVoiceVLANPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5, 1)
)
gs2328fVoiceVLANPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fVoiceVLANPort"),
)
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPortEntry.setStatus("current")


class _Gs2328fVoiceVLANPort_Type(Integer32):
    """Custom type gs2328fVoiceVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fVoiceVLANPort_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANPort_Object = MibTableColumn
gs2328fVoiceVLANPort = _Gs2328fVoiceVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5, 1, 1),
    _Gs2328fVoiceVLANPort_Type()
)
gs2328fVoiceVLANPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPort.setStatus("current")


class _Gs2328fVoiceVLANPortMode_Type(Integer32):
    """Custom type gs2328fVoiceVLANPortMode based on Integer32"""
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


_Gs2328fVoiceVLANPortMode_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANPortMode_Object = MibTableColumn
gs2328fVoiceVLANPortMode = _Gs2328fVoiceVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5, 1, 2),
    _Gs2328fVoiceVLANPortMode_Type()
)
gs2328fVoiceVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPortMode.setStatus("current")


class _Gs2328fVoiceVLANPortSecurity_Type(Integer32):
    """Custom type gs2328fVoiceVLANPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fVoiceVLANPortSecurity_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANPortSecurity_Object = MibTableColumn
gs2328fVoiceVLANPortSecurity = _Gs2328fVoiceVLANPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5, 1, 3),
    _Gs2328fVoiceVLANPortSecurity_Type()
)
gs2328fVoiceVLANPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPortSecurity.setStatus("current")


class _Gs2328fVoiceVLANPortDiscoveryProtocol_Type(Integer32):
    """Custom type gs2328fVoiceVLANPortDiscoveryProtocol based on Integer32"""
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


_Gs2328fVoiceVLANPortDiscoveryProtocol_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANPortDiscoveryProtocol_Object = MibTableColumn
gs2328fVoiceVLANPortDiscoveryProtocol = _Gs2328fVoiceVLANPortDiscoveryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5, 1, 4),
    _Gs2328fVoiceVLANPortDiscoveryProtocol_Type()
)
gs2328fVoiceVLANPortDiscoveryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANPortDiscoveryProtocol.setStatus("current")


class _Gs2328fVoiceVLANSkipNAS_Type(Integer32):
    """Custom type gs2328fVoiceVLANSkipNAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fVoiceVLANSkipNAS_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANSkipNAS_Object = MibScalar
gs2328fVoiceVLANSkipNAS = _Gs2328fVoiceVLANSkipNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 1, 5, 1, 5),
    _Gs2328fVoiceVLANSkipNAS_Type()
)
gs2328fVoiceVLANSkipNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANSkipNAS.setStatus("current")
_Gs2328fVoiceVLANOUI_ObjectIdentity = ObjectIdentity
gs2328fVoiceVLANOUI = _Gs2328fVoiceVLANOUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2)
)


class _Gs2328fVoiceVLANOUICreate_Type(Integer32):
    """Custom type gs2328fVoiceVLANOUICreate based on Integer32"""
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


_Gs2328fVoiceVLANOUICreate_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANOUICreate_Object = MibScalar
gs2328fVoiceVLANOUICreate = _Gs2328fVoiceVLANOUICreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 1),
    _Gs2328fVoiceVLANOUICreate_Type()
)
gs2328fVoiceVLANOUICreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANOUICreate.setStatus("current")
_Gs2328fVoiceVLANOUITable_Object = MibTable
gs2328fVoiceVLANOUITable = _Gs2328fVoiceVLANOUITable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fVoiceVLANOUITable.setStatus("current")
_Gs2328fVoiceVLANOUIEntry_Object = MibTableRow
gs2328fVoiceVLANOUIEntry = _Gs2328fVoiceVLANOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 2, 1)
)
gs2328fVoiceVLANOUIEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fVoiceVLANOUIIndex"),
)
if mibBuilder.loadTexts:
    gs2328fVoiceVLANOUIEntry.setStatus("current")


class _Gs2328fVoiceVLANOUIIndex_Type(Integer32):
    """Custom type gs2328fVoiceVLANOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2328fVoiceVLANOUIIndex_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANOUIIndex_Object = MibTableColumn
gs2328fVoiceVLANOUIIndex = _Gs2328fVoiceVLANOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 2, 1, 1),
    _Gs2328fVoiceVLANOUIIndex_Type()
)
gs2328fVoiceVLANOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANOUIIndex.setStatus("current")


class _Gs2328fVoiceVLANTelephonyOUI_Type(OctetString):
    """Custom type gs2328fVoiceVLANTelephonyOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fVoiceVLANTelephonyOUI_Type.__name__ = "OctetString"
_Gs2328fVoiceVLANTelephonyOUI_Object = MibTableColumn
gs2328fVoiceVLANTelephonyOUI = _Gs2328fVoiceVLANTelephonyOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 2, 1, 2),
    _Gs2328fVoiceVLANTelephonyOUI_Type()
)
gs2328fVoiceVLANTelephonyOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANTelephonyOUI.setStatus("current")


class _Gs2328fVoiceVLANDescription_Type(DisplayString):
    """Custom type gs2328fVoiceVLANDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fVoiceVLANDescription_Type.__name__ = "DisplayString"
_Gs2328fVoiceVLANDescription_Object = MibTableColumn
gs2328fVoiceVLANDescription = _Gs2328fVoiceVLANDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 2, 1, 3),
    _Gs2328fVoiceVLANDescription_Type()
)
gs2328fVoiceVLANDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANDescription.setStatus("current")


class _Gs2328fVoiceVLANOUIRowStatus_Type(Integer32):
    """Custom type gs2328fVoiceVLANOUIRowStatus based on Integer32"""
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


_Gs2328fVoiceVLANOUIRowStatus_Type.__name__ = "Integer32"
_Gs2328fVoiceVLANOUIRowStatus_Object = MibTableColumn
gs2328fVoiceVLANOUIRowStatus = _Gs2328fVoiceVLANOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 2, 2, 2, 1, 4),
    _Gs2328fVoiceVLANOUIRowStatus_Type()
)
gs2328fVoiceVLANOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVoiceVLANOUIRowStatus.setStatus("current")
_Gs2328fGARP_ObjectIdentity = ObjectIdentity
gs2328fGARP = _Gs2328fGARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3)
)
_Gs2328fGARPConfTable_Object = MibTable
gs2328fGARPConfTable = _Gs2328fGARPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gs2328fGARPConfTable.setStatus("current")
_Gs2328fGARPConfEntry_Object = MibTableRow
gs2328fGARPConfEntry = _Gs2328fGARPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1)
)
gs2328fGARPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fGARPConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fGARPConfEntry.setStatus("current")


class _Gs2328fGARPConfPort_Type(Integer32):
    """Custom type gs2328fGARPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fGARPConfPort_Type.__name__ = "Integer32"
_Gs2328fGARPConfPort_Object = MibTableColumn
gs2328fGARPConfPort = _Gs2328fGARPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 1),
    _Gs2328fGARPConfPort_Type()
)
gs2328fGARPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fGARPConfPort.setStatus("current")


class _Gs2328fGARPJoinTimer_Type(Integer32):
    """Custom type gs2328fGARPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_Gs2328fGARPJoinTimer_Type.__name__ = "Integer32"
_Gs2328fGARPJoinTimer_Object = MibTableColumn
gs2328fGARPJoinTimer = _Gs2328fGARPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 2),
    _Gs2328fGARPJoinTimer_Type()
)
gs2328fGARPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPJoinTimer.setStatus("current")


class _Gs2328fGARPLeaveTimer_Type(Integer32):
    """Custom type gs2328fGARPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3000),
    )


_Gs2328fGARPLeaveTimer_Type.__name__ = "Integer32"
_Gs2328fGARPLeaveTimer_Object = MibTableColumn
gs2328fGARPLeaveTimer = _Gs2328fGARPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 3),
    _Gs2328fGARPLeaveTimer_Type()
)
gs2328fGARPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPLeaveTimer.setStatus("current")


class _Gs2328fGARPLeaveAllTimer_Type(Integer32):
    """Custom type gs2328fGARPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 50000),
    )


_Gs2328fGARPLeaveAllTimer_Type.__name__ = "Integer32"
_Gs2328fGARPLeaveAllTimer_Object = MibTableColumn
gs2328fGARPLeaveAllTimer = _Gs2328fGARPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 4),
    _Gs2328fGARPLeaveAllTimer_Type()
)
gs2328fGARPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPLeaveAllTimer.setStatus("current")


class _Gs2328fGARPApplicantion_Type(Integer32):
    """Custom type gs2328fGARPApplicantion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gvrp", 1)
    )


_Gs2328fGARPApplicantion_Type.__name__ = "Integer32"
_Gs2328fGARPApplicantion_Object = MibTableColumn
gs2328fGARPApplicantion = _Gs2328fGARPApplicantion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 5),
    _Gs2328fGARPApplicantion_Type()
)
gs2328fGARPApplicantion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPApplicantion.setStatus("current")


class _Gs2328fGARPAttributeType_Type(Integer32):
    """Custom type gs2328fGARPAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_Gs2328fGARPAttributeType_Type.__name__ = "Integer32"
_Gs2328fGARPAttributeType_Object = MibTableColumn
gs2328fGARPAttributeType = _Gs2328fGARPAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 6),
    _Gs2328fGARPAttributeType_Type()
)
gs2328fGARPAttributeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPAttributeType.setStatus("current")


class _Gs2328fGARPApplicant_Type(Integer32):
    """Custom type gs2328fGARPApplicant based on Integer32"""
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


_Gs2328fGARPApplicant_Type.__name__ = "Integer32"
_Gs2328fGARPApplicant_Object = MibTableColumn
gs2328fGARPApplicant = _Gs2328fGARPApplicant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 1, 1, 7),
    _Gs2328fGARPApplicant_Type()
)
gs2328fGARPApplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGARPApplicant.setStatus("current")
_Gs2328fGARPStatisticsTable_Object = MibTable
gs2328fGARPStatisticsTable = _Gs2328fGARPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fGARPStatisticsTable.setStatus("current")
_Gs2328fGARPStatisticsEntry_Object = MibTableRow
gs2328fGARPStatisticsEntry = _Gs2328fGARPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 2, 1)
)
gs2328fGARPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fGARPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328fGARPStatisticsEntry.setStatus("current")


class _Gs2328fGARPStatisticsPort_Type(Integer32):
    """Custom type gs2328fGARPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fGARPStatisticsPort_Type.__name__ = "Integer32"
_Gs2328fGARPStatisticsPort_Object = MibTableColumn
gs2328fGARPStatisticsPort = _Gs2328fGARPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 2, 1, 1),
    _Gs2328fGARPStatisticsPort_Type()
)
gs2328fGARPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fGARPStatisticsPort.setStatus("current")
_Gs2328fGARPStatisticsPeerMAC_Type = DisplayString
_Gs2328fGARPStatisticsPeerMAC_Object = MibTableColumn
gs2328fGARPStatisticsPeerMAC = _Gs2328fGARPStatisticsPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 2, 1, 2),
    _Gs2328fGARPStatisticsPeerMAC_Type()
)
gs2328fGARPStatisticsPeerMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fGARPStatisticsPeerMAC.setStatus("current")
_Gs2328fGARPStatisticsFailedCount_Type = Counter32
_Gs2328fGARPStatisticsFailedCount_Object = MibTableColumn
gs2328fGARPStatisticsFailedCount = _Gs2328fGARPStatisticsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 3, 2, 1, 3),
    _Gs2328fGARPStatisticsFailedCount_Type()
)
gs2328fGARPStatisticsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fGARPStatisticsFailedCount.setStatus("current")
_Gs2328fGVRP_ObjectIdentity = ObjectIdentity
gs2328fGVRP = _Gs2328fGVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4)
)
_Gs2328fGVRPConf_ObjectIdentity = ObjectIdentity
gs2328fGVRPConf = _Gs2328fGVRPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1)
)


class _Gs2328fGVRPMode_Type(Integer32):
    """Custom type gs2328fGVRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fGVRPMode_Type.__name__ = "Integer32"
_Gs2328fGVRPMode_Object = MibScalar
gs2328fGVRPMode = _Gs2328fGVRPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1, 1),
    _Gs2328fGVRPMode_Type()
)
gs2328fGVRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGVRPMode.setStatus("current")
_Gs2328fGVRPConfTable_Object = MibTable
gs2328fGVRPConfTable = _Gs2328fGVRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fGVRPConfTable.setStatus("current")
_Gs2328fGVRPConfEntry_Object = MibTableRow
gs2328fGVRPConfEntry = _Gs2328fGVRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1, 2, 1)
)
gs2328fGVRPConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fGVRPConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fGVRPConfEntry.setStatus("current")


class _Gs2328fGVRPConfPort_Type(Integer32):
    """Custom type gs2328fGVRPConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fGVRPConfPort_Type.__name__ = "Integer32"
_Gs2328fGVRPConfPort_Object = MibTableColumn
gs2328fGVRPConfPort = _Gs2328fGVRPConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1, 2, 1, 1),
    _Gs2328fGVRPConfPort_Type()
)
gs2328fGVRPConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fGVRPConfPort.setStatus("current")


class _Gs2328fGVRPConfPortMode_Type(Integer32):
    """Custom type gs2328fGVRPConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fGVRPConfPortMode_Type.__name__ = "Integer32"
_Gs2328fGVRPConfPortMode_Object = MibTableColumn
gs2328fGVRPConfPortMode = _Gs2328fGVRPConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1, 2, 1, 2),
    _Gs2328fGVRPConfPortMode_Type()
)
gs2328fGVRPConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGVRPConfPortMode.setStatus("current")


class _Gs2328fGVRPConfPortRRole_Type(Integer32):
    """Custom type gs2328fGVRPConfPortRRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fGVRPConfPortRRole_Type.__name__ = "Integer32"
_Gs2328fGVRPConfPortRRole_Object = MibTableColumn
gs2328fGVRPConfPortRRole = _Gs2328fGVRPConfPortRRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 1, 2, 1, 3),
    _Gs2328fGVRPConfPortRRole_Type()
)
gs2328fGVRPConfPortRRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fGVRPConfPortRRole.setStatus("current")
_Gs2328fGVRPStatisticsTable_Object = MibTable
gs2328fGVRPStatisticsTable = _Gs2328fGVRPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fGVRPStatisticsTable.setStatus("current")
_Gs2328fGVRPStatisticsEntry_Object = MibTableRow
gs2328fGVRPStatisticsEntry = _Gs2328fGVRPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 2, 1)
)
gs2328fGVRPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fGVRPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328fGVRPStatisticsEntry.setStatus("current")


class _Gs2328fGVRPStatisticsPort_Type(Integer32):
    """Custom type gs2328fGVRPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fGVRPStatisticsPort_Type.__name__ = "Integer32"
_Gs2328fGVRPStatisticsPort_Object = MibTableColumn
gs2328fGVRPStatisticsPort = _Gs2328fGVRPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 2, 1, 1),
    _Gs2328fGVRPStatisticsPort_Type()
)
gs2328fGVRPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fGVRPStatisticsPort.setStatus("current")
_Gs2328fGVRPStatisticsJoinTxCnt_Type = Counter32
_Gs2328fGVRPStatisticsJoinTxCnt_Object = MibTableColumn
gs2328fGVRPStatisticsJoinTxCnt = _Gs2328fGVRPStatisticsJoinTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 2, 1, 2),
    _Gs2328fGVRPStatisticsJoinTxCnt_Type()
)
gs2328fGVRPStatisticsJoinTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fGVRPStatisticsJoinTxCnt.setStatus("current")
_Gs2328fGVRPStatisticsLeaveTxCnt_Type = Counter32
_Gs2328fGVRPStatisticsLeaveTxCnt_Object = MibTableColumn
gs2328fGVRPStatisticsLeaveTxCnt = _Gs2328fGVRPStatisticsLeaveTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 4, 2, 1, 3),
    _Gs2328fGVRPStatisticsLeaveTxCnt_Type()
)
gs2328fGVRPStatisticsLeaveTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fGVRPStatisticsLeaveTxCnt.setStatus("current")
_Gs2328fMirroring_ObjectIdentity = ObjectIdentity
gs2328fMirroring = _Gs2328fMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 6)
)


class _Gs2328fPortToMirrorOn_Type(Integer32):
    """Custom type gs2328fPortToMirrorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2328fPortToMirrorOn_Type.__name__ = "Integer32"
_Gs2328fPortToMirrorOn_Object = MibScalar
gs2328fPortToMirrorOn = _Gs2328fPortToMirrorOn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 6, 1),
    _Gs2328fPortToMirrorOn_Type()
)
gs2328fPortToMirrorOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortToMirrorOn.setStatus("current")
_Gs2328fMirrorTable_Object = MibTable
gs2328fMirrorTable = _Gs2328fMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328fMirrorTable.setStatus("current")
_Gs2328fMirrorEntry_Object = MibTableRow
gs2328fMirrorEntry = _Gs2328fMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 6, 2, 1)
)
gs2328fMirrorEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMirrorPort"),
)
if mibBuilder.loadTexts:
    gs2328fMirrorEntry.setStatus("current")


class _Gs2328fMirrorPort_Type(Integer32):
    """Custom type gs2328fMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMirrorPort_Type.__name__ = "Integer32"
_Gs2328fMirrorPort_Object = MibTableColumn
gs2328fMirrorPort = _Gs2328fMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 6, 2, 1, 1),
    _Gs2328fMirrorPort_Type()
)
gs2328fMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMirrorPort.setStatus("current")


class _Gs2328fMirrorMode_Type(Integer32):
    """Custom type gs2328fMirrorMode based on Integer32"""
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


_Gs2328fMirrorMode_Type.__name__ = "Integer32"
_Gs2328fMirrorMode_Object = MibTableColumn
gs2328fMirrorMode = _Gs2328fMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 6, 2, 1, 2),
    _Gs2328fMirrorMode_Type()
)
gs2328fMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMirrorMode.setStatus("current")
_Gs2328fTrapEventSeverity_ObjectIdentity = ObjectIdentity
gs2328fTrapEventSeverity = _Gs2328fTrapEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7)
)


class _Gs2328fTrapEventSeverityACL_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityACL based on Integer32"""
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


_Gs2328fTrapEventSeverityACL_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityACL_Object = MibScalar
gs2328fTrapEventSeverityACL = _Gs2328fTrapEventSeverityACL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 1),
    _Gs2328fTrapEventSeverityACL_Type()
)
gs2328fTrapEventSeverityACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityACL.setStatus("current")


class _Gs2328fTrapEventSeverityACLLog_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityACLLog based on Integer32"""
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


_Gs2328fTrapEventSeverityACLLog_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityACLLog_Object = MibScalar
gs2328fTrapEventSeverityACLLog = _Gs2328fTrapEventSeverityACLLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 2),
    _Gs2328fTrapEventSeverityACLLog_Type()
)
gs2328fTrapEventSeverityACLLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityACLLog.setStatus("current")


class _Gs2328fTrapEventSeverityAccessMgmt_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityAccessMgmt based on Integer32"""
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


_Gs2328fTrapEventSeverityAccessMgmt_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityAccessMgmt_Object = MibScalar
gs2328fTrapEventSeverityAccessMgmt = _Gs2328fTrapEventSeverityAccessMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 3),
    _Gs2328fTrapEventSeverityAccessMgmt_Type()
)
gs2328fTrapEventSeverityAccessMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityAccessMgmt.setStatus("current")


class _Gs2328fTrapEventSeverityAuthFailed_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityAuthFailed based on Integer32"""
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


_Gs2328fTrapEventSeverityAuthFailed_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityAuthFailed_Object = MibScalar
gs2328fTrapEventSeverityAuthFailed = _Gs2328fTrapEventSeverityAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 4),
    _Gs2328fTrapEventSeverityAuthFailed_Type()
)
gs2328fTrapEventSeverityAuthFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityAuthFailed.setStatus("current")


class _Gs2328fTrapEventSeverityColdStart_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityColdStart based on Integer32"""
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


_Gs2328fTrapEventSeverityColdStart_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityColdStart_Object = MibScalar
gs2328fTrapEventSeverityColdStart = _Gs2328fTrapEventSeverityColdStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 5),
    _Gs2328fTrapEventSeverityColdStart_Type()
)
gs2328fTrapEventSeverityColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityColdStart.setStatus("current")


class _Gs2328fTrapEventSeverityConfigInfo_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityConfigInfo based on Integer32"""
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


_Gs2328fTrapEventSeverityConfigInfo_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityConfigInfo_Object = MibScalar
gs2328fTrapEventSeverityConfigInfo = _Gs2328fTrapEventSeverityConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 6),
    _Gs2328fTrapEventSeverityConfigInfo_Type()
)
gs2328fTrapEventSeverityConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityConfigInfo.setStatus("current")


class _Gs2328fTrapEventSeverityFirmwareUpgrade_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityFirmwareUpgrade based on Integer32"""
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


_Gs2328fTrapEventSeverityFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityFirmwareUpgrade_Object = MibScalar
gs2328fTrapEventSeverityFirmwareUpgrade = _Gs2328fTrapEventSeverityFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 7),
    _Gs2328fTrapEventSeverityFirmwareUpgrade_Type()
)
gs2328fTrapEventSeverityFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityFirmwareUpgrade.setStatus("current")


class _Gs2328fTrapEventSeverityImportExport_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityImportExport based on Integer32"""
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


_Gs2328fTrapEventSeverityImportExport_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityImportExport_Object = MibScalar
gs2328fTrapEventSeverityImportExport = _Gs2328fTrapEventSeverityImportExport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 8),
    _Gs2328fTrapEventSeverityImportExport_Type()
)
gs2328fTrapEventSeverityImportExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityImportExport.setStatus("current")


class _Gs2328fTrapEventSeverityLACP_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityLACP based on Integer32"""
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


_Gs2328fTrapEventSeverityLACP_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityLACP_Object = MibScalar
gs2328fTrapEventSeverityLACP = _Gs2328fTrapEventSeverityLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 9),
    _Gs2328fTrapEventSeverityLACP_Type()
)
gs2328fTrapEventSeverityLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityLACP.setStatus("current")


class _Gs2328fTrapEventSeverityLinkStatus_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityLinkStatus based on Integer32"""
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


_Gs2328fTrapEventSeverityLinkStatus_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityLinkStatus_Object = MibScalar
gs2328fTrapEventSeverityLinkStatus = _Gs2328fTrapEventSeverityLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 10),
    _Gs2328fTrapEventSeverityLinkStatus_Type()
)
gs2328fTrapEventSeverityLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityLinkStatus.setStatus("current")


class _Gs2328fTrapEventSeverityLogin_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityLogin based on Integer32"""
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


_Gs2328fTrapEventSeverityLogin_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityLogin_Object = MibScalar
gs2328fTrapEventSeverityLogin = _Gs2328fTrapEventSeverityLogin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 11),
    _Gs2328fTrapEventSeverityLogin_Type()
)
gs2328fTrapEventSeverityLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityLogin.setStatus("current")


class _Gs2328fTrapEventSeverityLogout_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityLogout based on Integer32"""
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


_Gs2328fTrapEventSeverityLogout_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityLogout_Object = MibScalar
gs2328fTrapEventSeverityLogout = _Gs2328fTrapEventSeverityLogout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 12),
    _Gs2328fTrapEventSeverityLogout_Type()
)
gs2328fTrapEventSeverityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityLogout.setStatus("current")


class _Gs2328fTrapEventSeverityLoopProtect_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityLoopProtect based on Integer32"""
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


_Gs2328fTrapEventSeverityLoopProtect_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityLoopProtect_Object = MibScalar
gs2328fTrapEventSeverityLoopProtect = _Gs2328fTrapEventSeverityLoopProtect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 13),
    _Gs2328fTrapEventSeverityLoopProtect_Type()
)
gs2328fTrapEventSeverityLoopProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityLoopProtect.setStatus("current")


class _Gs2328fTrapEventSeverityMgmtIPChange_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityMgmtIPChange based on Integer32"""
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


_Gs2328fTrapEventSeverityMgmtIPChange_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityMgmtIPChange_Object = MibScalar
gs2328fTrapEventSeverityMgmtIPChange = _Gs2328fTrapEventSeverityMgmtIPChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 14),
    _Gs2328fTrapEventSeverityMgmtIPChange_Type()
)
gs2328fTrapEventSeverityMgmtIPChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityMgmtIPChange.setStatus("current")


class _Gs2328fTrapEventSeverityModuleChange_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityModuleChange based on Integer32"""
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


_Gs2328fTrapEventSeverityModuleChange_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityModuleChange_Object = MibScalar
gs2328fTrapEventSeverityModuleChange = _Gs2328fTrapEventSeverityModuleChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 15),
    _Gs2328fTrapEventSeverityModuleChange_Type()
)
gs2328fTrapEventSeverityModuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityModuleChange.setStatus("current")


class _Gs2328fTrapEventSeverityNAS_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityNAS based on Integer32"""
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


_Gs2328fTrapEventSeverityNAS_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityNAS_Object = MibScalar
gs2328fTrapEventSeverityNAS = _Gs2328fTrapEventSeverityNAS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 16),
    _Gs2328fTrapEventSeverityNAS_Type()
)
gs2328fTrapEventSeverityNAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityNAS.setStatus("current")


class _Gs2328fTrapEventSeverityPasswordChange_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityPasswordChange based on Integer32"""
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


_Gs2328fTrapEventSeverityPasswordChange_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityPasswordChange_Object = MibScalar
gs2328fTrapEventSeverityPasswordChange = _Gs2328fTrapEventSeverityPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 17),
    _Gs2328fTrapEventSeverityPasswordChange_Type()
)
gs2328fTrapEventSeverityPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityPasswordChange.setStatus("current")


class _Gs2328fTrapEventSeverityPortSecurity_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityPortSecurity based on Integer32"""
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


_Gs2328fTrapEventSeverityPortSecurity_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityPortSecurity_Object = MibScalar
gs2328fTrapEventSeverityPortSecurity = _Gs2328fTrapEventSeverityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 18),
    _Gs2328fTrapEventSeverityPortSecurity_Type()
)
gs2328fTrapEventSeverityPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityPortSecurity.setStatus("current")


class _Gs2328fTrapEventSeverityVLAN_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityVLAN based on Integer32"""
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


_Gs2328fTrapEventSeverityVLAN_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityVLAN_Object = MibScalar
gs2328fTrapEventSeverityVLAN = _Gs2328fTrapEventSeverityVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 20),
    _Gs2328fTrapEventSeverityVLAN_Type()
)
gs2328fTrapEventSeverityVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityVLAN.setStatus("current")


class _Gs2328fTrapEventSeverityWarmStart_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityWarmStart based on Integer32"""
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


_Gs2328fTrapEventSeverityWarmStart_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityWarmStart_Object = MibScalar
gs2328fTrapEventSeverityWarmStart = _Gs2328fTrapEventSeverityWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 21),
    _Gs2328fTrapEventSeverityWarmStart_Type()
)
gs2328fTrapEventSeverityWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityWarmStart.setStatus("current")


class _Gs2328fTrapEventSeverityARPConflict_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityARPConflict based on Integer32"""
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


_Gs2328fTrapEventSeverityARPConflict_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityARPConflict_Object = MibScalar
gs2328fTrapEventSeverityARPConflict = _Gs2328fTrapEventSeverityARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 25),
    _Gs2328fTrapEventSeverityARPConflict_Type()
)
gs2328fTrapEventSeverityARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityARPConflict.setStatus("current")


class _Gs2328fTrapEventSeveritySpoofingLimit_Type(Integer32):
    """Custom type gs2328fTrapEventSeveritySpoofingLimit based on Integer32"""
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


_Gs2328fTrapEventSeveritySpoofingLimit_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeveritySpoofingLimit_Object = MibScalar
gs2328fTrapEventSeveritySpoofingLimit = _Gs2328fTrapEventSeveritySpoofingLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 27),
    _Gs2328fTrapEventSeveritySpoofingLimit_Type()
)
gs2328fTrapEventSeveritySpoofingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeveritySpoofingLimit.setStatus("current")


class _Gs2328fTrapEventSeverityStaticARPConflict_Type(Integer32):
    """Custom type gs2328fTrapEventSeverityStaticARPConflict based on Integer32"""
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


_Gs2328fTrapEventSeverityStaticARPConflict_Type.__name__ = "Integer32"
_Gs2328fTrapEventSeverityStaticARPConflict_Object = MibScalar
gs2328fTrapEventSeverityStaticARPConflict = _Gs2328fTrapEventSeverityStaticARPConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 7, 28),
    _Gs2328fTrapEventSeverityStaticARPConflict_Type()
)
gs2328fTrapEventSeverityStaticARPConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTrapEventSeverityStaticARPConflict.setStatus("current")
_Gs2328fSMTP_ObjectIdentity = ObjectIdentity
gs2328fSMTP = _Gs2328fSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8)
)
_Gs2328fSMTPMailServer_Type = DisplayString
_Gs2328fSMTPMailServer_Object = MibScalar
gs2328fSMTPMailServer = _Gs2328fSMTPMailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 1),
    _Gs2328fSMTPMailServer_Type()
)
gs2328fSMTPMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPMailServer.setStatus("current")
_Gs2328fSMTPUserName_Type = DisplayString
_Gs2328fSMTPUserName_Object = MibScalar
gs2328fSMTPUserName = _Gs2328fSMTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 2),
    _Gs2328fSMTPUserName_Type()
)
gs2328fSMTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPUserName.setStatus("current")
_Gs2328fSMTPPassword_Type = DisplayString
_Gs2328fSMTPPassword_Object = MibScalar
gs2328fSMTPPassword = _Gs2328fSMTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 3),
    _Gs2328fSMTPPassword_Type()
)
gs2328fSMTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPPassword.setStatus("current")


class _Gs2328fSMTPServeriryLevel_Type(Integer32):
    """Custom type gs2328fSMTPServeriryLevel based on Integer32"""
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


_Gs2328fSMTPServeriryLevel_Type.__name__ = "Integer32"
_Gs2328fSMTPServeriryLevel_Object = MibScalar
gs2328fSMTPServeriryLevel = _Gs2328fSMTPServeriryLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 4),
    _Gs2328fSMTPServeriryLevel_Type()
)
gs2328fSMTPServeriryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPServeriryLevel.setStatus("current")
_Gs2328fSMTPSender_Type = DisplayString
_Gs2328fSMTPSender_Object = MibScalar
gs2328fSMTPSender = _Gs2328fSMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 5),
    _Gs2328fSMTPSender_Type()
)
gs2328fSMTPSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPSender.setStatus("current")
_Gs2328fSMTPReturnPath_Type = DisplayString
_Gs2328fSMTPReturnPath_Object = MibScalar
gs2328fSMTPReturnPath = _Gs2328fSMTPReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 6),
    _Gs2328fSMTPReturnPath_Type()
)
gs2328fSMTPReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPReturnPath.setStatus("current")
_Gs2328fSMTPEmailAddress1_Type = DisplayString
_Gs2328fSMTPEmailAddress1_Object = MibScalar
gs2328fSMTPEmailAddress1 = _Gs2328fSMTPEmailAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 7),
    _Gs2328fSMTPEmailAddress1_Type()
)
gs2328fSMTPEmailAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPEmailAddress1.setStatus("current")
_Gs2328fSMTPEmailAddress2_Type = DisplayString
_Gs2328fSMTPEmailAddress2_Object = MibScalar
gs2328fSMTPEmailAddress2 = _Gs2328fSMTPEmailAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 8),
    _Gs2328fSMTPEmailAddress2_Type()
)
gs2328fSMTPEmailAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPEmailAddress2.setStatus("current")
_Gs2328fSMTPEmailAddress3_Type = DisplayString
_Gs2328fSMTPEmailAddress3_Object = MibScalar
gs2328fSMTPEmailAddress3 = _Gs2328fSMTPEmailAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 9),
    _Gs2328fSMTPEmailAddress3_Type()
)
gs2328fSMTPEmailAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPEmailAddress3.setStatus("current")
_Gs2328fSMTPEmailAddress4_Type = DisplayString
_Gs2328fSMTPEmailAddress4_Object = MibScalar
gs2328fSMTPEmailAddress4 = _Gs2328fSMTPEmailAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 10),
    _Gs2328fSMTPEmailAddress4_Type()
)
gs2328fSMTPEmailAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPEmailAddress4.setStatus("current")
_Gs2328fSMTPEmailAddress5_Type = DisplayString
_Gs2328fSMTPEmailAddress5_Object = MibScalar
gs2328fSMTPEmailAddress5 = _Gs2328fSMTPEmailAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 11),
    _Gs2328fSMTPEmailAddress5_Type()
)
gs2328fSMTPEmailAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPEmailAddress5.setStatus("current")
_Gs2328fSMTPEmailAddress6_Type = DisplayString
_Gs2328fSMTPEmailAddress6_Object = MibScalar
gs2328fSMTPEmailAddress6 = _Gs2328fSMTPEmailAddress6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 8, 12),
    _Gs2328fSMTPEmailAddress6_Type()
)
gs2328fSMTPEmailAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSMTPEmailAddress6.setStatus("current")
_Gs2328fACL_ObjectIdentity = ObjectIdentity
gs2328fACL = _Gs2328fACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9)
)
_Gs2328fACLPortsConfTable_Object = MibTable
gs2328fACLPortsConfTable = _Gs2328fACLPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1)
)
if mibBuilder.loadTexts:
    gs2328fACLPortsConfTable.setStatus("current")
_Gs2328fACLPortsConfEntry_Object = MibTableRow
gs2328fACLPortsConfEntry = _Gs2328fACLPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1)
)
gs2328fACLPortsConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fACLPortsConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fACLPortsConfEntry.setStatus("current")


class _Gs2328fACLPortsConfPort_Type(Integer32):
    """Custom type gs2328fACLPortsConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fACLPortsConfPort_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfPort_Object = MibTableColumn
gs2328fACLPortsConfPort = _Gs2328fACLPortsConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 1),
    _Gs2328fACLPortsConfPort_Type()
)
gs2328fACLPortsConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfPort.setStatus("current")


class _Gs2328fACLPortsConfPolicyID_Type(Integer32):
    """Custom type gs2328fACLPortsConfPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328fACLPortsConfPolicyID_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfPolicyID_Object = MibTableColumn
gs2328fACLPortsConfPolicyID = _Gs2328fACLPortsConfPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 2),
    _Gs2328fACLPortsConfPolicyID_Type()
)
gs2328fACLPortsConfPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfPolicyID.setStatus("current")


class _Gs2328fACLPortsConfAction_Type(Integer32):
    """Custom type gs2328fACLPortsConfAction based on Integer32"""
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


_Gs2328fACLPortsConfAction_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfAction_Object = MibTableColumn
gs2328fACLPortsConfAction = _Gs2328fACLPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 3),
    _Gs2328fACLPortsConfAction_Type()
)
gs2328fACLPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfAction.setStatus("current")


class _Gs2328fACLPortsConfRateLimiterID_Type(Integer32):
    """Custom type gs2328fACLPortsConfRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2328fACLPortsConfRateLimiterID_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfRateLimiterID_Object = MibTableColumn
gs2328fACLPortsConfRateLimiterID = _Gs2328fACLPortsConfRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 4),
    _Gs2328fACLPortsConfRateLimiterID_Type()
)
gs2328fACLPortsConfRateLimiterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfRateLimiterID.setStatus("current")


class _Gs2328fACLPortsConfPortRedirect_Type(Integer32):
    """Custom type gs2328fACLPortsConfPortRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Gs2328fACLPortsConfPortRedirect_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfPortRedirect_Object = MibTableColumn
gs2328fACLPortsConfPortRedirect = _Gs2328fACLPortsConfPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 5),
    _Gs2328fACLPortsConfPortRedirect_Type()
)
gs2328fACLPortsConfPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfPortRedirect.setStatus("current")


class _Gs2328fACLPortsConfMirror_Type(Integer32):
    """Custom type gs2328fACLPortsConfMirror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLPortsConfMirror_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfMirror_Object = MibTableColumn
gs2328fACLPortsConfMirror = _Gs2328fACLPortsConfMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 6),
    _Gs2328fACLPortsConfMirror_Type()
)
gs2328fACLPortsConfMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfMirror.setStatus("current")


class _Gs2328fACLPortsConfLogging_Type(Integer32):
    """Custom type gs2328fACLPortsConfLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLPortsConfLogging_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfLogging_Object = MibTableColumn
gs2328fACLPortsConfLogging = _Gs2328fACLPortsConfLogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 7),
    _Gs2328fACLPortsConfLogging_Type()
)
gs2328fACLPortsConfLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfLogging.setStatus("current")


class _Gs2328fACLPortsConfShutdown_Type(Integer32):
    """Custom type gs2328fACLPortsConfShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLPortsConfShutdown_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfShutdown_Object = MibTableColumn
gs2328fACLPortsConfShutdown = _Gs2328fACLPortsConfShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 8),
    _Gs2328fACLPortsConfShutdown_Type()
)
gs2328fACLPortsConfShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfShutdown.setStatus("current")


class _Gs2328fACLPortsConfState_Type(Integer32):
    """Custom type gs2328fACLPortsConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLPortsConfState_Type.__name__ = "Integer32"
_Gs2328fACLPortsConfState_Object = MibTableColumn
gs2328fACLPortsConfState = _Gs2328fACLPortsConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 9),
    _Gs2328fACLPortsConfState_Type()
)
gs2328fACLPortsConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfState.setStatus("current")
_Gs2328fACLPortsConfCounter_Type = Counter32
_Gs2328fACLPortsConfCounter_Object = MibTableColumn
gs2328fACLPortsConfCounter = _Gs2328fACLPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 1, 1, 10),
    _Gs2328fACLPortsConfCounter_Type()
)
gs2328fACLPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLPortsConfCounter.setStatus("current")
_Gs2328fACLRateLimiterTable_Object = MibTable
gs2328fACLRateLimiterTable = _Gs2328fACLRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 2)
)
if mibBuilder.loadTexts:
    gs2328fACLRateLimiterTable.setStatus("current")
_Gs2328fACLRateLimiterEntry_Object = MibTableRow
gs2328fACLRateLimiterEntry = _Gs2328fACLRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 2, 1)
)
gs2328fACLRateLimiterEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fACLRateLimiterID"),
)
if mibBuilder.loadTexts:
    gs2328fACLRateLimiterEntry.setStatus("current")


class _Gs2328fACLRateLimiterID_Type(Integer32):
    """Custom type gs2328fACLRateLimiterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2328fACLRateLimiterID_Type.__name__ = "Integer32"
_Gs2328fACLRateLimiterID_Object = MibTableColumn
gs2328fACLRateLimiterID = _Gs2328fACLRateLimiterID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 2, 1, 1),
    _Gs2328fACLRateLimiterID_Type()
)
gs2328fACLRateLimiterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fACLRateLimiterID.setStatus("current")


class _Gs2328fACLRateLimiterUnit_Type(Integer32):
    """Custom type gs2328fACLRateLimiterUnit based on Integer32"""
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


_Gs2328fACLRateLimiterUnit_Type.__name__ = "Integer32"
_Gs2328fACLRateLimiterUnit_Object = MibTableColumn
gs2328fACLRateLimiterUnit = _Gs2328fACLRateLimiterUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 2, 1, 2),
    _Gs2328fACLRateLimiterUnit_Type()
)
gs2328fACLRateLimiterUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLRateLimiterUnit.setStatus("current")


class _Gs2328fACLRateLimiterRate_Type(Integer32):
    """Custom type gs2328fACLRateLimiterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_Gs2328fACLRateLimiterRate_Type.__name__ = "Integer32"
_Gs2328fACLRateLimiterRate_Object = MibTableColumn
gs2328fACLRateLimiterRate = _Gs2328fACLRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 2, 1, 3),
    _Gs2328fACLRateLimiterRate_Type()
)
gs2328fACLRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLRateLimiterRate.setStatus("current")
_Gs2328fACLACE_ObjectIdentity = ObjectIdentity
gs2328fACLACE = _Gs2328fACLACE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3)
)


class _Gs2328fACLACECreate_Type(Integer32):
    """Custom type gs2328fACLACECreate based on Integer32"""
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


_Gs2328fACLACECreate_Type.__name__ = "Integer32"
_Gs2328fACLACECreate_Object = MibScalar
gs2328fACLACECreate = _Gs2328fACLACECreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 1),
    _Gs2328fACLACECreate_Type()
)
gs2328fACLACECreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACECreate.setStatus("current")
_Gs2328fACLACETable_Object = MibTable
gs2328fACLACETable = _Gs2328fACLACETable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fACLACETable.setStatus("current")
_Gs2328fACLACEEntry_Object = MibTableRow
gs2328fACLACEEntry = _Gs2328fACLACEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1)
)
gs2328fACLACEEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fACLACEIndex"),
)
if mibBuilder.loadTexts:
    gs2328fACLACEEntry.setStatus("current")


class _Gs2328fACLACEIndex_Type(Integer32):
    """Custom type gs2328fACLACEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fACLACEIndex_Type.__name__ = "Integer32"
_Gs2328fACLACEIndex_Object = MibTableColumn
gs2328fACLACEIndex = _Gs2328fACLACEIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 1),
    _Gs2328fACLACEIndex_Type()
)
gs2328fACLACEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fACLACEIndex.setStatus("current")


class _Gs2328fACLACEID_Type(Integer32):
    """Custom type gs2328fACLACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fACLACEID_Type.__name__ = "Integer32"
_Gs2328fACLACEID_Object = MibTableColumn
gs2328fACLACEID = _Gs2328fACLACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 2),
    _Gs2328fACLACEID_Type()
)
gs2328fACLACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEID.setStatus("current")


class _Gs2328fACLACENextID_Type(Integer32):
    """Custom type gs2328fACLACENextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328fACLACENextID_Type.__name__ = "Integer32"
_Gs2328fACLACENextID_Object = MibTableColumn
gs2328fACLACENextID = _Gs2328fACLACENextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 3),
    _Gs2328fACLACENextID_Type()
)
gs2328fACLACENextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACENextID.setStatus("current")
_Gs2328fACLACEIngressPort_Type = DisplayString
_Gs2328fACLACEIngressPort_Object = MibTableColumn
gs2328fACLACEIngressPort = _Gs2328fACLACEIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 4),
    _Gs2328fACLACEIngressPort_Type()
)
gs2328fACLACEIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEIngressPort.setStatus("current")


class _Gs2328fACLACEPortPolicyNumber_Type(Integer32):
    """Custom type gs2328fACLACEPortPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328fACLACEPortPolicyNumber_Type.__name__ = "Integer32"
_Gs2328fACLACEPortPolicyNumber_Object = MibTableColumn
gs2328fACLACEPortPolicyNumber = _Gs2328fACLACEPortPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 5),
    _Gs2328fACLACEPortPolicyNumber_Type()
)
gs2328fACLACEPortPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEPortPolicyNumber.setStatus("current")


class _Gs2328fACLACEPortPolicyBitmask_Type(Integer32):
    """Custom type gs2328fACLACEPortPolicyBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328fACLACEPortPolicyBitmask_Type.__name__ = "Integer32"
_Gs2328fACLACEPortPolicyBitmask_Object = MibTableColumn
gs2328fACLACEPortPolicyBitmask = _Gs2328fACLACEPortPolicyBitmask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 6),
    _Gs2328fACLACEPortPolicyBitmask_Type()
)
gs2328fACLACEPortPolicyBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEPortPolicyBitmask.setStatus("current")


class _Gs2328fACLACEFrameType_Type(Integer32):
    """Custom type gs2328fACLACEFrameType based on Integer32"""
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


_Gs2328fACLACEFrameType_Type.__name__ = "Integer32"
_Gs2328fACLACEFrameType_Object = MibTableColumn
gs2328fACLACEFrameType = _Gs2328fACLACEFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 7),
    _Gs2328fACLACEFrameType_Type()
)
gs2328fACLACEFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEFrameType.setStatus("current")


class _Gs2328fACLACEAction_Type(Integer32):
    """Custom type gs2328fACLACEAction based on Integer32"""
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


_Gs2328fACLACEAction_Type.__name__ = "Integer32"
_Gs2328fACLACEAction_Object = MibTableColumn
gs2328fACLACEAction = _Gs2328fACLACEAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 8),
    _Gs2328fACLACEAction_Type()
)
gs2328fACLACEAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEAction.setStatus("current")
_Gs2328fACLACEDenyPortRedirect_Type = DisplayString
_Gs2328fACLACEDenyPortRedirect_Object = MibTableColumn
gs2328fACLACEDenyPortRedirect = _Gs2328fACLACEDenyPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 9),
    _Gs2328fACLACEDenyPortRedirect_Type()
)
gs2328fACLACEDenyPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDenyPortRedirect.setStatus("current")


class _Gs2328fACLACELogging_Type(Integer32):
    """Custom type gs2328fACLACELogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLACELogging_Type.__name__ = "Integer32"
_Gs2328fACLACELogging_Object = MibTableColumn
gs2328fACLACELogging = _Gs2328fACLACELogging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 10),
    _Gs2328fACLACELogging_Type()
)
gs2328fACLACELogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACELogging.setStatus("current")


class _Gs2328fACLACEMirror_Type(Integer32):
    """Custom type gs2328fACLACEMirror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLACEMirror_Type.__name__ = "Integer32"
_Gs2328fACLACEMirror_Object = MibTableColumn
gs2328fACLACEMirror = _Gs2328fACLACEMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 11),
    _Gs2328fACLACEMirror_Type()
)
gs2328fACLACEMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEMirror.setStatus("current")


class _Gs2328fACLACERateLimiter_Type(Integer32):
    """Custom type gs2328fACLACERateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2328fACLACERateLimiter_Type.__name__ = "Integer32"
_Gs2328fACLACERateLimiter_Object = MibTableColumn
gs2328fACLACERateLimiter = _Gs2328fACLACERateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 12),
    _Gs2328fACLACERateLimiter_Type()
)
gs2328fACLACERateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACERateLimiter.setStatus("current")


class _Gs2328fACLACEShutdown_Type(Integer32):
    """Custom type gs2328fACLACEShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fACLACEShutdown_Type.__name__ = "Integer32"
_Gs2328fACLACEShutdown_Object = MibTableColumn
gs2328fACLACEShutdown = _Gs2328fACLACEShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 13),
    _Gs2328fACLACEShutdown_Type()
)
gs2328fACLACEShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEShutdown.setStatus("current")


class _Gs2328fACLACEVLAN8021QTagged_Type(Integer32):
    """Custom type gs2328fACLACEVLAN8021QTagged based on Integer32"""
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


_Gs2328fACLACEVLAN8021QTagged_Type.__name__ = "Integer32"
_Gs2328fACLACEVLAN8021QTagged_Object = MibTableColumn
gs2328fACLACEVLAN8021QTagged = _Gs2328fACLACEVLAN8021QTagged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 14),
    _Gs2328fACLACEVLAN8021QTagged_Type()
)
gs2328fACLACEVLAN8021QTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEVLAN8021QTagged.setStatus("current")


class _Gs2328fACLACEVLANTagPriority_Type(Integer32):
    """Custom type gs2328fACLACEVLANTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2328fACLACEVLANTagPriority_Type.__name__ = "Integer32"
_Gs2328fACLACEVLANTagPriority_Object = MibTableColumn
gs2328fACLACEVLANTagPriority = _Gs2328fACLACEVLANTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 15),
    _Gs2328fACLACEVLANTagPriority_Type()
)
gs2328fACLACEVLANTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEVLANTagPriority.setStatus("current")


class _Gs2328fACLACEVLANVID_Type(Integer32):
    """Custom type gs2328fACLACEVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328fACLACEVLANVID_Type.__name__ = "Integer32"
_Gs2328fACLACEVLANVID_Object = MibTableColumn
gs2328fACLACEVLANVID = _Gs2328fACLACEVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 16),
    _Gs2328fACLACEVLANVID_Type()
)
gs2328fACLACEVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEVLANVID.setStatus("current")


class _Gs2328fACLACEEtherType_Type(Integer32):
    """Custom type gs2328fACLACEEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328fACLACEEtherType_Type.__name__ = "Integer32"
_Gs2328fACLACEEtherType_Object = MibTableColumn
gs2328fACLACEEtherType = _Gs2328fACLACEEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 17),
    _Gs2328fACLACEEtherType_Type()
)
gs2328fACLACEEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEEtherType.setStatus("current")
_Gs2328fACLACESMAC_Type = DisplayString
_Gs2328fACLACESMAC_Object = MibTableColumn
gs2328fACLACESMAC = _Gs2328fACLACESMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 18),
    _Gs2328fACLACESMAC_Type()
)
gs2328fACLACESMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACESMAC.setStatus("current")


class _Gs2328fACLACEDMACType_Type(Integer32):
    """Custom type gs2328fACLACEDMACType based on Integer32"""
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


_Gs2328fACLACEDMACType_Type.__name__ = "Integer32"
_Gs2328fACLACEDMACType_Object = MibTableColumn
gs2328fACLACEDMACType = _Gs2328fACLACEDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 19),
    _Gs2328fACLACEDMACType_Type()
)
gs2328fACLACEDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDMACType.setStatus("current")
_Gs2328fACLACEDMAC_Type = DisplayString
_Gs2328fACLACEDMAC_Object = MibTableColumn
gs2328fACLACEDMAC = _Gs2328fACLACEDMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 20),
    _Gs2328fACLACEDMAC_Type()
)
gs2328fACLACEDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDMAC.setStatus("current")


class _Gs2328fACLACEArpOpcode_Type(Integer32):
    """Custom type gs2328fACLACEArpOpcode based on Integer32"""
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


_Gs2328fACLACEArpOpcode_Type.__name__ = "Integer32"
_Gs2328fACLACEArpOpcode_Object = MibTableColumn
gs2328fACLACEArpOpcode = _Gs2328fACLACEArpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 21),
    _Gs2328fACLACEArpOpcode_Type()
)
gs2328fACLACEArpOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpOpcode.setStatus("current")


class _Gs2328fACLACEArpFlagsRequestReply_Type(Integer32):
    """Custom type gs2328fACLACEArpFlagsRequestReply based on Integer32"""
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


_Gs2328fACLACEArpFlagsRequestReply_Type.__name__ = "Integer32"
_Gs2328fACLACEArpFlagsRequestReply_Object = MibTableColumn
gs2328fACLACEArpFlagsRequestReply = _Gs2328fACLACEArpFlagsRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 22),
    _Gs2328fACLACEArpFlagsRequestReply_Type()
)
gs2328fACLACEArpFlagsRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpFlagsRequestReply.setStatus("current")


class _Gs2328fACLACEArpFlagsArpSmac_Type(Integer32):
    """Custom type gs2328fACLACEArpFlagsArpSmac based on Integer32"""
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


_Gs2328fACLACEArpFlagsArpSmac_Type.__name__ = "Integer32"
_Gs2328fACLACEArpFlagsArpSmac_Object = MibTableColumn
gs2328fACLACEArpFlagsArpSmac = _Gs2328fACLACEArpFlagsArpSmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 23),
    _Gs2328fACLACEArpFlagsArpSmac_Type()
)
gs2328fACLACEArpFlagsArpSmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpFlagsArpSmac.setStatus("current")


class _Gs2328fACLACEArpFlagsRarpDmac_Type(Integer32):
    """Custom type gs2328fACLACEArpFlagsRarpDmac based on Integer32"""
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


_Gs2328fACLACEArpFlagsRarpDmac_Type.__name__ = "Integer32"
_Gs2328fACLACEArpFlagsRarpDmac_Object = MibTableColumn
gs2328fACLACEArpFlagsRarpDmac = _Gs2328fACLACEArpFlagsRarpDmac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 24),
    _Gs2328fACLACEArpFlagsRarpDmac_Type()
)
gs2328fACLACEArpFlagsRarpDmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpFlagsRarpDmac.setStatus("current")


class _Gs2328fACLACEArpFlagsLength_Type(Integer32):
    """Custom type gs2328fACLACEArpFlagsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fACLACEArpFlagsLength_Type.__name__ = "Integer32"
_Gs2328fACLACEArpFlagsLength_Object = MibTableColumn
gs2328fACLACEArpFlagsLength = _Gs2328fACLACEArpFlagsLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 25),
    _Gs2328fACLACEArpFlagsLength_Type()
)
gs2328fACLACEArpFlagsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpFlagsLength.setStatus("current")


class _Gs2328fACLACEArpFlagsIp_Type(Integer32):
    """Custom type gs2328fACLACEArpFlagsIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fACLACEArpFlagsIp_Type.__name__ = "Integer32"
_Gs2328fACLACEArpFlagsIp_Object = MibTableColumn
gs2328fACLACEArpFlagsIp = _Gs2328fACLACEArpFlagsIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 26),
    _Gs2328fACLACEArpFlagsIp_Type()
)
gs2328fACLACEArpFlagsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpFlagsIp.setStatus("current")


class _Gs2328fACLACEArpFlagsEthernet_Type(Integer32):
    """Custom type gs2328fACLACEArpFlagsEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fACLACEArpFlagsEthernet_Type.__name__ = "Integer32"
_Gs2328fACLACEArpFlagsEthernet_Object = MibTableColumn
gs2328fACLACEArpFlagsEthernet = _Gs2328fACLACEArpFlagsEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 27),
    _Gs2328fACLACEArpFlagsEthernet_Type()
)
gs2328fACLACEArpFlagsEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEArpFlagsEthernet.setStatus("current")


class _Gs2328fACLACESIPType_Type(Integer32):
    """Custom type gs2328fACLACESIPType based on Integer32"""
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


_Gs2328fACLACESIPType_Type.__name__ = "Integer32"
_Gs2328fACLACESIPType_Object = MibTableColumn
gs2328fACLACESIPType = _Gs2328fACLACESIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 28),
    _Gs2328fACLACESIPType_Type()
)
gs2328fACLACESIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACESIPType.setStatus("current")
_Gs2328fACLACESIPIPAddress_Type = IpAddress
_Gs2328fACLACESIPIPAddress_Object = MibTableColumn
gs2328fACLACESIPIPAddress = _Gs2328fACLACESIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 29),
    _Gs2328fACLACESIPIPAddress_Type()
)
gs2328fACLACESIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACESIPIPAddress.setStatus("current")


class _Gs2328fACLACESIPNetworkPrefix_Type(Integer32):
    """Custom type gs2328fACLACESIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2328fACLACESIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2328fACLACESIPNetworkPrefix_Object = MibTableColumn
gs2328fACLACESIPNetworkPrefix = _Gs2328fACLACESIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 30),
    _Gs2328fACLACESIPNetworkPrefix_Type()
)
gs2328fACLACESIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACESIPNetworkPrefix.setStatus("current")


class _Gs2328fACLACEDIPType_Type(Integer32):
    """Custom type gs2328fACLACEDIPType based on Integer32"""
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


_Gs2328fACLACEDIPType_Type.__name__ = "Integer32"
_Gs2328fACLACEDIPType_Object = MibTableColumn
gs2328fACLACEDIPType = _Gs2328fACLACEDIPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 32),
    _Gs2328fACLACEDIPType_Type()
)
gs2328fACLACEDIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDIPType.setStatus("current")
_Gs2328fACLACEDIPIPAddress_Type = IpAddress
_Gs2328fACLACEDIPIPAddress_Object = MibTableColumn
gs2328fACLACEDIPIPAddress = _Gs2328fACLACEDIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 33),
    _Gs2328fACLACEDIPIPAddress_Type()
)
gs2328fACLACEDIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDIPIPAddress.setStatus("current")


class _Gs2328fACLACEDIPNetworkPrefix_Type(Integer32):
    """Custom type gs2328fACLACEDIPNetworkPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Gs2328fACLACEDIPNetworkPrefix_Type.__name__ = "Integer32"
_Gs2328fACLACEDIPNetworkPrefix_Object = MibTableColumn
gs2328fACLACEDIPNetworkPrefix = _Gs2328fACLACEDIPNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 34),
    _Gs2328fACLACEDIPNetworkPrefix_Type()
)
gs2328fACLACEDIPNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDIPNetworkPrefix.setStatus("current")


class _Gs2328fACLACEIPProtocol_Type(Integer32):
    """Custom type gs2328fACLACEIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2328fACLACEIPProtocol_Type.__name__ = "Integer32"
_Gs2328fACLACEIPProtocol_Object = MibTableColumn
gs2328fACLACEIPProtocol = _Gs2328fACLACEIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 36),
    _Gs2328fACLACEIPProtocol_Type()
)
gs2328fACLACEIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEIPProtocol.setStatus("current")


class _Gs2328fACLACEIPFlagsTTL_Type(Integer32):
    """Custom type gs2328fACLACEIPFlagsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fACLACEIPFlagsTTL_Type.__name__ = "Integer32"
_Gs2328fACLACEIPFlagsTTL_Object = MibTableColumn
gs2328fACLACEIPFlagsTTL = _Gs2328fACLACEIPFlagsTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 37),
    _Gs2328fACLACEIPFlagsTTL_Type()
)
gs2328fACLACEIPFlagsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEIPFlagsTTL.setStatus("current")


class _Gs2328fACLACEIPFlagsOptions_Type(Integer32):
    """Custom type gs2328fACLACEIPFlagsOptions based on Integer32"""
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


_Gs2328fACLACEIPFlagsOptions_Type.__name__ = "Integer32"
_Gs2328fACLACEIPFlagsOptions_Object = MibTableColumn
gs2328fACLACEIPFlagsOptions = _Gs2328fACLACEIPFlagsOptions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 38),
    _Gs2328fACLACEIPFlagsOptions_Type()
)
gs2328fACLACEIPFlagsOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEIPFlagsOptions.setStatus("current")


class _Gs2328fACLACEIPFlagsFragment_Type(Integer32):
    """Custom type gs2328fACLACEIPFlagsFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fACLACEIPFlagsFragment_Type.__name__ = "Integer32"
_Gs2328fACLACEIPFlagsFragment_Object = MibTableColumn
gs2328fACLACEIPFlagsFragment = _Gs2328fACLACEIPFlagsFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 39),
    _Gs2328fACLACEIPFlagsFragment_Type()
)
gs2328fACLACEIPFlagsFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEIPFlagsFragment.setStatus("current")


class _Gs2328fACLACEICMPType_Type(Integer32):
    """Custom type gs2328fACLACEICMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2328fACLACEICMPType_Type.__name__ = "Integer32"
_Gs2328fACLACEICMPType_Object = MibTableColumn
gs2328fACLACEICMPType = _Gs2328fACLACEICMPType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 40),
    _Gs2328fACLACEICMPType_Type()
)
gs2328fACLACEICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEICMPType.setStatus("current")


class _Gs2328fACLACEICMPCode_Type(Integer32):
    """Custom type gs2328fACLACEICMPCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_Gs2328fACLACEICMPCode_Type.__name__ = "Integer32"
_Gs2328fACLACEICMPCode_Object = MibTableColumn
gs2328fACLACEICMPCode = _Gs2328fACLACEICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 41),
    _Gs2328fACLACEICMPCode_Type()
)
gs2328fACLACEICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEICMPCode.setStatus("current")


class _Gs2328fACLACESourcePortMin_Type(Integer32):
    """Custom type gs2328fACLACESourcePortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328fACLACESourcePortMin_Type.__name__ = "Integer32"
_Gs2328fACLACESourcePortMin_Object = MibTableColumn
gs2328fACLACESourcePortMin = _Gs2328fACLACESourcePortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 42),
    _Gs2328fACLACESourcePortMin_Type()
)
gs2328fACLACESourcePortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACESourcePortMin.setStatus("current")


class _Gs2328fACLACESourcePortMax_Type(Integer32):
    """Custom type gs2328fACLACESourcePortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328fACLACESourcePortMax_Type.__name__ = "Integer32"
_Gs2328fACLACESourcePortMax_Object = MibTableColumn
gs2328fACLACESourcePortMax = _Gs2328fACLACESourcePortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 43),
    _Gs2328fACLACESourcePortMax_Type()
)
gs2328fACLACESourcePortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACESourcePortMax.setStatus("current")


class _Gs2328fACLACEDestPortMin_Type(Integer32):
    """Custom type gs2328fACLACEDestPortMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328fACLACEDestPortMin_Type.__name__ = "Integer32"
_Gs2328fACLACEDestPortMin_Object = MibTableColumn
gs2328fACLACEDestPortMin = _Gs2328fACLACEDestPortMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 44),
    _Gs2328fACLACEDestPortMin_Type()
)
gs2328fACLACEDestPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDestPortMin.setStatus("current")


class _Gs2328fACLACEDestPortMax_Type(Integer32):
    """Custom type gs2328fACLACEDestPortMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Gs2328fACLACEDestPortMax_Type.__name__ = "Integer32"
_Gs2328fACLACEDestPortMax_Object = MibTableColumn
gs2328fACLACEDestPortMax = _Gs2328fACLACEDestPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 45),
    _Gs2328fACLACEDestPortMax_Type()
)
gs2328fACLACEDestPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEDestPortMax.setStatus("current")


class _Gs2328fACLACETCPFlagsFin_Type(Integer32):
    """Custom type gs2328fACLACETCPFlagsFin based on Integer32"""
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


_Gs2328fACLACETCPFlagsFin_Type.__name__ = "Integer32"
_Gs2328fACLACETCPFlagsFin_Object = MibTableColumn
gs2328fACLACETCPFlagsFin = _Gs2328fACLACETCPFlagsFin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 46),
    _Gs2328fACLACETCPFlagsFin_Type()
)
gs2328fACLACETCPFlagsFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACETCPFlagsFin.setStatus("current")


class _Gs2328fACLACETCPFlagsSyn_Type(Integer32):
    """Custom type gs2328fACLACETCPFlagsSyn based on Integer32"""
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


_Gs2328fACLACETCPFlagsSyn_Type.__name__ = "Integer32"
_Gs2328fACLACETCPFlagsSyn_Object = MibTableColumn
gs2328fACLACETCPFlagsSyn = _Gs2328fACLACETCPFlagsSyn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 47),
    _Gs2328fACLACETCPFlagsSyn_Type()
)
gs2328fACLACETCPFlagsSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACETCPFlagsSyn.setStatus("current")


class _Gs2328fACLACETCPFlagsRst_Type(Integer32):
    """Custom type gs2328fACLACETCPFlagsRst based on Integer32"""
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


_Gs2328fACLACETCPFlagsRst_Type.__name__ = "Integer32"
_Gs2328fACLACETCPFlagsRst_Object = MibTableColumn
gs2328fACLACETCPFlagsRst = _Gs2328fACLACETCPFlagsRst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 48),
    _Gs2328fACLACETCPFlagsRst_Type()
)
gs2328fACLACETCPFlagsRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACETCPFlagsRst.setStatus("current")


class _Gs2328fACLACETCPFlagsPsh_Type(Integer32):
    """Custom type gs2328fACLACETCPFlagsPsh based on Integer32"""
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


_Gs2328fACLACETCPFlagsPsh_Type.__name__ = "Integer32"
_Gs2328fACLACETCPFlagsPsh_Object = MibTableColumn
gs2328fACLACETCPFlagsPsh = _Gs2328fACLACETCPFlagsPsh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 49),
    _Gs2328fACLACETCPFlagsPsh_Type()
)
gs2328fACLACETCPFlagsPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACETCPFlagsPsh.setStatus("current")


class _Gs2328fACLACETCPFlagsAck_Type(Integer32):
    """Custom type gs2328fACLACETCPFlagsAck based on Integer32"""
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


_Gs2328fACLACETCPFlagsAck_Type.__name__ = "Integer32"
_Gs2328fACLACETCPFlagsAck_Object = MibTableColumn
gs2328fACLACETCPFlagsAck = _Gs2328fACLACETCPFlagsAck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 50),
    _Gs2328fACLACETCPFlagsAck_Type()
)
gs2328fACLACETCPFlagsAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACETCPFlagsAck.setStatus("current")


class _Gs2328fACLACETCPFlagsUrg_Type(Integer32):
    """Custom type gs2328fACLACETCPFlagsUrg based on Integer32"""
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


_Gs2328fACLACETCPFlagsUrg_Type.__name__ = "Integer32"
_Gs2328fACLACETCPFlagsUrg_Object = MibTableColumn
gs2328fACLACETCPFlagsUrg = _Gs2328fACLACETCPFlagsUrg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 51),
    _Gs2328fACLACETCPFlagsUrg_Type()
)
gs2328fACLACETCPFlagsUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACETCPFlagsUrg.setStatus("current")


class _Gs2328fACLACERowStatus_Type(Integer32):
    """Custom type gs2328fACLACERowStatus based on Integer32"""
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


_Gs2328fACLACERowStatus_Type.__name__ = "Integer32"
_Gs2328fACLACERowStatus_Object = MibTableColumn
gs2328fACLACERowStatus = _Gs2328fACLACERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 2, 1, 66),
    _Gs2328fACLACERowStatus_Type()
)
gs2328fACLACERowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACERowStatus.setStatus("current")


class _Gs2328fACLACEClear_Type(Integer32):
    """Custom type gs2328fACLACEClear based on Integer32"""
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


_Gs2328fACLACEClear_Type.__name__ = "Integer32"
_Gs2328fACLACEClear_Object = MibScalar
gs2328fACLACEClear = _Gs2328fACLACEClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 3),
    _Gs2328fACLACEClear_Type()
)
gs2328fACLACEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEClear.setStatus("current")


class _Gs2328fACLACEMoveACEID_Type(Integer32):
    """Custom type gs2328fACLACEMoveACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328fACLACEMoveACEID_Type.__name__ = "Integer32"
_Gs2328fACLACEMoveACEID_Object = MibScalar
gs2328fACLACEMoveACEID = _Gs2328fACLACEMoveACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 4),
    _Gs2328fACLACEMoveACEID_Type()
)
gs2328fACLACEMoveACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEMoveACEID.setStatus("current")


class _Gs2328fACLACEMoveNextACEID_Type(Integer32):
    """Custom type gs2328fACLACEMoveNextACEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328fACLACEMoveNextACEID_Type.__name__ = "Integer32"
_Gs2328fACLACEMoveNextACEID_Object = MibScalar
gs2328fACLACEMoveNextACEID = _Gs2328fACLACEMoveNextACEID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 5),
    _Gs2328fACLACEMoveNextACEID_Type()
)
gs2328fACLACEMoveNextACEID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fACLACEMoveNextACEID.setStatus("current")
_Gs2328fACLACEStatusTable_Object = MibTable
gs2328fACLACEStatusTable = _Gs2328fACLACEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6)
)
if mibBuilder.loadTexts:
    gs2328fACLACEStatusTable.setStatus("current")
_Gs2328fACLACEStatusEntry_Object = MibTableRow
gs2328fACLACEStatusEntry = _Gs2328fACLACEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1)
)
gs2328fACLACEStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fACLACEStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2328fACLACEStatusEntry.setStatus("current")


class _Gs2328fACLACEStatusIndex_Type(Integer32):
    """Custom type gs2328fACLACEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fACLACEStatusIndex_Type.__name__ = "Integer32"
_Gs2328fACLACEStatusIndex_Object = MibTableColumn
gs2328fACLACEStatusIndex = _Gs2328fACLACEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 1),
    _Gs2328fACLACEStatusIndex_Type()
)
gs2328fACLACEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusIndex.setStatus("current")
_Gs2328fACLACEStatusUser_Type = DisplayString
_Gs2328fACLACEStatusUser_Object = MibTableColumn
gs2328fACLACEStatusUser = _Gs2328fACLACEStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 2),
    _Gs2328fACLACEStatusUser_Type()
)
gs2328fACLACEStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusUser.setStatus("current")


class _Gs2328fACLACEStatusID_Type(Integer32):
    """Custom type gs2328fACLACEStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fACLACEStatusID_Type.__name__ = "Integer32"
_Gs2328fACLACEStatusID_Object = MibTableColumn
gs2328fACLACEStatusID = _Gs2328fACLACEStatusID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 3),
    _Gs2328fACLACEStatusID_Type()
)
gs2328fACLACEStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusID.setStatus("current")
_Gs2328fACLACEStatusIngressPort_Type = DisplayString
_Gs2328fACLACEStatusIngressPort_Object = MibTableColumn
gs2328fACLACEStatusIngressPort = _Gs2328fACLACEStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 4),
    _Gs2328fACLACEStatusIngressPort_Type()
)
gs2328fACLACEStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusIngressPort.setStatus("current")
_Gs2328fACLACEStatusFrameType_Type = DisplayString
_Gs2328fACLACEStatusFrameType_Object = MibTableColumn
gs2328fACLACEStatusFrameType = _Gs2328fACLACEStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 5),
    _Gs2328fACLACEStatusFrameType_Type()
)
gs2328fACLACEStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusFrameType.setStatus("current")
_Gs2328fACLACEStatusAction_Type = DisplayString
_Gs2328fACLACEStatusAction_Object = MibTableColumn
gs2328fACLACEStatusAction = _Gs2328fACLACEStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 6),
    _Gs2328fACLACEStatusAction_Type()
)
gs2328fACLACEStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusAction.setStatus("current")
_Gs2328fACLACEStatusRateLimiter_Type = DisplayString
_Gs2328fACLACEStatusRateLimiter_Object = MibTableColumn
gs2328fACLACEStatusRateLimiter = _Gs2328fACLACEStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 7),
    _Gs2328fACLACEStatusRateLimiter_Type()
)
gs2328fACLACEStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusRateLimiter.setStatus("current")
_Gs2328fACLACEStatusPortCopy_Type = DisplayString
_Gs2328fACLACEStatusPortCopy_Object = MibTableColumn
gs2328fACLACEStatusPortCopy = _Gs2328fACLACEStatusPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 8),
    _Gs2328fACLACEStatusPortCopy_Type()
)
gs2328fACLACEStatusPortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusPortCopy.setStatus("current")
_Gs2328fACLACEStatusMirror_Type = DisplayString
_Gs2328fACLACEStatusMirror_Object = MibTableColumn
gs2328fACLACEStatusMirror = _Gs2328fACLACEStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 9),
    _Gs2328fACLACEStatusMirror_Type()
)
gs2328fACLACEStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusMirror.setStatus("current")
_Gs2328fACLACEStatusCPU_Type = DisplayString
_Gs2328fACLACEStatusCPU_Object = MibTableColumn
gs2328fACLACEStatusCPU = _Gs2328fACLACEStatusCPU_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 10),
    _Gs2328fACLACEStatusCPU_Type()
)
gs2328fACLACEStatusCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusCPU.setStatus("current")
_Gs2328fACLACEStatusCounter_Type = Counter32
_Gs2328fACLACEStatusCounter_Object = MibTableColumn
gs2328fACLACEStatusCounter = _Gs2328fACLACEStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 11),
    _Gs2328fACLACEStatusCounter_Type()
)
gs2328fACLACEStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusCounter.setStatus("current")
_Gs2328fACLACEStatusConflict_Type = DisplayString
_Gs2328fACLACEStatusConflict_Object = MibTableColumn
gs2328fACLACEStatusConflict = _Gs2328fACLACEStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 9, 3, 6, 1, 12),
    _Gs2328fACLACEStatusConflict_Type()
)
gs2328fACLACEStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fACLACEStatusConflict.setStatus("current")
_Gs2328fLoopProtection_ObjectIdentity = ObjectIdentity
gs2328fLoopProtection = _Gs2328fLoopProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12)
)
_Gs2328fLoopProtectionConfig_ObjectIdentity = ObjectIdentity
gs2328fLoopProtectionConfig = _Gs2328fLoopProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1)
)


class _Gs2328fLoopProtectionGlobalEnable_Type(Integer32):
    """Custom type gs2328fLoopProtectionGlobalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fLoopProtectionGlobalEnable_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionGlobalEnable_Object = MibScalar
gs2328fLoopProtectionGlobalEnable = _Gs2328fLoopProtectionGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 1),
    _Gs2328fLoopProtectionGlobalEnable_Type()
)
gs2328fLoopProtectionGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionGlobalEnable.setStatus("current")


class _Gs2328fLoopProtectionTranmisstionTime_Type(Integer32):
    """Custom type gs2328fLoopProtectionTranmisstionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328fLoopProtectionTranmisstionTime_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionTranmisstionTime_Object = MibScalar
gs2328fLoopProtectionTranmisstionTime = _Gs2328fLoopProtectionTranmisstionTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 2),
    _Gs2328fLoopProtectionTranmisstionTime_Type()
)
gs2328fLoopProtectionTranmisstionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionTranmisstionTime.setStatus("current")


class _Gs2328fLoopProtectionShutdownTime_Type(Integer32):
    """Custom type gs2328fLoopProtectionShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_Gs2328fLoopProtectionShutdownTime_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionShutdownTime_Object = MibScalar
gs2328fLoopProtectionShutdownTime = _Gs2328fLoopProtectionShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 3),
    _Gs2328fLoopProtectionShutdownTime_Type()
)
gs2328fLoopProtectionShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionShutdownTime.setStatus("current")
_Gs2328fLoopProtectionConfigurationTable_Object = MibTable
gs2328fLoopProtectionConfigurationTable = _Gs2328fLoopProtectionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    gs2328fLoopProtectionConfigurationTable.setStatus("current")
_Gs2328fLoopProtectionConfigurationEntry_Object = MibTableRow
gs2328fLoopProtectionConfigurationEntry = _Gs2328fLoopProtectionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 4, 1)
)
gs2328fLoopProtectionConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fLoopProtectionConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fLoopProtectionConfigurationEntry.setStatus("current")


class _Gs2328fLoopProtectionConfPort_Type(Integer32):
    """Custom type gs2328fLoopProtectionConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fLoopProtectionConfPort_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionConfPort_Object = MibTableColumn
gs2328fLoopProtectionConfPort = _Gs2328fLoopProtectionConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 4, 1, 1),
    _Gs2328fLoopProtectionConfPort_Type()
)
gs2328fLoopProtectionConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionConfPort.setStatus("current")


class _Gs2328fLoopProtectionConfEnable_Type(Integer32):
    """Custom type gs2328fLoopProtectionConfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fLoopProtectionConfEnable_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionConfEnable_Object = MibTableColumn
gs2328fLoopProtectionConfEnable = _Gs2328fLoopProtectionConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 4, 1, 2),
    _Gs2328fLoopProtectionConfEnable_Type()
)
gs2328fLoopProtectionConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionConfEnable.setStatus("current")


class _Gs2328fLoopProtectionConfAction_Type(Integer32):
    """Custom type gs2328fLoopProtectionConfAction based on Integer32"""
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


_Gs2328fLoopProtectionConfAction_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionConfAction_Object = MibTableColumn
gs2328fLoopProtectionConfAction = _Gs2328fLoopProtectionConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 4, 1, 3),
    _Gs2328fLoopProtectionConfAction_Type()
)
gs2328fLoopProtectionConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionConfAction.setStatus("current")


class _Gs2328fLoopProtectionConfTxmode_Type(Integer32):
    """Custom type gs2328fLoopProtectionConfTxmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fLoopProtectionConfTxmode_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionConfTxmode_Object = MibTableColumn
gs2328fLoopProtectionConfTxmode = _Gs2328fLoopProtectionConfTxmode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 1, 4, 1, 4),
    _Gs2328fLoopProtectionConfTxmode_Type()
)
gs2328fLoopProtectionConfTxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionConfTxmode.setStatus("current")
_Gs2328fLoopProtectionStatusTable_Object = MibTable
gs2328fLoopProtectionStatusTable = _Gs2328fLoopProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2)
)
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusTable.setStatus("current")
_Gs2328fLoopProtectionStatusEntry_Object = MibTableRow
gs2328fLoopProtectionStatusEntry = _Gs2328fLoopProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1)
)
gs2328fLoopProtectionStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fLoopProtectionStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusEntry.setStatus("current")


class _Gs2328fLoopProtectionStatusPort_Type(Integer32):
    """Custom type gs2328fLoopProtectionStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fLoopProtectionStatusPort_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionStatusPort_Object = MibTableColumn
gs2328fLoopProtectionStatusPort = _Gs2328fLoopProtectionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 1),
    _Gs2328fLoopProtectionStatusPort_Type()
)
gs2328fLoopProtectionStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusPort.setStatus("current")
_Gs2328fLoopProtectionStatusAction_Type = DisplayString
_Gs2328fLoopProtectionStatusAction_Object = MibTableColumn
gs2328fLoopProtectionStatusAction = _Gs2328fLoopProtectionStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 2),
    _Gs2328fLoopProtectionStatusAction_Type()
)
gs2328fLoopProtectionStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusAction.setStatus("current")
_Gs2328fLoopProtectionStatusTransmit_Type = DisplayString
_Gs2328fLoopProtectionStatusTransmit_Object = MibTableColumn
gs2328fLoopProtectionStatusTransmit = _Gs2328fLoopProtectionStatusTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 3),
    _Gs2328fLoopProtectionStatusTransmit_Type()
)
gs2328fLoopProtectionStatusTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusTransmit.setStatus("current")


class _Gs2328fLoopProtectionStatusLoops_Type(Integer32):
    """Custom type gs2328fLoopProtectionStatusLoops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2328fLoopProtectionStatusLoops_Type.__name__ = "Integer32"
_Gs2328fLoopProtectionStatusLoops_Object = MibTableColumn
gs2328fLoopProtectionStatusLoops = _Gs2328fLoopProtectionStatusLoops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 4),
    _Gs2328fLoopProtectionStatusLoops_Type()
)
gs2328fLoopProtectionStatusLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusLoops.setStatus("current")
_Gs2328fLoopProtectionStatusStatus_Type = DisplayString
_Gs2328fLoopProtectionStatusStatus_Object = MibTableColumn
gs2328fLoopProtectionStatusStatus = _Gs2328fLoopProtectionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 5),
    _Gs2328fLoopProtectionStatusStatus_Type()
)
gs2328fLoopProtectionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusStatus.setStatus("current")
_Gs2328fLoopProtectionStatusLoop_Type = DisplayString
_Gs2328fLoopProtectionStatusLoop_Object = MibTableColumn
gs2328fLoopProtectionStatusLoop = _Gs2328fLoopProtectionStatusLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 6),
    _Gs2328fLoopProtectionStatusLoop_Type()
)
gs2328fLoopProtectionStatusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusLoop.setStatus("current")
_Gs2328fLoopProtectionStatusTimeLastLoop_Type = DisplayString
_Gs2328fLoopProtectionStatusTimeLastLoop_Object = MibTableColumn
gs2328fLoopProtectionStatusTimeLastLoop = _Gs2328fLoopProtectionStatusTimeLastLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 12, 2, 1, 7),
    _Gs2328fLoopProtectionStatusTimeLastLoop_Type()
)
gs2328fLoopProtectionStatusTimeLastLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLoopProtectionStatusTimeLastLoop.setStatus("current")
_Gs2328fQos_ObjectIdentity = ObjectIdentity
gs2328fQos = _Gs2328fQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14)
)
_Gs2328fQosPortClassification_ObjectIdentity = ObjectIdentity
gs2328fQosPortClassification = _Gs2328fQosPortClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1)
)
_Gs2328fQosPortClassificationTable_Object = MibTable
gs2328fQosPortClassificationTable = _Gs2328fQosPortClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationTable.setStatus("current")
_Gs2328fQosPortClassificationEntry_Object = MibTableRow
gs2328fQosPortClassificationEntry = _Gs2328fQosPortClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1)
)
gs2328fQosPortClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosPortClassificationPort"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationEntry.setStatus("current")


class _Gs2328fQosPortClassificationPort_Type(Integer32):
    """Custom type gs2328fQosPortClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosPortClassificationPort_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationPort_Object = MibTableColumn
gs2328fQosPortClassificationPort = _Gs2328fQosPortClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 1),
    _Gs2328fQosPortClassificationPort_Type()
)
gs2328fQosPortClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationPort.setStatus("current")


class _Gs2328fQosPortClassificationQoSclass_Type(Integer32):
    """Custom type gs2328fQosPortClassificationQoSclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fQosPortClassificationQoSclass_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationQoSclass_Object = MibTableColumn
gs2328fQosPortClassificationQoSclass = _Gs2328fQosPortClassificationQoSclass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 2),
    _Gs2328fQosPortClassificationQoSclass_Type()
)
gs2328fQosPortClassificationQoSclass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationQoSclass.setStatus("current")


class _Gs2328fQosPortClassificationDPlevel_Type(Integer32):
    """Custom type gs2328fQosPortClassificationDPlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328fQosPortClassificationDPlevel_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationDPlevel_Object = MibTableColumn
gs2328fQosPortClassificationDPlevel = _Gs2328fQosPortClassificationDPlevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 3),
    _Gs2328fQosPortClassificationDPlevel_Type()
)
gs2328fQosPortClassificationDPlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationDPlevel.setStatus("current")


class _Gs2328fQosPortClassificationPCP_Type(Integer32):
    """Custom type gs2328fQosPortClassificationPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fQosPortClassificationPCP_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationPCP_Object = MibTableColumn
gs2328fQosPortClassificationPCP = _Gs2328fQosPortClassificationPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 4),
    _Gs2328fQosPortClassificationPCP_Type()
)
gs2328fQosPortClassificationPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationPCP.setStatus("current")


class _Gs2328fQosPortClassificationDEI_Type(Integer32):
    """Custom type gs2328fQosPortClassificationDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosPortClassificationDEI_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationDEI_Object = MibTableColumn
gs2328fQosPortClassificationDEI = _Gs2328fQosPortClassificationDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 5),
    _Gs2328fQosPortClassificationDEI_Type()
)
gs2328fQosPortClassificationDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationDEI.setStatus("current")


class _Gs2328fQosPortClassificationTagClass_Type(Integer32):
    """Custom type gs2328fQosPortClassificationTagClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosPortClassificationTagClass_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationTagClass_Object = MibTableColumn
gs2328fQosPortClassificationTagClass = _Gs2328fQosPortClassificationTagClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 6),
    _Gs2328fQosPortClassificationTagClass_Type()
)
gs2328fQosPortClassificationTagClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationTagClass.setStatus("current")


class _Gs2328fQosPortClassificationDSCPBased_Type(Integer32):
    """Custom type gs2328fQosPortClassificationDSCPBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosPortClassificationDSCPBased_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationDSCPBased_Object = MibTableColumn
gs2328fQosPortClassificationDSCPBased = _Gs2328fQosPortClassificationDSCPBased_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 7),
    _Gs2328fQosPortClassificationDSCPBased_Type()
)
gs2328fQosPortClassificationDSCPBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationDSCPBased.setStatus("current")


class _Gs2328fQosPortClassificationAddressMode_Type(Integer32):
    """Custom type gs2328fQosPortClassificationAddressMode based on Integer32"""
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


_Gs2328fQosPortClassificationAddressMode_Type.__name__ = "Integer32"
_Gs2328fQosPortClassificationAddressMode_Object = MibTableColumn
gs2328fQosPortClassificationAddressMode = _Gs2328fQosPortClassificationAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 1, 1, 8),
    _Gs2328fQosPortClassificationAddressMode_Type()
)
gs2328fQosPortClassificationAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortClassificationAddressMode.setStatus("current")
_Gs2328fQoSIngressPortTagClassificationTable_Object = MibTable
gs2328fQoSIngressPortTagClassificationTable = _Gs2328fQoSIngressPortTagClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagClassificationTable.setStatus("current")
_Gs2328fQoSIngressPortTagClassificationEntry_Object = MibTableRow
gs2328fQoSIngressPortTagClassificationEntry = _Gs2328fQoSIngressPortTagClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2, 1)
)
gs2328fQoSIngressPortTagClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQoSIngressPortTagClassificationPort"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQoSIngressPortTagPCP"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQoSIngressPortTagDEI"),
)
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagClassificationEntry.setStatus("current")


class _Gs2328fQoSIngressPortTagClassificationPort_Type(Integer32):
    """Custom type gs2328fQoSIngressPortTagClassificationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQoSIngressPortTagClassificationPort_Type.__name__ = "Integer32"
_Gs2328fQoSIngressPortTagClassificationPort_Object = MibTableColumn
gs2328fQoSIngressPortTagClassificationPort = _Gs2328fQoSIngressPortTagClassificationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2, 1, 1),
    _Gs2328fQoSIngressPortTagClassificationPort_Type()
)
gs2328fQoSIngressPortTagClassificationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagClassificationPort.setStatus("current")


class _Gs2328fQoSIngressPortTagPCP_Type(Integer32):
    """Custom type gs2328fQoSIngressPortTagPCP based on Integer32"""
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


_Gs2328fQoSIngressPortTagPCP_Type.__name__ = "Integer32"
_Gs2328fQoSIngressPortTagPCP_Object = MibTableColumn
gs2328fQoSIngressPortTagPCP = _Gs2328fQoSIngressPortTagPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2, 1, 2),
    _Gs2328fQoSIngressPortTagPCP_Type()
)
gs2328fQoSIngressPortTagPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagPCP.setStatus("current")


class _Gs2328fQoSIngressPortTagDEI_Type(Integer32):
    """Custom type gs2328fQoSIngressPortTagDEI based on Integer32"""
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


_Gs2328fQoSIngressPortTagDEI_Type.__name__ = "Integer32"
_Gs2328fQoSIngressPortTagDEI_Object = MibTableColumn
gs2328fQoSIngressPortTagDEI = _Gs2328fQoSIngressPortTagDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2, 1, 3),
    _Gs2328fQoSIngressPortTagDEI_Type()
)
gs2328fQoSIngressPortTagDEI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagDEI.setStatus("current")


class _Gs2328fQoSIngressPortTagQosClass_Type(Integer32):
    """Custom type gs2328fQoSIngressPortTagQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fQoSIngressPortTagQosClass_Type.__name__ = "Integer32"
_Gs2328fQoSIngressPortTagQosClass_Object = MibTableColumn
gs2328fQoSIngressPortTagQosClass = _Gs2328fQoSIngressPortTagQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2, 1, 4),
    _Gs2328fQoSIngressPortTagQosClass_Type()
)
gs2328fQoSIngressPortTagQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagQosClass.setStatus("current")


class _Gs2328fQoSIngressPortTagDPLevel_Type(Integer32):
    """Custom type gs2328fQoSIngressPortTagDPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328fQoSIngressPortTagDPLevel_Type.__name__ = "Integer32"
_Gs2328fQoSIngressPortTagDPLevel_Object = MibTableColumn
gs2328fQoSIngressPortTagDPLevel = _Gs2328fQoSIngressPortTagDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 1, 2, 1, 5),
    _Gs2328fQoSIngressPortTagDPLevel_Type()
)
gs2328fQoSIngressPortTagDPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSIngressPortTagDPLevel.setStatus("current")
_Gs2328fQosPortPolicingTable_Object = MibTable
gs2328fQosPortPolicingTable = _Gs2328fQosPortPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingTable.setStatus("current")
_Gs2328fQosPortPolicingEntry_Object = MibTableRow
gs2328fQosPortPolicingEntry = _Gs2328fQosPortPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2, 1)
)
gs2328fQosPortPolicingEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosPortPolicingPort"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingEntry.setStatus("current")


class _Gs2328fQosPortPolicingPort_Type(Integer32):
    """Custom type gs2328fQosPortPolicingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosPortPolicingPort_Type.__name__ = "Integer32"
_Gs2328fQosPortPolicingPort_Object = MibTableColumn
gs2328fQosPortPolicingPort = _Gs2328fQosPortPolicingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2, 1, 1),
    _Gs2328fQosPortPolicingPort_Type()
)
gs2328fQosPortPolicingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingPort.setStatus("current")


class _Gs2328fQosPortPolicingMode_Type(Integer32):
    """Custom type gs2328fQosPortPolicingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosPortPolicingMode_Type.__name__ = "Integer32"
_Gs2328fQosPortPolicingMode_Object = MibTableColumn
gs2328fQosPortPolicingMode = _Gs2328fQosPortPolicingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2, 1, 2),
    _Gs2328fQosPortPolicingMode_Type()
)
gs2328fQosPortPolicingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingMode.setStatus("current")


class _Gs2328fQosPortPolicingRate_Type(Integer32):
    """Custom type gs2328fQosPortPolicingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_Gs2328fQosPortPolicingRate_Type.__name__ = "Integer32"
_Gs2328fQosPortPolicingRate_Object = MibTableColumn
gs2328fQosPortPolicingRate = _Gs2328fQosPortPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2, 1, 3),
    _Gs2328fQosPortPolicingRate_Type()
)
gs2328fQosPortPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingRate.setStatus("current")


class _Gs2328fQosPortPolicingUnit_Type(Integer32):
    """Custom type gs2328fQosPortPolicingUnit based on Integer32"""
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


_Gs2328fQosPortPolicingUnit_Type.__name__ = "Integer32"
_Gs2328fQosPortPolicingUnit_Object = MibTableColumn
gs2328fQosPortPolicingUnit = _Gs2328fQosPortPolicingUnit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2, 1, 4),
    _Gs2328fQosPortPolicingUnit_Type()
)
gs2328fQosPortPolicingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingUnit.setStatus("current")


class _Gs2328fQosPortPolicingFlowControl_Type(Integer32):
    """Custom type gs2328fQosPortPolicingFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosPortPolicingFlowControl_Type.__name__ = "Integer32"
_Gs2328fQosPortPolicingFlowControl_Object = MibTableColumn
gs2328fQosPortPolicingFlowControl = _Gs2328fQosPortPolicingFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 2, 1, 5),
    _Gs2328fQosPortPolicingFlowControl_Type()
)
gs2328fQosPortPolicingFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortPolicingFlowControl.setStatus("current")
_Gs2328fQosPortScheduler_ObjectIdentity = ObjectIdentity
gs2328fQosPortScheduler = _Gs2328fQosPortScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3)
)
_Gs2328fQosPortSchedulerModeTable_Object = MibTable
gs2328fQosPortSchedulerModeTable = _Gs2328fQosPortSchedulerModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 1)
)
if mibBuilder.loadTexts:
    gs2328fQosPortSchedulerModeTable.setStatus("current")
_Gs2328fQosPortSchedulerModeEntry_Object = MibTableRow
gs2328fQosPortSchedulerModeEntry = _Gs2328fQosPortSchedulerModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 1, 1)
)
gs2328fQosPortSchedulerModeEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosSchedulerModePort"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortSchedulerModeEntry.setStatus("current")


class _Gs2328fQosSchedulerModePort_Type(Integer32):
    """Custom type gs2328fQosSchedulerModePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosSchedulerModePort_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerModePort_Object = MibTableColumn
gs2328fQosSchedulerModePort = _Gs2328fQosSchedulerModePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 1, 1, 1),
    _Gs2328fQosSchedulerModePort_Type()
)
gs2328fQosSchedulerModePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerModePort.setStatus("current")


class _Gs2328fQosSchedulerMode_Type(Integer32):
    """Custom type gs2328fQosSchedulerMode based on Integer32"""
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


_Gs2328fQosSchedulerMode_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerMode_Object = MibTableColumn
gs2328fQosSchedulerMode = _Gs2328fQosSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 1, 1, 2),
    _Gs2328fQosSchedulerMode_Type()
)
gs2328fQosSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerMode.setStatus("current")


class _Gs2328fQosSchedulerShaper_Type(Integer32):
    """Custom type gs2328fQosSchedulerShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosSchedulerShaper_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerShaper_Object = MibTableColumn
gs2328fQosSchedulerShaper = _Gs2328fQosSchedulerShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 1, 1, 3),
    _Gs2328fQosSchedulerShaper_Type()
)
gs2328fQosSchedulerShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerShaper.setStatus("current")


class _Gs2328fQosSchedulerShaperRate_Type(Integer32):
    """Custom type gs2328fQosSchedulerShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2328fQosSchedulerShaperRate_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerShaperRate_Object = MibTableColumn
gs2328fQosSchedulerShaperRate = _Gs2328fQosSchedulerShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 1, 1, 4),
    _Gs2328fQosSchedulerShaperRate_Type()
)
gs2328fQosSchedulerShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerShaperRate.setStatus("current")
_Gs2328fQosPortSchedulerTable_Object = MibTable
gs2328fQosPortSchedulerTable = _Gs2328fQosPortSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fQosPortSchedulerTable.setStatus("current")
_Gs2328fQosPortSchedulerEntry_Object = MibTableRow
gs2328fQosPortSchedulerEntry = _Gs2328fQosPortSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1)
)
gs2328fQosPortSchedulerEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosSchedulerPort"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosSchedulerPortQueue"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortSchedulerEntry.setStatus("current")


class _Gs2328fQosSchedulerPort_Type(Integer32):
    """Custom type gs2328fQosSchedulerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosSchedulerPort_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerPort_Object = MibTableColumn
gs2328fQosSchedulerPort = _Gs2328fQosSchedulerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 1),
    _Gs2328fQosSchedulerPort_Type()
)
gs2328fQosSchedulerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPort.setStatus("current")


class _Gs2328fQosSchedulerPortQueue_Type(Integer32):
    """Custom type gs2328fQosSchedulerPortQueue based on Integer32"""
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


_Gs2328fQosSchedulerPortQueue_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerPortQueue_Object = MibTableColumn
gs2328fQosSchedulerPortQueue = _Gs2328fQosSchedulerPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 2),
    _Gs2328fQosSchedulerPortQueue_Type()
)
gs2328fQosSchedulerPortQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPortQueue.setStatus("current")


class _Gs2328fQosSchedulerPortQueueShaper_Type(Integer32):
    """Custom type gs2328fQosSchedulerPortQueueShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosSchedulerPortQueueShaper_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerPortQueueShaper_Object = MibTableColumn
gs2328fQosSchedulerPortQueueShaper = _Gs2328fQosSchedulerPortQueueShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 3),
    _Gs2328fQosSchedulerPortQueueShaper_Type()
)
gs2328fQosSchedulerPortQueueShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPortQueueShaper.setStatus("current")


class _Gs2328fQosSchedulerPortQueueShaperRate_Type(Integer32):
    """Custom type gs2328fQosSchedulerPortQueueShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_Gs2328fQosSchedulerPortQueueShaperRate_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerPortQueueShaperRate_Object = MibTableColumn
gs2328fQosSchedulerPortQueueShaperRate = _Gs2328fQosSchedulerPortQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 4),
    _Gs2328fQosSchedulerPortQueueShaperRate_Type()
)
gs2328fQosSchedulerPortQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPortQueueShaperRate.setStatus("current")


class _Gs2328fQosSchedulerPortQueueShaperExcess_Type(Integer32):
    """Custom type gs2328fQosSchedulerPortQueueShaperExcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosSchedulerPortQueueShaperExcess_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerPortQueueShaperExcess_Object = MibTableColumn
gs2328fQosSchedulerPortQueueShaperExcess = _Gs2328fQosSchedulerPortQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 5),
    _Gs2328fQosSchedulerPortQueueShaperExcess_Type()
)
gs2328fQosSchedulerPortQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPortQueueShaperExcess.setStatus("current")


class _Gs2328fQosSchedulerPortQueueSchedulerWeight_Type(Integer32):
    """Custom type gs2328fQosSchedulerPortQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Gs2328fQosSchedulerPortQueueSchedulerWeight_Type.__name__ = "Integer32"
_Gs2328fQosSchedulerPortQueueSchedulerWeight_Object = MibTableColumn
gs2328fQosSchedulerPortQueueSchedulerWeight = _Gs2328fQosSchedulerPortQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 6),
    _Gs2328fQosSchedulerPortQueueSchedulerWeight_Type()
)
gs2328fQosSchedulerPortQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPortQueueSchedulerWeight.setStatus("current")
_Gs2328fQosSchedulerPortQueueSchedulerPercent_Type = DisplayString
_Gs2328fQosSchedulerPortQueueSchedulerPercent_Object = MibTableColumn
gs2328fQosSchedulerPortQueueSchedulerPercent = _Gs2328fQosSchedulerPortQueueSchedulerPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 3, 2, 1, 7),
    _Gs2328fQosSchedulerPortQueueSchedulerPercent_Type()
)
gs2328fQosSchedulerPortQueueSchedulerPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosSchedulerPortQueueSchedulerPercent.setStatus("current")
_Gs2328fQosPortEgressTagRemarking_ObjectIdentity = ObjectIdentity
gs2328fQosPortEgressTagRemarking = _Gs2328fQosPortEgressTagRemarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4)
)
_Gs2328fQosPortEgressTagRemarkingTable_Object = MibTable
gs2328fQosPortEgressTagRemarkingTable = _Gs2328fQosPortEgressTagRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 1)
)
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingTable.setStatus("current")
_Gs2328fQosPortEgressTagRemarkingEntry_Object = MibTableRow
gs2328fQosPortEgressTagRemarkingEntry = _Gs2328fQosPortEgressTagRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 1, 1)
)
gs2328fQosPortEgressTagRemarkingEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosEgressTagRemarkingPort"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingEntry.setStatus("current")


class _Gs2328fQosEgressTagRemarkingPort_Type(Integer32):
    """Custom type gs2328fQosEgressTagRemarkingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosEgressTagRemarkingPort_Type.__name__ = "Integer32"
_Gs2328fQosEgressTagRemarkingPort_Object = MibTableColumn
gs2328fQosEgressTagRemarkingPort = _Gs2328fQosEgressTagRemarkingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 1, 1, 1),
    _Gs2328fQosEgressTagRemarkingPort_Type()
)
gs2328fQosEgressTagRemarkingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosEgressTagRemarkingPort.setStatus("current")


class _Gs2328fQosEgressTagRemarkingMode_Type(Integer32):
    """Custom type gs2328fQosEgressTagRemarkingMode based on Integer32"""
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


_Gs2328fQosEgressTagRemarkingMode_Type.__name__ = "Integer32"
_Gs2328fQosEgressTagRemarkingMode_Object = MibTableColumn
gs2328fQosEgressTagRemarkingMode = _Gs2328fQosEgressTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 1, 1, 2),
    _Gs2328fQosEgressTagRemarkingMode_Type()
)
gs2328fQosEgressTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosEgressTagRemarkingMode.setStatus("current")
_Gs2328fQosPortEgressTagRemarkingDefTable_Object = MibTable
gs2328fQosPortEgressTagRemarkingDefTable = _Gs2328fQosPortEgressTagRemarkingDefTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingDefTable.setStatus("current")
_Gs2328fQosPortEgressTagRemarkingDefEntry_Object = MibTableRow
gs2328fQosPortEgressTagRemarkingDefEntry = _Gs2328fQosPortEgressTagRemarkingDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 2, 1)
)
gs2328fQosPortEgressTagRemarkingDefEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosEgressTagRemarkingDefPort"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingDefEntry.setStatus("current")


class _Gs2328fQosEgressTagRemarkingDefPort_Type(Integer32):
    """Custom type gs2328fQosEgressTagRemarkingDefPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosEgressTagRemarkingDefPort_Type.__name__ = "Integer32"
_Gs2328fQosEgressTagRemarkingDefPort_Object = MibTableColumn
gs2328fQosEgressTagRemarkingDefPort = _Gs2328fQosEgressTagRemarkingDefPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 2, 1, 1),
    _Gs2328fQosEgressTagRemarkingDefPort_Type()
)
gs2328fQosEgressTagRemarkingDefPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosEgressTagRemarkingDefPort.setStatus("current")


class _Gs2328fQosEgressTagRemarkingDefPCP_Type(Integer32):
    """Custom type gs2328fQosEgressTagRemarkingDefPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fQosEgressTagRemarkingDefPCP_Type.__name__ = "Integer32"
_Gs2328fQosEgressTagRemarkingDefPCP_Object = MibTableColumn
gs2328fQosEgressTagRemarkingDefPCP = _Gs2328fQosEgressTagRemarkingDefPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 2, 1, 2),
    _Gs2328fQosEgressTagRemarkingDefPCP_Type()
)
gs2328fQosEgressTagRemarkingDefPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosEgressTagRemarkingDefPCP.setStatus("current")


class _Gs2328fQosEgressTagRemarkingDefDEI_Type(Integer32):
    """Custom type gs2328fQosEgressTagRemarkingDefDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosEgressTagRemarkingDefDEI_Type.__name__ = "Integer32"
_Gs2328fQosEgressTagRemarkingDefDEI_Object = MibTableColumn
gs2328fQosEgressTagRemarkingDefDEI = _Gs2328fQosEgressTagRemarkingDefDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 2, 1, 3),
    _Gs2328fQosEgressTagRemarkingDefDEI_Type()
)
gs2328fQosEgressTagRemarkingDefDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosEgressTagRemarkingDefDEI.setStatus("current")
_Gs2328fQosPortEgressTagRemarkingMapTable_Object = MibTable
gs2328fQosPortEgressTagRemarkingMapTable = _Gs2328fQosPortEgressTagRemarkingMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4)
)
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingMapTable.setStatus("current")
_Gs2328fQosPortEgressTagRemarkingMapEntry_Object = MibTableRow
gs2328fQosPortEgressTagRemarkingMapEntry = _Gs2328fQosPortEgressTagRemarkingMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4, 1)
)
gs2328fQosPortEgressTagRemarkingMapEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosPortEgressTagRemarkingMapPort"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosTagRemarkingQoSClass"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosTagRemarkingDPLevel"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingMapEntry.setStatus("current")


class _Gs2328fQosPortEgressTagRemarkingMapPort_Type(Integer32):
    """Custom type gs2328fQosPortEgressTagRemarkingMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosPortEgressTagRemarkingMapPort_Type.__name__ = "Integer32"
_Gs2328fQosPortEgressTagRemarkingMapPort_Object = MibTableColumn
gs2328fQosPortEgressTagRemarkingMapPort = _Gs2328fQosPortEgressTagRemarkingMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4, 1, 1),
    _Gs2328fQosPortEgressTagRemarkingMapPort_Type()
)
gs2328fQosPortEgressTagRemarkingMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosPortEgressTagRemarkingMapPort.setStatus("current")


class _Gs2328fQosTagRemarkingQoSClass_Type(Integer32):
    """Custom type gs2328fQosTagRemarkingQoSClass based on Integer32"""
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


_Gs2328fQosTagRemarkingQoSClass_Type.__name__ = "Integer32"
_Gs2328fQosTagRemarkingQoSClass_Object = MibTableColumn
gs2328fQosTagRemarkingQoSClass = _Gs2328fQosTagRemarkingQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4, 1, 2),
    _Gs2328fQosTagRemarkingQoSClass_Type()
)
gs2328fQosTagRemarkingQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosTagRemarkingQoSClass.setStatus("current")


class _Gs2328fQosTagRemarkingDPLevel_Type(Integer32):
    """Custom type gs2328fQosTagRemarkingDPLevel based on Integer32"""
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


_Gs2328fQosTagRemarkingDPLevel_Type.__name__ = "Integer32"
_Gs2328fQosTagRemarkingDPLevel_Object = MibTableColumn
gs2328fQosTagRemarkingDPLevel = _Gs2328fQosTagRemarkingDPLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4, 1, 3),
    _Gs2328fQosTagRemarkingDPLevel_Type()
)
gs2328fQosTagRemarkingDPLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosTagRemarkingDPLevel.setStatus("current")


class _Gs2328fQosTagRemarkingPCP_Type(Integer32):
    """Custom type gs2328fQosTagRemarkingPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fQosTagRemarkingPCP_Type.__name__ = "Integer32"
_Gs2328fQosTagRemarkingPCP_Object = MibTableColumn
gs2328fQosTagRemarkingPCP = _Gs2328fQosTagRemarkingPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4, 1, 4),
    _Gs2328fQosTagRemarkingPCP_Type()
)
gs2328fQosTagRemarkingPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosTagRemarkingPCP.setStatus("current")


class _Gs2328fQosTagRemarkingDEI_Type(Integer32):
    """Custom type gs2328fQosTagRemarkingDEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328fQosTagRemarkingDEI_Type.__name__ = "Integer32"
_Gs2328fQosTagRemarkingDEI_Object = MibTableColumn
gs2328fQosTagRemarkingDEI = _Gs2328fQosTagRemarkingDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 4, 4, 1, 5),
    _Gs2328fQosTagRemarkingDEI_Type()
)
gs2328fQosTagRemarkingDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosTagRemarkingDEI.setStatus("current")
_Gs2328fQosPortDSCPTable_Object = MibTable
gs2328fQosPortDSCPTable = _Gs2328fQosPortDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 5)
)
if mibBuilder.loadTexts:
    gs2328fQosPortDSCPTable.setStatus("current")
_Gs2328fQosPortDSCPEntry_Object = MibTableRow
gs2328fQosPortDSCPEntry = _Gs2328fQosPortDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 5, 1)
)
gs2328fQosPortDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosPortDSCPPort"),
)
if mibBuilder.loadTexts:
    gs2328fQosPortDSCPEntry.setStatus("current")


class _Gs2328fQosPortDSCPPort_Type(Integer32):
    """Custom type gs2328fQosPortDSCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosPortDSCPPort_Type.__name__ = "Integer32"
_Gs2328fQosPortDSCPPort_Object = MibTableColumn
gs2328fQosPortDSCPPort = _Gs2328fQosPortDSCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 5, 1, 1),
    _Gs2328fQosPortDSCPPort_Type()
)
gs2328fQosPortDSCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosPortDSCPPort.setStatus("current")


class _Gs2328fQosPortDSCPIngressTranslate_Type(Integer32):
    """Custom type gs2328fQosPortDSCPIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosPortDSCPIngressTranslate_Type.__name__ = "Integer32"
_Gs2328fQosPortDSCPIngressTranslate_Object = MibTableColumn
gs2328fQosPortDSCPIngressTranslate = _Gs2328fQosPortDSCPIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 5, 1, 2),
    _Gs2328fQosPortDSCPIngressTranslate_Type()
)
gs2328fQosPortDSCPIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortDSCPIngressTranslate.setStatus("current")


class _Gs2328fQosPortDSCPIngressClassify_Type(Integer32):
    """Custom type gs2328fQosPortDSCPIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fQosPortDSCPIngressClassify_Type.__name__ = "Integer32"
_Gs2328fQosPortDSCPIngressClassify_Object = MibTableColumn
gs2328fQosPortDSCPIngressClassify = _Gs2328fQosPortDSCPIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 5, 1, 3),
    _Gs2328fQosPortDSCPIngressClassify_Type()
)
gs2328fQosPortDSCPIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortDSCPIngressClassify.setStatus("current")


class _Gs2328fQosPortDSCPEgressRewrite_Type(Integer32):
    """Custom type gs2328fQosPortDSCPEgressRewrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2328fQosPortDSCPEgressRewrite_Type.__name__ = "Integer32"
_Gs2328fQosPortDSCPEgressRewrite_Object = MibTableColumn
gs2328fQosPortDSCPEgressRewrite = _Gs2328fQosPortDSCPEgressRewrite_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 5, 1, 4),
    _Gs2328fQosPortDSCPEgressRewrite_Type()
)
gs2328fQosPortDSCPEgressRewrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPortDSCPEgressRewrite.setStatus("current")
_Gs2328fQosDSCPTable_Object = MibTable
gs2328fQosDSCPTable = _Gs2328fQosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6)
)
if mibBuilder.loadTexts:
    gs2328fQosDSCPTable.setStatus("current")
_Gs2328fQosDSCPEntry_Object = MibTableRow
gs2328fQosDSCPEntry = _Gs2328fQosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6, 1)
)
gs2328fQosDSCPEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosDSCPList"),
)
if mibBuilder.loadTexts:
    gs2328fQosDSCPEntry.setStatus("current")


class _Gs2328fQosDSCPList_Type(Integer32):
    """Custom type gs2328fQosDSCPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2328fQosDSCPList_Type.__name__ = "Integer32"
_Gs2328fQosDSCPList_Object = MibTableColumn
gs2328fQosDSCPList = _Gs2328fQosDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6, 1, 1),
    _Gs2328fQosDSCPList_Type()
)
gs2328fQosDSCPList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosDSCPList.setStatus("current")
_Gs2328fQosDSCP_Type = DisplayString
_Gs2328fQosDSCP_Object = MibTableColumn
gs2328fQosDSCP = _Gs2328fQosDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6, 1, 2),
    _Gs2328fQosDSCP_Type()
)
gs2328fQosDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosDSCP.setStatus("current")


class _Gs2328fQosDSCPTrust_Type(Integer32):
    """Custom type gs2328fQosDSCPTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosDSCPTrust_Type.__name__ = "Integer32"
_Gs2328fQosDSCPTrust_Object = MibTableColumn
gs2328fQosDSCPTrust = _Gs2328fQosDSCPTrust_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6, 1, 3),
    _Gs2328fQosDSCPTrust_Type()
)
gs2328fQosDSCPTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTrust.setStatus("current")


class _Gs2328fQosDSCPQosClass_Type(Integer32):
    """Custom type gs2328fQosDSCPQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2328fQosDSCPQosClass_Type.__name__ = "Integer32"
_Gs2328fQosDSCPQosClass_Object = MibTableColumn
gs2328fQosDSCPQosClass = _Gs2328fQosDSCPQosClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6, 1, 4),
    _Gs2328fQosDSCPQosClass_Type()
)
gs2328fQosDSCPQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPQosClass.setStatus("current")


class _Gs2328fQosDSCPDPL_Type(Integer32):
    """Custom type gs2328fQosDSCPDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328fQosDSCPDPL_Type.__name__ = "Integer32"
_Gs2328fQosDSCPDPL_Object = MibTableColumn
gs2328fQosDSCPDPL = _Gs2328fQosDSCPDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 6, 1, 5),
    _Gs2328fQosDSCPDPL_Type()
)
gs2328fQosDSCPDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPDPL.setStatus("current")
_Gs2328fQosDSCPTranslationTable_Object = MibTable
gs2328fQosDSCPTranslationTable = _Gs2328fQosDSCPTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7)
)
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationTable.setStatus("current")
_Gs2328fQosDSCPTranslationEntry_Object = MibTableRow
gs2328fQosDSCPTranslationEntry = _Gs2328fQosDSCPTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1)
)
gs2328fQosDSCPTranslationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosDSCPTranslationList"),
)
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationEntry.setStatus("current")


class _Gs2328fQosDSCPTranslationList_Type(Integer32):
    """Custom type gs2328fQosDSCPTranslationList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2328fQosDSCPTranslationList_Type.__name__ = "Integer32"
_Gs2328fQosDSCPTranslationList_Object = MibTableColumn
gs2328fQosDSCPTranslationList = _Gs2328fQosDSCPTranslationList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1, 1),
    _Gs2328fQosDSCPTranslationList_Type()
)
gs2328fQosDSCPTranslationList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationList.setStatus("current")
_Gs2328fQosDSCPTranslationDSCPBasedId_Type = DisplayString
_Gs2328fQosDSCPTranslationDSCPBasedId_Object = MibTableColumn
gs2328fQosDSCPTranslationDSCPBasedId = _Gs2328fQosDSCPTranslationDSCPBasedId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1, 2),
    _Gs2328fQosDSCPTranslationDSCPBasedId_Type()
)
gs2328fQosDSCPTranslationDSCPBasedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationDSCPBasedId.setStatus("current")


class _Gs2328fQosDSCPTranslationIngressTranslate_Type(Integer32):
    """Custom type gs2328fQosDSCPTranslationIngressTranslate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328fQosDSCPTranslationIngressTranslate_Type.__name__ = "Integer32"
_Gs2328fQosDSCPTranslationIngressTranslate_Object = MibTableColumn
gs2328fQosDSCPTranslationIngressTranslate = _Gs2328fQosDSCPTranslationIngressTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1, 3),
    _Gs2328fQosDSCPTranslationIngressTranslate_Type()
)
gs2328fQosDSCPTranslationIngressTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationIngressTranslate.setStatus("current")


class _Gs2328fQosDSCPTranslationIngressClassify_Type(Integer32):
    """Custom type gs2328fQosDSCPTranslationIngressClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQosDSCPTranslationIngressClassify_Type.__name__ = "Integer32"
_Gs2328fQosDSCPTranslationIngressClassify_Object = MibTableColumn
gs2328fQosDSCPTranslationIngressClassify = _Gs2328fQosDSCPTranslationIngressClassify_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1, 4),
    _Gs2328fQosDSCPTranslationIngressClassify_Type()
)
gs2328fQosDSCPTranslationIngressClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationIngressClassify.setStatus("current")


class _Gs2328fQosDSCPTranslationEgressRemapDP0_Type(Integer32):
    """Custom type gs2328fQosDSCPTranslationEgressRemapDP0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328fQosDSCPTranslationEgressRemapDP0_Type.__name__ = "Integer32"
_Gs2328fQosDSCPTranslationEgressRemapDP0_Object = MibTableColumn
gs2328fQosDSCPTranslationEgressRemapDP0 = _Gs2328fQosDSCPTranslationEgressRemapDP0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1, 5),
    _Gs2328fQosDSCPTranslationEgressRemapDP0_Type()
)
gs2328fQosDSCPTranslationEgressRemapDP0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationEgressRemapDP0.setStatus("current")


class _Gs2328fQosDSCPTranslationEgressRemapDP1_Type(Integer32):
    """Custom type gs2328fQosDSCPTranslationEgressRemapDP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328fQosDSCPTranslationEgressRemapDP1_Type.__name__ = "Integer32"
_Gs2328fQosDSCPTranslationEgressRemapDP1_Object = MibTableColumn
gs2328fQosDSCPTranslationEgressRemapDP1 = _Gs2328fQosDSCPTranslationEgressRemapDP1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 7, 1, 6),
    _Gs2328fQosDSCPTranslationEgressRemapDP1_Type()
)
gs2328fQosDSCPTranslationEgressRemapDP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPTranslationEgressRemapDP1.setStatus("current")
_Gs2328fQosDSCPClassificationTable_Object = MibTable
gs2328fQosDSCPClassificationTable = _Gs2328fQosDSCPClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 8)
)
if mibBuilder.loadTexts:
    gs2328fQosDSCPClassificationTable.setStatus("current")
_Gs2328fQosDSCPClassificationEntry_Object = MibTableRow
gs2328fQosDSCPClassificationEntry = _Gs2328fQosDSCPClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 8, 1)
)
gs2328fQosDSCPClassificationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosDSCPClassificationQoSClass"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosDSCPClassificationDPL"),
)
if mibBuilder.loadTexts:
    gs2328fQosDSCPClassificationEntry.setStatus("current")


class _Gs2328fQosDSCPClassificationQoSClass_Type(Integer32):
    """Custom type gs2328fQosDSCPClassificationQoSClass based on Integer32"""
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


_Gs2328fQosDSCPClassificationQoSClass_Type.__name__ = "Integer32"
_Gs2328fQosDSCPClassificationQoSClass_Object = MibTableColumn
gs2328fQosDSCPClassificationQoSClass = _Gs2328fQosDSCPClassificationQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 8, 1, 1),
    _Gs2328fQosDSCPClassificationQoSClass_Type()
)
gs2328fQosDSCPClassificationQoSClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosDSCPClassificationQoSClass.setStatus("current")


class _Gs2328fQosDSCPClassificationDPL_Type(Integer32):
    """Custom type gs2328fQosDSCPClassificationDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2328fQosDSCPClassificationDPL_Type.__name__ = "Integer32"
_Gs2328fQosDSCPClassificationDPL_Object = MibTableColumn
gs2328fQosDSCPClassificationDPL = _Gs2328fQosDSCPClassificationDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 8, 1, 2),
    _Gs2328fQosDSCPClassificationDPL_Type()
)
gs2328fQosDSCPClassificationDPL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosDSCPClassificationDPL.setStatus("current")


class _Gs2328fQosDSCPClassificationDSCP_Type(Integer32):
    """Custom type gs2328fQosDSCPClassificationDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Gs2328fQosDSCPClassificationDSCP_Type.__name__ = "Integer32"
_Gs2328fQosDSCPClassificationDSCP_Object = MibTableColumn
gs2328fQosDSCPClassificationDSCP = _Gs2328fQosDSCPClassificationDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 8, 1, 3),
    _Gs2328fQosDSCPClassificationDSCP_Type()
)
gs2328fQosDSCPClassificationDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDSCPClassificationDSCP.setStatus("current")
_Gs2328fQosControlList_ObjectIdentity = ObjectIdentity
gs2328fQosControlList = _Gs2328fQosControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9)
)


class _Gs2328fQosQceCreate_Type(Integer32):
    """Custom type gs2328fQosQceCreate based on Integer32"""
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


_Gs2328fQosQceCreate_Type.__name__ = "Integer32"
_Gs2328fQosQceCreate_Object = MibScalar
gs2328fQosQceCreate = _Gs2328fQosQceCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 1),
    _Gs2328fQosQceCreate_Type()
)
gs2328fQosQceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceCreate.setStatus("current")
_Gs2328fQosQceTable_Object = MibTable
gs2328fQosQceTable = _Gs2328fQosQceTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2)
)
if mibBuilder.loadTexts:
    gs2328fQosQceTable.setStatus("current")
_Gs2328fQosQceEntry_Object = MibTableRow
gs2328fQosQceEntry = _Gs2328fQosQceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1)
)
gs2328fQosQceEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosQceIndex"),
)
if mibBuilder.loadTexts:
    gs2328fQosQceEntry.setStatus("current")


class _Gs2328fQosQceIndex_Type(Integer32):
    """Custom type gs2328fQosQceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fQosQceIndex_Type.__name__ = "Integer32"
_Gs2328fQosQceIndex_Object = MibTableColumn
gs2328fQosQceIndex = _Gs2328fQosQceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 1),
    _Gs2328fQosQceIndex_Type()
)
gs2328fQosQceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosQceIndex.setStatus("current")


class _Gs2328fQosQceID_Type(Integer32):
    """Custom type gs2328fQosQceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fQosQceID_Type.__name__ = "Integer32"
_Gs2328fQosQceID_Object = MibTableColumn
gs2328fQosQceID = _Gs2328fQosQceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 2),
    _Gs2328fQosQceID_Type()
)
gs2328fQosQceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceID.setStatus("current")


class _Gs2328fQosQceNextID_Type(Integer32):
    """Custom type gs2328fQosQceNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fQosQceNextID_Type.__name__ = "Integer32"
_Gs2328fQosQceNextID_Object = MibTableColumn
gs2328fQosQceNextID = _Gs2328fQosQceNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 3),
    _Gs2328fQosQceNextID_Type()
)
gs2328fQosQceNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceNextID.setStatus("current")
_Gs2328fQosQcePortMembers_Type = DisplayString
_Gs2328fQosQcePortMembers_Object = MibTableColumn
gs2328fQosQcePortMembers = _Gs2328fQosQcePortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 4),
    _Gs2328fQosQcePortMembers_Type()
)
gs2328fQosQcePortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQcePortMembers.setStatus("current")
_Gs2328fQosQceTag_Type = DisplayString
_Gs2328fQosQceTag_Object = MibTableColumn
gs2328fQosQceTag = _Gs2328fQosQceTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 5),
    _Gs2328fQosQceTag_Type()
)
gs2328fQosQceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceTag.setStatus("current")
_Gs2328fQosQceVID_Type = DisplayString
_Gs2328fQosQceVID_Object = MibTableColumn
gs2328fQosQceVID = _Gs2328fQosQceVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 6),
    _Gs2328fQosQceVID_Type()
)
gs2328fQosQceVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceVID.setStatus("current")
_Gs2328fQosPCP_Type = DisplayString
_Gs2328fQosPCP_Object = MibTableColumn
gs2328fQosPCP = _Gs2328fQosPCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 7),
    _Gs2328fQosPCP_Type()
)
gs2328fQosPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosPCP.setStatus("current")
_Gs2328fQosDEI_Type = DisplayString
_Gs2328fQosDEI_Object = MibTableColumn
gs2328fQosDEI = _Gs2328fQosDEI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 8),
    _Gs2328fQosDEI_Type()
)
gs2328fQosDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDEI.setStatus("current")
_Gs2328fQosSMAC_Type = DisplayString
_Gs2328fQosSMAC_Object = MibTableColumn
gs2328fQosSMAC = _Gs2328fQosSMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 9),
    _Gs2328fQosSMAC_Type()
)
gs2328fQosSMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSMAC.setStatus("current")
_Gs2328fQosDMACType_Type = DisplayString
_Gs2328fQosDMACType_Object = MibTableColumn
gs2328fQosDMACType = _Gs2328fQosDMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 10),
    _Gs2328fQosDMACType_Type()
)
gs2328fQosDMACType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosDMACType.setStatus("current")


class _Gs2328fQosFrameType_Type(Integer32):
    """Custom type gs2328fQosFrameType based on Integer32"""
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


_Gs2328fQosFrameType_Type.__name__ = "Integer32"
_Gs2328fQosFrameType_Object = MibTableColumn
gs2328fQosFrameType = _Gs2328fQosFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 11),
    _Gs2328fQosFrameType_Type()
)
gs2328fQosFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosFrameType.setStatus("current")
_Gs2328fQosMacEtherType_Type = DisplayString
_Gs2328fQosMacEtherType_Object = MibTableColumn
gs2328fQosMacEtherType = _Gs2328fQosMacEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 12),
    _Gs2328fQosMacEtherType_Type()
)
gs2328fQosMacEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosMacEtherType.setStatus("current")
_Gs2328fQosLLCSSAPAddr_Type = DisplayString
_Gs2328fQosLLCSSAPAddr_Object = MibTableColumn
gs2328fQosLLCSSAPAddr = _Gs2328fQosLLCSSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 13),
    _Gs2328fQosLLCSSAPAddr_Type()
)
gs2328fQosLLCSSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosLLCSSAPAddr.setStatus("current")
_Gs2328fQosLLCDSAPAddr_Type = DisplayString
_Gs2328fQosLLCDSAPAddr_Object = MibTableColumn
gs2328fQosLLCDSAPAddr = _Gs2328fQosLLCDSAPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 14),
    _Gs2328fQosLLCDSAPAddr_Type()
)
gs2328fQosLLCDSAPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosLLCDSAPAddr.setStatus("current")
_Gs2328fQosLLCControl_Type = DisplayString
_Gs2328fQosLLCControl_Object = MibTableColumn
gs2328fQosLLCControl = _Gs2328fQosLLCControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 15),
    _Gs2328fQosLLCControl_Type()
)
gs2328fQosLLCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosLLCControl.setStatus("current")
_Gs2328fQosSNAPPID_Type = DisplayString
_Gs2328fQosSNAPPID_Object = MibTableColumn
gs2328fQosSNAPPID = _Gs2328fQosSNAPPID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 16),
    _Gs2328fQosSNAPPID_Type()
)
gs2328fQosSNAPPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosSNAPPID.setStatus("current")
_Gs2328fQosIpv4Protocol_Type = DisplayString
_Gs2328fQosIpv4Protocol_Object = MibTableColumn
gs2328fQosIpv4Protocol = _Gs2328fQosIpv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 17),
    _Gs2328fQosIpv4Protocol_Type()
)
gs2328fQosIpv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4Protocol.setStatus("current")


class _Gs2328fQosIpv4ProtocolValue_Type(Integer32):
    """Custom type gs2328fQosIpv4ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328fQosIpv4ProtocolValue_Type.__name__ = "Integer32"
_Gs2328fQosIpv4ProtocolValue_Object = MibTableColumn
gs2328fQosIpv4ProtocolValue = _Gs2328fQosIpv4ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 18),
    _Gs2328fQosIpv4ProtocolValue_Type()
)
gs2328fQosIpv4ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4ProtocolValue.setStatus("current")
_Gs2328fQosIpv4ProtocolUDPSport_Type = DisplayString
_Gs2328fQosIpv4ProtocolUDPSport_Object = MibTableColumn
gs2328fQosIpv4ProtocolUDPSport = _Gs2328fQosIpv4ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 19),
    _Gs2328fQosIpv4ProtocolUDPSport_Type()
)
gs2328fQosIpv4ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4ProtocolUDPSport.setStatus("current")
_Gs2328fQosIpv4ProtocolUDPDport_Type = DisplayString
_Gs2328fQosIpv4ProtocolUDPDport_Object = MibTableColumn
gs2328fQosIpv4ProtocolUDPDport = _Gs2328fQosIpv4ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 20),
    _Gs2328fQosIpv4ProtocolUDPDport_Type()
)
gs2328fQosIpv4ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4ProtocolUDPDport.setStatus("current")
_Gs2328fQosIpv4ProtocolTCPSport_Type = DisplayString
_Gs2328fQosIpv4ProtocolTCPSport_Object = MibTableColumn
gs2328fQosIpv4ProtocolTCPSport = _Gs2328fQosIpv4ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 21),
    _Gs2328fQosIpv4ProtocolTCPSport_Type()
)
gs2328fQosIpv4ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4ProtocolTCPSport.setStatus("current")
_Gs2328fQosIpv4ProtocolTCPDport_Type = DisplayString
_Gs2328fQosIpv4ProtocolTCPDport_Object = MibTableColumn
gs2328fQosIpv4ProtocolTCPDport = _Gs2328fQosIpv4ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 22),
    _Gs2328fQosIpv4ProtocolTCPDport_Type()
)
gs2328fQosIpv4ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4ProtocolTCPDport.setStatus("current")
_Gs2328fQosIpv4Ip_Type = DisplayString
_Gs2328fQosIpv4Ip_Object = MibTableColumn
gs2328fQosIpv4Ip = _Gs2328fQosIpv4Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 23),
    _Gs2328fQosIpv4Ip_Type()
)
gs2328fQosIpv4Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4Ip.setStatus("current")
_Gs2328fQosIpv4Mask_Type = DisplayString
_Gs2328fQosIpv4Mask_Object = MibTableColumn
gs2328fQosIpv4Mask = _Gs2328fQosIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 24),
    _Gs2328fQosIpv4Mask_Type()
)
gs2328fQosIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4Mask.setStatus("current")


class _Gs2328fQosIpv4IPFragment_Type(Integer32):
    """Custom type gs2328fQosIpv4IPFragment based on Integer32"""
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


_Gs2328fQosIpv4IPFragment_Type.__name__ = "Integer32"
_Gs2328fQosIpv4IPFragment_Object = MibTableColumn
gs2328fQosIpv4IPFragment = _Gs2328fQosIpv4IPFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 25),
    _Gs2328fQosIpv4IPFragment_Type()
)
gs2328fQosIpv4IPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4IPFragment.setStatus("current")
_Gs2328fQosIpv4DSCP_Type = DisplayString
_Gs2328fQosIpv4DSCP_Object = MibTableColumn
gs2328fQosIpv4DSCP = _Gs2328fQosIpv4DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 26),
    _Gs2328fQosIpv4DSCP_Type()
)
gs2328fQosIpv4DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv4DSCP.setStatus("current")
_Gs2328fQosIpv6Protocol_Type = DisplayString
_Gs2328fQosIpv6Protocol_Object = MibTableColumn
gs2328fQosIpv6Protocol = _Gs2328fQosIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 27),
    _Gs2328fQosIpv6Protocol_Type()
)
gs2328fQosIpv6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6Protocol.setStatus("current")


class _Gs2328fQosIpv6ProtocolValue_Type(Integer32):
    """Custom type gs2328fQosIpv6ProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2328fQosIpv6ProtocolValue_Type.__name__ = "Integer32"
_Gs2328fQosIpv6ProtocolValue_Object = MibTableColumn
gs2328fQosIpv6ProtocolValue = _Gs2328fQosIpv6ProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 28),
    _Gs2328fQosIpv6ProtocolValue_Type()
)
gs2328fQosIpv6ProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6ProtocolValue.setStatus("current")
_Gs2328fQosIpv6ProtocolUDPSport_Type = DisplayString
_Gs2328fQosIpv6ProtocolUDPSport_Object = MibTableColumn
gs2328fQosIpv6ProtocolUDPSport = _Gs2328fQosIpv6ProtocolUDPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 29),
    _Gs2328fQosIpv6ProtocolUDPSport_Type()
)
gs2328fQosIpv6ProtocolUDPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6ProtocolUDPSport.setStatus("current")
_Gs2328fQosIpv6ProtocolUDPDport_Type = DisplayString
_Gs2328fQosIpv6ProtocolUDPDport_Object = MibTableColumn
gs2328fQosIpv6ProtocolUDPDport = _Gs2328fQosIpv6ProtocolUDPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 30),
    _Gs2328fQosIpv6ProtocolUDPDport_Type()
)
gs2328fQosIpv6ProtocolUDPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6ProtocolUDPDport.setStatus("current")
_Gs2328fQosIpv6ProtocolTCPSport_Type = DisplayString
_Gs2328fQosIpv6ProtocolTCPSport_Object = MibTableColumn
gs2328fQosIpv6ProtocolTCPSport = _Gs2328fQosIpv6ProtocolTCPSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 31),
    _Gs2328fQosIpv6ProtocolTCPSport_Type()
)
gs2328fQosIpv6ProtocolTCPSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6ProtocolTCPSport.setStatus("current")
_Gs2328fQosIpv6ProtocolTCPDport_Type = DisplayString
_Gs2328fQosIpv6ProtocolTCPDport_Object = MibTableColumn
gs2328fQosIpv6ProtocolTCPDport = _Gs2328fQosIpv6ProtocolTCPDport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 32),
    _Gs2328fQosIpv6ProtocolTCPDport_Type()
)
gs2328fQosIpv6ProtocolTCPDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6ProtocolTCPDport.setStatus("current")
_Gs2328fQosIpv6Ip_Type = DisplayString
_Gs2328fQosIpv6Ip_Object = MibTableColumn
gs2328fQosIpv6Ip = _Gs2328fQosIpv6Ip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 33),
    _Gs2328fQosIpv6Ip_Type()
)
gs2328fQosIpv6Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6Ip.setStatus("current")
_Gs2328fQosIpv6Mask_Type = DisplayString
_Gs2328fQosIpv6Mask_Object = MibTableColumn
gs2328fQosIpv6Mask = _Gs2328fQosIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 34),
    _Gs2328fQosIpv6Mask_Type()
)
gs2328fQosIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6Mask.setStatus("current")
_Gs2328fQosIpv6DSCP_Type = DisplayString
_Gs2328fQosIpv6DSCP_Object = MibTableColumn
gs2328fQosIpv6DSCP = _Gs2328fQosIpv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 35),
    _Gs2328fQosIpv6DSCP_Type()
)
gs2328fQosIpv6DSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosIpv6DSCP.setStatus("current")


class _Gs2328fQosActionClass_Type(Integer32):
    """Custom type gs2328fQosActionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Gs2328fQosActionClass_Type.__name__ = "Integer32"
_Gs2328fQosActionClass_Object = MibTableColumn
gs2328fQosActionClass = _Gs2328fQosActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 36),
    _Gs2328fQosActionClass_Type()
)
gs2328fQosActionClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosActionClass.setStatus("current")


class _Gs2328fQosActionDPL_Type(Integer32):
    """Custom type gs2328fQosActionDPL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2328fQosActionDPL_Type.__name__ = "Integer32"
_Gs2328fQosActionDPL_Object = MibTableColumn
gs2328fQosActionDPL = _Gs2328fQosActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 37),
    _Gs2328fQosActionDPL_Type()
)
gs2328fQosActionDPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosActionDPL.setStatus("current")


class _Gs2328fQosActionDSCP_Type(Integer32):
    """Custom type gs2328fQosActionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2328fQosActionDSCP_Type.__name__ = "Integer32"
_Gs2328fQosActionDSCP_Object = MibTableColumn
gs2328fQosActionDSCP = _Gs2328fQosActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 38),
    _Gs2328fQosActionDSCP_Type()
)
gs2328fQosActionDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosActionDSCP.setStatus("current")


class _Gs2328fQosQceRowStatus_Type(Integer32):
    """Custom type gs2328fQosQceRowStatus based on Integer32"""
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


_Gs2328fQosQceRowStatus_Type.__name__ = "Integer32"
_Gs2328fQosQceRowStatus_Object = MibTableColumn
gs2328fQosQceRowStatus = _Gs2328fQosQceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 2, 1, 39),
    _Gs2328fQosQceRowStatus_Type()
)
gs2328fQosQceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceRowStatus.setStatus("current")


class _Gs2328fQosQceMoveID_Type(Integer32):
    """Custom type gs2328fQosQceMoveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328fQosQceMoveID_Type.__name__ = "Integer32"
_Gs2328fQosQceMoveID_Object = MibScalar
gs2328fQosQceMoveID = _Gs2328fQosQceMoveID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 3),
    _Gs2328fQosQceMoveID_Type()
)
gs2328fQosQceMoveID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceMoveID.setStatus("current")


class _Gs2328fQosQceMoveNextID_Type(Integer32):
    """Custom type gs2328fQosQceMoveNextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Gs2328fQosQceMoveNextID_Type.__name__ = "Integer32"
_Gs2328fQosQceMoveNextID_Object = MibScalar
gs2328fQosQceMoveNextID = _Gs2328fQosQceMoveNextID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 9, 4),
    _Gs2328fQosQceMoveNextID_Type()
)
gs2328fQosQceMoveNextID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQosQceMoveNextID.setStatus("current")
_Gs2328fQosQCLStatusTable_Object = MibTable
gs2328fQosQCLStatusTable = _Gs2328fQosQCLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10)
)
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusTable.setStatus("current")
_Gs2328fQosQCLStatusEntry_Object = MibTableRow
gs2328fQosQCLStatusEntry = _Gs2328fQosQCLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1)
)
gs2328fQosQCLStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fQosQCLStatusList"),
)
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusEntry.setStatus("current")


class _Gs2328fQosQCLStatusList_Type(Integer32):
    """Custom type gs2328fQosQCLStatusList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fQosQCLStatusList_Type.__name__ = "Integer32"
_Gs2328fQosQCLStatusList_Object = MibTableColumn
gs2328fQosQCLStatusList = _Gs2328fQosQCLStatusList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 1),
    _Gs2328fQosQCLStatusList_Type()
)
gs2328fQosQCLStatusList.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusList.setStatus("current")
_Gs2328fQosQCLStatusUser_Type = DisplayString
_Gs2328fQosQCLStatusUser_Object = MibTableColumn
gs2328fQosQCLStatusUser = _Gs2328fQosQCLStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 2),
    _Gs2328fQosQCLStatusUser_Type()
)
gs2328fQosQCLStatusUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusUser.setStatus("current")
_Gs2328fQosQCLStatusQCEId_Type = DisplayString
_Gs2328fQosQCLStatusQCEId_Object = MibTableColumn
gs2328fQosQCLStatusQCEId = _Gs2328fQosQCLStatusQCEId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 3),
    _Gs2328fQosQCLStatusQCEId_Type()
)
gs2328fQosQCLStatusQCEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusQCEId.setStatus("current")
_Gs2328fQosQCLStatusFrameType_Type = DisplayString
_Gs2328fQosQCLStatusFrameType_Object = MibTableColumn
gs2328fQosQCLStatusFrameType = _Gs2328fQosQCLStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 4),
    _Gs2328fQosQCLStatusFrameType_Type()
)
gs2328fQosQCLStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusFrameType.setStatus("current")
_Gs2328fQosQCLStatusPortlist_Type = DisplayString
_Gs2328fQosQCLStatusPortlist_Object = MibTableColumn
gs2328fQosQCLStatusPortlist = _Gs2328fQosQCLStatusPortlist_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 5),
    _Gs2328fQosQCLStatusPortlist_Type()
)
gs2328fQosQCLStatusPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusPortlist.setStatus("current")
_Gs2328fQosQCLStatusActionClass_Type = DisplayString
_Gs2328fQosQCLStatusActionClass_Object = MibTableColumn
gs2328fQosQCLStatusActionClass = _Gs2328fQosQCLStatusActionClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 6),
    _Gs2328fQosQCLStatusActionClass_Type()
)
gs2328fQosQCLStatusActionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusActionClass.setStatus("current")
_Gs2328fQosQCLStatusActionDPL_Type = DisplayString
_Gs2328fQosQCLStatusActionDPL_Object = MibTableColumn
gs2328fQosQCLStatusActionDPL = _Gs2328fQosQCLStatusActionDPL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 7),
    _Gs2328fQosQCLStatusActionDPL_Type()
)
gs2328fQosQCLStatusActionDPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusActionDPL.setStatus("current")
_Gs2328fQosQCLStatusActionDSCP_Type = DisplayString
_Gs2328fQosQCLStatusActionDSCP_Object = MibTableColumn
gs2328fQosQCLStatusActionDSCP = _Gs2328fQosQCLStatusActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 8),
    _Gs2328fQosQCLStatusActionDSCP_Type()
)
gs2328fQosQCLStatusActionDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusActionDSCP.setStatus("current")
_Gs2328fQosQCLStatusActionConflict_Type = DisplayString
_Gs2328fQosQCLStatusActionConflict_Object = MibTableColumn
gs2328fQosQCLStatusActionConflict = _Gs2328fQosQCLStatusActionConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 10, 1, 9),
    _Gs2328fQosQCLStatusActionConflict_Type()
)
gs2328fQosQCLStatusActionConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fQosQCLStatusActionConflict.setStatus("current")
_Gs2328fQosStormControl_ObjectIdentity = ObjectIdentity
gs2328fQosStormControl = _Gs2328fQosStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11)
)


class _Gs2328fQoSStormControlUC_Type(Integer32):
    """Custom type gs2328fQoSStormControlUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQoSStormControlUC_Type.__name__ = "Integer32"
_Gs2328fQoSStormControlUC_Object = MibScalar
gs2328fQoSStormControlUC = _Gs2328fQoSStormControlUC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11, 2),
    _Gs2328fQoSStormControlUC_Type()
)
gs2328fQoSStormControlUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSStormControlUC.setStatus("current")
_Gs2328fQoSStormControlUCRate_Type = DisplayString
_Gs2328fQoSStormControlUCRate_Object = MibScalar
gs2328fQoSStormControlUCRate = _Gs2328fQoSStormControlUCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11, 3),
    _Gs2328fQoSStormControlUCRate_Type()
)
gs2328fQoSStormControlUCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSStormControlUCRate.setStatus("current")


class _Gs2328fQoSStormControlMC_Type(Integer32):
    """Custom type gs2328fQoSStormControlMC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQoSStormControlMC_Type.__name__ = "Integer32"
_Gs2328fQoSStormControlMC_Object = MibScalar
gs2328fQoSStormControlMC = _Gs2328fQoSStormControlMC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11, 4),
    _Gs2328fQoSStormControlMC_Type()
)
gs2328fQoSStormControlMC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSStormControlMC.setStatus("current")
_Gs2328fQoSStormControlMCRate_Type = DisplayString
_Gs2328fQoSStormControlMCRate_Object = MibScalar
gs2328fQoSStormControlMCRate = _Gs2328fQoSStormControlMCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11, 5),
    _Gs2328fQoSStormControlMCRate_Type()
)
gs2328fQoSStormControlMCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSStormControlMCRate.setStatus("current")


class _Gs2328fQoSStormControlBC_Type(Integer32):
    """Custom type gs2328fQoSStormControlBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fQoSStormControlBC_Type.__name__ = "Integer32"
_Gs2328fQoSStormControlBC_Object = MibScalar
gs2328fQoSStormControlBC = _Gs2328fQoSStormControlBC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11, 6),
    _Gs2328fQoSStormControlBC_Type()
)
gs2328fQoSStormControlBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSStormControlBC.setStatus("current")
_Gs2328fQoSStormControlBCRate_Type = DisplayString
_Gs2328fQoSStormControlBCRate_Object = MibScalar
gs2328fQoSStormControlBCRate = _Gs2328fQoSStormControlBCRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 14, 11, 7),
    _Gs2328fQoSStormControlBCRate_Type()
)
gs2328fQoSStormControlBCRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fQoSStormControlBCRate.setStatus("current")
_Gs2328fVlan_ObjectIdentity = ObjectIdentity
gs2328fVlan = _Gs2328fVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15)
)
_Gs2328fVlanPorts_ObjectIdentity = ObjectIdentity
gs2328fVlanPorts = _Gs2328fVlanPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1)
)


class _Gs2328fVlanPortsTPIDforCustomSport_Type(OctetString):
    """Custom type gs2328fVlanPortsTPIDforCustomSport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Gs2328fVlanPortsTPIDforCustomSport_Type.__name__ = "OctetString"
_Gs2328fVlanPortsTPIDforCustomSport_Object = MibScalar
gs2328fVlanPortsTPIDforCustomSport = _Gs2328fVlanPortsTPIDforCustomSport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 1),
    _Gs2328fVlanPortsTPIDforCustomSport_Type()
)
gs2328fVlanPortsTPIDforCustomSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortsTPIDforCustomSport.setStatus("current")
_Gs2328fVlanPortsTable_Object = MibTable
gs2328fVlanPortsTable = _Gs2328fVlanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fVlanPortsTable.setStatus("current")
_Gs2328fVlanPortsEntry_Object = MibTableRow
gs2328fVlanPortsEntry = _Gs2328fVlanPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1)
)
gs2328fVlanPortsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fVlanPortsPort"),
)
if mibBuilder.loadTexts:
    gs2328fVlanPortsEntry.setStatus("current")


class _Gs2328fVlanPortsPort_Type(Integer32):
    """Custom type gs2328fVlanPortsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fVlanPortsPort_Type.__name__ = "Integer32"
_Gs2328fVlanPortsPort_Object = MibTableColumn
gs2328fVlanPortsPort = _Gs2328fVlanPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1, 1),
    _Gs2328fVlanPortsPort_Type()
)
gs2328fVlanPortsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fVlanPortsPort.setStatus("current")


class _Gs2328fVlanPortsPVID_Type(Integer32):
    """Custom type gs2328fVlanPortsPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fVlanPortsPVID_Type.__name__ = "Integer32"
_Gs2328fVlanPortsPVID_Object = MibTableColumn
gs2328fVlanPortsPVID = _Gs2328fVlanPortsPVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1, 2),
    _Gs2328fVlanPortsPVID_Type()
)
gs2328fVlanPortsPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortsPVID.setStatus("current")


class _Gs2328fVlanPortsFrameType_Type(Integer32):
    """Custom type gs2328fVlanPortsFrameType based on Integer32"""
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


_Gs2328fVlanPortsFrameType_Type.__name__ = "Integer32"
_Gs2328fVlanPortsFrameType_Object = MibTableColumn
gs2328fVlanPortsFrameType = _Gs2328fVlanPortsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1, 3),
    _Gs2328fVlanPortsFrameType_Type()
)
gs2328fVlanPortsFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortsFrameType.setStatus("current")


class _Gs2328fVlanPortsIngressFilter_Type(Integer32):
    """Custom type gs2328fVlanPortsIngressFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fVlanPortsIngressFilter_Type.__name__ = "Integer32"
_Gs2328fVlanPortsIngressFilter_Object = MibTableColumn
gs2328fVlanPortsIngressFilter = _Gs2328fVlanPortsIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1, 4),
    _Gs2328fVlanPortsIngressFilter_Type()
)
gs2328fVlanPortsIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortsIngressFilter.setStatus("current")


class _Gs2328fVlanPortsEgressRule_Type(Integer32):
    """Custom type gs2328fVlanPortsEgressRule based on Integer32"""
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


_Gs2328fVlanPortsEgressRule_Type.__name__ = "Integer32"
_Gs2328fVlanPortsEgressRule_Object = MibTableColumn
gs2328fVlanPortsEgressRule = _Gs2328fVlanPortsEgressRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1, 5),
    _Gs2328fVlanPortsEgressRule_Type()
)
gs2328fVlanPortsEgressRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortsEgressRule.setStatus("current")


class _Gs2328fVlanPortsPortType_Type(Integer32):
    """Custom type gs2328fVlanPortsPortType based on Integer32"""
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


_Gs2328fVlanPortsPortType_Type.__name__ = "Integer32"
_Gs2328fVlanPortsPortType_Object = MibTableColumn
gs2328fVlanPortsPortType = _Gs2328fVlanPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 1, 2, 1, 6),
    _Gs2328fVlanPortsPortType_Type()
)
gs2328fVlanPortsPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortsPortType.setStatus("current")
_Gs2328fVlanPrivateVLAN_ObjectIdentity = ObjectIdentity
gs2328fVlanPrivateVLAN = _Gs2328fVlanPrivateVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2)
)
_Gs2328fVlanPrivateVLANMembership_ObjectIdentity = ObjectIdentity
gs2328fVlanPrivateVLANMembership = _Gs2328fVlanPrivateVLANMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1)
)


class _Gs2328fVlanPrivateVLANMembershipCreate_Type(Integer32):
    """Custom type gs2328fVlanPrivateVLANMembershipCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fVlanPrivateVLANMembershipCreate_Type.__name__ = "Integer32"
_Gs2328fVlanPrivateVLANMembershipCreate_Object = MibScalar
gs2328fVlanPrivateVLANMembershipCreate = _Gs2328fVlanPrivateVLANMembershipCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 1),
    _Gs2328fVlanPrivateVLANMembershipCreate_Type()
)
gs2328fVlanPrivateVLANMembershipCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANMembershipCreate.setStatus("current")
_Gs2328fVlanPrivateVLANMembershipTable_Object = MibTable
gs2328fVlanPrivateVLANMembershipTable = _Gs2328fVlanPrivateVLANMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANMembershipTable.setStatus("current")
_Gs2328fVlanPrivateVLANMembershipEntry_Object = MibTableRow
gs2328fVlanPrivateVLANMembershipEntry = _Gs2328fVlanPrivateVLANMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 2, 1)
)
gs2328fVlanPrivateVLANMembershipEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fVlanPrivateVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANMembershipEntry.setStatus("current")


class _Gs2328fVlanPrivateVLANIndex_Type(Integer32):
    """Custom type gs2328fVlanPrivateVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2328fVlanPrivateVLANIndex_Type.__name__ = "Integer32"
_Gs2328fVlanPrivateVLANIndex_Object = MibTableColumn
gs2328fVlanPrivateVLANIndex = _Gs2328fVlanPrivateVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 2, 1, 1),
    _Gs2328fVlanPrivateVLANIndex_Type()
)
gs2328fVlanPrivateVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANIndex.setStatus("current")


class _Gs2328fVlanPrivateVLANID_Type(Integer32):
    """Custom type gs2328fVlanPrivateVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_Gs2328fVlanPrivateVLANID_Type.__name__ = "Integer32"
_Gs2328fVlanPrivateVLANID_Object = MibTableColumn
gs2328fVlanPrivateVLANID = _Gs2328fVlanPrivateVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 2, 1, 2),
    _Gs2328fVlanPrivateVLANID_Type()
)
gs2328fVlanPrivateVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANID.setStatus("current")
_Gs2328fVlanPrivateVLANMemberships_Type = DisplayString
_Gs2328fVlanPrivateVLANMemberships_Object = MibTableColumn
gs2328fVlanPrivateVLANMemberships = _Gs2328fVlanPrivateVLANMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 2, 1, 3),
    _Gs2328fVlanPrivateVLANMemberships_Type()
)
gs2328fVlanPrivateVLANMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANMemberships.setStatus("current")


class _Gs2328fVlanPrivateVLANRowStatus_Type(Integer32):
    """Custom type gs2328fVlanPrivateVLANRowStatus based on Integer32"""
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


_Gs2328fVlanPrivateVLANRowStatus_Type.__name__ = "Integer32"
_Gs2328fVlanPrivateVLANRowStatus_Object = MibTableColumn
gs2328fVlanPrivateVLANRowStatus = _Gs2328fVlanPrivateVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 1, 2, 1, 4),
    _Gs2328fVlanPrivateVLANRowStatus_Type()
)
gs2328fVlanPrivateVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPrivateVLANRowStatus.setStatus("current")
_Gs2328fVlanPortIsolationTable_Object = MibTable
gs2328fVlanPortIsolationTable = _Gs2328fVlanPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fVlanPortIsolationTable.setStatus("current")
_Gs2328fVlanPortIsolationEntry_Object = MibTableRow
gs2328fVlanPortIsolationEntry = _Gs2328fVlanPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 2, 1)
)
gs2328fVlanPortIsolationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fVlanPortIsolationPort"),
)
if mibBuilder.loadTexts:
    gs2328fVlanPortIsolationEntry.setStatus("current")


class _Gs2328fVlanPortIsolationPort_Type(Integer32):
    """Custom type gs2328fVlanPortIsolationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fVlanPortIsolationPort_Type.__name__ = "Integer32"
_Gs2328fVlanPortIsolationPort_Object = MibTableColumn
gs2328fVlanPortIsolationPort = _Gs2328fVlanPortIsolationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 2, 1, 1),
    _Gs2328fVlanPortIsolationPort_Type()
)
gs2328fVlanPortIsolationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fVlanPortIsolationPort.setStatus("current")


class _Gs2328fVlanPortIsolation_Type(Integer32):
    """Custom type gs2328fVlanPortIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fVlanPortIsolation_Type.__name__ = "Integer32"
_Gs2328fVlanPortIsolation_Object = MibTableColumn
gs2328fVlanPortIsolation = _Gs2328fVlanPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 2, 2, 1, 2),
    _Gs2328fVlanPortIsolation_Type()
)
gs2328fVlanPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fVlanPortIsolation.setStatus("current")
_Gs2328fMACbasedVLAN_ObjectIdentity = ObjectIdentity
gs2328fMACbasedVLAN = _Gs2328fMACbasedVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3)
)
_Gs2328fMACbasedVLANConf_ObjectIdentity = ObjectIdentity
gs2328fMACbasedVLANConf = _Gs2328fMACbasedVLANConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1)
)
_Gs2328fMACbasedVLANConfCreate_Type = Integer32
_Gs2328fMACbasedVLANConfCreate_Object = MibScalar
gs2328fMACbasedVLANConfCreate = _Gs2328fMACbasedVLANConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 1),
    _Gs2328fMACbasedVLANConfCreate_Type()
)
gs2328fMACbasedVLANConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACbasedVLANConfCreate.setStatus("current")
_Gs2328fMACbasedVLANConfTable_Object = MibTable
gs2328fMACbasedVLANConfTable = _Gs2328fMACbasedVLANConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fMACbasedVLANConfTable.setStatus("current")
_Gs2328fMACbasedVLANConfEntry_Object = MibTableRow
gs2328fMACbasedVLANConfEntry = _Gs2328fMACbasedVLANConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2, 1)
)
gs2328fMACbasedVLANConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMACbasedVLANIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMACbasedVLANConfEntry.setStatus("current")


class _Gs2328fMACbasedVLANIndex_Type(Integer32):
    """Custom type gs2328fMACbasedVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2328fMACbasedVLANIndex_Type.__name__ = "Integer32"
_Gs2328fMACbasedVLANIndex_Object = MibTableColumn
gs2328fMACbasedVLANIndex = _Gs2328fMACbasedVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2, 1, 1),
    _Gs2328fMACbasedVLANIndex_Type()
)
gs2328fMACbasedVLANIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACbasedVLANIndex.setStatus("current")
_Gs2328fMACbasedVLANMACAddress_Type = MacAddress
_Gs2328fMACbasedVLANMACAddress_Object = MibTableColumn
gs2328fMACbasedVLANMACAddress = _Gs2328fMACbasedVLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2, 1, 2),
    _Gs2328fMACbasedVLANMACAddress_Type()
)
gs2328fMACbasedVLANMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACbasedVLANMACAddress.setStatus("current")


class _Gs2328fMACbasedVLANID_Type(Integer32):
    """Custom type gs2328fMACbasedVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fMACbasedVLANID_Type.__name__ = "Integer32"
_Gs2328fMACbasedVLANID_Object = MibTableColumn
gs2328fMACbasedVLANID = _Gs2328fMACbasedVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2, 1, 3),
    _Gs2328fMACbasedVLANID_Type()
)
gs2328fMACbasedVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACbasedVLANID.setStatus("current")
_Gs2328fMACbasedMemberships_Type = DisplayString
_Gs2328fMACbasedMemberships_Object = MibTableColumn
gs2328fMACbasedMemberships = _Gs2328fMACbasedMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2, 1, 4),
    _Gs2328fMACbasedMemberships_Type()
)
gs2328fMACbasedMemberships.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACbasedMemberships.setStatus("current")


class _Gs2328fMACbaseRowStatus_Type(Integer32):
    """Custom type gs2328fMACbaseRowStatus based on Integer32"""
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


_Gs2328fMACbaseRowStatus_Type.__name__ = "Integer32"
_Gs2328fMACbaseRowStatus_Object = MibTableColumn
gs2328fMACbaseRowStatus = _Gs2328fMACbaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 15, 3, 1, 2, 1, 5),
    _Gs2328fMACbaseRowStatus_Type()
)
gs2328fMACbaseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMACbaseRowStatus.setStatus("current")
_Gs2328fIGMPSnooping_ObjectIdentity = ObjectIdentity
gs2328fIGMPSnooping = _Gs2328fIGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16)
)
_Gs2328fIGMPSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2328fIGMPSnoopingBasic = _Gs2328fIGMPSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1)
)


class _Gs2328fIGMPSnoopingEnable_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingEnable_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingEnable_Object = MibScalar
gs2328fIGMPSnoopingEnable = _Gs2328fIGMPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 1),
    _Gs2328fIGMPSnoopingEnable_Type()
)
gs2328fIGMPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingEnable.setStatus("current")


class _Gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding_Object = MibScalar
gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding = _Gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 2),
    _Gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding_Type()
)
gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding.setStatus("current")
_Gs2328fIGMPSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2328fIGMPSnoopingSSMIPRangeAddr_Object = MibScalar
gs2328fIGMPSnoopingSSMIPRangeAddr = _Gs2328fIGMPSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 3),
    _Gs2328fIGMPSnoopingSSMIPRangeAddr_Type()
)
gs2328fIGMPSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2328fIGMPSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_Gs2328fIGMPSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingSSMIPRangeValue_Object = MibScalar
gs2328fIGMPSnoopingSSMIPRangeValue = _Gs2328fIGMPSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 4),
    _Gs2328fIGMPSnoopingSSMIPRangeValue_Type()
)
gs2328fIGMPSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2328fIGMPSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingProxyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingProxyEnabled_Object = MibScalar
gs2328fIGMPSnoopingProxyEnabled = _Gs2328fIGMPSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 5),
    _Gs2328fIGMPSnoopingProxyEnabled_Type()
)
gs2328fIGMPSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingProxyEnabled.setStatus("current")
_Gs2328fIGMPSnoopingPortRelatedTable_Object = MibTable
gs2328fIGMPSnoopingPortRelatedTable = _Gs2328fIGMPSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortRelatedTable.setStatus("current")
_Gs2328fIGMPSnoopingPortRelatedEntry_Object = MibTableRow
gs2328fIGMPSnoopingPortRelatedEntry = _Gs2328fIGMPSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 6, 1)
)
gs2328fIGMPSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortRelatedEntry.setStatus("current")


class _Gs2328fIGMPSnoopingRouterPort_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingRouterPort_Object = MibTableColumn
gs2328fIGMPSnoopingRouterPort = _Gs2328fIGMPSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 6, 1, 1),
    _Gs2328fIGMPSnoopingRouterPort_Type()
)
gs2328fIGMPSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingRouterPort.setStatus("current")


class _Gs2328fIGMPSnoopingFastLeave_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingFastLeave_Object = MibTableColumn
gs2328fIGMPSnoopingFastLeave = _Gs2328fIGMPSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 6, 1, 2),
    _Gs2328fIGMPSnoopingFastLeave_Type()
)
gs2328fIGMPSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingFastLeave.setStatus("current")


class _Gs2328fIGMPSnoopingThrottling_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2328fIGMPSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingThrottling_Object = MibTableColumn
gs2328fIGMPSnoopingThrottling = _Gs2328fIGMPSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 1, 6, 1, 3),
    _Gs2328fIGMPSnoopingThrottling_Type()
)
gs2328fIGMPSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingThrottling.setStatus("current")
_Gs2328fIGMPSnoopingVLANTable_Object = MibTable
gs2328fIGMPSnoopingVLANTable = _Gs2328fIGMPSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANTable.setStatus("current")
_Gs2328fIGMPSnoopingVLANEntry_Object = MibTableRow
gs2328fIGMPSnoopingVLANEntry = _Gs2328fIGMPSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1)
)
gs2328fIGMPSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIGMPSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANEntry.setStatus("current")


class _Gs2328fIGMPSnoopingVLANID_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIGMPSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANID_Object = MibTableColumn
gs2328fIGMPSnoopingVLANID = _Gs2328fIGMPSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 1),
    _Gs2328fIGMPSnoopingVLANID_Type()
)
gs2328fIGMPSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANID.setStatus("current")


class _Gs2328fIGMPSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANEnable_Object = MibTableColumn
gs2328fIGMPSnoopingVLANEnable = _Gs2328fIGMPSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 2),
    _Gs2328fIGMPSnoopingVLANEnable_Type()
)
gs2328fIGMPSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANEnable.setStatus("current")


class _Gs2328fIGMPSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANIGMPQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIGMPSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2328fIGMPSnoopingVLANIGMPQuerier = _Gs2328fIGMPSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 3),
    _Gs2328fIGMPSnoopingVLANIGMPQuerier_Type()
)
gs2328fIGMPSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2328fIGMPSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANCompatibility based on Integer32"""
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


_Gs2328fIGMPSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANCompatibility_Object = MibTableColumn
gs2328fIGMPSnoopingVLANCompatibility = _Gs2328fIGMPSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 4),
    _Gs2328fIGMPSnoopingVLANCompatibility_Type()
)
gs2328fIGMPSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANCompatibility.setStatus("current")


class _Gs2328fIGMPSnoopingVLANRV_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2328fIGMPSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANRV_Object = MibTableColumn
gs2328fIGMPSnoopingVLANRV = _Gs2328fIGMPSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 5),
    _Gs2328fIGMPSnoopingVLANRV_Type()
)
gs2328fIGMPSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANRV.setStatus("current")


class _Gs2328fIGMPSnoopingVLANQI_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2328fIGMPSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANQI_Object = MibTableColumn
gs2328fIGMPSnoopingVLANQI = _Gs2328fIGMPSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 6),
    _Gs2328fIGMPSnoopingVLANQI_Type()
)
gs2328fIGMPSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANQI.setStatus("current")


class _Gs2328fIGMPSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328fIGMPSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANQRI_Object = MibTableColumn
gs2328fIGMPSnoopingVLANQRI = _Gs2328fIGMPSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 7),
    _Gs2328fIGMPSnoopingVLANQRI_Type()
)
gs2328fIGMPSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANQRI.setStatus("current")


class _Gs2328fIGMPSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328fIGMPSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANLLQI_Object = MibTableColumn
gs2328fIGMPSnoopingVLANLLQI = _Gs2328fIGMPSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 8),
    _Gs2328fIGMPSnoopingVLANLLQI_Type()
)
gs2328fIGMPSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANLLQI.setStatus("current")


class _Gs2328fIGMPSnoopingVLANURI_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328fIGMPSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingVLANURI_Object = MibTableColumn
gs2328fIGMPSnoopingVLANURI = _Gs2328fIGMPSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 2, 1, 9),
    _Gs2328fIGMPSnoopingVLANURI_Type()
)
gs2328fIGMPSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingVLANURI.setStatus("current")
_Gs2328fIGMPSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2328fIGMPSnoopingPortGroupFiltering = _Gs2328fIGMPSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3)
)
_Gs2328fIGMPSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2328fIGMPSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2328fIGMPSnoopingPortGroupFilteringCreate = _Gs2328fIGMPSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 1),
    _Gs2328fIGMPSnoopingPortGroupFilteringCreate_Type()
)
gs2328fIGMPSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2328fIGMPSnoopingPortGroupFilteringTable_Object = MibTable
gs2328fIGMPSnoopingPortGroupFilteringTable = _Gs2328fIGMPSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2328fIGMPSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2328fIGMPSnoopingPortGroupFilteringEntry = _Gs2328fIGMPSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 2, 1)
)
gs2328fIGMPSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIGMPSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2328fIGMPSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fIGMPSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2328fIGMPSnoopingPortGroupFilteringIndex = _Gs2328fIGMPSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 2, 1, 1),
    _Gs2328fIGMPSnoopingPortGroupFilteringIndex_Type()
)
gs2328fIGMPSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2328fIGMPSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fIGMPSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2328fIGMPSnoopingPortGroupFilteringPort = _Gs2328fIGMPSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 2, 1, 2),
    _Gs2328fIGMPSnoopingPortGroupFilteringPort_Type()
)
gs2328fIGMPSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2328fIGMPSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2328fIGMPSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2328fIGMPSnoopingPortGroupFilteringGroups = _Gs2328fIGMPSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 2, 1, 3),
    _Gs2328fIGMPSnoopingPortGroupFilteringGroups_Type()
)
gs2328fIGMPSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2328fIGMPSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2328fIGMPSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2328fIGMPSnoopingPortGroupFilteringRowStatus = _Gs2328fIGMPSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 3, 2, 1, 4),
    _Gs2328fIGMPSnoopingPortGroupFilteringRowStatus_Type()
)
gs2328fIGMPSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2328fIGMPSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2328fIGMPSnoopingStatus = _Gs2328fIGMPSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4)
)


class _Gs2328fIGMPSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingstatisticClear based on Integer32"""
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


_Gs2328fIGMPSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingstatisticClear_Object = MibScalar
gs2328fIGMPSnoopingstatisticClear = _Gs2328fIGMPSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 1),
    _Gs2328fIGMPSnoopingstatisticClear_Type()
)
gs2328fIGMPSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticClear.setStatus("current")
_Gs2328fIGMPSnoopingstatisticTable_Object = MibTable
gs2328fIGMPSnoopingstatisticTable = _Gs2328fIGMPSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticTable.setStatus("current")
_Gs2328fIGMPSnoopingstatisticEntry_Object = MibTableRow
gs2328fIGMPSnoopingstatisticEntry = _Gs2328fIGMPSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1)
)
gs2328fIGMPSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIGMPSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticEntry.setStatus("current")


class _Gs2328fIGMPSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIGMPSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingstatisticVLANID_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticVLANID = _Gs2328fIGMPSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 1),
    _Gs2328fIGMPSnoopingstatisticVLANID_Type()
)
gs2328fIGMPSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticVLANID.setStatus("current")
_Gs2328fIGMPSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2328fIGMPSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticQuerierVersion = _Gs2328fIGMPSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 2),
    _Gs2328fIGMPSnoopingstatisticQuerierVersion_Type()
)
gs2328fIGMPSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2328fIGMPSnoopingstatisticHostVersion_Type = DisplayString
_Gs2328fIGMPSnoopingstatisticHostVersion_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticHostVersion = _Gs2328fIGMPSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 3),
    _Gs2328fIGMPSnoopingstatisticHostVersion_Type()
)
gs2328fIGMPSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticHostVersion.setStatus("current")
_Gs2328fIGMPSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2328fIGMPSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticQuerierStatus = _Gs2328fIGMPSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 4),
    _Gs2328fIGMPSnoopingstatisticQuerierStatus_Type()
)
gs2328fIGMPSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2328fIGMPSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2328fIGMPSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticQueriesTransmitted = _Gs2328fIGMPSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 5),
    _Gs2328fIGMPSnoopingstatisticQueriesTransmitted_Type()
)
gs2328fIGMPSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2328fIGMPSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2328fIGMPSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticQueriesReceived = _Gs2328fIGMPSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 6),
    _Gs2328fIGMPSnoopingstatisticQueriesReceived_Type()
)
gs2328fIGMPSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2328fIGMPSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2328fIGMPSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticV1ReportsReceived = _Gs2328fIGMPSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 7),
    _Gs2328fIGMPSnoopingstatisticV1ReportsReceived_Type()
)
gs2328fIGMPSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2328fIGMPSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2328fIGMPSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticV2ReportsReceived = _Gs2328fIGMPSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 8),
    _Gs2328fIGMPSnoopingstatisticV2ReportsReceived_Type()
)
gs2328fIGMPSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2328fIGMPSnoopingstatisticV3ReportsReceived_Type = Counter32
_Gs2328fIGMPSnoopingstatisticV3ReportsReceived_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticV3ReportsReceived = _Gs2328fIGMPSnoopingstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 9),
    _Gs2328fIGMPSnoopingstatisticV3ReportsReceived_Type()
)
gs2328fIGMPSnoopingstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticV3ReportsReceived.setStatus("current")
_Gs2328fIGMPSnoopingstatisticV2LeavesReceived_Type = Counter32
_Gs2328fIGMPSnoopingstatisticV2LeavesReceived_Object = MibTableColumn
gs2328fIGMPSnoopingstatisticV2LeavesReceived = _Gs2328fIGMPSnoopingstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 2, 1, 10),
    _Gs2328fIGMPSnoopingstatisticV2LeavesReceived_Type()
)
gs2328fIGMPSnoopingstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingstatisticV2LeavesReceived.setStatus("current")
_Gs2328fIGMPSnoopingRouterPortTable_Object = MibTable
gs2328fIGMPSnoopingRouterPortTable = _Gs2328fIGMPSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 3)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingRouterPortTable.setStatus("current")
_Gs2328fIGMPSnoopingRouterPortEntry_Object = MibTableRow
gs2328fIGMPSnoopingRouterPortEntry = _Gs2328fIGMPSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 3, 1)
)
gs2328fIGMPSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingRouterPortEntry.setStatus("current")
_Gs2328fIGMPSnoopingRouterPortStatus_Type = DisplayString
_Gs2328fIGMPSnoopingRouterPortStatus_Object = MibTableColumn
gs2328fIGMPSnoopingRouterPortStatus = _Gs2328fIGMPSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 4, 3, 1, 1),
    _Gs2328fIGMPSnoopingRouterPortStatus_Type()
)
gs2328fIGMPSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingRouterPortStatus.setStatus("current")
_Gs2328fIGMPSnoopingGroupsTable_Object = MibTable
gs2328fIGMPSnoopingGroupsTable = _Gs2328fIGMPSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 5)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingGroupsTable.setStatus("current")
_Gs2328fIGMPSnoopingGroupsEntry_Object = MibTableRow
gs2328fIGMPSnoopingGroupsEntry = _Gs2328fIGMPSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 5, 1)
)
gs2328fIGMPSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIGMPSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingGroupsEntry.setStatus("current")


class _Gs2328fIGMPSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fIGMPSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingGroupsIndex_Object = MibTableColumn
gs2328fIGMPSnoopingGroupsIndex = _Gs2328fIGMPSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 5, 1, 1),
    _Gs2328fIGMPSnoopingGroupsIndex_Type()
)
gs2328fIGMPSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingGroupsIndex.setStatus("current")


class _Gs2328fIGMPSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIGMPSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingGroupsVLANID_Object = MibTableColumn
gs2328fIGMPSnoopingGroupsVLANID = _Gs2328fIGMPSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 5, 1, 2),
    _Gs2328fIGMPSnoopingGroupsVLANID_Type()
)
gs2328fIGMPSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingGroupsVLANID.setStatus("current")
_Gs2328fIGMPSnoopingGroups_Type = DisplayString
_Gs2328fIGMPSnoopingGroups_Object = MibTableColumn
gs2328fIGMPSnoopingGroups = _Gs2328fIGMPSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 5, 1, 3),
    _Gs2328fIGMPSnoopingGroups_Type()
)
gs2328fIGMPSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingGroups.setStatus("current")
_Gs2328fIGMPSnoopingGroupsMemberships_Type = DisplayString
_Gs2328fIGMPSnoopingGroupsMemberships_Object = MibTableColumn
gs2328fIGMPSnoopingGroupsMemberships = _Gs2328fIGMPSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 5, 1, 4),
    _Gs2328fIGMPSnoopingGroupsMemberships_Type()
)
gs2328fIGMPSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingGroupsMemberships.setStatus("current")
_Gs2328fIGMPSnoopingSSMTable_Object = MibTable
gs2328fIGMPSnoopingSSMTable = _Gs2328fIGMPSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6)
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMTable.setStatus("current")
_Gs2328fIGMPSnoopingSSMEntry_Object = MibTableRow
gs2328fIGMPSnoopingSSMEntry = _Gs2328fIGMPSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1)
)
gs2328fIGMPSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIGMPSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMEntry.setStatus("current")


class _Gs2328fIGMPSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fIGMPSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingSSMIndex_Object = MibTableColumn
gs2328fIGMPSnoopingSSMIndex = _Gs2328fIGMPSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 1),
    _Gs2328fIGMPSnoopingSSMIndex_Type()
)
gs2328fIGMPSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMIndex.setStatus("current")


class _Gs2328fIGMPSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIGMPSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingSSMVLANID_Object = MibTableColumn
gs2328fIGMPSnoopingSSMVLANID = _Gs2328fIGMPSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 2),
    _Gs2328fIGMPSnoopingSSMVLANID_Type()
)
gs2328fIGMPSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMVLANID.setStatus("current")
_Gs2328fIGMPSnoopingSSMGroup_Type = DisplayString
_Gs2328fIGMPSnoopingSSMGroup_Object = MibTableColumn
gs2328fIGMPSnoopingSSMGroup = _Gs2328fIGMPSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 3),
    _Gs2328fIGMPSnoopingSSMGroup_Type()
)
gs2328fIGMPSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMGroup.setStatus("current")


class _Gs2328fIGMPSnoopingSSMPort_Type(Integer32):
    """Custom type gs2328fIGMPSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fIGMPSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2328fIGMPSnoopingSSMPort_Object = MibTableColumn
gs2328fIGMPSnoopingSSMPort = _Gs2328fIGMPSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 4),
    _Gs2328fIGMPSnoopingSSMPort_Type()
)
gs2328fIGMPSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMPort.setStatus("current")
_Gs2328fIGMPSnoopingSSMMode_Type = DisplayString
_Gs2328fIGMPSnoopingSSMMode_Object = MibTableColumn
gs2328fIGMPSnoopingSSMMode = _Gs2328fIGMPSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 5),
    _Gs2328fIGMPSnoopingSSMMode_Type()
)
gs2328fIGMPSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMMode.setStatus("current")
_Gs2328fIGMPSnoopingSSMSourceAddress_Type = DisplayString
_Gs2328fIGMPSnoopingSSMSourceAddress_Object = MibTableColumn
gs2328fIGMPSnoopingSSMSourceAddress = _Gs2328fIGMPSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 6),
    _Gs2328fIGMPSnoopingSSMSourceAddress_Type()
)
gs2328fIGMPSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMSourceAddress.setStatus("current")
_Gs2328fIGMPSnoopingSSMType_Type = DisplayString
_Gs2328fIGMPSnoopingSSMType_Object = MibTableColumn
gs2328fIGMPSnoopingSSMType = _Gs2328fIGMPSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 16, 6, 1, 7),
    _Gs2328fIGMPSnoopingSSMType_Type()
)
gs2328fIGMPSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIGMPSnoopingSSMType.setStatus("current")
_Gs2328fMLDSnooping_ObjectIdentity = ObjectIdentity
gs2328fMLDSnooping = _Gs2328fMLDSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17)
)
_Gs2328fMLDSnoopingBasic_ObjectIdentity = ObjectIdentity
gs2328fMLDSnoopingBasic = _Gs2328fMLDSnoopingBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1)
)


class _Gs2328fMLDSnoopingEnable_Type(Integer32):
    """Custom type gs2328fMLDSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingEnable_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingEnable_Object = MibScalar
gs2328fMLDSnoopingEnable = _Gs2328fMLDSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 1),
    _Gs2328fMLDSnoopingEnable_Type()
)
gs2328fMLDSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingEnable.setStatus("current")


class _Gs2328fMLDSnoopingUnregisteredIPMCv6Flooding_Type(Integer32):
    """Custom type gs2328fMLDSnoopingUnregisteredIPMCv6Flooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingUnregisteredIPMCv6Flooding_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingUnregisteredIPMCv6Flooding_Object = MibScalar
gs2328fMLDSnoopingUnregisteredIPMCv6Flooding = _Gs2328fMLDSnoopingUnregisteredIPMCv6Flooding_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 2),
    _Gs2328fMLDSnoopingUnregisteredIPMCv6Flooding_Type()
)
gs2328fMLDSnoopingUnregisteredIPMCv6Flooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingUnregisteredIPMCv6Flooding.setStatus("current")
_Gs2328fMLDSnoopingSSMIPRangeAddr_Type = DisplayString
_Gs2328fMLDSnoopingSSMIPRangeAddr_Object = MibScalar
gs2328fMLDSnoopingSSMIPRangeAddr = _Gs2328fMLDSnoopingSSMIPRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 3),
    _Gs2328fMLDSnoopingSSMIPRangeAddr_Type()
)
gs2328fMLDSnoopingSSMIPRangeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMIPRangeAddr.setStatus("current")


class _Gs2328fMLDSnoopingSSMIPRangeValue_Type(Integer32):
    """Custom type gs2328fMLDSnoopingSSMIPRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 128),
    )


_Gs2328fMLDSnoopingSSMIPRangeValue_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingSSMIPRangeValue_Object = MibScalar
gs2328fMLDSnoopingSSMIPRangeValue = _Gs2328fMLDSnoopingSSMIPRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 4),
    _Gs2328fMLDSnoopingSSMIPRangeValue_Type()
)
gs2328fMLDSnoopingSSMIPRangeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMIPRangeValue.setStatus("current")


class _Gs2328fMLDSnoopingProxyEnabled_Type(Integer32):
    """Custom type gs2328fMLDSnoopingProxyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingProxyEnabled_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingProxyEnabled_Object = MibScalar
gs2328fMLDSnoopingProxyEnabled = _Gs2328fMLDSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 5),
    _Gs2328fMLDSnoopingProxyEnabled_Type()
)
gs2328fMLDSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingProxyEnabled.setStatus("current")
_Gs2328fMLDSnoopingPortRelatedTable_Object = MibTable
gs2328fMLDSnoopingPortRelatedTable = _Gs2328fMLDSnoopingPortRelatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 6)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortRelatedTable.setStatus("current")
_Gs2328fMLDSnoopingPortRelatedEntry_Object = MibTableRow
gs2328fMLDSnoopingPortRelatedEntry = _Gs2328fMLDSnoopingPortRelatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 6, 1)
)
gs2328fMLDSnoopingPortRelatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortRelatedEntry.setStatus("current")


class _Gs2328fMLDSnoopingRouterPort_Type(Integer32):
    """Custom type gs2328fMLDSnoopingRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingRouterPort_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingRouterPort_Object = MibTableColumn
gs2328fMLDSnoopingRouterPort = _Gs2328fMLDSnoopingRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 6, 1, 1),
    _Gs2328fMLDSnoopingRouterPort_Type()
)
gs2328fMLDSnoopingRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingRouterPort.setStatus("current")


class _Gs2328fMLDSnoopingFastLeave_Type(Integer32):
    """Custom type gs2328fMLDSnoopingFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingFastLeave_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingFastLeave_Object = MibTableColumn
gs2328fMLDSnoopingFastLeave = _Gs2328fMLDSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 6, 1, 2),
    _Gs2328fMLDSnoopingFastLeave_Type()
)
gs2328fMLDSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingFastLeave.setStatus("current")


class _Gs2328fMLDSnoopingThrottling_Type(Integer32):
    """Custom type gs2328fMLDSnoopingThrottling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gs2328fMLDSnoopingThrottling_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingThrottling_Object = MibTableColumn
gs2328fMLDSnoopingThrottling = _Gs2328fMLDSnoopingThrottling_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 1, 6, 1, 3),
    _Gs2328fMLDSnoopingThrottling_Type()
)
gs2328fMLDSnoopingThrottling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingThrottling.setStatus("current")
_Gs2328fMLDSnoopingVLANTable_Object = MibTable
gs2328fMLDSnoopingVLANTable = _Gs2328fMLDSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANTable.setStatus("current")
_Gs2328fMLDSnoopingVLANEntry_Object = MibTableRow
gs2328fMLDSnoopingVLANEntry = _Gs2328fMLDSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1)
)
gs2328fMLDSnoopingVLANEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMLDSnoopingVLANID"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANEntry.setStatus("current")


class _Gs2328fMLDSnoopingVLANID_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMLDSnoopingVLANID_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANID_Object = MibTableColumn
gs2328fMLDSnoopingVLANID = _Gs2328fMLDSnoopingVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 1),
    _Gs2328fMLDSnoopingVLANID_Type()
)
gs2328fMLDSnoopingVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANID.setStatus("current")


class _Gs2328fMLDSnoopingVLANEnable_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingVLANEnable_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANEnable_Object = MibTableColumn
gs2328fMLDSnoopingVLANEnable = _Gs2328fMLDSnoopingVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 2),
    _Gs2328fMLDSnoopingVLANEnable_Type()
)
gs2328fMLDSnoopingVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANEnable.setStatus("current")


class _Gs2328fMLDSnoopingVLANIGMPQuerier_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANIGMPQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMLDSnoopingVLANIGMPQuerier_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANIGMPQuerier_Object = MibTableColumn
gs2328fMLDSnoopingVLANIGMPQuerier = _Gs2328fMLDSnoopingVLANIGMPQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 3),
    _Gs2328fMLDSnoopingVLANIGMPQuerier_Type()
)
gs2328fMLDSnoopingVLANIGMPQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANIGMPQuerier.setStatus("current")


class _Gs2328fMLDSnoopingVLANCompatibility_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANCompatibility based on Integer32"""
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


_Gs2328fMLDSnoopingVLANCompatibility_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANCompatibility_Object = MibTableColumn
gs2328fMLDSnoopingVLANCompatibility = _Gs2328fMLDSnoopingVLANCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 4),
    _Gs2328fMLDSnoopingVLANCompatibility_Type()
)
gs2328fMLDSnoopingVLANCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANCompatibility.setStatus("current")


class _Gs2328fMLDSnoopingVLANRV_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANRV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 255),
    )


_Gs2328fMLDSnoopingVLANRV_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANRV_Object = MibTableColumn
gs2328fMLDSnoopingVLANRV = _Gs2328fMLDSnoopingVLANRV_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 5),
    _Gs2328fMLDSnoopingVLANRV_Type()
)
gs2328fMLDSnoopingVLANRV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANRV.setStatus("current")


class _Gs2328fMLDSnoopingVLANQI_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 31744),
    )


_Gs2328fMLDSnoopingVLANQI_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANQI_Object = MibTableColumn
gs2328fMLDSnoopingVLANQI = _Gs2328fMLDSnoopingVLANQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 6),
    _Gs2328fMLDSnoopingVLANQI_Type()
)
gs2328fMLDSnoopingVLANQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANQI.setStatus("current")


class _Gs2328fMLDSnoopingVLANQRI_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANQRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328fMLDSnoopingVLANQRI_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANQRI_Object = MibTableColumn
gs2328fMLDSnoopingVLANQRI = _Gs2328fMLDSnoopingVLANQRI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 7),
    _Gs2328fMLDSnoopingVLANQRI_Type()
)
gs2328fMLDSnoopingVLANQRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANQRI.setStatus("current")


class _Gs2328fMLDSnoopingVLANLLQI_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANLLQI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328fMLDSnoopingVLANLLQI_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANLLQI_Object = MibTableColumn
gs2328fMLDSnoopingVLANLLQI = _Gs2328fMLDSnoopingVLANLLQI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 8),
    _Gs2328fMLDSnoopingVLANLLQI_Type()
)
gs2328fMLDSnoopingVLANLLQI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANLLQI.setStatus("current")


class _Gs2328fMLDSnoopingVLANURI_Type(Integer32):
    """Custom type gs2328fMLDSnoopingVLANURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31744),
    )


_Gs2328fMLDSnoopingVLANURI_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingVLANURI_Object = MibTableColumn
gs2328fMLDSnoopingVLANURI = _Gs2328fMLDSnoopingVLANURI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 2, 1, 9),
    _Gs2328fMLDSnoopingVLANURI_Type()
)
gs2328fMLDSnoopingVLANURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingVLANURI.setStatus("current")
_Gs2328fMLDSnoopingPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2328fMLDSnoopingPortGroupFiltering = _Gs2328fMLDSnoopingPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3)
)
_Gs2328fMLDSnoopingPortGroupFilteringCreate_Type = Integer32
_Gs2328fMLDSnoopingPortGroupFilteringCreate_Object = MibScalar
gs2328fMLDSnoopingPortGroupFilteringCreate = _Gs2328fMLDSnoopingPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 1),
    _Gs2328fMLDSnoopingPortGroupFilteringCreate_Type()
)
gs2328fMLDSnoopingPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringCreate.setStatus("current")
_Gs2328fMLDSnoopingPortGroupFilteringTable_Object = MibTable
gs2328fMLDSnoopingPortGroupFilteringTable = _Gs2328fMLDSnoopingPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringTable.setStatus("current")
_Gs2328fMLDSnoopingPortGroupFilteringEntry_Object = MibTableRow
gs2328fMLDSnoopingPortGroupFilteringEntry = _Gs2328fMLDSnoopingPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 2, 1)
)
gs2328fMLDSnoopingPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMLDSnoopingPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringEntry.setStatus("current")


class _Gs2328fMLDSnoopingPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2328fMLDSnoopingPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMLDSnoopingPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingPortGroupFilteringIndex_Object = MibTableColumn
gs2328fMLDSnoopingPortGroupFilteringIndex = _Gs2328fMLDSnoopingPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 2, 1, 1),
    _Gs2328fMLDSnoopingPortGroupFilteringIndex_Type()
)
gs2328fMLDSnoopingPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringIndex.setStatus("current")


class _Gs2328fMLDSnoopingPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2328fMLDSnoopingPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMLDSnoopingPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingPortGroupFilteringPort_Object = MibTableColumn
gs2328fMLDSnoopingPortGroupFilteringPort = _Gs2328fMLDSnoopingPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 2, 1, 2),
    _Gs2328fMLDSnoopingPortGroupFilteringPort_Type()
)
gs2328fMLDSnoopingPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringPort.setStatus("current")
_Gs2328fMLDSnoopingPortGroupFilteringGroups_Type = DisplayString
_Gs2328fMLDSnoopingPortGroupFilteringGroups_Object = MibTableColumn
gs2328fMLDSnoopingPortGroupFilteringGroups = _Gs2328fMLDSnoopingPortGroupFilteringGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 2, 1, 3),
    _Gs2328fMLDSnoopingPortGroupFilteringGroups_Type()
)
gs2328fMLDSnoopingPortGroupFilteringGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringGroups.setStatus("current")


class _Gs2328fMLDSnoopingPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2328fMLDSnoopingPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2328fMLDSnoopingPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingPortGroupFilteringRowStatus_Object = MibTableColumn
gs2328fMLDSnoopingPortGroupFilteringRowStatus = _Gs2328fMLDSnoopingPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 3, 2, 1, 4),
    _Gs2328fMLDSnoopingPortGroupFilteringRowStatus_Type()
)
gs2328fMLDSnoopingPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingPortGroupFilteringRowStatus.setStatus("current")
_Gs2328fMLDSnoopingStatus_ObjectIdentity = ObjectIdentity
gs2328fMLDSnoopingStatus = _Gs2328fMLDSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4)
)


class _Gs2328fMLDSnoopingstatisticClear_Type(Integer32):
    """Custom type gs2328fMLDSnoopingstatisticClear based on Integer32"""
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


_Gs2328fMLDSnoopingstatisticClear_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingstatisticClear_Object = MibScalar
gs2328fMLDSnoopingstatisticClear = _Gs2328fMLDSnoopingstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 1),
    _Gs2328fMLDSnoopingstatisticClear_Type()
)
gs2328fMLDSnoopingstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticClear.setStatus("current")
_Gs2328fMLDSnoopingstatisticTable_Object = MibTable
gs2328fMLDSnoopingstatisticTable = _Gs2328fMLDSnoopingstatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticTable.setStatus("current")
_Gs2328fMLDSnoopingstatisticEntry_Object = MibTableRow
gs2328fMLDSnoopingstatisticEntry = _Gs2328fMLDSnoopingstatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1)
)
gs2328fMLDSnoopingstatisticEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMLDSnoopingstatisticVLANID"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticEntry.setStatus("current")


class _Gs2328fMLDSnoopingstatisticVLANID_Type(Integer32):
    """Custom type gs2328fMLDSnoopingstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMLDSnoopingstatisticVLANID_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingstatisticVLANID_Object = MibTableColumn
gs2328fMLDSnoopingstatisticVLANID = _Gs2328fMLDSnoopingstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 1),
    _Gs2328fMLDSnoopingstatisticVLANID_Type()
)
gs2328fMLDSnoopingstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticVLANID.setStatus("current")
_Gs2328fMLDSnoopingstatisticQuerierVersion_Type = DisplayString
_Gs2328fMLDSnoopingstatisticQuerierVersion_Object = MibTableColumn
gs2328fMLDSnoopingstatisticQuerierVersion = _Gs2328fMLDSnoopingstatisticQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 2),
    _Gs2328fMLDSnoopingstatisticQuerierVersion_Type()
)
gs2328fMLDSnoopingstatisticQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticQuerierVersion.setStatus("current")
_Gs2328fMLDSnoopingstatisticHostVersion_Type = DisplayString
_Gs2328fMLDSnoopingstatisticHostVersion_Object = MibTableColumn
gs2328fMLDSnoopingstatisticHostVersion = _Gs2328fMLDSnoopingstatisticHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 3),
    _Gs2328fMLDSnoopingstatisticHostVersion_Type()
)
gs2328fMLDSnoopingstatisticHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticHostVersion.setStatus("current")
_Gs2328fMLDSnoopingstatisticQuerierStatus_Type = DisplayString
_Gs2328fMLDSnoopingstatisticQuerierStatus_Object = MibTableColumn
gs2328fMLDSnoopingstatisticQuerierStatus = _Gs2328fMLDSnoopingstatisticQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 4),
    _Gs2328fMLDSnoopingstatisticQuerierStatus_Type()
)
gs2328fMLDSnoopingstatisticQuerierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticQuerierStatus.setStatus("current")
_Gs2328fMLDSnoopingstatisticQueriesTransmitted_Type = Counter32
_Gs2328fMLDSnoopingstatisticQueriesTransmitted_Object = MibTableColumn
gs2328fMLDSnoopingstatisticQueriesTransmitted = _Gs2328fMLDSnoopingstatisticQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 5),
    _Gs2328fMLDSnoopingstatisticQueriesTransmitted_Type()
)
gs2328fMLDSnoopingstatisticQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticQueriesTransmitted.setStatus("current")
_Gs2328fMLDSnoopingstatisticQueriesReceived_Type = Counter32
_Gs2328fMLDSnoopingstatisticQueriesReceived_Object = MibTableColumn
gs2328fMLDSnoopingstatisticQueriesReceived = _Gs2328fMLDSnoopingstatisticQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 6),
    _Gs2328fMLDSnoopingstatisticQueriesReceived_Type()
)
gs2328fMLDSnoopingstatisticQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticQueriesReceived.setStatus("current")
_Gs2328fMLDSnoopingstatisticV1ReportsReceived_Type = Counter32
_Gs2328fMLDSnoopingstatisticV1ReportsReceived_Object = MibTableColumn
gs2328fMLDSnoopingstatisticV1ReportsReceived = _Gs2328fMLDSnoopingstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 7),
    _Gs2328fMLDSnoopingstatisticV1ReportsReceived_Type()
)
gs2328fMLDSnoopingstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticV1ReportsReceived.setStatus("current")
_Gs2328fMLDSnoopingstatisticV2ReportsReceived_Type = Counter32
_Gs2328fMLDSnoopingstatisticV2ReportsReceived_Object = MibTableColumn
gs2328fMLDSnoopingstatisticV2ReportsReceived = _Gs2328fMLDSnoopingstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 8),
    _Gs2328fMLDSnoopingstatisticV2ReportsReceived_Type()
)
gs2328fMLDSnoopingstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticV2ReportsReceived.setStatus("current")
_Gs2328fMLDSnoopingstatisticV1LeavesReceived_Type = Counter32
_Gs2328fMLDSnoopingstatisticV1LeavesReceived_Object = MibTableColumn
gs2328fMLDSnoopingstatisticV1LeavesReceived = _Gs2328fMLDSnoopingstatisticV1LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 2, 1, 9),
    _Gs2328fMLDSnoopingstatisticV1LeavesReceived_Type()
)
gs2328fMLDSnoopingstatisticV1LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingstatisticV1LeavesReceived.setStatus("current")
_Gs2328fMLDSnoopingRouterPortTable_Object = MibTable
gs2328fMLDSnoopingRouterPortTable = _Gs2328fMLDSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 3)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingRouterPortTable.setStatus("current")
_Gs2328fMLDSnoopingRouterPortEntry_Object = MibTableRow
gs2328fMLDSnoopingRouterPortEntry = _Gs2328fMLDSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 3, 1)
)
gs2328fMLDSnoopingRouterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingRouterPortEntry.setStatus("current")
_Gs2328fMLDSnoopingRouterPortStatus_Type = DisplayString
_Gs2328fMLDSnoopingRouterPortStatus_Object = MibTableColumn
gs2328fMLDSnoopingRouterPortStatus = _Gs2328fMLDSnoopingRouterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 4, 3, 1, 1),
    _Gs2328fMLDSnoopingRouterPortStatus_Type()
)
gs2328fMLDSnoopingRouterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingRouterPortStatus.setStatus("current")
_Gs2328fMLDSnoopingGroupsTable_Object = MibTable
gs2328fMLDSnoopingGroupsTable = _Gs2328fMLDSnoopingGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 5)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingGroupsTable.setStatus("current")
_Gs2328fMLDSnoopingGroupsEntry_Object = MibTableRow
gs2328fMLDSnoopingGroupsEntry = _Gs2328fMLDSnoopingGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 5, 1)
)
gs2328fMLDSnoopingGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMLDSnoopingGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingGroupsEntry.setStatus("current")


class _Gs2328fMLDSnoopingGroupsIndex_Type(Integer32):
    """Custom type gs2328fMLDSnoopingGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMLDSnoopingGroupsIndex_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingGroupsIndex_Object = MibTableColumn
gs2328fMLDSnoopingGroupsIndex = _Gs2328fMLDSnoopingGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 5, 1, 1),
    _Gs2328fMLDSnoopingGroupsIndex_Type()
)
gs2328fMLDSnoopingGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingGroupsIndex.setStatus("current")


class _Gs2328fMLDSnoopingGroupsVLANID_Type(Integer32):
    """Custom type gs2328fMLDSnoopingGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMLDSnoopingGroupsVLANID_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingGroupsVLANID_Object = MibTableColumn
gs2328fMLDSnoopingGroupsVLANID = _Gs2328fMLDSnoopingGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 5, 1, 2),
    _Gs2328fMLDSnoopingGroupsVLANID_Type()
)
gs2328fMLDSnoopingGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingGroupsVLANID.setStatus("current")
_Gs2328fMLDSnoopingGroups_Type = DisplayString
_Gs2328fMLDSnoopingGroups_Object = MibTableColumn
gs2328fMLDSnoopingGroups = _Gs2328fMLDSnoopingGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 5, 1, 3),
    _Gs2328fMLDSnoopingGroups_Type()
)
gs2328fMLDSnoopingGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingGroups.setStatus("current")
_Gs2328fMLDSnoopingGroupsMemberships_Type = DisplayString
_Gs2328fMLDSnoopingGroupsMemberships_Object = MibTableColumn
gs2328fMLDSnoopingGroupsMemberships = _Gs2328fMLDSnoopingGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 5, 1, 4),
    _Gs2328fMLDSnoopingGroupsMemberships_Type()
)
gs2328fMLDSnoopingGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingGroupsMemberships.setStatus("current")
_Gs2328fMLDSnoopingSSMTable_Object = MibTable
gs2328fMLDSnoopingSSMTable = _Gs2328fMLDSnoopingSSMTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6)
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMTable.setStatus("current")
_Gs2328fMLDSnoopingSSMEntry_Object = MibTableRow
gs2328fMLDSnoopingSSMEntry = _Gs2328fMLDSnoopingSSMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1)
)
gs2328fMLDSnoopingSSMEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMLDSnoopingSSMIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMEntry.setStatus("current")


class _Gs2328fMLDSnoopingSSMIndex_Type(Integer32):
    """Custom type gs2328fMLDSnoopingSSMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMLDSnoopingSSMIndex_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingSSMIndex_Object = MibTableColumn
gs2328fMLDSnoopingSSMIndex = _Gs2328fMLDSnoopingSSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 1),
    _Gs2328fMLDSnoopingSSMIndex_Type()
)
gs2328fMLDSnoopingSSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMIndex.setStatus("current")


class _Gs2328fMLDSnoopingSSMVLANID_Type(Integer32):
    """Custom type gs2328fMLDSnoopingSSMVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMLDSnoopingSSMVLANID_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingSSMVLANID_Object = MibTableColumn
gs2328fMLDSnoopingSSMVLANID = _Gs2328fMLDSnoopingSSMVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 2),
    _Gs2328fMLDSnoopingSSMVLANID_Type()
)
gs2328fMLDSnoopingSSMVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMVLANID.setStatus("current")
_Gs2328fMLDSnoopingSSMGroup_Type = DisplayString
_Gs2328fMLDSnoopingSSMGroup_Object = MibTableColumn
gs2328fMLDSnoopingSSMGroup = _Gs2328fMLDSnoopingSSMGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 3),
    _Gs2328fMLDSnoopingSSMGroup_Type()
)
gs2328fMLDSnoopingSSMGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMGroup.setStatus("current")


class _Gs2328fMLDSnoopingSSMPort_Type(Integer32):
    """Custom type gs2328fMLDSnoopingSSMPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMLDSnoopingSSMPort_Type.__name__ = "Integer32"
_Gs2328fMLDSnoopingSSMPort_Object = MibTableColumn
gs2328fMLDSnoopingSSMPort = _Gs2328fMLDSnoopingSSMPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 4),
    _Gs2328fMLDSnoopingSSMPort_Type()
)
gs2328fMLDSnoopingSSMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMPort.setStatus("current")
_Gs2328fMLDSnoopingSSMMode_Type = DisplayString
_Gs2328fMLDSnoopingSSMMode_Object = MibTableColumn
gs2328fMLDSnoopingSSMMode = _Gs2328fMLDSnoopingSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 5),
    _Gs2328fMLDSnoopingSSMMode_Type()
)
gs2328fMLDSnoopingSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMMode.setStatus("current")
_Gs2328fMLDSnoopingSSMSourceAddress_Type = DisplayString
_Gs2328fMLDSnoopingSSMSourceAddress_Object = MibTableColumn
gs2328fMLDSnoopingSSMSourceAddress = _Gs2328fMLDSnoopingSSMSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 6),
    _Gs2328fMLDSnoopingSSMSourceAddress_Type()
)
gs2328fMLDSnoopingSSMSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMSourceAddress.setStatus("current")
_Gs2328fMLDSnoopingSSMType_Type = DisplayString
_Gs2328fMLDSnoopingSSMType_Object = MibTableColumn
gs2328fMLDSnoopingSSMType = _Gs2328fMLDSnoopingSSMType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 17, 6, 1, 7),
    _Gs2328fMLDSnoopingSSMType_Type()
)
gs2328fMLDSnoopingSSMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMLDSnoopingSSMType.setStatus("current")
_Gs2328fMVR_ObjectIdentity = ObjectIdentity
gs2328fMVR = _Gs2328fMVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18)
)
_Gs2328fMVRConfiguration_ObjectIdentity = ObjectIdentity
gs2328fMVRConfiguration = _Gs2328fMVRConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1)
)


class _Gs2328fMVRMode_Type(Integer32):
    """Custom type gs2328fMVRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMVRMode_Type.__name__ = "Integer32"
_Gs2328fMVRMode_Object = MibScalar
gs2328fMVRMode = _Gs2328fMVRMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 1),
    _Gs2328fMVRMode_Type()
)
gs2328fMVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRMode.setStatus("current")


class _Gs2328fMVRVLANId_Type(Integer32):
    """Custom type gs2328fMVRVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fMVRVLANId_Type.__name__ = "Integer32"
_Gs2328fMVRVLANId_Object = MibScalar
gs2328fMVRVLANId = _Gs2328fMVRVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 2),
    _Gs2328fMVRVLANId_Type()
)
gs2328fMVRVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRVLANId.setStatus("current")
_Gs2328fMVRPortConfigurationTable_Object = MibTable
gs2328fMVRPortConfigurationTable = _Gs2328fMVRPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 3)
)
if mibBuilder.loadTexts:
    gs2328fMVRPortConfigurationTable.setStatus("current")
_Gs2328fMVRPortConfigurationEntry_Object = MibTableRow
gs2328fMVRPortConfigurationEntry = _Gs2328fMVRPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 3, 1)
)
gs2328fMVRPortConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMVRPortConfigurationEntry.setStatus("current")


class _Gs2328fMVRPortConfigurationMode_Type(Integer32):
    """Custom type gs2328fMVRPortConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMVRPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2328fMVRPortConfigurationMode_Object = MibTableColumn
gs2328fMVRPortConfigurationMode = _Gs2328fMVRPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 3, 1, 1),
    _Gs2328fMVRPortConfigurationMode_Type()
)
gs2328fMVRPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortConfigurationMode.setStatus("current")


class _Gs2328fMVRPortConfigurationType_Type(Integer32):
    """Custom type gs2328fMVRPortConfigurationType based on Integer32"""
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


_Gs2328fMVRPortConfigurationType_Type.__name__ = "Integer32"
_Gs2328fMVRPortConfigurationType_Object = MibTableColumn
gs2328fMVRPortConfigurationType = _Gs2328fMVRPortConfigurationType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 3, 1, 2),
    _Gs2328fMVRPortConfigurationType_Type()
)
gs2328fMVRPortConfigurationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortConfigurationType.setStatus("current")


class _Gs2328fMVRPortConfigurationImmediateLeave_Type(Integer32):
    """Custom type gs2328fMVRPortConfigurationImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fMVRPortConfigurationImmediateLeave_Type.__name__ = "Integer32"
_Gs2328fMVRPortConfigurationImmediateLeave_Object = MibTableColumn
gs2328fMVRPortConfigurationImmediateLeave = _Gs2328fMVRPortConfigurationImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 1, 3, 1, 3),
    _Gs2328fMVRPortConfigurationImmediateLeave_Type()
)
gs2328fMVRPortConfigurationImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortConfigurationImmediateLeave.setStatus("current")
_Gs2328fMVRPortGroupFiltering_ObjectIdentity = ObjectIdentity
gs2328fMVRPortGroupFiltering = _Gs2328fMVRPortGroupFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2)
)
_Gs2328fMVRPortGroupFilteringCreate_Type = Integer32
_Gs2328fMVRPortGroupFilteringCreate_Object = MibScalar
gs2328fMVRPortGroupFilteringCreate = _Gs2328fMVRPortGroupFilteringCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 1),
    _Gs2328fMVRPortGroupFilteringCreate_Type()
)
gs2328fMVRPortGroupFilteringCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringCreate.setStatus("current")
_Gs2328fMVRPortGroupFilteringTable_Object = MibTable
gs2328fMVRPortGroupFilteringTable = _Gs2328fMVRPortGroupFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringTable.setStatus("current")
_Gs2328fMVRPortGroupFilteringEntry_Object = MibTableRow
gs2328fMVRPortGroupFilteringEntry = _Gs2328fMVRPortGroupFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2, 1)
)
gs2328fMVRPortGroupFilteringEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMVRPortGroupFilteringIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringEntry.setStatus("current")


class _Gs2328fMVRPortGroupFilteringIndex_Type(Integer32):
    """Custom type gs2328fMVRPortGroupFilteringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMVRPortGroupFilteringIndex_Type.__name__ = "Integer32"
_Gs2328fMVRPortGroupFilteringIndex_Object = MibTableColumn
gs2328fMVRPortGroupFilteringIndex = _Gs2328fMVRPortGroupFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2, 1, 1),
    _Gs2328fMVRPortGroupFilteringIndex_Type()
)
gs2328fMVRPortGroupFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringIndex.setStatus("current")


class _Gs2328fMVRPortGroupFilteringPort_Type(Integer32):
    """Custom type gs2328fMVRPortGroupFilteringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMVRPortGroupFilteringPort_Type.__name__ = "Integer32"
_Gs2328fMVRPortGroupFilteringPort_Object = MibTableColumn
gs2328fMVRPortGroupFilteringPort = _Gs2328fMVRPortGroupFilteringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2, 1, 2),
    _Gs2328fMVRPortGroupFilteringPort_Type()
)
gs2328fMVRPortGroupFilteringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringPort.setStatus("current")
_Gs2328fMVRPortGroupFilteringStartGroups_Type = DisplayString
_Gs2328fMVRPortGroupFilteringStartGroups_Object = MibTableColumn
gs2328fMVRPortGroupFilteringStartGroups = _Gs2328fMVRPortGroupFilteringStartGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2, 1, 3),
    _Gs2328fMVRPortGroupFilteringStartGroups_Type()
)
gs2328fMVRPortGroupFilteringStartGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringStartGroups.setStatus("current")
_Gs2328fMVRPortGroupFilteringEndGroups_Type = DisplayString
_Gs2328fMVRPortGroupFilteringEndGroups_Object = MibTableColumn
gs2328fMVRPortGroupFilteringEndGroups = _Gs2328fMVRPortGroupFilteringEndGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2, 1, 4),
    _Gs2328fMVRPortGroupFilteringEndGroups_Type()
)
gs2328fMVRPortGroupFilteringEndGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringEndGroups.setStatus("current")


class _Gs2328fMVRPortGroupFilteringRowStatus_Type(Integer32):
    """Custom type gs2328fMVRPortGroupFilteringRowStatus based on Integer32"""
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


_Gs2328fMVRPortGroupFilteringRowStatus_Type.__name__ = "Integer32"
_Gs2328fMVRPortGroupFilteringRowStatus_Object = MibTableColumn
gs2328fMVRPortGroupFilteringRowStatus = _Gs2328fMVRPortGroupFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 2, 2, 1, 5),
    _Gs2328fMVRPortGroupFilteringRowStatus_Type()
)
gs2328fMVRPortGroupFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRPortGroupFilteringRowStatus.setStatus("current")
_Gs2328fMVRGroupsTable_Object = MibTable
gs2328fMVRGroupsTable = _Gs2328fMVRGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gs2328fMVRGroupsTable.setStatus("current")
_Gs2328fMVRGroupsEntry_Object = MibTableRow
gs2328fMVRGroupsEntry = _Gs2328fMVRGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 3, 1)
)
gs2328fMVRGroupsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMVRGroupsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMVRGroupsEntry.setStatus("current")


class _Gs2328fMVRGroupsIndex_Type(Integer32):
    """Custom type gs2328fMVRGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fMVRGroupsIndex_Type.__name__ = "Integer32"
_Gs2328fMVRGroupsIndex_Object = MibTableColumn
gs2328fMVRGroupsIndex = _Gs2328fMVRGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 3, 1, 1),
    _Gs2328fMVRGroupsIndex_Type()
)
gs2328fMVRGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMVRGroupsIndex.setStatus("current")


class _Gs2328fMVRGroupsVLANID_Type(Integer32):
    """Custom type gs2328fMVRGroupsVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMVRGroupsVLANID_Type.__name__ = "Integer32"
_Gs2328fMVRGroupsVLANID_Object = MibTableColumn
gs2328fMVRGroupsVLANID = _Gs2328fMVRGroupsVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 3, 1, 2),
    _Gs2328fMVRGroupsVLANID_Type()
)
gs2328fMVRGroupsVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRGroupsVLANID.setStatus("current")
_Gs2328fMVRGroups_Type = DisplayString
_Gs2328fMVRGroups_Object = MibTableColumn
gs2328fMVRGroups = _Gs2328fMVRGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 3, 1, 3),
    _Gs2328fMVRGroups_Type()
)
gs2328fMVRGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRGroups.setStatus("current")
_Gs2328fMVRGroupsMemberships_Type = DisplayString
_Gs2328fMVRGroupsMemberships_Object = MibTableColumn
gs2328fMVRGroupsMemberships = _Gs2328fMVRGroupsMemberships_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 3, 1, 4),
    _Gs2328fMVRGroupsMemberships_Type()
)
gs2328fMVRGroupsMemberships.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRGroupsMemberships.setStatus("current")
_Gs2328fMVRStatus_ObjectIdentity = ObjectIdentity
gs2328fMVRStatus = _Gs2328fMVRStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4)
)


class _Gs2328fMVRstatisticClear_Type(Integer32):
    """Custom type gs2328fMVRstatisticClear based on Integer32"""
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


_Gs2328fMVRstatisticClear_Type.__name__ = "Integer32"
_Gs2328fMVRstatisticClear_Object = MibScalar
gs2328fMVRstatisticClear = _Gs2328fMVRstatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4, 1),
    _Gs2328fMVRstatisticClear_Type()
)
gs2328fMVRstatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fMVRstatisticClear.setStatus("current")


class _Gs2328fMVRstatisticVLANID_Type(Integer32):
    """Custom type gs2328fMVRstatisticVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMVRstatisticVLANID_Type.__name__ = "Integer32"
_Gs2328fMVRstatisticVLANID_Object = MibScalar
gs2328fMVRstatisticVLANID = _Gs2328fMVRstatisticVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4, 2),
    _Gs2328fMVRstatisticVLANID_Type()
)
gs2328fMVRstatisticVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRstatisticVLANID.setStatus("current")
_Gs2328fMVRstatisticV1ReportsReceived_Type = Counter32
_Gs2328fMVRstatisticV1ReportsReceived_Object = MibScalar
gs2328fMVRstatisticV1ReportsReceived = _Gs2328fMVRstatisticV1ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4, 3),
    _Gs2328fMVRstatisticV1ReportsReceived_Type()
)
gs2328fMVRstatisticV1ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRstatisticV1ReportsReceived.setStatus("current")
_Gs2328fMVRstatisticV2ReportsReceived_Type = Counter32
_Gs2328fMVRstatisticV2ReportsReceived_Object = MibScalar
gs2328fMVRstatisticV2ReportsReceived = _Gs2328fMVRstatisticV2ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4, 4),
    _Gs2328fMVRstatisticV2ReportsReceived_Type()
)
gs2328fMVRstatisticV2ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRstatisticV2ReportsReceived.setStatus("current")
_Gs2328fMVRstatisticV3ReportsReceived_Type = Counter32
_Gs2328fMVRstatisticV3ReportsReceived_Object = MibScalar
gs2328fMVRstatisticV3ReportsReceived = _Gs2328fMVRstatisticV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4, 5),
    _Gs2328fMVRstatisticV3ReportsReceived_Type()
)
gs2328fMVRstatisticV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRstatisticV3ReportsReceived.setStatus("current")
_Gs2328fMVRstatisticV2LeavesReceived_Type = Counter32
_Gs2328fMVRstatisticV2LeavesReceived_Object = MibScalar
gs2328fMVRstatisticV2LeavesReceived = _Gs2328fMVRstatisticV2LeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 18, 4, 6),
    _Gs2328fMVRstatisticV2LeavesReceived_Type()
)
gs2328fMVRstatisticV2LeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMVRstatisticV2LeavesReceived.setStatus("current")
_Gs2328fLACP_ObjectIdentity = ObjectIdentity
gs2328fLACP = _Gs2328fLACP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19)
)
_Gs2328fLACPConf_ObjectIdentity = ObjectIdentity
gs2328fLACPConf = _Gs2328fLACPConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1)
)
_Gs2328fLACPPortConfigurationTable_Object = MibTable
gs2328fLACPPortConfigurationTable = _Gs2328fLACPPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    gs2328fLACPPortConfigurationTable.setStatus("current")
_Gs2328fLACPPortConfigurationEntry_Object = MibTableRow
gs2328fLACPPortConfigurationEntry = _Gs2328fLACPPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1, 1, 1)
)
gs2328fLACPPortConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fLACPPortConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2328fLACPPortConfigurationEntry.setStatus("current")


class _Gs2328fLACPPortConfigurationPort_Type(Integer32):
    """Custom type gs2328fLACPPortConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fLACPPortConfigurationPort_Type.__name__ = "Integer32"
_Gs2328fLACPPortConfigurationPort_Object = MibTableColumn
gs2328fLACPPortConfigurationPort = _Gs2328fLACPPortConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1, 1, 1, 1),
    _Gs2328fLACPPortConfigurationPort_Type()
)
gs2328fLACPPortConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fLACPPortConfigurationPort.setStatus("current")


class _Gs2328fLACPPortConfigurationMode_Type(Integer32):
    """Custom type gs2328fLACPPortConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fLACPPortConfigurationMode_Type.__name__ = "Integer32"
_Gs2328fLACPPortConfigurationMode_Object = MibTableColumn
gs2328fLACPPortConfigurationMode = _Gs2328fLACPPortConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1, 1, 1, 2),
    _Gs2328fLACPPortConfigurationMode_Type()
)
gs2328fLACPPortConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLACPPortConfigurationMode.setStatus("current")


class _Gs2328fLACPPortConfigurationKey_Type(Integer32):
    """Custom type gs2328fLACPPortConfigurationKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328fLACPPortConfigurationKey_Type.__name__ = "Integer32"
_Gs2328fLACPPortConfigurationKey_Object = MibTableColumn
gs2328fLACPPortConfigurationKey = _Gs2328fLACPPortConfigurationKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1, 1, 1, 3),
    _Gs2328fLACPPortConfigurationKey_Type()
)
gs2328fLACPPortConfigurationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLACPPortConfigurationKey.setStatus("current")


class _Gs2328fLACPPortConfigurationRole_Type(Integer32):
    """Custom type gs2328fLACPPortConfigurationRole based on Integer32"""
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


_Gs2328fLACPPortConfigurationRole_Type.__name__ = "Integer32"
_Gs2328fLACPPortConfigurationRole_Object = MibTableColumn
gs2328fLACPPortConfigurationRole = _Gs2328fLACPPortConfigurationRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 1, 1, 1, 4),
    _Gs2328fLACPPortConfigurationRole_Type()
)
gs2328fLACPPortConfigurationRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLACPPortConfigurationRole.setStatus("current")
_Gs2328fLACPSystemStatusTable_Object = MibTable
gs2328fLACPSystemStatusTable = _Gs2328fLACPSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2)
)
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusTable.setStatus("current")
_Gs2328fLACPSystemStatusEntry_Object = MibTableRow
gs2328fLACPSystemStatusEntry = _Gs2328fLACPSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1)
)
gs2328fLACPSystemStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fLACPSystemStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusEntry.setStatus("current")


class _Gs2328fLACPSystemStatusIndex_Type(Integer32):
    """Custom type gs2328fLACPSystemStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Gs2328fLACPSystemStatusIndex_Type.__name__ = "Integer32"
_Gs2328fLACPSystemStatusIndex_Object = MibTableColumn
gs2328fLACPSystemStatusIndex = _Gs2328fLACPSystemStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1, 1),
    _Gs2328fLACPSystemStatusIndex_Type()
)
gs2328fLACPSystemStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusIndex.setStatus("current")
_Gs2328fLACPSystemStatusAggrID_Type = DisplayString
_Gs2328fLACPSystemStatusAggrID_Object = MibTableColumn
gs2328fLACPSystemStatusAggrID = _Gs2328fLACPSystemStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1, 2),
    _Gs2328fLACPSystemStatusAggrID_Type()
)
gs2328fLACPSystemStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusAggrID.setStatus("current")
_Gs2328fLACPSystemStatusPartnerSystemID_Type = MacAddress
_Gs2328fLACPSystemStatusPartnerSystemID_Object = MibTableColumn
gs2328fLACPSystemStatusPartnerSystemID = _Gs2328fLACPSystemStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1, 3),
    _Gs2328fLACPSystemStatusPartnerSystemID_Type()
)
gs2328fLACPSystemStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusPartnerSystemID.setStatus("current")
_Gs2328fLACPSystemStatusPartnerKey_Type = DisplayString
_Gs2328fLACPSystemStatusPartnerKey_Object = MibTableColumn
gs2328fLACPSystemStatusPartnerKey = _Gs2328fLACPSystemStatusPartnerKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1, 4),
    _Gs2328fLACPSystemStatusPartnerKey_Type()
)
gs2328fLACPSystemStatusPartnerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusPartnerKey.setStatus("current")
_Gs2328fLACPSystemStatusLastchanged_Type = DisplayString
_Gs2328fLACPSystemStatusLastchanged_Object = MibTableColumn
gs2328fLACPSystemStatusLastchanged = _Gs2328fLACPSystemStatusLastchanged_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1, 5),
    _Gs2328fLACPSystemStatusLastchanged_Type()
)
gs2328fLACPSystemStatusLastchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusLastchanged.setStatus("current")
_Gs2328fLACPSystemStatusLocalPorts_Type = DisplayString
_Gs2328fLACPSystemStatusLocalPorts_Object = MibTableColumn
gs2328fLACPSystemStatusLocalPorts = _Gs2328fLACPSystemStatusLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 2, 1, 6),
    _Gs2328fLACPSystemStatusLocalPorts_Type()
)
gs2328fLACPSystemStatusLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPSystemStatusLocalPorts.setStatus("current")
_Gs2328fLACPStatusTable_Object = MibTable
gs2328fLACPStatusTable = _Gs2328fLACPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3)
)
if mibBuilder.loadTexts:
    gs2328fLACPStatusTable.setStatus("current")
_Gs2328fLACPStatusEntry_Object = MibTableRow
gs2328fLACPStatusEntry = _Gs2328fLACPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1)
)
gs2328fLACPStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fLACPStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328fLACPStatusEntry.setStatus("current")


class _Gs2328fLACPStatusPort_Type(Integer32):
    """Custom type gs2328fLACPStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fLACPStatusPort_Type.__name__ = "Integer32"
_Gs2328fLACPStatusPort_Object = MibTableColumn
gs2328fLACPStatusPort = _Gs2328fLACPStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1, 1),
    _Gs2328fLACPStatusPort_Type()
)
gs2328fLACPStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fLACPStatusPort.setStatus("current")
_Gs2328fLACPStatusLACP_Type = DisplayString
_Gs2328fLACPStatusLACP_Object = MibTableColumn
gs2328fLACPStatusLACP = _Gs2328fLACPStatusLACP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1, 2),
    _Gs2328fLACPStatusLACP_Type()
)
gs2328fLACPStatusLACP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPStatusLACP.setStatus("current")
_Gs2328fLACPStatusKey_Type = DisplayString
_Gs2328fLACPStatusKey_Object = MibTableColumn
gs2328fLACPStatusKey = _Gs2328fLACPStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1, 3),
    _Gs2328fLACPStatusKey_Type()
)
gs2328fLACPStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPStatusKey.setStatus("current")
_Gs2328fLACPStatusAggrID_Type = DisplayString
_Gs2328fLACPStatusAggrID_Object = MibTableColumn
gs2328fLACPStatusAggrID = _Gs2328fLACPStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1, 4),
    _Gs2328fLACPStatusAggrID_Type()
)
gs2328fLACPStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPStatusAggrID.setStatus("current")
_Gs2328fLACPStatusPartnerSystemID_Type = DisplayString
_Gs2328fLACPStatusPartnerSystemID_Object = MibTableColumn
gs2328fLACPStatusPartnerSystemID = _Gs2328fLACPStatusPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1, 5),
    _Gs2328fLACPStatusPartnerSystemID_Type()
)
gs2328fLACPStatusPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPStatusPartnerSystemID.setStatus("current")
_Gs2328fLACPStatusPartnerPort_Type = DisplayString
_Gs2328fLACPStatusPartnerPort_Object = MibTableColumn
gs2328fLACPStatusPartnerPort = _Gs2328fLACPStatusPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 3, 1, 6),
    _Gs2328fLACPStatusPartnerPort_Type()
)
gs2328fLACPStatusPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPStatusPartnerPort.setStatus("current")
_Gs2328fLACPStatisticsTable_Object = MibTable
gs2328fLACPStatisticsTable = _Gs2328fLACPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4)
)
if mibBuilder.loadTexts:
    gs2328fLACPStatisticsTable.setStatus("current")
_Gs2328fLACPStatisticsEntry_Object = MibTableRow
gs2328fLACPStatisticsEntry = _Gs2328fLACPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4, 1)
)
gs2328fLACPStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fLACPStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328fLACPStatisticsEntry.setStatus("current")


class _Gs2328fLACPStatisticsPort_Type(Integer32):
    """Custom type gs2328fLACPStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fLACPStatisticsPort_Type.__name__ = "Integer32"
_Gs2328fLACPStatisticsPort_Object = MibTableColumn
gs2328fLACPStatisticsPort = _Gs2328fLACPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4, 1, 1),
    _Gs2328fLACPStatisticsPort_Type()
)
gs2328fLACPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fLACPStatisticsPort.setStatus("current")
_Gs2328fLACPReceived_Type = Counter32
_Gs2328fLACPReceived_Object = MibTableColumn
gs2328fLACPReceived = _Gs2328fLACPReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4, 1, 2),
    _Gs2328fLACPReceived_Type()
)
gs2328fLACPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPReceived.setStatus("current")
_Gs2328fLACPTransmitted_Type = Counter32
_Gs2328fLACPTransmitted_Object = MibTableColumn
gs2328fLACPTransmitted = _Gs2328fLACPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4, 1, 3),
    _Gs2328fLACPTransmitted_Type()
)
gs2328fLACPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPTransmitted.setStatus("current")
_Gs2328fLACPDiscardedUnknown_Type = Counter32
_Gs2328fLACPDiscardedUnknown_Object = MibTableColumn
gs2328fLACPDiscardedUnknown = _Gs2328fLACPDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4, 1, 4),
    _Gs2328fLACPDiscardedUnknown_Type()
)
gs2328fLACPDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPDiscardedUnknown.setStatus("current")
_Gs2328fLACPDiscardedIllegal_Type = Counter32
_Gs2328fLACPDiscardedIllegal_Object = MibTableColumn
gs2328fLACPDiscardedIllegal = _Gs2328fLACPDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 4, 1, 5),
    _Gs2328fLACPDiscardedIllegal_Type()
)
gs2328fLACPDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLACPDiscardedIllegal.setStatus("current")


class _Gs2328fLACPStatisticsClear_Type(Integer32):
    """Custom type gs2328fLACPStatisticsClear based on Integer32"""
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


_Gs2328fLACPStatisticsClear_Type.__name__ = "Integer32"
_Gs2328fLACPStatisticsClear_Object = MibScalar
gs2328fLACPStatisticsClear = _Gs2328fLACPStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 19, 5),
    _Gs2328fLACPStatisticsClear_Type()
)
gs2328fLACPStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLACPStatisticsClear.setStatus("current")
_Gs2328fSTP_ObjectIdentity = ObjectIdentity
gs2328fSTP = _Gs2328fSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20)
)
_Gs2328fSTPBridgeBasicConf_ObjectIdentity = ObjectIdentity
gs2328fSTPBridgeBasicConf = _Gs2328fSTPBridgeBasicConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1)
)


class _Gs2328fSTPBridgeProtocolVersion_Type(Integer32):
    """Custom type gs2328fSTPBridgeProtocolVersion based on Integer32"""
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


_Gs2328fSTPBridgeProtocolVersion_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeProtocolVersion_Object = MibScalar
gs2328fSTPBridgeProtocolVersion = _Gs2328fSTPBridgeProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1, 1),
    _Gs2328fSTPBridgeProtocolVersion_Type()
)
gs2328fSTPBridgeProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeProtocolVersion.setStatus("current")


class _Gs2328fSTPBridgePriority_Type(Integer32):
    """Custom type gs2328fSTPBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPBridgePriority_Type.__name__ = "Integer32"
_Gs2328fSTPBridgePriority_Object = MibScalar
gs2328fSTPBridgePriority = _Gs2328fSTPBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1, 2),
    _Gs2328fSTPBridgePriority_Type()
)
gs2328fSTPBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgePriority.setStatus("current")


class _Gs2328fSTPBridgeForwardDelay_Type(Integer32):
    """Custom type gs2328fSTPBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Gs2328fSTPBridgeForwardDelay_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeForwardDelay_Object = MibScalar
gs2328fSTPBridgeForwardDelay = _Gs2328fSTPBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1, 3),
    _Gs2328fSTPBridgeForwardDelay_Type()
)
gs2328fSTPBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeForwardDelay.setStatus("current")


class _Gs2328fSTPBridgeMaxAge_Type(Integer32):
    """Custom type gs2328fSTPBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2328fSTPBridgeMaxAge_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeMaxAge_Object = MibScalar
gs2328fSTPBridgeMaxAge = _Gs2328fSTPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1, 4),
    _Gs2328fSTPBridgeMaxAge_Type()
)
gs2328fSTPBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeMaxAge.setStatus("current")


class _Gs2328fSTPBridgeMaximumHopCount_Type(Integer32):
    """Custom type gs2328fSTPBridgeMaximumHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2328fSTPBridgeMaximumHopCount_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeMaximumHopCount_Object = MibScalar
gs2328fSTPBridgeMaximumHopCount = _Gs2328fSTPBridgeMaximumHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1, 5),
    _Gs2328fSTPBridgeMaximumHopCount_Type()
)
gs2328fSTPBridgeMaximumHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeMaximumHopCount.setStatus("current")


class _Gs2328fSTPBridgeTransmitHoldCount_Type(Integer32):
    """Custom type gs2328fSTPBridgeTransmitHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328fSTPBridgeTransmitHoldCount_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeTransmitHoldCount_Object = MibScalar
gs2328fSTPBridgeTransmitHoldCount = _Gs2328fSTPBridgeTransmitHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 1, 6),
    _Gs2328fSTPBridgeTransmitHoldCount_Type()
)
gs2328fSTPBridgeTransmitHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeTransmitHoldCount.setStatus("current")
_Gs2328fSTPBridgeAdvancedConf_ObjectIdentity = ObjectIdentity
gs2328fSTPBridgeAdvancedConf = _Gs2328fSTPBridgeAdvancedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 2)
)


class _Gs2328fSTPBridgeEdgePortBPDUFiltering_Type(Integer32):
    """Custom type gs2328fSTPBridgeEdgePortBPDUFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPBridgeEdgePortBPDUFiltering_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeEdgePortBPDUFiltering_Object = MibScalar
gs2328fSTPBridgeEdgePortBPDUFiltering = _Gs2328fSTPBridgeEdgePortBPDUFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 2, 1),
    _Gs2328fSTPBridgeEdgePortBPDUFiltering_Type()
)
gs2328fSTPBridgeEdgePortBPDUFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeEdgePortBPDUFiltering.setStatus("current")


class _Gs2328fSTPBridgeEdgePortBPDUGuard_Type(Integer32):
    """Custom type gs2328fSTPBridgeEdgePortBPDUGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPBridgeEdgePortBPDUGuard_Type.__name__ = "Integer32"
_Gs2328fSTPBridgeEdgePortBPDUGuard_Object = MibScalar
gs2328fSTPBridgeEdgePortBPDUGuard = _Gs2328fSTPBridgeEdgePortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 2, 2),
    _Gs2328fSTPBridgeEdgePortBPDUGuard_Type()
)
gs2328fSTPBridgeEdgePortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgeEdgePortBPDUGuard.setStatus("current")


class _Gs2328fSTPBridgePortErrorRecoveryTimeout_Type(Integer32):
    """Custom type gs2328fSTPBridgePortErrorRecoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Gs2328fSTPBridgePortErrorRecoveryTimeout_Type.__name__ = "Integer32"
_Gs2328fSTPBridgePortErrorRecoveryTimeout_Object = MibScalar
gs2328fSTPBridgePortErrorRecoveryTimeout = _Gs2328fSTPBridgePortErrorRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 2, 3),
    _Gs2328fSTPBridgePortErrorRecoveryTimeout_Type()
)
gs2328fSTPBridgePortErrorRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPBridgePortErrorRecoveryTimeout.setStatus("current")
_Gs2328fSTPMSTIConf_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTIConf = _Gs2328fSTPMSTIConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 3)
)


class _Gs2328fSTPMSTIConfigurationName_Type(DisplayString):
    """Custom type gs2328fSTPMSTIConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Gs2328fSTPMSTIConfigurationName_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTIConfigurationName_Object = MibScalar
gs2328fSTPMSTIConfigurationName = _Gs2328fSTPMSTIConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 3, 1),
    _Gs2328fSTPMSTIConfigurationName_Type()
)
gs2328fSTPMSTIConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTIConfigurationName.setStatus("current")


class _Gs2328fSTPMSTIConfigurationRevision_Type(Integer32):
    """Custom type gs2328fSTPMSTIConfigurationRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328fSTPMSTIConfigurationRevision_Type.__name__ = "Integer32"
_Gs2328fSTPMSTIConfigurationRevision_Object = MibScalar
gs2328fSTPMSTIConfigurationRevision = _Gs2328fSTPMSTIConfigurationRevision_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 3, 2),
    _Gs2328fSTPMSTIConfigurationRevision_Type()
)
gs2328fSTPMSTIConfigurationRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTIConfigurationRevision.setStatus("current")
_Gs2328fSTPMSTIMappingConf_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTIMappingConf = _Gs2328fSTPMSTIMappingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4)
)


class _Gs2328fSTPMSTI1VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI1VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI1VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI1VLANsMapped_Object = MibScalar
gs2328fSTPMSTI1VLANsMapped = _Gs2328fSTPMSTI1VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 1),
    _Gs2328fSTPMSTI1VLANsMapped_Type()
)
gs2328fSTPMSTI1VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1VLANsMapped.setStatus("current")


class _Gs2328fSTPMSTI2VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI2VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI2VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI2VLANsMapped_Object = MibScalar
gs2328fSTPMSTI2VLANsMapped = _Gs2328fSTPMSTI2VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 2),
    _Gs2328fSTPMSTI2VLANsMapped_Type()
)
gs2328fSTPMSTI2VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2VLANsMapped.setStatus("current")


class _Gs2328fSTPMSTI3VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI3VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI3VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI3VLANsMapped_Object = MibScalar
gs2328fSTPMSTI3VLANsMapped = _Gs2328fSTPMSTI3VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 3),
    _Gs2328fSTPMSTI3VLANsMapped_Type()
)
gs2328fSTPMSTI3VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3VLANsMapped.setStatus("current")


class _Gs2328fSTPMSTI4VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI4VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI4VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI4VLANsMapped_Object = MibScalar
gs2328fSTPMSTI4VLANsMapped = _Gs2328fSTPMSTI4VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 4),
    _Gs2328fSTPMSTI4VLANsMapped_Type()
)
gs2328fSTPMSTI4VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4VLANsMapped.setStatus("current")


class _Gs2328fSTPMSTI5VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI5VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI5VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI5VLANsMapped_Object = MibScalar
gs2328fSTPMSTI5VLANsMapped = _Gs2328fSTPMSTI5VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 5),
    _Gs2328fSTPMSTI5VLANsMapped_Type()
)
gs2328fSTPMSTI5VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5VLANsMapped.setStatus("current")


class _Gs2328fSTPMSTI6VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI6VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI6VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI6VLANsMapped_Object = MibScalar
gs2328fSTPMSTI6VLANsMapped = _Gs2328fSTPMSTI6VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 6),
    _Gs2328fSTPMSTI6VLANsMapped_Type()
)
gs2328fSTPMSTI6VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6VLANsMapped.setStatus("current")


class _Gs2328fSTPMSTI7VLANsMapped_Type(DisplayString):
    """Custom type gs2328fSTPMSTI7VLANsMapped based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_Gs2328fSTPMSTI7VLANsMapped_Type.__name__ = "DisplayString"
_Gs2328fSTPMSTI7VLANsMapped_Object = MibScalar
gs2328fSTPMSTI7VLANsMapped = _Gs2328fSTPMSTI7VLANsMapped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 4, 7),
    _Gs2328fSTPMSTI7VLANsMapped_Type()
)
gs2328fSTPMSTI7VLANsMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7VLANsMapped.setStatus("current")
_Gs2328fSTPMSTIPriority_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTIPriority = _Gs2328fSTPMSTIPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5)
)


class _Gs2328fSTPCISTPriority_Type(Integer32):
    """Custom type gs2328fSTPCISTPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPCISTPriority_Type.__name__ = "Integer32"
_Gs2328fSTPCISTPriority_Object = MibScalar
gs2328fSTPCISTPriority = _Gs2328fSTPCISTPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 1),
    _Gs2328fSTPCISTPriority_Type()
)
gs2328fSTPCISTPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTPriority.setStatus("current")


class _Gs2328fSTPMSTI1Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI1Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI1Priority_Object = MibScalar
gs2328fSTPMSTI1Priority = _Gs2328fSTPMSTI1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 2),
    _Gs2328fSTPMSTI1Priority_Type()
)
gs2328fSTPMSTI1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1Priority.setStatus("current")


class _Gs2328fSTPMSTI2Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI2Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI2Priority_Object = MibScalar
gs2328fSTPMSTI2Priority = _Gs2328fSTPMSTI2Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 3),
    _Gs2328fSTPMSTI2Priority_Type()
)
gs2328fSTPMSTI2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2Priority.setStatus("current")


class _Gs2328fSTPMSTI3Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI3Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI3Priority_Object = MibScalar
gs2328fSTPMSTI3Priority = _Gs2328fSTPMSTI3Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 4),
    _Gs2328fSTPMSTI3Priority_Type()
)
gs2328fSTPMSTI3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3Priority.setStatus("current")


class _Gs2328fSTPMSTI4Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI4Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI4Priority_Object = MibScalar
gs2328fSTPMSTI4Priority = _Gs2328fSTPMSTI4Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 5),
    _Gs2328fSTPMSTI4Priority_Type()
)
gs2328fSTPMSTI4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4Priority.setStatus("current")


class _Gs2328fSTPMSTI5Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI5Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI5Priority_Object = MibScalar
gs2328fSTPMSTI5Priority = _Gs2328fSTPMSTI5Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 6),
    _Gs2328fSTPMSTI5Priority_Type()
)
gs2328fSTPMSTI5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5Priority.setStatus("current")


class _Gs2328fSTPMSTI6Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI6Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI6Priority_Object = MibScalar
gs2328fSTPMSTI6Priority = _Gs2328fSTPMSTI6Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 7),
    _Gs2328fSTPMSTI6Priority_Type()
)
gs2328fSTPMSTI6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6Priority.setStatus("current")


class _Gs2328fSTPMSTI7Priority_Type(Integer32):
    """Custom type gs2328fSTPMSTI7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2328fSTPMSTI7Priority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI7Priority_Object = MibScalar
gs2328fSTPMSTI7Priority = _Gs2328fSTPMSTI7Priority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 5, 8),
    _Gs2328fSTPMSTI7Priority_Type()
)
gs2328fSTPMSTI7Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7Priority.setStatus("current")
_Gs2328fSTPCISTPort_ObjectIdentity = ObjectIdentity
gs2328fSTPCISTPort = _Gs2328fSTPCISTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6)
)
_Gs2328fSTPCISTAggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPCISTAggregatedPort = _Gs2328fSTPCISTAggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1)
)


class _Gs2328fSTPCISTAggregatedPortSTPEnabled_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortSTPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTAggregatedPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortSTPEnabled_Object = MibScalar
gs2328fSTPCISTAggregatedPortSTPEnabled = _Gs2328fSTPCISTAggregatedPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 1),
    _Gs2328fSTPCISTAggregatedPortSTPEnabled_Type()
)
gs2328fSTPCISTAggregatedPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortSTPEnabled.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPCISTAggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortPathCost_Object = MibScalar
gs2328fSTPCISTAggregatedPortPathCost = _Gs2328fSTPCISTAggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 2),
    _Gs2328fSTPCISTAggregatedPortPathCost_Type()
)
gs2328fSTPCISTAggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPCISTAggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortPriority_Object = MibScalar
gs2328fSTPCISTAggregatedPortPriority = _Gs2328fSTPCISTAggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 3),
    _Gs2328fSTPCISTAggregatedPortPriority_Type()
)
gs2328fSTPCISTAggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortPriority.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortAdminEdge_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortAdminEdge based on Integer32"""
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


_Gs2328fSTPCISTAggregatedPortAdminEdge_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortAdminEdge_Object = MibScalar
gs2328fSTPCISTAggregatedPortAdminEdge = _Gs2328fSTPCISTAggregatedPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 4),
    _Gs2328fSTPCISTAggregatedPortAdminEdge_Type()
)
gs2328fSTPCISTAggregatedPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortAdminEdge.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortAutoEdge_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortAutoEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTAggregatedPortAutoEdge_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortAutoEdge_Object = MibScalar
gs2328fSTPCISTAggregatedPortAutoEdge = _Gs2328fSTPCISTAggregatedPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 5),
    _Gs2328fSTPCISTAggregatedPortAutoEdge_Type()
)
gs2328fSTPCISTAggregatedPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortAutoEdge.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortRestrictedRole_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortRestrictedRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTAggregatedPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortRestrictedRole_Object = MibScalar
gs2328fSTPCISTAggregatedPortRestrictedRole = _Gs2328fSTPCISTAggregatedPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 6),
    _Gs2328fSTPCISTAggregatedPortRestrictedRole_Type()
)
gs2328fSTPCISTAggregatedPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortRestrictedRole.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortRestrictedTCN_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortRestrictedTCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTAggregatedPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortRestrictedTCN_Object = MibScalar
gs2328fSTPCISTAggregatedPortRestrictedTCN = _Gs2328fSTPCISTAggregatedPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 7),
    _Gs2328fSTPCISTAggregatedPortRestrictedTCN_Type()
)
gs2328fSTPCISTAggregatedPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortRestrictedTCN.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortBPDUGuard_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortBPDUGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTAggregatedPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortBPDUGuard_Object = MibScalar
gs2328fSTPCISTAggregatedPortBPDUGuard = _Gs2328fSTPCISTAggregatedPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 8),
    _Gs2328fSTPCISTAggregatedPortBPDUGuard_Type()
)
gs2328fSTPCISTAggregatedPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortBPDUGuard.setStatus("current")


class _Gs2328fSTPCISTAggregatedPortPointtoPoint_Type(Integer32):
    """Custom type gs2328fSTPCISTAggregatedPortPointtoPoint based on Integer32"""
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


_Gs2328fSTPCISTAggregatedPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2328fSTPCISTAggregatedPortPointtoPoint_Object = MibScalar
gs2328fSTPCISTAggregatedPortPointtoPoint = _Gs2328fSTPCISTAggregatedPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 1, 9),
    _Gs2328fSTPCISTAggregatedPortPointtoPoint_Type()
)
gs2328fSTPCISTAggregatedPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTAggregatedPortPointtoPoint.setStatus("current")
_Gs2328fSTPCISTNormalPortTable_Object = MibTable
gs2328fSTPCISTNormalPortTable = _Gs2328fSTPCISTNormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortTable.setStatus("current")
_Gs2328fSTPCISTNormalPortEntry_Object = MibTableRow
gs2328fSTPCISTNormalPortEntry = _Gs2328fSTPCISTNormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1)
)
gs2328fSTPCISTNormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPCISTNormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortEntry.setStatus("current")


class _Gs2328fSTPCISTNormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPCISTNormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortConfPort_Object = MibTableColumn
gs2328fSTPCISTNormalPortConfPort = _Gs2328fSTPCISTNormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 1),
    _Gs2328fSTPCISTNormalPortConfPort_Type()
)
gs2328fSTPCISTNormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortConfPort.setStatus("current")


class _Gs2328fSTPCISTNormalPortSTPEnabled_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortSTPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTNormalPortSTPEnabled_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortSTPEnabled_Object = MibTableColumn
gs2328fSTPCISTNormalPortSTPEnabled = _Gs2328fSTPCISTNormalPortSTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 2),
    _Gs2328fSTPCISTNormalPortSTPEnabled_Type()
)
gs2328fSTPCISTNormalPortSTPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortSTPEnabled.setStatus("current")


class _Gs2328fSTPCISTNormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPCISTNormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortPathCost_Object = MibTableColumn
gs2328fSTPCISTNormalPortPathCost = _Gs2328fSTPCISTNormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 3),
    _Gs2328fSTPCISTNormalPortPathCost_Type()
)
gs2328fSTPCISTNormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortPathCost.setStatus("current")


class _Gs2328fSTPCISTNormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPCISTNormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortPriority_Object = MibTableColumn
gs2328fSTPCISTNormalPortPriority = _Gs2328fSTPCISTNormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 4),
    _Gs2328fSTPCISTNormalPortPriority_Type()
)
gs2328fSTPCISTNormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortPriority.setStatus("current")


class _Gs2328fSTPCISTNormalPortAdminEdge_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortAdminEdge based on Integer32"""
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


_Gs2328fSTPCISTNormalPortAdminEdge_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortAdminEdge_Object = MibTableColumn
gs2328fSTPCISTNormalPortAdminEdge = _Gs2328fSTPCISTNormalPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 5),
    _Gs2328fSTPCISTNormalPortAdminEdge_Type()
)
gs2328fSTPCISTNormalPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortAdminEdge.setStatus("current")


class _Gs2328fSTPCISTNormalPortAutoEdge_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortAutoEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTNormalPortAutoEdge_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortAutoEdge_Object = MibTableColumn
gs2328fSTPCISTNormalPortAutoEdge = _Gs2328fSTPCISTNormalPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 6),
    _Gs2328fSTPCISTNormalPortAutoEdge_Type()
)
gs2328fSTPCISTNormalPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortAutoEdge.setStatus("current")


class _Gs2328fSTPCISTNormalPortRestrictedRole_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortRestrictedRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTNormalPortRestrictedRole_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortRestrictedRole_Object = MibTableColumn
gs2328fSTPCISTNormalPortRestrictedRole = _Gs2328fSTPCISTNormalPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 7),
    _Gs2328fSTPCISTNormalPortRestrictedRole_Type()
)
gs2328fSTPCISTNormalPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortRestrictedRole.setStatus("current")


class _Gs2328fSTPCISTNormalPortRestrictedTCN_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortRestrictedTCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTNormalPortRestrictedTCN_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortRestrictedTCN_Object = MibTableColumn
gs2328fSTPCISTNormalPortRestrictedTCN = _Gs2328fSTPCISTNormalPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 8),
    _Gs2328fSTPCISTNormalPortRestrictedTCN_Type()
)
gs2328fSTPCISTNormalPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortRestrictedTCN.setStatus("current")


class _Gs2328fSTPCISTNormalPortBPDUGuard_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortBPDUGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSTPCISTNormalPortBPDUGuard_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortBPDUGuard_Object = MibTableColumn
gs2328fSTPCISTNormalPortBPDUGuard = _Gs2328fSTPCISTNormalPortBPDUGuard_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 9),
    _Gs2328fSTPCISTNormalPortBPDUGuard_Type()
)
gs2328fSTPCISTNormalPortBPDUGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortBPDUGuard.setStatus("current")


class _Gs2328fSTPCISTNormalPortPointtoPoint_Type(Integer32):
    """Custom type gs2328fSTPCISTNormalPortPointtoPoint based on Integer32"""
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


_Gs2328fSTPCISTNormalPortPointtoPoint_Type.__name__ = "Integer32"
_Gs2328fSTPCISTNormalPortPointtoPoint_Object = MibTableColumn
gs2328fSTPCISTNormalPortPointtoPoint = _Gs2328fSTPCISTNormalPortPointtoPoint_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 6, 2, 1, 10),
    _Gs2328fSTPCISTNormalPortPointtoPoint_Type()
)
gs2328fSTPCISTNormalPortPointtoPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPCISTNormalPortPointtoPoint.setStatus("current")
_Gs2328fSTPMSTIPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTIPort = _Gs2328fSTPMSTIPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7)
)
_Gs2328fSTPMSTI1Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI1Port = _Gs2328fSTPMSTI1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1)
)
_Gs2328fSTPMSTI1AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI1AggregatedPort = _Gs2328fSTPMSTI1AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 1)
)


class _Gs2328fSTPMSTI1AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI1AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI1AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI1AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI1AggregatedPortPathCost = _Gs2328fSTPMSTI1AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 1, 1),
    _Gs2328fSTPMSTI1AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI1AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI1AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI1AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI1AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI1AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI1AggregatedPortPriority = _Gs2328fSTPMSTI1AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 1, 2),
    _Gs2328fSTPMSTI1AggregatedPortPriority_Type()
)
gs2328fSTPMSTI1AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI1NormalPortTable_Object = MibTable
gs2328fSTPMSTI1NormalPortTable = _Gs2328fSTPMSTI1NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI1NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI1NormalPortEntry = _Gs2328fSTPMSTI1NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 2, 1)
)
gs2328fSTPMSTI1NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI1NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI1NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI1NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI1NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI1NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI1NormalPortConfPort = _Gs2328fSTPMSTI1NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 2, 1, 1),
    _Gs2328fSTPMSTI1NormalPortConfPort_Type()
)
gs2328fSTPMSTI1NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI1NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI1NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI1NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI1NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI1NormalPortPathCost = _Gs2328fSTPMSTI1NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 2, 1, 2),
    _Gs2328fSTPMSTI1NormalPortPathCost_Type()
)
gs2328fSTPMSTI1NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI1NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI1NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI1NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI1NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI1NormalPortPriority = _Gs2328fSTPMSTI1NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 1, 2, 1, 3),
    _Gs2328fSTPMSTI1NormalPortPriority_Type()
)
gs2328fSTPMSTI1NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI1NormalPortPriority.setStatus("current")
_Gs2328fSTPMSTI2Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI2Port = _Gs2328fSTPMSTI2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2)
)
_Gs2328fSTPMSTI2AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI2AggregatedPort = _Gs2328fSTPMSTI2AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 1)
)


class _Gs2328fSTPMSTI2AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI2AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI2AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI2AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI2AggregatedPortPathCost = _Gs2328fSTPMSTI2AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 1, 1),
    _Gs2328fSTPMSTI2AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI2AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI2AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI2AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI2AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI2AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI2AggregatedPortPriority = _Gs2328fSTPMSTI2AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 1, 2),
    _Gs2328fSTPMSTI2AggregatedPortPriority_Type()
)
gs2328fSTPMSTI2AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI2NormalPortTable_Object = MibTable
gs2328fSTPMSTI2NormalPortTable = _Gs2328fSTPMSTI2NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI2NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI2NormalPortEntry = _Gs2328fSTPMSTI2NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 2, 1)
)
gs2328fSTPMSTI2NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI2NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI2NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI2NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI2NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI2NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI2NormalPortConfPort = _Gs2328fSTPMSTI2NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 2, 1, 1),
    _Gs2328fSTPMSTI2NormalPortConfPort_Type()
)
gs2328fSTPMSTI2NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI2NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI2NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI2NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI2NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI2NormalPortPathCost = _Gs2328fSTPMSTI2NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 2, 1, 2),
    _Gs2328fSTPMSTI2NormalPortPathCost_Type()
)
gs2328fSTPMSTI2NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI2NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI2NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI2NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI2NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI2NormalPortPriority = _Gs2328fSTPMSTI2NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 2, 2, 1, 3),
    _Gs2328fSTPMSTI2NormalPortPriority_Type()
)
gs2328fSTPMSTI2NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI2NormalPortPriority.setStatus("current")
_Gs2328fSTPMSTI3Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI3Port = _Gs2328fSTPMSTI3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3)
)
_Gs2328fSTPMSTI3AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI3AggregatedPort = _Gs2328fSTPMSTI3AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 1)
)


class _Gs2328fSTPMSTI3AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI3AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI3AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI3AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI3AggregatedPortPathCost = _Gs2328fSTPMSTI3AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 1, 1),
    _Gs2328fSTPMSTI3AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI3AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI3AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI3AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI3AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI3AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI3AggregatedPortPriority = _Gs2328fSTPMSTI3AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 1, 2),
    _Gs2328fSTPMSTI3AggregatedPortPriority_Type()
)
gs2328fSTPMSTI3AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI3NormalPortTable_Object = MibTable
gs2328fSTPMSTI3NormalPortTable = _Gs2328fSTPMSTI3NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI3NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI3NormalPortEntry = _Gs2328fSTPMSTI3NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 2, 1)
)
gs2328fSTPMSTI3NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI3NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI3NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI3NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI3NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI3NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI3NormalPortConfPort = _Gs2328fSTPMSTI3NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 2, 1, 1),
    _Gs2328fSTPMSTI3NormalPortConfPort_Type()
)
gs2328fSTPMSTI3NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI3NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI3NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI3NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI3NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI3NormalPortPathCost = _Gs2328fSTPMSTI3NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 2, 1, 2),
    _Gs2328fSTPMSTI3NormalPortPathCost_Type()
)
gs2328fSTPMSTI3NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI3NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI3NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI3NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI3NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI3NormalPortPriority = _Gs2328fSTPMSTI3NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 3, 2, 1, 3),
    _Gs2328fSTPMSTI3NormalPortPriority_Type()
)
gs2328fSTPMSTI3NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI3NormalPortPriority.setStatus("current")
_Gs2328fSTPMSTI4Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI4Port = _Gs2328fSTPMSTI4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4)
)
_Gs2328fSTPMSTI4AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI4AggregatedPort = _Gs2328fSTPMSTI4AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 1)
)


class _Gs2328fSTPMSTI4AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI4AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI4AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI4AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI4AggregatedPortPathCost = _Gs2328fSTPMSTI4AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 1, 1),
    _Gs2328fSTPMSTI4AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI4AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI4AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI4AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI4AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI4AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI4AggregatedPortPriority = _Gs2328fSTPMSTI4AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 1, 2),
    _Gs2328fSTPMSTI4AggregatedPortPriority_Type()
)
gs2328fSTPMSTI4AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI4NormalPortTable_Object = MibTable
gs2328fSTPMSTI4NormalPortTable = _Gs2328fSTPMSTI4NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI4NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI4NormalPortEntry = _Gs2328fSTPMSTI4NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 2, 1)
)
gs2328fSTPMSTI4NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI4NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI4NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI4NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI4NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI4NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI4NormalPortConfPort = _Gs2328fSTPMSTI4NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 2, 1, 1),
    _Gs2328fSTPMSTI4NormalPortConfPort_Type()
)
gs2328fSTPMSTI4NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI4NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI4NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI4NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI4NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI4NormalPortPathCost = _Gs2328fSTPMSTI4NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 2, 1, 2),
    _Gs2328fSTPMSTI4NormalPortPathCost_Type()
)
gs2328fSTPMSTI4NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI4NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI4NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI4NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI4NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI4NormalPortPriority = _Gs2328fSTPMSTI4NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 4, 2, 1, 3),
    _Gs2328fSTPMSTI4NormalPortPriority_Type()
)
gs2328fSTPMSTI4NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI4NormalPortPriority.setStatus("current")
_Gs2328fSTPMSTI5Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI5Port = _Gs2328fSTPMSTI5Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5)
)
_Gs2328fSTPMSTI5AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI5AggregatedPort = _Gs2328fSTPMSTI5AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 1)
)


class _Gs2328fSTPMSTI5AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI5AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI5AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI5AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI5AggregatedPortPathCost = _Gs2328fSTPMSTI5AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 1, 1),
    _Gs2328fSTPMSTI5AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI5AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI5AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI5AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI5AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI5AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI5AggregatedPortPriority = _Gs2328fSTPMSTI5AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 1, 2),
    _Gs2328fSTPMSTI5AggregatedPortPriority_Type()
)
gs2328fSTPMSTI5AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI5NormalPortTable_Object = MibTable
gs2328fSTPMSTI5NormalPortTable = _Gs2328fSTPMSTI5NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI5NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI5NormalPortEntry = _Gs2328fSTPMSTI5NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 2, 1)
)
gs2328fSTPMSTI5NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI5NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI5NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI5NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI5NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI5NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI5NormalPortConfPort = _Gs2328fSTPMSTI5NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 2, 1, 1),
    _Gs2328fSTPMSTI5NormalPortConfPort_Type()
)
gs2328fSTPMSTI5NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI5NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI5NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI5NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI5NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI5NormalPortPathCost = _Gs2328fSTPMSTI5NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 2, 1, 2),
    _Gs2328fSTPMSTI5NormalPortPathCost_Type()
)
gs2328fSTPMSTI5NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI5NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI5NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI5NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI5NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI5NormalPortPriority = _Gs2328fSTPMSTI5NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 5, 2, 1, 3),
    _Gs2328fSTPMSTI5NormalPortPriority_Type()
)
gs2328fSTPMSTI5NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI5NormalPortPriority.setStatus("current")
_Gs2328fSTPMSTI6Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI6Port = _Gs2328fSTPMSTI6Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6)
)
_Gs2328fSTPMSTI6AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI6AggregatedPort = _Gs2328fSTPMSTI6AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 1)
)


class _Gs2328fSTPMSTI6AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI6AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI6AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI6AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI6AggregatedPortPathCost = _Gs2328fSTPMSTI6AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 1, 1),
    _Gs2328fSTPMSTI6AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI6AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI6AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI6AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI6AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI6AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI6AggregatedPortPriority = _Gs2328fSTPMSTI6AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 1, 2),
    _Gs2328fSTPMSTI6AggregatedPortPriority_Type()
)
gs2328fSTPMSTI6AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI6NormalPortTable_Object = MibTable
gs2328fSTPMSTI6NormalPortTable = _Gs2328fSTPMSTI6NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI6NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI6NormalPortEntry = _Gs2328fSTPMSTI6NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 2, 1)
)
gs2328fSTPMSTI6NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI6NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI6NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI6NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI6NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI6NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI6NormalPortConfPort = _Gs2328fSTPMSTI6NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 2, 1, 1),
    _Gs2328fSTPMSTI6NormalPortConfPort_Type()
)
gs2328fSTPMSTI6NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI6NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI6NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI6NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI6NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI6NormalPortPathCost = _Gs2328fSTPMSTI6NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 2, 1, 2),
    _Gs2328fSTPMSTI6NormalPortPathCost_Type()
)
gs2328fSTPMSTI6NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI6NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI6NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI6NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI6NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI6NormalPortPriority = _Gs2328fSTPMSTI6NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 6, 2, 1, 3),
    _Gs2328fSTPMSTI6NormalPortPriority_Type()
)
gs2328fSTPMSTI6NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI6NormalPortPriority.setStatus("current")
_Gs2328fSTPMSTI7Port_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI7Port = _Gs2328fSTPMSTI7Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7)
)
_Gs2328fSTPMSTI7AggregatedPort_ObjectIdentity = ObjectIdentity
gs2328fSTPMSTI7AggregatedPort = _Gs2328fSTPMSTI7AggregatedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 1)
)


class _Gs2328fSTPMSTI7AggregatedPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI7AggregatedPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI7AggregatedPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI7AggregatedPortPathCost_Object = MibScalar
gs2328fSTPMSTI7AggregatedPortPathCost = _Gs2328fSTPMSTI7AggregatedPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 1, 1),
    _Gs2328fSTPMSTI7AggregatedPortPathCost_Type()
)
gs2328fSTPMSTI7AggregatedPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7AggregatedPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI7AggregatedPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI7AggregatedPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI7AggregatedPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI7AggregatedPortPriority_Object = MibScalar
gs2328fSTPMSTI7AggregatedPortPriority = _Gs2328fSTPMSTI7AggregatedPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 1, 2),
    _Gs2328fSTPMSTI7AggregatedPortPriority_Type()
)
gs2328fSTPMSTI7AggregatedPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7AggregatedPortPriority.setStatus("current")
_Gs2328fSTPMSTI7NormalPortTable_Object = MibTable
gs2328fSTPMSTI7NormalPortTable = _Gs2328fSTPMSTI7NormalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7NormalPortTable.setStatus("current")
_Gs2328fSTPMSTI7NormalPortEntry_Object = MibTableRow
gs2328fSTPMSTI7NormalPortEntry = _Gs2328fSTPMSTI7NormalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 2, 1)
)
gs2328fSTPMSTI7NormalPortEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPMSTI7NormalPortConfPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7NormalPortEntry.setStatus("current")


class _Gs2328fSTPMSTI7NormalPortConfPort_Type(Integer32):
    """Custom type gs2328fSTPMSTI7NormalPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPMSTI7NormalPortConfPort_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI7NormalPortConfPort_Object = MibTableColumn
gs2328fSTPMSTI7NormalPortConfPort = _Gs2328fSTPMSTI7NormalPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 2, 1, 1),
    _Gs2328fSTPMSTI7NormalPortConfPort_Type()
)
gs2328fSTPMSTI7NormalPortConfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7NormalPortConfPort.setStatus("current")


class _Gs2328fSTPMSTI7NormalPortPathCost_Type(Integer32):
    """Custom type gs2328fSTPMSTI7NormalPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fSTPMSTI7NormalPortPathCost_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI7NormalPortPathCost_Object = MibTableColumn
gs2328fSTPMSTI7NormalPortPathCost = _Gs2328fSTPMSTI7NormalPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 2, 1, 2),
    _Gs2328fSTPMSTI7NormalPortPathCost_Type()
)
gs2328fSTPMSTI7NormalPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7NormalPortPathCost.setStatus("current")


class _Gs2328fSTPMSTI7NormalPortPriority_Type(Integer32):
    """Custom type gs2328fSTPMSTI7NormalPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Gs2328fSTPMSTI7NormalPortPriority_Type.__name__ = "Integer32"
_Gs2328fSTPMSTI7NormalPortPriority_Object = MibTableColumn
gs2328fSTPMSTI7NormalPortPriority = _Gs2328fSTPMSTI7NormalPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 7, 7, 2, 1, 3),
    _Gs2328fSTPMSTI7NormalPortPriority_Type()
)
gs2328fSTPMSTI7NormalPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSTPMSTI7NormalPortPriority.setStatus("current")
_Gs2328fSTPBridgeStatus_ObjectIdentity = ObjectIdentity
gs2328fSTPBridgeStatus = _Gs2328fSTPBridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8)
)
_Gs2328fCISTBridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fCISTBridgeSTP = _Gs2328fCISTBridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1)
)
_Gs2328fCISTBridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fCISTBridgeSTPStatus = _Gs2328fCISTBridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1)
)
_Gs2328fCISTBridgeInstance_Type = DisplayString
_Gs2328fCISTBridgeInstance_Object = MibScalar
gs2328fCISTBridgeInstance = _Gs2328fCISTBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 1),
    _Gs2328fCISTBridgeInstance_Type()
)
gs2328fCISTBridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTBridgeInstance.setStatus("current")
_Gs2328fCISTBridgeID_Type = DisplayString
_Gs2328fCISTBridgeID_Object = MibScalar
gs2328fCISTBridgeID = _Gs2328fCISTBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 2),
    _Gs2328fCISTBridgeID_Type()
)
gs2328fCISTBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTBridgeID.setStatus("current")
_Gs2328fCISTRootID_Type = DisplayString
_Gs2328fCISTRootID_Object = MibScalar
gs2328fCISTRootID = _Gs2328fCISTRootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 3),
    _Gs2328fCISTRootID_Type()
)
gs2328fCISTRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTRootID.setStatus("current")
_Gs2328fCISTRootPort_Type = DisplayString
_Gs2328fCISTRootPort_Object = MibScalar
gs2328fCISTRootPort = _Gs2328fCISTRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 4),
    _Gs2328fCISTRootPort_Type()
)
gs2328fCISTRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTRootPort.setStatus("current")


class _Gs2328fCISTRootCost_Type(Integer32):
    """Custom type gs2328fCISTRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fCISTRootCost_Type.__name__ = "Integer32"
_Gs2328fCISTRootCost_Object = MibScalar
gs2328fCISTRootCost = _Gs2328fCISTRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 5),
    _Gs2328fCISTRootCost_Type()
)
gs2328fCISTRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTRootCost.setStatus("current")
_Gs2328fCISTRegionalRoot_Type = DisplayString
_Gs2328fCISTRegionalRoot_Object = MibScalar
gs2328fCISTRegionalRoot = _Gs2328fCISTRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 6),
    _Gs2328fCISTRegionalRoot_Type()
)
gs2328fCISTRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTRegionalRoot.setStatus("current")


class _Gs2328fCISTInternalRootCost_Type(Integer32):
    """Custom type gs2328fCISTInternalRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fCISTInternalRootCost_Type.__name__ = "Integer32"
_Gs2328fCISTInternalRootCost_Object = MibScalar
gs2328fCISTInternalRootCost = _Gs2328fCISTInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 7),
    _Gs2328fCISTInternalRootCost_Type()
)
gs2328fCISTInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTInternalRootCost.setStatus("current")
_Gs2328fCISTTopologyFlag_Type = DisplayString
_Gs2328fCISTTopologyFlag_Object = MibScalar
gs2328fCISTTopologyFlag = _Gs2328fCISTTopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 8),
    _Gs2328fCISTTopologyFlag_Type()
)
gs2328fCISTTopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTTopologyFlag.setStatus("current")
_Gs2328fCISTTopologyChangeCount_Type = Counter32
_Gs2328fCISTTopologyChangeCount_Object = MibScalar
gs2328fCISTTopologyChangeCount = _Gs2328fCISTTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 9),
    _Gs2328fCISTTopologyChangeCount_Type()
)
gs2328fCISTTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTTopologyChangeCount.setStatus("current")
_Gs2328fCISTTopologyChangeLast_Type = DisplayString
_Gs2328fCISTTopologyChangeLast_Object = MibScalar
gs2328fCISTTopologyChangeLast = _Gs2328fCISTTopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 1, 10),
    _Gs2328fCISTTopologyChangeLast_Type()
)
gs2328fCISTTopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTTopologyChangeLast.setStatus("current")
_Gs2328fCISTPortStateTable_Object = MibTable
gs2328fCISTPortStateTable = _Gs2328fCISTPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fCISTPortStateTable.setStatus("current")
_Gs2328fCISTPortStateEntry_Object = MibTableRow
gs2328fCISTPortStateEntry = _Gs2328fCISTPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1)
)
gs2328fCISTPortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fCISTPortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fCISTPortStateEntry.setStatus("current")


class _Gs2328fCISTPortStateIndex_Type(Integer32):
    """Custom type gs2328fCISTPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fCISTPortStateIndex_Type.__name__ = "Integer32"
_Gs2328fCISTPortStateIndex_Object = MibTableColumn
gs2328fCISTPortStateIndex = _Gs2328fCISTPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 1),
    _Gs2328fCISTPortStateIndex_Type()
)
gs2328fCISTPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fCISTPortStateIndex.setStatus("current")
_Gs2328fCISTPortStatePort_Type = DisplayString
_Gs2328fCISTPortStatePort_Object = MibTableColumn
gs2328fCISTPortStatePort = _Gs2328fCISTPortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 2),
    _Gs2328fCISTPortStatePort_Type()
)
gs2328fCISTPortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStatePort.setStatus("current")
_Gs2328fCISTPortStatePortID_Type = DisplayString
_Gs2328fCISTPortStatePortID_Object = MibTableColumn
gs2328fCISTPortStatePortID = _Gs2328fCISTPortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 3),
    _Gs2328fCISTPortStatePortID_Type()
)
gs2328fCISTPortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStatePortID.setStatus("current")
_Gs2328fCISTPortStateRole_Type = DisplayString
_Gs2328fCISTPortStateRole_Object = MibTableColumn
gs2328fCISTPortStateRole = _Gs2328fCISTPortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 4),
    _Gs2328fCISTPortStateRole_Type()
)
gs2328fCISTPortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStateRole.setStatus("current")
_Gs2328fCISTPortStateState_Type = DisplayString
_Gs2328fCISTPortStateState_Object = MibTableColumn
gs2328fCISTPortStateState = _Gs2328fCISTPortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 5),
    _Gs2328fCISTPortStateState_Type()
)
gs2328fCISTPortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStateState.setStatus("current")


class _Gs2328fCISTPortStatePathCost_Type(Integer32):
    """Custom type gs2328fCISTPortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fCISTPortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fCISTPortStatePathCost_Object = MibTableColumn
gs2328fCISTPortStatePathCost = _Gs2328fCISTPortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 6),
    _Gs2328fCISTPortStatePathCost_Type()
)
gs2328fCISTPortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStatePathCost.setStatus("current")
_Gs2328fCISTPortStateEdge_Type = DisplayString
_Gs2328fCISTPortStateEdge_Object = MibTableColumn
gs2328fCISTPortStateEdge = _Gs2328fCISTPortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 7),
    _Gs2328fCISTPortStateEdge_Type()
)
gs2328fCISTPortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStateEdge.setStatus("current")
_Gs2328fCISTPortStatePoint2Point_Type = DisplayString
_Gs2328fCISTPortStatePoint2Point_Object = MibTableColumn
gs2328fCISTPortStatePoint2Point = _Gs2328fCISTPortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 8),
    _Gs2328fCISTPortStatePoint2Point_Type()
)
gs2328fCISTPortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStatePoint2Point.setStatus("current")
_Gs2328fCISTPortStateUptime_Type = DisplayString
_Gs2328fCISTPortStateUptime_Object = MibTableColumn
gs2328fCISTPortStateUptime = _Gs2328fCISTPortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 1, 2, 1, 9),
    _Gs2328fCISTPortStateUptime_Type()
)
gs2328fCISTPortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fCISTPortStateUptime.setStatus("current")
_Gs2328fMSTI1BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI1BridgeSTP = _Gs2328fMSTI1BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2)
)
_Gs2328fMSTI1BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI1BridgeSTPStatus = _Gs2328fMSTI1BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1)
)
_Gs2328fMSTI1BridgeInstance_Type = DisplayString
_Gs2328fMSTI1BridgeInstance_Object = MibScalar
gs2328fMSTI1BridgeInstance = _Gs2328fMSTI1BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 1),
    _Gs2328fMSTI1BridgeInstance_Type()
)
gs2328fMSTI1BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1BridgeInstance.setStatus("current")
_Gs2328fMSTI1BridgeID_Type = DisplayString
_Gs2328fMSTI1BridgeID_Object = MibScalar
gs2328fMSTI1BridgeID = _Gs2328fMSTI1BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 2),
    _Gs2328fMSTI1BridgeID_Type()
)
gs2328fMSTI1BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1BridgeID.setStatus("current")
_Gs2328fMSTI1RootID_Type = DisplayString
_Gs2328fMSTI1RootID_Object = MibScalar
gs2328fMSTI1RootID = _Gs2328fMSTI1RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 3),
    _Gs2328fMSTI1RootID_Type()
)
gs2328fMSTI1RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1RootID.setStatus("current")
_Gs2328fMSTI1RootPort_Type = DisplayString
_Gs2328fMSTI1RootPort_Object = MibScalar
gs2328fMSTI1RootPort = _Gs2328fMSTI1RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 4),
    _Gs2328fMSTI1RootPort_Type()
)
gs2328fMSTI1RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1RootPort.setStatus("current")


class _Gs2328fMSTI1RootCost_Type(Integer32):
    """Custom type gs2328fMSTI1RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI1RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI1RootCost_Object = MibScalar
gs2328fMSTI1RootCost = _Gs2328fMSTI1RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 5),
    _Gs2328fMSTI1RootCost_Type()
)
gs2328fMSTI1RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1RootCost.setStatus("current")
_Gs2328fMSTI1TopologyFlag_Type = DisplayString
_Gs2328fMSTI1TopologyFlag_Object = MibScalar
gs2328fMSTI1TopologyFlag = _Gs2328fMSTI1TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 8),
    _Gs2328fMSTI1TopologyFlag_Type()
)
gs2328fMSTI1TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1TopologyFlag.setStatus("current")
_Gs2328fMSTI1TopologyChangeCount_Type = Counter32
_Gs2328fMSTI1TopologyChangeCount_Object = MibScalar
gs2328fMSTI1TopologyChangeCount = _Gs2328fMSTI1TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 9),
    _Gs2328fMSTI1TopologyChangeCount_Type()
)
gs2328fMSTI1TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1TopologyChangeCount.setStatus("current")
_Gs2328fMSTI1TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI1TopologyChangeLast_Object = MibScalar
gs2328fMSTI1TopologyChangeLast = _Gs2328fMSTI1TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 1, 10),
    _Gs2328fMSTI1TopologyChangeLast_Type()
)
gs2328fMSTI1TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1TopologyChangeLast.setStatus("current")
_Gs2328fMSTI1PortStateTable_Object = MibTable
gs2328fMSTI1PortStateTable = _Gs2328fMSTI1PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateTable.setStatus("current")
_Gs2328fMSTI1PortStateEntry_Object = MibTableRow
gs2328fMSTI1PortStateEntry = _Gs2328fMSTI1PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1)
)
gs2328fMSTI1PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI1PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateEntry.setStatus("current")


class _Gs2328fMSTI1PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI1PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI1PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI1PortStateIndex_Object = MibTableColumn
gs2328fMSTI1PortStateIndex = _Gs2328fMSTI1PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 1),
    _Gs2328fMSTI1PortStateIndex_Type()
)
gs2328fMSTI1PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateIndex.setStatus("current")
_Gs2328fMSTI1PortStatePort_Type = DisplayString
_Gs2328fMSTI1PortStatePort_Object = MibTableColumn
gs2328fMSTI1PortStatePort = _Gs2328fMSTI1PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 2),
    _Gs2328fMSTI1PortStatePort_Type()
)
gs2328fMSTI1PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStatePort.setStatus("current")
_Gs2328fMSTI1PortStatePortID_Type = DisplayString
_Gs2328fMSTI1PortStatePortID_Object = MibTableColumn
gs2328fMSTI1PortStatePortID = _Gs2328fMSTI1PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 3),
    _Gs2328fMSTI1PortStatePortID_Type()
)
gs2328fMSTI1PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStatePortID.setStatus("current")
_Gs2328fMSTI1PortStateRole_Type = DisplayString
_Gs2328fMSTI1PortStateRole_Object = MibTableColumn
gs2328fMSTI1PortStateRole = _Gs2328fMSTI1PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 4),
    _Gs2328fMSTI1PortStateRole_Type()
)
gs2328fMSTI1PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateRole.setStatus("current")
_Gs2328fMSTI1PortStateState_Type = DisplayString
_Gs2328fMSTI1PortStateState_Object = MibTableColumn
gs2328fMSTI1PortStateState = _Gs2328fMSTI1PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 5),
    _Gs2328fMSTI1PortStateState_Type()
)
gs2328fMSTI1PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateState.setStatus("current")


class _Gs2328fMSTI1PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI1PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI1PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI1PortStatePathCost_Object = MibTableColumn
gs2328fMSTI1PortStatePathCost = _Gs2328fMSTI1PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 6),
    _Gs2328fMSTI1PortStatePathCost_Type()
)
gs2328fMSTI1PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStatePathCost.setStatus("current")
_Gs2328fMSTI1PortStateEdge_Type = DisplayString
_Gs2328fMSTI1PortStateEdge_Object = MibTableColumn
gs2328fMSTI1PortStateEdge = _Gs2328fMSTI1PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 7),
    _Gs2328fMSTI1PortStateEdge_Type()
)
gs2328fMSTI1PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateEdge.setStatus("current")
_Gs2328fMSTI1PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI1PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI1PortStatePoint2Point = _Gs2328fMSTI1PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 8),
    _Gs2328fMSTI1PortStatePoint2Point_Type()
)
gs2328fMSTI1PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI1PortStateUptime_Type = DisplayString
_Gs2328fMSTI1PortStateUptime_Object = MibTableColumn
gs2328fMSTI1PortStateUptime = _Gs2328fMSTI1PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 2, 2, 1, 9),
    _Gs2328fMSTI1PortStateUptime_Type()
)
gs2328fMSTI1PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI1PortStateUptime.setStatus("current")
_Gs2328fMSTI2BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI2BridgeSTP = _Gs2328fMSTI2BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3)
)
_Gs2328fMSTI2BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI2BridgeSTPStatus = _Gs2328fMSTI2BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1)
)
_Gs2328fMSTI2BridgeInstance_Type = DisplayString
_Gs2328fMSTI2BridgeInstance_Object = MibScalar
gs2328fMSTI2BridgeInstance = _Gs2328fMSTI2BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 1),
    _Gs2328fMSTI2BridgeInstance_Type()
)
gs2328fMSTI2BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2BridgeInstance.setStatus("current")
_Gs2328fMSTI2BridgeID_Type = DisplayString
_Gs2328fMSTI2BridgeID_Object = MibScalar
gs2328fMSTI2BridgeID = _Gs2328fMSTI2BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 2),
    _Gs2328fMSTI2BridgeID_Type()
)
gs2328fMSTI2BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2BridgeID.setStatus("current")
_Gs2328fMSTI2RootID_Type = DisplayString
_Gs2328fMSTI2RootID_Object = MibScalar
gs2328fMSTI2RootID = _Gs2328fMSTI2RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 3),
    _Gs2328fMSTI2RootID_Type()
)
gs2328fMSTI2RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2RootID.setStatus("current")
_Gs2328fMSTI2RootPort_Type = DisplayString
_Gs2328fMSTI2RootPort_Object = MibScalar
gs2328fMSTI2RootPort = _Gs2328fMSTI2RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 4),
    _Gs2328fMSTI2RootPort_Type()
)
gs2328fMSTI2RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2RootPort.setStatus("current")


class _Gs2328fMSTI2RootCost_Type(Integer32):
    """Custom type gs2328fMSTI2RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI2RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI2RootCost_Object = MibScalar
gs2328fMSTI2RootCost = _Gs2328fMSTI2RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 5),
    _Gs2328fMSTI2RootCost_Type()
)
gs2328fMSTI2RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2RootCost.setStatus("current")
_Gs2328fMSTI2TopologyFlag_Type = DisplayString
_Gs2328fMSTI2TopologyFlag_Object = MibScalar
gs2328fMSTI2TopologyFlag = _Gs2328fMSTI2TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 8),
    _Gs2328fMSTI2TopologyFlag_Type()
)
gs2328fMSTI2TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2TopologyFlag.setStatus("current")
_Gs2328fMSTI2TopologyChangeCount_Type = Counter32
_Gs2328fMSTI2TopologyChangeCount_Object = MibScalar
gs2328fMSTI2TopologyChangeCount = _Gs2328fMSTI2TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 9),
    _Gs2328fMSTI2TopologyChangeCount_Type()
)
gs2328fMSTI2TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2TopologyChangeCount.setStatus("current")
_Gs2328fMSTI2TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI2TopologyChangeLast_Object = MibScalar
gs2328fMSTI2TopologyChangeLast = _Gs2328fMSTI2TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 1, 10),
    _Gs2328fMSTI2TopologyChangeLast_Type()
)
gs2328fMSTI2TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2TopologyChangeLast.setStatus("current")
_Gs2328fMSTI2PortStateTable_Object = MibTable
gs2328fMSTI2PortStateTable = _Gs2328fMSTI2PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateTable.setStatus("current")
_Gs2328fMSTI2PortStateEntry_Object = MibTableRow
gs2328fMSTI2PortStateEntry = _Gs2328fMSTI2PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1)
)
gs2328fMSTI2PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI2PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateEntry.setStatus("current")


class _Gs2328fMSTI2PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI2PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI2PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI2PortStateIndex_Object = MibTableColumn
gs2328fMSTI2PortStateIndex = _Gs2328fMSTI2PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 1),
    _Gs2328fMSTI2PortStateIndex_Type()
)
gs2328fMSTI2PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateIndex.setStatus("current")
_Gs2328fMSTI2PortStatePort_Type = DisplayString
_Gs2328fMSTI2PortStatePort_Object = MibTableColumn
gs2328fMSTI2PortStatePort = _Gs2328fMSTI2PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 2),
    _Gs2328fMSTI2PortStatePort_Type()
)
gs2328fMSTI2PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStatePort.setStatus("current")
_Gs2328fMSTI2PortStatePortID_Type = DisplayString
_Gs2328fMSTI2PortStatePortID_Object = MibTableColumn
gs2328fMSTI2PortStatePortID = _Gs2328fMSTI2PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 3),
    _Gs2328fMSTI2PortStatePortID_Type()
)
gs2328fMSTI2PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStatePortID.setStatus("current")
_Gs2328fMSTI2PortStateRole_Type = DisplayString
_Gs2328fMSTI2PortStateRole_Object = MibTableColumn
gs2328fMSTI2PortStateRole = _Gs2328fMSTI2PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 4),
    _Gs2328fMSTI2PortStateRole_Type()
)
gs2328fMSTI2PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateRole.setStatus("current")
_Gs2328fMSTI2PortStateState_Type = DisplayString
_Gs2328fMSTI2PortStateState_Object = MibTableColumn
gs2328fMSTI2PortStateState = _Gs2328fMSTI2PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 5),
    _Gs2328fMSTI2PortStateState_Type()
)
gs2328fMSTI2PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateState.setStatus("current")


class _Gs2328fMSTI2PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI2PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI2PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI2PortStatePathCost_Object = MibTableColumn
gs2328fMSTI2PortStatePathCost = _Gs2328fMSTI2PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 6),
    _Gs2328fMSTI2PortStatePathCost_Type()
)
gs2328fMSTI2PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStatePathCost.setStatus("current")
_Gs2328fMSTI2PortStateEdge_Type = DisplayString
_Gs2328fMSTI2PortStateEdge_Object = MibTableColumn
gs2328fMSTI2PortStateEdge = _Gs2328fMSTI2PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 7),
    _Gs2328fMSTI2PortStateEdge_Type()
)
gs2328fMSTI2PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateEdge.setStatus("current")
_Gs2328fMSTI2PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI2PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI2PortStatePoint2Point = _Gs2328fMSTI2PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 8),
    _Gs2328fMSTI2PortStatePoint2Point_Type()
)
gs2328fMSTI2PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI2PortStateUptime_Type = DisplayString
_Gs2328fMSTI2PortStateUptime_Object = MibTableColumn
gs2328fMSTI2PortStateUptime = _Gs2328fMSTI2PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 3, 2, 1, 9),
    _Gs2328fMSTI2PortStateUptime_Type()
)
gs2328fMSTI2PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI2PortStateUptime.setStatus("current")
_Gs2328fMSTI3BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI3BridgeSTP = _Gs2328fMSTI3BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4)
)
_Gs2328fMSTI3BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI3BridgeSTPStatus = _Gs2328fMSTI3BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1)
)
_Gs2328fMSTI3BridgeInstance_Type = DisplayString
_Gs2328fMSTI3BridgeInstance_Object = MibScalar
gs2328fMSTI3BridgeInstance = _Gs2328fMSTI3BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 1),
    _Gs2328fMSTI3BridgeInstance_Type()
)
gs2328fMSTI3BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3BridgeInstance.setStatus("current")
_Gs2328fMSTI3BridgeID_Type = DisplayString
_Gs2328fMSTI3BridgeID_Object = MibScalar
gs2328fMSTI3BridgeID = _Gs2328fMSTI3BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 2),
    _Gs2328fMSTI3BridgeID_Type()
)
gs2328fMSTI3BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3BridgeID.setStatus("current")
_Gs2328fMSTI3RootID_Type = DisplayString
_Gs2328fMSTI3RootID_Object = MibScalar
gs2328fMSTI3RootID = _Gs2328fMSTI3RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 3),
    _Gs2328fMSTI3RootID_Type()
)
gs2328fMSTI3RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3RootID.setStatus("current")
_Gs2328fMSTI3RootPort_Type = DisplayString
_Gs2328fMSTI3RootPort_Object = MibScalar
gs2328fMSTI3RootPort = _Gs2328fMSTI3RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 4),
    _Gs2328fMSTI3RootPort_Type()
)
gs2328fMSTI3RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3RootPort.setStatus("current")


class _Gs2328fMSTI3RootCost_Type(Integer32):
    """Custom type gs2328fMSTI3RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI3RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI3RootCost_Object = MibScalar
gs2328fMSTI3RootCost = _Gs2328fMSTI3RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 5),
    _Gs2328fMSTI3RootCost_Type()
)
gs2328fMSTI3RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3RootCost.setStatus("current")
_Gs2328fMSTI3TopologyFlag_Type = DisplayString
_Gs2328fMSTI3TopologyFlag_Object = MibScalar
gs2328fMSTI3TopologyFlag = _Gs2328fMSTI3TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 8),
    _Gs2328fMSTI3TopologyFlag_Type()
)
gs2328fMSTI3TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3TopologyFlag.setStatus("current")
_Gs2328fMSTI3TopologyChangeCount_Type = Counter32
_Gs2328fMSTI3TopologyChangeCount_Object = MibScalar
gs2328fMSTI3TopologyChangeCount = _Gs2328fMSTI3TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 9),
    _Gs2328fMSTI3TopologyChangeCount_Type()
)
gs2328fMSTI3TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3TopologyChangeCount.setStatus("current")
_Gs2328fMSTI3TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI3TopologyChangeLast_Object = MibScalar
gs2328fMSTI3TopologyChangeLast = _Gs2328fMSTI3TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 1, 10),
    _Gs2328fMSTI3TopologyChangeLast_Type()
)
gs2328fMSTI3TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3TopologyChangeLast.setStatus("current")
_Gs2328fMSTI3PortStateTable_Object = MibTable
gs2328fMSTI3PortStateTable = _Gs2328fMSTI3PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateTable.setStatus("current")
_Gs2328fMSTI3PortStateEntry_Object = MibTableRow
gs2328fMSTI3PortStateEntry = _Gs2328fMSTI3PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1)
)
gs2328fMSTI3PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI3PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateEntry.setStatus("current")


class _Gs2328fMSTI3PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI3PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI3PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI3PortStateIndex_Object = MibTableColumn
gs2328fMSTI3PortStateIndex = _Gs2328fMSTI3PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 1),
    _Gs2328fMSTI3PortStateIndex_Type()
)
gs2328fMSTI3PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateIndex.setStatus("current")
_Gs2328fMSTI3PortStatePort_Type = DisplayString
_Gs2328fMSTI3PortStatePort_Object = MibTableColumn
gs2328fMSTI3PortStatePort = _Gs2328fMSTI3PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 2),
    _Gs2328fMSTI3PortStatePort_Type()
)
gs2328fMSTI3PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStatePort.setStatus("current")
_Gs2328fMSTI3PortStatePortID_Type = DisplayString
_Gs2328fMSTI3PortStatePortID_Object = MibTableColumn
gs2328fMSTI3PortStatePortID = _Gs2328fMSTI3PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 3),
    _Gs2328fMSTI3PortStatePortID_Type()
)
gs2328fMSTI3PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStatePortID.setStatus("current")
_Gs2328fMSTI3PortStateRole_Type = DisplayString
_Gs2328fMSTI3PortStateRole_Object = MibTableColumn
gs2328fMSTI3PortStateRole = _Gs2328fMSTI3PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 4),
    _Gs2328fMSTI3PortStateRole_Type()
)
gs2328fMSTI3PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateRole.setStatus("current")
_Gs2328fMSTI3PortStateState_Type = DisplayString
_Gs2328fMSTI3PortStateState_Object = MibTableColumn
gs2328fMSTI3PortStateState = _Gs2328fMSTI3PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 5),
    _Gs2328fMSTI3PortStateState_Type()
)
gs2328fMSTI3PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateState.setStatus("current")


class _Gs2328fMSTI3PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI3PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI3PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI3PortStatePathCost_Object = MibTableColumn
gs2328fMSTI3PortStatePathCost = _Gs2328fMSTI3PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 6),
    _Gs2328fMSTI3PortStatePathCost_Type()
)
gs2328fMSTI3PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStatePathCost.setStatus("current")
_Gs2328fMSTI3PortStateEdge_Type = DisplayString
_Gs2328fMSTI3PortStateEdge_Object = MibTableColumn
gs2328fMSTI3PortStateEdge = _Gs2328fMSTI3PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 7),
    _Gs2328fMSTI3PortStateEdge_Type()
)
gs2328fMSTI3PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateEdge.setStatus("current")
_Gs2328fMSTI3PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI3PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI3PortStatePoint2Point = _Gs2328fMSTI3PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 8),
    _Gs2328fMSTI3PortStatePoint2Point_Type()
)
gs2328fMSTI3PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI3PortStateUptime_Type = DisplayString
_Gs2328fMSTI3PortStateUptime_Object = MibTableColumn
gs2328fMSTI3PortStateUptime = _Gs2328fMSTI3PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 4, 2, 1, 9),
    _Gs2328fMSTI3PortStateUptime_Type()
)
gs2328fMSTI3PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI3PortStateUptime.setStatus("current")
_Gs2328fMSTI4BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI4BridgeSTP = _Gs2328fMSTI4BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5)
)
_Gs2328fMSTI4BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI4BridgeSTPStatus = _Gs2328fMSTI4BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1)
)
_Gs2328fMSTI4BridgeInstance_Type = DisplayString
_Gs2328fMSTI4BridgeInstance_Object = MibScalar
gs2328fMSTI4BridgeInstance = _Gs2328fMSTI4BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 1),
    _Gs2328fMSTI4BridgeInstance_Type()
)
gs2328fMSTI4BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4BridgeInstance.setStatus("current")
_Gs2328fMSTI4BridgeID_Type = DisplayString
_Gs2328fMSTI4BridgeID_Object = MibScalar
gs2328fMSTI4BridgeID = _Gs2328fMSTI4BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 2),
    _Gs2328fMSTI4BridgeID_Type()
)
gs2328fMSTI4BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4BridgeID.setStatus("current")
_Gs2328fMSTI4RootID_Type = DisplayString
_Gs2328fMSTI4RootID_Object = MibScalar
gs2328fMSTI4RootID = _Gs2328fMSTI4RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 3),
    _Gs2328fMSTI4RootID_Type()
)
gs2328fMSTI4RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4RootID.setStatus("current")
_Gs2328fMSTI4RootPort_Type = DisplayString
_Gs2328fMSTI4RootPort_Object = MibScalar
gs2328fMSTI4RootPort = _Gs2328fMSTI4RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 4),
    _Gs2328fMSTI4RootPort_Type()
)
gs2328fMSTI4RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4RootPort.setStatus("current")


class _Gs2328fMSTI4RootCost_Type(Integer32):
    """Custom type gs2328fMSTI4RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI4RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI4RootCost_Object = MibScalar
gs2328fMSTI4RootCost = _Gs2328fMSTI4RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 5),
    _Gs2328fMSTI4RootCost_Type()
)
gs2328fMSTI4RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4RootCost.setStatus("current")
_Gs2328fMSTI4TopologyFlag_Type = DisplayString
_Gs2328fMSTI4TopologyFlag_Object = MibScalar
gs2328fMSTI4TopologyFlag = _Gs2328fMSTI4TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 8),
    _Gs2328fMSTI4TopologyFlag_Type()
)
gs2328fMSTI4TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4TopologyFlag.setStatus("current")
_Gs2328fMSTI4TopologyChangeCount_Type = Counter32
_Gs2328fMSTI4TopologyChangeCount_Object = MibScalar
gs2328fMSTI4TopologyChangeCount = _Gs2328fMSTI4TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 9),
    _Gs2328fMSTI4TopologyChangeCount_Type()
)
gs2328fMSTI4TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4TopologyChangeCount.setStatus("current")
_Gs2328fMSTI4TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI4TopologyChangeLast_Object = MibScalar
gs2328fMSTI4TopologyChangeLast = _Gs2328fMSTI4TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 1, 10),
    _Gs2328fMSTI4TopologyChangeLast_Type()
)
gs2328fMSTI4TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4TopologyChangeLast.setStatus("current")
_Gs2328fMSTI4PortStateTable_Object = MibTable
gs2328fMSTI4PortStateTable = _Gs2328fMSTI4PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateTable.setStatus("current")
_Gs2328fMSTI4PortStateEntry_Object = MibTableRow
gs2328fMSTI4PortStateEntry = _Gs2328fMSTI4PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1)
)
gs2328fMSTI4PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI4PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateEntry.setStatus("current")


class _Gs2328fMSTI4PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI4PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI4PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI4PortStateIndex_Object = MibTableColumn
gs2328fMSTI4PortStateIndex = _Gs2328fMSTI4PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 1),
    _Gs2328fMSTI4PortStateIndex_Type()
)
gs2328fMSTI4PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateIndex.setStatus("current")
_Gs2328fMSTI4PortStatePort_Type = DisplayString
_Gs2328fMSTI4PortStatePort_Object = MibTableColumn
gs2328fMSTI4PortStatePort = _Gs2328fMSTI4PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 2),
    _Gs2328fMSTI4PortStatePort_Type()
)
gs2328fMSTI4PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStatePort.setStatus("current")
_Gs2328fMSTI4PortStatePortID_Type = DisplayString
_Gs2328fMSTI4PortStatePortID_Object = MibTableColumn
gs2328fMSTI4PortStatePortID = _Gs2328fMSTI4PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 3),
    _Gs2328fMSTI4PortStatePortID_Type()
)
gs2328fMSTI4PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStatePortID.setStatus("current")
_Gs2328fMSTI4PortStateRole_Type = DisplayString
_Gs2328fMSTI4PortStateRole_Object = MibTableColumn
gs2328fMSTI4PortStateRole = _Gs2328fMSTI4PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 4),
    _Gs2328fMSTI4PortStateRole_Type()
)
gs2328fMSTI4PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateRole.setStatus("current")
_Gs2328fMSTI4PortStateState_Type = DisplayString
_Gs2328fMSTI4PortStateState_Object = MibTableColumn
gs2328fMSTI4PortStateState = _Gs2328fMSTI4PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 5),
    _Gs2328fMSTI4PortStateState_Type()
)
gs2328fMSTI4PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateState.setStatus("current")


class _Gs2328fMSTI4PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI4PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI4PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI4PortStatePathCost_Object = MibTableColumn
gs2328fMSTI4PortStatePathCost = _Gs2328fMSTI4PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 6),
    _Gs2328fMSTI4PortStatePathCost_Type()
)
gs2328fMSTI4PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStatePathCost.setStatus("current")
_Gs2328fMSTI4PortStateEdge_Type = DisplayString
_Gs2328fMSTI4PortStateEdge_Object = MibTableColumn
gs2328fMSTI4PortStateEdge = _Gs2328fMSTI4PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 7),
    _Gs2328fMSTI4PortStateEdge_Type()
)
gs2328fMSTI4PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateEdge.setStatus("current")
_Gs2328fMSTI4PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI4PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI4PortStatePoint2Point = _Gs2328fMSTI4PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 8),
    _Gs2328fMSTI4PortStatePoint2Point_Type()
)
gs2328fMSTI4PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI4PortStateUptime_Type = DisplayString
_Gs2328fMSTI4PortStateUptime_Object = MibTableColumn
gs2328fMSTI4PortStateUptime = _Gs2328fMSTI4PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 5, 2, 1, 9),
    _Gs2328fMSTI4PortStateUptime_Type()
)
gs2328fMSTI4PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI4PortStateUptime.setStatus("current")
_Gs2328fMSTI5BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI5BridgeSTP = _Gs2328fMSTI5BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6)
)
_Gs2328fMSTI5BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI5BridgeSTPStatus = _Gs2328fMSTI5BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1)
)
_Gs2328fMSTI5BridgeInstance_Type = DisplayString
_Gs2328fMSTI5BridgeInstance_Object = MibScalar
gs2328fMSTI5BridgeInstance = _Gs2328fMSTI5BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 1),
    _Gs2328fMSTI5BridgeInstance_Type()
)
gs2328fMSTI5BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5BridgeInstance.setStatus("current")
_Gs2328fMSTI5BridgeID_Type = DisplayString
_Gs2328fMSTI5BridgeID_Object = MibScalar
gs2328fMSTI5BridgeID = _Gs2328fMSTI5BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 2),
    _Gs2328fMSTI5BridgeID_Type()
)
gs2328fMSTI5BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5BridgeID.setStatus("current")
_Gs2328fMSTI5RootID_Type = DisplayString
_Gs2328fMSTI5RootID_Object = MibScalar
gs2328fMSTI5RootID = _Gs2328fMSTI5RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 3),
    _Gs2328fMSTI5RootID_Type()
)
gs2328fMSTI5RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5RootID.setStatus("current")
_Gs2328fMSTI5RootPort_Type = DisplayString
_Gs2328fMSTI5RootPort_Object = MibScalar
gs2328fMSTI5RootPort = _Gs2328fMSTI5RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 4),
    _Gs2328fMSTI5RootPort_Type()
)
gs2328fMSTI5RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5RootPort.setStatus("current")


class _Gs2328fMSTI5RootCost_Type(Integer32):
    """Custom type gs2328fMSTI5RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI5RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI5RootCost_Object = MibScalar
gs2328fMSTI5RootCost = _Gs2328fMSTI5RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 5),
    _Gs2328fMSTI5RootCost_Type()
)
gs2328fMSTI5RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5RootCost.setStatus("current")
_Gs2328fMSTI5TopologyFlag_Type = DisplayString
_Gs2328fMSTI5TopologyFlag_Object = MibScalar
gs2328fMSTI5TopologyFlag = _Gs2328fMSTI5TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 8),
    _Gs2328fMSTI5TopologyFlag_Type()
)
gs2328fMSTI5TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5TopologyFlag.setStatus("current")
_Gs2328fMSTI5TopologyChangeCount_Type = Counter32
_Gs2328fMSTI5TopologyChangeCount_Object = MibScalar
gs2328fMSTI5TopologyChangeCount = _Gs2328fMSTI5TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 9),
    _Gs2328fMSTI5TopologyChangeCount_Type()
)
gs2328fMSTI5TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5TopologyChangeCount.setStatus("current")
_Gs2328fMSTI5TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI5TopologyChangeLast_Object = MibScalar
gs2328fMSTI5TopologyChangeLast = _Gs2328fMSTI5TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 1, 10),
    _Gs2328fMSTI5TopologyChangeLast_Type()
)
gs2328fMSTI5TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5TopologyChangeLast.setStatus("current")
_Gs2328fMSTI5PortStateTable_Object = MibTable
gs2328fMSTI5PortStateTable = _Gs2328fMSTI5PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateTable.setStatus("current")
_Gs2328fMSTI5PortStateEntry_Object = MibTableRow
gs2328fMSTI5PortStateEntry = _Gs2328fMSTI5PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1)
)
gs2328fMSTI5PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI5PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateEntry.setStatus("current")


class _Gs2328fMSTI5PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI5PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI5PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI5PortStateIndex_Object = MibTableColumn
gs2328fMSTI5PortStateIndex = _Gs2328fMSTI5PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 1),
    _Gs2328fMSTI5PortStateIndex_Type()
)
gs2328fMSTI5PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateIndex.setStatus("current")
_Gs2328fMSTI5PortStatePort_Type = DisplayString
_Gs2328fMSTI5PortStatePort_Object = MibTableColumn
gs2328fMSTI5PortStatePort = _Gs2328fMSTI5PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 2),
    _Gs2328fMSTI5PortStatePort_Type()
)
gs2328fMSTI5PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStatePort.setStatus("current")
_Gs2328fMSTI5PortStatePortID_Type = DisplayString
_Gs2328fMSTI5PortStatePortID_Object = MibTableColumn
gs2328fMSTI5PortStatePortID = _Gs2328fMSTI5PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 3),
    _Gs2328fMSTI5PortStatePortID_Type()
)
gs2328fMSTI5PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStatePortID.setStatus("current")
_Gs2328fMSTI5PortStateRole_Type = DisplayString
_Gs2328fMSTI5PortStateRole_Object = MibTableColumn
gs2328fMSTI5PortStateRole = _Gs2328fMSTI5PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 4),
    _Gs2328fMSTI5PortStateRole_Type()
)
gs2328fMSTI5PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateRole.setStatus("current")
_Gs2328fMSTI5PortStateState_Type = DisplayString
_Gs2328fMSTI5PortStateState_Object = MibTableColumn
gs2328fMSTI5PortStateState = _Gs2328fMSTI5PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 5),
    _Gs2328fMSTI5PortStateState_Type()
)
gs2328fMSTI5PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateState.setStatus("current")


class _Gs2328fMSTI5PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI5PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI5PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI5PortStatePathCost_Object = MibTableColumn
gs2328fMSTI5PortStatePathCost = _Gs2328fMSTI5PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 6),
    _Gs2328fMSTI5PortStatePathCost_Type()
)
gs2328fMSTI5PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStatePathCost.setStatus("current")
_Gs2328fMSTI5PortStateEdge_Type = DisplayString
_Gs2328fMSTI5PortStateEdge_Object = MibTableColumn
gs2328fMSTI5PortStateEdge = _Gs2328fMSTI5PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 7),
    _Gs2328fMSTI5PortStateEdge_Type()
)
gs2328fMSTI5PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateEdge.setStatus("current")
_Gs2328fMSTI5PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI5PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI5PortStatePoint2Point = _Gs2328fMSTI5PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 8),
    _Gs2328fMSTI5PortStatePoint2Point_Type()
)
gs2328fMSTI5PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI5PortStateUptime_Type = DisplayString
_Gs2328fMSTI5PortStateUptime_Object = MibTableColumn
gs2328fMSTI5PortStateUptime = _Gs2328fMSTI5PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 6, 2, 1, 9),
    _Gs2328fMSTI5PortStateUptime_Type()
)
gs2328fMSTI5PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI5PortStateUptime.setStatus("current")
_Gs2328fMSTI6BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI6BridgeSTP = _Gs2328fMSTI6BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7)
)
_Gs2328fMSTI6BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI6BridgeSTPStatus = _Gs2328fMSTI6BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1)
)
_Gs2328fMSTI6BridgeInstance_Type = DisplayString
_Gs2328fMSTI6BridgeInstance_Object = MibScalar
gs2328fMSTI6BridgeInstance = _Gs2328fMSTI6BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 1),
    _Gs2328fMSTI6BridgeInstance_Type()
)
gs2328fMSTI6BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6BridgeInstance.setStatus("current")
_Gs2328fMSTI6BridgeID_Type = DisplayString
_Gs2328fMSTI6BridgeID_Object = MibScalar
gs2328fMSTI6BridgeID = _Gs2328fMSTI6BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 2),
    _Gs2328fMSTI6BridgeID_Type()
)
gs2328fMSTI6BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6BridgeID.setStatus("current")
_Gs2328fMSTI6RootID_Type = DisplayString
_Gs2328fMSTI6RootID_Object = MibScalar
gs2328fMSTI6RootID = _Gs2328fMSTI6RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 3),
    _Gs2328fMSTI6RootID_Type()
)
gs2328fMSTI6RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6RootID.setStatus("current")
_Gs2328fMSTI6RootPort_Type = DisplayString
_Gs2328fMSTI6RootPort_Object = MibScalar
gs2328fMSTI6RootPort = _Gs2328fMSTI6RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 4),
    _Gs2328fMSTI6RootPort_Type()
)
gs2328fMSTI6RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6RootPort.setStatus("current")


class _Gs2328fMSTI6RootCost_Type(Integer32):
    """Custom type gs2328fMSTI6RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI6RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI6RootCost_Object = MibScalar
gs2328fMSTI6RootCost = _Gs2328fMSTI6RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 5),
    _Gs2328fMSTI6RootCost_Type()
)
gs2328fMSTI6RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6RootCost.setStatus("current")
_Gs2328fMSTI6TopologyFlag_Type = DisplayString
_Gs2328fMSTI6TopologyFlag_Object = MibScalar
gs2328fMSTI6TopologyFlag = _Gs2328fMSTI6TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 8),
    _Gs2328fMSTI6TopologyFlag_Type()
)
gs2328fMSTI6TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6TopologyFlag.setStatus("current")
_Gs2328fMSTI6TopologyChangeCount_Type = Counter32
_Gs2328fMSTI6TopologyChangeCount_Object = MibScalar
gs2328fMSTI6TopologyChangeCount = _Gs2328fMSTI6TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 9),
    _Gs2328fMSTI6TopologyChangeCount_Type()
)
gs2328fMSTI6TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6TopologyChangeCount.setStatus("current")
_Gs2328fMSTI6TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI6TopologyChangeLast_Object = MibScalar
gs2328fMSTI6TopologyChangeLast = _Gs2328fMSTI6TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 1, 10),
    _Gs2328fMSTI6TopologyChangeLast_Type()
)
gs2328fMSTI6TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6TopologyChangeLast.setStatus("current")
_Gs2328fMSTI6PortStateTable_Object = MibTable
gs2328fMSTI6PortStateTable = _Gs2328fMSTI6PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateTable.setStatus("current")
_Gs2328fMSTI6PortStateEntry_Object = MibTableRow
gs2328fMSTI6PortStateEntry = _Gs2328fMSTI6PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1)
)
gs2328fMSTI6PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI6PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateEntry.setStatus("current")


class _Gs2328fMSTI6PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI6PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI6PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI6PortStateIndex_Object = MibTableColumn
gs2328fMSTI6PortStateIndex = _Gs2328fMSTI6PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 1),
    _Gs2328fMSTI6PortStateIndex_Type()
)
gs2328fMSTI6PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateIndex.setStatus("current")
_Gs2328fMSTI6PortStatePort_Type = DisplayString
_Gs2328fMSTI6PortStatePort_Object = MibTableColumn
gs2328fMSTI6PortStatePort = _Gs2328fMSTI6PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 2),
    _Gs2328fMSTI6PortStatePort_Type()
)
gs2328fMSTI6PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStatePort.setStatus("current")
_Gs2328fMSTI6PortStatePortID_Type = DisplayString
_Gs2328fMSTI6PortStatePortID_Object = MibTableColumn
gs2328fMSTI6PortStatePortID = _Gs2328fMSTI6PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 3),
    _Gs2328fMSTI6PortStatePortID_Type()
)
gs2328fMSTI6PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStatePortID.setStatus("current")
_Gs2328fMSTI6PortStateRole_Type = DisplayString
_Gs2328fMSTI6PortStateRole_Object = MibTableColumn
gs2328fMSTI6PortStateRole = _Gs2328fMSTI6PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 4),
    _Gs2328fMSTI6PortStateRole_Type()
)
gs2328fMSTI6PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateRole.setStatus("current")
_Gs2328fMSTI6PortStateState_Type = DisplayString
_Gs2328fMSTI6PortStateState_Object = MibTableColumn
gs2328fMSTI6PortStateState = _Gs2328fMSTI6PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 5),
    _Gs2328fMSTI6PortStateState_Type()
)
gs2328fMSTI6PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateState.setStatus("current")


class _Gs2328fMSTI6PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI6PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI6PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI6PortStatePathCost_Object = MibTableColumn
gs2328fMSTI6PortStatePathCost = _Gs2328fMSTI6PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 6),
    _Gs2328fMSTI6PortStatePathCost_Type()
)
gs2328fMSTI6PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStatePathCost.setStatus("current")
_Gs2328fMSTI6PortStateEdge_Type = DisplayString
_Gs2328fMSTI6PortStateEdge_Object = MibTableColumn
gs2328fMSTI6PortStateEdge = _Gs2328fMSTI6PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 7),
    _Gs2328fMSTI6PortStateEdge_Type()
)
gs2328fMSTI6PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateEdge.setStatus("current")
_Gs2328fMSTI6PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI6PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI6PortStatePoint2Point = _Gs2328fMSTI6PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 8),
    _Gs2328fMSTI6PortStatePoint2Point_Type()
)
gs2328fMSTI6PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI6PortStateUptime_Type = DisplayString
_Gs2328fMSTI6PortStateUptime_Object = MibTableColumn
gs2328fMSTI6PortStateUptime = _Gs2328fMSTI6PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 7, 2, 1, 9),
    _Gs2328fMSTI6PortStateUptime_Type()
)
gs2328fMSTI6PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI6PortStateUptime.setStatus("current")
_Gs2328fMSTI7BridgeSTP_ObjectIdentity = ObjectIdentity
gs2328fMSTI7BridgeSTP = _Gs2328fMSTI7BridgeSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8)
)
_Gs2328fMSTI7BridgeSTPStatus_ObjectIdentity = ObjectIdentity
gs2328fMSTI7BridgeSTPStatus = _Gs2328fMSTI7BridgeSTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1)
)
_Gs2328fMSTI7BridgeInstance_Type = DisplayString
_Gs2328fMSTI7BridgeInstance_Object = MibScalar
gs2328fMSTI7BridgeInstance = _Gs2328fMSTI7BridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 1),
    _Gs2328fMSTI7BridgeInstance_Type()
)
gs2328fMSTI7BridgeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7BridgeInstance.setStatus("current")
_Gs2328fMSTI7BridgeID_Type = DisplayString
_Gs2328fMSTI7BridgeID_Object = MibScalar
gs2328fMSTI7BridgeID = _Gs2328fMSTI7BridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 2),
    _Gs2328fMSTI7BridgeID_Type()
)
gs2328fMSTI7BridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7BridgeID.setStatus("current")
_Gs2328fMSTI7RootID_Type = DisplayString
_Gs2328fMSTI7RootID_Object = MibScalar
gs2328fMSTI7RootID = _Gs2328fMSTI7RootID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 3),
    _Gs2328fMSTI7RootID_Type()
)
gs2328fMSTI7RootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7RootID.setStatus("current")
_Gs2328fMSTI7RootPort_Type = DisplayString
_Gs2328fMSTI7RootPort_Object = MibScalar
gs2328fMSTI7RootPort = _Gs2328fMSTI7RootPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 4),
    _Gs2328fMSTI7RootPort_Type()
)
gs2328fMSTI7RootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7RootPort.setStatus("current")


class _Gs2328fMSTI7RootCost_Type(Integer32):
    """Custom type gs2328fMSTI7RootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI7RootCost_Type.__name__ = "Integer32"
_Gs2328fMSTI7RootCost_Object = MibScalar
gs2328fMSTI7RootCost = _Gs2328fMSTI7RootCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 5),
    _Gs2328fMSTI7RootCost_Type()
)
gs2328fMSTI7RootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7RootCost.setStatus("current")
_Gs2328fMSTI7TopologyFlag_Type = DisplayString
_Gs2328fMSTI7TopologyFlag_Object = MibScalar
gs2328fMSTI7TopologyFlag = _Gs2328fMSTI7TopologyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 8),
    _Gs2328fMSTI7TopologyFlag_Type()
)
gs2328fMSTI7TopologyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7TopologyFlag.setStatus("current")
_Gs2328fMSTI7TopologyChangeCount_Type = Counter32
_Gs2328fMSTI7TopologyChangeCount_Object = MibScalar
gs2328fMSTI7TopologyChangeCount = _Gs2328fMSTI7TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 9),
    _Gs2328fMSTI7TopologyChangeCount_Type()
)
gs2328fMSTI7TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7TopologyChangeCount.setStatus("current")
_Gs2328fMSTI7TopologyChangeLast_Type = DisplayString
_Gs2328fMSTI7TopologyChangeLast_Object = MibScalar
gs2328fMSTI7TopologyChangeLast = _Gs2328fMSTI7TopologyChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 1, 10),
    _Gs2328fMSTI7TopologyChangeLast_Type()
)
gs2328fMSTI7TopologyChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7TopologyChangeLast.setStatus("current")
_Gs2328fMSTI7PortStateTable_Object = MibTable
gs2328fMSTI7PortStateTable = _Gs2328fMSTI7PortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2)
)
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateTable.setStatus("current")
_Gs2328fMSTI7PortStateEntry_Object = MibTableRow
gs2328fMSTI7PortStateEntry = _Gs2328fMSTI7PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1)
)
gs2328fMSTI7PortStateEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fMSTI7PortStateIndex"),
)
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateEntry.setStatus("current")


class _Gs2328fMSTI7PortStateIndex_Type(Integer32):
    """Custom type gs2328fMSTI7PortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fMSTI7PortStateIndex_Type.__name__ = "Integer32"
_Gs2328fMSTI7PortStateIndex_Object = MibTableColumn
gs2328fMSTI7PortStateIndex = _Gs2328fMSTI7PortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 1),
    _Gs2328fMSTI7PortStateIndex_Type()
)
gs2328fMSTI7PortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateIndex.setStatus("current")
_Gs2328fMSTI7PortStatePort_Type = DisplayString
_Gs2328fMSTI7PortStatePort_Object = MibTableColumn
gs2328fMSTI7PortStatePort = _Gs2328fMSTI7PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 2),
    _Gs2328fMSTI7PortStatePort_Type()
)
gs2328fMSTI7PortStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStatePort.setStatus("current")
_Gs2328fMSTI7PortStatePortID_Type = DisplayString
_Gs2328fMSTI7PortStatePortID_Object = MibTableColumn
gs2328fMSTI7PortStatePortID = _Gs2328fMSTI7PortStatePortID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 3),
    _Gs2328fMSTI7PortStatePortID_Type()
)
gs2328fMSTI7PortStatePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStatePortID.setStatus("current")
_Gs2328fMSTI7PortStateRole_Type = DisplayString
_Gs2328fMSTI7PortStateRole_Object = MibTableColumn
gs2328fMSTI7PortStateRole = _Gs2328fMSTI7PortStateRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 4),
    _Gs2328fMSTI7PortStateRole_Type()
)
gs2328fMSTI7PortStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateRole.setStatus("current")
_Gs2328fMSTI7PortStateState_Type = DisplayString
_Gs2328fMSTI7PortStateState_Object = MibTableColumn
gs2328fMSTI7PortStateState = _Gs2328fMSTI7PortStateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 5),
    _Gs2328fMSTI7PortStateState_Type()
)
gs2328fMSTI7PortStateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateState.setStatus("current")


class _Gs2328fMSTI7PortStatePathCost_Type(Integer32):
    """Custom type gs2328fMSTI7PortStatePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Gs2328fMSTI7PortStatePathCost_Type.__name__ = "Integer32"
_Gs2328fMSTI7PortStatePathCost_Object = MibTableColumn
gs2328fMSTI7PortStatePathCost = _Gs2328fMSTI7PortStatePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 6),
    _Gs2328fMSTI7PortStatePathCost_Type()
)
gs2328fMSTI7PortStatePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStatePathCost.setStatus("current")
_Gs2328fMSTI7PortStateEdge_Type = DisplayString
_Gs2328fMSTI7PortStateEdge_Object = MibTableColumn
gs2328fMSTI7PortStateEdge = _Gs2328fMSTI7PortStateEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 7),
    _Gs2328fMSTI7PortStateEdge_Type()
)
gs2328fMSTI7PortStateEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateEdge.setStatus("current")
_Gs2328fMSTI7PortStatePoint2Point_Type = DisplayString
_Gs2328fMSTI7PortStatePoint2Point_Object = MibTableColumn
gs2328fMSTI7PortStatePoint2Point = _Gs2328fMSTI7PortStatePoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 8),
    _Gs2328fMSTI7PortStatePoint2Point_Type()
)
gs2328fMSTI7PortStatePoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStatePoint2Point.setStatus("current")
_Gs2328fMSTI7PortStateUptime_Type = DisplayString
_Gs2328fMSTI7PortStateUptime_Object = MibTableColumn
gs2328fMSTI7PortStateUptime = _Gs2328fMSTI7PortStateUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 8, 8, 2, 1, 9),
    _Gs2328fMSTI7PortStateUptime_Type()
)
gs2328fMSTI7PortStateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fMSTI7PortStateUptime.setStatus("current")
_Gs2328fSTPPortStatusTable_Object = MibTable
gs2328fSTPPortStatusTable = _Gs2328fSTPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 9)
)
if mibBuilder.loadTexts:
    gs2328fSTPPortStatusTable.setStatus("current")
_Gs2328fSTPPortStatusEntry_Object = MibTableRow
gs2328fSTPPortStatusEntry = _Gs2328fSTPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 9, 1)
)
gs2328fSTPPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPPortStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328fSTPPortStatusEntry.setStatus("current")


class _Gs2328fSTPPortStatusPort_Type(Integer32):
    """Custom type gs2328fSTPPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPPortStatusPort_Type.__name__ = "Integer32"
_Gs2328fSTPPortStatusPort_Object = MibTableColumn
gs2328fSTPPortStatusPort = _Gs2328fSTPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 9, 1, 1),
    _Gs2328fSTPPortStatusPort_Type()
)
gs2328fSTPPortStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPPortStatusPort.setStatus("current")
_Gs2328fSTPPortStatusCISTRole_Type = DisplayString
_Gs2328fSTPPortStatusCISTRole_Object = MibTableColumn
gs2328fSTPPortStatusCISTRole = _Gs2328fSTPPortStatusCISTRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 9, 1, 2),
    _Gs2328fSTPPortStatusCISTRole_Type()
)
gs2328fSTPPortStatusCISTRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPPortStatusCISTRole.setStatus("current")
_Gs2328fSTPPortStatusCISTState_Type = DisplayString
_Gs2328fSTPPortStatusCISTState_Object = MibTableColumn
gs2328fSTPPortStatusCISTState = _Gs2328fSTPPortStatusCISTState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 9, 1, 3),
    _Gs2328fSTPPortStatusCISTState_Type()
)
gs2328fSTPPortStatusCISTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPPortStatusCISTState.setStatus("current")
_Gs2328fSTPPortStatusUptime_Type = DisplayString
_Gs2328fSTPPortStatusUptime_Object = MibTableColumn
gs2328fSTPPortStatusUptime = _Gs2328fSTPPortStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 9, 1, 4),
    _Gs2328fSTPPortStatusUptime_Type()
)
gs2328fSTPPortStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPPortStatusUptime.setStatus("current")
_Gs2328fSTPPortStatisticsTable_Object = MibTable
gs2328fSTPPortStatisticsTable = _Gs2328fSTPPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10)
)
if mibBuilder.loadTexts:
    gs2328fSTPPortStatisticsTable.setStatus("current")
_Gs2328fSTPPortStatisticsEntry_Object = MibTableRow
gs2328fSTPPortStatisticsEntry = _Gs2328fSTPPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1)
)
gs2328fSTPPortStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fSTPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fSTPPortStatisticsEntry.setStatus("current")


class _Gs2328fSTPStatisticsIndex_Type(Integer32):
    """Custom type gs2328fSTPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fSTPStatisticsIndex_Type.__name__ = "Integer32"
_Gs2328fSTPStatisticsIndex_Object = MibTableColumn
gs2328fSTPStatisticsIndex = _Gs2328fSTPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 1),
    _Gs2328fSTPStatisticsIndex_Type()
)
gs2328fSTPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsIndex.setStatus("current")
_Gs2328fSTPStatisticsPort_Type = DisplayString
_Gs2328fSTPStatisticsPort_Object = MibTableColumn
gs2328fSTPStatisticsPort = _Gs2328fSTPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 2),
    _Gs2328fSTPStatisticsPort_Type()
)
gs2328fSTPStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsPort.setStatus("current")
_Gs2328fSTPStatisticsTxMSTP_Type = Counter32
_Gs2328fSTPStatisticsTxMSTP_Object = MibTableColumn
gs2328fSTPStatisticsTxMSTP = _Gs2328fSTPStatisticsTxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 3),
    _Gs2328fSTPStatisticsTxMSTP_Type()
)
gs2328fSTPStatisticsTxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsTxMSTP.setStatus("current")
_Gs2328fSTPStatisticsTxRSTP_Type = Counter32
_Gs2328fSTPStatisticsTxRSTP_Object = MibTableColumn
gs2328fSTPStatisticsTxRSTP = _Gs2328fSTPStatisticsTxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 4),
    _Gs2328fSTPStatisticsTxRSTP_Type()
)
gs2328fSTPStatisticsTxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsTxRSTP.setStatus("current")
_Gs2328fSTPStatisticsTxSTP_Type = Counter32
_Gs2328fSTPStatisticsTxSTP_Object = MibTableColumn
gs2328fSTPStatisticsTxSTP = _Gs2328fSTPStatisticsTxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 5),
    _Gs2328fSTPStatisticsTxSTP_Type()
)
gs2328fSTPStatisticsTxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsTxSTP.setStatus("current")
_Gs2328fSTPStatisticsTxTCN_Type = Counter32
_Gs2328fSTPStatisticsTxTCN_Object = MibTableColumn
gs2328fSTPStatisticsTxTCN = _Gs2328fSTPStatisticsTxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 6),
    _Gs2328fSTPStatisticsTxTCN_Type()
)
gs2328fSTPStatisticsTxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsTxTCN.setStatus("current")
_Gs2328fSTPStatisticsRxMSTP_Type = Counter32
_Gs2328fSTPStatisticsRxMSTP_Object = MibTableColumn
gs2328fSTPStatisticsRxMSTP = _Gs2328fSTPStatisticsRxMSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 7),
    _Gs2328fSTPStatisticsRxMSTP_Type()
)
gs2328fSTPStatisticsRxMSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsRxMSTP.setStatus("current")
_Gs2328fSTPStatisticsRxRSTP_Type = Counter32
_Gs2328fSTPStatisticsRxRSTP_Object = MibTableColumn
gs2328fSTPStatisticsRxRSTP = _Gs2328fSTPStatisticsRxRSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 8),
    _Gs2328fSTPStatisticsRxRSTP_Type()
)
gs2328fSTPStatisticsRxRSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsRxRSTP.setStatus("current")
_Gs2328fSTPStatisticsRxSTP_Type = Counter32
_Gs2328fSTPStatisticsRxSTP_Object = MibTableColumn
gs2328fSTPStatisticsRxSTP = _Gs2328fSTPStatisticsRxSTP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 9),
    _Gs2328fSTPStatisticsRxSTP_Type()
)
gs2328fSTPStatisticsRxSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsRxSTP.setStatus("current")
_Gs2328fSTPStatisticsRxTCN_Type = Counter32
_Gs2328fSTPStatisticsRxTCN_Object = MibTableColumn
gs2328fSTPStatisticsRxTCN = _Gs2328fSTPStatisticsRxTCN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 10),
    _Gs2328fSTPStatisticsRxTCN_Type()
)
gs2328fSTPStatisticsRxTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsRxTCN.setStatus("current")
_Gs2328fSTPStatisticsDiscardedUnknown_Type = Counter32
_Gs2328fSTPStatisticsDiscardedUnknown_Object = MibTableColumn
gs2328fSTPStatisticsDiscardedUnknown = _Gs2328fSTPStatisticsDiscardedUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 11),
    _Gs2328fSTPStatisticsDiscardedUnknown_Type()
)
gs2328fSTPStatisticsDiscardedUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsDiscardedUnknown.setStatus("current")
_Gs2328fSTPStatisticsDiscardedIllegal_Type = Counter32
_Gs2328fSTPStatisticsDiscardedIllegal_Object = MibTableColumn
gs2328fSTPStatisticsDiscardedIllegal = _Gs2328fSTPStatisticsDiscardedIllegal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 20, 10, 1, 12),
    _Gs2328fSTPStatisticsDiscardedIllegal_Type()
)
gs2328fSTPStatisticsDiscardedIllegal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSTPStatisticsDiscardedIllegal.setStatus("current")
_Gs2328fFilteringDataBase_ObjectIdentity = ObjectIdentity
gs2328fFilteringDataBase = _Gs2328fFilteringDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21)
)
_Gs2328fFilteringDataBaseConfig_ObjectIdentity = ObjectIdentity
gs2328fFilteringDataBaseConfig = _Gs2328fFilteringDataBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1)
)


class _Gs2328fFilteringDataBaseAgingTime_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Gs2328fFilteringDataBaseAgingTime_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseAgingTime_Object = MibScalar
gs2328fFilteringDataBaseAgingTime = _Gs2328fFilteringDataBaseAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 1),
    _Gs2328fFilteringDataBaseAgingTime_Type()
)
gs2328fFilteringDataBaseAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseAgingTime.setStatus("current")
_Gs2328fFilteringDataBaseConfigTable_Object = MibTable
gs2328fFilteringDataBaseConfigTable = _Gs2328fFilteringDataBaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseConfigTable.setStatus("current")
_Gs2328fFilteringDataBaseConfigEntry_Object = MibTableRow
gs2328fFilteringDataBaseConfigEntry = _Gs2328fFilteringDataBaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 2, 1)
)
gs2328fFilteringDataBaseConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fFilteringDataBaseConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseConfigEntry.setStatus("current")


class _Gs2328fFilteringDataBaseConfigPort_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fFilteringDataBaseConfigPort_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseConfigPort_Object = MibTableColumn
gs2328fFilteringDataBaseConfigPort = _Gs2328fFilteringDataBaseConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 2, 1, 1),
    _Gs2328fFilteringDataBaseConfigPort_Type()
)
gs2328fFilteringDataBaseConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseConfigPort.setStatus("current")


class _Gs2328fFilteringDataBaseConfigLearning_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseConfigLearning based on Integer32"""
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


_Gs2328fFilteringDataBaseConfigLearning_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseConfigLearning_Object = MibTableColumn
gs2328fFilteringDataBaseConfigLearning = _Gs2328fFilteringDataBaseConfigLearning_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 2, 1, 2),
    _Gs2328fFilteringDataBaseConfigLearning_Type()
)
gs2328fFilteringDataBaseConfigLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseConfigLearning.setStatus("current")
_Gs2328fFilteringDataBaseStaticMAC_ObjectIdentity = ObjectIdentity
gs2328fFilteringDataBaseStaticMAC = _Gs2328fFilteringDataBaseStaticMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3)
)


class _Gs2328fFilteringDataBaseStaticMACCreate_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseStaticMACCreate based on Integer32"""
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


_Gs2328fFilteringDataBaseStaticMACCreate_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseStaticMACCreate_Object = MibScalar
gs2328fFilteringDataBaseStaticMACCreate = _Gs2328fFilteringDataBaseStaticMACCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 1),
    _Gs2328fFilteringDataBaseStaticMACCreate_Type()
)
gs2328fFilteringDataBaseStaticMACCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACCreate.setStatus("current")
_Gs2328fFilteringDataBaseStaticMACTable_Object = MibTable
gs2328fFilteringDataBaseStaticMACTable = _Gs2328fFilteringDataBaseStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACTable.setStatus("current")
_Gs2328fFilteringDataBaseStaticMACEntry_Object = MibTableRow
gs2328fFilteringDataBaseStaticMACEntry = _Gs2328fFilteringDataBaseStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2, 1)
)
gs2328fFilteringDataBaseStaticMACEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fFilteringDataBaseStaticMACIndex"),
)
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACEntry.setStatus("current")


class _Gs2328fFilteringDataBaseStaticMACIndex_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseStaticMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fFilteringDataBaseStaticMACIndex_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseStaticMACIndex_Object = MibTableColumn
gs2328fFilteringDataBaseStaticMACIndex = _Gs2328fFilteringDataBaseStaticMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2, 1, 1),
    _Gs2328fFilteringDataBaseStaticMACIndex_Type()
)
gs2328fFilteringDataBaseStaticMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACIndex.setStatus("current")


class _Gs2328fFilteringDataBaseStaticMACVLANId_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseStaticMACVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fFilteringDataBaseStaticMACVLANId_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseStaticMACVLANId_Object = MibTableColumn
gs2328fFilteringDataBaseStaticMACVLANId = _Gs2328fFilteringDataBaseStaticMACVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2, 1, 2),
    _Gs2328fFilteringDataBaseStaticMACVLANId_Type()
)
gs2328fFilteringDataBaseStaticMACVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACVLANId.setStatus("current")
_Gs2328fFilteringDataBaseStaticMACAddress_Type = MacAddress
_Gs2328fFilteringDataBaseStaticMACAddress_Object = MibTableColumn
gs2328fFilteringDataBaseStaticMACAddress = _Gs2328fFilteringDataBaseStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2, 1, 3),
    _Gs2328fFilteringDataBaseStaticMACAddress_Type()
)
gs2328fFilteringDataBaseStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACAddress.setStatus("current")
_Gs2328fFilteringDataBaseStaticMACPortMembers_Type = DisplayString
_Gs2328fFilteringDataBaseStaticMACPortMembers_Object = MibTableColumn
gs2328fFilteringDataBaseStaticMACPortMembers = _Gs2328fFilteringDataBaseStaticMACPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2, 1, 4),
    _Gs2328fFilteringDataBaseStaticMACPortMembers_Type()
)
gs2328fFilteringDataBaseStaticMACPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACPortMembers.setStatus("current")


class _Gs2328fFilteringDataBaseStaticMACRowStatus_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseStaticMACRowStatus based on Integer32"""
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


_Gs2328fFilteringDataBaseStaticMACRowStatus_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseStaticMACRowStatus_Object = MibTableColumn
gs2328fFilteringDataBaseStaticMACRowStatus = _Gs2328fFilteringDataBaseStaticMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 3, 2, 1, 5),
    _Gs2328fFilteringDataBaseStaticMACRowStatus_Type()
)
gs2328fFilteringDataBaseStaticMACRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseStaticMACRowStatus.setStatus("current")
_Gs2328fFilteringDataBaseDynamicMACTable_Object = MibTable
gs2328fFilteringDataBaseDynamicMACTable = _Gs2328fFilteringDataBaseDynamicMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicMACTable.setStatus("current")
_Gs2328fFilteringDataBaseDynamicMACEntry_Object = MibTableRow
gs2328fFilteringDataBaseDynamicMACEntry = _Gs2328fFilteringDataBaseDynamicMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4, 1)
)
gs2328fFilteringDataBaseDynamicMACEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fFilteringDataBaseDynamicMACIndex"),
)
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicMACEntry.setStatus("current")


class _Gs2328fFilteringDataBaseDynamicMACIndex_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseDynamicMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fFilteringDataBaseDynamicMACIndex_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseDynamicMACIndex_Object = MibTableColumn
gs2328fFilteringDataBaseDynamicMACIndex = _Gs2328fFilteringDataBaseDynamicMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4, 1, 1),
    _Gs2328fFilteringDataBaseDynamicMACIndex_Type()
)
gs2328fFilteringDataBaseDynamicMACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicMACIndex.setStatus("current")


class _Gs2328fFilteringDataBaseDynamicMACType_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseDynamicMACType based on Integer32"""
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


_Gs2328fFilteringDataBaseDynamicMACType_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseDynamicMACType_Object = MibTableColumn
gs2328fFilteringDataBaseDynamicMACType = _Gs2328fFilteringDataBaseDynamicMACType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4, 1, 2),
    _Gs2328fFilteringDataBaseDynamicMACType_Type()
)
gs2328fFilteringDataBaseDynamicMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicMACType.setStatus("current")


class _Gs2328fFilteringDataBaseDynamicMACVLAN_Type(Integer32):
    """Custom type gs2328fFilteringDataBaseDynamicMACVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fFilteringDataBaseDynamicMACVLAN_Type.__name__ = "Integer32"
_Gs2328fFilteringDataBaseDynamicMACVLAN_Object = MibTableColumn
gs2328fFilteringDataBaseDynamicMACVLAN = _Gs2328fFilteringDataBaseDynamicMACVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4, 1, 3),
    _Gs2328fFilteringDataBaseDynamicMACVLAN_Type()
)
gs2328fFilteringDataBaseDynamicMACVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicMACVLAN.setStatus("current")
_Gs2328fFilteringDataBaseDynamicMACAddress_Type = MacAddress
_Gs2328fFilteringDataBaseDynamicMACAddress_Object = MibTableColumn
gs2328fFilteringDataBaseDynamicMACAddress = _Gs2328fFilteringDataBaseDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4, 1, 4),
    _Gs2328fFilteringDataBaseDynamicMACAddress_Type()
)
gs2328fFilteringDataBaseDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicMACAddress.setStatus("current")
_Gs2328fFilteringDataBaseDynamicPortMembers_Type = DisplayString
_Gs2328fFilteringDataBaseDynamicPortMembers_Object = MibTableColumn
gs2328fFilteringDataBaseDynamicPortMembers = _Gs2328fFilteringDataBaseDynamicPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 21, 1, 4, 1, 5),
    _Gs2328fFilteringDataBaseDynamicPortMembers_Type()
)
gs2328fFilteringDataBaseDynamicPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fFilteringDataBaseDynamicPortMembers.setStatus("current")
_Gs2328fSFlowAgent_ObjectIdentity = ObjectIdentity
gs2328fSFlowAgent = _Gs2328fSFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 22)
)
_Gs2328fSFlowAgentCollector_ObjectIdentity = ObjectIdentity
gs2328fSFlowAgentCollector = _Gs2328fSFlowAgentCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 22, 1)
)


class _Gs2328fSFlowAgentReceiverMode_Type(Integer32):
    """Custom type gs2328fSFlowAgentReceiverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSFlowAgentReceiverMode_Type.__name__ = "Integer32"
_Gs2328fSFlowAgentReceiverMode_Object = MibScalar
gs2328fSFlowAgentReceiverMode = _Gs2328fSFlowAgentReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 22, 1, 1),
    _Gs2328fSFlowAgentReceiverMode_Type()
)
gs2328fSFlowAgentReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSFlowAgentReceiverMode.setStatus("current")
_Gs2328fLMC_ObjectIdentity = ObjectIdentity
gs2328fLMC = _Gs2328fLMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500)
)


class _Gs2328fLMCOperating_Type(Integer32):
    """Custom type gs2328fLMCOperating based on Integer32"""
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


_Gs2328fLMCOperating_Type.__name__ = "Integer32"
_Gs2328fLMCOperating_Object = MibScalar
gs2328fLMCOperating = _Gs2328fLMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 1),
    _Gs2328fLMCOperating_Type()
)
gs2328fLMCOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLMCOperating.setStatus("current")


class _Gs2328fLMCConfigViaDhcp_Type(Integer32):
    """Custom type gs2328fLMCConfigViaDhcp based on Integer32"""
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


_Gs2328fLMCConfigViaDhcp_Type.__name__ = "Integer32"
_Gs2328fLMCConfigViaDhcp_Object = MibScalar
gs2328fLMCConfigViaDhcp = _Gs2328fLMCConfigViaDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 2),
    _Gs2328fLMCConfigViaDhcp_Type()
)
gs2328fLMCConfigViaDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLMCConfigViaDhcp.setStatus("current")


class _Gs2328fLMCDomain_Type(DisplayString):
    """Custom type gs2328fLMCDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gs2328fLMCDomain_Type.__name__ = "DisplayString"
_Gs2328fLMCDomain_Object = MibScalar
gs2328fLMCDomain = _Gs2328fLMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 3),
    _Gs2328fLMCDomain_Type()
)
gs2328fLMCDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLMCDomain.setStatus("current")


class _Gs2328fLMChcpClientAutoRenew_Type(Integer32):
    """Custom type gs2328fLMChcpClientAutoRenew based on Integer32"""
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


_Gs2328fLMChcpClientAutoRenew_Type.__name__ = "Integer32"
_Gs2328fLMChcpClientAutoRenew_Object = MibScalar
gs2328fLMChcpClientAutoRenew = _Gs2328fLMChcpClientAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 4),
    _Gs2328fLMChcpClientAutoRenew_Type()
)
gs2328fLMChcpClientAutoRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLMChcpClientAutoRenew.setStatus("current")


class _Gs2328fLMCZeroTouchSupport_Type(Integer32):
    """Custom type gs2328fLMCZeroTouchSupport based on Integer32"""
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


_Gs2328fLMCZeroTouchSupport_Type.__name__ = "Integer32"
_Gs2328fLMCZeroTouchSupport_Object = MibScalar
gs2328fLMCZeroTouchSupport = _Gs2328fLMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 50),
    _Gs2328fLMCZeroTouchSupport_Type()
)
gs2328fLMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCZeroTouchSupport.setStatus("current")


class _Gs2328fLMCPairingTokenPresent_Type(Integer32):
    """Custom type gs2328fLMCPairingTokenPresent based on Integer32"""
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


_Gs2328fLMCPairingTokenPresent_Type.__name__ = "Integer32"
_Gs2328fLMCPairingTokenPresent_Object = MibScalar
gs2328fLMCPairingTokenPresent = _Gs2328fLMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 51),
    _Gs2328fLMCPairingTokenPresent_Type()
)
gs2328fLMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCPairingTokenPresent.setStatus("current")
_Gs2328fLMCClientStatus_Type = DisplayString
_Gs2328fLMCClientStatus_Object = MibScalar
gs2328fLMCClientStatus = _Gs2328fLMCClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 52),
    _Gs2328fLMCClientStatus_Type()
)
gs2328fLMCClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCClientStatus.setStatus("current")


class _Gs2328fLMCManagementStatus_Type(Integer32):
    """Custom type gs2328fLMCManagementStatus based on Integer32"""
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


_Gs2328fLMCManagementStatus_Type.__name__ = "Integer32"
_Gs2328fLMCManagementStatus_Object = MibScalar
gs2328fLMCManagementStatus = _Gs2328fLMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 53),
    _Gs2328fLMCManagementStatus_Type()
)
gs2328fLMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCManagementStatus.setStatus("current")


class _Gs2328fLMCControlStatus_Type(Integer32):
    """Custom type gs2328fLMCControlStatus based on Integer32"""
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


_Gs2328fLMCControlStatus_Type.__name__ = "Integer32"
_Gs2328fLMCControlStatus_Object = MibScalar
gs2328fLMCControlStatus = _Gs2328fLMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 54),
    _Gs2328fLMCControlStatus_Type()
)
gs2328fLMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCControlStatus.setStatus("current")


class _Gs2328fLMCMonitoringStatus_Type(Integer32):
    """Custom type gs2328fLMCMonitoringStatus based on Integer32"""
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


_Gs2328fLMCMonitoringStatus_Type.__name__ = "Integer32"
_Gs2328fLMCMonitoringStatus_Object = MibScalar
gs2328fLMCMonitoringStatus = _Gs2328fLMCMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 55),
    _Gs2328fLMCMonitoringStatus_Type()
)
gs2328fLMCMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCMonitoringStatus.setStatus("current")
_Gs2328fLMCConfigurationSource_Type = DisplayString
_Gs2328fLMCConfigurationSource_Object = MibScalar
gs2328fLMCConfigurationSource = _Gs2328fLMCConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 56),
    _Gs2328fLMCConfigurationSource_Type()
)
gs2328fLMCConfigurationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCConfigurationSource.setStatus("current")


class _Gs2328fLMCConfigModified_Type(Integer32):
    """Custom type gs2328fLMCConfigModified based on Integer32"""
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


_Gs2328fLMCConfigModified_Type.__name__ = "Integer32"
_Gs2328fLMCConfigModified_Object = MibScalar
gs2328fLMCConfigModified = _Gs2328fLMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 57),
    _Gs2328fLMCConfigModified_Type()
)
gs2328fLMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCConfigModified.setStatus("current")
_Gs2328fLMCDeviceID_Type = DisplayString
_Gs2328fLMCDeviceID_Object = MibScalar
gs2328fLMCDeviceID = _Gs2328fLMCDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 58),
    _Gs2328fLMCDeviceID_Type()
)
gs2328fLMCDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCDeviceID.setStatus("current")
_Gs2328fLMCRoundTripTime_Type = Integer32
_Gs2328fLMCRoundTripTime_Object = MibScalar
gs2328fLMCRoundTripTime = _Gs2328fLMCRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 2, 1500, 100),
    _Gs2328fLMCRoundTripTime_Type()
)
gs2328fLMCRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fLMCRoundTripTime.setStatus("current")
_Gs2328fSecurity_ObjectIdentity = ObjectIdentity
gs2328fSecurity = _Gs2328fSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3)
)
_Gs2328fIPSourceGuard_ObjectIdentity = ObjectIdentity
gs2328fIPSourceGuard = _Gs2328fIPSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1)
)
_Gs2328fIPSourceGuardConf_ObjectIdentity = ObjectIdentity
gs2328fIPSourceGuardConf = _Gs2328fIPSourceGuardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1)
)


class _Gs2328fIPSourceGuardMode_Type(Integer32):
    """Custom type gs2328fIPSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIPSourceGuardMode_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardMode_Object = MibScalar
gs2328fIPSourceGuardMode = _Gs2328fIPSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1, 1),
    _Gs2328fIPSourceGuardMode_Type()
)
gs2328fIPSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardMode.setStatus("current")
_Gs2328fIPSourceGuardPortConfigTable_Object = MibTable
gs2328fIPSourceGuardPortConfigTable = _Gs2328fIPSourceGuardPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardPortConfigTable.setStatus("current")
_Gs2328fIPSourceGuardPortConfigEntry_Object = MibTableRow
gs2328fIPSourceGuardPortConfigEntry = _Gs2328fIPSourceGuardPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1, 2, 1)
)
gs2328fIPSourceGuardPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIPSourceGuardPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardPortConfigEntry.setStatus("current")


class _Gs2328fIPSourceGuardPortConfigPort_Type(Integer32):
    """Custom type gs2328fIPSourceGuardPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIPSourceGuardPortConfigPort_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardPortConfigPort_Object = MibTableColumn
gs2328fIPSourceGuardPortConfigPort = _Gs2328fIPSourceGuardPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1, 2, 1, 1),
    _Gs2328fIPSourceGuardPortConfigPort_Type()
)
gs2328fIPSourceGuardPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardPortConfigPort.setStatus("current")


class _Gs2328fIPSourceGuardPortConfigMode_Type(Integer32):
    """Custom type gs2328fIPSourceGuardPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fIPSourceGuardPortConfigMode_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardPortConfigMode_Object = MibTableColumn
gs2328fIPSourceGuardPortConfigMode = _Gs2328fIPSourceGuardPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1, 2, 1, 2),
    _Gs2328fIPSourceGuardPortConfigMode_Type()
)
gs2328fIPSourceGuardPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardPortConfigMode.setStatus("current")


class _Gs2328fIPSourceGuardPortMaxDynamicClients_Type(Integer32):
    """Custom type gs2328fIPSourceGuardPortMaxDynamicClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(99, 99),
    )


_Gs2328fIPSourceGuardPortMaxDynamicClients_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardPortMaxDynamicClients_Object = MibTableColumn
gs2328fIPSourceGuardPortMaxDynamicClients = _Gs2328fIPSourceGuardPortMaxDynamicClients_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 1, 2, 1, 3),
    _Gs2328fIPSourceGuardPortMaxDynamicClients_Type()
)
gs2328fIPSourceGuardPortMaxDynamicClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardPortMaxDynamicClients.setStatus("current")
_Gs2328fIPSourceGuardStatic_ObjectIdentity = ObjectIdentity
gs2328fIPSourceGuardStatic = _Gs2328fIPSourceGuardStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2)
)


class _Gs2328fIPSourceGuardStaticCreate_Type(Integer32):
    """Custom type gs2328fIPSourceGuardStaticCreate based on Integer32"""
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


_Gs2328fIPSourceGuardStaticCreate_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardStaticCreate_Object = MibScalar
gs2328fIPSourceGuardStaticCreate = _Gs2328fIPSourceGuardStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 1),
    _Gs2328fIPSourceGuardStaticCreate_Type()
)
gs2328fIPSourceGuardStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticCreate.setStatus("current")
_Gs2328fIPSourceGuardStaticTable_Object = MibTable
gs2328fIPSourceGuardStaticTable = _Gs2328fIPSourceGuardStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticTable.setStatus("current")
_Gs2328fIPSourceGuardStaticEntry_Object = MibTableRow
gs2328fIPSourceGuardStaticEntry = _Gs2328fIPSourceGuardStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1)
)
gs2328fIPSourceGuardStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIPSourceGuardStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticEntry.setStatus("current")


class _Gs2328fIPSourceGuardStaticIndex_Type(Integer32):
    """Custom type gs2328fIPSourceGuardStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_Gs2328fIPSourceGuardStaticIndex_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardStaticIndex_Object = MibTableColumn
gs2328fIPSourceGuardStaticIndex = _Gs2328fIPSourceGuardStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1, 1),
    _Gs2328fIPSourceGuardStaticIndex_Type()
)
gs2328fIPSourceGuardStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticIndex.setStatus("current")


class _Gs2328fIPSourceGuardStaticPort_Type(Integer32):
    """Custom type gs2328fIPSourceGuardStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIPSourceGuardStaticPort_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardStaticPort_Object = MibTableColumn
gs2328fIPSourceGuardStaticPort = _Gs2328fIPSourceGuardStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1, 2),
    _Gs2328fIPSourceGuardStaticPort_Type()
)
gs2328fIPSourceGuardStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticPort.setStatus("current")


class _Gs2328fIPSourceGuardStaticVLANId_Type(Integer32):
    """Custom type gs2328fIPSourceGuardStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fIPSourceGuardStaticVLANId_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardStaticVLANId_Object = MibTableColumn
gs2328fIPSourceGuardStaticVLANId = _Gs2328fIPSourceGuardStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1, 3),
    _Gs2328fIPSourceGuardStaticVLANId_Type()
)
gs2328fIPSourceGuardStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticVLANId.setStatus("current")
_Gs2328fIPSourceGuardStaticIPAddress_Type = IpAddress
_Gs2328fIPSourceGuardStaticIPAddress_Object = MibTableColumn
gs2328fIPSourceGuardStaticIPAddress = _Gs2328fIPSourceGuardStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1, 4),
    _Gs2328fIPSourceGuardStaticIPAddress_Type()
)
gs2328fIPSourceGuardStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticIPAddress.setStatus("current")
_Gs2328fIPSourceGuardStaticMACAddress_Type = MacAddress
_Gs2328fIPSourceGuardStaticMACAddress_Object = MibTableColumn
gs2328fIPSourceGuardStaticMACAddress = _Gs2328fIPSourceGuardStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1, 5),
    _Gs2328fIPSourceGuardStaticMACAddress_Type()
)
gs2328fIPSourceGuardStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticMACAddress.setStatus("current")


class _Gs2328fIPSourceGuardStaticRowStatus_Type(Integer32):
    """Custom type gs2328fIPSourceGuardStaticRowStatus based on Integer32"""
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


_Gs2328fIPSourceGuardStaticRowStatus_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardStaticRowStatus_Object = MibTableColumn
gs2328fIPSourceGuardStaticRowStatus = _Gs2328fIPSourceGuardStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 2, 2, 1, 6),
    _Gs2328fIPSourceGuardStaticRowStatus_Type()
)
gs2328fIPSourceGuardStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardStaticRowStatus.setStatus("current")
_Gs2328fIPSourceGuardDynamicTable_Object = MibTable
gs2328fIPSourceGuardDynamicTable = _Gs2328fIPSourceGuardDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3)
)
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicTable.setStatus("current")
_Gs2328fIPSourceGuardDynamicEntry_Object = MibTableRow
gs2328fIPSourceGuardDynamicEntry = _Gs2328fIPSourceGuardDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3, 1)
)
gs2328fIPSourceGuardDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fIPSourceGuardDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicEntry.setStatus("current")


class _Gs2328fIPSourceGuardDynamicIndex_Type(Integer32):
    """Custom type gs2328fIPSourceGuardDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fIPSourceGuardDynamicIndex_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardDynamicIndex_Object = MibTableColumn
gs2328fIPSourceGuardDynamicIndex = _Gs2328fIPSourceGuardDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3, 1, 1),
    _Gs2328fIPSourceGuardDynamicIndex_Type()
)
gs2328fIPSourceGuardDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicIndex.setStatus("current")


class _Gs2328fIPSourceGuardDynamicPort_Type(Integer32):
    """Custom type gs2328fIPSourceGuardDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2328fIPSourceGuardDynamicPort_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardDynamicPort_Object = MibTableColumn
gs2328fIPSourceGuardDynamicPort = _Gs2328fIPSourceGuardDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3, 1, 2),
    _Gs2328fIPSourceGuardDynamicPort_Type()
)
gs2328fIPSourceGuardDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicPort.setStatus("current")


class _Gs2328fIPSourceGuardDynamicVLANId_Type(Integer32):
    """Custom type gs2328fIPSourceGuardDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fIPSourceGuardDynamicVLANId_Type.__name__ = "Integer32"
_Gs2328fIPSourceGuardDynamicVLANId_Object = MibTableColumn
gs2328fIPSourceGuardDynamicVLANId = _Gs2328fIPSourceGuardDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3, 1, 3),
    _Gs2328fIPSourceGuardDynamicVLANId_Type()
)
gs2328fIPSourceGuardDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicVLANId.setStatus("current")
_Gs2328fIPSourceGuardDynamicIPAddress_Type = IpAddress
_Gs2328fIPSourceGuardDynamicIPAddress_Object = MibTableColumn
gs2328fIPSourceGuardDynamicIPAddress = _Gs2328fIPSourceGuardDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3, 1, 4),
    _Gs2328fIPSourceGuardDynamicIPAddress_Type()
)
gs2328fIPSourceGuardDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicIPAddress.setStatus("current")
_Gs2328fIPSourceGuardDynamicMACAddress_Type = MacAddress
_Gs2328fIPSourceGuardDynamicMACAddress_Object = MibTableColumn
gs2328fIPSourceGuardDynamicMACAddress = _Gs2328fIPSourceGuardDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 1, 3, 1, 5),
    _Gs2328fIPSourceGuardDynamicMACAddress_Type()
)
gs2328fIPSourceGuardDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fIPSourceGuardDynamicMACAddress.setStatus("current")
_Gs2328fARPInspection_ObjectIdentity = ObjectIdentity
gs2328fARPInspection = _Gs2328fARPInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2)
)
_Gs2328fARPInspectionConf_ObjectIdentity = ObjectIdentity
gs2328fARPInspectionConf = _Gs2328fARPInspectionConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 1)
)


class _Gs2328fARPInspectionConfMode_Type(Integer32):
    """Custom type gs2328fARPInspectionConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPInspectionConfMode_Type.__name__ = "Integer32"
_Gs2328fARPInspectionConfMode_Object = MibScalar
gs2328fARPInspectionConfMode = _Gs2328fARPInspectionConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 1, 1),
    _Gs2328fARPInspectionConfMode_Type()
)
gs2328fARPInspectionConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionConfMode.setStatus("current")
_Gs2328fARPInspectionConfTable_Object = MibTable
gs2328fARPInspectionConfTable = _Gs2328fARPInspectionConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fARPInspectionConfTable.setStatus("current")
_Gs2328fARPInspectionConfEntry_Object = MibTableRow
gs2328fARPInspectionConfEntry = _Gs2328fARPInspectionConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 1, 2, 1)
)
gs2328fARPInspectionConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fARPInspectionConfPortIndex"),
)
if mibBuilder.loadTexts:
    gs2328fARPInspectionConfEntry.setStatus("current")


class _Gs2328fARPInspectionConfPortIndex_Type(Integer32):
    """Custom type gs2328fARPInspectionConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPInspectionConfPortIndex_Type.__name__ = "Integer32"
_Gs2328fARPInspectionConfPortIndex_Object = MibTableColumn
gs2328fARPInspectionConfPortIndex = _Gs2328fARPInspectionConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 1, 2, 1, 1),
    _Gs2328fARPInspectionConfPortIndex_Type()
)
gs2328fARPInspectionConfPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fARPInspectionConfPortIndex.setStatus("current")


class _Gs2328fARPInspectionConfPortMode_Type(Integer32):
    """Custom type gs2328fARPInspectionConfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPInspectionConfPortMode_Type.__name__ = "Integer32"
_Gs2328fARPInspectionConfPortMode_Object = MibTableColumn
gs2328fARPInspectionConfPortMode = _Gs2328fARPInspectionConfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 1, 2, 1, 2),
    _Gs2328fARPInspectionConfPortMode_Type()
)
gs2328fARPInspectionConfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionConfPortMode.setStatus("current")
_Gs2328fARPInspectionStatic_ObjectIdentity = ObjectIdentity
gs2328fARPInspectionStatic = _Gs2328fARPInspectionStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2)
)


class _Gs2328fARPInspectionStaticCreate_Type(Integer32):
    """Custom type gs2328fARPInspectionStaticCreate based on Integer32"""
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


_Gs2328fARPInspectionStaticCreate_Type.__name__ = "Integer32"
_Gs2328fARPInspectionStaticCreate_Object = MibScalar
gs2328fARPInspectionStaticCreate = _Gs2328fARPInspectionStaticCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 1),
    _Gs2328fARPInspectionStaticCreate_Type()
)
gs2328fARPInspectionStaticCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticCreate.setStatus("current")
_Gs2328fARPInspectionStaticTable_Object = MibTable
gs2328fARPInspectionStaticTable = _Gs2328fARPInspectionStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticTable.setStatus("current")
_Gs2328fARPInspectionStaticEntry_Object = MibTableRow
gs2328fARPInspectionStaticEntry = _Gs2328fARPInspectionStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1)
)
gs2328fARPInspectionStaticEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fARPInspectionStaticIndex"),
)
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticEntry.setStatus("current")


class _Gs2328fARPInspectionStaticIndex_Type(Integer32):
    """Custom type gs2328fARPInspectionStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPInspectionStaticIndex_Type.__name__ = "Integer32"
_Gs2328fARPInspectionStaticIndex_Object = MibTableColumn
gs2328fARPInspectionStaticIndex = _Gs2328fARPInspectionStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1, 1),
    _Gs2328fARPInspectionStaticIndex_Type()
)
gs2328fARPInspectionStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticIndex.setStatus("current")


class _Gs2328fARPInspectionStaticPort_Type(Integer32):
    """Custom type gs2328fARPInspectionStaticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPInspectionStaticPort_Type.__name__ = "Integer32"
_Gs2328fARPInspectionStaticPort_Object = MibTableColumn
gs2328fARPInspectionStaticPort = _Gs2328fARPInspectionStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1, 2),
    _Gs2328fARPInspectionStaticPort_Type()
)
gs2328fARPInspectionStaticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticPort.setStatus("current")


class _Gs2328fARPInspectionStaticVLANId_Type(Integer32):
    """Custom type gs2328fARPInspectionStaticVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fARPInspectionStaticVLANId_Type.__name__ = "Integer32"
_Gs2328fARPInspectionStaticVLANId_Object = MibTableColumn
gs2328fARPInspectionStaticVLANId = _Gs2328fARPInspectionStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1, 3),
    _Gs2328fARPInspectionStaticVLANId_Type()
)
gs2328fARPInspectionStaticVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticVLANId.setStatus("current")
_Gs2328fARPInspectionStaticIPAddress_Type = IpAddress
_Gs2328fARPInspectionStaticIPAddress_Object = MibTableColumn
gs2328fARPInspectionStaticIPAddress = _Gs2328fARPInspectionStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1, 4),
    _Gs2328fARPInspectionStaticIPAddress_Type()
)
gs2328fARPInspectionStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticIPAddress.setStatus("current")
_Gs2328fARPInspectionStaticMACAddress_Type = MacAddress
_Gs2328fARPInspectionStaticMACAddress_Object = MibTableColumn
gs2328fARPInspectionStaticMACAddress = _Gs2328fARPInspectionStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1, 5),
    _Gs2328fARPInspectionStaticMACAddress_Type()
)
gs2328fARPInspectionStaticMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticMACAddress.setStatus("current")


class _Gs2328fARPInspectionStaticRowStatus_Type(Integer32):
    """Custom type gs2328fARPInspectionStaticRowStatus based on Integer32"""
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


_Gs2328fARPInspectionStaticRowStatus_Type.__name__ = "Integer32"
_Gs2328fARPInspectionStaticRowStatus_Object = MibTableColumn
gs2328fARPInspectionStaticRowStatus = _Gs2328fARPInspectionStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 2, 2, 1, 6),
    _Gs2328fARPInspectionStaticRowStatus_Type()
)
gs2328fARPInspectionStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPInspectionStaticRowStatus.setStatus("current")
_Gs2328fARPInspectionDynamicTable_Object = MibTable
gs2328fARPInspectionDynamicTable = _Gs2328fARPInspectionDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicTable.setStatus("current")
_Gs2328fARPInspectionDynamicEntry_Object = MibTableRow
gs2328fARPInspectionDynamicEntry = _Gs2328fARPInspectionDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3, 1)
)
gs2328fARPInspectionDynamicEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fARPInspectionDynamicIndex"),
)
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicEntry.setStatus("current")


class _Gs2328fARPInspectionDynamicIndex_Type(Integer32):
    """Custom type gs2328fARPInspectionDynamicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPInspectionDynamicIndex_Type.__name__ = "Integer32"
_Gs2328fARPInspectionDynamicIndex_Object = MibTableColumn
gs2328fARPInspectionDynamicIndex = _Gs2328fARPInspectionDynamicIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3, 1, 1),
    _Gs2328fARPInspectionDynamicIndex_Type()
)
gs2328fARPInspectionDynamicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicIndex.setStatus("current")


class _Gs2328fARPInspectionDynamicPort_Type(Integer32):
    """Custom type gs2328fARPInspectionDynamicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPInspectionDynamicPort_Type.__name__ = "Integer32"
_Gs2328fARPInspectionDynamicPort_Object = MibTableColumn
gs2328fARPInspectionDynamicPort = _Gs2328fARPInspectionDynamicPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3, 1, 2),
    _Gs2328fARPInspectionDynamicPort_Type()
)
gs2328fARPInspectionDynamicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicPort.setStatus("current")


class _Gs2328fARPInspectionDynamicVLANId_Type(Integer32):
    """Custom type gs2328fARPInspectionDynamicVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fARPInspectionDynamicVLANId_Type.__name__ = "Integer32"
_Gs2328fARPInspectionDynamicVLANId_Object = MibTableColumn
gs2328fARPInspectionDynamicVLANId = _Gs2328fARPInspectionDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3, 1, 3),
    _Gs2328fARPInspectionDynamicVLANId_Type()
)
gs2328fARPInspectionDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicVLANId.setStatus("current")
_Gs2328fARPInspectionDynamicIPAddress_Type = IpAddress
_Gs2328fARPInspectionDynamicIPAddress_Object = MibTableColumn
gs2328fARPInspectionDynamicIPAddress = _Gs2328fARPInspectionDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3, 1, 4),
    _Gs2328fARPInspectionDynamicIPAddress_Type()
)
gs2328fARPInspectionDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicIPAddress.setStatus("current")
_Gs2328fARPInspectionDynamicMACAddress_Type = MacAddress
_Gs2328fARPInspectionDynamicMACAddress_Object = MibTableColumn
gs2328fARPInspectionDynamicMACAddress = _Gs2328fARPInspectionDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 3, 1, 5),
    _Gs2328fARPInspectionDynamicMACAddress_Type()
)
gs2328fARPInspectionDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fARPInspectionDynamicMACAddress.setStatus("current")
_Gs2328fARPStaticGatewayCtrl_ObjectIdentity = ObjectIdentity
gs2328fARPStaticGatewayCtrl = _Gs2328fARPStaticGatewayCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6)
)
_Gs2328fARPStaticGatewayCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2328fARPStaticGatewayCtrlSystemConf = _Gs2328fARPStaticGatewayCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 1)
)


class _Gs2328fARPStaticGatewayCtrlMode_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPStaticGatewayCtrlMode_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlMode_Object = MibScalar
gs2328fARPStaticGatewayCtrlMode = _Gs2328fARPStaticGatewayCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 1, 1),
    _Gs2328fARPStaticGatewayCtrlMode_Type()
)
gs2328fARPStaticGatewayCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlMode.setStatus("current")


class _Gs2328fARPStaticGatewayCtrlCreate_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlCreate based on Integer32"""
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


_Gs2328fARPStaticGatewayCtrlCreate_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlCreate_Object = MibScalar
gs2328fARPStaticGatewayCtrlCreate = _Gs2328fARPStaticGatewayCtrlCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 2),
    _Gs2328fARPStaticGatewayCtrlCreate_Type()
)
gs2328fARPStaticGatewayCtrlCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlCreate.setStatus("current")
_Gs2328fARPStaticGatewayCtrlTable_Object = MibTable
gs2328fARPStaticGatewayCtrlTable = _Gs2328fARPStaticGatewayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlTable.setStatus("current")
_Gs2328fARPStaticGatewayCtrlEntry_Object = MibTableRow
gs2328fARPStaticGatewayCtrlEntry = _Gs2328fARPStaticGatewayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1)
)
gs2328fARPStaticGatewayCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fARPStaticGatewayCtrlIndex"),
)
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlEntry.setStatus("current")


class _Gs2328fARPStaticGatewayCtrlIndex_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2328fARPStaticGatewayCtrlIndex_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlIndex_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlIndex = _Gs2328fARPStaticGatewayCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 1),
    _Gs2328fARPStaticGatewayCtrlIndex_Type()
)
gs2328fARPStaticGatewayCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlIndex.setStatus("current")
_Gs2328fARPStaticGatewayCtrlIPAddress_Type = IpAddress
_Gs2328fARPStaticGatewayCtrlIPAddress_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlIPAddress = _Gs2328fARPStaticGatewayCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 2),
    _Gs2328fARPStaticGatewayCtrlIPAddress_Type()
)
gs2328fARPStaticGatewayCtrlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlIPAddress.setStatus("current")
_Gs2328fARPStaticGatewayCtrlMACAddress_Type = MacAddress
_Gs2328fARPStaticGatewayCtrlMACAddress_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlMACAddress = _Gs2328fARPStaticGatewayCtrlMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 3),
    _Gs2328fARPStaticGatewayCtrlMACAddress_Type()
)
gs2328fARPStaticGatewayCtrlMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlMACAddress.setStatus("current")


class _Gs2328fARPStaticGatewayCtrlPort_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPStaticGatewayCtrlPort_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlPort_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlPort = _Gs2328fARPStaticGatewayCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 4),
    _Gs2328fARPStaticGatewayCtrlPort_Type()
)
gs2328fARPStaticGatewayCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlPort.setStatus("current")


class _Gs2328fARPStaticGatewayCtrlAction_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlAction based on Integer32"""
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


_Gs2328fARPStaticGatewayCtrlAction_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlAction_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlAction = _Gs2328fARPStaticGatewayCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 5),
    _Gs2328fARPStaticGatewayCtrlAction_Type()
)
gs2328fARPStaticGatewayCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlAction.setStatus("current")
_Gs2328fARPStaticGatewayCtrlState_Type = DisplayString
_Gs2328fARPStaticGatewayCtrlState_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlState = _Gs2328fARPStaticGatewayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 6),
    _Gs2328fARPStaticGatewayCtrlState_Type()
)
gs2328fARPStaticGatewayCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlState.setStatus("current")


class _Gs2328fARPStaticGatewayCtrlReOpen_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlReOpen based on Integer32"""
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


_Gs2328fARPStaticGatewayCtrlReOpen_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlReOpen_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlReOpen = _Gs2328fARPStaticGatewayCtrlReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 7),
    _Gs2328fARPStaticGatewayCtrlReOpen_Type()
)
gs2328fARPStaticGatewayCtrlReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlReOpen.setStatus("current")


class _Gs2328fARPStaticGatewayCtrlRowStatus_Type(Integer32):
    """Custom type gs2328fARPStaticGatewayCtrlRowStatus based on Integer32"""
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


_Gs2328fARPStaticGatewayCtrlRowStatus_Type.__name__ = "Integer32"
_Gs2328fARPStaticGatewayCtrlRowStatus_Object = MibTableColumn
gs2328fARPStaticGatewayCtrlRowStatus = _Gs2328fARPStaticGatewayCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 6, 3, 1, 8),
    _Gs2328fARPStaticGatewayCtrlRowStatus_Type()
)
gs2328fARPStaticGatewayCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPStaticGatewayCtrlRowStatus.setStatus("current")
_Gs2328fARPSpoofingPrevention_ObjectIdentity = ObjectIdentity
gs2328fARPSpoofingPrevention = _Gs2328fARPSpoofingPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7)
)
_Gs2328fARPSpoofingPreventionSystemConf_ObjectIdentity = ObjectIdentity
gs2328fARPSpoofingPreventionSystemConf = _Gs2328fARPSpoofingPreventionSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 1)
)


class _Gs2328fARPSpoofingPreventionMode_Type(Integer32):
    """Custom type gs2328fARPSpoofingPreventionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPSpoofingPreventionMode_Type.__name__ = "Integer32"
_Gs2328fARPSpoofingPreventionMode_Object = MibScalar
gs2328fARPSpoofingPreventionMode = _Gs2328fARPSpoofingPreventionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 1, 1),
    _Gs2328fARPSpoofingPreventionMode_Type()
)
gs2328fARPSpoofingPreventionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionMode.setStatus("current")
_Gs2328fARPSpoofingPreventionTable_Object = MibTable
gs2328fARPSpoofingPreventionTable = _Gs2328fARPSpoofingPreventionTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionTable.setStatus("current")
_Gs2328fARPSpoofingPreventionEntry_Object = MibTableRow
gs2328fARPSpoofingPreventionEntry = _Gs2328fARPSpoofingPreventionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1)
)
gs2328fARPSpoofingPreventionEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fARPSpoofingPreventionPort"),
)
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionEntry.setStatus("current")


class _Gs2328fARPSpoofingPreventionPort_Type(Integer32):
    """Custom type gs2328fARPSpoofingPreventionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fARPSpoofingPreventionPort_Type.__name__ = "Integer32"
_Gs2328fARPSpoofingPreventionPort_Object = MibTableColumn
gs2328fARPSpoofingPreventionPort = _Gs2328fARPSpoofingPreventionPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1, 1),
    _Gs2328fARPSpoofingPreventionPort_Type()
)
gs2328fARPSpoofingPreventionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionPort.setStatus("current")


class _Gs2328fARPSpoofingPreventionPortMode_Type(Integer32):
    """Custom type gs2328fARPSpoofingPreventionPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPSpoofingPreventionPortMode_Type.__name__ = "Integer32"
_Gs2328fARPSpoofingPreventionPortMode_Object = MibTableColumn
gs2328fARPSpoofingPreventionPortMode = _Gs2328fARPSpoofingPreventionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1, 2),
    _Gs2328fARPSpoofingPreventionPortMode_Type()
)
gs2328fARPSpoofingPreventionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionPortMode.setStatus("current")


class _Gs2328fARPSpoofingPreventionPortLimit_Type(Integer32):
    """Custom type gs2328fARPSpoofingPreventionPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Gs2328fARPSpoofingPreventionPortLimit_Type.__name__ = "Integer32"
_Gs2328fARPSpoofingPreventionPortLimit_Object = MibTableColumn
gs2328fARPSpoofingPreventionPortLimit = _Gs2328fARPSpoofingPreventionPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1, 3),
    _Gs2328fARPSpoofingPreventionPortLimit_Type()
)
gs2328fARPSpoofingPreventionPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionPortLimit.setStatus("current")


class _Gs2328fARPSpoofingPreventionPortAction_Type(Integer32):
    """Custom type gs2328fARPSpoofingPreventionPortAction based on Integer32"""
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


_Gs2328fARPSpoofingPreventionPortAction_Type.__name__ = "Integer32"
_Gs2328fARPSpoofingPreventionPortAction_Object = MibTableColumn
gs2328fARPSpoofingPreventionPortAction = _Gs2328fARPSpoofingPreventionPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1, 4),
    _Gs2328fARPSpoofingPreventionPortAction_Type()
)
gs2328fARPSpoofingPreventionPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionPortAction.setStatus("current")
_Gs2328fARPSpoofingPreventionPortState_Type = DisplayString
_Gs2328fARPSpoofingPreventionPortState_Object = MibTableColumn
gs2328fARPSpoofingPreventionPortState = _Gs2328fARPSpoofingPreventionPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1, 5),
    _Gs2328fARPSpoofingPreventionPortState_Type()
)
gs2328fARPSpoofingPreventionPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionPortState.setStatus("current")


class _Gs2328fARPSpoofingPreventionPortReOpen_Type(Integer32):
    """Custom type gs2328fARPSpoofingPreventionPortReOpen based on Integer32"""
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


_Gs2328fARPSpoofingPreventionPortReOpen_Type.__name__ = "Integer32"
_Gs2328fARPSpoofingPreventionPortReOpen_Object = MibTableColumn
gs2328fARPSpoofingPreventionPortReOpen = _Gs2328fARPSpoofingPreventionPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 7, 2, 1, 6),
    _Gs2328fARPSpoofingPreventionPortReOpen_Type()
)
gs2328fARPSpoofingPreventionPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPSpoofingPreventionPortReOpen.setStatus("current")
_Gs2328fARPIPDoSPrevention_ObjectIdentity = ObjectIdentity
gs2328fARPIPDoSPrevention = _Gs2328fARPIPDoSPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8)
)


class _Gs2328fARPIPDoSPreventionTCPMode_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionTCPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPIPDoSPreventionTCPMode_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionTCPMode_Object = MibScalar
gs2328fARPIPDoSPreventionTCPMode = _Gs2328fARPIPDoSPreventionTCPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 1),
    _Gs2328fARPIPDoSPreventionTCPMode_Type()
)
gs2328fARPIPDoSPreventionTCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionTCPMode.setStatus("current")


class _Gs2328fARPIPDoSPreventionUDPMode_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionUDPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPIPDoSPreventionUDPMode_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionUDPMode_Object = MibScalar
gs2328fARPIPDoSPreventionUDPMode = _Gs2328fARPIPDoSPreventionUDPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 2),
    _Gs2328fARPIPDoSPreventionUDPMode_Type()
)
gs2328fARPIPDoSPreventionUDPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionUDPMode.setStatus("current")


class _Gs2328fARPIPDoSPreventionICMPMode_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionICMPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fARPIPDoSPreventionICMPMode_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionICMPMode_Object = MibScalar
gs2328fARPIPDoSPreventionICMPMode = _Gs2328fARPIPDoSPreventionICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 3),
    _Gs2328fARPIPDoSPreventionICMPMode_Type()
)
gs2328fARPIPDoSPreventionICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionICMPMode.setStatus("current")


class _Gs2328fARPIPDoSPreventionServerPort1_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionServerPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328fARPIPDoSPreventionServerPort1_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionServerPort1_Object = MibScalar
gs2328fARPIPDoSPreventionServerPort1 = _Gs2328fARPIPDoSPreventionServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 4),
    _Gs2328fARPIPDoSPreventionServerPort1_Type()
)
gs2328fARPIPDoSPreventionServerPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionServerPort1.setStatus("current")


class _Gs2328fARPIPDoSPreventionServerPort2_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionServerPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328fARPIPDoSPreventionServerPort2_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionServerPort2_Object = MibScalar
gs2328fARPIPDoSPreventionServerPort2 = _Gs2328fARPIPDoSPreventionServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 5),
    _Gs2328fARPIPDoSPreventionServerPort2_Type()
)
gs2328fARPIPDoSPreventionServerPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionServerPort2.setStatus("current")


class _Gs2328fARPIPDoSPreventionServerPort3_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionServerPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328fARPIPDoSPreventionServerPort3_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionServerPort3_Object = MibScalar
gs2328fARPIPDoSPreventionServerPort3 = _Gs2328fARPIPDoSPreventionServerPort3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 6),
    _Gs2328fARPIPDoSPreventionServerPort3_Type()
)
gs2328fARPIPDoSPreventionServerPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionServerPort3.setStatus("current")


class _Gs2328fARPIPDoSPreventionServerPort4_Type(Integer32):
    """Custom type gs2328fARPIPDoSPreventionServerPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2328fARPIPDoSPreventionServerPort4_Type.__name__ = "Integer32"
_Gs2328fARPIPDoSPreventionServerPort4_Object = MibScalar
gs2328fARPIPDoSPreventionServerPort4 = _Gs2328fARPIPDoSPreventionServerPort4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 2, 8, 7),
    _Gs2328fARPIPDoSPreventionServerPort4_Type()
)
gs2328fARPIPDoSPreventionServerPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fARPIPDoSPreventionServerPort4.setStatus("current")
_Gs2328fDHCPSnooping_ObjectIdentity = ObjectIdentity
gs2328fDHCPSnooping = _Gs2328fDHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3)
)
_Gs2328fDHCPSnoopingConf_ObjectIdentity = ObjectIdentity
gs2328fDHCPSnoopingConf = _Gs2328fDHCPSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 1)
)


class _Gs2328fDHCPSnoopingMode_Type(Integer32):
    """Custom type gs2328fDHCPSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fDHCPSnoopingMode_Type.__name__ = "Integer32"
_Gs2328fDHCPSnoopingMode_Object = MibScalar
gs2328fDHCPSnoopingMode = _Gs2328fDHCPSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 1, 1),
    _Gs2328fDHCPSnoopingMode_Type()
)
gs2328fDHCPSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingMode.setStatus("current")
_Gs2328fDHCPSnoopingPortModeConfigurationTable_Object = MibTable
gs2328fDHCPSnoopingPortModeConfigurationTable = _Gs2328fDHCPSnoopingPortModeConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingPortModeConfigurationTable.setStatus("current")
_Gs2328fDHCPSnoopingPortModeConfigurationEntry_Object = MibTableRow
gs2328fDHCPSnoopingPortModeConfigurationEntry = _Gs2328fDHCPSnoopingPortModeConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 1, 2, 1)
)
gs2328fDHCPSnoopingPortModeConfigurationEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fDHCPSnoopingPortModeConfigurationPort"),
)
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingPortModeConfigurationEntry.setStatus("current")


class _Gs2328fDHCPSnoopingPortModeConfigurationPort_Type(Integer32):
    """Custom type gs2328fDHCPSnoopingPortModeConfigurationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fDHCPSnoopingPortModeConfigurationPort_Type.__name__ = "Integer32"
_Gs2328fDHCPSnoopingPortModeConfigurationPort_Object = MibTableColumn
gs2328fDHCPSnoopingPortModeConfigurationPort = _Gs2328fDHCPSnoopingPortModeConfigurationPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 1, 2, 1, 1),
    _Gs2328fDHCPSnoopingPortModeConfigurationPort_Type()
)
gs2328fDHCPSnoopingPortModeConfigurationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingPortModeConfigurationPort.setStatus("current")


class _Gs2328fDHCPSnoopingPortModeConfigurationMode_Type(Integer32):
    """Custom type gs2328fDHCPSnoopingPortModeConfigurationMode based on Integer32"""
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


_Gs2328fDHCPSnoopingPortModeConfigurationMode_Type.__name__ = "Integer32"
_Gs2328fDHCPSnoopingPortModeConfigurationMode_Object = MibTableColumn
gs2328fDHCPSnoopingPortModeConfigurationMode = _Gs2328fDHCPSnoopingPortModeConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 1, 2, 1, 2),
    _Gs2328fDHCPSnoopingPortModeConfigurationMode_Type()
)
gs2328fDHCPSnoopingPortModeConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingPortModeConfigurationMode.setStatus("current")
_Gs2328fDHCPSnoopingStatisticsTable_Object = MibTable
gs2328fDHCPSnoopingStatisticsTable = _Gs2328fDHCPSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingStatisticsTable.setStatus("current")
_Gs2328fDHCPSnoopingStatisticsEntry_Object = MibTableRow
gs2328fDHCPSnoopingStatisticsEntry = _Gs2328fDHCPSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1)
)
gs2328fDHCPSnoopingStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fDHCPSnoopingStatisticsPort"),
)
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingStatisticsEntry.setStatus("current")


class _Gs2328fDHCPSnoopingStatisticsPort_Type(Integer32):
    """Custom type gs2328fDHCPSnoopingStatisticsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fDHCPSnoopingStatisticsPort_Type.__name__ = "Integer32"
_Gs2328fDHCPSnoopingStatisticsPort_Object = MibTableColumn
gs2328fDHCPSnoopingStatisticsPort = _Gs2328fDHCPSnoopingStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 1),
    _Gs2328fDHCPSnoopingStatisticsPort_Type()
)
gs2328fDHCPSnoopingStatisticsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingStatisticsPort.setStatus("current")


class _Gs2328fDHCPSnoopingStatisticsClear_Type(Integer32):
    """Custom type gs2328fDHCPSnoopingStatisticsClear based on Integer32"""
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


_Gs2328fDHCPSnoopingStatisticsClear_Type.__name__ = "Integer32"
_Gs2328fDHCPSnoopingStatisticsClear_Object = MibTableColumn
gs2328fDHCPSnoopingStatisticsClear = _Gs2328fDHCPSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 2),
    _Gs2328fDHCPSnoopingStatisticsClear_Type()
)
gs2328fDHCPSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingStatisticsClear.setStatus("current")
_Gs2328fDHCPSnoopingRxDiscover_Type = Counter32
_Gs2328fDHCPSnoopingRxDiscover_Object = MibTableColumn
gs2328fDHCPSnoopingRxDiscover = _Gs2328fDHCPSnoopingRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 3),
    _Gs2328fDHCPSnoopingRxDiscover_Type()
)
gs2328fDHCPSnoopingRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxDiscover.setStatus("current")
_Gs2328fDHCPSnoopingRxOffer_Type = Counter32
_Gs2328fDHCPSnoopingRxOffer_Object = MibTableColumn
gs2328fDHCPSnoopingRxOffer = _Gs2328fDHCPSnoopingRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 4),
    _Gs2328fDHCPSnoopingRxOffer_Type()
)
gs2328fDHCPSnoopingRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxOffer.setStatus("current")
_Gs2328fDHCPSnoopingRxRequest_Type = Counter32
_Gs2328fDHCPSnoopingRxRequest_Object = MibTableColumn
gs2328fDHCPSnoopingRxRequest = _Gs2328fDHCPSnoopingRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 5),
    _Gs2328fDHCPSnoopingRxRequest_Type()
)
gs2328fDHCPSnoopingRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxRequest.setStatus("current")
_Gs2328fDHCPSnoopingRxDecline_Type = Counter32
_Gs2328fDHCPSnoopingRxDecline_Object = MibTableColumn
gs2328fDHCPSnoopingRxDecline = _Gs2328fDHCPSnoopingRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 6),
    _Gs2328fDHCPSnoopingRxDecline_Type()
)
gs2328fDHCPSnoopingRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxDecline.setStatus("current")
_Gs2328fDHCPSnoopingRxACK_Type = Counter32
_Gs2328fDHCPSnoopingRxACK_Object = MibTableColumn
gs2328fDHCPSnoopingRxACK = _Gs2328fDHCPSnoopingRxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 7),
    _Gs2328fDHCPSnoopingRxACK_Type()
)
gs2328fDHCPSnoopingRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxACK.setStatus("current")
_Gs2328fDHCPSnoopingRxNAK_Type = Counter32
_Gs2328fDHCPSnoopingRxNAK_Object = MibTableColumn
gs2328fDHCPSnoopingRxNAK = _Gs2328fDHCPSnoopingRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 8),
    _Gs2328fDHCPSnoopingRxNAK_Type()
)
gs2328fDHCPSnoopingRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxNAK.setStatus("current")
_Gs2328fDHCPSnoopingRxRelease_Type = Counter32
_Gs2328fDHCPSnoopingRxRelease_Object = MibTableColumn
gs2328fDHCPSnoopingRxRelease = _Gs2328fDHCPSnoopingRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 9),
    _Gs2328fDHCPSnoopingRxRelease_Type()
)
gs2328fDHCPSnoopingRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxRelease.setStatus("current")
_Gs2328fDHCPSnoopingRxInform_Type = Counter32
_Gs2328fDHCPSnoopingRxInform_Object = MibTableColumn
gs2328fDHCPSnoopingRxInform = _Gs2328fDHCPSnoopingRxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 10),
    _Gs2328fDHCPSnoopingRxInform_Type()
)
gs2328fDHCPSnoopingRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxInform.setStatus("current")
_Gs2328fDHCPSnoopingRxLeaseQuery_Type = Counter32
_Gs2328fDHCPSnoopingRxLeaseQuery_Object = MibTableColumn
gs2328fDHCPSnoopingRxLeaseQuery = _Gs2328fDHCPSnoopingRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 11),
    _Gs2328fDHCPSnoopingRxLeaseQuery_Type()
)
gs2328fDHCPSnoopingRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxLeaseQuery.setStatus("current")
_Gs2328fDHCPSnoopingRxLeaseUnassigned_Type = Counter32
_Gs2328fDHCPSnoopingRxLeaseUnassigned_Object = MibTableColumn
gs2328fDHCPSnoopingRxLeaseUnassigned = _Gs2328fDHCPSnoopingRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 12),
    _Gs2328fDHCPSnoopingRxLeaseUnassigned_Type()
)
gs2328fDHCPSnoopingRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxLeaseUnassigned.setStatus("current")
_Gs2328fDHCPSnoopingRxLeaseUnknown_Type = Counter32
_Gs2328fDHCPSnoopingRxLeaseUnknown_Object = MibTableColumn
gs2328fDHCPSnoopingRxLeaseUnknown = _Gs2328fDHCPSnoopingRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 13),
    _Gs2328fDHCPSnoopingRxLeaseUnknown_Type()
)
gs2328fDHCPSnoopingRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxLeaseUnknown.setStatus("current")
_Gs2328fDHCPSnoopingRxLeaseActive_Type = Counter32
_Gs2328fDHCPSnoopingRxLeaseActive_Object = MibTableColumn
gs2328fDHCPSnoopingRxLeaseActive = _Gs2328fDHCPSnoopingRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 14),
    _Gs2328fDHCPSnoopingRxLeaseActive_Type()
)
gs2328fDHCPSnoopingRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingRxLeaseActive.setStatus("current")
_Gs2328fDHCPSnoopingTxDiscover_Type = Counter32
_Gs2328fDHCPSnoopingTxDiscover_Object = MibTableColumn
gs2328fDHCPSnoopingTxDiscover = _Gs2328fDHCPSnoopingTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 15),
    _Gs2328fDHCPSnoopingTxDiscover_Type()
)
gs2328fDHCPSnoopingTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxDiscover.setStatus("current")
_Gs2328fDHCPSnoopingTxOffer_Type = Counter32
_Gs2328fDHCPSnoopingTxOffer_Object = MibTableColumn
gs2328fDHCPSnoopingTxOffer = _Gs2328fDHCPSnoopingTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 16),
    _Gs2328fDHCPSnoopingTxOffer_Type()
)
gs2328fDHCPSnoopingTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxOffer.setStatus("current")
_Gs2328fDHCPSnoopingTxRequest_Type = Counter32
_Gs2328fDHCPSnoopingTxRequest_Object = MibTableColumn
gs2328fDHCPSnoopingTxRequest = _Gs2328fDHCPSnoopingTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 17),
    _Gs2328fDHCPSnoopingTxRequest_Type()
)
gs2328fDHCPSnoopingTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxRequest.setStatus("current")
_Gs2328fDHCPSnoopingTxDecline_Type = Counter32
_Gs2328fDHCPSnoopingTxDecline_Object = MibTableColumn
gs2328fDHCPSnoopingTxDecline = _Gs2328fDHCPSnoopingTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 18),
    _Gs2328fDHCPSnoopingTxDecline_Type()
)
gs2328fDHCPSnoopingTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxDecline.setStatus("current")
_Gs2328fDHCPSnoopingTxACK_Type = Counter32
_Gs2328fDHCPSnoopingTxACK_Object = MibTableColumn
gs2328fDHCPSnoopingTxACK = _Gs2328fDHCPSnoopingTxACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 19),
    _Gs2328fDHCPSnoopingTxACK_Type()
)
gs2328fDHCPSnoopingTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxACK.setStatus("current")
_Gs2328fDHCPSnoopingTxNAK_Type = Counter32
_Gs2328fDHCPSnoopingTxNAK_Object = MibTableColumn
gs2328fDHCPSnoopingTxNAK = _Gs2328fDHCPSnoopingTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 20),
    _Gs2328fDHCPSnoopingTxNAK_Type()
)
gs2328fDHCPSnoopingTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxNAK.setStatus("current")
_Gs2328fDHCPSnoopingTxRelease_Type = Counter32
_Gs2328fDHCPSnoopingTxRelease_Object = MibTableColumn
gs2328fDHCPSnoopingTxRelease = _Gs2328fDHCPSnoopingTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 21),
    _Gs2328fDHCPSnoopingTxRelease_Type()
)
gs2328fDHCPSnoopingTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxRelease.setStatus("current")
_Gs2328fDHCPSnoopingTxInform_Type = Counter32
_Gs2328fDHCPSnoopingTxInform_Object = MibTableColumn
gs2328fDHCPSnoopingTxInform = _Gs2328fDHCPSnoopingTxInform_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 22),
    _Gs2328fDHCPSnoopingTxInform_Type()
)
gs2328fDHCPSnoopingTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxInform.setStatus("current")
_Gs2328fDHCPSnoopingTxLeaseQuery_Type = Counter32
_Gs2328fDHCPSnoopingTxLeaseQuery_Object = MibTableColumn
gs2328fDHCPSnoopingTxLeaseQuery = _Gs2328fDHCPSnoopingTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 23),
    _Gs2328fDHCPSnoopingTxLeaseQuery_Type()
)
gs2328fDHCPSnoopingTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxLeaseQuery.setStatus("current")
_Gs2328fDHCPSnoopingTxLeaseUnassigned_Type = Counter32
_Gs2328fDHCPSnoopingTxLeaseUnassigned_Object = MibTableColumn
gs2328fDHCPSnoopingTxLeaseUnassigned = _Gs2328fDHCPSnoopingTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 24),
    _Gs2328fDHCPSnoopingTxLeaseUnassigned_Type()
)
gs2328fDHCPSnoopingTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxLeaseUnassigned.setStatus("current")
_Gs2328fDHCPSnoopingTxLeaseUnknown_Type = Counter32
_Gs2328fDHCPSnoopingTxLeaseUnknown_Object = MibTableColumn
gs2328fDHCPSnoopingTxLeaseUnknown = _Gs2328fDHCPSnoopingTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 25),
    _Gs2328fDHCPSnoopingTxLeaseUnknown_Type()
)
gs2328fDHCPSnoopingTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxLeaseUnknown.setStatus("current")
_Gs2328fDHCPSnoopingTxLeaseActive_Type = Counter32
_Gs2328fDHCPSnoopingTxLeaseActive_Object = MibTableColumn
gs2328fDHCPSnoopingTxLeaseActive = _Gs2328fDHCPSnoopingTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 3, 2, 1, 26),
    _Gs2328fDHCPSnoopingTxLeaseActive_Type()
)
gs2328fDHCPSnoopingTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fDHCPSnoopingTxLeaseActive.setStatus("current")
_Gs2328fDHCPRelay_ObjectIdentity = ObjectIdentity
gs2328fDHCPRelay = _Gs2328fDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4)
)
_Gs2328fDHCPRelayConfiguration_ObjectIdentity = ObjectIdentity
gs2328fDHCPRelayConfiguration = _Gs2328fDHCPRelayConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1)
)


class _Gs2328fDHCPRelayMode_Type(Integer32):
    """Custom type gs2328fDHCPRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fDHCPRelayMode_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayMode_Object = MibScalar
gs2328fDHCPRelayMode = _Gs2328fDHCPRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 1),
    _Gs2328fDHCPRelayMode_Type()
)
gs2328fDHCPRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayMode.setStatus("current")
_Gs2328fDHCPRelayServer_Type = IpAddress
_Gs2328fDHCPRelayServer_Object = MibScalar
gs2328fDHCPRelayServer = _Gs2328fDHCPRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 2),
    _Gs2328fDHCPRelayServer_Type()
)
gs2328fDHCPRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayServer.setStatus("current")


class _Gs2328fDHCPRelayInformationMode_Type(Integer32):
    """Custom type gs2328fDHCPRelayInformationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fDHCPRelayInformationMode_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayInformationMode_Object = MibScalar
gs2328fDHCPRelayInformationMode = _Gs2328fDHCPRelayInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 3),
    _Gs2328fDHCPRelayInformationMode_Type()
)
gs2328fDHCPRelayInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayInformationMode.setStatus("current")


class _Gs2328fDHCPRelayInformationPolicy_Type(Integer32):
    """Custom type gs2328fDHCPRelayInformationPolicy based on Integer32"""
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


_Gs2328fDHCPRelayInformationPolicy_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayInformationPolicy_Object = MibScalar
gs2328fDHCPRelayInformationPolicy = _Gs2328fDHCPRelayInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 4),
    _Gs2328fDHCPRelayInformationPolicy_Type()
)
gs2328fDHCPRelayInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayInformationPolicy.setStatus("current")
_Gs2328fDHCPRelayConfigurationGateways_ObjectIdentity = ObjectIdentity
gs2328fDHCPRelayConfigurationGateways = _Gs2328fDHCPRelayConfigurationGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5)
)


class _Gs2328fDHCPRelayConfigurationGatewaysCreate_Type(Integer32):
    """Custom type gs2328fDHCPRelayConfigurationGatewaysCreate based on Integer32"""
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


_Gs2328fDHCPRelayConfigurationGatewaysCreate_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayConfigurationGatewaysCreate_Object = MibScalar
gs2328fDHCPRelayConfigurationGatewaysCreate = _Gs2328fDHCPRelayConfigurationGatewaysCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 1),
    _Gs2328fDHCPRelayConfigurationGatewaysCreate_Type()
)
gs2328fDHCPRelayConfigurationGatewaysCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysCreate.setStatus("current")
_Gs2328fDHCPRelayConfigurationGatewaysTable_Object = MibTable
gs2328fDHCPRelayConfigurationGatewaysTable = _Gs2328fDHCPRelayConfigurationGatewaysTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysTable.setStatus("current")
_Gs2328fDHCPRelayConfigurationGatewaysEntry_Object = MibTableRow
gs2328fDHCPRelayConfigurationGatewaysEntry = _Gs2328fDHCPRelayConfigurationGatewaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 2, 1)
)
gs2328fDHCPRelayConfigurationGatewaysEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fDHCPRelayConfigurationGatewaysIndex"),
)
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysEntry.setStatus("current")


class _Gs2328fDHCPRelayConfigurationGatewaysIndex_Type(Integer32):
    """Custom type gs2328fDHCPRelayConfigurationGatewaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2328fDHCPRelayConfigurationGatewaysIndex_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayConfigurationGatewaysIndex_Object = MibTableColumn
gs2328fDHCPRelayConfigurationGatewaysIndex = _Gs2328fDHCPRelayConfigurationGatewaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 2, 1, 1),
    _Gs2328fDHCPRelayConfigurationGatewaysIndex_Type()
)
gs2328fDHCPRelayConfigurationGatewaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysIndex.setStatus("current")


class _Gs2328fDHCPRelayConfigurationGatewaysVLANId_Type(Integer32):
    """Custom type gs2328fDHCPRelayConfigurationGatewaysVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fDHCPRelayConfigurationGatewaysVLANId_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayConfigurationGatewaysVLANId_Object = MibTableColumn
gs2328fDHCPRelayConfigurationGatewaysVLANId = _Gs2328fDHCPRelayConfigurationGatewaysVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 2, 1, 2),
    _Gs2328fDHCPRelayConfigurationGatewaysVLANId_Type()
)
gs2328fDHCPRelayConfigurationGatewaysVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysVLANId.setStatus("current")
_Gs2328fDHCPRelayConfigurationGatewaysIP_Type = IpAddress
_Gs2328fDHCPRelayConfigurationGatewaysIP_Object = MibTableColumn
gs2328fDHCPRelayConfigurationGatewaysIP = _Gs2328fDHCPRelayConfigurationGatewaysIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 2, 1, 3),
    _Gs2328fDHCPRelayConfigurationGatewaysIP_Type()
)
gs2328fDHCPRelayConfigurationGatewaysIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysIP.setStatus("current")


class _Gs2328fDHCPRelayConfigurationGatewaysRowStatus_Type(Integer32):
    """Custom type gs2328fDHCPRelayConfigurationGatewaysRowStatus based on Integer32"""
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


_Gs2328fDHCPRelayConfigurationGatewaysRowStatus_Type.__name__ = "Integer32"
_Gs2328fDHCPRelayConfigurationGatewaysRowStatus_Object = MibTableColumn
gs2328fDHCPRelayConfigurationGatewaysRowStatus = _Gs2328fDHCPRelayConfigurationGatewaysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 5, 2, 1, 4),
    _Gs2328fDHCPRelayConfigurationGatewaysRowStatus_Type()
)
gs2328fDHCPRelayConfigurationGatewaysRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayConfigurationGatewaysRowStatus.setStatus("current")


class _Gs2328fDHCPRelayInformationCustom_Type(DisplayString):
    """Custom type gs2328fDHCPRelayInformationCustom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Gs2328fDHCPRelayInformationCustom_Type.__name__ = "DisplayString"
_Gs2328fDHCPRelayInformationCustom_Object = MibScalar
gs2328fDHCPRelayInformationCustom = _Gs2328fDHCPRelayInformationCustom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 1, 1500),
    _Gs2328fDHCPRelayInformationCustom_Type()
)
gs2328fDHCPRelayInformationCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDHCPRelayInformationCustom.setStatus("current")
_Gs2328fDHCPRelayStatistics_ObjectIdentity = ObjectIdentity
gs2328fDHCPRelayStatistics = _Gs2328fDHCPRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2)
)
_Gs2328fDHCPRelayServerStatistics_ObjectIdentity = ObjectIdentity
gs2328fDHCPRelayServerStatistics = _Gs2328fDHCPRelayServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1)
)
_Gs2328fServerStatTransmitToServer_Type = Counter32
_Gs2328fServerStatTransmitToServer_Object = MibScalar
gs2328fServerStatTransmitToServer = _Gs2328fServerStatTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 1),
    _Gs2328fServerStatTransmitToServer_Type()
)
gs2328fServerStatTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatTransmitToServer.setStatus("current")
_Gs2328fServerStatTransmitError_Type = Counter32
_Gs2328fServerStatTransmitError_Object = MibScalar
gs2328fServerStatTransmitError = _Gs2328fServerStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 2),
    _Gs2328fServerStatTransmitError_Type()
)
gs2328fServerStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatTransmitError.setStatus("current")
_Gs2328fServerStatReceiveFromServer_Type = Counter32
_Gs2328fServerStatReceiveFromServer_Object = MibScalar
gs2328fServerStatReceiveFromServer = _Gs2328fServerStatReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 3),
    _Gs2328fServerStatReceiveFromServer_Type()
)
gs2328fServerStatReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatReceiveFromServer.setStatus("current")
_Gs2328fServerStatReceiveMissingAgentOption_Type = Counter32
_Gs2328fServerStatReceiveMissingAgentOption_Object = MibScalar
gs2328fServerStatReceiveMissingAgentOption = _Gs2328fServerStatReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 4),
    _Gs2328fServerStatReceiveMissingAgentOption_Type()
)
gs2328fServerStatReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatReceiveMissingAgentOption.setStatus("current")
_Gs2328fServerStatReceiveMissingCircuitID_Type = Counter32
_Gs2328fServerStatReceiveMissingCircuitID_Object = MibScalar
gs2328fServerStatReceiveMissingCircuitID = _Gs2328fServerStatReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 5),
    _Gs2328fServerStatReceiveMissingCircuitID_Type()
)
gs2328fServerStatReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatReceiveMissingCircuitID.setStatus("current")
_Gs2328fServerStatReceiveMissingRemoteID_Type = Counter32
_Gs2328fServerStatReceiveMissingRemoteID_Object = MibScalar
gs2328fServerStatReceiveMissingRemoteID = _Gs2328fServerStatReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 6),
    _Gs2328fServerStatReceiveMissingRemoteID_Type()
)
gs2328fServerStatReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatReceiveMissingRemoteID.setStatus("current")
_Gs2328fServerStatReceiveBadCircuitID_Type = Counter32
_Gs2328fServerStatReceiveBadCircuitID_Object = MibScalar
gs2328fServerStatReceiveBadCircuitID = _Gs2328fServerStatReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 7),
    _Gs2328fServerStatReceiveBadCircuitID_Type()
)
gs2328fServerStatReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatReceiveBadCircuitID.setStatus("current")
_Gs2328fServerStatReceiveBadRemoteID_Type = Counter32
_Gs2328fServerStatReceiveBadRemoteID_Object = MibScalar
gs2328fServerStatReceiveBadRemoteID = _Gs2328fServerStatReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 1, 8),
    _Gs2328fServerStatReceiveBadRemoteID_Type()
)
gs2328fServerStatReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fServerStatReceiveBadRemoteID.setStatus("current")
_Gs2328fDHCPRelayClientStatistics_ObjectIdentity = ObjectIdentity
gs2328fDHCPRelayClientStatistics = _Gs2328fDHCPRelayClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2)
)
_Gs2328fClientStatTransmitToClient_Type = Counter32
_Gs2328fClientStatTransmitToClient_Object = MibScalar
gs2328fClientStatTransmitToClient = _Gs2328fClientStatTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 1),
    _Gs2328fClientStatTransmitToClient_Type()
)
gs2328fClientStatTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatTransmitToClient.setStatus("current")
_Gs2328fClientStatTransmitError_Type = Counter32
_Gs2328fClientStatTransmitError_Object = MibScalar
gs2328fClientStatTransmitError = _Gs2328fClientStatTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 2),
    _Gs2328fClientStatTransmitError_Type()
)
gs2328fClientStatTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatTransmitError.setStatus("current")
_Gs2328fClientStatReceivefromClient_Type = Counter32
_Gs2328fClientStatReceivefromClient_Object = MibScalar
gs2328fClientStatReceivefromClient = _Gs2328fClientStatReceivefromClient_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 3),
    _Gs2328fClientStatReceivefromClient_Type()
)
gs2328fClientStatReceivefromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatReceivefromClient.setStatus("current")
_Gs2328fClientStatReceiveAgentOption_Type = Counter32
_Gs2328fClientStatReceiveAgentOption_Object = MibScalar
gs2328fClientStatReceiveAgentOption = _Gs2328fClientStatReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 4),
    _Gs2328fClientStatReceiveAgentOption_Type()
)
gs2328fClientStatReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatReceiveAgentOption.setStatus("current")
_Gs2328fClientStatReplaceAgentOption_Type = Counter32
_Gs2328fClientStatReplaceAgentOption_Object = MibScalar
gs2328fClientStatReplaceAgentOption = _Gs2328fClientStatReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 5),
    _Gs2328fClientStatReplaceAgentOption_Type()
)
gs2328fClientStatReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatReplaceAgentOption.setStatus("current")
_Gs2328fClientStatKeepAgentOption_Type = Counter32
_Gs2328fClientStatKeepAgentOption_Object = MibScalar
gs2328fClientStatKeepAgentOption = _Gs2328fClientStatKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 6),
    _Gs2328fClientStatKeepAgentOption_Type()
)
gs2328fClientStatKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatKeepAgentOption.setStatus("current")
_Gs2328fClientStatDropAgentOption_Type = Counter32
_Gs2328fClientStatDropAgentOption_Object = MibScalar
gs2328fClientStatDropAgentOption = _Gs2328fClientStatDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 4, 2, 2, 7),
    _Gs2328fClientStatDropAgentOption_Type()
)
gs2328fClientStatDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fClientStatDropAgentOption.setStatus("current")
_Gs2328fPortSecurity_ObjectIdentity = ObjectIdentity
gs2328fPortSecurity = _Gs2328fPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5)
)
_Gs2328fPortSecLimitCtrl_ObjectIdentity = ObjectIdentity
gs2328fPortSecLimitCtrl = _Gs2328fPortSecLimitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1)
)
_Gs2328fPortSecLimitCtrlSystemConf_ObjectIdentity = ObjectIdentity
gs2328fPortSecLimitCtrlSystemConf = _Gs2328fPortSecLimitCtrlSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 1)
)


class _Gs2328fPortSecurityMode_Type(Integer32):
    """Custom type gs2328fPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fPortSecurityMode_Type.__name__ = "Integer32"
_Gs2328fPortSecurityMode_Object = MibScalar
gs2328fPortSecurityMode = _Gs2328fPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 1, 1),
    _Gs2328fPortSecurityMode_Type()
)
gs2328fPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecurityMode.setStatus("current")


class _Gs2328fPortSecurityAging_Type(Integer32):
    """Custom type gs2328fPortSecurityAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fPortSecurityAging_Type.__name__ = "Integer32"
_Gs2328fPortSecurityAging_Object = MibScalar
gs2328fPortSecurityAging = _Gs2328fPortSecurityAging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 1, 2),
    _Gs2328fPortSecurityAging_Type()
)
gs2328fPortSecurityAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecurityAging.setStatus("current")


class _Gs2328fPortSecurityAgingPeriod_Type(Integer32):
    """Custom type gs2328fPortSecurityAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000000),
    )


_Gs2328fPortSecurityAgingPeriod_Type.__name__ = "Integer32"
_Gs2328fPortSecurityAgingPeriod_Object = MibScalar
gs2328fPortSecurityAgingPeriod = _Gs2328fPortSecurityAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 1, 3),
    _Gs2328fPortSecurityAgingPeriod_Type()
)
gs2328fPortSecurityAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecurityAgingPeriod.setStatus("current")
_Gs2328fPortSecLimitCtrlTable_Object = MibTable
gs2328fPortSecLimitCtrlTable = _Gs2328fPortSecLimitCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlTable.setStatus("current")
_Gs2328fPortSecLimitCtrlEntry_Object = MibTableRow
gs2328fPortSecLimitCtrlEntry = _Gs2328fPortSecLimitCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1)
)
gs2328fPortSecLimitCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fPortSecLimitCtrlPort"),
)
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlEntry.setStatus("current")


class _Gs2328fPortSecLimitCtrlPort_Type(Integer32):
    """Custom type gs2328fPortSecLimitCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortSecLimitCtrlPort_Type.__name__ = "Integer32"
_Gs2328fPortSecLimitCtrlPort_Object = MibTableColumn
gs2328fPortSecLimitCtrlPort = _Gs2328fPortSecLimitCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1, 1),
    _Gs2328fPortSecLimitCtrlPort_Type()
)
gs2328fPortSecLimitCtrlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlPort.setStatus("current")


class _Gs2328fPortSecLimitCtrlPortMode_Type(Integer32):
    """Custom type gs2328fPortSecLimitCtrlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fPortSecLimitCtrlPortMode_Type.__name__ = "Integer32"
_Gs2328fPortSecLimitCtrlPortMode_Object = MibTableColumn
gs2328fPortSecLimitCtrlPortMode = _Gs2328fPortSecLimitCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1, 2),
    _Gs2328fPortSecLimitCtrlPortMode_Type()
)
gs2328fPortSecLimitCtrlPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlPortMode.setStatus("current")


class _Gs2328fPortSecLimitCtrlPortLimit_Type(Integer32):
    """Custom type gs2328fPortSecLimitCtrlPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2328fPortSecLimitCtrlPortLimit_Type.__name__ = "Integer32"
_Gs2328fPortSecLimitCtrlPortLimit_Object = MibTableColumn
gs2328fPortSecLimitCtrlPortLimit = _Gs2328fPortSecLimitCtrlPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1, 3),
    _Gs2328fPortSecLimitCtrlPortLimit_Type()
)
gs2328fPortSecLimitCtrlPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlPortLimit.setStatus("current")


class _Gs2328fPortSecLimitCtrlPortAction_Type(Integer32):
    """Custom type gs2328fPortSecLimitCtrlPortAction based on Integer32"""
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


_Gs2328fPortSecLimitCtrlPortAction_Type.__name__ = "Integer32"
_Gs2328fPortSecLimitCtrlPortAction_Object = MibTableColumn
gs2328fPortSecLimitCtrlPortAction = _Gs2328fPortSecLimitCtrlPortAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1, 4),
    _Gs2328fPortSecLimitCtrlPortAction_Type()
)
gs2328fPortSecLimitCtrlPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlPortAction.setStatus("current")
_Gs2328fPortSecLimitCtrlPortState_Type = DisplayString
_Gs2328fPortSecLimitCtrlPortState_Object = MibTableColumn
gs2328fPortSecLimitCtrlPortState = _Gs2328fPortSecLimitCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1, 5),
    _Gs2328fPortSecLimitCtrlPortState_Type()
)
gs2328fPortSecLimitCtrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlPortState.setStatus("current")


class _Gs2328fPortSecLimitCtrlPortReOpen_Type(Integer32):
    """Custom type gs2328fPortSecLimitCtrlPortReOpen based on Integer32"""
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


_Gs2328fPortSecLimitCtrlPortReOpen_Type.__name__ = "Integer32"
_Gs2328fPortSecLimitCtrlPortReOpen_Object = MibTableColumn
gs2328fPortSecLimitCtrlPortReOpen = _Gs2328fPortSecLimitCtrlPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 1, 2, 1, 6),
    _Gs2328fPortSecLimitCtrlPortReOpen_Type()
)
gs2328fPortSecLimitCtrlPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecLimitCtrlPortReOpen.setStatus("current")
_Gs2328fPortSecSwitchStatusTable_Object = MibTable
gs2328fPortSecSwitchStatusTable = _Gs2328fPortSecSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusTable.setStatus("current")
_Gs2328fPortSecSwitchStatusEntry_Object = MibTableRow
gs2328fPortSecSwitchStatusEntry = _Gs2328fPortSecSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2, 1)
)
gs2328fPortSecSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fPortSecSwitchStatusPort"),
)
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusEntry.setStatus("current")


class _Gs2328fPortSecSwitchStatusPort_Type(Integer32):
    """Custom type gs2328fPortSecSwitchStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortSecSwitchStatusPort_Type.__name__ = "Integer32"
_Gs2328fPortSecSwitchStatusPort_Object = MibTableColumn
gs2328fPortSecSwitchStatusPort = _Gs2328fPortSecSwitchStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2, 1, 1),
    _Gs2328fPortSecSwitchStatusPort_Type()
)
gs2328fPortSecSwitchStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusPort.setStatus("current")
_Gs2328fPortSecSwitchStatusUsers_Type = DisplayString
_Gs2328fPortSecSwitchStatusUsers_Object = MibTableColumn
gs2328fPortSecSwitchStatusUsers = _Gs2328fPortSecSwitchStatusUsers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2, 1, 2),
    _Gs2328fPortSecSwitchStatusUsers_Type()
)
gs2328fPortSecSwitchStatusUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusUsers.setStatus("current")
_Gs2328fPortSecSwitchStatusState_Type = DisplayString
_Gs2328fPortSecSwitchStatusState_Object = MibTableColumn
gs2328fPortSecSwitchStatusState = _Gs2328fPortSecSwitchStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2, 1, 3),
    _Gs2328fPortSecSwitchStatusState_Type()
)
gs2328fPortSecSwitchStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusState.setStatus("current")


class _Gs2328fPortSecSwitchStatusMACCountCurrent_Type(Integer32):
    """Custom type gs2328fPortSecSwitchStatusMACCountCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortSecSwitchStatusMACCountCurrent_Type.__name__ = "Integer32"
_Gs2328fPortSecSwitchStatusMACCountCurrent_Object = MibTableColumn
gs2328fPortSecSwitchStatusMACCountCurrent = _Gs2328fPortSecSwitchStatusMACCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2, 1, 4),
    _Gs2328fPortSecSwitchStatusMACCountCurrent_Type()
)
gs2328fPortSecSwitchStatusMACCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusMACCountCurrent.setStatus("current")


class _Gs2328fPortSecSwitchStatusMACCountLimit_Type(Integer32):
    """Custom type gs2328fPortSecSwitchStatusMACCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortSecSwitchStatusMACCountLimit_Type.__name__ = "Integer32"
_Gs2328fPortSecSwitchStatusMACCountLimit_Object = MibTableColumn
gs2328fPortSecSwitchStatusMACCountLimit = _Gs2328fPortSecSwitchStatusMACCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 2, 1, 5),
    _Gs2328fPortSecSwitchStatusMACCountLimit_Type()
)
gs2328fPortSecSwitchStatusMACCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecSwitchStatusMACCountLimit.setStatus("current")
_Gs2328fPortSecPortStatus_ObjectIdentity = ObjectIdentity
gs2328fPortSecPortStatus = _Gs2328fPortSecPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3)
)


class _Gs2328fPortSecPortStatusPort_Type(Integer32):
    """Custom type gs2328fPortSecPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortSecPortStatusPort_Type.__name__ = "Integer32"
_Gs2328fPortSecPortStatusPort_Object = MibScalar
gs2328fPortSecPortStatusPort = _Gs2328fPortSecPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 1),
    _Gs2328fPortSecPortStatusPort_Type()
)
gs2328fPortSecPortStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusPort.setStatus("current")
_Gs2328fPortSecPortStatusTable_Object = MibTable
gs2328fPortSecPortStatusTable = _Gs2328fPortSecPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusTable.setStatus("current")
_Gs2328fPortSecPortStatusEntry_Object = MibTableRow
gs2328fPortSecPortStatusEntry = _Gs2328fPortSecPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1)
)
gs2328fPortSecPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fPortSecPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusEntry.setStatus("current")


class _Gs2328fPortSecPortStatusIndex_Type(Integer32):
    """Custom type gs2328fPortSecPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fPortSecPortStatusIndex_Type.__name__ = "Integer32"
_Gs2328fPortSecPortStatusIndex_Object = MibTableColumn
gs2328fPortSecPortStatusIndex = _Gs2328fPortSecPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1, 1),
    _Gs2328fPortSecPortStatusIndex_Type()
)
gs2328fPortSecPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusIndex.setStatus("current")
_Gs2328fPortSecPortStatusMACAddress_Type = MacAddress
_Gs2328fPortSecPortStatusMACAddress_Object = MibTableColumn
gs2328fPortSecPortStatusMACAddress = _Gs2328fPortSecPortStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1, 2),
    _Gs2328fPortSecPortStatusMACAddress_Type()
)
gs2328fPortSecPortStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusMACAddress.setStatus("current")


class _Gs2328fPortSecPortStatusVLANId_Type(Integer32):
    """Custom type gs2328fPortSecPortStatusVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fPortSecPortStatusVLANId_Type.__name__ = "Integer32"
_Gs2328fPortSecPortStatusVLANId_Object = MibTableColumn
gs2328fPortSecPortStatusVLANId = _Gs2328fPortSecPortStatusVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1, 3),
    _Gs2328fPortSecPortStatusVLANId_Type()
)
gs2328fPortSecPortStatusVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusVLANId.setStatus("current")
_Gs2328fPortSecPortStatusState_Type = DisplayString
_Gs2328fPortSecPortStatusState_Object = MibTableColumn
gs2328fPortSecPortStatusState = _Gs2328fPortSecPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1, 4),
    _Gs2328fPortSecPortStatusState_Type()
)
gs2328fPortSecPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusState.setStatus("current")
_Gs2328fPortSecPortStatusTimeOfAddition_Type = DisplayString
_Gs2328fPortSecPortStatusTimeOfAddition_Object = MibTableColumn
gs2328fPortSecPortStatusTimeOfAddition = _Gs2328fPortSecPortStatusTimeOfAddition_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1, 5),
    _Gs2328fPortSecPortStatusTimeOfAddition_Type()
)
gs2328fPortSecPortStatusTimeOfAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusTimeOfAddition.setStatus("current")
_Gs2328fPortSecPortStatusAgeAndHold_Type = DisplayString
_Gs2328fPortSecPortStatusAgeAndHold_Object = MibTableColumn
gs2328fPortSecPortStatusAgeAndHold = _Gs2328fPortSecPortStatusAgeAndHold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 5, 3, 2, 1, 6),
    _Gs2328fPortSecPortStatusAgeAndHold_Type()
)
gs2328fPortSecPortStatusAgeAndHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPortSecPortStatusAgeAndHold.setStatus("current")
_Gs2328fAccessManagement_ObjectIdentity = ObjectIdentity
gs2328fAccessManagement = _Gs2328fAccessManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6)
)
_Gs2328fAccessMgtConf_ObjectIdentity = ObjectIdentity
gs2328fAccessMgtConf = _Gs2328fAccessMgtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1)
)


class _Gs2328fAccessMgtConfMode_Type(Integer32):
    """Custom type gs2328fAccessMgtConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAccessMgtConfMode_Type.__name__ = "Integer32"
_Gs2328fAccessMgtConfMode_Object = MibScalar
gs2328fAccessMgtConfMode = _Gs2328fAccessMgtConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 1),
    _Gs2328fAccessMgtConfMode_Type()
)
gs2328fAccessMgtConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtConfMode.setStatus("current")


class _Gs2328fAccessMgtConfCreate_Type(Integer32):
    """Custom type gs2328fAccessMgtConfCreate based on Integer32"""
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


_Gs2328fAccessMgtConfCreate_Type.__name__ = "Integer32"
_Gs2328fAccessMgtConfCreate_Object = MibScalar
gs2328fAccessMgtConfCreate = _Gs2328fAccessMgtConfCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 2),
    _Gs2328fAccessMgtConfCreate_Type()
)
gs2328fAccessMgtConfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtConfCreate.setStatus("current")
_Gs2328fAccessMgtConfTable_Object = MibTable
gs2328fAccessMgtConfTable = _Gs2328fAccessMgtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    gs2328fAccessMgtConfTable.setStatus("current")
_Gs2328fAccessMgtConfEntry_Object = MibTableRow
gs2328fAccessMgtConfEntry = _Gs2328fAccessMgtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1)
)
gs2328fAccessMgtConfEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fAccessMgtIndex"),
)
if mibBuilder.loadTexts:
    gs2328fAccessMgtConfEntry.setStatus("current")


class _Gs2328fAccessMgtIndex_Type(Integer32):
    """Custom type gs2328fAccessMgtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2328fAccessMgtIndex_Type.__name__ = "Integer32"
_Gs2328fAccessMgtIndex_Object = MibTableColumn
gs2328fAccessMgtIndex = _Gs2328fAccessMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 1),
    _Gs2328fAccessMgtIndex_Type()
)
gs2328fAccessMgtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtIndex.setStatus("current")


class _Gs2328fAccessMgtAddresstype_Type(Integer32):
    """Custom type gs2328fAccessMgtAddresstype based on Integer32"""
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


_Gs2328fAccessMgtAddresstype_Type.__name__ = "Integer32"
_Gs2328fAccessMgtAddresstype_Object = MibTableColumn
gs2328fAccessMgtAddresstype = _Gs2328fAccessMgtAddresstype_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 2),
    _Gs2328fAccessMgtAddresstype_Type()
)
gs2328fAccessMgtAddresstype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtAddresstype.setStatus("current")
_Gs2328fAccessMgtStartIpAddress_Type = DisplayString
_Gs2328fAccessMgtStartIpAddress_Object = MibTableColumn
gs2328fAccessMgtStartIpAddress = _Gs2328fAccessMgtStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 3),
    _Gs2328fAccessMgtStartIpAddress_Type()
)
gs2328fAccessMgtStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtStartIpAddress.setStatus("current")
_Gs2328fAccessMgtEndIpAddress_Type = DisplayString
_Gs2328fAccessMgtEndIpAddress_Object = MibTableColumn
gs2328fAccessMgtEndIpAddress = _Gs2328fAccessMgtEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 4),
    _Gs2328fAccessMgtEndIpAddress_Type()
)
gs2328fAccessMgtEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtEndIpAddress.setStatus("current")


class _Gs2328fAccessMgtHttpHttps_Type(Integer32):
    """Custom type gs2328fAccessMgtHttpHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAccessMgtHttpHttps_Type.__name__ = "Integer32"
_Gs2328fAccessMgtHttpHttps_Object = MibTableColumn
gs2328fAccessMgtHttpHttps = _Gs2328fAccessMgtHttpHttps_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 5),
    _Gs2328fAccessMgtHttpHttps_Type()
)
gs2328fAccessMgtHttpHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtHttpHttps.setStatus("current")


class _Gs2328fAccessMgtSNMP_Type(Integer32):
    """Custom type gs2328fAccessMgtSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAccessMgtSNMP_Type.__name__ = "Integer32"
_Gs2328fAccessMgtSNMP_Object = MibTableColumn
gs2328fAccessMgtSNMP = _Gs2328fAccessMgtSNMP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 6),
    _Gs2328fAccessMgtSNMP_Type()
)
gs2328fAccessMgtSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtSNMP.setStatus("current")


class _Gs2328fAccessMgtTelnetSSH_Type(Integer32):
    """Custom type gs2328fAccessMgtTelnetSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAccessMgtTelnetSSH_Type.__name__ = "Integer32"
_Gs2328fAccessMgtTelnetSSH_Object = MibTableColumn
gs2328fAccessMgtTelnetSSH = _Gs2328fAccessMgtTelnetSSH_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 7),
    _Gs2328fAccessMgtTelnetSSH_Type()
)
gs2328fAccessMgtTelnetSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtTelnetSSH.setStatus("current")


class _Gs2328fAccessMgtRowStatus_Type(Integer32):
    """Custom type gs2328fAccessMgtRowStatus based on Integer32"""
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


_Gs2328fAccessMgtRowStatus_Type.__name__ = "Integer32"
_Gs2328fAccessMgtRowStatus_Object = MibTableColumn
gs2328fAccessMgtRowStatus = _Gs2328fAccessMgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 1, 3, 1, 8),
    _Gs2328fAccessMgtRowStatus_Type()
)
gs2328fAccessMgtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtRowStatus.setStatus("current")
_Gs2328fAccessMgtStatistics_ObjectIdentity = ObjectIdentity
gs2328fAccessMgtStatistics = _Gs2328fAccessMgtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2)
)
_Gs2328fHttpReceivedPkts_Type = Counter32
_Gs2328fHttpReceivedPkts_Object = MibScalar
gs2328fHttpReceivedPkts = _Gs2328fHttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 1),
    _Gs2328fHttpReceivedPkts_Type()
)
gs2328fHttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHttpReceivedPkts.setStatus("current")
_Gs2328fHttpAllowedPkts_Type = Counter32
_Gs2328fHttpAllowedPkts_Object = MibScalar
gs2328fHttpAllowedPkts = _Gs2328fHttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 2),
    _Gs2328fHttpAllowedPkts_Type()
)
gs2328fHttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHttpAllowedPkts.setStatus("current")
_Gs2328fHttpDiscardedPkts_Type = Counter32
_Gs2328fHttpDiscardedPkts_Object = MibScalar
gs2328fHttpDiscardedPkts = _Gs2328fHttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 3),
    _Gs2328fHttpDiscardedPkts_Type()
)
gs2328fHttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHttpDiscardedPkts.setStatus("current")
_Gs2328fHttpsReceivedPkts_Type = Counter32
_Gs2328fHttpsReceivedPkts_Object = MibScalar
gs2328fHttpsReceivedPkts = _Gs2328fHttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 4),
    _Gs2328fHttpsReceivedPkts_Type()
)
gs2328fHttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHttpsReceivedPkts.setStatus("current")
_Gs2328fHttpsAllowedPkts_Type = Counter32
_Gs2328fHttpsAllowedPkts_Object = MibScalar
gs2328fHttpsAllowedPkts = _Gs2328fHttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 5),
    _Gs2328fHttpsAllowedPkts_Type()
)
gs2328fHttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHttpsAllowedPkts.setStatus("current")
_Gs2328fHttpsDiscardedPkts_Type = Counter32
_Gs2328fHttpsDiscardedPkts_Object = MibScalar
gs2328fHttpsDiscardedPkts = _Gs2328fHttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 6),
    _Gs2328fHttpsDiscardedPkts_Type()
)
gs2328fHttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fHttpsDiscardedPkts.setStatus("current")
_Gs2328fSnmpReceivedPkts_Type = Counter32
_Gs2328fSnmpReceivedPkts_Object = MibScalar
gs2328fSnmpReceivedPkts = _Gs2328fSnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 7),
    _Gs2328fSnmpReceivedPkts_Type()
)
gs2328fSnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSnmpReceivedPkts.setStatus("current")
_Gs2328fSnmpAllowedPkts_Type = Counter32
_Gs2328fSnmpAllowedPkts_Object = MibScalar
gs2328fSnmpAllowedPkts = _Gs2328fSnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 8),
    _Gs2328fSnmpAllowedPkts_Type()
)
gs2328fSnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSnmpAllowedPkts.setStatus("current")
_Gs2328fSnmpDiscardedPkts_Type = Counter32
_Gs2328fSnmpDiscardedPkts_Object = MibScalar
gs2328fSnmpDiscardedPkts = _Gs2328fSnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 9),
    _Gs2328fSnmpDiscardedPkts_Type()
)
gs2328fSnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSnmpDiscardedPkts.setStatus("current")
_Gs2328fTelnetReceivedPkts_Type = Counter32
_Gs2328fTelnetReceivedPkts_Object = MibScalar
gs2328fTelnetReceivedPkts = _Gs2328fTelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 10),
    _Gs2328fTelnetReceivedPkts_Type()
)
gs2328fTelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fTelnetReceivedPkts.setStatus("current")
_Gs2328fTelnetAllowedPkts_Type = Counter32
_Gs2328fTelnetAllowedPkts_Object = MibScalar
gs2328fTelnetAllowedPkts = _Gs2328fTelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 11),
    _Gs2328fTelnetAllowedPkts_Type()
)
gs2328fTelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fTelnetAllowedPkts.setStatus("current")
_Gs2328fTelnetDiscardedPkts_Type = Counter32
_Gs2328fTelnetDiscardedPkts_Object = MibScalar
gs2328fTelnetDiscardedPkts = _Gs2328fTelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 12),
    _Gs2328fTelnetDiscardedPkts_Type()
)
gs2328fTelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fTelnetDiscardedPkts.setStatus("current")
_Gs2328fSSHReceivedPkts_Type = Counter32
_Gs2328fSSHReceivedPkts_Object = MibScalar
gs2328fSSHReceivedPkts = _Gs2328fSSHReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 13),
    _Gs2328fSSHReceivedPkts_Type()
)
gs2328fSSHReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSSHReceivedPkts.setStatus("current")
_Gs2328fSSHAllowedPkts_Type = Counter32
_Gs2328fSSHAllowedPkts_Object = MibScalar
gs2328fSSHAllowedPkts = _Gs2328fSSHAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 14),
    _Gs2328fSSHAllowedPkts_Type()
)
gs2328fSSHAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSSHAllowedPkts.setStatus("current")
_Gs2328fSSHDiscardedPkts_Type = Counter32
_Gs2328fSSHDiscardedPkts_Object = MibScalar
gs2328fSSHDiscardedPkts = _Gs2328fSSHDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 15),
    _Gs2328fSSHDiscardedPkts_Type()
)
gs2328fSSHDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fSSHDiscardedPkts.setStatus("current")


class _Gs2328fAccessMgtStatisticsClearAll_Type(Integer32):
    """Custom type gs2328fAccessMgtStatisticsClearAll based on Integer32"""
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


_Gs2328fAccessMgtStatisticsClearAll_Type.__name__ = "Integer32"
_Gs2328fAccessMgtStatisticsClearAll_Object = MibScalar
gs2328fAccessMgtStatisticsClearAll = _Gs2328fAccessMgtStatisticsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 6, 2, 16),
    _Gs2328fAccessMgtStatisticsClearAll_Type()
)
gs2328fAccessMgtStatisticsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAccessMgtStatisticsClearAll.setStatus("current")
_Gs2328fSSH_ObjectIdentity = ObjectIdentity
gs2328fSSH = _Gs2328fSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 7)
)


class _Gs2328fSSHMode_Type(Integer32):
    """Custom type gs2328fSSHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSSHMode_Type.__name__ = "Integer32"
_Gs2328fSSHMode_Object = MibScalar
gs2328fSSHMode = _Gs2328fSSHMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 7, 1),
    _Gs2328fSSHMode_Type()
)
gs2328fSSHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSSHMode.setStatus("current")
_Gs2328fHTTPS_ObjectIdentity = ObjectIdentity
gs2328fHTTPS = _Gs2328fHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 8)
)


class _Gs2328fHTTPSMode_Type(Integer32):
    """Custom type gs2328fHTTPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fHTTPSMode_Type.__name__ = "Integer32"
_Gs2328fHTTPSMode_Object = MibScalar
gs2328fHTTPSMode = _Gs2328fHTTPSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 8, 1),
    _Gs2328fHTTPSMode_Type()
)
gs2328fHTTPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHTTPSMode.setStatus("current")


class _Gs2328fHTTPSAutoRedirect_Type(Integer32):
    """Custom type gs2328fHTTPSAutoRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fHTTPSAutoRedirect_Type.__name__ = "Integer32"
_Gs2328fHTTPSAutoRedirect_Object = MibScalar
gs2328fHTTPSAutoRedirect = _Gs2328fHTTPSAutoRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 8, 2),
    _Gs2328fHTTPSAutoRedirect_Type()
)
gs2328fHTTPSAutoRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHTTPSAutoRedirect.setStatus("current")


class _Gs2328fHTTPSCertRenew_Type(Integer32):
    """Custom type gs2328fHTTPSCertRenew based on Integer32"""
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


_Gs2328fHTTPSCertRenew_Type.__name__ = "Integer32"
_Gs2328fHTTPSCertRenew_Object = MibScalar
gs2328fHTTPSCertRenew = _Gs2328fHTTPSCertRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 8, 3),
    _Gs2328fHTTPSCertRenew_Type()
)
gs2328fHTTPSCertRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHTTPSCertRenew.setStatus("current")


class _Gs2328fHTTPSMinProtoVersion_Type(Integer32):
    """Custom type gs2328fHTTPSMinProtoVersion based on Integer32"""
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


_Gs2328fHTTPSMinProtoVersion_Type.__name__ = "Integer32"
_Gs2328fHTTPSMinProtoVersion_Object = MibScalar
gs2328fHTTPSMinProtoVersion = _Gs2328fHTTPSMinProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 8, 4),
    _Gs2328fHTTPSMinProtoVersion_Type()
)
gs2328fHTTPSMinProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHTTPSMinProtoVersion.setStatus("current")


class _Gs2328fHTTPMode_Type(Integer32):
    """Custom type gs2328fHTTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fHTTPMode_Type.__name__ = "Integer32"
_Gs2328fHTTPMode_Object = MibScalar
gs2328fHTTPMode = _Gs2328fHTTPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 8, 5),
    _Gs2328fHTTPMode_Type()
)
gs2328fHTTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHTTPMode.setStatus("current")
_Gs2328fAuthMethod_ObjectIdentity = ObjectIdentity
gs2328fAuthMethod = _Gs2328fAuthMethod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9)
)


class _Gs2328fConsoleAuthMethod_Type(Integer32):
    """Custom type gs2328fConsoleAuthMethod based on Integer32"""
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


_Gs2328fConsoleAuthMethod_Type.__name__ = "Integer32"
_Gs2328fConsoleAuthMethod_Object = MibScalar
gs2328fConsoleAuthMethod = _Gs2328fConsoleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 1),
    _Gs2328fConsoleAuthMethod_Type()
)
gs2328fConsoleAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fConsoleAuthMethod.setStatus("current")


class _Gs2328fConsoleFallback_Type(Integer32):
    """Custom type gs2328fConsoleFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fConsoleFallback_Type.__name__ = "Integer32"
_Gs2328fConsoleFallback_Object = MibScalar
gs2328fConsoleFallback = _Gs2328fConsoleFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 2),
    _Gs2328fConsoleFallback_Type()
)
gs2328fConsoleFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fConsoleFallback.setStatus("current")


class _Gs2328fTelnetAuthMethod_Type(Integer32):
    """Custom type gs2328fTelnetAuthMethod based on Integer32"""
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


_Gs2328fTelnetAuthMethod_Type.__name__ = "Integer32"
_Gs2328fTelnetAuthMethod_Object = MibScalar
gs2328fTelnetAuthMethod = _Gs2328fTelnetAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 3),
    _Gs2328fTelnetAuthMethod_Type()
)
gs2328fTelnetAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTelnetAuthMethod.setStatus("current")


class _Gs2328fTelnetFallback_Type(Integer32):
    """Custom type gs2328fTelnetFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fTelnetFallback_Type.__name__ = "Integer32"
_Gs2328fTelnetFallback_Object = MibScalar
gs2328fTelnetFallback = _Gs2328fTelnetFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 4),
    _Gs2328fTelnetFallback_Type()
)
gs2328fTelnetFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTelnetFallback.setStatus("current")


class _Gs2328fSshAuthMethod_Type(Integer32):
    """Custom type gs2328fSshAuthMethod based on Integer32"""
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


_Gs2328fSshAuthMethod_Type.__name__ = "Integer32"
_Gs2328fSshAuthMethod_Object = MibScalar
gs2328fSshAuthMethod = _Gs2328fSshAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 5),
    _Gs2328fSshAuthMethod_Type()
)
gs2328fSshAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSshAuthMethod.setStatus("current")


class _Gs2328fSshFallback_Type(Integer32):
    """Custom type gs2328fSshFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fSshFallback_Type.__name__ = "Integer32"
_Gs2328fSshFallback_Object = MibScalar
gs2328fSshFallback = _Gs2328fSshFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 6),
    _Gs2328fSshFallback_Type()
)
gs2328fSshFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSshFallback.setStatus("current")


class _Gs2328fTftpAuthMethod_Type(Integer32):
    """Custom type gs2328fTftpAuthMethod based on Integer32"""
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


_Gs2328fTftpAuthMethod_Type.__name__ = "Integer32"
_Gs2328fTftpAuthMethod_Object = MibScalar
gs2328fTftpAuthMethod = _Gs2328fTftpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 9),
    _Gs2328fTftpAuthMethod_Type()
)
gs2328fTftpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTftpAuthMethod.setStatus("current")


class _Gs2328fTftpFallback_Type(Integer32):
    """Custom type gs2328fTftpFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fTftpFallback_Type.__name__ = "Integer32"
_Gs2328fTftpFallback_Object = MibScalar
gs2328fTftpFallback = _Gs2328fTftpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 10),
    _Gs2328fTftpFallback_Type()
)
gs2328fTftpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTftpFallback.setStatus("current")


class _Gs2328fLoginFailures_Type(Integer32):
    """Custom type gs2328fLoginFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Gs2328fLoginFailures_Type.__name__ = "Integer32"
_Gs2328fLoginFailures_Object = MibScalar
gs2328fLoginFailures = _Gs2328fLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 11),
    _Gs2328fLoginFailures_Type()
)
gs2328fLoginFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLoginFailures.setStatus("current")


class _Gs2328fLockMinutes_Type(Integer32):
    """Custom type gs2328fLockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Gs2328fLockMinutes_Type.__name__ = "Integer32"
_Gs2328fLockMinutes_Object = MibScalar
gs2328fLockMinutes = _Gs2328fLockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 12),
    _Gs2328fLockMinutes_Type()
)
gs2328fLockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fLockMinutes.setStatus("current")


class _Gs2328fHttpAuthMethod_Type(Integer32):
    """Custom type gs2328fHttpAuthMethod based on Integer32"""
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


_Gs2328fHttpAuthMethod_Type.__name__ = "Integer32"
_Gs2328fHttpAuthMethod_Object = MibScalar
gs2328fHttpAuthMethod = _Gs2328fHttpAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 13),
    _Gs2328fHttpAuthMethod_Type()
)
gs2328fHttpAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHttpAuthMethod.setStatus("current")


class _Gs2328fHttpFallback_Type(Integer32):
    """Custom type gs2328fHttpFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fHttpFallback_Type.__name__ = "Integer32"
_Gs2328fHttpFallback_Object = MibScalar
gs2328fHttpFallback = _Gs2328fHttpFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 14),
    _Gs2328fHttpFallback_Type()
)
gs2328fHttpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHttpFallback.setStatus("current")


class _Gs2328fHttpsAuthMethod_Type(Integer32):
    """Custom type gs2328fHttpsAuthMethod based on Integer32"""
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


_Gs2328fHttpsAuthMethod_Type.__name__ = "Integer32"
_Gs2328fHttpsAuthMethod_Object = MibScalar
gs2328fHttpsAuthMethod = _Gs2328fHttpsAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 15),
    _Gs2328fHttpsAuthMethod_Type()
)
gs2328fHttpsAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHttpsAuthMethod.setStatus("current")


class _Gs2328fHttpsFallback_Type(Integer32):
    """Custom type gs2328fHttpsFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fHttpsFallback_Type.__name__ = "Integer32"
_Gs2328fHttpsFallback_Object = MibScalar
gs2328fHttpsFallback = _Gs2328fHttpsFallback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 9, 16),
    _Gs2328fHttpsFallback_Type()
)
gs2328fHttpsFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fHttpsFallback.setStatus("current")
_Gs2328fAAA_ObjectIdentity = ObjectIdentity
gs2328fAAA = _Gs2328fAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10)
)
_Gs2328fAAACommonServer_ObjectIdentity = ObjectIdentity
gs2328fAAACommonServer = _Gs2328fAAACommonServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 1)
)


class _Gs2328fAAACommonServerTimeout_Type(Integer32):
    """Custom type gs2328fAAACommonServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_Gs2328fAAACommonServerTimeout_Type.__name__ = "Integer32"
_Gs2328fAAACommonServerTimeout_Object = MibScalar
gs2328fAAACommonServerTimeout = _Gs2328fAAACommonServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 1, 1),
    _Gs2328fAAACommonServerTimeout_Type()
)
gs2328fAAACommonServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAAACommonServerTimeout.setStatus("current")


class _Gs2328fAAACommonServerDeadTime_Type(Integer32):
    """Custom type gs2328fAAACommonServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Gs2328fAAACommonServerDeadTime_Type.__name__ = "Integer32"
_Gs2328fAAACommonServerDeadTime_Object = MibScalar
gs2328fAAACommonServerDeadTime = _Gs2328fAAACommonServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 1, 2),
    _Gs2328fAAACommonServerDeadTime_Type()
)
gs2328fAAACommonServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAAACommonServerDeadTime.setStatus("current")
_Gs2328fAAATACACSPlusAuthAndAccounting_ObjectIdentity = ObjectIdentity
gs2328fAAATACACSPlusAuthAndAccounting = _Gs2328fAAATACACSPlusAuthAndAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 2)
)


class _Gs2328fAAAAuthorization_Type(Integer32):
    """Custom type gs2328fAAAAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAAAAuthorization_Type.__name__ = "Integer32"
_Gs2328fAAAAuthorization_Object = MibScalar
gs2328fAAAAuthorization = _Gs2328fAAAAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 2, 1),
    _Gs2328fAAAAuthorization_Type()
)
gs2328fAAAAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAAAAuthorization.setStatus("current")


class _Gs2328fAAAFallbackToLocalAuthorization_Type(Integer32):
    """Custom type gs2328fAAAFallbackToLocalAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAAAFallbackToLocalAuthorization_Type.__name__ = "Integer32"
_Gs2328fAAAFallbackToLocalAuthorization_Object = MibScalar
gs2328fAAAFallbackToLocalAuthorization = _Gs2328fAAAFallbackToLocalAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 2, 2),
    _Gs2328fAAAFallbackToLocalAuthorization_Type()
)
gs2328fAAAFallbackToLocalAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAAAFallbackToLocalAuthorization.setStatus("current")


class _Gs2328fAAAAccounting_Type(Integer32):
    """Custom type gs2328fAAAAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fAAAAccounting_Type.__name__ = "Integer32"
_Gs2328fAAAAccounting_Object = MibScalar
gs2328fAAAAccounting = _Gs2328fAAAAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 2, 3),
    _Gs2328fAAAAccounting_Type()
)
gs2328fAAAAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fAAAAccounting.setStatus("current")
_Gs2328fRADIUSAuthenticationServerTable_Object = MibTable
gs2328fRADIUSAuthenticationServerTable = _Gs2328fRADIUSAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3)
)
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerTable.setStatus("current")
_Gs2328fRADIUSAuthenticationServerEntry_Object = MibTableRow
gs2328fRADIUSAuthenticationServerEntry = _Gs2328fRADIUSAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3, 1)
)
gs2328fRADIUSAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fRADIUSAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerEntry.setStatus("current")


class _Gs2328fRADIUSAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2328fRADIUSAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328fRADIUSAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2328fRADIUSAuthenticationServerIndex_Object = MibTableColumn
gs2328fRADIUSAuthenticationServerIndex = _Gs2328fRADIUSAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3, 1, 1),
    _Gs2328fRADIUSAuthenticationServerIndex_Type()
)
gs2328fRADIUSAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerIndex.setStatus("current")


class _Gs2328fRADIUSAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2328fRADIUSAuthenticationServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fRADIUSAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2328fRADIUSAuthenticationServerEnable_Object = MibTableColumn
gs2328fRADIUSAuthenticationServerEnable = _Gs2328fRADIUSAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3, 1, 2),
    _Gs2328fRADIUSAuthenticationServerEnable_Type()
)
gs2328fRADIUSAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerEnable.setStatus("current")
_Gs2328fRADIUSAuthenticationServerIP_Type = DisplayString
_Gs2328fRADIUSAuthenticationServerIP_Object = MibTableColumn
gs2328fRADIUSAuthenticationServerIP = _Gs2328fRADIUSAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3, 1, 3),
    _Gs2328fRADIUSAuthenticationServerIP_Type()
)
gs2328fRADIUSAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerIP.setStatus("current")


class _Gs2328fRADIUSAuthenticationServerPort_Type(Integer32):
    """Custom type gs2328fRADIUSAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328fRADIUSAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2328fRADIUSAuthenticationServerPort_Object = MibTableColumn
gs2328fRADIUSAuthenticationServerPort = _Gs2328fRADIUSAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3, 1, 4),
    _Gs2328fRADIUSAuthenticationServerPort_Type()
)
gs2328fRADIUSAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerPort.setStatus("current")
_Gs2328fRADIUSAuthenticationServerSecret_Type = DisplayString
_Gs2328fRADIUSAuthenticationServerSecret_Object = MibTableColumn
gs2328fRADIUSAuthenticationServerSecret = _Gs2328fRADIUSAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 3, 1, 5),
    _Gs2328fRADIUSAuthenticationServerSecret_Type()
)
gs2328fRADIUSAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthenticationServerSecret.setStatus("current")
_Gs2328fRADIUSAccountingServerTable_Object = MibTable
gs2328fRADIUSAccountingServerTable = _Gs2328fRADIUSAccountingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4)
)
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerTable.setStatus("current")
_Gs2328fRADIUSAccountingServerEntry_Object = MibTableRow
gs2328fRADIUSAccountingServerEntry = _Gs2328fRADIUSAccountingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4, 1)
)
gs2328fRADIUSAccountingServerEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fRADIUSAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerEntry.setStatus("current")


class _Gs2328fRADIUSAccountingServerIndex_Type(Integer32):
    """Custom type gs2328fRADIUSAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328fRADIUSAccountingServerIndex_Type.__name__ = "Integer32"
_Gs2328fRADIUSAccountingServerIndex_Object = MibTableColumn
gs2328fRADIUSAccountingServerIndex = _Gs2328fRADIUSAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4, 1, 1),
    _Gs2328fRADIUSAccountingServerIndex_Type()
)
gs2328fRADIUSAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerIndex.setStatus("current")


class _Gs2328fRADIUSAccountingServerEnable_Type(Integer32):
    """Custom type gs2328fRADIUSAccountingServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fRADIUSAccountingServerEnable_Type.__name__ = "Integer32"
_Gs2328fRADIUSAccountingServerEnable_Object = MibTableColumn
gs2328fRADIUSAccountingServerEnable = _Gs2328fRADIUSAccountingServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4, 1, 2),
    _Gs2328fRADIUSAccountingServerEnable_Type()
)
gs2328fRADIUSAccountingServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerEnable.setStatus("current")
_Gs2328fRADIUSAccountingServerIP_Type = DisplayString
_Gs2328fRADIUSAccountingServerIP_Object = MibTableColumn
gs2328fRADIUSAccountingServerIP = _Gs2328fRADIUSAccountingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4, 1, 3),
    _Gs2328fRADIUSAccountingServerIP_Type()
)
gs2328fRADIUSAccountingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerIP.setStatus("current")


class _Gs2328fRADIUSAccountingServerPort_Type(Integer32):
    """Custom type gs2328fRADIUSAccountingServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328fRADIUSAccountingServerPort_Type.__name__ = "Integer32"
_Gs2328fRADIUSAccountingServerPort_Object = MibTableColumn
gs2328fRADIUSAccountingServerPort = _Gs2328fRADIUSAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4, 1, 4),
    _Gs2328fRADIUSAccountingServerPort_Type()
)
gs2328fRADIUSAccountingServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerPort.setStatus("current")
_Gs2328fRADIUSAccountingServerSecret_Type = DisplayString
_Gs2328fRADIUSAccountingServerSecret_Object = MibTableColumn
gs2328fRADIUSAccountingServerSecret = _Gs2328fRADIUSAccountingServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 4, 1, 5),
    _Gs2328fRADIUSAccountingServerSecret_Type()
)
gs2328fRADIUSAccountingServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingServerSecret.setStatus("current")
_Gs2328fTACACSPlusAuthenticationServerTable_Object = MibTable
gs2328fTACACSPlusAuthenticationServerTable = _Gs2328fTACACSPlusAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5)
)
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerTable.setStatus("current")
_Gs2328fTACACSPlusAuthenticationServerEntry_Object = MibTableRow
gs2328fTACACSPlusAuthenticationServerEntry = _Gs2328fTACACSPlusAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5, 1)
)
gs2328fTACACSPlusAuthenticationServerEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fTACACSPlusAuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerEntry.setStatus("current")


class _Gs2328fTACACSPlusAuthenticationServerIndex_Type(Integer32):
    """Custom type gs2328fTACACSPlusAuthenticationServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328fTACACSPlusAuthenticationServerIndex_Type.__name__ = "Integer32"
_Gs2328fTACACSPlusAuthenticationServerIndex_Object = MibTableColumn
gs2328fTACACSPlusAuthenticationServerIndex = _Gs2328fTACACSPlusAuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5, 1, 1),
    _Gs2328fTACACSPlusAuthenticationServerIndex_Type()
)
gs2328fTACACSPlusAuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerIndex.setStatus("current")


class _Gs2328fTACACSPlusAuthenticationServerEnable_Type(Integer32):
    """Custom type gs2328fTACACSPlusAuthenticationServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fTACACSPlusAuthenticationServerEnable_Type.__name__ = "Integer32"
_Gs2328fTACACSPlusAuthenticationServerEnable_Object = MibTableColumn
gs2328fTACACSPlusAuthenticationServerEnable = _Gs2328fTACACSPlusAuthenticationServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5, 1, 2),
    _Gs2328fTACACSPlusAuthenticationServerEnable_Type()
)
gs2328fTACACSPlusAuthenticationServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerEnable.setStatus("current")
_Gs2328fTACACSPlusAuthenticationServerIP_Type = DisplayString
_Gs2328fTACACSPlusAuthenticationServerIP_Object = MibTableColumn
gs2328fTACACSPlusAuthenticationServerIP = _Gs2328fTACACSPlusAuthenticationServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5, 1, 3),
    _Gs2328fTACACSPlusAuthenticationServerIP_Type()
)
gs2328fTACACSPlusAuthenticationServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerIP.setStatus("current")


class _Gs2328fTACACSPlusAuthenticationServerPort_Type(Integer32):
    """Custom type gs2328fTACACSPlusAuthenticationServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2328fTACACSPlusAuthenticationServerPort_Type.__name__ = "Integer32"
_Gs2328fTACACSPlusAuthenticationServerPort_Object = MibTableColumn
gs2328fTACACSPlusAuthenticationServerPort = _Gs2328fTACACSPlusAuthenticationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5, 1, 4),
    _Gs2328fTACACSPlusAuthenticationServerPort_Type()
)
gs2328fTACACSPlusAuthenticationServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerPort.setStatus("current")
_Gs2328fTACACSPlusAuthenticationServerSecret_Type = DisplayString
_Gs2328fTACACSPlusAuthenticationServerSecret_Object = MibTableColumn
gs2328fTACACSPlusAuthenticationServerSecret = _Gs2328fTACACSPlusAuthenticationServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 5, 1, 5),
    _Gs2328fTACACSPlusAuthenticationServerSecret_Type()
)
gs2328fTACACSPlusAuthenticationServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fTACACSPlusAuthenticationServerSecret.setStatus("current")
_Gs2328fRADIUSStatisticsTable_Object = MibTable
gs2328fRADIUSStatisticsTable = _Gs2328fRADIUSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6)
)
if mibBuilder.loadTexts:
    gs2328fRADIUSStatisticsTable.setStatus("current")
_Gs2328fRADIUSStatisticsEntry_Object = MibTableRow
gs2328fRADIUSStatisticsEntry = _Gs2328fRADIUSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1)
)
gs2328fRADIUSStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fRADIUSAuthStatisticsServerIndex"),
)
if mibBuilder.loadTexts:
    gs2328fRADIUSStatisticsEntry.setStatus("current")


class _Gs2328fRADIUSAuthStatisticsServerIndex_Type(Integer32):
    """Custom type gs2328fRADIUSAuthStatisticsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2328fRADIUSAuthStatisticsServerIndex_Type.__name__ = "Integer32"
_Gs2328fRADIUSAuthStatisticsServerIndex_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsServerIndex = _Gs2328fRADIUSAuthStatisticsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 1),
    _Gs2328fRADIUSAuthStatisticsServerIndex_Type()
)
gs2328fRADIUSAuthStatisticsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsServerIndex.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktAccessAccepts_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktAccessAccepts_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktAccessAccepts = _Gs2328fRADIUSAuthStatisticsRecPktAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 2),
    _Gs2328fRADIUSAuthStatisticsRecPktAccessAccepts_Type()
)
gs2328fRADIUSAuthStatisticsRecPktAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktAccessAccepts.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktAccessRejects_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktAccessRejects_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktAccessRejects = _Gs2328fRADIUSAuthStatisticsRecPktAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 3),
    _Gs2328fRADIUSAuthStatisticsRecPktAccessRejects_Type()
)
gs2328fRADIUSAuthStatisticsRecPktAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktAccessRejects.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktAccessChallenges_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktAccessChallenges_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktAccessChallenges = _Gs2328fRADIUSAuthStatisticsRecPktAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 4),
    _Gs2328fRADIUSAuthStatisticsRecPktAccessChallenges_Type()
)
gs2328fRADIUSAuthStatisticsRecPktAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktAccessChallenges.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses = _Gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 5),
    _Gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses_Type()
)
gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators = _Gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 6),
    _Gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators_Type()
)
gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktUnknownTypes = _Gs2328fRADIUSAuthStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 7),
    _Gs2328fRADIUSAuthStatisticsRecPktUnknownTypes_Type()
)
gs2328fRADIUSAuthStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2328fRADIUSAuthStatisticsRecPktDropped_Type = Counter32
_Gs2328fRADIUSAuthStatisticsRecPktDropped_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsRecPktDropped = _Gs2328fRADIUSAuthStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 8),
    _Gs2328fRADIUSAuthStatisticsRecPktDropped_Type()
)
gs2328fRADIUSAuthStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsRecPktDropped.setStatus("current")
_Gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests_Type = Counter32
_Gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests = _Gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 9),
    _Gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests_Type()
)
gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests.setStatus("current")
_Gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type = Counter32
_Gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions = _Gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 10),
    _Gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions_Type()
)
gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions.setStatus("current")
_Gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests = _Gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 11),
    _Gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests_Type()
)
gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2328fRADIUSAuthStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2328fRADIUSAuthStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2328fRADIUSAuthStatisticsTransmitPktTimeouts = _Gs2328fRADIUSAuthStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 12),
    _Gs2328fRADIUSAuthStatisticsTransmitPktTimeouts_Type()
)
gs2328fRADIUSAuthStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2328fRADIUSAuthIP_Type = DisplayString
_Gs2328fRADIUSAuthIP_Object = MibTableColumn
gs2328fRADIUSAuthIP = _Gs2328fRADIUSAuthIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 13),
    _Gs2328fRADIUSAuthIP_Type()
)
gs2328fRADIUSAuthIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthIP.setStatus("current")
_Gs2328fRADIUSAuthState_Type = DisplayString
_Gs2328fRADIUSAuthState_Object = MibTableColumn
gs2328fRADIUSAuthState = _Gs2328fRADIUSAuthState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 14),
    _Gs2328fRADIUSAuthState_Type()
)
gs2328fRADIUSAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthState.setStatus("current")
_Gs2328fRADIUSAuthRoundTripTime_Type = DisplayString
_Gs2328fRADIUSAuthRoundTripTime_Object = MibTableColumn
gs2328fRADIUSAuthRoundTripTime = _Gs2328fRADIUSAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 15),
    _Gs2328fRADIUSAuthRoundTripTime_Type()
)
gs2328fRADIUSAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAuthRoundTripTime.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsRecPktResponses_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsRecPktResponses_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsRecPktResponses = _Gs2328fRADIUSAccountingStatisticsRecPktResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 16),
    _Gs2328fRADIUSAccountingStatisticsRecPktResponses_Type()
)
gs2328fRADIUSAccountingStatisticsRecPktResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsRecPktResponses.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses = _Gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 17),
    _Gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses_Type()
)
gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators = _Gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 18),
    _Gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators_Type()
)
gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes = _Gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 19),
    _Gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes_Type()
)
gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsRecPktDropped_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsRecPktDropped_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsRecPktDropped = _Gs2328fRADIUSAccountingStatisticsRecPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 20),
    _Gs2328fRADIUSAccountingStatisticsRecPktDropped_Type()
)
gs2328fRADIUSAccountingStatisticsRecPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsRecPktDropped.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsTransmitPktRequests_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsTransmitPktRequests_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsTransmitPktRequests = _Gs2328fRADIUSAccountingStatisticsTransmitPktRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 21),
    _Gs2328fRADIUSAccountingStatisticsTransmitPktRequests_Type()
)
gs2328fRADIUSAccountingStatisticsTransmitPktRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsTransmitPktRequests.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions = _Gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 22),
    _Gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions_Type()
)
gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests = _Gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 23),
    _Gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests_Type()
)
gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests.setStatus("current")
_Gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts_Type = Counter32
_Gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts_Object = MibTableColumn
gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts = _Gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 24),
    _Gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts_Type()
)
gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts.setStatus("current")
_Gs2328fRADIUSAccountingIP_Type = DisplayString
_Gs2328fRADIUSAccountingIP_Object = MibTableColumn
gs2328fRADIUSAccountingIP = _Gs2328fRADIUSAccountingIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 25),
    _Gs2328fRADIUSAccountingIP_Type()
)
gs2328fRADIUSAccountingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingIP.setStatus("current")
_Gs2328fRADIUSAccountingState_Type = DisplayString
_Gs2328fRADIUSAccountingState_Object = MibTableColumn
gs2328fRADIUSAccountingState = _Gs2328fRADIUSAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 26),
    _Gs2328fRADIUSAccountingState_Type()
)
gs2328fRADIUSAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingState.setStatus("current")
_Gs2328fRADIUSAccountingRoundTripTime_Type = DisplayString
_Gs2328fRADIUSAccountingRoundTripTime_Object = MibTableColumn
gs2328fRADIUSAccountingRoundTripTime = _Gs2328fRADIUSAccountingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 27),
    _Gs2328fRADIUSAccountingRoundTripTime_Type()
)
gs2328fRADIUSAccountingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fRADIUSAccountingRoundTripTime.setStatus("current")


class _Gs2328fRADIUSStatisticsClear_Type(Integer32):
    """Custom type gs2328fRADIUSStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2328fRADIUSStatisticsClear_Type.__name__ = "Integer32"
_Gs2328fRADIUSStatisticsClear_Object = MibTableColumn
gs2328fRADIUSStatisticsClear = _Gs2328fRADIUSStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 10, 6, 1, 28),
    _Gs2328fRADIUSStatisticsClear_Type()
)
gs2328fRADIUSStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRADIUSStatisticsClear.setStatus("current")
_Gs2328fNAS_ObjectIdentity = ObjectIdentity
gs2328fNAS = _Gs2328fNAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11)
)
_Gs2328fNASConfiguration_ObjectIdentity = ObjectIdentity
gs2328fNASConfiguration = _Gs2328fNASConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1)
)


class _Gs2328fNASConfigMode_Type(Integer32):
    """Custom type gs2328fNASConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigMode_Type.__name__ = "Integer32"
_Gs2328fNASConfigMode_Object = MibScalar
gs2328fNASConfigMode = _Gs2328fNASConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 1),
    _Gs2328fNASConfigMode_Type()
)
gs2328fNASConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigMode.setStatus("current")


class _Gs2328fNASConfigReauthEnabled_Type(Integer32):
    """Custom type gs2328fNASConfigReauthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigReauthEnabled_Type.__name__ = "Integer32"
_Gs2328fNASConfigReauthEnabled_Object = MibScalar
gs2328fNASConfigReauthEnabled = _Gs2328fNASConfigReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 2),
    _Gs2328fNASConfigReauthEnabled_Type()
)
gs2328fNASConfigReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigReauthEnabled.setStatus("current")


class _Gs2328fNASConfigReauthPeriod_Type(Integer32):
    """Custom type gs2328fNASConfigReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Gs2328fNASConfigReauthPeriod_Type.__name__ = "Integer32"
_Gs2328fNASConfigReauthPeriod_Object = MibScalar
gs2328fNASConfigReauthPeriod = _Gs2328fNASConfigReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 3),
    _Gs2328fNASConfigReauthPeriod_Type()
)
gs2328fNASConfigReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigReauthPeriod.setStatus("current")


class _Gs2328fNASConfigEAPOLTimeout_Type(Integer32):
    """Custom type gs2328fNASConfigEAPOLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2328fNASConfigEAPOLTimeout_Type.__name__ = "Integer32"
_Gs2328fNASConfigEAPOLTimeout_Object = MibScalar
gs2328fNASConfigEAPOLTimeout = _Gs2328fNASConfigEAPOLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 4),
    _Gs2328fNASConfigEAPOLTimeout_Type()
)
gs2328fNASConfigEAPOLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigEAPOLTimeout.setStatus("current")


class _Gs2328fNASConfigAgingPeriod_Type(Integer32):
    """Custom type gs2328fNASConfigAgingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2328fNASConfigAgingPeriod_Type.__name__ = "Integer32"
_Gs2328fNASConfigAgingPeriod_Object = MibScalar
gs2328fNASConfigAgingPeriod = _Gs2328fNASConfigAgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 5),
    _Gs2328fNASConfigAgingPeriod_Type()
)
gs2328fNASConfigAgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigAgingPeriod.setStatus("current")


class _Gs2328fNASConfigHoldTime_Type(Integer32):
    """Custom type gs2328fNASConfigHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2328fNASConfigHoldTime_Type.__name__ = "Integer32"
_Gs2328fNASConfigHoldTime_Object = MibScalar
gs2328fNASConfigHoldTime = _Gs2328fNASConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 6),
    _Gs2328fNASConfigHoldTime_Type()
)
gs2328fNASConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigHoldTime.setStatus("current")


class _Gs2328fNASConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2328fNASConfigRADIUSAssignedQoSEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2328fNASConfigRADIUSAssignedQoSEnabled_Object = MibScalar
gs2328fNASConfigRADIUSAssignedQoSEnabled = _Gs2328fNASConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 7),
    _Gs2328fNASConfigRADIUSAssignedQoSEnabled_Type()
)
gs2328fNASConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2328fNASConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2328fNASConfigRADIUSAssignedVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2328fNASConfigRADIUSAssignedVLANEnabled_Object = MibScalar
gs2328fNASConfigRADIUSAssignedVLANEnabled = _Gs2328fNASConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 8),
    _Gs2328fNASConfigRADIUSAssignedVLANEnabled_Type()
)
gs2328fNASConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2328fNASConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2328fNASConfigGuestVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2328fNASConfigGuestVLANEnabled_Object = MibScalar
gs2328fNASConfigGuestVLANEnabled = _Gs2328fNASConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 9),
    _Gs2328fNASConfigGuestVLANEnabled_Type()
)
gs2328fNASConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigGuestVLANEnabled.setStatus("current")


class _Gs2328fNASConfigGuestVLANID_Type(Integer32):
    """Custom type gs2328fNASConfigGuestVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2328fNASConfigGuestVLANID_Type.__name__ = "Integer32"
_Gs2328fNASConfigGuestVLANID_Object = MibScalar
gs2328fNASConfigGuestVLANID = _Gs2328fNASConfigGuestVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 10),
    _Gs2328fNASConfigGuestVLANID_Type()
)
gs2328fNASConfigGuestVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigGuestVLANID.setStatus("current")


class _Gs2328fNASConfigMaxReauthCount_Type(Integer32):
    """Custom type gs2328fNASConfigMaxReauthCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2328fNASConfigMaxReauthCount_Type.__name__ = "Integer32"
_Gs2328fNASConfigMaxReauthCount_Object = MibScalar
gs2328fNASConfigMaxReauthCount = _Gs2328fNASConfigMaxReauthCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 11),
    _Gs2328fNASConfigMaxReauthCount_Type()
)
gs2328fNASConfigMaxReauthCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigMaxReauthCount.setStatus("current")


class _Gs2328fNASConfigAllowGuestVLANEAPOLSeen_Type(Integer32):
    """Custom type gs2328fNASConfigAllowGuestVLANEAPOLSeen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigAllowGuestVLANEAPOLSeen_Type.__name__ = "Integer32"
_Gs2328fNASConfigAllowGuestVLANEAPOLSeen_Object = MibScalar
gs2328fNASConfigAllowGuestVLANEAPOLSeen = _Gs2328fNASConfigAllowGuestVLANEAPOLSeen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 12),
    _Gs2328fNASConfigAllowGuestVLANEAPOLSeen_Type()
)
gs2328fNASConfigAllowGuestVLANEAPOLSeen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigAllowGuestVLANEAPOLSeen.setStatus("current")
_Gs2328fNASPortConfigTable_Object = MibTable
gs2328fNASPortConfigTable = _Gs2328fNASPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13)
)
if mibBuilder.loadTexts:
    gs2328fNASPortConfigTable.setStatus("current")
_Gs2328fNASPortConfigEntry_Object = MibTableRow
gs2328fNASPortConfigEntry = _Gs2328fNASPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1)
)
gs2328fNASPortConfigEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fNASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328fNASPortConfigEntry.setStatus("current")


class _Gs2328fNASPortConfigPort_Type(Integer32):
    """Custom type gs2328fNASPortConfigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2328fNASPortConfigPort_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigPort_Object = MibTableColumn
gs2328fNASPortConfigPort = _Gs2328fNASPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 1),
    _Gs2328fNASPortConfigPort_Type()
)
gs2328fNASPortConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigPort.setStatus("current")


class _Gs2328fNASPortConfigAdminState_Type(Integer32):
    """Custom type gs2328fNASPortConfigAdminState based on Integer32"""
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


_Gs2328fNASPortConfigAdminState_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigAdminState_Object = MibTableColumn
gs2328fNASPortConfigAdminState = _Gs2328fNASPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 2),
    _Gs2328fNASPortConfigAdminState_Type()
)
gs2328fNASPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigAdminState.setStatus("current")


class _Gs2328fNASPortConfigRADIUSAssignedQoSEnabled_Type(Integer32):
    """Custom type gs2328fNASPortConfigRADIUSAssignedQoSEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASPortConfigRADIUSAssignedQoSEnabled_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigRADIUSAssignedQoSEnabled_Object = MibTableColumn
gs2328fNASPortConfigRADIUSAssignedQoSEnabled = _Gs2328fNASPortConfigRADIUSAssignedQoSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 3),
    _Gs2328fNASPortConfigRADIUSAssignedQoSEnabled_Type()
)
gs2328fNASPortConfigRADIUSAssignedQoSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigRADIUSAssignedQoSEnabled.setStatus("current")


class _Gs2328fNASPortConfigRADIUSAssignedVLANEnabled_Type(Integer32):
    """Custom type gs2328fNASPortConfigRADIUSAssignedVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASPortConfigRADIUSAssignedVLANEnabled_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigRADIUSAssignedVLANEnabled_Object = MibTableColumn
gs2328fNASPortConfigRADIUSAssignedVLANEnabled = _Gs2328fNASPortConfigRADIUSAssignedVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 4),
    _Gs2328fNASPortConfigRADIUSAssignedVLANEnabled_Type()
)
gs2328fNASPortConfigRADIUSAssignedVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigRADIUSAssignedVLANEnabled.setStatus("current")


class _Gs2328fNASPortConfigGuestVLANEnabled_Type(Integer32):
    """Custom type gs2328fNASPortConfigGuestVLANEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASPortConfigGuestVLANEnabled_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigGuestVLANEnabled_Object = MibTableColumn
gs2328fNASPortConfigGuestVLANEnabled = _Gs2328fNASPortConfigGuestVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 5),
    _Gs2328fNASPortConfigGuestVLANEnabled_Type()
)
gs2328fNASPortConfigGuestVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigGuestVLANEnabled.setStatus("current")
_Gs2328fNASPortConfigPortState_Type = DisplayString
_Gs2328fNASPortConfigPortState_Object = MibTableColumn
gs2328fNASPortConfigPortState = _Gs2328fNASPortConfigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 6),
    _Gs2328fNASPortConfigPortState_Type()
)
gs2328fNASPortConfigPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigPortState.setStatus("current")


class _Gs2328fNASPortConfigReauthenticate_Type(Integer32):
    """Custom type gs2328fNASPortConfigReauthenticate based on Integer32"""
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


_Gs2328fNASPortConfigReauthenticate_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigReauthenticate_Object = MibTableColumn
gs2328fNASPortConfigReauthenticate = _Gs2328fNASPortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 7),
    _Gs2328fNASPortConfigReauthenticate_Type()
)
gs2328fNASPortConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigReauthenticate.setStatus("current")


class _Gs2328fNASPortConfigReinitialize_Type(Integer32):
    """Custom type gs2328fNASPortConfigReinitialize based on Integer32"""
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


_Gs2328fNASPortConfigReinitialize_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigReinitialize_Object = MibTableColumn
gs2328fNASPortConfigReinitialize = _Gs2328fNASPortConfigReinitialize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 8),
    _Gs2328fNASPortConfigReinitialize_Type()
)
gs2328fNASPortConfigReinitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigReinitialize.setStatus("current")


class _Gs2328fNASPortConfigFallbackEnabled_Type(Integer32):
    """Custom type gs2328fNASPortConfigFallbackEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASPortConfigFallbackEnabled_Type.__name__ = "Integer32"
_Gs2328fNASPortConfigFallbackEnabled_Object = MibTableColumn
gs2328fNASPortConfigFallbackEnabled = _Gs2328fNASPortConfigFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 13, 1, 101),
    _Gs2328fNASPortConfigFallbackEnabled_Type()
)
gs2328fNASPortConfigFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASPortConfigFallbackEnabled.setStatus("current")


class _Gs2328fNASConfigMacBasedUseEAP_Type(Integer32):
    """Custom type gs2328fNASConfigMacBasedUseEAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fNASConfigMacBasedUseEAP_Type.__name__ = "Integer32"
_Gs2328fNASConfigMacBasedUseEAP_Object = MibScalar
gs2328fNASConfigMacBasedUseEAP = _Gs2328fNASConfigMacBasedUseEAP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 1, 101),
    _Gs2328fNASConfigMacBasedUseEAP_Type()
)
gs2328fNASConfigMacBasedUseEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASConfigMacBasedUseEAP.setStatus("current")
_Gs2328fNASSwitchStatusTable_Object = MibTable
gs2328fNASSwitchStatusTable = _Gs2328fNASSwitchStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2)
)
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusTable.setStatus("current")
_Gs2328fNASSwitchStatusEntry_Object = MibTableRow
gs2328fNASSwitchStatusEntry = _Gs2328fNASSwitchStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1)
)
gs2328fNASSwitchStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fNASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusEntry.setStatus("current")
_Gs2328fNASSwitchStatusAdminState_Type = DisplayString
_Gs2328fNASSwitchStatusAdminState_Object = MibTableColumn
gs2328fNASSwitchStatusAdminState = _Gs2328fNASSwitchStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1, 2),
    _Gs2328fNASSwitchStatusAdminState_Type()
)
gs2328fNASSwitchStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusAdminState.setStatus("current")
_Gs2328fNASSwitchStatusPortState_Type = DisplayString
_Gs2328fNASSwitchStatusPortState_Object = MibTableColumn
gs2328fNASSwitchStatusPortState = _Gs2328fNASSwitchStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1, 3),
    _Gs2328fNASSwitchStatusPortState_Type()
)
gs2328fNASSwitchStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusPortState.setStatus("current")
_Gs2328fNASSwitchStatusLastSource_Type = DisplayString
_Gs2328fNASSwitchStatusLastSource_Object = MibTableColumn
gs2328fNASSwitchStatusLastSource = _Gs2328fNASSwitchStatusLastSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1, 4),
    _Gs2328fNASSwitchStatusLastSource_Type()
)
gs2328fNASSwitchStatusLastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusLastSource.setStatus("current")
_Gs2328fNASSwitchStatusLastID_Type = DisplayString
_Gs2328fNASSwitchStatusLastID_Object = MibTableColumn
gs2328fNASSwitchStatusLastID = _Gs2328fNASSwitchStatusLastID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1, 5),
    _Gs2328fNASSwitchStatusLastID_Type()
)
gs2328fNASSwitchStatusLastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusLastID.setStatus("current")
_Gs2328fNASSwitchStatusQoSClass_Type = DisplayString
_Gs2328fNASSwitchStatusQoSClass_Object = MibTableColumn
gs2328fNASSwitchStatusQoSClass = _Gs2328fNASSwitchStatusQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1, 6),
    _Gs2328fNASSwitchStatusQoSClass_Type()
)
gs2328fNASSwitchStatusQoSClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusQoSClass.setStatus("current")
_Gs2328fNASSwitchStatusPortVlanID_Type = DisplayString
_Gs2328fNASSwitchStatusPortVlanID_Object = MibTableColumn
gs2328fNASSwitchStatusPortVlanID = _Gs2328fNASSwitchStatusPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 2, 1, 7),
    _Gs2328fNASSwitchStatusPortVlanID_Type()
)
gs2328fNASSwitchStatusPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASSwitchStatusPortVlanID.setStatus("current")
_Gs2328fNASPortStatus_ObjectIdentity = ObjectIdentity
gs2328fNASPortStatus = _Gs2328fNASPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3)
)
_Gs2328fNASPortStatusCountersTable_Object = MibTable
gs2328fNASPortStatusCountersTable = _Gs2328fNASPortStatusCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    gs2328fNASPortStatusCountersTable.setStatus("current")
_Gs2328fNASPortStatusCountersEntry_Object = MibTableRow
gs2328fNASPortStatusCountersEntry = _Gs2328fNASPortStatusCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1)
)
gs2328fNASPortStatusCountersEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fNASPortConfigPort"),
)
if mibBuilder.loadTexts:
    gs2328fNASPortStatusCountersEntry.setStatus("current")
_Gs2328fNASRxCountersEAPOLTotal_Type = Counter32
_Gs2328fNASRxCountersEAPOLTotal_Object = MibTableColumn
gs2328fNASRxCountersEAPOLTotal = _Gs2328fNASRxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 2),
    _Gs2328fNASRxCountersEAPOLTotal_Type()
)
gs2328fNASRxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLTotal.setStatus("current")
_Gs2328fNASRxCountersEAPOLResponseID_Type = Counter32
_Gs2328fNASRxCountersEAPOLResponseID_Object = MibTableColumn
gs2328fNASRxCountersEAPOLResponseID = _Gs2328fNASRxCountersEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 3),
    _Gs2328fNASRxCountersEAPOLResponseID_Type()
)
gs2328fNASRxCountersEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLResponseID.setStatus("current")
_Gs2328fNASRxCountersEAPOLResponses_Type = Counter32
_Gs2328fNASRxCountersEAPOLResponses_Object = MibTableColumn
gs2328fNASRxCountersEAPOLResponses = _Gs2328fNASRxCountersEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 4),
    _Gs2328fNASRxCountersEAPOLResponses_Type()
)
gs2328fNASRxCountersEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLResponses.setStatus("current")
_Gs2328fNASRxCountersEAPOLStart_Type = Counter32
_Gs2328fNASRxCountersEAPOLStart_Object = MibTableColumn
gs2328fNASRxCountersEAPOLStart = _Gs2328fNASRxCountersEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 5),
    _Gs2328fNASRxCountersEAPOLStart_Type()
)
gs2328fNASRxCountersEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLStart.setStatus("current")
_Gs2328fNASRxCountersEAPOLLogoff_Type = Counter32
_Gs2328fNASRxCountersEAPOLLogoff_Object = MibTableColumn
gs2328fNASRxCountersEAPOLLogoff = _Gs2328fNASRxCountersEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 6),
    _Gs2328fNASRxCountersEAPOLLogoff_Type()
)
gs2328fNASRxCountersEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLLogoff.setStatus("current")
_Gs2328fNASRxCountersEAPOLInvalidType_Type = Counter32
_Gs2328fNASRxCountersEAPOLInvalidType_Object = MibTableColumn
gs2328fNASRxCountersEAPOLInvalidType = _Gs2328fNASRxCountersEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 7),
    _Gs2328fNASRxCountersEAPOLInvalidType_Type()
)
gs2328fNASRxCountersEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLInvalidType.setStatus("current")
_Gs2328fNASRxCountersEAPOLInvalidLength_Type = Counter32
_Gs2328fNASRxCountersEAPOLInvalidLength_Object = MibTableColumn
gs2328fNASRxCountersEAPOLInvalidLength = _Gs2328fNASRxCountersEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 8),
    _Gs2328fNASRxCountersEAPOLInvalidLength_Type()
)
gs2328fNASRxCountersEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxCountersEAPOLInvalidLength.setStatus("current")
_Gs2328fNASTxCountersEAPOLTotal_Type = Counter32
_Gs2328fNASTxCountersEAPOLTotal_Object = MibTableColumn
gs2328fNASTxCountersEAPOLTotal = _Gs2328fNASTxCountersEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 9),
    _Gs2328fNASTxCountersEAPOLTotal_Type()
)
gs2328fNASTxCountersEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxCountersEAPOLTotal.setStatus("current")
_Gs2328fNASTxCountersEAPOLRequestID_Type = Counter32
_Gs2328fNASTxCountersEAPOLRequestID_Object = MibTableColumn
gs2328fNASTxCountersEAPOLRequestID = _Gs2328fNASTxCountersEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 10),
    _Gs2328fNASTxCountersEAPOLRequestID_Type()
)
gs2328fNASTxCountersEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxCountersEAPOLRequestID.setStatus("current")
_Gs2328fNASTxCountersEAPOLRequests_Type = Counter32
_Gs2328fNASTxCountersEAPOLRequests_Object = MibTableColumn
gs2328fNASTxCountersEAPOLRequests = _Gs2328fNASTxCountersEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 11),
    _Gs2328fNASTxCountersEAPOLRequests_Type()
)
gs2328fNASTxCountersEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxCountersEAPOLRequests.setStatus("current")
_Gs2328fNASRxBackendServerCountersAccessChallenges_Type = Counter32
_Gs2328fNASRxBackendServerCountersAccessChallenges_Object = MibTableColumn
gs2328fNASRxBackendServerCountersAccessChallenges = _Gs2328fNASRxBackendServerCountersAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 12),
    _Gs2328fNASRxBackendServerCountersAccessChallenges_Type()
)
gs2328fNASRxBackendServerCountersAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerCountersAccessChallenges.setStatus("current")
_Gs2328fNASRxBackendServerCountersOtherRequests_Type = Counter32
_Gs2328fNASRxBackendServerCountersOtherRequests_Object = MibTableColumn
gs2328fNASRxBackendServerCountersOtherRequests = _Gs2328fNASRxBackendServerCountersOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 13),
    _Gs2328fNASRxBackendServerCountersOtherRequests_Type()
)
gs2328fNASRxBackendServerCountersOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerCountersOtherRequests.setStatus("current")
_Gs2328fNASRxBackendServerCountersAuthSuccesses_Type = Counter32
_Gs2328fNASRxBackendServerCountersAuthSuccesses_Object = MibTableColumn
gs2328fNASRxBackendServerCountersAuthSuccesses = _Gs2328fNASRxBackendServerCountersAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 14),
    _Gs2328fNASRxBackendServerCountersAuthSuccesses_Type()
)
gs2328fNASRxBackendServerCountersAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerCountersAuthSuccesses.setStatus("current")
_Gs2328fNASRxBackendServerCountersAuthFailures_Type = Counter32
_Gs2328fNASRxBackendServerCountersAuthFailures_Object = MibTableColumn
gs2328fNASRxBackendServerCountersAuthFailures = _Gs2328fNASRxBackendServerCountersAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 15),
    _Gs2328fNASRxBackendServerCountersAuthFailures_Type()
)
gs2328fNASRxBackendServerCountersAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerCountersAuthFailures.setStatus("current")
_Gs2328fNASTxBackendServerCountersResponses_Type = Counter32
_Gs2328fNASTxBackendServerCountersResponses_Object = MibTableColumn
gs2328fNASTxBackendServerCountersResponses = _Gs2328fNASTxBackendServerCountersResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 16),
    _Gs2328fNASTxBackendServerCountersResponses_Type()
)
gs2328fNASTxBackendServerCountersResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxBackendServerCountersResponses.setStatus("current")
_Gs2328fNASLastSupplicantInfoMACAddress_Type = DisplayString
_Gs2328fNASLastSupplicantInfoMACAddress_Object = MibTableColumn
gs2328fNASLastSupplicantInfoMACAddress = _Gs2328fNASLastSupplicantInfoMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 17),
    _Gs2328fNASLastSupplicantInfoMACAddress_Type()
)
gs2328fNASLastSupplicantInfoMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASLastSupplicantInfoMACAddress.setStatus("current")
_Gs2328fNASLastSupplicantInfoVlanID_Type = Integer32
_Gs2328fNASLastSupplicantInfoVlanID_Object = MibTableColumn
gs2328fNASLastSupplicantInfoVlanID = _Gs2328fNASLastSupplicantInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 18),
    _Gs2328fNASLastSupplicantInfoVlanID_Type()
)
gs2328fNASLastSupplicantInfoVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASLastSupplicantInfoVlanID.setStatus("current")
_Gs2328fNASLastSupplicantInfoVersion_Type = Integer32
_Gs2328fNASLastSupplicantInfoVersion_Object = MibTableColumn
gs2328fNASLastSupplicantInfoVersion = _Gs2328fNASLastSupplicantInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 19),
    _Gs2328fNASLastSupplicantInfoVersion_Type()
)
gs2328fNASLastSupplicantInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASLastSupplicantInfoVersion.setStatus("current")
_Gs2328fNASLastSupplicantInfoIdentity_Type = DisplayString
_Gs2328fNASLastSupplicantInfoIdentity_Object = MibTableColumn
gs2328fNASLastSupplicantInfoIdentity = _Gs2328fNASLastSupplicantInfoIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 20),
    _Gs2328fNASLastSupplicantInfoIdentity_Type()
)
gs2328fNASLastSupplicantInfoIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASLastSupplicantInfoIdentity.setStatus("current")


class _Gs2328fNASCountersDoClear_Type(Integer32):
    """Custom type gs2328fNASCountersDoClear based on Integer32"""
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


_Gs2328fNASCountersDoClear_Type.__name__ = "Integer32"
_Gs2328fNASCountersDoClear_Object = MibTableColumn
gs2328fNASCountersDoClear = _Gs2328fNASCountersDoClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 1, 1, 21),
    _Gs2328fNASCountersDoClear_Type()
)
gs2328fNASCountersDoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fNASCountersDoClear.setStatus("current")
_Gs2328fNASPortStatusClientsTable_Object = MibTable
gs2328fNASPortStatusClientsTable = _Gs2328fNASPortStatusClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gs2328fNASPortStatusClientsTable.setStatus("current")
_Gs2328fNASPortStatusClientsEntry_Object = MibTableRow
gs2328fNASPortStatusClientsEntry = _Gs2328fNASPortStatusClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1)
)
gs2328fNASPortStatusClientsEntry.setIndexNames(
    (0, "LANCOM-GS-2328F-MIB", "gs2328fNASPortConfigPort"),
    (0, "LANCOM-GS-2328F-MIB", "gs2328fNASClientsIndex"),
)
if mibBuilder.loadTexts:
    gs2328fNASPortStatusClientsEntry.setStatus("current")


class _Gs2328fNASClientsIndex_Type(Integer32):
    """Custom type gs2328fNASClientsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2328fNASClientsIndex_Type.__name__ = "Integer32"
_Gs2328fNASClientsIndex_Object = MibTableColumn
gs2328fNASClientsIndex = _Gs2328fNASClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 1),
    _Gs2328fNASClientsIndex_Type()
)
gs2328fNASClientsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2328fNASClientsIndex.setStatus("current")
_Gs2328fNASClientsIdentity_Type = DisplayString
_Gs2328fNASClientsIdentity_Object = MibTableColumn
gs2328fNASClientsIdentity = _Gs2328fNASClientsIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 2),
    _Gs2328fNASClientsIdentity_Type()
)
gs2328fNASClientsIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASClientsIdentity.setStatus("current")
_Gs2328fNASClientsMACAddress_Type = DisplayString
_Gs2328fNASClientsMACAddress_Object = MibTableColumn
gs2328fNASClientsMACAddress = _Gs2328fNASClientsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 3),
    _Gs2328fNASClientsMACAddress_Type()
)
gs2328fNASClientsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASClientsMACAddress.setStatus("current")


class _Gs2328fNASClientsVlanID_Type(Integer32):
    """Custom type gs2328fNASClientsVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Gs2328fNASClientsVlanID_Type.__name__ = "Integer32"
_Gs2328fNASClientsVlanID_Object = MibTableColumn
gs2328fNASClientsVlanID = _Gs2328fNASClientsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 4),
    _Gs2328fNASClientsVlanID_Type()
)
gs2328fNASClientsVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASClientsVlanID.setStatus("current")
_Gs2328fNASClientsState_Type = DisplayString
_Gs2328fNASClientsState_Object = MibTableColumn
gs2328fNASClientsState = _Gs2328fNASClientsState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 5),
    _Gs2328fNASClientsState_Type()
)
gs2328fNASClientsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASClientsState.setStatus("current")
_Gs2328fNASClientsLastAuth_Type = DisplayString
_Gs2328fNASClientsLastAuth_Object = MibTableColumn
gs2328fNASClientsLastAuth = _Gs2328fNASClientsLastAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 6),
    _Gs2328fNASClientsLastAuth_Type()
)
gs2328fNASClientsLastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASClientsLastAuth.setStatus("current")
_Gs2328fNASRxClientsEAPOLTotal_Type = Counter32
_Gs2328fNASRxClientsEAPOLTotal_Object = MibTableColumn
gs2328fNASRxClientsEAPOLTotal = _Gs2328fNASRxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 7),
    _Gs2328fNASRxClientsEAPOLTotal_Type()
)
gs2328fNASRxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLTotal.setStatus("current")
_Gs2328fNASRxClientsEAPOLResponseID_Type = Counter32
_Gs2328fNASRxClientsEAPOLResponseID_Object = MibTableColumn
gs2328fNASRxClientsEAPOLResponseID = _Gs2328fNASRxClientsEAPOLResponseID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 8),
    _Gs2328fNASRxClientsEAPOLResponseID_Type()
)
gs2328fNASRxClientsEAPOLResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLResponseID.setStatus("current")
_Gs2328fNASRxClientsEAPOLResponses_Type = Counter32
_Gs2328fNASRxClientsEAPOLResponses_Object = MibTableColumn
gs2328fNASRxClientsEAPOLResponses = _Gs2328fNASRxClientsEAPOLResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 9),
    _Gs2328fNASRxClientsEAPOLResponses_Type()
)
gs2328fNASRxClientsEAPOLResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLResponses.setStatus("current")
_Gs2328fNASRxClientsEAPOLStart_Type = Counter32
_Gs2328fNASRxClientsEAPOLStart_Object = MibTableColumn
gs2328fNASRxClientsEAPOLStart = _Gs2328fNASRxClientsEAPOLStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 10),
    _Gs2328fNASRxClientsEAPOLStart_Type()
)
gs2328fNASRxClientsEAPOLStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLStart.setStatus("current")
_Gs2328fNASRxClientsEAPOLLogoff_Type = Counter32
_Gs2328fNASRxClientsEAPOLLogoff_Object = MibTableColumn
gs2328fNASRxClientsEAPOLLogoff = _Gs2328fNASRxClientsEAPOLLogoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 11),
    _Gs2328fNASRxClientsEAPOLLogoff_Type()
)
gs2328fNASRxClientsEAPOLLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLLogoff.setStatus("current")
_Gs2328fNASRxClientsEAPOLInvalidType_Type = Counter32
_Gs2328fNASRxClientsEAPOLInvalidType_Object = MibTableColumn
gs2328fNASRxClientsEAPOLInvalidType = _Gs2328fNASRxClientsEAPOLInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 12),
    _Gs2328fNASRxClientsEAPOLInvalidType_Type()
)
gs2328fNASRxClientsEAPOLInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLInvalidType.setStatus("current")
_Gs2328fNASRxClientsEAPOLInvalidLength_Type = Counter32
_Gs2328fNASRxClientsEAPOLInvalidLength_Object = MibTableColumn
gs2328fNASRxClientsEAPOLInvalidLength = _Gs2328fNASRxClientsEAPOLInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 13),
    _Gs2328fNASRxClientsEAPOLInvalidLength_Type()
)
gs2328fNASRxClientsEAPOLInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxClientsEAPOLInvalidLength.setStatus("current")
_Gs2328fNASTxClientsEAPOLTotal_Type = Counter32
_Gs2328fNASTxClientsEAPOLTotal_Object = MibTableColumn
gs2328fNASTxClientsEAPOLTotal = _Gs2328fNASTxClientsEAPOLTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 14),
    _Gs2328fNASTxClientsEAPOLTotal_Type()
)
gs2328fNASTxClientsEAPOLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxClientsEAPOLTotal.setStatus("current")
_Gs2328fNASTxClientsEAPOLRequestID_Type = Counter32
_Gs2328fNASTxClientsEAPOLRequestID_Object = MibTableColumn
gs2328fNASTxClientsEAPOLRequestID = _Gs2328fNASTxClientsEAPOLRequestID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 15),
    _Gs2328fNASTxClientsEAPOLRequestID_Type()
)
gs2328fNASTxClientsEAPOLRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxClientsEAPOLRequestID.setStatus("current")
_Gs2328fNASTxClientsEAPOLRequests_Type = Counter32
_Gs2328fNASTxClientsEAPOLRequests_Object = MibTableColumn
gs2328fNASTxClientsEAPOLRequests = _Gs2328fNASTxClientsEAPOLRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 16),
    _Gs2328fNASTxClientsEAPOLRequests_Type()
)
gs2328fNASTxClientsEAPOLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxClientsEAPOLRequests.setStatus("current")
_Gs2328fNASRxBackendServerClientsAccessChallenges_Type = Counter32
_Gs2328fNASRxBackendServerClientsAccessChallenges_Object = MibTableColumn
gs2328fNASRxBackendServerClientsAccessChallenges = _Gs2328fNASRxBackendServerClientsAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 17),
    _Gs2328fNASRxBackendServerClientsAccessChallenges_Type()
)
gs2328fNASRxBackendServerClientsAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerClientsAccessChallenges.setStatus("current")
_Gs2328fNASRxBackendServerClientsOtherRequests_Type = Counter32
_Gs2328fNASRxBackendServerClientsOtherRequests_Object = MibTableColumn
gs2328fNASRxBackendServerClientsOtherRequests = _Gs2328fNASRxBackendServerClientsOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 18),
    _Gs2328fNASRxBackendServerClientsOtherRequests_Type()
)
gs2328fNASRxBackendServerClientsOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerClientsOtherRequests.setStatus("current")
_Gs2328fNASRxBackendServerClientsAuthSuccesses_Type = Counter32
_Gs2328fNASRxBackendServerClientsAuthSuccesses_Object = MibTableColumn
gs2328fNASRxBackendServerClientsAuthSuccesses = _Gs2328fNASRxBackendServerClientsAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 19),
    _Gs2328fNASRxBackendServerClientsAuthSuccesses_Type()
)
gs2328fNASRxBackendServerClientsAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerClientsAuthSuccesses.setStatus("current")
_Gs2328fNASRxBackendServerClientsAuthFailures_Type = Counter32
_Gs2328fNASRxBackendServerClientsAuthFailures_Object = MibTableColumn
gs2328fNASRxBackendServerClientsAuthFailures = _Gs2328fNASRxBackendServerClientsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 20),
    _Gs2328fNASRxBackendServerClientsAuthFailures_Type()
)
gs2328fNASRxBackendServerClientsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASRxBackendServerClientsAuthFailures.setStatus("current")
_Gs2328fNASTxBackendServerClientsResponses_Type = Counter32
_Gs2328fNASTxBackendServerClientsResponses_Object = MibTableColumn
gs2328fNASTxBackendServerClientsResponses = _Gs2328fNASTxBackendServerClientsResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 3, 11, 3, 2, 1, 21),
    _Gs2328fNASTxBackendServerClientsResponses_Type()
)
gs2328fNASTxBackendServerClientsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fNASTxBackendServerClientsResponses.setStatus("current")
_Gs2328fMaintenance_ObjectIdentity = ObjectIdentity
gs2328fMaintenance = _Gs2328fMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4)
)


class _Gs2328fRestartDevice_Type(Integer32):
    """Custom type gs2328fRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fRestartDevice_Type.__name__ = "Integer32"
_Gs2328fRestartDevice_Object = MibScalar
gs2328fRestartDevice = _Gs2328fRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 1),
    _Gs2328fRestartDevice_Type()
)
gs2328fRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRestartDevice.setStatus("current")
_Gs2328fFirmware_ObjectIdentity = ObjectIdentity
gs2328fFirmware = _Gs2328fFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 2)
)
_Gs2328fFirmwareIpAddress_Type = IpAddress
_Gs2328fFirmwareIpAddress_Object = MibScalar
gs2328fFirmwareIpAddress = _Gs2328fFirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 2, 1),
    _Gs2328fFirmwareIpAddress_Type()
)
gs2328fFirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFirmwareIpAddress.setStatus("current")
_Gs2328fFirmwareFileName_Type = DisplayString
_Gs2328fFirmwareFileName_Object = MibScalar
gs2328fFirmwareFileName = _Gs2328fFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 2, 2),
    _Gs2328fFirmwareFileName_Type()
)
gs2328fFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFirmwareFileName.setStatus("current")


class _Gs2328fDoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2328fDoFirmwareUpgrade based on Integer32"""
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


_Gs2328fDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2328fDoFirmwareUpgrade_Object = MibScalar
gs2328fDoFirmwareUpgrade = _Gs2328fDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 2, 3),
    _Gs2328fDoFirmwareUpgrade_Type()
)
gs2328fDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDoFirmwareUpgrade.setStatus("current")
_Gs2328fSaveOrRestore_ObjectIdentity = ObjectIdentity
gs2328fSaveOrRestore = _Gs2328fSaveOrRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 3)
)


class _Gs2328fFactoryDefaults_Type(Integer32):
    """Custom type gs2328fFactoryDefaults based on Integer32"""
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


_Gs2328fFactoryDefaults_Type.__name__ = "Integer32"
_Gs2328fFactoryDefaults_Object = MibScalar
gs2328fFactoryDefaults = _Gs2328fFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 3, 1),
    _Gs2328fFactoryDefaults_Type()
)
gs2328fFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fFactoryDefaults.setStatus("current")


class _Gs2328fSaveStart_Type(Integer32):
    """Custom type gs2328fSaveStart based on Integer32"""
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


_Gs2328fSaveStart_Type.__name__ = "Integer32"
_Gs2328fSaveStart_Object = MibScalar
gs2328fSaveStart = _Gs2328fSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 3, 2),
    _Gs2328fSaveStart_Type()
)
gs2328fSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSaveStart.setStatus("current")


class _Gs2328fSaveUser_Type(Integer32):
    """Custom type gs2328fSaveUser based on Integer32"""
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


_Gs2328fSaveUser_Type.__name__ = "Integer32"
_Gs2328fSaveUser_Object = MibScalar
gs2328fSaveUser = _Gs2328fSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 3, 3),
    _Gs2328fSaveUser_Type()
)
gs2328fSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fSaveUser.setStatus("current")


class _Gs2328fRestoreUser_Type(Integer32):
    """Custom type gs2328fRestoreUser based on Integer32"""
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


_Gs2328fRestoreUser_Type.__name__ = "Integer32"
_Gs2328fRestoreUser_Object = MibScalar
gs2328fRestoreUser = _Gs2328fRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 3, 4),
    _Gs2328fRestoreUser_Type()
)
gs2328fRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fRestoreUser.setStatus("current")
_Gs2328fExportOrImport_ObjectIdentity = ObjectIdentity
gs2328fExportOrImport = _Gs2328fExportOrImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4)
)
_Gs2328fExportIpAddress_Type = IpAddress
_Gs2328fExportIpAddress_Object = MibScalar
gs2328fExportIpAddress = _Gs2328fExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4, 1),
    _Gs2328fExportIpAddress_Type()
)
gs2328fExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fExportIpAddress.setStatus("current")
_Gs2328fExportConfigName_Type = DisplayString
_Gs2328fExportConfigName_Object = MibScalar
gs2328fExportConfigName = _Gs2328fExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4, 2),
    _Gs2328fExportConfigName_Type()
)
gs2328fExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fExportConfigName.setStatus("current")


class _Gs2328fDoExportConfig_Type(Integer32):
    """Custom type gs2328fDoExportConfig based on Integer32"""
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


_Gs2328fDoExportConfig_Type.__name__ = "Integer32"
_Gs2328fDoExportConfig_Object = MibScalar
gs2328fDoExportConfig = _Gs2328fDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4, 3),
    _Gs2328fDoExportConfig_Type()
)
gs2328fDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDoExportConfig.setStatus("current")
_Gs2328fImportIpAddress_Type = IpAddress
_Gs2328fImportIpAddress_Object = MibScalar
gs2328fImportIpAddress = _Gs2328fImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4, 4),
    _Gs2328fImportIpAddress_Type()
)
gs2328fImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fImportIpAddress.setStatus("current")
_Gs2328fImportConfigName_Type = DisplayString
_Gs2328fImportConfigName_Object = MibScalar
gs2328fImportConfigName = _Gs2328fImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4, 5),
    _Gs2328fImportConfigName_Type()
)
gs2328fImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fImportConfigName.setStatus("current")


class _Gs2328fDoImportConfig_Type(Integer32):
    """Custom type gs2328fDoImportConfig based on Integer32"""
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


_Gs2328fDoImportConfig_Type.__name__ = "Integer32"
_Gs2328fDoImportConfig_Object = MibScalar
gs2328fDoImportConfig = _Gs2328fDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 4, 6),
    _Gs2328fDoImportConfig_Type()
)
gs2328fDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDoImportConfig.setStatus("current")
_Gs2328fDiagnostics_ObjectIdentity = ObjectIdentity
gs2328fDiagnostics = _Gs2328fDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5)
)
_Gs2328fPingIpAddress_Type = IpAddress
_Gs2328fPingIpAddress_Object = MibScalar
gs2328fPingIpAddress = _Gs2328fPingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 1),
    _Gs2328fPingIpAddress_Type()
)
gs2328fPingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPingIpAddress.setStatus("current")


class _Gs2328fPingSize_Type(Integer32):
    """Custom type gs2328fPingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2328fPingSize_Type.__name__ = "Integer32"
_Gs2328fPingSize_Object = MibScalar
gs2328fPingSize = _Gs2328fPingSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 2),
    _Gs2328fPingSize_Type()
)
gs2328fPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPingSize.setStatus("current")


class _Gs2328fDoPingConfig_Type(Integer32):
    """Custom type gs2328fDoPingConfig based on Integer32"""
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


_Gs2328fDoPingConfig_Type.__name__ = "Integer32"
_Gs2328fDoPingConfig_Object = MibScalar
gs2328fDoPingConfig = _Gs2328fDoPingConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 3),
    _Gs2328fDoPingConfig_Type()
)
gs2328fDoPingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDoPingConfig.setStatus("current")
_Gs2328fPingResult_Type = DisplayString
_Gs2328fPingResult_Object = MibScalar
gs2328fPingResult = _Gs2328fPingResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 4),
    _Gs2328fPingResult_Type()
)
gs2328fPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPingResult.setStatus("current")
_Gs2328fPing6IpAddress_Type = DisplayString
_Gs2328fPing6IpAddress_Object = MibScalar
gs2328fPing6IpAddress = _Gs2328fPing6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 5),
    _Gs2328fPing6IpAddress_Type()
)
gs2328fPing6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPing6IpAddress.setStatus("current")


class _Gs2328fPing6Size_Type(Integer32):
    """Custom type gs2328fPing6Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1400),
    )


_Gs2328fPing6Size_Type.__name__ = "Integer32"
_Gs2328fPing6Size_Object = MibScalar
gs2328fPing6Size = _Gs2328fPing6Size_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 6),
    _Gs2328fPing6Size_Type()
)
gs2328fPing6Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fPing6Size.setStatus("current")


class _Gs2328fDoPing6Config_Type(Integer32):
    """Custom type gs2328fDoPing6Config based on Integer32"""
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


_Gs2328fDoPing6Config_Type.__name__ = "Integer32"
_Gs2328fDoPing6Config_Object = MibScalar
gs2328fDoPing6Config = _Gs2328fDoPing6Config_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 7),
    _Gs2328fDoPing6Config_Type()
)
gs2328fDoPing6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fDoPing6Config.setStatus("current")
_Gs2328fPing6Result_Type = DisplayString
_Gs2328fPing6Result_Object = MibScalar
gs2328fPing6Result = _Gs2328fPing6Result_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 5, 8),
    _Gs2328fPing6Result_Type()
)
gs2328fPing6Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fPing6Result.setStatus("current")


class _Gs2328fColdRestartDevice_Type(Integer32):
    """Custom type gs2328fColdRestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Gs2328fColdRestartDevice_Type.__name__ = "Integer32"
_Gs2328fColdRestartDevice_Object = MibScalar
gs2328fColdRestartDevice = _Gs2328fColdRestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 4, 1500),
    _Gs2328fColdRestartDevice_Type()
)
gs2328fColdRestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2328fColdRestartDevice.setStatus("current")
_Gs2328fTrap_ObjectIdentity = ObjectIdentity
gs2328fTrap = _Gs2328fTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5)
)
_Gs2328fTrapEvent_ObjectIdentity = ObjectIdentity
gs2328fTrapEvent = _Gs2328fTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1)
)
_Gs2328fTrapVariable_ObjectIdentity = ObjectIdentity
gs2328fTrapVariable = _Gs2328fTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 2)
)
_Gs2328fInformation_Type = DisplayString
_Gs2328fInformation_Object = MibScalar
gs2328fInformation = _Gs2328fInformation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 2, 1),
    _Gs2328fInformation_Type()
)
gs2328fInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2328fInformation.setStatus("current")

# Managed Objects groups


# Notification objects

gs2328fEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 1)
)
gs2328fEmergency.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fEmergency.setStatus(
        "current"
    )

gs2328fAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 2)
)
gs2328fAlert.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fAlert.setStatus(
        "current"
    )

gs2328fCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 3)
)
gs2328fCritical.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fCritical.setStatus(
        "current"
    )

gs2328fError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 4)
)
gs2328fError.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fError.setStatus(
        "current"
    )

gs2328fWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 5)
)
gs2328fWarning.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fWarning.setStatus(
        "current"
    )

gs2328fNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 6)
)
gs2328fNotice.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fNotice.setStatus(
        "current"
    )

gs2328fInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 7)
)
gs2328fInformational.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fInformational.setStatus(
        "current"
    )

gs2328fDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2332, 5, 1, 8)
)
gs2328fDebug.setObjects(
    ("LANCOM-GS-2328F-MIB", "gs2328fInformation")
)
if mibBuilder.loadTexts:
    gs2328fDebug.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-GS-2328F-MIB",
    **{"lancom-systems": lancom_systems,
       "switchingSystems": switchingSystems,
       "gigabitEthernetSwitches": gigabitEthernetSwitches,
       "lancomGS2328F": lancomGS2328F,
       "gs2328fSystem": gs2328fSystem,
       "gs2328fSystemInformation": gs2328fSystemInformation,
       "gs2328fModelName": gs2328fModelName,
       "gs2328fBIOSVersion": gs2328fBIOSVersion,
       "gs2328fFirmwareVersion": gs2328fFirmwareVersion,
       "gs2328fHardwareMechanicalVersion": gs2328fHardwareMechanicalVersion,
       "gs2328fSerialNumber": gs2328fSerialNumber,
       "gs2328fHostMACAddress": gs2328fHostMACAddress,
       "gs2328fConsoleBaudrate": gs2328fConsoleBaudrate,
       "gs2328fRAMSize": gs2328fRAMSize,
       "gs2328fFlashSize": gs2328fFlashSize,
       "gs2328fBridgeFDBSize": gs2328fBridgeFDBSize,
       "gs2328fTransmitQueue": gs2328fTransmitQueue,
       "gs2328fMaximumFrameSize": gs2328fMaximumFrameSize,
       "gs2328fCPULoad": gs2328fCPULoad,
       "gs2328fFanSpeed": gs2328fFanSpeed,
       "gs2328fACPower": gs2328fACPower,
       "gs2328fTemperature": gs2328fTemperature,
       "gs2328fDCPower": gs2328fDCPower,
       "gs2328fSystemDescription": gs2328fSystemDescription,
       "gs2328fLocation": gs2328fLocation,
       "gs2328fContact": gs2328fContact,
       "gs2328fDeviceName": gs2328fDeviceName,
       "gs2328fSystemDate": gs2328fSystemDate,
       "gs2328fSystemUptime": gs2328fSystemUptime,
       "gs2328fSystemIPv4Address": gs2328fSystemIPv4Address,
       "gs2328fSystemIPv4SubnetMask": gs2328fSystemIPv4SubnetMask,
       "gs2328fSystemIPv4Gateway": gs2328fSystemIPv4Gateway,
       "gs2328fIPv6LinkLocalAddress": gs2328fIPv6LinkLocalAddress,
       "gs2328fIPv6Address": gs2328fIPv6Address,
       "gs2328fIPv6Prefix": gs2328fIPv6Prefix,
       "gs2328fIPv6Gateway": gs2328fIPv6Gateway,
       "gs2328fLargestFreeMemBlock": gs2328fLargestFreeMemBlock,
       "gs2328fMemFree": gs2328fMemFree,
       "gs2328fSystemTime": gs2328fSystemTime,
       "gs2328fSystemTimeManual": gs2328fSystemTimeManual,
       "gs2328fSystemTimeManualClockSource": gs2328fSystemTimeManualClockSource,
       "gs2328fSystemTimeManualLocaltime": gs2328fSystemTimeManualLocaltime,
       "gs2328fSystemTimeManualTimeZoneOffset": gs2328fSystemTimeManualTimeZoneOffset,
       "gs2328fSystemTimeManualDaylightSavings": gs2328fSystemTimeManualDaylightSavings,
       "gs2328fSystemTimeManualTimeSetOffset": gs2328fSystemTimeManualTimeSetOffset,
       "gs2328fSystemTimeManualDaylightSavingsType": gs2328fSystemTimeManualDaylightSavingsType,
       "gs2328fSystemTimeManualDaylightSavingsBydatesFrom": gs2328fSystemTimeManualDaylightSavingsBydatesFrom,
       "gs2328fSystemTimeManualDaylightSavingsBydatesTo": gs2328fSystemTimeManualDaylightSavingsBydatesTo,
       "gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom": gs2328fSystemTimeManualDaylightSavingsRecurringDayFrom,
       "gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom": gs2328fSystemTimeManualDaylightSavingsRecurringWeekFrom,
       "gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom": gs2328fSystemTimeManualDaylightSavingsRecurringMonthFrom,
       "gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom": gs2328fSystemTimeManualDaylightSavingsRecurringTimeFrom,
       "gs2328fSystemTimeManualDaylightSavingsRecurringDayTo": gs2328fSystemTimeManualDaylightSavingsRecurringDayTo,
       "gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo": gs2328fSystemTimeManualDaylightSavingsRecurringWeekTo,
       "gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo": gs2328fSystemTimeManualDaylightSavingsRecurringMonthTo,
       "gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo": gs2328fSystemTimeManualDaylightSavingsRecurringTimeTo,
       "gs2328fSystemTimeNTP": gs2328fSystemTimeNTP,
       "gs2328fSystemTimeNTPTable": gs2328fSystemTimeNTPTable,
       "gs2328fSystemTimeNTPEntry": gs2328fSystemTimeNTPEntry,
       "gs2328fSystemTimeNTPIndex": gs2328fSystemTimeNTPIndex,
       "gs2328fSystemTimeNTPServerIPType": gs2328fSystemTimeNTPServerIPType,
       "gs2328fSystemTimeNTPServer": gs2328fSystemTimeNTPServer,
       "gs2328fSystemTimeNTPCurrentMode": gs2328fSystemTimeNTPCurrentMode,
       "gs2328fSystemTimeNTPRequestInterval": gs2328fSystemTimeNTPRequestInterval,
       "gs2328fSystemTimeNTPTriesNumber": gs2328fSystemTimeNTPTriesNumber,
       "gs2328fSystemAccount": gs2328fSystemAccount,
       "gs2328fSystemAccountUsers": gs2328fSystemAccountUsers,
       "gs2328fSystemAccountUserCreate": gs2328fSystemAccountUserCreate,
       "gs2328fSystemAccountUsersTable": gs2328fSystemAccountUsersTable,
       "gs2328fSystemAccountUsersEntry": gs2328fSystemAccountUsersEntry,
       "gs2328fUserIndex": gs2328fUserIndex,
       "gs2328fUserName": gs2328fUserName,
       "gs2328fPassword": gs2328fPassword,
       "gs2328fUserPrivilegeLevel": gs2328fUserPrivilegeLevel,
       "gs2328fAccountUserRowStatus": gs2328fAccountUserRowStatus,
       "gs2328fSystemAccountUsersSuperUserPassword": gs2328fSystemAccountUsersSuperUserPassword,
       "gs2328fSystemAccountEnforcePasswordRules": gs2328fSystemAccountEnforcePasswordRules,
       "gs2328fSystemAccountPrivilegeLevel": gs2328fSystemAccountPrivilegeLevel,
       "gs2328fAccountPrivilegeLevel": gs2328fAccountPrivilegeLevel,
       "gs2328fAggregationPrivilegeLevel": gs2328fAggregationPrivilegeLevel,
       "gs2328fDiagnosticsPrivilegeLevel": gs2328fDiagnosticsPrivilegeLevel,
       "gs2328fEEEPrivilegeLevel": gs2328fEEEPrivilegeLevel,
       "gs2328fEasyportPrivilegeLevel": gs2328fEasyportPrivilegeLevel,
       "gs2328fGARPPrivilegeLevel": gs2328fGARPPrivilegeLevel,
       "gs2328fGVRPPrivilegeLevel": gs2328fGVRPPrivilegeLevel,
       "gs2328fIPPrivilegeLevel": gs2328fIPPrivilegeLevel,
       "gs2328fIPMCSnoopingPrivilegeLevel": gs2328fIPMCSnoopingPrivilegeLevel,
       "gs2328fLACPPrivilegeLevel": gs2328fLACPPrivilegeLevel,
       "gs2328fLLDPPrivilegeLevel": gs2328fLLDPPrivilegeLevel,
       "gs2328fLLDPMEDPrivilegeLevel": gs2328fLLDPMEDPrivilegeLevel,
       "gs2328fLoopProtectPrivilegeLevel": gs2328fLoopProtectPrivilegeLevel,
       "gs2328fMACTablePrivilegeLevel": gs2328fMACTablePrivilegeLevel,
       "gs2328fMVRPrivilegeLevel": gs2328fMVRPrivilegeLevel,
       "gs2328fMaintenancePrivilegeLevel": gs2328fMaintenancePrivilegeLevel,
       "gs2328fMirroringPrivilegeLevel": gs2328fMirroringPrivilegeLevel,
       "gs2328fPortsPrivilegeLevel": gs2328fPortsPrivilegeLevel,
       "gs2328fPrivateVLANsPrivilegeLevel": gs2328fPrivateVLANsPrivilegeLevel,
       "gs2328fQoSPrivilegeLevel": gs2328fQoSPrivilegeLevel,
       "gs2328fSFlowPrivilegeLevel": gs2328fSFlowPrivilegeLevel,
       "gs2328fSMTPPrivilegeLevel": gs2328fSMTPPrivilegeLevel,
       "gs2328fSNMPPrivilegeLevel": gs2328fSNMPPrivilegeLevel,
       "gs2328fSecurityPrivilegeLevel": gs2328fSecurityPrivilegeLevel,
       "gs2328fSingleIPPrivilegeLevel": gs2328fSingleIPPrivilegeLevel,
       "gs2328fSpanningTreePrivilegeLevel": gs2328fSpanningTreePrivilegeLevel,
       "gs2328fSystemPrivilegeLevel": gs2328fSystemPrivilegeLevel,
       "gs2328fTrapEventPrivilegeLevel": gs2328fTrapEventPrivilegeLevel,
       "gs2328fUPnPPrivilegeLevel": gs2328fUPnPPrivilegeLevel,
       "gs2328fVCLPrivilegeLevel": gs2328fVCLPrivilegeLevel,
       "gs2328fVLANsPrivilegeLevel": gs2328fVLANsPrivilegeLevel,
       "gs2328fVoiceVLANPrivilegeLevel": gs2328fVoiceVLANPrivilegeLevel,
       "gs2328fIP": gs2328fIP,
       "gs2328fIPv4": gs2328fIPv4,
       "gs2328fIPv4Configured": gs2328fIPv4Configured,
       "gs2328fIpv4DHCPClient": gs2328fIpv4DHCPClient,
       "gs2328fIPv4Address": gs2328fIPv4Address,
       "gs2328fIPv4Mask": gs2328fIPv4Mask,
       "gs2328fIPv4Gateway": gs2328fIPv4Gateway,
       "gs2328fIPv4VLANId": gs2328fIPv4VLANId,
       "gs2328fIPv4DNSServer": gs2328fIPv4DNSServer,
       "gs2328fIPv4DNSProxy": gs2328fIPv4DNSProxy,
       "gs2328fIPv4Current": gs2328fIPv4Current,
       "gs2328fIpv4CurrentDHCPClient": gs2328fIpv4CurrentDHCPClient,
       "gs2328fIPv4CurrentAddress": gs2328fIPv4CurrentAddress,
       "gs2328fIPv4CurrentMask": gs2328fIPv4CurrentMask,
       "gs2328fIPv4CurrentGateway": gs2328fIPv4CurrentGateway,
       "gs2328fIPv4CurrentVLANId": gs2328fIPv4CurrentVLANId,
       "gs2328fIPv4CurrentDNSServer": gs2328fIPv4CurrentDNSServer,
       "gs2328fIPv6": gs2328fIPv6,
       "gs2328fIPv6Configured": gs2328fIPv6Configured,
       "gs2328fIpv6AutoConfiguration": gs2328fIpv6AutoConfiguration,
       "gs2328fIpv6Address": gs2328fIpv6Address,
       "gs2328fIpv6Prefix": gs2328fIpv6Prefix,
       "gs2328fIpv6Gateway": gs2328fIpv6Gateway,
       "gs2328fIPv6Current": gs2328fIPv6Current,
       "gs2328fIpv6CurrentAutoConfiguration": gs2328fIpv6CurrentAutoConfiguration,
       "gs2328fIpv6CurrentAddress": gs2328fIpv6CurrentAddress,
       "gs2328fIpv6CurrentLinkLocalAddress": gs2328fIpv6CurrentLinkLocalAddress,
       "gs2328fIpv6CurrentPrefix": gs2328fIpv6CurrentPrefix,
       "gs2328fIpv6CurrentGateway": gs2328fIpv6CurrentGateway,
       "gs2328fSyslog": gs2328fSyslog,
       "gs2328fSyslogConf": gs2328fSyslogConf,
       "gs2328fServerMode": gs2328fServerMode,
       "gs2328fServerAddress1": gs2328fServerAddress1,
       "gs2328fServerAddress2": gs2328fServerAddress2,
       "gs2328fSyslogLevel": gs2328fSyslogLevel,
       "gs2328fSyslogDetailedInfo": gs2328fSyslogDetailedInfo,
       "gs2328fSyslogDetailedInfoClear": gs2328fSyslogDetailedInfoClear,
       "gs2328fSyslogDetailedInfoTable": gs2328fSyslogDetailedInfoTable,
       "gs2328fSyslogDetailedInfoEntry": gs2328fSyslogDetailedInfoEntry,
       "gs2328fSyslogDetailedInfoIndex": gs2328fSyslogDetailedInfoIndex,
       "gs2328fSyslogDetailedInfoLevel": gs2328fSyslogDetailedInfoLevel,
       "gs2328fSyslogDetailedInfoTime": gs2328fSyslogDetailedInfoTime,
       "gs2328fSyslogDetailedInfoMessage": gs2328fSyslogDetailedInfoMessage,
       "gs2328fSnmp": gs2328fSnmp,
       "gs2328fSnmpConf": gs2328fSnmpConf,
       "gs2328fGetCommunityMode": gs2328fGetCommunityMode,
       "gs2328fGetCommunity": gs2328fGetCommunity,
       "gs2328fSetCommunityMode": gs2328fSetCommunityMode,
       "gs2328fSetCommunity": gs2328fSetCommunity,
       "gs2328fGetCommunityConfTable": gs2328fGetCommunityConfTable,
       "gs2328fGetCommunityConfEntry": gs2328fGetCommunityConfEntry,
       "gs2328fCommunityConfIndex": gs2328fCommunityConfIndex,
       "gs2328fCommunityConfGetCommunity": gs2328fCommunityConfGetCommunity,
       "gs2328fTrapHostConfTable": gs2328fTrapHostConfTable,
       "gs2328fTrapHostConfEntry": gs2328fTrapHostConfEntry,
       "gs2328fTrapHostConfIndex": gs2328fTrapHostConfIndex,
       "gs2328fTrapHostConfVersion": gs2328fTrapHostConfVersion,
       "gs2328fTrapHostConfIPType": gs2328fTrapHostConfIPType,
       "gs2328fTrapHostConfIP": gs2328fTrapHostConfIP,
       "gs2328fTrapHostConfPort": gs2328fTrapHostConfPort,
       "gs2328fTrapHostConfCommunity": gs2328fTrapHostConfCommunity,
       "gs2328fTrapHostConfSeverityLevel": gs2328fTrapHostConfSeverityLevel,
       "gs2328fTrapHostConfSecurityLevel": gs2328fTrapHostConfSecurityLevel,
       "gs2328fTrapHostConfAuthPtc": gs2328fTrapHostConfAuthPtc,
       "gs2328fTrapHostConfAuthPassword": gs2328fTrapHostConfAuthPassword,
       "gs2328fTrapHostConfPrivPtc": gs2328fTrapHostConfPrivPtc,
       "gs2328fTrapHostConfPrivPassword": gs2328fTrapHostConfPrivPassword,
       "gs2328fTrapHostConfCurrentMode": gs2328fTrapHostConfCurrentMode,
       "gs2328fSnmpSystem": gs2328fSnmpSystem,
       "gs2328fSnmpState": gs2328fSnmpState,
       "gs2328fSnmpEngineID": gs2328fSnmpEngineID,
       "gs2328fSnmpCommunities": gs2328fSnmpCommunities,
       "gs2328fSnmpCommunitiesCreate": gs2328fSnmpCommunitiesCreate,
       "gs2328fSnmpCommunitiesTable": gs2328fSnmpCommunitiesTable,
       "gs2328fSnmpCommunitiesEntry": gs2328fSnmpCommunitiesEntry,
       "gs2328fSnmpCommunitiesIndex": gs2328fSnmpCommunitiesIndex,
       "gs2328fSnmpCommunitiesCommunity": gs2328fSnmpCommunitiesCommunity,
       "gs2328fSnmpCommunitiesUserName": gs2328fSnmpCommunitiesUserName,
       "gs2328fSnmpCommunitiesSourceIP": gs2328fSnmpCommunitiesSourceIP,
       "gs2328fSnmpCommunitiesSourceMask": gs2328fSnmpCommunitiesSourceMask,
       "gs2328fSnmpCommunitiesRowStatus": gs2328fSnmpCommunitiesRowStatus,
       "gs2328fSnmpUsers": gs2328fSnmpUsers,
       "gs2328fSnmpUsersCreate": gs2328fSnmpUsersCreate,
       "gs2328fSnmpUsersTable": gs2328fSnmpUsersTable,
       "gs2328fSnmpUsersEntry": gs2328fSnmpUsersEntry,
       "gs2328fSnmpUsersIndex": gs2328fSnmpUsersIndex,
       "gs2328fSnmpUsersUserName": gs2328fSnmpUsersUserName,
       "gs2328fSnmpUsersSecurityLevel": gs2328fSnmpUsersSecurityLevel,
       "gs2328fSnmpUsersAuthenticationProtocol": gs2328fSnmpUsersAuthenticationProtocol,
       "gs2328fSnmpUsersAuthenticationPassword": gs2328fSnmpUsersAuthenticationPassword,
       "gs2328fSnmpUsersPrivacyProtocol": gs2328fSnmpUsersPrivacyProtocol,
       "gs2328fSnmpUsersPrivacyPassword": gs2328fSnmpUsersPrivacyPassword,
       "gs2328fSnmpUsersRowStatus": gs2328fSnmpUsersRowStatus,
       "gs2328fSnmpGroups": gs2328fSnmpGroups,
       "gs2328fSnmpGroupsCreate": gs2328fSnmpGroupsCreate,
       "gs2328fSnmpGroupsTable": gs2328fSnmpGroupsTable,
       "gs2328fSnmpGroupsEntry": gs2328fSnmpGroupsEntry,
       "gs2328fSnmpGroupsIndex": gs2328fSnmpGroupsIndex,
       "gs2328fSnmpGroupsSecurityModel": gs2328fSnmpGroupsSecurityModel,
       "gs2328fSnmpGroupsSecurityName": gs2328fSnmpGroupsSecurityName,
       "gs2328fSnmpGroupsGroupName": gs2328fSnmpGroupsGroupName,
       "gs2328fSnmpGroupsRowStatus": gs2328fSnmpGroupsRowStatus,
       "gs2328fSnmpViews": gs2328fSnmpViews,
       "gs2328fSnmpViewsCreate": gs2328fSnmpViewsCreate,
       "gs2328fSnmpViewsTable": gs2328fSnmpViewsTable,
       "gs2328fSnmpViewsEntry": gs2328fSnmpViewsEntry,
       "gs2328fSnmpViewsIndex": gs2328fSnmpViewsIndex,
       "gs2328fSnmpViewsName": gs2328fSnmpViewsName,
       "gs2328fSnmpViewsType": gs2328fSnmpViewsType,
       "gs2328fSnmpViewsOIDSubtree": gs2328fSnmpViewsOIDSubtree,
       "gs2328fSnmpViewsRowStatus": gs2328fSnmpViewsRowStatus,
       "gs2328fSnmpAccess": gs2328fSnmpAccess,
       "gs2328fSnmpAccessCreate": gs2328fSnmpAccessCreate,
       "gs2328fSnmpAccessTable": gs2328fSnmpAccessTable,
       "gs2328fSnmpAccessEntry": gs2328fSnmpAccessEntry,
       "gs2328fSnmpAccessIndex": gs2328fSnmpAccessIndex,
       "gs2328fSnmpAccessGroupName": gs2328fSnmpAccessGroupName,
       "gs2328fSnmpAccessSecurityModel": gs2328fSnmpAccessSecurityModel,
       "gs2328fSnmpAccessSecurityLevel": gs2328fSnmpAccessSecurityLevel,
       "gs2328fSnmpAccessReadViewName": gs2328fSnmpAccessReadViewName,
       "gs2328fSnmpAccessWriteViewName": gs2328fSnmpAccessWriteViewName,
       "gs2328fSnmpAccessRowStatus": gs2328fSnmpAccessRowStatus,
       "gs2328fConfiguration": gs2328fConfiguration,
       "gs2328fPort": gs2328fPort,
       "gs2328fPortConfigurationTable": gs2328fPortConfigurationTable,
       "gs2328fPortConfigurationEntry": gs2328fPortConfigurationEntry,
       "gs2328fPortConfPort": gs2328fPortConfPort,
       "gs2328fPortConfPortMedia": gs2328fPortConfPortMedia,
       "gs2328fPortConfLink": gs2328fPortConfLink,
       "gs2328fPortConfCurrentSpeed": gs2328fPortConfCurrentSpeed,
       "gs2328fPortConfSpeed": gs2328fPortConfSpeed,
       "gs2328fPortConfCurrentFlowControlRx": gs2328fPortConfCurrentFlowControlRx,
       "gs2328fPortConfCurrentFlowControlTx": gs2328fPortConfCurrentFlowControlTx,
       "gs2328fPortConfFlowControl": gs2328fPortConfFlowControl,
       "gs2328fPortConfMaxFrameSize": gs2328fPortConfMaxFrameSize,
       "gs2328fPortConfExcessiveCollisionMode": gs2328fPortConfExcessiveCollisionMode,
       "gs2328fPortConfPowerControl": gs2328fPortConfPowerControl,
       "gs2328fPortConfDescription": gs2328fPortConfDescription,
       "gs2328fPortTrafficStatisticsTable": gs2328fPortTrafficStatisticsTable,
       "gs2328fPortTrafficStatisticsEntry": gs2328fPortTrafficStatisticsEntry,
       "gs2328fPortTrafficStatisticsPort": gs2328fPortTrafficStatisticsPort,
       "gs2328fPortTrafficStatisticsClear": gs2328fPortTrafficStatisticsClear,
       "gs2328fPortTrafficRxPackets": gs2328fPortTrafficRxPackets,
       "gs2328fPortTrafficRxOctets": gs2328fPortTrafficRxOctets,
       "gs2328fPortTrafficRxUnicast": gs2328fPortTrafficRxUnicast,
       "gs2328fPortTrafficRxMulticast": gs2328fPortTrafficRxMulticast,
       "gs2328fPortTrafficRxBroadcast": gs2328fPortTrafficRxBroadcast,
       "gs2328fPortTrafficRxPause": gs2328fPortTrafficRxPause,
       "gs2328fPortTrafficRx64Bytes": gs2328fPortTrafficRx64Bytes,
       "gs2328fPortTrafficRx65to127Bytes": gs2328fPortTrafficRx65to127Bytes,
       "gs2328fPortTrafficRx128to255Bytes": gs2328fPortTrafficRx128to255Bytes,
       "gs2328fPortTrafficRx256to511Bytes": gs2328fPortTrafficRx256to511Bytes,
       "gs2328fPortTrafficRx512to1023Bytes": gs2328fPortTrafficRx512to1023Bytes,
       "gs2328fPortTrafficRx1024to1526Bytes": gs2328fPortTrafficRx1024to1526Bytes,
       "gs2328fPortTrafficRxExceecd1527Bytes": gs2328fPortTrafficRxExceecd1527Bytes,
       "gs2328fPortTrafficRxQ0": gs2328fPortTrafficRxQ0,
       "gs2328fPortTrafficRxQ1": gs2328fPortTrafficRxQ1,
       "gs2328fPortTrafficRxQ2": gs2328fPortTrafficRxQ2,
       "gs2328fPortTrafficRxQ3": gs2328fPortTrafficRxQ3,
       "gs2328fPortTrafficRxQ4": gs2328fPortTrafficRxQ4,
       "gs2328fPortTrafficRxQ5": gs2328fPortTrafficRxQ5,
       "gs2328fPortTrafficRxQ6": gs2328fPortTrafficRxQ6,
       "gs2328fPortTrafficRxQ7": gs2328fPortTrafficRxQ7,
       "gs2328fPortTrafficRxDrops": gs2328fPortTrafficRxDrops,
       "gs2328fPortTrafficRxCRCorAlignment": gs2328fPortTrafficRxCRCorAlignment,
       "gs2328fPortTrafficRxUndersize": gs2328fPortTrafficRxUndersize,
       "gs2328fPortTrafficRxOversize": gs2328fPortTrafficRxOversize,
       "gs2328fPortTrafficRxFragments": gs2328fPortTrafficRxFragments,
       "gs2328fPortTrafficRxJabber": gs2328fPortTrafficRxJabber,
       "gs2328fPortTrafficRxFiltered": gs2328fPortTrafficRxFiltered,
       "gs2328fPortTrafficTxPackets": gs2328fPortTrafficTxPackets,
       "gs2328fPortTrafficTxOctets": gs2328fPortTrafficTxOctets,
       "gs2328fPortTrafficTxUnicast": gs2328fPortTrafficTxUnicast,
       "gs2328fPortTrafficTxMulticast": gs2328fPortTrafficTxMulticast,
       "gs2328fPortTrafficTxBroadcast": gs2328fPortTrafficTxBroadcast,
       "gs2328fPortTrafficTxPause": gs2328fPortTrafficTxPause,
       "gs2328fPortTrafficTx64Bytes": gs2328fPortTrafficTx64Bytes,
       "gs2328fPortTrafficTx65to127Bytes": gs2328fPortTrafficTx65to127Bytes,
       "gs2328fPortTrafficTx128to255Bytes": gs2328fPortTrafficTx128to255Bytes,
       "gs2328fPortTrafficTx256to511Bytes": gs2328fPortTrafficTx256to511Bytes,
       "gs2328fPortTrafficTx512to1023Bytes": gs2328fPortTrafficTx512to1023Bytes,
       "gs2328fPortTrafficTx1024to1526Bytes": gs2328fPortTrafficTx1024to1526Bytes,
       "gs2328fPortTrafficTxExceecd1527Bytes": gs2328fPortTrafficTxExceecd1527Bytes,
       "gs2328fPortTrafficTxQ0": gs2328fPortTrafficTxQ0,
       "gs2328fPortTrafficTxQ1": gs2328fPortTrafficTxQ1,
       "gs2328fPortTrafficTxQ2": gs2328fPortTrafficTxQ2,
       "gs2328fPortTrafficTxQ3": gs2328fPortTrafficTxQ3,
       "gs2328fPortTrafficTxQ4": gs2328fPortTrafficTxQ4,
       "gs2328fPortTrafficTxQ5": gs2328fPortTrafficTxQ5,
       "gs2328fPortTrafficTxQ6": gs2328fPortTrafficTxQ6,
       "gs2328fPortTrafficTxQ7": gs2328fPortTrafficTxQ7,
       "gs2328fPortTrafficTxDrops": gs2328fPortTrafficTxDrops,
       "gs2328fPortTrafficTxLateOrExcColl": gs2328fPortTrafficTxLateOrExcColl,
       "gs2328fPortQoSStatistics": gs2328fPortQoSStatistics,
       "gs2328fPortQoSStatisticsClear": gs2328fPortQoSStatisticsClear,
       "gs2328fPortQoSStatisticsTable": gs2328fPortQoSStatisticsTable,
       "gs2328fPortQoSStatisticsEntry": gs2328fPortQoSStatisticsEntry,
       "gs2328fPortQoSStatisticsPort": gs2328fPortQoSStatisticsPort,
       "gs2328fPortQoSQ0Rx": gs2328fPortQoSQ0Rx,
       "gs2328fPortQoSQ0Tx": gs2328fPortQoSQ0Tx,
       "gs2328fPortQoSQ1Rx": gs2328fPortQoSQ1Rx,
       "gs2328fPortQoSQ1Tx": gs2328fPortQoSQ1Tx,
       "gs2328fPortQoSQ2Rx": gs2328fPortQoSQ2Rx,
       "gs2328fPortQoSQ2Tx": gs2328fPortQoSQ2Tx,
       "gs2328fPortQoSQ3Rx": gs2328fPortQoSQ3Rx,
       "gs2328fPortQoSQ3Tx": gs2328fPortQoSQ3Tx,
       "gs2328fPortQoSQ4Rx": gs2328fPortQoSQ4Rx,
       "gs2328fPortQoSQ4Tx": gs2328fPortQoSQ4Tx,
       "gs2328fPortQoSQ5Rx": gs2328fPortQoSQ5Rx,
       "gs2328fPortQoSQ5Tx": gs2328fPortQoSQ5Tx,
       "gs2328fPortQoSQ6Rx": gs2328fPortQoSQ6Rx,
       "gs2328fPortQoSQ6Tx": gs2328fPortQoSQ6Tx,
       "gs2328fPortQoSQ7Rx": gs2328fPortQoSQ7Rx,
       "gs2328fPortQoSQ7Tx": gs2328fPortQoSQ7Tx,
       "gs2328fSFPInfoTable": gs2328fSFPInfoTable,
       "gs2328fSFPInfoEntry": gs2328fSFPInfoEntry,
       "gs2328fSFPInfoIndex": gs2328fSFPInfoIndex,
       "gs2328fSFPInfoPort": gs2328fSFPInfoPort,
       "gs2328fSFPConnectorType": gs2328fSFPConnectorType,
       "gs2328fSFPFiberType": gs2328fSFPFiberType,
       "gs2328fSFPTxCentralWavelength": gs2328fSFPTxCentralWavelength,
       "gs2328fSFPBaudRate": gs2328fSFPBaudRate,
       "gs2328fSFPVendorOUI": gs2328fSFPVendorOUI,
       "gs2328fSFPVendorName": gs2328fSFPVendorName,
       "gs2328fSFPVendorPN": gs2328fSFPVendorPN,
       "gs2328fSFPVendorRev": gs2328fSFPVendorRev,
       "gs2328fSFPVendorSN": gs2328fSFPVendorSN,
       "gs2328fSFPDateCode": gs2328fSFPDateCode,
       "gs2328fSFPTemperature": gs2328fSFPTemperature,
       "gs2328fSFPVcc": gs2328fSFPVcc,
       "gs2328fSFPMon1Bias": gs2328fSFPMon1Bias,
       "gs2328fSFPMon2TxPWR": gs2328fSFPMon2TxPWR,
       "gs2328fSFPMon3RxPWR": gs2328fSFPMon3RxPWR,
       "gs2328fVoiceVLAN": gs2328fVoiceVLAN,
       "gs2328fVoiceVLANConf": gs2328fVoiceVLANConf,
       "gs2328fVoiceVLANMode": gs2328fVoiceVLANMode,
       "gs2328fVoiceVLANVLANId": gs2328fVoiceVLANVLANId,
       "gs2328fVoiceVLANAgingTime": gs2328fVoiceVLANAgingTime,
       "gs2328fVoiceVLANTrafficClass": gs2328fVoiceVLANTrafficClass,
       "gs2328fVoiceVLANPortTable": gs2328fVoiceVLANPortTable,
       "gs2328fVoiceVLANPortEntry": gs2328fVoiceVLANPortEntry,
       "gs2328fVoiceVLANPort": gs2328fVoiceVLANPort,
       "gs2328fVoiceVLANPortMode": gs2328fVoiceVLANPortMode,
       "gs2328fVoiceVLANPortSecurity": gs2328fVoiceVLANPortSecurity,
       "gs2328fVoiceVLANPortDiscoveryProtocol": gs2328fVoiceVLANPortDiscoveryProtocol,
       "gs2328fVoiceVLANSkipNAS": gs2328fVoiceVLANSkipNAS,
       "gs2328fVoiceVLANOUI": gs2328fVoiceVLANOUI,
       "gs2328fVoiceVLANOUICreate": gs2328fVoiceVLANOUICreate,
       "gs2328fVoiceVLANOUITable": gs2328fVoiceVLANOUITable,
       "gs2328fVoiceVLANOUIEntry": gs2328fVoiceVLANOUIEntry,
       "gs2328fVoiceVLANOUIIndex": gs2328fVoiceVLANOUIIndex,
       "gs2328fVoiceVLANTelephonyOUI": gs2328fVoiceVLANTelephonyOUI,
       "gs2328fVoiceVLANDescription": gs2328fVoiceVLANDescription,
       "gs2328fVoiceVLANOUIRowStatus": gs2328fVoiceVLANOUIRowStatus,
       "gs2328fGARP": gs2328fGARP,
       "gs2328fGARPConfTable": gs2328fGARPConfTable,
       "gs2328fGARPConfEntry": gs2328fGARPConfEntry,
       "gs2328fGARPConfPort": gs2328fGARPConfPort,
       "gs2328fGARPJoinTimer": gs2328fGARPJoinTimer,
       "gs2328fGARPLeaveTimer": gs2328fGARPLeaveTimer,
       "gs2328fGARPLeaveAllTimer": gs2328fGARPLeaveAllTimer,
       "gs2328fGARPApplicantion": gs2328fGARPApplicantion,
       "gs2328fGARPAttributeType": gs2328fGARPAttributeType,
       "gs2328fGARPApplicant": gs2328fGARPApplicant,
       "gs2328fGARPStatisticsTable": gs2328fGARPStatisticsTable,
       "gs2328fGARPStatisticsEntry": gs2328fGARPStatisticsEntry,
       "gs2328fGARPStatisticsPort": gs2328fGARPStatisticsPort,
       "gs2328fGARPStatisticsPeerMAC": gs2328fGARPStatisticsPeerMAC,
       "gs2328fGARPStatisticsFailedCount": gs2328fGARPStatisticsFailedCount,
       "gs2328fGVRP": gs2328fGVRP,
       "gs2328fGVRPConf": gs2328fGVRPConf,
       "gs2328fGVRPMode": gs2328fGVRPMode,
       "gs2328fGVRPConfTable": gs2328fGVRPConfTable,
       "gs2328fGVRPConfEntry": gs2328fGVRPConfEntry,
       "gs2328fGVRPConfPort": gs2328fGVRPConfPort,
       "gs2328fGVRPConfPortMode": gs2328fGVRPConfPortMode,
       "gs2328fGVRPConfPortRRole": gs2328fGVRPConfPortRRole,
       "gs2328fGVRPStatisticsTable": gs2328fGVRPStatisticsTable,
       "gs2328fGVRPStatisticsEntry": gs2328fGVRPStatisticsEntry,
       "gs2328fGVRPStatisticsPort": gs2328fGVRPStatisticsPort,
       "gs2328fGVRPStatisticsJoinTxCnt": gs2328fGVRPStatisticsJoinTxCnt,
       "gs2328fGVRPStatisticsLeaveTxCnt": gs2328fGVRPStatisticsLeaveTxCnt,
       "gs2328fMirroring": gs2328fMirroring,
       "gs2328fPortToMirrorOn": gs2328fPortToMirrorOn,
       "gs2328fMirrorTable": gs2328fMirrorTable,
       "gs2328fMirrorEntry": gs2328fMirrorEntry,
       "gs2328fMirrorPort": gs2328fMirrorPort,
       "gs2328fMirrorMode": gs2328fMirrorMode,
       "gs2328fTrapEventSeverity": gs2328fTrapEventSeverity,
       "gs2328fTrapEventSeverityACL": gs2328fTrapEventSeverityACL,
       "gs2328fTrapEventSeverityACLLog": gs2328fTrapEventSeverityACLLog,
       "gs2328fTrapEventSeverityAccessMgmt": gs2328fTrapEventSeverityAccessMgmt,
       "gs2328fTrapEventSeverityAuthFailed": gs2328fTrapEventSeverityAuthFailed,
       "gs2328fTrapEventSeverityColdStart": gs2328fTrapEventSeverityColdStart,
       "gs2328fTrapEventSeverityConfigInfo": gs2328fTrapEventSeverityConfigInfo,
       "gs2328fTrapEventSeverityFirmwareUpgrade": gs2328fTrapEventSeverityFirmwareUpgrade,
       "gs2328fTrapEventSeverityImportExport": gs2328fTrapEventSeverityImportExport,
       "gs2328fTrapEventSeverityLACP": gs2328fTrapEventSeverityLACP,
       "gs2328fTrapEventSeverityLinkStatus": gs2328fTrapEventSeverityLinkStatus,
       "gs2328fTrapEventSeverityLogin": gs2328fTrapEventSeverityLogin,
       "gs2328fTrapEventSeverityLogout": gs2328fTrapEventSeverityLogout,
       "gs2328fTrapEventSeverityLoopProtect": gs2328fTrapEventSeverityLoopProtect,
       "gs2328fTrapEventSeverityMgmtIPChange": gs2328fTrapEventSeverityMgmtIPChange,
       "gs2328fTrapEventSeverityModuleChange": gs2328fTrapEventSeverityModuleChange,
       "gs2328fTrapEventSeverityNAS": gs2328fTrapEventSeverityNAS,
       "gs2328fTrapEventSeverityPasswordChange": gs2328fTrapEventSeverityPasswordChange,
       "gs2328fTrapEventSeverityPortSecurity": gs2328fTrapEventSeverityPortSecurity,
       "gs2328fTrapEventSeverityVLAN": gs2328fTrapEventSeverityVLAN,
       "gs2328fTrapEventSeverityWarmStart": gs2328fTrapEventSeverityWarmStart,
       "gs2328fTrapEventSeverityARPConflict": gs2328fTrapEventSeverityARPConflict,
       "gs2328fTrapEventSeveritySpoofingLimit": gs2328fTrapEventSeveritySpoofingLimit,
       "gs2328fTrapEventSeverityStaticARPConflict": gs2328fTrapEventSeverityStaticARPConflict,
       "gs2328fSMTP": gs2328fSMTP,
       "gs2328fSMTPMailServer": gs2328fSMTPMailServer,
       "gs2328fSMTPUserName": gs2328fSMTPUserName,
       "gs2328fSMTPPassword": gs2328fSMTPPassword,
       "gs2328fSMTPServeriryLevel": gs2328fSMTPServeriryLevel,
       "gs2328fSMTPSender": gs2328fSMTPSender,
       "gs2328fSMTPReturnPath": gs2328fSMTPReturnPath,
       "gs2328fSMTPEmailAddress1": gs2328fSMTPEmailAddress1,
       "gs2328fSMTPEmailAddress2": gs2328fSMTPEmailAddress2,
       "gs2328fSMTPEmailAddress3": gs2328fSMTPEmailAddress3,
       "gs2328fSMTPEmailAddress4": gs2328fSMTPEmailAddress4,
       "gs2328fSMTPEmailAddress5": gs2328fSMTPEmailAddress5,
       "gs2328fSMTPEmailAddress6": gs2328fSMTPEmailAddress6,
       "gs2328fACL": gs2328fACL,
       "gs2328fACLPortsConfTable": gs2328fACLPortsConfTable,
       "gs2328fACLPortsConfEntry": gs2328fACLPortsConfEntry,
       "gs2328fACLPortsConfPort": gs2328fACLPortsConfPort,
       "gs2328fACLPortsConfPolicyID": gs2328fACLPortsConfPolicyID,
       "gs2328fACLPortsConfAction": gs2328fACLPortsConfAction,
       "gs2328fACLPortsConfRateLimiterID": gs2328fACLPortsConfRateLimiterID,
       "gs2328fACLPortsConfPortRedirect": gs2328fACLPortsConfPortRedirect,
       "gs2328fACLPortsConfMirror": gs2328fACLPortsConfMirror,
       "gs2328fACLPortsConfLogging": gs2328fACLPortsConfLogging,
       "gs2328fACLPortsConfShutdown": gs2328fACLPortsConfShutdown,
       "gs2328fACLPortsConfState": gs2328fACLPortsConfState,
       "gs2328fACLPortsConfCounter": gs2328fACLPortsConfCounter,
       "gs2328fACLRateLimiterTable": gs2328fACLRateLimiterTable,
       "gs2328fACLRateLimiterEntry": gs2328fACLRateLimiterEntry,
       "gs2328fACLRateLimiterID": gs2328fACLRateLimiterID,
       "gs2328fACLRateLimiterUnit": gs2328fACLRateLimiterUnit,
       "gs2328fACLRateLimiterRate": gs2328fACLRateLimiterRate,
       "gs2328fACLACE": gs2328fACLACE,
       "gs2328fACLACECreate": gs2328fACLACECreate,
       "gs2328fACLACETable": gs2328fACLACETable,
       "gs2328fACLACEEntry": gs2328fACLACEEntry,
       "gs2328fACLACEIndex": gs2328fACLACEIndex,
       "gs2328fACLACEID": gs2328fACLACEID,
       "gs2328fACLACENextID": gs2328fACLACENextID,
       "gs2328fACLACEIngressPort": gs2328fACLACEIngressPort,
       "gs2328fACLACEPortPolicyNumber": gs2328fACLACEPortPolicyNumber,
       "gs2328fACLACEPortPolicyBitmask": gs2328fACLACEPortPolicyBitmask,
       "gs2328fACLACEFrameType": gs2328fACLACEFrameType,
       "gs2328fACLACEAction": gs2328fACLACEAction,
       "gs2328fACLACEDenyPortRedirect": gs2328fACLACEDenyPortRedirect,
       "gs2328fACLACELogging": gs2328fACLACELogging,
       "gs2328fACLACEMirror": gs2328fACLACEMirror,
       "gs2328fACLACERateLimiter": gs2328fACLACERateLimiter,
       "gs2328fACLACEShutdown": gs2328fACLACEShutdown,
       "gs2328fACLACEVLAN8021QTagged": gs2328fACLACEVLAN8021QTagged,
       "gs2328fACLACEVLANTagPriority": gs2328fACLACEVLANTagPriority,
       "gs2328fACLACEVLANVID": gs2328fACLACEVLANVID,
       "gs2328fACLACEEtherType": gs2328fACLACEEtherType,
       "gs2328fACLACESMAC": gs2328fACLACESMAC,
       "gs2328fACLACEDMACType": gs2328fACLACEDMACType,
       "gs2328fACLACEDMAC": gs2328fACLACEDMAC,
       "gs2328fACLACEArpOpcode": gs2328fACLACEArpOpcode,
       "gs2328fACLACEArpFlagsRequestReply": gs2328fACLACEArpFlagsRequestReply,
       "gs2328fACLACEArpFlagsArpSmac": gs2328fACLACEArpFlagsArpSmac,
       "gs2328fACLACEArpFlagsRarpDmac": gs2328fACLACEArpFlagsRarpDmac,
       "gs2328fACLACEArpFlagsLength": gs2328fACLACEArpFlagsLength,
       "gs2328fACLACEArpFlagsIp": gs2328fACLACEArpFlagsIp,
       "gs2328fACLACEArpFlagsEthernet": gs2328fACLACEArpFlagsEthernet,
       "gs2328fACLACESIPType": gs2328fACLACESIPType,
       "gs2328fACLACESIPIPAddress": gs2328fACLACESIPIPAddress,
       "gs2328fACLACESIPNetworkPrefix": gs2328fACLACESIPNetworkPrefix,
       "gs2328fACLACEDIPType": gs2328fACLACEDIPType,
       "gs2328fACLACEDIPIPAddress": gs2328fACLACEDIPIPAddress,
       "gs2328fACLACEDIPNetworkPrefix": gs2328fACLACEDIPNetworkPrefix,
       "gs2328fACLACEIPProtocol": gs2328fACLACEIPProtocol,
       "gs2328fACLACEIPFlagsTTL": gs2328fACLACEIPFlagsTTL,
       "gs2328fACLACEIPFlagsOptions": gs2328fACLACEIPFlagsOptions,
       "gs2328fACLACEIPFlagsFragment": gs2328fACLACEIPFlagsFragment,
       "gs2328fACLACEICMPType": gs2328fACLACEICMPType,
       "gs2328fACLACEICMPCode": gs2328fACLACEICMPCode,
       "gs2328fACLACESourcePortMin": gs2328fACLACESourcePortMin,
       "gs2328fACLACESourcePortMax": gs2328fACLACESourcePortMax,
       "gs2328fACLACEDestPortMin": gs2328fACLACEDestPortMin,
       "gs2328fACLACEDestPortMax": gs2328fACLACEDestPortMax,
       "gs2328fACLACETCPFlagsFin": gs2328fACLACETCPFlagsFin,
       "gs2328fACLACETCPFlagsSyn": gs2328fACLACETCPFlagsSyn,
       "gs2328fACLACETCPFlagsRst": gs2328fACLACETCPFlagsRst,
       "gs2328fACLACETCPFlagsPsh": gs2328fACLACETCPFlagsPsh,
       "gs2328fACLACETCPFlagsAck": gs2328fACLACETCPFlagsAck,
       "gs2328fACLACETCPFlagsUrg": gs2328fACLACETCPFlagsUrg,
       "gs2328fACLACERowStatus": gs2328fACLACERowStatus,
       "gs2328fACLACEClear": gs2328fACLACEClear,
       "gs2328fACLACEMoveACEID": gs2328fACLACEMoveACEID,
       "gs2328fACLACEMoveNextACEID": gs2328fACLACEMoveNextACEID,
       "gs2328fACLACEStatusTable": gs2328fACLACEStatusTable,
       "gs2328fACLACEStatusEntry": gs2328fACLACEStatusEntry,
       "gs2328fACLACEStatusIndex": gs2328fACLACEStatusIndex,
       "gs2328fACLACEStatusUser": gs2328fACLACEStatusUser,
       "gs2328fACLACEStatusID": gs2328fACLACEStatusID,
       "gs2328fACLACEStatusIngressPort": gs2328fACLACEStatusIngressPort,
       "gs2328fACLACEStatusFrameType": gs2328fACLACEStatusFrameType,
       "gs2328fACLACEStatusAction": gs2328fACLACEStatusAction,
       "gs2328fACLACEStatusRateLimiter": gs2328fACLACEStatusRateLimiter,
       "gs2328fACLACEStatusPortCopy": gs2328fACLACEStatusPortCopy,
       "gs2328fACLACEStatusMirror": gs2328fACLACEStatusMirror,
       "gs2328fACLACEStatusCPU": gs2328fACLACEStatusCPU,
       "gs2328fACLACEStatusCounter": gs2328fACLACEStatusCounter,
       "gs2328fACLACEStatusConflict": gs2328fACLACEStatusConflict,
       "gs2328fLoopProtection": gs2328fLoopProtection,
       "gs2328fLoopProtectionConfig": gs2328fLoopProtectionConfig,
       "gs2328fLoopProtectionGlobalEnable": gs2328fLoopProtectionGlobalEnable,
       "gs2328fLoopProtectionTranmisstionTime": gs2328fLoopProtectionTranmisstionTime,
       "gs2328fLoopProtectionShutdownTime": gs2328fLoopProtectionShutdownTime,
       "gs2328fLoopProtectionConfigurationTable": gs2328fLoopProtectionConfigurationTable,
       "gs2328fLoopProtectionConfigurationEntry": gs2328fLoopProtectionConfigurationEntry,
       "gs2328fLoopProtectionConfPort": gs2328fLoopProtectionConfPort,
       "gs2328fLoopProtectionConfEnable": gs2328fLoopProtectionConfEnable,
       "gs2328fLoopProtectionConfAction": gs2328fLoopProtectionConfAction,
       "gs2328fLoopProtectionConfTxmode": gs2328fLoopProtectionConfTxmode,
       "gs2328fLoopProtectionStatusTable": gs2328fLoopProtectionStatusTable,
       "gs2328fLoopProtectionStatusEntry": gs2328fLoopProtectionStatusEntry,
       "gs2328fLoopProtectionStatusPort": gs2328fLoopProtectionStatusPort,
       "gs2328fLoopProtectionStatusAction": gs2328fLoopProtectionStatusAction,
       "gs2328fLoopProtectionStatusTransmit": gs2328fLoopProtectionStatusTransmit,
       "gs2328fLoopProtectionStatusLoops": gs2328fLoopProtectionStatusLoops,
       "gs2328fLoopProtectionStatusStatus": gs2328fLoopProtectionStatusStatus,
       "gs2328fLoopProtectionStatusLoop": gs2328fLoopProtectionStatusLoop,
       "gs2328fLoopProtectionStatusTimeLastLoop": gs2328fLoopProtectionStatusTimeLastLoop,
       "gs2328fQos": gs2328fQos,
       "gs2328fQosPortClassification": gs2328fQosPortClassification,
       "gs2328fQosPortClassificationTable": gs2328fQosPortClassificationTable,
       "gs2328fQosPortClassificationEntry": gs2328fQosPortClassificationEntry,
       "gs2328fQosPortClassificationPort": gs2328fQosPortClassificationPort,
       "gs2328fQosPortClassificationQoSclass": gs2328fQosPortClassificationQoSclass,
       "gs2328fQosPortClassificationDPlevel": gs2328fQosPortClassificationDPlevel,
       "gs2328fQosPortClassificationPCP": gs2328fQosPortClassificationPCP,
       "gs2328fQosPortClassificationDEI": gs2328fQosPortClassificationDEI,
       "gs2328fQosPortClassificationTagClass": gs2328fQosPortClassificationTagClass,
       "gs2328fQosPortClassificationDSCPBased": gs2328fQosPortClassificationDSCPBased,
       "gs2328fQosPortClassificationAddressMode": gs2328fQosPortClassificationAddressMode,
       "gs2328fQoSIngressPortTagClassificationTable": gs2328fQoSIngressPortTagClassificationTable,
       "gs2328fQoSIngressPortTagClassificationEntry": gs2328fQoSIngressPortTagClassificationEntry,
       "gs2328fQoSIngressPortTagClassificationPort": gs2328fQoSIngressPortTagClassificationPort,
       "gs2328fQoSIngressPortTagPCP": gs2328fQoSIngressPortTagPCP,
       "gs2328fQoSIngressPortTagDEI": gs2328fQoSIngressPortTagDEI,
       "gs2328fQoSIngressPortTagQosClass": gs2328fQoSIngressPortTagQosClass,
       "gs2328fQoSIngressPortTagDPLevel": gs2328fQoSIngressPortTagDPLevel,
       "gs2328fQosPortPolicingTable": gs2328fQosPortPolicingTable,
       "gs2328fQosPortPolicingEntry": gs2328fQosPortPolicingEntry,
       "gs2328fQosPortPolicingPort": gs2328fQosPortPolicingPort,
       "gs2328fQosPortPolicingMode": gs2328fQosPortPolicingMode,
       "gs2328fQosPortPolicingRate": gs2328fQosPortPolicingRate,
       "gs2328fQosPortPolicingUnit": gs2328fQosPortPolicingUnit,
       "gs2328fQosPortPolicingFlowControl": gs2328fQosPortPolicingFlowControl,
       "gs2328fQosPortScheduler": gs2328fQosPortScheduler,
       "gs2328fQosPortSchedulerModeTable": gs2328fQosPortSchedulerModeTable,
       "gs2328fQosPortSchedulerModeEntry": gs2328fQosPortSchedulerModeEntry,
       "gs2328fQosSchedulerModePort": gs2328fQosSchedulerModePort,
       "gs2328fQosSchedulerMode": gs2328fQosSchedulerMode,
       "gs2328fQosSchedulerShaper": gs2328fQosSchedulerShaper,
       "gs2328fQosSchedulerShaperRate": gs2328fQosSchedulerShaperRate,
       "gs2328fQosPortSchedulerTable": gs2328fQosPortSchedulerTable,
       "gs2328fQosPortSchedulerEntry": gs2328fQosPortSchedulerEntry,
       "gs2328fQosSchedulerPort": gs2328fQosSchedulerPort,
       "gs2328fQosSchedulerPortQueue": gs2328fQosSchedulerPortQueue,
       "gs2328fQosSchedulerPortQueueShaper": gs2328fQosSchedulerPortQueueShaper,
       "gs2328fQosSchedulerPortQueueShaperRate": gs2328fQosSchedulerPortQueueShaperRate,
       "gs2328fQosSchedulerPortQueueShaperExcess": gs2328fQosSchedulerPortQueueShaperExcess,
       "gs2328fQosSchedulerPortQueueSchedulerWeight": gs2328fQosSchedulerPortQueueSchedulerWeight,
       "gs2328fQosSchedulerPortQueueSchedulerPercent": gs2328fQosSchedulerPortQueueSchedulerPercent,
       "gs2328fQosPortEgressTagRemarking": gs2328fQosPortEgressTagRemarking,
       "gs2328fQosPortEgressTagRemarkingTable": gs2328fQosPortEgressTagRemarkingTable,
       "gs2328fQosPortEgressTagRemarkingEntry": gs2328fQosPortEgressTagRemarkingEntry,
       "gs2328fQosEgressTagRemarkingPort": gs2328fQosEgressTagRemarkingPort,
       "gs2328fQosEgressTagRemarkingMode": gs2328fQosEgressTagRemarkingMode,
       "gs2328fQosPortEgressTagRemarkingDefTable": gs2328fQosPortEgressTagRemarkingDefTable,
       "gs2328fQosPortEgressTagRemarkingDefEntry": gs2328fQosPortEgressTagRemarkingDefEntry,
       "gs2328fQosEgressTagRemarkingDefPort": gs2328fQosEgressTagRemarkingDefPort,
       "gs2328fQosEgressTagRemarkingDefPCP": gs2328fQosEgressTagRemarkingDefPCP,
       "gs2328fQosEgressTagRemarkingDefDEI": gs2328fQosEgressTagRemarkingDefDEI,
       "gs2328fQosPortEgressTagRemarkingMapTable": gs2328fQosPortEgressTagRemarkingMapTable,
       "gs2328fQosPortEgressTagRemarkingMapEntry": gs2328fQosPortEgressTagRemarkingMapEntry,
       "gs2328fQosPortEgressTagRemarkingMapPort": gs2328fQosPortEgressTagRemarkingMapPort,
       "gs2328fQosTagRemarkingQoSClass": gs2328fQosTagRemarkingQoSClass,
       "gs2328fQosTagRemarkingDPLevel": gs2328fQosTagRemarkingDPLevel,
       "gs2328fQosTagRemarkingPCP": gs2328fQosTagRemarkingPCP,
       "gs2328fQosTagRemarkingDEI": gs2328fQosTagRemarkingDEI,
       "gs2328fQosPortDSCPTable": gs2328fQosPortDSCPTable,
       "gs2328fQosPortDSCPEntry": gs2328fQosPortDSCPEntry,
       "gs2328fQosPortDSCPPort": gs2328fQosPortDSCPPort,
       "gs2328fQosPortDSCPIngressTranslate": gs2328fQosPortDSCPIngressTranslate,
       "gs2328fQosPortDSCPIngressClassify": gs2328fQosPortDSCPIngressClassify,
       "gs2328fQosPortDSCPEgressRewrite": gs2328fQosPortDSCPEgressRewrite,
       "gs2328fQosDSCPTable": gs2328fQosDSCPTable,
       "gs2328fQosDSCPEntry": gs2328fQosDSCPEntry,
       "gs2328fQosDSCPList": gs2328fQosDSCPList,
       "gs2328fQosDSCP": gs2328fQosDSCP,
       "gs2328fQosDSCPTrust": gs2328fQosDSCPTrust,
       "gs2328fQosDSCPQosClass": gs2328fQosDSCPQosClass,
       "gs2328fQosDSCPDPL": gs2328fQosDSCPDPL,
       "gs2328fQosDSCPTranslationTable": gs2328fQosDSCPTranslationTable,
       "gs2328fQosDSCPTranslationEntry": gs2328fQosDSCPTranslationEntry,
       "gs2328fQosDSCPTranslationList": gs2328fQosDSCPTranslationList,
       "gs2328fQosDSCPTranslationDSCPBasedId": gs2328fQosDSCPTranslationDSCPBasedId,
       "gs2328fQosDSCPTranslationIngressTranslate": gs2328fQosDSCPTranslationIngressTranslate,
       "gs2328fQosDSCPTranslationIngressClassify": gs2328fQosDSCPTranslationIngressClassify,
       "gs2328fQosDSCPTranslationEgressRemapDP0": gs2328fQosDSCPTranslationEgressRemapDP0,
       "gs2328fQosDSCPTranslationEgressRemapDP1": gs2328fQosDSCPTranslationEgressRemapDP1,
       "gs2328fQosDSCPClassificationTable": gs2328fQosDSCPClassificationTable,
       "gs2328fQosDSCPClassificationEntry": gs2328fQosDSCPClassificationEntry,
       "gs2328fQosDSCPClassificationQoSClass": gs2328fQosDSCPClassificationQoSClass,
       "gs2328fQosDSCPClassificationDPL": gs2328fQosDSCPClassificationDPL,
       "gs2328fQosDSCPClassificationDSCP": gs2328fQosDSCPClassificationDSCP,
       "gs2328fQosControlList": gs2328fQosControlList,
       "gs2328fQosQceCreate": gs2328fQosQceCreate,
       "gs2328fQosQceTable": gs2328fQosQceTable,
       "gs2328fQosQceEntry": gs2328fQosQceEntry,
       "gs2328fQosQceIndex": gs2328fQosQceIndex,
       "gs2328fQosQceID": gs2328fQosQceID,
       "gs2328fQosQceNextID": gs2328fQosQceNextID,
       "gs2328fQosQcePortMembers": gs2328fQosQcePortMembers,
       "gs2328fQosQceTag": gs2328fQosQceTag,
       "gs2328fQosQceVID": gs2328fQosQceVID,
       "gs2328fQosPCP": gs2328fQosPCP,
       "gs2328fQosDEI": gs2328fQosDEI,
       "gs2328fQosSMAC": gs2328fQosSMAC,
       "gs2328fQosDMACType": gs2328fQosDMACType,
       "gs2328fQosFrameType": gs2328fQosFrameType,
       "gs2328fQosMacEtherType": gs2328fQosMacEtherType,
       "gs2328fQosLLCSSAPAddr": gs2328fQosLLCSSAPAddr,
       "gs2328fQosLLCDSAPAddr": gs2328fQosLLCDSAPAddr,
       "gs2328fQosLLCControl": gs2328fQosLLCControl,
       "gs2328fQosSNAPPID": gs2328fQosSNAPPID,
       "gs2328fQosIpv4Protocol": gs2328fQosIpv4Protocol,
       "gs2328fQosIpv4ProtocolValue": gs2328fQosIpv4ProtocolValue,
       "gs2328fQosIpv4ProtocolUDPSport": gs2328fQosIpv4ProtocolUDPSport,
       "gs2328fQosIpv4ProtocolUDPDport": gs2328fQosIpv4ProtocolUDPDport,
       "gs2328fQosIpv4ProtocolTCPSport": gs2328fQosIpv4ProtocolTCPSport,
       "gs2328fQosIpv4ProtocolTCPDport": gs2328fQosIpv4ProtocolTCPDport,
       "gs2328fQosIpv4Ip": gs2328fQosIpv4Ip,
       "gs2328fQosIpv4Mask": gs2328fQosIpv4Mask,
       "gs2328fQosIpv4IPFragment": gs2328fQosIpv4IPFragment,
       "gs2328fQosIpv4DSCP": gs2328fQosIpv4DSCP,
       "gs2328fQosIpv6Protocol": gs2328fQosIpv6Protocol,
       "gs2328fQosIpv6ProtocolValue": gs2328fQosIpv6ProtocolValue,
       "gs2328fQosIpv6ProtocolUDPSport": gs2328fQosIpv6ProtocolUDPSport,
       "gs2328fQosIpv6ProtocolUDPDport": gs2328fQosIpv6ProtocolUDPDport,
       "gs2328fQosIpv6ProtocolTCPSport": gs2328fQosIpv6ProtocolTCPSport,
       "gs2328fQosIpv6ProtocolTCPDport": gs2328fQosIpv6ProtocolTCPDport,
       "gs2328fQosIpv6Ip": gs2328fQosIpv6Ip,
       "gs2328fQosIpv6Mask": gs2328fQosIpv6Mask,
       "gs2328fQosIpv6DSCP": gs2328fQosIpv6DSCP,
       "gs2328fQosActionClass": gs2328fQosActionClass,
       "gs2328fQosActionDPL": gs2328fQosActionDPL,
       "gs2328fQosActionDSCP": gs2328fQosActionDSCP,
       "gs2328fQosQceRowStatus": gs2328fQosQceRowStatus,
       "gs2328fQosQceMoveID": gs2328fQosQceMoveID,
       "gs2328fQosQceMoveNextID": gs2328fQosQceMoveNextID,
       "gs2328fQosQCLStatusTable": gs2328fQosQCLStatusTable,
       "gs2328fQosQCLStatusEntry": gs2328fQosQCLStatusEntry,
       "gs2328fQosQCLStatusList": gs2328fQosQCLStatusList,
       "gs2328fQosQCLStatusUser": gs2328fQosQCLStatusUser,
       "gs2328fQosQCLStatusQCEId": gs2328fQosQCLStatusQCEId,
       "gs2328fQosQCLStatusFrameType": gs2328fQosQCLStatusFrameType,
       "gs2328fQosQCLStatusPortlist": gs2328fQosQCLStatusPortlist,
       "gs2328fQosQCLStatusActionClass": gs2328fQosQCLStatusActionClass,
       "gs2328fQosQCLStatusActionDPL": gs2328fQosQCLStatusActionDPL,
       "gs2328fQosQCLStatusActionDSCP": gs2328fQosQCLStatusActionDSCP,
       "gs2328fQosQCLStatusActionConflict": gs2328fQosQCLStatusActionConflict,
       "gs2328fQosStormControl": gs2328fQosStormControl,
       "gs2328fQoSStormControlUC": gs2328fQoSStormControlUC,
       "gs2328fQoSStormControlUCRate": gs2328fQoSStormControlUCRate,
       "gs2328fQoSStormControlMC": gs2328fQoSStormControlMC,
       "gs2328fQoSStormControlMCRate": gs2328fQoSStormControlMCRate,
       "gs2328fQoSStormControlBC": gs2328fQoSStormControlBC,
       "gs2328fQoSStormControlBCRate": gs2328fQoSStormControlBCRate,
       "gs2328fVlan": gs2328fVlan,
       "gs2328fVlanPorts": gs2328fVlanPorts,
       "gs2328fVlanPortsTPIDforCustomSport": gs2328fVlanPortsTPIDforCustomSport,
       "gs2328fVlanPortsTable": gs2328fVlanPortsTable,
       "gs2328fVlanPortsEntry": gs2328fVlanPortsEntry,
       "gs2328fVlanPortsPort": gs2328fVlanPortsPort,
       "gs2328fVlanPortsPVID": gs2328fVlanPortsPVID,
       "gs2328fVlanPortsFrameType": gs2328fVlanPortsFrameType,
       "gs2328fVlanPortsIngressFilter": gs2328fVlanPortsIngressFilter,
       "gs2328fVlanPortsEgressRule": gs2328fVlanPortsEgressRule,
       "gs2328fVlanPortsPortType": gs2328fVlanPortsPortType,
       "gs2328fVlanPrivateVLAN": gs2328fVlanPrivateVLAN,
       "gs2328fVlanPrivateVLANMembership": gs2328fVlanPrivateVLANMembership,
       "gs2328fVlanPrivateVLANMembershipCreate": gs2328fVlanPrivateVLANMembershipCreate,
       "gs2328fVlanPrivateVLANMembershipTable": gs2328fVlanPrivateVLANMembershipTable,
       "gs2328fVlanPrivateVLANMembershipEntry": gs2328fVlanPrivateVLANMembershipEntry,
       "gs2328fVlanPrivateVLANIndex": gs2328fVlanPrivateVLANIndex,
       "gs2328fVlanPrivateVLANID": gs2328fVlanPrivateVLANID,
       "gs2328fVlanPrivateVLANMemberships": gs2328fVlanPrivateVLANMemberships,
       "gs2328fVlanPrivateVLANRowStatus": gs2328fVlanPrivateVLANRowStatus,
       "gs2328fVlanPortIsolationTable": gs2328fVlanPortIsolationTable,
       "gs2328fVlanPortIsolationEntry": gs2328fVlanPortIsolationEntry,
       "gs2328fVlanPortIsolationPort": gs2328fVlanPortIsolationPort,
       "gs2328fVlanPortIsolation": gs2328fVlanPortIsolation,
       "gs2328fMACbasedVLAN": gs2328fMACbasedVLAN,
       "gs2328fMACbasedVLANConf": gs2328fMACbasedVLANConf,
       "gs2328fMACbasedVLANConfCreate": gs2328fMACbasedVLANConfCreate,
       "gs2328fMACbasedVLANConfTable": gs2328fMACbasedVLANConfTable,
       "gs2328fMACbasedVLANConfEntry": gs2328fMACbasedVLANConfEntry,
       "gs2328fMACbasedVLANIndex": gs2328fMACbasedVLANIndex,
       "gs2328fMACbasedVLANMACAddress": gs2328fMACbasedVLANMACAddress,
       "gs2328fMACbasedVLANID": gs2328fMACbasedVLANID,
       "gs2328fMACbasedMemberships": gs2328fMACbasedMemberships,
       "gs2328fMACbaseRowStatus": gs2328fMACbaseRowStatus,
       "gs2328fIGMPSnooping": gs2328fIGMPSnooping,
       "gs2328fIGMPSnoopingBasic": gs2328fIGMPSnoopingBasic,
       "gs2328fIGMPSnoopingEnable": gs2328fIGMPSnoopingEnable,
       "gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding": gs2328fIGMPSnoopingUnregisteredIPMCv4Flooding,
       "gs2328fIGMPSnoopingSSMIPRangeAddr": gs2328fIGMPSnoopingSSMIPRangeAddr,
       "gs2328fIGMPSnoopingSSMIPRangeValue": gs2328fIGMPSnoopingSSMIPRangeValue,
       "gs2328fIGMPSnoopingProxyEnabled": gs2328fIGMPSnoopingProxyEnabled,
       "gs2328fIGMPSnoopingPortRelatedTable": gs2328fIGMPSnoopingPortRelatedTable,
       "gs2328fIGMPSnoopingPortRelatedEntry": gs2328fIGMPSnoopingPortRelatedEntry,
       "gs2328fIGMPSnoopingRouterPort": gs2328fIGMPSnoopingRouterPort,
       "gs2328fIGMPSnoopingFastLeave": gs2328fIGMPSnoopingFastLeave,
       "gs2328fIGMPSnoopingThrottling": gs2328fIGMPSnoopingThrottling,
       "gs2328fIGMPSnoopingVLANTable": gs2328fIGMPSnoopingVLANTable,
       "gs2328fIGMPSnoopingVLANEntry": gs2328fIGMPSnoopingVLANEntry,
       "gs2328fIGMPSnoopingVLANID": gs2328fIGMPSnoopingVLANID,
       "gs2328fIGMPSnoopingVLANEnable": gs2328fIGMPSnoopingVLANEnable,
       "gs2328fIGMPSnoopingVLANIGMPQuerier": gs2328fIGMPSnoopingVLANIGMPQuerier,
       "gs2328fIGMPSnoopingVLANCompatibility": gs2328fIGMPSnoopingVLANCompatibility,
       "gs2328fIGMPSnoopingVLANRV": gs2328fIGMPSnoopingVLANRV,
       "gs2328fIGMPSnoopingVLANQI": gs2328fIGMPSnoopingVLANQI,
       "gs2328fIGMPSnoopingVLANQRI": gs2328fIGMPSnoopingVLANQRI,
       "gs2328fIGMPSnoopingVLANLLQI": gs2328fIGMPSnoopingVLANLLQI,
       "gs2328fIGMPSnoopingVLANURI": gs2328fIGMPSnoopingVLANURI,
       "gs2328fIGMPSnoopingPortGroupFiltering": gs2328fIGMPSnoopingPortGroupFiltering,
       "gs2328fIGMPSnoopingPortGroupFilteringCreate": gs2328fIGMPSnoopingPortGroupFilteringCreate,
       "gs2328fIGMPSnoopingPortGroupFilteringTable": gs2328fIGMPSnoopingPortGroupFilteringTable,
       "gs2328fIGMPSnoopingPortGroupFilteringEntry": gs2328fIGMPSnoopingPortGroupFilteringEntry,
       "gs2328fIGMPSnoopingPortGroupFilteringIndex": gs2328fIGMPSnoopingPortGroupFilteringIndex,
       "gs2328fIGMPSnoopingPortGroupFilteringPort": gs2328fIGMPSnoopingPortGroupFilteringPort,
       "gs2328fIGMPSnoopingPortGroupFilteringGroups": gs2328fIGMPSnoopingPortGroupFilteringGroups,
       "gs2328fIGMPSnoopingPortGroupFilteringRowStatus": gs2328fIGMPSnoopingPortGroupFilteringRowStatus,
       "gs2328fIGMPSnoopingStatus": gs2328fIGMPSnoopingStatus,
       "gs2328fIGMPSnoopingstatisticClear": gs2328fIGMPSnoopingstatisticClear,
       "gs2328fIGMPSnoopingstatisticTable": gs2328fIGMPSnoopingstatisticTable,
       "gs2328fIGMPSnoopingstatisticEntry": gs2328fIGMPSnoopingstatisticEntry,
       "gs2328fIGMPSnoopingstatisticVLANID": gs2328fIGMPSnoopingstatisticVLANID,
       "gs2328fIGMPSnoopingstatisticQuerierVersion": gs2328fIGMPSnoopingstatisticQuerierVersion,
       "gs2328fIGMPSnoopingstatisticHostVersion": gs2328fIGMPSnoopingstatisticHostVersion,
       "gs2328fIGMPSnoopingstatisticQuerierStatus": gs2328fIGMPSnoopingstatisticQuerierStatus,
       "gs2328fIGMPSnoopingstatisticQueriesTransmitted": gs2328fIGMPSnoopingstatisticQueriesTransmitted,
       "gs2328fIGMPSnoopingstatisticQueriesReceived": gs2328fIGMPSnoopingstatisticQueriesReceived,
       "gs2328fIGMPSnoopingstatisticV1ReportsReceived": gs2328fIGMPSnoopingstatisticV1ReportsReceived,
       "gs2328fIGMPSnoopingstatisticV2ReportsReceived": gs2328fIGMPSnoopingstatisticV2ReportsReceived,
       "gs2328fIGMPSnoopingstatisticV3ReportsReceived": gs2328fIGMPSnoopingstatisticV3ReportsReceived,
       "gs2328fIGMPSnoopingstatisticV2LeavesReceived": gs2328fIGMPSnoopingstatisticV2LeavesReceived,
       "gs2328fIGMPSnoopingRouterPortTable": gs2328fIGMPSnoopingRouterPortTable,
       "gs2328fIGMPSnoopingRouterPortEntry": gs2328fIGMPSnoopingRouterPortEntry,
       "gs2328fIGMPSnoopingRouterPortStatus": gs2328fIGMPSnoopingRouterPortStatus,
       "gs2328fIGMPSnoopingGroupsTable": gs2328fIGMPSnoopingGroupsTable,
       "gs2328fIGMPSnoopingGroupsEntry": gs2328fIGMPSnoopingGroupsEntry,
       "gs2328fIGMPSnoopingGroupsIndex": gs2328fIGMPSnoopingGroupsIndex,
       "gs2328fIGMPSnoopingGroupsVLANID": gs2328fIGMPSnoopingGroupsVLANID,
       "gs2328fIGMPSnoopingGroups": gs2328fIGMPSnoopingGroups,
       "gs2328fIGMPSnoopingGroupsMemberships": gs2328fIGMPSnoopingGroupsMemberships,
       "gs2328fIGMPSnoopingSSMTable": gs2328fIGMPSnoopingSSMTable,
       "gs2328fIGMPSnoopingSSMEntry": gs2328fIGMPSnoopingSSMEntry,
       "gs2328fIGMPSnoopingSSMIndex": gs2328fIGMPSnoopingSSMIndex,
       "gs2328fIGMPSnoopingSSMVLANID": gs2328fIGMPSnoopingSSMVLANID,
       "gs2328fIGMPSnoopingSSMGroup": gs2328fIGMPSnoopingSSMGroup,
       "gs2328fIGMPSnoopingSSMPort": gs2328fIGMPSnoopingSSMPort,
       "gs2328fIGMPSnoopingSSMMode": gs2328fIGMPSnoopingSSMMode,
       "gs2328fIGMPSnoopingSSMSourceAddress": gs2328fIGMPSnoopingSSMSourceAddress,
       "gs2328fIGMPSnoopingSSMType": gs2328fIGMPSnoopingSSMType,
       "gs2328fMLDSnooping": gs2328fMLDSnooping,
       "gs2328fMLDSnoopingBasic": gs2328fMLDSnoopingBasic,
       "gs2328fMLDSnoopingEnable": gs2328fMLDSnoopingEnable,
       "gs2328fMLDSnoopingUnregisteredIPMCv6Flooding": gs2328fMLDSnoopingUnregisteredIPMCv6Flooding,
       "gs2328fMLDSnoopingSSMIPRangeAddr": gs2328fMLDSnoopingSSMIPRangeAddr,
       "gs2328fMLDSnoopingSSMIPRangeValue": gs2328fMLDSnoopingSSMIPRangeValue,
       "gs2328fMLDSnoopingProxyEnabled": gs2328fMLDSnoopingProxyEnabled,
       "gs2328fMLDSnoopingPortRelatedTable": gs2328fMLDSnoopingPortRelatedTable,
       "gs2328fMLDSnoopingPortRelatedEntry": gs2328fMLDSnoopingPortRelatedEntry,
       "gs2328fMLDSnoopingRouterPort": gs2328fMLDSnoopingRouterPort,
       "gs2328fMLDSnoopingFastLeave": gs2328fMLDSnoopingFastLeave,
       "gs2328fMLDSnoopingThrottling": gs2328fMLDSnoopingThrottling,
       "gs2328fMLDSnoopingVLANTable": gs2328fMLDSnoopingVLANTable,
       "gs2328fMLDSnoopingVLANEntry": gs2328fMLDSnoopingVLANEntry,
       "gs2328fMLDSnoopingVLANID": gs2328fMLDSnoopingVLANID,
       "gs2328fMLDSnoopingVLANEnable": gs2328fMLDSnoopingVLANEnable,
       "gs2328fMLDSnoopingVLANIGMPQuerier": gs2328fMLDSnoopingVLANIGMPQuerier,
       "gs2328fMLDSnoopingVLANCompatibility": gs2328fMLDSnoopingVLANCompatibility,
       "gs2328fMLDSnoopingVLANRV": gs2328fMLDSnoopingVLANRV,
       "gs2328fMLDSnoopingVLANQI": gs2328fMLDSnoopingVLANQI,
       "gs2328fMLDSnoopingVLANQRI": gs2328fMLDSnoopingVLANQRI,
       "gs2328fMLDSnoopingVLANLLQI": gs2328fMLDSnoopingVLANLLQI,
       "gs2328fMLDSnoopingVLANURI": gs2328fMLDSnoopingVLANURI,
       "gs2328fMLDSnoopingPortGroupFiltering": gs2328fMLDSnoopingPortGroupFiltering,
       "gs2328fMLDSnoopingPortGroupFilteringCreate": gs2328fMLDSnoopingPortGroupFilteringCreate,
       "gs2328fMLDSnoopingPortGroupFilteringTable": gs2328fMLDSnoopingPortGroupFilteringTable,
       "gs2328fMLDSnoopingPortGroupFilteringEntry": gs2328fMLDSnoopingPortGroupFilteringEntry,
       "gs2328fMLDSnoopingPortGroupFilteringIndex": gs2328fMLDSnoopingPortGroupFilteringIndex,
       "gs2328fMLDSnoopingPortGroupFilteringPort": gs2328fMLDSnoopingPortGroupFilteringPort,
       "gs2328fMLDSnoopingPortGroupFilteringGroups": gs2328fMLDSnoopingPortGroupFilteringGroups,
       "gs2328fMLDSnoopingPortGroupFilteringRowStatus": gs2328fMLDSnoopingPortGroupFilteringRowStatus,
       "gs2328fMLDSnoopingStatus": gs2328fMLDSnoopingStatus,
       "gs2328fMLDSnoopingstatisticClear": gs2328fMLDSnoopingstatisticClear,
       "gs2328fMLDSnoopingstatisticTable": gs2328fMLDSnoopingstatisticTable,
       "gs2328fMLDSnoopingstatisticEntry": gs2328fMLDSnoopingstatisticEntry,
       "gs2328fMLDSnoopingstatisticVLANID": gs2328fMLDSnoopingstatisticVLANID,
       "gs2328fMLDSnoopingstatisticQuerierVersion": gs2328fMLDSnoopingstatisticQuerierVersion,
       "gs2328fMLDSnoopingstatisticHostVersion": gs2328fMLDSnoopingstatisticHostVersion,
       "gs2328fMLDSnoopingstatisticQuerierStatus": gs2328fMLDSnoopingstatisticQuerierStatus,
       "gs2328fMLDSnoopingstatisticQueriesTransmitted": gs2328fMLDSnoopingstatisticQueriesTransmitted,
       "gs2328fMLDSnoopingstatisticQueriesReceived": gs2328fMLDSnoopingstatisticQueriesReceived,
       "gs2328fMLDSnoopingstatisticV1ReportsReceived": gs2328fMLDSnoopingstatisticV1ReportsReceived,
       "gs2328fMLDSnoopingstatisticV2ReportsReceived": gs2328fMLDSnoopingstatisticV2ReportsReceived,
       "gs2328fMLDSnoopingstatisticV1LeavesReceived": gs2328fMLDSnoopingstatisticV1LeavesReceived,
       "gs2328fMLDSnoopingRouterPortTable": gs2328fMLDSnoopingRouterPortTable,
       "gs2328fMLDSnoopingRouterPortEntry": gs2328fMLDSnoopingRouterPortEntry,
       "gs2328fMLDSnoopingRouterPortStatus": gs2328fMLDSnoopingRouterPortStatus,
       "gs2328fMLDSnoopingGroupsTable": gs2328fMLDSnoopingGroupsTable,
       "gs2328fMLDSnoopingGroupsEntry": gs2328fMLDSnoopingGroupsEntry,
       "gs2328fMLDSnoopingGroupsIndex": gs2328fMLDSnoopingGroupsIndex,
       "gs2328fMLDSnoopingGroupsVLANID": gs2328fMLDSnoopingGroupsVLANID,
       "gs2328fMLDSnoopingGroups": gs2328fMLDSnoopingGroups,
       "gs2328fMLDSnoopingGroupsMemberships": gs2328fMLDSnoopingGroupsMemberships,
       "gs2328fMLDSnoopingSSMTable": gs2328fMLDSnoopingSSMTable,
       "gs2328fMLDSnoopingSSMEntry": gs2328fMLDSnoopingSSMEntry,
       "gs2328fMLDSnoopingSSMIndex": gs2328fMLDSnoopingSSMIndex,
       "gs2328fMLDSnoopingSSMVLANID": gs2328fMLDSnoopingSSMVLANID,
       "gs2328fMLDSnoopingSSMGroup": gs2328fMLDSnoopingSSMGroup,
       "gs2328fMLDSnoopingSSMPort": gs2328fMLDSnoopingSSMPort,
       "gs2328fMLDSnoopingSSMMode": gs2328fMLDSnoopingSSMMode,
       "gs2328fMLDSnoopingSSMSourceAddress": gs2328fMLDSnoopingSSMSourceAddress,
       "gs2328fMLDSnoopingSSMType": gs2328fMLDSnoopingSSMType,
       "gs2328fMVR": gs2328fMVR,
       "gs2328fMVRConfiguration": gs2328fMVRConfiguration,
       "gs2328fMVRMode": gs2328fMVRMode,
       "gs2328fMVRVLANId": gs2328fMVRVLANId,
       "gs2328fMVRPortConfigurationTable": gs2328fMVRPortConfigurationTable,
       "gs2328fMVRPortConfigurationEntry": gs2328fMVRPortConfigurationEntry,
       "gs2328fMVRPortConfigurationMode": gs2328fMVRPortConfigurationMode,
       "gs2328fMVRPortConfigurationType": gs2328fMVRPortConfigurationType,
       "gs2328fMVRPortConfigurationImmediateLeave": gs2328fMVRPortConfigurationImmediateLeave,
       "gs2328fMVRPortGroupFiltering": gs2328fMVRPortGroupFiltering,
       "gs2328fMVRPortGroupFilteringCreate": gs2328fMVRPortGroupFilteringCreate,
       "gs2328fMVRPortGroupFilteringTable": gs2328fMVRPortGroupFilteringTable,
       "gs2328fMVRPortGroupFilteringEntry": gs2328fMVRPortGroupFilteringEntry,
       "gs2328fMVRPortGroupFilteringIndex": gs2328fMVRPortGroupFilteringIndex,
       "gs2328fMVRPortGroupFilteringPort": gs2328fMVRPortGroupFilteringPort,
       "gs2328fMVRPortGroupFilteringStartGroups": gs2328fMVRPortGroupFilteringStartGroups,
       "gs2328fMVRPortGroupFilteringEndGroups": gs2328fMVRPortGroupFilteringEndGroups,
       "gs2328fMVRPortGroupFilteringRowStatus": gs2328fMVRPortGroupFilteringRowStatus,
       "gs2328fMVRGroupsTable": gs2328fMVRGroupsTable,
       "gs2328fMVRGroupsEntry": gs2328fMVRGroupsEntry,
       "gs2328fMVRGroupsIndex": gs2328fMVRGroupsIndex,
       "gs2328fMVRGroupsVLANID": gs2328fMVRGroupsVLANID,
       "gs2328fMVRGroups": gs2328fMVRGroups,
       "gs2328fMVRGroupsMemberships": gs2328fMVRGroupsMemberships,
       "gs2328fMVRStatus": gs2328fMVRStatus,
       "gs2328fMVRstatisticClear": gs2328fMVRstatisticClear,
       "gs2328fMVRstatisticVLANID": gs2328fMVRstatisticVLANID,
       "gs2328fMVRstatisticV1ReportsReceived": gs2328fMVRstatisticV1ReportsReceived,
       "gs2328fMVRstatisticV2ReportsReceived": gs2328fMVRstatisticV2ReportsReceived,
       "gs2328fMVRstatisticV3ReportsReceived": gs2328fMVRstatisticV3ReportsReceived,
       "gs2328fMVRstatisticV2LeavesReceived": gs2328fMVRstatisticV2LeavesReceived,
       "gs2328fLACP": gs2328fLACP,
       "gs2328fLACPConf": gs2328fLACPConf,
       "gs2328fLACPPortConfigurationTable": gs2328fLACPPortConfigurationTable,
       "gs2328fLACPPortConfigurationEntry": gs2328fLACPPortConfigurationEntry,
       "gs2328fLACPPortConfigurationPort": gs2328fLACPPortConfigurationPort,
       "gs2328fLACPPortConfigurationMode": gs2328fLACPPortConfigurationMode,
       "gs2328fLACPPortConfigurationKey": gs2328fLACPPortConfigurationKey,
       "gs2328fLACPPortConfigurationRole": gs2328fLACPPortConfigurationRole,
       "gs2328fLACPSystemStatusTable": gs2328fLACPSystemStatusTable,
       "gs2328fLACPSystemStatusEntry": gs2328fLACPSystemStatusEntry,
       "gs2328fLACPSystemStatusIndex": gs2328fLACPSystemStatusIndex,
       "gs2328fLACPSystemStatusAggrID": gs2328fLACPSystemStatusAggrID,
       "gs2328fLACPSystemStatusPartnerSystemID": gs2328fLACPSystemStatusPartnerSystemID,
       "gs2328fLACPSystemStatusPartnerKey": gs2328fLACPSystemStatusPartnerKey,
       "gs2328fLACPSystemStatusLastchanged": gs2328fLACPSystemStatusLastchanged,
       "gs2328fLACPSystemStatusLocalPorts": gs2328fLACPSystemStatusLocalPorts,
       "gs2328fLACPStatusTable": gs2328fLACPStatusTable,
       "gs2328fLACPStatusEntry": gs2328fLACPStatusEntry,
       "gs2328fLACPStatusPort": gs2328fLACPStatusPort,
       "gs2328fLACPStatusLACP": gs2328fLACPStatusLACP,
       "gs2328fLACPStatusKey": gs2328fLACPStatusKey,
       "gs2328fLACPStatusAggrID": gs2328fLACPStatusAggrID,
       "gs2328fLACPStatusPartnerSystemID": gs2328fLACPStatusPartnerSystemID,
       "gs2328fLACPStatusPartnerPort": gs2328fLACPStatusPartnerPort,
       "gs2328fLACPStatisticsTable": gs2328fLACPStatisticsTable,
       "gs2328fLACPStatisticsEntry": gs2328fLACPStatisticsEntry,
       "gs2328fLACPStatisticsPort": gs2328fLACPStatisticsPort,
       "gs2328fLACPReceived": gs2328fLACPReceived,
       "gs2328fLACPTransmitted": gs2328fLACPTransmitted,
       "gs2328fLACPDiscardedUnknown": gs2328fLACPDiscardedUnknown,
       "gs2328fLACPDiscardedIllegal": gs2328fLACPDiscardedIllegal,
       "gs2328fLACPStatisticsClear": gs2328fLACPStatisticsClear,
       "gs2328fSTP": gs2328fSTP,
       "gs2328fSTPBridgeBasicConf": gs2328fSTPBridgeBasicConf,
       "gs2328fSTPBridgeProtocolVersion": gs2328fSTPBridgeProtocolVersion,
       "gs2328fSTPBridgePriority": gs2328fSTPBridgePriority,
       "gs2328fSTPBridgeForwardDelay": gs2328fSTPBridgeForwardDelay,
       "gs2328fSTPBridgeMaxAge": gs2328fSTPBridgeMaxAge,
       "gs2328fSTPBridgeMaximumHopCount": gs2328fSTPBridgeMaximumHopCount,
       "gs2328fSTPBridgeTransmitHoldCount": gs2328fSTPBridgeTransmitHoldCount,
       "gs2328fSTPBridgeAdvancedConf": gs2328fSTPBridgeAdvancedConf,
       "gs2328fSTPBridgeEdgePortBPDUFiltering": gs2328fSTPBridgeEdgePortBPDUFiltering,
       "gs2328fSTPBridgeEdgePortBPDUGuard": gs2328fSTPBridgeEdgePortBPDUGuard,
       "gs2328fSTPBridgePortErrorRecoveryTimeout": gs2328fSTPBridgePortErrorRecoveryTimeout,
       "gs2328fSTPMSTIConf": gs2328fSTPMSTIConf,
       "gs2328fSTPMSTIConfigurationName": gs2328fSTPMSTIConfigurationName,
       "gs2328fSTPMSTIConfigurationRevision": gs2328fSTPMSTIConfigurationRevision,
       "gs2328fSTPMSTIMappingConf": gs2328fSTPMSTIMappingConf,
       "gs2328fSTPMSTI1VLANsMapped": gs2328fSTPMSTI1VLANsMapped,
       "gs2328fSTPMSTI2VLANsMapped": gs2328fSTPMSTI2VLANsMapped,
       "gs2328fSTPMSTI3VLANsMapped": gs2328fSTPMSTI3VLANsMapped,
       "gs2328fSTPMSTI4VLANsMapped": gs2328fSTPMSTI4VLANsMapped,
       "gs2328fSTPMSTI5VLANsMapped": gs2328fSTPMSTI5VLANsMapped,
       "gs2328fSTPMSTI6VLANsMapped": gs2328fSTPMSTI6VLANsMapped,
       "gs2328fSTPMSTI7VLANsMapped": gs2328fSTPMSTI7VLANsMapped,
       "gs2328fSTPMSTIPriority": gs2328fSTPMSTIPriority,
       "gs2328fSTPCISTPriority": gs2328fSTPCISTPriority,
       "gs2328fSTPMSTI1Priority": gs2328fSTPMSTI1Priority,
       "gs2328fSTPMSTI2Priority": gs2328fSTPMSTI2Priority,
       "gs2328fSTPMSTI3Priority": gs2328fSTPMSTI3Priority,
       "gs2328fSTPMSTI4Priority": gs2328fSTPMSTI4Priority,
       "gs2328fSTPMSTI5Priority": gs2328fSTPMSTI5Priority,
       "gs2328fSTPMSTI6Priority": gs2328fSTPMSTI6Priority,
       "gs2328fSTPMSTI7Priority": gs2328fSTPMSTI7Priority,
       "gs2328fSTPCISTPort": gs2328fSTPCISTPort,
       "gs2328fSTPCISTAggregatedPort": gs2328fSTPCISTAggregatedPort,
       "gs2328fSTPCISTAggregatedPortSTPEnabled": gs2328fSTPCISTAggregatedPortSTPEnabled,
       "gs2328fSTPCISTAggregatedPortPathCost": gs2328fSTPCISTAggregatedPortPathCost,
       "gs2328fSTPCISTAggregatedPortPriority": gs2328fSTPCISTAggregatedPortPriority,
       "gs2328fSTPCISTAggregatedPortAdminEdge": gs2328fSTPCISTAggregatedPortAdminEdge,
       "gs2328fSTPCISTAggregatedPortAutoEdge": gs2328fSTPCISTAggregatedPortAutoEdge,
       "gs2328fSTPCISTAggregatedPortRestrictedRole": gs2328fSTPCISTAggregatedPortRestrictedRole,
       "gs2328fSTPCISTAggregatedPortRestrictedTCN": gs2328fSTPCISTAggregatedPortRestrictedTCN,
       "gs2328fSTPCISTAggregatedPortBPDUGuard": gs2328fSTPCISTAggregatedPortBPDUGuard,
       "gs2328fSTPCISTAggregatedPortPointtoPoint": gs2328fSTPCISTAggregatedPortPointtoPoint,
       "gs2328fSTPCISTNormalPortTable": gs2328fSTPCISTNormalPortTable,
       "gs2328fSTPCISTNormalPortEntry": gs2328fSTPCISTNormalPortEntry,
       "gs2328fSTPCISTNormalPortConfPort": gs2328fSTPCISTNormalPortConfPort,
       "gs2328fSTPCISTNormalPortSTPEnabled": gs2328fSTPCISTNormalPortSTPEnabled,
       "gs2328fSTPCISTNormalPortPathCost": gs2328fSTPCISTNormalPortPathCost,
       "gs2328fSTPCISTNormalPortPriority": gs2328fSTPCISTNormalPortPriority,
       "gs2328fSTPCISTNormalPortAdminEdge": gs2328fSTPCISTNormalPortAdminEdge,
       "gs2328fSTPCISTNormalPortAutoEdge": gs2328fSTPCISTNormalPortAutoEdge,
       "gs2328fSTPCISTNormalPortRestrictedRole": gs2328fSTPCISTNormalPortRestrictedRole,
       "gs2328fSTPCISTNormalPortRestrictedTCN": gs2328fSTPCISTNormalPortRestrictedTCN,
       "gs2328fSTPCISTNormalPortBPDUGuard": gs2328fSTPCISTNormalPortBPDUGuard,
       "gs2328fSTPCISTNormalPortPointtoPoint": gs2328fSTPCISTNormalPortPointtoPoint,
       "gs2328fSTPMSTIPort": gs2328fSTPMSTIPort,
       "gs2328fSTPMSTI1Port": gs2328fSTPMSTI1Port,
       "gs2328fSTPMSTI1AggregatedPort": gs2328fSTPMSTI1AggregatedPort,
       "gs2328fSTPMSTI1AggregatedPortPathCost": gs2328fSTPMSTI1AggregatedPortPathCost,
       "gs2328fSTPMSTI1AggregatedPortPriority": gs2328fSTPMSTI1AggregatedPortPriority,
       "gs2328fSTPMSTI1NormalPortTable": gs2328fSTPMSTI1NormalPortTable,
       "gs2328fSTPMSTI1NormalPortEntry": gs2328fSTPMSTI1NormalPortEntry,
       "gs2328fSTPMSTI1NormalPortConfPort": gs2328fSTPMSTI1NormalPortConfPort,
       "gs2328fSTPMSTI1NormalPortPathCost": gs2328fSTPMSTI1NormalPortPathCost,
       "gs2328fSTPMSTI1NormalPortPriority": gs2328fSTPMSTI1NormalPortPriority,
       "gs2328fSTPMSTI2Port": gs2328fSTPMSTI2Port,
       "gs2328fSTPMSTI2AggregatedPort": gs2328fSTPMSTI2AggregatedPort,
       "gs2328fSTPMSTI2AggregatedPortPathCost": gs2328fSTPMSTI2AggregatedPortPathCost,
       "gs2328fSTPMSTI2AggregatedPortPriority": gs2328fSTPMSTI2AggregatedPortPriority,
       "gs2328fSTPMSTI2NormalPortTable": gs2328fSTPMSTI2NormalPortTable,
       "gs2328fSTPMSTI2NormalPortEntry": gs2328fSTPMSTI2NormalPortEntry,
       "gs2328fSTPMSTI2NormalPortConfPort": gs2328fSTPMSTI2NormalPortConfPort,
       "gs2328fSTPMSTI2NormalPortPathCost": gs2328fSTPMSTI2NormalPortPathCost,
       "gs2328fSTPMSTI2NormalPortPriority": gs2328fSTPMSTI2NormalPortPriority,
       "gs2328fSTPMSTI3Port": gs2328fSTPMSTI3Port,
       "gs2328fSTPMSTI3AggregatedPort": gs2328fSTPMSTI3AggregatedPort,
       "gs2328fSTPMSTI3AggregatedPortPathCost": gs2328fSTPMSTI3AggregatedPortPathCost,
       "gs2328fSTPMSTI3AggregatedPortPriority": gs2328fSTPMSTI3AggregatedPortPriority,
       "gs2328fSTPMSTI3NormalPortTable": gs2328fSTPMSTI3NormalPortTable,
       "gs2328fSTPMSTI3NormalPortEntry": gs2328fSTPMSTI3NormalPortEntry,
       "gs2328fSTPMSTI3NormalPortConfPort": gs2328fSTPMSTI3NormalPortConfPort,
       "gs2328fSTPMSTI3NormalPortPathCost": gs2328fSTPMSTI3NormalPortPathCost,
       "gs2328fSTPMSTI3NormalPortPriority": gs2328fSTPMSTI3NormalPortPriority,
       "gs2328fSTPMSTI4Port": gs2328fSTPMSTI4Port,
       "gs2328fSTPMSTI4AggregatedPort": gs2328fSTPMSTI4AggregatedPort,
       "gs2328fSTPMSTI4AggregatedPortPathCost": gs2328fSTPMSTI4AggregatedPortPathCost,
       "gs2328fSTPMSTI4AggregatedPortPriority": gs2328fSTPMSTI4AggregatedPortPriority,
       "gs2328fSTPMSTI4NormalPortTable": gs2328fSTPMSTI4NormalPortTable,
       "gs2328fSTPMSTI4NormalPortEntry": gs2328fSTPMSTI4NormalPortEntry,
       "gs2328fSTPMSTI4NormalPortConfPort": gs2328fSTPMSTI4NormalPortConfPort,
       "gs2328fSTPMSTI4NormalPortPathCost": gs2328fSTPMSTI4NormalPortPathCost,
       "gs2328fSTPMSTI4NormalPortPriority": gs2328fSTPMSTI4NormalPortPriority,
       "gs2328fSTPMSTI5Port": gs2328fSTPMSTI5Port,
       "gs2328fSTPMSTI5AggregatedPort": gs2328fSTPMSTI5AggregatedPort,
       "gs2328fSTPMSTI5AggregatedPortPathCost": gs2328fSTPMSTI5AggregatedPortPathCost,
       "gs2328fSTPMSTI5AggregatedPortPriority": gs2328fSTPMSTI5AggregatedPortPriority,
       "gs2328fSTPMSTI5NormalPortTable": gs2328fSTPMSTI5NormalPortTable,
       "gs2328fSTPMSTI5NormalPortEntry": gs2328fSTPMSTI5NormalPortEntry,
       "gs2328fSTPMSTI5NormalPortConfPort": gs2328fSTPMSTI5NormalPortConfPort,
       "gs2328fSTPMSTI5NormalPortPathCost": gs2328fSTPMSTI5NormalPortPathCost,
       "gs2328fSTPMSTI5NormalPortPriority": gs2328fSTPMSTI5NormalPortPriority,
       "gs2328fSTPMSTI6Port": gs2328fSTPMSTI6Port,
       "gs2328fSTPMSTI6AggregatedPort": gs2328fSTPMSTI6AggregatedPort,
       "gs2328fSTPMSTI6AggregatedPortPathCost": gs2328fSTPMSTI6AggregatedPortPathCost,
       "gs2328fSTPMSTI6AggregatedPortPriority": gs2328fSTPMSTI6AggregatedPortPriority,
       "gs2328fSTPMSTI6NormalPortTable": gs2328fSTPMSTI6NormalPortTable,
       "gs2328fSTPMSTI6NormalPortEntry": gs2328fSTPMSTI6NormalPortEntry,
       "gs2328fSTPMSTI6NormalPortConfPort": gs2328fSTPMSTI6NormalPortConfPort,
       "gs2328fSTPMSTI6NormalPortPathCost": gs2328fSTPMSTI6NormalPortPathCost,
       "gs2328fSTPMSTI6NormalPortPriority": gs2328fSTPMSTI6NormalPortPriority,
       "gs2328fSTPMSTI7Port": gs2328fSTPMSTI7Port,
       "gs2328fSTPMSTI7AggregatedPort": gs2328fSTPMSTI7AggregatedPort,
       "gs2328fSTPMSTI7AggregatedPortPathCost": gs2328fSTPMSTI7AggregatedPortPathCost,
       "gs2328fSTPMSTI7AggregatedPortPriority": gs2328fSTPMSTI7AggregatedPortPriority,
       "gs2328fSTPMSTI7NormalPortTable": gs2328fSTPMSTI7NormalPortTable,
       "gs2328fSTPMSTI7NormalPortEntry": gs2328fSTPMSTI7NormalPortEntry,
       "gs2328fSTPMSTI7NormalPortConfPort": gs2328fSTPMSTI7NormalPortConfPort,
       "gs2328fSTPMSTI7NormalPortPathCost": gs2328fSTPMSTI7NormalPortPathCost,
       "gs2328fSTPMSTI7NormalPortPriority": gs2328fSTPMSTI7NormalPortPriority,
       "gs2328fSTPBridgeStatus": gs2328fSTPBridgeStatus,
       "gs2328fCISTBridgeSTP": gs2328fCISTBridgeSTP,
       "gs2328fCISTBridgeSTPStatus": gs2328fCISTBridgeSTPStatus,
       "gs2328fCISTBridgeInstance": gs2328fCISTBridgeInstance,
       "gs2328fCISTBridgeID": gs2328fCISTBridgeID,
       "gs2328fCISTRootID": gs2328fCISTRootID,
       "gs2328fCISTRootPort": gs2328fCISTRootPort,
       "gs2328fCISTRootCost": gs2328fCISTRootCost,
       "gs2328fCISTRegionalRoot": gs2328fCISTRegionalRoot,
       "gs2328fCISTInternalRootCost": gs2328fCISTInternalRootCost,
       "gs2328fCISTTopologyFlag": gs2328fCISTTopologyFlag,
       "gs2328fCISTTopologyChangeCount": gs2328fCISTTopologyChangeCount,
       "gs2328fCISTTopologyChangeLast": gs2328fCISTTopologyChangeLast,
       "gs2328fCISTPortStateTable": gs2328fCISTPortStateTable,
       "gs2328fCISTPortStateEntry": gs2328fCISTPortStateEntry,
       "gs2328fCISTPortStateIndex": gs2328fCISTPortStateIndex,
       "gs2328fCISTPortStatePort": gs2328fCISTPortStatePort,
       "gs2328fCISTPortStatePortID": gs2328fCISTPortStatePortID,
       "gs2328fCISTPortStateRole": gs2328fCISTPortStateRole,
       "gs2328fCISTPortStateState": gs2328fCISTPortStateState,
       "gs2328fCISTPortStatePathCost": gs2328fCISTPortStatePathCost,
       "gs2328fCISTPortStateEdge": gs2328fCISTPortStateEdge,
       "gs2328fCISTPortStatePoint2Point": gs2328fCISTPortStatePoint2Point,
       "gs2328fCISTPortStateUptime": gs2328fCISTPortStateUptime,
       "gs2328fMSTI1BridgeSTP": gs2328fMSTI1BridgeSTP,
       "gs2328fMSTI1BridgeSTPStatus": gs2328fMSTI1BridgeSTPStatus,
       "gs2328fMSTI1BridgeInstance": gs2328fMSTI1BridgeInstance,
       "gs2328fMSTI1BridgeID": gs2328fMSTI1BridgeID,
       "gs2328fMSTI1RootID": gs2328fMSTI1RootID,
       "gs2328fMSTI1RootPort": gs2328fMSTI1RootPort,
       "gs2328fMSTI1RootCost": gs2328fMSTI1RootCost,
       "gs2328fMSTI1TopologyFlag": gs2328fMSTI1TopologyFlag,
       "gs2328fMSTI1TopologyChangeCount": gs2328fMSTI1TopologyChangeCount,
       "gs2328fMSTI1TopologyChangeLast": gs2328fMSTI1TopologyChangeLast,
       "gs2328fMSTI1PortStateTable": gs2328fMSTI1PortStateTable,
       "gs2328fMSTI1PortStateEntry": gs2328fMSTI1PortStateEntry,
       "gs2328fMSTI1PortStateIndex": gs2328fMSTI1PortStateIndex,
       "gs2328fMSTI1PortStatePort": gs2328fMSTI1PortStatePort,
       "gs2328fMSTI1PortStatePortID": gs2328fMSTI1PortStatePortID,
       "gs2328fMSTI1PortStateRole": gs2328fMSTI1PortStateRole,
       "gs2328fMSTI1PortStateState": gs2328fMSTI1PortStateState,
       "gs2328fMSTI1PortStatePathCost": gs2328fMSTI1PortStatePathCost,
       "gs2328fMSTI1PortStateEdge": gs2328fMSTI1PortStateEdge,
       "gs2328fMSTI1PortStatePoint2Point": gs2328fMSTI1PortStatePoint2Point,
       "gs2328fMSTI1PortStateUptime": gs2328fMSTI1PortStateUptime,
       "gs2328fMSTI2BridgeSTP": gs2328fMSTI2BridgeSTP,
       "gs2328fMSTI2BridgeSTPStatus": gs2328fMSTI2BridgeSTPStatus,
       "gs2328fMSTI2BridgeInstance": gs2328fMSTI2BridgeInstance,
       "gs2328fMSTI2BridgeID": gs2328fMSTI2BridgeID,
       "gs2328fMSTI2RootID": gs2328fMSTI2RootID,
       "gs2328fMSTI2RootPort": gs2328fMSTI2RootPort,
       "gs2328fMSTI2RootCost": gs2328fMSTI2RootCost,
       "gs2328fMSTI2TopologyFlag": gs2328fMSTI2TopologyFlag,
       "gs2328fMSTI2TopologyChangeCount": gs2328fMSTI2TopologyChangeCount,
       "gs2328fMSTI2TopologyChangeLast": gs2328fMSTI2TopologyChangeLast,
       "gs2328fMSTI2PortStateTable": gs2328fMSTI2PortStateTable,
       "gs2328fMSTI2PortStateEntry": gs2328fMSTI2PortStateEntry,
       "gs2328fMSTI2PortStateIndex": gs2328fMSTI2PortStateIndex,
       "gs2328fMSTI2PortStatePort": gs2328fMSTI2PortStatePort,
       "gs2328fMSTI2PortStatePortID": gs2328fMSTI2PortStatePortID,
       "gs2328fMSTI2PortStateRole": gs2328fMSTI2PortStateRole,
       "gs2328fMSTI2PortStateState": gs2328fMSTI2PortStateState,
       "gs2328fMSTI2PortStatePathCost": gs2328fMSTI2PortStatePathCost,
       "gs2328fMSTI2PortStateEdge": gs2328fMSTI2PortStateEdge,
       "gs2328fMSTI2PortStatePoint2Point": gs2328fMSTI2PortStatePoint2Point,
       "gs2328fMSTI2PortStateUptime": gs2328fMSTI2PortStateUptime,
       "gs2328fMSTI3BridgeSTP": gs2328fMSTI3BridgeSTP,
       "gs2328fMSTI3BridgeSTPStatus": gs2328fMSTI3BridgeSTPStatus,
       "gs2328fMSTI3BridgeInstance": gs2328fMSTI3BridgeInstance,
       "gs2328fMSTI3BridgeID": gs2328fMSTI3BridgeID,
       "gs2328fMSTI3RootID": gs2328fMSTI3RootID,
       "gs2328fMSTI3RootPort": gs2328fMSTI3RootPort,
       "gs2328fMSTI3RootCost": gs2328fMSTI3RootCost,
       "gs2328fMSTI3TopologyFlag": gs2328fMSTI3TopologyFlag,
       "gs2328fMSTI3TopologyChangeCount": gs2328fMSTI3TopologyChangeCount,
       "gs2328fMSTI3TopologyChangeLast": gs2328fMSTI3TopologyChangeLast,
       "gs2328fMSTI3PortStateTable": gs2328fMSTI3PortStateTable,
       "gs2328fMSTI3PortStateEntry": gs2328fMSTI3PortStateEntry,
       "gs2328fMSTI3PortStateIndex": gs2328fMSTI3PortStateIndex,
       "gs2328fMSTI3PortStatePort": gs2328fMSTI3PortStatePort,
       "gs2328fMSTI3PortStatePortID": gs2328fMSTI3PortStatePortID,
       "gs2328fMSTI3PortStateRole": gs2328fMSTI3PortStateRole,
       "gs2328fMSTI3PortStateState": gs2328fMSTI3PortStateState,
       "gs2328fMSTI3PortStatePathCost": gs2328fMSTI3PortStatePathCost,
       "gs2328fMSTI3PortStateEdge": gs2328fMSTI3PortStateEdge,
       "gs2328fMSTI3PortStatePoint2Point": gs2328fMSTI3PortStatePoint2Point,
       "gs2328fMSTI3PortStateUptime": gs2328fMSTI3PortStateUptime,
       "gs2328fMSTI4BridgeSTP": gs2328fMSTI4BridgeSTP,
       "gs2328fMSTI4BridgeSTPStatus": gs2328fMSTI4BridgeSTPStatus,
       "gs2328fMSTI4BridgeInstance": gs2328fMSTI4BridgeInstance,
       "gs2328fMSTI4BridgeID": gs2328fMSTI4BridgeID,
       "gs2328fMSTI4RootID": gs2328fMSTI4RootID,
       "gs2328fMSTI4RootPort": gs2328fMSTI4RootPort,
       "gs2328fMSTI4RootCost": gs2328fMSTI4RootCost,
       "gs2328fMSTI4TopologyFlag": gs2328fMSTI4TopologyFlag,
       "gs2328fMSTI4TopologyChangeCount": gs2328fMSTI4TopologyChangeCount,
       "gs2328fMSTI4TopologyChangeLast": gs2328fMSTI4TopologyChangeLast,
       "gs2328fMSTI4PortStateTable": gs2328fMSTI4PortStateTable,
       "gs2328fMSTI4PortStateEntry": gs2328fMSTI4PortStateEntry,
       "gs2328fMSTI4PortStateIndex": gs2328fMSTI4PortStateIndex,
       "gs2328fMSTI4PortStatePort": gs2328fMSTI4PortStatePort,
       "gs2328fMSTI4PortStatePortID": gs2328fMSTI4PortStatePortID,
       "gs2328fMSTI4PortStateRole": gs2328fMSTI4PortStateRole,
       "gs2328fMSTI4PortStateState": gs2328fMSTI4PortStateState,
       "gs2328fMSTI4PortStatePathCost": gs2328fMSTI4PortStatePathCost,
       "gs2328fMSTI4PortStateEdge": gs2328fMSTI4PortStateEdge,
       "gs2328fMSTI4PortStatePoint2Point": gs2328fMSTI4PortStatePoint2Point,
       "gs2328fMSTI4PortStateUptime": gs2328fMSTI4PortStateUptime,
       "gs2328fMSTI5BridgeSTP": gs2328fMSTI5BridgeSTP,
       "gs2328fMSTI5BridgeSTPStatus": gs2328fMSTI5BridgeSTPStatus,
       "gs2328fMSTI5BridgeInstance": gs2328fMSTI5BridgeInstance,
       "gs2328fMSTI5BridgeID": gs2328fMSTI5BridgeID,
       "gs2328fMSTI5RootID": gs2328fMSTI5RootID,
       "gs2328fMSTI5RootPort": gs2328fMSTI5RootPort,
       "gs2328fMSTI5RootCost": gs2328fMSTI5RootCost,
       "gs2328fMSTI5TopologyFlag": gs2328fMSTI5TopologyFlag,
       "gs2328fMSTI5TopologyChangeCount": gs2328fMSTI5TopologyChangeCount,
       "gs2328fMSTI5TopologyChangeLast": gs2328fMSTI5TopologyChangeLast,
       "gs2328fMSTI5PortStateTable": gs2328fMSTI5PortStateTable,
       "gs2328fMSTI5PortStateEntry": gs2328fMSTI5PortStateEntry,
       "gs2328fMSTI5PortStateIndex": gs2328fMSTI5PortStateIndex,
       "gs2328fMSTI5PortStatePort": gs2328fMSTI5PortStatePort,
       "gs2328fMSTI5PortStatePortID": gs2328fMSTI5PortStatePortID,
       "gs2328fMSTI5PortStateRole": gs2328fMSTI5PortStateRole,
       "gs2328fMSTI5PortStateState": gs2328fMSTI5PortStateState,
       "gs2328fMSTI5PortStatePathCost": gs2328fMSTI5PortStatePathCost,
       "gs2328fMSTI5PortStateEdge": gs2328fMSTI5PortStateEdge,
       "gs2328fMSTI5PortStatePoint2Point": gs2328fMSTI5PortStatePoint2Point,
       "gs2328fMSTI5PortStateUptime": gs2328fMSTI5PortStateUptime,
       "gs2328fMSTI6BridgeSTP": gs2328fMSTI6BridgeSTP,
       "gs2328fMSTI6BridgeSTPStatus": gs2328fMSTI6BridgeSTPStatus,
       "gs2328fMSTI6BridgeInstance": gs2328fMSTI6BridgeInstance,
       "gs2328fMSTI6BridgeID": gs2328fMSTI6BridgeID,
       "gs2328fMSTI6RootID": gs2328fMSTI6RootID,
       "gs2328fMSTI6RootPort": gs2328fMSTI6RootPort,
       "gs2328fMSTI6RootCost": gs2328fMSTI6RootCost,
       "gs2328fMSTI6TopologyFlag": gs2328fMSTI6TopologyFlag,
       "gs2328fMSTI6TopologyChangeCount": gs2328fMSTI6TopologyChangeCount,
       "gs2328fMSTI6TopologyChangeLast": gs2328fMSTI6TopologyChangeLast,
       "gs2328fMSTI6PortStateTable": gs2328fMSTI6PortStateTable,
       "gs2328fMSTI6PortStateEntry": gs2328fMSTI6PortStateEntry,
       "gs2328fMSTI6PortStateIndex": gs2328fMSTI6PortStateIndex,
       "gs2328fMSTI6PortStatePort": gs2328fMSTI6PortStatePort,
       "gs2328fMSTI6PortStatePortID": gs2328fMSTI6PortStatePortID,
       "gs2328fMSTI6PortStateRole": gs2328fMSTI6PortStateRole,
       "gs2328fMSTI6PortStateState": gs2328fMSTI6PortStateState,
       "gs2328fMSTI6PortStatePathCost": gs2328fMSTI6PortStatePathCost,
       "gs2328fMSTI6PortStateEdge": gs2328fMSTI6PortStateEdge,
       "gs2328fMSTI6PortStatePoint2Point": gs2328fMSTI6PortStatePoint2Point,
       "gs2328fMSTI6PortStateUptime": gs2328fMSTI6PortStateUptime,
       "gs2328fMSTI7BridgeSTP": gs2328fMSTI7BridgeSTP,
       "gs2328fMSTI7BridgeSTPStatus": gs2328fMSTI7BridgeSTPStatus,
       "gs2328fMSTI7BridgeInstance": gs2328fMSTI7BridgeInstance,
       "gs2328fMSTI7BridgeID": gs2328fMSTI7BridgeID,
       "gs2328fMSTI7RootID": gs2328fMSTI7RootID,
       "gs2328fMSTI7RootPort": gs2328fMSTI7RootPort,
       "gs2328fMSTI7RootCost": gs2328fMSTI7RootCost,
       "gs2328fMSTI7TopologyFlag": gs2328fMSTI7TopologyFlag,
       "gs2328fMSTI7TopologyChangeCount": gs2328fMSTI7TopologyChangeCount,
       "gs2328fMSTI7TopologyChangeLast": gs2328fMSTI7TopologyChangeLast,
       "gs2328fMSTI7PortStateTable": gs2328fMSTI7PortStateTable,
       "gs2328fMSTI7PortStateEntry": gs2328fMSTI7PortStateEntry,
       "gs2328fMSTI7PortStateIndex": gs2328fMSTI7PortStateIndex,
       "gs2328fMSTI7PortStatePort": gs2328fMSTI7PortStatePort,
       "gs2328fMSTI7PortStatePortID": gs2328fMSTI7PortStatePortID,
       "gs2328fMSTI7PortStateRole": gs2328fMSTI7PortStateRole,
       "gs2328fMSTI7PortStateState": gs2328fMSTI7PortStateState,
       "gs2328fMSTI7PortStatePathCost": gs2328fMSTI7PortStatePathCost,
       "gs2328fMSTI7PortStateEdge": gs2328fMSTI7PortStateEdge,
       "gs2328fMSTI7PortStatePoint2Point": gs2328fMSTI7PortStatePoint2Point,
       "gs2328fMSTI7PortStateUptime": gs2328fMSTI7PortStateUptime,
       "gs2328fSTPPortStatusTable": gs2328fSTPPortStatusTable,
       "gs2328fSTPPortStatusEntry": gs2328fSTPPortStatusEntry,
       "gs2328fSTPPortStatusPort": gs2328fSTPPortStatusPort,
       "gs2328fSTPPortStatusCISTRole": gs2328fSTPPortStatusCISTRole,
       "gs2328fSTPPortStatusCISTState": gs2328fSTPPortStatusCISTState,
       "gs2328fSTPPortStatusUptime": gs2328fSTPPortStatusUptime,
       "gs2328fSTPPortStatisticsTable": gs2328fSTPPortStatisticsTable,
       "gs2328fSTPPortStatisticsEntry": gs2328fSTPPortStatisticsEntry,
       "gs2328fSTPStatisticsIndex": gs2328fSTPStatisticsIndex,
       "gs2328fSTPStatisticsPort": gs2328fSTPStatisticsPort,
       "gs2328fSTPStatisticsTxMSTP": gs2328fSTPStatisticsTxMSTP,
       "gs2328fSTPStatisticsTxRSTP": gs2328fSTPStatisticsTxRSTP,
       "gs2328fSTPStatisticsTxSTP": gs2328fSTPStatisticsTxSTP,
       "gs2328fSTPStatisticsTxTCN": gs2328fSTPStatisticsTxTCN,
       "gs2328fSTPStatisticsRxMSTP": gs2328fSTPStatisticsRxMSTP,
       "gs2328fSTPStatisticsRxRSTP": gs2328fSTPStatisticsRxRSTP,
       "gs2328fSTPStatisticsRxSTP": gs2328fSTPStatisticsRxSTP,
       "gs2328fSTPStatisticsRxTCN": gs2328fSTPStatisticsRxTCN,
       "gs2328fSTPStatisticsDiscardedUnknown": gs2328fSTPStatisticsDiscardedUnknown,
       "gs2328fSTPStatisticsDiscardedIllegal": gs2328fSTPStatisticsDiscardedIllegal,
       "gs2328fFilteringDataBase": gs2328fFilteringDataBase,
       "gs2328fFilteringDataBaseConfig": gs2328fFilteringDataBaseConfig,
       "gs2328fFilteringDataBaseAgingTime": gs2328fFilteringDataBaseAgingTime,
       "gs2328fFilteringDataBaseConfigTable": gs2328fFilteringDataBaseConfigTable,
       "gs2328fFilteringDataBaseConfigEntry": gs2328fFilteringDataBaseConfigEntry,
       "gs2328fFilteringDataBaseConfigPort": gs2328fFilteringDataBaseConfigPort,
       "gs2328fFilteringDataBaseConfigLearning": gs2328fFilteringDataBaseConfigLearning,
       "gs2328fFilteringDataBaseStaticMAC": gs2328fFilteringDataBaseStaticMAC,
       "gs2328fFilteringDataBaseStaticMACCreate": gs2328fFilteringDataBaseStaticMACCreate,
       "gs2328fFilteringDataBaseStaticMACTable": gs2328fFilteringDataBaseStaticMACTable,
       "gs2328fFilteringDataBaseStaticMACEntry": gs2328fFilteringDataBaseStaticMACEntry,
       "gs2328fFilteringDataBaseStaticMACIndex": gs2328fFilteringDataBaseStaticMACIndex,
       "gs2328fFilteringDataBaseStaticMACVLANId": gs2328fFilteringDataBaseStaticMACVLANId,
       "gs2328fFilteringDataBaseStaticMACAddress": gs2328fFilteringDataBaseStaticMACAddress,
       "gs2328fFilteringDataBaseStaticMACPortMembers": gs2328fFilteringDataBaseStaticMACPortMembers,
       "gs2328fFilteringDataBaseStaticMACRowStatus": gs2328fFilteringDataBaseStaticMACRowStatus,
       "gs2328fFilteringDataBaseDynamicMACTable": gs2328fFilteringDataBaseDynamicMACTable,
       "gs2328fFilteringDataBaseDynamicMACEntry": gs2328fFilteringDataBaseDynamicMACEntry,
       "gs2328fFilteringDataBaseDynamicMACIndex": gs2328fFilteringDataBaseDynamicMACIndex,
       "gs2328fFilteringDataBaseDynamicMACType": gs2328fFilteringDataBaseDynamicMACType,
       "gs2328fFilteringDataBaseDynamicMACVLAN": gs2328fFilteringDataBaseDynamicMACVLAN,
       "gs2328fFilteringDataBaseDynamicMACAddress": gs2328fFilteringDataBaseDynamicMACAddress,
       "gs2328fFilteringDataBaseDynamicPortMembers": gs2328fFilteringDataBaseDynamicPortMembers,
       "gs2328fSFlowAgent": gs2328fSFlowAgent,
       "gs2328fSFlowAgentCollector": gs2328fSFlowAgentCollector,
       "gs2328fSFlowAgentReceiverMode": gs2328fSFlowAgentReceiverMode,
       "gs2328fLMC": gs2328fLMC,
       "gs2328fLMCOperating": gs2328fLMCOperating,
       "gs2328fLMCConfigViaDhcp": gs2328fLMCConfigViaDhcp,
       "gs2328fLMCDomain": gs2328fLMCDomain,
       "gs2328fLMChcpClientAutoRenew": gs2328fLMChcpClientAutoRenew,
       "gs2328fLMCZeroTouchSupport": gs2328fLMCZeroTouchSupport,
       "gs2328fLMCPairingTokenPresent": gs2328fLMCPairingTokenPresent,
       "gs2328fLMCClientStatus": gs2328fLMCClientStatus,
       "gs2328fLMCManagementStatus": gs2328fLMCManagementStatus,
       "gs2328fLMCControlStatus": gs2328fLMCControlStatus,
       "gs2328fLMCMonitoringStatus": gs2328fLMCMonitoringStatus,
       "gs2328fLMCConfigurationSource": gs2328fLMCConfigurationSource,
       "gs2328fLMCConfigModified": gs2328fLMCConfigModified,
       "gs2328fLMCDeviceID": gs2328fLMCDeviceID,
       "gs2328fLMCRoundTripTime": gs2328fLMCRoundTripTime,
       "gs2328fSecurity": gs2328fSecurity,
       "gs2328fIPSourceGuard": gs2328fIPSourceGuard,
       "gs2328fIPSourceGuardConf": gs2328fIPSourceGuardConf,
       "gs2328fIPSourceGuardMode": gs2328fIPSourceGuardMode,
       "gs2328fIPSourceGuardPortConfigTable": gs2328fIPSourceGuardPortConfigTable,
       "gs2328fIPSourceGuardPortConfigEntry": gs2328fIPSourceGuardPortConfigEntry,
       "gs2328fIPSourceGuardPortConfigPort": gs2328fIPSourceGuardPortConfigPort,
       "gs2328fIPSourceGuardPortConfigMode": gs2328fIPSourceGuardPortConfigMode,
       "gs2328fIPSourceGuardPortMaxDynamicClients": gs2328fIPSourceGuardPortMaxDynamicClients,
       "gs2328fIPSourceGuardStatic": gs2328fIPSourceGuardStatic,
       "gs2328fIPSourceGuardStaticCreate": gs2328fIPSourceGuardStaticCreate,
       "gs2328fIPSourceGuardStaticTable": gs2328fIPSourceGuardStaticTable,
       "gs2328fIPSourceGuardStaticEntry": gs2328fIPSourceGuardStaticEntry,
       "gs2328fIPSourceGuardStaticIndex": gs2328fIPSourceGuardStaticIndex,
       "gs2328fIPSourceGuardStaticPort": gs2328fIPSourceGuardStaticPort,
       "gs2328fIPSourceGuardStaticVLANId": gs2328fIPSourceGuardStaticVLANId,
       "gs2328fIPSourceGuardStaticIPAddress": gs2328fIPSourceGuardStaticIPAddress,
       "gs2328fIPSourceGuardStaticMACAddress": gs2328fIPSourceGuardStaticMACAddress,
       "gs2328fIPSourceGuardStaticRowStatus": gs2328fIPSourceGuardStaticRowStatus,
       "gs2328fIPSourceGuardDynamicTable": gs2328fIPSourceGuardDynamicTable,
       "gs2328fIPSourceGuardDynamicEntry": gs2328fIPSourceGuardDynamicEntry,
       "gs2328fIPSourceGuardDynamicIndex": gs2328fIPSourceGuardDynamicIndex,
       "gs2328fIPSourceGuardDynamicPort": gs2328fIPSourceGuardDynamicPort,
       "gs2328fIPSourceGuardDynamicVLANId": gs2328fIPSourceGuardDynamicVLANId,
       "gs2328fIPSourceGuardDynamicIPAddress": gs2328fIPSourceGuardDynamicIPAddress,
       "gs2328fIPSourceGuardDynamicMACAddress": gs2328fIPSourceGuardDynamicMACAddress,
       "gs2328fARPInspection": gs2328fARPInspection,
       "gs2328fARPInspectionConf": gs2328fARPInspectionConf,
       "gs2328fARPInspectionConfMode": gs2328fARPInspectionConfMode,
       "gs2328fARPInspectionConfTable": gs2328fARPInspectionConfTable,
       "gs2328fARPInspectionConfEntry": gs2328fARPInspectionConfEntry,
       "gs2328fARPInspectionConfPortIndex": gs2328fARPInspectionConfPortIndex,
       "gs2328fARPInspectionConfPortMode": gs2328fARPInspectionConfPortMode,
       "gs2328fARPInspectionStatic": gs2328fARPInspectionStatic,
       "gs2328fARPInspectionStaticCreate": gs2328fARPInspectionStaticCreate,
       "gs2328fARPInspectionStaticTable": gs2328fARPInspectionStaticTable,
       "gs2328fARPInspectionStaticEntry": gs2328fARPInspectionStaticEntry,
       "gs2328fARPInspectionStaticIndex": gs2328fARPInspectionStaticIndex,
       "gs2328fARPInspectionStaticPort": gs2328fARPInspectionStaticPort,
       "gs2328fARPInspectionStaticVLANId": gs2328fARPInspectionStaticVLANId,
       "gs2328fARPInspectionStaticIPAddress": gs2328fARPInspectionStaticIPAddress,
       "gs2328fARPInspectionStaticMACAddress": gs2328fARPInspectionStaticMACAddress,
       "gs2328fARPInspectionStaticRowStatus": gs2328fARPInspectionStaticRowStatus,
       "gs2328fARPInspectionDynamicTable": gs2328fARPInspectionDynamicTable,
       "gs2328fARPInspectionDynamicEntry": gs2328fARPInspectionDynamicEntry,
       "gs2328fARPInspectionDynamicIndex": gs2328fARPInspectionDynamicIndex,
       "gs2328fARPInspectionDynamicPort": gs2328fARPInspectionDynamicPort,
       "gs2328fARPInspectionDynamicVLANId": gs2328fARPInspectionDynamicVLANId,
       "gs2328fARPInspectionDynamicIPAddress": gs2328fARPInspectionDynamicIPAddress,
       "gs2328fARPInspectionDynamicMACAddress": gs2328fARPInspectionDynamicMACAddress,
       "gs2328fARPStaticGatewayCtrl": gs2328fARPStaticGatewayCtrl,
       "gs2328fARPStaticGatewayCtrlSystemConf": gs2328fARPStaticGatewayCtrlSystemConf,
       "gs2328fARPStaticGatewayCtrlMode": gs2328fARPStaticGatewayCtrlMode,
       "gs2328fARPStaticGatewayCtrlCreate": gs2328fARPStaticGatewayCtrlCreate,
       "gs2328fARPStaticGatewayCtrlTable": gs2328fARPStaticGatewayCtrlTable,
       "gs2328fARPStaticGatewayCtrlEntry": gs2328fARPStaticGatewayCtrlEntry,
       "gs2328fARPStaticGatewayCtrlIndex": gs2328fARPStaticGatewayCtrlIndex,
       "gs2328fARPStaticGatewayCtrlIPAddress": gs2328fARPStaticGatewayCtrlIPAddress,
       "gs2328fARPStaticGatewayCtrlMACAddress": gs2328fARPStaticGatewayCtrlMACAddress,
       "gs2328fARPStaticGatewayCtrlPort": gs2328fARPStaticGatewayCtrlPort,
       "gs2328fARPStaticGatewayCtrlAction": gs2328fARPStaticGatewayCtrlAction,
       "gs2328fARPStaticGatewayCtrlState": gs2328fARPStaticGatewayCtrlState,
       "gs2328fARPStaticGatewayCtrlReOpen": gs2328fARPStaticGatewayCtrlReOpen,
       "gs2328fARPStaticGatewayCtrlRowStatus": gs2328fARPStaticGatewayCtrlRowStatus,
       "gs2328fARPSpoofingPrevention": gs2328fARPSpoofingPrevention,
       "gs2328fARPSpoofingPreventionSystemConf": gs2328fARPSpoofingPreventionSystemConf,
       "gs2328fARPSpoofingPreventionMode": gs2328fARPSpoofingPreventionMode,
       "gs2328fARPSpoofingPreventionTable": gs2328fARPSpoofingPreventionTable,
       "gs2328fARPSpoofingPreventionEntry": gs2328fARPSpoofingPreventionEntry,
       "gs2328fARPSpoofingPreventionPort": gs2328fARPSpoofingPreventionPort,
       "gs2328fARPSpoofingPreventionPortMode": gs2328fARPSpoofingPreventionPortMode,
       "gs2328fARPSpoofingPreventionPortLimit": gs2328fARPSpoofingPreventionPortLimit,
       "gs2328fARPSpoofingPreventionPortAction": gs2328fARPSpoofingPreventionPortAction,
       "gs2328fARPSpoofingPreventionPortState": gs2328fARPSpoofingPreventionPortState,
       "gs2328fARPSpoofingPreventionPortReOpen": gs2328fARPSpoofingPreventionPortReOpen,
       "gs2328fARPIPDoSPrevention": gs2328fARPIPDoSPrevention,
       "gs2328fARPIPDoSPreventionTCPMode": gs2328fARPIPDoSPreventionTCPMode,
       "gs2328fARPIPDoSPreventionUDPMode": gs2328fARPIPDoSPreventionUDPMode,
       "gs2328fARPIPDoSPreventionICMPMode": gs2328fARPIPDoSPreventionICMPMode,
       "gs2328fARPIPDoSPreventionServerPort1": gs2328fARPIPDoSPreventionServerPort1,
       "gs2328fARPIPDoSPreventionServerPort2": gs2328fARPIPDoSPreventionServerPort2,
       "gs2328fARPIPDoSPreventionServerPort3": gs2328fARPIPDoSPreventionServerPort3,
       "gs2328fARPIPDoSPreventionServerPort4": gs2328fARPIPDoSPreventionServerPort4,
       "gs2328fDHCPSnooping": gs2328fDHCPSnooping,
       "gs2328fDHCPSnoopingConf": gs2328fDHCPSnoopingConf,
       "gs2328fDHCPSnoopingMode": gs2328fDHCPSnoopingMode,
       "gs2328fDHCPSnoopingPortModeConfigurationTable": gs2328fDHCPSnoopingPortModeConfigurationTable,
       "gs2328fDHCPSnoopingPortModeConfigurationEntry": gs2328fDHCPSnoopingPortModeConfigurationEntry,
       "gs2328fDHCPSnoopingPortModeConfigurationPort": gs2328fDHCPSnoopingPortModeConfigurationPort,
       "gs2328fDHCPSnoopingPortModeConfigurationMode": gs2328fDHCPSnoopingPortModeConfigurationMode,
       "gs2328fDHCPSnoopingStatisticsTable": gs2328fDHCPSnoopingStatisticsTable,
       "gs2328fDHCPSnoopingStatisticsEntry": gs2328fDHCPSnoopingStatisticsEntry,
       "gs2328fDHCPSnoopingStatisticsPort": gs2328fDHCPSnoopingStatisticsPort,
       "gs2328fDHCPSnoopingStatisticsClear": gs2328fDHCPSnoopingStatisticsClear,
       "gs2328fDHCPSnoopingRxDiscover": gs2328fDHCPSnoopingRxDiscover,
       "gs2328fDHCPSnoopingRxOffer": gs2328fDHCPSnoopingRxOffer,
       "gs2328fDHCPSnoopingRxRequest": gs2328fDHCPSnoopingRxRequest,
       "gs2328fDHCPSnoopingRxDecline": gs2328fDHCPSnoopingRxDecline,
       "gs2328fDHCPSnoopingRxACK": gs2328fDHCPSnoopingRxACK,
       "gs2328fDHCPSnoopingRxNAK": gs2328fDHCPSnoopingRxNAK,
       "gs2328fDHCPSnoopingRxRelease": gs2328fDHCPSnoopingRxRelease,
       "gs2328fDHCPSnoopingRxInform": gs2328fDHCPSnoopingRxInform,
       "gs2328fDHCPSnoopingRxLeaseQuery": gs2328fDHCPSnoopingRxLeaseQuery,
       "gs2328fDHCPSnoopingRxLeaseUnassigned": gs2328fDHCPSnoopingRxLeaseUnassigned,
       "gs2328fDHCPSnoopingRxLeaseUnknown": gs2328fDHCPSnoopingRxLeaseUnknown,
       "gs2328fDHCPSnoopingRxLeaseActive": gs2328fDHCPSnoopingRxLeaseActive,
       "gs2328fDHCPSnoopingTxDiscover": gs2328fDHCPSnoopingTxDiscover,
       "gs2328fDHCPSnoopingTxOffer": gs2328fDHCPSnoopingTxOffer,
       "gs2328fDHCPSnoopingTxRequest": gs2328fDHCPSnoopingTxRequest,
       "gs2328fDHCPSnoopingTxDecline": gs2328fDHCPSnoopingTxDecline,
       "gs2328fDHCPSnoopingTxACK": gs2328fDHCPSnoopingTxACK,
       "gs2328fDHCPSnoopingTxNAK": gs2328fDHCPSnoopingTxNAK,
       "gs2328fDHCPSnoopingTxRelease": gs2328fDHCPSnoopingTxRelease,
       "gs2328fDHCPSnoopingTxInform": gs2328fDHCPSnoopingTxInform,
       "gs2328fDHCPSnoopingTxLeaseQuery": gs2328fDHCPSnoopingTxLeaseQuery,
       "gs2328fDHCPSnoopingTxLeaseUnassigned": gs2328fDHCPSnoopingTxLeaseUnassigned,
       "gs2328fDHCPSnoopingTxLeaseUnknown": gs2328fDHCPSnoopingTxLeaseUnknown,
       "gs2328fDHCPSnoopingTxLeaseActive": gs2328fDHCPSnoopingTxLeaseActive,
       "gs2328fDHCPRelay": gs2328fDHCPRelay,
       "gs2328fDHCPRelayConfiguration": gs2328fDHCPRelayConfiguration,
       "gs2328fDHCPRelayMode": gs2328fDHCPRelayMode,
       "gs2328fDHCPRelayServer": gs2328fDHCPRelayServer,
       "gs2328fDHCPRelayInformationMode": gs2328fDHCPRelayInformationMode,
       "gs2328fDHCPRelayInformationPolicy": gs2328fDHCPRelayInformationPolicy,
       "gs2328fDHCPRelayConfigurationGateways": gs2328fDHCPRelayConfigurationGateways,
       "gs2328fDHCPRelayConfigurationGatewaysCreate": gs2328fDHCPRelayConfigurationGatewaysCreate,
       "gs2328fDHCPRelayConfigurationGatewaysTable": gs2328fDHCPRelayConfigurationGatewaysTable,
       "gs2328fDHCPRelayConfigurationGatewaysEntry": gs2328fDHCPRelayConfigurationGatewaysEntry,
       "gs2328fDHCPRelayConfigurationGatewaysIndex": gs2328fDHCPRelayConfigurationGatewaysIndex,
       "gs2328fDHCPRelayConfigurationGatewaysVLANId": gs2328fDHCPRelayConfigurationGatewaysVLANId,
       "gs2328fDHCPRelayConfigurationGatewaysIP": gs2328fDHCPRelayConfigurationGatewaysIP,
       "gs2328fDHCPRelayConfigurationGatewaysRowStatus": gs2328fDHCPRelayConfigurationGatewaysRowStatus,
       "gs2328fDHCPRelayInformationCustom": gs2328fDHCPRelayInformationCustom,
       "gs2328fDHCPRelayStatistics": gs2328fDHCPRelayStatistics,
       "gs2328fDHCPRelayServerStatistics": gs2328fDHCPRelayServerStatistics,
       "gs2328fServerStatTransmitToServer": gs2328fServerStatTransmitToServer,
       "gs2328fServerStatTransmitError": gs2328fServerStatTransmitError,
       "gs2328fServerStatReceiveFromServer": gs2328fServerStatReceiveFromServer,
       "gs2328fServerStatReceiveMissingAgentOption": gs2328fServerStatReceiveMissingAgentOption,
       "gs2328fServerStatReceiveMissingCircuitID": gs2328fServerStatReceiveMissingCircuitID,
       "gs2328fServerStatReceiveMissingRemoteID": gs2328fServerStatReceiveMissingRemoteID,
       "gs2328fServerStatReceiveBadCircuitID": gs2328fServerStatReceiveBadCircuitID,
       "gs2328fServerStatReceiveBadRemoteID": gs2328fServerStatReceiveBadRemoteID,
       "gs2328fDHCPRelayClientStatistics": gs2328fDHCPRelayClientStatistics,
       "gs2328fClientStatTransmitToClient": gs2328fClientStatTransmitToClient,
       "gs2328fClientStatTransmitError": gs2328fClientStatTransmitError,
       "gs2328fClientStatReceivefromClient": gs2328fClientStatReceivefromClient,
       "gs2328fClientStatReceiveAgentOption": gs2328fClientStatReceiveAgentOption,
       "gs2328fClientStatReplaceAgentOption": gs2328fClientStatReplaceAgentOption,
       "gs2328fClientStatKeepAgentOption": gs2328fClientStatKeepAgentOption,
       "gs2328fClientStatDropAgentOption": gs2328fClientStatDropAgentOption,
       "gs2328fPortSecurity": gs2328fPortSecurity,
       "gs2328fPortSecLimitCtrl": gs2328fPortSecLimitCtrl,
       "gs2328fPortSecLimitCtrlSystemConf": gs2328fPortSecLimitCtrlSystemConf,
       "gs2328fPortSecurityMode": gs2328fPortSecurityMode,
       "gs2328fPortSecurityAging": gs2328fPortSecurityAging,
       "gs2328fPortSecurityAgingPeriod": gs2328fPortSecurityAgingPeriod,
       "gs2328fPortSecLimitCtrlTable": gs2328fPortSecLimitCtrlTable,
       "gs2328fPortSecLimitCtrlEntry": gs2328fPortSecLimitCtrlEntry,
       "gs2328fPortSecLimitCtrlPort": gs2328fPortSecLimitCtrlPort,
       "gs2328fPortSecLimitCtrlPortMode": gs2328fPortSecLimitCtrlPortMode,
       "gs2328fPortSecLimitCtrlPortLimit": gs2328fPortSecLimitCtrlPortLimit,
       "gs2328fPortSecLimitCtrlPortAction": gs2328fPortSecLimitCtrlPortAction,
       "gs2328fPortSecLimitCtrlPortState": gs2328fPortSecLimitCtrlPortState,
       "gs2328fPortSecLimitCtrlPortReOpen": gs2328fPortSecLimitCtrlPortReOpen,
       "gs2328fPortSecSwitchStatusTable": gs2328fPortSecSwitchStatusTable,
       "gs2328fPortSecSwitchStatusEntry": gs2328fPortSecSwitchStatusEntry,
       "gs2328fPortSecSwitchStatusPort": gs2328fPortSecSwitchStatusPort,
       "gs2328fPortSecSwitchStatusUsers": gs2328fPortSecSwitchStatusUsers,
       "gs2328fPortSecSwitchStatusState": gs2328fPortSecSwitchStatusState,
       "gs2328fPortSecSwitchStatusMACCountCurrent": gs2328fPortSecSwitchStatusMACCountCurrent,
       "gs2328fPortSecSwitchStatusMACCountLimit": gs2328fPortSecSwitchStatusMACCountLimit,
       "gs2328fPortSecPortStatus": gs2328fPortSecPortStatus,
       "gs2328fPortSecPortStatusPort": gs2328fPortSecPortStatusPort,
       "gs2328fPortSecPortStatusTable": gs2328fPortSecPortStatusTable,
       "gs2328fPortSecPortStatusEntry": gs2328fPortSecPortStatusEntry,
       "gs2328fPortSecPortStatusIndex": gs2328fPortSecPortStatusIndex,
       "gs2328fPortSecPortStatusMACAddress": gs2328fPortSecPortStatusMACAddress,
       "gs2328fPortSecPortStatusVLANId": gs2328fPortSecPortStatusVLANId,
       "gs2328fPortSecPortStatusState": gs2328fPortSecPortStatusState,
       "gs2328fPortSecPortStatusTimeOfAddition": gs2328fPortSecPortStatusTimeOfAddition,
       "gs2328fPortSecPortStatusAgeAndHold": gs2328fPortSecPortStatusAgeAndHold,
       "gs2328fAccessManagement": gs2328fAccessManagement,
       "gs2328fAccessMgtConf": gs2328fAccessMgtConf,
       "gs2328fAccessMgtConfMode": gs2328fAccessMgtConfMode,
       "gs2328fAccessMgtConfCreate": gs2328fAccessMgtConfCreate,
       "gs2328fAccessMgtConfTable": gs2328fAccessMgtConfTable,
       "gs2328fAccessMgtConfEntry": gs2328fAccessMgtConfEntry,
       "gs2328fAccessMgtIndex": gs2328fAccessMgtIndex,
       "gs2328fAccessMgtAddresstype": gs2328fAccessMgtAddresstype,
       "gs2328fAccessMgtStartIpAddress": gs2328fAccessMgtStartIpAddress,
       "gs2328fAccessMgtEndIpAddress": gs2328fAccessMgtEndIpAddress,
       "gs2328fAccessMgtHttpHttps": gs2328fAccessMgtHttpHttps,
       "gs2328fAccessMgtSNMP": gs2328fAccessMgtSNMP,
       "gs2328fAccessMgtTelnetSSH": gs2328fAccessMgtTelnetSSH,
       "gs2328fAccessMgtRowStatus": gs2328fAccessMgtRowStatus,
       "gs2328fAccessMgtStatistics": gs2328fAccessMgtStatistics,
       "gs2328fHttpReceivedPkts": gs2328fHttpReceivedPkts,
       "gs2328fHttpAllowedPkts": gs2328fHttpAllowedPkts,
       "gs2328fHttpDiscardedPkts": gs2328fHttpDiscardedPkts,
       "gs2328fHttpsReceivedPkts": gs2328fHttpsReceivedPkts,
       "gs2328fHttpsAllowedPkts": gs2328fHttpsAllowedPkts,
       "gs2328fHttpsDiscardedPkts": gs2328fHttpsDiscardedPkts,
       "gs2328fSnmpReceivedPkts": gs2328fSnmpReceivedPkts,
       "gs2328fSnmpAllowedPkts": gs2328fSnmpAllowedPkts,
       "gs2328fSnmpDiscardedPkts": gs2328fSnmpDiscardedPkts,
       "gs2328fTelnetReceivedPkts": gs2328fTelnetReceivedPkts,
       "gs2328fTelnetAllowedPkts": gs2328fTelnetAllowedPkts,
       "gs2328fTelnetDiscardedPkts": gs2328fTelnetDiscardedPkts,
       "gs2328fSSHReceivedPkts": gs2328fSSHReceivedPkts,
       "gs2328fSSHAllowedPkts": gs2328fSSHAllowedPkts,
       "gs2328fSSHDiscardedPkts": gs2328fSSHDiscardedPkts,
       "gs2328fAccessMgtStatisticsClearAll": gs2328fAccessMgtStatisticsClearAll,
       "gs2328fSSH": gs2328fSSH,
       "gs2328fSSHMode": gs2328fSSHMode,
       "gs2328fHTTPS": gs2328fHTTPS,
       "gs2328fHTTPSMode": gs2328fHTTPSMode,
       "gs2328fHTTPSAutoRedirect": gs2328fHTTPSAutoRedirect,
       "gs2328fHTTPSCertRenew": gs2328fHTTPSCertRenew,
       "gs2328fHTTPSMinProtoVersion": gs2328fHTTPSMinProtoVersion,
       "gs2328fHTTPMode": gs2328fHTTPMode,
       "gs2328fAuthMethod": gs2328fAuthMethod,
       "gs2328fConsoleAuthMethod": gs2328fConsoleAuthMethod,
       "gs2328fConsoleFallback": gs2328fConsoleFallback,
       "gs2328fTelnetAuthMethod": gs2328fTelnetAuthMethod,
       "gs2328fTelnetFallback": gs2328fTelnetFallback,
       "gs2328fSshAuthMethod": gs2328fSshAuthMethod,
       "gs2328fSshFallback": gs2328fSshFallback,
       "gs2328fTftpAuthMethod": gs2328fTftpAuthMethod,
       "gs2328fTftpFallback": gs2328fTftpFallback,
       "gs2328fLoginFailures": gs2328fLoginFailures,
       "gs2328fLockMinutes": gs2328fLockMinutes,
       "gs2328fHttpAuthMethod": gs2328fHttpAuthMethod,
       "gs2328fHttpFallback": gs2328fHttpFallback,
       "gs2328fHttpsAuthMethod": gs2328fHttpsAuthMethod,
       "gs2328fHttpsFallback": gs2328fHttpsFallback,
       "gs2328fAAA": gs2328fAAA,
       "gs2328fAAACommonServer": gs2328fAAACommonServer,
       "gs2328fAAACommonServerTimeout": gs2328fAAACommonServerTimeout,
       "gs2328fAAACommonServerDeadTime": gs2328fAAACommonServerDeadTime,
       "gs2328fAAATACACSPlusAuthAndAccounting": gs2328fAAATACACSPlusAuthAndAccounting,
       "gs2328fAAAAuthorization": gs2328fAAAAuthorization,
       "gs2328fAAAFallbackToLocalAuthorization": gs2328fAAAFallbackToLocalAuthorization,
       "gs2328fAAAAccounting": gs2328fAAAAccounting,
       "gs2328fRADIUSAuthenticationServerTable": gs2328fRADIUSAuthenticationServerTable,
       "gs2328fRADIUSAuthenticationServerEntry": gs2328fRADIUSAuthenticationServerEntry,
       "gs2328fRADIUSAuthenticationServerIndex": gs2328fRADIUSAuthenticationServerIndex,
       "gs2328fRADIUSAuthenticationServerEnable": gs2328fRADIUSAuthenticationServerEnable,
       "gs2328fRADIUSAuthenticationServerIP": gs2328fRADIUSAuthenticationServerIP,
       "gs2328fRADIUSAuthenticationServerPort": gs2328fRADIUSAuthenticationServerPort,
       "gs2328fRADIUSAuthenticationServerSecret": gs2328fRADIUSAuthenticationServerSecret,
       "gs2328fRADIUSAccountingServerTable": gs2328fRADIUSAccountingServerTable,
       "gs2328fRADIUSAccountingServerEntry": gs2328fRADIUSAccountingServerEntry,
       "gs2328fRADIUSAccountingServerIndex": gs2328fRADIUSAccountingServerIndex,
       "gs2328fRADIUSAccountingServerEnable": gs2328fRADIUSAccountingServerEnable,
       "gs2328fRADIUSAccountingServerIP": gs2328fRADIUSAccountingServerIP,
       "gs2328fRADIUSAccountingServerPort": gs2328fRADIUSAccountingServerPort,
       "gs2328fRADIUSAccountingServerSecret": gs2328fRADIUSAccountingServerSecret,
       "gs2328fTACACSPlusAuthenticationServerTable": gs2328fTACACSPlusAuthenticationServerTable,
       "gs2328fTACACSPlusAuthenticationServerEntry": gs2328fTACACSPlusAuthenticationServerEntry,
       "gs2328fTACACSPlusAuthenticationServerIndex": gs2328fTACACSPlusAuthenticationServerIndex,
       "gs2328fTACACSPlusAuthenticationServerEnable": gs2328fTACACSPlusAuthenticationServerEnable,
       "gs2328fTACACSPlusAuthenticationServerIP": gs2328fTACACSPlusAuthenticationServerIP,
       "gs2328fTACACSPlusAuthenticationServerPort": gs2328fTACACSPlusAuthenticationServerPort,
       "gs2328fTACACSPlusAuthenticationServerSecret": gs2328fTACACSPlusAuthenticationServerSecret,
       "gs2328fRADIUSStatisticsTable": gs2328fRADIUSStatisticsTable,
       "gs2328fRADIUSStatisticsEntry": gs2328fRADIUSStatisticsEntry,
       "gs2328fRADIUSAuthStatisticsServerIndex": gs2328fRADIUSAuthStatisticsServerIndex,
       "gs2328fRADIUSAuthStatisticsRecPktAccessAccepts": gs2328fRADIUSAuthStatisticsRecPktAccessAccepts,
       "gs2328fRADIUSAuthStatisticsRecPktAccessRejects": gs2328fRADIUSAuthStatisticsRecPktAccessRejects,
       "gs2328fRADIUSAuthStatisticsRecPktAccessChallenges": gs2328fRADIUSAuthStatisticsRecPktAccessChallenges,
       "gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses": gs2328fRADIUSAuthStatisticsRecPktMalformedAccResponses,
       "gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators": gs2328fRADIUSAuthStatisticsRecPktBadAuthenticators,
       "gs2328fRADIUSAuthStatisticsRecPktUnknownTypes": gs2328fRADIUSAuthStatisticsRecPktUnknownTypes,
       "gs2328fRADIUSAuthStatisticsRecPktDropped": gs2328fRADIUSAuthStatisticsRecPktDropped,
       "gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests": gs2328fRADIUSAuthStatisticsTransmitPktAccessRequests,
       "gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions": gs2328fRADIUSAuthStatisticsTransmitPktAccessRetransmissions,
       "gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests": gs2328fRADIUSAuthStatisticsTransmitPktPendingRequests,
       "gs2328fRADIUSAuthStatisticsTransmitPktTimeouts": gs2328fRADIUSAuthStatisticsTransmitPktTimeouts,
       "gs2328fRADIUSAuthIP": gs2328fRADIUSAuthIP,
       "gs2328fRADIUSAuthState": gs2328fRADIUSAuthState,
       "gs2328fRADIUSAuthRoundTripTime": gs2328fRADIUSAuthRoundTripTime,
       "gs2328fRADIUSAccountingStatisticsRecPktResponses": gs2328fRADIUSAccountingStatisticsRecPktResponses,
       "gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses": gs2328fRADIUSAccountingStatisticsRecPktMalformedResponses,
       "gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators": gs2328fRADIUSAccountingStatisticsRecPktBadAuthenticators,
       "gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes": gs2328fRADIUSAccountingStatisticsRecPktUnknownTypes,
       "gs2328fRADIUSAccountingStatisticsRecPktDropped": gs2328fRADIUSAccountingStatisticsRecPktDropped,
       "gs2328fRADIUSAccountingStatisticsTransmitPktRequests": gs2328fRADIUSAccountingStatisticsTransmitPktRequests,
       "gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions": gs2328fRADIUSAccountingStatisticsTransmitPktRetransmissions,
       "gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests": gs2328fRADIUSAccountingStatisticsTransmitPktPendingRequests,
       "gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts": gs2328fRADIUSAccountingStatisticsTransmitPktTimeouts,
       "gs2328fRADIUSAccountingIP": gs2328fRADIUSAccountingIP,
       "gs2328fRADIUSAccountingState": gs2328fRADIUSAccountingState,
       "gs2328fRADIUSAccountingRoundTripTime": gs2328fRADIUSAccountingRoundTripTime,
       "gs2328fRADIUSStatisticsClear": gs2328fRADIUSStatisticsClear,
       "gs2328fNAS": gs2328fNAS,
       "gs2328fNASConfiguration": gs2328fNASConfiguration,
       "gs2328fNASConfigMode": gs2328fNASConfigMode,
       "gs2328fNASConfigReauthEnabled": gs2328fNASConfigReauthEnabled,
       "gs2328fNASConfigReauthPeriod": gs2328fNASConfigReauthPeriod,
       "gs2328fNASConfigEAPOLTimeout": gs2328fNASConfigEAPOLTimeout,
       "gs2328fNASConfigAgingPeriod": gs2328fNASConfigAgingPeriod,
       "gs2328fNASConfigHoldTime": gs2328fNASConfigHoldTime,
       "gs2328fNASConfigRADIUSAssignedQoSEnabled": gs2328fNASConfigRADIUSAssignedQoSEnabled,
       "gs2328fNASConfigRADIUSAssignedVLANEnabled": gs2328fNASConfigRADIUSAssignedVLANEnabled,
       "gs2328fNASConfigGuestVLANEnabled": gs2328fNASConfigGuestVLANEnabled,
       "gs2328fNASConfigGuestVLANID": gs2328fNASConfigGuestVLANID,
       "gs2328fNASConfigMaxReauthCount": gs2328fNASConfigMaxReauthCount,
       "gs2328fNASConfigAllowGuestVLANEAPOLSeen": gs2328fNASConfigAllowGuestVLANEAPOLSeen,
       "gs2328fNASPortConfigTable": gs2328fNASPortConfigTable,
       "gs2328fNASPortConfigEntry": gs2328fNASPortConfigEntry,
       "gs2328fNASPortConfigPort": gs2328fNASPortConfigPort,
       "gs2328fNASPortConfigAdminState": gs2328fNASPortConfigAdminState,
       "gs2328fNASPortConfigRADIUSAssignedQoSEnabled": gs2328fNASPortConfigRADIUSAssignedQoSEnabled,
       "gs2328fNASPortConfigRADIUSAssignedVLANEnabled": gs2328fNASPortConfigRADIUSAssignedVLANEnabled,
       "gs2328fNASPortConfigGuestVLANEnabled": gs2328fNASPortConfigGuestVLANEnabled,
       "gs2328fNASPortConfigPortState": gs2328fNASPortConfigPortState,
       "gs2328fNASPortConfigReauthenticate": gs2328fNASPortConfigReauthenticate,
       "gs2328fNASPortConfigReinitialize": gs2328fNASPortConfigReinitialize,
       "gs2328fNASPortConfigFallbackEnabled": gs2328fNASPortConfigFallbackEnabled,
       "gs2328fNASConfigMacBasedUseEAP": gs2328fNASConfigMacBasedUseEAP,
       "gs2328fNASSwitchStatusTable": gs2328fNASSwitchStatusTable,
       "gs2328fNASSwitchStatusEntry": gs2328fNASSwitchStatusEntry,
       "gs2328fNASSwitchStatusAdminState": gs2328fNASSwitchStatusAdminState,
       "gs2328fNASSwitchStatusPortState": gs2328fNASSwitchStatusPortState,
       "gs2328fNASSwitchStatusLastSource": gs2328fNASSwitchStatusLastSource,
       "gs2328fNASSwitchStatusLastID": gs2328fNASSwitchStatusLastID,
       "gs2328fNASSwitchStatusQoSClass": gs2328fNASSwitchStatusQoSClass,
       "gs2328fNASSwitchStatusPortVlanID": gs2328fNASSwitchStatusPortVlanID,
       "gs2328fNASPortStatus": gs2328fNASPortStatus,
       "gs2328fNASPortStatusCountersTable": gs2328fNASPortStatusCountersTable,
       "gs2328fNASPortStatusCountersEntry": gs2328fNASPortStatusCountersEntry,
       "gs2328fNASRxCountersEAPOLTotal": gs2328fNASRxCountersEAPOLTotal,
       "gs2328fNASRxCountersEAPOLResponseID": gs2328fNASRxCountersEAPOLResponseID,
       "gs2328fNASRxCountersEAPOLResponses": gs2328fNASRxCountersEAPOLResponses,
       "gs2328fNASRxCountersEAPOLStart": gs2328fNASRxCountersEAPOLStart,
       "gs2328fNASRxCountersEAPOLLogoff": gs2328fNASRxCountersEAPOLLogoff,
       "gs2328fNASRxCountersEAPOLInvalidType": gs2328fNASRxCountersEAPOLInvalidType,
       "gs2328fNASRxCountersEAPOLInvalidLength": gs2328fNASRxCountersEAPOLInvalidLength,
       "gs2328fNASTxCountersEAPOLTotal": gs2328fNASTxCountersEAPOLTotal,
       "gs2328fNASTxCountersEAPOLRequestID": gs2328fNASTxCountersEAPOLRequestID,
       "gs2328fNASTxCountersEAPOLRequests": gs2328fNASTxCountersEAPOLRequests,
       "gs2328fNASRxBackendServerCountersAccessChallenges": gs2328fNASRxBackendServerCountersAccessChallenges,
       "gs2328fNASRxBackendServerCountersOtherRequests": gs2328fNASRxBackendServerCountersOtherRequests,
       "gs2328fNASRxBackendServerCountersAuthSuccesses": gs2328fNASRxBackendServerCountersAuthSuccesses,
       "gs2328fNASRxBackendServerCountersAuthFailures": gs2328fNASRxBackendServerCountersAuthFailures,
       "gs2328fNASTxBackendServerCountersResponses": gs2328fNASTxBackendServerCountersResponses,
       "gs2328fNASLastSupplicantInfoMACAddress": gs2328fNASLastSupplicantInfoMACAddress,
       "gs2328fNASLastSupplicantInfoVlanID": gs2328fNASLastSupplicantInfoVlanID,
       "gs2328fNASLastSupplicantInfoVersion": gs2328fNASLastSupplicantInfoVersion,
       "gs2328fNASLastSupplicantInfoIdentity": gs2328fNASLastSupplicantInfoIdentity,
       "gs2328fNASCountersDoClear": gs2328fNASCountersDoClear,
       "gs2328fNASPortStatusClientsTable": gs2328fNASPortStatusClientsTable,
       "gs2328fNASPortStatusClientsEntry": gs2328fNASPortStatusClientsEntry,
       "gs2328fNASClientsIndex": gs2328fNASClientsIndex,
       "gs2328fNASClientsIdentity": gs2328fNASClientsIdentity,
       "gs2328fNASClientsMACAddress": gs2328fNASClientsMACAddress,
       "gs2328fNASClientsVlanID": gs2328fNASClientsVlanID,
       "gs2328fNASClientsState": gs2328fNASClientsState,
       "gs2328fNASClientsLastAuth": gs2328fNASClientsLastAuth,
       "gs2328fNASRxClientsEAPOLTotal": gs2328fNASRxClientsEAPOLTotal,
       "gs2328fNASRxClientsEAPOLResponseID": gs2328fNASRxClientsEAPOLResponseID,
       "gs2328fNASRxClientsEAPOLResponses": gs2328fNASRxClientsEAPOLResponses,
       "gs2328fNASRxClientsEAPOLStart": gs2328fNASRxClientsEAPOLStart,
       "gs2328fNASRxClientsEAPOLLogoff": gs2328fNASRxClientsEAPOLLogoff,
       "gs2328fNASRxClientsEAPOLInvalidType": gs2328fNASRxClientsEAPOLInvalidType,
       "gs2328fNASRxClientsEAPOLInvalidLength": gs2328fNASRxClientsEAPOLInvalidLength,
       "gs2328fNASTxClientsEAPOLTotal": gs2328fNASTxClientsEAPOLTotal,
       "gs2328fNASTxClientsEAPOLRequestID": gs2328fNASTxClientsEAPOLRequestID,
       "gs2328fNASTxClientsEAPOLRequests": gs2328fNASTxClientsEAPOLRequests,
       "gs2328fNASRxBackendServerClientsAccessChallenges": gs2328fNASRxBackendServerClientsAccessChallenges,
       "gs2328fNASRxBackendServerClientsOtherRequests": gs2328fNASRxBackendServerClientsOtherRequests,
       "gs2328fNASRxBackendServerClientsAuthSuccesses": gs2328fNASRxBackendServerClientsAuthSuccesses,
       "gs2328fNASRxBackendServerClientsAuthFailures": gs2328fNASRxBackendServerClientsAuthFailures,
       "gs2328fNASTxBackendServerClientsResponses": gs2328fNASTxBackendServerClientsResponses,
       "gs2328fMaintenance": gs2328fMaintenance,
       "gs2328fRestartDevice": gs2328fRestartDevice,
       "gs2328fFirmware": gs2328fFirmware,
       "gs2328fFirmwareIpAddress": gs2328fFirmwareIpAddress,
       "gs2328fFirmwareFileName": gs2328fFirmwareFileName,
       "gs2328fDoFirmwareUpgrade": gs2328fDoFirmwareUpgrade,
       "gs2328fSaveOrRestore": gs2328fSaveOrRestore,
       "gs2328fFactoryDefaults": gs2328fFactoryDefaults,
       "gs2328fSaveStart": gs2328fSaveStart,
       "gs2328fSaveUser": gs2328fSaveUser,
       "gs2328fRestoreUser": gs2328fRestoreUser,
       "gs2328fExportOrImport": gs2328fExportOrImport,
       "gs2328fExportIpAddress": gs2328fExportIpAddress,
       "gs2328fExportConfigName": gs2328fExportConfigName,
       "gs2328fDoExportConfig": gs2328fDoExportConfig,
       "gs2328fImportIpAddress": gs2328fImportIpAddress,
       "gs2328fImportConfigName": gs2328fImportConfigName,
       "gs2328fDoImportConfig": gs2328fDoImportConfig,
       "gs2328fDiagnostics": gs2328fDiagnostics,
       "gs2328fPingIpAddress": gs2328fPingIpAddress,
       "gs2328fPingSize": gs2328fPingSize,
       "gs2328fDoPingConfig": gs2328fDoPingConfig,
       "gs2328fPingResult": gs2328fPingResult,
       "gs2328fPing6IpAddress": gs2328fPing6IpAddress,
       "gs2328fPing6Size": gs2328fPing6Size,
       "gs2328fDoPing6Config": gs2328fDoPing6Config,
       "gs2328fPing6Result": gs2328fPing6Result,
       "gs2328fColdRestartDevice": gs2328fColdRestartDevice,
       "gs2328fTrap": gs2328fTrap,
       "gs2328fTrapEvent": gs2328fTrapEvent,
       "gs2328fEmergency": gs2328fEmergency,
       "gs2328fAlert": gs2328fAlert,
       "gs2328fCritical": gs2328fCritical,
       "gs2328fError": gs2328fError,
       "gs2328fWarning": gs2328fWarning,
       "gs2328fNotice": gs2328fNotice,
       "gs2328fInformational": gs2328fInformational,
       "gs2328fDebug": gs2328fDebug,
       "gs2328fTrapVariable": gs2328fTrapVariable,
       "gs2328fInformation": gs2328fInformation}
)
