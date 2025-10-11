# SNMP MIB module (LANCOM-ES-2126PLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-ES-2126PLUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:59 2025
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
_FastEthernetSwitches_ObjectIdentity = ObjectIdentity
fastEthernetSwitches = _FastEthernetSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2)
)
_LancomES2126PLUS_ObjectIdentity = ObjectIdentity
lancomES2126PLUS = _LancomES2126PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128)
)
_Es2126plusProduces_ObjectIdentity = ObjectIdentity
es2126plusProduces = _Es2126plusProduces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1)
)
_Es2126plusSystem_ObjectIdentity = ObjectIdentity
es2126plusSystem = _Es2126plusSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1)
)
_Es2126plusCommonSys_ObjectIdentity = ObjectIdentity
es2126plusCommonSys = _Es2126plusCommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1)
)


class _Es2126plusReboot_Type(Integer32):
    """Custom type es2126plusReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126plusReboot_Type.__name__ = "Integer32"
_Es2126plusReboot_Object = MibScalar
es2126plusReboot = _Es2126plusReboot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 1),
    _Es2126plusReboot_Type()
)
es2126plusReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusReboot.setStatus("current")
_Es2126plusBiosVsersion_Type = DisplayString
_Es2126plusBiosVsersion_Object = MibScalar
es2126plusBiosVsersion = _Es2126plusBiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 2),
    _Es2126plusBiosVsersion_Type()
)
es2126plusBiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusBiosVsersion.setStatus("current")
_Es2126plusFirmwareVersion_Type = DisplayString
_Es2126plusFirmwareVersion_Object = MibScalar
es2126plusFirmwareVersion = _Es2126plusFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 3),
    _Es2126plusFirmwareVersion_Type()
)
es2126plusFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusFirmwareVersion.setStatus("current")
_Es2126plusHardwareVersion_Type = DisplayString
_Es2126plusHardwareVersion_Object = MibScalar
es2126plusHardwareVersion = _Es2126plusHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 4),
    _Es2126plusHardwareVersion_Type()
)
es2126plusHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusHardwareVersion.setStatus("current")
_Es2126plusMechanicalVersion_Type = DisplayString
_Es2126plusMechanicalVersion_Object = MibScalar
es2126plusMechanicalVersion = _Es2126plusMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 5),
    _Es2126plusMechanicalVersion_Type()
)
es2126plusMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusMechanicalVersion.setStatus("current")
_Es2126plusSerialNumber_Type = DisplayString
_Es2126plusSerialNumber_Object = MibScalar
es2126plusSerialNumber = _Es2126plusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 6),
    _Es2126plusSerialNumber_Type()
)
es2126plusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusSerialNumber.setStatus("current")
_Es2126plusHostMacAddress_Type = DisplayString
_Es2126plusHostMacAddress_Object = MibScalar
es2126plusHostMacAddress = _Es2126plusHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 7),
    _Es2126plusHostMacAddress_Type()
)
es2126plusHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusHostMacAddress.setStatus("current")
_Es2126plusDevicePort_Type = DisplayString
_Es2126plusDevicePort_Object = MibScalar
es2126plusDevicePort = _Es2126plusDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 8),
    _Es2126plusDevicePort_Type()
)
es2126plusDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusDevicePort.setStatus("current")
_Es2126plusRamSize_Type = DisplayString
_Es2126plusRamSize_Object = MibScalar
es2126plusRamSize = _Es2126plusRamSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 9),
    _Es2126plusRamSize_Type()
)
es2126plusRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusRamSize.setStatus("current")
_Es2126plusFlashSize_Type = DisplayString
_Es2126plusFlashSize_Object = MibScalar
es2126plusFlashSize = _Es2126plusFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 10),
    _Es2126plusFlashSize_Type()
)
es2126plusFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusFlashSize.setStatus("current")
_Es2126plusSystemDescription_Type = DisplayString
_Es2126plusSystemDescription_Object = MibScalar
es2126plusSystemDescription = _Es2126plusSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 11),
    _Es2126plusSystemDescription_Type()
)
es2126plusSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusSystemDescription.setStatus("current")
_Es2126plusDeviceName_Type = DisplayString
_Es2126plusDeviceName_Object = MibScalar
es2126plusDeviceName = _Es2126plusDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 1, 12),
    _Es2126plusDeviceName_Type()
)
es2126plusDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDeviceName.setStatus("current")
_Es2126plusIP_ObjectIdentity = ObjectIdentity
es2126plusIP = _Es2126plusIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2)
)


class _Es2126plusDhcpSetting_Type(Integer32):
    """Custom type es2126plusDhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusDhcpSetting_Type.__name__ = "Integer32"
_Es2126plusDhcpSetting_Object = MibScalar
es2126plusDhcpSetting = _Es2126plusDhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2, 1),
    _Es2126plusDhcpSetting_Type()
)
es2126plusDhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDhcpSetting.setStatus("current")
_Es2126plusIPAddress_Type = IpAddress
_Es2126plusIPAddress_Object = MibScalar
es2126plusIPAddress = _Es2126plusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2, 2),
    _Es2126plusIPAddress_Type()
)
es2126plusIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusIPAddress.setStatus("current")
_Es2126plusNetMask_Type = IpAddress
_Es2126plusNetMask_Object = MibScalar
es2126plusNetMask = _Es2126plusNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2, 3),
    _Es2126plusNetMask_Type()
)
es2126plusNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusNetMask.setStatus("current")
_Es2126plusDefaultGateway_Type = IpAddress
_Es2126plusDefaultGateway_Object = MibScalar
es2126plusDefaultGateway = _Es2126plusDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2, 4),
    _Es2126plusDefaultGateway_Type()
)
es2126plusDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDefaultGateway.setStatus("current")


class _Es2126plusDnsSetting_Type(Integer32):
    """Custom type es2126plusDnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusDnsSetting_Type.__name__ = "Integer32"
_Es2126plusDnsSetting_Object = MibScalar
es2126plusDnsSetting = _Es2126plusDnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2, 5),
    _Es2126plusDnsSetting_Type()
)
es2126plusDnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDnsSetting.setStatus("current")
_Es2126plusDnsServer_Type = IpAddress
_Es2126plusDnsServer_Object = MibScalar
es2126plusDnsServer = _Es2126plusDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 2, 6),
    _Es2126plusDnsServer_Type()
)
es2126plusDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDnsServer.setStatus("current")
_Es2126plusTime_ObjectIdentity = ObjectIdentity
es2126plusTime = _Es2126plusTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3)
)
_Es2126plusSystemCurrentTime_Type = DisplayString
_Es2126plusSystemCurrentTime_Object = MibScalar
es2126plusSystemCurrentTime = _Es2126plusSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 1),
    _Es2126plusSystemCurrentTime_Type()
)
es2126plusSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusSystemCurrentTime.setStatus("current")
_Es2126plusManualTimeSetting_Type = DisplayString
_Es2126plusManualTimeSetting_Object = MibScalar
es2126plusManualTimeSetting = _Es2126plusManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 2),
    _Es2126plusManualTimeSetting_Type()
)
es2126plusManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManualTimeSetting.setStatus("current")
_Es2126plusNTPServer_Type = DisplayString
_Es2126plusNTPServer_Object = MibScalar
es2126plusNTPServer = _Es2126plusNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 3),
    _Es2126plusNTPServer_Type()
)
es2126plusNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusNTPServer.setStatus("current")


class _Es2126plusNTPTimeZone_Type(Integer32):
    """Custom type es2126plusNTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Es2126plusNTPTimeZone_Type.__name__ = "Integer32"
_Es2126plusNTPTimeZone_Object = MibScalar
es2126plusNTPTimeZone = _Es2126plusNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 4),
    _Es2126plusNTPTimeZone_Type()
)
es2126plusNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusNTPTimeZone.setStatus("current")


class _Es2126plusNTPTimeSync_Type(Integer32):
    """Custom type es2126plusNTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusNTPTimeSync_Type.__name__ = "Integer32"
_Es2126plusNTPTimeSync_Object = MibScalar
es2126plusNTPTimeSync = _Es2126plusNTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 5),
    _Es2126plusNTPTimeSync_Type()
)
es2126plusNTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusNTPTimeSync.setStatus("current")


class _Es2126plusDaylightSavingTime_Type(Integer32):
    """Custom type es2126plusDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Es2126plusDaylightSavingTime_Type.__name__ = "Integer32"
_Es2126plusDaylightSavingTime_Object = MibScalar
es2126plusDaylightSavingTime = _Es2126plusDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 6),
    _Es2126plusDaylightSavingTime_Type()
)
es2126plusDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDaylightSavingTime.setStatus("current")
_Es2126plusDaylightStartTime_Type = DisplayString
_Es2126plusDaylightStartTime_Object = MibScalar
es2126plusDaylightStartTime = _Es2126plusDaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 7),
    _Es2126plusDaylightStartTime_Type()
)
es2126plusDaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDaylightStartTime.setStatus("current")
_Es2126plusDaylightEndTime_Type = DisplayString
_Es2126plusDaylightEndTime_Object = MibScalar
es2126plusDaylightEndTime = _Es2126plusDaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 3, 8),
    _Es2126plusDaylightEndTime_Type()
)
es2126plusDaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDaylightEndTime.setStatus("current")
_Es2126plusAccount_ObjectIdentity = ObjectIdentity
es2126plusAccount = _Es2126plusAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4)
)


class _Es2126plusAccountNumber_Type(Integer32):
    """Custom type es2126plusAccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2126plusAccountNumber_Type.__name__ = "Integer32"
_Es2126plusAccountNumber_Object = MibScalar
es2126plusAccountNumber = _Es2126plusAccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 1),
    _Es2126plusAccountNumber_Type()
)
es2126plusAccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusAccountNumber.setStatus("current")
_Es2126plusAccountTable_Object = MibTable
es2126plusAccountTable = _Es2126plusAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    es2126plusAccountTable.setStatus("current")
_Es2126plusAccountEntry_Object = MibTableRow
es2126plusAccountEntry = _Es2126plusAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 2, 1)
)
es2126plusAccountEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusAccountIndex"),
)
if mibBuilder.loadTexts:
    es2126plusAccountEntry.setStatus("current")


class _Es2126plusAccountIndex_Type(Integer32):
    """Custom type es2126plusAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2126plusAccountIndex_Type.__name__ = "Integer32"
_Es2126plusAccountIndex_Object = MibTableColumn
es2126plusAccountIndex = _Es2126plusAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 2, 1, 1),
    _Es2126plusAccountIndex_Type()
)
es2126plusAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusAccountIndex.setStatus("current")
_Es2126plusAccountAuthorization_Type = DisplayString
_Es2126plusAccountAuthorization_Object = MibTableColumn
es2126plusAccountAuthorization = _Es2126plusAccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 2, 1, 2),
    _Es2126plusAccountAuthorization_Type()
)
es2126plusAccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusAccountAuthorization.setStatus("current")
_Es2126plusAccountName_Type = DisplayString
_Es2126plusAccountName_Object = MibTableColumn
es2126plusAccountName = _Es2126plusAccountName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 2, 1, 3),
    _Es2126plusAccountName_Type()
)
es2126plusAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountName.setStatus("current")
_Es2126plusAccountPassword_Type = DisplayString
_Es2126plusAccountPassword_Object = MibTableColumn
es2126plusAccountPassword = _Es2126plusAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 2, 1, 4),
    _Es2126plusAccountPassword_Type()
)
es2126plusAccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountPassword.setStatus("current")
_Es2126plusAccountAddName_Type = DisplayString
_Es2126plusAccountAddName_Object = MibScalar
es2126plusAccountAddName = _Es2126plusAccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 3),
    _Es2126plusAccountAddName_Type()
)
es2126plusAccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountAddName.setStatus("current")
_Es2126plusAccountAddPassword_Type = DisplayString
_Es2126plusAccountAddPassword_Object = MibScalar
es2126plusAccountAddPassword = _Es2126plusAccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 4),
    _Es2126plusAccountAddPassword_Type()
)
es2126plusAccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountAddPassword.setStatus("current")


class _Es2126plusDoAccountAdd_Type(Integer32):
    """Custom type es2126plusDoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusDoAccountAdd_Type.__name__ = "Integer32"
_Es2126plusDoAccountAdd_Object = MibScalar
es2126plusDoAccountAdd = _Es2126plusDoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 5),
    _Es2126plusDoAccountAdd_Type()
)
es2126plusDoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDoAccountAdd.setStatus("current")


class _Es2126plusAccountDel_Type(Integer32):
    """Custom type es2126plusAccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Es2126plusAccountDel_Type.__name__ = "Integer32"
_Es2126plusAccountDel_Object = MibScalar
es2126plusAccountDel = _Es2126plusAccountDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 1, 4, 6),
    _Es2126plusAccountDel_Type()
)
es2126plusAccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountDel.setStatus("current")
_Es2126plusSnmp_ObjectIdentity = ObjectIdentity
es2126plusSnmp = _Es2126plusSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2)
)
_Es2126plusGetCommunity_Type = DisplayString
_Es2126plusGetCommunity_Object = MibScalar
es2126plusGetCommunity = _Es2126plusGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 1),
    _Es2126plusGetCommunity_Type()
)
es2126plusGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGetCommunity.setStatus("current")
_Es2126plusSetCommunity_Type = DisplayString
_Es2126plusSetCommunity_Object = MibScalar
es2126plusSetCommunity = _Es2126plusSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 2),
    _Es2126plusSetCommunity_Type()
)
es2126plusSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusSetCommunity.setStatus("current")


class _Es2126plusTrapHostNumber_Type(Integer32):
    """Custom type es2126plusTrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126plusTrapHostNumber_Type.__name__ = "Integer32"
_Es2126plusTrapHostNumber_Object = MibScalar
es2126plusTrapHostNumber = _Es2126plusTrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 3),
    _Es2126plusTrapHostNumber_Type()
)
es2126plusTrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusTrapHostNumber.setStatus("current")
_Es2126plusTrapHostTable_Object = MibTable
es2126plusTrapHostTable = _Es2126plusTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 4)
)
if mibBuilder.loadTexts:
    es2126plusTrapHostTable.setStatus("current")
_Es2126plusTrapHostEntry_Object = MibTableRow
es2126plusTrapHostEntry = _Es2126plusTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 4, 1)
)
es2126plusTrapHostEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusTrapHostIndex"),
)
if mibBuilder.loadTexts:
    es2126plusTrapHostEntry.setStatus("current")


class _Es2126plusTrapHostIndex_Type(Integer32):
    """Custom type es2126plusTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126plusTrapHostIndex_Type.__name__ = "Integer32"
_Es2126plusTrapHostIndex_Object = MibTableColumn
es2126plusTrapHostIndex = _Es2126plusTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 4, 1, 1),
    _Es2126plusTrapHostIndex_Type()
)
es2126plusTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusTrapHostIndex.setStatus("current")
_Es2126plusTrapHostIP_Type = IpAddress
_Es2126plusTrapHostIP_Object = MibTableColumn
es2126plusTrapHostIP = _Es2126plusTrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 4, 1, 2),
    _Es2126plusTrapHostIP_Type()
)
es2126plusTrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrapHostIP.setStatus("current")


class _Es2126plusTrapHostPort_Type(Integer32):
    """Custom type es2126plusTrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusTrapHostPort_Type.__name__ = "Integer32"
_Es2126plusTrapHostPort_Object = MibTableColumn
es2126plusTrapHostPort = _Es2126plusTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 4, 1, 3),
    _Es2126plusTrapHostPort_Type()
)
es2126plusTrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrapHostPort.setStatus("current")
_Es2126plusTrapHostCommunity_Type = DisplayString
_Es2126plusTrapHostCommunity_Object = MibTableColumn
es2126plusTrapHostCommunity = _Es2126plusTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 4, 1, 4),
    _Es2126plusTrapHostCommunity_Type()
)
es2126plusTrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrapHostCommunity.setStatus("current")
_Es2126plusRegisterMonitor_Type = DisplayString
_Es2126plusRegisterMonitor_Object = MibScalar
es2126plusRegisterMonitor = _Es2126plusRegisterMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 5),
    _Es2126plusRegisterMonitor_Type()
)
es2126plusRegisterMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusRegisterMonitor.setStatus("current")
_Es2126plusDeleteMonitor_Type = DisplayString
_Es2126plusDeleteMonitor_Object = MibScalar
es2126plusDeleteMonitor = _Es2126plusDeleteMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 6),
    _Es2126plusDeleteMonitor_Type()
)
es2126plusDeleteMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDeleteMonitor.setStatus("current")
_Es2126plusMonitorTable_Object = MibTable
es2126plusMonitorTable = _Es2126plusMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 7)
)
if mibBuilder.loadTexts:
    es2126plusMonitorTable.setStatus("current")
_Es2126plusMonitorEntry_Object = MibTableRow
es2126plusMonitorEntry = _Es2126plusMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 7, 1)
)
es2126plusMonitorEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusMonitorTableIp"),
)
if mibBuilder.loadTexts:
    es2126plusMonitorEntry.setStatus("current")
_Es2126plusMonitorTableIp_Type = IpAddress
_Es2126plusMonitorTableIp_Object = MibTableColumn
es2126plusMonitorTableIp = _Es2126plusMonitorTableIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 7, 1, 1),
    _Es2126plusMonitorTableIp_Type()
)
es2126plusMonitorTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusMonitorTableIp.setStatus("current")
_Es2126plusMonitorTableMac_Type = DisplayString
_Es2126plusMonitorTableMac_Object = MibTableColumn
es2126plusMonitorTableMac = _Es2126plusMonitorTableMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 7, 1, 2),
    _Es2126plusMonitorTableMac_Type()
)
es2126plusMonitorTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusMonitorTableMac.setStatus("current")


class _Es2126plusTrapBootDelayTime_Type(Integer32):
    """Custom type es2126plusTrapBootDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2126plusTrapBootDelayTime_Type.__name__ = "Integer32"
_Es2126plusTrapBootDelayTime_Object = MibScalar
es2126plusTrapBootDelayTime = _Es2126plusTrapBootDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 2, 8),
    _Es2126plusTrapBootDelayTime_Type()
)
es2126plusTrapBootDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrapBootDelayTime.setStatus("current")
_Es2126plusAlarm_ObjectIdentity = ObjectIdentity
es2126plusAlarm = _Es2126plusAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3)
)
_Es2126plusEvent_ObjectIdentity = ObjectIdentity
es2126plusEvent = _Es2126plusEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1)
)


class _Es2126plusEventNumber_Type(Integer32):
    """Custom type es2126plusEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusEventNumber_Type.__name__ = "Integer32"
_Es2126plusEventNumber_Object = MibScalar
es2126plusEventNumber = _Es2126plusEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 1),
    _Es2126plusEventNumber_Type()
)
es2126plusEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusEventNumber.setStatus("current")
_Es2126plusEventTable_Object = MibTable
es2126plusEventTable = _Es2126plusEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    es2126plusEventTable.setStatus("current")
_Es2126plusEventEntry_Object = MibTableRow
es2126plusEventEntry = _Es2126plusEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 2, 1)
)
es2126plusEventEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusEventIndex"),
)
if mibBuilder.loadTexts:
    es2126plusEventEntry.setStatus("current")


class _Es2126plusEventIndex_Type(Integer32):
    """Custom type es2126plusEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusEventIndex_Type.__name__ = "Integer32"
_Es2126plusEventIndex_Object = MibTableColumn
es2126plusEventIndex = _Es2126plusEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 2, 1, 1),
    _Es2126plusEventIndex_Type()
)
es2126plusEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusEventIndex.setStatus("current")
_Es2126plusEventName_Type = DisplayString
_Es2126plusEventName_Object = MibTableColumn
es2126plusEventName = _Es2126plusEventName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 2, 1, 2),
    _Es2126plusEventName_Type()
)
es2126plusEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusEventName.setStatus("current")


class _Es2126plusEventSendEmail_Type(Integer32):
    """Custom type es2126plusEventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusEventSendEmail_Type.__name__ = "Integer32"
_Es2126plusEventSendEmail_Object = MibTableColumn
es2126plusEventSendEmail = _Es2126plusEventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 2, 1, 3),
    _Es2126plusEventSendEmail_Type()
)
es2126plusEventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEventSendEmail.setStatus("current")


class _Es2126plusEventSendTrap_Type(Integer32):
    """Custom type es2126plusEventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusEventSendTrap_Type.__name__ = "Integer32"
_Es2126plusEventSendTrap_Object = MibTableColumn
es2126plusEventSendTrap = _Es2126plusEventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 1, 2, 1, 4),
    _Es2126plusEventSendTrap_Type()
)
es2126plusEventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEventSendTrap.setStatus("current")
_Es2126plusEmail_ObjectIdentity = ObjectIdentity
es2126plusEmail = _Es2126plusEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2)
)
_Es2126plusEmailServer_Type = DisplayString
_Es2126plusEmailServer_Object = MibScalar
es2126plusEmailServer = _Es2126plusEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 1),
    _Es2126plusEmailServer_Type()
)
es2126plusEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEmailServer.setStatus("current")
_Es2126plusEmailUsername_Type = DisplayString
_Es2126plusEmailUsername_Object = MibScalar
es2126plusEmailUsername = _Es2126plusEmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 2),
    _Es2126plusEmailUsername_Type()
)
es2126plusEmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEmailUsername.setStatus("current")
_Es2126plusEmailPassword_Type = DisplayString
_Es2126plusEmailPassword_Object = MibScalar
es2126plusEmailPassword = _Es2126plusEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 3),
    _Es2126plusEmailPassword_Type()
)
es2126plusEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEmailPassword.setStatus("current")
_Es2126plusEmailSender_Type = DisplayString
_Es2126plusEmailSender_Object = MibScalar
es2126plusEmailSender = _Es2126plusEmailSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 4),
    _Es2126plusEmailSender_Type()
)
es2126plusEmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEmailSender.setStatus("current")
_Es2126plusEmailReturnPath_Type = DisplayString
_Es2126plusEmailReturnPath_Object = MibScalar
es2126plusEmailReturnPath = _Es2126plusEmailReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 5),
    _Es2126plusEmailReturnPath_Type()
)
es2126plusEmailReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEmailReturnPath.setStatus("current")


