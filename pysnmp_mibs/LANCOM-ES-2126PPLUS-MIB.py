# SNMP MIB module (LANCOM-ES-2126PPLUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-ES-2126PPLUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:01 2025
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
_LancomES2126P_ObjectIdentity = ObjectIdentity
lancomES2126P = _LancomES2126P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129)
)
_Es2126PoEplusProduces_ObjectIdentity = ObjectIdentity
es2126PoEplusProduces = _Es2126PoEplusProduces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1)
)
_Es2126PoEplusSystem_ObjectIdentity = ObjectIdentity
es2126PoEplusSystem = _Es2126PoEplusSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1)
)
_Es2126PoEplusCommonSys_ObjectIdentity = ObjectIdentity
es2126PoEplusCommonSys = _Es2126PoEplusCommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1)
)


class _Es2126PoEplusReboot_Type(Integer32):
    """Custom type es2126PoEplusReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126PoEplusReboot_Type.__name__ = "Integer32"
_Es2126PoEplusReboot_Object = MibScalar
es2126PoEplusReboot = _Es2126PoEplusReboot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 1),
    _Es2126PoEplusReboot_Type()
)
es2126PoEplusReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusReboot.setStatus("current")
_Es2126PoEplusBiosVsersion_Type = DisplayString
_Es2126PoEplusBiosVsersion_Object = MibScalar
es2126PoEplusBiosVsersion = _Es2126PoEplusBiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 2),
    _Es2126PoEplusBiosVsersion_Type()
)
es2126PoEplusBiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusBiosVsersion.setStatus("current")
_Es2126PoEplusFirmwareVersion_Type = DisplayString
_Es2126PoEplusFirmwareVersion_Object = MibScalar
es2126PoEplusFirmwareVersion = _Es2126PoEplusFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 3),
    _Es2126PoEplusFirmwareVersion_Type()
)
es2126PoEplusFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusFirmwareVersion.setStatus("current")
_Es2126PoEplusHardwareVersion_Type = DisplayString
_Es2126PoEplusHardwareVersion_Object = MibScalar
es2126PoEplusHardwareVersion = _Es2126PoEplusHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 4),
    _Es2126PoEplusHardwareVersion_Type()
)
es2126PoEplusHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusHardwareVersion.setStatus("current")
_Es2126PoEplusMechanicalVersion_Type = DisplayString
_Es2126PoEplusMechanicalVersion_Object = MibScalar
es2126PoEplusMechanicalVersion = _Es2126PoEplusMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 5),
    _Es2126PoEplusMechanicalVersion_Type()
)
es2126PoEplusMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusMechanicalVersion.setStatus("current")
_Es2126PoEplusSerialNumber_Type = DisplayString
_Es2126PoEplusSerialNumber_Object = MibScalar
es2126PoEplusSerialNumber = _Es2126PoEplusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 6),
    _Es2126PoEplusSerialNumber_Type()
)
es2126PoEplusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusSerialNumber.setStatus("current")
_Es2126PoEplusHostMacAddress_Type = DisplayString
_Es2126PoEplusHostMacAddress_Object = MibScalar
es2126PoEplusHostMacAddress = _Es2126PoEplusHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 7),
    _Es2126PoEplusHostMacAddress_Type()
)
es2126PoEplusHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusHostMacAddress.setStatus("current")
_Es2126PoEplusDevicePort_Type = DisplayString
_Es2126PoEplusDevicePort_Object = MibScalar
es2126PoEplusDevicePort = _Es2126PoEplusDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 8),
    _Es2126PoEplusDevicePort_Type()
)
es2126PoEplusDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusDevicePort.setStatus("current")
_Es2126PoEplusRamSize_Type = DisplayString
_Es2126PoEplusRamSize_Object = MibScalar
es2126PoEplusRamSize = _Es2126PoEplusRamSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 9),
    _Es2126PoEplusRamSize_Type()
)
es2126PoEplusRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusRamSize.setStatus("current")
_Es2126PoEplusFlashSize_Type = DisplayString
_Es2126PoEplusFlashSize_Object = MibScalar
es2126PoEplusFlashSize = _Es2126PoEplusFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 10),
    _Es2126PoEplusFlashSize_Type()
)
es2126PoEplusFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusFlashSize.setStatus("current")
_Es2126PoEplusSystemDescription_Type = DisplayString
_Es2126PoEplusSystemDescription_Object = MibScalar
es2126PoEplusSystemDescription = _Es2126PoEplusSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 11),
    _Es2126PoEplusSystemDescription_Type()
)
es2126PoEplusSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusSystemDescription.setStatus("current")
_Es2126PoEplusDeviceName_Type = DisplayString
_Es2126PoEplusDeviceName_Object = MibScalar
es2126PoEplusDeviceName = _Es2126PoEplusDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 1, 12),
    _Es2126PoEplusDeviceName_Type()
)
es2126PoEplusDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDeviceName.setStatus("current")
_Es2126PoEplusIP_ObjectIdentity = ObjectIdentity
es2126PoEplusIP = _Es2126PoEplusIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2)
)


class _Es2126PoEplusDhcpSetting_Type(Integer32):
    """Custom type es2126PoEplusDhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusDhcpSetting_Type.__name__ = "Integer32"
_Es2126PoEplusDhcpSetting_Object = MibScalar
es2126PoEplusDhcpSetting = _Es2126PoEplusDhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2, 1),
    _Es2126PoEplusDhcpSetting_Type()
)
es2126PoEplusDhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDhcpSetting.setStatus("current")
_Es2126PoEplusIPAddress_Type = IpAddress
_Es2126PoEplusIPAddress_Object = MibScalar
es2126PoEplusIPAddress = _Es2126PoEplusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2, 2),
    _Es2126PoEplusIPAddress_Type()
)
es2126PoEplusIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusIPAddress.setStatus("current")
_Es2126PoEplusNetMask_Type = IpAddress
_Es2126PoEplusNetMask_Object = MibScalar
es2126PoEplusNetMask = _Es2126PoEplusNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2, 3),
    _Es2126PoEplusNetMask_Type()
)
es2126PoEplusNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusNetMask.setStatus("current")
_Es2126PoEplusDefaultGateway_Type = IpAddress
_Es2126PoEplusDefaultGateway_Object = MibScalar
es2126PoEplusDefaultGateway = _Es2126PoEplusDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2, 4),
    _Es2126PoEplusDefaultGateway_Type()
)
es2126PoEplusDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDefaultGateway.setStatus("current")


class _Es2126PoEplusDnsSetting_Type(Integer32):
    """Custom type es2126PoEplusDnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusDnsSetting_Type.__name__ = "Integer32"
_Es2126PoEplusDnsSetting_Object = MibScalar
es2126PoEplusDnsSetting = _Es2126PoEplusDnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2, 5),
    _Es2126PoEplusDnsSetting_Type()
)
es2126PoEplusDnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDnsSetting.setStatus("current")
_Es2126PoEplusDnsServer_Type = IpAddress
_Es2126PoEplusDnsServer_Object = MibScalar
es2126PoEplusDnsServer = _Es2126PoEplusDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 2, 6),
    _Es2126PoEplusDnsServer_Type()
)
es2126PoEplusDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDnsServer.setStatus("current")
_Es2126PoEplusTime_ObjectIdentity = ObjectIdentity
es2126PoEplusTime = _Es2126PoEplusTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3)
)
_Es2126PoEplusSystemCurrentTime_Type = DisplayString
_Es2126PoEplusSystemCurrentTime_Object = MibScalar
es2126PoEplusSystemCurrentTime = _Es2126PoEplusSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 1),
    _Es2126PoEplusSystemCurrentTime_Type()
)
es2126PoEplusSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusSystemCurrentTime.setStatus("current")
_Es2126PoEplusManualTimeSetting_Type = DisplayString
_Es2126PoEplusManualTimeSetting_Object = MibScalar
es2126PoEplusManualTimeSetting = _Es2126PoEplusManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 2),
    _Es2126PoEplusManualTimeSetting_Type()
)
es2126PoEplusManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManualTimeSetting.setStatus("current")
_Es2126PoEplusNTPServer_Type = DisplayString
_Es2126PoEplusNTPServer_Object = MibScalar
es2126PoEplusNTPServer = _Es2126PoEplusNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 3),
    _Es2126PoEplusNTPServer_Type()
)
es2126PoEplusNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusNTPServer.setStatus("current")


class _Es2126PoEplusNTPTimeZone_Type(Integer32):
    """Custom type es2126PoEplusNTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Es2126PoEplusNTPTimeZone_Type.__name__ = "Integer32"
_Es2126PoEplusNTPTimeZone_Object = MibScalar
es2126PoEplusNTPTimeZone = _Es2126PoEplusNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 4),
    _Es2126PoEplusNTPTimeZone_Type()
)
es2126PoEplusNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusNTPTimeZone.setStatus("current")


class _Es2126PoEplusNTPTimeSync_Type(Integer32):
    """Custom type es2126PoEplusNTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusNTPTimeSync_Type.__name__ = "Integer32"
_Es2126PoEplusNTPTimeSync_Object = MibScalar
es2126PoEplusNTPTimeSync = _Es2126PoEplusNTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 5),
    _Es2126PoEplusNTPTimeSync_Type()
)
es2126PoEplusNTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusNTPTimeSync.setStatus("current")


class _Es2126PoEplusDaylightSavingTime_Type(Integer32):
    """Custom type es2126PoEplusDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Es2126PoEplusDaylightSavingTime_Type.__name__ = "Integer32"
_Es2126PoEplusDaylightSavingTime_Object = MibScalar
es2126PoEplusDaylightSavingTime = _Es2126PoEplusDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 6),
    _Es2126PoEplusDaylightSavingTime_Type()
)
es2126PoEplusDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDaylightSavingTime.setStatus("current")
_Es2126PoEplusDaylightStartTime_Type = DisplayString
_Es2126PoEplusDaylightStartTime_Object = MibScalar
es2126PoEplusDaylightStartTime = _Es2126PoEplusDaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 7),
    _Es2126PoEplusDaylightStartTime_Type()
)
es2126PoEplusDaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDaylightStartTime.setStatus("current")
_Es2126PoEplusDaylightEndTime_Type = DisplayString
_Es2126PoEplusDaylightEndTime_Object = MibScalar
es2126PoEplusDaylightEndTime = _Es2126PoEplusDaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 3, 8),
    _Es2126PoEplusDaylightEndTime_Type()
)
es2126PoEplusDaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDaylightEndTime.setStatus("current")
_Es2126PoEplusAccount_ObjectIdentity = ObjectIdentity
es2126PoEplusAccount = _Es2126PoEplusAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4)
)


class _Es2126PoEplusAccountNumber_Type(Integer32):
    """Custom type es2126PoEplusAccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2126PoEplusAccountNumber_Type.__name__ = "Integer32"
_Es2126PoEplusAccountNumber_Object = MibScalar
es2126PoEplusAccountNumber = _Es2126PoEplusAccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 1),
    _Es2126PoEplusAccountNumber_Type()
)
es2126PoEplusAccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusAccountNumber.setStatus("current")
_Es2126PoEplusAccountTable_Object = MibTable
es2126PoEplusAccountTable = _Es2126PoEplusAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusAccountTable.setStatus("current")
_Es2126PoEplusAccountEntry_Object = MibTableRow
es2126PoEplusAccountEntry = _Es2126PoEplusAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 2, 1)
)
es2126PoEplusAccountEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusAccountIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusAccountEntry.setStatus("current")


class _Es2126PoEplusAccountIndex_Type(Integer32):
    """Custom type es2126PoEplusAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Es2126PoEplusAccountIndex_Type.__name__ = "Integer32"
_Es2126PoEplusAccountIndex_Object = MibTableColumn
es2126PoEplusAccountIndex = _Es2126PoEplusAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 2, 1, 1),
    _Es2126PoEplusAccountIndex_Type()
)
es2126PoEplusAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusAccountIndex.setStatus("current")
_Es2126PoEplusAccountAuthorization_Type = DisplayString
_Es2126PoEplusAccountAuthorization_Object = MibTableColumn
es2126PoEplusAccountAuthorization = _Es2126PoEplusAccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 2, 1, 2),
    _Es2126PoEplusAccountAuthorization_Type()
)
es2126PoEplusAccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusAccountAuthorization.setStatus("current")
_Es2126PoEplusAccountName_Type = DisplayString
_Es2126PoEplusAccountName_Object = MibTableColumn
es2126PoEplusAccountName = _Es2126PoEplusAccountName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 2, 1, 3),
    _Es2126PoEplusAccountName_Type()
)
es2126PoEplusAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountName.setStatus("current")
_Es2126PoEplusAccountPassword_Type = DisplayString
_Es2126PoEplusAccountPassword_Object = MibTableColumn
es2126PoEplusAccountPassword = _Es2126PoEplusAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 2, 1, 4),
    _Es2126PoEplusAccountPassword_Type()
)
es2126PoEplusAccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountPassword.setStatus("current")
_Es2126PoEplusAccountAddName_Type = DisplayString
_Es2126PoEplusAccountAddName_Object = MibScalar
es2126PoEplusAccountAddName = _Es2126PoEplusAccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 3),
    _Es2126PoEplusAccountAddName_Type()
)
es2126PoEplusAccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountAddName.setStatus("current")
_Es2126PoEplusAccountAddPassword_Type = DisplayString
_Es2126PoEplusAccountAddPassword_Object = MibScalar
es2126PoEplusAccountAddPassword = _Es2126PoEplusAccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 4),
    _Es2126PoEplusAccountAddPassword_Type()
)
es2126PoEplusAccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountAddPassword.setStatus("current")


class _Es2126PoEplusDoAccountAdd_Type(Integer32):
    """Custom type es2126PoEplusDoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusDoAccountAdd_Type.__name__ = "Integer32"
_Es2126PoEplusDoAccountAdd_Object = MibScalar
es2126PoEplusDoAccountAdd = _Es2126PoEplusDoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 5),
    _Es2126PoEplusDoAccountAdd_Type()
)
es2126PoEplusDoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDoAccountAdd.setStatus("current")


class _Es2126PoEplusAccountDel_Type(Integer32):
    """Custom type es2126PoEplusAccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Es2126PoEplusAccountDel_Type.__name__ = "Integer32"
_Es2126PoEplusAccountDel_Object = MibScalar
es2126PoEplusAccountDel = _Es2126PoEplusAccountDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 1, 4, 6),
    _Es2126PoEplusAccountDel_Type()
)
es2126PoEplusAccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountDel.setStatus("current")
_Es2126PoEplusSnmp_ObjectIdentity = ObjectIdentity
es2126PoEplusSnmp = _Es2126PoEplusSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2)
)
_Es2126PoEplusGetCommunity_Type = DisplayString
_Es2126PoEplusGetCommunity_Object = MibScalar
es2126PoEplusGetCommunity = _Es2126PoEplusGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 1),
    _Es2126PoEplusGetCommunity_Type()
)
es2126PoEplusGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGetCommunity.setStatus("current")
_Es2126PoEplusSetCommunity_Type = DisplayString
_Es2126PoEplusSetCommunity_Object = MibScalar
es2126PoEplusSetCommunity = _Es2126PoEplusSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 2),
    _Es2126PoEplusSetCommunity_Type()
)
es2126PoEplusSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusSetCommunity.setStatus("current")


class _Es2126PoEplusTrapHostNumber_Type(Integer32):
    """Custom type es2126PoEplusTrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126PoEplusTrapHostNumber_Type.__name__ = "Integer32"
_Es2126PoEplusTrapHostNumber_Object = MibScalar
es2126PoEplusTrapHostNumber = _Es2126PoEplusTrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 3),
    _Es2126PoEplusTrapHostNumber_Type()
)
es2126PoEplusTrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostNumber.setStatus("current")
_Es2126PoEplusTrapHostTable_Object = MibTable
es2126PoEplusTrapHostTable = _Es2126PoEplusTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 4)
)
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostTable.setStatus("current")
_Es2126PoEplusTrapHostEntry_Object = MibTableRow
es2126PoEplusTrapHostEntry = _Es2126PoEplusTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 4, 1)
)
es2126PoEplusTrapHostEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusTrapHostIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostEntry.setStatus("current")


class _Es2126PoEplusTrapHostIndex_Type(Integer32):
    """Custom type es2126PoEplusTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126PoEplusTrapHostIndex_Type.__name__ = "Integer32"
_Es2126PoEplusTrapHostIndex_Object = MibTableColumn
es2126PoEplusTrapHostIndex = _Es2126PoEplusTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 4, 1, 1),
    _Es2126PoEplusTrapHostIndex_Type()
)
es2126PoEplusTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostIndex.setStatus("current")
_Es2126PoEplusTrapHostIP_Type = IpAddress
_Es2126PoEplusTrapHostIP_Object = MibTableColumn
es2126PoEplusTrapHostIP = _Es2126PoEplusTrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 4, 1, 2),
    _Es2126PoEplusTrapHostIP_Type()
)
es2126PoEplusTrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostIP.setStatus("current")


class _Es2126PoEplusTrapHostPort_Type(Integer32):
    """Custom type es2126PoEplusTrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusTrapHostPort_Type.__name__ = "Integer32"
_Es2126PoEplusTrapHostPort_Object = MibTableColumn
es2126PoEplusTrapHostPort = _Es2126PoEplusTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 4, 1, 3),
    _Es2126PoEplusTrapHostPort_Type()
)
es2126PoEplusTrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostPort.setStatus("current")
_Es2126PoEplusTrapHostCommunity_Type = DisplayString
_Es2126PoEplusTrapHostCommunity_Object = MibTableColumn
es2126PoEplusTrapHostCommunity = _Es2126PoEplusTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 4, 1, 4),
    _Es2126PoEplusTrapHostCommunity_Type()
)
es2126PoEplusTrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrapHostCommunity.setStatus("current")
_Es2126PoEplusRegisterMonitor_Type = DisplayString
_Es2126PoEplusRegisterMonitor_Object = MibScalar
es2126PoEplusRegisterMonitor = _Es2126PoEplusRegisterMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 5),
    _Es2126PoEplusRegisterMonitor_Type()
)
es2126PoEplusRegisterMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRegisterMonitor.setStatus("current")
_Es2126PoEplusDeleteMonitor_Type = DisplayString
_Es2126PoEplusDeleteMonitor_Object = MibScalar
es2126PoEplusDeleteMonitor = _Es2126PoEplusDeleteMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 6),
    _Es2126PoEplusDeleteMonitor_Type()
)
es2126PoEplusDeleteMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDeleteMonitor.setStatus("current")
_Es2126PoEplusMonitorTable_Object = MibTable
es2126PoEplusMonitorTable = _Es2126PoEplusMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 7)
)
if mibBuilder.loadTexts:
    es2126PoEplusMonitorTable.setStatus("current")
_Es2126PoEplusMonitorEntry_Object = MibTableRow
es2126PoEplusMonitorEntry = _Es2126PoEplusMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 7, 1)
)
es2126PoEplusMonitorEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusMonitorTableIp"),
)
if mibBuilder.loadTexts:
    es2126PoEplusMonitorEntry.setStatus("current")
_Es2126PoEplusMonitorTableIp_Type = IpAddress
_Es2126PoEplusMonitorTableIp_Object = MibTableColumn
es2126PoEplusMonitorTableIp = _Es2126PoEplusMonitorTableIp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 7, 1, 1),
    _Es2126PoEplusMonitorTableIp_Type()
)
es2126PoEplusMonitorTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusMonitorTableIp.setStatus("current")
_Es2126PoEplusMonitorTableMac_Type = DisplayString
_Es2126PoEplusMonitorTableMac_Object = MibTableColumn
es2126PoEplusMonitorTableMac = _Es2126PoEplusMonitorTableMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 7, 1, 2),
    _Es2126PoEplusMonitorTableMac_Type()
)
es2126PoEplusMonitorTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusMonitorTableMac.setStatus("current")


class _Es2126PoEplusTrapBootDelayTime_Type(Integer32):
    """Custom type es2126PoEplusTrapBootDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2126PoEplusTrapBootDelayTime_Type.__name__ = "Integer32"
_Es2126PoEplusTrapBootDelayTime_Object = MibScalar
es2126PoEplusTrapBootDelayTime = _Es2126PoEplusTrapBootDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 2, 8),
    _Es2126PoEplusTrapBootDelayTime_Type()
)
es2126PoEplusTrapBootDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrapBootDelayTime.setStatus("current")
_Es2126PoEplusAlarm_ObjectIdentity = ObjectIdentity
es2126PoEplusAlarm = _Es2126PoEplusAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3)
)
_Es2126PoEplusEvent_ObjectIdentity = ObjectIdentity
es2126PoEplusEvent = _Es2126PoEplusEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1)
)


class _Es2126PoEplusEventNumber_Type(Integer32):
    """Custom type es2126PoEplusEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusEventNumber_Type.__name__ = "Integer32"
_Es2126PoEplusEventNumber_Object = MibScalar
es2126PoEplusEventNumber = _Es2126PoEplusEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 1),
    _Es2126PoEplusEventNumber_Type()
)
es2126PoEplusEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusEventNumber.setStatus("current")
_Es2126PoEplusEventTable_Object = MibTable
es2126PoEplusEventTable = _Es2126PoEplusEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusEventTable.setStatus("current")
_Es2126PoEplusEventEntry_Object = MibTableRow
es2126PoEplusEventEntry = _Es2126PoEplusEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 2, 1)
)
es2126PoEplusEventEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusEventIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusEventEntry.setStatus("current")


class _Es2126PoEplusEventIndex_Type(Integer32):
    """Custom type es2126PoEplusEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusEventIndex_Type.__name__ = "Integer32"
_Es2126PoEplusEventIndex_Object = MibTableColumn
es2126PoEplusEventIndex = _Es2126PoEplusEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 2, 1, 1),
    _Es2126PoEplusEventIndex_Type()
)
es2126PoEplusEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusEventIndex.setStatus("current")
_Es2126PoEplusEventName_Type = DisplayString
_Es2126PoEplusEventName_Object = MibTableColumn
es2126PoEplusEventName = _Es2126PoEplusEventName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 2, 1, 2),
    _Es2126PoEplusEventName_Type()
)
es2126PoEplusEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusEventName.setStatus("current")


class _Es2126PoEplusEventSendEmail_Type(Integer32):
    """Custom type es2126PoEplusEventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusEventSendEmail_Type.__name__ = "Integer32"
_Es2126PoEplusEventSendEmail_Object = MibTableColumn
es2126PoEplusEventSendEmail = _Es2126PoEplusEventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 2, 1, 3),
    _Es2126PoEplusEventSendEmail_Type()
)
es2126PoEplusEventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEventSendEmail.setStatus("current")


class _Es2126PoEplusEventSendTrap_Type(Integer32):
    """Custom type es2126PoEplusEventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusEventSendTrap_Type.__name__ = "Integer32"
_Es2126PoEplusEventSendTrap_Object = MibTableColumn
es2126PoEplusEventSendTrap = _Es2126PoEplusEventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 1, 2, 1, 4),
    _Es2126PoEplusEventSendTrap_Type()
)
es2126PoEplusEventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEventSendTrap.setStatus("current")
_Es2126PoEplusEmail_ObjectIdentity = ObjectIdentity
es2126PoEplusEmail = _Es2126PoEplusEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2)
)
_Es2126PoEplusEmailServer_Type = DisplayString
_Es2126PoEplusEmailServer_Object = MibScalar
es2126PoEplusEmailServer = _Es2126PoEplusEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 1),
    _Es2126PoEplusEmailServer_Type()
)
es2126PoEplusEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEmailServer.setStatus("current")
_Es2126PoEplusEmailUsername_Type = DisplayString
_Es2126PoEplusEmailUsername_Object = MibScalar
es2126PoEplusEmailUsername = _Es2126PoEplusEmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 2),
    _Es2126PoEplusEmailUsername_Type()
)
es2126PoEplusEmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEmailUsername.setStatus("current")
_Es2126PoEplusEmailPassword_Type = DisplayString
_Es2126PoEplusEmailPassword_Object = MibScalar
es2126PoEplusEmailPassword = _Es2126PoEplusEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 3),
    _Es2126PoEplusEmailPassword_Type()
)
es2126PoEplusEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEmailPassword.setStatus("current")
_Es2126PoEplusEmailSender_Type = DisplayString
_Es2126PoEplusEmailSender_Object = MibScalar
es2126PoEplusEmailSender = _Es2126PoEplusEmailSender_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 4),
    _Es2126PoEplusEmailSender_Type()
)
es2126PoEplusEmailSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEmailSender.setStatus("current")
_Es2126PoEplusEmailReturnPath_Type = DisplayString
_Es2126PoEplusEmailReturnPath_Object = MibScalar
es2126PoEplusEmailReturnPath = _Es2126PoEplusEmailReturnPath_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 5),
    _Es2126PoEplusEmailReturnPath_Type()
)
es2126PoEplusEmailReturnPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEmailReturnPath.setStatus("current")


