# SNMP MIB module (RUBYTECH-ES2226-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rubytech/RUBYTECH-ES2226-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:42 2025
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
_Es2226ProductID_ObjectIdentity = ObjectIdentity
es2226ProductID = _Es2226ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31)
)
_Es2226Produces_ObjectIdentity = ObjectIdentity
es2226Produces = _Es2226Produces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1)
)
_Es2226System_ObjectIdentity = ObjectIdentity
es2226System = _Es2226System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1)
)
_Es2226CommonSys_ObjectIdentity = ObjectIdentity
es2226CommonSys = _Es2226CommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1)
)


class _Es2226Reboot_Type(Integer32):
    """Custom type es2226Reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2226Reboot_Type.__name__ = "Integer32"
_Es2226Reboot_Object = MibScalar
es2226Reboot = _Es2226Reboot_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 1),
    _Es2226Reboot_Type()
)
es2226Reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Reboot.setStatus("current")
_Es2226BiosVsersion_Type = DisplayString
_Es2226BiosVsersion_Object = MibScalar
es2226BiosVsersion = _Es2226BiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 2),
    _Es2226BiosVsersion_Type()
)
es2226BiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226BiosVsersion.setStatus("current")
_Es2226FirmwareVersion_Type = DisplayString
_Es2226FirmwareVersion_Object = MibScalar
es2226FirmwareVersion = _Es2226FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 3),
    _Es2226FirmwareVersion_Type()
)
es2226FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226FirmwareVersion.setStatus("current")
_Es2226HardwareVersion_Type = DisplayString
_Es2226HardwareVersion_Object = MibScalar
es2226HardwareVersion = _Es2226HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 4),
    _Es2226HardwareVersion_Type()
)
es2226HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226HardwareVersion.setStatus("current")
_Es2226MechanicalVersion_Type = DisplayString
_Es2226MechanicalVersion_Object = MibScalar
es2226MechanicalVersion = _Es2226MechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 5),
    _Es2226MechanicalVersion_Type()
)
es2226MechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MechanicalVersion.setStatus("current")
_Es2226SerialNumber_Type = DisplayString
_Es2226SerialNumber_Object = MibScalar
es2226SerialNumber = _Es2226SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 6),
    _Es2226SerialNumber_Type()
)
es2226SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226SerialNumber.setStatus("current")
_Es2226HostMacAddress_Type = DisplayString
_Es2226HostMacAddress_Object = MibScalar
es2226HostMacAddress = _Es2226HostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 7),
    _Es2226HostMacAddress_Type()
)
es2226HostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226HostMacAddress.setStatus("current")
_Es2226DevicePort_Type = DisplayString
_Es2226DevicePort_Object = MibScalar
es2226DevicePort = _Es2226DevicePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 8),
    _Es2226DevicePort_Type()
)
es2226DevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DevicePort.setStatus("current")
_Es2226RamSize_Type = DisplayString
_Es2226RamSize_Object = MibScalar
es2226RamSize = _Es2226RamSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 9),
    _Es2226RamSize_Type()
)
es2226RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226RamSize.setStatus("current")
_Es2226FlashSize_Type = DisplayString
_Es2226FlashSize_Object = MibScalar
es2226FlashSize = _Es2226FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 10),
    _Es2226FlashSize_Type()
)
es2226FlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226FlashSize.setStatus("current")
_Es2226CPULoad_Type = DisplayString
_Es2226CPULoad_Object = MibScalar
es2226CPULoad = _Es2226CPULoad_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 1, 11),
    _Es2226CPULoad_Type()
)
es2226CPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226CPULoad.setStatus("current")
_Es2226IP_ObjectIdentity = ObjectIdentity
es2226IP = _Es2226IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2)
)


class _Es2226DhcpSetting_Type(Integer32):
    """Custom type es2226DhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpSetting_Type.__name__ = "Integer32"
_Es2226DhcpSetting_Object = MibScalar
es2226DhcpSetting = _Es2226DhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2, 1),
    _Es2226DhcpSetting_Type()
)
es2226DhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSetting.setStatus("current")
_Es2226IPAddress_Type = IpAddress
_Es2226IPAddress_Object = MibScalar
es2226IPAddress = _Es2226IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2, 2),
    _Es2226IPAddress_Type()
)
es2226IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IPAddress.setStatus("current")
_Es2226NetMask_Type = IpAddress
_Es2226NetMask_Object = MibScalar
es2226NetMask = _Es2226NetMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2, 3),
    _Es2226NetMask_Type()
)
es2226NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226NetMask.setStatus("current")
_Es2226DefaultGateway_Type = IpAddress
_Es2226DefaultGateway_Object = MibScalar
es2226DefaultGateway = _Es2226DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2, 4),
    _Es2226DefaultGateway_Type()
)
es2226DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DefaultGateway.setStatus("current")


class _Es2226DnsSetting_Type(Integer32):
    """Custom type es2226DnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DnsSetting_Type.__name__ = "Integer32"
_Es2226DnsSetting_Object = MibScalar
es2226DnsSetting = _Es2226DnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2, 5),
    _Es2226DnsSetting_Type()
)
es2226DnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DnsSetting.setStatus("current")
_Es2226DnsServer_Type = IpAddress
_Es2226DnsServer_Object = MibScalar
es2226DnsServer = _Es2226DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 2, 6),
    _Es2226DnsServer_Type()
)
es2226DnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DnsServer.setStatus("current")
_Es2226Time_ObjectIdentity = ObjectIdentity
es2226Time = _Es2226Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3)
)
_Es2226SystemCurrentTime_Type = DisplayString
_Es2226SystemCurrentTime_Object = MibScalar
es2226SystemCurrentTime = _Es2226SystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 1),
    _Es2226SystemCurrentTime_Type()
)
es2226SystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226SystemCurrentTime.setStatus("current")
_Es2226ManualTimeSetting_Type = DisplayString
_Es2226ManualTimeSetting_Object = MibScalar
es2226ManualTimeSetting = _Es2226ManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 2),
    _Es2226ManualTimeSetting_Type()
)
es2226ManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManualTimeSetting.setStatus("current")
_Es2226NTPServer_Type = DisplayString
_Es2226NTPServer_Object = MibScalar
es2226NTPServer = _Es2226NTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 3),
    _Es2226NTPServer_Type()
)
es2226NTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226NTPServer.setStatus("current")


class _Es2226NTPTimeZone_Type(Integer32):
    """Custom type es2226NTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Es2226NTPTimeZone_Type.__name__ = "Integer32"
_Es2226NTPTimeZone_Object = MibScalar
es2226NTPTimeZone = _Es2226NTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 4),
    _Es2226NTPTimeZone_Type()
)
es2226NTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226NTPTimeZone.setStatus("current")


class _Es2226NTPTimeSync_Type(Integer32):
    """Custom type es2226NTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226NTPTimeSync_Type.__name__ = "Integer32"
_Es2226NTPTimeSync_Object = MibScalar
es2226NTPTimeSync = _Es2226NTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 5),
    _Es2226NTPTimeSync_Type()
)
es2226NTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226NTPTimeSync.setStatus("current")


class _Es2226DaylightSavingTime_Type(Integer32):
    """Custom type es2226DaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Es2226DaylightSavingTime_Type.__name__ = "Integer32"
_Es2226DaylightSavingTime_Object = MibScalar
es2226DaylightSavingTime = _Es2226DaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 6),
    _Es2226DaylightSavingTime_Type()
)
es2226DaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DaylightSavingTime.setStatus("current")
_Es2226DaylightStartTime_Type = DisplayString
_Es2226DaylightStartTime_Object = MibScalar
es2226DaylightStartTime = _Es2226DaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 7),
    _Es2226DaylightStartTime_Type()
)
es2226DaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DaylightStartTime.setStatus("current")
_Es2226DaylightEndTime_Type = DisplayString
_Es2226DaylightEndTime_Object = MibScalar
es2226DaylightEndTime = _Es2226DaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 3, 8),
    _Es2226DaylightEndTime_Type()
)
es2226DaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DaylightEndTime.setStatus("current")
_Es2226Account_ObjectIdentity = ObjectIdentity
es2226Account = _Es2226Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4)
)


class _Es2226AccountNumber_Type(Integer32):
    """Custom type es2226AccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2226AccountNumber_Type.__name__ = "Integer32"
_Es2226AccountNumber_Object = MibScalar
es2226AccountNumber = _Es2226AccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 1),
    _Es2226AccountNumber_Type()
)
es2226AccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226AccountNumber.setStatus("current")
_Es2226AccountTable_Object = MibTable
es2226AccountTable = _Es2226AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    es2226AccountTable.setStatus("current")
_Es2226AccountEntry_Object = MibTableRow
es2226AccountEntry = _Es2226AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 2, 1)
)
es2226AccountEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226AccountIndex"),
)
if mibBuilder.loadTexts:
    es2226AccountEntry.setStatus("current")


class _Es2226AccountIndex_Type(Integer32):
    """Custom type es2226AccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2226AccountIndex_Type.__name__ = "Integer32"
_Es2226AccountIndex_Object = MibTableColumn
es2226AccountIndex = _Es2226AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 2, 1, 1),
    _Es2226AccountIndex_Type()
)
es2226AccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226AccountIndex.setStatus("current")
_Es2226AccountAuthorization_Type = DisplayString
_Es2226AccountAuthorization_Object = MibTableColumn
es2226AccountAuthorization = _Es2226AccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 2, 1, 2),
    _Es2226AccountAuthorization_Type()
)
es2226AccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226AccountAuthorization.setStatus("current")
_Es2226AccountName_Type = DisplayString
_Es2226AccountName_Object = MibTableColumn
es2226AccountName = _Es2226AccountName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 2, 1, 3),
    _Es2226AccountName_Type()
)
es2226AccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountName.setStatus("current")
_Es2226AccountPassword_Type = DisplayString
_Es2226AccountPassword_Object = MibTableColumn
es2226AccountPassword = _Es2226AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 2, 1, 4),
    _Es2226AccountPassword_Type()
)
es2226AccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountPassword.setStatus("current")
_Es2226AccountAddName_Type = DisplayString
_Es2226AccountAddName_Object = MibScalar
es2226AccountAddName = _Es2226AccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 3),
    _Es2226AccountAddName_Type()
)
es2226AccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountAddName.setStatus("current")
_Es2226AccountAddPassword_Type = DisplayString
_Es2226AccountAddPassword_Object = MibScalar
es2226AccountAddPassword = _Es2226AccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 4),
    _Es2226AccountAddPassword_Type()
)
es2226AccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountAddPassword.setStatus("current")


class _Es2226DoAccountAdd_Type(Integer32):
    """Custom type es2226DoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DoAccountAdd_Type.__name__ = "Integer32"
_Es2226DoAccountAdd_Object = MibScalar
es2226DoAccountAdd = _Es2226DoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 5),
    _Es2226DoAccountAdd_Type()
)
es2226DoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DoAccountAdd.setStatus("current")


class _Es2226AccountDel_Type(Integer32):
    """Custom type es2226AccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Es2226AccountDel_Type.__name__ = "Integer32"
_Es2226AccountDel_Object = MibScalar
es2226AccountDel = _Es2226AccountDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 1, 4, 6),
    _Es2226AccountDel_Type()
)
es2226AccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountDel.setStatus("current")
_Es2226TrapHost_ObjectIdentity = ObjectIdentity
es2226TrapHost = _Es2226TrapHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2)
)


class _Es2226TrapBootDelayTime_Type(Integer32):
    """Custom type es2226TrapBootDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2226TrapBootDelayTime_Type.__name__ = "Integer32"
_Es2226TrapBootDelayTime_Object = MibScalar
es2226TrapBootDelayTime = _Es2226TrapBootDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 1),
    _Es2226TrapBootDelayTime_Type()
)
es2226TrapBootDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapBootDelayTime.setStatus("current")
_Es2226TrapHostTable_Object = MibTable
es2226TrapHostTable = _Es2226TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2)
)
if mibBuilder.loadTexts:
    es2226TrapHostTable.setStatus("current")
_Es2226TrapHostEntry_Object = MibTableRow
es2226TrapHostEntry = _Es2226TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1)
)
es2226TrapHostEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226TrapHostIndex"),
)
if mibBuilder.loadTexts:
    es2226TrapHostEntry.setStatus("current")


class _Es2226TrapHostIndex_Type(Integer32):
    """Custom type es2226TrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2226TrapHostIndex_Type.__name__ = "Integer32"
_Es2226TrapHostIndex_Object = MibTableColumn
es2226TrapHostIndex = _Es2226TrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 1),
    _Es2226TrapHostIndex_Type()
)
es2226TrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226TrapHostIndex.setStatus("current")


class _Es2226TrapHostVersion_Type(Integer32):
    """Custom type es2226TrapHostVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226TrapHostVersion_Type.__name__ = "Integer32"
_Es2226TrapHostVersion_Object = MibTableColumn
es2226TrapHostVersion = _Es2226TrapHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 2),
    _Es2226TrapHostVersion_Type()
)
es2226TrapHostVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostVersion.setStatus("current")
_Es2226TrapHostIP_Type = IpAddress
_Es2226TrapHostIP_Object = MibTableColumn
es2226TrapHostIP = _Es2226TrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 3),
    _Es2226TrapHostIP_Type()
)
es2226TrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostIP.setStatus("current")


class _Es2226TrapHostPort_Type(Integer32):
    """Custom type es2226TrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226TrapHostPort_Type.__name__ = "Integer32"
_Es2226TrapHostPort_Object = MibTableColumn
es2226TrapHostPort = _Es2226TrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 4),
    _Es2226TrapHostPort_Type()
)
es2226TrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostPort.setStatus("current")
_Es2226TrapHostCommunity_Type = DisplayString
_Es2226TrapHostCommunity_Object = MibTableColumn
es2226TrapHostCommunity = _Es2226TrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 5),
    _Es2226TrapHostCommunity_Type()
)
es2226TrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostCommunity.setStatus("current")


class _Es2226TrapHostSecurity_Type(Integer32):
    """Custom type es2226TrapHostSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226TrapHostSecurity_Type.__name__ = "Integer32"
_Es2226TrapHostSecurity_Object = MibTableColumn
es2226TrapHostSecurity = _Es2226TrapHostSecurity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 6),
    _Es2226TrapHostSecurity_Type()
)
es2226TrapHostSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostSecurity.setStatus("current")
_Es2226TrapHostAuthPtc_Type = DisplayString
_Es2226TrapHostAuthPtc_Object = MibTableColumn
es2226TrapHostAuthPtc = _Es2226TrapHostAuthPtc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 7),
    _Es2226TrapHostAuthPtc_Type()
)
es2226TrapHostAuthPtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostAuthPtc.setStatus("current")
_Es2226TrapHostAuthPassword_Type = DisplayString
_Es2226TrapHostAuthPassword_Object = MibTableColumn
es2226TrapHostAuthPassword = _Es2226TrapHostAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 8),
    _Es2226TrapHostAuthPassword_Type()
)
es2226TrapHostAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostAuthPassword.setStatus("current")
_Es2226TrapHostPrivPtc_Type = DisplayString
_Es2226TrapHostPrivPtc_Object = MibTableColumn
es2226TrapHostPrivPtc = _Es2226TrapHostPrivPtc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 9),
    _Es2226TrapHostPrivPtc_Type()
)
es2226TrapHostPrivPtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226TrapHostPrivPtc.setStatus("current")
_Es2226TrapHostPrivPassword_Type = DisplayString
_Es2226TrapHostPrivPassword_Object = MibTableColumn
es2226TrapHostPrivPassword = _Es2226TrapHostPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 10),
    _Es2226TrapHostPrivPassword_Type()
)
es2226TrapHostPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostPrivPassword.setStatus("current")


class _Es2226TrapHostCurrentMode_Type(Integer32):
    """Custom type es2226TrapHostCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226TrapHostCurrentMode_Type.__name__ = "Integer32"
_Es2226TrapHostCurrentMode_Object = MibTableColumn
es2226TrapHostCurrentMode = _Es2226TrapHostCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 2, 2, 1, 11),
    _Es2226TrapHostCurrentMode_Type()
)
es2226TrapHostCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrapHostCurrentMode.setStatus("current")
_Es2226Alarm_ObjectIdentity = ObjectIdentity
es2226Alarm = _Es2226Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3)
)
_Es2226Event_ObjectIdentity = ObjectIdentity
es2226Event = _Es2226Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1)
)


class _Es2226EventNumber_Type(Integer32):
    """Custom type es2226EventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226EventNumber_Type.__name__ = "Integer32"
_Es2226EventNumber_Object = MibScalar
es2226EventNumber = _Es2226EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 1),
    _Es2226EventNumber_Type()
)
es2226EventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226EventNumber.setStatus("current")
_Es2226EventTable_Object = MibTable
es2226EventTable = _Es2226EventTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    es2226EventTable.setStatus("current")
_Es2226EventEntry_Object = MibTableRow
es2226EventEntry = _Es2226EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 2, 1)
)
es2226EventEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226EventIndex"),
)
if mibBuilder.loadTexts:
    es2226EventEntry.setStatus("current")


class _Es2226EventIndex_Type(Integer32):
    """Custom type es2226EventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226EventIndex_Type.__name__ = "Integer32"
_Es2226EventIndex_Object = MibTableColumn
es2226EventIndex = _Es2226EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 2, 1, 1),
    _Es2226EventIndex_Type()
)
es2226EventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226EventIndex.setStatus("current")
_Es2226EventName_Type = DisplayString
_Es2226EventName_Object = MibTableColumn
es2226EventName = _Es2226EventName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 2, 1, 2),
    _Es2226EventName_Type()
)
es2226EventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226EventName.setStatus("current")


class _Es2226EventSendEmail_Type(Integer32):
    """Custom type es2226EventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226EventSendEmail_Type.__name__ = "Integer32"
_Es2226EventSendEmail_Object = MibTableColumn
es2226EventSendEmail = _Es2226EventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 2, 1, 3),
    _Es2226EventSendEmail_Type()
)
es2226EventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EventSendEmail.setStatus("current")


class _Es2226EventSendTrap_Type(Integer32):
    """Custom type es2226EventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226EventSendTrap_Type.__name__ = "Integer32"
_Es2226EventSendTrap_Object = MibTableColumn
es2226EventSendTrap = _Es2226EventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 1, 2, 1, 4),
    _Es2226EventSendTrap_Type()
)
es2226EventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EventSendTrap.setStatus("current")
_Es2226Email_ObjectIdentity = ObjectIdentity
es2226Email = _Es2226Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2)
)
_Es2226EmailServer_Type = DisplayString
_Es2226EmailServer_Object = MibScalar
es2226EmailServer = _Es2226EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 1),
    _Es2226EmailServer_Type()
)
es2226EmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EmailServer.setStatus("current")
_Es2226EmailUsername_Type = DisplayString
_Es2226EmailUsername_Object = MibScalar
es2226EmailUsername = _Es2226EmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 2),
    _Es2226EmailUsername_Type()
)
es2226EmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EmailUsername.setStatus("current")
_Es2226EmailPassword_Type = DisplayString
_Es2226EmailPassword_Object = MibScalar
es2226EmailPassword = _Es2226EmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 3),
    _Es2226EmailPassword_Type()
)
es2226EmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EmailPassword.setStatus("current")
_Es2226EmailSender_Type = DisplayString
_Es2226EmailSender_Object = MibScalar
es2226EmailSender = _Es2226EmailSender_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 4),
    _Es2226EmailSender_Type()
)
es2226EmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EmailSender.setStatus("current")
_Es2226EmailReturnPath_Type = DisplayString
_Es2226EmailReturnPath_Object = MibScalar
es2226EmailReturnPath = _Es2226EmailReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 5),
    _Es2226EmailReturnPath_Type()
)
es2226EmailReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EmailReturnPath.setStatus("current")


class _Es2226EmailUserNumber_Type(Integer32):
    """Custom type es2226EmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2226EmailUserNumber_Type.__name__ = "Integer32"
_Es2226EmailUserNumber_Object = MibScalar
es2226EmailUserNumber = _Es2226EmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 6),
    _Es2226EmailUserNumber_Type()
)
es2226EmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226EmailUserNumber.setStatus("current")
_Es2226EmailUserTable_Object = MibTable
es2226EmailUserTable = _Es2226EmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    es2226EmailUserTable.setStatus("current")
_Es2226EmailUserEntry_Object = MibTableRow
es2226EmailUserEntry = _Es2226EmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 7, 1)
)
es2226EmailUserEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226EmailUserIndex"),
)
if mibBuilder.loadTexts:
    es2226EmailUserEntry.setStatus("current")


class _Es2226EmailUserIndex_Type(Integer32):
    """Custom type es2226EmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2226EmailUserIndex_Type.__name__ = "Integer32"
_Es2226EmailUserIndex_Object = MibTableColumn
es2226EmailUserIndex = _Es2226EmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 7, 1, 1),
    _Es2226EmailUserIndex_Type()
)
es2226EmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226EmailUserIndex.setStatus("current")
_Es2226EmailUserAddress_Type = DisplayString
_Es2226EmailUserAddress_Object = MibTableColumn
es2226EmailUserAddress = _Es2226EmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 3, 2, 7, 1, 2),
    _Es2226EmailUserAddress_Type()
)
es2226EmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226EmailUserAddress.setStatus("current")
_Es2226Tftp_ObjectIdentity = ObjectIdentity
es2226Tftp = _Es2226Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 4)
)
_Es2226TftpServer_Type = IpAddress
_Es2226TftpServer_Object = MibScalar
es2226TftpServer = _Es2226TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 4, 1),
    _Es2226TftpServer_Type()
)
es2226TftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TftpServer.setStatus("current")
_Es2226Configuration_ObjectIdentity = ObjectIdentity
es2226Configuration = _Es2226Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5)
)
_Es2226SaveRestore_ObjectIdentity = ObjectIdentity
es2226SaveRestore = _Es2226SaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 1)
)


class _Es2226SaveStart_Type(Integer32):
    """Custom type es2226SaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226SaveStart_Type.__name__ = "Integer32"
_Es2226SaveStart_Object = MibScalar
es2226SaveStart = _Es2226SaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 1, 1),
    _Es2226SaveStart_Type()
)
es2226SaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226SaveStart.setStatus("current")


class _Es2226SaveUser_Type(Integer32):
    """Custom type es2226SaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226SaveUser_Type.__name__ = "Integer32"
_Es2226SaveUser_Object = MibScalar
es2226SaveUser = _Es2226SaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 1, 2),
    _Es2226SaveUser_Type()
)
es2226SaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226SaveUser.setStatus("current")


class _Es2226RestoreDefault_Type(Integer32):
    """Custom type es2226RestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2226RestoreDefault_Type.__name__ = "Integer32"
_Es2226RestoreDefault_Object = MibScalar
es2226RestoreDefault = _Es2226RestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 1, 3),
    _Es2226RestoreDefault_Type()
)
es2226RestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RestoreDefault.setStatus("current")


class _Es2226RestoreUser_Type(Integer32):
    """Custom type es2226RestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226RestoreUser_Type.__name__ = "Integer32"
_Es2226RestoreUser_Object = MibScalar
es2226RestoreUser = _Es2226RestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 1, 4),
    _Es2226RestoreUser_Type()
)
es2226RestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RestoreUser.setStatus("current")
_Es2226ConfigFile_ObjectIdentity = ObjectIdentity
es2226ConfigFile = _Es2226ConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 2)
)
_Es2226ExportConfigName_Type = DisplayString
_Es2226ExportConfigName_Object = MibScalar
es2226ExportConfigName = _Es2226ExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 2, 1),
    _Es2226ExportConfigName_Type()
)
es2226ExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ExportConfigName.setStatus("current")


class _Es2226DoExportConfig_Type(Integer32):
    """Custom type es2226DoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2226DoExportConfig_Type.__name__ = "Integer32"
_Es2226DoExportConfig_Object = MibScalar
es2226DoExportConfig = _Es2226DoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 2, 2),
    _Es2226DoExportConfig_Type()
)
es2226DoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DoExportConfig.setStatus("current")
_Es2226ImportConfigName_Type = DisplayString
_Es2226ImportConfigName_Object = MibScalar
es2226ImportConfigName = _Es2226ImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 2, 3),
    _Es2226ImportConfigName_Type()
)
es2226ImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ImportConfigName.setStatus("current")


class _Es2226DoImportConfig_Type(Integer32):
    """Custom type es2226DoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2226DoImportConfig_Type.__name__ = "Integer32"
_Es2226DoImportConfig_Object = MibScalar
es2226DoImportConfig = _Es2226DoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 5, 2, 4),
    _Es2226DoImportConfig_Type()
)
es2226DoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DoImportConfig.setStatus("current")
_Es2226Diagnostic_ObjectIdentity = ObjectIdentity
es2226Diagnostic = _Es2226Diagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6)
)
_Es2226EEPROMTest_Type = DisplayString
_Es2226EEPROMTest_Object = MibScalar
es2226EEPROMTest = _Es2226EEPROMTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 1),
    _Es2226EEPROMTest_Type()
)
es2226EEPROMTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226EEPROMTest.setStatus("current")
_Es2226UartTest_Type = DisplayString
_Es2226UartTest_Object = MibScalar
es2226UartTest = _Es2226UartTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 2),
    _Es2226UartTest_Type()
)
es2226UartTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226UartTest.setStatus("current")
_Es2226DramTest_Type = DisplayString
_Es2226DramTest_Object = MibScalar
es2226DramTest = _Es2226DramTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 3),
    _Es2226DramTest_Type()
)
es2226DramTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DramTest.setStatus("current")
_Es2226FlashTest_Type = DisplayString
_Es2226FlashTest_Object = MibScalar
es2226FlashTest = _Es2226FlashTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 4),
    _Es2226FlashTest_Type()
)
es2226FlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226FlashTest.setStatus("current")
_Es2226InternalLoopbackTest_Type = DisplayString
_Es2226InternalLoopbackTest_Object = MibScalar
es2226InternalLoopbackTest = _Es2226InternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 5),
    _Es2226InternalLoopbackTest_Type()
)
es2226InternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226InternalLoopbackTest.setStatus("current")
_Es2226ExternalLoopbackTest_Type = DisplayString
_Es2226ExternalLoopbackTest_Object = MibScalar
es2226ExternalLoopbackTest = _Es2226ExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 6),
    _Es2226ExternalLoopbackTest_Type()
)
es2226ExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226ExternalLoopbackTest.setStatus("current")
_Es2226PingTest_Type = DisplayString
_Es2226PingTest_Object = MibScalar
es2226PingTest = _Es2226PingTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 6, 7),
    _Es2226PingTest_Type()
)
es2226PingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PingTest.setStatus("current")
_Es2226Log_ObjectIdentity = ObjectIdentity
es2226Log = _Es2226Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7)
)


class _Es2226ClearLog_Type(Integer32):
    """Custom type es2226ClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226ClearLog_Type.__name__ = "Integer32"
_Es2226ClearLog_Object = MibScalar
es2226ClearLog = _Es2226ClearLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 1),
    _Es2226ClearLog_Type()
)
es2226ClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ClearLog.setStatus("current")


class _Es2226UploadLog_Type(Integer32):
    """Custom type es2226UploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226UploadLog_Type.__name__ = "Integer32"
_Es2226UploadLog_Object = MibScalar
es2226UploadLog = _Es2226UploadLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 2),
    _Es2226UploadLog_Type()
)
es2226UploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226UploadLog.setStatus("current")


class _Es2226AutoUploadLogState_Type(Integer32):
    """Custom type es2226AutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226AutoUploadLogState_Type.__name__ = "Integer32"
_Es2226AutoUploadLogState_Object = MibScalar
es2226AutoUploadLogState = _Es2226AutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 3),
    _Es2226AutoUploadLogState_Type()
)
es2226AutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AutoUploadLogState.setStatus("current")


class _Es2226LogNumber_Type(Integer32):
    """Custom type es2226LogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2226LogNumber_Type.__name__ = "Integer32"
_Es2226LogNumber_Object = MibScalar
es2226LogNumber = _Es2226LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 4),
    _Es2226LogNumber_Type()
)
es2226LogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LogNumber.setStatus("current")
_Es2226LogTable_Object = MibTable
es2226LogTable = _Es2226LogTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 5)
)
if mibBuilder.loadTexts:
    es2226LogTable.setStatus("current")
_Es2226LogEntry_Object = MibTableRow
es2226LogEntry = _Es2226LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 5, 1)
)
es2226LogEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226LogIndex"),
)
if mibBuilder.loadTexts:
    es2226LogEntry.setStatus("current")


class _Es2226LogIndex_Type(Integer32):
    """Custom type es2226LogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Es2226LogIndex_Type.__name__ = "Integer32"
_Es2226LogIndex_Object = MibTableColumn
es2226LogIndex = _Es2226LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 5, 1, 1),
    _Es2226LogIndex_Type()
)
es2226LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LogIndex.setStatus("current")
_Es2226LogEvent_Type = DisplayString
_Es2226LogEvent_Object = MibTableColumn
es2226LogEvent = _Es2226LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 7, 5, 1, 2),
    _Es2226LogEvent_Type()
)
es2226LogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LogEvent.setStatus("current")
_Es2226Firmware_ObjectIdentity = ObjectIdentity
es2226Firmware = _Es2226Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 8)
)
_Es2226FirmwareFileName_Type = DisplayString
_Es2226FirmwareFileName_Object = MibScalar
es2226FirmwareFileName = _Es2226FirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 8, 1),
    _Es2226FirmwareFileName_Type()
)
es2226FirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226FirmwareFileName.setStatus("current")


class _Es2226DoFirmwareUpgrade_Type(Integer32):
    """Custom type es2226DoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DoFirmwareUpgrade_Type.__name__ = "Integer32"