class _Es2126plusEmailUserNumber_Type(Integer32):
    """Custom type es2126plusEmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126plusEmailUserNumber_Type.__name__ = "Integer32"
_Es2126plusEmailUserNumber_Object = MibScalar
es2126plusEmailUserNumber = _Es2126plusEmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 6),
    _Es2126plusEmailUserNumber_Type()
)
es2126plusEmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusEmailUserNumber.setStatus("current")
_Es2126plusEmailUserTable_Object = MibTable
es2126plusEmailUserTable = _Es2126plusEmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    es2126plusEmailUserTable.setStatus("current")
_Es2126plusEmailUserEntry_Object = MibTableRow
es2126plusEmailUserEntry = _Es2126plusEmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 7, 1)
)
es2126plusEmailUserEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusEmailUserIndex"),
)
if mibBuilder.loadTexts:
    es2126plusEmailUserEntry.setStatus("current")


class _Es2126plusEmailUserIndex_Type(Integer32):
    """Custom type es2126plusEmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126plusEmailUserIndex_Type.__name__ = "Integer32"
_Es2126plusEmailUserIndex_Object = MibTableColumn
es2126plusEmailUserIndex = _Es2126plusEmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 7, 1, 1),
    _Es2126plusEmailUserIndex_Type()
)
es2126plusEmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusEmailUserIndex.setStatus("current")
_Es2126plusEmailUserAddress_Type = DisplayString
_Es2126plusEmailUserAddress_Object = MibTableColumn
es2126plusEmailUserAddress = _Es2126plusEmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 3, 2, 7, 1, 2),
    _Es2126plusEmailUserAddress_Type()
)
es2126plusEmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusEmailUserAddress.setStatus("current")
_Es2126plusTftp_ObjectIdentity = ObjectIdentity
es2126plusTftp = _Es2126plusTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 4)
)
_Es2126plusTftpRemoteServer_Type = IpAddress
_Es2126plusTftpRemoteServer_Object = MibScalar
es2126plusTftpRemoteServer = _Es2126plusTftpRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 4, 1),
    _Es2126plusTftpRemoteServer_Type()
)
es2126plusTftpRemoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTftpRemoteServer.setStatus("current")


class _Es2126plusTftpInternalServerState_Type(Integer32):
    """Custom type es2126plusTftpInternalServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusTftpInternalServerState_Type.__name__ = "Integer32"
_Es2126plusTftpInternalServerState_Object = MibScalar
es2126plusTftpInternalServerState = _Es2126plusTftpInternalServerState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 4, 2),
    _Es2126plusTftpInternalServerState_Type()
)
es2126plusTftpInternalServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTftpInternalServerState.setStatus("current")
_Es2126plusConfiguration_ObjectIdentity = ObjectIdentity
es2126plusConfiguration = _Es2126plusConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5)
)
_Es2126plusSaveRestore_ObjectIdentity = ObjectIdentity
es2126plusSaveRestore = _Es2126plusSaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 1)
)


class _Es2126plusSaveStart_Type(Integer32):
    """Custom type es2126plusSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusSaveStart_Type.__name__ = "Integer32"
_Es2126plusSaveStart_Object = MibScalar
es2126plusSaveStart = _Es2126plusSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 1, 1),
    _Es2126plusSaveStart_Type()
)
es2126plusSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusSaveStart.setStatus("current")


class _Es2126plusSaveUser_Type(Integer32):
    """Custom type es2126plusSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusSaveUser_Type.__name__ = "Integer32"
_Es2126plusSaveUser_Object = MibScalar
es2126plusSaveUser = _Es2126plusSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 1, 2),
    _Es2126plusSaveUser_Type()
)
es2126plusSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusSaveUser.setStatus("current")


class _Es2126plusRestoreDefault_Type(Integer32):
    """Custom type es2126plusRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126plusRestoreDefault_Type.__name__ = "Integer32"
_Es2126plusRestoreDefault_Object = MibScalar
es2126plusRestoreDefault = _Es2126plusRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 1, 3),
    _Es2126plusRestoreDefault_Type()
)
es2126plusRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusRestoreDefault.setStatus("current")


class _Es2126plusRestoreUser_Type(Integer32):
    """Custom type es2126plusRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusRestoreUser_Type.__name__ = "Integer32"
_Es2126plusRestoreUser_Object = MibScalar
es2126plusRestoreUser = _Es2126plusRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 1, 4),
    _Es2126plusRestoreUser_Type()
)
es2126plusRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusRestoreUser.setStatus("current")
_Es2126plusConfigFile_ObjectIdentity = ObjectIdentity
es2126plusConfigFile = _Es2126plusConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 2)
)
_Es2126plusExportConfigName_Type = DisplayString
_Es2126plusExportConfigName_Object = MibScalar
es2126plusExportConfigName = _Es2126plusExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 2, 1),
    _Es2126plusExportConfigName_Type()
)
es2126plusExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusExportConfigName.setStatus("current")


class _Es2126plusDoExportConfig_Type(Integer32):
    """Custom type es2126plusDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126plusDoExportConfig_Type.__name__ = "Integer32"
_Es2126plusDoExportConfig_Object = MibScalar
es2126plusDoExportConfig = _Es2126plusDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 2, 2),
    _Es2126plusDoExportConfig_Type()
)
es2126plusDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDoExportConfig.setStatus("current")
_Es2126plusImportConfigName_Type = DisplayString
_Es2126plusImportConfigName_Object = MibScalar
es2126plusImportConfigName = _Es2126plusImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 2, 3),
    _Es2126plusImportConfigName_Type()
)
es2126plusImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusImportConfigName.setStatus("current")


class _Es2126plusDoImportConfig_Type(Integer32):
    """Custom type es2126plusDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126plusDoImportConfig_Type.__name__ = "Integer32"
_Es2126plusDoImportConfig_Object = MibScalar
es2126plusDoImportConfig = _Es2126plusDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 5, 2, 4),
    _Es2126plusDoImportConfig_Type()
)
es2126plusDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDoImportConfig.setStatus("current")
_Es2126plusDiagnostic_ObjectIdentity = ObjectIdentity
es2126plusDiagnostic = _Es2126plusDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6)
)
_Es2126plusInternalLoopbackTest_Type = DisplayString
_Es2126plusInternalLoopbackTest_Object = MibScalar
es2126plusInternalLoopbackTest = _Es2126plusInternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 1),
    _Es2126plusInternalLoopbackTest_Type()
)
es2126plusInternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusInternalLoopbackTest.setStatus("current")
_Es2126plusExternalLoopbackTest_Type = DisplayString
_Es2126plusExternalLoopbackTest_Object = MibScalar
es2126plusExternalLoopbackTest = _Es2126plusExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 2),
    _Es2126plusExternalLoopbackTest_Type()
)
es2126plusExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusExternalLoopbackTest.setStatus("current")
_Es2126plusPingTest_Type = DisplayString
_Es2126plusPingTest_Object = MibScalar
es2126plusPingTest = _Es2126plusPingTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 3),
    _Es2126plusPingTest_Type()
)
es2126plusPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPingTest.setStatus("current")
_Es2126plusWatchdog_ObjectIdentity = ObjectIdentity
es2126plusWatchdog = _Es2126plusWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4)
)


class _Es2126plusWatchdogState_Type(Integer32):
    """Custom type es2126plusWatchdogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusWatchdogState_Type.__name__ = "Integer32"
_Es2126plusWatchdogState_Object = MibScalar
es2126plusWatchdogState = _Es2126plusWatchdogState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 1),
    _Es2126plusWatchdogState_Type()
)
es2126plusWatchdogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogState.setStatus("current")


class _Es2126plusWatchdogTimeGap_Type(Integer32):
    """Custom type es2126plusWatchdogTimeGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Es2126plusWatchdogTimeGap_Type.__name__ = "Integer32"
_Es2126plusWatchdogTimeGap_Object = MibScalar
es2126plusWatchdogTimeGap = _Es2126plusWatchdogTimeGap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 2),
    _Es2126plusWatchdogTimeGap_Type()
)
es2126plusWatchdogTimeGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogTimeGap.setStatus("current")
_Es2126plusWatchdogHost_Type = DisplayString
_Es2126plusWatchdogHost_Object = MibScalar
es2126plusWatchdogHost = _Es2126plusWatchdogHost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 3),
    _Es2126plusWatchdogHost_Type()
)
es2126plusWatchdogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogHost.setStatus("current")


class _Es2126plusWatchdogResetMgtInf_Type(Integer32):
    """Custom type es2126plusWatchdogResetMgtInf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusWatchdogResetMgtInf_Type.__name__ = "Integer32"
_Es2126plusWatchdogResetMgtInf_Object = MibScalar
es2126plusWatchdogResetMgtInf = _Es2126plusWatchdogResetMgtInf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 4),
    _Es2126plusWatchdogResetMgtInf_Type()
)
es2126plusWatchdogResetMgtInf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogResetMgtInf.setStatus("current")


class _Es2126plusWatchdogResetMgtInfCount_Type(Integer32):
    """Custom type es2126plusWatchdogResetMgtInfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Es2126plusWatchdogResetMgtInfCount_Type.__name__ = "Integer32"
_Es2126plusWatchdogResetMgtInfCount_Object = MibScalar
es2126plusWatchdogResetMgtInfCount = _Es2126plusWatchdogResetMgtInfCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 5),
    _Es2126plusWatchdogResetMgtInfCount_Type()
)
es2126plusWatchdogResetMgtInfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogResetMgtInfCount.setStatus("current")


class _Es2126plusWatchdogResetSystem_Type(Integer32):
    """Custom type es2126plusWatchdogResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusWatchdogResetSystem_Type.__name__ = "Integer32"
_Es2126plusWatchdogResetSystem_Object = MibScalar
es2126plusWatchdogResetSystem = _Es2126plusWatchdogResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 6),
    _Es2126plusWatchdogResetSystem_Type()
)
es2126plusWatchdogResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogResetSystem.setStatus("current")


class _Es2126plusWatchdogResetSystemCount_Type(Integer32):
    """Custom type es2126plusWatchdogResetSystemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Es2126plusWatchdogResetSystemCount_Type.__name__ = "Integer32"
_Es2126plusWatchdogResetSystemCount_Object = MibScalar
es2126plusWatchdogResetSystemCount = _Es2126plusWatchdogResetSystemCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 6, 4, 7),
    _Es2126plusWatchdogResetSystemCount_Type()
)
es2126plusWatchdogResetSystemCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusWatchdogResetSystemCount.setStatus("current")
_Es2126plusLog_ObjectIdentity = ObjectIdentity
es2126plusLog = _Es2126plusLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7)
)


class _Es2126plusClearLog_Type(Integer32):
    """Custom type es2126plusClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusClearLog_Type.__name__ = "Integer32"
_Es2126plusClearLog_Object = MibScalar
es2126plusClearLog = _Es2126plusClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 1),
    _Es2126plusClearLog_Type()
)
es2126plusClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusClearLog.setStatus("current")


class _Es2126plusUploadLog_Type(Integer32):
    """Custom type es2126plusUploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusUploadLog_Type.__name__ = "Integer32"
_Es2126plusUploadLog_Object = MibScalar
es2126plusUploadLog = _Es2126plusUploadLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 2),
    _Es2126plusUploadLog_Type()
)
es2126plusUploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusUploadLog.setStatus("current")


class _Es2126plusAutoUploadLogState_Type(Integer32):
    """Custom type es2126plusAutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusAutoUploadLogState_Type.__name__ = "Integer32"
_Es2126plusAutoUploadLogState_Object = MibScalar
es2126plusAutoUploadLogState = _Es2126plusAutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 3),
    _Es2126plusAutoUploadLogState_Type()
)
es2126plusAutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAutoUploadLogState.setStatus("current")


class _Es2126plusLogNumber_Type(Integer32):
    """Custom type es2126plusLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2126plusLogNumber_Type.__name__ = "Integer32"
_Es2126plusLogNumber_Object = MibScalar
es2126plusLogNumber = _Es2126plusLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 4),
    _Es2126plusLogNumber_Type()
)
es2126plusLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusLogNumber.setStatus("current")
_Es2126plusLogTable_Object = MibTable
es2126plusLogTable = _Es2126plusLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 5)
)
if mibBuilder.loadTexts:
    es2126plusLogTable.setStatus("current")
_Es2126plusLogEntry_Object = MibTableRow
es2126plusLogEntry = _Es2126plusLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 5, 1)
)
es2126plusLogEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusLogIndex"),
)
if mibBuilder.loadTexts:
    es2126plusLogEntry.setStatus("current")


class _Es2126plusLogIndex_Type(Integer32):
    """Custom type es2126plusLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Es2126plusLogIndex_Type.__name__ = "Integer32"
_Es2126plusLogIndex_Object = MibTableColumn
es2126plusLogIndex = _Es2126plusLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 5, 1, 1),
    _Es2126plusLogIndex_Type()
)
es2126plusLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusLogIndex.setStatus("current")
_Es2126plusLogEvent_Type = DisplayString
_Es2126plusLogEvent_Object = MibTableColumn
es2126plusLogEvent = _Es2126plusLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 7, 5, 1, 2),
    _Es2126plusLogEvent_Type()
)
es2126plusLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusLogEvent.setStatus("current")
_Es2126plusFirmware_ObjectIdentity = ObjectIdentity
es2126plusFirmware = _Es2126plusFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 8)
)
_Es2126plusFirmwareFileName_Type = DisplayString
_Es2126plusFirmwareFileName_Object = MibScalar
es2126plusFirmwareFileName = _Es2126plusFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 8, 1),
    _Es2126plusFirmwareFileName_Type()
)
es2126plusFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusFirmwareFileName.setStatus("current")


class _Es2126plusDoFirmwareUpgrade_Type(Integer32):
    """Custom type es2126plusDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Es2126plusDoFirmwareUpgrade_Object = MibScalar
es2126plusDoFirmwareUpgrade = _Es2126plusDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 8, 2),
    _Es2126plusDoFirmwareUpgrade_Type()
)
es2126plusDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDoFirmwareUpgrade.setStatus("current")
_Es2126plusPort_ObjectIdentity = ObjectIdentity
es2126plusPort = _Es2126plusPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9)
)
_Es2126plusPortStatus_ObjectIdentity = ObjectIdentity
es2126plusPortStatus = _Es2126plusPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1)
)


class _Es2126plusPortStatusNumber_Type(Integer32):
    """Custom type es2126plusPortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusPortStatusNumber_Type.__name__ = "Integer32"
_Es2126plusPortStatusNumber_Object = MibScalar
es2126plusPortStatusNumber = _Es2126plusPortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 1),
    _Es2126plusPortStatusNumber_Type()
)
es2126plusPortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusNumber.setStatus("current")
_Es2126plusPortStatusTable_Object = MibTable
es2126plusPortStatusTable = _Es2126plusPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    es2126plusPortStatusTable.setStatus("current")
_Es2126plusPortStatusEntry_Object = MibTableRow
es2126plusPortStatusEntry = _Es2126plusPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1)
)
es2126plusPortStatusEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusPortStatusIndex"),
)
if mibBuilder.loadTexts:
    es2126plusPortStatusEntry.setStatus("current")


class _Es2126plusPortStatusIndex_Type(Integer32):
    """Custom type es2126plusPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusPortStatusIndex_Type.__name__ = "Integer32"
_Es2126plusPortStatusIndex_Object = MibTableColumn
es2126plusPortStatusIndex = _Es2126plusPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 1),
    _Es2126plusPortStatusIndex_Type()
)
es2126plusPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusIndex.setStatus("current")
_Es2126plusPortStatusMedia_Type = DisplayString
_Es2126plusPortStatusMedia_Object = MibTableColumn
es2126plusPortStatusMedia = _Es2126plusPortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 2),
    _Es2126plusPortStatusMedia_Type()
)
es2126plusPortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusMedia.setStatus("current")
_Es2126plusPortStatusLink_Type = DisplayString
_Es2126plusPortStatusLink_Object = MibTableColumn
es2126plusPortStatusLink = _Es2126plusPortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 3),
    _Es2126plusPortStatusLink_Type()
)
es2126plusPortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusLink.setStatus("current")
_Es2126plusPortStatusPortState_Type = DisplayString
_Es2126plusPortStatusPortState_Object = MibTableColumn
es2126plusPortStatusPortState = _Es2126plusPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 4),
    _Es2126plusPortStatusPortState_Type()
)
es2126plusPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusPortState.setStatus("current")
_Es2126plusPortStatusAutoNego_Type = DisplayString
_Es2126plusPortStatusAutoNego_Object = MibTableColumn
es2126plusPortStatusAutoNego = _Es2126plusPortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 5),
    _Es2126plusPortStatusAutoNego_Type()
)
es2126plusPortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusAutoNego.setStatus("current")
_Es2126plusPortStatusSpdDpx_Type = DisplayString
_Es2126plusPortStatusSpdDpx_Object = MibTableColumn
es2126plusPortStatusSpdDpx = _Es2126plusPortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 6),
    _Es2126plusPortStatusSpdDpx_Type()
)
es2126plusPortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusSpdDpx.setStatus("current")
_Es2126plusPortStatusRxPause_Type = DisplayString
_Es2126plusPortStatusRxPause_Object = MibTableColumn
es2126plusPortStatusRxPause = _Es2126plusPortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 7),
    _Es2126plusPortStatusRxPause_Type()
)
es2126plusPortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusRxPause.setStatus("current")
_Es2126plusPortStatusTxPause_Type = DisplayString
_Es2126plusPortStatusTxPause_Object = MibTableColumn
es2126plusPortStatusTxPause = _Es2126plusPortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 8),
    _Es2126plusPortStatusTxPause_Type()
)
es2126plusPortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusTxPause.setStatus("current")
_Es2126plusPortStatusDescription_Type = DisplayString
_Es2126plusPortStatusDescription_Object = MibTableColumn
es2126plusPortStatusDescription = _Es2126plusPortStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 1, 2, 1, 9),
    _Es2126plusPortStatusDescription_Type()
)
es2126plusPortStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortStatusDescription.setStatus("current")
_Es2126plusPortConf_ObjectIdentity = ObjectIdentity
es2126plusPortConf = _Es2126plusPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2)
)


class _Es2126plusPortConfNumber_Type(Integer32):
    """Custom type es2126plusPortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusPortConfNumber_Type.__name__ = "Integer32"
_Es2126plusPortConfNumber_Object = MibScalar
es2126plusPortConfNumber = _Es2126plusPortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 1),
    _Es2126plusPortConfNumber_Type()
)
es2126plusPortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortConfNumber.setStatus("current")
_Es2126plusPortConfTable_Object = MibTable
es2126plusPortConfTable = _Es2126plusPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    es2126plusPortConfTable.setStatus("current")
_Es2126plusPortConfEntry_Object = MibTableRow
es2126plusPortConfEntry = _Es2126plusPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2, 1)
)
es2126plusPortConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusPortConfIndex"),
)
if mibBuilder.loadTexts:
    es2126plusPortConfEntry.setStatus("current")


class _Es2126plusPortConfIndex_Type(Integer32):
    """Custom type es2126plusPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusPortConfIndex_Type.__name__ = "Integer32"
_Es2126plusPortConfIndex_Object = MibTableColumn
es2126plusPortConfIndex = _Es2126plusPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2, 1, 1),
    _Es2126plusPortConfIndex_Type()
)
es2126plusPortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortConfIndex.setStatus("current")


class _Es2126plusPortConfPortState_Type(Integer32):
    """Custom type es2126plusPortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusPortConfPortState_Type.__name__ = "Integer32"
_Es2126plusPortConfPortState_Object = MibTableColumn
es2126plusPortConfPortState = _Es2126plusPortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2, 1, 2),
    _Es2126plusPortConfPortState_Type()
)
es2126plusPortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortConfPortState.setStatus("current")


class _Es2126plusPortConfSpdDpx_Type(Integer32):
    """Custom type es2126plusPortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Es2126plusPortConfSpdDpx_Type.__name__ = "Integer32"
_Es2126plusPortConfSpdDpx_Object = MibTableColumn
es2126plusPortConfSpdDpx = _Es2126plusPortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2, 1, 3),
    _Es2126plusPortConfSpdDpx_Type()
)
es2126plusPortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortConfSpdDpx.setStatus("current")


class _Es2126plusPortConfFlwCtrl_Type(Integer32):
    """Custom type es2126plusPortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusPortConfFlwCtrl_Type.__name__ = "Integer32"
_Es2126plusPortConfFlwCtrl_Object = MibTableColumn
es2126plusPortConfFlwCtrl = _Es2126plusPortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2, 1, 4),
    _Es2126plusPortConfFlwCtrl_Type()
)
es2126plusPortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortConfFlwCtrl.setStatus("current")
_Es2126plusPortConfDescription_Type = DisplayString
_Es2126plusPortConfDescription_Object = MibTableColumn
es2126plusPortConfDescription = _Es2126plusPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 2, 2, 1, 5),
    _Es2126plusPortConfDescription_Type()
)
es2126plusPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortConfDescription.setStatus("current")
_Es2126plusPortBandwidth_ObjectIdentity = ObjectIdentity
es2126plusPortBandwidth = _Es2126plusPortBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3)
)
_Es2126plusPortBandwidthTable_Object = MibTable
es2126plusPortBandwidthTable = _Es2126plusPortBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    es2126plusPortBandwidthTable.setStatus("current")
_Es2126plusPortBandwidthEntry_Object = MibTableRow
es2126plusPortBandwidthEntry = _Es2126plusPortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 1, 1)
)
es2126plusPortBandwidthEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusPortBandwidthIndex"),
)
if mibBuilder.loadTexts:
    es2126plusPortBandwidthEntry.setStatus("current")