class _Es2126PoEplusEmailUserNumber_Type(Integer32):
    """Custom type es2126PoEplusEmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126PoEplusEmailUserNumber_Type.__name__ = "Integer32"
_Es2126PoEplusEmailUserNumber_Object = MibScalar
es2126PoEplusEmailUserNumber = _Es2126PoEplusEmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 6),
    _Es2126PoEplusEmailUserNumber_Type()
)
es2126PoEplusEmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusEmailUserNumber.setStatus("current")
_Es2126PoEplusEmailUserTable_Object = MibTable
es2126PoEplusEmailUserTable = _Es2126PoEplusEmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    es2126PoEplusEmailUserTable.setStatus("current")
_Es2126PoEplusEmailUserEntry_Object = MibTableRow
es2126PoEplusEmailUserEntry = _Es2126PoEplusEmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 7, 1)
)
es2126PoEplusEmailUserEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusEmailUserIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusEmailUserEntry.setStatus("current")


class _Es2126PoEplusEmailUserIndex_Type(Integer32):
    """Custom type es2126PoEplusEmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Es2126PoEplusEmailUserIndex_Type.__name__ = "Integer32"
_Es2126PoEplusEmailUserIndex_Object = MibTableColumn
es2126PoEplusEmailUserIndex = _Es2126PoEplusEmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 7, 1, 1),
    _Es2126PoEplusEmailUserIndex_Type()
)
es2126PoEplusEmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusEmailUserIndex.setStatus("current")
_Es2126PoEplusEmailUserAddress_Type = DisplayString
_Es2126PoEplusEmailUserAddress_Object = MibTableColumn
es2126PoEplusEmailUserAddress = _Es2126PoEplusEmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 3, 2, 7, 1, 2),
    _Es2126PoEplusEmailUserAddress_Type()
)
es2126PoEplusEmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusEmailUserAddress.setStatus("current")
_Es2126PoEplusTftp_ObjectIdentity = ObjectIdentity
es2126PoEplusTftp = _Es2126PoEplusTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 4)
)
_Es2126PoEplusRemoteTftpServer_Type = IpAddress
_Es2126PoEplusRemoteTftpServer_Object = MibScalar
es2126PoEplusRemoteTftpServer = _Es2126PoEplusRemoteTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 4, 1),
    _Es2126PoEplusRemoteTftpServer_Type()
)
es2126PoEplusRemoteTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRemoteTftpServer.setStatus("current")


class _Es2126PoEplusInternalTftpServerState_Type(Integer32):
    """Custom type es2126PoEplusInternalTftpServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusInternalTftpServerState_Type.__name__ = "Integer32"
_Es2126PoEplusInternalTftpServerState_Object = MibScalar
es2126PoEplusInternalTftpServerState = _Es2126PoEplusInternalTftpServerState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 4, 2),
    _Es2126PoEplusInternalTftpServerState_Type()
)
es2126PoEplusInternalTftpServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusInternalTftpServerState.setStatus("current")
_Es2126PoEplusConfiguration_ObjectIdentity = ObjectIdentity
es2126PoEplusConfiguration = _Es2126PoEplusConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5)
)
_Es2126PoEplusSaveRestore_ObjectIdentity = ObjectIdentity
es2126PoEplusSaveRestore = _Es2126PoEplusSaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 1)
)


class _Es2126PoEplusSaveStart_Type(Integer32):
    """Custom type es2126PoEplusSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusSaveStart_Type.__name__ = "Integer32"
_Es2126PoEplusSaveStart_Object = MibScalar
es2126PoEplusSaveStart = _Es2126PoEplusSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 1, 1),
    _Es2126PoEplusSaveStart_Type()
)
es2126PoEplusSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusSaveStart.setStatus("current")


class _Es2126PoEplusSaveUser_Type(Integer32):
    """Custom type es2126PoEplusSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusSaveUser_Type.__name__ = "Integer32"
_Es2126PoEplusSaveUser_Object = MibScalar
es2126PoEplusSaveUser = _Es2126PoEplusSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 1, 2),
    _Es2126PoEplusSaveUser_Type()
)
es2126PoEplusSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusSaveUser.setStatus("current")


class _Es2126PoEplusRestoreDefault_Type(Integer32):
    """Custom type es2126PoEplusRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126PoEplusRestoreDefault_Type.__name__ = "Integer32"
_Es2126PoEplusRestoreDefault_Object = MibScalar
es2126PoEplusRestoreDefault = _Es2126PoEplusRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 1, 3),
    _Es2126PoEplusRestoreDefault_Type()
)
es2126PoEplusRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRestoreDefault.setStatus("current")


class _Es2126PoEplusRestoreUser_Type(Integer32):
    """Custom type es2126PoEplusRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusRestoreUser_Type.__name__ = "Integer32"
_Es2126PoEplusRestoreUser_Object = MibScalar
es2126PoEplusRestoreUser = _Es2126PoEplusRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 1, 4),
    _Es2126PoEplusRestoreUser_Type()
)
es2126PoEplusRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRestoreUser.setStatus("current")
_Es2126PoEplusConfigFile_ObjectIdentity = ObjectIdentity
es2126PoEplusConfigFile = _Es2126PoEplusConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 2)
)
_Es2126PoEplusExportConfigName_Type = DisplayString
_Es2126PoEplusExportConfigName_Object = MibScalar
es2126PoEplusExportConfigName = _Es2126PoEplusExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 2, 1),
    _Es2126PoEplusExportConfigName_Type()
)
es2126PoEplusExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusExportConfigName.setStatus("current")


class _Es2126PoEplusDoExportConfig_Type(Integer32):
    """Custom type es2126PoEplusDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126PoEplusDoExportConfig_Type.__name__ = "Integer32"
_Es2126PoEplusDoExportConfig_Object = MibScalar
es2126PoEplusDoExportConfig = _Es2126PoEplusDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 2, 2),
    _Es2126PoEplusDoExportConfig_Type()
)
es2126PoEplusDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDoExportConfig.setStatus("current")
_Es2126PoEplusImportConfigName_Type = DisplayString
_Es2126PoEplusImportConfigName_Object = MibScalar
es2126PoEplusImportConfigName = _Es2126PoEplusImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 2, 3),
    _Es2126PoEplusImportConfigName_Type()
)
es2126PoEplusImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusImportConfigName.setStatus("current")


class _Es2126PoEplusDoImportConfig_Type(Integer32):
    """Custom type es2126PoEplusDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126PoEplusDoImportConfig_Type.__name__ = "Integer32"
_Es2126PoEplusDoImportConfig_Object = MibScalar
es2126PoEplusDoImportConfig = _Es2126PoEplusDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 5, 2, 4),
    _Es2126PoEplusDoImportConfig_Type()
)
es2126PoEplusDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDoImportConfig.setStatus("current")
_Es2126PoEplusDiagnostic_ObjectIdentity = ObjectIdentity
es2126PoEplusDiagnostic = _Es2126PoEplusDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6)
)
_Es2126PoEplusEEPROMTest_Type = DisplayString
_Es2126PoEplusEEPROMTest_Object = MibScalar
es2126PoEplusEEPROMTest = _Es2126PoEplusEEPROMTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 1),
    _Es2126PoEplusEEPROMTest_Type()
)
es2126PoEplusEEPROMTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusEEPROMTest.setStatus("current")
_Es2126PoEplusUartTest_Type = DisplayString
_Es2126PoEplusUartTest_Object = MibScalar
es2126PoEplusUartTest = _Es2126PoEplusUartTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 2),
    _Es2126PoEplusUartTest_Type()
)
es2126PoEplusUartTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusUartTest.setStatus("current")
_Es2126PoEplusDramTest_Type = DisplayString
_Es2126PoEplusDramTest_Object = MibScalar
es2126PoEplusDramTest = _Es2126PoEplusDramTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 3),
    _Es2126PoEplusDramTest_Type()
)
es2126PoEplusDramTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusDramTest.setStatus("current")
_Es2126PoEplusFlashTest_Type = DisplayString
_Es2126PoEplusFlashTest_Object = MibScalar
es2126PoEplusFlashTest = _Es2126PoEplusFlashTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 4),
    _Es2126PoEplusFlashTest_Type()
)
es2126PoEplusFlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusFlashTest.setStatus("current")
_Es2126PoEplusInternalLoopbackTest_Type = DisplayString
_Es2126PoEplusInternalLoopbackTest_Object = MibScalar
es2126PoEplusInternalLoopbackTest = _Es2126PoEplusInternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 5),
    _Es2126PoEplusInternalLoopbackTest_Type()
)
es2126PoEplusInternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusInternalLoopbackTest.setStatus("current")
_Es2126PoEplusExternalLoopbackTest_Type = DisplayString
_Es2126PoEplusExternalLoopbackTest_Object = MibScalar
es2126PoEplusExternalLoopbackTest = _Es2126PoEplusExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 6),
    _Es2126PoEplusExternalLoopbackTest_Type()
)
es2126PoEplusExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusExternalLoopbackTest.setStatus("current")
_Es2126PoEplusPingTest_Type = DisplayString
_Es2126PoEplusPingTest_Object = MibScalar
es2126PoEplusPingTest = _Es2126PoEplusPingTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 6, 7),
    _Es2126PoEplusPingTest_Type()
)
es2126PoEplusPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPingTest.setStatus("current")
_Es2126PoEplusLog_ObjectIdentity = ObjectIdentity
es2126PoEplusLog = _Es2126PoEplusLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7)
)


class _Es2126PoEplusClearLog_Type(Integer32):
    """Custom type es2126PoEplusClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusClearLog_Type.__name__ = "Integer32"
_Es2126PoEplusClearLog_Object = MibScalar
es2126PoEplusClearLog = _Es2126PoEplusClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 1),
    _Es2126PoEplusClearLog_Type()
)
es2126PoEplusClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusClearLog.setStatus("current")


class _Es2126PoEplusUploadLog_Type(Integer32):
    """Custom type es2126PoEplusUploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusUploadLog_Type.__name__ = "Integer32"
_Es2126PoEplusUploadLog_Object = MibScalar
es2126PoEplusUploadLog = _Es2126PoEplusUploadLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 2),
    _Es2126PoEplusUploadLog_Type()
)
es2126PoEplusUploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusUploadLog.setStatus("current")


class _Es2126PoEplusAutoUploadLogState_Type(Integer32):
    """Custom type es2126PoEplusAutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusAutoUploadLogState_Type.__name__ = "Integer32"
_Es2126PoEplusAutoUploadLogState_Object = MibScalar
es2126PoEplusAutoUploadLogState = _Es2126PoEplusAutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 3),
    _Es2126PoEplusAutoUploadLogState_Type()
)
es2126PoEplusAutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAutoUploadLogState.setStatus("current")


class _Es2126PoEplusLogNumber_Type(Integer32):
    """Custom type es2126PoEplusLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Es2126PoEplusLogNumber_Type.__name__ = "Integer32"
_Es2126PoEplusLogNumber_Object = MibScalar
es2126PoEplusLogNumber = _Es2126PoEplusLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 4),
    _Es2126PoEplusLogNumber_Type()
)
es2126PoEplusLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusLogNumber.setStatus("current")
_Es2126PoEplusLogTable_Object = MibTable
es2126PoEplusLogTable = _Es2126PoEplusLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 5)
)
if mibBuilder.loadTexts:
    es2126PoEplusLogTable.setStatus("current")
_Es2126PoEplusLogEntry_Object = MibTableRow
es2126PoEplusLogEntry = _Es2126PoEplusLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 5, 1)
)
es2126PoEplusLogEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusLogIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusLogEntry.setStatus("current")


class _Es2126PoEplusLogIndex_Type(Integer32):
    """Custom type es2126PoEplusLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Es2126PoEplusLogIndex_Type.__name__ = "Integer32"
_Es2126PoEplusLogIndex_Object = MibTableColumn
es2126PoEplusLogIndex = _Es2126PoEplusLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 5, 1, 1),
    _Es2126PoEplusLogIndex_Type()
)
es2126PoEplusLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusLogIndex.setStatus("current")
_Es2126PoEplusLogEvent_Type = DisplayString
_Es2126PoEplusLogEvent_Object = MibTableColumn
es2126PoEplusLogEvent = _Es2126PoEplusLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 7, 5, 1, 2),
    _Es2126PoEplusLogEvent_Type()
)
es2126PoEplusLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusLogEvent.setStatus("current")
_Es2126PoEplusFirmware_ObjectIdentity = ObjectIdentity
es2126PoEplusFirmware = _Es2126PoEplusFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 8)
)
_Es2126PoEplusFirmwareFileName_Type = DisplayString
_Es2126PoEplusFirmwareFileName_Object = MibScalar
es2126PoEplusFirmwareFileName = _Es2126PoEplusFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 8, 1),
    _Es2126PoEplusFirmwareFileName_Type()
)
es2126PoEplusFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusFirmwareFileName.setStatus("current")


class _Es2126PoEplusDoFirmwareUpgrade_Type(Integer32):
    """Custom type es2126PoEplusDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Es2126PoEplusDoFirmwareUpgrade_Object = MibScalar
es2126PoEplusDoFirmwareUpgrade = _Es2126PoEplusDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 8, 2),
    _Es2126PoEplusDoFirmwareUpgrade_Type()
)
es2126PoEplusDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDoFirmwareUpgrade.setStatus("current")
_Es2126PoEplusPort_ObjectIdentity = ObjectIdentity
es2126PoEplusPort = _Es2126PoEplusPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9)
)
_Es2126PoEplusPortStatus_ObjectIdentity = ObjectIdentity
es2126PoEplusPortStatus = _Es2126PoEplusPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1)
)


class _Es2126PoEplusPortStatusNumber_Type(Integer32):
    """Custom type es2126PoEplusPortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusPortStatusNumber_Type.__name__ = "Integer32"
_Es2126PoEplusPortStatusNumber_Object = MibScalar
es2126PoEplusPortStatusNumber = _Es2126PoEplusPortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 1),
    _Es2126PoEplusPortStatusNumber_Type()
)
es2126PoEplusPortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusNumber.setStatus("current")
_Es2126PoEplusPortStatusTable_Object = MibTable
es2126PoEplusPortStatusTable = _Es2126PoEplusPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusTable.setStatus("current")
_Es2126PoEplusPortStatusEntry_Object = MibTableRow
es2126PoEplusPortStatusEntry = _Es2126PoEplusPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1)
)
es2126PoEplusPortStatusEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPortStatusIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusEntry.setStatus("current")


class _Es2126PoEplusPortStatusIndex_Type(Integer32):
    """Custom type es2126PoEplusPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusPortStatusIndex_Type.__name__ = "Integer32"
_Es2126PoEplusPortStatusIndex_Object = MibTableColumn
es2126PoEplusPortStatusIndex = _Es2126PoEplusPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 1),
    _Es2126PoEplusPortStatusIndex_Type()
)
es2126PoEplusPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusIndex.setStatus("current")
_Es2126PoEplusPortStatusMedia_Type = DisplayString
_Es2126PoEplusPortStatusMedia_Object = MibTableColumn
es2126PoEplusPortStatusMedia = _Es2126PoEplusPortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 2),
    _Es2126PoEplusPortStatusMedia_Type()
)
es2126PoEplusPortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusMedia.setStatus("current")
_Es2126PoEplusPortStatusLink_Type = DisplayString
_Es2126PoEplusPortStatusLink_Object = MibTableColumn
es2126PoEplusPortStatusLink = _Es2126PoEplusPortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 3),
    _Es2126PoEplusPortStatusLink_Type()
)
es2126PoEplusPortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusLink.setStatus("current")
_Es2126PoEplusPortStatusPortState_Type = DisplayString
_Es2126PoEplusPortStatusPortState_Object = MibTableColumn
es2126PoEplusPortStatusPortState = _Es2126PoEplusPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 4),
    _Es2126PoEplusPortStatusPortState_Type()
)
es2126PoEplusPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusPortState.setStatus("current")
_Es2126PoEplusPortStatusAutoNego_Type = DisplayString
_Es2126PoEplusPortStatusAutoNego_Object = MibTableColumn
es2126PoEplusPortStatusAutoNego = _Es2126PoEplusPortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 5),
    _Es2126PoEplusPortStatusAutoNego_Type()
)
es2126PoEplusPortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusAutoNego.setStatus("current")
_Es2126PoEplusPortStatusSpdDpx_Type = DisplayString
_Es2126PoEplusPortStatusSpdDpx_Object = MibTableColumn
es2126PoEplusPortStatusSpdDpx = _Es2126PoEplusPortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 6),
    _Es2126PoEplusPortStatusSpdDpx_Type()
)
es2126PoEplusPortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusSpdDpx.setStatus("current")
_Es2126PoEplusPortStatusRxPause_Type = DisplayString
_Es2126PoEplusPortStatusRxPause_Object = MibTableColumn
es2126PoEplusPortStatusRxPause = _Es2126PoEplusPortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 7),
    _Es2126PoEplusPortStatusRxPause_Type()
)
es2126PoEplusPortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusRxPause.setStatus("current")
_Es2126PoEplusPortStatusTxPause_Type = DisplayString
_Es2126PoEplusPortStatusTxPause_Object = MibTableColumn
es2126PoEplusPortStatusTxPause = _Es2126PoEplusPortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 8),
    _Es2126PoEplusPortStatusTxPause_Type()
)
es2126PoEplusPortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusTxPause.setStatus("current")
_Es2126PoEplusPortStatusDescription_Type = DisplayString
_Es2126PoEplusPortStatusDescription_Object = MibTableColumn
es2126PoEplusPortStatusDescription = _Es2126PoEplusPortStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 1, 2, 1, 9),
    _Es2126PoEplusPortStatusDescription_Type()
)
es2126PoEplusPortStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortStatusDescription.setStatus("current")
_Es2126PoEplusPortConf_ObjectIdentity = ObjectIdentity
es2126PoEplusPortConf = _Es2126PoEplusPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2)
)


class _Es2126PoEplusPortConfNumber_Type(Integer32):
    """Custom type es2126PoEplusPortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusPortConfNumber_Type.__name__ = "Integer32"
_Es2126PoEplusPortConfNumber_Object = MibScalar
es2126PoEplusPortConfNumber = _Es2126PoEplusPortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 1),
    _Es2126PoEplusPortConfNumber_Type()
)
es2126PoEplusPortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortConfNumber.setStatus("current")
_Es2126PoEplusPortConfTable_Object = MibTable
es2126PoEplusPortConfTable = _Es2126PoEplusPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusPortConfTable.setStatus("current")
_Es2126PoEplusPortConfEntry_Object = MibTableRow
es2126PoEplusPortConfEntry = _Es2126PoEplusPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2, 1)
)
es2126PoEplusPortConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPortConfIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPortConfEntry.setStatus("current")


class _Es2126PoEplusPortConfIndex_Type(Integer32):
    """Custom type es2126PoEplusPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusPortConfIndex_Type.__name__ = "Integer32"
_Es2126PoEplusPortConfIndex_Object = MibTableColumn
es2126PoEplusPortConfIndex = _Es2126PoEplusPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2, 1, 1),
    _Es2126PoEplusPortConfIndex_Type()
)
es2126PoEplusPortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortConfIndex.setStatus("current")


class _Es2126PoEplusPortConfPortState_Type(Integer32):
    """Custom type es2126PoEplusPortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPortConfPortState_Type.__name__ = "Integer32"
_Es2126PoEplusPortConfPortState_Object = MibTableColumn
es2126PoEplusPortConfPortState = _Es2126PoEplusPortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2, 1, 2),
    _Es2126PoEplusPortConfPortState_Type()
)
es2126PoEplusPortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortConfPortState.setStatus("current")


class _Es2126PoEplusPortConfSpdDpx_Type(Integer32):
    """Custom type es2126PoEplusPortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Es2126PoEplusPortConfSpdDpx_Type.__name__ = "Integer32"
_Es2126PoEplusPortConfSpdDpx_Object = MibTableColumn
es2126PoEplusPortConfSpdDpx = _Es2126PoEplusPortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2, 1, 3),
    _Es2126PoEplusPortConfSpdDpx_Type()
)
es2126PoEplusPortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortConfSpdDpx.setStatus("current")


class _Es2126PoEplusPortConfFlwCtrl_Type(Integer32):
    """Custom type es2126PoEplusPortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPortConfFlwCtrl_Type.__name__ = "Integer32"
_Es2126PoEplusPortConfFlwCtrl_Object = MibTableColumn
es2126PoEplusPortConfFlwCtrl = _Es2126PoEplusPortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2, 1, 4),
    _Es2126PoEplusPortConfFlwCtrl_Type()
)
es2126PoEplusPortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortConfFlwCtrl.setStatus("current")
_Es2126PoEplusPortConfDescription_Type = DisplayString
_Es2126PoEplusPortConfDescription_Object = MibTableColumn
es2126PoEplusPortConfDescription = _Es2126PoEplusPortConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 2, 2, 1, 5),
    _Es2126PoEplusPortConfDescription_Type()
)
es2126PoEplusPortConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortConfDescription.setStatus("current")
_Es2126PoEplusPortBandwidth_ObjectIdentity = ObjectIdentity
es2126PoEplusPortBandwidth = _Es2126PoEplusPortBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3)
)
_Es2126PoEplusPortBandwidthTable_Object = MibTable
es2126PoEplusPortBandwidthTable = _Es2126PoEplusPortBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthTable.setStatus("current")
_Es2126PoEplusPortBandwidthEntry_Object = MibTableRow
es2126PoEplusPortBandwidthEntry = _Es2126PoEplusPortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 1, 1)
)
es2126PoEplusPortBandwidthEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPortBandwidthIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthEntry.setStatus("current")


class _Es2126PoEplusPortBandwidthIndex_Type(Integer32):
    """Custom type es2126PoEplusPortBandwidthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusPortBandwidthIndex_Type.__name__ = "Integer32"
_Es2126PoEplusPortBandwidthIndex_Object = MibTableColumn
es2126PoEplusPortBandwidthIndex = _Es2126PoEplusPortBandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 1, 1, 1),
    _Es2126PoEplusPortBandwidthIndex_Type()
)
es2126PoEplusPortBandwidthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthIndex.setStatus("current")


class _Es2126PoEplusPortBandwidthIngressRate_Type(Integer32):
    """Custom type es2126PoEplusPortBandwidthIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 1024000),
    )


_Es2126PoEplusPortBandwidthIngressRate_Type.__name__ = "Integer32"
_Es2126PoEplusPortBandwidthIngressRate_Object = MibTableColumn
es2126PoEplusPortBandwidthIngressRate = _Es2126PoEplusPortBandwidthIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 1, 1, 2),
    _Es2126PoEplusPortBandwidthIngressRate_Type()
)
es2126PoEplusPortBandwidthIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthIngressRate.setStatus("current")


class _Es2126PoEplusPortBandwidthEgressRate_Type(Integer32):
    """Custom type es2126PoEplusPortBandwidthEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 1024000),
    )


_Es2126PoEplusPortBandwidthEgressRate_Type.__name__ = "Integer32"
_Es2126PoEplusPortBandwidthEgressRate_Object = MibTableColumn
es2126PoEplusPortBandwidthEgressRate = _Es2126PoEplusPortBandwidthEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 1, 1, 3),
    _Es2126PoEplusPortBandwidthEgressRate_Type()
)
es2126PoEplusPortBandwidthEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthEgressRate.setStatus("current")


class _Es2126PoEplusPortBandwidthStormType_Type(Integer32):
    """Custom type es2126PoEplusPortBandwidthStormType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Es2126PoEplusPortBandwidthStormType_Type.__name__ = "Integer32"
_Es2126PoEplusPortBandwidthStormType_Object = MibScalar
es2126PoEplusPortBandwidthStormType = _Es2126PoEplusPortBandwidthStormType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 2),
    _Es2126PoEplusPortBandwidthStormType_Type()
)
es2126PoEplusPortBandwidthStormType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthStormType.setStatus("current")


class _Es2126PoEplusPortBandwidthStormRate_Type(Integer32):
    """Custom type es2126PoEplusPortBandwidthStormRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Es2126PoEplusPortBandwidthStormRate_Type.__name__ = "Integer32"
_Es2126PoEplusPortBandwidthStormRate_Object = MibScalar
es2126PoEplusPortBandwidthStormRate = _Es2126PoEplusPortBandwidthStormRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 3, 3),
    _Es2126PoEplusPortBandwidthStormRate_Type()
)
es2126PoEplusPortBandwidthStormRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBandwidthStormRate.setStatus("current")
_Es2126PoEplusPortSFPInfo_ObjectIdentity = ObjectIdentity
es2126PoEplusPortSFPInfo = _Es2126PoEplusPortSFPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4)
)


class _Es2126PoEplusPortSFPInfoNumber_Type(Integer32):
    """Custom type es2126PoEplusPortSFPInfoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusPortSFPInfoNumber_Type.__name__ = "Integer32"
_Es2126PoEplusPortSFPInfoNumber_Object = MibScalar
es2126PoEplusPortSFPInfoNumber = _Es2126PoEplusPortSFPInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 1),
    _Es2126PoEplusPortSFPInfoNumber_Type()
)
es2126PoEplusPortSFPInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPInfoNumber.setStatus("current")
_Es2126PoEplusPortSFPInfoTable_Object = MibTable
es2126PoEplusPortSFPInfoTable = _Es2126PoEplusPortSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPInfoTable.setStatus("current")
_Es2126PoEplusPortSFPInfoEntry_Object = MibTableRow
es2126PoEplusPortSFPInfoEntry = _Es2126PoEplusPortSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1)
)
es2126PoEplusPortSFPInfoEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPortSFPInfoIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPInfoEntry.setStatus("current")