_Es2226DoFirmwareUpgrade_Object = MibScalar
es2226DoFirmwareUpgrade = _Es2226DoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 8, 2),
    _Es2226DoFirmwareUpgrade_Type()
)
es2226DoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DoFirmwareUpgrade.setStatus("current")
_Es2226Port_ObjectIdentity = ObjectIdentity
es2226Port = _Es2226Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9)
)
_Es2226PortStatus_ObjectIdentity = ObjectIdentity
es2226PortStatus = _Es2226PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1)
)


class _Es2226PortStatusNumber_Type(Integer32):
    """Custom type es2226PortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortStatusNumber_Type.__name__ = "Integer32"
_Es2226PortStatusNumber_Object = MibScalar
es2226PortStatusNumber = _Es2226PortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 1),
    _Es2226PortStatusNumber_Type()
)
es2226PortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusNumber.setStatus("current")
_Es2226PortStatusTable_Object = MibTable
es2226PortStatusTable = _Es2226PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    es2226PortStatusTable.setStatus("current")
_Es2226PortStatusEntry_Object = MibTableRow
es2226PortStatusEntry = _Es2226PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1)
)
es2226PortStatusEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226PortStatusIndex"),
)
if mibBuilder.loadTexts:
    es2226PortStatusEntry.setStatus("current")


class _Es2226PortStatusIndex_Type(Integer32):
    """Custom type es2226PortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortStatusIndex_Type.__name__ = "Integer32"
_Es2226PortStatusIndex_Object = MibTableColumn
es2226PortStatusIndex = _Es2226PortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 1),
    _Es2226PortStatusIndex_Type()
)
es2226PortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusIndex.setStatus("current")
_Es2226PortStatusMedia_Type = DisplayString
_Es2226PortStatusMedia_Object = MibTableColumn
es2226PortStatusMedia = _Es2226PortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 2),
    _Es2226PortStatusMedia_Type()
)
es2226PortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusMedia.setStatus("current")
_Es2226PortStatusLink_Type = DisplayString
_Es2226PortStatusLink_Object = MibTableColumn
es2226PortStatusLink = _Es2226PortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 3),
    _Es2226PortStatusLink_Type()
)
es2226PortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusLink.setStatus("current")
_Es2226PortStatusPortState_Type = DisplayString
_Es2226PortStatusPortState_Object = MibTableColumn
es2226PortStatusPortState = _Es2226PortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 4),
    _Es2226PortStatusPortState_Type()
)
es2226PortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusPortState.setStatus("current")
_Es2226PortStatusAutoNego_Type = DisplayString
_Es2226PortStatusAutoNego_Object = MibTableColumn
es2226PortStatusAutoNego = _Es2226PortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 5),
    _Es2226PortStatusAutoNego_Type()
)
es2226PortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusAutoNego.setStatus("current")
_Es2226PortStatusSpdDpx_Type = DisplayString
_Es2226PortStatusSpdDpx_Object = MibTableColumn
es2226PortStatusSpdDpx = _Es2226PortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 6),
    _Es2226PortStatusSpdDpx_Type()
)
es2226PortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusSpdDpx.setStatus("current")
_Es2226PortStatusRxPause_Type = DisplayString
_Es2226PortStatusRxPause_Object = MibTableColumn
es2226PortStatusRxPause = _Es2226PortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 7),
    _Es2226PortStatusRxPause_Type()
)
es2226PortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusRxPause.setStatus("current")
_Es2226PortStatusTxPause_Type = DisplayString
_Es2226PortStatusTxPause_Object = MibTableColumn
es2226PortStatusTxPause = _Es2226PortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 8),
    _Es2226PortStatusTxPause_Type()
)
es2226PortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusTxPause.setStatus("current")
_Es2226PortStatusDescription_Type = DisplayString
_Es2226PortStatusDescription_Object = MibTableColumn
es2226PortStatusDescription = _Es2226PortStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 1, 2, 1, 9),
    _Es2226PortStatusDescription_Type()
)
es2226PortStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortStatusDescription.setStatus("current")
_Es2226PortConf_ObjectIdentity = ObjectIdentity
es2226PortConf = _Es2226PortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2)
)


class _Es2226PortConfNumber_Type(Integer32):
    """Custom type es2226PortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortConfNumber_Type.__name__ = "Integer32"
_Es2226PortConfNumber_Object = MibScalar
es2226PortConfNumber = _Es2226PortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 1),
    _Es2226PortConfNumber_Type()
)
es2226PortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortConfNumber.setStatus("current")
_Es2226PortConfTable_Object = MibTable
es2226PortConfTable = _Es2226PortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    es2226PortConfTable.setStatus("current")
_Es2226PortConfEntry_Object = MibTableRow
es2226PortConfEntry = _Es2226PortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1)
)
es2226PortConfEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226PortConfIndex"),
)
if mibBuilder.loadTexts:
    es2226PortConfEntry.setStatus("current")


class _Es2226PortConfIndex_Type(Integer32):
    """Custom type es2226PortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortConfIndex_Type.__name__ = "Integer32"
_Es2226PortConfIndex_Object = MibTableColumn
es2226PortConfIndex = _Es2226PortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1, 1),
    _Es2226PortConfIndex_Type()
)
es2226PortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortConfIndex.setStatus("current")


class _Es2226PortConfPortState_Type(Integer32):
    """Custom type es2226PortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226PortConfPortState_Type.__name__ = "Integer32"
_Es2226PortConfPortState_Object = MibTableColumn
es2226PortConfPortState = _Es2226PortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1, 2),
    _Es2226PortConfPortState_Type()
)
es2226PortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortConfPortState.setStatus("current")


class _Es2226PortConfSpdDpx_Type(Integer32):
    """Custom type es2226PortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Es2226PortConfSpdDpx_Type.__name__ = "Integer32"
_Es2226PortConfSpdDpx_Object = MibTableColumn
es2226PortConfSpdDpx = _Es2226PortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1, 3),
    _Es2226PortConfSpdDpx_Type()
)
es2226PortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortConfSpdDpx.setStatus("current")


class _Es2226PortConfFlwCtrl_Type(Integer32):
    """Custom type es2226PortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Es2226PortConfFlwCtrl_Type.__name__ = "Integer32"
_Es2226PortConfFlwCtrl_Object = MibTableColumn
es2226PortConfFlwCtrl = _Es2226PortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1, 4),
    _Es2226PortConfFlwCtrl_Type()
)
es2226PortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortConfFlwCtrl.setStatus("current")


class _Es2226PortConfPowerSaving_Type(Integer32):
    """Custom type es2226PortConfPowerSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226PortConfPowerSaving_Type.__name__ = "Integer32"
_Es2226PortConfPowerSaving_Object = MibTableColumn
es2226PortConfPowerSaving = _Es2226PortConfPowerSaving_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1, 5),
    _Es2226PortConfPowerSaving_Type()
)
es2226PortConfPowerSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortConfPowerSaving.setStatus("current")
_Es2226PortConfDescription_Type = DisplayString
_Es2226PortConfDescription_Object = MibTableColumn
es2226PortConfDescription = _Es2226PortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 2, 2, 1, 6),
    _Es2226PortConfDescription_Type()
)
es2226PortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortConfDescription.setStatus("current")
_Es2226PortBandwidth_ObjectIdentity = ObjectIdentity
es2226PortBandwidth = _Es2226PortBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3)
)


class _Es2226PortBandwidthNumber_Type(Integer32):
    """Custom type es2226PortBandwidthNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortBandwidthNumber_Type.__name__ = "Integer32"
_Es2226PortBandwidthNumber_Object = MibScalar
es2226PortBandwidthNumber = _Es2226PortBandwidthNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 1),
    _Es2226PortBandwidthNumber_Type()
)
es2226PortBandwidthNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortBandwidthNumber.setStatus("current")
_Es2226PortBandwidthTable_Object = MibTable
es2226PortBandwidthTable = _Es2226PortBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    es2226PortBandwidthTable.setStatus("current")
_Es2226PortBandwidthEntry_Object = MibTableRow
es2226PortBandwidthEntry = _Es2226PortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2, 1)
)
es2226PortBandwidthEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226PortBandwidthIndex"),
)
if mibBuilder.loadTexts:
    es2226PortBandwidthEntry.setStatus("current")


class _Es2226PortBandwidthIndex_Type(Integer32):
    """Custom type es2226PortBandwidthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226PortBandwidthIndex_Type.__name__ = "Integer32"
_Es2226PortBandwidthIndex_Object = MibTableColumn
es2226PortBandwidthIndex = _Es2226PortBandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2, 1, 1),
    _Es2226PortBandwidthIndex_Type()
)
es2226PortBandwidthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortBandwidthIndex.setStatus("current")


class _Es2226PortBandwidthIngressRate_Type(Integer32):
    """Custom type es2226PortBandwidthIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_Es2226PortBandwidthIngressRate_Type.__name__ = "Integer32"
_Es2226PortBandwidthIngressRate_Object = MibTableColumn
es2226PortBandwidthIngressRate = _Es2226PortBandwidthIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2, 1, 2),
    _Es2226PortBandwidthIngressRate_Type()
)
es2226PortBandwidthIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBandwidthIngressRate.setStatus("current")


class _Es2226PortBandwidthEgressRate_Type(Integer32):
    """Custom type es2226PortBandwidthEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_Es2226PortBandwidthEgressRate_Type.__name__ = "Integer32"
_Es2226PortBandwidthEgressRate_Object = MibTableColumn
es2226PortBandwidthEgressRate = _Es2226PortBandwidthEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2, 1, 3),
    _Es2226PortBandwidthEgressRate_Type()
)
es2226PortBandwidthEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBandwidthEgressRate.setStatus("current")


class _Es2226PortBandwidthStormType_Type(Integer32):
    """Custom type es2226PortBandwidthStormType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226PortBandwidthStormType_Type.__name__ = "Integer32"
_Es2226PortBandwidthStormType_Object = MibTableColumn
es2226PortBandwidthStormType = _Es2226PortBandwidthStormType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2, 1, 4),
    _Es2226PortBandwidthStormType_Type()
)
es2226PortBandwidthStormType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBandwidthStormType.setStatus("current")


class _Es2226PortBandwidthStormRate_Type(Integer32):
    """Custom type es2226PortBandwidthStormRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_Es2226PortBandwidthStormRate_Type.__name__ = "Integer32"
_Es2226PortBandwidthStormRate_Object = MibTableColumn
es2226PortBandwidthStormRate = _Es2226PortBandwidthStormRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 3, 2, 1, 5),
    _Es2226PortBandwidthStormRate_Type()
)
es2226PortBandwidthStormRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBandwidthStormRate.setStatus("current")
_Es2226PortSFPInfo_ObjectIdentity = ObjectIdentity
es2226PortSFPInfo = _Es2226PortSFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4)
)


class _Es2226PortSFPInfoNumber_Type(Integer32):
    """Custom type es2226PortSFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortSFPInfoNumber_Type.__name__ = "Integer32"
_Es2226PortSFPInfoNumber_Object = MibScalar
es2226PortSFPInfoNumber = _Es2226PortSFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 1),
    _Es2226PortSFPInfoNumber_Type()
)
es2226PortSFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPInfoNumber.setStatus("current")
_Es2226PortSFPInfoTable_Object = MibTable
es2226PortSFPInfoTable = _Es2226PortSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    es2226PortSFPInfoTable.setStatus("current")
_Es2226PortSFPInfoEntry_Object = MibTableRow
es2226PortSFPInfoEntry = _Es2226PortSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1)
)
es2226PortSFPInfoEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226PortSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    es2226PortSFPInfoEntry.setStatus("current")


class _Es2226PortSFPInfoIndex_Type(Integer32):
    """Custom type es2226PortSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226PortSFPInfoIndex_Type.__name__ = "Integer32"
_Es2226PortSFPInfoIndex_Object = MibTableColumn
es2226PortSFPInfoIndex = _Es2226PortSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 1),
    _Es2226PortSFPInfoIndex_Type()
)
es2226PortSFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPInfoIndex.setStatus("current")
_Es2226PortSFPConnectorType_Type = DisplayString
_Es2226PortSFPConnectorType_Object = MibTableColumn
es2226PortSFPConnectorType = _Es2226PortSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 2),
    _Es2226PortSFPConnectorType_Type()
)
es2226PortSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPConnectorType.setStatus("current")
_Es2226PortSFPFiberType_Type = DisplayString
_Es2226PortSFPFiberType_Object = MibTableColumn
es2226PortSFPFiberType = _Es2226PortSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 3),
    _Es2226PortSFPFiberType_Type()
)
es2226PortSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPFiberType.setStatus("current")
_Es2226PortSFPWavelength_Type = DisplayString
_Es2226PortSFPWavelength_Object = MibTableColumn
es2226PortSFPWavelength = _Es2226PortSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 4),
    _Es2226PortSFPWavelength_Type()
)
es2226PortSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPWavelength.setStatus("current")
_Es2226PortSFPBaudRate_Type = DisplayString
_Es2226PortSFPBaudRate_Object = MibTableColumn
es2226PortSFPBaudRate = _Es2226PortSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 5),
    _Es2226PortSFPBaudRate_Type()
)
es2226PortSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPBaudRate.setStatus("current")
_Es2226PortSFPVendorOUI_Type = DisplayString
_Es2226PortSFPVendorOUI_Object = MibTableColumn
es2226PortSFPVendorOUI = _Es2226PortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 6),
    _Es2226PortSFPVendorOUI_Type()
)
es2226PortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPVendorOUI.setStatus("current")
_Es2226PortSFPVendorName_Type = DisplayString
_Es2226PortSFPVendorName_Object = MibTableColumn
es2226PortSFPVendorName = _Es2226PortSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 7),
    _Es2226PortSFPVendorName_Type()
)
es2226PortSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPVendorName.setStatus("current")
_Es2226PortSFPVendorPN_Type = DisplayString
_Es2226PortSFPVendorPN_Object = MibTableColumn
es2226PortSFPVendorPN = _Es2226PortSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 8),
    _Es2226PortSFPVendorPN_Type()
)
es2226PortSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPVendorPN.setStatus("current")
_Es2226PortSFPVendorRev_Type = DisplayString
_Es2226PortSFPVendorRev_Object = MibTableColumn
es2226PortSFPVendorRev = _Es2226PortSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 9),
    _Es2226PortSFPVendorRev_Type()
)
es2226PortSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPVendorRev.setStatus("current")
_Es2226PortSFPVendorSN_Type = DisplayString
_Es2226PortSFPVendorSN_Object = MibTableColumn
es2226PortSFPVendorSN = _Es2226PortSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 10),
    _Es2226PortSFPVendorSN_Type()
)
es2226PortSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPVendorSN.setStatus("current")
_Es2226PortSFPDateCode_Type = DisplayString
_Es2226PortSFPDateCode_Object = MibTableColumn
es2226PortSFPDateCode = _Es2226PortSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 11),
    _Es2226PortSFPDateCode_Type()
)
es2226PortSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPDateCode.setStatus("current")
_Es2226PortSFPTemperature_Type = DisplayString
_Es2226PortSFPTemperature_Object = MibTableColumn
es2226PortSFPTemperature = _Es2226PortSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 12),
    _Es2226PortSFPTemperature_Type()
)
es2226PortSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPTemperature.setStatus("current")
_Es2226PortSFPVcc_Type = DisplayString
_Es2226PortSFPVcc_Object = MibTableColumn
es2226PortSFPVcc = _Es2226PortSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 13),
    _Es2226PortSFPVcc_Type()
)
es2226PortSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPVcc.setStatus("current")
_Es2226PortSFPTxBias_Type = DisplayString
_Es2226PortSFPTxBias_Object = MibTableColumn
es2226PortSFPTxBias = _Es2226PortSFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 14),
    _Es2226PortSFPTxBias_Type()
)
es2226PortSFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPTxBias.setStatus("current")
_Es2226PortSFPTxPWR_Type = DisplayString
_Es2226PortSFPTxPWR_Object = MibTableColumn
es2226PortSFPTxPWR = _Es2226PortSFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 15),
    _Es2226PortSFPTxPWR_Type()
)
es2226PortSFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPTxPWR.setStatus("current")
_Es2226PortSFPRxPWR_Type = DisplayString
_Es2226PortSFPRxPWR_Object = MibTableColumn
es2226PortSFPRxPWR = _Es2226PortSFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 9, 4, 2, 1, 16),
    _Es2226PortSFPRxPWR_Type()
)
es2226PortSFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortSFPRxPWR.setStatus("current")
_Es2226LoopDetectedConf_ObjectIdentity = ObjectIdentity
es2226LoopDetectedConf = _Es2226LoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10)
)


class _Es2226LoopDetectedNumber_Type(Integer32):
    """Custom type es2226LoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226LoopDetectedNumber_Type.__name__ = "Integer32"
_Es2226LoopDetectedNumber_Object = MibScalar
es2226LoopDetectedNumber = _Es2226LoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 1),
    _Es2226LoopDetectedNumber_Type()
)
es2226LoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LoopDetectedNumber.setStatus("current")
_Es2226LoopDetectedTable_Object = MibTable
es2226LoopDetectedTable = _Es2226LoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 2)
)
if mibBuilder.loadTexts:
    es2226LoopDetectedTable.setStatus("current")
_Es2226LoopDetectedEntry_Object = MibTableRow
es2226LoopDetectedEntry = _Es2226LoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 2, 1)
)
es2226LoopDetectedEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226LoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    es2226LoopDetectedEntry.setStatus("current")


class _Es2226LoopDetectedfIndex_Type(Integer32):
    """Custom type es2226LoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226LoopDetectedfIndex_Type.__name__ = "Integer32"
_Es2226LoopDetectedfIndex_Object = MibTableColumn
es2226LoopDetectedfIndex = _Es2226LoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 2, 1, 1),
    _Es2226LoopDetectedfIndex_Type()
)
es2226LoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LoopDetectedfIndex.setStatus("current")


class _Es2226LoopDetectedStateEbl_Type(Integer32):
    """Custom type es2226LoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LoopDetectedStateEbl_Type.__name__ = "Integer32"
_Es2226LoopDetectedStateEbl_Object = MibTableColumn
es2226LoopDetectedStateEbl = _Es2226LoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 2, 1, 2),
    _Es2226LoopDetectedStateEbl_Type()
)
es2226LoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LoopDetectedStateEbl.setStatus("current")


class _Es2226LoopDetectedCurrentStatus_Type(Integer32):
    """Custom type es2226LoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_Es2226LoopDetectedCurrentStatus_Object = MibTableColumn
es2226LoopDetectedCurrentStatus = _Es2226LoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 2, 1, 3),
    _Es2226LoopDetectedCurrentStatus_Type()
)
es2226LoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LoopDetectedCurrentStatus.setStatus("current")


class _Es2226LoopDetectedResumed_Type(Integer32):
    """Custom type es2226LoopDetectedResumed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LoopDetectedResumed_Type.__name__ = "Integer32"
_Es2226LoopDetectedResumed_Object = MibTableColumn
es2226LoopDetectedResumed = _Es2226LoopDetectedResumed_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 2, 1, 4),
    _Es2226LoopDetectedResumed_Type()
)
es2226LoopDetectedResumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LoopDetectedResumed.setStatus("current")


class _Es2226LoopDetectedAction_Type(Integer32):
    """Custom type es2226LoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LoopDetectedAction_Type.__name__ = "Integer32"
_Es2226LoopDetectedAction_Object = MibScalar
es2226LoopDetectedAction = _Es2226LoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 10, 3),
    _Es2226LoopDetectedAction_Type()
)
es2226LoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LoopDetectedAction.setStatus("current")
_Es2226IpMacBind_ObjectIdentity = ObjectIdentity
es2226IpMacBind = _Es2226IpMacBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11)
)
_Es2226IpMacBindStatus_ObjectIdentity = ObjectIdentity
es2226IpMacBindStatus = _Es2226IpMacBindStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1)
)


class _Es2226IpMacBindMode_Type(Integer32):
    """Custom type es2226IpMacBindMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IpMacBindMode_Type.__name__ = "Integer32"
_Es2226IpMacBindMode_Object = MibScalar
es2226IpMacBindMode = _Es2226IpMacBindMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 1),
    _Es2226IpMacBindMode_Type()
)
es2226IpMacBindMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindMode.setStatus("current")
_Es2226IpMacBindPort_Type = DisplayString
_Es2226IpMacBindPort_Object = MibScalar
es2226IpMacBindPort = _Es2226IpMacBindPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 2),
    _Es2226IpMacBindPort_Type()
)
es2226IpMacBindPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindPort.setStatus("current")


class _Es2226IpMacBindCount_Type(Integer32):
    """Custom type es2226IpMacBindCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Es2226IpMacBindCount_Type.__name__ = "Integer32"
_Es2226IpMacBindCount_Object = MibScalar
es2226IpMacBindCount = _Es2226IpMacBindCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 3),
    _Es2226IpMacBindCount_Type()
)
es2226IpMacBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226IpMacBindCount.setStatus("current")


class _Es2226IpMacBindCreatStatus_Type(Integer32):
    """Custom type es2226IpMacBindCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IpMacBindCreatStatus_Type.__name__ = "Integer32"
_Es2226IpMacBindCreatStatus_Object = MibScalar
es2226IpMacBindCreatStatus = _Es2226IpMacBindCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 4),
    _Es2226IpMacBindCreatStatus_Type()
)
es2226IpMacBindCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindCreatStatus.setStatus("current")
_Es2226IpMacBindStatusTable_Object = MibTable
es2226IpMacBindStatusTable = _Es2226IpMacBindStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5)
)
if mibBuilder.loadTexts:
    es2226IpMacBindStatusTable.setStatus("current")
_Es2226IpMacBindStatusEntry_Object = MibTableRow
es2226IpMacBindStatusEntry = _Es2226IpMacBindStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1)
)
es2226IpMacBindStatusEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226IpMacBindStatusIndex"),
)
if mibBuilder.loadTexts:
    es2226IpMacBindStatusEntry.setStatus("current")


class _Es2226IpMacBindStatusIndex_Type(Integer32):
    """Custom type es2226IpMacBindStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2226IpMacBindStatusIndex_Type.__name__ = "Integer32"
_Es2226IpMacBindStatusIndex_Object = MibTableColumn
es2226IpMacBindStatusIndex = _Es2226IpMacBindStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 1),
    _Es2226IpMacBindStatusIndex_Type()
)
es2226IpMacBindStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusIndex.setStatus("current")
_Es2226IpMacBindStatusName_Type = DisplayString
_Es2226IpMacBindStatusName_Object = MibTableColumn
es2226IpMacBindStatusName = _Es2226IpMacBindStatusName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 2),
    _Es2226IpMacBindStatusName_Type()
)
es2226IpMacBindStatusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusName.setStatus("current")
_Es2226IpMacBindStatusMac_Type = DisplayString
_Es2226IpMacBindStatusMac_Object = MibTableColumn
es2226IpMacBindStatusMac = _Es2226IpMacBindStatusMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 3),
    _Es2226IpMacBindStatusMac_Type()
)
es2226IpMacBindStatusMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusMac.setStatus("current")
_Es2226IpMacBindStatusIp_Type = IpAddress
_Es2226IpMacBindStatusIp_Object = MibTableColumn
es2226IpMacBindStatusIp = _Es2226IpMacBindStatusIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 4),
    _Es2226IpMacBindStatusIp_Type()
)
es2226IpMacBindStatusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusIp.setStatus("current")
_Es2226IpMacBindStatusPort_Type = DisplayString
_Es2226IpMacBindStatusPort_Object = MibTableColumn
es2226IpMacBindStatusPort = _Es2226IpMacBindStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 5),
    _Es2226IpMacBindStatusPort_Type()
)
es2226IpMacBindStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusPort.setStatus("current")


class _Es2226IpMacBindStatusBindingMethod_Type(Integer32):
    """Custom type es2226IpMacBindStatusBindingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IpMacBindStatusBindingMethod_Type.__name__ = "Integer32"
_Es2226IpMacBindStatusBindingMethod_Object = MibTableColumn
es2226IpMacBindStatusBindingMethod = _Es2226IpMacBindStatusBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 6),
    _Es2226IpMacBindStatusBindingMethod_Type()
)
es2226IpMacBindStatusBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusBindingMethod.setStatus("current")


class _Es2226IpMacBindStatusType_Type(Integer32):
    """Custom type es2226IpMacBindStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IpMacBindStatusType_Type.__name__ = "Integer32"
_Es2226IpMacBindStatusType_Object = MibTableColumn
es2226IpMacBindStatusType = _Es2226IpMacBindStatusType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 7),
    _Es2226IpMacBindStatusType_Type()
)
es2226IpMacBindStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusType.setStatus("current")


class _Es2226IpMacBindStatusRowStatus_Type(Integer32):
    """Custom type es2226IpMacBindStatusRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226IpMacBindStatusRowStatus_Type.__name__ = "Integer32"
_Es2226IpMacBindStatusRowStatus_Object = MibTableColumn
es2226IpMacBindStatusRowStatus = _Es2226IpMacBindStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 11, 1, 5, 1, 8),
    _Es2226IpMacBindStatusRowStatus_Type()
)
es2226IpMacBindStatusRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IpMacBindStatusRowStatus.setStatus("current")
_Es2226MacTableInfo_ObjectIdentity = ObjectIdentity
es2226MacTableInfo = _Es2226MacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12)
)
_Es2226MacTableMaintenance_ObjectIdentity = ObjectIdentity
es2226MacTableMaintenance = _Es2226MacTableMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1)
)


class _Es2226MacTableAgingTime_Type(Integer32):
    """Custom type es2226MacTableAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_Es2226MacTableAgingTime_Type.__name__ = "Integer32"
_Es2226MacTableAgingTime_Object = MibScalar
es2226MacTableAgingTime = _Es2226MacTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1, 1),
    _Es2226MacTableAgingTime_Type()
)
es2226MacTableAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableAgingTime.setStatus("current")


class _Es2226MacTableFlush_Type(Integer32):
    """Custom type es2226MacTableFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226MacTableFlush_Type.__name__ = "Integer32"
_Es2226MacTableFlush_Object = MibScalar
es2226MacTableFlush = _Es2226MacTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1, 2),
    _Es2226MacTableFlush_Type()
)
es2226MacTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableFlush.setStatus("current")
_Es2226MacTableLearnPortLimitTable_Object = MibTable
es2226MacTableLearnPortLimitTable = _Es2226MacTableLearnPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1, 3)
)
if mibBuilder.loadTexts:
    es2226MacTableLearnPortLimitTable.setStatus("current")
_Es2226MacTableLearnPortLimitEntry_Object = MibTableRow
es2226MacTableLearnPortLimitEntry = _Es2226MacTableLearnPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1, 3, 1)
)
es2226MacTableLearnPortLimitEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226MacTableLearnPortLimitIndex"),
)
if mibBuilder.loadTexts:
    es2226MacTableLearnPortLimitEntry.setStatus("current")


class _Es2226MacTableLearnPortLimitIndex_Type(Integer32):
    """Custom type es2226MacTableLearnPortLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226MacTableLearnPortLimitIndex_Type.__name__ = "Integer32"
_Es2226MacTableLearnPortLimitIndex_Object = MibTableColumn
es2226MacTableLearnPortLimitIndex = _Es2226MacTableLearnPortLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1, 3, 1, 1),
    _Es2226MacTableLearnPortLimitIndex_Type()
)
es2226MacTableLearnPortLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MacTableLearnPortLimitIndex.setStatus("current")


class _Es2226MacTableLearnPortLimit_Type(Integer32):
    """Custom type es2226MacTableLearnPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_Es2226MacTableLearnPortLimit_Type.__name__ = "Integer32"
_Es2226MacTableLearnPortLimit_Object = MibTableColumn
es2226MacTableLearnPortLimit = _Es2226MacTableLearnPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 1, 3, 1, 2),
    _Es2226MacTableLearnPortLimit_Type()
)
es2226MacTableLearnPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableLearnPortLimit.setStatus("current")
_Es2226MacTableStaticMac_ObjectIdentity = ObjectIdentity
es2226MacTableStaticMac = _Es2226MacTableStaticMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2)
)


class _Es2226MacTableStaticMacCreatStatus_Type(Integer32):
    """Custom type es2226MacTableStaticMacCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226MacTableStaticMacCreatStatus_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacCreatStatus_Object = MibScalar
es2226MacTableStaticMacCreatStatus = _Es2226MacTableStaticMacCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 1),
    _Es2226MacTableStaticMacCreatStatus_Type()
)
es2226MacTableStaticMacCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacCreatStatus.setStatus("current")


