# SNMP MIB module (PRIVATE-FESW-26-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rubytech/PRIVATE-FESW-26-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:39 2025
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

privatetech = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5205)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2)
)
_FeSW26ProductID_ObjectIdentity = ObjectIdentity
feSW26ProductID = _FeSW26ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16)
)
_FeSW26Produces_ObjectIdentity = ObjectIdentity
feSW26Produces = _FeSW26Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1)
)
_FeSW26System_ObjectIdentity = ObjectIdentity
feSW26System = _FeSW26System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1)
)
_FeSW26CommonSys_ObjectIdentity = ObjectIdentity
feSW26CommonSys = _FeSW26CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1)
)


class _FeSW26Reboot_Type(Integer32):
    """Custom type feSW26Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeSW26Reboot_Type.__name__ = "Integer32"
_FeSW26Reboot_Object = MibScalar
feSW26Reboot = _FeSW26Reboot_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 1),
    _FeSW26Reboot_Type()
)
feSW26Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26Reboot.setStatus("current")
_FeSW26BiosVsersion_Type = DisplayString
_FeSW26BiosVsersion_Object = MibScalar
feSW26BiosVsersion = _FeSW26BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 2),
    _FeSW26BiosVsersion_Type()
)
feSW26BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26BiosVsersion.setStatus("current")
_FeSW26FirmwareVersion_Type = DisplayString
_FeSW26FirmwareVersion_Object = MibScalar
feSW26FirmwareVersion = _FeSW26FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 3),
    _FeSW26FirmwareVersion_Type()
)
feSW26FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26FirmwareVersion.setStatus("current")
_FeSW26HardwareVersion_Type = DisplayString
_FeSW26HardwareVersion_Object = MibScalar
feSW26HardwareVersion = _FeSW26HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 4),
    _FeSW26HardwareVersion_Type()
)
feSW26HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26HardwareVersion.setStatus("current")
_FeSW26MechanicalVersion_Type = DisplayString
_FeSW26MechanicalVersion_Object = MibScalar
feSW26MechanicalVersion = _FeSW26MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 5),
    _FeSW26MechanicalVersion_Type()
)
feSW26MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26MechanicalVersion.setStatus("current")
_FeSW26SerialNumber_Type = DisplayString
_FeSW26SerialNumber_Object = MibScalar
feSW26SerialNumber = _FeSW26SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 6),
    _FeSW26SerialNumber_Type()
)
feSW26SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26SerialNumber.setStatus("current")
_FeSW26HostMacAddress_Type = DisplayString
_FeSW26HostMacAddress_Object = MibScalar
feSW26HostMacAddress = _FeSW26HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 7),
    _FeSW26HostMacAddress_Type()
)
feSW26HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26HostMacAddress.setStatus("current")
_FeSW26DevicePort_Type = DisplayString
_FeSW26DevicePort_Object = MibScalar
feSW26DevicePort = _FeSW26DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 8),
    _FeSW26DevicePort_Type()
)
feSW26DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26DevicePort.setStatus("current")
_FeSW26RamSize_Type = DisplayString
_FeSW26RamSize_Object = MibScalar
feSW26RamSize = _FeSW26RamSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 9),
    _FeSW26RamSize_Type()
)
feSW26RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26RamSize.setStatus("current")
_FeSW26FlashSize_Type = DisplayString
_FeSW26FlashSize_Object = MibScalar
feSW26FlashSize = _FeSW26FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 1, 10),
    _FeSW26FlashSize_Type()
)
feSW26FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26FlashSize.setStatus("current")
_FeSW26IP_ObjectIdentity = ObjectIdentity
feSW26IP = _FeSW26IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2)
)


class _FeSW26DhcpSetting_Type(Integer32):
    """Custom type feSW26DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26DhcpSetting_Type.__name__ = "Integer32"
_FeSW26DhcpSetting_Object = MibScalar
feSW26DhcpSetting = _FeSW26DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2, 1),
    _FeSW26DhcpSetting_Type()
)
feSW26DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DhcpSetting.setStatus("current")
_FeSW26IPAddress_Type = IpAddress
_FeSW26IPAddress_Object = MibScalar
feSW26IPAddress = _FeSW26IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2, 2),
    _FeSW26IPAddress_Type()
)
feSW26IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26IPAddress.setStatus("current")
_FeSW26NetMask_Type = IpAddress
_FeSW26NetMask_Object = MibScalar
feSW26NetMask = _FeSW26NetMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2, 3),
    _FeSW26NetMask_Type()
)
feSW26NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26NetMask.setStatus("current")
_FeSW26DefaultGateway_Type = IpAddress
_FeSW26DefaultGateway_Object = MibScalar
feSW26DefaultGateway = _FeSW26DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2, 4),
    _FeSW26DefaultGateway_Type()
)
feSW26DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DefaultGateway.setStatus("current")


class _FeSW26DnsSetting_Type(Integer32):
    """Custom type feSW26DnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26DnsSetting_Type.__name__ = "Integer32"
_FeSW26DnsSetting_Object = MibScalar
feSW26DnsSetting = _FeSW26DnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2, 5),
    _FeSW26DnsSetting_Type()
)
feSW26DnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DnsSetting.setStatus("current")
_FeSW26DnsServer_Type = IpAddress
_FeSW26DnsServer_Object = MibScalar
feSW26DnsServer = _FeSW26DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 2, 6),
    _FeSW26DnsServer_Type()
)
feSW26DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DnsServer.setStatus("current")
_FeSW26Time_ObjectIdentity = ObjectIdentity
feSW26Time = _FeSW26Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3)
)
_FeSW26SystemCurrentTime_Type = DisplayString
_FeSW26SystemCurrentTime_Object = MibScalar
feSW26SystemCurrentTime = _FeSW26SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 1),
    _FeSW26SystemCurrentTime_Type()
)
feSW26SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26SystemCurrentTime.setStatus("current")
_FeSW26ManualTimeSetting_Type = DisplayString
_FeSW26ManualTimeSetting_Object = MibScalar
feSW26ManualTimeSetting = _FeSW26ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 2),
    _FeSW26ManualTimeSetting_Type()
)
feSW26ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26ManualTimeSetting.setStatus("current")
_FeSW26NTPServer_Type = DisplayString
_FeSW26NTPServer_Object = MibScalar
feSW26NTPServer = _FeSW26NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 3),
    _FeSW26NTPServer_Type()
)
feSW26NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26NTPServer.setStatus("current")


class _FeSW26NTPTimeZone_Type(Integer32):
    """Custom type feSW26NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_FeSW26NTPTimeZone_Type.__name__ = "Integer32"
_FeSW26NTPTimeZone_Object = MibScalar
feSW26NTPTimeZone = _FeSW26NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 4),
    _FeSW26NTPTimeZone_Type()
)
feSW26NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26NTPTimeZone.setStatus("current")


class _FeSW26NTPTimeSync_Type(Integer32):
    """Custom type feSW26NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26NTPTimeSync_Type.__name__ = "Integer32"
_FeSW26NTPTimeSync_Object = MibScalar
feSW26NTPTimeSync = _FeSW26NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 5),
    _FeSW26NTPTimeSync_Type()
)
feSW26NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26NTPTimeSync.setStatus("current")


class _FeSW26DaylightSavingTime_Type(Integer32):
    """Custom type feSW26DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_FeSW26DaylightSavingTime_Type.__name__ = "Integer32"
