# SNMP MIB module (RUBYTECH-GS2108C-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rubytech/RUBYTECH-GS2108C-MIB
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
_Gs2108cProductID_ObjectIdentity = ObjectIdentity
gs2108cProductID = _Gs2108cProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18)
)
_Gs2108cProduces_ObjectIdentity = ObjectIdentity
gs2108cProduces = _Gs2108cProduces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1)
)
_Gs2108cSystem_ObjectIdentity = ObjectIdentity
gs2108cSystem = _Gs2108cSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1)
)
_Gs2108cCommonSys_ObjectIdentity = ObjectIdentity
gs2108cCommonSys = _Gs2108cCommonSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1)
)


class _Gs2108cReboot_Type(Integer32):
    """Custom type gs2108cReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2108cReboot_Type.__name__ = "Integer32"
_Gs2108cReboot_Object = MibScalar
gs2108cReboot = _Gs2108cReboot_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 1),
    _Gs2108cReboot_Type()
)
gs2108cReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cReboot.setStatus("current")
_Gs2108cBiosVsersion_Type = DisplayString
_Gs2108cBiosVsersion_Object = MibScalar
gs2108cBiosVsersion = _Gs2108cBiosVsersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 2),
    _Gs2108cBiosVsersion_Type()
)
gs2108cBiosVsersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cBiosVsersion.setStatus("current")
_Gs2108cFirmwareVersion_Type = DisplayString
_Gs2108cFirmwareVersion_Object = MibScalar
gs2108cFirmwareVersion = _Gs2108cFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 3),
    _Gs2108cFirmwareVersion_Type()
)
gs2108cFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cFirmwareVersion.setStatus("current")
_Gs2108cHardwareVersion_Type = DisplayString
_Gs2108cHardwareVersion_Object = MibScalar
gs2108cHardwareVersion = _Gs2108cHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 4),
    _Gs2108cHardwareVersion_Type()
)
gs2108cHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cHardwareVersion.setStatus("current")
_Gs2108cMechanicalVersion_Type = DisplayString
_Gs2108cMechanicalVersion_Object = MibScalar
gs2108cMechanicalVersion = _Gs2108cMechanicalVersion_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 5),
    _Gs2108cMechanicalVersion_Type()
)
gs2108cMechanicalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cMechanicalVersion.setStatus("current")
_Gs2108cSeriesNumber_Type = DisplayString
_Gs2108cSeriesNumber_Object = MibScalar
gs2108cSeriesNumber = _Gs2108cSeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 6),
    _Gs2108cSeriesNumber_Type()
)
gs2108cSeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cSeriesNumber.setStatus("current")
_Gs2108cHostMacAddress_Type = DisplayString
_Gs2108cHostMacAddress_Object = MibScalar
gs2108cHostMacAddress = _Gs2108cHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 7),
    _Gs2108cHostMacAddress_Type()
)
gs2108cHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cHostMacAddress.setStatus("current")
_Gs2108cDevicePort_Type = DisplayString
_Gs2108cDevicePort_Object = MibScalar
gs2108cDevicePort = _Gs2108cDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 8),
    _Gs2108cDevicePort_Type()
)
gs2108cDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cDevicePort.setStatus("current")
_Gs2108cRamSize_Type = DisplayString
_Gs2108cRamSize_Object = MibScalar
gs2108cRamSize = _Gs2108cRamSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 9),
    _Gs2108cRamSize_Type()
)
gs2108cRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cRamSize.setStatus("current")
_Gs2108cFlashSize_Type = DisplayString
_Gs2108cFlashSize_Object = MibScalar
gs2108cFlashSize = _Gs2108cFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 1, 10),
    _Gs2108cFlashSize_Type()
)
gs2108cFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cFlashSize.setStatus("current")
_Gs2108cIP_ObjectIdentity = ObjectIdentity
gs2108cIP = _Gs2108cIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2)
)


class _Gs2108cDhcpSetting_Type(Integer32):
    """Custom type gs2108cDhcpSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cDhcpSetting_Type.__name__ = "Integer32"
_Gs2108cDhcpSetting_Object = MibScalar
gs2108cDhcpSetting = _Gs2108cDhcpSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2, 1),
    _Gs2108cDhcpSetting_Type()
)
gs2108cDhcpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDhcpSetting.setStatus("current")
_Gs2108cIPAddress_Type = IpAddress
_Gs2108cIPAddress_Object = MibScalar
gs2108cIPAddress = _Gs2108cIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2, 2),
    _Gs2108cIPAddress_Type()
)
gs2108cIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cIPAddress.setStatus("current")
_Gs2108cNetMask_Type = IpAddress
_Gs2108cNetMask_Object = MibScalar
gs2108cNetMask = _Gs2108cNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2, 3),
    _Gs2108cNetMask_Type()
)
gs2108cNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cNetMask.setStatus("current")
_Gs2108cDefaultGateway_Type = IpAddress
_Gs2108cDefaultGateway_Object = MibScalar
gs2108cDefaultGateway = _Gs2108cDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2, 4),
    _Gs2108cDefaultGateway_Type()
)
gs2108cDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDefaultGateway.setStatus("current")


class _Gs2108cDnsSetting_Type(Integer32):
    """Custom type gs2108cDnsSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cDnsSetting_Type.__name__ = "Integer32"
_Gs2108cDnsSetting_Object = MibScalar
gs2108cDnsSetting = _Gs2108cDnsSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2, 5),
    _Gs2108cDnsSetting_Type()
)
gs2108cDnsSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDnsSetting.setStatus("current")
_Gs2108cDnsServer_Type = IpAddress
_Gs2108cDnsServer_Object = MibScalar
gs2108cDnsServer = _Gs2108cDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 2, 6),
    _Gs2108cDnsServer_Type()
)
gs2108cDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDnsServer.setStatus("current")
_Gs2108cTime_ObjectIdentity = ObjectIdentity
gs2108cTime = _Gs2108cTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3)
)
_Gs2108cSystemCurrentTime_Type = DisplayString
_Gs2108cSystemCurrentTime_Object = MibScalar
gs2108cSystemCurrentTime = _Gs2108cSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 1),
    _Gs2108cSystemCurrentTime_Type()
)
gs2108cSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cSystemCurrentTime.setStatus("current")
_Gs2108cManualTimeSetting_Type = DisplayString
_Gs2108cManualTimeSetting_Object = MibScalar
gs2108cManualTimeSetting = _Gs2108cManualTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 2),
    _Gs2108cManualTimeSetting_Type()
)
gs2108cManualTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cManualTimeSetting.setStatus("current")
_Gs2108cNTPServer_Type = DisplayString
_Gs2108cNTPServer_Object = MibScalar
gs2108cNTPServer = _Gs2108cNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 3),
    _Gs2108cNTPServer_Type()
)
gs2108cNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cNTPServer.setStatus("current")


class _Gs2108cNTPTimeZone_Type(Integer32):
    """Custom type gs2108cNTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Gs2108cNTPTimeZone_Type.__name__ = "Integer32"
_Gs2108cNTPTimeZone_Object = MibScalar
gs2108cNTPTimeZone = _Gs2108cNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 4),
    _Gs2108cNTPTimeZone_Type()
)
gs2108cNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cNTPTimeZone.setStatus("current")


class _Gs2108cNTPTimeSync_Type(Integer32):
    """Custom type gs2108cNTPTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cNTPTimeSync_Type.__name__ = "Integer32"
_Gs2108cNTPTimeSync_Object = MibScalar
gs2108cNTPTimeSync = _Gs2108cNTPTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 5),
    _Gs2108cNTPTimeSync_Type()
)
gs2108cNTPTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cNTPTimeSync.setStatus("current")


class _Gs2108cDaylightSavingTime_Type(Integer32):
    """Custom type gs2108cDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 5),
    )


_Gs2108cDaylightSavingTime_Type.__name__ = "Integer32"
_Gs2108cDaylightSavingTime_Object = MibScalar
gs2108cDaylightSavingTime = _Gs2108cDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 6),
    _Gs2108cDaylightSavingTime_Type()
)
gs2108cDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDaylightSavingTime.setStatus("current")
_Gs2108cDaylightStartTime_Type = DisplayString
_Gs2108cDaylightStartTime_Object = MibScalar
gs2108cDaylightStartTime = _Gs2108cDaylightStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 7),
    _Gs2108cDaylightStartTime_Type()
)
gs2108cDaylightStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDaylightStartTime.setStatus("current")
_Gs2108cDaylightEndTime_Type = DisplayString
_Gs2108cDaylightEndTime_Object = MibScalar
gs2108cDaylightEndTime = _Gs2108cDaylightEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 3, 8),
    _Gs2108cDaylightEndTime_Type()
)
gs2108cDaylightEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDaylightEndTime.setStatus("current")
_Gs2108cAccount_ObjectIdentity = ObjectIdentity
gs2108cAccount = _Gs2108cAccount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4)
)