class _Es2226MacTableStaticMacNumber_Type(Integer32):
    """Custom type es2226MacTableStaticMacNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2226MacTableStaticMacNumber_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacNumber_Object = MibScalar
es2226MacTableStaticMacNumber = _Es2226MacTableStaticMacNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 2),
    _Es2226MacTableStaticMacNumber_Type()
)
es2226MacTableStaticMacNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacNumber.setStatus("current")
_Es2226MacTableStaticMacTable_Object = MibTable
es2226MacTableStaticMacTable = _Es2226MacTableStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3)
)
if mibBuilder.loadTexts:
    es2226MacTableStaticMacTable.setStatus("current")
_Es2226MacTableStaticMacEntry_Object = MibTableRow
es2226MacTableStaticMacEntry = _Es2226MacTableStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1)
)
es2226MacTableStaticMacEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226MacTableStaticMacIndex"),
)
if mibBuilder.loadTexts:
    es2226MacTableStaticMacEntry.setStatus("current")


class _Es2226MacTableStaticMacIndex_Type(Integer32):
    """Custom type es2226MacTableStaticMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2226MacTableStaticMacIndex_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacIndex_Object = MibTableColumn
es2226MacTableStaticMacIndex = _Es2226MacTableStaticMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1, 1),
    _Es2226MacTableStaticMacIndex_Type()
)
es2226MacTableStaticMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacIndex.setStatus("current")
_Es2226MacTableStaticMacAddress_Type = DisplayString
_Es2226MacTableStaticMacAddress_Object = MibTableColumn
es2226MacTableStaticMacAddress = _Es2226MacTableStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1, 2),
    _Es2226MacTableStaticMacAddress_Type()
)
es2226MacTableStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacAddress.setStatus("current")


class _Es2226MacTableStaticMacVid_Type(Integer32):
    """Custom type es2226MacTableStaticMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226MacTableStaticMacVid_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacVid_Object = MibTableColumn
es2226MacTableStaticMacVid = _Es2226MacTableStaticMacVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1, 3),
    _Es2226MacTableStaticMacVid_Type()
)
es2226MacTableStaticMacVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacVid.setStatus("current")


class _Es2226MacTableStaticMacRule_Type(Integer32):
    """Custom type es2226MacTableStaticMacRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226MacTableStaticMacRule_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacRule_Object = MibTableColumn
es2226MacTableStaticMacRule = _Es2226MacTableStaticMacRule_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1, 4),
    _Es2226MacTableStaticMacRule_Type()
)
es2226MacTableStaticMacRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacRule.setStatus("current")


class _Es2226MacTableStaticMacPort_Type(Integer32):
    """Custom type es2226MacTableStaticMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226MacTableStaticMacPort_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacPort_Object = MibTableColumn
es2226MacTableStaticMacPort = _Es2226MacTableStaticMacPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1, 5),
    _Es2226MacTableStaticMacPort_Type()
)
es2226MacTableStaticMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacPort.setStatus("current")


class _Es2226MacTableStaticMacRowStatus_Type(Integer32):
    """Custom type es2226MacTableStaticMacRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226MacTableStaticMacRowStatus_Type.__name__ = "Integer32"
_Es2226MacTableStaticMacRowStatus_Object = MibTableColumn
es2226MacTableStaticMacRowStatus = _Es2226MacTableStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 2, 3, 1, 6),
    _Es2226MacTableStaticMacRowStatus_Type()
)
es2226MacTableStaticMacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableStaticMacRowStatus.setStatus("current")
_Es2226MacTableMacAlias_ObjectIdentity = ObjectIdentity
es2226MacTableMacAlias = _Es2226MacTableMacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3)
)


class _Es2226MacTableMacAliasCreatStatus_Type(Integer32):
    """Custom type es2226MacTableMacAliasCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226MacTableMacAliasCreatStatus_Type.__name__ = "Integer32"
_Es2226MacTableMacAliasCreatStatus_Object = MibScalar
es2226MacTableMacAliasCreatStatus = _Es2226MacTableMacAliasCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 1),
    _Es2226MacTableMacAliasCreatStatus_Type()
)
es2226MacTableMacAliasCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableMacAliasCreatStatus.setStatus("current")


class _Es2226MacTableMacAliasNumber_Type(Integer32):
    """Custom type es2226MacTableMacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2226MacTableMacAliasNumber_Type.__name__ = "Integer32"
_Es2226MacTableMacAliasNumber_Object = MibScalar
es2226MacTableMacAliasNumber = _Es2226MacTableMacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 2),
    _Es2226MacTableMacAliasNumber_Type()
)
es2226MacTableMacAliasNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableMacAliasNumber.setStatus("current")
_Es2226MacTableMacAliasTable_Object = MibTable
es2226MacTableMacAliasTable = _Es2226MacTableMacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 3)
)
if mibBuilder.loadTexts:
    es2226MacTableMacAliasTable.setStatus("current")
_Es2226MacTableMacAliasEntry_Object = MibTableRow
es2226MacTableMacAliasEntry = _Es2226MacTableMacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 3, 1)
)
es2226MacTableMacAliasEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226MacTableMacAliasIndex"),
)
if mibBuilder.loadTexts:
    es2226MacTableMacAliasEntry.setStatus("current")


class _Es2226MacTableMacAliasIndex_Type(Integer32):
    """Custom type es2226MacTableMacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2226MacTableMacAliasIndex_Type.__name__ = "Integer32"
_Es2226MacTableMacAliasIndex_Object = MibTableColumn
es2226MacTableMacAliasIndex = _Es2226MacTableMacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 3, 1, 1),
    _Es2226MacTableMacAliasIndex_Type()
)
es2226MacTableMacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226MacTableMacAliasIndex.setStatus("current")
_Es2226MacTableMacAliasAddress_Type = DisplayString
_Es2226MacTableMacAliasAddress_Object = MibTableColumn
es2226MacTableMacAliasAddress = _Es2226MacTableMacAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 3, 1, 2),
    _Es2226MacTableMacAliasAddress_Type()
)
es2226MacTableMacAliasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableMacAliasAddress.setStatus("current")
_Es2226MacTableMacAliasAlias_Type = DisplayString
_Es2226MacTableMacAliasAlias_Object = MibTableColumn
es2226MacTableMacAliasAlias = _Es2226MacTableMacAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 3, 1, 3),
    _Es2226MacTableMacAliasAlias_Type()
)
es2226MacTableMacAliasAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableMacAliasAlias.setStatus("current")


class _Es2226MacTableMacAliasRowStatus_Type(Integer32):
    """Custom type es2226MacTableMacAliasRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226MacTableMacAliasRowStatus_Type.__name__ = "Integer32"
_Es2226MacTableMacAliasRowStatus_Object = MibTableColumn
es2226MacTableMacAliasRowStatus = _Es2226MacTableMacAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 12, 3, 3, 1, 4),
    _Es2226MacTableMacAliasRowStatus_Type()
)
es2226MacTableMacAliasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MacTableMacAliasRowStatus.setStatus("current")
_Es2226Security_ObjectIdentity = ObjectIdentity
es2226Security = _Es2226Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13)
)
_Es2226Mirror_ObjectIdentity = ObjectIdentity
es2226Mirror = _Es2226Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 1)
)


class _Es2226MirrorMode_Type(Integer32):
    """Custom type es2226MirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226MirrorMode_Type.__name__ = "Integer32"
_Es2226MirrorMode_Object = MibScalar
es2226MirrorMode = _Es2226MirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 1, 1),
    _Es2226MirrorMode_Type()
)
es2226MirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MirrorMode.setStatus("current")


class _Es2226MonitoringPort_Type(Integer32):
    """Custom type es2226MonitoringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Es2226MonitoringPort_Type.__name__ = "Integer32"
_Es2226MonitoringPort_Object = MibScalar
es2226MonitoringPort = _Es2226MonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 1, 2),
    _Es2226MonitoringPort_Type()
)
es2226MonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MonitoringPort.setStatus("current")
_Es2226MonitoredIngressPort_Type = DisplayString
_Es2226MonitoredIngressPort_Object = MibScalar
es2226MonitoredIngressPort = _Es2226MonitoredIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 1, 3),
    _Es2226MonitoredIngressPort_Type()
)
es2226MonitoredIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MonitoredIngressPort.setStatus("current")
_Es2226MonitoredEgressPort_Type = DisplayString
_Es2226MonitoredEgressPort_Object = MibScalar
es2226MonitoredEgressPort = _Es2226MonitoredEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 1, 4),
    _Es2226MonitoredEgressPort_Type()
)
es2226MonitoredEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MonitoredEgressPort.setStatus("current")
_Es2226IsolatedGroup_ObjectIdentity = ObjectIdentity
es2226IsolatedGroup = _Es2226IsolatedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 2)
)
_Es2226IsolatedPortGroup_Type = DisplayString
_Es2226IsolatedPortGroup_Object = MibScalar
es2226IsolatedPortGroup = _Es2226IsolatedPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 2, 1),
    _Es2226IsolatedPortGroup_Type()
)
es2226IsolatedPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IsolatedPortGroup.setStatus("current")
_Es2226ArpProtect_ObjectIdentity = ObjectIdentity
es2226ArpProtect = _Es2226ArpProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 3)
)


class _Es2226ArpProtectPackerBurst_Type(Integer32):
    """Custom type es2226ArpProtectPackerBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Es2226ArpProtectPackerBurst_Type.__name__ = "Integer32"
_Es2226ArpProtectPackerBurst_Object = MibScalar
es2226ArpProtectPackerBurst = _Es2226ArpProtectPackerBurst_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 3, 1),
    _Es2226ArpProtectPackerBurst_Type()
)
es2226ArpProtectPackerBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ArpProtectPackerBurst.setStatus("current")


class _Es2226ArpProtectRatePerSec_Type(Integer32):
    """Custom type es2226ArpProtectRatePerSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 25600),
    )


_Es2226ArpProtectRatePerSec_Type.__name__ = "Integer32"
_Es2226ArpProtectRatePerSec_Object = MibScalar
es2226ArpProtectRatePerSec = _Es2226ArpProtectRatePerSec_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 13, 3, 2),
    _Es2226ArpProtectRatePerSec_Type()
)
es2226ArpProtectRatePerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ArpProtectRatePerSec.setStatus("current")
_Es2226VirtualStack_ObjectIdentity = ObjectIdentity
es2226VirtualStack = _Es2226VirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 14)
)


class _Es2226VirtualStackState_Type(Integer32):
    """Custom type es2226VirtualStackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226VirtualStackState_Type.__name__ = "Integer32"
_Es2226VirtualStackState_Object = MibScalar
es2226VirtualStackState = _Es2226VirtualStackState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 14, 1),
    _Es2226VirtualStackState_Type()
)
es2226VirtualStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VirtualStackState.setStatus("current")


class _Es2226VirtualStackRole_Type(Integer32):
    """Custom type es2226VirtualStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226VirtualStackRole_Type.__name__ = "Integer32"
_Es2226VirtualStackRole_Object = MibScalar
es2226VirtualStackRole = _Es2226VirtualStackRole_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 14, 2),
    _Es2226VirtualStackRole_Type()
)
es2226VirtualStackRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VirtualStackRole.setStatus("current")
_Es2226VirtualStackGroupID_Type = DisplayString
_Es2226VirtualStackGroupID_Object = MibScalar
es2226VirtualStackGroupID = _Es2226VirtualStackGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 14, 3),
    _Es2226VirtualStackGroupID_Type()
)
es2226VirtualStackGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VirtualStackGroupID.setStatus("current")
_Es2226ManagementSecurity_ObjectIdentity = ObjectIdentity
es2226ManagementSecurity = _Es2226ManagementSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15)
)


class _Es2226ManagementSecurityNumber_Type(Integer32):
    """Custom type es2226ManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2226ManagementSecurityNumber_Type.__name__ = "Integer32"
_Es2226ManagementSecurityNumber_Object = MibScalar
es2226ManagementSecurityNumber = _Es2226ManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 1),
    _Es2226ManagementSecurityNumber_Type()
)
es2226ManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226ManagementSecurityNumber.setStatus("current")


class _Es2226ManagementSecurityEntryCreate_Type(Integer32):
    """Custom type es2226ManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226ManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Es2226ManagementSecurityEntryCreate_Object = MibScalar
es2226ManagementSecurityEntryCreate = _Es2226ManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 2),
    _Es2226ManagementSecurityEntryCreate_Type()
)
es2226ManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityEntryCreate.setStatus("current")
_Es2226ManagementSecurityTable_Object = MibTable
es2226ManagementSecurityTable = _Es2226ManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3)
)
if mibBuilder.loadTexts:
    es2226ManagementSecurityTable.setStatus("current")
_Es2226ManagementSecurityEntry_Object = MibTableRow
es2226ManagementSecurityEntry = _Es2226ManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1)
)
es2226ManagementSecurityEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226ManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    es2226ManagementSecurityEntry.setStatus("current")


class _Es2226ManagementSecurityIndex_Type(Integer32):
    """Custom type es2226ManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2226ManagementSecurityIndex_Type.__name__ = "Integer32"
_Es2226ManagementSecurityIndex_Object = MibTableColumn
es2226ManagementSecurityIndex = _Es2226ManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 1),
    _Es2226ManagementSecurityIndex_Type()
)
es2226ManagementSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226ManagementSecurityIndex.setStatus("current")
_Es2226ManagementSecurityName_Type = DisplayString
_Es2226ManagementSecurityName_Object = MibTableColumn
es2226ManagementSecurityName = _Es2226ManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 2),
    _Es2226ManagementSecurityName_Type()
)
es2226ManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityName.setStatus("current")


class _Es2226ManagementSecurityVid_Type(Integer32):
    """Custom type es2226ManagementSecurityVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226ManagementSecurityVid_Type.__name__ = "Integer32"
_Es2226ManagementSecurityVid_Object = MibTableColumn
es2226ManagementSecurityVid = _Es2226ManagementSecurityVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 3),
    _Es2226ManagementSecurityVid_Type()
)
es2226ManagementSecurityVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityVid.setStatus("current")
_Es2226ManagementSecurityIpRange_Type = DisplayString
_Es2226ManagementSecurityIpRange_Object = MibTableColumn
es2226ManagementSecurityIpRange = _Es2226ManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 4),
    _Es2226ManagementSecurityIpRange_Type()
)
es2226ManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityIpRange.setStatus("current")
_Es2226ManagementSecurityIncomigPort_Type = DisplayString
_Es2226ManagementSecurityIncomigPort_Object = MibTableColumn
es2226ManagementSecurityIncomigPort = _Es2226ManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 5),
    _Es2226ManagementSecurityIncomigPort_Type()
)
es2226ManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityIncomigPort.setStatus("current")
_Es2226ManagementSecurityAccessType_Type = DisplayString
_Es2226ManagementSecurityAccessType_Object = MibTableColumn
es2226ManagementSecurityAccessType = _Es2226ManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 6),
    _Es2226ManagementSecurityAccessType_Type()
)
es2226ManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityAccessType.setStatus("current")


class _Es2226ManagementSecurityAction_Type(Integer32):
    """Custom type es2226ManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226ManagementSecurityAction_Type.__name__ = "Integer32"
_Es2226ManagementSecurityAction_Object = MibTableColumn
es2226ManagementSecurityAction = _Es2226ManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 7),
    _Es2226ManagementSecurityAction_Type()
)
es2226ManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityAction.setStatus("current")


class _Es2226ManagementSecurityRowStatus_Type(Integer32):
    """Custom type es2226ManagementSecurityRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226ManagementSecurityRowStatus_Type.__name__ = "Integer32"
_Es2226ManagementSecurityRowStatus_Object = MibTableColumn
es2226ManagementSecurityRowStatus = _Es2226ManagementSecurityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 15, 3, 1, 8),
    _Es2226ManagementSecurityRowStatus_Type()
)
es2226ManagementSecurityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementSecurityRowStatus.setStatus("current")
_Es2226QoS_ObjectIdentity = ObjectIdentity
es2226QoS = _Es2226QoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16)
)
_Es2226QoSGlobalConfig_ObjectIdentity = ObjectIdentity
es2226QoSGlobalConfig = _Es2226QoSGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1)
)


class _Es2226QoSMode_Type(Integer32):
    """Custom type es2226QoSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226QoSMode_Type.__name__ = "Integer32"
_Es2226QoSMode_Object = MibScalar
es2226QoSMode = _Es2226QoSMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 1),
    _Es2226QoSMode_Type()
)
es2226QoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSMode.setStatus("current")


class _Es2226QoS1PEnable_Type(Integer32):
    """Custom type es2226QoS1PEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226QoS1PEnable_Type.__name__ = "Integer32"
_Es2226QoS1PEnable_Object = MibScalar
es2226QoS1PEnable = _Es2226QoS1PEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 2),
    _Es2226QoS1PEnable_Type()
)
es2226QoS1PEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoS1PEnable.setStatus("current")


class _Es2226QoSDSCPEnable_Type(Integer32):
    """Custom type es2226QoSDSCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226QoSDSCPEnable_Type.__name__ = "Integer32"
_Es2226QoSDSCPEnable_Object = MibScalar
es2226QoSDSCPEnable = _Es2226QoSDSCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 3),
    _Es2226QoSDSCPEnable_Type()
)
es2226QoSDSCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSDSCPEnable.setStatus("current")


class _Es2226QoSSchedulingMethod_Type(Integer32):
    """Custom type es2226QoSSchedulingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226QoSSchedulingMethod_Type.__name__ = "Integer32"
_Es2226QoSSchedulingMethod_Object = MibScalar
es2226QoSSchedulingMethod = _Es2226QoSSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 4),
    _Es2226QoSSchedulingMethod_Type()
)
es2226QoSSchedulingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSSchedulingMethod.setStatus("current")


class _Es2226QoSWeightQ0_Type(Integer32):
    """Custom type es2226QoSWeightQ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2226QoSWeightQ0_Type.__name__ = "Integer32"
_Es2226QoSWeightQ0_Object = MibScalar
es2226QoSWeightQ0 = _Es2226QoSWeightQ0_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 5),
    _Es2226QoSWeightQ0_Type()
)
es2226QoSWeightQ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSWeightQ0.setStatus("current")


class _Es2226QoSWeightQ1_Type(Integer32):
    """Custom type es2226QoSWeightQ1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2226QoSWeightQ1_Type.__name__ = "Integer32"
_Es2226QoSWeightQ1_Object = MibScalar
es2226QoSWeightQ1 = _Es2226QoSWeightQ1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 6),
    _Es2226QoSWeightQ1_Type()
)
es2226QoSWeightQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSWeightQ1.setStatus("current")


class _Es2226QoSWeightQ2_Type(Integer32):
    """Custom type es2226QoSWeightQ2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2226QoSWeightQ2_Type.__name__ = "Integer32"
_Es2226QoSWeightQ2_Object = MibScalar
es2226QoSWeightQ2 = _Es2226QoSWeightQ2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 7),
    _Es2226QoSWeightQ2_Type()
)
es2226QoSWeightQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSWeightQ2.setStatus("current")


class _Es2226QoSWeightQ3_Type(Integer32):
    """Custom type es2226QoSWeightQ3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2226QoSWeightQ3_Type.__name__ = "Integer32"
_Es2226QoSWeightQ3_Object = MibScalar
es2226QoSWeightQ3 = _Es2226QoSWeightQ3_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 1, 8),
    _Es2226QoSWeightQ3_Type()
)
es2226QoSWeightQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSWeightQ3.setStatus("current")
_Es2226QoS1PPriority_ObjectIdentity = ObjectIdentity
es2226QoS1PPriority = _Es2226QoS1PPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 2)
)
_Es2226QoS1PPriorityTable_Object = MibTable
es2226QoS1PPriorityTable = _Es2226QoS1PPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    es2226QoS1PPriorityTable.setStatus("current")
_Es2226QoS1PPriorityEntry_Object = MibTableRow
es2226QoS1PPriorityEntry = _Es2226QoS1PPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 2, 1, 1)
)
es2226QoS1PPriorityEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226QoS1PPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2226QoS1PPriorityEntry.setStatus("current")


class _Es2226QoS1PPriorityIndex_Type(Integer32):
    """Custom type es2226QoS1PPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2226QoS1PPriorityIndex_Type.__name__ = "Integer32"
_Es2226QoS1PPriorityIndex_Object = MibTableColumn
es2226QoS1PPriorityIndex = _Es2226QoS1PPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 2, 1, 1, 1),
    _Es2226QoS1PPriorityIndex_Type()
)
es2226QoS1PPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226QoS1PPriorityIndex.setStatus("current")


class _Es2226QoS1PPriorityValue_Type(Integer32):
    """Custom type es2226QoS1PPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226QoS1PPriorityValue_Type.__name__ = "Integer32"
_Es2226QoS1PPriorityValue_Object = MibTableColumn
es2226QoS1PPriorityValue = _Es2226QoS1PPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 2, 1, 1, 2),
    _Es2226QoS1PPriorityValue_Type()
)
es2226QoS1PPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226QoS1PPriorityValue.setStatus("current")


class _Es2226QoS1PPriorityQueue_Type(Integer32):
    """Custom type es2226QoS1PPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226QoS1PPriorityQueue_Type.__name__ = "Integer32"
_Es2226QoS1PPriorityQueue_Object = MibTableColumn
es2226QoS1PPriorityQueue = _Es2226QoS1PPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 2, 1, 1, 3),
    _Es2226QoS1PPriorityQueue_Type()
)
es2226QoS1PPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoS1PPriorityQueue.setStatus("current")
_Es2226QoSDSCPPriority_ObjectIdentity = ObjectIdentity
es2226QoSDSCPPriority = _Es2226QoSDSCPPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 3)
)
_Es2226QoSDSCPPriorityTable_Object = MibTable
es2226QoSDSCPPriorityTable = _Es2226QoSDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    es2226QoSDSCPPriorityTable.setStatus("current")
_Es2226QoSDSCPPriorityEntry_Object = MibTableRow
es2226QoSDSCPPriorityEntry = _Es2226QoSDSCPPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 3, 1, 1)
)
es2226QoSDSCPPriorityEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226QoSDSCPPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2226QoSDSCPPriorityEntry.setStatus("current")


class _Es2226QoSDSCPPriorityIndex_Type(Integer32):
    """Custom type es2226QoSDSCPPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2226QoSDSCPPriorityIndex_Type.__name__ = "Integer32"
_Es2226QoSDSCPPriorityIndex_Object = MibTableColumn
es2226QoSDSCPPriorityIndex = _Es2226QoSDSCPPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 3, 1, 1, 1),
    _Es2226QoSDSCPPriorityIndex_Type()
)
es2226QoSDSCPPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226QoSDSCPPriorityIndex.setStatus("current")


class _Es2226QoSDSCPPriorityValue_Type(Integer32):
    """Custom type es2226QoSDSCPPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226QoSDSCPPriorityValue_Type.__name__ = "Integer32"
_Es2226QoSDSCPPriorityValue_Object = MibTableColumn
es2226QoSDSCPPriorityValue = _Es2226QoSDSCPPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 3, 1, 1, 2),
    _Es2226QoSDSCPPriorityValue_Type()
)
es2226QoSDSCPPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226QoSDSCPPriorityValue.setStatus("current")


class _Es2226QoSDSCPPriorityQueue_Type(Integer32):
    """Custom type es2226QoSDSCPPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226QoSDSCPPriorityQueue_Type.__name__ = "Integer32"
_Es2226QoSDSCPPriorityQueue_Object = MibTableColumn
es2226QoSDSCPPriorityQueue = _Es2226QoSDSCPPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 16, 3, 1, 1, 3),
    _Es2226QoSDSCPPriorityQueue_Type()
)
es2226QoSDSCPPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226QoSDSCPPriorityQueue.setStatus("current")
_Es2226Vlan_ObjectIdentity = ObjectIdentity
es2226Vlan = _Es2226Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17)
)
_Es2226VlanModeConfig_ObjectIdentity = ObjectIdentity
es2226VlanModeConfig = _Es2226VlanModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1)
)


class _Es2226VlanMode_Type(Integer32):
    """Custom type es2226VlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226VlanMode_Type.__name__ = "Integer32"
_Es2226VlanMode_Object = MibScalar
es2226VlanMode = _Es2226VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1, 1),
    _Es2226VlanMode_Type()
)
es2226VlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VlanMode.setStatus("current")


class _Es2226SymmetricVlan_Type(Integer32):
    """Custom type es2226SymmetricVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226SymmetricVlan_Type.__name__ = "Integer32"
_Es2226SymmetricVlan_Object = MibScalar
es2226SymmetricVlan = _Es2226SymmetricVlan_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1, 2),
    _Es2226SymmetricVlan_Type()
)
es2226SymmetricVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226SymmetricVlan.setStatus("current")


class _Es2226VlanSVL_Type(Integer32):
    """Custom type es2226VlanSVL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226VlanSVL_Type.__name__ = "Integer32"
_Es2226VlanSVL_Object = MibScalar
es2226VlanSVL = _Es2226VlanSVL_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1, 3),
    _Es2226VlanSVL_Type()
)
es2226VlanSVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VlanSVL.setStatus("current")


class _Es2226DoubleTag_Type(Integer32):
    """Custom type es2226DoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226DoubleTag_Type.__name__ = "Integer32"
_Es2226DoubleTag_Object = MibScalar
es2226DoubleTag = _Es2226DoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1, 4),
    _Es2226DoubleTag_Type()
)
es2226DoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DoubleTag.setStatus("current")
_Es2226SpPortMember_Type = DisplayString
_Es2226SpPortMember_Object = MibScalar
es2226SpPortMember = _Es2226SpPortMember_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1, 5),
    _Es2226SpPortMember_Type()
)
es2226SpPortMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226SpPortMember.setStatus("current")


class _Es2226UpLinkPort_Type(Integer32):
    """Custom type es2226UpLinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226UpLinkPort_Type.__name__ = "Integer32"
_Es2226UpLinkPort_Object = MibScalar
es2226UpLinkPort = _Es2226UpLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 1, 6),
    _Es2226UpLinkPort_Type()
)
es2226UpLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226UpLinkPort.setStatus("current")
_Es2226VlanPvid_ObjectIdentity = ObjectIdentity
es2226VlanPvid = _Es2226VlanPvid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2)
)
_Es2226VlanPvidTable_Object = MibTable
es2226VlanPvidTable = _Es2226VlanPvidTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    es2226VlanPvidTable.setStatus("current")
_Es2226VlanPvidEntry_Object = MibTableRow
es2226VlanPvidEntry = _Es2226VlanPvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2, 1, 1)
)
es2226VlanPvidEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226VlanPvidPort"),
)
if mibBuilder.loadTexts:
    es2226VlanPvidEntry.setStatus("current")


class _Es2226VlanPvidPort_Type(Integer32):
    """Custom type es2226VlanPvidPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226VlanPvidPort_Type.__name__ = "Integer32"
_Es2226VlanPvidPort_Object = MibTableColumn
es2226VlanPvidPort = _Es2226VlanPvidPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2, 1, 1, 1),
    _Es2226VlanPvidPort_Type()
)
es2226VlanPvidPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226VlanPvidPort.setStatus("current")


class _Es2226VlanPvidValue_Type(Integer32):
    """Custom type es2226VlanPvidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226VlanPvidValue_Type.__name__ = "Integer32"
_Es2226VlanPvidValue_Object = MibTableColumn
es2226VlanPvidValue = _Es2226VlanPvidValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2, 1, 1, 2),
    _Es2226VlanPvidValue_Type()
)
es2226VlanPvidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VlanPvidValue.setStatus("current")


class _Es2226VlanPvidDefaultPriority_Type(Integer32):
    """Custom type es2226VlanPvidDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226VlanPvidDefaultPriority_Type.__name__ = "Integer32"
_Es2226VlanPvidDefaultPriority_Object = MibTableColumn
es2226VlanPvidDefaultPriority = _Es2226VlanPvidDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2, 1, 1, 3),
    _Es2226VlanPvidDefaultPriority_Type()
)
es2226VlanPvidDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VlanPvidDefaultPriority.setStatus("current")


class _Es2226VlanPvidDropUntag_Type(Integer32):
    """Custom type es2226VlanPvidDropUntag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226VlanPvidDropUntag_Type.__name__ = "Integer32"
_Es2226VlanPvidDropUntag_Object = MibTableColumn
es2226VlanPvidDropUntag = _Es2226VlanPvidDropUntag_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 2, 1, 1, 4),
    _Es2226VlanPvidDropUntag_Type()
)
es2226VlanPvidDropUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226VlanPvidDropUntag.setStatus("current")
_Es2226PortBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2226PortBasedVlanGroup = _Es2226PortBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3)
)


class _Es2226PortBasedVlanNumbers_Type(Integer32):
    """Custom type es2226PortBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226PortBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2226PortBasedVlanNumbers_Object = MibScalar
es2226PortBasedVlanNumbers = _Es2226PortBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 1),
    _Es2226PortBasedVlanNumbers_Type()
)
es2226PortBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226PortBasedVlanNumbers.setStatus("current")


class _Es2226PortBasedCreateStatus_Type(Integer32):
    """Custom type es2226PortBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226PortBasedCreateStatus_Type.__name__ = "Integer32"
_Es2226PortBasedCreateStatus_Object = MibScalar
es2226PortBasedCreateStatus = _Es2226PortBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 2),
    _Es2226PortBasedCreateStatus_Type()
)
es2226PortBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBasedCreateStatus.setStatus("current")
_Es2226PortBasedVlanTable_Object = MibTable
es2226PortBasedVlanTable = _Es2226PortBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 3)
)
if mibBuilder.loadTexts:
    es2226PortBasedVlanTable.setStatus("current")
_Es2226PortBasedVlanEntry_Object = MibTableRow
es2226PortBasedVlanEntry = _Es2226PortBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 3, 1)
)
es2226PortBasedVlanEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226PortBasedVlanIndex"),
)
if mibBuilder.loadTexts:
    es2226PortBasedVlanEntry.setStatus("current")


class _Es2226PortBasedVlanIndex_Type(Integer32):
    """Custom type es2226PortBasedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226PortBasedVlanIndex_Type.__name__ = "Integer32"