_FeSW26DaylightSavingTime_Object = MibScalar
feSW26DaylightSavingTime = _FeSW26DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 6),
    _FeSW26DaylightSavingTime_Type()
)
feSW26DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DaylightSavingTime.setStatus("current")
_FeSW26DaylightStartTime_Type = DisplayString
_FeSW26DaylightStartTime_Object = MibScalar
feSW26DaylightStartTime = _FeSW26DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 7),
    _FeSW26DaylightStartTime_Type()
)
feSW26DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DaylightStartTime.setStatus("current")
_FeSW26DaylightEndTime_Type = DisplayString
_FeSW26DaylightEndTime_Object = MibScalar
feSW26DaylightEndTime = _FeSW26DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 3, 8),
    _FeSW26DaylightEndTime_Type()
)
feSW26DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DaylightEndTime.setStatus("current")
_FeSW26Account_ObjectIdentity = ObjectIdentity
feSW26Account = _FeSW26Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4)
)


class _FeSW26AccountNumber_Type(Integer32):
    """Custom type feSW26AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FeSW26AccountNumber_Type.__name__ = "Integer32"
_FeSW26AccountNumber_Object = MibScalar
feSW26AccountNumber = _FeSW26AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 1),
    _FeSW26AccountNumber_Type()
)
feSW26AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26AccountNumber.setStatus("current")
_FeSW26AccountTable_Object = MibTable
feSW26AccountTable = _FeSW26AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    feSW26AccountTable.setStatus("current")
_FeSW26AccountEntry_Object = MibTableRow
feSW26AccountEntry = _FeSW26AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 2, 1)
)
feSW26AccountEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26AccountIndex"),
)
if mibBuilder.loadTexts:
    feSW26AccountEntry.setStatus("current")


class _FeSW26AccountIndex_Type(Integer32):
    """Custom type feSW26AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FeSW26AccountIndex_Type.__name__ = "Integer32"
_FeSW26AccountIndex_Object = MibTableColumn
feSW26AccountIndex = _FeSW26AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 2, 1, 1),
    _FeSW26AccountIndex_Type()
)
feSW26AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26AccountIndex.setStatus("current")
_FeSW26AccountAuthorization_Type = DisplayString
_FeSW26AccountAuthorization_Object = MibTableColumn
feSW26AccountAuthorization = _FeSW26AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 2, 1, 2),
    _FeSW26AccountAuthorization_Type()
)
feSW26AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26AccountAuthorization.setStatus("current")
_FeSW26AccountName_Type = DisplayString
_FeSW26AccountName_Object = MibTableColumn
feSW26AccountName = _FeSW26AccountName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 2, 1, 3),
    _FeSW26AccountName_Type()
)
feSW26AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26AccountName.setStatus("current")
_FeSW26AccountPassword_Type = DisplayString
_FeSW26AccountPassword_Object = MibTableColumn
feSW26AccountPassword = _FeSW26AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 2, 1, 4),
    _FeSW26AccountPassword_Type()
)
feSW26AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26AccountPassword.setStatus("current")
_FeSW26AccountAddName_Type = DisplayString
_FeSW26AccountAddName_Object = MibScalar
feSW26AccountAddName = _FeSW26AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 3),
    _FeSW26AccountAddName_Type()
)
feSW26AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26AccountAddName.setStatus("current")
_FeSW26AccountAddPassword_Type = DisplayString
_FeSW26AccountAddPassword_Object = MibScalar
feSW26AccountAddPassword = _FeSW26AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 4),
    _FeSW26AccountAddPassword_Type()
)
feSW26AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26AccountAddPassword.setStatus("current")


class _FeSW26DoAccountAdd_Type(Integer32):
    """Custom type feSW26DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26DoAccountAdd_Type.__name__ = "Integer32"
_FeSW26DoAccountAdd_Object = MibScalar
feSW26DoAccountAdd = _FeSW26DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 5),
    _FeSW26DoAccountAdd_Type()
)
feSW26DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DoAccountAdd.setStatus("current")


class _FeSW26AccountDel_Type(Integer32):
    """Custom type feSW26AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_FeSW26AccountDel_Type.__name__ = "Integer32"
_FeSW26AccountDel_Object = MibScalar
feSW26AccountDel = _FeSW26AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 1, 4, 6),
    _FeSW26AccountDel_Type()
)
feSW26AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26AccountDel.setStatus("current")
_FeSW26Snmp_ObjectIdentity = ObjectIdentity
feSW26Snmp = _FeSW26Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2)
)
_FeSW26GetCommunity_Type = DisplayString
_FeSW26GetCommunity_Object = MibScalar
feSW26GetCommunity = _FeSW26GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 1),
    _FeSW26GetCommunity_Type()
)
feSW26GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26GetCommunity.setStatus("current")
_FeSW26SetCommunity_Type = DisplayString
_FeSW26SetCommunity_Object = MibScalar
feSW26SetCommunity = _FeSW26SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 2),
    _FeSW26SetCommunity_Type()
)
feSW26SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SetCommunity.setStatus("current")


class _FeSW26TrapHostNumber_Type(Integer32):
    """Custom type feSW26TrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeSW26TrapHostNumber_Type.__name__ = "Integer32"
_FeSW26TrapHostNumber_Object = MibScalar
feSW26TrapHostNumber = _FeSW26TrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 3),
    _FeSW26TrapHostNumber_Type()
)
feSW26TrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26TrapHostNumber.setStatus("current")
_FeSW26TrapHostTable_Object = MibTable
feSW26TrapHostTable = _FeSW26TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 4)
)
if mibBuilder.loadTexts:
    feSW26TrapHostTable.setStatus("current")
_FeSW26TrapHostEntry_Object = MibTableRow
feSW26TrapHostEntry = _FeSW26TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 4, 1)
)
feSW26TrapHostEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26TrapHostIndex"),
)
if mibBuilder.loadTexts:
    feSW26TrapHostEntry.setStatus("current")


class _FeSW26TrapHostIndex_Type(Integer32):
    """Custom type feSW26TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeSW26TrapHostIndex_Type.__name__ = "Integer32"
_FeSW26TrapHostIndex_Object = MibTableColumn
feSW26TrapHostIndex = _FeSW26TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 4, 1, 1),
    _FeSW26TrapHostIndex_Type()
)
feSW26TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26TrapHostIndex.setStatus("current")
_FeSW26TrapHostIP_Type = IpAddress
_FeSW26TrapHostIP_Object = MibTableColumn
feSW26TrapHostIP = _FeSW26TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 4, 1, 2),
    _FeSW26TrapHostIP_Type()
)
feSW26TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26TrapHostIP.setStatus("current")