class _Es2126plusPortBandwidthIndex_Type(Integer32):
    """Custom type es2126plusPortBandwidthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusPortBandwidthIndex_Type.__name__ = "Integer32"
_Es2126plusPortBandwidthIndex_Object = MibTableColumn
es2126plusPortBandwidthIndex = _Es2126plusPortBandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 1, 1, 1),
    _Es2126plusPortBandwidthIndex_Type()
)
es2126plusPortBandwidthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortBandwidthIndex.setStatus("current")


class _Es2126plusPortBandwidthIngressRate_Type(Integer32):
    """Custom type es2126plusPortBandwidthIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 1024000),
    )


_Es2126plusPortBandwidthIngressRate_Type.__name__ = "Integer32"
_Es2126plusPortBandwidthIngressRate_Object = MibTableColumn
es2126plusPortBandwidthIngressRate = _Es2126plusPortBandwidthIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 1, 1, 2),
    _Es2126plusPortBandwidthIngressRate_Type()
)
es2126plusPortBandwidthIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBandwidthIngressRate.setStatus("current")


class _Es2126plusPortBandwidthEgressRate_Type(Integer32):
    """Custom type es2126plusPortBandwidthEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 1024000),
    )


_Es2126plusPortBandwidthEgressRate_Type.__name__ = "Integer32"
_Es2126plusPortBandwidthEgressRate_Object = MibTableColumn
es2126plusPortBandwidthEgressRate = _Es2126plusPortBandwidthEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 1, 1, 3),
    _Es2126plusPortBandwidthEgressRate_Type()
)
es2126plusPortBandwidthEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBandwidthEgressRate.setStatus("current")


class _Es2126plusPortBandwidthStormType_Type(Integer32):
    """Custom type es2126plusPortBandwidthStormType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Es2126plusPortBandwidthStormType_Type.__name__ = "Integer32"
_Es2126plusPortBandwidthStormType_Object = MibScalar
es2126plusPortBandwidthStormType = _Es2126plusPortBandwidthStormType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 2),
    _Es2126plusPortBandwidthStormType_Type()
)
es2126plusPortBandwidthStormType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBandwidthStormType.setStatus("current")


class _Es2126plusPortBandwidthStormRate_Type(Integer32):
    """Custom type es2126plusPortBandwidthStormRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Es2126plusPortBandwidthStormRate_Type.__name__ = "Integer32"
_Es2126plusPortBandwidthStormRate_Object = MibScalar
es2126plusPortBandwidthStormRate = _Es2126plusPortBandwidthStormRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 3, 3),
    _Es2126plusPortBandwidthStormRate_Type()
)
es2126plusPortBandwidthStormRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBandwidthStormRate.setStatus("current")
_Es2126plusPortSFPInfo_ObjectIdentity = ObjectIdentity
es2126plusPortSFPInfo = _Es2126plusPortSFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4)
)


class _Es2126plusPortSFPInfoNumber_Type(Integer32):
    """Custom type es2126plusPortSFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusPortSFPInfoNumber_Type.__name__ = "Integer32"
_Es2126plusPortSFPInfoNumber_Object = MibScalar
es2126plusPortSFPInfoNumber = _Es2126plusPortSFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 1),
    _Es2126plusPortSFPInfoNumber_Type()
)
es2126plusPortSFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPInfoNumber.setStatus("current")
_Es2126plusPortSFPInfoTable_Object = MibTable
es2126plusPortSFPInfoTable = _Es2126plusPortSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    es2126plusPortSFPInfoTable.setStatus("current")
_Es2126plusPortSFPInfoEntry_Object = MibTableRow
es2126plusPortSFPInfoEntry = _Es2126plusPortSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1)
)
es2126plusPortSFPInfoEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusPortSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    es2126plusPortSFPInfoEntry.setStatus("current")


class _Es2126plusPortSFPInfoIndex_Type(Integer32):
    """Custom type es2126plusPortSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusPortSFPInfoIndex_Type.__name__ = "Integer32"
_Es2126plusPortSFPInfoIndex_Object = MibTableColumn
es2126plusPortSFPInfoIndex = _Es2126plusPortSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 1),
    _Es2126plusPortSFPInfoIndex_Type()
)
es2126plusPortSFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPInfoIndex.setStatus("current")
_Es2126plusPortSFPConnectorType_Type = DisplayString
_Es2126plusPortSFPConnectorType_Object = MibTableColumn
es2126plusPortSFPConnectorType = _Es2126plusPortSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 2),
    _Es2126plusPortSFPConnectorType_Type()
)
es2126plusPortSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPConnectorType.setStatus("current")
_Es2126plusPortSFPFiberType_Type = DisplayString
_Es2126plusPortSFPFiberType_Object = MibTableColumn
es2126plusPortSFPFiberType = _Es2126plusPortSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 3),
    _Es2126plusPortSFPFiberType_Type()
)
es2126plusPortSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPFiberType.setStatus("current")
_Es2126plusPortSFPWavelength_Type = DisplayString
_Es2126plusPortSFPWavelength_Object = MibTableColumn
es2126plusPortSFPWavelength = _Es2126plusPortSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 4),
    _Es2126plusPortSFPWavelength_Type()
)
es2126plusPortSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPWavelength.setStatus("current")
_Es2126plusPortSFPBaudRate_Type = DisplayString
_Es2126plusPortSFPBaudRate_Object = MibTableColumn
es2126plusPortSFPBaudRate = _Es2126plusPortSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 5),
    _Es2126plusPortSFPBaudRate_Type()
)
es2126plusPortSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPBaudRate.setStatus("current")
_Es2126plusPortSFPVendorOUI_Type = DisplayString
_Es2126plusPortSFPVendorOUI_Object = MibTableColumn
es2126plusPortSFPVendorOUI = _Es2126plusPortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 6),
    _Es2126plusPortSFPVendorOUI_Type()
)
es2126plusPortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPVendorOUI.setStatus("current")
_Es2126plusPortSFPVendorName_Type = DisplayString
_Es2126plusPortSFPVendorName_Object = MibTableColumn
es2126plusPortSFPVendorName = _Es2126plusPortSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 7),
    _Es2126plusPortSFPVendorName_Type()
)
es2126plusPortSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPVendorName.setStatus("current")
_Es2126plusPortSFPVendorPN_Type = DisplayString
_Es2126plusPortSFPVendorPN_Object = MibTableColumn
es2126plusPortSFPVendorPN = _Es2126plusPortSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 8),
    _Es2126plusPortSFPVendorPN_Type()
)
es2126plusPortSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPVendorPN.setStatus("current")
_Es2126plusPortSFPVendorRev_Type = DisplayString
_Es2126plusPortSFPVendorRev_Object = MibTableColumn
es2126plusPortSFPVendorRev = _Es2126plusPortSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 9),
    _Es2126plusPortSFPVendorRev_Type()
)
es2126plusPortSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPVendorRev.setStatus("current")
_Es2126plusPortSFPVendorSN_Type = DisplayString
_Es2126plusPortSFPVendorSN_Object = MibTableColumn
es2126plusPortSFPVendorSN = _Es2126plusPortSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 10),
    _Es2126plusPortSFPVendorSN_Type()
)
es2126plusPortSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPVendorSN.setStatus("current")
_Es2126plusPortSFPDateCode_Type = DisplayString
_Es2126plusPortSFPDateCode_Object = MibTableColumn
es2126plusPortSFPDateCode = _Es2126plusPortSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 11),
    _Es2126plusPortSFPDateCode_Type()
)
es2126plusPortSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPDateCode.setStatus("current")
_Es2126plusPortSFPTemperature_Type = DisplayString
_Es2126plusPortSFPTemperature_Object = MibTableColumn
es2126plusPortSFPTemperature = _Es2126plusPortSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 12),
    _Es2126plusPortSFPTemperature_Type()
)
es2126plusPortSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPTemperature.setStatus("current")
_Es2126plusPortSFPVcc_Type = DisplayString
_Es2126plusPortSFPVcc_Object = MibTableColumn
es2126plusPortSFPVcc = _Es2126plusPortSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 13),
    _Es2126plusPortSFPVcc_Type()
)
es2126plusPortSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPVcc.setStatus("current")
_Es2126plusPortSFPTxBias_Type = DisplayString
_Es2126plusPortSFPTxBias_Object = MibTableColumn
es2126plusPortSFPTxBias = _Es2126plusPortSFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 14),
    _Es2126plusPortSFPTxBias_Type()
)
es2126plusPortSFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPTxBias.setStatus("current")
_Es2126plusPortSFPTxPWR_Type = DisplayString
_Es2126plusPortSFPTxPWR_Object = MibTableColumn
es2126plusPortSFPTxPWR = _Es2126plusPortSFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 15),
    _Es2126plusPortSFPTxPWR_Type()
)
es2126plusPortSFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPTxPWR.setStatus("current")
_Es2126plusPortSFPRxPWR_Type = DisplayString
_Es2126plusPortSFPRxPWR_Object = MibTableColumn
es2126plusPortSFPRxPWR = _Es2126plusPortSFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 9, 4, 2, 1, 16),
    _Es2126plusPortSFPRxPWR_Type()
)
es2126plusPortSFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortSFPRxPWR.setStatus("current")
_Es2126plusLoopDetectedConf_ObjectIdentity = ObjectIdentity
es2126plusLoopDetectedConf = _Es2126plusLoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10)
)


class _Es2126plusLoopDetectedNumber_Type(Integer32):
    """Custom type es2126plusLoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusLoopDetectedNumber_Type.__name__ = "Integer32"
_Es2126plusLoopDetectedNumber_Object = MibScalar
es2126plusLoopDetectedNumber = _Es2126plusLoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 1),
    _Es2126plusLoopDetectedNumber_Type()
)
es2126plusLoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusLoopDetectedNumber.setStatus("current")
_Es2126plusLoopDetectedTable_Object = MibTable
es2126plusLoopDetectedTable = _Es2126plusLoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 2)
)
if mibBuilder.loadTexts:
    es2126plusLoopDetectedTable.setStatus("current")
_Es2126plusLoopDetectedEntry_Object = MibTableRow
es2126plusLoopDetectedEntry = _Es2126plusLoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 2, 1)
)
es2126plusLoopDetectedEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusLoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    es2126plusLoopDetectedEntry.setStatus("current")


class _Es2126plusLoopDetectedfIndex_Type(Integer32):
    """Custom type es2126plusLoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126plusLoopDetectedfIndex_Type.__name__ = "Integer32"
_Es2126plusLoopDetectedfIndex_Object = MibTableColumn
es2126plusLoopDetectedfIndex = _Es2126plusLoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 2, 1, 1),
    _Es2126plusLoopDetectedfIndex_Type()
)
es2126plusLoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusLoopDetectedfIndex.setStatus("current")


class _Es2126plusLoopDetectedStateEbl_Type(Integer32):
    """Custom type es2126plusLoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusLoopDetectedStateEbl_Type.__name__ = "Integer32"
_Es2126plusLoopDetectedStateEbl_Object = MibTableColumn
es2126plusLoopDetectedStateEbl = _Es2126plusLoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 2, 1, 2),
    _Es2126plusLoopDetectedStateEbl_Type()
)
es2126plusLoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusLoopDetectedStateEbl.setStatus("current")


class _Es2126plusLoopDetectedCurrentStatus_Type(Integer32):
    """Custom type es2126plusLoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusLoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_Es2126plusLoopDetectedCurrentStatus_Object = MibTableColumn
es2126plusLoopDetectedCurrentStatus = _Es2126plusLoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 2, 1, 3),
    _Es2126plusLoopDetectedCurrentStatus_Type()
)
es2126plusLoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusLoopDetectedCurrentStatus.setStatus("current")


class _Es2126plusLoopDetectedRemoved_Type(Integer32):
    """Custom type es2126plusLoopDetectedRemoved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusLoopDetectedRemoved_Type.__name__ = "Integer32"
_Es2126plusLoopDetectedRemoved_Object = MibTableColumn
es2126plusLoopDetectedRemoved = _Es2126plusLoopDetectedRemoved_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 2, 1, 4),
    _Es2126plusLoopDetectedRemoved_Type()
)
es2126plusLoopDetectedRemoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusLoopDetectedRemoved.setStatus("current")


class _Es2126plusLoopDetectedAction_Type(Integer32):
    """Custom type es2126plusLoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusLoopDetectedAction_Type.__name__ = "Integer32"
_Es2126plusLoopDetectedAction_Object = MibScalar
es2126plusLoopDetectedAction = _Es2126plusLoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 10, 3),
    _Es2126plusLoopDetectedAction_Type()
)
es2126plusLoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusLoopDetectedAction.setStatus("current")
_Es2126plusMacTableInfo_ObjectIdentity = ObjectIdentity
es2126plusMacTableInfo = _Es2126plusMacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11)
)
_Es2126plusMacTableMaintenance_ObjectIdentity = ObjectIdentity
es2126plusMacTableMaintenance = _Es2126plusMacTableMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1)
)


class _Es2126plusMacTableAgingTime_Type(Integer32):
    """Custom type es2126plusMacTableAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_Es2126plusMacTableAgingTime_Type.__name__ = "Integer32"
_Es2126plusMacTableAgingTime_Object = MibScalar
es2126plusMacTableAgingTime = _Es2126plusMacTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1, 1),
    _Es2126plusMacTableAgingTime_Type()
)
es2126plusMacTableAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableAgingTime.setStatus("current")


class _Es2126plusMacTableFlush_Type(Integer32):
    """Custom type es2126plusMacTableFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusMacTableFlush_Type.__name__ = "Integer32"
_Es2126plusMacTableFlush_Object = MibScalar
es2126plusMacTableFlush = _Es2126plusMacTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1, 2),
    _Es2126plusMacTableFlush_Type()
)
es2126plusMacTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableFlush.setStatus("current")
_Es2126plusMacTableLearnPortLimitTable_Object = MibTable
es2126plusMacTableLearnPortLimitTable = _Es2126plusMacTableLearnPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    es2126plusMacTableLearnPortLimitTable.setStatus("current")
_Es2126plusMacTableLearnPortLimitEntry_Object = MibTableRow
es2126plusMacTableLearnPortLimitEntry = _Es2126plusMacTableLearnPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1, 3, 1)
)
es2126plusMacTableLearnPortLimitEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusMacTableLearnPortLimitIndex"),
)
if mibBuilder.loadTexts:
    es2126plusMacTableLearnPortLimitEntry.setStatus("current")


class _Es2126plusMacTableLearnPortLimitIndex_Type(Integer32):
    """Custom type es2126plusMacTableLearnPortLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusMacTableLearnPortLimitIndex_Type.__name__ = "Integer32"
_Es2126plusMacTableLearnPortLimitIndex_Object = MibTableColumn
es2126plusMacTableLearnPortLimitIndex = _Es2126plusMacTableLearnPortLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1, 3, 1, 1),
    _Es2126plusMacTableLearnPortLimitIndex_Type()
)
es2126plusMacTableLearnPortLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusMacTableLearnPortLimitIndex.setStatus("current")


class _Es2126plusMacTableLearnPortLimit_Type(Integer32):
    """Custom type es2126plusMacTableLearnPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_Es2126plusMacTableLearnPortLimit_Type.__name__ = "Integer32"
_Es2126plusMacTableLearnPortLimit_Object = MibTableColumn
es2126plusMacTableLearnPortLimit = _Es2126plusMacTableLearnPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 1, 3, 1, 2),
    _Es2126plusMacTableLearnPortLimit_Type()
)
es2126plusMacTableLearnPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableLearnPortLimit.setStatus("current")
_Es2126plusMacTableStaticMac_ObjectIdentity = ObjectIdentity
es2126plusMacTableStaticMac = _Es2126plusMacTableStaticMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3)
)


class _Es2126plusMacTableStaticMacNumber_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2126plusMacTableStaticMacNumber_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacNumber_Object = MibScalar
es2126plusMacTableStaticMacNumber = _Es2126plusMacTableStaticMacNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 1),
    _Es2126plusMacTableStaticMacNumber_Type()
)
es2126plusMacTableStaticMacNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacNumber.setStatus("current")


class _Es2126plusMacTableStaticMacEntryCreate_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2126plusMacTableStaticMacEntryCreate_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacEntryCreate_Object = MibScalar
es2126plusMacTableStaticMacEntryCreate = _Es2126plusMacTableStaticMacEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 2),
    _Es2126plusMacTableStaticMacEntryCreate_Type()
)
es2126plusMacTableStaticMacEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacEntryCreate.setStatus("current")
_Es2126plusMacTableStaticMacTable_Object = MibTable
es2126plusMacTableStaticMacTable = _Es2126plusMacTableStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacTable.setStatus("current")
_Es2126plusMacTableStaticMacEntry_Object = MibTableRow
es2126plusMacTableStaticMacEntry = _Es2126plusMacTableStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1)
)
es2126plusMacTableStaticMacEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusMacTableStaticMacIndex"),
)
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacEntry.setStatus("current")


class _Es2126plusMacTableStaticMacIndex_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2126plusMacTableStaticMacIndex_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacIndex_Object = MibTableColumn
es2126plusMacTableStaticMacIndex = _Es2126plusMacTableStaticMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 1),
    _Es2126plusMacTableStaticMacIndex_Type()
)
es2126plusMacTableStaticMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacIndex.setStatus("current")
_Es2126plusMacTableStaticMacAddress_Type = DisplayString
_Es2126plusMacTableStaticMacAddress_Object = MibTableColumn
es2126plusMacTableStaticMacAddress = _Es2126plusMacTableStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 2),
    _Es2126plusMacTableStaticMacAddress_Type()
)
es2126plusMacTableStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacAddress.setStatus("current")


class _Es2126plusMacTableStaticMacVid_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusMacTableStaticMacVid_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacVid_Object = MibTableColumn
es2126plusMacTableStaticMacVid = _Es2126plusMacTableStaticMacVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 3),
    _Es2126plusMacTableStaticMacVid_Type()
)
es2126plusMacTableStaticMacVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacVid.setStatus("current")


class _Es2126plusMacTableStaticMacQueue_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusMacTableStaticMacQueue_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacQueue_Object = MibTableColumn
es2126plusMacTableStaticMacQueue = _Es2126plusMacTableStaticMacQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 4),
    _Es2126plusMacTableStaticMacQueue_Type()
)
es2126plusMacTableStaticMacQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacQueue.setStatus("current")


class _Es2126plusMacTableStaticMacFwRule_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacFwRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusMacTableStaticMacFwRule_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacFwRule_Object = MibTableColumn
es2126plusMacTableStaticMacFwRule = _Es2126plusMacTableStaticMacFwRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 5),
    _Es2126plusMacTableStaticMacFwRule_Type()
)
es2126plusMacTableStaticMacFwRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacFwRule.setStatus("current")


class _Es2126plusMacTableStaticMacPort_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusMacTableStaticMacPort_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacPort_Object = MibTableColumn
es2126plusMacTableStaticMacPort = _Es2126plusMacTableStaticMacPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 6),
    _Es2126plusMacTableStaticMacPort_Type()
)
es2126plusMacTableStaticMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacPort.setStatus("current")


class _Es2126plusMacTableStaticMacEntryAction_Type(Integer32):
    """Custom type es2126plusMacTableStaticMacEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126plusMacTableStaticMacEntryAction_Type.__name__ = "Integer32"
_Es2126plusMacTableStaticMacEntryAction_Object = MibTableColumn
es2126plusMacTableStaticMacEntryAction = _Es2126plusMacTableStaticMacEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 3, 3, 1, 7),
    _Es2126plusMacTableStaticMacEntryAction_Type()
)
es2126plusMacTableStaticMacEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableStaticMacEntryAction.setStatus("current")
_Es2126plusMacTableMacAlias_ObjectIdentity = ObjectIdentity
es2126plusMacTableMacAlias = _Es2126plusMacTableMacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4)
)


class _Es2126plusMacTableMacAliasNumber_Type(Integer32):
    """Custom type es2126plusMacTableMacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_Es2126plusMacTableMacAliasNumber_Type.__name__ = "Integer32"
_Es2126plusMacTableMacAliasNumber_Object = MibScalar
es2126plusMacTableMacAliasNumber = _Es2126plusMacTableMacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 1),
    _Es2126plusMacTableMacAliasNumber_Type()
)
es2126plusMacTableMacAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasNumber.setStatus("current")


class _Es2126plusMacTableMacAliasEntryCreate_Type(Integer32):
    """Custom type es2126plusMacTableMacAliasEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_Es2126plusMacTableMacAliasEntryCreate_Type.__name__ = "Integer32"
_Es2126plusMacTableMacAliasEntryCreate_Object = MibScalar
es2126plusMacTableMacAliasEntryCreate = _Es2126plusMacTableMacAliasEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 2),
    _Es2126plusMacTableMacAliasEntryCreate_Type()
)
es2126plusMacTableMacAliasEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasEntryCreate.setStatus("current")
_Es2126plusMacTableMacAliasTable_Object = MibTable
es2126plusMacTableMacAliasTable = _Es2126plusMacTableMacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 3)
)
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasTable.setStatus("current")
_Es2126plusMacTableMacAliasEntry_Object = MibTableRow
es2126plusMacTableMacAliasEntry = _Es2126plusMacTableMacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 3, 1)
)
es2126plusMacTableMacAliasEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusMacTableMacAliasIndex"),
)
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasEntry.setStatus("current")


