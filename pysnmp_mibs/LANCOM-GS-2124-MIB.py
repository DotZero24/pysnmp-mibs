# SNMP MIB module (LANCOM-GS-2124-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-GS-2124-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:46 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lancomSystems = ModuleIdentity(
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
_LancomGS2124_ObjectIdentity = ObjectIdentity
lancomGS2124 = _LancomGS2124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124)
)
_Gs2124Produces_ObjectIdentity = ObjectIdentity
gs2124Produces = _Gs2124Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1)
)
_Gs2124System_ObjectIdentity = ObjectIdentity
gs2124System = _Gs2124System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1)
)
_Gs2124CommonSys_ObjectIdentity = ObjectIdentity
gs2124CommonSys = _Gs2124CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1)
)


class _Gs2124Reboot_Type(Integer32):
    """Custom type gs2124Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124Reboot_Type.__name__ = "Integer32"
_Gs2124Reboot_Object = MibScalar
gs2124Reboot = _Gs2124Reboot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 1),
    _Gs2124Reboot_Type()
)
gs2124Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Reboot.setStatus("current")
_Gs2124BiosVsersion_Type = DisplayString
_Gs2124BiosVsersion_Object = MibScalar
gs2124BiosVsersion = _Gs2124BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 2),
    _Gs2124BiosVsersion_Type()
)
gs2124BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124BiosVsersion.setStatus("current")
_Gs2124FirmwareVersion_Type = DisplayString
_Gs2124FirmwareVersion_Object = MibScalar
gs2124FirmwareVersion = _Gs2124FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 3),
    _Gs2124FirmwareVersion_Type()
)
gs2124FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124FirmwareVersion.setStatus("current")
_Gs2124HardwareVersion_Type = DisplayString
_Gs2124HardwareVersion_Object = MibScalar
gs2124HardwareVersion = _Gs2124HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 4),
    _Gs2124HardwareVersion_Type()
)
gs2124HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124HardwareVersion.setStatus("current")
_Gs2124MechanicalVersion_Type = DisplayString
_Gs2124MechanicalVersion_Object = MibScalar
gs2124MechanicalVersion = _Gs2124MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 5),
    _Gs2124MechanicalVersion_Type()
)
gs2124MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MechanicalVersion.setStatus("current")
_Gs2124SerialNumber_Type = DisplayString
_Gs2124SerialNumber_Object = MibScalar
gs2124SerialNumber = _Gs2124SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 6),
    _Gs2124SerialNumber_Type()
)
gs2124SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SerialNumber.setStatus("current")
_Gs2124HostMacAddress_Type = DisplayString
_Gs2124HostMacAddress_Object = MibScalar
gs2124HostMacAddress = _Gs2124HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 7),
    _Gs2124HostMacAddress_Type()
)
gs2124HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124HostMacAddress.setStatus("current")
_Gs2124DevicePort_Type = DisplayString
_Gs2124DevicePort_Object = MibScalar
gs2124DevicePort = _Gs2124DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 8),
    _Gs2124DevicePort_Type()
)
gs2124DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DevicePort.setStatus("current")
_Gs2124RamSize_Type = DisplayString
_Gs2124RamSize_Object = MibScalar
gs2124RamSize = _Gs2124RamSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 9),
    _Gs2124RamSize_Type()
)
gs2124RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124RamSize.setStatus("current")
_Gs2124FlashSize_Type = DisplayString
_Gs2124FlashSize_Object = MibScalar
gs2124FlashSize = _Gs2124FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 10),
    _Gs2124FlashSize_Type()
)
gs2124FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124FlashSize.setStatus("current")
_Gs2124DeviceName_Type = DisplayString
_Gs2124DeviceName_Object = MibScalar
gs2124DeviceName = _Gs2124DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 11),
    _Gs2124DeviceName_Type()
)
gs2124DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DeviceName.setStatus("current")
_Gs2124SystemDescription_Type = DisplayString
_Gs2124SystemDescription_Object = MibScalar
gs2124SystemDescription = _Gs2124SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 12),
    _Gs2124SystemDescription_Type()
)
gs2124SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SystemDescription.setStatus("current")
_Gs2124CpuLoad_Type = DisplayString
_Gs2124CpuLoad_Object = MibScalar
gs2124CpuLoad = _Gs2124CpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 1, 13),
    _Gs2124CpuLoad_Type()
)
gs2124CpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124CpuLoad.setStatus("current")
_Gs2124IP_ObjectIdentity = ObjectIdentity
gs2124IP = _Gs2124IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2)
)


class _Gs2124DhcpSetting_Type(Integer32):
    """Custom type gs2124DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DhcpSetting_Type.__name__ = "Integer32"
_Gs2124DhcpSetting_Object = MibScalar
gs2124DhcpSetting = _Gs2124DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 1),
    _Gs2124DhcpSetting_Type()
)
gs2124DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSetting.setStatus("current")
_Gs2124IPAddress_Type = IpAddress
_Gs2124IPAddress_Object = MibScalar
gs2124IPAddress = _Gs2124IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 2),
    _Gs2124IPAddress_Type()
)
gs2124IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IPAddress.setStatus("current")
_Gs2124NetMask_Type = IpAddress
_Gs2124NetMask_Object = MibScalar
gs2124NetMask = _Gs2124NetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 3),
    _Gs2124NetMask_Type()
)
gs2124NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124NetMask.setStatus("current")
_Gs2124DefaultGateway_Type = IpAddress
_Gs2124DefaultGateway_Object = MibScalar
gs2124DefaultGateway = _Gs2124DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 4),
    _Gs2124DefaultGateway_Type()
)
gs2124DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DefaultGateway.setStatus("current")


class _Gs2124DnsConf_Type(Integer32):
    """Custom type gs2124DnsConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DnsConf_Type.__name__ = "Integer32"
_Gs2124DnsConf_Object = MibScalar
gs2124DnsConf = _Gs2124DnsConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 5),
    _Gs2124DnsConf_Type()
)
gs2124DnsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DnsConf.setStatus("current")


class _Gs2124DnsState_Type(Integer32):
    """Custom type gs2124DnsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DnsState_Type.__name__ = "Integer32"
_Gs2124DnsState_Object = MibScalar
gs2124DnsState = _Gs2124DnsState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 6),
    _Gs2124DnsState_Type()
)
gs2124DnsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DnsState.setStatus("current")
_Gs2124DnsServer_Type = IpAddress
_Gs2124DnsServer_Object = MibScalar
gs2124DnsServer = _Gs2124DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 2, 7),
    _Gs2124DnsServer_Type()
)
gs2124DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DnsServer.setStatus("current")
_Gs2124Time_ObjectIdentity = ObjectIdentity
gs2124Time = _Gs2124Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3)
)
_Gs2124SystemCurrentTime_Type = DisplayString
_Gs2124SystemCurrentTime_Object = MibScalar
gs2124SystemCurrentTime = _Gs2124SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 1),
    _Gs2124SystemCurrentTime_Type()
)
gs2124SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SystemCurrentTime.setStatus("current")
_Gs2124ManualTimeSetting_Type = DisplayString
_Gs2124ManualTimeSetting_Object = MibScalar
gs2124ManualTimeSetting = _Gs2124ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 2),
    _Gs2124ManualTimeSetting_Type()
)
gs2124ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManualTimeSetting.setStatus("current")
_Gs2124NTPServer_Type = DisplayString
_Gs2124NTPServer_Object = MibScalar
gs2124NTPServer = _Gs2124NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 3),
    _Gs2124NTPServer_Type()
)
gs2124NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124NTPServer.setStatus("current")


class _Gs2124NTPTimeZone_Type(Integer32):
    """Custom type gs2124NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Gs2124NTPTimeZone_Type.__name__ = "Integer32"
_Gs2124NTPTimeZone_Object = MibScalar
gs2124NTPTimeZone = _Gs2124NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 4),
    _Gs2124NTPTimeZone_Type()
)
gs2124NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124NTPTimeZone.setStatus("current")


class _Gs2124NTPTimeSync_Type(Integer32):
    """Custom type gs2124NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124NTPTimeSync_Type.__name__ = "Integer32"
_Gs2124NTPTimeSync_Object = MibScalar
gs2124NTPTimeSync = _Gs2124NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 5),
    _Gs2124NTPTimeSync_Type()
)
gs2124NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124NTPTimeSync.setStatus("current")


class _Gs2124DaylightSavingTime_Type(Integer32):
    """Custom type gs2124DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Gs2124DaylightSavingTime_Type.__name__ = "Integer32"
_Gs2124DaylightSavingTime_Object = MibScalar
gs2124DaylightSavingTime = _Gs2124DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 6),
    _Gs2124DaylightSavingTime_Type()
)
gs2124DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DaylightSavingTime.setStatus("current")
_Gs2124DaylightStartTime_Type = DisplayString
_Gs2124DaylightStartTime_Object = MibScalar
gs2124DaylightStartTime = _Gs2124DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 7),
    _Gs2124DaylightStartTime_Type()
)
gs2124DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DaylightStartTime.setStatus("current")
_Gs2124DaylightEndTime_Type = DisplayString
_Gs2124DaylightEndTime_Object = MibScalar
gs2124DaylightEndTime = _Gs2124DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 3, 8),
    _Gs2124DaylightEndTime_Type()
)
gs2124DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DaylightEndTime.setStatus("current")
_Gs2124Account_ObjectIdentity = ObjectIdentity
gs2124Account = _Gs2124Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4)
)


class _Gs2124AccountNumber_Type(Integer32):
    """Custom type gs2124AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2124AccountNumber_Type.__name__ = "Integer32"
_Gs2124AccountNumber_Object = MibScalar
gs2124AccountNumber = _Gs2124AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 1),
    _Gs2124AccountNumber_Type()
)
gs2124AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AccountNumber.setStatus("current")
_Gs2124AccountTable_Object = MibTable
gs2124AccountTable = _Gs2124AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    gs2124AccountTable.setStatus("current")
_Gs2124AccountEntry_Object = MibTableRow
gs2124AccountEntry = _Gs2124AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 2, 1)
)
gs2124AccountEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124AccountIndex"),
)
if mibBuilder.loadTexts:
    gs2124AccountEntry.setStatus("current")


class _Gs2124AccountIndex_Type(Integer32):
    """Custom type gs2124AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2124AccountIndex_Type.__name__ = "Integer32"
_Gs2124AccountIndex_Object = MibTableColumn
gs2124AccountIndex = _Gs2124AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 2, 1, 1),
    _Gs2124AccountIndex_Type()
)
gs2124AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AccountIndex.setStatus("current")
_Gs2124AccountAuthorization_Type = DisplayString
_Gs2124AccountAuthorization_Object = MibTableColumn
gs2124AccountAuthorization = _Gs2124AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 2, 1, 2),
    _Gs2124AccountAuthorization_Type()
)
gs2124AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AccountAuthorization.setStatus("current")
_Gs2124AccountName_Type = DisplayString
_Gs2124AccountName_Object = MibTableColumn
gs2124AccountName = _Gs2124AccountName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 2, 1, 3),
    _Gs2124AccountName_Type()
)
gs2124AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AccountName.setStatus("current")
_Gs2124AccountPassword_Type = DisplayString
_Gs2124AccountPassword_Object = MibTableColumn
gs2124AccountPassword = _Gs2124AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 2, 1, 4),
    _Gs2124AccountPassword_Type()
)
gs2124AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AccountPassword.setStatus("current")


class _Gs2124AccountAddAuthorization_Type(Integer32):
    """Custom type gs2124AccountAddAuthorization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AccountAddAuthorization_Type.__name__ = "Integer32"
_Gs2124AccountAddAuthorization_Object = MibScalar
gs2124AccountAddAuthorization = _Gs2124AccountAddAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 3),
    _Gs2124AccountAddAuthorization_Type()
)
gs2124AccountAddAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AccountAddAuthorization.setStatus("current")
_Gs2124AccountAddName_Type = DisplayString
_Gs2124AccountAddName_Object = MibScalar
gs2124AccountAddName = _Gs2124AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 4),
    _Gs2124AccountAddName_Type()
)
gs2124AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AccountAddName.setStatus("current")
_Gs2124AccountAddPassword_Type = DisplayString
_Gs2124AccountAddPassword_Object = MibScalar
gs2124AccountAddPassword = _Gs2124AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 5),
    _Gs2124AccountAddPassword_Type()
)
gs2124AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AccountAddPassword.setStatus("current")


class _Gs2124DoAccountAdd_Type(Integer32):
    """Custom type gs2124DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DoAccountAdd_Type.__name__ = "Integer32"
_Gs2124DoAccountAdd_Object = MibScalar
gs2124DoAccountAdd = _Gs2124DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 6),
    _Gs2124DoAccountAdd_Type()
)
gs2124DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DoAccountAdd.setStatus("current")


class _Gs2124AccountDel_Type(Integer32):
    """Custom type gs2124AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Gs2124AccountDel_Type.__name__ = "Integer32"
_Gs2124AccountDel_Object = MibScalar
gs2124AccountDel = _Gs2124AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 4, 7),
    _Gs2124AccountDel_Type()
)
gs2124AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AccountDel.setStatus("current")
_Gs2124Vsm_ObjectIdentity = ObjectIdentity
gs2124Vsm = _Gs2124Vsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 5)
)


class _Gs2124VsmState_Type(Integer32):
    """Custom type gs2124VsmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124VsmState_Type.__name__ = "Integer32"
_Gs2124VsmState_Object = MibScalar
gs2124VsmState = _Gs2124VsmState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 5, 1),
    _Gs2124VsmState_Type()
)
gs2124VsmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VsmState.setStatus("current")


class _Gs2124VsmRole_Type(Integer32):
    """Custom type gs2124VsmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124VsmRole_Type.__name__ = "Integer32"
_Gs2124VsmRole_Object = MibScalar
gs2124VsmRole = _Gs2124VsmRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 5, 2),
    _Gs2124VsmRole_Type()
)
gs2124VsmRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VsmRole.setStatus("current")
_Gs2124VsmGroupid_Type = DisplayString
_Gs2124VsmGroupid_Object = MibScalar
gs2124VsmGroupid = _Gs2124VsmGroupid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 1, 5, 3),
    _Gs2124VsmGroupid_Type()
)
gs2124VsmGroupid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VsmGroupid.setStatus("current")
_Gs2124Snmp_ObjectIdentity = ObjectIdentity
gs2124Snmp = _Gs2124Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2)
)
_Gs2124GetCommunity_Type = DisplayString
_Gs2124GetCommunity_Object = MibScalar
gs2124GetCommunity = _Gs2124GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 1),
    _Gs2124GetCommunity_Type()
)
gs2124GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GetCommunity.setStatus("current")
_Gs2124SetCommunity_Type = DisplayString
_Gs2124SetCommunity_Object = MibScalar
gs2124SetCommunity = _Gs2124SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 2),
    _Gs2124SetCommunity_Type()
)
gs2124SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124SetCommunity.setStatus("current")


class _Gs2124TrapHostNumber_Type(Integer32):
    """Custom type gs2124TrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2124TrapHostNumber_Type.__name__ = "Integer32"
_Gs2124TrapHostNumber_Object = MibScalar
gs2124TrapHostNumber = _Gs2124TrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 3),
    _Gs2124TrapHostNumber_Type()
)
gs2124TrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TrapHostNumber.setStatus("current")
_Gs2124TrapHostTable_Object = MibTable
gs2124TrapHostTable = _Gs2124TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 4)
)
if mibBuilder.loadTexts:
    gs2124TrapHostTable.setStatus("current")
_Gs2124TrapHostEntry_Object = MibTableRow
gs2124TrapHostEntry = _Gs2124TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 4, 1)
)
gs2124TrapHostEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124TrapHostIndex"),
)
if mibBuilder.loadTexts:
    gs2124TrapHostEntry.setStatus("current")


class _Gs2124TrapHostIndex_Type(Integer32):
    """Custom type gs2124TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2124TrapHostIndex_Type.__name__ = "Integer32"
_Gs2124TrapHostIndex_Object = MibTableColumn
gs2124TrapHostIndex = _Gs2124TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 4, 1, 1),
    _Gs2124TrapHostIndex_Type()
)
gs2124TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TrapHostIndex.setStatus("current")
_Gs2124TrapHostIP_Type = IpAddress
_Gs2124TrapHostIP_Object = MibTableColumn
gs2124TrapHostIP = _Gs2124TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 4, 1, 2),
    _Gs2124TrapHostIP_Type()
)
gs2124TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrapHostIP.setStatus("current")


class _Gs2124TrapHostPort_Type(Integer32):
    """Custom type gs2124TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124TrapHostPort_Type.__name__ = "Integer32"
_Gs2124TrapHostPort_Object = MibTableColumn
gs2124TrapHostPort = _Gs2124TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 4, 1, 3),
    _Gs2124TrapHostPort_Type()
)
gs2124TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrapHostPort.setStatus("current")
_Gs2124TrapHostCommunity_Type = DisplayString
_Gs2124TrapHostCommunity_Object = MibTableColumn
gs2124TrapHostCommunity = _Gs2124TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 2, 4, 1, 4),
    _Gs2124TrapHostCommunity_Type()
)
gs2124TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrapHostCommunity.setStatus("current")
_Gs2124Alarm_ObjectIdentity = ObjectIdentity
gs2124Alarm = _Gs2124Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3)
)
_Gs2124Event_ObjectIdentity = ObjectIdentity
gs2124Event = _Gs2124Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1)
)


class _Gs2124EventNumber_Type(Integer32):
    """Custom type gs2124EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124EventNumber_Type.__name__ = "Integer32"
_Gs2124EventNumber_Object = MibScalar
gs2124EventNumber = _Gs2124EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 1),
    _Gs2124EventNumber_Type()
)
gs2124EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124EventNumber.setStatus("current")
_Gs2124EventTable_Object = MibTable
gs2124EventTable = _Gs2124EventTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2124EventTable.setStatus("current")
_Gs2124EventEntry_Object = MibTableRow
gs2124EventEntry = _Gs2124EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 2, 1)
)
gs2124EventEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124EventIndex"),
)
if mibBuilder.loadTexts:
    gs2124EventEntry.setStatus("current")


class _Gs2124EventIndex_Type(Integer32):
    """Custom type gs2124EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124EventIndex_Type.__name__ = "Integer32"
_Gs2124EventIndex_Object = MibTableColumn
gs2124EventIndex = _Gs2124EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 2, 1, 1),
    _Gs2124EventIndex_Type()
)
gs2124EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124EventIndex.setStatus("current")
_Gs2124EventName_Type = DisplayString
_Gs2124EventName_Object = MibTableColumn
gs2124EventName = _Gs2124EventName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 2, 1, 2),
    _Gs2124EventName_Type()
)
gs2124EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124EventName.setStatus("current")


class _Gs2124EventSendEmail_Type(Integer32):
    """Custom type gs2124EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124EventSendEmail_Type.__name__ = "Integer32"
_Gs2124EventSendEmail_Object = MibTableColumn
gs2124EventSendEmail = _Gs2124EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 2, 1, 3),
    _Gs2124EventSendEmail_Type()
)
gs2124EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EventSendEmail.setStatus("current")


class _Gs2124EventSendTrap_Type(Integer32):
    """Custom type gs2124EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124EventSendTrap_Type.__name__ = "Integer32"
_Gs2124EventSendTrap_Object = MibTableColumn
gs2124EventSendTrap = _Gs2124EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 1, 2, 1, 4),
    _Gs2124EventSendTrap_Type()
)
gs2124EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EventSendTrap.setStatus("current")
_Gs2124Email_ObjectIdentity = ObjectIdentity
gs2124Email = _Gs2124Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2)
)
_Gs2124EmailServer_Type = DisplayString
_Gs2124EmailServer_Object = MibScalar
gs2124EmailServer = _Gs2124EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 1),
    _Gs2124EmailServer_Type()
)
gs2124EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EmailServer.setStatus("current")
_Gs2124EmailUsername_Type = DisplayString
_Gs2124EmailUsername_Object = MibScalar
gs2124EmailUsername = _Gs2124EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 2),
    _Gs2124EmailUsername_Type()
)
gs2124EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EmailUsername.setStatus("current")
_Gs2124EmailPassword_Type = DisplayString
_Gs2124EmailPassword_Object = MibScalar
gs2124EmailPassword = _Gs2124EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 3),
    _Gs2124EmailPassword_Type()
)
gs2124EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EmailPassword.setStatus("current")
_Gs2124EmailSender_Type = DisplayString
_Gs2124EmailSender_Object = MibScalar
gs2124EmailSender = _Gs2124EmailSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 4),
    _Gs2124EmailSender_Type()
)
gs2124EmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EmailSender.setStatus("current")
_Gs2124EmailReturnPath_Type = DisplayString
_Gs2124EmailReturnPath_Object = MibScalar
gs2124EmailReturnPath = _Gs2124EmailReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 5),
    _Gs2124EmailReturnPath_Type()
)
gs2124EmailReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EmailReturnPath.setStatus("current")


class _Gs2124EmailUserNumber_Type(Integer32):
    """Custom type gs2124EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2124EmailUserNumber_Type.__name__ = "Integer32"
_Gs2124EmailUserNumber_Object = MibScalar
gs2124EmailUserNumber = _Gs2124EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 6),
    _Gs2124EmailUserNumber_Type()
)
gs2124EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124EmailUserNumber.setStatus("current")
_Gs2124EmailUserTable_Object = MibTable
gs2124EmailUserTable = _Gs2124EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    gs2124EmailUserTable.setStatus("current")
_Gs2124EmailUserEntry_Object = MibTableRow
gs2124EmailUserEntry = _Gs2124EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 7, 1)
)
gs2124EmailUserEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124EmailUserIndex"),
)
if mibBuilder.loadTexts:
    gs2124EmailUserEntry.setStatus("current")


class _Gs2124EmailUserIndex_Type(Integer32):
    """Custom type gs2124EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2124EmailUserIndex_Type.__name__ = "Integer32"
_Gs2124EmailUserIndex_Object = MibTableColumn
gs2124EmailUserIndex = _Gs2124EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 7, 1, 1),
    _Gs2124EmailUserIndex_Type()
)
gs2124EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124EmailUserIndex.setStatus("current")
_Gs2124EmailUserAddress_Type = DisplayString
_Gs2124EmailUserAddress_Object = MibTableColumn
gs2124EmailUserAddress = _Gs2124EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 3, 2, 7, 1, 2),
    _Gs2124EmailUserAddress_Type()
)
gs2124EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EmailUserAddress.setStatus("current")
_Gs2124Configuration_ObjectIdentity = ObjectIdentity
gs2124Configuration = _Gs2124Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5)
)
_Gs2124SaveRestore_ObjectIdentity = ObjectIdentity
gs2124SaveRestore = _Gs2124SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 1)
)


class _Gs2124SaveStart_Type(Integer32):
    """Custom type gs2124SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124SaveStart_Type.__name__ = "Integer32"
_Gs2124SaveStart_Object = MibScalar
gs2124SaveStart = _Gs2124SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 1, 1),
    _Gs2124SaveStart_Type()
)
gs2124SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124SaveStart.setStatus("current")


class _Gs2124SaveUser_Type(Integer32):
    """Custom type gs2124SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124SaveUser_Type.__name__ = "Integer32"
_Gs2124SaveUser_Object = MibScalar
gs2124SaveUser = _Gs2124SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 1, 2),
    _Gs2124SaveUser_Type()
)
gs2124SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124SaveUser.setStatus("current")


class _Gs2124RestoreDefault_Type(Integer32):
    """Custom type gs2124RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2124RestoreDefault_Type.__name__ = "Integer32"
_Gs2124RestoreDefault_Object = MibScalar
gs2124RestoreDefault = _Gs2124RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 1, 3),
    _Gs2124RestoreDefault_Type()
)
gs2124RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124RestoreDefault.setStatus("current")


class _Gs2124RestoreUser_Type(Integer32):
    """Custom type gs2124RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124RestoreUser_Type.__name__ = "Integer32"
_Gs2124RestoreUser_Object = MibScalar
gs2124RestoreUser = _Gs2124RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 1, 4),
    _Gs2124RestoreUser_Type()
)
gs2124RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124RestoreUser.setStatus("current")
_Gs2124ConfigFile_ObjectIdentity = ObjectIdentity
gs2124ConfigFile = _Gs2124ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 2)
)
_Gs2124ExportIpAddress_Type = IpAddress
_Gs2124ExportIpAddress_Object = MibScalar
gs2124ExportIpAddress = _Gs2124ExportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 2, 1),
    _Gs2124ExportIpAddress_Type()
)
gs2124ExportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ExportIpAddress.setStatus("current")


class _Gs2124DoExportConfig_Type(Integer32):
    """Custom type gs2124DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2124DoExportConfig_Type.__name__ = "Integer32"
_Gs2124DoExportConfig_Object = MibScalar
gs2124DoExportConfig = _Gs2124DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 2, 2),
    _Gs2124DoExportConfig_Type()
)
gs2124DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DoExportConfig.setStatus("current")
_Gs2124ImportIpAddress_Type = IpAddress
_Gs2124ImportIpAddress_Object = MibScalar
gs2124ImportIpAddress = _Gs2124ImportIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 2, 3),
    _Gs2124ImportIpAddress_Type()
)
gs2124ImportIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ImportIpAddress.setStatus("current")
_Gs2124ImportConfigName_Type = DisplayString
_Gs2124ImportConfigName_Object = MibScalar
gs2124ImportConfigName = _Gs2124ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 2, 4),
    _Gs2124ImportConfigName_Type()
)
gs2124ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ImportConfigName.setStatus("current")


class _Gs2124DoImportConfig_Type(Integer32):
    """Custom type gs2124DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2124DoImportConfig_Type.__name__ = "Integer32"
_Gs2124DoImportConfig_Object = MibScalar
gs2124DoImportConfig = _Gs2124DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 5, 2, 5),
    _Gs2124DoImportConfig_Type()
)
gs2124DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DoImportConfig.setStatus("current")
_Gs2124Log_ObjectIdentity = ObjectIdentity
gs2124Log = _Gs2124Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7)
)


class _Gs2124ClearLog_Type(Integer32):
    """Custom type gs2124ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124ClearLog_Type.__name__ = "Integer32"
_Gs2124ClearLog_Object = MibScalar
gs2124ClearLog = _Gs2124ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7, 1),
    _Gs2124ClearLog_Type()
)
gs2124ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ClearLog.setStatus("current")


class _Gs2124LogNumber_Type(Integer32):
    """Custom type gs2124LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Gs2124LogNumber_Type.__name__ = "Integer32"
_Gs2124LogNumber_Object = MibScalar
gs2124LogNumber = _Gs2124LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7, 4),
    _Gs2124LogNumber_Type()
)
gs2124LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124LogNumber.setStatus("current")
_Gs2124LogTable_Object = MibTable
gs2124LogTable = _Gs2124LogTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7, 5)
)
if mibBuilder.loadTexts:
    gs2124LogTable.setStatus("current")
_Gs2124LogEntry_Object = MibTableRow
gs2124LogEntry = _Gs2124LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7, 5, 1)
)
gs2124LogEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124LogIndex"),
)
if mibBuilder.loadTexts:
    gs2124LogEntry.setStatus("current")


class _Gs2124LogIndex_Type(Integer32):
    """Custom type gs2124LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gs2124LogIndex_Type.__name__ = "Integer32"
_Gs2124LogIndex_Object = MibTableColumn
gs2124LogIndex = _Gs2124LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7, 5, 1, 1),
    _Gs2124LogIndex_Type()
)
gs2124LogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124LogIndex.setStatus("current")
_Gs2124LogEvent_Type = DisplayString
_Gs2124LogEvent_Object = MibTableColumn
gs2124LogEvent = _Gs2124LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 7, 5, 1, 2),
    _Gs2124LogEvent_Type()
)
gs2124LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124LogEvent.setStatus("current")
_Gs2124Firmware_ObjectIdentity = ObjectIdentity
gs2124Firmware = _Gs2124Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 8)
)
_Gs2124FirmwareIpAddress_Type = IpAddress
_Gs2124FirmwareIpAddress_Object = MibScalar
gs2124FirmwareIpAddress = _Gs2124FirmwareIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 8, 1),
    _Gs2124FirmwareIpAddress_Type()
)
gs2124FirmwareIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124FirmwareIpAddress.setStatus("current")
_Gs2124FirmwareFileName_Type = DisplayString
_Gs2124FirmwareFileName_Object = MibScalar
gs2124FirmwareFileName = _Gs2124FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 8, 2),
    _Gs2124FirmwareFileName_Type()
)
gs2124FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124FirmwareFileName.setStatus("current")


class _Gs2124DoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2124DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2124DoFirmwareUpgrade_Object = MibScalar
gs2124DoFirmwareUpgrade = _Gs2124DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 8, 3),
    _Gs2124DoFirmwareUpgrade_Type()
)
gs2124DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DoFirmwareUpgrade.setStatus("current")
_Gs2124Port_ObjectIdentity = ObjectIdentity
gs2124Port = _Gs2124Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9)
)
_Gs2124PortStatus_ObjectIdentity = ObjectIdentity
gs2124PortStatus = _Gs2124PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1)
)


class _Gs2124PortStatusNumber_Type(Integer32):
    """Custom type gs2124PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124PortStatusNumber_Type.__name__ = "Integer32"
_Gs2124PortStatusNumber_Object = MibScalar
gs2124PortStatusNumber = _Gs2124PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 1),
    _Gs2124PortStatusNumber_Type()
)
gs2124PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusNumber.setStatus("current")
_Gs2124PortStatusTable_Object = MibTable
gs2124PortStatusTable = _Gs2124PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    gs2124PortStatusTable.setStatus("current")
_Gs2124PortStatusEntry_Object = MibTableRow
gs2124PortStatusEntry = _Gs2124PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1)
)
gs2124PortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124PortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2124PortStatusEntry.setStatus("current")


class _Gs2124PortStatusIndex_Type(Integer32):
    """Custom type gs2124PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124PortStatusIndex_Type.__name__ = "Integer32"
_Gs2124PortStatusIndex_Object = MibTableColumn
gs2124PortStatusIndex = _Gs2124PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 1),
    _Gs2124PortStatusIndex_Type()
)
gs2124PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusIndex.setStatus("current")
_Gs2124PortStatusMedia_Type = DisplayString
_Gs2124PortStatusMedia_Object = MibTableColumn
gs2124PortStatusMedia = _Gs2124PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 2),
    _Gs2124PortStatusMedia_Type()
)
gs2124PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusMedia.setStatus("current")
_Gs2124PortStatusPortState_Type = DisplayString
_Gs2124PortStatusPortState_Object = MibTableColumn
gs2124PortStatusPortState = _Gs2124PortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 3),
    _Gs2124PortStatusPortState_Type()
)
gs2124PortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusPortState.setStatus("current")
_Gs2124PortStatusLink_Type = DisplayString
_Gs2124PortStatusLink_Object = MibTableColumn
gs2124PortStatusLink = _Gs2124PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 4),
    _Gs2124PortStatusLink_Type()
)
gs2124PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusLink.setStatus("current")
_Gs2124PortStatusAutoNego_Type = DisplayString
_Gs2124PortStatusAutoNego_Object = MibTableColumn
gs2124PortStatusAutoNego = _Gs2124PortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 5),
    _Gs2124PortStatusAutoNego_Type()
)
gs2124PortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusAutoNego.setStatus("current")
_Gs2124PortStatusSpdDpx_Type = DisplayString
_Gs2124PortStatusSpdDpx_Object = MibTableColumn
gs2124PortStatusSpdDpx = _Gs2124PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 6),
    _Gs2124PortStatusSpdDpx_Type()
)
gs2124PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusSpdDpx.setStatus("current")
_Gs2124PortStatusFlwCtrlRx_Type = DisplayString
_Gs2124PortStatusFlwCtrlRx_Object = MibTableColumn
gs2124PortStatusFlwCtrlRx = _Gs2124PortStatusFlwCtrlRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 7),
    _Gs2124PortStatusFlwCtrlRx_Type()
)
gs2124PortStatusFlwCtrlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusFlwCtrlRx.setStatus("current")
_Gs2124PortStatusFlwCtrlTx_Type = DisplayString
_Gs2124PortStatusFlwCtrlTx_Object = MibTableColumn
gs2124PortStatusFlwCtrlTx = _Gs2124PortStatusFlwCtrlTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 8),
    _Gs2124PortStatusFlwCtrlTx_Type()
)
gs2124PortStatusFlwCtrlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatusFlwCtrlTx.setStatus("current")
_Gs2124PortStatuDescription_Type = DisplayString
_Gs2124PortStatuDescription_Object = MibTableColumn
gs2124PortStatuDescription = _Gs2124PortStatuDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 1, 2, 1, 9),
    _Gs2124PortStatuDescription_Type()
)
gs2124PortStatuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortStatuDescription.setStatus("current")
_Gs2124PortConf_ObjectIdentity = ObjectIdentity
gs2124PortConf = _Gs2124PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2)
)


class _Gs2124PortConfNumber_Type(Integer32):
    """Custom type gs2124PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124PortConfNumber_Type.__name__ = "Integer32"
_Gs2124PortConfNumber_Object = MibScalar
gs2124PortConfNumber = _Gs2124PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 1),
    _Gs2124PortConfNumber_Type()
)
gs2124PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortConfNumber.setStatus("current")
_Gs2124PortConfTable_Object = MibTable
gs2124PortConfTable = _Gs2124PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    gs2124PortConfTable.setStatus("current")
_Gs2124PortConfEntry_Object = MibTableRow
gs2124PortConfEntry = _Gs2124PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1)
)
gs2124PortConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124PortConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124PortConfEntry.setStatus("current")


class _Gs2124PortConfIndex_Type(Integer32):
    """Custom type gs2124PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124PortConfIndex_Type.__name__ = "Integer32"
_Gs2124PortConfIndex_Object = MibTableColumn
gs2124PortConfIndex = _Gs2124PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 1),
    _Gs2124PortConfIndex_Type()
)
gs2124PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124PortConfIndex.setStatus("current")


class _Gs2124PortConfPortState_Type(Integer32):
    """Custom type gs2124PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124PortConfPortState_Type.__name__ = "Integer32"
_Gs2124PortConfPortState_Object = MibTableColumn
gs2124PortConfPortState = _Gs2124PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 2),
    _Gs2124PortConfPortState_Type()
)
gs2124PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfPortState.setStatus("current")


class _Gs2124PortConfTPSpdDpx_Type(Integer32):
    """Custom type gs2124PortConfTPSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Gs2124PortConfTPSpdDpx_Type.__name__ = "Integer32"
_Gs2124PortConfTPSpdDpx_Object = MibTableColumn
gs2124PortConfTPSpdDpx = _Gs2124PortConfTPSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 3),
    _Gs2124PortConfTPSpdDpx_Type()
)
gs2124PortConfTPSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfTPSpdDpx.setStatus("current")


class _Gs2124PortConfSFPSpdDpx_Type(Integer32):
    """Custom type gs2124PortConfSFPSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
    )


_Gs2124PortConfSFPSpdDpx_Type.__name__ = "Integer32"
_Gs2124PortConfSFPSpdDpx_Object = MibTableColumn
gs2124PortConfSFPSpdDpx = _Gs2124PortConfSFPSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 4),
    _Gs2124PortConfSFPSpdDpx_Type()
)
gs2124PortConfSFPSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfSFPSpdDpx.setStatus("current")


class _Gs2124PortConfFlwCtrl_Type(Integer32):
    """Custom type gs2124PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124PortConfFlwCtrl_Type.__name__ = "Integer32"
_Gs2124PortConfFlwCtrl_Object = MibTableColumn
gs2124PortConfFlwCtrl = _Gs2124PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 5),
    _Gs2124PortConfFlwCtrl_Type()
)
gs2124PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfFlwCtrl.setStatus("current")


class _Gs2124PortConfExcessiveCollisionMode_Type(Integer32):
    """Custom type gs2124PortConfExcessiveCollisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124PortConfExcessiveCollisionMode_Type.__name__ = "Integer32"
_Gs2124PortConfExcessiveCollisionMode_Object = MibTableColumn
gs2124PortConfExcessiveCollisionMode = _Gs2124PortConfExcessiveCollisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 6),
    _Gs2124PortConfExcessiveCollisionMode_Type()
)
gs2124PortConfExcessiveCollisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfExcessiveCollisionMode.setStatus("current")
_Gs2124PortConfDescription_Type = DisplayString
_Gs2124PortConfDescription_Object = MibTableColumn
gs2124PortConfDescription = _Gs2124PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 7),
    _Gs2124PortConfDescription_Type()
)
gs2124PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfDescription.setStatus("current")


class _Gs2124PortConfPowerSaving_Type(Integer32):
    """Custom type gs2124PortConfPowerSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124PortConfPowerSaving_Type.__name__ = "Integer32"
_Gs2124PortConfPowerSaving_Object = MibTableColumn
gs2124PortConfPowerSaving = _Gs2124PortConfPowerSaving_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 2, 2, 1, 8),
    _Gs2124PortConfPowerSaving_Type()
)
gs2124PortConfPowerSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortConfPowerSaving.setStatus("current")
_Gs2124SFPInfo_ObjectIdentity = ObjectIdentity
gs2124SFPInfo = _Gs2124SFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3)
)


class _Gs2124SFPInfoNumber_Type(Integer32):
    """Custom type gs2124SFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124SFPInfoNumber_Type.__name__ = "Integer32"
_Gs2124SFPInfoNumber_Object = MibScalar
gs2124SFPInfoNumber = _Gs2124SFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 1),
    _Gs2124SFPInfoNumber_Type()
)
gs2124SFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPInfoNumber.setStatus("current")
_Gs2124SFPInfoTable_Object = MibTable
gs2124SFPInfoTable = _Gs2124SFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    gs2124SFPInfoTable.setStatus("current")
_Gs2124SFPInfoEntry_Object = MibTableRow
gs2124SFPInfoEntry = _Gs2124SFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1)
)
gs2124SFPInfoEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124SFPInfoIndex"),
)
if mibBuilder.loadTexts:
    gs2124SFPInfoEntry.setStatus("current")


class _Gs2124SFPInfoIndex_Type(Integer32):
    """Custom type gs2124SFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124SFPInfoIndex_Type.__name__ = "Integer32"
_Gs2124SFPInfoIndex_Object = MibTableColumn
gs2124SFPInfoIndex = _Gs2124SFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 1),
    _Gs2124SFPInfoIndex_Type()
)
gs2124SFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPInfoIndex.setStatus("current")
_Gs2124SFPConnectorType_Type = DisplayString
_Gs2124SFPConnectorType_Object = MibTableColumn
gs2124SFPConnectorType = _Gs2124SFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 2),
    _Gs2124SFPConnectorType_Type()
)
gs2124SFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPConnectorType.setStatus("current")
_Gs2124SFPFiberType_Type = DisplayString
_Gs2124SFPFiberType_Object = MibTableColumn
gs2124SFPFiberType = _Gs2124SFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 3),
    _Gs2124SFPFiberType_Type()
)
gs2124SFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPFiberType.setStatus("current")
_Gs2124SFPWavelength_Type = DisplayString
_Gs2124SFPWavelength_Object = MibTableColumn
gs2124SFPWavelength = _Gs2124SFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 4),
    _Gs2124SFPWavelength_Type()
)
gs2124SFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPWavelength.setStatus("current")
_Gs2124SFPBaudRate_Type = DisplayString
_Gs2124SFPBaudRate_Object = MibTableColumn
gs2124SFPBaudRate = _Gs2124SFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 5),
    _Gs2124SFPBaudRate_Type()
)
gs2124SFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPBaudRate.setStatus("current")
_Gs2124SFPVendorOUI_Type = DisplayString
_Gs2124SFPVendorOUI_Object = MibTableColumn
gs2124SFPVendorOUI = _Gs2124SFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 6),
    _Gs2124SFPVendorOUI_Type()
)
gs2124SFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPVendorOUI.setStatus("current")
_Gs2124SFPVendorName_Type = DisplayString
_Gs2124SFPVendorName_Object = MibTableColumn
gs2124SFPVendorName = _Gs2124SFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 7),
    _Gs2124SFPVendorName_Type()
)
gs2124SFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPVendorName.setStatus("current")
_Gs2124SFPVendorPN_Type = DisplayString
_Gs2124SFPVendorPN_Object = MibTableColumn
gs2124SFPVendorPN = _Gs2124SFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 8),
    _Gs2124SFPVendorPN_Type()
)
gs2124SFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPVendorPN.setStatus("current")
_Gs2124SFPVendorRev_Type = DisplayString
_Gs2124SFPVendorRev_Object = MibTableColumn
gs2124SFPVendorRev = _Gs2124SFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 9),
    _Gs2124SFPVendorRev_Type()
)
gs2124SFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPVendorRev.setStatus("current")
_Gs2124SFPVendorSN_Type = DisplayString
_Gs2124SFPVendorSN_Object = MibTableColumn
gs2124SFPVendorSN = _Gs2124SFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 10),
    _Gs2124SFPVendorSN_Type()
)
gs2124SFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPVendorSN.setStatus("current")
_Gs2124SFPDateCode_Type = DisplayString
_Gs2124SFPDateCode_Object = MibTableColumn
gs2124SFPDateCode = _Gs2124SFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 11),
    _Gs2124SFPDateCode_Type()
)
gs2124SFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPDateCode.setStatus("current")
_Gs2124SFPTemperature_Type = DisplayString
_Gs2124SFPTemperature_Object = MibTableColumn
gs2124SFPTemperature = _Gs2124SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 12),
    _Gs2124SFPTemperature_Type()
)
gs2124SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPTemperature.setStatus("current")
_Gs2124SFPVcc_Type = DisplayString
_Gs2124SFPVcc_Object = MibTableColumn
gs2124SFPVcc = _Gs2124SFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 13),
    _Gs2124SFPVcc_Type()
)
gs2124SFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPVcc.setStatus("current")
_Gs2124SFPTxBias_Type = DisplayString
_Gs2124SFPTxBias_Object = MibTableColumn
gs2124SFPTxBias = _Gs2124SFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 14),
    _Gs2124SFPTxBias_Type()
)
gs2124SFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPTxBias.setStatus("current")
_Gs2124SFPTxPWR_Type = DisplayString
_Gs2124SFPTxPWR_Object = MibTableColumn
gs2124SFPTxPWR = _Gs2124SFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 15),
    _Gs2124SFPTxPWR_Type()
)
gs2124SFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPTxPWR.setStatus("current")
_Gs2124SFPRxPWR_Type = DisplayString
_Gs2124SFPRxPWR_Object = MibTableColumn
gs2124SFPRxPWR = _Gs2124SFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 9, 3, 2, 1, 16),
    _Gs2124SFPRxPWR_Type()
)
gs2124SFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SFPRxPWR.setStatus("current")
_Gs2124Mirror_ObjectIdentity = ObjectIdentity
gs2124Mirror = _Gs2124Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10)
)


class _Gs2124MirroringPort_Type(Integer32):
    """Custom type gs2124MirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Gs2124MirroringPort_Type.__name__ = "Integer32"
_Gs2124MirroringPort_Object = MibScalar
gs2124MirroringPort = _Gs2124MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10, 1),
    _Gs2124MirroringPort_Type()
)
gs2124MirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MirroringPort.setStatus("current")
_Gs2124MirroredPortsTable_Object = MibTable
gs2124MirroredPortsTable = _Gs2124MirroredPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10, 2)
)
if mibBuilder.loadTexts:
    gs2124MirroredPortsTable.setStatus("current")
_Gs2124MirroredPortsEntry_Object = MibTableRow
gs2124MirroredPortsEntry = _Gs2124MirroredPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10, 2, 1)
)
gs2124MirroredPortsEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MirroredPortIndex"),
)
if mibBuilder.loadTexts:
    gs2124MirroredPortsEntry.setStatus("current")


class _Gs2124MirroredPortIndex_Type(Integer32):
    """Custom type gs2124MirroredPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124MirroredPortIndex_Type.__name__ = "Integer32"
_Gs2124MirroredPortIndex_Object = MibTableColumn
gs2124MirroredPortIndex = _Gs2124MirroredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10, 2, 1, 1),
    _Gs2124MirroredPortIndex_Type()
)
gs2124MirroredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MirroredPortIndex.setStatus("current")


class _Gs2124MirroredPortSrouceEnable_Type(Integer32):
    """Custom type gs2124MirroredPortSrouceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124MirroredPortSrouceEnable_Type.__name__ = "Integer32"
_Gs2124MirroredPortSrouceEnable_Object = MibTableColumn
gs2124MirroredPortSrouceEnable = _Gs2124MirroredPortSrouceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10, 2, 1, 2),
    _Gs2124MirroredPortSrouceEnable_Type()
)
gs2124MirroredPortSrouceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MirroredPortSrouceEnable.setStatus("current")


class _Gs2124MirroredPortDestinationEnable_Type(Integer32):
    """Custom type gs2124MirroredPortDestinationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124MirroredPortDestinationEnable_Type.__name__ = "Integer32"
_Gs2124MirroredPortDestinationEnable_Object = MibTableColumn
gs2124MirroredPortDestinationEnable = _Gs2124MirroredPortDestinationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 10, 2, 1, 3),
    _Gs2124MirroredPortDestinationEnable_Type()
)
gs2124MirroredPortDestinationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MirroredPortDestinationEnable.setStatus("current")
_Gs2124MaxPktLen_ObjectIdentity = ObjectIdentity
gs2124MaxPktLen = _Gs2124MaxPktLen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 11)
)


class _Gs2124MaxPktLenPortNumber_Type(Integer32):
    """Custom type gs2124MaxPktLenPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124MaxPktLenPortNumber_Type.__name__ = "Integer32"
_Gs2124MaxPktLenPortNumber_Object = MibScalar
gs2124MaxPktLenPortNumber = _Gs2124MaxPktLenPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 11, 1),
    _Gs2124MaxPktLenPortNumber_Type()
)
gs2124MaxPktLenPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MaxPktLenPortNumber.setStatus("current")
_Gs2124MaxPktLenConfTable_Object = MibTable
gs2124MaxPktLenConfTable = _Gs2124MaxPktLenConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 11, 2)
)
if mibBuilder.loadTexts:
    gs2124MaxPktLenConfTable.setStatus("current")
_Gs2124MaxPktLenConfEntry_Object = MibTableRow
gs2124MaxPktLenConfEntry = _Gs2124MaxPktLenConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 11, 2, 1)
)
gs2124MaxPktLenConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MaxPktLenConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124MaxPktLenConfEntry.setStatus("current")


class _Gs2124MaxPktLenConfIndex_Type(Integer32):
    """Custom type gs2124MaxPktLenConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124MaxPktLenConfIndex_Type.__name__ = "Integer32"
_Gs2124MaxPktLenConfIndex_Object = MibTableColumn
gs2124MaxPktLenConfIndex = _Gs2124MaxPktLenConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 11, 2, 1, 1),
    _Gs2124MaxPktLenConfIndex_Type()
)
gs2124MaxPktLenConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MaxPktLenConfIndex.setStatus("current")


class _Gs2124MaxPktLenConfSetting_Type(Integer32):
    """Custom type gs2124MaxPktLenConfSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_Gs2124MaxPktLenConfSetting_Type.__name__ = "Integer32"
_Gs2124MaxPktLenConfSetting_Object = MibTableColumn
gs2124MaxPktLenConfSetting = _Gs2124MaxPktLenConfSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 11, 2, 1, 2),
    _Gs2124MaxPktLenConfSetting_Type()
)
gs2124MaxPktLenConfSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MaxPktLenConfSetting.setStatus("current")
_Gs2124LoopDetectedConf_ObjectIdentity = ObjectIdentity
gs2124LoopDetectedConf = _Gs2124LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12)
)


class _Gs2124LoopDetectedNumber_Type(Integer32):
    """Custom type gs2124LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124LoopDetectedNumber_Type.__name__ = "Integer32"
_Gs2124LoopDetectedNumber_Object = MibScalar
gs2124LoopDetectedNumber = _Gs2124LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12, 1),
    _Gs2124LoopDetectedNumber_Type()
)
gs2124LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124LoopDetectedNumber.setStatus("current")
_Gs2124LoopDetectedTable_Object = MibTable
gs2124LoopDetectedTable = _Gs2124LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12, 2)
)
if mibBuilder.loadTexts:
    gs2124LoopDetectedTable.setStatus("current")
_Gs2124LoopDetectedEntry_Object = MibTableRow
gs2124LoopDetectedEntry = _Gs2124LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12, 2, 1)
)
gs2124LoopDetectedEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    gs2124LoopDetectedEntry.setStatus("current")


class _Gs2124LoopDetectedfIndex_Type(Integer32):
    """Custom type gs2124LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2124LoopDetectedfIndex_Type.__name__ = "Integer32"
_Gs2124LoopDetectedfIndex_Object = MibTableColumn
gs2124LoopDetectedfIndex = _Gs2124LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12, 2, 1, 1),
    _Gs2124LoopDetectedfIndex_Type()
)
gs2124LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124LoopDetectedfIndex.setStatus("current")


class _Gs2124LoopDetectedPort_Type(Integer32):
    """Custom type gs2124LoopDetectedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124LoopDetectedPort_Type.__name__ = "Integer32"
_Gs2124LoopDetectedPort_Object = MibTableColumn
gs2124LoopDetectedPort = _Gs2124LoopDetectedPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12, 2, 1, 2),
    _Gs2124LoopDetectedPort_Type()
)
gs2124LoopDetectedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124LoopDetectedPort.setStatus("current")


class _Gs2124LoopDetectedLockedPort_Type(Integer32):
    """Custom type gs2124LoopDetectedLockedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124LoopDetectedLockedPort_Type.__name__ = "Integer32"
_Gs2124LoopDetectedLockedPort_Object = MibTableColumn
gs2124LoopDetectedLockedPort = _Gs2124LoopDetectedLockedPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 12, 2, 1, 3),
    _Gs2124LoopDetectedLockedPort_Type()
)
gs2124LoopDetectedLockedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124LoopDetectedLockedPort.setStatus("current")
_Gs2124ManagementPolicy_ObjectIdentity = ObjectIdentity
gs2124ManagementPolicy = _Gs2124ManagementPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13)
)


class _Gs2124ManagementSecurityNumber_Type(Integer32):
    """Custom type gs2124ManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2124ManagementSecurityNumber_Type.__name__ = "Integer32"
_Gs2124ManagementSecurityNumber_Object = MibScalar
gs2124ManagementSecurityNumber = _Gs2124ManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 1),
    _Gs2124ManagementSecurityNumber_Type()
)
gs2124ManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityNumber.setStatus("current")


class _Gs2124ManagementSecurityEntryCreate_Type(Integer32):
    """Custom type gs2124ManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Gs2124ManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Gs2124ManagementSecurityEntryCreate_Object = MibScalar
gs2124ManagementSecurityEntryCreate = _Gs2124ManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 2),
    _Gs2124ManagementSecurityEntryCreate_Type()
)
gs2124ManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityEntryCreate.setStatus("current")
_Gs2124ManagementSecurityTable_Object = MibTable
gs2124ManagementSecurityTable = _Gs2124ManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3)
)
if mibBuilder.loadTexts:
    gs2124ManagementSecurityTable.setStatus("current")
_Gs2124ManagementSecurityEntry_Object = MibTableRow
gs2124ManagementSecurityEntry = _Gs2124ManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1)
)
gs2124ManagementSecurityEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124ManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    gs2124ManagementSecurityEntry.setStatus("current")


class _Gs2124ManagementSecurityIndex_Type(Integer32):
    """Custom type gs2124ManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Gs2124ManagementSecurityIndex_Type.__name__ = "Integer32"
_Gs2124ManagementSecurityIndex_Object = MibTableColumn
gs2124ManagementSecurityIndex = _Gs2124ManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 1),
    _Gs2124ManagementSecurityIndex_Type()
)
gs2124ManagementSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityIndex.setStatus("current")
_Gs2124ManagementSecurityName_Type = DisplayString
_Gs2124ManagementSecurityName_Object = MibTableColumn
gs2124ManagementSecurityName = _Gs2124ManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 2),
    _Gs2124ManagementSecurityName_Type()
)
gs2124ManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityName.setStatus("current")
_Gs2124ManagementSecurityIpRange_Type = DisplayString
_Gs2124ManagementSecurityIpRange_Object = MibTableColumn
gs2124ManagementSecurityIpRange = _Gs2124ManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 3),
    _Gs2124ManagementSecurityIpRange_Type()
)
gs2124ManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityIpRange.setStatus("current")
_Gs2124ManagementSecurityIncomigPort_Type = DisplayString
_Gs2124ManagementSecurityIncomigPort_Object = MibTableColumn
gs2124ManagementSecurityIncomigPort = _Gs2124ManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 4),
    _Gs2124ManagementSecurityIncomigPort_Type()
)
gs2124ManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityIncomigPort.setStatus("current")
_Gs2124ManagementSecurityAccessType_Type = DisplayString
_Gs2124ManagementSecurityAccessType_Object = MibTableColumn
gs2124ManagementSecurityAccessType = _Gs2124ManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 5),
    _Gs2124ManagementSecurityAccessType_Type()
)
gs2124ManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityAccessType.setStatus("current")


class _Gs2124ManagementSecurityAction_Type(Integer32):
    """Custom type gs2124ManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124ManagementSecurityAction_Type.__name__ = "Integer32"
_Gs2124ManagementSecurityAction_Object = MibTableColumn
gs2124ManagementSecurityAction = _Gs2124ManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 6),
    _Gs2124ManagementSecurityAction_Type()
)
gs2124ManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityAction.setStatus("current")


class _Gs2124ManagementSecurityEntryAction_Type(Integer32):
    """Custom type gs2124ManagementSecurityEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124ManagementSecurityEntryAction_Type.__name__ = "Integer32"
_Gs2124ManagementSecurityEntryAction_Object = MibTableColumn
gs2124ManagementSecurityEntryAction = _Gs2124ManagementSecurityEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 13, 3, 1, 7),
    _Gs2124ManagementSecurityEntryAction_Type()
)
gs2124ManagementSecurityEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementSecurityEntryAction.setStatus("current")
_Gs2124VLAN_ObjectIdentity = ObjectIdentity
gs2124VLAN = _Gs2124VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14)
)
_Gs2124VlanConf_ObjectIdentity = ObjectIdentity
gs2124VlanConf = _Gs2124VlanConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 1)
)


class _Gs2124VlanMode_Type(Integer32):
    """Custom type gs2124VlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124VlanMode_Type.__name__ = "Integer32"
_Gs2124VlanMode_Object = MibScalar
gs2124VlanMode = _Gs2124VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 1, 1),
    _Gs2124VlanMode_Type()
)
gs2124VlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanMode.setStatus("current")


class _Gs2124ManagementVlan_Type(Integer32):
    """Custom type gs2124ManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124ManagementVlan_Type.__name__ = "Integer32"
_Gs2124ManagementVlan_Object = MibScalar
gs2124ManagementVlan = _Gs2124ManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 1, 2),
    _Gs2124ManagementVlan_Type()
)
gs2124ManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124ManagementVlan.setStatus("current")
_Gs2124PortIsolation_Type = DisplayString
_Gs2124PortIsolation_Object = MibScalar
gs2124PortIsolation = _Gs2124PortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 1, 3),
    _Gs2124PortIsolation_Type()
)
gs2124PortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortIsolation.setStatus("current")


class _Gs2124TagIdentifier_Type(Integer32):
    """Custom type gs2124TagIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124TagIdentifier_Type.__name__ = "Integer32"
_Gs2124TagIdentifier_Object = MibScalar
gs2124TagIdentifier = _Gs2124TagIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 1, 4),
    _Gs2124TagIdentifier_Type()
)
gs2124TagIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagIdentifier.setStatus("current")
_Gs2124TagBaseVlanGroup_ObjectIdentity = ObjectIdentity
gs2124TagBaseVlanGroup = _Gs2124TagBaseVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2)
)


class _Gs2124TagBaseVlanNumber_Type(Integer32):
    """Custom type gs2124TagBaseVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124TagBaseVlanNumber_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanNumber_Object = MibScalar
gs2124TagBaseVlanNumber = _Gs2124TagBaseVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 1),
    _Gs2124TagBaseVlanNumber_Type()
)
gs2124TagBaseVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanNumber.setStatus("current")


class _Gs2124TagBaseVlanGroupEntryCreate_Type(Integer32):
    """Custom type gs2124TagBaseVlanGroupEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124TagBaseVlanGroupEntryCreate_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanGroupEntryCreate_Object = MibScalar
gs2124TagBaseVlanGroupEntryCreate = _Gs2124TagBaseVlanGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 2),
    _Gs2124TagBaseVlanGroupEntryCreate_Type()
)
gs2124TagBaseVlanGroupEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanGroupEntryCreate.setStatus("current")
_Gs2124TagBaseVlanGroupTable_Object = MibTable
gs2124TagBaseVlanGroupTable = _Gs2124TagBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3)
)
if mibBuilder.loadTexts:
    gs2124TagBaseVlanGroupTable.setStatus("current")
_Gs2124TagBaseVlanGroupEntry_Object = MibTableRow
gs2124TagBaseVlanGroupEntry = _Gs2124TagBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1)
)
gs2124TagBaseVlanGroupEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124TagBaseVlanVid"),
)
if mibBuilder.loadTexts:
    gs2124TagBaseVlanGroupEntry.setStatus("current")


class _Gs2124TagBaseVlanVid_Type(Integer32):
    """Custom type gs2124TagBaseVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124TagBaseVlanVid_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanVid_Object = MibTableColumn
gs2124TagBaseVlanVid = _Gs2124TagBaseVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 1),
    _Gs2124TagBaseVlanVid_Type()
)
gs2124TagBaseVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanVid.setStatus("current")
_Gs2124TagBaseVlanName_Type = DisplayString
_Gs2124TagBaseVlanName_Object = MibTableColumn
gs2124TagBaseVlanName = _Gs2124TagBaseVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 2),
    _Gs2124TagBaseVlanName_Type()
)
gs2124TagBaseVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanName.setStatus("current")


class _Gs2124TagBaseVlanIgmpProxy_Type(Integer32):
    """Custom type gs2124TagBaseVlanIgmpProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124TagBaseVlanIgmpProxy_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanIgmpProxy_Object = MibTableColumn
gs2124TagBaseVlanIgmpProxy = _Gs2124TagBaseVlanIgmpProxy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 3),
    _Gs2124TagBaseVlanIgmpProxy_Type()
)
gs2124TagBaseVlanIgmpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanIgmpProxy.setStatus("current")


class _Gs2124TagBaseVlanPrivateVlan_Type(Integer32):
    """Custom type gs2124TagBaseVlanPrivateVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124TagBaseVlanPrivateVlan_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanPrivateVlan_Object = MibTableColumn
gs2124TagBaseVlanPrivateVlan = _Gs2124TagBaseVlanPrivateVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 4),
    _Gs2124TagBaseVlanPrivateVlan_Type()
)
gs2124TagBaseVlanPrivateVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanPrivateVlan.setStatus("current")


class _Gs2124TagBaseVlanGvrp_Type(Integer32):
    """Custom type gs2124TagBaseVlanGvrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124TagBaseVlanGvrp_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanGvrp_Object = MibTableColumn
gs2124TagBaseVlanGvrp = _Gs2124TagBaseVlanGvrp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 5),
    _Gs2124TagBaseVlanGvrp_Type()
)
gs2124TagBaseVlanGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanGvrp.setStatus("current")
_Gs2124TagBaseVlanMemberPort_Type = DisplayString
_Gs2124TagBaseVlanMemberPort_Object = MibTableColumn
gs2124TagBaseVlanMemberPort = _Gs2124TagBaseVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 6),
    _Gs2124TagBaseVlanMemberPort_Type()
)
gs2124TagBaseVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanMemberPort.setStatus("current")


class _Gs2124TagBaseVlanEntryAction_Type(Integer32):
    """Custom type gs2124TagBaseVlanEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124TagBaseVlanEntryAction_Type.__name__ = "Integer32"
_Gs2124TagBaseVlanEntryAction_Object = MibTableColumn
gs2124TagBaseVlanEntryAction = _Gs2124TagBaseVlanEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 2, 3, 1, 7),
    _Gs2124TagBaseVlanEntryAction_Type()
)
gs2124TagBaseVlanEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TagBaseVlanEntryAction.setStatus("current")
_Gs2124VlanPortConfTable_Object = MibTable
gs2124VlanPortConfTable = _Gs2124VlanPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3)
)
if mibBuilder.loadTexts:
    gs2124VlanPortConfTable.setStatus("current")
_Gs2124VlanPortConfEntry_Object = MibTableRow
gs2124VlanPortConfEntry = _Gs2124VlanPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1)
)
gs2124VlanPortConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124VlanPortConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124VlanPortConfEntry.setStatus("current")


class _Gs2124VlanPortConfIndex_Type(Integer32):
    """Custom type gs2124VlanPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124VlanPortConfIndex_Type.__name__ = "Integer32"
_Gs2124VlanPortConfIndex_Object = MibTableColumn
gs2124VlanPortConfIndex = _Gs2124VlanPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 1),
    _Gs2124VlanPortConfIndex_Type()
)
gs2124VlanPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124VlanPortConfIndex.setStatus("current")


class _Gs2124VlanPortConfVlanAware_Type(Integer32):
    """Custom type gs2124VlanPortConfVlanAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124VlanPortConfVlanAware_Type.__name__ = "Integer32"
_Gs2124VlanPortConfVlanAware_Object = MibTableColumn
gs2124VlanPortConfVlanAware = _Gs2124VlanPortConfVlanAware_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 2),
    _Gs2124VlanPortConfVlanAware_Type()
)
gs2124VlanPortConfVlanAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfVlanAware.setStatus("current")


class _Gs2124VlanPortConfIngressFiltering_Type(Integer32):
    """Custom type gs2124VlanPortConfIngressFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124VlanPortConfIngressFiltering_Type.__name__ = "Integer32"
_Gs2124VlanPortConfIngressFiltering_Object = MibTableColumn
gs2124VlanPortConfIngressFiltering = _Gs2124VlanPortConfIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 3),
    _Gs2124VlanPortConfIngressFiltering_Type()
)
gs2124VlanPortConfIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfIngressFiltering.setStatus("current")


class _Gs2124VlanPortConfFrameType_Type(Integer32):
    """Custom type gs2124VlanPortConfFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124VlanPortConfFrameType_Type.__name__ = "Integer32"
_Gs2124VlanPortConfFrameType_Object = MibTableColumn
gs2124VlanPortConfFrameType = _Gs2124VlanPortConfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 4),
    _Gs2124VlanPortConfFrameType_Type()
)
gs2124VlanPortConfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfFrameType.setStatus("current")


class _Gs2124VlanPortConfPvid_Type(Integer32):
    """Custom type gs2124VlanPortConfPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124VlanPortConfPvid_Type.__name__ = "Integer32"
_Gs2124VlanPortConfPvid_Object = MibTableColumn
gs2124VlanPortConfPvid = _Gs2124VlanPortConfPvid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 5),
    _Gs2124VlanPortConfPvid_Type()
)
gs2124VlanPortConfPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfPvid.setStatus("current")


class _Gs2124VlanPortConfRole_Type(Integer32):
    """Custom type gs2124VlanPortConfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124VlanPortConfRole_Type.__name__ = "Integer32"
_Gs2124VlanPortConfRole_Object = MibTableColumn
gs2124VlanPortConfRole = _Gs2124VlanPortConfRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 6),
    _Gs2124VlanPortConfRole_Type()
)
gs2124VlanPortConfRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfRole.setStatus("current")


class _Gs2124VlanPortConfUntagVid_Type(Integer32):
    """Custom type gs2124VlanPortConfUntagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124VlanPortConfUntagVid_Type.__name__ = "Integer32"
_Gs2124VlanPortConfUntagVid_Object = MibTableColumn
gs2124VlanPortConfUntagVid = _Gs2124VlanPortConfUntagVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 7),
    _Gs2124VlanPortConfUntagVid_Type()
)
gs2124VlanPortConfUntagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfUntagVid.setStatus("current")


class _Gs2124VlanPortConfDoubleTag_Type(Integer32):
    """Custom type gs2124VlanPortConfDoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124VlanPortConfDoubleTag_Type.__name__ = "Integer32"
_Gs2124VlanPortConfDoubleTag_Object = MibTableColumn
gs2124VlanPortConfDoubleTag = _Gs2124VlanPortConfDoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 3, 1, 8),
    _Gs2124VlanPortConfDoubleTag_Type()
)
gs2124VlanPortConfDoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124VlanPortConfDoubleTag.setStatus("current")
_Gs2124PortBaseVlanGroup_ObjectIdentity = ObjectIdentity
gs2124PortBaseVlanGroup = _Gs2124PortBaseVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4)
)


class _Gs2124PortBaseVlanNumber_Type(Integer32):
    """Custom type gs2124PortBaseVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124PortBaseVlanNumber_Type.__name__ = "Integer32"
_Gs2124PortBaseVlanNumber_Object = MibScalar
gs2124PortBaseVlanNumber = _Gs2124PortBaseVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 1),
    _Gs2124PortBaseVlanNumber_Type()
)
gs2124PortBaseVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortBaseVlanNumber.setStatus("current")


class _Gs2124PortBaseVlanGroupEntryCreate_Type(Integer32):
    """Custom type gs2124PortBaseVlanGroupEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124PortBaseVlanGroupEntryCreate_Type.__name__ = "Integer32"
_Gs2124PortBaseVlanGroupEntryCreate_Object = MibScalar
gs2124PortBaseVlanGroupEntryCreate = _Gs2124PortBaseVlanGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 2),
    _Gs2124PortBaseVlanGroupEntryCreate_Type()
)
gs2124PortBaseVlanGroupEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupEntryCreate.setStatus("current")
_Gs2124PortBaseVlanGroupTable_Object = MibTable
gs2124PortBaseVlanGroupTable = _Gs2124PortBaseVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupTable.setStatus("current")
_Gs2124PortBaseVlanGroupEntry_Object = MibTableRow
gs2124PortBaseVlanGroupEntry = _Gs2124PortBaseVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 3, 1)
)
gs2124PortBaseVlanGroupEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124PortBaseVlanGroupIndex"),
)
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupEntry.setStatus("current")


class _Gs2124PortBaseVlanGroupIndex_Type(Integer32):
    """Custom type gs2124PortBaseVlanGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124PortBaseVlanGroupIndex_Type.__name__ = "Integer32"
_Gs2124PortBaseVlanGroupIndex_Object = MibTableColumn
gs2124PortBaseVlanGroupIndex = _Gs2124PortBaseVlanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 3, 1, 1),
    _Gs2124PortBaseVlanGroupIndex_Type()
)
gs2124PortBaseVlanGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupIndex.setStatus("current")
_Gs2124PortBaseVlanGroupName_Type = DisplayString
_Gs2124PortBaseVlanGroupName_Object = MibTableColumn
gs2124PortBaseVlanGroupName = _Gs2124PortBaseVlanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 3, 1, 2),
    _Gs2124PortBaseVlanGroupName_Type()
)
gs2124PortBaseVlanGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupName.setStatus("current")
_Gs2124PortBaseVlanGroupMembers_Type = DisplayString
_Gs2124PortBaseVlanGroupMembers_Object = MibTableColumn
gs2124PortBaseVlanGroupMembers = _Gs2124PortBaseVlanGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 3, 1, 3),
    _Gs2124PortBaseVlanGroupMembers_Type()
)
gs2124PortBaseVlanGroupMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupMembers.setStatus("current")


class _Gs2124PortBaseVlanGroupEntryAction_Type(Integer32):
    """Custom type gs2124PortBaseVlanGroupEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124PortBaseVlanGroupEntryAction_Type.__name__ = "Integer32"
_Gs2124PortBaseVlanGroupEntryAction_Object = MibTableColumn
gs2124PortBaseVlanGroupEntryAction = _Gs2124PortBaseVlanGroupEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 14, 4, 3, 1, 4),
    _Gs2124PortBaseVlanGroupEntryAction_Type()
)
gs2124PortBaseVlanGroupEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124PortBaseVlanGroupEntryAction.setStatus("current")
_Gs2124MacTableInfo_ObjectIdentity = ObjectIdentity
gs2124MacTableInfo = _Gs2124MacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15)
)
_Gs2124MacTableConf_ObjectIdentity = ObjectIdentity
gs2124MacTableConf = _Gs2124MacTableConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 1)
)


class _Gs2124MacAgeTime_Type(Integer32):
    """Custom type gs2124MacAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Gs2124MacAgeTime_Type.__name__ = "Integer32"
_Gs2124MacAgeTime_Object = MibScalar
gs2124MacAgeTime = _Gs2124MacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 1, 1),
    _Gs2124MacAgeTime_Type()
)
gs2124MacAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacAgeTime.setStatus("current")
_Gs2124MacTableLearningConfTable_Object = MibTable
gs2124MacTableLearningConfTable = _Gs2124MacTableLearningConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gs2124MacTableLearningConfTable.setStatus("current")
_Gs2124MacTableLearningConfEntry_Object = MibTableRow
gs2124MacTableLearningConfEntry = _Gs2124MacTableLearningConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 1, 2, 1)
)
gs2124MacTableLearningConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MacTableLearningConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124MacTableLearningConfEntry.setStatus("current")


class _Gs2124MacTableLearningConfIndex_Type(Integer32):
    """Custom type gs2124MacTableLearningConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124MacTableLearningConfIndex_Type.__name__ = "Integer32"
_Gs2124MacTableLearningConfIndex_Object = MibTableColumn
gs2124MacTableLearningConfIndex = _Gs2124MacTableLearningConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 1, 2, 1, 1),
    _Gs2124MacTableLearningConfIndex_Type()
)
gs2124MacTableLearningConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MacTableLearningConfIndex.setStatus("current")


class _Gs2124MacTableLearningConfstate_Type(Integer32):
    """Custom type gs2124MacTableLearningConfstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2124MacTableLearningConfstate_Type.__name__ = "Integer32"
_Gs2124MacTableLearningConfstate_Object = MibTableColumn
gs2124MacTableLearningConfstate = _Gs2124MacTableLearningConfstate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 1, 2, 1, 2),
    _Gs2124MacTableLearningConfstate_Type()
)
gs2124MacTableLearningConfstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableLearningConfstate.setStatus("current")
_Gs2124MacTableStaticFilter_ObjectIdentity = ObjectIdentity
gs2124MacTableStaticFilter = _Gs2124MacTableStaticFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2)
)


class _Gs2124MacTableStaticFilterNumber_Type(Integer32):
    """Custom type gs2124MacTableStaticFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Gs2124MacTableStaticFilterNumber_Type.__name__ = "Integer32"
_Gs2124MacTableStaticFilterNumber_Object = MibScalar
gs2124MacTableStaticFilterNumber = _Gs2124MacTableStaticFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 1),
    _Gs2124MacTableStaticFilterNumber_Type()
)
gs2124MacTableStaticFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterNumber.setStatus("current")


class _Gs2124MacTableStaticFilterEntryCreate_Type(Integer32):
    """Custom type gs2124MacTableStaticFilterEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Gs2124MacTableStaticFilterEntryCreate_Type.__name__ = "Integer32"
_Gs2124MacTableStaticFilterEntryCreate_Object = MibScalar
gs2124MacTableStaticFilterEntryCreate = _Gs2124MacTableStaticFilterEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 2),
    _Gs2124MacTableStaticFilterEntryCreate_Type()
)
gs2124MacTableStaticFilterEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterEntryCreate.setStatus("current")
_Gs2124MacTableStaticFilterTable_Object = MibTable
gs2124MacTableStaticFilterTable = _Gs2124MacTableStaticFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterTable.setStatus("current")
_Gs2124MacTableStaticFilterEntry_Object = MibTableRow
gs2124MacTableStaticFilterEntry = _Gs2124MacTableStaticFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3, 1)
)
gs2124MacTableStaticFilterEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MacTableStaticFilterIndex"),
)
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterEntry.setStatus("current")


class _Gs2124MacTableStaticFilterIndex_Type(Integer32):
    """Custom type gs2124MacTableStaticFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Gs2124MacTableStaticFilterIndex_Type.__name__ = "Integer32"
_Gs2124MacTableStaticFilterIndex_Object = MibTableColumn
gs2124MacTableStaticFilterIndex = _Gs2124MacTableStaticFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3, 1, 1),
    _Gs2124MacTableStaticFilterIndex_Type()
)
gs2124MacTableStaticFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterIndex.setStatus("current")
_Gs2124MacTableStaticFilterMac_Type = DisplayString
_Gs2124MacTableStaticFilterMac_Object = MibTableColumn
gs2124MacTableStaticFilterMac = _Gs2124MacTableStaticFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3, 1, 2),
    _Gs2124MacTableStaticFilterMac_Type()
)
gs2124MacTableStaticFilterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterMac.setStatus("current")


class _Gs2124MacTableStaticFilterVid_Type(Integer32):
    """Custom type gs2124MacTableStaticFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124MacTableStaticFilterVid_Type.__name__ = "Integer32"
_Gs2124MacTableStaticFilterVid_Object = MibTableColumn
gs2124MacTableStaticFilterVid = _Gs2124MacTableStaticFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3, 1, 3),
    _Gs2124MacTableStaticFilterVid_Type()
)
gs2124MacTableStaticFilterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterVid.setStatus("current")
_Gs2124MacTableStaticFilterAlias_Type = DisplayString
_Gs2124MacTableStaticFilterAlias_Object = MibTableColumn
gs2124MacTableStaticFilterAlias = _Gs2124MacTableStaticFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3, 1, 4),
    _Gs2124MacTableStaticFilterAlias_Type()
)
gs2124MacTableStaticFilterAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterAlias.setStatus("current")


class _Gs2124MacTableStaticFilterEntryAction_Type(Integer32):
    """Custom type gs2124MacTableStaticFilterEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124MacTableStaticFilterEntryAction_Type.__name__ = "Integer32"
_Gs2124MacTableStaticFilterEntryAction_Object = MibTableColumn
gs2124MacTableStaticFilterEntryAction = _Gs2124MacTableStaticFilterEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 2, 3, 1, 5),
    _Gs2124MacTableStaticFilterEntryAction_Type()
)
gs2124MacTableStaticFilterEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticFilterEntryAction.setStatus("current")
_Gs2124MacTableStaticForward_ObjectIdentity = ObjectIdentity
gs2124MacTableStaticForward = _Gs2124MacTableStaticForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3)
)


class _Gs2124MacTableStaticForwardNumber_Type(Integer32):
    """Custom type gs2124MacTableStaticForwardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Gs2124MacTableStaticForwardNumber_Type.__name__ = "Integer32"
_Gs2124MacTableStaticForwardNumber_Object = MibScalar
gs2124MacTableStaticForwardNumber = _Gs2124MacTableStaticForwardNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 1),
    _Gs2124MacTableStaticForwardNumber_Type()
)
gs2124MacTableStaticForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardNumber.setStatus("current")


class _Gs2124MacTableStaticForwardEntryCreate_Type(Integer32):
    """Custom type gs2124MacTableStaticForwardEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Gs2124MacTableStaticForwardEntryCreate_Type.__name__ = "Integer32"
_Gs2124MacTableStaticForwardEntryCreate_Object = MibScalar
gs2124MacTableStaticForwardEntryCreate = _Gs2124MacTableStaticForwardEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 2),
    _Gs2124MacTableStaticForwardEntryCreate_Type()
)
gs2124MacTableStaticForwardEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardEntryCreate.setStatus("current")
_Gs2124MacTableStaticForwardTable_Object = MibTable
gs2124MacTableStaticForwardTable = _Gs2124MacTableStaticForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3)
)
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardTable.setStatus("current")
_Gs2124MacTableStaticForwardEntry_Object = MibTableRow
gs2124MacTableStaticForwardEntry = _Gs2124MacTableStaticForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1)
)
gs2124MacTableStaticForwardEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MacTableStaticForwardIndex"),
)
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardEntry.setStatus("current")


class _Gs2124MacTableStaticForwardIndex_Type(Integer32):
    """Custom type gs2124MacTableStaticForwardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Gs2124MacTableStaticForwardIndex_Type.__name__ = "Integer32"
_Gs2124MacTableStaticForwardIndex_Object = MibTableColumn
gs2124MacTableStaticForwardIndex = _Gs2124MacTableStaticForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1, 1),
    _Gs2124MacTableStaticForwardIndex_Type()
)
gs2124MacTableStaticForwardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardIndex.setStatus("current")
_Gs2124MacTableStaticForwardMac_Type = DisplayString
_Gs2124MacTableStaticForwardMac_Object = MibTableColumn
gs2124MacTableStaticForwardMac = _Gs2124MacTableStaticForwardMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1, 2),
    _Gs2124MacTableStaticForwardMac_Type()
)
gs2124MacTableStaticForwardMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardMac.setStatus("current")


class _Gs2124MacTableStaticForwardPort_Type(Integer32):
    """Custom type gs2124MacTableStaticForwardPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124MacTableStaticForwardPort_Type.__name__ = "Integer32"
_Gs2124MacTableStaticForwardPort_Object = MibTableColumn
gs2124MacTableStaticForwardPort = _Gs2124MacTableStaticForwardPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1, 3),
    _Gs2124MacTableStaticForwardPort_Type()
)
gs2124MacTableStaticForwardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardPort.setStatus("current")


class _Gs2124MacTableStaticForwardVid_Type(Integer32):
    """Custom type gs2124MacTableStaticForwardVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124MacTableStaticForwardVid_Type.__name__ = "Integer32"
_Gs2124MacTableStaticForwardVid_Object = MibTableColumn
gs2124MacTableStaticForwardVid = _Gs2124MacTableStaticForwardVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1, 4),
    _Gs2124MacTableStaticForwardVid_Type()
)
gs2124MacTableStaticForwardVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardVid.setStatus("current")
_Gs2124MacTableStaticForwardAlias_Type = DisplayString
_Gs2124MacTableStaticForwardAlias_Object = MibTableColumn
gs2124MacTableStaticForwardAlias = _Gs2124MacTableStaticForwardAlias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1, 5),
    _Gs2124MacTableStaticForwardAlias_Type()
)
gs2124MacTableStaticForwardAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardAlias.setStatus("current")


class _Gs2124MacTableStaticForwardEntryAction_Type(Integer32):
    """Custom type gs2124MacTableStaticForwardEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124MacTableStaticForwardEntryAction_Type.__name__ = "Integer32"
_Gs2124MacTableStaticForwardEntryAction_Object = MibTableColumn
gs2124MacTableStaticForwardEntryAction = _Gs2124MacTableStaticForwardEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 3, 3, 1, 6),
    _Gs2124MacTableStaticForwardEntryAction_Type()
)
gs2124MacTableStaticForwardEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacTableStaticForwardEntryAction.setStatus("current")
_Gs2124MacAlias_ObjectIdentity = ObjectIdentity
gs2124MacAlias = _Gs2124MacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4)
)


class _Gs2124MacAliasNumber_Type(Integer32):
    """Custom type gs2124MacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Gs2124MacAliasNumber_Type.__name__ = "Integer32"
_Gs2124MacAliasNumber_Object = MibScalar
gs2124MacAliasNumber = _Gs2124MacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 1),
    _Gs2124MacAliasNumber_Type()
)
gs2124MacAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MacAliasNumber.setStatus("current")


class _Gs2124MacAliasEntryCreate_Type(Integer32):
    """Custom type gs2124MacAliasEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Gs2124MacAliasEntryCreate_Type.__name__ = "Integer32"
_Gs2124MacAliasEntryCreate_Object = MibScalar
gs2124MacAliasEntryCreate = _Gs2124MacAliasEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 2),
    _Gs2124MacAliasEntryCreate_Type()
)
gs2124MacAliasEntryCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MacAliasEntryCreate.setStatus("current")
_Gs2124MacAliasTable_Object = MibTable
gs2124MacAliasTable = _Gs2124MacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 3)
)
if mibBuilder.loadTexts:
    gs2124MacAliasTable.setStatus("current")
_Gs2124MacAliasEntry_Object = MibTableRow
gs2124MacAliasEntry = _Gs2124MacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 3, 1)
)
gs2124MacAliasEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MacAliasIndex"),
)
if mibBuilder.loadTexts:
    gs2124MacAliasEntry.setStatus("current")


class _Gs2124MacAliasIndex_Type(Integer32):
    """Custom type gs2124MacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2124MacAliasIndex_Type.__name__ = "Integer32"
_Gs2124MacAliasIndex_Object = MibTableColumn
gs2124MacAliasIndex = _Gs2124MacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 3, 1, 1),
    _Gs2124MacAliasIndex_Type()
)
gs2124MacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MacAliasIndex.setStatus("current")
_Gs2124AliasMac_Type = DisplayString
_Gs2124AliasMac_Object = MibTableColumn
gs2124AliasMac = _Gs2124AliasMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 3, 1, 2),
    _Gs2124AliasMac_Type()
)
gs2124AliasMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AliasMac.setStatus("current")
_Gs2124AliasName_Type = DisplayString
_Gs2124AliasName_Object = MibTableColumn
gs2124AliasName = _Gs2124AliasName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 3, 1, 3),
    _Gs2124AliasName_Type()
)
gs2124AliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AliasName.setStatus("current")


class _Gs2124MacAliasEntryAction_Type(Integer32):
    """Custom type gs2124MacAliasEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124MacAliasEntryAction_Type.__name__ = "Integer32"
_Gs2124MacAliasEntryAction_Object = MibTableColumn
gs2124MacAliasEntryAction = _Gs2124MacAliasEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 15, 4, 3, 1, 4),
    _Gs2124MacAliasEntryAction_Type()
)
gs2124MacAliasEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MacAliasEntryAction.setStatus("current")
_Gs2124GVRPInfo_ObjectIdentity = ObjectIdentity
gs2124GVRPInfo = _Gs2124GVRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16)
)
_Gs2124GvrpConf_ObjectIdentity = ObjectIdentity
gs2124GvrpConf = _Gs2124GvrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1)
)


class _Gs2124GvrpConfState_Type(Integer32):
    """Custom type gs2124GvrpConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124GvrpConfState_Type.__name__ = "Integer32"
_Gs2124GvrpConfState_Object = MibScalar
gs2124GvrpConfState = _Gs2124GvrpConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 1),
    _Gs2124GvrpConfState_Type()
)
gs2124GvrpConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfState.setStatus("current")
_Gs2124GvrpConfTable_Object = MibTable
gs2124GvrpConfTable = _Gs2124GvrpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    gs2124GvrpConfTable.setStatus("current")
_Gs2124GvrpConfEntry_Object = MibTableRow
gs2124GvrpConfEntry = _Gs2124GvrpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1)
)
gs2124GvrpConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124GvrpConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124GvrpConfEntry.setStatus("current")


class _Gs2124GvrpConfIndex_Type(Integer32):
    """Custom type gs2124GvrpConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124GvrpConfIndex_Type.__name__ = "Integer32"
_Gs2124GvrpConfIndex_Object = MibTableColumn
gs2124GvrpConfIndex = _Gs2124GvrpConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 1),
    _Gs2124GvrpConfIndex_Type()
)
gs2124GvrpConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124GvrpConfIndex.setStatus("current")


class _Gs2124GvrpConfJoinTime_Type(Integer32):
    """Custom type gs2124GvrpConfJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Gs2124GvrpConfJoinTime_Type.__name__ = "Integer32"
_Gs2124GvrpConfJoinTime_Object = MibTableColumn
gs2124GvrpConfJoinTime = _Gs2124GvrpConfJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 2),
    _Gs2124GvrpConfJoinTime_Type()
)
gs2124GvrpConfJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfJoinTime.setStatus("current")


class _Gs2124GvrpConfLeaveTime_Type(Integer32):
    """Custom type gs2124GvrpConfLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Gs2124GvrpConfLeaveTime_Type.__name__ = "Integer32"
_Gs2124GvrpConfLeaveTime_Object = MibTableColumn
gs2124GvrpConfLeaveTime = _Gs2124GvrpConfLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 3),
    _Gs2124GvrpConfLeaveTime_Type()
)
gs2124GvrpConfLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfLeaveTime.setStatus("current")


class _Gs2124GvrpConfLeaveAllTime_Type(Integer32):
    """Custom type gs2124GvrpConfLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_Gs2124GvrpConfLeaveAllTime_Type.__name__ = "Integer32"
_Gs2124GvrpConfLeaveAllTime_Object = MibTableColumn
gs2124GvrpConfLeaveAllTime = _Gs2124GvrpConfLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 4),
    _Gs2124GvrpConfLeaveAllTime_Type()
)
gs2124GvrpConfLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfLeaveAllTime.setStatus("current")


class _Gs2124GvrpConfDefaultAppMode_Type(Integer32):
    """Custom type gs2124GvrpConfDefaultAppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124GvrpConfDefaultAppMode_Type.__name__ = "Integer32"
_Gs2124GvrpConfDefaultAppMode_Object = MibTableColumn
gs2124GvrpConfDefaultAppMode = _Gs2124GvrpConfDefaultAppMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 5),
    _Gs2124GvrpConfDefaultAppMode_Type()
)
gs2124GvrpConfDefaultAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfDefaultAppMode.setStatus("current")


class _Gs2124GvrpConfDefaultRegMode_Type(Integer32):
    """Custom type gs2124GvrpConfDefaultRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2124GvrpConfDefaultRegMode_Type.__name__ = "Integer32"
_Gs2124GvrpConfDefaultRegMode_Object = MibTableColumn
gs2124GvrpConfDefaultRegMode = _Gs2124GvrpConfDefaultRegMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 6),
    _Gs2124GvrpConfDefaultRegMode_Type()
)
gs2124GvrpConfDefaultRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfDefaultRegMode.setStatus("current")


class _Gs2124GvrpConfRestrictedMode_Type(Integer32):
    """Custom type gs2124GvrpConfRestrictedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124GvrpConfRestrictedMode_Type.__name__ = "Integer32"
_Gs2124GvrpConfRestrictedMode_Object = MibTableColumn
gs2124GvrpConfRestrictedMode = _Gs2124GvrpConfRestrictedMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 1, 2, 1, 7),
    _Gs2124GvrpConfRestrictedMode_Type()
)
gs2124GvrpConfRestrictedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpConfRestrictedMode.setStatus("current")
_Gs2124GvrpCounter_ObjectIdentity = ObjectIdentity
gs2124GvrpCounter = _Gs2124GvrpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2)
)
_Gs2124GvrpCounterTable_Object = MibTable
gs2124GvrpCounterTable = _Gs2124GvrpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    gs2124GvrpCounterTable.setStatus("current")
_Gs2124GvrpCounterEntry_Object = MibTableRow
gs2124GvrpCounterEntry = _Gs2124GvrpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1)
)
gs2124GvrpCounterEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124GvrpCounterIndex"),
)
if mibBuilder.loadTexts:
    gs2124GvrpCounterEntry.setStatus("current")


class _Gs2124GvrpCounterIndex_Type(Integer32):
    """Custom type gs2124GvrpCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124GvrpCounterIndex_Type.__name__ = "Integer32"
_Gs2124GvrpCounterIndex_Object = MibTableColumn
gs2124GvrpCounterIndex = _Gs2124GvrpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 1),
    _Gs2124GvrpCounterIndex_Type()
)
gs2124GvrpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124GvrpCounterIndex.setStatus("current")
_Gs2124GvrpCounterRxTotalGvrpPkts_Type = Counter32
_Gs2124GvrpCounterRxTotalGvrpPkts_Object = MibTableColumn
gs2124GvrpCounterRxTotalGvrpPkts = _Gs2124GvrpCounterRxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 2),
    _Gs2124GvrpCounterRxTotalGvrpPkts_Type()
)
gs2124GvrpCounterRxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxTotalGvrpPkts.setStatus("current")
_Gs2124GvrpCounterRxInvalidGvrpPkts_Type = Counter32
_Gs2124GvrpCounterRxInvalidGvrpPkts_Object = MibTableColumn
gs2124GvrpCounterRxInvalidGvrpPkts = _Gs2124GvrpCounterRxInvalidGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 3),
    _Gs2124GvrpCounterRxInvalidGvrpPkts_Type()
)
gs2124GvrpCounterRxInvalidGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxInvalidGvrpPkts.setStatus("current")
_Gs2124GvrpCounterRxLeaveAllMsg_Type = Counter32
_Gs2124GvrpCounterRxLeaveAllMsg_Object = MibTableColumn
gs2124GvrpCounterRxLeaveAllMsg = _Gs2124GvrpCounterRxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 4),
    _Gs2124GvrpCounterRxLeaveAllMsg_Type()
)
gs2124GvrpCounterRxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxLeaveAllMsg.setStatus("current")
_Gs2124GvrpCounterRxJoinEmptyMsg_Type = Counter32
_Gs2124GvrpCounterRxJoinEmptyMsg_Object = MibTableColumn
gs2124GvrpCounterRxJoinEmptyMsg = _Gs2124GvrpCounterRxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 5),
    _Gs2124GvrpCounterRxJoinEmptyMsg_Type()
)
gs2124GvrpCounterRxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxJoinEmptyMsg.setStatus("current")
_Gs2124GvrpCounterRxJoinInMsg_Type = Counter32
_Gs2124GvrpCounterRxJoinInMsg_Object = MibTableColumn
gs2124GvrpCounterRxJoinInMsg = _Gs2124GvrpCounterRxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 6),
    _Gs2124GvrpCounterRxJoinInMsg_Type()
)
gs2124GvrpCounterRxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxJoinInMsg.setStatus("current")
_Gs2124GvrpCounterRxLeaveEmptyMsg_Type = Counter32
_Gs2124GvrpCounterRxLeaveEmptyMsg_Object = MibTableColumn
gs2124GvrpCounterRxLeaveEmptyMsg = _Gs2124GvrpCounterRxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 7),
    _Gs2124GvrpCounterRxLeaveEmptyMsg_Type()
)
gs2124GvrpCounterRxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxLeaveEmptyMsg.setStatus("current")
_Gs2124GvrpCounterRxEmptyMsg_Type = Counter32
_Gs2124GvrpCounterRxEmptyMsg_Object = MibTableColumn
gs2124GvrpCounterRxEmptyMsg = _Gs2124GvrpCounterRxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 8),
    _Gs2124GvrpCounterRxEmptyMsg_Type()
)
gs2124GvrpCounterRxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterRxEmptyMsg.setStatus("current")
_Gs2124GvrpCounterTxTotalGvrpPkts_Type = Counter32
_Gs2124GvrpCounterTxTotalGvrpPkts_Object = MibTableColumn
gs2124GvrpCounterTxTotalGvrpPkts = _Gs2124GvrpCounterTxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 9),
    _Gs2124GvrpCounterTxTotalGvrpPkts_Type()
)
gs2124GvrpCounterTxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterTxTotalGvrpPkts.setStatus("current")
_Gs2124GvrpCounterTxLeaveAllMsg_Type = Counter32
_Gs2124GvrpCounterTxLeaveAllMsg_Object = MibTableColumn
gs2124GvrpCounterTxLeaveAllMsg = _Gs2124GvrpCounterTxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 10),
    _Gs2124GvrpCounterTxLeaveAllMsg_Type()
)
gs2124GvrpCounterTxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterTxLeaveAllMsg.setStatus("current")
_Gs2124GvrpCounterTxJoinEmptyMsg_Type = Counter32
_Gs2124GvrpCounterTxJoinEmptyMsg_Object = MibTableColumn
gs2124GvrpCounterTxJoinEmptyMsg = _Gs2124GvrpCounterTxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 11),
    _Gs2124GvrpCounterTxJoinEmptyMsg_Type()
)
gs2124GvrpCounterTxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterTxJoinEmptyMsg.setStatus("current")
_Gs2124GvrpCounterTxJoinInMsg_Type = Counter32
_Gs2124GvrpCounterTxJoinInMsg_Object = MibTableColumn
gs2124GvrpCounterTxJoinInMsg = _Gs2124GvrpCounterTxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 12),
    _Gs2124GvrpCounterTxJoinInMsg_Type()
)
gs2124GvrpCounterTxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterTxJoinInMsg.setStatus("current")
_Gs2124GvrpCounterTxLeaveEmptyMsg_Type = Counter32
_Gs2124GvrpCounterTxLeaveEmptyMsg_Object = MibTableColumn
gs2124GvrpCounterTxLeaveEmptyMsg = _Gs2124GvrpCounterTxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 13),
    _Gs2124GvrpCounterTxLeaveEmptyMsg_Type()
)
gs2124GvrpCounterTxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterTxLeaveEmptyMsg.setStatus("current")
_Gs2124GvrpCounterTxEmptyMsg_Type = Counter32
_Gs2124GvrpCounterTxEmptyMsg_Object = MibTableColumn
gs2124GvrpCounterTxEmptyMsg = _Gs2124GvrpCounterTxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 2, 1, 1, 14),
    _Gs2124GvrpCounterTxEmptyMsg_Type()
)
gs2124GvrpCounterTxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpCounterTxEmptyMsg.setStatus("current")
_Gs2124GvrpGroup_ObjectIdentity = ObjectIdentity
gs2124GvrpGroup = _Gs2124GvrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3)
)


class _Gs2124GvrpGroupNumber_Type(Integer32):
    """Custom type gs2124GvrpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124GvrpGroupNumber_Type.__name__ = "Integer32"
_Gs2124GvrpGroupNumber_Object = MibScalar
gs2124GvrpGroupNumber = _Gs2124GvrpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 1),
    _Gs2124GvrpGroupNumber_Type()
)
gs2124GvrpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpGroupNumber.setStatus("current")
_Gs2124GvrpGroupTable_Object = MibTable
gs2124GvrpGroupTable = _Gs2124GvrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 2)
)
if mibBuilder.loadTexts:
    gs2124GvrpGroupTable.setStatus("current")
_Gs2124GvrpGroupEntry_Object = MibTableRow
gs2124GvrpGroupEntry = _Gs2124GvrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 2, 1)
)
gs2124GvrpGroupEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124GvrpGroupId"),
)
if mibBuilder.loadTexts:
    gs2124GvrpGroupEntry.setStatus("current")


class _Gs2124GvrpGroupId_Type(Integer32):
    """Custom type gs2124GvrpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124GvrpGroupId_Type.__name__ = "Integer32"
_Gs2124GvrpGroupId_Object = MibTableColumn
gs2124GvrpGroupId = _Gs2124GvrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 2, 1, 1),
    _Gs2124GvrpGroupId_Type()
)
gs2124GvrpGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpGroupId.setStatus("current")


class _Gs2124GvrpGroupVid_Type(Integer32):
    """Custom type gs2124GvrpGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124GvrpGroupVid_Type.__name__ = "Integer32"
_Gs2124GvrpGroupVid_Object = MibTableColumn
gs2124GvrpGroupVid = _Gs2124GvrpGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 2, 1, 2),
    _Gs2124GvrpGroupVid_Type()
)
gs2124GvrpGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpGroupVid.setStatus("current")
_Gs2124GvrpGroupMemberPort_Type = DisplayString
_Gs2124GvrpGroupMemberPort_Object = MibTableColumn
gs2124GvrpGroupMemberPort = _Gs2124GvrpGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 2, 1, 3),
    _Gs2124GvrpGroupMemberPort_Type()
)
gs2124GvrpGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpGroupMemberPort.setStatus("current")
_Gs2124GvrpGroupAdministrativeCtrlTable_Object = MibTable
gs2124GvrpGroupAdministrativeCtrlTable = _Gs2124GvrpGroupAdministrativeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 3)
)
if mibBuilder.loadTexts:
    gs2124GvrpGroupAdministrativeCtrlTable.setStatus("current")
_Gs2124GvrpGroupAdministrativeCtrlEntry_Object = MibTableRow
gs2124GvrpGroupAdministrativeCtrlEntry = _Gs2124GvrpGroupAdministrativeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 3, 1)
)
gs2124GvrpGroupAdministrativeCtrlEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124GvrpGroupAdministrativeCtrlVid"),
    (0, "LANCOM-GS-2124-MIB", "gs2124GvrpGroupAdministrativeCtrlPort"),
)
if mibBuilder.loadTexts:
    gs2124GvrpGroupAdministrativeCtrlEntry.setStatus("current")


class _Gs2124GvrpGroupAdministrativeCtrlVid_Type(Integer32):
    """Custom type gs2124GvrpGroupAdministrativeCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124GvrpGroupAdministrativeCtrlVid_Type.__name__ = "Integer32"
_Gs2124GvrpGroupAdministrativeCtrlVid_Object = MibTableColumn
gs2124GvrpGroupAdministrativeCtrlVid = _Gs2124GvrpGroupAdministrativeCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 3, 1, 1),
    _Gs2124GvrpGroupAdministrativeCtrlVid_Type()
)
gs2124GvrpGroupAdministrativeCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpGroupAdministrativeCtrlVid.setStatus("current")


class _Gs2124GvrpGroupAdministrativeCtrlPort_Type(Integer32):
    """Custom type gs2124GvrpGroupAdministrativeCtrlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124GvrpGroupAdministrativeCtrlPort_Type.__name__ = "Integer32"
_Gs2124GvrpGroupAdministrativeCtrlPort_Object = MibTableColumn
gs2124GvrpGroupAdministrativeCtrlPort = _Gs2124GvrpGroupAdministrativeCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 3, 1, 2),
    _Gs2124GvrpGroupAdministrativeCtrlPort_Type()
)
gs2124GvrpGroupAdministrativeCtrlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124GvrpGroupAdministrativeCtrlPort.setStatus("current")


class _Gs2124GvrpGroupAdministrativeCtrlApp_Type(Integer32):
    """Custom type gs2124GvrpGroupAdministrativeCtrlApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124GvrpGroupAdministrativeCtrlApp_Type.__name__ = "Integer32"
_Gs2124GvrpGroupAdministrativeCtrlApp_Object = MibTableColumn
gs2124GvrpGroupAdministrativeCtrlApp = _Gs2124GvrpGroupAdministrativeCtrlApp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 3, 1, 3),
    _Gs2124GvrpGroupAdministrativeCtrlApp_Type()
)
gs2124GvrpGroupAdministrativeCtrlApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpGroupAdministrativeCtrlApp.setStatus("current")


class _Gs2124GvrpGroupAdministrativeCtrlReg_Type(Integer32):
    """Custom type gs2124GvrpGroupAdministrativeCtrlReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124GvrpGroupAdministrativeCtrlReg_Type.__name__ = "Integer32"
_Gs2124GvrpGroupAdministrativeCtrlReg_Object = MibTableColumn
gs2124GvrpGroupAdministrativeCtrlReg = _Gs2124GvrpGroupAdministrativeCtrlReg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 16, 3, 3, 1, 4),
    _Gs2124GvrpGroupAdministrativeCtrlReg_Type()
)
gs2124GvrpGroupAdministrativeCtrlReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124GvrpGroupAdministrativeCtrlReg.setStatus("current")
_Gs2124QosInfo_ObjectIdentity = ObjectIdentity
gs2124QosInfo = _Gs2124QosInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17)
)
_Gs2124QosPortConf_ObjectIdentity = ObjectIdentity
gs2124QosPortConf = _Gs2124QosPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1)
)


class _Gs2124QosNumOfClasses_Type(Integer32):
    """Custom type gs2124QosNumOfClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_Gs2124QosNumOfClasses_Type.__name__ = "Integer32"
_Gs2124QosNumOfClasses_Object = MibScalar
gs2124QosNumOfClasses = _Gs2124QosNumOfClasses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 1),
    _Gs2124QosNumOfClasses_Type()
)
gs2124QosNumOfClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosNumOfClasses.setStatus("current")
_Gs2124QosPortConfTable_Object = MibTable
gs2124QosPortConfTable = _Gs2124QosPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2)
)
if mibBuilder.loadTexts:
    gs2124QosPortConfTable.setStatus("current")
_Gs2124QosPortConfEntry_Object = MibTableRow
gs2124QosPortConfEntry = _Gs2124QosPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1)
)
gs2124QosPortConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124QosPortConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124QosPortConfEntry.setStatus("current")


class _Gs2124QosPortConfIndex_Type(Integer32):
    """Custom type gs2124QosPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosPortConfIndex_Type.__name__ = "Integer32"
_Gs2124QosPortConfIndex_Object = MibTableColumn
gs2124QosPortConfIndex = _Gs2124QosPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 1),
    _Gs2124QosPortConfIndex_Type()
)
gs2124QosPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124QosPortConfIndex.setStatus("current")


class _Gs2124QosPortConfDefaultClasses_Type(Integer32):
    """Custom type gs2124QosPortConfDefaultClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2124QosPortConfDefaultClasses_Type.__name__ = "Integer32"
_Gs2124QosPortConfDefaultClasses_Object = MibTableColumn
gs2124QosPortConfDefaultClasses = _Gs2124QosPortConfDefaultClasses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 2),
    _Gs2124QosPortConfDefaultClasses_Type()
)
gs2124QosPortConfDefaultClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfDefaultClasses.setStatus("current")


class _Gs2124QosPortConfQCL_Type(Integer32):
    """Custom type gs2124QosPortConfQCL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosPortConfQCL_Type.__name__ = "Integer32"
_Gs2124QosPortConfQCL_Object = MibTableColumn
gs2124QosPortConfQCL = _Gs2124QosPortConfQCL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 3),
    _Gs2124QosPortConfQCL_Type()
)
gs2124QosPortConfQCL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfQCL.setStatus("current")


class _Gs2124QosPortConfUserPriority_Type(Integer32):
    """Custom type gs2124QosPortConfUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Gs2124QosPortConfUserPriority_Type.__name__ = "Integer32"
_Gs2124QosPortConfUserPriority_Object = MibTableColumn
gs2124QosPortConfUserPriority = _Gs2124QosPortConfUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 4),
    _Gs2124QosPortConfUserPriority_Type()
)
gs2124QosPortConfUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfUserPriority.setStatus("current")


class _Gs2124QosPortConfQueuingMode_Type(Integer32):
    """Custom type gs2124QosPortConfQueuingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124QosPortConfQueuingMode_Type.__name__ = "Integer32"
_Gs2124QosPortConfQueuingMode_Object = MibTableColumn
gs2124QosPortConfQueuingMode = _Gs2124QosPortConfQueuingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 5),
    _Gs2124QosPortConfQueuingMode_Type()
)
gs2124QosPortConfQueuingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfQueuingMode.setStatus("current")


class _Gs2124QosPortConfQueueWeightedLow_Type(Integer32):
    """Custom type gs2124QosPortConfQueueWeightedLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Gs2124QosPortConfQueueWeightedLow_Type.__name__ = "Integer32"
_Gs2124QosPortConfQueueWeightedLow_Object = MibTableColumn
gs2124QosPortConfQueueWeightedLow = _Gs2124QosPortConfQueueWeightedLow_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 6),
    _Gs2124QosPortConfQueueWeightedLow_Type()
)
gs2124QosPortConfQueueWeightedLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfQueueWeightedLow.setStatus("current")


class _Gs2124QosPortConfQueueWeightedNormal_Type(Integer32):
    """Custom type gs2124QosPortConfQueueWeightedNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Gs2124QosPortConfQueueWeightedNormal_Type.__name__ = "Integer32"
_Gs2124QosPortConfQueueWeightedNormal_Object = MibTableColumn
gs2124QosPortConfQueueWeightedNormal = _Gs2124QosPortConfQueueWeightedNormal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 7),
    _Gs2124QosPortConfQueueWeightedNormal_Type()
)
gs2124QosPortConfQueueWeightedNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfQueueWeightedNormal.setStatus("current")


class _Gs2124QosPortConfQueueWeightedMedium_Type(Integer32):
    """Custom type gs2124QosPortConfQueueWeightedMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Gs2124QosPortConfQueueWeightedMedium_Type.__name__ = "Integer32"
_Gs2124QosPortConfQueueWeightedMedium_Object = MibTableColumn
gs2124QosPortConfQueueWeightedMedium = _Gs2124QosPortConfQueueWeightedMedium_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 8),
    _Gs2124QosPortConfQueueWeightedMedium_Type()
)
gs2124QosPortConfQueueWeightedMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfQueueWeightedMedium.setStatus("current")


class _Gs2124QosPortConfQueueWeightedHigh_Type(Integer32):
    """Custom type gs2124QosPortConfQueueWeightedHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Gs2124QosPortConfQueueWeightedHigh_Type.__name__ = "Integer32"
_Gs2124QosPortConfQueueWeightedHigh_Object = MibTableColumn
gs2124QosPortConfQueueWeightedHigh = _Gs2124QosPortConfQueueWeightedHigh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 1, 2, 1, 9),
    _Gs2124QosPortConfQueueWeightedHigh_Type()
)
gs2124QosPortConfQueueWeightedHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosPortConfQueueWeightedHigh.setStatus("current")
_Gs2124QosRateLimiters_ObjectIdentity = ObjectIdentity
gs2124QosRateLimiters = _Gs2124QosRateLimiters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3)
)
_Gs2124QosRateLimitersTable_Object = MibTable
gs2124QosRateLimitersTable = _Gs2124QosRateLimitersTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    gs2124QosRateLimitersTable.setStatus("current")
_Gs2124QosRateLimitersEntry_Object = MibTableRow
gs2124QosRateLimitersEntry = _Gs2124QosRateLimitersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1, 1)
)
gs2124QosRateLimitersEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124QosRateLimitersIndex"),
)
if mibBuilder.loadTexts:
    gs2124QosRateLimitersEntry.setStatus("current")


class _Gs2124QosRateLimitersIndex_Type(Integer32):
    """Custom type gs2124QosRateLimitersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosRateLimitersIndex_Type.__name__ = "Integer32"
_Gs2124QosRateLimitersIndex_Object = MibTableColumn
gs2124QosRateLimitersIndex = _Gs2124QosRateLimitersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1, 1, 1),
    _Gs2124QosRateLimitersIndex_Type()
)
gs2124QosRateLimitersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124QosRateLimitersIndex.setStatus("current")


class _Gs2124QosRateLimitersPolicer_Type(Integer32):
    """Custom type gs2124QosRateLimitersPolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124QosRateLimitersPolicer_Type.__name__ = "Integer32"
_Gs2124QosRateLimitersPolicer_Object = MibTableColumn
gs2124QosRateLimitersPolicer = _Gs2124QosRateLimitersPolicer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1, 1, 2),
    _Gs2124QosRateLimitersPolicer_Type()
)
gs2124QosRateLimitersPolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosRateLimitersPolicer.setStatus("current")


class _Gs2124QosRateLimitersPolicerRate_Type(Integer32):
    """Custom type gs2124QosRateLimitersPolicerRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Gs2124QosRateLimitersPolicerRate_Type.__name__ = "Integer32"
_Gs2124QosRateLimitersPolicerRate_Object = MibTableColumn
gs2124QosRateLimitersPolicerRate = _Gs2124QosRateLimitersPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1, 1, 3),
    _Gs2124QosRateLimitersPolicerRate_Type()
)
gs2124QosRateLimitersPolicerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosRateLimitersPolicerRate.setStatus("current")


class _Gs2124QosRateLimitersShaper_Type(Integer32):
    """Custom type gs2124QosRateLimitersShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124QosRateLimitersShaper_Type.__name__ = "Integer32"
_Gs2124QosRateLimitersShaper_Object = MibTableColumn
gs2124QosRateLimitersShaper = _Gs2124QosRateLimitersShaper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1, 1, 4),
    _Gs2124QosRateLimitersShaper_Type()
)
gs2124QosRateLimitersShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosRateLimitersShaper.setStatus("current")


class _Gs2124QosRateLimitersShaperRate_Type(Integer32):
    """Custom type gs2124QosRateLimitersShaperRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Gs2124QosRateLimitersShaperRate_Type.__name__ = "Integer32"
_Gs2124QosRateLimitersShaperRate_Object = MibTableColumn
gs2124QosRateLimitersShaperRate = _Gs2124QosRateLimitersShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 3, 1, 1, 5),
    _Gs2124QosRateLimitersShaperRate_Type()
)
gs2124QosRateLimitersShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosRateLimitersShaperRate.setStatus("current")
_Gs2124QosStormCtrl_ObjectIdentity = ObjectIdentity
gs2124QosStormCtrl = _Gs2124QosStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4)
)


class _Gs2124QosStromCtrlFloodedUnicastStatus_Type(Integer32):
    """Custom type gs2124QosStromCtrlFloodedUnicastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124QosStromCtrlFloodedUnicastStatus_Type.__name__ = "Integer32"
_Gs2124QosStromCtrlFloodedUnicastStatus_Object = MibScalar
gs2124QosStromCtrlFloodedUnicastStatus = _Gs2124QosStromCtrlFloodedUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4, 1),
    _Gs2124QosStromCtrlFloodedUnicastStatus_Type()
)
gs2124QosStromCtrlFloodedUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosStromCtrlFloodedUnicastStatus.setStatus("current")
_Gs2124QosStromCtrlFloodedUnicastRate_Type = DisplayString
_Gs2124QosStromCtrlFloodedUnicastRate_Object = MibScalar
gs2124QosStromCtrlFloodedUnicastRate = _Gs2124QosStromCtrlFloodedUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4, 2),
    _Gs2124QosStromCtrlFloodedUnicastRate_Type()
)
gs2124QosStromCtrlFloodedUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosStromCtrlFloodedUnicastRate.setStatus("current")


class _Gs2124QosStromCtrlMulticastStatus_Type(Integer32):
    """Custom type gs2124QosStromCtrlMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124QosStromCtrlMulticastStatus_Type.__name__ = "Integer32"
_Gs2124QosStromCtrlMulticastStatus_Object = MibScalar
gs2124QosStromCtrlMulticastStatus = _Gs2124QosStromCtrlMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4, 3),
    _Gs2124QosStromCtrlMulticastStatus_Type()
)
gs2124QosStromCtrlMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosStromCtrlMulticastStatus.setStatus("current")
_Gs2124QosStromCtrlMulticastRate_Type = DisplayString
_Gs2124QosStromCtrlMulticastRate_Object = MibScalar
gs2124QosStromCtrlMulticastRate = _Gs2124QosStromCtrlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4, 4),
    _Gs2124QosStromCtrlMulticastRate_Type()
)
gs2124QosStromCtrlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosStromCtrlMulticastRate.setStatus("current")


class _Gs2124QosStromCtrlBroadcastStatus_Type(Integer32):
    """Custom type gs2124QosStromCtrlBroadcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124QosStromCtrlBroadcastStatus_Type.__name__ = "Integer32"
_Gs2124QosStromCtrlBroadcastStatus_Object = MibScalar
gs2124QosStromCtrlBroadcastStatus = _Gs2124QosStromCtrlBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4, 5),
    _Gs2124QosStromCtrlBroadcastStatus_Type()
)
gs2124QosStromCtrlBroadcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosStromCtrlBroadcastStatus.setStatus("current")
_Gs2124QosStromCtrlBroadcastRate_Type = DisplayString
_Gs2124QosStromCtrlBroadcastRate_Object = MibScalar
gs2124QosStromCtrlBroadcastRate = _Gs2124QosStromCtrlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 4, 6),
    _Gs2124QosStromCtrlBroadcastRate_Type()
)
gs2124QosStromCtrlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosStromCtrlBroadcastRate.setStatus("current")
_Gs2124QosQCL_ObjectIdentity = ObjectIdentity
gs2124QosQCL = _Gs2124QosQCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5)
)


class _Gs2124QosQclCreate_Type(Integer32):
    """Custom type gs2124QosQclCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosQclCreate_Type.__name__ = "Integer32"
_Gs2124QosQclCreate_Object = MibScalar
gs2124QosQclCreate = _Gs2124QosQclCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 1),
    _Gs2124QosQclCreate_Type()
)
gs2124QosQclCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclCreate.setStatus("current")
_Gs2124QosQclTable_Object = MibTable
gs2124QosQclTable = _Gs2124QosQclTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2)
)
if mibBuilder.loadTexts:
    gs2124QosQclTable.setStatus("current")
_Gs2124QosQclEntry_Object = MibTableRow
gs2124QosQclEntry = _Gs2124QosQclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1)
)
gs2124QosQclEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124QosQclNo"),
    (0, "LANCOM-GS-2124-MIB", "gs2124QosQclQceListNo"),
)
if mibBuilder.loadTexts:
    gs2124QosQclEntry.setStatus("current")


class _Gs2124QosQclNo_Type(Integer32):
    """Custom type gs2124QosQclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosQclNo_Type.__name__ = "Integer32"
_Gs2124QosQclNo_Object = MibTableColumn
gs2124QosQclNo = _Gs2124QosQclNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 1),
    _Gs2124QosQclNo_Type()
)
gs2124QosQclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124QosQclNo.setStatus("current")


class _Gs2124QosQclQceListNo_Type(Integer32):
    """Custom type gs2124QosQclQceListNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosQclQceListNo_Type.__name__ = "Integer32"
_Gs2124QosQclQceListNo_Object = MibTableColumn
gs2124QosQclQceListNo = _Gs2124QosQclQceListNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 2),
    _Gs2124QosQclQceListNo_Type()
)
gs2124QosQclQceListNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124QosQclQceListNo.setStatus("current")


class _Gs2124QosQclQceMoveTo_Type(Integer32):
    """Custom type gs2124QosQclQceMoveTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124QosQclQceMoveTo_Type.__name__ = "Integer32"
_Gs2124QosQclQceMoveTo_Object = MibTableColumn
gs2124QosQclQceMoveTo = _Gs2124QosQclQceMoveTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 3),
    _Gs2124QosQclQceMoveTo_Type()
)
gs2124QosQclQceMoveTo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124QosQclQceMoveTo.setStatus("current")


class _Gs2124QosQclQceType_Type(Integer32):
    """Custom type gs2124QosQclQceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Gs2124QosQclQceType_Type.__name__ = "Integer32"
_Gs2124QosQclQceType_Object = MibTableColumn
gs2124QosQclQceType = _Gs2124QosQclQceType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 4),
    _Gs2124QosQclQceType_Type()
)
gs2124QosQclQceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQceType.setStatus("current")
_Gs2124QosQclQceValue_Type = DisplayString
_Gs2124QosQclQceValue_Object = MibTableColumn
gs2124QosQclQceValue = _Gs2124QosQclQceValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 5),
    _Gs2124QosQclQceValue_Type()
)
gs2124QosQclQceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQceValue.setStatus("current")
_Gs2124QosQclQceTrafficClass_Type = DisplayString
_Gs2124QosQclQceTrafficClass_Object = MibTableColumn
gs2124QosQclQceTrafficClass = _Gs2124QosQclQceTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 6),
    _Gs2124QosQclQceTrafficClass_Type()
)
gs2124QosQclQceTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQceTrafficClass.setStatus("current")
_Gs2124QosQclQcePriority0Class_Type = DisplayString
_Gs2124QosQclQcePriority0Class_Object = MibTableColumn
gs2124QosQclQcePriority0Class = _Gs2124QosQclQcePriority0Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 7),
    _Gs2124QosQclQcePriority0Class_Type()
)
gs2124QosQclQcePriority0Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority0Class.setStatus("current")
_Gs2124QosQclQcePriority1Class_Type = DisplayString
_Gs2124QosQclQcePriority1Class_Object = MibTableColumn
gs2124QosQclQcePriority1Class = _Gs2124QosQclQcePriority1Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 8),
    _Gs2124QosQclQcePriority1Class_Type()
)
gs2124QosQclQcePriority1Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority1Class.setStatus("current")
_Gs2124QosQclQcePriority2Class_Type = DisplayString
_Gs2124QosQclQcePriority2Class_Object = MibTableColumn
gs2124QosQclQcePriority2Class = _Gs2124QosQclQcePriority2Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 9),
    _Gs2124QosQclQcePriority2Class_Type()
)
gs2124QosQclQcePriority2Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority2Class.setStatus("current")
_Gs2124QosQclQcePriority3Class_Type = DisplayString
_Gs2124QosQclQcePriority3Class_Object = MibTableColumn
gs2124QosQclQcePriority3Class = _Gs2124QosQclQcePriority3Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 10),
    _Gs2124QosQclQcePriority3Class_Type()
)
gs2124QosQclQcePriority3Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority3Class.setStatus("current")
_Gs2124QosQclQcePriority4Class_Type = DisplayString
_Gs2124QosQclQcePriority4Class_Object = MibTableColumn
gs2124QosQclQcePriority4Class = _Gs2124QosQclQcePriority4Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 11),
    _Gs2124QosQclQcePriority4Class_Type()
)
gs2124QosQclQcePriority4Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority4Class.setStatus("current")
_Gs2124QosQclQcePriority5Class_Type = DisplayString
_Gs2124QosQclQcePriority5Class_Object = MibTableColumn
gs2124QosQclQcePriority5Class = _Gs2124QosQclQcePriority5Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 12),
    _Gs2124QosQclQcePriority5Class_Type()
)
gs2124QosQclQcePriority5Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority5Class.setStatus("current")
_Gs2124QosQclQcePriority6Class_Type = DisplayString
_Gs2124QosQclQcePriority6Class_Object = MibTableColumn
gs2124QosQclQcePriority6Class = _Gs2124QosQclQcePriority6Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 13),
    _Gs2124QosQclQcePriority6Class_Type()
)
gs2124QosQclQcePriority6Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority6Class.setStatus("current")
_Gs2124QosQclQcePriority7Class_Type = DisplayString
_Gs2124QosQclQcePriority7Class_Object = MibTableColumn
gs2124QosQclQcePriority7Class = _Gs2124QosQclQcePriority7Class_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 14),
    _Gs2124QosQclQcePriority7Class_Type()
)
gs2124QosQclQcePriority7Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQcePriority7Class.setStatus("current")


class _Gs2124QosQclQceEntryAction_Type(Integer32):
    """Custom type gs2124QosQclQceEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124QosQclQceEntryAction_Type.__name__ = "Integer32"
_Gs2124QosQclQceEntryAction_Object = MibTableColumn
gs2124QosQclQceEntryAction = _Gs2124QosQclQceEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 17, 5, 2, 1, 15),
    _Gs2124QosQclQceEntryAction_Type()
)
gs2124QosQclQceEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124QosQclQceEntryAction.setStatus("current")
_Gs2124AclInfo_ObjectIdentity = ObjectIdentity
gs2124AclInfo = _Gs2124AclInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18)
)
_Gs2124AclPortsConfTable_Object = MibTable
gs2124AclPortsConfTable = _Gs2124AclPortsConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1)
)
if mibBuilder.loadTexts:
    gs2124AclPortsConfTable.setStatus("current")
_Gs2124AclPortsConfEntry_Object = MibTableRow
gs2124AclPortsConfEntry = _Gs2124AclPortsConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1)
)
gs2124AclPortsConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124AclPortsConfIndex"),
)
if mibBuilder.loadTexts:
    gs2124AclPortsConfEntry.setStatus("current")


class _Gs2124AclPortsConfIndex_Type(Integer32):
    """Custom type gs2124AclPortsConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124AclPortsConfIndex_Type.__name__ = "Integer32"
_Gs2124AclPortsConfIndex_Object = MibTableColumn
gs2124AclPortsConfIndex = _Gs2124AclPortsConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1, 1),
    _Gs2124AclPortsConfIndex_Type()
)
gs2124AclPortsConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124AclPortsConfIndex.setStatus("current")


class _Gs2124AclPortsConfPolicyId_Type(Integer32):
    """Custom type gs2124AclPortsConfPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Gs2124AclPortsConfPolicyId_Type.__name__ = "Integer32"
_Gs2124AclPortsConfPolicyId_Object = MibTableColumn
gs2124AclPortsConfPolicyId = _Gs2124AclPortsConfPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1, 2),
    _Gs2124AclPortsConfPolicyId_Type()
)
gs2124AclPortsConfPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AclPortsConfPolicyId.setStatus("current")


class _Gs2124AclPortsConfAction_Type(Integer32):
    """Custom type gs2124AclPortsConfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124AclPortsConfAction_Type.__name__ = "Integer32"
_Gs2124AclPortsConfAction_Object = MibTableColumn
gs2124AclPortsConfAction = _Gs2124AclPortsConfAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1, 3),
    _Gs2124AclPortsConfAction_Type()
)
gs2124AclPortsConfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AclPortsConfAction.setStatus("current")


class _Gs2124AclPortsConfRateLimiterId_Type(Integer32):
    """Custom type gs2124AclPortsConfRateLimiterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124AclPortsConfRateLimiterId_Type.__name__ = "Integer32"
_Gs2124AclPortsConfRateLimiterId_Object = MibTableColumn
gs2124AclPortsConfRateLimiterId = _Gs2124AclPortsConfRateLimiterId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1, 4),
    _Gs2124AclPortsConfRateLimiterId_Type()
)
gs2124AclPortsConfRateLimiterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AclPortsConfRateLimiterId.setStatus("current")


class _Gs2124AclPortsConfPortCopy_Type(Integer32):
    """Custom type gs2124AclPortsConfPortCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124AclPortsConfPortCopy_Type.__name__ = "Integer32"
_Gs2124AclPortsConfPortCopy_Object = MibTableColumn
gs2124AclPortsConfPortCopy = _Gs2124AclPortsConfPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1, 5),
    _Gs2124AclPortsConfPortCopy_Type()
)
gs2124AclPortsConfPortCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AclPortsConfPortCopy.setStatus("current")
_Gs2124AclPortsConfCounter_Type = Counter32
_Gs2124AclPortsConfCounter_Object = MibTableColumn
gs2124AclPortsConfCounter = _Gs2124AclPortsConfCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 1, 1, 6),
    _Gs2124AclPortsConfCounter_Type()
)
gs2124AclPortsConfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AclPortsConfCounter.setStatus("current")
_Gs2124AclRateLimiter_ObjectIdentity = ObjectIdentity
gs2124AclRateLimiter = _Gs2124AclRateLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 2)
)
_Gs2124AclRateLimiterTable_Object = MibTable
gs2124AclRateLimiterTable = _Gs2124AclRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    gs2124AclRateLimiterTable.setStatus("current")
_Gs2124AclRateLimiterEntry_Object = MibTableRow
gs2124AclRateLimiterEntry = _Gs2124AclRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 2, 1, 1)
)
gs2124AclRateLimiterEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124AclRateLimiterIndex"),
)
if mibBuilder.loadTexts:
    gs2124AclRateLimiterEntry.setStatus("current")


class _Gs2124AclRateLimiterIndex_Type(Integer32):
    """Custom type gs2124AclRateLimiterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124AclRateLimiterIndex_Type.__name__ = "Integer32"
_Gs2124AclRateLimiterIndex_Object = MibTableColumn
gs2124AclRateLimiterIndex = _Gs2124AclRateLimiterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 2, 1, 1, 1),
    _Gs2124AclRateLimiterIndex_Type()
)
gs2124AclRateLimiterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124AclRateLimiterIndex.setStatus("current")
_Gs2124AclRateLimiterRate_Type = DisplayString
_Gs2124AclRateLimiterRate_Object = MibTableColumn
gs2124AclRateLimiterRate = _Gs2124AclRateLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 2, 1, 1, 2),
    _Gs2124AclRateLimiterRate_Type()
)
gs2124AclRateLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AclRateLimiterRate.setStatus("current")
_Gs2124AclInfoViewTable_Object = MibTable
gs2124AclInfoViewTable = _Gs2124AclInfoViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3)
)
if mibBuilder.loadTexts:
    gs2124AclInfoViewTable.setStatus("current")
_Gs2124AclInfoViewEntry_Object = MibTableRow
gs2124AclInfoViewEntry = _Gs2124AclInfoViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1)
)
gs2124AclInfoViewEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124AclInfoViewNo"),
)
if mibBuilder.loadTexts:
    gs2124AclInfoViewEntry.setStatus("current")


class _Gs2124AclInfoViewNo_Type(Integer32):
    """Custom type gs2124AclInfoViewNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2124AclInfoViewNo_Type.__name__ = "Integer32"
_Gs2124AclInfoViewNo_Object = MibTableColumn
gs2124AclInfoViewNo = _Gs2124AclInfoViewNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 1),
    _Gs2124AclInfoViewNo_Type()
)
gs2124AclInfoViewNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124AclInfoViewNo.setStatus("current")
_Gs2124AceIngressPort_Type = DisplayString
_Gs2124AceIngressPort_Object = MibTableColumn
gs2124AceIngressPort = _Gs2124AceIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 2),
    _Gs2124AceIngressPort_Type()
)
gs2124AceIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AceIngressPort.setStatus("current")
_Gs2124AceFrameType_Type = DisplayString
_Gs2124AceFrameType_Object = MibTableColumn
gs2124AceFrameType = _Gs2124AceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 3),
    _Gs2124AceFrameType_Type()
)
gs2124AceFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AceFrameType.setStatus("current")
_Gs2124AceAction_Type = DisplayString
_Gs2124AceAction_Object = MibTableColumn
gs2124AceAction = _Gs2124AceAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 4),
    _Gs2124AceAction_Type()
)
gs2124AceAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AceAction.setStatus("current")
_Gs2124AceRateLimiter_Type = DisplayString
_Gs2124AceRateLimiter_Object = MibTableColumn
gs2124AceRateLimiter = _Gs2124AceRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 5),
    _Gs2124AceRateLimiter_Type()
)
gs2124AceRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AceRateLimiter.setStatus("current")
_Gs2124AcePortCopy_Type = DisplayString
_Gs2124AcePortCopy_Object = MibTableColumn
gs2124AcePortCopy = _Gs2124AcePortCopy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 6),
    _Gs2124AcePortCopy_Type()
)
gs2124AcePortCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AcePortCopy.setStatus("current")
_Gs2124AceCounter_Type = Counter32
_Gs2124AceCounter_Object = MibTableColumn
gs2124AceCounter = _Gs2124AceCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 7),
    _Gs2124AceCounter_Type()
)
gs2124AceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AceCounter.setStatus("current")
_Gs2124SmacFilter_Type = DisplayString
_Gs2124SmacFilter_Object = MibTableColumn
gs2124SmacFilter = _Gs2124SmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 8),
    _Gs2124SmacFilter_Type()
)
gs2124SmacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SmacFilter.setStatus("current")
_Gs2124DmacFilter_Type = DisplayString
_Gs2124DmacFilter_Object = MibTableColumn
gs2124DmacFilter = _Gs2124DmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 9),
    _Gs2124DmacFilter_Type()
)
gs2124DmacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DmacFilter.setStatus("current")
_Gs2124VlanIdFilter_Type = DisplayString
_Gs2124VlanIdFilter_Object = MibTableColumn
gs2124VlanIdFilter = _Gs2124VlanIdFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 10),
    _Gs2124VlanIdFilter_Type()
)
gs2124VlanIdFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124VlanIdFilter.setStatus("current")
_Gs2124VlanTagPriority_Type = DisplayString
_Gs2124VlanTagPriority_Object = MibTableColumn
gs2124VlanTagPriority = _Gs2124VlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 11),
    _Gs2124VlanTagPriority_Type()
)
gs2124VlanTagPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124VlanTagPriority.setStatus("current")
_Gs2124EtherTypeFilter_Type = DisplayString
_Gs2124EtherTypeFilter_Object = MibTableColumn
gs2124EtherTypeFilter = _Gs2124EtherTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 12),
    _Gs2124EtherTypeFilter_Type()
)
gs2124EtherTypeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124EtherTypeFilter.setStatus("current")
_Gs2124ArpRarp_Type = DisplayString
_Gs2124ArpRarp_Object = MibTableColumn
gs2124ArpRarp = _Gs2124ArpRarp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 13),
    _Gs2124ArpRarp_Type()
)
gs2124ArpRarp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpRarp.setStatus("current")
_Gs2124ArpRequestReply_Type = DisplayString
_Gs2124ArpRequestReply_Object = MibTableColumn
gs2124ArpRequestReply = _Gs2124ArpRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 14),
    _Gs2124ArpRequestReply_Type()
)
gs2124ArpRequestReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpRequestReply.setStatus("current")
_Gs2124ArpSenderIpFilter_Type = DisplayString
_Gs2124ArpSenderIpFilter_Object = MibTableColumn
gs2124ArpSenderIpFilter = _Gs2124ArpSenderIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 15),
    _Gs2124ArpSenderIpFilter_Type()
)
gs2124ArpSenderIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpSenderIpFilter.setStatus("current")
_Gs2124ArpSenderIpAddress_Type = DisplayString
_Gs2124ArpSenderIpAddress_Object = MibTableColumn
gs2124ArpSenderIpAddress = _Gs2124ArpSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 16),
    _Gs2124ArpSenderIpAddress_Type()
)
gs2124ArpSenderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpSenderIpAddress.setStatus("current")
_Gs2124ArpSenderIpMask_Type = DisplayString
_Gs2124ArpSenderIpMask_Object = MibTableColumn
gs2124ArpSenderIpMask = _Gs2124ArpSenderIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 17),
    _Gs2124ArpSenderIpMask_Type()
)
gs2124ArpSenderIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpSenderIpMask.setStatus("current")
_Gs2124ArpTargetIpFilter_Type = DisplayString
_Gs2124ArpTargetIpFilter_Object = MibTableColumn
gs2124ArpTargetIpFilter = _Gs2124ArpTargetIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 18),
    _Gs2124ArpTargetIpFilter_Type()
)
gs2124ArpTargetIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpTargetIpFilter.setStatus("current")
_Gs2124ArpTargetIpAddress_Type = DisplayString
_Gs2124ArpTargetIpAddress_Object = MibTableColumn
gs2124ArpTargetIpAddress = _Gs2124ArpTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 19),
    _Gs2124ArpTargetIpAddress_Type()
)
gs2124ArpTargetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpTargetIpAddress.setStatus("current")
_Gs2124ArpTargetIpMask_Type = DisplayString
_Gs2124ArpTargetIpMask_Object = MibTableColumn
gs2124ArpTargetIpMask = _Gs2124ArpTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 20),
    _Gs2124ArpTargetIpMask_Type()
)
gs2124ArpTargetIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpTargetIpMask.setStatus("current")
_Gs2124ArpSmacMatch_Type = DisplayString
_Gs2124ArpSmacMatch_Object = MibTableColumn
gs2124ArpSmacMatch = _Gs2124ArpSmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 21),
    _Gs2124ArpSmacMatch_Type()
)
gs2124ArpSmacMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpSmacMatch.setStatus("current")
_Gs2124ArpRarpDmacMatch_Type = DisplayString
_Gs2124ArpRarpDmacMatch_Object = MibTableColumn
gs2124ArpRarpDmacMatch = _Gs2124ArpRarpDmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 22),
    _Gs2124ArpRarpDmacMatch_Type()
)
gs2124ArpRarpDmacMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpRarpDmacMatch.setStatus("current")
_Gs2124ArpIpEthernetLength_Type = DisplayString
_Gs2124ArpIpEthernetLength_Object = MibTableColumn
gs2124ArpIpEthernetLength = _Gs2124ArpIpEthernetLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 23),
    _Gs2124ArpIpEthernetLength_Type()
)
gs2124ArpIpEthernetLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpIpEthernetLength.setStatus("current")
_Gs2124ArpIp_Type = DisplayString
_Gs2124ArpIp_Object = MibTableColumn
gs2124ArpIp = _Gs2124ArpIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 24),
    _Gs2124ArpIp_Type()
)
gs2124ArpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpIp.setStatus("current")
_Gs2124ArpEthernet_Type = DisplayString
_Gs2124ArpEthernet_Object = MibTableColumn
gs2124ArpEthernet = _Gs2124ArpEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 25),
    _Gs2124ArpEthernet_Type()
)
gs2124ArpEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124ArpEthernet.setStatus("current")
_Gs2124IpProtocolFilter_Type = DisplayString
_Gs2124IpProtocolFilter_Object = MibTableColumn
gs2124IpProtocolFilter = _Gs2124IpProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 26),
    _Gs2124IpProtocolFilter_Type()
)
gs2124IpProtocolFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IpProtocolFilter.setStatus("current")
_Gs2124IpProtocolValue_Type = DisplayString
_Gs2124IpProtocolValue_Object = MibTableColumn
gs2124IpProtocolValue = _Gs2124IpProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 27),
    _Gs2124IpProtocolValue_Type()
)
gs2124IpProtocolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IpProtocolValue.setStatus("current")
_Gs2124IpTTL_Type = DisplayString
_Gs2124IpTTL_Object = MibTableColumn
gs2124IpTTL = _Gs2124IpTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 28),
    _Gs2124IpTTL_Type()
)
gs2124IpTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IpTTL.setStatus("current")
_Gs2124IpFragment_Type = DisplayString
_Gs2124IpFragment_Object = MibTableColumn
gs2124IpFragment = _Gs2124IpFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 29),
    _Gs2124IpFragment_Type()
)
gs2124IpFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IpFragment.setStatus("current")
_Gs2124IpOption_Type = DisplayString
_Gs2124IpOption_Object = MibTableColumn
gs2124IpOption = _Gs2124IpOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 30),
    _Gs2124IpOption_Type()
)
gs2124IpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IpOption.setStatus("current")
_Gs2124SipFilter_Type = DisplayString
_Gs2124SipFilter_Object = MibTableColumn
gs2124SipFilter = _Gs2124SipFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 31),
    _Gs2124SipFilter_Type()
)
gs2124SipFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SipFilter.setStatus("current")
_Gs2124SipAddress_Type = DisplayString
_Gs2124SipAddress_Object = MibTableColumn
gs2124SipAddress = _Gs2124SipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 32),
    _Gs2124SipAddress_Type()
)
gs2124SipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SipAddress.setStatus("current")
_Gs2124SipMask_Type = DisplayString
_Gs2124SipMask_Object = MibTableColumn
gs2124SipMask = _Gs2124SipMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 33),
    _Gs2124SipMask_Type()
)
gs2124SipMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124SipMask.setStatus("current")
_Gs2124DipFilter_Type = DisplayString
_Gs2124DipFilter_Object = MibTableColumn
gs2124DipFilter = _Gs2124DipFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 34),
    _Gs2124DipFilter_Type()
)
gs2124DipFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DipFilter.setStatus("current")
_Gs2124DipAddress_Type = DisplayString
_Gs2124DipAddress_Object = MibTableColumn
gs2124DipAddress = _Gs2124DipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 35),
    _Gs2124DipAddress_Type()
)
gs2124DipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DipAddress.setStatus("current")
_Gs2124DipMask_Type = DisplayString
_Gs2124DipMask_Object = MibTableColumn
gs2124DipMask = _Gs2124DipMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 36),
    _Gs2124DipMask_Type()
)
gs2124DipMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DipMask.setStatus("current")
_Gs2124IcmpTypeFilter_Type = DisplayString
_Gs2124IcmpTypeFilter_Object = MibTableColumn
gs2124IcmpTypeFilter = _Gs2124IcmpTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 37),
    _Gs2124IcmpTypeFilter_Type()
)
gs2124IcmpTypeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IcmpTypeFilter.setStatus("current")
_Gs2124IcmpCodeFilter_Type = DisplayString
_Gs2124IcmpCodeFilter_Object = MibTableColumn
gs2124IcmpCodeFilter = _Gs2124IcmpCodeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 38),
    _Gs2124IcmpCodeFilter_Type()
)
gs2124IcmpCodeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IcmpCodeFilter.setStatus("current")
_Gs2124UdpSourcePortFilter_Type = DisplayString
_Gs2124UdpSourcePortFilter_Object = MibTableColumn
gs2124UdpSourcePortFilter = _Gs2124UdpSourcePortFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 39),
    _Gs2124UdpSourcePortFilter_Type()
)
gs2124UdpSourcePortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124UdpSourcePortFilter.setStatus("current")
_Gs2124UdpDestPortFilter_Type = DisplayString
_Gs2124UdpDestPortFilter_Object = MibTableColumn
gs2124UdpDestPortFilter = _Gs2124UdpDestPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 40),
    _Gs2124UdpDestPortFilter_Type()
)
gs2124UdpDestPortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124UdpDestPortFilter.setStatus("current")
_Gs2124TcpSourcePortFilter_Type = DisplayString
_Gs2124TcpSourcePortFilter_Object = MibTableColumn
gs2124TcpSourcePortFilter = _Gs2124TcpSourcePortFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 41),
    _Gs2124TcpSourcePortFilter_Type()
)
gs2124TcpSourcePortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpSourcePortFilter.setStatus("current")
_Gs2124TcpDestPortFilter_Type = DisplayString
_Gs2124TcpDestPortFilter_Object = MibTableColumn
gs2124TcpDestPortFilter = _Gs2124TcpDestPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 42),
    _Gs2124TcpDestPortFilter_Type()
)
gs2124TcpDestPortFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpDestPortFilter.setStatus("current")
_Gs2124TcpFIN_Type = DisplayString
_Gs2124TcpFIN_Object = MibTableColumn
gs2124TcpFIN = _Gs2124TcpFIN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 43),
    _Gs2124TcpFIN_Type()
)
gs2124TcpFIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpFIN.setStatus("current")
_Gs2124TcpSYN_Type = DisplayString
_Gs2124TcpSYN_Object = MibTableColumn
gs2124TcpSYN = _Gs2124TcpSYN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 44),
    _Gs2124TcpSYN_Type()
)
gs2124TcpSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpSYN.setStatus("current")
_Gs2124TcpRST_Type = DisplayString
_Gs2124TcpRST_Object = MibTableColumn
gs2124TcpRST = _Gs2124TcpRST_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 45),
    _Gs2124TcpRST_Type()
)
gs2124TcpRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpRST.setStatus("current")
_Gs2124TcpPSH_Type = DisplayString
_Gs2124TcpPSH_Object = MibTableColumn
gs2124TcpPSH = _Gs2124TcpPSH_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 46),
    _Gs2124TcpPSH_Type()
)
gs2124TcpPSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpPSH.setStatus("current")
_Gs2124TcpACK_Type = DisplayString
_Gs2124TcpACK_Object = MibTableColumn
gs2124TcpACK = _Gs2124TcpACK_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 47),
    _Gs2124TcpACK_Type()
)
gs2124TcpACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpACK.setStatus("current")
_Gs2124TcpURG_Type = DisplayString
_Gs2124TcpURG_Object = MibTableColumn
gs2124TcpURG = _Gs2124TcpURG_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 48),
    _Gs2124TcpURG_Type()
)
gs2124TcpURG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TcpURG.setStatus("current")


class _Gs2124AclInfoEntryAction_Type(Integer32):
    """Custom type gs2124AclInfoEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2124AclInfoEntryAction_Type.__name__ = "Integer32"
_Gs2124AclInfoEntryAction_Object = MibTableColumn
gs2124AclInfoEntryAction = _Gs2124AclInfoEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 3, 1, 49),
    _Gs2124AclInfoEntryAction_Type()
)
gs2124AclInfoEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AclInfoEntryAction.setStatus("current")
_Gs2124AclInfoConf_ObjectIdentity = ObjectIdentity
gs2124AclInfoConf = _Gs2124AclInfoConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4)
)


class _Gs2124AceNo_Type(Integer32):
    """Custom type gs2124AceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Gs2124AceNo_Type.__name__ = "Integer32"
_Gs2124AceNo_Object = MibScalar
gs2124AceNo = _Gs2124AceNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 1),
    _Gs2124AceNo_Type()
)
gs2124AceNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceNo.setStatus("current")


class _Gs2124AceMoveTo_Type(Integer32):
    """Custom type gs2124AceMoveTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Gs2124AceMoveTo_Type.__name__ = "Integer32"
_Gs2124AceMoveTo_Object = MibScalar
gs2124AceMoveTo = _Gs2124AceMoveTo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 2),
    _Gs2124AceMoveTo_Type()
)
gs2124AceMoveTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceMoveTo.setStatus("current")
_Gs2124AceIngressPortConf_Type = DisplayString
_Gs2124AceIngressPortConf_Object = MibScalar
gs2124AceIngressPortConf = _Gs2124AceIngressPortConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 3),
    _Gs2124AceIngressPortConf_Type()
)
gs2124AceIngressPortConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIngressPortConf.setStatus("current")


class _Gs2124AceFrameTypeConf_Type(Integer32):
    """Custom type gs2124AceFrameTypeConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2124AceFrameTypeConf_Type.__name__ = "Integer32"
_Gs2124AceFrameTypeConf_Object = MibScalar
gs2124AceFrameTypeConf = _Gs2124AceFrameTypeConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 4),
    _Gs2124AceFrameTypeConf_Type()
)
gs2124AceFrameTypeConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceFrameTypeConf.setStatus("current")
_Gs2124AceFrameTypeParameters_ObjectIdentity = ObjectIdentity
gs2124AceFrameTypeParameters = _Gs2124AceFrameTypeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5)
)
_Gs2124EthernetTypeFilter_Type = DisplayString
_Gs2124EthernetTypeFilter_Object = MibScalar
gs2124EthernetTypeFilter = _Gs2124EthernetTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 1),
    _Gs2124EthernetTypeFilter_Type()
)
gs2124EthernetTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124EthernetTypeFilter.setStatus("current")
_Gs2124AclArpParameters_ObjectIdentity = ObjectIdentity
gs2124AclArpParameters = _Gs2124AclArpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2)
)


class _Gs2124AceArpRarp_Type(Integer32):
    """Custom type gs2124AceArpRarp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Gs2124AceArpRarp_Type.__name__ = "Integer32"
_Gs2124AceArpRarp_Object = MibScalar
gs2124AceArpRarp = _Gs2124AceArpRarp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 1),
    _Gs2124AceArpRarp_Type()
)
gs2124AceArpRarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpRarp.setStatus("current")


class _Gs2124AceArpRequestReply_Type(Integer32):
    """Custom type gs2124AceArpRequestReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AceArpRequestReply_Type.__name__ = "Integer32"
_Gs2124AceArpRequestReply_Object = MibScalar
gs2124AceArpRequestReply = _Gs2124AceArpRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 2),
    _Gs2124AceArpRequestReply_Type()
)
gs2124AceArpRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpRequestReply.setStatus("current")


class _Gs2124AceArpSenderIpFilter_Type(Integer32):
    """Custom type gs2124AceArpSenderIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AceArpSenderIpFilter_Type.__name__ = "Integer32"
_Gs2124AceArpSenderIpFilter_Object = MibScalar
gs2124AceArpSenderIpFilter = _Gs2124AceArpSenderIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 3),
    _Gs2124AceArpSenderIpFilter_Type()
)
gs2124AceArpSenderIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpSenderIpFilter.setStatus("current")
_Gs2124AceArpSenderIpAddress_Type = DisplayString
_Gs2124AceArpSenderIpAddress_Object = MibScalar
gs2124AceArpSenderIpAddress = _Gs2124AceArpSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 4),
    _Gs2124AceArpSenderIpAddress_Type()
)
gs2124AceArpSenderIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpSenderIpAddress.setStatus("current")
_Gs2124AceArpSenderIpMask_Type = DisplayString
_Gs2124AceArpSenderIpMask_Object = MibScalar
gs2124AceArpSenderIpMask = _Gs2124AceArpSenderIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 5),
    _Gs2124AceArpSenderIpMask_Type()
)
gs2124AceArpSenderIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpSenderIpMask.setStatus("current")


class _Gs2124AceArpTargetIpFilter_Type(Integer32):
    """Custom type gs2124AceArpTargetIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AceArpTargetIpFilter_Type.__name__ = "Integer32"
_Gs2124AceArpTargetIpFilter_Object = MibScalar
gs2124AceArpTargetIpFilter = _Gs2124AceArpTargetIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 6),
    _Gs2124AceArpTargetIpFilter_Type()
)
gs2124AceArpTargetIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpTargetIpFilter.setStatus("current")
_Gs2124AceArpTargetIpAddress_Type = DisplayString
_Gs2124AceArpTargetIpAddress_Object = MibScalar
gs2124AceArpTargetIpAddress = _Gs2124AceArpTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 7),
    _Gs2124AceArpTargetIpAddress_Type()
)
gs2124AceArpTargetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpTargetIpAddress.setStatus("current")
_Gs2124AceArpTargetIpMask_Type = DisplayString
_Gs2124AceArpTargetIpMask_Object = MibScalar
gs2124AceArpTargetIpMask = _Gs2124AceArpTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 8),
    _Gs2124AceArpTargetIpMask_Type()
)
gs2124AceArpTargetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpTargetIpMask.setStatus("current")
_Gs2124AceArpSmacMatch_Type = DisplayString
_Gs2124AceArpSmacMatch_Object = MibScalar
gs2124AceArpSmacMatch = _Gs2124AceArpSmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 9),
    _Gs2124AceArpSmacMatch_Type()
)
gs2124AceArpSmacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpSmacMatch.setStatus("current")
_Gs2124AceArpRarpDmacMatch_Type = DisplayString
_Gs2124AceArpRarpDmacMatch_Object = MibScalar
gs2124AceArpRarpDmacMatch = _Gs2124AceArpRarpDmacMatch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 10),
    _Gs2124AceArpRarpDmacMatch_Type()
)
gs2124AceArpRarpDmacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpRarpDmacMatch.setStatus("current")
_Gs2124AceArpIpEthernetLength_Type = DisplayString
_Gs2124AceArpIpEthernetLength_Object = MibScalar
gs2124AceArpIpEthernetLength = _Gs2124AceArpIpEthernetLength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 11),
    _Gs2124AceArpIpEthernetLength_Type()
)
gs2124AceArpIpEthernetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpIpEthernetLength.setStatus("current")
_Gs2124AceArpIp_Type = DisplayString
_Gs2124AceArpIp_Object = MibScalar
gs2124AceArpIp = _Gs2124AceArpIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 12),
    _Gs2124AceArpIp_Type()
)
gs2124AceArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpIp.setStatus("current")
_Gs2124AceArpEthernet_Type = DisplayString
_Gs2124AceArpEthernet_Object = MibScalar
gs2124AceArpEthernet = _Gs2124AceArpEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 2, 13),
    _Gs2124AceArpEthernet_Type()
)
gs2124AceArpEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceArpEthernet.setStatus("current")
_Gs2124AclIpParameters_ObjectIdentity = ObjectIdentity
gs2124AclIpParameters = _Gs2124AclIpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3)
)


class _Gs2124AceIpProtocolFilter_Type(Integer32):
    """Custom type gs2124AceIpProtocolFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2124AceIpProtocolFilter_Type.__name__ = "Integer32"
_Gs2124AceIpProtocolFilter_Object = MibScalar
gs2124AceIpProtocolFilter = _Gs2124AceIpProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 1),
    _Gs2124AceIpProtocolFilter_Type()
)
gs2124AceIpProtocolFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIpProtocolFilter.setStatus("current")
_Gs2124AceIpProtocolFilterParameters_ObjectIdentity = ObjectIdentity
gs2124AceIpProtocolFilterParameters = _Gs2124AceIpProtocolFilterParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2)
)
_Gs2124AceIcmpParameters_ObjectIdentity = ObjectIdentity
gs2124AceIcmpParameters = _Gs2124AceIcmpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 1)
)
_Gs2124AceIcmpTypeFilter_Type = DisplayString
_Gs2124AceIcmpTypeFilter_Object = MibScalar
gs2124AceIcmpTypeFilter = _Gs2124AceIcmpTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 1, 1),
    _Gs2124AceIcmpTypeFilter_Type()
)
gs2124AceIcmpTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIcmpTypeFilter.setStatus("current")
_Gs2124AceIcmpCodeFilter_Type = DisplayString
_Gs2124AceIcmpCodeFilter_Object = MibScalar
gs2124AceIcmpCodeFilter = _Gs2124AceIcmpCodeFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 1, 2),
    _Gs2124AceIcmpCodeFilter_Type()
)
gs2124AceIcmpCodeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIcmpCodeFilter.setStatus("current")
_Gs2124AceUdpParameters_ObjectIdentity = ObjectIdentity
gs2124AceUdpParameters = _Gs2124AceUdpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 2)
)
_Gs2124UdpSourcePortFilterConf_Type = DisplayString
_Gs2124UdpSourcePortFilterConf_Object = MibScalar
gs2124UdpSourcePortFilterConf = _Gs2124UdpSourcePortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 2, 1),
    _Gs2124UdpSourcePortFilterConf_Type()
)
gs2124UdpSourcePortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124UdpSourcePortFilterConf.setStatus("current")
_Gs2124UdpDestPortFilterConf_Type = DisplayString
_Gs2124UdpDestPortFilterConf_Object = MibScalar
gs2124UdpDestPortFilterConf = _Gs2124UdpDestPortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 2, 2),
    _Gs2124UdpDestPortFilterConf_Type()
)
gs2124UdpDestPortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124UdpDestPortFilterConf.setStatus("current")
_Gs2124AceTcpParameters_ObjectIdentity = ObjectIdentity
gs2124AceTcpParameters = _Gs2124AceTcpParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3)
)
_Gs2124TcpSourcePortFilterConf_Type = DisplayString
_Gs2124TcpSourcePortFilterConf_Object = MibScalar
gs2124TcpSourcePortFilterConf = _Gs2124TcpSourcePortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 1),
    _Gs2124TcpSourcePortFilterConf_Type()
)
gs2124TcpSourcePortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpSourcePortFilterConf.setStatus("current")
_Gs2124TcpDestPortFilterConf_Type = DisplayString
_Gs2124TcpDestPortFilterConf_Object = MibScalar
gs2124TcpDestPortFilterConf = _Gs2124TcpDestPortFilterConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 2),
    _Gs2124TcpDestPortFilterConf_Type()
)
gs2124TcpDestPortFilterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpDestPortFilterConf.setStatus("current")
_Gs2124TcpFINConf_Type = DisplayString
_Gs2124TcpFINConf_Object = MibScalar
gs2124TcpFINConf = _Gs2124TcpFINConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 3),
    _Gs2124TcpFINConf_Type()
)
gs2124TcpFINConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpFINConf.setStatus("current")
_Gs2124TcpSYNConf_Type = DisplayString
_Gs2124TcpSYNConf_Object = MibScalar
gs2124TcpSYNConf = _Gs2124TcpSYNConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 4),
    _Gs2124TcpSYNConf_Type()
)
gs2124TcpSYNConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpSYNConf.setStatus("current")
_Gs2124TcpRSTConf_Type = DisplayString
_Gs2124TcpRSTConf_Object = MibScalar
gs2124TcpRSTConf = _Gs2124TcpRSTConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 5),
    _Gs2124TcpRSTConf_Type()
)
gs2124TcpRSTConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpRSTConf.setStatus("current")
_Gs2124TcpPSHConf_Type = DisplayString
_Gs2124TcpPSHConf_Object = MibScalar
gs2124TcpPSHConf = _Gs2124TcpPSHConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 6),
    _Gs2124TcpPSHConf_Type()
)
gs2124TcpPSHConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpPSHConf.setStatus("current")
_Gs2124TcpACKConf_Type = DisplayString
_Gs2124TcpACKConf_Object = MibScalar
gs2124TcpACKConf = _Gs2124TcpACKConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 7),
    _Gs2124TcpACKConf_Type()
)
gs2124TcpACKConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpACKConf.setStatus("current")
_Gs2124TcpURGConf_Type = DisplayString
_Gs2124TcpURGConf_Object = MibScalar
gs2124TcpURGConf = _Gs2124TcpURGConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 2, 3, 8),
    _Gs2124TcpURGConf_Type()
)
gs2124TcpURGConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TcpURGConf.setStatus("current")


class _Gs2124AceIpProtocolValue_Type(Integer32):
    """Custom type gs2124AceIpProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2124AceIpProtocolValue_Type.__name__ = "Integer32"
_Gs2124AceIpProtocolValue_Object = MibScalar
gs2124AceIpProtocolValue = _Gs2124AceIpProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 3),
    _Gs2124AceIpProtocolValue_Type()
)
gs2124AceIpProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIpProtocolValue.setStatus("current")
_Gs2124AceIpTTL_Type = DisplayString
_Gs2124AceIpTTL_Object = MibScalar
gs2124AceIpTTL = _Gs2124AceIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 4),
    _Gs2124AceIpTTL_Type()
)
gs2124AceIpTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIpTTL.setStatus("current")
_Gs2124AceIpFragment_Type = DisplayString
_Gs2124AceIpFragment_Object = MibScalar
gs2124AceIpFragment = _Gs2124AceIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 5),
    _Gs2124AceIpFragment_Type()
)
gs2124AceIpFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIpFragment.setStatus("current")
_Gs2124AceIpOption_Type = DisplayString
_Gs2124AceIpOption_Object = MibScalar
gs2124AceIpOption = _Gs2124AceIpOption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 6),
    _Gs2124AceIpOption_Type()
)
gs2124AceIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceIpOption.setStatus("current")


class _Gs2124AceSipFilter_Type(Integer32):
    """Custom type gs2124AceSipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AceSipFilter_Type.__name__ = "Integer32"
_Gs2124AceSipFilter_Object = MibScalar
gs2124AceSipFilter = _Gs2124AceSipFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 7),
    _Gs2124AceSipFilter_Type()
)
gs2124AceSipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceSipFilter.setStatus("current")
_Gs2124AceSipAddress_Type = DisplayString
_Gs2124AceSipAddress_Object = MibScalar
gs2124AceSipAddress = _Gs2124AceSipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 8),
    _Gs2124AceSipAddress_Type()
)
gs2124AceSipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceSipAddress.setStatus("current")
_Gs2124AceSipMask_Type = DisplayString
_Gs2124AceSipMask_Object = MibScalar
gs2124AceSipMask = _Gs2124AceSipMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 9),
    _Gs2124AceSipMask_Type()
)
gs2124AceSipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceSipMask.setStatus("current")


class _Gs2124AceDipFilter_Type(Integer32):
    """Custom type gs2124AceDipFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AceDipFilter_Type.__name__ = "Integer32"
_Gs2124AceDipFilter_Object = MibScalar
gs2124AceDipFilter = _Gs2124AceDipFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 10),
    _Gs2124AceDipFilter_Type()
)
gs2124AceDipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceDipFilter.setStatus("current")
_Gs2124AceDipAddress_Type = DisplayString
_Gs2124AceDipAddress_Object = MibScalar
gs2124AceDipAddress = _Gs2124AceDipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 11),
    _Gs2124AceDipAddress_Type()
)
gs2124AceDipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceDipAddress.setStatus("current")
_Gs2124AceDipMask_Type = DisplayString
_Gs2124AceDipMask_Object = MibScalar
gs2124AceDipMask = _Gs2124AceDipMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 5, 3, 12),
    _Gs2124AceDipMask_Type()
)
gs2124AceDipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceDipMask.setStatus("current")


class _Gs2124AceActionConf_Type(Integer32):
    """Custom type gs2124AceActionConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124AceActionConf_Type.__name__ = "Integer32"
_Gs2124AceActionConf_Object = MibScalar
gs2124AceActionConf = _Gs2124AceActionConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 6),
    _Gs2124AceActionConf_Type()
)
gs2124AceActionConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceActionConf.setStatus("current")


class _Gs2124AceRateLimiterConf_Type(Integer32):
    """Custom type gs2124AceRateLimiterConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Gs2124AceRateLimiterConf_Type.__name__ = "Integer32"
_Gs2124AceRateLimiterConf_Object = MibScalar
gs2124AceRateLimiterConf = _Gs2124AceRateLimiterConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 7),
    _Gs2124AceRateLimiterConf_Type()
)
gs2124AceRateLimiterConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceRateLimiterConf.setStatus("current")


class _Gs2124AcePortCopyConf_Type(Integer32):
    """Custom type gs2124AcePortCopyConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124AcePortCopyConf_Type.__name__ = "Integer32"
_Gs2124AcePortCopyConf_Object = MibScalar
gs2124AcePortCopyConf = _Gs2124AcePortCopyConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 8),
    _Gs2124AcePortCopyConf_Type()
)
gs2124AcePortCopyConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AcePortCopyConf.setStatus("current")
_Gs2124AceMacParameters_ObjectIdentity = ObjectIdentity
gs2124AceMacParameters = _Gs2124AceMacParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 9)
)
_Gs2124AceSmacFilter_Type = DisplayString
_Gs2124AceSmacFilter_Object = MibScalar
gs2124AceSmacFilter = _Gs2124AceSmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 9, 1),
    _Gs2124AceSmacFilter_Type()
)
gs2124AceSmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceSmacFilter.setStatus("current")
_Gs2124AceDmacFilter_Type = DisplayString
_Gs2124AceDmacFilter_Object = MibScalar
gs2124AceDmacFilter = _Gs2124AceDmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 9, 2),
    _Gs2124AceDmacFilter_Type()
)
gs2124AceDmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceDmacFilter.setStatus("current")
_Gs2124AceVlanParameters_ObjectIdentity = ObjectIdentity
gs2124AceVlanParameters = _Gs2124AceVlanParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 10)
)
_Gs2124AceVlanIdFilter_Type = DisplayString
_Gs2124AceVlanIdFilter_Object = MibScalar
gs2124AceVlanIdFilter = _Gs2124AceVlanIdFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 10, 1),
    _Gs2124AceVlanIdFilter_Type()
)
gs2124AceVlanIdFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceVlanIdFilter.setStatus("current")
_Gs2124AceTagPriority_Type = DisplayString
_Gs2124AceTagPriority_Object = MibScalar
gs2124AceTagPriority = _Gs2124AceTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 10, 2),
    _Gs2124AceTagPriority_Type()
)
gs2124AceTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceTagPriority.setStatus("current")


class _Gs2124AceInfoEntryAction_Type(Integer32):
    """Custom type gs2124AceInfoEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2124AceInfoEntryAction_Type.__name__ = "Integer32"
_Gs2124AceInfoEntryAction_Object = MibScalar
gs2124AceInfoEntryAction = _Gs2124AceInfoEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 18, 4, 11),
    _Gs2124AceInfoEntryAction_Type()
)
gs2124AceInfoEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124AceInfoEntryAction.setStatus("current")
_Gs2124IpMacBind_ObjectIdentity = ObjectIdentity
gs2124IpMacBind = _Gs2124IpMacBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19)
)
_Gs2124IpMacBindConf_ObjectIdentity = ObjectIdentity
gs2124IpMacBindConf = _Gs2124IpMacBindConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 1)
)


class _Gs2124IpMacBindstate_Type(Integer32):
    """Custom type gs2124IpMacBindstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124IpMacBindstate_Type.__name__ = "Integer32"
_Gs2124IpMacBindstate_Object = MibScalar
gs2124IpMacBindstate = _Gs2124IpMacBindstate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 1, 1),
    _Gs2124IpMacBindstate_Type()
)
gs2124IpMacBindstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindstate.setStatus("current")
_Gs2124IpMacBindTrustPort_Type = DisplayString
_Gs2124IpMacBindTrustPort_Object = MibScalar
gs2124IpMacBindTrustPort = _Gs2124IpMacBindTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 1, 2),
    _Gs2124IpMacBindTrustPort_Type()
)
gs2124IpMacBindTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindTrustPort.setStatus("current")
_Gs2124IpMacBindSetting_ObjectIdentity = ObjectIdentity
gs2124IpMacBindSetting = _Gs2124IpMacBindSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2)
)


class _Gs2124IpMacBindSettingNumber_Type(Integer32):
    """Custom type gs2124IpMacBindSettingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Gs2124IpMacBindSettingNumber_Type.__name__ = "Integer32"
_Gs2124IpMacBindSettingNumber_Object = MibScalar
gs2124IpMacBindSettingNumber = _Gs2124IpMacBindSettingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 1),
    _Gs2124IpMacBindSettingNumber_Type()
)
gs2124IpMacBindSettingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingNumber.setStatus("current")


class _Gs2124IpMacBindSettingEntryCreate_Type(Integer32):
    """Custom type gs2124IpMacBindSettingEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124IpMacBindSettingEntryCreate_Type.__name__ = "Integer32"
_Gs2124IpMacBindSettingEntryCreate_Object = MibScalar
gs2124IpMacBindSettingEntryCreate = _Gs2124IpMacBindSettingEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 2),
    _Gs2124IpMacBindSettingEntryCreate_Type()
)
gs2124IpMacBindSettingEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingEntryCreate.setStatus("current")
_Gs2124IpMacBindSettingTable_Object = MibTable
gs2124IpMacBindSettingTable = _Gs2124IpMacBindSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3)
)
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingTable.setStatus("current")
_Gs2124IpMacBindSettingEntry_Object = MibTableRow
gs2124IpMacBindSettingEntry = _Gs2124IpMacBindSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1)
)
gs2124IpMacBindSettingEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124IpMacBindSettingIndex"),
)
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingEntry.setStatus("current")


class _Gs2124IpMacBindSettingIndex_Type(Integer32):
    """Custom type gs2124IpMacBindSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2124IpMacBindSettingIndex_Type.__name__ = "Integer32"
_Gs2124IpMacBindSettingIndex_Object = MibTableColumn
gs2124IpMacBindSettingIndex = _Gs2124IpMacBindSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1, 1),
    _Gs2124IpMacBindSettingIndex_Type()
)
gs2124IpMacBindSettingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingIndex.setStatus("current")
_Gs2124IpMacBindSettingMAC_Type = DisplayString
_Gs2124IpMacBindSettingMAC_Object = MibTableColumn
gs2124IpMacBindSettingMAC = _Gs2124IpMacBindSettingMAC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1, 2),
    _Gs2124IpMacBindSettingMAC_Type()
)
gs2124IpMacBindSettingMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingMAC.setStatus("current")
_Gs2124IpMacBindSettingIP_Type = IpAddress
_Gs2124IpMacBindSettingIP_Object = MibTableColumn
gs2124IpMacBindSettingIP = _Gs2124IpMacBindSettingIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1, 3),
    _Gs2124IpMacBindSettingIP_Type()
)
gs2124IpMacBindSettingIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingIP.setStatus("current")


class _Gs2124IpMacBindSettingPort_Type(Integer32):
    """Custom type gs2124IpMacBindSettingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124IpMacBindSettingPort_Type.__name__ = "Integer32"
_Gs2124IpMacBindSettingPort_Object = MibTableColumn
gs2124IpMacBindSettingPort = _Gs2124IpMacBindSettingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1, 4),
    _Gs2124IpMacBindSettingPort_Type()
)
gs2124IpMacBindSettingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingPort.setStatus("current")


class _Gs2124IpMacBindSettingVID_Type(Integer32):
    """Custom type gs2124IpMacBindSettingVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124IpMacBindSettingVID_Type.__name__ = "Integer32"
_Gs2124IpMacBindSettingVID_Object = MibTableColumn
gs2124IpMacBindSettingVID = _Gs2124IpMacBindSettingVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1, 5),
    _Gs2124IpMacBindSettingVID_Type()
)
gs2124IpMacBindSettingVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingVID.setStatus("current")


class _Gs2124IpMacBindSettingEntryAction_Type(Integer32):
    """Custom type gs2124IpMacBindSettingEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124IpMacBindSettingEntryAction_Type.__name__ = "Integer32"
_Gs2124IpMacBindSettingEntryAction_Object = MibTableColumn
gs2124IpMacBindSettingEntryAction = _Gs2124IpMacBindSettingEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 19, 2, 3, 1, 6),
    _Gs2124IpMacBindSettingEntryAction_Type()
)
gs2124IpMacBindSettingEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IpMacBindSettingEntryAction.setStatus("current")
_Gs2124TrapEntry_ObjectIdentity = ObjectIdentity
gs2124TrapEntry = _Gs2124TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20)
)
_Gs2124TrapVariable_ObjectIdentity = ObjectIdentity
gs2124TrapVariable = _Gs2124TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 1),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _GroupId_Type(Integer32):
    """Custom type groupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GroupId_Type.__name__ = "Integer32"
_GroupId_Object = MibScalar
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupId.setStatus("current")


class _Actorkey_Type(Integer32):
    """Custom type actorkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Actorkey_Type.__name__ = "Integer32"
_Actorkey_Object = MibScalar
actorkey = _Actorkey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 3),
    _Actorkey_Type()
)
actorkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actorkey.setStatus("current")


class _Partnerkey_Type(Integer32):
    """Custom type partnerkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Partnerkey_Type.__name__ = "Integer32"
_Partnerkey_Object = MibScalar
partnerkey = _Partnerkey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Swapto_Type = DisplayString
_Swapto_Object = MibScalar
swapto = _Swapto_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 6),
    _Swapto_Type()
)
swapto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapto.setStatus("current")
_IpmacIp_Type = DisplayString
_IpmacIp_Object = MibScalar
ipmacIp = _IpmacIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 7),
    _IpmacIp_Type()
)
ipmacIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacIp.setStatus("current")
_IpmacMac_Type = DisplayString
_IpmacMac_Object = MibScalar
ipmacMac = _IpmacMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 21, 8),
    _IpmacMac_Type()
)
ipmacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacMac.setStatus("current")
_Gs2124Dot1X_ObjectIdentity = ObjectIdentity
gs2124Dot1X = _Gs2124Dot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23)
)
_Gs2124Dot1XServerConf_ObjectIdentity = ObjectIdentity
gs2124Dot1XServerConf = _Gs2124Dot1XServerConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1)
)
_Gs2124Dot1XServerConfAuthenticationServerIp_Type = IpAddress
_Gs2124Dot1XServerConfAuthenticationServerIp_Object = MibScalar
gs2124Dot1XServerConfAuthenticationServerIp = _Gs2124Dot1XServerConfAuthenticationServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 1),
    _Gs2124Dot1XServerConfAuthenticationServerIp_Type()
)
gs2124Dot1XServerConfAuthenticationServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAuthenticationServerIp.setStatus("current")


class _Gs2124Dot1XServerConfAuthenticationUdpPort_Type(Integer32):
    """Custom type gs2124Dot1XServerConfAuthenticationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124Dot1XServerConfAuthenticationUdpPort_Type.__name__ = "Integer32"
_Gs2124Dot1XServerConfAuthenticationUdpPort_Object = MibScalar
gs2124Dot1XServerConfAuthenticationUdpPort = _Gs2124Dot1XServerConfAuthenticationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 2),
    _Gs2124Dot1XServerConfAuthenticationUdpPort_Type()
)
gs2124Dot1XServerConfAuthenticationUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAuthenticationUdpPort.setStatus("current")
_Gs2124Dot1XServerConfAuthenticationServerIp2_Type = IpAddress
_Gs2124Dot1XServerConfAuthenticationServerIp2_Object = MibScalar
gs2124Dot1XServerConfAuthenticationServerIp2 = _Gs2124Dot1XServerConfAuthenticationServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 3),
    _Gs2124Dot1XServerConfAuthenticationServerIp2_Type()
)
gs2124Dot1XServerConfAuthenticationServerIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAuthenticationServerIp2.setStatus("current")


class _Gs2124Dot1XServerConfAuthenticationUdpPort2_Type(Integer32):
    """Custom type gs2124Dot1XServerConfAuthenticationUdpPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124Dot1XServerConfAuthenticationUdpPort2_Type.__name__ = "Integer32"
_Gs2124Dot1XServerConfAuthenticationUdpPort2_Object = MibScalar
gs2124Dot1XServerConfAuthenticationUdpPort2 = _Gs2124Dot1XServerConfAuthenticationUdpPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 4),
    _Gs2124Dot1XServerConfAuthenticationUdpPort2_Type()
)
gs2124Dot1XServerConfAuthenticationUdpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAuthenticationUdpPort2.setStatus("current")
_Gs2124Dot1XServerConfAuthenticationSecretKey_Type = DisplayString
_Gs2124Dot1XServerConfAuthenticationSecretKey_Object = MibScalar
gs2124Dot1XServerConfAuthenticationSecretKey = _Gs2124Dot1XServerConfAuthenticationSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 5),
    _Gs2124Dot1XServerConfAuthenticationSecretKey_Type()
)
gs2124Dot1XServerConfAuthenticationSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAuthenticationSecretKey.setStatus("current")
_Gs2124Dot1XServerConfAccountingServerIp_Type = IpAddress
_Gs2124Dot1XServerConfAccountingServerIp_Object = MibScalar
gs2124Dot1XServerConfAccountingServerIp = _Gs2124Dot1XServerConfAccountingServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 6),
    _Gs2124Dot1XServerConfAccountingServerIp_Type()
)
gs2124Dot1XServerConfAccountingServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAccountingServerIp.setStatus("current")


class _Gs2124Dot1XServerConfAccountingUdpPort_Type(Integer32):
    """Custom type gs2124Dot1XServerConfAccountingUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124Dot1XServerConfAccountingUdpPort_Type.__name__ = "Integer32"
_Gs2124Dot1XServerConfAccountingUdpPort_Object = MibScalar
gs2124Dot1XServerConfAccountingUdpPort = _Gs2124Dot1XServerConfAccountingUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 7),
    _Gs2124Dot1XServerConfAccountingUdpPort_Type()
)
gs2124Dot1XServerConfAccountingUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAccountingUdpPort.setStatus("current")
_Gs2124Dot1XServerConfAccountingServerIp2_Type = IpAddress
_Gs2124Dot1XServerConfAccountingServerIp2_Object = MibScalar
gs2124Dot1XServerConfAccountingServerIp2 = _Gs2124Dot1XServerConfAccountingServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 8),
    _Gs2124Dot1XServerConfAccountingServerIp2_Type()
)
gs2124Dot1XServerConfAccountingServerIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAccountingServerIp2.setStatus("current")


class _Gs2124Dot1XServerConfAccountingUdpPort2_Type(Integer32):
    """Custom type gs2124Dot1XServerConfAccountingUdpPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124Dot1XServerConfAccountingUdpPort2_Type.__name__ = "Integer32"
_Gs2124Dot1XServerConfAccountingUdpPort2_Object = MibScalar
gs2124Dot1XServerConfAccountingUdpPort2 = _Gs2124Dot1XServerConfAccountingUdpPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 9),
    _Gs2124Dot1XServerConfAccountingUdpPort2_Type()
)
gs2124Dot1XServerConfAccountingUdpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAccountingUdpPort2.setStatus("current")
_Gs2124Dot1XServerConfAccountingSecretKey_Type = DisplayString
_Gs2124Dot1XServerConfAccountingSecretKey_Object = MibScalar
gs2124Dot1XServerConfAccountingSecretKey = _Gs2124Dot1XServerConfAccountingSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 1, 10),
    _Gs2124Dot1XServerConfAccountingSecretKey_Type()
)
gs2124Dot1XServerConfAccountingSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XServerConfAccountingSecretKey.setStatus("current")
_Gs2124Dot1XPortConfTable_Object = MibTable
gs2124Dot1XPortConfTable = _Gs2124Dot1XPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2)
)
if mibBuilder.loadTexts:
    gs2124Dot1XPortConfTable.setStatus("current")
_Gs2124Dot1XPortConfEntry_Object = MibTableRow
gs2124Dot1XPortConfEntry = _Gs2124Dot1XPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1)
)
gs2124Dot1XPortConfEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124Dot1XPort"),
)
if mibBuilder.loadTexts:
    gs2124Dot1XPortConfEntry.setStatus("current")


class _Gs2124Dot1XPort_Type(Integer32):
    """Custom type gs2124Dot1XPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124Dot1XPort_Type.__name__ = "Integer32"
_Gs2124Dot1XPort_Object = MibTableColumn
gs2124Dot1XPort = _Gs2124Dot1XPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 1),
    _Gs2124Dot1XPort_Type()
)
gs2124Dot1XPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPort.setStatus("current")


class _Gs2124Dot1XPortMode_Type(Integer32):
    """Custom type gs2124Dot1XPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Gs2124Dot1XPortMode_Type.__name__ = "Integer32"
_Gs2124Dot1XPortMode_Object = MibTableColumn
gs2124Dot1XPortMode = _Gs2124Dot1XPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 2),
    _Gs2124Dot1XPortMode_Type()
)
gs2124Dot1XPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortMode.setStatus("current")


class _Gs2124Dot1XPortControl_Type(Integer32):
    """Custom type gs2124Dot1XPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124Dot1XPortControl_Type.__name__ = "Integer32"
_Gs2124Dot1XPortControl_Object = MibTableColumn
gs2124Dot1XPortControl = _Gs2124Dot1XPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 3),
    _Gs2124Dot1XPortControl_Type()
)
gs2124Dot1XPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortControl.setStatus("current")


class _Gs2124Dot1XPortreAuthMax_Type(Integer32):
    """Custom type gs2124Dot1XPortreAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2124Dot1XPortreAuthMax_Type.__name__ = "Integer32"
_Gs2124Dot1XPortreAuthMax_Object = MibTableColumn
gs2124Dot1XPortreAuthMax = _Gs2124Dot1XPortreAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 4),
    _Gs2124Dot1XPortreAuthMax_Type()
)
gs2124Dot1XPortreAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortreAuthMax.setStatus("current")


class _Gs2124Dot1XPorttxPeriod_Type(Integer32):
    """Custom type gs2124Dot1XPorttxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124Dot1XPorttxPeriod_Type.__name__ = "Integer32"
_Gs2124Dot1XPorttxPeriod_Object = MibTableColumn
gs2124Dot1XPorttxPeriod = _Gs2124Dot1XPorttxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 5),
    _Gs2124Dot1XPorttxPeriod_Type()
)
gs2124Dot1XPorttxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPorttxPeriod.setStatus("current")


class _Gs2124Dot1XPortquietPeriod_Type(Integer32):
    """Custom type gs2124Dot1XPortquietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2124Dot1XPortquietPeriod_Type.__name__ = "Integer32"
_Gs2124Dot1XPortquietPeriod_Object = MibTableColumn
gs2124Dot1XPortquietPeriod = _Gs2124Dot1XPortquietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 6),
    _Gs2124Dot1XPortquietPeriod_Type()
)
gs2124Dot1XPortquietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortquietPeriod.setStatus("current")


class _Gs2124Dot1XPortreAuthEnabled_Type(Integer32):
    """Custom type gs2124Dot1XPortreAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124Dot1XPortreAuthEnabled_Type.__name__ = "Integer32"
_Gs2124Dot1XPortreAuthEnabled_Object = MibTableColumn
gs2124Dot1XPortreAuthEnabled = _Gs2124Dot1XPortreAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 7),
    _Gs2124Dot1XPortreAuthEnabled_Type()
)
gs2124Dot1XPortreAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortreAuthEnabled.setStatus("current")


class _Gs2124Dot1XPortreAuthPeriod_Type(Integer32):
    """Custom type gs2124Dot1XPortreAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124Dot1XPortreAuthPeriod_Type.__name__ = "Integer32"
_Gs2124Dot1XPortreAuthPeriod_Object = MibTableColumn
gs2124Dot1XPortreAuthPeriod = _Gs2124Dot1XPortreAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 8),
    _Gs2124Dot1XPortreAuthPeriod_Type()
)
gs2124Dot1XPortreAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortreAuthPeriod.setStatus("current")


class _Gs2124Dot1XPortmaxReq_Type(Integer32):
    """Custom type gs2124Dot1XPortmaxReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Gs2124Dot1XPortmaxReq_Type.__name__ = "Integer32"
_Gs2124Dot1XPortmaxReq_Object = MibTableColumn
gs2124Dot1XPortmaxReq = _Gs2124Dot1XPortmaxReq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 9),
    _Gs2124Dot1XPortmaxReq_Type()
)
gs2124Dot1XPortmaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortmaxReq.setStatus("current")


class _Gs2124Dot1XPortsuppTimeout_Type(Integer32):
    """Custom type gs2124Dot1XPortsuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2124Dot1XPortsuppTimeout_Type.__name__ = "Integer32"
_Gs2124Dot1XPortsuppTimeout_Object = MibTableColumn
gs2124Dot1XPortsuppTimeout = _Gs2124Dot1XPortsuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 10),
    _Gs2124Dot1XPortsuppTimeout_Type()
)
gs2124Dot1XPortsuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortsuppTimeout.setStatus("current")


class _Gs2124Dot1XPortserverTimeout_Type(Integer32):
    """Custom type gs2124Dot1XPortserverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Gs2124Dot1XPortserverTimeout_Type.__name__ = "Integer32"
_Gs2124Dot1XPortserverTimeout_Object = MibTableColumn
gs2124Dot1XPortserverTimeout = _Gs2124Dot1XPortserverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 11),
    _Gs2124Dot1XPortserverTimeout_Type()
)
gs2124Dot1XPortserverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortserverTimeout.setStatus("current")


class _Gs2124Dot1XPortVlanAssignment_Type(Integer32):
    """Custom type gs2124Dot1XPortVlanAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Gs2124Dot1XPortVlanAssignment_Type.__name__ = "Integer32"
_Gs2124Dot1XPortVlanAssignment_Object = MibTableColumn
gs2124Dot1XPortVlanAssignment = _Gs2124Dot1XPortVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 12),
    _Gs2124Dot1XPortVlanAssignment_Type()
)
gs2124Dot1XPortVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortVlanAssignment.setStatus("current")


class _Gs2124Dot1XPortGuestVlan_Type(Integer32):
    """Custom type gs2124Dot1XPortGuestVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124Dot1XPortGuestVlan_Type.__name__ = "Integer32"
_Gs2124Dot1XPortGuestVlan_Object = MibTableColumn
gs2124Dot1XPortGuestVlan = _Gs2124Dot1XPortGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 13),
    _Gs2124Dot1XPortGuestVlan_Type()
)
gs2124Dot1XPortGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortGuestVlan.setStatus("current")


class _Gs2124Dot1XPortAuthFailedVlan_Type(Integer32):
    """Custom type gs2124Dot1XPortAuthFailedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124Dot1XPortAuthFailedVlan_Type.__name__ = "Integer32"
_Gs2124Dot1XPortAuthFailedVlan_Object = MibTableColumn
gs2124Dot1XPortAuthFailedVlan = _Gs2124Dot1XPortAuthFailedVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 2, 1, 14),
    _Gs2124Dot1XPortAuthFailedVlan_Type()
)
gs2124Dot1XPortAuthFailedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XPortAuthFailedVlan.setStatus("current")
_Gs2124Dot1XStatusTable_Object = MibTable
gs2124Dot1XStatusTable = _Gs2124Dot1XStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 3)
)
if mibBuilder.loadTexts:
    gs2124Dot1XStatusTable.setStatus("current")
_Gs2124Dot1XStatusEntry_Object = MibTableRow
gs2124Dot1XStatusEntry = _Gs2124Dot1XStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 3, 1)
)
gs2124Dot1XStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124Dot1XStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2124Dot1XStatusEntry.setStatus("current")


class _Gs2124Dot1XStatusIndex_Type(Integer32):
    """Custom type gs2124Dot1XStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124Dot1XStatusIndex_Type.__name__ = "Integer32"
_Gs2124Dot1XStatusIndex_Object = MibTableColumn
gs2124Dot1XStatusIndex = _Gs2124Dot1XStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 3, 1, 1),
    _Gs2124Dot1XStatusIndex_Type()
)
gs2124Dot1XStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124Dot1XStatusIndex.setStatus("current")
_Gs2124Dot1XStatusMode_Type = DisplayString
_Gs2124Dot1XStatusMode_Object = MibTableColumn
gs2124Dot1XStatusMode = _Gs2124Dot1XStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 3, 1, 2),
    _Gs2124Dot1XStatusMode_Type()
)
gs2124Dot1XStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XStatusMode.setStatus("current")
_Gs2124Dot1XStatusStatus_Type = DisplayString
_Gs2124Dot1XStatusStatus_Object = MibTableColumn
gs2124Dot1XStatusStatus = _Gs2124Dot1XStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 3, 1, 3),
    _Gs2124Dot1XStatusStatus_Type()
)
gs2124Dot1XStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XStatusStatus.setStatus("current")
_Gs2124Dot1XVlanPlicy_Type = DisplayString
_Gs2124Dot1XVlanPlicy_Object = MibTableColumn
gs2124Dot1XVlanPlicy = _Gs2124Dot1XVlanPlicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 3, 1, 4),
    _Gs2124Dot1XVlanPlicy_Type()
)
gs2124Dot1XVlanPlicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XVlanPlicy.setStatus("current")
_Gs2124Dot1XStatisticsTable_Object = MibTable
gs2124Dot1XStatisticsTable = _Gs2124Dot1XStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4)
)
if mibBuilder.loadTexts:
    gs2124Dot1XStatisticsTable.setStatus("current")
_Gs2124Dot1XStatisticsEntry_Object = MibTableRow
gs2124Dot1XStatisticsEntry = _Gs2124Dot1XStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1)
)
gs2124Dot1XStatisticsEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124Dot1XStatisticsIndex"),
)
if mibBuilder.loadTexts:
    gs2124Dot1XStatisticsEntry.setStatus("current")


class _Gs2124Dot1XStatisticsIndex_Type(Integer32):
    """Custom type gs2124Dot1XStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124Dot1XStatisticsIndex_Type.__name__ = "Integer32"
_Gs2124Dot1XStatisticsIndex_Object = MibTableColumn
gs2124Dot1XStatisticsIndex = _Gs2124Dot1XStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 1),
    _Gs2124Dot1XStatisticsIndex_Type()
)
gs2124Dot1XStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124Dot1XStatisticsIndex.setStatus("current")


class _Gs2124Dot1XClearCounter_Type(Integer32):
    """Custom type gs2124Dot1XClearCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124Dot1XClearCounter_Type.__name__ = "Integer32"
_Gs2124Dot1XClearCounter_Object = MibTableColumn
gs2124Dot1XClearCounter = _Gs2124Dot1XClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 2),
    _Gs2124Dot1XClearCounter_Type()
)
gs2124Dot1XClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124Dot1XClearCounter.setStatus("current")
_Gs2124Dot1XAuthEntersConnecting_Type = Counter32
_Gs2124Dot1XAuthEntersConnecting_Object = MibTableColumn
gs2124Dot1XAuthEntersConnecting = _Gs2124Dot1XAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 3),
    _Gs2124Dot1XAuthEntersConnecting_Type()
)
gs2124Dot1XAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEntersConnecting.setStatus("current")
_Gs2124Dot1XauthEapLogoffsWhileConnecting_Type = Counter32
_Gs2124Dot1XauthEapLogoffsWhileConnecting_Object = MibTableColumn
gs2124Dot1XauthEapLogoffsWhileConnecting = _Gs2124Dot1XauthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 4),
    _Gs2124Dot1XauthEapLogoffsWhileConnecting_Type()
)
gs2124Dot1XauthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XauthEapLogoffsWhileConnecting.setStatus("current")
_Gs2124Dot1XAuthEntersAuthenticating_Type = Counter32
_Gs2124Dot1XAuthEntersAuthenticating_Object = MibTableColumn
gs2124Dot1XAuthEntersAuthenticating = _Gs2124Dot1XAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 5),
    _Gs2124Dot1XAuthEntersAuthenticating_Type()
)
gs2124Dot1XAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEntersAuthenticating.setStatus("current")
_Gs2124Dot1XAuthAuthSuccessesWhileAuthenticating_Type = Counter32
_Gs2124Dot1XAuthAuthSuccessesWhileAuthenticating_Object = MibTableColumn
gs2124Dot1XAuthAuthSuccessesWhileAuthenticating = _Gs2124Dot1XAuthAuthSuccessesWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 6),
    _Gs2124Dot1XAuthAuthSuccessesWhileAuthenticating_Type()
)
gs2124Dot1XAuthAuthSuccessesWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthSuccessesWhileAuthenticating.setStatus("current")
_Gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_Gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating = _Gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 7),
    _Gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating_Type()
)
gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_Gs2124Dot1XAuthAuthFailWhileAuthenticating_Type = Counter32
_Gs2124Dot1XAuthAuthFailWhileAuthenticating_Object = MibTableColumn
gs2124Dot1XAuthAuthFailWhileAuthenticating = _Gs2124Dot1XAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 8),
    _Gs2124Dot1XAuthAuthFailWhileAuthenticating_Type()
)
gs2124Dot1XAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthFailWhileAuthenticating.setStatus("current")
_Gs2124Dot1XAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_Gs2124Dot1XAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
gs2124Dot1XAuthAuthEapStartsWhileAuthenticating = _Gs2124Dot1XAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 9),
    _Gs2124Dot1XAuthAuthEapStartsWhileAuthenticating_Type()
)
gs2124Dot1XAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating = _Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 10),
    _Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating_Type()
)
gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_Gs2124Dot1XAuthAuthReauthsWhileAuthenticated_Type = Counter32
_Gs2124Dot1XAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
gs2124Dot1XAuthAuthReauthsWhileAuthenticated = _Gs2124Dot1XAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 11),
    _Gs2124Dot1XAuthAuthReauthsWhileAuthenticated_Type()
)
gs2124Dot1XAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthReauthsWhileAuthenticated.setStatus("current")
_Gs2124Dot1XAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_Gs2124Dot1XAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
gs2124Dot1XAuthAuthEapStartsWhileAuthenticated = _Gs2124Dot1XAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 12),
    _Gs2124Dot1XAuthAuthEapStartsWhileAuthenticated_Type()
)
gs2124Dot1XAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated = _Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 13),
    _Gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated_Type()
)
gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_Gs2124Dot1XBackendResponses_Type = Counter32
_Gs2124Dot1XBackendResponses_Object = MibTableColumn
gs2124Dot1XBackendResponses = _Gs2124Dot1XBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 14),
    _Gs2124Dot1XBackendResponses_Type()
)
gs2124Dot1XBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XBackendResponses.setStatus("current")
_Gs2124Dot1XBackendAccessChallenges_Type = Counter32
_Gs2124Dot1XBackendAccessChallenges_Object = MibTableColumn
gs2124Dot1XBackendAccessChallenges = _Gs2124Dot1XBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 15),
    _Gs2124Dot1XBackendAccessChallenges_Type()
)
gs2124Dot1XBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XBackendAccessChallenges.setStatus("current")
_Gs2124Dot1XBackendOtherRequestsToSupplicant_Type = Counter32
_Gs2124Dot1XBackendOtherRequestsToSupplicant_Object = MibTableColumn
gs2124Dot1XBackendOtherRequestsToSupplicant = _Gs2124Dot1XBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 16),
    _Gs2124Dot1XBackendOtherRequestsToSupplicant_Type()
)
gs2124Dot1XBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XBackendOtherRequestsToSupplicant.setStatus("current")
_Gs2124Dot1XBackendAuthSuccesses_Type = Counter32
_Gs2124Dot1XBackendAuthSuccesses_Object = MibTableColumn
gs2124Dot1XBackendAuthSuccesses = _Gs2124Dot1XBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 17),
    _Gs2124Dot1XBackendAuthSuccesses_Type()
)
gs2124Dot1XBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XBackendAuthSuccesses.setStatus("current")
_Gs2124Dot1XBackendAuthFails_Type = Counter32
_Gs2124Dot1XBackendAuthFails_Object = MibTableColumn
gs2124Dot1XBackendAuthFails = _Gs2124Dot1XBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 18),
    _Gs2124Dot1XBackendAuthFails_Type()
)
gs2124Dot1XBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XBackendAuthFails.setStatus("current")
_Gs2124Dot1XAuthEapolFramesRx_Type = Counter32
_Gs2124Dot1XAuthEapolFramesRx_Object = MibTableColumn
gs2124Dot1XAuthEapolFramesRx = _Gs2124Dot1XAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 19),
    _Gs2124Dot1XAuthEapolFramesRx_Type()
)
gs2124Dot1XAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolFramesRx.setStatus("current")
_Gs2124Dot1XAuthEapolFramesTx_Type = Counter32
_Gs2124Dot1XAuthEapolFramesTx_Object = MibTableColumn
gs2124Dot1XAuthEapolFramesTx = _Gs2124Dot1XAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 20),
    _Gs2124Dot1XAuthEapolFramesTx_Type()
)
gs2124Dot1XAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolFramesTx.setStatus("current")
_Gs2124Dot1XAuthEapolStartFramesRx_Type = Counter32
_Gs2124Dot1XAuthEapolStartFramesRx_Object = MibTableColumn
gs2124Dot1XAuthEapolStartFramesRx = _Gs2124Dot1XAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 21),
    _Gs2124Dot1XAuthEapolStartFramesRx_Type()
)
gs2124Dot1XAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolStartFramesRx.setStatus("current")
_Gs2124Dot1XAuthEapolLogoffFramesRx_Type = Counter32
_Gs2124Dot1XAuthEapolLogoffFramesRx_Object = MibTableColumn
gs2124Dot1XAuthEapolLogoffFramesRx = _Gs2124Dot1XAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 22),
    _Gs2124Dot1XAuthEapolLogoffFramesRx_Type()
)
gs2124Dot1XAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolLogoffFramesRx.setStatus("current")
_Gs2124Dot1XAuthEapolRespIdFramesRx_Type = Counter32
_Gs2124Dot1XAuthEapolRespIdFramesRx_Object = MibTableColumn
gs2124Dot1XAuthEapolRespIdFramesRx = _Gs2124Dot1XAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 23),
    _Gs2124Dot1XAuthEapolRespIdFramesRx_Type()
)
gs2124Dot1XAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolRespIdFramesRx.setStatus("current")
_Gs2124Dot1XAuthEapolRespFramesRx_Type = Counter32
_Gs2124Dot1XAuthEapolRespFramesRx_Object = MibTableColumn
gs2124Dot1XAuthEapolRespFramesRx = _Gs2124Dot1XAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 24),
    _Gs2124Dot1XAuthEapolRespFramesRx_Type()
)
gs2124Dot1XAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolRespFramesRx.setStatus("current")
_Gs2124Dot1XAuthEapolReqIdFramesTx_Type = Counter32
_Gs2124Dot1XAuthEapolReqIdFramesTx_Object = MibTableColumn
gs2124Dot1XAuthEapolReqIdFramesTx = _Gs2124Dot1XAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 25),
    _Gs2124Dot1XAuthEapolReqIdFramesTx_Type()
)
gs2124Dot1XAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolReqIdFramesTx.setStatus("current")
_Gs2124Dot1XAuthEapolReqFramesTx_Type = Counter32
_Gs2124Dot1XAuthEapolReqFramesTx_Object = MibTableColumn
gs2124Dot1XAuthEapolReqFramesTx = _Gs2124Dot1XAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 26),
    _Gs2124Dot1XAuthEapolReqFramesTx_Type()
)
gs2124Dot1XAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapolReqFramesTx.setStatus("current")
_Gs2124Dot1XAuthInvalidEapolFramesRx_Type = Counter32
_Gs2124Dot1XAuthInvalidEapolFramesRx_Object = MibTableColumn
gs2124Dot1XAuthInvalidEapolFramesRx = _Gs2124Dot1XAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 27),
    _Gs2124Dot1XAuthInvalidEapolFramesRx_Type()
)
gs2124Dot1XAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthInvalidEapolFramesRx.setStatus("current")
_Gs2124Dot1XAuthEapLengthErrorFramesRx_Type = Counter32
_Gs2124Dot1XAuthEapLengthErrorFramesRx_Object = MibTableColumn
gs2124Dot1XAuthEapLengthErrorFramesRx = _Gs2124Dot1XAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 28),
    _Gs2124Dot1XAuthEapLengthErrorFramesRx_Type()
)
gs2124Dot1XAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthEapLengthErrorFramesRx.setStatus("current")
_Gs2124Dot1XAuthLastEapolFrameVersion_Type = Counter32
_Gs2124Dot1XAuthLastEapolFrameVersion_Object = MibTableColumn
gs2124Dot1XAuthLastEapolFrameVersion = _Gs2124Dot1XAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 29),
    _Gs2124Dot1XAuthLastEapolFrameVersion_Type()
)
gs2124Dot1XAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthLastEapolFrameVersion.setStatus("current")
_Gs2124Dot1XAuthLastEapolFrameSource_Type = DisplayString
_Gs2124Dot1XAuthLastEapolFrameSource_Object = MibTableColumn
gs2124Dot1XAuthLastEapolFrameSource = _Gs2124Dot1XAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 23, 4, 1, 30),
    _Gs2124Dot1XAuthLastEapolFrameSource_Type()
)
gs2124Dot1XAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124Dot1XAuthLastEapolFrameSource.setStatus("current")
_Gs2124TrunkInfo_ObjectIdentity = ObjectIdentity
gs2124TrunkInfo = _Gs2124TrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24)
)
_Gs2124TrunkPort_ObjectIdentity = ObjectIdentity
gs2124TrunkPort = _Gs2124TrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1)
)
_Gs2124TrunkPortTable_Object = MibTable
gs2124TrunkPortTable = _Gs2124TrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    gs2124TrunkPortTable.setStatus("current")
_Gs2124TrunkPortEntry_Object = MibTableRow
gs2124TrunkPortEntry = _Gs2124TrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1)
)
gs2124TrunkPortEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124TrunkPortIndex"),
)
if mibBuilder.loadTexts:
    gs2124TrunkPortEntry.setStatus("current")


class _Gs2124TrunkPortIndex_Type(Integer32):
    """Custom type gs2124TrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124TrunkPortIndex_Type.__name__ = "Integer32"
_Gs2124TrunkPortIndex_Object = MibTableColumn
gs2124TrunkPortIndex = _Gs2124TrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 1),
    _Gs2124TrunkPortIndex_Type()
)
gs2124TrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124TrunkPortIndex.setStatus("current")


class _Gs2124TrunkPortMethod_Type(Integer32):
    """Custom type gs2124TrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124TrunkPortMethod_Type.__name__ = "Integer32"
_Gs2124TrunkPortMethod_Object = MibTableColumn
gs2124TrunkPortMethod = _Gs2124TrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 2),
    _Gs2124TrunkPortMethod_Type()
)
gs2124TrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrunkPortMethod.setStatus("current")


class _Gs2124TrunkPortGroup_Type(Integer32):
    """Custom type gs2124TrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Gs2124TrunkPortGroup_Type.__name__ = "Integer32"
_Gs2124TrunkPortGroup_Object = MibTableColumn
gs2124TrunkPortGroup = _Gs2124TrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 3),
    _Gs2124TrunkPortGroup_Type()
)
gs2124TrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrunkPortGroup.setStatus("current")


class _Gs2124TrunkPortActiveLacp_Type(Integer32):
    """Custom type gs2124TrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124TrunkPortActiveLacp_Type.__name__ = "Integer32"
_Gs2124TrunkPortActiveLacp_Object = MibTableColumn
gs2124TrunkPortActiveLacp = _Gs2124TrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 4),
    _Gs2124TrunkPortActiveLacp_Type()
)
gs2124TrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrunkPortActiveLacp.setStatus("current")


class _Gs2124TrunkPortAggtr_Type(Integer32):
    """Custom type gs2124TrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124TrunkPortAggtr_Type.__name__ = "Integer32"
_Gs2124TrunkPortAggtr_Object = MibTableColumn
gs2124TrunkPortAggtr = _Gs2124TrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 5),
    _Gs2124TrunkPortAggtr_Type()
)
gs2124TrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TrunkPortAggtr.setStatus("current")


class _Gs2124TrunkPortStatus_Type(Integer32):
    """Custom type gs2124TrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124TrunkPortStatus_Type.__name__ = "Integer32"
_Gs2124TrunkPortStatus_Object = MibTableColumn
gs2124TrunkPortStatus = _Gs2124TrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 6),
    _Gs2124TrunkPortStatus_Type()
)
gs2124TrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124TrunkPortStatus.setStatus("current")


class _Gs2124TrunkPortCurrentMode_Type(Integer32):
    """Custom type gs2124TrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124TrunkPortCurrentMode_Type.__name__ = "Integer32"
_Gs2124TrunkPortCurrentMode_Object = MibTableColumn
gs2124TrunkPortCurrentMode = _Gs2124TrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 1, 1, 1, 7),
    _Gs2124TrunkPortCurrentMode_Type()
)
gs2124TrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124TrunkPortCurrentMode.setStatus("current")
_Gs2124AggregatorView_ObjectIdentity = ObjectIdentity
gs2124AggregatorView = _Gs2124AggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2)
)
_Gs2124AggregatorViewTable_Object = MibTable
gs2124AggregatorViewTable = _Gs2124AggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    gs2124AggregatorViewTable.setStatus("current")
_Gs2124AggregatorViewEntry_Object = MibTableRow
gs2124AggregatorViewEntry = _Gs2124AggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2, 1, 1)
)
gs2124AggregatorViewEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124AggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    gs2124AggregatorViewEntry.setStatus("current")


class _Gs2124AggregatorViewIndex_Type(Integer32):
    """Custom type gs2124AggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124AggregatorViewIndex_Type.__name__ = "Integer32"
_Gs2124AggregatorViewIndex_Object = MibTableColumn
gs2124AggregatorViewIndex = _Gs2124AggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2, 1, 1, 1),
    _Gs2124AggregatorViewIndex_Type()
)
gs2124AggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124AggregatorViewIndex.setStatus("current")


class _Gs2124AggregatorViewMethod_Type(Integer32):
    """Custom type gs2124AggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124AggregatorViewMethod_Type.__name__ = "Integer32"
_Gs2124AggregatorViewMethod_Object = MibTableColumn
gs2124AggregatorViewMethod = _Gs2124AggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2, 1, 1, 2),
    _Gs2124AggregatorViewMethod_Type()
)
gs2124AggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AggregatorViewMethod.setStatus("current")
_Gs2124AggregatorViewMemberPorts_Type = DisplayString
_Gs2124AggregatorViewMemberPorts_Object = MibTableColumn
gs2124AggregatorViewMemberPorts = _Gs2124AggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2, 1, 1, 3),
    _Gs2124AggregatorViewMemberPorts_Type()
)
gs2124AggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AggregatorViewMemberPorts.setStatus("current")
_Gs2124AggregatorViewReadyPorts_Type = DisplayString
_Gs2124AggregatorViewReadyPorts_Object = MibTableColumn
gs2124AggregatorViewReadyPorts = _Gs2124AggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 2, 1, 1, 4),
    _Gs2124AggregatorViewReadyPorts_Type()
)
gs2124AggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124AggregatorViewReadyPorts.setStatus("current")


class _Gs2124LacpSystemPriority_Type(Integer32):
    """Custom type gs2124LacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124LacpSystemPriority_Type.__name__ = "Integer32"
_Gs2124LacpSystemPriority_Object = MibScalar
gs2124LacpSystemPriority = _Gs2124LacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 3),
    _Gs2124LacpSystemPriority_Type()
)
gs2124LacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124LacpSystemPriority.setStatus("current")
_Gs2124AggregationHashMode_ObjectIdentity = ObjectIdentity
gs2124AggregationHashMode = _Gs2124AggregationHashMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 4)
)


class _Gs2124HashCodeSourceMacAddress_Type(Integer32):
    """Custom type gs2124HashCodeSourceMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124HashCodeSourceMacAddress_Type.__name__ = "Integer32"
_Gs2124HashCodeSourceMacAddress_Object = MibScalar
gs2124HashCodeSourceMacAddress = _Gs2124HashCodeSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 4, 1),
    _Gs2124HashCodeSourceMacAddress_Type()
)
gs2124HashCodeSourceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124HashCodeSourceMacAddress.setStatus("current")


class _Gs2124HashCodeDestinationMacAddress_Type(Integer32):
    """Custom type gs2124HashCodeDestinationMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124HashCodeDestinationMacAddress_Type.__name__ = "Integer32"
_Gs2124HashCodeDestinationMacAddress_Object = MibScalar
gs2124HashCodeDestinationMacAddress = _Gs2124HashCodeDestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 4, 2),
    _Gs2124HashCodeDestinationMacAddress_Type()
)
gs2124HashCodeDestinationMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124HashCodeDestinationMacAddress.setStatus("current")


class _Gs2124HashCodeIpAddress_Type(Integer32):
    """Custom type gs2124HashCodeIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124HashCodeIpAddress_Type.__name__ = "Integer32"
_Gs2124HashCodeIpAddress_Object = MibScalar
gs2124HashCodeIpAddress = _Gs2124HashCodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 4, 3),
    _Gs2124HashCodeIpAddress_Type()
)
gs2124HashCodeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124HashCodeIpAddress.setStatus("current")


class _Gs2124HashCodeTcpUdpPortNumber_Type(Integer32):
    """Custom type gs2124HashCodeTcpUdpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124HashCodeTcpUdpPortNumber_Type.__name__ = "Integer32"
_Gs2124HashCodeTcpUdpPortNumber_Object = MibScalar
gs2124HashCodeTcpUdpPortNumber = _Gs2124HashCodeTcpUdpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 24, 4, 4),
    _Gs2124HashCodeTcpUdpPortNumber_Type()
)
gs2124HashCodeTcpUdpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124HashCodeTcpUdpPortNumber.setStatus("current")
_Gs2124MulticastInfo_ObjectIdentity = ObjectIdentity
gs2124MulticastInfo = _Gs2124MulticastInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25)
)


class _Gs2124IGMPMode_Type(Integer32):
    """Custom type gs2124IGMPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2124IGMPMode_Type.__name__ = "Integer32"
_Gs2124IGMPMode_Object = MibScalar
gs2124IGMPMode = _Gs2124IGMPMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 1),
    _Gs2124IGMPMode_Type()
)
gs2124IGMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IGMPMode.setStatus("current")
_Gs2124IGMPGroupAllowConf_ObjectIdentity = ObjectIdentity
gs2124IGMPGroupAllowConf = _Gs2124IGMPGroupAllowConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2)
)


class _Gs2124IGMPGroupAllowNumber_Type(Integer32):
    """Custom type gs2124IGMPGroupAllowNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2124IGMPGroupAllowNumber_Type.__name__ = "Integer32"
_Gs2124IGMPGroupAllowNumber_Object = MibScalar
gs2124IGMPGroupAllowNumber = _Gs2124IGMPGroupAllowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 1),
    _Gs2124IGMPGroupAllowNumber_Type()
)
gs2124IGMPGroupAllowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowNumber.setStatus("current")


class _Gs2124IGMPGroupAllowEntryCreate_Type(Integer32):
    """Custom type gs2124IGMPGroupAllowEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124IGMPGroupAllowEntryCreate_Type.__name__ = "Integer32"
_Gs2124IGMPGroupAllowEntryCreate_Object = MibScalar
gs2124IGMPGroupAllowEntryCreate = _Gs2124IGMPGroupAllowEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 2),
    _Gs2124IGMPGroupAllowEntryCreate_Type()
)
gs2124IGMPGroupAllowEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowEntryCreate.setStatus("current")
_Gs2124IGMPGroupAllowTable_Object = MibTable
gs2124IGMPGroupAllowTable = _Gs2124IGMPGroupAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowTable.setStatus("current")
_Gs2124IGMPGroupAllowEntry_Object = MibTableRow
gs2124IGMPGroupAllowEntry = _Gs2124IGMPGroupAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3, 1)
)
gs2124IGMPGroupAllowEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124IGMPGroupAllowNo"),
)
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowEntry.setStatus("current")


class _Gs2124IGMPGroupAllowNo_Type(Integer32):
    """Custom type gs2124IGMPGroupAllowNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2124IGMPGroupAllowNo_Type.__name__ = "Integer32"
_Gs2124IGMPGroupAllowNo_Object = MibTableColumn
gs2124IGMPGroupAllowNo = _Gs2124IGMPGroupAllowNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3, 1, 1),
    _Gs2124IGMPGroupAllowNo_Type()
)
gs2124IGMPGroupAllowNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowNo.setStatus("current")


class _Gs2124IGMPGroupAllowVid_Type(Integer32):
    """Custom type gs2124IGMPGroupAllowVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124IGMPGroupAllowVid_Type.__name__ = "Integer32"
_Gs2124IGMPGroupAllowVid_Object = MibTableColumn
gs2124IGMPGroupAllowVid = _Gs2124IGMPGroupAllowVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3, 1, 2),
    _Gs2124IGMPGroupAllowVid_Type()
)
gs2124IGMPGroupAllowVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowVid.setStatus("current")
_Gs2124IGMPGroupAllowStartAddress_Type = DisplayString
_Gs2124IGMPGroupAllowStartAddress_Object = MibTableColumn
gs2124IGMPGroupAllowStartAddress = _Gs2124IGMPGroupAllowStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3, 1, 3),
    _Gs2124IGMPGroupAllowStartAddress_Type()
)
gs2124IGMPGroupAllowStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowStartAddress.setStatus("current")
_Gs2124IGMPGroupAllowEndAddress_Type = DisplayString
_Gs2124IGMPGroupAllowEndAddress_Object = MibTableColumn
gs2124IGMPGroupAllowEndAddress = _Gs2124IGMPGroupAllowEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3, 1, 4),
    _Gs2124IGMPGroupAllowEndAddress_Type()
)
gs2124IGMPGroupAllowEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowEndAddress.setStatus("current")


class _Gs2124IGMPGroupAllowEntryAction_Type(Integer32):
    """Custom type gs2124IGMPGroupAllowEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2124IGMPGroupAllowEntryAction_Type.__name__ = "Integer32"
_Gs2124IGMPGroupAllowEntryAction_Object = MibTableColumn
gs2124IGMPGroupAllowEntryAction = _Gs2124IGMPGroupAllowEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 2, 3, 1, 5),
    _Gs2124IGMPGroupAllowEntryAction_Type()
)
gs2124IGMPGroupAllowEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IGMPGroupAllowEntryAction.setStatus("current")
_Gs2124IGMPProxy_ObjectIdentity = ObjectIdentity
gs2124IGMPProxy = _Gs2124IGMPProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3)
)


class _Gs2124IgmpProxyConfGeneralQueryInterval_Type(Integer32):
    """Custom type gs2124IgmpProxyConfGeneralQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Gs2124IgmpProxyConfGeneralQueryInterval_Type.__name__ = "Integer32"
_Gs2124IgmpProxyConfGeneralQueryInterval_Object = MibScalar
gs2124IgmpProxyConfGeneralQueryInterval = _Gs2124IgmpProxyConfGeneralQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 1),
    _Gs2124IgmpProxyConfGeneralQueryInterval_Type()
)
gs2124IgmpProxyConfGeneralQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfGeneralQueryInterval.setStatus("current")


class _Gs2124IgmpProxyConfGeneralQueryRepTimeout_Type(Integer32):
    """Custom type gs2124IgmpProxyConfGeneralQueryRepTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Gs2124IgmpProxyConfGeneralQueryRepTimeout_Type.__name__ = "Integer32"
_Gs2124IgmpProxyConfGeneralQueryRepTimeout_Object = MibScalar
gs2124IgmpProxyConfGeneralQueryRepTimeout = _Gs2124IgmpProxyConfGeneralQueryRepTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 2),
    _Gs2124IgmpProxyConfGeneralQueryRepTimeout_Type()
)
gs2124IgmpProxyConfGeneralQueryRepTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfGeneralQueryRepTimeout.setStatus("current")


class _Gs2124IgmpProxyConfGeneralQueryMaxRepTime_Type(Integer32):
    """Custom type gs2124IgmpProxyConfGeneralQueryMaxRepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Gs2124IgmpProxyConfGeneralQueryMaxRepTime_Type.__name__ = "Integer32"
_Gs2124IgmpProxyConfGeneralQueryMaxRepTime_Object = MibScalar
gs2124IgmpProxyConfGeneralQueryMaxRepTime = _Gs2124IgmpProxyConfGeneralQueryMaxRepTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 3),
    _Gs2124IgmpProxyConfGeneralQueryMaxRepTime_Type()
)
gs2124IgmpProxyConfGeneralQueryMaxRepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfGeneralQueryMaxRepTime.setStatus("current")


class _Gs2124IgmpProxyConfLastMemberQueryCount_Type(Integer32):
    """Custom type gs2124IgmpProxyConfLastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2124IgmpProxyConfLastMemberQueryCount_Type.__name__ = "Integer32"
_Gs2124IgmpProxyConfLastMemberQueryCount_Object = MibScalar
gs2124IgmpProxyConfLastMemberQueryCount = _Gs2124IgmpProxyConfLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 4),
    _Gs2124IgmpProxyConfLastMemberQueryCount_Type()
)
gs2124IgmpProxyConfLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfLastMemberQueryCount.setStatus("current")


class _Gs2124IgmpProxyConfLastMemberQueryInterval_Type(Integer32):
    """Custom type gs2124IgmpProxyConfLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Gs2124IgmpProxyConfLastMemberQueryInterval_Type.__name__ = "Integer32"
_Gs2124IgmpProxyConfLastMemberQueryInterval_Object = MibScalar
gs2124IgmpProxyConfLastMemberQueryInterval = _Gs2124IgmpProxyConfLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 5),
    _Gs2124IgmpProxyConfLastMemberQueryInterval_Type()
)
gs2124IgmpProxyConfLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfLastMemberQueryInterval.setStatus("current")


class _Gs2124IgmpProxyConfLastMemberQueryMaxRepTime_Type(Integer32):
    """Custom type gs2124IgmpProxyConfLastMemberQueryMaxRepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_Gs2124IgmpProxyConfLastMemberQueryMaxRepTime_Type.__name__ = "Integer32"
_Gs2124IgmpProxyConfLastMemberQueryMaxRepTime_Object = MibScalar
gs2124IgmpProxyConfLastMemberQueryMaxRepTime = _Gs2124IgmpProxyConfLastMemberQueryMaxRepTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 6),
    _Gs2124IgmpProxyConfLastMemberQueryMaxRepTime_Type()
)
gs2124IgmpProxyConfLastMemberQueryMaxRepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfLastMemberQueryMaxRepTime.setStatus("current")
_Gs2124IgmpProxyConfRouterPorts_Type = DisplayString
_Gs2124IgmpProxyConfRouterPorts_Object = MibScalar
gs2124IgmpProxyConfRouterPorts = _Gs2124IgmpProxyConfRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 7),
    _Gs2124IgmpProxyConfRouterPorts_Type()
)
gs2124IgmpProxyConfRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyConfRouterPorts.setStatus("current")


class _Gs2124IgmpProxyGroupMembershipNumber_Type(Integer32):
    """Custom type gs2124IgmpProxyGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Gs2124IgmpProxyGroupMembershipNumber_Type.__name__ = "Integer32"
_Gs2124IgmpProxyGroupMembershipNumber_Object = MibScalar
gs2124IgmpProxyGroupMembershipNumber = _Gs2124IgmpProxyGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 8),
    _Gs2124IgmpProxyGroupMembershipNumber_Type()
)
gs2124IgmpProxyGroupMembershipNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupMembershipNumber.setStatus("current")
_Gs2124IgmpProxyGroupMembershipTable_Object = MibTable
gs2124IgmpProxyGroupMembershipTable = _Gs2124IgmpProxyGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 9)
)
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupMembershipTable.setStatus("current")
_Gs2124IgmpProxyGroupMembershipEntry_Object = MibTableRow
gs2124IgmpProxyGroupMembershipEntry = _Gs2124IgmpProxyGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 9, 1)
)
gs2124IgmpProxyGroupMembershipEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124IgmpProxyGroupNo"),
)
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupMembershipEntry.setStatus("current")


class _Gs2124IgmpProxyGroupNo_Type(Integer32):
    """Custom type gs2124IgmpProxyGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2124IgmpProxyGroupNo_Type.__name__ = "Integer32"
_Gs2124IgmpProxyGroupNo_Object = MibTableColumn
gs2124IgmpProxyGroupNo = _Gs2124IgmpProxyGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 9, 1, 1),
    _Gs2124IgmpProxyGroupNo_Type()
)
gs2124IgmpProxyGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupNo.setStatus("current")
_Gs2124IgmpProxyGroupAddress_Type = DisplayString
_Gs2124IgmpProxyGroupAddress_Object = MibTableColumn
gs2124IgmpProxyGroupAddress = _Gs2124IgmpProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 9, 1, 2),
    _Gs2124IgmpProxyGroupAddress_Type()
)
gs2124IgmpProxyGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupAddress.setStatus("current")


class _Gs2124IgmpProxyGroupVLANId_Type(Integer32):
    """Custom type gs2124IgmpProxyGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124IgmpProxyGroupVLANId_Type.__name__ = "Integer32"
_Gs2124IgmpProxyGroupVLANId_Object = MibTableColumn
gs2124IgmpProxyGroupVLANId = _Gs2124IgmpProxyGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 9, 1, 3),
    _Gs2124IgmpProxyGroupVLANId_Type()
)
gs2124IgmpProxyGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupVLANId.setStatus("current")
_Gs2124IgmpProxyGroupPortMembers_Type = DisplayString
_Gs2124IgmpProxyGroupPortMembers_Object = MibTableColumn
gs2124IgmpProxyGroupPortMembers = _Gs2124IgmpProxyGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 3, 9, 1, 4),
    _Gs2124IgmpProxyGroupPortMembers_Type()
)
gs2124IgmpProxyGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IgmpProxyGroupPortMembers.setStatus("current")
_Gs2124IGMPSnooping_ObjectIdentity = ObjectIdentity
gs2124IGMPSnooping = _Gs2124IGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4)
)


class _Gs2124IgmpSnoopingConfHostTimeout_Type(Integer32):
    """Custom type gs2124IgmpSnoopingConfHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124IgmpSnoopingConfHostTimeout_Type.__name__ = "Integer32"
_Gs2124IgmpSnoopingConfHostTimeout_Object = MibScalar
gs2124IgmpSnoopingConfHostTimeout = _Gs2124IgmpSnoopingConfHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 1),
    _Gs2124IgmpSnoopingConfHostTimeout_Type()
)
gs2124IgmpSnoopingConfHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingConfHostTimeout.setStatus("current")
_Gs2124IgmpSnoopingConfFastLeave_Type = DisplayString
_Gs2124IgmpSnoopingConfFastLeave_Object = MibScalar
gs2124IgmpSnoopingConfFastLeave = _Gs2124IgmpSnoopingConfFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 2),
    _Gs2124IgmpSnoopingConfFastLeave_Type()
)
gs2124IgmpSnoopingConfFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingConfFastLeave.setStatus("current")
_Gs2124IgmpSnoopingConfRouterPorts_Type = DisplayString
_Gs2124IgmpSnoopingConfRouterPorts_Object = MibScalar
gs2124IgmpSnoopingConfRouterPorts = _Gs2124IgmpSnoopingConfRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 3),
    _Gs2124IgmpSnoopingConfRouterPorts_Type()
)
gs2124IgmpSnoopingConfRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingConfRouterPorts.setStatus("current")


class _Gs2124IgmpSnoopingGroupMembershipNumber_Type(Integer32):
    """Custom type gs2124IgmpSnoopingGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Gs2124IgmpSnoopingGroupMembershipNumber_Type.__name__ = "Integer32"
_Gs2124IgmpSnoopingGroupMembershipNumber_Object = MibScalar
gs2124IgmpSnoopingGroupMembershipNumber = _Gs2124IgmpSnoopingGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 4),
    _Gs2124IgmpSnoopingGroupMembershipNumber_Type()
)
gs2124IgmpSnoopingGroupMembershipNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupMembershipNumber.setStatus("current")
_Gs2124IgmpSnoopingGroupMembershipTable_Object = MibTable
gs2124IgmpSnoopingGroupMembershipTable = _Gs2124IgmpSnoopingGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 5)
)
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupMembershipTable.setStatus("current")
_Gs2124IgmpSnoopingGroupMembershipEntry_Object = MibTableRow
gs2124IgmpSnoopingGroupMembershipEntry = _Gs2124IgmpSnoopingGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 5, 1)
)
gs2124IgmpSnoopingGroupMembershipEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124IgmpSnoopingGroupNo"),
)
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupMembershipEntry.setStatus("current")


class _Gs2124IgmpSnoopingGroupNo_Type(Integer32):
    """Custom type gs2124IgmpSnoopingGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2124IgmpSnoopingGroupNo_Type.__name__ = "Integer32"
_Gs2124IgmpSnoopingGroupNo_Object = MibTableColumn
gs2124IgmpSnoopingGroupNo = _Gs2124IgmpSnoopingGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 5, 1, 1),
    _Gs2124IgmpSnoopingGroupNo_Type()
)
gs2124IgmpSnoopingGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupNo.setStatus("current")
_Gs2124IgmpSnoopingGroupAddress_Type = DisplayString
_Gs2124IgmpSnoopingGroupAddress_Object = MibTableColumn
gs2124IgmpSnoopingGroupAddress = _Gs2124IgmpSnoopingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 5, 1, 2),
    _Gs2124IgmpSnoopingGroupAddress_Type()
)
gs2124IgmpSnoopingGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupAddress.setStatus("current")


class _Gs2124IgmpSnoopingGroupVLANId_Type(Integer32):
    """Custom type gs2124IgmpSnoopingGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124IgmpSnoopingGroupVLANId_Type.__name__ = "Integer32"
_Gs2124IgmpSnoopingGroupVLANId_Object = MibTableColumn
gs2124IgmpSnoopingGroupVLANId = _Gs2124IgmpSnoopingGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 5, 1, 3),
    _Gs2124IgmpSnoopingGroupVLANId_Type()
)
gs2124IgmpSnoopingGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupVLANId.setStatus("current")
_Gs2124IgmpSnoopingGroupPortMembers_Type = DisplayString
_Gs2124IgmpSnoopingGroupPortMembers_Object = MibTableColumn
gs2124IgmpSnoopingGroupPortMembers = _Gs2124IgmpSnoopingGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 4, 5, 1, 4),
    _Gs2124IgmpSnoopingGroupPortMembers_Type()
)
gs2124IgmpSnoopingGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124IgmpSnoopingGroupPortMembers.setStatus("current")
_Gs2124MVR_ObjectIdentity = ObjectIdentity
gs2124MVR = _Gs2124MVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5)
)


class _Gs2124MVRMode_Type(Integer32):
    """Custom type gs2124MVRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124MVRMode_Type.__name__ = "Integer32"
_Gs2124MVRMode_Object = MibScalar
gs2124MVRMode = _Gs2124MVRMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 1),
    _Gs2124MVRMode_Type()
)
gs2124MVRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVRMode.setStatus("current")


class _Gs2124MVRConfHostTimeout_Type(Integer32):
    """Custom type gs2124MVRConfHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2124MVRConfHostTimeout_Type.__name__ = "Integer32"
_Gs2124MVRConfHostTimeout_Object = MibScalar
gs2124MVRConfHostTimeout = _Gs2124MVRConfHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 2),
    _Gs2124MVRConfHostTimeout_Type()
)
gs2124MVRConfHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVRConfHostTimeout.setStatus("current")
_Gs2124MVRConfFastLeave_Type = DisplayString
_Gs2124MVRConfFastLeave_Object = MibScalar
gs2124MVRConfFastLeave = _Gs2124MVRConfFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 3),
    _Gs2124MVRConfFastLeave_Type()
)
gs2124MVRConfFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVRConfFastLeave.setStatus("current")
_Gs2124MVIDConf_ObjectIdentity = ObjectIdentity
gs2124MVIDConf = _Gs2124MVIDConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4)
)


class _Gs2124MVIDNumber_Type(Integer32):
    """Custom type gs2124MVIDNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124MVIDNumber_Type.__name__ = "Integer32"
_Gs2124MVIDNumber_Object = MibScalar
gs2124MVIDNumber = _Gs2124MVIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 1),
    _Gs2124MVIDNumber_Type()
)
gs2124MVIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MVIDNumber.setStatus("current")


class _Gs2124MVIDEntryCreate_Type(Integer32):
    """Custom type gs2124MVIDEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124MVIDEntryCreate_Type.__name__ = "Integer32"
_Gs2124MVIDEntryCreate_Object = MibScalar
gs2124MVIDEntryCreate = _Gs2124MVIDEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 2),
    _Gs2124MVIDEntryCreate_Type()
)
gs2124MVIDEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDEntryCreate.setStatus("current")
_Gs2124MVIDGroupTable_Object = MibTable
gs2124MVIDGroupTable = _Gs2124MVIDGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 3)
)
if mibBuilder.loadTexts:
    gs2124MVIDGroupTable.setStatus("current")
_Gs2124MVIDGroupEntry_Object = MibTableRow
gs2124MVIDGroupEntry = _Gs2124MVIDGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 3, 1)
)
gs2124MVIDGroupEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MVID"),
)
if mibBuilder.loadTexts:
    gs2124MVIDGroupEntry.setStatus("current")


class _Gs2124MVID_Type(Integer32):
    """Custom type gs2124MVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124MVID_Type.__name__ = "Integer32"
_Gs2124MVID_Object = MibTableColumn
gs2124MVID = _Gs2124MVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 3, 1, 1),
    _Gs2124MVID_Type()
)
gs2124MVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MVID.setStatus("current")
_Gs2124MVIDMemberPort_Type = DisplayString
_Gs2124MVIDMemberPort_Object = MibTableColumn
gs2124MVIDMemberPort = _Gs2124MVIDMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 3, 1, 2),
    _Gs2124MVIDMemberPort_Type()
)
gs2124MVIDMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDMemberPort.setStatus("current")
_Gs2124MVIDRouterPorts_Type = DisplayString
_Gs2124MVIDRouterPorts_Object = MibTableColumn
gs2124MVIDRouterPorts = _Gs2124MVIDRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 3, 1, 3),
    _Gs2124MVIDRouterPorts_Type()
)
gs2124MVIDRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDRouterPorts.setStatus("current")


class _Gs2124MVIDEntryAction_Type(Integer32):
    """Custom type gs2124MVIDEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2124MVIDEntryAction_Type.__name__ = "Integer32"
_Gs2124MVIDEntryAction_Object = MibTableColumn
gs2124MVIDEntryAction = _Gs2124MVIDEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 4, 3, 1, 4),
    _Gs2124MVIDEntryAction_Type()
)
gs2124MVIDEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDEntryAction.setStatus("current")
_Gs2124MVIDGroupAllowConf_ObjectIdentity = ObjectIdentity
gs2124MVIDGroupAllowConf = _Gs2124MVIDGroupAllowConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5)
)


class _Gs2124MVIDGroupAllowNumber_Type(Integer32):
    """Custom type gs2124MVIDGroupAllowNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Gs2124MVIDGroupAllowNumber_Type.__name__ = "Integer32"
_Gs2124MVIDGroupAllowNumber_Object = MibScalar
gs2124MVIDGroupAllowNumber = _Gs2124MVIDGroupAllowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 1),
    _Gs2124MVIDGroupAllowNumber_Type()
)
gs2124MVIDGroupAllowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowNumber.setStatus("current")


class _Gs2124MVIDGroupAllowEntryCreate_Type(Integer32):
    """Custom type gs2124MVIDGroupAllowEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124MVIDGroupAllowEntryCreate_Type.__name__ = "Integer32"
_Gs2124MVIDGroupAllowEntryCreate_Object = MibScalar
gs2124MVIDGroupAllowEntryCreate = _Gs2124MVIDGroupAllowEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 2),
    _Gs2124MVIDGroupAllowEntryCreate_Type()
)
gs2124MVIDGroupAllowEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowEntryCreate.setStatus("current")
_Gs2124MVIDGroupAllowTable_Object = MibTable
gs2124MVIDGroupAllowTable = _Gs2124MVIDGroupAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3)
)
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowTable.setStatus("current")
_Gs2124MVIDGroupAllowEntry_Object = MibTableRow
gs2124MVIDGroupAllowEntry = _Gs2124MVIDGroupAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3, 1)
)
gs2124MVIDGroupAllowEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MVIDGroupAllowNo"),
)
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowEntry.setStatus("current")


class _Gs2124MVIDGroupAllowNo_Type(Integer32):
    """Custom type gs2124MVIDGroupAllowNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2124MVIDGroupAllowNo_Type.__name__ = "Integer32"
_Gs2124MVIDGroupAllowNo_Object = MibTableColumn
gs2124MVIDGroupAllowNo = _Gs2124MVIDGroupAllowNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3, 1, 1),
    _Gs2124MVIDGroupAllowNo_Type()
)
gs2124MVIDGroupAllowNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowNo.setStatus("current")


class _Gs2124MVIDGroupAllowMvid_Type(Integer32):
    """Custom type gs2124MVIDGroupAllowMvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124MVIDGroupAllowMvid_Type.__name__ = "Integer32"
_Gs2124MVIDGroupAllowMvid_Object = MibTableColumn
gs2124MVIDGroupAllowMvid = _Gs2124MVIDGroupAllowMvid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3, 1, 2),
    _Gs2124MVIDGroupAllowMvid_Type()
)
gs2124MVIDGroupAllowMvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowMvid.setStatus("current")
_Gs2124MVIDGroupAllowStartAddress_Type = DisplayString
_Gs2124MVIDGroupAllowStartAddress_Object = MibTableColumn
gs2124MVIDGroupAllowStartAddress = _Gs2124MVIDGroupAllowStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3, 1, 3),
    _Gs2124MVIDGroupAllowStartAddress_Type()
)
gs2124MVIDGroupAllowStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowStartAddress.setStatus("current")
_Gs2124MVIDGroupAllowEndAddress_Type = DisplayString
_Gs2124MVIDGroupAllowEndAddress_Object = MibTableColumn
gs2124MVIDGroupAllowEndAddress = _Gs2124MVIDGroupAllowEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3, 1, 4),
    _Gs2124MVIDGroupAllowEndAddress_Type()
)
gs2124MVIDGroupAllowEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowEndAddress.setStatus("current")


class _Gs2124MVIDGroupAllowEntryAction_Type(Integer32):
    """Custom type gs2124MVIDGroupAllowEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Gs2124MVIDGroupAllowEntryAction_Type.__name__ = "Integer32"
_Gs2124MVIDGroupAllowEntryAction_Object = MibTableColumn
gs2124MVIDGroupAllowEntryAction = _Gs2124MVIDGroupAllowEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 5, 3, 1, 5),
    _Gs2124MVIDGroupAllowEntryAction_Type()
)
gs2124MVIDGroupAllowEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124MVIDGroupAllowEntryAction.setStatus("current")


class _Gs2124MVRGroupMembershipNumber_Type(Integer32):
    """Custom type gs2124MVRGroupMembershipNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Gs2124MVRGroupMembershipNumber_Type.__name__ = "Integer32"
_Gs2124MVRGroupMembershipNumber_Object = MibScalar
gs2124MVRGroupMembershipNumber = _Gs2124MVRGroupMembershipNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 6),
    _Gs2124MVRGroupMembershipNumber_Type()
)
gs2124MVRGroupMembershipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MVRGroupMembershipNumber.setStatus("current")
_Gs2124MVRGroupMembershipTable_Object = MibTable
gs2124MVRGroupMembershipTable = _Gs2124MVRGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 7)
)
if mibBuilder.loadTexts:
    gs2124MVRGroupMembershipTable.setStatus("current")
_Gs2124MVRGroupMembershipEntry_Object = MibTableRow
gs2124MVRGroupMembershipEntry = _Gs2124MVRGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 7, 1)
)
gs2124MVRGroupMembershipEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124MVRGroupNo"),
)
if mibBuilder.loadTexts:
    gs2124MVRGroupMembershipEntry.setStatus("current")


class _Gs2124MVRGroupNo_Type(Integer32):
    """Custom type gs2124MVRGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Gs2124MVRGroupNo_Type.__name__ = "Integer32"
_Gs2124MVRGroupNo_Object = MibTableColumn
gs2124MVRGroupNo = _Gs2124MVRGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 7, 1, 1),
    _Gs2124MVRGroupNo_Type()
)
gs2124MVRGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124MVRGroupNo.setStatus("current")
_Gs2124MVRGroupAddress_Type = DisplayString
_Gs2124MVRGroupAddress_Object = MibTableColumn
gs2124MVRGroupAddress = _Gs2124MVRGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 7, 1, 2),
    _Gs2124MVRGroupAddress_Type()
)
gs2124MVRGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MVRGroupAddress.setStatus("current")


class _Gs2124MVRGroupVLANId_Type(Integer32):
    """Custom type gs2124MVRGroupVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124MVRGroupVLANId_Type.__name__ = "Integer32"
_Gs2124MVRGroupVLANId_Object = MibTableColumn
gs2124MVRGroupVLANId = _Gs2124MVRGroupVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 7, 1, 3),
    _Gs2124MVRGroupVLANId_Type()
)
gs2124MVRGroupVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MVRGroupVLANId.setStatus("current")
_Gs2124MVRGroupPortMembers_Type = DisplayString
_Gs2124MVRGroupPortMembers_Object = MibTableColumn
gs2124MVRGroupPortMembers = _Gs2124MVRGroupPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 25, 5, 7, 1, 4),
    _Gs2124MVRGroupPortMembers_Type()
)
gs2124MVRGroupPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124MVRGroupPortMembers.setStatus("current")
_Gs2124DhcpSnooping_ObjectIdentity = ObjectIdentity
gs2124DhcpSnooping = _Gs2124DhcpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26)
)


class _Gs2124DhcpSnoopingState_Type(Integer32):
    """Custom type gs2124DhcpSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DhcpSnoopingState_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingState_Object = MibScalar
gs2124DhcpSnoopingState = _Gs2124DhcpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 1),
    _Gs2124DhcpSnoopingState_Type()
)
gs2124DhcpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingState.setStatus("current")
_Gs2124DhcpSnoopingInfo_ObjectIdentity = ObjectIdentity
gs2124DhcpSnoopingInfo = _Gs2124DhcpSnoopingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2)
)


class _Gs2124DhcpSnoopingCreate_Type(Integer32):
    """Custom type gs2124DhcpSnoopingCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DhcpSnoopingCreate_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingCreate_Object = MibScalar
gs2124DhcpSnoopingCreate = _Gs2124DhcpSnoopingCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 1),
    _Gs2124DhcpSnoopingCreate_Type()
)
gs2124DhcpSnoopingCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingCreate.setStatus("current")
_Gs2124DhcpSnoopingTable_Object = MibTable
gs2124DhcpSnoopingTable = _Gs2124DhcpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2)
)
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingTable.setStatus("current")
_Gs2124DhcpSnoopingEntry_Object = MibTableRow
gs2124DhcpSnoopingEntry = _Gs2124DhcpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1)
)
gs2124DhcpSnoopingEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124DhcpSnoopingIndex"),
)
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingEntry.setStatus("current")


class _Gs2124DhcpSnoopingIndex_Type(Integer32):
    """Custom type gs2124DhcpSnoopingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Gs2124DhcpSnoopingIndex_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingIndex_Object = MibTableColumn
gs2124DhcpSnoopingIndex = _Gs2124DhcpSnoopingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 1),
    _Gs2124DhcpSnoopingIndex_Type()
)
gs2124DhcpSnoopingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingIndex.setStatus("current")


class _Gs2124DhcpSnoopingVID_Type(Integer32):
    """Custom type gs2124DhcpSnoopingVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124DhcpSnoopingVID_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingVID_Object = MibTableColumn
gs2124DhcpSnoopingVID = _Gs2124DhcpSnoopingVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 2),
    _Gs2124DhcpSnoopingVID_Type()
)
gs2124DhcpSnoopingVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingVID.setStatus("current")


class _Gs2124DhcpSnoopingTrustPort1_Type(Integer32):
    """Custom type gs2124DhcpSnoopingTrustPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124DhcpSnoopingTrustPort1_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingTrustPort1_Object = MibTableColumn
gs2124DhcpSnoopingTrustPort1 = _Gs2124DhcpSnoopingTrustPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 3),
    _Gs2124DhcpSnoopingTrustPort1_Type()
)
gs2124DhcpSnoopingTrustPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingTrustPort1.setStatus("current")


class _Gs2124DhcpSnoopingTrustPort2_Type(Integer32):
    """Custom type gs2124DhcpSnoopingTrustPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124DhcpSnoopingTrustPort2_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingTrustPort2_Object = MibTableColumn
gs2124DhcpSnoopingTrustPort2 = _Gs2124DhcpSnoopingTrustPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 4),
    _Gs2124DhcpSnoopingTrustPort2_Type()
)
gs2124DhcpSnoopingTrustPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingTrustPort2.setStatus("current")
_Gs2124DhcpSnoopingServerIP_Type = IpAddress
_Gs2124DhcpSnoopingServerIP_Object = MibTableColumn
gs2124DhcpSnoopingServerIP = _Gs2124DhcpSnoopingServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 5),
    _Gs2124DhcpSnoopingServerIP_Type()
)
gs2124DhcpSnoopingServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingServerIP.setStatus("current")


class _Gs2124DhcpSnoopingOption82_Type(Integer32):
    """Custom type gs2124DhcpSnoopingOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DhcpSnoopingOption82_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingOption82_Object = MibTableColumn
gs2124DhcpSnoopingOption82 = _Gs2124DhcpSnoopingOption82_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 6),
    _Gs2124DhcpSnoopingOption82_Type()
)
gs2124DhcpSnoopingOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingOption82.setStatus("current")


class _Gs2124DhcpSnoopingAction_Type(Integer32):
    """Custom type gs2124DhcpSnoopingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124DhcpSnoopingAction_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingAction_Object = MibTableColumn
gs2124DhcpSnoopingAction = _Gs2124DhcpSnoopingAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 7),
    _Gs2124DhcpSnoopingAction_Type()
)
gs2124DhcpSnoopingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingAction.setStatus("current")


class _Gs2124DhcpSnoopingEntryAction_Type(Integer32):
    """Custom type gs2124DhcpSnoopingEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124DhcpSnoopingEntryAction_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingEntryAction_Object = MibTableColumn
gs2124DhcpSnoopingEntryAction = _Gs2124DhcpSnoopingEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 2, 1, 8),
    _Gs2124DhcpSnoopingEntryAction_Type()
)
gs2124DhcpSnoopingEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingEntryAction.setStatus("current")
_Gs2124DhcpSnoopingDefaultData_ObjectIdentity = ObjectIdentity
gs2124DhcpSnoopingDefaultData = _Gs2124DhcpSnoopingDefaultData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3)
)


class _Gs2124DhcpSnoopingDefaultVID_Type(Integer32):
    """Custom type gs2124DhcpSnoopingDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124DhcpSnoopingDefaultVID_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingDefaultVID_Object = MibScalar
gs2124DhcpSnoopingDefaultVID = _Gs2124DhcpSnoopingDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 1),
    _Gs2124DhcpSnoopingDefaultVID_Type()
)
gs2124DhcpSnoopingDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultVID.setStatus("current")


class _Gs2124DhcpSnoopingDefaultTrustPort1_Type(Integer32):
    """Custom type gs2124DhcpSnoopingDefaultTrustPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124DhcpSnoopingDefaultTrustPort1_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingDefaultTrustPort1_Object = MibScalar
gs2124DhcpSnoopingDefaultTrustPort1 = _Gs2124DhcpSnoopingDefaultTrustPort1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 2),
    _Gs2124DhcpSnoopingDefaultTrustPort1_Type()
)
gs2124DhcpSnoopingDefaultTrustPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultTrustPort1.setStatus("current")


class _Gs2124DhcpSnoopingDefaultTrustPort2_Type(Integer32):
    """Custom type gs2124DhcpSnoopingDefaultTrustPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Gs2124DhcpSnoopingDefaultTrustPort2_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingDefaultTrustPort2_Object = MibScalar
gs2124DhcpSnoopingDefaultTrustPort2 = _Gs2124DhcpSnoopingDefaultTrustPort2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 3),
    _Gs2124DhcpSnoopingDefaultTrustPort2_Type()
)
gs2124DhcpSnoopingDefaultTrustPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultTrustPort2.setStatus("current")
_Gs2124DhcpSnoopingDefaultServerIP_Type = IpAddress
_Gs2124DhcpSnoopingDefaultServerIP_Object = MibScalar
gs2124DhcpSnoopingDefaultServerIP = _Gs2124DhcpSnoopingDefaultServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 4),
    _Gs2124DhcpSnoopingDefaultServerIP_Type()
)
gs2124DhcpSnoopingDefaultServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultServerIP.setStatus("current")


class _Gs2124DhcpSnoopingDefaultOption82_Type(Integer32):
    """Custom type gs2124DhcpSnoopingDefaultOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124DhcpSnoopingDefaultOption82_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingDefaultOption82_Object = MibScalar
gs2124DhcpSnoopingDefaultOption82 = _Gs2124DhcpSnoopingDefaultOption82_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 5),
    _Gs2124DhcpSnoopingDefaultOption82_Type()
)
gs2124DhcpSnoopingDefaultOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultOption82.setStatus("current")


class _Gs2124DhcpSnoopingDefaultAction_Type(Integer32):
    """Custom type gs2124DhcpSnoopingDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124DhcpSnoopingDefaultAction_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingDefaultAction_Object = MibScalar
gs2124DhcpSnoopingDefaultAction = _Gs2124DhcpSnoopingDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 6),
    _Gs2124DhcpSnoopingDefaultAction_Type()
)
gs2124DhcpSnoopingDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultAction.setStatus("current")


class _Gs2124DhcpSnoopingDefaultEntryAction_Type(Integer32):
    """Custom type gs2124DhcpSnoopingDefaultEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Gs2124DhcpSnoopingDefaultEntryAction_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingDefaultEntryAction_Object = MibScalar
gs2124DhcpSnoopingDefaultEntryAction = _Gs2124DhcpSnoopingDefaultEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 2, 3, 7),
    _Gs2124DhcpSnoopingDefaultEntryAction_Type()
)
gs2124DhcpSnoopingDefaultEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingDefaultEntryAction.setStatus("current")
_Gs2124DhcpSnoopingClientTable_Object = MibTable
gs2124DhcpSnoopingClientTable = _Gs2124DhcpSnoopingClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3)
)
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientTable.setStatus("current")
_Gs2124DhcpSnoopingClientEntry_Object = MibTableRow
gs2124DhcpSnoopingClientEntry = _Gs2124DhcpSnoopingClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1)
)
gs2124DhcpSnoopingClientEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124DhcpSnoopingClientIndex"),
)
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientEntry.setStatus("current")


class _Gs2124DhcpSnoopingClientIndex_Type(Integer32):
    """Custom type gs2124DhcpSnoopingClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Gs2124DhcpSnoopingClientIndex_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingClientIndex_Object = MibTableColumn
gs2124DhcpSnoopingClientIndex = _Gs2124DhcpSnoopingClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1, 1),
    _Gs2124DhcpSnoopingClientIndex_Type()
)
gs2124DhcpSnoopingClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientIndex.setStatus("current")
_Gs2124DhcpSnoopingClientMac_Type = DisplayString
_Gs2124DhcpSnoopingClientMac_Object = MibTableColumn
gs2124DhcpSnoopingClientMac = _Gs2124DhcpSnoopingClientMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1, 2),
    _Gs2124DhcpSnoopingClientMac_Type()
)
gs2124DhcpSnoopingClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientMac.setStatus("current")


class _Gs2124DhcpSnoopingClientVID_Type(Integer32):
    """Custom type gs2124DhcpSnoopingClientVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124DhcpSnoopingClientVID_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingClientVID_Object = MibTableColumn
gs2124DhcpSnoopingClientVID = _Gs2124DhcpSnoopingClientVID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1, 3),
    _Gs2124DhcpSnoopingClientVID_Type()
)
gs2124DhcpSnoopingClientVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientVID.setStatus("current")


class _Gs2124DhcpSnoopingClientPort_Type(Integer32):
    """Custom type gs2124DhcpSnoopingClientPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Gs2124DhcpSnoopingClientPort_Type.__name__ = "Integer32"
_Gs2124DhcpSnoopingClientPort_Object = MibTableColumn
gs2124DhcpSnoopingClientPort = _Gs2124DhcpSnoopingClientPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1, 4),
    _Gs2124DhcpSnoopingClientPort_Type()
)
gs2124DhcpSnoopingClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientPort.setStatus("current")
_Gs2124DhcpSnoopingClientIP_Type = IpAddress
_Gs2124DhcpSnoopingClientIP_Object = MibTableColumn
gs2124DhcpSnoopingClientIP = _Gs2124DhcpSnoopingClientIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1, 5),
    _Gs2124DhcpSnoopingClientIP_Type()
)
gs2124DhcpSnoopingClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientIP.setStatus("current")
_Gs2124DhcpSnoopingClientLease_Type = DisplayString
_Gs2124DhcpSnoopingClientLease_Object = MibTableColumn
gs2124DhcpSnoopingClientLease = _Gs2124DhcpSnoopingClientLease_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 26, 3, 1, 6),
    _Gs2124DhcpSnoopingClientLease_Type()
)
gs2124DhcpSnoopingClientLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124DhcpSnoopingClientLease.setStatus("current")
_Gs2124mstpMIB_ObjectIdentity = ObjectIdentity
gs2124mstpMIB = _Gs2124mstpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200)
)
_Gs2124mstpInstanceView_ObjectIdentity = ObjectIdentity
gs2124mstpInstanceView = _Gs2124mstpInstanceView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1)
)


class _Gs2124mstpInstanceEntryCreate_Type(Integer32):
    """Custom type gs2124mstpInstanceEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Gs2124mstpInstanceEntryCreate_Type.__name__ = "Integer32"
_Gs2124mstpInstanceEntryCreate_Object = MibScalar
gs2124mstpInstanceEntryCreate = _Gs2124mstpInstanceEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 1),
    _Gs2124mstpInstanceEntryCreate_Type()
)
gs2124mstpInstanceEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpInstanceEntryCreate.setStatus("current")
_Gs2124mstpInstanceViewTable_Object = MibTable
gs2124mstpInstanceViewTable = _Gs2124mstpInstanceViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 2)
)
if mibBuilder.loadTexts:
    gs2124mstpInstanceViewTable.setStatus("current")
_Gs2124mstpInstanceViewEntry_Object = MibTableRow
gs2124mstpInstanceViewEntry = _Gs2124mstpInstanceViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 2, 1)
)
gs2124mstpInstanceViewEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpInstanceViewIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpInstanceViewEntry.setStatus("current")


class _Gs2124mstpInstanceViewIndex_Type(Integer32):
    """Custom type gs2124mstpInstanceViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_Gs2124mstpInstanceViewIndex_Type.__name__ = "Integer32"
_Gs2124mstpInstanceViewIndex_Object = MibTableColumn
gs2124mstpInstanceViewIndex = _Gs2124mstpInstanceViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 2, 1, 1),
    _Gs2124mstpInstanceViewIndex_Type()
)
gs2124mstpInstanceViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpInstanceViewIndex.setStatus("current")
_Gs2124mstpInstanceViewInstance_Type = Integer32
_Gs2124mstpInstanceViewInstance_Object = MibTableColumn
gs2124mstpInstanceViewInstance = _Gs2124mstpInstanceViewInstance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 2, 1, 2),
    _Gs2124mstpInstanceViewInstance_Type()
)
gs2124mstpInstanceViewInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpInstanceViewInstance.setStatus("current")
_Gs2124mstpInstanceViewCorrespondingVlans_Type = DisplayString
_Gs2124mstpInstanceViewCorrespondingVlans_Object = MibTableColumn
gs2124mstpInstanceViewCorrespondingVlans = _Gs2124mstpInstanceViewCorrespondingVlans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 2, 1, 3),
    _Gs2124mstpInstanceViewCorrespondingVlans_Type()
)
gs2124mstpInstanceViewCorrespondingVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpInstanceViewCorrespondingVlans.setStatus("current")


class _Gs2124mstpInstanceViewEntryAction_Type(Integer32):
    """Custom type gs2124mstpInstanceViewEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Gs2124mstpInstanceViewEntryAction_Type.__name__ = "Integer32"
_Gs2124mstpInstanceViewEntryAction_Object = MibTableColumn
gs2124mstpInstanceViewEntryAction = _Gs2124mstpInstanceViewEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 1, 2, 1, 4),
    _Gs2124mstpInstanceViewEntryAction_Type()
)
gs2124mstpInstanceViewEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpInstanceViewEntryAction.setStatus("current")
_Gs2124mstpGen_ObjectIdentity = ObjectIdentity
gs2124mstpGen = _Gs2124mstpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2)
)


class _Gs2124mstpGenSupported_Type(Integer32):
    """Custom type gs2124mstpGenSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2124mstpGenSupported_Type.__name__ = "Integer32"
_Gs2124mstpGenSupported_Object = MibScalar
gs2124mstpGenSupported = _Gs2124mstpGenSupported_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 1),
    _Gs2124mstpGenSupported_Type()
)
gs2124mstpGenSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpGenSupported.setStatus("current")


class _Gs2124mstpGenVersion_Type(Integer32):
    """Custom type gs2124mstpGenVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_Gs2124mstpGenVersion_Type.__name__ = "Integer32"
_Gs2124mstpGenVersion_Object = MibScalar
gs2124mstpGenVersion = _Gs2124mstpGenVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 2),
    _Gs2124mstpGenVersion_Type()
)
gs2124mstpGenVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpGenVersion.setStatus("current")
_Gs2124mstpGenCfgIdFmtSel_Type = Integer32
_Gs2124mstpGenCfgIdFmtSel_Object = MibScalar
gs2124mstpGenCfgIdFmtSel = _Gs2124mstpGenCfgIdFmtSel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 3),
    _Gs2124mstpGenCfgIdFmtSel_Type()
)
gs2124mstpGenCfgIdFmtSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCfgIdFmtSel.setStatus("current")


class _Gs2124mstpGenCfgIdName_Type(DisplayString):
    """Custom type gs2124mstpGenCfgIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_Gs2124mstpGenCfgIdName_Type.__name__ = "DisplayString"
_Gs2124mstpGenCfgIdName_Object = MibScalar
gs2124mstpGenCfgIdName = _Gs2124mstpGenCfgIdName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 4),
    _Gs2124mstpGenCfgIdName_Type()
)
gs2124mstpGenCfgIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpGenCfgIdName.setStatus("current")


class _Gs2124mstpGenCfgIdRevLevel_Type(Integer32):
    """Custom type gs2124mstpGenCfgIdRevLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Gs2124mstpGenCfgIdRevLevel_Type.__name__ = "Integer32"
_Gs2124mstpGenCfgIdRevLevel_Object = MibScalar
gs2124mstpGenCfgIdRevLevel = _Gs2124mstpGenCfgIdRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 5),
    _Gs2124mstpGenCfgIdRevLevel_Type()
)
gs2124mstpGenCfgIdRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpGenCfgIdRevLevel.setStatus("current")


class _Gs2124mstpGenBridgeMaxAge_Type(Integer32):
    """Custom type gs2124mstpGenBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Gs2124mstpGenBridgeMaxAge_Type.__name__ = "Integer32"
_Gs2124mstpGenBridgeMaxAge_Object = MibScalar
gs2124mstpGenBridgeMaxAge = _Gs2124mstpGenBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 6),
    _Gs2124mstpGenBridgeMaxAge_Type()
)
gs2124mstpGenBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenBridgeMaxAge.setStatus("current")
_Gs2124mstpGenBridgeFwdDelay_Type = Integer32
_Gs2124mstpGenBridgeFwdDelay_Object = MibScalar
gs2124mstpGenBridgeFwdDelay = _Gs2124mstpGenBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 7),
    _Gs2124mstpGenBridgeFwdDelay_Type()
)
gs2124mstpGenBridgeFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenBridgeFwdDelay.setStatus("current")
_Gs2124mstpGenBridgeMaxHops_Type = Integer32
_Gs2124mstpGenBridgeMaxHops_Object = MibScalar
gs2124mstpGenBridgeMaxHops = _Gs2124mstpGenBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 8),
    _Gs2124mstpGenBridgeMaxHops_Type()
)
gs2124mstpGenBridgeMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenBridgeMaxHops.setStatus("current")
_Gs2124mstpGenInstancePriority_Type = Integer32
_Gs2124mstpGenInstancePriority_Object = MibScalar
gs2124mstpGenInstancePriority = _Gs2124mstpGenInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 9),
    _Gs2124mstpGenInstancePriority_Type()
)
gs2124mstpGenInstancePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenInstancePriority.setStatus("current")
_Gs2124mstpGenCistRootPriority_Type = Integer32
_Gs2124mstpGenCistRootPriority_Object = MibScalar
gs2124mstpGenCistRootPriority = _Gs2124mstpGenCistRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 10),
    _Gs2124mstpGenCistRootPriority_Type()
)
gs2124mstpGenCistRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistRootPriority.setStatus("current")
_Gs2124mstpGenCistRootMac_Type = MacAddress
_Gs2124mstpGenCistRootMac_Object = MibScalar
gs2124mstpGenCistRootMac = _Gs2124mstpGenCistRootMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 11),
    _Gs2124mstpGenCistRootMac_Type()
)
gs2124mstpGenCistRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistRootMac.setStatus("current")
_Gs2124mstpGenCistExtRootPathCost_Type = Integer32
_Gs2124mstpGenCistExtRootPathCost_Object = MibScalar
gs2124mstpGenCistExtRootPathCost = _Gs2124mstpGenCistExtRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 12),
    _Gs2124mstpGenCistExtRootPathCost_Type()
)
gs2124mstpGenCistExtRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistExtRootPathCost.setStatus("current")
_Gs2124mstpGenCistRootPortId_Type = Integer32
_Gs2124mstpGenCistRootPortId_Object = MibScalar
gs2124mstpGenCistRootPortId = _Gs2124mstpGenCistRootPortId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 13),
    _Gs2124mstpGenCistRootPortId_Type()
)
gs2124mstpGenCistRootPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistRootPortId.setStatus("current")
_Gs2124mstpGenCistRegionalRootPriority_Type = Integer32
_Gs2124mstpGenCistRegionalRootPriority_Object = MibScalar
gs2124mstpGenCistRegionalRootPriority = _Gs2124mstpGenCistRegionalRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 14),
    _Gs2124mstpGenCistRegionalRootPriority_Type()
)
gs2124mstpGenCistRegionalRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistRegionalRootPriority.setStatus("current")
_Gs2124mstpGenCistRegionalRootMac_Type = MacAddress
_Gs2124mstpGenCistRegionalRootMac_Object = MibScalar
gs2124mstpGenCistRegionalRootMac = _Gs2124mstpGenCistRegionalRootMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 15),
    _Gs2124mstpGenCistRegionalRootMac_Type()
)
gs2124mstpGenCistRegionalRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistRegionalRootMac.setStatus("current")
_Gs2124mstpGenCistInternalRootPathCost_Type = Integer32
_Gs2124mstpGenCistInternalRootPathCost_Object = MibScalar
gs2124mstpGenCistInternalRootPathCost = _Gs2124mstpGenCistInternalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 16),
    _Gs2124mstpGenCistInternalRootPathCost_Type()
)
gs2124mstpGenCistInternalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistInternalRootPathCost.setStatus("current")
_Gs2124mstpGenCistCurrentMaxAge_Type = Integer32
_Gs2124mstpGenCistCurrentMaxAge_Object = MibScalar
gs2124mstpGenCistCurrentMaxAge = _Gs2124mstpGenCistCurrentMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 17),
    _Gs2124mstpGenCistCurrentMaxAge_Type()
)
gs2124mstpGenCistCurrentMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistCurrentMaxAge.setStatus("current")
_Gs2124mstpGenCistCurrentFwdDelay_Type = Integer32
_Gs2124mstpGenCistCurrentFwdDelay_Object = MibScalar
gs2124mstpGenCistCurrentFwdDelay = _Gs2124mstpGenCistCurrentFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 18),
    _Gs2124mstpGenCistCurrentFwdDelay_Type()
)
gs2124mstpGenCistCurrentFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenCistCurrentFwdDelay.setStatus("current")
_Gs2124mstpGenTimeSinceLastTopoChange_Type = Integer32
_Gs2124mstpGenTimeSinceLastTopoChange_Object = MibScalar
gs2124mstpGenTimeSinceLastTopoChange = _Gs2124mstpGenTimeSinceLastTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 19),
    _Gs2124mstpGenTimeSinceLastTopoChange_Type()
)
gs2124mstpGenTimeSinceLastTopoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenTimeSinceLastTopoChange.setStatus("current")
_Gs2124mstpGenTopoChangeCount_Type = Integer32
_Gs2124mstpGenTopoChangeCount_Object = MibScalar
gs2124mstpGenTopoChangeCount = _Gs2124mstpGenTopoChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 2, 20),
    _Gs2124mstpGenTopoChangeCount_Type()
)
gs2124mstpGenTopoChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpGenTopoChangeCount.setStatus("current")
_Gs2124mstpMstiStatusTable_Object = MibTable
gs2124mstpMstiStatusTable = _Gs2124mstpMstiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3)
)
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusTable.setStatus("current")
_Gs2124mstpMstiStatusEntry_Object = MibTableRow
gs2124mstpMstiStatusEntry = _Gs2124mstpMstiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1)
)
gs2124mstpMstiStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpMstiStatusInstanceIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusEntry.setStatus("current")


class _Gs2124mstpMstiStatusInstanceIndex_Type(Integer32):
    """Custom type gs2124mstpMstiStatusInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpMstiStatusInstanceIndex_Type.__name__ = "Integer32"
_Gs2124mstpMstiStatusInstanceIndex_Object = MibTableColumn
gs2124mstpMstiStatusInstanceIndex = _Gs2124mstpMstiStatusInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 1),
    _Gs2124mstpMstiStatusInstanceIndex_Type()
)
gs2124mstpMstiStatusInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusInstanceIndex.setStatus("current")
_Gs2124mstpMstiStatusState_Type = DisplayString
_Gs2124mstpMstiStatusState_Object = MibTableColumn
gs2124mstpMstiStatusState = _Gs2124mstpMstiStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 2),
    _Gs2124mstpMstiStatusState_Type()
)
gs2124mstpMstiStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusState.setStatus("current")
_Gs2124mstpMstiStatusPriority_Type = Integer32
_Gs2124mstpMstiStatusPriority_Object = MibTableColumn
gs2124mstpMstiStatusPriority = _Gs2124mstpMstiStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 3),
    _Gs2124mstpMstiStatusPriority_Type()
)
gs2124mstpMstiStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusPriority.setStatus("current")
_Gs2124mstpMstiStatusBridgeMac_Type = MacAddress
_Gs2124mstpMstiStatusBridgeMac_Object = MibTableColumn
gs2124mstpMstiStatusBridgeMac = _Gs2124mstpMstiStatusBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 4),
    _Gs2124mstpMstiStatusBridgeMac_Type()
)
gs2124mstpMstiStatusBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusBridgeMac.setStatus("current")
_Gs2124mstpMstiStatusRegionalRootPriority_Type = Integer32
_Gs2124mstpMstiStatusRegionalRootPriority_Object = MibTableColumn
gs2124mstpMstiStatusRegionalRootPriority = _Gs2124mstpMstiStatusRegionalRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 5),
    _Gs2124mstpMstiStatusRegionalRootPriority_Type()
)
gs2124mstpMstiStatusRegionalRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusRegionalRootPriority.setStatus("current")
_Gs2124mstpMstiStatusRegionalRootMac_Type = MacAddress
_Gs2124mstpMstiStatusRegionalRootMac_Object = MibTableColumn
gs2124mstpMstiStatusRegionalRootMac = _Gs2124mstpMstiStatusRegionalRootMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 6),
    _Gs2124mstpMstiStatusRegionalRootMac_Type()
)
gs2124mstpMstiStatusRegionalRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusRegionalRootMac.setStatus("current")
_Gs2124mstpMstiStatusInternalRootPathCost_Type = Integer32
_Gs2124mstpMstiStatusInternalRootPathCost_Object = MibTableColumn
gs2124mstpMstiStatusInternalRootPathCost = _Gs2124mstpMstiStatusInternalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 7),
    _Gs2124mstpMstiStatusInternalRootPathCost_Type()
)
gs2124mstpMstiStatusInternalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusInternalRootPathCost.setStatus("current")
_Gs2124mstpMstiStatusRootPortId_Type = Integer32
_Gs2124mstpMstiStatusRootPortId_Object = MibTableColumn
gs2124mstpMstiStatusRootPortId = _Gs2124mstpMstiStatusRootPortId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 8),
    _Gs2124mstpMstiStatusRootPortId_Type()
)
gs2124mstpMstiStatusRootPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusRootPortId.setStatus("current")
_Gs2124mstpMstiStatusTimeSinceLastTopoChg_Type = Integer32
_Gs2124mstpMstiStatusTimeSinceLastTopoChg_Object = MibTableColumn
gs2124mstpMstiStatusTimeSinceLastTopoChg = _Gs2124mstpMstiStatusTimeSinceLastTopoChg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 9),
    _Gs2124mstpMstiStatusTimeSinceLastTopoChg_Type()
)
gs2124mstpMstiStatusTimeSinceLastTopoChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusTimeSinceLastTopoChg.setStatus("current")
_Gs2124mstpMstiStatusTopochgcount_Type = Integer32
_Gs2124mstpMstiStatusTopochgcount_Object = MibTableColumn
gs2124mstpMstiStatusTopochgcount = _Gs2124mstpMstiStatusTopochgcount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 3, 1, 10),
    _Gs2124mstpMstiStatusTopochgcount_Type()
)
gs2124mstpMstiStatusTopochgcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiStatusTopochgcount.setStatus("current")
_Gs2124mstpPortCfg_ObjectIdentity = ObjectIdentity
gs2124mstpPortCfg = _Gs2124mstpPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4)
)
_Gs2124mstpCistPortCfgTable_Object = MibTable
gs2124mstpCistPortCfgTable = _Gs2124mstpCistPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1)
)
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgTable.setStatus("current")
_Gs2124mstpCistPortCfgEntry_Object = MibTableRow
gs2124mstpCistPortCfgEntry = _Gs2124mstpCistPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1)
)
gs2124mstpCistPortCfgEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpCistPortCfgPortIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgEntry.setStatus("current")


class _Gs2124mstpCistPortCfgPortIndex_Type(Integer32):
    """Custom type gs2124mstpCistPortCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpCistPortCfgPortIndex_Type.__name__ = "Integer32"
_Gs2124mstpCistPortCfgPortIndex_Object = MibTableColumn
gs2124mstpCistPortCfgPortIndex = _Gs2124mstpCistPortCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 1),
    _Gs2124mstpCistPortCfgPortIndex_Type()
)
gs2124mstpCistPortCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgPortIndex.setStatus("current")
_Gs2124mstpCistPortCfgPathCost_Type = Integer32
_Gs2124mstpCistPortCfgPathCost_Object = MibTableColumn
gs2124mstpCistPortCfgPathCost = _Gs2124mstpCistPortCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 2),
    _Gs2124mstpCistPortCfgPathCost_Type()
)
gs2124mstpCistPortCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgPathCost.setStatus("current")
_Gs2124mstpCistPortCfgPriority_Type = Integer32
_Gs2124mstpCistPortCfgPriority_Object = MibTableColumn
gs2124mstpCistPortCfgPriority = _Gs2124mstpCistPortCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 3),
    _Gs2124mstpCistPortCfgPriority_Type()
)
gs2124mstpCistPortCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgPriority.setStatus("current")
_Gs2124mstpCistPortCfgHelloTime_Type = Integer32
_Gs2124mstpCistPortCfgHelloTime_Object = MibTableColumn
gs2124mstpCistPortCfgHelloTime = _Gs2124mstpCistPortCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 4),
    _Gs2124mstpCistPortCfgHelloTime_Type()
)
gs2124mstpCistPortCfgHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgHelloTime.setStatus("current")
_Gs2124mstpCistPortCfgAdminEdge_Type = Integer32
_Gs2124mstpCistPortCfgAdminEdge_Object = MibTableColumn
gs2124mstpCistPortCfgAdminEdge = _Gs2124mstpCistPortCfgAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 5),
    _Gs2124mstpCistPortCfgAdminEdge_Type()
)
gs2124mstpCistPortCfgAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgAdminEdge.setStatus("current")
_Gs2124mstpCistPortCfgP2P_Type = Integer32
_Gs2124mstpCistPortCfgP2P_Object = MibTableColumn
gs2124mstpCistPortCfgP2P = _Gs2124mstpCistPortCfgP2P_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 6),
    _Gs2124mstpCistPortCfgP2P_Type()
)
gs2124mstpCistPortCfgP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgP2P.setStatus("current")
_Gs2124mstpCistPortCfgRestrictedRole_Type = Integer32
_Gs2124mstpCistPortCfgRestrictedRole_Object = MibTableColumn
gs2124mstpCistPortCfgRestrictedRole = _Gs2124mstpCistPortCfgRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 7),
    _Gs2124mstpCistPortCfgRestrictedRole_Type()
)
gs2124mstpCistPortCfgRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgRestrictedRole.setStatus("current")
_Gs2124mstpCistPortCfgRestrictedTcn_Type = Integer32
_Gs2124mstpCistPortCfgRestrictedTcn_Object = MibTableColumn
gs2124mstpCistPortCfgRestrictedTcn = _Gs2124mstpCistPortCfgRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 8),
    _Gs2124mstpCistPortCfgRestrictedTcn_Type()
)
gs2124mstpCistPortCfgRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgRestrictedTcn.setStatus("current")
_Gs2124mstpCistPortCfgMigrationCheck_Type = Integer32
_Gs2124mstpCistPortCfgMigrationCheck_Object = MibTableColumn
gs2124mstpCistPortCfgMigrationCheck = _Gs2124mstpCistPortCfgMigrationCheck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 1, 1, 9),
    _Gs2124mstpCistPortCfgMigrationCheck_Type()
)
gs2124mstpCistPortCfgMigrationCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCistPortCfgMigrationCheck.setStatus("current")
_Gs2124mstpMstiPortCfgTable_Object = MibTable
gs2124mstpMstiPortCfgTable = _Gs2124mstpMstiPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 2)
)
if mibBuilder.loadTexts:
    gs2124mstpMstiPortCfgTable.setStatus("current")
_Gs2124mstpMstiPortCfgEntry_Object = MibTableRow
gs2124mstpMstiPortCfgEntry = _Gs2124mstpMstiPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 2, 1)
)
gs2124mstpMstiPortCfgEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpMstiPortCfgInstanceIndex"),
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpMstiPortCfgPortIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpMstiPortCfgEntry.setStatus("current")


class _Gs2124mstpMstiPortCfgInstanceIndex_Type(Integer32):
    """Custom type gs2124mstpMstiPortCfgInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpMstiPortCfgInstanceIndex_Type.__name__ = "Integer32"
_Gs2124mstpMstiPortCfgInstanceIndex_Object = MibTableColumn
gs2124mstpMstiPortCfgInstanceIndex = _Gs2124mstpMstiPortCfgInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 2, 1, 1),
    _Gs2124mstpMstiPortCfgInstanceIndex_Type()
)
gs2124mstpMstiPortCfgInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortCfgInstanceIndex.setStatus("current")


class _Gs2124mstpMstiPortCfgPortIndex_Type(Integer32):
    """Custom type gs2124mstpMstiPortCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpMstiPortCfgPortIndex_Type.__name__ = "Integer32"
_Gs2124mstpMstiPortCfgPortIndex_Object = MibTableColumn
gs2124mstpMstiPortCfgPortIndex = _Gs2124mstpMstiPortCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 2, 1, 2),
    _Gs2124mstpMstiPortCfgPortIndex_Type()
)
gs2124mstpMstiPortCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortCfgPortIndex.setStatus("current")
_Gs2124mstpMstiPortCfgPathCost_Type = Integer32
_Gs2124mstpMstiPortCfgPathCost_Object = MibTableColumn
gs2124mstpMstiPortCfgPathCost = _Gs2124mstpMstiPortCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 2, 1, 3),
    _Gs2124mstpMstiPortCfgPathCost_Type()
)
gs2124mstpMstiPortCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortCfgPathCost.setStatus("current")
_Gs2124mstpMstiPortCfgPriority_Type = Integer32
_Gs2124mstpMstiPortCfgPriority_Object = MibTableColumn
gs2124mstpMstiPortCfgPriority = _Gs2124mstpMstiPortCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 4, 2, 1, 4),
    _Gs2124mstpMstiPortCfgPriority_Type()
)
gs2124mstpMstiPortCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortCfgPriority.setStatus("current")
_Gs2124mstpCfg_ObjectIdentity = ObjectIdentity
gs2124mstpCfg = _Gs2124mstpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5)
)
_Gs2124mstpCfgCist_ObjectIdentity = ObjectIdentity
gs2124mstpCfgCist = _Gs2124mstpCfgCist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 1)
)


class _Gs2124mstpCfgCistPriority_Type(Integer32):
    """Custom type gs2124mstpCfgCistPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Gs2124mstpCfgCistPriority_Type.__name__ = "Integer32"
_Gs2124mstpCfgCistPriority_Object = MibScalar
gs2124mstpCfgCistPriority = _Gs2124mstpCfgCistPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 1, 1),
    _Gs2124mstpCfgCistPriority_Type()
)
gs2124mstpCfgCistPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCfgCistPriority.setStatus("current")


class _Gs2124mstpCfgCistMaxAge_Type(Integer32):
    """Custom type gs2124mstpCfgCistMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2124mstpCfgCistMaxAge_Type.__name__ = "Integer32"
_Gs2124mstpCfgCistMaxAge_Object = MibScalar
gs2124mstpCfgCistMaxAge = _Gs2124mstpCfgCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 1, 2),
    _Gs2124mstpCfgCistMaxAge_Type()
)
gs2124mstpCfgCistMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCfgCistMaxAge.setStatus("current")


class _Gs2124mstpCfgCistFwdDelay_Type(Integer32):
    """Custom type gs2124mstpCfgCistFwdDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Gs2124mstpCfgCistFwdDelay_Type.__name__ = "Integer32"
_Gs2124mstpCfgCistFwdDelay_Object = MibScalar
gs2124mstpCfgCistFwdDelay = _Gs2124mstpCfgCistFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 1, 3),
    _Gs2124mstpCfgCistFwdDelay_Type()
)
gs2124mstpCfgCistFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCfgCistFwdDelay.setStatus("current")


class _Gs2124mstpCfgCistMaxHops_Type(Integer32):
    """Custom type gs2124mstpCfgCistMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Gs2124mstpCfgCistMaxHops_Type.__name__ = "Integer32"
_Gs2124mstpCfgCistMaxHops_Object = MibScalar
gs2124mstpCfgCistMaxHops = _Gs2124mstpCfgCistMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 1, 4),
    _Gs2124mstpCfgCistMaxHops_Type()
)
gs2124mstpCfgCistMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCfgCistMaxHops.setStatus("current")
_Gs2124mstpCfgMstiTable_Object = MibTable
gs2124mstpCfgMstiTable = _Gs2124mstpCfgMstiTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 2)
)
if mibBuilder.loadTexts:
    gs2124mstpCfgMstiTable.setStatus("current")
_Gs2124mstpCfgMstiEntry_Object = MibTableRow
gs2124mstpCfgMstiEntry = _Gs2124mstpCfgMstiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 2, 1)
)
gs2124mstpCfgMstiEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpCfgMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpCfgMstiEntry.setStatus("current")


class _Gs2124mstpCfgMstiInstanceIndex_Type(Integer32):
    """Custom type gs2124mstpCfgMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpCfgMstiInstanceIndex_Type.__name__ = "Integer32"
_Gs2124mstpCfgMstiInstanceIndex_Object = MibTableColumn
gs2124mstpCfgMstiInstanceIndex = _Gs2124mstpCfgMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 2, 1, 1),
    _Gs2124mstpCfgMstiInstanceIndex_Type()
)
gs2124mstpCfgMstiInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpCfgMstiInstanceIndex.setStatus("current")
_Gs2124mstpCfgMstiPriority_Type = Integer32
_Gs2124mstpCfgMstiPriority_Object = MibTableColumn
gs2124mstpCfgMstiPriority = _Gs2124mstpCfgMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 5, 2, 1, 2),
    _Gs2124mstpCfgMstiPriority_Type()
)
gs2124mstpCfgMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2124mstpCfgMstiPriority.setStatus("current")
_Gs2124mstpPortStatus_ObjectIdentity = ObjectIdentity
gs2124mstpPortStatus = _Gs2124mstpPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6)
)
_Gs2124mstpCistPortStatusTable_Object = MibTable
gs2124mstpCistPortStatusTable = _Gs2124mstpCistPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1)
)
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusTable.setStatus("current")
_Gs2124mstpCistPortStatusEntry_Object = MibTableRow
gs2124mstpCistPortStatusEntry = _Gs2124mstpCistPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1)
)
gs2124mstpCistPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpCistPortStatusPortIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusEntry.setStatus("current")


class _Gs2124mstpCistPortStatusPortIndex_Type(Integer32):
    """Custom type gs2124mstpCistPortStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpCistPortStatusPortIndex_Type.__name__ = "Integer32"
_Gs2124mstpCistPortStatusPortIndex_Object = MibTableColumn
gs2124mstpCistPortStatusPortIndex = _Gs2124mstpCistPortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 1),
    _Gs2124mstpCistPortStatusPortIndex_Type()
)
gs2124mstpCistPortStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusPortIndex.setStatus("current")
_Gs2124mstpCistPortStatusStatus_Type = DisplayString
_Gs2124mstpCistPortStatusStatus_Object = MibTableColumn
gs2124mstpCistPortStatusStatus = _Gs2124mstpCistPortStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 2),
    _Gs2124mstpCistPortStatusStatus_Type()
)
gs2124mstpCistPortStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusStatus.setStatus("current")
_Gs2124mstpCistPortStatusRole_Type = DisplayString
_Gs2124mstpCistPortStatusRole_Object = MibTableColumn
gs2124mstpCistPortStatusRole = _Gs2124mstpCistPortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 3),
    _Gs2124mstpCistPortStatusRole_Type()
)
gs2124mstpCistPortStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusRole.setStatus("current")
_Gs2124mstpCistPortStatusPathCost_Type = Integer32
_Gs2124mstpCistPortStatusPathCost_Object = MibTableColumn
gs2124mstpCistPortStatusPathCost = _Gs2124mstpCistPortStatusPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 4),
    _Gs2124mstpCistPortStatusPathCost_Type()
)
gs2124mstpCistPortStatusPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusPathCost.setStatus("current")
_Gs2124mstpCistPortStatusPriority_Type = Integer32
_Gs2124mstpCistPortStatusPriority_Object = MibTableColumn
gs2124mstpCistPortStatusPriority = _Gs2124mstpCistPortStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 5),
    _Gs2124mstpCistPortStatusPriority_Type()
)
gs2124mstpCistPortStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusPriority.setStatus("current")
_Gs2124mstpCistPortStatusHelloTime_Type = DisplayString
_Gs2124mstpCistPortStatusHelloTime_Object = MibTableColumn
gs2124mstpCistPortStatusHelloTime = _Gs2124mstpCistPortStatusHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 6),
    _Gs2124mstpCistPortStatusHelloTime_Type()
)
gs2124mstpCistPortStatusHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusHelloTime.setStatus("current")
_Gs2124mstpCistPortStatusOperEdge_Type = DisplayString
_Gs2124mstpCistPortStatusOperEdge_Object = MibTableColumn
gs2124mstpCistPortStatusOperEdge = _Gs2124mstpCistPortStatusOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 7),
    _Gs2124mstpCistPortStatusOperEdge_Type()
)
gs2124mstpCistPortStatusOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusOperEdge.setStatus("current")
_Gs2124mstpCistPortStatusOperP2P_Type = DisplayString
_Gs2124mstpCistPortStatusOperP2P_Object = MibTableColumn
gs2124mstpCistPortStatusOperP2P = _Gs2124mstpCistPortStatusOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 8),
    _Gs2124mstpCistPortStatusOperP2P_Type()
)
gs2124mstpCistPortStatusOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusOperP2P.setStatus("current")
_Gs2124mstpCistPortStatusRestrictedRole_Type = DisplayString
_Gs2124mstpCistPortStatusRestrictedRole_Object = MibTableColumn
gs2124mstpCistPortStatusRestrictedRole = _Gs2124mstpCistPortStatusRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 9),
    _Gs2124mstpCistPortStatusRestrictedRole_Type()
)
gs2124mstpCistPortStatusRestrictedRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusRestrictedRole.setStatus("current")
_Gs2124mstpCistPortStatusRestrictedTcn_Type = DisplayString
_Gs2124mstpCistPortStatusRestrictedTcn_Object = MibTableColumn
gs2124mstpCistPortStatusRestrictedTcn = _Gs2124mstpCistPortStatusRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 1, 1, 10),
    _Gs2124mstpCistPortStatusRestrictedTcn_Type()
)
gs2124mstpCistPortStatusRestrictedTcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpCistPortStatusRestrictedTcn.setStatus("current")
_Gs2124mstpMstiPortStatusTable_Object = MibTable
gs2124mstpMstiPortStatusTable = _Gs2124mstpMstiPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2)
)
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusTable.setStatus("current")
_Gs2124mstpMstiPortStatusEntry_Object = MibTableRow
gs2124mstpMstiPortStatusEntry = _Gs2124mstpMstiPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1)
)
gs2124mstpMstiPortStatusEntry.setIndexNames(
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpMstiPortStatusInstanceIndex"),
    (0, "LANCOM-GS-2124-MIB", "gs2124mstpMstiPortStatusPortIndex"),
)
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusEntry.setStatus("current")


class _Gs2124mstpMstiPortStatusInstanceIndex_Type(Integer32):
    """Custom type gs2124mstpMstiPortStatusInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpMstiPortStatusInstanceIndex_Type.__name__ = "Integer32"
_Gs2124mstpMstiPortStatusInstanceIndex_Object = MibTableColumn
gs2124mstpMstiPortStatusInstanceIndex = _Gs2124mstpMstiPortStatusInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 1),
    _Gs2124mstpMstiPortStatusInstanceIndex_Type()
)
gs2124mstpMstiPortStatusInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusInstanceIndex.setStatus("current")


class _Gs2124mstpMstiPortStatusPortIndex_Type(Integer32):
    """Custom type gs2124mstpMstiPortStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Gs2124mstpMstiPortStatusPortIndex_Type.__name__ = "Integer32"
_Gs2124mstpMstiPortStatusPortIndex_Object = MibTableColumn
gs2124mstpMstiPortStatusPortIndex = _Gs2124mstpMstiPortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 2),
    _Gs2124mstpMstiPortStatusPortIndex_Type()
)
gs2124mstpMstiPortStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusPortIndex.setStatus("current")
_Gs2124mstpMstiPortStatusStatus_Type = DisplayString
_Gs2124mstpMstiPortStatusStatus_Object = MibTableColumn
gs2124mstpMstiPortStatusStatus = _Gs2124mstpMstiPortStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 3),
    _Gs2124mstpMstiPortStatusStatus_Type()
)
gs2124mstpMstiPortStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusStatus.setStatus("current")
_Gs2124mstpMstiPortStatusRole_Type = DisplayString
_Gs2124mstpMstiPortStatusRole_Object = MibTableColumn
gs2124mstpMstiPortStatusRole = _Gs2124mstpMstiPortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 4),
    _Gs2124mstpMstiPortStatusRole_Type()
)
gs2124mstpMstiPortStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusRole.setStatus("current")
_Gs2124mstpMstiPortStatusPathCost_Type = DisplayString
_Gs2124mstpMstiPortStatusPathCost_Object = MibTableColumn
gs2124mstpMstiPortStatusPathCost = _Gs2124mstpMstiPortStatusPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 5),
    _Gs2124mstpMstiPortStatusPathCost_Type()
)
gs2124mstpMstiPortStatusPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusPathCost.setStatus("current")
_Gs2124mstpMstiPortStatusPriority_Type = DisplayString
_Gs2124mstpMstiPortStatusPriority_Object = MibTableColumn
gs2124mstpMstiPortStatusPriority = _Gs2124mstpMstiPortStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 6),
    _Gs2124mstpMstiPortStatusPriority_Type()
)
gs2124mstpMstiPortStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusPriority.setStatus("current")
_Gs2124mstpMstiPortStatusHelloTime_Type = DisplayString
_Gs2124mstpMstiPortStatusHelloTime_Object = MibTableColumn
gs2124mstpMstiPortStatusHelloTime = _Gs2124mstpMstiPortStatusHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 7),
    _Gs2124mstpMstiPortStatusHelloTime_Type()
)
gs2124mstpMstiPortStatusHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusHelloTime.setStatus("current")
_Gs2124mstpMstiPortStatusOperEdge_Type = DisplayString
_Gs2124mstpMstiPortStatusOperEdge_Object = MibTableColumn
gs2124mstpMstiPortStatusOperEdge = _Gs2124mstpMstiPortStatusOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 8),
    _Gs2124mstpMstiPortStatusOperEdge_Type()
)
gs2124mstpMstiPortStatusOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusOperEdge.setStatus("current")
_Gs2124mstpMstiPortStatusOperP2P_Type = DisplayString
_Gs2124mstpMstiPortStatusOperP2P_Object = MibTableColumn
gs2124mstpMstiPortStatusOperP2P = _Gs2124mstpMstiPortStatusOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 9),
    _Gs2124mstpMstiPortStatusOperP2P_Type()
)
gs2124mstpMstiPortStatusOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusOperP2P.setStatus("current")
_Gs2124mstpMstiPortStatusRestrictedRole_Type = DisplayString
_Gs2124mstpMstiPortStatusRestrictedRole_Object = MibTableColumn
gs2124mstpMstiPortStatusRestrictedRole = _Gs2124mstpMstiPortStatusRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 10),
    _Gs2124mstpMstiPortStatusRestrictedRole_Type()
)
gs2124mstpMstiPortStatusRestrictedRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusRestrictedRole.setStatus("current")
_Gs2124mstpMstiPortStatusRestrictedTcn_Type = DisplayString
_Gs2124mstpMstiPortStatusRestrictedTcn_Object = MibTableColumn
gs2124mstpMstiPortStatusRestrictedTcn = _Gs2124mstpMstiPortStatusRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 200, 6, 2, 1, 11),
    _Gs2124mstpMstiPortStatusRestrictedTcn_Type()
)
gs2124mstpMstiPortStatusRestrictedTcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2124mstpMstiPortStatusRestrictedTcn.setStatus("current")

# Managed Objects groups


# Notification objects

gs2124UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 1)
)
gs2124UserLogin.setObjects(
    ("LANCOM-GS-2124-MIB", "username")
)
if mibBuilder.loadTexts:
    gs2124UserLogin.setStatus(
        "current"
    )

gs2124UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 2)
)
gs2124UserLogout.setObjects(
    ("LANCOM-GS-2124-MIB", "username")
)
if mibBuilder.loadTexts:
    gs2124UserLogout.setStatus(
        "current"
    )

gs2124ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 3)
)
gs2124ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2124ModuleInserted.setStatus(
        "current"
    )

gs2124ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 4)
)
gs2124ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2124ModuleRemoved.setStatus(
        "current"
    )

gs2124DualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 5)
)
gs2124DualMediaSwapped.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-GS-2124-MIB", "swapto"))
)
if mibBuilder.loadTexts:
    gs2124DualMediaSwapped.setStatus(
        "current"
    )

gs2124LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 6)
)
gs2124LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2124LoopDetected.setStatus(
        "current"
    )

gs2124StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 7)
)
if mibBuilder.loadTexts:
    gs2124StpStateDisabled.setStatus(
        "current"
    )

gs2124StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 8)
)
if mibBuilder.loadTexts:
    gs2124StpStateEnabled.setStatus(
        "current"
    )

gs2124StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 9)
)
gs2124StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2124StpTopologyChanged.setStatus(
        "current"
    )

gs2124LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 10)
)
gs2124LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-GS-2124-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    gs2124LacpStateDisabled.setStatus(
        "current"
    )

gs2124LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 11)
)
gs2124LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-GS-2124-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    gs2124LacpStateEnabled.setStatus(
        "current"
    )

gs2124LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 12)
)
gs2124LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-GS-2124-MIB", "actorkey"),
        ("LANCOM-GS-2124-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    gs2124LacpPortAdded.setStatus(
        "current"
    )

gs2124LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 13)
)
gs2124LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-GS-2124-MIB", "actorkey"),
        ("LANCOM-GS-2124-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    gs2124LacpPortTrunkFailure.setStatus(
        "current"
    )

gs2124GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 14)
)
if mibBuilder.loadTexts:
    gs2124GvrpStateDisabled.setStatus(
        "current"
    )

gs2124GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 15)
)
if mibBuilder.loadTexts:
    gs2124GvrpStateEnabled.setStatus(
        "current"
    )

gs2124VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 17)
)
if mibBuilder.loadTexts:
    gs2124VlanPortBaseEnabled.setStatus(
        "current"
    )

gs2124VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 18)
)
if mibBuilder.loadTexts:
    gs2124VlanTagBaseEnabled.setStatus(
        "current"
    )

gs2124IpmbStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 19)
)
if mibBuilder.loadTexts:
    gs2124IpmbStateEnabled.setStatus(
        "current"
    )

gs2124IpmbStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 20)
)
if mibBuilder.loadTexts:
    gs2124IpmbStateDisabled.setStatus(
        "current"
    )

gs2124IpmbEntryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 3, 2124, 1, 20, 21)
)
gs2124IpmbEntryFailure.setObjects(
      *(("LANCOM-GS-2124-MIB", "ipmacIp"),
        ("LANCOM-GS-2124-MIB", "ipmacMac"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    gs2124IpmbEntryFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-GS-2124-MIB",
    **{"lancomSystems": lancomSystems,
       "switchingSystems": switchingSystems,
       "gigabitEthernetSwitches": gigabitEthernetSwitches,
       "lancomGS2124": lancomGS2124,
       "gs2124Produces": gs2124Produces,
       "gs2124System": gs2124System,
       "gs2124CommonSys": gs2124CommonSys,
       "gs2124Reboot": gs2124Reboot,
       "gs2124BiosVsersion": gs2124BiosVsersion,
       "gs2124FirmwareVersion": gs2124FirmwareVersion,
       "gs2124HardwareVersion": gs2124HardwareVersion,
       "gs2124MechanicalVersion": gs2124MechanicalVersion,
       "gs2124SerialNumber": gs2124SerialNumber,
       "gs2124HostMacAddress": gs2124HostMacAddress,
       "gs2124DevicePort": gs2124DevicePort,
       "gs2124RamSize": gs2124RamSize,
       "gs2124FlashSize": gs2124FlashSize,
       "gs2124DeviceName": gs2124DeviceName,
       "gs2124SystemDescription": gs2124SystemDescription,
       "gs2124CpuLoad": gs2124CpuLoad,
       "gs2124IP": gs2124IP,
       "gs2124DhcpSetting": gs2124DhcpSetting,
       "gs2124IPAddress": gs2124IPAddress,
       "gs2124NetMask": gs2124NetMask,
       "gs2124DefaultGateway": gs2124DefaultGateway,
       "gs2124DnsConf": gs2124DnsConf,
       "gs2124DnsState": gs2124DnsState,
       "gs2124DnsServer": gs2124DnsServer,
       "gs2124Time": gs2124Time,
       "gs2124SystemCurrentTime": gs2124SystemCurrentTime,
       "gs2124ManualTimeSetting": gs2124ManualTimeSetting,
       "gs2124NTPServer": gs2124NTPServer,
       "gs2124NTPTimeZone": gs2124NTPTimeZone,
       "gs2124NTPTimeSync": gs2124NTPTimeSync,
       "gs2124DaylightSavingTime": gs2124DaylightSavingTime,
       "gs2124DaylightStartTime": gs2124DaylightStartTime,
       "gs2124DaylightEndTime": gs2124DaylightEndTime,
       "gs2124Account": gs2124Account,
       "gs2124AccountNumber": gs2124AccountNumber,
       "gs2124AccountTable": gs2124AccountTable,
       "gs2124AccountEntry": gs2124AccountEntry,
       "gs2124AccountIndex": gs2124AccountIndex,
       "gs2124AccountAuthorization": gs2124AccountAuthorization,
       "gs2124AccountName": gs2124AccountName,
       "gs2124AccountPassword": gs2124AccountPassword,
       "gs2124AccountAddAuthorization": gs2124AccountAddAuthorization,
       "gs2124AccountAddName": gs2124AccountAddName,
       "gs2124AccountAddPassword": gs2124AccountAddPassword,
       "gs2124DoAccountAdd": gs2124DoAccountAdd,
       "gs2124AccountDel": gs2124AccountDel,
       "gs2124Vsm": gs2124Vsm,
       "gs2124VsmState": gs2124VsmState,
       "gs2124VsmRole": gs2124VsmRole,
       "gs2124VsmGroupid": gs2124VsmGroupid,
       "gs2124Snmp": gs2124Snmp,
       "gs2124GetCommunity": gs2124GetCommunity,
       "gs2124SetCommunity": gs2124SetCommunity,
       "gs2124TrapHostNumber": gs2124TrapHostNumber,
       "gs2124TrapHostTable": gs2124TrapHostTable,
       "gs2124TrapHostEntry": gs2124TrapHostEntry,
       "gs2124TrapHostIndex": gs2124TrapHostIndex,
       "gs2124TrapHostIP": gs2124TrapHostIP,
       "gs2124TrapHostPort": gs2124TrapHostPort,
       "gs2124TrapHostCommunity": gs2124TrapHostCommunity,
       "gs2124Alarm": gs2124Alarm,
       "gs2124Event": gs2124Event,
       "gs2124EventNumber": gs2124EventNumber,
       "gs2124EventTable": gs2124EventTable,
       "gs2124EventEntry": gs2124EventEntry,
       "gs2124EventIndex": gs2124EventIndex,
       "gs2124EventName": gs2124EventName,
       "gs2124EventSendEmail": gs2124EventSendEmail,
       "gs2124EventSendTrap": gs2124EventSendTrap,
       "gs2124Email": gs2124Email,
       "gs2124EmailServer": gs2124EmailServer,
       "gs2124EmailUsername": gs2124EmailUsername,
       "gs2124EmailPassword": gs2124EmailPassword,
       "gs2124EmailSender": gs2124EmailSender,
       "gs2124EmailReturnPath": gs2124EmailReturnPath,
       "gs2124EmailUserNumber": gs2124EmailUserNumber,
       "gs2124EmailUserTable": gs2124EmailUserTable,
       "gs2124EmailUserEntry": gs2124EmailUserEntry,
       "gs2124EmailUserIndex": gs2124EmailUserIndex,
       "gs2124EmailUserAddress": gs2124EmailUserAddress,
       "gs2124Configuration": gs2124Configuration,
       "gs2124SaveRestore": gs2124SaveRestore,
       "gs2124SaveStart": gs2124SaveStart,
       "gs2124SaveUser": gs2124SaveUser,
       "gs2124RestoreDefault": gs2124RestoreDefault,
       "gs2124RestoreUser": gs2124RestoreUser,
       "gs2124ConfigFile": gs2124ConfigFile,
       "gs2124ExportIpAddress": gs2124ExportIpAddress,
       "gs2124DoExportConfig": gs2124DoExportConfig,
       "gs2124ImportIpAddress": gs2124ImportIpAddress,
       "gs2124ImportConfigName": gs2124ImportConfigName,
       "gs2124DoImportConfig": gs2124DoImportConfig,
       "gs2124Log": gs2124Log,
       "gs2124ClearLog": gs2124ClearLog,
       "gs2124LogNumber": gs2124LogNumber,
       "gs2124LogTable": gs2124LogTable,
       "gs2124LogEntry": gs2124LogEntry,
       "gs2124LogIndex": gs2124LogIndex,
       "gs2124LogEvent": gs2124LogEvent,
       "gs2124Firmware": gs2124Firmware,
       "gs2124FirmwareIpAddress": gs2124FirmwareIpAddress,
       "gs2124FirmwareFileName": gs2124FirmwareFileName,
       "gs2124DoFirmwareUpgrade": gs2124DoFirmwareUpgrade,
       "gs2124Port": gs2124Port,
       "gs2124PortStatus": gs2124PortStatus,
       "gs2124PortStatusNumber": gs2124PortStatusNumber,
       "gs2124PortStatusTable": gs2124PortStatusTable,
       "gs2124PortStatusEntry": gs2124PortStatusEntry,
       "gs2124PortStatusIndex": gs2124PortStatusIndex,
       "gs2124PortStatusMedia": gs2124PortStatusMedia,
       "gs2124PortStatusPortState": gs2124PortStatusPortState,
       "gs2124PortStatusLink": gs2124PortStatusLink,
       "gs2124PortStatusAutoNego": gs2124PortStatusAutoNego,
       "gs2124PortStatusSpdDpx": gs2124PortStatusSpdDpx,
       "gs2124PortStatusFlwCtrlRx": gs2124PortStatusFlwCtrlRx,
       "gs2124PortStatusFlwCtrlTx": gs2124PortStatusFlwCtrlTx,
       "gs2124PortStatuDescription": gs2124PortStatuDescription,
       "gs2124PortConf": gs2124PortConf,
       "gs2124PortConfNumber": gs2124PortConfNumber,
       "gs2124PortConfTable": gs2124PortConfTable,
       "gs2124PortConfEntry": gs2124PortConfEntry,
       "gs2124PortConfIndex": gs2124PortConfIndex,
       "gs2124PortConfPortState": gs2124PortConfPortState,
       "gs2124PortConfTPSpdDpx": gs2124PortConfTPSpdDpx,
       "gs2124PortConfSFPSpdDpx": gs2124PortConfSFPSpdDpx,
       "gs2124PortConfFlwCtrl": gs2124PortConfFlwCtrl,
       "gs2124PortConfExcessiveCollisionMode": gs2124PortConfExcessiveCollisionMode,
       "gs2124PortConfDescription": gs2124PortConfDescription,
       "gs2124PortConfPowerSaving": gs2124PortConfPowerSaving,
       "gs2124SFPInfo": gs2124SFPInfo,
       "gs2124SFPInfoNumber": gs2124SFPInfoNumber,
       "gs2124SFPInfoTable": gs2124SFPInfoTable,
       "gs2124SFPInfoEntry": gs2124SFPInfoEntry,
       "gs2124SFPInfoIndex": gs2124SFPInfoIndex,
       "gs2124SFPConnectorType": gs2124SFPConnectorType,
       "gs2124SFPFiberType": gs2124SFPFiberType,
       "gs2124SFPWavelength": gs2124SFPWavelength,
       "gs2124SFPBaudRate": gs2124SFPBaudRate,
       "gs2124SFPVendorOUI": gs2124SFPVendorOUI,
       "gs2124SFPVendorName": gs2124SFPVendorName,
       "gs2124SFPVendorPN": gs2124SFPVendorPN,
       "gs2124SFPVendorRev": gs2124SFPVendorRev,
       "gs2124SFPVendorSN": gs2124SFPVendorSN,
       "gs2124SFPDateCode": gs2124SFPDateCode,
       "gs2124SFPTemperature": gs2124SFPTemperature,
       "gs2124SFPVcc": gs2124SFPVcc,
       "gs2124SFPTxBias": gs2124SFPTxBias,
       "gs2124SFPTxPWR": gs2124SFPTxPWR,
       "gs2124SFPRxPWR": gs2124SFPRxPWR,
       "gs2124Mirror": gs2124Mirror,
       "gs2124MirroringPort": gs2124MirroringPort,
       "gs2124MirroredPortsTable": gs2124MirroredPortsTable,
       "gs2124MirroredPortsEntry": gs2124MirroredPortsEntry,
       "gs2124MirroredPortIndex": gs2124MirroredPortIndex,
       "gs2124MirroredPortSrouceEnable": gs2124MirroredPortSrouceEnable,
       "gs2124MirroredPortDestinationEnable": gs2124MirroredPortDestinationEnable,
       "gs2124MaxPktLen": gs2124MaxPktLen,
       "gs2124MaxPktLenPortNumber": gs2124MaxPktLenPortNumber,
       "gs2124MaxPktLenConfTable": gs2124MaxPktLenConfTable,
       "gs2124MaxPktLenConfEntry": gs2124MaxPktLenConfEntry,
       "gs2124MaxPktLenConfIndex": gs2124MaxPktLenConfIndex,
       "gs2124MaxPktLenConfSetting": gs2124MaxPktLenConfSetting,
       "gs2124LoopDetectedConf": gs2124LoopDetectedConf,
       "gs2124LoopDetectedNumber": gs2124LoopDetectedNumber,
       "gs2124LoopDetectedTable": gs2124LoopDetectedTable,
       "gs2124LoopDetectedEntry": gs2124LoopDetectedEntry,
       "gs2124LoopDetectedfIndex": gs2124LoopDetectedfIndex,
       "gs2124LoopDetectedPort": gs2124LoopDetectedPort,
       "gs2124LoopDetectedLockedPort": gs2124LoopDetectedLockedPort,
       "gs2124ManagementPolicy": gs2124ManagementPolicy,
       "gs2124ManagementSecurityNumber": gs2124ManagementSecurityNumber,
       "gs2124ManagementSecurityEntryCreate": gs2124ManagementSecurityEntryCreate,
       "gs2124ManagementSecurityTable": gs2124ManagementSecurityTable,
       "gs2124ManagementSecurityEntry": gs2124ManagementSecurityEntry,
       "gs2124ManagementSecurityIndex": gs2124ManagementSecurityIndex,
       "gs2124ManagementSecurityName": gs2124ManagementSecurityName,
       "gs2124ManagementSecurityIpRange": gs2124ManagementSecurityIpRange,
       "gs2124ManagementSecurityIncomigPort": gs2124ManagementSecurityIncomigPort,
       "gs2124ManagementSecurityAccessType": gs2124ManagementSecurityAccessType,
       "gs2124ManagementSecurityAction": gs2124ManagementSecurityAction,
       "gs2124ManagementSecurityEntryAction": gs2124ManagementSecurityEntryAction,
       "gs2124VLAN": gs2124VLAN,
       "gs2124VlanConf": gs2124VlanConf,
       "gs2124VlanMode": gs2124VlanMode,
       "gs2124ManagementVlan": gs2124ManagementVlan,
       "gs2124PortIsolation": gs2124PortIsolation,
       "gs2124TagIdentifier": gs2124TagIdentifier,
       "gs2124TagBaseVlanGroup": gs2124TagBaseVlanGroup,
       "gs2124TagBaseVlanNumber": gs2124TagBaseVlanNumber,
       "gs2124TagBaseVlanGroupEntryCreate": gs2124TagBaseVlanGroupEntryCreate,
       "gs2124TagBaseVlanGroupTable": gs2124TagBaseVlanGroupTable,
       "gs2124TagBaseVlanGroupEntry": gs2124TagBaseVlanGroupEntry,
       "gs2124TagBaseVlanVid": gs2124TagBaseVlanVid,
       "gs2124TagBaseVlanName": gs2124TagBaseVlanName,
       "gs2124TagBaseVlanIgmpProxy": gs2124TagBaseVlanIgmpProxy,
       "gs2124TagBaseVlanPrivateVlan": gs2124TagBaseVlanPrivateVlan,
       "gs2124TagBaseVlanGvrp": gs2124TagBaseVlanGvrp,
       "gs2124TagBaseVlanMemberPort": gs2124TagBaseVlanMemberPort,
       "gs2124TagBaseVlanEntryAction": gs2124TagBaseVlanEntryAction,
       "gs2124VlanPortConfTable": gs2124VlanPortConfTable,
       "gs2124VlanPortConfEntry": gs2124VlanPortConfEntry,
       "gs2124VlanPortConfIndex": gs2124VlanPortConfIndex,
       "gs2124VlanPortConfVlanAware": gs2124VlanPortConfVlanAware,
       "gs2124VlanPortConfIngressFiltering": gs2124VlanPortConfIngressFiltering,
       "gs2124VlanPortConfFrameType": gs2124VlanPortConfFrameType,
       "gs2124VlanPortConfPvid": gs2124VlanPortConfPvid,
       "gs2124VlanPortConfRole": gs2124VlanPortConfRole,
       "gs2124VlanPortConfUntagVid": gs2124VlanPortConfUntagVid,
       "gs2124VlanPortConfDoubleTag": gs2124VlanPortConfDoubleTag,
       "gs2124PortBaseVlanGroup": gs2124PortBaseVlanGroup,
       "gs2124PortBaseVlanNumber": gs2124PortBaseVlanNumber,
       "gs2124PortBaseVlanGroupEntryCreate": gs2124PortBaseVlanGroupEntryCreate,
       "gs2124PortBaseVlanGroupTable": gs2124PortBaseVlanGroupTable,
       "gs2124PortBaseVlanGroupEntry": gs2124PortBaseVlanGroupEntry,
       "gs2124PortBaseVlanGroupIndex": gs2124PortBaseVlanGroupIndex,
       "gs2124PortBaseVlanGroupName": gs2124PortBaseVlanGroupName,
       "gs2124PortBaseVlanGroupMembers": gs2124PortBaseVlanGroupMembers,
       "gs2124PortBaseVlanGroupEntryAction": gs2124PortBaseVlanGroupEntryAction,
       "gs2124MacTableInfo": gs2124MacTableInfo,
       "gs2124MacTableConf": gs2124MacTableConf,
       "gs2124MacAgeTime": gs2124MacAgeTime,
       "gs2124MacTableLearningConfTable": gs2124MacTableLearningConfTable,
       "gs2124MacTableLearningConfEntry": gs2124MacTableLearningConfEntry,
       "gs2124MacTableLearningConfIndex": gs2124MacTableLearningConfIndex,
       "gs2124MacTableLearningConfstate": gs2124MacTableLearningConfstate,
       "gs2124MacTableStaticFilter": gs2124MacTableStaticFilter,
       "gs2124MacTableStaticFilterNumber": gs2124MacTableStaticFilterNumber,
       "gs2124MacTableStaticFilterEntryCreate": gs2124MacTableStaticFilterEntryCreate,
       "gs2124MacTableStaticFilterTable": gs2124MacTableStaticFilterTable,
       "gs2124MacTableStaticFilterEntry": gs2124MacTableStaticFilterEntry,
       "gs2124MacTableStaticFilterIndex": gs2124MacTableStaticFilterIndex,
       "gs2124MacTableStaticFilterMac": gs2124MacTableStaticFilterMac,
       "gs2124MacTableStaticFilterVid": gs2124MacTableStaticFilterVid,
       "gs2124MacTableStaticFilterAlias": gs2124MacTableStaticFilterAlias,
       "gs2124MacTableStaticFilterEntryAction": gs2124MacTableStaticFilterEntryAction,
       "gs2124MacTableStaticForward": gs2124MacTableStaticForward,
       "gs2124MacTableStaticForwardNumber": gs2124MacTableStaticForwardNumber,
       "gs2124MacTableStaticForwardEntryCreate": gs2124MacTableStaticForwardEntryCreate,
       "gs2124MacTableStaticForwardTable": gs2124MacTableStaticForwardTable,
       "gs2124MacTableStaticForwardEntry": gs2124MacTableStaticForwardEntry,
       "gs2124MacTableStaticForwardIndex": gs2124MacTableStaticForwardIndex,
       "gs2124MacTableStaticForwardMac": gs2124MacTableStaticForwardMac,
       "gs2124MacTableStaticForwardPort": gs2124MacTableStaticForwardPort,
       "gs2124MacTableStaticForwardVid": gs2124MacTableStaticForwardVid,
       "gs2124MacTableStaticForwardAlias": gs2124MacTableStaticForwardAlias,
       "gs2124MacTableStaticForwardEntryAction": gs2124MacTableStaticForwardEntryAction,
       "gs2124MacAlias": gs2124MacAlias,
       "gs2124MacAliasNumber": gs2124MacAliasNumber,
       "gs2124MacAliasEntryCreate": gs2124MacAliasEntryCreate,
       "gs2124MacAliasTable": gs2124MacAliasTable,
       "gs2124MacAliasEntry": gs2124MacAliasEntry,
       "gs2124MacAliasIndex": gs2124MacAliasIndex,
       "gs2124AliasMac": gs2124AliasMac,
       "gs2124AliasName": gs2124AliasName,
       "gs2124MacAliasEntryAction": gs2124MacAliasEntryAction,
       "gs2124GVRPInfo": gs2124GVRPInfo,
       "gs2124GvrpConf": gs2124GvrpConf,
       "gs2124GvrpConfState": gs2124GvrpConfState,
       "gs2124GvrpConfTable": gs2124GvrpConfTable,
       "gs2124GvrpConfEntry": gs2124GvrpConfEntry,
       "gs2124GvrpConfIndex": gs2124GvrpConfIndex,
       "gs2124GvrpConfJoinTime": gs2124GvrpConfJoinTime,
       "gs2124GvrpConfLeaveTime": gs2124GvrpConfLeaveTime,
       "gs2124GvrpConfLeaveAllTime": gs2124GvrpConfLeaveAllTime,
       "gs2124GvrpConfDefaultAppMode": gs2124GvrpConfDefaultAppMode,
       "gs2124GvrpConfDefaultRegMode": gs2124GvrpConfDefaultRegMode,
       "gs2124GvrpConfRestrictedMode": gs2124GvrpConfRestrictedMode,
       "gs2124GvrpCounter": gs2124GvrpCounter,
       "gs2124GvrpCounterTable": gs2124GvrpCounterTable,
       "gs2124GvrpCounterEntry": gs2124GvrpCounterEntry,
       "gs2124GvrpCounterIndex": gs2124GvrpCounterIndex,
       "gs2124GvrpCounterRxTotalGvrpPkts": gs2124GvrpCounterRxTotalGvrpPkts,
       "gs2124GvrpCounterRxInvalidGvrpPkts": gs2124GvrpCounterRxInvalidGvrpPkts,
       "gs2124GvrpCounterRxLeaveAllMsg": gs2124GvrpCounterRxLeaveAllMsg,
       "gs2124GvrpCounterRxJoinEmptyMsg": gs2124GvrpCounterRxJoinEmptyMsg,
       "gs2124GvrpCounterRxJoinInMsg": gs2124GvrpCounterRxJoinInMsg,
       "gs2124GvrpCounterRxLeaveEmptyMsg": gs2124GvrpCounterRxLeaveEmptyMsg,
       "gs2124GvrpCounterRxEmptyMsg": gs2124GvrpCounterRxEmptyMsg,
       "gs2124GvrpCounterTxTotalGvrpPkts": gs2124GvrpCounterTxTotalGvrpPkts,
       "gs2124GvrpCounterTxLeaveAllMsg": gs2124GvrpCounterTxLeaveAllMsg,
       "gs2124GvrpCounterTxJoinEmptyMsg": gs2124GvrpCounterTxJoinEmptyMsg,
       "gs2124GvrpCounterTxJoinInMsg": gs2124GvrpCounterTxJoinInMsg,
       "gs2124GvrpCounterTxLeaveEmptyMsg": gs2124GvrpCounterTxLeaveEmptyMsg,
       "gs2124GvrpCounterTxEmptyMsg": gs2124GvrpCounterTxEmptyMsg,
       "gs2124GvrpGroup": gs2124GvrpGroup,
       "gs2124GvrpGroupNumber": gs2124GvrpGroupNumber,
       "gs2124GvrpGroupTable": gs2124GvrpGroupTable,
       "gs2124GvrpGroupEntry": gs2124GvrpGroupEntry,
       "gs2124GvrpGroupId": gs2124GvrpGroupId,
       "gs2124GvrpGroupVid": gs2124GvrpGroupVid,
       "gs2124GvrpGroupMemberPort": gs2124GvrpGroupMemberPort,
       "gs2124GvrpGroupAdministrativeCtrlTable": gs2124GvrpGroupAdministrativeCtrlTable,
       "gs2124GvrpGroupAdministrativeCtrlEntry": gs2124GvrpGroupAdministrativeCtrlEntry,
       "gs2124GvrpGroupAdministrativeCtrlVid": gs2124GvrpGroupAdministrativeCtrlVid,
       "gs2124GvrpGroupAdministrativeCtrlPort": gs2124GvrpGroupAdministrativeCtrlPort,
       "gs2124GvrpGroupAdministrativeCtrlApp": gs2124GvrpGroupAdministrativeCtrlApp,
       "gs2124GvrpGroupAdministrativeCtrlReg": gs2124GvrpGroupAdministrativeCtrlReg,
       "gs2124QosInfo": gs2124QosInfo,
       "gs2124QosPortConf": gs2124QosPortConf,
       "gs2124QosNumOfClasses": gs2124QosNumOfClasses,
       "gs2124QosPortConfTable": gs2124QosPortConfTable,
       "gs2124QosPortConfEntry": gs2124QosPortConfEntry,
       "gs2124QosPortConfIndex": gs2124QosPortConfIndex,
       "gs2124QosPortConfDefaultClasses": gs2124QosPortConfDefaultClasses,
       "gs2124QosPortConfQCL": gs2124QosPortConfQCL,
       "gs2124QosPortConfUserPriority": gs2124QosPortConfUserPriority,
       "gs2124QosPortConfQueuingMode": gs2124QosPortConfQueuingMode,
       "gs2124QosPortConfQueueWeightedLow": gs2124QosPortConfQueueWeightedLow,
       "gs2124QosPortConfQueueWeightedNormal": gs2124QosPortConfQueueWeightedNormal,
       "gs2124QosPortConfQueueWeightedMedium": gs2124QosPortConfQueueWeightedMedium,
       "gs2124QosPortConfQueueWeightedHigh": gs2124QosPortConfQueueWeightedHigh,
       "gs2124QosRateLimiters": gs2124QosRateLimiters,
       "gs2124QosRateLimitersTable": gs2124QosRateLimitersTable,
       "gs2124QosRateLimitersEntry": gs2124QosRateLimitersEntry,
       "gs2124QosRateLimitersIndex": gs2124QosRateLimitersIndex,
       "gs2124QosRateLimitersPolicer": gs2124QosRateLimitersPolicer,
       "gs2124QosRateLimitersPolicerRate": gs2124QosRateLimitersPolicerRate,
       "gs2124QosRateLimitersShaper": gs2124QosRateLimitersShaper,
       "gs2124QosRateLimitersShaperRate": gs2124QosRateLimitersShaperRate,
       "gs2124QosStormCtrl": gs2124QosStormCtrl,
       "gs2124QosStromCtrlFloodedUnicastStatus": gs2124QosStromCtrlFloodedUnicastStatus,
       "gs2124QosStromCtrlFloodedUnicastRate": gs2124QosStromCtrlFloodedUnicastRate,
       "gs2124QosStromCtrlMulticastStatus": gs2124QosStromCtrlMulticastStatus,
       "gs2124QosStromCtrlMulticastRate": gs2124QosStromCtrlMulticastRate,
       "gs2124QosStromCtrlBroadcastStatus": gs2124QosStromCtrlBroadcastStatus,
       "gs2124QosStromCtrlBroadcastRate": gs2124QosStromCtrlBroadcastRate,
       "gs2124QosQCL": gs2124QosQCL,
       "gs2124QosQclCreate": gs2124QosQclCreate,
       "gs2124QosQclTable": gs2124QosQclTable,
       "gs2124QosQclEntry": gs2124QosQclEntry,
       "gs2124QosQclNo": gs2124QosQclNo,
       "gs2124QosQclQceListNo": gs2124QosQclQceListNo,
       "gs2124QosQclQceMoveTo": gs2124QosQclQceMoveTo,
       "gs2124QosQclQceType": gs2124QosQclQceType,
       "gs2124QosQclQceValue": gs2124QosQclQceValue,
       "gs2124QosQclQceTrafficClass": gs2124QosQclQceTrafficClass,
       "gs2124QosQclQcePriority0Class": gs2124QosQclQcePriority0Class,
       "gs2124QosQclQcePriority1Class": gs2124QosQclQcePriority1Class,
       "gs2124QosQclQcePriority2Class": gs2124QosQclQcePriority2Class,
       "gs2124QosQclQcePriority3Class": gs2124QosQclQcePriority3Class,
       "gs2124QosQclQcePriority4Class": gs2124QosQclQcePriority4Class,
       "gs2124QosQclQcePriority5Class": gs2124QosQclQcePriority5Class,
       "gs2124QosQclQcePriority6Class": gs2124QosQclQcePriority6Class,
       "gs2124QosQclQcePriority7Class": gs2124QosQclQcePriority7Class,
       "gs2124QosQclQceEntryAction": gs2124QosQclQceEntryAction,
       "gs2124AclInfo": gs2124AclInfo,
       "gs2124AclPortsConfTable": gs2124AclPortsConfTable,
       "gs2124AclPortsConfEntry": gs2124AclPortsConfEntry,
       "gs2124AclPortsConfIndex": gs2124AclPortsConfIndex,
       "gs2124AclPortsConfPolicyId": gs2124AclPortsConfPolicyId,
       "gs2124AclPortsConfAction": gs2124AclPortsConfAction,
       "gs2124AclPortsConfRateLimiterId": gs2124AclPortsConfRateLimiterId,
       "gs2124AclPortsConfPortCopy": gs2124AclPortsConfPortCopy,
       "gs2124AclPortsConfCounter": gs2124AclPortsConfCounter,
       "gs2124AclRateLimiter": gs2124AclRateLimiter,
       "gs2124AclRateLimiterTable": gs2124AclRateLimiterTable,
       "gs2124AclRateLimiterEntry": gs2124AclRateLimiterEntry,
       "gs2124AclRateLimiterIndex": gs2124AclRateLimiterIndex,
       "gs2124AclRateLimiterRate": gs2124AclRateLimiterRate,
       "gs2124AclInfoViewTable": gs2124AclInfoViewTable,
       "gs2124AclInfoViewEntry": gs2124AclInfoViewEntry,
       "gs2124AclInfoViewNo": gs2124AclInfoViewNo,
       "gs2124AceIngressPort": gs2124AceIngressPort,
       "gs2124AceFrameType": gs2124AceFrameType,
       "gs2124AceAction": gs2124AceAction,
       "gs2124AceRateLimiter": gs2124AceRateLimiter,
       "gs2124AcePortCopy": gs2124AcePortCopy,
       "gs2124AceCounter": gs2124AceCounter,
       "gs2124SmacFilter": gs2124SmacFilter,
       "gs2124DmacFilter": gs2124DmacFilter,
       "gs2124VlanIdFilter": gs2124VlanIdFilter,
       "gs2124VlanTagPriority": gs2124VlanTagPriority,
       "gs2124EtherTypeFilter": gs2124EtherTypeFilter,
       "gs2124ArpRarp": gs2124ArpRarp,
       "gs2124ArpRequestReply": gs2124ArpRequestReply,
       "gs2124ArpSenderIpFilter": gs2124ArpSenderIpFilter,
       "gs2124ArpSenderIpAddress": gs2124ArpSenderIpAddress,
       "gs2124ArpSenderIpMask": gs2124ArpSenderIpMask,
       "gs2124ArpTargetIpFilter": gs2124ArpTargetIpFilter,
       "gs2124ArpTargetIpAddress": gs2124ArpTargetIpAddress,
       "gs2124ArpTargetIpMask": gs2124ArpTargetIpMask,
       "gs2124ArpSmacMatch": gs2124ArpSmacMatch,
       "gs2124ArpRarpDmacMatch": gs2124ArpRarpDmacMatch,
       "gs2124ArpIpEthernetLength": gs2124ArpIpEthernetLength,
       "gs2124ArpIp": gs2124ArpIp,
       "gs2124ArpEthernet": gs2124ArpEthernet,
       "gs2124IpProtocolFilter": gs2124IpProtocolFilter,
       "gs2124IpProtocolValue": gs2124IpProtocolValue,
       "gs2124IpTTL": gs2124IpTTL,
       "gs2124IpFragment": gs2124IpFragment,
       "gs2124IpOption": gs2124IpOption,
       "gs2124SipFilter": gs2124SipFilter,
       "gs2124SipAddress": gs2124SipAddress,
       "gs2124SipMask": gs2124SipMask,
       "gs2124DipFilter": gs2124DipFilter,
       "gs2124DipAddress": gs2124DipAddress,
       "gs2124DipMask": gs2124DipMask,
       "gs2124IcmpTypeFilter": gs2124IcmpTypeFilter,
       "gs2124IcmpCodeFilter": gs2124IcmpCodeFilter,
       "gs2124UdpSourcePortFilter": gs2124UdpSourcePortFilter,
       "gs2124UdpDestPortFilter": gs2124UdpDestPortFilter,
       "gs2124TcpSourcePortFilter": gs2124TcpSourcePortFilter,
       "gs2124TcpDestPortFilter": gs2124TcpDestPortFilter,
       "gs2124TcpFIN": gs2124TcpFIN,
       "gs2124TcpSYN": gs2124TcpSYN,
       "gs2124TcpRST": gs2124TcpRST,
       "gs2124TcpPSH": gs2124TcpPSH,
       "gs2124TcpACK": gs2124TcpACK,
       "gs2124TcpURG": gs2124TcpURG,
       "gs2124AclInfoEntryAction": gs2124AclInfoEntryAction,
       "gs2124AclInfoConf": gs2124AclInfoConf,
       "gs2124AceNo": gs2124AceNo,
       "gs2124AceMoveTo": gs2124AceMoveTo,
       "gs2124AceIngressPortConf": gs2124AceIngressPortConf,
       "gs2124AceFrameTypeConf": gs2124AceFrameTypeConf,
       "gs2124AceFrameTypeParameters": gs2124AceFrameTypeParameters,
       "gs2124EthernetTypeFilter": gs2124EthernetTypeFilter,
       "gs2124AclArpParameters": gs2124AclArpParameters,
       "gs2124AceArpRarp": gs2124AceArpRarp,
       "gs2124AceArpRequestReply": gs2124AceArpRequestReply,
       "gs2124AceArpSenderIpFilter": gs2124AceArpSenderIpFilter,
       "gs2124AceArpSenderIpAddress": gs2124AceArpSenderIpAddress,
       "gs2124AceArpSenderIpMask": gs2124AceArpSenderIpMask,
       "gs2124AceArpTargetIpFilter": gs2124AceArpTargetIpFilter,
       "gs2124AceArpTargetIpAddress": gs2124AceArpTargetIpAddress,
       "gs2124AceArpTargetIpMask": gs2124AceArpTargetIpMask,
       "gs2124AceArpSmacMatch": gs2124AceArpSmacMatch,
       "gs2124AceArpRarpDmacMatch": gs2124AceArpRarpDmacMatch,
       "gs2124AceArpIpEthernetLength": gs2124AceArpIpEthernetLength,
       "gs2124AceArpIp": gs2124AceArpIp,
       "gs2124AceArpEthernet": gs2124AceArpEthernet,
       "gs2124AclIpParameters": gs2124AclIpParameters,
       "gs2124AceIpProtocolFilter": gs2124AceIpProtocolFilter,
       "gs2124AceIpProtocolFilterParameters": gs2124AceIpProtocolFilterParameters,
       "gs2124AceIcmpParameters": gs2124AceIcmpParameters,
       "gs2124AceIcmpTypeFilter": gs2124AceIcmpTypeFilter,
       "gs2124AceIcmpCodeFilter": gs2124AceIcmpCodeFilter,
       "gs2124AceUdpParameters": gs2124AceUdpParameters,
       "gs2124UdpSourcePortFilterConf": gs2124UdpSourcePortFilterConf,
       "gs2124UdpDestPortFilterConf": gs2124UdpDestPortFilterConf,
       "gs2124AceTcpParameters": gs2124AceTcpParameters,
       "gs2124TcpSourcePortFilterConf": gs2124TcpSourcePortFilterConf,
       "gs2124TcpDestPortFilterConf": gs2124TcpDestPortFilterConf,
       "gs2124TcpFINConf": gs2124TcpFINConf,
       "gs2124TcpSYNConf": gs2124TcpSYNConf,
       "gs2124TcpRSTConf": gs2124TcpRSTConf,
       "gs2124TcpPSHConf": gs2124TcpPSHConf,
       "gs2124TcpACKConf": gs2124TcpACKConf,
       "gs2124TcpURGConf": gs2124TcpURGConf,
       "gs2124AceIpProtocolValue": gs2124AceIpProtocolValue,
       "gs2124AceIpTTL": gs2124AceIpTTL,
       "gs2124AceIpFragment": gs2124AceIpFragment,
       "gs2124AceIpOption": gs2124AceIpOption,
       "gs2124AceSipFilter": gs2124AceSipFilter,
       "gs2124AceSipAddress": gs2124AceSipAddress,
       "gs2124AceSipMask": gs2124AceSipMask,
       "gs2124AceDipFilter": gs2124AceDipFilter,
       "gs2124AceDipAddress": gs2124AceDipAddress,
       "gs2124AceDipMask": gs2124AceDipMask,
       "gs2124AceActionConf": gs2124AceActionConf,
       "gs2124AceRateLimiterConf": gs2124AceRateLimiterConf,
       "gs2124AcePortCopyConf": gs2124AcePortCopyConf,
       "gs2124AceMacParameters": gs2124AceMacParameters,
       "gs2124AceSmacFilter": gs2124AceSmacFilter,
       "gs2124AceDmacFilter": gs2124AceDmacFilter,
       "gs2124AceVlanParameters": gs2124AceVlanParameters,
       "gs2124AceVlanIdFilter": gs2124AceVlanIdFilter,
       "gs2124AceTagPriority": gs2124AceTagPriority,
       "gs2124AceInfoEntryAction": gs2124AceInfoEntryAction,
       "gs2124IpMacBind": gs2124IpMacBind,
       "gs2124IpMacBindConf": gs2124IpMacBindConf,
       "gs2124IpMacBindstate": gs2124IpMacBindstate,
       "gs2124IpMacBindTrustPort": gs2124IpMacBindTrustPort,
       "gs2124IpMacBindSetting": gs2124IpMacBindSetting,
       "gs2124IpMacBindSettingNumber": gs2124IpMacBindSettingNumber,
       "gs2124IpMacBindSettingEntryCreate": gs2124IpMacBindSettingEntryCreate,
       "gs2124IpMacBindSettingTable": gs2124IpMacBindSettingTable,
       "gs2124IpMacBindSettingEntry": gs2124IpMacBindSettingEntry,
       "gs2124IpMacBindSettingIndex": gs2124IpMacBindSettingIndex,
       "gs2124IpMacBindSettingMAC": gs2124IpMacBindSettingMAC,
       "gs2124IpMacBindSettingIP": gs2124IpMacBindSettingIP,
       "gs2124IpMacBindSettingPort": gs2124IpMacBindSettingPort,
       "gs2124IpMacBindSettingVID": gs2124IpMacBindSettingVID,
       "gs2124IpMacBindSettingEntryAction": gs2124IpMacBindSettingEntryAction,
       "gs2124TrapEntry": gs2124TrapEntry,
       "gs2124UserLogin": gs2124UserLogin,
       "gs2124UserLogout": gs2124UserLogout,
       "gs2124ModuleInserted": gs2124ModuleInserted,
       "gs2124ModuleRemoved": gs2124ModuleRemoved,
       "gs2124DualMediaSwapped": gs2124DualMediaSwapped,
       "gs2124LoopDetected": gs2124LoopDetected,
       "gs2124StpStateDisabled": gs2124StpStateDisabled,
       "gs2124StpStateEnabled": gs2124StpStateEnabled,
       "gs2124StpTopologyChanged": gs2124StpTopologyChanged,
       "gs2124LacpStateDisabled": gs2124LacpStateDisabled,
       "gs2124LacpStateEnabled": gs2124LacpStateEnabled,
       "gs2124LacpPortAdded": gs2124LacpPortAdded,
       "gs2124LacpPortTrunkFailure": gs2124LacpPortTrunkFailure,
       "gs2124GvrpStateDisabled": gs2124GvrpStateDisabled,
       "gs2124GvrpStateEnabled": gs2124GvrpStateEnabled,
       "gs2124VlanPortBaseEnabled": gs2124VlanPortBaseEnabled,
       "gs2124VlanTagBaseEnabled": gs2124VlanTagBaseEnabled,
       "gs2124IpmbStateEnabled": gs2124IpmbStateEnabled,
       "gs2124IpmbStateDisabled": gs2124IpmbStateDisabled,
       "gs2124IpmbEntryFailure": gs2124IpmbEntryFailure,
       "gs2124TrapVariable": gs2124TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "swapto": swapto,
       "ipmacIp": ipmacIp,
       "ipmacMac": ipmacMac,
       "gs2124Dot1X": gs2124Dot1X,
       "gs2124Dot1XServerConf": gs2124Dot1XServerConf,
       "gs2124Dot1XServerConfAuthenticationServerIp": gs2124Dot1XServerConfAuthenticationServerIp,
       "gs2124Dot1XServerConfAuthenticationUdpPort": gs2124Dot1XServerConfAuthenticationUdpPort,
       "gs2124Dot1XServerConfAuthenticationServerIp2": gs2124Dot1XServerConfAuthenticationServerIp2,
       "gs2124Dot1XServerConfAuthenticationUdpPort2": gs2124Dot1XServerConfAuthenticationUdpPort2,
       "gs2124Dot1XServerConfAuthenticationSecretKey": gs2124Dot1XServerConfAuthenticationSecretKey,
       "gs2124Dot1XServerConfAccountingServerIp": gs2124Dot1XServerConfAccountingServerIp,
       "gs2124Dot1XServerConfAccountingUdpPort": gs2124Dot1XServerConfAccountingUdpPort,
       "gs2124Dot1XServerConfAccountingServerIp2": gs2124Dot1XServerConfAccountingServerIp2,
       "gs2124Dot1XServerConfAccountingUdpPort2": gs2124Dot1XServerConfAccountingUdpPort2,
       "gs2124Dot1XServerConfAccountingSecretKey": gs2124Dot1XServerConfAccountingSecretKey,
       "gs2124Dot1XPortConfTable": gs2124Dot1XPortConfTable,
       "gs2124Dot1XPortConfEntry": gs2124Dot1XPortConfEntry,
       "gs2124Dot1XPort": gs2124Dot1XPort,
       "gs2124Dot1XPortMode": gs2124Dot1XPortMode,
       "gs2124Dot1XPortControl": gs2124Dot1XPortControl,
       "gs2124Dot1XPortreAuthMax": gs2124Dot1XPortreAuthMax,
       "gs2124Dot1XPorttxPeriod": gs2124Dot1XPorttxPeriod,
       "gs2124Dot1XPortquietPeriod": gs2124Dot1XPortquietPeriod,
       "gs2124Dot1XPortreAuthEnabled": gs2124Dot1XPortreAuthEnabled,
       "gs2124Dot1XPortreAuthPeriod": gs2124Dot1XPortreAuthPeriod,
       "gs2124Dot1XPortmaxReq": gs2124Dot1XPortmaxReq,
       "gs2124Dot1XPortsuppTimeout": gs2124Dot1XPortsuppTimeout,
       "gs2124Dot1XPortserverTimeout": gs2124Dot1XPortserverTimeout,
       "gs2124Dot1XPortVlanAssignment": gs2124Dot1XPortVlanAssignment,
       "gs2124Dot1XPortGuestVlan": gs2124Dot1XPortGuestVlan,
       "gs2124Dot1XPortAuthFailedVlan": gs2124Dot1XPortAuthFailedVlan,
       "gs2124Dot1XStatusTable": gs2124Dot1XStatusTable,
       "gs2124Dot1XStatusEntry": gs2124Dot1XStatusEntry,
       "gs2124Dot1XStatusIndex": gs2124Dot1XStatusIndex,
       "gs2124Dot1XStatusMode": gs2124Dot1XStatusMode,
       "gs2124Dot1XStatusStatus": gs2124Dot1XStatusStatus,
       "gs2124Dot1XVlanPlicy": gs2124Dot1XVlanPlicy,
       "gs2124Dot1XStatisticsTable": gs2124Dot1XStatisticsTable,
       "gs2124Dot1XStatisticsEntry": gs2124Dot1XStatisticsEntry,
       "gs2124Dot1XStatisticsIndex": gs2124Dot1XStatisticsIndex,
       "gs2124Dot1XClearCounter": gs2124Dot1XClearCounter,
       "gs2124Dot1XAuthEntersConnecting": gs2124Dot1XAuthEntersConnecting,
       "gs2124Dot1XauthEapLogoffsWhileConnecting": gs2124Dot1XauthEapLogoffsWhileConnecting,
       "gs2124Dot1XAuthEntersAuthenticating": gs2124Dot1XAuthEntersAuthenticating,
       "gs2124Dot1XAuthAuthSuccessesWhileAuthenticating": gs2124Dot1XAuthAuthSuccessesWhileAuthenticating,
       "gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating": gs2124Dot1XAuthAuthTimeoutsWhileAuthenticating,
       "gs2124Dot1XAuthAuthFailWhileAuthenticating": gs2124Dot1XAuthAuthFailWhileAuthenticating,
       "gs2124Dot1XAuthAuthEapStartsWhileAuthenticating": gs2124Dot1XAuthAuthEapStartsWhileAuthenticating,
       "gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating": gs2124Dot1XAuthAuthEapLogoffWhileAuthenticating,
       "gs2124Dot1XAuthAuthReauthsWhileAuthenticated": gs2124Dot1XAuthAuthReauthsWhileAuthenticated,
       "gs2124Dot1XAuthAuthEapStartsWhileAuthenticated": gs2124Dot1XAuthAuthEapStartsWhileAuthenticated,
       "gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated": gs2124Dot1XAuthAuthEapLogoffWhileAuthenticated,
       "gs2124Dot1XBackendResponses": gs2124Dot1XBackendResponses,
       "gs2124Dot1XBackendAccessChallenges": gs2124Dot1XBackendAccessChallenges,
       "gs2124Dot1XBackendOtherRequestsToSupplicant": gs2124Dot1XBackendOtherRequestsToSupplicant,
       "gs2124Dot1XBackendAuthSuccesses": gs2124Dot1XBackendAuthSuccesses,
       "gs2124Dot1XBackendAuthFails": gs2124Dot1XBackendAuthFails,
       "gs2124Dot1XAuthEapolFramesRx": gs2124Dot1XAuthEapolFramesRx,
       "gs2124Dot1XAuthEapolFramesTx": gs2124Dot1XAuthEapolFramesTx,
       "gs2124Dot1XAuthEapolStartFramesRx": gs2124Dot1XAuthEapolStartFramesRx,
       "gs2124Dot1XAuthEapolLogoffFramesRx": gs2124Dot1XAuthEapolLogoffFramesRx,
       "gs2124Dot1XAuthEapolRespIdFramesRx": gs2124Dot1XAuthEapolRespIdFramesRx,
       "gs2124Dot1XAuthEapolRespFramesRx": gs2124Dot1XAuthEapolRespFramesRx,
       "gs2124Dot1XAuthEapolReqIdFramesTx": gs2124Dot1XAuthEapolReqIdFramesTx,
       "gs2124Dot1XAuthEapolReqFramesTx": gs2124Dot1XAuthEapolReqFramesTx,
       "gs2124Dot1XAuthInvalidEapolFramesRx": gs2124Dot1XAuthInvalidEapolFramesRx,
       "gs2124Dot1XAuthEapLengthErrorFramesRx": gs2124Dot1XAuthEapLengthErrorFramesRx,
       "gs2124Dot1XAuthLastEapolFrameVersion": gs2124Dot1XAuthLastEapolFrameVersion,
       "gs2124Dot1XAuthLastEapolFrameSource": gs2124Dot1XAuthLastEapolFrameSource,
       "gs2124TrunkInfo": gs2124TrunkInfo,
       "gs2124TrunkPort": gs2124TrunkPort,
       "gs2124TrunkPortTable": gs2124TrunkPortTable,
       "gs2124TrunkPortEntry": gs2124TrunkPortEntry,
       "gs2124TrunkPortIndex": gs2124TrunkPortIndex,
       "gs2124TrunkPortMethod": gs2124TrunkPortMethod,
       "gs2124TrunkPortGroup": gs2124TrunkPortGroup,
       "gs2124TrunkPortActiveLacp": gs2124TrunkPortActiveLacp,
       "gs2124TrunkPortAggtr": gs2124TrunkPortAggtr,
       "gs2124TrunkPortStatus": gs2124TrunkPortStatus,
       "gs2124TrunkPortCurrentMode": gs2124TrunkPortCurrentMode,
       "gs2124AggregatorView": gs2124AggregatorView,
       "gs2124AggregatorViewTable": gs2124AggregatorViewTable,
       "gs2124AggregatorViewEntry": gs2124AggregatorViewEntry,
       "gs2124AggregatorViewIndex": gs2124AggregatorViewIndex,
       "gs2124AggregatorViewMethod": gs2124AggregatorViewMethod,
       "gs2124AggregatorViewMemberPorts": gs2124AggregatorViewMemberPorts,
       "gs2124AggregatorViewReadyPorts": gs2124AggregatorViewReadyPorts,
       "gs2124LacpSystemPriority": gs2124LacpSystemPriority,
       "gs2124AggregationHashMode": gs2124AggregationHashMode,
       "gs2124HashCodeSourceMacAddress": gs2124HashCodeSourceMacAddress,
       "gs2124HashCodeDestinationMacAddress": gs2124HashCodeDestinationMacAddress,
       "gs2124HashCodeIpAddress": gs2124HashCodeIpAddress,
       "gs2124HashCodeTcpUdpPortNumber": gs2124HashCodeTcpUdpPortNumber,
       "gs2124MulticastInfo": gs2124MulticastInfo,
       "gs2124IGMPMode": gs2124IGMPMode,
       "gs2124IGMPGroupAllowConf": gs2124IGMPGroupAllowConf,
       "gs2124IGMPGroupAllowNumber": gs2124IGMPGroupAllowNumber,
       "gs2124IGMPGroupAllowEntryCreate": gs2124IGMPGroupAllowEntryCreate,
       "gs2124IGMPGroupAllowTable": gs2124IGMPGroupAllowTable,
       "gs2124IGMPGroupAllowEntry": gs2124IGMPGroupAllowEntry,
       "gs2124IGMPGroupAllowNo": gs2124IGMPGroupAllowNo,
       "gs2124IGMPGroupAllowVid": gs2124IGMPGroupAllowVid,
       "gs2124IGMPGroupAllowStartAddress": gs2124IGMPGroupAllowStartAddress,
       "gs2124IGMPGroupAllowEndAddress": gs2124IGMPGroupAllowEndAddress,
       "gs2124IGMPGroupAllowEntryAction": gs2124IGMPGroupAllowEntryAction,
       "gs2124IGMPProxy": gs2124IGMPProxy,
       "gs2124IgmpProxyConfGeneralQueryInterval": gs2124IgmpProxyConfGeneralQueryInterval,
       "gs2124IgmpProxyConfGeneralQueryRepTimeout": gs2124IgmpProxyConfGeneralQueryRepTimeout,
       "gs2124IgmpProxyConfGeneralQueryMaxRepTime": gs2124IgmpProxyConfGeneralQueryMaxRepTime,
       "gs2124IgmpProxyConfLastMemberQueryCount": gs2124IgmpProxyConfLastMemberQueryCount,
       "gs2124IgmpProxyConfLastMemberQueryInterval": gs2124IgmpProxyConfLastMemberQueryInterval,
       "gs2124IgmpProxyConfLastMemberQueryMaxRepTime": gs2124IgmpProxyConfLastMemberQueryMaxRepTime,
       "gs2124IgmpProxyConfRouterPorts": gs2124IgmpProxyConfRouterPorts,
       "gs2124IgmpProxyGroupMembershipNumber": gs2124IgmpProxyGroupMembershipNumber,
       "gs2124IgmpProxyGroupMembershipTable": gs2124IgmpProxyGroupMembershipTable,
       "gs2124IgmpProxyGroupMembershipEntry": gs2124IgmpProxyGroupMembershipEntry,
       "gs2124IgmpProxyGroupNo": gs2124IgmpProxyGroupNo,
       "gs2124IgmpProxyGroupAddress": gs2124IgmpProxyGroupAddress,
       "gs2124IgmpProxyGroupVLANId": gs2124IgmpProxyGroupVLANId,
       "gs2124IgmpProxyGroupPortMembers": gs2124IgmpProxyGroupPortMembers,
       "gs2124IGMPSnooping": gs2124IGMPSnooping,
       "gs2124IgmpSnoopingConfHostTimeout": gs2124IgmpSnoopingConfHostTimeout,
       "gs2124IgmpSnoopingConfFastLeave": gs2124IgmpSnoopingConfFastLeave,
       "gs2124IgmpSnoopingConfRouterPorts": gs2124IgmpSnoopingConfRouterPorts,
       "gs2124IgmpSnoopingGroupMembershipNumber": gs2124IgmpSnoopingGroupMembershipNumber,
       "gs2124IgmpSnoopingGroupMembershipTable": gs2124IgmpSnoopingGroupMembershipTable,
       "gs2124IgmpSnoopingGroupMembershipEntry": gs2124IgmpSnoopingGroupMembershipEntry,
       "gs2124IgmpSnoopingGroupNo": gs2124IgmpSnoopingGroupNo,
       "gs2124IgmpSnoopingGroupAddress": gs2124IgmpSnoopingGroupAddress,
       "gs2124IgmpSnoopingGroupVLANId": gs2124IgmpSnoopingGroupVLANId,
       "gs2124IgmpSnoopingGroupPortMembers": gs2124IgmpSnoopingGroupPortMembers,
       "gs2124MVR": gs2124MVR,
       "gs2124MVRMode": gs2124MVRMode,
       "gs2124MVRConfHostTimeout": gs2124MVRConfHostTimeout,
       "gs2124MVRConfFastLeave": gs2124MVRConfFastLeave,
       "gs2124MVIDConf": gs2124MVIDConf,
       "gs2124MVIDNumber": gs2124MVIDNumber,
       "gs2124MVIDEntryCreate": gs2124MVIDEntryCreate,
       "gs2124MVIDGroupTable": gs2124MVIDGroupTable,
       "gs2124MVIDGroupEntry": gs2124MVIDGroupEntry,
       "gs2124MVID": gs2124MVID,
       "gs2124MVIDMemberPort": gs2124MVIDMemberPort,
       "gs2124MVIDRouterPorts": gs2124MVIDRouterPorts,
       "gs2124MVIDEntryAction": gs2124MVIDEntryAction,
       "gs2124MVIDGroupAllowConf": gs2124MVIDGroupAllowConf,
       "gs2124MVIDGroupAllowNumber": gs2124MVIDGroupAllowNumber,
       "gs2124MVIDGroupAllowEntryCreate": gs2124MVIDGroupAllowEntryCreate,
       "gs2124MVIDGroupAllowTable": gs2124MVIDGroupAllowTable,
       "gs2124MVIDGroupAllowEntry": gs2124MVIDGroupAllowEntry,
       "gs2124MVIDGroupAllowNo": gs2124MVIDGroupAllowNo,
       "gs2124MVIDGroupAllowMvid": gs2124MVIDGroupAllowMvid,
       "gs2124MVIDGroupAllowStartAddress": gs2124MVIDGroupAllowStartAddress,
       "gs2124MVIDGroupAllowEndAddress": gs2124MVIDGroupAllowEndAddress,
       "gs2124MVIDGroupAllowEntryAction": gs2124MVIDGroupAllowEntryAction,
       "gs2124MVRGroupMembershipNumber": gs2124MVRGroupMembershipNumber,
       "gs2124MVRGroupMembershipTable": gs2124MVRGroupMembershipTable,
       "gs2124MVRGroupMembershipEntry": gs2124MVRGroupMembershipEntry,
       "gs2124MVRGroupNo": gs2124MVRGroupNo,
       "gs2124MVRGroupAddress": gs2124MVRGroupAddress,
       "gs2124MVRGroupVLANId": gs2124MVRGroupVLANId,
       "gs2124MVRGroupPortMembers": gs2124MVRGroupPortMembers,
       "gs2124DhcpSnooping": gs2124DhcpSnooping,
       "gs2124DhcpSnoopingState": gs2124DhcpSnoopingState,
       "gs2124DhcpSnoopingInfo": gs2124DhcpSnoopingInfo,
       "gs2124DhcpSnoopingCreate": gs2124DhcpSnoopingCreate,
       "gs2124DhcpSnoopingTable": gs2124DhcpSnoopingTable,
       "gs2124DhcpSnoopingEntry": gs2124DhcpSnoopingEntry,
       "gs2124DhcpSnoopingIndex": gs2124DhcpSnoopingIndex,
       "gs2124DhcpSnoopingVID": gs2124DhcpSnoopingVID,
       "gs2124DhcpSnoopingTrustPort1": gs2124DhcpSnoopingTrustPort1,
       "gs2124DhcpSnoopingTrustPort2": gs2124DhcpSnoopingTrustPort2,
       "gs2124DhcpSnoopingServerIP": gs2124DhcpSnoopingServerIP,
       "gs2124DhcpSnoopingOption82": gs2124DhcpSnoopingOption82,
       "gs2124DhcpSnoopingAction": gs2124DhcpSnoopingAction,
       "gs2124DhcpSnoopingEntryAction": gs2124DhcpSnoopingEntryAction,
       "gs2124DhcpSnoopingDefaultData": gs2124DhcpSnoopingDefaultData,
       "gs2124DhcpSnoopingDefaultVID": gs2124DhcpSnoopingDefaultVID,
       "gs2124DhcpSnoopingDefaultTrustPort1": gs2124DhcpSnoopingDefaultTrustPort1,
       "gs2124DhcpSnoopingDefaultTrustPort2": gs2124DhcpSnoopingDefaultTrustPort2,
       "gs2124DhcpSnoopingDefaultServerIP": gs2124DhcpSnoopingDefaultServerIP,
       "gs2124DhcpSnoopingDefaultOption82": gs2124DhcpSnoopingDefaultOption82,
       "gs2124DhcpSnoopingDefaultAction": gs2124DhcpSnoopingDefaultAction,
       "gs2124DhcpSnoopingDefaultEntryAction": gs2124DhcpSnoopingDefaultEntryAction,
       "gs2124DhcpSnoopingClientTable": gs2124DhcpSnoopingClientTable,
       "gs2124DhcpSnoopingClientEntry": gs2124DhcpSnoopingClientEntry,
       "gs2124DhcpSnoopingClientIndex": gs2124DhcpSnoopingClientIndex,
       "gs2124DhcpSnoopingClientMac": gs2124DhcpSnoopingClientMac,
       "gs2124DhcpSnoopingClientVID": gs2124DhcpSnoopingClientVID,
       "gs2124DhcpSnoopingClientPort": gs2124DhcpSnoopingClientPort,
       "gs2124DhcpSnoopingClientIP": gs2124DhcpSnoopingClientIP,
       "gs2124DhcpSnoopingClientLease": gs2124DhcpSnoopingClientLease,
       "gs2124mstpMIB": gs2124mstpMIB,
       "gs2124mstpInstanceView": gs2124mstpInstanceView,
       "gs2124mstpInstanceEntryCreate": gs2124mstpInstanceEntryCreate,
       "gs2124mstpInstanceViewTable": gs2124mstpInstanceViewTable,
       "gs2124mstpInstanceViewEntry": gs2124mstpInstanceViewEntry,
       "gs2124mstpInstanceViewIndex": gs2124mstpInstanceViewIndex,
       "gs2124mstpInstanceViewInstance": gs2124mstpInstanceViewInstance,
       "gs2124mstpInstanceViewCorrespondingVlans": gs2124mstpInstanceViewCorrespondingVlans,
       "gs2124mstpInstanceViewEntryAction": gs2124mstpInstanceViewEntryAction,
       "gs2124mstpGen": gs2124mstpGen,
       "gs2124mstpGenSupported": gs2124mstpGenSupported,
       "gs2124mstpGenVersion": gs2124mstpGenVersion,
       "gs2124mstpGenCfgIdFmtSel": gs2124mstpGenCfgIdFmtSel,
       "gs2124mstpGenCfgIdName": gs2124mstpGenCfgIdName,
       "gs2124mstpGenCfgIdRevLevel": gs2124mstpGenCfgIdRevLevel,
       "gs2124mstpGenBridgeMaxAge": gs2124mstpGenBridgeMaxAge,
       "gs2124mstpGenBridgeFwdDelay": gs2124mstpGenBridgeFwdDelay,
       "gs2124mstpGenBridgeMaxHops": gs2124mstpGenBridgeMaxHops,
       "gs2124mstpGenInstancePriority": gs2124mstpGenInstancePriority,
       "gs2124mstpGenCistRootPriority": gs2124mstpGenCistRootPriority,
       "gs2124mstpGenCistRootMac": gs2124mstpGenCistRootMac,
       "gs2124mstpGenCistExtRootPathCost": gs2124mstpGenCistExtRootPathCost,
       "gs2124mstpGenCistRootPortId": gs2124mstpGenCistRootPortId,
       "gs2124mstpGenCistRegionalRootPriority": gs2124mstpGenCistRegionalRootPriority,
       "gs2124mstpGenCistRegionalRootMac": gs2124mstpGenCistRegionalRootMac,
       "gs2124mstpGenCistInternalRootPathCost": gs2124mstpGenCistInternalRootPathCost,
       "gs2124mstpGenCistCurrentMaxAge": gs2124mstpGenCistCurrentMaxAge,
       "gs2124mstpGenCistCurrentFwdDelay": gs2124mstpGenCistCurrentFwdDelay,
       "gs2124mstpGenTimeSinceLastTopoChange": gs2124mstpGenTimeSinceLastTopoChange,
       "gs2124mstpGenTopoChangeCount": gs2124mstpGenTopoChangeCount,
       "gs2124mstpMstiStatusTable": gs2124mstpMstiStatusTable,
       "gs2124mstpMstiStatusEntry": gs2124mstpMstiStatusEntry,
       "gs2124mstpMstiStatusInstanceIndex": gs2124mstpMstiStatusInstanceIndex,
       "gs2124mstpMstiStatusState": gs2124mstpMstiStatusState,
       "gs2124mstpMstiStatusPriority": gs2124mstpMstiStatusPriority,
       "gs2124mstpMstiStatusBridgeMac": gs2124mstpMstiStatusBridgeMac,
       "gs2124mstpMstiStatusRegionalRootPriority": gs2124mstpMstiStatusRegionalRootPriority,
       "gs2124mstpMstiStatusRegionalRootMac": gs2124mstpMstiStatusRegionalRootMac,
       "gs2124mstpMstiStatusInternalRootPathCost": gs2124mstpMstiStatusInternalRootPathCost,
       "gs2124mstpMstiStatusRootPortId": gs2124mstpMstiStatusRootPortId,
       "gs2124mstpMstiStatusTimeSinceLastTopoChg": gs2124mstpMstiStatusTimeSinceLastTopoChg,
       "gs2124mstpMstiStatusTopochgcount": gs2124mstpMstiStatusTopochgcount,
       "gs2124mstpPortCfg": gs2124mstpPortCfg,
       "gs2124mstpCistPortCfgTable": gs2124mstpCistPortCfgTable,
       "gs2124mstpCistPortCfgEntry": gs2124mstpCistPortCfgEntry,
       "gs2124mstpCistPortCfgPortIndex": gs2124mstpCistPortCfgPortIndex,
       "gs2124mstpCistPortCfgPathCost": gs2124mstpCistPortCfgPathCost,
       "gs2124mstpCistPortCfgPriority": gs2124mstpCistPortCfgPriority,
       "gs2124mstpCistPortCfgHelloTime": gs2124mstpCistPortCfgHelloTime,
       "gs2124mstpCistPortCfgAdminEdge": gs2124mstpCistPortCfgAdminEdge,
       "gs2124mstpCistPortCfgP2P": gs2124mstpCistPortCfgP2P,
       "gs2124mstpCistPortCfgRestrictedRole": gs2124mstpCistPortCfgRestrictedRole,
       "gs2124mstpCistPortCfgRestrictedTcn": gs2124mstpCistPortCfgRestrictedTcn,
       "gs2124mstpCistPortCfgMigrationCheck": gs2124mstpCistPortCfgMigrationCheck,
       "gs2124mstpMstiPortCfgTable": gs2124mstpMstiPortCfgTable,
       "gs2124mstpMstiPortCfgEntry": gs2124mstpMstiPortCfgEntry,
       "gs2124mstpMstiPortCfgInstanceIndex": gs2124mstpMstiPortCfgInstanceIndex,
       "gs2124mstpMstiPortCfgPortIndex": gs2124mstpMstiPortCfgPortIndex,
       "gs2124mstpMstiPortCfgPathCost": gs2124mstpMstiPortCfgPathCost,
       "gs2124mstpMstiPortCfgPriority": gs2124mstpMstiPortCfgPriority,
       "gs2124mstpCfg": gs2124mstpCfg,
       "gs2124mstpCfgCist": gs2124mstpCfgCist,
       "gs2124mstpCfgCistPriority": gs2124mstpCfgCistPriority,
       "gs2124mstpCfgCistMaxAge": gs2124mstpCfgCistMaxAge,
       "gs2124mstpCfgCistFwdDelay": gs2124mstpCfgCistFwdDelay,
       "gs2124mstpCfgCistMaxHops": gs2124mstpCfgCistMaxHops,
       "gs2124mstpCfgMstiTable": gs2124mstpCfgMstiTable,
       "gs2124mstpCfgMstiEntry": gs2124mstpCfgMstiEntry,
       "gs2124mstpCfgMstiInstanceIndex": gs2124mstpCfgMstiInstanceIndex,
       "gs2124mstpCfgMstiPriority": gs2124mstpCfgMstiPriority,
       "gs2124mstpPortStatus": gs2124mstpPortStatus,
       "gs2124mstpCistPortStatusTable": gs2124mstpCistPortStatusTable,
       "gs2124mstpCistPortStatusEntry": gs2124mstpCistPortStatusEntry,
       "gs2124mstpCistPortStatusPortIndex": gs2124mstpCistPortStatusPortIndex,
       "gs2124mstpCistPortStatusStatus": gs2124mstpCistPortStatusStatus,
       "gs2124mstpCistPortStatusRole": gs2124mstpCistPortStatusRole,
       "gs2124mstpCistPortStatusPathCost": gs2124mstpCistPortStatusPathCost,
       "gs2124mstpCistPortStatusPriority": gs2124mstpCistPortStatusPriority,
       "gs2124mstpCistPortStatusHelloTime": gs2124mstpCistPortStatusHelloTime,
       "gs2124mstpCistPortStatusOperEdge": gs2124mstpCistPortStatusOperEdge,
       "gs2124mstpCistPortStatusOperP2P": gs2124mstpCistPortStatusOperP2P,
       "gs2124mstpCistPortStatusRestrictedRole": gs2124mstpCistPortStatusRestrictedRole,
       "gs2124mstpCistPortStatusRestrictedTcn": gs2124mstpCistPortStatusRestrictedTcn,
       "gs2124mstpMstiPortStatusTable": gs2124mstpMstiPortStatusTable,
       "gs2124mstpMstiPortStatusEntry": gs2124mstpMstiPortStatusEntry,
       "gs2124mstpMstiPortStatusInstanceIndex": gs2124mstpMstiPortStatusInstanceIndex,
       "gs2124mstpMstiPortStatusPortIndex": gs2124mstpMstiPortStatusPortIndex,
       "gs2124mstpMstiPortStatusStatus": gs2124mstpMstiPortStatusStatus,
       "gs2124mstpMstiPortStatusRole": gs2124mstpMstiPortStatusRole,
       "gs2124mstpMstiPortStatusPathCost": gs2124mstpMstiPortStatusPathCost,
       "gs2124mstpMstiPortStatusPriority": gs2124mstpMstiPortStatusPriority,
       "gs2124mstpMstiPortStatusHelloTime": gs2124mstpMstiPortStatusHelloTime,
       "gs2124mstpMstiPortStatusOperEdge": gs2124mstpMstiPortStatusOperEdge,
       "gs2124mstpMstiPortStatusOperP2P": gs2124mstpMstiPortStatusOperP2P,
       "gs2124mstpMstiPortStatusRestrictedRole": gs2124mstpMstiPortStatusRestrictedRole,
       "gs2124mstpMstiPortStatusRestrictedTcn": gs2124mstpMstiPortStatusRestrictedTcn}
)