class _FeSW26TrapHostPort_Type(Integer32):
    """Custom type feSW26TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FeSW26TrapHostPort_Type.__name__ = "Integer32"
_FeSW26TrapHostPort_Object = MibTableColumn
feSW26TrapHostPort = _FeSW26TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 4, 1, 3),
    _FeSW26TrapHostPort_Type()
)
feSW26TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26TrapHostPort.setStatus("current")
_FeSW26TrapHostCommunity_Type = DisplayString
_FeSW26TrapHostCommunity_Object = MibTableColumn
feSW26TrapHostCommunity = _FeSW26TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 2, 4, 1, 4),
    _FeSW26TrapHostCommunity_Type()
)
feSW26TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26TrapHostCommunity.setStatus("current")
_FeSW26Alarm_ObjectIdentity = ObjectIdentity
feSW26Alarm = _FeSW26Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3)
)
_FeSW26Event_ObjectIdentity = ObjectIdentity
feSW26Event = _FeSW26Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1)
)


class _FeSW26EventNumber_Type(Integer32):
    """Custom type feSW26EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26EventNumber_Type.__name__ = "Integer32"
_FeSW26EventNumber_Object = MibScalar
feSW26EventNumber = _FeSW26EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 1),
    _FeSW26EventNumber_Type()
)
feSW26EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26EventNumber.setStatus("current")
_FeSW26EventTable_Object = MibTable
feSW26EventTable = _FeSW26EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    feSW26EventTable.setStatus("current")
_FeSW26EventEntry_Object = MibTableRow
feSW26EventEntry = _FeSW26EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2, 1)
)
feSW26EventEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26EventIndex"),
)
if mibBuilder.loadTexts:
    feSW26EventEntry.setStatus("current")


class _FeSW26EventIndex_Type(Integer32):
    """Custom type feSW26EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26EventIndex_Type.__name__ = "Integer32"
_FeSW26EventIndex_Object = MibTableColumn
feSW26EventIndex = _FeSW26EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2, 1, 1),
    _FeSW26EventIndex_Type()
)
feSW26EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26EventIndex.setStatus("current")
_FeSW26EventName_Type = DisplayString
_FeSW26EventName_Object = MibTableColumn
feSW26EventName = _FeSW26EventName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2, 1, 2),
    _FeSW26EventName_Type()
)
feSW26EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26EventName.setStatus("current")


class _FeSW26EventSendEmail_Type(Integer32):
    """Custom type feSW26EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26EventSendEmail_Type.__name__ = "Integer32"
_FeSW26EventSendEmail_Object = MibTableColumn
feSW26EventSendEmail = _FeSW26EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2, 1, 3),
    _FeSW26EventSendEmail_Type()
)
feSW26EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EventSendEmail.setStatus("current")


class _FeSW26EventSendSMS_Type(Integer32):
    """Custom type feSW26EventSendSMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26EventSendSMS_Type.__name__ = "Integer32"
_FeSW26EventSendSMS_Object = MibTableColumn
feSW26EventSendSMS = _FeSW26EventSendSMS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2, 1, 4),
    _FeSW26EventSendSMS_Type()
)
feSW26EventSendSMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EventSendSMS.setStatus("current")


class _FeSW26EventSendTrap_Type(Integer32):
    """Custom type feSW26EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26EventSendTrap_Type.__name__ = "Integer32"
_FeSW26EventSendTrap_Object = MibTableColumn
feSW26EventSendTrap = _FeSW26EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 1, 2, 1, 5),
    _FeSW26EventSendTrap_Type()
)
feSW26EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EventSendTrap.setStatus("current")
_FeSW26Email_ObjectIdentity = ObjectIdentity
feSW26Email = _FeSW26Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2)
)
_FeSW26EmailServer_Type = DisplayString
_FeSW26EmailServer_Object = MibScalar
feSW26EmailServer = _FeSW26EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 1),
    _FeSW26EmailServer_Type()
)
feSW26EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EmailServer.setStatus("current")
_FeSW26EmailUsername_Type = DisplayString
_FeSW26EmailUsername_Object = MibScalar
feSW26EmailUsername = _FeSW26EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 2),
    _FeSW26EmailUsername_Type()
)
feSW26EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EmailUsername.setStatus("current")
_FeSW26EmailPassword_Type = DisplayString
_FeSW26EmailPassword_Object = MibScalar
feSW26EmailPassword = _FeSW26EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 3),
    _FeSW26EmailPassword_Type()
)
feSW26EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EmailPassword.setStatus("current")


class _FeSW26EmailUserNumber_Type(Integer32):
    """Custom type feSW26EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeSW26EmailUserNumber_Type.__name__ = "Integer32"
_FeSW26EmailUserNumber_Object = MibScalar
feSW26EmailUserNumber = _FeSW26EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 4),
    _FeSW26EmailUserNumber_Type()
)
feSW26EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26EmailUserNumber.setStatus("current")
_FeSW26EmailUserTable_Object = MibTable
feSW26EmailUserTable = _FeSW26EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    feSW26EmailUserTable.setStatus("current")
_FeSW26EmailUserEntry_Object = MibTableRow
feSW26EmailUserEntry = _FeSW26EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 5, 1)
)
feSW26EmailUserEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26EmailUserIndex"),
)
if mibBuilder.loadTexts:
    feSW26EmailUserEntry.setStatus("current")


class _FeSW26EmailUserIndex_Type(Integer32):
    """Custom type feSW26EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeSW26EmailUserIndex_Type.__name__ = "Integer32"
_FeSW26EmailUserIndex_Object = MibTableColumn
feSW26EmailUserIndex = _FeSW26EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 5, 1, 1),
    _FeSW26EmailUserIndex_Type()
)
feSW26EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26EmailUserIndex.setStatus("current")
_FeSW26EmailUserAddress_Type = DisplayString
_FeSW26EmailUserAddress_Object = MibTableColumn
feSW26EmailUserAddress = _FeSW26EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 2, 5, 1, 2),
    _FeSW26EmailUserAddress_Type()
)
feSW26EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26EmailUserAddress.setStatus("current")
_FeSW26SMS_ObjectIdentity = ObjectIdentity
feSW26SMS = _FeSW26SMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3)
)
_FeSW26SMSServer_Type = DisplayString
_FeSW26SMSServer_Object = MibScalar
feSW26SMSServer = _FeSW26SMSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 1),
    _FeSW26SMSServer_Type()
)
feSW26SMSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SMSServer.setStatus("current")
_FeSW26SMSUsername_Type = DisplayString
_FeSW26SMSUsername_Object = MibScalar
feSW26SMSUsername = _FeSW26SMSUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 2),
    _FeSW26SMSUsername_Type()
)
feSW26SMSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SMSUsername.setStatus("current")
_FeSW26SMSPassword_Type = DisplayString
_FeSW26SMSPassword_Object = MibScalar
feSW26SMSPassword = _FeSW26SMSPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 3),
    _FeSW26SMSPassword_Type()
)
feSW26SMSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SMSPassword.setStatus("current")