class _Es2126PoEplusPortSFPInfoIndex_Type(Integer32):
    """Custom type es2126PoEplusPortSFPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusPortSFPInfoIndex_Type.__name__ = "Integer32"
_Es2126PoEplusPortSFPInfoIndex_Object = MibTableColumn
es2126PoEplusPortSFPInfoIndex = _Es2126PoEplusPortSFPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 1),
    _Es2126PoEplusPortSFPInfoIndex_Type()
)
es2126PoEplusPortSFPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPInfoIndex.setStatus("current")
_Es2126PoEplusPortSFPConnectorType_Type = DisplayString
_Es2126PoEplusPortSFPConnectorType_Object = MibTableColumn
es2126PoEplusPortSFPConnectorType = _Es2126PoEplusPortSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 2),
    _Es2126PoEplusPortSFPConnectorType_Type()
)
es2126PoEplusPortSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPConnectorType.setStatus("current")
_Es2126PoEplusPortSFPFiberType_Type = DisplayString
_Es2126PoEplusPortSFPFiberType_Object = MibTableColumn
es2126PoEplusPortSFPFiberType = _Es2126PoEplusPortSFPFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 3),
    _Es2126PoEplusPortSFPFiberType_Type()
)
es2126PoEplusPortSFPFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPFiberType.setStatus("current")
_Es2126PoEplusPortSFPWavelength_Type = DisplayString
_Es2126PoEplusPortSFPWavelength_Object = MibTableColumn
es2126PoEplusPortSFPWavelength = _Es2126PoEplusPortSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 4),
    _Es2126PoEplusPortSFPWavelength_Type()
)
es2126PoEplusPortSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPWavelength.setStatus("current")
_Es2126PoEplusPortSFPBaudRate_Type = DisplayString
_Es2126PoEplusPortSFPBaudRate_Object = MibTableColumn
es2126PoEplusPortSFPBaudRate = _Es2126PoEplusPortSFPBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 5),
    _Es2126PoEplusPortSFPBaudRate_Type()
)
es2126PoEplusPortSFPBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPBaudRate.setStatus("current")
_Es2126PoEplusPortSFPVendorOUI_Type = DisplayString
_Es2126PoEplusPortSFPVendorOUI_Object = MibTableColumn
es2126PoEplusPortSFPVendorOUI = _Es2126PoEplusPortSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 6),
    _Es2126PoEplusPortSFPVendorOUI_Type()
)
es2126PoEplusPortSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPVendorOUI.setStatus("current")
_Es2126PoEplusPortSFPVendorName_Type = DisplayString
_Es2126PoEplusPortSFPVendorName_Object = MibTableColumn
es2126PoEplusPortSFPVendorName = _Es2126PoEplusPortSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 7),
    _Es2126PoEplusPortSFPVendorName_Type()
)
es2126PoEplusPortSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPVendorName.setStatus("current")
_Es2126PoEplusPortSFPVendorPN_Type = DisplayString
_Es2126PoEplusPortSFPVendorPN_Object = MibTableColumn
es2126PoEplusPortSFPVendorPN = _Es2126PoEplusPortSFPVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 8),
    _Es2126PoEplusPortSFPVendorPN_Type()
)
es2126PoEplusPortSFPVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPVendorPN.setStatus("current")
_Es2126PoEplusPortSFPVendorRev_Type = DisplayString
_Es2126PoEplusPortSFPVendorRev_Object = MibTableColumn
es2126PoEplusPortSFPVendorRev = _Es2126PoEplusPortSFPVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 9),
    _Es2126PoEplusPortSFPVendorRev_Type()
)
es2126PoEplusPortSFPVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPVendorRev.setStatus("current")
_Es2126PoEplusPortSFPVendorSN_Type = DisplayString
_Es2126PoEplusPortSFPVendorSN_Object = MibTableColumn
es2126PoEplusPortSFPVendorSN = _Es2126PoEplusPortSFPVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 10),
    _Es2126PoEplusPortSFPVendorSN_Type()
)
es2126PoEplusPortSFPVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPVendorSN.setStatus("current")
_Es2126PoEplusPortSFPDateCode_Type = DisplayString
_Es2126PoEplusPortSFPDateCode_Object = MibTableColumn
es2126PoEplusPortSFPDateCode = _Es2126PoEplusPortSFPDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 11),
    _Es2126PoEplusPortSFPDateCode_Type()
)
es2126PoEplusPortSFPDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPDateCode.setStatus("current")
_Es2126PoEplusPortSFPTemperature_Type = DisplayString
_Es2126PoEplusPortSFPTemperature_Object = MibTableColumn
es2126PoEplusPortSFPTemperature = _Es2126PoEplusPortSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 12),
    _Es2126PoEplusPortSFPTemperature_Type()
)
es2126PoEplusPortSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPTemperature.setStatus("current")
_Es2126PoEplusPortSFPVcc_Type = DisplayString
_Es2126PoEplusPortSFPVcc_Object = MibTableColumn
es2126PoEplusPortSFPVcc = _Es2126PoEplusPortSFPVcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 13),
    _Es2126PoEplusPortSFPVcc_Type()
)
es2126PoEplusPortSFPVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPVcc.setStatus("current")
_Es2126PoEplusPortSFPTxBias_Type = DisplayString
_Es2126PoEplusPortSFPTxBias_Object = MibTableColumn
es2126PoEplusPortSFPTxBias = _Es2126PoEplusPortSFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 14),
    _Es2126PoEplusPortSFPTxBias_Type()
)
es2126PoEplusPortSFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPTxBias.setStatus("current")
_Es2126PoEplusPortSFPTxPWR_Type = DisplayString
_Es2126PoEplusPortSFPTxPWR_Object = MibTableColumn
es2126PoEplusPortSFPTxPWR = _Es2126PoEplusPortSFPTxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 15),
    _Es2126PoEplusPortSFPTxPWR_Type()
)
es2126PoEplusPortSFPTxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPTxPWR.setStatus("current")
_Es2126PoEplusPortSFPRxPWR_Type = DisplayString
_Es2126PoEplusPortSFPRxPWR_Object = MibTableColumn
es2126PoEplusPortSFPRxPWR = _Es2126PoEplusPortSFPRxPWR_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 9, 4, 2, 1, 16),
    _Es2126PoEplusPortSFPRxPWR_Type()
)
es2126PoEplusPortSFPRxPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortSFPRxPWR.setStatus("current")
_Es2126PoEplusLoopDetectedConf_ObjectIdentity = ObjectIdentity
es2126PoEplusLoopDetectedConf = _Es2126PoEplusLoopDetectedConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10)
)


class _Es2126PoEplusLoopDetectedNumber_Type(Integer32):
    """Custom type es2126PoEplusLoopDetectedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusLoopDetectedNumber_Type.__name__ = "Integer32"
_Es2126PoEplusLoopDetectedNumber_Object = MibScalar
es2126PoEplusLoopDetectedNumber = _Es2126PoEplusLoopDetectedNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 1),
    _Es2126PoEplusLoopDetectedNumber_Type()
)
es2126PoEplusLoopDetectedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedNumber.setStatus("current")
_Es2126PoEplusLoopDetectedTable_Object = MibTable
es2126PoEplusLoopDetectedTable = _Es2126PoEplusLoopDetectedTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedTable.setStatus("current")
_Es2126PoEplusLoopDetectedEntry_Object = MibTableRow
es2126PoEplusLoopDetectedEntry = _Es2126PoEplusLoopDetectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 2, 1)
)
es2126PoEplusLoopDetectedEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusLoopDetectedfIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedEntry.setStatus("current")


class _Es2126PoEplusLoopDetectedfIndex_Type(Integer32):
    """Custom type es2126PoEplusLoopDetectedfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Es2126PoEplusLoopDetectedfIndex_Type.__name__ = "Integer32"
_Es2126PoEplusLoopDetectedfIndex_Object = MibTableColumn
es2126PoEplusLoopDetectedfIndex = _Es2126PoEplusLoopDetectedfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 2, 1, 1),
    _Es2126PoEplusLoopDetectedfIndex_Type()
)
es2126PoEplusLoopDetectedfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedfIndex.setStatus("current")


class _Es2126PoEplusLoopDetectedStateEbl_Type(Integer32):
    """Custom type es2126PoEplusLoopDetectedStateEbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusLoopDetectedStateEbl_Type.__name__ = "Integer32"
_Es2126PoEplusLoopDetectedStateEbl_Object = MibTableColumn
es2126PoEplusLoopDetectedStateEbl = _Es2126PoEplusLoopDetectedStateEbl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 2, 1, 2),
    _Es2126PoEplusLoopDetectedStateEbl_Type()
)
es2126PoEplusLoopDetectedStateEbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedStateEbl.setStatus("current")


class _Es2126PoEplusLoopDetectedCurrentStatus_Type(Integer32):
    """Custom type es2126PoEplusLoopDetectedCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusLoopDetectedCurrentStatus_Type.__name__ = "Integer32"
_Es2126PoEplusLoopDetectedCurrentStatus_Object = MibTableColumn
es2126PoEplusLoopDetectedCurrentStatus = _Es2126PoEplusLoopDetectedCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 2, 1, 3),
    _Es2126PoEplusLoopDetectedCurrentStatus_Type()
)
es2126PoEplusLoopDetectedCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedCurrentStatus.setStatus("current")


class _Es2126PoEplusLoopDetectedResumed_Type(Integer32):
    """Custom type es2126PoEplusLoopDetectedResumed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusLoopDetectedResumed_Type.__name__ = "Integer32"
_Es2126PoEplusLoopDetectedResumed_Object = MibTableColumn
es2126PoEplusLoopDetectedResumed = _Es2126PoEplusLoopDetectedResumed_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 2, 1, 4),
    _Es2126PoEplusLoopDetectedResumed_Type()
)
es2126PoEplusLoopDetectedResumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedResumed.setStatus("current")


class _Es2126PoEplusLoopDetectedAction_Type(Integer32):
    """Custom type es2126PoEplusLoopDetectedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusLoopDetectedAction_Type.__name__ = "Integer32"
_Es2126PoEplusLoopDetectedAction_Object = MibScalar
es2126PoEplusLoopDetectedAction = _Es2126PoEplusLoopDetectedAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 10, 3),
    _Es2126PoEplusLoopDetectedAction_Type()
)
es2126PoEplusLoopDetectedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetectedAction.setStatus("current")
_Es2126PoEplusMacTableInfo_ObjectIdentity = ObjectIdentity
es2126PoEplusMacTableInfo = _Es2126PoEplusMacTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11)
)
_Es2126PoEplusMacTableMaintenance_ObjectIdentity = ObjectIdentity
es2126PoEplusMacTableMaintenance = _Es2126PoEplusMacTableMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1)
)


class _Es2126PoEplusMacTableAgingTime_Type(Integer32):
    """Custom type es2126PoEplusMacTableAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000000),
    )


_Es2126PoEplusMacTableAgingTime_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableAgingTime_Object = MibScalar
es2126PoEplusMacTableAgingTime = _Es2126PoEplusMacTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1, 1),
    _Es2126PoEplusMacTableAgingTime_Type()
)
es2126PoEplusMacTableAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableAgingTime.setStatus("current")


class _Es2126PoEplusMacTableFlush_Type(Integer32):
    """Custom type es2126PoEplusMacTableFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusMacTableFlush_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableFlush_Object = MibScalar
es2126PoEplusMacTableFlush = _Es2126PoEplusMacTableFlush_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1, 2),
    _Es2126PoEplusMacTableFlush_Type()
)
es2126PoEplusMacTableFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableFlush.setStatus("current")
_Es2126PoEplusMacTableLearnPortLimitTable_Object = MibTable
es2126PoEplusMacTableLearnPortLimitTable = _Es2126PoEplusMacTableLearnPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1, 3)
)
if mibBuilder.loadTexts:
    es2126PoEplusMacTableLearnPortLimitTable.setStatus("current")
_Es2126PoEplusMacTableLearnPortLimitEntry_Object = MibTableRow
es2126PoEplusMacTableLearnPortLimitEntry = _Es2126PoEplusMacTableLearnPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1, 3, 1)
)
es2126PoEplusMacTableLearnPortLimitEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusMacTableLearnPortLimitIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusMacTableLearnPortLimitEntry.setStatus("current")


class _Es2126PoEplusMacTableLearnPortLimitIndex_Type(Integer32):
    """Custom type es2126PoEplusMacTableLearnPortLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusMacTableLearnPortLimitIndex_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableLearnPortLimitIndex_Object = MibTableColumn
es2126PoEplusMacTableLearnPortLimitIndex = _Es2126PoEplusMacTableLearnPortLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1, 3, 1, 1),
    _Es2126PoEplusMacTableLearnPortLimitIndex_Type()
)
es2126PoEplusMacTableLearnPortLimitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableLearnPortLimitIndex.setStatus("current")


class _Es2126PoEplusMacTableLearnPortLimit_Type(Integer32):
    """Custom type es2126PoEplusMacTableLearnPortLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_Es2126PoEplusMacTableLearnPortLimit_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableLearnPortLimit_Object = MibTableColumn
es2126PoEplusMacTableLearnPortLimit = _Es2126PoEplusMacTableLearnPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 1, 3, 1, 2),
    _Es2126PoEplusMacTableLearnPortLimit_Type()
)
es2126PoEplusMacTableLearnPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableLearnPortLimit.setStatus("current")
_Es2126PoEplusMacTableStaticMac_ObjectIdentity = ObjectIdentity
es2126PoEplusMacTableStaticMac = _Es2126PoEplusMacTableStaticMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3)
)


class _Es2126PoEplusMacTableStaticMacNumber_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2126PoEplusMacTableStaticMacNumber_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacNumber_Object = MibScalar
es2126PoEplusMacTableStaticMacNumber = _Es2126PoEplusMacTableStaticMacNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 1),
    _Es2126PoEplusMacTableStaticMacNumber_Type()
)
es2126PoEplusMacTableStaticMacNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacNumber.setStatus("current")


class _Es2126PoEplusMacTableStaticMacEntryCreate_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Es2126PoEplusMacTableStaticMacEntryCreate_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacEntryCreate_Object = MibScalar
es2126PoEplusMacTableStaticMacEntryCreate = _Es2126PoEplusMacTableStaticMacEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 2),
    _Es2126PoEplusMacTableStaticMacEntryCreate_Type()
)
es2126PoEplusMacTableStaticMacEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacEntryCreate.setStatus("current")
_Es2126PoEplusMacTableStaticMacTable_Object = MibTable
es2126PoEplusMacTableStaticMacTable = _Es2126PoEplusMacTableStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacTable.setStatus("current")
_Es2126PoEplusMacTableStaticMacEntry_Object = MibTableRow
es2126PoEplusMacTableStaticMacEntry = _Es2126PoEplusMacTableStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1)
)
es2126PoEplusMacTableStaticMacEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusMacTableStaticMacIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacEntry.setStatus("current")


class _Es2126PoEplusMacTableStaticMacIndex_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2126PoEplusMacTableStaticMacIndex_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacIndex_Object = MibTableColumn
es2126PoEplusMacTableStaticMacIndex = _Es2126PoEplusMacTableStaticMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 1),
    _Es2126PoEplusMacTableStaticMacIndex_Type()
)
es2126PoEplusMacTableStaticMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacIndex.setStatus("current")
_Es2126PoEplusMacTableStaticMacAddress_Type = DisplayString
_Es2126PoEplusMacTableStaticMacAddress_Object = MibTableColumn
es2126PoEplusMacTableStaticMacAddress = _Es2126PoEplusMacTableStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 2),
    _Es2126PoEplusMacTableStaticMacAddress_Type()
)
es2126PoEplusMacTableStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacAddress.setStatus("current")


class _Es2126PoEplusMacTableStaticMacVid_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusMacTableStaticMacVid_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacVid_Object = MibTableColumn
es2126PoEplusMacTableStaticMacVid = _Es2126PoEplusMacTableStaticMacVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 3),
    _Es2126PoEplusMacTableStaticMacVid_Type()
)
es2126PoEplusMacTableStaticMacVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacVid.setStatus("current")


class _Es2126PoEplusMacTableStaticMacQueue_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusMacTableStaticMacQueue_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacQueue_Object = MibTableColumn
es2126PoEplusMacTableStaticMacQueue = _Es2126PoEplusMacTableStaticMacQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 4),
    _Es2126PoEplusMacTableStaticMacQueue_Type()
)
es2126PoEplusMacTableStaticMacQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacQueue.setStatus("current")


class _Es2126PoEplusMacTableStaticMacFwRule_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacFwRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusMacTableStaticMacFwRule_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacFwRule_Object = MibTableColumn
es2126PoEplusMacTableStaticMacFwRule = _Es2126PoEplusMacTableStaticMacFwRule_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 5),
    _Es2126PoEplusMacTableStaticMacFwRule_Type()
)
es2126PoEplusMacTableStaticMacFwRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacFwRule.setStatus("current")


class _Es2126PoEplusMacTableStaticMacPort_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusMacTableStaticMacPort_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacPort_Object = MibTableColumn
es2126PoEplusMacTableStaticMacPort = _Es2126PoEplusMacTableStaticMacPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 6),
    _Es2126PoEplusMacTableStaticMacPort_Type()
)
es2126PoEplusMacTableStaticMacPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacPort.setStatus("current")


class _Es2126PoEplusMacTableStaticMacEntryAction_Type(Integer32):
    """Custom type es2126PoEplusMacTableStaticMacEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126PoEplusMacTableStaticMacEntryAction_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableStaticMacEntryAction_Object = MibTableColumn
es2126PoEplusMacTableStaticMacEntryAction = _Es2126PoEplusMacTableStaticMacEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 3, 3, 1, 7),
    _Es2126PoEplusMacTableStaticMacEntryAction_Type()
)
es2126PoEplusMacTableStaticMacEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableStaticMacEntryAction.setStatus("current")
_Es2126PoEplusMacTableMacAlias_ObjectIdentity = ObjectIdentity
es2126PoEplusMacTableMacAlias = _Es2126PoEplusMacTableMacAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4)
)


class _Es2126PoEplusMacTableMacAliasNumber_Type(Integer32):
    """Custom type es2126PoEplusMacTableMacAliasNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_Es2126PoEplusMacTableMacAliasNumber_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableMacAliasNumber_Object = MibScalar
es2126PoEplusMacTableMacAliasNumber = _Es2126PoEplusMacTableMacAliasNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 1),
    _Es2126PoEplusMacTableMacAliasNumber_Type()
)
es2126PoEplusMacTableMacAliasNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasNumber.setStatus("current")


class _Es2126PoEplusMacTableMacAliasEntryCreate_Type(Integer32):
    """Custom type es2126PoEplusMacTableMacAliasEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_Es2126PoEplusMacTableMacAliasEntryCreate_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableMacAliasEntryCreate_Object = MibScalar
es2126PoEplusMacTableMacAliasEntryCreate = _Es2126PoEplusMacTableMacAliasEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 2),
    _Es2126PoEplusMacTableMacAliasEntryCreate_Type()
)
es2126PoEplusMacTableMacAliasEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasEntryCreate.setStatus("current")
_Es2126PoEplusMacTableMacAliasTable_Object = MibTable
es2126PoEplusMacTableMacAliasTable = _Es2126PoEplusMacTableMacAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 3)
)
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasTable.setStatus("current")
_Es2126PoEplusMacTableMacAliasEntry_Object = MibTableRow
es2126PoEplusMacTableMacAliasEntry = _Es2126PoEplusMacTableMacAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 3, 1)
)
es2126PoEplusMacTableMacAliasEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusMacTableMacAliasIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasEntry.setStatus("current")


class _Es2126PoEplusMacTableMacAliasIndex_Type(Integer32):
    """Custom type es2126PoEplusMacTableMacAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Es2126PoEplusMacTableMacAliasIndex_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableMacAliasIndex_Object = MibTableColumn
es2126PoEplusMacTableMacAliasIndex = _Es2126PoEplusMacTableMacAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 3, 1, 1),
    _Es2126PoEplusMacTableMacAliasIndex_Type()
)
es2126PoEplusMacTableMacAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasIndex.setStatus("current")
_Es2126PoEplusMacTableMacAliasAddress_Type = DisplayString
_Es2126PoEplusMacTableMacAliasAddress_Object = MibTableColumn
es2126PoEplusMacTableMacAliasAddress = _Es2126PoEplusMacTableMacAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 3, 1, 2),
    _Es2126PoEplusMacTableMacAliasAddress_Type()
)
es2126PoEplusMacTableMacAliasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasAddress.setStatus("current")
_Es2126PoEplusMacTableMacAliasAlias_Type = DisplayString
_Es2126PoEplusMacTableMacAliasAlias_Object = MibTableColumn
es2126PoEplusMacTableMacAliasAlias = _Es2126PoEplusMacTableMacAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 3, 1, 3),
    _Es2126PoEplusMacTableMacAliasAlias_Type()
)
es2126PoEplusMacTableMacAliasAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasAlias.setStatus("current")


class _Es2126PoEplusMacTableMacAliasEntryAction_Type(Integer32):
    """Custom type es2126PoEplusMacTableMacAliasEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126PoEplusMacTableMacAliasEntryAction_Type.__name__ = "Integer32"
_Es2126PoEplusMacTableMacAliasEntryAction_Object = MibTableColumn
es2126PoEplusMacTableMacAliasEntryAction = _Es2126PoEplusMacTableMacAliasEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 11, 4, 3, 1, 4),
    _Es2126PoEplusMacTableMacAliasEntryAction_Type()
)
es2126PoEplusMacTableMacAliasEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMacTableMacAliasEntryAction.setStatus("current")
_Es2126PoEplusGVRPInfo_ObjectIdentity = ObjectIdentity
es2126PoEplusGVRPInfo = _Es2126PoEplusGVRPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12)
)
_Es2126PoEplusGvrpConf_ObjectIdentity = ObjectIdentity
es2126PoEplusGvrpConf = _Es2126PoEplusGvrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1)
)


class _Es2126PoEplusGvrpConfState_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusGvrpConfState_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfState_Object = MibScalar
es2126PoEplusGvrpConfState = _Es2126PoEplusGvrpConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 1),
    _Es2126PoEplusGvrpConfState_Type()
)
es2126PoEplusGvrpConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfState.setStatus("current")
_Es2126PoEplusGvrpConfTable_Object = MibTable
es2126PoEplusGvrpConfTable = _Es2126PoEplusGvrpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfTable.setStatus("current")
_Es2126PoEplusGvrpConfEntry_Object = MibTableRow
es2126PoEplusGvrpConfEntry = _Es2126PoEplusGvrpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1)
)
es2126PoEplusGvrpConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusGvrpConfIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfEntry.setStatus("current")


class _Es2126PoEplusGvrpConfIndex_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusGvrpConfIndex_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfIndex_Object = MibTableColumn
es2126PoEplusGvrpConfIndex = _Es2126PoEplusGvrpConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 1),
    _Es2126PoEplusGvrpConfIndex_Type()
)
es2126PoEplusGvrpConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfIndex.setStatus("current")


class _Es2126PoEplusGvrpConfJoinTime_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfJoinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_Es2126PoEplusGvrpConfJoinTime_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfJoinTime_Object = MibTableColumn
es2126PoEplusGvrpConfJoinTime = _Es2126PoEplusGvrpConfJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 2),
    _Es2126PoEplusGvrpConfJoinTime_Type()
)
es2126PoEplusGvrpConfJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfJoinTime.setStatus("current")


class _Es2126PoEplusGvrpConfLeaveTime_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfLeaveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Es2126PoEplusGvrpConfLeaveTime_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfLeaveTime_Object = MibTableColumn
es2126PoEplusGvrpConfLeaveTime = _Es2126PoEplusGvrpConfLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 3),
    _Es2126PoEplusGvrpConfLeaveTime_Type()
)
es2126PoEplusGvrpConfLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfLeaveTime.setStatus("current")


class _Es2126PoEplusGvrpConfLeaveAllTime_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfLeaveAllTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5000),
    )


_Es2126PoEplusGvrpConfLeaveAllTime_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfLeaveAllTime_Object = MibTableColumn
es2126PoEplusGvrpConfLeaveAllTime = _Es2126PoEplusGvrpConfLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 4),
    _Es2126PoEplusGvrpConfLeaveAllTime_Type()
)
es2126PoEplusGvrpConfLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfLeaveAllTime.setStatus("current")


class _Es2126PoEplusGvrpConfDefaultAppMode_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfDefaultAppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusGvrpConfDefaultAppMode_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfDefaultAppMode_Object = MibTableColumn
es2126PoEplusGvrpConfDefaultAppMode = _Es2126PoEplusGvrpConfDefaultAppMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 5),
    _Es2126PoEplusGvrpConfDefaultAppMode_Type()
)
es2126PoEplusGvrpConfDefaultAppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfDefaultAppMode.setStatus("current")


class _Es2126PoEplusGvrpConfDefaultRegMode_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfDefaultRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Es2126PoEplusGvrpConfDefaultRegMode_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfDefaultRegMode_Object = MibTableColumn
es2126PoEplusGvrpConfDefaultRegMode = _Es2126PoEplusGvrpConfDefaultRegMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 6),
    _Es2126PoEplusGvrpConfDefaultRegMode_Type()
)
es2126PoEplusGvrpConfDefaultRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfDefaultRegMode.setStatus("current")