class _Es2126plusMacTableMacAliasIndex_Type(Integer32):
    """Custom type es2126plusMacTableMacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2126plusMacTableMacAliasIndex_Type.__name__ = "Integer32"
_Es2126plusMacTableMacAliasIndex_Object = MibTableColumn
es2126plusMacTableMacAliasIndex = _Es2126plusMacTableMacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 3, 1, 1),
    _Es2126plusMacTableMacAliasIndex_Type()
)
es2126plusMacTableMacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasIndex.setStatus("current")
_Es2126plusMacTableMacAliasAddress_Type = DisplayString
_Es2126plusMacTableMacAliasAddress_Object = MibTableColumn
es2126plusMacTableMacAliasAddress = _Es2126plusMacTableMacAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 3, 1, 2),
    _Es2126plusMacTableMacAliasAddress_Type()
)
es2126plusMacTableMacAliasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasAddress.setStatus("current")
_Es2126plusMacTableMacAliasAlias_Type = DisplayString
_Es2126plusMacTableMacAliasAlias_Object = MibTableColumn
es2126plusMacTableMacAliasAlias = _Es2126plusMacTableMacAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 3, 1, 3),
    _Es2126plusMacTableMacAliasAlias_Type()
)
es2126plusMacTableMacAliasAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasAlias.setStatus("current")


class _Es2126plusMacTableMacAliasEntryAction_Type(Integer32):
    """Custom type es2126plusMacTableMacAliasEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126plusMacTableMacAliasEntryAction_Type.__name__ = "Integer32"
_Es2126plusMacTableMacAliasEntryAction_Object = MibTableColumn
es2126plusMacTableMacAliasEntryAction = _Es2126plusMacTableMacAliasEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 11, 4, 3, 1, 4),
    _Es2126plusMacTableMacAliasEntryAction_Type()
)
es2126plusMacTableMacAliasEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMacTableMacAliasEntryAction.setStatus("current")
_Es2126plusGVRPInfo_ObjectIdentity = ObjectIdentity
es2126plusGVRPInfo = _Es2126plusGVRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12)
)
_Es2126plusGvrpConf_ObjectIdentity = ObjectIdentity
es2126plusGvrpConf = _Es2126plusGvrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1)
)


class _Es2126plusGvrpConfState_Type(Integer32):
    """Custom type es2126plusGvrpConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusGvrpConfState_Type.__name__ = "Integer32"
_Es2126plusGvrpConfState_Object = MibScalar
es2126plusGvrpConfState = _Es2126plusGvrpConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 1),
    _Es2126plusGvrpConfState_Type()
)
es2126plusGvrpConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfState.setStatus("current")
_Es2126plusGvrpConfTable_Object = MibTable
es2126plusGvrpConfTable = _Es2126plusGvrpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    es2126plusGvrpConfTable.setStatus("current")
_Es2126plusGvrpConfEntry_Object = MibTableRow
es2126plusGvrpConfEntry = _Es2126plusGvrpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1)
)
es2126plusGvrpConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusGvrpConfIndex"),
)
if mibBuilder.loadTexts:
    es2126plusGvrpConfEntry.setStatus("current")


class _Es2126plusGvrpConfIndex_Type(Integer32):
    """Custom type es2126plusGvrpConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusGvrpConfIndex_Type.__name__ = "Integer32"
_Es2126plusGvrpConfIndex_Object = MibTableColumn
es2126plusGvrpConfIndex = _Es2126plusGvrpConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 1),
    _Es2126plusGvrpConfIndex_Type()
)
es2126plusGvrpConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusGvrpConfIndex.setStatus("current")


class _Es2126plusGvrpConfJoinTime_Type(Integer32):
    """Custom type es2126plusGvrpConfJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Es2126plusGvrpConfJoinTime_Type.__name__ = "Integer32"
_Es2126plusGvrpConfJoinTime_Object = MibTableColumn
es2126plusGvrpConfJoinTime = _Es2126plusGvrpConfJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 2),
    _Es2126plusGvrpConfJoinTime_Type()
)
es2126plusGvrpConfJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfJoinTime.setStatus("current")


class _Es2126plusGvrpConfLeaveTime_Type(Integer32):
    """Custom type es2126plusGvrpConfLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Es2126plusGvrpConfLeaveTime_Type.__name__ = "Integer32"
_Es2126plusGvrpConfLeaveTime_Object = MibTableColumn
es2126plusGvrpConfLeaveTime = _Es2126plusGvrpConfLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 3),
    _Es2126plusGvrpConfLeaveTime_Type()
)
es2126plusGvrpConfLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfLeaveTime.setStatus("current")


class _Es2126plusGvrpConfLeaveAllTime_Type(Integer32):
    """Custom type es2126plusGvrpConfLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_Es2126plusGvrpConfLeaveAllTime_Type.__name__ = "Integer32"
_Es2126plusGvrpConfLeaveAllTime_Object = MibTableColumn
es2126plusGvrpConfLeaveAllTime = _Es2126plusGvrpConfLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 4),
    _Es2126plusGvrpConfLeaveAllTime_Type()
)
es2126plusGvrpConfLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfLeaveAllTime.setStatus("current")


class _Es2126plusGvrpConfDefaultAppMode_Type(Integer32):
    """Custom type es2126plusGvrpConfDefaultAppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusGvrpConfDefaultAppMode_Type.__name__ = "Integer32"
_Es2126plusGvrpConfDefaultAppMode_Object = MibTableColumn
es2126plusGvrpConfDefaultAppMode = _Es2126plusGvrpConfDefaultAppMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 5),
    _Es2126plusGvrpConfDefaultAppMode_Type()
)
es2126plusGvrpConfDefaultAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfDefaultAppMode.setStatus("current")


class _Es2126plusGvrpConfDefaultRegMode_Type(Integer32):
    """Custom type es2126plusGvrpConfDefaultRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126plusGvrpConfDefaultRegMode_Type.__name__ = "Integer32"
_Es2126plusGvrpConfDefaultRegMode_Object = MibTableColumn
es2126plusGvrpConfDefaultRegMode = _Es2126plusGvrpConfDefaultRegMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 6),
    _Es2126plusGvrpConfDefaultRegMode_Type()
)
es2126plusGvrpConfDefaultRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfDefaultRegMode.setStatus("current")


class _Es2126plusGvrpConfRestrictedMode_Type(Integer32):
    """Custom type es2126plusGvrpConfRestrictedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusGvrpConfRestrictedMode_Type.__name__ = "Integer32"
_Es2126plusGvrpConfRestrictedMode_Object = MibTableColumn
es2126plusGvrpConfRestrictedMode = _Es2126plusGvrpConfRestrictedMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 1, 2, 1, 7),
    _Es2126plusGvrpConfRestrictedMode_Type()
)
es2126plusGvrpConfRestrictedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusGvrpConfRestrictedMode.setStatus("current")
_Es2126plusGvrpCounter_ObjectIdentity = ObjectIdentity
es2126plusGvrpCounter = _Es2126plusGvrpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2)
)
_Es2126plusGvrpCounterTable_Object = MibTable
es2126plusGvrpCounterTable = _Es2126plusGvrpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTable.setStatus("current")
_Es2126plusGvrpCounterEntry_Object = MibTableRow
es2126plusGvrpCounterEntry = _Es2126plusGvrpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1)
)
es2126plusGvrpCounterEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusGvrpCounterIndex"),
)
if mibBuilder.loadTexts:
    es2126plusGvrpCounterEntry.setStatus("current")


class _Es2126plusGvrpCounterIndex_Type(Integer32):
    """Custom type es2126plusGvrpCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusGvrpCounterIndex_Type.__name__ = "Integer32"
_Es2126plusGvrpCounterIndex_Object = MibTableColumn
es2126plusGvrpCounterIndex = _Es2126plusGvrpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 1),
    _Es2126plusGvrpCounterIndex_Type()
)
es2126plusGvrpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterIndex.setStatus("current")
_Es2126plusGvrpCounterRxTotalGvrpPkts_Type = Counter32
_Es2126plusGvrpCounterRxTotalGvrpPkts_Object = MibTableColumn
es2126plusGvrpCounterRxTotalGvrpPkts = _Es2126plusGvrpCounterRxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 2),
    _Es2126plusGvrpCounterRxTotalGvrpPkts_Type()
)
es2126plusGvrpCounterRxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxTotalGvrpPkts.setStatus("current")
_Es2126plusGvrpCounterRxInvalidGvrpPkts_Type = Counter32
_Es2126plusGvrpCounterRxInvalidGvrpPkts_Object = MibTableColumn
es2126plusGvrpCounterRxInvalidGvrpPkts = _Es2126plusGvrpCounterRxInvalidGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 3),
    _Es2126plusGvrpCounterRxInvalidGvrpPkts_Type()
)
es2126plusGvrpCounterRxInvalidGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxInvalidGvrpPkts.setStatus("current")
_Es2126plusGvrpCounterRxLeaveAllMsg_Type = Counter32
_Es2126plusGvrpCounterRxLeaveAllMsg_Object = MibTableColumn
es2126plusGvrpCounterRxLeaveAllMsg = _Es2126plusGvrpCounterRxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 4),
    _Es2126plusGvrpCounterRxLeaveAllMsg_Type()
)
es2126plusGvrpCounterRxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxLeaveAllMsg.setStatus("current")
_Es2126plusGvrpCounterRxJoinEmptyMsg_Type = Counter32
_Es2126plusGvrpCounterRxJoinEmptyMsg_Object = MibTableColumn
es2126plusGvrpCounterRxJoinEmptyMsg = _Es2126plusGvrpCounterRxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 5),
    _Es2126plusGvrpCounterRxJoinEmptyMsg_Type()
)
es2126plusGvrpCounterRxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxJoinEmptyMsg.setStatus("current")
_Es2126plusGvrpCounterRxJoinInMsg_Type = Counter32
_Es2126plusGvrpCounterRxJoinInMsg_Object = MibTableColumn
es2126plusGvrpCounterRxJoinInMsg = _Es2126plusGvrpCounterRxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 6),
    _Es2126plusGvrpCounterRxJoinInMsg_Type()
)
es2126plusGvrpCounterRxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxJoinInMsg.setStatus("current")
_Es2126plusGvrpCounterRxLeaveEmptyMsg_Type = Counter32
_Es2126plusGvrpCounterRxLeaveEmptyMsg_Object = MibTableColumn
es2126plusGvrpCounterRxLeaveEmptyMsg = _Es2126plusGvrpCounterRxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 7),
    _Es2126plusGvrpCounterRxLeaveEmptyMsg_Type()
)
es2126plusGvrpCounterRxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxLeaveEmptyMsg.setStatus("current")
_Es2126plusGvrpCounterRxEmptyMsg_Type = Counter32
_Es2126plusGvrpCounterRxEmptyMsg_Object = MibTableColumn
es2126plusGvrpCounterRxEmptyMsg = _Es2126plusGvrpCounterRxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 8),
    _Es2126plusGvrpCounterRxEmptyMsg_Type()
)
es2126plusGvrpCounterRxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterRxEmptyMsg.setStatus("current")
_Es2126plusGvrpCounterTxTotalGvrpPkts_Type = Counter32
_Es2126plusGvrpCounterTxTotalGvrpPkts_Object = MibTableColumn
es2126plusGvrpCounterTxTotalGvrpPkts = _Es2126plusGvrpCounterTxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 9),
    _Es2126plusGvrpCounterTxTotalGvrpPkts_Type()
)
es2126plusGvrpCounterTxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTxTotalGvrpPkts.setStatus("current")
_Es2126plusGvrpCounterTxLeaveAllMsg_Type = Counter32
_Es2126plusGvrpCounterTxLeaveAllMsg_Object = MibTableColumn
es2126plusGvrpCounterTxLeaveAllMsg = _Es2126plusGvrpCounterTxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 10),
    _Es2126plusGvrpCounterTxLeaveAllMsg_Type()
)
es2126plusGvrpCounterTxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTxLeaveAllMsg.setStatus("current")
_Es2126plusGvrpCounterTxJoinEmptyMsg_Type = Counter32
_Es2126plusGvrpCounterTxJoinEmptyMsg_Object = MibTableColumn
es2126plusGvrpCounterTxJoinEmptyMsg = _Es2126plusGvrpCounterTxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 11),
    _Es2126plusGvrpCounterTxJoinEmptyMsg_Type()
)
es2126plusGvrpCounterTxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTxJoinEmptyMsg.setStatus("current")
_Es2126plusGvrpCounterTxJoinInMsg_Type = Counter32
_Es2126plusGvrpCounterTxJoinInMsg_Object = MibTableColumn
es2126plusGvrpCounterTxJoinInMsg = _Es2126plusGvrpCounterTxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 12),
    _Es2126plusGvrpCounterTxJoinInMsg_Type()
)
es2126plusGvrpCounterTxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTxJoinInMsg.setStatus("current")
_Es2126plusGvrpCounterTxLeaveEmptyMsg_Type = Counter32
_Es2126plusGvrpCounterTxLeaveEmptyMsg_Object = MibTableColumn
es2126plusGvrpCounterTxLeaveEmptyMsg = _Es2126plusGvrpCounterTxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 13),
    _Es2126plusGvrpCounterTxLeaveEmptyMsg_Type()
)
es2126plusGvrpCounterTxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTxLeaveEmptyMsg.setStatus("current")
_Es2126plusGvrpCounterTxEmptyMsg_Type = Counter32
_Es2126plusGvrpCounterTxEmptyMsg_Object = MibTableColumn
es2126plusGvrpCounterTxEmptyMsg = _Es2126plusGvrpCounterTxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 2, 1, 1, 14),
    _Es2126plusGvrpCounterTxEmptyMsg_Type()
)
es2126plusGvrpCounterTxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpCounterTxEmptyMsg.setStatus("current")
_Es2126plusGvrpGroup_ObjectIdentity = ObjectIdentity
es2126plusGvrpGroup = _Es2126plusGvrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3)
)


class _Es2126plusGvrpGroupNumber_Type(Integer32):
    """Custom type es2126plusGvrpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126plusGvrpGroupNumber_Type.__name__ = "Integer32"
_Es2126plusGvrpGroupNumber_Object = MibScalar
es2126plusGvrpGroupNumber = _Es2126plusGvrpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3, 1),
    _Es2126plusGvrpGroupNumber_Type()
)
es2126plusGvrpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpGroupNumber.setStatus("current")
_Es2126plusGvrpGroupTable_Object = MibTable
es2126plusGvrpGroupTable = _Es2126plusGvrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    es2126plusGvrpGroupTable.setStatus("current")
_Es2126plusGvrpGroupEntry_Object = MibTableRow
es2126plusGvrpGroupEntry = _Es2126plusGvrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3, 2, 1)
)
es2126plusGvrpGroupEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusGvrpGroupId"),
)
if mibBuilder.loadTexts:
    es2126plusGvrpGroupEntry.setStatus("current")


class _Es2126plusGvrpGroupId_Type(Integer32):
    """Custom type es2126plusGvrpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusGvrpGroupId_Type.__name__ = "Integer32"
_Es2126plusGvrpGroupId_Object = MibTableColumn
es2126plusGvrpGroupId = _Es2126plusGvrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3, 2, 1, 1),
    _Es2126plusGvrpGroupId_Type()
)
es2126plusGvrpGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpGroupId.setStatus("current")


class _Es2126plusGvrpGroupVid_Type(Integer32):
    """Custom type es2126plusGvrpGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusGvrpGroupVid_Type.__name__ = "Integer32"
_Es2126plusGvrpGroupVid_Object = MibTableColumn
es2126plusGvrpGroupVid = _Es2126plusGvrpGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3, 2, 1, 2),
    _Es2126plusGvrpGroupVid_Type()
)
es2126plusGvrpGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpGroupVid.setStatus("current")
_Es2126plusGvrpGroupMemberPort_Type = DisplayString
_Es2126plusGvrpGroupMemberPort_Object = MibTableColumn
es2126plusGvrpGroupMemberPort = _Es2126plusGvrpGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 12, 3, 2, 1, 3),
    _Es2126plusGvrpGroupMemberPort_Type()
)
es2126plusGvrpGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusGvrpGroupMemberPort.setStatus("current")
_Es2126plusSecurity_ObjectIdentity = ObjectIdentity
es2126plusSecurity = _Es2126plusSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13)
)
_Es2126plusIsolatedPortGroup_Type = DisplayString
_Es2126plusIsolatedPortGroup_Object = MibScalar
es2126plusIsolatedPortGroup = _Es2126plusIsolatedPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 1),
    _Es2126plusIsolatedPortGroup_Type()
)
es2126plusIsolatedPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusIsolatedPortGroup.setStatus("current")
_Es2126plusMirror_ObjectIdentity = ObjectIdentity
es2126plusMirror = _Es2126plusMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 2)
)


class _Es2126plusMirrorMode_Type(Integer32):
    """Custom type es2126plusMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusMirrorMode_Type.__name__ = "Integer32"
_Es2126plusMirrorMode_Object = MibScalar
es2126plusMirrorMode = _Es2126plusMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 2, 1),
    _Es2126plusMirrorMode_Type()
)
es2126plusMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMirrorMode.setStatus("current")


class _Es2126plusMonitoringPort_Type(Integer32):
    """Custom type es2126plusMonitoringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusMonitoringPort_Type.__name__ = "Integer32"
_Es2126plusMonitoringPort_Object = MibScalar
es2126plusMonitoringPort = _Es2126plusMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 2, 2),
    _Es2126plusMonitoringPort_Type()
)
es2126plusMonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMonitoringPort.setStatus("current")
_Es2126plusMonitoredIngressPort_Type = DisplayString
_Es2126plusMonitoredIngressPort_Object = MibScalar
es2126plusMonitoredIngressPort = _Es2126plusMonitoredIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 2, 3),
    _Es2126plusMonitoredIngressPort_Type()
)
es2126plusMonitoredIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMonitoredIngressPort.setStatus("current")
_Es2126plusMonitoredEgressPort_Type = DisplayString
_Es2126plusMonitoredEgressPort_Object = MibScalar
es2126plusMonitoredEgressPort = _Es2126plusMonitoredEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 2, 4),
    _Es2126plusMonitoredEgressPort_Type()
)
es2126plusMonitoredEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusMonitoredEgressPort.setStatus("current")
_Es2126plusRestrictedGroup_ObjectIdentity = ObjectIdentity
es2126plusRestrictedGroup = _Es2126plusRestrictedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 3)
)
_Es2126plusRestrictedGroupIngress_Type = DisplayString
_Es2126plusRestrictedGroupIngress_Object = MibScalar
es2126plusRestrictedGroupIngress = _Es2126plusRestrictedGroupIngress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 3, 1),
    _Es2126plusRestrictedGroupIngress_Type()
)
es2126plusRestrictedGroupIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusRestrictedGroupIngress.setStatus("current")
_Es2126plusRestrictedGroupEgress_Type = DisplayString
_Es2126plusRestrictedGroupEgress_Object = MibScalar
es2126plusRestrictedGroupEgress = _Es2126plusRestrictedGroupEgress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 13, 3, 2),
    _Es2126plusRestrictedGroupEgress_Type()
)
es2126plusRestrictedGroupEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusRestrictedGroupEgress.setStatus("current")
_Es2126plusVirtualStack_ObjectIdentity = ObjectIdentity
es2126plusVirtualStack = _Es2126plusVirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 14)
)


class _Es2126plusVirtualStackState_Type(Integer32):
    """Custom type es2126plusVirtualStackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusVirtualStackState_Type.__name__ = "Integer32"
_Es2126plusVirtualStackState_Object = MibScalar
es2126plusVirtualStackState = _Es2126plusVirtualStackState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 14, 1),
    _Es2126plusVirtualStackState_Type()
)
es2126plusVirtualStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVirtualStackState.setStatus("current")


class _Es2126plusVirtualStackRole_Type(Integer32):
    """Custom type es2126plusVirtualStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusVirtualStackRole_Type.__name__ = "Integer32"
_Es2126plusVirtualStackRole_Object = MibScalar
es2126plusVirtualStackRole = _Es2126plusVirtualStackRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 14, 2),
    _Es2126plusVirtualStackRole_Type()
)
es2126plusVirtualStackRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVirtualStackRole.setStatus("current")
_Es2126plusVirtualStackGroupID_Type = DisplayString
_Es2126plusVirtualStackGroupID_Object = MibScalar
es2126plusVirtualStackGroupID = _Es2126plusVirtualStackGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 14, 3),
    _Es2126plusVirtualStackGroupID_Type()
)
es2126plusVirtualStackGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVirtualStackGroupID.setStatus("current")
_Es2126plusManagementSecurity_ObjectIdentity = ObjectIdentity
es2126plusManagementSecurity = _Es2126plusManagementSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15)
)


class _Es2126plusManagementSecurityNumber_Type(Integer32):
    """Custom type es2126plusManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2126plusManagementSecurityNumber_Type.__name__ = "Integer32"
_Es2126plusManagementSecurityNumber_Object = MibScalar
es2126plusManagementSecurityNumber = _Es2126plusManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 1),
    _Es2126plusManagementSecurityNumber_Type()
)
es2126plusManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityNumber.setStatus("current")


class _Es2126plusManagementSecurityEntryCreate_Type(Integer32):
    """Custom type es2126plusManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2126plusManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Es2126plusManagementSecurityEntryCreate_Object = MibScalar
es2126plusManagementSecurityEntryCreate = _Es2126plusManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 2),
    _Es2126plusManagementSecurityEntryCreate_Type()
)
es2126plusManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityEntryCreate.setStatus("current")
_Es2126plusManagementSecurityTable_Object = MibTable
es2126plusManagementSecurityTable = _Es2126plusManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3)
)
if mibBuilder.loadTexts:
    es2126plusManagementSecurityTable.setStatus("current")
_Es2126plusManagementSecurityEntry_Object = MibTableRow
es2126plusManagementSecurityEntry = _Es2126plusManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1)
)
es2126plusManagementSecurityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusManagementSecurityEntry.setStatus("current")


class _Es2126plusManagementSecurityIndex_Type(Integer32):
    """Custom type es2126plusManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2126plusManagementSecurityIndex_Type.__name__ = "Integer32"
_Es2126plusManagementSecurityIndex_Object = MibTableColumn
es2126plusManagementSecurityIndex = _Es2126plusManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 1),
    _Es2126plusManagementSecurityIndex_Type()
)
es2126plusManagementSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityIndex.setStatus("current")
_Es2126plusManagementSecurityName_Type = DisplayString
_Es2126plusManagementSecurityName_Object = MibTableColumn
es2126plusManagementSecurityName = _Es2126plusManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 2),
    _Es2126plusManagementSecurityName_Type()
)
es2126plusManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityName.setStatus("current")


class _Es2126plusManagementSecurityVid_Type(Integer32):
    """Custom type es2126plusManagementSecurityVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126plusManagementSecurityVid_Type.__name__ = "Integer32"