class _FeSW26SMSUserNumber_Type(Integer32):
    """Custom type feSW26SMSUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeSW26SMSUserNumber_Type.__name__ = "Integer32"
_FeSW26SMSUserNumber_Object = MibScalar
feSW26SMSUserNumber = _FeSW26SMSUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 4),
    _FeSW26SMSUserNumber_Type()
)
feSW26SMSUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26SMSUserNumber.setStatus("current")
_FeSW26SMSUserTable_Object = MibTable
feSW26SMSUserTable = _FeSW26SMSUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    feSW26SMSUserTable.setStatus("current")
_FeSW26SMSUserEntry_Object = MibTableRow
feSW26SMSUserEntry = _FeSW26SMSUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 5, 1)
)
feSW26SMSUserEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26SMSUserIndex"),
)
if mibBuilder.loadTexts:
    feSW26SMSUserEntry.setStatus("current")


class _FeSW26SMSUserIndex_Type(Integer32):
    """Custom type feSW26SMSUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FeSW26SMSUserIndex_Type.__name__ = "Integer32"
_FeSW26SMSUserIndex_Object = MibTableColumn
feSW26SMSUserIndex = _FeSW26SMSUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 5, 1, 1),
    _FeSW26SMSUserIndex_Type()
)
feSW26SMSUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26SMSUserIndex.setStatus("current")
_FeSW26SMSUserMobilePhone_Type = DisplayString
_FeSW26SMSUserMobilePhone_Object = MibTableColumn
feSW26SMSUserMobilePhone = _FeSW26SMSUserMobilePhone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 3, 3, 5, 1, 2),
    _FeSW26SMSUserMobilePhone_Type()
)
feSW26SMSUserMobilePhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SMSUserMobilePhone.setStatus("current")
_FeSW26Tftp_ObjectIdentity = ObjectIdentity
feSW26Tftp = _FeSW26Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 4)
)
_FeSW26TftpServer_Type = IpAddress
_FeSW26TftpServer_Object = MibScalar
feSW26TftpServer = _FeSW26TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 4, 1),
    _FeSW26TftpServer_Type()
)
feSW26TftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26TftpServer.setStatus("current")
_FeSW26Configuration_ObjectIdentity = ObjectIdentity
feSW26Configuration = _FeSW26Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5)
)
_FeSW26SaveRestore_ObjectIdentity = ObjectIdentity
feSW26SaveRestore = _FeSW26SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 1)
)


class _FeSW26SaveStart_Type(Integer32):
    """Custom type feSW26SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26SaveStart_Type.__name__ = "Integer32"
_FeSW26SaveStart_Object = MibScalar
feSW26SaveStart = _FeSW26SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 1, 1),
    _FeSW26SaveStart_Type()
)
feSW26SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SaveStart.setStatus("current")


class _FeSW26SaveUser_Type(Integer32):
    """Custom type feSW26SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26SaveUser_Type.__name__ = "Integer32"
_FeSW26SaveUser_Object = MibScalar
feSW26SaveUser = _FeSW26SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 1, 2),
    _FeSW26SaveUser_Type()
)
feSW26SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26SaveUser.setStatus("current")


class _FeSW26RestoreDefault_Type(Integer32):
    """Custom type feSW26RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeSW26RestoreDefault_Type.__name__ = "Integer32"
_FeSW26RestoreDefault_Object = MibScalar
feSW26RestoreDefault = _FeSW26RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 1, 3),
    _FeSW26RestoreDefault_Type()
)
feSW26RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26RestoreDefault.setStatus("current")


class _FeSW26RestoreUser_Type(Integer32):
    """Custom type feSW26RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26RestoreUser_Type.__name__ = "Integer32"
_FeSW26RestoreUser_Object = MibScalar
feSW26RestoreUser = _FeSW26RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 1, 4),
    _FeSW26RestoreUser_Type()
)
feSW26RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26RestoreUser.setStatus("current")
_FeSW26ConfigFile_ObjectIdentity = ObjectIdentity
feSW26ConfigFile = _FeSW26ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 2)
)
_FeSW26ExportConfigName_Type = DisplayString
_FeSW26ExportConfigName_Object = MibScalar
feSW26ExportConfigName = _FeSW26ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 2, 1),
    _FeSW26ExportConfigName_Type()
)
feSW26ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26ExportConfigName.setStatus("current")


class _FeSW26DoExportConfig_Type(Integer32):
    """Custom type feSW26DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeSW26DoExportConfig_Type.__name__ = "Integer32"
_FeSW26DoExportConfig_Object = MibScalar
feSW26DoExportConfig = _FeSW26DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 2, 2),
    _FeSW26DoExportConfig_Type()
)
feSW26DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DoExportConfig.setStatus("current")
_FeSW26ImportConfigName_Type = DisplayString
_FeSW26ImportConfigName_Object = MibScalar
feSW26ImportConfigName = _FeSW26ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 2, 3),
    _FeSW26ImportConfigName_Type()
)
feSW26ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26ImportConfigName.setStatus("current")


class _FeSW26DoImportConfig_Type(Integer32):
    """Custom type feSW26DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_FeSW26DoImportConfig_Type.__name__ = "Integer32"
_FeSW26DoImportConfig_Object = MibScalar
feSW26DoImportConfig = _FeSW26DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 5, 2, 4),
    _FeSW26DoImportConfig_Type()
)
feSW26DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DoImportConfig.setStatus("current")
_FeSW26Diagnostic_ObjectIdentity = ObjectIdentity
feSW26Diagnostic = _FeSW26Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6)
)
_FeSW26EEPROMTest_Type = DisplayString
_FeSW26EEPROMTest_Object = MibScalar
feSW26EEPROMTest = _FeSW26EEPROMTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 1),
    _FeSW26EEPROMTest_Type()
)
feSW26EEPROMTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26EEPROMTest.setStatus("current")
_FeSW26UartTest_Type = DisplayString
_FeSW26UartTest_Object = MibScalar
feSW26UartTest = _FeSW26UartTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 2),
    _FeSW26UartTest_Type()
)
feSW26UartTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26UartTest.setStatus("current")
_FeSW26DramTest_Type = DisplayString
_FeSW26DramTest_Object = MibScalar
feSW26DramTest = _FeSW26DramTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 3),
    _FeSW26DramTest_Type()
)
feSW26DramTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26DramTest.setStatus("current")
_FeSW26FlashTest_Type = DisplayString
_FeSW26FlashTest_Object = MibScalar
feSW26FlashTest = _FeSW26FlashTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 4),
    _FeSW26FlashTest_Type()
)
feSW26FlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26FlashTest.setStatus("current")
_FeSW26InternalLoopbackTest_Type = DisplayString
_FeSW26InternalLoopbackTest_Object = MibScalar
feSW26InternalLoopbackTest = _FeSW26InternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 5),
    _FeSW26InternalLoopbackTest_Type()
)
feSW26InternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26InternalLoopbackTest.setStatus("current")
_FeSW26ExternalLoopbackTest_Type = DisplayString
_FeSW26ExternalLoopbackTest_Object = MibScalar
feSW26ExternalLoopbackTest = _FeSW26ExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 6),
    _FeSW26ExternalLoopbackTest_Type()
)
feSW26ExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26ExternalLoopbackTest.setStatus("current")
_FeSW26PingTest_Type = DisplayString
_FeSW26PingTest_Object = MibScalar
feSW26PingTest = _FeSW26PingTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 6, 7),
    _FeSW26PingTest_Type()
)
feSW26PingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26PingTest.setStatus("current")
_FeSW26Log_ObjectIdentity = ObjectIdentity
feSW26Log = _FeSW26Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7)
)


