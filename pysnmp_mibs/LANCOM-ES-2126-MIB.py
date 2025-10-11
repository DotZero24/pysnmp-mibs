# SNMP MIB module (LANCOM-ES-2126-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-ES-2126-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:10 2025
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
_FastEthernetSwitches_ObjectIdentity = ObjectIdentity
fastEthernetSwitches = _FastEthernetSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2)
)
_LancomES2126_ObjectIdentity = ObjectIdentity
lancomES2126 = _LancomES2126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126)
)
_Es2126Produces_ObjectIdentity = ObjectIdentity
es2126Produces = _Es2126Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1)
)
_Es2126System_ObjectIdentity = ObjectIdentity
es2126System = _Es2126System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1)
)
_Es2126CommonSys_ObjectIdentity = ObjectIdentity
es2126CommonSys = _Es2126CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1)
)


class _Es2126Reboot_Type(Integer32):
    """Custom type es2126Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126Reboot_Type.__name__ = "Integer32"
_Es2126Reboot_Object = MibScalar
es2126Reboot = _Es2126Reboot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 1),
    _Es2126Reboot_Type()
)
es2126Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Reboot.setStatus("current")
_Es2126BiosVsersion_Type = DisplayString
_Es2126BiosVsersion_Object = MibScalar
es2126BiosVsersion = _Es2126BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 2),
    _Es2126BiosVsersion_Type()
)
es2126BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126BiosVsersion.setStatus("current")
_Es2126FirmwareVersion_Type = DisplayString
_Es2126FirmwareVersion_Object = MibScalar
es2126FirmwareVersion = _Es2126FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 3),
    _Es2126FirmwareVersion_Type()
)
es2126FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126FirmwareVersion.setStatus("current")
_Es2126HardwareVersion_Type = DisplayString
_Es2126HardwareVersion_Object = MibScalar
es2126HardwareVersion = _Es2126HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 4),
    _Es2126HardwareVersion_Type()
)
es2126HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126HardwareVersion.setStatus("current")
_Es2126MechanicalVersion_Type = DisplayString
_Es2126MechanicalVersion_Object = MibScalar
es2126MechanicalVersion = _Es2126MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 5),
    _Es2126MechanicalVersion_Type()
)
es2126MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126MechanicalVersion.setStatus("current")
_Es2126SerialNumber_Type = DisplayString
_Es2126SerialNumber_Object = MibScalar
es2126SerialNumber = _Es2126SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 6),
    _Es2126SerialNumber_Type()
)
es2126SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126SerialNumber.setStatus("current")
_Es2126HostMacAddress_Type = DisplayString
_Es2126HostMacAddress_Object = MibScalar
es2126HostMacAddress = _Es2126HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 7),
    _Es2126HostMacAddress_Type()
)
es2126HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126HostMacAddress.setStatus("current")
_Es2126DevicePort_Type = DisplayString
_Es2126DevicePort_Object = MibScalar
es2126DevicePort = _Es2126DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 8),
    _Es2126DevicePort_Type()
)
es2126DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126DevicePort.setStatus("current")
_Es2126RamSize_Type = DisplayString
_Es2126RamSize_Object = MibScalar
es2126RamSize = _Es2126RamSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 9),
    _Es2126RamSize_Type()
)
es2126RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126RamSize.setStatus("current")
_Es2126FlashSize_Type = DisplayString
_Es2126FlashSize_Object = MibScalar
es2126FlashSize = _Es2126FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 10),
    _Es2126FlashSize_Type()
)
es2126FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126FlashSize.setStatus("current")
_Es2126SystemDescription_Type = DisplayString
_Es2126SystemDescription_Object = MibScalar
es2126SystemDescription = _Es2126SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 11),
    _Es2126SystemDescription_Type()
)
es2126SystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126SystemDescription.setStatus("current")
_Es2126DeviceName_Type = DisplayString
_Es2126DeviceName_Object = MibScalar
es2126DeviceName = _Es2126DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 1, 12),
    _Es2126DeviceName_Type()
)
es2126DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DeviceName.setStatus("current")
_Es2126IP_ObjectIdentity = ObjectIdentity
es2126IP = _Es2126IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2)
)


class _Es2126DhcpSetting_Type(Integer32):
    """Custom type es2126DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126DhcpSetting_Type.__name__ = "Integer32"
_Es2126DhcpSetting_Object = MibScalar
es2126DhcpSetting = _Es2126DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2, 1),
    _Es2126DhcpSetting_Type()
)
es2126DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DhcpSetting.setStatus("current")
_Es2126IPAddress_Type = IpAddress
_Es2126IPAddress_Object = MibScalar
es2126IPAddress = _Es2126IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2, 2),
    _Es2126IPAddress_Type()
)
es2126IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126IPAddress.setStatus("current")
_Es2126NetMask_Type = IpAddress
_Es2126NetMask_Object = MibScalar
es2126NetMask = _Es2126NetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2, 3),
    _Es2126NetMask_Type()
)
es2126NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126NetMask.setStatus("current")
_Es2126DefaultGateway_Type = IpAddress
_Es2126DefaultGateway_Object = MibScalar
es2126DefaultGateway = _Es2126DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2, 4),
    _Es2126DefaultGateway_Type()
)
es2126DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DefaultGateway.setStatus("current")


class _Es2126DnsSetting_Type(Integer32):
    """Custom type es2126DnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126DnsSetting_Type.__name__ = "Integer32"
_Es2126DnsSetting_Object = MibScalar
es2126DnsSetting = _Es2126DnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2, 5),
    _Es2126DnsSetting_Type()
)
es2126DnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DnsSetting.setStatus("current")
_Es2126DnsServer_Type = IpAddress
_Es2126DnsServer_Object = MibScalar
es2126DnsServer = _Es2126DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 2, 6),
    _Es2126DnsServer_Type()
)
es2126DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DnsServer.setStatus("current")
_Es2126Time_ObjectIdentity = ObjectIdentity
es2126Time = _Es2126Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3)
)
_Es2126SystemCurrentTime_Type = DisplayString
_Es2126SystemCurrentTime_Object = MibScalar
es2126SystemCurrentTime = _Es2126SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 1),
    _Es2126SystemCurrentTime_Type()
)
es2126SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126SystemCurrentTime.setStatus("current")
_Es2126ManualTimeSetting_Type = DisplayString
_Es2126ManualTimeSetting_Object = MibScalar
es2126ManualTimeSetting = _Es2126ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 2),
    _Es2126ManualTimeSetting_Type()
)
es2126ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManualTimeSetting.setStatus("current")
_Es2126NTPServer_Type = DisplayString
_Es2126NTPServer_Object = MibScalar
es2126NTPServer = _Es2126NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 3),
    _Es2126NTPServer_Type()
)
es2126NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126NTPServer.setStatus("current")


class _Es2126NTPTimeZone_Type(Integer32):
    """Custom type es2126NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Es2126NTPTimeZone_Type.__name__ = "Integer32"
_Es2126NTPTimeZone_Object = MibScalar
es2126NTPTimeZone = _Es2126NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 4),
    _Es2126NTPTimeZone_Type()
)
es2126NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126NTPTimeZone.setStatus("current")


class _Es2126NTPTimeSync_Type(Integer32):
    """Custom type es2126NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126NTPTimeSync_Type.__name__ = "Integer32"
_Es2126NTPTimeSync_Object = MibScalar
es2126NTPTimeSync = _Es2126NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 5),
    _Es2126NTPTimeSync_Type()
)
es2126NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126NTPTimeSync.setStatus("current")


class _Es2126DaylightSavingTime_Type(Integer32):
    """Custom type es2126DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Es2126DaylightSavingTime_Type.__name__ = "Integer32"
_Es2126DaylightSavingTime_Object = MibScalar
es2126DaylightSavingTime = _Es2126DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 6),
    _Es2126DaylightSavingTime_Type()
)
es2126DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DaylightSavingTime.setStatus("current")
_Es2126DaylightStartTime_Type = DisplayString
_Es2126DaylightStartTime_Object = MibScalar
es2126DaylightStartTime = _Es2126DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 7),
    _Es2126DaylightStartTime_Type()
)
es2126DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DaylightStartTime.setStatus("current")
_Es2126DaylightEndTime_Type = DisplayString
_Es2126DaylightEndTime_Object = MibScalar
es2126DaylightEndTime = _Es2126DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 3, 8),
    _Es2126DaylightEndTime_Type()
)
es2126DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DaylightEndTime.setStatus("current")
_Es2126Account_ObjectIdentity = ObjectIdentity
es2126Account = _Es2126Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4)
)


class _Es2126AccountNumber_Type(Integer32):
    """Custom type es2126AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2126AccountNumber_Type.__name__ = "Integer32"
_Es2126AccountNumber_Object = MibScalar
es2126AccountNumber = _Es2126AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 1),
    _Es2126AccountNumber_Type()
)
es2126AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126AccountNumber.setStatus("current")
_Es2126AccountTable_Object = MibTable
es2126AccountTable = _Es2126AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    es2126AccountTable.setStatus("current")
_Es2126AccountEntry_Object = MibTableRow
es2126AccountEntry = _Es2126AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 2, 1)
)
es2126AccountEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126AccountIndex"),
)
if mibBuilder.loadTexts:
    es2126AccountEntry.setStatus("current")


class _Es2126AccountIndex_Type(Integer32):
    """Custom type es2126AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2126AccountIndex_Type.__name__ = "Integer32"
_Es2126AccountIndex_Object = MibTableColumn
es2126AccountIndex = _Es2126AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 2, 1, 1),
    _Es2126AccountIndex_Type()
)
es2126AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126AccountIndex.setStatus("current")
_Es2126AccountAuthorization_Type = DisplayString
_Es2126AccountAuthorization_Object = MibTableColumn
es2126AccountAuthorization = _Es2126AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 2, 1, 2),
    _Es2126AccountAuthorization_Type()
)
es2126AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126AccountAuthorization.setStatus("current")
_Es2126AccountName_Type = DisplayString
_Es2126AccountName_Object = MibTableColumn
es2126AccountName = _Es2126AccountName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 2, 1, 3),
    _Es2126AccountName_Type()
)
es2126AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountName.setStatus("current")
_Es2126AccountPassword_Type = DisplayString
_Es2126AccountPassword_Object = MibTableColumn
es2126AccountPassword = _Es2126AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 2, 1, 4),
    _Es2126AccountPassword_Type()
)
es2126AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountPassword.setStatus("current")
_Es2126AccountAddName_Type = DisplayString
_Es2126AccountAddName_Object = MibScalar
es2126AccountAddName = _Es2126AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 3),
    _Es2126AccountAddName_Type()
)
es2126AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountAddName.setStatus("current")
_Es2126AccountAddPassword_Type = DisplayString
_Es2126AccountAddPassword_Object = MibScalar
es2126AccountAddPassword = _Es2126AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 4),
    _Es2126AccountAddPassword_Type()
)
es2126AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountAddPassword.setStatus("current")


class _Es2126DoAccountAdd_Type(Integer32):
    """Custom type es2126DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126DoAccountAdd_Type.__name__ = "Integer32"
_Es2126DoAccountAdd_Object = MibScalar
es2126DoAccountAdd = _Es2126DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 5),
    _Es2126DoAccountAdd_Type()
)
es2126DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DoAccountAdd.setStatus("current")


class _Es2126AccountDel_Type(Integer32):
    """Custom type es2126AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Es2126AccountDel_Type.__name__ = "Integer32"
_Es2126AccountDel_Object = MibScalar
es2126AccountDel = _Es2126AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 1, 4, 6),
    _Es2126AccountDel_Type()
)
es2126AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountDel.setStatus("current")
_Es2126Snmp_ObjectIdentity = ObjectIdentity
es2126Snmp = _Es2126Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2)
)
_Es2126GetCommunity_Type = DisplayString
_Es2126GetCommunity_Object = MibScalar
es2126GetCommunity = _Es2126GetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 1),
    _Es2126GetCommunity_Type()
)
es2126GetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GetCommunity.setStatus("current")
_Es2126SetCommunity_Type = DisplayString
_Es2126SetCommunity_Object = MibScalar
es2126SetCommunity = _Es2126SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 2),
    _Es2126SetCommunity_Type()
)
es2126SetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126SetCommunity.setStatus("current")


class _Es2126TrapHostNumber_Type(Integer32):
    """Custom type es2126TrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126TrapHostNumber_Type.__name__ = "Integer32"
_Es2126TrapHostNumber_Object = MibScalar
es2126TrapHostNumber = _Es2126TrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 3),
    _Es2126TrapHostNumber_Type()
)
es2126TrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126TrapHostNumber.setStatus("current")
_Es2126TrapHostTable_Object = MibTable
es2126TrapHostTable = _Es2126TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 4)
)
if mibBuilder.loadTexts:
    es2126TrapHostTable.setStatus("current")
_Es2126TrapHostEntry_Object = MibTableRow
es2126TrapHostEntry = _Es2126TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 4, 1)
)
es2126TrapHostEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126TrapHostIndex"),
)
if mibBuilder.loadTexts:
    es2126TrapHostEntry.setStatus("current")


class _Es2126TrapHostIndex_Type(Integer32):
    """Custom type es2126TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126TrapHostIndex_Type.__name__ = "Integer32"
_Es2126TrapHostIndex_Object = MibTableColumn
es2126TrapHostIndex = _Es2126TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 4, 1, 1),
    _Es2126TrapHostIndex_Type()
)
es2126TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126TrapHostIndex.setStatus("current")
_Es2126TrapHostIP_Type = IpAddress
_Es2126TrapHostIP_Object = MibTableColumn
es2126TrapHostIP = _Es2126TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 4, 1, 2),
    _Es2126TrapHostIP_Type()
)
es2126TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrapHostIP.setStatus("current")


class _Es2126TrapHostPort_Type(Integer32):
    """Custom type es2126TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126TrapHostPort_Type.__name__ = "Integer32"
_Es2126TrapHostPort_Object = MibTableColumn
es2126TrapHostPort = _Es2126TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 4, 1, 3),
    _Es2126TrapHostPort_Type()
)
es2126TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrapHostPort.setStatus("current")
_Es2126TrapHostCommunity_Type = DisplayString
_Es2126TrapHostCommunity_Object = MibTableColumn
es2126TrapHostCommunity = _Es2126TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 4, 1, 4),
    _Es2126TrapHostCommunity_Type()
)
es2126TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrapHostCommunity.setStatus("current")
_Es2126RegisterMonitor_Type = DisplayString
_Es2126RegisterMonitor_Object = MibScalar
es2126RegisterMonitor = _Es2126RegisterMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 5),
    _Es2126RegisterMonitor_Type()
)
es2126RegisterMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126RegisterMonitor.setStatus("current")
_Es2126DeleteMonitor_Type = DisplayString
_Es2126DeleteMonitor_Object = MibScalar
es2126DeleteMonitor = _Es2126DeleteMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 6),
    _Es2126DeleteMonitor_Type()
)
es2126DeleteMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DeleteMonitor.setStatus("current")
_Es2126MonitorTable_Object = MibTable
es2126MonitorTable = _Es2126MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 7)
)
if mibBuilder.loadTexts:
    es2126MonitorTable.setStatus("current")
_Es2126MonitorEntry_Object = MibTableRow
es2126MonitorEntry = _Es2126MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 7, 1)
)
es2126MonitorEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126MonitorTableIp"),
)
if mibBuilder.loadTexts:
    es2126MonitorEntry.setStatus("current")
_Es2126MonitorTableIp_Type = IpAddress
_Es2126MonitorTableIp_Object = MibTableColumn
es2126MonitorTableIp = _Es2126MonitorTableIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 7, 1, 1),
    _Es2126MonitorTableIp_Type()
)
es2126MonitorTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126MonitorTableIp.setStatus("current")
_Es2126MonitorTableMac_Type = DisplayString
_Es2126MonitorTableMac_Object = MibTableColumn
es2126MonitorTableMac = _Es2126MonitorTableMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 7, 1, 2),
    _Es2126MonitorTableMac_Type()
)
es2126MonitorTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126MonitorTableMac.setStatus("current")


class _Es2126TrapBootDelayTime_Type(Integer32):
    """Custom type es2126TrapBootDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2126TrapBootDelayTime_Type.__name__ = "Integer32"
_Es2126TrapBootDelayTime_Object = MibScalar
es2126TrapBootDelayTime = _Es2126TrapBootDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 2, 8),
    _Es2126TrapBootDelayTime_Type()
)
es2126TrapBootDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrapBootDelayTime.setStatus("current")
_Es2126Alarm_ObjectIdentity = ObjectIdentity
es2126Alarm = _Es2126Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3)
)
_Es2126Event_ObjectIdentity = ObjectIdentity
es2126Event = _Es2126Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1)
)


class _Es2126EventNumber_Type(Integer32):
    """Custom type es2126EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126EventNumber_Type.__name__ = "Integer32"
_Es2126EventNumber_Object = MibScalar
es2126EventNumber = _Es2126EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 1),
    _Es2126EventNumber_Type()
)
es2126EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126EventNumber.setStatus("current")
_Es2126EventTable_Object = MibTable
es2126EventTable = _Es2126EventTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    es2126EventTable.setStatus("current")
_Es2126EventEntry_Object = MibTableRow
es2126EventEntry = _Es2126EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 2, 1)
)
es2126EventEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126EventIndex"),
)
if mibBuilder.loadTexts:
    es2126EventEntry.setStatus("current")


class _Es2126EventIndex_Type(Integer32):
    """Custom type es2126EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126EventIndex_Type.__name__ = "Integer32"
_Es2126EventIndex_Object = MibTableColumn
es2126EventIndex = _Es2126EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 2, 1, 1),
    _Es2126EventIndex_Type()
)
es2126EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126EventIndex.setStatus("current")
_Es2126EventName_Type = DisplayString
_Es2126EventName_Object = MibTableColumn
es2126EventName = _Es2126EventName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 2, 1, 2),
    _Es2126EventName_Type()
)
es2126EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126EventName.setStatus("current")


class _Es2126EventSendEmail_Type(Integer32):
    """Custom type es2126EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126EventSendEmail_Type.__name__ = "Integer32"
_Es2126EventSendEmail_Object = MibTableColumn
es2126EventSendEmail = _Es2126EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 2, 1, 3),
    _Es2126EventSendEmail_Type()
)
es2126EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EventSendEmail.setStatus("current")


class _Es2126EventSendTrap_Type(Integer32):
    """Custom type es2126EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126EventSendTrap_Type.__name__ = "Integer32"
_Es2126EventSendTrap_Object = MibTableColumn
es2126EventSendTrap = _Es2126EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 1, 2, 1, 4),
    _Es2126EventSendTrap_Type()
)
es2126EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EventSendTrap.setStatus("current")
_Es2126Email_ObjectIdentity = ObjectIdentity
es2126Email = _Es2126Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2)
)
_Es2126EmailServer_Type = DisplayString
_Es2126EmailServer_Object = MibScalar
es2126EmailServer = _Es2126EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 1),
    _Es2126EmailServer_Type()
)
es2126EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EmailServer.setStatus("current")
_Es2126EmailUsername_Type = DisplayString
_Es2126EmailUsername_Object = MibScalar
es2126EmailUsername = _Es2126EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 2),
    _Es2126EmailUsername_Type()
)
es2126EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EmailUsername.setStatus("current")
_Es2126EmailPassword_Type = DisplayString
_Es2126EmailPassword_Object = MibScalar
es2126EmailPassword = _Es2126EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 3),
    _Es2126EmailPassword_Type()
)
es2126EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EmailPassword.setStatus("current")
_Es2126EmailSender_Type = DisplayString
_Es2126EmailSender_Object = MibScalar
es2126EmailSender = _Es2126EmailSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 4),
    _Es2126EmailSender_Type()
)
es2126EmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EmailSender.setStatus("current")
_Es2126EmailReturnPath_Type = DisplayString
_Es2126EmailReturnPath_Object = MibScalar
es2126EmailReturnPath = _Es2126EmailReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 5),
    _Es2126EmailReturnPath_Type()
)
es2126EmailReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EmailReturnPath.setStatus("current")