class _Gs2108cAccountNumber_Type(Integer32):
    """Custom type gs2108cAccountNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2108cAccountNumber_Type.__name__ = "Integer32"
_Gs2108cAccountNumber_Object = MibScalar
gs2108cAccountNumber = _Gs2108cAccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 1),
    _Gs2108cAccountNumber_Type()
)
gs2108cAccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cAccountNumber.setStatus("current")
_Gs2108cAccountTable_Object = MibTable
gs2108cAccountTable = _Gs2108cAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    gs2108cAccountTable.setStatus("current")
_Gs2108cAccountEntry_Object = MibTableRow
gs2108cAccountEntry = _Gs2108cAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 2, 1)
)
gs2108cAccountEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cAccountIndex"),
)
if mibBuilder.loadTexts:
    gs2108cAccountEntry.setStatus("current")


class _Gs2108cAccountIndex_Type(Integer32):
    """Custom type gs2108cAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Gs2108cAccountIndex_Type.__name__ = "Integer32"
_Gs2108cAccountIndex_Object = MibTableColumn
gs2108cAccountIndex = _Gs2108cAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 2, 1, 1),
    _Gs2108cAccountIndex_Type()
)
gs2108cAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cAccountIndex.setStatus("current")
_Gs2108cAccountAuthorization_Type = DisplayString
_Gs2108cAccountAuthorization_Object = MibTableColumn
gs2108cAccountAuthorization = _Gs2108cAccountAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 2, 1, 2),
    _Gs2108cAccountAuthorization_Type()
)
gs2108cAccountAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cAccountAuthorization.setStatus("current")
_Gs2108cAccountName_Type = DisplayString
_Gs2108cAccountName_Object = MibTableColumn
gs2108cAccountName = _Gs2108cAccountName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 2, 1, 3),
    _Gs2108cAccountName_Type()
)
gs2108cAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cAccountName.setStatus("current")
_Gs2108cAccountPassword_Type = DisplayString
_Gs2108cAccountPassword_Object = MibTableColumn
gs2108cAccountPassword = _Gs2108cAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 2, 1, 4),
    _Gs2108cAccountPassword_Type()
)
gs2108cAccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cAccountPassword.setStatus("current")
_Gs2108cAccountAddName_Type = DisplayString
_Gs2108cAccountAddName_Object = MibScalar
gs2108cAccountAddName = _Gs2108cAccountAddName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 3),
    _Gs2108cAccountAddName_Type()
)
gs2108cAccountAddName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cAccountAddName.setStatus("current")
_Gs2108cAccountAddPassword_Type = DisplayString
_Gs2108cAccountAddPassword_Object = MibScalar
gs2108cAccountAddPassword = _Gs2108cAccountAddPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 4),
    _Gs2108cAccountAddPassword_Type()
)
gs2108cAccountAddPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cAccountAddPassword.setStatus("current")


class _Gs2108cDoAccountAdd_Type(Integer32):
    """Custom type gs2108cDoAccountAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cDoAccountAdd_Type.__name__ = "Integer32"
_Gs2108cDoAccountAdd_Object = MibScalar
gs2108cDoAccountAdd = _Gs2108cDoAccountAdd_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 5),
    _Gs2108cDoAccountAdd_Type()
)
gs2108cDoAccountAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDoAccountAdd.setStatus("current")


class _Gs2108cAccountDel_Type(Integer32):
    """Custom type gs2108cAccountDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Gs2108cAccountDel_Type.__name__ = "Integer32"
_Gs2108cAccountDel_Object = MibScalar
gs2108cAccountDel = _Gs2108cAccountDel_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 1, 4, 6),
    _Gs2108cAccountDel_Type()
)
gs2108cAccountDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cAccountDel.setStatus("current")
_Gs2108cSnmp_ObjectIdentity = ObjectIdentity
gs2108cSnmp = _Gs2108cSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2)
)
_Gs2108cGetCommunity_Type = DisplayString
_Gs2108cGetCommunity_Object = MibScalar
gs2108cGetCommunity = _Gs2108cGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 1),
    _Gs2108cGetCommunity_Type()
)
gs2108cGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cGetCommunity.setStatus("current")
_Gs2108cSetCommunity_Type = DisplayString
_Gs2108cSetCommunity_Object = MibScalar
gs2108cSetCommunity = _Gs2108cSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 2),
    _Gs2108cSetCommunity_Type()
)
gs2108cSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSetCommunity.setStatus("current")


class _Gs2108cTrapHostNumber_Type(Integer32):
    """Custom type gs2108cTrapHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2108cTrapHostNumber_Type.__name__ = "Integer32"
_Gs2108cTrapHostNumber_Object = MibScalar
gs2108cTrapHostNumber = _Gs2108cTrapHostNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 3),
    _Gs2108cTrapHostNumber_Type()
)
gs2108cTrapHostNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cTrapHostNumber.setStatus("current")
_Gs2108cTrapHostTable_Object = MibTable
gs2108cTrapHostTable = _Gs2108cTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 4)
)
if mibBuilder.loadTexts:
    gs2108cTrapHostTable.setStatus("current")
_Gs2108cTrapHostEntry_Object = MibTableRow
gs2108cTrapHostEntry = _Gs2108cTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 4, 1)
)
gs2108cTrapHostEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cTrapHostIndex"),
)
if mibBuilder.loadTexts:
    gs2108cTrapHostEntry.setStatus("current")


class _Gs2108cTrapHostIndex_Type(Integer32):
    """Custom type gs2108cTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2108cTrapHostIndex_Type.__name__ = "Integer32"
_Gs2108cTrapHostIndex_Object = MibTableColumn
gs2108cTrapHostIndex = _Gs2108cTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 4, 1, 1),
    _Gs2108cTrapHostIndex_Type()
)
gs2108cTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cTrapHostIndex.setStatus("current")
_Gs2108cTrapHostIP_Type = IpAddress
_Gs2108cTrapHostIP_Object = MibTableColumn
gs2108cTrapHostIP = _Gs2108cTrapHostIP_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 4, 1, 2),
    _Gs2108cTrapHostIP_Type()
)
gs2108cTrapHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cTrapHostIP.setStatus("current")


class _Gs2108cTrapHostPort_Type(Integer32):
    """Custom type gs2108cTrapHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Gs2108cTrapHostPort_Type.__name__ = "Integer32"
_Gs2108cTrapHostPort_Object = MibTableColumn
gs2108cTrapHostPort = _Gs2108cTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 4, 1, 3),
    _Gs2108cTrapHostPort_Type()
)
gs2108cTrapHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cTrapHostPort.setStatus("current")
_Gs2108cTrapHostCommunity_Type = DisplayString
_Gs2108cTrapHostCommunity_Object = MibTableColumn
gs2108cTrapHostCommunity = _Gs2108cTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 2, 4, 1, 4),
    _Gs2108cTrapHostCommunity_Type()
)
gs2108cTrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cTrapHostCommunity.setStatus("current")
_Gs2108cAlarm_ObjectIdentity = ObjectIdentity
gs2108cAlarm = _Gs2108cAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3)
)
_Gs2108cEvent_ObjectIdentity = ObjectIdentity
gs2108cEvent = _Gs2108cEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1)
)


class _Gs2108cEventNumber_Type(Integer32):
    """Custom type gs2108cEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cEventNumber_Type.__name__ = "Integer32"
_Gs2108cEventNumber_Object = MibScalar
gs2108cEventNumber = _Gs2108cEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 1),
    _Gs2108cEventNumber_Type()
)
gs2108cEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cEventNumber.setStatus("current")
_Gs2108cEventTable_Object = MibTable
gs2108cEventTable = _Gs2108cEventTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gs2108cEventTable.setStatus("current")
_Gs2108cEventEntry_Object = MibTableRow
gs2108cEventEntry = _Gs2108cEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2, 1)
)
gs2108cEventEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cEventIndex"),
)
if mibBuilder.loadTexts:
    gs2108cEventEntry.setStatus("current")