class _FeSW26ClearLog_Type(Integer32):
    """Custom type feSW26ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26ClearLog_Type.__name__ = "Integer32"
_FeSW26ClearLog_Object = MibScalar
feSW26ClearLog = _FeSW26ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 1),
    _FeSW26ClearLog_Type()
)
feSW26ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26ClearLog.setStatus("current")


class _FeSW26UploadLog_Type(Integer32):
    """Custom type feSW26UploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26UploadLog_Type.__name__ = "Integer32"
_FeSW26UploadLog_Object = MibScalar
feSW26UploadLog = _FeSW26UploadLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 2),
    _FeSW26UploadLog_Type()
)
feSW26UploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26UploadLog.setStatus("current")


class _FeSW26AutoUploadLogState_Type(Integer32):
    """Custom type feSW26AutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26AutoUploadLogState_Type.__name__ = "Integer32"
_FeSW26AutoUploadLogState_Object = MibScalar
feSW26AutoUploadLogState = _FeSW26AutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 3),
    _FeSW26AutoUploadLogState_Type()
)
feSW26AutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26AutoUploadLogState.setStatus("current")


class _FeSW26LogNumber_Type(Integer32):
    """Custom type feSW26LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_FeSW26LogNumber_Type.__name__ = "Integer32"
_FeSW26LogNumber_Object = MibScalar
feSW26LogNumber = _FeSW26LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 4),
    _FeSW26LogNumber_Type()
)
feSW26LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26LogNumber.setStatus("current")
_FeSW26LogTable_Object = MibTable
feSW26LogTable = _FeSW26LogTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 5)
)
if mibBuilder.loadTexts:
    feSW26LogTable.setStatus("current")
_FeSW26LogEntry_Object = MibTableRow
feSW26LogEntry = _FeSW26LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 5, 1)
)
feSW26LogEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26LogIndex"),
)
if mibBuilder.loadTexts:
    feSW26LogEntry.setStatus("current")


class _FeSW26LogIndex_Type(Integer32):
    """Custom type feSW26LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_FeSW26LogIndex_Type.__name__ = "Integer32"
_FeSW26LogIndex_Object = MibTableColumn
feSW26LogIndex = _FeSW26LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 5, 1, 1),
    _FeSW26LogIndex_Type()
)
feSW26LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26LogIndex.setStatus("current")
_FeSW26LogEvent_Type = DisplayString
_FeSW26LogEvent_Object = MibTableColumn
feSW26LogEvent = _FeSW26LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 7, 5, 1, 2),
    _FeSW26LogEvent_Type()
)
feSW26LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26LogEvent.setStatus("current")
_FeSW26Firmware_ObjectIdentity = ObjectIdentity
feSW26Firmware = _FeSW26Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 8)
)
_FeSW26FirmwareFileName_Type = DisplayString
_FeSW26FirmwareFileName_Object = MibScalar
feSW26FirmwareFileName = _FeSW26FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 8, 1),
    _FeSW26FirmwareFileName_Type()
)
feSW26FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26FirmwareFileName.setStatus("current")


class _FeSW26DoFirmwareUpgrade_Type(Integer32):
    """Custom type feSW26DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26DoFirmwareUpgrade_Type.__name__ = "Integer32"
_FeSW26DoFirmwareUpgrade_Object = MibScalar
feSW26DoFirmwareUpgrade = _FeSW26DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 8, 2),
    _FeSW26DoFirmwareUpgrade_Type()
)
feSW26DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26DoFirmwareUpgrade.setStatus("current")
_FeSW26Port_ObjectIdentity = ObjectIdentity
feSW26Port = _FeSW26Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9)
)
_FeSW26PortStatus_ObjectIdentity = ObjectIdentity
feSW26PortStatus = _FeSW26PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1)
)


class _FeSW26PortStatusNumber_Type(Integer32):
    """Custom type feSW26PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26PortStatusNumber_Type.__name__ = "Integer32"
_FeSW26PortStatusNumber_Object = MibScalar
feSW26PortStatusNumber = _FeSW26PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 1),
    _FeSW26PortStatusNumber_Type()
)
feSW26PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusNumber.setStatus("current")
_FeSW26PortStatusTable_Object = MibTable
feSW26PortStatusTable = _FeSW26PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    feSW26PortStatusTable.setStatus("current")
_FeSW26PortStatusEntry_Object = MibTableRow
feSW26PortStatusEntry = _FeSW26PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1)
)
feSW26PortStatusEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26PortStatusIndex"),
)
if mibBuilder.loadTexts:
    feSW26PortStatusEntry.setStatus("current")


class _FeSW26PortStatusIndex_Type(Integer32):
    """Custom type feSW26PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26PortStatusIndex_Type.__name__ = "Integer32"
_FeSW26PortStatusIndex_Object = MibTableColumn
feSW26PortStatusIndex = _FeSW26PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 1),
    _FeSW26PortStatusIndex_Type()
)
feSW26PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusIndex.setStatus("current")
_FeSW26PortStatusMedia_Type = DisplayString
_FeSW26PortStatusMedia_Object = MibTableColumn
feSW26PortStatusMedia = _FeSW26PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 2),
    _FeSW26PortStatusMedia_Type()
)
feSW26PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusMedia.setStatus("current")
_FeSW26PortStatusLink_Type = DisplayString
_FeSW26PortStatusLink_Object = MibTableColumn
feSW26PortStatusLink = _FeSW26PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 3),
    _FeSW26PortStatusLink_Type()
)
feSW26PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusLink.setStatus("current")
_FeSW26PortStatusPortState_Type = DisplayString
_FeSW26PortStatusPortState_Object = MibTableColumn
feSW26PortStatusPortState = _FeSW26PortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 4),
    _FeSW26PortStatusPortState_Type()
)
feSW26PortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusPortState.setStatus("current")
_FeSW26PortStatusAutoNego_Type = DisplayString
_FeSW26PortStatusAutoNego_Object = MibTableColumn
feSW26PortStatusAutoNego = _FeSW26PortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 5),
    _FeSW26PortStatusAutoNego_Type()
)
feSW26PortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusAutoNego.setStatus("current")
_FeSW26PortStatusSpdDpx_Type = DisplayString
_FeSW26PortStatusSpdDpx_Object = MibTableColumn
feSW26PortStatusSpdDpx = _FeSW26PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 6),
    _FeSW26PortStatusSpdDpx_Type()
)
feSW26PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusSpdDpx.setStatus("current")
_FeSW26PortStatusRxPause_Type = DisplayString
_FeSW26PortStatusRxPause_Object = MibTableColumn
feSW26PortStatusRxPause = _FeSW26PortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 7),
    _FeSW26PortStatusRxPause_Type()
)
feSW26PortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusRxPause.setStatus("current")
_FeSW26PortStatusTxPause_Type = DisplayString
_FeSW26PortStatusTxPause_Object = MibTableColumn
feSW26PortStatusTxPause = _FeSW26PortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 8),
    _FeSW26PortStatusTxPause_Type()
)
feSW26PortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatusTxPause.setStatus("current")
_FeSW26PortStatuDescription_Type = DisplayString
_FeSW26PortStatuDescription_Object = MibTableColumn
feSW26PortStatuDescription = _FeSW26PortStatuDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 1, 2, 1, 9),
    _FeSW26PortStatuDescription_Type()
)
feSW26PortStatuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortStatuDescription.setStatus("current")
_FeSW26PortConf_ObjectIdentity = ObjectIdentity
feSW26PortConf = _FeSW26PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2)
)