class _Es2126EmailUserNumber_Type(Integer32):
    """Custom type es2126EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126EmailUserNumber_Type.__name__ = "Integer32"
_Es2126EmailUserNumber_Object = MibScalar
es2126EmailUserNumber = _Es2126EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 6),
    _Es2126EmailUserNumber_Type()
)
es2126EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126EmailUserNumber.setStatus("current")
_Es2126EmailUserTable_Object = MibTable
es2126EmailUserTable = _Es2126EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    es2126EmailUserTable.setStatus("current")
_Es2126EmailUserEntry_Object = MibTableRow
es2126EmailUserEntry = _Es2126EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 7, 1)
)
es2126EmailUserEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126EmailUserIndex"),
)
if mibBuilder.loadTexts:
    es2126EmailUserEntry.setStatus("current")


class _Es2126EmailUserIndex_Type(Integer32):
    """Custom type es2126EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126EmailUserIndex_Type.__name__ = "Integer32"
_Es2126EmailUserIndex_Object = MibTableColumn
es2126EmailUserIndex = _Es2126EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 7, 1, 1),
    _Es2126EmailUserIndex_Type()
)
es2126EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126EmailUserIndex.setStatus("current")
_Es2126EmailUserAddress_Type = DisplayString
_Es2126EmailUserAddress_Object = MibTableColumn
es2126EmailUserAddress = _Es2126EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 3, 2, 7, 1, 2),
    _Es2126EmailUserAddress_Type()
)
es2126EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126EmailUserAddress.setStatus("current")
_Es2126Tftp_ObjectIdentity = ObjectIdentity
es2126Tftp = _Es2126Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 4)
)
_Es2126RemoteTftpServer_Type = IpAddress
_Es2126RemoteTftpServer_Object = MibScalar
es2126RemoteTftpServer = _Es2126RemoteTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 4, 1),
    _Es2126RemoteTftpServer_Type()
)
es2126RemoteTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126RemoteTftpServer.setStatus("current")


class _Es2126InternalTftpServerState_Type(Integer32):
    """Custom type es2126InternalTftpServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126InternalTftpServerState_Type.__name__ = "Integer32"
_Es2126InternalTftpServerState_Object = MibScalar
es2126InternalTftpServerState = _Es2126InternalTftpServerState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 4, 2),
    _Es2126InternalTftpServerState_Type()
)
es2126InternalTftpServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126InternalTftpServerState.setStatus("current")
_Es2126Configuration_ObjectIdentity = ObjectIdentity
es2126Configuration = _Es2126Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5)
)
_Es2126SaveRestore_ObjectIdentity = ObjectIdentity
es2126SaveRestore = _Es2126SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 1)
)


class _Es2126SaveStart_Type(Integer32):
    """Custom type es2126SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126SaveStart_Type.__name__ = "Integer32"
_Es2126SaveStart_Object = MibScalar
es2126SaveStart = _Es2126SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 1, 1),
    _Es2126SaveStart_Type()
)
es2126SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126SaveStart.setStatus("current")


class _Es2126SaveUser_Type(Integer32):
    """Custom type es2126SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126SaveUser_Type.__name__ = "Integer32"
_Es2126SaveUser_Object = MibScalar
es2126SaveUser = _Es2126SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 1, 2),
    _Es2126SaveUser_Type()
)
es2126SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126SaveUser.setStatus("current")


class _Es2126RestoreDefault_Type(Integer32):
    """Custom type es2126RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126RestoreDefault_Type.__name__ = "Integer32"
_Es2126RestoreDefault_Object = MibScalar
es2126RestoreDefault = _Es2126RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 1, 3),
    _Es2126RestoreDefault_Type()
)
es2126RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126RestoreDefault.setStatus("current")


class _Es2126RestoreUser_Type(Integer32):
    """Custom type es2126RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126RestoreUser_Type.__name__ = "Integer32"
_Es2126RestoreUser_Object = MibScalar
es2126RestoreUser = _Es2126RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 1, 4),
    _Es2126RestoreUser_Type()
)
es2126RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126RestoreUser.setStatus("current")
_Es2126ConfigFile_ObjectIdentity = ObjectIdentity
es2126ConfigFile = _Es2126ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 2)
)
_Es2126ExportConfigName_Type = DisplayString
_Es2126ExportConfigName_Object = MibScalar
es2126ExportConfigName = _Es2126ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 2, 1),
    _Es2126ExportConfigName_Type()
)
es2126ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ExportConfigName.setStatus("current")


class _Es2126DoExportConfig_Type(Integer32):
    """Custom type es2126DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126DoExportConfig_Type.__name__ = "Integer32"
_Es2126DoExportConfig_Object = MibScalar
es2126DoExportConfig = _Es2126DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 2, 2),
    _Es2126DoExportConfig_Type()
)
es2126DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DoExportConfig.setStatus("current")
_Es2126ImportConfigName_Type = DisplayString
_Es2126ImportConfigName_Object = MibScalar
es2126ImportConfigName = _Es2126ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 2, 3),
    _Es2126ImportConfigName_Type()
)
es2126ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ImportConfigName.setStatus("current")


class _Es2126DoImportConfig_Type(Integer32):
    """Custom type es2126DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126DoImportConfig_Type.__name__ = "Integer32"
_Es2126DoImportConfig_Object = MibScalar
es2126DoImportConfig = _Es2126DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 5, 2, 4),
    _Es2126DoImportConfig_Type()
)
es2126DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DoImportConfig.setStatus("current")
_Es2126Diagnostic_ObjectIdentity = ObjectIdentity
es2126Diagnostic = _Es2126Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6)
)
_Es2126InternalLoopbackTest_Type = DisplayString
_Es2126InternalLoopbackTest_Object = MibScalar
es2126InternalLoopbackTest = _Es2126InternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 1),
    _Es2126InternalLoopbackTest_Type()
)
es2126InternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126InternalLoopbackTest.setStatus("current")
_Es2126ExternalLoopbackTest_Type = DisplayString
_Es2126ExternalLoopbackTest_Object = MibScalar
es2126ExternalLoopbackTest = _Es2126ExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 2),
    _Es2126ExternalLoopbackTest_Type()
)
es2126ExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126ExternalLoopbackTest.setStatus("current")
_Es2126PingTest_Type = DisplayString
_Es2126PingTest_Object = MibScalar
es2126PingTest = _Es2126PingTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 3),
    _Es2126PingTest_Type()
)
es2126PingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PingTest.setStatus("current")
_Es2126Watchdog_ObjectIdentity = ObjectIdentity
es2126Watchdog = _Es2126Watchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4)
)


class _Es2126WatchdogState_Type(Integer32):
    """Custom type es2126WatchdogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126WatchdogState_Type.__name__ = "Integer32"
_Es2126WatchdogState_Object = MibScalar
es2126WatchdogState = _Es2126WatchdogState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 1),
    _Es2126WatchdogState_Type()
)
es2126WatchdogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogState.setStatus("current")


class _Es2126WatchdogTimeGap_Type(Integer32):
    """Custom type es2126WatchdogTimeGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Es2126WatchdogTimeGap_Type.__name__ = "Integer32"
_Es2126WatchdogTimeGap_Object = MibScalar
es2126WatchdogTimeGap = _Es2126WatchdogTimeGap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 2),
    _Es2126WatchdogTimeGap_Type()
)
es2126WatchdogTimeGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogTimeGap.setStatus("current")
_Es2126WatchdogHost_Type = DisplayString
_Es2126WatchdogHost_Object = MibScalar
es2126WatchdogHost = _Es2126WatchdogHost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 3),
    _Es2126WatchdogHost_Type()
)
es2126WatchdogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogHost.setStatus("current")


class _Es2126WatchdogResetMgtInf_Type(Integer32):
    """Custom type es2126WatchdogResetMgtInf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126WatchdogResetMgtInf_Type.__name__ = "Integer32"
_Es2126WatchdogResetMgtInf_Object = MibScalar
es2126WatchdogResetMgtInf = _Es2126WatchdogResetMgtInf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 4),
    _Es2126WatchdogResetMgtInf_Type()
)
es2126WatchdogResetMgtInf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogResetMgtInf.setStatus("current")


class _Es2126WatchdogResetMgtInfCount_Type(Integer32):
    """Custom type es2126WatchdogResetMgtInfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Es2126WatchdogResetMgtInfCount_Type.__name__ = "Integer32"
_Es2126WatchdogResetMgtInfCount_Object = MibScalar
es2126WatchdogResetMgtInfCount = _Es2126WatchdogResetMgtInfCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 5),
    _Es2126WatchdogResetMgtInfCount_Type()
)
es2126WatchdogResetMgtInfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogResetMgtInfCount.setStatus("current")


class _Es2126WatchdogResetSystem_Type(Integer32):
    """Custom type es2126WatchdogResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126WatchdogResetSystem_Type.__name__ = "Integer32"
_Es2126WatchdogResetSystem_Object = MibScalar
es2126WatchdogResetSystem = _Es2126WatchdogResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 6),
    _Es2126WatchdogResetSystem_Type()
)
es2126WatchdogResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogResetSystem.setStatus("current")


class _Es2126WatchdogResetSystemCount_Type(Integer32):
    """Custom type es2126WatchdogResetSystemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Es2126WatchdogResetSystemCount_Type.__name__ = "Integer32"
_Es2126WatchdogResetSystemCount_Object = MibScalar
es2126WatchdogResetSystemCount = _Es2126WatchdogResetSystemCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 6, 4, 7),
    _Es2126WatchdogResetSystemCount_Type()
)
es2126WatchdogResetSystemCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126WatchdogResetSystemCount.setStatus("current")
_Es2126Log_ObjectIdentity = ObjectIdentity
es2126Log = _Es2126Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7)
)


class _Es2126ClearLog_Type(Integer32):
    """Custom type es2126ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126ClearLog_Type.__name__ = "Integer32"
_Es2126ClearLog_Object = MibScalar
es2126ClearLog = _Es2126ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 1),
    _Es2126ClearLog_Type()
)
es2126ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ClearLog.setStatus("current")


class _Es2126UploadLog_Type(Integer32):
    """Custom type es2126UploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126UploadLog_Type.__name__ = "Integer32"
_Es2126UploadLog_Object = MibScalar
es2126UploadLog = _Es2126UploadLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 2),
    _Es2126UploadLog_Type()
)
es2126UploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126UploadLog.setStatus("current")


class _Es2126AutoUploadLogState_Type(Integer32):
    """Custom type es2126AutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126AutoUploadLogState_Type.__name__ = "Integer32"
_Es2126AutoUploadLogState_Object = MibScalar
es2126AutoUploadLogState = _Es2126AutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 3),
    _Es2126AutoUploadLogState_Type()
)
es2126AutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AutoUploadLogState.setStatus("current")


class _Es2126LogNumber_Type(Integer32):
    """Custom type es2126LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2126LogNumber_Type.__name__ = "Integer32"
_Es2126LogNumber_Object = MibScalar
es2126LogNumber = _Es2126LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 4),
    _Es2126LogNumber_Type()
)
es2126LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126LogNumber.setStatus("current")
_Es2126LogTable_Object = MibTable
es2126LogTable = _Es2126LogTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 5)
)
if mibBuilder.loadTexts:
    es2126LogTable.setStatus("current")
_Es2126LogEntry_Object = MibTableRow
es2126LogEntry = _Es2126LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 5, 1)
)
es2126LogEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126LogIndex"),
)
if mibBuilder.loadTexts:
    es2126LogEntry.setStatus("current")


class _Es2126LogIndex_Type(Integer32):
    """Custom type es2126LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Es2126LogIndex_Type.__name__ = "Integer32"
_Es2126LogIndex_Object = MibTableColumn
es2126LogIndex = _Es2126LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 5, 1, 1),
    _Es2126LogIndex_Type()
)
es2126LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126LogIndex.setStatus("current")
_Es2126LogEvent_Type = DisplayString
_Es2126LogEvent_Object = MibTableColumn
es2126LogEvent = _Es2126LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 7, 5, 1, 2),
    _Es2126LogEvent_Type()
)
es2126LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126LogEvent.setStatus("current")
_Es2126Firmware_ObjectIdentity = ObjectIdentity
es2126Firmware = _Es2126Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 8)
)
_Es2126FirmwareFileName_Type = DisplayString
_Es2126FirmwareFileName_Object = MibScalar
es2126FirmwareFileName = _Es2126FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 8, 1),
    _Es2126FirmwareFileName_Type()
)
es2126FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126FirmwareFileName.setStatus("current")


class _Es2126DoFirmwareUpgrade_Type(Integer32):
    """Custom type es2126DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Es2126DoFirmwareUpgrade_Object = MibScalar
es2126DoFirmwareUpgrade = _Es2126DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 8, 2),
    _Es2126DoFirmwareUpgrade_Type()
)
es2126DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DoFirmwareUpgrade.setStatus("current")
_Es2126Port_ObjectIdentity = ObjectIdentity
es2126Port = _Es2126Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9)
)
_Es2126PortStatus_ObjectIdentity = ObjectIdentity
es2126PortStatus = _Es2126PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1)
)


class _Es2126PortStatusNumber_Type(Integer32):
    """Custom type es2126PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PortStatusNumber_Type.__name__ = "Integer32"
_Es2126PortStatusNumber_Object = MibScalar
es2126PortStatusNumber = _Es2126PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 1),
    _Es2126PortStatusNumber_Type()
)
es2126PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusNumber.setStatus("current")
_Es2126PortStatusTable_Object = MibTable
es2126PortStatusTable = _Es2126PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    es2126PortStatusTable.setStatus("current")
_Es2126PortStatusEntry_Object = MibTableRow
es2126PortStatusEntry = _Es2126PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1)
)
es2126PortStatusEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126PortStatusIndex"),
)
if mibBuilder.loadTexts:
    es2126PortStatusEntry.setStatus("current")


class _Es2126PortStatusIndex_Type(Integer32):
    """Custom type es2126PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PortStatusIndex_Type.__name__ = "Integer32"
_Es2126PortStatusIndex_Object = MibTableColumn
es2126PortStatusIndex = _Es2126PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 1),
    _Es2126PortStatusIndex_Type()
)
es2126PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusIndex.setStatus("current")
_Es2126PortStatusMedia_Type = DisplayString
_Es2126PortStatusMedia_Object = MibTableColumn
es2126PortStatusMedia = _Es2126PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 2),
    _Es2126PortStatusMedia_Type()
)
es2126PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusMedia.setStatus("current")
_Es2126PortStatusLink_Type = DisplayString
_Es2126PortStatusLink_Object = MibTableColumn
es2126PortStatusLink = _Es2126PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 3),
    _Es2126PortStatusLink_Type()
)
es2126PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusLink.setStatus("current")
_Es2126PortStatusPortState_Type = DisplayString
_Es2126PortStatusPortState_Object = MibTableColumn
es2126PortStatusPortState = _Es2126PortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 4),
    _Es2126PortStatusPortState_Type()
)
es2126PortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusPortState.setStatus("current")
_Es2126PortStatusAutoNego_Type = DisplayString
_Es2126PortStatusAutoNego_Object = MibTableColumn
es2126PortStatusAutoNego = _Es2126PortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 5),
    _Es2126PortStatusAutoNego_Type()
)
es2126PortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusAutoNego.setStatus("current")
_Es2126PortStatusSpdDpx_Type = DisplayString
_Es2126PortStatusSpdDpx_Object = MibTableColumn
es2126PortStatusSpdDpx = _Es2126PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 6),
    _Es2126PortStatusSpdDpx_Type()
)
es2126PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusSpdDpx.setStatus("current")
_Es2126PortStatusRxPause_Type = DisplayString
_Es2126PortStatusRxPause_Object = MibTableColumn
es2126PortStatusRxPause = _Es2126PortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 7),
    _Es2126PortStatusRxPause_Type()
)
es2126PortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusRxPause.setStatus("current")
_Es2126PortStatusTxPause_Type = DisplayString
_Es2126PortStatusTxPause_Object = MibTableColumn
es2126PortStatusTxPause = _Es2126PortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 8),
    _Es2126PortStatusTxPause_Type()
)
es2126PortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusTxPause.setStatus("current")
_Es2126PortStatusDescription_Type = DisplayString
_Es2126PortStatusDescription_Object = MibTableColumn
es2126PortStatusDescription = _Es2126PortStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 1, 2, 1, 9),
    _Es2126PortStatusDescription_Type()
)
es2126PortStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortStatusDescription.setStatus("current")
_Es2126PortConf_ObjectIdentity = ObjectIdentity
es2126PortConf = _Es2126PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2)
)


class _Es2126PortConfNumber_Type(Integer32):
    """Custom type es2126PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PortConfNumber_Type.__name__ = "Integer32"
_Es2126PortConfNumber_Object = MibScalar
es2126PortConfNumber = _Es2126PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 1),
    _Es2126PortConfNumber_Type()
)
es2126PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortConfNumber.setStatus("current")
_Es2126PortConfTable_Object = MibTable
es2126PortConfTable = _Es2126PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    es2126PortConfTable.setStatus("current")
_Es2126PortConfEntry_Object = MibTableRow
es2126PortConfEntry = _Es2126PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2, 1)
)
es2126PortConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126PortConfIndex"),
)
if mibBuilder.loadTexts:
    es2126PortConfEntry.setStatus("current")


class _Es2126PortConfIndex_Type(Integer32):
    """Custom type es2126PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PortConfIndex_Type.__name__ = "Integer32"
_Es2126PortConfIndex_Object = MibTableColumn
es2126PortConfIndex = _Es2126PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2, 1, 1),
    _Es2126PortConfIndex_Type()
)
es2126PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortConfIndex.setStatus("current")


class _Es2126PortConfPortState_Type(Integer32):
    """Custom type es2126PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PortConfPortState_Type.__name__ = "Integer32"
_Es2126PortConfPortState_Object = MibTableColumn
es2126PortConfPortState = _Es2126PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2, 1, 2),
    _Es2126PortConfPortState_Type()
)
es2126PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortConfPortState.setStatus("current")


class _Es2126PortConfSpdDpx_Type(Integer32):
    """Custom type es2126PortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Es2126PortConfSpdDpx_Type.__name__ = "Integer32"
_Es2126PortConfSpdDpx_Object = MibTableColumn
es2126PortConfSpdDpx = _Es2126PortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2, 1, 3),
    _Es2126PortConfSpdDpx_Type()
)
es2126PortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortConfSpdDpx.setStatus("current")


class _Es2126PortConfFlwCtrl_Type(Integer32):
    """Custom type es2126PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PortConfFlwCtrl_Type.__name__ = "Integer32"
_Es2126PortConfFlwCtrl_Object = MibTableColumn
es2126PortConfFlwCtrl = _Es2126PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2, 1, 4),
    _Es2126PortConfFlwCtrl_Type()
)
es2126PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortConfFlwCtrl.setStatus("current")
_Es2126PortConfDescription_Type = DisplayString
_Es2126PortConfDescription_Object = MibTableColumn
es2126PortConfDescription = _Es2126PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 2, 2, 1, 5),
    _Es2126PortConfDescription_Type()
)
es2126PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortConfDescription.setStatus("current")
_Es2126PortBandwidth_ObjectIdentity = ObjectIdentity
es2126PortBandwidth = _Es2126PortBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3)
)
_Es2126PortBandwidthTable_Object = MibTable
es2126PortBandwidthTable = _Es2126PortBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    es2126PortBandwidthTable.setStatus("current")
_Es2126PortBandwidthEntry_Object = MibTableRow
es2126PortBandwidthEntry = _Es2126PortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 1, 1)
)
es2126PortBandwidthEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126PortBandwidthIndex"),
)
if mibBuilder.loadTexts:
    es2126PortBandwidthEntry.setStatus("current")


class _Es2126PortBandwidthIndex_Type(Integer32):
    """Custom type es2126PortBandwidthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PortBandwidthIndex_Type.__name__ = "Integer32"
_Es2126PortBandwidthIndex_Object = MibTableColumn
es2126PortBandwidthIndex = _Es2126PortBandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 1, 1, 1),
    _Es2126PortBandwidthIndex_Type()
)
es2126PortBandwidthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortBandwidthIndex.setStatus("current")


class _Es2126PortBandwidthIngressRate_Type(Integer32):
    """Custom type es2126PortBandwidthIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 1024000),
    )