class _Gs2108cEventIndex_Type(Integer32):
    """Custom type gs2108cEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cEventIndex_Type.__name__ = "Integer32"
_Gs2108cEventIndex_Object = MibTableColumn
gs2108cEventIndex = _Gs2108cEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2, 1, 1),
    _Gs2108cEventIndex_Type()
)
gs2108cEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cEventIndex.setStatus("current")
_Gs2108cEventName_Type = DisplayString
_Gs2108cEventName_Object = MibTableColumn
gs2108cEventName = _Gs2108cEventName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2, 1, 2),
    _Gs2108cEventName_Type()
)
gs2108cEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cEventName.setStatus("current")


class _Gs2108cEventSendEmail_Type(Integer32):
    """Custom type gs2108cEventSendEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cEventSendEmail_Type.__name__ = "Integer32"
_Gs2108cEventSendEmail_Object = MibTableColumn
gs2108cEventSendEmail = _Gs2108cEventSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2, 1, 3),
    _Gs2108cEventSendEmail_Type()
)
gs2108cEventSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEventSendEmail.setStatus("current")


class _Gs2108cEventSendSMS_Type(Integer32):
    """Custom type gs2108cEventSendSMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cEventSendSMS_Type.__name__ = "Integer32"
_Gs2108cEventSendSMS_Object = MibTableColumn
gs2108cEventSendSMS = _Gs2108cEventSendSMS_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2, 1, 4),
    _Gs2108cEventSendSMS_Type()
)
gs2108cEventSendSMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEventSendSMS.setStatus("current")


class _Gs2108cEventSendTrap_Type(Integer32):
    """Custom type gs2108cEventSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cEventSendTrap_Type.__name__ = "Integer32"
_Gs2108cEventSendTrap_Object = MibTableColumn
gs2108cEventSendTrap = _Gs2108cEventSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 1, 2, 1, 5),
    _Gs2108cEventSendTrap_Type()
)
gs2108cEventSendTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEventSendTrap.setStatus("current")
_Gs2108cEmail_ObjectIdentity = ObjectIdentity
gs2108cEmail = _Gs2108cEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2)
)
_Gs2108cEmailServer_Type = DisplayString
_Gs2108cEmailServer_Object = MibScalar
gs2108cEmailServer = _Gs2108cEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 1),
    _Gs2108cEmailServer_Type()
)
gs2108cEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEmailServer.setStatus("current")
_Gs2108cEmailUsername_Type = DisplayString
_Gs2108cEmailUsername_Object = MibScalar
gs2108cEmailUsername = _Gs2108cEmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 2),
    _Gs2108cEmailUsername_Type()
)
gs2108cEmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEmailUsername.setStatus("current")
_Gs2108cEmailPassword_Type = DisplayString
_Gs2108cEmailPassword_Object = MibScalar
gs2108cEmailPassword = _Gs2108cEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 3),
    _Gs2108cEmailPassword_Type()
)
gs2108cEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEmailPassword.setStatus("current")


class _Gs2108cEmailUserNumber_Type(Integer32):
    """Custom type gs2108cEmailUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2108cEmailUserNumber_Type.__name__ = "Integer32"
_Gs2108cEmailUserNumber_Object = MibScalar
gs2108cEmailUserNumber = _Gs2108cEmailUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 4),
    _Gs2108cEmailUserNumber_Type()
)
gs2108cEmailUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cEmailUserNumber.setStatus("current")
_Gs2108cEmailUserTable_Object = MibTable
gs2108cEmailUserTable = _Gs2108cEmailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    gs2108cEmailUserTable.setStatus("current")
_Gs2108cEmailUserEntry_Object = MibTableRow
gs2108cEmailUserEntry = _Gs2108cEmailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 5, 1)
)
gs2108cEmailUserEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cEmailUserIndex"),
)
if mibBuilder.loadTexts:
    gs2108cEmailUserEntry.setStatus("current")


class _Gs2108cEmailUserIndex_Type(Integer32):
    """Custom type gs2108cEmailUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2108cEmailUserIndex_Type.__name__ = "Integer32"
_Gs2108cEmailUserIndex_Object = MibTableColumn
gs2108cEmailUserIndex = _Gs2108cEmailUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 5, 1, 1),
    _Gs2108cEmailUserIndex_Type()
)
gs2108cEmailUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cEmailUserIndex.setStatus("current")
_Gs2108cEmailUserAddress_Type = DisplayString
_Gs2108cEmailUserAddress_Object = MibTableColumn
gs2108cEmailUserAddress = _Gs2108cEmailUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 2, 5, 1, 2),
    _Gs2108cEmailUserAddress_Type()
)
gs2108cEmailUserAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cEmailUserAddress.setStatus("current")
_Gs2108cSMS_ObjectIdentity = ObjectIdentity
gs2108cSMS = _Gs2108cSMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3)
)
_Gs2108cSMSServer_Type = DisplayString
_Gs2108cSMSServer_Object = MibScalar
gs2108cSMSServer = _Gs2108cSMSServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 1),
    _Gs2108cSMSServer_Type()
)
gs2108cSMSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSMSServer.setStatus("current")
_Gs2108cSMSUsername_Type = DisplayString
_Gs2108cSMSUsername_Object = MibScalar
gs2108cSMSUsername = _Gs2108cSMSUsername_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 2),
    _Gs2108cSMSUsername_Type()
)
gs2108cSMSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSMSUsername.setStatus("current")
_Gs2108cSMSPassword_Type = DisplayString
_Gs2108cSMSPassword_Object = MibScalar
gs2108cSMSPassword = _Gs2108cSMSPassword_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 3),
    _Gs2108cSMSPassword_Type()
)
gs2108cSMSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSMSPassword.setStatus("current")


class _Gs2108cSMSUserNumber_Type(Integer32):
    """Custom type gs2108cSMSUserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2108cSMSUserNumber_Type.__name__ = "Integer32"
_Gs2108cSMSUserNumber_Object = MibScalar
gs2108cSMSUserNumber = _Gs2108cSMSUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 4),
    _Gs2108cSMSUserNumber_Type()
)
gs2108cSMSUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cSMSUserNumber.setStatus("current")
_Gs2108cSMSUserTable_Object = MibTable
gs2108cSMSUserTable = _Gs2108cSMSUserTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    gs2108cSMSUserTable.setStatus("current")
_Gs2108cSMSUserEntry_Object = MibTableRow
gs2108cSMSUserEntry = _Gs2108cSMSUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 5, 1)
)
gs2108cSMSUserEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cSMSUserIndex"),
)
if mibBuilder.loadTexts:
    gs2108cSMSUserEntry.setStatus("current")


class _Gs2108cSMSUserIndex_Type(Integer32):
    """Custom type gs2108cSMSUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Gs2108cSMSUserIndex_Type.__name__ = "Integer32"
_Gs2108cSMSUserIndex_Object = MibTableColumn
gs2108cSMSUserIndex = _Gs2108cSMSUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 5, 1, 1),
    _Gs2108cSMSUserIndex_Type()
)
gs2108cSMSUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cSMSUserIndex.setStatus("current")
_Gs2108cSMSUserMobilePhone_Type = DisplayString
_Gs2108cSMSUserMobilePhone_Object = MibTableColumn
gs2108cSMSUserMobilePhone = _Gs2108cSMSUserMobilePhone_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 3, 3, 5, 1, 2),
    _Gs2108cSMSUserMobilePhone_Type()
)
gs2108cSMSUserMobilePhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSMSUserMobilePhone.setStatus("current")
_Gs2108cTftp_ObjectIdentity = ObjectIdentity
gs2108cTftp = _Gs2108cTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 4)
)
_Gs2108cTftpServer_Type = IpAddress
_Gs2108cTftpServer_Object = MibScalar
gs2108cTftpServer = _Gs2108cTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 4, 1),
    _Gs2108cTftpServer_Type()
)
gs2108cTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cTftpServer.setStatus("current")
_Gs2108cConfiguration_ObjectIdentity = ObjectIdentity
gs2108cConfiguration = _Gs2108cConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5)
)
_Gs2108cSaveRestore_ObjectIdentity = ObjectIdentity
gs2108cSaveRestore = _Gs2108cSaveRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 1)
)


class _Gs2108cSaveStart_Type(Integer32):
    """Custom type gs2108cSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cSaveStart_Type.__name__ = "Integer32"
_Gs2108cSaveStart_Object = MibScalar
gs2108cSaveStart = _Gs2108cSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 1, 1),
    _Gs2108cSaveStart_Type()
)
gs2108cSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSaveStart.setStatus("current")


class _Gs2108cSaveUser_Type(Integer32):
    """Custom type gs2108cSaveUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cSaveUser_Type.__name__ = "Integer32"