class _FeSW26PortConfNumber_Type(Integer32):
    """Custom type feSW26PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26PortConfNumber_Type.__name__ = "Integer32"
_FeSW26PortConfNumber_Object = MibScalar
feSW26PortConfNumber = _FeSW26PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 1),
    _FeSW26PortConfNumber_Type()
)
feSW26PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortConfNumber.setStatus("current")
_FeSW26PortConfTable_Object = MibTable
feSW26PortConfTable = _FeSW26PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    feSW26PortConfTable.setStatus("current")
_FeSW26PortConfEntry_Object = MibTableRow
feSW26PortConfEntry = _FeSW26PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2, 1)
)
feSW26PortConfEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26PortConfIndex"),
)
if mibBuilder.loadTexts:
    feSW26PortConfEntry.setStatus("current")


class _FeSW26PortConfIndex_Type(Integer32):
    """Custom type feSW26PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26PortConfIndex_Type.__name__ = "Integer32"
_FeSW26PortConfIndex_Object = MibTableColumn
feSW26PortConfIndex = _FeSW26PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2, 1, 1),
    _FeSW26PortConfIndex_Type()
)
feSW26PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26PortConfIndex.setStatus("current")


class _FeSW26PortConfPortState_Type(Integer32):
    """Custom type feSW26PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26PortConfPortState_Type.__name__ = "Integer32"
_FeSW26PortConfPortState_Object = MibTableColumn
feSW26PortConfPortState = _FeSW26PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2, 1, 2),
    _FeSW26PortConfPortState_Type()
)
feSW26PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26PortConfPortState.setStatus("current")


class _FeSW26PortConfSpdDpx_Type(Integer32):
    """Custom type feSW26PortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FeSW26PortConfSpdDpx_Type.__name__ = "Integer32"
_FeSW26PortConfSpdDpx_Object = MibTableColumn
feSW26PortConfSpdDpx = _FeSW26PortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2, 1, 3),
    _FeSW26PortConfSpdDpx_Type()
)
feSW26PortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26PortConfSpdDpx.setStatus("current")


class _FeSW26PortConfFlwCtrl_Type(Integer32):
    """Custom type feSW26PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26PortConfFlwCtrl_Type.__name__ = "Integer32"
_FeSW26PortConfFlwCtrl_Object = MibTableColumn
feSW26PortConfFlwCtrl = _FeSW26PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2, 1, 4),
    _FeSW26PortConfFlwCtrl_Type()
)
feSW26PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26PortConfFlwCtrl.setStatus("current")
_FeSW26PortConfDescription_Type = DisplayString
_FeSW26PortConfDescription_Object = MibTableColumn
feSW26PortConfDescription = _FeSW26PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 9, 2, 2, 1, 5),
    _FeSW26PortConfDescription_Type()
)
feSW26PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26PortConfDescription.setStatus("current")
_FeSW26LoopDetectedConf_ObjectIdentity = ObjectIdentity
feSW26LoopDetectedConf = _FeSW26LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10)
)


class _FeSW26LoopDetectedNumber_Type(Integer32):
    """Custom type feSW26LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26LoopDetectedNumber_Type.__name__ = "Integer32"
_FeSW26LoopDetectedNumber_Object = MibScalar
feSW26LoopDetectedNumber = _FeSW26LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 1),
    _FeSW26LoopDetectedNumber_Type()
)
feSW26LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26LoopDetectedNumber.setStatus("current")
_FeSW26LoopDetectedTable_Object = MibTable
feSW26LoopDetectedTable = _FeSW26LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 2)
)
if mibBuilder.loadTexts:
    feSW26LoopDetectedTable.setStatus("current")
_FeSW26LoopDetectedEntry_Object = MibTableRow
feSW26LoopDetectedEntry = _FeSW26LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 2, 1)
)
feSW26LoopDetectedEntry.setIndexNames(
    (0, "PRIVATE-FESW-26-MIB", "feSW26LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    feSW26LoopDetectedEntry.setStatus("current")


class _FeSW26LoopDetectedfIndex_Type(Integer32):
    """Custom type feSW26LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FeSW26LoopDetectedfIndex_Type.__name__ = "Integer32"
_FeSW26LoopDetectedfIndex_Object = MibTableColumn
feSW26LoopDetectedfIndex = _FeSW26LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 2, 1, 1),
    _FeSW26LoopDetectedfIndex_Type()
)
feSW26LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26LoopDetectedfIndex.setStatus("current")


class _FeSW26LoopDetectedStateEbl_Type(Integer32):
    """Custom type feSW26LoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26LoopDetectedStateEbl_Type.__name__ = "Integer32"
_FeSW26LoopDetectedStateEbl_Object = MibTableColumn
feSW26LoopDetectedStateEbl = _FeSW26LoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 2, 1, 2),
    _FeSW26LoopDetectedStateEbl_Type()
)
feSW26LoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26LoopDetectedStateEbl.setStatus("current")


class _FeSW26LoopDetectedCurrentStatus_Type(Integer32):
    """Custom type feSW26LoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26LoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_FeSW26LoopDetectedCurrentStatus_Object = MibTableColumn
feSW26LoopDetectedCurrentStatus = _FeSW26LoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 2, 1, 3),
    _FeSW26LoopDetectedCurrentStatus_Type()
)
feSW26LoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSW26LoopDetectedCurrentStatus.setStatus("current")


class _FeSW26LoopDetectedResumed_Type(Integer32):
    """Custom type feSW26LoopDetectedResumed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26LoopDetectedResumed_Type.__name__ = "Integer32"
_FeSW26LoopDetectedResumed_Object = MibTableColumn
feSW26LoopDetectedResumed = _FeSW26LoopDetectedResumed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 2, 1, 4),
    _FeSW26LoopDetectedResumed_Type()
)
feSW26LoopDetectedResumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26LoopDetectedResumed.setStatus("current")


class _FeSW26LoopDetectedAction_Type(Integer32):
    """Custom type feSW26LoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_FeSW26LoopDetectedAction_Type.__name__ = "Integer32"
_FeSW26LoopDetectedAction_Object = MibScalar
feSW26LoopDetectedAction = _FeSW26LoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 10, 3),
    _FeSW26LoopDetectedAction_Type()
)
feSW26LoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feSW26LoopDetectedAction.setStatus("current")
_FeSW26TrapEntry_ObjectIdentity = ObjectIdentity
feSW26TrapEntry = _FeSW26TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20)
)
_FeSW26TrapVariable_ObjectIdentity = ObjectIdentity
feSW26TrapVariable = _FeSW26TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 21, 1),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _GroupId_Type(Integer32):
    """Custom type groupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GroupId_Type.__name__ = "Integer32"