_Es2126plusManagementSecurityVid_Object = MibTableColumn
es2126plusManagementSecurityVid = _Es2126plusManagementSecurityVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 3),
    _Es2126plusManagementSecurityVid_Type()
)
es2126plusManagementSecurityVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityVid.setStatus("current")
_Es2126plusManagementSecurityIpRange_Type = DisplayString
_Es2126plusManagementSecurityIpRange_Object = MibTableColumn
es2126plusManagementSecurityIpRange = _Es2126plusManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 4),
    _Es2126plusManagementSecurityIpRange_Type()
)
es2126plusManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityIpRange.setStatus("current")
_Es2126plusManagementSecurityIncomigPort_Type = DisplayString
_Es2126plusManagementSecurityIncomigPort_Object = MibTableColumn
es2126plusManagementSecurityIncomigPort = _Es2126plusManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 5),
    _Es2126plusManagementSecurityIncomigPort_Type()
)
es2126plusManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityIncomigPort.setStatus("current")
_Es2126plusManagementSecurityAccessType_Type = DisplayString
_Es2126plusManagementSecurityAccessType_Object = MibTableColumn
es2126plusManagementSecurityAccessType = _Es2126plusManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 6),
    _Es2126plusManagementSecurityAccessType_Type()
)
es2126plusManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityAccessType.setStatus("current")


class _Es2126plusManagementSecurityAction_Type(Integer32):
    """Custom type es2126plusManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusManagementSecurityAction_Type.__name__ = "Integer32"
_Es2126plusManagementSecurityAction_Object = MibTableColumn
es2126plusManagementSecurityAction = _Es2126plusManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 7),
    _Es2126plusManagementSecurityAction_Type()
)
es2126plusManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityAction.setStatus("current")


class _Es2126plusManagementSecurityEntryAction_Type(Integer32):
    """Custom type es2126plusManagementSecurityEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusManagementSecurityEntryAction_Type.__name__ = "Integer32"
_Es2126plusManagementSecurityEntryAction_Object = MibTableColumn
es2126plusManagementSecurityEntryAction = _Es2126plusManagementSecurityEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 15, 3, 1, 8),
    _Es2126plusManagementSecurityEntryAction_Type()
)
es2126plusManagementSecurityEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementSecurityEntryAction.setStatus("current")
_Es2126plusQoS_ObjectIdentity = ObjectIdentity
es2126plusQoS = _Es2126plusQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16)
)
_Es2126plusQoSGlobalConfig_ObjectIdentity = ObjectIdentity
es2126plusQoSGlobalConfig = _Es2126plusQoSGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1)
)


class _Es2126plusQoSMode_Type(Integer32):
    """Custom type es2126plusQoSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusQoSMode_Type.__name__ = "Integer32"
_Es2126plusQoSMode_Object = MibScalar
es2126plusQoSMode = _Es2126plusQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 1),
    _Es2126plusQoSMode_Type()
)
es2126plusQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSMode.setStatus("current")


class _Es2126plusQosPriorityControl1p_Type(Integer32):
    """Custom type es2126plusQosPriorityControl1p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusQosPriorityControl1p_Type.__name__ = "Integer32"
_Es2126plusQosPriorityControl1p_Object = MibScalar
es2126plusQosPriorityControl1p = _Es2126plusQosPriorityControl1p_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 2),
    _Es2126plusQosPriorityControl1p_Type()
)
es2126plusQosPriorityControl1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQosPriorityControl1p.setStatus("current")


class _Es2126plusQosPriorityControlTOS_Type(Integer32):
    """Custom type es2126plusQosPriorityControlTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusQosPriorityControlTOS_Type.__name__ = "Integer32"
_Es2126plusQosPriorityControlTOS_Object = MibScalar
es2126plusQosPriorityControlTOS = _Es2126plusQosPriorityControlTOS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 3),
    _Es2126plusQosPriorityControlTOS_Type()
)
es2126plusQosPriorityControlTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQosPriorityControlTOS.setStatus("current")


class _Es2126plusQosPriorityControlDSCP_Type(Integer32):
    """Custom type es2126plusQosPriorityControlDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusQosPriorityControlDSCP_Type.__name__ = "Integer32"
_Es2126plusQosPriorityControlDSCP_Object = MibScalar
es2126plusQosPriorityControlDSCP = _Es2126plusQosPriorityControlDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 4),
    _Es2126plusQosPriorityControlDSCP_Type()
)
es2126plusQosPriorityControlDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQosPriorityControlDSCP.setStatus("current")


class _Es2126plusQoSSchedulingMethod_Type(Integer32):
    """Custom type es2126plusQoSSchedulingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusQoSSchedulingMethod_Type.__name__ = "Integer32"
_Es2126plusQoSSchedulingMethod_Object = MibScalar
es2126plusQoSSchedulingMethod = _Es2126plusQoSSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 5),
    _Es2126plusQoSSchedulingMethod_Type()
)
es2126plusQoSSchedulingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSSchedulingMethod.setStatus("current")


class _Es2126plusQoSWeightQ0_Type(Integer32):
    """Custom type es2126plusQoSWeightQ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126plusQoSWeightQ0_Type.__name__ = "Integer32"
_Es2126plusQoSWeightQ0_Object = MibScalar
es2126plusQoSWeightQ0 = _Es2126plusQoSWeightQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 6),
    _Es2126plusQoSWeightQ0_Type()
)
es2126plusQoSWeightQ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSWeightQ0.setStatus("current")


class _Es2126plusQoSWeightQ1_Type(Integer32):
    """Custom type es2126plusQoSWeightQ1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126plusQoSWeightQ1_Type.__name__ = "Integer32"
_Es2126plusQoSWeightQ1_Object = MibScalar
es2126plusQoSWeightQ1 = _Es2126plusQoSWeightQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 7),
    _Es2126plusQoSWeightQ1_Type()
)
es2126plusQoSWeightQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSWeightQ1.setStatus("current")


class _Es2126plusQoSWeightQ2_Type(Integer32):
    """Custom type es2126plusQoSWeightQ2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126plusQoSWeightQ2_Type.__name__ = "Integer32"
_Es2126plusQoSWeightQ2_Object = MibScalar
es2126plusQoSWeightQ2 = _Es2126plusQoSWeightQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 8),
    _Es2126plusQoSWeightQ2_Type()
)
es2126plusQoSWeightQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSWeightQ2.setStatus("current")


class _Es2126plusQoSWeightQ3_Type(Integer32):
    """Custom type es2126plusQoSWeightQ3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126plusQoSWeightQ3_Type.__name__ = "Integer32"
_Es2126plusQoSWeightQ3_Object = MibScalar
es2126plusQoSWeightQ3 = _Es2126plusQoSWeightQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 1, 9),
    _Es2126plusQoSWeightQ3_Type()
)
es2126plusQoSWeightQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSWeightQ3.setStatus("current")
_Es2126plusQoSVIPPort_Type = DisplayString
_Es2126plusQoSVIPPort_Object = MibScalar
es2126plusQoSVIPPort = _Es2126plusQoSVIPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 2),
    _Es2126plusQoSVIPPort_Type()
)
es2126plusQoSVIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSVIPPort.setStatus("current")
_Es2126plusQoS1pPriority_ObjectIdentity = ObjectIdentity
es2126plusQoS1pPriority = _Es2126plusQoS1pPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 3)
)
_Es2126plusQoS1pPriorityTable_Object = MibTable
es2126plusQoS1pPriorityTable = _Es2126plusQoS1pPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    es2126plusQoS1pPriorityTable.setStatus("current")
_Es2126plusQoS1pPriorityEntry_Object = MibTableRow
es2126plusQoS1pPriorityEntry = _Es2126plusQoS1pPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 3, 1, 1)
)
es2126plusQoS1pPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusQoS1pPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusQoS1pPriorityEntry.setStatus("current")


class _Es2126plusQoS1pPriorityIndex_Type(Integer32):
    """Custom type es2126plusQoS1pPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126plusQoS1pPriorityIndex_Type.__name__ = "Integer32"
_Es2126plusQoS1pPriorityIndex_Object = MibTableColumn
es2126plusQoS1pPriorityIndex = _Es2126plusQoS1pPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 3, 1, 1, 1),
    _Es2126plusQoS1pPriorityIndex_Type()
)
es2126plusQoS1pPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusQoS1pPriorityIndex.setStatus("current")


class _Es2126plusQoS1pPriorityValue_Type(Integer32):
    """Custom type es2126plusQoS1pPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusQoS1pPriorityValue_Type.__name__ = "Integer32"
_Es2126plusQoS1pPriorityValue_Object = MibTableColumn
es2126plusQoS1pPriorityValue = _Es2126plusQoS1pPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 3, 1, 1, 2),
    _Es2126plusQoS1pPriorityValue_Type()
)
es2126plusQoS1pPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusQoS1pPriorityValue.setStatus("current")


class _Es2126plusQoS1pPriorityQueue_Type(Integer32):
    """Custom type es2126plusQoS1pPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusQoS1pPriorityQueue_Type.__name__ = "Integer32"
_Es2126plusQoS1pPriorityQueue_Object = MibTableColumn
es2126plusQoS1pPriorityQueue = _Es2126plusQoS1pPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 3, 1, 1, 3),
    _Es2126plusQoS1pPriorityQueue_Type()
)
es2126plusQoS1pPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoS1pPriorityQueue.setStatus("current")
_Es2126plusQoSDTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126plusQoSDTypeTOSPriority = _Es2126plusQoSDTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 4)
)
_Es2126plusQoSDTypeTOSPriorityTable_Object = MibTable
es2126plusQoSDTypeTOSPriorityTable = _Es2126plusQoSDTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    es2126plusQoSDTypeTOSPriorityTable.setStatus("current")
_Es2126plusQoSDTypeTOSPriorityEntry_Object = MibTableRow
es2126plusQoSDTypeTOSPriorityEntry = _Es2126plusQoSDTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 4, 1, 1)
)
es2126plusQoSDTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusQoSDTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusQoSDTypeTOSPriorityEntry.setStatus("current")


class _Es2126plusQoSDTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126plusQoSDTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126plusQoSDTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126plusQoSDTypeTOSPriorityIndex_Object = MibTableColumn
es2126plusQoSDTypeTOSPriorityIndex = _Es2126plusQoSDTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 4, 1, 1, 1),
    _Es2126plusQoSDTypeTOSPriorityIndex_Type()
)
es2126plusQoSDTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusQoSDTypeTOSPriorityIndex.setStatus("current")


class _Es2126plusQoSDTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126plusQoSDTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusQoSDTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126plusQoSDTypeTOSPriorityValue_Object = MibTableColumn
es2126plusQoSDTypeTOSPriorityValue = _Es2126plusQoSDTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 4, 1, 1, 2),
    _Es2126plusQoSDTypeTOSPriorityValue_Type()
)
es2126plusQoSDTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusQoSDTypeTOSPriorityValue.setStatus("current")


class _Es2126plusQoSDTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126plusQoSDTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusQoSDTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126plusQoSDTypeTOSPriorityQueue_Object = MibTableColumn
es2126plusQoSDTypeTOSPriorityQueue = _Es2126plusQoSDTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 4, 1, 1, 3),
    _Es2126plusQoSDTypeTOSPriorityQueue_Type()
)
es2126plusQoSDTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSDTypeTOSPriorityQueue.setStatus("current")
_Es2126plusQoSTTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126plusQoSTTypeTOSPriority = _Es2126plusQoSTTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 5)
)
_Es2126plusQoSTTypeTOSPriorityTable_Object = MibTable
es2126plusQoSTTypeTOSPriorityTable = _Es2126plusQoSTTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    es2126plusQoSTTypeTOSPriorityTable.setStatus("current")
_Es2126plusQoSTTypeTOSPriorityEntry_Object = MibTableRow
es2126plusQoSTTypeTOSPriorityEntry = _Es2126plusQoSTTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 5, 1, 1)
)
es2126plusQoSTTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusQoSTTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusQoSTTypeTOSPriorityEntry.setStatus("current")


class _Es2126plusQoSTTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126plusQoSTTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126plusQoSTTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126plusQoSTTypeTOSPriorityIndex_Object = MibTableColumn
es2126plusQoSTTypeTOSPriorityIndex = _Es2126plusQoSTTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 5, 1, 1, 1),
    _Es2126plusQoSTTypeTOSPriorityIndex_Type()
)
es2126plusQoSTTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusQoSTTypeTOSPriorityIndex.setStatus("current")


class _Es2126plusQoSTTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126plusQoSTTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusQoSTTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126plusQoSTTypeTOSPriorityValue_Object = MibTableColumn
es2126plusQoSTTypeTOSPriorityValue = _Es2126plusQoSTTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 5, 1, 1, 2),
    _Es2126plusQoSTTypeTOSPriorityValue_Type()
)
es2126plusQoSTTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusQoSTTypeTOSPriorityValue.setStatus("current")


class _Es2126plusQoSTTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126plusQoSTTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusQoSTTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126plusQoSTTypeTOSPriorityQueue_Object = MibTableColumn
es2126plusQoSTTypeTOSPriorityQueue = _Es2126plusQoSTTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 5, 1, 1, 3),
    _Es2126plusQoSTTypeTOSPriorityQueue_Type()
)
es2126plusQoSTTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSTTypeTOSPriorityQueue.setStatus("current")
_Es2126plusQoSRTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126plusQoSRTypeTOSPriority = _Es2126plusQoSRTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 6)
)
_Es2126plusQoSRTypeTOSPriorityTable_Object = MibTable
es2126plusQoSRTypeTOSPriorityTable = _Es2126plusQoSRTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 6, 1)
)
if mibBuilder.loadTexts:
    es2126plusQoSRTypeTOSPriorityTable.setStatus("current")
_Es2126plusQoSRTypeTOSPriorityEntry_Object = MibTableRow
es2126plusQoSRTypeTOSPriorityEntry = _Es2126plusQoSRTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 6, 1, 1)
)
es2126plusQoSRTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusQoSRTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusQoSRTypeTOSPriorityEntry.setStatus("current")


class _Es2126plusQoSRTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126plusQoSRTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126plusQoSRTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126plusQoSRTypeTOSPriorityIndex_Object = MibTableColumn
es2126plusQoSRTypeTOSPriorityIndex = _Es2126plusQoSRTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 6, 1, 1, 1),
    _Es2126plusQoSRTypeTOSPriorityIndex_Type()
)
es2126plusQoSRTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusQoSRTypeTOSPriorityIndex.setStatus("current")


class _Es2126plusQoSRTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126plusQoSRTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusQoSRTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126plusQoSRTypeTOSPriorityValue_Object = MibTableColumn
es2126plusQoSRTypeTOSPriorityValue = _Es2126plusQoSRTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 6, 1, 1, 2),
    _Es2126plusQoSRTypeTOSPriorityValue_Type()
)
es2126plusQoSRTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusQoSRTypeTOSPriorityValue.setStatus("current")


class _Es2126plusQoSRTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126plusQoSRTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusQoSRTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126plusQoSRTypeTOSPriorityQueue_Object = MibTableColumn
es2126plusQoSRTypeTOSPriorityQueue = _Es2126plusQoSRTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 6, 1, 1, 3),
    _Es2126plusQoSRTypeTOSPriorityQueue_Type()
)
es2126plusQoSRTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSRTypeTOSPriorityQueue.setStatus("current")
_Es2126plusQoSMTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126plusQoSMTypeTOSPriority = _Es2126plusQoSMTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 7)
)
_Es2126plusQoSMTypeTOSPriorityTable_Object = MibTable
es2126plusQoSMTypeTOSPriorityTable = _Es2126plusQoSMTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 7, 1)
)
if mibBuilder.loadTexts:
    es2126plusQoSMTypeTOSPriorityTable.setStatus("current")
_Es2126plusQoSMTypeTOSPriorityEntry_Object = MibTableRow
es2126plusQoSMTypeTOSPriorityEntry = _Es2126plusQoSMTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 7, 1, 1)
)
es2126plusQoSMTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusQoSMTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusQoSMTypeTOSPriorityEntry.setStatus("current")


class _Es2126plusQoSMTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126plusQoSMTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126plusQoSMTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126plusQoSMTypeTOSPriorityIndex_Object = MibTableColumn
es2126plusQoSMTypeTOSPriorityIndex = _Es2126plusQoSMTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 7, 1, 1, 1),
    _Es2126plusQoSMTypeTOSPriorityIndex_Type()
)
es2126plusQoSMTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusQoSMTypeTOSPriorityIndex.setStatus("current")


class _Es2126plusQoSMTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126plusQoSMTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusQoSMTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126plusQoSMTypeTOSPriorityValue_Object = MibTableColumn
es2126plusQoSMTypeTOSPriorityValue = _Es2126plusQoSMTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 7, 1, 1, 2),
    _Es2126plusQoSMTypeTOSPriorityValue_Type()
)
es2126plusQoSMTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusQoSMTypeTOSPriorityValue.setStatus("current")


class _Es2126plusQoSMTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126plusQoSMTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusQoSMTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126plusQoSMTypeTOSPriorityQueue_Object = MibTableColumn
es2126plusQoSMTypeTOSPriorityQueue = _Es2126plusQoSMTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 7, 1, 1, 3),
    _Es2126plusQoSMTypeTOSPriorityQueue_Type()
)
es2126plusQoSMTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSMTypeTOSPriorityQueue.setStatus("current")
_Es2126plusQoSDSCPPriority_ObjectIdentity = ObjectIdentity
es2126plusQoSDSCPPriority = _Es2126plusQoSDSCPPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 8)
)
_Es2126plusQoSDSCPPriorityTable_Object = MibTable
es2126plusQoSDSCPPriorityTable = _Es2126plusQoSDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 8, 1)
)
if mibBuilder.loadTexts:
    es2126plusQoSDSCPPriorityTable.setStatus("current")
_Es2126plusQoSDSCPPriorityEntry_Object = MibTableRow
es2126plusQoSDSCPPriorityEntry = _Es2126plusQoSDSCPPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 8, 1, 1)
)
es2126plusQoSDSCPPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusQoSDSCPPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126plusQoSDSCPPriorityEntry.setStatus("current")


class _Es2126plusQoSDSCPPriorityIndex_Type(Integer32):
    """Custom type es2126plusQoSDSCPPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2126plusQoSDSCPPriorityIndex_Type.__name__ = "Integer32"
_Es2126plusQoSDSCPPriorityIndex_Object = MibTableColumn
es2126plusQoSDSCPPriorityIndex = _Es2126plusQoSDSCPPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 8, 1, 1, 1),
    _Es2126plusQoSDSCPPriorityIndex_Type()
)
es2126plusQoSDSCPPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusQoSDSCPPriorityIndex.setStatus("current")


class _Es2126plusQoSDSCPPriorityValue_Type(Integer32):
    """Custom type es2126plusQoSDSCPPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2126plusQoSDSCPPriorityValue_Type.__name__ = "Integer32"
_Es2126plusQoSDSCPPriorityValue_Object = MibTableColumn
es2126plusQoSDSCPPriorityValue = _Es2126plusQoSDSCPPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 8, 1, 1, 2),
    _Es2126plusQoSDSCPPriorityValue_Type()
)
es2126plusQoSDSCPPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusQoSDSCPPriorityValue.setStatus("current")


class _Es2126plusQoSDSCPPriorityQueue_Type(Integer32):
    """Custom type es2126plusQoSDSCPPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusQoSDSCPPriorityQueue_Type.__name__ = "Integer32"
_Es2126plusQoSDSCPPriorityQueue_Object = MibTableColumn
es2126plusQoSDSCPPriorityQueue = _Es2126plusQoSDSCPPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 16, 8, 1, 1, 3),
    _Es2126plusQoSDSCPPriorityQueue_Type()
)
es2126plusQoSDSCPPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusQoSDSCPPriorityQueue.setStatus("current")
_Es2126plusVlan_ObjectIdentity = ObjectIdentity
es2126plusVlan = _Es2126plusVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17)
)
_Es2126plusVlanModeConfig_ObjectIdentity = ObjectIdentity
es2126plusVlanModeConfig = _Es2126plusVlanModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 1)
)


class _Es2126plusVlanMode_Type(Integer32):
    """Custom type es2126plusVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusVlanMode_Type.__name__ = "Integer32"
_Es2126plusVlanMode_Object = MibScalar
es2126plusVlanMode = _Es2126plusVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 1, 1),
    _Es2126plusVlanMode_Type()
)
es2126plusVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVlanMode.setStatus("current")


class _Es2126plusSymmetricVlan_Type(Integer32):
    """Custom type es2126plusSymmetricVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusSymmetricVlan_Type.__name__ = "Integer32"
_Es2126plusSymmetricVlan_Object = MibScalar
es2126plusSymmetricVlan = _Es2126plusSymmetricVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 1, 2),
    _Es2126plusSymmetricVlan_Type()
)
es2126plusSymmetricVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusSymmetricVlan.setStatus("current")


class _Es2126plusVlanSVL_Type(Integer32):
    """Custom type es2126plusVlanSVL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusVlanSVL_Type.__name__ = "Integer32"
_Es2126plusVlanSVL_Object = MibScalar
es2126plusVlanSVL = _Es2126plusVlanSVL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 1, 3),
    _Es2126plusVlanSVL_Type()
)
es2126plusVlanSVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVlanSVL.setStatus("current")


class _Es2126plusDoubleTag_Type(Integer32):
    """Custom type es2126plusDoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusDoubleTag_Type.__name__ = "Integer32"
_Es2126plusDoubleTag_Object = MibScalar
es2126plusDoubleTag = _Es2126plusDoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 1, 4),
    _Es2126plusDoubleTag_Type()
)
es2126plusDoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDoubleTag.setStatus("current")


class _Es2126plusUpLinkPort_Type(Integer32):
    """Custom type es2126plusUpLinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusUpLinkPort_Type.__name__ = "Integer32"