class _Es2126PoEplusGvrpConfRestrictedMode_Type(Integer32):
    """Custom type es2126PoEplusGvrpConfRestrictedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusGvrpConfRestrictedMode_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpConfRestrictedMode_Object = MibTableColumn
es2126PoEplusGvrpConfRestrictedMode = _Es2126PoEplusGvrpConfRestrictedMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 1, 2, 1, 7),
    _Es2126PoEplusGvrpConfRestrictedMode_Type()
)
es2126PoEplusGvrpConfRestrictedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpConfRestrictedMode.setStatus("current")
_Es2126PoEplusGvrpCounter_ObjectIdentity = ObjectIdentity
es2126PoEplusGvrpCounter = _Es2126PoEplusGvrpCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2)
)
_Es2126PoEplusGvrpCounterTable_Object = MibTable
es2126PoEplusGvrpCounterTable = _Es2126PoEplusGvrpCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTable.setStatus("current")
_Es2126PoEplusGvrpCounterEntry_Object = MibTableRow
es2126PoEplusGvrpCounterEntry = _Es2126PoEplusGvrpCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1)
)
es2126PoEplusGvrpCounterEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusGvrpCounterIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterEntry.setStatus("current")


class _Es2126PoEplusGvrpCounterIndex_Type(Integer32):
    """Custom type es2126PoEplusGvrpCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusGvrpCounterIndex_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpCounterIndex_Object = MibTableColumn
es2126PoEplusGvrpCounterIndex = _Es2126PoEplusGvrpCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 1),
    _Es2126PoEplusGvrpCounterIndex_Type()
)
es2126PoEplusGvrpCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterIndex.setStatus("current")
_Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Type = Counter32
_Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Object = MibTableColumn
es2126PoEplusGvrpCounterRxTotalGvrpPkts = _Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 2),
    _Es2126PoEplusGvrpCounterRxTotalGvrpPkts_Type()
)
es2126PoEplusGvrpCounterRxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxTotalGvrpPkts.setStatus("current")
_Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Type = Counter32
_Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Object = MibTableColumn
es2126PoEplusGvrpCounterRxInvalidGvrpPkts = _Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 3),
    _Es2126PoEplusGvrpCounterRxInvalidGvrpPkts_Type()
)
es2126PoEplusGvrpCounterRxInvalidGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxInvalidGvrpPkts.setStatus("current")
_Es2126PoEplusGvrpCounterRxLeaveAllMsg_Type = Counter32
_Es2126PoEplusGvrpCounterRxLeaveAllMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterRxLeaveAllMsg = _Es2126PoEplusGvrpCounterRxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 4),
    _Es2126PoEplusGvrpCounterRxLeaveAllMsg_Type()
)
es2126PoEplusGvrpCounterRxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxLeaveAllMsg.setStatus("current")
_Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Type = Counter32
_Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterRxJoinEmptyMsg = _Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 5),
    _Es2126PoEplusGvrpCounterRxJoinEmptyMsg_Type()
)
es2126PoEplusGvrpCounterRxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxJoinEmptyMsg.setStatus("current")
_Es2126PoEplusGvrpCounterRxJoinInMsg_Type = Counter32
_Es2126PoEplusGvrpCounterRxJoinInMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterRxJoinInMsg = _Es2126PoEplusGvrpCounterRxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 6),
    _Es2126PoEplusGvrpCounterRxJoinInMsg_Type()
)
es2126PoEplusGvrpCounterRxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxJoinInMsg.setStatus("current")
_Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Type = Counter32
_Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterRxLeaveEmptyMsg = _Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 7),
    _Es2126PoEplusGvrpCounterRxLeaveEmptyMsg_Type()
)
es2126PoEplusGvrpCounterRxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxLeaveEmptyMsg.setStatus("current")
_Es2126PoEplusGvrpCounterRxEmptyMsg_Type = Counter32
_Es2126PoEplusGvrpCounterRxEmptyMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterRxEmptyMsg = _Es2126PoEplusGvrpCounterRxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 8),
    _Es2126PoEplusGvrpCounterRxEmptyMsg_Type()
)
es2126PoEplusGvrpCounterRxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterRxEmptyMsg.setStatus("current")
_Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Type = Counter32
_Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Object = MibTableColumn
es2126PoEplusGvrpCounterTxTotalGvrpPkts = _Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 9),
    _Es2126PoEplusGvrpCounterTxTotalGvrpPkts_Type()
)
es2126PoEplusGvrpCounterTxTotalGvrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTxTotalGvrpPkts.setStatus("current")
_Es2126PoEplusGvrpCounterTxLeaveAllMsg_Type = Counter32
_Es2126PoEplusGvrpCounterTxLeaveAllMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterTxLeaveAllMsg = _Es2126PoEplusGvrpCounterTxLeaveAllMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 10),
    _Es2126PoEplusGvrpCounterTxLeaveAllMsg_Type()
)
es2126PoEplusGvrpCounterTxLeaveAllMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTxLeaveAllMsg.setStatus("current")
_Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Type = Counter32
_Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterTxJoinEmptyMsg = _Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 11),
    _Es2126PoEplusGvrpCounterTxJoinEmptyMsg_Type()
)
es2126PoEplusGvrpCounterTxJoinEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTxJoinEmptyMsg.setStatus("current")
_Es2126PoEplusGvrpCounterTxJoinInMsg_Type = Counter32
_Es2126PoEplusGvrpCounterTxJoinInMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterTxJoinInMsg = _Es2126PoEplusGvrpCounterTxJoinInMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 12),
    _Es2126PoEplusGvrpCounterTxJoinInMsg_Type()
)
es2126PoEplusGvrpCounterTxJoinInMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTxJoinInMsg.setStatus("current")
_Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Type = Counter32
_Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterTxLeaveEmptyMsg = _Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 13),
    _Es2126PoEplusGvrpCounterTxLeaveEmptyMsg_Type()
)
es2126PoEplusGvrpCounterTxLeaveEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTxLeaveEmptyMsg.setStatus("current")
_Es2126PoEplusGvrpCounterTxEmptyMsg_Type = Counter32
_Es2126PoEplusGvrpCounterTxEmptyMsg_Object = MibTableColumn
es2126PoEplusGvrpCounterTxEmptyMsg = _Es2126PoEplusGvrpCounterTxEmptyMsg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 2, 1, 1, 14),
    _Es2126PoEplusGvrpCounterTxEmptyMsg_Type()
)
es2126PoEplusGvrpCounterTxEmptyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpCounterTxEmptyMsg.setStatus("current")
_Es2126PoEplusGvrpGroup_ObjectIdentity = ObjectIdentity
es2126PoEplusGvrpGroup = _Es2126PoEplusGvrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3)
)


class _Es2126PoEplusGvrpGroupNumber_Type(Integer32):
    """Custom type es2126PoEplusGvrpGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126PoEplusGvrpGroupNumber_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpGroupNumber_Object = MibScalar
es2126PoEplusGvrpGroupNumber = _Es2126PoEplusGvrpGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3, 1),
    _Es2126PoEplusGvrpGroupNumber_Type()
)
es2126PoEplusGvrpGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpGroupNumber.setStatus("current")
_Es2126PoEplusGvrpGroupTable_Object = MibTable
es2126PoEplusGvrpGroupTable = _Es2126PoEplusGvrpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpGroupTable.setStatus("current")
_Es2126PoEplusGvrpGroupEntry_Object = MibTableRow
es2126PoEplusGvrpGroupEntry = _Es2126PoEplusGvrpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3, 2, 1)
)
es2126PoEplusGvrpGroupEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusGvrpGroupId"),
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpGroupEntry.setStatus("current")


class _Es2126PoEplusGvrpGroupId_Type(Integer32):
    """Custom type es2126PoEplusGvrpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusGvrpGroupId_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpGroupId_Object = MibTableColumn
es2126PoEplusGvrpGroupId = _Es2126PoEplusGvrpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3, 2, 1, 1),
    _Es2126PoEplusGvrpGroupId_Type()
)
es2126PoEplusGvrpGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpGroupId.setStatus("current")


class _Es2126PoEplusGvrpGroupVid_Type(Integer32):
    """Custom type es2126PoEplusGvrpGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusGvrpGroupVid_Type.__name__ = "Integer32"
_Es2126PoEplusGvrpGroupVid_Object = MibTableColumn
es2126PoEplusGvrpGroupVid = _Es2126PoEplusGvrpGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3, 2, 1, 2),
    _Es2126PoEplusGvrpGroupVid_Type()
)
es2126PoEplusGvrpGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpGroupVid.setStatus("current")
_Es2126PoEplusGvrpGroupMemberPort_Type = DisplayString
_Es2126PoEplusGvrpGroupMemberPort_Object = MibTableColumn
es2126PoEplusGvrpGroupMemberPort = _Es2126PoEplusGvrpGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 12, 3, 2, 1, 3),
    _Es2126PoEplusGvrpGroupMemberPort_Type()
)
es2126PoEplusGvrpGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusGvrpGroupMemberPort.setStatus("current")
_Es2126PoEplusSecurity_ObjectIdentity = ObjectIdentity
es2126PoEplusSecurity = _Es2126PoEplusSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13)
)
_Es2126PoEplusIsolatedPortGroup_Type = DisplayString
_Es2126PoEplusIsolatedPortGroup_Object = MibScalar
es2126PoEplusIsolatedPortGroup = _Es2126PoEplusIsolatedPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 1),
    _Es2126PoEplusIsolatedPortGroup_Type()
)
es2126PoEplusIsolatedPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusIsolatedPortGroup.setStatus("current")
_Es2126PoEplusMirror_ObjectIdentity = ObjectIdentity
es2126PoEplusMirror = _Es2126PoEplusMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 2)
)


class _Es2126PoEplusMirrorMode_Type(Integer32):
    """Custom type es2126PoEplusMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusMirrorMode_Type.__name__ = "Integer32"
_Es2126PoEplusMirrorMode_Object = MibScalar
es2126PoEplusMirrorMode = _Es2126PoEplusMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 2, 1),
    _Es2126PoEplusMirrorMode_Type()
)
es2126PoEplusMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMirrorMode.setStatus("current")


class _Es2126PoEplusMonitoringPort_Type(Integer32):
    """Custom type es2126PoEplusMonitoringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusMonitoringPort_Type.__name__ = "Integer32"
_Es2126PoEplusMonitoringPort_Object = MibScalar
es2126PoEplusMonitoringPort = _Es2126PoEplusMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 2, 2),
    _Es2126PoEplusMonitoringPort_Type()
)
es2126PoEplusMonitoringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMonitoringPort.setStatus("current")
_Es2126PoEplusMonitoredIngressPort_Type = DisplayString
_Es2126PoEplusMonitoredIngressPort_Object = MibScalar
es2126PoEplusMonitoredIngressPort = _Es2126PoEplusMonitoredIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 2, 3),
    _Es2126PoEplusMonitoredIngressPort_Type()
)
es2126PoEplusMonitoredIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMonitoredIngressPort.setStatus("current")
_Es2126PoEplusMonitoredEgressPort_Type = DisplayString
_Es2126PoEplusMonitoredEgressPort_Object = MibScalar
es2126PoEplusMonitoredEgressPort = _Es2126PoEplusMonitoredEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 2, 4),
    _Es2126PoEplusMonitoredEgressPort_Type()
)
es2126PoEplusMonitoredEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusMonitoredEgressPort.setStatus("current")
_Es2126PoEplusRestrictedGroup_ObjectIdentity = ObjectIdentity
es2126PoEplusRestrictedGroup = _Es2126PoEplusRestrictedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 3)
)
_Es2126PoEplusRestrictedGroupIngress_Type = DisplayString
_Es2126PoEplusRestrictedGroupIngress_Object = MibScalar
es2126PoEplusRestrictedGroupIngress = _Es2126PoEplusRestrictedGroupIngress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 3, 1),
    _Es2126PoEplusRestrictedGroupIngress_Type()
)
es2126PoEplusRestrictedGroupIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRestrictedGroupIngress.setStatus("current")
_Es2126PoEplusRestrictedGroupEgress_Type = DisplayString
_Es2126PoEplusRestrictedGroupEgress_Object = MibScalar
es2126PoEplusRestrictedGroupEgress = _Es2126PoEplusRestrictedGroupEgress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 13, 3, 2),
    _Es2126PoEplusRestrictedGroupEgress_Type()
)
es2126PoEplusRestrictedGroupEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRestrictedGroupEgress.setStatus("current")
_Es2126PoEplusVirtualStack_ObjectIdentity = ObjectIdentity
es2126PoEplusVirtualStack = _Es2126PoEplusVirtualStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 14)
)


class _Es2126PoEplusVirtualStackState_Type(Integer32):
    """Custom type es2126PoEplusVirtualStackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusVirtualStackState_Type.__name__ = "Integer32"
_Es2126PoEplusVirtualStackState_Object = MibScalar
es2126PoEplusVirtualStackState = _Es2126PoEplusVirtualStackState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 14, 1),
    _Es2126PoEplusVirtualStackState_Type()
)
es2126PoEplusVirtualStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVirtualStackState.setStatus("current")


class _Es2126PoEplusVirtualStackRole_Type(Integer32):
    """Custom type es2126PoEplusVirtualStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusVirtualStackRole_Type.__name__ = "Integer32"
_Es2126PoEplusVirtualStackRole_Object = MibScalar
es2126PoEplusVirtualStackRole = _Es2126PoEplusVirtualStackRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 14, 2),
    _Es2126PoEplusVirtualStackRole_Type()
)
es2126PoEplusVirtualStackRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVirtualStackRole.setStatus("current")
_Es2126PoEplusVirtualStackGroupID_Type = DisplayString
_Es2126PoEplusVirtualStackGroupID_Object = MibScalar
es2126PoEplusVirtualStackGroupID = _Es2126PoEplusVirtualStackGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 14, 3),
    _Es2126PoEplusVirtualStackGroupID_Type()
)
es2126PoEplusVirtualStackGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVirtualStackGroupID.setStatus("current")
_Es2126PoEplusManagementSecurity_ObjectIdentity = ObjectIdentity
es2126PoEplusManagementSecurity = _Es2126PoEplusManagementSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15)
)


class _Es2126PoEplusManagementSecurityNumber_Type(Integer32):
    """Custom type es2126PoEplusManagementSecurityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2126PoEplusManagementSecurityNumber_Type.__name__ = "Integer32"
_Es2126PoEplusManagementSecurityNumber_Object = MibScalar
es2126PoEplusManagementSecurityNumber = _Es2126PoEplusManagementSecurityNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 1),
    _Es2126PoEplusManagementSecurityNumber_Type()
)
es2126PoEplusManagementSecurityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityNumber.setStatus("current")


class _Es2126PoEplusManagementSecurityEntryCreate_Type(Integer32):
    """Custom type es2126PoEplusManagementSecurityEntryCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Es2126PoEplusManagementSecurityEntryCreate_Type.__name__ = "Integer32"
_Es2126PoEplusManagementSecurityEntryCreate_Object = MibScalar
es2126PoEplusManagementSecurityEntryCreate = _Es2126PoEplusManagementSecurityEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 2),
    _Es2126PoEplusManagementSecurityEntryCreate_Type()
)
es2126PoEplusManagementSecurityEntryCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityEntryCreate.setStatus("current")
_Es2126PoEplusManagementSecurityTable_Object = MibTable
es2126PoEplusManagementSecurityTable = _Es2126PoEplusManagementSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3)
)
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityTable.setStatus("current")
_Es2126PoEplusManagementSecurityEntry_Object = MibTableRow
es2126PoEplusManagementSecurityEntry = _Es2126PoEplusManagementSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1)
)
es2126PoEplusManagementSecurityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusManagementSecurityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityEntry.setStatus("current")


class _Es2126PoEplusManagementSecurityIndex_Type(Integer32):
    """Custom type es2126PoEplusManagementSecurityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2126PoEplusManagementSecurityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusManagementSecurityIndex_Object = MibTableColumn
es2126PoEplusManagementSecurityIndex = _Es2126PoEplusManagementSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 1),
    _Es2126PoEplusManagementSecurityIndex_Type()
)
es2126PoEplusManagementSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityIndex.setStatus("current")
_Es2126PoEplusManagementSecurityName_Type = DisplayString
_Es2126PoEplusManagementSecurityName_Object = MibTableColumn
es2126PoEplusManagementSecurityName = _Es2126PoEplusManagementSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 2),
    _Es2126PoEplusManagementSecurityName_Type()
)
es2126PoEplusManagementSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityName.setStatus("current")


class _Es2126PoEplusManagementSecurityVid_Type(Integer32):
    """Custom type es2126PoEplusManagementSecurityVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126PoEplusManagementSecurityVid_Type.__name__ = "Integer32"
_Es2126PoEplusManagementSecurityVid_Object = MibTableColumn
es2126PoEplusManagementSecurityVid = _Es2126PoEplusManagementSecurityVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 3),
    _Es2126PoEplusManagementSecurityVid_Type()
)
es2126PoEplusManagementSecurityVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityVid.setStatus("current")
_Es2126PoEplusManagementSecurityIpRange_Type = DisplayString
_Es2126PoEplusManagementSecurityIpRange_Object = MibTableColumn
es2126PoEplusManagementSecurityIpRange = _Es2126PoEplusManagementSecurityIpRange_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 4),
    _Es2126PoEplusManagementSecurityIpRange_Type()
)
es2126PoEplusManagementSecurityIpRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityIpRange.setStatus("current")
_Es2126PoEplusManagementSecurityIncomigPort_Type = DisplayString
_Es2126PoEplusManagementSecurityIncomigPort_Object = MibTableColumn
es2126PoEplusManagementSecurityIncomigPort = _Es2126PoEplusManagementSecurityIncomigPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 5),
    _Es2126PoEplusManagementSecurityIncomigPort_Type()
)
es2126PoEplusManagementSecurityIncomigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityIncomigPort.setStatus("current")
_Es2126PoEplusManagementSecurityAccessType_Type = DisplayString
_Es2126PoEplusManagementSecurityAccessType_Object = MibTableColumn
es2126PoEplusManagementSecurityAccessType = _Es2126PoEplusManagementSecurityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 6),
    _Es2126PoEplusManagementSecurityAccessType_Type()
)
es2126PoEplusManagementSecurityAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityAccessType.setStatus("current")


class _Es2126PoEplusManagementSecurityAction_Type(Integer32):
    """Custom type es2126PoEplusManagementSecurityAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusManagementSecurityAction_Type.__name__ = "Integer32"
_Es2126PoEplusManagementSecurityAction_Object = MibTableColumn
es2126PoEplusManagementSecurityAction = _Es2126PoEplusManagementSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 7),
    _Es2126PoEplusManagementSecurityAction_Type()
)
es2126PoEplusManagementSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityAction.setStatus("current")


class _Es2126PoEplusManagementSecurityEntryAction_Type(Integer32):
    """Custom type es2126PoEplusManagementSecurityEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusManagementSecurityEntryAction_Type.__name__ = "Integer32"
_Es2126PoEplusManagementSecurityEntryAction_Object = MibTableColumn
es2126PoEplusManagementSecurityEntryAction = _Es2126PoEplusManagementSecurityEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 15, 3, 1, 8),
    _Es2126PoEplusManagementSecurityEntryAction_Type()
)
es2126PoEplusManagementSecurityEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementSecurityEntryAction.setStatus("current")
_Es2126PoEplusQoS_ObjectIdentity = ObjectIdentity
es2126PoEplusQoS = _Es2126PoEplusQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16)
)
_Es2126PoEplusQoSGlobalConfig_ObjectIdentity = ObjectIdentity
es2126PoEplusQoSGlobalConfig = _Es2126PoEplusQoSGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1)
)


class _Es2126PoEplusQoSMode_Type(Integer32):
    """Custom type es2126PoEplusQoSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusQoSMode_Type.__name__ = "Integer32"
_Es2126PoEplusQoSMode_Object = MibScalar
es2126PoEplusQoSMode = _Es2126PoEplusQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 1),
    _Es2126PoEplusQoSMode_Type()
)
es2126PoEplusQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSMode.setStatus("current")


class _Es2126PoEplusQosPriorityControl1p_Type(Integer32):
    """Custom type es2126PoEplusQosPriorityControl1p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusQosPriorityControl1p_Type.__name__ = "Integer32"
_Es2126PoEplusQosPriorityControl1p_Object = MibScalar
es2126PoEplusQosPriorityControl1p = _Es2126PoEplusQosPriorityControl1p_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 2),
    _Es2126PoEplusQosPriorityControl1p_Type()
)
es2126PoEplusQosPriorityControl1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQosPriorityControl1p.setStatus("current")


class _Es2126PoEplusQosPriorityControlTOS_Type(Integer32):
    """Custom type es2126PoEplusQosPriorityControlTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusQosPriorityControlTOS_Type.__name__ = "Integer32"
_Es2126PoEplusQosPriorityControlTOS_Object = MibScalar
es2126PoEplusQosPriorityControlTOS = _Es2126PoEplusQosPriorityControlTOS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 3),
    _Es2126PoEplusQosPriorityControlTOS_Type()
)
es2126PoEplusQosPriorityControlTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQosPriorityControlTOS.setStatus("current")


class _Es2126PoEplusQosPriorityControlDSCP_Type(Integer32):
    """Custom type es2126PoEplusQosPriorityControlDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusQosPriorityControlDSCP_Type.__name__ = "Integer32"
_Es2126PoEplusQosPriorityControlDSCP_Object = MibScalar
es2126PoEplusQosPriorityControlDSCP = _Es2126PoEplusQosPriorityControlDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 4),
    _Es2126PoEplusQosPriorityControlDSCP_Type()
)
es2126PoEplusQosPriorityControlDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQosPriorityControlDSCP.setStatus("current")


class _Es2126PoEplusQoSSchedulingMethod_Type(Integer32):
    """Custom type es2126PoEplusQoSSchedulingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusQoSSchedulingMethod_Type.__name__ = "Integer32"
_Es2126PoEplusQoSSchedulingMethod_Object = MibScalar
es2126PoEplusQoSSchedulingMethod = _Es2126PoEplusQoSSchedulingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 5),
    _Es2126PoEplusQoSSchedulingMethod_Type()
)
es2126PoEplusQoSSchedulingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSSchedulingMethod.setStatus("current")


class _Es2126PoEplusQoSWeightQ0_Type(Integer32):
    """Custom type es2126PoEplusQoSWeightQ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126PoEplusQoSWeightQ0_Type.__name__ = "Integer32"
_Es2126PoEplusQoSWeightQ0_Object = MibScalar
es2126PoEplusQoSWeightQ0 = _Es2126PoEplusQoSWeightQ0_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 6),
    _Es2126PoEplusQoSWeightQ0_Type()
)
es2126PoEplusQoSWeightQ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSWeightQ0.setStatus("current")


class _Es2126PoEplusQoSWeightQ1_Type(Integer32):
    """Custom type es2126PoEplusQoSWeightQ1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126PoEplusQoSWeightQ1_Type.__name__ = "Integer32"
_Es2126PoEplusQoSWeightQ1_Object = MibScalar
es2126PoEplusQoSWeightQ1 = _Es2126PoEplusQoSWeightQ1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 7),
    _Es2126PoEplusQoSWeightQ1_Type()
)
es2126PoEplusQoSWeightQ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSWeightQ1.setStatus("current")


class _Es2126PoEplusQoSWeightQ2_Type(Integer32):
    """Custom type es2126PoEplusQoSWeightQ2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126PoEplusQoSWeightQ2_Type.__name__ = "Integer32"
_Es2126PoEplusQoSWeightQ2_Object = MibScalar
es2126PoEplusQoSWeightQ2 = _Es2126PoEplusQoSWeightQ2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 8),
    _Es2126PoEplusQoSWeightQ2_Type()
)
es2126PoEplusQoSWeightQ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSWeightQ2.setStatus("current")


class _Es2126PoEplusQoSWeightQ3_Type(Integer32):
    """Custom type es2126PoEplusQoSWeightQ3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Es2126PoEplusQoSWeightQ3_Type.__name__ = "Integer32"
_Es2126PoEplusQoSWeightQ3_Object = MibScalar
es2126PoEplusQoSWeightQ3 = _Es2126PoEplusQoSWeightQ3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 1, 9),
    _Es2126PoEplusQoSWeightQ3_Type()
)
es2126PoEplusQoSWeightQ3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSWeightQ3.setStatus("current")
_Es2126PoEplusQoSVIPPort_Type = DisplayString
_Es2126PoEplusQoSVIPPort_Object = MibScalar
es2126PoEplusQoSVIPPort = _Es2126PoEplusQoSVIPPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 2),
    _Es2126PoEplusQoSVIPPort_Type()
)
es2126PoEplusQoSVIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSVIPPort.setStatus("current")
_Es2126PoEplusQoS1pPriority_ObjectIdentity = ObjectIdentity
es2126PoEplusQoS1pPriority = _Es2126PoEplusQoS1pPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 3)
)
_Es2126PoEplusQoS1pPriorityTable_Object = MibTable
es2126PoEplusQoS1pPriorityTable = _Es2126PoEplusQoS1pPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusQoS1pPriorityTable.setStatus("current")
_Es2126PoEplusQoS1pPriorityEntry_Object = MibTableRow
es2126PoEplusQoS1pPriorityEntry = _Es2126PoEplusQoS1pPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 3, 1, 1)
)
es2126PoEplusQoS1pPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusQoS1pPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusQoS1pPriorityEntry.setStatus("current")


class _Es2126PoEplusQoS1pPriorityIndex_Type(Integer32):
    """Custom type es2126PoEplusQoS1pPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126PoEplusQoS1pPriorityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusQoS1pPriorityIndex_Object = MibTableColumn
es2126PoEplusQoS1pPriorityIndex = _Es2126PoEplusQoS1pPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 3, 1, 1, 1),
    _Es2126PoEplusQoS1pPriorityIndex_Type()
)
es2126PoEplusQoS1pPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusQoS1pPriorityIndex.setStatus("current")


class _Es2126PoEplusQoS1pPriorityValue_Type(Integer32):
    """Custom type es2126PoEplusQoS1pPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusQoS1pPriorityValue_Type.__name__ = "Integer32"