_Gs2108cSaveUser_Object = MibScalar
gs2108cSaveUser = _Gs2108cSaveUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 1, 2),
    _Gs2108cSaveUser_Type()
)
gs2108cSaveUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cSaveUser.setStatus("current")


class _Gs2108cRestoreDefault_Type(Integer32):
    """Custom type gs2108cRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2108cRestoreDefault_Type.__name__ = "Integer32"
_Gs2108cRestoreDefault_Object = MibScalar
gs2108cRestoreDefault = _Gs2108cRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 1, 3),
    _Gs2108cRestoreDefault_Type()
)
gs2108cRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cRestoreDefault.setStatus("current")


class _Gs2108cRestoreUser_Type(Integer32):
    """Custom type gs2108cRestoreUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cRestoreUser_Type.__name__ = "Integer32"
_Gs2108cRestoreUser_Object = MibScalar
gs2108cRestoreUser = _Gs2108cRestoreUser_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 1, 4),
    _Gs2108cRestoreUser_Type()
)
gs2108cRestoreUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cRestoreUser.setStatus("current")
_Gs2108cConfigFile_ObjectIdentity = ObjectIdentity
gs2108cConfigFile = _Gs2108cConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 2)
)
_Gs2108cExportConfigName_Type = DisplayString
_Gs2108cExportConfigName_Object = MibScalar
gs2108cExportConfigName = _Gs2108cExportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 2, 1),
    _Gs2108cExportConfigName_Type()
)
gs2108cExportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cExportConfigName.setStatus("current")


class _Gs2108cDoExportConfig_Type(Integer32):
    """Custom type gs2108cDoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2108cDoExportConfig_Type.__name__ = "Integer32"
_Gs2108cDoExportConfig_Object = MibScalar
gs2108cDoExportConfig = _Gs2108cDoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 2, 2),
    _Gs2108cDoExportConfig_Type()
)
gs2108cDoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDoExportConfig.setStatus("current")
_Gs2108cImportConfigName_Type = DisplayString
_Gs2108cImportConfigName_Object = MibScalar
gs2108cImportConfigName = _Gs2108cImportConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 2, 3),
    _Gs2108cImportConfigName_Type()
)
gs2108cImportConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cImportConfigName.setStatus("current")


class _Gs2108cDoImportConfig_Type(Integer32):
    """Custom type gs2108cDoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Gs2108cDoImportConfig_Type.__name__ = "Integer32"
_Gs2108cDoImportConfig_Object = MibScalar
gs2108cDoImportConfig = _Gs2108cDoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 5, 2, 4),
    _Gs2108cDoImportConfig_Type()
)
gs2108cDoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDoImportConfig.setStatus("current")
_Gs2108cDiagnostic_ObjectIdentity = ObjectIdentity
gs2108cDiagnostic = _Gs2108cDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6)
)
_Gs2108cEEPROMTest_Type = DisplayString
_Gs2108cEEPROMTest_Object = MibScalar
gs2108cEEPROMTest = _Gs2108cEEPROMTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 1),
    _Gs2108cEEPROMTest_Type()
)
gs2108cEEPROMTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cEEPROMTest.setStatus("current")
_Gs2108cUartTest_Type = DisplayString
_Gs2108cUartTest_Object = MibScalar
gs2108cUartTest = _Gs2108cUartTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 2),
    _Gs2108cUartTest_Type()
)
gs2108cUartTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cUartTest.setStatus("current")
_Gs2108cDramTest_Type = DisplayString
_Gs2108cDramTest_Object = MibScalar
gs2108cDramTest = _Gs2108cDramTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 3),
    _Gs2108cDramTest_Type()
)
gs2108cDramTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cDramTest.setStatus("current")
_Gs2108cFlashTest_Type = DisplayString
_Gs2108cFlashTest_Object = MibScalar
gs2108cFlashTest = _Gs2108cFlashTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 4),
    _Gs2108cFlashTest_Type()
)
gs2108cFlashTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cFlashTest.setStatus("current")
_Gs2108cInternalLoopbackTest_Type = DisplayString
_Gs2108cInternalLoopbackTest_Object = MibScalar
gs2108cInternalLoopbackTest = _Gs2108cInternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 5),
    _Gs2108cInternalLoopbackTest_Type()
)
gs2108cInternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cInternalLoopbackTest.setStatus("current")
_Gs2108cExternalLoopbackTest_Type = DisplayString
_Gs2108cExternalLoopbackTest_Object = MibScalar
gs2108cExternalLoopbackTest = _Gs2108cExternalLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 6),
    _Gs2108cExternalLoopbackTest_Type()
)
gs2108cExternalLoopbackTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cExternalLoopbackTest.setStatus("current")
_Gs2108cPingTest_Type = DisplayString
_Gs2108cPingTest_Object = MibScalar
gs2108cPingTest = _Gs2108cPingTest_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 6, 7),
    _Gs2108cPingTest_Type()
)
gs2108cPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cPingTest.setStatus("current")
_Gs2108cLog_ObjectIdentity = ObjectIdentity
gs2108cLog = _Gs2108cLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7)
)


class _Gs2108cClearLog_Type(Integer32):
    """Custom type gs2108cClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cClearLog_Type.__name__ = "Integer32"
_Gs2108cClearLog_Object = MibScalar
gs2108cClearLog = _Gs2108cClearLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 1),
    _Gs2108cClearLog_Type()
)
gs2108cClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cClearLog.setStatus("current")


class _Gs2108cUploadLog_Type(Integer32):
    """Custom type gs2108cUploadLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cUploadLog_Type.__name__ = "Integer32"
_Gs2108cUploadLog_Object = MibScalar
gs2108cUploadLog = _Gs2108cUploadLog_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 2),
    _Gs2108cUploadLog_Type()
)
gs2108cUploadLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cUploadLog.setStatus("current")


class _Gs2108cAutoUploadLogState_Type(Integer32):
    """Custom type gs2108cAutoUploadLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cAutoUploadLogState_Type.__name__ = "Integer32"
_Gs2108cAutoUploadLogState_Object = MibScalar
gs2108cAutoUploadLogState = _Gs2108cAutoUploadLogState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 3),
    _Gs2108cAutoUploadLogState_Type()
)
gs2108cAutoUploadLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cAutoUploadLogState.setStatus("current")


class _Gs2108cLogNumber_Type(Integer32):
    """Custom type gs2108cLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Gs2108cLogNumber_Type.__name__ = "Integer32"
_Gs2108cLogNumber_Object = MibScalar
gs2108cLogNumber = _Gs2108cLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 4),
    _Gs2108cLogNumber_Type()
)
gs2108cLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cLogNumber.setStatus("current")
_Gs2108cLogTable_Object = MibTable
gs2108cLogTable = _Gs2108cLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 5)
)
if mibBuilder.loadTexts:
    gs2108cLogTable.setStatus("current")
_Gs2108cLogEntry_Object = MibTableRow
gs2108cLogEntry = _Gs2108cLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 5, 1)
)
gs2108cLogEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cLogIndex"),
)
if mibBuilder.loadTexts:
    gs2108cLogEntry.setStatus("current")


class _Gs2108cLogIndex_Type(Integer32):
    """Custom type gs2108cLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Gs2108cLogIndex_Type.__name__ = "Integer32"
_Gs2108cLogIndex_Object = MibTableColumn
gs2108cLogIndex = _Gs2108cLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 5, 1, 1),
    _Gs2108cLogIndex_Type()
)
gs2108cLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cLogIndex.setStatus("current")
_Gs2108cLogEvent_Type = DisplayString
_Gs2108cLogEvent_Object = MibTableColumn
gs2108cLogEvent = _Gs2108cLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 7, 5, 1, 2),
    _Gs2108cLogEvent_Type()
)
gs2108cLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cLogEvent.setStatus("current")
_Gs2108cFirmware_ObjectIdentity = ObjectIdentity
gs2108cFirmware = _Gs2108cFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 8)
)
_Gs2108cFirmwareFileName_Type = DisplayString
_Gs2108cFirmwareFileName_Object = MibScalar
gs2108cFirmwareFileName = _Gs2108cFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 8, 1),
    _Gs2108cFirmwareFileName_Type()
)
gs2108cFirmwareFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cFirmwareFileName.setStatus("current")


class _Gs2108cDoFirmwareUpgrade_Type(Integer32):
    """Custom type gs2108cDoFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cDoFirmwareUpgrade_Type.__name__ = "Integer32"