_Es2126PortBandwidthIngressRate_Type.__name__ = "Integer32"
_Es2126PortBandwidthIngressRate_Object = MibTableColumn
es2126PortBandwidthIngressRate = _Es2126PortBandwidthIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 1, 1, 2),
    _Es2126PortBandwidthIngressRate_Type()
)
es2126PortBandwidthIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBandwidthIngressRate.setStatus("current")


class _Es2126PortBandwidthEgressRate_Type(Integer32):
    """Custom type es2126PortBandwidthEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 1024000),
    )


_Es2126PortBandwidthEgressRate_Type.__name__ = "Integer32"
_Es2126PortBandwidthEgressRate_Object = MibTableColumn
es2126PortBandwidthEgressRate = _Es2126PortBandwidthEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 1, 1, 3),
    _Es2126PortBandwidthEgressRate_Type()
)
es2126PortBandwidthEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBandwidthEgressRate.setStatus("current")


class _Es2126PortBandwidthStormType_Type(Integer32):
    """Custom type es2126PortBandwidthStormType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Es2126PortBandwidthStormType_Type.__name__ = "Integer32"
_Es2126PortBandwidthStormType_Object = MibScalar
es2126PortBandwidthStormType = _Es2126PortBandwidthStormType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 2),
    _Es2126PortBandwidthStormType_Type()
)
es2126PortBandwidthStormType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBandwidthStormType.setStatus("current")


class _Es2126PortBandwidthStormRate_Type(Integer32):
    """Custom type es2126PortBandwidthStormRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Es2126PortBandwidthStormRate_Type.__name__ = "Integer32"
_Es2126PortBandwidthStormRate_Object = MibScalar
es2126PortBandwidthStormRate = _Es2126PortBandwidthStormRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 3, 3),
    _Es2126PortBandwidthStormRate_Type()
)
es2126PortBandwidthStormRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBandwidthStormRate.setStatus("current")
_Es2126PortSFPInfo_ObjectIdentity = ObjectIdentity
es2126PortSFPInfo = _Es2126PortSFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4)
)


class _Es2126PortSFPInfoNumber_Type(Integer32):
    """Custom type es2126PortSFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PortSFPInfoNumber_Type.__name__ = "Integer32"
_Es2126PortSFPInfoNumber_Object = MibScalar
es2126PortSFPInfoNumber = _Es2126PortSFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 1),
    _Es2126PortSFPInfoNumber_Type()
)
es2126PortSFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPInfoNumber.setStatus("current")
_Es2126PortSFPInfoTable_Object = MibTable
es2126PortSFPInfoTable = _Es2126PortSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    es2126PortSFPInfoTable.setStatus("current")
_Es2126PortSFPInfoEntry_Object = MibTableRow
es2126PortSFPInfoEntry = _Es2126PortSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1)
)
es2126PortSFPInfoEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126PortSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    es2126PortSFPInfoEntry.setStatus("current")


class _Es2126PortSFPInfoIndex_Type(Integer32):
    """Custom type es2126PortSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PortSFPInfoIndex_Type.__name__ = "Integer32"
_Es2126PortSFPInfoIndex_Object = MibTableColumn
es2126PortSFPInfoIndex = _Es2126PortSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 1),
    _Es2126PortSFPInfoIndex_Type()
)
es2126PortSFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPInfoIndex.setStatus("current")
_Es2126PortSFPConnectorType_Type = DisplayString
_Es2126PortSFPConnectorType_Object = MibTableColumn
es2126PortSFPConnectorType = _Es2126PortSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 2),
    _Es2126PortSFPConnectorType_Type()
)
es2126PortSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPConnectorType.setStatus("current")
_Es2126PortSFPFiberType_Type = DisplayString
_Es2126PortSFPFiberType_Object = MibTableColumn
es2126PortSFPFiberType = _Es2126PortSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 3),
    _Es2126PortSFPFiberType_Type()
)
es2126PortSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPFiberType.setStatus("current")
_Es2126PortSFPWavelength_Type = DisplayString
_Es2126PortSFPWavelength_Object = MibTableColumn
es2126PortSFPWavelength = _Es2126PortSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 4),
    _Es2126PortSFPWavelength_Type()
)
es2126PortSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPWavelength.setStatus("current")
_Es2126PortSFPBaudRate_Type = DisplayString
_Es2126PortSFPBaudRate_Object = MibTableColumn
es2126PortSFPBaudRate = _Es2126PortSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 5),
    _Es2126PortSFPBaudRate_Type()
)
es2126PortSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPBaudRate.setStatus("current")
_Es2126PortSFPVendorOUI_Type = DisplayString
_Es2126PortSFPVendorOUI_Object = MibTableColumn
es2126PortSFPVendorOUI = _Es2126PortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 6),
    _Es2126PortSFPVendorOUI_Type()
)
es2126PortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPVendorOUI.setStatus("current")
_Es2126PortSFPVendorName_Type = DisplayString
_Es2126PortSFPVendorName_Object = MibTableColumn
es2126PortSFPVendorName = _Es2126PortSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 7),
    _Es2126PortSFPVendorName_Type()
)
es2126PortSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPVendorName.setStatus("current")
_Es2126PortSFPVendorPN_Type = DisplayString
_Es2126PortSFPVendorPN_Object = MibTableColumn
es2126PortSFPVendorPN = _Es2126PortSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 8),
    _Es2126PortSFPVendorPN_Type()
)
es2126PortSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPVendorPN.setStatus("current")
_Es2126PortSFPVendorRev_Type = DisplayString
_Es2126PortSFPVendorRev_Object = MibTableColumn
es2126PortSFPVendorRev = _Es2126PortSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 9),
    _Es2126PortSFPVendorRev_Type()
)
es2126PortSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPVendorRev.setStatus("current")
_Es2126PortSFPVendorSN_Type = DisplayString
_Es2126PortSFPVendorSN_Object = MibTableColumn
es2126PortSFPVendorSN = _Es2126PortSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 10),
    _Es2126PortSFPVendorSN_Type()
)
es2126PortSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPVendorSN.setStatus("current")
_Es2126PortSFPDateCode_Type = DisplayString
_Es2126PortSFPDateCode_Object = MibTableColumn
es2126PortSFPDateCode = _Es2126PortSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 11),
    _Es2126PortSFPDateCode_Type()
)
es2126PortSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPDateCode.setStatus("current")
_Es2126PortSFPTemperature_Type = DisplayString
_Es2126PortSFPTemperature_Object = MibTableColumn
es2126PortSFPTemperature = _Es2126PortSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 12),
    _Es2126PortSFPTemperature_Type()
)
es2126PortSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPTemperature.setStatus("current")
_Es2126PortSFPVcc_Type = DisplayString
_Es2126PortSFPVcc_Object = MibTableColumn
es2126PortSFPVcc = _Es2126PortSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 13),
    _Es2126PortSFPVcc_Type()
)
es2126PortSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPVcc.setStatus("current")
_Es2126PortSFPTxBias_Type = DisplayString
_Es2126PortSFPTxBias_Object = MibTableColumn
es2126PortSFPTxBias = _Es2126PortSFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 14),
    _Es2126PortSFPTxBias_Type()
)
es2126PortSFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPTxBias.setStatus("current")
_Es2126PortSFPTxPWR_Type = DisplayString
_Es2126PortSFPTxPWR_Object = MibTableColumn
es2126PortSFPTxPWR = _Es2126PortSFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 15),
    _Es2126PortSFPTxPWR_Type()
)
es2126PortSFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPTxPWR.setStatus("current")
_Es2126PortSFPRxPWR_Type = DisplayString
_Es2126PortSFPRxPWR_Object = MibTableColumn
es2126PortSFPRxPWR = _Es2126PortSFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 9, 4, 2, 1, 16),
    _Es2126PortSFPRxPWR_Type()
)
es2126PortSFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortSFPRxPWR.setStatus("current")
_Es2126LoopDetectedConf_ObjectIdentity = ObjectIdentity
es2126LoopDetectedConf = _Es2126LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10)
)


class _Es2126LoopDetectedNumber_Type(Integer32):
    """Custom type es2126LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126LoopDetectedNumber_Type.__name__ = "Integer32"
_Es2126LoopDetectedNumber_Object = MibScalar
es2126LoopDetectedNumber = _Es2126LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 1),
    _Es2126LoopDetectedNumber_Type()
)
es2126LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126LoopDetectedNumber.setStatus("current")
_Es2126LoopDetectedTable_Object = MibTable
es2126LoopDetectedTable = _Es2126LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 2)
)
if mibBuilder.loadTexts:
    es2126LoopDetectedTable.setStatus("current")
_Es2126LoopDetectedEntry_Object = MibTableRow
es2126LoopDetectedEntry = _Es2126LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 2, 1)
)
es2126LoopDetectedEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    es2126LoopDetectedEntry.setStatus("current")


class _Es2126LoopDetectedfIndex_Type(Integer32):
    """Custom type es2126LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126LoopDetectedfIndex_Type.__name__ = "Integer32"
_Es2126LoopDetectedfIndex_Object = MibTableColumn
es2126LoopDetectedfIndex = _Es2126LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 2, 1, 1),
    _Es2126LoopDetectedfIndex_Type()
)
es2126LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126LoopDetectedfIndex.setStatus("current")


class _Es2126LoopDetectedStateEbl_Type(Integer32):
    """Custom type es2126LoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126LoopDetectedStateEbl_Type.__name__ = "Integer32"
_Es2126LoopDetectedStateEbl_Object = MibTableColumn
es2126LoopDetectedStateEbl = _Es2126LoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 2, 1, 2),
    _Es2126LoopDetectedStateEbl_Type()
)
es2126LoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LoopDetectedStateEbl.setStatus("current")


class _Es2126LoopDetectedCurrentStatus_Type(Integer32):
    """Custom type es2126LoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126LoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_Es2126LoopDetectedCurrentStatus_Object = MibTableColumn
es2126LoopDetectedCurrentStatus = _Es2126LoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 2, 1, 3),
    _Es2126LoopDetectedCurrentStatus_Type()
)
es2126LoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126LoopDetectedCurrentStatus.setStatus("current")


class _Es2126LoopDetectedResumed_Type(Integer32):
    """Custom type es2126LoopDetectedResumed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126LoopDetectedResumed_Type.__name__ = "Integer32"
_Es2126LoopDetectedResumed_Object = MibTableColumn
es2126LoopDetectedResumed = _Es2126LoopDetectedResumed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 2, 1, 4),
    _Es2126LoopDetectedResumed_Type()
)
es2126LoopDetectedResumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LoopDetectedResumed.setStatus("current")


class _Es2126LoopDetectedAction_Type(Integer32):
    """Custom type es2126LoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126LoopDetectedAction_Type.__name__ = "Integer32"
_Es2126LoopDetectedAction_Object = MibScalar
es2126LoopDetectedAction = _Es2126LoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 10, 3),
    _Es2126LoopDetectedAction_Type()
)
es2126LoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LoopDetectedAction.setStatus("current")
_Es2126MacTableInfo_ObjectIdentity = ObjectIdentity
es2126MacTableInfo = _Es2126MacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11)
)
_Es2126MacTableMaintenance_ObjectIdentity = ObjectIdentity
es2126MacTableMaintenance = _Es2126MacTableMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1)
)


class _Es2126MacTableAgingTime_Type(Integer32):
    """Custom type es2126MacTableAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_Es2126MacTableAgingTime_Type.__name__ = "Integer32"
_Es2126MacTableAgingTime_Object = MibScalar
es2126MacTableAgingTime = _Es2126MacTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1, 1),
    _Es2126MacTableAgingTime_Type()
)
es2126MacTableAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableAgingTime.setStatus("current")


class _Es2126MacTableFlush_Type(Integer32):
    """Custom type es2126MacTableFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126MacTableFlush_Type.__name__ = "Integer32"
_Es2126MacTableFlush_Object = MibScalar
es2126MacTableFlush = _Es2126MacTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1, 2),
    _Es2126MacTableFlush_Type()
)
es2126MacTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableFlush.setStatus("current")
_Es2126MacTableLearnPortLimitTable_Object = MibTable
es2126MacTableLearnPortLimitTable = _Es2126MacTableLearnPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    es2126MacTableLearnPortLimitTable.setStatus("current")
_Es2126MacTableLearnPortLimitEntry_Object = MibTableRow
es2126MacTableLearnPortLimitEntry = _Es2126MacTableLearnPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1, 3, 1)
)
es2126MacTableLearnPortLimitEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126MacTableLearnPortLimitIndex"),
)
if mibBuilder.loadTexts:
    es2126MacTableLearnPortLimitEntry.setStatus("current")


class _Es2126MacTableLearnPortLimitIndex_Type(Integer32):
    """Custom type es2126MacTableLearnPortLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126MacTableLearnPortLimitIndex_Type.__name__ = "Integer32"
_Es2126MacTableLearnPortLimitIndex_Object = MibTableColumn
es2126MacTableLearnPortLimitIndex = _Es2126MacTableLearnPortLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1, 3, 1, 1),
    _Es2126MacTableLearnPortLimitIndex_Type()
)
es2126MacTableLearnPortLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126MacTableLearnPortLimitIndex.setStatus("current")


class _Es2126MacTableLearnPortLimit_Type(Integer32):
    """Custom type es2126MacTableLearnPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_Es2126MacTableLearnPortLimit_Type.__name__ = "Integer32"
_Es2126MacTableLearnPortLimit_Object = MibTableColumn
es2126MacTableLearnPortLimit = _Es2126MacTableLearnPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 1, 3, 1, 2),
    _Es2126MacTableLearnPortLimit_Type()
)
es2126MacTableLearnPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableLearnPortLimit.setStatus("current")
_Es2126MacTableStaticMac_ObjectIdentity = ObjectIdentity
es2126MacTableStaticMac = _Es2126MacTableStaticMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3)
)


class _Es2126MacTableStaticMacNumber_Type(Integer32):
    """Custom type es2126MacTableStaticMacNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2126MacTableStaticMacNumber_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacNumber_Object = MibScalar
es2126MacTableStaticMacNumber = _Es2126MacTableStaticMacNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 1),
    _Es2126MacTableStaticMacNumber_Type()
)
es2126MacTableStaticMacNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacNumber.setStatus("current")


class _Es2126MacTableStaticMacEntryCreate_Type(Integer32):
    """Custom type es2126MacTableStaticMacEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2126MacTableStaticMacEntryCreate_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacEntryCreate_Object = MibScalar
es2126MacTableStaticMacEntryCreate = _Es2126MacTableStaticMacEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 2),
    _Es2126MacTableStaticMacEntryCreate_Type()
)
es2126MacTableStaticMacEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacEntryCreate.setStatus("current")
_Es2126MacTableStaticMacTable_Object = MibTable
es2126MacTableStaticMacTable = _Es2126MacTableStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    es2126MacTableStaticMacTable.setStatus("current")
_Es2126MacTableStaticMacEntry_Object = MibTableRow
es2126MacTableStaticMacEntry = _Es2126MacTableStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1)
)
es2126MacTableStaticMacEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126MacTableStaticMacIndex"),
)
if mibBuilder.loadTexts:
    es2126MacTableStaticMacEntry.setStatus("current")


class _Es2126MacTableStaticMacIndex_Type(Integer32):
    """Custom type es2126MacTableStaticMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2126MacTableStaticMacIndex_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacIndex_Object = MibTableColumn
es2126MacTableStaticMacIndex = _Es2126MacTableStaticMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 1),
    _Es2126MacTableStaticMacIndex_Type()
)
es2126MacTableStaticMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacIndex.setStatus("current")
_Es2126MacTableStaticMacAddress_Type = DisplayString
_Es2126MacTableStaticMacAddress_Object = MibTableColumn
es2126MacTableStaticMacAddress = _Es2126MacTableStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 2),
    _Es2126MacTableStaticMacAddress_Type()
)
es2126MacTableStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacAddress.setStatus("current")


class _Es2126MacTableStaticMacVid_Type(Integer32):
    """Custom type es2126MacTableStaticMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126MacTableStaticMacVid_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacVid_Object = MibTableColumn
es2126MacTableStaticMacVid = _Es2126MacTableStaticMacVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 3),
    _Es2126MacTableStaticMacVid_Type()
)
es2126MacTableStaticMacVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacVid.setStatus("current")


class _Es2126MacTableStaticMacQueue_Type(Integer32):
    """Custom type es2126MacTableStaticMacQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126MacTableStaticMacQueue_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacQueue_Object = MibTableColumn
es2126MacTableStaticMacQueue = _Es2126MacTableStaticMacQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 4),
    _Es2126MacTableStaticMacQueue_Type()
)
es2126MacTableStaticMacQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacQueue.setStatus("current")


class _Es2126MacTableStaticMacFwRule_Type(Integer32):
    """Custom type es2126MacTableStaticMacFwRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126MacTableStaticMacFwRule_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacFwRule_Object = MibTableColumn
es2126MacTableStaticMacFwRule = _Es2126MacTableStaticMacFwRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 5),
    _Es2126MacTableStaticMacFwRule_Type()
)
es2126MacTableStaticMacFwRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacFwRule.setStatus("current")


class _Es2126MacTableStaticMacPort_Type(Integer32):
    """Custom type es2126MacTableStaticMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126MacTableStaticMacPort_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacPort_Object = MibTableColumn
es2126MacTableStaticMacPort = _Es2126MacTableStaticMacPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 6),
    _Es2126MacTableStaticMacPort_Type()
)
es2126MacTableStaticMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacPort.setStatus("current")


class _Es2126MacTableStaticMacEntryAction_Type(Integer32):
    """Custom type es2126MacTableStaticMacEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126MacTableStaticMacEntryAction_Type.__name__ = "Integer32"
_Es2126MacTableStaticMacEntryAction_Object = MibTableColumn
es2126MacTableStaticMacEntryAction = _Es2126MacTableStaticMacEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 3, 3, 1, 7),
    _Es2126MacTableStaticMacEntryAction_Type()
)
es2126MacTableStaticMacEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableStaticMacEntryAction.setStatus("current")
_Es2126MacTableMacAlias_ObjectIdentity = ObjectIdentity
es2126MacTableMacAlias = _Es2126MacTableMacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4)
)


class _Es2126MacTableMacAliasNumber_Type(Integer32):
    """Custom type es2126MacTableMacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_Es2126MacTableMacAliasNumber_Type.__name__ = "Integer32"
_Es2126MacTableMacAliasNumber_Object = MibScalar
es2126MacTableMacAliasNumber = _Es2126MacTableMacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 1),
    _Es2126MacTableMacAliasNumber_Type()
)
es2126MacTableMacAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126MacTableMacAliasNumber.setStatus("current")


class _Es2126MacTableMacAliasEntryCreate_Type(Integer32):
    """Custom type es2126MacTableMacAliasEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_Es2126MacTableMacAliasEntryCreate_Type.__name__ = "Integer32"
_Es2126MacTableMacAliasEntryCreate_Object = MibScalar
es2126MacTableMacAliasEntryCreate = _Es2126MacTableMacAliasEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 2),
    _Es2126MacTableMacAliasEntryCreate_Type()
)
es2126MacTableMacAliasEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableMacAliasEntryCreate.setStatus("current")
_Es2126MacTableMacAliasTable_Object = MibTable
es2126MacTableMacAliasTable = _Es2126MacTableMacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 3)
)
if mibBuilder.loadTexts:
    es2126MacTableMacAliasTable.setStatus("current")
_Es2126MacTableMacAliasEntry_Object = MibTableRow
es2126MacTableMacAliasEntry = _Es2126MacTableMacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 3, 1)
)
es2126MacTableMacAliasEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126MacTableMacAliasIndex"),
)
if mibBuilder.loadTexts:
    es2126MacTableMacAliasEntry.setStatus("current")


class _Es2126MacTableMacAliasIndex_Type(Integer32):
    """Custom type es2126MacTableMacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2126MacTableMacAliasIndex_Type.__name__ = "Integer32"