_Es2226PortBasedVlanIndex_Object = MibTableColumn
es2226PortBasedVlanIndex = _Es2226PortBasedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 3, 1, 1),
    _Es2226PortBasedVlanIndex_Type()
)
es2226PortBasedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226PortBasedVlanIndex.setStatus("current")
_Es2226PortBasedVlanName_Type = DisplayString
_Es2226PortBasedVlanName_Object = MibTableColumn
es2226PortBasedVlanName = _Es2226PortBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 3, 1, 2),
    _Es2226PortBasedVlanName_Type()
)
es2226PortBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBasedVlanName.setStatus("current")
_Es2226PortBasedVlanMember_Type = DisplayString
_Es2226PortBasedVlanMember_Object = MibTableColumn
es2226PortBasedVlanMember = _Es2226PortBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 3, 1, 3),
    _Es2226PortBasedVlanMember_Type()
)
es2226PortBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBasedVlanMember.setStatus("current")


class _Es2226PortBasedVlanRowStatus_Type(Integer32):
    """Custom type es2226PortBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226PortBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2226PortBasedVlanRowStatus_Object = MibTableColumn
es2226PortBasedVlanRowStatus = _Es2226PortBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 3, 3, 1, 4),
    _Es2226PortBasedVlanRowStatus_Type()
)
es2226PortBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226PortBasedVlanRowStatus.setStatus("current")
_Es2226ManagementVlan_ObjectIdentity = ObjectIdentity
es2226ManagementVlan = _Es2226ManagementVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 4)
)


class _Es2226ManagementVlanState_Type(Integer32):
    """Custom type es2226ManagementVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226ManagementVlanState_Type.__name__ = "Integer32"
_Es2226ManagementVlanState_Object = MibScalar
es2226ManagementVlanState = _Es2226ManagementVlanState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 4, 1),
    _Es2226ManagementVlanState_Type()
)
es2226ManagementVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementVlanState.setStatus("current")


class _Es2226ManagementVlanVid_Type(Integer32):
    """Custom type es2226ManagementVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226ManagementVlanVid_Type.__name__ = "Integer32"
_Es2226ManagementVlanVid_Object = MibScalar
es2226ManagementVlanVid = _Es2226ManagementVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 17, 4, 2),
    _Es2226ManagementVlanVid_Type()
)
es2226ManagementVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226ManagementVlanVid.setStatus("current")
_Es2226DhcpSnooping_ObjectIdentity = ObjectIdentity
es2226DhcpSnooping = _Es2226DhcpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18)
)
_Es2226DhcpSnoopingConf_ObjectIdentity = ObjectIdentity
es2226DhcpSnoopingConf = _Es2226DhcpSnoopingConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 1)
)


class _Es2226DhcpSnoopingState_Type(Integer32):
    """Custom type es2226DhcpSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpSnoopingState_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingState_Object = MibScalar
es2226DhcpSnoopingState = _Es2226DhcpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 1, 1),
    _Es2226DhcpSnoopingState_Type()
)
es2226DhcpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingState.setStatus("current")
_Es2226DhcpSnoopingPortCountSetupTable_Object = MibTable
es2226DhcpSnoopingPortCountSetupTable = _Es2226DhcpSnoopingPortCountSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingPortCountSetupTable.setStatus("current")
_Es2226DhcpSnoopingPortCountSetupEntry_Object = MibTableRow
es2226DhcpSnoopingPortCountSetupEntry = _Es2226DhcpSnoopingPortCountSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 1, 2, 1)
)
es2226DhcpSnoopingPortCountSetupEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226DhcpSnoopingPortCountSetupPortIndex"),
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingPortCountSetupEntry.setStatus("current")


class _Es2226DhcpSnoopingPortCountSetupPortIndex_Type(Integer32):
    """Custom type es2226DhcpSnoopingPortCountSetupPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226DhcpSnoopingPortCountSetupPortIndex_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingPortCountSetupPortIndex_Object = MibTableColumn
es2226DhcpSnoopingPortCountSetupPortIndex = _Es2226DhcpSnoopingPortCountSetupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 1, 2, 1, 1),
    _Es2226DhcpSnoopingPortCountSetupPortIndex_Type()
)
es2226DhcpSnoopingPortCountSetupPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingPortCountSetupPortIndex.setStatus("current")


class _Es2226DhcpSnoopingPortCountSetupCount_Type(Integer32):
    """Custom type es2226DhcpSnoopingPortCountSetupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Es2226DhcpSnoopingPortCountSetupCount_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingPortCountSetupCount_Object = MibTableColumn
es2226DhcpSnoopingPortCountSetupCount = _Es2226DhcpSnoopingPortCountSetupCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 1, 2, 1, 2),
    _Es2226DhcpSnoopingPortCountSetupCount_Type()
)
es2226DhcpSnoopingPortCountSetupCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingPortCountSetupCount.setStatus("current")
_Es2226DhcpSnoopingTrustGroupConf_ObjectIdentity = ObjectIdentity
es2226DhcpSnoopingTrustGroupConf = _Es2226DhcpSnoopingTrustGroupConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2)
)


class _Es2226DhcpSnoopingTrustGroupNumbers_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Es2226DhcpSnoopingTrustGroupNumbers_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupNumbers_Object = MibScalar
es2226DhcpSnoopingTrustGroupNumbers = _Es2226DhcpSnoopingTrustGroupNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 1),
    _Es2226DhcpSnoopingTrustGroupNumbers_Type()
)
es2226DhcpSnoopingTrustGroupNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupNumbers.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupCreatStatus_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226DhcpSnoopingTrustGroupCreatStatus_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupCreatStatus_Object = MibScalar
es2226DhcpSnoopingTrustGroupCreatStatus = _Es2226DhcpSnoopingTrustGroupCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 2),
    _Es2226DhcpSnoopingTrustGroupCreatStatus_Type()
)
es2226DhcpSnoopingTrustGroupCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupCreatStatus.setStatus("current")
_Es2226DhcpSnoopingTrustGroupTable_Object = MibTable
es2226DhcpSnoopingTrustGroupTable = _Es2226DhcpSnoopingTrustGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3)
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupTable.setStatus("current")
_Es2226DhcpSnoopingTrustGroupEntry_Object = MibTableRow
es2226DhcpSnoopingTrustGroupEntry = _Es2226DhcpSnoopingTrustGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1)
)
es2226DhcpSnoopingTrustGroupEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226DhcpSnoopingTrustGroupIndex"),
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupEntry.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupIndex_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Es2226DhcpSnoopingTrustGroupIndex_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupIndex_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupIndex = _Es2226DhcpSnoopingTrustGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 1),
    _Es2226DhcpSnoopingTrustGroupIndex_Type()
)
es2226DhcpSnoopingTrustGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupIndex.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupTrustVid_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupTrustVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226DhcpSnoopingTrustGroupTrustVid_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupTrustVid_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupTrustVid = _Es2226DhcpSnoopingTrustGroupTrustVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 2),
    _Es2226DhcpSnoopingTrustGroupTrustVid_Type()
)
es2226DhcpSnoopingTrustGroupTrustVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupTrustVid.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupOption82_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpSnoopingTrustGroupOption82_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupOption82_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupOption82 = _Es2226DhcpSnoopingTrustGroupOption82_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 3),
    _Es2226DhcpSnoopingTrustGroupOption82_Type()
)
es2226DhcpSnoopingTrustGroupOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupOption82.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupAction_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226DhcpSnoopingTrustGroupAction_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupAction_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupAction = _Es2226DhcpSnoopingTrustGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 4),
    _Es2226DhcpSnoopingTrustGroupAction_Type()
)
es2226DhcpSnoopingTrustGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupAction.setStatus("current")
_Es2226DhcpSnoopingTrustGroupServerPort_Type = DisplayString
_Es2226DhcpSnoopingTrustGroupServerPort_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupServerPort = _Es2226DhcpSnoopingTrustGroupServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 5),
    _Es2226DhcpSnoopingTrustGroupServerPort_Type()
)
es2226DhcpSnoopingTrustGroupServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupServerPort.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupServerVid_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupServerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226DhcpSnoopingTrustGroupServerVid_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupServerVid_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupServerVid = _Es2226DhcpSnoopingTrustGroupServerVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 6),
    _Es2226DhcpSnoopingTrustGroupServerVid_Type()
)
es2226DhcpSnoopingTrustGroupServerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupServerVid.setStatus("current")
_Es2226DhcpSnoopingTrustGroupServerIp_Type = IpAddress
_Es2226DhcpSnoopingTrustGroupServerIp_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupServerIp = _Es2226DhcpSnoopingTrustGroupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 7),
    _Es2226DhcpSnoopingTrustGroupServerIp_Type()
)
es2226DhcpSnoopingTrustGroupServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupServerIp.setStatus("current")


class _Es2226DhcpSnoopingTrustGroupRowStatus_Type(Integer32):
    """Custom type es2226DhcpSnoopingTrustGroupRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226DhcpSnoopingTrustGroupRowStatus_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingTrustGroupRowStatus_Object = MibTableColumn
es2226DhcpSnoopingTrustGroupRowStatus = _Es2226DhcpSnoopingTrustGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 2, 3, 1, 8),
    _Es2226DhcpSnoopingTrustGroupRowStatus_Type()
)
es2226DhcpSnoopingTrustGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingTrustGroupRowStatus.setStatus("current")
_Es2226DhcpSnoopingDefaultGroupConf_ObjectIdentity = ObjectIdentity
es2226DhcpSnoopingDefaultGroupConf = _Es2226DhcpSnoopingDefaultGroupConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 3)
)
_Es2226DhcpSnoopingDefaultGroupServerPort_Type = DisplayString
_Es2226DhcpSnoopingDefaultGroupServerPort_Object = MibScalar
es2226DhcpSnoopingDefaultGroupServerPort = _Es2226DhcpSnoopingDefaultGroupServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 3, 1),
    _Es2226DhcpSnoopingDefaultGroupServerPort_Type()
)
es2226DhcpSnoopingDefaultGroupServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingDefaultGroupServerPort.setStatus("current")


class _Es2226DhcpSnoopingDefaultGroupServerVid_Type(Integer32):
    """Custom type es2226DhcpSnoopingDefaultGroupServerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226DhcpSnoopingDefaultGroupServerVid_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingDefaultGroupServerVid_Object = MibScalar
es2226DhcpSnoopingDefaultGroupServerVid = _Es2226DhcpSnoopingDefaultGroupServerVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 3, 2),
    _Es2226DhcpSnoopingDefaultGroupServerVid_Type()
)
es2226DhcpSnoopingDefaultGroupServerVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingDefaultGroupServerVid.setStatus("current")


class _Es2226DhcpSnoopingDefaultGroupOption82_Type(Integer32):
    """Custom type es2226DhcpSnoopingDefaultGroupOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpSnoopingDefaultGroupOption82_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingDefaultGroupOption82_Object = MibScalar
es2226DhcpSnoopingDefaultGroupOption82 = _Es2226DhcpSnoopingDefaultGroupOption82_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 3, 3),
    _Es2226DhcpSnoopingDefaultGroupOption82_Type()
)
es2226DhcpSnoopingDefaultGroupOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingDefaultGroupOption82.setStatus("current")


class _Es2226DhcpSnoopingDefaultGroupAction_Type(Integer32):
    """Custom type es2226DhcpSnoopingDefaultGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226DhcpSnoopingDefaultGroupAction_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingDefaultGroupAction_Object = MibScalar
es2226DhcpSnoopingDefaultGroupAction = _Es2226DhcpSnoopingDefaultGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 3, 4),
    _Es2226DhcpSnoopingDefaultGroupAction_Type()
)
es2226DhcpSnoopingDefaultGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingDefaultGroupAction.setStatus("current")
_Es2226DhcpSnoopingDefaultGroupServerIp_Type = IpAddress
_Es2226DhcpSnoopingDefaultGroupServerIp_Object = MibScalar
es2226DhcpSnoopingDefaultGroupServerIp = _Es2226DhcpSnoopingDefaultGroupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 3, 5),
    _Es2226DhcpSnoopingDefaultGroupServerIp_Type()
)
es2226DhcpSnoopingDefaultGroupServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingDefaultGroupServerIp.setStatus("current")
_Es2226DhcpSnoopingLeaseList_ObjectIdentity = ObjectIdentity
es2226DhcpSnoopingLeaseList = _Es2226DhcpSnoopingLeaseList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4)
)


class _Es2226DhcpSnoopingLeaseListDeleteAll_Type(Integer32):
    """Custom type es2226DhcpSnoopingLeaseListDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpSnoopingLeaseListDeleteAll_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingLeaseListDeleteAll_Object = MibScalar
es2226DhcpSnoopingLeaseListDeleteAll = _Es2226DhcpSnoopingLeaseListDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 1),
    _Es2226DhcpSnoopingLeaseListDeleteAll_Type()
)
es2226DhcpSnoopingLeaseListDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListDeleteAll.setStatus("current")


class _Es2226DhcpSnoopingLeaseListNumbers_Type(Integer32):
    """Custom type es2226DhcpSnoopingLeaseListNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Es2226DhcpSnoopingLeaseListNumbers_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingLeaseListNumbers_Object = MibScalar
es2226DhcpSnoopingLeaseListNumbers = _Es2226DhcpSnoopingLeaseListNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 2),
    _Es2226DhcpSnoopingLeaseListNumbers_Type()
)
es2226DhcpSnoopingLeaseListNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListNumbers.setStatus("current")
_Es2226DhcpSnoopingLeaseListTable_Object = MibTable
es2226DhcpSnoopingLeaseListTable = _Es2226DhcpSnoopingLeaseListTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3)
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListTable.setStatus("current")
_Es2226DhcpSnoopingLeaseListEntry_Object = MibTableRow
es2226DhcpSnoopingLeaseListEntry = _Es2226DhcpSnoopingLeaseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1)
)
es2226DhcpSnoopingLeaseListEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226DhcpSnoopingLeaseListIndex"),
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListEntry.setStatus("current")


class _Es2226DhcpSnoopingLeaseListIndex_Type(Integer32):
    """Custom type es2226DhcpSnoopingLeaseListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Es2226DhcpSnoopingLeaseListIndex_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingLeaseListIndex_Object = MibTableColumn
es2226DhcpSnoopingLeaseListIndex = _Es2226DhcpSnoopingLeaseListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1, 1),
    _Es2226DhcpSnoopingLeaseListIndex_Type()
)
es2226DhcpSnoopingLeaseListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListIndex.setStatus("current")
_Es2226DhcpSnoopingLeaseListMac_Type = DisplayString
_Es2226DhcpSnoopingLeaseListMac_Object = MibTableColumn
es2226DhcpSnoopingLeaseListMac = _Es2226DhcpSnoopingLeaseListMac_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1, 2),
    _Es2226DhcpSnoopingLeaseListMac_Type()
)
es2226DhcpSnoopingLeaseListMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListMac.setStatus("current")
_Es2226DhcpSnoopingLeaseListIp_Type = IpAddress
_Es2226DhcpSnoopingLeaseListIp_Object = MibTableColumn
es2226DhcpSnoopingLeaseListIp = _Es2226DhcpSnoopingLeaseListIp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1, 3),
    _Es2226DhcpSnoopingLeaseListIp_Type()
)
es2226DhcpSnoopingLeaseListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListIp.setStatus("current")


class _Es2226DhcpSnoopingLeaseListPort_Type(Integer32):
    """Custom type es2226DhcpSnoopingLeaseListPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226DhcpSnoopingLeaseListPort_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingLeaseListPort_Object = MibTableColumn
es2226DhcpSnoopingLeaseListPort = _Es2226DhcpSnoopingLeaseListPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1, 4),
    _Es2226DhcpSnoopingLeaseListPort_Type()
)
es2226DhcpSnoopingLeaseListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListPort.setStatus("current")


class _Es2226DhcpSnoopingLeaseListVid_Type(Integer32):
    """Custom type es2226DhcpSnoopingLeaseListVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226DhcpSnoopingLeaseListVid_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingLeaseListVid_Object = MibTableColumn
es2226DhcpSnoopingLeaseListVid = _Es2226DhcpSnoopingLeaseListVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1, 5),
    _Es2226DhcpSnoopingLeaseListVid_Type()
)
es2226DhcpSnoopingLeaseListVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListVid.setStatus("current")
_Es2226DhcpSnoopingLeaseListLease_Type = DisplayString
_Es2226DhcpSnoopingLeaseListLease_Object = MibTableColumn
es2226DhcpSnoopingLeaseListLease = _Es2226DhcpSnoopingLeaseListLease_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 4, 3, 1, 6),
    _Es2226DhcpSnoopingLeaseListLease_Type()
)
es2226DhcpSnoopingLeaseListLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingLeaseListLease.setStatus("current")
_Es2226DhcpSnoopingCounter_ObjectIdentity = ObjectIdentity
es2226DhcpSnoopingCounter = _Es2226DhcpSnoopingCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5)
)


class _Es2226DhcpSnoopingCounterReset_Type(Integer32):
    """Custom type es2226DhcpSnoopingCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpSnoopingCounterReset_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingCounterReset_Object = MibScalar
es2226DhcpSnoopingCounterReset = _Es2226DhcpSnoopingCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 1),
    _Es2226DhcpSnoopingCounterReset_Type()
)
es2226DhcpSnoopingCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterReset.setStatus("current")
_Es2226DhcpSnoopingCounterTable_Object = MibTable
es2226DhcpSnoopingCounterTable = _Es2226DhcpSnoopingCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2)
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterTable.setStatus("current")
_Es2226DhcpSnoopingCounterEntry_Object = MibTableRow
es2226DhcpSnoopingCounterEntry = _Es2226DhcpSnoopingCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1)
)
es2226DhcpSnoopingCounterEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226DhcpSnoopingCounterPortIndex"),
)
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterEntry.setStatus("current")


class _Es2226DhcpSnoopingCounterPortIndex_Type(Integer32):
    """Custom type es2226DhcpSnoopingCounterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226DhcpSnoopingCounterPortIndex_Type.__name__ = "Integer32"
_Es2226DhcpSnoopingCounterPortIndex_Object = MibTableColumn
es2226DhcpSnoopingCounterPortIndex = _Es2226DhcpSnoopingCounterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 1),
    _Es2226DhcpSnoopingCounterPortIndex_Type()
)
es2226DhcpSnoopingCounterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterPortIndex.setStatus("current")
_Es2226DhcpSnoopingCounterDiscover_Type = Counter32
_Es2226DhcpSnoopingCounterDiscover_Object = MibTableColumn
es2226DhcpSnoopingCounterDiscover = _Es2226DhcpSnoopingCounterDiscover_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 2),
    _Es2226DhcpSnoopingCounterDiscover_Type()
)
es2226DhcpSnoopingCounterDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterDiscover.setStatus("current")
_Es2226DhcpSnoopingCounterOffer_Type = Counter32
_Es2226DhcpSnoopingCounterOffer_Object = MibTableColumn
es2226DhcpSnoopingCounterOffer = _Es2226DhcpSnoopingCounterOffer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 3),
    _Es2226DhcpSnoopingCounterOffer_Type()
)
es2226DhcpSnoopingCounterOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterOffer.setStatus("current")
_Es2226DhcpSnoopingCounterRequest_Type = Counter32
_Es2226DhcpSnoopingCounterRequest_Object = MibTableColumn
es2226DhcpSnoopingCounterRequest = _Es2226DhcpSnoopingCounterRequest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 4),
    _Es2226DhcpSnoopingCounterRequest_Type()
)
es2226DhcpSnoopingCounterRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterRequest.setStatus("current")
_Es2226DhcpSnoopingCounterDecline_Type = Counter32
_Es2226DhcpSnoopingCounterDecline_Object = MibTableColumn
es2226DhcpSnoopingCounterDecline = _Es2226DhcpSnoopingCounterDecline_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 5),
    _Es2226DhcpSnoopingCounterDecline_Type()
)
es2226DhcpSnoopingCounterDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterDecline.setStatus("current")
_Es2226DhcpSnoopingCounterAck_Type = Counter32
_Es2226DhcpSnoopingCounterAck_Object = MibTableColumn
es2226DhcpSnoopingCounterAck = _Es2226DhcpSnoopingCounterAck_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 6),
    _Es2226DhcpSnoopingCounterAck_Type()
)
es2226DhcpSnoopingCounterAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterAck.setStatus("current")
_Es2226DhcpSnoopingCounterNack_Type = Counter32
_Es2226DhcpSnoopingCounterNack_Object = MibTableColumn
es2226DhcpSnoopingCounterNack = _Es2226DhcpSnoopingCounterNack_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 7),
    _Es2226DhcpSnoopingCounterNack_Type()
)
es2226DhcpSnoopingCounterNack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterNack.setStatus("current")
_Es2226DhcpSnoopingCounterRelease_Type = Counter32
_Es2226DhcpSnoopingCounterRelease_Object = MibTableColumn
es2226DhcpSnoopingCounterRelease = _Es2226DhcpSnoopingCounterRelease_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 8),
    _Es2226DhcpSnoopingCounterRelease_Type()
)
es2226DhcpSnoopingCounterRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterRelease.setStatus("current")
_Es2226DhcpSnoopingCounterInform_Type = Counter32
_Es2226DhcpSnoopingCounterInform_Object = MibTableColumn
es2226DhcpSnoopingCounterInform = _Es2226DhcpSnoopingCounterInform_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 18, 5, 2, 1, 9),
    _Es2226DhcpSnoopingCounterInform_Type()
)
es2226DhcpSnoopingCounterInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226DhcpSnoopingCounterInform.setStatus("current")
_Es2226Dot1X_ObjectIdentity = ObjectIdentity
es2226Dot1X = _Es2226Dot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19)
)
_Es2226Dot1XStateSetting_ObjectIdentity = ObjectIdentity
es2226Dot1XStateSetting = _Es2226Dot1XStateSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1)
)
_Es2226RadiusServer1_Type = IpAddress
_Es2226RadiusServer1_Object = MibScalar
es2226RadiusServer1 = _Es2226RadiusServer1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 1),
    _Es2226RadiusServer1_Type()
)
es2226RadiusServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusServer1.setStatus("current")


class _Es2226Dot1XPort1_Type(Integer32):
    """Custom type es2226Dot1XPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226Dot1XPort1_Type.__name__ = "Integer32"
_Es2226Dot1XPort1_Object = MibScalar
es2226Dot1XPort1 = _Es2226Dot1XPort1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 2),
    _Es2226Dot1XPort1_Type()
)
es2226Dot1XPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPort1.setStatus("current")
_Es2226RadiusServer2_Type = IpAddress
_Es2226RadiusServer2_Object = MibScalar
es2226RadiusServer2 = _Es2226RadiusServer2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 3),
    _Es2226RadiusServer2_Type()
)
es2226RadiusServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusServer2.setStatus("current")


class _Es2226Dot1XPort2_Type(Integer32):
    """Custom type es2226Dot1XPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226Dot1XPort2_Type.__name__ = "Integer32"
_Es2226Dot1XPort2_Object = MibScalar
es2226Dot1XPort2 = _Es2226Dot1XPort2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 4),
    _Es2226Dot1XPort2_Type()
)
es2226Dot1XPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPort2.setStatus("current")
_Es2226SecretKey1_Type = DisplayString
_Es2226SecretKey1_Object = MibScalar
es2226SecretKey1 = _Es2226SecretKey1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 5),
    _Es2226SecretKey1_Type()
)
es2226SecretKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226SecretKey1.setStatus("current")


class _Es2226AccountingService_Type(Integer32):
    """Custom type es2226AccountingService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226AccountingService_Type.__name__ = "Integer32"
_Es2226AccountingService_Object = MibScalar
es2226AccountingService = _Es2226AccountingService_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 6),
    _Es2226AccountingService_Type()
)
es2226AccountingService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountingService.setStatus("current")
_Es2226AccountingServer1_Type = IpAddress
_Es2226AccountingServer1_Object = MibScalar
es2226AccountingServer1 = _Es2226AccountingServer1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 7),
    _Es2226AccountingServer1_Type()
)
es2226AccountingServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountingServer1.setStatus("current")


class _Es2226AccountingPort1_Type(Integer32):
    """Custom type es2226AccountingPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226AccountingPort1_Type.__name__ = "Integer32"
_Es2226AccountingPort1_Object = MibScalar
es2226AccountingPort1 = _Es2226AccountingPort1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 8),
    _Es2226AccountingPort1_Type()
)
es2226AccountingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountingPort1.setStatus("current")
_Es2226AccountingServer2_Type = IpAddress
_Es2226AccountingServer2_Object = MibScalar
es2226AccountingServer2 = _Es2226AccountingServer2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 9),
    _Es2226AccountingServer2_Type()
)
es2226AccountingServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountingServer2.setStatus("current")


class _Es2226AccountingPort2_Type(Integer32):
    """Custom type es2226AccountingPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226AccountingPort2_Type.__name__ = "Integer32"
_Es2226AccountingPort2_Object = MibScalar
es2226AccountingPort2 = _Es2226AccountingPort2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 10),
    _Es2226AccountingPort2_Type()
)
es2226AccountingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226AccountingPort2.setStatus("current")
_Es2226SecretKey2_Type = DisplayString
_Es2226SecretKey2_Object = MibScalar
es2226SecretKey2 = _Es2226SecretKey2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 1, 11),
    _Es2226SecretKey2_Type()
)
es2226SecretKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226SecretKey2.setStatus("current")
_Es2226Dot1XPortSecurityManagement_ObjectIdentity = ObjectIdentity
es2226Dot1XPortSecurityManagement = _Es2226Dot1XPortSecurityManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2)
)
_Es2226Dot1XPortSecurityTable_Object = MibTable
es2226Dot1XPortSecurityTable = _Es2226Dot1XPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityTable.setStatus("current")
_Es2226Dot1XPortSecurityEntry_Object = MibTableRow
es2226Dot1XPortSecurityEntry = _Es2226Dot1XPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1)
)
es2226Dot1XPortSecurityEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226Dot1XPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityEntry.setStatus("current")


class _Es2226Dot1XPortSecurityPortIndex_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226Dot1XPortSecurityPortIndex_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityPortIndex_Object = MibTableColumn
es2226Dot1XPortSecurityPortIndex = _Es2226Dot1XPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 1),
    _Es2226Dot1XPortSecurityPortIndex_Type()
)
es2226Dot1XPortSecurityPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityPortIndex.setStatus("current")


class _Es2226Dot1XPortSecurityMode_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226Dot1XPortSecurityMode_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityMode_Object = MibTableColumn
es2226Dot1XPortSecurityMode = _Es2226Dot1XPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 2),
    _Es2226Dot1XPortSecurityMode_Type()
)
es2226Dot1XPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityMode.setStatus("current")


class _Es2226Dot1XPortSecurityPortControl_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226Dot1XPortSecurityPortControl_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityPortControl_Object = MibTableColumn
es2226Dot1XPortSecurityPortControl = _Es2226Dot1XPortSecurityPortControl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 3),
    _Es2226Dot1XPortSecurityPortControl_Type()
)
es2226Dot1XPortSecurityPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityPortControl.setStatus("current")


class _Es2226Dot1XPortSecurityReAuthMax_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityReAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2226Dot1XPortSecurityReAuthMax_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityReAuthMax_Object = MibTableColumn
es2226Dot1XPortSecurityReAuthMax = _Es2226Dot1XPortSecurityReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 4),
    _Es2226Dot1XPortSecurityReAuthMax_Type()
)
es2226Dot1XPortSecurityReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityReAuthMax.setStatus("current")


class _Es2226Dot1XPortSecurityTxPeriod_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226Dot1XPortSecurityTxPeriod_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityTxPeriod_Object = MibTableColumn
es2226Dot1XPortSecurityTxPeriod = _Es2226Dot1XPortSecurityTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 5),
    _Es2226Dot1XPortSecurityTxPeriod_Type()
)
es2226Dot1XPortSecurityTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityTxPeriod.setStatus("current")


class _Es2226Dot1XPortSecurityQuietPeriod_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2226Dot1XPortSecurityQuietPeriod_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityQuietPeriod_Object = MibTableColumn
es2226Dot1XPortSecurityQuietPeriod = _Es2226Dot1XPortSecurityQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 6),
    _Es2226Dot1XPortSecurityQuietPeriod_Type()
)
es2226Dot1XPortSecurityQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityQuietPeriod.setStatus("current")


class _Es2226Dot1XPortSecurityReAuthEnabled_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityReAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226Dot1XPortSecurityReAuthEnabled_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityReAuthEnabled_Object = MibTableColumn
es2226Dot1XPortSecurityReAuthEnabled = _Es2226Dot1XPortSecurityReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 7),
    _Es2226Dot1XPortSecurityReAuthEnabled_Type()
)
es2226Dot1XPortSecurityReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityReAuthEnabled.setStatus("current")


class _Es2226Dot1XPortSecurityReAuthPeriod_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226Dot1XPortSecurityReAuthPeriod_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityReAuthPeriod_Object = MibTableColumn
es2226Dot1XPortSecurityReAuthPeriod = _Es2226Dot1XPortSecurityReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 8),
    _Es2226Dot1XPortSecurityReAuthPeriod_Type()
)
es2226Dot1XPortSecurityReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityReAuthPeriod.setStatus("current")