_Gs2108cDoFirmwareUpgrade_Object = MibScalar
gs2108cDoFirmwareUpgrade = _Gs2108cDoFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 8, 2),
    _Gs2108cDoFirmwareUpgrade_Type()
)
gs2108cDoFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cDoFirmwareUpgrade.setStatus("current")
_Gs2108cPort_ObjectIdentity = ObjectIdentity
gs2108cPort = _Gs2108cPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9)
)
_Gs2108cPortStatus_ObjectIdentity = ObjectIdentity
gs2108cPortStatus = _Gs2108cPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1)
)


class _Gs2108cPortStatusNumber_Type(Integer32):
    """Custom type gs2108cPortStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cPortStatusNumber_Type.__name__ = "Integer32"
_Gs2108cPortStatusNumber_Object = MibScalar
gs2108cPortStatusNumber = _Gs2108cPortStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 1),
    _Gs2108cPortStatusNumber_Type()
)
gs2108cPortStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusNumber.setStatus("current")
_Gs2108cPortStatusTable_Object = MibTable
gs2108cPortStatusTable = _Gs2108cPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    gs2108cPortStatusTable.setStatus("current")
_Gs2108cPortStatusEntry_Object = MibTableRow
gs2108cPortStatusEntry = _Gs2108cPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1)
)
gs2108cPortStatusEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gs2108cPortStatusEntry.setStatus("current")


class _Gs2108cPortStatusIndex_Type(Integer32):
    """Custom type gs2108cPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cPortStatusIndex_Type.__name__ = "Integer32"
_Gs2108cPortStatusIndex_Object = MibTableColumn
gs2108cPortStatusIndex = _Gs2108cPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 1),
    _Gs2108cPortStatusIndex_Type()
)
gs2108cPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusIndex.setStatus("current")
_Gs2108cPortStatusMedia_Type = DisplayString
_Gs2108cPortStatusMedia_Object = MibTableColumn
gs2108cPortStatusMedia = _Gs2108cPortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 2),
    _Gs2108cPortStatusMedia_Type()
)
gs2108cPortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusMedia.setStatus("current")
_Gs2108cPortStatusLink_Type = DisplayString
_Gs2108cPortStatusLink_Object = MibTableColumn
gs2108cPortStatusLink = _Gs2108cPortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 3),
    _Gs2108cPortStatusLink_Type()
)
gs2108cPortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusLink.setStatus("current")
_Gs2108cPortStatusPortState_Type = DisplayString
_Gs2108cPortStatusPortState_Object = MibTableColumn
gs2108cPortStatusPortState = _Gs2108cPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 4),
    _Gs2108cPortStatusPortState_Type()
)
gs2108cPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusPortState.setStatus("current")
_Gs2108cPortStatusAutoNego_Type = DisplayString
_Gs2108cPortStatusAutoNego_Object = MibTableColumn
gs2108cPortStatusAutoNego = _Gs2108cPortStatusAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 5),
    _Gs2108cPortStatusAutoNego_Type()
)
gs2108cPortStatusAutoNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusAutoNego.setStatus("current")
_Gs2108cPortStatusSpdDpx_Type = DisplayString
_Gs2108cPortStatusSpdDpx_Object = MibTableColumn
gs2108cPortStatusSpdDpx = _Gs2108cPortStatusSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 6),
    _Gs2108cPortStatusSpdDpx_Type()
)
gs2108cPortStatusSpdDpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusSpdDpx.setStatus("current")
_Gs2108cPortStatusFlwCtrl_Type = DisplayString
_Gs2108cPortStatusFlwCtrl_Object = MibTableColumn
gs2108cPortStatusFlwCtrl = _Gs2108cPortStatusFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 7),
    _Gs2108cPortStatusFlwCtrl_Type()
)
gs2108cPortStatusFlwCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusFlwCtrl.setStatus("current")
_Gs2108cPortStatusWaitState_Type = DisplayString
_Gs2108cPortStatusWaitState_Object = MibTableColumn
gs2108cPortStatusWaitState = _Gs2108cPortStatusWaitState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 1, 2, 1, 8),
    _Gs2108cPortStatusWaitState_Type()
)
gs2108cPortStatusWaitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortStatusWaitState.setStatus("current")
_Gs2108cPortConf_ObjectIdentity = ObjectIdentity
gs2108cPortConf = _Gs2108cPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2)
)


class _Gs2108cPortConfNumber_Type(Integer32):
    """Custom type gs2108cPortConfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cPortConfNumber_Type.__name__ = "Integer32"
_Gs2108cPortConfNumber_Object = MibScalar
gs2108cPortConfNumber = _Gs2108cPortConfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 1),
    _Gs2108cPortConfNumber_Type()
)
gs2108cPortConfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortConfNumber.setStatus("current")
_Gs2108cPortConfTable_Object = MibTable
gs2108cPortConfTable = _Gs2108cPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    gs2108cPortConfTable.setStatus("current")
_Gs2108cPortConfEntry_Object = MibTableRow
gs2108cPortConfEntry = _Gs2108cPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2, 1)
)
gs2108cPortConfEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cPortConfIndex"),
)
if mibBuilder.loadTexts:
    gs2108cPortConfEntry.setStatus("current")


class _Gs2108cPortConfIndex_Type(Integer32):
    """Custom type gs2108cPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cPortConfIndex_Type.__name__ = "Integer32"
_Gs2108cPortConfIndex_Object = MibTableColumn
gs2108cPortConfIndex = _Gs2108cPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2, 1, 1),
    _Gs2108cPortConfIndex_Type()
)
gs2108cPortConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cPortConfIndex.setStatus("current")


class _Gs2108cPortConfPortState_Type(Integer32):
    """Custom type gs2108cPortConfPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cPortConfPortState_Type.__name__ = "Integer32"
_Gs2108cPortConfPortState_Object = MibTableColumn
gs2108cPortConfPortState = _Gs2108cPortConfPortState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2, 1, 2),
    _Gs2108cPortConfPortState_Type()
)
gs2108cPortConfPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cPortConfPortState.setStatus("current")


class _Gs2108cPortConfSpdDpx_Type(Integer32):
    """Custom type gs2108cPortConfSpdDpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Gs2108cPortConfSpdDpx_Type.__name__ = "Integer32"
_Gs2108cPortConfSpdDpx_Object = MibTableColumn
gs2108cPortConfSpdDpx = _Gs2108cPortConfSpdDpx_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2, 1, 3),
    _Gs2108cPortConfSpdDpx_Type()
)
gs2108cPortConfSpdDpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cPortConfSpdDpx.setStatus("current")


class _Gs2108cPortConfFlwCtrl_Type(Integer32):
    """Custom type gs2108cPortConfFlwCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cPortConfFlwCtrl_Type.__name__ = "Integer32"
_Gs2108cPortConfFlwCtrl_Object = MibTableColumn
gs2108cPortConfFlwCtrl = _Gs2108cPortConfFlwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2, 1, 4),
    _Gs2108cPortConfFlwCtrl_Type()
)
gs2108cPortConfFlwCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cPortConfFlwCtrl.setStatus("current")


class _Gs2108cPortConfWaitState_Type(Integer32):
    """Custom type gs2108cPortConfWaitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cPortConfWaitState_Type.__name__ = "Integer32"
_Gs2108cPortConfWaitState_Object = MibTableColumn
gs2108cPortConfWaitState = _Gs2108cPortConfWaitState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 9, 2, 2, 1, 5),
    _Gs2108cPortConfWaitState_Type()
)
gs2108cPortConfWaitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cPortConfWaitState.setStatus("current")
_Gs2108cMirror_ObjectIdentity = ObjectIdentity
gs2108cMirror = _Gs2108cMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 10)
)


class _Gs2108cMirrorMode_Type(Integer32):
    """Custom type gs2108cMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cMirrorMode_Type.__name__ = "Integer32"
_Gs2108cMirrorMode_Object = MibScalar
gs2108cMirrorMode = _Gs2108cMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 10, 1),
    _Gs2108cMirrorMode_Type()
)
gs2108cMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cMirrorMode.setStatus("current")


class _Gs2108cMirroringPort_Type(Integer32):
    """Custom type gs2108cMirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cMirroringPort_Type.__name__ = "Integer32"