_Es2126MacTableMacAliasIndex_Object = MibTableColumn
es2126MacTableMacAliasIndex = _Es2126MacTableMacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 3, 1, 1),
    _Es2126MacTableMacAliasIndex_Type()
)
es2126MacTableMacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126MacTableMacAliasIndex.setStatus("current")
_Es2126MacTableMacAliasAddress_Type = DisplayString
_Es2126MacTableMacAliasAddress_Object = MibTableColumn
es2126MacTableMacAliasAddress = _Es2126MacTableMacAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 3, 1, 2),
    _Es2126MacTableMacAliasAddress_Type()
)
es2126MacTableMacAliasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableMacAliasAddress.setStatus("current")
_Es2126MacTableMacAliasAlias_Type = DisplayString
_Es2126MacTableMacAliasAlias_Object = MibTableColumn
es2126MacTableMacAliasAlias = _Es2126MacTableMacAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 3, 1, 3),
    _Es2126MacTableMacAliasAlias_Type()
)
es2126MacTableMacAliasAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableMacAliasAlias.setStatus("current")


class _Es2126MacTableMacAliasEntryAction_Type(Integer32):
    """Custom type es2126MacTableMacAliasEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126MacTableMacAliasEntryAction_Type.__name__ = "Integer32"
_Es2126MacTableMacAliasEntryAction_Object = MibTableColumn
es2126MacTableMacAliasEntryAction = _Es2126MacTableMacAliasEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 11, 4, 3, 1, 4),
    _Es2126MacTableMacAliasEntryAction_Type()
)
es2126MacTableMacAliasEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MacTableMacAliasEntryAction.setStatus("current")
_Es2126GVRPInfo_ObjectIdentity = ObjectIdentity
es2126GVRPInfo = _Es2126GVRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12)
)
_Es2126GvrpConf_ObjectIdentity = ObjectIdentity
es2126GvrpConf = _Es2126GvrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1)
)


class _Es2126GvrpConfState_Type(Integer32):
    """Custom type es2126GvrpConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126GvrpConfState_Type.__name__ = "Integer32"
_Es2126GvrpConfState_Object = MibScalar
es2126GvrpConfState = _Es2126GvrpConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 1),
    _Es2126GvrpConfState_Type()
)
es2126GvrpConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfState.setStatus("current")
_Es2126GvrpConfTable_Object = MibTable
es2126GvrpConfTable = _Es2126GvrpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    es2126GvrpConfTable.setStatus("current")
_Es2126GvrpConfEntry_Object = MibTableRow
es2126GvrpConfEntry = _Es2126GvrpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1)
)
es2126GvrpConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126GvrpConfIndex"),
)
if mibBuilder.loadTexts:
    es2126GvrpConfEntry.setStatus("current")


class _Es2126GvrpConfIndex_Type(Integer32):
    """Custom type es2126GvrpConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126GvrpConfIndex_Type.__name__ = "Integer32"
_Es2126GvrpConfIndex_Object = MibTableColumn
es2126GvrpConfIndex = _Es2126GvrpConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 1),
    _Es2126GvrpConfIndex_Type()
)
es2126GvrpConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126GvrpConfIndex.setStatus("current")


class _Es2126GvrpConfJoinTime_Type(Integer32):
    """Custom type es2126GvrpConfJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Es2126GvrpConfJoinTime_Type.__name__ = "Integer32"
_Es2126GvrpConfJoinTime_Object = MibTableColumn
es2126GvrpConfJoinTime = _Es2126GvrpConfJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 2),
    _Es2126GvrpConfJoinTime_Type()
)
es2126GvrpConfJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfJoinTime.setStatus("current")


class _Es2126GvrpConfLeaveTime_Type(Integer32):
    """Custom type es2126GvrpConfLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Es2126GvrpConfLeaveTime_Type.__name__ = "Integer32"
_Es2126GvrpConfLeaveTime_Object = MibTableColumn
es2126GvrpConfLeaveTime = _Es2126GvrpConfLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 3),
    _Es2126GvrpConfLeaveTime_Type()
)
es2126GvrpConfLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfLeaveTime.setStatus("current")


class _Es2126GvrpConfLeaveAllTime_Type(Integer32):
    """Custom type es2126GvrpConfLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_Es2126GvrpConfLeaveAllTime_Type.__name__ = "Integer32"
_Es2126GvrpConfLeaveAllTime_Object = MibTableColumn
es2126GvrpConfLeaveAllTime = _Es2126GvrpConfLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 4),
    _Es2126GvrpConfLeaveAllTime_Type()
)
es2126GvrpConfLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfLeaveAllTime.setStatus("current")


class _Es2126GvrpConfDefaultAppMode_Type(Integer32):
    """Custom type es2126GvrpConfDefaultAppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126GvrpConfDefaultAppMode_Type.__name__ = "Integer32"
_Es2126GvrpConfDefaultAppMode_Object = MibTableColumn
es2126GvrpConfDefaultAppMode = _Es2126GvrpConfDefaultAppMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 5),
    _Es2126GvrpConfDefaultAppMode_Type()
)
es2126GvrpConfDefaultAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfDefaultAppMode.setStatus("current")


class _Es2126GvrpConfDefaultRegMode_Type(Integer32):
    """Custom type es2126GvrpConfDefaultRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126GvrpConfDefaultRegMode_Type.__name__ = "Integer32"
_Es2126GvrpConfDefaultRegMode_Object = MibTableColumn
es2126GvrpConfDefaultRegMode = _Es2126GvrpConfDefaultRegMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 6),
    _Es2126GvrpConfDefaultRegMode_Type()
)
es2126GvrpConfDefaultRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfDefaultRegMode.setStatus("current")


class _Es2126GvrpConfRestrictedMode_Type(Integer32):
    """Custom type es2126GvrpConfRestrictedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126GvrpConfRestrictedMode_Type.__name__ = "Integer32"
_Es2126GvrpConfRestrictedMode_Object = MibTableColumn
es2126GvrpConfRestrictedMode = _Es2126GvrpConfRestrictedMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 1, 2, 1, 7),
    _Es2126GvrpConfRestrictedMode_Type()
)
es2126GvrpConfRestrictedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126GvrpConfRestrictedMode.setStatus("current")
_Es2126GvrpCounter_ObjectIdentity = ObjectIdentity
es2126GvrpCounter = _Es2126GvrpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2)
)
_Es2126GvrpCounterTable_Object = MibTable
es2126GvrpCounterTable = _Es2126GvrpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    es2126GvrpCounterTable.setStatus("current")
_Es2126GvrpCounterEntry_Object = MibTableRow
es2126GvrpCounterEntry = _Es2126GvrpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1)
)
es2126GvrpCounterEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126GvrpCounterIndex"),
)
if mibBuilder.loadTexts:
    es2126GvrpCounterEntry.setStatus("current")


class _Es2126GvrpCounterIndex_Type(Integer32):
    """Custom type es2126GvrpCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126GvrpCounterIndex_Type.__name__ = "Integer32"
_Es2126GvrpCounterIndex_Object = MibTableColumn
es2126GvrpCounterIndex = _Es2126GvrpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 1),
    _Es2126GvrpCounterIndex_Type()
)
es2126GvrpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126GvrpCounterIndex.setStatus("current")
_Es2126GvrpCounterRxTotalGvrpPkts_Type = Counter32
_Es2126GvrpCounterRxTotalGvrpPkts_Object = MibTableColumn
es2126GvrpCounterRxTotalGvrpPkts = _Es2126GvrpCounterRxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 2),
    _Es2126GvrpCounterRxTotalGvrpPkts_Type()
)
es2126GvrpCounterRxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxTotalGvrpPkts.setStatus("current")
_Es2126GvrpCounterRxInvalidGvrpPkts_Type = Counter32
_Es2126GvrpCounterRxInvalidGvrpPkts_Object = MibTableColumn
es2126GvrpCounterRxInvalidGvrpPkts = _Es2126GvrpCounterRxInvalidGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 3),
    _Es2126GvrpCounterRxInvalidGvrpPkts_Type()
)
es2126GvrpCounterRxInvalidGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxInvalidGvrpPkts.setStatus("current")
_Es2126GvrpCounterRxLeaveAllMsg_Type = Counter32
_Es2126GvrpCounterRxLeaveAllMsg_Object = MibTableColumn
es2126GvrpCounterRxLeaveAllMsg = _Es2126GvrpCounterRxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 4),
    _Es2126GvrpCounterRxLeaveAllMsg_Type()
)
es2126GvrpCounterRxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxLeaveAllMsg.setStatus("current")
_Es2126GvrpCounterRxJoinEmptyMsg_Type = Counter32
_Es2126GvrpCounterRxJoinEmptyMsg_Object = MibTableColumn
es2126GvrpCounterRxJoinEmptyMsg = _Es2126GvrpCounterRxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 5),
    _Es2126GvrpCounterRxJoinEmptyMsg_Type()
)
es2126GvrpCounterRxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxJoinEmptyMsg.setStatus("current")
_Es2126GvrpCounterRxJoinInMsg_Type = Counter32
_Es2126GvrpCounterRxJoinInMsg_Object = MibTableColumn
es2126GvrpCounterRxJoinInMsg = _Es2126GvrpCounterRxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 6),
    _Es2126GvrpCounterRxJoinInMsg_Type()
)
es2126GvrpCounterRxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxJoinInMsg.setStatus("current")
_Es2126GvrpCounterRxLeaveEmptyMsg_Type = Counter32
_Es2126GvrpCounterRxLeaveEmptyMsg_Object = MibTableColumn
es2126GvrpCounterRxLeaveEmptyMsg = _Es2126GvrpCounterRxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 7),
    _Es2126GvrpCounterRxLeaveEmptyMsg_Type()
)
es2126GvrpCounterRxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxLeaveEmptyMsg.setStatus("current")
_Es2126GvrpCounterRxEmptyMsg_Type = Counter32
_Es2126GvrpCounterRxEmptyMsg_Object = MibTableColumn
es2126GvrpCounterRxEmptyMsg = _Es2126GvrpCounterRxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 8),
    _Es2126GvrpCounterRxEmptyMsg_Type()
)
es2126GvrpCounterRxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterRxEmptyMsg.setStatus("current")
_Es2126GvrpCounterTxTotalGvrpPkts_Type = Counter32
_Es2126GvrpCounterTxTotalGvrpPkts_Object = MibTableColumn
es2126GvrpCounterTxTotalGvrpPkts = _Es2126GvrpCounterTxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 9),
    _Es2126GvrpCounterTxTotalGvrpPkts_Type()
)
es2126GvrpCounterTxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterTxTotalGvrpPkts.setStatus("current")
_Es2126GvrpCounterTxLeaveAllMsg_Type = Counter32
_Es2126GvrpCounterTxLeaveAllMsg_Object = MibTableColumn
es2126GvrpCounterTxLeaveAllMsg = _Es2126GvrpCounterTxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 10),
    _Es2126GvrpCounterTxLeaveAllMsg_Type()
)
es2126GvrpCounterTxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterTxLeaveAllMsg.setStatus("current")
_Es2126GvrpCounterTxJoinEmptyMsg_Type = Counter32
_Es2126GvrpCounterTxJoinEmptyMsg_Object = MibTableColumn
es2126GvrpCounterTxJoinEmptyMsg = _Es2126GvrpCounterTxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 11),
    _Es2126GvrpCounterTxJoinEmptyMsg_Type()
)
es2126GvrpCounterTxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterTxJoinEmptyMsg.setStatus("current")
_Es2126GvrpCounterTxJoinInMsg_Type = Counter32
_Es2126GvrpCounterTxJoinInMsg_Object = MibTableColumn
es2126GvrpCounterTxJoinInMsg = _Es2126GvrpCounterTxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 12),
    _Es2126GvrpCounterTxJoinInMsg_Type()
)
es2126GvrpCounterTxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterTxJoinInMsg.setStatus("current")
_Es2126GvrpCounterTxLeaveEmptyMsg_Type = Counter32
_Es2126GvrpCounterTxLeaveEmptyMsg_Object = MibTableColumn
es2126GvrpCounterTxLeaveEmptyMsg = _Es2126GvrpCounterTxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 13),
    _Es2126GvrpCounterTxLeaveEmptyMsg_Type()
)
es2126GvrpCounterTxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterTxLeaveEmptyMsg.setStatus("current")
_Es2126GvrpCounterTxEmptyMsg_Type = Counter32
_Es2126GvrpCounterTxEmptyMsg_Object = MibTableColumn
es2126GvrpCounterTxEmptyMsg = _Es2126GvrpCounterTxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 2, 1, 1, 14),
    _Es2126GvrpCounterTxEmptyMsg_Type()
)
es2126GvrpCounterTxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpCounterTxEmptyMsg.setStatus("current")
_Es2126GvrpGroup_ObjectIdentity = ObjectIdentity
es2126GvrpGroup = _Es2126GvrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3)
)


class _Es2126GvrpGroupNumber_Type(Integer32):
    """Custom type es2126GvrpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126GvrpGroupNumber_Type.__name__ = "Integer32"
_Es2126GvrpGroupNumber_Object = MibScalar
es2126GvrpGroupNumber = _Es2126GvrpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3, 1),
    _Es2126GvrpGroupNumber_Type()
)
es2126GvrpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpGroupNumber.setStatus("current")
_Es2126GvrpGroupTable_Object = MibTable
es2126GvrpGroupTable = _Es2126GvrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    es2126GvrpGroupTable.setStatus("current")
_Es2126GvrpGroupEntry_Object = MibTableRow
es2126GvrpGroupEntry = _Es2126GvrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3, 2, 1)
)
es2126GvrpGroupEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126GvrpGroupId"),
)
if mibBuilder.loadTexts:
    es2126GvrpGroupEntry.setStatus("current")


class _Es2126GvrpGroupId_Type(Integer32):
    """Custom type es2126GvrpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126GvrpGroupId_Type.__name__ = "Integer32"
_Es2126GvrpGroupId_Object = MibTableColumn
es2126GvrpGroupId = _Es2126GvrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3, 2, 1, 1),
    _Es2126GvrpGroupId_Type()
)
es2126GvrpGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpGroupId.setStatus("current")


class _Es2126GvrpGroupVid_Type(Integer32):
    """Custom type es2126GvrpGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126GvrpGroupVid_Type.__name__ = "Integer32"
_Es2126GvrpGroupVid_Object = MibTableColumn
es2126GvrpGroupVid = _Es2126GvrpGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3, 2, 1, 2),
    _Es2126GvrpGroupVid_Type()
)
es2126GvrpGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpGroupVid.setStatus("current")
_Es2126GvrpGroupMemberPort_Type = DisplayString
_Es2126GvrpGroupMemberPort_Object = MibTableColumn
es2126GvrpGroupMemberPort = _Es2126GvrpGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 12, 3, 2, 1, 3),
    _Es2126GvrpGroupMemberPort_Type()
)
es2126GvrpGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126GvrpGroupMemberPort.setStatus("current")
_Es2126Security_ObjectIdentity = ObjectIdentity
es2126Security = _Es2126Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13)
)
_Es2126IsolatedPortGroup_Type = DisplayString
_Es2126IsolatedPortGroup_Object = MibScalar
es2126IsolatedPortGroup = _Es2126IsolatedPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13, 1),
    _Es2126IsolatedPortGroup_Type()
)
es2126IsolatedPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126IsolatedPortGroup.setStatus("current")
_Es2126Mirror_ObjectIdentity = ObjectIdentity
es2126Mirror = _Es2126Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13, 2)
)


class _Es2126MirrorMode_Type(Integer32):
    """Custom type es2126MirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126MirrorMode_Type.__name__ = "Integer32"
_Es2126MirrorMode_Object = MibScalar
es2126MirrorMode = _Es2126MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13, 2, 1),
    _Es2126MirrorMode_Type()
)
es2126MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MirrorMode.setStatus("current")


class _Es2126MonitoringPort_Type(Integer32):
    """Custom type es2126MonitoringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126MonitoringPort_Type.__name__ = "Integer32"
_Es2126MonitoringPort_Object = MibScalar
es2126MonitoringPort = _Es2126MonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13, 2, 2),
    _Es2126MonitoringPort_Type()
)
es2126MonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MonitoringPort.setStatus("current")
_Es2126MonitoredIngressPort_Type = DisplayString
_Es2126MonitoredIngressPort_Object = MibScalar
es2126MonitoredIngressPort = _Es2126MonitoredIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13, 2, 3),
    _Es2126MonitoredIngressPort_Type()
)
es2126MonitoredIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MonitoredIngressPort.setStatus("current")
_Es2126MonitoredEgressPort_Type = DisplayString
_Es2126MonitoredEgressPort_Object = MibScalar
es2126MonitoredEgressPort = _Es2126MonitoredEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 13, 2, 4),
    _Es2126MonitoredEgressPort_Type()
)
es2126MonitoredEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126MonitoredEgressPort.setStatus("current")
_Es2126VirtualStack_ObjectIdentity = ObjectIdentity
es2126VirtualStack = _Es2126VirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 14)
)


class _Es2126VirtualStackState_Type(Integer32):
    """Custom type es2126VirtualStackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126VirtualStackState_Type.__name__ = "Integer32"
_Es2126VirtualStackState_Object = MibScalar
es2126VirtualStackState = _Es2126VirtualStackState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 14, 1),
    _Es2126VirtualStackState_Type()
)
es2126VirtualStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VirtualStackState.setStatus("current")


class _Es2126VirtualStackRole_Type(Integer32):
    """Custom type es2126VirtualStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126VirtualStackRole_Type.__name__ = "Integer32"
_Es2126VirtualStackRole_Object = MibScalar
es2126VirtualStackRole = _Es2126VirtualStackRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 14, 2),
    _Es2126VirtualStackRole_Type()
)
es2126VirtualStackRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VirtualStackRole.setStatus("current")
_Es2126VirtualStackGroupID_Type = DisplayString
_Es2126VirtualStackGroupID_Object = MibScalar
es2126VirtualStackGroupID = _Es2126VirtualStackGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 14, 3),
    _Es2126VirtualStackGroupID_Type()
)
es2126VirtualStackGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VirtualStackGroupID.setStatus("current")
_Es2126ManagementSecurity_ObjectIdentity = ObjectIdentity
es2126ManagementSecurity = _Es2126ManagementSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15)
)


class _Es2126ManagementSecurityNumber_Type(Integer32):
    """Custom type es2126ManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2126ManagementSecurityNumber_Type.__name__ = "Integer32"
_Es2126ManagementSecurityNumber_Object = MibScalar
es2126ManagementSecurityNumber = _Es2126ManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 1),
    _Es2126ManagementSecurityNumber_Type()
)
es2126ManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126ManagementSecurityNumber.setStatus("current")


class _Es2126ManagementSecurityEntryCreate_Type(Integer32):
    """Custom type es2126ManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2126ManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Es2126ManagementSecurityEntryCreate_Object = MibScalar
es2126ManagementSecurityEntryCreate = _Es2126ManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 2),
    _Es2126ManagementSecurityEntryCreate_Type()
)
es2126ManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityEntryCreate.setStatus("current")
_Es2126ManagementSecurityTable_Object = MibTable
es2126ManagementSecurityTable = _Es2126ManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3)
)
if mibBuilder.loadTexts:
    es2126ManagementSecurityTable.setStatus("current")
_Es2126ManagementSecurityEntry_Object = MibTableRow
es2126ManagementSecurityEntry = _Es2126ManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1)
)
es2126ManagementSecurityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126ManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    es2126ManagementSecurityEntry.setStatus("current")


class _Es2126ManagementSecurityIndex_Type(Integer32):
    """Custom type es2126ManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2126ManagementSecurityIndex_Type.__name__ = "Integer32"
_Es2126ManagementSecurityIndex_Object = MibTableColumn
es2126ManagementSecurityIndex = _Es2126ManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 1),
    _Es2126ManagementSecurityIndex_Type()
)
es2126ManagementSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126ManagementSecurityIndex.setStatus("current")
_Es2126ManagementSecurityName_Type = DisplayString
_Es2126ManagementSecurityName_Object = MibTableColumn
es2126ManagementSecurityName = _Es2126ManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 2),
    _Es2126ManagementSecurityName_Type()
)
es2126ManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityName.setStatus("current")