_Es2126plusUpLinkPort_Object = MibScalar
es2126plusUpLinkPort = _Es2126plusUpLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 1, 5),
    _Es2126plusUpLinkPort_Type()
)
es2126plusUpLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusUpLinkPort.setStatus("current")
_Es2126plusTagBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2126plusTagBasedVlanGroup = _Es2126plusTagBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2)
)


class _Es2126plusTagBasedVlanNumbers_Type(Integer32):
    """Custom type es2126plusTagBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusTagBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2126plusTagBasedVlanNumbers_Object = MibScalar
es2126plusTagBasedVlanNumbers = _Es2126plusTagBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 1),
    _Es2126plusTagBasedVlanNumbers_Type()
)
es2126plusTagBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanNumbers.setStatus("current")


class _Es2126plusTagBasedCreateStatus_Type(Integer32):
    """Custom type es2126plusTagBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126plusTagBasedCreateStatus_Type.__name__ = "Integer32"
_Es2126plusTagBasedCreateStatus_Object = MibScalar
es2126plusTagBasedCreateStatus = _Es2126plusTagBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 2),
    _Es2126plusTagBasedCreateStatus_Type()
)
es2126plusTagBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTagBasedCreateStatus.setStatus("current")
_Es2126plusTagBasedVlanTable_Object = MibTable
es2126plusTagBasedVlanTable = _Es2126plusTagBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3)
)
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanTable.setStatus("current")
_Es2126plusTagBasedVlanEntry_Object = MibTableRow
es2126plusTagBasedVlanEntry = _Es2126plusTagBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3, 1)
)
es2126plusTagBasedVlanEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusTagBasedVlanVid"),
)
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanEntry.setStatus("current")


class _Es2126plusTagBasedVlanVid_Type(Integer32):
    """Custom type es2126plusTagBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusTagBasedVlanVid_Type.__name__ = "Integer32"
_Es2126plusTagBasedVlanVid_Object = MibTableColumn
es2126plusTagBasedVlanVid = _Es2126plusTagBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3, 1, 1),
    _Es2126plusTagBasedVlanVid_Type()
)
es2126plusTagBasedVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanVid.setStatus("current")
_Es2126plusTagBasedVlanName_Type = DisplayString
_Es2126plusTagBasedVlanName_Object = MibTableColumn
es2126plusTagBasedVlanName = _Es2126plusTagBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3, 1, 2),
    _Es2126plusTagBasedVlanName_Type()
)
es2126plusTagBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanName.setStatus("current")
_Es2126plusTagBasedVlanMember_Type = DisplayString
_Es2126plusTagBasedVlanMember_Object = MibTableColumn
es2126plusTagBasedVlanMember = _Es2126plusTagBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3, 1, 3),
    _Es2126plusTagBasedVlanMember_Type()
)
es2126plusTagBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanMember.setStatus("current")
_Es2126plusTagBasedVlanUntag_Type = DisplayString
_Es2126plusTagBasedVlanUntag_Object = MibTableColumn
es2126plusTagBasedVlanUntag = _Es2126plusTagBasedVlanUntag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3, 1, 4),
    _Es2126plusTagBasedVlanUntag_Type()
)
es2126plusTagBasedVlanUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanUntag.setStatus("current")


class _Es2126plusTagBasedVlanRowStatus_Type(Integer32):
    """Custom type es2126plusTagBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126plusTagBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2126plusTagBasedVlanRowStatus_Object = MibTableColumn
es2126plusTagBasedVlanRowStatus = _Es2126plusTagBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 2, 3, 1, 5),
    _Es2126plusTagBasedVlanRowStatus_Type()
)
es2126plusTagBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTagBasedVlanRowStatus.setStatus("current")
_Es2126plusVlanPvid_ObjectIdentity = ObjectIdentity
es2126plusVlanPvid = _Es2126plusVlanPvid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3)
)
_Es2126plusVlanPvidTable_Object = MibTable
es2126plusVlanPvidTable = _Es2126plusVlanPvidTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    es2126plusVlanPvidTable.setStatus("current")
_Es2126plusVlanPvidEntry_Object = MibTableRow
es2126plusVlanPvidEntry = _Es2126plusVlanPvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3, 1, 1)
)
es2126plusVlanPvidEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusVlanPvidPort"),
)
if mibBuilder.loadTexts:
    es2126plusVlanPvidEntry.setStatus("current")


class _Es2126plusVlanPvidPort_Type(Integer32):
    """Custom type es2126plusVlanPvidPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusVlanPvidPort_Type.__name__ = "Integer32"
_Es2126plusVlanPvidPort_Object = MibTableColumn
es2126plusVlanPvidPort = _Es2126plusVlanPvidPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3, 1, 1, 1),
    _Es2126plusVlanPvidPort_Type()
)
es2126plusVlanPvidPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusVlanPvidPort.setStatus("current")


class _Es2126plusVlanPvidValue_Type(Integer32):
    """Custom type es2126plusVlanPvidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusVlanPvidValue_Type.__name__ = "Integer32"
_Es2126plusVlanPvidValue_Object = MibTableColumn
es2126plusVlanPvidValue = _Es2126plusVlanPvidValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3, 1, 1, 2),
    _Es2126plusVlanPvidValue_Type()
)
es2126plusVlanPvidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVlanPvidValue.setStatus("current")


class _Es2126plusVlanPvidDefaultPriority_Type(Integer32):
    """Custom type es2126plusVlanPvidDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusVlanPvidDefaultPriority_Type.__name__ = "Integer32"
_Es2126plusVlanPvidDefaultPriority_Object = MibTableColumn
es2126plusVlanPvidDefaultPriority = _Es2126plusVlanPvidDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3, 1, 1, 3),
    _Es2126plusVlanPvidDefaultPriority_Type()
)
es2126plusVlanPvidDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVlanPvidDefaultPriority.setStatus("current")


class _Es2126plusVlanPvidDropUntag_Type(Integer32):
    """Custom type es2126plusVlanPvidDropUntag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126plusVlanPvidDropUntag_Type.__name__ = "Integer32"
_Es2126plusVlanPvidDropUntag_Object = MibTableColumn
es2126plusVlanPvidDropUntag = _Es2126plusVlanPvidDropUntag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 3, 1, 1, 4),
    _Es2126plusVlanPvidDropUntag_Type()
)
es2126plusVlanPvidDropUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusVlanPvidDropUntag.setStatus("current")
_Es2126plusPortBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2126plusPortBasedVlanGroup = _Es2126plusPortBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4)
)


class _Es2126plusPortBasedVlanNumbers_Type(Integer32):
    """Custom type es2126plusPortBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusPortBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2126plusPortBasedVlanNumbers_Object = MibScalar
es2126plusPortBasedVlanNumbers = _Es2126plusPortBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 1),
    _Es2126plusPortBasedVlanNumbers_Type()
)
es2126plusPortBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanNumbers.setStatus("current")


class _Es2126plusPortBasedCreateStatus_Type(Integer32):
    """Custom type es2126plusPortBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusPortBasedCreateStatus_Type.__name__ = "Integer32"
_Es2126plusPortBasedCreateStatus_Object = MibScalar
es2126plusPortBasedCreateStatus = _Es2126plusPortBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 2),
    _Es2126plusPortBasedCreateStatus_Type()
)
es2126plusPortBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBasedCreateStatus.setStatus("current")
_Es2126plusPortBasedVlanTable_Object = MibTable
es2126plusPortBasedVlanTable = _Es2126plusPortBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 3)
)
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanTable.setStatus("current")
_Es2126plusPortBasedVlanEntry_Object = MibTableRow
es2126plusPortBasedVlanEntry = _Es2126plusPortBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 3, 1)
)
es2126plusPortBasedVlanEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusPortBasedVlanIndex"),
)
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanEntry.setStatus("current")


class _Es2126plusPortBasedVlanIndex_Type(Integer32):
    """Custom type es2126plusPortBasedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusPortBasedVlanIndex_Type.__name__ = "Integer32"
_Es2126plusPortBasedVlanIndex_Object = MibTableColumn
es2126plusPortBasedVlanIndex = _Es2126plusPortBasedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 3, 1, 1),
    _Es2126plusPortBasedVlanIndex_Type()
)
es2126plusPortBasedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanIndex.setStatus("current")
_Es2126plusPortBasedVlanName_Type = DisplayString
_Es2126plusPortBasedVlanName_Object = MibTableColumn
es2126plusPortBasedVlanName = _Es2126plusPortBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 3, 1, 2),
    _Es2126plusPortBasedVlanName_Type()
)
es2126plusPortBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanName.setStatus("current")
_Es2126plusPortBasedVlanMember_Type = DisplayString
_Es2126plusPortBasedVlanMember_Object = MibTableColumn
es2126plusPortBasedVlanMember = _Es2126plusPortBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 3, 1, 3),
    _Es2126plusPortBasedVlanMember_Type()
)
es2126plusPortBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanMember.setStatus("current")


class _Es2126plusPortBasedVlanRowStatus_Type(Integer32):
    """Custom type es2126plusPortBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126plusPortBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2126plusPortBasedVlanRowStatus_Object = MibTableColumn
es2126plusPortBasedVlanRowStatus = _Es2126plusPortBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 4, 3, 1, 4),
    _Es2126plusPortBasedVlanRowStatus_Type()
)
es2126plusPortBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusPortBasedVlanRowStatus.setStatus("current")
_Es2126plusManagementVlan_ObjectIdentity = ObjectIdentity
es2126plusManagementVlan = _Es2126plusManagementVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 5)
)


class _Es2126plusManagementVlanState_Type(Integer32):
    """Custom type es2126plusManagementVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusManagementVlanState_Type.__name__ = "Integer32"
_Es2126plusManagementVlanState_Object = MibScalar
es2126plusManagementVlanState = _Es2126plusManagementVlanState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 5, 1),
    _Es2126plusManagementVlanState_Type()
)
es2126plusManagementVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementVlanState.setStatus("current")


class _Es2126plusManagementVlanVid_Type(Integer32):
    """Custom type es2126plusManagementVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126plusManagementVlanVid_Type.__name__ = "Integer32"
_Es2126plusManagementVlanVid_Object = MibScalar
es2126plusManagementVlanVid = _Es2126plusManagementVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 17, 5, 2),
    _Es2126plusManagementVlanVid_Type()
)
es2126plusManagementVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusManagementVlanVid.setStatus("current")
_Es2126plusDot1X_ObjectIdentity = ObjectIdentity
es2126plusDot1X = _Es2126plusDot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18)
)
_Es2126plusDot1XStateSetting_ObjectIdentity = ObjectIdentity
es2126plusDot1XStateSetting = _Es2126plusDot1XStateSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1)
)
_Es2126plusRadiusServer_Type = IpAddress
_Es2126plusRadiusServer_Object = MibScalar
es2126plusRadiusServer = _Es2126plusRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1, 1),
    _Es2126plusRadiusServer_Type()
)
es2126plusRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusRadiusServer.setStatus("current")


class _Es2126plusDot1XPort_Type(Integer32):
    """Custom type es2126plusDot1XPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusDot1XPort_Type.__name__ = "Integer32"
_Es2126plusDot1XPort_Object = MibScalar
es2126plusDot1XPort = _Es2126plusDot1XPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1, 2),
    _Es2126plusDot1XPort_Type()
)
es2126plusDot1XPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPort.setStatus("current")
_Es2126plusSecretKey_Type = DisplayString
_Es2126plusSecretKey_Object = MibScalar
es2126plusSecretKey = _Es2126plusSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1, 3),
    _Es2126plusSecretKey_Type()
)
es2126plusSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusSecretKey.setStatus("current")


class _Es2126plusAccountingService_Type(Integer32):
    """Custom type es2126plusAccountingService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusAccountingService_Type.__name__ = "Integer32"
_Es2126plusAccountingService_Object = MibScalar
es2126plusAccountingService = _Es2126plusAccountingService_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1, 4),
    _Es2126plusAccountingService_Type()
)
es2126plusAccountingService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountingService.setStatus("current")
_Es2126plusAccountingServer_Type = IpAddress
_Es2126plusAccountingServer_Object = MibScalar
es2126plusAccountingServer = _Es2126plusAccountingServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1, 5),
    _Es2126plusAccountingServer_Type()
)
es2126plusAccountingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountingServer.setStatus("current")


class _Es2126plusAccountingPort_Type(Integer32):
    """Custom type es2126plusAccountingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusAccountingPort_Type.__name__ = "Integer32"
_Es2126plusAccountingPort_Object = MibScalar
es2126plusAccountingPort = _Es2126plusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 1, 6),
    _Es2126plusAccountingPort_Type()
)
es2126plusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusAccountingPort.setStatus("current")
_Es2126plusDot1XPortSecurityManagement_ObjectIdentity = ObjectIdentity
es2126plusDot1XPortSecurityManagement = _Es2126plusDot1XPortSecurityManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2)
)
_Es2126plusDot1XPortSecurityTable_Object = MibTable
es2126plusDot1XPortSecurityTable = _Es2126plusDot1XPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityTable.setStatus("current")
_Es2126plusDot1XPortSecurityEntry_Object = MibTableRow
es2126plusDot1XPortSecurityEntry = _Es2126plusDot1XPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1)
)
es2126plusDot1XPortSecurityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusDot1XPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityEntry.setStatus("current")


class _Es2126plusDot1XPortSecurityPortIndex_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusDot1XPortSecurityPortIndex_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityPortIndex_Object = MibTableColumn
es2126plusDot1XPortSecurityPortIndex = _Es2126plusDot1XPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 1),
    _Es2126plusDot1XPortSecurityPortIndex_Type()
)
es2126plusDot1XPortSecurityPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityPortIndex.setStatus("current")


class _Es2126plusDot1XPortSecurityMode_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusDot1XPortSecurityMode_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityMode_Object = MibTableColumn
es2126plusDot1XPortSecurityMode = _Es2126plusDot1XPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 2),
    _Es2126plusDot1XPortSecurityMode_Type()
)
es2126plusDot1XPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityMode.setStatus("current")


class _Es2126plusDot1XPortSecurityPortControl_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusDot1XPortSecurityPortControl_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityPortControl_Object = MibTableColumn
es2126plusDot1XPortSecurityPortControl = _Es2126plusDot1XPortSecurityPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 3),
    _Es2126plusDot1XPortSecurityPortControl_Type()
)
es2126plusDot1XPortSecurityPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityPortControl.setStatus("current")


class _Es2126plusDot1XPortSecurityReAuthMax_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityReAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2126plusDot1XPortSecurityReAuthMax_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityReAuthMax_Object = MibTableColumn
es2126plusDot1XPortSecurityReAuthMax = _Es2126plusDot1XPortSecurityReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 4),
    _Es2126plusDot1XPortSecurityReAuthMax_Type()
)
es2126plusDot1XPortSecurityReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityReAuthMax.setStatus("current")


class _Es2126plusDot1XPortSecurityTxPeriod_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusDot1XPortSecurityTxPeriod_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityTxPeriod_Object = MibTableColumn
es2126plusDot1XPortSecurityTxPeriod = _Es2126plusDot1XPortSecurityTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 5),
    _Es2126plusDot1XPortSecurityTxPeriod_Type()
)
es2126plusDot1XPortSecurityTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityTxPeriod.setStatus("current")


class _Es2126plusDot1XPortSecurityQuietPeriod_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2126plusDot1XPortSecurityQuietPeriod_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityQuietPeriod_Object = MibTableColumn
es2126plusDot1XPortSecurityQuietPeriod = _Es2126plusDot1XPortSecurityQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 6),
    _Es2126plusDot1XPortSecurityQuietPeriod_Type()
)
es2126plusDot1XPortSecurityQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityQuietPeriod.setStatus("current")


class _Es2126plusDot1XPortSecurityReAuthEnabled_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityReAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusDot1XPortSecurityReAuthEnabled_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityReAuthEnabled_Object = MibTableColumn
es2126plusDot1XPortSecurityReAuthEnabled = _Es2126plusDot1XPortSecurityReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 7),
    _Es2126plusDot1XPortSecurityReAuthEnabled_Type()
)
es2126plusDot1XPortSecurityReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityReAuthEnabled.setStatus("current")


class _Es2126plusDot1XPortSecurityReAuthPeriod_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusDot1XPortSecurityReAuthPeriod_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityReAuthPeriod_Object = MibTableColumn
es2126plusDot1XPortSecurityReAuthPeriod = _Es2126plusDot1XPortSecurityReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 8),
    _Es2126plusDot1XPortSecurityReAuthPeriod_Type()
)
es2126plusDot1XPortSecurityReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityReAuthPeriod.setStatus("current")


class _Es2126plusDot1XPortSecurityMaxRequest_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityMaxRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2126plusDot1XPortSecurityMaxRequest_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityMaxRequest_Object = MibTableColumn
es2126plusDot1XPortSecurityMaxRequest = _Es2126plusDot1XPortSecurityMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 9),
    _Es2126plusDot1XPortSecurityMaxRequest_Type()
)
es2126plusDot1XPortSecurityMaxRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityMaxRequest.setStatus("current")


class _Es2126plusDot1XPortSecuritySuppTimeout_Type(Integer32):
    """Custom type es2126plusDot1XPortSecuritySuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusDot1XPortSecuritySuppTimeout_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecuritySuppTimeout_Object = MibTableColumn
es2126plusDot1XPortSecuritySuppTimeout = _Es2126plusDot1XPortSecuritySuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 10),
    _Es2126plusDot1XPortSecuritySuppTimeout_Type()
)
es2126plusDot1XPortSecuritySuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecuritySuppTimeout.setStatus("current")


class _Es2126plusDot1XPortSecurityServerTimeout_Type(Integer32):
    """Custom type es2126plusDot1XPortSecurityServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusDot1XPortSecurityServerTimeout_Type.__name__ = "Integer32"
_Es2126plusDot1XPortSecurityServerTimeout_Object = MibTableColumn
es2126plusDot1XPortSecurityServerTimeout = _Es2126plusDot1XPortSecurityServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 11),
    _Es2126plusDot1XPortSecurityServerTimeout_Type()
)
es2126plusDot1XPortSecurityServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityServerTimeout.setStatus("current")
_Es2126plusDot1XPortSecurityStatus_Type = DisplayString
_Es2126plusDot1XPortSecurityStatus_Object = MibTableColumn
es2126plusDot1XPortSecurityStatus = _Es2126plusDot1XPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 18, 2, 1, 1, 12),
    _Es2126plusDot1XPortSecurityStatus_Type()
)
es2126plusDot1XPortSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusDot1XPortSecurityStatus.setStatus("current")
_Es2126plusTrunkInfo_ObjectIdentity = ObjectIdentity
es2126plusTrunkInfo = _Es2126plusTrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19)
)
_Es2126plusTrunkPort_ObjectIdentity = ObjectIdentity
es2126plusTrunkPort = _Es2126plusTrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1)
)
_Es2126plusTrunkPortTable_Object = MibTable
es2126plusTrunkPortTable = _Es2126plusTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    es2126plusTrunkPortTable.setStatus("current")
_Es2126plusTrunkPortEntry_Object = MibTableRow
es2126plusTrunkPortEntry = _Es2126plusTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1)
)
es2126plusTrunkPortEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    es2126plusTrunkPortEntry.setStatus("current")


class _Es2126plusTrunkPortIndex_Type(Integer32):
    """Custom type es2126plusTrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusTrunkPortIndex_Type.__name__ = "Integer32"
_Es2126plusTrunkPortIndex_Object = MibTableColumn
es2126plusTrunkPortIndex = _Es2126plusTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 1),
    _Es2126plusTrunkPortIndex_Type()
)
es2126plusTrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusTrunkPortIndex.setStatus("current")


class _Es2126plusTrunkPortMethod_Type(Integer32):
    """Custom type es2126plusTrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusTrunkPortMethod_Type.__name__ = "Integer32"
_Es2126plusTrunkPortMethod_Object = MibTableColumn
es2126plusTrunkPortMethod = _Es2126plusTrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 2),
    _Es2126plusTrunkPortMethod_Type()
)
es2126plusTrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrunkPortMethod.setStatus("current")


class _Es2126plusTrunkPortGroup_Type(Integer32):
    """Custom type es2126plusTrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126plusTrunkPortGroup_Type.__name__ = "Integer32"
_Es2126plusTrunkPortGroup_Object = MibTableColumn
es2126plusTrunkPortGroup = _Es2126plusTrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 3),
    _Es2126plusTrunkPortGroup_Type()
)
es2126plusTrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrunkPortGroup.setStatus("current")


class _Es2126plusTrunkPortActiveLacp_Type(Integer32):
    """Custom type es2126plusTrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusTrunkPortActiveLacp_Type.__name__ = "Integer32"
_Es2126plusTrunkPortActiveLacp_Object = MibTableColumn
es2126plusTrunkPortActiveLacp = _Es2126plusTrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 4),
    _Es2126plusTrunkPortActiveLacp_Type()
)
es2126plusTrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrunkPortActiveLacp.setStatus("current")


class _Es2126plusTrunkPortAggtr_Type(Integer32):
    """Custom type es2126plusTrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusTrunkPortAggtr_Type.__name__ = "Integer32"
_Es2126plusTrunkPortAggtr_Object = MibTableColumn
es2126plusTrunkPortAggtr = _Es2126plusTrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 5),
    _Es2126plusTrunkPortAggtr_Type()
)
es2126plusTrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusTrunkPortAggtr.setStatus("current")


class _Es2126plusTrunkPortStatus_Type(Integer32):
    """Custom type es2126plusTrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126plusTrunkPortStatus_Type.__name__ = "Integer32"
_Es2126plusTrunkPortStatus_Object = MibTableColumn
es2126plusTrunkPortStatus = _Es2126plusTrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 6),
    _Es2126plusTrunkPortStatus_Type()
)
es2126plusTrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusTrunkPortStatus.setStatus("current")


class _Es2126plusTrunkPortCurrentMode_Type(Integer32):
    """Custom type es2126plusTrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusTrunkPortCurrentMode_Type.__name__ = "Integer32"