_Gs2108cMirroringPort_Object = MibScalar
gs2108cMirroringPort = _Gs2108cMirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 10, 2),
    _Gs2108cMirroringPort_Type()
)
gs2108cMirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cMirroringPort.setStatus("current")
_Gs2108cMirroredPorts_Type = DisplayString
_Gs2108cMirroredPorts_Object = MibScalar
gs2108cMirroredPorts = _Gs2108cMirroredPorts_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 10, 3),
    _Gs2108cMirroredPorts_Type()
)
gs2108cMirroredPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cMirroredPorts.setStatus("current")
_Gs2108cMaxPktLen_ObjectIdentity = ObjectIdentity
gs2108cMaxPktLen = _Gs2108cMaxPktLen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11)
)
_Gs2108cMaxPktLen1_ObjectIdentity = ObjectIdentity
gs2108cMaxPktLen1 = _Gs2108cMaxPktLen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11, 1)
)


class _Gs2108cMaxPktLenPortNumber_Type(Integer32):
    """Custom type gs2108cMaxPktLenPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cMaxPktLenPortNumber_Type.__name__ = "Integer32"
_Gs2108cMaxPktLenPortNumber_Object = MibScalar
gs2108cMaxPktLenPortNumber = _Gs2108cMaxPktLenPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11, 1, 1),
    _Gs2108cMaxPktLenPortNumber_Type()
)
gs2108cMaxPktLenPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cMaxPktLenPortNumber.setStatus("current")
_Gs2108cMaxPktLenConfTable_Object = MibTable
gs2108cMaxPktLenConfTable = _Gs2108cMaxPktLenConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    gs2108cMaxPktLenConfTable.setStatus("current")
_Gs2108cMaxPktLenConfEntry_Object = MibTableRow
gs2108cMaxPktLenConfEntry = _Gs2108cMaxPktLenConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11, 1, 2, 1)
)
gs2108cMaxPktLenConfEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cMaxPktLenConfIndex"),
)
if mibBuilder.loadTexts:
    gs2108cMaxPktLenConfEntry.setStatus("current")


class _Gs2108cMaxPktLenConfIndex_Type(Integer32):
    """Custom type gs2108cMaxPktLenConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cMaxPktLenConfIndex_Type.__name__ = "Integer32"
_Gs2108cMaxPktLenConfIndex_Object = MibTableColumn
gs2108cMaxPktLenConfIndex = _Gs2108cMaxPktLenConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11, 1, 2, 1, 1),
    _Gs2108cMaxPktLenConfIndex_Type()
)
gs2108cMaxPktLenConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cMaxPktLenConfIndex.setStatus("current")


class _Gs2108cMaxPktLenConfSetting_Type(Integer32):
    """Custom type gs2108cMaxPktLenConfSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 1518),
        ValueRangeConstraint(1532, 1532),
        ValueRangeConstraint(9216, 9216),
    )


_Gs2108cMaxPktLenConfSetting_Type.__name__ = "Integer32"
_Gs2108cMaxPktLenConfSetting_Object = MibTableColumn
gs2108cMaxPktLenConfSetting = _Gs2108cMaxPktLenConfSetting_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 11, 1, 2, 1, 2),
    _Gs2108cMaxPktLenConfSetting_Type()
)
gs2108cMaxPktLenConfSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cMaxPktLenConfSetting.setStatus("current")
_Gs2108cBandwidth_ObjectIdentity = ObjectIdentity
gs2108cBandwidth = _Gs2108cBandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12)
)
_Gs2108cBandwidth1_ObjectIdentity = ObjectIdentity
gs2108cBandwidth1 = _Gs2108cBandwidth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1)
)


class _Gs2108cBandwidthPortNumber_Type(Integer32):
    """Custom type gs2108cBandwidthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cBandwidthPortNumber_Type.__name__ = "Integer32"
_Gs2108cBandwidthPortNumber_Object = MibScalar
gs2108cBandwidthPortNumber = _Gs2108cBandwidthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 1),
    _Gs2108cBandwidthPortNumber_Type()
)
gs2108cBandwidthPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cBandwidthPortNumber.setStatus("current")
_Gs2108cBandwidthConfTable_Object = MibTable
gs2108cBandwidthConfTable = _Gs2108cBandwidthConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    gs2108cBandwidthConfTable.setStatus("current")
_Gs2108cBandwidthConfEntry_Object = MibTableRow
gs2108cBandwidthConfEntry = _Gs2108cBandwidthConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1)
)
gs2108cBandwidthConfEntry.setIndexNames(
    (0, "RUBYTECH-GS2108C-MIB", "gs2108cBandwidthConfIndex"),
)
if mibBuilder.loadTexts:
    gs2108cBandwidthConfEntry.setStatus("current")


class _Gs2108cBandwidthConfIndex_Type(Integer32):
    """Custom type gs2108cBandwidthConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gs2108cBandwidthConfIndex_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfIndex_Object = MibTableColumn
gs2108cBandwidthConfIndex = _Gs2108cBandwidthConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 1),
    _Gs2108cBandwidthConfIndex_Type()
)
gs2108cBandwidthConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfIndex.setStatus("current")


class _Gs2108cBandwidthConfIgressState_Type(Integer32):
    """Custom type gs2108cBandwidthConfIgressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cBandwidthConfIgressState_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfIgressState_Object = MibTableColumn
gs2108cBandwidthConfIgressState = _Gs2108cBandwidthConfIgressState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 2),
    _Gs2108cBandwidthConfIgressState_Type()
)
gs2108cBandwidthConfIgressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfIgressState.setStatus("current")


class _Gs2108cBandwidthConfIgressBW_Type(Integer32):
    """Custom type gs2108cBandwidthConfIgressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Gs2108cBandwidthConfIgressBW_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfIgressBW_Object = MibTableColumn
gs2108cBandwidthConfIgressBW = _Gs2108cBandwidthConfIgressBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 3),
    _Gs2108cBandwidthConfIgressBW_Type()
)
gs2108cBandwidthConfIgressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfIgressBW.setStatus("current")


class _Gs2108cBandwidthConfStormState_Type(Integer32):
    """Custom type gs2108cBandwidthConfStormState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cBandwidthConfStormState_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfStormState_Object = MibTableColumn
gs2108cBandwidthConfStormState = _Gs2108cBandwidthConfStormState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 4),
    _Gs2108cBandwidthConfStormState_Type()
)
gs2108cBandwidthConfStormState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfStormState.setStatus("current")


class _Gs2108cBandwidthConfStormBW_Type(Integer32):
    """Custom type gs2108cBandwidthConfStormBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Gs2108cBandwidthConfStormBW_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfStormBW_Object = MibTableColumn
gs2108cBandwidthConfStormBW = _Gs2108cBandwidthConfStormBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 5),
    _Gs2108cBandwidthConfStormBW_Type()
)
gs2108cBandwidthConfStormBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfStormBW.setStatus("current")


class _Gs2108cBandwidthConfEgressState_Type(Integer32):
    """Custom type gs2108cBandwidthConfEgressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_Gs2108cBandwidthConfEgressState_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfEgressState_Object = MibTableColumn
gs2108cBandwidthConfEgressState = _Gs2108cBandwidthConfEgressState_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 6),
    _Gs2108cBandwidthConfEgressState_Type()
)
gs2108cBandwidthConfEgressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfEgressState.setStatus("current")