class _Es2226Dot1XPortSecurityMaxRequest_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityMaxRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2226Dot1XPortSecurityMaxRequest_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityMaxRequest_Object = MibTableColumn
es2226Dot1XPortSecurityMaxRequest = _Es2226Dot1XPortSecurityMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 9),
    _Es2226Dot1XPortSecurityMaxRequest_Type()
)
es2226Dot1XPortSecurityMaxRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityMaxRequest.setStatus("current")


class _Es2226Dot1XPortSecuritySuppTimeout_Type(Integer32):
    """Custom type es2226Dot1XPortSecuritySuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Es2226Dot1XPortSecuritySuppTimeout_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecuritySuppTimeout_Object = MibTableColumn
es2226Dot1XPortSecuritySuppTimeout = _Es2226Dot1XPortSecuritySuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 10),
    _Es2226Dot1XPortSecuritySuppTimeout_Type()
)
es2226Dot1XPortSecuritySuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecuritySuppTimeout.setStatus("current")


class _Es2226Dot1XPortSecurityServerTimeout_Type(Integer32):
    """Custom type es2226Dot1XPortSecurityServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Es2226Dot1XPortSecurityServerTimeout_Type.__name__ = "Integer32"
_Es2226Dot1XPortSecurityServerTimeout_Object = MibTableColumn
es2226Dot1XPortSecurityServerTimeout = _Es2226Dot1XPortSecurityServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 11),
    _Es2226Dot1XPortSecurityServerTimeout_Type()
)
es2226Dot1XPortSecurityServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityServerTimeout.setStatus("current")
_Es2226Dot1XPortSecurityStatus_Type = DisplayString
_Es2226Dot1XPortSecurityStatus_Object = MibTableColumn
es2226Dot1XPortSecurityStatus = _Es2226Dot1XPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 19, 2, 1, 1, 12),
    _Es2226Dot1XPortSecurityStatus_Type()
)
es2226Dot1XPortSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226Dot1XPortSecurityStatus.setStatus("current")
_Es2226TrapEntry_ObjectIdentity = ObjectIdentity
es2226TrapEntry = _Es2226TrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20)
)
_Es2226TrapVariable_ObjectIdentity = ObjectIdentity
es2226TrapVariable = _Es2226TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 1),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")
_Ipmacbind_Type = DisplayString
_Ipmacbind_Object = MibScalar
ipmacbind = _Ipmacbind_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 6),
    _Ipmacbind_Type()
)
ipmacbind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmacbind.setStatus("current")
_Arpinspect_Type = DisplayString
_Arpinspect_Object = MibScalar
arpinspect = _Arpinspect_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 21, 7),
    _Arpinspect_Type()
)
arpinspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpinspect.setStatus("current")
_Es2226Acl_ObjectIdentity = ObjectIdentity
es2226Acl = _Es2226Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22)
)
_Es2226HighAcl_ObjectIdentity = ObjectIdentity
es2226HighAcl = _Es2226HighAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1)
)


class _Es2226HighAclCreatStatus_Type(Integer32):
    """Custom type es2226HighAclCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226HighAclCreatStatus_Type.__name__ = "Integer32"
_Es2226HighAclCreatStatus_Object = MibScalar
es2226HighAclCreatStatus = _Es2226HighAclCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 1),
    _Es2226HighAclCreatStatus_Type()
)
es2226HighAclCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclCreatStatus.setStatus("current")


class _Es2226HighAclNumbers_Type(Integer32):
    """Custom type es2226HighAclNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Es2226HighAclNumbers_Type.__name__ = "Integer32"
_Es2226HighAclNumbers_Object = MibScalar
es2226HighAclNumbers = _Es2226HighAclNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 2),
    _Es2226HighAclNumbers_Type()
)
es2226HighAclNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226HighAclNumbers.setStatus("current")
_Es2226HighAclTable_Object = MibTable
es2226HighAclTable = _Es2226HighAclTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3)
)
if mibBuilder.loadTexts:
    es2226HighAclTable.setStatus("current")
_Es2226HighAclEntry_Object = MibTableRow
es2226HighAclEntry = _Es2226HighAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1)
)
es2226HighAclEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226HighAclIndex"),
)
if mibBuilder.loadTexts:
    es2226HighAclEntry.setStatus("current")


class _Es2226HighAclIndex_Type(Integer32):
    """Custom type es2226HighAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Es2226HighAclIndex_Type.__name__ = "Integer32"
_Es2226HighAclIndex_Object = MibTableColumn
es2226HighAclIndex = _Es2226HighAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 1),
    _Es2226HighAclIndex_Type()
)
es2226HighAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226HighAclIndex.setStatus("current")
_Es2226HighAclName_Type = DisplayString
_Es2226HighAclName_Object = MibTableColumn
es2226HighAclName = _Es2226HighAclName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 2),
    _Es2226HighAclName_Type()
)
es2226HighAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclName.setStatus("current")
_Es2226HighAclIngressPortMap_Type = DisplayString
_Es2226HighAclIngressPortMap_Object = MibTableColumn
es2226HighAclIngressPortMap = _Es2226HighAclIngressPortMap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 3),
    _Es2226HighAclIngressPortMap_Type()
)
es2226HighAclIngressPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIngressPortMap.setStatus("current")
_Es2226HighAclSMacFilter_Type = DisplayString
_Es2226HighAclSMacFilter_Object = MibTableColumn
es2226HighAclSMacFilter = _Es2226HighAclSMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 4),
    _Es2226HighAclSMacFilter_Type()
)
es2226HighAclSMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclSMacFilter.setStatus("current")
_Es2226HighAclDMacFilter_Type = DisplayString
_Es2226HighAclDMacFilter_Object = MibTableColumn
es2226HighAclDMacFilter = _Es2226HighAclDMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 5),
    _Es2226HighAclDMacFilter_Type()
)
es2226HighAclDMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclDMacFilter.setStatus("current")


class _Es2226HighAclVlanType_Type(Integer32):
    """Custom type es2226HighAclVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226HighAclVlanType_Type.__name__ = "Integer32"
_Es2226HighAclVlanType_Object = MibTableColumn
es2226HighAclVlanType = _Es2226HighAclVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 6),
    _Es2226HighAclVlanType_Type()
)
es2226HighAclVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclVlanType.setStatus("current")


class _Es2226HighAclTagVid_Type(Integer32):
    """Custom type es2226HighAclTagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226HighAclTagVid_Type.__name__ = "Integer32"
_Es2226HighAclTagVid_Object = MibTableColumn
es2226HighAclTagVid = _Es2226HighAclTagVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 7),
    _Es2226HighAclTagVid_Type()
)
es2226HighAclTagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclTagVid.setStatus("current")


class _Es2226HighAclTagPriority_Type(Integer32):
    """Custom type es2226HighAclTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226HighAclTagPriority_Type.__name__ = "Integer32"
_Es2226HighAclTagPriority_Object = MibTableColumn
es2226HighAclTagPriority = _Es2226HighAclTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 8),
    _Es2226HighAclTagPriority_Type()
)
es2226HighAclTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclTagPriority.setStatus("current")


class _Es2226HighAclEthernetType_Type(DisplayString):
    """Custom type es2226HighAclEthernetType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Es2226HighAclEthernetType_Type.__name__ = "DisplayString"
_Es2226HighAclEthernetType_Object = MibTableColumn
es2226HighAclEthernetType = _Es2226HighAclEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 9),
    _Es2226HighAclEthernetType_Type()
)
es2226HighAclEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclEthernetType.setStatus("current")


class _Es2226HighAclIPv4Protocol_Type(Integer32):
    """Custom type es2226HighAclIPv4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Es2226HighAclIPv4Protocol_Type.__name__ = "Integer32"
_Es2226HighAclIPv4Protocol_Object = MibTableColumn
es2226HighAclIPv4Protocol = _Es2226HighAclIPv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 10),
    _Es2226HighAclIPv4Protocol_Type()
)
es2226HighAclIPv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4Protocol.setStatus("current")


class _Es2226HighAclIPv4ToS_Type(DisplayString):
    """Custom type es2226HighAclIPv4ToS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Es2226HighAclIPv4ToS_Type.__name__ = "DisplayString"
_Es2226HighAclIPv4ToS_Object = MibTableColumn
es2226HighAclIPv4ToS = _Es2226HighAclIPv4ToS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 11),
    _Es2226HighAclIPv4ToS_Type()
)
es2226HighAclIPv4ToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4ToS.setStatus("current")


class _Es2226HighAclIPv4TTLRange_Type(Integer32):
    """Custom type es2226HighAclIPv4TTLRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226HighAclIPv4TTLRange_Type.__name__ = "Integer32"
_Es2226HighAclIPv4TTLRange_Object = MibTableColumn
es2226HighAclIPv4TTLRange = _Es2226HighAclIPv4TTLRange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 12),
    _Es2226HighAclIPv4TTLRange_Type()
)
es2226HighAclIPv4TTLRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4TTLRange.setStatus("current")
_Es2226HighAclIPv4DA_Type = IpAddress
_Es2226HighAclIPv4DA_Object = MibTableColumn
es2226HighAclIPv4DA = _Es2226HighAclIPv4DA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 13),
    _Es2226HighAclIPv4DA_Type()
)
es2226HighAclIPv4DA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4DA.setStatus("current")
_Es2226HighAclIPv4DAMask_Type = IpAddress
_Es2226HighAclIPv4DAMask_Object = MibTableColumn
es2226HighAclIPv4DAMask = _Es2226HighAclIPv4DAMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 14),
    _Es2226HighAclIPv4DAMask_Type()
)
es2226HighAclIPv4DAMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4DAMask.setStatus("current")
_Es2226HighAclIPv4SA_Type = IpAddress
_Es2226HighAclIPv4SA_Object = MibTableColumn
es2226HighAclIPv4SA = _Es2226HighAclIPv4SA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 15),
    _Es2226HighAclIPv4SA_Type()
)
es2226HighAclIPv4SA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4SA.setStatus("current")
_Es2226HighAclIPv4SAMask_Type = IpAddress
_Es2226HighAclIPv4SAMask_Object = MibTableColumn
es2226HighAclIPv4SAMask = _Es2226HighAclIPv4SAMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 16),
    _Es2226HighAclIPv4SAMask_Type()
)
es2226HighAclIPv4SAMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclIPv4SAMask.setStatus("current")


class _Es2226HighAclL4DestinationPort_Type(Integer32):
    """Custom type es2226HighAclL4DestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2226HighAclL4DestinationPort_Type.__name__ = "Integer32"
_Es2226HighAclL4DestinationPort_Object = MibTableColumn
es2226HighAclL4DestinationPort = _Es2226HighAclL4DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 17),
    _Es2226HighAclL4DestinationPort_Type()
)
es2226HighAclL4DestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclL4DestinationPort.setStatus("current")


class _Es2226HighAclL4SourcePort_Type(Integer32):
    """Custom type es2226HighAclL4SourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2226HighAclL4SourcePort_Type.__name__ = "Integer32"
_Es2226HighAclL4SourcePort_Object = MibTableColumn
es2226HighAclL4SourcePort = _Es2226HighAclL4SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 18),
    _Es2226HighAclL4SourcePort_Type()
)
es2226HighAclL4SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclL4SourcePort.setStatus("current")


class _Es2226HighAclActionIBForwardDecision_Type(Integer32):
    """Custom type es2226HighAclActionIBForwardDecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226HighAclActionIBForwardDecision_Type.__name__ = "Integer32"
_Es2226HighAclActionIBForwardDecision_Object = MibTableColumn
es2226HighAclActionIBForwardDecision = _Es2226HighAclActionIBForwardDecision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 19),
    _Es2226HighAclActionIBForwardDecision_Type()
)
es2226HighAclActionIBForwardDecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionIBForwardDecision.setStatus("current")


class _Es2226HighAclActionIBForwardMap_Type(Integer32):
    """Custom type es2226HighAclActionIBForwardMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Es2226HighAclActionIBForwardMap_Type.__name__ = "Integer32"
_Es2226HighAclActionIBForwardMap_Object = MibTableColumn
es2226HighAclActionIBForwardMap = _Es2226HighAclActionIBForwardMap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 20),
    _Es2226HighAclActionIBForwardMap_Type()
)
es2226HighAclActionIBForwardMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionIBForwardMap.setStatus("current")


class _Es2226HighAclActionIBModifyDSCPPacket_Type(Integer32):
    """Custom type es2226HighAclActionIBModifyDSCPPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226HighAclActionIBModifyDSCPPacket_Type.__name__ = "Integer32"
_Es2226HighAclActionIBModifyDSCPPacket_Object = MibTableColumn
es2226HighAclActionIBModifyDSCPPacket = _Es2226HighAclActionIBModifyDSCPPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 21),
    _Es2226HighAclActionIBModifyDSCPPacket_Type()
)
es2226HighAclActionIBModifyDSCPPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionIBModifyDSCPPacket.setStatus("current")


class _Es2226HighAclActionIBModifyDSCPValue_Type(Integer32):
    """Custom type es2226HighAclActionIBModifyDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2226HighAclActionIBModifyDSCPValue_Type.__name__ = "Integer32"
_Es2226HighAclActionIBModifyDSCPValue_Object = MibTableColumn
es2226HighAclActionIBModifyDSCPValue = _Es2226HighAclActionIBModifyDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 22),
    _Es2226HighAclActionIBModifyDSCPValue_Type()
)
es2226HighAclActionIBModifyDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionIBModifyDSCPValue.setStatus("current")


class _Es2226HighAclActionOBForwardDecision_Type(Integer32):
    """Custom type es2226HighAclActionOBForwardDecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226HighAclActionOBForwardDecision_Type.__name__ = "Integer32"
_Es2226HighAclActionOBForwardDecision_Object = MibTableColumn
es2226HighAclActionOBForwardDecision = _Es2226HighAclActionOBForwardDecision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 23),
    _Es2226HighAclActionOBForwardDecision_Type()
)
es2226HighAclActionOBForwardDecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionOBForwardDecision.setStatus("current")


class _Es2226HighAclActionOBForwardMap_Type(Integer32):
    """Custom type es2226HighAclActionOBForwardMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Es2226HighAclActionOBForwardMap_Type.__name__ = "Integer32"
_Es2226HighAclActionOBForwardMap_Object = MibTableColumn
es2226HighAclActionOBForwardMap = _Es2226HighAclActionOBForwardMap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 24),
    _Es2226HighAclActionOBForwardMap_Type()
)
es2226HighAclActionOBForwardMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionOBForwardMap.setStatus("current")


class _Es2226HighAclActionOBModifyDSCPPacket_Type(Integer32):
    """Custom type es2226HighAclActionOBModifyDSCPPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226HighAclActionOBModifyDSCPPacket_Type.__name__ = "Integer32"
_Es2226HighAclActionOBModifyDSCPPacket_Object = MibTableColumn
es2226HighAclActionOBModifyDSCPPacket = _Es2226HighAclActionOBModifyDSCPPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 25),
    _Es2226HighAclActionOBModifyDSCPPacket_Type()
)
es2226HighAclActionOBModifyDSCPPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionOBModifyDSCPPacket.setStatus("current")


class _Es2226HighAclActionOBModifyDSCPValue_Type(Integer32):
    """Custom type es2226HighAclActionOBModifyDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2226HighAclActionOBModifyDSCPValue_Type.__name__ = "Integer32"
_Es2226HighAclActionOBModifyDSCPValue_Object = MibTableColumn
es2226HighAclActionOBModifyDSCPValue = _Es2226HighAclActionOBModifyDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 26),
    _Es2226HighAclActionOBModifyDSCPValue_Type()
)
es2226HighAclActionOBModifyDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionOBModifyDSCPValue.setStatus("current")


class _Es2226HighAclActionModifyDot1PPacket_Type(Integer32):
    """Custom type es2226HighAclActionModifyDot1PPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226HighAclActionModifyDot1PPacket_Type.__name__ = "Integer32"
_Es2226HighAclActionModifyDot1PPacket_Object = MibTableColumn
es2226HighAclActionModifyDot1PPacket = _Es2226HighAclActionModifyDot1PPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 27),
    _Es2226HighAclActionModifyDot1PPacket_Type()
)
es2226HighAclActionModifyDot1PPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionModifyDot1PPacket.setStatus("current")


class _Es2226HighAclActionModifyDot1PValue_Type(Integer32):
    """Custom type es2226HighAclActionModifyDot1PValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226HighAclActionModifyDot1PValue_Type.__name__ = "Integer32"
_Es2226HighAclActionModifyDot1PValue_Object = MibTableColumn
es2226HighAclActionModifyDot1PValue = _Es2226HighAclActionModifyDot1PValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 28),
    _Es2226HighAclActionModifyDot1PValue_Type()
)
es2226HighAclActionModifyDot1PValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionModifyDot1PValue.setStatus("current")


class _Es2226HighAclActionModifyQoSPacket_Type(Integer32):
    """Custom type es2226HighAclActionModifyQoSPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226HighAclActionModifyQoSPacket_Type.__name__ = "Integer32"
_Es2226HighAclActionModifyQoSPacket_Object = MibTableColumn
es2226HighAclActionModifyQoSPacket = _Es2226HighAclActionModifyQoSPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 29),
    _Es2226HighAclActionModifyQoSPacket_Type()
)
es2226HighAclActionModifyQoSPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionModifyQoSPacket.setStatus("current")


class _Es2226HighAclActionModifyQoSValue_Type(Integer32):
    """Custom type es2226HighAclActionModifyQoSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226HighAclActionModifyQoSValue_Type.__name__ = "Integer32"
_Es2226HighAclActionModifyQoSValue_Object = MibTableColumn
es2226HighAclActionModifyQoSValue = _Es2226HighAclActionModifyQoSValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 30),
    _Es2226HighAclActionModifyQoSValue_Type()
)
es2226HighAclActionModifyQoSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclActionModifyQoSValue.setStatus("current")


class _Es2226HighAclRateMeter_Type(Integer32):
    """Custom type es2226HighAclRateMeter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_Es2226HighAclRateMeter_Type.__name__ = "Integer32"
_Es2226HighAclRateMeter_Object = MibTableColumn
es2226HighAclRateMeter = _Es2226HighAclRateMeter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 31),
    _Es2226HighAclRateMeter_Type()
)
es2226HighAclRateMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclRateMeter.setStatus("current")


class _Es2226HighAclRowStatus_Type(Integer32):
    """Custom type es2226HighAclRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226HighAclRowStatus_Type.__name__ = "Integer32"
_Es2226HighAclRowStatus_Object = MibTableColumn
es2226HighAclRowStatus = _Es2226HighAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 1, 3, 1, 32),
    _Es2226HighAclRowStatus_Type()
)
es2226HighAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226HighAclRowStatus.setStatus("current")
_Es2226LowAcl_ObjectIdentity = ObjectIdentity
es2226LowAcl = _Es2226LowAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2)
)


class _Es2226LowAclCreatStatus_Type(Integer32):
    """Custom type es2226LowAclCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LowAclCreatStatus_Type.__name__ = "Integer32"
_Es2226LowAclCreatStatus_Object = MibScalar
es2226LowAclCreatStatus = _Es2226LowAclCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 1),
    _Es2226LowAclCreatStatus_Type()
)
es2226LowAclCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclCreatStatus.setStatus("current")


class _Es2226LowAclNumbers_Type(Integer32):
    """Custom type es2226LowAclNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Es2226LowAclNumbers_Type.__name__ = "Integer32"
_Es2226LowAclNumbers_Object = MibScalar
es2226LowAclNumbers = _Es2226LowAclNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 2),
    _Es2226LowAclNumbers_Type()
)
es2226LowAclNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226LowAclNumbers.setStatus("current")
_Es2226LowAclTable_Object = MibTable
es2226LowAclTable = _Es2226LowAclTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3)
)
if mibBuilder.loadTexts:
    es2226LowAclTable.setStatus("current")
_Es2226LowAclEntry_Object = MibTableRow
es2226LowAclEntry = _Es2226LowAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1)
)
es2226LowAclEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226LowAclIndex"),
)
if mibBuilder.loadTexts:
    es2226LowAclEntry.setStatus("current")


class _Es2226LowAclIndex_Type(Integer32):
    """Custom type es2226LowAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Es2226LowAclIndex_Type.__name__ = "Integer32"
_Es2226LowAclIndex_Object = MibTableColumn
es2226LowAclIndex = _Es2226LowAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 1),
    _Es2226LowAclIndex_Type()
)
es2226LowAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226LowAclIndex.setStatus("current")
_Es2226LowAclName_Type = DisplayString
_Es2226LowAclName_Object = MibTableColumn
es2226LowAclName = _Es2226LowAclName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 2),
    _Es2226LowAclName_Type()
)
es2226LowAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclName.setStatus("current")
_Es2226LowAclIngressPortMap_Type = DisplayString
_Es2226LowAclIngressPortMap_Object = MibTableColumn
es2226LowAclIngressPortMap = _Es2226LowAclIngressPortMap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 3),
    _Es2226LowAclIngressPortMap_Type()
)
es2226LowAclIngressPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIngressPortMap.setStatus("current")
_Es2226LowAclSMacFilter_Type = DisplayString
_Es2226LowAclSMacFilter_Object = MibTableColumn
es2226LowAclSMacFilter = _Es2226LowAclSMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 4),
    _Es2226LowAclSMacFilter_Type()
)
es2226LowAclSMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclSMacFilter.setStatus("current")
_Es2226LowAclDMacFilter_Type = DisplayString
_Es2226LowAclDMacFilter_Object = MibTableColumn
es2226LowAclDMacFilter = _Es2226LowAclDMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 5),
    _Es2226LowAclDMacFilter_Type()
)
es2226LowAclDMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclDMacFilter.setStatus("current")


class _Es2226LowAclVlanType_Type(Integer32):
    """Custom type es2226LowAclVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LowAclVlanType_Type.__name__ = "Integer32"
_Es2226LowAclVlanType_Object = MibTableColumn
es2226LowAclVlanType = _Es2226LowAclVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 6),
    _Es2226LowAclVlanType_Type()
)
es2226LowAclVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclVlanType.setStatus("current")


class _Es2226LowAclTagVid_Type(Integer32):
    """Custom type es2226LowAclTagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226LowAclTagVid_Type.__name__ = "Integer32"
_Es2226LowAclTagVid_Object = MibTableColumn
es2226LowAclTagVid = _Es2226LowAclTagVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 7),
    _Es2226LowAclTagVid_Type()
)
es2226LowAclTagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclTagVid.setStatus("current")


class _Es2226LowAclTagPriority_Type(Integer32):
    """Custom type es2226LowAclTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226LowAclTagPriority_Type.__name__ = "Integer32"
_Es2226LowAclTagPriority_Object = MibTableColumn
es2226LowAclTagPriority = _Es2226LowAclTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 8),
    _Es2226LowAclTagPriority_Type()
)
es2226LowAclTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclTagPriority.setStatus("current")


class _Es2226LowAclEthernetType_Type(DisplayString):
    """Custom type es2226LowAclEthernetType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Es2226LowAclEthernetType_Type.__name__ = "DisplayString"
_Es2226LowAclEthernetType_Object = MibTableColumn
es2226LowAclEthernetType = _Es2226LowAclEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 9),
    _Es2226LowAclEthernetType_Type()
)
es2226LowAclEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclEthernetType.setStatus("current")


class _Es2226LowAclIPv4Protocol_Type(Integer32):
    """Custom type es2226LowAclIPv4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Es2226LowAclIPv4Protocol_Type.__name__ = "Integer32"
_Es2226LowAclIPv4Protocol_Object = MibTableColumn
es2226LowAclIPv4Protocol = _Es2226LowAclIPv4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 10),
    _Es2226LowAclIPv4Protocol_Type()
)
es2226LowAclIPv4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4Protocol.setStatus("current")


class _Es2226LowAclIPv4ToS_Type(DisplayString):
    """Custom type es2226LowAclIPv4ToS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Es2226LowAclIPv4ToS_Type.__name__ = "DisplayString"
_Es2226LowAclIPv4ToS_Object = MibTableColumn
es2226LowAclIPv4ToS = _Es2226LowAclIPv4ToS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 11),
    _Es2226LowAclIPv4ToS_Type()
)
es2226LowAclIPv4ToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4ToS.setStatus("current")


class _Es2226LowAclIPv4TTLRange_Type(Integer32):
    """Custom type es2226LowAclIPv4TTLRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226LowAclIPv4TTLRange_Type.__name__ = "Integer32"
_Es2226LowAclIPv4TTLRange_Object = MibTableColumn
es2226LowAclIPv4TTLRange = _Es2226LowAclIPv4TTLRange_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 12),
    _Es2226LowAclIPv4TTLRange_Type()
)
es2226LowAclIPv4TTLRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4TTLRange.setStatus("current")
_Es2226LowAclIPv4DA_Type = IpAddress
_Es2226LowAclIPv4DA_Object = MibTableColumn
es2226LowAclIPv4DA = _Es2226LowAclIPv4DA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 13),
    _Es2226LowAclIPv4DA_Type()
)
es2226LowAclIPv4DA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4DA.setStatus("current")
_Es2226LowAclIPv4DAMask_Type = IpAddress
_Es2226LowAclIPv4DAMask_Object = MibTableColumn
es2226LowAclIPv4DAMask = _Es2226LowAclIPv4DAMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 14),
    _Es2226LowAclIPv4DAMask_Type()
)
es2226LowAclIPv4DAMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4DAMask.setStatus("current")
_Es2226LowAclIPv4SA_Type = IpAddress
_Es2226LowAclIPv4SA_Object = MibTableColumn
es2226LowAclIPv4SA = _Es2226LowAclIPv4SA_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 15),
    _Es2226LowAclIPv4SA_Type()
)
es2226LowAclIPv4SA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4SA.setStatus("current")
_Es2226LowAclIPv4SAMask_Type = IpAddress
_Es2226LowAclIPv4SAMask_Object = MibTableColumn
es2226LowAclIPv4SAMask = _Es2226LowAclIPv4SAMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 16),
    _Es2226LowAclIPv4SAMask_Type()
)
es2226LowAclIPv4SAMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclIPv4SAMask.setStatus("current")


class _Es2226LowAclL4DestinationPort_Type(Integer32):
    """Custom type es2226LowAclL4DestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2226LowAclL4DestinationPort_Type.__name__ = "Integer32"
_Es2226LowAclL4DestinationPort_Object = MibTableColumn
es2226LowAclL4DestinationPort = _Es2226LowAclL4DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 17),
    _Es2226LowAclL4DestinationPort_Type()
)
es2226LowAclL4DestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclL4DestinationPort.setStatus("current")


class _Es2226LowAclL4SourcePort_Type(Integer32):
    """Custom type es2226LowAclL4SourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2226LowAclL4SourcePort_Type.__name__ = "Integer32"
_Es2226LowAclL4SourcePort_Object = MibTableColumn
es2226LowAclL4SourcePort = _Es2226LowAclL4SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 18),
    _Es2226LowAclL4SourcePort_Type()
)
es2226LowAclL4SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclL4SourcePort.setStatus("current")


class _Es2226LowAclActionIBForwardDecision_Type(Integer32):
    """Custom type es2226LowAclActionIBForwardDecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226LowAclActionIBForwardDecision_Type.__name__ = "Integer32"
_Es2226LowAclActionIBForwardDecision_Object = MibTableColumn
es2226LowAclActionIBForwardDecision = _Es2226LowAclActionIBForwardDecision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 19),
    _Es2226LowAclActionIBForwardDecision_Type()
)
es2226LowAclActionIBForwardDecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionIBForwardDecision.setStatus("current")


class _Es2226LowAclActionIBForwardMap_Type(Integer32):
    """Custom type es2226LowAclActionIBForwardMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Es2226LowAclActionIBForwardMap_Type.__name__ = "Integer32"
_Es2226LowAclActionIBForwardMap_Object = MibTableColumn
es2226LowAclActionIBForwardMap = _Es2226LowAclActionIBForwardMap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 20),
    _Es2226LowAclActionIBForwardMap_Type()
)
es2226LowAclActionIBForwardMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionIBForwardMap.setStatus("current")


class _Es2226LowAclActionIBModifyDSCPPacket_Type(Integer32):
    """Custom type es2226LowAclActionIBModifyDSCPPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LowAclActionIBModifyDSCPPacket_Type.__name__ = "Integer32"
_Es2226LowAclActionIBModifyDSCPPacket_Object = MibTableColumn
es2226LowAclActionIBModifyDSCPPacket = _Es2226LowAclActionIBModifyDSCPPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 21),
    _Es2226LowAclActionIBModifyDSCPPacket_Type()
)
es2226LowAclActionIBModifyDSCPPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionIBModifyDSCPPacket.setStatus("current")


class _Es2226LowAclActionIBModifyDSCPValue_Type(Integer32):
    """Custom type es2226LowAclActionIBModifyDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2226LowAclActionIBModifyDSCPValue_Type.__name__ = "Integer32"
_Es2226LowAclActionIBModifyDSCPValue_Object = MibTableColumn
es2226LowAclActionIBModifyDSCPValue = _Es2226LowAclActionIBModifyDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 22),
    _Es2226LowAclActionIBModifyDSCPValue_Type()
)
es2226LowAclActionIBModifyDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionIBModifyDSCPValue.setStatus("current")