class _Es2126ManagementSecurityVid_Type(Integer32):
    """Custom type es2126ManagementSecurityVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126ManagementSecurityVid_Type.__name__ = "Integer32"
_Es2126ManagementSecurityVid_Object = MibTableColumn
es2126ManagementSecurityVid = _Es2126ManagementSecurityVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 3),
    _Es2126ManagementSecurityVid_Type()
)
es2126ManagementSecurityVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityVid.setStatus("current")
_Es2126ManagementSecurityIpRange_Type = DisplayString
_Es2126ManagementSecurityIpRange_Object = MibTableColumn
es2126ManagementSecurityIpRange = _Es2126ManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 4),
    _Es2126ManagementSecurityIpRange_Type()
)
es2126ManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityIpRange.setStatus("current")
_Es2126ManagementSecurityIncomigPort_Type = DisplayString
_Es2126ManagementSecurityIncomigPort_Object = MibTableColumn
es2126ManagementSecurityIncomigPort = _Es2126ManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 5),
    _Es2126ManagementSecurityIncomigPort_Type()
)
es2126ManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityIncomigPort.setStatus("current")
_Es2126ManagementSecurityAccessType_Type = DisplayString
_Es2126ManagementSecurityAccessType_Object = MibTableColumn
es2126ManagementSecurityAccessType = _Es2126ManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 6),
    _Es2126ManagementSecurityAccessType_Type()
)
es2126ManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityAccessType.setStatus("current")


class _Es2126ManagementSecurityAction_Type(Integer32):
    """Custom type es2126ManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126ManagementSecurityAction_Type.__name__ = "Integer32"
_Es2126ManagementSecurityAction_Object = MibTableColumn
es2126ManagementSecurityAction = _Es2126ManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 7),
    _Es2126ManagementSecurityAction_Type()
)
es2126ManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityAction.setStatus("current")


class _Es2126ManagementSecurityEntryAction_Type(Integer32):
    """Custom type es2126ManagementSecurityEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126ManagementSecurityEntryAction_Type.__name__ = "Integer32"
_Es2126ManagementSecurityEntryAction_Object = MibTableColumn
es2126ManagementSecurityEntryAction = _Es2126ManagementSecurityEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 15, 3, 1, 8),
    _Es2126ManagementSecurityEntryAction_Type()
)
es2126ManagementSecurityEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementSecurityEntryAction.setStatus("current")
_Es2126QoS_ObjectIdentity = ObjectIdentity
es2126QoS = _Es2126QoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16)
)
_Es2126QoSGlobalConfig_ObjectIdentity = ObjectIdentity
es2126QoSGlobalConfig = _Es2126QoSGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1)
)


class _Es2126QoSMode_Type(Integer32):
    """Custom type es2126QoSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126QoSMode_Type.__name__ = "Integer32"
_Es2126QoSMode_Object = MibScalar
es2126QoSMode = _Es2126QoSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 1),
    _Es2126QoSMode_Type()
)
es2126QoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSMode.setStatus("current")


class _Es2126QosPriorityControl1p_Type(Integer32):
    """Custom type es2126QosPriorityControl1p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126QosPriorityControl1p_Type.__name__ = "Integer32"
_Es2126QosPriorityControl1p_Object = MibScalar
es2126QosPriorityControl1p = _Es2126QosPriorityControl1p_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 2),
    _Es2126QosPriorityControl1p_Type()
)
es2126QosPriorityControl1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QosPriorityControl1p.setStatus("current")


class _Es2126QosPriorityControlTOS_Type(Integer32):
    """Custom type es2126QosPriorityControlTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126QosPriorityControlTOS_Type.__name__ = "Integer32"
_Es2126QosPriorityControlTOS_Object = MibScalar
es2126QosPriorityControlTOS = _Es2126QosPriorityControlTOS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 3),
    _Es2126QosPriorityControlTOS_Type()
)
es2126QosPriorityControlTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QosPriorityControlTOS.setStatus("current")


class _Es2126QosPriorityControlDSCP_Type(Integer32):
    """Custom type es2126QosPriorityControlDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126QosPriorityControlDSCP_Type.__name__ = "Integer32"
_Es2126QosPriorityControlDSCP_Object = MibScalar
es2126QosPriorityControlDSCP = _Es2126QosPriorityControlDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 4),
    _Es2126QosPriorityControlDSCP_Type()
)
es2126QosPriorityControlDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QosPriorityControlDSCP.setStatus("current")


class _Es2126QoSSchedulingMethod_Type(Integer32):
    """Custom type es2126QoSSchedulingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126QoSSchedulingMethod_Type.__name__ = "Integer32"
_Es2126QoSSchedulingMethod_Object = MibScalar
es2126QoSSchedulingMethod = _Es2126QoSSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 5),
    _Es2126QoSSchedulingMethod_Type()
)
es2126QoSSchedulingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSSchedulingMethod.setStatus("current")


class _Es2126QoSWeightQ0_Type(Integer32):
    """Custom type es2126QoSWeightQ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126QoSWeightQ0_Type.__name__ = "Integer32"
_Es2126QoSWeightQ0_Object = MibScalar
es2126QoSWeightQ0 = _Es2126QoSWeightQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 6),
    _Es2126QoSWeightQ0_Type()
)
es2126QoSWeightQ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSWeightQ0.setStatus("current")


class _Es2126QoSWeightQ1_Type(Integer32):
    """Custom type es2126QoSWeightQ1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126QoSWeightQ1_Type.__name__ = "Integer32"
_Es2126QoSWeightQ1_Object = MibScalar
es2126QoSWeightQ1 = _Es2126QoSWeightQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 7),
    _Es2126QoSWeightQ1_Type()
)
es2126QoSWeightQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSWeightQ1.setStatus("current")


class _Es2126QoSWeightQ2_Type(Integer32):
    """Custom type es2126QoSWeightQ2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126QoSWeightQ2_Type.__name__ = "Integer32"
_Es2126QoSWeightQ2_Object = MibScalar
es2126QoSWeightQ2 = _Es2126QoSWeightQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 8),
    _Es2126QoSWeightQ2_Type()
)
es2126QoSWeightQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSWeightQ2.setStatus("current")


class _Es2126QoSWeightQ3_Type(Integer32):
    """Custom type es2126QoSWeightQ3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126QoSWeightQ3_Type.__name__ = "Integer32"
_Es2126QoSWeightQ3_Object = MibScalar
es2126QoSWeightQ3 = _Es2126QoSWeightQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 1, 9),
    _Es2126QoSWeightQ3_Type()
)
es2126QoSWeightQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSWeightQ3.setStatus("current")
_Es2126QoSVIPPort_Type = DisplayString
_Es2126QoSVIPPort_Object = MibScalar
es2126QoSVIPPort = _Es2126QoSVIPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 2),
    _Es2126QoSVIPPort_Type()
)
es2126QoSVIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSVIPPort.setStatus("current")
_Es2126QoS1pPriority_ObjectIdentity = ObjectIdentity
es2126QoS1pPriority = _Es2126QoS1pPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 3)
)
_Es2126QoS1pPriorityTable_Object = MibTable
es2126QoS1pPriorityTable = _Es2126QoS1pPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    es2126QoS1pPriorityTable.setStatus("current")
_Es2126QoS1pPriorityEntry_Object = MibTableRow
es2126QoS1pPriorityEntry = _Es2126QoS1pPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 3, 1, 1)
)
es2126QoS1pPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126QoS1pPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126QoS1pPriorityEntry.setStatus("current")


class _Es2126QoS1pPriorityIndex_Type(Integer32):
    """Custom type es2126QoS1pPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126QoS1pPriorityIndex_Type.__name__ = "Integer32"
_Es2126QoS1pPriorityIndex_Object = MibTableColumn
es2126QoS1pPriorityIndex = _Es2126QoS1pPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 3, 1, 1, 1),
    _Es2126QoS1pPriorityIndex_Type()
)
es2126QoS1pPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126QoS1pPriorityIndex.setStatus("current")


class _Es2126QoS1pPriorityValue_Type(Integer32):
    """Custom type es2126QoS1pPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126QoS1pPriorityValue_Type.__name__ = "Integer32"
_Es2126QoS1pPriorityValue_Object = MibTableColumn
es2126QoS1pPriorityValue = _Es2126QoS1pPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 3, 1, 1, 2),
    _Es2126QoS1pPriorityValue_Type()
)
es2126QoS1pPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126QoS1pPriorityValue.setStatus("current")


class _Es2126QoS1pPriorityQueue_Type(Integer32):
    """Custom type es2126QoS1pPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126QoS1pPriorityQueue_Type.__name__ = "Integer32"
_Es2126QoS1pPriorityQueue_Object = MibTableColumn
es2126QoS1pPriorityQueue = _Es2126QoS1pPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 3, 1, 1, 3),
    _Es2126QoS1pPriorityQueue_Type()
)
es2126QoS1pPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoS1pPriorityQueue.setStatus("current")
_Es2126QoSDTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126QoSDTypeTOSPriority = _Es2126QoSDTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 4)
)
_Es2126QoSDTypeTOSPriorityTable_Object = MibTable
es2126QoSDTypeTOSPriorityTable = _Es2126QoSDTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    es2126QoSDTypeTOSPriorityTable.setStatus("current")
_Es2126QoSDTypeTOSPriorityEntry_Object = MibTableRow
es2126QoSDTypeTOSPriorityEntry = _Es2126QoSDTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 4, 1, 1)
)
es2126QoSDTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126QoSDTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126QoSDTypeTOSPriorityEntry.setStatus("current")


class _Es2126QoSDTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126QoSDTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126QoSDTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126QoSDTypeTOSPriorityIndex_Object = MibTableColumn
es2126QoSDTypeTOSPriorityIndex = _Es2126QoSDTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 4, 1, 1, 1),
    _Es2126QoSDTypeTOSPriorityIndex_Type()
)
es2126QoSDTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126QoSDTypeTOSPriorityIndex.setStatus("current")


class _Es2126QoSDTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126QoSDTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126QoSDTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126QoSDTypeTOSPriorityValue_Object = MibTableColumn
es2126QoSDTypeTOSPriorityValue = _Es2126QoSDTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 4, 1, 1, 2),
    _Es2126QoSDTypeTOSPriorityValue_Type()
)
es2126QoSDTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126QoSDTypeTOSPriorityValue.setStatus("current")


class _Es2126QoSDTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126QoSDTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126QoSDTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126QoSDTypeTOSPriorityQueue_Object = MibTableColumn
es2126QoSDTypeTOSPriorityQueue = _Es2126QoSDTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 4, 1, 1, 3),
    _Es2126QoSDTypeTOSPriorityQueue_Type()
)
es2126QoSDTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSDTypeTOSPriorityQueue.setStatus("current")
_Es2126QoSTTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126QoSTTypeTOSPriority = _Es2126QoSTTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 5)
)
_Es2126QoSTTypeTOSPriorityTable_Object = MibTable
es2126QoSTTypeTOSPriorityTable = _Es2126QoSTTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    es2126QoSTTypeTOSPriorityTable.setStatus("current")
_Es2126QoSTTypeTOSPriorityEntry_Object = MibTableRow
es2126QoSTTypeTOSPriorityEntry = _Es2126QoSTTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 5, 1, 1)
)
es2126QoSTTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126QoSTTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126QoSTTypeTOSPriorityEntry.setStatus("current")


class _Es2126QoSTTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126QoSTTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126QoSTTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126QoSTTypeTOSPriorityIndex_Object = MibTableColumn
es2126QoSTTypeTOSPriorityIndex = _Es2126QoSTTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 5, 1, 1, 1),
    _Es2126QoSTTypeTOSPriorityIndex_Type()
)
es2126QoSTTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126QoSTTypeTOSPriorityIndex.setStatus("current")


class _Es2126QoSTTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126QoSTTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126QoSTTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126QoSTTypeTOSPriorityValue_Object = MibTableColumn
es2126QoSTTypeTOSPriorityValue = _Es2126QoSTTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 5, 1, 1, 2),
    _Es2126QoSTTypeTOSPriorityValue_Type()
)
es2126QoSTTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126QoSTTypeTOSPriorityValue.setStatus("current")


class _Es2126QoSTTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126QoSTTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126QoSTTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126QoSTTypeTOSPriorityQueue_Object = MibTableColumn
es2126QoSTTypeTOSPriorityQueue = _Es2126QoSTTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 5, 1, 1, 3),
    _Es2126QoSTTypeTOSPriorityQueue_Type()
)
es2126QoSTTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSTTypeTOSPriorityQueue.setStatus("current")
_Es2126QoSRTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126QoSRTypeTOSPriority = _Es2126QoSRTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 6)
)
_Es2126QoSRTypeTOSPriorityTable_Object = MibTable
es2126QoSRTypeTOSPriorityTable = _Es2126QoSRTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 6, 1)
)
if mibBuilder.loadTexts:
    es2126QoSRTypeTOSPriorityTable.setStatus("current")
_Es2126QoSRTypeTOSPriorityEntry_Object = MibTableRow
es2126QoSRTypeTOSPriorityEntry = _Es2126QoSRTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 6, 1, 1)
)
es2126QoSRTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126QoSRTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126QoSRTypeTOSPriorityEntry.setStatus("current")


class _Es2126QoSRTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126QoSRTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126QoSRTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126QoSRTypeTOSPriorityIndex_Object = MibTableColumn
es2126QoSRTypeTOSPriorityIndex = _Es2126QoSRTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 6, 1, 1, 1),
    _Es2126QoSRTypeTOSPriorityIndex_Type()
)
es2126QoSRTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126QoSRTypeTOSPriorityIndex.setStatus("current")


class _Es2126QoSRTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126QoSRTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126QoSRTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126QoSRTypeTOSPriorityValue_Object = MibTableColumn
es2126QoSRTypeTOSPriorityValue = _Es2126QoSRTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 6, 1, 1, 2),
    _Es2126QoSRTypeTOSPriorityValue_Type()
)
es2126QoSRTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126QoSRTypeTOSPriorityValue.setStatus("current")


class _Es2126QoSRTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126QoSRTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126QoSRTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126QoSRTypeTOSPriorityQueue_Object = MibTableColumn
es2126QoSRTypeTOSPriorityQueue = _Es2126QoSRTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 6, 1, 1, 3),
    _Es2126QoSRTypeTOSPriorityQueue_Type()
)
es2126QoSRTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSRTypeTOSPriorityQueue.setStatus("current")
_Es2126QoSMTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126QoSMTypeTOSPriority = _Es2126QoSMTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 7)
)
_Es2126QoSMTypeTOSPriorityTable_Object = MibTable
es2126QoSMTypeTOSPriorityTable = _Es2126QoSMTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 7, 1)
)
if mibBuilder.loadTexts:
    es2126QoSMTypeTOSPriorityTable.setStatus("current")
_Es2126QoSMTypeTOSPriorityEntry_Object = MibTableRow
es2126QoSMTypeTOSPriorityEntry = _Es2126QoSMTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 7, 1, 1)
)
es2126QoSMTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126QoSMTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126QoSMTypeTOSPriorityEntry.setStatus("current")


class _Es2126QoSMTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126QoSMTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126QoSMTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126QoSMTypeTOSPriorityIndex_Object = MibTableColumn
es2126QoSMTypeTOSPriorityIndex = _Es2126QoSMTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 7, 1, 1, 1),
    _Es2126QoSMTypeTOSPriorityIndex_Type()
)
es2126QoSMTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126QoSMTypeTOSPriorityIndex.setStatus("current")


class _Es2126QoSMTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126QoSMTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126QoSMTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126QoSMTypeTOSPriorityValue_Object = MibTableColumn
es2126QoSMTypeTOSPriorityValue = _Es2126QoSMTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 7, 1, 1, 2),
    _Es2126QoSMTypeTOSPriorityValue_Type()
)
es2126QoSMTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126QoSMTypeTOSPriorityValue.setStatus("current")


class _Es2126QoSMTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126QoSMTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126QoSMTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126QoSMTypeTOSPriorityQueue_Object = MibTableColumn
es2126QoSMTypeTOSPriorityQueue = _Es2126QoSMTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 7, 1, 1, 3),
    _Es2126QoSMTypeTOSPriorityQueue_Type()
)
es2126QoSMTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSMTypeTOSPriorityQueue.setStatus("current")
_Es2126QoSDSCPPriority_ObjectIdentity = ObjectIdentity
es2126QoSDSCPPriority = _Es2126QoSDSCPPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 8)
)
_Es2126QoSDSCPPriorityTable_Object = MibTable
es2126QoSDSCPPriorityTable = _Es2126QoSDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 8, 1)
)
if mibBuilder.loadTexts:
    es2126QoSDSCPPriorityTable.setStatus("current")
_Es2126QoSDSCPPriorityEntry_Object = MibTableRow
es2126QoSDSCPPriorityEntry = _Es2126QoSDSCPPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 8, 1, 1)
)
es2126QoSDSCPPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126QoSDSCPPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126QoSDSCPPriorityEntry.setStatus("current")


class _Es2126QoSDSCPPriorityIndex_Type(Integer32):
    """Custom type es2126QoSDSCPPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2126QoSDSCPPriorityIndex_Type.__name__ = "Integer32"
_Es2126QoSDSCPPriorityIndex_Object = MibTableColumn
es2126QoSDSCPPriorityIndex = _Es2126QoSDSCPPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 8, 1, 1, 1),
    _Es2126QoSDSCPPriorityIndex_Type()
)
es2126QoSDSCPPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126QoSDSCPPriorityIndex.setStatus("current")


class _Es2126QoSDSCPPriorityValue_Type(Integer32):
    """Custom type es2126QoSDSCPPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2126QoSDSCPPriorityValue_Type.__name__ = "Integer32"
_Es2126QoSDSCPPriorityValue_Object = MibTableColumn
es2126QoSDSCPPriorityValue = _Es2126QoSDSCPPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 8, 1, 1, 2),
    _Es2126QoSDSCPPriorityValue_Type()
)
es2126QoSDSCPPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126QoSDSCPPriorityValue.setStatus("current")


class _Es2126QoSDSCPPriorityQueue_Type(Integer32):
    """Custom type es2126QoSDSCPPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126QoSDSCPPriorityQueue_Type.__name__ = "Integer32"
_Es2126QoSDSCPPriorityQueue_Object = MibTableColumn
es2126QoSDSCPPriorityQueue = _Es2126QoSDSCPPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 16, 8, 1, 1, 3),
    _Es2126QoSDSCPPriorityQueue_Type()
)
es2126QoSDSCPPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126QoSDSCPPriorityQueue.setStatus("current")
_Es2126Vlan_ObjectIdentity = ObjectIdentity
es2126Vlan = _Es2126Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17)
)
_Es2126VlanModeConfig_ObjectIdentity = ObjectIdentity
es2126VlanModeConfig = _Es2126VlanModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 1)
)


class _Es2126VlanMode_Type(Integer32):
    """Custom type es2126VlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126VlanMode_Type.__name__ = "Integer32"
_Es2126VlanMode_Object = MibScalar
es2126VlanMode = _Es2126VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 1, 1),
    _Es2126VlanMode_Type()
)
es2126VlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VlanMode.setStatus("current")


class _Es2126SymmetricVlan_Type(Integer32):
    """Custom type es2126SymmetricVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126SymmetricVlan_Type.__name__ = "Integer32"
_Es2126SymmetricVlan_Object = MibScalar
es2126SymmetricVlan = _Es2126SymmetricVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 1, 2),
    _Es2126SymmetricVlan_Type()
)
es2126SymmetricVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126SymmetricVlan.setStatus("current")


class _Es2126VlanSVL_Type(Integer32):
    """Custom type es2126VlanSVL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126VlanSVL_Type.__name__ = "Integer32"
_Es2126VlanSVL_Object = MibScalar
es2126VlanSVL = _Es2126VlanSVL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 1, 3),
    _Es2126VlanSVL_Type()
)
es2126VlanSVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VlanSVL.setStatus("current")


class _Es2126DoubleTag_Type(Integer32):
    """Custom type es2126DoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126DoubleTag_Type.__name__ = "Integer32"