_Es2126PoEplusQoS1pPriorityValue_Object = MibTableColumn
es2126PoEplusQoS1pPriorityValue = _Es2126PoEplusQoS1pPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 3, 1, 1, 2),
    _Es2126PoEplusQoS1pPriorityValue_Type()
)
es2126PoEplusQoS1pPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusQoS1pPriorityValue.setStatus("current")


class _Es2126PoEplusQoS1pPriorityQueue_Type(Integer32):
    """Custom type es2126PoEplusQoS1pPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusQoS1pPriorityQueue_Type.__name__ = "Integer32"
_Es2126PoEplusQoS1pPriorityQueue_Object = MibTableColumn
es2126PoEplusQoS1pPriorityQueue = _Es2126PoEplusQoS1pPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 3, 1, 1, 3),
    _Es2126PoEplusQoS1pPriorityQueue_Type()
)
es2126PoEplusQoS1pPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoS1pPriorityQueue.setStatus("current")
_Es2126PoEplusQoSDTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126PoEplusQoSDTypeTOSPriority = _Es2126PoEplusQoSDTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 4)
)
_Es2126PoEplusQoSDTypeTOSPriorityTable_Object = MibTable
es2126PoEplusQoSDTypeTOSPriorityTable = _Es2126PoEplusQoSDTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSDTypeTOSPriorityTable.setStatus("current")
_Es2126PoEplusQoSDTypeTOSPriorityEntry_Object = MibTableRow
es2126PoEplusQoSDTypeTOSPriorityEntry = _Es2126PoEplusQoSDTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 4, 1, 1)
)
es2126PoEplusQoSDTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusQoSDTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSDTypeTOSPriorityEntry.setStatus("current")


class _Es2126PoEplusQoSDTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126PoEplusQoSDTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126PoEplusQoSDTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusQoSDTypeTOSPriorityIndex_Object = MibTableColumn
es2126PoEplusQoSDTypeTOSPriorityIndex = _Es2126PoEplusQoSDTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 4, 1, 1, 1),
    _Es2126PoEplusQoSDTypeTOSPriorityIndex_Type()
)
es2126PoEplusQoSDTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusQoSDTypeTOSPriorityIndex.setStatus("current")


class _Es2126PoEplusQoSDTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126PoEplusQoSDTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusQoSDTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSDTypeTOSPriorityValue_Object = MibTableColumn
es2126PoEplusQoSDTypeTOSPriorityValue = _Es2126PoEplusQoSDTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 4, 1, 1, 2),
    _Es2126PoEplusQoSDTypeTOSPriorityValue_Type()
)
es2126PoEplusQoSDTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusQoSDTypeTOSPriorityValue.setStatus("current")


class _Es2126PoEplusQoSDTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126PoEplusQoSDTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusQoSDTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSDTypeTOSPriorityQueue_Object = MibTableColumn
es2126PoEplusQoSDTypeTOSPriorityQueue = _Es2126PoEplusQoSDTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 4, 1, 1, 3),
    _Es2126PoEplusQoSDTypeTOSPriorityQueue_Type()
)
es2126PoEplusQoSDTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSDTypeTOSPriorityQueue.setStatus("current")
_Es2126PoEplusQoSTTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126PoEplusQoSTTypeTOSPriority = _Es2126PoEplusQoSTTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 5)
)
_Es2126PoEplusQoSTTypeTOSPriorityTable_Object = MibTable
es2126PoEplusQoSTTypeTOSPriorityTable = _Es2126PoEplusQoSTTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSTTypeTOSPriorityTable.setStatus("current")
_Es2126PoEplusQoSTTypeTOSPriorityEntry_Object = MibTableRow
es2126PoEplusQoSTTypeTOSPriorityEntry = _Es2126PoEplusQoSTTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 5, 1, 1)
)
es2126PoEplusQoSTTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusQoSTTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSTTypeTOSPriorityEntry.setStatus("current")


class _Es2126PoEplusQoSTTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126PoEplusQoSTTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126PoEplusQoSTTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusQoSTTypeTOSPriorityIndex_Object = MibTableColumn
es2126PoEplusQoSTTypeTOSPriorityIndex = _Es2126PoEplusQoSTTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 5, 1, 1, 1),
    _Es2126PoEplusQoSTTypeTOSPriorityIndex_Type()
)
es2126PoEplusQoSTTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusQoSTTypeTOSPriorityIndex.setStatus("current")


class _Es2126PoEplusQoSTTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126PoEplusQoSTTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusQoSTTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSTTypeTOSPriorityValue_Object = MibTableColumn
es2126PoEplusQoSTTypeTOSPriorityValue = _Es2126PoEplusQoSTTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 5, 1, 1, 2),
    _Es2126PoEplusQoSTTypeTOSPriorityValue_Type()
)
es2126PoEplusQoSTTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusQoSTTypeTOSPriorityValue.setStatus("current")


class _Es2126PoEplusQoSTTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126PoEplusQoSTTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusQoSTTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSTTypeTOSPriorityQueue_Object = MibTableColumn
es2126PoEplusQoSTTypeTOSPriorityQueue = _Es2126PoEplusQoSTTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 5, 1, 1, 3),
    _Es2126PoEplusQoSTTypeTOSPriorityQueue_Type()
)
es2126PoEplusQoSTTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSTTypeTOSPriorityQueue.setStatus("current")
_Es2126PoEplusQoSRTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126PoEplusQoSRTypeTOSPriority = _Es2126PoEplusQoSRTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 6)
)
_Es2126PoEplusQoSRTypeTOSPriorityTable_Object = MibTable
es2126PoEplusQoSRTypeTOSPriorityTable = _Es2126PoEplusQoSRTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 6, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSRTypeTOSPriorityTable.setStatus("current")
_Es2126PoEplusQoSRTypeTOSPriorityEntry_Object = MibTableRow
es2126PoEplusQoSRTypeTOSPriorityEntry = _Es2126PoEplusQoSRTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 6, 1, 1)
)
es2126PoEplusQoSRTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusQoSRTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSRTypeTOSPriorityEntry.setStatus("current")


class _Es2126PoEplusQoSRTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126PoEplusQoSRTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126PoEplusQoSRTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusQoSRTypeTOSPriorityIndex_Object = MibTableColumn
es2126PoEplusQoSRTypeTOSPriorityIndex = _Es2126PoEplusQoSRTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 6, 1, 1, 1),
    _Es2126PoEplusQoSRTypeTOSPriorityIndex_Type()
)
es2126PoEplusQoSRTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusQoSRTypeTOSPriorityIndex.setStatus("current")


class _Es2126PoEplusQoSRTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126PoEplusQoSRTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusQoSRTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSRTypeTOSPriorityValue_Object = MibTableColumn
es2126PoEplusQoSRTypeTOSPriorityValue = _Es2126PoEplusQoSRTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 6, 1, 1, 2),
    _Es2126PoEplusQoSRTypeTOSPriorityValue_Type()
)
es2126PoEplusQoSRTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusQoSRTypeTOSPriorityValue.setStatus("current")


class _Es2126PoEplusQoSRTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126PoEplusQoSRTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusQoSRTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSRTypeTOSPriorityQueue_Object = MibTableColumn
es2126PoEplusQoSRTypeTOSPriorityQueue = _Es2126PoEplusQoSRTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 6, 1, 1, 3),
    _Es2126PoEplusQoSRTypeTOSPriorityQueue_Type()
)
es2126PoEplusQoSRTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSRTypeTOSPriorityQueue.setStatus("current")
_Es2126PoEplusQoSMTypeTOSPriority_ObjectIdentity = ObjectIdentity
es2126PoEplusQoSMTypeTOSPriority = _Es2126PoEplusQoSMTypeTOSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 7)
)
_Es2126PoEplusQoSMTypeTOSPriorityTable_Object = MibTable
es2126PoEplusQoSMTypeTOSPriorityTable = _Es2126PoEplusQoSMTypeTOSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 7, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSMTypeTOSPriorityTable.setStatus("current")
_Es2126PoEplusQoSMTypeTOSPriorityEntry_Object = MibTableRow
es2126PoEplusQoSMTypeTOSPriorityEntry = _Es2126PoEplusQoSMTypeTOSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 7, 1, 1)
)
es2126PoEplusQoSMTypeTOSPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusQoSMTypeTOSPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSMTypeTOSPriorityEntry.setStatus("current")


class _Es2126PoEplusQoSMTypeTOSPriorityIndex_Type(Integer32):
    """Custom type es2126PoEplusQoSMTypeTOSPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Es2126PoEplusQoSMTypeTOSPriorityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusQoSMTypeTOSPriorityIndex_Object = MibTableColumn
es2126PoEplusQoSMTypeTOSPriorityIndex = _Es2126PoEplusQoSMTypeTOSPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 7, 1, 1, 1),
    _Es2126PoEplusQoSMTypeTOSPriorityIndex_Type()
)
es2126PoEplusQoSMTypeTOSPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusQoSMTypeTOSPriorityIndex.setStatus("current")


class _Es2126PoEplusQoSMTypeTOSPriorityValue_Type(Integer32):
    """Custom type es2126PoEplusQoSMTypeTOSPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusQoSMTypeTOSPriorityValue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSMTypeTOSPriorityValue_Object = MibTableColumn
es2126PoEplusQoSMTypeTOSPriorityValue = _Es2126PoEplusQoSMTypeTOSPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 7, 1, 1, 2),
    _Es2126PoEplusQoSMTypeTOSPriorityValue_Type()
)
es2126PoEplusQoSMTypeTOSPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusQoSMTypeTOSPriorityValue.setStatus("current")


class _Es2126PoEplusQoSMTypeTOSPriorityQueue_Type(Integer32):
    """Custom type es2126PoEplusQoSMTypeTOSPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusQoSMTypeTOSPriorityQueue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSMTypeTOSPriorityQueue_Object = MibTableColumn
es2126PoEplusQoSMTypeTOSPriorityQueue = _Es2126PoEplusQoSMTypeTOSPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 7, 1, 1, 3),
    _Es2126PoEplusQoSMTypeTOSPriorityQueue_Type()
)
es2126PoEplusQoSMTypeTOSPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSMTypeTOSPriorityQueue.setStatus("current")
_Es2126PoEplusQoSDSCPPriority_ObjectIdentity = ObjectIdentity
es2126PoEplusQoSDSCPPriority = _Es2126PoEplusQoSDSCPPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 8)
)
_Es2126PoEplusQoSDSCPPriorityTable_Object = MibTable
es2126PoEplusQoSDSCPPriorityTable = _Es2126PoEplusQoSDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 8, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSDSCPPriorityTable.setStatus("current")
_Es2126PoEplusQoSDSCPPriorityEntry_Object = MibTableRow
es2126PoEplusQoSDSCPPriorityEntry = _Es2126PoEplusQoSDSCPPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 8, 1, 1)
)
es2126PoEplusQoSDSCPPriorityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusQoSDSCPPriorityIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusQoSDSCPPriorityEntry.setStatus("current")


class _Es2126PoEplusQoSDSCPPriorityIndex_Type(Integer32):
    """Custom type es2126PoEplusQoSDSCPPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Es2126PoEplusQoSDSCPPriorityIndex_Type.__name__ = "Integer32"
_Es2126PoEplusQoSDSCPPriorityIndex_Object = MibTableColumn
es2126PoEplusQoSDSCPPriorityIndex = _Es2126PoEplusQoSDSCPPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 8, 1, 1, 1),
    _Es2126PoEplusQoSDSCPPriorityIndex_Type()
)
es2126PoEplusQoSDSCPPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusQoSDSCPPriorityIndex.setStatus("current")


class _Es2126PoEplusQoSDSCPPriorityValue_Type(Integer32):
    """Custom type es2126PoEplusQoSDSCPPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Es2126PoEplusQoSDSCPPriorityValue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSDSCPPriorityValue_Object = MibTableColumn
es2126PoEplusQoSDSCPPriorityValue = _Es2126PoEplusQoSDSCPPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 8, 1, 1, 2),
    _Es2126PoEplusQoSDSCPPriorityValue_Type()
)
es2126PoEplusQoSDSCPPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusQoSDSCPPriorityValue.setStatus("current")


class _Es2126PoEplusQoSDSCPPriorityQueue_Type(Integer32):
    """Custom type es2126PoEplusQoSDSCPPriorityQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusQoSDSCPPriorityQueue_Type.__name__ = "Integer32"
_Es2126PoEplusQoSDSCPPriorityQueue_Object = MibTableColumn
es2126PoEplusQoSDSCPPriorityQueue = _Es2126PoEplusQoSDSCPPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 16, 8, 1, 1, 3),
    _Es2126PoEplusQoSDSCPPriorityQueue_Type()
)
es2126PoEplusQoSDSCPPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusQoSDSCPPriorityQueue.setStatus("current")
_Es2126PoEplusVlan_ObjectIdentity = ObjectIdentity
es2126PoEplusVlan = _Es2126PoEplusVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17)
)
_Es2126PoEplusVlanModeConfig_ObjectIdentity = ObjectIdentity
es2126PoEplusVlanModeConfig = _Es2126PoEplusVlanModeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 1)
)


class _Es2126PoEplusVlanMode_Type(Integer32):
    """Custom type es2126PoEplusVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusVlanMode_Type.__name__ = "Integer32"
_Es2126PoEplusVlanMode_Object = MibScalar
es2126PoEplusVlanMode = _Es2126PoEplusVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 1, 1),
    _Es2126PoEplusVlanMode_Type()
)
es2126PoEplusVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVlanMode.setStatus("current")


class _Es2126PoEplusSymmetricVlan_Type(Integer32):
    """Custom type es2126PoEplusSymmetricVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusSymmetricVlan_Type.__name__ = "Integer32"
_Es2126PoEplusSymmetricVlan_Object = MibScalar
es2126PoEplusSymmetricVlan = _Es2126PoEplusSymmetricVlan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 1, 2),
    _Es2126PoEplusSymmetricVlan_Type()
)
es2126PoEplusSymmetricVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusSymmetricVlan.setStatus("current")


class _Es2126PoEplusVlanSVL_Type(Integer32):
    """Custom type es2126PoEplusVlanSVL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusVlanSVL_Type.__name__ = "Integer32"
_Es2126PoEplusVlanSVL_Object = MibScalar
es2126PoEplusVlanSVL = _Es2126PoEplusVlanSVL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 1, 3),
    _Es2126PoEplusVlanSVL_Type()
)
es2126PoEplusVlanSVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVlanSVL.setStatus("current")


class _Es2126PoEplusDoubleTag_Type(Integer32):
    """Custom type es2126PoEplusDoubleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusDoubleTag_Type.__name__ = "Integer32"
_Es2126PoEplusDoubleTag_Object = MibScalar
es2126PoEplusDoubleTag = _Es2126PoEplusDoubleTag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 1, 4),
    _Es2126PoEplusDoubleTag_Type()
)
es2126PoEplusDoubleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDoubleTag.setStatus("current")


class _Es2126PoEplusUpLinkPort_Type(Integer32):
    """Custom type es2126PoEplusUpLinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusUpLinkPort_Type.__name__ = "Integer32"
_Es2126PoEplusUpLinkPort_Object = MibScalar
es2126PoEplusUpLinkPort = _Es2126PoEplusUpLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 1, 5),
    _Es2126PoEplusUpLinkPort_Type()
)
es2126PoEplusUpLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusUpLinkPort.setStatus("current")
_Es2126PoEplusTagBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2126PoEplusTagBasedVlanGroup = _Es2126PoEplusTagBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2)
)


class _Es2126PoEplusTagBasedVlanNumbers_Type(Integer32):
    """Custom type es2126PoEplusTagBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusTagBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2126PoEplusTagBasedVlanNumbers_Object = MibScalar
es2126PoEplusTagBasedVlanNumbers = _Es2126PoEplusTagBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 1),
    _Es2126PoEplusTagBasedVlanNumbers_Type()
)
es2126PoEplusTagBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanNumbers.setStatus("current")


class _Es2126PoEplusTagBasedCreateStatus_Type(Integer32):
    """Custom type es2126PoEplusTagBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Es2126PoEplusTagBasedCreateStatus_Type.__name__ = "Integer32"
_Es2126PoEplusTagBasedCreateStatus_Object = MibScalar
es2126PoEplusTagBasedCreateStatus = _Es2126PoEplusTagBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 2),
    _Es2126PoEplusTagBasedCreateStatus_Type()
)
es2126PoEplusTagBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedCreateStatus.setStatus("current")
_Es2126PoEplusTagBasedVlanTable_Object = MibTable
es2126PoEplusTagBasedVlanTable = _Es2126PoEplusTagBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3)
)
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanTable.setStatus("current")
_Es2126PoEplusTagBasedVlanEntry_Object = MibTableRow
es2126PoEplusTagBasedVlanEntry = _Es2126PoEplusTagBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3, 1)
)
es2126PoEplusTagBasedVlanEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusTagBasedVlanVid"),
)
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanEntry.setStatus("current")


class _Es2126PoEplusTagBasedVlanVid_Type(Integer32):
    """Custom type es2126PoEplusTagBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusTagBasedVlanVid_Type.__name__ = "Integer32"
_Es2126PoEplusTagBasedVlanVid_Object = MibTableColumn
es2126PoEplusTagBasedVlanVid = _Es2126PoEplusTagBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3, 1, 1),
    _Es2126PoEplusTagBasedVlanVid_Type()
)
es2126PoEplusTagBasedVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanVid.setStatus("current")
_Es2126PoEplusTagBasedVlanName_Type = DisplayString
_Es2126PoEplusTagBasedVlanName_Object = MibTableColumn
es2126PoEplusTagBasedVlanName = _Es2126PoEplusTagBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3, 1, 2),
    _Es2126PoEplusTagBasedVlanName_Type()
)
es2126PoEplusTagBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanName.setStatus("current")
_Es2126PoEplusTagBasedVlanMember_Type = DisplayString
_Es2126PoEplusTagBasedVlanMember_Object = MibTableColumn
es2126PoEplusTagBasedVlanMember = _Es2126PoEplusTagBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3, 1, 3),
    _Es2126PoEplusTagBasedVlanMember_Type()
)
es2126PoEplusTagBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanMember.setStatus("current")
_Es2126PoEplusTagBasedVlanUntag_Type = DisplayString
_Es2126PoEplusTagBasedVlanUntag_Object = MibTableColumn
es2126PoEplusTagBasedVlanUntag = _Es2126PoEplusTagBasedVlanUntag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3, 1, 4),
    _Es2126PoEplusTagBasedVlanUntag_Type()
)
es2126PoEplusTagBasedVlanUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanUntag.setStatus("current")


class _Es2126PoEplusTagBasedVlanRowStatus_Type(Integer32):
    """Custom type es2126PoEplusTagBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126PoEplusTagBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2126PoEplusTagBasedVlanRowStatus_Object = MibTableColumn
es2126PoEplusTagBasedVlanRowStatus = _Es2126PoEplusTagBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 2, 3, 1, 5),
    _Es2126PoEplusTagBasedVlanRowStatus_Type()
)
es2126PoEplusTagBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTagBasedVlanRowStatus.setStatus("current")
_Es2126PoEplusVlanPvid_ObjectIdentity = ObjectIdentity
es2126PoEplusVlanPvid = _Es2126PoEplusVlanPvid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3)
)
_Es2126PoEplusVlanPvidTable_Object = MibTable
es2126PoEplusVlanPvidTable = _Es2126PoEplusVlanPvidTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusVlanPvidTable.setStatus("current")
_Es2126PoEplusVlanPvidEntry_Object = MibTableRow
es2126PoEplusVlanPvidEntry = _Es2126PoEplusVlanPvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3, 1, 1)
)
es2126PoEplusVlanPvidEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusVlanPvidPort"),
)
if mibBuilder.loadTexts:
    es2126PoEplusVlanPvidEntry.setStatus("current")


class _Es2126PoEplusVlanPvidPort_Type(Integer32):
    """Custom type es2126PoEplusVlanPvidPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusVlanPvidPort_Type.__name__ = "Integer32"
_Es2126PoEplusVlanPvidPort_Object = MibTableColumn
es2126PoEplusVlanPvidPort = _Es2126PoEplusVlanPvidPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3, 1, 1, 1),
    _Es2126PoEplusVlanPvidPort_Type()
)
es2126PoEplusVlanPvidPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusVlanPvidPort.setStatus("current")


class _Es2126PoEplusVlanPvidValue_Type(Integer32):
    """Custom type es2126PoEplusVlanPvidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusVlanPvidValue_Type.__name__ = "Integer32"
_Es2126PoEplusVlanPvidValue_Object = MibTableColumn
es2126PoEplusVlanPvidValue = _Es2126PoEplusVlanPvidValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3, 1, 1, 2),
    _Es2126PoEplusVlanPvidValue_Type()
)
es2126PoEplusVlanPvidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVlanPvidValue.setStatus("current")


class _Es2126PoEplusVlanPvidDefaultPriority_Type(Integer32):
    """Custom type es2126PoEplusVlanPvidDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusVlanPvidDefaultPriority_Type.__name__ = "Integer32"
_Es2126PoEplusVlanPvidDefaultPriority_Object = MibTableColumn
es2126PoEplusVlanPvidDefaultPriority = _Es2126PoEplusVlanPvidDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3, 1, 1, 3),
    _Es2126PoEplusVlanPvidDefaultPriority_Type()
)
es2126PoEplusVlanPvidDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVlanPvidDefaultPriority.setStatus("current")


class _Es2126PoEplusVlanPvidDropUntag_Type(Integer32):
    """Custom type es2126PoEplusVlanPvidDropUntag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es2126PoEplusVlanPvidDropUntag_Type.__name__ = "Integer32"
_Es2126PoEplusVlanPvidDropUntag_Object = MibTableColumn
es2126PoEplusVlanPvidDropUntag = _Es2126PoEplusVlanPvidDropUntag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 3, 1, 1, 4),
    _Es2126PoEplusVlanPvidDropUntag_Type()
)
es2126PoEplusVlanPvidDropUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusVlanPvidDropUntag.setStatus("current")
_Es2126PoEplusPortBasedVlanGroup_ObjectIdentity = ObjectIdentity
es2126PoEplusPortBasedVlanGroup = _Es2126PoEplusPortBasedVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4)
)


class _Es2126PoEplusPortBasedVlanNumbers_Type(Integer32):
    """Custom type es2126PoEplusPortBasedVlanNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusPortBasedVlanNumbers_Type.__name__ = "Integer32"
_Es2126PoEplusPortBasedVlanNumbers_Object = MibScalar
es2126PoEplusPortBasedVlanNumbers = _Es2126PoEplusPortBasedVlanNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 1),
    _Es2126PoEplusPortBasedVlanNumbers_Type()
)
es2126PoEplusPortBasedVlanNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanNumbers.setStatus("current")


class _Es2126PoEplusPortBasedCreateStatus_Type(Integer32):
    """Custom type es2126PoEplusPortBasedCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPortBasedCreateStatus_Type.__name__ = "Integer32"
_Es2126PoEplusPortBasedCreateStatus_Object = MibScalar
es2126PoEplusPortBasedCreateStatus = _Es2126PoEplusPortBasedCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 2),
    _Es2126PoEplusPortBasedCreateStatus_Type()
)
es2126PoEplusPortBasedCreateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedCreateStatus.setStatus("current")
_Es2126PoEplusPortBasedVlanTable_Object = MibTable
es2126PoEplusPortBasedVlanTable = _Es2126PoEplusPortBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 3)
)
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanTable.setStatus("current")
_Es2126PoEplusPortBasedVlanEntry_Object = MibTableRow
es2126PoEplusPortBasedVlanEntry = _Es2126PoEplusPortBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 3, 1)
)
es2126PoEplusPortBasedVlanEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPortBasedVlanIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanEntry.setStatus("current")


class _Es2126PoEplusPortBasedVlanIndex_Type(Integer32):
    """Custom type es2126PoEplusPortBasedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusPortBasedVlanIndex_Type.__name__ = "Integer32"
_Es2126PoEplusPortBasedVlanIndex_Object = MibTableColumn
es2126PoEplusPortBasedVlanIndex = _Es2126PoEplusPortBasedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 3, 1, 1),
    _Es2126PoEplusPortBasedVlanIndex_Type()
)
es2126PoEplusPortBasedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanIndex.setStatus("current")
_Es2126PoEplusPortBasedVlanName_Type = DisplayString
_Es2126PoEplusPortBasedVlanName_Object = MibTableColumn
es2126PoEplusPortBasedVlanName = _Es2126PoEplusPortBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 3, 1, 2),
    _Es2126PoEplusPortBasedVlanName_Type()
)
es2126PoEplusPortBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanName.setStatus("current")
_Es2126PoEplusPortBasedVlanMember_Type = DisplayString
_Es2126PoEplusPortBasedVlanMember_Object = MibTableColumn
es2126PoEplusPortBasedVlanMember = _Es2126PoEplusPortBasedVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 3, 1, 3),
    _Es2126PoEplusPortBasedVlanMember_Type()
)
es2126PoEplusPortBasedVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanMember.setStatus("current")


class _Es2126PoEplusPortBasedVlanRowStatus_Type(Integer32):
    """Custom type es2126PoEplusPortBasedVlanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Es2126PoEplusPortBasedVlanRowStatus_Type.__name__ = "Integer32"