class _Es2226LowAclActionOBForwardDecision_Type(Integer32):
    """Custom type es2226LowAclActionOBForwardDecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226LowAclActionOBForwardDecision_Type.__name__ = "Integer32"
_Es2226LowAclActionOBForwardDecision_Object = MibTableColumn
es2226LowAclActionOBForwardDecision = _Es2226LowAclActionOBForwardDecision_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 23),
    _Es2226LowAclActionOBForwardDecision_Type()
)
es2226LowAclActionOBForwardDecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionOBForwardDecision.setStatus("current")


class _Es2226LowAclActionOBForwardMap_Type(Integer32):
    """Custom type es2226LowAclActionOBForwardMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_Es2226LowAclActionOBForwardMap_Type.__name__ = "Integer32"
_Es2226LowAclActionOBForwardMap_Object = MibTableColumn
es2226LowAclActionOBForwardMap = _Es2226LowAclActionOBForwardMap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 24),
    _Es2226LowAclActionOBForwardMap_Type()
)
es2226LowAclActionOBForwardMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionOBForwardMap.setStatus("current")


class _Es2226LowAclActionOBModifyDSCPPacket_Type(Integer32):
    """Custom type es2226LowAclActionOBModifyDSCPPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LowAclActionOBModifyDSCPPacket_Type.__name__ = "Integer32"
_Es2226LowAclActionOBModifyDSCPPacket_Object = MibTableColumn
es2226LowAclActionOBModifyDSCPPacket = _Es2226LowAclActionOBModifyDSCPPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 25),
    _Es2226LowAclActionOBModifyDSCPPacket_Type()
)
es2226LowAclActionOBModifyDSCPPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionOBModifyDSCPPacket.setStatus("current")


class _Es2226LowAclActionOBModifyDSCPValue_Type(Integer32):
    """Custom type es2226LowAclActionOBModifyDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2226LowAclActionOBModifyDSCPValue_Type.__name__ = "Integer32"
_Es2226LowAclActionOBModifyDSCPValue_Object = MibTableColumn
es2226LowAclActionOBModifyDSCPValue = _Es2226LowAclActionOBModifyDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 26),
    _Es2226LowAclActionOBModifyDSCPValue_Type()
)
es2226LowAclActionOBModifyDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionOBModifyDSCPValue.setStatus("current")


class _Es2226LowAclActionModifyDot1PPacket_Type(Integer32):
    """Custom type es2226LowAclActionModifyDot1PPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LowAclActionModifyDot1PPacket_Type.__name__ = "Integer32"
_Es2226LowAclActionModifyDot1PPacket_Object = MibTableColumn
es2226LowAclActionModifyDot1PPacket = _Es2226LowAclActionModifyDot1PPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 27),
    _Es2226LowAclActionModifyDot1PPacket_Type()
)
es2226LowAclActionModifyDot1PPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionModifyDot1PPacket.setStatus("current")


class _Es2226LowAclActionModifyDot1PValue_Type(Integer32):
    """Custom type es2226LowAclActionModifyDot1PValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2226LowAclActionModifyDot1PValue_Type.__name__ = "Integer32"
_Es2226LowAclActionModifyDot1PValue_Object = MibTableColumn
es2226LowAclActionModifyDot1PValue = _Es2226LowAclActionModifyDot1PValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 28),
    _Es2226LowAclActionModifyDot1PValue_Type()
)
es2226LowAclActionModifyDot1PValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionModifyDot1PValue.setStatus("current")


class _Es2226LowAclActionModifyQoSPacket_Type(Integer32):
    """Custom type es2226LowAclActionModifyQoSPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226LowAclActionModifyQoSPacket_Type.__name__ = "Integer32"
_Es2226LowAclActionModifyQoSPacket_Object = MibTableColumn
es2226LowAclActionModifyQoSPacket = _Es2226LowAclActionModifyQoSPacket_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 29),
    _Es2226LowAclActionModifyQoSPacket_Type()
)
es2226LowAclActionModifyQoSPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionModifyQoSPacket.setStatus("current")


class _Es2226LowAclActionModifyQoSValue_Type(Integer32):
    """Custom type es2226LowAclActionModifyQoSValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2226LowAclActionModifyQoSValue_Type.__name__ = "Integer32"
_Es2226LowAclActionModifyQoSValue_Object = MibTableColumn
es2226LowAclActionModifyQoSValue = _Es2226LowAclActionModifyQoSValue_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 30),
    _Es2226LowAclActionModifyQoSValue_Type()
)
es2226LowAclActionModifyQoSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclActionModifyQoSValue.setStatus("current")


class _Es2226LowAclRateMeter_Type(Integer32):
    """Custom type es2226LowAclRateMeter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_Es2226LowAclRateMeter_Type.__name__ = "Integer32"
_Es2226LowAclRateMeter_Object = MibTableColumn
es2226LowAclRateMeter = _Es2226LowAclRateMeter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 31),
    _Es2226LowAclRateMeter_Type()
)
es2226LowAclRateMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclRateMeter.setStatus("current")


class _Es2226LowAclRowStatus_Type(Integer32):
    """Custom type es2226LowAclRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226LowAclRowStatus_Type.__name__ = "Integer32"
_Es2226LowAclRowStatus_Object = MibTableColumn
es2226LowAclRowStatus = _Es2226LowAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 22, 2, 3, 1, 32),
    _Es2226LowAclRowStatus_Type()
)
es2226LowAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LowAclRowStatus.setStatus("current")
_Es2226TrunkInfo_ObjectIdentity = ObjectIdentity
es2226TrunkInfo = _Es2226TrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23)
)
_Es2226TrunkPort_ObjectIdentity = ObjectIdentity
es2226TrunkPort = _Es2226TrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1)
)
_Es2226TrunkPortTable_Object = MibTable
es2226TrunkPortTable = _Es2226TrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    es2226TrunkPortTable.setStatus("current")
_Es2226TrunkPortEntry_Object = MibTableRow
es2226TrunkPortEntry = _Es2226TrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1)
)
es2226TrunkPortEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226TrunkPortIndex"),
)
if mibBuilder.loadTexts:
    es2226TrunkPortEntry.setStatus("current")


class _Es2226TrunkPortIndex_Type(Integer32):
    """Custom type es2226TrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226TrunkPortIndex_Type.__name__ = "Integer32"
_Es2226TrunkPortIndex_Object = MibTableColumn
es2226TrunkPortIndex = _Es2226TrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 1),
    _Es2226TrunkPortIndex_Type()
)
es2226TrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226TrunkPortIndex.setStatus("current")


class _Es2226TrunkPortMethod_Type(Integer32):
    """Custom type es2226TrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226TrunkPortMethod_Type.__name__ = "Integer32"
_Es2226TrunkPortMethod_Object = MibTableColumn
es2226TrunkPortMethod = _Es2226TrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 2),
    _Es2226TrunkPortMethod_Type()
)
es2226TrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrunkPortMethod.setStatus("current")


class _Es2226TrunkPortGroup_Type(Integer32):
    """Custom type es2226TrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Es2226TrunkPortGroup_Type.__name__ = "Integer32"
_Es2226TrunkPortGroup_Object = MibTableColumn
es2226TrunkPortGroup = _Es2226TrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 3),
    _Es2226TrunkPortGroup_Type()
)
es2226TrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrunkPortGroup.setStatus("current")


class _Es2226TrunkPortActiveLacp_Type(Integer32):
    """Custom type es2226TrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226TrunkPortActiveLacp_Type.__name__ = "Integer32"
_Es2226TrunkPortActiveLacp_Object = MibTableColumn
es2226TrunkPortActiveLacp = _Es2226TrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 4),
    _Es2226TrunkPortActiveLacp_Type()
)
es2226TrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrunkPortActiveLacp.setStatus("current")


class _Es2226TrunkPortAggtr_Type(Integer32):
    """Custom type es2226TrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226TrunkPortAggtr_Type.__name__ = "Integer32"
_Es2226TrunkPortAggtr_Object = MibTableColumn
es2226TrunkPortAggtr = _Es2226TrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 5),
    _Es2226TrunkPortAggtr_Type()
)
es2226TrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226TrunkPortAggtr.setStatus("current")


class _Es2226TrunkPortStatus_Type(Integer32):
    """Custom type es2226TrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226TrunkPortStatus_Type.__name__ = "Integer32"
_Es2226TrunkPortStatus_Object = MibTableColumn
es2226TrunkPortStatus = _Es2226TrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 6),
    _Es2226TrunkPortStatus_Type()
)
es2226TrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226TrunkPortStatus.setStatus("current")


class _Es2226TrunkPortCurrentMode_Type(Integer32):
    """Custom type es2226TrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226TrunkPortCurrentMode_Type.__name__ = "Integer32"
_Es2226TrunkPortCurrentMode_Object = MibTableColumn
es2226TrunkPortCurrentMode = _Es2226TrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 1, 1, 1, 7),
    _Es2226TrunkPortCurrentMode_Type()
)
es2226TrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226TrunkPortCurrentMode.setStatus("current")
_Es2226AggregatorView_ObjectIdentity = ObjectIdentity
es2226AggregatorView = _Es2226AggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2)
)
_Es2226AggregatorViewTable_Object = MibTable
es2226AggregatorViewTable = _Es2226AggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    es2226AggregatorViewTable.setStatus("current")
_Es2226AggregatorViewEntry_Object = MibTableRow
es2226AggregatorViewEntry = _Es2226AggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2, 1, 1)
)
es2226AggregatorViewEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226AggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    es2226AggregatorViewEntry.setStatus("current")


class _Es2226AggregatorViewIndex_Type(Integer32):
    """Custom type es2226AggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226AggregatorViewIndex_Type.__name__ = "Integer32"
_Es2226AggregatorViewIndex_Object = MibTableColumn
es2226AggregatorViewIndex = _Es2226AggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2, 1, 1, 1),
    _Es2226AggregatorViewIndex_Type()
)
es2226AggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226AggregatorViewIndex.setStatus("current")


class _Es2226AggregatorViewMethod_Type(Integer32):
    """Custom type es2226AggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226AggregatorViewMethod_Type.__name__ = "Integer32"
_Es2226AggregatorViewMethod_Object = MibTableColumn
es2226AggregatorViewMethod = _Es2226AggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2, 1, 1, 2),
    _Es2226AggregatorViewMethod_Type()
)
es2226AggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226AggregatorViewMethod.setStatus("current")
_Es2226AggregatorViewMemberPorts_Type = DisplayString
_Es2226AggregatorViewMemberPorts_Object = MibTableColumn
es2226AggregatorViewMemberPorts = _Es2226AggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2, 1, 1, 3),
    _Es2226AggregatorViewMemberPorts_Type()
)
es2226AggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226AggregatorViewMemberPorts.setStatus("current")
_Es2226AggregatorViewReadyPorts_Type = DisplayString
_Es2226AggregatorViewReadyPorts_Object = MibTableColumn
es2226AggregatorViewReadyPorts = _Es2226AggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 2, 1, 1, 4),
    _Es2226AggregatorViewReadyPorts_Type()
)
es2226AggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226AggregatorViewReadyPorts.setStatus("current")
_Es2226LacpSystemConfiguration_ObjectIdentity = ObjectIdentity
es2226LacpSystemConfiguration = _Es2226LacpSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 3)
)


class _Es2226LacpSystemPriority_Type(Integer32):
    """Custom type es2226LacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226LacpSystemPriority_Type.__name__ = "Integer32"
_Es2226LacpSystemPriority_Object = MibScalar
es2226LacpSystemPriority = _Es2226LacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 3, 1),
    _Es2226LacpSystemPriority_Type()
)
es2226LacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LacpSystemPriority.setStatus("current")


class _Es2226LacpSystemHashMethod_Type(Integer32):
    """Custom type es2226LacpSystemHashMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Es2226LacpSystemHashMethod_Type.__name__ = "Integer32"
_Es2226LacpSystemHashMethod_Object = MibScalar
es2226LacpSystemHashMethod = _Es2226LacpSystemHashMethod_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 23, 3, 2),
    _Es2226LacpSystemHashMethod_Type()
)
es2226LacpSystemHashMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226LacpSystemHashMethod.setStatus("current")
_Es2226Dhcprelay_ObjectIdentity = ObjectIdentity
es2226Dhcprelay = _Es2226Dhcprelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25)
)


class _Es2226DhcpRelayState_Type(Integer32):
    """Custom type es2226DhcpRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpRelayState_Type.__name__ = "Integer32"
_Es2226DhcpRelayState_Object = MibScalar
es2226DhcpRelayState = _Es2226DhcpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25, 1),
    _Es2226DhcpRelayState_Type()
)
es2226DhcpRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpRelayState.setStatus("current")


class _Es2226DhcpRelayLifeTime_Type(Integer32):
    """Custom type es2226DhcpRelayLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2226DhcpRelayLifeTime_Type.__name__ = "Integer32"
_Es2226DhcpRelayLifeTime_Object = MibScalar
es2226DhcpRelayLifeTime = _Es2226DhcpRelayLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25, 2),
    _Es2226DhcpRelayLifeTime_Type()
)
es2226DhcpRelayLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpRelayLifeTime.setStatus("current")


class _Es2226DhcpRelayOption82_Type(Integer32):
    """Custom type es2226DhcpRelayOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226DhcpRelayOption82_Type.__name__ = "Integer32"
_Es2226DhcpRelayOption82_Object = MibScalar
es2226DhcpRelayOption82 = _Es2226DhcpRelayOption82_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25, 3),
    _Es2226DhcpRelayOption82_Type()
)
es2226DhcpRelayOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpRelayOption82.setStatus("current")


class _Es2226DhcpRelayOption82Action_Type(Integer32):
    """Custom type es2226DhcpRelayOption82Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226DhcpRelayOption82Action_Type.__name__ = "Integer32"
_Es2226DhcpRelayOption82Action_Object = MibScalar
es2226DhcpRelayOption82Action = _Es2226DhcpRelayOption82Action_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25, 4),
    _Es2226DhcpRelayOption82Action_Type()
)
es2226DhcpRelayOption82Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpRelayOption82Action.setStatus("current")
_Es2226DhcpRelayServerPort_Type = DisplayString
_Es2226DhcpRelayServerPort_Object = MibScalar
es2226DhcpRelayServerPort = _Es2226DhcpRelayServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25, 5),
    _Es2226DhcpRelayServerPort_Type()
)
es2226DhcpRelayServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpRelayServerPort.setStatus("current")
_Es2226DhcpRelayServerIP_Type = IpAddress
_Es2226DhcpRelayServerIP_Object = MibScalar
es2226DhcpRelayServerIP = _Es2226DhcpRelayServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 25, 6),
    _Es2226DhcpRelayServerIP_Type()
)
es2226DhcpRelayServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226DhcpRelayServerIP.setStatus("current")
_Es2226Multicast_ObjectIdentity = ObjectIdentity
es2226Multicast = _Es2226Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26)
)
_Es2226IgmpSetting_ObjectIdentity = ObjectIdentity
es2226IgmpSetting = _Es2226IgmpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1)
)


class _Es2226IgmpSnoopingState_Type(Integer32):
    """Custom type es2226IgmpSnoopingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IgmpSnoopingState_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingState_Object = MibScalar
es2226IgmpSnoopingState = _Es2226IgmpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 1),
    _Es2226IgmpSnoopingState_Type()
)
es2226IgmpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingState.setStatus("current")


class _Es2226IgmpSnoopingUnregisterMulticastFlooding_Type(Integer32):
    """Custom type es2226IgmpSnoopingUnregisterMulticastFlooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IgmpSnoopingUnregisterMulticastFlooding_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingUnregisterMulticastFlooding_Object = MibScalar
es2226IgmpSnoopingUnregisterMulticastFlooding = _Es2226IgmpSnoopingUnregisterMulticastFlooding_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 2),
    _Es2226IgmpSnoopingUnregisterMulticastFlooding_Type()
)
es2226IgmpSnoopingUnregisterMulticastFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingUnregisterMulticastFlooding.setStatus("current")


class _Es2226IgmpSnoopingGeneralQueryInterval_Type(Integer32):
    """Custom type es2226IgmpSnoopingGeneralQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Es2226IgmpSnoopingGeneralQueryInterval_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingGeneralQueryInterval_Object = MibScalar
es2226IgmpSnoopingGeneralQueryInterval = _Es2226IgmpSnoopingGeneralQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 3),
    _Es2226IgmpSnoopingGeneralQueryInterval_Type()
)
es2226IgmpSnoopingGeneralQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingGeneralQueryInterval.setStatus("current")


class _Es2226IgmpSnoopingGeneralQueryMaxResponseTime_Type(Integer32):
    """Custom type es2226IgmpSnoopingGeneralQueryMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2226IgmpSnoopingGeneralQueryMaxResponseTime_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingGeneralQueryMaxResponseTime_Object = MibScalar
es2226IgmpSnoopingGeneralQueryMaxResponseTime = _Es2226IgmpSnoopingGeneralQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 4),
    _Es2226IgmpSnoopingGeneralQueryMaxResponseTime_Type()
)
es2226IgmpSnoopingGeneralQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingGeneralQueryMaxResponseTime.setStatus("current")


class _Es2226IgmpSnoopingGeneralQueryTimeout_Type(Integer32):
    """Custom type es2226IgmpSnoopingGeneralQueryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Es2226IgmpSnoopingGeneralQueryTimeout_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingGeneralQueryTimeout_Object = MibScalar
es2226IgmpSnoopingGeneralQueryTimeout = _Es2226IgmpSnoopingGeneralQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 5),
    _Es2226IgmpSnoopingGeneralQueryTimeout_Type()
)
es2226IgmpSnoopingGeneralQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingGeneralQueryTimeout.setStatus("current")


class _Es2226IgmpSnoopingSpecificQueryCount_Type(Integer32):
    """Custom type es2226IgmpSnoopingSpecificQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2226IgmpSnoopingSpecificQueryCount_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingSpecificQueryCount_Object = MibScalar
es2226IgmpSnoopingSpecificQueryCount = _Es2226IgmpSnoopingSpecificQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 6),
    _Es2226IgmpSnoopingSpecificQueryCount_Type()
)
es2226IgmpSnoopingSpecificQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSpecificQueryCount.setStatus("current")


class _Es2226IgmpSnoopingSpecificQueryMaxResponseTime_Type(Integer32):
    """Custom type es2226IgmpSnoopingSpecificQueryMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2226IgmpSnoopingSpecificQueryMaxResponseTime_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingSpecificQueryMaxResponseTime_Object = MibScalar
es2226IgmpSnoopingSpecificQueryMaxResponseTime = _Es2226IgmpSnoopingSpecificQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 7),
    _Es2226IgmpSnoopingSpecificQueryMaxResponseTime_Type()
)
es2226IgmpSnoopingSpecificQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSpecificQueryMaxResponseTime.setStatus("current")


class _Es2226IgmpSnoopingSpecificQueryTimeout_Type(Integer32):
    """Custom type es2226IgmpSnoopingSpecificQueryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Es2226IgmpSnoopingSpecificQueryTimeout_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingSpecificQueryTimeout_Object = MibScalar
es2226IgmpSnoopingSpecificQueryTimeout = _Es2226IgmpSnoopingSpecificQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 8),
    _Es2226IgmpSnoopingSpecificQueryTimeout_Type()
)
es2226IgmpSnoopingSpecificQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSpecificQueryTimeout.setStatus("current")
_Es2226IgmpSnoopingSettingTable_Object = MibTable
es2226IgmpSnoopingSettingTable = _Es2226IgmpSnoopingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 9)
)
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSettingTable.setStatus("current")
_Es2226IgmpSnoopingSettingEntry_Object = MibTableRow
es2226IgmpSnoopingSettingEntry = _Es2226IgmpSnoopingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 9, 1)
)
es2226IgmpSnoopingSettingEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226IgmpSnoopingSettingPortIndex"),
)
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSettingEntry.setStatus("current")


class _Es2226IgmpSnoopingSettingPortIndex_Type(Integer32):
    """Custom type es2226IgmpSnoopingSettingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226IgmpSnoopingSettingPortIndex_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingSettingPortIndex_Object = MibTableColumn
es2226IgmpSnoopingSettingPortIndex = _Es2226IgmpSnoopingSettingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 9, 1, 1),
    _Es2226IgmpSnoopingSettingPortIndex_Type()
)
es2226IgmpSnoopingSettingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSettingPortIndex.setStatus("current")


class _Es2226IgmpSnoopingSettingMulticastGroupLimit_Type(Integer32):
    """Custom type es2226IgmpSnoopingSettingMulticastGroupLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Es2226IgmpSnoopingSettingMulticastGroupLimit_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingSettingMulticastGroupLimit_Object = MibTableColumn
es2226IgmpSnoopingSettingMulticastGroupLimit = _Es2226IgmpSnoopingSettingMulticastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 9, 1, 2),
    _Es2226IgmpSnoopingSettingMulticastGroupLimit_Type()
)
es2226IgmpSnoopingSettingMulticastGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSettingMulticastGroupLimit.setStatus("current")


class _Es2226IgmpSnoopingSettingIGMPRouter_Type(Integer32):
    """Custom type es2226IgmpSnoopingSettingIGMPRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226IgmpSnoopingSettingIGMPRouter_Type.__name__ = "Integer32"
_Es2226IgmpSnoopingSettingIGMPRouter_Object = MibTableColumn
es2226IgmpSnoopingSettingIGMPRouter = _Es2226IgmpSnoopingSettingIGMPRouter_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 1, 9, 1, 3),
    _Es2226IgmpSnoopingSettingIGMPRouter_Type()
)
es2226IgmpSnoopingSettingIGMPRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpSnoopingSettingIGMPRouter.setStatus("current")
_Es2226IgmpVlan_ObjectIdentity = ObjectIdentity
es2226IgmpVlan = _Es2226IgmpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2)
)


class _Es2226IgmpVlanNumbers_Type(Integer32):
    """Custom type es2226IgmpVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Es2226IgmpVlanNumbers_Type.__name__ = "Integer32"
_Es2226IgmpVlanNumbers_Object = MibScalar
es2226IgmpVlanNumbers = _Es2226IgmpVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 1),
    _Es2226IgmpVlanNumbers_Type()
)
es2226IgmpVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226IgmpVlanNumbers.setStatus("current")


class _Es2226IgmpVlanCreatStatus_Type(Integer32):
    """Custom type es2226IgmpVlanCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226IgmpVlanCreatStatus_Type.__name__ = "Integer32"
_Es2226IgmpVlanCreatStatus_Object = MibScalar
es2226IgmpVlanCreatStatus = _Es2226IgmpVlanCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 2),
    _Es2226IgmpVlanCreatStatus_Type()
)
es2226IgmpVlanCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanCreatStatus.setStatus("current")
_Es2226IgmpVlanTable_Object = MibTable
es2226IgmpVlanTable = _Es2226IgmpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 3)
)
if mibBuilder.loadTexts:
    es2226IgmpVlanTable.setStatus("current")
_Es2226IgmpVlanEntry_Object = MibTableRow
es2226IgmpVlanEntry = _Es2226IgmpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 3, 1)
)
es2226IgmpVlanEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226IgmpVlanIndex"),
)
if mibBuilder.loadTexts:
    es2226IgmpVlanEntry.setStatus("current")


class _Es2226IgmpVlanIndex_Type(Integer32):
    """Custom type es2226IgmpVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2226IgmpVlanIndex_Type.__name__ = "Integer32"
_Es2226IgmpVlanIndex_Object = MibTableColumn
es2226IgmpVlanIndex = _Es2226IgmpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 3, 1, 1),
    _Es2226IgmpVlanIndex_Type()
)
es2226IgmpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226IgmpVlanIndex.setStatus("current")


class _Es2226IgmpVlanVid_Type(Integer32):
    """Custom type es2226IgmpVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226IgmpVlanVid_Type.__name__ = "Integer32"
_Es2226IgmpVlanVid_Object = MibTableColumn
es2226IgmpVlanVid = _Es2226IgmpVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 3, 1, 2),
    _Es2226IgmpVlanVid_Type()
)
es2226IgmpVlanVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226IgmpVlanVid.setStatus("current")


class _Es2226IgmpVlanRowStatus_Type(Integer32):
    """Custom type es2226IgmpVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226IgmpVlanRowStatus_Type.__name__ = "Integer32"
_Es2226IgmpVlanRowStatus_Object = MibTableColumn
es2226IgmpVlanRowStatus = _Es2226IgmpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 2, 3, 1, 3),
    _Es2226IgmpVlanRowStatus_Type()
)
es2226IgmpVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanRowStatus.setStatus("current")
_Es2226IgmpVlanGroupAllow_ObjectIdentity = ObjectIdentity
es2226IgmpVlanGroupAllow = _Es2226IgmpVlanGroupAllow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3)
)


class _Es2226IgmpVlanGroupAllowCreatStatus_Type(Integer32):
    """Custom type es2226IgmpVlanGroupAllowCreatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226IgmpVlanGroupAllowCreatStatus_Type.__name__ = "Integer32"
_Es2226IgmpVlanGroupAllowCreatStatus_Object = MibScalar
es2226IgmpVlanGroupAllowCreatStatus = _Es2226IgmpVlanGroupAllowCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 1),
    _Es2226IgmpVlanGroupAllowCreatStatus_Type()
)
es2226IgmpVlanGroupAllowCreatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowCreatStatus.setStatus("current")
_Es2226IgmpVlanGroupAllowTable_Object = MibTable
es2226IgmpVlanGroupAllowTable = _Es2226IgmpVlanGroupAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2)
)
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowTable.setStatus("current")
_Es2226IgmpVlanGroupAllowEntry_Object = MibTableRow
es2226IgmpVlanGroupAllowEntry = _Es2226IgmpVlanGroupAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1)
)
es2226IgmpVlanGroupAllowEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226IgmpVlanGroupAllowIndex"),
)
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowEntry.setStatus("current")


class _Es2226IgmpVlanGroupAllowIndex_Type(Integer32):
    """Custom type es2226IgmpVlanGroupAllowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Es2226IgmpVlanGroupAllowIndex_Type.__name__ = "Integer32"
_Es2226IgmpVlanGroupAllowIndex_Object = MibTableColumn
es2226IgmpVlanGroupAllowIndex = _Es2226IgmpVlanGroupAllowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1, 1),
    _Es2226IgmpVlanGroupAllowIndex_Type()
)
es2226IgmpVlanGroupAllowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowIndex.setStatus("current")
_Es2226IgmpVlanGroupAllowStartAddress_Type = IpAddress
_Es2226IgmpVlanGroupAllowStartAddress_Object = MibTableColumn
es2226IgmpVlanGroupAllowStartAddress = _Es2226IgmpVlanGroupAllowStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1, 2),
    _Es2226IgmpVlanGroupAllowStartAddress_Type()
)
es2226IgmpVlanGroupAllowStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowStartAddress.setStatus("current")
_Es2226IgmpVlanGroupAllowEndAddress_Type = IpAddress
_Es2226IgmpVlanGroupAllowEndAddress_Object = MibTableColumn
es2226IgmpVlanGroupAllowEndAddress = _Es2226IgmpVlanGroupAllowEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1, 3),
    _Es2226IgmpVlanGroupAllowEndAddress_Type()
)
es2226IgmpVlanGroupAllowEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowEndAddress.setStatus("current")


class _Es2226IgmpVlanGroupAllowVid_Type(Integer32):
    """Custom type es2226IgmpVlanGroupAllowVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226IgmpVlanGroupAllowVid_Type.__name__ = "Integer32"
_Es2226IgmpVlanGroupAllowVid_Object = MibTableColumn
es2226IgmpVlanGroupAllowVid = _Es2226IgmpVlanGroupAllowVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1, 4),
    _Es2226IgmpVlanGroupAllowVid_Type()
)
es2226IgmpVlanGroupAllowVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowVid.setStatus("current")
_Es2226IgmpVlanGroupAllowPortMember_Type = DisplayString
_Es2226IgmpVlanGroupAllowPortMember_Object = MibTableColumn
es2226IgmpVlanGroupAllowPortMember = _Es2226IgmpVlanGroupAllowPortMember_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1, 5),
    _Es2226IgmpVlanGroupAllowPortMember_Type()
)
es2226IgmpVlanGroupAllowPortMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowPortMember.setStatus("current")


class _Es2226IgmpVlanGroupAllowRowStatus_Type(Integer32):
    """Custom type es2226IgmpVlanGroupAllowRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2226IgmpVlanGroupAllowRowStatus_Type.__name__ = "Integer32"
_Es2226IgmpVlanGroupAllowRowStatus_Object = MibTableColumn
es2226IgmpVlanGroupAllowRowStatus = _Es2226IgmpVlanGroupAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 3, 2, 1, 6),
    _Es2226IgmpVlanGroupAllowRowStatus_Type()
)
es2226IgmpVlanGroupAllowRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226IgmpVlanGroupAllowRowStatus.setStatus("current")
_Es2226MvrSetting_ObjectIdentity = ObjectIdentity
es2226MvrSetting = _Es2226MvrSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4)
)


class _Es2226MvrSettingMulticastVlanRegistration_Type(Integer32):
    """Custom type es2226MvrSettingMulticastVlanRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226MvrSettingMulticastVlanRegistration_Type.__name__ = "Integer32"
_Es2226MvrSettingMulticastVlanRegistration_Object = MibScalar
es2226MvrSettingMulticastVlanRegistration = _Es2226MvrSettingMulticastVlanRegistration_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 1),
    _Es2226MvrSettingMulticastVlanRegistration_Type()
)
es2226MvrSettingMulticastVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MvrSettingMulticastVlanRegistration.setStatus("current")