_Es2126DoubleTag_Object = MibScalar
es2126DoubleTag = _Es2126DoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 1, 4),
    _Es2126DoubleTag_Type()
)
es2126DoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126DoubleTag.setStatus("current")


class _Es2126UpLinkPort_Type(Integer32):
    """Custom type es2126UpLinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126UpLinkPort_Type.__name__ = "Integer32"
_Es2126UpLinkPort_Object = MibScalar
es2126UpLinkPort = _Es2126UpLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 1, 5),
    _Es2126UpLinkPort_Type()
)
es2126UpLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126UpLinkPort.setStatus("current")
_Es2126TagBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2126TagBasedVlanGroup = _Es2126TagBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2)
)


class _Es2126TagBasedVlanNumbers_Type(Integer32):
    """Custom type es2126TagBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126TagBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2126TagBasedVlanNumbers_Object = MibScalar
es2126TagBasedVlanNumbers = _Es2126TagBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 1),
    _Es2126TagBasedVlanNumbers_Type()
)
es2126TagBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126TagBasedVlanNumbers.setStatus("current")


class _Es2126TagBasedCreateStatus_Type(Integer32):
    """Custom type es2126TagBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126TagBasedCreateStatus_Type.__name__ = "Integer32"
_Es2126TagBasedCreateStatus_Object = MibScalar
es2126TagBasedCreateStatus = _Es2126TagBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 2),
    _Es2126TagBasedCreateStatus_Type()
)
es2126TagBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TagBasedCreateStatus.setStatus("current")
_Es2126TagBasedVlanTable_Object = MibTable
es2126TagBasedVlanTable = _Es2126TagBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3)
)
if mibBuilder.loadTexts:
    es2126TagBasedVlanTable.setStatus("current")
_Es2126TagBasedVlanEntry_Object = MibTableRow
es2126TagBasedVlanEntry = _Es2126TagBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3, 1)
)
es2126TagBasedVlanEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126TagBasedVlanVid"),
)
if mibBuilder.loadTexts:
    es2126TagBasedVlanEntry.setStatus("current")


class _Es2126TagBasedVlanVid_Type(Integer32):
    """Custom type es2126TagBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126TagBasedVlanVid_Type.__name__ = "Integer32"
_Es2126TagBasedVlanVid_Object = MibTableColumn
es2126TagBasedVlanVid = _Es2126TagBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3, 1, 1),
    _Es2126TagBasedVlanVid_Type()
)
es2126TagBasedVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126TagBasedVlanVid.setStatus("current")
_Es2126TagBasedVlanName_Type = DisplayString
_Es2126TagBasedVlanName_Object = MibTableColumn
es2126TagBasedVlanName = _Es2126TagBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3, 1, 2),
    _Es2126TagBasedVlanName_Type()
)
es2126TagBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TagBasedVlanName.setStatus("current")
_Es2126TagBasedVlanMember_Type = DisplayString
_Es2126TagBasedVlanMember_Object = MibTableColumn
es2126TagBasedVlanMember = _Es2126TagBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3, 1, 3),
    _Es2126TagBasedVlanMember_Type()
)
es2126TagBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TagBasedVlanMember.setStatus("current")
_Es2126TagBasedVlanUntag_Type = DisplayString
_Es2126TagBasedVlanUntag_Object = MibTableColumn
es2126TagBasedVlanUntag = _Es2126TagBasedVlanUntag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3, 1, 4),
    _Es2126TagBasedVlanUntag_Type()
)
es2126TagBasedVlanUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TagBasedVlanUntag.setStatus("current")


class _Es2126TagBasedVlanRowStatus_Type(Integer32):
    """Custom type es2126TagBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126TagBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2126TagBasedVlanRowStatus_Object = MibTableColumn
es2126TagBasedVlanRowStatus = _Es2126TagBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 2, 3, 1, 5),
    _Es2126TagBasedVlanRowStatus_Type()
)
es2126TagBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TagBasedVlanRowStatus.setStatus("current")
_Es2126VlanPvid_ObjectIdentity = ObjectIdentity
es2126VlanPvid = _Es2126VlanPvid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3)
)
_Es2126VlanPvidTable_Object = MibTable
es2126VlanPvidTable = _Es2126VlanPvidTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    es2126VlanPvidTable.setStatus("current")
_Es2126VlanPvidEntry_Object = MibTableRow
es2126VlanPvidEntry = _Es2126VlanPvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3, 1, 1)
)
es2126VlanPvidEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126VlanPvidPort"),
)
if mibBuilder.loadTexts:
    es2126VlanPvidEntry.setStatus("current")


class _Es2126VlanPvidPort_Type(Integer32):
    """Custom type es2126VlanPvidPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126VlanPvidPort_Type.__name__ = "Integer32"
_Es2126VlanPvidPort_Object = MibTableColumn
es2126VlanPvidPort = _Es2126VlanPvidPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3, 1, 1, 1),
    _Es2126VlanPvidPort_Type()
)
es2126VlanPvidPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126VlanPvidPort.setStatus("current")


class _Es2126VlanPvidValue_Type(Integer32):
    """Custom type es2126VlanPvidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126VlanPvidValue_Type.__name__ = "Integer32"
_Es2126VlanPvidValue_Object = MibTableColumn
es2126VlanPvidValue = _Es2126VlanPvidValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3, 1, 1, 2),
    _Es2126VlanPvidValue_Type()
)
es2126VlanPvidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VlanPvidValue.setStatus("current")


class _Es2126VlanPvidDefaultPriority_Type(Integer32):
    """Custom type es2126VlanPvidDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126VlanPvidDefaultPriority_Type.__name__ = "Integer32"
_Es2126VlanPvidDefaultPriority_Object = MibTableColumn
es2126VlanPvidDefaultPriority = _Es2126VlanPvidDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3, 1, 1, 3),
    _Es2126VlanPvidDefaultPriority_Type()
)
es2126VlanPvidDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VlanPvidDefaultPriority.setStatus("current")


class _Es2126VlanPvidDropUntag_Type(Integer32):
    """Custom type es2126VlanPvidDropUntag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126VlanPvidDropUntag_Type.__name__ = "Integer32"
_Es2126VlanPvidDropUntag_Object = MibTableColumn
es2126VlanPvidDropUntag = _Es2126VlanPvidDropUntag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 3, 1, 1, 4),
    _Es2126VlanPvidDropUntag_Type()
)
es2126VlanPvidDropUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126VlanPvidDropUntag.setStatus("current")
_Es2126PortBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2126PortBasedVlanGroup = _Es2126PortBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4)
)


class _Es2126PortBasedVlanNumbers_Type(Integer32):
    """Custom type es2126PortBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PortBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2126PortBasedVlanNumbers_Object = MibScalar
es2126PortBasedVlanNumbers = _Es2126PortBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 1),
    _Es2126PortBasedVlanNumbers_Type()
)
es2126PortBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PortBasedVlanNumbers.setStatus("current")


class _Es2126PortBasedCreateStatus_Type(Integer32):
    """Custom type es2126PortBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PortBasedCreateStatus_Type.__name__ = "Integer32"
_Es2126PortBasedCreateStatus_Object = MibScalar
es2126PortBasedCreateStatus = _Es2126PortBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 2),
    _Es2126PortBasedCreateStatus_Type()
)
es2126PortBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBasedCreateStatus.setStatus("current")
_Es2126PortBasedVlanTable_Object = MibTable
es2126PortBasedVlanTable = _Es2126PortBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 3)
)
if mibBuilder.loadTexts:
    es2126PortBasedVlanTable.setStatus("current")
_Es2126PortBasedVlanEntry_Object = MibTableRow
es2126PortBasedVlanEntry = _Es2126PortBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 3, 1)
)
es2126PortBasedVlanEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126PortBasedVlanIndex"),
)
if mibBuilder.loadTexts:
    es2126PortBasedVlanEntry.setStatus("current")


class _Es2126PortBasedVlanIndex_Type(Integer32):
    """Custom type es2126PortBasedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PortBasedVlanIndex_Type.__name__ = "Integer32"
_Es2126PortBasedVlanIndex_Object = MibTableColumn
es2126PortBasedVlanIndex = _Es2126PortBasedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 3, 1, 1),
    _Es2126PortBasedVlanIndex_Type()
)
es2126PortBasedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PortBasedVlanIndex.setStatus("current")
_Es2126PortBasedVlanName_Type = DisplayString
_Es2126PortBasedVlanName_Object = MibTableColumn
es2126PortBasedVlanName = _Es2126PortBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 3, 1, 2),
    _Es2126PortBasedVlanName_Type()
)
es2126PortBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBasedVlanName.setStatus("current")
_Es2126PortBasedVlanMember_Type = DisplayString
_Es2126PortBasedVlanMember_Object = MibTableColumn
es2126PortBasedVlanMember = _Es2126PortBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 3, 1, 3),
    _Es2126PortBasedVlanMember_Type()
)
es2126PortBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBasedVlanMember.setStatus("current")


class _Es2126PortBasedVlanRowStatus_Type(Integer32):
    """Custom type es2126PortBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126PortBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2126PortBasedVlanRowStatus_Object = MibTableColumn
es2126PortBasedVlanRowStatus = _Es2126PortBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 4, 3, 1, 4),
    _Es2126PortBasedVlanRowStatus_Type()
)
es2126PortBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PortBasedVlanRowStatus.setStatus("current")
_Es2126ManagementVlan_ObjectIdentity = ObjectIdentity
es2126ManagementVlan = _Es2126ManagementVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 5)
)


class _Es2126ManagementVlanState_Type(Integer32):
    """Custom type es2126ManagementVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126ManagementVlanState_Type.__name__ = "Integer32"
_Es2126ManagementVlanState_Object = MibScalar
es2126ManagementVlanState = _Es2126ManagementVlanState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 5, 1),
    _Es2126ManagementVlanState_Type()
)
es2126ManagementVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementVlanState.setStatus("current")


class _Es2126ManagementVlanVid_Type(Integer32):
    """Custom type es2126ManagementVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126ManagementVlanVid_Type.__name__ = "Integer32"
_Es2126ManagementVlanVid_Object = MibScalar
es2126ManagementVlanVid = _Es2126ManagementVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 17, 5, 2),
    _Es2126ManagementVlanVid_Type()
)
es2126ManagementVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126ManagementVlanVid.setStatus("current")
_Es2126Dot1X_ObjectIdentity = ObjectIdentity
es2126Dot1X = _Es2126Dot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18)
)
_Es2126Dot1XStateSetting_ObjectIdentity = ObjectIdentity
es2126Dot1XStateSetting = _Es2126Dot1XStateSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1)
)
_Es2126RadiusServer_Type = IpAddress
_Es2126RadiusServer_Object = MibScalar
es2126RadiusServer = _Es2126RadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1, 1),
    _Es2126RadiusServer_Type()
)
es2126RadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126RadiusServer.setStatus("current")


class _Es2126Dot1XPort_Type(Integer32):
    """Custom type es2126Dot1XPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126Dot1XPort_Type.__name__ = "Integer32"
_Es2126Dot1XPort_Object = MibScalar
es2126Dot1XPort = _Es2126Dot1XPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1, 2),
    _Es2126Dot1XPort_Type()
)
es2126Dot1XPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPort.setStatus("current")
_Es2126SecretKey_Type = DisplayString
_Es2126SecretKey_Object = MibScalar
es2126SecretKey = _Es2126SecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1, 3),
    _Es2126SecretKey_Type()
)
es2126SecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126SecretKey.setStatus("current")


class _Es2126AccountingService_Type(Integer32):
    """Custom type es2126AccountingService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126AccountingService_Type.__name__ = "Integer32"
_Es2126AccountingService_Object = MibScalar
es2126AccountingService = _Es2126AccountingService_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1, 4),
    _Es2126AccountingService_Type()
)
es2126AccountingService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountingService.setStatus("current")
_Es2126AccountingServer_Type = IpAddress
_Es2126AccountingServer_Object = MibScalar
es2126AccountingServer = _Es2126AccountingServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1, 5),
    _Es2126AccountingServer_Type()
)
es2126AccountingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountingServer.setStatus("current")


class _Es2126AccountingPort_Type(Integer32):
    """Custom type es2126AccountingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126AccountingPort_Type.__name__ = "Integer32"
_Es2126AccountingPort_Object = MibScalar
es2126AccountingPort = _Es2126AccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 1, 6),
    _Es2126AccountingPort_Type()
)
es2126AccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126AccountingPort.setStatus("current")
_Es2126Dot1XPortSecurityManagement_ObjectIdentity = ObjectIdentity
es2126Dot1XPortSecurityManagement = _Es2126Dot1XPortSecurityManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2)
)
_Es2126Dot1XPortSecurityTable_Object = MibTable
es2126Dot1XPortSecurityTable = _Es2126Dot1XPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityTable.setStatus("current")
_Es2126Dot1XPortSecurityEntry_Object = MibTableRow
es2126Dot1XPortSecurityEntry = _Es2126Dot1XPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1)
)
es2126Dot1XPortSecurityEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126Dot1XPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityEntry.setStatus("current")


class _Es2126Dot1XPortSecurityPortIndex_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126Dot1XPortSecurityPortIndex_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityPortIndex_Object = MibTableColumn
es2126Dot1XPortSecurityPortIndex = _Es2126Dot1XPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 1),
    _Es2126Dot1XPortSecurityPortIndex_Type()
)
es2126Dot1XPortSecurityPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityPortIndex.setStatus("current")


class _Es2126Dot1XPortSecurityMode_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126Dot1XPortSecurityMode_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityMode_Object = MibTableColumn
es2126Dot1XPortSecurityMode = _Es2126Dot1XPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 2),
    _Es2126Dot1XPortSecurityMode_Type()
)
es2126Dot1XPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityMode.setStatus("current")


class _Es2126Dot1XPortSecurityPortControl_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126Dot1XPortSecurityPortControl_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityPortControl_Object = MibTableColumn
es2126Dot1XPortSecurityPortControl = _Es2126Dot1XPortSecurityPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 3),
    _Es2126Dot1XPortSecurityPortControl_Type()
)
es2126Dot1XPortSecurityPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityPortControl.setStatus("current")


class _Es2126Dot1XPortSecurityReAuthMax_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityReAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2126Dot1XPortSecurityReAuthMax_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityReAuthMax_Object = MibTableColumn
es2126Dot1XPortSecurityReAuthMax = _Es2126Dot1XPortSecurityReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 4),
    _Es2126Dot1XPortSecurityReAuthMax_Type()
)
es2126Dot1XPortSecurityReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityReAuthMax.setStatus("current")


class _Es2126Dot1XPortSecurityTxPeriod_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126Dot1XPortSecurityTxPeriod_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityTxPeriod_Object = MibTableColumn
es2126Dot1XPortSecurityTxPeriod = _Es2126Dot1XPortSecurityTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 5),
    _Es2126Dot1XPortSecurityTxPeriod_Type()
)
es2126Dot1XPortSecurityTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityTxPeriod.setStatus("current")


class _Es2126Dot1XPortSecurityQuietPeriod_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2126Dot1XPortSecurityQuietPeriod_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityQuietPeriod_Object = MibTableColumn
es2126Dot1XPortSecurityQuietPeriod = _Es2126Dot1XPortSecurityQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 6),
    _Es2126Dot1XPortSecurityQuietPeriod_Type()
)
es2126Dot1XPortSecurityQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityQuietPeriod.setStatus("current")


class _Es2126Dot1XPortSecurityReAuthEnabled_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityReAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126Dot1XPortSecurityReAuthEnabled_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityReAuthEnabled_Object = MibTableColumn
es2126Dot1XPortSecurityReAuthEnabled = _Es2126Dot1XPortSecurityReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 7),
    _Es2126Dot1XPortSecurityReAuthEnabled_Type()
)
es2126Dot1XPortSecurityReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityReAuthEnabled.setStatus("current")


class _Es2126Dot1XPortSecurityReAuthPeriod_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126Dot1XPortSecurityReAuthPeriod_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityReAuthPeriod_Object = MibTableColumn
es2126Dot1XPortSecurityReAuthPeriod = _Es2126Dot1XPortSecurityReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 8),
    _Es2126Dot1XPortSecurityReAuthPeriod_Type()
)
es2126Dot1XPortSecurityReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityReAuthPeriod.setStatus("current")


class _Es2126Dot1XPortSecurityMaxRequest_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityMaxRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2126Dot1XPortSecurityMaxRequest_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityMaxRequest_Object = MibTableColumn
es2126Dot1XPortSecurityMaxRequest = _Es2126Dot1XPortSecurityMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 9),
    _Es2126Dot1XPortSecurityMaxRequest_Type()
)
es2126Dot1XPortSecurityMaxRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityMaxRequest.setStatus("current")


class _Es2126Dot1XPortSecuritySuppTimeout_Type(Integer32):
    """Custom type es2126Dot1XPortSecuritySuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126Dot1XPortSecuritySuppTimeout_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecuritySuppTimeout_Object = MibTableColumn
es2126Dot1XPortSecuritySuppTimeout = _Es2126Dot1XPortSecuritySuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 10),
    _Es2126Dot1XPortSecuritySuppTimeout_Type()
)
es2126Dot1XPortSecuritySuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecuritySuppTimeout.setStatus("current")


class _Es2126Dot1XPortSecurityServerTimeout_Type(Integer32):
    """Custom type es2126Dot1XPortSecurityServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126Dot1XPortSecurityServerTimeout_Type.__name__ = "Integer32"
_Es2126Dot1XPortSecurityServerTimeout_Object = MibTableColumn
es2126Dot1XPortSecurityServerTimeout = _Es2126Dot1XPortSecurityServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 11),
    _Es2126Dot1XPortSecurityServerTimeout_Type()
)
es2126Dot1XPortSecurityServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityServerTimeout.setStatus("current")
_Es2126Dot1XPortSecurityStatus_Type = DisplayString
_Es2126Dot1XPortSecurityStatus_Object = MibTableColumn
es2126Dot1XPortSecurityStatus = _Es2126Dot1XPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 18, 2, 1, 1, 12),
    _Es2126Dot1XPortSecurityStatus_Type()
)
es2126Dot1XPortSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126Dot1XPortSecurityStatus.setStatus("current")
_Es2126TrunkInfo_ObjectIdentity = ObjectIdentity
es2126TrunkInfo = _Es2126TrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19)
)
_Es2126TrunkPort_ObjectIdentity = ObjectIdentity
es2126TrunkPort = _Es2126TrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1)
)
_Es2126TrunkPortTable_Object = MibTable
es2126TrunkPortTable = _Es2126TrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    es2126TrunkPortTable.setStatus("current")
_Es2126TrunkPortEntry_Object = MibTableRow
es2126TrunkPortEntry = _Es2126TrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1)
)
es2126TrunkPortEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126TrunkPortIndex"),
)
if mibBuilder.loadTexts:
    es2126TrunkPortEntry.setStatus("current")


class _Es2126TrunkPortIndex_Type(Integer32):
    """Custom type es2126TrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126TrunkPortIndex_Type.__name__ = "Integer32"
_Es2126TrunkPortIndex_Object = MibTableColumn
es2126TrunkPortIndex = _Es2126TrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 1),
    _Es2126TrunkPortIndex_Type()
)
es2126TrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126TrunkPortIndex.setStatus("current")


class _Es2126TrunkPortMethod_Type(Integer32):
    """Custom type es2126TrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126TrunkPortMethod_Type.__name__ = "Integer32"
_Es2126TrunkPortMethod_Object = MibTableColumn
es2126TrunkPortMethod = _Es2126TrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 2),
    _Es2126TrunkPortMethod_Type()
)
es2126TrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrunkPortMethod.setStatus("current")


class _Es2126TrunkPortGroup_Type(Integer32):
    """Custom type es2126TrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126TrunkPortGroup_Type.__name__ = "Integer32"
_Es2126TrunkPortGroup_Object = MibTableColumn
es2126TrunkPortGroup = _Es2126TrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 3),
    _Es2126TrunkPortGroup_Type()
)
es2126TrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrunkPortGroup.setStatus("current")


class _Es2126TrunkPortActiveLacp_Type(Integer32):
    """Custom type es2126TrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126TrunkPortActiveLacp_Type.__name__ = "Integer32"