_Es2126PoEplusPortBasedVlanRowStatus_Object = MibTableColumn
es2126PoEplusPortBasedVlanRowStatus = _Es2126PoEplusPortBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 4, 3, 1, 4),
    _Es2126PoEplusPortBasedVlanRowStatus_Type()
)
es2126PoEplusPortBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPortBasedVlanRowStatus.setStatus("current")
_Es2126PoEplusManagementVlan_ObjectIdentity = ObjectIdentity
es2126PoEplusManagementVlan = _Es2126PoEplusManagementVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 5)
)


class _Es2126PoEplusManagementVlanState_Type(Integer32):
    """Custom type es2126PoEplusManagementVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusManagementVlanState_Type.__name__ = "Integer32"
_Es2126PoEplusManagementVlanState_Object = MibScalar
es2126PoEplusManagementVlanState = _Es2126PoEplusManagementVlanState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 5, 1),
    _Es2126PoEplusManagementVlanState_Type()
)
es2126PoEplusManagementVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementVlanState.setStatus("current")


class _Es2126PoEplusManagementVlanVid_Type(Integer32):
    """Custom type es2126PoEplusManagementVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es2126PoEplusManagementVlanVid_Type.__name__ = "Integer32"
_Es2126PoEplusManagementVlanVid_Object = MibScalar
es2126PoEplusManagementVlanVid = _Es2126PoEplusManagementVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 17, 5, 2),
    _Es2126PoEplusManagementVlanVid_Type()
)
es2126PoEplusManagementVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusManagementVlanVid.setStatus("current")
_Es2126PoEplusDot1X_ObjectIdentity = ObjectIdentity
es2126PoEplusDot1X = _Es2126PoEplusDot1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18)
)
_Es2126PoEplusDot1XStateSetting_ObjectIdentity = ObjectIdentity
es2126PoEplusDot1XStateSetting = _Es2126PoEplusDot1XStateSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1)
)
_Es2126PoEplusRadiusServer_Type = IpAddress
_Es2126PoEplusRadiusServer_Object = MibScalar
es2126PoEplusRadiusServer = _Es2126PoEplusRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1, 1),
    _Es2126PoEplusRadiusServer_Type()
)
es2126PoEplusRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusRadiusServer.setStatus("current")


class _Es2126PoEplusDot1XPort_Type(Integer32):
    """Custom type es2126PoEplusDot1XPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusDot1XPort_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPort_Object = MibScalar
es2126PoEplusDot1XPort = _Es2126PoEplusDot1XPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1, 2),
    _Es2126PoEplusDot1XPort_Type()
)
es2126PoEplusDot1XPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPort.setStatus("current")
_Es2126PoEplusSecretKey_Type = DisplayString
_Es2126PoEplusSecretKey_Object = MibScalar
es2126PoEplusSecretKey = _Es2126PoEplusSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1, 3),
    _Es2126PoEplusSecretKey_Type()
)
es2126PoEplusSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusSecretKey.setStatus("current")


class _Es2126PoEplusAccountingService_Type(Integer32):
    """Custom type es2126PoEplusAccountingService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusAccountingService_Type.__name__ = "Integer32"
_Es2126PoEplusAccountingService_Object = MibScalar
es2126PoEplusAccountingService = _Es2126PoEplusAccountingService_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1, 4),
    _Es2126PoEplusAccountingService_Type()
)
es2126PoEplusAccountingService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountingService.setStatus("current")
_Es2126PoEplusAccountingServer_Type = IpAddress
_Es2126PoEplusAccountingServer_Object = MibScalar
es2126PoEplusAccountingServer = _Es2126PoEplusAccountingServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1, 5),
    _Es2126PoEplusAccountingServer_Type()
)
es2126PoEplusAccountingServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountingServer.setStatus("current")


class _Es2126PoEplusAccountingPort_Type(Integer32):
    """Custom type es2126PoEplusAccountingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusAccountingPort_Type.__name__ = "Integer32"
_Es2126PoEplusAccountingPort_Object = MibScalar
es2126PoEplusAccountingPort = _Es2126PoEplusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 1, 6),
    _Es2126PoEplusAccountingPort_Type()
)
es2126PoEplusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusAccountingPort.setStatus("current")
_Es2126PoEplusDot1XPortSecurityManagement_ObjectIdentity = ObjectIdentity
es2126PoEplusDot1XPortSecurityManagement = _Es2126PoEplusDot1XPortSecurityManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2)
)
_Es2126PoEplusDot1XPortSecurityTable_Object = MibTable
es2126PoEplusDot1XPortSecurityTable = _Es2126PoEplusDot1XPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityTable.setStatus("current")
_Es2126PoEplusDot1XPortSecurityEntry_Object = MibTableRow
es2126PoEplusDot1XPortSecurityEntry = _Es2126PoEplusDot1XPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1)
)
es2126PoEplusDot1XPortSecurityEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusDot1XPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityEntry.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityPortIndex_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusDot1XPortSecurityPortIndex_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityPortIndex_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityPortIndex = _Es2126PoEplusDot1XPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 1),
    _Es2126PoEplusDot1XPortSecurityPortIndex_Type()
)
es2126PoEplusDot1XPortSecurityPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityPortIndex.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityMode_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusDot1XPortSecurityMode_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityMode_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityMode = _Es2126PoEplusDot1XPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 2),
    _Es2126PoEplusDot1XPortSecurityMode_Type()
)
es2126PoEplusDot1XPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityMode.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityPortControl_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusDot1XPortSecurityPortControl_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityPortControl_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityPortControl = _Es2126PoEplusDot1XPortSecurityPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 3),
    _Es2126PoEplusDot1XPortSecurityPortControl_Type()
)
es2126PoEplusDot1XPortSecurityPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityPortControl.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityReAuthMax_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityReAuthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2126PoEplusDot1XPortSecurityReAuthMax_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityReAuthMax_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityReAuthMax = _Es2126PoEplusDot1XPortSecurityReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 4),
    _Es2126PoEplusDot1XPortSecurityReAuthMax_Type()
)
es2126PoEplusDot1XPortSecurityReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityReAuthMax.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityTxPeriod_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusDot1XPortSecurityTxPeriod_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityTxPeriod_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityTxPeriod = _Es2126PoEplusDot1XPortSecurityTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 5),
    _Es2126PoEplusDot1XPortSecurityTxPeriod_Type()
)
es2126PoEplusDot1XPortSecurityTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityTxPeriod.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityQuietPeriod_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es2126PoEplusDot1XPortSecurityQuietPeriod_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityQuietPeriod_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityQuietPeriod = _Es2126PoEplusDot1XPortSecurityQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 6),
    _Es2126PoEplusDot1XPortSecurityQuietPeriod_Type()
)
es2126PoEplusDot1XPortSecurityQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityQuietPeriod.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityReAuthEnabled_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityReAuthEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusDot1XPortSecurityReAuthEnabled_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityReAuthEnabled_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityReAuthEnabled = _Es2126PoEplusDot1XPortSecurityReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 7),
    _Es2126PoEplusDot1XPortSecurityReAuthEnabled_Type()
)
es2126PoEplusDot1XPortSecurityReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityReAuthEnabled.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityReAuthPeriod_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusDot1XPortSecurityReAuthPeriod_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityReAuthPeriod_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityReAuthPeriod = _Es2126PoEplusDot1XPortSecurityReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 8),
    _Es2126PoEplusDot1XPortSecurityReAuthPeriod_Type()
)
es2126PoEplusDot1XPortSecurityReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityReAuthPeriod.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityMaxRequest_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityMaxRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Es2126PoEplusDot1XPortSecurityMaxRequest_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityMaxRequest_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityMaxRequest = _Es2126PoEplusDot1XPortSecurityMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 9),
    _Es2126PoEplusDot1XPortSecurityMaxRequest_Type()
)
es2126PoEplusDot1XPortSecurityMaxRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityMaxRequest.setStatus("current")


class _Es2126PoEplusDot1XPortSecuritySuppTimeout_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecuritySuppTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusDot1XPortSecuritySuppTimeout_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecuritySuppTimeout_Object = MibTableColumn
es2126PoEplusDot1XPortSecuritySuppTimeout = _Es2126PoEplusDot1XPortSecuritySuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 10),
    _Es2126PoEplusDot1XPortSecuritySuppTimeout_Type()
)
es2126PoEplusDot1XPortSecuritySuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecuritySuppTimeout.setStatus("current")


class _Es2126PoEplusDot1XPortSecurityServerTimeout_Type(Integer32):
    """Custom type es2126PoEplusDot1XPortSecurityServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusDot1XPortSecurityServerTimeout_Type.__name__ = "Integer32"
_Es2126PoEplusDot1XPortSecurityServerTimeout_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityServerTimeout = _Es2126PoEplusDot1XPortSecurityServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 11),
    _Es2126PoEplusDot1XPortSecurityServerTimeout_Type()
)
es2126PoEplusDot1XPortSecurityServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityServerTimeout.setStatus("current")
_Es2126PoEplusDot1XPortSecurityStatus_Type = DisplayString
_Es2126PoEplusDot1XPortSecurityStatus_Object = MibTableColumn
es2126PoEplusDot1XPortSecurityStatus = _Es2126PoEplusDot1XPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 18, 2, 1, 1, 12),
    _Es2126PoEplusDot1XPortSecurityStatus_Type()
)
es2126PoEplusDot1XPortSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusDot1XPortSecurityStatus.setStatus("current")
_Es2126PoEplusTrunkInfo_ObjectIdentity = ObjectIdentity
es2126PoEplusTrunkInfo = _Es2126PoEplusTrunkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19)
)
_Es2126PoEplusTrunkPort_ObjectIdentity = ObjectIdentity
es2126PoEplusTrunkPort = _Es2126PoEplusTrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1)
)
_Es2126PoEplusTrunkPortTable_Object = MibTable
es2126PoEplusTrunkPortTable = _Es2126PoEplusTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortTable.setStatus("current")
_Es2126PoEplusTrunkPortEntry_Object = MibTableRow
es2126PoEplusTrunkPortEntry = _Es2126PoEplusTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1)
)
es2126PoEplusTrunkPortEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortEntry.setStatus("current")


class _Es2126PoEplusTrunkPortIndex_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusTrunkPortIndex_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortIndex_Object = MibTableColumn
es2126PoEplusTrunkPortIndex = _Es2126PoEplusTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 1),
    _Es2126PoEplusTrunkPortIndex_Type()
)
es2126PoEplusTrunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortIndex.setStatus("current")


class _Es2126PoEplusTrunkPortMethod_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusTrunkPortMethod_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortMethod_Object = MibTableColumn
es2126PoEplusTrunkPortMethod = _Es2126PoEplusTrunkPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 2),
    _Es2126PoEplusTrunkPortMethod_Type()
)
es2126PoEplusTrunkPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortMethod.setStatus("current")


class _Es2126PoEplusTrunkPortGroup_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Es2126PoEplusTrunkPortGroup_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortGroup_Object = MibTableColumn
es2126PoEplusTrunkPortGroup = _Es2126PoEplusTrunkPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 3),
    _Es2126PoEplusTrunkPortGroup_Type()
)
es2126PoEplusTrunkPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortGroup.setStatus("current")


class _Es2126PoEplusTrunkPortActiveLacp_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortActiveLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusTrunkPortActiveLacp_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortActiveLacp_Object = MibTableColumn
es2126PoEplusTrunkPortActiveLacp = _Es2126PoEplusTrunkPortActiveLacp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 4),
    _Es2126PoEplusTrunkPortActiveLacp_Type()
)
es2126PoEplusTrunkPortActiveLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortActiveLacp.setStatus("current")


class _Es2126PoEplusTrunkPortAggtr_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortAggtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusTrunkPortAggtr_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortAggtr_Object = MibTableColumn
es2126PoEplusTrunkPortAggtr = _Es2126PoEplusTrunkPortAggtr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 5),
    _Es2126PoEplusTrunkPortAggtr_Type()
)
es2126PoEplusTrunkPortAggtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortAggtr.setStatus("current")


class _Es2126PoEplusTrunkPortStatus_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusTrunkPortStatus_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortStatus_Object = MibTableColumn
es2126PoEplusTrunkPortStatus = _Es2126PoEplusTrunkPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 6),
    _Es2126PoEplusTrunkPortStatus_Type()
)
es2126PoEplusTrunkPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortStatus.setStatus("current")


class _Es2126PoEplusTrunkPortCurrentMode_Type(Integer32):
    """Custom type es2126PoEplusTrunkPortCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusTrunkPortCurrentMode_Type.__name__ = "Integer32"
_Es2126PoEplusTrunkPortCurrentMode_Object = MibTableColumn
es2126PoEplusTrunkPortCurrentMode = _Es2126PoEplusTrunkPortCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 1, 1, 1, 7),
    _Es2126PoEplusTrunkPortCurrentMode_Type()
)
es2126PoEplusTrunkPortCurrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusTrunkPortCurrentMode.setStatus("current")
_Es2126PoEplusAggregatorView_ObjectIdentity = ObjectIdentity
es2126PoEplusAggregatorView = _Es2126PoEplusAggregatorView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2)
)
_Es2126PoEplusAggregatorViewTable_Object = MibTable
es2126PoEplusAggregatorViewTable = _Es2126PoEplusAggregatorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    es2126PoEplusAggregatorViewTable.setStatus("current")
_Es2126PoEplusAggregatorViewEntry_Object = MibTableRow
es2126PoEplusAggregatorViewEntry = _Es2126PoEplusAggregatorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2, 1, 1)
)
es2126PoEplusAggregatorViewEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusAggregatorViewIndex"),
)
if mibBuilder.loadTexts:
    es2126PoEplusAggregatorViewEntry.setStatus("current")


class _Es2126PoEplusAggregatorViewIndex_Type(Integer32):
    """Custom type es2126PoEplusAggregatorViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es2126PoEplusAggregatorViewIndex_Type.__name__ = "Integer32"
_Es2126PoEplusAggregatorViewIndex_Object = MibTableColumn
es2126PoEplusAggregatorViewIndex = _Es2126PoEplusAggregatorViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2, 1, 1, 1),
    _Es2126PoEplusAggregatorViewIndex_Type()
)
es2126PoEplusAggregatorViewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusAggregatorViewIndex.setStatus("current")


class _Es2126PoEplusAggregatorViewMethod_Type(Integer32):
    """Custom type es2126PoEplusAggregatorViewMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusAggregatorViewMethod_Type.__name__ = "Integer32"
_Es2126PoEplusAggregatorViewMethod_Object = MibTableColumn
es2126PoEplusAggregatorViewMethod = _Es2126PoEplusAggregatorViewMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2, 1, 1, 2),
    _Es2126PoEplusAggregatorViewMethod_Type()
)
es2126PoEplusAggregatorViewMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusAggregatorViewMethod.setStatus("current")
_Es2126PoEplusAggregatorViewMemberPorts_Type = DisplayString
_Es2126PoEplusAggregatorViewMemberPorts_Object = MibTableColumn
es2126PoEplusAggregatorViewMemberPorts = _Es2126PoEplusAggregatorViewMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2, 1, 1, 3),
    _Es2126PoEplusAggregatorViewMemberPorts_Type()
)
es2126PoEplusAggregatorViewMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusAggregatorViewMemberPorts.setStatus("current")
_Es2126PoEplusAggregatorViewReadyPorts_Type = DisplayString
_Es2126PoEplusAggregatorViewReadyPorts_Object = MibTableColumn
es2126PoEplusAggregatorViewReadyPorts = _Es2126PoEplusAggregatorViewReadyPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 2, 1, 1, 4),
    _Es2126PoEplusAggregatorViewReadyPorts_Type()
)
es2126PoEplusAggregatorViewReadyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusAggregatorViewReadyPorts.setStatus("current")
_Es2126PoEplusLacpSystemConfiguration_ObjectIdentity = ObjectIdentity
es2126PoEplusLacpSystemConfiguration = _Es2126PoEplusLacpSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 3)
)


class _Es2126PoEplusLacpSystemPriority_Type(Integer32):
    """Custom type es2126PoEplusLacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es2126PoEplusLacpSystemPriority_Type.__name__ = "Integer32"
_Es2126PoEplusLacpSystemPriority_Object = MibScalar
es2126PoEplusLacpSystemPriority = _Es2126PoEplusLacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 3, 1),
    _Es2126PoEplusLacpSystemPriority_Type()
)
es2126PoEplusLacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLacpSystemPriority.setStatus("current")


class _Es2126PoEplusLacpSystemHashMethod_Type(Integer32):
    """Custom type es2126PoEplusLacpSystemHashMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusLacpSystemHashMethod_Type.__name__ = "Integer32"
_Es2126PoEplusLacpSystemHashMethod_Object = MibScalar
es2126PoEplusLacpSystemHashMethod = _Es2126PoEplusLacpSystemHashMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 19, 3, 2),
    _Es2126PoEplusLacpSystemHashMethod_Type()
)
es2126PoEplusLacpSystemHashMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLacpSystemHashMethod.setStatus("current")
_Es2126PoEplusTrapEntry_ObjectIdentity = ObjectIdentity
es2126PoEplusTrapEntry = _Es2126PoEplusTrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20)
)
_Es2126PoEplusTrapVariable_ObjectIdentity = ObjectIdentity
es2126PoEplusTrapVariable = _Es2126PoEplusTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21, 1),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")
_LoginProtectInfo_Type = DisplayString
_LoginProtectInfo_Object = MibScalar
loginProtectInfo = _LoginProtectInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 21, 6),
    _LoginProtectInfo_Type()
)
loginProtectInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginProtectInfo.setStatus("current")
_Es2126PoEplusPoE_ObjectIdentity = ObjectIdentity
es2126PoEplusPoE = _Es2126PoEplusPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22)
)
_Es2126PoEplusPoEStatus_ObjectIdentity = ObjectIdentity
es2126PoEplusPoEStatus = _Es2126PoEplusPoEStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1)
)
_Es2126PoEplusPoEStatusVmain_Type = DisplayString
_Es2126PoEplusPoEStatusVmain_Object = MibScalar
es2126PoEplusPoEStatusVmain = _Es2126PoEplusPoEStatusVmain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 1),
    _Es2126PoEplusPoEStatusVmain_Type()
)
es2126PoEplusPoEStatusVmain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusVmain.setStatus("current")
_Es2126PoEplusPoEStatusImain_Type = DisplayString
_Es2126PoEplusPoEStatusImain_Object = MibScalar
es2126PoEplusPoEStatusImain = _Es2126PoEplusPoEStatusImain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 2),
    _Es2126PoEplusPoEStatusImain_Type()
)
es2126PoEplusPoEStatusImain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusImain.setStatus("current")
_Es2126PoEplusPoEStatusPconsume_Type = DisplayString
_Es2126PoEplusPoEStatusPconsume_Object = MibScalar
es2126PoEplusPoEStatusPconsume = _Es2126PoEplusPoEStatusPconsume_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 3),
    _Es2126PoEplusPoEStatusPconsume_Type()
)
es2126PoEplusPoEStatusPconsume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusPconsume.setStatus("current")
_Es2126PoEplusPoEStatusPowerLimit_Type = DisplayString
_Es2126PoEplusPoEStatusPowerLimit_Object = MibScalar
es2126PoEplusPoEStatusPowerLimit = _Es2126PoEplusPoEStatusPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 4),
    _Es2126PoEplusPoEStatusPowerLimit_Type()
)
es2126PoEplusPoEStatusPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusPowerLimit.setStatus("current")
_Es2126PoEplusPoEStatusTemperature_Type = DisplayString
_Es2126PoEplusPoEStatusTemperature_Object = MibScalar
es2126PoEplusPoEStatusTemperature = _Es2126PoEplusPoEStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 5),
    _Es2126PoEplusPoEStatusTemperature_Type()
)
es2126PoEplusPoEStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusTemperature.setStatus("current")
_Es2126PoEplusPoEStatusTable_Object = MibTable
es2126PoEplusPoEStatusTable = _Es2126PoEplusPoEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6)
)
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusTable.setStatus("current")
_Es2126PoEplusPoEStatusEntry_Object = MibTableRow
es2126PoEplusPoEStatusEntry = _Es2126PoEplusPoEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1)
)
es2126PoEplusPoEStatusEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPoEStatusPortNum"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusEntry.setStatus("current")


class _Es2126PoEplusPoEStatusPortNum_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Es2126PoEplusPoEStatusPortNum_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusPortNum_Object = MibTableColumn
es2126PoEplusPoEStatusPortNum = _Es2126PoEplusPoEStatusPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 1),
    _Es2126PoEplusPoEStatusPortNum_Type()
)
es2126PoEplusPoEStatusPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusPortNum.setStatus("current")


class _Es2126PoEplusPoEStatusPortOn_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusPortOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEStatusPortOn_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusPortOn_Object = MibTableColumn
es2126PoEplusPoEStatusPortOn = _Es2126PoEplusPoEStatusPortOn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 2),
    _Es2126PoEplusPoEStatusPortOn_Type()
)
es2126PoEplusPoEStatusPortOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusPortOn.setStatus("current")


class _Es2126PoEplusPoEStatusACPortOff_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusACPortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 8),
    )


_Es2126PoEplusPoEStatusACPortOff_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusACPortOff_Object = MibTableColumn
es2126PoEplusPoEStatusACPortOff = _Es2126PoEplusPoEStatusACPortOff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 3),
    _Es2126PoEplusPoEStatusACPortOff_Type()
)
es2126PoEplusPoEStatusACPortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusACPortOff.setStatus("current")


class _Es2126PoEplusPoEStatusDCPortOff_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusDCPortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEStatusDCPortOff_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusDCPortOff_Object = MibTableColumn
es2126PoEplusPoEStatusDCPortOff = _Es2126PoEplusPoEStatusDCPortOff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 4),
    _Es2126PoEplusPoEStatusDCPortOff_Type()
)
es2126PoEplusPoEStatusDCPortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusDCPortOff.setStatus("current")


class _Es2126PoEplusPoEStatusOverloadPortOff_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusOverloadPortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
    )


_Es2126PoEplusPoEStatusOverloadPortOff_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusOverloadPortOff_Object = MibTableColumn
es2126PoEplusPoEStatusOverloadPortOff = _Es2126PoEplusPoEStatusOverloadPortOff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 5),
    _Es2126PoEplusPoEStatusOverloadPortOff_Type()
)
es2126PoEplusPoEStatusOverloadPortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusOverloadPortOff.setStatus("current")


class _Es2126PoEplusPoEStatusShortCircuitPortOff_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusShortCircuitPortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEStatusShortCircuitPortOff_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusShortCircuitPortOff_Object = MibTableColumn
es2126PoEplusPoEStatusShortCircuitPortOff = _Es2126PoEplusPoEStatusShortCircuitPortOff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 6),
    _Es2126PoEplusPoEStatusShortCircuitPortOff_Type()
)
es2126PoEplusPoEStatusShortCircuitPortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusShortCircuitPortOff.setStatus("current")


class _Es2126PoEplusPoEStatusOverTemperature_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEStatusOverTemperature_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusOverTemperature_Object = MibTableColumn
es2126PoEplusPoEStatusOverTemperature = _Es2126PoEplusPoEStatusOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 7),
    _Es2126PoEplusPoEStatusOverTemperature_Type()
)
es2126PoEplusPoEStatusOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusOverTemperature.setStatus("current")


class _Es2126PoEplusPoEStatusPowerManagePortOff_Type(Integer32):
    """Custom type es2126PoEplusPoEStatusPowerManagePortOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEStatusPowerManagePortOff_Type.__name__ = "Integer32"
_Es2126PoEplusPoEStatusPowerManagePortOff_Object = MibTableColumn
es2126PoEplusPoEStatusPowerManagePortOff = _Es2126PoEplusPoEStatusPowerManagePortOff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 1, 6, 1, 8),
    _Es2126PoEplusPoEStatusPowerManagePortOff_Type()
)
es2126PoEplusPoEStatusPowerManagePortOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEStatusPowerManagePortOff.setStatus("current")
_Es2126PoEplusPoEConfTable_Object = MibTable
es2126PoEplusPoEConfTable = _Es2126PoEplusPoEConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2)
)
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfTable.setStatus("current")
_Es2126PoEplusPoEConfEntry_Object = MibTableRow
es2126PoEplusPoEConfEntry = _Es2126PoEplusPoEConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1)
)
es2126PoEplusPoEConfEntry.setIndexNames(
    (0, "LANCOM-ES-2126PPLUS-MIB", "es2126PoEplusPoEConfPortNum"),
)
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfEntry.setStatus("current")


class _Es2126PoEplusPoEConfPortNum_Type(Integer32):
    """Custom type es2126PoEplusPoEConfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Es2126PoEplusPoEConfPortNum_Type.__name__ = "Integer32"
_Es2126PoEplusPoEConfPortNum_Object = MibTableColumn
es2126PoEplusPoEConfPortNum = _Es2126PoEplusPoEConfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 1),
    _Es2126PoEplusPoEConfPortNum_Type()
)
es2126PoEplusPoEConfPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfPortNum.setStatus("current")


class _Es2126PoEplusPoEConfStatus_Type(Integer32):
    """Custom type es2126PoEplusPoEConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEConfStatus_Type.__name__ = "Integer32"
_Es2126PoEplusPoEConfStatus_Object = MibTableColumn
es2126PoEplusPoEConfStatus = _Es2126PoEplusPoEConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 2),
    _Es2126PoEplusPoEConfStatus_Type()
)
es2126PoEplusPoEConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfStatus.setStatus("current")