class _Es2226MvrSettingMulticastVlanIdConf_Type(Integer32):
    """Custom type es2226MvrSettingMulticastVlanIdConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_Es2226MvrSettingMulticastVlanIdConf_Type.__name__ = "Integer32"
_Es2226MvrSettingMulticastVlanIdConf_Object = MibScalar
es2226MvrSettingMulticastVlanIdConf = _Es2226MvrSettingMulticastVlanIdConf_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 2),
    _Es2226MvrSettingMulticastVlanIdConf_Type()
)
es2226MvrSettingMulticastVlanIdConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MvrSettingMulticastVlanIdConf.setStatus("current")


class _Es2226MvrSettingMulticastVlanIdShow_Type(Integer32):
    """Custom type es2226MvrSettingMulticastVlanIdShow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2226MvrSettingMulticastVlanIdShow_Type.__name__ = "Integer32"
_Es2226MvrSettingMulticastVlanIdShow_Object = MibScalar
es2226MvrSettingMulticastVlanIdShow = _Es2226MvrSettingMulticastVlanIdShow_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 3),
    _Es2226MvrSettingMulticastVlanIdShow_Type()
)
es2226MvrSettingMulticastVlanIdShow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MvrSettingMulticastVlanIdShow.setStatus("current")
_Es2226MvrSettingTable_Object = MibTable
es2226MvrSettingTable = _Es2226MvrSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 4)
)
if mibBuilder.loadTexts:
    es2226MvrSettingTable.setStatus("current")
_Es2226MvrSettingEntry_Object = MibTableRow
es2226MvrSettingEntry = _Es2226MvrSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 4, 1)
)
es2226MvrSettingEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226MvrSettingPort"),
)
if mibBuilder.loadTexts:
    es2226MvrSettingEntry.setStatus("current")


class _Es2226MvrSettingPort_Type(Integer32):
    """Custom type es2226MvrSettingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2226MvrSettingPort_Type.__name__ = "Integer32"
_Es2226MvrSettingPort_Object = MibTableColumn
es2226MvrSettingPort = _Es2226MvrSettingPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 4, 1, 1),
    _Es2226MvrSettingPort_Type()
)
es2226MvrSettingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226MvrSettingPort.setStatus("current")


class _Es2226MvrSettingServerType_Type(Integer32):
    """Custom type es2226MvrSettingServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2226MvrSettingServerType_Type.__name__ = "Integer32"
_Es2226MvrSettingServerType_Object = MibTableColumn
es2226MvrSettingServerType = _Es2226MvrSettingServerType_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 4, 1, 2),
    _Es2226MvrSettingServerType_Type()
)
es2226MvrSettingServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MvrSettingServerType.setStatus("current")


class _Es2226MvrSettingTagging_Type(Integer32):
    """Custom type es2226MvrSettingTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2226MvrSettingTagging_Type.__name__ = "Integer32"
_Es2226MvrSettingTagging_Object = MibTableColumn
es2226MvrSettingTagging = _Es2226MvrSettingTagging_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 4, 4, 1, 3),
    _Es2226MvrSettingTagging_Type()
)
es2226MvrSettingTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226MvrSettingTagging.setStatus("current")
_Es2226MulticastStatus_ObjectIdentity = ObjectIdentity
es2226MulticastStatus = _Es2226MulticastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5)
)
_Es2226MulticastStatusTable_Object = MibTable
es2226MulticastStatusTable = _Es2226MulticastStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5, 1)
)
if mibBuilder.loadTexts:
    es2226MulticastStatusTable.setStatus("current")
_Es2226MulticastStatusEntry_Object = MibTableRow
es2226MulticastStatusEntry = _Es2226MulticastStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5, 1, 1)
)
es2226MulticastStatusEntry.setIndexNames(
    (0, "RUBYTECH-ES2226-MIB", "es2226MulticastStatusIndex"),
)
if mibBuilder.loadTexts:
    es2226MulticastStatusEntry.setStatus("current")


class _Es2226MulticastStatusIndex_Type(Integer32):
    """Custom type es2226MulticastStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Es2226MulticastStatusIndex_Type.__name__ = "Integer32"
_Es2226MulticastStatusIndex_Object = MibTableColumn
es2226MulticastStatusIndex = _Es2226MulticastStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5, 1, 1, 1),
    _Es2226MulticastStatusIndex_Type()
)
es2226MulticastStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2226MulticastStatusIndex.setStatus("current")


class _Es2226MulticastStatusVid_Type(Integer32):
    """Custom type es2226MulticastStatusVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2226MulticastStatusVid_Type.__name__ = "Integer32"
_Es2226MulticastStatusVid_Object = MibTableColumn
es2226MulticastStatusVid = _Es2226MulticastStatusVid_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5, 1, 1, 2),
    _Es2226MulticastStatusVid_Type()
)
es2226MulticastStatusVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MulticastStatusVid.setStatus("current")
_Es2226MulticastStatusMulticastGroup_Type = IpAddress
_Es2226MulticastStatusMulticastGroup_Object = MibTableColumn
es2226MulticastStatusMulticastGroup = _Es2226MulticastStatusMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5, 1, 1, 3),
    _Es2226MulticastStatusMulticastGroup_Type()
)
es2226MulticastStatusMulticastGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MulticastStatusMulticastGroup.setStatus("current")
_Es2226MulticastStatusPortMember_Type = DisplayString
_Es2226MulticastStatusPortMember_Object = MibTableColumn
es2226MulticastStatusPortMember = _Es2226MulticastStatusPortMember_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 5, 1, 1, 4),
    _Es2226MulticastStatusPortMember_Type()
)
es2226MulticastStatusPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2226MulticastStatusPortMember.setStatus("current")
_Es2226RadiusIgmpSetting_ObjectIdentity = ObjectIdentity
es2226RadiusIgmpSetting = _Es2226RadiusIgmpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6)
)
_Es2226RadiusIgmpServer1_Type = IpAddress
_Es2226RadiusIgmpServer1_Object = MibScalar
es2226RadiusIgmpServer1 = _Es2226RadiusIgmpServer1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 1),
    _Es2226RadiusIgmpServer1_Type()
)
es2226RadiusIgmpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpServer1.setStatus("current")


class _Es2226RadiusIgmpPortNumber1_Type(Integer32):
    """Custom type es2226RadiusIgmpPortNumber1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226RadiusIgmpPortNumber1_Type.__name__ = "Integer32"
_Es2226RadiusIgmpPortNumber1_Object = MibScalar
es2226RadiusIgmpPortNumber1 = _Es2226RadiusIgmpPortNumber1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 2),
    _Es2226RadiusIgmpPortNumber1_Type()
)
es2226RadiusIgmpPortNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpPortNumber1.setStatus("current")
_Es2226RadiusIgmpServer2_Type = IpAddress
_Es2226RadiusIgmpServer2_Object = MibScalar
es2226RadiusIgmpServer2 = _Es2226RadiusIgmpServer2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 3),
    _Es2226RadiusIgmpServer2_Type()
)
es2226RadiusIgmpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpServer2.setStatus("current")


class _Es2226RadiusIgmpPortNumber2_Type(Integer32):
    """Custom type es2226RadiusIgmpPortNumber2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226RadiusIgmpPortNumber2_Type.__name__ = "Integer32"
_Es2226RadiusIgmpPortNumber2_Object = MibScalar
es2226RadiusIgmpPortNumber2 = _Es2226RadiusIgmpPortNumber2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 4),
    _Es2226RadiusIgmpPortNumber2_Type()
)
es2226RadiusIgmpPortNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpPortNumber2.setStatus("current")
_Es2226RadiusIgmpSecretKey1_Type = DisplayString
_Es2226RadiusIgmpSecretKey1_Object = MibScalar
es2226RadiusIgmpSecretKey1 = _Es2226RadiusIgmpSecretKey1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 5),
    _Es2226RadiusIgmpSecretKey1_Type()
)
es2226RadiusIgmpSecretKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpSecretKey1.setStatus("current")
_Es2226RadiusIgmpAccountingServer1_Type = IpAddress
_Es2226RadiusIgmpAccountingServer1_Object = MibScalar
es2226RadiusIgmpAccountingServer1 = _Es2226RadiusIgmpAccountingServer1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 6),
    _Es2226RadiusIgmpAccountingServer1_Type()
)
es2226RadiusIgmpAccountingServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpAccountingServer1.setStatus("current")


class _Es2226RadiusIgmpAccountingPortNumber1_Type(Integer32):
    """Custom type es2226RadiusIgmpAccountingPortNumber1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226RadiusIgmpAccountingPortNumber1_Type.__name__ = "Integer32"
_Es2226RadiusIgmpAccountingPortNumber1_Object = MibScalar
es2226RadiusIgmpAccountingPortNumber1 = _Es2226RadiusIgmpAccountingPortNumber1_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 7),
    _Es2226RadiusIgmpAccountingPortNumber1_Type()
)
es2226RadiusIgmpAccountingPortNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpAccountingPortNumber1.setStatus("current")
_Es2226RadiusIgmpAccountingServer2_Type = IpAddress
_Es2226RadiusIgmpAccountingServer2_Object = MibScalar
es2226RadiusIgmpAccountingServer2 = _Es2226RadiusIgmpAccountingServer2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 8),
    _Es2226RadiusIgmpAccountingServer2_Type()
)
es2226RadiusIgmpAccountingServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpAccountingServer2.setStatus("current")


class _Es2226RadiusIgmpAccountingPortNumber2_Type(Integer32):
    """Custom type es2226RadiusIgmpAccountingPortNumber2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2226RadiusIgmpAccountingPortNumber2_Type.__name__ = "Integer32"
_Es2226RadiusIgmpAccountingPortNumber2_Object = MibScalar
es2226RadiusIgmpAccountingPortNumber2 = _Es2226RadiusIgmpAccountingPortNumber2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 9),
    _Es2226RadiusIgmpAccountingPortNumber2_Type()
)
es2226RadiusIgmpAccountingPortNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpAccountingPortNumber2.setStatus("current")
_Es2226RadiusIgmpSecretKey2_Type = DisplayString
_Es2226RadiusIgmpSecretKey2_Object = MibScalar
es2226RadiusIgmpSecretKey2 = _Es2226RadiusIgmpSecretKey2_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 10),
    _Es2226RadiusIgmpSecretKey2_Type()
)
es2226RadiusIgmpSecretKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpSecretKey2.setStatus("current")


class _Es2226RadiusIgmpResponseTimeout_Type(Integer32):
    """Custom type es2226RadiusIgmpResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_Es2226RadiusIgmpResponseTimeout_Type.__name__ = "Integer32"
_Es2226RadiusIgmpResponseTimeout_Object = MibScalar
es2226RadiusIgmpResponseTimeout = _Es2226RadiusIgmpResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 11),
    _Es2226RadiusIgmpResponseTimeout_Type()
)
es2226RadiusIgmpResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpResponseTimeout.setStatus("current")