_Es2126TrunkPortActiveLacp_Object = MibTableColumn
es2126TrunkPortActiveLacp = _Es2126TrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 4),
    _Es2126TrunkPortActiveLacp_Type()
)
es2126TrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrunkPortActiveLacp.setStatus("current")


class _Es2126TrunkPortAggtr_Type(Integer32):
    """Custom type es2126TrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126TrunkPortAggtr_Type.__name__ = "Integer32"
_Es2126TrunkPortAggtr_Object = MibTableColumn
es2126TrunkPortAggtr = _Es2126TrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 5),
    _Es2126TrunkPortAggtr_Type()
)
es2126TrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126TrunkPortAggtr.setStatus("current")


class _Es2126TrunkPortStatus_Type(Integer32):
    """Custom type es2126TrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126TrunkPortStatus_Type.__name__ = "Integer32"
_Es2126TrunkPortStatus_Object = MibTableColumn
es2126TrunkPortStatus = _Es2126TrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 6),
    _Es2126TrunkPortStatus_Type()
)
es2126TrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126TrunkPortStatus.setStatus("current")


class _Es2126TrunkPortCurrentMode_Type(Integer32):
    """Custom type es2126TrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126TrunkPortCurrentMode_Type.__name__ = "Integer32"
_Es2126TrunkPortCurrentMode_Object = MibTableColumn
es2126TrunkPortCurrentMode = _Es2126TrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 1, 1, 1, 7),
    _Es2126TrunkPortCurrentMode_Type()
)
es2126TrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126TrunkPortCurrentMode.setStatus("current")
_Es2126AggregatorView_ObjectIdentity = ObjectIdentity
es2126AggregatorView = _Es2126AggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2)
)
_Es2126AggregatorViewTable_Object = MibTable
es2126AggregatorViewTable = _Es2126AggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    es2126AggregatorViewTable.setStatus("current")
_Es2126AggregatorViewEntry_Object = MibTableRow
es2126AggregatorViewEntry = _Es2126AggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2, 1, 1)
)
es2126AggregatorViewEntry.setIndexNames(
    (0, "LANCOM-ES-2126-MIB", "es2126AggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    es2126AggregatorViewEntry.setStatus("current")


class _Es2126AggregatorViewIndex_Type(Integer32):
    """Custom type es2126AggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126AggregatorViewIndex_Type.__name__ = "Integer32"
_Es2126AggregatorViewIndex_Object = MibTableColumn
es2126AggregatorViewIndex = _Es2126AggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2, 1, 1, 1),
    _Es2126AggregatorViewIndex_Type()
)
es2126AggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126AggregatorViewIndex.setStatus("current")


class _Es2126AggregatorViewMethod_Type(Integer32):
    """Custom type es2126AggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126AggregatorViewMethod_Type.__name__ = "Integer32"
_Es2126AggregatorViewMethod_Object = MibTableColumn
es2126AggregatorViewMethod = _Es2126AggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2, 1, 1, 2),
    _Es2126AggregatorViewMethod_Type()
)
es2126AggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126AggregatorViewMethod.setStatus("current")
_Es2126AggregatorViewMemberPorts_Type = DisplayString
_Es2126AggregatorViewMemberPorts_Object = MibTableColumn
es2126AggregatorViewMemberPorts = _Es2126AggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2, 1, 1, 3),
    _Es2126AggregatorViewMemberPorts_Type()
)
es2126AggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126AggregatorViewMemberPorts.setStatus("current")
_Es2126AggregatorViewReadyPorts_Type = DisplayString
_Es2126AggregatorViewReadyPorts_Object = MibTableColumn
es2126AggregatorViewReadyPorts = _Es2126AggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 2, 1, 1, 4),
    _Es2126AggregatorViewReadyPorts_Type()
)
es2126AggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126AggregatorViewReadyPorts.setStatus("current")
_Es2126LacpSystemConfiguration_ObjectIdentity = ObjectIdentity
es2126LacpSystemConfiguration = _Es2126LacpSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 3)
)


class _Es2126LacpSystemPriority_Type(Integer32):
    """Custom type es2126LacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126LacpSystemPriority_Type.__name__ = "Integer32"
_Es2126LacpSystemPriority_Object = MibScalar
es2126LacpSystemPriority = _Es2126LacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 3, 1),
    _Es2126LacpSystemPriority_Type()
)
es2126LacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LacpSystemPriority.setStatus("current")


class _Es2126LacpSystemHashMethod_Type(Integer32):
    """Custom type es2126LacpSystemHashMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126LacpSystemHashMethod_Type.__name__ = "Integer32"
_Es2126LacpSystemHashMethod_Object = MibScalar
es2126LacpSystemHashMethod = _Es2126LacpSystemHashMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 19, 3, 2),
    _Es2126LacpSystemHashMethod_Type()
)
es2126LacpSystemHashMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LacpSystemHashMethod.setStatus("current")
_Es2126TrapEntry_ObjectIdentity = ObjectIdentity
es2126TrapEntry = _Es2126TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20)
)
_Es2126TrapVariable_ObjectIdentity = ObjectIdentity
es2126TrapVariable = _Es2126TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21, 1),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")
_LoginProtectInfo_Type = DisplayString
_LoginProtectInfo_Object = MibScalar
loginProtectInfo = _LoginProtectInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 21, 6),
    _LoginProtectInfo_Type()
)
loginProtectInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginProtectInfo.setStatus("current")
_Es2126LoginProtect_ObjectIdentity = ObjectIdentity
es2126LoginProtect = _Es2126LoginProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 22)
)


class _Es2126LockMinutes_Type(Integer32):
    """Custom type es2126LockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2126LockMinutes_Type.__name__ = "Integer32"
_Es2126LockMinutes_Object = MibScalar
es2126LockMinutes = _Es2126LockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 22, 1),
    _Es2126LockMinutes_Type()
)
es2126LockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LockMinutes.setStatus("current")