_Es2126plusTrunkPortCurrentMode_Object = MibTableColumn
es2126plusTrunkPortCurrentMode = _Es2126plusTrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 1, 1, 1, 7),
    _Es2126plusTrunkPortCurrentMode_Type()
)
es2126plusTrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusTrunkPortCurrentMode.setStatus("current")
_Es2126plusAggregatorView_ObjectIdentity = ObjectIdentity
es2126plusAggregatorView = _Es2126plusAggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2)
)
_Es2126plusAggregatorViewTable_Object = MibTable
es2126plusAggregatorViewTable = _Es2126plusAggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    es2126plusAggregatorViewTable.setStatus("current")
_Es2126plusAggregatorViewEntry_Object = MibTableRow
es2126plusAggregatorViewEntry = _Es2126plusAggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2, 1, 1)
)
es2126plusAggregatorViewEntry.setIndexNames(
    (0, "LANCOM-ES-2126PLUS-MIB", "es2126plusAggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    es2126plusAggregatorViewEntry.setStatus("current")


class _Es2126plusAggregatorViewIndex_Type(Integer32):
    """Custom type es2126plusAggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126plusAggregatorViewIndex_Type.__name__ = "Integer32"
_Es2126plusAggregatorViewIndex_Object = MibTableColumn
es2126plusAggregatorViewIndex = _Es2126plusAggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2, 1, 1, 1),
    _Es2126plusAggregatorViewIndex_Type()
)
es2126plusAggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126plusAggregatorViewIndex.setStatus("current")


class _Es2126plusAggregatorViewMethod_Type(Integer32):
    """Custom type es2126plusAggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusAggregatorViewMethod_Type.__name__ = "Integer32"
_Es2126plusAggregatorViewMethod_Object = MibTableColumn
es2126plusAggregatorViewMethod = _Es2126plusAggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2, 1, 1, 2),
    _Es2126plusAggregatorViewMethod_Type()
)
es2126plusAggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusAggregatorViewMethod.setStatus("current")
_Es2126plusAggregatorViewMemberPorts_Type = DisplayString
_Es2126plusAggregatorViewMemberPorts_Object = MibTableColumn
es2126plusAggregatorViewMemberPorts = _Es2126plusAggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2, 1, 1, 3),
    _Es2126plusAggregatorViewMemberPorts_Type()
)
es2126plusAggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusAggregatorViewMemberPorts.setStatus("current")
_Es2126plusAggregatorViewReadyPorts_Type = DisplayString
_Es2126plusAggregatorViewReadyPorts_Object = MibTableColumn
es2126plusAggregatorViewReadyPorts = _Es2126plusAggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 2, 1, 1, 4),
    _Es2126plusAggregatorViewReadyPorts_Type()
)
es2126plusAggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126plusAggregatorViewReadyPorts.setStatus("current")
_Es2126plusLacpSystemConfiguration_ObjectIdentity = ObjectIdentity
es2126plusLacpSystemConfiguration = _Es2126plusLacpSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 3)
)


class _Es2126plusLacpSystemPriority_Type(Integer32):
    """Custom type es2126plusLacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126plusLacpSystemPriority_Type.__name__ = "Integer32"
_Es2126plusLacpSystemPriority_Object = MibScalar
es2126plusLacpSystemPriority = _Es2126plusLacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 3, 1),
    _Es2126plusLacpSystemPriority_Type()
)
es2126plusLacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusLacpSystemPriority.setStatus("current")


class _Es2126plusLacpSystemHashMethod_Type(Integer32):
    """Custom type es2126plusLacpSystemHashMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126plusLacpSystemHashMethod_Type.__name__ = "Integer32"
_Es2126plusLacpSystemHashMethod_Object = MibScalar
es2126plusLacpSystemHashMethod = _Es2126plusLacpSystemHashMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 19, 3, 2),
    _Es2126plusLacpSystemHashMethod_Type()
)
es2126plusLacpSystemHashMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusLacpSystemHashMethod.setStatus("current")
_Es2126plusTrapEntry_ObjectIdentity = ObjectIdentity
es2126plusTrapEntry = _Es2126plusTrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20)
)
_Es2126plusTrapVariable_ObjectIdentity = ObjectIdentity
es2126plusTrapVariable = _Es2126plusTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21, 1),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")
_LoginProtectInfo_Type = DisplayString
_LoginProtectInfo_Object = MibScalar
loginProtectInfo = _LoginProtectInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 21, 6),
    _LoginProtectInfo_Type()
)
loginProtectInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginProtectInfo.setStatus("current")
_Es2126plusLoginProtect_ObjectIdentity = ObjectIdentity
es2126plusLoginProtect = _Es2126plusLoginProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 22)
)


class _Es2126plusLockTime_Type(Integer32):
    """Custom type es2126plusLockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2126plusLockTime_Type.__name__ = "Integer32"
_Es2126plusLockTime_Object = MibScalar
es2126plusLockTime = _Es2126plusLockTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 22, 1),
    _Es2126plusLockTime_Type()
)
es2126plusLockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusLockTime.setStatus("current")


class _Es2126plusErrorCount_Type(Integer32):
    """Custom type es2126plusErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2126plusErrorCount_Type.__name__ = "Integer32"
_Es2126plusErrorCount_Object = MibScalar
es2126plusErrorCount = _Es2126plusErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 22, 2),
    _Es2126plusErrorCount_Type()
)
es2126plusErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126plusErrorCount.setStatus("current")

# Managed Objects groups


# Notification objects

es2126plusModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 1)
)
es2126plusModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126plusModuleInserted.setStatus(
        "current"
    )

es2126plusModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 2)
)
es2126plusModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126plusModuleRemoved.setStatus(
        "current"
    )

es2126plusDualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 3)
)
es2126plusDualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126plusDualMediaSwapped.setStatus(
        "current"
    )

es2126plusLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 4)
)
es2126plusLoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126plusLoopDetected.setStatus(
        "current"
    )

es2126plusLoginProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 5)
)
es2126plusLoginProtected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126plusLoginProtected.setStatus(
        "current"
    )

es2126plusStpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 100)
)
if mibBuilder.loadTexts:
    es2126plusStpStateDisabled.setStatus(
        "current"
    )

es2126plusStpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 101)
)
if mibBuilder.loadTexts:
    es2126plusStpStateEnabled.setStatus(
        "current"
    )

es2126plusStpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 102)
)
es2126plusStpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126plusStpTopologyChanged.setStatus(
        "current"
    )

es2126plusRmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 110)
)
if mibBuilder.loadTexts:
    es2126plusRmonRisingAlarm.setStatus(
        "current"
    )

es2126plusRmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 111)
)
if mibBuilder.loadTexts:
    es2126plusRmonFallingAlarm.setStatus(
        "current"
    )

es2126plusLacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 120)
)
es2126plusLacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PLUS-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2126plusLacpStateDisabled.setStatus(
        "current"
    )

es2126plusLacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 121)
)
es2126plusLacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PLUS-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2126plusLacpStateEnabled.setStatus(
        "current"
    )

es2126plusLacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 123)
)
es2126plusLacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PLUS-MIB", "actorkey"),
        ("LANCOM-ES-2126PLUS-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2126plusLacpPortAdded.setStatus(
        "current"
    )

es2126plusLacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 124)
)
es2126plusLacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PLUS-MIB", "actorkey"),
        ("LANCOM-ES-2126PLUS-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2126plusLacpPortTrunkFailure.setStatus(
        "current"
    )

es2126plusGvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 140)
)
if mibBuilder.loadTexts:
    es2126plusGvrpStateDisabled.setStatus(
        "current"
    )

es2126plusGvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 141)
)
if mibBuilder.loadTexts:
    es2126plusGvrpStateEnabled.setStatus(
        "current"
    )

es2126plusVlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 151)
)
if mibBuilder.loadTexts:
    es2126plusVlanPortBaseEnabled.setStatus(
        "current"
    )

es2126plusVlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 152)
)
if mibBuilder.loadTexts:
    es2126plusVlanTagBaseEnabled.setStatus(
        "current"
    )

es2126plusVlanMetroBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 153)
)
if mibBuilder.loadTexts:
    es2126plusVlanMetroBaseEnabled.setStatus(
        "current"
    )

es2126plusUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 200)
)
es2126plusUserLogin.setObjects(
    ("LANCOM-ES-2126PLUS-MIB", "username")
)
if mibBuilder.loadTexts:
    es2126plusUserLogin.setStatus(
        "current"
    )