class _Es2126PoEplusPoEConfState_Type(Integer32):
    """Custom type es2126PoEplusPoEConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Es2126PoEplusPoEConfState_Type.__name__ = "Integer32"
_Es2126PoEplusPoEConfState_Object = MibTableColumn
es2126PoEplusPoEConfState = _Es2126PoEplusPoEConfState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 3),
    _Es2126PoEplusPoEConfState_Type()
)
es2126PoEplusPoEConfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfState.setStatus("current")


class _Es2126PoEplusPoEConfPriority_Type(Integer32):
    """Custom type es2126PoEplusPoEConfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Es2126PoEplusPoEConfPriority_Type.__name__ = "Integer32"
_Es2126PoEplusPoEConfPriority_Object = MibTableColumn
es2126PoEplusPoEConfPriority = _Es2126PoEplusPoEConfPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 4),
    _Es2126PoEplusPoEConfPriority_Type()
)
es2126PoEplusPoEConfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfPriority.setStatus("current")
_Es2126PoEplusPoEConfPower_Type = DisplayString
_Es2126PoEplusPoEConfPower_Object = MibTableColumn
es2126PoEplusPoEConfPower = _Es2126PoEplusPoEConfPower_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 5),
    _Es2126PoEplusPoEConfPower_Type()
)
es2126PoEplusPoEConfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfPower.setStatus("current")


class _Es2126PoEplusPoEConfCurrent_Type(Integer32):
    """Custom type es2126PoEplusPoEConfCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Es2126PoEplusPoEConfCurrent_Type.__name__ = "Integer32"
_Es2126PoEplusPoEConfCurrent_Object = MibTableColumn
es2126PoEplusPoEConfCurrent = _Es2126PoEplusPoEConfCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 6),
    _Es2126PoEplusPoEConfCurrent_Type()
)
es2126PoEplusPoEConfCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfCurrent.setStatus("current")


class _Es2126PoEplusPoEConfClass_Type(Integer32):
    """Custom type es2126PoEplusPoEConfClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Es2126PoEplusPoEConfClass_Type.__name__ = "Integer32"
_Es2126PoEplusPoEConfClass_Object = MibTableColumn
es2126PoEplusPoEConfClass = _Es2126PoEplusPoEConfClass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 22, 2, 1, 7),
    _Es2126PoEplusPoEConfClass_Type()
)
es2126PoEplusPoEConfClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es2126PoEplusPoEConfClass.setStatus("current")
_Es2126PoEplusLoginProtect_ObjectIdentity = ObjectIdentity
es2126PoEplusLoginProtect = _Es2126PoEplusLoginProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 23)
)


class _Es2126PoEplusLockMinutes_Type(Integer32):
    """Custom type es2126PoEplusLockMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2126PoEplusLockMinutes_Type.__name__ = "Integer32"
_Es2126PoEplusLockMinutes_Object = MibScalar
es2126PoEplusLockMinutes = _Es2126PoEplusLockMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 23, 1),
    _Es2126PoEplusLockMinutes_Type()
)
es2126PoEplusLockMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLockMinutes.setStatus("current")


class _Es2126PoEplusLoginErrors_Type(Integer32):
    """Custom type es2126PoEplusLoginErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Es2126PoEplusLoginErrors_Type.__name__ = "Integer32"
_Es2126PoEplusLoginErrors_Object = MibScalar
es2126PoEplusLoginErrors = _Es2126PoEplusLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 23, 2),
    _Es2126PoEplusLoginErrors_Type()
)
es2126PoEplusLoginErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es2126PoEplusLoginErrors.setStatus("current")

# Managed Objects groups


# Notification objects

es2126PoEplusModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 1)
)
es2126PoEplusModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126PoEplusModuleInserted.setStatus(
        "current"
    )

es2126PoEplusModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 2)
)
es2126PoEplusModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126PoEplusModuleRemoved.setStatus(
        "current"
    )

es2126PoEplusDualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 3)
)
es2126PoEplusDualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126PoEplusDualMediaSwapped.setStatus(
        "current"
    )

es2126PoEplusPoEFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 4)
)
if mibBuilder.loadTexts:
    es2126PoEplusPoEFailure.setStatus(
        "current"
    )

es2126PoEplusLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 5)
)
es2126PoEplusLoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126PoEplusLoopDetected.setStatus(
        "current"
    )

es2126PoEplusLoginProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 6)
)
es2126PoEplusLoginProtected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126PoEplusLoginProtected.setStatus(
        "current"
    )

es2126PoEplusStpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 100)
)
if mibBuilder.loadTexts:
    es2126PoEplusStpStateDisabled.setStatus(
        "current"
    )

es2126PoEplusStpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 101)
)
if mibBuilder.loadTexts:
    es2126PoEplusStpStateEnabled.setStatus(
        "current"
    )

es2126PoEplusStpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 102)
)
es2126PoEplusStpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    es2126PoEplusStpTopologyChanged.setStatus(
        "current"
    )

es2126PoEplusRmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 110)
)
if mibBuilder.loadTexts:
    es2126PoEplusRmonRisingAlarm.setStatus(
        "current"
    )

es2126PoEplusRmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 111)
)
if mibBuilder.loadTexts:
    es2126PoEplusRmonFallingAlarm.setStatus(
        "current"
    )

es2126PoEplusLacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 120)
)
es2126PoEplusLacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PPLUS-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2126PoEplusLacpStateDisabled.setStatus(
        "current"
    )

es2126PoEplusLacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 121)
)
es2126PoEplusLacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PPLUS-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    es2126PoEplusLacpStateEnabled.setStatus(
        "current"
    )

es2126PoEplusLacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 123)
)
es2126PoEplusLacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PPLUS-MIB", "actorkey"),
        ("LANCOM-ES-2126PPLUS-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2126PoEplusLacpPortAdded.setStatus(
        "current"
    )

es2126PoEplusLacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 124)
)
es2126PoEplusLacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("LANCOM-ES-2126PPLUS-MIB", "actorkey"),
        ("LANCOM-ES-2126PPLUS-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    es2126PoEplusLacpPortTrunkFailure.setStatus(
        "current"
    )

es2126PoEplusGvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 140)
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpStateDisabled.setStatus(
        "current"
    )

es2126PoEplusGvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 141)
)
if mibBuilder.loadTexts:
    es2126PoEplusGvrpStateEnabled.setStatus(
        "current"
    )

es2126PoEplusVlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 151)
)
if mibBuilder.loadTexts:
    es2126PoEplusVlanPortBaseEnabled.setStatus(
        "current"
    )

es2126PoEplusVlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 152)
)
if mibBuilder.loadTexts:
    es2126PoEplusVlanTagBaseEnabled.setStatus(
        "current"
    )

es2126PoEplusVlanMetroBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 153)
)
if mibBuilder.loadTexts:
    es2126PoEplusVlanMetroBaseEnabled.setStatus(
        "current"
    )

es2126PoEplusUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 200)
)
es2126PoEplusUserLogin.setObjects(
    ("LANCOM-ES-2126PPLUS-MIB", "username")
)
if mibBuilder.loadTexts:
    es2126PoEplusUserLogin.setStatus(
        "current"
    )