class _Es2126LoginErrors_Type(Integer32):
    """Custom type es2126LoginErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2126LoginErrors_Type.__name__ = "Integer32"
_Es2126LoginErrors_Object = MibScalar
es2126LoginErrors = _Es2126LoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 22, 2),
    _Es2126LoginErrors_Type()
)
es2126LoginErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126LoginErrors.setStatus("current")

# Managed Objects groups


# Notification objects

es2126ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 1)
)
es2126ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126ModuleInserted.setStatus(
        "current"
    )

es2126ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 2)
)
es2126ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126ModuleRemoved.setStatus(
        "current"
    )

es2126DualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 3)
)
es2126DualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126DualMediaSwapped.setStatus(
        "current"
    )

es2126LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 4)
)
es2126LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126LoopDetected.setStatus(
        "current"
    )

es2126StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 100)
)
if mibBuilder.loadTexts:
    es2126StpStateDisabled.setStatus(
        "current"
    )

es2126StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 101)
)
if mibBuilder.loadTexts:
    es2126StpStateEnabled.setStatus(
        "current"
    )

es2126StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 102)
)
es2126StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126StpTopologyChanged.setStatus(
        "current"
    )

es2126RmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 110)
)
if mibBuilder.loadTexts:
    es2126RmonRisingAlarm.setStatus(
        "current"
    )

es2126RmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 111)
)
if mibBuilder.loadTexts:
    es2126RmonFallingAlarm.setStatus(
        "current"
    )

es2126LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 120)
)
es2126LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2126LacpStateDisabled.setStatus(
        "current"
    )

es2126LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 121)
)
es2126LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2126LacpStateEnabled.setStatus(
        "current"
    )

es2126LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 123)
)
es2126LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126-MIB", "actorkey"),
        ("LANCOM-ES-2126-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2126LacpPortAdded.setStatus(
        "current"
    )

es2126LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 124)
)
es2126LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126-MIB", "actorkey"),
        ("LANCOM-ES-2126-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2126LacpPortTrunkFailure.setStatus(
        "current"
    )

es2126GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 140)
)
if mibBuilder.loadTexts:
    es2126GvrpStateDisabled.setStatus(
        "current"
    )

es2126GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 141)
)
if mibBuilder.loadTexts:
    es2126GvrpStateEnabled.setStatus(
        "current"
    )

es2126VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 151)
)
if mibBuilder.loadTexts:
    es2126VlanPortBaseEnabled.setStatus(
        "current"
    )

es2126VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 152)
)
if mibBuilder.loadTexts:
    es2126VlanTagBaseEnabled.setStatus(
        "current"
    )

es2126VlanMetroBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 153)
)
if mibBuilder.loadTexts:
    es2126VlanMetroBaseEnabled.setStatus(
        "current"
    )

es2126UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 200)
)
es2126UserLogin.setObjects(
    ("LANCOM-ES-2126-MIB", "username")
)
if mibBuilder.loadTexts:
    es2126UserLogin.setStatus(
        "current"
    )

es2126UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2126, 1, 20, 201)
)
es2126UserLogout.setObjects(
    ("LANCOM-ES-2126-MIB", "username")
)
if mibBuilder.loadTexts:
    es2126UserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-ES-2126-MIB",
    **{"lancomSystems": lancomSystems,
       "switchingSystems": switchingSystems,
       "fastEthernetSwitches": fastEthernetSwitches,
       "lancomES2126": lancomES2126,
       "es2126Produces": es2126Produces,
       "es2126System": es2126System,
       "es2126CommonSys": es2126CommonSys,
       "es2126Reboot": es2126Reboot,
       "es2126BiosVsersion": es2126BiosVsersion,
       "es2126FirmwareVersion": es2126FirmwareVersion,
       "es2126HardwareVersion": es2126HardwareVersion,
       "es2126MechanicalVersion": es2126MechanicalVersion,
       "es2126SerialNumber": es2126SerialNumber,
       "es2126HostMacAddress": es2126HostMacAddress,
       "es2126DevicePort": es2126DevicePort,
       "es2126RamSize": es2126RamSize,
       "es2126FlashSize": es2126FlashSize,
       "es2126SystemDescription": es2126SystemDescription,
       "es2126DeviceName": es2126DeviceName,
       "es2126IP": es2126IP,
       "es2126DhcpSetting": es2126DhcpSetting,
       "es2126IPAddress": es2126IPAddress,
       "es2126NetMask": es2126NetMask,
       "es2126DefaultGateway": es2126DefaultGateway,
       "es2126DnsSetting": es2126DnsSetting,
       "es2126DnsServer": es2126DnsServer,
       "es2126Time": es2126Time,
       "es2126SystemCurrentTime": es2126SystemCurrentTime,
       "es2126ManualTimeSetting": es2126ManualTimeSetting,
       "es2126NTPServer": es2126NTPServer,
       "es2126NTPTimeZone": es2126NTPTimeZone,
       "es2126NTPTimeSync": es2126NTPTimeSync,
       "es2126DaylightSavingTime": es2126DaylightSavingTime,
       "es2126DaylightStartTime": es2126DaylightStartTime,
       "es2126DaylightEndTime": es2126DaylightEndTime,
       "es2126Account": es2126Account,
       "es2126AccountNumber": es2126AccountNumber,
       "es2126AccountTable": es2126AccountTable,
       "es2126AccountEntry": es2126AccountEntry,
       "es2126AccountIndex": es2126AccountIndex,
       "es2126AccountAuthorization": es2126AccountAuthorization,
       "es2126AccountName": es2126AccountName,
       "es2126AccountPassword": es2126AccountPassword,
       "es2126AccountAddName": es2126AccountAddName,
       "es2126AccountAddPassword": es2126AccountAddPassword,
       "es2126DoAccountAdd": es2126DoAccountAdd,
       "es2126AccountDel": es2126AccountDel,
       "es2126Snmp": es2126Snmp,
       "es2126GetCommunity": es2126GetCommunity,
       "es2126SetCommunity": es2126SetCommunity,
       "es2126TrapHostNumber": es2126TrapHostNumber,
       "es2126TrapHostTable": es2126TrapHostTable,
       "es2126TrapHostEntry": es2126TrapHostEntry,
       "es2126TrapHostIndex": es2126TrapHostIndex,
       "es2126TrapHostIP": es2126TrapHostIP,
       "es2126TrapHostPort": es2126TrapHostPort,
       "es2126TrapHostCommunity": es2126TrapHostCommunity,
       "es2126RegisterMonitor": es2126RegisterMonitor,
       "es2126DeleteMonitor": es2126DeleteMonitor,
       "es2126MonitorTable": es2126MonitorTable,
       "es2126MonitorEntry": es2126MonitorEntry,
       "es2126MonitorTableIp": es2126MonitorTableIp,
       "es2126MonitorTableMac": es2126MonitorTableMac,
       "es2126TrapBootDelayTime": es2126TrapBootDelayTime,
       "es2126Alarm": es2126Alarm,
       "es2126Event": es2126Event,
       "es2126EventNumber": es2126EventNumber,
       "es2126EventTable": es2126EventTable,
       "es2126EventEntry": es2126EventEntry,
       "es2126EventIndex": es2126EventIndex,
       "es2126EventName": es2126EventName,
       "es2126EventSendEmail": es2126EventSendEmail,
       "es2126EventSendTrap": es2126EventSendTrap,
       "es2126Email": es2126Email,
       "es2126EmailServer": es2126EmailServer,
       "es2126EmailUsername": es2126EmailUsername,
       "es2126EmailPassword": es2126EmailPassword,
       "es2126EmailSender": es2126EmailSender,
       "es2126EmailReturnPath": es2126EmailReturnPath,
       "es2126EmailUserNumber": es2126EmailUserNumber,
       "es2126EmailUserTable": es2126EmailUserTable,
       "es2126EmailUserEntry": es2126EmailUserEntry,
       "es2126EmailUserIndex": es2126EmailUserIndex,
       "es2126EmailUserAddress": es2126EmailUserAddress,
       "es2126Tftp": es2126Tftp,
       "es2126RemoteTftpServer": es2126RemoteTftpServer,
       "es2126InternalTftpServerState": es2126InternalTftpServerState,
       "es2126Configuration": es2126Configuration,
       "es2126SaveRestore": es2126SaveRestore,
       "es2126SaveStart": es2126SaveStart,
       "es2126SaveUser": es2126SaveUser,
       "es2126RestoreDefault": es2126RestoreDefault,
       "es2126RestoreUser": es2126RestoreUser,
       "es2126ConfigFile": es2126ConfigFile,
       "es2126ExportConfigName": es2126ExportConfigName,
       "es2126DoExportConfig": es2126DoExportConfig,
       "es2126ImportConfigName": es2126ImportConfigName,
       "es2126DoImportConfig": es2126DoImportConfig,
       "es2126Diagnostic": es2126Diagnostic,
       "es2126InternalLoopbackTest": es2126InternalLoopbackTest,
       "es2126ExternalLoopbackTest": es2126ExternalLoopbackTest,
       "es2126PingTest": es2126PingTest,
       "es2126Watchdog": es2126Watchdog,
       "es2126WatchdogState": es2126WatchdogState,
       "es2126WatchdogTimeGap": es2126WatchdogTimeGap,
       "es2126WatchdogHost": es2126WatchdogHost,
       "es2126WatchdogResetMgtInf": es2126WatchdogResetMgtInf,
       "es2126WatchdogResetMgtInfCount": es2126WatchdogResetMgtInfCount,
       "es2126WatchdogResetSystem": es2126WatchdogResetSystem,
       "es2126WatchdogResetSystemCount": es2126WatchdogResetSystemCount,
       "es2126Log": es2126Log,
       "es2126ClearLog": es2126ClearLog,
       "es2126UploadLog": es2126UploadLog,
       "es2126AutoUploadLogState": es2126AutoUploadLogState,
       "es2126LogNumber": es2126LogNumber,
       "es2126LogTable": es2126LogTable,
       "es2126LogEntry": es2126LogEntry,
       "es2126LogIndex": es2126LogIndex,
       "es2126LogEvent": es2126LogEvent,
       "es2126Firmware": es2126Firmware,
       "es2126FirmwareFileName": es2126FirmwareFileName,
       "es2126DoFirmwareUpgrade": es2126DoFirmwareUpgrade,
       "es2126Port": es2126Port,
       "es2126PortStatus": es2126PortStatus,
       "es2126PortStatusNumber": es2126PortStatusNumber,
       "es2126PortStatusTable": es2126PortStatusTable,
       "es2126PortStatusEntry": es2126PortStatusEntry,
       "es2126PortStatusIndex": es2126PortStatusIndex,
       "es2126PortStatusMedia": es2126PortStatusMedia,
       "es2126PortStatusLink": es2126PortStatusLink,
       "es2126PortStatusPortState": es2126PortStatusPortState,
       "es2126PortStatusAutoNego": es2126PortStatusAutoNego,
       "es2126PortStatusSpdDpx": es2126PortStatusSpdDpx,
       "es2126PortStatusRxPause": es2126PortStatusRxPause,
       "es2126PortStatusTxPause": es2126PortStatusTxPause,
       "es2126PortStatusDescription": es2126PortStatusDescription,
       "es2126PortConf": es2126PortConf,
       "es2126PortConfNumber": es2126PortConfNumber,
       "es2126PortConfTable": es2126PortConfTable,
       "es2126PortConfEntry": es2126PortConfEntry,
       "es2126PortConfIndex": es2126PortConfIndex,
       "es2126PortConfPortState": es2126PortConfPortState,
       "es2126PortConfSpdDpx": es2126PortConfSpdDpx,
       "es2126PortConfFlwCtrl": es2126PortConfFlwCtrl,
       "es2126PortConfDescription": es2126PortConfDescription,
       "es2126PortBandwidth": es2126PortBandwidth,
       "es2126PortBandwidthTable": es2126PortBandwidthTable,
       "es2126PortBandwidthEntry": es2126PortBandwidthEntry,
       "es2126PortBandwidthIndex": es2126PortBandwidthIndex,
       "es2126PortBandwidthIngressRate": es2126PortBandwidthIngressRate,
       "es2126PortBandwidthEgressRate": es2126PortBandwidthEgressRate,
       "es2126PortBandwidthStormType": es2126PortBandwidthStormType,
       "es2126PortBandwidthStormRate": es2126PortBandwidthStormRate,
       "es2126PortSFPInfo": es2126PortSFPInfo,
       "es2126PortSFPInfoNumber": es2126PortSFPInfoNumber,
       "es2126PortSFPInfoTable": es2126PortSFPInfoTable,
       "es2126PortSFPInfoEntry": es2126PortSFPInfoEntry,
       "es2126PortSFPInfoIndex": es2126PortSFPInfoIndex,
       "es2126PortSFPConnectorType": es2126PortSFPConnectorType,
       "es2126PortSFPFiberType": es2126PortSFPFiberType,
       "es2126PortSFPWavelength": es2126PortSFPWavelength,
       "es2126PortSFPBaudRate": es2126PortSFPBaudRate,
       "es2126PortSFPVendorOUI": es2126PortSFPVendorOUI,
       "es2126PortSFPVendorName": es2126PortSFPVendorName,
       "es2126PortSFPVendorPN": es2126PortSFPVendorPN,
       "es2126PortSFPVendorRev": es2126PortSFPVendorRev,
       "es2126PortSFPVendorSN": es2126PortSFPVendorSN,
       "es2126PortSFPDateCode": es2126PortSFPDateCode,
       "es2126PortSFPTemperature": es2126PortSFPTemperature,
       "es2126PortSFPVcc": es2126PortSFPVcc,
       "es2126PortSFPTxBias": es2126PortSFPTxBias,
       "es2126PortSFPTxPWR": es2126PortSFPTxPWR,
       "es2126PortSFPRxPWR": es2126PortSFPRxPWR,
       "es2126LoopDetectedConf": es2126LoopDetectedConf,
       "es2126LoopDetectedNumber": es2126LoopDetectedNumber,
       "es2126LoopDetectedTable": es2126LoopDetectedTable,
       "es2126LoopDetectedEntry": es2126LoopDetectedEntry,
       "es2126LoopDetectedfIndex": es2126LoopDetectedfIndex,
       "es2126LoopDetectedStateEbl": es2126LoopDetectedStateEbl,
       "es2126LoopDetectedCurrentStatus": es2126LoopDetectedCurrentStatus,
       "es2126LoopDetectedResumed": es2126LoopDetectedResumed,
       "es2126LoopDetectedAction": es2126LoopDetectedAction,
       "es2126MacTableInfo": es2126MacTableInfo,
       "es2126MacTableMaintenance": es2126MacTableMaintenance,
       "es2126MacTableAgingTime": es2126MacTableAgingTime,
       "es2126MacTableFlush": es2126MacTableFlush,
       "es2126MacTableLearnPortLimitTable": es2126MacTableLearnPortLimitTable,
       "es2126MacTableLearnPortLimitEntry": es2126MacTableLearnPortLimitEntry,
       "es2126MacTableLearnPortLimitIndex": es2126MacTableLearnPortLimitIndex,
       "es2126MacTableLearnPortLimit": es2126MacTableLearnPortLimit,
       "es2126MacTableStaticMac": es2126MacTableStaticMac,
       "es2126MacTableStaticMacNumber": es2126MacTableStaticMacNumber,
       "es2126MacTableStaticMacEntryCreate": es2126MacTableStaticMacEntryCreate,
       "es2126MacTableStaticMacTable": es2126MacTableStaticMacTable,
       "es2126MacTableStaticMacEntry": es2126MacTableStaticMacEntry,
       "es2126MacTableStaticMacIndex": es2126MacTableStaticMacIndex,
       "es2126MacTableStaticMacAddress": es2126MacTableStaticMacAddress,
       "es2126MacTableStaticMacVid": es2126MacTableStaticMacVid,
       "es2126MacTableStaticMacQueue": es2126MacTableStaticMacQueue,
       "es2126MacTableStaticMacFwRule": es2126MacTableStaticMacFwRule,
       "es2126MacTableStaticMacPort": es2126MacTableStaticMacPort,
       "es2126MacTableStaticMacEntryAction": es2126MacTableStaticMacEntryAction,
       "es2126MacTableMacAlias": es2126MacTableMacAlias,
       "es2126MacTableMacAliasNumber": es2126MacTableMacAliasNumber,
       "es2126MacTableMacAliasEntryCreate": es2126MacTableMacAliasEntryCreate,
       "es2126MacTableMacAliasTable": es2126MacTableMacAliasTable,
       "es2126MacTableMacAliasEntry": es2126MacTableMacAliasEntry,
       "es2126MacTableMacAliasIndex": es2126MacTableMacAliasIndex,
       "es2126MacTableMacAliasAddress": es2126MacTableMacAliasAddress,
       "es2126MacTableMacAliasAlias": es2126MacTableMacAliasAlias,
       "es2126MacTableMacAliasEntryAction": es2126MacTableMacAliasEntryAction,
       "es2126GVRPInfo": es2126GVRPInfo,
       "es2126GvrpConf": es2126GvrpConf,
       "es2126GvrpConfState": es2126GvrpConfState,
       "es2126GvrpConfTable": es2126GvrpConfTable,
       "es2126GvrpConfEntry": es2126GvrpConfEntry,
       "es2126GvrpConfIndex": es2126GvrpConfIndex,
       "es2126GvrpConfJoinTime": es2126GvrpConfJoinTime,
       "es2126GvrpConfLeaveTime": es2126GvrpConfLeaveTime,
       "es2126GvrpConfLeaveAllTime": es2126GvrpConfLeaveAllTime,
       "es2126GvrpConfDefaultAppMode": es2126GvrpConfDefaultAppMode,
       "es2126GvrpConfDefaultRegMode": es2126GvrpConfDefaultRegMode,
       "es2126GvrpConfRestrictedMode": es2126GvrpConfRestrictedMode,
       "es2126GvrpCounter": es2126GvrpCounter,
       "es2126GvrpCounterTable": es2126GvrpCounterTable,
       "es2126GvrpCounterEntry": es2126GvrpCounterEntry,
       "es2126GvrpCounterIndex": es2126GvrpCounterIndex,
       "es2126GvrpCounterRxTotalGvrpPkts": es2126GvrpCounterRxTotalGvrpPkts,
       "es2126GvrpCounterRxInvalidGvrpPkts": es2126GvrpCounterRxInvalidGvrpPkts,
       "es2126GvrpCounterRxLeaveAllMsg": es2126GvrpCounterRxLeaveAllMsg,
       "es2126GvrpCounterRxJoinEmptyMsg": es2126GvrpCounterRxJoinEmptyMsg,
       "es2126GvrpCounterRxJoinInMsg": es2126GvrpCounterRxJoinInMsg,
       "es2126GvrpCounterRxLeaveEmptyMsg": es2126GvrpCounterRxLeaveEmptyMsg,
       "es2126GvrpCounterRxEmptyMsg": es2126GvrpCounterRxEmptyMsg,
       "es2126GvrpCounterTxTotalGvrpPkts": es2126GvrpCounterTxTotalGvrpPkts,
       "es2126GvrpCounterTxLeaveAllMsg": es2126GvrpCounterTxLeaveAllMsg,
       "es2126GvrpCounterTxJoinEmptyMsg": es2126GvrpCounterTxJoinEmptyMsg,
       "es2126GvrpCounterTxJoinInMsg": es2126GvrpCounterTxJoinInMsg,
       "es2126GvrpCounterTxLeaveEmptyMsg": es2126GvrpCounterTxLeaveEmptyMsg,
       "es2126GvrpCounterTxEmptyMsg": es2126GvrpCounterTxEmptyMsg,
       "es2126GvrpGroup": es2126GvrpGroup,
       "es2126GvrpGroupNumber": es2126GvrpGroupNumber,
       "es2126GvrpGroupTable": es2126GvrpGroupTable,
       "es2126GvrpGroupEntry": es2126GvrpGroupEntry,
       "es2126GvrpGroupId": es2126GvrpGroupId,
       "es2126GvrpGroupVid": es2126GvrpGroupVid,
       "es2126GvrpGroupMemberPort": es2126GvrpGroupMemberPort,
       "es2126Security": es2126Security,
       "es2126IsolatedPortGroup": es2126IsolatedPortGroup,
       "es2126Mirror": es2126Mirror,
       "es2126MirrorMode": es2126MirrorMode,
       "es2126MonitoringPort": es2126MonitoringPort,
       "es2126MonitoredIngressPort": es2126MonitoredIngressPort,
       "es2126MonitoredEgressPort": es2126MonitoredEgressPort,
       "es2126VirtualStack": es2126VirtualStack,
       "es2126VirtualStackState": es2126VirtualStackState,
       "es2126VirtualStackRole": es2126VirtualStackRole,
       "es2126VirtualStackGroupID": es2126VirtualStackGroupID,
       "es2126ManagementSecurity": es2126ManagementSecurity,
       "es2126ManagementSecurityNumber": es2126ManagementSecurityNumber,
       "es2126ManagementSecurityEntryCreate": es2126ManagementSecurityEntryCreate,
       "es2126ManagementSecurityTable": es2126ManagementSecurityTable,
       "es2126ManagementSecurityEntry": es2126ManagementSecurityEntry,
       "es2126ManagementSecurityIndex": es2126ManagementSecurityIndex,
       "es2126ManagementSecurityName": es2126ManagementSecurityName,
       "es2126ManagementSecurityVid": es2126ManagementSecurityVid,
       "es2126ManagementSecurityIpRange": es2126ManagementSecurityIpRange,
       "es2126ManagementSecurityIncomigPort": es2126ManagementSecurityIncomigPort,
       "es2126ManagementSecurityAccessType": es2126ManagementSecurityAccessType,
       "es2126ManagementSecurityAction": es2126ManagementSecurityAction,
       "es2126ManagementSecurityEntryAction": es2126ManagementSecurityEntryAction,
       "es2126QoS": es2126QoS,
       "es2126QoSGlobalConfig": es2126QoSGlobalConfig,
       "es2126QoSMode": es2126QoSMode,
       "es2126QosPriorityControl1p": es2126QosPriorityControl1p,
       "es2126QosPriorityControlTOS": es2126QosPriorityControlTOS,
       "es2126QosPriorityControlDSCP": es2126QosPriorityControlDSCP,
       "es2126QoSSchedulingMethod": es2126QoSSchedulingMethod,
       "es2126QoSWeightQ0": es2126QoSWeightQ0,
       "es2126QoSWeightQ1": es2126QoSWeightQ1,
       "es2126QoSWeightQ2": es2126QoSWeightQ2,
       "es2126QoSWeightQ3": es2126QoSWeightQ3,
       "es2126QoSVIPPort": es2126QoSVIPPort,
       "es2126QoS1pPriority": es2126QoS1pPriority,
       "es2126QoS1pPriorityTable": es2126QoS1pPriorityTable,
       "es2126QoS1pPriorityEntry": es2126QoS1pPriorityEntry,
       "es2126QoS1pPriorityIndex": es2126QoS1pPriorityIndex,
       "es2126QoS1pPriorityValue": es2126QoS1pPriorityValue,
       "es2126QoS1pPriorityQueue": es2126QoS1pPriorityQueue,
       "es2126QoSDTypeTOSPriority": es2126QoSDTypeTOSPriority,
       "es2126QoSDTypeTOSPriorityTable": es2126QoSDTypeTOSPriorityTable,
       "es2126QoSDTypeTOSPriorityEntry": es2126QoSDTypeTOSPriorityEntry,
       "es2126QoSDTypeTOSPriorityIndex": es2126QoSDTypeTOSPriorityIndex,
       "es2126QoSDTypeTOSPriorityValue": es2126QoSDTypeTOSPriorityValue,
       "es2126QoSDTypeTOSPriorityQueue": es2126QoSDTypeTOSPriorityQueue,
       "es2126QoSTTypeTOSPriority": es2126QoSTTypeTOSPriority,
       "es2126QoSTTypeTOSPriorityTable": es2126QoSTTypeTOSPriorityTable,
       "es2126QoSTTypeTOSPriorityEntry": es2126QoSTTypeTOSPriorityEntry,
       "es2126QoSTTypeTOSPriorityIndex": es2126QoSTTypeTOSPriorityIndex,
       "es2126QoSTTypeTOSPriorityValue": es2126QoSTTypeTOSPriorityValue,
       "es2126QoSTTypeTOSPriorityQueue": es2126QoSTTypeTOSPriorityQueue,
       "es2126QoSRTypeTOSPriority": es2126QoSRTypeTOSPriority,
       "es2126QoSRTypeTOSPriorityTable": es2126QoSRTypeTOSPriorityTable,
       "es2126QoSRTypeTOSPriorityEntry": es2126QoSRTypeTOSPriorityEntry,
       "es2126QoSRTypeTOSPriorityIndex": es2126QoSRTypeTOSPriorityIndex,
       "es2126QoSRTypeTOSPriorityValue": es2126QoSRTypeTOSPriorityValue,
       "es2126QoSRTypeTOSPriorityQueue": es2126QoSRTypeTOSPriorityQueue,
       "es2126QoSMTypeTOSPriority": es2126QoSMTypeTOSPriority,
       "es2126QoSMTypeTOSPriorityTable": es2126QoSMTypeTOSPriorityTable,
       "es2126QoSMTypeTOSPriorityEntry": es2126QoSMTypeTOSPriorityEntry,
       "es2126QoSMTypeTOSPriorityIndex": es2126QoSMTypeTOSPriorityIndex,
       "es2126QoSMTypeTOSPriorityValue": es2126QoSMTypeTOSPriorityValue,
       "es2126QoSMTypeTOSPriorityQueue": es2126QoSMTypeTOSPriorityQueue,
       "es2126QoSDSCPPriority": es2126QoSDSCPPriority,
       "es2126QoSDSCPPriorityTable": es2126QoSDSCPPriorityTable,
       "es2126QoSDSCPPriorityEntry": es2126QoSDSCPPriorityEntry,
       "es2126QoSDSCPPriorityIndex": es2126QoSDSCPPriorityIndex,
       "es2126QoSDSCPPriorityValue": es2126QoSDSCPPriorityValue,
       "es2126QoSDSCPPriorityQueue": es2126QoSDSCPPriorityQueue,
       "es2126Vlan": es2126Vlan,
       "es2126VlanModeConfig": es2126VlanModeConfig,
       "es2126VlanMode": es2126VlanMode,
       "es2126SymmetricVlan": es2126SymmetricVlan,
       "es2126VlanSVL": es2126VlanSVL,
       "es2126DoubleTag": es2126DoubleTag,
       "es2126UpLinkPort": es2126UpLinkPort,
       "es2126TagBasedVlanGroup": es2126TagBasedVlanGroup,
       "es2126TagBasedVlanNumbers": es2126TagBasedVlanNumbers,
       "es2126TagBasedCreateStatus": es2126TagBasedCreateStatus,
       "es2126TagBasedVlanTable": es2126TagBasedVlanTable,
       "es2126TagBasedVlanEntry": es2126TagBasedVlanEntry,
       "es2126TagBasedVlanVid": es2126TagBasedVlanVid,
       "es2126TagBasedVlanName": es2126TagBasedVlanName,
       "es2126TagBasedVlanMember": es2126TagBasedVlanMember,
       "es2126TagBasedVlanUntag": es2126TagBasedVlanUntag,
       "es2126TagBasedVlanRowStatus": es2126TagBasedVlanRowStatus,
       "es2126VlanPvid": es2126VlanPvid,
       "es2126VlanPvidTable": es2126VlanPvidTable,
       "es2126VlanPvidEntry": es2126VlanPvidEntry,
       "es2126VlanPvidPort": es2126VlanPvidPort,
       "es2126VlanPvidValue": es2126VlanPvidValue,
       "es2126VlanPvidDefaultPriority": es2126VlanPvidDefaultPriority,
       "es2126VlanPvidDropUntag": es2126VlanPvidDropUntag,
       "es2126PortBasedVlanGroup": es2126PortBasedVlanGroup,
       "es2126PortBasedVlanNumbers": es2126PortBasedVlanNumbers,
       "es2126PortBasedCreateStatus": es2126PortBasedCreateStatus,
       "es2126PortBasedVlanTable": es2126PortBasedVlanTable,
       "es2126PortBasedVlanEntry": es2126PortBasedVlanEntry,
       "es2126PortBasedVlanIndex": es2126PortBasedVlanIndex,
       "es2126PortBasedVlanName": es2126PortBasedVlanName,
       "es2126PortBasedVlanMember": es2126PortBasedVlanMember,
       "es2126PortBasedVlanRowStatus": es2126PortBasedVlanRowStatus,
       "es2126ManagementVlan": es2126ManagementVlan,
       "es2126ManagementVlanState": es2126ManagementVlanState,
       "es2126ManagementVlanVid": es2126ManagementVlanVid,
       "es2126Dot1X": es2126Dot1X,
       "es2126Dot1XStateSetting": es2126Dot1XStateSetting,
       "es2126RadiusServer": es2126RadiusServer,
       "es2126Dot1XPort": es2126Dot1XPort,
       "es2126SecretKey": es2126SecretKey,
       "es2126AccountingService": es2126AccountingService,
       "es2126AccountingServer": es2126AccountingServer,
       "es2126AccountingPort": es2126AccountingPort,
       "es2126Dot1XPortSecurityManagement": es2126Dot1XPortSecurityManagement,
       "es2126Dot1XPortSecurityTable": es2126Dot1XPortSecurityTable,
       "es2126Dot1XPortSecurityEntry": es2126Dot1XPortSecurityEntry,
       "es2126Dot1XPortSecurityPortIndex": es2126Dot1XPortSecurityPortIndex,
       "es2126Dot1XPortSecurityMode": es2126Dot1XPortSecurityMode,
       "es2126Dot1XPortSecurityPortControl": es2126Dot1XPortSecurityPortControl,
       "es2126Dot1XPortSecurityReAuthMax": es2126Dot1XPortSecurityReAuthMax,
       "es2126Dot1XPortSecurityTxPeriod": es2126Dot1XPortSecurityTxPeriod,
       "es2126Dot1XPortSecurityQuietPeriod": es2126Dot1XPortSecurityQuietPeriod,
       "es2126Dot1XPortSecurityReAuthEnabled": es2126Dot1XPortSecurityReAuthEnabled,
       "es2126Dot1XPortSecurityReAuthPeriod": es2126Dot1XPortSecurityReAuthPeriod,
       "es2126Dot1XPortSecurityMaxRequest": es2126Dot1XPortSecurityMaxRequest,
       "es2126Dot1XPortSecuritySuppTimeout": es2126Dot1XPortSecuritySuppTimeout,
       "es2126Dot1XPortSecurityServerTimeout": es2126Dot1XPortSecurityServerTimeout,
       "es2126Dot1XPortSecurityStatus": es2126Dot1XPortSecurityStatus,
       "es2126TrunkInfo": es2126TrunkInfo,
       "es2126TrunkPort": es2126TrunkPort,
       "es2126TrunkPortTable": es2126TrunkPortTable,
       "es2126TrunkPortEntry": es2126TrunkPortEntry,
       "es2126TrunkPortIndex": es2126TrunkPortIndex,
       "es2126TrunkPortMethod": es2126TrunkPortMethod,
       "es2126TrunkPortGroup": es2126TrunkPortGroup,
       "es2126TrunkPortActiveLacp": es2126TrunkPortActiveLacp,
       "es2126TrunkPortAggtr": es2126TrunkPortAggtr,
       "es2126TrunkPortStatus": es2126TrunkPortStatus,
       "es2126TrunkPortCurrentMode": es2126TrunkPortCurrentMode,
       "es2126AggregatorView": es2126AggregatorView,
       "es2126AggregatorViewTable": es2126AggregatorViewTable,
       "es2126AggregatorViewEntry": es2126AggregatorViewEntry,
       "es2126AggregatorViewIndex": es2126AggregatorViewIndex,
       "es2126AggregatorViewMethod": es2126AggregatorViewMethod,
       "es2126AggregatorViewMemberPorts": es2126AggregatorViewMemberPorts,
       "es2126AggregatorViewReadyPorts": es2126AggregatorViewReadyPorts,
       "es2126LacpSystemConfiguration": es2126LacpSystemConfiguration,
       "es2126LacpSystemPriority": es2126LacpSystemPriority,
       "es2126LacpSystemHashMethod": es2126LacpSystemHashMethod,
       "es2126TrapEntry": es2126TrapEntry,
       "es2126ModuleInserted": es2126ModuleInserted,
       "es2126ModuleRemoved": es2126ModuleRemoved,
       "es2126DualMediaSwapped": es2126DualMediaSwapped,
       "es2126LoopDetected": es2126LoopDetected,
       "es2126StpStateDisabled": es2126StpStateDisabled,
       "es2126StpStateEnabled": es2126StpStateEnabled,
       "es2126StpTopologyChanged": es2126StpTopologyChanged,
       "es2126RmonRisingAlarm": es2126RmonRisingAlarm,
       "es2126RmonFallingAlarm": es2126RmonFallingAlarm,
       "es2126LacpStateDisabled": es2126LacpStateDisabled,
       "es2126LacpStateEnabled": es2126LacpStateEnabled,
       "es2126LacpPortAdded": es2126LacpPortAdded,
       "es2126LacpPortTrunkFailure": es2126LacpPortTrunkFailure,
       "es2126GvrpStateDisabled": es2126GvrpStateDisabled,
       "es2126GvrpStateEnabled": es2126GvrpStateEnabled,
       "es2126VlanPortBaseEnabled": es2126VlanPortBaseEnabled,
       "es2126VlanTagBaseEnabled": es2126VlanTagBaseEnabled,
       "es2126VlanMetroBaseEnabled": es2126VlanMetroBaseEnabled,
       "es2126UserLogin": es2126UserLogin,
       "es2126UserLogout": es2126UserLogout,
       "es2126TrapVariable": es2126TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink,
       "loginProtectInfo": loginProtectInfo,
       "es2126LoginProtect": es2126LoginProtect,
       "es2126LockMinutes": es2126LockMinutes,
       "es2126LoginErrors": es2126LoginErrors}
)