_GroupId_Object = MibScalar
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")

# Managed Objects groups


# Notification objects

feSW26ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 1)
)
feSW26ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feSW26ModuleInserted.setStatus(
        "current"
    )

feSW26ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 2)
)
feSW26ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feSW26ModuleRemoved.setStatus(
        "current"
    )

feSW26DualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 3)
)
feSW26DualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feSW26DualMediaSwapped.setStatus(
        "current"
    )

feSW26LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 5)
)
feSW26LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feSW26LoopDetected.setStatus(
        "current"
    )

feSW26StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 100)
)
if mibBuilder.loadTexts:
    feSW26StpStateDisabled.setStatus(
        "current"
    )

feSW26StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 101)
)
if mibBuilder.loadTexts:
    feSW26StpStateEnabled.setStatus(
        "current"
    )

feSW26StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 102)
)
feSW26StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    feSW26StpTopologyChanged.setStatus(
        "current"
    )

feSW26RmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 110)
)
if mibBuilder.loadTexts:
    feSW26RmonRisingAlarm.setStatus(
        "current"
    )

feSW26RmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 111)
)
if mibBuilder.loadTexts:
    feSW26RmonFallingAlarm.setStatus(
        "current"
    )

feSW26LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 120)
)
feSW26LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FESW-26-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    feSW26LacpStateDisabled.setStatus(
        "current"
    )

feSW26LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 121)
)
feSW26LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FESW-26-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    feSW26LacpStateEnabled.setStatus(
        "current"
    )

feSW26LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 123)
)
feSW26LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FESW-26-MIB", "actorkey"),
        ("PRIVATE-FESW-26-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    feSW26LacpPortAdded.setStatus(
        "current"
    )

feSW26LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 124)
)
feSW26LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRIVATE-FESW-26-MIB", "actorkey"),
        ("PRIVATE-FESW-26-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    feSW26LacpPortTrunkFailure.setStatus(
        "current"
    )

feSW26GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 140)
)
if mibBuilder.loadTexts:
    feSW26GvrpStateDisabled.setStatus(
        "current"
    )

feSW26GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 141)
)
if mibBuilder.loadTexts:
    feSW26GvrpStateEnabled.setStatus(
        "current"
    )

feSW26VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 151)
)
if mibBuilder.loadTexts:
    feSW26VlanPortBaseEnabled.setStatus(
        "current"
    )

feSW26VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 152)
)
if mibBuilder.loadTexts:
    feSW26VlanTagBaseEnabled.setStatus(
        "current"
    )

feSW26VlanMetroBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 153)
)
if mibBuilder.loadTexts:
    feSW26VlanMetroBaseEnabled.setStatus(
        "current"
    )

feSW26UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 200)
)
feSW26UserLogin.setObjects(
    ("PRIVATE-FESW-26-MIB", "username")
)
if mibBuilder.loadTexts:
    feSW26UserLogin.setStatus(
        "current"
    )