es2126plusUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2128, 1, 20, 201)
)
es2126plusUserLogout.setObjects(
    ("LANCOM-ES-2126PLUS-MIB", "username")
)
if mibBuilder.loadTexts:
    es2126plusUserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-ES-2126PLUS-MIB",
    **{"lancomSystems": lancomSystems,
       "switchingSystems": switchingSystems,
       "fastEthernetSwitches": fastEthernetSwitches,
       "lancomES2126PLUS": lancomES2126PLUS,
       "es2126plusProduces": es2126plusProduces,
       "es2126plusSystem": es2126plusSystem,
       "es2126plusCommonSys": es2126plusCommonSys,
       "es2126plusReboot": es2126plusReboot,
       "es2126plusBiosVsersion": es2126plusBiosVsersion,
       "es2126plusFirmwareVersion": es2126plusFirmwareVersion,
       "es2126plusHardwareVersion": es2126plusHardwareVersion,
       "es2126plusMechanicalVersion": es2126plusMechanicalVersion,
       "es2126plusSerialNumber": es2126plusSerialNumber,
       "es2126plusHostMacAddress": es2126plusHostMacAddress,
       "es2126plusDevicePort": es2126plusDevicePort,
       "es2126plusRamSize": es2126plusRamSize,
       "es2126plusFlashSize": es2126plusFlashSize,
       "es2126plusSystemDescription": es2126plusSystemDescription,
       "es2126plusDeviceName": es2126plusDeviceName,
       "es2126plusIP": es2126plusIP,
       "es2126plusDhcpSetting": es2126plusDhcpSetting,
       "es2126plusIPAddress": es2126plusIPAddress,
       "es2126plusNetMask": es2126plusNetMask,
       "es2126plusDefaultGateway": es2126plusDefaultGateway,
       "es2126plusDnsSetting": es2126plusDnsSetting,
       "es2126plusDnsServer": es2126plusDnsServer,
       "es2126plusTime": es2126plusTime,
       "es2126plusSystemCurrentTime": es2126plusSystemCurrentTime,
       "es2126plusManualTimeSetting": es2126plusManualTimeSetting,
       "es2126plusNTPServer": es2126plusNTPServer,
       "es2126plusNTPTimeZone": es2126plusNTPTimeZone,
       "es2126plusNTPTimeSync": es2126plusNTPTimeSync,
       "es2126plusDaylightSavingTime": es2126plusDaylightSavingTime,
       "es2126plusDaylightStartTime": es2126plusDaylightStartTime,
       "es2126plusDaylightEndTime": es2126plusDaylightEndTime,
       "es2126plusAccount": es2126plusAccount,
       "es2126plusAccountNumber": es2126plusAccountNumber,
       "es2126plusAccountTable": es2126plusAccountTable,
       "es2126plusAccountEntry": es2126plusAccountEntry,
       "es2126plusAccountIndex": es2126plusAccountIndex,
       "es2126plusAccountAuthorization": es2126plusAccountAuthorization,
       "es2126plusAccountName": es2126plusAccountName,
       "es2126plusAccountPassword": es2126plusAccountPassword,
       "es2126plusAccountAddName": es2126plusAccountAddName,
       "es2126plusAccountAddPassword": es2126plusAccountAddPassword,
       "es2126plusDoAccountAdd": es2126plusDoAccountAdd,
       "es2126plusAccountDel": es2126plusAccountDel,
       "es2126plusSnmp": es2126plusSnmp,
       "es2126plusGetCommunity": es2126plusGetCommunity,
       "es2126plusSetCommunity": es2126plusSetCommunity,
       "es2126plusTrapHostNumber": es2126plusTrapHostNumber,
       "es2126plusTrapHostTable": es2126plusTrapHostTable,
       "es2126plusTrapHostEntry": es2126plusTrapHostEntry,
       "es2126plusTrapHostIndex": es2126plusTrapHostIndex,
       "es2126plusTrapHostIP": es2126plusTrapHostIP,
       "es2126plusTrapHostPort": es2126plusTrapHostPort,
       "es2126plusTrapHostCommunity": es2126plusTrapHostCommunity,
       "es2126plusRegisterMonitor": es2126plusRegisterMonitor,
       "es2126plusDeleteMonitor": es2126plusDeleteMonitor,
       "es2126plusMonitorTable": es2126plusMonitorTable,
       "es2126plusMonitorEntry": es2126plusMonitorEntry,
       "es2126plusMonitorTableIp": es2126plusMonitorTableIp,
       "es2126plusMonitorTableMac": es2126plusMonitorTableMac,
       "es2126plusTrapBootDelayTime": es2126plusTrapBootDelayTime,
       "es2126plusAlarm": es2126plusAlarm,
       "es2126plusEvent": es2126plusEvent,
       "es2126plusEventNumber": es2126plusEventNumber,
       "es2126plusEventTable": es2126plusEventTable,
       "es2126plusEventEntry": es2126plusEventEntry,
       "es2126plusEventIndex": es2126plusEventIndex,
       "es2126plusEventName": es2126plusEventName,
       "es2126plusEventSendEmail": es2126plusEventSendEmail,
       "es2126plusEventSendTrap": es2126plusEventSendTrap,
       "es2126plusEmail": es2126plusEmail,
       "es2126plusEmailServer": es2126plusEmailServer,
       "es2126plusEmailUsername": es2126plusEmailUsername,
       "es2126plusEmailPassword": es2126plusEmailPassword,
       "es2126plusEmailSender": es2126plusEmailSender,
       "es2126plusEmailReturnPath": es2126plusEmailReturnPath,
       "es2126plusEmailUserNumber": es2126plusEmailUserNumber,
       "es2126plusEmailUserTable": es2126plusEmailUserTable,
       "es2126plusEmailUserEntry": es2126plusEmailUserEntry,
       "es2126plusEmailUserIndex": es2126plusEmailUserIndex,
       "es2126plusEmailUserAddress": es2126plusEmailUserAddress,
       "es2126plusTftp": es2126plusTftp,
       "es2126plusTftpRemoteServer": es2126plusTftpRemoteServer,
       "es2126plusTftpInternalServerState": es2126plusTftpInternalServerState,
       "es2126plusConfiguration": es2126plusConfiguration,
       "es2126plusSaveRestore": es2126plusSaveRestore,
       "es2126plusSaveStart": es2126plusSaveStart,
       "es2126plusSaveUser": es2126plusSaveUser,
       "es2126plusRestoreDefault": es2126plusRestoreDefault,
       "es2126plusRestoreUser": es2126plusRestoreUser,
       "es2126plusConfigFile": es2126plusConfigFile,
       "es2126plusExportConfigName": es2126plusExportConfigName,
       "es2126plusDoExportConfig": es2126plusDoExportConfig,
       "es2126plusImportConfigName": es2126plusImportConfigName,
       "es2126plusDoImportConfig": es2126plusDoImportConfig,
       "es2126plusDiagnostic": es2126plusDiagnostic,
       "es2126plusInternalLoopbackTest": es2126plusInternalLoopbackTest,
       "es2126plusExternalLoopbackTest": es2126plusExternalLoopbackTest,
       "es2126plusPingTest": es2126plusPingTest,
       "es2126plusWatchdog": es2126plusWatchdog,
       "es2126plusWatchdogState": es2126plusWatchdogState,
       "es2126plusWatchdogTimeGap": es2126plusWatchdogTimeGap,
       "es2126plusWatchdogHost": es2126plusWatchdogHost,
       "es2126plusWatchdogResetMgtInf": es2126plusWatchdogResetMgtInf,
       "es2126plusWatchdogResetMgtInfCount": es2126plusWatchdogResetMgtInfCount,
       "es2126plusWatchdogResetSystem": es2126plusWatchdogResetSystem,
       "es2126plusWatchdogResetSystemCount": es2126plusWatchdogResetSystemCount,
       "es2126plusLog": es2126plusLog,
       "es2126plusClearLog": es2126plusClearLog,
       "es2126plusUploadLog": es2126plusUploadLog,
       "es2126plusAutoUploadLogState": es2126plusAutoUploadLogState,
       "es2126plusLogNumber": es2126plusLogNumber,
       "es2126plusLogTable": es2126plusLogTable,
       "es2126plusLogEntry": es2126plusLogEntry,
       "es2126plusLogIndex": es2126plusLogIndex,
       "es2126plusLogEvent": es2126plusLogEvent,
       "es2126plusFirmware": es2126plusFirmware,
       "es2126plusFirmwareFileName": es2126plusFirmwareFileName,
       "es2126plusDoFirmwareUpgrade": es2126plusDoFirmwareUpgrade,
       "es2126plusPort": es2126plusPort,
       "es2126plusPortStatus": es2126plusPortStatus,
       "es2126plusPortStatusNumber": es2126plusPortStatusNumber,
       "es2126plusPortStatusTable": es2126plusPortStatusTable,
       "es2126plusPortStatusEntry": es2126plusPortStatusEntry,
       "es2126plusPortStatusIndex": es2126plusPortStatusIndex,
       "es2126plusPortStatusMedia": es2126plusPortStatusMedia,
       "es2126plusPortStatusLink": es2126plusPortStatusLink,
       "es2126plusPortStatusPortState": es2126plusPortStatusPortState,
       "es2126plusPortStatusAutoNego": es2126plusPortStatusAutoNego,
       "es2126plusPortStatusSpdDpx": es2126plusPortStatusSpdDpx,
       "es2126plusPortStatusRxPause": es2126plusPortStatusRxPause,
       "es2126plusPortStatusTxPause": es2126plusPortStatusTxPause,
       "es2126plusPortStatusDescription": es2126plusPortStatusDescription,
       "es2126plusPortConf": es2126plusPortConf,
       "es2126plusPortConfNumber": es2126plusPortConfNumber,
       "es2126plusPortConfTable": es2126plusPortConfTable,
       "es2126plusPortConfEntry": es2126plusPortConfEntry,
       "es2126plusPortConfIndex": es2126plusPortConfIndex,
       "es2126plusPortConfPortState": es2126plusPortConfPortState,
       "es2126plusPortConfSpdDpx": es2126plusPortConfSpdDpx,
       "es2126plusPortConfFlwCtrl": es2126plusPortConfFlwCtrl,
       "es2126plusPortConfDescription": es2126plusPortConfDescription,
       "es2126plusPortBandwidth": es2126plusPortBandwidth,
       "es2126plusPortBandwidthTable": es2126plusPortBandwidthTable,
       "es2126plusPortBandwidthEntry": es2126plusPortBandwidthEntry,
       "es2126plusPortBandwidthIndex": es2126plusPortBandwidthIndex,
       "es2126plusPortBandwidthIngressRate": es2126plusPortBandwidthIngressRate,
       "es2126plusPortBandwidthEgressRate": es2126plusPortBandwidthEgressRate,
       "es2126plusPortBandwidthStormType": es2126plusPortBandwidthStormType,
       "es2126plusPortBandwidthStormRate": es2126plusPortBandwidthStormRate,
       "es2126plusPortSFPInfo": es2126plusPortSFPInfo,
       "es2126plusPortSFPInfoNumber": es2126plusPortSFPInfoNumber,
       "es2126plusPortSFPInfoTable": es2126plusPortSFPInfoTable,
       "es2126plusPortSFPInfoEntry": es2126plusPortSFPInfoEntry,
       "es2126plusPortSFPInfoIndex": es2126plusPortSFPInfoIndex,
       "es2126plusPortSFPConnectorType": es2126plusPortSFPConnectorType,
       "es2126plusPortSFPFiberType": es2126plusPortSFPFiberType,
       "es2126plusPortSFPWavelength": es2126plusPortSFPWavelength,
       "es2126plusPortSFPBaudRate": es2126plusPortSFPBaudRate,
       "es2126plusPortSFPVendorOUI": es2126plusPortSFPVendorOUI,
       "es2126plusPortSFPVendorName": es2126plusPortSFPVendorName,
       "es2126plusPortSFPVendorPN": es2126plusPortSFPVendorPN,
       "es2126plusPortSFPVendorRev": es2126plusPortSFPVendorRev,
       "es2126plusPortSFPVendorSN": es2126plusPortSFPVendorSN,
       "es2126plusPortSFPDateCode": es2126plusPortSFPDateCode,
       "es2126plusPortSFPTemperature": es2126plusPortSFPTemperature,
       "es2126plusPortSFPVcc": es2126plusPortSFPVcc,
       "es2126plusPortSFPTxBias": es2126plusPortSFPTxBias,
       "es2126plusPortSFPTxPWR": es2126plusPortSFPTxPWR,
       "es2126plusPortSFPRxPWR": es2126plusPortSFPRxPWR,
       "es2126plusLoopDetectedConf": es2126plusLoopDetectedConf,
       "es2126plusLoopDetectedNumber": es2126plusLoopDetectedNumber,
       "es2126plusLoopDetectedTable": es2126plusLoopDetectedTable,
       "es2126plusLoopDetectedEntry": es2126plusLoopDetectedEntry,
       "es2126plusLoopDetectedfIndex": es2126plusLoopDetectedfIndex,
       "es2126plusLoopDetectedStateEbl": es2126plusLoopDetectedStateEbl,
       "es2126plusLoopDetectedCurrentStatus": es2126plusLoopDetectedCurrentStatus,
       "es2126plusLoopDetectedRemoved": es2126plusLoopDetectedRemoved,
       "es2126plusLoopDetectedAction": es2126plusLoopDetectedAction,
       "es2126plusMacTableInfo": es2126plusMacTableInfo,
       "es2126plusMacTableMaintenance": es2126plusMacTableMaintenance,
       "es2126plusMacTableAgingTime": es2126plusMacTableAgingTime,
       "es2126plusMacTableFlush": es2126plusMacTableFlush,
       "es2126plusMacTableLearnPortLimitTable": es2126plusMacTableLearnPortLimitTable,
       "es2126plusMacTableLearnPortLimitEntry": es2126plusMacTableLearnPortLimitEntry,
       "es2126plusMacTableLearnPortLimitIndex": es2126plusMacTableLearnPortLimitIndex,
       "es2126plusMacTableLearnPortLimit": es2126plusMacTableLearnPortLimit,
       "es2126plusMacTableStaticMac": es2126plusMacTableStaticMac,
       "es2126plusMacTableStaticMacNumber": es2126plusMacTableStaticMacNumber,
       "es2126plusMacTableStaticMacEntryCreate": es2126plusMacTableStaticMacEntryCreate,
       "es2126plusMacTableStaticMacTable": es2126plusMacTableStaticMacTable,
       "es2126plusMacTableStaticMacEntry": es2126plusMacTableStaticMacEntry,
       "es2126plusMacTableStaticMacIndex": es2126plusMacTableStaticMacIndex,
       "es2126plusMacTableStaticMacAddress": es2126plusMacTableStaticMacAddress,
       "es2126plusMacTableStaticMacVid": es2126plusMacTableStaticMacVid,
       "es2126plusMacTableStaticMacQueue": es2126plusMacTableStaticMacQueue,
       "es2126plusMacTableStaticMacFwRule": es2126plusMacTableStaticMacFwRule,
       "es2126plusMacTableStaticMacPort": es2126plusMacTableStaticMacPort,
       "es2126plusMacTableStaticMacEntryAction": es2126plusMacTableStaticMacEntryAction,
       "es2126plusMacTableMacAlias": es2126plusMacTableMacAlias,
       "es2126plusMacTableMacAliasNumber": es2126plusMacTableMacAliasNumber,
       "es2126plusMacTableMacAliasEntryCreate": es2126plusMacTableMacAliasEntryCreate,
       "es2126plusMacTableMacAliasTable": es2126plusMacTableMacAliasTable,
       "es2126plusMacTableMacAliasEntry": es2126plusMacTableMacAliasEntry,
       "es2126plusMacTableMacAliasIndex": es2126plusMacTableMacAliasIndex,
       "es2126plusMacTableMacAliasAddress": es2126plusMacTableMacAliasAddress,
       "es2126plusMacTableMacAliasAlias": es2126plusMacTableMacAliasAlias,
       "es2126plusMacTableMacAliasEntryAction": es2126plusMacTableMacAliasEntryAction,
       "es2126plusGVRPInfo": es2126plusGVRPInfo,
       "es2126plusGvrpConf": es2126plusGvrpConf,
       "es2126plusGvrpConfState": es2126plusGvrpConfState,
       "es2126plusGvrpConfTable": es2126plusGvrpConfTable,
       "es2126plusGvrpConfEntry": es2126plusGvrpConfEntry,
       "es2126plusGvrpConfIndex": es2126plusGvrpConfIndex,
       "es2126plusGvrpConfJoinTime": es2126plusGvrpConfJoinTime,
       "es2126plusGvrpConfLeaveTime": es2126plusGvrpConfLeaveTime,
       "es2126plusGvrpConfLeaveAllTime": es2126plusGvrpConfLeaveAllTime,
       "es2126plusGvrpConfDefaultAppMode": es2126plusGvrpConfDefaultAppMode,
       "es2126plusGvrpConfDefaultRegMode": es2126plusGvrpConfDefaultRegMode,
       "es2126plusGvrpConfRestrictedMode": es2126plusGvrpConfRestrictedMode,
       "es2126plusGvrpCounter": es2126plusGvrpCounter,
       "es2126plusGvrpCounterTable": es2126plusGvrpCounterTable,
       "es2126plusGvrpCounterEntry": es2126plusGvrpCounterEntry,
       "es2126plusGvrpCounterIndex": es2126plusGvrpCounterIndex,
       "es2126plusGvrpCounterRxTotalGvrpPkts": es2126plusGvrpCounterRxTotalGvrpPkts,
       "es2126plusGvrpCounterRxInvalidGvrpPkts": es2126plusGvrpCounterRxInvalidGvrpPkts,
       "es2126plusGvrpCounterRxLeaveAllMsg": es2126plusGvrpCounterRxLeaveAllMsg,
       "es2126plusGvrpCounterRxJoinEmptyMsg": es2126plusGvrpCounterRxJoinEmptyMsg,
       "es2126plusGvrpCounterRxJoinInMsg": es2126plusGvrpCounterRxJoinInMsg,
       "es2126plusGvrpCounterRxLeaveEmptyMsg": es2126plusGvrpCounterRxLeaveEmptyMsg,
       "es2126plusGvrpCounterRxEmptyMsg": es2126plusGvrpCounterRxEmptyMsg,
       "es2126plusGvrpCounterTxTotalGvrpPkts": es2126plusGvrpCounterTxTotalGvrpPkts,
       "es2126plusGvrpCounterTxLeaveAllMsg": es2126plusGvrpCounterTxLeaveAllMsg,
       "es2126plusGvrpCounterTxJoinEmptyMsg": es2126plusGvrpCounterTxJoinEmptyMsg,
       "es2126plusGvrpCounterTxJoinInMsg": es2126plusGvrpCounterTxJoinInMsg,
       "es2126plusGvrpCounterTxLeaveEmptyMsg": es2126plusGvrpCounterTxLeaveEmptyMsg,
       "es2126plusGvrpCounterTxEmptyMsg": es2126plusGvrpCounterTxEmptyMsg,
       "es2126plusGvrpGroup": es2126plusGvrpGroup,
       "es2126plusGvrpGroupNumber": es2126plusGvrpGroupNumber,
       "es2126plusGvrpGroupTable": es2126plusGvrpGroupTable,
       "es2126plusGvrpGroupEntry": es2126plusGvrpGroupEntry,
       "es2126plusGvrpGroupId": es2126plusGvrpGroupId,
       "es2126plusGvrpGroupVid": es2126plusGvrpGroupVid,
       "es2126plusGvrpGroupMemberPort": es2126plusGvrpGroupMemberPort,
       "es2126plusSecurity": es2126plusSecurity,
       "es2126plusIsolatedPortGroup": es2126plusIsolatedPortGroup,
       "es2126plusMirror": es2126plusMirror,
       "es2126plusMirrorMode": es2126plusMirrorMode,
       "es2126plusMonitoringPort": es2126plusMonitoringPort,
       "es2126plusMonitoredIngressPort": es2126plusMonitoredIngressPort,
       "es2126plusMonitoredEgressPort": es2126plusMonitoredEgressPort,
       "es2126plusRestrictedGroup": es2126plusRestrictedGroup,
       "es2126plusRestrictedGroupIngress": es2126plusRestrictedGroupIngress,
       "es2126plusRestrictedGroupEgress": es2126plusRestrictedGroupEgress,
       "es2126plusVirtualStack": es2126plusVirtualStack,
       "es2126plusVirtualStackState": es2126plusVirtualStackState,
       "es2126plusVirtualStackRole": es2126plusVirtualStackRole,
       "es2126plusVirtualStackGroupID": es2126plusVirtualStackGroupID,
       "es2126plusManagementSecurity": es2126plusManagementSecurity,
       "es2126plusManagementSecurityNumber": es2126plusManagementSecurityNumber,
       "es2126plusManagementSecurityEntryCreate": es2126plusManagementSecurityEntryCreate,
       "es2126plusManagementSecurityTable": es2126plusManagementSecurityTable,
       "es2126plusManagementSecurityEntry": es2126plusManagementSecurityEntry,
       "es2126plusManagementSecurityIndex": es2126plusManagementSecurityIndex,
       "es2126plusManagementSecurityName": es2126plusManagementSecurityName,
       "es2126plusManagementSecurityVid": es2126plusManagementSecurityVid,
       "es2126plusManagementSecurityIpRange": es2126plusManagementSecurityIpRange,
       "es2126plusManagementSecurityIncomigPort": es2126plusManagementSecurityIncomigPort,
       "es2126plusManagementSecurityAccessType": es2126plusManagementSecurityAccessType,
       "es2126plusManagementSecurityAction": es2126plusManagementSecurityAction,
       "es2126plusManagementSecurityEntryAction": es2126plusManagementSecurityEntryAction,
       "es2126plusQoS": es2126plusQoS,
       "es2126plusQoSGlobalConfig": es2126plusQoSGlobalConfig,
       "es2126plusQoSMode": es2126plusQoSMode,
       "es2126plusQosPriorityControl1p": es2126plusQosPriorityControl1p,
       "es2126plusQosPriorityControlTOS": es2126plusQosPriorityControlTOS,
       "es2126plusQosPriorityControlDSCP": es2126plusQosPriorityControlDSCP,
       "es2126plusQoSSchedulingMethod": es2126plusQoSSchedulingMethod,
       "es2126plusQoSWeightQ0": es2126plusQoSWeightQ0,
       "es2126plusQoSWeightQ1": es2126plusQoSWeightQ1,
       "es2126plusQoSWeightQ2": es2126plusQoSWeightQ2,
       "es2126plusQoSWeightQ3": es2126plusQoSWeightQ3,
       "es2126plusQoSVIPPort": es2126plusQoSVIPPort,
       "es2126plusQoS1pPriority": es2126plusQoS1pPriority,
       "es2126plusQoS1pPriorityTable": es2126plusQoS1pPriorityTable,
       "es2126plusQoS1pPriorityEntry": es2126plusQoS1pPriorityEntry,
       "es2126plusQoS1pPriorityIndex": es2126plusQoS1pPriorityIndex,
       "es2126plusQoS1pPriorityValue": es2126plusQoS1pPriorityValue,
       "es2126plusQoS1pPriorityQueue": es2126plusQoS1pPriorityQueue,
       "es2126plusQoSDTypeTOSPriority": es2126plusQoSDTypeTOSPriority,
       "es2126plusQoSDTypeTOSPriorityTable": es2126plusQoSDTypeTOSPriorityTable,
       "es2126plusQoSDTypeTOSPriorityEntry": es2126plusQoSDTypeTOSPriorityEntry,
       "es2126plusQoSDTypeTOSPriorityIndex": es2126plusQoSDTypeTOSPriorityIndex,
       "es2126plusQoSDTypeTOSPriorityValue": es2126plusQoSDTypeTOSPriorityValue,
       "es2126plusQoSDTypeTOSPriorityQueue": es2126plusQoSDTypeTOSPriorityQueue,
       "es2126plusQoSTTypeTOSPriority": es2126plusQoSTTypeTOSPriority,
       "es2126plusQoSTTypeTOSPriorityTable": es2126plusQoSTTypeTOSPriorityTable,
       "es2126plusQoSTTypeTOSPriorityEntry": es2126plusQoSTTypeTOSPriorityEntry,
       "es2126plusQoSTTypeTOSPriorityIndex": es2126plusQoSTTypeTOSPriorityIndex,
       "es2126plusQoSTTypeTOSPriorityValue": es2126plusQoSTTypeTOSPriorityValue,
       "es2126plusQoSTTypeTOSPriorityQueue": es2126plusQoSTTypeTOSPriorityQueue,
       "es2126plusQoSRTypeTOSPriority": es2126plusQoSRTypeTOSPriority,
       "es2126plusQoSRTypeTOSPriorityTable": es2126plusQoSRTypeTOSPriorityTable,
       "es2126plusQoSRTypeTOSPriorityEntry": es2126plusQoSRTypeTOSPriorityEntry,
       "es2126plusQoSRTypeTOSPriorityIndex": es2126plusQoSRTypeTOSPriorityIndex,
       "es2126plusQoSRTypeTOSPriorityValue": es2126plusQoSRTypeTOSPriorityValue,
       "es2126plusQoSRTypeTOSPriorityQueue": es2126plusQoSRTypeTOSPriorityQueue,
       "es2126plusQoSMTypeTOSPriority": es2126plusQoSMTypeTOSPriority,
       "es2126plusQoSMTypeTOSPriorityTable": es2126plusQoSMTypeTOSPriorityTable,
       "es2126plusQoSMTypeTOSPriorityEntry": es2126plusQoSMTypeTOSPriorityEntry,
       "es2126plusQoSMTypeTOSPriorityIndex": es2126plusQoSMTypeTOSPriorityIndex,
       "es2126plusQoSMTypeTOSPriorityValue": es2126plusQoSMTypeTOSPriorityValue,
       "es2126plusQoSMTypeTOSPriorityQueue": es2126plusQoSMTypeTOSPriorityQueue,
       "es2126plusQoSDSCPPriority": es2126plusQoSDSCPPriority,
       "es2126plusQoSDSCPPriorityTable": es2126plusQoSDSCPPriorityTable,
       "es2126plusQoSDSCPPriorityEntry": es2126plusQoSDSCPPriorityEntry,
       "es2126plusQoSDSCPPriorityIndex": es2126plusQoSDSCPPriorityIndex,
       "es2126plusQoSDSCPPriorityValue": es2126plusQoSDSCPPriorityValue,
       "es2126plusQoSDSCPPriorityQueue": es2126plusQoSDSCPPriorityQueue,
       "es2126plusVlan": es2126plusVlan,
       "es2126plusVlanModeConfig": es2126plusVlanModeConfig,
       "es2126plusVlanMode": es2126plusVlanMode,
       "es2126plusSymmetricVlan": es2126plusSymmetricVlan,
       "es2126plusVlanSVL": es2126plusVlanSVL,
       "es2126plusDoubleTag": es2126plusDoubleTag,
       "es2126plusUpLinkPort": es2126plusUpLinkPort,
       "es2126plusTagBasedVlanGroup": es2126plusTagBasedVlanGroup,
       "es2126plusTagBasedVlanNumbers": es2126plusTagBasedVlanNumbers,
       "es2126plusTagBasedCreateStatus": es2126plusTagBasedCreateStatus,
       "es2126plusTagBasedVlanTable": es2126plusTagBasedVlanTable,
       "es2126plusTagBasedVlanEntry": es2126plusTagBasedVlanEntry,
       "es2126plusTagBasedVlanVid": es2126plusTagBasedVlanVid,
       "es2126plusTagBasedVlanName": es2126plusTagBasedVlanName,
       "es2126plusTagBasedVlanMember": es2126plusTagBasedVlanMember,
       "es2126plusTagBasedVlanUntag": es2126plusTagBasedVlanUntag,
       "es2126plusTagBasedVlanRowStatus": es2126plusTagBasedVlanRowStatus,
       "es2126plusVlanPvid": es2126plusVlanPvid,
       "es2126plusVlanPvidTable": es2126plusVlanPvidTable,
       "es2126plusVlanPvidEntry": es2126plusVlanPvidEntry,
       "es2126plusVlanPvidPort": es2126plusVlanPvidPort,
       "es2126plusVlanPvidValue": es2126plusVlanPvidValue,
       "es2126plusVlanPvidDefaultPriority": es2126plusVlanPvidDefaultPriority,
       "es2126plusVlanPvidDropUntag": es2126plusVlanPvidDropUntag,
       "es2126plusPortBasedVlanGroup": es2126plusPortBasedVlanGroup,
       "es2126plusPortBasedVlanNumbers": es2126plusPortBasedVlanNumbers,
       "es2126plusPortBasedCreateStatus": es2126plusPortBasedCreateStatus,
       "es2126plusPortBasedVlanTable": es2126plusPortBasedVlanTable,
       "es2126plusPortBasedVlanEntry": es2126plusPortBasedVlanEntry,
       "es2126plusPortBasedVlanIndex": es2126plusPortBasedVlanIndex,
       "es2126plusPortBasedVlanName": es2126plusPortBasedVlanName,
       "es2126plusPortBasedVlanMember": es2126plusPortBasedVlanMember,
       "es2126plusPortBasedVlanRowStatus": es2126plusPortBasedVlanRowStatus,
       "es2126plusManagementVlan": es2126plusManagementVlan,
       "es2126plusManagementVlanState": es2126plusManagementVlanState,
       "es2126plusManagementVlanVid": es2126plusManagementVlanVid,
       "es2126plusDot1X": es2126plusDot1X,
       "es2126plusDot1XStateSetting": es2126plusDot1XStateSetting,
       "es2126plusRadiusServer": es2126plusRadiusServer,
       "es2126plusDot1XPort": es2126plusDot1XPort,
       "es2126plusSecretKey": es2126plusSecretKey,
       "es2126plusAccountingService": es2126plusAccountingService,
       "es2126plusAccountingServer": es2126plusAccountingServer,
       "es2126plusAccountingPort": es2126plusAccountingPort,
       "es2126plusDot1XPortSecurityManagement": es2126plusDot1XPortSecurityManagement,
       "es2126plusDot1XPortSecurityTable": es2126plusDot1XPortSecurityTable,
       "es2126plusDot1XPortSecurityEntry": es2126plusDot1XPortSecurityEntry,
       "es2126plusDot1XPortSecurityPortIndex": es2126plusDot1XPortSecurityPortIndex,
       "es2126plusDot1XPortSecurityMode": es2126plusDot1XPortSecurityMode,
       "es2126plusDot1XPortSecurityPortControl": es2126plusDot1XPortSecurityPortControl,
       "es2126plusDot1XPortSecurityReAuthMax": es2126plusDot1XPortSecurityReAuthMax,
       "es2126plusDot1XPortSecurityTxPeriod": es2126plusDot1XPortSecurityTxPeriod,
       "es2126plusDot1XPortSecurityQuietPeriod": es2126plusDot1XPortSecurityQuietPeriod,
       "es2126plusDot1XPortSecurityReAuthEnabled": es2126plusDot1XPortSecurityReAuthEnabled,
       "es2126plusDot1XPortSecurityReAuthPeriod": es2126plusDot1XPortSecurityReAuthPeriod,
       "es2126plusDot1XPortSecurityMaxRequest": es2126plusDot1XPortSecurityMaxRequest,
       "es2126plusDot1XPortSecuritySuppTimeout": es2126plusDot1XPortSecuritySuppTimeout,
       "es2126plusDot1XPortSecurityServerTimeout": es2126plusDot1XPortSecurityServerTimeout,
       "es2126plusDot1XPortSecurityStatus": es2126plusDot1XPortSecurityStatus,
       "es2126plusTrunkInfo": es2126plusTrunkInfo,
       "es2126plusTrunkPort": es2126plusTrunkPort,
       "es2126plusTrunkPortTable": es2126plusTrunkPortTable,
       "es2126plusTrunkPortEntry": es2126plusTrunkPortEntry,
       "es2126plusTrunkPortIndex": es2126plusTrunkPortIndex,
       "es2126plusTrunkPortMethod": es2126plusTrunkPortMethod,
       "es2126plusTrunkPortGroup": es2126plusTrunkPortGroup,
       "es2126plusTrunkPortActiveLacp": es2126plusTrunkPortActiveLacp,
       "es2126plusTrunkPortAggtr": es2126plusTrunkPortAggtr,
       "es2126plusTrunkPortStatus": es2126plusTrunkPortStatus,
       "es2126plusTrunkPortCurrentMode": es2126plusTrunkPortCurrentMode,
       "es2126plusAggregatorView": es2126plusAggregatorView,
       "es2126plusAggregatorViewTable": es2126plusAggregatorViewTable,
       "es2126plusAggregatorViewEntry": es2126plusAggregatorViewEntry,
       "es2126plusAggregatorViewIndex": es2126plusAggregatorViewIndex,
       "es2126plusAggregatorViewMethod": es2126plusAggregatorViewMethod,
       "es2126plusAggregatorViewMemberPorts": es2126plusAggregatorViewMemberPorts,
       "es2126plusAggregatorViewReadyPorts": es2126plusAggregatorViewReadyPorts,
       "es2126plusLacpSystemConfiguration": es2126plusLacpSystemConfiguration,
       "es2126plusLacpSystemPriority": es2126plusLacpSystemPriority,
       "es2126plusLacpSystemHashMethod": es2126plusLacpSystemHashMethod,
       "es2126plusTrapEntry": es2126plusTrapEntry,
       "es2126plusModuleInserted": es2126plusModuleInserted,
       "es2126plusModuleRemoved": es2126plusModuleRemoved,
       "es2126plusDualMediaSwapped": es2126plusDualMediaSwapped,
       "es2126plusLoopDetected": es2126plusLoopDetected,
       "es2126plusLoginProtected": es2126plusLoginProtected,
       "es2126plusStpStateDisabled": es2126plusStpStateDisabled,
       "es2126plusStpStateEnabled": es2126plusStpStateEnabled,
       "es2126plusStpTopologyChanged": es2126plusStpTopologyChanged,
       "es2126plusRmonRisingAlarm": es2126plusRmonRisingAlarm,
       "es2126plusRmonFallingAlarm": es2126plusRmonFallingAlarm,
       "es2126plusLacpStateDisabled": es2126plusLacpStateDisabled,
       "es2126plusLacpStateEnabled": es2126plusLacpStateEnabled,
       "es2126plusLacpPortAdded": es2126plusLacpPortAdded,
       "es2126plusLacpPortTrunkFailure": es2126plusLacpPortTrunkFailure,
       "es2126plusGvrpStateDisabled": es2126plusGvrpStateDisabled,
       "es2126plusGvrpStateEnabled": es2126plusGvrpStateEnabled,
       "es2126plusVlanPortBaseEnabled": es2126plusVlanPortBaseEnabled,
       "es2126plusVlanTagBaseEnabled": es2126plusVlanTagBaseEnabled,
       "es2126plusVlanMetroBaseEnabled": es2126plusVlanMetroBaseEnabled,
       "es2126plusUserLogin": es2126plusUserLogin,
       "es2126plusUserLogout": es2126plusUserLogout,
       "es2126plusTrapVariable": es2126plusTrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink,
       "loginProtectInfo": loginProtectInfo,
       "es2126plusLoginProtect": es2126plusLoginProtect,
       "es2126plusLockTime": es2126plusLockTime,
       "es2126plusErrorCount": es2126plusErrorCount}
)