es2126PoEplusUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 800, 2, 2129, 1, 20, 201)
)
es2126PoEplusUserLogout.setObjects(
    ("LANCOM-ES-2126PPLUS-MIB", "username")
)
if mibBuilder.loadTexts:
    es2126PoEplusUserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-ES-2126PPLUS-MIB",
    **{"lancomSystems": lancomSystems,
       "switchingSystems": switchingSystems,
       "fastEthernetSwitches": fastEthernetSwitches,
       "lancomES2126P": lancomES2126P,
       "es2126PoEplusProduces": es2126PoEplusProduces,
       "es2126PoEplusSystem": es2126PoEplusSystem,
       "es2126PoEplusCommonSys": es2126PoEplusCommonSys,
       "es2126PoEplusReboot": es2126PoEplusReboot,
       "es2126PoEplusBiosVsersion": es2126PoEplusBiosVsersion,
       "es2126PoEplusFirmwareVersion": es2126PoEplusFirmwareVersion,
       "es2126PoEplusHardwareVersion": es2126PoEplusHardwareVersion,
       "es2126PoEplusMechanicalVersion": es2126PoEplusMechanicalVersion,
       "es2126PoEplusSerialNumber": es2126PoEplusSerialNumber,
       "es2126PoEplusHostMacAddress": es2126PoEplusHostMacAddress,
       "es2126PoEplusDevicePort": es2126PoEplusDevicePort,
       "es2126PoEplusRamSize": es2126PoEplusRamSize,
       "es2126PoEplusFlashSize": es2126PoEplusFlashSize,
       "es2126PoEplusSystemDescription": es2126PoEplusSystemDescription,
       "es2126PoEplusDeviceName": es2126PoEplusDeviceName,
       "es2126PoEplusIP": es2126PoEplusIP,
       "es2126PoEplusDhcpSetting": es2126PoEplusDhcpSetting,
       "es2126PoEplusIPAddress": es2126PoEplusIPAddress,
       "es2126PoEplusNetMask": es2126PoEplusNetMask,
       "es2126PoEplusDefaultGateway": es2126PoEplusDefaultGateway,
       "es2126PoEplusDnsSetting": es2126PoEplusDnsSetting,
       "es2126PoEplusDnsServer": es2126PoEplusDnsServer,
       "es2126PoEplusTime": es2126PoEplusTime,
       "es2126PoEplusSystemCurrentTime": es2126PoEplusSystemCurrentTime,
       "es2126PoEplusManualTimeSetting": es2126PoEplusManualTimeSetting,
       "es2126PoEplusNTPServer": es2126PoEplusNTPServer,
       "es2126PoEplusNTPTimeZone": es2126PoEplusNTPTimeZone,
       "es2126PoEplusNTPTimeSync": es2126PoEplusNTPTimeSync,
       "es2126PoEplusDaylightSavingTime": es2126PoEplusDaylightSavingTime,
       "es2126PoEplusDaylightStartTime": es2126PoEplusDaylightStartTime,
       "es2126PoEplusDaylightEndTime": es2126PoEplusDaylightEndTime,
       "es2126PoEplusAccount": es2126PoEplusAccount,
       "es2126PoEplusAccountNumber": es2126PoEplusAccountNumber,
       "es2126PoEplusAccountTable": es2126PoEplusAccountTable,
       "es2126PoEplusAccountEntry": es2126PoEplusAccountEntry,
       "es2126PoEplusAccountIndex": es2126PoEplusAccountIndex,
       "es2126PoEplusAccountAuthorization": es2126PoEplusAccountAuthorization,
       "es2126PoEplusAccountName": es2126PoEplusAccountName,
       "es2126PoEplusAccountPassword": es2126PoEplusAccountPassword,
       "es2126PoEplusAccountAddName": es2126PoEplusAccountAddName,
       "es2126PoEplusAccountAddPassword": es2126PoEplusAccountAddPassword,
       "es2126PoEplusDoAccountAdd": es2126PoEplusDoAccountAdd,
       "es2126PoEplusAccountDel": es2126PoEplusAccountDel,
       "es2126PoEplusSnmp": es2126PoEplusSnmp,
       "es2126PoEplusGetCommunity": es2126PoEplusGetCommunity,
       "es2126PoEplusSetCommunity": es2126PoEplusSetCommunity,
       "es2126PoEplusTrapHostNumber": es2126PoEplusTrapHostNumber,
       "es2126PoEplusTrapHostTable": es2126PoEplusTrapHostTable,
       "es2126PoEplusTrapHostEntry": es2126PoEplusTrapHostEntry,
       "es2126PoEplusTrapHostIndex": es2126PoEplusTrapHostIndex,
       "es2126PoEplusTrapHostIP": es2126PoEplusTrapHostIP,
       "es2126PoEplusTrapHostPort": es2126PoEplusTrapHostPort,
       "es2126PoEplusTrapHostCommunity": es2126PoEplusTrapHostCommunity,
       "es2126PoEplusRegisterMonitor": es2126PoEplusRegisterMonitor,
       "es2126PoEplusDeleteMonitor": es2126PoEplusDeleteMonitor,
       "es2126PoEplusMonitorTable": es2126PoEplusMonitorTable,
       "es2126PoEplusMonitorEntry": es2126PoEplusMonitorEntry,
       "es2126PoEplusMonitorTableIp": es2126PoEplusMonitorTableIp,
       "es2126PoEplusMonitorTableMac": es2126PoEplusMonitorTableMac,
       "es2126PoEplusTrapBootDelayTime": es2126PoEplusTrapBootDelayTime,
       "es2126PoEplusAlarm": es2126PoEplusAlarm,
       "es2126PoEplusEvent": es2126PoEplusEvent,
       "es2126PoEplusEventNumber": es2126PoEplusEventNumber,
       "es2126PoEplusEventTable": es2126PoEplusEventTable,
       "es2126PoEplusEventEntry": es2126PoEplusEventEntry,
       "es2126PoEplusEventIndex": es2126PoEplusEventIndex,
       "es2126PoEplusEventName": es2126PoEplusEventName,
       "es2126PoEplusEventSendEmail": es2126PoEplusEventSendEmail,
       "es2126PoEplusEventSendTrap": es2126PoEplusEventSendTrap,
       "es2126PoEplusEmail": es2126PoEplusEmail,
       "es2126PoEplusEmailServer": es2126PoEplusEmailServer,
       "es2126PoEplusEmailUsername": es2126PoEplusEmailUsername,
       "es2126PoEplusEmailPassword": es2126PoEplusEmailPassword,
       "es2126PoEplusEmailSender": es2126PoEplusEmailSender,
       "es2126PoEplusEmailReturnPath": es2126PoEplusEmailReturnPath,
       "es2126PoEplusEmailUserNumber": es2126PoEplusEmailUserNumber,
       "es2126PoEplusEmailUserTable": es2126PoEplusEmailUserTable,
       "es2126PoEplusEmailUserEntry": es2126PoEplusEmailUserEntry,
       "es2126PoEplusEmailUserIndex": es2126PoEplusEmailUserIndex,
       "es2126PoEplusEmailUserAddress": es2126PoEplusEmailUserAddress,
       "es2126PoEplusTftp": es2126PoEplusTftp,
       "es2126PoEplusRemoteTftpServer": es2126PoEplusRemoteTftpServer,
       "es2126PoEplusInternalTftpServerState": es2126PoEplusInternalTftpServerState,
       "es2126PoEplusConfiguration": es2126PoEplusConfiguration,
       "es2126PoEplusSaveRestore": es2126PoEplusSaveRestore,
       "es2126PoEplusSaveStart": es2126PoEplusSaveStart,
       "es2126PoEplusSaveUser": es2126PoEplusSaveUser,
       "es2126PoEplusRestoreDefault": es2126PoEplusRestoreDefault,
       "es2126PoEplusRestoreUser": es2126PoEplusRestoreUser,
       "es2126PoEplusConfigFile": es2126PoEplusConfigFile,
       "es2126PoEplusExportConfigName": es2126PoEplusExportConfigName,
       "es2126PoEplusDoExportConfig": es2126PoEplusDoExportConfig,
       "es2126PoEplusImportConfigName": es2126PoEplusImportConfigName,
       "es2126PoEplusDoImportConfig": es2126PoEplusDoImportConfig,
       "es2126PoEplusDiagnostic": es2126PoEplusDiagnostic,
       "es2126PoEplusEEPROMTest": es2126PoEplusEEPROMTest,
       "es2126PoEplusUartTest": es2126PoEplusUartTest,
       "es2126PoEplusDramTest": es2126PoEplusDramTest,
       "es2126PoEplusFlashTest": es2126PoEplusFlashTest,
       "es2126PoEplusInternalLoopbackTest": es2126PoEplusInternalLoopbackTest,
       "es2126PoEplusExternalLoopbackTest": es2126PoEplusExternalLoopbackTest,
       "es2126PoEplusPingTest": es2126PoEplusPingTest,
       "es2126PoEplusLog": es2126PoEplusLog,
       "es2126PoEplusClearLog": es2126PoEplusClearLog,
       "es2126PoEplusUploadLog": es2126PoEplusUploadLog,
       "es2126PoEplusAutoUploadLogState": es2126PoEplusAutoUploadLogState,
       "es2126PoEplusLogNumber": es2126PoEplusLogNumber,
       "es2126PoEplusLogTable": es2126PoEplusLogTable,
       "es2126PoEplusLogEntry": es2126PoEplusLogEntry,
       "es2126PoEplusLogIndex": es2126PoEplusLogIndex,
       "es2126PoEplusLogEvent": es2126PoEplusLogEvent,
       "es2126PoEplusFirmware": es2126PoEplusFirmware,
       "es2126PoEplusFirmwareFileName": es2126PoEplusFirmwareFileName,
       "es2126PoEplusDoFirmwareUpgrade": es2126PoEplusDoFirmwareUpgrade,
       "es2126PoEplusPort": es2126PoEplusPort,
       "es2126PoEplusPortStatus": es2126PoEplusPortStatus,
       "es2126PoEplusPortStatusNumber": es2126PoEplusPortStatusNumber,
       "es2126PoEplusPortStatusTable": es2126PoEplusPortStatusTable,
       "es2126PoEplusPortStatusEntry": es2126PoEplusPortStatusEntry,
       "es2126PoEplusPortStatusIndex": es2126PoEplusPortStatusIndex,
       "es2126PoEplusPortStatusMedia": es2126PoEplusPortStatusMedia,
       "es2126PoEplusPortStatusLink": es2126PoEplusPortStatusLink,
       "es2126PoEplusPortStatusPortState": es2126PoEplusPortStatusPortState,
       "es2126PoEplusPortStatusAutoNego": es2126PoEplusPortStatusAutoNego,
       "es2126PoEplusPortStatusSpdDpx": es2126PoEplusPortStatusSpdDpx,
       "es2126PoEplusPortStatusRxPause": es2126PoEplusPortStatusRxPause,
       "es2126PoEplusPortStatusTxPause": es2126PoEplusPortStatusTxPause,
       "es2126PoEplusPortStatusDescription": es2126PoEplusPortStatusDescription,
       "es2126PoEplusPortConf": es2126PoEplusPortConf,
       "es2126PoEplusPortConfNumber": es2126PoEplusPortConfNumber,
       "es2126PoEplusPortConfTable": es2126PoEplusPortConfTable,
       "es2126PoEplusPortConfEntry": es2126PoEplusPortConfEntry,
       "es2126PoEplusPortConfIndex": es2126PoEplusPortConfIndex,
       "es2126PoEplusPortConfPortState": es2126PoEplusPortConfPortState,
       "es2126PoEplusPortConfSpdDpx": es2126PoEplusPortConfSpdDpx,
       "es2126PoEplusPortConfFlwCtrl": es2126PoEplusPortConfFlwCtrl,
       "es2126PoEplusPortConfDescription": es2126PoEplusPortConfDescription,
       "es2126PoEplusPortBandwidth": es2126PoEplusPortBandwidth,
       "es2126PoEplusPortBandwidthTable": es2126PoEplusPortBandwidthTable,
       "es2126PoEplusPortBandwidthEntry": es2126PoEplusPortBandwidthEntry,
       "es2126PoEplusPortBandwidthIndex": es2126PoEplusPortBandwidthIndex,
       "es2126PoEplusPortBandwidthIngressRate": es2126PoEplusPortBandwidthIngressRate,
       "es2126PoEplusPortBandwidthEgressRate": es2126PoEplusPortBandwidthEgressRate,
       "es2126PoEplusPortBandwidthStormType": es2126PoEplusPortBandwidthStormType,
       "es2126PoEplusPortBandwidthStormRate": es2126PoEplusPortBandwidthStormRate,
       "es2126PoEplusPortSFPInfo": es2126PoEplusPortSFPInfo,
       "es2126PoEplusPortSFPInfoNumber": es2126PoEplusPortSFPInfoNumber,
       "es2126PoEplusPortSFPInfoTable": es2126PoEplusPortSFPInfoTable,
       "es2126PoEplusPortSFPInfoEntry": es2126PoEplusPortSFPInfoEntry,
       "es2126PoEplusPortSFPInfoIndex": es2126PoEplusPortSFPInfoIndex,
       "es2126PoEplusPortSFPConnectorType": es2126PoEplusPortSFPConnectorType,
       "es2126PoEplusPortSFPFiberType": es2126PoEplusPortSFPFiberType,
       "es2126PoEplusPortSFPWavelength": es2126PoEplusPortSFPWavelength,
       "es2126PoEplusPortSFPBaudRate": es2126PoEplusPortSFPBaudRate,
       "es2126PoEplusPortSFPVendorOUI": es2126PoEplusPortSFPVendorOUI,
       "es2126PoEplusPortSFPVendorName": es2126PoEplusPortSFPVendorName,
       "es2126PoEplusPortSFPVendorPN": es2126PoEplusPortSFPVendorPN,
       "es2126PoEplusPortSFPVendorRev": es2126PoEplusPortSFPVendorRev,
       "es2126PoEplusPortSFPVendorSN": es2126PoEplusPortSFPVendorSN,
       "es2126PoEplusPortSFPDateCode": es2126PoEplusPortSFPDateCode,
       "es2126PoEplusPortSFPTemperature": es2126PoEplusPortSFPTemperature,
       "es2126PoEplusPortSFPVcc": es2126PoEplusPortSFPVcc,
       "es2126PoEplusPortSFPTxBias": es2126PoEplusPortSFPTxBias,
       "es2126PoEplusPortSFPTxPWR": es2126PoEplusPortSFPTxPWR,
       "es2126PoEplusPortSFPRxPWR": es2126PoEplusPortSFPRxPWR,
       "es2126PoEplusLoopDetectedConf": es2126PoEplusLoopDetectedConf,
       "es2126PoEplusLoopDetectedNumber": es2126PoEplusLoopDetectedNumber,
       "es2126PoEplusLoopDetectedTable": es2126PoEplusLoopDetectedTable,
       "es2126PoEplusLoopDetectedEntry": es2126PoEplusLoopDetectedEntry,
       "es2126PoEplusLoopDetectedfIndex": es2126PoEplusLoopDetectedfIndex,
       "es2126PoEplusLoopDetectedStateEbl": es2126PoEplusLoopDetectedStateEbl,
       "es2126PoEplusLoopDetectedCurrentStatus": es2126PoEplusLoopDetectedCurrentStatus,
       "es2126PoEplusLoopDetectedResumed": es2126PoEplusLoopDetectedResumed,
       "es2126PoEplusLoopDetectedAction": es2126PoEplusLoopDetectedAction,
       "es2126PoEplusMacTableInfo": es2126PoEplusMacTableInfo,
       "es2126PoEplusMacTableMaintenance": es2126PoEplusMacTableMaintenance,
       "es2126PoEplusMacTableAgingTime": es2126PoEplusMacTableAgingTime,
       "es2126PoEplusMacTableFlush": es2126PoEplusMacTableFlush,
       "es2126PoEplusMacTableLearnPortLimitTable": es2126PoEplusMacTableLearnPortLimitTable,
       "es2126PoEplusMacTableLearnPortLimitEntry": es2126PoEplusMacTableLearnPortLimitEntry,
       "es2126PoEplusMacTableLearnPortLimitIndex": es2126PoEplusMacTableLearnPortLimitIndex,
       "es2126PoEplusMacTableLearnPortLimit": es2126PoEplusMacTableLearnPortLimit,
       "es2126PoEplusMacTableStaticMac": es2126PoEplusMacTableStaticMac,
       "es2126PoEplusMacTableStaticMacNumber": es2126PoEplusMacTableStaticMacNumber,
       "es2126PoEplusMacTableStaticMacEntryCreate": es2126PoEplusMacTableStaticMacEntryCreate,
       "es2126PoEplusMacTableStaticMacTable": es2126PoEplusMacTableStaticMacTable,
       "es2126PoEplusMacTableStaticMacEntry": es2126PoEplusMacTableStaticMacEntry,
       "es2126PoEplusMacTableStaticMacIndex": es2126PoEplusMacTableStaticMacIndex,
       "es2126PoEplusMacTableStaticMacAddress": es2126PoEplusMacTableStaticMacAddress,
       "es2126PoEplusMacTableStaticMacVid": es2126PoEplusMacTableStaticMacVid,
       "es2126PoEplusMacTableStaticMacQueue": es2126PoEplusMacTableStaticMacQueue,
       "es2126PoEplusMacTableStaticMacFwRule": es2126PoEplusMacTableStaticMacFwRule,
       "es2126PoEplusMacTableStaticMacPort": es2126PoEplusMacTableStaticMacPort,
       "es2126PoEplusMacTableStaticMacEntryAction": es2126PoEplusMacTableStaticMacEntryAction,
       "es2126PoEplusMacTableMacAlias": es2126PoEplusMacTableMacAlias,
       "es2126PoEplusMacTableMacAliasNumber": es2126PoEplusMacTableMacAliasNumber,
       "es2126PoEplusMacTableMacAliasEntryCreate": es2126PoEplusMacTableMacAliasEntryCreate,
       "es2126PoEplusMacTableMacAliasTable": es2126PoEplusMacTableMacAliasTable,
       "es2126PoEplusMacTableMacAliasEntry": es2126PoEplusMacTableMacAliasEntry,
       "es2126PoEplusMacTableMacAliasIndex": es2126PoEplusMacTableMacAliasIndex,
       "es2126PoEplusMacTableMacAliasAddress": es2126PoEplusMacTableMacAliasAddress,
       "es2126PoEplusMacTableMacAliasAlias": es2126PoEplusMacTableMacAliasAlias,
       "es2126PoEplusMacTableMacAliasEntryAction": es2126PoEplusMacTableMacAliasEntryAction,
       "es2126PoEplusGVRPInfo": es2126PoEplusGVRPInfo,
       "es2126PoEplusGvrpConf": es2126PoEplusGvrpConf,
       "es2126PoEplusGvrpConfState": es2126PoEplusGvrpConfState,
       "es2126PoEplusGvrpConfTable": es2126PoEplusGvrpConfTable,
       "es2126PoEplusGvrpConfEntry": es2126PoEplusGvrpConfEntry,
       "es2126PoEplusGvrpConfIndex": es2126PoEplusGvrpConfIndex,
       "es2126PoEplusGvrpConfJoinTime": es2126PoEplusGvrpConfJoinTime,
       "es2126PoEplusGvrpConfLeaveTime": es2126PoEplusGvrpConfLeaveTime,
       "es2126PoEplusGvrpConfLeaveAllTime": es2126PoEplusGvrpConfLeaveAllTime,
       "es2126PoEplusGvrpConfDefaultAppMode": es2126PoEplusGvrpConfDefaultAppMode,
       "es2126PoEplusGvrpConfDefaultRegMode": es2126PoEplusGvrpConfDefaultRegMode,
       "es2126PoEplusGvrpConfRestrictedMode": es2126PoEplusGvrpConfRestrictedMode,
       "es2126PoEplusGvrpCounter": es2126PoEplusGvrpCounter,
       "es2126PoEplusGvrpCounterTable": es2126PoEplusGvrpCounterTable,
       "es2126PoEplusGvrpCounterEntry": es2126PoEplusGvrpCounterEntry,
       "es2126PoEplusGvrpCounterIndex": es2126PoEplusGvrpCounterIndex,
       "es2126PoEplusGvrpCounterRxTotalGvrpPkts": es2126PoEplusGvrpCounterRxTotalGvrpPkts,
       "es2126PoEplusGvrpCounterRxInvalidGvrpPkts": es2126PoEplusGvrpCounterRxInvalidGvrpPkts,
       "es2126PoEplusGvrpCounterRxLeaveAllMsg": es2126PoEplusGvrpCounterRxLeaveAllMsg,
       "es2126PoEplusGvrpCounterRxJoinEmptyMsg": es2126PoEplusGvrpCounterRxJoinEmptyMsg,
       "es2126PoEplusGvrpCounterRxJoinInMsg": es2126PoEplusGvrpCounterRxJoinInMsg,
       "es2126PoEplusGvrpCounterRxLeaveEmptyMsg": es2126PoEplusGvrpCounterRxLeaveEmptyMsg,
       "es2126PoEplusGvrpCounterRxEmptyMsg": es2126PoEplusGvrpCounterRxEmptyMsg,
       "es2126PoEplusGvrpCounterTxTotalGvrpPkts": es2126PoEplusGvrpCounterTxTotalGvrpPkts,
       "es2126PoEplusGvrpCounterTxLeaveAllMsg": es2126PoEplusGvrpCounterTxLeaveAllMsg,
       "es2126PoEplusGvrpCounterTxJoinEmptyMsg": es2126PoEplusGvrpCounterTxJoinEmptyMsg,
       "es2126PoEplusGvrpCounterTxJoinInMsg": es2126PoEplusGvrpCounterTxJoinInMsg,
       "es2126PoEplusGvrpCounterTxLeaveEmptyMsg": es2126PoEplusGvrpCounterTxLeaveEmptyMsg,
       "es2126PoEplusGvrpCounterTxEmptyMsg": es2126PoEplusGvrpCounterTxEmptyMsg,
       "es2126PoEplusGvrpGroup": es2126PoEplusGvrpGroup,
       "es2126PoEplusGvrpGroupNumber": es2126PoEplusGvrpGroupNumber,
       "es2126PoEplusGvrpGroupTable": es2126PoEplusGvrpGroupTable,
       "es2126PoEplusGvrpGroupEntry": es2126PoEplusGvrpGroupEntry,
       "es2126PoEplusGvrpGroupId": es2126PoEplusGvrpGroupId,
       "es2126PoEplusGvrpGroupVid": es2126PoEplusGvrpGroupVid,
       "es2126PoEplusGvrpGroupMemberPort": es2126PoEplusGvrpGroupMemberPort,
       "es2126PoEplusSecurity": es2126PoEplusSecurity,
       "es2126PoEplusIsolatedPortGroup": es2126PoEplusIsolatedPortGroup,
       "es2126PoEplusMirror": es2126PoEplusMirror,
       "es2126PoEplusMirrorMode": es2126PoEplusMirrorMode,
       "es2126PoEplusMonitoringPort": es2126PoEplusMonitoringPort,
       "es2126PoEplusMonitoredIngressPort": es2126PoEplusMonitoredIngressPort,
       "es2126PoEplusMonitoredEgressPort": es2126PoEplusMonitoredEgressPort,
       "es2126PoEplusRestrictedGroup": es2126PoEplusRestrictedGroup,
       "es2126PoEplusRestrictedGroupIngress": es2126PoEplusRestrictedGroupIngress,
       "es2126PoEplusRestrictedGroupEgress": es2126PoEplusRestrictedGroupEgress,
       "es2126PoEplusVirtualStack": es2126PoEplusVirtualStack,
       "es2126PoEplusVirtualStackState": es2126PoEplusVirtualStackState,
       "es2126PoEplusVirtualStackRole": es2126PoEplusVirtualStackRole,
       "es2126PoEplusVirtualStackGroupID": es2126PoEplusVirtualStackGroupID,
       "es2126PoEplusManagementSecurity": es2126PoEplusManagementSecurity,
       "es2126PoEplusManagementSecurityNumber": es2126PoEplusManagementSecurityNumber,
       "es2126PoEplusManagementSecurityEntryCreate": es2126PoEplusManagementSecurityEntryCreate,
       "es2126PoEplusManagementSecurityTable": es2126PoEplusManagementSecurityTable,
       "es2126PoEplusManagementSecurityEntry": es2126PoEplusManagementSecurityEntry,
       "es2126PoEplusManagementSecurityIndex": es2126PoEplusManagementSecurityIndex,
       "es2126PoEplusManagementSecurityName": es2126PoEplusManagementSecurityName,
       "es2126PoEplusManagementSecurityVid": es2126PoEplusManagementSecurityVid,
       "es2126PoEplusManagementSecurityIpRange": es2126PoEplusManagementSecurityIpRange,
       "es2126PoEplusManagementSecurityIncomigPort": es2126PoEplusManagementSecurityIncomigPort,
       "es2126PoEplusManagementSecurityAccessType": es2126PoEplusManagementSecurityAccessType,
       "es2126PoEplusManagementSecurityAction": es2126PoEplusManagementSecurityAction,
       "es2126PoEplusManagementSecurityEntryAction": es2126PoEplusManagementSecurityEntryAction,
       "es2126PoEplusQoS": es2126PoEplusQoS,
       "es2126PoEplusQoSGlobalConfig": es2126PoEplusQoSGlobalConfig,
       "es2126PoEplusQoSMode": es2126PoEplusQoSMode,
       "es2126PoEplusQosPriorityControl1p": es2126PoEplusQosPriorityControl1p,
       "es2126PoEplusQosPriorityControlTOS": es2126PoEplusQosPriorityControlTOS,
       "es2126PoEplusQosPriorityControlDSCP": es2126PoEplusQosPriorityControlDSCP,
       "es2126PoEplusQoSSchedulingMethod": es2126PoEplusQoSSchedulingMethod,
       "es2126PoEplusQoSWeightQ0": es2126PoEplusQoSWeightQ0,
       "es2126PoEplusQoSWeightQ1": es2126PoEplusQoSWeightQ1,
       "es2126PoEplusQoSWeightQ2": es2126PoEplusQoSWeightQ2,
       "es2126PoEplusQoSWeightQ3": es2126PoEplusQoSWeightQ3,
       "es2126PoEplusQoSVIPPort": es2126PoEplusQoSVIPPort,
       "es2126PoEplusQoS1pPriority": es2126PoEplusQoS1pPriority,
       "es2126PoEplusQoS1pPriorityTable": es2126PoEplusQoS1pPriorityTable,
       "es2126PoEplusQoS1pPriorityEntry": es2126PoEplusQoS1pPriorityEntry,
       "es2126PoEplusQoS1pPriorityIndex": es2126PoEplusQoS1pPriorityIndex,
       "es2126PoEplusQoS1pPriorityValue": es2126PoEplusQoS1pPriorityValue,
       "es2126PoEplusQoS1pPriorityQueue": es2126PoEplusQoS1pPriorityQueue,
       "es2126PoEplusQoSDTypeTOSPriority": es2126PoEplusQoSDTypeTOSPriority,
       "es2126PoEplusQoSDTypeTOSPriorityTable": es2126PoEplusQoSDTypeTOSPriorityTable,
       "es2126PoEplusQoSDTypeTOSPriorityEntry": es2126PoEplusQoSDTypeTOSPriorityEntry,
       "es2126PoEplusQoSDTypeTOSPriorityIndex": es2126PoEplusQoSDTypeTOSPriorityIndex,
       "es2126PoEplusQoSDTypeTOSPriorityValue": es2126PoEplusQoSDTypeTOSPriorityValue,
       "es2126PoEplusQoSDTypeTOSPriorityQueue": es2126PoEplusQoSDTypeTOSPriorityQueue,
       "es2126PoEplusQoSTTypeTOSPriority": es2126PoEplusQoSTTypeTOSPriority,
       "es2126PoEplusQoSTTypeTOSPriorityTable": es2126PoEplusQoSTTypeTOSPriorityTable,
       "es2126PoEplusQoSTTypeTOSPriorityEntry": es2126PoEplusQoSTTypeTOSPriorityEntry,
       "es2126PoEplusQoSTTypeTOSPriorityIndex": es2126PoEplusQoSTTypeTOSPriorityIndex,
       "es2126PoEplusQoSTTypeTOSPriorityValue": es2126PoEplusQoSTTypeTOSPriorityValue,
       "es2126PoEplusQoSTTypeTOSPriorityQueue": es2126PoEplusQoSTTypeTOSPriorityQueue,
       "es2126PoEplusQoSRTypeTOSPriority": es2126PoEplusQoSRTypeTOSPriority,
       "es2126PoEplusQoSRTypeTOSPriorityTable": es2126PoEplusQoSRTypeTOSPriorityTable,
       "es2126PoEplusQoSRTypeTOSPriorityEntry": es2126PoEplusQoSRTypeTOSPriorityEntry,
       "es2126PoEplusQoSRTypeTOSPriorityIndex": es2126PoEplusQoSRTypeTOSPriorityIndex,
       "es2126PoEplusQoSRTypeTOSPriorityValue": es2126PoEplusQoSRTypeTOSPriorityValue,
       "es2126PoEplusQoSRTypeTOSPriorityQueue": es2126PoEplusQoSRTypeTOSPriorityQueue,
       "es2126PoEplusQoSMTypeTOSPriority": es2126PoEplusQoSMTypeTOSPriority,
       "es2126PoEplusQoSMTypeTOSPriorityTable": es2126PoEplusQoSMTypeTOSPriorityTable,
       "es2126PoEplusQoSMTypeTOSPriorityEntry": es2126PoEplusQoSMTypeTOSPriorityEntry,
       "es2126PoEplusQoSMTypeTOSPriorityIndex": es2126PoEplusQoSMTypeTOSPriorityIndex,
       "es2126PoEplusQoSMTypeTOSPriorityValue": es2126PoEplusQoSMTypeTOSPriorityValue,
       "es2126PoEplusQoSMTypeTOSPriorityQueue": es2126PoEplusQoSMTypeTOSPriorityQueue,
       "es2126PoEplusQoSDSCPPriority": es2126PoEplusQoSDSCPPriority,
       "es2126PoEplusQoSDSCPPriorityTable": es2126PoEplusQoSDSCPPriorityTable,
       "es2126PoEplusQoSDSCPPriorityEntry": es2126PoEplusQoSDSCPPriorityEntry,
       "es2126PoEplusQoSDSCPPriorityIndex": es2126PoEplusQoSDSCPPriorityIndex,
       "es2126PoEplusQoSDSCPPriorityValue": es2126PoEplusQoSDSCPPriorityValue,
       "es2126PoEplusQoSDSCPPriorityQueue": es2126PoEplusQoSDSCPPriorityQueue,
       "es2126PoEplusVlan": es2126PoEplusVlan,
       "es2126PoEplusVlanModeConfig": es2126PoEplusVlanModeConfig,
       "es2126PoEplusVlanMode": es2126PoEplusVlanMode,
       "es2126PoEplusSymmetricVlan": es2126PoEplusSymmetricVlan,
       "es2126PoEplusVlanSVL": es2126PoEplusVlanSVL,
       "es2126PoEplusDoubleTag": es2126PoEplusDoubleTag,
       "es2126PoEplusUpLinkPort": es2126PoEplusUpLinkPort,
       "es2126PoEplusTagBasedVlanGroup": es2126PoEplusTagBasedVlanGroup,
       "es2126PoEplusTagBasedVlanNumbers": es2126PoEplusTagBasedVlanNumbers,
       "es2126PoEplusTagBasedCreateStatus": es2126PoEplusTagBasedCreateStatus,
       "es2126PoEplusTagBasedVlanTable": es2126PoEplusTagBasedVlanTable,
       "es2126PoEplusTagBasedVlanEntry": es2126PoEplusTagBasedVlanEntry,
       "es2126PoEplusTagBasedVlanVid": es2126PoEplusTagBasedVlanVid,
       "es2126PoEplusTagBasedVlanName": es2126PoEplusTagBasedVlanName,
       "es2126PoEplusTagBasedVlanMember": es2126PoEplusTagBasedVlanMember,
       "es2126PoEplusTagBasedVlanUntag": es2126PoEplusTagBasedVlanUntag,
       "es2126PoEplusTagBasedVlanRowStatus": es2126PoEplusTagBasedVlanRowStatus,
       "es2126PoEplusVlanPvid": es2126PoEplusVlanPvid,
       "es2126PoEplusVlanPvidTable": es2126PoEplusVlanPvidTable,
       "es2126PoEplusVlanPvidEntry": es2126PoEplusVlanPvidEntry,
       "es2126PoEplusVlanPvidPort": es2126PoEplusVlanPvidPort,
       "es2126PoEplusVlanPvidValue": es2126PoEplusVlanPvidValue,
       "es2126PoEplusVlanPvidDefaultPriority": es2126PoEplusVlanPvidDefaultPriority,
       "es2126PoEplusVlanPvidDropUntag": es2126PoEplusVlanPvidDropUntag,
       "es2126PoEplusPortBasedVlanGroup": es2126PoEplusPortBasedVlanGroup,
       "es2126PoEplusPortBasedVlanNumbers": es2126PoEplusPortBasedVlanNumbers,
       "es2126PoEplusPortBasedCreateStatus": es2126PoEplusPortBasedCreateStatus,
       "es2126PoEplusPortBasedVlanTable": es2126PoEplusPortBasedVlanTable,
       "es2126PoEplusPortBasedVlanEntry": es2126PoEplusPortBasedVlanEntry,
       "es2126PoEplusPortBasedVlanIndex": es2126PoEplusPortBasedVlanIndex,
       "es2126PoEplusPortBasedVlanName": es2126PoEplusPortBasedVlanName,
       "es2126PoEplusPortBasedVlanMember": es2126PoEplusPortBasedVlanMember,
       "es2126PoEplusPortBasedVlanRowStatus": es2126PoEplusPortBasedVlanRowStatus,
       "es2126PoEplusManagementVlan": es2126PoEplusManagementVlan,
       "es2126PoEplusManagementVlanState": es2126PoEplusManagementVlanState,
       "es2126PoEplusManagementVlanVid": es2126PoEplusManagementVlanVid,
       "es2126PoEplusDot1X": es2126PoEplusDot1X,
       "es2126PoEplusDot1XStateSetting": es2126PoEplusDot1XStateSetting,
       "es2126PoEplusRadiusServer": es2126PoEplusRadiusServer,
       "es2126PoEplusDot1XPort": es2126PoEplusDot1XPort,
       "es2126PoEplusSecretKey": es2126PoEplusSecretKey,
       "es2126PoEplusAccountingService": es2126PoEplusAccountingService,
       "es2126PoEplusAccountingServer": es2126PoEplusAccountingServer,
       "es2126PoEplusAccountingPort": es2126PoEplusAccountingPort,
       "es2126PoEplusDot1XPortSecurityManagement": es2126PoEplusDot1XPortSecurityManagement,
       "es2126PoEplusDot1XPortSecurityTable": es2126PoEplusDot1XPortSecurityTable,
       "es2126PoEplusDot1XPortSecurityEntry": es2126PoEplusDot1XPortSecurityEntry,
       "es2126PoEplusDot1XPortSecurityPortIndex": es2126PoEplusDot1XPortSecurityPortIndex,
       "es2126PoEplusDot1XPortSecurityMode": es2126PoEplusDot1XPortSecurityMode,
       "es2126PoEplusDot1XPortSecurityPortControl": es2126PoEplusDot1XPortSecurityPortControl,
       "es2126PoEplusDot1XPortSecurityReAuthMax": es2126PoEplusDot1XPortSecurityReAuthMax,
       "es2126PoEplusDot1XPortSecurityTxPeriod": es2126PoEplusDot1XPortSecurityTxPeriod,
       "es2126PoEplusDot1XPortSecurityQuietPeriod": es2126PoEplusDot1XPortSecurityQuietPeriod,
       "es2126PoEplusDot1XPortSecurityReAuthEnabled": es2126PoEplusDot1XPortSecurityReAuthEnabled,
       "es2126PoEplusDot1XPortSecurityReAuthPeriod": es2126PoEplusDot1XPortSecurityReAuthPeriod,
       "es2126PoEplusDot1XPortSecurityMaxRequest": es2126PoEplusDot1XPortSecurityMaxRequest,
       "es2126PoEplusDot1XPortSecuritySuppTimeout": es2126PoEplusDot1XPortSecuritySuppTimeout,
       "es2126PoEplusDot1XPortSecurityServerTimeout": es2126PoEplusDot1XPortSecurityServerTimeout,
       "es2126PoEplusDot1XPortSecurityStatus": es2126PoEplusDot1XPortSecurityStatus,
       "es2126PoEplusTrunkInfo": es2126PoEplusTrunkInfo,
       "es2126PoEplusTrunkPort": es2126PoEplusTrunkPort,
       "es2126PoEplusTrunkPortTable": es2126PoEplusTrunkPortTable,
       "es2126PoEplusTrunkPortEntry": es2126PoEplusTrunkPortEntry,
       "es2126PoEplusTrunkPortIndex": es2126PoEplusTrunkPortIndex,
       "es2126PoEplusTrunkPortMethod": es2126PoEplusTrunkPortMethod,
       "es2126PoEplusTrunkPortGroup": es2126PoEplusTrunkPortGroup,
       "es2126PoEplusTrunkPortActiveLacp": es2126PoEplusTrunkPortActiveLacp,
       "es2126PoEplusTrunkPortAggtr": es2126PoEplusTrunkPortAggtr,
       "es2126PoEplusTrunkPortStatus": es2126PoEplusTrunkPortStatus,
       "es2126PoEplusTrunkPortCurrentMode": es2126PoEplusTrunkPortCurrentMode,
       "es2126PoEplusAggregatorView": es2126PoEplusAggregatorView,
       "es2126PoEplusAggregatorViewTable": es2126PoEplusAggregatorViewTable,
       "es2126PoEplusAggregatorViewEntry": es2126PoEplusAggregatorViewEntry,
       "es2126PoEplusAggregatorViewIndex": es2126PoEplusAggregatorViewIndex,
       "es2126PoEplusAggregatorViewMethod": es2126PoEplusAggregatorViewMethod,
       "es2126PoEplusAggregatorViewMemberPorts": es2126PoEplusAggregatorViewMemberPorts,
       "es2126PoEplusAggregatorViewReadyPorts": es2126PoEplusAggregatorViewReadyPorts,
       "es2126PoEplusLacpSystemConfiguration": es2126PoEplusLacpSystemConfiguration,
       "es2126PoEplusLacpSystemPriority": es2126PoEplusLacpSystemPriority,
       "es2126PoEplusLacpSystemHashMethod": es2126PoEplusLacpSystemHashMethod,
       "es2126PoEplusTrapEntry": es2126PoEplusTrapEntry,
       "es2126PoEplusModuleInserted": es2126PoEplusModuleInserted,
       "es2126PoEplusModuleRemoved": es2126PoEplusModuleRemoved,
       "es2126PoEplusDualMediaSwapped": es2126PoEplusDualMediaSwapped,
       "es2126PoEplusPoEFailure": es2126PoEplusPoEFailure,
       "es2126PoEplusLoopDetected": es2126PoEplusLoopDetected,
       "es2126PoEplusLoginProtected": es2126PoEplusLoginProtected,
       "es2126PoEplusStpStateDisabled": es2126PoEplusStpStateDisabled,
       "es2126PoEplusStpStateEnabled": es2126PoEplusStpStateEnabled,
       "es2126PoEplusStpTopologyChanged": es2126PoEplusStpTopologyChanged,
       "es2126PoEplusRmonRisingAlarm": es2126PoEplusRmonRisingAlarm,
       "es2126PoEplusRmonFallingAlarm": es2126PoEplusRmonFallingAlarm,
       "es2126PoEplusLacpStateDisabled": es2126PoEplusLacpStateDisabled,
       "es2126PoEplusLacpStateEnabled": es2126PoEplusLacpStateEnabled,
       "es2126PoEplusLacpPortAdded": es2126PoEplusLacpPortAdded,
       "es2126PoEplusLacpPortTrunkFailure": es2126PoEplusLacpPortTrunkFailure,
       "es2126PoEplusGvrpStateDisabled": es2126PoEplusGvrpStateDisabled,
       "es2126PoEplusGvrpStateEnabled": es2126PoEplusGvrpStateEnabled,
       "es2126PoEplusVlanPortBaseEnabled": es2126PoEplusVlanPortBaseEnabled,
       "es2126PoEplusVlanTagBaseEnabled": es2126PoEplusVlanTagBaseEnabled,
       "es2126PoEplusVlanMetroBaseEnabled": es2126PoEplusVlanMetroBaseEnabled,
       "es2126PoEplusUserLogin": es2126PoEplusUserLogin,
       "es2126PoEplusUserLogout": es2126PoEplusUserLogout,
       "es2126PoEplusTrapVariable": es2126PoEplusTrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink,
       "loginProtectInfo": loginProtectInfo,
       "es2126PoEplusPoE": es2126PoEplusPoE,
       "es2126PoEplusPoEStatus": es2126PoEplusPoEStatus,
       "es2126PoEplusPoEStatusVmain": es2126PoEplusPoEStatusVmain,
       "es2126PoEplusPoEStatusImain": es2126PoEplusPoEStatusImain,
       "es2126PoEplusPoEStatusPconsume": es2126PoEplusPoEStatusPconsume,
       "es2126PoEplusPoEStatusPowerLimit": es2126PoEplusPoEStatusPowerLimit,
       "es2126PoEplusPoEStatusTemperature": es2126PoEplusPoEStatusTemperature,
       "es2126PoEplusPoEStatusTable": es2126PoEplusPoEStatusTable,
       "es2126PoEplusPoEStatusEntry": es2126PoEplusPoEStatusEntry,
       "es2126PoEplusPoEStatusPortNum": es2126PoEplusPoEStatusPortNum,
       "es2126PoEplusPoEStatusPortOn": es2126PoEplusPoEStatusPortOn,
       "es2126PoEplusPoEStatusACPortOff": es2126PoEplusPoEStatusACPortOff,
       "es2126PoEplusPoEStatusDCPortOff": es2126PoEplusPoEStatusDCPortOff,
       "es2126PoEplusPoEStatusOverloadPortOff": es2126PoEplusPoEStatusOverloadPortOff,
       "es2126PoEplusPoEStatusShortCircuitPortOff": es2126PoEplusPoEStatusShortCircuitPortOff,
       "es2126PoEplusPoEStatusOverTemperature": es2126PoEplusPoEStatusOverTemperature,
       "es2126PoEplusPoEStatusPowerManagePortOff": es2126PoEplusPoEStatusPowerManagePortOff,
       "es2126PoEplusPoEConfTable": es2126PoEplusPoEConfTable,
       "es2126PoEplusPoEConfEntry": es2126PoEplusPoEConfEntry,
       "es2126PoEplusPoEConfPortNum": es2126PoEplusPoEConfPortNum,
       "es2126PoEplusPoEConfStatus": es2126PoEplusPoEConfStatus,
       "es2126PoEplusPoEConfState": es2126PoEplusPoEConfState,
       "es2126PoEplusPoEConfPriority": es2126PoEplusPoEConfPriority,
       "es2126PoEplusPoEConfPower": es2126PoEplusPoEConfPower,
       "es2126PoEplusPoEConfCurrent": es2126PoEplusPoEConfCurrent,
       "es2126PoEplusPoEConfClass": es2126PoEplusPoEConfClass,
       "es2126PoEplusLoginProtect": es2126PoEplusLoginProtect,
       "es2126PoEplusLockMinutes": es2126PoEplusLockMinutes,
       "es2126PoEplusLoginErrors": es2126PoEplusLoginErrors}
)