feSW26UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 16, 1, 20, 201)
)
feSW26UserLogout.setObjects(
    ("PRIVATE-FESW-26-MIB", "username")
)
if mibBuilder.loadTexts:
    feSW26UserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATE-FESW-26-MIB",
    **{"privatetech": privatetech,
       "switch": switch,
       "feSW26ProductID": feSW26ProductID,
       "feSW26Produces": feSW26Produces,
       "feSW26System": feSW26System,
       "feSW26CommonSys": feSW26CommonSys,
       "feSW26Reboot": feSW26Reboot,
       "feSW26BiosVsersion": feSW26BiosVsersion,
       "feSW26FirmwareVersion": feSW26FirmwareVersion,
       "feSW26HardwareVersion": feSW26HardwareVersion,
       "feSW26MechanicalVersion": feSW26MechanicalVersion,
       "feSW26SerialNumber": feSW26SerialNumber,
       "feSW26HostMacAddress": feSW26HostMacAddress,
       "feSW26DevicePort": feSW26DevicePort,
       "feSW26RamSize": feSW26RamSize,
       "feSW26FlashSize": feSW26FlashSize,
       "feSW26IP": feSW26IP,
       "feSW26DhcpSetting": feSW26DhcpSetting,
       "feSW26IPAddress": feSW26IPAddress,
       "feSW26NetMask": feSW26NetMask,
       "feSW26DefaultGateway": feSW26DefaultGateway,
       "feSW26DnsSetting": feSW26DnsSetting,
       "feSW26DnsServer": feSW26DnsServer,
       "feSW26Time": feSW26Time,
       "feSW26SystemCurrentTime": feSW26SystemCurrentTime,
       "feSW26ManualTimeSetting": feSW26ManualTimeSetting,
       "feSW26NTPServer": feSW26NTPServer,
       "feSW26NTPTimeZone": feSW26NTPTimeZone,
       "feSW26NTPTimeSync": feSW26NTPTimeSync,
       "feSW26DaylightSavingTime": feSW26DaylightSavingTime,
       "feSW26DaylightStartTime": feSW26DaylightStartTime,
       "feSW26DaylightEndTime": feSW26DaylightEndTime,
       "feSW26Account": feSW26Account,
       "feSW26AccountNumber": feSW26AccountNumber,
       "feSW26AccountTable": feSW26AccountTable,
       "feSW26AccountEntry": feSW26AccountEntry,
       "feSW26AccountIndex": feSW26AccountIndex,
       "feSW26AccountAuthorization": feSW26AccountAuthorization,
       "feSW26AccountName": feSW26AccountName,
       "feSW26AccountPassword": feSW26AccountPassword,
       "feSW26AccountAddName": feSW26AccountAddName,
       "feSW26AccountAddPassword": feSW26AccountAddPassword,
       "feSW26DoAccountAdd": feSW26DoAccountAdd,
       "feSW26AccountDel": feSW26AccountDel,
       "feSW26Snmp": feSW26Snmp,
       "feSW26GetCommunity": feSW26GetCommunity,
       "feSW26SetCommunity": feSW26SetCommunity,
       "feSW26TrapHostNumber": feSW26TrapHostNumber,
       "feSW26TrapHostTable": feSW26TrapHostTable,
       "feSW26TrapHostEntry": feSW26TrapHostEntry,
       "feSW26TrapHostIndex": feSW26TrapHostIndex,
       "feSW26TrapHostIP": feSW26TrapHostIP,
       "feSW26TrapHostPort": feSW26TrapHostPort,
       "feSW26TrapHostCommunity": feSW26TrapHostCommunity,
       "feSW26Alarm": feSW26Alarm,
       "feSW26Event": feSW26Event,
       "feSW26EventNumber": feSW26EventNumber,
       "feSW26EventTable": feSW26EventTable,
       "feSW26EventEntry": feSW26EventEntry,
       "feSW26EventIndex": feSW26EventIndex,
       "feSW26EventName": feSW26EventName,
       "feSW26EventSendEmail": feSW26EventSendEmail,
       "feSW26EventSendSMS": feSW26EventSendSMS,
       "feSW26EventSendTrap": feSW26EventSendTrap,
       "feSW26Email": feSW26Email,
       "feSW26EmailServer": feSW26EmailServer,
       "feSW26EmailUsername": feSW26EmailUsername,
       "feSW26EmailPassword": feSW26EmailPassword,
       "feSW26EmailUserNumber": feSW26EmailUserNumber,
       "feSW26EmailUserTable": feSW26EmailUserTable,
       "feSW26EmailUserEntry": feSW26EmailUserEntry,
       "feSW26EmailUserIndex": feSW26EmailUserIndex,
       "feSW26EmailUserAddress": feSW26EmailUserAddress,
       "feSW26SMS": feSW26SMS,
       "feSW26SMSServer": feSW26SMSServer,
       "feSW26SMSUsername": feSW26SMSUsername,
       "feSW26SMSPassword": feSW26SMSPassword,
       "feSW26SMSUserNumber": feSW26SMSUserNumber,
       "feSW26SMSUserTable": feSW26SMSUserTable,
       "feSW26SMSUserEntry": feSW26SMSUserEntry,
       "feSW26SMSUserIndex": feSW26SMSUserIndex,
       "feSW26SMSUserMobilePhone": feSW26SMSUserMobilePhone,
       "feSW26Tftp": feSW26Tftp,
       "feSW26TftpServer": feSW26TftpServer,
       "feSW26Configuration": feSW26Configuration,
       "feSW26SaveRestore": feSW26SaveRestore,
       "feSW26SaveStart": feSW26SaveStart,
       "feSW26SaveUser": feSW26SaveUser,
       "feSW26RestoreDefault": feSW26RestoreDefault,
       "feSW26RestoreUser": feSW26RestoreUser,
       "feSW26ConfigFile": feSW26ConfigFile,
       "feSW26ExportConfigName": feSW26ExportConfigName,
       "feSW26DoExportConfig": feSW26DoExportConfig,
       "feSW26ImportConfigName": feSW26ImportConfigName,
       "feSW26DoImportConfig": feSW26DoImportConfig,
       "feSW26Diagnostic": feSW26Diagnostic,
       "feSW26EEPROMTest": feSW26EEPROMTest,
       "feSW26UartTest": feSW26UartTest,
       "feSW26DramTest": feSW26DramTest,
       "feSW26FlashTest": feSW26FlashTest,
       "feSW26InternalLoopbackTest": feSW26InternalLoopbackTest,
       "feSW26ExternalLoopbackTest": feSW26ExternalLoopbackTest,
       "feSW26PingTest": feSW26PingTest,
       "feSW26Log": feSW26Log,
       "feSW26ClearLog": feSW26ClearLog,
       "feSW26UploadLog": feSW26UploadLog,
       "feSW26AutoUploadLogState": feSW26AutoUploadLogState,
       "feSW26LogNumber": feSW26LogNumber,
       "feSW26LogTable": feSW26LogTable,
       "feSW26LogEntry": feSW26LogEntry,
       "feSW26LogIndex": feSW26LogIndex,
       "feSW26LogEvent": feSW26LogEvent,
       "feSW26Firmware": feSW26Firmware,
       "feSW26FirmwareFileName": feSW26FirmwareFileName,
       "feSW26DoFirmwareUpgrade": feSW26DoFirmwareUpgrade,
       "feSW26Port": feSW26Port,
       "feSW26PortStatus": feSW26PortStatus,
       "feSW26PortStatusNumber": feSW26PortStatusNumber,
       "feSW26PortStatusTable": feSW26PortStatusTable,
       "feSW26PortStatusEntry": feSW26PortStatusEntry,
       "feSW26PortStatusIndex": feSW26PortStatusIndex,
       "feSW26PortStatusMedia": feSW26PortStatusMedia,
       "feSW26PortStatusLink": feSW26PortStatusLink,
       "feSW26PortStatusPortState": feSW26PortStatusPortState,
       "feSW26PortStatusAutoNego": feSW26PortStatusAutoNego,
       "feSW26PortStatusSpdDpx": feSW26PortStatusSpdDpx,
       "feSW26PortStatusRxPause": feSW26PortStatusRxPause,
       "feSW26PortStatusTxPause": feSW26PortStatusTxPause,
       "feSW26PortStatuDescription": feSW26PortStatuDescription,
       "feSW26PortConf": feSW26PortConf,
       "feSW26PortConfNumber": feSW26PortConfNumber,
       "feSW26PortConfTable": feSW26PortConfTable,
       "feSW26PortConfEntry": feSW26PortConfEntry,
       "feSW26PortConfIndex": feSW26PortConfIndex,
       "feSW26PortConfPortState": feSW26PortConfPortState,
       "feSW26PortConfSpdDpx": feSW26PortConfSpdDpx,
       "feSW26PortConfFlwCtrl": feSW26PortConfFlwCtrl,
       "feSW26PortConfDescription": feSW26PortConfDescription,
       "feSW26LoopDetectedConf": feSW26LoopDetectedConf,
       "feSW26LoopDetectedNumber": feSW26LoopDetectedNumber,
       "feSW26LoopDetectedTable": feSW26LoopDetectedTable,
       "feSW26LoopDetectedEntry": feSW26LoopDetectedEntry,
       "feSW26LoopDetectedfIndex": feSW26LoopDetectedfIndex,
       "feSW26LoopDetectedStateEbl": feSW26LoopDetectedStateEbl,
       "feSW26LoopDetectedCurrentStatus": feSW26LoopDetectedCurrentStatus,
       "feSW26LoopDetectedResumed": feSW26LoopDetectedResumed,
       "feSW26LoopDetectedAction": feSW26LoopDetectedAction,
       "feSW26TrapEntry": feSW26TrapEntry,
       "feSW26ModuleInserted": feSW26ModuleInserted,
       "feSW26ModuleRemoved": feSW26ModuleRemoved,
       "feSW26DualMediaSwapped": feSW26DualMediaSwapped,
       "feSW26LoopDetected": feSW26LoopDetected,
       "feSW26StpStateDisabled": feSW26StpStateDisabled,
       "feSW26StpStateEnabled": feSW26StpStateEnabled,
       "feSW26StpTopologyChanged": feSW26StpTopologyChanged,
       "feSW26RmonRisingAlarm": feSW26RmonRisingAlarm,
       "feSW26RmonFallingAlarm": feSW26RmonFallingAlarm,
       "feSW26LacpStateDisabled": feSW26LacpStateDisabled,
       "feSW26LacpStateEnabled": feSW26LacpStateEnabled,
       "feSW26LacpPortAdded": feSW26LacpPortAdded,
       "feSW26LacpPortTrunkFailure": feSW26LacpPortTrunkFailure,
       "feSW26GvrpStateDisabled": feSW26GvrpStateDisabled,
       "feSW26GvrpStateEnabled": feSW26GvrpStateEnabled,
       "feSW26VlanPortBaseEnabled": feSW26VlanPortBaseEnabled,
       "feSW26VlanTagBaseEnabled": feSW26VlanTagBaseEnabled,
       "feSW26VlanMetroBaseEnabled": feSW26VlanMetroBaseEnabled,
       "feSW26UserLogin": feSW26UserLogin,
       "feSW26UserLogout": feSW26UserLogout,
       "feSW26TrapVariable": feSW26TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink}
)