class _Gs2108cBandwidthConfEgressBW_Type(Integer32):
    """Custom type gs2108cBandwidthConfEgressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Gs2108cBandwidthConfEgressBW_Type.__name__ = "Integer32"
_Gs2108cBandwidthConfEgressBW_Object = MibTableColumn
gs2108cBandwidthConfEgressBW = _Gs2108cBandwidthConfEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 12, 1, 2, 1, 7),
    _Gs2108cBandwidthConfEgressBW_Type()
)
gs2108cBandwidthConfEgressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gs2108cBandwidthConfEgressBW.setStatus("current")
_Gs2108cTrapEntry_ObjectIdentity = ObjectIdentity
gs2108cTrapEntry = _Gs2108cTrapEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20)
)
_Gs2108cTrapVariable_ObjectIdentity = ObjectIdentity
gs2108cTrapVariable = _Gs2108cTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 21)
)
_Username_Type = DisplayString
_Username_Object = MibScalar
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 21, 1),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 21, 2),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 21, 3),
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
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 21, 4),
    _Partnerkey_Type()
)
partnerkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerkey.setStatus("current")
_Uplink_Type = DisplayString
_Uplink_Object = MibScalar
uplink = _Uplink_Object(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 21, 5),
    _Uplink_Type()
)
uplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplink.setStatus("current")

# Managed Objects groups


# Notification objects

gs2108cModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 1)
)
gs2108cModuleInserted.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2108cModuleInserted.setStatus(
        "current"
    )

gs2108cModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 2)
)
gs2108cModuleRemoved.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2108cModuleRemoved.setStatus(
        "current"
    )

gs2108cDualMediaSwapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 3)
)
gs2108cDualMediaSwapped.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2108cDualMediaSwapped.setStatus(
        "current"
    )

gs2108cStpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 100)
)
if mibBuilder.loadTexts:
    gs2108cStpStateDisabled.setStatus(
        "current"
    )

gs2108cStpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 101)
)
if mibBuilder.loadTexts:
    gs2108cStpStateEnabled.setStatus(
        "current"
    )

gs2108cStpTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 102)
)
gs2108cStpTopologyChanged.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    gs2108cStpTopologyChanged.setStatus(
        "current"
    )

gs2108cRmonRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 110)
)
if mibBuilder.loadTexts:
    gs2108cRmonRisingAlarm.setStatus(
        "current"
    )

gs2108cRmonFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 111)
)
if mibBuilder.loadTexts:
    gs2108cRmonFallingAlarm.setStatus(
        "current"
    )

gs2108cLacpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 120)
)
gs2108cLacpStateDisabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-GS2108C-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    gs2108cLacpStateDisabled.setStatus(
        "current"
    )

gs2108cLacpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 121)
)
gs2108cLacpStateEnabled.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-GS2108C-MIB", "groupId"))
)
if mibBuilder.loadTexts:
    gs2108cLacpStateEnabled.setStatus(
        "current"
    )

gs2108cLacpPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 123)
)
gs2108cLacpPortAdded.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-GS2108C-MIB", "actorkey"),
        ("RUBYTECH-GS2108C-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    gs2108cLacpPortAdded.setStatus(
        "current"
    )

gs2108cLacpPortTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 124)
)
gs2108cLacpPortTrunkFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUBYTECH-GS2108C-MIB", "actorkey"),
        ("RUBYTECH-GS2108C-MIB", "partnerkey"))
)
if mibBuilder.loadTexts:
    gs2108cLacpPortTrunkFailure.setStatus(
        "current"
    )

gs2108cGvrpStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 140)
)
if mibBuilder.loadTexts:
    gs2108cGvrpStateDisabled.setStatus(
        "current"
    )

gs2108cGvrpStateEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 141)
)
if mibBuilder.loadTexts:
    gs2108cGvrpStateEnabled.setStatus(
        "current"
    )

gs2108cVlanStateDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 150)
)
if mibBuilder.loadTexts:
    gs2108cVlanStateDisabled.setStatus(
        "current"
    )

gs2108cVlanPortBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 151)
)
if mibBuilder.loadTexts:
    gs2108cVlanPortBaseEnabled.setStatus(
        "current"
    )

gs2108cVlanTagBaseEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 152)
)
if mibBuilder.loadTexts:
    gs2108cVlanTagBaseEnabled.setStatus(
        "current"
    )

gs2108cVlanMetroModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 153)
)
gs2108cVlanMetroModeEnabled.setObjects(
    ("RUBYTECH-GS2108C-MIB", "uplink")
)
if mibBuilder.loadTexts:
    gs2108cVlanMetroModeEnabled.setStatus(
        "current"
    )

gs2108cVlanDoubleTagEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 154)
)
if mibBuilder.loadTexts:
    gs2108cVlanDoubleTagEnabled.setStatus(
        "current"
    )

gs2108cUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 200)
)
gs2108cUserLogin.setObjects(
    ("RUBYTECH-GS2108C-MIB", "username")
)
if mibBuilder.loadTexts:
    gs2108cUserLogin.setStatus(
        "current"
    )

gs2108cUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 5205, 2, 18, 1, 20, 201)
)
gs2108cUserLogout.setObjects(
    ("RUBYTECH-GS2108C-MIB", "username")
)
if mibBuilder.loadTexts:
    gs2108cUserLogout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUBYTECH-GS2108C-MIB",
    **{"rubytech": rubytech,
       "switch": switch,
       "gs2108cProductID": gs2108cProductID,
       "gs2108cProduces": gs2108cProduces,
       "gs2108cSystem": gs2108cSystem,
       "gs2108cCommonSys": gs2108cCommonSys,
       "gs2108cReboot": gs2108cReboot,
       "gs2108cBiosVsersion": gs2108cBiosVsersion,
       "gs2108cFirmwareVersion": gs2108cFirmwareVersion,
       "gs2108cHardwareVersion": gs2108cHardwareVersion,
       "gs2108cMechanicalVersion": gs2108cMechanicalVersion,
       "gs2108cSeriesNumber": gs2108cSeriesNumber,
       "gs2108cHostMacAddress": gs2108cHostMacAddress,
       "gs2108cDevicePort": gs2108cDevicePort,
       "gs2108cRamSize": gs2108cRamSize,
       "gs2108cFlashSize": gs2108cFlashSize,
       "gs2108cIP": gs2108cIP,
       "gs2108cDhcpSetting": gs2108cDhcpSetting,
       "gs2108cIPAddress": gs2108cIPAddress,
       "gs2108cNetMask": gs2108cNetMask,
       "gs2108cDefaultGateway": gs2108cDefaultGateway,
       "gs2108cDnsSetting": gs2108cDnsSetting,
       "gs2108cDnsServer": gs2108cDnsServer,
       "gs2108cTime": gs2108cTime,
       "gs2108cSystemCurrentTime": gs2108cSystemCurrentTime,
       "gs2108cManualTimeSetting": gs2108cManualTimeSetting,
       "gs2108cNTPServer": gs2108cNTPServer,
       "gs2108cNTPTimeZone": gs2108cNTPTimeZone,
       "gs2108cNTPTimeSync": gs2108cNTPTimeSync,
       "gs2108cDaylightSavingTime": gs2108cDaylightSavingTime,
       "gs2108cDaylightStartTime": gs2108cDaylightStartTime,
       "gs2108cDaylightEndTime": gs2108cDaylightEndTime,
       "gs2108cAccount": gs2108cAccount,
       "gs2108cAccountNumber": gs2108cAccountNumber,
       "gs2108cAccountTable": gs2108cAccountTable,
       "gs2108cAccountEntry": gs2108cAccountEntry,
       "gs2108cAccountIndex": gs2108cAccountIndex,
       "gs2108cAccountAuthorization": gs2108cAccountAuthorization,
       "gs2108cAccountName": gs2108cAccountName,
       "gs2108cAccountPassword": gs2108cAccountPassword,
       "gs2108cAccountAddName": gs2108cAccountAddName,
       "gs2108cAccountAddPassword": gs2108cAccountAddPassword,
       "gs2108cDoAccountAdd": gs2108cDoAccountAdd,
       "gs2108cAccountDel": gs2108cAccountDel,
       "gs2108cSnmp": gs2108cSnmp,
       "gs2108cGetCommunity": gs2108cGetCommunity,
       "gs2108cSetCommunity": gs2108cSetCommunity,
       "gs2108cTrapHostNumber": gs2108cTrapHostNumber,
       "gs2108cTrapHostTable": gs2108cTrapHostTable,
       "gs2108cTrapHostEntry": gs2108cTrapHostEntry,
       "gs2108cTrapHostIndex": gs2108cTrapHostIndex,
       "gs2108cTrapHostIP": gs2108cTrapHostIP,
       "gs2108cTrapHostPort": gs2108cTrapHostPort,
       "gs2108cTrapHostCommunity": gs2108cTrapHostCommunity,
       "gs2108cAlarm": gs2108cAlarm,
       "gs2108cEvent": gs2108cEvent,
       "gs2108cEventNumber": gs2108cEventNumber,
       "gs2108cEventTable": gs2108cEventTable,
       "gs2108cEventEntry": gs2108cEventEntry,
       "gs2108cEventIndex": gs2108cEventIndex,
       "gs2108cEventName": gs2108cEventName,
       "gs2108cEventSendEmail": gs2108cEventSendEmail,
       "gs2108cEventSendSMS": gs2108cEventSendSMS,
       "gs2108cEventSendTrap": gs2108cEventSendTrap,
       "gs2108cEmail": gs2108cEmail,
       "gs2108cEmailServer": gs2108cEmailServer,
       "gs2108cEmailUsername": gs2108cEmailUsername,
       "gs2108cEmailPassword": gs2108cEmailPassword,
       "gs2108cEmailUserNumber": gs2108cEmailUserNumber,
       "gs2108cEmailUserTable": gs2108cEmailUserTable,
       "gs2108cEmailUserEntry": gs2108cEmailUserEntry,
       "gs2108cEmailUserIndex": gs2108cEmailUserIndex,
       "gs2108cEmailUserAddress": gs2108cEmailUserAddress,
       "gs2108cSMS": gs2108cSMS,
       "gs2108cSMSServer": gs2108cSMSServer,
       "gs2108cSMSUsername": gs2108cSMSUsername,
       "gs2108cSMSPassword": gs2108cSMSPassword,
       "gs2108cSMSUserNumber": gs2108cSMSUserNumber,
       "gs2108cSMSUserTable": gs2108cSMSUserTable,
       "gs2108cSMSUserEntry": gs2108cSMSUserEntry,
       "gs2108cSMSUserIndex": gs2108cSMSUserIndex,
       "gs2108cSMSUserMobilePhone": gs2108cSMSUserMobilePhone,
       "gs2108cTftp": gs2108cTftp,
       "gs2108cTftpServer": gs2108cTftpServer,
       "gs2108cConfiguration": gs2108cConfiguration,
       "gs2108cSaveRestore": gs2108cSaveRestore,
       "gs2108cSaveStart": gs2108cSaveStart,
       "gs2108cSaveUser": gs2108cSaveUser,
       "gs2108cRestoreDefault": gs2108cRestoreDefault,
       "gs2108cRestoreUser": gs2108cRestoreUser,
       "gs2108cConfigFile": gs2108cConfigFile,
       "gs2108cExportConfigName": gs2108cExportConfigName,
       "gs2108cDoExportConfig": gs2108cDoExportConfig,
       "gs2108cImportConfigName": gs2108cImportConfigName,
       "gs2108cDoImportConfig": gs2108cDoImportConfig,
       "gs2108cDiagnostic": gs2108cDiagnostic,
       "gs2108cEEPROMTest": gs2108cEEPROMTest,
       "gs2108cUartTest": gs2108cUartTest,
       "gs2108cDramTest": gs2108cDramTest,
       "gs2108cFlashTest": gs2108cFlashTest,
       "gs2108cInternalLoopbackTest": gs2108cInternalLoopbackTest,
       "gs2108cExternalLoopbackTest": gs2108cExternalLoopbackTest,
       "gs2108cPingTest": gs2108cPingTest,
       "gs2108cLog": gs2108cLog,
       "gs2108cClearLog": gs2108cClearLog,
       "gs2108cUploadLog": gs2108cUploadLog,
       "gs2108cAutoUploadLogState": gs2108cAutoUploadLogState,
       "gs2108cLogNumber": gs2108cLogNumber,
       "gs2108cLogTable": gs2108cLogTable,
       "gs2108cLogEntry": gs2108cLogEntry,
       "gs2108cLogIndex": gs2108cLogIndex,
       "gs2108cLogEvent": gs2108cLogEvent,
       "gs2108cFirmware": gs2108cFirmware,
       "gs2108cFirmwareFileName": gs2108cFirmwareFileName,
       "gs2108cDoFirmwareUpgrade": gs2108cDoFirmwareUpgrade,
       "gs2108cPort": gs2108cPort,
       "gs2108cPortStatus": gs2108cPortStatus,
       "gs2108cPortStatusNumber": gs2108cPortStatusNumber,
       "gs2108cPortStatusTable": gs2108cPortStatusTable,
       "gs2108cPortStatusEntry": gs2108cPortStatusEntry,
       "gs2108cPortStatusIndex": gs2108cPortStatusIndex,
       "gs2108cPortStatusMedia": gs2108cPortStatusMedia,
       "gs2108cPortStatusLink": gs2108cPortStatusLink,
       "gs2108cPortStatusPortState": gs2108cPortStatusPortState,
       "gs2108cPortStatusAutoNego": gs2108cPortStatusAutoNego,
       "gs2108cPortStatusSpdDpx": gs2108cPortStatusSpdDpx,
       "gs2108cPortStatusFlwCtrl": gs2108cPortStatusFlwCtrl,
       "gs2108cPortStatusWaitState": gs2108cPortStatusWaitState,
       "gs2108cPortConf": gs2108cPortConf,
       "gs2108cPortConfNumber": gs2108cPortConfNumber,
       "gs2108cPortConfTable": gs2108cPortConfTable,
       "gs2108cPortConfEntry": gs2108cPortConfEntry,
       "gs2108cPortConfIndex": gs2108cPortConfIndex,
       "gs2108cPortConfPortState": gs2108cPortConfPortState,
       "gs2108cPortConfSpdDpx": gs2108cPortConfSpdDpx,
       "gs2108cPortConfFlwCtrl": gs2108cPortConfFlwCtrl,
       "gs2108cPortConfWaitState": gs2108cPortConfWaitState,
       "gs2108cMirror": gs2108cMirror,
       "gs2108cMirrorMode": gs2108cMirrorMode,
       "gs2108cMirroringPort": gs2108cMirroringPort,
       "gs2108cMirroredPorts": gs2108cMirroredPorts,
       "gs2108cMaxPktLen": gs2108cMaxPktLen,
       "gs2108cMaxPktLen1": gs2108cMaxPktLen1,
       "gs2108cMaxPktLenPortNumber": gs2108cMaxPktLenPortNumber,
       "gs2108cMaxPktLenConfTable": gs2108cMaxPktLenConfTable,
       "gs2108cMaxPktLenConfEntry": gs2108cMaxPktLenConfEntry,
       "gs2108cMaxPktLenConfIndex": gs2108cMaxPktLenConfIndex,
       "gs2108cMaxPktLenConfSetting": gs2108cMaxPktLenConfSetting,
       "gs2108cBandwidth": gs2108cBandwidth,
       "gs2108cBandwidth1": gs2108cBandwidth1,
       "gs2108cBandwidthPortNumber": gs2108cBandwidthPortNumber,
       "gs2108cBandwidthConfTable": gs2108cBandwidthConfTable,
       "gs2108cBandwidthConfEntry": gs2108cBandwidthConfEntry,
       "gs2108cBandwidthConfIndex": gs2108cBandwidthConfIndex,
       "gs2108cBandwidthConfIgressState": gs2108cBandwidthConfIgressState,
       "gs2108cBandwidthConfIgressBW": gs2108cBandwidthConfIgressBW,
       "gs2108cBandwidthConfStormState": gs2108cBandwidthConfStormState,
       "gs2108cBandwidthConfStormBW": gs2108cBandwidthConfStormBW,
       "gs2108cBandwidthConfEgressState": gs2108cBandwidthConfEgressState,
       "gs2108cBandwidthConfEgressBW": gs2108cBandwidthConfEgressBW,
       "gs2108cTrapEntry": gs2108cTrapEntry,
       "gs2108cModuleInserted": gs2108cModuleInserted,
       "gs2108cModuleRemoved": gs2108cModuleRemoved,
       "gs2108cDualMediaSwapped": gs2108cDualMediaSwapped,
       "gs2108cStpStateDisabled": gs2108cStpStateDisabled,
       "gs2108cStpStateEnabled": gs2108cStpStateEnabled,
       "gs2108cStpTopologyChanged": gs2108cStpTopologyChanged,
       "gs2108cRmonRisingAlarm": gs2108cRmonRisingAlarm,
       "gs2108cRmonFallingAlarm": gs2108cRmonFallingAlarm,
       "gs2108cLacpStateDisabled": gs2108cLacpStateDisabled,
       "gs2108cLacpStateEnabled": gs2108cLacpStateEnabled,
       "gs2108cLacpPortAdded": gs2108cLacpPortAdded,
       "gs2108cLacpPortTrunkFailure": gs2108cLacpPortTrunkFailure,
       "gs2108cGvrpStateDisabled": gs2108cGvrpStateDisabled,
       "gs2108cGvrpStateEnabled": gs2108cGvrpStateEnabled,
       "gs2108cVlanStateDisabled": gs2108cVlanStateDisabled,
       "gs2108cVlanPortBaseEnabled": gs2108cVlanPortBaseEnabled,
       "gs2108cVlanTagBaseEnabled": gs2108cVlanTagBaseEnabled,
       "gs2108cVlanMetroModeEnabled": gs2108cVlanMetroModeEnabled,
       "gs2108cVlanDoubleTagEnabled": gs2108cVlanDoubleTagEnabled,
       "gs2108cUserLogin": gs2108cUserLogin,
       "gs2108cUserLogout": gs2108cUserLogout,
       "gs2108cTrapVariable": gs2108cTrapVariable,
       "username": username,
       "groupId": groupId,
       "actorkey": actorkey,
       "partnerkey": partnerkey,
       "uplink": uplink}
)