class _Es2226RadiusIgmpNumberOfRetry_Type(Integer32):
    """Custom type es2226RadiusIgmpNumberOfRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2226RadiusIgmpNumberOfRetry_Type.__name__ = "Integer32"
_Es2226RadiusIgmpNumberOfRetry_Object = MibScalar
es2226RadiusIgmpNumberOfRetry = _Es2226RadiusIgmpNumberOfRetry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 12),
    _Es2226RadiusIgmpNumberOfRetry_Type()
)
es2226RadiusIgmpNumberOfRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpNumberOfRetry.setStatus("current")
_Es2226RadiusIgmpPortMember_Type = DisplayString
_Es2226RadiusIgmpPortMember_Object = MibScalar
es2226RadiusIgmpPortMember = _Es2226RadiusIgmpPortMember_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 26, 6, 13),
    _Es2226RadiusIgmpPortMember_Type()
)
es2226RadiusIgmpPortMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2226RadiusIgmpPortMember.setStatus("current")

# Managed Objects groups


# Notification objects

es2226ModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 1)
)
es2226ModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2226ModuleInserted.setStatus(
        "current"
    )

es2226ModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 2)
)
es2226ModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2226ModuleRemoved.setStatus(
        "current"
    )

es2226DualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 3)
)
es2226DualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2226DualMediaSwapped.setStatus(
        "current"
    )

es2226LoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 4)
)
es2226LoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2226LoopDetected.setStatus(
        "current"
    )

es2226IpMacBindOffered = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 5)
)
es2226IpMacBindOffered.setObjects(
    ("RUBYTECH-ES2226-MIB", "ipmacbind")
)
if mibBuilder.loadTexts:
    es2226IpMacBindOffered.setStatus(
        "current"
    )

es2226IpMacBindReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 6)
)
es2226IpMacBindReleased.setObjects(
    ("RUBYTECH-ES2226-MIB", "ipmacbind")
)
if mibBuilder.loadTexts:
    es2226IpMacBindReleased.setStatus(
        "current"
    )

es2226ARPInspectionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 7)
)
es2226ARPInspectionDetected.setObjects(
    ("RUBYTECH-ES2226-MIB", "arpinspect")
)
if mibBuilder.loadTexts:
    es2226ARPInspectionDetected.setStatus(
        "current"
    )

es2226StpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 100)
)
if mibBuilder.loadTexts:
    es2226StpStateDisabled.setStatus(
        "current"
    )

es2226StpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 101)
)
if mibBuilder.loadTexts:
    es2226StpStateEnabled.setStatus(
        "current"
    )

es2226StpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 102)
)
es2226StpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2226StpTopologyChanged.setStatus(
        "current"
    )

es2226RmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 110)
)
if mibBuilder.loadTexts:
    es2226RmonRisingAlarm.setStatus(
        "current"
    )

es2226RmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 111)
)
if mibBuilder.loadTexts:
    es2226RmonFallingAlarm.setStatus(
        "current"
    )

es2226LacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 120)
)
es2226LacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-ES2226-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2226LacpStateDisabled.setStatus(
        "current"
    )

es2226LacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 121)
)
es2226LacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-ES2226-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2226LacpStateEnabled.setStatus(
        "current"
    )

es2226LacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 123)
)
es2226LacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-ES2226-MIB", "actorkey"),
        ("RUBYTECH-ES2226-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2226LacpPortAdded.setStatus(
        "current"
    )

es2226LacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 124)
)
es2226LacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-ES2226-MIB", "actorkey"),
        ("RUBYTECH-ES2226-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2226LacpPortTrunkFailure.setStatus(
        "current"
    )

es2226GvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 140)
)
if mibBuilder.loadTexts:
    es2226GvrpStateDisabled.setStatus(
        "current"
    )

es2226GvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 141)
)
if mibBuilder.loadTexts:
    es2226GvrpStateEnabled.setStatus(
        "current"
    )

es2226VlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 151)
)
if mibBuilder.loadTexts:
    es2226VlanPortBaseEnabled.setStatus(
        "current"
    )

es2226VlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 152)
)
if mibBuilder.loadTexts:
    es2226VlanTagBaseEnabled.setStatus(
        "current"
    )

es2226VlanMetroBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 153)
)
if mibBuilder.loadTexts:
    es2226VlanMetroBaseEnabled.setStatus(
        "current"
    )

es2226UserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 200)
)
es2226UserLogin.setObjects(
    ("RUBYTECH-ES2226-MIB", "username")
)
if mibBuilder.loadTexts:
    es2226UserLogin.setStatus(
        "current"
    )

es2226UserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 31, 1, 20, 201)
)
es2226UserLogout.setObjects(
    ("RUBYTECH-ES2226-MIB", "username")
)
if mibBuilder.loadTexts:
    es2226UserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUBYTECH-ES2226-MIB",
    **{"rubytech": rubytech,
       "switch": switch,
       "es2226ProductID": es2226ProductID,
       "es2226Produces": es2226Produces,
       "es2226System": es2226System,
       "es2226CommonSys": es2226CommonSys,
       "es2226Reboot": es2226Reboot,
       "es2226BiosVsersion": es2226BiosVsersion,
       "es2226FirmwareVersion": es2226FirmwareVersion,
       "es2226HardwareVersion": es2226HardwareVersion,
       "es2226MechanicalVersion": es2226MechanicalVersion,
       "es2226SerialNumber": es2226SerialNumber,
       "es2226HostMacAddress": es2226HostMacAddress,
       "es2226DevicePort": es2226DevicePort,
       "es2226RamSize": es2226RamSize,
       "es2226FlashSize": es2226FlashSize,
       "es2226CPULoad": es2226CPULoad,
       "es2226IP": es2226IP,
       "es2226DhcpSetting": es2226DhcpSetting,
       "es2226IPAddress": es2226IPAddress,
       "es2226NetMask": es2226NetMask,
       "es2226DefaultGateway": es2226DefaultGateway,
       "es2226DnsSetting": es2226DnsSetting,
       "es2226DnsServer": es2226DnsServer,
       "es2226Time": es2226Time,
       "es2226SystemCurrentTime": es2226SystemCurrentTime,
       "es2226ManualTimeSetting": es2226ManualTimeSetting,
       "es2226NTPServer": es2226NTPServer,
       "es2226NTPTimeZone": es2226NTPTimeZone,
       "es2226NTPTimeSync": es2226NTPTimeSync,
       "es2226DaylightSavingTime": es2226DaylightSavingTime,
       "es2226DaylightStartTime": es2226DaylightStartTime,
       "es2226DaylightEndTime": es2226DaylightEndTime,
       "es2226Account": es2226Account,
       "es2226AccountNumber": es2226AccountNumber,
       "es2226AccountTable": es2226AccountTable,
       "es2226AccountEntry": es2226AccountEntry,
       "es2226AccountIndex": es2226AccountIndex,
       "es2226AccountAuthorization": es2226AccountAuthorization,
       "es2226AccountName": es2226AccountName,
       "es2226AccountPassword": es2226AccountPassword,
       "es2226AccountAddName": es2226AccountAddName,
       "es2226AccountAddPassword": es2226AccountAddPassword,
       "es2226DoAccountAdd": es2226DoAccountAdd,
       "es2226AccountDel": es2226AccountDel,
       "es2226TrapHost": es2226TrapHost,
       "es2226TrapBootDelayTime": es2226TrapBootDelayTime,
       "es2226TrapHostTable": es2226TrapHostTable,
       "es2226TrapHostEntry": es2226TrapHostEntry,
       "es2226TrapHostIndex": es2226TrapHostIndex,
       "es2226TrapHostVersion": es2226TrapHostVersion,
       "es2226TrapHostIP": es2226TrapHostIP,
       "es2226TrapHostPort": es2226TrapHostPort,
       "es2226TrapHostCommunity": es2226TrapHostCommunity,
       "es2226TrapHostSecurity": es2226TrapHostSecurity,
       "es2226TrapHostAuthPtc": es2226TrapHostAuthPtc,
       "es2226TrapHostAuthPassword": es2226TrapHostAuthPassword,
       "es2226TrapHostPrivPtc": es2226TrapHostPrivPtc,
       "es2226TrapHostPrivPassword": es2226TrapHostPrivPassword,
       "es2226TrapHostCurrentMode": es2226TrapHostCurrentMode,
       "es2226Alarm": es2226Alarm,
       "es2226Event": es2226Event,
       "es2226EventNumber": es2226EventNumber,
       "es2226EventTable": es2226EventTable,
       "es2226EventEntry": es2226EventEntry,
       "es2226EventIndex": es2226EventIndex,
       "es2226EventName": es2226EventName,
       "es2226EventSendEmail": es2226EventSendEmail,
       "es2226EventSendTrap": es2226EventSendTrap,
       "es2226Email": es2226Email,
       "es2226EmailServer": es2226EmailServer,
       "es2226EmailUsername": es2226EmailUsername,
       "es2226EmailPassword": es2226EmailPassword,
       "es2226EmailSender": es2226EmailSender,
       "es2226EmailReturnPath": es2226EmailReturnPath,
       "es2226EmailUserNumber": es2226EmailUserNumber,
       "es2226EmailUserTable": es2226EmailUserTable,
       "es2226EmailUserEntry": es2226EmailUserEntry,
       "es2226EmailUserIndex": es2226EmailUserIndex,
       "es2226EmailUserAddress": es2226EmailUserAddress,
       "es2226Tftp": es2226Tftp,
       "es2226TftpServer": es2226TftpServer,
       "es2226Configuration": es2226Configuration,
       "es2226SaveRestore": es2226SaveRestore,
       "es2226SaveStart": es2226SaveStart,
       "es2226SaveUser": es2226SaveUser,
       "es2226RestoreDefault": es2226RestoreDefault,
       "es2226RestoreUser": es2226RestoreUser,
       "es2226ConfigFile": es2226ConfigFile,
       "es2226ExportConfigName": es2226ExportConfigName,
       "es2226DoExportConfig": es2226DoExportConfig,
       "es2226ImportConfigName": es2226ImportConfigName,
       "es2226DoImportConfig": es2226DoImportConfig,
       "es2226Diagnostic": es2226Diagnostic,
       "es2226EEPROMTest": es2226EEPROMTest,
       "es2226UartTest": es2226UartTest,
       "es2226DramTest": es2226DramTest,
       "es2226FlashTest": es2226FlashTest,
       "es2226InternalLoopbackTest": es2226InternalLoopbackTest,
       "es2226ExternalLoopbackTest": es2226ExternalLoopbackTest,
       "es2226PingTest": es2226PingTest,
       "es2226Log": es2226Log,
       "es2226ClearLog": es2226ClearLog,
       "es2226UploadLog": es2226UploadLog,
       "es2226AutoUploadLogState": es2226AutoUploadLogState,
       "es2226LogNumber": es2226LogNumber,
       "es2226LogTable": es2226LogTable,
       "es2226LogEntry": es2226LogEntry,
       "es2226LogIndex": es2226LogIndex,
       "es2226LogEvent": es2226LogEvent,
       "es2226Firmware": es2226Firmware,
       "es2226FirmwareFileName": es2226FirmwareFileName,
       "es2226DoFirmwareUpgrade": es2226DoFirmwareUpgrade,
       "es2226Port": es2226Port,
       "es2226PortStatus": es2226PortStatus,
       "es2226PortStatusNumber": es2226PortStatusNumber,
       "es2226PortStatusTable": es2226PortStatusTable,
       "es2226PortStatusEntry": es2226PortStatusEntry,
       "es2226PortStatusIndex": es2226PortStatusIndex,
       "es2226PortStatusMedia": es2226PortStatusMedia,
       "es2226PortStatusLink": es2226PortStatusLink,
       "es2226PortStatusPortState": es2226PortStatusPortState,
       "es2226PortStatusAutoNego": es2226PortStatusAutoNego,
       "es2226PortStatusSpdDpx": es2226PortStatusSpdDpx,
       "es2226PortStatusRxPause": es2226PortStatusRxPause,
       "es2226PortStatusTxPause": es2226PortStatusTxPause,
       "es2226PortStatusDescription": es2226PortStatusDescription,
       "es2226PortConf": es2226PortConf,
       "es2226PortConfNumber": es2226PortConfNumber,
       "es2226PortConfTable": es2226PortConfTable,
       "es2226PortConfEntry": es2226PortConfEntry,
       "es2226PortConfIndex": es2226PortConfIndex,
       "es2226PortConfPortState": es2226PortConfPortState,
       "es2226PortConfSpdDpx": es2226PortConfSpdDpx,
       "es2226PortConfFlwCtrl": es2226PortConfFlwCtrl,
       "es2226PortConfPowerSaving": es2226PortConfPowerSaving,
       "es2226PortConfDescription": es2226PortConfDescription,
       "es2226PortBandwidth": es2226PortBandwidth,
       "es2226PortBandwidthNumber": es2226PortBandwidthNumber,
       "es2226PortBandwidthTable": es2226PortBandwidthTable,
       "es2226PortBandwidthEntry": es2226PortBandwidthEntry,
       "es2226PortBandwidthIndex": es2226PortBandwidthIndex,
       "es2226PortBandwidthIngressRate": es2226PortBandwidthIngressRate,
       "es2226PortBandwidthEgressRate": es2226PortBandwidthEgressRate,
       "es2226PortBandwidthStormType": es2226PortBandwidthStormType,
       "es2226PortBandwidthStormRate": es2226PortBandwidthStormRate,
       "es2226PortSFPInfo": es2226PortSFPInfo,
       "es2226PortSFPInfoNumber": es2226PortSFPInfoNumber,
       "es2226PortSFPInfoTable": es2226PortSFPInfoTable,
       "es2226PortSFPInfoEntry": es2226PortSFPInfoEntry,
       "es2226PortSFPInfoIndex": es2226PortSFPInfoIndex,
       "es2226PortSFPConnectorType": es2226PortSFPConnectorType,
       "es2226PortSFPFiberType": es2226PortSFPFiberType,
       "es2226PortSFPWavelength": es2226PortSFPWavelength,
       "es2226PortSFPBaudRate": es2226PortSFPBaudRate,
       "es2226PortSFPVendorOUI": es2226PortSFPVendorOUI,
       "es2226PortSFPVendorName": es2226PortSFPVendorName,
       "es2226PortSFPVendorPN": es2226PortSFPVendorPN,
       "es2226PortSFPVendorRev": es2226PortSFPVendorRev,
       "es2226PortSFPVendorSN": es2226PortSFPVendorSN,
       "es2226PortSFPDateCode": es2226PortSFPDateCode,
       "es2226PortSFPTemperature": es2226PortSFPTemperature,
       "es2226PortSFPVcc": es2226PortSFPVcc,
       "es2226PortSFPTxBias": es2226PortSFPTxBias,
       "es2226PortSFPTxPWR": es2226PortSFPTxPWR,
       "es2226PortSFPRxPWR": es2226PortSFPRxPWR,
       "es2226LoopDetectedConf": es2226LoopDetectedConf,
       "es2226LoopDetectedNumber": es2226LoopDetectedNumber,
       "es2226LoopDetectedTable": es2226LoopDetectedTable,
       "es2226LoopDetectedEntry": es2226LoopDetectedEntry,
       "es2226LoopDetectedfIndex": es2226LoopDetectedfIndex,
       "es2226LoopDetectedStateEbl": es2226LoopDetectedStateEbl,
       "es2226LoopDetectedCurrentStatus": es2226LoopDetectedCurrentStatus,
       "es2226LoopDetectedResumed": es2226LoopDetectedResumed,
       "es2226LoopDetectedAction": es2226LoopDetectedAction,
       "es2226IpMacBind": es2226IpMacBind,
       "es2226IpMacBindStatus": es2226IpMacBindStatus,
       "es2226IpMacBindMode": es2226IpMacBindMode,
       "es2226IpMacBindPort": es2226IpMacBindPort,
       "es2226IpMacBindCount": es2226IpMacBindCount,
       "es2226IpMacBindCreatStatus": es2226IpMacBindCreatStatus,
       "es2226IpMacBindStatusTable": es2226IpMacBindStatusTable,
       "es2226IpMacBindStatusEntry": es2226IpMacBindStatusEntry,
       "es2226IpMacBindStatusIndex": es2226IpMacBindStatusIndex,
       "es2226IpMacBindStatusName": es2226IpMacBindStatusName,
       "es2226IpMacBindStatusMac": es2226IpMacBindStatusMac,
       "es2226IpMacBindStatusIp": es2226IpMacBindStatusIp,
       "es2226IpMacBindStatusPort": es2226IpMacBindStatusPort,
       "es2226IpMacBindStatusBindingMethod": es2226IpMacBindStatusBindingMethod,
       "es2226IpMacBindStatusType": es2226IpMacBindStatusType,
       "es2226IpMacBindStatusRowStatus": es2226IpMacBindStatusRowStatus,
       "es2226MacTableInfo": es2226MacTableInfo,
       "es2226MacTableMaintenance": es2226MacTableMaintenance,
       "es2226MacTableAgingTime": es2226MacTableAgingTime,
       "es2226MacTableFlush": es2226MacTableFlush,
       "es2226MacTableLearnPortLimitTable": es2226MacTableLearnPortLimitTable,
       "es2226MacTableLearnPortLimitEntry": es2226MacTableLearnPortLimitEntry,
       "es2226MacTableLearnPortLimitIndex": es2226MacTableLearnPortLimitIndex,
       "es2226MacTableLearnPortLimit": es2226MacTableLearnPortLimit,
       "es2226MacTableStaticMac": es2226MacTableStaticMac,
       "es2226MacTableStaticMacCreatStatus": es2226MacTableStaticMacCreatStatus,
       "es2226MacTableStaticMacNumber": es2226MacTableStaticMacNumber,
       "es2226MacTableStaticMacTable": es2226MacTableStaticMacTable,
       "es2226MacTableStaticMacEntry": es2226MacTableStaticMacEntry,
       "es2226MacTableStaticMacIndex": es2226MacTableStaticMacIndex,
       "es2226MacTableStaticMacAddress": es2226MacTableStaticMacAddress,
       "es2226MacTableStaticMacVid": es2226MacTableStaticMacVid,
       "es2226MacTableStaticMacRule": es2226MacTableStaticMacRule,
       "es2226MacTableStaticMacPort": es2226MacTableStaticMacPort,
       "es2226MacTableStaticMacRowStatus": es2226MacTableStaticMacRowStatus,
       "es2226MacTableMacAlias": es2226MacTableMacAlias,
       "es2226MacTableMacAliasCreatStatus": es2226MacTableMacAliasCreatStatus,
       "es2226MacTableMacAliasNumber": es2226MacTableMacAliasNumber,
       "es2226MacTableMacAliasTable": es2226MacTableMacAliasTable,
       "es2226MacTableMacAliasEntry": es2226MacTableMacAliasEntry,
       "es2226MacTableMacAliasIndex": es2226MacTableMacAliasIndex,
       "es2226MacTableMacAliasAddress": es2226MacTableMacAliasAddress,
       "es2226MacTableMacAliasAlias": es2226MacTableMacAliasAlias,
       "es2226MacTableMacAliasRowStatus": es2226MacTableMacAliasRowStatus,
       "es2226Security": es2226Security,
       "es2226Mirror": es2226Mirror,
       "es2226MirrorMode": es2226MirrorMode,
       "es2226MonitoringPort": es2226MonitoringPort,
       "es2226MonitoredIngressPort": es2226MonitoredIngressPort,
       "es2226MonitoredEgressPort": es2226MonitoredEgressPort,
       "es2226IsolatedGroup": es2226IsolatedGroup,
       "es2226IsolatedPortGroup": es2226IsolatedPortGroup,
       "es2226ArpProtect": es2226ArpProtect,
       "es2226ArpProtectPackerBurst": es2226ArpProtectPackerBurst,
       "es2226ArpProtectRatePerSec": es2226ArpProtectRatePerSec,
       "es2226VirtualStack": es2226VirtualStack,
       "es2226VirtualStackState": es2226VirtualStackState,
       "es2226VirtualStackRole": es2226VirtualStackRole,
       "es2226VirtualStackGroupID": es2226VirtualStackGroupID,
       "es2226ManagementSecurity": es2226ManagementSecurity,
       "es2226ManagementSecurityNumber": es2226ManagementSecurityNumber,
       "es2226ManagementSecurityEntryCreate": es2226ManagementSecurityEntryCreate,
       "es2226ManagementSecurityTable": es2226ManagementSecurityTable,
       "es2226ManagementSecurityEntry": es2226ManagementSecurityEntry,
       "es2226ManagementSecurityIndex": es2226ManagementSecurityIndex,
       "es2226ManagementSecurityName": es2226ManagementSecurityName,
       "es2226ManagementSecurityVid": es2226ManagementSecurityVid,
       "es2226ManagementSecurityIpRange": es2226ManagementSecurityIpRange,
       "es2226ManagementSecurityIncomigPort": es2226ManagementSecurityIncomigPort,
       "es2226ManagementSecurityAccessType": es2226ManagementSecurityAccessType,
       "es2226ManagementSecurityAction": es2226ManagementSecurityAction,
       "es2226ManagementSecurityRowStatus": es2226ManagementSecurityRowStatus,
       "es2226QoS": es2226QoS,
       "es2226QoSGlobalConfig": es2226QoSGlobalConfig,
       "es2226QoSMode": es2226QoSMode,
       "es2226QoS1PEnable": es2226QoS1PEnable,
       "es2226QoSDSCPEnable": es2226QoSDSCPEnable,
       "es2226QoSSchedulingMethod": es2226QoSSchedulingMethod,
       "es2226QoSWeightQ0": es2226QoSWeightQ0,
       "es2226QoSWeightQ1": es2226QoSWeightQ1,
       "es2226QoSWeightQ2": es2226QoSWeightQ2,
       "es2226QoSWeightQ3": es2226QoSWeightQ3,
       "es2226QoS1PPriority": es2226QoS1PPriority,
       "es2226QoS1PPriorityTable": es2226QoS1PPriorityTable,
       "es2226QoS1PPriorityEntry": es2226QoS1PPriorityEntry,
       "es2226QoS1PPriorityIndex": es2226QoS1PPriorityIndex,
       "es2226QoS1PPriorityValue": es2226QoS1PPriorityValue,
       "es2226QoS1PPriorityQueue": es2226QoS1PPriorityQueue,
       "es2226QoSDSCPPriority": es2226QoSDSCPPriority,
       "es2226QoSDSCPPriorityTable": es2226QoSDSCPPriorityTable,
       "es2226QoSDSCPPriorityEntry": es2226QoSDSCPPriorityEntry,
       "es2226QoSDSCPPriorityIndex": es2226QoSDSCPPriorityIndex,
       "es2226QoSDSCPPriorityValue": es2226QoSDSCPPriorityValue,
       "es2226QoSDSCPPriorityQueue": es2226QoSDSCPPriorityQueue,
       "es2226Vlan": es2226Vlan,
       "es2226VlanModeConfig": es2226VlanModeConfig,
       "es2226VlanMode": es2226VlanMode,
       "es2226SymmetricVlan": es2226SymmetricVlan,
       "es2226VlanSVL": es2226VlanSVL,
       "es2226DoubleTag": es2226DoubleTag,
       "es2226SpPortMember": es2226SpPortMember,
       "es2226UpLinkPort": es2226UpLinkPort,
       "es2226VlanPvid": es2226VlanPvid,
       "es2226VlanPvidTable": es2226VlanPvidTable,
       "es2226VlanPvidEntry": es2226VlanPvidEntry,
       "es2226VlanPvidPort": es2226VlanPvidPort,
       "es2226VlanPvidValue": es2226VlanPvidValue,
       "es2226VlanPvidDefaultPriority": es2226VlanPvidDefaultPriority,
       "es2226VlanPvidDropUntag": es2226VlanPvidDropUntag,
       "es2226PortBasedVlanGroup": es2226PortBasedVlanGroup,
       "es2226PortBasedVlanNumbers": es2226PortBasedVlanNumbers,
       "es2226PortBasedCreateStatus": es2226PortBasedCreateStatus,
       "es2226PortBasedVlanTable": es2226PortBasedVlanTable,
       "es2226PortBasedVlanEntry": es2226PortBasedVlanEntry,
       "es2226PortBasedVlanIndex": es2226PortBasedVlanIndex,
       "es2226PortBasedVlanName": es2226PortBasedVlanName,
       "es2226PortBasedVlanMember": es2226PortBasedVlanMember,
       "es2226PortBasedVlanRowStatus": es2226PortBasedVlanRowStatus,
       "es2226ManagementVlan": es2226ManagementVlan,
       "es2226ManagementVlanState": es2226ManagementVlanState,
       "es2226ManagementVlanVid": es2226ManagementVlanVid,
       "es2226DhcpSnooping": es2226DhcpSnooping,
       "es2226DhcpSnoopingConf": es2226DhcpSnoopingConf,
       "es2226DhcpSnoopingState": es2226DhcpSnoopingState,
       "es2226DhcpSnoopingPortCountSetupTable": es2226DhcpSnoopingPortCountSetupTable,
       "es2226DhcpSnoopingPortCountSetupEntry": es2226DhcpSnoopingPortCountSetupEntry,
       "es2226DhcpSnoopingPortCountSetupPortIndex": es2226DhcpSnoopingPortCountSetupPortIndex,
       "es2226DhcpSnoopingPortCountSetupCount": es2226DhcpSnoopingPortCountSetupCount,
       "es2226DhcpSnoopingTrustGroupConf": es2226DhcpSnoopingTrustGroupConf,
       "es2226DhcpSnoopingTrustGroupNumbers": es2226DhcpSnoopingTrustGroupNumbers,
       "es2226DhcpSnoopingTrustGroupCreatStatus": es2226DhcpSnoopingTrustGroupCreatStatus,
       "es2226DhcpSnoopingTrustGroupTable": es2226DhcpSnoopingTrustGroupTable,
       "es2226DhcpSnoopingTrustGroupEntry": es2226DhcpSnoopingTrustGroupEntry,
       "es2226DhcpSnoopingTrustGroupIndex": es2226DhcpSnoopingTrustGroupIndex,
       "es2226DhcpSnoopingTrustGroupTrustVid": es2226DhcpSnoopingTrustGroupTrustVid,
       "es2226DhcpSnoopingTrustGroupOption82": es2226DhcpSnoopingTrustGroupOption82,
       "es2226DhcpSnoopingTrustGroupAction": es2226DhcpSnoopingTrustGroupAction,
       "es2226DhcpSnoopingTrustGroupServerPort": es2226DhcpSnoopingTrustGroupServerPort,
       "es2226DhcpSnoopingTrustGroupServerVid": es2226DhcpSnoopingTrustGroupServerVid,
       "es2226DhcpSnoopingTrustGroupServerIp": es2226DhcpSnoopingTrustGroupServerIp,
       "es2226DhcpSnoopingTrustGroupRowStatus": es2226DhcpSnoopingTrustGroupRowStatus,
       "es2226DhcpSnoopingDefaultGroupConf": es2226DhcpSnoopingDefaultGroupConf,
       "es2226DhcpSnoopingDefaultGroupServerPort": es2226DhcpSnoopingDefaultGroupServerPort,
       "es2226DhcpSnoopingDefaultGroupServerVid": es2226DhcpSnoopingDefaultGroupServerVid,
       "es2226DhcpSnoopingDefaultGroupOption82": es2226DhcpSnoopingDefaultGroupOption82,
       "es2226DhcpSnoopingDefaultGroupAction": es2226DhcpSnoopingDefaultGroupAction,
       "es2226DhcpSnoopingDefaultGroupServerIp": es2226DhcpSnoopingDefaultGroupServerIp,
       "es2226DhcpSnoopingLeaseList": es2226DhcpSnoopingLeaseList,
       "es2226DhcpSnoopingLeaseListDeleteAll": es2226DhcpSnoopingLeaseListDeleteAll,
       "es2226DhcpSnoopingLeaseListNumbers": es2226DhcpSnoopingLeaseListNumbers,
       "es2226DhcpSnoopingLeaseListTable": es2226DhcpSnoopingLeaseListTable,
       "es2226DhcpSnoopingLeaseListEntry": es2226DhcpSnoopingLeaseListEntry,
       "es2226DhcpSnoopingLeaseListIndex": es2226DhcpSnoopingLeaseListIndex,
       "es2226DhcpSnoopingLeaseListMac": es2226DhcpSnoopingLeaseListMac,
       "es2226DhcpSnoopingLeaseListIp": es2226DhcpSnoopingLeaseListIp,
       "es2226DhcpSnoopingLeaseListPort": es2226DhcpSnoopingLeaseListPort,
       "es2226DhcpSnoopingLeaseListVid": es2226DhcpSnoopingLeaseListVid,
       "es2226DhcpSnoopingLeaseListLease": es2226DhcpSnoopingLeaseListLease,
       "es2226DhcpSnoopingCounter": es2226DhcpSnoopingCounter,
       "es2226DhcpSnoopingCounterReset": es2226DhcpSnoopingCounterReset,
       "es2226DhcpSnoopingCounterTable": es2226DhcpSnoopingCounterTable,
       "es2226DhcpSnoopingCounterEntry": es2226DhcpSnoopingCounterEntry,
       "es2226DhcpSnoopingCounterPortIndex": es2226DhcpSnoopingCounterPortIndex,
       "es2226DhcpSnoopingCounterDiscover": es2226DhcpSnoopingCounterDiscover,
       "es2226DhcpSnoopingCounterOffer": es2226DhcpSnoopingCounterOffer,
       "es2226DhcpSnoopingCounterRequest": es2226DhcpSnoopingCounterRequest,
       "es2226DhcpSnoopingCounterDecline": es2226DhcpSnoopingCounterDecline,
       "es2226DhcpSnoopingCounterAck": es2226DhcpSnoopingCounterAck,
       "es2226DhcpSnoopingCounterNack": es2226DhcpSnoopingCounterNack,
       "es2226DhcpSnoopingCounterRelease": es2226DhcpSnoopingCounterRelease,
       "es2226DhcpSnoopingCounterInform": es2226DhcpSnoopingCounterInform,
       "es2226Dot1X": es2226Dot1X,
       "es2226Dot1XStateSetting": es2226Dot1XStateSetting,
       "es2226RadiusServer1": es2226RadiusServer1,
       "es2226Dot1XPort1": es2226Dot1XPort1,
       "es2226RadiusServer2": es2226RadiusServer2,
       "es2226Dot1XPort2": es2226Dot1XPort2,
       "es2226SecretKey1": es2226SecretKey1,
       "es2226AccountingService": es2226AccountingService,
       "es2226AccountingServer1": es2226AccountingServer1,
       "es2226AccountingPort1": es2226AccountingPort1,
       "es2226AccountingServer2": es2226AccountingServer2,
       "es2226AccountingPort2": es2226AccountingPort2,
       "es2226SecretKey2": es2226SecretKey2,
       "es2226Dot1XPortSecurityManagement": es2226Dot1XPortSecurityManagement,
       "es2226Dot1XPortSecurityTable": es2226Dot1XPortSecurityTable,
       "es2226Dot1XPortSecurityEntry": es2226Dot1XPortSecurityEntry,
       "es2226Dot1XPortSecurityPortIndex": es2226Dot1XPortSecurityPortIndex,
       "es2226Dot1XPortSecurityMode": es2226Dot1XPortSecurityMode,
       "es2226Dot1XPortSecurityPortControl": es2226Dot1XPortSecurityPortControl,
       "es2226Dot1XPortSecurityReAuthMax": es2226Dot1XPortSecurityReAuthMax,
       "es2226Dot1XPortSecurityTxPeriod": es2226Dot1XPortSecurityTxPeriod,
       "es2226Dot1XPortSecurityQuietPeriod": es2226Dot1XPortSecurityQuietPeriod,
       "es2226Dot1XPortSecurityReAuthEnabled": es2226Dot1XPortSecurityReAuthEnabled,
       "es2226Dot1XPortSecurityReAuthPeriod": es2226Dot1XPortSecurityReAuthPeriod,
       "es2226Dot1XPortSecurityMaxRequest": es2226Dot1XPortSecurityMaxRequest,
       "es2226Dot1XPortSecuritySuppTimeout": es2226Dot1XPortSecuritySuppTimeout,
       "es2226Dot1XPortSecurityServerTimeout": es2226Dot1XPortSecurityServerTimeout,
       "es2226Dot1XPortSecurityStatus": es2226Dot1XPortSecurityStatus,
       "es2226TrapEntry": es2226TrapEntry,
       "es2226ModuleInserted": es2226ModuleInserted,
       "es2226ModuleRemoved": es2226ModuleRemoved,
       "es2226DualMediaSwapped": es2226DualMediaSwapped,
       "es2226LoopDetected": es2226LoopDetected,
       "es2226IpMacBindOffered": es2226IpMacBindOffered,
       "es2226IpMacBindReleased": es2226IpMacBindReleased,
       "es2226ARPInspectionDetected": es2226ARPInspectionDetected,
       "es2226StpStateDisabled": es2226StpStateDisabled,
       "es2226StpStateEnabled": es2226StpStateEnabled,
       "es2226StpTopologyChanged": es2226StpTopologyChanged,
       "es2226RmonRisingAlarm": es2226RmonRisingAlarm,
       "es2226RmonFallingAlarm": es2226RmonFallingAlarm,
       "es2226LacpStateDisabled": es2226LacpStateDisabled,
       "es2226LacpStateEnabled": es2226LacpStateEnabled,
       "es2226LacpPortAdded": es2226LacpPortAdded,
       "es2226LacpPortTrunkFailure": es2226LacpPortTrunkFailure,
       "es2226GvrpStateDisabled": es2226GvrpStateDisabled,
       "es2226GvrpStateEnabled": es2226GvrpStateEnabled,
       "es2226VlanPortBaseEnabled": es2226VlanPortBaseEnabled,
       "es2226VlanTagBaseEnabled": es2226VlanTagBaseEnabled,
       "es2226VlanMetroBaseEnabled": es2226VlanMetroBaseEnabled,
       "es2226UserLogin": es2226UserLogin,
       "es2226UserLogout": es2226UserLogout,
       "es2226TrapVariable": es2226TrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink,
       "ipmacbind": ipmacbind,
       "arpinspect": arpinspect,
       "es2226Acl": es2226Acl,
       "es2226HighAcl": es2226HighAcl,
       "es2226HighAclCreatStatus": es2226HighAclCreatStatus,
       "es2226HighAclNumbers": es2226HighAclNumbers,
       "es2226HighAclTable": es2226HighAclTable,
       "es2226HighAclEntry": es2226HighAclEntry,
       "es2226HighAclIndex": es2226HighAclIndex,
       "es2226HighAclName": es2226HighAclName,
       "es2226HighAclIngressPortMap": es2226HighAclIngressPortMap,
       "es2226HighAclSMacFilter": es2226HighAclSMacFilter,
       "es2226HighAclDMacFilter": es2226HighAclDMacFilter,
       "es2226HighAclVlanType": es2226HighAclVlanType,
       "es2226HighAclTagVid": es2226HighAclTagVid,
       "es2226HighAclTagPriority": es2226HighAclTagPriority,
       "es2226HighAclEthernetType": es2226HighAclEthernetType,
       "es2226HighAclIPv4Protocol": es2226HighAclIPv4Protocol,
       "es2226HighAclIPv4ToS": es2226HighAclIPv4ToS,
       "es2226HighAclIPv4TTLRange": es2226HighAclIPv4TTLRange,
       "es2226HighAclIPv4DA": es2226HighAclIPv4DA,
       "es2226HighAclIPv4DAMask": es2226HighAclIPv4DAMask,
       "es2226HighAclIPv4SA": es2226HighAclIPv4SA,
       "es2226HighAclIPv4SAMask": es2226HighAclIPv4SAMask,
       "es2226HighAclL4DestinationPort": es2226HighAclL4DestinationPort,
       "es2226HighAclL4SourcePort": es2226HighAclL4SourcePort,
       "es2226HighAclActionIBForwardDecision": es2226HighAclActionIBForwardDecision,
       "es2226HighAclActionIBForwardMap": es2226HighAclActionIBForwardMap,
       "es2226HighAclActionIBModifyDSCPPacket": es2226HighAclActionIBModifyDSCPPacket,
       "es2226HighAclActionIBModifyDSCPValue": es2226HighAclActionIBModifyDSCPValue,
       "es2226HighAclActionOBForwardDecision": es2226HighAclActionOBForwardDecision,
       "es2226HighAclActionOBForwardMap": es2226HighAclActionOBForwardMap,
       "es2226HighAclActionOBModifyDSCPPacket": es2226HighAclActionOBModifyDSCPPacket,
       "es2226HighAclActionOBModifyDSCPValue": es2226HighAclActionOBModifyDSCPValue,
       "es2226HighAclActionModifyDot1PPacket": es2226HighAclActionModifyDot1PPacket,
       "es2226HighAclActionModifyDot1PValue": es2226HighAclActionModifyDot1PValue,
       "es2226HighAclActionModifyQoSPacket": es2226HighAclActionModifyQoSPacket,
       "es2226HighAclActionModifyQoSValue": es2226HighAclActionModifyQoSValue,
       "es2226HighAclRateMeter": es2226HighAclRateMeter,
       "es2226HighAclRowStatus": es2226HighAclRowStatus,
       "es2226LowAcl": es2226LowAcl,
       "es2226LowAclCreatStatus": es2226LowAclCreatStatus,
       "es2226LowAclNumbers": es2226LowAclNumbers,
       "es2226LowAclTable": es2226LowAclTable,
       "es2226LowAclEntry": es2226LowAclEntry,
       "es2226LowAclIndex": es2226LowAclIndex,
       "es2226LowAclName": es2226LowAclName,
       "es2226LowAclIngressPortMap": es2226LowAclIngressPortMap,
       "es2226LowAclSMacFilter": es2226LowAclSMacFilter,
       "es2226LowAclDMacFilter": es2226LowAclDMacFilter,
       "es2226LowAclVlanType": es2226LowAclVlanType,
       "es2226LowAclTagVid": es2226LowAclTagVid,
       "es2226LowAclTagPriority": es2226LowAclTagPriority,
       "es2226LowAclEthernetType": es2226LowAclEthernetType,
       "es2226LowAclIPv4Protocol": es2226LowAclIPv4Protocol,
       "es2226LowAclIPv4ToS": es2226LowAclIPv4ToS,
       "es2226LowAclIPv4TTLRange": es2226LowAclIPv4TTLRange,
       "es2226LowAclIPv4DA": es2226LowAclIPv4DA,
       "es2226LowAclIPv4DAMask": es2226LowAclIPv4DAMask,
       "es2226LowAclIPv4SA": es2226LowAclIPv4SA,
       "es2226LowAclIPv4SAMask": es2226LowAclIPv4SAMask,
       "es2226LowAclL4DestinationPort": es2226LowAclL4DestinationPort,
       "es2226LowAclL4SourcePort": es2226LowAclL4SourcePort,
       "es2226LowAclActionIBForwardDecision": es2226LowAclActionIBForwardDecision,
       "es2226LowAclActionIBForwardMap": es2226LowAclActionIBForwardMap,
       "es2226LowAclActionIBModifyDSCPPacket": es2226LowAclActionIBModifyDSCPPacket,
       "es2226LowAclActionIBModifyDSCPValue": es2226LowAclActionIBModifyDSCPValue,
       "es2226LowAclActionOBForwardDecision": es2226LowAclActionOBForwardDecision,
       "es2226LowAclActionOBForwardMap": es2226LowAclActionOBForwardMap,
       "es2226LowAclActionOBModifyDSCPPacket": es2226LowAclActionOBModifyDSCPPacket,
       "es2226LowAclActionOBModifyDSCPValue": es2226LowAclActionOBModifyDSCPValue,
       "es2226LowAclActionModifyDot1PPacket": es2226LowAclActionModifyDot1PPacket,
       "es2226LowAclActionModifyDot1PValue": es2226LowAclActionModifyDot1PValue,
       "es2226LowAclActionModifyQoSPacket": es2226LowAclActionModifyQoSPacket,
       "es2226LowAclActionModifyQoSValue": es2226LowAclActionModifyQoSValue,
       "es2226LowAclRateMeter": es2226LowAclRateMeter,
       "es2226LowAclRowStatus": es2226LowAclRowStatus,
       "es2226TrunkInfo": es2226TrunkInfo,
       "es2226TrunkPort": es2226TrunkPort,
       "es2226TrunkPortTable": es2226TrunkPortTable,
       "es2226TrunkPortEntry": es2226TrunkPortEntry,
       "es2226TrunkPortIndex": es2226TrunkPortIndex,
       "es2226TrunkPortMethod": es2226TrunkPortMethod,
       "es2226TrunkPortGroup": es2226TrunkPortGroup,
       "es2226TrunkPortActiveLacp": es2226TrunkPortActiveLacp,
       "es2226TrunkPortAggtr": es2226TrunkPortAggtr,
       "es2226TrunkPortStatus": es2226TrunkPortStatus,
       "es2226TrunkPortCurrentMode": es2226TrunkPortCurrentMode,
       "es2226AggregatorView": es2226AggregatorView,
       "es2226AggregatorViewTable": es2226AggregatorViewTable,
       "es2226AggregatorViewEntry": es2226AggregatorViewEntry,
       "es2226AggregatorViewIndex": es2226AggregatorViewIndex,
       "es2226AggregatorViewMethod": es2226AggregatorViewMethod,
       "es2226AggregatorViewMemberPorts": es2226AggregatorViewMemberPorts,
       "es2226AggregatorViewReadyPorts": es2226AggregatorViewReadyPorts,
       "es2226LacpSystemConfiguration": es2226LacpSystemConfiguration,
       "es2226LacpSystemPriority": es2226LacpSystemPriority,
       "es2226LacpSystemHashMethod": es2226LacpSystemHashMethod,
       "es2226Dhcprelay": es2226Dhcprelay,
       "es2226DhcpRelayState": es2226DhcpRelayState,
       "es2226DhcpRelayLifeTime": es2226DhcpRelayLifeTime,
       "es2226DhcpRelayOption82": es2226DhcpRelayOption82,
       "es2226DhcpRelayOption82Action": es2226DhcpRelayOption82Action,
       "es2226DhcpRelayServerPort": es2226DhcpRelayServerPort,
       "es2226DhcpRelayServerIP": es2226DhcpRelayServerIP,
       "es2226Multicast": es2226Multicast,
       "es2226IgmpSetting": es2226IgmpSetting,
       "es2226IgmpSnoopingState": es2226IgmpSnoopingState,
       "es2226IgmpSnoopingUnregisterMulticastFlooding": es2226IgmpSnoopingUnregisterMulticastFlooding,
       "es2226IgmpSnoopingGeneralQueryInterval": es2226IgmpSnoopingGeneralQueryInterval,
       "es2226IgmpSnoopingGeneralQueryMaxResponseTime": es2226IgmpSnoopingGeneralQueryMaxResponseTime,
       "es2226IgmpSnoopingGeneralQueryTimeout": es2226IgmpSnoopingGeneralQueryTimeout,
       "es2226IgmpSnoopingSpecificQueryCount": es2226IgmpSnoopingSpecificQueryCount,
       "es2226IgmpSnoopingSpecificQueryMaxResponseTime": es2226IgmpSnoopingSpecificQueryMaxResponseTime,
       "es2226IgmpSnoopingSpecificQueryTimeout": es2226IgmpSnoopingSpecificQueryTimeout,
       "es2226IgmpSnoopingSettingTable": es2226IgmpSnoopingSettingTable,
       "es2226IgmpSnoopingSettingEntry": es2226IgmpSnoopingSettingEntry,
       "es2226IgmpSnoopingSettingPortIndex": es2226IgmpSnoopingSettingPortIndex,
       "es2226IgmpSnoopingSettingMulticastGroupLimit": es2226IgmpSnoopingSettingMulticastGroupLimit,
       "es2226IgmpSnoopingSettingIGMPRouter": es2226IgmpSnoopingSettingIGMPRouter,
       "es2226IgmpVlan": es2226IgmpVlan,
       "es2226IgmpVlanNumbers": es2226IgmpVlanNumbers,
       "es2226IgmpVlanCreatStatus": es2226IgmpVlanCreatStatus,
       "es2226IgmpVlanTable": es2226IgmpVlanTable,
       "es2226IgmpVlanEntry": es2226IgmpVlanEntry,
       "es2226IgmpVlanIndex": es2226IgmpVlanIndex,
       "es2226IgmpVlanVid": es2226IgmpVlanVid,
       "es2226IgmpVlanRowStatus": es2226IgmpVlanRowStatus,
       "es2226IgmpVlanGroupAllow": es2226IgmpVlanGroupAllow,
       "es2226IgmpVlanGroupAllowCreatStatus": es2226IgmpVlanGroupAllowCreatStatus,
       "es2226IgmpVlanGroupAllowTable": es2226IgmpVlanGroupAllowTable,
       "es2226IgmpVlanGroupAllowEntry": es2226IgmpVlanGroupAllowEntry,
       "es2226IgmpVlanGroupAllowIndex": es2226IgmpVlanGroupAllowIndex,
       "es2226IgmpVlanGroupAllowStartAddress": es2226IgmpVlanGroupAllowStartAddress,
       "es2226IgmpVlanGroupAllowEndAddress": es2226IgmpVlanGroupAllowEndAddress,
       "es2226IgmpVlanGroupAllowVid": es2226IgmpVlanGroupAllowVid,
       "es2226IgmpVlanGroupAllowPortMember": es2226IgmpVlanGroupAllowPortMember,
       "es2226IgmpVlanGroupAllowRowStatus": es2226IgmpVlanGroupAllowRowStatus,
       "es2226MvrSetting": es2226MvrSetting,
       "es2226MvrSettingMulticastVlanRegistration": es2226MvrSettingMulticastVlanRegistration,
       "es2226MvrSettingMulticastVlanIdConf": es2226MvrSettingMulticastVlanIdConf,
       "es2226MvrSettingMulticastVlanIdShow": es2226MvrSettingMulticastVlanIdShow,
       "es2226MvrSettingTable": es2226MvrSettingTable,
       "es2226MvrSettingEntry": es2226MvrSettingEntry,
       "es2226MvrSettingPort": es2226MvrSettingPort,
       "es2226MvrSettingServerType": es2226MvrSettingServerType,
       "es2226MvrSettingTagging": es2226MvrSettingTagging,
       "es2226MulticastStatus": es2226MulticastStatus,
       "es2226MulticastStatusTable": es2226MulticastStatusTable,
       "es2226MulticastStatusEntry": es2226MulticastStatusEntry,
       "es2226MulticastStatusIndex": es2226MulticastStatusIndex,
       "es2226MulticastStatusVid": es2226MulticastStatusVid,
       "es2226MulticastStatusMulticastGroup": es2226MulticastStatusMulticastGroup,
       "es2226MulticastStatusPortMember": es2226MulticastStatusPortMember,
       "es2226RadiusIgmpSetting": es2226RadiusIgmpSetting,
       "es2226RadiusIgmpServer1": es2226RadiusIgmpServer1,
       "es2226RadiusIgmpPortNumber1": es2226RadiusIgmpPortNumber1,
       "es2226RadiusIgmpServer2": es2226RadiusIgmpServer2,
       "es2226RadiusIgmpPortNumber2": es2226RadiusIgmpPortNumber2,
       "es2226RadiusIgmpSecretKey1": es2226RadiusIgmpSecretKey1,
       "es2226RadiusIgmpAccountingServer1": es2226RadiusIgmpAccountingServer1,
       "es2226RadiusIgmpAccountingPortNumber1": es2226RadiusIgmpAccountingPortNumber1,
       "es2226RadiusIgmpAccountingServer2": es2226RadiusIgmpAccountingServer2,
       "es2226RadiusIgmpAccountingPortNumber2": es2226RadiusIgmpAccountingPortNumber2,
       "es2226RadiusIgmpSecretKey2": es2226RadiusIgmpSecretKey2,
       "es2226RadiusIgmpResponseTimeout": es2226RadiusIgmpResponseTimeout,
       "es2226RadiusIgmpNumberOfRetry": es2226RadiusIgmpNumberOfRetry,
       "es2226RadiusIgmpPortMember": es2226RadiusIgmpPortMember}
)
